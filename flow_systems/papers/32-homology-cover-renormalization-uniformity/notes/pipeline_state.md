# P32 pipeline state

Date: **2026-09-03 (UTC+08:00)**

Current controlling state: **`stage3_prime_round1_aborted_awaiting_round2_authorization`**.

| Item | Status |
|---|---|
| Pipeline global state | `stage3_prime_round1_aborted_awaiting_round2_authorization` |
| ARS Stage 1 | `COMPLETE`; Phase-6 checkpoint and Stage-2 handoff frozen |
| ARS Stage 2 WRITE | `COMPLETE` |
| Stage-2 authorization | `CONFIRMED`; `BATCH_ROUND10_STAGE2_AUTHORIZATION_20260902.txt` |
| Stage-2 pre-prose registration | `COMPLETE`; 8/8 ClaimIntents, one-to-one same-or-narrower lineage |
| Stage-2.5 authorization | `CONFIRMED`; `BATCH_ROUND10_STAGE2_5_AUTHORIZATION_20260902.txt` |
| Manuscript | `CANONICAL_POST_REPAIR`; SHA-256 `4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a` |
| Bibliography | `COMPLETE`; 26 entries, all cited, no missing/orphan; SHA-256 `e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9` |
| PDF | `CANONICAL_POST_REPAIR`; 13 pages, 254332 bytes; SHA-256 `66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93` |
| Build receipt | `PASS`; `notes/stage2_5_post_repair_build_receipt.json` |
| Independent recheck | `PASS`; 8/8 ClaimIntents; no unresolved Blocker, Major, or Minor; `notes/stage2_independent_recheck.md` |
| Explicit paper progress | The paper now fixes a falsification-first theorem program: higher-content and zero-content local factors are the first discriminating targets under exact `1/N` time and `1/N^3` log normalization; content-one is explicitly survival-conditional and secondary. This is a design/certificate advance, not an executed factor derivation or obstruction result. |
| Frozen dynamical system | pure genus-two homology-cover tower H_N; all-content oriented primitive owners; exact 1/N time and 1/N^3 logarithmic normalization |
| P32-S13 boundary | Current identity/metadata are bibliographically `VERIFIED`, but use remains background-only; citation carrier `anchor:none`; claim-to-passage `INCONCLUSIVE`. The unchanged historical Phase-2 25/1 sentence remains historical. |
| Phase A/B | `PASS`; references 26/26 checked and 26/26 `VERIFIED`; citation contexts 8/26 sampled and 8/8 supported; unresolved findings 0 |
| Phase C | `PASS`; 58/58 claim surfaces; figure/table traces 0; `no_experiments_declared`; `experiment_provenance=[]` |
| Phase D originality | `PASS`; 24/77 paragraphs, 10/10 major sections, 24 `ORIGINAL`; authorized changed paragraphs 5/5 inspected |
| Phase E claims | `PASS_SELECTED_POPULATION`; 98 registered, 88 selected, 108 evidence tuples, 88/88 `VERIFIED`; 108/108 anchorless |
| Seven failure modes | `CLEAR` 7/7; `SUSPECTED` 0; `INSUFFICIENT EVIDENCE` 0 |
| Official E6 | Stage-4 Revision-Evidence Bundle present at SHA-256 `b527625c90cff83468df0ca40b066b79f47b8deaa22c8f62324d297ae4275269`; Stage-4.5 E6 `NOT_INVOKED`; bounded semantic audit `PASS` is not official E6 |
| New retrieval / scientific execution | `NO` / `no_experiments_declared`; scientific executions 0 |
| Canonical scientific-result refresh | `NO` |
| Novelty assessment | No priority/novelty claim; bounded Phase-D public-Web/local-corpus originality screen only |
| Formal Route-A tuple | `UNASSIGNED`; formal tuples `0`; positive arithmetic A2 `0` |
| Route position | Route A A0/A1 foundation/interface only; P32 A0 unavailable; no formal tuple, A2/A3/A4 credit, or Route-B invocation. |
| Route B | `CLOSED`; evaluation `NOT_RUN`; invocation `false` |
| Stage 2.5 integrity | `COMPLETE`; `PASS_AT_STAGE_2.5_CHECKPOINT`; unresolved Serious/Major/Medium = 0/0/0 |
| Stage-2.5 mandatory checkpoint | `SATISFIED_BY_STAGE3_ENTRY_AUTHORIZATION` |
| Stage 3 entry | `AUTHORIZED`; receipt `BATCH_ROUND10_STAGE3_AUTHORIZATION_RECEIPT.json` |
| Stage 3 Phase 0 | `COMPLETE`; scholar-confirmed; 4 dynamic cards + 1 fixed DA; validation `PASS` |
| Stage 3 substantive review | `COMPLETE`; Phase 1/2 reports `5/5`; editorial decision `Major Revision`; source weaknesses `13`; roadmap items `12 = 7 must + 5 should` |
| Stage 3 final validation | `PASS`; `../../../BATCH_ROUND10_STAGE3_VALIDATION_RECEIPT.json`; SHA-256 `808d0a89b27bf538b9a8134225e824d1d17952e4ed5df86d4ed7fe1b5f694c7b` |
| Stage 4 | `COMPLETE WITHIN EXACT AUTHORIZATION`; 12/12 items; 12 operations; 8 RESOLVED + 4 DELIBERATE_LIMITATION; 9/98 affected E1; +437 words; 14-page clean preview |
| Stage-4 write boundary | only versioned `notes/` revision artifacts changed; canonical manuscript/bibliography/PDF and science trees unchanged; Route advancement `NONE` |
| Stage 3′ Round 1 | `ABORTED / phase1_lint_failed`; failed closed at mandatory Phase-1 criterion lint; recorded and audited aggregates both 6/5/1, but `REV-P32-R1-W2` is a false FULL and `REV-P32-R3-W1` is a false PARTIAL; Phase-1 criterion drift affects `REV-P32-R3-W1` and `REV-P32-DA-M1`; mechanical B3 candidate suppressed; no decision signed or emitted |
| Semantic calibration boundary | Fresh-context and role-separated, but same-family; the semantic passes are not independent error processes |
| Next legal transition | only a new user `确认` authorizing fresh Stage 3′ Round 2 with a new round id, new manifest, fresh Phase-1/2A contexts, and all Round-1 artifacts preserved |
| Stage-2 output manifest | SHA-256 `b023d9b91e18580bc9921be56c1ab0fb0c6723575305baae1a7f330eb1907bfa` |

