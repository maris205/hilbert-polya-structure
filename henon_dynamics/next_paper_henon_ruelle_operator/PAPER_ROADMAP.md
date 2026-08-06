# Paper roadmap

> Priority note (2026-08-05): retained as a foundation/control/fallback plan.
> The breadth-first candidate tournament in
> `../next_paper_henon_candidate_search/` now controls next-paper selection.

Working title:

> **Certified Hausdorff Dimension of a Local Area-Preserving Hénon Basic Set
> via Effective Ruelle Operators**

## 1. Paper thesis

The paper will not claim a Hilbert--Pólya construction. Its single thesis is:

> The certified local hyperbolic survivor of the area-preserving Hénon map at
> \(a=6\), equipped with its intrinsic instability roof, supports an explicitly
> defined Ruelle operator whose real pressure is approximated by
> cylinder-memory matrices with effective, machine-checkable error bounds, and
> whose unique Bowen root certifies the Hausdorff dimension of that local set.

The minimum new theorem is the complete certified chain from Hénon interval
geometry to an explicit Hausdorff-dimension interval. A complex determinant
statement is an optional strengthening, never inferred from finite sections
alone.

## 2. Dependency chain from Paper 5

Paper 5 introduced the exact area-preserving recurrence

\[
H_a(q,p)=(1-aq^2-p,q),\qquad \det DH_a=1.
\]

The roadmap keeps that map and the search for intrinsic trace/determinant data.
It does not inherit Paper 5's low-parameter critical-value interpretation,
quartic Schrödinger surrogate, fitted \(\hbar_{\rm eff}\), target schedules, or
legacy Markov construction.

The immediate theorem chain is:

\[
\text{Paper 5 map}
\longrightarrow
\text{certified }H_6\text{ local survivor}
\longrightarrow
\text{intrinsic non-lattice instability roof}
\longrightarrow
\text{effective Ruelle limit}
\longrightarrow
\text{certified }\dim_H\Lambda_*.
\]

This preserves genuine chronological dynamics: the shift records admissible
source-to-target histories, and no time-dependent process is replaced by an
averaged transition matrix.

## 3. Theorem architecture

### Theorem A -- effective geometric roof regularity

On the certified coding \(\pi:\Sigma_A\to\Lambda_*\), use the inherited
normalized tangent coordinates

\[
\widetilde u=\delta q/(7/48),\qquad
\widetilde v=\delta p/(41/256),
\qquad r=123/112.
\]

At a phase point \(z=(q,p)\in\Lambda_*\), if
\(E^u(z)=\{(\widetilde u,m^u(z)\widetilde u)\}\) in those coordinates, define
the positive physical adapted Jacobian and its symbolic pullback by

\[
\bar J^u_{\rm ad}(z)=|-12q-rm^u(z)|,
\qquad
\bar\tau_{\rm ad}=\log\bar J^u_{\rm ad},
\qquad
\tau_{\rm ad}=\bar\tau_{\rm ad}\circ\pi.
\]

The inherited lower bound is \(\bar J^u_{\rm ad}\ge773/224>1\). Prove that

\[
\operatorname{var}_m(\tau_{\rm ad})\le C_0\theta^m
\]

for explicit, machine-checked \(C_0>0\) and \(0<\theta<1\).

Novel burden: connect the existing cone/contraction certificate to an interval
unstable graph transform and publish all constants.

### Theorem B -- effective one-sided reduction

There are explicit \(u\) and future-dependent \(\tau^+\) such that

\[
\tau_{\rm ad}=\tau^++u-u\circ\sigma,
\]

with computable Hölder and truncation bounds. Every periodic sum is exactly
preserved.

Pointwise positivity of \(\tau^+\) is a separate obligation. If it is not
proved, the original positive two-sided \(\tau_{\rm ad}\) defines the
suspension and \(\tau^+\) is used only for the operator; no constant may be
added.

Novel burden: turn the classical Sinai cohomology lemma into a reproducible
effective construction for this Hénon coding.

### Theorem C -- specified analytic Ruelle family

On a named Banach space, with metric and norm written in the theorem,

\[
(\mathcal L_s f)(x)=
\sum_{\sigma y=x}e^{-s\tau^+(y)}f(y)
\]

is bounded and analytic in \(s\); for real \(s\) it has the required
Ruelle--Perron--Frobenius leading eigenvalue, and the stated quasi-compactness
or essential spectral-radius estimate holds.

