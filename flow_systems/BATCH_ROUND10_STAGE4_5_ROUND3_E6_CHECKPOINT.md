# Round10 · Stage 4.5 Round3 — E6 保守处置与精确恢复确认点

五项 E6 的保守选择已登记；两份新恢复补丁已准备并复核，**尚未应用**。本页是新的后继记录，不改写早期“待选择”快照、历史发现或完整审查 FAIL。

## 当前状态

| 项目 | 已记录选择及当前证据 | 本次正文写入 |
|---|---|---|
| P29 / ADV-E6-1 / B0049 | restore 路线；R1 op26 → R2 op2 → R4 op5 的收窄链已记录，R6 保持该限定 | 无，不重复替换 |
| P30 / ADV-E6-1 / B0061 | restore 路线；R1 op5 → R2 op3 → R4 op4，保留 same-model-family / not independent replications | 无，不重复替换 |
| P30 / ADV-E6-2 / B0103 | restore 路线；R1 op17 → R2 op12，保留 cyclic-label symmetry / label-equivariance 而非 placement-breaking | 无，不重复替换 |
| P31 / ADV-E6-1 / B0108 | restore 路线；现行 R5 → 拟 R6 的精确补丁如下 | 未应用，待确认 |
| P32 / ADV-E6-1 / B0128 | restore 路线；现行 R5 → 拟 R6 的精确补丁如下 | 未应用，待确认 |

P29/P30 的[现有证据](papers/29-bianchi-ideal-owner-refinement/notes/stage4_5_round3_e6_existing_restoration_evidence.json)及[P30 两项证据](papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round3_e6_existing_restoration_evidence.json)确定的是措辞与版本链，不证明原独立性、shuffle 性质或完整历史程序叙述，不追认历史增强，也不删除历史发现。

## 正式处置的含义

[官方执行记录](BATCH_ROUND10_STAGE4_5_ROUND3_E6_DISPOSITION_EXECUTION.json)包含四次 build、四次 replay validate，退出码均为 0，覆盖五项 restore。四份侧车仍为 `pipeline_action=restore_required`。`disposition_status=complete` 只表示每项选择已经记录，不表示恢复完成、新 E6 PASS 或放行。

侧车仍绑定原 Round3 findings 及其当时的 draft/bundle，未把旧发现偷偷重绑到普通补丁后的现行稿。现行稿效果另行记录。P33 原来未报告 E6 finding，本次不制造空处置侧车。

[范围记录](BATCH_ROUND10_STAGE4_5_ROUND3_E6_SCOPE_RECORD.json)明确：本次只有一条复合用户确认。为每项处置分别保留的五份 run-local 原消息文本副本，是同一消息的逐项绑定，不是五条独立用户消息或身份凭证。副本和临时输入位于仓库外；UTF-8 文本末尾添加一个 LF。运行时重算字节哈希，不能认证来源、作者身份或声明事实；不保证临时文件永久保存，失去其字节后重放须失败关闭。

## 精确补丁请求

[机器可读精确请求](BATCH_ROUND10_STAGE4_5_ROUND3_E6_EXACT_RESTORATION_REQUEST.json)含完整 patch JSON、原文、替换全文、目标和全部绑定。

请求 SHA-256：`5239c9237959c9df3e442073b5157dee3c510fb9f9170b09685a3c84385cfa59`。

以下两份都是 `patch_format_version=1.1 / integrity_correction / revision_round=6`，每份仅一个 `EA-001 / replace_block`。方案选择已收到；对这些新制成的精确补丁尚未建立应用授权。

### P31 / B0108

[控制补丁](papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round3_e6_restoration_caller_bound_patch.json)（1459 bytes），SHA-256：

`fee4cd43a33e3a09246c68673b2ba935f7ad6952a894f829a8b27ee4d3517c44`

[现行 R5](papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round5.tex)，SHA-256：`1d9463eea8aebdb305842f7de6eb2ad2577b7e2ac8cc563a180a91275780d797`。

[Issue list](papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round3_e6_restoration_issue_list.json)，SHA-256：`66580fb4321181fefb4dbb843360dd058073f1f8ce51bea1ad4021278cb9839b`。Manifest-owned `old_hash=6ac2cbc87cc1`。

唯一变化：`verified every claim` → `verified any claim`。

完整替换块：

```tex
Liang Wang is the responsible human author. He approved the project
restrictions, stage gates, and the Phase-6 author-adjudicated design
choice. Those approvals must not be interpreted as a statement that he
personally read every source in full or verified any claim at the exact
source-passage level. The recorded verification was bounded mainly to
source identity, metadata, abstracts, authoritative landing pages, and
project-local claim-fitness records. Bounded source finalization yielded
7/22 locator-available rows and 15/22 explicit bounded-unavailability rows;
the located passages provide bounded context for the registered uses but do not
prove the registered roles in full, no unavailable locator was guessed, and no
project-specific theorem transfer follows. The
article does not claim complete theorem-level source verification, novelty
clearance, or a clean retraction/conflict screen.
```

