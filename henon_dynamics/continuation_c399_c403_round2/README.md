# C399–C403 五篇研究稿：续接批次

日期：2026-09-05。五篇完整研究稿及实际 PDF 已完成，共 **59 页**。
本轮续接用户确认的未完成批次，不跳号。C399/C400 是此前已验收的两稿，
保留原字节并登记编号；本轮新写 C401–C403。没有把旧快照追认成当时
已经交付五篇，也没有把保留的初稿、拒绝候选或纠错另算论文。

## 五个独立问题与实际 PDF

| 编号 / 页数 | 实际正文 | 完整源结论及主要新增范围 | Route A 判断 |
|---|---|---|---|
| C399 / 9 | [Boole 有限实稳定性乘积](../research_c399_c403/boole/paper/main.pdf) | 全参数有限实乘积、完整共振除子、临界非亚纯 germ 与双侧补偿极限；经典相图、计数和圆周谱归原来源。 | REJECTED |
| C400 / 14 | [有限正耦合 harmonic δ-comb](../research_c399_c403/delta_comb/paper/main.pdf) | 每个有限 κ>0 的两项高能计数律及 Oκ(log k) 误差；范数预解式 Dirichlet 极限与高能极限不交换，主项系数由 2 变为端点的 1。 | REJECTED |
| C401 / 13 | [Frobenius–Hénon 双时钟交数](henon_arithmetic/paper/main.pdf) | 非共振 d^n≠q^r 时，所有系数统一的几何点数 max(d^n q^r,q^(2r))；精确边界长度、短时缺陷、阈值与两种时钟切片之别。 | 源机制 EXPLORATORY |
| C402 / 12 | [多项式坐标权重留数迹](nonlinear_return/paper/main.pdf) | 任意固定一元多项式坐标权重都由同一有限边矩阵给出所有周期 τ_n=−Tr W^n；周期无关流界、逆 determinant 与退化留数约定。 | REJECTED |
| C403 / 11 | [非乘性慢变整除 Gram 极限](spectral_regular_variation/paper/main.pdf) | 正可测慢变系数、紧区间上下界下，在且仅在 q(1−2σ)>1 的全部 S_q 中收敛至经典 LCM 核，包括 q<1；LCM 谱渐近本身不算新增。 | 源机制 EXPLORATORY |

目标 A2/A3 全部未通过，九项目标/Route-B scope flags 均为 false。
三类强制算术对照仍是 INCOMPLETE；没有目标训练、验证或 sealed-test 数据，
目标零点指标为 NOT_TESTABLE，不是零误差。完整 tuple、解析对照和未做项
见 [EVALUATION_SCOPE.md](EVALUATION_SCOPE.md) 与其中五份正式评估。
所有结论保持 `NO_BAD_EULER_OR_ROOT_NUMBER`；这五份源研究稿不是 RH 证明。

## 完整证明、所有权和审查

[冻结计划](BATCH_PLAN.md) 登记对象、参数、域、时钟、迹约定、五个独立
论文级问题及来源扣除；不以页数或文件数判断研究增量。三个新合同的
完整证明分别在 [C401 合同](henon_arithmetic/CONTRACT_SCOUT.md)、
[C402 合同](nonlinear_return/CONTRACT_SCOUT.md)、
[C403 证明](spectral_regular_variation/PROOF_PACKAGE.md)，正文也给出完整论证。
这些合同各有独立内部证明审查，随后新写的 TeX 又接受非作者全文审查。
主协调者已逐份读完三个新稿的全部数学正文、宏、书目、引用审计和初编译回执。

- C399/C400：前轮独立证明/正文/全部引用审查、真实小修和定点闭合均原样
  复用，见 [复用收据](REUSE_C399_C400.md)。没有重复执行来增加检查次数。
- C401：[完整正文审查及小修闭合](reviews/C401_MANUSCRIPT_REVIEW.md)，
  0 blocking、0 open minor；唯一 minor 是主定理一句条件澄清，协调者
  修正后非作者定点复核通过，初稿完整保存。全部 6 条书目、7 个实际引用
  语境、14 项关键主张及全部保存精确检查已核对。
