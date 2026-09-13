---
name: route-b-evaluator
description: Evaluate whether a strong Route-A candidate can be promoted to a rigorous Hilbert-Pólya realization. Use when auditing the proposed Hilbert space, operator domain, boundary conditions, self-adjointness, spectral correspondence, zeta-regularized determinant identity, or proof gaps of a Riemann spectral construction.
---

# Skill: Route B Evaluator

**Name:** `route-b-evaluator`  
**Version:** `0.2.0`  
**Purpose:** Evaluate whether a strong Route-A candidate can be promoted to a rigorous Hilbert–Pólya realization in one mathematically compatible construction.

---

## 1. Scope

Route B is a proof route.

Its target is a genuine operator-theoretic realization, not a finite matrix fit, a real numerical spectrum, a PT-symmetric heuristic, or a formal Hamiltonian.

The central principle is:

> The prime side, periodic-orbit side, operator side, trace formula and determinant must belong to the same mathematical object.

No coordinatewise patching of unrelated constructions is allowed.

The ultimate target is an operator \(H\) satisfying

\[
\det_{\zeta}(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right),
\]

where \(H\) is self-adjoint on a rigorously defined Hilbert space and \(e^{q(E)}\) introduces no extra zeros.

---

## 2. Entry conditions

Route B should normally be invoked only if Route A reports:

```text
ROUTE_A_SUCCESS_ROUTE_B_READY
```

A limited early audit is allowed only to answer:

- whether a natural Hilbert space exists;
- whether a proposed quantization is coherent;
- whether a self-adjointness route is obviously impossible;
- whether the candidate belongs to a known exact trace-formula framework.

Route B must not be used to rescue a weak Route-A fit.

---

## 3. Inputs

Required:

```yaml
candidate_id:
route_a_evaluation:
classical_system:
arithmetic_origin:
quantization_map:
proposed_hilbert_space:
proposed_operator:
proposed_domain:
boundary_conditions:
clock:
normalization:
spectral_parameter_map:
code_commit:
artifact_paths:
```

Optional:

```yaml
trace_formula_hint:
weil_form_hint:
explicit_formula_hint:
determinant_hint:
```

Reject as `NOT_TESTABLE` if the Hilbert space, operator action, domain, arithmetic origin, clock, or normalization is absent.

---

# 4. Route-B layers

## B1 — Operator-definition layer

### Question

Is there a mathematically complete operator, not only a formal expression?

### Required checks

1. Hilbert space \(\mathcal H\) is explicit.
2. Inner product and measure are explicit.
3. Dense domain \(\mathcal D(H)\) is explicit.
4. Boundary conditions are explicit.
5. Operator action is explicit.
6. Closedness or closability is addressed.
7. The spectral parameter map
   \[
   E\longleftrightarrow s=\frac12+iE
   \]
   is explicit.
8. The operator is derived naturally from the Route-A candidate.
9. The operator does not use the Riemann-zero list in its definition.

### B1 verdicts

```text
B1_FAIL
B1_FORMAL_OPERATOR
B1_DENSELY_DEFINED
B1_CLOSED_OR_CLOSABLE
B1_COMPLETE_OPERATOR_DEFINITION
```

### B1 fail conditions

- finite matrix only;
- unspecified domain;
- boundary conditions chosen after seeing zeros;
- different clocks between classical and quantum objects;
- operator defined through the zero list itself.

---

## B2 — Self-adjointness layer

### Question

Is the operator genuinely self-adjoint?

### Acceptable proof routes

- essential self-adjointness;
- deficiency indices;
- Kato–Rellich;
- quadratic-form methods;
- boundary triplets/extensions;
- unitary equivalence to a self-adjoint operator;
- a bounded positive metric with a proved similarity theorem, when applicable.

### Required distinction

```text
symmetric ≠ self-adjoint
real finite spectrum ≠ self-adjoint
PT-symmetric ≠ automatically real spectrum
formal Hermiticity ≠ operator self-adjointness
```

### B2 verdicts

