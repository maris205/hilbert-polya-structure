# R401-VAL-L3-A1 independent checker contract candidate

Contract identifier: `R401-VAL-L3-A1-CHECKER-CONTRACT`

Prepared: 2026-08-09 UTC

Status: **PROSPECTIVE_NON_LICENSING / REJECT_FOR_DISPATCH**

## 1. Authority split

The future L3-A1 release has three independent scientific checkers and three
write-once postchecks:

```text
static aggregate -> static checker -> STATIC_POSTCHECK_STATUS.json
branch aggregate -> branch checker -> BRANCH_POSTCHECK_STATUS.json
both component chains -> composite checker -> POSTCHECK_STATUS.json.
```

No checker imports the scheduler, an evaluator, another checker, an S0
producer, or producer interval/path/status helpers.  The checkers may use
independently implemented standard-library parsing and pinned Arb primitives.

Component checkers assign only `component_status`.  Their milestone, theorem,
and final fields remain null.  Only the composite checker can assign the local
theorem status.  Postchecks copy and bind an existing checker result but never
create or widen authority.

Only partial checker implementation candidates exist.  The complete
three-checker/three-postcheck chain is neither implemented nor frozen and
authorizes no evaluator.

## 2. Candidate exact result schemas

Final implementations may tighten nested diagnostics before freeze.  They may
not change the following exact top-level schemas after the first frozen
dispatch.

### 2.1 Component checker object

The exact top-level key set is:

```text
schema_version
protocol_id
artifact_role
authority
checker_status
component_status
scientific_licensing_enabled
passed
matrix_id
main_freeze_sha256
run_config_sha256
component_aggregate_summary_sha256
component_aggregate_manifest_sha256
replay_counts
cross_precision
diagnostics
failures
source_bindings
claim_boundary
milestone_status
theorem_status
final_status
```

For a passing static checker:

```text
artifact_role = STATIC_INDEPENDENT_CHECKER
authority = INDEPENDENT_CHECKER
checker_status = PASS_INDEPENDENT_CHECKER
component_status = PASS_STATIC_PHASE_ANCHOR_ALL_SLABS
scientific_licensing_enabled = false
passed = true
milestone_status = null
theorem_status = null
final_status = null.
```

For a passing branch checker, the same fields apply with roles
`BRANCH_INDEPENDENT_CHECKER` and
`PASS_BRANCH_TUBE_ALL_SLABS`.  On any failure, `passed=false`,
`checker_status=FAIL_INDEPENDENT_CHECKER`, `component_status=null`, and the
three authority statuses remain null.

### 2.2 Composite checker object

The exact top-level key set is:

```text
schema_version
protocol_id
artifact_role
authority
checker_status
component_status
scientific_licensing_enabled
passed
matrix_id
main_freeze_sha256
run_config_sha256
static_chain
branch_chain
upstream_chains
s0_compatibility
replay_counts
cross_precision
diagnostics
failures
source_bindings
claim_boundary
milestone_status
theorem_status
final_status
```

A passing object has exactly:

```text
artifact_role = COMPOSITE_INDEPENDENT_CHECKER
authority = INDEPENDENT_CHECKER
checker_status = PASS_INDEPENDENT_CHECKER
component_status = null
scientific_licensing_enabled = true
passed = true
milestone_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
theorem_status = PASS_LOCAL_PHASE_TUBE_ALL_SLABS
final_status = null.
```

On failure, licensing is false and all three scientific status fields are
null.

### 2.3 Postcheck object

All three postchecks share this exact top-level key set:

```text
schema_version
protocol_id
artifact_role
authority
postcheck_status
passed
checker_path
checker_sha256
main_freeze_sha256
run_config_sha256
bound_artifacts
replay_counts
failures
claim_boundary
component_status
milestone_status
theorem_status
final_status
```

The roles are `STATIC_POSTCHECK`, `BRANCH_POSTCHECK`, and
`COMPOSITE_POSTCHECK`.  `authority=POSTCHECK_ONLY` and
`postcheck_status=PASS_WRITE_ONCE_POSTCHECK` indicate only that a separate
postcheck-mode replay reproduced the published checker chain.  Component
postchecks copy their checker component status while retaining null
milestone/theorem/final values.  The composite postcheck copies the exact
composite milestone/theorem and retains `final_status=null`.

## 3. Strict data and path rules

All JSON is strict and canonical:

- duplicate keys, NaN, Infinity, exponent overflow, and nonfinite parsed
  values are rejected;
- Boolean values cannot stand for integers; integral floats cannot stand for
  integer versions, counts, precisions, or limits;
- every object has its exact key set and every nested diagnostic has a frozen
  exact schema;
- path traversal, backslashes, absolute aliases, `.`/`..`, doubled
  separators, hidden extras, and normalization aliases are rejected;
- every authoritative original lexical path and parent component is checked
  for symlinks before resolution;
- hard-link aliases of write-once control objects are rejected; and
- semantic parsing and hashing use the same captured byte snapshot, with
  concurrent-mutation checks before accepting the snapshot.

The checker exact-scans the authoritative root.  Operational staging and
telemetry must be in its frozen same-filesystem sibling and never count as
scientific evidence.

## 4. Exact matrix and archive replay

Each checker independently constructs the protocol matrix: the canonical
`S000` through `S050` sequence at 128 bits followed by the same sequence at
256 bits.  It computes the canonical matrix digest and compares it with the
main freeze, run config, every cell record/manifest, both aggregates, and the
checker output.

For its component, a checker requires exactly:

```text
102 canonical cell directories,
102 canonical cell manifests,
1 aggregate summary,
1 aggregate manifest,
0 extra authoritative paths.
```

The aggregate manifest's ordered content root is independently recomputed
from the 102 cell manifests.  Every cell manifest is opened, strictly parsed,
and used to rehash every cell byte.  A digest quoted by another object is not
trusted without direct recomputation.

## 5. Static scientific replay

The static checker reconstructs the model from exact algebraic definitions,
not producer constants or rounded eigenvectors.  It independently verifies:

1. exact epsilon, coordinate order, root boxes, outer implications, and
   precision identity;
2. exact rational/dyadic parent--child unions, deterministic normalized-width
   split choice, and tie order;
3. energy and slow-tube exclusions on every corresponding leaf;
4. on every `ANGLE_CERTIFIED` leaf, strict positive lower endpoints for
   `D_plus`, `N_plus`, and `omega_plus*N_plus`, plus angular-rate upper endpoint
   below 18;
5. exact counts, maximum depths, decisive extrema, tree content roots, and
   zero unresolved leaves;
6. exact forbidden-section shell exclusion and the central closed landing
   window inside `0.12<Q_plus<0.17`;
7. an outward independent proof of `18*0.69<4*pi`; and
8. the winding-one and unique-positive-crossing analytic implication.

The checker does not accept an `angle_passed` Boolean in place of endpoints.
A static scientific-stop status is absent because interval permission of a
bad gate is not a constrained existence witness.

## 6. Branch scientific replay

The branch checker independently validates the exact L1 primary record for
each cell and the accepted L1 five-object chain.  It checks the exact
12-string invocation, unique input echo, persistent binary/source/CAPD/runtime
bindings, return code, unique status, stdout/stderr caps, truncation flag, and
raw hashes.

For every passing transcript it requires exactly 64 ordered phase records and
independently reconstructs

```text
[k/64,(k+1)/64], k=0,...,63.
```

The intervals cover `[0,1]` with endpoint-only adjacency and no gap,
reordering, omission, or replacement.  The declared `SolutionCurve` domain
must contain this cover.

Every printed CAPD state endpoint is parsed as an exact decimal rational.  At
the frozen precision, the checker independently reconstructs an outward Arb
enclosure of `omega_minus` and recomputes

```text
(omega_minus*Q_minus)^2 + P_minus^2.
```

Every rigorous upper endpoint must be below `0.0016`; the global maximum and
minimum margin are independently derived.  Printed slow-radius and margin
fields are telemetry and must enclose, but cannot replace, recomputation.

This replay is not a second ODE integration.  The frozen CAPD source, binary,
dependency, and machine chain supply the flow enclosure; the checker proves
that archived state enclosures imply the tube inequality.

## 7. Cross-precision semantics

For every slab, both component checkers require the 128- and 256-bit records
to use the same exact rational epsilon interval, same exact static roots, and
same exact pre-outward L1 primary root domain.  Both must have the same passing
component status.

The checker does not require identical:

- dyadic tree topology, node count, or maximum depth;
- Arb or CAPD printed endpoints;
- CAPD `SolutionCurve` piece count;
- proof, transcript, manifest, or content bytes; or
- decisive margin values.

