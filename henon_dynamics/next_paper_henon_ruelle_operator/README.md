# Next paper: certified dimension via a Hénon Ruelle operator

Status: **certified foundation/control/fallback lane; no longer preselected as
the RH flagship or the immediate next paper**.

Priority note (2026-08-05): the breadth-first Hénon search in
`../next_paper_henon_candidate_search/` supersedes the earlier N+1/N+2
ordering. This package remains valuable as a rigorous dynamical-systems paper
and as common certified infrastructure. It may re-enter the main slot only
after it produces evidence beyond a non-arithmetic pressure/dimension result.

Primary legacy source:

- `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`

Working title:

> **Certified Hausdorff Dimension of a Local Area-Preserving Hénon Basic Set
> via Effective Ruelle Operators**

## Original candidate decision (retained as a scoped fallback)

Paper 5's durable object is the exact reversible, area-preserving Hénon family,
not its later quartic continuum surrogate or zero fit. Subsequent repository
work has now certified a local hyperbolic survivor for \(H_6\), its symbolic
dynamics, and a positive non-lattice instability roof. The missing theorem is
the effective operator limit and its intrinsic geometric consequence: finite
cycle sections have been computed, but no specified continuous Ruelle
operator, finite-memory approximation theorem, or certified Hausdorff
dimension of this survivor has been established. That gap remains a clean
rigorous continuation of Paper 5, but it is not by itself a new
Hilbert--Pólya bridge. A determinant theorem remains an optional Route-A
strengthening rather than the minimum-paper claim.

## Single mathematical question

Let \(\Lambda_*\) be the certified four-state local survivor of

\[
H_6(q,p)=(1-6q^2-p,q),
\]

let \(\pi:\Sigma_A\to\Lambda_*\) be the certified symbolic conjugacy, and for
\(z\in\Lambda_*\) let

\[
\bar\tau_{\rm ad}(z)=\log \bar J^u_{\rm ad}(z),
\qquad
\tau_{\rm ad}=\bar\tau_{\rm ad}\circ\pi
\]

be the inherited positive instability roof in the certified adapted tangent
coordinates. Can one:

1. construct an explicit one-sided Hölder representative \(\tau^+\)
   cohomologous to \(\tau_{\rm ad}\), with a computable cylinder-variation
   bound;
2. define a specified analytic family of Ruelle operators

   \[
   (\mathcal L_s f)(x)
   =\sum_{\sigma y=x}e^{-s\tau^+(y)}f(y)
   \]

   on a named Banach space;
3. prove that locally constant \(m\)-memory transfer matrices give explicit
   exponential upper/lower bounds for real pressure and leading Perron data,
   treating complex isolated branches only if a separate perturbation theorem
   applies;
4. certify that the unique pressure root is the unstable slice dimension and,
   using area preservation, that

   \[
   \dim_H\Lambda_*=2h_*;
   \]

5. only if a uniform contour/tail theorem is obtained, certify a nonreal
   determinant zero?

## Dominant contribution

> An end-to-end computer-assisted theorem that converts certified Hénon
> geometry into an explicit Ruelle-pressure enclosure and a machine-checkable
> Hausdorff-dimension interval for the local basic set.

The main paper is about an intrinsic geometric invariant obtained through a
controlled operator limit. Root plots are secondary outputs. Riemann zeros are
not inputs or validation targets.

## Why this is the right continuation of Paper 5

Retained from Paper 5:

- the exact area-preserving Hénon recurrence;
- reversibility and genuine chronological iteration;
- the search for a trace/determinant built from intrinsic dynamics.

Not retained:

- \(a_c\simeq1.00561\) or \(a\simeq1.02\) as certified critical values;
- the LL finite-sample statistic;
- the stored chaotic-layer coefficient;
- fitted \(\hbar_{\rm eff}\), quartic confinement, or phase unwrapping;
- static/logarithmic schedules selected from target behavior;
- the legacy Markov matrix or any averaged non-autonomous transition matrix;
- zero matching, GUE-only evidence, or hardware analogies.

The proof regime is \(a=6\) because the repository has certified a local
hyperbolic survivor there. The project does not claim that this local survivor
is the full bounded repeller or full binary horseshoe.

## Frozen inherited theorems and data

The new paper may cite, but must independently check the interfaces to:

1. R058 exact h-set covering and cone certificates;
2. R059 symbolic contraction and conjugacy;
3. the four-state mixing SFT with unweighted determinant
   \(1-z-z^3-z^4\);
4. the positive Hölder instability roof;
5. the non-lattice witness;
6. the 2,170 primitive **local** cycles through period 20;
7. the existing finite-section controls and their A3 failure.

Every inherited artifact will be content-addressed in an immutable dependency
manifest. The 2,170-cycle catalogue is not a global Hénon orbit catalogue.

