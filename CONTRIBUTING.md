# Contributing

Thanks for helping us make these documents better. The site is Markdown under `docs/`, built with [Zensical](https://zensical.org/docs/).

## Fixing a page

For a typo, a wrong flag or a dead link: open the page on the site, click the edit icon by the title, make the change on GitHub, open a pull request. The build check runs; when it's green, merge it.

For anything larger, work locally so you can see the result:

```bash
git clone git@github.com:ODI-DPAC/hydra.git && cd hydra
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
git checkout -b my-change
zensical serve                # http://localhost:8000, rebuilds when you save
```

When it looks right, `zensical build --strict` (this is what CI runs; it fails on a broken link or a page missing from the nav), then push and open a pull request against `main`.

## How we write

The model is [docs.nersc.gov](https://docs.nersc.gov/). Write the way a senior HPC person explains the system to a capable colleague: plain, specific, complete, and unhurried. Here is a short page written that way:

````markdown
# Recover a file from a snapshot

A **snapshot** is a read-only copy of a filesystem taken at a fixed time. `/home` keeps snapshots
for 4 weeks and `/data` for 2 weeks, under a hidden `.snapshot` directory at the top of each
partition, so a file you deleted or overwrote in that time is still there.

1. List the snapshots:

    ```console
    $ ls /data/genomics/.snapshot
    hourly.2026-09-15_1005  hourly.2026-09-15_1105  weekly.2026-09-14_0015
    ```

2. Copy the file back from the snapshot you want. `-p` keeps the file's dates, and `-i` asks before
   overwriting anything:

    ```bash
    cp -pi /data/genomics/.snapshot/hourly.2026-09-15_1105/USERNAME/analysis/results.csv /data/genomics/USERNAME/analysis/
    ```

!!! warning "`/scratch` has no snapshots"

    A file deleted from `/scratch` cannot be recovered this way. See [Scrubbed files and restores](scrubber.md).

## Further reading

- [Backups](backups.md) for what protects against a failure of the storage system itself
````

What to take from it:

- **Start with what the thing is.** One sentence, then the procedure. Put a term the reader may not know in bold the first time.
- **Short sentences, one idea each.** If you find yourself joining two thoughts with a semicolon or a colon, make them two sentences.
- **Say why.** A rule without its reason reads as arbitrary; "`-i` asks before overwriting" is enough.
- **"We" is the HPC team and "you" is the reader.** Tell people what to do in the imperative ("copy the file"), and it is fine to say "please" and to use contractions.
- **Commands as a sentence, then the command, then the output** if there is any. Numbered steps only when the order matters.
- **Limits, quotas and versions live on the reference pages**, in tables. Elsewhere, link to them rather than repeating the number.
- **Write enough that a first-time user finishes the task on this page**, screenshots included. For analysis software, cover what is specific to Hydra and link the package's own manual for the rest.
- **Admonitions** are for things the reader must not miss: the message is the title, the body is a line or two. `warning` for things that cost time or data, `danger` for something irreversible, `note` for an aside.
- **Code blocks have a language** (`bash` for a command, `console` for a prompt and its output, `text` for raw output), and commands, paths, flags and hostnames in prose are in backticks. Placeholders are `USERNAME` and `JOBID`.
- **Long pages end with "Further reading"**, three or four links with a few words each on why.

Things we don't do: open a page with "This page covers…", write "currently" or "as of" (it dates the page), say "click here", or use em dashes.

Content tabs (`=== "macOS and Linux"`) are for the same procedure on different systems, as on the login page. Tables are for anything with the same fields on every row. Images only for things that are visual, with alt text, under `docs/assets/`. Section names in the nav, and the H1 of each section's index page, are in Title Case ("Running Jobs"). Page titles and the headings inside a page are in sentence case ("Submit a job array").

## Important to keep in mind

- A hand-typed "Last updated" line is not necessary. The build adds one from git.
- A new page must be in `nav` in `mkdocs.yml` (the strict build catches this) or must be linked from its section's index page.

## News and the banner

To announce something, file an "Admin team - News item" issue from the Issues tab. Give the date, one to three sentences, a page to link if there is one, and whether to show a banner. A pull request appears within a minute. Approve and merge it.

For maintenance, give the downtime start and end. The status pill on the home page turns to "Down for maintenance" only during that window. An outage starts now.

A banner with an end time comes down by itself the morning after. A banner without one comes down when you file an "Admin team - Remove banner" issue. That form has an optional closing line, which is added to the News entry. There is one banner at a time, and a new one replaces the old.

The same thing by hand is `python scripts/add_news.py --date YYYY-MM-DD --text "…"`, with `--link PAGE`, `--banner maintenance --from "YYYY-MM-DD HH:MM" --until "YYYY-MM-DD HH:MM"` as needed, or `--clear-banner --note "…"`. Then a pull request. Entries live on `docs/news/index.md`, newest year first, one bold date per entry with an `<a id="YYYY-MM-DD">` anchor. `scripts/build_home_news.py` copies the newest three to the home page and runs in CI.

## Generated files

Don't edit these by hand; run the script and commit the result.

| File | Script | Where to run it |
|---|---|---|
| `docs/software/module-list.md` | `scripts/gen_module_list.sh` | a Hydra login node |
| News card on `docs/index.md` | `scripts/build_home_news.py` | anywhere |
| "Last updated" line on each page | `scripts/stamp_dates.py` | CI only; never commit its output |

A weekly check on the cluster compares `module-list.md` with the module tree and mails SI-HPC-Admin when they differ, with the regenerated file saved under `/home/hpc/cron/check-module-list/`. Copy that file over `docs/software/module-list.md` on a branch and open a PR.
