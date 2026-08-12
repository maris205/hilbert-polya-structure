# Decision log

## 2026-08-12 — flatten paper-package layout

- Removed the redundant `zeta_mvp0/papers/` container and promoted each
  existing paper package to an immediate `zeta_mvp0/paper_*` directory.
- Kept every paper internally self-contained: manuscript, research records,
  source, tests, validation assets, and result certificates move together.
- Retained historical frozen evidence bytes unchanged.  Absolute paths stored
  in those records describe their original capture environment and are not
  rewritten as if the historical capture had occurred after this relocation.
- Updated repository navigation and ignore rules to the flattened layout.
  Historical path-bound commands, tools, and receipts remain byte-exact and
  therefore fail closed when treated as authority for the relocated tree.
- The published V2 role-5 object remains historical under its original
  `C/H/D/A/P` identity.  Its relocated byte image is not a new canonical
  publication.  Paper 02 has no active role-5 authority at the new root, so
  roles 10 and later, initialization, and scientific dispatch remain stopped
  until a distinct path-aware control generation receives independent review.
- Recorded the exact mapping and control boundary in
  [`PAPER_LAYOUT_MIGRATION_2026-08-12.md`](PAPER_LAYOUT_MIGRATION_2026-08-12.md).

## 2026-08-06 — repository split

- Adopted one paper per subdirectory under `zeta_mvp0/papers/`.
- Preserved the analytic-v3 manuscript as Paper 01 rather than mislabelling
  its historical Round-2 baseline as a second paper.
- Separated the post-freeze Route A4/R400/R401 validated wave-trace story as
  Paper 02.
- Excluded caches, rebuildable native binaries, and large unrelated failed
  FEM/relative-trace arrays from the main Git history.

## 2026-08-06 — A4.13 accepted

- Accepted `R401-VAL-L1-MG-V2 / PASS_LOCAL_MONODROMY_GAP`.
- Replaced unsafe nearest-float bound displays with exact fractions and
  directed decimal floor/ceil payloads.
- Retained V1 as superseded rather than erasing its audit history; its exact
  fraction core remains true, but its human-readable bound labels are
  non-licensing.
- Kept the independent event-projected determinant, Taylor residual, root
  complement, phase cover, global cover, \(\delta_{\rm tr}\), and \(P_0\)
  explicitly open.

## 2026-08-06 — repository organization audit

- Confirmed `zeta_mvp0/papers/` as the only paper-package namespace, with one
  research paper per named subdirectory.
- Confirmed Paper 01 as the sole fully mirrored evidence package at this
  stage.
- Kept Paper 02 as a metadata/manuscript placeholder and deliberately did not
  copy its source, frozen L2 work, or result archives in this step.
- Split mathematical status from repository availability so that a
  source-workspace theorem cannot be mistaken for a result reproducible from
  the present Git repository.
- Required the root README, programme README, and global claim ledger to move
  together when a paper is imported or an evidence boundary changes.

## 2026-08-06 — controlled Paper 02 import

- Imported the Paper 02 source, theorem/protocol records, relevant tests, and
  release-bound A4.12/A4.13 proof objects into its own paper directory.
- Added a read-only release audit that verifies the authoritative provenance
  chains while refusing to treat the superseded monodromy V1 archive as
  licensing evidence.
- Verified 27 Paper 02 package tests and the authoritative release hashes in
  the repository copy.
- Mirrored only the exact executable bound by the authoritative A4.12
  manifest; kept invalid/superseded executables and caches untracked.
- Updated repository availability from `placeholder / transfer pending` to
  `mirrored` without enlarging any mathematical claim.

## 2026-08-06 — L2 complement staging

- Froze `R401-VAL-L2-S0` as a representative six-tree implementation smoke,
  not an all-slab theorem.
- Restricted the smoke to S000, S025, and S050 at 128 and 256 bits; producer
  output has no milestone authority before independent checking and release
  sealing.
