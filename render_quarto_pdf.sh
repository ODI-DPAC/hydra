#!/usr/bin/env bash
# Render the quarto book project to a single PDF via Typst.
#
# Quarto's normal `quarto render --to typst` fails on this project with
# "internal error: expected link ancestor in logical tree" -- a bug in
# Typst's tagged-PDF (accessibility) writer, reproduced on Typst 0.14.2
# and 0.15.0, unrelated to this project's content. Typst's own
# `--no-pdf-tags` flag avoids it, but Quarto does not expose that flag,
# so the PDF is produced in two steps: let quarto do the qmd -> .typ
# conversion (keep-typ: true in _quarto.yml keeps the .typ file even
# though quarto's own compile attempt fails), then compile that .typ
# file directly with `typst compile --no-pdf-tags`.
set -euo pipefail

PROJECT_DIR="${1:-HPC_docs/quarto}"

cd "$PROJECT_DIR"
rm -rf _book .quarto index_files index.typ

quarto render --to typst || true

if [ ! -f index.typ ]; then
    echo "ERROR: index.typ was not produced; quarto's pandoc conversion failed." >&2
    exit 1
fi

mkdir -p _book
typst compile --no-pdf-tags index.typ _book/index.pdf

echo "PDF written to $PROJECT_DIR/_book/index.pdf"
