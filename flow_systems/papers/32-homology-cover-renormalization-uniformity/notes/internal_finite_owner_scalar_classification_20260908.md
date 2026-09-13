# P32 内部研究：有限 owner 标量层的复对数连接与分类

记录日期：2026-09-08 UTC。接续[单个零 owner 的复增长笔记][complex-note]，本轮把有限标量乘积、条件几何复对数连接、固定有限集合的分类，以及正实轴上对扩大截断仍有效的下界一起完成。仍只作内部研究记录，不修改冻结原文、归一化或正式审查状态。

本轮完成的是下述明确有限公式的理论层：固定集合若无零 owner 且全为 content one，则恒等于基准；若无零 owner 但含高 content，则沿阶乘序列稳定到不同的全纯函数；若含零 owner，则在每个固定复紧集上模长发散。正实轴的正性还给出对任意保留指定见证的有限截断族统一有效的下界。它们不等于全 owner 乘积、机器输入认证或正式 Route 结论。

## 1. 有限对象与保留的几何前提

令 `Omega={s in C:Re(s)>0}`。取数学 owner 索引中的有限集合

\[
E=E_+\sqcup E_0,\qquad
E_+\subset\mathcal O_+,\quad E_0\subset\mathcal O_0.
\]

各 owner 互异、有向且本原，长度 `ell_g>0` 固定；正分支有 content `d_g>=1`。该集合不是本次已执行的冻结 panel 或规范枚举前缀。几何解释要求各标签确实绑定互异的基流轨道和最小周期，并保留[条件覆盖推导][cover-note]的 H0–H3；不能仅凭任意数据表声称这些条件已被认证。

对整数 `N>=1`，仅对 `g in E_+` 令 `q_(N,g)=gcd(N,d_g)`，定义有限求值函数

\[
F_{N,g}(s)=
\begin{cases}
(1-e^{-s\ell_g/q_{N,g}})^{-q_{N,g}},&g\in E_+,\\
(1-e^{-s\ell_g/N})^{-N},&g\in E_0,
\end{cases}
\]

\[
Q_{N,E}(s):=\prod_{g\in E}F_{N,g}(s),\qquad
B_E(s):=\prod_{g\in E}(1-e^{-s\ell_g})^{-1}.
\]

空积为一。各因子来自[既有有限形式域的分别求值][finite-domains]，分母在 `Omega` 上非零，故这些有限函数全纯且无零点。正零分支在求值后于 `C` 中作有限乘法，不是在不同 `H_g` 间新增形式乘法，也没有在整个 `R_+` 或 `H_g` 上宣告标量映射。

冻结模数序列始终为 `N_k=k!`。以下在适当处证明全整数公式的性质，但不以另一条子序列替换它。

## 2. 补上有限几何乘积的全纯对数连接

本节是新给出的复域连接定义与证明，不改写成“旧 H3 已经规定复对数”。它保留旧正实规则，并明确排除对原始高次乘积直接套 principal Log 的做法。

### 2.1 单个周期的归零全纯对数

对固定 `T>0`，定义

\[
L_T(s)=\sum_{r\ge1}\frac{e^{-rsT}}r,\qquad s\in\Omega.
\]

固定非空紧集 `K subset Omega`，令 `a=min_K Re(s)>0`。该级数被 `sum_(r>=1)e^(-raT)/r` 一致控制，后者不超过几何级数，故绝对且局部一致收敛。这里的 `r` 是单因子的级数指标，不是 owner 求和。

具体地，单位圆盘中的幂级数 `G(z)=sum_(r>=1)z^r/r` 满足 `G'(z)=1/(1-z)`，所以

\[
\frac{d}{dz}\bigl((1-z)e^{G(z)}\bigr)=0,
\qquad (1-0)e^{G(0)}=1.
\]

复合 `z=e^(-sT)`，得到全纯函数及精确恒等式

\[
e^{L_T(s)}=(1-e^{-sT})^{-1}.
\]

正实 `s` 时，`L_T(s)` 为实数，故等于这个正实因子的实对数。由 `0<=L_T(s)<=e^(-sT)/(1-e^(-sT))`，沿正实 `s -> +infinity` 有 `L_T(s)->0`。

这也是唯一满足该归零条件的全纯对数：另一个全纯对数与它的差取值于 `2 pi i Z`，因 `Omega` 连通而为常数；正实无穷处的归零条件迫使该常数为零。这里没有借助未指定的对数分支。