### P32 / B0128

[控制补丁](papers/32-homology-cover-renormalization-uniformity/notes/stage4_5_round3_e6_restoration_patch.json)（1409 bytes），SHA-256：

`08bed5b9e63e844c419d5dc1635ff52f8d2f8a70ad389c807fb2bf3a1efd7abf`

[现行 R5](papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round5.tex)，SHA-256：`9bae93de2df2f68fdc0bdd2731a9b13a12033d88a5d40ef7873ec86a53cb1e09`。

[Issue list](papers/32-homology-cover-renormalization-uniformity/notes/stage4_5_round3_e6_restoration_issue_list.json)，SHA-256：`3f62cea4afec3a696e83434b53ab14eee1886b8c3a4e4ccc6c4626645ad50a2f`。Manifest-owned `old_hash=cdbb23c8a5e9`。

唯一变化：在 `reading` 后补回个人对任何主张进行 exact source-passage verification 的限定。B0121 不在操作范围。

完整替换块：

```tex
The project report names Liang Wang as the responsible human author and records
approvals of the project restrictions, workflow gates, and the Phase-6
falsification-first design choice. Those secondary entries are not original
attestations of the approval acts and are not evidence of personal full-text
reading or of the author's verification of any claim at the exact source-passage
level.
The bounded source work now records four retained closest-work scopes, 18 exact
locators for inherited-source contextual uses, and eight explicit metadata-only
unavailability records. Exact locators and support-excerpt digests do not establish
project-specific theorem applicability; unavailable rows authorize no passage
transfer. The article does not claim comprehensive full-text verification, novelty,
impossibility, or a clean retraction/conflict screen.
```


这些限定说的是审批或二手记录不能支持何种推论；既不认证作者确实阅读全文或核验具体主张，也不反向断言作者实际从未阅读或核验。段落中保留下来的作者身份或批准行为等陈述不因此被核证。

## 已完成的检查与仍未进行的检查

[提案复核记录](BATCH_ROUND10_STAGE4_5_ROUND3_E6_PROPOSAL_VALIDATION.json)记录实际命令及结果：

- 两份 issue list 和两份控制 patch 均通过当前 schema。
- 当前 draft、manifest、bundle 和 issue-list 绑定一致；目标 old_hash 来自各自 manifest。
- 替换全文与先前展示方案逐字一致，数值及 citation/reference token 未变。
- 只读内存拼接中，P31 的 113 块仅 B0108 改变，另 112 块不变；P32 的 139 块仅 B0128 改变，另 138 块不变，包含 B0121。
- 未发出 R6 稿、apply report、新 manifest 或新 bundle；未运行补丁应用授权构建或 apply。本次没有新的 PDF，也没有针对已应用 R6 的事后复验结果。

[P31 早发初版](papers/31-level11-conjugacy-owner-ledger/notes/stage4_5_round3_e6_restoration_patch.json)保留为非控制提案：它早于 caller 提供 issue-list 哈希而生成。主线程随后单独读取并提供精确绑定，writer 在新 `caller_bound` 路径完整重新发出。两份字节相同，故哈希相同；相同哈希不追溯改变初版的生成顺序。本次没有 apply 失败、数据哈希不一致或对初版的追溯授权。

[保护检查](BATCH_ROUND10_STAGE4_5_ROUND3_E6_PRESERVATION_CHECK.json)在其记录时点验证原输入锁 375 项、原 Round3 证据 299 项、已完成普通修正证据 74 项，合计 745 个不同路径，无新增不一致；15 个科学目录仍与锁定目录内容一致。P29/P30 新证据中的 69 个文件绑定及三个当前块也核对一致。P30 既有 reader `/entries/7` 描述符不一致保留为已知历史情况，未修复或隐去。

## 确认后允许的后继范围

确认本页两份精确补丁后，才可生成各自的 hash-bound 应用授权，校验后只写 P31/P32 的 notes-side R6；随后核对应用见证、全部变化/未变化字节、manifest、连续 revision bundle，并对变化内容做必要完整性/E6 定向复验。任何绑定不一致或官方工具失败须停止，不通过重写旧证据修复。

[16 条作者事项](BATCH_ROUND10_STAGE4_5_ROUND3_AUTHOR_PENDING.md)继续未决。身份、贡献、资金、利益、个人审读和责任承担不代为确认；未授予全篇完整性 PASS，原 FAIL 与发现仍保留。restore 路线在完成必要的新完整性/E6 检查前不能解除检查点。未授权 Stage5/6、对外发布、永久删除、canonical promotion、Route 改判或科学实验，也不重做已完成的五份普通补丁。

是否确认应用本页 P31/P32 两份精确补丁，并继续上述必要应用检查与定向复验？
