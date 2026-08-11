# R401-VAL-L3-A1 prospective all-slab pre-freeze design

Design identifier: `R401-VAL-L3-A1-PREFREEZE-DESIGN`

Prepared: 2026-08-09 UTC

Repository baseline: `529697ce3feccf11d16f739d0e07d27a2d1c4d16`

Design status: **PROSPECTIVE / NON_LICENSING / REJECT_FOR_DISPATCH**

## 1. Decision and exact scope

The accepted A4.16 S0 archive supports construction of a formal all-slab
experiment, but its component runners are not production schedulers.  The
minimum prospective production matrix is

```text
128 bits: S000, S001, ..., S050
256 bits: S000, S001, ..., S050
```

and contains exactly 102 parameter--precision cells.  Every cell has two
logically independent obligations:

1. a static Arb/exact-dyadic phase-anchor certificate containing the outer,
   fast-angle, and positive-section landing trees; and
2. a CAPD multiprecision `SolutionCurve` certificate for the accepted branch
   over the complete normalized period.

Thus the frozen experiment will have 102 composite cells but 204 component
evaluations.  The two component archives must be independently checkable and
independently resumable.  They are joined only after both component checkers
pass the identical 102-cell matrix.

The prospective mathematical result is the following local, conditional
statement over the exact 51-slab parameter cover.

- Every energy-one periodic candidate with period in `[0.64,0.69]` that stays
  in `r_minus < 0.06` over its complete period is the accepted branch modulo
  time translation.
- The accepted branch itself stays in the stricter tube `r_minus < 0.04` over
  its complete period.

This does not place an arbitrary global candidate inside the tube.  It does
not establish global orbit uniqueness, a trace formula, a Hilbert--Polya
operator, zeta-zero reconstruction, RH, or an implication toward RH.

No file described here is a freeze.  This document does not authorize an
all-slab evaluator dispatch.

## 2. Audited evidence and scaling envelope

The design uses only the already public representative cells
`S000`, `S025`, and `S050` at 128 and 256 bits.  No outcome from another L3
cell was inspected during this audit.

| Component | Accepted S0 observation | Linear 102-cell envelope | Interpretation |
|---|---:|---:|---|
| static proof nodes | 84,172 over 6 cells; maximum depth 14 | 1,430,924 nodes | planning estimate, not a pass threshold |
| static producer wall | 6.926 s, serial | 117.7 single-process s | excludes future scheduling and filesystem overhead |
| static archive | about 25 MiB | about 425 MiB | ordinary-case estimate only |
| branch evaluator wall | 44.83 process-s over 6 jobs | about 762 process-s | compilation is to be removed from production |
| branch concurrent wall | 17.37 s with 6 workers | roughly 2--5 min with 6 workers | heuristic operational estimate |
| branch raw transcript | about 0.54 MiB over 6 jobs | about 9.2 MiB | excludes aggregate and provenance objects |

The static S0 maximum was 14,498 nodes in one cell.  The branch S0 maximum
rigorous value was

```text
r_minus^2 <= 0.0001124580903773778485...
```

against the fixed threshold `0.0016`.  These observations justify continued
engineering but cannot select a held-out scientific outcome.

## 3. Component separation

### 3.1 Static phase-anchor component

One static evaluator process receives one frozen cell and produces one
canonical proof payload containing exactly four trees:

```text
ANGLE
SECTION_LOW
SECTION_HIGH
SECTION_WINDOW
```

The following S0 mathematics may be extracted without semantic changes:

- construction of the algebraic normal-mode model;
- exact rational and Arb interval conversion;
- Hamiltonian, slow-radius, `D_plus`, `N_plus`, and angular-rate evaluation;
- terminal classification and deterministic dyadic splitting;
- outer-domain gates and decisive-extrema accumulation; and
- the independent checker's no-import tree replay.

The production evaluator must not import the S0 runner as an executable
module.  A new cell evaluator must expose the frozen limits and exact input
identity through its ABI.  Its canonical proof must exclude wall time,
hostname, process identifier, completion order, and mutable absolute output
paths.

The static cell is the correct transaction boundary.  A representative cell
takes about one second and produces about 4--5 MiB, so node-level subprocess
dispatch would add complexity without a corresponding recovery benefit.  A
crash before the cell commit reruns that cell; a committed cell is validated
and skipped on resume.

### 3.2 Continuous branch-tube component

The following C++ S0 core may be retained after independent source review:

- the six-state normalized-time vector field;
- interval epsilon and period as constant state variables;
- Taylor order 24;
- CAPD multiprecision `SolutionCurve` evaluation;
- the exact 64-cell closed dyadic cover of `[0,1]`; and
- outward state boxes used to certify `r_minus^2 < 0.0016`.

The production binary must be built once before the main freeze and placed at
a persistent, non-symlinked path.  Production may not compile into its result
directory.  The formal machine record must bind the C++ source, a declarative
compile template targeting `@STAGING_BINARY@`, an actual argv-list rebuild
with `shell=false` in an owned direct-child `/tmp` directory, no-overwrite
transfer evidence for the persistent role-17 binary, the CAPD commit and
libraries, runtime libraries, binary mode, size, and SHA-256 digest.

The current S0 runner's direct concurrent writes, runtime compilation,
absolute-path manifest, wall-time fields, and fixed representative matrix
must not be carried into production.  Each branch process must run in a new
process group so timeout handling can terminate the complete descendant
group before the cell is classified.

### 3.3 Composite boundary

Neither component producer nor its aggregate builder may infer the A4.16
conclusion.  The composite checker must require both independently accepted
component records for every one of the 102 exact cell identities, bind the
accepted A4.15 release, and replay the analytic implication recorded in the
A4.16 derivation.  No component result may fill in a missing partner or a
missing precision.

## 4. Required new production files

Names below are prospective.  They become authoritative only if their exact
bytes are included in a later accepted main freeze.

### 4.1 Protocol and freeze inputs

