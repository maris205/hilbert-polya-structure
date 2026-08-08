# HCS-C21 compilation report

**Date:** 2026-08-08
**Target:** `paper/main.pdf`
**Build status:** PASS

## Reproducible build

From `paper/`:

```bash
lualatex --version
fc-match "Droid Sans Fallback"
latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The release build used:

- LuaHBTeX 1.14.0 from TeX Live 2022;
- latexmk 4.76;
- `Droid Sans Fallback` Regular for the Traditional-Chinese abstract; and
- Latin Modern plus the bundled AMS fonts elsewhere.

## PDF ledger

| Field | Value |
|---|---|
| Pages | 17 |
| Page size | A4, 595.276 x 841.89 pt |
| File size | 304,240 bytes |
| PDF version | 1.5 |
| SHA-256 | `984ad0bc7cd0fe8840ce6a6f442dd377f930127e28836137ca814a2dd30847e1` |
| Source freshness | no `.tex` or `.bib` file newer than the PDF |

## Quality gates

- build exit status: PASS;
- undefined references or citations: 0;
- missing characters: 0;
- overfull boxes: 0;
- embedded fonts: all listed fonts embedded and subsetted;
- PDF metadata: title, author placeholder, subject, and keywords present;
- visual inspection: title/dual abstracts on page 1, quotient diamond and
  cohomology theorem on page 9, and reproducibility appendix on page 15;
- bibliography: all 12 cite keys resolve and all 12 entries are used.

The log contains 18 cosmetic `Underfull \hbox` notices confined to the
bibliography.  They are caused by long immutable repository URLs, do not
remove text, and were visually inspected.  They are recorded rather than
hidden.
