# Round 10：五份预览完成；P29 双语范围预检暂停

日期：2026-09-05 UTC。本文是已执行预览、材料交叉阅读与范围预检的记录，不是完成的 Stage 4.5 Round 3 Integrity Report，也不是新增正文写入授权。

## 已完成的结果

作者对 P32 临时排版恢复请求回复“确认”。事件、范围及精确请求绑定已落在 `BATCH_ROUND10_STAGE4_5_ROUND2_P32_PREVIEW_RECOVERY_AUTHORIZATION_RECEIPT.json`，SHA-256 `92b9eee054597a88fe4edac24eeb1235c809cefce0bf1c039b5acb4e4df8cde1`。

只在 P32 临时编译副本中，对获批 B0007 精确片段插入 115 个可逆的 `\allowbreak{}`；工作稿、原 patch、科学结果均未修改。保留原构建器原路径与原字节，没有破坏前三份构建回执的工具绑定，也保留了 P32 失败回执和两份原日志。

| Paper | 当前 notes-side PDF | 实际页数 | 构建状态 |
| --- | --- | ---: | --- |
| P29 | [Round4 预览](papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round4.pdf) | 16 | PASS_CLEAN；本次未重建 |
| P30 | [Round4 预览](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round4.pdf) | 18 | PASS_CLEAN；本次未重建 |
| P31 | [Round4 预览](papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round4.pdf) | 16 | PASS_CLEAN；本次未重建 |
| P32 | [Round4 attempt2 预览](papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round4_preview_attempt2.pdf) | 19 | PASS_CLEAN；本次恢复成功 |
| P33 | [Round3 预览](papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round3.pdf) | 18 | PASS_CLEAN；本次首次构建 |

合计 **87 页**。聊天中曾把 P33 页数误述为 22，已随后明确更正；此表与构建回执的实际 18 页一致。五项阻断诊断（overfull hbox、undefined citation、undefined reference、missing glyph、fatal error）五篇均为零。不是所有 TeX 提示均不存在，也不是全文科学结论已通过。

主线程已运行 [预览完成检查器](tools/finalize_round10_exact_patch_preview_completion.py)，重新核对五份 draft/patch/apply report/bundle/manifest/Bib、六项构建命令退出状态、实际 PDF/log/transcript 和临时编译副本的精确变换。实际完成回执见 [EXACT_PATCH_PREVIEW_COMPLETION_RECEIPT.json](BATCH_ROUND10_STAGE4_5_ROUND2_EXACT_PATCH_PREVIEW_COMPLETION_RECEIPT.json)。119 个锁定绑定、15 个 canonical 文件、15 棵 science tree 与 16 个 README/status 文件的受保护边界未变。

## 材料交叉阅读

主线程以实际文件描述符复核当前产物。三位同模型家族代理分别执行了以下只读交叉阅读；这不是跨模型验证，也不证明错误过程独立。

- P30 matrix round3：18 个继承段落定位、8 个 unavailable、2 个 metadata-only。保留 C01→S01、S02 `10.1063/1.457672`、C02→S03 的分离关系。未把元数据充作正文支持。
- P31 matrix round3：7 个继承段落定位、15 个 unavailable、2 个 metadata-only。Reader round3 的 11 个当前描述符匹配；旧 TSV 不是新 JSON 的当前投影。旧 reader 的历史 12020-byte 声明失配仍明确披露，未冒充当前有效绑定。
- P32 matrix round4：30 行为 18+8+4，四个 closest-work 当前无绑定摘录；26 条继承定位/摘录字段保留。B0018 的限定必须与后续 B0132 表格及结论联读。
- P33 matrix round3：48 个引用使用、14 个带引用 context，全部 `INCONCLUSIVE`、零新增原文支持。无独立 citation 的 B0127 仍须与 B0037 联读；14 个 context 不是全文 claim registry。B0062/B0128 的同链诊断不证明契约正确。

这些结论只涵盖实际所读的材料绑定、局部文本和证据分区，没有代替完整 A–E 审计或官方 coverage/EVR/E6 执行。

## 当前需要新增授权的具体问题

定位：[P29 当前稿 B0006](papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round4.tex:44)。完整稿 SHA-256 `8d6294051fe03de2c433e5d7115bcc0b73e8ac66504b17542a3700ef1762be10`，63629 bytes；当前 block manifest 的 B0006 `old_hash=a6eadf4da416`。

