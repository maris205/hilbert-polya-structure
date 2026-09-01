# P26 Stage 5 provenance summary

## Input and authority

- Content confirmation: exact response `确认`, recorded 2026-09-01 UTC in
  `notes/stage5_content_confirmation_20260901.md`.
- Locked TeX SHA-256:
  `fca2b382c3d64273ccb6c17d63330ecfad20ff02087b001175c1003bb4006fd3`.
- Locked bibliography SHA-256:
  `dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f`.
- Confirmed content-proof SHA-256:
  `402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da`.

The confirmation authorizes format finalization and package audit only. It
does not authorize scientific, declaration, citation-style, subtype, Route,
canonical-paper, or result changes.

## Deterministic build provenance

Two independent temporary builds used
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, followed
the same LuaLaTeX--BibTeX--LuaLaTeX--LuaLaTeX command sequence, and produced
byte-identical PDFs. The retained final SHA-256 is
`2e7b0deb7e9bda399d155f514d6f3fdcc89e5d463082456817da91bfca0792c5`.
The 16-page `pdftotext -layout` stream has SHA-256
`67805a2b582713a79755b5c8074dac91e793754f2bb7fd179d8e4bfcd8b74444`,
identical to the confirmed proof. Build-A logs and auxiliary files are retained
under `notes/stage5_build_artifacts/`.

All 18 PDF font programs are embedded. The five text/CJK/italic/monospace font
rows carry Unicode maps; thirteen Computer Modern Type-1 mathematical subsets
report `uni=no`, matching the confirmed proof's font map. This is recorded as
a technical limitation, not presented as a clean all-font ToUnicode result.

## Scientific and Route boundary

The unchanged scientific result is the exact `2/2/134` taxonomy on 138
registered Hecke output instances and the 51/55 failures of each primary law.
The result remains finite and does not establish a global primitive census or
determinant. The project is still at the early Route-A A0--A1 / A1--A2
frontier; positive-arithmetic A2 is `0/5` across the batch and Route B
invocations are `0/5`. The Route evaluator SHA-256 values remain
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
