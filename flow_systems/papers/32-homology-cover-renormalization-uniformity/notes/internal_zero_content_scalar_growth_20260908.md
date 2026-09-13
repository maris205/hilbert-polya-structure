# P32 内部研究：零 content 局部因子的显式标量增长界

记录日期：2026-09-08 UTC。接续[形式拓扑与有限标量求值笔记][topology-note]，本次直接分析已推导的单个零 content 局部因子，不从形式非柯西或求值不连续反推标量行为。仅新增内部理论记录，不修改论文、冻结归一化或正式审查状态。

本次结果：对固定零 content owner 的固定长度 `ell>0`，其明确实函数

\[
\Phi_N(s)=(1-e^{-s\ell/N})^{-N},\qquad s>0,
\]

沿整数 `N -> infinity` 趋于正无穷，特别沿冻结的 `N_k=k!` 如此；还可给出带显式相对误差的渐近

\[
\Phi_N(s)\sim e^{s\ell/2}\left(\frac{N}{s\ell}\right)^N.
\]

下文的一致估计只针对同一个 owner 的正实紧区间，不涉及全 owner 乘积、复数紧集或尾界。

## 1. 函数本身与几何解释分开绑定

固定[显式非真幂族笔记][owner-note]中的零 content owner

\[
g_{\mathrm{zc}}=[[a_1,b_1]],
\]

外层括号表示有向共轭类。此前的群论与测地线连接给出其在固定标记闭双曲曲面上的本原有向轨道，以及符号最小物理周期 `ell=ell(g_zc)>0`。本次不另选 owner，不改变度量，也不虚构数值长度或机器 owner 证书。

[条件覆盖推导][cover-note]已在 H1–H3 下给出零分支的 `h=1`、`c=N^4`、未缩放提升周期 `ell`；先令周期乘 `1/N`，再令有限乘积的对数乘 `1/N^3`，得到上述指数为 `N` 的局部因子。将它解释为实际覆盖因子，仍保留规定覆盖、物理时钟、最小周期绑定及本原有向提升逐条计数的前提。

对每个 `N`，它都可从当层的合法有限域得到：

\[
a_{N,g_{\mathrm{zc}}}=(1-z_{g_{\mathrm{zc}}}^{1/N})^{-N}
\in A^0_{g_{\mathrm{zc}},N},\qquad
\tau_{s,g_{\mathrm{zc}},N}(a_{N,g_{\mathrm{zc}}})=\Phi_N(s).
\]

各层的有限求值是[原有定义][zero-domain]，不同 `N` 的结果可直接在同一个实数空间中比较。不需要把 `tau` 延拓到整个 `H_(g_zc)`，也不交换任何形式极限与求值。

下面关于明确实函数的估计，只需 `ell>0`、`s>0` 及所列公式。若把全整数 `N` 的结论作几何解释，覆盖前提须在全部相应层数成立；若仅给出了阶乘层数的覆盖前提，几何解释就只限于该子序列。冻结的研究控制序列始终是 `N_k=k!`，证明更广的函数估计不表示更换控制序列。

比较基准仍是固定的局部因子

\[
B(s)=(1-e^{-s\ell})^{-1}\in(1,+\infty).
\]

## 2. 直接双边界与点态标量发散

**命题 1。** 对每个实数 `s>0` 和整数 `N>=1`，记 `x=s ell>0`，则

\[
\boxed{\left(\frac Nx\right)^N
<\Phi_N(s)
<e^x\left(\frac Nx\right)^N.}
\]

证明：对 `y>0`，积分恒等式与正实数序关系给出

\[
1-e^{-y}=\int_0^y e^{-t}\,dt,
\qquad ye^{-y}<1-e^{-y}<y.
\]

取倒数并升至正整数次幂 `N`，再代入 `y=x/N`，即得结论。所有量都为正，这里的大小关系不用于复数参数。

固定 `s` 后，当 `N>=max(1,ceil(2x))` 时，`N/x>=2`，所以

\[
\Phi_N(s)>2^N\longrightarrow+\infty.
\]

由 `B(s)` 是固定有限正数，更有

