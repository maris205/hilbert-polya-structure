# Round 9 Papers 24--28：Stage 4.5 与 Stage 4′ 批次报告

日期：**2026-08-30 UTC**

## 一、批次结论

本轮五篇论文均取得了明确、可核验的阶段进展，但当前形成两个彼此独立的授权关口：

- **P25 已完成当前 Stage-4 修订稿上的一次全新 Stage 4.5 完整性审计，结论为 `HOLD`：0 `SERIOUS`、0 `MEDIUM`、4 `MINOR`。** 四项问题均是定点书目元数据或勘误披露修复；精确补丁已经准备但尚未获授权、尚未应用。因此 P25 不能进入 Stage 5。
- **P24、P26、P27、P28 已完成 Stage 4′ 写入前准备，状态为 `PREPARED — AWAITING EXACT AUTHOR AUTHORITY`。** 六个残留评审项、51/51 个注册 ClaimIntent surface、目标块、操作和支持范围均已冻结并复验，但没有创建或应用任何 Stage 4′ 修订补丁。

本报告只汇总已经落地的审计和准备工作。它不是作者裁决，不授予修订权限，不提升任何 Route gate，不启动 Route B，也不授权 Stage 5、canonical manuscript/PDF promotion 或 canonical-results refresh。

## 二、五篇论文的明确进展

| 论文 | 本轮阶段 | 已落地结果 | 当前关口 |
|---|---|---|---|
| P24 | Stage 4′ pre-authority | 冻结 `REV-001`、`REV-003` 两个 `must_fix` 残留项；10/10 注册 surface 在当前稿中 exact-once | 等待六项批次请求中的精确作者授权；无补丁 |
| P25 | Stage 4.5 fresh audit | 8/8 references、13/13 citation contexts、114 claims、127 source-bound evidence rows、45/74 originality sample、6/6 experiment claims、75/75 tests 与 13 页隔离构建均完成；发现 4 个 MINOR 书目控制项 | 等待精确书目补丁授权；Stage 5 关闭 |
| P26 | Stage 4′ pre-authority | 冻结 `REV-02` (`must_fix`) 与 `REV-04` (`should_fix`)；17/17 注册 surface exact-once | 等待精确作者授权，其中 `REV-02` 还绑定两条 append-only 书目项；无补丁 |
| P27 | Stage 4′ pre-authority | 冻结 `REV-03` 一个 `must_fix`；10/10 注册 surface exact-once | 等待精确作者授权；无补丁 |
| P28 | Stage 4′ pre-authority | 冻结 `REV-02` 一个 `must_fix`；14/14 注册 surface exact-once | 等待精确作者授权；无补丁 |

P24/P26/P27/P28 合计为 **6 个残留项 = 5 `must_fix` + 1 `should_fix`**，以及 **51/51 个注册 surface = 10 + 17 + 10 + 14**。P25 与这四篇处在不同的合法分支，不能用其中一个授权替代另一个。

## 三、P25 Stage 4.5 全新审计

### 3.1 冻结目标

- 当前审计稿：`papers/25-three-disk-scattering-flow/notes/stage4_revision_round1.tex`
  - SHA-256：`39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835`
- 当前 canonical bibliography：`papers/25-three-disk-scattering-flow/paper/references.bib`
  - SHA-256：`de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6b`

本次审计未修改上述两份文件，也未覆盖项目 PDF 或 canonical result。

### 3.2 References 与 citation contexts

Fresh Phase A/B 审计覆盖：

- **8/8** 个注册参考文献均找到可核验记录；0 `NOT_FOUND`，0 DOI misdirection；
- **13/13** 个注册 citation context 均为 `SUPPORTED`；0 distorted，0 unverifiable；
- 8/8 个文献表条目均在正文中被引用；13/13 个引用命令均解析成功；
- 两篇 Gaspard--Rice 文献存在 publisher correction，但当前正文引用的是不依赖所更正公式的宽口径背景论述，支持关系仍成立。

这里的“fresh”仅表示本轮重新查询并记录了指定 DOI、出版社、学会、仓储或作者托管的主要来源。对于六个未返回更新记录的查询，结论仅限于**指定来源中未检出**，不等于证明世界范围内不存在更新。

审计载体：

- `papers/25-three-disk-scattering-flow/notes/stage4_5_reference_citation_audit.md`
  - SHA-256：`891a027ca49c7e8fbab8244ed4abc8f98630a7ca41b872e814ddb42f44f647b7`

### 3.3 Claims、evidence 与语义边界