- Rejected the first prospective all-slab design for freeze until exact
  scheduling, transactional recovery, 102-tree matrix, raw-proof replay,
  path-safety, and authority contracts are executable and adversarially
  tested.

## 2026-08-06 — A4.14 representative complement accepted

- Accepted `R401-VAL-L2-S0 / PASS_IMPLEMENTATION_SMOKE` after all six frozen
  trees closed at 128 and 256 MPFR bits.
- Recorded 3,016 evaluated nodes, 183 energy-exclusion leaves, 1,349
  return-exclusion leaves, and zero root-candidate, invalid, or unresolved
  leaves.
- Accepted the independent exact-decimal replay after 89,962 checks with
  zero failures and sealed an 18-object release-provenance chain.
- Kept `final_status` null and explicitly refused promotion to the 51-slab
  local-complement theorem, phase/global cover, quantitative trace radius,
  arithmetic trace, Hilbert--Pólya claim, or RH.
- Sent the prospective 102-tree scheduler/checker through a formal-release
  revision.  Its 68 passing synthetic contracts now cover actual evaluator
  binary/CAPD identity, three-layer argv binding, generation-bound
  provenance, write-once authority, and pre-resolution symlink checks.
  Complete crash/quarantine/race/end-to-end tests and a second freeze review
  remain required; held-out slabs remain unread and unexecuted.

## 2026-08-09 — A4.15 all-slab local complement accepted

- Accepted `R401-VAL-L2-A1 / PASS_LOCAL_COMPLEMENT_ALL_SLABS` after all 102
  prospectively frozen trees closed on S000--S050 at 128 and 256 MPFR bits.
- Recorded 52,790 evaluated nodes: 3,368 energy exclusions, 23,435 necessary
  return exclusions, and 25,987 internal splits, with empty frontiers and no
  root candidate, invalid result, timeout, depth exhaustion, node-budget
  exhaustion, or precision-domain disagreement.
- Accepted the independent exact-rational replay after 158,782 checks with
  zero failures and sealed a write-once 19-role release-provenance chain.
- Combined the A1 complement exclusion with the already accepted L1
  existence-and-uniqueness certificate to obtain pointwise reduced-root
  uniqueness in the frozen local box for all 51 slabs.
- Retained `final_status = null` and confined the theorem to the frozen local
  `P_+=0` reduced chart.  The phase/flow-box cover, global return cover,
  independent event-projected determinant/Taylor-width gate, quantitative
  trace radius, endogenous prime trace, Hilbert--Pólya synthesis, zeta-zero
  correspondence, and RH remain open or unauthorized as before.
- Mirrored the compact certificate, aggregate, checker, postcheck, and release
  objects in Git.  Kept the 1.2-GiB raw archive and bulk tree/manifests outside
  ordinary Git; complete raw replay requires a separately transferred
  immutable archive.

## 2026-08-09 — A4.16 representative phase-tube smoke recorded

- Recorded `R401-VAL-L3-S0-COMPOSITE-DRAFT` only as representative
  implementation evidence under `DRAFT_NON_LICENSING`.
- Bound the exact `S000/S025/S050 x 128/256` matrix across two independently
  checked components: 84,172 static phase-anchor nodes with zero unresolved
  leaves and six complete-period CAPD branch-tube records.
- Recorded that the independent composite replay passed all six cells and 18
  manifest/control bindings with zero failures under
  `PASS_IMPLEMENTATION_SMOKE`.
- Retained null milestone, theorem, and final programme values.  A4.15
  remains the highest accepted theorem; the other 48 slabs, arbitrary-orbit
  tube routing, global cover, trace threshold, arithmetic trace,
  Hilbert--Pólya synthesis, zeta-zero correspondence, and RH remain open or
  unauthorized.
- Required independent pre-freeze review and a new prospectively frozen
  51-slab by two-precision production before any A4.16 theorem can be
  considered.