\[
\boxed{\Phi_N(s)\longrightarrow+\infty,\qquad
\frac{\Phi_N(s)}{B(s)}=(1-e^{-x})\Phi_N(s)\longrightarrow+\infty.}
\]

因此在相应几何前提成立的层数上，该局部因子不可能沿冻结阶乘序列趋于基准；这比已有的有限 `N>=2` 时严格大于基准更强。这里没有据此生成正式 owner mismatch、恢复或 Route 回执。

## 3. 增长比值的精确常数与显式误差

只为描述原因子的增长阶，定义诊断比值

\[
R_N(s):=\frac{\Phi_N(s)}{(N/(s\ell))^N}.
\]

分母不替代 `Phi_N`，不引入覆盖配方，也不是对冻结方案添加第三项归一化。

**命题 2。** 对所有 `x=s ell>0`、整数 `N>=1`，

\[
\boxed{e^{x/2-x^2/(24N)}\le R_N(s)\le e^{x/2},}
\]

并且

\[
\boxed{0\le1-e^{-x/2}R_N(s)
\le1-e^{-x^2/(24N)}\le\frac{x^2}{24N}.}
\]

证明：令 `t=x/(2N)>0`，利用

\[
1-e^{-x/N}=2e^{-t}\sinh t
\]

得到精确恒等式

\[
R_N(s)=e^{x/2}\left(\frac{\sinh t}{t}\right)^{-N}.
\]

为控制比值，不使用未写明余项的展开。对每个整数 `j>=0`，有

\[
(2j+1)!\ge6^j j!.
\]

`j=0` 时等号成立。若该式对 `j` 成立，由

\[
(2j+3)(2j+2)-6(j+1)=4j(j+1)\ge0
\]

即可递推到 `j+1`。对绝对收敛的正项级数逐项比较，得到

\[
1\le\frac{\sinh t}{t}
=\sum_{j\ge0}\frac{t^{2j}}{(2j+1)!}
\le\sum_{j\ge0}\frac{(t^2/6)^j}{j!}
=e^{t^2/6}.
\]

取负整数幂 `-N`，再乘 `e^(x/2)`，且 `N t^2/6=x^2/(24N)`，即得第一组界。第二组界来自 `1-e^(-a)<=a` 对 `a>=0` 成立，可同样由积分表示看出。

由此得出带明确常数的渐近：

\[
R_N(s)\longrightarrow e^{s\ell/2},\qquad
\frac{\Phi_N(s)}{e^{s\ell/2}(N/(s\ell))^N}\longrightarrow1.
\]

不能把它简写为 `Phi_N(s) ~ (N/(s ell))^N`，因为遗漏的比值极限 `e^(s ell/2)` 一般不为 `1`。沿冻结阶乘序列，准确写法为

\[
\Phi_{k!}(s)\sim e^{s\ell/2}
\left(\frac{k!}{s\ell}\right)^{k!},
\qquad
0\le1-\frac{\Phi_{k!}(s)}{e^{s\ell/2}(k!/(s\ell))^{k!}}
\le\frac{(s\ell)^2}{24k!}.
\]

## 4. 固定 owner 的正实紧区间一致界

取固定正实紧区间 `K=[s_-,s_+]`，其中 `0<s_-<=s_+<infinity`。令

\[
m=\ell s_->0,\qquad M=\ell s_+<\infty.
\]

由第 2 节逐点下界，

\[
\inf_{s\in K}\Phi_N(s)\ge\left(\frac NM\right)^N\longrightarrow+\infty,
\]

\[
\inf_{s\in K}\frac{\Phi_N(s)}{B(s)}
\ge(1-e^{-m})\left(\frac NM\right)^N\longrightarrow+\infty.
\]

这里“一致趋于正无穷”指：对每个 `L>0`，存在依赖 `K,ell,L` 的 `N_0`，使所有 `N>=N_0` 和所有 `s in K` 的相应函数值均大于 `L`。这不是收敛到通常实数或复数空间中的某个有限值。

第 3 节还给出增长比值的一致误差。相对误差与绝对误差分别为

