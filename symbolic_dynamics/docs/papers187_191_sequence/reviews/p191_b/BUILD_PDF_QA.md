# P191 Review B — source-only build and PDF QA

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

- SHA-256: `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`
- bytes: `380787`
- pages: `4`
- page box: `A4 / 595.276 x 841.89 pt`
- PDF version: `1.5`

Byte comparisons:

- cold build vs `main_round1.pdf`: `PASS`
- cold build vs `main_round2.pdf`: `PASS`
- cold build vs live `main.pdf`: `PASS`

## Mechanical checks

- `pdffonts`: `28/28` embedded, `28/28` subsetted, `28/28` Unicode mapped.
- `pdftotext`: `330` lines / `12397` bytes.
- Extracted markers include `global target-path recurrence`, `CRediT roles`,
  `HOLD_EXTERNAL`, and `References`.
- Final `main.log`: no LaTeX/package warning, undefined citation/reference,
  rerun request, overfull/underfull box, fatal error, or emergency stop.

This is artifact QA only. A reproducible PDF hash does not itself prove the
mathematics and does not relax `OWNER_AMBER / HOLD_EXTERNAL`.
