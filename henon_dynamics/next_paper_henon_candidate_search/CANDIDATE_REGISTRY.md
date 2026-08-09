# Candidate registry

Date: 2026-08-05

This is the append-only generation-round registry.  C02, C03, and C05 have
completed source-locked pilots.  None reached BF3, so their Route-A labels are
conservative screening ceilings rather than formal evaluation YAMLs.

The later C02C/C02D continuation is now complete. C02C retained an effective
complex pinning specialization, while C02D closed the proposed same-clock
finite-memory operator lane **NO_GO**. Its separate frozen object has a formal
Route-A rejection record under
`../henon_pinning_trace_obstruction/evaluations/route_a/`.

## Compact registry

| ID | Candidate family | Role | Status | First decisive test |
|---|---|---|---|---|
| HCS-C00 | Certified Ruelle pressure/dimension | baseline, control, fallback | BASELINE | external theorem-delta gate |
| HCS-C01 | Ordered two-letter Hénon skew product/cocycle | discovery | IDEA | common hyperbolicity and chronology control |
| HCS-C22 | Paper-5-coordinate two-letter Hénon skew product with intrinsic local instability sectors | promoted child of C01 / theorem plus obstruction | OBSTRUCTION | closed orbitwise scalar cancellation; graded child authorized |
| HCS-C22G | Projectivized two-letter Hénon skew product with exterior-degree Ruelle--Lefschetz complex | child of C22 / changed operator form | SOURCE_LOCKED | common nuclear branch factorization and exact low-period supertrace |
| HCS-C02 | Derivative-projective Schottky/holomorphic strictification | high-risk discovery | ANALYTIC_CANDIDATE | finite-window endpoint lemma plus crossed/pinning-map composition |
| HCS-C02B | Signed-root complex sequence-polydisc bridge | child of C02 | ANALYTIC_CANDIDATE | proved self-map; no finite analytic branch/operator yet |
| HCS-C03 | Finite-field local zeta and global Euler product | discovery/negative control | OBSTRUCTION | naive global product rejected; two-axis Frobenius/iterate mechanism required for revival |
| HCS-C04 | Derivative-representation zeta ladder | discovery | IDEA | nontrivial factorization beyond scalar shifts |
| HCS-C05 | Action--instability--Maslov two-variable determinant | discovery/negative control | OBSTRUCTION | additive-constant gauge and proved one-symbol Maslov collapse |
| HCS-C06 | Global pruning-front/tangency-window zeta | discovery | IDEA | complete symbolic chamber or smallest obstruction |
| HCS-C07 | Parabolic induced zeta at \(a=3\) | discovery | IDEA | robust return tail and inducing scheme |
| HCS-C08 | Contact/Reeb realization of the instability suspension | discovery | IDEA | exact gluing without changing periodic sums |
| HCS-C09 | Open quantum Hénon dilation/scattering | discovery | IDEA | cutoff-independent scattering determinant |
| HCS-C10 | Complex compactification/Lefschetz obstruction | obstruction candidate | IDEA | theorem delta beyond standard algebraic stability |
| HCS-C11 | Cylinder inverse-limit metric quantum graph | negative control | IDEA | canonical resolvent limit independent of boundary choices |
| HCS-C12 | Periodic-orbit number fields/Galois-twisted zeta | high-risk discovery | IDEA | canonical Galois character and repetition law |
| HCS-C12A | Fixed-\(n\) Frobenius zeta of periodic schemes | child of C12 / obstruction | OBSTRUCTION | closed: universal finite-permutation determinant |
| HCS-C12B | \(a=6,n=5\) reversor-line \(S_6\) sextic | child of C12 / novelty control | REJECTED | closed: Endler--Gallas 2006 collision |
| HCS-C12C | Parameter-varying exact-period dihedral quotient curve | child of C12 / scoped obstruction | OBSTRUCTION | stopped: prior low-period marker collision, invariant-sector loss, and no frozen cross-period determinant |
| HCS-C13 | Fibonacci spectral section hit equals trace-map return | system-level pivot / negative control | OBSTRUCTION | exact witnesses and 48 gcd gates refute clocks m=k and m=q_k |
| HCS-C13B | Casdagli marked-band boundary language versus closed zeta | child of C13 / structural obstruction | OBSTRUCTION | source-faithful ten-state identity and decorated unweighted six-state quotient at \(\lambda\ge16\) |
| HCS-C13P | Uniform polynomial-weight Fibonacci transfer family | child of C13 / theorem obstruction | OBSTRUCTION | proved energy-degree/clock no-go for arbitrary finite \(N_k\) with uniform local degree |
| HCS-C13G | Fibonacci zero-radius analytic-germ model | child of C13 / theorem obstruction | OBSTRUCTION | exact witness series have radius zero, excluding literal analytic coefficient/log-trace matching |
| HCS-C13R | Infinite-dimensional energy-dependent Fibonacci boundary Fredholm model | child of C13 / possible reframe | REJECTED | Route-A input NOT_TESTABLE until operator tuple is defined; switch system |
| HCS-C02D | Trace-compatible finite-memory pinning operator | child of C02C / obstruction | OBSTRUCTION | exact one-step kernel has no frozen memory truncation; scalar sign repair fails on repetition |

