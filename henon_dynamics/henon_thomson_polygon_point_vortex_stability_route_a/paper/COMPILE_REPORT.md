# Deterministic compile and visual report

- Engine: LuaLaTeX.
- Locked environment: `SOURCE_DATE_EPOCH=1788307200`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Each round was compiled for two passes in each of two fresh directories.
- The two fresh builds of every round were byte-identical to one another and
  to the corresponding archived PDF.
- Settled second-pass logs were warning-free: no layout, citation, reference,
  destination, missing-character, or rerun warnings.
- Every font row in every archived PDF is embedded and subset.
- `pdftotext` recovers the DFT theorem, heptagon multiplicities, source-owner
  boundary, executable receipt, Route-A tuple, scope literal, and all three
  DOI records.
- All twelve rendered pages across the three archives were visually inspected;
  no clipping, overlap, missing glyph, broken formula, or unreadable table was
  found.  Round 1 and round 2 leave deliberate whitespace after their short
  reference lists; the pages remain correctly composed.
- Font audit totals are 18/19/20 rows for rounds 0/1/2; every row is embedded
  and subset.  Extracted word counts are 1174/1661/1992 and increase strictly.

| revision | pages | SHA-256 |
|---|---:|---|
| round 0 original | 3 | `84ffd06198298313ea07c65d9a857261f3546be11fbfa7f0add3f28945e683e5` |
| round 1 | 4 | `7f838e6c0863795737bcd76fa0d36f4c089731b8c1e1bd5687e4e2dd589ad53d` |
| round 2 | 5 | `6b1501af2dba761ad34e87cc89502c8f4ba8e9c8bb04ed7771ef49f6bf009f6f` |
| final (`main.pdf`) | 5 | `6b1501af2dba761ad34e87cc89502c8f4ba8e9c8bb04ed7771ef49f6bf009f6f` |

The three revision hashes are distinct and the final PDF equals round 2
byte-for-byte.