Novel burden: specify exactly which standard theorem is used and verify every
hypothesis with the effective constants. Quasi-compactness is not described as
nuclearity.

### Theorem D -- finite-memory convergence

For cylinder envelopes \(\underline\tau_m\le\tau^+\le
\overline\tau_m\), choose one frozen representative
\(\widehat\tau_m\), and prove at least

\[
\|\tau^+-\widehat\tau_m\|_\infty\le C_1\theta^m
\]

and, for real \(s\),

\[
|P(-s\tau^+)-P(-s\widehat\tau_m)|
\le |s|C_1\theta^m.
\]

For complex isolated spectral data, freeze an analytic eigenvalue/logarithm
branch and use a named theorem with explicit spectral separation, uniform
Lasota--Yorke constants, and strong/weak norm assumptions. Do not claim
whole-spectrum Hausdorff convergence from entrywise matrix convergence.

For real \(s>0\), pressure monotonicity gives

\[
P(-s\underline\tau_m)\ge P(-s\tau^+)
\ge P(-s\overline\tau_m).
\]

If \(\inf\underline\tau_m>0\) is certified, the envelope pressures have
unique roots and, with \(h(\eta)\) denoting the root for roof \(\eta\),

\[
h(\overline\tau_m)\le h_*\le h(\underline\tau_m).
\]

If envelope positivity is not certified, do not call their crossings unique
roots. Use the finite matrices only to certify sign inequalities

\[
P(-s_L\overline\tau_m)>0,
\qquad
P(-s_U\underline\tau_m)<0.
\]

The target identity
\(P(-s\tau^+)=P(-s\tau_{\rm ad})\), together with positivity of
\(\tau_{\rm ad}\), then yields the unique target root bracket
\(s_L<h_*<s_U\).

Certify the finite-matrix spectral radii with interval Collatz--Wielandt
bounds.

### Theorem E -- certified Bowen root and Hausdorff dimension

There is a unique \(h_*>0\) satisfying

\[
P(-h_*\tau^+)=P(-h_*\tau_{\rm ad})=0,
\]

and \(h_*\) lies in a machine-checkable interval whose width includes both
rounding and memory-truncation error.

The pressure computation uses the positive adapted representative, whereas
the dimension theorem uses Euclidean unit-vector expansion. For the physical
adapted unstable basis on the physical set

\[
\bar e^u_{\rm ad}(z)=(7/48,(41/256)m^u(z)),
\qquad \bar b_u(z)=\log\|\bar e^u_{\rm ad}(z)\|_2,
\]

first prove the exact invariant-frame identity

\[
DH_6(z)\bar e^u_{\rm ad}(z)
=\lambda_u(z)\bar e^u_{\rm ad}(H_6z),
\qquad
\lambda_u(z)=-12q-rm^u(z),
\]

and certify that \(\bar b_u\) is bounded Hölder. Taking Euclidean norms gives
the exact gauge bridge

\[
\bar\tau_E^u(z)=\log\|DH_6(z)|_{E^u(z)}\|_2
=\bar\tau_{\rm ad}(z)+\bar b_u(H_6z)-\bar b_u(z).
\]

For the symbolic pullbacks
\(b_u=\bar b_u\circ\pi\) and
\(\tau_E^u=\bar\tau_E^u\circ\pi\), the same identity is

\[
\tau_E^u=\tau_{\rm ad}+b_u\circ\sigma-b_u.
\]

Thus the adapted and Euclidean potentials have identical periodic sums and
pressure. Certify that \(\Lambda_*\) is locally maximal as well as mixing and
uniformly hyperbolic. Apply the exact surface-basic-set dimension theorem to
obtain

\[
d^u(\Lambda_*)=h_*.
\]

Let \(\bar J_E^{u,s}(z)\) be the Euclidean Jacobians and
\(\bar\alpha(z)\) the Euclidean angle between the stable and unstable unit
lines. Area preservation gives the physical coboundary identity

\[
\log\bar J_E^u(z)+\log\bar J_E^s(z)
=\log\sin\bar\alpha(z)-\log\sin\bar\alpha(H_6z).
\]

Equivalently, after pullback to \(\Sigma_A\),

\[
\log J_E^u+\log J_E^s
=\log\sin\alpha-\log\sin\alpha\circ\sigma.
\]

After interval-certifying the angle away from zero, set
\(g=\log\sin\alpha\) and verify explicitly that the stable geometric potential
obeys

\[
\tau_E^s:=-\log J_E^s=\tau_E^u-g+g\circ\sigma.
\]

