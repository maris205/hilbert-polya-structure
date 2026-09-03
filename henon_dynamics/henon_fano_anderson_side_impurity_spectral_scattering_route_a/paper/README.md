# Paper build

`main.tex` is compiled with LuaLaTeX and a fixed trailer ID.  Define
`\CRevisionRound` to 0, 1, or 2 before inputting the source.  The release gate
builds every round twice in fresh temporary directories with
`SOURCE_DATE_EPOCH=1788393600`, requires byte identity, and records:

- `main_round0_original.pdf` — branch-safe Schur/two-pole theorem;
- `main_round1.pdf` — sign-correct Stone-complete spectral measure and
  scattering extension;
- `main_round2.pdf` — full boundary, evidence, source, and scope closure;
- `main.pdf` — byte-identical copy of round 2.

The gate rejects warnings, overfull/underfull boxes, undefined references,
missing glyphs, literal TeX debris, non-embedded or non-subset fonts, raster
failures, and stale round files.
