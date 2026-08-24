# Compile report

- Engine: pdfTeX 1.40.22 (TeX Live 2022/Debian)
- Reproducible command: `SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex`, twice
- Output: 3 US-letter pages, PDF 1.5
- Final SHA-256: `db2bf56fd9c099a1c7449adc2ce4fb119459ee8ee088ab932fd51853fb0ca052`
- Determinism: a second two-pass build produced the identical hash
- Fonts: every font is embedded and subset
- Log: no overfull/underfull boxes, undefined references, or warnings

The frozen epoch removes creation-time metadata variance only.
