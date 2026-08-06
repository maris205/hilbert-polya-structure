# R401-VAL-L2-A1 all-slab local-complement draft

Status: **REJECT FOR FREEZE pending design-contract corrections; prospective
draft; not a claim**.  
Date: 2026-08-06.

## Objective

Upgrade the representative `R401-VAL-L2-S0` implementation smoke to a
computer-assisted local-complement theorem over every one of the 51 accepted
L1 parameter slabs and at both 128 and 256 MPFR bits.

For each slab $I_j$, let $B_j^{\rm L1}$ be the exact protected plan box
whose Krawczyk image is already certified strictly inside it.  The target is
to exclude every reduced return root in

\[
  B_{\rm loc}\setminus\operatorname{int}(B_j^{\rm L1}),
  \qquad
  B_{\rm loc}=[-.02,.02]\times[.12,.17]\times[-.08,.08]\times[.64,.69].
\]

The exact target statement is pointwise in the parameter:

\[
  \forall j\in\{0,\ldots,50\},\quad
  \forall\epsilon\in E_j:\qquad
  Z(F_\epsilon)\cap B_{\rm loc}=\{x_j(\epsilon)\}.
\]

If successful, L1 plus L2-A1 would give uniqueness of the reduced root in
the complete frozen local box $B_{\rm loc}$ for every parameter in every
slab.  Full-state return recovery would remain a corollary only in the
frozen $P_+=0$ chart.  The result would not establish the local
phase/flow-box cover, uniqueness on the whole energy shell, the global shell
cover, an independent event-projected determinant, a quantitative
$\delta_{\rm tr}>0.01$, an arithmetic prime trace, or RH.

## Prospective production matrix

- exact slabs: `S000` through `S050`, as recorded in
  `R401_VAL_L1_FINAL_PLAN_V2.json`;
- precision: 128 and 256 MPFR bits;
- exact matrix: 102 independently archived trees;
- domain decomposition, interval-Newton energy contraction, residual
  exclusion rules, and split rule: identical to the accepted S0 protocol;
- no sampled residual may be a logical gate;
- cross-precision requirement: both precisions cover the same exact input
  domains and reach the same domain-level exclusion verdict; adaptive tree
  shapes and counts need not agree.

The accepted S0 release has now supplied the preregistered budget evidence.
Across its six trees it evaluated 3,016 nodes, reached maximum depth 36, and
used 28.605 node-hours.  The largest tree contained 574 nodes.  On a linear
102-tree extrapolation, the observed workload is approximately 486
node-hours, or 20.3 wall hours under ideal 24-worker saturation.  This is a
capacity estimate, not a stopping or acceptance rule.

The prospective formal budget is depth 48 and 20,000 evaluated nodes per
tree, with 24 global workers, at most one in-flight node per tree, and a
7,200-second per-node timeout.  Timeout or either per-tree limit is a
non-pass.  No global node or wall-time budget may affect the scientific
verdict.  These values remain recommendations until the formal protocol and
machine-readable freeze pass their second review; they may not be tuned
after inspecting an L2-A1 held-out failure.

The observed S0 archive occupies about 49 MB, suggesting roughly 0.83 GB at
the same node density for 102 trees.  The preregistered 2.04-million-node
worst case is instead on the order of 34 GB before Git packing and duplicate
working/release copies.  The current filesystem has only about 48 GB free,
so formal production should require at least 100 GB free storage even though
the expected archive is much smaller.

## Scheduler redesign

S0 deliberately executes one tree at a time.  Near a protected-box boundary,
one tree can narrow to only 2--8 active branches, leaving most cores idle even
though each MPFR integration remains expensive.  L2-A1 should therefore use
a two-level scheduler:

1. a global queue of independent `(precision, slab, node)` tasks;
2. per-tree state machines that commit a node result atomically and enqueue
   children only after an `UNKNOWN` classification;
3. fair scheduling across multiple slabs so serial boundary tails from one
   tree overlap wide fronts from other trees;
4. a fixed global worker count recorded in the environment manifest;
5. no scientific result may depend on completion order.

The target scheduler is resumable but not mutable.  Every committed node
must bind its exact input box, epsilon slab, precision, evaluator hash, raw
stdout/stderr hashes, return code, and classification.  Resume may reuse a
node only if every binding matches the frozen run; otherwise that tree is
invalidated and rerun from its eight exact shells.

## Sharded release layout

```text
results/r401_val_l2_all_slabs/
  run_config.json
  trees/{128,256}/S000.json ... S050.json
  raw/{128,256}/S000/... ... S050/...
  tree_manifests/{128,256}/S000.json ... S050.json
  aggregate_summary.json
  aggregate_manifest.json
  independent_checker.json
  POSTCHECK_STATUS.json
```

Each tree manifest should be independently checkable so an interrupted
multi-hour run does not require reparsing unrelated shards.  The aggregate
manifest must bind the exact set of 102 tree manifests and reject duplicates,
missing pairs, or unexpected files.

## Prospective acceptance gates