Thus the Euclidean stable and unstable geometric potentials are cohomologous
and their pressure roots agree. Their one-step Euclidean representatives are
not assumed pointwise positive; uniqueness is transferred from the positive
adapted roof. State the stable Bowen equation first for \(H_6^{-1}\)
along \(E^s\), then justify its reindexing as
\(P_\sigma(-t\tau_E^s)=0\). If the selected theorem assumes a compact ambient
surface, construct and certify an extension agreeing with \(H_6\) near the
isolating neighborhood; otherwise cite a genuinely local version. Verify the
local-product dimension theorem and certify

\[
d^u(\Lambda_*)=d^s(\Lambda_*)=h_*,
\qquad
\dim_H\Lambda_*=2h_*.
\]

This is the primary intrinsic geometric output and applies only to the local
survivor.

The inherited irrational ratio of two primitive roof periods rules out an
arithmetic roof. After checking all hypotheses of the applicable suspension
theorem, derive the corollary

\[
\pi_{\rm dyn}(T)
=\#\{p\text{ primitive}:T_p\le T\}
\sim \frac{e^{h_*T}}{h_*T}.
\]

This is the precise arithmetic-looking structure earned by the dynamics. It
does not identify Hénon orbits with prime numbers and does not upgrade Route-A
A1 beyond weak status.

### Optional Theorem F -- local determinant

Only after constructing a nuclear operator on a suitable holomorphic space or
proving a uniform periodic-orbit tail, identify a determinant. Prove
holomorphy on a neighborhood of the selected contour and its closed interior
(or track all poles in a meromorphic version), including any required analytic
continuation beyond the log-series convergence half-plane, before certifying a
zero count.

If Theorem F fails, publish Theorems A--E without a determinant subtitle or
complex-zero claim. If the failure yields a general obstruction, promote that
obstruction to a negative theorem.

## 4. Manuscript outline

### 1. Introduction

- State the operator-limit gap, not the Hilbert--Pólya dream, as the problem.
- Give the exact minimum theorem and the determinant fallback.
- Explain the local nature of \(\Lambda_*\).

### 2. What survives from the original Hénon model

- Define Paper 5's map and exact area preservation.
- Record the linear conjugacy to the standard conservative Hénon convention.
- Separate durable dynamics from legacy low-parameter and quartic-surrogate
  claims.
- State that the proof parameter is \(a=6\), not \(a\simeq1.02\).

### 3. Certified symbolic base

- Four rectangles and the six source-to-target coverings.
- Source-row/target-column adjacency convention.
- Hyperbolicity, contraction, conjugacy, mixing, and locality.
- Exact unweighted determinant \(1-z-z^3-z^4\), emphasizing that it is not
  \(1-2z\).

### 4. Effective instability roof

- Interval unstable graph transform in the inherited adapted tangent
  coordinates.
- Positivity of \(\bar J^u_{\rm ad}\) and regularity of \(\tau_{\rm ad}\).
- Proof and certificate for \(C_0,\theta\).
- Positivity and inherited non-lattice witness.

### 5. One-sided cohomology

- Reference-past construction.
- Telescoping convergence and explicit tail.
- Periodic-sum invariance and the original-roof fallback if the one-sided
  representative is not pointwise positive.

### 6. The Ruelle operator

- Symbolic metric and Banach norm.
- Boundedness, analyticity, conjugation symmetry.
- Real RPF theorem and essential spectrum.
- A boxed warning separating quasi-compact and nuclear operators.

### 7. Finite-memory theorem

- Cylinder roof intervals.
- Sparse matrix construction.
- Real pressure bound.
- Optional isolated complex-spectrum perturbation theorem, clearly outside the
  dimension minimum.
- Complexity and reproducibility.

### 8. Certified Bowen root and Hausdorff dimension

- Monotonicity and uniqueness.
- Interval bracketing and memory tail.
- Independent checker.
- Certified adapted-to-Euclidean norm coboundary and periodic-sum invariance.
- Isolating neighborhood and local maximality.
- Euclidean stable/unstable angle coboundary and matching slice roots.
- Local-product theorem and total dimension interval.
- Non-arithmetic suspension prime-orbit corollary and its exact non-claim.

### 9. Controls and failure analysis

- Constant and exact finite-memory roofs.
- Flat, shuffled, random, precision, and memory controls.
- Cycle/matrix orientation audit.
- Which finite roots fail to persist.

