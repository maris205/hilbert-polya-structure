# P32 内部研究：正 content 见证族的长度控制与穷尽障碍

记录日期：2026-09-08 UTC。接续[有限 owner 标量分类][finite-note]。本轮不再只用一个 content-two 见证，而是使用[已有非真幂族][owner-note]的全部正 content 成员，补上物理长度上界，证明即使完全排除零同调 owner，保留该族的有限截断仍在正实轴发散。

这是规定局部因子和覆盖前提下的内部定理，不是新的归一化、实际枚举运行或正式 Route 结论。论文、冻结方案、历史审查与 `FAIL / BLOCK` 不变。

## 1. 输入、函数与本轮命题

固定既有带标记闭双曲亏格二曲面及单位速度测地流。[既有证明][owner-note]给出

\[
g_d=a_1^d[a_1,b_1],\qquad d\ge1,
\]

为互异的有向非真幂共轭类，其同调为 `(d,0,0,0)`，对应本原有向轨道，最小周期记作 `ell_d>0`。本轮使用 `d>=2` 的族；不把 word length 当成物理长度，也不把这个显式族当成全 owner 枚举。

沿用[条件覆盖推导][cover-note]的 H0–H3；几何解释要求它们对所声称的 owner 和层数成立。对任意有限 owner 集合 `E`，定义

\[
m_{N,g}=\begin{cases}
\gcd(N,d_g),&g\in\mathcal O_+,\\
N,&g\in\mathcal O_0,
\end{cases}
\qquad
F_{N,g}(s)=(1-e^{-s\ell_g/m_{N,g}})^{-m_{N,g}},
\]

\[
Q_{N,E}(s)=\prod_{g\in E}F_{N,g}(s),\quad
B_E(s)=\prod_{g\in E}(1-e^{-s\ell_g})^{-1},\quad
R_{N,E}(s)=Q_{N,E}(s)/B_E(s).
\]

空积为一，本文始终在实数 `s>0` 上使用这些有限值。冻结层数为 `N_k=k!`。前一笔记已经证明所有 `F_(N,g)>1`，所有局部相对比值 `r_(N,g)=F_(N,g)/B_{g}>=1`。

本轮的主要量词是：`E_k` 每次有限，且对每个固定整数 `d>=2`，存在 `k_d` 使得所有 `k>=k_d` 都有 `g_d in E_k`。下称**最终保留该族**。它不要求 `E_k` 嵌套，不要求包含零 owner，也不要求已证明穷尽全体 owner；仅仅每个成员出现过一次则不够。

## 2. 基点环路给出物理长度的线性上界

在固定曲面上选同一个基点 `p`，以分段光滑环路 `alpha,beta` 分别代表标记生成元 `a_1,b_1`。记它们的固定长度为

\[
A=\operatorname{len}(\alpha)>0,\qquad
B=\operatorname{len}(\beta)>0.
\]

不要求这两个带基点环路本身是闭测地线。把

\[
\alpha^d\alpha\beta\alpha^{-1}\beta^{-1}
\]

按路径连接起来，得到 `g_d` 的带基点代表，其长度为

\[
(d+2)A+2B=dA+C_0,\qquad C_0=2A+2B.
\]

下面直接证明该长度确实控制 `ell_d`，不把“测地线代表存在”省略成长度比较。取 `p` 的一个提升 `x in H^2`，上述路径提升后从 `x` 走到 `g_d x`（相反的 deck 标记约定只会换成逆元，不影响长度）。已有闭测地线代表的提升给出 `g_d` 的一条不变测地轴；若先得到共轭元的轴，按该共轭变换拉回即可。取轴上点 `y`，有

\[
\operatorname{dist}(y,g_d^n y)=n\ell_d,\qquad n\ge1.
\]

这里用到双曲平面中的完整测地线按弧长全局最短，以及 deck 作用等距。三角不等式给出

\[
n\ell_d-2\operatorname{dist}(x,y)
\le\operatorname{dist}(x,g_d^n x)
\le n\operatorname{dist}(x,g_d x).
\]

除以 `n` 并令 `n -> infinity`，再用提升路径长度不变，得到

\[
\boxed{0<\ell_d\le\operatorname{dist}(x,g_d x)
\le dA+C_0.}
\]

因此，取一个方便但不追求最优的固定常数

\[
C=A+C_0=3A+2B>0,
\qquad \ell_d/d\le C\quad(d\ge1).
\]

这些长度与常数属于同一个固定度量和同一组固定环路。没有给出数值，也不声称它们跨所有度量统一。证明没有假设 `ell_d` 等于连接词的长度，没有使用曲面群中一般元素的 translation length 次可加性，更没有使用原始自由词长度 `d+4` 作为物理长度。

## 3. 高 content 因子的族统一实轴下界

固定正实紧区间

