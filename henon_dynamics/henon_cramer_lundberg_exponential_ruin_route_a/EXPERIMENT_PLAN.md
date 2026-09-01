# Claim-driven executable plan

## Locks

- Surplus: `U_t=u+c t-sum Y_i`, with `u>=0`, `c>0`.
- Claim clock: Poisson rate `nu>=0`; sizes iid `Exp(beta)`, `beta>0`.
- Ruin: first strict passage below zero; deficit `D=-U_tau`.
- Baseline: `51fb3d46f96b854314811c1ad62d3103cd5d54e5`.
- Evaluator SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Epoch/scope: `1788220800`; `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Gates

1. Derive the Gerber–Shiu first-jump equation including the ruin forcing term.
2. Close the convolution with a two-dimensional linear system, prove that its
   two characteristic modes exhaust the solution space, and use `J(0)=0` to
   fix the surviving coefficient.
3. Select the positive-discount root by
   boundedness and the profitable zero-discount root by the vanishing
   probability boundary at infinite reserve, with `nu=0` handled directly.
4. Prove overshoot factorization rather than assuming independence.
5. Close profitable, critical, adverse, and no-claim ultimate-ruin chambers.
6. Differentiate at zero discount and prove both finite first-mean formulas and the
   critical square-root divergence.
7. Derive the adjustment martingale and exact supremum mixture.
8. Reconstruct 36 exact regime, 448 transform, 144 conditional-first-mean, 12 martingale, and
   six boundary rows independently.
9. Require exact key-set completeness, boundary semantics, symbolic
   reconstruction, byte replay, and repaired-hash
   hostile mutation rejection.
10. Retain three substantive deterministic PDF revisions and the exact
   27-payload release ledger.

Finite rows exercise the theorem and boundary conventions; the proof for all
continuous parameters is analytic and separate.
