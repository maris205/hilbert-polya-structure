# P32 内部研究：辅助分量记录与连续读出下的恢复极限障碍

记录日期：2026-09-08 UTC。接续[形式产品与阶乘极限笔记][limit-note]。本次新增一个辅助拓扑记录空间，在其中定义并检验“分量保持的形式恢复”，再给出向其他拓扑实现传递障碍的明确条件。它不是原稿已经定义的全 owner Euler 乘积，也不替换原来的零 content 带标签不交并。

核心结论：在保留既定分量拓扑的辅助记录空间中，固定阶乘序列没有极限；任何保留同一个精确、连续的零-owner 读出的拓扑实现，也不能承载该序列的收敛极限。这是带有读出条件的排除结论，不是对所有标量化或所有恢复方案的无条件否定。

## 1. 输入与原有类型不变

沿用[原稿的全体数学 owner 索引][owner-frame]及[形式空间定义][carrier]：`O_+` 为正 content 的有向本原共轭类，`O_0` 为零 content 的有向本原共轭类。正分量仍是

\[
R_+=\varprojlim_{(F,D)}R_{F,D},\qquad
R_{F,D}=\mathbb Q[u_g:g\in F]/\mathfrak m_F^{D+1},\qquad
\mathfrak m_F=(u_g:g\in F).
\]

各有限坐标离散，过渡映射删除其他变量并截断总次数。保留全部有限 `(F,D)` 坐标，包括混合 owner 单项式，不以 singleton 投影代替整个 `R_+`。

[零分量原定义][zero-carrier]仍为

\[
R_0=\bigsqcup_{g\in\mathcal O_0}\{g\}\times H_g.
\]

各 `H_g` 的系数为有理数，指数为非负有理数、支撑良序；非零元素的 `v_g` 为其最小支撑指数，约定 `v_g(0)=+infinity`。取原有赋值拓扑，零邻域为 `U_r={h:v_g(h)>r}`。不同 owner 的变量和标签不合并；原 `R_0` 中的运算仍只在同一个纤维内进行。

上一份笔记已经构造了 `mathcal P_N^+`、`mathcal B^+` 和 `mathcal P_*^+`。其有限坐标分别是以下因子的有限乘积再截断：

\[
f_{N,g}=(1-u_g^{d(g)/\gcd(N,d(g))})^{-\gcd(N,d(g))},
\qquad b_g^+=(1-u_g^{d(g)})^{-1},
\qquad f_{*,g}=(1-u_g)^{-d(g)}.
\]

本次不重新把这些已证结果当作新进展。用到的两个明确 owner 是[显式非真幂族][owner-note]中的

\[
g_{\mathrm{hc}}=[a_1^2[a_1,b_1]]\in\mathcal O_+,\quad d(g_{\mathrm{hc}})=2;
\qquad g_{\mathrm{zc}}=[[a_1,b_1]]\in\mathcal O_0.
\]

外层括号表示有向共轭类。这两个名称不是规范枚举序号，也不表示本次生成了机器 owner 证书。控制序列始终为 `N_k=k!`、`k>=1`。

## 2. 新增辅助记录空间，不新增跨 owner 乘法

定义

\[
\mathscr C_{\mathrm{rec}}
:=R_+\times\prod_{g\in\mathcal O_0}^{\mathrm{Cartesian}}H_g.
\]

这里的元素是 `(x,h)`：`x in R_+`，而 `h` 是定义域为 `O_0` 的函数，满足每个 `h(g) in H_g`。这是一次记录所有标签值的笛卡尔积；原 `R_0` 的一个元素只落在一个带标签纤维中，二者不是同一个对象。

本笔记只赋予 `mathscr C_rec` 乘积拓扑，并定义到 `R_+` 的投影 `pr_+` 及到各 `H_g` 的投影 `pr_g`。不在此定义跨 owner Euler 乘法、跨纤维求和、到 `R_+` 的零分量强制转换，或把所有零变量合成为一个 Hahn 级数。这些投影是新辅助空间的坐标投影，不是声称原 `R_0` 已提供全 owner 合并或删除分支的映射。

