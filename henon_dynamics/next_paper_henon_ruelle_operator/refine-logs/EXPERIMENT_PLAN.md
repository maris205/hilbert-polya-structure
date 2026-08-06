# Claim-driven experiment plan

Status: **design frozen at the level of theorem gates; numerical protocol must
be frozen in R001 before production runs**.

## 1. Research question

For the certified four-state local survivor \(\Lambda_*\) of

\[
H_6(q,p)=(1-6q^2-p,q),
\]

can the geometric instability roof be represented by a future-dependent
Hölder potential whose finite-memory transfer matrices converge, with explicit
and machine-checkable error bounds, to the pressure and leading spectral data
of a specified Ruelle operator?

The primary geometric question is whether the unique pressure root can be
certified as the stable/unstable slice dimension and hence half the Hausdorff
dimension of this local area-preserving basic set. The optional final question
is whether the same bounds are strong enough to define and certify a local
dynamical determinant on one fixed complex domain. It is not assumed that the
determinant answer is positive.

## 2. Frozen mathematical objects

### 2.1 Base system

- Map: \(H_6(q,p)=(1-6q^2-p,q)\).
- Smoothness/invertibility: record the exact \(C^\infty\) inverse

  \[
  H_6^{-1}(q,p)=(p,1-6p^2-q)
  \]

  and \(\det DH_6=1\).
- Scope: only the certified local survivor \(\Lambda_*\), never the full
  bounded Hénon set.
- State order: \((--,-+,+-,++)\).
- Adjacency convention: rows are sources and columns are targets,

  \[
  A=\begin{pmatrix}
  1&0&1&0\\
  1&0&0&0\\
  0&1&0&1\\
  0&1&0&0
  \end{pmatrix}.
  \]

- Symbolic dynamics: the two-sided mixing SFT \((\Sigma_A,\sigma)\), its
  one-sided future shift \((\Sigma_A^+,\sigma)\), and the certified coding
  \(\pi:\Sigma_A\to\Lambda_*\).
- Basic-set obligation: certify an open isolating neighborhood for which
  \(\Lambda_*\) is the maximal invariant set. Conjugacy plus hyperbolicity is
  not silently substituted for local maximality.
- Ambient-surface obligation: use a dimension theorem stated locally on a
  surface, or certify a \(C^{1+\alpha}\) compact-surface extension that agrees
  with \(H_6\) on a neighborhood of the isolating set. A theorem whose stated
  hypotheses require a compact ambient surface is not applied directly to
  \(\mathbb R^2\) without this bridge.

The source/target convention is a hard invariant. A non-palindromic closed word
must be used in every implementation test so that an accidental transpose is
detectable.

### 2.2 Roof and metric

- Positive adapted roof inherited from the certified cone construction. In
  normalized tangent coordinates

  \[
  \widetilde u=\delta q/(7/48),\qquad
  \widetilde v=\delta p/(41/256),
  \qquad r=123/112,
  \]

  at \(z=(q,p)\in\Lambda_*\), write
  \(E^u(z)=\{(\widetilde u,m^u(z)\widetilde u)\}\) and set

  \[
  \bar J^u_{\rm ad}(z)=|-12q-rm^u(z)|,
  \qquad
  \bar\tau_{\rm ad}(z)=\log\bar J^u_{\rm ad}(z),
  \qquad
  \tau_{\rm ad}=\bar\tau_{\rm ad}\circ\pi.
  \]

  The inherited certificate gives
  \(\bar J^u_{\rm ad}\ge773/224>1\). Its symbolic pullback is the suspension
  clock and the representative used for monotone pressure bounds.
