# Contributing

Every page has an edit icon that opens it on GitHub. Small fixes: edit there and open a pull request. Larger changes: clone, `mkdocs serve`, edit, PR.

## Conventions

- One topic per page. If a page needs more than three H2 sections, split it.
- Imperative headings: "Submit a job", not "Job submission".
- Every command in a code block, copy-pasteable, with the prompt omitted. Show output in a separate block when it matters.
- Prefer admonitions (`!!! note`, `!!! warning`, `!!! tip`) over bold sentences.
- Link with relative paths to `.md` files. Never link to a URL on this site.
- Do not add "Last updated" lines. The build stamps every page from git.
- Do not hand-edit generated tables (module lists, hardware limits). Rerun the script.
- No screenshots of terminal output; paste the text. Screenshots are fine for GUIs (Globus, RStudio).
- Names of queues, paths, modules and commands in backticks.
- Dated notices go at the top of the current year in `docs/news/index.md`: bold date, one to three sentences, link to the page with the details. Never edit an old entry to describe a new change; add a new one.

## Adding a page

1. Create the file under the right directory.
2. Add it to `nav` in `mkdocs.yml` (the build warns if you forget).
3. `mkdocs build --strict` must pass.

## Removing or renaming a page

Add the old path to `redirect_maps` in `mkdocs.yml` so old links keep working.