### 2.2 先缩放周期，再缩放有限乘积的对数

固定层数 `N` 与有限集合 `E`，假设其几何覆盖和轨道输入满足 H0–H3。以 `T_(N,g,j)>0` 表示第 `j` 条本原提升轨道的未缩放最小周期，`c_(N,g)` 为条数。不同基轨道不能共用同一条提升轨道，因为一条提升流轨道的投影只有一个基流轨道；故有限集合的汇总不引入额外重复计数。方向与 deck 计数仍按原约定。

先写未缩放乘积，再实施一次时间缩放：

\[
U_{N,E}(s)=\prod_{g\in E}\prod_{j=1}^{c_{N,g}}
(1-e^{-sT_{N,g,j}})^{-1},
\]

\[
t_{N,g,j}=T_{N,g,j}/N,\qquad
V_{N,E}(s)=U_{N,E}(s/N)
=\prod_{g\in E}\prod_j(1-e^{-st_{N,g,j}})^{-1}.
\]

其在正实无穷处归零的全纯对数为

\[
L_{V,N,E}(s)=\sum_{g\in E}\sum_jL_{t_{N,g,j}}(s).
\]

和是有限的，指数化恰给 `V_(N,E)`；与上面相同的连通性证明给出唯一性。定义旧实归一化配方的全纯延拓

\[
\widehat F_{N,E}(s)
:=\exp\bigl(N^{-3}L_{V,N,E}(s)\bigr).
\]

在正实轴上，有限对数和就是 `log V_(N,E)` 的实值，因此严格匹配先乘 `1/N` 的时间、再乘 `1/N^3` 的对数两项旧操作。它不是再缩放一次周期，也不是将乘积值直接乘 `N^-3`。

已证的覆盖计数给出

\[
\begin{array}{c|c|c|c}
 &c_{N,g}&T_{N,g,j}&t_{N,g,j}\\ \hline
g\in E_+&N^3q_{N,g}&N\ell_g/q_{N,g}&\ell_g/q_{N,g}\\
g\in E_0&N^4&\ell_g&\ell_g/N
\end{array}
\]

因此

\[
N^{-3}L_{V,N,E}(s)
=\sum_{g\in E_+}q_{N,g}L_{\ell_g/q_{N,g}}(s)
+\sum_{g\in E_0}N L_{\ell_g/N}(s).
\]

指数化后，`q_(N,g)` 与 `N` 都是整数，故

\[
\boxed{\widehat F_{N,E}(s)=Q_{N,E}(s),\qquad s\in\Omega.}
\]

这补上了有限层的条件几何连接，而不留下分数幂歧义。归零全纯对数唯一；作为旧正实函数的全纯延拓，结果也唯一，因为两个这样的函数之差在正实轴上有内部聚集的零点，恒等定理使其在连通的 `Omega` 上恒为零。空 `E` 时，`U=V=1`、`L_V=0`、`widehat F=Q=1`。

本节的级数收敛及无穷处归零针对固定 `N,E`；周期可能随 `N` 变小，不能据此宣称对所有层数或所有 owner 的一致对数估计。几何前提必须在实际声称的层数和轨道上成立，本节不生成矩阵、覆盖输入或机器证书。固定有限数据下对 `s` 全纯，也不意味着固定 `s` 的求值映射对形式拓扑连续。

## 3. 复域中其余正因子的统一下界

上一笔记指出复因子的模可能小于一；本节不再假设它们至少为一，而是证明对有限正集合足够的下界。

设

\[
D_E:=\sum_{g\in E_+}d_g.
\]

对 `g in E_+`，`1<=q_(N,g)<=d_g`，且 `|1-e^(-s ell_g/q_(N,g))|<2`，所以

\[
|F_{N,g}(s)|>2^{-q_{N,g}}\ge2^{-d_g},
\qquad
\left|\prod_{g\in E_+}F_{N,g}(s)\right|\ge2^{-D_E}.
\]

这对所有 `N>=1` 和 `s in Omega` 成立。正集合为空时，最后两侧均为一。故复相位不会使这个固定有限正乘积随 `N` 趋零。

固定非空紧集 `K subset Omega`，令 `a=min_K Re(s)>0`、`R=max_K|s|>0`。[零因子的已证模长下界][complex-note]给出

