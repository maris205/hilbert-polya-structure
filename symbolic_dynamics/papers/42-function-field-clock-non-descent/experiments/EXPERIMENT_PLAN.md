# Paper 42 exact authority-integration experiment blueprint

Status: `BLUEPRINT_ONLY_NO_RESULTS_NO_AUTHORITY_WRITE`.

Candidate: proposed `SD-C44`.

Historical parent: `SD-C01`.

Working title: **Finite-Field Clocks Do Not Become Rational Primes: Exact
Factor Non-Descent for the Full Shift**.

This blueprint specifies a future exact, CPU-only authority integration. It
does not create code, results, evaluations, experiment reports, manifests,
commits, or authority bytes. It supplies no future count, hash, commit, or
pass value. Every future value must be generated from one declared static
seal and verified from canonical bytes.

## 1. Frozen inputs and chronology

The following read-only inputs were verified before writing this blueprint.

| Input | Exact SHA-256 | Role |
|---|---|---|
| Frozen package `SHA256SUMS.txt` | `f8f3ada901a3e26735819db05e3bcd01a26e571a8f9bd6cc4af8e1a2e705a433` | Self-excluding package seal; 16 declared package files |
| Frozen `RESEARCH_LOCK.json` | `fc4d3613165bebdd812789f0407329de983e1ec81020ef1024a665563293ffc2` | Fifteen-file immutable research mapping |
| Frozen `SOURCE_LOCK.md` | `2c4e85ebf6c0eff9211f30317ec0663f6f691838dfa4b38f4b811c8a2b87adc9` | Object, marker, clock, owner, and portability contract |
| Frozen `ROUTE_EXPECTATION.yaml` | `79eafee424590e0e1b65ffa7dc48d2a066a4822513ff1520f6bcf35593c6f71c` | Preactive strict Route expectation, not an integrated Route record |
| Independent DA report | `e46ecdab5aec15a3aa3dd5b80277e62f32677cd5162d803100a565b812bb265d` | `DA_ACCEPT_PREAUTHORITY` against the repaired package |
| Independent DA sidecar file | `1f691de1d3fd87c096fe95e65bd42b30b0664ac7bc24e8a5f37dfbcfb2c34585` | External binding for the DA report |
| Latest writer `WRITER_SHA256SUMS.txt` | `d930e78b2ce4ccb2bf84d88708f60c3b21227e8764d0c33fda66ad55d561e471` | Eighteen-file result-free writer seal after portability, reference-numbering, and diagnostic-chronology repair |

The chronology is not prospective science:

- all six historical card outcomes, the retrospective selector, the exact
  witnesses, and the mathematical conclusions were known before the frozen
  Paper-42 package was written;
- the independent DA found and repaired a preauthority Route-base defect
  before accepting the final package;
- the writer seal was created after the mathematics and DA were known, then
  repaired after intake audit to remove scratch-host tokens, to number labeled
  displays correctly, and to align the plan with completed diagnostic QA;
  these repairs changed no theorem, and the seal contains no canonical
  implementation result;
- a future static implementation seal may be frozen before its one declared
  canonical rerun, but this grants no preregistration, blind,
  outcome-independent, novelty, discovery, priority, ranking, or authorization
  credit; and
- if any smoke-test or failed-output bytes are seen during implementation,
  the final chronology must disclose them before the replacement static seal.

P39 supplies existence/governance provenance only. P40 and P41 supply
collision and chronology boundaries only. None ranks, selects, or authorizes
Paper 42.

## 2. Claims to be replayed

### Primary claim P1 — exact typed non-descent

For each frozen `q` in `{2,3,5}`, the valid full-shift primitive ledger cannot
be retyped as the rational-prime Euler ledger while simultaneously retaining
the total source factor set, exact clock `n log q`, original source-symbol
marker `z^n`, target multiplicity one, ordinary repetitions, and source
operator ownership.

Minimum convincing evidence:

1. a source-convention replay deriving fixed-point counts, primitive necklace
   counts, the primitive product, and `D_q(s,z)=1-zq^(1-s)`;
2. the length-two primitive witness `[01]`, whose exact-clock image is the
   composite `q^2`;
3. the length-one `q:1` source-to-target multiplicity collision after marker
   and weight equality force `n=1,p=q`; and
4. the first marked trace-log coefficient mismatch
   `q^(1-s) != P(s)` on the common domain.

### Supporting claim P2 — the source ledger remains positive and ownership is
typed

The full shift retains its intrinsic primitive/repetition ledger and ordinary
determinant. The degree-count match with finite-field prime polynomials is a
positive control. The rational-prime diagonal determinant is also a valid
positive control, but it is a separately owned object. Every declared repair
loses at least one locked field.

Minimum convincing evidence:

