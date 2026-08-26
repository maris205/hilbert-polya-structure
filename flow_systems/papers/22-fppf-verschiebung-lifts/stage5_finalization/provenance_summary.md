# Provenance and advisory summary

Project: `22-fppf-verschiebung-lifts`  
Stage: `5 — FINALIZE`  
Date: `2026-08-26`

## Final-content binding

- Author-confirmed LaTeX source: `manuscript.tex`, SHA-256
  `e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed`.
- Verified BibTeX database: `references.bib`, SHA-256
  `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093`.
- Reproducible final PDF: `paper.pdf`, SHA-256
  `e030259bb34c6d92af8fd53af80dce0e43200133c9bbdc91efb4f54e8f6c761a`.
- Accepted content proof retained as `content_proof.pdf`, SHA-256
  `20e2d14f5a9e46b7d4f5eafac6669032c72fc69367fdf902e54440816a4a3f04`.
- `pdftotext -layout` SHA-256 for the final PDF and content proof:
  `5bdca519563858a0c084c2315f5f28d0132f0ad9b1459c07294953bfdab64c67`.
- Citation profile: `natbib[numbers,sort&compress] + plainnat`.
- Citation audit: 21 citation commands, 3 unique keys, 3 bibliography
  entries, 0 missing keys, 0 orphan entries, and 0 duplicate keys.
- Stage 4.5 exact integrity boundary: `PASS`; SERIOUS=0, MEDIUM=0,
  MINOR=0. Formatting did not re-open or change the scientific content.

The PDF was built twice in independent temporary directories with
`SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and LuaTeX
optional-info bit 512 suppressed so that its random trailer ID could not make
otherwise identical PDFs byte-different. The two final outputs have the same
SHA-256 shown above.

## Mandatory non-clean advisory disclosures

### #660 tortured-phrase advisory

- Layer: `HEURISTIC-ADVISORY`.
- Evaluation status: `UNMEASURED`.
- Check status: `not_checked`.
- Finding: `unresolved`.
- Reason: `SNAPSHOT_NOT_PROVIDED`.
- Rules evaluated: 0.

This is **not** a clean certificate. No phrase-list snapshot was provided, so
absence of findings cannot be inferred.

### #672 cross-document advisory

- Exact diagnostic: `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`.
- No valid named preregistration sidecar or caller declaration was available.
- No cross-document carrier was written.

This is **not** an agreement result and **not** a clean certificate.

## Route boundary

- Route A: `NOT_TESTABLE`; tuple not assigned; no advancement or Gate A--E
  credit.
- Route B: `ROUTE_B_NOT_TESTABLE`; invocation and entry not authorized; tuple
  not assigned; no Hilbert--Pólya claim and no Gate A--E credit.

The final paper is a completed general mathematical manuscript, not a
Route A/B advancement artifact.

## Input-freeze lifecycle note

`notes/stage5_input_manifest.json` is the immutable pre-promotion input freeze.
Its `accepted_content_proof_pdf` row records the then-current
`paper/paper.pdf` at SHA-256 `20e2d14f...3f04`. Stage 5 intentionally promoted
the final PDF at that current path, so replaying the historical manifest
against current paths now yields 13/14. The exact old bytes are preserved at
`content_proof.pdf` with the original SHA-256, and the final manifest binds both
the retained proof and promoted final PDF. This expected locator transition is
not content drift.

## Submission Package Advisories

The deterministic ARS package verifier was run with the explicitly resolved
`advisory` policy. Its report is fresh for package fingerprint
`ae88ba5618ee5879542b02173e9db72562d0fcd96bddd98096f69d622abd4ac9`.
No `TERMINAL-BLOCK`, `VERIFICATION-INCOMPLETE`, or `STALE-REPORT` token was
emitted.

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

Thus the general paper package closes under the advisory policy, but venue
limits remain explicitly untested. A declared venue profile would require a
fresh venue-specific formatting and package-verification pass.

The verifier was intentionally run without optional `--passport`, `--join-map`,
or `--venue-profile` inputs. The current Material Passport is an output-state
carrier and contains neither `citation_verification_summary[]` nor
`literature_corpus[]`; binding that changing output into the verifier would
create a circular lifecycle without adding a reference join. C1/C2 therefore
remain explicitly labelled as best-effort extraction in the machine report,
while the stronger Stage-4.5 citation audit remains the content-integrity
authority.
