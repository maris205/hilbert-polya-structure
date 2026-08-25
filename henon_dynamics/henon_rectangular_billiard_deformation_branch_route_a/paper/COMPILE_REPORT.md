# C167 compile report

Date: 2026-08-25

Engine: LuaLaTeX

Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`

## Final checks

- Two empty auxiliary directories were built with identical fixed-epoch
  commands.  Their PDFs are byte-identical to each other and to the released
  `main.pdf`.
- `main.pdf` is byte-identical to `main_round2.pdf`; round zero, round one,
  and round two have three distinct SHA-256 values.
- Final PDF SHA-256:
  `03ce3fe4f1827d9f781dcd7a07575458d0f26f7c76cf0073cb25d9a9a787ba08`.
- Output is two A4 pages.  Every font reported by `pdffonts` is embedded.
- Both fresh logs contain no warning, overfull/underfull box, missing-glyph,
  undefined-reference/citation, or multiply-defined-label message.
- Both rendered pages were inspected: no clipping, collision, truncation,
  blank page, malformed formula, or unreadable text was found.
- The English abstract has 203 rendered words.  The independently composed
  Chinese abstract has 330 non-whitespace rendered characters.  Each language
  has six keywords.
- A post-round hostile audit tightened all collision language to distinguish
  pairwise transverse crossings from a higher-multiplicity fibre; the fresh
  builds above are of that corrected title and source.

## Reproducible command shape

```text
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -lualatex -interaction=nonstopmode -halt-on-error \
  -output-directory=<empty-directory> <empty-directory>/main.tex
```

The final audit also runs `pdfinfo`, `pdffonts`, `pdftoppm`, and bytewise
comparisons.  LaTeX auxiliary, log, recorder, and build-cache files are not
release payloads and are removed before manifest generation.