- Euclidean dimension potential. In physical tangent coordinates set

  \[
  \bar e^u_{\rm ad}(z)=(7/48,(41/256)m^u(z)),
  \qquad \bar b_u(z)=\log\|\bar e^u_{\rm ad}(z)\|_2,
  \]

  and certify

  \[
  \bar\tau_E^u(z)=\log\|DH_6(z)|_{E^u(z)}\|_2
  =\bar\tau_{\rm ad}(z)+\bar b_u(H_6z)-\bar b_u(z).
  \]

  Pull back by \(\pi\): with \(b_u=\bar b_u\circ\pi\) and
  \(\tau_E^u=\bar\tau_E^u\circ\pi\),

  \[
  \tau_E^u=\tau_{\rm ad}+b_u\circ\sigma-b_u.
  \]

  The two symbolic potentials are not treated as pointwise identical. Their
  pressures and periodic sums agree because their difference is the displayed
  coboundary.
- Symbolic metric:

  \[
  d_\vartheta(x,y)=\vartheta^{N(x,y)},\qquad 0<\vartheta<1,
  \]

  where the exact definition of \(N\), the Hölder exponent, and the norm are
  frozen before production calculations.
- One-sided representative: \(\tau^+\) must be constructed with an explicit
  transfer function \(u\) satisfying

  \[
  \tau_{\rm ad}=\tau^++u-u\circ\sigma.
  \]

Periodic sums must agree identically, not just numerically.

- Stable potential and angle. On the physical set define the Euclidean
  Jacobians \(\bar J_E^{u,s}(z)\) and angle \(\bar\alpha(z)\). Their symbolic
  pullbacks are \(J_E^{u,s}=\bar J_E^{u,s}\circ\pi\) and
  \(\alpha=\bar\alpha\circ\pi\), with stable potential

  \[
  \tau_E^s=-\log J_E^s.
  \]

  Here both physical Jacobians and \(\bar\alpha\) use Euclidean unit vectors.
  Directed interval bounds must keep \(\sin\bar\alpha\) away from zero and
  verify

  \[
  \log\bar J_E^u(z)+\log\bar J_E^s(z)
  =\log\sin\bar\alpha(z)-\log\sin\bar\alpha(H_6z),
  \]

  equivalently, on the symbolic space,

  \[
  \log J_E^u+\log J_E^s
  =\log\sin\alpha-\log\sin\alpha\circ\sigma.
  \]

  Hence, with \(g=\log\sin\alpha\), verify the signed consequence

  \[
  \tau_E^s=\tau_E^u-g+g\circ\sigma.
  \]

  Freeze the stable Bowen convention explicitly: it starts with unstable
  expansion for \(H_6^{-1}\) along \(E^s\), then is reindexed as

  \[
  P_\sigma(-t\tau_E^s)=0,
  \qquad \tau_E^s=-\log J_E^s.
  \]

  This identity is distinct from the adapted-to-Euclidean roof bridge.

### 2.3 Operator and determinant

The minimal operator is

\[
(\mathcal L_s f)(x)
=\sum_{\sigma y=x}e^{-s\tau^+(y)}f(y)
\]

on one named Hölder or Walters space. The compact real and complex parameter
domains are frozen in R001.

The following objects remain distinct throughout:

1. the bounded operator \(\mathcal L_s\);
2. its real leading eigenvalue and pressure;
3. a finite-memory matrix \(L_{s,m}\);
4. the suspension Euler product;
5. the two-variable periodic determinant;
6. a genuine nuclear/Fredholm determinant, if one is proved to exist.

No equality among items 4--6 is used without a theorem covering the stated
space and domain.

## 3. Claims and falsifiers

