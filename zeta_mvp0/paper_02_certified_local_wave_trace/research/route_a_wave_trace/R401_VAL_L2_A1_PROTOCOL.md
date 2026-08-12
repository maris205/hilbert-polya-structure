# R401-VAL-L2-A1 all-slab local-complement protocol

Protocol ID: `R401-VAL-L2-A1`  
Protocol version: 1  
Status: **formal protocol candidate; non-authorizing until the separate machine-readable freeze and independent pre-freeze review are sealed**.  
Prepared: 2026-08-07 UTC.

## 1. Purpose and licensed mathematical target

This protocol prospectively extends the accepted six-tree
`R401-VAL-L2-S0` implementation smoke to every parameter slab accepted by
the frozen L1 branch certificate.  It licenses exactly the following target.

Let

\[
B_{\rm loc}=[-0.02,0.02]\times[0.12,0.17]\times[-0.08,0.08]
             \times[0.64,0.69]
\]

in the ordered reduced coordinates

```text
q_slow, q_fast, p_slow, period.
```

For slab `Sxxx`, let \(E_j\) be its exact closed epsilon interval and let
\(P_j\) be the exact protected L1 plan box.  The prospective result is

\[
\forall j\in\{0,\ldots,50\},\quad
\forall\epsilon\in E_j:\qquad
Z(F_\epsilon)\cap B_{\rm loc}=\{x_j(\epsilon)\}.
\]

Here existence and uniqueness inside \(P_j\) come only from the already
accepted L1 release.  L2-A1 may contribute only the exclusion

\[
Z(F_\epsilon)\cap
\bigl(B_{\rm loc}\setminus\operatorname{int}P_j\bigr)=\varnothing.
\]

The complete target matrix is the exact canonical order

```text
128 bits: S000, S001, ..., S050
256 bits: S000, S001, ..., S050
```

and therefore contains exactly 102 trees.  A strict subset cannot receive
the all-slab milestone.

## 2. Explicit nonclaims

Even a completely passing archive is confined to the frozen reduced
\(P_+=0\) local chart and the exact parameter interval covered by the 51 L1
slabs.  It does not establish any of the following:

- a phase/flow-box cover of a full periodic orbit;
- uniqueness on the full energy shell or in global phase space;
- a global parameter continuation theorem outside the frozen slabs;
- primitive period or exclusion of every shorter return;
- an event-projected determinant or a new quantitative
  \(\delta_{\rm tr}>0.01\) bound;
- a prime trace, Riemann-zero reconstruction, a Hilbert--Polya operator,
  the Riemann hypothesis, or any implication toward RH.

These nonclaims apply to abstracts, figures, README files, certificates,
release notes, and manuscripts as well as to machine-readable statuses.

## 3. Frozen geometric decomposition

For each protected box \(P_j\), the scheduler constructs the eight exact
closed coordinate shells in the fixed coordinate order.  At coordinate
\(k\), the lower and upper shells use the current outer prefix in coordinates
\(0,\ldots,k-1\), the lower or upper part outside \(P_j\) in coordinate
\(k\), and the full local box in later coordinates.  Their union is exactly

\[
B_{\rm loc}\setminus\operatorname{int}P_j.
\]

Every nonterminal node is bisected at its exact rational midpoint.  The
split coordinate maximizes width divided by the corresponding full width of
\(B_{\rm loc}\); ties are resolved by the coordinate order
`q_slow, q_fast, p_slow, period`.  Children are named by appending `0` and
`1`.  Parent and child boxes must be reconstructed independently by the
checker using exact rational arithmetic.

## 4. Node evaluator and closed result namespace

Each task launches one separate evaluator process.  No process shares CAPD
or MPFR rounding state with another process.  The exact invocation contains
12 strings:

1. the frozen absolute evaluator path;
2. precision bits;
3. epsilon lower endpoint;
4. epsilon upper endpoint;
5. eight box endpoints in the frozen coordinate order.

The only recognized `(status, return code, action)` values are:

