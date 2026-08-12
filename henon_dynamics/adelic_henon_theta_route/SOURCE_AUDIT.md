# Source and novelty audit

Search date: 2026-08-12.

## Source-locked Hénon base

The local project source is

henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf

with SHA-256

23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9.

It fixes the area-preserving quadratic Hénon model and the original
Hilbert--Pólya motivation. C35 retains that map but changes the arithmetic
and operator architecture.

## Primary prior art

1. J. Tate, Fourier Analysis in Number Fields and Hecke's Zeta-Functions:
   adelic Schwartz spaces, self-dual Fourier transform, local/global
   characters, Poisson summation, and the zeta functional equation are prior
   art.
2. A. Connes, Trace formula in noncommutative geometry and the zeros of the
   Riemann zeta function, Selecta Math. 5 (1999), arXiv:math/9811068:
   absorption-spectrum and trace-formula architecture is prior art.
   https://arxiv.org/abs/math/9811068
3. A. Connes and C. Consani, The Scaling Hamiltonian, arXiv:1910.14368:
   the Poisson map, Fourier/inversion relation, scaling representation, and
   zeta multiplier are prior art. The two boundary terms in the full
   nonzero-rational Poisson identity are also imported from this standard
   Poisson calculation.
   https://arxiv.org/abs/1910.14368
4. A. Connes and C. Consani, Knots, primes and the adele class space,
   arXiv:2401.08401: the scaling-site periodic orbit
   \(C_p=\mathbb R_+^*/p^{\mathbb Z}\) and length \(\log p\) are prior art.
   https://arxiv.org/abs/2401.08401

## Search boundary

The bounded search covered combinations of:

- adelic Hénon or polynomial-kick quantization;
- cubic chirps and adelic theta distributions;
- Tate/Connes relative scattering;
- finite-rank defects of Poisson boundary spaces;
- polynomial canonical transformations and Riemann spectral realization.

No source was located that packages the specific H6 adelic unitary, proves
its rational theta-stabilizer identity, derives the exact cubic dilation
recurrence, proves the static range-pair bound, and exposes the infinite
scaling-covariance orbit that blocks a two-channel interpretation.

This is a search-bounded novelty statement, not a claim of exhaustive
priority.

## Claim boundary

Imported:

- all Tate/Poisson analytic continuation and functional-equation results;
- the Connes absorption and scaling framework;
- scaling-site prime orbits and their clock.

New in this project:

- the exact H6 specialization as one restricted adelic unitary;
- the global cancellation of the rational generating-function gauge in this
  Hénon package;
- the exact \(p\)-adic cubic-ball recurrence used as a noncompactness
  witness;
- the codimension-two static fixed-phase range-pair bound and its precise
  failure to imply finitely many dynamical channels;
- the infinite-dimensional scaling orbit theorem for the cubic boundary
  family;
- the explicit H6 scaling-family specialization of the standard Poisson
  boundary-defect formula, used to isolate the common output mode without
  claiming determinant class;
- the parity firewall requiring the full \(\mathbb Q^\times\) adelic Poisson
  map rather than a positive-integer even-sector shorthand;
- the sharp Route-A branching test for the resulting determinant.

Not claimed:

- a proof of RH;
- a new proof of Tate's thesis or the Connes trace formula;
- an already constructed nontrivial relative determinant;
- Hénon essentiality;
- Route-B readiness.
