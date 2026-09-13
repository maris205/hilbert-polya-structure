# Paper28 EC-supplement build delta

Date: 2026-09-05. Prospective successor; no preflight or build has run.
The single-file capture actually exited0. At plan authoring, its independent
recording audit was pending; the controller's explicit audit-hash placeholder
must be replaced with the completed audit hash before executable-profile review
and execution. This authoring-time status does not create a second audit gate.

## Inherited contract and authority

The user confirmed the narrow EC supplement and requested instruction
optimization first; that instruction audit is complete. This delta addresses
only the actual first-pass request for ecrm1095.tfm. It does not authorize wider
recapture, a larger budget, manuscript changes, host fallback, old-root access
or external publication.

The unchanged contract is incorporated from HERMETIC_BUILD_PLAN_20260905.md,
SHA-256 dddff3b541e91d8175934e64a551f74d6ad74a55de9232e617e655076e322be8.
Its predecessor controller HERMETIC_BUILD_20260905.py has SHA-256
3081c6c677fac2ac4adca4fe34066289708875e9280bce2a035a517653a1b098.
Only the explicit changes below supersede those original names and bindings.
The new controller contains its own complete controlled flow; it does not
execute the frozen predecessor or introduce an adapter or generic file API.

The original manuscript identities, CAPTURE2 seals, loader selection, PDF
validator, environment, fixed commands/passes, resource limits, chroot and
privilege/process-ownership predicates, log/PDF/visual acceptance conditions,
namespace verification and cross-root equality remain unchanged. There is no
weaker substitute for any original predicate. In particular:

- PDF_ACCEPTANCE_20260905.py remains SHA-256
  e173a8a54d051f8d296b5d1319a44bdea0f30d3ab0be91cc16747027bf9a126c.
- LOADER_SELECTION_20260905.json remains SHA-256
  ecc5e3751def20eac1bb96a2ddb5336925d46cf8fcb80b5ee60f4ab25bed9606.
- Original failures, CAPTURE2, source/locks and accepted Paper27 stay unchanged.
  Build failure preserves the new root without retry or fallback. Automated
  success still requires visual disposition and independent final integrity
  before local anonymous acceptance; it is not submission or external release.

## Exact supplemental input

The sole new publication input is ecrm1095.tfm from
`notes/dependency-ec-supplement-20260905`, materialized at
`/usr/share/texlive/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm`.
The absolute target is namespace metadata, never a live-host read by this build.

Actual capture: 3584 bytes, LF12, original mode0o644, file SHA-256
6a3850cd71bbb2f43d98b7eb6b47f925de25626f5f4a0648c2d9d7b4b774eb2a.
Its outcome.json SHA-256 is
507016423515267d4ab5ab55e9e08cc2818391a4f4e00ec803b3870d75645535.
The capture's 4096-byte budget remains within the original unchanged 2 GiB
limit. Its actual decision remains EC_METRIC_CAPTURED_AUDIT_PENDING; a separate
`notes/EC_SUPPLEMENT_AUDIT_20260905.md` supplies the later recording verdict,
bound by exact hash rather than changing that historical outcome.

Validate the established outcome fields: fixed source_path, budget_bytes4096,
host_bytes_read3584, unchanged manuscript sources, exact file metadata and
no_retrytrue. Rehash its six exact sealed outputs: intent.json,
independent-review.json, attempt.json, metadata-before.json,
metadata-after.json and ecrm1095.tfm. Bind outcome/audit bytes and hashes,
capture-control bindings and those actual output seals. No additional metric,
full recapture, merged archive, font generation or speculative dependency is
included; a new actual missing input is reported as a new failure.

## Namespace delta

First inventory the original 6838 CAPTURE2 entries without modification.
Add exactly one file entry and any missing real ancestors to the existing
synthesized-directory set; reject duplicate target or non-directory ancestor.
The namespace has 6839 captured-content entries, including 6051 regular files;
synthetic parents are not tar members.

archive_check strictly validates the unchanged original 6838-member tar set,
excluding the fixed supplemental target, with all original metadata/byte/PAX
checks and 199 PAX path members. Then it separately verifies the snapshot's
3584 bytes/hash/LF and invokes the same verified-data consumer. The unchanged
namespace_file/parent_fd helpers write it exclusively with no-follow dirfds
before symlinks. It becomes root-owned0444; synthesized parents are real
root-owned0555 directories under the existing transform. No symlink ancestor
is followed or inserted. Existing pre/post namespace snapshots and verification
include the new file and parents without changing their predicates.

## Fresh root, review and evidence

Only HERMETIC_BUILD_EC_20260905.py and this plan are new build controls.
Their control set also includes the unchanged PDF validator and loader JSON.
The independent review is `notes/HERMETIC_BUILD_EC_REVIEW_20260905.json`;
its exact supplied hash and EXECUTABLE_PROFILE_REVIEW_PASS decision bind the
four controls, original manuscript and CAPTURE2 audit/outcome, plus an exact
ec_supplement object. That object contains target, file metadata, outcome/audit
lengths and hashes, six output seals, capture-control bindings and capture
budget/byte count. An old review cannot authorize these new control hashes.

The sole new execution root is
`papers/28-primitive-selector-cycle-monodromy/build-capsule-ec-20260905`,
containing evidence/r0/r1, exclusively created only after the complete
preflight and review binding. No old root is probed, reused or repaired.
Opening and closing contracts seal the same supplemental object as well as
the unchanged base/source/control bindings. Failure recording attempts its
own supplement rebind and records a mismatch or check failure explicitly.
Unfinalized hashes fail before root creation. No successor execution is
authorized merely by the capture's exit0 or this plan's existence.
