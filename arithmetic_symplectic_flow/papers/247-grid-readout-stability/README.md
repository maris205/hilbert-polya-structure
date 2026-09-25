# 247 — 固定非自治路径的网格读出稳定性

**Scope ID:** `ASFS-DISCOVERY-20260919-DS04`。  
**Status:** `GRID TEST COMPLETE; FIT GRID-SENSITIVE; STABILITY PROMOTION STOP`。  
**Decision:** `stop` 当前拟合的网格稳健性晋级；三次前向完成。  
**Formal coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

复用 N=250 原基线，已新增 N=260、280、300 各一次；动态起点、
完整300步路径、hbar、箱长及原读出规则不变，不重新调参。
各 N 分别记录算子、谱与首点尺度。增加 N 同时细化空间网格和扩大
动量截止，不能称为同一有限矩阵只提高精度或无限谱收敛认证。

| N | 百点 MAPE | 首间隙 | 首点尺度 |
| --- | ---: | ---: | ---: |
| 250，旧基线 | 2.29046% | 0.06662192 | 212.16289 |
| 260 | 54.96826% | 0.20020593 | 70.60081 |
| 280 | 40.82490% | 0.27464768 | 51.46484 |
| 300 | 68.95543% | 0.62910952 | 22.46779 |

三次均正常退出，未调参、重试或重跑 N250。原 2.29% 表现没有在
所测离散族中保持。纯期望诊断也有同类恶化，不能只归咎于整数
取整。保留 N250 的有限复现，不推出所有更高 N 或所有模型失败。

- [完整结果、方法与限制](paper.md)
- [当前卡](candidate-card.md) · [执行前授权卡](candidate-card-authorized-v1.md)
- [声明账本](claim-ledger.md)
- [命令、输入锁与实际运行](evidence/README.md)
- [机器可读汇总](evidence/run-1/comparison.json)
- [四网格逐点比较](evidence/run-1/prediction-comparison.csv)

当前授权范围已完成，后续改动应先明确有限 N 的模型身份或一致
极限定义，再另冻控制；不自动追加优化或网格点。
