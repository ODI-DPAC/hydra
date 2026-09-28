#!/usr/bin/env python3
"""Add a News entry and/or set the announcement banner; or take the banner down.

  python scripts/add_news.py --date 2026-10-07 --text "..." [--link jobs/queues.md]
      [--banner maintenance|outage|info] [--from "2026-10-07 08:00"] [--until "2026-10-07 12:00"]
      [--no-news] [--issue 42]
  python scripts/add_news.py --clear-banner [--note "Hydra is back in service as of 3 pm."]

Times are Eastern, "YYYY-MM-DD HH:MM" or "YYYY-MM-DD" (00:00). They are stored in
mkdocs.yml as ISO 8601 with the UTC offset, which the page's script and the expiry
job read. Writes docs/news/index.md (newest entry at the top of its year),
mkdocs.yml (extra.announce), and refreshes the home card. Commit through a PR.
"""
import argparse, datetime, pathlib, re, subprocess, sys
from zoneinfo import ZoneInfo

NEWS = pathlib.Path("docs/news/index.md")
CONF = pathlib.Path("mkdocs.yml")
TZ = ZoneInfo("America/New_York")

def iso(s):
    """'2026-10-07 08:00' or '2026-10-07' (Eastern) -> '2026-10-07T08:00:00-04:00'."""
    if not s: return ""
    s = s.strip().replace("T", " ")
    fmt = "%Y-%m-%d %H:%M" if " " in s else "%Y-%m-%d"
    return datetime.datetime.strptime(s, fmt).replace(tzinfo=TZ).isoformat()

def add_entry(date, text, link):
    d = datetime.date.fromisoformat(date)
    anchor = d.isoformat()
    text = text.strip().rstrip(".") + "."
    if link:
        link = link.strip()
        if not re.match(r"https?://", link):
            link = "../" + link.lstrip("/")
        text += f" See [details]({link})."
    entry = f'<a id="{anchor}"></a>**{d.strftime("%B")} {d.day}.** {text}'
    src = NEWS.read_text()
    if f'<a id="{anchor}"></a>' in src:
        sys.exit(f"an entry for {anchor} already exists; edit docs/news/index.md by hand")
    year_head = f"## {d.year}"
    if year_head in src:
        src = src.replace(year_head + "\n", year_head + "\n\n" + entry + "\n", 1)
    else:
        m = re.search(r"^## \d{4}\s*$", src, re.M)
        if not m: sys.exit("no '## YYYY' heading found in docs/news/index.md")
        src = src[:m.start()] + year_head + "\n\n" + entry + "\n\n" + src[m.start():]
    NEWS.write_text(src)
    print(f"added: {entry[:80]}...")
    return anchor

def append_note(note):
    """Append a closing note to the entry the banner links to, or add a dated entry."""
    conf = CONF.read_text()
    m = re.search(r"^  announce:\n(?:    .*\n)*?    link: news/#(\d{4}-\d{2}-\d{2})", conf, re.M)
    src = NEWS.read_text()
    note = note.strip().rstrip(".") + "."
    if m and f'<a id="{m.group(1)}"></a>' in src:
        tag = f'<a id="{m.group(1)}"></a>'
        i = src.index(tag); j = src.index("\n", i)
        src = src[:j] + " " + note + src[j:]
        NEWS.write_text(src); print("note appended to", m.group(1))
    else:
        add_entry(datetime.datetime.now(TZ).date().isoformat(), note, "")

def set_banner(kind, text, link, start, until, issue):
    conf = CONF.read_text()
    def sub(key, value):
        nonlocal conf
        pat = rf"(^  announce:\n(?:    .*\n)*?    {key}:)[^\n]*"
        if re.search(pat, conf, re.M):
            conf = re.sub(pat, rf"\1 {value}", conf, count=1, flags=re.M)
        else:
            conf = re.sub(r"(^  announce:\n)", rf"\1    {key}: {value}\n", conf, count=1, flags=re.M)
    sub("kind", kind)
    sub("text", '"' + text.replace('"', "'") + '"')
    sub("link", link)
    sub("from", f'"{start}"'); sub("until", f'"{until}"')
    sub("since", f'"{datetime.datetime.now(TZ).date().isoformat()}"' if text else '""')
    sub("issue", f'"{issue}"' if text and issue else '""')
    CONF.write_text(conf)
    print("banner:", kind or "cleared", start or "", until or "")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--date"); p.add_argument("--text"); p.add_argument("--link", default="")
    p.add_argument("--banner", choices=["maintenance", "outage", "info"])
    p.add_argument("--from", dest="start", default=""); p.add_argument("--until", default="")
    p.add_argument("--no-news", action="store_true", help="banner only; no News entry")
    p.add_argument("--issue", default="")
    p.add_argument("--clear-banner", action="store_true"); p.add_argument("--note", default="")
    a = p.parse_args()
    if a.clear_banner:
        if a.note: append_note(a.note)
        set_banner("info", "", "news/", "", "", "")
    else:
        if not a.text: p.error("--text is required")
        if a.no_news:
            link = "news/" if not a.link else a.link
        else:
            if not a.date: p.error("--date is required unless --no-news")
            link = "news/#" + add_entry(a.date, a.text, a.link)
        if a.banner:
            first = re.split(r"(?<=[.!?])\s", a.text.strip(), maxsplit=1)[0]
            start = iso(a.start) if a.start else (datetime.datetime.now(TZ).replace(second=0, microsecond=0).isoformat() if a.banner == "outage" else "")
            set_banner(a.banner, first, link, start, iso(a.until), a.issue)
    subprocess.run([sys.executable, "scripts/build_home_news.py"], check=True)

if __name__ == "__main__":
    main()
