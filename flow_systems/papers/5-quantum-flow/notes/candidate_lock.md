# Candidate Lock — `FF-FROB-SUSP-P1-F2-KOOPMAN-P1`

Lock date: 2026-08-13  
Underlying classical ID: `FF-FROB-SUSP-P1-F2`  
Stage: Route A / A4 and project-lead-authorized early Route B / B1--B3  
Change policy: a change of classical system, clock, deleted component,
nonconstant density, coupling, potential, or boundary condition creates a new
candidate ID

## 1. Locked operator object

```yaml
candidate_id: FF-FROB-SUSP-P1-F2-KOOPMAN-P1
candidate_definition: >-
  Koopman pullback group of the unchanged constant-roof arithmetic-Frobenius
  suspension of discrete P^1(overline(F_2)), represented canonically on the
  Hilbert direct sum of flow-time L^2 spaces of all closed-point circles.
family: natural Koopman lifts of finite-field Frobenius suspensions
underlying_classical_candidate: FF-FROB-SUSP-P1-F2
arithmetic_scheme: P^1_{F_2}
phase_space:
  object: coproduct over closed points x of R/(deg(x) log(2) Z)
  topology: topological coproduct inherited from Paper 4
  topology_status: MODELING_CHOICE inherited, not modified
dynamics:
  formula: phi^t_x(u) = u + t mod deg(x) log(2)
clock:
  unit: suspension flow time
  one_return: log(2)
  status: identical to Paper 4
measure:
  canonical: mu_1 restricted to C_x equals du_x
  allowed_equivalent_family: mu_w restricted to C_x equals w_x du_x
  weight_condition: 0 < w_x < infinity for every x
  canonical_properties:
    - invariant
    - sigma_finite
    - full_support
    - Radon
  probability_status: possible only by noncanonical summable component weights
hilbert_space:
  canonical: H_1 = orthogonal_sum_x L^2(C_x, du_x)
  weighted: H_w = orthogonal_sum_x L^2(C_x, w_x du_x)
unitary_weight_intertwiner:
  formula: (W_w f)_x = sqrt(w_x) f_x
  direction: H_w -> H_1
  result: W_w U_t^(w) = U_t^(1) W_w and W_w A_w = A_1 W_w
koopman_group:
  pullback_convention: (U_t f)_x(u) = f_x(u-t)
  stone_convention: U_t = exp(-i t A_K)
  status: strongly_continuous_unitary_group
operator:
  symbol: A_K
  component_action: A_x f_x = -i d f_x/du
  global_action: orthogonal direct sum over every closed point x
domain:
  component: H^1_per(0, deg(x) log(2))
  global: >-
    all componentwise periodic H^1 vectors for which the weighted sum of
    L^2 norms of f_x and f'_x is finite
boundary_conditions: f_x(0) = f_x(deg(x) log(2)) in periodic Sobolev trace sense
dense_core: finite-component trigonometric polynomials
closedness: self_adjoint_hence_closed
self_adjointness: PROVED
spectral_parameter_map:
  formula: E <-> s = 1/2 + i E
  status: bookkeeping convention only; no target correspondence inferred
quantization_map:
  object: classical-observable pullback under the flow
  status: natural_unitary_lift_not_physical_quantization
orbit_zeta:
  formula: 1 / ((1-2^(-s))(1-2^(1-s)))
  ledger: primitive-orbit/Hasse-Weil ledger inherited from Paper 4
operator_determinant:
  standard_fredholm: undefined for the frozen Koopman inputs
  spectral_zeta_compact_resolvent: unavailable
  equality_to_orbit_zeta: not_claimed
parameters: none
fitted_parameters: none
training_data: none
forbidden_data:
  - Riemann-zero lists
  - rational-prime tables
  - fitted scales, shifts, phases, potentials, or boundary conditions
  - finite-degree cutoffs represented as the full object
  - component coupling under the locked candidate ID
  - substitution of etale Frobenius for the Koopman generator
code_commit: not_applicable_workspace_not_git
artifact_paths:
  - papers/5-quantum-flow/notes/research_protocol.md
  - papers/5-quantum-flow/notes/source_matrix.md
  - papers/5-quantum-flow/notes/candidate_lock.md
  - papers/5-quantum-flow/notes/proof_audit.md
  - papers/5-quantum-flow/notes/composition_blueprint.md
  - papers/5-quantum-flow/notes/sources/
  - papers/5-quantum-flow/code/koopman_spectral_controls.py
  - papers/5-quantum-flow/code/test_koopman_spectral_controls.py
  - papers/5-quantum-flow/experiments/reproduce.sh
  - papers/5-quantum-flow/results/koopman_spectral_manifest.json
```

