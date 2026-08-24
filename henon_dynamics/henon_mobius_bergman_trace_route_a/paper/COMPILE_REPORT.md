# Compile report

- Engine: pdfTeX 1.40.22 (TeX Live 2022/Debian)
- Command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex`, twice
- Final PDF: 3 US-letter pages, PDF 1.5
- SHA-256: `8a090802c0bc97694d6173050d15dfacc67028a5f3dbd5734c548cfb30fd0f5e`
- Determinism: two fresh isolated two-pass builds and the checked-in final PDF have identical hashes
- Fonts: every font reported by `pdffonts` is embedded and subset
- Layout: all three pages were visually inspected; no clipping, collision, truncation, or blank content
- Log: no overfull/underfull box, undefined reference, multiply-defined label, citation, or other warning remains

The frozen epoch removes creation-time metadata variance only and does not
alter mathematical content.
