# SD-C04 — Gauss/Mayer Transfer Candidate

## Frozen construction

The countable full shift on continued-fraction digits \(n\ge1\) codes the
inverse branches

\[
\phi_n(z)=\frac1{n+z}.
\]

For a primitive word \(\gamma\), the roof is the intrinsic logarithmic
derivative length

\[
T_\gamma=2\log\lambda_+(M_\gamma).
\]

On Mayer's holomorphic Banach-space realization,

\[
(\mathcal L_sf)(z)=
\sum_{n\ge1}(n+z)^{-2s}
f\!\left(\frac1{n+z}\right),
\]

and the frozen determinant is

\[
D_{\rm MG}(s)
=\det(I-\mathcal L_s^2)
=\det(I-\mathcal L_s)\det(I+\mathcal L_s).
\]

## Findings

- **PROVED / primary-source verified:** the grammar, derivative roof, and
  signed Fredholm determinants form a natural analytic symbolic package.
- **PROVED:** primitive words are periodic continued fractions and determine
  quadratic irrationals or hyperbolic modular classes; cyclic rotation is the
  orbit equivalence and word powers give repetitions.
- **REFUTED for the rational-prime target:** no canonical map from these
  primitive classes to rational primes or from their repetitions to the
  \(\Lambda(p^r)\) ledger is supplied by the construction.
- **NUMERICAL OBSERVATION:** finite digit/word truncations test the exact
  symbolic bookkeeping only.  They are not certified analytic continuation.
- **STOP_SCOPED:** the known modular-surface interpretation is recorded as a
  ROUND2 clue and is not used to invoke Route B.

This is the strongest natural determinant candidate in the session, but it
fails the hard rational-prime A0 gate and remains Route-A exploratory.

## Sources

- D. Mayer, [Gauss-map transfer operator](https://doi.org/10.1007/BF02473355)
- D. Mayer, [Selberg zeta and transfer determinants](https://doi.org/10.1090/S0273-0979-1991-16023-4)
- S. Isola, [Farey and Gauss transfer operators](https://doi.org/10.1088/0951-7715/15/5/310)

## Artifacts

- [Derivation package](DERIVATION_PACKAGE.md)
- exact word-enumeration and truncation diagnostics under the session-level
  code/, experiments/, and results/ directories
