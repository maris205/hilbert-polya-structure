# P28 Stage 3′ Round 2 Verification Review Report

- **Round id:** `p28-stage3-prime-round2-2026-08-30`
- **Decision:** **Major Revision**
- **Mechanical rule:** `B3`
- **Official checker:** PASS (exit 0)
- **Apply-report chain:** `pass`
- **Checked at:** `2026-08-30T10:41:10Z`
- **Attempt 1:** preserved as immutable aborted audit evidence; it was not an input to this fresh review.

## Judge Record (#539)

- **Verification judge:** OpenAI GPT-5 / Codex session family; exact runtime model id was not exposed to the artifact layer.
- **Round-1 panel provenance:** `valid`; artifact `notes/stage3_review_panel_provenance.json`; raw SHA-256 `bf675940f217351ad619078ee061a388f8ca122cae25235b95d8b494c412b9fd`; normalized-manifest SHA-256 `b2515249aa69465766e34b2db937d2b8c9c28218f97aee7a15aea68b3f111b09`; execution-topology SHA-256 `a1f8e1998cabc29c3dff3c103f2a38a00a0fb2a020fba5816012bf1ab240cb4d`.
- **Six provenance axes:** role-separated=`true`; fresh-context=`true` (`within_panel_attempt_only`); blind-to-peer-outputs=`true`; model-family-distinct=`false`; provider-distinct=`false`; human-distinct=`false`.
- **Blind cross-model pass:** `not_configured`.
- **Pre-committed criteria:** JCS SHA-256 `7af9511ee1a4bbcfe22d93bc2410b21d2d6cbf228da93972813b0e8e1fc34bea`.
- **Prompt/rubric surfaces:** ARS re-review three-gate protocol and current contract family `1.1`.
- **Reviewer configuration:** `round1_cards_reused`.
- **Routing:** `card_mapped`; DA-only items route to EIC by protocol.
- **Evidence seen:** Phase 1 — roadmap/decision letter/Round-1 findings/cards; Phase 2A — original and revised manuscripts plus bound patch/apply/bundle; Phase 2B — bound response JSON. Author adjudication remained checker-only.
- **Judging budget:** three gated review turns, with transport shared inside the paper batch; exact per-paper token accounting unavailable.

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

## Decision

**Major Revision** under `B3`. The decision is checker-derived from the frozen Phase-2A verdicts and zero Phase-2B adjustments. It is a mandatory Stage 3′ checkpoint, not authorization for Stage 4′.

## Revision Response Checklist

| Ref | Item | Class | Final status | Verified by | Original concern | Author claim | Revision location |
|---|---|---|---|---|---|---|---|
| R1 | REV-01 | MUST_FIX | FULLY_ADDRESSED | EIC | The manuscript states a digest-before-reconstruction replay order, while the audited builder executes proof guards and finite traversal before build_… | Claims that B0099 now states proof guards and finite reconstruction first, build_validation lock and binding checks second, and retains temporary-directory verify-only c… | The emitted patch has replaced anchored block B0099 in the subsection “Independent replay obligations.” |
| R2 | REV-02 | MUST_FIX | CANNOT_VERIFY | R1 | The official Round-8 suite exercises several canonicalization and closure invariants only indirectly, leaving test-localization and same-builder assu… | Claims that direct tests executed repeated Delta cancellation, global-negation normalization idempotence, both inverse orders, and sampled canonical collisions and that … | The emitted patch has replaced anchored block B0048 in the subsection “Canonicalization invariants.” |
| S1 | REV-03 | SHOULD_FIX | FULLY_ADDRESSED | R3 | Adjacent-field readers lack a compact definition map for A0--A4 and a consolidated chain of the still-unexecuted matched-census, owner-quotient, sign… | Claims that the inserted non-ranking legend defines A0-A4, keeps the full tuple unassigned and the historical proxy unchanged, limits current credit to A0-A1 infrastruct… | The emitted patch has inserted the obligation legend immediately after anchored block B0106 in “Adversarial c… |
| S2 | REV-04 | SHOULD_FIX | FULLY_ADDRESSED | R3 | The manuscript states the geodesic-to-magnetic boundary mainly through exclusions and does not provide a typed map separating present geodesic output… | Claims that the inserted typed map exposes only control-surface, exact group-element, geodesic-length, and cutoff outputs and separately types magnetic, owner, multiplic… | The emitted patch has inserted the typed interface immediately after anchored block B0037 in “Related exact-c… |

## Frozen evidence summary

- `FULLY_ADDRESSED`: 3
- `PARTIALLY_ADDRESSED`: 0
- `NOT_ADDRESSED`: 0
- `MADE_WORSE`: 0
- `CANNOT_VERIFY`: 1
- Phase-2B adjustments: 0
- New issues / dissents / escalation exceptions: 0 / 0 / 0
- Should-fix addressed rate: 2/2

## Residual issues

- **REV-02 — CANNOT_VERIFY** (must_fix): B0048 now states that Stage-4 direct tests exercise repeated Delta cancellation, global-sign normalization idempotence, both inverse orders, and sampled canonical collisions, but the actual test record and exact replay artifact are outside and unbound to the permitted Phase-2A evidence set, so the manuscript's execution claim cannot be verified independently of its own text.

A `CANNOT_VERIFY` result means the criterion required evidence not present in the hash-bound Stage 3′ input set; it does not assert that a separately stored Stage-4 test failed.

## Checker record

The official checker accepted the current manifest, all three gated artifacts, immutable roadmap, exact author sidecar, complete revision-evidence bundle, decision letter and ordered apply report. Advisory only: Editorial decision letter present but no Required Item Details blocks parsed; the level-2 criteria layer is empty.

- [Input manifest](stage3_prime_round2_input_manifest.json)
- [Phase-1 precommitment](stage3_prime_round2_precommitment.json)
- [Phase-2A verdict record](stage3_prime_round2_verdict_record.json)
- [Phase-2B integration](stage3_prime_round2_phase2b_integration.json)
- [Traceability sidecar](stage3_prime_round2_traceability.json)
- [Checker receipt](stage3_prime_round2_checker_receipt.json)

## Boundary and next checkpoint

No canonical manuscript, PDF, result, Route-A tuple or Route-B state changed in this verification round. The next legal transition is **Stage 4′**, and only after explicit user authorization.
