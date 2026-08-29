# Final mechanical QA — P107

QA date: 2026-08-29 UTC.  Scope: only the frozen package
`papers/107-annihilator-power-ideal-dynamics/`.  This is an internal artifact
freeze, not an external-release or novelty decision.  External status remains
**HOLD**.

## Decision

**PASS_INTERNAL / HOLD_EXTERNAL.**  No mathematical source edit was required.
The canonical verifier, deterministic LaTeX build, PDF metadata, fonts,
searchable text, bibliography closure, and page images all passed.

## Exact control

The canonical command was run with stdout redirected to a fresh temporary
file:

```text
python3 code/verify_annihilator_power.py
```

`cmp` against `code/verification_output.txt` exited zero.  Both files have
SHA-256
`0ad8903f24d032b94daaf4d2cb77295ee9e14cd2c50a0ed9705dd17b4fce2fd3`.
The stored result is:

```text
annihilator-power ideal dynamics exact control: PASS
assertions=212843
coordinate_states=29880
literal_divisor_ideal_states=49476
coordinate_grid=r=2..10, a=1..80
literal_moduli=N=2..1000, r=2..8
```

## Build and determinism

The exact sequence

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

exited zero.  The complete four-stage sequence was then repeated.  The PDF
hash before and after that deterministic rebuild was identical:

```text
76ea9249f290657d83d7ceeed2ba2ddad12d95b7c6b2f4f2142ff417f46b6c39  main.pdf
```

## Log and bibliography gates

Precise scans of `main.log` and `main.blg` found zero:

- LaTeX, package, or pdfTeX warnings;
- undefined citations or references;
- multiply defined labels;
- overfull or underfull boxes;
- fatal/errors or rerun requests;
- BibTeX warnings or syntax failures.

A broad token scan found only the loaded package names `infwarerr` and
`rerunfilecheck`, the informational statement that `main.out` had not
changed, and BibTeX's summary `warning$ -- 0`; none is an emitted warning or
rerun request.

All five keys in `references.bib` are cited in `main.tex`.  There are zero
uncited bibliography entries, zero cited keys missing from the bibliography,
and no unresolved bibliography marker.

## PDF metadata and fonts

`pdfinfo` reports:

- 4 pages;
- A4 media box, `595.276 x 841.89 pt`;
- 271,211 bytes and PDF version 1.5;
- an empty `Author` field;
- `Encrypted: no`, `Form: none`, `JavaScript: no`, and page rotation zero.

`pdffonts` reports 23 font entries.  Every entry has `emb=yes`, `sub=yes`,
and `uni=yes`; the failure scan is empty.

## Searchable text and visual inspection

Plain `pdftotext` extraction produced 10,208 bytes in 311 lines;
layout-preserving extraction produced 13,646 bytes in 211 lines.  Both are
nonempty and searchable.  Neither contains `??`, `[?]`, `TODO`, `FIXME`,
`VERIFY`, or the literal typo `qquad`.

All four pages were rendered at 150 dpi and inspected individually.  The
title/abstract, clipped-reflection and deviation displays, parity-sensitive
depth formula, floor/ceiling CDF, CRT fixed-count and zeta displays,
collision/HOLD language, and DOI-bearing references are legible.  There is
no clipping, overlap, malformed glyph or equation, accidental blank page,
or orphaned bibliography material.

## Freeze boundary

`SHA256SUMS` covers the manuscript, bibliography, verifier and stored stdout,
README/evidence/control/build ledgers, both hostile reviews and their
consolidated decision, this QA record, and `main.pdf`.  Generated auxiliary
files and `SHA256SUMS` itself are intentionally excluded.  The manifest was
validated with `sha256sum -c SHA256SUMS`.

Final disposition: **PASS_INTERNAL / HOLD_EXTERNAL**.
