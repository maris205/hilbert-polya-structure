# Compile report

- Engine: pdfTeX 1.40.22 (TeX Live 2022/Debian).
- Command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 TZ=UTC latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`, in two fresh isolated directories.
- Final source SHA-256: `53b6d2793a9a3a08ee898f7eddbbe75b8a64f654eb37f538f8001fa7a352cc89`.
- Final PDF: 3 US-letter pages, PDF 1.5, 292799 bytes.
- SHA-256: `abc8fb4dff98646b07ff030a900467f1d5cfe5c0ce9db317d57205bb7689f0c6`.
- Determinism: two fresh isolated two-pass builds, `main_round2.pdf`, and the checked-in `main.pdf` have identical hashes.
- Fonts: every font reported by `pdffonts` is embedded and subset.
- Log: zero overfull/underfull boxes, undefined references, multiply-defined labels, citations, or other warnings.
- Visual audit: all three pages were inspected at rendered page resolution; no clipping, overlap, truncation, malformed formula, or blank content was found.  A malformed spacing command and a half-phase lift ambiguity found on page one were corrected and the complete final PDF was rebuilt.

The fixed epoch removes creation-time metadata variance only and does not alter mathematical content.