```text
research/route_a_wave_trace/R401_VAL_L3_A1_PROTOCOL.md
research/route_a_wave_trace/R401_VAL_L3_A1_SCHEDULER_CONTRACT.md
research/route_a_wave_trace/R401_VAL_L3_A1_CHECKER_CONTRACT.md
research/route_a_wave_trace/R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md
research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json
research/route_a_wave_trace/R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json
research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_TESTS.json
research/route_a_wave_trace/R401_VAL_L3_A1_PREFREEZE_REVIEW.md
research/route_a_wave_trace/R401_VAL_L3_A1_FREEZE.json
```

`R401_VAL_L3_A1_MACHINE_FREEZE.json` is input role 10.  After the historical
temp-capture and publisher-implementation increments, a separately authorized
transaction published it once and role 24 independently postverified the
canonical inode.  Its SHA-256 is
`0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e`.
At the role-13 implementation/prepublication snapshot recorded by these
bytes, input role 13 is absent; its fixed-destination capture/publication
surface is implemented but has not been executed against the repository at
that snapshot.
Only after all 53 ordered input roles have their final bytes may
`R401_VAL_L3_A1_FREEZE.json` be created as downstream release role 54; it
contains no self-hash.  This pre-freeze design and its tracker are planning
inputs only; the later protocol must state explicitly whether it binds them.

### 4.2 Evaluators, schedulers, checkers, and release builder

```text
scripts/evaluate_r401_val_l3_a1_static_cell.py
validated/capd_r401_phase_branch_tube_mp_a1.cpp
validated/bin/capd_r401_phase_branch_tube_mp_a1
scripts/run_r401_val_l3_a1_all_slabs.py
scripts/check_r401_val_l3_a1_static_independent.py
scripts/check_r401_val_l3_a1_branch_independent.py
scripts/check_r401_val_l3_a1_composite_independent.py
scripts/replay_r401_val_l3_s0_through_a1_checkers.py
scripts/build_r401_val_l3_a1_release_provenance.py
```

A single scheduler may coordinate both component queues, but the archive
roots, cell namespaces, component summaries, component manifests, and
component checker results must remain separate.  The independent checkers
must not import the scheduler, the cell evaluator, one another, or the S0
producer modules.

### 4.3 Minimum focused tests

```text
tests/test_r401_val_l3_a1_static_scheduler.py
tests/test_r401_val_l3_a1_static_checker.py
tests/test_r401_val_l3_a1_branch_scheduler.py
tests/test_r401_val_l3_a1_branch_checker.py
tests/test_r401_val_l3_a1_composite_contract.py
tests/test_r401_val_l3_a1_adversarial_e2e.py
tests/test_r401_val_l3_a1_release_provenance.py
```

## 5. Prospective authoritative layout

```text
results/r401_val_l3_all_slabs/
├── run_config.json
├── static/
│   ├── cells/{128,256}/Sxxx/
│   │   ├── proof.json
│   │   ├── stdout.txt
│   │   ├── stderr.txt
│   │   └── record.json
│   ├── cell_manifests/{128,256}/Sxxx.json
│   ├── aggregate_summary.json
│   └── aggregate_manifest.json
├── branch/
│   ├── cells/{128,256}/Sxxx/
│   │   ├── stdout.txt
│   │   ├── stderr.txt
│   │   └── record.json
│   ├── cell_manifests/{128,256}/Sxxx.json
│   ├── aggregate_summary.json
│   └── aggregate_manifest.json
├── independent_static_checker.json
├── STATIC_POSTCHECK_STATUS.json
├── independent_branch_checker.json
├── BRANCH_POSTCHECK_STATUS.json
├── composite_summary.json
├── composite_manifest.json
├── independent_checker.json
├── POSTCHECK_STATUS.json
├── R401_VAL_L3_A1_REPORT.md
└── RELEASE_PROVENANCE.json
```

Operational telemetry and interrupted staging objects must live in the
same-filesystem sibling
`results/r401_val_l3_all_slabs.operational/`, never below the authoritative
result root.  Canonical hidden staging directories live only under that
sibling's `staging/static/` or `staging/branch/` directory and are atomically
renamed across sibling directories into a canonical cell path.  They may be
preserved for diagnosis but do not enter canonical scientific payloads.  The
formal checker rejects every hidden or extra path below the authoritative
result root.  Quarantine records and moves both the authoritative generation
and its paired operational sibling without mixing either with a new run.

## 6. Exact schema and authority contract

### 6.1 Common producer fields

Every committed producer record, cell manifest, component aggregate, and
composite producer object has an exact top-level schema including:

```text
schema_version
protocol_id
artifact_role
authority = PRODUCER_ONLY
scientific_licensing_enabled = false
matrix_id
freeze_sha256
run_config_sha256
milestone_status = null
theorem_status = null
final_status = null
claim_boundary
```

`matrix_id` is the SHA-256 digest of the canonical JSON encoding of the exact
ordered 102-record matrix, not a free-form label.  The producer and each
checker independently reconstruct that array from the accepted plan before
comparing the digest.

Unknown keys, duplicate keys, nonfinite JSON numbers, Boolean/integer aliases,
integral-float/integer aliases, normalized path aliases, symlinks, hard-link
aliases of published control objects, and overwritten write-once objects are
fatal provenance defects.

### 6.2 Prospective main-freeze and run-config schemas

The strict main-freeze schema has exactly one noncircular ordered input-role
array and includes exactly:

```text
schema_version = exact integer
protocol_id = R401-VAL-L3-A1
status = FROZEN_FOR_PRODUCTION
scientific_licensing_enabled = true
matrix + matrix_id
static evaluator/checker identities, budgets, workers, and status whitelist
branch source/binary/checker identities, budgets, workers, and status whitelist
composite checker and release-builder identities
scheduler policy and maximum inflight counts
machine requirements and machine-freeze hash
archive layout and failure policy
complete ordered 53-element input_roles array of {role,path,sha256}
claim boundary
```

It contains no outcome status and no self-hash.  Its input map must bind all
protocol/contract documents, final code and tests, the machine freeze, the S0
compatibility replay, the independent pre-freeze review, both accepted
upstream release chains, the A4.16 derivation, and the sealed S0 component and
composite controls.