## Stage-2.5 traceability

| Artifact | SHA-256 |
|---|---|
| `BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md` | `ce99860d6fe60de840c9802757686d4818a1d735dd2b03cf5f11976b1b9d2106` |
| `BATCH_ROUND10_STAGE2_5_INTEGRITY_SUMMARY.json` | `ea4773bd5d612a8095f2f9950854e7274c6ed9d33b1568cc7fb543cd928b0bc9` |
| `BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json` | `8d9ecc4d4ccba99762db1656e9055b2e236f0b352c19a144eed32e6df0aa38b8` |
| `BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json` | `54bd577683595dd9259ba2a97405b7257a269bf740ffcaa1c0135718869e5041` |
| `BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json` | `14c846c4b32dc77e7735fc645c7afe359c91109cc4c5c6c60554882317c1cf3b` |
| `BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json` | `946973cc01c273cb38d88efdfbb4693e709b9aa08e6fb769e649c2c408393c7b` |
| `notes/stage2_5_integrity_report.json` | `e5cb65212a55a6b090fe1985cd68eaef0ba4b4bf3825da2c9c03a7ae041217bd` |
| `notes/stage2_5_material_passport.json` | `f3136c99aab75685063e5fc8ea61dfe814c333fd60797a39690d802af4788cae` |

Stage-2.5 PASS certifies the declared, denominator-bounded integrity checks for
the frozen canonical package. It does not certify theorem correctness,
passage-level support, global originality, scientific implementation, or Route
promotion, and it does not itself authorize Stage 3.

## Frozen Stage-4 completion bindings

| Artifact | SHA-256 |
|---|---|
| [Per-paper completion report](stage4_completion_report.md) | `f7dc5ab5465f63256809576c5d7ca17a977b56d238c9eef6d7d9d9808e38c84d` |
| [Bounded semantic audit](stage4_unregistered_claim_drift_audit.md) | `609f5b056034ceb9bd28ea2b5f95aaeaa52e0a4cb581a3c3a6b4be064191a949` |
| [Route crosswalk](stage4_route_crosswalk.md) | `570b8d7307913495053c69560ccd04e0d37ab6dbcd99fbe53248b81db296fcda` |
| [Revision-Evidence Bundle](stage4_revision_evidence_bundle.json) | `b527625c90cff83468df0ca40b066b79f47b8deaa22c8f62324d297ae4275269` |
| [Batch completion report](../../../BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md) | `b285a5478b08f9740926d534ad5256237ac5bd43da5059586fd3d87daced830a` |
| [Batch completion receipt](../../../BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json) | `9628917f81d07288dbb6a255f922c397ca87cf4114df61a07fe600c02cfb97bd` |

## Current Stage-3′ Round-1 bindings

| Artifact | SHA-256 |
|---|---|
| [Verification report](stage3_prime_round1_verification_report.md) | `deab1d001c3b6a183a94c371ecb8ddf9494147e23d86ba9dcc0ff1ff22aebb85` |
| [Checker/semantic receipt](stage3_prime_round1_checker_receipt.json) | `4033a2346ba98d56f37176523e07f682115838e07e6b73c0395e2020ed4c82f6` |
| [Abort record](stage3_prime_round1_abort_record.json) | `b11516b0046dfb0a8c33d18090df33e0191cf1e9a2f8efe68df189116e27a941` |
| [Batch outcome report](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND1_REPORT.md) | `16799921ba4222fca534adf9c56b242879b012576bb72bac9ba95c025cdd8fbf` |
| [Batch outcome receipt](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json) | `2d315dae3f051956698958fab9ea95b0024ec7e78d78c8abd9e4a3ead4377ba2` |

The ClaimIntent replay is `0/0` vacuous and not a clean certificate. Completion
rests on the bounded changed-operation/E1 semantic audit. generic Route-A A1-A2 preparation with arithmetic A0 unavailable; formal tuple `UNASSIGNED`; Route B uninvoked.
Canonical bytes and scientific trees are unchanged. Round 1 is immutable and
failed closed. Only a new user `确认` may authorize fresh Round 2; Stage 4′,
Stage 4.5, Stage 5, canonical promotion, submission, Route advancement, result
refresh, and new scientific execution remain unauthorized.
