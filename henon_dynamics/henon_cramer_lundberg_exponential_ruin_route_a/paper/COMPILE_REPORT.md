# Deterministic compile and visual report

- Engine: LuaLaTeX.
- Environment: `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Every revision received two passes in each of two fresh directories; paired
  builds were byte-identical.
- All settled logs were warning-free: no layout, citation, reference,
  destination, missing-character, or rerun warning.
- All font rows in all archives are embedded and subset.
- Text extraction recovers the joint transform, loading table, critical cusp,
  supremum mixture, evidence receipt, citations, tuple, and scope literal.
- All eight pages across the three revisions were visually inspected after the
  independent uniqueness/killed-owner/first-mean repair; no page has clipping,
  overlap, missing glyph, or an unreadable table.

| revision | pages | SHA-256 |
|---|---:|---|
| round 0 original | 2 | `9d839e63ac589b1f4f3188a36bf7738a39bf42a20e56a18827be43d076d25be0` |
| round 1 | 3 | `818037a1ffb543d4770aaa15a9a8629575b457e0e00f24a7779389507ac67060` |
| round 2 | 3 | `bb934cc9ed23105dac16c3ee7dba1acd37f0826f8da7a0b5c215f97ff9e4218e` |
| final (`main.pdf`) | 3 | `bb934cc9ed23105dac16c3ee7dba1acd37f0826f8da7a0b5c215f97ff9e4218e` |

The three hashes are distinct and final equals round 2 byte-for-byte.