| ID | Intended claim | Required evidence | Decisive falsifier |
|---|---|---|---|
| C1 | The inherited adapted roof has an effective cylinder bound \(\operatorname{var}_m(\tau_{\rm ad})\le C_0\theta^m\). | Interval graph transform, explicit \(C_0\), \(\theta<1\), independent checker. | No useful contraction after subdivision, or a violated interval bound. |
| C2 | A future-dependent \(\tau^+\) is effectively cohomologous to \(\tau_{\rm ad}\). | Constructed \(u\), norm/variation bounds, exact periodic-sum invariance. | A closed word whose two sums differ beyond certified arithmetic. |
| C3 | Finite-memory transfer matrices give controlled upper/lower bounds for real pressure and leading Perron data. Complex isolated branches are optional. | Cylinder envelopes, pressure monotonicity/Lipschitz bounds, interval Perron estimates, and known-truth controls; a named two-norm theorem only for any complex extension. | Real enclosures are inconsistent or fail the analytic envelope; any complex claim lacks spectral isolation or its perturbation theorem. |
| C4 | The unique real root satisfies \(d^u=d^s=h_*\) and \(\dim_H\Lambda_*=2h_*\); the non-lattice roof also yields the standard local prime-orbit asymptotic. | Root bracket, R015 local-basic-set/theorem preflight, adapted-to-Euclidean gauge certificate, Euclidean angle coboundary and exact stable-root transport, product-dimension theorem, independent reproduction, and non-arithmetic suspension theorem. An independent stable computation counts only if it has its own variation/tail certificate. | The root is not uniquely enclosed, either coboundary fails, any dimension-theorem hypothesis fails, exact stable-root transport fails, or the prime-orbit hypotheses fail. |
| C5 | Optional: a local determinant and fixed-contour zero count are rigorous. | Named analytic-domain and nuclearity/uniform-tail theorem; holomorphy on a neighborhood of the contour and its closed interior, or a complete meromorphic pole ledger; any required continuation domain; and a Rouché/argument-principle certificate. | No interior analytic-domain theorem, an untracked pole, no uniform contour separation/tail bound, or a determinant convention that depends on truncation. |

C1--C4 are the minimum positive paper. C5 is not required for publication and
must be dropped if its theorem gate fails.

## 4. Experimental units and leakage rules

The primary units are admissible symbolic cylinders, closed symbolic words,
and certified Hénon orbit intervals. They are deterministic mathematical
objects, so no bootstrap confidence intervals or pseudo-population p-values
will be reported.

Forbidden inputs before all theorem and control decisions are frozen:

- primes, primality labels, Riemann zeros, \(\zeta\), \(\xi\), or target
  spectra;
- affine rescaling chosen by a target comparison;
- parameter or memory selection based on attractive complex roots;
- averaged transition matrices for any non-autonomous extension;
- cycles outside the certified local survivor presented as complete data;
- neighboring-parameter reuse without a separate survivor and roof
  certificate.

## 5. Run matrix

### G000 -- primary-source theorem-delta audit

Before pilot code, compare the exact intended statements and error models with:

- general Ruelle/Fredholm determinant theorems;
- explicit eigenvalue bounds on holomorphic transfer-operator spaces;
- validated min--max/finite-rank pressure computations;
- prior periodic-orbit and transport calculations for the area-preserving
  Hénon map;
- any Hénon-specific geometric-potential thermodynamic formalism.
- surface-basic-set Bowen dimension formulae, certified dimension algorithms,
  and prior dimension results for hyperbolic area-preserving Hénon maps.

Outputs: `refine-logs/G000_THEOREM_DELTA.md` and
`refine-logs/G000_SOURCE_LEDGER.json`, containing a
claim/assumption/error-bound matrix showing what is inherited, what is an
application, and what is genuinely new. If only the numerical value of a
standard pressure root is new, T0--T5 are not by themselves a publication
gate; a reusable end-to-end certificate theorem or T6 becomes mandatory.

### R000 -- theorem-aware pilot

Purpose: determine only numerical feasibility, interval precision, subdivision
depth, memory range, and storage cost.

Allowed observations:

- contraction margins;
- interval widths;
- wall time and memory;
- exact known-truth control errors.

Forbidden observations:

- comparisons with arithmetic targets;
- selection of contours because a visually interesting Hénon root appears.

Output: a draft protocol. Pilot artifacts are marked `development_only` and
cannot be used as confirmatory evidence.

### R001 -- immutable protocol and dependency lock

