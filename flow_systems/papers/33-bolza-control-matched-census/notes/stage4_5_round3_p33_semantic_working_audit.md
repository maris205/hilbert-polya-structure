# P33 Stage 4.5 Round 3 — interrupted semantic work record

Sealed 2026-09-05 09:37:12 UTC. Status: **STOP — input-integrity mismatch reported by the parent agent. This is not a completed audit or PASS.**

The parent reported an actual nested historical hash mismatch at the P30 owner's independent read-only C-reader entry and invoked the approved “Any artifact/hash mismatch STOP” condition. P33 stopped all further search, audit, and validation immediately. This append-only record preserves only work completed before that instruction; it does not independently confirm the P30 mismatch, repair any input, or authorize resumption.

## Input association

Last observed batch lock: `BATCH_ROUND10_STAGE4_5_ROUND3_INPUT_LOCK.json`, SHA-256 `0c7755b343990af1d37049838f81e0483323584c96eab58cddf6e14bc572e229`. This was the parent-reported runtime binding before the stop, not a fresh rehash at sealing.

P33 current draft: `notes/stage4_prime_revision_round3.tex`, SHA-256 `aa3783e6a24f830918ccb88b8dc5ebb28d9c15a94d87ffdb907cf5da9e049d6d`. The companion JSON retains the other last-observed input associations and exact submitted query list.

## Work actually completed

- The required ARS skill, workflow, integrity role and routed references were read before task actions.
- The entire current manuscript, lines 1–736 and all 128 blocks, was read, including tables, equations, Chinese abstract, declarations and the adjacent B0037+B0127 and B0062+B0128 contexts. Reading coverage is not claim-verification coverage.
- A fresh metadata effort generated 11 raw captures, A01–A11, covering searches and original pages for the 20 base sources and two correction records. Final 22-record field-level closure was unfinished.
- All 14 current citation contexts were read. The frozen 48 uses remain INCONCLUSIVE, with zero new passage bindings. Metadata was not promoted to passage support.
- D1 Mode 2 submitted 49 actual quoted queries (48 English 10-word queries and one exact Chinese phrase) in 13 captured batches. Selected blocks cover the actual chain's modified/current additions and extra untouched chapters. Formal paragraph coverage accounting and final candidate adjudication were unfinished. The last batch returned no results. Broad unrelated returns were inspected; potentially relevant theorem-proving/provenance pages still needed comparison.
- The actual continuous revision bundle contains 13 + 37 + 20 = 70 operations over protocol rounds 1 → 2 → 3. All 13 Round-1 old/new operations and changed-prose comparisons for the first 27 Round-2 operations were inspected. The final manuscript was read, but the remaining operation-level E6 review was not completed.
- The Round-3 issue list and exact integrity authorization were read. They specify 20 allowed replacements under IL-MEDIUM-1 and IL-SERIOUS-1; no empty claim-strength array was treated as semantic clearance.

## Pre-stop observations, not finalized findings

The official [Takeuchi J-STAGE record](https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article) explicitly records CITATION and PDF FILE corrections dated 20 October 2006. The [Popescu chapter](https://link.springer.com/chapter/10.1007/978-3-031-51959-8_16) distinguishes first-online 2023 from the publisher's recommended 2024 citation. The [Strohmaier–Uski correction record](https://link.springer.com/article/10.1007/s00220-018-3094-z) exposes volume 359, page 427 (2018); no substantive correction effect was inferred. The Schmutz landing-page title spelling and Epstein–Holt competing pagination remained unresolved. The supplied EPFL source URL returned 405 and was not bypassed.

Uncited B0019/B0079/B0115 wording about literature or corpus “support” was flagged for final whole-context adjudication against the revised unverified reading-queue language. No severity was assigned. B0037 explicitly qualifies the immediately following B0127 comparator hypotheses, so the two must remain together. B0062+B0128 similarly limits the same-lineage 14/14 record to diagnostic agreement; original harness checks were unfinished.

## Work not completed

C original-artifact checks; all-field A adjudication; the per-use B ledger; D1 denominator and complete top-candidate judgments; D2 same-author comparison; the full E claim/byte-span registry; remaining E6 comparisons and issue closure; and seven-failure-mode/compliance adjudication remain incomplete. Shared same-author primary-response carriers were loaded as leads, but no P33 identity/similarity verdict was inherited or completed.

No official validator, scientific experiment, producer, fixture harness, manuscript/bibliography mutation, canonical promotion, Git mutation, or input repair was performed by this component.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

## Preserved artifacts

The detailed partial record is `notes/stage4_5_round3_p33_semantic_working_audit.json`. Existing captures `notes/stage4_5_round3_p33_web_A01.json` through `A11.json` and `notes/stage4_5_round3_p33_web_D01.json` through `D13.json` remain unchanged. This Markdown file and its JSON companion are work fragments only and must not be interpreted as the requested final Stage 4.5 result.

Sealing transcription caveat: the companion JSON's `bibliography_sha256` literal accidentally includes trailing byte-count text copied from an earlier compact record. It is explicitly non-authoritative and must not be consumed as a SHA-256 binding. This caveat preserves the original sealed field without silently overwriting it. The controlling batch lock, not this partial work record, supplies authoritative input digests. No input rehash was performed after STOP.
