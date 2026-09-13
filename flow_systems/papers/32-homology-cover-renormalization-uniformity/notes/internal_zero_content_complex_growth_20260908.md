# P32 内部研究：零 content 有限因子的复求值与紧集增长

记录日期：2026-09-08 UTC。接续[正实局部标量增长笔记][real-note]，本次研究同一个零 content 有限形式因子在复数右半平面的求值。新增结论是紧集上的模长发散和保留复相位的统一渐近；不修改冻结归一化、论文或正式审查状态。

## 1. 复求值对象与几何解释的边界

仍固定[显式 owner 笔记][owner-note]中的 `g_zc=[[a_1,b_1]]` 及其固定符号最小周期 `ell>0`。令

\[
\Omega=\{s\in\mathbb C:\operatorname{Re}s>0\},\qquad
\Phi_N(s)=(1-e^{-s\ell/N})^{-N},\quad N\in\mathbb N.
\]

这是[原有有限域映射][zero-domain]的明确复求值：

\[
\Phi_N(s)=\tau_{s,g_{\mathrm{zc}},N}
\bigl((1-z_{g_{\mathrm{zc}}}^{1/N})^{-N}\bigr),
\qquad s\in\Omega.
\]

因为 `|exp(-s ell/N)|<1`，分母非零，所以每个 `Phi_N` 在 `Omega` 上全纯且无零点。外部幂次为整数；形式生成元的像由指数公式指定，不是任取复数的 `N` 次根。这里没有全域 `H_g -> C` 求值，也没有形式极限与标量求值的交换。

其正实轴限制与[条件覆盖推导][cover-note]中的实归一化公式一致。但该推导的 H3 使用正实 `s` 和实对数；本笔记只分析既有有限形式因子的复求值，不另宣称已经建立原始几何乘积在整个半平面上的复对数归一化。不能把高次原始乘积的 principal Log 默认为相容的分量对数和。

原来的覆盖、最小周期绑定、有向本原提升计数及两项归一化前提仍保留；本次不补造覆盖或 owner 输入认证。冻结控制序列为 `N_k=k!`。公式的全整数估计自动适用于该子序列，不表示改选控制序列或补全所有层数的几何前提。

基准仍取其合法有限复求值

\[
B(s)=(1-e^{-s\ell})^{-1},\qquad s\in\Omega,
\]

它在 `Omega` 上有限且非零。

## 2. 无需渐近展开的模长下界

**命题 1。** 对每个 `s in Omega` 和整数 `N>=1`，

\[
\boxed{|\Phi_N(s)|>\left(\frac{N}{\ell|s|}\right)^N.}
\]

证明：令 `w=s ell/N`，则 `Re(w)>0`，且

\[
1-e^{-w}=w\int_0^1 e^{-tw}\,dt.
\]

由三角不等式和实函数积分，

\[
|1-e^{-w}|
\le |w|\int_0^1 e^{-t\operatorname{Re}w}\,dt
<|w|.
\]

最后一步因为 `Re(w)>0`，被积函数在 `t>0` 时严格小于一。取倒数并升至整数次幂 `N`，即得结论。这里只比较模长，没有使用复数大小序或复对数。

现在固定非空紧集 `K subset Omega`，定义

\[
M=\ell\max_{s\in K}|s|\in(0,\infty),\qquad
\alpha=\ell\min_{s\in K}\operatorname{Re}s>0.
\]

由逐点下界及反三角不等式，

\[
\inf_{s\in K}|\Phi_N(s)|
\ge\left(\frac NM\right)^N\longrightarrow+\infty,
\]

\[
|1-e^{-s\ell}|\ge1-e^{-\ell\operatorname{Re}s}\ge1-e^{-\alpha},
\]

从而

\[
\boxed{\inf_{s\in K}\left|\frac{\Phi_N(s)}{B(s)}\right|
\ge(1-e^{-\alpha})\left(\frac NM\right)^N
\longrightarrow+\infty.}
\]