| evaluator status | return code | scheduler action |
|---|---:|---|
| `ENERGY_EXCLUDED` | 0 | terminal exclusion |
| `RETURN_EXCLUDED` | 0 | terminal exclusion |
| `UNKNOWN` | 2 | split below the depth limit |
| `ENERGY_DERIVATIVE_FAIL` | 3 | split below the depth limit |
| `ENERGY_GUARD_FAIL` | 3 | split below the depth limit |
| `FLOW_FAIL` | 3 | split below the depth limit |
| `ROOT_CANDIDATE` | 4 | hard scientific stop, non-pass |
| `INVALID_EXCLUSION_UNIQUENESS_CONFLICT` | 5 | hard invalid stop |

A timeout, signal, missing or repeated status, malformed transcript,
non-whitelisted pair, or boolean return code is invalid and never splittable.
Depth or node exhaustion is inconclusive, not exclusion.

The independent checker must replay, from every transcript and using exact
rational arithmetic where applicable:

- every energy interval-Newton contraction and guard;
- `F_mean` and `C F_mean` enclosures;
- the Krawczyk image;
- each selected direct, mean, or preconditioned separation component;
- the strict logical margin;
- the exclusion/uniqueness-conflict flag;
- the complete shell cover and split DAG.

This replay is independent algebra over archived proof objects.  It is not a
second numerical integration and must not be described as one.

## 5. Scientific budgets and scheduler contract

The machine-readable freeze must bind exactly:

```text
max_depth per tree            = 48
max evaluated nodes per tree  = 20000
workers                       = 24
max_inflight_per_tree         = 1
node timeout                  = 7200 seconds
global scientific budget      = null
scheduler policy              = deterministic_round_robin_barrier_batches_v1
```

The scheduler admits at most one task from any tree into one barrier batch.
It commits completed tasks in canonical `(precision, slab, depth, node_id)`
order, independently of worker completion time.  No global node count,
wall-clock limit, disk watermark, operator stop, or dispatch limit may turn a
scientific pass into a failure or vice versa.  An operational interruption
leaves a resumable, scientifically incomplete generation.

The resource values above were selected before inspecting any held-out A1
outcome.  They are supported by the accepted S0 archive: 3,016 nodes, maximum
depth 36, largest tree 574 nodes, and 28.605 evaluator node-hours.  The
linear 102-tree estimate is about 486 node-hours; this estimate is not an
acceptance rule.

## 6. Machine and storage admission

Production is local to the frozen host/container environment.  The separate
file `R401_VAL_L2_A1_MACHINE_FREEZE.json` binds the effective cgroup limits,
compiler and Python identities, persistent CAPD checkout/build, evaluator
binary, runtime libraries, filesystem, and ordered build flags.

The formal launch requires at least 100 GiB free on the filesystem holding
the result generation.  The operational watermarks are:

```text
>= 220 GiB free : GREEN
<  200 GiB free : operator warning
<  150 GiB free : pause new admission after the current barrier
<  120 GiB free : remain incomplete; inventory and recovery only
```

A storage pause is operational only.  It cannot set a milestone, theorem, or
final scientific status.  The result directory, node staging directories,
and atomic commit targets must reside on one filesystem.

## 7. Transaction, resume, and quarantine rules

Every evaluated node is one same-filesystem directory transaction containing
`stdout.txt`, `stderr.txt`, `telemetry.json`, and `record.json`.  Files and
directories are flushed before the hidden staging directory is atomically
renamed.  A producer-canonical hidden interrupted node staging directory, or
producer-canonical hidden tree/tree-manifest staging file left before its
atomic rename, is non-authoritative; every other hidden path is rejected.

The record binds the exact task, invocation, run config, source and binary
hashes, raw hashes, return code, and classification.  A tree file is written
before its tree-manifest commit marker.  The aggregate summary is written
before its aggregate manifest.  Canonical proof objects exclude elapsed
time and completion order.

Resume is permitted only when the complete run binding is byte-for-byte
identical to the sealed run config.  A mismatch cannot be repaired in place.
With an explicit quarantine operation, the entire old generation is moved to
a recoverable sibling quarantine directory and a fresh generation begins
from all eight shells; node records from different generations may never be
mixed.  No quarantine operation deletes scientific data.

