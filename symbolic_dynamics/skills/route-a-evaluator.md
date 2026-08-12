---
name: route-a-evaluator
description: Evaluate whether a proposed classical dynamical system, transfer operator, symbolic suspension, quantum graph, or Fredholm-determinant construction is a credible Route-A candidate for a Riemann dynamical determinant. Use when assessing primitive-orbit structure, trace formulas, determinant matching, normalization, robustness, falsification tests, or Route-B readiness for a proposed Riemann-dynamics construction.
---

# Skill: Route A Evaluator

**Name:** `route-a-evaluator`  
**Version:** `0.2.0`  
**Purpose:** Evaluate whether a proposed dynamical system is a credible Route-A candidate for a Riemann dynamical determinant, with arithmetic relevance treated as a mandatory entry gate.

---

## 1. Scope

Route A is a discovery and validation route. It does **not** prove the Riemann Hypothesis and does **not** establish a Hilbert–Pólya operator.

The target is a natural dynamical object whose arithmetic origin, periodic-orbit structure, transfer operator, or Fredholm determinant satisfies, exactly or asymptotically,

\[
D_{\mathrm{dyn}}(s)\approx e^{g(s)}\xi(s),
\]

where \(e^{g(s)}\) introduces no extra zeros.

The central principle is:

> A candidate is not interesting merely because its spectrum looks Riemann-like. It must have a natural arithmetic origin, directly or indirectly.

A successful Route A result may still be a major result even if Route B later fails.

---

## 2. Inputs

Required:

```yaml
candidate_id:
candidate_definition:
family:
phase_space:
dynamics:
parameters:
parameter_provenance:
arithmetic_origin:
clock:
normalization:
determinant_convention:
orbit_cutoff:
precision:
training_data:
forbidden_data:
code_commit:
artifact_paths:
```

Optional:

```yaml
symbolic_partition:
transfer_operator:
roof_function:
potential_function:
quantization_hint:
weil_form_hint:
explicit_formula_hint:
prior_work_links:
legacy_rh_links:
```

Reject the evaluation as `NOT_TESTABLE` if the mathematical object, arithmetic origin, clock, normalization, determinant convention, or data split is missing.

---

## 3. Evidence hierarchy

Use only these labels:

```text
PROVED
CONDITIONAL_THEOREM
NUMERICALLY_CERTIFIED
NUMERICAL_OBSERVATION
HEURISTIC
MODELING_CHOICE
FITTED_PARAMETER
OPEN
REFUTED
NOT_TESTABLE
STOP_SCOPED
```

Never promote a numerical observation to a theorem.

---

# 4. Route-A layers

## A0 — Arithmetic relevance gate

### Question

Why should this dynamical system have anything to do with primes or prime powers?

The answer must come from the candidate itself, not from post-hoc fitting to the Riemann spectrum.

### Required checks

1. State the arithmetic source explicitly.
2. Distinguish direct arithmetic structure from indirect arithmetic structure.
3. Explain how primitive objects could correspond to rational primes.
4. Explain how repetitions could correspond to prime powers.
5. Identify whether \(\log p\), \(\Lambda(n)\), or equivalent arithmetic weights emerge naturally.
6. Verify that prime tables and Riemann-zero tables are not embedded in the candidate definition.
7. Verify that free parameters are not chosen by matching target zeros.
8. Compare against non-prime controls.

### Preferred target structure

At minimum, seek an intrinsic relation of the form

\[
p\longleftrightarrow \gamma_p,
\qquad
T_{\gamma_p}\approx \log p.
\]

The stronger target is

\[
p^r\longleftrightarrow \gamma_p^r,
\qquad
A_{\gamma_p,r}
\approx
\frac{\log p}{p^{r/2}}
\]

with correct repetition, multiplicity, sign and phase structure.

### Mandatory arithmetic controls

At least three of:

- shuffled primes;
- matched-density random integers;
- composites only;
- pseudoprime or sieve-matched controls;
- randomized arithmetic labels;
- neighboring dynamical parameters;
- simpler parent system.

### A0 verdicts

```text
A0_FAIL
A0_WEAK_ARITHMETIC_RELATION
A0_NUMERICAL_ARITHMETIC_SIGNAL
A0_STRUCTURAL_ARITHMETIC_RELATION
A0_ANALYTIC_ARITHMETIC_ORIGIN
```

### A0 fail conditions

