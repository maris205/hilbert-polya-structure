# C179 test report

All exact tests target source commit
`bbb809ee198bc9ad5f196383baab1e3d9de38e43`.

| Gate | Result |
|---|---:|
| canonical producer | pass; 4,927 exact finite rows |
| producer-independent checker | pass; 320,291 assertions |
| separate SymPy reconstruction | pass; 6,674 exact checks |
| byte-for-byte replay | pass; 2,219,358 bytes |
| repaired-hash mutations | pass; 64/64 rejected |
| stale-hash mutation | pass; 1/1 rejected |

The canonical payload SHA-256 is
`22b08c44f51e4bf063a2fc608d570a3584462d3efbaf3e2acb47d0f9b083b34f`;
the released evidence-file SHA-256 is
`0a756181a775171a6c7de06afced94a75d835cd265d14f38ab825c1119525066`.

The checker does not import producer code.  It uses an independent
Miller–Rabin path, independent factorization/order routines, and brute unit
enumeration.  SymPy separately reconstructs cyclotomic, formal-series,
prime-power order, characteristic-polynomial, and reversor identities.
Mutation tests recompute the canonical payload hash after changing semantics,
so checksum verification alone cannot pass.

Claim-bearing metadata now uses exact-map validation rather than substring or
prefix acceptance: the complete attribution registry, theorem ledger, Route-A
map, scope flags, and integrity map must equal their frozen contracts.  The
original 60 repaired-hash attacks remain intact, and four formerly escaping
attacks were appended: attribution status `NEW_THEOREM_CLAIMED`, an appended
log-p clock claim in A0, an appended target-operator claim in A4, and an
absolutized enlarged-owner impossibility theorem.  All 64, including the four
new cases, are independently rejected after their payload hashes are repaired.

PDF build, font, layout, visual, snapshot, and manifest results are recorded
in `paper/COMPILE_REPORT.md` and `C179_RELEASE_MANIFEST.json`.
