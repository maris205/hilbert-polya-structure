# Round 9 Papers 24--28 — Stage 4 Exact Authorization Request

Date: 2026-08-30 (UTC)

Status: `AWAITING_EXPLICIT_AUTHOR_ADJUDICATION`

The message `确认，继续下一轮` confirms continuation after Stage 3, but it does not by itself state one author triage decision and one exact target/operation scope for every roadmap item. No manuscript, code, result, test, or canonical experiment artifact has been modified under that message.

## Frozen authority bindings

| Paper | Roadmap SHA-256 | Anchored base SHA-256 | Block manifest SHA-256 | Claim-surface manifest SHA-256 |
|---|---|---|---|---|
| 24 | `9617cd604bccdb8484883362165723e505c8d0f4d22ffa82ac5e9f82f88a41f0` | `b59bc70c51960f6c89167619df21923c035b4311d9df4e40c034a1fe036cf60e` | `c0a86683ac4137831c80b11dd06b2369c7fb8b96cbd01b2f7b8b5e723f6dc2e0` | `2af286143812b1fdd1d1242df2868a8a75f375fa5cd9c1f1f0ff1b2472ce5d64` |
| 25 | `ec77e5a53f2d5e937909732992be8139cbc2486f86fa5aa0faec1b54a8cd37a2` | `4c3af70463340eab57c7ed9db6b88c2a6d64f88b2f03b058b3527573da375f70` | `4f386b130e29c032ecbef86fd06e21fcfde36c7737b8f79801c3bbcb1e307f30` | `323d27b42fb2e1208cd477297123b45370460913195ac5792d61ded5884b25b9` |
| 26 | `e58163c3796bde9eb524c972e44023c6afaf4f7885f1d55b2859886cc7216438` | `af61f7b9a80b95bbc15c937ff0af3eed1ecc327965679324c51c376ad9dbb836` | `29f3d9fecdc8c11273a15298310ff58b27641d58d592d0f7d49d773a65e932a4` | `d1ad38e0b7e71949abc0bc22a35bfce5ff6e1f5133067d8f8bcf8c4b4f52309e` |
| 27 | `fe8a2c1d828d04404a9bffb42468266d73530a819beb26e24314bb88ec37add4` | `e74f592f6ee907fb25712de0eb2b09359af09848d6cee458bd0a565d7a58f20e` | `276a946006d54e59f27b3abd3224f116885655c8bb9dc0df237770c8abcdd531` | `00dc5e76ab6ca776979ecdc8368a928d23d287e27319ddb591b78fc91fe33012` |
| 28 | `721a659d16f7f0c07d0cf8bca6bac298067855c8a19aa643179e0825c5a74bcf` | `743a047cbe5f6227fbfaa5fef3169029b339af5790218df4ddf8f7cac2987f59` | `e70d9d74f0e1396938b75e7908e2f86008a5934cb635f8393bc7f5595c9774c0` | `269a55d6e2590dc2e0bac8c9b98f5e10f63def23e31f2c7871526fc583f5c5e2` |

All five roadmap + base + block-manifest + claim-surface tuples replay successfully with the ARS `revision_roadmap.py render` validator.

## Proposed author disposition and exact manuscript scopes

The proposed batch decision is `will_address` for all 33 source-ordered items. Every row below authorizes exactly the listed roadmap-proposed block/operation set. The patch may use a subset; it may not broaden the set.

### Paper 24 — 8 items

| Item | Class | Exact proposed target/operation authority |
|---|---|---|
| `REV-001` | `must_fix` | `B0015/replace_block`, `B0032/replace_block`, `B0034/replace_block`, `B0104/replace_block` |
| `REV-002` | `should_fix` | `B0004/replace_block`, `B0006/replace_block` |
| `REV-003` | `must_fix` | `B0056/replace_block`, `B0065/replace_block`, `B0067/replace_block`, `B0068/replace_block`, `B0075/replace_block`, `B0084/replace_block` |
| `REV-004` | `should_fix` | `B0030/replace_block`, `B0033/replace_block`, `B0074/replace_block` |
| `REV-005` | `should_fix` | `B0049/replace_block` |
| `REV-006` | `should_fix` | `B0093/replace_block`, `B0096/replace_block` |
| `REV-007` | `must_fix` | `B0023/replace_block`, `B0054/replace_block`, `B0084/replace_block`, `B0099/replace_block` |
| `REV-008` | `must_fix` | `B0072/replace_block`, `B0084/replace_block`, `B0100/replace_block`, `B0104/replace_block` |