Freeze:

- dependency SHA-256 hashes;
- source/target and shift conventions;
- symbolic metric, strong/weak Hölder exponents and Banach norms (candidate
  \(C^\alpha\hookrightarrow C^\beta\), \(0<\beta<\alpha\)), the exact
  perturbation theorem, uniform Lasota--Yorke constants, and spectral
  separation region;
- adapted roof, one-sided cohomology, Euclidean dimension potential, pressure,
  matrix, zeta, and determinant conventions;
- the tangent-coordinate scales \(7/48\), \(41/256\), and \(r=123/112\),
  plus the exact adapted-to-Euclidean gauge formula;
- dimension theorem/version and any erratum, Euclidean stable/unstable
  Jacobian and angle conventions, the \(H_6^{-1}\)-to-\(\sigma\) stable
  pressure reindexing, isolating-neighborhood criterion, and local-versus-
  compact-ambient applicability;
- finite-memory layout: admissible \((m-1)\)-words are states, each admissible
  \(m\)-word is a chronological source-to-target edge, and its cylinder roof
  weight is attached to that edge;
- interval package, directed-rounding mode, working precisions;
- memory depths and compact \(s\)-domains;
- all success, fallback, and stop criteria;
- environment and source-control state.

The top-level workspace is currently recorded as
`source_control: NOT_A_GIT_WORKTREE`; provenance therefore relies on hashes,
immutable configs, package versions, and artifact manifests rather than an
invented commit identifier.

### R010 -- inherited geometry interface check

Re-run the independent checks for:

- six source-to-target coverings;
- cone/hyperbolicity inequalities;
- mutual rectangle separation;
- symbolic contraction/coding;
- the complete inherited period range.

This is an interface audit, not a re-claim of the inherited theorem.

### R015 -- local-basic-set and dimension-theorem preflight

Run the minimum paper's geometric kill gate before investing in roof/operator
production:

1. certify an open isolating neighborhood and
   \(\Lambda_*=\bigcap_{n\in\mathbb Z}H_6^n(U)\);
2. freeze the exact slice-dimension and product-dimension theorem versions,
   including applicable errata;
3. verify compactness, invariance, \(C^{1+\alpha}\) regularity, one-dimensional
   splitting, hyperbolicity, and transitivity/mixing inputs inherited through
   R010;
4. certify that the theorem is local on \(\mathbb R^2\), or construct the
   required compact-surface extension agreeing with \(H_6\) near \(U\);
5. write a hypothesis ledger marking only the later Euclidean-potential,
   angle, and pressure certificates as pending.

Outputs: `basic_set_certificate.json` and
`dimension_theorem_preflight.json`. Failure stops the dimension-paper route
before R020; it is not postponed until after a pressure root is computed.

### R020 -- unstable graph transform and variation certificate

For paired points/cylinders with a common central word:

1. enclose the coded phase-space rectangles;
2. enclose the unstable slope by interval graph transform;
3. enclose the physical \(\bar J^u_{\rm ad}\) and
   \(\bar\tau_{\rm ad}=\log\bar J^u_{\rm ad}\), then record their symbolic
   pullbacks;
4. prove the exact invariant-frame identity
   \(DH_6\bar e^u_{\rm ad}=(-12q-rm^u)\bar e^u_{\rm ad}\circ H_6\), certify
   bounded Hölder constants for
   \(\bar b_u=\log\|(7/48,(41/256)m^u)\|_2\), and derive both the physical
   \(H_6\)-coboundary and symbolic \(\sigma\)-coboundary algebraically before
   interval-enclosing their quantities;
5. propagate the contraction estimate;
6. distinguish two-sided central-cylinder variation from one-sided future
   variation;
7. combine the coding contraction and unstable graph-transform contraction by
   taking the slower certified rate, and use the positive \(\bar J^u_{\rm ad}\)
   lower bound when passing to \(\tau_{\rm ad}\);
