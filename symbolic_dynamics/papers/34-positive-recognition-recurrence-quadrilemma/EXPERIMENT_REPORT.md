# Exact experiment report — Paper 34 / SD-C36

## Outcome

The authority experiment validates the finite exact consequences and sharp
scope of the positive recognition-to-recurrence quadrilemma. The originally
preregistered strict connector witness is false as written; its 18,272
counterexamples are retained in full. The minimally repaired same-SCC
statement passes all 844,544 pair checks. Terminal recognition is determinant
neutral until recurrent blocks are pruned, finite-visible logarithmic codes
instantiate the Kraft-clock obstruction, and first return changes the free
marker from `z^ell` to `z`.

The result closes the ordinary positive scalar recognizer-compiler branch. It
does not close signed, matrix-valued, nonlocal, infinite-alphabet, anisotropic,
or genuinely different symbolic systems.

## Frozen source and execution order

`SOURCE_LOCK.md`, `PREREGISTRATION.md`, and
`experiments/EXPERIMENT_PLAN.md` were frozen before authority output
generation. The canonical runner then executed three physically distinct,
initially absent result directories:

1. fresh run A: neutral source, post-source evaluator, tests, analysis;
2. fresh run B: the same complete pipeline without reuse;
3. cache-free cold-start run C after another cache purge.

Each run produced the same 19 declared scientific artifacts. The A/B fresh
aggregate and the cold-start aggregate are
`ae0aa6d1767bb207d0096df149224995bfb40aba674367a2f300668bfdd88c02`.
Only run A was published, and only after all hashes agreed.

## Counterexample-first theorem repair

The strict C2 proxy required one pair of attachment points and two shortest
connector paths whose interiors simultaneously avoid both cycles. It fails:

| Evidence class | Three vertices | Four vertices | 5--8 vertex controls | Total |
|---|---:|---:|---:|---:|
| strict-proxy counterexamples | 24 | 17,952 | 296 | 18,272 |

This is a failure of the preregistered witness normal form, not of the core
same-SCC obstruction. The repaired theorem chooses arbitrary `u` and `v` on
the two cycles and arbitrary SCC paths `P:u->v`, `Q:v->u`; paths may traverse
cycle vertices. The closed word `alpha P beta Q` has a mixed primitive root.

The evaluator records:

```text
preregistered_C2_status = FAIL_AS_WRITTEN
repaired_C2_status      = PASS
positive-class repaired failures = 0
```

The full counterexample ledger is
`results/connector_construction_counterexamples.csv`; no row was deleted or
reclassified after the outcome was known.

## Complete enumeration versus finite controls

These evidence classes are not combined into an exhaustive claim.

| Evidence | Graphs | Shared-state pairs | Repaired connector pairs | Mixed-root certificates | True failures |
|---|---:|---:|---:|---:|---:|
| complete masks on 1--4 vertices | 66,066 | 613,996 | 161,475 | 775,471 | 0 |
| 64 SHA-seeded controls on 5--8 vertices | 64 | 66,212 | 2,861 | 69,073 | 0 |
| combined finite pair audit | — | 680,208 | 164,336 | 844,544 | 0 |

The first row is complete for the frozen finite class. The second row is a
deterministic larger-graph control. Neither row numerically proves the
countable theorem; the proof package supplies the arbitrary-graph argument.

## Terminal recognition and determinant ownership

The neutral exact graph has 160 states: 126 recurrent states in 17 disjoint
cycles and 34 acyclic decision states. The source computes
`det(I-zA)` by Newton identities; the evaluator independently reconstructs the
recurrent SCC product. The two exact coefficient lists agree.

Eight post-source inventories were tested: trial-division atoms, perfect
squares, Fibonacci numbers, a modular support, SHA-selected support,
matched-cardinality SHA support, all values, and the empty support. Acyclic
terminal tags leave the unclassified determinant unchanged in all eight
cases. Each of the six proper nonempty supports changes the determinant only
after recurrent blocks are deleted. Thus the selected product belongs to a
label-dependent pruned operator, not to the original recognizer graph.

## Kraft-clock and marker firewalls

- All 12 q-ary/cutoff configurations passed exact prefix decoding,
  prefix-freeness, Kraft, roof-share, and powered-clock checks.
- All 6,141 item rows satisfy roof-share sum one and `n^2<q^ell` exactly.
- These rows are finite regression witnesses for the analytic weak-null
  noncompactness proof, not cutoff extrapolation.
- All 17 raw factors `1-w z^ell` differ formally from the induced factors
  `1-w z`.
- All 17 agree after setting `z=1`; this specialization earns no same-marker
  ownership.

## Sharp boundaries

The signed three-state adjacency is nilpotent and has determinant one while
the absolute-weight graph has recurrent traces. Orthogonal matrix branches
have zero mixed products and surviving pure products. One-way connectors,
transient branches, and cyclic rotations of one orbit provide the remaining
minimum-hypothesis controls. Positivity, cyclic distinctness, and mutual
recurrence are therefore essential.

## Source/evaluator separation

The candidate source contains neutral graph masks, paths, rational weights,
q-ary codes, roofs, and determinants only. Its source AST firewall has zero
forbidden identifiers. Arithmetic and arbitrary-inventory labels occur only
in `code/independent_evaluator.py` after the source artifacts are frozen.

The two sides use different decisive algorithms:

| Task | Source | Independent evaluator |
|---|---|---|
| SCC | Tarjan | transitive-closure equivalence |
| cycles | DFS | vertex permutations |
| primitive root | divisor scan | coordinate-period test |
| connector | queue search | permuted path interiors |
| determinant | Newton identities | recurrent-SCC product |

All five aggregate census rows agree field for field. The exact test report is
76/76 PASS.

The scientific A/B/C pipeline uses only the Python standard library. PyYAML
6.0.2 is separately locked as a seal/audit dependency because the Route-A card
is YAML; it is not a dependency of any of the 19 scientific artifacts.

## Route decision and provenance

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

No target-zero or root comparison was performed; every such Route-A metric is
recorded as a scoped `not_applicable;...` string. Stage-1 provenance keeps all
three commit fields equal to `PENDING_FIRST_ARTIFACT_COMMIT`. A future
metadata-only Stage 2 may replace them simultaneously with one immutable
artifact commit and regenerate the manifest, without changing scientific
payloads.

The strict v0.2 A2 card also records `cutoff_drift`, `precision_drift`, and
`control_margin` as scoped `not_applicable;...` strings. The research lock
binds the current bytes of six frozen research documents; the final auditor
recomputes all six pointers, and the fresh, cold-start, and metadata-seal
certificates bind the research-lock hash.

## Integrity contract

The canonical seal requires the exact 29-file result set, 41 SHA-ledger
entries, source/evaluator separation, A/B/C stability, metadata-seal stability,
UTF-8/LF, exactly one LF at EOF, no trailing whitespace or forbidden control
characters, no Python/test caches, idempotent freeze/audit output, and exact
SHA verification. The machine-readable statuses and final ledger hash are in
`results/integrity_audit.json`, `results/idempotence_certificate.json`, and
`results/aggregate_sha256.txt`.