## Required record schema

```yaml
candidate_id:
revision:
generation_round:
status: IDEA | SOURCE_LOCKED | CHEAP_TEST | PILOT | ROUTE_A_CANDIDATE |
        ANALYTIC_CANDIDATE | ROUTE_B_AUDIT | REJECTED | BASELINE |
        OBSTRUCTION
role: discovery | baseline | control | fallback
parent_candidates:
variant_group:

source_lock:
  candidate_definition:
  family:
  phase_space:
  dynamics:
  parameters:
  parameter_provenance:
  chronology:
  symbolic_partition:
  primitive_orbit_definition:
  clock:
  potential_and_weight:
  repetition_rule:
  normalization:
  determinant_convention:
  transfer_operator:
  quantization_hint:
  orbit_cutoff:
  precision:
  code_commit:
  artifact_paths:

mechanism_chain:
  dynamics_to_orbits:
  orbits_to_weights:
  weights_to_determinant:
  determinant_to_global_divisor:
  natural_operator_lift:
  weakest_arrow:
  conditional_end_to_end_story:
  predicted_anomaly:

equivalence_fingerprint:
  dynamics_conjugacy_class:
  symbolic_presentation_class:
  canonical_cycle_order:
  short_cycle_period_vector_hash:
  roof_livsic_signature:
  weight_character:
  determinant_divisor_class:
  quantization_class:
  duplicate_of:

data_firewall:
  generation_data:
  calibration_data:
  frozen_validation_data:
  sealed_target_region:
  forbidden_data:
  freeze_timestamp:

cheap_falsifiers:
  - test_id:
    mathematical_prediction:
    kill_threshold:
    maximum_budget:
    result:
    artifact:

controls:
  simpler_parent:
  shuffled_periods:
  random_weights:
  random_phases:
  same_density_lengths:
  neighboring_parameters:
  recoding_or_gauge_controls:

engineering_quality:
  internal_zeta_stability:
  root_count_method:
  cutoff_drift:
  precision_drift:

route_a:
  a1_verdict:
  a2_verdict:
  a3_verdict:
  a4_verdict:
  overall_verdict:
  evaluation_artifacts:

route_b_entry_authorized: false

budget:
  credits_allocated:
  credits_spent:
  next_gate_cap:
  cpu_hours:
  researcher_days:

decision:
  current_gate:
  pass_or_fail:
  strongest_positive:
  strongest_obstruction:
  next_smallest_test:
```

`engineering_quality.internal_zeta_stability` is deliberately distinct from
`route_a.a2_verdict`.  Stable finite sections can be excellent numerical work
while formal A2 still fails because no target divisor, analytic determinant,
or sealed validation has been established.