- 当前稿注册 claim population：**114/114**；registry SHA-256：`9e333277db2225c1e9d68afadb1c55acdb7845a28a72cb896aca8bef0cd8b90b`。
- 机械候选检查记录 `candidate_unregistered_count=0`；coverage artifact SHA-256：`d8f9343806bbf42846f204a45a04ad4c7c07ae2eb7af3d5779da0d8b3cf61098`。
- 形成 **127** 条 source-bound evidence rows，覆盖 114 个唯一 claim ID；evidence rows SHA-256：`752504e737d4162dff1e189c878f4c1492054207cbd36752dfc6ff86cacce146`。其中 `captured_at` 是冻结的语义抽取事件字段；后续 builder replay 校验并复用精确字节，不重新铸造时间戳。
- Evidence source map 绑定本地冻结 artifact chain 和八个 fresh citation-audit carriers；SHA-256：`2134ef5b70b85d93882a6d9616c7e2d4e9e45566186525b245b096ecfe9bd711`。
- E6 的独立语义检查未记录 claim-strength drift；finding set 为空，SHA-256：`f618185110e7264805743072b4f866eb85db1b4eced4e50ed9f755a4572bc644`。

上述 `VERIFIED` 表示 claim 与指定证据载体之间的可追溯绑定通过，不应解读为对每条科学命题的独立证明。E6 是有协议绑定的**模型介导语义复核**，不是确定性无漂移证书、完备性证明或作者裁决。

### 3.4 数值、实验、构建与内部一致性

- **6/6** 个注册 experiment-backed ClaimIntent surface 与持久化结果、provenance 和正文表述对齐；
- fresh read-only replay：**75/75 tests PASS**，68 个锁定 artifact 通过；
- 物理回放 CSV 为 2,241 行，每个 `d/a in {29/5, 6, 31/5}` 几何各 747 行，其中每个几何 3 个 scalar-clock matches、744 个 disagreements；exact witness CSV 为 6 行；
- 两张表均完成逐项追踪；18 个数学与文档一致性 family 均通过本轮检查；
- marker-stripped 隔离构建得到 **13 页 A4 PDF**，0 undefined citations/references、0 missing characters、0 fatal errors、0 overfull boxes；
- 未 refresh canonical results，未改变 scientific value。

隔离构建的连续 PDF **并非 byte-identical**，因为构建过程嵌入可变元数据；因此这里只报告内容/日志层面的干净构建，不主张 PDF byte reproducibility。有限回放数据是 validation surface，不是 2,241 个独立统计样本，也不是 roof noncohomology 的第二份证明。

内部一致性审计：

- `papers/25-three-disk-scattering-flow/notes/stage4_5_phase_c_internal_consistency_audit.md`
  - SHA-256：`7265849d0ad465ec0847cff8e69d600c5815904cdc63afe719292657c2f158bf`

### 3.5 Originality 与 failure-mode 边界

- 当前英语正文段落母体为 74；确定性抽样 **45/74 = 60.8%**；
- Stage-4 新增或实质替换段落 **17/17** 全部纳入；
- 抽样结果为 38 个 `ORIGINAL / no indexed exact match` 与 7 个 `COMMON_KNOWLEDGE / formula-adjacent technical prose`；0 `PARAPHRASE`、0 `CLOSE_MATCH`、0 `VERBATIM`；
- 七类 AI-research failure-mode 中没有 `SUSPECTED`，但 Mode 7 保留 `INSUFFICIENT_EVIDENCE_WARNING`。

该结果只是一次受限的公开 Web 精确短语筛查。它不能替代 Turnitin、iThenticate、出版社 similarity report 或完整作者出版语料核查，也不能给出可靠的全局重复率；搜索索引、付费墙、翻译、图像文本和语义改写均可能漏检。

审计载体：

- `papers/25-three-disk-scattering-flow/notes/stage4_5_originality_failure_mode_audit.md`
  - SHA-256：`52a8364c4fc5f4020bc8e6a3c2d941a57dcd47b42eda0a73b2a3e751c1775567`

### 3.6 四项 MINOR 与 Stage hold

当前 Stage-4.5 issue count 为 **0 `SERIOUS` / 0 `MEDIUM` / 4 `MINOR`**：

| ID | 精确目标/操作 | 精确效果 |
|---|---|---|
| `IL-MINOR-1` | `B0001/replace_block` | 为 `GaspardRice1989Semiclassical` 增加 publisher erratum DOI `10.1063/1.457672` 的 note |
| `IL-MINOR-2` | `B0002/replace_block` | 为 `GaspardRice1989Exact` 增加 publisher erratum DOI `10.1063/1.457670` 的 note |
| `IL-MINOR-3` | `B0006/replace_block` | 为 `Ruelle1976` 增加 publisher-record issue `number = {3}` |
| `IL-MINOR-4` | `B0008/replace_block` | 将作者形式规范为 `author = {Liv\v{s}ic, A. N.}` |