- prime table is used directly in the dynamics;
- roof lengths are assigned as \(\log p\) by hand;
- von Mangoldt weights are inserted manually;
- adjacency rules are designed from the target prime list;
- Riemann zeros are used to choose parameters;
- only GUE statistics or generic chaos are offered as the arithmetic link;
- the same signal appears for matched random/composite controls.

If A0 fails, the candidate may remain mathematically interesting but is not a primary HP-Dynamics candidate.

---

## A1 — Primitive-orbit layer

### Question

Does the candidate possess a natural, reproducible primitive-periodic-orbit structure carrying the arithmetic information identified in A0?

### Required checks

1. Primitive orbit definition is intrinsic to the dynamics.
2. Orbit enumeration is reproducible.
3. Repeated orbits are distinguished from primitive orbits.
4. Orbit orientation, phase and multiplicity are recorded.
5. Monodromy/stability multipliers are computed.
6. Completeness or missed-orbit risk is reported.
7. Arithmetic labels are derived from the orbit structure, not attached afterward.

### Target structure

At minimum, seek a non-accidental correspondence

\[
p\longleftrightarrow \gamma_p,
\qquad
T_{\gamma_p}\approx \log p.
\]

The stronger target is

\[
A_{\gamma_p,r}
\approx
\frac{\log p}{p^{r/2}}
\]

with correct repetition, multiplicity and phase structure.

### Mandatory controls

- shuffled periods;
- random weights;
- random phases;
- same-density random lengths;
- neighboring candidate parameters;
- simpler parent candidate.

### A1 verdicts

```text
A1_FAIL
A1_WEAK
A1_PASS_NUMERICAL
A1_PASS_CERTIFIED
A1_PASS_ANALYTIC
```

### A1 fail conditions

- direct prime lookup;
- period matching only after high-dimensional fitting;
- UPO enumeration incomplete without an uncertainty report;
- primitive and repeated cycles mixed;
- signed/complex weights replaced by absolute values;
- result disappears under small parameter or cutoff changes.

---

## A2 — Dynamical-Zeta layer

### Question

Do the primitive orbits define a stable weighted dynamical Zeta function or Fredholm determinant whose zeros/divisor structure matches the target beyond the fitted region?

### Required object

One explicit convention, for example

\[
Z_{\mathrm{dyn}}(s)
=
\prod_{\gamma}
\left(1-w_\gamma e^{-sT_\gamma}\right)^{-1},
\]

or

\[
D_{\mathrm{dyn}}(s)=\det(I-\mathcal L_s).
\]

The report must state whether the target concerns:

```text
Z
1/Z
Z'/Z
det(I-L_s)
another explicitly defined determinant
```

### Required checks

1. Training, validation and sealed test regions are separated.
2. Parameters are frozen before validation.
3. Root count is checked with the argument principle or an equivalent method.
4. Missing and extra zeros are reported.
5. Results are compared across orbit cutoffs.
6. Precision dependence is reported.
7. Two independent implementations are preferred.
8. Signed/complex cancellations are preserved.

### Mandatory outputs

```yaml
zero_error_train:
zero_error_validation:
zero_error_test:
extra_zero_count:
missing_zero_count:
root_count_discrepancy:
cutoff_drift:
precision_drift:
control_margin:
```

### A2 verdicts

```text
A2_FAIL
A2_TRAIN_ONLY
A2_FROZEN_VALIDATION_PASS
A2_ADVERSARIAL_PASS
A2_CERTIFIED_PREFIX
A2_ANALYTIC_DETERMINANT
```

### A2 fail conditions

- test-set refitting;
- changing scale, offset or unfolding after validation;
- reporting only the best seed;
- ignoring extra zeros;
- combining incompatible determinant decompositions;
- using different clocks or normalizations for head, orbit and tail pieces.

---

## A3 — Analytic and arithmetic-operator structure

### Question

Does the candidate reproduce the global analytic structure, and can the same arithmetic content be read through a Weil/explicit-formula-type finite operator compression?

### A3a — Global analytic structure

Required checks:

1. Conjugation symmetry:
   \[
   D(\bar s)=\overline{D(s)}.
   \]
2. Functional-equation behavior:
   \[
   D(s)\sim D(1-s)
   \]
   with all normalization factors stated.
3. Correct treatment of:
   - Gamma factor;
   - trivial zeros;
   - pole removal;
   - entire prefactors.
