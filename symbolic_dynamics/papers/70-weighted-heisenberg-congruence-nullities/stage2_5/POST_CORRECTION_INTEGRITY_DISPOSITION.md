# P70 post-correction integrity disposition (ARS 0.1.27)

**Audit date:** 2026-08-26 UTC  
**Artifact disposition:** **PASS_WITH_NOTES** for the bounded internal
Stage-2.5 artifact gate; **external release remains HOLD**.  This is neither a
worldwide novelty/priority certificate nor a submission authorization.

## Scope and active material passport

This disposition covers the corrected P70 manuscript package, the current
Round-1 claim registry, and the strict evidence-row artifacts.  No manuscript
source or PDF was changed in this closure.  The active passport is the single
workspace record
`docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml` (SHA-256
`097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`).
It declares `experiment_intake_declaration.status: no_experiments_declared`,
with `experiment_provenance: []` and `experiment_alignment_results: []`.
The batch passport is marked `verification_status: VERIFIED` only for the
completed bounded Stage-2.5 integrity gate; it does not infer any additional
human declaration, priority clearance, or release authorization.

## A/B — bibliographic records and citation contexts

- 7 BibTeX records; 7 distinct cited keys; 14 citation commands and 16
  citation-key mentions.
- 7/7 records and 14/14 citation contexts were checked in the corrected
  Stage-2.5 source/context audit.  Ghost keys: 0; dangling records: 0;
  undefined citations: 0.
- Direct source queries, metadata decisions, and context-level support are in
  `SOURCE_SEARCH_LEDGER.md`, `INTEGRITY_AND_PRIORITY_AUDIT.md`, and
  `CORRECTION_ROUND_1.md`.  Those bounded checks do not imply that the search
  universe is complete.

## C — proof, controls, and experiment boundary

The manuscript is theoretical.  Its finite matrix program is a deterministic
proof-regression control, not an experiment and not a proof premise.  The
frozen control output remains byte-identical to a live replay (script SHA-256
`a476ddddca2d9373c1412039e86dac64457354740e530ff3e20ab7ade4e5b1e1`;
stdout SHA-256
`fe26d12a4fd332b87027db685563980b788fb097bd633dc974b091de0bc2f42f`).
The left/right convention is proved analytically; nullity-only whole-matrix
checks are not claimed to distinguish the dual convention.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

Because the active passport declares no experiments, the C4 sentence is a
boundary statement rather than an experimental-quality verdict.

## D1 — corrected-manuscript paragraph screen

The corrected denominator was recomputed over Sections 1--8, excluding the
abstract.  After removing unescaped comments, blank lines delimit blocks;
TeX command tokens do not count as prose; a block enters the denominator when
its rendered-text normalization has at least 20 alphabetic/hyphenated tokens.
This gives **46 body paragraphs**.  The current sample is **14/46 = 30.43%**
and represents every major section.  Queries are exact 8--12-word rendered-
text spans; all were classified `NO_EXACT_MATCH_IN_INDEXED_WEB` in the public
Web searches recorded on 2026-08-26.

| # | Current locator | Exact rendered-text query |
|---:|---|---|
| 1 | `sections/1_introduction.tex:3-10` | Periodic configurations convert an infinite symbolic constraint into a finite linear problem |
| 2 | introduction 31-37 | That algorithmic framework and its representation ledger are prior |
| 3 | introduction 39-50 | The answer has two qualitatively different pieces The one-dimensional representations behave |
| 4 | `sections/2_setup.tex:17-25` | This is a closed shift-invariant linear group shift |
| 5 | setup 60-63 | Their different scales are essential the character term is at most |
| 6 | `sections/3_regular_decomposition.tex:3-4` | We first remove a possible field splitting ambiguity |
| 7 | regular decomposition 52-60 | The shift matrix cyclically permutes all eigenspaces so a nonzero invariant |
| 8 | `sections/4_character_blocks.tex:3-5` | The following calculation identifies it over the ground field |
| 9 | `sections/5_nonlinear_blocks.tex:9-10` | another primitive root which will not change the calculation below |
| 10 | nonlinear blocks 35-36 | A determinant alone would not determine the fixed-space dimension |
| 11 | `sections/6_phase_diagram_controls.tex:3-5` | The family therefore lives naturally in the projective coefficient plane |
| 12 | phase diagram/controls 69-76 | They can expose many transcription or implementation mistakes including an omitted |
| 13 | `sections/7_scope_declarations.tex:12-19` | Degenerate two-term rules admit separate elementary case splits but are outside |
| 14 | `sections/8_conclusion.tex:11-14` | The failure of semisimplicity should replace the two-stratum ledger by a |

