# P31 Stage 1 Phase 5 Editorial Review

## Input binding and review status

| Field | Bound value |
|---|---|
| Seat | `R10-P5-EIC` |
| Review role | Editor-in-Chief |
| Calibration | `NOT_CALIBRATED` |
| Phase-4 report SHA-256 | `9465546ed487c96db45301de68c3640b673f7d604fc6262f39fa6029f5ae0213` |
| Phase-4 claim-intent manifest SHA-256 | `bc69ffd820542982a56f250b950f08dfdae60d86ba58ae2a3d720f55022ccd11` |
| Phase-4 checkpoint SHA-256 | `7b06fec73644fc78951b93a6a8cb882d86b2e5ec59134f07e545fe040b957b94` |
| New retrieval | `NOT_RUN` |
| Input modification | `NONE` |
| Overall verdict | `MAJOR_REVISION` |

## Overall assessment

The report offers a strong proof-first decomposition of a finite owner-ledger problem. It separates group representation, subgroup conjugacy, primitive-root and inversion semantics, deterministic certification, and the later construction of global-owner, incidence, and cell-local estimands. The distinction among `G`, `I`, and `C`, together with the warning that aggregate class counts cannot validate a pair partition, is especially valuable.

The draft is not yet ready as a Q1-level research or methods article. Its central architecture remains project-defined and uninstantiated; the necessity of a full 9,453-pair ledger is asserted but not justified against more compact equivalence-class certificate designs; the `G/I/C` map has no self-contained formal specification; originality is unassessed; and theorem-adjacent source transfers remain locator-free. These shortcomings require substantial development but do not undermine the report's honest conclusion that no owner census has yet been executed.

## Dimension judgments

| Dimension | Judgment | Evidence-based rationale |
|---|---|---|
| Originality and contribution | `NEEDS_REVISION` | Sections 4 and 5 articulate a useful four-layer architecture, but Section 6 and the ledger explicitly decline novelty assessment, and no comparison establishes whether this certificate design advances existing exact conjugacy or census methods. |
| Methodological rigor | `NEEDS_REVISION` | The fail-closed dependency order is rigorous as governance, yet no selected subgroup representation, complete conjugacy route, negative-certificate semantics, or independent verifier is formally bound. The all-pairs requirement itself is not defended as necessary. |
| Evidence sufficiency | `NEEDS_REVISION` | The 22-source corpus covers the relevant traditions, but Section 3.3 and Section 6 state that all claim-level locators are absent and exact theorem hypotheses were not inspected. |
| Argument coherence | `STRONG` | The report consistently distinguishes instance counts, global owners, incidences, and cell-local credit, and it keeps inverse orientation and traversal powers separate from Hecke degree. |
| Writing quality | `ADEQUATE` | The report is well structured and readable, but project codes, repeated negative boundaries, inline provenance markup, and the long machine ledger are not yet adapted to a general mathematical audience. |

## Concrete strengths

- The Introduction fixes the exact owner semantics and rejects trace, length, homology, and other filters as final subgroup-conjugacy certificates.
- Sections 2.1–2.3 separate group representation, pair decision, root and inverse semantics, and certificate replay instead of treating “algorithm exists” as an implementation.
- Sections 2.4 and 4.4 correctly place aggregate `Gamma_0(N)` counts after pair closure as consistency controls rather than pairwise proof.
- Section 4.3 gives a clear conceptual distinction among global owner table `G`, 138-row incidence relation `I`, and cell-local quotient `C`.
- Sections 5.3 and 6 preserve precise not-evaluable outcomes rather than turning bounded search failure into nonconjugacy.

## Findings and required revisions

### Critical findings

None. The report makes no owner decision and does not claim that the proposed solver or certificate format already exists.

### Major findings

#### `P31-EIC-001` — The necessity of all 9,453 pair decisions is not established

**Exact section evidence:** Section 4.2 states that every unordered pair must terminate after primitive-root replacement, and the abstract treats terminal decisions for all 9,453 pairs as an ordered dependency.

**Editorial consequence:** A complete equivalence partition can sometimes be certified with canonical representatives, positive membership witnesses, and class-level completeness evidence without materializing a negative certificate for every cross-class pair. The manuscript does not explain why the stronger quadratic ledger is mathematically necessary rather than one conservative audit design.