## 8. Freeze and provenance DAG

The machine-readable main freeze is generated last among its inputs and does
not contain its own hash.  It binds at least:

- this protocol;
- the formal producer and independent checker;
- evaluator source and frozen evaluator binary;
- CAPD dependency lock and machine freeze;
- exact L1 final plan;
- upstream L1 release provenance, summary, manifest, checker, and postcheck;
- the independent pre-freeze review;
- the S0 compatibility replay, schema adapter, release builder, and final
  release-provenance contract;
- exact matrix, limits, scheduler, thresholds, status whitelist, archive
  layout, failure policy, and claim boundary.

The S0 replay is additionally checked as a closed semantic object by both
producer and independent checker: six ordered public trees, 3,016 nodes,
6,055 manifest-hash checks, and exact status totals 183 energy-excluded,
1,349 return-excluded, and 1,484 split/unknown, with current checker/adapter
and actual S0 release/manifest/postcheck hashes.

The downstream sealed `run_config.json` records the main freeze hash.  Node
records bind the run config; tree manifests bind the tree and all node/raw
hashes; the aggregate manifest binds the ordered 102 tree manifests.  The
independent checker binds that archive generation.  A final release
provenance object, generated only after the checker and certificate, binds
all prior objects and contains no self-hash.

All formal JSON uses type-strict comparison: a JSON boolean or integral float
cannot stand in for an integer schema version, resource count, limit, or
precision bit.  Normalization aliases in bound paths and exponent-overflow
numbers are rejected.  At the final release edge, semantic validation and
hashing operate on the same captured bytes, every opened input is checked for
concurrent mutation, and write-once publication links an open source inode
through a pinned directory descriptor before checking the published inode and
exact bytes.

## 9. Authority split and acceptance gates

The producer and scheduler must leave

```text
milestone_status = null
theorem_status   = null
final_status     = null
```

in every authoritative object.  They cannot promote a scientific claim.
Only the frozen independent checker may assign
`PASS_LOCAL_COMPLEMENT_ALL_SLABS`, and only if all of the following hold:

1. the freeze/run-config/machine handshake is exact;
2. the upstream L1 release and protected-box relations replay exactly;
3. all 102 canonical tree/manifest pairs exist, with no extras or symlinks;
4. every reachable node and every raw transcript passes independent replay;
5. every terminal leaf is `ENERGY_EXCLUDED` or `RETURN_EXCLUDED`;
6. no root candidate, invalid result, unresolved leaf, timeout, depth
   exhaustion, node exhaustion, or precision-domain disagreement occurs;
7. the aggregate hash DAG and write-once checker/postcheck objects agree.

`final_status` remains null even after this local-complement milestone.

## 10. Failure and reporting policy

- A `ROOT_CANDIDATE` is a scientific failure of the frozen route and is
  preserved; it is not permission to shrink the domain after inspection.
- A resource limit is inconclusive.  The frozen attempt is archived without
  tuning the limit after looking at the result.
- An implementation or provenance defect invalidates the generation.  A
  repaired implementation requires a new freeze and a new generation.
- A passing subset may be reported only as a diagnostic subset, never as the
  all-slab result.
- A 128/256 domain-verdict disagreement prevents promotion.
- Every human-readable report must repeat the explicit nonclaims in section
  2.

## 11. Pre-production gates

Before the first held-out evaluator dispatch, all of the following must be
sealed and independently reviewed:

- formal producer/checker namespace and freeze handshake tests;
- a complete 102-tree synthetic end-to-end run;
- crash/resume and whole-generation quarantine fault tests;
- randomized completion-order invariance and multi-tree budget-race tests;
- read-only replay of all 3,016 already public S0 node transcripts through a
  schema adapter or equivalent test harness;
- persistent CAPD rebuild and machine freeze;
- independent pre-freeze review with an explicit `ACCEPT_FOR_FREEZE` verdict;
- formal main freeze, followed by an `--initialize-only` run-config check.

No A1 held-out outcome is authorized before these gates close.