The write-once `run_config.json` is downstream.  It contains the main-freeze
path and hash, the complete frozen input map, matrix and matrix digest,
component budgets, status tables, scheduler/worker values, evaluator
identities, machine-freeze hash, exact output filesystem, and null producer
authority.  Resume requires type-strict byte-equivalent binding; changing a
worker count is a new generation, not an operational toggle.

### 6.3 Static cell schema

The static `proof.json` additionally contains:

- exact cell identity and exact rational epsilon endpoints;
- exact root boxes and coordinate order;
- the four complete tree payloads in canonical tree order;
- exact parent--child geometry and terminal classifications;
- per-tree and cell totals for nodes, internal nodes, terminal leaves,
  unresolved leaves, and maximum depth;
- decisive Arb endpoints for the outer, angle, and landing gates;
- canonical content roots for every tree and for the complete proof; and
- the frozen Python, python-flint/Arb, evaluator, checker, L1-plan, and L1
  release-chain bindings.

No stored pass Boolean substitutes for the decisive interval endpoints.

### 6.4 Branch cell schema

The branch `record.json` binds:

- exact cell identity, accepted L1 primary-record identity, epsilon, root
  box, precision, and exact 12-string evaluator invocation;
- evaluator source, persistent binary, CAPD commit/flags, runtime-library,
  main-freeze, and run-config hashes;
- return code and the unique parsed evaluator status;
- stdout and stderr hashes and sizes;
- Taylor order, precision-dependent tolerance, phase-grid size, and exact
  threshold;
- exact 64-cell phase cover, the independently recomputable state boxes, and
  the archived maximum `r_minus^2` upper endpoint; and
- null producer authority fields and the local claim boundary.

The checker treats the printed `r_minus^2` as telemetry.  It reconstructs
`omega_minus` with its own Arb computation and recomputes the slow-radius
enclosure from the printed CAPD state endpoints interpreted as exact decimal
rationals.

### 6.5 Closed evaluator namespaces

The static evaluator ABI must admit only:

| status | return code | meaning |
|---|---:|---|
| `STATIC_CELL_CERTIFIED` | 0 | all four trees close with zero unresolved leaves |
| `STATIC_UNRESOLVED_DEPTH` | 2 | frozen depth cap reached |
| `STATIC_UNRESOLVED_NODE_BUDGET` | 2 | frozen node cap reached |
| `STATIC_INTERVAL_FAIL` | 3 | interval primitive or outward evaluation failed |
| `INVALID_STATIC_PROOF_CONTRACT` | 5 | malformed or contradictory proof state |

A failed static gate is `UNRESOLVED` unless a separate future protocol
defines and checks a constrained existence witness on `K=1` inside the slow
tube.  An interval box that merely permits a bad value does not prove such a
state exists and cannot receive a scientific-stop or violation status.

The branch evaluator ABI must admit only:

| status | return code | meaning |
|---|---:|---|
| `BRANCH_CELL_CERTIFIED` | 0 | the complete frozen phase cover lies strictly inside the branch tube |
| `BRANCH_TUBE_UNRESOLVED` | 2 | a phase enclosure does not decide the strict inequality |
| `BRANCH_FLOW_FAIL` | 3 | CAPD cannot construct the frozen complete-period enclosure |
| `BRANCH_TUBE_VIOLATION` | 4 | a phase box has a rigorous lower bound at or outside the tube radius |
| `INVALID_BRANCH_PROOF_CONTRACT` | 5 | malformed input, output, or internal contract conflict |

A timeout, signal, missing or repeated status, status/code mismatch, nonempty
stderr on a nominal pass, or malformed transcript is not splittable.  It is a
frozen resource/provenance failure and prevents promotion.  A `VIOLATION`
status may be emitted only from a lower-bound certificate; failure of an
upper-bound proof is merely `UNRESOLVED`.

Evaluator status and scheduler classification are distinct fields.  The
scheduler classification is one of:

```text
COMMITTED_EVALUATOR_RESULT
CELL_TIMEOUT
CELL_SIGNAL
CELL_OUTPUT_BUDGET_EXHAUSTED
MALFORMED_EVALUATOR_OUTPUT
PROVENANCE_INVALID
```

Only `COMMITTED_EVALUATOR_RESULT` may carry an evaluator status.  The other
classifications have `evaluator_status = null`, preserve every available
raw byte, and prevent component promotion.  A timeout or signal therefore
cannot be forged into an evaluator `UNRESOLVED` result.

### 6.6 Checker promotion values

All component and composite producers retain null authority.  The exact
frozen component checkers may assign the following component-only values:

```text
PASS_STATIC_PHASE_ANCHOR_ALL_SLABS
PASS_BRANCH_TUBE_ALL_SLABS
```

Only the composite checker may assign the local theorem value:

```text
PASS_LOCAL_PHASE_TUBE_ALL_SLABS
```

The component values appear only in `component_status`.  Component checker
objects retain

```text
milestone_status = null
theorem_status   = null
final_status     = null
```

The composite value requires both component passes on all 102 cells plus the
accepted A4.15 release binding.  A passing composite checker may set

```text
milestone_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
theorem_status   = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
final_status     = null
```

The exact authority table is:

| checker | `component_status` | milestone/theorem | final |
|---|---|---|---|
| static | `PASS_STATIC_PHASE_ANCHOR_ALL_SLABS` | `null` / `null` | `null` |
| branch | `PASS_BRANCH_TUBE_ALL_SLABS` | `null` / `null` | `null` |
| composite | `null` | `PASS_LOCAL_PHASE_TUBE_ALL_SLABS` / same | `null` |

On any incomplete or failed replay, `component_status`, milestone, and theorem
values are null; a near-pass or passing subset has no alternative status.

Each checker object has `authority = INDEPENDENT_CHECKER`.  Its frozen
capability is distinct from its result: component checkers retain
`scientific_licensing_enabled = false`, while only the composite checker may
set that field true after the formal freeze authorizes the exact local-theorem
namespace.  A failed or incomplete replay records an exact failure list.

