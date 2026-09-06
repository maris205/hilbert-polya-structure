# C404–C408：五项独立合同的续接冻结计划

2026-09-06。用户在三篇部分交付后明确“继续”；只补 C407/C408，
不进入 C409。起点 `ec024cadfbb728cc66aa0dcaca88a6d2f4dbd4d0`。
本文件冻结五项现已通过实质准入的合同，并不提前宣称两篇新稿已完成。

## 三项已封存合同：复用，不回写或重跑

以下三项的精确量词、证明、非作者审查、双新目录同字节构建和全部
33 页 QA 已在 [原部分合同计划](../continuation_c404_c408_round2/ADMISSION_AND_BATCH_PLAN.md)
与 [原交付记录](../continuation_c404_c408_round2/README.md) 冻结。
原包 179 个文件保持原字节；本次不将既有工作计作新增成果。

| 编号 | 独立问题与完整结果 | 当前完成状态 |
|---|---|---|
| C404 | 非线性 Hénon–Frobenius 共振在整个 p-幂塔中的交数及普通全周期计数，覆盖旧非共振定理遗漏分支 | 已封存，10 页 |
| C405 | 临界整除 Gram 归一化极限的最大可闭下界与强预解式二分，不限乘性慢变权 | 已封存，10 页 |
| C406 | 调和 δ 链临界尺度的第二 Weyl 系数、全渐近耦合类稳定性及端点 | 已封存，13 页 |

## C407：双素数与野性失真下的完整聚点集拓扑

对象为 BCH 定义的正熵、唯一主根（hyperbolic）有限 adelic 失真
系统的原生整数时钟。observable 为 `N*pi_f(N)/Lambda^N` 的整个
聚点集，`pi_f(N)` 是长度不超过 N 的 primitive orbit 数。
先在明确的有限素数、正周期系数及非负实周期指数数据上证明连续
detector image 定理；动力学推论只用于实际满足 FAD 定义的系统。

冻结合同：[精确参数与范围](arithmetic_candidate/CONTRACT.md)、
[完整证明](arithmetic_candidate/PROOF_PACKAGE.md)。无 active prime 时
聚点集有限；有 d>=1 个 active primes 时为 Cantor 集，并满足
`N_epsilon <= C(1+log(1/epsilon))^(2d)`，因此上盒维为零。
覆盖全部有限素数和允许的野性指数，不限一个经典算例。

新增证明是自适应 valuation-tree 覆盖与有限径向核类型的严格负
Fourier 系数／渐近支配，从而在每个 cylinder 排除局部常值。
detector 渐近式、已知单素数 Cantor 结果、负整数切片技巧及经典
固定点实现均明确扣除；三个不同 regime 的实现只是同一定理应用，
不拆篇。参见 [来源审计](arithmetic_candidate/SOURCE_AUDIT.md) 和
[实际动力学实现](arithmetic_candidate/REALIZED_EXAMPLES.md)。

准入依据：协调者独立通读完整证明与合同并核验关键原文；另有
[非作者独立数学及来源审查](wild_ordinary/CROSS_REVIEW_ARITHMETIC_TOPOLOGY.md)，
未发现数学阻断。对照 BCH 2024 公开 v2 中明确留下的 hyperbolic
regimes，结果具有完整问题级增量。2026 引文列其 EMS 书稿待出版，
最终书稿未取得；该版本缺口必须进入正文，不保证全球优先权。
不声称一般 nonhyperbolic 情形、detector 单射或 Haar 推前无原子。

## C408：奇次循环交换关系的交替零点局部交长

对象固定为复数域上的**未饱和**有限循环关系代数
`C[x_i:i mod 2m]/(x_i^k+1-x_(i-1)*x_(i+1))`，所有奇数 k>=3、m>=1。
时钟是关系式的原生长度 n=2m；observable 是全部交替零支撑处的
局部代数长度，不是普通周期点数，也不是光滑 cluster surface 的
固定点概形。完整合同及证明见 [证明包](cluster_boundary/PROOF_PACKAGE.md)。

每个交替零点具有同一长度 ell_m。设
`D_k(t)=1-t-(k-1)t^2-t^3-2k*t^4`，
`-log D_k(t)=sum T_m*t^m/m`，则
`ell_m=T_m+1+4(k-1)*1_(4|m)`。
其局部长度生成函数为
`Z_k(t)=1/((1-t)D_k(t)(1-t^4)^(k-1))`。
原生时钟边界贡献为
`Z_k(u^2)^((k+1)/2) Z_k(-u^2)^((k-1)/2)`；不称 Artin–Mazur zeta。

已知交替 deep support 归 Beyer–Muller；新增实质是全 m、全奇 k 的
非约化厚度分类，尤其路径核抵消后的 `2k-1`、循环二维核 `4k+1`
及坐标／梯度分支的合法交数加法。生成函数是同一合同推论，不另计。
准入依据为 [根协调者非作者完整审查](ROOT_CLUSTER_REVIEW.md)、原方程
六项独立局部标准基检查及 [来源核验](cluster_boundary/SOURCE_AUDIT.md)。
较大 k=3,m=4 的直接计算被终止且未计 PASS；该共振由已复核的
全量词解析证明支撑。完整边界、偶 k 及 torus 总计数仍不在合同内。

## 未准入材料与防止凑数

`wild_ordinary/` 的 p=3、period 12、局部权重 4 精确反例已由
独立 h-adic 计算验证；同类有限域循环定理保留研究札记，不作为
第六论文或第四个新 PDF。`spectral_candidates/` 的双素数张量谱
no-go 是已知谱的短推论，未准入；其它替换线的失败理由保留。

## 剩余完成门槛与职责

两位作者只写各自 PAPER_PLAN 与完整独立 LaTeX 正文。协调者拥有
共享状态、正式 Route-A v0.2.0 评价、发布清单及 Git。新稿必须通过
非作者正文／实际引文审查，定点修复、两次新空目录确定性构建、
字体文本告警与所有最终页面 QA，然后封存精确 payload 成员并只读
核验。只有这些门槛完成后才称五篇批次完成。

写作采用 `paper-plan`、`paper-write`、`paper-compile` 的可追溯
论证和构建要求；纯数学不用旧 ML 会议/GPU/固定 GPT-5.4 审查配额。
当前团队内部审查不是人类同行评审，无外部上传。源算术、局部
关系长度或 Cantor 拓扑不提升目标 A2/A3；三类对照未运行则如实
INCOMPLETE。保持 `NO_BAD_EULER_OR_ROOT_NUMBER`，不进入 Route B。

完成后仅同步授权 C 系列新包和相关索引，交付原三篇加两篇新的
五个 PDF，并在 C408 停下；八个继承未跟踪目录继续保留不暂存。

## 本计划的完成记录

正文审查、构建与页面 QA 门槛现已完成；精确封存核验与 Git 同步
由协调者继续收尾，其最终状态见 [当前入口](../CURRENT_RESEARCH_STATE.md)。
C407 13 页、C408 12 页，各自非作者正文与引文审查的必要修订关闭；
两次新空目录构建同字节，全部 25 页实际检查。
连同保持原字节的 C404–C406 共五篇、58 页。冻结时的“剩余”任务
保留为计划历史，完成证据以 [最终构建收据](FINAL_BUILD_REPORT.md)
和 [五篇交付入口](README.md) 为准；目标 A2/A3 未获提升。
