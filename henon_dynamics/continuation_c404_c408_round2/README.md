# C404–C408 续接：三篇完成，两篇空缺

2026-09-06。当前交付 **C404–C406 三篇完整研究稿，共 33 页**。
这不是五篇批次完成声明：C407/C408 尚无通过实质门槛的合同，未开始
C409。首轮九组候选/零篇论文的 [冻结检查点](../research_c404_c408/README.md)
保持原字节；本次不重计那些有限反例或旧论文。

## 三个独立问题与实际 PDF

| 编号 / 页数 | 正文 PDF | 完整源结论及实际增量 | Route A |
|---|---|---|---|
| C404 / 10 | [非线性 Hénon–Frobenius 共振计数](henon_resonance/paper/main.pdf) | 对 `H=(y,y^q+g(y)-a x)`、`2<=m=deg(g)<q`、`p` 不整除 `m`，证明系数统一的全周期普通点数，尤其完整 p-幂时钟的非线性抵消；同一计数的 zeta 及每个正整数幂具有自然边界。 | 源机制 EXPLORATORY |
| C405 / 10 | [临界整除 Gram 的奇异型与极限](arithmetic_forms/paper/main.pdf) | 在 `a(k)=k^(-1/2)L(k)` 临界线上给出完整可求和二分：发散分支的 GCD 型纯奇异且正逐项逼近强预解式塌缩到零；可求和分支收敛到最大行式卷积的非零 Gram。 | 源机制 EXPLORATORY |
| C406 / 13 | [调和 δ 链的临界第二 Weyl 系数](critical_delta/paper/main.pdf) | 任意正耦合 `b_n/n -> kappa>0` 的两项计数律，完整周期态密度积分系数及其严格单调范围；核心是增长过渡区域的局部周期化与累计 `o(k)` 误差，兼及率无关稳定性和硬/软端点。 | REJECTED |

[部分合同计划](ADMISSION_AND_BATCH_PLAN.md) 冻结各自对象、参数、时钟、
域、observable、经典输入及成篇门槛；没有将一个主定理的推论拆为多篇。
三份稿件包含完整证明，不是计划书或仅有公式的脚手架。

目标 A2/A3 全部 FAIL；27 个目标/Route-B scope flags 全为 false，
27 个目标指标为 NOT_TESTABLE，不是零误差。强制三类算术对照仍
INCOMPLETE。C404 的 A1_PASS_ANALYTIC 仅指原生有限域周期问题；
C405 的 A4_FORMAL_HINT 和 C406 的 A4_NATURAL_QUANTIZATION 也只
属于各自源算子。完整 tuple 与未做项见 [评价范围](EVALUATION_SCOPE.md)
及三份 YAML；另有 [独立边界一致性审计](reviews/EVALUATION_BOUNDARY_REVIEW.md)。
保持 `NO_BAD_EULER_OR_ROOT_NUMBER`，没有目标欧拉因子、根数、零点
对应、Hilbert–Pólya 实现或 Route-B 晋级。

## 证明、来源与内部审查

| 稿件 | 全量词证明 / 来源审计 | 独立实际正文审查 |
|---|---|---|
| C404 | [证明](henon_resonance/PROOF_PACKAGE.md) / [来源](henon_resonance/SOURCE_AUDIT.md) | [C404 全文审查](reviews/C404_MANUSCRIPT_REVIEW.md) |
| C405 | [证明](arithmetic_forms/PROOF_PACKAGE.md) / [来源](arithmetic_forms/SOURCE_AUDIT.md) | [C405 全文审查](reviews/C405_MANUSCRIPT_REVIEW.md) |
| C406 | [证明](critical_delta/PROOF_PACKAGE.md) / [来源](critical_delta/SOURCE_AUDIT.md) | [C406 全文审查](reviews/C406_MANUSCRIPT_REVIEW.md) |

各证明包先接受独立的证明/最近来源/实质准入检查，随后三份实际正文
分别完成非作者全文审查。当前未留下必须修订的数学、引文或范围问题。
C405 在写作前补强 Simon 一般二次型分解的归属，并已定点复核；
其一般变分推论不单列为创新。C406 原证明审查者后来写作，故另由
不同研究者检查正文，未将作者早先的审查冒称为其稿件的独立审查。