1. independent bounded agreement between primitive necklaces and monic
   irreducible-polynomial counts;
2. source cyclicity and word-power controls with zero source failure;
3. a field-by-field derivation of the six declared repair classifications;
4. exact type and owner ledgers with no cross-type credit; and
5. strict Route-A re-evaluation that keeps source A1/A2 positive.

### Anti-claims that the integration must reject

- The full-shift/function-field ledger failed.
- One failed rational-prime projection lowers A1 or A2.
- A separately supplied rational-prime diagonal inventory is source-owned.
- The theorem covers partial maps, re-marked first returns, induced systems,
  countable/infinite-memory models, or every function-field/number-field map.
- The declared six-repair matrix is exhaustive over all possible repairs.
- The selector or implementation is prospective, novelty-bearing, or
  authorized by P39--P41.
- A finite census proves the universal formulas.
- A target zero, prime table, fit, seed search, or Route-B calculation is
  part of the evidence.

If a later verified source formally publishes the same typed closure, apply
`STOP_DUPLICATE`, stop the standalone publication route, and assign no
novelty credit.

## 3. Exact bounded control grid

The finite computation is a theorem-replay and mutation-control grid, not the
source of the universal proof.

| Coordinate | Frozen control value | Purpose |
|---|---|---|
| Field sizes | `q in {2,3,5}` | Exact historical `SD-C01` fields |
| Word lengths | `1 <= n <= 6` | Exhaustive primitive-necklace control |
| Fixed-point periods | `1 <= r <= 3` | Literal fixed-word control matching the DA replay |
| Irreducible-polynomial degrees | `1 <= d <= 4` | Independent bounded function-field positive control |
| Decisive primitive word | `01` | Length-two clock/support witness |
| Decisive multiplicity layer | `n=1` | Marker/weight/multiplicity witness |
| Marker algebra | formal monomials in free `z` | Prevent premature `z=1` specialization |
| Analytic comparison | `Re(s)>1`, locally/formally in `z` | Common target/source coefficient domain |

No floating point, randomness, stochastic seed, training data, prime table,
or Riemann-zero data is permitted. All finite values are integers, exact
rationals, finite tuples, symbolic monomials, or normalized formula strings.

## 4. Raw packet contract

The producer emits one canonical JSON packet and no scientific verdict. Its
exact top-level keys should be:

```text
candidate_id
claim_boundary
control_grid
integration_chronology
marker_contract
operator_contract
portable_source_input
positive_control_input
raw_repair_rows
raw_selection_cards
schema
source_object_input
target_object_input
terminal_contract
type_ledger
witness_input
```

Required schema identifier:
`paper42-exact-source-packet-v1`.

The packet contains raw values only:

- alphabet sizes, maximum control lengths, the literal word `01`, and the
  rotation/reversal/power conventions;
- source and target marker definitions, clocks, factor monomials, and owners;
- the six repair rows as declared field transformations, without their
  classifications;
- the six historical card byte hashes and the raw fields used by the selector,
  without a preset survivor;
- all 29 typed source IDs, expected source hashes, and package-relative
  vendored locations;
- exact chronology booleans and status tokens; and
- the frozen terminal/claim vocabulary, but no pass flag or computed Route
  tuple.

Forbidden packet fields include primitive counts, witness results,
compositeness flags, repair verdicts, derived survivor sets, evaluator checks,
Route verdicts, expected output counts, and producer-authored `all_pass`
booleans.

Canonical JSON is ASCII, keys sorted, two-space indented, and terminated by
one linefeed. Every serialized path is package-relative POSIX text. No
absolute path, temporary directory, timestamp, hostname, environment value,
or source-tree discovery result may enter the packet.

## 5. Two physically independent scientific algorithms

The two evaluators run as separate isolated processes. Neither imports the
packet producer, the other evaluator, the Route renderer, the Route auditor,
or any project-local helper. Sharing the standard-library JSON format and the
same raw packet is allowed; sharing arithmetic, rotation, divisor, polynomial,
source-resolver, or pass-predicate code is forbidden.

### Algorithm M — enumeration-primary main evaluator

Suggested path: `code/evaluator/evaluate_packet.py`.

1. Parse the packet with exact JSON type checks and reject duplicate or extra
   semantic fields before computation.
2. For each `q,n`, enumerate tuples in `{0,...,q-1}^n`.
3. Determine least period by comparing the tuple to explicit repetitions of
   every proper divisor-length prefix.
4. Retain aperiodic tuples and choose the lexicographically least cyclic
   rotation as representative. Do not quotient reversal.
5. Enumerate fixed words directly for periods one through three and compute
   primitive counts from the representative inventory.
6. Independently enumerate monic polynomials through degree four. Test
   reducibility by exact polynomial division over `F_q` against every monic
   candidate divisor of degree at most half the polynomial degree.
