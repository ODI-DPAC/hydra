#!/usr/bin/env python3
"""Append a last-updated line to every page, from git history. Run in CI before the build.
Modifies files in the checkout only; nothing is committed. Delete when Zensical ships native git dates."""
import subprocess, pathlib, sys

docs = pathlib.Path("docs")
n = 0
for md in docs.rglob("*.md"):
    if md == docs / "index.md":
        continue
    date = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(md)],
        capture_output=True, text=True).stdout.strip()
    if not date:
        continue  # untracked file
    text = md.read_text()
    if "<!-- stamped -->" in text:
        continue
    md.write_text(text.rstrip("\n") + f"\n\n---\n<small>Last updated {date}</small>\n<!-- stamped -->\n")
    n += 1
print(f"stamped {n} pages", file=sys.stderr)