## Round-one append-only decision record

| Candidate | Evidence state | Screening tuple | Overall | Route B |
|---|---|---|---|---|
| C02/C02B | proved complex sequence-domain and real-base/complex-fibre contraction | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_EXPLORATORY` | closed |
| C03 | exact local factors plus matched reversible controls | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` | closed |
| C05 | proved gauge obstruction and local-symbol Maslov collapse; finite-section ledger | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` for intrinsic fixed-\(z\) phase | closed |

The detailed evidence is in `refine-logs/EXPERIMENT_RESULTS.md`.  No formal
Route-A YAML was created because all three failed to reach BF3 under the
frozen search protocol.  C02/C02B is additionally `NOT_TESTABLE` at formal
Route-A input validation because no clock, normalization, determinant, or
transfer operator is frozen; its tuple is only a triage ceiling.

## C02D append-only decision record

| Candidate | Evidence state | Formal tuple | Overall | Route B |
|---|---|---|---|---|
| C02D | exact mixed-domain certificate plus two exact scoped obstructions | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` | closed |

The smallest obstruction witness is a primitive cycle together with its
double repetition: a multiplicative scalar correction cannot be \(-1\) on
both. The independent certificate also proves that the standard exact BPS
kernel has no length-\(N\) one-step coefficient for C02C windows to truncate.

## C12A/C12B append-only decision record

| Candidate | Evidence state | Formal tuple | Overall | Route B |
|---|---|---|---|---|
| C12A | finite-flat rank theorem, exact low-period certificate, general finite-scheme Frobenius collapse, reversible information-loss control | (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL) | ROUTE_A_REJECTED for the registered fixed-\(n\) local-rationality mechanism | not authorized |
| C12B | exact \(a=6,n=5\) \(Z\)-sextic, discriminant scaling, modular \(S_6\) certificate | n/a: exact prior-work collision | REJECTED as novelty claim | not authorized |

C12A does not refute the nontrivial zeros of the resulting classical global
Dedekind/Artin factors, nor all joint-action or positive-dimensional
mechanisms.  It proves that fixed-\(n\) local rationality and finite recurrence
in Frobenius degree are universal and therefore nondiagnostic.  C12B collides
directly with Endler--Gallas (2006), with later companion-polynomial work by
Brison--Gallas (2018).

C12C is closed as a scoped obstruction, not a universal quotient no-go.  The
low-period orbit-marker method collides with Endler--Gallas/Gallas prior work;
ordinary constant-coefficient cohomology of the coarse dihedral quotient sees
only the trivial isotypic sector; and the period-six squarefree marker
components have genus zero.  Primitive period remains an external grading,
so the result must not be paraphrased as saying that every autonomous scalar
dynamical zeta loses its clock.  Without a frozen weighted cross-period
determinant, formal Route-A input is `NOT_TESTABLE` and the management decision
is `STOP_SCOPED`.

## C13/C13B/C13P/C13G/C13R append-only decision record