7. Build the one-by-one weighted adjacency symbolically and derive its
   characteristic determinant and trace-log coefficients.
8. Prove the witness `01` primitive from its enumerated least period; derive
   the factorization certificate `q^2=q*q` with both factors greater than one.
9. Derive the length-one collision from the actual canonical representatives,
   not from an emitted count.
10. Compare the first marked coefficients as exact Dirichlet coefficient
    maps: the source has coefficient `q` at support integer `q`, while the
    target prime-zeta coefficient at rational prime `q` is one.
11. Evaluate every repair by applying its declared transformation to a typed
    `(object, clock, marker, support, multiplicity, repetition, owner)` record.
12. Parse the six historical YAML card snapshots with a duplicate-rejecting
    YAML loader and derive the selector survivor from its literal clauses.
13. Emit a normalized science projection and a separate main check ledger.

### Algorithm R — recurrence/formula-first independent evaluator

Suggested path: `code/evaluator/independent_evaluator.py`.

1. Implement a separate strict JSON reader and all predicates locally. Do not
   import Algorithm M or project helper modules.
2. Compute primitive counts recursively from
   `q^n = sum_(d|n) d N_q(d)` using a separately implemented divisor walk;
   do not enumerate necklaces or call a Möbius helper from Algorithm M.
3. Prove `01` primitive directly: a two-letter proper power has two equal
   symbols, whereas `0 != 1`.
4. Derive fixed-point counts as cardinalities of functions from a cyclic
   period set to `F_q`, not from the main word list.
5. Verify irreducible-polynomial counts through degree four with a distinct
   Frobenius/Rabin-style exact test using polynomial gcd and modular powering;
   do not use Algorithm M's trial-division routine.
6. Derive the source determinant from the formal identity
   `exp(sum_(r>=1)(z q^(1-s))^r/r)=1/(1-z q^(1-s))`, independently of a matrix
   determinant helper.
7. Derive the multiplicity obstruction from the recurrence value `N_q(1)`.
8. Verify first-coefficient nonidentity by the frozen large-real-`s` limit
   split: after multiplication by `2^s`, source limits are classified by
   `q=2` versus `q>2`, while the target limit is one with an exact dominating
   tail bound. Do not consume Algorithm M's coefficient map.
9. Reconstruct repair classifications from a separately implemented
   obligation-set difference.
10. Parse the six historical card snapshots with a constrained line/state
    parser for the required scalar fields, independently verify their raw
    hashes, and derive the survivor. Do not import the YAML renderer/parser
    used by Algorithm M.
11. Emit the same normalized science projection and a distinct independent
    check ledger.

### Required agreement and independence gates

- The canonical bytes of `main.science` and `independent.science` must be
  identical. Python object equality is insufficient.
- Wrapper-specific `implementation` and `checks` fields remain outside the
  science projection.
- A static import-graph audit must show no evaluator-to-evaluator,
  evaluator-to-producer, or independent-evaluator-to-Route-renderer import.
- A hostile `PYTHONPATH`, hostile `sitecustomize`, project-local shadow
  modules, a non-project working directory, and bytecode-disabled isolated
  invocation must not alter canonical bytes.
- Synthetic `false` versus `0`, `1` versus `1.0`, reordered mapping, tuple
  versus list, and missing/extra field controls must be rejected by canonical
  byte/type comparison.
- Any algorithm disagreement exits nonzero and materializes no accepted
  Route or report.

## 6. Canonical scientific projection

Both algorithms independently produce exactly these top-level science keys:

```text
candidate_id
claim_scope
control_grid
determinant_certificate
function_field_positive_control
integration_chronology
marker_ledger
necklace_census
operator_ledger
repair_classification
route
schema
selection
source_resolver
terminal_codes
theorems
type_ledger
universal_no_go_claimed
witness_ledger
```

Required schema identifier:
`paper42-exact-science-projection-v1`.

The projection must record, without overclaiming:

- exact bounded control rows for the declared grid;
- the universal formulas as frozen theorem statements, not as inferences from
  the grid;
- separate clock/support, marker/multiplicity, and determinant-coefficient
  certificates;
- source-positive, one-factor, repetition-weight, and separate-target-owner
  controls;
- all six repair classifications and
  `declared_repairs_are_exhaustive=false`;
- `ShiftPrimitiveNecklace_q`, `FiniteFieldPrimePolynomial_q`, and
  `RationalPrimeAtom` as distinct types;
- the independently derived unique survivor `SD-C01` and retrospective
  chronology;
- the strict Route tuple
  `(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,
  A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`;
- `overall_verdict=ROUTE_A_REJECTED` and Route B false; and
- `universal_no_go_claimed=false`.

