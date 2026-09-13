# Round10 · Stage 4.5 Round3 — 修正准备完成，等待精确补丁确认

本次已完成证据复核、审查误报更正、版本化本地 reader 清单及五份精确补丁的准备与格式/锚点验证。**正文补丁尚未应用，五篇完整性 FAIL 保留。** 作者待确认事项与 E6 独立列出，不作为普通补丁准备的前置条件。

## 审查结论更正

P30 的 `IL-SERIOUS-1` 是审查误报：当前锁定书目中，S01/S02/S03 的更正 DOI 分别为 `10.1063/1.457669`、`10.1063/1.457672`、`10.1063/1.457670`，与保留的出版社来源元数据一致。上轮审查错误地把历史 S02 注记转写为当前书目字段；本次没有“修复”已经正确的书目，也没有改写旧报告。

因此普通问题由原记录 42 条调整为 41 条（SERIOUS 24、MEDIUM 9、MINOR 8）：25 条形成正文修正提案，16 条保留作者待确认。E6 仍为独立的 5 条。详见[审查更正附录](BATCH_ROUND10_STAGE4_5_ROUND3_AUDIT_CORRECTION_ADDENDUM.json)。

## 五份精确补丁

| 稿件 | 普通问题 / 修改块 | 拟议修正 |
|---|---:|---|
| [P29 补丁](papers/29-bianchi-ideal-owner-refinement/notes/stage4_5_round3_correction_patch.json) | 1 / 2 | 将算法范围否定收窄到保留的元数据记录；同步收窄 B0041 小节标题，不改变章节数或顺序。 |
| [P30 补丁](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round3_correction_patch.json) | 12 / 12 | 限定文献支持范围与双语摘要的设计属性；区分固定比较窗口与未实例化定理域；统一 cyclic-label symmetry 名称和 Gate6 状态；绑定新的有范围限制的 reader。 |
| [P31 补丁](papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round3_correction_patch.json) | 4 / 4 | 区分历史八条 ClaimIntent 与当前完整性；删除“最严格”比较性断言；统一 unresolved 诊断记录到 I_diag。 |
| [P32 补丁](papers/32-homology-cover-renormalization-uniformity/notes/stage4_5_round3_correction_patch.json) | 4 / 4 | 区分源材料范围与项目定义/实现义务；将远程字节一致描述限定为 2026-09-04 的历史记录，保留本轮 TLS 失败与当前未核实状态。 |
| [P33 补丁](papers/33-bolza-control-matched-census/notes/stage4_5_round3_correction_patch.json) | 4 / 4 | 限定为 48 个登记引用用途；承认 14 个合成诊断夹具；纠正 run_id/proof_type；把结论明确表述为条件性设计提案。 |

合计 25 条普通问题、26 个块；P29 的一条问题同时覆盖相邻标题与正文。完整旧/新文本、依据和作者待确认 ID 见各论文的 `stage4_5_round3_correction_candidate_blocks.json`，精确基稿、操作和全文 SHA-256 见[补丁确认清单](BATCH_ROUND10_STAGE4_5_ROUND3_EXACT_CORRECTION_PATCH_REQUEST.json)。

确认清单本身的 SHA-256：

`ddf2ebb85dfe2408eaae6bce0203a6e9c2d808f1a053407d9001aeac61ce6d54`

本次没有创建作者授权输入或授权 PASS 侧车。清单是待确认请求，不是确认已发生的记录。

## 作者与 E6

- [作者待确认清单](BATCH_ROUND10_STAGE4_5_ROUND3_AUTHOR_PENDING.md)：16 条涉及作者/地址、资金、利益、CRediT 及个人行为/责任的原声明。没有代填确认，也没有把它们改为 PASS。
- [E6 逐项记录](BATCH_ROUND10_STAGE4_5_ROUND3_E6_HANDLING.md)：P29 一条与 P30 两条历史漂移已由保留的后续正文收窄，历史发现不撤销；P31 的 `every → any` 与 P32 的精确段落免责声明恢复全文单列，未应用。P32 的 B0121 缓解说明保留。P33 为零条，无需 E6 处置。
- 五份普通补丁不包含上述两处 E6 恢复，不要求先取得这些额外选择。没有代作者生成 `restore`、`authorize_with_reason` 或 `pause` 的正式决定。

## 已执行的验证及边界

新 [P30 reader 清单](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round3_correction_reader_manifest_v1.json) 的 16 个选定本地文件绑定全部一致，且逐项区分历史与 Round3 审查所选的当前输入。旧 reader 的 `entries/7` mismatch 保留：新清单没有恢复旧 matrix 原始字节，也不是远程可用、永久归档或科学支持的证明。

[提案验证](BATCH_ROUND10_STAGE4_5_ROUND3_CORRECTION_PROPOSAL_VALIDATION.json) 使用官方 integrity-list 与 patch 的只读验证函数，检查了五篇基稿、清单、原文锚点、补丁格式、目标范围和结构分析；全部通过。**未验证作者授权，未应用补丁，未建立新稿/新 bundle，未编译 PDF，也未运行新的完整 Stage4.5 final-check。** 官方 Markdown 解析器未将 P29 的 LaTeX 小节命令分类为 heading；B0041 的标题文字变更仍明确单列需确认。

[保留性复核](BATCH_ROUND10_STAGE4_5_ROUND3_CORRECTION_PRESERVATION_CHECK.json) 核对 375 项锁定输入绑定、299 项上轮审查证据文件及 15 个科学目录，未发现变化。这是文件与字节范围检查，不是科学独立验证。原有 87 页预览、正文、书目、矩阵、旧 reader、旧 FAIL/STOP、canonical、Route、README/状态与 Git 均未改动；没有执行科学实验或对外发布。

## 当前暂停点

按照所用 [ARS Revision Patch Protocol 的 integrity-correction 分支](/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/skills/academic-research-suite/ars/academic-paper/references/revision_patch_protocol.md:81)，必须在展示精确补丁及 SHA-256 后取得确认，才能应用正文。当前范围授权没有被伪记为对后来生成字节的确认。

下一步可确认上述五份精确普通补丁（包括 P29 B0041 标题），允许生成版本化 notes-side 新稿并运行相应应用、连续 bundle 与修改内容复验；16 条作者声明和 5 条正式 E6 处置继续保持待确认/未决。该确认不等于作者身份或个人声明真实性证明，也不授权科学、Route、canonical、Stage5/6、发布或删除操作。
