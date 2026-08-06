# Final research proposal

## Problem anchor

The exact area-preserving Hénon map in Paper 5 has now generated two strong
local classical results in the repository: a certified symbolic hyperbolic
survivor and a positive non-lattice instability roof. Yet every weighted zeta
or operator comparison remains finite. The missing object is not another
catalogue or grid; it is a continuous transfer operator with a proved
approximation theorem and an intrinsic geometric quantity that the operator
certifies.

## Specific failure mode

Existing finite cycle sections and restricted matrices show useful numerical
windows but nonmonotone refinement and root drift. They do not establish:

- which Banach space carries the intended transfer operator;
- whether the operator is bounded, quasi-compact, or nuclear;
- whether finite-memory/cycle approximations converge uniformly;
- whether an infinite determinant exists in the stated convention;
- whether any observed complex zero persists under the operator limit.
- whether the apparent real pressure root rigorously equals the Hausdorff
  dimension data of the explicitly certified local survivor.

Consequently the current Route-A analytic-structure verdict remains failed.

## Gap after prior work

General thermodynamic formalism for mixing subshifts and Hölder potentials is
classical, and general dynamical determinant theorems exist. The project-level
gap is an **effective, certified realization** for this exact Hénon survivor:

- explicit constants inherited from the contraction and cone geometry;
- an explicit one-sided representative of the geometric roof;
- interval-enclosed cylinder approximants;
- rigorous finite-memory error bounds;
- a machine-checkable leading pressure root;
- a verified Bowen dimension theorem and Hausdorff-dimension interval for this
  exact local basic set;
- optionally, a fixed-contour determinant certificate.

The paper must not present a standard abstract Ruelle theorem as new. Its
contribution is the explicit certified Hénon geometry-to-operator-to-dimension
chain and its machine-checkable constants.

## Chosen contribution

> Construct the Ruelle operator for the certified \(H_6\) instability
> potential, prove effective finite-memory pressure bounds, and certify that
> the unique root gives
> \(d^u(\Lambda_*)=d^s(\Lambda_*)=h_*\) and
> \(\dim_H\Lambda_*=2h_*\), with a determinant statement only to the extent
> justified by a nuclear or periodic-tail theorem.

## Why this route dominates

- It closes the exact theorem obligation left by both Hénon successor projects.
- It uses intrinsic, target-free data.
- It turns the real root into an intrinsic fractal dimension rather than an
  otherwise artificial suspension constant.
- It preserves chronological dynamics.
- It can produce a rigorous positive or negative result.
- It advances operator/analytic structure rather than adding finite roots.
- It avoids the heavy external overlap now identified for quantum Hénon maps.

## Mathematical objects

### Base dynamics

Use only the certified local survivor \(\Lambda_*\subset\mathbb R^2\) of
\(H_6\) and its mixing four-state SFT \((\Sigma_A,\sigma)\). The conjugacy is
\(\pi:\Sigma_A\to\Lambda_*\).

### Roof

For \(z\in\Lambda_*\), let

\[
\bar\tau_{\rm ad}(z)=\log\bar J^u_{\rm ad}(z)>0,
\qquad
\tau_{\rm ad}=\bar\tau_{\rm ad}\circ\pi.
\]

This is the inherited positive Hölder representative in adapted tangent
coordinates; the prior project also proves non-lattice behavior. The new paper
needs effective constants, a one-sided cohomologous representative, and a
certified coboundary bridge to the Euclidean unit-vector potential required by
the dimension theorem.

### One-sided operator

For a frozen convention,

\[
(\mathcal L_s f)(x)
=\sum_{\sigma y=x}e^{-s\tau^+(y)}f(y),
\qquad x\in\Sigma_A^+.
\]

The minimal Banach space is a named Hölder space with an explicit metric and
norm. A holomorphic/nuclear space is optional and must be constructed, not
assumed.

### Determinant conventions

Keep separate:

1. the operator \(\mathcal L_s\);
2. its leading eigenvalue/pressure;
3. the suspension zeta

   \[
   \zeta_{\rm susp}(s)
   =\prod_p(1-e^{-sT_p})^{-1};
   \]

4. the two-variable periodic determinant

   \[
   D(z,s)=\exp\!\left[-\sum_{n\ge1}\frac{z^n}{n}
   \sum_{\sigma^n x=x}e^{-s(\tau^+)_n(x)}\right],
   \qquad
   (\tau^+)_n=\sum_{k=0}^{n-1}\tau^+\circ\sigma^k;
   \]

