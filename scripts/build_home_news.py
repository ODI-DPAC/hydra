#!/usr/bin/env python3
"""Copy the newest three News entries into the home page card.
Entries are paragraphs on docs/news/index.md that start with a bold date:
  **December 16.** text...        (under a ## YYYY heading)
Links are reduced to their text. Run after editing News; also runs in CI."""
import re, pathlib

news = pathlib.Path("docs/news/index.md").read_text()
home = pathlib.Path("docs/index.md")

entries, year = [], None
for line in news.splitlines():
    m = re.match(r"##\s+(\d{4})\s*$", line)
    if m:
        year = m.group(1)
        continue
    m = re.match(r"(?:<a id=\"[^\"]*\"></a>)?\*\*([A-Za-z]+ \d{1,2})\.\*\*\s*(.+)", line)
    if m and year:
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(2))   # [text](link) -> text
        text = re.sub(r"`([^`]+)`", r"\1", text)                       # drop code ticks
        first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]        # first sentence only
        entries.append(f"**{m.group(1)}, {year}.** {first}")
    if len(entries) == 3:
        break

block = "<!-- news:start -->\n" + "\n\n".join(entries) + "\n<!-- news:end -->"
src = home.read_text()
new = re.sub(r"<!-- news:start -->.*?<!-- news:end -->", block, src, flags=re.S)
if new != src:
    home.write_text(new)
    print(f"home page news updated ({len(entries)} entries)")
else:
    print("home page news already current")