# Round 10 接续记录：模型切换后的历史校准

校准日期：2026-09-05 UTC。性质：接续说明与证据索引，不是授权回执、完整性终审结论或阶段晋升记录。

**最新接续入口：见第 12 节。第 2–5 节是模型切换时快照，第 7 节是已完成的 Round-2 审计收口；第 8–11 节保留后续修订准备、应用、排版恢复及双语范围预检的历史停点。**

## 1. 持续目标与用户偏好

- 研究按 `skills/route-a-evaluator.md` 和 `skills/route-b-evaluator.md` 对应推进，以相对完整的论文作为主要交付物；每批五篇，每篇须有可说明的实质进展。
- 保留动力学系统的初始限定；可探索不同子类型，但不能把事后调参、改变时钟/owner/归一化或目标数据拟合冒充原系统成果。
- 分开记录论文流程进展与科学路线图进展。论文、引用或审计检查通过，不自动取得 Route-A 积分，也不代表新定理或新实验成立。
- 用户希望需要决策时只回复简短“确认”；已有授权继续有效，不因模型切换而重问。确认的具体作用由当时的明确请求和检查点确定。
- 常规交付偏好是更新 README 的结论概要，并通过 SSH 同步到 `maris205/hilbert-polya-structure` 的 `flow_systems/`。当前审计阶段的特定冻结边界仍需遵守。
- 作者 Liang Wang；既有作者、单位、邮箱、贡献声明沿用；资助无，利益冲突无；引用保持 `natbib[numbers,sort&compress] + plainnat` 数字制。

## 2. 当前准确位置

**Round 10，Papers 29–33，Stage 4.5 Round 2 审计尚未完成批次收口。** 当前授权是一次新鲜完整性审计及记录其结果所需的审计侧产物。

授权依据：

- [授权记录](BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECORD.md)
- [授权回执](BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT.json)，SHA-256 `139631992e610beb9ffc2e5b72c1ee5022bed87460d95b3c5da7812dd3b2db60`
- [输入锁](BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK.json)，SHA-256 `11875bf33e0318997c385d0d89bde3a7987bb9166b18967994ccb3ca5ac44bb0`

当前授权不包含正文/Bib/源矩阵/科研代码/实验/结果/初始系统变更、canonical 晋升、README 或 pipeline-state 改写、Git 同步、Stage 5/6、投稿或新一批论文。接续说明不扩大这份授权。

旧的 `BATCH_ROUND10_PAPERS_29_33.md` 和 README 含历史阶段状态，不能据此把当前审计退回 Stage 2/3；它们仍保留为历史交付证据。

## 3. 五篇论文与路线图位置

| Paper | 冻结研究对象与论文方向 | 当前科学位置 |
|---|---|---|
| P29 | 固定 level-(3) Gaussian Bianchi 单位速测地流；literal Gaussian-prime-ideal owner；区分机制许可与商完备性 | A1 owner/完备性准备；机制与商证明仍未闭合 |
| P30 | `d=6a` 无遮蔽等边三圆盘物理流；Euclidean free-flight clock；物理 roof 与 determinant 的六门槛和误差合同 | `A0_FAIL / A2_NOT_ELIGIBLE`；尚无物理 determinant 证书 |
| P31 | 固定正时间变换的 `Gamma_0(11)` 测地流；有向 primitive owner；138 实例、55 组、9,453 pair 的冻结设计 | A1 canonicalization/owner ledger 准备；未执行 owner census |
| P32 | 纯 genus-two homology-cover tower；时间 `1/N`、对数重数 `1/N^3`；higher/zero-content 优先证伪 | 一般 A1–A2 证伪准备；无正式 A0 结论或均匀性证明 |
| P33 | Bolza `b=1/2` even subtype 与固定非算术 genus-two 对照；`Lambda=21/10` | A1 证书语义准备；`P33-RC-1=0/7`；无 matched census |

本批 formal Route-A tuples、positive arithmetic A2、A3、A4、Route-B invocations 均为 `0/5`。这不抹除方法论文层面的进展，也不能被误读成整个项目从未获得任何历史结果。论文编号不能直接充当独立动力学系统种类数。

路线图 SHA-256：A `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`；B `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`。

## 4. 本次实际复核的文件状态

主审调用现有 finalizer 的 `protected_boundary_replay()` 进行只读复放：119 个锁定文件绑定全部通过；15 个 canonical 文件、15 棵 science tree 和受保护 README/pipeline-state 均通过；受保护文件变更数为 0。该检查不是完整批次终审。