```text
B2_FAIL
B2_SYMMETRIC_ONLY
B2_SELF_ADJOINT_EXTENSION_EXISTS
B2_ESSENTIALLY_SELF_ADJOINT
B2_SELF_ADJOINT
```

### B2 fail conditions

- numerical eigenvalues are real but domain analysis is absent;
- PT symmetry is used without proving the unbroken regime and metric/domain conditions;
- self-adjoint extension is nonunique and no canonical choice is justified.

---

## B3 — Spectral-type layer

### Question

Does the operator have the spectral type required for the proposed Hilbert–Pólya realization?

### Required checks

1. Discrete spectrum or the exact required resonance formulation.
2. Compact resolvent, confining form, trace-class heat kernel, or another precise mechanism.
3. Multiplicity is controlled.
4. Spectral counting function is compatible with the Riemann–von Mangoldt law.
5. No uncontrolled essential spectrum contaminates the target.
6. The spectral determinant is well-defined.
7. The counting law is intrinsic, not imposed by parameter fitting.

### B3 verdicts

```text
B3_FAIL
B3_SPECTRAL_TYPE_OPEN
B3_DISCRETE_SPECTRUM_PARTIAL
B3_COMPACT_RESOLVENT
B3_TARGET_SPECTRAL_TYPE
```

### Important rule

Compact phase space is not mandatory. What matters is the operator's actual spectral type.

---

## B4 — Arithmetic trace and Weil-form layer

### Question

Is there a rigorous bridge from the operator spectrum to the exact prime-power arithmetic structure, and does the same operator naturally induce the relevant Hermitian/explicit-formula structure?

B4 has two sub-obligations.

### B4a — Exact prime-power trace

For a suitable test function \(f\), seek

\[
\operatorname{Tr}f(H)
=
\text{smooth term}
+
\sum_{p}\sum_{r\ge1}
A_{p,r}\widehat f(r\log p),
\]

with the required von Mangoldt / prime-power amplitudes, phases and multiplicities.

Required checks:

1. Equality is rigorous, or the error term is explicit and sufficient.
2. Primitive and repeated orbits are correctly distinguished.
3. The amplitude is derived, not fitted.
4. The smooth Weyl term is correct.
5. Distributional convergence is justified.
6. The same operator, clock and normalization are used throughout.
7. No incompatible classical and quantum ledgers are glued together.
8. \(\log p\) and von Mangoldt weights are outputs of the structure, not inserted by hand.

### B4b — Weil-form / explicit-formula compatibility

The 2026 two-thirds result gives a rigorous benchmark in which:

```text
prime powers
↔ Weil explicit formula
↔ finite Hermitian compression
↔ trace / second moment / inertia
↔ zero information
```

A strong HP candidate should therefore be tested for a natural analogue.

Questions:

1. Does the same operator or transfer structure define a Hermitian form \(W_H\)?
2. Can finite compressions \(G_H\) be defined without using target zeros?
3. Can \(\operatorname{tr}G_H\) and \(\operatorname{tr}(G_H^2)\) be read from the same prime-power ledger as B4a?
4. Is the inertia/signature structure intrinsic?
5. Is the relationship to the arithmetic Weil form an identity, a theorem-level correspondence, a heuristic analogy, or merely a modeling choice?
6. Are the arithmetic and operator sides using identical clocks and normalizations?

A particularly strong target is a factorization or representation such as

\[
W_\zeta(f,g)=\langle Af,Ag\rangle_{\mathcal H},
\]

or an equivalent positive/indefinite operator representation derived from the candidate itself.

This is not required in exactly this form, but any claimed Weil-form bridge must be mathematically explicit.

### B4 verdicts

```text
B4_FAIL
B4_SEMICLASSICAL_ANALOGY
B4_PARTIAL_TRACE_IDENTITY
B4_VON_MANGOLDT_WEIGHTED_TRACE
B4_WEIL_FORM_COMPATIBLE
B4_EXACT_TRACE_FORMULA
```

### B4 fail conditions

