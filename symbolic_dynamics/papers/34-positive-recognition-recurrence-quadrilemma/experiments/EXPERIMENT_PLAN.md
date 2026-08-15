# Exact experiment plan — SD-C36

**Freeze status:** frozen after `SOURCE_LOCK.md` and `PREREGISTRATION.md`, and
before canonical authority result generation.

## Frozen question

Test the finite exact consequences and sharp boundaries of the positive
recognition-to-recurrence quadrilemma. The finite experiment validates
implementations and theorem hypotheses; the infinite recurrent-core,
noncompactness, pruning, and marker statements have independent proofs.

## Claim-to-certificate matrix

| ID | Frozen audit | Exact success condition | Primary artifact |
|---|---|---|---|
| E1 | shared recurrent states | every cyclically distinct simple-cycle pair sharing a state has an additional positive primitive-root certificate | `graph_census.csv` |
| E2 | mutual SCC connectors | retain every strict external-connector failure; arbitrary SCC paths repair every pair | `connector_construction_counterexamples.csv` |
| E3 | terminal recognition and pruning | acyclic tails preserve the recurrent determinant; every proper nonempty support-dependent pruning changes it | `neutral_recognizer.json`, `inventory_controls.csv` |
| E4 | finite code and logarithmic clock | exact q-ary prefix, Kraft, roof-share, and powered-clock checks all pass | `kraft_clock_summary.csv`, `code_clock_ledger.csv` |
| E5 | first-return marker | raw `z^ell` and induced `z` factors differ formally and agree only after `z=1` | `marker_ledger.csv` |
| E6 | sharp scope controls | one-way/transient/rotation controls and signed/matrix cancellation boundaries are explicit | `boundary_controls.json`, `counterexamples.json` |
| E7 | reproducibility | source/evaluator separation, three fresh builds including a canonical double-run and cold start, exact result inventory, metadata stability, full integrity, and SHA gates pass | reproducibility metadata and `SHA256SUMS.txt` |

## Frozen protocol

- Exhaustive loop-allowed simple directed graph masks on 1, 2, 3, and 4
  vertices.
- Sixty-four deterministic SHA-seeded strongly connected graph controls on
  5--8 vertices; these are finite controls, not complete enumeration.
- Strictly positive rational scalar primary edge weights.
- q-ary gamma payloads for q=2,3,4 and cutoffs 31,127,511,2047.
- Neutral recurrent values 2--18 with exact orbit weight `1/n^2`.
- Post-source inventories: trial-division atoms, squares, Fibonacci, modular,
  SHA-selected, matched-cardinality SHA, all, and empty.
- Exact integer, `Fraction`, polynomial, CSV, JSON, YAML, and SHA-256 gates.
- No GPU, network, external data, target zeros, coefficient fitting, runtime
  timestamps, stochastic sampling, Route B, or another terminal decider.

## Run order

1. Static AST and small-graph sanity.
2. Fresh run A: source, evaluator, tests, analysis.
3. Fresh run B: identical full pipeline in a distinct empty directory.
4. Cache-free cold-start run C in a third empty directory.
5. Publish A only after A=B=C byte identity.
6. Write the report, Route-A card, registries, and tracker without changing the
   19 frozen scientific payloads.
7. Certify metadata-seal stability, exact result inventory, hygiene,
   idempotence, and SHA-256.

## Acceptance gates

1. `C2` remains `FAIL_AS_WRITTEN` with all 18,272 strict-proxy failures.
2. Repaired C2 is `PASS` with 844,544/844,544 mixed-root pair certificates.
3. All 76 scientific tests pass.
4. All three fresh builds have the same 19 artifact hashes.
5. Route tuple is exactly
   `(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
6. Overall verdict is `ROUTE_A_REJECTED`; Route B is false.
7. All Route-A target-zero/root metrics begin with `not_applicable;`.
8. The three provenance fields carry the identical
   `PENDING_FIRST_ARTIFACT_COMMIT` token with a two-stage note.
9. Exact result set, UTF-8/LF, exact-one-LF EOF, trailing whitespace, control
   bytes, caches, schemas, metadata stability, and SHA gates pass.

## Scope firewall

Passing this plan supports only the frozen positive scalar, finite-visible,
natural vertex-adjacency class. Signed, matrix, supertrace, nonlocal-weight,
anisotropic-space, hidden-countable-alphabet, and induced-return programs
remain outside the no-cancellation conclusion and require new source locks.