Any domain or final-verdict disagreement blocks both component and composite
promotion.

## 8. Exact S0 compatibility gate

Before a future main freeze, the no-evaluator S0 adapter and an independent
checker must read the sealed S0 archive without modifying it.  The exact S0
matrix is `{S000,S025,S050} x {128,256}`.  The exact facts are:

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

The strict compatibility object's exact top-level keys are:

```text
schema_version
protocol_id
artifact_role
artifact_status
source_protocols
matrix
static_facts
branch_facts
composite_facts
control_hashes
role_sets
source_bindings
replay_status
failures
claim_boundary
milestone_status
theorem_status
final_status
```

It has `artifact_status=NON_LICENSING`,
`replay_status=PASS_S0_COMPATIBILITY_REPLAY` only on exact replay, and null
milestone/theorem/final values.  Its nine exact control hashes are those in
the sealed A4.16 representative report; a matching hash with changed role,
count, status, or schema is rejected.  The main freeze binds both this object
and the nine controls directly.

## 9. Component postchecks

After a component checker publishes once, its frozen postcheck mode:

1. refuses to overwrite an existing postcheck;
2. reopens the published checker and both component aggregates;
3. repeats the exact matrix/path/schema/hash and scientific replay;
4. checks the checker-source hash against the main-freeze 53-role input map;
5. reproduces the component status and failure list; and
6. publishes the corresponding component postcheck with no new authority.

A component postcheck is required even though the composite checker later
replays both component chains.

## 10. Composite replay and authority

The composite checker requires exact passing static and branch checker plus
postcheck objects, the identical 102-cell matrix, and exact component
aggregate roots.  It independently replays:

- all 53 mandatory main-freeze input roles defined by the release contract;
- the accepted L1 and A4.15 five-object chains;
- the exact S0 compatibility object and nine S0 control roles;
- the A4.16 analytic derivation and conditional tube-residence premise;
- null producer and component programme statuses; and
- all claim-boundary text tokens.

Only then may it assign `PASS_LOCAL_PHASE_TUBE_ALL_SLABS`.  Its postcheck
reopens and reproduces the complete composite chain and binds the exact 68-
role release map candidate.  `final_status` remains null.

## 11. Failure policy

The checker fails closed on any missing/extra cell, unresolved leaf, depth or
node exhaustion, timeout, signal, output cap, CAPD flow failure, malformed
object, non-whitelisted status/code pair, scientific stop, cross-precision
disagreement, symlink/path alias, hash mismatch, stale machine binding,
changed role map, or non-null unauthorized status.

A failure writes an exact failure list only if the checker output path is a
new write-once path.  It never repairs producer bytes.  A defect in producer,
checker, or contract code requires a new future freeze and generation.

## 12. Candidate exact role counts

The main-freeze input map has exactly 53 named roles.  A future release has
exactly 68 named roles: those 53 inputs, the main freeze, and 14 result/control
roles.  The role names and paths are enumerated in
`R401_VAL_L3_A1_RELEASE_PROVENANCE_CONTRACT.md`.  Missing, extra, duplicated,
aliased, or reordered roles are rejected.  Per-cell files are transitively
bound by the independently recomputed component aggregate manifests rather
than assigned 204 top-level release roles.

The 53-role map explicitly binds the implementation-design review, static
evaluator test, branch runtime module, and S0-compatibility test.  None may be
treated as an unbound transitive helper.  This count supersedes the earlier
incomplete 49-role implementation candidate; it does not create a freeze.

## 13. Required checker tests

Before freeze construction, focused tests must mutate every decisive static
and branch interval, every phase endpoint, every count and content root,
every authority field, every role and hash, and every cross-precision domain
or verdict.  Tests must also cover strict JSON types, nonfinite values,
symlinks, hard links, TOCTOU snapshots, missing/extra authoritative paths,
checker/postcheck overwrite, and a full mocked 102-by-two-component chain.

The test suite and recorded hashes are mandatory main-freeze inputs.  A mock
pass has no scientific status.

## 14. Present rejection gate

```text
contract_status = PROSPECTIVE_NON_LICENSING
checker_implementation_stable = false
component_postchecks_exist = false
composite_postcheck_exists = false
main_freeze_exists = false
dispatch_authorized = false
milestone_status = null
theorem_status = null
final_status = null
```

This checker contract invokes no evaluator and accepts no current theorem.
