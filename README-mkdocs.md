# Hydra documentation

User documentation for Hydra, the Smithsonian Institution HPC cluster. Built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and published to GitHub Pages on every push to `main`.

## Local preview

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000, live reload
mkdocs build --strict # what CI runs; fails on broken links
```

## Layout

```
docs/
  index.md            landing page
  getting-started/    shared across platforms: account, login, quick start, citing
  hydra/              everything specific to the Hydra cluster
    jobs/ interactive/ storage/ software/ hardware/
  data-transfer/      shared: scp, Globus, rclone
  policies/           shared: policies, help, FAQ, status
  news/               blog plugin; posts/ holds dated notices, upgrades/ holds upgrade pages
scripts/              gen_module_list.sh regenerates the module table from the cluster
audit/                content-audit.csv: every Confluence page and where it went
```

The nav in `mkdocs.yml` is independent of the directory tree. `hydra/` is a URL prefix so a second platform can be added later as a sibling directory and a new tab, without moving files.

## Before first deploy

Search the repo for `REPLACE_ME`:

- `mkdocs.yml`: `site_url`, `repo_url`, `repo_name`, `extra.status_url`, social link
- `docs/assets/favicon.png` is a placeholder; replace with a real PNG
- GitHub repo settings → Pages → Source: `gh-pages` branch, `/ (root)`

## Migration status

`audit/content-audit.csv` tracks every source page. Stub pages carry a "Not yet migrated" box that names their source section and page number in the February 2026 Confluence export. Delete the box when the page is done and set `done` in the CSV.

See CONTRIBUTING.md for writing conventions.