| Candidate | Evidence state | Formal tuple | Overall | Route B |
|---|---|---|---|---|
| C13-AM | source-faithful ten-state zeta at lambda=16 plus the exact failure of the frozen coefficient identity `tr(A10^k)=d_k(E)` | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` for the literal unweighted coefficient identification | not authorized |
| C13B | source-faithful ten-state band language, boundary resolvent, closed determinant, and decorated unweighted quotient | structural record, not a positive Route-A candidate | `PROVED STRUCTURAL IDENTITY` in the source large-coupling regime | not authorized |
| C13P | all-level dimension-independent polynomial degree theorem plus exact degree certificate | obstruction record, not a positive Route-A candidate | `PROVED OBSTRUCTION` | not authorized |
| C13G | exact product-growth witnesses plus Cauchy--Hadamard analytic-germ theorem | obstruction record, not a positive Route-A candidate | `PROVED OBSTRUCTION` | not authorized |
| C13R | schematic infinite-dimensional boundary Fredholm proposal | input gate `NOT_TESTABLE` | `NOT_TESTABLE`; no layer verdict until fully defined | not authorized |

C13 proves only that the frozen one-coordinate section incidences are not
three-coordinate returns at \(m=k\) or \(m=q_k\); it does not infer a general
Fredholm no-go from those gcds.  These witnesses, their gcd audit, and C13G
are at \(\lambda=1\).  The values \(E=0,-1\) are
finite-periodic-approximant section energies, not asserted spectral points of
the infinite Fibonacci Hamiltonian.  C13B is separate: Casdagli's
source-faithful ten-state band language applies for \(V_{\rm C}\ge8\),
equivalently \(\lambda\ge16\), and its unweighted six-state quotient requires
a decorated initial lift.

C13P supplies the stronger reusable polynomial theorem: arbitrary finite
dimensions \(N_k\) with uniformly bounded local polynomial degree still have
\(E\)-degree \(O(k)\) in short-clock traces, boundary coefficients, and
order-\(k\) determinant coefficients, while the chronological Fibonacci
discriminant has degree \(F_{k+2}\).  Merely growing state dimension is not an
escape.  C13G supplies a complementary dimension-free theorem: at the exact
section witnesses, \(|d_k(E_*)|^{1/k}\to\infty\), so the coefficient and
logarithmic-trace series have radius zero.  No scalar germ analytic at
\(z=0\) can realize either literal matching; this includes fixed
bounded-resolvent matrix elements and standard analytic Fredholm
determinants.

Physical time, nonlinear/composition dynamics, level-dependent
exponential-degree weights, growing-order full characteristic determinants,
\(k\)-dependent or nonanalytic/zero-radius constructions, singularity at a
witness, and indirect energy-divisor maps remain outside the combined
theorems.  Infinite dimension alone does not evade C13G if the claimed scalar
coefficient or logarithmic determinant is analytic at zero.  The unrestricted
C13R proposal lacks an operator, function space, weights, variables, clock,
normalization, and exact coefficient/divisor identity, so no local numerical
tuning is authorized.

## HCS-C14 append-only decision record

| Candidate | Evidence state | Formal tuple | Overall | Route B |
|---|---|---|---|---|
| HCS-C14 | exact dyadic-solenoid fixed indices, cyclic parity theorem, congruence tower, analytic-type chronology witness, and global continuation theorem | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` for Hilbert--Pólya; `PROVED_STRUCTURAL_RESULT` for arithmetic dynamics | not authorized |

HCS-C14 changes category from smooth Hénon dynamics to the autonomous skew
product on

\[
\Sigma_2\times\widehat{\mathbb Z[1/2]^2}
\]

generated by

\[
A=\begin{pmatrix}3&1\\1&3\end{pmatrix},\qquad
B=\begin{pmatrix}3&2\\2&4\end{pmatrix}.
\]

For every chronological word,

\[
\#\operatorname{Fix}(\alpha_{M_w})
=\operatorname{oddpart}\!\left(8^{|w|}-\operatorname{tr}M_w+1\right).
\]

The active dyadic words are exactly the cyclic no-`aa` language.  The
equal-Parikh primitive base words `aabbb` and `ababb` have rational and
natural-boundary return zetas, respectively, proving that chronology can
change analytic type.  Globally, \((1-16z)Z_2(z)\) is holomorphic and nowhere
zero for \(|z|<(8\varphi)^{-1}\); the first convergence circle is therefore
not a natural boundary.  The secondary circle remains open.  The natural
Koopman lift contains the Bernoulli bilateral shift and hence a continuous
spectral component, so it is not a discrete Hilbert--Pólya operator.

The formal corrected evaluation is
`../s_integer_solenoid_chronology_zeta/evaluations/route_a/hcs_c14/20260806T130222Z.yaml`.
The compiled paper and exact audit are under
`../s_integer_solenoid_chronology_zeta/`.