The projection must not contain target-zero metrics, fitted coefficients,
prime-table rows, floating-point approximations, performance timing, or
claims of newly proving the classical source ledger.

## 7. Strict Route renderer and independent auditor

### Renderer

Suggested path: `code/evaluator/evaluate_route_a.py`.

The renderer consumes only canonical science bytes, the frozen integration
contract, the vendored Route-A v0.2 schema/skill bytes, and the current legal
provenance state. It must:

1. use exact canonical top-level and nested key sets;
2. render duplicate-free ASCII YAML in one deterministic key order;
3. re-root the authority Route card at
   `papers/42-function-field-clock-non-descent`, while preserving the immutable
   preauthority expectation at its own `.../preauthority` base;
4. use `preauthority/...`, `experiments/...`, and `results/...` artifact paths
   that resolve under the authority paper root;
5. derive every rung, evidence status, metric, terminal code, blocking
   condition, repair boundary, and Route-B field from canonical science and
   frozen contracts;
6. preserve A1/A2 source-positive status despite the rational-prime failure;
7. bind `scientific_results.json` by SHA-256; and
8. support exactly the two legal provenance states in Section 11.

The exact evidence-status ledger is A0 `PROVED`, A1 `PROVED`, A2 `PROVED`,
A3 `PROVED`, and A4 `OPEN`; A3's Weil-compression substatus remains the
frozen scoped stop. The exact terminal codes are
`STOP_Q_POWER_RATIONAL_PRIME_SUPPORT`,
`STOP_MARKER_MULTIPLICITY_CONJUNCTION`, and
`STOP_FIRST_MARKED_COEFFICIENT_MISMATCH`. The branch status remains
`CLOSE_SD_C01_SAME_CLOCK_SAME_MARKER_RATIONAL_PRIME_PROJECTION`.

The renderer must never read writer prose, a live external repository, a
paper manifest while in State A, or target data.

### Independent Route auditor

Suggested independent mode in `code/evaluator/independent_evaluator.py`, or a
separate `code/evaluator/audit_route_a.py` with no renderer import.

The auditor reparses YAML with duplicate-key rejection and independently
checks:

- exact v0.2 key sets, literal enums, legal evidence statuses, and artifact
  path resolution;
- all source-lock fields and forbidden-data boundaries;
- every A0/A1 control, the type ledger, determinant orientation, domains, and
  first-coefficient certificate;
- tuple, overall verdict, Route-B booleans, terminal set, chronology, and
  `universal_no_go_claimed=false`;
- the science hash and the exact set of authority integration fields;
- State A versus State B provenance without accepting a mixed state; and
- a normalized scientific Route payload that is identical across states
  after replacing only the permitted provenance fields.

The strict validator and independent auditor each emit their own check ledger.
Neither trusts renderer pass flags or an emitted expected tuple. The
read-only integrity auditor must validate the state-specific provenance
internally while emitting the same sorted check names, truth values, status,
and therefore byte-identical canonical stdout for both legal states.

## 8. Portable, self-contained source boundary

Canonical execution must not read a live historical repository or use the
network. Before the static integration seal:

1. copy the exact frozen 16-file preauthority package and external DA bytes
   into their authority-owned immutable locations;
2. vendor the exact 21 `repo:` source bytes and eight `dependency:P41_*`
   source bytes named by the 29-ID manifest into a package-relative snapshot;
3. store a path-safe ID-to-container map and byte hashes in
   `docs/DEPENDENCY_LOCK.json`;
4. vendor and hash the exact Route-A v0.2 schema and skill bytes;
5. reject absolute paths, `..`, symlink traversal, duplicate or unknown IDs,
   non-C-sorted IDs, missing or multiply resolved dependencies, and hash
   drift; and
6. record canonical external-tree state as `NOT_QUERIED`, never as a live
   comparison result.

All subprocesses use the declared isolated interpreter form, equivalent to
`python3 -I -B`. Canonical output must remain byte-identical when copied to a
different temporary root and invoked from a non-project working directory.
No output may serialize a host-specific absolute path, hostname, current
working directory, interpreter path, wall clock, file mtime, random seed, or
network state.

## 9. Adversarial mutation matrix

The implementation must freeze a C-sorted, unique mutation registry before
the one declared final canonical rerun. The blueprint fixes the mutation
classes, not their future generated IDs, count, or hash. Every applicable raw
mutation is executed against both scientific evaluators; Route mutations are
executed against both Route validators; static/state mutations are executed
against the read-only integrity auditor. A mutation passes only when every
designated consumer rejects it nonzero for the correct structural reason.

