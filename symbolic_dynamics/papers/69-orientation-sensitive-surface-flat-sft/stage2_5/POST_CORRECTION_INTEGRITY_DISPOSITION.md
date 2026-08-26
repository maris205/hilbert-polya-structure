# P69 post-correction integrity disposition

Date: 2026-08-26 (UTC)  
Protocol: ARS-Codex academic-research-suite 0.1.27, strict Stage 2.5 closure  
Manuscript: *Orientation-Sensitive Periodic Spectra of Surface-Group Flat-Connection Shifts*  
Posture: author-side integrity closure, not independent or specialist review  
External release: **HOLD**

## 1. Disposition

The strict Phase-E tuple gate is **PASS**.  The active claim registry has
38 claims, of which all 32 HIGH-IMPACT claims and three RANDOM claims are
selected.  Exact registry-order expansion produces 37 evidence rows: 12 rows
contain positive, session-held excerpts from the registered cited sources and
25 no-reference claims have explicit anchorless empty-state rows.  There are
zero manuscript-self evidence rows.  All 35 selected claims carry claim-level
verdict `VERIFIED` (37 VERIFIED rows, because two claims have two references).
Every row validates against the ARS 0.1.27 evidence-row contract, and the observed
tuple order equals the registry-derived order.

The overall post-correction integrity disposition is **PASS_WITH_NOTES**, not an
unqualified PASS.  The notes are substantive boundaries:

- 25 selected claims have no registered external reference.  Their claim-level
  verdict is `VERIFIED` by the current internal proof/proof-control audit, while
  their evidence excerpt remains correctly `anchorless`; that empty excerpt does
  not create or upgrade external provenance and does not make the manuscript
  evidence for itself.
- E6 claim-strength-drift output is schema-valid but has status
  `skipped_no_revision_evidence`: no authorized Revision-Evidence Bundle exists.
  The empty findings array is not evidence that no semantic drift occurred.
- D2 is `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`.
- Collision risk remains **MEDIUM** under a bounded literature search.  No
  worldwide priority, specialist, or release clearance is granted.
- Authorship, contributions, funding, competing interests, author-overlap
  screening, and human release authorization remain unresolved.

Consequently, the Stage-2.5 content checkpoint is cleared and Stage 3 is
**ELIGIBLE ONLY AFTER EXPLICIT USER CONFIRMATION**.  The schema-valid E6 skip is
the prescribed branch when no prior block-anchored revision evidence exists;
specialist collision review and human declaration/release decisions remain
separate downstream review or external-release gates and are not silently
satisfied here.

No manuscript source, bibliography source, control source, or PDF was changed in
this strict-closure pass.  `main.pdf` remains 11 A4 pages, 377,379 bytes, SHA-256
`93462a17e92207d9dfbccc55d6ac543391c55a8950d5057a50e9a3b9996c2766`.

## 2. Active material and experiment authority

The active batch passport/declaration pointer is exactly:

`docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`

Its SHA-256 is
`097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`.
It declares a theoretical manuscript batch, `no_experiments_declared`, an empty
`experiment_provenance` list, and deterministic scripts as
`proof_regression_controls_not_experiments`; external release is `HOLD`.  The
passport's own `verification_status` is `VERIFIED` for this bounded Stage-2.5
gate.  That status does not duplicate, extend, or infer declarations from the
empty provenance.  The P69 package's older `DECLARATIONS.md` is package-local
historical metadata, not a replacement for the active batch passport.

## 3. Current content identity

### 3.1 Source-bundle hash

The current source-bundle digest is
`4b5662953e295cf61e9a0bfcf8b5a0d89651778da522e90196300eaad27a85be`.
It was computed by:

1. taking `main.tex`, `references.bib`, every `sections/*.tex`, and every
   `code/*.py` file (12 files total);
2. sorting their workspace-relative POSIX paths bytewise;
3. emitting one byte-exact line per file in GNU `sha256sum` form,
   `<64 lowercase hex><two spaces><workspace-relative path>\n`;
4. SHA-256 hashing the complete 1,693-byte, 12-line stream.

The bundle intentionally excludes generated PDFs, build products, frozen control
output, QA receipts, and Stage 2.5 audit sidecars.

