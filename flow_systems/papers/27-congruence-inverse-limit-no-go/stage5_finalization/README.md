# P27 Stage 5 finalization workspace

Status: **Stage 5 `in_progress`; awaiting one scholar content confirmation.**

This directory is a format-only staging area derived from the accepted fresh
Stage-4.5 Round-2 inputs:

- `manuscript.tex` is the accepted Stage-4.5 TeX with exactly 110 standalone
  ARS `<!--block:B####-->` transport-marker lines removed. No other source
  byte was changed. SHA-256:
  `bbac2f5dd43149348c33da883e2b7fe0d342abdf932723ea859edf70d46d5e48`.
- `references.bib` is byte-identical to the accepted bibliography. SHA-256:
  `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981`.
- `content_proof.pdf` is a byte-identical copy of the accepted Stage-4.5
  preview, supplied only for the pending scholar content confirmation.
  SHA-256:
  `087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208`.

The locked citation profile is numeric `natbib` plus `plainnat`. LaTeX is the
authoritative format because the recorded Pandoc preflight is lossy for this
source. No final `paper.pdf` exists here by design; it must not be created
before the pending content confirmation.