| Class | Raw mutation | Required rejection |
|---|---|---|
| JSON type | Replace `false` by `0`, integer by float, list by scalar, or string by number | Exact type/schema failure |
| JSON structure | Delete, duplicate, or add any top-level or nested packet field | Exact-set failure |
| Candidate | Change `SD-C44` or historical parent `SD-C01` | Candidate/provenance failure |
| Field grid | Add another `q`, delete a frozen `q`, or change a bound after seal | Control-grid failure |
| Rotation | Count based words as necklaces or omit cyclic quotient | Primitive-count failure |
| Reversal | Silently quotient reversal | Orientation/type failure |
| Primitivity | Mark `01` imprimitive or accept a proper power as primitive | Witness/least-period failure |
| Clock support | Mark `q^2` prime, change `n log q`, or permit a partial map as total | Clock/support theorem failure |
| Marker | Replace `z^n` by `z`, specialize `z=1`, or ignore exponent equality | Marker-contract failure |
| Weight | Replace `q^(-ns)` or `p^(-s)` by a different exponent | Weight certificate failure |
| Multiplicity | Merge the `q` degree-one classes without a projection flag | Multiplicity/totality failure |
| Repetition | Credit `z^(nr)` as `z^r` before primitive marker agreement | Repetition typing failure |
| Determinant sign | Swap determinant with reciprocal or flip `-log D` orientation | Determinant convention failure |
| Coefficient | Replace source `q^(1-s)` by `q^(-s)` or target `P(s)` by a finite list | Coefficient certificate failure |
| Domain | Claim target trace class outside `Re(s)>1` or a global log across zeros | Analytic-domain failure |
| Source positive control | Change fixed-point count, source determinant, or power law | Source-fidelity hard stop |
| Polynomial control | Corrupt irreducible count or identify equal counts as an objectwise bijection | Positive-control/type failure |
| Type owner | Retype a necklace as a rational prime or assign target `Q_s` to the source | Type/ownership failure |
| Repair scope | Set `declared_repairs_are_exhaustive=true` or silently add a repair | Quantifier failure |
| Repair classification | Flip any retained/lost coordinate in a declared row | Row-derivation failure |
| Selector | Preset `SD-C01`, use paper number/order, or remove one literal clause | Selection derivation failure |
| Card bytes | Modify, omit, duplicate, or reorder a historical card without canonical handling | Card hash/exact-set failure |
| Chronology | Set prospective, preregistered, blind, results unseen, novelty, or priority true | Chronology failure |
| P39--P41 role | Mark any predecessor as ranking, selecting, authorizing, or transferring credit | Governance failure |
| Literature boundary | Remove external `STOP_DUPLICATE` or turn bounded collision-search absence into novelty evidence | Literature/claim-boundary failure |
| Route A0 | Raise A0 above weak or erase the rational-prime support failure | Route semantic failure |
| Route A1/A2 | Lower source A1/A2 because the target projection fails | Route semantic failure |
| Route A3/A4 | Raise A3/A4 using the separate target comparator or finite adjacency | Route semantic failure |
| Route B | Set top-level `route_b_invocation_allowed` or nested `route_b.invocation_allowed` true, make them disagree, or delete/alter `route_b.reason` | Route-B hard failure |
| Route schema | Delete/insert/reorder list members, alter scalar type/value, or add mapping keys | Strict recursive schema failure |
| Artifact path | Use host-absolute, parent-escaping, nonexistent, or wrong-base artifact paths | Path-resolution failure |
| Source ID | Duplicate, unsort, rename scheme, use absolute/`..`, or change expected hash | Typed resolver failure |
| Dependency | Remove, multiply resolve, or symlink-escape a P41 dependency | Dependency-resolution failure |
| External tree | Make live authority available/unavailable or change it | Canonical bytes unchanged; any read is failure |
| CWD relocation | Run from another working directory and installation root | Canonical bytes must remain identical |
| Module shadow | Inject hostile `json`, `hashlib`, `pathlib`, `yaml`, project helper, or `sitecustomize` | Isolated canonical invocation unaffected; naive mode rejected |
| Cache | Precreate `__pycache__`, `.pyc`, or tool caches | Hygiene/audit failure or no creation under `-B` |
| Path leak | Force producer/evaluator to serialize an absolute input path | Portability failure |
| Output tamper | Flip any producer/evaluator/check/summary/chronology field without changing raw evidence | Independent consistency failure |
| Science hash | Alter science bytes but preserve an old hash | Hash-binding failure |
| Result set | Add, remove, rename, or symlink an expected output | Exact output-set failure |
| Result ledger | Self-include, unsort, duplicate, omit, path-escape, or use a wrong hash | Ledger failure |
| State A | Add a paper manifest or replace only one pending provenance field | Illegal mixed-state failure |
| State B | Omit manifest, use unequal/zero/non-hex/wrong commit values, or stale freeze note | Illegal sealed-state failure |
| Stage-2 scope | Change any path other than canonical Route card and root paper manifest | Metadata-only scope failure |

