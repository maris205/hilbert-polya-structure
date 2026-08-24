# Source audit — C119

- The rational matrix `A=[[3/4,-1/4],[1/2,0]]` and the standard bosonic Fock
  construction are frozen before computation.
- Matrix spectra, singular values, traces, Taylor coefficients, and zero
  multiplicities are derived exactly; no floating-point value enters evidence.
- The only decimal evaluations occur inside assertions that supplement, but do
  not replace, the recorded radical inequality certificate.
- `Gamma(A)` is an expressly defined operator owner, not inferred from an orbit
  table and not fitted to external zeros.
- No prime table, target-zero table, arithmetic local datum, Euler factor, root
  number, automorphy datum, or Hilbert–Pólya operator is imported.
- There are no external citations. Literature novelty is `UNVERIFIED`, and no
  precedence or novelty claim is made.