Each component checker is followed by a distinct write-once component
postcheck: `STATIC_POSTCHECK_STATUS.json` and
`BRANCH_POSTCHECK_STATUS.json`.  The same frozen checker source may expose a
separate postcheck-only mode, but that mode must reopen the already published
checker object, rerun the complete archive binding, and refuse overwrite.  A
component postcheck cannot widen its component checker's status.  The final
composite checker is analogously followed by `POSTCHECK_STATUS.json`.

The release builder may reproduce and bind that declaration but cannot
create, widen, or rename it.

## 7. Independent scientific replay

### 7.1 Static checker

The no-import static checker independently reconstructs:

1. the exact 102-cell matrix and slab endpoints from the accepted plan;
2. the algebraic normal modes, Hamiltonian, `r_minus`, `D_plus`, `N_plus`,
   `omega_plus N_plus`, and angular rate;
3. every exact dyadic parent--child union and deterministic split choice;
4. every energy, tube, angle, and section classification;
5. all decisive extrema and content roots;
6. the exact inequality `18 * 0.69 < 4*pi` with directed pi bounds; and
7. the one-positive-crossing winding implication.

The checker requires zero unresolved leaves and exact domain/verdict agreement
between the 128- and 256-bit records for each slab.  It does not require
bitwise equality of Arb endpoints across precisions.

### 7.2 Branch checker

The no-import branch checker independently verifies:

1. the exact L1 primary box selected for each cell and the five-object L1
   release chain;
2. the unique input echo and the exact 64 closed phase intervals
   `[k/64,(k+1)/64]`, including endpoints, order, and no gaps;
3. the CAPD source, persistent binary, dependency, compiler, and runtime
   bindings;
4. every raw transcript hash, unique status, return code, stderr gate, and
   `SolutionCurve` domain declaration;
5. every state interval and the exact-rational replay of
   `(omega_minus Q_minus)^2 + P_minus^2 < 0.0016`; and
6. cell identities and pass verdicts at both precisions.

This arithmetic replay is not a second ODE integration.  Mathematical trust
in the flow enclosure comes from the frozen CAPD evaluator and machine chain;
the checker verifies that the archived enclosures imply the claimed tube
inequality.

### 7.3 Composite checker

The composite checker independently requires:

- exact 102-cell sets in both component archives and no extra records;
- passing, write-once component checker and postcheck objects;
- exact component aggregate roots and per-cell content hashes;
- the A4.16 derivation and the accepted S0 compatibility replay;
- the exact five-object L1 chain used for branch initial boxes;
- the exact five-object A4.15/L2-A1 chain consisting of release provenance,
  aggregate summary, aggregate manifest, independent checker, and postcheck;
- null final programme values throughout; and
- the unchanged conditional/global nonclaim language.

It must not import either component checker.  It reopens their public objects
and independently validates their exact schemas and hash bindings.

### 7.4 Exact S0 compatibility object

`R401_VAL_L3_A1_S0_COMPATIBILITY_REPLAY.json` is a closed-schema, read-only
replay of the sealed S0 archive.  Its construction must not invoke either
evaluator and must not modify an S0 byte.  It binds the exact S0 matrix

```text
{S000, S025, S050} x {128, 256}
```

and requires these exact public facts:

```text
static proof count             6
static nodes                   84172
static internal nodes          42074
static terminal nodes          42098
static unresolved nodes        0
static independent checks      122300
static maximum depth           14
branch raw replay count        6
branch manifest file count     26
composite cell count           6
composite binding count        18
composite failures             0
```

The exact nine component/control hashes are:

| role | sealed S0 SHA-256 |
|---|---|
| static summary | `e55c5280dcda615dcc672e58694a5639177fd0777595ff03eca163014c1bc225` |
| static manifest | `f37b11967aab879e369080d3440d932c706bfe662734065077a51cfb1f5bb2ce` |
| static checker | `4be68b9369714cba1979b03bcb08bc9dd40a4de8a02732b90fb87b39b422a262` |
| branch summary | `a8853e4eb308cd44ad8413cbbd45da29240c113df15ea4ff3472bc740d3b089a` |
| branch manifest | `edfa8a2a8e82e14e95828173da3b30c6a8820ef9950d5f31125bddc9c76231bc` |
| branch checker | `162ebcc992054945deb48c84fa9b47bff970e9865cb629633049b986e3986753` |
| composite summary | `ab0d7921623a5d4ba61d148ce833d22e14da75c77385897c328b20e41d64257f` |
| composite manifest | `75c1533196c6c4df96bf21c09ecae3230423924323709652c259cbcd1d67cb05` |
| composite checker | `197a087ecc75c95f186764f5365d3fc6769cb4cfe99793bfc1abc61afc037470` |

The compatibility checker also requires the exact six static proof entries,
the branch manifest's exact 26-role set, the composite manifest's exact role
set, the component-only status ownership, and null milestone/theorem/final
values inherited from S0.  A matching digest with a changed role, count,
status, or schema is rejected.  The resulting compatibility object has null
scientific authority and is itself rebound by the main freeze.

The implemented artifact schema remains closed at exactly 18 top-level keys:
the fields listed in the checker contract, with
`artifact_role=S0_TO_A1_COMPATIBILITY_REPLAY`,
`artifact_status=NON_LICENSING`,
`replay_status=PASS_S0_COMPATIBILITY_REPLAY`, empty failures, and null
milestone/theorem/final statuses.  Capture and publication add no receipt,
self-hash, or authority field to that artifact.

Role 23 now implements two exact-exclusive non-dispatch modes:

```text
--capture-s0-compatibility --output /tmp/EXACT_NEW_CANDIDATE.json
```

or

```text
--publish-s0-compatibility \
--candidate /tmp/EXACT_CANDIDATE.json \
--expected-sha256 EXACT_64_LOWERHEX \
--authority-root EXACT_LIVE_PAPER02_ROOT
```

Capture creates a new one-link `0600` candidate.  Publication accepts no
destination override and derives the fixed role-13 path.  It caps the
candidate at `1048576` bytes, requires exact compact bytes and live replay
equality, and terminally reopens the adapter, this design, the checker
contract, and the release contract.  Those four source bindings must be
stable before fresh candidate capture.