For recursive Route mutation, every scalar value and scalar type, every list
member/index/order, and every mapping key/presence must be covered. The four
provenance fields normalized between State A and State B are mutated and
tested separately, not excluded from adversarial coverage.

## 10. Run order and hard gates

### M0 — static-input seal

- Materialize code, contracts, experiments, vendored inputs, and mutation
  registry in an empty-output tree.
- Freeze a sorted self-excluding static-input manifest.
- Verify immutable package, DA, writer pointer, source IDs, Route schema, and
  dependency locks.
- Gate: no output tree exists; no static input has a host path or mutable
  external dependency.

### M1 — raw packet

- Run only the isolated packet producer.
- Validate exact key/type/path schema with a read-only packet linter.
- Gate: packet contains no derived answer or pass flag.

### M2 — independent science

- Run Algorithm M and Algorithm R as separate isolated processes.
- Require exact canonical science byte equality.
- Gate: every theorem and positive control derives from raw fields; any
  mismatch hard-stops before Route rendering.

### M3 — strict Route

- Render State-A Route YAML from canonical science.
- Run the strict validator and independent auditor.
- Gate: exact tuple, rejected overall verdict, Route B false, legal artifact
  base, and source A1/A2 preserved.

### M4 — adversarial suite

- Apply the frozen mutation registry to raw packet, output payload, Route,
  static dependency, and paired-state copies.
- Gate: zero survivors in every declared class for every designated
  evaluator/auditor.

### M5 — deterministic replay and cold copy

- Run independent clean A and B materializations.
- Copy static inputs to a different temporary root and execute cold C from a
  non-project working directory with the external historical tree unavailable.
- Gate: deterministic artifact bytes A=B=C, no path leak, and no external
  read.

### M6 — exact-set, ledger, idempotence, and paired states

- Materialize the exact result set, result ledger, report, and integrity
  audit in State A.
- Rerun the full parent and require zero writes and zero changed paths.
- In a disposable copy only, create hypothetical State B and require the
  read-only integrity-audit stdout to be byte-identical to State A.
- Gate: exact output set, valid self-excluding ledger, clean State A, clean
  hypothetical State B, mixed-state rejection, and final idempotence.

Only after all gates pass may an integrator issue a `FINAL / POST-OUTPUT
CLEAN` handoff. No failure may be converted to a pass by editing only a report
or expected tuple.

## 11. Legal State A / State B provenance

The canonical Route card path is
`evaluations/route_a/SD-C44/2026-08-17.yaml`.

### State A — complete first artifact, pending triple

- `/source_commit` is the literal `PENDING_FIRST_ARTIFACT_COMMIT`;
- `/code_commit` is the same literal;
- `/source_lock/code_commit` is the same literal;
- `/freeze_note` is the exact State-A note fixed by the integration contract;
- `PAPER_MANIFEST.sha256` is absent; and
- all approved static inputs, canonical outputs, writer publication bytes,
  PDF/report bytes, and root registration intended for the first artifact are
  already final.

### State B — metadata-only seal

After the real State-A artifact commit exists:

- the three commit fields receive the same actual lowercase nonzero 40-hex
  State-A artifact commit;
- `/freeze_note` receives the exact State-B note naming that commit; and
- a C-sorted, unique, path-safe, hash-valid, self-excluding
  `PAPER_MANIFEST.sha256` is added.

The State-A-to-State-B changed-path set is exactly:

```text
evaluations/route_a/SD-C44/2026-08-17.yaml
PAPER_MANIFEST.sha256
```

State B changes no science, code, experiment, result, report, writer, PDF,
immutable research/DA, root README, registry, or mirror byte. The manifest
includes the final State-B Route card and excludes itself. This blueprint
contains no commit value and does not authorize either state transition.

## 12. Exact expected canonical output path set

The future integration contract must declare exactly the following output
paths before the canonical run. No path is created by this blueprint.