例如整数 `N>=max(1,ceil(2M))` 后，`(N/M)^N>=2^N`。这给出同一个 owner 在每个固定复紧集上的模长一致趋于无穷：对每个 `L>0`，所有充分大的 `N` 和所有 `s in K` 的相应模长均大于 `L`。阈值可以依赖 `K,ell,L`。

因此对任意固定 `s in Omega`，序列没有有限复数极限，也不趋于基准 `B(s)`；沿 `N=k!` 同样成立。相位可以变化，复值本身不写成实数意义的“趋于正无穷”。这不是对所有 owner、无界参数区域或全 owner 产品的一致结论。

## 3. 不选复对数分支的相对误差估计

对固定非空 `K subset Omega`，沿用上面的 `M`。诊断相对比值定义为

\[
W_N(s):=\frac{\Phi_N(s)}{e^{s\ell/2}(N/(s\ell))^N}
=e^{-s\ell/2}\left(\frac{s\ell}{N}\right)^N\Phi_N(s).
\]

`s ell!=0`，所有幂次都是整数，故该定义没有分支选择。此比值只描述原因子的增长，不替代 `Phi_N`，也不向覆盖配方增加新的归一化。

**命题 2。** 当整数 `N>=N_0=max(1,ceil(M))` 时，

\[
\boxed{\sup_{s\in K}|W_N(s)-1|
\le\exp\!\left(\frac{M^2}{6N}\right)-1.}
\]

证明：令 `x=s ell`、`t=x/(2N)`，并定义整函数

\[
S(t)=\frac{\sinh t}{t},\quad S(0)=1.
\]

由 `1-e^(-x/N)=2e^(-t)sinh(t)`，直接得到

\[
W_N(s)=S(t)^{-N}.
\]

这里的恒等式来自指数运算和整数幂，不需要对复值函数取对数。由于 `N>=M`，有 `|t|<=1/2`。令 `delta=S(t)-1`；利用[上一笔记已证明的系数不等式][real-note] `(2j+1)!>=6^j j!`，可对绝对收敛级数取模并比较：

\[
|\delta|
\le\sum_{j\ge1}\frac{|t|^{2j}}{(2j+1)!}
\le e^{|t|^2/6}-1
\le e^b-1,
\qquad b=\frac{M^2}{24N^2}\le\frac1{24}.
\]

对 `0<=b<1`，由指数级数与几何级数比较，`e^b-1<=b/(1-b)`，故

\[
r:=|\delta|\le e^b-1\le\frac b{1-b}\le2b
=\frac{M^2}{12N^2}\le\frac1{12}.
\]

特别是 `|delta|<1`。将 `N` 个绝对收敛的几何级数相乘并去掉常数项，得到

\[
|W_N(s)-1|
=|(1+\delta)^{-N}-1|
\le\sum_{j\ge1}\binom{N+j-1}{j}r^j
=(1-r)^{-N}-1.
\]

剩下只需实数不等式：对 `0<=r<=1/2`，

\[
-\log(1-r)=\int_0^r\frac{du}{1-u}\le2r.
\]

这里的 `log` 是正实数 `1-r` 的实对数，不是复对数。因此

\[
|W_N(s)-1|
\le e^{2Nr}-1
\le\exp\!\left(\frac{M^2}{6N}\right)-1.
\]

右侧不依赖 `s in K`，命题得证。

指数误差界不能直接缩成 `M^2/(6N)`。若希望显式显示倒数阶，由 `e^a-1<=a e^a` 及 `N>=M` 可进一步写为

\[
\sup_{s\in K}|W_N(s)-1|
\le\frac{e^{M/6}}6\frac{M^2}{N}\longrightarrow0.
\]

## 4. 复数渐近与相位保留

命题 2 的含义是局部一致的相对渐近：

\[
\boxed{\Phi_N(s)\sim e^{s\ell/2}
\left(\frac{N}{s\ell}\right)^N
\quad\text{于每个固定非空紧集 }K\subset\Omega.}
\]

这里的 `sim` 指上一节的复相对比值 `W_N` 一致趋于一；主项保留 `s` 的复相位，没有把它替换为 `|s|`。以下误差界仍要求 `N>=N_0`。增长比值的绝对误差可写为