### 3.2 Claim view and registry

The current claim view is
`stage2_5/draft_for_claim_registry_round1.md`, 34,047 UTF-8 bytes, with raw-file
SHA-256
`276cb82f2fcb4d2aaa70a609bb999c0297261ad1fbfd870e3785fc2b08c8760b`.
The active registry is `stage2_5/claim_registry_round1.json`, 27,954 bytes,
SHA-256
`a183b820506a697012a6b1cbe43a4918125a57920cdf7c7ef1407cddfcc4c5ba`.
The claim-view hash is the SHA-256 of the file's raw bytes, with no text
normalization.  The registry records that same digest as its draft identity.

## 4. Phases A and B: all references and citation contexts

The current bibliography has seven entries.  All seven are cited, all cited keys
exist, and no duplicate key is present.  Static source extraction finds 12 citation
commands/contexts, 14 key mentions, and seven unique keys.  The current compiled log
has zero undefined citations or references.  Ghost citations: 0.  Dangling
bibliography records: 0.

### 4.1 Reference records

| Ref slug | Direct source surface used for record/context verification | Record verdict |
|---|---|---|
| `Klug2025` | Cambridge published record/full text: <https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/counting-homomorphisms-from-surface-groups-to-finite-groups/C523AC49DFABB67F60E13A19BBF11F52> | VERIFIED |
| `CarrollPenland2015` | New York Journal of Mathematics: <https://nyjm.albany.edu/j/2015/21-36.html> | VERIFIED |
| `CohenGoodmanStrauss2017` | EMS Press: <https://ems.press/journals/ggd/articles/14944> | VERIFIED |
| `Snyder2007` | arXiv: <https://arxiv.org/abs/math/0703073> | VERIFIED |
| `LiebeckShalev2005` | DOI: <https://doi.org/10.1112/S0024611504014935>; author text: <https://www.ma.imperial.ac.uk/~mwl/chardeg3.pdf> | VERIFIED |
| `Ward1998` | UEA institutional title/abstract: <https://research-portal.uea.ac.uk/en/publications/a-family-of-markov-shifts-almost-classified-by-periodic-points/> | VERIFIED |
| `Roettger2005` | Elsevier DOI/PII coredata: <https://api.elsevier.com/content/article/pii/S0022314X04002549?httpAccept=text/xml> | VERIFIED_WITH_ACCESS_NOTE |

For Roettger, the author publication page's purported paper PDF was opened and found
to be a different paper; it was excluded.  The session-held Elsevier surface exposes
the genuine title/core metadata but not the article abstract.  The positive strict
evidence therefore uses only the publisher title, “Periodic points classify a family
of Markov shifts,” and does not manufacture an abstract excerpt.

### 4.2 Twelve citation contexts

| ID | Current source location | Citation claim checked | Source-side disposition |
|---|---|---|---|
| B01 | `sections/1_introduction.tex:26-28` | Carroll--Penland: general group-shift finite-index periodic organization | VERIFIED against NYJM article page/text |
| B02 | `sections/1_introduction.tex:28-30` | Cohen--Goodman-Strauss: finite-type symbolic systems on surface groups | VERIFIED against EMS title/abstract |
| B03 | `sections/1_introduction.tex:33-43` | Ward almost-classification and Roettger completion in the distinct finite-abelian `Z^2` Markov-shift family | VERIFIED jointly from Ward's institutional title/abstract and the genuine Roettger publisher title, with the access note above |
| B04 | `sections/1_introduction.tex:45-48` | Snyder: lattice-TQFT proof route for orientable and nonorientable surface formulas | VERIFIED against arXiv abstract |
| B05 | `sections/1_introduction.tex:49-51` | Klug: chosen modern normalization account, not historical ownership | VERIFIED against Cambridge published account |
| B06 | `sections/2_background.tex:55-57` | Klug Corollary 1 and displays following Theorem 3.1 | VERIFIED; current pinpoint is exactly “Theorem 3.1” |
| B07 | `sections/2_background.tex:57-58` | Snyder: separate topological/combinatorial derivation | VERIFIED against arXiv abstract |
| B08 | `sections/5_moment_recovery.tex:83-85` | inverse character-degree sums are standard zeta values | VERIFIED against Liebeck--Shalev text |
| B09 | `sections/7_scope_controls.tex:13-16` | Klug modern-source/historical-owner boundary | VERIFIED against Cambridge published account |
| B10 | `sections/7_scope_controls.tex:17-19` | Snyder already supplies the lattice-TQFT route | VERIFIED against arXiv abstract |
| B11 | `sections/7_scope_controls.tex:19-20` | character-degree zeta setting | VERIFIED against Liebeck--Shalev text |
| B12 | `sections/7_scope_controls.tex:26-32` | Ward/Roettger as conceptual periodic-recovery neighbors, not the P69 surface-group theorem | VERIFIED jointly with the same Roettger access limitation as B03 |

