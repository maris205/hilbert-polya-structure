# R401-VAL-L3-A1 scheduler and archive contract candidate

Contract identifier: `R401-VAL-L3-A1-SCHEDULER-CONTRACT`

Prepared: 2026-08-09 UTC

Status: **PROSPECTIVE_NON_LICENSING / REJECT_FOR_DISPATCH**

## 1. Scope

This contract specifies a future two-component scheduler for the exact
102-cell matrix in `R401_VAL_L3_A1_PROTOCOL.md`.  It dispatches proof tasks,
commits raw and canonical bytes, resumes an identical generation, and builds
producer aggregates.  It never evaluates scientific truth and never assigns
a component, milestone, theorem, or final pass.

Partial mock/static/branch implementation candidates now exist, but the
complete production scheduler, machine freeze, main freeze, and accepted
independent pre-freeze review do not.  Therefore no CLI execution mode may
dispatch an evaluator in the current repository state.

## 2. Canonical task identities and stages

A cell key is the exact pair

```text
(precision_bits, slab_id)
```

in protocol order: all 51 slabs at 128 bits followed by all 51 at 256 bits.
A task key is

```text
(component, precision_bits, slab_id),
component in {STATIC, BRANCH}.
```

The scheduler policy candidate is

```text
deterministic_component_barrier_batches_v1.
```

The static stage runs first.  At most eight distinct static cells are in one
barrier batch.  Completed cells are committed in canonical cell order,
independently of completion order.  A successful production generation then
runs the branch stage with at most six distinct branch cells per barrier,
again committing canonically.  No cell has more than one inflight task.

Branch admission begins only if all 102 static producer cells are structurally
complete and carry `STATIC_CELL_CERTIFIED`.  This producer gate is an
operational stop rule, not a scientific status.  If it fails, the generation
is preserved as non-passing and no branch task is dispatched.

## 3. Frozen one-cell ABIs

### 3.1 Static ABI

The future static Python process receives the exact frozen Python path,
precision, slab identity, epsilon endpoints, root definitions, limits, and
main-freeze/run-config identities.  It emits one strict canonical JSON proof
stream and exactly one evaluator status.

The only allowed pairs are:

| evaluator status | code | scheduler meaning |
|---|---:|---|
| `STATIC_CELL_CERTIFIED` | 0 | commit a complete proof candidate |
| `STATIC_UNRESOLVED_DEPTH` | 2 | commit resource-inconclusive cell and stop promotion |
| `STATIC_UNRESOLVED_NODE_BUDGET` | 2 | commit resource-inconclusive cell and stop promotion |
| `STATIC_INTERVAL_FAIL` | 3 | commit evaluator failure and stop promotion |
| `INVALID_STATIC_PROOF_CONTRACT` | 5 | commit invalid result and stop the generation |

There is no generic static violation status.  A box that fails to prove an
angle or landing gate is unresolved unless a separately frozen constrained
existence-witness contract exists.

### 3.2 Branch ABI

The future persistent CAPD binary receives exactly 12 strings:

1. frozen absolute binary path;
2. precision bits;
3. epsilon lower endpoint;
4. epsilon upper endpoint;
5. eight exact primary-box endpoints in
   `(Q_minus,Q_plus,P_minus,T)` order.

The only allowed pairs are:

| evaluator status | code | scheduler meaning |
|---|---:|---|
| `BRANCH_CELL_CERTIFIED` | 0 | commit a complete branch transcript candidate |
| `BRANCH_TUBE_UNRESOLVED` | 2 | commit inconclusive enclosure and stop promotion |
| `BRANCH_FLOW_FAIL` | 3 | commit CAPD failure and stop promotion |
| `BRANCH_TUBE_VIOLATION` | 4 | commit a lower-bound-certified scientific stop |
| `INVALID_BRANCH_PROOF_CONTRACT` | 5 | commit invalid result and stop the generation |

`BRANCH_TUBE_VIOLATION` requires a lower-bound proof at or above `0.0016`.
An upper enclosure that crosses the threshold is only unresolved.

### 3.3 Scheduler classifications

Evaluator status and scheduler classification are separate.  The closed
scheduler namespace is:

```text
COMMITTED_EVALUATOR_RESULT
CELL_TIMEOUT
CELL_SIGNAL
CELL_OUTPUT_BUDGET_EXHAUSTED
MALFORMED_EVALUATOR_OUTPUT
PROVENANCE_INVALID
```

Only `COMMITTED_EVALUATOR_RESULT` carries a non-null evaluator status.  Every
other classification carries `evaluator_status = null`, preserves available
raw bytes, and blocks promotion.  Missing/repeated status, Boolean return
code, unlisted status/code pair, nonempty stderr on a nominal pass, malformed
JSON/transcript, timeout, or signal is never splittable or silently retried.

## 4. Candidate budgets and admission

The future main freeze must select exact values.  The implementation
candidates are:

```text
static workers                       8
static maximum depth per tree        24
static maximum nodes per tree        250000
static maximum nodes per cell        1000000
static timeout per cell              1800 seconds
static maximum total cell bytes      512 MiB

branch workers                       6
branch timeout per cell              600 seconds
branch stdout cap                    16 MiB
branch stderr cap                    1 MiB
branch record cap                    4 MiB
branch maximum total cell bytes      32 MiB

max inflight per component cell      1
global scientific budget             null
```

Static and branch worker pools are never active together.  The future machine
freeze must show

```text
idle baseline + workers*representative peak RSS + 8 GiB reserve <= 48 GiB.
```

Candidate storage gates are launch at or above 200 GiB free, warning below
180 GiB, pause new admission below 150 GiB, and inventory/recovery only below
120 GiB.  Memory admission pauses at 48 GiB cgroup current usage.  Admission
is rechecked before every barrier.

A memory or disk pause occurs after the current barrier commits and leaves a
resumable incomplete generation.  It does not create a failure status.  A
depth, node, timeout, or byte cap is a frozen inconclusive result and cannot
be relaxed after inspection within the same generation.

## 5. Bounded streaming and process control

The scheduler continuously drains stdout and stderr to staging files and
counts bytes.  It may not use an unbounded in-memory capture.  Static proof
bytes are likewise streamed to the staging proof path.

If a frozen per-stream, record, or total-cell cap is reached, the scheduler:

1. stops accepting bytes beyond the exact cap;
2. sends `SIGTERM` to the evaluator process group;
3. waits a future frozen grace interval;
4. sends `SIGKILL` to the complete group if necessary;
5. waits for and records group termination;
6. commits `CELL_OUTPUT_BUDGET_EXHAUSTED`, exact captured counts, caps, and
   `truncated=true`; and
7. prevents automatic retry and promotion.

Timeout follows the same process-group termination sequence and commits
`CELL_TIMEOUT`.  A scheduler or operator crash before cell commit is
different: resume may rerun the exact task because no authoritative outcome
exists.  Orphan-descendant and TERM/KILL escalation tests are mandatory
before freeze construction.

## 6. Result and operational namespaces

The authoritative root is exactly

```text
results/r401_val_l3_all_slabs/
```

with component cells, cell manifests, aggregates, three checker results,
three postchecks, composite controls, report, and release laid out by the
protocol and checker contract.

All temporary and telemetry paths live in the same-filesystem sibling

```text
results/r401_val_l3_all_slabs.operational/
```

and never below the authoritative root.  For each component and precision,
the only legal live or retained interrupted staging path is

```text
staging/{static,branch}/{128,256}/
  .{slab_id}.tmp-{generation_prefix_16hex}-{attempt_decimal}
```

Its basename is matched exactly by

```text
^\.(S(?:00[0-9]|0[1-4][0-9]|050))\.tmp-([0-9a-f]{16})-(0|[1-9][0-9]*)$
```

The 16-hex prefix is the first 16 lower-case hexadecimal digits of the sealed
`run_config.json` SHA-256.  The attempt is a canonical nonnegative decimal
integer (`0` or a nonzero digit followed by digits).  This is the same
generation-bound namespace required by the reviewed pre-freeze design and
the branch runtime; the earlier `.cell-...staging`/detached `interrupted/`
candidate is withdrawn.  No other hidden path is recognized.  Independent
scanners reject every hidden or extra path below the authoritative root.

## 7. Cell transaction

One component cell is one same-filesystem transaction:

1. exclusively create its canonical live staging directory;
2. write streamed raw/proof files and the strict record;
3. flush every file;
4. flush the staging directory;
5. atomically rename staging to the canonical cell directory;
6. flush both the staging parent and canonical parent directories;
7. derive the unique cell manifest from the published bytes;
8. write and flush the cell manifest with exclusive creation; and
9. flush the manifest parent directory.

Static authoritative cells contain exactly `proof.json` and `record.json`.
Branch authoritative cells contain exactly `stdout.txt`, `stderr.txt`, and
`record.json`.  Telemetry is operational and absent from both.

A cell manifest binds the exact task, invocation hash, record, all raw/proof
hashes and sizes, evaluator/source/binary identities, main freeze, run config,
and null producer authority.  It contains no self-hash.

## 8. Resume and manifest-less recovery

Resume derives the frontier from strict validation of published cell
manifests, not from scheduler counters.  A committed non-pass is authoritative
and is not automatically retried.

A crash can leave a canonical cell directory after atomic rename but before
its manifest.  That directory is not a committed pass.  Resume may publish
the manifest only after independently rebuilding the frozen task, validating
every canonical byte, and deriving the unique expected manifest without
changing the cell directory.  If exact recovery fails, the entire generation
is quarantined.  The cell is never overwritten or mixed with a rerun.