\[
I=[s_-,s_+]\subset(0,\infty),\qquad
\rho_I=1-e^{-s_+C}\in(0,1),\quad
c_I=-\log\rho_I>0.
\]

对每个固定 `d>=2`，当 `k>=d` 时，`d|k!`，故 `m_(k!,g_d)=d`。记 `t=exp(-s ell_d/d)`；第 2 节给出 `t>=exp(-s_+ C)`，从而 `1-t<=rho_I`。于是

\[
\boxed{F_{k!,g_d}(s)=(1-t)^{-d}
\ge\rho_I^{-d}=e^{c_I d},\qquad s\in I.}
\]

对同一个 owner 的基准，相对比值满足

\[
r_{k!,g_d}(s)=\frac{1-t^d}{(1-t)^d}
\ge\frac{1-t}{(1-t)^d}
=(1-t)^{-(d-1)}
\ge\rho_I^{-(d-1)}=e^{c_I(d-1)}.
\]

这里 `0<t<1`、`d>=2`，所以 `1-t^d>=1-t`。尤其，控制相对比值不需要再证明 `ell_d` 的下界，也不需要预先知道整个基准乘积是否收敛。

## 4. 正分支本身的有限截断发散定理

设有限 `E_k` 最终保留第 1 节的族。任取实数阈值 `M>0`，先选定一个整数 `d>=2`，使 `exp(c_I(d-1))>M`，再令

\[
k\ge\max(d,k_d).
\]

此时这个固定的 `g_d` 已在 `E_k` 内且自身 content 已稳定。其他有限因子及局部比值均至少为一，所以对所有 `s in I`，

\[
Q_{k!,E_k}(s)\ge e^{c_I d}>M,\qquad
R_{k!,E_k}(s)\ge e^{c_I(d-1)}>M.
\]

因此

\[
\boxed{\inf_{s\in I}Q_{k!,E_k}(s)\longrightarrow+\infty,
\qquad
\inf_{s\in I}R_{k!,E_k}(s)\longrightarrow+\infty.}
\]

这已经适用于 `E_k subset O_+` 的纯正集合；加入任何其他 owner 也不能减小这两个实轴量。它加强了前一笔记的固定 content-two 正差距：这里借助一个 content 无界且 `ell_d/d` 有统一上界的族，得到发散，而不仅是不等于基准。

量词的次序不可替换：先选一个固定 `d`，再等待它被保留且 `k>=d`。不从逐个最终稳定推出当层 `E_k` 的所有正 content 都已经整除 `k!`，也不假设移动见证 `g_k` 或 `g_(k!)` 必在当层集合中。

### 可按实际包含关系表达的更强下界

若 `k>=D>=2` 且 `E_k` 包含 `g_2,...,g_D`，不同 `d` 的 owner 互异，因而可以相乘：

\[
\inf_I Q_{k!,E_k}\ge
\exp\!\left(c_I\left(\frac{D(D+1)}2-1\right)\right),
\qquad
\inf_I R_{k!,E_k}\ge
\exp\!\left(c_I\frac{D(D-1)}2\right).
\]

对任意最终保留该族的 `E_k`，可定义只用于陈述下界的整数

\[
h_k=\max\Bigl(\{1\}\cup
\{D:2\le D\le k,\ \{g_2,\ldots,g_D\}\subset E_k\}\Bigr).
\]

固定 `D` 时取所有 `k_2,...,k_D` 的有限最大值，即证 `h_k -> infinity`。上面两个界对 `D=h_k` 成立，`h_k=1` 时按空积得到一。这不是修改截断计划或自适应选择保留哪些 owner；`h_k` 只是既有集合包含进度的数学读数。本轮没有计算任何规范前缀的 `h_k`，故不给出 `k` 的已认证数值收敛速度。

## 5. 稳定正乘积与统一对数控制的直接后果

### 5.1 形式极限的普通正实截断求值不有限

[既有形式正乘积][formal-note]沿阶乘序列有一个形式极限；其固定有限正集合的标量代表为

\[
A_E^+(s)=\prod_{g\in E}(1-e^{-s\ell_g/d_g})^{-d_g}.
\]

第 3–4 节的同样下界对 `A_E^+` 及 `A_E^+/B_E` 成立，不再需要 `k` 的门槛。因此，对包含整个 `g_d (d>=2)` 族的正 owner 集，在所有有限子集按包含关系增长的网中，稳定乘积的上述两个正实截断量均趋于正无穷；任何最终保留该族的有限截断序列也如此。

这不是宣告形式极限不存在。它说明：不能以这些字面有限截断的通常实数极限，给该形式极限赋一个有限标量值。它不排除另行定义的正则化或其他不保留该截断极限的赋值；本轮没有引入这些新对象。

### 5.2 全正分支不存在这类层数一致的可求和对数 majorant

