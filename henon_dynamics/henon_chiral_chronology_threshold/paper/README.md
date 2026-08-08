# HCS-C21 manuscript

**Title:** *Point chronology without cohomological time in a period-six
chiral Hénon cover*
**Format:** English body with an independent Traditional-Chinese abstract
**Status:** 17-page LuaLaTeX manuscript compiled from the final Stage-2
sources

The central theorem proves that the genuine order-six point chronology on
the genus-one chiral ordered cover acts trivially on ordinary weight-one
cohomology.  The period-seven comparison remains explicitly limited to the
adopted HCS-C20 component.  The paper does not claim a varying-period
determinant or a Hilbert--Pólya operator.

## Files

- [main.pdf](main.pdf): compiled manuscript.
- [main.tex](main.tex): entry point.
- [sections/](sections/): English and Traditional-Chinese abstracts, theorem
  sections, declarations, and reproducibility appendices.
- [references.bib](references.bib): source-audited bibliography with frozen
  repository links.
- [PAPER_CONFIGURATION.md](PAPER_CONFIGURATION.md),
  [PAPER_OUTLINE.md](PAPER_OUTLINE.md), and
  [ARGUMENT_BLUEPRINT.md](ARGUMENT_BLUEPRINT.md): manuscript planning and
  claim architecture.

## Build

The build requires LuaLaTeX, `latexmk`, Babel's
`chinese-traditional` locale, and the `Droid Sans Fallback` font.

```bash
lualatex --version
fc-match "Droid Sans Fallback"
latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The released PDF has SHA-256
`984ad0bc7cd0fe8840ce6a6f442dd377f930127e28836137ca814a2dd30847e1`.
See [../COMPILE_REPORT.md](../COMPILE_REPORT.md) for the complete validation
ledger.
