# Compile report

- Engine: pdfTeX 1.40.22 (TeX Live 2022/Debian).
- Command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex`, twice per build.
- Final PDF: 3 US-letter pages, PDF 1.5.
- SHA-256: `71619e35d0395c53e946bf18c97e320a0f80f88ffcca1ef3fc207020b18b8a2a`.
- Determinism: two fresh isolated two-pass builds, `main_round2.pdf`, and the checked-in `main.pdf` have identical hashes.
- Fonts: every font reported by `pdffonts` is embedded and subset.
- Log: zero overfull/underfull boxes, undefined references, multiply-defined labels, citations, or other warnings.
- Visual audit: all three pages were inspected at rendered page resolution; no clipping, overlap, truncation, malformed formula, or blank content was found.

The fixed epoch removes creation-time metadata variance only and does not alter mathematical content.