Publication uses an explicit-`0644` same-parent stage and only
`renameat2(RENAME_NOREPLACE)`.  Every existing canonical entry is fatal,
including identical bytes.  After rename, no failure permits rollback,
deletion, repair, overwrite, or idempotent republish.  Its transient exact
21-key receipt is limited to `ROLE23_ADAPTER_PUBLICATION_ONLY`, with
`independent_verification_performed=false`, licensing/production/dispatch
false, and component/milestone/theorem/final null.  At this explicit
implementation/prepublication snapshot, the publisher has not been executed
and canonical role 13 is absent.

## 8. Transaction, resume, and crash recovery

Each component cell is committed with a same-filesystem transaction.  The
only permitted staging namespace is

```text
operational/staging/{static,branch}/{128,256}/
  .{slab_id}.tmp-{generation_prefix_16hex}-{attempt_decimal}
```

Here `slab_id` is exactly `S000` through `S050`, the generation prefix is
derived from the sealed run-config hash, and the attempt is an exact
nonnegative decimal integer.  The scheduler rejects every other hidden name,
requires staging and authoritative parents to have the same `st_dev`, and
allows only one active staging owner for a cell.  No hidden staging directory
is permitted inside an authoritative component namespace.

The transaction is:

1. create a producer-canonical hidden staging directory;
2. write raw/proof objects and `record.json` with exclusive creation;
3. flush every file;
4. flush the staging directory;
5. atomically rename it to the canonical cell directory;
6. flush both the staging parent and canonical parent;
7. write the separate cell manifest last as the commit marker.

Evaluator output is drained continuously into capped staging files; the
scheduler must not use an unbounded in-memory `capture_output`.  Reaching a
frozen stdout, stderr, proof, record, or total-cell byte cap terminates the
complete process group and commits
`CELL_OUTPUT_BUDGET_EXHAUSTED` with the captured prefix, exact captured-byte
count, cap, and `truncated = true`.  Such a record is non-passing.  This
per-cell rule protects the filesystem between barrier-level disk checks.

Component aggregate summaries are committed before their aggregate
manifests.  Composite summary, manifest, checker, postcheck, report, and
release are also write-once objects in that order.  No object contains its
own hash.

Resume reconstructs its frontier from validated cell manifests, not from a
mutable scheduler-state counter.  A hidden interrupted staging directory is
non-authoritative and may be retained for inspection; its task may be rerun.
A committed non-pass cell is authoritative and may not be silently retried
under the same freeze.  Corruption of a committed cell, any run-config
mismatch, or any frozen-input mismatch invalidates the generation.

A crash may occur after the canonical cell-directory rename but before its
separate manifest commit.  On resume, that manifest-less directory is never
counted as a committed pass.  The scheduler may complete the manifest only
after revalidating every canonical byte against the frozen task and deriving
the unique expected manifest without modifying the directory.  If that exact
recovery is impossible, the complete generation is quarantined; the cell is
not overwritten or mixed with a rerun.

An explicit quarantine operation moves the complete generation to a
recoverable sibling path before a fresh generation starts.  Static objects,
branch objects, and checker objects from different generations may never be
mixed.  Quarantine never deletes scientific data.

For a scheduler crash or operator termination before a cell commit, resume
may rerun the exact cell.  A frozen per-cell timeout is different: the
scheduler terminates the complete evaluator process group, archives the
timeout as a non-pass resource outcome, and does not retry it automatically.

## 9. Provenance DAG

The mandatory graph is acyclic and has the following order.

```text
accepted L1 five-object release chain
accepted A4.15 five-object release chain
A4.16 derivation + sealed S0 protocol/report/components/composite
exact L1 plan + CAPD dependency lock
                 |
                 v
final L3-A1 protocol/scheduler/checker/release contracts
final evaluators/scheduler/checkers/release builder/tests
                 |
                 +--> stable live on-disk role-19 source bytes
                 |          |
                 |          v
                 |    temp candidate + role-24 preverification
                 |          |
                 |          v
                 +--> role-10 machine freeze + role-24 postverification
                 +--> exact S0-to-A1 compatibility replay
                 +--> pre-freeze test record
                              |
                              v
independent pre-freeze review: exact `Verdict: ACCEPT_FOR_FREEZE`
                              |
                              v
role-54 main L3-A1 freeze, generated after all 53 inputs; no self-hash
                              |
                              v
sealed run_config binding the main-freeze hash and complete input map
                 /------------+------------\
                v                          v
      102 static cell commits     102 branch cell commits
                |                          |
                v                          v
   static aggregate manifest     branch aggregate manifest
                |                          |
                v                          v
 independent static checker   independent branch checker
                |                          |
                v                          v
       static postcheck              branch postcheck
                 \------------+------------/
                              v
           composite summary and manifest
                              v
              independent composite checker
                              v
       composite postcheck + exact-boundary report
                              v
       write-once release provenance; no self-hash
```

Every semantic parse and digest at the freeze and release edges must operate
on the same captured bytes.  Original lexical paths are checked for symlink
components before resolution.  Publication must link or rename a pinned open
inode and then verify the published inode and exact bytes, following the
accepted L2-A1 release discipline.

The numbered 53-role array is an authority order, not the construction
topology shown above.  Role 10 binds the stable current live on-disk role-19
capture/publisher source hash,
but role 19 contains no role-10 hash, so no cycle is present.  After role 10
is published, roles 10 and 19 are immutable; final role 24 performs the
canonical read-only replay and then also remains immutable.  The main freeze
is not “last among” those inputs: it is external downstream role 54 and
follows all 53 final input bytes.

## 10. Candidate scientific and operational budgets

These values are candidates only.  They may be frozen once, before any
held-out L3 dispatch, using only accepted S0 resource evidence and mock runs.

### 10.1 Static candidates

```text
maximum depth per tree              24
maximum nodes per tree              250000
maximum nodes per cell              1000000
cell timeout                        1800 seconds
workers                             8
maximum authoritative cell bytes   512 MiB
```

