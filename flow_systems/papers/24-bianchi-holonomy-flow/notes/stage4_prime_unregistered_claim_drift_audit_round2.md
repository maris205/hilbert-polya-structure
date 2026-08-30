# P24 Stage-4′ Round-2 Unregistered-Claim Drift Audit

Date: **2026-08-30**

Status: **PASS WITH MODEL-MEDIATED LIMITATION — no unauthorized strengthening found in the reviewed changes**

This is the Stage-4′ review required by the apply report's `unregistered_claim_drift_review_required=true` flag. It combines deterministic byte checks with a model-mediated semantic comparison. The semantic result is not a deterministic proof that no unregistered claim drift exists, is not the mandatory fresh Stage-4.5 E6 invocation, and does not advance the paper to Stage 5.

## Bound artifacts

- patch: `9b7a7dd19557488852abc5ddcd26ac431568f3dbe259ffb6da23ba44da4f6d97`;
- revised draft: `79735d058d965a35de10cc0b3655e0b1db5217bde00e02d2d48b7564cd841afc`;
- apply report: `484c1436c89733aab44fd35b1243af8443836e64cf3d4548cc31b83eb9fd6ce9`;
- token sidecar: `f398f4efb8da8f3871bae70fab46e2170db3643e8d5127ede4226259eb1ffbd8`;
- registered-surface replay: `622ca996f85a4737646581db061cd9793be096d28cab04bb523dc94c418c3403`;
- source-evidence sidecar: `d606e79c459065febe96432b8645e19ba6a1d6db1a9f299fdd13240f7f19e4b0`.

## Semantic comparison

| Item | Comparison of old block and added text | Direction |
|---|---|---|
| `REV-001` | The new text exposes exact source locators, assigns elementary mechanisms to antecedents, and repeats that the check is bounded and non-priority-bearing. It does not extend the theorem, claim exhaustive literature coverage, or assign the full Bianchi flow. | narrowed / source-bound |
| `REV-003` | The new text binds an already existing verify-only artifact chain. It adds no scientific value and repeatedly retains the matrix-row boundary, no-primitivity clause, incomplete owner quotient, and unchanged Route tuple. | same scientific claim, stronger provenance |

## Deterministic conservation facts

- all 10 registered surfaces occur byte-exactly once in their original registered blocks;
- all 10 patch operations carry empty `claim_strength_changes` and `collateral_authorization_ids`;
- 101/111 blocks are byte-identical to the base; section count and headings are unchanged;
- the token checker reports only expected additions from source locators, SHA fragments, and the 10-test provenance statement;
- canonical Round-7/Round-8 results were verified, not refreshed;
- the Route-A tuple remains `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, the full-flow tuple remains unassigned, and Route B remains uninvoked.

No reviewed change was found to strengthen an unregistered claim beyond its authorized evidence. Because that last sentence is a semantic judgment, the mandatory Stage-4.5 integrity gate must re-evaluate E6 independently before any later-stage promotion.
