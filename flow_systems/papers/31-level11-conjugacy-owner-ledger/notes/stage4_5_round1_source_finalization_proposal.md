# P31 Stage 4.5 Round 1 bounded source-finalization proposal

Status: PROPOSAL ONLY — awaiting explicit Stage 4-prime correction authorization.

This notes-side artifact finalizes the bounded source search for blocker P31-S45R1-I01. It changes no manuscript, bibliography, PDF, science, result, Route, README, canonical artifact, or Stage 4.5 verdict. No passage locator is guessed.

## Bound result

- Registered anchorless citation contexts: 22/22 reviewed.
- Exact locator available for a later authorized block replacement: 7/22.
- Exact supporting passage unavailable at the bounded stop: 15/22.
- Current manuscript contexts changed: 0/22.
- Current Stage 4.5 disposition: FAIL remains unchanged.

## Row ledger

| Source | Context | Exact target | Finalization | Locator or bounded outcome | Later allowed branch |
|---|---|---|---|---|---|
| P31-S01 | P31-CTX-003 | B0021 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | WILEY_FULL_TEXT_ACCESS_BARRIER | replace_block: source-specific metadata narrowing/removal |
| P31-S02 | P31-CTX-004 | B0021 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | JSTOR_SCRIPT_CHALLENGE | replace_block: source-specific metadata narrowing/removal |
| P31-S03 | P31-CTX-005 | B0021 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | WORLD_SCIENTIFIC_ACCESS_BARRIER | replace_block: source-specific metadata narrowing/removal |
| P31-S04 | P31-CTX-006 | B0021 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | WILEY_FULL_TEXT_ACCESS_BARRIER | replace_block: source-specific metadata narrowing/removal |
| P31-S05 | P31-CTX-007 | B0021 | EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT | publisher-deposited Crossref abstract, sentence 1 | replace_block: source-specific locator; preserve aggregate block |
| P31-S06 | P31-CTX-008 | B0021 | EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT | publisher-deposited Crossref abstract, sentence 1 | replace_block: source-specific locator; preserve aggregate block |
| P31-S07 | P31-CTX-009 | B0025 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | JSTOR_SCRIPT_CHALLENGE | replace_block: source-specific metadata narrowing/removal |
| P31-S08 | P31-CTX-010 | B0025 | EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT | publisher-deposited Crossref abstract, sentence 1 | replace_block: source-specific locator; preserve aggregate block |
| P31-S09 | P31-CTX-011 | B0025 | EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT | publisher-deposited Crossref abstract, opening sentence, bounded phrase | replace_block: source-specific locator; preserve aggregate block |
| P31-S10 | P31-CTX-012 | B0025 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | TAYLOR_FRANCIS_ACCESS_BARRIER | replace_block: source-specific metadata narrowing/removal |
| P31-S11 | P31-CTX-013 | B0025 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | ELSEVIER_REDIRECT_ONLY | replace_block: source-specific metadata narrowing/removal |
| P31-S12 | P31-CTX-014 | B0025 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | JSTOR_SCRIPT_CHALLENGE | replace_block: source-specific metadata narrowing/removal |
| P31-S13 | P31-CTX-015 | B0025 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | WILEY_FULL_TEXT_ACCESS_BARRIER | replace_block: source-specific metadata narrowing/removal |
| P31-S15 | P31-CTX-016 | B0029 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | WILEY_FULL_TEXT_ACCESS_BARRIER | replace_block: source-specific metadata narrowing/removal |
| P31-S16 | P31-CTX-017 | B0029 | EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT | publisher-deposited Crossref abstract, sentence 1 | replace_block: source-specific locator; preserve aggregate block |
| P31-S17 | P31-CTX-018 | B0029 | EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT | publisher-deposited Crossref abstract, algorithm sentence | replace_block: source-specific locator; preserve aggregate block |
| P31-S18 | P31-CTX-019 | B0029 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | IOP_OFFICIAL_ENDPOINT_ACCESS_BARRIER | replace_block: source-specific metadata narrowing/removal |
| P31-S19 | P31-CTX-020 | B0029 | EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT | American Mathematical Society official PDF page 1, Pell’s Equation opening discussion | replace_block: source-specific locator; preserve aggregate block |
| P31-S20 | P31-CTX-021 | B0029 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | BOOK_PREVIEW_NO_PROJECT_FIT_PASSAGE | replace_block: source-specific metadata narrowing/removal |
| P31-S14 | P31-CTX-022 | B0032 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | ELSEVIER_REDIRECT_ONLY | replace_block: source-specific metadata narrowing/removal |
| P31-S21 | P31-CTX-023 | B0032 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | NO_FIT_PASSAGE_ADJUDICATED | replace_block: source-specific metadata narrowing/removal |
| P31-S22 | P31-CTX-024 | B0032 | EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY | ELSEVIER_REDIRECT_ONLY | replace_block: source-specific metadata narrowing/removal |

## Guardrails

P31 groups several citations inside four aggregate blocks. A later replacement must update the entire named block atomically under its exact old hash, preserve every unaffected source mapping in that block, and never infer a missing passage. Locator-available rows may bind only the retained excerpt and locator. Explicit-unavailability rows must narrow or remove that source-specific substantive attribution and may retain only an honest metadata-level corpus description.

The proposed edits, if later authorized, require a fresh Stage 4.5 audit and cannot promote this manuscript.

Machine-readable companion: stage4_5_round1_source_finalization_proposal.json