固定任意 `s_0>0`。假设非负数 `M_g(s_0)` 对整个正 owner 集满足

\[
\log F_{k!,g}(s_0)\le M_g(s_0)\quad(\forall k\ge1),
\qquad\sum_{g\in\mathcal O_+}M_g(s_0)<\infty.
\]

取 `I={s_0}`（或包含它的紧区间），对每个 `d>=2` 再取 `k>=d`，则

\[
M_{g_d}(s_0)\ge c_I d.
\]

由于这些 owner 互异，`sum_(d>=2)c_I d=+infinity`，产生矛盾。即使只要求上述控制对所有 `k>=k_*` 成立，仍可取 `k>=max(k_*,d)`，结论不变。对 `log r_(k!,g)` 同样得到 `(d-1)c_I` 的矛盾。

这是特定非负局部对数、全正 owner 集与冻结阶乘层数下的不可求和结论。它不排除别的重组／抵消型估计，不涉及 content-one 子集的可求和性，也不把原稿的 AN-1–AN-5 状态改成已验证或已执行。本轮没有重写那些解析义务。

## 6. 与无限对象的关系和完成边界

伴随笔记[标量无限乘积接口][interface-note]进一步区分：实轴扩展值上确界、有限子集的两种迭代次序、附带绝对可求和假设的全纯产品，以及增长集合的条件复域下界。这里的族发散提供前两者的一个明确无穷结局，但不自动满足后两者的条件。

本轮完成的证明链为：已有非真幂及物理周期绑定 → 同基点代表环路的长度上界 → 已规定正因子的族统一下界 → 保留该族的任意有限截断实轴发散 → 稳定正乘积普通求值与统一对数 majorant 的障碍。

实际覆盖输入、矩阵与数值长度认证、一般 owner 规范化、规范枚举的包含证书、固定层无限乘积的实际计数尾界、复域全局控制、行列式或迹公式仍未完成。由于其他复因子的模可能小于一，本笔记的正实结论不能直接推广到任意复紧集。固定有限集合的稳定定理与本轮增长集合的发散定理不矛盾。

## 7. 来源、检错与保存范围

本轮按 ARS 的论证流程分别检查长度控制、量词、实序极限与复域条件，再由主线程整合写入。同系助手只参与逻辑检错，不是独立科学认证。群论族及本原测地线对应复用所链接内部证明及其当时保留的来源边界；新增长度不等式的证明完整写在第 2 节，不以一个书目链接代替证明。

为尝试补核既有一般几何来源，本轮只向公开网页发送书名／一般定理查询和公共 URL，没有上传稿件或笔记。旧 Pisa 书稿入口获取超时；作者书目页可读，但只支持书目身份；两个尝试的 PDF 地址未能打开，作者书目页链接的 Utah 入口返回 403 后未继续该访问路径。因此未取得新的命题原文，不记为来源复核通过，也不据此修改旧来源记录。[可读的作者书目页](https://www.math.uchicago.edu/~farb/books.html)只用于记录这次访问的身份线索，不承担本轮定理支持。

新增此笔记及伴随接口笔记，在前一有限层笔记和总内部记录各追加入口。只读文件检查核对链接、必要量词／边界、原文前缀与九个指定保护文件的字节保全；这些是文档保全检查，不是数学证明认证。工作目录的 `git status --short` 返回“非 Git 仓库”，本轮不用 Git 差异作为验证依据。未运行科学实验、数值长度、owner 枚举、既有审查脚本或论文构建，未改论文、代码、结果、锁或正式回执。

检查尝试记录：首个内联检查提交因检查代码中反引号嵌套，在命令执行前发生 JavaScript 语法错误；修正该表达式后，首次实际 Node 检查在关键字断言 `最终包含` 上退出，因为此篇正文使用的是“最终保留该族”，并在后文明确量词次序。两次失败均是本轮临时文档检查自身的问题，没有产生文件写入或修改数学输入。随后将断言对应到正文实际的量词段落并重跑同一只读检查；不删除前两次失败，也不把文档通过记为科学认证。

[finite-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_finite_owner_scalar_classification_20260908.md
[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[formal-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_formal_product_limits_20260908.md
[interface-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_scalar_infinite_product_interfaces_20260908.md

## 追加进展：几何覆盖与长度截断（2026-09-08）

后续[几何同调覆盖塔、长度截断与固定层乘积](internal_geometric_tower_and_length_cutoff_20260908.md)已从同一个真实标记双曲曲面构造 H1 的抽象覆盖塔，证明物理长度截断有限、共尾，并把本笔记的正族发散接到任意趋向无穷的几何长度阈值。该后续证明还给出轨道计数上界、指数尾和与固定层 `Re(s)>N` 上的无限几何乘积连接；不回写本笔记原来的证据状态，不认证数值输入或规范枚举，也不改变正式审查结论。