The A/B disposition is **PASS_WITH_NOTES**: all 7 records and all 12 contexts have
direct support, while the Roettger source-access limitation is explicitly preserved.
No cited source is used to prove P69's original reconstruction theorem or any priority
claim.

## 5. Phase C: mathematical controls and disclosure boundary

`python3 code/verify_surface_flat_sft.py` terminates with `ALL CHECKS PASS`.
`code/verify_surface_flat_sft.out` and `qa/control_replay.txt` are byte-identical,
with SHA-256
`c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d`.
The script SHA-256 is
`1acc02c0d8fce337660c6c8b655a0803a8d856febaf721a37e299572ac3ac4e1`.

The replay covers group axioms, character/indicator signatures, direct orientable
and nonorientable homomorphism enumeration, fixed-law comparison, `D8/Q8`
orientation-sensitive separation, the `C3` indicator-zero trichotomy and
reconstruction, and an `S3` independent-order check.  These finite checks are proof
regression controls.  They are not experiments, statistical evidence, or premises
for the general theorem.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

That required C4 sentence is retained verbatim even though the active passport
declares no experiments; it records the protocol boundary and must not be read as an
assertion that an experiment exists.

## 6. Phase D: current paragraph-overlap census

The current D1 census uses blank-line-delimited blocks with at least 20 alphabetic
words after documented TeX/comment normalization.  It finds 70 narrative paragraph
units across the abstract and Sections 1--8.  The protocol floor is
`ceil(0.30 * 70) = 21`; 24 units were searched, or 34.2857%, and all nine section
files are represented.  Each query is an exact 8--12-word string from the current
source.  Every search was run against the general indexed web on 2026-08-26.

| ID | Current source location | Exact query | Result |
|---|---|---|---|
| D01 | `sections/0_abstract.tex:1-21` | “Finite moment inversion shows that the two spectra jointly determine” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D02 | `sections/1_introduction.tex:4-9` | “This makes the topology of the corresponding finite covers available” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D03 | `sections/1_introduction.tex:33-43` | “Periodic data already recover a finite-group parameter in a distinct” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D04 | `sections/1_introduction.tex:45-51` | “this bibliographic choice does not alter historical ownership” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D05 | `sections/1_introduction.tex:105-119` | “The inverse step is a finite exponential-moment problem” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D06 | `sections/2_background.tex:22-27` | “This criterion will be important because it is the same” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D07 | `sections/2_background.tex:45-59` | “our chosen modern normalization source, we use Klug's account” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D08 | `sections/2_background.tex:76-81` | “We do not reprove this character calculation, and we make no” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D09 | `sections/3_flat_shift.tex:36-47` | “There are finitely many forbidden patterns on this set” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D10 | `sections/3_flat_shift.tex:90-94` | “Every connection has a unique based gauge transform whose labels” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D11 | `sections/3_flat_shift.tex:114-120` | “The full gauge group can have stabilizers governed by centralizers” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D12 | `sections/4_subgroup_counts.tex:4-10` | “We retain all positive moduli because both parities of the” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D13 | `sections/4_subgroup_counts.tex:44-46` | “This prevents the orientation comparison from being hidden in unrelated” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D14 | `sections/5_moment_recovery.tex:20-30` | “The reduced rational function on the right has simple poles” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D15 | `sections/5_moment_recovery.tex:32-38` | “When the bases are known, moments with nonnegative indices” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D16 | `sections/5_moment_recovery.tex:76-89` | “We use this standard finite-group expression at positive even integers” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D17 | `sections/5_moment_recovery.tex:167-170` | “The orientable moments alone cannot distinguish characters of equal degree” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D18 | `sections/6_dihedral_quaternion.tex:17-40` | “The two-dimensional indicators have opposite signs. This can be checked” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D19 | `sections/6_dihedral_quaternion.tex:69-76` | “separation holds at every odd level, not only at the first one” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D20 | `sections/7_scope_controls.tex:13-24` | “The residual proof sequence in this manuscript begins with the” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D21 | `sections/7_scope_controls.tex:92-95` | “This finite enumeration can detect normalization or parity regressions” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D22 | `sections/7_scope_controls.tex:99-103` | “That negative search is not a priority result” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D23 | `sections/8_conclusion.tex:4-11` | “The flat-connection SFT converts finite-index fixed points into raw flat” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D24 | `sections/8_conclusion.tex:13-18` | “Several boundaries are deliberate. The recovered signature is not a” | NO_EXACT_MATCH_IN_INDEXED_WEB |

