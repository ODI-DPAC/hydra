# Hydra documentation

User documentation for Hydra, the Smithsonian Institution HPC cluster. Built with [Zensical](https://zensical.org/docs/) and published to GitHub Pages.

## Local preview

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
zensical serve          # http://localhost:8000, rebuilds on save
zensical build --strict # what CI runs; fails on broken links and missing pages
```

## Layout

```
docs/
  index.md            home page
  getting-started/    account, login, quick start, training
  hydra/              everything specific to the Hydra cluster
    jobs/ hardware/ interactive/ storage/ software/
  data-transfer/      scp and rsync, Globus, rclone
  policies/           usage policies, citing, help, FAQ, status
  news/               index.md is the current year, history.md older notices, upgrades/ one page per upgrade
  stylesheets/        extra.css: SI palette, home page, content tabs
  assets/             images
overrides/            main.html: announcement bar and status pill
scripts/              build_home_news.py, stamp_dates.py, gen_module_list.sh (see CONTRIBUTING.md)
migration/            map.csv: where every page of the old site went
```

The nav in `mkdocs.yml` is independent of the directory tree. `hydra/` is a URL prefix so a second platform can be added later as a sibling directory and a new tab without moving files.

## Branches

`main` is the site. Every change is a branch and a pull request; the `build` check must pass. 

Writing conventions are in CONTRIBUTING.md.
