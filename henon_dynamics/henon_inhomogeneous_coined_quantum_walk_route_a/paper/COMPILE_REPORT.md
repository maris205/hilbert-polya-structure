# Compile report

- Engine: pdfTeX 1.40.22 (TeX Live 2022/Debian).
- Command: `SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex`, twice per build.
- Final PDF: 3 US-letter pages, PDF 1.5.
- Source SHA-256: `ee87678af8b68debc2b46b4924083028b0ce1d4a34eac1ed523817c4ddb49435`.
- PDF SHA-256: `8099e81a1bb9e11f9da3e5521bb6bf15bc7bf28eaf7cc06890a813e03c1e79e6`.
- Round-zero and round-one hashes are distinct; `main.pdf` equals
  `main_round2.pdf`.
- Every font reported by `pdffonts` is embedded and subset.
- The final log has no warning, overfull/underfull box, undefined reference,
  multiply-defined label, or citation warning.

The uniform batch audit performs a second isolated deterministic build pair
and rendered-page inspection before release.
