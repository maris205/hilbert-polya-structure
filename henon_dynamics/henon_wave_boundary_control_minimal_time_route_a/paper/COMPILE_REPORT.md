# Deterministic compile and visual report

- Engine: LuaLaTeX, two passes per build.
- Locked environment: `SOURCE_DATE_EPOCH=1788307200`, `TZ=UTC`, and the fixed
  trailer ID in `main.tex`.
- Each round was rebuilt in two fresh directories.  Both fresh builds were
  byte-identical to one another and to the corresponding archive.
- Settled second-pass logs were warning-free: no LaTeX/package warning,
  overfull or underfull box, undefined reference/citation, missing character,
  or rerun request occurred.
- Page counts are 1/2/3 for rounds 0/1/2.
- Font audit totals are 19/21/23 rows; every row is embedded and subset.
- Extracted word counts are 260/489/1003 under the manifest's normalized
  Unicode-whitespace tokenization, and increase strictly across the two
  substantive revisions.
- All six rendered pages were visually inspected.  No clipping, overlap,
  missing glyph, broken formula, or unreadable text was found.  The sparse
  reference pages in rounds 1 and 2 are deliberate and correctly composed.

| revision | pages | SHA-256 |
|---|---:|---|
| round 0 original | 1 | `91bfa4f1d7a1f821160acce33df8dc17f3c92692c4d87956b1d94a1226c9ef1b` |
| round 1 | 2 | `787750ff8f7b3bd93772661f31c13c45cea2b9cd56b3613f580071bff874ead0` |
| round 2 | 3 | `e0fb034b86b6016aca38207387bcd3152eba62ce76e85b08c2239305f2e23fe7` |
| final (`main.pdf`) | 3 | `e0fb034b86b6016aca38207387bcd3152eba62ce76e85b08c2239305f2e23fe7` |

The three revision hashes are distinct and the final PDF equals round 2
byte-for-byte.
