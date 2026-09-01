# Paper 24 Stage-5 provenance and advisory summary

Project: `24-bianchi-holonomy-flow`  
Stage: `5 — FINALIZE`  
Date: `2026-09-01 UTC`

## Final-content binding

- Confirmed finalization source: `manuscript.tex`, SHA-256
  `153e80d360b35c25cac8f0ad2fc1cea14ba43afed07ce7fbb59b9f48c7baeb4e`.
- Accepted bibliography: `references.bib`, SHA-256
  `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87`.
- Scholar-confirmed proof: `content_proof.pdf`, SHA-256
  `7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea`.
- Final PDF: `paper.pdf`, SHA-256
  `8d690aa887c9aed27e1070b6bc840de333ff2d2de9f81a79945a034401025eeb`.
- Final/proof `pdftotext -layout` SHA-256:
  `f72efc209a139b7eb586b4db5b5b2ab9f8850d4728931c6c9f0882359c073931`.
- Citation profile: `natbib[numbers,sort&compress] + plainnat`.

The exact scholar response `确认`, dated 2026-09-01 UTC, confirms the retained
proof and authorizes the final PDF, package audit, and FULL Stage-5 completion
checkpoint. Stage 5 is format-only: the canonical `paper/` and `results/`
trees, manuscript science, declarations, bibliography content, flow
restriction, and Route state were not modified.

## Entry advisories

### #660 phrase-list screening advisory

- Layer: `HEURISTIC-ADVISORY`.
- Measurement: `UNMEASURED`.
- Status: `not_checked`.
- Reason: `SNAPSHOT_NOT_PROVIDED`.

This is nonblocking but not clean. It supports no absence, provenance, origin,
or publisher-acceptance inference.

### #672 cross-document advisory

- Exact state: `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`.
- Carrier written: no.

This is nonblocking but is not an agreement or clean result.

## Route boundary

Paper 24 remains at early Route-A A0–A1. The proxy tuple is unchanged:
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; the complete
Bianchi flow remains `UNASSIGNED`. Route B is uninvoked. Batch arithmetic is
positive A2 `0/5` and Route-B invocations `0/5`; 19 model instances are not
independent samples. No Route or gate advancement follows from formatting.
The unchanged evaluator hashes are
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
for Route A and
`170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`
for Route B.

## Font and conversion boundary

All 17 PDF fonts are embedded. Five CID text fonts have explicit Unicode maps;
12 legacy Computer Modern Type-1 math subsets do not advertise ToUnicode in
`pdffonts`. The package therefore does not claim all-font ToUnicode coverage;
instead, complete Unicode text extraction is bounded by the exact proof/final
`pdftotext -layout` hash equality. Pandoc/DOCX remains withheld because the
preflight trial was materially lossy for theorem, mathematics, and citation
structure.

## Submission Package Advisories

The ARS verifier ran under explicitly resolved `advisory` policy. Report
fingerprint:
`f4aa2e5407a3b43aee5fe9900b514395112bba1a8a118d7791245eda390512c3`.
The following are every `fail`, `warn`, or `not_checked` row in the report;
there are no `fail` or `warn` rows.

- `B1`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
  - location: none
- `B2`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
  - location: none
- `B3`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
  - location: none
- `B4`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
  - location: none
- `B5`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
  - location: none

The report's C1/C2 best-effort reference checks pass 7/7 in both directions;
A1–A7 are not applicable because no anonymized variant or double-blind venue
profile was supplied. B1–B5 remain explicitly untested. This package is not a
venue-readiness, submission, public-release, or scientific-correctness
certificate.