The current S0 engine interprets its node cap per tree.  The formal protocol
must remove this ambiguity by freezing both per-tree and aggregate per-cell
limits.  Any depth, node, byte, or timeout cap is an inconclusive result, not
a negative theorem.

### 10.2 Branch candidates

```text
phase cells                         64
Taylor order                        24
absolute/relative tolerance at 128  1e-30
absolute/relative tolerance at 256  1e-60
cell timeout                        600 seconds
workers                             6
maximum stdout per cell             16 MiB
maximum stderr per cell             1 MiB
maximum record per cell             4 MiB
maximum total branch cell bytes     32 MiB
```

The precision-dependent tolerance is the behavior of the sealed S0 C++
source.  A future formal protocol must state it exactly rather than repeat the
S0 draft's abbreviated single-tolerance bullet.

### 10.3 Host and storage candidates

The audit observed 32 logical CPUs, a 60-GiB cgroup memory limit, and about
347 GiB free on `/root/autodl-tmp`.  These are observations, not a machine
freeze.  Candidate admission gates are:

```text
minimum launch free storage    200 GiB
operator warning below         180 GiB
pause new admission below      150 GiB
inventory/recovery only below  120 GiB
pause new admission at memory  48 GiB cgroup current usage
global scientific budget       null
```

Static and branch stages should run sequentially, not with both worker pools
active.  The branch worker count cannot be finally frozen above the six-way
S0 configuration until representative peak-RSS telemetry is collected.  A
pre-freeze resource gate must prove

```text
baseline memory + workers * representative peak RSS + reserve <= 48 GiB.
```

The candidate reserve is 8 GiB.  The formal machine freeze must capture the
idle baseline and the measurement method; until that calculation passes, the
worker values remain planning numbers.

Operational disk or memory pauses occur after the current deterministic
barrier and leave a resumable incomplete generation.  They cannot assign a
scientific status.  There is no global scientific wall-clock budget.

## 11. Required test matrix

| Gate | Required tests | Pass condition |
|---|---|---|
| exact matrix | missing, extra, duplicate, reordered, wrong-precision, and wrong-slab cells | only the canonical 102 identities pass |
| static science | outer, angle, landing, split, boundary, extrema, and unresolved mutations | checker independently rejects every mutation |
| branch science | phase gap/overlap, state endpoint, input echo, status, margin, binary, and CAPD mutations | checker independently rejects every mutation |
| strict data | duplicate keys, NaN/Infinity/overflow, Boolean/integer and float/integer aliases | fail closed before authority evaluation |
| path safety | traversal, absolute aliases, backslashes, hidden extras, leaf/parent symlinks, hard-link aliases | no authoritative alias is accepted |
| transaction | crash before each file flush, before/after directory rename, and before/after manifest commit | resume either reruns an uncommitted cell or validates a complete one |
| quarantine | run-config, source, binary, matrix, threshold, or worker mismatch | whole generation moves recoverably; no mixing |
| concurrency | randomized completion delay, worker race, duplicate admission, budget-edge race | canonical scientific bytes are invariant |
| process control | timeout, SIGTERM, SIGKILL escalation, descendant process, missing status | no orphan; non-pass classification is exact |
| resource pause | memory and disk thresholds at barrier boundaries | admission pauses without scientific failure |
| compatibility | all six accepted S0 cells replayed through prospective schema adapters | exact S0 facts and null final value preserved |
| compatibility capture/publication | exact mode XOR, new `0600` `/tmp` candidate, 1-MiB cap, four live source bindings, fixed destination, namespace/candidate/stage TOCTOU, explicit `0644`, `renameat2(RENAME_NOREPLACE)`, identical-existing refusal, crash residue, and post-rename ambiguity | implementation fixtures only; the prepublication snapshot has no canonical role 13 and invokes no evaluator |
| machine capture/verify | temp-path exclusivity, fresh-build staging, no-overwrite persistent binding, compiler-subobject mutations, path/link/TOCTOU attacks, and read-only independent replay | only one compact temporary candidate passes; no role-10 publication or evaluator dispatch |
| machine publication | fixed role-10 destination, expected-hash pin, `1..1048576` pre-open type/size cap, stale role-19 binding, candidate/namespace TOCTOU, same-parent staging, explicit mode, `renameat2(RENAME_NOREPLACE)`, identical-existing refusal, crash residue, post-rename ambiguity, source preservation, and exact receipt | historical implementation fixtures passed first; the later authorized canonical role 10 was published once and separately replayed by role 24 |
| synthetic E2E | mocked 102-cell static and 102-cell branch archives through composite and release | exact DAG closes with no evaluator dispatch |
| release | write-once, verify-only, same-byte snapshot, TOCTOU, self-hash, extra role, altered report status | only one exact acyclic release is accepted |

The focused test record must list commands, counts, durations, source hashes,
and a clean post-test hash audit.  Synthetic pass fixtures must be visibly
marked and cannot be placed in the production result directory.

## 12. Launch gates

All gates below must close before the first evaluator dispatch for any of the
48 L3 slabs not present in S0.

1. **Mathematical freeze candidate:** final A4.16 derivation review and exact
   formal protocol, including the conditional tube-residence premise.
2. **Implementation freeze candidate:** final cell evaluators, transactional
   scheduler, three no-import checkers, S0 adapter, release builder, and all
   focused tests.
3. **Persistent environment and role 10:** completed by the canonical
   machine-admission object with SHA-256
   `0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e`
   and the separate role-24 canonical replay; this completion grants no
   scientific authority.
4. **Non-held-out validation and role 13:** complete mocked 102-cell
   end-to-end run and adversarial fault suite; stabilize all four compatibility
   source bindings, capture a fresh `0600` candidate, and only under separate
   authorization publish the exact compatibility bytes once at role 13.  At
   this prepublication snapshot the publisher is implemented and canonical
   role 13 is absent.
5. **Resource admission:** representative-only memory calibration, candidate
   worker validation, and live disk/memory headroom.  This gate requires a
   separate instruction before running even representative evaluators.
6. **Independent review:** a reviewer who did not author the final producer
   or checker issues the sole exact verdict `Verdict: ACCEPT_FOR_FREEZE`.