## 2. Weight-equivalence lock

The canonical representative is \(w_x=1\). The candidate ID denotes its
entire positive component-weight unitary-equivalence class:

\[
 W_w:\mathcal H_w\to\mathcal H_1,\qquad
 (W_wf)_x=\sqrt{w_x}f_x.
\]

This is allowed without re-identification only when every \(w_x\) is a finite,
strictly positive constant on its entire component. The following are new
objects:

- \(w_x=0\), because a closed-point component is deleted;
- an infinite component weight, because it does not define the stated
  component \(L^2\) measure;
- a density varying with \(u\), unless a new group/action and domain audit
  proves invariance and equivalence;
- off-diagonal coupling between different circles.

Thus the choice between counting-times-Lebesgue, normalized component Haar, or
a summable probability weighting has no spectral effect.

## 3. Frozen theorem ledger

Let \(\tau=\log2\), \(d_x=\deg x\), and \(L_x=d_x\tau\).

| Field | Frozen result | Evidence |
|---|---|---|
| closed points by degree | \(a_1=3\); \(a_d=d^{-1}\sum_{e\mid d}\mu_{\rm Mob}(e)2^{d/e}>0\) for every \(d\ge2\) | `PROVED` |
| component generator | \(-i\,d/du\) on \(H^1_{\rm per}(0,L_x)\) | `PROVED` |
| degree-\(d\) frequencies | \(2\pi n/(d\log2)\), \(n\in\mathbb Z\) | `PROVED` |
| point spectrum | \(\sigma_{\rm p}(A_K)=(2\pi/\log2)\mathbb Q\) | `PROVED` |
| point multiplicity | every rational frequency, including zero, has countably infinite multiplicity | `PROVED` |
| full spectrum | \(\sigma(A_K)=\mathbb R\) | `PROVED` |
| essential spectrum | \(\sigma_{\rm ess}(A_K)=\mathbb R\), \(\sigma_{\rm disc}(A_K)=\varnothing\) | `PROVED` |
| spectral-measure type | complete orthonormal eigenbasis; all vector spectral measures are pure point | `PROVED` |
| irrational spectral points | irrational reals are not eigenvalues but are continuous-spectrum accumulation points in the set-theoretic operator spectrum | `PROVED` |
| resolvent | not compact for every \(z\notin\mathbb R\) | `PROVED` |
| local projections | \(\operatorname{rank}\mathbf1_I(A_K)=\infty\) for every interval \(I\) of positive width | `PROVED` |
| centered counting | \(N(E)=\dim\operatorname{Ran}\mathbf1_{[-E,E]}(A_K)=\infty\) for every \(E\ge0\) | `PROVED` |
| heat | \(e^{-tA_K^2}\) and \(e^{-t|A_K|}\) are not trace class for every \(t>0\) | `PROVED` |
| kernel deletion control | removing zero modes does not help because every nonzero rational eigenspace is infinite-dimensional | `PROVED` |
| standard spectral determinant | no compact-resolvent spectral zeta and no ordinary Fredholm determinant from the frozen resolvent/group | `PROVED` obstruction |
| orbit Hasse--Weil determinant | exact in the separate primitive-orbit/cohomological ledger | inherited `PROVED` |
| equality of that determinant with a determinant of \(A_K\) | absent; must not be claimed | `NOT_TESTABLE` bridge, with naive standard determinant obstructed |
| physical quantization | not supplied by Koopman pullback | `NOT_TESTABLE` |

### Pure point versus continuous-spectrum set

Two true statements must be retained together:

1. the vectors \(e_{x,n}\) are a complete eigenbasis, hence every vector's
   spectral measure is atomic;
2. the closed operator spectrum is all of \(\mathbb R\), and each irrational
   real is a non-eigenvalue continuous-spectrum point obtained as an
   accumulation of rational eigenvalues.

Calling this “discrete spectrum” would be false: no point is an isolated
finite-multiplicity eigenvalue, and the resolvent is noncompact.

## 4. Proof certificate

### P1 — Every degree exists

For \(d\ge2\),

\[
\begin{aligned}
d\,a_d
&=\sum_{e\mid d}\mu_{\rm Mob}(e)2^{d/e}\\
&\ge2^d-\sum_{\substack{e\mid d\\e\ge2}}2^{d/e}\\
&\ge2^d-\sum_{j=1}^{\lfloor d/2\rfloor}2^j>0.
\end{aligned}
\]

The projective point at infinity gives the third degree-one point. Therefore a
closed point exists in every positive degree.

### P2 — Complete operator and self-adjointness