4. Riemann–von Mangoldt counting law.
5. Analytic continuation or a controlled annular/domain theorem.
6. Truncation error or moving-order control.
7. No zero-producing hidden prefactor.

### A3b — Weil-compression benchmark

The 2026 two-thirds result provides a rigorous benchmark in which the same finite compression of Weil's Hermitian form is read from two sides:

```text
prime powers
↔ explicit formula
↔ finite Hermitian compression
↔ trace / second moment / inertia
↔ critical-line zero information
```

For a candidate dynamical system, attempt to define a natural finite-dimensional Hermitian compression \(G_{\mathrm{dyn}}\), or an equivalent object.

Check, when mathematically meaningful,

\[
\operatorname{tr}G_{\mathrm{dyn}},
\qquad
\operatorname{tr}(G_{\mathrm{dyn}}^2),
\qquad
n_+(G_{\mathrm{dyn}}),
\qquad
n_-(G_{\mathrm{dyn}}).
\]

The strongest evidence would be an identity in which the same compression is readable from both:

```text
dynamical / orbit side
and
arithmetic / prime-power side
```

This benchmark is optional when no natural Weil-type form exists, but any artificial definition chosen only to imitate the Riemann explicit formula must be labeled `MODELING_CHOICE`.

### Strong optional evidence

- nuclear or trace-class transfer operator;
- Fredholm determinant theorem;
- certified annular \(H^\infty\) or \(H^2\) control;
- exact trace identity;
- all-order coefficient theorem;
- explicit-formula compatibility;
- finite-compression trace identity;
- inertia/signature theorem.

### A3 verdicts

```text
A3_FAIL
A3_NUMERICAL_GLOBAL_MATCH
A3_PARTIAL_ANALYTIC_STRUCTURE
A3_CONTROLLED_CONTINUATION
A3_WEIL_COMPRESSION_COMPATIBLE
A3_EXACT_DIVISOR_CANDIDATE
```

### A3 fail conditions

- finite zero fit presented as analytic continuation;
- separate absolute majorants destroy required cancellation;
- fixed-order data promoted to moving-order asymptotics;
- an abstract algebraic completion presented as a physical dynamical determinant;
- Weil-form structure is inserted by hand rather than derived;
- arithmetic and dynamical compressions use different clocks or incompatible normalizations.

---

## A4 — Natural-liftability layer

### Question

Is there a natural, non-post-hoc path from the classical candidate to a unitary, scattering, or Hamiltonian object?

### Required checks

1. Quantization is defined from the candidate, not invented after zero fitting.
2. Candidate has a coherent phase space and symplectic/contact/scattering structure, where applicable.
3. Time-reversal or antiunitary symmetry is explicitly tested.
4. The proposed quantum object preserves the same clock and normalization.
5. The proposed lift retains the relevant orbit phases and weights.
6. A plausible Hilbert space and operator domain can be named.

### A4 verdicts

```text
A4_FAIL
A4_FORMAL_HINT
A4_NATURAL_QUANTIZATION
A4_UNITARY_OR_SCATTERING_CANDIDATE
A4_ROUTE_B_READY
```

A candidate may be a strong Route-A success even if A4 fails.

---

# 5. Adversarial control gate

Every serious Route-A candidate must be tested against objects for which analogous RH statements are false or irrelevant.

Examples include, where applicable:

- Davenport–Heilbronn-type functions;
- Epstein zeta functions with off-line zeros;
- synthetic planted-zero systems;
- randomized Euler products;
- matched symbolic systems without arithmetic structure.

The purpose is to detect a **proves-too-much** mechanism.

Required question:

> Would the same argument, with the same hypotheses, falsely certify an RH-like conclusion for a control object?

If yes:

```text
STOP_SCOPED / PROVES_TOO_MUCH
```

A control failure must be reported even if the candidate has excellent numerical agreement.

---

# 6. Overall Route-A decision

Use the tuple

```text
(A0, A1, A2, A3, A4)
```

and one overall status:

```text
ROUTE_A_REJECTED
ROUTE_A_EXPLORATORY
ROUTE_A_ARITHMETIC_CANDIDATE
ROUTE_A_NUMERICAL_CANDIDATE
ROUTE_A_STRONG_CANDIDATE
ROUTE_A_ANALYTIC_CANDIDATE
ROUTE_A_SUCCESS_ROUTE_B_NOT_READY
ROUTE_A_SUCCESS_ROUTE_B_READY
```

