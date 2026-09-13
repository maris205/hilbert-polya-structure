# P32 内部研究：有限标量求值的形式拓扑不连续性与延拓障碍

记录日期：2026-09-08 UTC。接续[辅助分量记录与连续读出笔记][record-note]，检查形式空间与通常复数标量之间的连续性桥梁。只新增内部理论记录，不修改 R6、原有映射定义、冻结方案或正式审查状态。

本次证明：有限域采用从既有形式空间继承的拓扑时，非空正 owner 域的 `sigma` 和固定零 owner／固定模数域的 `tau` 在零处不连续；因此不能连续延拓到相应整个形式空间。此外，通常标量空间也不能通过一个在零处连续的映射，精确恢复整个有限域的形式元素。后一个方向另有独立反例，不是前一个方向的自动推论。

这些结论限制的是明确拓扑与精确相容条件下的映射，不是数值 Euler 产品的发散定理。下文的检验序列不是覆盖归一化因子；其中的 `n!` 只是系数，不改变原控制序列 `N_k=k!`。

## 1. 定义域、目标拓扑与量词

沿用 [R6 的正形式空间][carrier]及其有限代数：

\[
R_+=\varprojlim_{(E,D)}
\mathbb Q[u_g:g\in E]/\mathfrak m_E^{D+1},
\qquad \mathfrak m_E=(u_g:g\in E),
\]

\[
A_F=\mathbb Q[u_g:g\in F]
[(1-u_g^r)^{-1}:g\in F,\ r\in\mathbb N],
\qquad j_F:A_F\hookrightarrow R_+.
\]

`E,F` 为有限正 content owner 集，`D>=0`；各有限坐标离散。`j_F` 是既有形式嵌入。本笔记明确给 `A_F` 赋予由 `j_F` 拉回的子空间拓扑。R6 没有另行给有限代数指定拓扑；这里是在已有嵌入下选择继承拓扑来检查连续性，不把该约定默认为所有标量模型的拓扑。

对[零分支][zero-domain]，固定同一个 `g in O_0` 和同一个整数 `N>=1`，使用

\[
A^0_{g,N}=\mathbb Q[z_g^{1/N}]
[(1-z_g^{1/N})^{-1},(1-z_g)^{-1}]\subset H_g.
\]

这里 `H_g` 的系数为有理数，指数为非负有理数、支撑良序，取赋值零邻域 `U_r={h:v_g(h)>r}`。非零元素的赋值是最小支撑指数，`v_g(0)=+infinity`；`A^0_(g,N)` 使用该包含映射诱导的子空间拓扑。没有改变 owner 标签或根阶。

始终给目标 `C` 赋予通常复数拓扑。每次先固定一个复数 `s` 满足 `Re(s)>0`，并保留固定符号长度 `ell(g)>0`。原有有限求值为

\[
\sigma_{s,F}(u_g)=e^{-s\ell(g)/d(g)},\quad d(g)\geq1;
\qquad
\tau_{s,g,N}(z_g^{1/N})=e^{-s\ell(g)/N}.
\]

所有规定分母的像均非零，故它们仍是良定义的有限代数映射。[R6 的形式相容引理][compatibility]对过渡映射与 `pi_g` 声明连续，对有限标量映射只声明良定义；本次结果不与该原文冲突。

## 2. 正 content：非空有限域中的反例

**命题 1。** 固定非空有限 `F subset O_+` 和 `Re(s)>0`。上述 `sigma_(s,F)` 在 `A_F` 的继承形式拓扑下不连续于零。

证明：选定一个 `g in F`，记

\[
t=e^{-s\ell(g)/d(g)},\qquad
\rho=|t|=e^{-\operatorname{Re}(s)\ell(g)/d(g)}\in(0,1).
\]

取合法多项式检验序列

\[
h_n=n!u_g^n\in\mathbb Q[u_g]\subset A_F,\qquad n\geq1.
\]

对每个固定坐标 `(E,D)`，若 `g notin E`，`j_F(h_n)` 的该坐标恒为零；若 `g in E`，则一旦 `n>D`，次数截断使该坐标为零。系数多大都不影响这个精确截断。因此

\[
j_F(h_n)\longrightarrow0\quad\text{于 }R_+,
\qquad h_n\longrightarrow0\quad\text{于 }A_F.
\]

但标量模满足

\[
|\sigma_{s,F}(h_n)|=n!\rho^n,\qquad
\frac{(n+1)!\rho^{n+1}}{n!\rho^n}=(n+1)\rho.
\]

