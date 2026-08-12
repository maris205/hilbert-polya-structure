# R401-VAL-L2-A1 independent-checker draft

Status: **DRAFT_NON_LICENSING; REJECT FOR PRODUCTION FREEZE**.  
Date: 2026-08-07.  
Prototype:
`scripts/check_r401_val_l2_all_slabs_independent.py`.  
Adversarial contract tests:
`tests/test_r401_val_l2_all_slabs_checker_contract.py`.

## Decision

The independent-checker architecture is implemented, but it cannot promote
the all-slab milestone in the repository's current state.  This is deliberate:

1. no formal machine-readable `R401_VAL_L2_A1_FREEZE.json` exists;
2. the present scheduler identifies itself as
   `R401-VAL-L2-A1-DRAFT`, with scientific licensing disabled;
3. no complete, sealed 102-tree production generation exists.

Any one of these facts is sufficient for
`REJECT_DRAFT_NON_LICENSING`.  The prototype writes only
`independent_checker.draft.json` and `DRAFT_POSTCHECK_STATUS.json` on a
rejection.  It cannot occupy the authoritative checker/postcheck namespace.

This draft does not inspect, execute, or tune against the 48 held-out L1
slabs.  All contract tests use synthetic archives.  Compatibility of the
exact-rational transcript algebra was checked only on already public S0 proof
objects.

## Independence boundary

The checker does not import:

- `scripts/run_r401_val_l2_all_slabs.py`;
- the S0 producer;
- a scheduler utility module; or
- any producer parser, interval helper, split helper, or status table.

It independently defines:

- the ordered pair matrix
  
  \[
    (128,S000),\ldots,(128,S050),
    (256,S000),\ldots,(256,S050);
  \]

- the local box and coordinate order;
- the eight-shell construction;
- exact midpoint and normalized-width splitting;
- the evaluator status/return-code namespace;
- strict JSON and path parsing;
- exact-rational interval/vector/matrix arithmetic; and
- the complete hash-DAG replay.

The checker does not perform a second ODE integration.  It verifies the
logical consequences of the archived outward interval proof objects.

## Formal promotion gate

A future production attempt must add the machine-readable file
`research/route_a_wave_trace/R401_VAL_L2_A1_FREEZE.json`.  It must contain at
least:

```json
{
  "schema_version": 1,
  "protocol_id": "R401-VAL-L2-A1",
  "status": "FROZEN_FOR_PRODUCTION",
  "scientific_licensing_enabled": true,
  "checker_mode": "INDEPENDENT_EXACT_RATIONAL_REPLAY",
  "checker_source_sha256": "...",
  "matrix": ["exact ordered 102 pair records"],
  "per_tree_limits": {
    "max_depth": "frozen integer",
    "max_nodes": "frozen integer"
  },
  "scheduler": {
    "policy": "deterministic_round_robin_barrier_batches_v1",
    "workers": "frozen positive integer",
    "node_timeout_seconds": "null or frozen positive integer",
    "global_scientific_budget": null
  },
  "logical_thresholds": "the exact four-field threshold object",
  "evaluator": {
    "source_file": "frozen relative source path",
    "source_sha256": "...",
    "binary_file": "frozen absolute invocation path",
    "binary_sha256": "...",
    "capd_commit": "731079217a9254ea2948d742df2b170895effe7f",
    "capd_flags": ["exact ordered build flags"],
    "status_returncode_whitelist": "the exact closed table"
  },
  "input_hashes": {
    "scripts/check_r401_val_l2_all_slabs_independent.py": "...",
    "scripts/run_r401_val_l2_all_slabs.py": "...",
    "validated/capd_r401_local_complement_mp.cpp": "...",
    "validated/CAPD_DEPENDENCY.md": "...",
    "research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json": "...",
    "research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md": "..."
  }
}
```

The future sealed `run_config.json` must independently bind the same exact
matrix, limits, immutable-input hash map, evaluator source and binary hashes,
CAPD commit/flags, scheduler policy/workers/timeout, logical thresholds,
closed status namespace, and freeze hash.  The checker hashes the actual
binary bytes at the exact invocation path; a plausible digest string alone is
not accepted.  Its required production namespace is:

```text
protocol_id = R401-VAL-L2-A1
licensing = FROZEN_PRODUCTION
scientific_licensing_enabled = true
milestone_status = null
theorem_status = null
final_status = null
```

The producer, scheduler, tree files, tree manifests, aggregate summary, and
aggregate manifest must all leave the three scientific status fields null.
Only this independently frozen checker may set
`PASS_LOCAL_COMPLEMENT_ALL_SLABS`, and it always leaves `final_status` null.

## Canonical archive and path gates

The checker generates, rather than trusts, the 102 expected tree paths and
102 expected tree-manifest paths.  It requires exactly:

```text
trees/{128,256}/S000.json ... S050.json
tree_manifests/{128,256}/S000.json ... S050.json
```

It rejects:

- a missing, extra, duplicated, or reordered pair;
- tree/path, manifest/path, aggregate/path, or payload identity disagreement;
- duplicate JSON object keys or non-finite JSON constants;
- absolute paths, `..`, backslashes, hidden path components, or noncanonical
  relative paths;
- a symlink at the leaf or in any authoritative parent component;
- hidden or unexpected authoritative shards; and
- a missing, extra, or duplicated raw node directory or file.

For every node ID in every canonical tree, the exact raw directory is:

```text
raw/<bits>/<slab>/<node-id>/
  record.json
  stdout.txt
  stderr.txt
  telemetry.json
```

No other committed raw object is accepted.  Operational telemetry is read
and JSON-validated but is excluded from the mathematical proof tree.

## Exact tree replay

For the exact L1 plan box

\[
 P_j=\prod_{k=0}^3[p^-_{jk},p^+_{jk}]
 \Subset B_{\rm loc},
\]

the checker independently constructs the standard eight closed shells:

\[
\begin{aligned}
C_{k,L}&=\prod_{i<k}[p^-_{ji},p^+_{ji}]
 \times[b^-_k,p^-_{jk}]
 \times\prod_{i>k}[b^-_i,b^+_i],\\
C_{k,U}&=\prod_{i<k}[p^-_{ji},p^+_{ji}]
 \times[p^+_{jk},b^+_k]
 \times\prod_{i>k}[b^-_i,b^+_i].
\end{aligned}
\]

Thus the verified domain identity is

\[
  P_j\cup\bigcup_{k=0}^{3}(C_{k,L}\cup C_{k,U})=B_{\rm loc},
\]

with boundary overlap allowed and no gap.  Equivalently, the eight shells
cover (B_{\rm loc}\setminus\operatorname{int}(P_j)).

At each split node, the checker recomputes

\[
 k_* = \operatorname*{arg\,max}_{k}
 \frac{\operatorname{wid}(X_k)}{\operatorname{wid}((B_{\rm loc})_k)},
 \qquad
 m=\frac{X^-_{k_*}+X^+_{k_*}}2,
\]

with the frozen exact-tie order
`q_slow, q_fast, p_slow, period`.  It then reconstructs the two child boxes
and their canonical IDs.  Missing children, orphan nodes, duplicate node IDs,
noncanonical node order, false parent/depth data, altered midpoints, altered
coordinates, depth exhaustion, and per-tree node-budget excess all fail.

Every reachable leaf must be `ENERGY_EXCLUDED` or `RETURN_EXCLUDED`.  A tree
containing `ROOT_CANDIDATE`, invalid/conflict, unresolved, resource-exhausted,
or unclassified leaves is non-licensing.

## Raw status and invocation replay

The closed evaluator namespace is:

| stdout status | return code | checker action |
|---|---:|---|
| `ENERGY_EXCLUDED` | 0 | terminal exclusion |
| `RETURN_EXCLUDED` | 0 | terminal exclusion |
| `UNKNOWN` | 2 | split below depth limit |
| `ENERGY_DERIVATIVE_FAIL` | 3 | split below depth limit |
| `ENERGY_GUARD_FAIL` | 3 | split below depth limit |
| `FLOW_FAIL` | 3 | split below depth limit |
| `ROOT_CANDIDATE` | 4 | scientific stop, never pass |
| `INVALID_EXCLUSION_UNIQUENESS_CONFLICT` | 5 | invalid, never pass |

A missing or repeated status, boolean return code, signal, timeout, unlisted
status/code pair, or split at the depth limit is invalid.  Failure outcomes
are never silently turned into splittable `UNKNOWN` nodes.

