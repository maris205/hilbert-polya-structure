# P212 terminal preflight

2026-09-11 UTC. The first documentary command incorrectly ran the
directory-relative frozen Round2 manifest from workspace root. It failed with
24 unread paths and one wrong-base README comparison. It created no qa_final
tree and ran no TeX; this failure is preserved here and was not relabelled.

The corrected command changed only cwd to frozen_round2. All 25 Round2
manifest entries, all eight terminal build sources and all 223 selected
runtime content pins then passed. Both terminal output paths were absent,
available space was 12,763,353,088 bytes, recipe syntax passed, and exact
source/runtime manifest SHA-256 values are respectively
`ac6a5776e0f42298fcd0212ac681f0881549680d05361fe8bd15546c51dcc3a1`
and `35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530`.
Recipe SHA-256 is
`1c19b69023fae89da87adffdc4bed6ddd7de812d0df6aa0cad3006d2666ee9f1`.