**Required revision:** Prove that the all-pairs ledger is required by the estimand or completeness theorem, or explicitly present it as a chosen audit architecture and compare it with at least one sound class-based alternative. State which certificate invariant, not raw pair count, is necessary and sufficient for closure.

#### `P31-EIC-002` — The proposed certificate system is not a formal method yet

**Exact section evidence:** Sections 2.2 and 2.3 require positive conjugators and “complete negative certificates,” while Sections 4.1 and 5.1 acknowledge that no route is selected and no certificate serialization is instantiated.

**Editorial consequence:** “Replayable negative certificate” is central to the paper but has no schema, verifier semantics, completeness theorem, or example. The architecture therefore cannot yet be reproduced or falsified.

**Required revision:** Specify the exact fields, mathematical predicates, canonicalization rules, verifier acceptance conditions, and termination/completeness theorem for each positive and negative disposition. Include adversarial accepted and rejected fixtures only under a later authorized methods revision; do not report them as executed now.

#### `P31-EIC-003` — The `G/I/C` estimand map remains an unproved project definition

**Exact section evidence:** Section 4.3 describes the three objects and states that no reviewed source establishes the map; Section 6 lists a self-contained proof of the mapping as an outstanding limitation.

**Editorial consequence:** The research question asks how global ownership induces the cell-local classification, but the draft does not provide formal definitions, invariants, or a proposition showing that the no-double-credit map is well defined and preserves the intended units.

**Required revision:** Give self-contained mathematical definitions of `G`, `I`, `C`, the cell key, multiplicity, and credit rule, followed by a proof of well-definedness and the required conservation or uniqueness invariants. Separate this internal theorem from literature-supported conjugacy machinery.

#### `P31-EIC-004` — The literature protocol and theorem transfers are not reproducible

**Exact section evidence:** Section 3.1 gives aggregate capture, screening, exclusion, and verification counts; Section 3.3 and Section 6 state that all citations are `anchor:none` and exact theorem hypotheses were not inspected.

**Editorial consequence:** Readers cannot reproduce either the corpus boundary or the claim that no included source closes the exact `Gamma_0(11)` interface.

**Required revision:** Supply the complete search and screening protocol in an immutable supplement, and attach exact passage locators and hypothesis maps to every source used for subgroup, conjugacy, root, centralizer, and census claims.

#### `P31-EIC-005` — The contribution is not positioned for publication

**Exact section evidence:** Section 4.5 claims sharper progress than a generic literature review, while the ledger states `NOVELTY_ASSESSMENT=NOT_RUN` and all scientific outputs remain absent.

**Editorial consequence:** The paper's article type and original contribution cannot be judged.

**Required revision:** Perform a separately authorized novelty and contribution comparison. Decide whether the deliverable is a mathematical methods protocol, a certificate-architecture paper, or a research report, then calibrate the title, abstract, claims, and required validation accordingly.

### Minor findings

#### `P31-EIC-006` — The AI verification statement is broader than the evidence

**Exact section evidence:** The AI Disclosure says all findings were verified against cited sources, then defines verification as mostly metadata, abstracts, landing pages, and bounded records.

**Editorial consequence:** The first statement can be misread as theorem-level validation.

**Required revision:** Use a single bounded statement that distinguishes source identity, claim fitness, and passage-level verification.

#### `P31-EIC-007` — Provenance vocabulary needs a publication layer

**Exact section evidence:** The report embeds `anchor:none`, numerous all-caps state codes, and a long closed machine ledger in the main text.

**Editorial consequence:** These are useful audit records but obscure the main mathematical narrative for external readers.

**Required revision:** Preserve the machine-readable audit trail in a supplement and define or remove project-internal codes in the journal rendering.

## Route-A and Route-B boundary

This editorial verdict creates no Route evidence. P31 remains an A1 ownership/completeness preparation for the positive time-changed `Gamma_0(11)` flow. The formal Route-A tuple is `UNASSIGNED`, positive arithmetic A2 remains absent, no determinant result is created, and Route B remains uninvoked. Editorial acceptance in a future phase would not by itself close the owner ledger or change any Route coordinate.

## Procedural-independence and model disclosure

This review was produced by the `R10-P5-EIC` seat using the current Codex model family. The seat was procedurally separated from the Ethics, citation-integrity, and Devil's Advocate seats and did not inspect or synthesize their Phase-5 outputs. No external provider or cross-model transfer was authorized. Procedural separation does not imply statistically independent errors; the review is single-family and `NOT_CALIBRATED`.
