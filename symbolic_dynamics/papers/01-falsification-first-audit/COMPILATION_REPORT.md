# Compilation Report

## Final Round-2 release

- Status: **SUCCESS**
- Current PDF: `main.pdf`
- Frozen artifact: `main_round2.pdf` (byte-identical to `main.pdf`)
- Preserved intermediate: `main_round1.pdf`
- Pages: **19**
- PDF size: **513,650 bytes**
- SHA-256:
  `c2d87b185088e75e0cde7c7f2085ebd59a6fb1de97d0db9db1c7d1d68ab9520c`
- Build: `pdflatex` → `bibtex` → three `pdflatex` stabilization passes
- Undefined references/citations: **0**
- LaTeX errors: **0**
- Overfull/underfull boxes: **0**
- Fonts embedded: **YES**
- Rendered author line: **Anonymous Authors**
- Figures and the generated evaluator table were visually inspected; colors
  have redundant text encoding and a colorblind-safe palette.

## Preserved baseline

- Artifact: `main_round0_original.pdf`
- Pages: **16**
- SHA-256:
  `4860190af19b27877d5a4fe1bb0bc0756d339fb47b4aaf8c075655715fe02742`

## Preserved Round 1

- Artifact: `main_round1.pdf`
- Pages: **19**
- SHA-256:
  `f16cdd9c880a2fa3e17afa219b012ff9836ad9feee6f26eb5038a077552c336e`

Ignored LaTeX intermediates are removed after final validation and can be
regenerated with the commands in `README.md`.