## Theorem ladder

### G0. External theorem-delta audit

Before R000, compare the intended effective Hénon result against rigorous
pressure computation, holomorphic transfer-operator approximation, general
dynamical-determinant theory, and prior area-preserving Hénon cycle work. The
deliverable is a theorem-by-theorem delta table, not a keyword search.

If T0--T5 reduce to a routine substitution into an existing validated
algorithm, publication requires either a reusable new geometry-to-operator
certificate theorem or T6. No implementation result can waive G0.

### T0. Source lock and object definition

Freeze:

- \(H_6\), \(\Lambda_*\), \(A\), and \(\pi\);
- adapted roof orientation, tangent-coordinate scales, Euclidean
  unstable-Jacobian convention, and the exact norm-gauge bridge;
- one-sided shift convention;
- Banach space and norm;
- transfer-operator normalization;
- determinant/zeta convention;
- allowed complex domain and contour;
- all inherited hashes and forbidden data.

No numerical spectrum may be interpreted before T0 is complete.

### T1. Effective Hölder/cylinder bound

Use the R059 contraction and an interval graph-transform bound for unstable
directions to prove

\[
\operatorname{var}_m(\tau_{\rm ad})
\le C_0\theta^m,
\qquad 0<\theta<1,
\]

with explicit \(C_0,\theta\), not merely an observed slope.

### T2. One-sided cohomology

Construct explicit \(u\) and \(\tau^+\) satisfying

\[
\tau_{\rm ad}=\tau^++u-u\circ\sigma,
\]

where \(\tau^+\) depends only on future coordinates. Prove effective bounds
for \(\|u\|\) and \(\operatorname{var}_m(\tau^+)\). Either prove
\(\tau^+>0\), or retain the original positive two-sided \(\tau_{\rm ad}\) as the
suspension roof and use \(\tau^+\) only for the one-sided operator. Periodic
orbit sums must be unchanged exactly; adding a constant is not an allowed
positivity repair.

### T3. Specified Ruelle operator

Define \(\mathcal L_s\) on a named Hölder space
\(C^\alpha(\Sigma_A^+)\), or on a rigorously constructed holomorphic space if
a nuclear determinant is pursued. Prove boundedness, analytic dependence on
\(s\), and the relevant Ruelle--Perron--Frobenius/quasi-compactness statement.

Do not call \(\det(I-\mathcal L_s)\) a Fredholm determinant on a Hölder space
without an actual determinant theorem.

### T4. Finite-memory convergence

Build cylinder envelopes \(\underline\tau_m\le\tau^+\le
\overline\tau_m\), choose one representative \(\widehat\tau_m\) between
them, and construct the corresponding finite matrices. Prove first:

\[
\|\tau^+-\widehat\tau_m\|_\infty\le C_1\theta^m.
\]

For \(s\) in a frozen **real** interval, prove

\[
|P(-s\tau^+)-P(-s\widehat\tau_m)|
\le |s|C_1\theta^m,
\]

using the variational pressure inequality only for real-valued potentials.
On a frozen complex domain, discuss only analytic isolated-eigenvalue branches
with an explicit spectral gap, logarithm branch, and named strong/weak
perturbation theorem.

If direct operator norm convergence fails in the strong Hölder norm, use the
stated two-norm perturbation theorem rather than hiding the failure.

For real \(s>0\), exploit pointwise order and interval
Collatz--Wielandt bounds:

\[
P(-s\underline\tau_m)\ge P(-s\tau^+)
\ge P(-s\overline\tau_m).
\]

If \(\inf\underline\tau_m>0\) is certified, both envelope pressures are
strictly decreasing and their unique roots satisfy

\[
h(\overline\tau_m)\le h_*\le h(\underline\tau_m).
\]

Otherwise, do not assign unique roots to the envelopes. Instead certify

\[
P(-s_L\overline\tau_m)>0,
\qquad
P(-s_U\underline\tau_m)<0,
\]

which, together with
\(P(-s\tau^+)=P(-s\tau_{\rm ad})\) and positivity of
\(\tau_{\rm ad}\), proves \(s_L<h_*<s_U\).

### T5. Certified dimension root

For real \(s\), use the original positive adapted roof, monotonicity,
interval pressure bounds, and pressure's cohomology invariance to certify the
unique solution

\[
P(-h_*\tau^+)=P(-h_*\tau_{\rm ad})=0

\]

inside a reported interval. Prove its memory-truncation error. This is a
dynamical pressure root, not an arithmetic constant.

The dimension potential is a different pointwise representative. At a phase
point \(z\in\Lambda_*\), set

\[
\bar e^u_{\rm ad}(z)=(7/48,(41/256)m^u(z)),
\qquad
\bar b_u(z)=\log\|\bar e^u_{\rm ad}(z)\|_2.
\]

