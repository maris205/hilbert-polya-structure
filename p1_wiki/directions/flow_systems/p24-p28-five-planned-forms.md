# P24–P28：五种计划中的连续时间形式

[P1 Wiki](../../README.md) · [本方向目录](index.md) · [结论边界](conclusions.md) · [路线图](roadmap.md) · [五种连续时间子型](p24-p28-five-planned-forms.md) · [来源与原件](sources.md)

## 这五个对象为什么要并列

P24–P28 是 Session 5 在自由探索后按路线图启动的一批五个连续时间子型。它们刻意改变：时间由谁拥有、闭轨和相位如何出现、空间是否紧致、解析对象在哪里、以及第一条可证伪结论是什么。故它们不是单一模型的参数变体。

共同的冻结约束是：主对象为连续时间流；不以素数/零点表定义或调参；不人工植入 `log p` 周期或 von Mangoldt 权重；大胆假设在闭合前仅为 `HEURISTIC`；Route B 不因存在量子对象而自动启动。

> “计划中的形式”保留的是启动时的研究架构。以下的“终态”只报告已落入最终论文的受限结果，不把计划、对照或交付状态提升为 Route 成果。

## 总览

| Paper | 冻结连续时间子型 | 启动时的核心问题 | 最终结果的性质 |
| --- | --- | --- | --- |
| P24 | 有限体积、带 cusp 的 Bianchi 双曲三维流 | 复长度 holonomy 与 Gaussian 算术能否给出内生 prime-ideal 因子？ | 负特异性/所有权压力测试 |
| P25 | 开放双曲三圆盘散射台球流 | 物理 roof 是否可继承 unit-roof 符号 determinant？ | 非算术负迁移校准 |
| P26 | Level-11 新形式驱动的正时间变换测地流 | 时间变换的 first variation 是否显出 Hecke/Euler 分解？ | 有限所有权 taxonomy 与非因子化障碍 |
| P27 | 同余逆极限测地层状空间 | 没有极限闭轨时，有限层数据还能否拥有极限 Zeta？ | 极限闭轨 no-go / 所有权逃逸 |
| P28 | Bolza 磁 Hamiltonian/contact 流加 tensor-power 量子族 | 最小非零 flux 是否在 source-bound trace 中给出算术特异相消？ | 正控制与半经典/固定算子分离 |

## P24：Bianchi holonomy flow

- **初始对象：** finite-volume cusped hyperbolic 3-flow；冻结 complex length、cusp/scattering 义务，以及 `Q(i)` Dedekind-zeta 的 prime-ideal ownership。
- **启动时已记录的进展：** level-`(3)` neat/torsion-free lemma 已自包含证明。
- **`HEURISTIC`：** complex-length holonomy 加 Gaussian arithmetic 可能给出内生 prime-ideal local factorization。
- **第一 kill gate：** 固定长度而打乱 holonomy angles，并与匹配的非算术 Kleinian ledger 比较；若没有 canonical orbit/prime map，即停止该解释。
- **计划的下一工件：** 带 cusp-risk 列的 exact word-cutoff complex-length/holonomy ledger。
- **最终受限结果：** principal-congruence trace identity 与 first-jet laws 在一般系数环上成立；冻结矩阵 profile 的最大 collision bucket 由 208 降到 84，但 singleton owner 为 0。因此这是量化的负 specificity，不是 orbit-owner solution。
- **Route 边界：** proxy 为 `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`；完整 flow 未赋值。

入口：[项目 README](../../../flow_systems/papers/24-bianchi-holonomy-flow/README.md) · [最终 PDF](../../../flow_systems/papers/24-bianchi-holonomy-flow/stage5_finalization/paper.pdf)

## P25：three-disk scattering flow

- **初始对象：** `d=6a` 的 no-eclipse 开放双曲三圆盘台球流；unit-roof symbolic object 被明确分开，作为非算术 calibrator。
- **启动时已记录的进展：** 冻结几何已证明 safely no-eclipse；exact multiple-scattering determinant 与 semiclassical orbit Zeta 已分离。
- **`HEURISTIC`：** instability half-density 可能因纯粹 generic 的原因呈现“算术般”外观。
- **第一 kill gate：** 比较 `d/a=5.8, 6.0, 6.2`，再加 shuffled/random/composite labels；若现象持续，结论是 `PROVES_TOO_MUCH`，而不是成功。
- **计划的下一工件：** 直到 topological length 12 的 exhaustive primitive cyclic disk-word ledger。
- **最终受限结果：** exact roof-nontransfer theorem 与 2,241 行 validation-only estimand 说明物理三圆盘流不能取得 unit-roof symbolic determinant credit。
- **Route 边界：** unit-roof calibrator 是非算术对象；物理 flow 未赋值，不能把 calibrator 的 A2 解析结果计为正向算术 A2。

入口：[项目 README](../../../flow_systems/papers/25-three-disk-scattering-flow/README.md) · [最终 PDF](../../../flow_systems/papers/25-three-disk-scattering-flow/stage5_finalization/paper.pdf)

## P26：Level-11 newform time change

