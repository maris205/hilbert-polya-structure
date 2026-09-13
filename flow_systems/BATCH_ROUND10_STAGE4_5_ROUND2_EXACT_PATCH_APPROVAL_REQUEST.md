# Round 10：五篇精确补丁统一确认包

状态：补丁已准备并通过只读格式、哈希和范围检查，**尚未应用，尚未进行新一轮完整性审计**。仍为 P29–P33 这五篇，不开启新批次。

机器请求：[BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_APPROVAL_REQUEST.json](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_APPROVAL_REQUEST.json)

SHA-256：`759480e724b818c5068233134712a14a4736df116ca295578495912f3a86a42d`；26066 bytes。

回复一次“确认”，将批准下列五份具体补丁字节及各问题的列明目标/操作，以及一处精确 Bib 更正；不需要手工抄写哈希或长授权文本。

| 论文 | 正文替换块 | 精确补丁 SHA-256 |
| --- | ---: | --- |
| [P29](papers/29-bianchi-ideal-owner-refinement/notes/stage4_5_round2_correction_patch.json) | 20 | `4bbe3a59ece85174835f9ab119d607646630eb9bde4eec5309bb35f6b36dbdbc` |
| [P30](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round2_correction_patch.json) | 11 | `697f33e2e3353f2ec12fc61df98c2418c3b4f955a1b672dd86907c37d32d45a0` |
| [P31](papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round2_correction_patch.json) | 8 | `abb4ff59da32b708126e9daa0199ce91d84f4fc1beedfca77d4f2c7fae3f3b0c` |
| [P32](papers/32-homology-cover-renormalization-uniformity/notes/stage4_5_round2_correction_patch.json) | 7 | `0d2336a73c6c1ca6a5f4e52d2ae19b699b211e78a377c1a55e948a85d89cdb2e` |
| [P33](papers/33-bolza-control-matched-census/notes/stage4_5_round2_correction_patch.json) | 20 | `2ba62c388f042bf014b0ef985a338d2c43b725c904bb1b0a107556ad015cc445` |

P30 的 [Bib 更正提案](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round2_correction_bib_proposal.json)：仅将 P30-S02 的 note 字段纠正 DOI 从 `10.1063/1.457669` 改为 `10.1063/1.457672`；P30-C01→S01 与 P30-C02→S03 不变。提案 SHA-256 `8329b90cba6be8b3e9443013a0e9cb8991acaf520a9f6c20c3ed4585aafc31aa`。

[逐块原文/拟文差异](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_REVIEW.diff)；[只读前置验证回执](BATCH_ROUND10_STAGE4_5_ROUND2_PATCH_PREAPPLICATION_VALIDATION.json)。五份 patch 文件包含待批准的完整 new_text；未生成后继稿或 PDF，不将提案当成已落地论文。

主要修订内容：

- P29：纠正翻译状态，保留有支持的设计内容，撤回锁内缺少原始载体的完成性表述。
- P30：更正引用关系和五席评审描述，区分已完成旧审计与未验证的新修订，收窄未支撑的理论归属和 AI 历史表述。
- P31：撤回未核验的方法迁移与过宽的文献否定，明确旧 reader manifest 的绑定失效。
- P32：纠正翻译状态；将原文未绑定的 closest-work 对照限定为候选比较假设。B0018 与未改 B0132 表须连读。
- P33：将无原文支持的引用收窄为阅读候选；同源合成测试的 14/14 仅保留为运行诊断，不充当正确性或独立验证证据。B0037 与未改 B0127 比较段须连读。

确认后只在原有授权边界内执行官方 apply、列明的衍生矩阵/reader manifest、隔离预览和 Stage 4.5 Round 3，再停在其检查点。当前 Route A、五个初始动力学系统、canonical 稿件、科学代码与结果、README/status 均保持冻结；不执行 Git 同步，不进入 Stage 5/6。

依 ARS academic-research-suite 的 revision_patch_protocol，范围确认不能替代具体 patch SHA 的作者确认；本包不包含伪造的作者输入或授权 PASS。五篇上一轮完整性结果仍是 FAIL，前置机械检查通过不是论文通过。

[提交前阅读注意](BATCH_ROUND10_STAGE4_5_ROUND2_PATCH_PREAPPLICATION_READING_NOTES.md) 保留了尚需复验的语境问题：P29 繁中摘要的非状态句按精确授权保持原文，其范围仍有跨语言歧义；B0109 仍是历史 Round-1 状态说明。当前请求明确披露最新 Round-2 FAIL，不把这些问题记成已解决，也不据此暗增改写权限。
