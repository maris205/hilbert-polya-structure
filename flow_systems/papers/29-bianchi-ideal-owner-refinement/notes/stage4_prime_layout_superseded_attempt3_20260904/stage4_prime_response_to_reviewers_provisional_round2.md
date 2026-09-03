# P29 Stage 4-prime Round 2 provisional response to reviewers

Status: **PROVISIONAL — patch emitted, not applied.** Mechanical locations, output hashes, word-count delta, and E6 disposition remain for the separate applicator and post-apply audit.

Layout lineage: the current complete patch re-emits the second candidate archived under `notes/stage4_prime_layout_superseded_attempt2_20260904/`, which reduced the recorded layout failures from seven to five but remained ineligible for the final chain. It preserves every existing string and discretionary breakpoint, and adds only three scoped `\begingroup\sloppy … \par\endgroup` controls around the authorized B0107, B0112, and B0113 paragraphs. Removing those controls recovers the archived second-attempt patch exactly. A separate apply/build role must still establish the zero-overfull-box disposition.

| Item | Response | Emitted target(s) | Status |
|---|---|---|---|
| REV-R1-1 | Replayed all 53 frozen query lines on 2026-09-04 under the declared top-three/no-pagination bound; emitted a 144-row current replay ledger and a hash-linked 22-row P29-S01--P29-S22 inventory/matrix crosswalk. Historical rejected rows remain unavailable and were not reconstructed. | B0048, B0080, B0089, B0107 | PROVISIONALLY_RESOLVED_PENDING_APPLY |
| REV-NEW-1 (source NEW-1) | Replaced the independence claim with procedurally role-separated, same-model-family perspectives and retained correlated-error risk. | B0049 | PROVISIONALLY_RESOLVED_PENDING_APPLY |
| REV-R3-1 | Completed the prospective dependency/stop map for ObjectLedger, Gate Q, Gate M, PerformanceLedger, and replay. | B0112 | PROVISIONALLY_RESOLVED_PENDING_APPLY |
| REV-R3-2 | Added the three exact fail-closed control outputs while preserving diagnostic and non-diagnostic limits; none is observed. | B0113 | PROVISIONALLY_RESOLVED_PENDING_APPLY |
| REV-DA-2 | Limited value to prospective organizational benefit and defined, but did not run, SF-LITERAL-01 with its baseline, literal candidate, scoped expected stop, and no-performance/all-codomain prohibitions. | B0084 + fixture sidecar | PROVISIONALLY_RESOLVED_PENDING_APPLY |

Patch: `notes/stage4_prime_revision_patch_round2.json`  
SHA-256: `d02911b1f000716d703c68934dca899120de00c2f8d311778d55d9b7793f7135`

No bibliography entry, registered ClaimIntent replacement, scientific value, canonical file, Route coordinate, or later-stage artifact was changed.
