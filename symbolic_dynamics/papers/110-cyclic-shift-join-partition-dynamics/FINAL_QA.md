# Final mechanical QA — P110

QA date: 2026-08-29 UTC.  Scope: only the frozen post-Review-A/B package
`papers/110-cyclic-shift-join-partition-dynamics/`.  This is an internal
artifact freeze, not a novelty, owner-clearance, or external-release
decision.  External status remains **HOLD**.

## Decision and hostile-review closure

**PASS_INTERNAL / HOLD_EXTERNAL.**  `HOSTILE_REVIEW.md` consolidates Review
B's owner/scope repair, abstract narrowing, and P97/P105 collision firewall,
plus Review A's open-problem wording repair and P107/P108/P109/P111 batch
firewall.  Aggregate severity is zero critical, zero mathematical major, one
repaired owner/scope major, and four repaired minors.  There are zero
unresolved mathematical issues.  Final QA required no mathematical source or
verifier edit.

## Exact control

The canonical command

```text
python3 code/verify.py
```

was freshly run with stdout redirected to a temporary file.  `cmp` against
`CONTROL_OUTPUT.txt` exited zero.  Both files have SHA-256
`8b88fb8202b063ee843eb5941ed57a373b8941f1759c5d334447105913d01ab3`.
The canonical header is:

```text
cyclic shift--join partition dynamics exact control: PASS
assertions=1916206
partitions_enumerated=142417
exhaustive_n=1..10
closed_formula_n=1..50
binary_cut_defect_n=3..12
temporal_mobius_and_zeta_period=1..60
```

## Build and determinism

The exact sequence

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

exited zero.  The complete four-stage sequence was repeated.  The PDF hash
before and after that rebuild was identical:

```text
313c9f3584ebb4e38d8c88450b060ec9429f31fe33eb7db2ee1b948936682f3b  main.pdf
```

## Log, text, and bibliography gates

Precise scans of `main.log` and `main.blg` found zero LaTeX/package/pdfTeX or
BibTeX warnings, undefined citations or references, multiply defined labels,
overfull or underfull boxes, fatal errors, and rerun requests.  A broad token
scan found only the loaded package names `infwarerr` and `rerunfilecheck`, the
informational statement that `main.out` had not changed, and BibTeX's summary
`warning$ -- 0`; none is an emitted warning or rerun request.

All four keys in `references.bib` are cited in `main.tex`.  There are zero
uncited bibliography entries and zero cited keys missing from the
bibliography.

Plain `pdftotext` extraction produced 16,448 bytes in 370 lines;
layout-preserving extraction produced 19,535 bytes in 271 lines.  Both are
nonempty and searchable.  Exact scans found none of `??`, `[?]`, `TODO`,
`FIXME`, `[VERIFY]`, or the literal typo `qquad`.  The ordinary word
`verify` appears only in the legitimate filename `code/verify.py` and is not
a placeholder.

## PDF metadata, fonts, and visual inspection

`pdfinfo` reports 5 pages, A4 media size `595.276 x 841.89 pt`, 321,838
bytes, and PDF version 1.5.  The `Author` field is empty; encryption is off,
forms are absent, JavaScript is absent, and page rotation is zero.

`pdffonts` reports 25 entries.  Every entry has `emb=yes`, `sub=yes`, and
`uni=yes`; the failure scan is empty.

All five pages were rendered at 150 dpi and inspected individually.  The
title and abstract, exact iterate and endpoint statements, Möbius--Bell
formula, chord-cycle and two-defect lemmas, complete deepest-shell converse,
control paragraph, narrowed conclusion, and four bibliography entries are
legible.  There is no clipping, overlap, malformed formula or glyph,
accidental blank page, orphaned reference page, or illegible material.

## Freeze boundary

`SHA256SUMS` covers `main.tex`, the bibliography, canonical verifier and
stored stdout, README, claims/control/build ledgers, Reviews A and B and their
consolidated decision, this QA record, and `main.pdf`.  The manifest excludes
itself and generated `aux/log/bbl/blg/out` files.  It was validated with
`sha256sum -c SHA256SUMS`.

Final disposition: **PASS_INTERNAL / HOLD_EXTERNAL**.
