# P190 Review B — source-only build and PDF QA

## Result

`PASS / SOURCE_ONLY_BUILD / ROUND1_HASH_REPRODUCED`

Review B copied only `main.tex` and `references.bib` into a fresh temporary
directory and ran:

```bash
SOURCE_DATE_EPOCH=1704067200 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1704067200 TZ=UTC bibtex main
SOURCE_DATE_EPOCH=1704067200 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1704067200 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled cold-build artifact is:

- SHA-256: `81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d`
- bytes: `383748`
- pages: `4`
- page box: `A4 / 595.276 x 841.89 pt`
- PDF version: `1.5`

Byte comparisons:

- cold build vs `main_round1.pdf`: `PASS`
- cold build vs `main_round2.pdf`: `PASS`
- cold build vs live `main.pdf`: `PASS`

## Mechanical checks

- `pdffonts`: `29/29` embedded, `29/29` subsetted, `29/29` Unicode mapped.
- `pdftotext`: `340` lines / `13165` bytes.
- Extracted markers include `good-run normal form`, `zero-fibre spectrum`,
  `CRediT`, `HOLD_EXTERNAL`, and `References`.
- Final `main.log`: no LaTeX/package warning, undefined citation/reference,
  rerun request, overfull/underfull box, fatal error, or emergency stop.

This is artifact QA only. A reproducible PDF hash does not itself prove the
mathematics and does not relax `OWNER_AMBER / HOLD_EXTERNAL`.