Implementation defaults: run a new loxodromic-only profile from already frozen exact rows; make no primitive-owner claim without a certified witness; use historical/self-reported freeze wording unless independent dated evidence is already present; use level-subgroup conjugacy as the operative proved owner equivalence; define the missing third control as an unexecuted matched-distribution noncongruence matrix ensemble with a predeclared persistence/non-persistence prediction. Preserve the author, affiliation, email, and non-title metadata in `B0004` exactly.

### Paper 25 — 6 items

| Item | Class | Exact proposed target/operation authority |
|---|---|---|
| `REV-001` | `must_fix` | `B0013/replace_block`, `B0026/replace_block`, `B0033/replace_block`, `B0105/replace_block`, `B0108/replace_block` |
| `REV-002` | `should_fix` | `B0018/replace_block`, `B0033/replace_block`, `B0090/replace_block`, `B0091/replace_block`, `B0108/replace_block` |
| `REV-003` | `must_fix` | `B0015/replace_block`, `B0062/replace_block`, `B0078/replace_block`, `B0079/replace_block`, `B0084/replace_block`, `B0102/replace_block`, `B0108/replace_block` |
| `REV-004` | `should_fix` | `B0082/replace_block`, `B0109/replace_block` |
| `REV-005` | `should_fix` | `B0109/replace_block` |
| `REV-006` | `should_fix` | `B0082/replace_block`, `B0109/replace_block` |

Implementation defaults: classify the 2,241-row replay as solver/reproducibility validation rather than additional proof; create one unified machine-readable Stage-4 reproducibility lock that binds the environment, bibliography, Round-2--8 source/test/input/output bytes, and reproduction commands; preserve all funding, conflict, contribution, ethics, and AI-use declarations in `B0109` exactly except for the Data and code availability pointer. Heading-only targets `B0062` and `B0084` will not be touched unless a later structural checkpoint is explicitly approved.

### Paper 26 — 9 items

| Item | Class | Exact proposed target/operation authority |
|---|---|---|
| `REV-01` | `should_fix` | `B0004/replace_block` |
| `REV-02` | `must_fix` | `B0029/replace_block`, `B0030/replace_block`, `B0031/replace_block`, `B0092/replace_block` |
| `REV-03` | `should_fix` | `B0041/insert_after`, `B0076/replace_block` |
| `REV-04` | `should_fix` | `B0080/replace_block`, `B0081/replace_block`, `B0082/replace_block`, `B0083/replace_block`, `B0093/replace_block` |
| `REV-05` | `should_fix` | `B0042/insert_after` |
| `REV-06` | `should_fix` | `B0062/insert_after` |
| `REV-07` | `must_fix` | `B0013/replace_block`, `B0014/replace_block`, `B0041/replace_block`, `B0076/replace_block`, `B0089/replace_block`, `B0090/replace_block`, `B0092/replace_block` |
| `REV-08` | `must_fix` | `B0014/replace_block`, `B0015/replace_block`, `B0031/replace_block`, `B0075/replace_block`, `B0077/replace_block`, `B0087/replace_block` or `B0087/insert_after`, `B0092/replace_block` |
| `REV-09` | `must_fix` | `B0040/replace_block` or `B0040/insert_after`, `B0046/replace_block`, `B0071/replace_block`, `B0080/replace_block`, `B0082/replace_block` |

Implementation defaults: keep every theorem and conclusion bounded to the registered 138-instance/55-group correspondence-component multiset; regenerate the Round-8 dependency manifest/receipt with transitive project-source closure and fail-closed hash checks without changing canonical result bytes; run a matched exact control decomposition for `REV-08` when it can be derived from the frozen definitions without target-label fitting, otherwise take the roadmap's conservative generic-obstruction branch; express the primitive-root completeness argument locally. To obey one-op-per-block, use `B0041/insert_after` for `REV-03` and address `REV-07` through its other authorized blocks; use a single `B0040/replace_block` for `REV-09`.

### Paper 27 — 6 items

