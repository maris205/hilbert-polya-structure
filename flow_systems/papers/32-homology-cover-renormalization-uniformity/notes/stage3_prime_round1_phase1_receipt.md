# P32 Stage 3′ Round 1 — Phase 1 Receipt

## Contract binding

- Contract: `re-review/precommitment` version `1.1`.
- Round: `p32-stage3-prime-round1-2026-09-03`.
- Input-manifest JCS hash: `f474b87618729b960212d1d6aaa3d393e228671cf53ce68b21a7d45b4e6bdeee` (caller-supplied binding; the manifest itself was not opened).
- Gate completed: Phase 1 criteria commitment only (revision-blind).

## Read allowlist and isolation

The paper-specific read set was limited to:

1. `notes/stage3_revision_roadmap.json`
2. `notes/stage3_editorial_synthesis.md`
3. `notes/stage3_review_package.json`
4. `notes/stage3_phase0_field_analysis.md`

The only non-paper materials consulted were the ARS academic-paper-reviewer workflow, the re-review mode protocol, and `shared/contracts/re_review/precommitment.schema.json`.

No `stage4_*` file, `stage3_prime_round1_input_manifest.json`, `stage3_revision_base.tex`, `paper/manuscript.tex`, root README, batch Stage-4 report, revised or original manuscript body, patch/apply/bundle artifact, author adjudication, or Response to Reviewers was read. No revision-side metadata or revision fact entered the criteria commitment.

## Item and criterion accounting

- Frozen Roadmap: 7 `must_fix`, 5 `should_fix`, 0 `consider`.
- Emitted records: 12, in exact Roadmap order; exactly one record for every `must_fix` and `should_fix` item.
- `roadmap_text`: copied verbatim for all 12 records.
- Required-item letter layer: **advisory degradation**. The decision-letter layer was not parser-resolvable under the strict Required Item Details grammar. Per the revision-blind contract and the caller's explicit instruction, no `letter_text` or `letter_item_ref` field was emitted; all P32 records inherit only the verbatim level-1 Roadmap criterion.
- `must_fix` operationalizations: each contains concrete `fully_addressed`, `partially_addressed`, and `made_worse_discriminator` patterns.
- `should_fix` operationalizations: each contains only the lighter-form `fully_addressed` pattern.
- Expected change surfaces: navigation hypotheses derived only from each frozen Roadmap item's `target_section` and `proposed_targets` (with no post-revision surface information).
- Equivalent evidence-backed fixes remain allowed.
- `new_standards`: empty; no criterion beyond the inherited Round-1 Roadmap layer was added.

## Frozen-card routing

- Reviewer configuration: `round1_cards_reused`.
- Routing status: `card_mapped`.
- The DA is never used as a verification persona; DA-only items therefore route to the EIC fallback while retaining their verbatim reviewer strings and normalized `DA` source labels.

| Item | Obligation | Verbatim source reviewer | Normalized labels | Phase 2A seat reserved by this commitment |
|---|---|---|---|---|
| `REV-P32-EIC-W1` | `must_fix` | `EIC` | `EIC` | `EIC` |
| `REV-P32-EIC-W2` | `must_fix` | `EIC` | `EIC` | `EIC` |
| `REV-P32-EIC-W3` | `should_fix` | `EIC` | `EIC` | `EIC` |
| `REV-P32-EIC-W4` | `should_fix` | `EIC` | `EIC` | `EIC` |
| `REV-P32-R1-W1` | `must_fix` | `R1` | `R1` | `R1` |
| `REV-P32-R1-W2` | `must_fix` | `R1` | `R1` | `R1` |
| `REV-P32-R1-W3-R2-W2` | `must_fix` | `R1; R2` | `R1`, `R2` | `R1` |
| `REV-P32-R1-W4` | `must_fix` | `R1` | `R1` | `R1` |
| `REV-P32-R2-W1` | `should_fix` | `R2` | `R2` | `R2` |
| `REV-P32-R3-W1` | `should_fix` | `R3` | `R3` | `R3` |
| `REV-P32-DA-N1` | `should_fix` | `DA` | `DA` | `EIC` fallback |
| `REV-P32-DA-M1` | `must_fix` | `DA` | `DA` | `EIC` fallback |

## Gate boundary

This artifact contains no Phase 2A evidence assessment, verdict, manuscript-change claim, new-issue finding, author-claim matching, decision derivation, or re-review outcome. Phase 2A was not entered.

[CONTRACT-ACKNOWLEDGED]
