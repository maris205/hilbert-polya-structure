# zeta_mvp0：原生 programme

[返回方向索引](index.md) · [结论与边界](conclusions.md) · [条件路线图](roadmap.md) · [来源目录](sources.md)

## 身份与组织规则

原生 `zeta_mvp0` programme 是“大胆生成候选、设置显式结构门槛、独立核验、谨慎限定结论”的研究线。它的原生 paper package 是直接位于 `zeta_mvp0/` 下的 `paper_01_*` 与 `paper_02_*`；外部 RH 导入所使用的 `papers/` 命名空间不构成一个新的原生 paper。

| 原生包 | 上游定位 | 当前使用方式 |
|---|---|---|
| Paper 01 | clock-preserving Hénon operator 线 | Q/W 与 \(S_{\rm op}\) 的已许可依据之一。 |
| Paper 02 | certified local relative wave trace 线 | 局部 \(P^*_{\rm loc}\) 证据与后续局部 theorem engineering；不能跳过全局与算术门槛。 |

包入口可见于上游[programme README](../../../zeta_mvp0/README.md)：[Paper 01](../../../zeta_mvp0/paper_01_clock_preserving_henon/README.md) 与 [Paper 02](../../../zeta_mvp0/paper_02_certified_local_wave_trace/README.md)。本 wiki 的状态判断仍以 programme README、路线图和台账为准。

## 状态读取顺序

1. 读[结论与边界](conclusions.md)，先确定当前可声称与不可声称的范围。
2. 读[条件路线图](roadmap.md)，确定某个新问题属于哪一个尚未通过的门槛。
3. 查[全局 claim ledger](../../../zeta_mvp0/docs/GLOBAL_CLAIM_LEDGER.md)区分数学状态和仓库可用性。
4. 查[证据政策](../../../zeta_mvp0/docs/EVIDENCE_POLICY.md)判断 theorem、computer-assisted theorem、普通数值证据与 heuristic 的差异。
5. 需要历史组织背景时，查[决策日志](../../../zeta_mvp0/docs/DECISION_LOG.md)，但不将历史路径或 superseded 记录重解释为当下授权。

## 原生 programme 的关键防火墙

- 任何 prime table 或 zeta-zero array 都不能成为宣称内生 prime carrier 的隐藏选择输入。
- 数学证据等级与仓库可复现性分离；`mirrored`、`placeholder / transfer pending`、`roadmap only` 不可互相替代。
- 失败、停止、无效或 superseded 记录为溯源而保留，内部的 `PASS` 字符串不自动许可当前结论。
- 局部周期轨道/trace 结果不自动导向 prime-time、zeta-zero 或 RH 结论。

这些规则的细节由上游[证据政策](../../../zeta_mvp0/docs/EVIDENCE_POLICY.md)和[programme README](../../../zeta_mvp0/README.md)给出。

## 与导入档案的接口

导入的 RH 语料可以作为来源可追溯的参考材料，但不是原生 programme 的独立验证结果。请先读[导入 RH 档案](imported-rh-corpus.md)中的 source pin、复现方式和不提升 claim 的规则，再决定是否仅作阅读/比对用途。

## 直接来源

- [programme README](../../../zeta_mvp0/README.md)
- [证据政策](../../../zeta_mvp0/docs/EVIDENCE_POLICY.md)
- [决策日志](../../../zeta_mvp0/docs/DECISION_LOG.md)
