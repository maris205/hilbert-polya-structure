# P31 Stage 3′ Round 2 Verification Review Report

- **Round id:** `p31-stage3-prime-round2-2026-09-03`
- **Decision:** **Major Revision**
- **Mechanical rule:** `B4`
- **Official checker:** PASS (exit 0)
- **Apply-report chain:** `pass`
- **Checked at:** `2026-09-03T12:06:19Z`
- **Round 1:** preserved byte-for-byte as frozen abort evidence and excluded from the fresh review contexts.

## Judge Record (#539)

- **Verification judge:** OpenAI GPT-5 family through Codex; the exact service model id is not exposed to this artifact layer.
- **Round-1 panel provenance:** `valid`; artifact `notes/stage3_review_panel_provenance.json`; raw SHA-256 `0a5cdae92e3165c19cac5213acd0bb9a01ee8255b894af2cd91fc48001370027`; normalized-manifest SHA-256 `f0f48732fe3507ae5bac58283afc1e71dbfeb7f22b1005f95e34784db2185816`; execution-topology SHA-256 `a1f8e1998cabc29c3dff3c103f2a38a00a0fb2a020fba5816012bf1ab240cb4d`.
- **Six provenance axes:** role-separated=`true`; fresh-context=`true` (`within_panel_attempt_only`); blind-to-peer-outputs=`true`; model-family-distinct=`false`; provider-distinct=`false`; human-distinct=`false`.
- **Blind cross-model pass:** `not_configured`; no independent-error-process claim is made.
- **Pre-committed criteria:** JCS SHA-256 `e22a19a20caaf3a24d59ea6be717cfd8425ea14eea83a073c8f0be92c61217eb`.
- **Prompt/rubric surfaces:** ARS re-review three-gate protocol and contract family `1.1`; exact hashes are recorded in the checker receipt.
- **Reviewer configuration:** `round1_cards_reused`.
- **Routing:** `card_mapped`; the DA seat is not a verification persona.
- **Evidence seen:** Phase 1 used only frozen Round-1 yardsticks; Phase 2A added original/revised manuscripts and bound patch/apply/bundle evidence while withholding the response; Phase 2B added the response. Author adjudication remained checker-only.
- **Judging budget:** three gated review calls plus this deterministic checker invocation; exact token telemetry was not retained.

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

## Decision

**Major Revision** under `B4`. The official checker recomputed this decision from the committed artifacts. It is a mandatory Stage 3′ checkpoint, not authorization for Stage 4′.

## Revision Response Checklist

| Ref | Item | Class | Final status | Verified by | Original concern | Author claim | Revision location |
|---|---|---|---|---|---|---|---|
| R1 | REV-P31-001 | MUST_FIX | PARTIALLY_ADDRESSED | EIC | The manuscript leaves the originality and field significance of the certificate-first architecture unresolved because it does not compare the proposal with the closest canonical-form, computational-group-theory, proof-c… | The emitted patch supplies a frozen-corpus comparison across subgroup encoding, conjugacy algorithms, reduction and reversibility ingredients, and aggregate counting. It limits the contribution to the project-specific c… | Anchored block B0016 in the Introduction contribution paragraph. |
| R2 | REV-P31-002 | MUST_FIX | PARTIALLY_ADDRESSED | EIC | Claims that readers can recover hash-bound corpus, review, manifest, and revision artifacts are not accompanied by stable locators or a reader-resolvable artifact manifest. | The emitted patch lists existing repository-relative source, verification, passport, and roadmap artifacts with their exact SHA-256 values and explicitly labels them internal locators. It does not claim an archival rele… | Anchored block B0105 in Data and materials availability. |
| R3 | REV-P31-003 | MUST_FIX | FULLY_ADDRESSED | EIC | The Executed Methodology section presents a previous review panel's decision and finding counts as part of the scholarly method rather than as manuscript-development provenance. | The emitted patch describes capture, deduplication, screening, source-effect coding, and limitation propagation as the executed scholarly method. The four review roles, editorial outcome, and author adjudication are now… | Anchored block B0041 in the revision-procedure subsection. |
| R4 | REV-P31-004 | MUST_FIX | PARTIALLY_ADDRESSED | R1 | The central contract conflates a canonical owner map defined on resolved inputs with a total disposition process that may emit unresolved states, leaving the biconditional and complete G/I/C materialization without one … | The emitted patch types each root decision as Resolved or Unresolved, defines X_res as the domain of the byte map, and requires a total owner disposition over X. The downstream contract now states explicitly that comple… | Anchored block B0046 in the canonicalization contract. |
| R5 | REV-P31-005 | MUST_FIX | PARTIALLY_ADDRESSED | R1 | The unordered table of distinct input pairs cannot independently test reflexivity, directional symmetry, or transitivity in the broad way claimed without self-fixtures, ordered reversals, and triple or class-level closu… | The emitted patch separates self fixtures, ordered reversal pairs, three-input closure fixtures, and independently sourced disagreement rows. It states that 9,453 unordered distinct pairs alone cannot exercise self, dir… | Anchored block B0062 in the all-pairs audit subsection. |
| R6 | REV-P31-006 | MUST_FIX | FULLY_ADDRESSED | R1 | The certificate and verifier contract remains a prose specification because it supplies no closed byte schema, theorem registry, proof-payload grammar, fixture bytes, producer, reference verifier, or build manifest. | The emitted patch takes the authorized narrowing branch. It identifies the contract as non-executable, enumerates the absent schema bytes, theorem registry, fixture corpus, producer, verifier, and build manifest, and re… | Anchored block B0056 in the prospective certificate-and-verifier contract. |
| R7 | REV-P31-007 | MUST_FIX | PARTIALLY_ADDRESSED | R1 | The executed literature synthesis reports aggregate corpus counts and citation closure but omits exact search queries, complete screening decisions, and theorem/page locators for component claims used in the design. | The emitted patch records that aggregate corpus counts exist but a complete row-level exclusion ledger and exact theorem-page and quotation locators do not. All citation carriers remain anchor:none and claim-to-passage … | Anchored block B0089 in Acknowledged Limitations. |
| R8 | REV-P31-008 | MUST_FIX | PARTIALLY_ADDRESSED | R2 | The categorical rule that an owner must never share bytes with its inverse lacks either a theorem excluding subgroup self-reciprocity or a typed branch for an inverse-related representative in the same owner class. | The emitted patch does not invent a theorem. It retains the initial inverse-separate convention as a proof obligation, requires a replayable self-reciprocity branch, and mandates UNRESOLVED_INVERSE_SEPARATION until the … | Anchored block B0049 in the canonicalization target subsection. |
| R9 | REV-P31-009 | MUST_FIX | PARTIALLY_ADDRESSED | R3 | The prose definitions of G, I, and C do not consolidate primary keys, foreign keys, uniqueness constraints, unresolved-state policy, provenance fields, projection functions, and materialization preconditions in one rela… | The emitted patch specifies primary and foreign keys, typed fields, the I-to-G/C dependency, a distinct C projection, and a separate non-estimand I_diag surface. It now makes the materialization invariant explicit: zero… | Anchored block B0067 at the beginning of the G/I/C estimand subsection. |
| R10 | REV-P31-010 | MUST_FIX | FULLY_ADDRESSED | R3 | The interoperability claim permits polygonal, arithmetic, or word-hyperbolic producers under one owner contract but gives no worked trace from heterogeneous representations to common owner bytes and verifier disposition… | The emitted patch adds a clearly synthetic trace for hypothetical polygonal and word-hyperbolic producers. It distinguishes route-private proof tags from common envelope fields, specifies fail-closed schema-version hand… | An authorized insertion immediately after anchored block B0086 in the Discussion. |
| R11 | REV-P31-011 | MUST_FIX | PARTIALLY_ADDRESSED | EIC | The 9,453-row audit is generated from the canonical partition it is meant to challenge, so without an independently bound direct route it cannot detect semantic false merges or splits. | The emitted patch limits the table to serialization, binding, inverse-label, traversal, and bookkeeping consequences and marks the direct-solver field ABSENT. It states that semantic false merges and splits require an i… | Anchored block B0061 in the all-pairs audit subsection. |

