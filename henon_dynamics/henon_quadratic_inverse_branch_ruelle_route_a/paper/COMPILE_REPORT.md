# C141 compile report

## Accepted artifact

- Source: `main.tex`, SHA-256 `d87ad2b720e4263cfec761e17dedf018fb57b12707aff744a9eaeb92eaf1a75d`.
- Final PDF: `main.pdf`, 349,293 bytes, 2 pages, PDF 1.5.
- Final PDF SHA-256: `d23d87e351622821834fdd6fac6fe6117b0ba602167939e0251442ad0fbfe948`.
- `main_round2.pdf` is byte-identical to `main.pdf`.

## Deterministic build

Two fresh isolated directories received only the accepted `main.tex`. Each was compiled with

```bash
SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir="$build_dir" "$build_dir/main.tex"
```

Both output hashes were
`d23d87e351622821834fdd6fac6fe6117b0ba602167939e0251442ad0fbfe948`, and `cmp` returned success. Generated auxiliary files remained outside the package.

## Round preservation

- Round 0: `a3356c041f7e7b805d1e56c5a42310c6f85948dbfc064c9d4d4d7a208025a04d`.
- Round 1: `81818dad1d58a12de15dfbd189e4d72f4b50144824d0e9051ec036e42ba0c9d7`.
- Round 2/final: `d23d87e351622821834fdd6fac6fe6117b0ba602167939e0251442ad0fbfe948`.

The concrete theorem, orbit-regrouping, convergence-language, and typography edits are recorded in `../PAPER_IMPROVEMENT_LOG.md`. These are internal construction audits, not external peer review.

## Mechanical audit

- Final `main.log` scan: zero `Warning`, `Overfull`, `Underfull`, `undefined`, or `multiply defined` matches.
- `pdffonts`: every listed font is embedded and subsetted; all report Unicode mapping.
- Plain `pdftotext`: title, theorem, both numbered equations, all exact values, tuple, and nonclaims are extractable.
- Extracted-text SHA-256: `ed0b59be31effc750da3f7105afd4b5fe30a87a792337056a4b0bd815cd3cc7e`.
- Two pages were rasterized at 150 dpi and inspected at original detail. No clipping, collision, missing glyph, spill, blank page, or unreadably small exact fraction was observed.
- The four long degree-five/six fractions were separated from the compact degree-one/four table after the round-1 visual audit.

Status: **PASS — deterministic, embedded-font, warning-free, and visually accepted**.
