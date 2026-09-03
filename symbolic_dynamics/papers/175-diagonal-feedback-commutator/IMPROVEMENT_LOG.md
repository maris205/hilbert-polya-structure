# Improvement log — P175

## Author Round 0

- PDF SHA-256:
  `32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba`.
- Author verifier: 2,111,465 assertions, `RESULT PASS`.

## Hostile Review A and Round 1

Review A returned `0 Critical / 0 Major / 0 Minor`.  Its independent
flat-tuple prime-field verifier passed 345,906 assertions and independently
checked every-target occupation fibres, image/kernel graph sums, unique
maximum, and the height-two tree.  No manuscript change was required, so
`main_round1.pdf` is byte-identical to `main_round0_original.pdf`.

## Hostile Review B and final Round 2

Review B returned `0 Critical / 1 Major / 0 Minor`.  Its independent
polynomial-field verifier passed 2,559,272 assertions, including genuine
`GF(4/8/9/16)` boxes; every theorem survived.

`P175-B-M01` is implemented: the manuscript displays the exact complete-
graph multivariate-Potts specialization with activities `-1` on support
edges and `X^2-1` on nonedges, cites Stanley's chromatic symmetric function
for the occupation enumerator, and assigns the deterministic occupation-
weight transform zero credit.  The residual is narrowed to the literal
matrix-to-support reduction and consequent rooted functional tree.

Final Round-2 PDF: 4 pages, 328,780 bytes, SHA-256
`321d59b8b66cc2aef22296f214ee0d0072652c86d53293714599b0e07ee4b703`.
Reviewer B then re-read the complete package, verified the exact Sokal and
Stanley identities, the narrowed residual, current PDF/source pins, and the
8/8 live manifest, and marked `P175-B-M01 CLOSED`.  There are no open review
findings.  Two final source-only cold builds reproduce the accepted PDF byte
for byte; `HOLD_EXTERNAL` remains unchanged.