8. derive \(C_0\) and \(\theta\);
9. verify observed cylinder widths lie inside the analytic envelope.

Primary artifacts:

- `variation_certificate.json`;
- `roof_gauge_bridge_certificate.json`;
- per-depth cylinder width table;
- independent directed-rounding check.

The gauge certificate must include the exact frame identity, Hölder/bounded
data for \(\bar b_u\), the symbolic pullback, and telescoping cancellation of
every closed-orbit sum; a small numerical residual alone is insufficient.

### R030 -- effective one-sided cohomology

Choose and freeze an admissible reference past separately for each possible
initial state of a future and prove that the reference map is continuous.
Construct \(u\) by the convergent telescoping series supplied by the Sinai
cohomology argument. Bound
the truncation tail with R020 constants and form interval cylinders for
\(\tau^+\), starting from \(\tau_{\rm ad}\).

Tests:

- cohomology residual enclosure;
- positivity or, if it is not proved, an explicit declaration that the
  original positive two-sided adapted roof defines the suspension;
- equality of periodic sums for every inherited primitive word through the
  certified period range;
- reference-past change gives a coboundary-equivalent result.

### R040 -- known-truth operator controls

Run the full matrix and root pipeline on the same adjacency graph with:

1. a constant positive roof, whose pressure equation is explicit;
2. a one-step roof, whose transfer matrix is exact at memory one;
3. a synthetic \(k\)-memory roof, which must become exact at memory \(k\);
4. a high-precision non-interval implementation compared with the interval
   implementation.

Any failure blocks Hénon interpretation.

### R050 -- finite-memory Hénon operators

For the frozen memory sequence, nominally \(m=2,\ldots,16\) subject to R000
resource limits:

- enumerate admissible \(m\)-cylinders without dense full-shift padding;
- compute \(\underline\tau_m\), \(\overline\tau_m\), and one frozen
  \(\widehat\tau_m\);
- certify and record whether \(\inf\underline\tau_m>0\); this flag controls
  whether envelope crossings may be called unique roots;
- assemble the three corresponding sparse matrices using the R001
  \((m-1)\)-state/\(m\)-edge and source-row/target-column convention;
- enclose real leading eigenvalues and pressure;
- track only isolated complex spectral components covered by the named
  perturbation theorem, frozen strong/weak spaces, uniform Lasota--Yorke
  constants, spectral separation, and logarithm branch;
- record strong- and weak-norm bounds separately.

The production output must never infer an infinite spectrum from visual
stability alone.

### R060 -- real pressure-root certification

For each accepted memory depth:

- obtain interval upper and lower pressure functions;
- use cohomology invariance to identify the target pressure with that of the
  original positive two-sided adapted roof and thereby prove strict
  monotonicity and uniqueness of the **target** zero;
- if \(\inf\underline\tau_m>0\) is certified, bracket with the unique roots of
  the two envelope pressures;
- otherwise, do not assign unique roots to the envelopes: certify
  \(P(-s_L\overline\tau_m)>0\) and
  \(P(-s_U\underline\tau_m)<0\), which imply \(s_L<h_*<s_U\) by pointwise
  pressure order and target monotonicity;
- add the analytic memory tail to the numerical interval;
- require the final enclosures to be mutually consistent and eventually
  nested after accounting for the proved error.

Output: `pressure_root_certificate.json` with a checker that needs no plotting
code.

After the root certificate, separately verify the hypotheses of the
non-arithmetic suspension prime-orbit theorem. The asymptotic is a theoretical
corollary; the finite period-20 catalogue is not used to claim empirical
large-\(T\) convergence.

### R065 -- Hausdorff-dimension certification

This run turns the pressure root into the paper's primary geometric result:

1. verify the immutable hashes and all completed hypotheses in the R015
   basic-set/theorem-preflight certificates;
2. verify the R020 adapted-to-Euclidean gauge certificate and thereby identify
   the R060 root with the Euclidean unstable Bowen root;