对每个整数 `N>=1`、每个 `g in O_0`，定义

\[
a_{N,g}=(1-z_g^{1/N})^{-N}
=\sum_{j\geq0}\binom{N+j-1}{j}z_g^{j/N},
\qquad b_g^0=(1-z_g)^{-1}.
\]

各支撑分别为 `(1/N) Z_(>=0)` 和 `Z_(>=0)`，均良序，故各值确实属于对应的 `H_g`。公式显式给出每个标签的值，所以以下记录存在，无须任选代表、假定可数枚举或要求不同 owner 支撑的联合良序性：

\[
C_N=\bigl(\mathcal P_N^+,(a_{N,g})_{g\in\mathcal O_0}\bigr),
\qquad
C_{\mathrm b}=\bigl(\mathcal B^+,(b_g^0)_{g\in\mathcal O_0}\bigr)
\quad\in\mathscr C_{\mathrm{rec}}.
\]

乘积拓扑的有限柱状邻域可写为：在 `c=(x,h)` 附近，固定有限 `F subset O_+`、非负整数 `D`、有限 `G subset O_0` 和各纤维阈值 `r_g>=0`，要求

\[
p_{F,D}(x')=p_{F,D}(x),\qquad
v_g(h'(g)-h(g))>r_g\quad(g\in G).
\]

这些集合构成邻域基。正分量若同时指定有限多个坐标，可取 owner 集的并和次数的最大值，得到一个更细的上述邻域；零分量只涉及有限个标签。减法始终在各自的 `H_g` 内进行。

## 3. “分量保持的形式恢复”是辅助判准

在本笔记中定义辅助判准（auxiliary criterion）：沿固定 `N_k=k!` 的分量保持形式恢复，指下述合取成立：

\[
\mathcal P_{k!}^+\longrightarrow\mathcal B^+\quad\text{于 }R_+,
\qquad
\forall g\in\mathcal O_0,\quad a_{k!,g}\longrightarrow b_g^0
\quad\text{于 }H_g.
\tag{CR}
\]

**命题 1。** `(CR)` 等价于 `C_(k!) -> C_b` 在 `mathscr C_rec` 中成立。

证明：若 `C_(k!) -> C_b`，则每个坐标投影的连续性给出 `(CR)`。反过来，假设 `(CR)`，给定第 2 节的一个有限柱状邻域，正分量的收敛给出该 `(F,D)` 坐标的最终稳定阈值；每个 `g in G` 的收敛给出对应赋值邻域的阈值。取这些有限多个阈值的最大值，即保证整个记录最终落在该邻域中。因此得到记录收敛。

零分量一侧的量词是

\[
\forall g\in\mathcal O_0\ \forall r\geq0\ \exists K(g,r)\ \forall k\geq K(g,r),
\quad v_g(a_{k!,g}-b_g^0)>r.
\]

它不要求一个对全部 owner 共同有效的 `K`；这里采用乘积拓扑，不是同时约束无限多坐标的盒拓扑。正分量仍要求所有有限 `(F,D)`，不是只查单变量投影。命题 1 只说明新辅助空间与新判准等价，尚未证明该判准与原项目的全部解析恢复目标等价。

## 4. 两个障碍给出不同强度的结论

### 4.1 正 content 坐标排除基准极限

令 `u=u_(g_hc)`，取离散空间 `Q[u]/(u^2)` 中的连续读出

\[
E_{\mathrm{hc}}:=p_{\{g_{\mathrm{hc}}\},1}\circ\operatorname{pr}_+
:\mathscr C_{\mathrm{rec}}\longrightarrow\mathbb Q[u]/(u^2).
\]

由[上一笔记第 4 节][limit-note]的已证坐标公式，

\[
E_{\mathrm{hc}}(C_{k!})=1+2u\quad(k\geq2),\qquad
E_{\mathrm{hc}}(C_{\mathrm b})=1.
\]

`2u!=0`，所以开邻域 `E_hc^(-1)({1})` 包含基准记录，却排除整条 `k>=2` 的尾端。因此 `C_(k!)` 不趋于 `C_b`，辅助判准 `(CR)` 失败。

这一证据本身只排除基准极限，不排除其他极限；事实上正分量本身确实收敛到 `mathcal P_*^+ != mathcal B^+`。若要排除整个记录的任何极限，需要另一个论据。

### 4.2 固定零 content 坐标排除记录空间内的任何极限

在同一个 `H_(g_zc)` 内，简写 `a_N=a_(N,g_zc)`。上一笔记第 5 节已证明

\[
v_{g_{\mathrm{zc}}}(a_N-a_M)=1/N\qquad(N>M\geq1).
\]

其原因是常数项抵消后，`a_N` 的最小正指数为 `1/N`、系数为非零有理数 `N`，而 `a_M` 的最小正指数为更大的 `1/M`。因此在任意尾端中都可取 `k>=2` 使

\[
v_{g_{\mathrm{zc}}}(a_{(k+1)!}-a_{k!})=1/(k+1)!<1/2.
\]

差不落在固定零邻域 `U_(1/2)` 中，故该纤维序列非柯西，并且不收敛于 `H_(g_zc)` 中任何点。这里无需完备性：若收敛于 `a`，两个充分靠后的项与 `a` 的差都有赋值大于 `1/2`，赋值不等式就迫使它们的互差赋值也大于 `1/2`，矛盾。

**命题 2。** 序列 `(C_(k!))` 在 `mathscr C_rec` 中没有极限。

证明：若 `C_(k!) -> C`，连续投影 `pr_(g_zc)` 将给出 `a_(k!,g_zc) -> pr_(g_zc)(C)`，与上一段矛盾。

本笔记只给记录空间指定了拓扑，因此此处结论写作“没有极限”，不另称整个记录序列“非柯西”。非柯西的计算发生在已指定赋值邻域的单个 `H_(g_zc)` 中。

## 5. 向其他空间传递：必须保留精确且连续的读出

**命题 3（连续分量读出下的恢复极限障碍）。** 设 `X` 为任意拓扑空间，`x_k in X` 为序列，`x_b in X` 为候选基准。

1. 若存在固定连续映射 `E:X -> Q[u]/(u^2)`，目标取离散拓扑，满足 `E(x_k)=1+2u` 对所有 `k>=2` 成立且 `E(x_b)=1`，则 `x_k` 不趋于 `x_b`。
2. 若存在固定连续映射 `Z:X -> H_(g_zc)`，满足对所有 `k>=1` 都有 `Z(x_k)=a_(k!,g_zc)`，则 `x_k` 不收敛于 `X` 中任何点。

证明：第一项若有 `x_k -> x_b`，则连续性给出 `E(x_k) -> 1`，但离散空间中的收敛要求最终等于 `1`，与精确坐标值矛盾。第二项若有 `x_k -> x`，则连续性给出 `a_(k!,g_zc) -> Z(x)`，与第 4.2 节矛盾。

两个结论都不要求 `X` 上有乘法，不要求读出线性、保乘法或单射，也不要求 `X` 为 Hausdorff。第一项实际上只需在 `x_b` 连续；第二项的读出须在所讨论的候选极限点处定义并连续。仅在序列取值集合上定义一个读出，不能排除它在该读出定义域之外的极限。

“固定”也不可省略：`Z` 读的是同一个 owner、同一个赋值拓扑下的精确元素；它不是随 `k` 改变的映射族。增加其他辅助坐标不影响命题，只要上述固定连续读出仍然存在并满足精确等式。

普通连续性只传递收敛，不能仅凭第二项推出任意 `X` 中的序列非柯西。作为一般连续性不足的另一个例子，令 `X=(0,1]` 与目标 `R` 均取通常度量：`x_k=1/k` 是柯西序列，而连续映射 `Z_tilde:X -> R`、`Z_tilde(t)=1/t` 的像序列 `k` 非柯西。该实数目标例子不是命题 3 的 `H_(g_zc)` 读出实例。若另要传递柯西性质，必须指定一致结构并增加适当条件，例如读出的一致连续性。本命题不作这样的新增声明，也不额外推出聚点、子序列或扩张空间中的极限不存在。

## 6. 与原项目之间仍须补的桥梁

| 结论层 | 本笔记支持的范围 | 不能自动推出 |
| --- | --- | --- |
| 辅助空间存在 | 显式记录一个完整正分量及所有带标签零分量 | 全零 owner 或正零混合的 Euler 乘法对象已构造 |
| 辅助判准失败 | 原有分量拓扑下，`C_(k!)` 不趋于基准，且没有任何极限 | 该判准已等价于原计划所有解析恢复目标 |
| 向 `X` 传递障碍 | 精确读出等式及其连续性成立时，得到命题 3 的相应结论 | 任意标量化、任意重新组织或任意拓扑实现都失败 |

目前没有证明原项目的任何全 owner 解析实现都必然具备连续的 `H_(g_zc)` 读出。尤其，单个标量产品的收敛并不自动提供可连续取回独立 owner 的映射。若某方案合并或丢弃 owner、改变读出、拓扑、基准或归一化，就必须重新核对命题前提；本笔记既不否定这些前提之外的全部方案，也不授权改变冻结方案。

几何解释仍须保留[覆盖推导][cover-note]的明确覆盖、物理时钟、本原提升及因子计数条件。显式群论 owner 和符号最小周期不替代 `SG2OwnerCanonical-v1` 的一般接口、冻结枚举和输入证书。本次未建立整个 `R_+` 或 `H_g` 上的标量映射，没有证明数值产品发散，没有启动 content-one 解析阶段、AN-1–AN-5、Route 评估或 Stage 5／6；正式完整性 `FAIL / BLOCK` 不变。

## 7. 论证核对与保存范围

按 ARS 的论证流程，论证链为：既有分量及精确公式 → 新辅助空间与有限柱状拓扑 → 分量收敛等价 → 两种不同强度的障碍 → 有条件的连续读出传递。对主要反问分别限定：笛卡尔积不等于 Euler 产品；乘积分量收敛不等于 owner 一致收敛；排除基准不等于排除任意极限；普通连续性不传递任意柯西性质；辅助判准不自动等同于解析目标。

三个只读推敲任务分别检查类型与乘积拓扑、连续读出命题、以及与原计划的范围边界；主线程整合并写出证明。同系助手的意见只作逻辑查错，不作为独立科学证据。论证依赖下列既有定义和已写出的证明，不新增外部文献结论或来源查询，也不作投稿适配或独立复核认证。

本次只新增此内部笔记，并在上一笔记和总内部研究记录中追加入口。实际文件核对使用只读 `node` 内联检查：检查本笔记及新增入口的链接与条件标记；按编辑前字节长度和 SHA-256 核对两个追加文件的原文前缀，以及 R6、显式 owner 笔记、条件覆盖推导、Recovery3 状态和完成报告五个保护文件的不变性。这些是文件级检查，不认证数学正确性。没有运行科学实验、枚举、数值计算、既有审查脚本或论文构建；没有修改论文、锁、回执、文献库、代码或结果文件。

[limit-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_formal_product_limits_20260908.md
[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[owner-frame]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:188
[carrier]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:720
[zero-carrier]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:778

## 后续内部推导入口（2026-09-08）

后续见[有限标量求值的形式拓扑不连续性与延拓障碍](internal_scalar_topology_bridge_obstruction_20260908.md)：对有限域明确采用继承形式拓扑后，证明非空正分支及固定零 owner／模数的标量求值不连续，排除与整个指定有限域相容的连续延拓，并用有理常数另证精确反向读出的连续性障碍。此结果不否定本笔记的形式投影，也不等于数值 Euler 产品发散；旧文与正式审查状态不变。