The future node record must contain:

```json
"invocation": {
  "argv": ["exact evaluator path and 11 exact argument strings"],
  "argv_sha256": "sha256(canonical-json(argv))"
}
```

The checker reconstructs this vector from the sealed evaluator path, tree
precision, slab interval, and node box.  The scheduler prototype now archives
this object, binds it into each tree manifest, and independently rejects
missing, reordered, endpoint-mutated, path-mutated, or hash-mutated argv
payloads.  It requires the exact three-way equality

```text
tree node invocation == record invocation == manifest argv hash.
```

The checker still returns `MISSING_PROOF_OBJECT` for any archive that lacks
the field; it never infers argv from an unbound process history.

## Energy-Newton replay

From the printed intervals at every energy step, the checker recomputes using
exact rational arithmetic

\[
  N=m-\frac{F(m)}{D(X)},
  \qquad D(X)=\partial_{Q_+}K_\epsilon(X).
\]

It verifies:

1. contiguous step indices and the complete contraction chain;
2. (m\subseteq X);
3. (D(X)>0), unless the exact status is
   `ENERGY_DERIVATIVE_FAIL`;
4. the displayed guarded Newton image contains the exact-rational replay and
   the printed raw Newton image plus the frozen symmetric guard;
5. the exact printed-box intersection or its emptiness;
6. the next `after` box equals a safe enclosure of that intersection; and
7. consistency of the final summary fields and flags.

For an empty intersection, the licensing gap is independently recomputed as

\[
 g=\operatorname{dist}(X,N_{\rm guarded}).
\]

`ENERGY_EXCLUDED` requires both this independently recomputed gap and the
separately displayed MPFR gap to exceed the mathematical margin.  The
displayed gap is not assumed to enclose the recomputed gap: decimal widening
of the separately printed operands can make the rational replay a few final
display units smaller.  Only the recomputed gap licenses the decision.

## Mean-value, preconditioned, and Krawczyk replay

For every transcript that reaches the return calculation, the checker reads

\[
X,\quad \bar x,\quad F_c,\quad F_{\rm dir},\quad J,\quad C
\]

and independently forms

\[
\widehat F_{\rm mv}=F_c+J(X-\bar x),
\]

\[
\widehat F_{\rm pre}=C\widehat F_{\rm mv},
\]

and

\[
\widehat K=\bar x-CF_c+(I-CJ)(X-\bar x).
\]

The displayed `F_mean`, `F_preconditioned`, and `K` must enclose these exact
rational reconstructions.  The checker recomputes the first selected
component and its exact distance from zero.  A displayed mean-value or
preconditioned separation is accepted only if the independently reconstructed
interval itself omits zero by more than the frozen margin.  It does not rely
on the producer's selected index alone.

The checker also tests

\[
  \widehat K\Subset\operatorname{int}(X)
\]

coordinate by coordinate.  It independently reconstructs the four logical
return outcomes:

| separation | Krawczyk strict subset | required status |
|---|---|---|
| yes | no | `RETURN_EXCLUDED` |
| no | yes | `ROOT_CANDIDATE` |
| yes | yes | `INVALID_EXCLUSION_UNIQUENESS_CONFLICT` |
| no | no | `UNKNOWN` |

If outward decimal display is too coarse to reproduce a producer decision,
the checker returns `MISSING_PROOF_OBJECT` rather than weakening the margin
or trusting the producer flag.  A future evaluator may need explicit display
guards for these algebraic objects if this occurs in a frozen mock/S0 replay.

## Hash DAG

The checker verifies the acyclic chain

```text
formal freeze
  -> immutable input files and checker hash
  -> sealed run_config and evaluator identities
  -> node task + exact argv + raw stdout/stderr hashes
  -> record.json hash
  -> tree file and per-node hashes
  -> tree manifest
  -> exact ordered 102-entry aggregate summary
  -> aggregate manifest
  -> independent checker result
  -> postcheck
```

No object contains its own hash.  The checker and postcheck are downstream of
the producer aggregate and therefore do not create a circular producer hash.
Release provenance remains a later, separately sealed object.

