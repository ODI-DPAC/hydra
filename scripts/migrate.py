#!/usr/bin/env python3
"""Move Quarto pages from their old paths into the docs/ tree, per migration/map.csv.

map.csv columns:  source, dest, note
  source  old path in the repo (as on main), e.g. reference-pages/available-queues.md
  dest    new path under docs/, e.g. docs/hydra/jobs/queues.md, or DROP
  note    free text
Several rows with the same dest = merge, in row order; the first is git-mv'd
(keeps history), the rest are appended with their headings demoted one level
and git-rm'd. Rows with dest DROP are git-rm'd. Internal links, and links to
confluence.si.edu pages by title, are rewritten via the map.

  python scripts/migrate.py plan                       show what would happen
  python scripts/migrate.py plan --only docs/hydra/jobs
  python scripts/migrate.py apply                      git mv / git rm, convert, fix links, strip stub
  python scripts/migrate.py apply --only docs/hydra/jobs
  python scripts/migrate.py unmapped                   old pages not in the map; stubs with no source
"""
import csv, os, re, subprocess, sys, pathlib
from collections import OrderedDict
from urllib.parse import unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAP = ROOT / "migration" / "map.csv"
CALLOUT = {"note": "note", "tip": "tip", "warning": "warning", "important": "info", "caution": "danger", "info": "info", "danger": "danger"}
# Link label may contain one level of nested brackets, e.g. [hydra-login0[12].si.edu](x.md)
LABEL = r"(?:[^\[\]]|\[[^\]]*\])*"
LINK = re.compile(r"\[(" + LABEL + r")\]\(([^)\s]+)\)")
# Quarto/pandoc fenced-div callouts in any of these shapes, body inline or on its own lines:
#   ::: {.callout-note}      ::: {.note title="Note:"}      ::: callout-warning
CALLOUT_RE = re.compile(
    r'^:{3,} *\{?\.?(?:callout-)?(\w+)(?: +title="([^"]*)")?\}? *\n?(.*?)\n? *:{3,} *$',
    flags=re.S | re.M)
# Links into the Confluence space by page title, either URL form.
CONFLUENCE = re.compile(r"^https?://confluence\.si\.edu/(?:display/HPC/|spaces/HPC/pages/\d+/)([^#?]+)")
# Confluence titles that were renamed before the Quarto export: old title slug -> Quarto path.
ALIASES = {
    "2021-cluster-upgrade": "cluster-upgrades/2021-cluster-upgrade-to-hydra-6.md",
}

def sh(*args):
    return subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True).stdout

def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", unquote(title).replace("+", " ").lower()).strip("-")

def load_map():
    groups = OrderedDict()
    with open(MAP, newline="") as f:
        for row in csv.DictReader(f):
            src = (row.get("source") or "").strip()
            if not src or src.startswith("#"):
                continue
            groups.setdefault(row["dest"].strip(), []).append(src)
    old2new = {s: d for d, ss in groups.items() for s in ss}
    # Quarto filename stem -> old path, for resolving Confluence title links. Ambiguous stems are unusable.
    by_stem = {}
    for s in old2new:
        by_stem.setdefault(pathlib.Path(s).stem, []).append(s)
    slug2old = {k: v[0] for k, v in by_stem.items() if len(v) == 1}
    slug2old.update(ALIASES)
    return groups, old2new, slug2old

def fix_links(text, source, dest, old2new, slug2old, unresolved):
    """Rewrite internal links from the source's old location to paths relative to dest."""
    src_dir = os.path.dirname(source)
    dest_dir = os.path.dirname(dest)
    def one(m):
        label, target = m.group(1), m.group(2)
        c = CONFLUENCE.match(target)
        if c:
            old = slug2old.get(slug(c.group(1)))
            anchor = ""                                   # Confluence anchors do not survive
            if old is None:
                unresolved.append((source, target)); return m.group(0)
        elif re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        else:
            path, _, anchor = target.partition("#")
            if not path.endswith((".md", ".qmd")):
                return m.group(0)
            old = os.path.normpath(os.path.join(src_dir, path))
        new = old2new.get(old)
        if new is None:
            unresolved.append((source, target)); return m.group(0)
        if new == "DROP":
            return label
        if new == dest:
            return f"[{label}](#{anchor})" if anchor else label
        rel = os.path.relpath(new, dest_dir)
        return f"[{label}]({rel}#{anchor})" if anchor else f"[{label}]({rel})"
    return LINK.sub(one, text)

def strip_self_toc(text, source, dest, old2new):
    """Drop the Confluence page TOC: a leading run of list items that all link to this page."""
    src_dir = os.path.dirname(source)
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith("# ")):
        out.append(lines[i]); i += 1
    j = i
    while j < len(lines):
        m = re.match(r"^\s*(?:\d+\.|-|\*)\s+\[" + LABEL + r"\]\(([^)#\s]+)", lines[j])
        if not m:
            break
        if old2new.get(os.path.normpath(os.path.join(src_dir, m.group(1)))) != dest:
            break
        j += 1
    if j - i >= 2:
        i = j
    return "\n".join(out + lines[i:])

