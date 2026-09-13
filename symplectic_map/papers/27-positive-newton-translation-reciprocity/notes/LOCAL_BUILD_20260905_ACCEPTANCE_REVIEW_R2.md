# Local build acceptance-code prebuild review — revision 2

Reviewed SHA256: 49fba6fa53a6ecf7f4ebd23b2dca72db2a1079d83437088cf89b0c94e6936a9a
Decision: PASS

Date: 2026-09-05 (UTC)
Scope: targeted independent prebuild code re-review of the complete 680-line
`LOCAL_BUILD_20260905.py`, the complete 176-line regression test file, and the
updated local plan, against the retained substantive contract reviewed in R1.
The approved local-control replacement and single-writer assumption remain
premises. This is not a build execution, PDF/artifact review, mathematics review,
or release-grade publication decision. The original hash-bound FAIL report is
preserved unchanged.

## Closure of previous findings

1. **R1 F1 closed.** Lines 395–399 exempt only the two exact known normal
   diagnostic-mode header spellings, with zero or one leading space. Genuine
   error text, including text appended to that otherwise-normal header, still
   fails. Regression `test_normal_diagnostic_header` covers both positive
   spellings and an appended-real-error negative. The change does not alter
   publication argv or waive real TeX errors.

2. **R1 F2 closed.** Lines 366–370 permit exactly one `./` prefix before applying
   the unchanged local filename allowlist. `../main.aux`, `./../main.aux`, and
   `././main.aux` remain rejected by the regression. Recorder snapshots remain
   raw bytes, and cross-root normalization at lines 585–587 remains exclusively
   the corresponding absolute root prefix replacement. No additional recorder
   content normalization was introduced.

3. **R1 F3 addressed at the intended automated/independent-review boundary.**
   Lines 445–447 now reject the known section, theorem-clause, boundary, and
   conclusion anchors in the reference suffix. The regression exercises every
   such anchor, including the previous repeated-Introduction counterexample.
   The plan explicitly reserves full reference-suffix and layout inspection
   for mandatory independent artifact review and expressly does not claim
   semantic completeness for these anchor checks. Accordingly this bounded
   prebuild review does not require a generic proof-prose classifier and does
   not interpret `OUTPUT_CHECKS_PASS` as final publication acceptance.

## Additional changed code

- Lines 265–328 catch ordinary command-communication failures/cancellation,
  perform bounded TERM/KILL cleanup of the spawned process group, drain/reap
  where possible, close the pipes, and capture status plus cleanup information.
  An unknown child return code raises `ChildUnreaped`; lines 667–671 record a
  no-restart HOLD rather than continuing or claiming success. Tests cover
  cancellation, already-exited process-group races, timeout escalation,
  unreaped-child HOLD, and the ordinary success path. This is bounded ordinary
  cleanup review, not a claim of recovery after arbitrary process termination.
- Lines 79–85 and 246–253 bind 17 explicitly named installed PyMuPDF Python/
  shared-library files by aggregate SHA256
  `66cb425ff3a012c077f5ee1f8b8e7019f8f4d8c471635a2cfc98acdbb3ee6a2b`.
  The binding is checked in initial preflight and before/after PDF parsing
  (lines 458, 528, and 643), and is included in acceptance comparison. The
  parser remains read-only and version-restricted. No PDF rewriting, extra
  publication pass, installation, or external transmission was introduced.
- The fixed four publication commands, snapshots, source/tool/dependency
  rebindings, root-file universe, sentinel/page limits, twenty-key citation
  census, strict substantive diagnostic rejection, warning preservation,
  metadata/font/security/text checks, and exact cross-root manifest projection
  retain the behavior examined in R1. No new blocking acceptance defect was
  found in this targeted re-review.

## Verification performed independently

All Python invocations used `-I -B`. No build/evidence pathname was opened,
listed, or statted; no publication command, old runner, `--build`, network
operation, or PDF write was performed. Mocked command tests used no real child
process or real process-group signal.

- `LOCAL_BUILD_20260905_TEST.py`: all 18 test methods passed, including their
  table-driven subcases.
- `LOCAL_BUILD_20260905.py --self-test`: PASS; 2 positive and 11 negative cases.
- `LOCAL_BUILD_20260905.py --preflight`: exit zero; source/tool bindings,
  87 logical/86 final dependencies, and the specified PDF runtime hash passed.
  Returned dependency-frame SHA256:
  `27f807a21bce6c72d09f189b200c1212d3629ef4550d9ad203740eef4a8fb726`.
- Final production-script rehash remained exactly the Reviewed SHA256 above.
  Regression-file SHA256:
  `a7315da3cc603e9a8163ec33d40922b3c02ce0833cd9d53f8f33caf9037744b7`.

This PASS closes the acceptance-code prebuild concerns for this exact candidate
only. The new build still must satisfy its runtime predicates and subsequent
independent artifact, warning, typography, mathematics/citation, and evidence
review. It does not change any prior failure or authorize retries, reuse,
cleanup, or publication.
