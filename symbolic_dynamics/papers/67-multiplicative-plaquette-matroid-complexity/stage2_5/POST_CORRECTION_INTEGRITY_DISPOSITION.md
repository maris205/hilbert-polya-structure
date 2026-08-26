# P67 post-correction integrity disposition (ARS 0.1.27)

**Audit date:** 2026-08-26 UTC  
**Artifact disposition:** **PASS_WITH_NOTES** for the bounded internal
Stage-2.5 artifact gate; **external release remains HOLD**.  This is neither a
worldwide novelty/priority certificate nor a submission authorization.

## Scope and active material passport

This disposition covers the corrected P67 manuscript package, the current
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

- 11 BibTeX records; 11 distinct cited keys; 17 citation commands and 21
  citation-key mentions.
- 11/11 records and 17/17 citation contexts were checked in the corrected
  Stage-2.5 source/context audit.  Ghost keys: 0; dangling records: 0;
  undefined citations: 0.
- Direct source queries, metadata decisions, and context-level support are in
  `SOURCE_SEARCH_LEDGER.md`, `INTEGRITY_AND_PRIORITY_AUDIT.md`, and
  `CORRECTION_ROUND_1.md`.  Those bounded checks do not imply that the search
  universe is complete.

## C — proof, controls, and experiment boundary

The manuscript is theoretical.  Its finite enumeration program is a
deterministic proof-regression control, not an experiment and not a proof
premise.  The frozen control output remains byte-identical to a live replay
(script SHA-256
`d0a2d3a1bd0c743b375eaf7e2dc98b100ff08f30cd741641cb1fcd81ab98a158`;
stdout SHA-256
`a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26`).
The proof dependencies and the limits of the finite checks remain stated in
the manuscript and proof package.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

Because the active passport declares no experiments, the C4 sentence is a
boundary statement rather than an experimental-quality verdict.

## D1 — corrected-manuscript paragraph screen

The corrected denominator was recomputed over Sections 1--7, excluding the
abstract.  After removing unescaped comments, blank lines delimit blocks;
TeX command tokens do not count as prose; a block enters the denominator when
its rendered-text normalization has at least 20 alphabetic/hyphenated tokens.
This gives **85 body paragraphs**.  The current sample is **26/85 = 30.59%**
and represents every major section.  Queries are exact 8--12-word rendered-
text spans; all were classified `NO_EXACT_MATCH_IN_INDEXED_WEB` in the public
Web searches recorded on 2026-08-26.

| # | Current locator | Exact rendered-text query |
|---:|---|---|
| 1 | `sections/1_introduction.tex:3-7` | Multiplicative symbolic constraints come with more than one natural finite geometry |
| 2 | introduction 9-21 | we isolate one finite-field linear rule and ask for an exact answer |
| 3 | introduction 23-34 | That elementary observation is only the starting point the main result identifies |
| 4 | introduction 127-134 | The proof has three short layers First the multiplicative root decomposition |
| 5 | `sections/2_coordinates.tex:3-8` | The coprimality assumption gives a coordinate system adapted to both multipliers |
| 6 | coordinates 57-68 | Direct substitution proves the converse The gauge formula follows immediately |
| 7 | coordinates 70-76 | The component solution group is therefore explicitly isomorphic to |
| 8 | coordinates 115-119 | The inverse is therefore continuous in the product topology |
| 9 | `sections/3_finite_projections.tex:3-6` | The product homeomorphism solves global extension but it does not |
| 10 | finite projections 29-35 | potentials on the used vertices extend to all row and column indices |
| 11 | finite projections 68-72 | It suffices to check the fundamental cycles relative to any spanning forest |
| 12 | finite projections 140-148 | Finally two distinct arithmetic coordinates produce two distinct edges |
| 13 | `sections/4_prefixes.tex:3-4` | The global free-axis coordinates immediately give the exact prefix law |
| 14 | prefixes 36-44 | the pivot computation below is not by itself an extension theorem |
| 15 | `sections/5_rectangles.tex:3-9` | An exponent rectangle instead stays inside one component and retains |
| 16 | rectangles 39-48 | The pattern exponent has boundary rather than area order |
| 17 | rectangles 91-98 | An added edge is dependent exactly when its endpoints were already connected |
| 18 | rectangles 100-101 | Thus the arbitrary-shape theorem records more than the number of rows |
| 19 | `sections/6_scope.tex:3-4` | The finite-shape theorem sits at the intersection of several established frameworks |
| 20 | scope 19-24 | That affine index geometry is a direct multiplicative-shift neighbor but it |
| 21 | scope 45-56 | Their framework owns the graph-symmetric matroid neighborhood but not the arithmetic |
| 22 | scope 58-63 | After these owners are subtracted the residual P67 statement is the |
| 23 | scope 99-107 | These checks exercise composite coprime multipliers and the characteristic-two sign convention |
| 24 | `sections/7_conclusion.tex:3-7` | The multiplicative plaquette rule has a global set of free coordinates |
| 25 | conclusion 9-16 | The arbitrary finite-shape theorem adds the missing local organization |
| 26 | conclusion 18-28 | A separate choice of action and averaging sequence is required |

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

