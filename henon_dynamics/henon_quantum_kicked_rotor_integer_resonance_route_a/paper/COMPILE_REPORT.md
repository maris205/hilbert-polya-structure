# C337 compilation report

- Engine: LuaLaTeX, two passes in a fresh directory for each build.
- Determinism environment: `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, fixed trailer identifier.
- Round 0: 2 pages, 20 embedded/subset font rows, SHA-256 `3c95dc08a70b5204b3cca04d7f39a084dc78daed3bce2721db3f97b790d4f47a`.
- Round 1: 3 pages, 20 embedded/subset font rows, SHA-256 `6ff9954a5b6ae3f8c6178c1e579748f64e27ddc7570c3aeacf65a19225ef87fe`.
- Round 2/final: 3 pages, 21 embedded/subset font rows, SHA-256 `c8190d9295bd62c41af9f666bcfe341ee26006e0854631a2639cca4a64663a3d`.
- All rounds are substantively distinct; `main.pdf` equals round 2 byte for byte.
- Two fresh builds per round are byte-identical to each checked-in PDF.
- LaTeX/package warnings: 0. Overfull boxes: 0. Underfull boxes: 0. Undefined references/citations: 0. Missing glyphs: 0.
- Extracted-text control bytes and literal TeX garbage: 0.  The source gate
  also requires the exact powers `U_{2\pi\ell}^{t}` and
  `U_{2\pi\ell}^{2}` and rejects the author-review `^{,t}` / `^{,2}`
  transcription failure.
- Every page in all three rounds was rasterized and visually inspected; no clipping, collision, blank-final-page error, or unreadable formula was found.
