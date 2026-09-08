# C419–C423 第五轮研究检查点

日期：2026-09-08。用户在第四轮检查点后明确“继续”，本轮续接同批，
没有开始新批次。当前 **M1／AS2／IR1 共 3/5 项完整合同准入，仍缺
2 项；0 新稿、0 PDF、0 正式评价**。七个筛选条目、五个深入尝试
均未增加准入；LY4 是旧问题续接，CF2／AF5-D 仅浅筛，不称七个
新独立问题。原三项已通过的证明与认证没有重跑。

[协调者完整裁决](COORDINATOR_REVIEW.md)保留原合同及每项的证明／
来源边界；[冻结计划](SCOUT_PLAN.md)没有在结果出现后缩小目标。

## 本轮实质进展

| 方向 | 已完成的结果 | 仍不准入的原因 |
| --- | --- | --- |
| LY4，三阶 Lyness 全整数周期 | 完整六周期分支、唯一五周期、整个 $a=1$ 整数图谱及 $a\ne1$ 真八周期排除；另证避开 $0,-1$ 的有理普通周期 $N\le48$，覆盖全部不变量纤维 | 全整数周期穷尽 E 仍未证明；有限周期长度不等于有限参数／高度 |
| AF5-G，可逆 Hénon 全周期 Galois 群 | 四周期实际群 8 阶、中心化子 16 阶；公共二次子域精确推翻最大性猜想 | 所有周期的替代群与块间域关系未分类 |
| AF5-C，全分圆域有效周期图谱 | 整性、有界 house、无周期曲线及依赖文献定理的逐参数有限性 | 缺保证终止的 conductor／period 穷尽算法 |
| AF5-D，有效轨道–曲线交集 | 经典定性 DML 适用性 | 无有效最后命中界，仅浅筛 |
| CF1，Kummer 半线性 skew | 全素数／全多项式／全时间普通计数与 zeta 有理性–自然边界二分全部证明 | Kummer 平凡化、经典 Weil 误差与既有 C404 论证的短重构，非独立实质合同 |
| CF2，Laurent 级数 Hénon horseshoe | 冻结参数区内所有普通周期计数 | 已有定理直接覆盖，仅浅筛 |
| CF3，紧 Wehler 普通周期 zeta | 所有点均有非约化返回；无穷多个时间的普通计数严格小于方案长度 | 全轨道／全特征幂局部重数修正及 zeta 分类未闭合 |

Lyness 的完整六周期通道为
$$W(r,s)=(r,-r-1,r,s,-s-1,s),\qquad a=rs+1,$$
$r,s\in\mathbb Z\setminus\{0,-1\}$；最小周期的 $2/3/6$ 退化条件
在证明中明确。唯一真五周期为 $a=13$ 的 $(-2,-2,-3,-4,-3)$。
有理上界的独立定理域是所有不经过 $0$ 或 $-1$ 的普通有理轨道，
不是将这些特殊层从完整整数合同删除；特殊层由各自的证明覆盖。

## 证明、来源与审查入口

- Lyness：[完整分支证明](lyness_closure/PROOF_PACKAGE.md)、
  [原问题与精确缺口](lyness_closure/SCOUT_REPORT.md)、
  [非作者分支复核](lyness_closure/INDEPENDENT_STRATA_REVIEW.md)。
- 有理周期界：[全纤维证明](lyness_sources/PROOF_PACKAGE.md)、
  [独立内部审查](lyness_sources/INDEPENDENT_PERIOD_BOUND_REVIEW.md)、
  [实际来源与经典归属](lyness_sources/SOURCE_AUDIT.md)。该审查无范围内
  必改数学问题；Mazur 原始长证明没有声称读完。
- 算术：[证明包](arithmetic_frontier/PROOF_PACKAGE.md)、
  [来源账本](arithmetic_frontier/SOURCE_AUDIT.md)、
  [支线交接](arithmetic_frontier/SCOUT_REPORT.md)、
  [非作者辅助证明审查](arithmetic_frontier/INDEPENDENT_HELPER_REVIEW.md)。
  来源链接的一处 fragment 删除已经定向复核并记录新哈希，数学不变。
- 正特征：[完整证明与未闭合边界](charp_frontier/PROOF_PACKAGE.md)、
  [来源账本](charp_frontier/SOURCE_AUDIT.md)、
  [支线交接](charp_frontier/SCOUT_REPORT.md)、
  [非作者完整 CF1／辅助 CF3 复核](charp_frontier/INDEPENDENT_HELPER_REVIEW.md)。
  两个审查范围均无必改数学问题；CF3 全问题不因此通过，CF2 由
  协调者实际核对原定理后作来源覆盖裁决。

这些是 AI 辅助内部审查，不是人类同行评审、全球优先权证明或
正式 Route-A 评价。完整短重构即使数学通过，也不自动占论文名额。

[最终文档／静态审查](CHECKPOINT_DOCUMENTATION_REVIEW.md)已完成：
24 个输入范围的 145 处真实本地链接均存在，七份受审输入哈希
与适用收据一致。上界摘要的适用域遗漏已在三处修正并定向闭环；
无剩余必改文档问题。该收据不冒算审查报告自身及随后新增的入口
链接，也不是数学复算或封存证明。

## 实际执行与工作树

三份来源账本记录 **79 条检索式**：协调者 15、算术 33、正特征 31。
其中包括依赖查找与选题前线索；不是 79 项独立发现，也不表示
全球查新通过。直接打开／查找来源不重复计作检索式。

本轮 **数学程序执行 0 次**。没有扩大上一轮高度八字母表，没有
旧反例、旧证明、IR1、有限域／因式分解程序或 PDF 构建的重跑。
本轮低周期恒等式与小除数表均为完整手推；文档、链接、哈希与
Git 的静态检查不冒充数学认证。没有 GPU、付费 API 或稿件上传。

HEAD 与本地记录的 origin/main 都是
`2974f8ea5f9e7cb0f8146cae017add38a6939da0`；本轮没有 fetch，
不据此宣称远端服务器此刻无新增提交。新研究材料与总状态仍在
工作树，未暂存、提交或推送；旧封存树及八个继承未跟踪目录不动。

按照批次技能的完整合同门槛，停在真实研究检查点。下一步须闭合
已明确的全族缺口，或找到不同且实质完整的机制；不能把上界、
单周期分支或经典推论拆成第四、第五篇。没有 A2 晋升，没有目标
Euler 因子／根数／零点对应或 Hilbert–Pólya 实现，授权止于 C423。