P30/P31 当前 controlling output manifest 仍为 **attempt 5**：

- P30：`42ecd80e6e63d8ac10e1c97afad2fc81c4a94e81f0d21f5f9120778daefc40ec`
- P31：`c2d8cf1a26f9479de1b1d1e27369d9c4037d68ff5e117b128e3d9eeffeb3453e`

未晋升的 attempt-6 TEMP8 候选保留在：

- `/tmp/r10-p30-p31-semantic-temp8a.lenS0X/candidate`
- `/tmp/r10-p30-p31-semantic-temp8b.SkP7xM/candidate`

切换前主审已确认这两次构建的 46/46 文件相同，并对 TEMP8a 跑过官方 evidence/schema 检查：P30 542 rows、P31 2,470 rows 通过。两位原复验代理随后报告额度错误；没有最终独立复验交付，不能把此前“正在检查”升级成 PASS。

**新发现的接续差异：** TEMP8 绑定 builder `d9a30a36...`，而磁盘上的 builder 已变为 `0abf32c6...`。TEMP8 的历史通过结果仍可保留，但不支持当前脚本的新运行；需复核脚本末次修改并重建候选。

校准时工具摘要：

| 工具 | SHA-256 |
|---|---|
| `tools/rebuild_round10_stage4_5_p30_p31_dispatch.py` | `0abf32c6b1c93a07db5d233d5edde4b16fffc1b8578eef2e1613c17efa7fba9e` |
| `tools/audit_round10_stage4_5_round2.rb` | `45816948d44caaefaf8d06b655c96b5e9b100a612826a7b1987ed0c49b080840` |
| `tools/finalize_round10_stage4_5_round2.py` | `4d4af205a4ede3f8e71721c0bb5d6a0e3f60e3c594eac25a8b6e34fdb0e28b6a` |

另一个环境差异：当前可用 ARS 插件为 `0.1.28`，原 `0.1.26` 缓存路径已不存在，上述审计工具仍引用旧路径。应先核实依赖和版本兼容性、记录真实运行工具版本，再执行后续复放；不得把新版本工具冒记为旧版本已复验。

独立只读核对已找到保留的原版插件：`/root/autodl-tmp/.codex/.tmp/marketplaces/.staging/marketplace-upgrade-0JRs4e/plugins/ars-codex`，其 `plugin.json` 标记版本 `0.1.26`。其中 `evidence_rows.py`、`claim_registry_coverage.py`、`check_compliance_report.py`、`_block_parser.py` 与当前 `0.1.28` 的对应文件 SHA 相同。原工具并未完全丢失；路径适配及其依赖范围的复核仍待执行。本次未改插件或审计工具。

根目录尚无 `BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_INDEPENDENT_REPLAY.json`；finalizer 中的独审 SHA 仍为 `TO_BE_FROZEN_AFTER_POSTREPAIR_REPLAY`。批次最终报告、最终回执与精确定点修订请求尚未生成。

## 5. 可继承的审计发现与待完成顺序

当前候选/收口器拟汇总 797 条 registered claims：686 VERIFIED、98 UNVERIFIABLE、13 MAJOR_DISTORTION；拟定 17 个问题、66 个正文 replace_block 目标及 1 个 P30 后继 Bib 定点更正。这些是待最终复验的汇总口径，尚非已获作者批准的修订，也非批次正式收口结论。

复验必须保留的重点：P30 E050 的实际五席评审角色与正文四角色枚举不符；P30 E052 全 ClaimIntent 字段；P30 E107 仅接受当前授权审计执行的窄证据；P31 Phase-6 全字段与历史锁链；E117 `retraction_unrun`；E125 的 metadata-only 身份证据和 stale reader-manifest mismatch。共享网络采集器的精确路径在 P30 notes 下，不能伪造 P31 独立采集器或把未留存的 HTTP 原始正文宣称为可重算证书。

接续顺序：

1. 解决 ARS 工具路径/版本兼容性，复核 builder 在 TEMP8 之后的修改；使用真实生成时间重建审计候选。
2. 针对新候选完成两路独立复验及主审复放，冻结实际工具、证据与清单哈希。
3. 在现有审计侧授权内归档旧包、发布经复验的审计包；核对 119 个绑定、science trees、完整 root replay。
4. 生成真实的最终独审记录；校验后冻结其 SHA，再生成批次报告、回执、检查点与精确修订请求。
5. 将论文阻断项交给作者进行已约定的简短确认；不重复索取已经存在的审计授权。

