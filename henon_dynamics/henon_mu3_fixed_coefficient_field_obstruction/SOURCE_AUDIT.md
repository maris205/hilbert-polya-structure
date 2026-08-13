# HCS-C44 source and novelty audit

## Locked local sources

- HCS-C43 certificate SHA-256:
  `4c431d89c59a5aef8f765dc93ee60e5aa338466500aee033fa87c4a8b2ab7501`.
- HCS-C43 derivation SHA-256:
  `5e0f495807e4e9cb6f42f09bb91874047a7d549f5e5e1e00842b78884a9d10da`.
- HCS-C38--C42 project READMEs were reviewed to exclude scalar Kummer,
  bare three-channel, Schatten-clock, CM-elliptic, and finite Tate--CM
  duplication.

## Primary literature boundary

- Chun Yin Hui, *On the rationality of algebraic monodromy groups of
  compatible systems*, JEMS 27 (2025), DOI `10.4171/JEMS/1438`, fixes a number
  field \(E\) and a common finite dimension in the definition of an
  \(E\)-compatible system.
- Raju Krishnamoorthy and Yeuk Hay Joshua Lam, *Frobenius trace fields of
  cohomologically rigid local systems*, arXiv:2308.10642, treats boundedness of
  Frobenius trace fields as a substantive geometric-origin condition.  C44 is
  a concrete negative trace-field theorem for the Hénon kernel family, not an
  application of their rigidity hypotheses.
- The finite-field monomial sums and cyclotomic stabilizer argument used here
  are proved directly; no classification theorem is imported.

## Nonduplication

- C38 proves functorial scalar cubic Kummer decorations are coboundaries.  C44
  uses the nonfunctorial full Hénon kernel and the actual coordinate
  permutation surviving that obstruction.
- C39 and C40 concern a fixed three-channel divisor and externally damped
  prime blocks.  C44 concerns unbounded Frobenius trace fields.
- C41 and C42 close the minimal fixed-rank CM/Tate repair.  C44 closes the
  broader source-native paired-kernel repair at the coefficient-field gate.
- The C43 finite local-degree ledger motivates but does not prove C44.  The
  new result is the all-prime two-moment stabilizer theorem.

## Novelty verdict

`MEDIUM_HIGH_SEARCH_BOUNDED` as of 2026-08-13.  No source located formulates
this Hénon histogram, its maximal-real-cyclotomic trace-field theorem, or the
resulting compatible-system obstruction.  The compatible-system and
trace-field framework itself is established prior art.

