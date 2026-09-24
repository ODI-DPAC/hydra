# Contributing

Thanks for helping us make these documents better. The site is Markdown under `docs/`, built with [Zensical](https://zensical.org/docs/).

## Fixing a page

For a typo, a wrong flag or a dead link: open the page on the site, click the edit icon by the title, make the change on GitHub, open a pull request. The build check runs; when it's green, merge it.

For anything larger, work locally so you can see the result:

```bash
git clone git@github.com:Smithsonian/hydra.git && cd hydra
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
git checkout -b my-change
zensical serve                # http://localhost:8000, rebuilds when you save
```

When it looks right, `zensical build --strict` (this is what CI runs; it fails on a broken link or a page missing from the nav), then push and open a pull request against `main`.

## What a page looks like

Here is a short page written the way we want the whole site to read:

````markdown
# Recover a file from a snapshot

`/home` and `/data` keep hourly and weekly snapshots for two weeks. This page covers copying back
a file you have deleted or overwritten.

Snapshots are read-only copies under a hidden `.snapshot` directory at the top of each filesystem.

1. List the snapshots:

```console
    $ ls /data/genomics/.snapshot
    hourly.2026-09-15_1005  hourly.2026-09-15_1105  weekly.2026-09-14_0015
```

2. Copy the file back from the snapshot you want:

```bash
    cp -pi /data/genomics/.snapshot/hourly.2026-09-15_1105/USERNAME/analysis/results.csv /data/genomics/USERNAME/analysis/
```

!!! warning "`/scratch` has no snapshots"

    A file deleted from `/scratch` cannot be recovered. See [Scrubber](scrubber.md).
````

The things to copy from it:

- **The title is the task or the thing**, in sentence case. "Recover a file from a snapshot", not "Snapshots and how to use them".
- **The first paragraph says what the page covers.** Two sentences.
- **Second person, imperative, present tense.** "Copy the file", not "the user should copy the file"; "the scheduler starts the job", not "the job will be started".
- **Steps are a numbered list, one action each, with the command in a code block.** Explanation is prose. Bullets are for lists of things. A paragraph should not be five nested bullets.
- **Code blocks have a language.** `bash` for a command, `console` for a prompt and its output (with `$` as the prompt, so the copy button copies only the command), `text` for raw output. Every command, path, flag, hostname and queue name in prose is in backticks. Placeholders are `USERNAME`, `JOBID`, in capitals.
- **An admonition when the reader must not miss something, with the message as its title.** `warning` for things that cost time or data, `note` for an aside, `danger` for irreversible loss. Body one or two lines.
- **Numbers and versions live in tables, not prose.** "macOS 15", not "newer versions of macOS". Node counts, quotas and limits are on the reference pages; link there rather than repeating them.
- **Link text says where the link goes.** "See [Scrubber](scrubber.md)", never "click here".
- **Don't document upstream software.** How conda or Globus works is their manual's job. Write what's Hydra-specific: paths, queues, modules, what breaks here.

Content tabs (`=== "macOS and Linux"`) are for the same procedure on different systems, as on the login page. Tables are for anything with the same fields on every row. Images only for things that are visual, with alt text, under `docs/assets/`.

## Important to keep in mind

- A hand-typed "Last updated" line is not necessary. The build adds one from git.
- A new page must be in `nav` in `mkdocs.yml` (the strict build catches this) or must be linked from its section's index page.

## News and announcements

News is one page, `docs/news/index.md`, newest first under `## YYYY`. An entry is one paragraph, and its first sentence has to stand on its own because the home page shows only that:

```markdown
<a id="2025-12-16"></a>**December 16.** The RStudio server was upgraded to a newer OS and R. See [RStudio](../interactive/rstudio.md).
```

Don't rewrite old entries; add new ones. After editing, run `python scripts/build_home_news.py` so the home page card matches (CI runs it too, so forgetting only affects your preview).

The yellow banner at the top of every page and the status pill on the home page come from one block in `mkdocs.yml`:

```yaml
extra:
  announce:
    kind: maintenance     # maintenance | outage | info
    text: "Hydra is down for scheduled maintenance Tue Oct 7, 08:00 to 17:00 ET."
    link: news/#2026-10-07
```

Blank `text` means no banner and a green pill. Change it in a PR and add the matching News entry in the same PR.

## Generated files

Don't edit these by hand; run the script and commit the result.

| File | Script | Where to run it |
|---|---|---|
| `docs/software/module-list.md` | `scripts/gen_module_list.sh` | a Hydra login node |
| News card on `docs/index.md` | `scripts/build_home_news.py` | anywhere |
| "Last updated" line on each page | `scripts/stamp_dates.py` | CI only; never commit its output |

A weekly check on the cluster compares `module-list.md` with the module tree and mails SI-HPC-Admin when they differ, with the regenerated file saved under `/home/hpc/cron/check-module-list/`. Copy that file over `docs/software/module-list.md` on a branch and open a PR.