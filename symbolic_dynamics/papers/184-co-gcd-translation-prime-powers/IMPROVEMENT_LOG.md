# P184 improvement log

## Round 0 → Round 1

Review A solved modular predecessor equations separately on the valuation
strata and rebuilt each functional graph.  Its 521,367 assertions covered 39
prime-power carriers, including zero, `p=2`, `a=1`, and the even middle layer,
with zero Critical, Major, or Minor finding.  Round 1 is an intentional
byte-identical receipt of Round 0.

## Round 1 → Round 2

Review B used least-significant-first base-`p` digit words, carry-level
updates, indegree peeling/reverse BFS, union--find cycle reconstruction, and a
separate inverse grammar.  Its 3,987,801 assertions covered 48 carriers and
all targets, again with zero finding.  No source repair was requested, so all
three rounds share SHA-256
`991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab`.
Two source-only cold builds reproduce the final PDF.  External status remains
`OWNER_AMBER / HOLD_EXTERNAL`.
