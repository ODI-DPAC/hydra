#!/usr/bin/env python3
"""Stitch the built site into one PDF, in nav order.

    zensical build
    python scripts/build_pdf.py site/hydra-documentation.pdf

Reads mkdocs.yml for the page order and site/ for the rendered pages. Each page
becomes one section with a page break before it; internal links become links
within the PDF; content tabs are flattened so every tab's content is printed
under its label. Needs: pyyaml, beautifulsoup4, weasyprint.
"""
import datetime, pathlib, re, subprocess, sys
from urllib.parse import urljoin, urlparse
import yaml
from bs4 import BeautifulSoup
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else SITE / "hydra-documentation.pdf")

CSS = """
@page { size: A4; margin: 22mm 18mm 20mm 18mm;
        @bottom-center { content: counter(page); font: 9pt sans-serif; color: #75787b; } }
body { font: 10.5pt/1.45 "DejaVu Sans", "Helvetica Neue", Arial, sans-serif; color: #101820; }
h1, h2, h3, h4 { font-weight: 700; line-height: 1.2; page-break-after: avoid; }
h1 { font-size: 22pt; margin: 0 0 12pt; border-bottom: 3px solid #ffcd00; padding-bottom: 6pt; }
h2 { font-size: 15pt; margin: 18pt 0 6pt; }
h3 { font-size: 12pt; margin: 14pt 0 4pt; }
h4 { font-size: 10.5pt; margin: 12pt 0 4pt; }
p, ul, ol, table, pre { margin: 0 0 8pt; }
a { color: #165c7d; text-decoration: none; }
code { font: 9pt "DejaVu Sans Mono", Menlo, monospace; background: #efefef; padding: 0 2pt; border-radius: 2pt; }
pre { background: #f5f5f5; border: 1px solid #d0d7de; border-radius: 3pt; padding: 6pt 8pt;
      white-space: pre-wrap; word-wrap: break-word; page-break-inside: avoid; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; table-layout: auto; width: 100%; font-size: 9.5pt; page-break-inside: avoid; }
th, td { border: 1px solid #d0d7de; padding: 3pt 6pt; text-align: left; vertical-align: top; overflow-wrap: break-word; }
td code, th code { white-space: normal; overflow-wrap: break-word; }
th { background: #efefef; }
img { max-width: 100%; }
.admonition { border-left: 4px solid #75787b; background: #f5f5f5; padding: 6pt 10pt; margin: 8pt 0;
              page-break-inside: avoid; }
.admonition.note, .admonition.info { border-color: #165c7d; background: #eef4f8; }
.admonition.warning { border-color: #d98a00; background: #fff6e5; }
.admonition.danger { border-color: #c0262f; background: #fdeeee; }
.admonition-title { font-weight: 700; margin: 0 0 4pt; }
.tab-label { font-weight: 700; margin: 10pt 0 4pt; }
.page { page-break-before: always; }
.cover { page-break-after: always; padding-top: 60mm; }
.cover .kicker { font-size: 11pt; letter-spacing: .08em; text-transform: uppercase; color: #75787b; }
.cover h1 { font-size: 34pt; border: 0; }
.cover p { color: #333f48; }
.toc { page-break-after: always; }
.toc h1 { font-size: 18pt; }
.toc ul { list-style: none; padding: 0; }
.toc li { margin: 2pt 0; }
.toc li.section { font-weight: 700; margin-top: 8pt; }
.toc li.entry { padding-left: 14pt; }
.toc a::after { content: leader(".") target-counter(attr(href), page); }
.headerlink, .md-content__button, .md-source-file { display: none; }
hr { border: 0; border-top: 1px solid #d0d7de; margin: 14pt 0 6pt; }
"""

def nav_pages(items, section=None, out=None):
    """Flatten mkdocs.yml nav into [(section_title, page_title, path.md)]."""
    out = [] if out is None else out
    for item in items:
        if isinstance(item, str):
            out.append((section, None, item))
        elif isinstance(item, dict):
            (title, value), = item.items()
            if isinstance(value, str):
                out.append((section, title, value))
            else:
                nav_pages(value, title if section is None else section, out)
    return out

