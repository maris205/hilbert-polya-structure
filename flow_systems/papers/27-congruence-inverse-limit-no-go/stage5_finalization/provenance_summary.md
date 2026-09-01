# P27 Stage 5 provenance summary

## Input and authority

- Content confirmation: exact response `确认`, recorded 2026-09-01 UTC in
  `notes/stage5_content_confirmation_20260901.md`.
- Locked TeX SHA-256:
  `bbac2f5dd43149348c33da883e2b7fe0d342abdf932723ea859edf70d46d5e48`.
- Locked bibliography SHA-256:
  `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981`.
- Confirmed content-proof SHA-256:
  `087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208`.

The confirmation authorizes format finalization and package audit only. It
does not authorize scientific, declaration, citation-style, subtype, Route,
canonical-paper, or result changes.

## Deterministic build provenance

Two independent temporary builds used
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, followed
the same LuaLaTeX--BibTeX--LuaLaTeX--LuaLaTeX command sequence, and produced
byte-identical PDFs. The retained final SHA-256 is
`6b82701f253ab452b4c6be1c7f27dd6ff24267f5609317743492889834b40684`.
The 13-page `pdftotext -layout` stream has SHA-256
`5f02152c13d9f36fd9163cbe2906572ae52aa9bc282d5ea979165ea536bb114b`,
identical to the confirmed proof. Build-A logs and auxiliary files are retained
under `notes/stage5_build_artifacts/`.

All 18 PDF font programs are embedded. The five text/CJK/italic/monospace font
rows carry Unicode maps; thirteen Computer Modern Type-1 mathematical subsets
report `uni=no`, matching the confirmed proof's font map. This is recorded as
a technical limitation, not presented as a clean all-font ToUnicode result.

## Scientific and Route boundary

The unchanged scientific result is the aperiodicity of the residual
congruence inverse-limit flow and the exact fixed-panel `Q11` calibration for
a separate nonresidual homology-cover object. Both objects retain their
rejected Route-A tuples; no Route credit transfers between them. The project
is still at the early Route-A A0--A1 / A1--A2 frontier;
positive-arithmetic A2 is `0/5` across the batch and Route B invocations are
`0/5`. The Route evaluator SHA-256 values remain
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and
`170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

## Existing nonblocking advisories

- `#660`: `not_checked/SNAPSHOT_NOT_PROVIDED`.
- `#672`: `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`.

Both are nonblocking but non-clean. They are transcribed without
reinterpretation and do not support a clean-manuscript inference.

## Scope and readiness boundary

No venue profile was provided, so venue-limit checks cannot establish venue
conformance. This package makes no venue-readiness, submission, acceptance, or
public-release claim. The submission-package advisories below are mechanical
transcriptions from the ARS verifier report under advisory policy.

## Submission Package Advisories

Policy: `advisory`. The verifier report contains no `fail` or `warn` row. It
contains the following five `not_checked` rows; they are nonblocking but do not
constitute venue conformance. No location was supplied for any row.

- `B1`; family `venue_limits`; status `not_checked`; signal class
  `deterministic`. Detail: `no venue profile declared — limits are never
  guessed from the journal name (R-L3-2-D mirror)`.
- `B2`; family `venue_limits`; status `not_checked`; signal class
  `deterministic`. Detail: `no venue profile declared — limits are never
  guessed from the journal name (R-L3-2-D mirror)`.
- `B3`; family `venue_limits`; status `not_checked`; signal class
  `deterministic`. Detail: `no venue profile declared — limits are never
  guessed from the journal name (R-L3-2-D mirror)`.
- `B4`; family `venue_limits`; status `not_checked`; signal class
  `deterministic`. Detail: `no venue profile declared — limits are never
  guessed from the journal name (R-L3-2-D mirror)`.
- `B5`; family `venue_limits`; status `not_checked`; signal class
  `deterministic`. Detail: `no venue profile declared — limits are never
  guessed from the journal name (R-L3-2-D mirror)`.