## HCS-C15 append-only decision record

| Candidate | Evidence state | Formal tuple | Overall | Route B |
|---|---|---|---|---|
| HCS-C15 | exact nonabelian chronology witness, fixed-roof zero-density theorem, and conductor-resolved Heisenberg branch-return certificate | (A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT) | ROUTE_A_REJECTED; PROVED_SCOPED_OBSTRUCTION | not authorized |

HCS-C15 tests the regular-minus-trivial Artin--Ihara proposal without
averaging chronological voltage products. Canonical aggregation coarsens a
primitive holonomy to its element order; fixed finite-memory representation
resolution has only \(O(T)\) divisor growth; and the registered amenable
Heisenberg tower has exact-conductor nonabelian blocks whose top eigenvalues
tend to four. The last theorem rules out the frozen uniform
Ramanujan/new-sector-gap rescue, not every renormalized tower determinant.

The formal evaluation and complete paper package are under
../nonabelian_voltage_zeta_obstruction/.

## HCS-C22 append-only decision record

| Candidate | Evidence state | Formal tuple | Overall | Route B |
|---|---|---|---|---|
| HCS-C22 | T1 exact common survivor; T2 complete 29/49-branch rational interval separations; T3 exact unit-numerator global residue collapse | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_EXPLORATORY`; one staged T4--T5 kill round authorized | not authorized |
| HCS-C22 | T4 exact instability Euler product in a nonzero domain; common base/projective/log domains; orbitwise scalar denominator cancellation refuted by double repetition | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_EXPLORATORY`; frozen termwise scalar lane closed; aggregate scalar nonexistence not claimed | not authorized |
| HCS-C22G | inherited certified projective/log geometry; four-degree nuclear exterior complex and supertrace still open | not yet formally evaluated | `SOURCE_LOCKED`; one large nuclear/supertrace kill round authorized | not authorized |

HCS-C22 is the theorem-stage promotion of HCS-C01, not a separately invented
skew product.  It freezes

\[
F(\omega,z)=(\sigma\omega,H_{a_{\omega_0}}z),
\qquad
(a_0,a_1)=(59/10,61/10),
\]

in the physical Paper-5 coordinate convention.  Every admissible binary
joint parameter--state itinerary has exactly one orbit in a common uniformly
fibre-hyperbolic local survivor.  Complete conditional coefficients
\(Q_w(1)\) distinguish the certified same-bigram period-seven pair and
same-trigram period-eight pair after all 29 and 49 state branches are summed.
This is not an infinite-memory theorem.

The all-complex control is sharply negative: the cyclic scheme has length
\(2^n\), the unit-numerator signed scheme-residue determinant is one, and the
bare global scheme zeta is \((1-4z)^{-1}\).  Pointwise flat equality requires
all-repetition nondegeneracy.  Local absolute/instability data remain outside
that residue cancellation.

T4 now passes with exact multiplier bounds and a nonzero normal-convergence
domain.  The common two-letter base-pinning and projective/logarithm domains
also pass.  Orbitwise scalar denominator cancellation fails before spectrum
computation: its fixed-point correction cannot be multiplied consistently
on a primitive saddle and its double repetition.  This closes HCS-C22 under
its frozen termwise geometric convention, while leaving unmarked aggregate
scalar compensation unexcluded.

HCS-C22G is the authorized changed form.  It uses the unique unstable
projective lift and four exterior degrees so that a Lefschetz supertrace can
cancel the denominator.  Projective lifting and exterior cancellation are
prior art; promotion requires a common quantitative nuclear factorization
and exact chronology-preserving supertrace, not a finite section.

The source package is
[`../henon_time_ordered_ruelle_cocycle/`](../henon_time_ordered_ruelle_cocycle/),
and the formal evaluation is
[`20260809T050207Z.yaml`](../henon_time_ordered_ruelle_cocycle/evaluations/route_a/hcs_c22/20260809T050207Z.yaml).
