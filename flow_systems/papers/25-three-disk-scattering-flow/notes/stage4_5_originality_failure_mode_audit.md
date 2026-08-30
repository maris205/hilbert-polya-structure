# Paper 25 Stage 4.5 originality and AI failure-mode audit

Audit time: **2026-08-30T12:27:09Z**  
Mode: **Stage 4.5 / Mode 2 / current revised draft**  
Target SHA-256: `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835`

## Human-facing result

**NO BLOCKING ORIGINALITY SIGNAL; WARN-NOT-BLOCK LIMITATIONS APPLY.** A fresh
public-Web exact-phrase screen returned no actionable external match for the
sampled prose. This is a bounded heuristic screen, not Turnitin,
iThenticate, a publisher similarity report, or a reliable global-overlap
percentage.

## D1. Population and sampling

- Current English body-paragraph denominator: **74**.
- Deterministic sample: **45/74 = 60.8%**.
- Stage-4 new/substantially replaced body paragraphs: **17/17 checked**.
- Modified declarations: **all Funding, Conflict of Interest, Author
  contributions, Data and code availability, Ethics, and AI-assistance
  paragraphs checked**.
- Title/byline/affiliation/email metadata: **checked**.
- Major-section coverage: every numbered section contributes at least one
  sampled paragraph.

Sampled block IDs:

`B0006, B0010, B0013, B0111, B0015, B0018, B0020, B0024, B0026, B0031,
B0112, B0034, B0037, B0039, B0042, B0044, B0046, B0050, B0054, B0058,
B0060, B0063, B0065, B0067, B0071, B0074, B0076, B0078, B0113, B0114,
B0080, B0082, B0115, B0085, B0087, B0090, B0091, B0096, B0098, B0101,
B0102, B0103, B0105, B0108, B0116`.

All 17 current paragraphs introduced or materially replaced by the authorized
Stage-4 patch are present in this set. Table bodies were checked separately in
Phase C; declarations and metadata are additional to the 74-paragraph body
denominator.

## Search procedure and grades

For each sampled block, one characteristic 8--12 word fragment was searched
as a quoted phrase on 2026-08-30. Formula-heavy fragments were paired with
nearby distinctive prose. Results were inspected for true textual overlap,
not mere shared technical vocabulary.

| Grade | Count | Meaning |
|---|---:|---|
| ORIGINAL / no indexed exact match | 38 | no external exact-phrase match returned |
| COMMON_KNOWLEDGE / formula-adjacent technical prose | 7 | generic mathematical wording or standard terminology; no distinctive copied passage found |
| PARAPHRASE | 0 | no actionable semantic near-copy found in the checked results |
| CLOSE_MATCH | 0 | none |
| VERBATIM | 0 | none |

The queried fragments included the abstract boundary, both exact witness
paragraphs, the cohomology framing, the four-object map, finite-replay scope,
lock/provenance wording, both Route paragraphs, limitations, and conclusion.
Search results were either empty or topically unrelated; no external page
returned the paper-specific sentence strings.

## D2. Self-reuse screen

Four author-aware searches combined the supplied email, author name, exact
topic, and characteristic title language. No reliably author-linked prior text
containing a sampled characteristic fragment was found. Name-only hits were
not treated as author identity evidence.

Disposition: **INSUFFICIENT EVIDENCE FOR A GLOBAL CLEAN CERTIFICATE; NO
ACTIONABLE SIGNAL IN THE SEARCHABLE AUTHOR-LINKED SUBSET.** The audit does not
have an authoritative complete publication corpus, cannot inspect every
paywalled or unindexed source, and is weak for translated/cross-language
reuse.

## D3. AI-writing heuristics

The current draft was inspected for formulaic section transitions, repeated
claim templates, synthetic quotations, unexplained terminology shifts,
reference-style drift, and abrupt scope inflation. Two recurring transition
patterns (`First/Second/...` and repeated ownership-boundary wording) were
observed, but both organize a declared limitations/typing argument and do not
form an originality finding. This is not an authorship classifier.

## Seven AI-research failure modes

| Mode | Status | Recorded basis and boundary |
|---|---|---|
| 1. Implementation bug passes self-review | `CLEAR_AFTER_REPLAY` | 75/75 tests, eight fail-closed tamper cases, 68-file lock, and isolated Round-8 rebuilds passed. This does not prove absence of every implementation bug. |
| 2. Hallucinated citation | `CLEAR_CONTEXT_WITH_MINOR_METADATA_HOLD` | Fresh Phase A/B found all 8 works and support for all 13 citation contexts; four exact metadata/update-disclosure repairs remain proposed, so the overall gate is not zero-issue. |
| 3. Hallucinated experimental result | `CLEAR_AFTER_DECLARATION_AND_REPLAY` | 6/6 registered experiment claims align to persisted results/provenance, and the fresh replay reproduced the declared counts without canonical refresh. |
| 4. Shortcut reliance | `CLEAR_WITH_SCOPE_BOUNDARY` | The theorem rests on two exact symmetric witnesses; the 2,241-row computation is explicitly validation-only. No external target table is used. |
| 5. Bug reframed as novel insight | `CLEAR` | The theorem-level result is independent of solver output; no failed implementation is narrated as the mathematical contribution. |
| 6. Methodology fabrication | `CLEAR_FOR_DECLARED_FINITE_REPLAY` | Source, lock, environment, tests, outputs, receipts, and limitations exist. This status does not certify an undeclared global physical determinant or asymptotic experiment. |
| 7. Early frame-lock | `INSUFFICIENT_EVIDENCE_WARNING` | Object typing, negative controls, limitations, and Route boundaries show active alternative checking, but the artifacts cannot reconstruct every counterfactual Stage-1 framing choice. No `SUSPECTED` signal was recorded. |

There are zero `SUSPECTED` modes. Mode 7 remains visible as the protocol's
warning-eligible insufficient-evidence class. The four fresh bibliography
MINOR findings independently keep Stage 5 closed.

## Limitations

- Search-engine indexing is incomplete and ranking is unstable.
- Exact phrase search can miss paraphrase, translation, images, and
  inaccessible full text.
- No professional similarity database was available.
- Common mathematical formulas and terminology cannot by themselves establish
  copying or originality.

Professional similarity screening remains recommended before formal
submission.

