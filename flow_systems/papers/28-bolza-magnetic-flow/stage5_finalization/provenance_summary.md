# Provenance and advisory summary

Project: `28-bolza-magnetic-flow`  
Stage: `5 — FINALIZE`  
Date: `2026-09-01`

## Final-content binding

- Confirmed LaTeX source: `manuscript.tex`, SHA-256
  `14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22`.
- Verified BibTeX database: `references.bib`, SHA-256
  `95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e`.
- Reproducible final PDF: `paper.pdf`, SHA-256
  `be156f76fcf3f31ecdc2d8be5dde5ccf7aaf7f0b530c7dc8efc9b889e3633cc9`.
- Accepted content proof: `content_proof.pdf`, SHA-256
  `253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382`.
- Final/proof `pdftotext -layout` SHA-256:
  `2e7c021043d9d5e00e561bcc134a047df00f957d39b91bf48fd856f74861f1ff`.
- Citation profile: `natbib[numbers,sort&compress] + plainnat`.
- Citation closure inherited from the byte-locked preflight source: 9 citation
  commands, 6 unique keys, 6 BibTeX entries, and 0 missing, orphan, or
  duplicate keys.
- Stage-4.5 Round-2 integrity boundary: `PASS`; references 6/6, citation
  contexts 9/9, registered claims 95/95, and evidence tuples 104/104.

Two independent builds under `SOURCE_DATE_EPOCH=1788220800`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, and LuaTeX optional-info suppression produced
byte-identical final PDFs.  Scientific content, declarations, bibliography,
subtype, canonical source/result trees, and Route state were not changed.

## Font and render advisory

All 17 fonts are embedded and subsetted; five text/CJK fonts have explicit
ToUnicode maps.  The 12 legacy Computer Modern Type-1 math fonts report
`uni=no`, the same profile as the accepted proof.  This is a bounded
accessibility advisory, not a claim of complete per-font ToUnicode coverage.
The final and proof text-extraction streams are nevertheless byte-identical.
Visual review covered all 14 pages through a `pdfpages` contact rendering and
found no layout defect.

## Mandatory non-clean advisory disclosures

### #660 tortured-phrase advisory

- Layer: `HEURISTIC-ADVISORY`.
- Evaluation status: `UNMEASURED`.
- Check status: `not_checked`.
- Finding: `unresolved`.
- Reason: `SNAPSHOT_NOT_PROVIDED`.
- Rules evaluated: 0.

This is **not** a clean certificate.  No phrase-list snapshot was provided,
so absence of findings cannot be inferred.

### #672 cross-document advisory

- Exact diagnostic: `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`.
- No valid named preregistration sidecar or caller declaration was available.
- No cross-document carrier was written.

This is **not** an agreement result and **not** a clean certificate.

## Scientific and Route boundary

The exact nonarithmeticity result, finite completeness certificate, and exact
systole chain form a positive control.  Magnetic/arithmetic transfer is not
claimed.  P28 remains in Route A's early control-infrastructure layer: its
formal tuple is unassigned, the batch positive-arithmetic A2 count is `0/5`,
Route-B invocations are `0/5`, and 19 recorded model instances are not
independent statistical samples.  Route-file hashes remain:

- `skills/route-a-evaluator.md`:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- `skills/route-b-evaluator.md`:
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

Stage-5 completion is not a Route promotion, venue-readiness certificate,
submission, release, external contact, or Git action.  Stage 6 remains
pending.

## Submission Package Advisories

The deterministic ARS submission-package verifier was run under the resolved
`advisory` policy.  Its package fingerprint is
`27fa855909de6309c11203cc40842b2077ee31aaaa5496b7e4194be4c6a367a4`.
The report contains no `fail` or `warn` row.  Every `not_checked` row is
transcribed below; `not_applicable` rows are intentionally excluded by the
ARS carrier contract.

- `B1`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
- `B2`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
- `B3`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
- `B4`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`
- `B5`
  - family: `venue_limits`
  - status: `not_checked`
  - signal_class: `deterministic`
  - detail: `no venue profile declared — limits are never guessed from the journal name (R-L3-2-D mirror)`

The verifier was intentionally run without `--passport`, `--join-map`, or
`--venue-profile`.  C1 and C2 therefore use explicitly labelled best-effort
LaTeX/BibTeX extraction and both pass at 6/6.  Stage-4.5's stronger 104-tuple
evidence audit remains the scientific provenance authority.  Venue-limit
status remains unknown until a scholar declares a venue profile; no venue
compliance or submission readiness is inferred.