\[
\boxed{\inf_{s\in K}|Q_{N,E}(s)|
\ge2^{-D_E}\prod_{g\in E_0}
\left(\frac{N}{\ell_gR}\right)^N.}
\]

再记

\[
c_{E,K}:=\prod_{g\in E}(1-e^{-a\ell_g})>0,
\]

由 `|1-e^(-s ell_g)|>=1-e^(-a ell_g)` 得

\[
\boxed{\inf_{s\in K}\left|\frac{Q_{N,E}(s)}{B_E(s)}\right|
\ge c_{E,K}2^{-D_E}\prod_{g\in E_0}
\left(\frac{N}{\ell_gR}\right)^N.}
\]

若 `nu=|E_0|>=1`，令 `C=R max_(g in E_0)ell_g`。当 `N>=max(1,ceil(2C))` 时，第一下界至少为 `2^(nu N-D_E)`，第二下界再乘固定正数 `c_(E,K)`。所以两者在 `N -> infinity` 时均趋于正无穷，特别沿 `N=k!` 如此。

这已经落实前一笔记所缺的“其余因子乘积不趋零”条件，但仅针对本节明确的有限因子公式。常数依赖固定 `E,K`；不能从这里直接得到复参数下对增长集合的统一界。

## 4. 固定有限集合的三种结局

对有限正集合定义

\[
K_E=\max\bigl(\{1\}\cup\{d_g:g\in E_+\}\bigr),\qquad
A_E^+(s)=\prod_{g\in E_+}(1-e^{-s\ell_g/d_g})^{-d_g}.
\]

当 `k>=K_E` 时，所有正 owner 都有 `d_g|k!`，所以其有限乘积在任何求值之前就精确稳定；这是[既有阶乘稳定证明][formal-note]的有限域结论。

| 互斥条件 | 沿冻结 `N=k!` 的结论 |
| --- | --- |
| `E_0` 为空，且全部 `d_g=1` | 每个 `N` 就已满足 `Q_(N,E)=B_E`；空集合也在此列，两者为一 |
| `E_0` 为空，且至少一个 `d_g>=2` | `k>=K_E` 后精确等于 `A_E^+`；该函数不同于 `B_E` |
| `E_0` 非空 | `Q_(N,E)` 及 `Q_(N,E)/B_E` 的模在每个固定复紧集上一致趋于无穷 |

第二行的函数不等由正实轴直接证明。对 `x>0`、整数 `m>=2`，设 `t=e^(-x/m)`，则

\[
(1-t)^m<1-t<1-t^m,
\qquad (1-e^{-x/m})^{-m}>(1-e^{-x})^{-1}.
\]

因此对每个实数 `s>0`，高 content 因子严格大于基准，其余 content-one 因子相等，从而 `A_E^+(s)>B_E(s)`。这证明二者不是同一全纯函数，不声称每个复数点都不相等，也不声称任意复紧集上都有统一差距。

第二行的全整数序列还有明确的周期性质。令 `L=lcm{d_g:g in E_+}`，则

\[
Q_{N+L,E}=Q_{N,E},\qquad
N\equiv1\pmod L\Rightarrow Q_{N,E}=B_E,\qquad
L\mid N\Rightarrow Q_{N,E}=A_E^+.
\]

两个不同函数反复出现，所以全整数函数序列没有局部一致极限；每个正实点的数值序列也不收敛。某个固定复点处若全部周期值恰巧相同，则该点可以有极限，不能无证排除这种巧合。这个周期观察不授权用恢复基准的余数子列替换冻结阶乘序列。

特别是，“全部正 owner 都为 content one”只有同时排除零 owner，才是第一行的条件；不能用真空量词把含零集合误列为恢复分支。

## 5. 固定有限混合乘积的完整主项与误差

记

\[
\nu=|E_0|,\qquad
\Lambda_E=\sum_{g\in E_0}\ell_g,\qquad
P_E=\prod_{g\in E_0}\ell_g.
\]

零集合为空时取 `nu=Lambda_E=0`、`P_E=1`。对固定非空紧集 `K subset Omega`，令 `R=max_K|s|`、`M_g=ell_g R`，并设

\[
N_0=\max\!\left(1,
\left\lceil\max\bigl(\{0\}\cup\{M_g:g\in E_0\}\bigr)\right\rceil\right).
\]

这里把零纳入最大值，避免对空集取最大值。令 `N=k!`，同时要求

