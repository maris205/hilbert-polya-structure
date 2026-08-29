# Final mechanical QA — P108

QA date: 2026-08-29 UTC.  Scope: only the frozen post-Review-B package
`papers/108-capped-fibonacci-dynamics/`.  This is an internal artifact
freeze, not a novelty, owner-clearance, or external-release decision.
External status remains **HOLD**.

## Decision and review closure

**PASS_INTERNAL / HOLD_EXTERNAL.**  `HOSTILE_REVIEW.md` faithfully
consolidates Reviews A and B: Review A's P83/P89/P101 historical firewall;
Review B's removal of the invalid real-interval semiring wording; and Review
B's P107/P109/P110/P111 within-batch firewall.  Across both reviews there
were zero critical or major findings and three repaired minors.  No theorem
formula or verifier code required a final-QA edit.

## Exact control

The canonical verifier was freshly run as

```text
python3 code/verify_capped_fibonacci.py
```

with stdout redirected to a temporary file.  `cmp` against
`code/verification_output.txt` exited zero.  Both files have SHA-256
`ca2e3c6f0bb312544ec08921416fb39eb2293e2d547e67bca2ae383e802aa48c`.
The exact stored result is:

```text
capped Fibonacci dynamics exact control: PASS
assertions=67475970
states_checked=3622410
trajectory_formula_checks=60226906
fibre_formula_checks=3622410
caps=a=1..220
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
610f893fc1bfb6d393777e90f048eefcfa7780789ee9d5b6ddd7d0cd38446c23  main.pdf
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

Plain `pdftotext` extraction produced 8,291 bytes in 212 lines;
layout-preserving extraction produced 10,420 bytes in 152 lines.  Both are
nonempty and searchable.  Neither contains `??`, `[?]`, `TODO`, `FIXME`,
`VERIFY`, or the literal typo `qquad`.

## PDF metadata, fonts, and visual inspection

`pdfinfo` reports 3 pages, A4 media size `595.276 x 841.89 pt`, 269,786
bytes, and PDF version 1.5.  The `Author` field is empty; encryption is off,
forms are absent, JavaScript is absent, and page rotation is zero.

`pdffonts` reports 21 entries.  Every entry has `emb=yes`, `sub=yes`, and
`uni=yes`; the failure scan is empty.

All three pages were rendered at 150 dpi and inspected individually.  The
long title, exact iterate, clipping identity, recurrent/depth/CDF statements,
Fibonacci plateau wording, inverse-fibre display, historical and within-batch
firewalls, conclusion, and four bibliography entries are legible.  There is
no clipping, overlap, malformed formula or glyph, accidental blank page, or
orphaned bibliography material.

## Freeze boundary

`SHA256SUMS` covers the manuscript, bibliography, canonical verifier and
stored stdout, README, author self-check, evidence/control/build ledgers,
Reviews A and B and their consolidated decision, this QA record, and
`main.pdf`.  The manifest excludes itself and generated
`aux/log/bbl/blg/out` files.  It was validated with
`sha256sum -c SHA256SUMS`.

Final disposition: **PASS_INTERNAL / HOLD_EXTERNAL**.