7. **Main freeze:** generated as role 54 only after all 53 ordered input roles,
   including canonical machine role 10, are final, strict-parsed, and
   hash-audited in a clean repository state.
8. **Initialize only:** the scheduler creates and independently verifies the
   sealed run configuration without dispatching an evaluator.
9. **Explicit production authorization:** only a later, explicit instruction
   may start the held-out/all-slab generation.

Failure of any gate leaves `dispatch_authorized = false`.  A nominal source
file named `FREEZE` or a producer self-declaration cannot bypass the
independent review and exact main-freeze handshake.

## 13. Blocking issues before freeze construction

| ID | Blocker | Required resolution |
|---|---|---|
| B1 | S0 static runner is fixed to six cells and lacks formal run-config, resume, quarantine, and write-once publication | extract a one-cell evaluator and implement the production scheduler transaction |
| B2 | static proof/summary contains wall time and can be overwritten | remove telemetry from canonical payloads and enforce exclusive/write-once commits |
| B3 | S0 branch runner compiles inside the result directory and writes concurrently without durable transactions | persistent pre-freeze binary plus cell transactions and process-group control |
| B4 | both S0 checkers hard-code the representative matrix | new independent 102-cell checkers and strict aggregate schemas |
| B5 | no L3 S0-to-A1 semantic compatibility adapter exists | implement and independently validate exact six-cell replay |
| B6 | static node cap is per tree but no per-cell cap is stated | freeze both meanings and test boundary races |
| B7 | no representative CAPD peak-RSS record exists | collect resource-only S0 telemetry before freezing branch workers; no held-out cell |
| B8 | old L2 machine freeze omits the L3 static/Arb and branch binary chain | construct a new L3 machine freeze from live exact bytes |
| B9 | S0 branch failure vocabulary conflates non-certification and possible violation | implement the closed production status/code table and lower-bound-only violation rule |
| B10 | existing L3 schemas do not bind the accepted A4.15 five-object chain | add it to main freeze, composite checker, and release roles |
| B11 | no L3 transaction, fault, full-matrix mock, or release test suite exists | close the complete test matrix in section 11 |
| B12 | no independent L3-A1 pre-freeze review or main freeze exists | obtain review only after final bytes and tests are stable |

These are construction blockers, not evidence that the mathematical route is
false.  They forbid production dispatch in the current repository state.

## 14. Reuse versus rewrite ledger

| Existing asset | Decision | Reason |
|---|---|---|
| S0 static algebra/model/tree core | extract and reuse after byte-level review | already independently replayed on representative cells |
| S0 static matrix/output/main | rewrite | fixed S0 authority, non-resumable, telemetry in canonical objects |
| S0 static independent math replay | extract and extend | scientific logic is valuable; matrix/DAG/status are S0-specific |
| S0 branch vector field and `SolutionCurve` loop | reuse in new formal C++ source | validated representative numerical mechanism |
| S0 branch compile/run/archive layer | rewrite | runtime build, direct writes, no formal handshake |
| S0 branch transcript arithmetic replay | extend | retain exact-rational margin check; add formal matrix/DAG/phase/status gates |
| S0 composite packager/checker | use as schema reference, not production code | six-cell and non-licensing status are hard-coded |
| L2-A1 transaction/run-config/quarantine/path code | adapt or factor with tests | accepted production architecture matches the operational problem |
| L2-A1 geometric evaluator/checker | do not reuse | it proves a different reduced-root exclusion statement |
| L2-A1 release builder and adversarial patterns | adapt | strong same-byte, write-once, TOCTOU, and status-boundary discipline |
| L2-A1 machine freeze | use as template only | L3 dependencies and evaluator binaries differ |

## 15. Pre-freeze decision

The design is sufficiently concrete to begin implementation of the formal
cell evaluators, scheduler, checkers, compatibility replay, and tests.  It is
not ready for construction of the main freeze because blockers B1--B12 are
open.

Current exact decision:

```text
internal_design_audit_complete = true
independent_design_review_complete = true
formal_protocol_exists = true
formal_machine_freeze_exists = true
formal_machine_freeze_sha256 = 0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e
formal_machine_freeze_role24_postverify = PASS_MACHINE_FREEZE_VERIFY_ONLY
s0_compatibility_capture_implemented = true
s0_compatibility_publisher_implemented = true
s0_compatibility_adapter_sha256 = a00117303874eec16c7d116f344179c1e586856046cb725efb92c7b8c22640b0
s0_compatibility_test_sha256 = f93832a2de731bad2972a08534adf5c8001c84805e57f01c5970a810bae2e95d
s0_compatibility_focused_tests = 72/72
canonical_s0_compatibility_role13_exists_at_prepublication_snapshot = false
independent_prefreeze_accept = false
main_freeze_exists = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```

The next safe implementation step is to build and mock-test the static
one-cell transaction and its no-import production checker, followed by the
persistent CAPD branch transaction.  Held-out/all-slab evaluator execution
remains explicitly prohibited.

## 16. Implemented exact-schema increment and remaining freeze blockers

The control plane now has independent closed validators for the exact machine,
main-freeze, and final-shaped run-config schemas; a pinned ordered 53-role
capture/replay handshake; temp-only machine capture plus producer-independent
verify-only replay; write-once noncanonical initialization; pure formal static
and branch transaction plans; exact static four-file packaging; and a
102-certified-only aggregate builder.  Formal initialization produces only
`run_config.json`, cannot resume or be upgraded in place, and the execution
mode remains an unconditional rejection.

