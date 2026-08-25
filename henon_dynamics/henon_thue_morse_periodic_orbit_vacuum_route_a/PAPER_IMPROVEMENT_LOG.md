# C144 paper improvement log

No external reviewer transport or numeric review score was used.  Both rounds
were direct internal theorem, scope, and presentation audits, and each repair
was compiled before the next round.

## Round 0 to round 1

Findings:

- The product-topology nonemptiness argument did not explicitly explain why a
  fixed window eventually lies wholly inside the one-sided fixed point.
- The least-period sentence for `w_k^infinity` skipped the divisor implication
  connecting a smaller cyclic period to equality of the two halves.
- The finite defect ledger did not explain why its language-membership test was
  exhaustive.

Repairs:

- Specified an arbitrary negative extension and origins tending to positive
  infinity.
- Added that a proper divisor of `2^k` divides `2^(k-1)`, contradicting the
  complementary halves.
- Added the four-concatenation language capture used by the exact ledger.

## Round 1 to round 2

Findings:

- Closedness and shift invariance of the language subshift were implicit.
- The assertion that all four adjacent dyadic block types occur needed an
  explicit witness.
- The local and macroscopic finite cutoffs could be separated more sharply
  from the all-period aperiodicity proof.

Repairs:

- Stated closedness and shift invariance.
- Exhibited all four pairs inside `01101001`.
- Stated that neither finite cutoff enters the proof of the periodic-orbit
  vacuum.

Final audit: no unresolved critical, major, or minor issue remains within the
frozen claim scope.  The final paper makes no external-independence claim.