`rho` 是固定正数，所以该比值最终至少为 `2`，从而模趋于无穷，特别是不趋于 `sigma_(s,F)(0)=0`。这与零处连续的必要条件矛盾。

这对每个固定 `s` 都成立；增长阈值允许依赖 `s,ell(g),d(g)`，不声称一个对整个半平面统一有效的阈值。证明只需 `d(g)>=1`，同样适用于 content-one owner，不是高 content 特有的算术现象。

**空集例外。** `F=emptyset` 时，`A_F=Q` 的继承拓扑是离散拓扑：常数项坐标 `p_(emptyset,0)` 可以区分各有理常数。因此该有限求值 `Q_discrete -> C` 连续，不能把空集纳入命题 1。

## 3. 零 content：固定模数已经足以破坏连续性

**命题 2。** 固定 `g in O_0`、整数 `N>=1` 和 `Re(s)>0`。上述 `tau_(s,g,N)` 在 `A^0_(g,N)` 的继承赋值拓扑下不连续于零。

证明：取

\[
w_n=n!z_g^{n/N}\in\mathbb Q[z_g^{1/N}]\subset A^0_{g,N}.
\]

每项只有一个支撑指数，且 `n!` 是非零有理数，所以

\[
v_g(w_n)=n/N\longrightarrow+\infty,
\qquad w_n\longrightarrow0\quad\text{于 }H_g
\text{ 及 }A^0_{g,N}.
\]

另一方面，令固定正数 `c=Re(s)ell(g)/N`，则

\[
|\tau_{s,g,N}(w_n)|=n!e^{-cn},\qquad
\frac{(n+1)!e^{-c(n+1)}}{n!e^{-cn}}=(n+1)e^{-c}.
\]

比值最终至少为 `2`，所以模趋于无穷，不趋于 `tau_(s,g,N)(0)=0`。因此不连续。

整个证明固定同一个 `N`，没有随 `n` 改变有限域或增加根阶；`n` 是检验序号，`n!` 是系数。赋值只测量支撑指数，不控制有理系数在通常绝对值下的大小。它与上一笔记中模数变化的 `a_(k!,g)` 是不同序列。

## 4. 连续延拓不可能，且无需代数性假设

**推论 3。** 对命题 1 中的非空 `F`，不存在在零处连续的映射

\[
S:R_+\longrightarrow\mathbb C,
\qquad S\circ j_F=\sigma_{s,F}\quad\text{在整个 }A_F\text{ 上}.
\]

对命题 2 中的固定 `g,N`，不存在在零处连续的映射

\[
T:H_g\longrightarrow\mathbb C,
\qquad T|_{A^0_{g,N}}=\tau_{s,g,N}.
\]

证明：相容等式包含零元素，故 `S(0)=T(0)=0`。分别对第 2、3 节的形式零收敛序列应用零处连续性，就要求其精确标量像趋于零，与计算矛盾。

没有要求 `S,T` 线性、保乘法或单射。完整有限域上的相容是此处明列的要求；不把反例推广成对一切更小定义域的否定。此证明也不判定非连续代数延拓或一般集合映射延拓是否存在。

正向的空集例外确实可延拓：

\[
R_+\xrightarrow{\ p_{\varnothing,0}\ }\mathbb Q_{\mathrm{discrete}}
\hookrightarrow\mathbb C
\]

是连续映射，其在常数子代数上的限制就是 `sigma_(s,emptyset)`。

## 5. 反向精确读出：有理常数给出另一个障碍

**命题 4。** 不存在在零处连续的 `J:C -> R_+`，满足 `J(0)=0` 且对全部整数 `n>=1` 都有 `J(1/n)=(1/n)1_(R_+)`。也不存在满足相应常数等式、在零处连续的 `L:C -> H_g`。

证明：通常复数拓扑下 `1/n -> 0`。若第一种读出存在，连续性将使形式常数 `(1/n)1_(R_+) -> 0`。但它们经离散常数项坐标 `p_(emptyset,0)` 仍为非零数 `1/n`，并不最终等于零，矛盾。第二种读出同理：`v_g(1/n)=0` 对所有 `n` 成立，形式常数不进入零邻域 `U_0={h:v_g(h)>0}`，故不能趋于零。

因此，要求在整个有限域上精确恢复的连续读出尤其不存在：

\[
J\bigl(\sigma_{s,F}(a)\bigr)=j_F(a)\quad(\forall a\in A_F),
\qquad
L\bigl(\tau_{s,g,N}(a)\bigr)=a\quad(\forall a\in A^0_{g,N})
\]

