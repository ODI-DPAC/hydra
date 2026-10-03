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
  jobs/               the scheduler, job files, queues, limits, monitoring, hardware
  interactive/        qrsh, Jupyter, VS Code, RStudio
  storage/            filesystems, quotas, snapshots, the scrubber, /store, backups
  software/           modules, languages, GPUs, containers, compilers, guides/
  data-transfer/      scp and rsync, Globus, rclone
  policies/           usage policies, citing, getting help, status
  news/               index.md is the current year, history.md older notices, upgrades/ one page per upgrade
  stylesheets/        extra.css: SI palette, home page, content tabs
  assets/             images
overrides/            main.html: announcement bar and status pill
scripts/              add_news.py, build_home_news.py, build_pdf.py, stamp_dates.py, gen_module_list.sh (see CONTRIBUTING.md)
migration/            map.csv: where every page of the old site went
```

The nav in `mkdocs.yml` is independent of the directory tree. The site is served under `/hydra/`, so the docs tree is flat.

## Branches

`main` is the site. Every change is a branch and a pull request. The `build` check must pass.

Writing conventions are in CONTRIBUTING.md.
