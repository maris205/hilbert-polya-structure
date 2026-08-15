# Authority experiment preregistration — Paper 36 / SD-C38

Freeze date: 2026-08-15 UTC.

Freeze order: this document and `EXPERIMENT_PLAN.md` exist before any
authority code or result payload. The root `SOURCE_LOCK.md` and
`PREREGISTRATION.md` remain the mathematical source of truth.

## 1. Decision target

Audit the exact finite consequences of the frozen Cayley-chain mechanism for

```text
M_r=<u,v | vu=u^r v>+,  r=2,3,4,5,
```

with composite baseline `r=4`, balanced control `r=1`, the same four oriented
letters, the unit graph-step marker, source-derived finite semidirect cells,
and the scalar `(1,2,1)` chain lift.

The experiment is a theorem-regression and implementation certificate. It
does not numerically prove contractibility, trace-class ownership, marker
non-descent, or the all-orders supertrace identity.

## 2. Prototype bridge

The `/tmp` prototype is research evidence only. Authority results are not
canonical until independently regenerated after this freeze.

| Frozen prototype artifact | SHA-256 |
|---|---|
| `source_core.py` | `041b8a1ee487eddafb1a4e935a015eaedf44aff1c32c6d26443c5a05e6cf94bd` |
| `independent_evaluator.py` | `d2cbd2bf5174b90a96135670b8022c94a4de2e9ba9404860ff49725ed41e28ce` |
| `run_exact.py` | `ee0a345bde7e3f57e42d4da41ab2297771a6527177e30abaf4993d3cd7ca2fc5` |
| `scientific_results.json` | `499b1a5b0647e9a9999dbfdfc881a8edc0877875102d91607c10e041f69f5221` |

The bridge target is semantic: `33/33` prototype assertions, first excess
lengths `5,6,7,8`, excess counts `10,12,14,32`, marker failure for
`r=2,3,4,5`, marker descent for `r=1`, six finite boundary controls, affine
residual dimensions `2,1,1,1,1,1`, complete residual dimension zero, and
zero scalar supertraces through length 12.

## 3. Physical source/evaluator firewall

The authority source side and evaluator side are separate Python processes.

- `source_core.py` is the byte-preserved neutral prototype construction.
- `source_generator.py` imports only `source_core.py` and writes raw exact
  presentation data without route verdicts or target labels.
- `independent_evaluator.py` is the prototype evaluator helper normalized only
  by removing its extra blank terminal line to satisfy authority exact-EOF.
- `evaluate_results.py` imports only `independent_evaluator.py`, never imports
  source code, and independently reconstructs affine multiplication, word
  counts, free reductions, finite boundaries, exact ranks, markers, and
  control decisions.

Candidate-source identifiers and imports are audited by Python AST. Prime,
factorization, accepted-support, target-zero, network, fitted-coefficient, and
Route-B oracles are forbidden.

## 4. Frozen runs and exact checks

1. Execute a complete fresh run A in an initially absent temporary result
   directory.
2. Execute the same complete run B in another initially absent directory.
3. Require every declared scientific payload and stage stdout to be
   byte-identical between A and B.
4. Purge Python/test caches, execute cold run C in a third initially absent
   directory, and require byte identity with A and B.
5. Publish run A only after all comparisons pass.
6. Add deterministic run certificates, research/dependency locks, Route-A
   metadata, exact inventory, SHA ledger, idempotence, and integrity audit.

The scientific checks include all ten root preregistration tests, independent
reconstruction of every decisive value, primitive/cyclic-nonbacktracking
relation-word checks, free-marker germ checks, exponent mutation, and a
matched arbitrary two-generator/one-relator scalar-lift control.

## 5. Failure retention

No failed row, mismatched hash, unexpected cache, source/evaluator import,
boundary-square error, prototype mismatch, or Route-schema failure may be
deleted or relabelled after execution. Any such event makes the authority run
noncanonical and must remain reported.

## 6. Frozen Route-A decision

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

All target-zero and root-comparison metrics are scoped
`not_applicable;...` strings. The three provenance fields are paired as
`PENDING_FIRST_ARTIFACT_COMMIT`; a future metadata-only stage may replace all
three with the same immutable artifact commit.

## 7. Hygiene and inventory

Canonical text is UTF-8 with LF line endings, exactly one terminal LF, no
trailing whitespace, no forbidden control bytes, and no Python/test caches.
The result inventory and SHA ledger are exact, sorted, path-unique, and
independently verified. Self-referential integrity files are explicitly
excluded from the ledger and bound later by the paper manifest.