First prove

\[
DH_6(z)\bar e^u_{\rm ad}(z)
=(-12q-rm^u(z))\bar e^u_{\rm ad}(H_6z)
\]

and certify that \(\bar b_u\) is bounded Hölder. Taking Euclidean norms then
gives on the physical system

\[
\bar\tau_E^u(z)
=\log\|DH_6(z)|_{E^u(z)}\|_2
=\bar\tau_{\rm ad}(z)+\bar b_u(H_6z)-\bar b_u(z).
\]

After pullback by \(\pi\), with
\(b_u=\bar b_u\circ\pi\) and
\(\tau_E^u=\bar\tau_E^u\circ\pi\), this is

\[
\tau_E^u=\tau_{\rm ad}+b_u\circ\sigma-b_u.
\]

Thus \(P(-h_*\tau_E^u)=0\) by cohomology invariance. Then verify that
\(\Lambda_*\) is a locally maximal mixing hyperbolic basic set
in the exact hypotheses of the selected surface-diffeomorphism dimension
theorem. Prove that the unstable slice dimension is \(h_*\). With physical
Euclidean Jacobians \(\bar J_E^{u,s}(z)\) and angle \(\bar\alpha(z)\), use area
preservation to certify

\[
\log \bar J_E^u(z)+\log \bar J_E^s(z)
=\log\sin\bar\alpha(z)-\log\sin\bar\alpha(H_6z).
\]

Equivalently, the symbolic pullbacks satisfy

\[
\log J_E^u+\log J_E^s
=\log\sin\alpha-\log\sin\alpha\circ\sigma.
\]

Thus, with \(\tau_E^s=-\log J_E^s\) and
\(g=\log\sin\alpha\),

\[
\tau_E^s=\tau_E^u-g+g\circ\sigma.
\]

The Euclidean stable and unstable geometric potentials are cohomologous, so
their Bowen roots agree; no pointwise positivity in the Euclidean norm is
assumed. Uniqueness is inherited from cohomology with the positive adapted
roof. Derive the stable equation first for \(H_6^{-1}\), then justify
the reindexing to \(P_\sigma(-t\tau_E^s)=0\). Also verify that the selected
dimension theorem is local on \(\mathbb R^2\), or provide a certified compact-
surface extension equal to \(H_6\) near the isolating set. After verifying the
local product theorem's hypotheses, conclude

\[
d^u(\Lambda_*)=d^s(\Lambda_*)=h_*,
\qquad
\dim_H\Lambda_*=2h_*.
\]

The result is only for the certified local survivor, not for the full Hénon
nonwandering set.

As a corollary, verify the hypotheses of the non-arithmetic suspension
prime-orbit theorem and state

\[
\#\{p\text{ primitive}:T_p\le T\}
\sim \frac{e^{h_*T}}{h_*T}.
\]

This is a prime-orbit theorem for the local Hénon suspension, not a
correspondence with arithmetic primes.

### Stretch T6. Local dynamical determinant

Define one explicit two-variable convention, for example

\[
D(z,s)=
\exp\!\left(
-\sum_{n\ge1}\frac{z^n}{n}
\sum_{\sigma^n x=x}e^{-s(\tau^+)_n(x)}
\right).
\]

Here \((\tau^+)_n(x)=\sum_{k=0}^{n-1}\tau^+(\sigma^k x)\).

Obtain either a nuclear-operator theorem or an independent periodic-orbit tail
bound uniform on a fixed contour **and its interior**. Prove that the limiting
and approximating determinants are holomorphic on a neighborhood of that
closed interior (or track all poles in a meromorphic formulation), including
the analytic continuation beyond the absolute-convergence half-plane when
needed. Only then use Rouché's theorem or the argument principle to certify a
zero count or a nonreal zero.

If T6 fails, the paper stops honestly at T5.

## Experiment design

The computational program has five independent layers:

1. interval geometry and roof-variation bounds;
2. one-sided cohomology and cylinder enclosures;
3. finite-memory matrices and pressure/eigenvalue convergence;
4. local-maximality, stable/unstable, and Hausdorff-dimension certification;
5. independent periodic-orbit traces/determinants and known-truth controls.

Memory depths, complex domains, precision, and contours are frozen after a
pilot and before the main convergence/root analysis. Detailed runs and metrics
are in [refine-logs/EXPERIMENT_PLAN.md](refine-logs/EXPERIMENT_PLAN.md).

## Route-A interpretation

