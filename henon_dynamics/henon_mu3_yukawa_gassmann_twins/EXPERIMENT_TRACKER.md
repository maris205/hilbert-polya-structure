# HCS-C59 experiment tracker

Status: **PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

Date locked: 2026-08-16.

## 1. Milestone ledger

| milestone | current state | exact meaning |
|---|---|---|
| adaptive predecessor | PASS | C58 is released and frozen |
| mathematical target review | TARGET_LOCK_GO | historical target-selection gate passed |
| primary-source/non-salami review | TARGET_LOCK_GO | narrow instance claim clears selection; no absolute priority |
| primitive-element pilot | STAGED_PILOT_PASS | historical selection evidence; superseded by complete G1 evidence |
| graph automorphism pilot | STAGED_PILOT_PASS | historical selection evidence; superseded by complete G1 evidence |
| engineering implementation | PREFREEZE_CODE_RESULTS_PASS | exact 13-code/8-result tuple passed |
| theorem statement | THEOREM_TARGET_LOCKED | `THEOREM_PACKAGE.md` |
| code/results | PREFREEZE_CODE_RESULTS_PASS | promoted exact certificate/check/schema/manifest tuple |
| post-refresh machine audit | POSTREFRESH_PASS | independent hostile audit passed on promoted bytes |
| refreshed formal-doc audit | FORMAL_DOCS_PASS | independent read-only hostile audit passed on the updated aggregate |
| paper | PAPER_PENDING | no paper directory or build exists |
| release | NOT_RELEASED | no implementation commit, full-project manifest, Route archive, or promotion |

The historical Phase-1 `NO-GO` and target-selection pilots are superseded
chronology. Current machine authority is the promoted G0--G7 tuple, not the
pilot records.

## 2. Canonical gate tracker

| gate | canonical task | state |
|---|---|---|
| G0 | released-authority rebind | PREFREEZE_CODE_RESULTS_PASS |
| G1 | primitive integral orbit-sum resolvents and graph-label independence | PREFREEZE_CODE_RESULTS_PASS |
| G2 | complete Gassmann/minimality certificate | PREFREEZE_CODE_RESULTS_PASS |
| G3 | fixed-field, normal-closure, nonisomorphism, and zeta bridge | PREFREEZE_CODE_RESULTS_PASS |
| G4 | signed discriminant, signature, and exact support | PREFREEZE_CODE_RESULTS_PASS |
| G5 | complete ToM-140 local algebra | PREFREEZE_CODE_RESULTS_PASS |
| G6 | complete ToM-206 local algebra and branch independence | PREFREEZE_CODE_RESULTS_PASS |
| G7 | checker independence, mutation/rebound envelope, novelty, scope, and release discipline | PREFREEZE_CODE_RESULTS_PASS |

This map is copied only from `EXPERIMENT_PLAN.md`; no historical G-number map
is authoritative.

## 3. Exact target ledger

| target | locked value | state |
|---|---|---|
| group/order | (W(E_6)), 51840 | certified |
| subgroup orders/indices | 162/320, 162/320 | certified |
| SmallGroup IDs | `[162,11]`, `[162,19]` | certified |
| supports | (27+27), 81 | certified |
| invariant | scaled integral (eta) in (alpha_i=Ld_i) | certified notation |
| split witness | 692717 | certified |
| modular hashes | `21b304...`, `76fa808...` | certified |
| degree | 320 and 320 | certified |
| signature | `(16,152)` | certified |
| exponents | `(624,496,192,160)` | certified |
| signed discriminant | `+3^624*5^496*A^192*B^160` | certified |
| ramified support | exact eight C58 primes | certified |
| ToM-140 table | complete four/five row sets | certified |
| ToM-206 table | complete four/five row sets | certified |
| branch selection | false | certified scope leaf |

## 4. Status vocabulary

The authorized current status tuple is:

```text
PREFREEZE_CODE_RESULTS_PASS
POSTREFRESH_PASS
FORMAL_DOCS_PASS
PAPER_PENDING
NOT_RELEASED
```

Historical `TARGET_LOCK_GO`, `THEOREM_TARGET_LOCKED`, and `STAGED_PILOT_PASS`
records remain provenance, but they are not the current machine state.
`PREFREEZE_CODE_RESULTS_PASS` does not mean `RELEASE_FROZEN`.

## 5. Machine tuple ledger

| item | certified value |
|---|---|
| inventories | code 13; results 8; live 21; scoped 20 |
| source tests | 48 PASS |
| payload scalar leaves | 10,412 |
| mutations rejected | 20,894 certificate; 8 evidence rebound |
| payload SHA-256 | `a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b` |
| payload shape SHA-256 | `788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2` |
| G0 SHA-256 | `ac445822702b5e376eed6fbfa86a4df81c7f8177ca35c8211282dca830123d5d` |
| certificate SHA-256 | `3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a` |
| check-report SHA-256 | `271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3` |
| schema SHA-256 | `07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4` |
| group-evidence SHA-256 | `0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958` |
| resolvent-evidence SHA-256 | `667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6` |
| scoped-manifest SHA-256 | `c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda` |

The certificate/manifest-bound `results/RESULTS.md` and
`results/TEST_REPORT.md` intentionally retain their pre-promotion,
source-stable wording. Their bytes are bound by the scoped manifest inside the
certificate/check-defined inventory, so editing them after certification
would invalidate the manifest and destroy the source-stable promoted tuple.
Their prose is historical build-layer metadata, not the official live-status
authority; the certificate, independent check report, scoped manifest, and
`POSTREFRESH_PASS` audit are authoritative.

## 6. Paper and release ledger

| artifact/gate | state |
|---|---|
| paper source inventory | PENDING / absent |
| PDF, log, extracted text | PENDING / absent |
| compilation report | PENDING / absent |
| paper hostile audit | PENDING |
| code commit | null |
| provenance commit | null |
| scoped code/results manifest | present; 20 entries; hash above |
| full-project manifest | absent |
| Route archive | absent |
| promotion authorized | false |
| release status | NOT_RELEASED |

## 7. Next actions

The independent refreshed formal-document audit and new root-aggregate bind
are complete. Next build and audit the paper, then complete the implementation
commit, full-project manifest, Route archive, promotion, and release gates.
No paper or release PASS is inferred from the machine or formal tuple alone.

The inherited scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
