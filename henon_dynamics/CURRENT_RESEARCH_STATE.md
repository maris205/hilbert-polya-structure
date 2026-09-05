# 当前研究状态与恢复入口

核对日期：2026-09-05。适用主线：`henon_dynamics` 五篇一轮。
本文件用于模型切换、压缩和中断恢复；完成声明以实际发布清单与批次审查为准，
不覆盖其他研究主线。

## 先读这一段

- 最新授权是 **C389–C393**。用户在 C384–C388 交付后回复“确认，下一轮”。
  **本批五篇完整发布包均已完成**：238个payload加五份manifest，
  最终PDF合计22页；完整write/nonwrite、双fresh编译、逐页视觉检查、
  独立内部交叉审和两路文件/哈希总审均通过。
  五篇后确认节点已到达；等待用户确认，不得自行开启 C394–C398。
  上批 C384–C388 已完成并推送：237个payload加五份manifest，最终PDF合计24页。
- 正确仓库：`/root/autodl-tmp/hilbert-polya-structure`，分支 `main`。
  环境的 `/root/autodl-tmp/henon_zeta` 不是本轮研究目录。
- 本批冻结证据基线：`0c877206d202f732e21ea0b194f9c7fdf30467ee`
  （已交付并推送 C384–C388）。新授权时实际 HEAD 与此一致。
  本轮 fetch 发现三个符号主线提交，467路径仅属 docs/papers/符号状态；
  核实无本轮目录或 evaluator 重叠后安全快进至
  `908069ac646c281941788b49e09c0671bf8be0b8`，证据基线不变。
- C384–C388 及 C379–C383 都是已完成批次，不要重构冒充本轮工作。
  旧 C99–C103 摘要更早，相关未跟踪材料须保留，不能据此倒退编号。
- 本批实际分工：C382 代理负责 C389，C379 代理负责 C390，
  C383 代理负责 C391及独立工程审；root 负责 C392/C393及总封包。
  C379另做五包静态总审，C382修复C393一处跨包说明并完成重封。
  这不代表恢复时仍有活动进程。代理名不是论文编号，不复用失效进程号。

## 用户长期原则

1. 优先 skills 路线图 A 路线，尤其 A1、A2 的实质进展。
2. 每轮五篇、每篇一个完整独立问题；不能把一篇文章拆成五个小步骤充数。
3. 允许大胆假设、扩大步幅，闭合不了可以换动力学子类型。
   假设、证明、引用定理、数值观察和文献新颖性必须区分。
4. 每篇输出 PDF，保留完整证明、独立复算与明确进展。经典结果须归属原作者。
5. 已授权批次内部持续执行，五篇完成后中文汇报并等待确认。
   额度重置的表述不构成无限新开批次的授权。
6. 文件、篇数、页数和测试数量不等于目标 A1/A2 已突破。

## 当前批次 C389–C393

入口：[冻结计划](BATCH_PLAN_C389_C393.md)、[选题排重](IDEA_REPORT_C389_C393.md)、
[最终批次审查与哈希](BATCH_REVIEW_C389_C393.md)。
障碍 HEN-O373–HEN-O377，epoch 1788566400。

| 编号 | 完整源系统进展 | 当前阶段 |
|---|---|---|
| C389 | Carlitz 全环作用扭点、所有素多项式幂 Galois 塔、全导子无交及分歧过滤/different | 完成：4页，52+1文件，完整发布复验通过 |
| C390 | Lyness 全正实椭圆轨道、实素数周期与正有理扭点障碍、环带Koopman谱 | 完成：5页，48+1文件，精确/数值计数分离后发布通过 |
| C391 | 超临界逆平方势全自伴边界、双向负谱、连续散射与尺度极限环 | 完成：5页，44+1文件，实际Stone跳跃/归一化检查及发布通过 |
| C392 | Lüroth 无限 Hardy 谱、全平面亚纯族与行列式不可见幂零留数 | 完成：4页，47+1文件，双fresh和完整发布复验通过 |
| C393 | 二次泛型全逆像树、全循环指标/亏格、模素数周期点比例趋零 | 完成：4页，47+1文件，文档跨包残留修复后重封/复验通过 |

这些是源系统结论。经典所有权、显式外部定理和严格 A1/A2 边界均须保留。
无限量词由完整证明承担，有限数据仅回归验证。五包完成结论以实际
release write/nonwrite、最终清单、独立审及root复核共同支撑，
不只是代理 PASS 消息。每包三轮是同一篇论文的实质修订。
提交由 Git 历史中的 `Add Route-A papers C389-C393` 标识；
精确提交及远端核对在用户交付信息中报告，避免文件自引用所在提交。

## 上批 C384–C388：已交付快照

入口：[批次计划](BATCH_PLAN_C384_C388.md)、
[选题记录](IDEA_REPORT_C384_C388.md)。
日期 2026-09-05；构建 epoch `1788566400`；
障碍编号 `HEN-O368`–`HEN-O372`。

