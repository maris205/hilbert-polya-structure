# Claim ledger — ASFS-DISCOVERY-20260919-DS04

**Status:** `GRID TEST COMPLETE; FIT GRID-SENSITIVE; STABILITY PROMOTION STOP`。  
**Formal coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

| ID | 声明 | 当前证据 / 状态 | 限制 |
| --- | --- | --- | --- |
| DS04-P1 | 仅新增 N260/280/300 各一次，复用 N250，原非自治路径和参数固定 | Protocol + execution COMPLETE | 全路径逐元素相同；无重新调参 |
| DS04-P2 | 固定 L 时增加 N 同时细化 dq 并提高 FFT 动量截止 | Source algebra | 不是单纯浮点精度变化，也不是时间步收敛 |
| DS04-P3 | 每个 N 拥有独立 H/U、态、分支和首点尺度 | Ownership control | 不跨维度按列号或排序号作物理态配准 |
| DS04-C1 | 新 N 的 MAPE 54.96826%、40.82490%、68.95543%，原 N250 为2.29046% | Finite OBSERVED | 固定参数所测离散族的强敏感性，非所有 N 的无限结论 |
| DS04-C2 | 首间隙约为基线3.005、4.122、9.443倍，各自首点定标后仍大幅偏离 | Finite OBSERVED | 不是只沿用旧尺度造成的恶化；排序曲线不等于同态跟踪 |
| DS04-C3 | 纯期望读出同样明显恶化，取整前首间隙已改变 | Diagnostic OBSERVED | 不把根因唯一归给取整，也未定位唯一物理机制 |
| DS04-C4 | 每组完整 N 态、100点、300步保存；有限残差小，指标重算一致 | Execution + saved-array checks | 非无限收敛、高精度或近简并稳定认证 |
| DS04-N2 | 连续极限、无限谱、盲测或内生算术 | NOT ESTABLISHED | 即使有限四点接近也不能推出 |
| DS04-R1 | A0/A1/A2/T0–T3、Route B | NOT EVALUATED | 仅 A−1 发现检验协议 |

当前 `stop` 只停止将原低误差晋级为所测离散族的网格稳健谱证据。
旧 N250 基线和各组独立 owner 不变，负向结果不转化为 Route 分数。
