# Papers 49--50 pre-Stage-0 handoff

Status: `PROVISIONAL_AWAITING_PLAN_READY`

This file records the read-only baseline and proposed namespace.  It is not an
authorization to write the authority repository.

## Frozen Git baseline

- Authority: `/root/autodl-tmp/hilbert-polya-structure`
- Baseline commit: `7ce44588f866e6b803bc76161a9841fb07b7f644`
- Local `HEAD`, `origin/main`, and sampled live `refs/heads/main` matched at the
  baseline checkpoint.
- `HEAD:symbolic_dynamics` tree:
  `68540814b3496324d86ba00c45fab902304daf67`.
- The preceding 15-commit drift from `f5bc1ccecd3690b29acf6c907cdc2d466d37d87f`
  was a strict fast-forward whose 274 changed paths were all under
  `henon_dynamics/`; the symbolic tree was byte-identical at both endpoints.
- Authority and plain mirror symbolic trees were byte-identical at the
  checkpoint, excluding the mirror-only `id.txt` bookkeeping file.

The live remote must be sampled again immediately before every Git mutation;
the checkpoint above is not a standing compare-and-swap authorization.

## Proposed paper namespaces

These paths become final only if the independent GPT-5.4 xhigh plan gates keep
the corresponding title and theorem scope unchanged.

1. Paper 49
   - plan-gated title: *Hausdorff Dimension for Complete Cyclic Markov Hom
     Tree-Shifts with an Unrestricted One-Level Feeder or Canonical
     Unrestricted L-Level Forced Chains*
   - proposed path:
     `symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts/`
   - writer root: `/tmp/paper49_writer_candidate`
   - plan gate: `PLAN_READY`; raw independent review SHA-256
     `ebe20d1c4d33be751b78c7770ac28247e5bca035b7592ec744315024ae2e14ba`
   - theorem input: `/tmp/p49_tree_stage2`
   - reciprocal audit: `/tmp/p49_tree_cross_audit`

2. Paper 50
   - plan-gated title: *Affine Divisibility Toeplitz Systems: Constructive
     Periods and Same-Base Pointed Factor Posets*
   - proposed path:
     `symbolic_dynamics/papers/50-affine-divisibility-toeplitz-factor-posets/`
   - writer root: `/tmp/paper50_writer_candidate`
   - plan gate: `PLAN_READY`; raw independent recheck SHA-256
     `ac4ca32ecc55e8b87dad4fcc8e38175593ec20434da7e69440212cf07dfb9750`
   - theorem input: `/tmp/p50_toeplitz_stage2`
   - reciprocal audit: `/tmp/p50_toeplitz_independent_audit`

Both target paths and the next prospective Route identifiers must be checked
for absence again after the plan gates.  No Route identifier is assigned here.

## Stage-0 boundary

Each paper receives its own static, output-free project candidate in `/tmp`.
The candidate must contain:

- a byte-locked copy of the applicable frozen theorem/source package;
- two independent exact implementations or a production implementation plus
  a no-production-import auditor;
- a claim-driven integration plan, typed result schema, source lock, theorem
  falsifiers, mutation registry, and Route expectation;
- a deterministic `run_integration.py --state A` entry point that writes only
  its own `outputs/` namespace;
- a static manifest and self-verifying pre-output seal;
- no manuscript bytes, no final paper manifest, and no publication seal.

Finite enumeration is evidence and falsification control only.  The analytic
proofs remain self-contained and must not depend on bounded checks.

## Required gates

1. Both manuscript plans reach exact `PLAN_READY` through independent
   GPT-5.4 xhigh review.
2. Static candidates pass source, type, mode, manifest, hostile-environment,
   mutation, and no-write audits in disposable roots.
3. A fresh independent pre-run audit returns `RUN-GO` for each exact candidate.
4. Only then may the two static roots be installed in authority and their
   State-A integration entry points run once, followed by idempotence replay
   and an independent post-output audit.
5. Writer closure, publication transition, README registration, Git commits,
   push, and mirror synchronization remain later and separately audited gates.
