# C419–C423 第四轮研究检查点

2026-09-08。用户明确 **“继续”** 后，本批第四轮有界研究已完成。
结果为 **零新增准入，保留 M1／AS2／IR1 三项：3/5 合同、仍缺 2 项、
0 新稿／PDF／正式评价**。尚未分配本批 C 编号，五篇目标未完成。

本轮的实质进展是两项完整短证明、两项 Lyness 全参数辅助结论及
明确的反例／适用性障碍；它们没有替代各自冻结的实质准入条件。
[协调裁决](COORDINATOR_REVIEW.md)记录逐项证据、来源扣除和剩余缺口。

| 支线 | 已得到的准确结果 | 不增加准入的原因 |
| --- | --- | --- |
| [非单位 Jacobian Hénon](dissipative_henon/SCOUT_REPORT.md) | 全整数参数、全有理周期点的必要充分分类；固定轨道的全时间 return-gcd 极限 | 两项都完整，但剩余证明只是短的经典局部／逆模应用 |
| [迹映射全有理闭合](rational_trace_closure/SCOUT_REPORT.md) | 具体反证了“在骨架上即可全程 tropical 比较”和“各素数好相位自动同步”两条桥接 | 仍缺全分母、全周期消去通道的统一分类 |
| [正特征原生返回](wild_native_returns/SCOUT_REPORT.md) | 特征三 Lattès 提升；所有 $p\geq5$ 的非动态仿射性、全有限返回广义 residue 为零及非恒定首重数族 | 仍缺全部周期的首返回分布和零 residue 野返回塔 |
| [三阶 Lyness 整数周期](third_order_lyness/SCOUT_REPORT.md) | 交替不变量整数性、$a\ne1$ 的完整 $-1$ 层、无界真六周期族 | 剩余 no-$-1$ 周期尚未穷尽；原统一高度核心已被否定 |

七个筛选条目不是七个新独立问题：W4-A 是原问题的浅层再进入检查，
W4-C 仅为旧机制的有理变体。深入筛选共五项，不按公式或辅助引理
数量增加合同。三项原准入及其已通过检查均不重跑。

## 证明与审查入口

- [Hénon 两项完整证明](dissipative_henon/COMPLETE_SHORT_PROOFS.md)
  和[非作者审查](dissipative_henon/INDEPENDENT_SHORT_PROOF_REVIEW.md)：
  全量词均闭合，无本范围必改数学问题，但不通过实质新论文门槛。
  正向 Jacobian 是 2，不是目录名暗示的实面积耗散；$d_2=1$ 也不是 Jacobian。
- [Lyness 辅助证明](third_order_lyness/PROOF_PACKAGE.md)
  和[非作者辅助／静态审查](third_order_lyness/INDEPENDENT_HELPER_REVIEW.md)：
  三项辅助结论通过内部检查；未声称完整分类或独立有限图复建。
- [有理迹证明边界](rational_trace_closure/PROOF_STATUS.md)与
  [正特征证明边界](wild_native_returns/PROOF_PACKAGE.md)：
  保留具体已证内容和精确全族缺口，不把失败桥接写成“不可能解决”。
- [最终文档／静态审查](CHECKPOINT_DOCUMENTATION_REVIEW.md)：
  单列链接、语法、字段和状态口径核对的真实范围，不作为数学复算。

各支线的 `SOURCE_AUDIT.md` 区分实际原文阅读、元数据、失败请求、
旧成果归属和版本日期。合计 63 条新检索式不构成全球查新证明。
Matsuzawa 的 2025 年无条件定理与 2026 年 Barrios 更正的边界已区分；
DH2 另有完全不依赖它们的初等证明，不再报作 Vojta 条件下的缺口。
当前团队的审查为 AI 辅助内部审查，不是人类同行评审。

## 唯一数学执行及真实停止边界

只执行了 **一个新数学程序、一次**：Lyness 在预先冻结字母表上的
[精确反例检查](third_order_lyness/SCOUT_REPORT.md)。65,536 个四态产生
20,800 条内部边和 363 个有向周期，无周期截断；这是有限字母表
结果，不是全高度或全有理分类。随后手推的
$(-M,M-1,1,-2,1,M-1)$，$a=M\geq5$，将反例提升为真正无界族。
没有扩大字母表、重跑旧数学程序、生成新稿或重建旧 PDF。

依 `henon-route-a-batch` 的实质准入门槛，本轮停在真实研究检查点：
仍需两项独立、完整且有足够剩余增量的合同。后续须闭合明确的
全族缺口或更换子类型，不把短伴随结论拆成两篇。

2026-09-08 只读 Git 核对：HEAD 与本地 `origin/main` 均为
`2974f8ea5f9e7cb0f8146cae017add38a6939da0`，无已暂存差异；本轮未 fetch，
不声称远端实时状态。研究材料及状态仍在工作树，**未暂存、提交或推送**；
旧封存树与八个继承未跟踪目录保持不动。

没有 A2 晋升或目标 Euler 因子、根数、零点对应、Hilbert–Pólya 实现。
`NO_BAD_EULER_OR_ROOT_NUMBER` 不变；不开始 C424，不进入 Route B，
不外部投稿、上传或公告。[返回本批入口](../README.md)。