```text
EXPERIMENT_REPORT.md
evaluations/route_a/SD-C44/2026-08-17.yaml
evaluations/route_a/SD-C44/independent_evaluation.json
results/SHA256SUMS.txt
results/adversarial_tests.json
results/algorithm_independence.json
results/analysis_summary.json
results/cold_copy_certificate.json
results/dependency_controls.json
results/determinant_coefficient_certificate.json
results/exact_result_set.json
results/exact_text_set.json
results/external_provenance_stability.json
results/function_field_positive_control.json
results/idempotence_certificate.json
results/immutable_inputs.json
results/independent_evaluation.json
results/integrity_audit.json
results/integrity_contract.json
results/main_evaluation.json
results/operator_ownership_certificate.json
results/repair_matrix_certificate.json
results/reproducibility_certificate.json
results/research_reproduction.json
results/route_evaluation.json
results/route_schema_certificate.json
results/runs/A/independent_evaluation.json
results/runs/A/main_evaluation.json
results/runs/A/route_evaluation.json
results/runs/A/scientific_results.json
results/runs/A/source_packet.json
results/runs/B/independent_evaluation.json
results/runs/B/main_evaluation.json
results/runs/B/route_evaluation.json
results/runs/B/scientific_results.json
results/runs/B/source_packet.json
results/runs/C/independent_evaluation.json
results/runs/C/main_evaluation.json
results/runs/C/route_evaluation.json
results/runs/C/scientific_results.json
results/runs/C/source_packet.json
results/scientific_results.json
results/sealed_state_compatibility.json
results/selection_resolver.json
results/source_evaluator_boundary.json
results/source_packet.json
results/source_resolver.json
results/type_contract_certificate.json
results/witness_certificate.json
```

`results/exact_result_set.json` lists the exact `results/**` subset above.
`results/exact_text_set.json` lists every integrator-managed text path and
states that writer paths are excluded. `results/SHA256SUMS.txt` is C-sorted,
unique, exact-set, path-safe, and self-excluding; it also excludes the Route
YAML and forbidden paper manifest, which have separate contracts. The two
evaluation paths and `EXPERIMENT_REPORT.md` are nevertheless part of the
parent's exact output set.

`PAPER_MANIFEST.sha256` is not a canonical experiment output and is forbidden
in State A.

## 13. Output-to-claim map

| Output | Claim defended | Required contents |
|---|---|---|
| `witness_certificate.json` | P1 clock/support and multiplicity | Primitive `01`, forced composite norm, length-one classes, no finite-to-universal inference |
| `determinant_coefficient_certificate.json` | P1 analytic mismatch | Correct determinant orientation, common domain, Algorithm-M coefficient map, Algorithm-R limit proof |
| `function_field_positive_control.json` | P2 source fidelity | Necklace and irreducible counts, source powers, determinant, no cross-type bijection claim |
| `operator_ownership_certificate.json` | P2 ownership | Source adjacency and target diagonal inventory separated by type, Hilbert space, marker, and domain |
| `repair_matrix_certificate.json` | P2 bounded repair classification | Six declared rows, exact lost coordinates, non-exhaustiveness flag false |
| `selection_resolver.json` | Retrospective selection | All six card rows, literal clause values, unique survivor, no ranking/authorization |
| `source_resolver.json` | Portability | All typed IDs, relative containers, hashes, negative-control classes, no live source read |
| `main_evaluation.json` | Independent replay M | Main checks, implementation identity, canonical science projection |
| `independent_evaluation.json` | Independent replay R | Independent checks, implementation identity, same science projection |
| `algorithm_independence.json` | No shared helper | Import graph, subprocess boundary, distinct algorithm certificates |
| `type_contract_certificate.json` | Type strictness | Exact type sets, marker/owner relations, bool/int and structure controls |
| Route outputs | Strict disposition | Exact v0.2 schema, tuple, Route B lock, artifacts, paired-state status |
| `adversarial_tests.json` | Sharpness | Frozen mutation IDs/classes, per-consumer rejection, zero survivors |
| reproducibility/cold/idempotence outputs | Determinism | A/B/C byte identity, relocation, non-project CWD, zero second-write changes |
| integrity outputs and ledger | Exact package | Exact path sets, hashes, hygiene, State A/B compatibility |
| `EXPERIMENT_REPORT.md` | Publication handoff | Claim-first result summary, exact chronology, canonical bindings, no novelty inflation |

## 14. Publication synchronization fields

The latest writer seal contains no canonical implementation block. Its unique
future insertion anchor is the paragraph beginning at frozen
`sections/6_route_reproducibility.tex:44`:

```text
This writer scaffold contains no canonical implementation block, experiment
```

Only after a designated final handoff may that paragraph be replaced by one
canonical block. Values may be inserted only for the following fields, and
each must be verified against the named canonical artifact:

