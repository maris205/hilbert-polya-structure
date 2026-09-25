# 244 — A−1 动态起点：更新同步与首个基线复现

**Scope ID:** `ASFS-DISCOVERY-20260918-DS01`  
**Status:** `SOURCE SYNC COMPLETE; H1 BASELINE REPRODUCED`。  
**Decision:** `advance` 基线层；一次 H1 已完成，不推进原 241/242。  
**Formal Route coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

两个上游更新已另存版本锁定代码快照，原归档不变。已核对非自治起点、
有限终点补偿、谱读出和计算预算：Hénon 的 `a_start` 必须进入整段演化；
Logistic 的不同历史冷却律不能混作一个对象。新版 Logistic 的一项
“样本外”实现重新使用测试标签定标，须另做固定尺度与正确编号的检验。
以上是源码审计结果；其后经用户确认，已执行一次原参数 Hénon H1：
MSE **12.228914226096645** 与历史完整日志一致，前 100 点 MAPE
**2.29045795741477%**。保留动态起点与原有读出，没有重新调参。
这仍是历史训练基线，不是完美拟合、样本外预测或动态起点因果消融。

- [完整记录](paper.md)
- [范围冻结卡](candidate-card.md)
- [声明账本](claim-ledger.md)
- [首轮试验方案及执行确认边界](experiment-plan.md)
- [H1 执行前冻结卡](evidence/h1-card.md)
- [H1 运行结果与限制](evidence/h1-result.md) · [原样 stdout](evidence/h1-stdout.json)
- [来源、命令与校验](evidence/README.md)
- [已同步的版本快照](../../docs/upstream_snapshots/20260918/README.md)

ARS experiment-agent 的确认门已由用户对 H1 的“可以，继续”满足；
只运行确认的现成命令，没有自动扩为其他试验。默认 Python 缺少
`numba` 不影响该 Hénon 前向；未安装依赖、未修改源代码、未启动 GPU。
下一步可另定逐点输出与静态对照；本次授权的单次运行已结束。