`NO_EXACT_MATCH_IN_INDEXED_WEB` means only that an exact phrase was not seen
in the inspected indexed results.  General public-Web search is not Turnitin,
iThenticate, Crossref Similarity Check, a subscription corpus, or a complete
historical archive.  It can miss paywalls, non-indexed text, OCR/TeX
normalization, translations, and paraphrases, and it can return false
positives.  This phase cannot certify originality.

**D2:** `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.  The manuscript identifies
the author only as Anonymous, so no author-publication overlap query can be
run responsibly.

## E1/E3.1 — semantic claims and strict source tuples

`claim_registry_round1.json` contains 35 semantic claims: 27 HIGH-IMPACT,
3 RANDOM, and 5 NOT-SELECTED.  All 30 selected claims were checked; the
selection exceeds `min(10,total)`, and
`semantic completeness=not_machine_detectable`.

The selected claims expand, in registry order and exact `ref_slugs` order, to
**34** `evidence-row/1.0` tuples in `evidence_rows_round1.json`:

- 13 cited tuples have nonempty, exact source excerpts, `quote` anchors, and
  `verified_exact_match` replay state;
- 21 selected claims without `ref_slugs` have explicit `none` anchors and
  `anchorless` empty-state excerpts;
- 7 unique source slugs are bound by exact held-session text in
  `evidence_source_map_round1.json`; and
- the ARS 0.1.27 builder/validator and an independent registry-order replay
  both return PASS.  The row verdict count is 34 `VERIFIED`.

The bounded source passages have no human-read attestation in the machine
manifest; their positive status means exact replay against the held source
text, not independent human certification of the whole cited work.  The
builder/source/registry hashes and direct URLs are recorded in
`evidence_source_manifest_round1.json`.

## E6 — claim-strength drift gate

`claim_strength_drift_findings_round1.json` validates against schema
`claim-strength-drift-findings/1.0` and is bound to corrected draft SHA-256
`7945d73d2bdede0ec36743b71ccbaf34f91baadf2363a5a3c85bcaf5509b2ec7`.
Its status is `skipped_no_revision_evidence`: no ARS Revision-Evidence Bundle
or `revision_patch_round*.json` exists in the dispatch scope, so a semantic
before/after drift reconstruction was not invented.  The bundle hash is null
and the findings array is empty.  This is a valid empty-state artifact, not a
completed no-drift finding.

## Seven AI-research failure modes

Only the protocol vocabulary `CLEAR`, `SUSPECTED`, and
`INSUFFICIENT EVIDENCE` is used.

| Mode | Status | Evidence-bound disposition |
|---|---|---|
| 1. Implementation bug passing AI self-review | CLEAR | analytic proofs, two review tracks, and deterministic matrix replay agree; controls remain non-premises |
| 2. Hallucinated citation | CLEAR | 7/7 records, zero ghost/dangling keys, 13 cited source tuples replay exactly |
| 3. Hallucinated experimental result | CLEAR | active passport declares no experiments; numerical statements are theorem consequences or disclosed controls |
| 4. Shortcut reliance | CLEAR | representation ledger, action convention, determinant, corank, descent, and regular multiplicity are proved explicitly |
| 5. Implementation bug reframed as novel insight | CLEAR | correction/review receipts separate convention/control repairs from the residual theorem and owner subtraction |
| 6. Methodology fabrication | CLEAR | the theoretical derivation and deterministic control procedure are inspectable; no empirical method is asserted |
| 7. Frame-lock at early pipeline stage | CLEAR | alternate-term searches across finite convolution, representation, congruence-nullity, clock--shift, and algebraic-action vocabularies recovered and integrated omitted owners; no checked neighbor was excluded by the initial framing |

## Residual risk, unresolved declarations, and HOLD

The Mode-7 finding is limited to the checked frame-lock mechanism and does not
imply a complete literature universe.  The exact-neighbor search remains
bounded, collision risk remains **MEDIUM-HIGH**, and specialist
forward/backward citation review is pending.
Author identity, final contribution roles, author-approved funding and COI
statements, and a venue-specific author-approved AI-assistance disclosure
remain unresolved.  The passport's own verification status is unresolved.
These notes prevent an unqualified PASS or release authorization.  Canonical
`main.pdf` remains the unchanged 7-page, 345,028-byte artifact with SHA-256
`61398af7a4ab61ea3ace029ec315721d4a855bf8f60986c84b2fdc94d9bd0142`.
