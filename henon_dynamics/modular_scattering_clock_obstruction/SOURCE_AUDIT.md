# Source and novelty audit

**Source lock:** 2026-08-07

**Scope:** modular cusp double cosets, scattering coefficients and sojourn
times, Gauss/continued-fraction transfer operators, and the distinction
between open scattering channels and closed hyperbolic conjugacy classes.

## Local project boundary

The HCS-C01--C16 project packages and both local registries were checked before
HCS-C17 was frozen.  No previous local project implements the modular cusp
double-coset classification, the modular scattering coefficient, or a
Gauss/Mayer countable transfer operator.  HCS-C14 and HCS-C15 already cover
chronology loss and fixed finite-memory zero density, while HCS-C16 explicitly
recommends a noncompact scattering/countable-return switch.  HCS-C17 therefore
does not repeat a local experiment.

The foundational local paper is Liang Wang, *An Area-Preserving Hénon-Map
Model for the Riemann Zeros* (2026), stored at
`../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`.  It is
used as motivation for looking for an intrinsic dynamical clock, not as a
proof of its continuum regularization, fitted scale, or Hilbert--Pólya bridge.

## Primary-source boundary

1. **Selberg zeta and the modular surface.**  Selberg's trace-formula work is
   the classical source for the closed-geodesic zeta and spectral relation:
   A. Selberg, “Harmonic analysis and discontinuous groups in weakly
   symmetric Riemannian spaces,” *J. Indian Math. Soc.* 20 (1956), 47--87.

2. **Eisenstein scattering and the zeta quotient.**  The constant term of the
   non-holomorphic Eisenstein series gives the standard modular scattering
   coefficient
   \(\Phi(s)=\Lambda(2s-1)/\Lambda(2s)\).  D. Zagier, “Eisenstein series and
   the Riemann zeta function,” in *Automorphic Forms, Representation Theory
   and Arithmetic* (1981), 275--301.

3. **Gauss dynamics and Fredholm determinants.**  D. H. Mayer,
   “On the thermodynamic formalism for the Gauss map,” *Commun. Math. Phys.*
   130 (1990), 311--333, DOI
   <https://doi.org/10.1007/BF02473355>, and “The thermodynamic formalism
   approach to Selberg's zeta function for \(\mathrm{PSL}(2,\mathbb Z)\),”
   *Bull. Amer. Math. Soc.* 25 (1991), 55--60, DOI
   <https://doi.org/10.1090/S0273-0979-1991-16068-1>.  These papers place the
   countable Gauss transfer operator firmly on the Selberg endpoint; that
   endpoint is not novel here.

4. **Continued fractions and geodesic coding.**  C. Series, “The modular
   surface and continued fractions,” *J. London Math. Soc.* 31 (1985),
   69--80, DOI <https://doi.org/10.1112/jlms/s2-31.1.69>.  Cyclic Gauss words
   code closed geodesics, so cyclic invariance is a mandatory total-period
   test rather than an optional numerical control.

5. **Modern cusp acceleration.**  A. D. Pohl and M. Wabnitz,
   “Selberg zeta functions, cuspidal accelerations, and transfer operators,”
   arXiv:2209.05927, <https://arxiv.org/abs/2209.05927>.  Their general
   acceleration and nuclear Fredholm construction rules out novelty claims of
   the form “countable cusp map \(\to\) nuclear determinant \(\to\) Selberg
   zeta.”

6. **Sojourn times and scattering geodesics.**  V. Guillemin,
   “Sojourn times and asymptotic properties of the scattering matrix,”
   *Publ. RIMS* 12, special issue 99 (1976), 69--88, DOI
   <https://doi.org/10.2977/PRIMS/1195196598>, supplies the geometric
   scattering/sojourn-time framework.  A recent explicit modular treatment is
   S. Pujahari and B. Satpathy, “Prime scattering geodesic theorem,”
   arXiv:2505.04973, <https://arxiv.org/abs/2505.04973>; it makes the
   \(2\log(cT_0)\) sojourn clock and orientation conventions especially
   relevant.  This recent work is treated as direct overlap for open-channel
   counting, not as support for a closed-orbit identification.

7. **Scattering poles and geometry.**  L. Ji and M. Zworski,
   “Scattering matrices and scattering geodesics of locally symmetric
   spaces,” *Ann. Sci. Éc. Norm. Supér.* 34 (2001), 441--469, DOI
   <https://doi.org/10.1016/S0012-9593(01)01065-5>, gives broader geometric
   context for the category distinction.

## What is classical

The following are not claimed as new:

- the \(P\backslash\Gamma/P\) classification and \(\varphi(c)\) count;
- \(\sum\varphi(c)c^{-2s}=\zeta(2s-1)/\zeta(2s)\);
- the completed modular scattering coefficient;
- Gauss/Series coding and Mayer's Selberg determinant;
- Cayley--Hamilton and the Chebyshev formula for matrix powers;
- hyperbolic translation length and its repetition law;
- the fact that a zero-free factor cannot remove a meromorphic divisor.

## Defensible contribution

The contribution is the combination, formulated as a compatibility ruling:

- an explicit separation of oriented open cusp channels from closed
  conjugacy classes;
- a no-regularity theorem showing that every final-denominator-only
  \(F(\alpha|c|)\) satisfying square repetition on all positive hyperbolic
  matrices is zero;
- identification of the canonical stable homogenization of
  \(2\log|c(g^n)|\) with the Selberg translation length;
- an exact Euler-product corollary and a source-normalization divisor no-go;
- independent code certificates that use neither prime nor zero tables.

This is a modest internal theorem delta with high Route-A value.  The audit
does not establish priority for each elementary lemma, and it does not present
a new scattering or transfer-operator theory.

## Excluded overclaims

The theorem does not rule out local denominator cocycles, cyclic sums,
cohomologous roofs, full-word or trace-dependent clocks, endpoint-extended
operators, matrix-valued cocycles, subadditive pressure, open groupoid traces,
multi-cusp scattering matrices, or a compensating factor that itself carries
a zeta-zero divisor.
