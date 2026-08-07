# HCS-C18 primary-source and novelty audit

**Search cutoff:** 2026-08-07.

## 1. Local project boundary

The foundational manuscript `5-An Area-Preserving Henon-Map Model.pdf`
motivates a deterministic dynamical route to Hilbert--P\'olya structures.  It
does not supply the modular endpoint groupoid, the squarefree congruence
scattering tensor formula, or the trace-closure theorems proved here.

HCS-C17 established the one-cusp open double-coset arithmetic and closed the
literal final-denominator-only hyperbolic clock.  Its stated exclusions include
endpoint groupoids and multi-cusp scattering, so HCS-C18 is not a restatement
of that theorem.  The present project closes two standard versions of those
exclusions and leaves nonstandard off-diagonal extensions open.

## 2. Scattering geodesics and sojourn times

- V. Guillemin, *Sojourn Times and Asymptotic Properties of the Scattering
  Matrix*, PRIMS 12 (1976), 69--88,
  [DOI](https://doi.org/10.2977/PRIMS/1195196598).  This is the geometric
  source for cusp-to-cusp scattering geodesics and the relation between their
  sojourn times and the scattering matrix.  HCS-C18 claims no novelty for that
  relation.
- L. Ji and M. Zworski, *Scattering Matrices and Scattering Geodesics of
  Locally Symmetric Spaces*, Ann. Sci. ENS 34 (2001), 441--469,
  [original article](https://www.numdam.org/articles/10.1016/S0012-9593(01)01065-5/),
  with the 2002 correction and supplements
  [here](https://www.numdam.org/articles/10.1016/S0012-9593(02)01111-4/).
  These works already provide the higher-rank geometric framework.  The
  project uses only the modular rank-one specialization.
- S. Pujahari and P. P. Satpathy, *Prime Scattering Geodesic Theorem*,
  arXiv:2505.04973 (2025),
  [primary preprint](https://arxiv.org/abs/2505.04973).  Their Theorems 1.5
  and 1.8 and equation (2.10) give the unoriented representatives,
  \(n_q=(\varphi(q)+s_q)/2\), and \(\ell_q=2\log(qT_0)\).  Proposition 2.1 of
  HCS-C18 is a direct Euler-product corollary of these inputs and is labelled a
  low-novelty positive control.

## 3. Endpoint cocycles and trace closure

- V. Nekrashevych, *Hyperbolic Groupoids: Metric and Measure*, Groups Geom.
  Dyn. 8 (2014), 883--932,
  [publisher page](https://ems.press/journals/ggd/articles/12777).  This is a
  general source for groupoid Busemann cocycles and their cohomology.  The
  rational primitive-section proof in HCS-C18 is elementary and does not claim
  a new groupoid formalism.
- D. Mayer, *The Thermodynamic Formalism Approach to Selberg's Zeta Function
  for PSL(2,Z)*, Bull. AMS 25 (1991), 55--60,
  [DOI](https://doi.org/10.1090/S0273-0979-1991-16068-1), and A. Pohl with
  P. Wabnitz, *Selberg Zeta Functions, Cuspidal Accelerations, and Existence of
  Strict Transfer Operator Approaches*, Memoirs AMS 318 (2026), no. 1616,
  [DOI](https://doi.org/10.1090/memo/1616).  These sources establish that
  standard modular/geodesic transfer-operator closure reaches Selberg zeta.
  HCS-C18's theorem delta is the explicit algebraic
  cusp-coboundary/full-boundary-period dichotomy, not another Selberg
  determinant.  The rational transfer function is discontinuous and
  unbounded, so no analytic transfer-operator conjugacy is claimed.

The fixed-point classification of real modular transformations and the
formula \(\ell(g)=2\operatorname{arcosh}(|\operatorname{tr}g|/2)\) are
classical.  They are used as proof ingredients, not advertised as discoveries.

## 4. Congruence scattering matrices

- M. N. Huxley, *Scattering Matrices for Congruence Subgroups*, in *Modular
  Forms, Durham 1983*, Horwood (1984), 141--156.  Huxley computed the
  congruence scattering matrices for trivial nebentypus.  The historical
  source has no stable public DOI; its bibliographic data and role are
  corroborated in the published sources below.
- F. Cakoni and S. Chanillo, *Transmission Eigenvalues and the Riemann Zeta
  Function in Scattering Theory for Automorphic Forms on Fuchsian Groups of
  Type I*, Acta Math. Sin. (Engl. Ser.) 35 (2019), 987--1010,
  [DOI](https://doi.org/10.1007/s10114-019-8128-8).  Their Theorem 2.8 prints
  the exact prime block and the squarefree tensor formula used as HCS-C18's
  source lock.
- M. Levitin and A. Strohmaier, *Computations of Eigenvalues and Resonances on
  Perturbed Hyperbolic Surfaces with Cusps*, IMRN 2021, 4003--4050,
  [DOI](https://doi.org/10.1093/imrn/rnz157).  Equation (19) gives the same
  squarefree tensor product and records its Huxley--Hejhal provenance.
- M. P. Young, *Explicit Calculations with Eisenstein Series*, J. Number
  Theory 199 (2019), 1--48,
  [DOI](https://doi.org/10.1016/j.jnt.2018.11.007),
  [primary preprint](https://arxiv.org/abs/1710.03624).  Young gives explicit
  cusp/newform Eisenstein basis changes and the character-friendly
  decomposition.  Consequently, neither the fixed Walsh basis nor the finite
  local eigenfactors are standalone novelty claims.

The HCS-C18 corollary that a family with one fixed eigenbasis has
permutation-invariant spectral-parameter products is elementary linear
algebra.  Its contribution is a conditional warning for models that elect to
use those matrices as successive steps, not a claim that the spectral
parameter is time and not a new formula for \(\Phi_N\).  Fixed-basis
commutativity is asserted only in the frozen Huxley--Hejhal
width/Atkin--Lehner normalization, not under arbitrary \(s\)-dependent cusp
renormalization.

## 5. Off-diagonal and twisted directions

- E. M. K\i ral, *Opposite Sign Kloosterman Sum Zeta Function*,
  [arXiv:1504.01860](https://arxiv.org/abs/1504.01860), develops the spectral
  continuation of a relevant off-diagonal Kloosterman zeta family.
- N. Diamantis, S. Friedberg, and F. Str\"omberg, *Sums of Kloosterman Sums
  Formed with Modular Symbols*,
  [arXiv:2607.10786](https://arxiv.org/abs/2607.10786), constructs a current
  modular-symbol twist and continues the associated zeta to
  \(\Re s>1/2\).
- D. Borthwick, C. Judge, and P. Perry, *Selberg's Zeta Function and the
  Spectral Geometry of Geometrically Finite Hyperbolic Surfaces*,
  [arXiv:math/0310364](https://arxiv.org/abs/math/0310364), relates Selberg
  zeta, relative scattering phase, and resonances.

These sources make an important scope distinction.  Off-diagonal matrix
coefficients and projector-resolved paths can retain information that a
plain trace loses, but that territory is already close to mature
Kloosterman/relative-scattering theory.  HCS-C18 records one positive
projector witness and makes no novelty claim for a new twisted zeta.

## 6. Closest claims and defensible delta

| HCS-C18 statement | prior status | defensible project status |
|---|---|---|
| open-geodesic count and sojourn formula | Pujahari--Satpathy | classical input |
| explicit \(Z_{\rm sc}\) two-term formula | immediate Euler-product consequence | positive control, very low novelty |
| projective automorphy cocycle | standard Busemann/groupoid construction | classical input |
| rational cusp projective-section cocycle is an algebraic coboundary via primitive vectors | elementary consequence | proved compatibility lemma; no analytic conjugacy |
| nonzero full-boundary periods are signed Selberg lengths | classical fixed-point facts | proved period-support synthesis; no determinant identity |
| squarefree tensor scattering formula | Huxley/Hejhal; printed in later sources | classical input |
| fixed Walsh eigenchannels | immediate tensor algebra/Atkin--Lehner characters | classical corollary |
| frozen bare spectral-parameter products are permutation-invariant | immediate simultaneous diagonalization | conditional modeling obstruction |
| projectors restore assignment/path sensitivity | elementary finite matrix fact | positive scope control only, not intrinsic chronology |
| every standard channel retains the shifted zeta quotient divisor | local-factor line classification | proved scoped divisor corollary |

## 7. Novelty ruling

External theorem novelty is **low**.  No new scattering formula or groupoid
machinery is claimed.  The synthesis value is moderate: the
project closes the rational ordinary-loop repair and shows that a bare
squarefree spectral-parameter product is permutation-invariant in the frozen
normalization.  It also identifies the off-diagonal structure needed to leave
that commutative algebra.  That compatibility result is the paper's
defensible contribution.
