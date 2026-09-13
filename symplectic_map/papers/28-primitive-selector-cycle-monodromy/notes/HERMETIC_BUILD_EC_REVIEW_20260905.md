# Paper28 EC successor: independent exact-profile review

Date: 2026-09-05. Decision: `EXECUTABLE_PROFILE_REVIEW_PASS`.
No blocking finding in the one-EC-snapshot delta.

The machine-consumed review is `HERMETIC_BUILD_EC_REVIEW_20260905.json`.
It binds the exact controller SHA-256
`25ab27f749f1585405b927ffc62d5a8b322ad283f45e08fa32704fafc2f76553`,
delta-plan SHA-256
`34c85c0050d1d21d03e923d7136a6071c51879912aa1024f3727807e8d714fcb`,
unchanged loader/validator/manuscript identities, CAPTURE2 audit/outcome and
the complete supplemental input object.

## Checks and evidence

- Read the final delta plan fully and compared the final controller diff and
  AST against the hash-verified frozen predecessor. Relative to the preliminary
  logic review, the controller only finalizes the supplemental constants.
- The original 6838 entries and 6050 regular files remain; the fixed EC snapshot
  adds one regular file and only needed real structural ancestors. Duplicate
  targets and non-directory ancestors are rejected. The unchanged no-follow
  materializer writes the snapshot before installing symlinks.
- Source, loader, validator, environment, fixed commands, limits, chroot,
  privilege drop, process ownership, namespace checks, auxiliary convergence,
  log/PDF acceptance and raw cross-root comparison are preserved. New binding
  checks cover opening, review authorization, materialization, closing and
  best-effort failure recording. No host fallback, old-root reuse or retry was
  added.
- Independently rehashed all four build controls, the three actual source files
  with byte/LF counts, frozen predecessor code/plan, CAPTURE2 outcome/audit and
  manifest, supplement outcome/audit, its six sealed outputs and both capture
  controls. Their relevant identities exactly match the supplied preflight.
- Read the independently authored supplement audit, whose exact SHA-256 is
  `887fa0213c9a6866fc1ca7a4da0fd1fa951461c788a44b4e061818d7881f9a70`;
  it reports `EC_SUPPLEMENT_RECORDING_INTEGRITY_PASS`. The historical capture
  outcome remains unchanged. The plan's authoring-time pending statement does
  not create a separate gate after this completed audit.
- The actual supplied `HERMETIC_BUILD_EC_PREFLIGHT_20260905.json` reports
  `PREFLIGHT_PASS_NOT_EXECUTED`, 6838 base members, one supplement, 199 PAX path
  members and 6051 regular files. Its independently checked SHA-256 is
  `c4aa7b781b0957a7984e24b24fa30a8aa21240fdf2ba2dac0b506a402e855be1`.
  The completed base archive/census verification is taken from that actual
  preflight; this reviewer did not redundantly rescan the base archive.

## Boundary

This reviewer ran only read-only local code/binding checks, not the controller,
its preflight, any capture or build. No build root, old failure directory or
live-host font content/metadata was accessed. Only the two new review documents
were written. This review neither changes the implementation nor claims
runtime isolation testing or scientific manuscript review.

PASS is confined to the exact reviewed one-shot executable profile and the
already established authority/contract. It is not build/PDF success, assurance
that no further dependency is missing, visual approval or final local anonymous
acceptance. The original post-build checks and preserved-failure rules remain.