1. exactly one authoritative tree for every one of the 102 frozen pairs;
2. exact eight-shell coverage of each local complement;
3. exact midpoint/max-normalized-width splits and parent--child unions;
4. every stored node evaluated, reachable, within the frozen depth and node
   budgets, and bound to its raw transcript;
5. every terminal leaf classified `ENERGY_EXCLUDED` or `RETURN_EXCLUDED`;
6. zero `ROOT_CANDIDATE`, `UNKNOWN` terminal, invalid, flow-fail, derivative-
   fail, budget-exhausted, or exclusion/Krawczyk-conflict leaves;
7. exact replay of every archived Newton contraction/gap and return-separation
   certificate by a checker that does not import the producer;
8. authoritative A4.12 L1 release and protected-box relations replayed before
   accepting any tree;
9. per-tree manifests, aggregate manifest, checker, postcheck, and release
   provenance all agree;
10. producer and scheduler leave the final theorem status null; only the
    independent checker may promote the named local-complement milestone.

## Failure policy

- A `ROOT_CANDIDATE` is a scientific failure requiring a new theorem route,
  not an invitation to shrink the domain after inspection.
- Depth/node exhaustion is inconclusive and preserves the frozen attempt.
- An implementation or provenance defect invalidates the affected attempt;
  it is not repaired inside an apparently passing archive.
- A successful subset of slabs remains a diagnostic subset and cannot be
  reported as the all-slab theorem.
- If 128 and 256 bits disagree at the domain-verdict level, the milestone
  fails even when one precision closes every tree.

## Work required before freeze

- [x] accept `R401-VAL-L2-S0` with independent postcheck and release
      provenance (`PASS_IMPLEMENTATION_SMOKE`);
- [x] record S0 maximum depth, node counts, wall time, and per-class counts;
- [x] estimate all-slab storage and CPU needs from the six frozen trees;
- [x] implement and component-test the cross-tree scheduler without changing the C++
      evaluator's proof semantics;
- [ ] add interruption/resume, duplicate-shard, corrupted-transcript, and
      completion-order invariance tests;
- [ ] independently audit the scheduler and checker;
- [ ] freeze all hashes, budgets, resource settings, and status namespaces
      before production.

## Independent design review

The 2026-08-06 release-blocking review accepted the mathematical kernel after
the pointwise/domain correction above, but rejected this draft for freeze.
The other 48 real slabs remain held out: implementation and budget tuning may
use only mock evaluators and the already public S0 data.

A second read-only design audit returned `REVISE`, not rejection of the
architecture.  The subsequent formal-readiness hardening closed actual
binary/CAPD identity, three-layer argv binding, generation-bound provenance,
write-once authority, and pre-resolution symlink checks.  The combined mock
suites now pass 68 tests.  Formal protocol promotion, end-to-end 102-tree
synthetic replay, crash/quarantine/order/budget-race tests, and a final
independent freeze review remain mandatory.

Before a freeze can be accepted, the next revision must specify and test all
of the following:

1. exact per-tree depth and evaluated-node budgets, with no global budget or
   wall-clock rule that can make the scientific result depend on scheduling;
2. canonical round-robin admission across 102 ordered tree state machines,
   per-tree inflight limits, exact rational midpoint arithmetic, and the
   coordinate tie-break `q_slow, q_fast, p_slow, period`;
3. one evaluator per process so CAPD/MPFR rounding state is never shared
   across concurrent tasks;
4. transactional node commits on one filesystem, binding run config, pair,
   node geometry, evaluator/dependency identities, exact argv, raw hashes,
   return code, and status before an atomic commit marker appears;
5. strict resume: a binding mismatch quarantines the complete old generation
   and starts a new eight-shell tree; generations may never be mixed;
6. canonical proof trees independent of completion time/order, with telemetry
   stored separately;
7. a checker-generated exact path matrix for all 102 tree and tree-manifest
   files, rejecting extras, duplicates, symlinks, traversal, payload/path
   mismatch, duplicate JSON keys, and malformed slab union;
8. raw transcript replay for every evaluated node, including nodes later
   classified `SPLIT`, under a frozen `(status, return code, action)`
   whitelist; unknown status or signal/timeout is invalid, never splittable;
9. independent exact-rational reconstruction of the Newton steps,
   `F_mean`, `C F_mean`, the Krawczyk image, selected exclusion component,
   logical margin, and exclusion/uniqueness conflict from archived proof
   objects; this still is not a second ODE integration;
10. a noncircular hash DAG from protocol/freeze through sealed run config,
    node commits, tree manifests, aggregate manifest, checker/postcheck, and
    final release provenance;
11. exact status names and authority: the scheduler/producer cannot set a
    milestone, subsets cannot pass, unexpected evaluator behavior is invalid,
    and `final_status` remains null after any local-complement pass;
12. adversarial tests for missing/duplicate/extra pairs, proof-object
    mutation, budget races, random completion delays, crash points, resume
    provenance, path safety, and checker independence.

The planned promotion theorem may be reconsidered only after these contracts
pass mock/S0 tests and receive a second independent review.  No A1 result is
authorized by this draft.
