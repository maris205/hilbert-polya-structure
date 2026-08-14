# Source audit

Date: 2026-08-14

## External proof source

**William Parry and Mark Pollicott, _Zeta Functions and the Periodic Orbit
Structure of Hyperbolic Dynamics_, Astérisque 187--188 (1990).**

The official NUMDAM record and PDF were checked.  The manuscript uses:

- Theorem 6.3 and Corollary 6.3.1 (pp. 95--96) for the weak-mixing positive-roof
  suspension zeta and the principal part of its logarithmic derivative;
- Theorem 6.4 and Corollary 6.4.1 (pp. 97--98) for the two-parameter weighted
  zeta under the explicitly stated Hölder periodic-sum hypothesis;
- Theorem 6.9 (p. 109) for the primitive-orbit counting asymptotic.

The source parameter map is printed in the paper: `f=hat tau`, `g=0`,
`c=1`, and `k=psi`, with `P(g-cf)=0`.  The source proves a local meromorphic
germ in the stated dynamical setting.  It does **not** identify the Galois
excess with a Hölder potential and does not prove continuation of the actual
full Mahler-weighted amplitude.

Official record:
<https://www.numdam.org/item/AST_1990__187-188__1_0/>.

## Background source

Michel Hénon's bibliographic metadata for “A Two-Dimensional Mapping with a
Strange Attractor,” _Communications in Mathematical Physics_ 50(1), 69--77
(1976), were verified through DOI
<https://doi.org/10.1007/BF01608556>.  This citation supplies historical
background, not the certified H6 survivor or the pressure theorem.

## Internal source locks

The producer and independent checker recompute eight SHA-256 locks:

- P31 Bowen-pressure theorem package;
- P45 pressure-normalized prime-orbit README and certificate;
- P48 exact multiplier-field certificate;
- P53 README, proof package and certificate;
- the inherited instability-roof zeta README.

These artifacts supply the frozen survivor, pressure interval, non-lattice
roof, exact trace polynomials and Mahler-height amplitude.  Their claims are
not inferred from the present finite rows.

## Citation ceiling

No checked source proves a rational-prime orbit correspondence, a
von-Mangoldt trace, a completed Riemann determinant, a self-adjoint operator,
or the Riemann hypothesis.  Parry--Pollicott attaches unconditionally only to
the physical suspension zeta; its weighted theorem is used only inside the
explicit conditional completion.