C404 的 [五组新精确检验](henon_resonance/CHECK_RECEIPT.md) 含真实 F4
系数及 `p|m` 的失败控制；未重跑首轮旧例来增加检查次数。C405 的
[有理算术 sentinel](arithmetic_forms/BOUNDED_RECEIPTS.md) 只验证有限
恒等式和假设失败控制，不验证无穷收敛。C406 是解析证明，不制造
数值实验。数学正确性、有限可执行证据与文件摘要各有不同作用。

文献检索有界，来源记录明确真正读取的版本、范围和全文缺失项，不
宣称全球优先权。审查由当前 AI 团队内部完成，不等于人类同行评审、
期刊录用或完整 ARS 十阶段认证。责任作者身份、贡献、资助及利益
冲突信息须在任何投稿前由实际作者确认；本轮没有第三方稿件上传。

## 为什么还缺两篇

- [野性动力学札记](wild_dynamics/SCOUT_REPORT.md)：首返交数加权
  全周期公式数学成立，但已知局部深定理之外的剩余增量不足以支撑
  本批要求的独立实质论文。接受 [独立审查](nonlinear_geometry/CROSS_REVIEW_WILD_DYNAMICS.md)，
  不分配 C 号。`p=3,H=1+x+x^2,n=2` 的普通非零点数 13 与加权值
  15 不可混用，不能把加权结论改名为普通计数。
- [非线性几何候选](nonlinear_geometry/SCOUT_REPORT.md)：Lyness/QRT
  拟议计数落入经典来源；cluster 低期递推拟合被 `k=6,n=5` 的
  [精确边界重数反例](nonlinear_geometry/PARTIAL_RESULTS.md) 推翻，
  实际环面方案长度 6666 而非拟合值 6726。局部反例不是全周期
  分类，也不是整个模型族不存在有用结果的 no-go。

因此本轮具体限度是三个可辩护的完整合同，不是五个。继续本批时仍
应先解决 C407/C408 的实质问题，不重开这三篇已验收的证明和构建。
另有 [独立缺额与计篇边界审计](reviews/PARTIAL_BATCH_BOUNDARY_REVIEW.md)
全文核对两条未准入线；它将科学合同缺额与仅欠排版区分，并确认
上述特定反例不构成全模型族 no-go。

## 构建、封存及同步边界

三稿各做两次新空目录构建，两次 PDF 及经审查初稿逐对同字节；最终
日志无未解析引用或排版警告，字体全嵌入，全部 33 页已实际逐页查看。
命令、真实目录、工具版本、原始日志、输入及 PDF 摘要见
[最终构建收据](FINAL_BUILD_REPORT.md)。
另有 [独立本地链接与交付一致性审计](reviews/RELEASE_LINK_AUDIT.md)，
它只核对链接、PDF 实测数据及索引范围，不重复数学或终构建。

`paper-plan`、`paper-write`、`paper-compile` 用于完整论证、核实引用
和实际 PDF；研究与 ARS 的相关来源/诚信规则使经典归属及 AI 辅助范围
显式保留。本地 `henon-route-a-batch` 的实质门槛导致两条未准入线仅
保留研究记录；不以旧 ML 配额、固定模型或文件数量代替研究判断。

封存集合是本目录的全部实际文件。精确 [payload ledger](PAYLOAD_FILES.txt)
只排除自身及 [manifest](MANIFEST.sha256)；manifest 包含 ledger，
仅排除自身。最终只读核验要求摘要匹配、成员完全一致、无重复、额外
文件或符号链接。原首轮、旧论文、共享 CURRENT/注册表、外部文献和
固定 evaluator 不在这个载荷树内，分别由原封存、Git 和来源记录约束。
没有新增发布程序或虚构篡改测试。

封存后的真实核验与 Git 同步状态见 [当前入口](../CURRENT_RESEARCH_STATE.md)
及 Git 对象；不为把自身提交号写入 payload 而循环改写 manifest。
八个继承未跟踪目录保留并排除暂存。当前检查点为三篇已完成、两篇
未完成，不是 C404–C408 五篇完成。