- “looks like Gutzwiller” without a theorem;
- only low-order orbit matching;
- amplitudes inserted manually;
- \(\log p\) roof lengths inserted manually;
- separate absolute estimates destroy signed cancellation;
- local rows promoted to a cyclic trace theorem;
- the Weil form is defined post-hoc from the Riemann zeros;
- prime-side and operator-side formulas come from different incompatible objects.

---

## B5 — Spectral-determinant/divisor layer

### Question

Is the operator determinant rigorously equal to the completed Riemann function up to a zero-free factor?

### Ultimate target

\[
\det_\zeta(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

### Required checks

1. The zeta-regularized determinant exists.
2. The normalization is fixed.
3. The entire prefactor is proved zero-free.
4. Zero multiplicities agree.
5. No extra eigenvalues/zeros exist.
6. No target zeros/eigenvalues are missing.
7. Equality holds globally, not only on a finite set.
8. Analytic continuation and growth order are controlled.

### B5 verdicts

```text
B5_FAIL
B5_FINITE_DIVISOR_MATCH
B5_LOCAL_DETERMINANT_IDENTITY
B5_GLOBAL_DIVISOR_EQUALITY
B5_COMPLETED_XI_IDENTITY
```

Only `B5_COMPLETED_XI_IDENTITY` with B1–B4 fully closed is a complete Hilbert–Pólya realization.

---

# 5. Adversarial control gate

Every Route-B claim must be subjected to a proves-too-much test.

Where mathematically applicable, run the same operator/trace-formula logic against control objects such as:

- Davenport–Heilbronn-type functions;
- Epstein zeta functions with off-line zeros;
- synthetic planted-zero models;
- randomized Euler products;
- operator models with the same coarse spectral statistics but no prime structure.

Required question:

> Would the same theorem, under the same hypotheses, incorrectly imply an RH-like statement for a control object?

If yes:

```text
STOP_SCOPED / PROVES_TOO_MUCH
```

The control test must be stated explicitly in every serious Route-B evaluation.

---

# 6. Gate mapping

Use the following gates:

```text
Gate A:
canonical intrinsic dynamical spectral determinant

Gate B:
time-oriented scattering or unitary completion

Gate C:
genuine self-adjoint generator and intrinsic T log T law

Gate D:
von Mangoldt-weighted prime-power trace plus arithmetic/Weil compatibility

Gate E:
equality with the completed-zeta divisor
```

Mapping:

```text
Route-A A0–A3 → Gate A
Route-A A4 / Route-B B1 → Gate B
Route-B B2–B3 → Gate C
Route-B B4 → Gate D
Route-B B5 → Gate E
```

All gates must be reported separately. Coordinatewise maxima from different constructions are not a valid certificate.

---

# 7. Overall Route-B decision

Use the tuple

```text
(B1, B2, B3, B4, B5)
```

and one overall status:

```text
ROUTE_B_REJECTED
ROUTE_B_NOT_TESTABLE
ROUTE_B_FORMAL_ONLY
ROUTE_B_OPERATOR_CANDIDATE
ROUTE_B_SELF_ADJOINT_CANDIDATE
ROUTE_B_TRACE_FORMULA_CANDIDATE
ROUTE_B_PARTIAL_REALIZATION
HILBERT_POLYA_REALIZATION
```

Interpretation:

```text
B1 only:
formal operator program

B1 + B2:
self-adjoint operator candidate

B1 + B2 + B3:
valid spectral host candidate

B1 + B2 + B3 + B4:
strong partial Hilbert–Pólya realization

B1 + B2 + B3 + B4 + B5:
complete Hilbert–Pólya realization
```

---

# 8. Mandatory adversarial questions

Every Route-B evaluation must answer:

1. Is the arithmetic origin explicit?
2. Is the domain fully specified?
3. Is the operator merely symmetric?
4. Are boundary conditions post-hoc fitted?
5. Is the self-adjoint extension canonical?
6. Is the spectrum truly discrete?
7. Is the determinant mathematically defined?
8. Does the trace formula derive the weights?
9. Are \(\log p\) and von Mangoldt factors emergent rather than inserted?
10. Are extra eigenvalues excluded?
11. Is the equality global?
12. Does the proof depend on RH itself?
13. Are different determinant data types being combined?
14. Is an abstract completion being called physical?
15. Is a finite matrix being called an operator realization?
16. Is GUE evidence being used as proof?
17. Are moving-order/all-order claims actually proved?
18. Is the Weil-form bridge intrinsic or post-hoc?
19. Do arithmetic and operator sides use the same clock and normalization?
20. Does the method prove too much on a known false-RH control object?

---

# 9. Knowledge sources

Read:

```text
latest Route-A evaluation
docs/prior_work/README.md
docs/prior_work/papers/
docs/obstruction_registry.md
docs/operator_obligations.md
docs/candidate_registry.md
```

Interpretation inherited from prior work:

```text
Papers 1–5:
dynamical-system clues, obstructions, non-autonomous lessons,
finite spectral warnings, and the Hénon-to-conservative-geometry bridge

Paper 6:
prime-side arithmetic ↔ Weil finite compression ↔ zero information
```

The prior-work chain supplies search clues and rigorous benchmarks. It does not by itself establish any Route-B layer.

---

# 10. Output schema

```yaml
skill: route-b-evaluator
skill_version: 0.2.0
candidate_id:
source_commit:
evaluation_date:

route_a_entry:
  route_a_verdict:
  entry_authorized:
  limitations:

source_lock:
  arithmetic_origin:
  clock:
  normalization:
  operator:
  domain:
  boundary_conditions:

b1:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  obligations:
  artifacts:

b2:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  obligations:
  artifacts:

b3:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  obligations:
  artifacts:

b4:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  prime_power_trace:
  weil_form_compatibility:
  obligations:
  artifacts:

b5:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  obligations:
  artifacts:

adversarial_controls:
  controls_used:
  proves_too_much_risk:
  verdict:

gates:
  gate_a:
  gate_b:
  gate_c:
  gate_d:
  gate_e:

overall_verdict:
claim_boundary:
blocking_conditions:
next_smallest_theorem:
hilbert_polya_claim_allowed: false
```

`hilbert_polya_claim_allowed` is `true` only if:

```text
B1_COMPLETE_OPERATOR_DEFINITION
B2_SELF_ADJOINT
B3_TARGET_SPECTRAL_TYPE
B4_EXACT_TRACE_FORMULA
B5_COMPLETED_XI_IDENTITY
```

are all rigorously established in one compatible construction.

---

# 11. Accumulation protocol

Save every evaluation under:

```text
evaluations/route_b/<candidate_id>/<timestamp>.yaml
```

Update:

```text
docs/operator_obligations.md
docs/obstruction_registry.md
docs/candidate_registry.md
```

Extract reusable results as:

```text
operator-domain pattern
self-adjointness lemma
spectral-type theorem
trace-formula lemma
Weil-form lemma
determinant identity
proved obstruction
canonical-boundary-condition criterion
```

Do not overwrite prior evaluations.

---

# 12. Invocation prompt

```text
Apply the Route-B Evaluator skill to candidate <candidate_id>.

Read the latest frozen Route-A evaluation first.
Do not use Route B to rescue a weak Route-A fit.

Evaluate:
B1 complete operator definition,
B2 self-adjointness,
B3 target spectral type,
B4 exact von-Mangoldt-weighted prime-power trace plus Weil-form compatibility,
B5 completed-xi determinant/divisor equality.

Keep all gates and data types separate.
Require the arithmetic, periodic-orbit, operator, trace and determinant ledgers
to belong to one compatible construction.

Do not infer self-adjointness from real numerical eigenvalues.
Do not treat PT symmetry, GUE statistics, a finite matrix, or an abstract
completion as a Hilbert–Pólya realization.
Do not insert log-prime lengths or von-Mangoldt weights by hand.
Run proves-too-much controls against known false-RH analogues when applicable.

Return the exact YAML output schema and identify the next smallest theorem
needed for progress.
```