\[
\sup_{s\in K}|e^{-s\ell/2}R_N(s)-1|
\le\frac{M^2}{24N},
\]

\[
\sup_{s\in K}|R_N(s)-e^{s\ell/2}|
\le e^{M/2}\frac{M^2}{24N}.
\]

这些界对所有 `N>=1` 成立；将 `N` 替换为 `k!` 即得原控制序列的界。`ell` 始终属于同一个 owner，不能把这些阈值或误差常数声称为全 owner 一致有效。

## 5. 有限正实乘积只在明列条件下继承下界

若另行给定一个明确的有限正实乘积

\[
Q_N(s)=\Phi_N(s)\prod_{j\in J}C_{N,j}(s),
\qquad J\text{ 有限},\qquad C_{N,j}(s)\ge1,
\]

则直接有 `Q_N(s)>=Phi_N(s)`。因而在这些条件成立的固定 `s` 或整个 `K` 上，分别继承第 2、4 节的下界和发散结论。

这只是有限个正实数相乘的序关系，没有构造项目的跨零 owner 形式乘积或全 owner 标量对象，也不为 `C_(N,j)` 指定未经证明的几何来源。含有额外前因子、商、抵消、正则化或解析延拓的表示，不得自动套用这个下界。

## 6. 相对既有笔记的新增范围

| 论证 | 对象与结论 | 不能互相代替的部分 |
| --- | --- | --- |
| 既有 Hahn 计算 | 同标签形式序列 `a_(k!,g_zc)` 非柯西 | 不单凭此推出标量发散 |
| 上轮连续性反例 | `n!u^n`、固定根阶的 `n!z^(n/N)` 排除连续全域求值延拓 | 检验序列不是本次的实际局部因子序列 |
| 本次直接估计 | 明确的 `Phi_N(s)` 在正实域发散，并有显式增长比值及紧区间误差 | 不建立全 owner 产品、复域界或解析尾估计 |

上轮的“本次未证明标量产品发散”保留其当时范围；这次另用直接实函数证明新增单 owner 的局部标量发散，不回写历史状态。没有建立数值长度、矩阵模型、覆盖输入认证或冻结枚举，也没有把数学推导包装成实验观察。

本次不启动 content-one 解析阶段、AN-1–AN-5、Route 评估或 Stage 5／6。正实紧区间上的单 owner 估计不涉及 owner 求和、尾界或极限交换；正式完整性 `FAIL / BLOCK` 不变。

## 7. 核对与保存范围

按 ARS 的论证流程，分开记录函数定义与几何前提、粗界与发散、精确比值与误差、单 owner 一致量词，以及有限正实乘积的条件推论。三个只读推敲任务分别检查直接增长界、精确误差、几何与阶段范围；主线程整合并写出证明。同系助手意见只用于逻辑查错，不作为独立科学证据。新增推论由正文证明支持，没有新增外部定理或来源查询。

只新增此内部笔记，在上一笔记及总内部记录追加入口。文件级检查使用只读 `node` 内联核对：链接、关键条件，以及编辑前长度／SHA-256 所绑定的两个追加文件原文前缀和七个保护文件（R6、形式产品笔记、辅助记录笔记、显式 owner 笔记、条件覆盖推导、Recovery3 状态及完成报告）的字节保全。文件检查不是数学正确性认证。

没有运行科学实验、枚举、数值程序、既有审查脚本或论文构建；未修改论文、文献库、代码、结果、锁或回执。

[topology-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_scalar_topology_bridge_obstruction_20260908.md
[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[cover-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_conditional_cover_factor_derivation_20260907.md
[zero-domain]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round6.tex:778

## 后续内部推导入口（2026-09-08）

后续见[零 content 有限因子的复求值与紧集增长](internal_zero_content_complex_growth_20260908.md)：将同一个有限形式因子的合法求值放在复数右半平面，证明紧集上的模长发散与保留复相位的统一相对渐近，证明不选复对数分支。该结果不自动建立几何复对数归一化，也不能照搬本笔记的正实有限乘积序下界；旧文和正式审查状态不变。