The machine freeze stores the original static compact and branch pretty
resource-calibration images as raw UTF-8 strings plus hashes.  Those images
are strict-parsed and replayed without reopening historical `/tmp` proof,
stdout, or stderr paths.  Current evaluator, interpreter, plan, module,
`RECORD`, binary, and library bindings are live-opened and terminally
replayed.  The machine receipt separately binds the Python/Arb and CAPD chains,
the declarative build recipe, private fresh-rebuild receipt with
`shell_used=false`, no-overwrite transfer evidence, exact
cwd/environment/umask/argv/stdout/stderr, ELF and `DT_NEEDED`, separated
Python-bundled and CAPD-system runtime libraries, filesystem identities, and
the conservative resource inequalities.  `production_authorized` remains
false.
The Python Conda-package live root, raw python-flint `RECORD` hash, and
python-flint installed-file root are pairwise-distinct exact fields.  The
Conda root is recomputed from its unique Python 3.12.3 metadata record and a
terminal replay of every declared file/link.  CAPD validation independently
proves that the checksum-covered v2 index reconstructs the detached HEAD tree
OID, then derives a separate live tracked-row SHA-256 root under
`GIT_INDEX_LIVE_TREE_CJ_COMPACT_V1`.  The persistent ELF build-id and dynamic
`DT_NEEDED` entries are parsed directly from the pinned binary rather than
trusted from an external inspection command.  Frozen runtime-library rows are
then live-opened and checked for exact bytes, build-id, and SONAME; they are
not presented as a parser-derived transitive closure.  The python-flint module, `RECORD`, Arb, and
fmpq images are confined to one exact site-packages layout.

The branch formal runtime and independent checker now share exact integer
millisecond budgets (`600000`, `2000`, `1000`), so the migration gate is true.
The production/scientific dispatch gate remains unconditionally closed.

The role-19 capture surface owns and removes its fresh-build `/tmp` staging.
The role-24 verifier performs no write and spawns no subprocess; any second
fresh rebuild belongs to a future role-11 pre-freeze test, not to verify-only.
The temporary capture/verify surface writes no canonical role-10 path, no main
freeze, and no result.  A successful verify-only line is non-authoritative and
cannot promote the candidate.

Role 19 now also implements a separate exact-exclusive publisher.  It accepts
one temporary candidate and expected digest but no destination override,
derives the fixed role-10 path, uses an explicit-`0644` same-parent staging
inode and `renameat2(RENAME_NOREPLACE)`, and refuses every pre-existing
canonical entry, including identical bytes.  Its success remains
`PUBLISHED_WRITE_ONCE_PENDING_INDEPENDENT_VERIFY`; role 24 must be invoked
separately after publication.  Role 19 does not call role 24 or an evaluator.
The publisher has not been executed in the repository, so role 10 remains
absent.

The remaining smallest blockers are now explicit:

1. after final publisher bytes are stable, capture a fresh role-19-bound
   candidate, verify it through role 24, and under separate authorization
   publish the expected byte image once as canonical input role 10; then run
   role 24 separately on the canonical path; the current increment implements
   but does not execute this operation;
2. complete the remaining canonical inputs, freeze final code/test/document
   hashes, and obtain the sole strict-ASCII independent pre-freeze ACCEPT
   review; only after all 53 inputs are final may role 54 be constructed; and
3. independently validate the initialized run binding before any separate
   decision about execution authority.

None of these steps licenses a scientific evaluator.  No canonical machine
freeze, main freeze, result archive, or release is created by this design
increment.

## 17. Subsequent canonical role-10 amendment

The absence and unexecuted-publisher statements above describe the historical
design and implementation boundaries at which they were recorded.  They are
superseded for the current repository state by the following later, separately
authorized event:

```text
canonical_machine_role10_exists = true
canonical_machine_role10_path = research/route_a_wave_trace/R401_VAL_L3_A1_MACHINE_FREEZE.json
canonical_machine_role10_sha256 = 0d5c46726ee8142e0e53f97c904213dfc9b795ac300b423277bc27a711f5c21e
canonical_machine_role10_size_bytes = 54526
canonical_machine_role10_mode = 0644
canonical_machine_role10_nlink = 1
canonical_machine_role10_publication_commit = 5086e33c7c66f33785338e90b340347e086d9941
canonical_machine_role10_role19_sha256 = 262985fcb1fc82890501b635bfce163712f1821e2d92276aee9f363ee0473a82
canonical_machine_role10_role24_postverify = PASS_MACHINE_FREEZE_VERIFY_ONLY
main_freeze_role54_exists = false
independent_prefreeze_accept = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```

The role-24 replay was zero-write, zero-subprocess, and explicitly
`NON_AUTHORITATIVE_VERIFY_ONLY`; it granted no promotion or dispatch
authority.  At this role-10-only amendment snapshot, the next bounded inputs
were the canonical role-13 compatibility replay and role-11 pre-freeze test
receipt, followed by the independent role-12 review.  Role 54 remains last
and cannot be constructed until all 53 inputs are final.

## 18. Role-13 implementation/prepublication snapshot

The role-23 capture/publication implementation described in section 7.4 is
now stable as an engineering surface.  Its adapter SHA-256 is
`a00117303874eec16c7d116f344179c1e586856046cb725efb92c7b8c22640b0`;
the focused test SHA-256 is
`f93832a2de731bad2972a08534adf5c8001c84805e57f01c5970a810bae2e95d`.
The final focused replay passed `72/72` in `1.42 s`; Python compilation and
the implementation-owner diff check passed.  Those are non-dispatching
implementation results, not a role-13 receipt or scientific verdict.

The complete transaction and exact 18-key artifact / 21-key receipt boundaries
are recorded in
[`A416_L3_A1_S0_COMPATIBILITY_PUBLICATION_INCREMENT.md`](A416_L3_A1_S0_COMPATIBILITY_PUBLICATION_INCREMENT.md).
At this explicit prepublication snapshot, the implementation has not executed
the publisher against the repository and canonical role 13 is absent.  A
future publication receipt's independent-verification field remains false;
role 54 and every scientific status are also absent or null at this snapshot.

Because a future compatibility object binds this design, the checker
contract, the release contract, and the adapter itself, those four roles must
now remain stable until a fresh candidate is captured and either rejected or
separately authorized for the one-shot fixed-destination publication edge.

These design bytes are themselves one of the four role-13 source bindings.
After a candidate is captured and especially after any successful
publication, this bound document is intentionally frozen and must not be
edited merely to restate later repository presence.  Postpublication current
state belongs in the unbound compatibility-publication increment and tracker,
and in the later role-11 pre-freeze test record.  No future role-13 candidate
SHA-256 or publication commit belongs in this source-bound document.
