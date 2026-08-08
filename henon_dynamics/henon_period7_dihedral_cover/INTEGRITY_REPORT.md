# HCS-C20 research-integrity report

**Date:** 2026-08-08

## Computational integrity

- All displayed geometric identities are reconstructed from the frozen
  septic with exact symbolic arithmetic.
- All finite-field counts are exact; no floating-point inference or fitted
  parameter is used.
- Producer and checker share formulas but no code.  The checker neither
  imports the producer nor uses its finite-field packages or HCS-C19
  artifacts.
- The checker binds its report to the exact certificate bytes by SHA-256.
- Mutation tests cover candidate identity, quotient naming, local-factor
  coefficients, good-reduction ledgers, and certificate-byte binding.
- H\'enon period (n), chronological exponent (s), and Frobenius extension
  degree (r) are never identified or averaged.

## Source and citation integrity

- The foundational recurrence is locked to the repository copy of Paper 5.
- The adopted septic and the printed-formula discrepancy are inherited with
  HCS-C19's explicit caveats; no publisher erratum is asserted.
- External references were checked against primary publisher, arXiv, or
  Stacks Project records before use.
- Classical (D_7) covers, quotient-Jacobian relations, Prym decomposition,
  and real multiplication are credited as prior theory.
- The originality statement is deliberately bounded to the exact
  source-locked H\'enon realization; it is not a professional novelty opinion.

## Seven failure-mode audit

1. **Self-confirming code:** cleared by a separately implemented checker and
   tamper failures.
2. **Fabricated or weak citations:** cleared for cited bibliographic facts by
   direct metadata/source checks.
3. **Unreproducible numbers:** cleared by deterministic scripts and compact
   machine-readable certificates.
4. **Chronology destruction:** cleared; the actual ordered-edge action
   (\tau) is retained and no averaged transition matrix substitutes for it.
5. **Narrative repair after anomaly:** cleared; the unexpected ordinary
   spectral collapse is reported as a theorem and obstruction, not hidden.
6. **Method/artifact mismatch:** cleared; manuscript commands and artifact
   paths match the released producer, checker, tests, and PDF.
7. **Hilbert--Polya overclaim:** cleared; fixed-period RM is explicitly
   separated from a cross-period determinant or Riemann spectral map.

## Residual limitations

The selected-prime theorem covers exactly (p=5,11,13).  The work does not
classify all bad primes, compute the complete endomorphism algebra, establish
absolute simplicity, or provide a global dynamical zeta function.