def callout(mm):
    kind = CALLOUT.get(mm.group(1).lower(), "note")
    ttl = (mm.group(2) or "").strip().rstrip(":").strip()
    ttl = f' "{ttl}"' if ttl and ttl.lower() != kind else ""
    body = "\n".join(("    " + l) if l.strip() else "" for l in mm.group(3).strip().splitlines())
    return f"!!! {kind}{ttl}\n{body}\n"

def demote(text):
    """Push every markdown heading down one level."""
    return re.sub(r"^(#{1,5}) ", r"#\1 ", text, flags=re.M)

def convert(text, source, dest, old2new, slug2old, unresolved):
    """Quarto -> Zensical markdown."""
    m = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    title = None
    if m:
        t = re.search(r"^title:\s*(.+)$", m.group(1), flags=re.M)
        title = t.group(1).strip().strip('"\'') if t else None
        text = text[m.end():]
    if title:
        # Quarto keeps the title in front matter and uses H1 for sections. Make the
        # title the only H1: drop a leading H1 that repeats it, demote the rest.
        text = re.sub(r"\A\s*# +" + re.escape(title) + r" *\n", "", text, flags=re.I)
        if re.search(r"^# ", text, flags=re.M):
            text = demote(text)
        text = f"# {title}\n\n{text.lstrip()}"
    text = strip_self_toc(text, source, dest, old2new)
    text = re.sub(r"!\[\([^)]*\)\]\(https://confluence\.si\.edu/[^)]*\)\s*", "", text)   # emoticons
    text = re.sub(r"^(#+) +\d+(?:\.\d+)*\.? +", r"\1 ", text, flags=re.M)               # Confluence heading numbers
    text = CALLOUT_RE.sub(callout, text)
    depth = len(pathlib.Path(dest).relative_to("docs").parts) - 1
    text = re.sub(r"\]\((?:\.\./)*assets/", "](" + "../" * depth + "assets/", text)
    text = re.sub(r"\{\{<.*?>\}\}\n?", "", text)
    text = fix_links(text, source, dest, old2new, slug2old, unresolved)
    return text.rstrip("\n") + "\n"

def strip_stub(text):
    return re.sub(r'!!! warning "Not yet migrated"\n(?:    .*\n?)*\n?<!--.*?-->\n?', "", text, flags=re.S)

def plan(groups, only=None):
    for dest, sources in groups.items():
        if only and not dest.startswith(only):
            continue
        if dest == "DROP":
            for s in sources:
                print(f"DROP\n    rm  {s}{'' if (ROOT / s).exists() else '   [MISSING]'}")
            continue
        print(dest)
        for s in sources:
            print(f"    {'mv ' if s == sources[0] else 'add'} {s}{'' if (ROOT / s).exists() else '   [MISSING]'}")

def apply(groups, old2new, slug2old, only=None):
    unresolved = []
    for dest, sources in groups.items():
        if only and not dest.startswith(only):
            continue
        if dest == "DROP":
            for s in sources:
                if (ROOT / s).exists():
                    sh("git", "rm", "-q", s); print(f"drop {s}")
            continue
        if not all((ROOT / s).exists() for s in sources):
            print(f"skip {dest}: a source is missing (run plan)"); continue
        dpath = ROOT / dest
        stub_title = None
        if dpath.exists():
            h = re.search(r"^# (.+)$", dpath.read_text(), flags=re.M)
            stub_title = h.group(1) if h else None
            dpath.unlink()
        dpath.parent.mkdir(parents=True, exist_ok=True)
        sh("git", "mv", sources[0], dest)
        body = convert(dpath.read_text(), sources[0], dest, old2new, slug2old, unresolved)
        for extra in sources[1:]:
            more = convert((ROOT / extra).read_text(), extra, dest, old2new, slug2old, unresolved)
            body += "\n" + demote(more)
            sh("git", "rm", "-q", extra)
        if stub_title:
            body = re.sub(r"^# .+$", f"# {stub_title}", body, count=1, flags=re.M)
        dpath.write_text(strip_stub(body))
        sh("git", "add", dest)
        print(f"done {dest}  <- {', '.join(sources)}")
    if unresolved:
        print("\nlinks not in map (left as-is):")
        for s, t in unresolved:
            print(f"    {s}: {t}")

def unmapped(groups):
    mapped = {s for ss in groups.values() for s in ss}
    # Quarto pages are lowercase slugs; capitalized names (README, CONTRIBUTING) are repo docs, not pages.
    old = [p for p in sh("git", "ls-files", "*.md", "*.qmd").splitlines()
           if not p.startswith("docs/") and not pathlib.Path(p).name[0].isupper()]
    print("old pages not in map:")
    for p in old:
        if p not in mapped: print("   ", p)
    print("stubs with no source:")
    for p in sorted((ROOT / "docs").rglob("*.md")):
        if '"Not yet migrated"' in p.read_text() and str(p.relative_to(ROOT)) not in groups:
            print("   ", p.relative_to(ROOT))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    g, o2n, s2o = load_map()
    {"plan": lambda: plan(g, only), "apply": lambda: apply(g, o2n, s2o, only), "unmapped": lambda: unmapped(g)}[cmd]()