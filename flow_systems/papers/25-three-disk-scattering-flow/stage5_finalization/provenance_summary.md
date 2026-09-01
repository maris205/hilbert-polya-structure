# Paper 25 Stage-5 provenance and advisory summary

Project: `25-three-disk-scattering-flow`  
Stage: `5 — FINALIZE`  
Date: `2026-09-01 UTC`

## Final-content binding

- Confirmed finalization source: `manuscript.tex`, SHA-256
  `9c7782ebf6a90f0e33ab86f2e77d7ce78ecfb2ad0ddb9413e4829cfe33f776e1`.
- Accepted corrected derived bibliography: `references.bib`, SHA-256
  `a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab`.
- Scholar-confirmed proof: `content_proof.pdf`, SHA-256
  `34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65`.
- Final PDF: `paper.pdf`, SHA-256
  `5968230a947956744c41d542a833e8cc165a0610980bb8bcdb3fed31c4f0198f`.
- Final/proof `pdftotext -layout` SHA-256:
  `60aedb5e593ad6971ed37cda6206e2eab0aefc5653064f10f516f9208408b185`.
- Citation profile: `natbib[numbers,sort&compress] + plainnat`.

The exact scholar response `确认`, dated 2026-09-01 UTC, confirms the retained
proof and authorizes the final PDF, package audit, and FULL Stage-5 completion
checkpoint. Stage 5 is format-only: the canonical `paper/` and `results/`
trees, canonical bibliography, manuscript science, declarations, flow
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

## Bibliographic update note

The fresh Stage-4.5 source audit identified the linked erratum for
`GaspardRice1989Exact`, DOI `10.1063/1.457670`. It corrects Eq. (5.4) and
Appendix equations/typography. Both current manuscript contexts cite the
abstract and Sections II–III only for the multiple-scattering matrix/determinant
characterization, so the recorded impact assessment found those contexts
unaffected. This is a bounded context assessment, not an all-source clean or
no-update certificate.

## Route boundary

Paper 25 remains at the early Route-A A1–A2 typed symbolic-calibrator layer.
Its tuple is unchanged:
`(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` and the
arithmetic route remains rejected; the physical-flow tuple is `UNASSIGNED`.
Route B is uninvoked. Batch arithmetic is positive A2 `0/5` and Route-B
invocations `0/5`; 19 model instances are not independent samples. No Route
or gate advancement follows from formatting. The unchanged evaluator hashes
are
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
`782aa5e54234d906212175917a0ceec92d8da305d1bb797e734941f1f7d3d967`.
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

The report's C1/C2 best-effort reference checks pass 8/8 in both directions;
A1–A7 are not applicable because no anonymized variant or double-blind venue
profile was supplied. B1–B5 remain explicitly untested. This package is not a
venue-readiness, submission, public-release, or scientific-correctness
certificate.