| 编号 | 单篇完整增量 | 当前落盘状态 |
|---|---|---|
| C384 | 野分歧加性映射：全周期/全扩张域计数、局部重数、几何 zeta 自然边界 | 完成：五页终稿；类型漏洞修复后58项攻击与最终write/nonwrite通过 |
| C385 | Lozi：全有界轨道重建、变矩阵双曲性、全周期稳定性和二次单位时钟排除 | 四页终稿；最终 write/nonwrite 均通过，全页视觉检查闭合 |
| C386 | alpha-Szego：精确阈值、双向 sech² 级联、转折点与行列式盲区 | 完成：五页终稿；完整write/nonwrite与独立总审通过 |
| C387 | 紧 Heisenberg nilflow：全返回族、全谱、定义域、反演与行列式障碍 | 完成：五页终稿；完整write/nonwrite与独立总审通过 |
| C388 | 连通代数 Z² 作用：全格固定群、整数核体积修正、方向时钟障碍 | 完成：五页终稿；精度元数据修正后完整write/nonwrite及总审通过 |

每包三轮稿件是同一论文的实质修订，不是三篇论文。
最终哈希和实际验收凭据见 [C384–C388批次审查](BATCH_REVIEW_C384_C388.md)。
提交由 Git 历史中的 `Add Route-A papers C384-C388` 标识；精确提交哈希
及实际远端核对结果在用户交付信息中记录，不在本文件自引用其所在提交。
C388 的最小三维反例针对实际核对的 arXiv:0912.5169v1 Lemma 2.1
中有限格分支计数公式；不声称最终出版版本从未修正，也不据此推翻熵增长主定理。

## 路线图与最终评估边界

权威入口：[Route-A evaluator](../flow_systems/skills/route-a-evaluator.md)，
版本 `0.2.0`，SHA-256：
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`。

- A0：内生算术来源，不能事后给素数、权重或时钟贴标签。
- A1：本原轨道、重复、方向、相位、重数、稳定性与完整性；
  严格目标评估还要求算术信息与规定对照。
- A2：明确动力学 zeta/Fredholm 对象、验证域、时钟/归一化，
  以及与目标零点或除子的关系。
- A3：全局解析结构与算术算子关联。
- A4：自然量子化、幺正或散射结构；候选局部结构不自动授权 Route B。

| 候选 | A0 | A1 | A2 | A3 | A4 | 总判定 |
|---|---|---|---|---|---|---|
| C389 | STRUCTURAL_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FAIL | EXPLORATORY |
| C390 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C391 | FAIL | FAIL | FAIL | FAIL | NATURAL_QUANTIZATION | REJECTED |
| C392 | FAIL | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C393 | STRUCTURAL_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | EXPLORATORY |

精确 tuple 以各包冻结 YAML 为准。原系统完整定理与目标桥梁是不同结论。
公共边界 `NO_BAD_EULER_OR_ROOT_NUMBER`；九项目标/Route-B flags 全 false。
不声称目标局部算术、Euler 因子、根数、自守性、目标函数方程/零点/除子、
Hilbert–Pólya 算子，也不把新变量、重整化或改时钟默认为原对象的修复。

本轮实际使用 ARS 0.1.28、idea-creator、proof-writer、paper-write 和 paper-compile 的
适用流程；以用户“五篇完成后确认”替代批内反复许可停顿。
内部交叉审使用当前模型团队，不称外部、跨模型或人类同行评审；
没有外传稿件给外部模型、GPU训练、投稿或发表新颖性认证。

## 上一批 C379–C383：历史状态

该批已提交 `3e692da6…`，共234个payload加五份manifest，
五篇最终PDF合计24页；当时完成完整write/nonwrite与独立静态总审。
见 [C379–C383批次审查](BATCH_REVIEW_C379_C383.md)。
C379/C380 为 A1_WEAK，C381 为 A1_WEAK，C382为结构A0加弱A1，
C383为A4幺正/散射候选；五篇目标A2/A3均未通过。
这不是本轮成果，也不是全仓库总体评级。

## 遗留未跟踪材料

以下均在本轮前存在，保留、排除在本轮暂存范围外：

- 本目录下五个 `henon_mu3_yukawa_mark_*` 的 C99–C103 遗留包：
  generating_polynomial、minmax_aggregation、triple_coupling、
  triple_orbit_quotient、pair_dependence_geometry。
- 仓库根的 `henon_ermakov_pinney_isotonic_action_route_a/`。
- 仓库根的 `henon_flat_magnetic_torus_landau_route_a/`。
- 仓库根的 `henon_hysteretic_relay_oscillator_route_a/`。

三个根目录共有12个遗留文件，未发现本批新根目录残留。
不可宽泛清理，亦不可把根目录副本与本目录已提交论文混为一谈。
最终可以报告本批跟踪文件无遗漏，但不能因此称整个worktree全空。

## 恢复与发布最短流程

1. 核对仓库、分支、Git状态、实际代理和当前五包；本文件是快照，不是实时状态。
2. 读适用 skills 与当前计划，按单篇边界恢复，不重做已完成旧批。
3. 先证明、再独立实现与复核；无限量词不从有限样本推出。
4. 完成每包write及完整nonwrite、实际PDF视觉检查、哈希/物理成员总审；
   更新 [候选表](docs/candidate_registry.md) 和 [障碍表](docs/obstruction_registry.md)。
5. 只暂存五个本轮包及八个相关全局文件。fetch并检查远端路径；
   若只是不重叠主线推进可安全快进，否则不强推或覆盖。
6. 提交、推送并核实远端实际HEAD；中文报告五篇进展及严格路线位置，
   然后等待用户确认。不要从恢复文件自行开启下一批。

模型更换不被视作历史全文无损继承的证据。本文件通过随工作更新与仓库复核
维持可靠性；本轮没有修改应用记忆设置、删除会话或手动触发压缩。