\[
k\ge K_E,\qquad N=k!\ge N_0.
\]

第一个门槛保证正因子精确稳定；第二个保证各零因子的复误差界有效。定义主项

\[
H_{N,E}(s)=A_E^+(s)e^{s\Lambda_E/2}
\frac{N^{\nu N}}{(s^\nu P_E)^N}.
\]

所有幂次都是整数，`s!=0`，故不选择复对数分支。这只是增长主项，不是新增归一化或新的恢复目标。

由上一笔记，零 owner 的相对因子

\[
W_{N,g}(s)=\frac{F_{N,g}(s)}{e^{s\ell_g/2}(N/(s\ell_g))^N}
\]

满足 `sup_K|W_(N,g)-1|<=exp(M_g^2/(6N))-1`。正部分已精确稳定，故

\[
\frac{Q_{N,E}(s)}{H_{N,E}(s)}=\prod_{g\in E_0}W_{N,g}(s).
\]

将有限乘积写成 `prod(1+(W_g-1))`，展开非空子集项并取模，得到

\[
\left|\prod_{g\in E_0}W_{N,g}-1\right|
\le\prod_{g\in E_0}(1+|W_{N,g}-1|)-1.
\]

因此

\[
\boxed{\sup_{s\in K}\left|\frac{Q_{k!,E}(s)}{H_{k!,E}(s)}-1\right|
\le\exp\!\left(\frac{\sum_{g\in E_0}M_g^2}{6k!}\right)-1
\longrightarrow0.}
\]

这保留每个 owner 的复相位。零集合为空时误差界为零，退化为纯正集合的精确稳定。集合和长度始终固定；该误差估计本身不适用于随 `k` 增长且未另控长度平方和的集合。

## 6. 正实轴上，扩大有限截断不能消除指定见证

本节有别于固定 `E` 的复域估计：利用正实轴的正性，下界可以对其他 owner 的数量与长度统一有效。每一项仍是已经定义的有限公式。

对实数 `s>0`，每个 `F_(N,g)>1`，且

\[
r_{N,g}(s):=\frac{F_{N,g}(s)}{(1-e^{-s\ell_g})^{-1}}\ge1.
\]

证明仍是第 4 节的不等式：正分支取 `m=q_(N,g)`，零分支取 `m=N`；`m=1` 时相等，`m>=2` 时严格。故其他有限因子或局部比值不能抵消指定 owner 的实轴下界。

### 6.1 保留一个零 owner：绝对值与相对基准均发散

固定[已有显式见证][owner-note] `g_zc=[[a_1,b_1]]`、`ell_z=ell(g_zc)>0`。对任何包含它的有限 `E`，

\[
Q_{N,E}(s)\ge F_{N,g_{\mathrm{zc}}}(s),\qquad
\frac{Q_{N,E}(s)}{B_E(s)}
\ge\frac{F_{N,g_{\mathrm{zc}}}(s)}{B_{\{g_{\mathrm{zc}}\}}(s)}.
\]

在固定正实紧区间 `I=[s_-,s_+] subset (0,infinity)` 上，[已证的实增长界][real-note]给出

\[
\inf_{s\in I}Q_{N,E}(s)
\ge\left(\frac{N}{s_+\ell_z}\right)^N,
\]

\[
\inf_{s\in I}\frac{Q_{N,E}(s)}{B_E(s)}
\ge(1-e^{-s_-\ell_z})\left(\frac{N}{s_+\ell_z}\right)^N.
\]

右侧与其他 owner 无关。因此对任何有限集合序列 `E_k`，只要最终都含同一个 `g_zc`，在冻结 `N_k=k!` 上，两项左侧均趋于正无穷。无需 `E_k` 单调、穷尽所有 owner 或来自某个规范枚举。相对结论比较每一项与其自身的 `B_(E_k)`，没有把变化的基准当成固定数。

### 6.2 保留一个 content-two owner：相对恢复有统一正差距

固定另一显式见证 `g_hc=[a_1^2[a_1,b_1]]`、`ell_h=ell(g_hc)>0`。若 `E_k` 最终包含它，取 `k_0` 使 `k>=k_0` 时 `g_hc in E_k`。以下不等式对所有 `k>=max(2,k_0)` 成立，此时 `q_(k!,g_hc)=2`。令 `t(s)=exp(-s ell_h/2)`，有