D1 verdict: **PASS_WITH_TOOL_LIMITATIONS**.  The machine-readable census is
`stage2_5/d1_current_census.json`, SHA-256
`adb98c7c00f364d1b4a8fc7afa47808c29ebd4b9a627cdef97241386a4233078`.

D2 status is exactly:

`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`

The search surface is a general indexed web, not Turnitin, iThenticate, Crossref
Similarity Check, a subscription full-text corpus, or a complete historical
archive.  Exact-string queries can miss paywalls, unindexed documents, OCR and
TeX/math normalization, translations, paraphrases, and alternate terminology.
Therefore a no-match result is a bounded retrieval result, not a plagiarism or
originality certificate.

## 7. Phase E: semantic registry and strict evidence replay

`semantic completeness=not_machine_detectable`

The registry contains 38 claims: 32 HIGH-IMPACT, three RANDOM, and three
NOT-SELECTED.  All HIGH-IMPACT claims and all RANDOM claims are selected, satisfying
the `min(10,total)` floor.  A selected claim with references expands to one row per
ordered ref slug; a selected claim with no references expands to one explicit
anchorless row.  This gives 37 expected and 37 observed rows in exact registry order.

### 7.1 Positive cited-source tuples

| Row | `(claim_id, ref_slug, anchor kind)` | Genuine session-held excerpt |
|---|---|---|
| 0002 | `(P69-R1-CAND-002, CohenGoodmanStrauss2017, quote)` | “Strongly aperiodic subshifts on surface groups” |
| 0003 | `(P69-R1-CAND-003, Roettger2005, quote)` | “Periodic points classify a family of Markov shifts” |
| 0004 | `(P69-R1-CAND-003, Ward1998, quote)` | “A family of Markov shifts (almost) classified by periodic points” |
| 0005 | `(P69-R1-CAND-004, Snyder2007, quote)` | “The main tool is an elementary invariant of surfaces attached to a semisimple algebra called a lattice topological quantum field theory.” |
| 0006 | `(P69-R1-CAND-005, Klug2025, quote)` | “proof is structured so that the corresponding results for closed and possibly orientable surfaces, as well as some generalizations, are derived using the same methods.” |
| 0017 | `(P69-R1-CAND-008, Snyder2007, quote)` | “Here we present a greatly simplified proof of these results which uses only elementary topology and combinatorics.” |
| 0024 | `(P69-R1-CAND-011, LiebeckShalev2005, quote)` | “and define the ‘zeta function’ ζH(t) = P χ∈Irr(H) χ(1)−t for real t > 0.” |
| 0029 | `(P69-R1-CAND-014, Klug2025, quote)` | same exact Klug source excerpt as row 0006 |
| 0030 | `(P69-R1-CAND-015, Snyder2007, quote)` | same exact Snyder source excerpt as row 0005 |
| 0031 | `(P69-R1-CAND-016, LiebeckShalev2005, quote)` | same exact Liebeck--Shalev source excerpt as row 0024 |
| 0032 | `(P69-R1-CAND-017, Roettger2005, quote)` | “Periodic points classify a family of Markov shifts” |
| 0033 | `(P69-R1-CAND-017, Ward1998, quote)` | “The compact zero-dimensional set XG carries a natural shift Z2-action sG and the pair SG = (XG,sG) is a two-dimensional topological Markov shift.” |

