# P26 Stage 5 finalization workspace

Status: **Stage 5 `in_progress`; awaiting one scholar content confirmation.**

This directory is a format-only staging area derived from the accepted fresh
Stage-4.5 Round-2 inputs:

- `manuscript.tex` is the accepted Stage-4.5 TeX with exactly 125 standalone
  ARS `<!--block:B####-->` transport-marker lines removed. No other source
  byte was changed. SHA-256:
  `fca2b382c3d64273ccb6c17d63330ecfad20ff02087b001175c1003bb4006fd3`.
- `references.bib` is byte-identical to the accepted bibliography. SHA-256:
  `dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f`.
- `content_proof.pdf` is a byte-identical copy of the accepted Stage-4.5
  preview, supplied only for the pending scholar content confirmation.
  SHA-256:
  `402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da`.

The locked citation profile is numeric `natbib` plus `plainnat`. LaTeX is the
authoritative format because the recorded Pandoc preflight is lossy for this
source. No final `paper.pdf` exists here by design; it must not be created
before the pending content confirmation.
