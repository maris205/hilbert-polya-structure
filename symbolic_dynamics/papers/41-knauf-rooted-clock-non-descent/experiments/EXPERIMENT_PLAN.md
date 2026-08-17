# SD-C43 exact authority-integration experiment plan

This plan implements the frozen retrospective contract in
`experiments/PREREGISTRATION.md`. It is frozen before authority code,
vendored runtime inputs, Route outputs, results, and the experiment report.

## 1. Claim-to-test matrix

| ID | Scoped claim | Independent evidence | Failure condition |
|---|---|---|---|
| C1 | The matrix convention is exactly the frozen `SD-C06` convention. | Matrix evaluator, recurrence evaluator, and exhaustive prefixes through length three agree. | Any word-order, multiplication, complement, or recurrence mismatch. |
| C2 | Right append-one does not descend to the trailing-zero colimit. | Recompute `epsilon ~ 0`, colimit invariance of `h`, and distinct labels of the two append-one images. | The equivalence, invariance, or distinguishing witness fails. |
| C3 | The rooted clock is neither cyclic nor power-compatible. | Recompute both rotation labels and the word-square labels with exact integers. | Either frozen inequality disappears or a changed clock is substituted. |
| C4 | The literal Liouville observable is not a scalar orbit character. | Independently factor generated labels, test cyclicity, repetition, and the one-letter contradiction. | A sign is imported, a factorization differs, or only one required failure is checked. |
| C5 | The diagonal determinant belongs to state inventory only. | Verify exact finite determinant/trace coefficients, the inherited multiplicity assumption, domains, marker types, and the eigenvalue-one factor. | Inventory powers are credited as binary returns, domains expand, or the first trace is identified with the whole determinant. |
| C6 | The six-card Boolean rule returns only `SD-C06` and is explicitly retrospective. | Resolve all six normalized card records and evaluate every literal clause in both evaluators. | Missing/duplicate card, hash drift, hidden predicate, preset winner, prospective claim, or different survivor set. |
| C7 | Strict Route-A v0.2 yields the frozen rejected tuple and keeps Route B locked. | Decode the exact vendored skill, construct the card from science results, and validate schema and semantics independently. | Any layer, status, control, metric, artifact, overall, or Route-B field drifts. |
| C8 | The authority certificate is reproducible and ownership-safe. | A/B/cold reproduction, mutation replay, exact sets, self-excluding ledger, paired-state audit, relocation, and idempotence. | Any byte mismatch, accepted mutation, path drift, mixed state, or forbidden write. |

No row establishes a universal no-go for enlarged states, trace or eigenvalue
clocks, non-scalar cocycles, Farey/Gauss operators, Selberg determinants, or
other changed models.

## 2. Planned integration-owned files

The static implementation will use:

```text
code/audit_integrity.py
code/contracts/INTEGRATION_CONTRACT.json
code/contracts/MUTATION_REGISTRY.json
code/contracts/ROUTE_A_V0_2_SCHEMA.json
code/evaluator/evaluate_packet.py
code/evaluator/evaluate_route_a.py
code/evaluator/independent_evaluator.py
code/run_exact_integration.py
code/run_tests.py
code/source/emit_packet.py
code/source/source_core.py
docs/DEPENDENCY_LOCK.json
docs/INTEGRITY_PROTOCOL.md
docs/inputs/SESSION4_SELECTION_PACKET.json
docs/inputs/dependencies/paper40_DA_REPORT.md
docs/inputs/dependencies/paper40_DA_REPORT.sha256
docs/inputs/route-a-evaluator-v0.2.0.md.b64
```

The contract will freeze exact integration-owned paths, immutable research
hashes, local dependency hashes, Python imports, result paths, text paths,
Route path, stage notes, terminal codes, type sets, marker sets, witness sets,
and mutation IDs. It will not enumerate or hash mutable writer files.

## 3. Source packet

`source_core.py` reads only local frozen contracts and vendored inputs. It
emits primitive data rather than trusted conclusions:

- raw `L` and `R` matrices and the ordered word fixtures;
- direct-limit generator pairs, cyclic pairs, repetition pairs, and
  one-letter-character fixtures;
- integer ranges for exact recurrence and diagonal-inventory controls;
- typed object, marker, operator, determinant, domain, and repair records;
- the normalized six-card selection packet with original byte hashes;
- the portable 22-ID source manifest plus a local dependency map;
- chronology booleans and claim-boundary tokens;
- strict Route schema and vendored skill hashes.

The source module performs grammar and local-input checks but emits no trusted
theorem verdict, survivor, Route tuple, or aggregate PASS Boolean.

## 4. Main evaluator

The main evaluator reads canonical packet bytes and recomputes:

1. ordered 2-by-2 matrix products and every `h` value;
2. the recurrence table for all prefixes through length three;
3. T1--T3 witnesses and positive controls;
4. Liouville values by exact trial division;
5. Euler-phi multiplicities for the finite inventory control and exact
   rational trace/determinant coefficients;
6. the type/marker/operator and repair ledgers;
7. all six Boolean selector rows and the singleton result;
8. the portable source-ID resolver result and negative-control classes;
9. a normalized science projection with exact witness and terminal sets.

Any mismatch raises a structured rejection; a packet cannot request a
different convention or silently weaken a universal identity.

## 5. Independent evaluator

The independent evaluator is a standalone program with no import from
`code/source`, `evaluate_packet.py`, or the Route renderer. It parses the
entire packet, computes `h` from the recursive complement rule, separately
checks raw matrix products, implements its own factorization and totient
routines, reconstructs the selection rule from literal fields, and emits the
same normalized science projection.

Static AST inspection verifies the import boundary and the exact standard
library plus PyYAML dependency contract.

## 6. Strict Route renderer and evaluator

The Route module decodes the locally vendored v0.2.0 skill bytes and checks
their frozen digest before loading the schema fixture. It renders one
canonical Stage-1 card at
`evaluations/route_a/SD-C43/2026-08-17.yaml` with three pending provenance
fields and no paper manifest.

Validation includes duplicate-key rejection, exact top-level/source/layer
key sets, evidence/verdict label membership, nonempty and distinct artifacts,
artifact-path containment, exact tuple consistency, required A2 metrics,
A0/A1 controls, target-data nonuse, scoped terminal language, and the false
Route-B lock. A separate JSON projection records the independent semantic
evaluation.

## 7. Mutation execution

`MUTATION_REGISTRY.json` gives every mutation a stable ID, packet or Route
target, field class, and expected rejection class. `run_tests.py` constructs
each mutation programmatically and invokes both evaluators in isolated
processes. Route mutations include explicit semantic attacks and recursive
schema leaf deletion, replacement, insertion, and duplicate-key attacks.

The report records the exact sorted mutation-ID set and SHA-256. A mutation
count without the exact ID ledger is insufficient.

## 8. Orchestration and deterministic outputs

`run_exact_integration.py` performs, in order:

1. verify the two frozen experiment files and all immutable research/DA
   anchors;
2. verify local dependencies and vendored Route skill bytes;
3. generate a source packet in a fresh run directory;
4. execute main and independent evaluators as separate processes;
5. compare normalized science projections byte-for-byte;
6. render and independently validate the strict Route card;
7. execute all packet and Route mutations against both validators;
8. repeat as runs A and B and compare deterministic bytes;
9. build results, exact path inventories, and a self-excluding result ledger;
10. run the read-only State-A integrity audit;
11. copy to an isolated empty-output tree, run cold C from another working
    directory, and compare deterministic bytes;
12. create an isolated dummy State-B copy and require identical audit check
    names, ordering, count, and success values;
13. rerun the full pipeline and require `changed_paths=0`.

Canonical JSON uses sorted keys, ASCII encoding, two-space indentation, and
one final linefeed. YAML order is explicitly defined by the renderer. Fixed
integer seeds are allowed only for deterministic mutation/control fixtures;
no target data or best-seed selection exists.

## 9. Planned result contract

The exact result set will include run-level A/B/C packets and evaluations,
top-level source/science/Route projections, mutation results, dependency and
source-resolver controls, source/evaluator separation, exact-set controls,
paired-state compatibility, cold-copy and idempotence certificates, the
integrity audit, and `results/SHA256SUMS.txt`.

The ledger excludes itself, the fixed Route YAML, and the forbidden paper
manifest. These exclusions are explicit and machine checked. The Route YAML
is checked independently by the strict Route validator.

## 10. Acceptance and handoff

Canonical handoff requires all of:

- immutable package 15/15 and research lock 14/14;
- portable source resolver 22/22 plus all registered negative controls;
- exact main/independent science equality;
- zero frozen theorem failures;
- singleton retrospective survivor `SD-C06` with all overclaim flags false;
- exact Route tuple, rejected overall verdict, and Route B false;
- zero survivors across the exact mutation-ID set in both evaluators;
- byte-identical A/B/cold deterministic artifacts;
- exact result/text sets and a valid self-excluding ledger;
- State A and isolated State B read-only audit success;
- final `changed_paths=0` idempotence;
- ownership and text hygiene clean.

The handoff may invite the writer to consume canonical result bytes. It does
not authorize writer edits, a paper manifest, Git activity, registry changes,
root README changes, or mirror publication.