Every positive anchor decodes to an exact contiguous substring of the corresponding
session-held source packet.  Each excerpt is at most 25 words.  Source packets are
bound by SHA-256 in the rows and their direct URLs/capture surfaces are recorded in
`stage2_5/evidence_source_inventory_round1.json`.  No excerpt comes from P69 itself.

### 7.2 Explicit no-reference empty states

The 25 selected no-reference claims are:

`P69-SEM-001`, `P69-SEM-002`, `P69-SEM-003`, `P69-SEM-004`,
`P69-SEM-005`, `P69-SEM-006`, `P69-SEM-007`, `P69-SEM-008`,
`P69-SEM-009`, `P69-SEM-010`, `P69-SEM-011`, `P69-SEM-012`,
`P69-SEM-013`, `P69-SEM-014`, `P69-CAND-006`, `P69-CAND-007`,
`P69-SEM-015`, `P69-CAND-008`, `P69-SEM-016`, `P69-SEM-017`,
`P69-CAND-009`, `P69-CAND-011`, `P69-SEM-018`, `P69-SEM-019`, and
`P69-SEM-020`.

Each has `source.ref_slug = null`, `anchor.kind = none`, an empty encoded/decoded
anchor, `excerpt.state = anchorless`, and claim-level verdict `VERIFIED`.  The
verdict is inherited from the current internal proof/proof-control audit at the
registered paper locator; the empty excerpt remains the required no-reference
evidence state.  Claim verdict and excerpt provenance are separate fields: the
verdict does not turn an anchorless row into source evidence and does not replace
the internal proof audit.

### 7.3 Replay receipts

| Artifact | Count/boundary | SHA-256 |
|---|---|---|
| `stage2_5/evidence_rows_round1.json` | 37 VERIFIED rows; 12 positive, 25 anchorless, 0 self-source, 0 serious verdicts | `b094e0edd17f00e221b0b507c954aabdef5813f99c2b5ce72df8d7201b96bd90` |
| `stage2_5/evidence_source_map_round1.json` | six unique session-held source packets | `4d56f3748b24938a6aedb85cba8e7633371141be16bed17c2aae2f3e0f941f60` |
| `stage2_5/evidence_source_inventory_round1.json` | direct URLs, capture surfaces, source hashes | `28546196dfb8777ebf538ac5228e2112262927cfcdd5509540405b9066a8540b` |
| `stage2_5/evidence_tuple_replay_round1.json` | 37/37 exact ordered tuple replay; 35/35 selected claims VERIFIED; schema validation PASS | `faabf3baceed133cf1eda5edffff21f015d8503b68fcb24a7635b16abbbe1c8b` |

The source-map count is six rather than seven because no selected registry tuple
uses `CarrollPenland2015`; Carroll--Penland is nevertheless included in the complete
7-record/12-context A/B audit above.

### 7.4 E6 exact-schema sidecar

`stage2_5/claim_strength_drift_findings_round1.json` validates against the exact
`claim-strength-drift-findings/1.0` JSON schema.  Its SHA-256 is
`3fc83321dc858c80faf5348e44f0120d25e3fc9a284ca186ce7ab2fc55ba0f19`.
It records:

- `status = skipped_no_revision_evidence`;
- final-draft SHA-256
  `276cb82f2fcb4d2aaa70a609bb999c0297261ad1fbfd870e3785fc2b08c8760b`;
- `revision_evidence_bundle_sha256 = null`;
- model-mediated detection provenance and the protocol hash; and
- an empty `findings` array.

ARS prohibits reconstructing or guessing a Revision-Evidence Bundle.  Thus this is
the truthful, schema-valid first-pass branch because no prior block-anchored
revision evidence exists.  It is non-blocking for this checkpoint, but is not a
completed semantic drift audit and not evidence of absence of claim-strength
drift.  A future request for completed E6 review would require an authorized
Revision-Evidence Bundle and a fresh sidecar.

## 8. Owner subtraction and collision boundary

The source/search ledger records alternate-term searches through 2026-08-26 for
lattice gauge/configuration shifts, surface-group SFTs and group shifts,
Mednykh/Frobenius--Schur homomorphism formulas, orientation-sensitive cover spectra,
and character-degree/indicator moment recovery.  The principal owner subtraction is:

- Mednykh and Frobenius--Schur own the classical surface homomorphism formulas;
  Klug is the chosen modern normalization account, and Snyder owns a
  lattice-TQFT derivation route.
- Carroll--Penland owns general finite-index periodic organization for group SFTs;
  Cohen--Goodman-Strauss owns a surface-group SFT existence line.
- Ward and Roettger own periodic-data recovery/classification for their distinct
  finite-abelian-parameter Ledrappier-type algebraic `Z^2` Markov-shift family.
- Liebeck--Shalev supplies representation-zeta context for inverse character-degree
  sums; finite Vandermonde inversion and standard `D8/Q8/C3` character calculations
  are not claimed as standalone contributions.

The residual P69 candidate is the combined explicit `N3` flat-edge SFT, two
divisibility-directed surface-cover families, rooted raw fixed-count identity, and
joint recovery of group order plus the multiset of character degree and
Frobenius--Schur indicator.  No exact collision for that complete combination was
found within the bounded search, but ingredient proximity and tool coverage leave
collision risk **MEDIUM**.  This is not a global priority certificate.

## 9. Final seven-mode failure table

The verdict column uses only the protocol's permitted final vocabulary.

| Failure mode | Evidence and boundary | Verdict |
|---|---|---|
| 1. Implementation bug | Group axioms, direct counts, formula comparison, frozen-output replay, and byte hashes agree within the finite control scope; controls do not prove the theorem | CLEAR |
| 2. Hallucinated citation | 7/7 records and 12/12 contexts checked; the wrong Roettger author-page PDF was detected and excluded; the current Klug pinpoint is Theorem 3.1 | CLEAR |
| 3. Hallucinated experimental result | Active passport declares no experiments; numerical outputs are explicitly proof-regression controls | CLEAR |
| 4. Shortcut reliance | General claims rest on stated proofs and cited classical inputs; code is not a proof premise | CLEAR |
| 5. Bug reframed as insight | No code/formula discrepancy remains in the checked scope, and limitations are explicit | CLEAR |
| 6. Methodology fabrication | Definitions, proof chain, deterministic script, frozen output, source packets, and receipts are present; no statistical method is claimed | CLEAR |
| 7. Frame-lock | Alternate-term searches across all five core claim families surfaced and integrated the relevant neighboring frames and owners; this clears the checked frame-lock mechanism but does not imply exhaustive collision or priority clearance | CLEAR |

## 10. Final gates and unresolved requirements

| Gate | Current status | Required next action |
|---|---|---|
| Strict registry/source tuple replay | PASS: 37/37 VERIFIED rows in order, 12 genuine positive excerpts, 25 anchorless empty states, 0 manuscript-self rows, 0 serious claim verdicts | Preserve tuple/source packets and replay receipt |
| References and contexts | PASS_WITH_NOTES: 7 records, 12 contexts, 0 ghost/dangling; Roettger access limitation disclosed | Specialist may obtain the correct full article independently |
| D1 overlap screen | PASS_WITH_TOOL_LIMITATIONS: 24/70 = 34.2857%, all sections | Treat as bounded screen only |
| D2 author overlap | `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE` | Rerun after author identities are authorized |
| E6 claim-strength drift | PRESCRIBED SKIP: no prior block-anchored Revision-Evidence Bundle; schema PASS; non-blocking for this checkpoint | Supply an authorized bundle only if a completed semantic drift review is later required |
| Mathematical/proof regression | Current author audit and exact finite controls are consistent | Obtain independent surface-topology/finite-group specialist review |
| Collision/priority | MEDIUM risk; search-bounded; no clearance | Independent specialist collision review; no priority claim meanwhile |
| Authorship/funding/COI | UNRESOLVED | Human authors approve complete declarations |
| Stage 3 checkpoint | ELIGIBLE, NOT ENTERED | Await explicit user confirmation; specialist review is a Stage-3 task |
| External release | HOLD | Explicit human authorization required |

After this disposition and the synchronized QA/state metadata were sealed, the
package-level `SHA256SUMS` was regenerated and replay-checked as the current
comprehensive manifest.
