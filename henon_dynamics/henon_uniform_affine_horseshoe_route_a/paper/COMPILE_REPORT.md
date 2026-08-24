# Compile report

- Engine: pdfTeX 1.40.22 (TeX Live 2022/Debian)
- Command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex`, twice
- Final PDF: 3 US-letter pages
- SHA-256: `fb39a43a58737c97674972d01829da2a332df5f156383db0f98c0dadd7b95ab3`
- Determinism: identical SHA-256 after a second independent two-pass build
- Fonts: all fonts reported by `pdffonts` are embedded and subset
- Layout: no overfull or underfull boxes
- References: no undefined references or citation warnings

The frozen epoch is used only to remove PDF creation-time nondeterminism; it
does not alter mathematical content.
