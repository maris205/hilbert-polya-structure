# Improvement log — P172

## Author Round 0

- Frozen PDF SHA-256:
  `ac16b12438b1c2db313cc55af630887112ce53833cb7afb76deb656329164ecb`.
- Author verifier: 48,575 assertions, `RESULT PASS`.

## Hostile Review A and Round 1

Review A returned `0 Critical / 0 Major / 2 Minor`.

- `P172-RA-MIN-01` closed: the manuscript and package now quantify
  `n>=1` explicitly.
- `P172-RA-MIN-02` closed: Hoffman–Jenkins–Roughgarden's
  successive-elimination/leader-election neighbour was added to the source
  ledger and bibliography.  Its zero-indegree survivors and induced-current
  graph are explicitly distinguished from P172's positive-indegree retained
  set and fresh fixed-ambient map.
- Review-A independent verifier: 86,630 assertions, `RESULT PASS`.
- Author verifier after repair: 48,575 assertions, unchanged and passing.
- Round-1 PDF SHA-256:
  `ef34c142ea0350d86501d04cc829b8ba8a5e87ea21970b6f180e4bcd7276e62b`.

## Hostile Review B and final Round 2

Review B returned `0 Critical / 3 Major / 5 Minor`; every mathematical claim
survived its independent 20,317-assertion control.

- `Major-B1` repaired: Charalambides' specified-cell occupancy and O'Neill's
  extended occupancy are cited, the exact specialization
  `Q_ab=Occ(b|a,a,a/n)` is displayed for `a>=1`, the empty row is isolated
  from the source's positive-parameter domain, and the whole row/required-box
  algebra is assigned zero credit.
- `Major-B2` repaired: the fixed-target multiepoch subprobability polynomial,
  aggregate identity, fixed-target division, and coefficientwise stabilizer
  proof are explicit; generic marked-kernel/Feynman--Kac multiplication is
  subtracted through Fitzsimmons--Pitman.
- `Major-B3` repaired: P158, P162, P170, and P173 are named, their common
  nesting/quotient/symmetry/Jordan/absorption shell earns zero separation
  credit, and the two distinct inverse axes are stated.
- Minor repairs replace “Boolean multiplicities”, state empty-source Stirling
  conventions, give explicit access-to-zero paths, use `m_a` for the mean,
  and add the three-epoch coefficientwise hostile control to the evidence
  ledger.
- Final Round-2 PDF: 4 pages, SHA-256
  `91e8cc76f007eafba48a343aae116eeda03daa8bf3e1bcdbe50d2fc2e2013c83`.

Reviewer-B then performed a read-only delta audit, independently checked the
O'Neill specialization in 5,425 exact cases through `n=30`, replayed the
48,575 author and 20,317 reviewer assertions, and marked all three Major and
five Minor findings `CLOSED`.  Final disposition:
`ROUND2_DELTA_ACCEPTED / MATHEMATICS_SURVIVES / HOLD_EXTERNAL`.