- **初始对象：** 测地流的 smooth positive time change；`rho` 被固定为 time-density/slowness，速度乘子为 `1/rho`。
- **启动时已记录的进展：** positivity interval 与精确 first period variation 已证明；不再使用无支持的“standard modular symbol”标签。
- **`HEURISTIC`：** time-changed Zeta 的 first variation 可能显出 Hecke/Euler decomposition。
- **第一 kill gate：** 用 norm-matched generic bounded observable 替换 newform one-form，并置换 orbit periods；没有精确 Hecke recurrence 即停止。
- **计划的下一工件：** 包含 `length`、newform period、first-variation coefficient 与 generic-observable controls 的 primitive hyperbolic-class ledger。
- **最终受限结果：** 138-instance / 55-group owner taxonomy、配对负控及 both-controls-pass residue `0` 支持有限范围的 nonfactorization。
- **Route 边界：** 有限 multiset 没有提升为 global primitive Euler owner；A2 失败。

入口：[项目 README](../../../flow_systems/papers/26-level11-newform-time-change/README.md) · [最终 PDF](../../../flow_systems/papers/26-level11-newform-time-change/stage5_finalization/paper.pdf)

## P27：congruence inverse-limit no-go

- **初始对象：** inverse-limit geodesic lamination；同时追踪 residual inverse-limit 与同源 homology-cover 对照，不能混同。
- **启动时已记录的进展：** residual normal tower 的 total-space flow 没有 periodic point；compatible-lift、normality 与 `PSL_2` intersection 的步骤均已证明。
- **`HEURISTIC`：** 即便 inverse-limit flow 本身没有闭轨，renormalized finite-level Zeta data 也许仍有意义。
- **第一 kill gate：** 区分 finite-level projective statistic 与由 limit flow 拥有的 Zeta；任何把两者混为一谈的论证立即拒绝。
- **计划的下一工件：** finite-level reduction-order table，并明确与极限流无闭轨定理分开。
- **最终受限结果：** residual inverse-limit renormalization no-go/fixed-owner escape 及独立的 homology-cover four-quadrant calibration 均为负候选结果。
- **Route 边界：** 启动时 `PROVED_A1_OBSTRUCTION` 只是 informal mapping，不是 formal `A1_FAIL`。后续对象级记录才把 residual candidate 固定为 `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`、`ROUTE_A_REJECTED`；独立 homology calibrator 也被拒绝，且两者均无正向算术 A2 或 Route-B entry。

入口：[项目 README](../../../flow_systems/papers/27-congruence-inverse-limit-no-go/README.md) · [最终 PDF](../../../flow_systems/papers/27-congruence-inverse-limit-no-go/stage5_finalization/paper.pdf)

## P28：Bolza magnetic flow

- **初始对象：** compact magnetic Hamiltonian/contact flow 与 tensor-power quantization；使用 connection holonomy 而非不存在的 global potential。冻结的半经典族是 `H_N=Delta^{L^N}` on `L^2(Sigma_B,L^N)`，`N→infinity`；fixed `Delta^L` 是另行追踪的开放候选。
- **启动时已记录的进展：** degree/flux normalization 已证明，量子对象的所有权已被明确拆分。
- **`HEURISTIC`：** minimal nonzero flux 在 source-bound tensor-power trace regime 中可能带来算术特异的 phase cancellation。
- **第一 kill gate：** 在相同 `N`、bundle degree、energy window 和 trace regime 下比较 `b=0,+1/2,-1/2`，并使用匹配非算术 metric；若仅拓扑/flux 仍持久，则 A0 失败。
- **计划的下一工件：** 先给出 tensor-family owner lemma，再建立带 symmetry resolution 的 ledger；fixed-operator high-energy ownership 保持独立且开放。
- **最终受限结果：** exact nonarithmeticity、finite word-to-length completeness 和 exact systole chain 构成实质正控制。
- **Route 边界：** 不把该正控制转移成 magnetic/arithmetic credit；magnetic/arithmetic transfer、匹配 Bolza/control A2 比较和完整 tuple 均未声明。

入口：[项目 README](../../../flow_systems/papers/28-bolza-magnetic-flow/README.md) · [最终 PDF](../../../flow_systems/papers/28-bolza-magnetic-flow/stage5_finalization/paper.pdf)

## 从启动计划到终态：如何正确读取

启动文档中的“next artifact”和 Round 2–4 的中间结果，是该批的冻结研究合同与历史证据；它们不是对未来的自动授权。Round 9 结束后，五个项目的流程状态是：

```text
Stage 5 = completed
Stage 6 = skipped（用户明确拒绝）
pipeline global state = completed
scientific / route state = 未因流程收尾改变
```

批次层面的正向算术 A2 仍为 `0/5`，Route B 调用仍为 `0/5`。应将本页的每一条“最终结果”与 [结论边界](conclusions.md) 一起阅读，并回到 [来源与原件](sources.md) 的原始论文和收据核验。

启动时的完整表、假设与 kill gates 见 [P24–P28 批次启动记录](../../../flow_systems/BATCH_START_PAPERS_24_28.md)；最终交付状态见 [Round 9 Stage-5 报告](../../../flow_systems/BATCH_ROUND9_STAGE5_COMPLETION_REPORT.md)。