| Publication field | Canonical source |
|---|---|
| `MAIN_EVALUATOR_CHECKS_PASSED` / `MAIN_EVALUATOR_CHECKS_TOTAL` | `results/main_evaluation.json` |
| `INDEPENDENT_EVALUATOR_CHECKS_PASSED` / `INDEPENDENT_EVALUATOR_CHECKS_TOTAL` | `results/independent_evaluation.json` |
| `CANONICAL_SCIENCE_SHA256` | exact bytes of `results/scientific_results.json` and Route binding |
| `SOURCE_RESOLVER_MATCHES` / `SOURCE_RESOLVER_TOTAL` | `results/source_resolver.json` |
| `SELECTION_SURVIVORS` | `results/selection_resolver.json` |
| `THEOREM_FAILURES` | canonical science/Route theorem ledger |
| `POSITIVE_CONTROL_FAILURES` | `results/function_field_positive_control.json` |
| `REPAIR_ROWS_CHECKED` / `REPAIR_FAILURES` | `results/repair_matrix_certificate.json` |
| `MAIN_ROUTE_CHECKS_PASSED` / `MAIN_ROUTE_CHECKS_TOTAL` | `results/route_evaluation.json` |
| `INDEPENDENT_ROUTE_CHECKS_PASSED` / `INDEPENDENT_ROUTE_CHECKS_TOTAL` | independent Route evaluation |
| `ROUTE_TUPLE` | canonical science and Route card |
| `OVERALL_VERDICT` | canonical science and Route card |
| `ROUTE_B_INVOCATION_ALLOWED` | canonical science and Route card |
| `MUTATION_GROUP_COUNTS` / `MUTATION_SURVIVORS` | `results/adversarial_tests.json` |
| `MUTATION_IDS_SHA256` / `MUTATION_REGISTRY_SHA256` | `results/adversarial_tests.json` and static registry |
| `RUN_A_B_C_BYTE_IDENTICAL` | `results/reproducibility_certificate.json` |
| `COLD_COPY_RUN_C_EQUALS_RUN_A` | `results/cold_copy_certificate.json` |
| `STATE_A_B_AUDIT_BYTE_IDENTICAL` | `results/sealed_state_compatibility.json` |
| `INTEGRITY_AUDIT_CHECKS_PASSED` / `INTEGRITY_AUDIT_CHECKS_TOTAL` | `results/integrity_audit.json` |
| `INTEGRITY_AUDIT_SHA256` | exact bytes of `results/integrity_audit.json` |
| `IDEMPOTENCE_CHANGED_PATHS` | `results/idempotence_certificate.json` and parent stdout |
| `RESULT_LEDGER_ENTRY_COUNT` / `RESULT_LEDGER_SHA256` | parsed and hashed `results/SHA256SUMS.txt` |
| `EXACT_OUTPUT_PATH_COUNT` | parent exact-output set |
| `INTEGRATION_CHRONOLOGY_STATUS` | canonical science chronology |
| `FINAL_PARENT_STATUS` | final isolated parent stdout |

No value is supplied by this blueprint. The writer must not insert a commit,
paper-manifest hash, target-zero metric, fitted value, timing claim, or result
derived from a transient tree. After insertion, synchronize only the bounded
result-status prose in `PAPER_PLAN.md` and `WRITER_HANDOFF.md`, rebuild out of
tree, and preserve all theorem, scope, `STOP_DUPLICATE`, chronology, and
Route-language firewalls.

## 15. Acceptance and stop table

| Gate | GO condition | STOP / repair condition |
|---|---|---|
| Source convention | Both algorithms derive the same source ledger and positive controls | `STOP_SOURCE_CONVENTION_MISMATCH` |
| Totality/marker logic | Raw contract and both evaluators agree the obligations are necessary for the claimed full ledger | `STOP_INVALID_TOTALITY_OR_MARKER_REQUIREMENT` |
| Duplicate boundary | Frozen DA/literature binding remains valid | `STOP_DUPLICATE` |
| Quantifiers | Every theorem and repair row stays within its frozen class | `REVISE_QUANTIFIER_SCOPE` |
| Route | Exact tuple, overall rejection, Route B false, A1/A2 preserved | `REVISE_ROUTE_TUPLE` |
| Algorithm independence | Separate processes, no shared project helper, exact science byte equality | hard implementation STOP |
| Type strictness | Every schema/type mutation rejected | hard implementation STOP |
| Portability | Cold relocation is byte-identical with no live external read/path leak | hard implementation STOP |
| Reproducibility | A/B/C deterministic artifacts identical; final rerun writes nothing | hard implementation STOP |
| Paired states | State A and hypothetical State B legal; all mixed states rejected | hard seal STOP |
| Publication | Only final canonical fields inserted; no scope or chronology drift | writer HOLD |

## 16. Resource and reporting boundary

This is a bounded exact CPU experiment. It uses no GPU, network, human
evaluation, stochastic seed, training budget, target data, or parameter
search. The exhaustive control grid is fixed in Section 3. No wall-time,
memory, output count, mutation count, result hash, or commit is predicted in
this blueprint; those are measured or sealed only by a future authorized
implementation.

The final report must lead with the theorem-replay outcome, then state the
source-positive controls, typed repair/owner result, strict Route tuple,
mutation and portability evidence, paired-state status, and exact chronology.
It must say that computation independently replayed already-known mathematics;
it must not call the run prospective evidence or assign novelty to classical
full-shift, necklace, finite-field, or rational Euler-product identities.