精确 correction list：

- `papers/25-three-disk-scattering-flow/notes/stage4_5_integrity_correction_list.json`
  - SHA-256：`f25c80eae179acd0f50d948447000f775575a0c962ea9de3627c87d6d9c217c7`

精确补丁：

- `papers/25-three-disk-scattering-flow/notes/stage4_5_integrity_patch_round1.json`
  - SHA-256：`c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc`

精确授权请求：

- `papers/25-three-disk-scattering-flow/notes/STAGE4_5_INTEGRITY_CORRECTION_AUTHORIZATION_REQUEST.md`
  - SHA-256：`72743007c76cff3079252f00ba23c64b4aa810f095b743c37552ed7e5567243e`

补丁 schema、base hash、target、old hash 与结构比例检查均已通过，但 **patch application 未执行**。四项均不包含 claim-strength change、collateral authorization、正文修改或 scientific/canonical-result 变化。Stage 5 只有在精确授权、补丁应用、零开放问题 fresh rerun 和 mandatory scholar checkpoint 均完成后才可能开放。

## 四、P24/P26/P27/P28 Stage 4′ 写入前准备

### 4.1 六个冻结残留项

| 论文 | Item | Round-2 verdict | Obligation | Proposed manuscript target/operation |
|---|---|---|---|---|
| P24 | `REV-001` | `PARTIALLY_ADDRESSED` | `must_fix` | `B0015`, `B0032`, `B0034`, `B0104` / `replace_block` |
| P24 | `REV-003` | `PARTIALLY_ADDRESSED` | `must_fix` | `B0056`, `B0065`, `B0067`, `B0068`, `B0075`, `B0084` / `replace_block` |
| P26 | `REV-02` | `PARTIALLY_ADDRESSED` | `must_fix` | `B0029`, `B0030`, `B0031`, `B0092` / `replace_block` |
| P26 | `REV-04` | `CANNOT_VERIFY` | `should_fix` | `B0080`, `B0081`, `B0082`, `B0083`, `B0093` / `replace_block` |
| P27 | `REV-03` | `PARTIALLY_ADDRESSED` | `must_fix` | `B0040`, `B0041`, `B0042` / `replace_block` |
| P28 | `REV-02` | `CANNOT_VERIFY` | `must_fix` | `B0048` / `replace_block` |

每一项的完整 support scope，以及 P26 `REV-02` 的两条条件性 append-only bibliography entry，均在精确授权请求中逐项列出。没有提出或授权 registered claim-strength replacement。

### 4.2 已完成验证

- official `revision-roadmap/1.0` schema、base-draft/block-manifest hashes、块顺序/hash replay、target existence/order 与 residual count：**4/4 PASS**；
- official `claim-surface-manifest/1.0` schema、roadmap/base binding、ClaimIntent source hashes、UTF-8 offsets、block containment、non-overlap 与 exact-once：**4/4 PASS**；
- 独立 whole-draft exact-once：**51/51 PASS**；
- scope-to-filesystem/request projection：**4/4 PASS**；六个 frozen Stage-3′ Round-2 residual projection：**6/6 PASS**；
- builder 隔离重放：**10/10 generated outputs byte-identical**，对象为四个 roadmap、四个 claim-surface manifest、batch scope 和 authorization request；
- 已有 P24/P26 support-output receipt bindings：**4/4 PASS**；
- 没有创建 Stage 4′ author-adjudication sidecar 或 revision patch。

此处的 10/10 byte identity 仅指上述生成型 JSON/Markdown 控制产物的隔离重放，不应延伸解释为 PDF byte reproducibility 或科学数值的新确认。

控制产物：

- `BATCH_ROUND9_STAGE4_PRIME_PREPARATION_REPORT.md`
  - SHA-256：`401cac4bbc9e1f5145ff4b00266afb140b1e5b5250f2a464fbe6980235cc4300`
- `BATCH_ROUND9_STAGE4_PRIME_SCOPE_MANIFEST.json`
  - SHA-256：`96206b64bc893493e499ab4c317c5a0e0316ca125d6e096826389173a7d09327`
- `BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md`
  - SHA-256：`d2e94cd10b1ca12204c8747b5bc0895f6c642e3a3ff7c08194016ed62fd461ec`

## 五、与 Route A / Route B 路线图的对应

本轮继续受以下两个仓库路线定义约束：