3. identify the unstable slice dimension with that Euclidean Bowen root;
4. interval-enclose physical \(\bar J_E^s\), \(\bar J_E^u\), and
   \(\bar\alpha\), verify the \(H_6\)-identity, and separately verify its
   symbolic pullback using \(J_E^{u,s}\), \(\alpha\), and \(\sigma\);
5. certify that \(g=\log\sin\alpha\) is bounded Hölder, derive the stable
   equation first for \(H_6^{-1}\), and verify the frozen reindexing and exact
   cohomology to \(P_\sigma(-t\tau_E^s)=0\);
6. transport the certified unstable-root interval to the stable root by that
   exact cohomology. An independently computed stable bracket is diagnostic
   unless it has its own certified cylinder-variation and memory-tail bounds;
7. verify the local-product dimension-additivity theorem and output
   \(d^u\), \(d^s\), and \(\dim_H\Lambda_*\) intervals.

Failure of any theorem hypothesis yields `DIMENSION_NOT_CERTIFIED`; it is not
repaired by box-counting plots.

### R070 -- independent cycle comparison

Using a separate closed-word enumerator and the inherited orbit catalogue:

- compare \(\operatorname{tr}L_{s,m}^n\) with symbolic fixed-point sums in the
  regime where the potential is exactly represented;
- compare periodic sums from \(\tau_{\rm ad}\), \(\tau_E^u\), and \(\tau^+\);
- verify primitive/repetition bookkeeping;
- test at least one non-palindromic word to expose transposed dynamics.

This checks implementation consistency; it is not by itself an infinite
determinant theorem.

### R080 -- structural controls and perturbations

Controls are diagnostic, not statistical publication gates:

- constant, unit, and flat roofs;
- shuffled cylinder weights with the graph held fixed;
- random positive roofs matched only in coarse range;
- cycle-level shuffled symbolic periods and same-density random lengths,
  explicitly labeled as determinant controls that need not define a coherent
  transfer-operator potential;
- random phases for complex tests;
- small interval-contained roof perturbations;
- precision and memory changes;
- a neighboring Hénon parameter only if its own invariant set and roof are
  separately certified.

Expected conclusion: which spectral features are forced by adjacency, which
by a non-lattice roof, and which are unstable artifacts.

### R090 -- optional determinant/contour certificate

This run is locked until T6 is proved. Freeze the complex compact set and
contours independently of roots found in production data. Prove holomorphy on
an open neighborhood of every contour and its closed interior (or explicitly
track poles in a meromorphic version), including any analytic continuation
beyond the log-series absolute-convergence domain. Then either:

- evaluate a nuclear Fredholm determinant with a certified approximation
  error; or
- combine complete periodic data with a theorem-level uniform tail bound.

For each contour require

\[
\sup_{s\in\Gamma}|D(s)-D_m(s)|
<\inf_{s\in\Gamma}|D_m(s)|.
\]

Only then report a Rouché zero count. A contour-only tail estimate without
interior holomorphy is insufficient. If the inequality cannot be certified,
report `NOT_CERTIFIED`, not a candidate zero.

### R100 -- independent reproduction and Route-A audit

A second implementation checks all machine-readable certificates. The formal
Route-A evaluator is applied with the exact frozen candidate tuple. Route B
remains unauthorized.

Save each immutable evaluation as
`evaluations/route_a/<candidate_id>/<UTC_timestamp>.yaml`, using the exact
skill schema. Create or update `docs/candidate_registry.md` and
`docs/obstruction_registry.md` as required by the accumulation protocol; these
registry files are not created during planning because no result has yet been
evaluated.

## 6. Primary metrics

### Regularity

- separate two-sided central-cylinder and one-sided future-cylinder widths
  \(W_m^{\pm}\) and \(W_m^+\);
- certified \(C_0,\theta\) and slack ratio
  \(W_m^{\bullet}/(C_0\theta^m)\);