\[
\sup_{s\in K}\left|
\left(\frac{s\ell}{N}\right)^N\Phi_N(s)-e^{s\ell/2}\right|
\le e^{M/2}\left(e^{M^2/(6N)}-1\right).
\]

对模长，由 `||W_N|-1|<=|W_N-1|` 得

\[
\sup_{s\in K}\left|
\frac{|\Phi_N(s)|}
{e^{\ell\operatorname{Re}s/2}(N/(\ell|s|))^N}-1
\right|
\le e^{M^2/(6N)}-1.
\]

这与第 2 节不借助渐近得到的下界相容。沿冻结序列只需令 `N=k!`；当 `k!>=N_0` 时，相对误差界为 `exp(M^2/(6k!))-1`。没有另选模数序列。

## 5. 正实乘积下界不能自动搬到复参数

上一笔记的有限乘积推论要求其余因子在正实参数下至少为一。复参数时，这个前提不能自动替换成“其余因子的模至少为一”。例如对任意 `T>0`，取

\[
s=\frac{\log 2+i\pi}{T}\in\Omega,
\qquad e^{-sT}=-\frac12,
\]

则一个普通倒数 Euler 因子已经满足

\[
|(1-e^{-sT})^{-1}|=\frac23<1.
\]

这只是说明复参数下不存在所需的自动序下界，不是在项目中指定一个新 owner、周期或控制点。单凭某个有限乘积含有 `Phi_N`，不能直接宣称其模大于等于 `|Phi_N|`。

若另有已定义表示 `Q_N(s)=Phi_N(s)G_N(s)`，并另外证明 `inf_(s in K)|G_N(s)|>=c_K>0` 对所有充分大的 `N` 一致成立，才可用 `|Q_N|>=c_K|Phi_N|` 传递发散。仅知每个 `N` 下 `G_N` 非零并不够；本次没有为项目的其余因子乘积提供这个一致下界，也没有构造全 owner 产品。

## 6. 核对与保存范围

按 ARS 的论证流程，将合法有限复求值、直接模长下界、无复对数分支的误差证明、相位解释及乘积传递的缺失条件分开记录。三个只读推敲任务分别检查模长与基准下界、统一相对误差、H3 与复乘积的范围边界；主线程整合并写出证明。同系助手意见只作逻辑查错，不作为独立科学证据。本次没有新增外部定理或文献查询。

本次是同一个 owner 的有限求值函数估计，不处理 owner 求和、枚举共尾性、尾项或极限交换；不启动 content-one 解析阶段、AN-1–AN-5、Route 评估或 Stage 5／6。未认证复对数几何归一化、具体覆盖模型或机器 owner 数据，正式完整性 `FAIL / BLOCK` 不变。

只新增此内部笔记，在上一笔记及总内部记录追加入口。文件级检查使用只读 `node` 内联核对链接、关键条件，以及编辑前长度和 SHA-256 所绑定的两个追加文件原文前缀与六个保护文件（R6、标量拓扑笔记、显式 owner 笔记、条件覆盖推导、Recovery3 状态及完成报告）的字节保全。这些检查不认证数学正确性。

首轮文件检查因分数的 LaTeX 字面标记不匹配而退出：正文为 `\frac23<1`，检查器误按带花括号的写法匹配。修正检查表达式后重新核对；未因此改写数学公式或任何锁定材料。

没有运行科学实验、枚举、数值程序、既有审查脚本或论文构建；未修改论文、文献库、代码、结果、锁或回执。

[real-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_zero_content_scalar_growth_20260908.md
[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[zero-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:778

## 后续内部整合入口（2026-09-08）

后续见[有限 owner 标量层的复对数连接与分类](internal_finite_owner_scalar_classification_20260908.md)：新增条件有限几何乘积的归零全纯对数连接，落实其余有限正因子的复模下界，完成固定有限集合的三分分类与混合渐近；另在正实轴证明对保留指定见证的任意有限截断族统一有效的下界。未构造全 owner 乘积或迁移冻结协议，本笔记的历史范围和正式状态原样保留。
