# Paper28 manuscript/validator successor build delta

Date: 2026-09-05. Prospective local implementation; this controller has not
performed preflight or a build. User confirmation permits a separately versioned
source and validator successor, independent review, then one fresh two-root
build. It does not alter previous source/capture/review records or authorize
a retry in any existing root.

## Inherited contract

This delta incorporates HERMETIC_BUILD_EC_PLAN_20260905.md, SHA-256
34c85c0050d1d21d03e923d7136a6071c51879912aa1024f3727807e8d714fcb,
and the underlying HERMETIC_BUILD_PLAN_20260905.md, SHA-256
dddff3b541e91d8175934e64a551f74d6ad74a55de9232e617e655076e322be8.
Its code predecessor HERMETIC_BUILD_EC_20260905.py remains SHA-256
25ab27f749f1585405b927ffc62d5a8b322ad283f45e08fa32704fafc2f76553.
Only the source/validator identities, new control/root names and explicit
source-provenance separation below supersede those original provisions.
The new file contains its own controlled flow; it does not execute or modify
a frozen predecessor, introduce an adapter or make an arbitrary-build API.

The captured dependency namespace, loader, four TeX/BibTeX passes, remaining
inspection commands, environment, resource limits, chroot and privilege/process
ownership, no-follow materialization, log checks, dual-root equality and failure
preservation remain unchanged. The validator command changes only the reviewed
script name. Original page, bibliography, metadata/anonymity, link/action and
visual/final-integrity acceptance requirements still apply; the new source and
validator review must show that the authorized corrections do not lower them.
Existing failures, source/locks, both dependency recordings and accepted Paper27
remain preserved. No host fallback, installation, recapture, external effect or
new resource budget is introduced.

## Two distinct source roles

Historical CAPTURE_SOURCES contains the original three pins:

- main.tex: SHA-256
  bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e,
  73733 bytes, LF1605.
- math_commands.tex: SHA-256
  16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5,
  444 bytes, LF14.
- references.bib: SHA-256
  e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e,
  6104 bytes, LF204.

Their actual original directory remains `project/paper`. CAPTURE2's manifest
sources and the EC outcome sources must equal this historical binding, never
the successor binding. Their existing outcome/audit/archive hashes remain
unchanged; no capture is relabelled as having read or certified the new source.
The original trio is also reread and matched before/after each child and in the
opening/closing checks, with explicit failure reporting if it changes.

The actual publication SOURCE directory is
`project/paper-successor-20260905`. Its separate exact main.tex hash/byte/LF
pins are finalized in the new controller before review. The macro and bibliography
pins must still equal the original values above, enforced in preflight. Source
review also checks the stated unchanged package/import scope. Only this new trio
is copied into isolated /source and used by the commands, PDF validator, per-child
source checks, materialized-source verification and final publication binding.
Thus a historical capture-source PASS is never presented as a review of the new
manuscript, and an unchanged new /source never substitutes for preserving the old
capture provenance.

At authoring, the new main.tex and validator pins may have explicit PENDING
values. Preflight rejects an unfinalized hash before opening a build root.
The final executable-profile review binds the actual finished source/control
hashes, not those placeholders; this statement is not an extra review round.

The independent new-source review is SOURCE_SUCCESSOR_REVIEW_20260905.md.
Its completed exact SHA-256 is pinned separately and included in the administrative
control bindings/evidence copies; the old static source review is not promoted
to a review of the new manuscript. Initial main.tex pins may be updated while
that review is active; all five administrative bindings are finalized before
the executable-profile review.

## Validator, root and review delta

New controls are HERMETIC_BUILD_SUCCESSOR_20260905.py and this plan,
with PDF_ACCEPTANCE_SUCCESSOR_20260905.py as the separately reviewed and
hash-pinned validator. LOADER_SELECTION_20260905.json remains SHA-256
ecc5e3751def20eac1bb96a2ddb5336925d46cf8fcb80b5ee60f4ab25bed9606.
The copied /control member and validator argv use the successor script name;
all its other execution arguments and namespace checks are unchanged.

The sole new root is
`project/build-capsule-successor-20260905`, containing evidence/r0/r1,
created exclusively after preflight and the exact independent review.
No old build root is inspected, reused, repaired or rerun.

The review path is HERMETIC_BUILD_SUCCESSOR_REVIEW_20260905.json.
Its supplied SHA-256 and EXECUTABLE_PROFILE_REVIEW_PASS decision must bind the
five administrative controls (including the new-source review), new publication
sources, separate capture_sources, original
CAPTURE2 audit/outcome and the unchanged ec_supplement report. An old source or
build review cannot authorize the new source/validator identities.

The preflight schema is paper28-build-successor-preflight-v1. Its sources field
means the new publication trio; capture_sources means the verified original
trio. Both directory names are explicit. Per-child intents retain both bindings.
Closing contracts compare both roles and all prior capture/supplement/control
seals. Failure records separately attempt new-source, original-source and
EC-supplement rebinds; unavailable checks remain errors, not invented matches.
Successful automated outcome distinguishes publication source_unchanged from
capture_sources_unchanged and still grants no final local acceptance.

## Bounded implementation verification

Before execution, use code-only AST/diff checks and the existing pure-memory
self-test. The added source-role test uses in-memory byte fixtures to accept
each source under its own pins and reject the new bytes under historical pins.
No test needs host dependency reads or an existing build root. Actual preflight,
independent final hash binding and execution are later governed actions; no
planned or static result is reported as an actual PDF/build PASS.