均会强制满足上述有理常数等式。此反向结论连 `F=emptyset` 也成立；它不与空集有限求值的正向连续性矛盾，两个方向使用的定义域拓扑不同。

这是独立于第 2–4 节的证明；正向不连续本身不自动证明逆向不连续。完整有限域只是充分条件，实际反例只需精确保留 `{0,1/n:n>=1}`。这里没有证明集合论逆或非连续逆存在，也不要求先假设有限求值单射。

## 6. 对项目桥梁的含义与反例边界

| 方向 | 明列条件下的结论 | 不应扩大成 |
| --- | --- | --- |
| 形式空间 → 通常复数 | 与指定非平凡有限求值域全部相容的连续延拓不存在 | 非连续求值也不存在；任何标量 Euler 产品都发散 |
| 通常复数 → 形式空间 | 连 `{0,1/n}` 都精确保留的零处连续读出不存在 | 任何只对某个特殊因子序列规定取值的读出都不存在 |
| 候选 `X` → 固定形式分量 | 上一笔记的精确、连续读出仍可传递其特定序列的极限障碍 | 不经证明就把通常标量求值视为这种读出 |

映射不连续不表示所有序列都破坏收敛。例如去掉阶乘系数后，`u_g^n` 与固定 `N` 的 `z_g^(n/N)` 均形式趋零，且其有限标量像也趋零。

原项目的有限因子还有更直接的特例：对固定有限 `F`，令

\[
A^+_{k,F}=\prod_{g\in F}
(1-u_g^{d(g)/\gcd(k!,d(g))})^{-\gcd(k!,d(g))}
\quad\in A_F.
\]

由[已证的阶乘稳定公式][limit-note]，一旦 `k>=max({1} union {d(g):g in F})`，该有限代数元素就精确等于 `prod_(g in F)(1-u_g)^(-d(g))`。所以其有限求值也最终精确稳定；这只用相等保持，不需要 `sigma` 在整个有限域连续。它不提供对所有 `F` 统一的阈值，也没有对 `mathcal P_*^+ in R_+` 使用未定义的全域求值。

上一笔记的读出命题以形式坐标或 `H_g` 为目标，并要求一个固定映射在候选极限点处连续。这里既不否定那些形式投影，也未排除所有仅针对特殊因子序列的读出。形式不收敛不能自动推出其某个标量像不收敛；不同方向和不同定义域的映射不得互换。

若进一步分析真实标量因子序列，仍需指定实际函数、有效定义域及相应估计；本次未启动 content-one 解析阶段、全 owner 标量产品、AN-1–AN-5 或新的拓扑方案。改变系数控制、拓扑或相容要求属于另一个命题，不能静默替换冻结定义。几何覆盖、最小物理周期和因子约定仍以[条件覆盖推导][cover-note]及其后续 owner 绑定为前提。

## 7. 核对与保存范围

按 ARS 的论证流程，将有限代数合法性、所选继承拓扑、两个正向反例、延拓推论、独立反向反例和特定序列例外分开陈述。三个只读推敲任务分别检查正分支、零分支、原稿措辞与方向边界；主线程整合并写出证明。同系助手意见仅作逻辑查错，不作为独立科学证据。本次无新增外部定理或文献查询。

只新增此内部笔记，在上一笔记与总内部记录追加入口。文件级核对使用只读 `node` 内联检查，验证链接与条件标记，并以编辑前长度和 SHA-256 核对两个追加文件的原文字节前缀，以及 R6、形式产品笔记、显式 owner 笔记、条件覆盖推导、Recovery3 状态和完成报告六个保护文件的不变性。此类检查不认证数学正确性。

没有运行科学实验、枚举、数值程序、既有审查脚本或论文构建；没有修改论文、文献库、代码、结果、锁或回执。正式完整性 `FAIL / BLOCK` 不变，没有启动 Route 评估或 Stage 5／6。

[record-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_componentwise_recovery_obstruction_20260908.md
[limit-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_formal_product_limits_20260908.md
[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[carrier]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:720
[zero-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:778
[compatibility]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:796

## 后续内部推导入口（2026-09-08）

后续见[零 content 局部因子的显式标量增长界](internal_zero_content_scalar_growth_20260908.md)：直接从已给出的单 owner 实函数证明其沿模数增长趋于正无穷，并给出含 `exp(s ell/2)` 的精确渐近及正实紧区间上的显式误差。本项不是从本笔记的拓扑检验序列推出，也不增加冻结归一化或全 owner 产品结论；原文和正式状态保持不变。