Periodic Fourier series diagonalize each \(A_x\). Each is self-adjoint on its
periodic \(H^1\) domain. The countable orthogonal-direct-sum theorem proves
self-adjointness on the stated square-summability domain. Equivalently, the
explicit strongly continuous unitary translations have this unique Stone
generator.

### P3 — Point spectrum and infinite multiplicity

The component union is

\[
\bigcup_{d\ge1}\frac{2\pi}{d\log2}\mathbb Z
=\frac{2\pi}{\log2}\mathbb Q.
\]

For \(q=a/b\) in lowest terms, degree \(kb\) and Fourier mode \(ka\) realize
\((2\pi/\log2)q\) for every \(k\ge1\). Choosing one closed point in each such
degree gives an infinite orthonormal eigenset. Conversely, an eigenvector must
have a nonzero component, so no other point eigenvalue occurs.

### P4 — Full and essential spectrum

The direct-sum spectrum is the closure of the component union, hence
\(\mathbb R\). Rational spectral points have infinite-multiplicity exact
eigenvectors. For irrational \(\lambda\), take distinct rational eigenvalues
\(\lambda_j\to\lambda\) on distinct components. Their eigenvectors converge
weakly to zero and satisfy
\(\|(A_K-\lambda)e_j\|\to0\). The singular Weyl criterion proves every real
point essential.

### P5 — Compactness, counting, and heat

For \(z\notin\mathbb R\), the resolvent sends each normalized zero mode to
\(-z^{-1}\) times itself. This infinite orthogonal image disproves compactness.
Every interval of positive width contains a rational eigenvalue of infinite
multiplicity, so its spectral projection has infinite rank. Heat fixes the
infinite zero eigenspace; even after kernel deletion it repeats one positive
heat eigenvalue infinitely on any chosen nonzero rational eigenspace.

### P6 — Determinant ledger separation

The standard Fredholm determinant requires a trace-class operator. The
candidate's resolvents and heat functions fail the necessary compactness/trace
tests. Deligne's equation (1.5.4) instead takes alternating determinants of
Frobenius on finite-dimensional etale cohomology. The two actions and spaces
are not the same object; no intertwiner or trace identity has been provided.

## 5. Operator ledger lock

```yaml
koopman_ledger:
  space: orthogonal sum of L^2 suspension circles
  action: flow pullback / periodic derivative
  eigenvalues: (2 pi / log(2)) Q with infinite multiplicities
  determinant_status: standard spectral determinant unavailable
orbit_ledger:
  objects: primitive suspension circles and their repetitions
  product: product_x (1 - exp(-s deg(x) log(2)))^(-1)
  result: Hasse-Weil zeta of P^1/F_2
  operator_status: no trace-class transfer operator identified on Koopman space
cohomology_ledger:
  space: finite-dimensional compactly supported etale cohomology
  action: Frobenius
  determinant: alternating Deligne determinant, equation (1.5.4)
  relation_to_koopman: common arithmetic source only; no operator equivalence
physical_quantization_ledger:
  required_extra_structure:
    - source-derived symplectic or appropriate phase-space structure
    - prequantum/polarization or another explicit quantization rule
    - physical normalization and observable map
  status: absent_from_frozen_candidate
same_object_certificate:
  paper3_fields_blocked_from_coordinatewise_merge:
    - T0_object_identity
    - T3_analytic_ledger
    - T5_coefficient_provenance
  bridge_morphism: absent
  same_operator_trace_identity: absent
```

The Hasse--Weil equality remains exact and valuable, but it is not a spectral
determinant statement about \(A_K\).

## 6. Exact Route-A A4 lock

```yaml
route_a_layer: A4
verdict: A4_UNITARY_OR_SCATTERING_CANDIDATE
evidence_status: PROVED
why_this_enum:
  - Koopman pullback is intrinsic to the frozen flow
  - the clock and normalization are unchanged
  - the Hilbert space and periodic generator domain are explicit
why_not_A4_NATURAL_QUANTIZATION:
  - no physical or geometric quantization map is supplied
  - no source-derived symplectic/prequantum/polarization data are frozen
why_not_A4_ROUTE_B_READY:
  - relevant primitive-orbit phases and weights are not a trace of A_K
  - no determinant bridge belongs to the same operator
  - B3_FAIL is proved
route_b_invocation_allowed_normally: false
limited_early_audit_authorized_by_project_lead: true
```

For the Riemann target, Paper 4's overall `ROUTE_A_REJECTED` remains in force.
This positive A4 unitary result does not repair A0/A2/A3.

## 7. Exact limited Route-B enumeration

This Phase 1 audit issues exactly three evaluator enums:

```text
B1_COMPLETE_OPERATOR_DEFINITION
B2_SELF_ADJOINT
B3_FAIL
```