| Item | Class | Exact proposed target/operation authority |
|---|---|---|
| `REV-01` | `consider` | `B0004/replace_block`, `B0015/replace_block` |
| `REV-02` | `should_fix` | `B0015/insert_after` |
| `REV-03` | `must_fix` | `B0041/replace_block`, `B0042/replace_block` |
| `REV-04` | `must_fix` | `B0006/replace_block`, `B0008/replace_block`, `B0012/replace_block`, `B0014/replace_block`, `B0016/replace_block`, `B0067/replace_block`, `B0086/replace_block`, `B0094/replace_block` |
| `REV-05` | `should_fix` | `B0024/insert_after` |
| `REV-06` | `must_fix` | `B0006/replace_block`, `B0008/replace_block`, `B0015/replace_block`, `B0022/replace_block`, `B0073/replace_block`, `B0087/replace_block`, `B0094/replace_block` |

Implementation defaults: adjudicate `REV-01` as `will_address` while retaining `criteria_binding_unavailable`, a field-general title/position, and no venue-fit or submission-readiness claim; add a direct `-I` scalar-sign fixture and report any shared-kernel limitation honestly; use the comparative-methods/calibration-note framing unless an exact source comparison supports a narrower theorem-level increment. To obey one-op-per-block, use `B0015/insert_after` for `REV-02` and address `REV-01`/`REV-06` through their other authorized blocks.

### Paper 28 — 4 items

| Item | Class | Exact proposed target/operation authority |
|---|---|---|
| `REV-01` | `must_fix` | `B0099/replace_block` |
| `REV-02` | `must_fix` | `B0048/replace_block` |
| `REV-03` | `should_fix` | `B0106/insert_after` |
| `REV-04` | `should_fix` | `B0037/insert_after` |

Implementation defaults: correct the replay order; add and execute direct tests for repeated Delta cancellation, global-negation normalization idempotence, generator/inverse multiplication order, and sampled canonical-state collisions; do not refresh canonical results; add only field-general typed maps and the exact A0--A4 obligation chain.

## Claim, collateral, structural, and Route boundaries

- `display_order.mode = source_traceability` for every paper.
- All 33 items are proposed as `will_address`; therefore `collateral_authorizations = []`.
- All 57 non-overlapping registered ClaimIntent surfaces remain byte-identical; `claim_strength_authorizations = []`. Five shorter nested ClaimIntent strings cannot be simultaneously registered under the non-overlap schema and remain mandatory E6 semantic-audit surfaces.
- No exact claim-strength replacement is authorized. If a registered claim cannot remain exact, stop and present its full replacement text, hashes, rungs, direction, and reason for a new author event.
- No structural acknowledgment is granted. A heading edit, section-count change, or touched ratio over the default threshold stops at the mandatory structural checkpoint.
- Route-A tuples remain unchanged. This round may strengthen evidence and paper clarity, but it grants no A2/A3/A4 promotion.
- Route B remains uninvoked and unauthorized. No prime/zero table, target-zero fitting, log-prime roof, von-Mangoldt weight, determinant identity, spectral realization, venue submission, publication, or later pipeline stage is authorized.
- Supporting code/test/provenance writes are limited to the named Stage-4 reviewer obligations. Canonical result refresh is forbidden unless separately approved; a failed test, changed scientific value, or required target-scope expansion stops before write-through.

## Exact confirmation text

To authorize the batch in one event, the author can confirm the following paragraph verbatim or equivalently:

> 我批准 `BATCH_ROUND9_STAGE4_AUTHORIZATION_REQUEST.md` 中 Papers 24--28 的全部 33 项 Stage-3 revision roadmaps 与所列实现分支，并将每项均裁决为 `will_address`：P24 `REV-001--REV-008`、P25 `REV-001--REV-006`、P26 `REV-01--REV-09`、P27 `REV-01--REV-06`、P28 `REV-01--REV-04`。授权每项表中列出的全部 `proposed_targets` 与 `allowed_operations`，按 `source_traceability` 顺序进入 Stage 4；无 declined item、无 collateral authorization、无 registered ClaimIntent claim-strength replacement，57 条已注册 ClaimIntent 保持原字节。另授权仅为这些路线图义务创建、修改和执行文中明确列出的辅助分析、依赖/来源 manifest、receipt 与直接回归测试，但不得刷新 canonical results；测试失败、科学数值变化、registered claim 必须改写、结构性修改或超出 target scope 时停止并另行请示。Route-A tuple 不变，Route B 与后续 Stage 未授权。