## Frozen evidence summary

- `FULLY_ADDRESSED`: 3
- `PARTIALLY_ADDRESSED`: 8
- `NOT_ADDRESSED`: 0
- `MADE_WORSE`: 0
- `CANNOT_VERIFY`: 0
- Phase-2B adjustments: 0
- New issues / dissents / escalation exceptions: 0 / 0 / 0
- Should-fix addressed rate: 0/0

## Residual issues

- **REV-P31-001 — PARTIALLY_ADDRESSED** (`must_fix` residual): The comparison still does not name and cite the closest proof-carrying-data and ledger-verification work, so the precommitted four-family positioning pattern is incomplete.
- **REV-P31-002 — PARTIALLY_ADDRESSED** (`must_fix` residual): Several materials still described as reader-recoverable are absent from the list, and the listed entries lack schema or version and explicit access-state fields, so neither the metadata branch nor removal-of-retrieval-claims branch is complete.
- **REV-P31-004 — PARTIALLY_ADDRESSED** (`must_fix` residual): Blocks B0050-B0051 retain a total-owner-map statement whose totality condition admits unresolved dispositions, so not every totality statement uses the newly separated matching type.
- **REV-P31-005 — PARTIALLY_ADDRESSED** (`must_fix` residual): The introductory claim in B0015 still assigns nontransitivity and merge-or-split detection to the all-pairs expansion without the capable triple or independent semantic audit surface, leaving a material manuscript-level contradiction.
- **REV-P31-007 — PARTIALLY_ADDRESSED** (`must_fix` residual): The required replayable search and screening supplement and source-finalization records remain absent; transparent unresolved labels satisfy only part of the committed evidence pattern.
- **REV-P31-008 — PARTIALLY_ADDRESSED** (`should_fix` residual): The revision safely defers the case but supplies neither an applicable exclusion lemma nor the typed resolved branch for a genuinely self-reciprocal owner, so the branch-complete inverse rule remains open.
- **REV-P31-009 — PARTIALLY_ADDRESSED** (`should_fix` residual): The required directly checkable consolidated table is still absent even though most of its required content now appears in prose.
- **REV-P31-011 — PARTIALLY_ADDRESSED** (`must_fix` residual): Broader manuscript wording still credits the all-pairs expansion with semantic merge, split, or transitivity detection without independently generated evidence, contradicting the new block-level limitation.

## Concrete paper progress

Owner canonicalization, G/I/C materializations, and the 9,453-pair adversarial-audit architecture survive the fresh Round-2 criteria and evidence gates. Residual must-fix obligations still prevent acceptance.

## Route-map and initial-system boundary

- **Frozen system:** fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree is distinct.
- **Route position:** A1-only preparation; formal tuple UNASSIGNED; positive arithmetic A2 = 0; Route B uninvoked.
- This review changed no Route-A tuple, A2 result, Route-B state, system clock/owner/normalization, canonical manuscript, bibliography, PDF, or scientific result.

## Checker record

The official ARS checker exited zero, agreed with `Major Revision` / `B4`, and replayed the apply chain as `pass`. Exact stdout, stderr, command-input hashes, and checker hash are preserved in `stage3_prime_round2_checker_receipt.json`.

## Boundary and next checkpoint

The next legal transition is **Stage 4′**, only after explicit user authorization. No Stage 4′ work has begun.
