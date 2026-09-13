# P29：Stage 4.5 Round 4 最终审查发现

本轮完整性结论：**FAIL**。这是同一次审查的 Recovery2 汇总，不是新审查轮次，不授予全篇通过、科学有效性、作者身份或 Stage 5 权限。

| 检查 | 本轮结果 | 证据边界 |
|---|---|---|
| A 作品身份 | 22/22 | 作品存在不等于每个书目字段均已从一手来源确认；字段缺口见下表 |
| B 引用语境 | 22/22 | 只判定当前限定语境忠实性，不自动建立项目定理适用性 |
| E 注册主张 | 372/375 VERIFIED | 不意味着语义提取完整或全部主张正确 |
| 官方证据行 | 375 行完整保留 | 行数不是不同主张数；已进行整份报告的来源重放 |
| 机械覆盖候选 | 0 个非 clean 候选 | 原始计数保留，语义提取覆盖始终为 not_machine_detectable |
| 普通问题 | 3 SERIOUS / 1 MEDIUM / 0 MINOR | 去重问题，不含 E6 或信息性文风观察 |

完整 [Schema5 报告](stage4_5_round4_recovery2_integrity_report_root.json) 包含 A–E、全部证据行、E6 指针及审查边界。[合规报告](stage4_5_round4_recovery1_compliance_report.json) 使用 non-SR / principles_only；RAISE 贡献封顶 WARN，独立完整性／失败模式使总体仍为 BLOCK。它不是官方 RAISE 证据综合认证。

## 当前修订路由清单

下列编号只属于本报告；原观察和旧作者待确认编号另存映射。列出建议不等于作者已经授权修改。SERIOUS 作者事项表示证据不足，不是造假或身份虚假判定。

| 本轮编号 | 程度 | 定位 | 发现 |
|---|---|---|---|
| IL-SERIOUS-1 | SERIOUS | B0002 | Compound author, affiliation, address and email metadata have no current original-author attestation. Same-name/same-email public candidates and configuration records do not confirm the current institutional claim. |
| IL-SERIOUS-2 | SERIOUS | B0104 | Funding or competing-interest declaration requires the author's factual confirmation; neither generated prose nor other public papers supply this attestation. |
| IL-SERIOUS-3 | SERIOUS | B0105 | Funding or competing-interest declaration requires the author's factual confirmation; neither generated prose nor other public papers supply this attestation. |
| IL-MEDIUM-1 | MEDIUM | B0023, B0038 | Two cited, short technical result sentences remain closely worded to their retained source fragments. Rephrase the explanatory framing more distinctly or delimit a short quotation while keeping attribution; this is a wording-level flag, not a plagiarism verdict. |

## E6 与执行边界

完整修订链已按当时实际授权审查。历史强度漂移若已在当前稿恢复，仍保留在 [本轮 E6 发现集](stage4_5_round4_claim_strength_drift_findings.json)；文字恢复不能自动替代新发现集的作者处置。空发现集只表示本次语义审查未检出，不是机器证明不存在漂移。

本报告不修改稿件、书目、来源矩阵、科学文件或历史收据，不新跑实验，不重评或提升 Route，不发布、不进入 Stage 5/6。所有最终结构／绑定检查结果统一见根目录 BATCH_ROUND10_STAGE4_5_ROUND4_RECOVERY2_FINAL_VALIDATION.json；不能用检查通过替代本页 FAIL。

P31 的28行来源定位对应问题另有暂停记录，不影响本篇已完成检查，但五篇整批尚未完成交接。