\[
\frac{Q_{k!,E_k}(s)}{B_{E_k}(s)}
\ge\frac{1-t(s)^2}{(1-t(s))^2}
=\frac{1+t(s)}{1-t(s)}.
\]

在同一个 `I` 上，`t(s)>=exp(-s_+ell_h/2)`，因此

\[
\boxed{\frac{Q_{k!,E_k}(s)}{B_{E_k}(s)}\ge1+\eta_I,\qquad
\eta_I=\frac{2e^{-s_+\ell_h/2}}{1-e^{-s_+\ell_h/2}}>0.}
\]

这里不要求包含零 owner；它排除相对比值趋于一，但不单凭此宣称比值发散。`eta_I` 是见证自身比值 `(1+t(s))/(1-t(s))` 在 `I` 上相对一的最小差距，于 `s=s_+` 取得；对整个有限乘积，它只提供统一下界，不宣称等号或最优性。

这些结论适用于字面有限因子及其基准乘积，不包括额外前因子、商、抵消或正则化。它们不定义无限乘积，也不认证任何穷尽序列。复域中模可能小于一，故不能把本节对增长集合的实轴统一界直接搬到复参数。

## 7. 本轮完成范围与仍然开放的边界

本轮已把有限层的类型、复对数分支、复模下界、阶乘分类、混合主项误差，以及实轴上对保留见证的有限截断族下界写成连续证明链。对全体数学 owner 的无正则化有限截断而言，只要满足本节明列的最终包含条件，扩大集合不能恢复被这两个见证排除的实轴比较；这不依赖先构造全 owner 乘积。

仍未完成的事项与上述结论不同：具体覆盖和机器 owner 认证、规范枚举或穷尽输入、全 owner 形式／标量对象、无限标量求值及其定义域、复域中增长集合的统一估计，以及任何全局行列式、迹公式或 Route 证明。没有交换两种极限，也没有把本轮的实轴有限截断下界称为 AN-1–AN-5 或 content-one 解析阶段的完成。

新增的有限几何全纯连接保留条件输入；原来只写实 H3 或尚未建立复连接的历史笔记保持当时原文，不回写为先前已证。正实有限 content-one 恒等也不能升级为全局恢复。论文、冻结方案、正式完整性 `FAIL / BLOCK`、Route 状态及 Stage 5／6 均不因本轮内部推导而改变。

## 8. 核对与保存范围

按 ARS 的论证流程，本轮将三个可并行的核心部分（有限模下界与分类、混合主项误差、几何全纯对数连接）分别推敲，再补核实轴有限截断族的统一下界。主线程整合并写出证明；同系助手的意见只作逻辑查错，不作为独立科学证据。新增推论由正文证明支持，没有新增外部来源或文献查询。

只新增此内部笔记，在上一笔记与总内部研究记录追加入口。文件检查使用只读 `node` 内联核对链接、关键量词与空集／门槛标记，以及编辑前长度和 SHA-256 所绑定的两个追加文件原文前缀与七个保护文件（R6、条件覆盖推导、显式 owner 笔记、形式产品笔记、正实增长笔记、Recovery3 状态及完成报告）的字节保全。此类检查不认证数学正确性。

没有运行科学实验、枚举、数值程序、既有审查脚本或论文构建；没有修改论文、文献库、代码、结果、锁或回执，也没有生成正式放行文件。

[complex-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_zero_content_complex_growth_20260908.md
[real-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_zero_content_scalar_growth_20260908.md
[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[formal-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_formal_product_limits_20260908.md
[finite-domains]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:764

## 追加进展：正 content 族与无限接口（2026-09-08）

后续[正 content 族的长度控制与穷尽障碍](internal_positive_content_exhaustion_obstruction_20260908.md)已把既有 `g_d` 族的物理长度控制为 `ell_d<=dA+C_0`，由此证明即使排除零 owner，最终保留每个固定族成员的有限截断仍在正实紧区间上绝对及相对发散，并排除相应全正对数的层数一致可求和 majorant。[伴随标量无限接口](internal_scalar_infinite_product_interfaces_20260908.md)区分实轴扩展值上确界与阶乘实序双极限、附加可求和前提下的全纯产品、增长有限集合的条件复域估计。以上是后续新证明，不回写为本笔记原来已完成的结果；实际枚举、复域全局结论及正式状态仍未获认证或改变。
