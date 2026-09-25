#!/usr/bin/env python3
"""Add a News entry, and optionally set or clear the announcement banner.

  python scripts/add_news.py --date 2026-10-07 --text "Hydra is down for maintenance on ..." \
      [--link jobs/queues.md] [--banner maintenance|outage|info --until 2026-10-08]
  python scripts/add_news.py --clear-banner

Writes docs/news/index.md (newest entry at the top of its year, creating the year
heading if needed), mkdocs.yml (extra.announce), and refreshes the home page card
by running scripts/build_home_news.py. Commit the result through a pull request.
"""
import argparse, datetime, pathlib, re, subprocess, sys

NEWS = pathlib.Path("docs/news/index.md")
CONF = pathlib.Path("mkdocs.yml")

def add_entry(date, text, link):
    d = datetime.date.fromisoformat(date)
    anchor = d.isoformat()
    label = f"{d.strftime('%B')} {d.day}."
    text = text.strip().rstrip(".") + "."
    if link:
        link = link.strip()
        if not re.match(r"https?://", link):
            link = "../" + link.lstrip("/")          # news/index.md -> docs root
        text += f" See [details]({link})."
    entry = f'<a id="{anchor}"></a>**{label}** {text}'
    src = NEWS.read_text()
    if f'<a id="{anchor}"></a>' in src:
        sys.exit(f"an entry for {anchor} already exists; edit docs/news/index.md by hand")
    year_head = f"## {d.year}"
    if year_head in src:
        src = src.replace(year_head + "\n", year_head + "\n\n" + entry + "\n", 1)
    else:
        # new year goes above the first existing year heading
        m = re.search(r"^## \d{4}\s*$", src, re.M)
        if not m:
            sys.exit("no '## YYYY' heading found in docs/news/index.md")
        src = src[:m.start()] + year_head + "\n\n" + entry + "\n\n" + src[m.start():]
    NEWS.write_text(src)
    print(f"added: {entry[:80]}...")
    return anchor

def set_banner(kind, text, link, until):
    conf = CONF.read_text()
    def sub(key, value):
        nonlocal conf
        pat = rf"(^  announce:\n(?:    .*\n)*?    {key}:)[^\n]*"
        if not re.search(pat, conf, re.M):
            conf = re.sub(r"(^  announce:\n)", rf"\1    {key}: {value}\n", conf, count=1, flags=re.M)
        else:
            conf = re.sub(pat, rf"\1 {value}", conf, count=1, flags=re.M)
    sub("kind", kind)
    sub("text", '"' + text.replace('"', "'") + '"')
    sub("link", link)
    sub("until", until if until else '""')
    CONF.write_text(conf)
    print("banner:", kind, "until", until or "cleared by hand")

def clear_banner():
    set_banner("info", "", "news/", "")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--date"); p.add_argument("--text"); p.add_argument("--link", default="")
    p.add_argument("--banner", choices=["maintenance", "outage", "info"])
    p.add_argument("--until", help="YYYY-MM-DD; the banner clears itself after this date")
    p.add_argument("--clear-banner", action="store_true")
    a = p.parse_args()
    if a.clear_banner:
        clear_banner()
    else:
        if not (a.date and a.text):
            p.error("--date and --text are required")
        anchor = add_entry(a.date, a.text, a.link)
        if a.banner:
            first = re.split(r"(?<=[.!?])\s", a.text.strip(), maxsplit=1)[0]
            set_banner(a.banner, first, f"news/#{anchor}", a.until)
    subprocess.run([sys.executable, "scripts/build_home_news.py"], check=True)

if __name__ == "__main__":
    main()