- C402：[完整正文审查](reviews/C402_MANUSCRIPT_REVIEW.md)，0 blocking、
  0 actionable minor；全部 4 条书目、9 个实际引用语境、所有登记主张与
  保存精确结果，以及独立手工五状态证书均核对。
- C403：[完整正文审查](reviews/C403_MANUSCRIPT_REVIEW.md)，0 blocking、
  0 actionable minor，所有 4 条书目、11 个实际引用语境和关键主张逐项核对。

[独立评价边界一致性审计](reviews/EVALUATION_BOUNDARY_REVIEW.md) 另核对
五份 tuple、45 项 false scope flags、45 项 NOT_TESTABLE 目标指标和
INCOMPLETE controls，未发现跨产物矛盾；它不是重新执行正式评价。

数学证明、有限代码证据和哈希一致性分开使用。C401 47 个非共振检查及
共振反例、C402 留数/Groebner/短周期等已保存精确检查仅作有限支持，
不证明无限量词；C403 是解析证明，没有为配额制造实验。旧精确结果未因
TeX 编写或编号复用而重跑。非仿射正特征候选保留在
[被淘汰候选记录](nonaffine_charp/CONTRACT_SCOUT.md)，0 个计入五篇。

文献检索有界，不提供全球优先权或无人做过证明。引用审计逐项记录
真正访问的版本、定位、元数据及未取得原书/原刊全文的限制。当前团队的
独立内部审查不等于人类同行评审、期刊录用或完整 ARS 十阶段认证。
作者身份、贡献、资助及利益冲突信息仍须由责任作者在任何投稿前确认。
本轮未上传论文到第三方模型，也未作期刊投稿。

## C108 历史依赖纠错

[新缺陷记录](nonlinear_return/BUG_FINDING_C108.md) 展示实际指定 Hénon
映射与旧二周期 producer 方程不符。对字面映射及原参数，正确 τ₂=0，
旧 −1664/1725 和直接依赖的 determinant 前缀不能继续作为通过证据。
CURRENT 与注册表已隔离这些依赖；C108 的旧冻结文件和旧评估没有改写，
该发现不自动否定其余命题，也不是本批第六篇论文。

## 构建、复用和封存边界

真实最终命令、两个新空目录、输入/PDF 哈希、日志/字体/文本与逐页目视
在 [FINAL_BUILD_REPORT.md](FINAL_BUILD_REPORT.md)。C399/C400 的原 23 页和
先前已验收收据不重复执行；C401–C403 的 36 页本轮已逐页检查。
`paper-plan → paper-write → paper-compile` 用于完整主张驱动写作及真实 PDF；
ARS 适用的来源/完整性原则使经典所有权、未做项与 AI 辅助状态显式保留。
没有沿用旧模型、ML 配额或虚构外部评审。

封存集合是此目录的全部实际文件，以及通过相对路径引用的
`../research_c399_c403/` 原 59 个冻结文件。两个原 PDF 不搬迁，不修改旧
manifest。精确 ledger 排除它自身及本轮 manifest；本轮 manifest 包含
ledger 并只排除自身。最终集合必须无符号链接、无额外成员且摘要一致。
清单见 [PAYLOAD_FILES.txt](PAYLOAD_FILES.txt) 与 [MANIFEST.sha256](MANIFEST.sha256)。
共享 CURRENT/注册表、外部经典来源和固定 evaluator 不在该 payload 树内，
分别由 Git、来源记录及 evaluator 固定 SHA256 约束。没有新造发布程序。

封存后的实际只读核验及授权 Git 同步状态见
[当前入口](../CURRENT_RESEARCH_STATE.md) 与 Git 对象；本目录封存后不为
写入自身提交号而循环改写。用户确认的五篇检查点停在 C403，未启动 C404。
