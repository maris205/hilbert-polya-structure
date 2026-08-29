# C233 compile report

- Engine: LuaLaTeX; two passes per revision.
- Fixed environment: `SOURCE_DATE_EPOCH=1787875200`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Two independent fresh build directories were run for each of revisions 0, 1
  and 2; every pair is byte-identical. Settled logs have zero warnings,
  overfull/underfull boxes, undefined references, missing characters or errors.
- Page counts: round 0 = 3, round 1 = 3, round 2/final = 3; A4.
- Final font audit: 18 entries, every font embedded and subset.
- Extracted-text and visual page audit: PASS; `main.pdf` equals
  `main_round2.pdf` byte-for-byte.
- No LaTeX sidecars are retained in the release directory.

## SHA-256

```text
main_round0_original.pdf  ee0a0bf8c91ba6781f57269ee3976d99ef00c6ab8dd7a3241d8cd1323cf49365
main_round1.pdf           cfc3d010d16d0627cbe360b5629a3ca2d05fff004c9a7b92d865118b5cf00303
main_round2.pdf           e6232d91c62b0fba6b8c432d4419227e0853f101ad2c9e5c652a0b92d3645927
main.pdf                  e6232d91c62b0fba6b8c432d4419227e0853f101ad2c9e5c652a0b92d3645927
```