5. any genuine Fredholm/nuclear determinant.

No equality between these is asserted without the applicable theorem and
domain.

## Theorem obligations

### T0. Immutable dependency and convention lock

Create a manifest hashing R058/R059 geometry, adjacency, conjugacy data,
instability-roof code/results, cycle catalogues, and all conventions. Record
the exact candidate tuple required by the Route-A evaluator.

### T1. Effective roof regularity

Prove a cylinder-variation bound using interval geometry and graph transform:

\[
\operatorname{var}_m(\tau_{\rm ad})\le C_0\theta^m.
\]

Both constants must be explicit and independently checked.

### T2. Effective Sinai cohomology reduction

Construct \(u\) and future-dependent \(\tau^+\) with

\[
\tau_{\rm ad}=\tau^++u-u\circ\sigma.
\]

Prove Hölder constants and exact preservation of periodic sums. If pointwise
positivity of \(\tau^+\) is not proved, define the suspension with the original
positive two-sided \(\tau_{\rm ad}\) and use \(\tau^+\) only for the operator; do not add
a constant, which would alter periods and the pressure root.

### T3. Operator theorem

Name the metric, exponent, Banach norm, domain, and normalization. Prove:

- boundedness and analytic dependence on \(s\);
- the real Ruelle--Perron--Frobenius eigenvalue;
- quasi-compactness/essential spectral-radius control needed downstream;
- conjugation symmetry on the chosen complex family.

Nuclearity is a separate obligation.

### T4. Effective memory approximation

For admissible \(m\)-cylinders, construct
\(\underline\tau_m\le\tau^+\le\overline\tau_m\), one frozen representative
\(\widehat\tau_m\), and their finite matrices. Prove uniform roof and **real**
pressure bounds. For complex leading-spectral claims, freeze a spectral
isolation region and logarithm branch and verify every hypothesis of a named
weak/strong two-norm perturbation theorem.

### T5. Certified Bowen root and Hausdorff dimension

Certify the unique real \(h_*>0\) satisfying

\[
P(-h_*\tau^+)=P(-h_*\tau_{\rm ad})=0
\]

and provide an explicit memory/truncation error.

Using the R020 invariant-frame certificate, construct the Euclidean unstable
potential on the physical set. For \(z\in\Lambda_*\), use the inherited
adapted basis

\[
\bar e^u_{\rm ad}(z)=(7/48,(41/256)m^u(z)),
\qquad \bar b_u(z)=\log\|\bar e^u_{\rm ad}(z)\|_2,
\]

certify

\[
\bar\tau_E^u(z)=\log\|DH_6(z)|_{E^u(z)}\|_2
=\bar\tau_{\rm ad}(z)+\bar b_u(H_6z)-\bar b_u(z).
\]

After pullback, \(b_u=\bar b_u\circ\pi\) and
\(\tau_E^u=\bar\tau_E^u\circ\pi\) obey

\[
\tau_E^u=\tau_{\rm ad}+b_u\circ\sigma-b_u.
\]

Hence the exact target pressure root enclosed by the adapted finite-memory
bounds is the Euclidean Bowen root; no finite-memory approximant is identified
with that limit. Consume the earlier R015 certificate that the exact survivor
is a locally maximal mixing basic hyperbolic set in the hypotheses of the
selected dimension theorem. Then certify

\[
d^u(\Lambda_*)=h_*.
\]

For physical Euclidean unit stable/unstable directions, their Jacobians
\(\bar J_E^{u,s}\), and their angle \(\bar\alpha\), verify

\[
\log\bar J_E^u(z)+\log\bar J_E^s(z)
=\log\sin\bar\alpha(z)-\log\sin\bar\alpha(H_6z).
\]

Equivalently, the symbolic pullbacks satisfy

\[
\log J_E^u+\log J_E^s
=\log\sin\alpha-\log\sin\alpha\circ\sigma.
\]

Consequently, for \(g=\log\sin\alpha\), the stable geometric potential satisfies

\[
\tau_E^s:=-\log J_E^s=\tau_E^u-g+g\circ\sigma.
\]

It is therefore cohomologous to the unstable Euclidean geometric potential;
neither Euclidean one-step representative is assumed pointwise positive.
Root uniqueness is transferred from the positive adapted roof, so
the stable Bowen equation, first stated for \(H_6^{-1}\) and then reindexed as
\(P_\sigma(-t\tau_E^s)=0\), has root \(h_*\). Verify either a local
surface-basic-set dimension theorem or a certified compact-surface extension
equal to \(H_6\) near the isolating set. Then verify the local
product/dimension-additivity hypotheses and conclude

