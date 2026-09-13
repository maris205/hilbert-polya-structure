---
type: p1-direction
route: henon_dynamics
session: "Session 2：Hénon Dynamics（低维 vs 高维）"
source_role: navigation-only
aliases:
  - Hénon Dynamics
  - Henon Dynamics
  - Session 2
---

# Session 2：Hénon Dynamics（低维 vs 高维）

[P1 Wiki](../../index.md) · [方向总览](../index.md) · [本页](index.md) · [结论](conclusions.md) · [路线图](roadmap.md) · [来源与阶段](sources.md)

## 这一页如何使用

这是顶层 [`henon_dynamics/`](../../../henon_dynamics/README.md) 研究流的导航层。它以“低维 vs 高维”组织 Hénon 型映射、Fricke 返回词、全仿射好模型、Vieta 递推和任意次数单因子谱的探索；这一分类是本 Session 的工作视角，不等于已经得到一条连续时间、谱论或 Hilbert–Pólya 构造。

原始论文、证明、程序、审查、构建日志、封存清单和 Git 回执仍是证据权威。本 Wiki 只提供可检索的进入路径；它没有重新证明任一结果，也不会把源端的 `EXPLORATORY` 标签升级为目标算术、RH 或 Hilbert–Pólya 结论。

## 建议阅读路径

1. 先读 [结论与边界](conclusions.md)，分清已封存的源端结果、Route-A 状态与未建立事项。
2. 再读 [路线图](roadmap.md)，了解原方案、C424–C428 的完成门和 C429–C433 的保存边界。
3. 需要核对论文、状态、封存或恢复权限时，进入 [来源与阶段](sources.md)，然后回到原始材料。

## 阶段快照

| 批次 | 可作为知识库入口的状态 | 必须保留的解释边界 |
| --- | --- | --- |
| C424–C428 | 2026-09-09 的五篇论文包已经完成最终论文、封存、独立成员核验和同步；五份最终 PDF 共 72 页。 | 这是一批 **Route-A exploratory** 的源端交付，不是 Route B、目标 Euler 因子、零点对应或 Hilbert–Pólya 的通过证明。 |
| C429–C433 | 2026-09-10 的会话检查点将该批保存为 **in-progress preservation checkpoint**：五项合同已准入，完成论文数为 0。 | 它不把仍未关闭的修订、最终复现/视觉检查或发布门认证为完成；已保存的稿审、引文审计和 Route-A 记录仍须按其原始范围读取，不能据此假定论文已经发布。 |

这两个状态不能互相覆盖。尤其是 C424–C428 的封存完成不使 C429–C433 自动完成；而 C429–C433 的起草或审查材料也不能反向修改 C424–C428 的冻结证据。

## 已封存五篇：低维与高维的对照入口

| 论文 | 研究对象 / 维度视角 | 原始入口 |
| --- | --- | --- |
| C424 | 整数值二次 Hénon 映射在有理点上的周期图谱 | [README](../../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/README.md) · [PDF](../../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/main.pdf) |
| C425 | 一般 Fricke 返回词的整数周期轨道与层结构 | [README](../../../henon_dynamics/research_c424_c428/papers/C425_fricke_return/README.md) · [PDF](../../../henon_dynamics/research_c424_c428/papers/C425_fricke_return/main.pdf) |
| C426 | 单因子 Hénon 的局部／全局二维仿射好模型 | [README](../../../henon_dynamics/research_c424_c428/papers/C426_affine_good_models/README.md) · [PDF](../../../henon_dynamics/research_c424_c428/papers/C426_affine_good_models/main.pdf) |
| C427 | 全维 Vieta 半线性周期图谱，`n >= 3` | [README](../../../henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/README.md) · [PDF](../../../henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/main.pdf) |
| C428 | 任意次数、双 Jacobian 符号的单因子 Hénon 整数周期谱 | [README](../../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/README.md) · [PDF](../../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/main.pdf) |

五篇的逐项结果、限制和评价标签见 [结论与边界](conclusions.md)；正式论文包入口是 [C424–C428 README](../../../henon_dynamics/research_c424_c428/README.md)。

## 后续五项合同：仅作保存中的工作地图

| 编号 | 冻结的问题接口 | 检查点地位 |
| --- | --- | --- |
| C429 | 有限特征中 unicritical 多项式的周期数据刚性（PC424-L） | 已准入合同；非完成论文。 |
| C430 | 小野周期的原生 Galois 域（UL4） | 已准入合同；非完成论文。 |
| C431 | 最优野周期测度的 Haar 极限（OM4） | 已准入合同；非完成论文。 |
| C432 | 处处局部可逆但无全局 reversor 的显式反例（RLG5） | 已准入合同；非完成论文。 |
| C433 | 导数为零多项式与有理权的乘法周期数据有限检测（FCP10） | 已准入合同；非完成论文。 |

这些标题和量词以 [C429–C433 大纲](../../../henon_dynamics/research_c429_c433/BATCH_PLAN.md) 为准。它们是下一阶段可读取的合同接口，不是可引用为“已经完成”的五篇论文。

## 下一位 agent 的最短入口

1. 先读取 [Hénon 当前研究状态](../../../henon_dynamics/CURRENT_RESEARCH_STATE.md)、[本流约束](../../../henon_dynamics/AGENTS.md) 和 [会话检查点](../../../henon_dynamics/research_c429_c433/SESSION_CHECKPOINT_2026-09-10.md)。
2. 若只是维护、检索或转换材料，可直接使用本 Wiki 和原始入口；不得改写封存的 C424–C428 包。
3. 若要恢复研究，先根据当时的用户授权和当前状态文件判定是否允许继续，再从 [路线图](roadmap.md) 的相应门开始；本页本身不授予研究、Route B、投稿或外部上传权限。

参见：[结论与边界](conclusions.md) · [路线图与交接](roadmap.md) · [来源与阶段](sources.md)
