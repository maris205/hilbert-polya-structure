# Compile report

- Engine: pdfTeX 1.40.22 (TeX Live 2022/Debian).
- Command: `SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex`, twice per build.
- Final PDF: 3 US-letter pages, PDF 1.5.
- Source SHA-256: `c531285409a76f1daf99ef6415cfa84a3b14dd693e0cc623b1897cc6b522aaad`.
- PDF SHA-256: `43473a72f7cf7ae375bae14471c3ee1e1c2a745e0c7a781d9e8722848f7d7382`.
- Snapshot hashes are distinct for rounds 0 and 1; `main.pdf` equals `main_round2.pdf`.
- Fonts: every font reported by `pdffonts` is embedded and subset.
- Final log: no warning, overfull/underfull box, undefined reference,
  multiply-defined label, or citation warning.

The final deterministic double-build and rendered-page audit are repeated in
the uniform batch release gate.