The checker verdict also records the exact freeze, sealed run config,
aggregate summary, aggregate manifest, evaluator source/binary, CAPD build,
and an ordered 102-entry tree-manifest root.  Their canonical digest defines
an `archive_generation_sha256`.  Authoritative checker and postcheck files are
write-once-or-byte-identical, so a later run cannot overwrite them with a
verdict for another generation.

## Current adversarial test coverage

The synthetic checker contract suite covers:

- source-level producer/scheduler import independence;
- duplicate JSON keys and non-finite values;
- path traversal, absolute/backslash/hidden paths, and symlinks;
- missing and extra tree/manifest pairs and payload/path identity mutation;
- the full closed status/return-code map and duplicate/missing raw status;
- exact Newton replay and guarded-image mutation;
- exact (F_{\rm mv}), (C F_{\rm mv}), Krawczyk, and selected-margin replay;
- exact eight-shell cover, midpoint split DAG, and child-geometry mutation;
- mandatory exact argv proof object and argv mutation;
- tree/record/manifest three-way argv binding and manifest mutation;
- missing/extra raw node objects and raw symlinks; and
- the exact ordered 102-entry aggregate hash DAG and hash mutation;
- original-path and parent-component symlink rejection before resolution;
- actual evaluator-binary, CAPD commit/flags, scheduler worker/timeout, and
  logical-threshold freeze/run-config comparison; and
- generation-bound provenance plus write-once authoritative output.

The focused suite must remain green before a formal freeze.  Additional tests
still required before production are listed below.

After the formal-readiness hardening, the combined scheduler/checker focused
suites passed 68 tests.  This is a mock/schema
result only and does not inspect held-out scientific outcomes.

## Remaining release blockers

- [x] Accept and seal `R401-VAL-L2-S0` as
      `PASS_IMPLEMENTATION_SMOKE`; its release provenance binds all six
      trees and 89,962 zero-failure independent checks.  The recommended
      all-slab limits are now depth 48 and 20,000 nodes per tree, but remain
      non-authoritative until the formal protocol/freeze review.
- [ ] Promote the mathematical protocol from the current rejected draft to
      `R401_VAL_L2_A1_PROTOCOL.md` after independent review.
- [x] Add exact `invocation.argv` and its canonical hash to every node record,
      with checker-enforced tree/record/manifest equality and mutation tests.
- [ ] Change the future frozen producer namespace from `DRAFT_NONE` to
      `FROZEN_PRODUCTION` without allowing it to assign scientific status.
- [x] Implement fail-closed prototype comparison of checker/producer inputs,
      actual evaluator binary, CAPD commit/flags, exact matrix, scheduler
      workers/timeout/policy, limits, thresholds, and status whitelist.
      Creating their machine-readable freeze remains deliberately deferred.
- [x] Bind a future verdict to the freeze, run config, aggregates, evaluator,
      and ordered tree-manifest root; make authoritative outputs write-once per
      archive generation.
- [x] Reject symlinked CLI provenance paths and parent components before
      resolution.
- [ ] Add synthetic crash tests at each transactional write boundary and
      prove that incomplete hidden staging objects cannot enter a generation.
- [ ] Add generation-quarantine tests: any resume binding mismatch must start
      a fresh eight-shell generation and must never mix old/new nodes.
- [ ] Add randomized completion-delay tests proving that canonical proof
      trees and hashes are invariant under worker completion order.
- [ ] Add budget-race tests at `max_nodes-1`, `max_nodes`, and
      `max_nodes+1` independently for multiple simultaneous trees.
- [ ] Run a mock/S0-only full checker audit after the schema change, including
      every internal `SPLIT` transcript, before touching held-out slabs.
- [ ] Obtain a second independent design review and explicitly accept the
      freeze; no self-approval by the scheduler or checker author.

## Claim boundary

Even a future `PASS_LOCAL_COMPLEMENT_ALL_SLABS` would prove only pointwise
uniqueness of the reduced return root inside the frozen local coordinate box
for every accepted L1 slab and every parameter in that slab.  Full-state
recovery remains restricted to the frozen (P_+=0) chart.

It would not prove uniqueness on an energy shell, a global orbit cover, a
phase/flow-box cover, a quantitative analytic trace radius containing
`delta=0.01`, a prime trace, a zeta-zero spectrum, a Hilbert--Polya operator,
the Riemann hypothesis, or any final programme claim.