Recommended interpretation:

```text
A0 weak or failed:
not a primary HP-Dynamics candidate

A0 + A1:
arithmetic orbit candidate

A0 + A1 + A2:
credible dynamical-Zeta candidate

A0 + A1 + A2 + partial A3:
strong Route-A candidate

A0 + A1 + A2 + strong A3:
Route-A success

A0 + A1 + A2 + strong A3 + A4:
send to Route-B Evaluator
```

---

# 7. Knowledge sources

Read in this order:

```text
docs/prior_work/README.md
docs/prior_work/papers/
<stage_root>/docs/obstruction_registry.md
<stage_root>/docs/candidate_registry.md
```

Freeze `<stage_root>` before the evaluation begins. Shared prior-work sources are
resolved from the `symbolic_dynamics/` umbrella root; candidate registries,
evaluations, and experiment artifacts are resolved from the frozen stage root.

Interpretation inherited from prior work:

```text
Paper 1: arithmetic-symbolic clue and low-dimensional prime-dynamics seed
Paper 2: one-dimensional topological obstruction
Paper 3: sequential / non-autonomous dynamics
Paper 4: numerical spectral baseline and overfitting warning
Paper 5: area-preserving Hénon as a geometric bridge toward conservative dynamics
Paper 6: prime-side arithmetic ↔ Weil finite compression ↔ zero information
```

The six papers provide clues, examples and benchmarks. They do not establish a candidate automatically.

---

# 8. Output schema

```yaml
skill: route-a-evaluator
skill_version: 0.2.0
candidate_id:
source_commit:
evaluation_date:
artifact_path_base:  # stage root, relative to symbolic_dynamics/

source_lock:
  object:
  arithmetic_origin:
  clock:
  normalization:
  determinant_convention:
  cutoff:
  precision:
  allowed_data:
  forbidden_data:

a0:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  arithmetic_controls:
  artifacts:

a1:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  metrics:
  artifacts:

a2:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  metrics:
  artifacts:

a3:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  analytic_structure:
  weil_compression:
  artifacts:

a4:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  metrics:
  artifacts:

adversarial_controls:
  controls_used:
  proves_too_much_risk:
  verdict:

overall_verdict:
claim_boundary:
blocking_conditions:
next_smallest_test:
round2_clues:
route_b_invocation_allowed: false
```

Set `route_b_invocation_allowed: true` only after A4 reaches `A4_ROUTE_B_READY` or the project lead explicitly authorizes a limited Route-B audit.

---

# 9. Accumulation protocol

Every evaluation must be saved under:

```text
<stage_root>/evaluations/route_a/<candidate_id>/<timestamp>.yaml
```

Update:

```text
<stage_root>/docs/candidate_registry.md
<stage_root>/docs/obstruction_registry.md
```

Every relative path in an evaluation's `artifact_paths` or `artifacts` fields is
resolved against `artifact_path_base`. Do not silently mix artifacts from two
stages or candidates.

Do not overwrite prior evaluations. New evidence creates a new version.

A clue that leaves the current dynamical-system family should be recorded as `round2 clue` rather than pursued inside the same first-round session.

Reusable knowledge should be extracted as one of:

```text
positive structural prior
negative structural prior
numerical benchmark
proved obstruction
open theorem obligation
reusable implementation pattern
round2 clue
```

---

# 10. Invocation prompt

```text
Apply the Route-A Evaluator skill to candidate <candidate_id>.

Use the repository as the source of truth.
Freeze the object, arithmetic origin, clock, normalization, determinant convention,
cutoff, precision and data split before evaluation.

Evaluate:
A0 arithmetic relevance,
A1 primitive-orbit structure,
A2 dynamical Zeta/Fredholm determinant,
A3 global analytic structure plus Weil-compression compatibility when natural,
A4 natural liftability.

Preserve signed and complex cancellations.
Do not use test zeros for fitting.
Do not embed prime tables, zero tables, log-prime roofs, or von-Mangoldt weights by hand.
Run proves-too-much controls.
Do not combine incompatible determinant decompositions.

Stay inside the current dynamical-system family.
If a promising idea requires a different family, record it as ROUND2_CLUE and stop.

Return the exact YAML output schema and recommend only the next smallest verifiable step.
```