英文 B0004 已明确将本计划未完成的所有者法则与完整商集义务，同来源中不存在相关成果的判断分开。繁中 B0006 仍保留以下句子：

> 文獻足以界定 Picard／Bianchi 幾何對象、原始與反向辨識語彙、相鄰算術群演算法及理想算術工具，卻未提供本計畫專屬的所有者法則，也未完成最大根、共軛、取逆及無向正規化所需的完整商集。

主线程与角色分离的只读审阅均判定：此句以“文献”为主语，同时作出正面充分性与负面内容判断。英文摘要与 B0014 的一般边界不能可靠消除中文摘要独立阅读时的较强含义。13 个逐列受限短摘录与 9 个 metadata-only 记录不足以支持这种对文献内容的整体否定。

该风险早已如实留在 [提交前阅读注意](BATCH_ROUND10_STAGE4_5_ROUND2_PATCH_PREAPPLICATION_READING_NOTES.md)，此前未宣称解决。原批准的 B0006 操作仅允许定位状态子串替换，写作日志也明确 `No other text in this block changes`。不能借本次排版恢复或原 exact patch 授权扩大到这个句子。

建议的新范围仅为 B0006 中上述一句，改成：

> 現有來源記錄僅支持逐列限定的脈絡用途，並非對整個文獻集合所能證明內容的完整段落層級評估。本計畫專屬的所有者法則，以及最大根、共軛、取逆及無向正規化所需的完整商集，仍是本計畫未完成的義務；這不是關於文獻中不存在相關結果的判斷。

保留该块其余文字、13+9 分区、所有数学对象、Gate M/Q、时钟、owner、值域与 Route 边界。此处只呈现修订范围及拟文，**尚无新的 patch、author input、authorization sidecar 或 successor draft**。下一次简短“确认”可批准准备这一限定修订；正式应用仍须遵守 ARS 对具体补丁字节的显式确认与官方授权回放要求。不会把当前确认回溯为尚不存在的 patch SHA 的批准。

## 真正的阶段与接续

当前仍是 **Round 10 / P29–P33 五篇**。P32 恢复已完成，五份预览齐备；现停在新稿材料/双语范围预检。正式 Stage 4.5 Round 3 输入锁、完整 A–E/coverage/EVR/E6/compliance 包尚未生成或执行，不能宣称完成第三轮审计或计入第三次完整 FAIL。最近完成的完整性审计仍是 Round2 五篇 FAIL。

已通知全部代理停止后续启动。取得新的范围/精确补丁授权后，仅修正 P29 所列句子、输出新的 versioned draft 与连续 revision bundle，按约定复验其预览，再对五篇实际当前稿执行 fresh Stage 4.5 Round3。P30–P33 不重写、不重做已成功应用或构建。

本次没有进行新科学执行、Route 晋级、canonical/投稿晋升、README/status 更新、Git commit/push 或 Stage5/6。本批 formal Route-A tuple、正向算术 A2、A3、A4、Route-B invocations 仍各为 0/5；路线图 A 与初始系统保持原限定。这些是本批状态，不是整个项目历史的科学样本总数。

### 已完成的只读审计准备提示

旧 Round2 builder、root validator 和 finalizer 均绑定旧输入，不能仅改轮次名或 SHA 后作为 fresh 结论。不可复用的捷径包括：把本稿/矩阵拼成 LocalArtifactChain 自动 VERIFIED；用是否有 citation 自动决定 claim verdict；用 IDs 存在和空 strength 数组替代 E6 语义比较；官方 EVR build 后手工修改时间/摘要；重置 passport 而丢失历史。新轮须重建实际 claims 与 UTF-8 spans、官方 coverage/EVR 并逐项语义判定，旧分母不是新分母。

E6 必须保留完整协议链：P30 四轮 80 ops（21+14+34+11），P31 四轮 52 ops（11+20+13+8），P33 三轮 70 ops（13+37+20）。最后一轮是 `integrity_correction` 分支。P33 旧文件名 round6 只是准备迭代名，实际协议轮是 1→2→3。P29 如新增修订则连续接在实际 round4 后，不可重新开始链或用当前 FAIL 替代原始 PASS 起点。