def page_url(md):
    """docs path -> site-relative URL (use_directory_urls)."""
    if md == "index.md":
        return ""
    if md.endswith("/index.md"):
        return md[:-len("index.md")]
    return md[:-3] + "/"

def page_id(md):
    return "p-" + re.sub(r"[^a-z0-9]+", "-", page_url(md).lower()).strip("-") or "p-home"

def main():
    class Loose(yaml.SafeLoader):
        pass
    Loose.add_multi_constructor("tag:yaml.org,2002:python/", lambda loader, suffix, node: None)
    cfg = yaml.load((ROOT / "mkdocs.yml").read_text(), Loader=Loose)
    SKIP_SECTIONS = {"News"}
    pages = [p for p in nav_pages(cfg["nav"])
             if p[2] != "index.md" and p[0] not in SKIP_SECTIONS]     # no home page, no news
    known = {page_url(md): page_id(md) for _, _, md in pages}

    try:
        rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                             capture_output=True, text=True).stdout.strip()
    except Exception:
        rev = ""
    today = datetime.date.today().isoformat()

    body, toc, last_section = [], [], None
    for section, title, md in pages:
        html_path = SITE / page_url(md) / "index.html"
        if not html_path.exists():
            print(f"missing {html_path}", file=sys.stderr); continue
        soup = BeautifulSoup(html_path.read_text(), "html.parser")
        art = soup.select_one("article.md-content__inner") or soup.select_one("article")
        if art is None:
            print(f"no article in {html_path}", file=sys.stderr); continue

        for el in art.select(".headerlink, .md-content__button, .md-source-file, script, style"):
            el.decompose()
        for el in art.select("colgroup, col"):
            el.decompose()
        for el in art.select("table, th, td"):
            for attr in ("width", "style"):
                el.attrs.pop(attr, None)
        for ts in art.select(".tabbed-set"):
            labels = [l.get_text(" ", strip=True) for l in ts.select(".tabbed-labels label")]
            blocks = ts.select(".tabbed-content > .tabbed-block")
            repl = soup.new_tag("div")
            for label, block in zip(labels, blocks):
                h = soup.new_tag("p", attrs={"class": "tab-label"}); h.string = label
                repl.append(h); repl.append(block)
            ts.replace_with(repl)
        base = "/" + page_url(md)
        for a in art.select("a[href]"):
            href = a["href"]
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            u = urlparse(urljoin(base, href))
            target = u.path.lstrip("/")
            if target in known:
                a["href"] = "#" + known[target] + (("-" + u.fragment) if u.fragment else "")
            else:
                a["href"] = urljoin(cfg.get("site_url", "/"), u.path.lstrip("/"))
        for img in art.select("img[src]"):
            src = img["src"]
            if not src.startswith(("http://", "https://", "data:")):
                img["src"] = (SITE / urljoin(base, src).lstrip("/")).as_uri()
        # Prefix in-page heading ids so anchors stay unique across pages.
        pid = page_id(md)
        for el in art.select("[id]"):
            el["id"] = f"{pid}-{el['id']}"

        h1 = art.find("h1")
        ptitle = title or (h1.get_text(strip=True) if h1 else md)
        if section != last_section:
            toc.append(f'<li class="section">{section or ""}</li>'); last_section = section
        toc.append(f'<li class="entry"><a href="#{pid}">{ptitle}</a></li>')
        body.append(f'<section class="page" id="{pid}">{art.decode_contents()}</section>')

    doc = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover"><p class="kicker">Smithsonian High Performance Computing</p>
<h1>Hydra</h1>
<p>{cfg.get("site_description", "")}</p>
<p>Generated {today}. The current version is at
<a href="{cfg.get("site_url", "")}">{cfg.get("site_url", "")}</a>.</p></div>
<div class="toc"><h1>Contents</h1><ul>{"".join(toc)}</ul></div>
{"".join(body)}
</body></html>"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=doc, base_url=str(SITE)).write_pdf(str(OUT))
    print(f"wrote {OUT} ({len(body)} pages)")

if __name__ == "__main__":
    main()