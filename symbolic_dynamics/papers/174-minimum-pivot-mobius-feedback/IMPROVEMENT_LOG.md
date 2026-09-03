# Improvement log — P174

## Author Round 0

- PDF SHA-256:
  `c1865f487b633477b41ffda5a6a03c0974516c3cea0f30160077e93c3157ec58`.
- Author verifier: 131,018,555 assertions, `RESULT PASS`.

## Hostile Review A and Round 1

Review A returned `0 Critical / 0 Major / 0 Minor`, with the amber
adaptive-normalization/artificial-order kill switch explicitly retained.
Its independent bit-mask verifier passed 161,536 assertions across 35
complete parameter boxes.  No source or manuscript change was required, so
`main_round1.pdf` is byte-identical to `main_round0_original.pdf`.

## Hostile Review B and Round 2

Review B returned `0 Critical / 0 Major / 1 Minor` after 4,755,152
independent exact assertions.  `P174-RB-MIN-01` required an explicit source
and subtraction for ordered minimal/canonical images and canonizing elements.
Jefferson--Jonauskyte--Pfeiffer--Waldecker (2019) is now present in the
manuscript, bibliography, source/evidence ledgers, README, and expanded owner
query log.  The nontransfer boundary is explicit: their machinery minimizes
over a group and is orbit-constant, while P174 applies one current-pivot-
selected projectivity and studies an orbit-nonconstant feedback tower and
target-dependent pivot interval.

The reviewer performed a read-only delta audit and marked the finding
`CLOSED`.  Final Round-2 PDF: 4 pages, 321,776 bytes, SHA-256
`b428c24be406d8c2cef9c1d6fc5a2630495f2eed54473ed1dec7b1120444ff7f`.
The gate remains `PROVISIONAL_AMBER / HOLD_EXTERNAL`.