### 10. Optional determinant theorem

- Exact determinant convention.
- Nuclear or periodic-tail proof.
- Holomorphy/meromorphy on the contour interior and any analytic-continuation
  theorem.
- Fixed-contour Rouché certificate.
- Omit this section entirely if the theorem gate fails.

### 11. Route-A assessment and non-claims

- A1 remains weak: certified local periodic orbits are not prime-like.
- The evaluation is `NOT_TESTABLE` before source lock. Once testable, A2 is
  `A2_FAIL` without a \(\xi\)-divisor result; a valid local dynamical zeta is
  not enough.
- A3 remains `A3_FAIL` after Theorems A--E. It can become partial only if Theorem
  F provides the controlled determinant continuation/tail; no functional
  equation, Gamma factor, trivial zeros, or Riemann--von Mangoldt law follows.
- A4 evidence is `NOT_TESTABLE` in this paper; if the inherited lift hint is
  scored, use at most `A4_FORMAL_HINT`. Route B is not authorized.

### Appendices

- Dependency manifest and exact conventions.
- Interval graph-transform constants.
- Effective cohomology proof.
- Perturbation theorem hypotheses.
- Adapted-to-Euclidean gauge, local-maximality, Euclidean angle-coboundary,
  and Hausdorff-dimension certificates.
- Machine-readable certificate schemas and reproduction commands.

## 5. Figure and table plan

No figure is made before its theorem or diagnostic role is fixed.

1. Dependency diagram from Paper 5 to Theorems A--F.
2. Four-state directed graph with source/target convention.
3. Certified cylinder width \(W_m\) and analytic envelope
   \(C_0\theta^m\).
4. Pressure/root and \(\dim_H\Lambda_*\) interval widths versus memory depth.
5. Known-truth controls versus Hénon roof convergence.
6. Optional fixed-contour modulus and Rouché margin.
7. Table of all constants, hashes, and theorem dependencies.
8. Route-A verdict table with explicit non-claims.

## 6. Work packages and calendar

### Weeks 1--2: T0 and R000--R015

- Complete G000's primary-source theorem-delta audit.
- Freeze dependencies and conventions.
- Run known-truth prototypes and geometry interface checks.
- Complete the local-maximality and dimension-theorem/ambient-applicability
  preflight before roof production.
- Deliverable: R001 protocol, dependency manifest, and R015 preflight
  certificates.

If G000 finds that the proposed minimum is only a routine instance of an
existing validated pressure algorithm, strengthen the paper to a reusable
geometry-to-operator certificate theorem or make Theorem F mandatory before
continuing.

### Weeks 3--5: T1 / R020

- Implement interval unstable graph transform.
- Prove and independently check cylinder-variation constants.
- Kill condition: no usable exponential bound after justified subdivision.

### Weeks 6--7: T2 / R030

- Construct future-dependent roof and effective coboundary.
- Verify all inherited periodic sums.

### Weeks 8--10: T3--T4 / R040--R050

- Freeze the Banach-space theorem.
- Build sparse memory matrices and known-truth tests.
- Prove pressure and isolated-leading-spectrum approximation.

### Weeks 11--13: T5 / R060--R080

- Certify the real pressure root.
- Consume R015 and complete R065's stable/unstable and Hausdorff-dimension
  certificate.
- Run independent cycle and structural controls.
- At this point a minimum paper decision is possible.

### Weeks 14--16: optional T6 / R090

- Attempt holomorphic/nuclear or periodic-tail route.
- Use one fixed contour only after the theorem exists.
- Stop T6 cleanly if the uniform bound fails.

### Week 17: R100 and manuscript freeze

- Independent certificate checker.
- Route-A evaluation.
- Reproducibility and claim audit.

## 7. Decision tree

- **A--F pass:** submit the dimension paper with a determinant strengthening.
- **A--E pass, F fails:** submit the certified local-Hénon Hausdorff-dimension
  paper with a documented determinant limitation.
- **A--D pass, E dimension gate fails:** improve only certified
  local-maximality/angle/interval geometry; do not publish a Hausdorff claim.
- **A or B fails:** stop this route; further finite matrices do not repair the
  missing continuous object.

## 8. Candidate-search boundary

This Ruelle paper is the certified fallback C00. The quantum route is HCS-C09
and may start only after its external-prior-art gate, cutoff/operator freeze,
trace-class proof, and a result stronger than the standard fixed-time Hénon
trace formula. Neither lane is preselected by the other.