A live operational staging directory is handled before new admission.  If it
is a complete exact transaction it may finish the same atomic publication.
Otherwise the scheduler fails closed: no fresh attempt and no aggregate may
be admitted while that retained object exists.  Recovery requires the
write-once whole-generation quarantine transaction in section 9; the next
generation then starts with an empty staging namespace.  There is no detached
per-cell interrupted namespace and no same-generation partial-stage deletion.
These operations never alter an authoritative cell.

## 9. Run binding and whole-generation quarantine

The write-once `run_config.json` binds at least:

- formal protocol, scheduler/checker/release contracts, machine freeze, and
  main-freeze hash;
- exact 102 matrix and matrix digest;
- complete 53-role mandatory input-hash map defined by the release contract;
- both evaluator ABIs, source/binary/toolchain/runtime identities;
- static and branch limits, status tables, scheduler policy, worker counts,
  maximum inflight value, and process-group grace interval;
- exact result and operational roots and filesystem identity; and
- null producer authority and claim boundary.

The prospective provenance contract enumerates exactly 53 ordered
main-freeze input roles and exactly 68 ordered release roles.  The scheduler
may bind those maps but cannot add, remove, reorder, or license a role.

Resume first requires the stored raw `run_config.json` bytes to equal the
strict canonical JSON serialization of the parsed object, then requires
type-strict equality of the complete binding.  Semantically equal whitespace,
key-order, numeric-spelling, or trailing-byte variants are rejected.  A
changed worker count, timeout, threshold, role hash, output root, binary, or
scheduler policy is a different generation.

An explicit quarantine operation first exclusively writes and flushes the
canonical sibling intent journal
`{authoritative_name}.quarantine-transaction.json`.  The strict canonical
journal binds the source authoritative/operational roots, both selected
quarantine destinations, transaction index, reason, and whether the
operational sibling existed.  Only then may the two directory renames occur.
Each rename is followed by parent-directory flushes.  Resume detects the
journal before opening or creating a run config, infers each rename state from
the exact source/destination pair, completes any missing rename, writes the
null-authority `QUARANTINE_RECORD.json`, and removes the journal only after
the record is durable.  Both/neither source/destination states, noncanonical
or schema-invalid journal bytes, a noncanonical bound path, destination
collision, or reason mismatch fail closed.
This makes crashes before either rename, between the renames, after both, or
after record publication recoverable without mixing generations.  It never
deletes scientific data.  Static, branch, or checker objects from different
generations may never be combined.

## 10. Aggregates and deterministic bytes

After all 102 component cells commit, the scheduler writes the component
aggregate summary followed by its aggregate manifest.  The manifest binds the
ordered 102 cell manifests and the ordered content root.  It contains no
self-hash.

Aggregate construction and resume exact-scan the component namespace before
accepting any digest.  The cell root contains exactly precision directories
`128` and `256`; each contains exactly `S000` through `S050`; and each static
cell contains exactly `proof.json` and `record.json` while each branch cell
contains exactly `stdout.txt`, `stderr.txt`, and `record.json`.  The parallel
manifest hierarchy is equally exact.  An extra cell subtree, ordinary file,
hidden entry, linked alias, or aggregate/control name blocks publication even
when all 102 expected manifests individually validate.

Canonical proof, cell, and aggregate payloads exclude wall time, hostname,
PID, peak RSS, completion order, and platform display strings.  Those values
may appear only under the operational sibling.  With identical frozen inputs,
worker completion order cannot change canonical scientific bytes.

The scheduler writes composite producer controls only after both component
aggregates exist.  Those controls retain null component, milestone, theorem,
and final statuses.  Scientific checkers and postchecks are downstream and
are never scheduler outputs.

## 11. Required pre-freeze tests

The future focused suite must cover:

- exact 102-cell order and one-inflight-per-cell barriers;
- randomized completion-delay invariance;
- atomic admission at depth/node/byte boundaries;
- crash before and after every flush, rename, and manifest boundary;
- exact manifest-less recovery and failure-to-quarantine behavior;
- whole-generation quarantine under every run-binding mutation;
- quarantine-journal recovery after intent, each directory rename, and
  record publication;
- timeout, signal, output cap, descendant process, and TERM/KILL escalation;
- memory and storage pause without scientific status;
- missing, extra, aliased, symlinked, hard-linked, or hidden authoritative
  paths;
- strict JSON, duplicate-key, type-alias, and nonfinite-number rejection; and
- a complete mocked 102-static plus 102-branch run without evaluator dispatch.

## 12. CLI and present rejection gate

A future scheduler may offer `--initialize-only`, `--resume`, and explicit
production modes.  `--initialize-only` validates a real accepted main freeze
and writes only the run config.  Production mode must fail closed unless the
exact main freeze has status `FROZEN_FOR_PRODUCTION`, its sole independent
pre-freeze verdict is `Verdict: ACCEPT_FOR_FREEZE`, live machine admission
passes, and every mandatory hash agrees.

Current exact state:

```text
contract_status = PROSPECTIVE_NON_LICENSING
implementation_stable = false
machine_freeze_exists = false
main_freeze_exists = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```

This contract records no executable production command.