## 6. 以后如何接续

用户明确要求与原始授权事件用于判断权限；当前受锁定的文件、执行回执和实际复放用于判断事实；本说明和会话压缩摘要用于定位材料。出现冲突时回到原始证据核对，不让“记得做过”替代执行记录。

原始历史文件与会话保持不动。本说明只提供入口；未修改 Codex 内部记忆文件、记忆开关、插件安装或模型设置。模型切换本身不清除已完成的项目文件，也不能证明所有历史细节都已完整进入当前上下文。

官方说明把客户端的持久记忆与模型上下文分开，并建议将必须遵守的项目规则保存在项目文档中，记忆仅作辅助检索层：[Memories](https://learn.chatgpt.com/docs/customization/memories)。本记录采用文件核对作为接续依据，不推断此客户端的具体记忆开关，也不推断 GPT-5/GPT-6 之间未核实的内部记忆差异。

## 7. 已完成的本次接续与当前停点

2026-09-05 UTC：**Round 10 / Papers 29–33 / Stage 4.5 Round 2 已完成审计收口；五篇论文尚未定稿。** 审计包复放 PASS，五篇科学完整性 disposition 仍全部 FAIL，Stage 5 未开始、未获授权。这不是新论文批次，也不是新动力学实验轮次。

正式依据：

- [完整性终审报告](BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_INTEGRITY_REPORT.md)
- [批次机器审计](BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_AUDIT.json)，SHA-256 `82966cd48562301fd86a5b2d86fdf52f56d6c22cdb79f90e683fb0009826de25`
- [最终验证回执](BATCH_ROUND10_STAGE4_5_ROUND2_VALIDATION_RECEIPT.json)，SHA-256 `271f992a54abc7797d981b9c9b3996956ddc8668ff4672ef76c71eace5b80a26`
- [最终独立执行复放](BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_INDEPENDENT_REPLAY.json)，SHA-256 `2596f8caa15c91a04f7bb33d69bbc231f0e2154df6d6bc01f1e1db50d304094f`，23171 bytes，真实生成时间 `2026-09-05T04:14:02Z`
- [强制检查点](BATCH_ROUND10_STAGE4_5_ROUND2_MANDATORY_CHECKPOINT.md)

实际全量 root replay 已通过 89/89；主审、分别执行的复验代理及 finalizer 都实际运行了对应完整检查。119 个锁定绑定、15 个 canonical 文件、15 棵 science tree 和 README/status 受保护边界通过，变更数为零。多代理为同模型家族的分角色复验，不是跨模型或错误过程独立证明。

本批核查了 126 条参考文献、156 个引用上下文、797 个注册 claims（686 VERIFIED / 98 UNVERIFIABLE / 13 MAJOR_DISTORTION），对应 3953 条 EVR。P29–P32 的 3502 个组件和 EVR/claim 是不同分母，不得混用。这些是审计数量，不是科学样本或新实验。

接续过程中已经完成：

1. 对 ARS 0.1.26 保留版与当前 0.1.28 的实际四个 helper、三个 schema 做字节等同性核对，只适配工具路径；见 [运行时兼容记录](BATCH_ROUND10_STAGE4_5_ROUND2_RUNTIME_COMPATIBILITY.md)。旧 TEMP8 临时目录在再次接续时已不可用，不作为当前恢复源。
2. 按真实时间生成 TEMP9，P30/P31 的 46 个文件通过定点、批次及主审复放后按原字节发布。旧 attempt-5 审计材料分别归档 43/38 个，未删除。
3. 首次完整 root replay 真实出现 88 PASS / 1 FAIL：P31 S23/S24 分母旧断言漏计 E067 两条缺失证据。仅修复审计谓词为精确 5×2 组件集合，保留十条 UNVERIFIABLE；负向测试通过。原 validator 及失败经过保留于 [计数修复记录](BATCH_ROUND10_STAGE4_5_ROUND2_VALIDATOR_COUNT_REPAIR.md)。
4. P30 E107 只重绑定新 validator 的 SHA/bytes；仅五个 JSON、十二个叶值变化，EVR、历史 incident/lineage 和 P31 全包不变。前一 TEMP9 P30 包的 44 个文件另行归档。随后完整 root replay 达到实际 89 PASS。
5. 冻结真实最终独审 SHA 后，finalizer 成功生成六份收口产物。最终工具 SHA：builder `c24f848afc99f10e6301b159c57cfa82e408dd45073a996a338c1d9cfd85fb8c`；root validator `b432c4a7b008f0ebea92590d0bb051fc18239fc315704f4d6ba635c2fe76eafc`；finalizer `7396dad339f2cf25b89de32941e95ebcf31c04d42ec0c2f02a661fd8985f732d`。finalizer 在路径适配之后仅再将独审 SHA 占位符替换为真实冻结值。

当前 P30 controlling manifest 为 `ef82adeebd08e2b6532f2c84ee997da942a923bee7d2f44f62188b10a7e07919`，P31 为 `20de4b1356282d0e931335d838ae4920c2f9bed22653da605e484c401e84ed12`。第 4 节的 attempt-5 描述符现为历史值。

### 下一次简短确认的精确含义

[修订请求说明](BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.md) 对应 [机器请求](BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_AUTHORIZATION_REQUEST.json)，SHA-256 **`d9be18e2199dd64100a1482018eb9bf77586e2548ba751cc0c2b57e06195f992`**，87787 bytes。目前状态为 `AWAITING_EXPLICIT_AUTHOR_CONFIRMATION_NOT_AUTHORIZED_NOT_APPLIED`。

| Paper | 已记录问题数 | 精确正文块目标数 | 修订方向 |
| --- | ---: | ---: | --- |
| P29 | 2 | 20 | 纠正翻译状态；缩限缺少原始载体的复合表述 |
| P30 | 6 | 11 | 更正引用关系、角色枚举和过期状态；缩限未支撑归属与元数据；另有 1 个后继 Bib 更正 |
| P31 | 4 | 8 | 缩限方法来源和文献否定；修正过期 reader manifest 依赖与元数据 |
| P32 | 3 | 7 | 纠正翻译状态；明确 closest-work 与本地载体缺口 |
| P33 | 2 | 20 | 缩限缺少原文段落支撑的表述；取消同链 synthetic harness 的证据性解读 |

用户在看到这一请求及其 SHA 后回复简短“确认”，只授权 66 个精确 `replace_block`、一个 P30-S02 后继 Bib 项更正、列名的 notes-side 衍生物、隔离预览和新的 Stage 4.5 Round 3 审计，随后停在其检查点。当前尚未收到该确认，不能把此前的“继续”追溯解释为已批准这份新请求。

路线图 A 与五个初始系统保持第 3 节原限定，本批 formal tuple/正向算术 A2/A3/A4/Route B 仍各为 0/5。本次没有新科学执行、正文修订、正式 PDF 晋升、README/status 更新或 Git 操作。用户对最终 README 概要和 SSH 同步的长期偏好保留，不能在当前冻结范围内提前执行。

## 8. 作者已确认范围；修订准备因官方格式校验失败暂停

作者随后回复了“确认”，已记录在 [范围授权说明](BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_SCOPE_AUTHORIZATION_RECORD.md)。第 7 节的范围请求已获确认，但没有把这次事件伪记成对尚未生成的五份具体补丁哈希的批准。当前 ARS integrity-correction 分支要求具体补丁确认后才能 official apply。

主审开始准备五份规范 issue-list 适配器与 writer handoff 时，官方 `revision_roadmap.validate_integrity_correction_list` 拒绝了 P31 EA-003 的目标排序。确认清单采用正文物理顺序 `B0016, B0112, B0037, B0038`，规范要求编号顺序 `B0016, B0037, B0038, B0112`。这是准备代码的排序问题；目标集合不变。由于范围请求明确规定任何官方校验失败即停，主审未自行修补后重试，三路写作任务均已停止。

完整失败经过、实际零写入的补丁状态及下一次简短确认的限定恢复范围见 [准备停止记录](BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_PREPARATION_STOP.md)。现有 helper SHA-256 为 `e30adabbbd64763c59f10cdabf750c06736ce13f42cb43d14c4fcc3183d07459`，尚未实施排序修复。

所有基稿和旧审计包保持原字节，119 个锁定绑定复放通过，受保护变更 0。五份具体补丁、writer handoff、后继稿和 Bib 后继均未产生；Stage 4.5 Round 3 尚未开始。

已完成的只读工作可继承：三个写作代理分别完整阅读 P29/P32、P30/P31、P33 基稿及各自的修改范围和 ARS patch 规范。P30/P31 的相关原始缺口已阅读，P29/P32 的逐靶组件阅读尚未全部完成。恢复时先取得对这个排序缺陷的限定修复方向，再修准备 helper、生成规范 handoff，继续原五篇补丁，不重启新批次、不重复已有完整基稿阅读、不改科学结论。

## 9. 排序恢复已完成；五篇具体补丁待统一确认

2026-09-05 UTC：作者对限定排序恢复方案回复“确认”，见 [恢复事件与执行记录](BATCH_ROUND10_STAGE4_5_ROUND2_CORRECTION_PREPARATION_RECOVERY_RECORD.md)。第 8 节的停点已解除，原失败历史保留。准备 helper 仅新增按 ARS `_target_key` 排序，当前 SHA `0aebdffb90012d6eb4b4d129c7b92508e3b89d93da8400d9c419179798512060`。五份 issue-list 官方校验已实际通过，原 66 个目标与允许操作完全不变，11 个 handoff/issue-list/receipt 文件已生成。

三路写作已完成五篇 patch 与逐块日志：P29/P30/P31/P32/P33 分别为 20/11/8/7/20 个 `replace_block`。P30-S02 的一处 Bib note DOI 更正另有精确提案。主审已阅读全部拟文；写作角色之外的代理交叉阅读 P29–P32，主审检查 P33。该分工不证明跨模型或错误过程独立性。P32 B0018 根据反馈补足了对未改表格及表后结论的明确限定，其早期提案从未获作者批准或应用。

五份官方 issue-list 和只读 patch phase-1 校验全部 PASS，无结构标记；这不是 official apply 的授权 PASS，更不是科学完整性 PASS。生成物发布后，75 个描述符出现项与实际文件字节再次核对成功；119 个受锁定绑定、15 个 canonical 文件、15 棵 science tree、16 个 README/status 边界文件均未改变。

当前入口为 [具体补丁统一确认说明](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_APPROVAL_REQUEST.md) 与 [机器请求](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_APPROVAL_REQUEST.json)，机器请求 SHA-256 **`759480e724b818c5068233134712a14a4736df116ca295578495912f3a86a42d`**，26066 bytes。前置验证回执 SHA `ad9d0f57e98e97a38c019e9dbf1744acbb412d55817d0535946266dea251e7cd`；生成工具 `tools/prepare_round10_stage4_5_round2_exact_patch_approval.py` SHA `dbff7baab0691e48639558630a81001e809ada22c8f18f4be4e1896d210c23c4`。

| Paper | 待批准 patch SHA-256 |
| --- | --- |
| P29 | `4bbe3a59ece85174835f9ab119d607646630eb9bde4eec5309bb35f6b36dbdbc` |
| P30 | `697f33e2e3353f2ec12fc61df98c2418c3b4f955a1b672dd86907c37d32d45a0` |
| P31 | `abb4ff59da32b708126e9daa0199ce91d84f4fc1beedfca77d4f2c7fae3f3b0c` |
| P32 | `0d2336a73c6c1ca6a5f4e52d2ae19b699b211e78a377c1a55e948a85d89cdb2e` |
| P33 | `2ba62c388f042bf014b0ef985a338d2c43b725c904bb1b0a107556ad015cc445` |

Bib 提案 SHA `8329b90cba6be8b3e9443013a0e9cb8991acaf520a9f6c20c3ed4585aafc31aa`；只改 P30-S02 的 note 内 `10.1063/1.457669`→`10.1063/1.457672`，其他字节不变。没有生成后继 Bib。

作者下一次在看到本请求精确 SHA 后的无保留“确认”，才能转录为五份具体 patch 的逐问题授权输入，使用正式 builder 生成 sidecar 后 official apply。不得把先前排序确认或范围确认当成这份新 patch 字节的批准；任何提案字节变化都需新确认。执行仍受原 scope 限制：仅列名 successor、矩阵/reader manifest、隔离预览和 Stage 4.5 Round 3，并停在新检查点；任何校验/构建失败、科学/结构变化或必要的超范围修改都停下请示。

[提交前阅读注意](BATCH_ROUND10_STAGE4_5_ROUND2_PATCH_PREAPPLICATION_READING_NOTES.md) 不是新完整性 verdict。尤其 P29 B0006 只按授权替换了翻译状态句，其他繁中措辞的跨语言范围歧义如实保留；B0109 的历史 Round-1 FAIL 也不等于最新状态。尚需复验的问题不得标成已解决，更不得暗增改写范围。最近实际完成的 Stage 4.5 Round 2 仍为五篇 FAIL，本次 patch 尚未应用，隔离 PDF 构建和 Round 3 均未开始，Round 10 五篇未定稿。

本次未做新动力学/科学执行、路线晋级、canonical 晋升、README/status 更新或 Git 同步。Route A、五个初始系统以及 0/5 formal tuple/正向算术 A2/A3/A4/Route B 边界保持原样。

## 10. 五篇正文已应用；三份 PDF 通过，P32 断行失败触发暂停

作者随后确认了第 9 节具体补丁包。真实新事件记录在 `BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_AUTHOR_EVENT_20260905.txt`，不同于之前范围/排序事件。逐篇 `stage4_5_round2_correction_author_input.json` 经官方 ARS builder 生成 `stage4_5_round2_correction_integrity_authorization.json`，五份授权 witness 均实际 PASS。根 [具体授权回执](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_AUTHORIZATION_RECEIPT.json) SHA `3f4e15e8aa07d9c6aa1e24297c19edaab594695f472d6a70c8e4e8ae9512478d`，41621 bytes。

五份完整旧 bundle 先实际通过官方 replay，随后五篇均由正式 `ars_apply_revision_patch.run()` 应用，无结构 override；66 个拟文逐块完全吻合，558 个未改标记块保持字节一致。后继块 manifest 和新完整 bundle 也已生成并通过官方 replay。P30 的已批准 Bib 后继已创建，只有单一 note DOI 变化。

| Paper | 正式后继稿 SHA-256 | 隔离预览状态 |
| --- | --- | --- |
| P29 | `8d6294051fe03de2c433e5d7115bcc0b73e8ac66504b17542a3700ef1762be10` | Round4 PDF，16 页，PASS_CLEAN |
| P30 | `9a38c81279303ac81a20914d7a2be70056b6c7b568eef2640ebe3665d54399de` | Round4 PDF，18 页，PASS_CLEAN |
| P31 | `ba7d12ec9bf2766c37fcdb9504f49ba08392ac078c21897587e3ba57fdc85750` | Round4 PDF，16 页，PASS_CLEAN |
| P32 | `af56c1c68fd514faace8ef546ac38976255b753d662ddfb3e8aad0fbfc1e5073` | Round4 构建 FAIL，不发布失败 PDF |
| P33 | `aa3783e6a24f830918ccb88b8dc5ebb28d9c15a94d87ffdb907cf5da9e049d6d` | Round3 PDF 尚未构建 |

[应用与接链回执](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_APPLICATION_RECEIPT.json) SHA `799c3ee37e73a29d562b350a80c2d26ec60499990c781321f5608be2d3c3204f`，26759 bytes。不要重做 apply，也不要覆盖它们或倒退到第 9 节的未应用状态。P33 的旧协议轮为 1→2，本次协议轮为 3；历史 patch 文件名 round6 只是准备迭代名，不能把它误当协议轮。P29–P32 当前协议轮均为 4。

P29 正式 apply 后，主线程附加的只读字节比较误用了不存在的 `Block.raw_text` 字段，命令因此中断，尚未处理其他四篇。官方 apply 本身已成功；主线程读实际解析器接口，用 `full_start/span` 核实 P29 95 个未改块及 20 个新文本全等后，仅继续四篇尚未应用的补丁。没有改批准字节或官方工具，见 [局部诊断接口错误记录](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_LOCAL_DIAGNOSTIC_INCIDENT.md)。生成接链 sidecar 的第一份终端输出还曾被传输 token 上限截断，apply_patch 未接收任何文件；扩大完整接收窗口后重新生成并发布，未改正文。

获批四份矩阵（P30/P31 round3、P32 round4、P33 round3）和 P31 reader round3 已由三路写作者用 apply_patch 生成，各有 `notes/stage4_5_round2_derived_materials_receipt.json`，仅做了生成方基本结构/绑定检查，主审与新完整性审计尚未完成。精确输出 SHA、bytes 和状态已统一列在下述执行停点 JSON，不得把它们算成 Stage 4.5 PASS。

**当前真正阻断：P32 隔离构建。** `tools/build_round10_exact_patch_previews.py` 是本轮受限构建器，SHA `b7f2052d5fac684457acfdadc580c5b4bd5b893708b17135b1bc74c7cc3f3f0f`。P32 于 2026-09-05T07:00:16Z 的四条编译命令全部 exit 0，但其新中文摘要 B0007 状态句在临时源 lines 66–67 产生 572.49495 pt 的单一 Overfull hbox。缺字、未定义引文、未定义交叉引用、fatal 均 0；零溢出标准未通过，已按明确停止条件停下，所有代理收到停止通知。失败 build receipt SHA `df1b5dbee8dddf387a1af457d3f0cf3bee035cb2e972f3f840c1fac67a07ec28`，原日志与 `/tmp/round10-exact-p32-jg0h9put` 保留。不能自行忽略 warning、修正文或重试。

当前 [执行停点 JSON](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_EXECUTION_STOP.json) SHA **`27edd1e5c9a0bb3d75d919f402ba33beb6943b25e5af01db45d21caa8e895ea0`**；[中文停点说明](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_EXECUTION_STOP.md)。Stage 4.5 Round 3 尚未开始，最新完成的科学完整性 disposition 仍是旧 Round2 五篇 FAIL。

### 下一次确认只授权 P32 临时排版恢复

[P32 仅预览恢复请求](BATCH_ROUND10_STAGE4_5_ROUND2_P32_PREVIEW_RECOVERY_REQUEST.json) SHA **`78aeff4125881c496c65352a023b567649ffcff239f2a2610c39e54714258b08`**，6902 bytes。作者下一次在看到它的精确 SHA 后无保留回复“确认”，只授权：先保留当前构建器，再加入 P32 专用、完整稿哈希和精确片段双绑定的临时编译变换；在原中文状态句的相邻汉字间插入已列明的 115 个 `\allowbreak{}`，删除这些标记后必须严格恢复原句。**不改工作稿或 patch**，不用新的正文修订链，也无需重新批准五篇已应用补丁。

P32 新输出必须采用请求列明的 `stage4_prime_revision_round4_preview_attempt2.*`，保留旧失败日志，收据明确临时排版变换、不再宣称只有 marker stripping；零 overfull/undefined/missing-glyph/fatal 门禁不变。P32 成功后才做 P33 首次预览，再复核既有衍生物、锁定当前新稿输入并开展已授权 Stage 4.5 Round 3，随后停在该检查点。不要重建已经成功的 P29–P31 PDF，不改 README/status/Git、canonical 或科学结果。

## 11. P32 恢复与五份预览完成；P29 双语范围预检暂停

2026-09-05 UTC：作者对第 10 节 P32 精确临时恢复请求回复“确认”。已生成真实新事件、record 与授权 receipt（SHA `92b9eee054597a88fe4edac24eeb1235c809cefce0bf1c039b5acb4e4df8cde1`），仅新建 `tools/build_round10_exact_patch_previews_p32_recovery.py`，原 builder 原路径原字节保留。P32 attempt2 实际于 07:38:25Z 完成、19 页、五项阻断诊断零；P33 实际于 07:39:11Z 首次构建完成、18 页、五项零。P29–P31 没有重建。五篇共 87 页，均为 notes-side preview，不是正式终稿。

五篇实际输入/回执/临时编译变换和全部受保护边界已经主线程复核，见 [预览完成回执](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_PREVIEW_COMPLETION_RECEIPT.json)。P32 新回执 SHA `2b8eb8d3a8fc148fe3886e4aadf1dafc094fe164266c0175928f4bb76aa1b13f`；P33 新回执 SHA `ea12c0c4059abd227064335687a0c75a86912bd8c846040be1a1b0d0039c0787`。P32 旧失败回执、旧日志、五份批准 patch 与工作稿全部保持原字节。

四份新矩阵和 P31 reader 已由非其写作者的角色分别交叉阅读，分区与当前绑定匹配，但并非 A–E 或科学 PASS。当前新阻断是 P29 B0006 原有中文“文獻足以界定…卻未提供…也未完成…”仍可能独立读成整体文献充分性/缺席结论，和 B0004 新英文的显式限定不一致。主审与另一角色实际联读后认为须缩限；此前 B0006 仅批准定位状态子串，不允许此次顺手改写。

已暂停下游并请求这一句的新限定修订范围；**没有新 patch 或 successor，也没有正式开始/完成 Stage4.5 Round3**。旧 Round2 五篇 FAIL 仍为最近完整审计结果。具体句子、拟文、五份可读 PDF、已核对证据、接续的旧 builder 陷阱均见 [最新预检停点](BATCH_ROUND10_STAGE4_5_ROUND3_PREFLIGHT_STOP.md)。下一次简短确认是这一句的准备范围授权，不能伪造对尚未生成的具体 patch SHA 的批准；正式应用仍须按 ARS 精确确认流程。

当前仍在 Round10 五篇和 Route A 原限定内，未做科学执行、canonical 晋升、README/status/Git 或 Stage5/6。不要重做已完成的五份补丁、P32 恢复或五篇预览，不要用第 8–10 节历史停点覆盖本节最新事实。

## 12. P29 单句范围已确认；具体单块补丁已准备并通过前检

2026-09-05 UTC：作者对第 11 节 P29 B0006 单句修订准备范围回复“确认”。本次新事件及含义记录在 `BATCH_ROUND10_P29_B0006_SCOPE_AUTHOR_EVENT_20260905.txt` 和 `BATCH_ROUND10_P29_B0006_SCOPE_AUTHORIZATION_RECORD.md`。这不是具体补丁 SHA 的确认，也不是已应用记录。

已生成规范的局部预检 correction-list 适配器和 writer handoff；主线程实际调用官方 `validate_integrity_correction_list` 通过，manifest 与当前整稿块序列一致。适配器明确来自局部预检，不伪称完整 Stage4.5 Round3 已运行。写作者完整读当前稿后只生成一个 `B0006/replace_block`，没有重出整稿或改写 ClaimIntent。

[具体 patch](papers/29-bianchi-ideal-owner-refinement/notes/stage4_5_round3_preflight_b0006_patch.json)：SHA-256 **`f9ece4cb8ba64c6270b63443bdef09240b5648e3d745dcf2131218e643629362`**，2049 bytes。仅将 STOP.md 所列 258-byte 旧句替换为 336-byte 新句；B0006 其余文字和其他 114 个块不在修改范围内。其余五篇稿件、PDF 与衍生材料保持现有字节。

非本补丁写作者实际核对了整个 JSON、handoff、原句/拟句和稿件绑定；主线程另行调用官方 `ars_apply_revision_patch.validate_patch` 的只读 phase1：PASS，无结构标记。119 个锁定绑定、15 个 canonical 文件、15 棵 science tree 和 16 个 README/status 文件的保护复放通过，变更为零。这些是提案/边界检查，不是应用授权或完整性 PASS。记录见 [前置验证回执](BATCH_ROUND10_P29_B0006_PREAPPLICATION_VALIDATION.json)，SHA `7fe6225b47400515ab3e06298610585fe82b57fdb753482a4a1d50b16311bc50`；[局部语义阅读](BATCH_ROUND10_P29_B0006_PREAPPLICATION_READING.md)。

当前待确认入口：[精确补丁说明](BATCH_ROUND10_P29_B0006_EXACT_PATCH_APPROVAL_REQUEST.md) 与 [机器请求](BATCH_ROUND10_P29_B0006_EXACT_PATCH_APPROVAL_REQUEST.json)，请求 SHA **`87407696aba59cad12c8c0737c69caad2cb6797cea6c9d024fd313206c639d96`**。唯一待作者决定为 `IL-MEDIUM-1 / authorize / B0006 / replace_block`。下一次在看到这份具体请求和 patch SHA 后无保留回复“确认”，才能转录为官方作者输入、生成授权后正式应用。任何 patch 字节变化都需新确认。

确认后 P29 输出为新的 `stage4_prime_revision_round5.tex` 及连续 round5 bundle/manifest/apply report；只对 P29 构建新预览，保留所有已有版本，再执行原五篇 fresh Stage4.5 Round3 并停在其检查点。P29 revision round5 是连续写链索引，不是第五次完整性审计。当前只有内存预期正文 SHA `4f43bdbdfcfc3e1a784e1d1641b39cf3c818faa2ef8f5ac8ce613deab4d1726a`/63707 bytes，**没有输出新正文、bundle 或 PDF**。

准备工具 `tools/prepare_round10_p29_b0006_exact_approval.py` SHA `fec1927dbf9dadcd5e87d8ea40cb08fe3c1c8c058c09fb59477fdd16cf9b9239`。不要再次运行其写包入口覆盖已有产物，也不要重做五篇既成 apply/预览。原 Stage4.5 Round2 五篇 FAIL 仍为最近完整审计，Round3 尚未启动；路线图 A、初始系统、科学结果、README/status/Git、canonical 与 Stage5/6 边界不变。