\[
\dim_H\Lambda_*=2h_*.
\]

All three quantities receive explicit intervals. These are dimensions of the
local survivor, not the full Hénon nonwandering set.

Verify the standard non-arithmetic suspension hypotheses and derive the
primitive-orbit asymptotic

\[
\pi_{\rm dyn}(T)
=\#\{p:T_p\le T\}
\sim \frac{e^{h_*T}}{h_*T}.
\]

The result concerns primitive local Hénon orbits and is not an encoding of
number-theoretic primes.

### T6. Optional determinant theorem

Either:

- construct a holomorphic complex-neighborhood operator that is nuclear and
  identify its Fredholm determinant; or
- derive a periodic-orbit tail bound sufficient for a fixed compact domain.

In either case prove holomorphy on an open neighborhood of the contour and its
closed interior, or explicitly account for every pole in a meromorphic
version. A continuation theorem beyond the logarithmic orbit series'
absolute-convergence half-plane is required whenever the contour leaves it.
Only then certify complex zeros by Rouché/argument principle. If neither route
works, state the Fredholm obstruction and omit infinite-determinant zeros.

## Minimal computational tests

1. Known-truth constant and finite-memory potentials on the same SFT.
2. Interval cylinder variation versus memory depth.
3. Pressure and leading eigenvalue versus memory depth and precision.
4. Independent cycle-trace comparison through the complete inherited period.
5. Certified real-root brackets nested across memory.
6. Independent check of the exact stable-root transport, angle coboundary, and
   dimension interval. A separately computed stable bracket is a certificate
   only with its own cylinder-variation and memory-tail artifact hashes;
   otherwise it is diagnostic.
7. Random-weight, random-phase, flat-roof, and perturbed-roof controls.
8. Fixed contour comparison only after T6 supplies a tail theorem.

No prime or Riemann-zero data is permitted.

## Scope and non-claims

In scope:

- effective thermodynamic formalism on \(\Lambda_*\);
- finite-memory operator approximation;
- certified pressure/leading spectrum;
- certified stable/unstable slice and total Hausdorff dimension of
  \(\Lambda_*\);
- local determinant only if justified;
- explicit Route-A reassessment.

Out of scope:

- the full bounded Hénon repeller;
- a global horseshoe-threshold proof;
- the mixed \(a\simeq1.02\) phase space;
- quantum Hénon spectra;
- Riemann-zero fitting or prime encoding;
- functional equation, Gamma factor, or completed \(\xi\);
- Route B.

## Key risks

1. General theory may make a non-effective proof insufficiently novel.
2. Effective unstable-direction Hölder constants may be too coarse for useful
   memory depths.
3. Hölder-space quasi-compactness does not imply a Fredholm determinant.
4. Complex roots may be finite-memory artifacts even when pressure converges.
5. One-sided cohomology can preserve periodic sums while losing an easy
   positivity bound if normalized carelessly.
6. Interval overestimation can prevent a useful root bracket.
7. The local survivor must never be upgraded to a global repeller claim.
8. Local maximality or dimension-additivity hypotheses may not follow from the
   inherited conjugacy without an additional certified neighborhood theorem.

## Fallback ladder

1. T0--T6: full operator and local determinant paper.
2. T0--T5: certified local-Hénon Hausdorff-dimension paper.
3. T0--T4 plus a proved determinant obstruction: negative operator paper.
4. If T1 effective constants fail, stop; more finite matrices are not a paper.

## Route-A expectation

- A1: remains weak without prime-like content, though orbit bookkeeping is
  certified.
- A2: the whole evaluation is `NOT_TESTABLE` before source lock; once
  testable, expect `A2_FAIL` without a \(\xi\)-divisor result. Internal
  determinant consistency is insufficient.
- A3: remains `A3_FAIL` after T0--T5; only a successful T6 can justify
  `A3_PARTIAL_ANALYTIC_STRUCTURE` for the dynamical object itself.
- A4: evidence remains `NOT_TESTABLE` in this classical paper; if the inherited
  symplectic/quantization hint is scored, use at most `A4_FORMAL_HINT`.

Overall: strong classical dynamics paper, exploratory as an RH candidate,
Route B not authorized.