- `skills/route-a-evaluator.md`
  - SHA-256：`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- `skills/route-b-evaluator.md`
  - SHA-256：`170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`

Stage 4.5 的证据完整性检查和 Stage 4′ 的授权准备都不产生新的 A0--A4 科学证据，因此所有冻结 tuple 保持不变：

- **P24 proxy**：`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` / `ROUTE_A_EXPLORATORY`；full Bianchi flow 仍为 `UNASSIGNED`。
- **P25 unit-roof symbolic calibrator**：`(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` / `ROUTE_A_REJECTED`；physical three-disk flow 仍为 `UNASSIGNED`。
- **P26 registered finite owner multiset**：`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` / `ROUTE_A_EXPLORATORY`。
- **P27 residual candidate**：`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` / `ROUTE_A_REJECTED`；distinct homology calibrator 为 `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)` / `ROUTE_A_REJECTED`。
- **P28 full tuple**：`UNASSIGNED`；historical proxy 为 `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` / `ROUTE_A_EXPLORATORY`。

所以，positive arithmetic candidates reaching A2 仍为 **0/5**，Route-B invocation 仍为 **0/5**。五篇论文均未提出满足 Route B 入口所需的同一对象上的完整 Hilbert space、operator/domain、self-adjointness、spectral type、prime-power trace 和 determinant identity；Route B 不能被有限回放、论文修订或 clean build 代替。

## 六、动力学系统初始限定与模型计数

本轮没有制造新的动力学类型，仍保留五个连续时间子类型及其冻结初始限定：

1. torsion-free cusped Bianchi 3-flow proxy，且完整 Bianchi flow 不因有限 proxy 获得 tuple；
2. no-eclipse equilateral three-disk exterior billiard，物理几何冻结为 `d/a in {29/5, 6, 31/5}`；另有严格分型的 no-repeat `q`-symbol unit-roof suspension，`q=2,...,8`，不得把 symbolic clock 转授给 physical roof；
3. positive Level-11 newform time change；
4. residual inverse-limit geodesic candidate 与 distinct nonresidual homology-cover calibrator，owner、tower、clock、normalization 和 finite-panel scope 均保持分离；
5. nonarithmetic genus-two geodesic control 与 magnetic precursor，尚未以 Stage-4.5/Stage-4′ 文书动作补做 matched magnetic census 或完整 tuple。

计数仍为 **12 个冻结 geometry/physics parameter instances + 7 个 `q`-symbol analytic calibrators = 19 个 bookkeeping model instances**。这 19 个实例不是 19 个统计独立样本；它们共享论文级假设、生成机制和控制结构。本轮没有增加子类型、没有改变初始限制、没有改变任何科学数值。

## 七、精确授权关口

### 7.1 P25：书目 MINOR 修复

下一项可写操作需要明确绑定以下精确补丁：

`c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc`

所需授权必须覆盖四个且仅四个 target/operation pair：

`IL-MINOR-1 B0001/replace_block`；`IL-MINOR-2 B0002/replace_block`；`IL-MINOR-3 B0006/replace_block`；`IL-MINOR-4 B0008/replace_block`。

授权仍不得扩展为 collateral edit、claim-strength change、canonical-results refresh、正文修改或在该授权步骤中直接修改 `paper/references.bib`。任何 hash/precondition/validator 失败、structural flag 或超范围需求都必须停下请示。

### 7.2 P24/P26/P27/P28：Stage 4′ 六项作者裁决

下一项可写操作需要明确绑定请求：

`BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md`，SHA-256
`d2e94cd10b1ca12204c8747b5bc0895f6c642e3a3ff7c08194016ed62fd461ec`。

作者需要为六项逐一选择 `will_address`、`wont_address` 或 `not_on_point`。若全部批准，紧凑授权也必须明确：六项均为 `will_address`；全部列明 block/operation pair 与 support scope 获授权；P26 两条精确 append-only bibliography entry 获授权；不授权 claim-strength replacement；canonical/Route freeze 继续有效。

通用的“确认、继续”足以让审计和写入前准备继续推进，但不会自动产生上述两个关口的 exact write authority。两个请求必须分别满足，任何一个都不能替代另一个。

## 八、当前停止点

批次当前状态可压缩为：

```text
P25: Stage 4.5 fresh audit complete -> HOLD (0 serious / 0 medium / 4 minor)
P24/P26/P27/P28: Stage 4′ pre-authority prepared -> 6 exact decisions pending
Route A: tuples frozen; no new gate credit
Route B: uninvoked
Canonical manuscripts/PDFs/results: frozen
```

下一轮真正的写入工作，必须从相应 exact authorization 开始，而不是从推断授权或重放旧授权开始。
