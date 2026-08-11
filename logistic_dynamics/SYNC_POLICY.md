# HP-Dynamics mirror synchronization policy

## Repository roles

`riemann_dyna` is the complete research laboratory and historical evidence
store.  `hilbert-polya-structure/logistic_dynamics` is the unified shareable
archive for stable HP-Dynamics checkpoints.  Synchronization copies evidence;
it does not delete or rewrite the source history.

## What must be mirrored

A stable checkpoint is mirrored when it has a frozen mathematical object and
at least one of the following:

1. a versioned Route-A evaluation;
2. a formal result or obstruction;
3. a certified artifact with a reusable research conclusion;
4. an archive/control role required to interpret later stages.

Every mirrored record must identify:

- candidate/audit/clue IDs;
- formal-candidate status;
- source lock and Route-A evaluation, when they exist;
- analytic and Riemann-target Route-A boundaries;
- Route-B authorization state;
- strongest evidence and strongest failure;
- exact source commit and SHA-256 hashes;
- paper status and next legitimate task.

## What is not promoted

The mirror must not turn any of the following into a paper claim:

- saved numerical zero matches or best-seed plots;
- prime, Riemann-zero, USTC, or GUE tables used by legacy diagnostics;
- a fixed-order result presented as an all-order theorem;
- a scalar continuation relabeled as the original operator determinant;
- a natural finite/unitary spectrum presented as self-adjointness;
- a cross-determinant completion or a changed clock/normalization;
- an audit whose mathematical object remains undefined.

Such material may appear only in an explicitly marked archive or diagnostic
project.

## Version and correction rules

- Historical YAML files are copied byte-for-byte and are never normalized in
  place.
- Later evaluations supersede incompatible earlier claims but do not erase
  them.
- Generated `SOURCE_PROVENANCE.yaml` and `SOURCE_HASHES.sha256` files bind the
  shareable project to one main-repository commit.
- Existing manuscripts are preserved.  The synchronizer may add provenance or
  missing source evidence but never edit a hand-written paper.
- A changed object, clock, determinant, function space, or data firewall
  requires a new source lock and normally a new project stage.

## Dependency policy

Repository-relative dependencies named by generators and evaluations are
copied automatically when available.  Independent repositories are not
silently vendored.  They must be listed under `external_dependencies` in the
stage provenance.

Repository-wide ledgers needed as exact regression fixtures are listed as
`no_follow_files`: their bytes are mirrored and hashed, but prose links inside
them do not recursively import unrelated stages into the current project.

In particular, the legacy RH programme under
`docs/related_programs/prime_dynamics_theory` remains a separate Git
repository and is intentionally excluded from this mirror.

## Future workflow

```text
complete stable checkpoint in riemann_dyna
        ↓
freeze source commit and add/update sync_manifest.yaml
        ↓
run sync_from_riemann_dyna.py
        ↓
run --check, project tests, YAML validation, and git diff --check
        ↓
update STAGE_INDEX.md automatically
        ↓
commit and push hilbert-polya-structure via SSH
```

The manifest and checker, rather than chat memory, define whether the two
repositories are synchronized.