`claim_registry_round1.json` contains 33 semantic claims: 20 HIGH-IMPACT,
3 RANDOM, and 10 NOT-SELECTED.  All 23 selected claims were checked; the
selection exceeds `min(10,total)`, and
`semantic completeness=not_machine_detectable`.

The selected claims expand, in registry order and exact `ref_slugs` order, to
**27** `evidence-row/1.0` tuples in `evidence_rows_round1.json`:

- 11 cited tuples have nonempty, exact source excerpts, `quote` anchors, and
  `verified_exact_match` replay state;
- 16 selected claims without `ref_slugs` have explicit `none` anchors and
  `anchorless` empty-state excerpts;
- 8 unique source slugs are bound by exact held-session text in
  `evidence_source_map_round1.json`; and
- the ARS 0.1.27 builder/validator and an independent registry-order replay
  both return PASS.  The row verdict count is 27 `VERIFIED`.

The bounded source passages have no human-read attestation in the machine
manifest; their positive status means exact replay against the held source
text, not independent human certification of the whole cited work.  The
builder/source/registry hashes and direct URLs are recorded in
`evidence_source_manifest_round1.json`.

## E6 — claim-strength drift gate

`claim_strength_drift_findings_round1.json` validates against schema
`claim-strength-drift-findings/1.0` and is bound to corrected draft SHA-256
`cce01e567fca31595efe200e1b31b9d652531e200d83e2ac7337e7acc0477e6a`.
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
| 1. Implementation bug passing AI self-review | CLEAR | analytic proofs, two review tracks, and deterministic regression replay agree; controls remain non-premises |
| 2. Hallucinated citation | CLEAR | 11/11 records, zero ghost/dangling keys, 11 cited source tuples replay exactly |
| 3. Hallucinated experimental result | CLEAR | active passport declares no experiments; numerical statements are theorem consequences or disclosed controls |
| 4. Shortcut reliance | CLEAR | global extension, graphic rank/cycle, Haar, prefix, and rectangle claims have explicit proof dependencies |
| 5. Implementation bug reframed as novel insight | CLEAR | correction/review receipts separate repairs from residual claims and retain owner subtraction |
| 6. Methodology fabrication | CLEAR | the theoretical derivation and deterministic control procedure are inspectable; no empirical method is asserted |
| 7. Frame-lock at early pipeline stage | CLEAR | alternate-term searches across multiplicative-shift, mixed-difference, matroid, and correlation vocabularies recovered and integrated omitted owners; no checked neighbor was excluded by the initial framing |

## Residual risk, unresolved declarations, and HOLD

The Mode-7 finding is limited to the checked frame-lock mechanism and does not
imply a complete literature universe.  The exact-neighbor search remains
bounded, collision risk remains **MEDIUM**, and specialist forward/backward
citation review is pending.  Author identity,
author contribution roles, author-approved funding and COI statements, and a
venue-specific author-approved AI-assistance disclosure remain unresolved.
The passport's own verification status is unresolved.  These notes prevent an
unqualified PASS or release authorization.  Canonical `main.pdf` remains the
unchanged 11-page, 408,243-byte artifact with SHA-256
`ed2ffeedc97cc82d006bf540468ef7bf9c1655cad3f4600fb393f8d6451fc7da`.
