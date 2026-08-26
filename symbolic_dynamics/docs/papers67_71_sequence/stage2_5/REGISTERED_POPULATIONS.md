# Stage 2.5 registered audit populations

Registration date: `2026-08-26`  
Protocol: all high-impact claims plus a deterministic random sentinel and a
top-up to at least ten selected claims when needed.

## Reference and claim populations

| Paper | bibliography population | claim-registry population | high-impact | random sentinel | not selected |
|---|---:|---:|---:|---:|---:|
| P67 | 8 | 30 | 16 | 3 | 11 |
| P68 | 4 | 31 | 20 | 3 | 8 |
| P69 | 3 | 31 | 25 | 3 | 3 |
| P70 | 5 | 32 | 22 | 3 | 7 |
| P71 | 7 | 42 | 26 | 3 | 13 |
| **Total** | **27** | **166** | **109** | **15** | **42** |

The random seed is recorded by the registry builder as
`<paper>:stage2.5:2026-08-26`.  Each registry stores exact byte spans and the
raw SHA-256 of its claim view.  All five registries pass schema validation and
exact replay.  The mechanical detector reports zero unregistered candidates
among its bounded classes (`citation_bearing_sentence` and
`quantitative_sentence`).

The mechanical result is deliberately not promoted into a semantic
completeness claim.  Every coverage report records
`semantic_extraction_coverage: not_machine_detectable`; the independent
semantic selection and the paper-specific claim/evidence ledger remain part
of the human audit.

## Other registered populations and boundaries

- Citation-key population: all 27 bibliography records; no dangling citation
  key and no uncited bibliography record at freeze time.
- Citation-context population: every in-manuscript context attached to those
  records, with at least 30% independently sampled per paper and all contexts
  checked where practicable.
- Originality population: body paragraphs, stratified by major section; at
  least 30% and at least one paragraph per major section.
- Numerical/data-surface population: all tables, equations presented as
  finite enumerations, and deterministic-script claims.  These five papers
  declare no experiments or empirical results.
- Self-plagiarism search: `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE` because no
  author identities or prior-work corpus was provided.
- Optional cross-model external upload: `NOT_AUTHORIZED` and not performed.
- External posting, submission, author/journal contact, circulation, or
  priority claim: `HOLD`.

## Post-correction Round-1 registered populations

The table above is the immutable Round-0 registration.  Bibliography and
claim populations were re-extracted after the objective source-boundary edits;
the Round-1 registries preserve their own raw hashes and exact rebase reports.

| Paper | final references | Round-1 claims | high-impact | random sentinel | not selected | selected claims | exact tuples | source-bound | anchorless |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| P67 | 11 | 33 | 20 | 3 | 10 | 23 | 27 | 11 | 16 |
| P68 | 4 | 31 | 20 | 3 | 8 | 23 | 23 | 3 | 20 |
| P69 | 7 | 38 | 32 | 3 | 3 | 35 | 37 | 12 | 25 |
| P70 | 7 | 35 | 27 | 3 | 5 | 30 | 34 | 13 | 21 |
| P71 | 9 | 42 | 26 | 3 | 13 | 29 | 31 | 8 | 23 |
| **Total** | **38** | **179** | **125** | **15** | **39** | **140** | **152** | **47** | **105** |

All 140 selected Round-1 claims expand in registry order to 152 schema-valid
`(claim_id, ref_slug, anchor)` rows.  Forty-seven rows bind exact excerpts from
session-held external source text; 105 no-reference tuples preserve an explicit
`anchorless` empty state; zero rows use the manuscript itself as a source.  All
five coverage reports replay `PASS`, with zero mechanical candidate gaps and
`semantic_extraction_coverage: not_machine_detectable`.  Evidence-row
validation establishes provenance fidelity only; it is not an independent
truth, execution, novelty, or priority judgment.  An anchorless row likewise
does not establish external support or prove the manuscript claim.

The Round-0 high-impact selections rebased without unresolved claims: P67
16/16, P68 20/20, P69 25/25, and P70 22/22. P71 rebased 24/26; the other two
old source-boundary claims were explicitly superseded by corrected owner-
boundary claims, leaving zero unresolved items.
