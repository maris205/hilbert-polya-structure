# Paper 28 Stage 4 unregistered-claim drift audit

Date: **2026-08-30**

Status: **PRELIMINARY STAGE-4 PASS — NO UNAUTHORIZED CLAIM-STRENGTH MOVE FOUND IN THE FOUR CHANGED OPERATIONS**

This is the manual Stage-4 review required by the apply report's
`unregistered_claim_drift_review_required=true` flag. It is deliberately
preliminary and bounded to the four authorized Stage-4 operations. It is not a
Stage-4.5 E6 invocation, does not emit an E6 finding/disposition artifact, does
not claim complete semantic recall, and does not advance the pipeline to Stage
3 prime or Stage 4.5.

## Bound artifacts

- patch SHA-256:
  `37f8ac948f1d8a6aab65f16f10d916d89629208d341871e22f0710cb1fe4ef12`;
- revised anchored draft SHA-256:
  `884ca28dacf24cabe6f5473c67cb55bdfd1491e87eb6bd763aab7646cfce1bb2`;
- apply-report SHA-256:
  `3ccc1c7987b791fe3e708766a92094e66107c0671c3e53c87806f2ed369bd8b8`;
- final response SHA-256:
  `045e6510d125f58c40ef9abb3e802419349da60f41b1cfa7bc2a4e2afca91929`;
- revision-evidence-bundle SHA-256:
  `93ea0ae450ac06db827de266d38c0d5cc550757789e2a2766f9cf945dc692d9f`;
- marker-stripped preview receipt SHA-256:
  `90aad833c8114f66ec68cd07f63ad1b9a8f05cb720da42331d15db169d42243f`;
- registered-surface replay SHA-256:
  `487e3bba9c56f1fea454de54de4d0e52c56c0a82a675ca484b3b4bff7a57127a`;
- token-conservation advisory SHA-256:
  `b91b9382de67f418a93367527a465ae5ad904349bdc27831e8e30f4a72c2c2da`;
- direct invariant/replay receipt SHA-256:
  `f235c254dcbad3930556ca0142255ae23d7da904c5fa3395cf3605bc11bb0b11`.

## Semantic findings

| Roadmap item | Manual comparison result | Strength direction |
|---|---|---|
| `REV-01` | B0099 now follows the audited execution order: proof guards and finite traversal/reconstruction precede `build_validation`; validation and explicit refresh remain mandatory before canonical writes. The correction changes no theorem, scientific value, result count, or canonical-result hash. | factual method correction; no scientific promotion |
| `REV-02` | B0048 retains its original invariant account and adds only the executed direct-test record: repeated Delta cancellation, global-negation idempotence, both generator/inverse orders, and sampled collisions. It expressly states that the tests import the audited builder and are not an independently implemented closure checker. | supported bounded addition |
| `REV-03` | B0126 defines the A0–A4 obligations while keeping the formal P28 tuple unassigned and the historical proxy `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` unchanged and unpromoted. The exact control systole/cutoff remains A0–A1 infrastructure, and 144 remains an element-level count. | narrowed and clarified boundary |
| `REV-04` | B0125 types only the constructed control-surface, exact group-state, geodesic-length, and target-blind-cutoff interface. Magnetic, owner, determinant, analytic, and spectral objects remain separately typed and unconstructed; no A2/A3/A4 or Route-B inference is added. | clarified interface; no promotion |

## Numerical-token advisory adjudication

| Advisory | Exact source of the added tokens | Disposition |
|---|---|---|
| `ADV-REV-1` — B0048 | The values 585 words and 457 canonical states, the four generators, and identity/order notation reproduce the executed Stage-4 invariant receipt. | supported by the bound receipt; no new theorem or independent-closure claim |
| `ADV-REV-2` — B0106/B0126 | The repeated value 144 is expressly qualified as equality-achieving group elements only. | existing result restated with a narrower owner boundary |
| `ADV-REV-3` — B0037/B0125 | `PSU(1,1)`, the already frozen cutoff `21/10`, and 144 occur inside the authorized typed interface and its explicit negative inference boundary. | existing inputs/results restated; no Route credit |

## Conservation checks

- all **14/14** registered ClaimIntent surfaces occur byte-exactly once in the
  revised anchored draft;
- all four authorized roadmap items are `RESOLVED` through four operations,
  each with empty `claim_strength_changes` and
  `collateral_authorization_ids` arrays;
- the marker-stripped word count changes from **5,600 to 5,986** (`+386`);
- no citation key or bibliography entry was added;
- the combined direct/legacy run passed **28/28** tests; the verify-only replay
  passed its 24-test suite and produced two identical temporary tree hashes;
- the canonical Round-8 result bytes were not refreshed and no scientific
  value changed;
- the formal full P28 tuple remains `UNASSIGNED`; the historical proxy remains
  `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`;
- Stage 4 supplies A0–A1 control-side infrastructure only, with no Gate
  promotion and no Route-B invocation.

Within this preliminary four-operation review, every new claim-bearing phrase
is either the authorized method correction, receipt-backed direct-test
description, or a narrowing interface/Route qualification. No hidden
claim-strength promotion was found. A later Stage-4.5 E6 run, if separately
invoked, remains a fresh checkpoint-closing semantic process and is not
prejudged by this document.