- cohomology residual and tail bound;
- adapted-to-Euclidean norm-coboundary residual and periodic-sum discrepancy;
- lower/upper bounds for \(\tau^+\).

### Operator convergence

- \(\|\tau^+-\widehat\tau_m\|_\infty\), together with separate
  \(\underline\tau_m,\overline\tau_m\) widths;
- real pressure enclosure width;
- leading-eigenvalue enclosure and inter-memory distance;
- strong/weak perturbation constants;
- exact-control discrepancy.

### Pressure root

- envelope-positivity flag and either the raw memory-\(m\) root sandwich or
  the two certified pressure-sign margins;
- analytic truncation inflation;
- final certified root width;
- monotonicity and uniqueness margins.

### Hausdorff dimension

- isolating-neighborhood margins;
- local-theorem applicability or compact-surface extension certificate;
- minimum Euclidean stable/unstable angle, roof-gauge residual, and
  area-coboundary residual enclosure;
- \(H_6^{-1}\)-to-symbolic stable-pressure convention check;
- unstable Bowen-root interval and its exact cohomology-transported stable
  interval; optional independent stable diagnostic with a separate
  variation/tail status;
- slice-root overlap margin;
- final \(\dim_H\Lambda_*\) interval and theorem-version manifest;
- independent checker verdict.

### Optional determinant

- analytic-domain theorem/version and verified closed-interior coverage;
- absolute-convergence and analytic-continuation domains;
- meromorphic pole ledger, if applicable;
- cycle/matrix trace discrepancy;
- uniform tail bound on each contour;
- minimum contour modulus;
- Rouché margin and winding number;
- independent zero count.

## 7. Success gates

### Minimum paper gate

All of the following are required:

1. T0--T5 are proved.
2. \(C_0\) and \(\theta<1\) are explicit and machine-checked.
3. Known-truth controls pass exactly or within certified rounding.
4. The real root has a unique finite interval with a proved memory tail.
5. R065 proves the local-basic-set and dimension-formula hypotheses and gives
   a machine-checkable interval for \(\dim_H\Lambda_*\).
6. A second implementation reproduces the certificate.
7. No Riemann or prime data entered design, selection, or validation.

### Strong paper gate

The minimum gate plus T6, verified holomorphy on the contour's closed interior
(or a complete meromorphic pole ledger), and at least one fixed-contour zero
count with positive Rouché margin.

### Negative-result gate

A publishable negative result requires a theorem, not only failed numerics;
examples include a proved obstruction to nuclearity on the natural chosen
space, or a certified demonstration that a finite-memory complex root leaves
every allowed limiting enclosure.

## 8. Stop conditions

Stop rather than accumulating more matrices if any persists after reasonable
subdivision and precision increases:

- the unstable bundle or roof cannot be enclosed on the certified survivor;
- no explicit exponential cylinder bound is obtained;
- one-sided periodic sums fail exact invariance;
- no appropriate perturbation theorem applies to the claimed spectral data;
- the real root cannot be uniquely bracketed;
- local maximality, angle control, or the Hausdorff-dimension theorem cannot be
  certified (stop the minimum-paper claim);
- a required compact-ambient bridge or stable-pressure reindexing cannot be
  certified (stop the minimum-paper claim);
- determinant nuclearity/tail control fails (stop T6 only; retain T0--T5).

## 9. Required artifacts

Every production run writes:

- immutable config and its SHA-256;
- dependency manifest and hashes;
- environment/package manifest;
- interval arithmetic mode and precision;
- command line and wall-clock record;
- machine-readable results plus schema version;
- independent-check result;
- human-readable analysis separating theorem, computation, inference, and
  non-claim.

Minimum project-level artifacts additionally include
`dimension_theorem_preflight.json`, `roof_gauge_bridge_certificate.json`,
`basic_set_certificate.json`, `angle_coboundary_certificate.json`, and
`hausdorff_dimension_certificate.json`.
