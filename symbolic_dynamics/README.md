# Symbolic Dynamics Research Program

This directory is the umbrella for the symbolic-dynamics branch of the
Hilbert–Pólya structure program.  Research outputs are organized by stage so
that a completed screening round remains frozen while the next deformation is
developed independently.

The global scope rule remains unchanged: **Symbolic Dynamics is the only
primary system family**.  Ideas requiring geometry, Hamiltonian dynamics,
quantum graphs, scattering, or an external operator algebra remain
`ROUND2_CLUE` entries until a later project explicitly changes the family.

## Stage index

| Stage | Status | Purpose | Entry point |
|---|---|---|---|
| `stage_01_scope_screening` | **COMPLETE / FROZEN** | Six-candidate Session-4 audit, proofs, literature, experiments, and Route-A evaluations | [Stage 01 README](stages/stage_01_scope_screening/README.md) |
| `stage_02_stationary_wheel_extension` | **THEOREM SCREENING COMPLETE; SOURCE LOCK PENDING** | Determine whether the endogenous wheel-sieve clock can survive a stationary symbolic recoding with primitive cycles | [Stage 02 README](stages/stage_02_stationary_wheel_extension/README.md) |

Stage 01 remains the evidence base.  Stage 02 does not inherit a candidate
verdict from it and has not been assigned `SD-C07`: a new candidate ID is
allowed only after one grammar, clock, function space, and determinant
convention have all been frozen.

## Shared inputs and rules

- [Original Symbolic Dynamics proposal](propose-symbolic-dynamics.md)
- [Route-A evaluator](skills/route-a-evaluator.md)
- [Route-B evaluator](skills/route-b-evaluator.md)
- [Shared prior-work guide](docs/prior_work/README.md)
- [Stage lifecycle](stages/README.md)

The PDF and legacy prior-work corpus stays under `docs/prior_work/` as a
read-only input shared by stages.  It is intentionally not duplicated inside
the frozen Stage 01 package.

## Current decision

The next step is not to add reset edges to the wheel DAG.  Stage 02 has proved
that a strict extension cannot create periodic points, that a strong
bisimulation quotient of a finite DAG remains acyclic, and that preserving
the exact multiplier as a state-class label prevents cross-level merging.

The only live branch is therefore a genuinely new infinite factor or
observational recoding.  Before code is run it must freeze a level-blind map,
alphabet/memory class, exact clock decoder, cutoff-consistency rule, and
path-lifting semantics.  The immediate task is the
[Stage 02 source lock](stages/stage_02_stationary_wheel_extension/OBSERVATIONAL_RECODING_SOURCE_LOCK.md);
the contingent computation roadmap is in the
[experiment plan](stages/stage_02_stationary_wheel_extension/refine-logs/EXPERIMENT_PLAN.md).

## Integrity

`ARTIFACT_MANIFEST.sha256` is the umbrella manifest and is verified from the
repository root.  Each stage also carries a self-contained
`STAGE_MANIFEST.sha256`, whose paths are resolved from that stage's root.
The manifests cover the versioned, non-ignored research package; the shared
local PDF/legacy corpus and runtime caches are intentionally excluded.
