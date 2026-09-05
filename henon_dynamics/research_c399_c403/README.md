# C399–C403 研究续接：两个完整源系统候选，五篇批次未闭合

日期：2026-09-05。正确仓库：`hilbert-polya-structure`。
本目录保存当前授权批次的真实研究进展，不是冻结五篇计划或正式 C 编号发布。
用户要求的五篇独立、实质、完整论文仍未完成；不把技术引理或经典重述补作名额。

## 已保存的两份研究稿

| 研究稿 | 数学结果与边界 | 当前核验状态 |
|---|---|---|
| [Boole：有限实稳定性乘积、共振与临界补偿](boole/paper/main.pdf) | 全参数加权和、完整零极点消去、整个 iff 参数族、两侧局部一致极限；不是自然实域 Perron 算子的构造 | 完整证明及稿件独立内部审查；9 页；两次新目录构建字节相同；9 页均已逐页查看 |
| [有限耦合 harmonic δ 梳的两项谱渐近](delta_comb/paper/main.pdf) | 固定正有限耦合的 `2k log k + Cκ k + Oκ(log k)`、热迹／zeta／Schatten 后果、强耦合端点与极限不交换；不是目标零谱对应 | 完整证明及稿件独立内部审查；最终 14 页；两次新目录构建字节相同；14 页均已逐页查看 |

它们是包含完整论证的**未编号研究稿**，不是空架构，但尚未被计为正式批次论文。
未运行新一轮完整 Route A evaluator，未修改既有 evaluator、冻结 YAML 或历史发布。
没有新增目标 A2/A3 证据，保持 `NO_BAD_EULER_OR_ROOT_NUMBER`。

## 证明、审查和实际计算

- Boole：[完整证明](boole/PROOF_PACKAGE.md)、[来源与归属](boole/SOURCE_AUDIT.md)、
  [证明审查](reviews/BOOLE_INDEPENDENT_REVIEW.md)、
  [稿件审查及修复回执](reviews/BOOLE_MANUSCRIPT_REVIEW.md)、
  [最终研究稿构建记录](boole/BUILD_REPORT.md)。原证明、计算回执和论文计划均保留
  审查时的历史字节：其中 `REPRODUCIBILITY.md` 的 “has no PDF”／待审句子、
  `PAPER_PLAN.md` 的 remaining 列表及证明的 “review pending” 不代表当前状态；
  实际稿件、后续审查与构建状态以本页及上述最终回执为准。
- δ 梳：[完整证明](delta_comb/PROOF_PACKAGE.md)、
  [独立数学审查](boole/REVIEW_OF_DELTA_COMB.md)、
  [来源审计](delta_comb/SOURCE_AUDIT.md)、
  [更广点相互作用文献核查](reviews/DELTA_BROADER_SOURCE_CHECK.md)、
  [正文与引文审查及修订回执](reviews/DELTA_MANUSCRIPT_REVIEW.md)、
  [最终研究稿构建记录](delta_comb/BUILD_REPORT.md)、
  [数值报告](delta_comb/CHECK_REPORT.md)、[实际输出](delta_comb/SANITY_OUTPUT.json)。
  两个数值方法在九个所测条件的较细网格一致，但 `κ=2,k=40` 的粗网格给出
  311 而不是较细网格的 312；这是保留的离散化偏差，不是无限谱的认证计数。

两份最终 PDF 合计 **23 页**。δ 梳的论文计划与初编译回执保留其历史阶段用语；
13 页初版 PDF 已另存，最终正文为 14 页（最后一页续排参考文献），不混用两次
产物的页数或哈希。每份研究稿只有一次完整正文独立审查及其实际修改的定点复核，
没有虚构额外外部轮次。

经典所有权明确保留：Boole 的相图、删 prepole 域、已有编码与相应无权计数，
以及完整圈 Blaschke 谱；δ 梳的模型、离散性、强 resolvent 极限和 Dirichlet
divisor 端点。未在有界文献集合中找到完整加权合同／有限耦合两项公式，
不等于证明全球新颖性。较广 AKM 原文有一篇未取得全文，访问边界已记录。

## 为什么目前不能填满五篇

1. [全双曲普通迹材料](hyperbolic_trace/PROOF_PACKAGE.md) 的四项数学结论得到
   [独立审查](arithmetic_scout/HYPERBOLIC_TRACE_ADMISSION_REVIEW.md) 支持，
   但相对已有 P25、经典正则化行列式和有权 Hankel 工具，独立论文增量仍不足。
   保留为可复用技术结果，不占一篇。
2. [算术续筛](arithmetic_scout/CONTINUATION_CLOSEOUT.md) 的矩阵多项式动力学、
   Hessian/Lattès 入口均触及直接所有权；固定特征非线性 zeta 仍缺全周期分歧
   汇总，不能用有限局部 jet 代替全局结论。新增合同数为零。
3. [备用续筛](nonlinear_reserves/RESERVE_SCOUT.md) 的 Markoff 全素数轨道问题
   没有得到所需新证明；超奇异 isogeny 非回溯 zeta 的普通图部分已有所有权，
   half-loop 约定缺口也未闭合。新增合同数仍为零。

因此缺少的是其余三个可闭合且足够独立的研究合同，而不是编译资源或例行权限。
这里没有把一次有限筛选失败夸大为整个方向不存在新结果。
算术续筛旧快照中的“其余两篇”是当时尚在判断普通迹材料的口径；在它被判为
论文准入 HOLD 后，当前确切缺口为三个，不能继续沿用旧快照的名额计数。

## 工作流范围

使用仓库 `henon-route-a-batch` 的实质准入与原始证据边界，以及
`proof-writer`、`paper-write`、`paper-compile` 的证明、写作和构建检查。
按用户数学研究合同采用匿名数学 article，不套用 ML 会议页数、实验和固定
多轮外部评审配额。当前团队的实际独立审查是内部审查；没有旧 GPT-5.4 MCP
调用、完整 ARS runtime 通过或人类审稿的声明。来源、实验和理论证据分开记录。

所有新增材料都在本目录；八个继承的无关未跟踪目录保持不动并排除暂存。
证明、稿件及最终 PDF 的上述研究稿级检查已经结束；余下批次工作是发现并闭合
三个实质独立合同，再处理正式批次准入、评估与发布。不会因入口文档更新重跑
已通过的全部数学计算。本目录的进度说明不得替代五篇正式发布门槛。

## 研究快照的文件核验

[PAYLOAD_FILES.txt](PAYLOAD_FILES.txt) 逐项列出本目录的实际研究载荷，不包括清单
本身与哈希文件；[MANIFEST.sha256](MANIFEST.sha256) 覆盖这些载荷及该清单，
只排除自身。两者仅用于本次研究进展快照，不是正式 C 系列发布清单。
在本目录运行 `sha256sum -c MANIFEST.sha256` 可检查字节身份；还须将实际文件
集合与载荷清单加两项元数据比较，才能发现额外文件。当前材料不使用符号链接。
没有新增发布器或安全校验代码，也不把该哈希检查说成数学证明、重新计算、
篡改防御测试或正式 Route A 通过。Git 提交身份应从仓库读取，不嵌入自身载荷。