B4 and B5 are outside the authorized scope and receive no verdict here. In
particular, no invented “not invoked” layer enum may be serialized. The scoped
audit record is:

```yaml
entry:
  normal_condition_met: false
  reason: Route A did not return ROUTE_A_SUCCESS_ROUTE_B_READY
  exception: project lead explicitly authorized a limited early B1-B3 audit
b1:
  verdict: B1_COMPLETE_OPERATOR_DEFINITION
  evidence_status: PROVED
  reason: >-
    Hilbert space, invariant measure, inner product, dense domain, periodic
    boundary conditions, action, closedness, same clock, and bookkeeping
    spectral map are explicit and use no zero list.
b2:
  verdict: B2_SELF_ADJOINT
  evidence_status: PROVED
  reason: >-
    The periodic component derivatives are self-adjoint; their canonical
    orthogonal sum is self-adjoint and is the unique Stone generator.
b3:
  verdict: B3_FAIL
  evidence_status: PROVED
  reason: >-
    The spectrum and essential spectrum are R; every point eigenvalue has
    infinite multiplicity; the resolvent is noncompact; every positive-width
    interval has infinite projection rank; heat is not trace class; no
    intrinsic locally finite spectral count or standard determinant exists.
audit_scope:
  included:
    - B1
    - B2
    - B3
  not_invoked:
    - B4
    - B5
gate_b:
  status: PASS_OPERATOR_DEFINITION_ONLY
gate_c:
  status: FAIL_SPECTRAL_TYPE
overall_verdict: ROUTE_B_REJECTED
hilbert_polya_claim_allowed: false
```

B1 and B2 are genuine positive theorems, but they do not authorize B4. The
spectral-host obligation is conjunctive, and Gate C fails. A future formal
five-layer serialization must use the Route-B schema and is left to the
subsequent bridge audit.

## 8. Robustness controls

| Attempted repair | Exact result | Lock consequence |
|---|---|---|
| arbitrary positive component weights | unitary equivalence via \(W_w\) | same candidate, same failure |
| choose a probability measure | special positive weights | same candidate, same failure |
| keep only one closed point per degree | every denominator still occurs along degrees \(kb\) | infinite multiplicity remains |
| delete zero modes | each nonzero rational frequency still has infinite multiplicity | compactness/heat/counting still fail |
| finite-degree cutoff | finitely many compact circles have compact resolvent | new artificial cutoff object |
| couple components | may change spectrum | new candidate needing a provenance and domain audit |
| add a potential | no longer the pure Koopman generator | new candidate |
| use etale Frobenius determinant | recovers native zeta | different operator ledger, not a B3 repair |
| use relative/renormalized determinant | may be definable after choices | new regularization data and candidate ID |

No control uses target zeros or fitted data.

## 9. Claim boundary

Allowed:

> The fixed Frobenius suspension possesses a canonical, same-clock Koopman
> unitary group with an explicit self-adjoint generator. Its point spectrum is
> \((2\pi/\log2)\mathbb Q\), every point eigenvalue has infinite multiplicity,
> and its full and essential spectra are \(\mathbb R\). Hence the canonical
> lift fails compact-resolvent, local-counting, heat-trace, and standard
> spectral-determinant requirements.

Not allowed:

- “The orbit Hasse--Weil zeta is the determinant of the Stone generator.”
- “A pure-point eigenbasis makes the spectrum discrete.”
- “Removing invariant functions repairs the trace.”
- “Self-adjoint Koopman transport is a physical quantization.”
- “B1 plus B2 is sufficient for a Hilbert--Pólya claim.”
- “A finite cutoff determinant belongs to the full arithmetic suspension.”

## 10. Paper 6 reuse interface

Paper 6 inherits the following exact obstruction certificate:

```yaml
paper6_reuse_id: FF-FROB-SUSP-P1-F2-KOOPMAN-P1/B3-OBSTRUCTION
operator: A_K = orthogonal_sum_x (-i d/du)_periodic
point_spectrum: (2 pi / log(2)) Q
point_multiplicity: countably_infinite_at_every_point_eigenvalue
spectrum: R
essential_spectrum: R
compact_resolvent: false
positive_width_local_counting: infinite
heat_trace_class: false
ordinary_fredholm_determinant: unavailable
orbit_zeta_is_AK_determinant: false
cohomological_frobenius_same_operator: false
b4_invocation_from_this_candidate: not_authorized
smallest_allowed_next_test: >-
  construct or identify a source-derived same-object trace bridge with an
  explicit morphism; do not transplant closed-point coefficients into A_K.
```

This interface is a stop condition for a formal prime trace of \(A_K\), not a
license to start B4 by analogy.