| Layer | Intended result | Honest limitation |
|---|---|---|
| A1: primitive orbits | Certified local orbit definition, completeness, repetitions, phases/signs, monodromy, and intrinsic non-lattice clock | No prime-like orbit correspondence; expected to remain A1_WEAK |
| A2: dynamical zeta | T0--T5 specify the candidate but do not validate a target divisor | The evaluation is `NOT_TESTABLE` before source lock; once testable, expect `A2_FAIL` without a \(\xi\)-divisor result; internal cycle/matrix consistency is not an A2 pass |
| A3: analytic structure | T0--T5 provide operator and pressure foundations; only T6 can supply controlled determinant continuation/tails | `A3_FAIL` without T6; at most `A3_PARTIAL_ANALYTIC_STRUCTURE` if T6 passes; still no functional equation, Gamma factor, trivial zeros, or global Riemann counting law |
| A4: natural lift | Not evaluated by this classical operator paper | Evidence is `NOT_TESTABLE` here; if the inherited symplectic/quantization hint is scored, the ceiling is `A4_FORMAL_HINT`; the quantum route is deferred and Route B unauthorized |

Expected overall status after T0--T5: a rigorous classical operator result but
`A2_FAIL`, `A3_FAIL`, and at most `A4_FORMAL_HINT` for the Hilbert--Pólya
candidate; overall `ROUTE_A_EXPLORATORY`. T6 could conditionally raise A3 to
partial analytic structure without creating an arithmetic match.

## Publication success and failure modes

Minimum positive paper:

- T0--T5 proved with explicit constants;
- independent finite-memory and cycle computations agree within certified
  bounds;
- leading root bracket stable and reproducible;
- the surface dimension theorem's local-maximality, regularity, angle, and
  product-structure hypotheses are certified, yielding an interval for
  \(\dim_H\Lambda_*\);
- the non-lattice hypothesis is used to derive the local suspension
  prime-orbit corollary, with no arithmetic relabeling;
- all control and dependency manifests pass.

Stronger paper:

- T6 fixed-contour determinant certification;
- one nonreal zero or resonance certified without finite-section promotion.

Valuable negative paper:

- a rigorous demonstration that the Hölder operator is quasi-compact but no
  nuclear/Fredholm determinant compatible with the desired cycle weights is
  available on the tested natural spaces; or
- a proof that observed complex finite-section roots are not stable under the
  controlled operator limit.

## Hard stop conditions

- No named Banach space or operator norm.
- No explicit roof-variation constant.
- Direct prime or Riemann-zero lookup.
- Retuning after viewing a sealed contour/root region.
- Calling a finite matrix determinant the continuous determinant.
- Claiming nuclearity from quasi-compactness.
- Replacing chronological dynamics with an average matrix.
- Treating the local four-state survivor as the full Hénon repeller.
- Interpreting the leading real root or a finite complex root as an arithmetic
  constant.

## Project files

- [SOURCE_AUDIT.md](SOURCE_AUDIT.md): Paper-5 corrections, dependency ledger,
  prior-art boundary, and G0 novelty burden.
- [PAPER_ROADMAP.md](PAPER_ROADMAP.md): manuscript plan, milestones, and
  fallback ladder.
- [refine-logs/FINAL_PROPOSAL.md](refine-logs/FINAL_PROPOSAL.md): frozen
  contribution and theorem obligations.
- [refine-logs/EXPERIMENT_PLAN.md](refine-logs/EXPERIMENT_PLAN.md): run matrix,
  metrics, controls, and artifacts.
- [refine-logs/EXPERIMENT_TRACKER.md](refine-logs/EXPERIMENT_TRACKER.md): live
  gate ledger.
- [code/README.md](code/README.md): planned implementation.
- [results/README.md](results/README.md): artifact contract.
- [paper/README.md](paper/README.md): manuscript claim contract.
- [evaluations/route_a/README.md](evaluations/route_a/README.md): formal
  evaluation status discipline.
- [REPOSITORY_UPDATE.md](REPOSITORY_UPDATE.md): planning update.

## Core references

- M. Hénon, *Numerical study of quadratic area-preserving mappings*, Q. Appl.
  Math. 27 (1969), 291--312.
- D. G. Sterling, H. R. Dullin, and J. D. Meiss, *Homoclinic bifurcations for
  the Hénon map*. <https://arxiv.org/abs/chao-dyn/9904019>
- C. Liverani, *Fredholm determinants, Anosov maps and Ruelle resonances*.
  <https://arxiv.org/abs/math/0505049>
- S. Friedland and G. Ochs, *Hausdorff dimension, strong hyperbolicity and
  complex dynamics*. <https://doi.org/10.3934/dcds.1998.4.405>
- O. Jenkinson and M. Pollicott, rigorous effective dimension bounds via
  transfer operators. <https://arxiv.org/abs/1611.09276>
- Internal R058/R059 proof packages and the completed instability-roof project
  listed in the dependency manifest to be created at T0.
