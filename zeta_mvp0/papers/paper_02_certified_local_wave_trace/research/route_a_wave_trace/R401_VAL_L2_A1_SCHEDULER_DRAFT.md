# R401-VAL-L2-A1 scheduler prototype

Status: **DRAFT_NON_LICENSING**.  This note is neither a freeze nor a
computer-assisted result.  Date: 2026-08-06.

## Scope

`scripts/run_r401_val_l2_all_slabs.py` is a prospective cross-tree scheduler
for the exact matrix

```text
{128, 256 MPFR bits} x {S000, ..., S050} = 102 trees.
```

It preserves the node-level proof semantics of
`validated/capd_r401_local_complement_mp.cpp`.  Its only role is to dispatch
exact boxes, commit evaluator transcripts, resume an immutable generation,
and produce canonical tree shards.  The eight closed complement shells cover

\[
  B_{\rm loc}\setminus\operatorname{int}(P_j),
\]

where (P_j) is the exact protected L1 plan box.  The prospective pointwise
target is

\[
  \forall j\;\forall\epsilon\in E_j:\qquad
  Z(F_\epsilon)\cap B_{\rm loc}=\{x_j(\epsilon)\}.
\]

Even a future successful independent validation would be confined to the
frozen local (P_+=0) chart.  It would not prove uniqueness on the whole
energy shell, global uniqueness, a phase/global cover, an arithmetic trace,
Hilbert--Polya, zeta-zero reconstruction, or RH.

## Scheduler and archive contract

- Admission is deterministic round robin over the 102 tree queues.  A barrier
  batch is committed in canonical `(precision, slab, depth, node_id)` order,
  so worker completion order cannot change a proof tree or manifest.
- Depth and node limits are per tree.  The prototype has no default L2-A1
  limits because those values have not been frozen.  An operational
  `--dispatch-limit` may stop a session for testing or maintenance, but it can
  never license a completed tree.
- Every evaluated node, including a `SPLIT`, is committed as one same-filesystem
  directory transaction containing `stdout.txt`, `stderr.txt`, telemetry, and
  `record.json`.  Files are flushed with `fsync`; the staging directory is
  atomically renamed only after the record commit marker is durable.  Hidden
  interrupted staging directories are non-authoritative and preserved for
  inspection.
- Every node record contains the exact 12-string process invocation: evaluator
  path, precision, two epsilon endpoints, and the eight box endpoints in the
  frozen `(q_slow, q_fast, p_slow, period)` order.  Its `argv_sha256` is the
  SHA-256 digest of the canonical JSON encoding of that string array.  Resume
  regenerates the array from the exact node task and rejects a missing field,
  reordered argument, altered endpoint/path, or changed digest.
- A canonical tree is written to `trees/{bits}/Sxxx.json`; its independently
  located `tree_manifests/{bits}/Sxxx.json` is written last as the commit
  marker.  The manifest binds the tree, every committed node/raw hash, and each
  node's `argv_sha256`.  It contains no self-hash, so the provenance graph is
  acyclic.
- Resume binds the run configuration, prospective freeze hash, exact tree and
  node identity, epsilon/box, evaluator source and binary hashes, CAPD commit
  and flags, precision, logical thresholds, worker count, and per-tree limits.
  A mismatch or corrupted committed shard raises an error and leaves the old
  generation untouched; it is never repaired silently inside a finalized
  tree.
- CLI provenance paths are checked lexically before resolution.  A symlinked
  evaluator, CAPD source/config helper, prospective freeze, output leaf, or
  existing parent component is rejected rather than silently followed.
- Canonical matrix scans reject missing or extra tree/manifest paths,
  duplicate internal identities, duplicate JSON keys, path traversal,
  symlinks, missing raw files, and hash mismatches.
- Telemetry such as wall time is excluded from canonical proof trees and
  manifests.  It may differ between runs without changing scientific bytes.

The evaluator status/return-code relation is a closed whitelist:

| Evaluator output | Scheduler action |
|---|---|
| `ENERGY_EXCLUDED / 0` | terminal exclusion |
| `RETURN_EXCLUDED / 0` | terminal exclusion |
| `UNKNOWN / 2` | split below the depth limit |
| `ENERGY_DERIVATIVE_FAIL / 3` | split below the depth limit |
| `ENERGY_GUARD_FAIL / 3` | split below the depth limit |
| `FLOW_FAIL / 3` | split below the depth limit |
| `ROOT_CANDIDATE / 4` | hard scientific stop, non-pass |
| `INVALID_EXCLUSION_UNIQUENESS_CONFLICT / 5` | hard invalid stop |
| timeout, signal, missing/repeated status, or any other pair | invalid |

Depth exhaustion, per-tree node exhaustion, a root candidate, and evaluator or
provenance corruption remain distinct non-pass states.  Every producer object
keeps `milestone_status`, `theorem_status`, and `final_status` equal to `null`.

## Current use

The only authorized current use is code inspection and mocked/S0-contract
testing:

```bash
pytest -q tests/test_r401_val_l2_all_slabs_scheduler.py
```

The CLI deliberately requires explicit values for `--max-depth` and
`--max-nodes`.  `--execute-draft` additionally refuses to start without an
explicit freeze file.  The current all-slab document is only a draft, so no
production command is recorded here and no outcomes from the other 48 slabs
have been inspected by this implementation milestone.

## Deferred before any production or claim

1. **Independent checker audit:** the non-importing checker prototype now
   parses every raw node, replays interval Newton and return separation,
   independently recomputes (F_{\rm mean}), (C F_{\rm mean}), (K), and the
   exclusion/Krawczyk conflict, and checks the exact 102-pair hash DAG.  The
   combined scheduler/checker focused suites pass 68 tests, but the pair
   still requires a second design audit and a formal freeze.
2. **Audit and freeze:** independently audit this scheduler/checker, then bind
   their hashes, CAPD build, exact per-tree budgets, worker count, thresholds,
   and status namespaces in a noncircular L2-A1 freeze before looking at
   held-out outcomes.
3. **Held-out production:** only after that freeze, run all 102 trees and the
   independent postcheck.  The scheduler alone can never promote a theorem
   status, even if every producer tree terminates by exclusion.

The accepted S0, L1, and monodromy-gap files/results are unchanged by this
prototype.
