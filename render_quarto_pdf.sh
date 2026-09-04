#!/usr/bin/env bash
# Render the "pdf" profile (a book view of the same source files -- see
# _quarto-pdf.yml) to a single consolidated PDF via Typst.
#
# Quarto's normal `quarto render --to typst` fails on this project with
# "internal error: expected link ancestor in logical tree" -- a bug in
# Typst's tagged-PDF (accessibility) writer, reproduced on Typst 0.14.2
# and 0.15.0, unrelated to this project's content. Typst's own
# `--no-pdf-tags` flag avoids it, but Quarto does not expose that flag,
# so the PDF is produced in two steps: let quarto do the md -> .typ
# conversion (keep-typ: true in _quarto-pdf.yml keeps the .typ file even
# though quarto's own compile attempt fails), then compile that .typ
# file directly with `typst compile --no-pdf-tags`.
set -euo pipefail

cd "$(dirname "$0")"

OUT="${1:-assets/documentation.pdf}"

rm -rf _book index_files index.typ

quarto render --profile pdf --to typst || true

if [ ! -f index.typ ]; then
    echo "ERROR: index.typ was not produced; quarto's pandoc conversion failed." >&2
    exit 1
fi

typst compile --no-pdf-tags index.typ "$OUT"
rm -f index.typ

echo "PDF written to $OUT"
