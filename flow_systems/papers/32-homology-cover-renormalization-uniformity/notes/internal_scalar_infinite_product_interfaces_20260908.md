# P32 内部研究：有限标量截断与无限对象的三类接口

记录日期：2026-09-08 UTC。接续[有限 owner 分类][finite-note]，与[正 content 族穷尽障碍][family-note]同轮完成。分别处理实轴扩展值乘积、附加可求和前提下的全纯乘积，以及增长有限集合的条件复域估计；这三种对象和结论不互相替代。

沿用规定局部因子与几何前提；本文不修改冻结归一化，不构造跨不同零 owner 的 Hahn 乘法，不宣告整个形式载体的连续标量求值，也不改变论文、正式审查或 Route 状态。

## 1. 实轴：无需枚举的扩展值乘积

固定 owner 集 `O`，每个 owner 有既定长度 `ell_g>0`，正／零分支分开规定。`O` 可以是全体 owner 或明确子集；本节不需要其可数性。用 `F_(N,g),Q_(N,E),B_E,R_(N,E)` 表示[前一笔记][family-note]定义的同一有限函数；仅在 `s>0` 上取值。

令 `F(O)` 为 `O` 的全部有限子集，按包含关系定向。因为每个 `F_(N,g)>1`、`B_g>1`、`r_(N,g)>=1`，三种有限乘积均随 `E` 不减。定义

\[
\mathcal Q_N(s)=\sup_{E\in\mathscr F(\mathcal O)}Q_{N,E}(s),\qquad
\mathcal B(s)=\sup_E B_E(s),\qquad
\mathcal R_N(s)=\sup_E R_{N,E}(s),
\]

取值域为 `[1,+infinity]`。这些是新明确的**扩展正实序对象**，并非已构造的有限复数 Euler 产品。

每个有限子集网在扩展实数的序拓扑中趋于相应上确界：若 `M` 小于上确界，可找到有限 `E_0` 使值大于 `M`，其后每个包含 `E_0` 的集合均保留该下界；有限上确界情形另有该上确界作为共同上界。这一证明不需要规范化算法、枚举顺序或有限值收敛的先验假设。

### 比值乘积不能擅自替换为两个无穷量的商

在 `[1,+infinity]` 的乘法中，始终有

\[
\boxed{\mathcal Q_N=\mathcal B\,\mathcal R_N.}
\]

有限层等式给出一个方向。另一个方向可分别选取逼近 `mathcal B`、`mathcal R_N` 的有限集合，再取并集，使两个下界同时成立。若任一个上确界无穷，相应有限层值可任意大，而另一项至少为一；故扩展值情形也成立，没有 `0 times infinity` 歧义。

只有在 `mathcal B<infinity` 时，才可进一步写

\[
\mathcal R_N=\mathcal Q_N/\mathcal B,
\]

此时 `infinity` 除以有限正数也有明确定义。若 `mathcal B=infinity`，必有 `mathcal Q_N=infinity`，但 `infinity/infinity` 不是这里的比值对象；`mathcal R_N` 仍由自己的有限乘积上确界定义。

一个仅关于正因子接口的反例是：取 `b_j=2`，分别令所有 `r_j=1`、仅 `r_1=2` 而其余为一、或所有 `r_j=2`。三种情形的两个原乘积均为无穷，比值乘积却分别为 `1,2,infinity`。这不是 P32 owner 数据或一次实验。

## 2. 冻结阶乘序列的两次实序极限与对角极限

对固定 `x>0`，函数

\[
\Phi_m(x)=(1-e^{-x/m})^{-m}
\]

随正整数 `m` 严格增加：若 `n>m`，则 `1/(1-e^{-x/n})>1/(1-e^{-x/m})>1`，先增大底数，再增大指数即可比较。正分支有

\[
\gcd(k!,d_g)\mid\gcd((k+1)!,d_g),
\]

零分支的整数指数则直接从 `k!` 增至 `(k+1)!`。所以 `F_(k!,g)` 与 `r_(k!,g)` 均随 `k` 不减。

对 `U_(k,E)=Q_(k!,E)` 或 `R_(k!,E)`，因此有双向单调性

\[
k'\ge k,\quad E'\supseteq E
\quad\Longrightarrow\quad U_{k',E'}(s)\ge U_{k,E}(s).
\]

所有以下极限均在 `[1,+infinity]` 中、对固定 `s>0` 理解：

\[
\boxed{
\lim_k\lim_E U_{k,E}
=\sup_k\sup_E U_{k,E}
=\sup_E\sup_k U_{k,E}
=\lim_E\lim_k U_{k,E}
=\sup_{k,E}U_{k,E}.}
\]

这是两重上确界的交换，允许共同值为无穷；不是有限值全纯收敛定理，也没有用它替代原稿的解析尾界或 AN-1–AN-5。

若有限集合序列 `E_k` 满足

\[
\forall g\in\mathcal O\ \exists k_g\ \forall k\ge k_g:
\quad g\in E_k,
\]

则 `U_(k,E_k)` 也趋于同一上确界，不要求 `E_k` 嵌套。证明：任意固定有限 `E_0` 的所有成员最终都在 `E_k` 中；再要求 `k>=k_0`，对角值便最终支配任意固定的 `U_(k_0,E_0)`。用上确界的定义逼近即可。没有这种最终包含条件时，一般不能声称任意有限对角序列穷尽这个上确界。

### 两种足以强迫共同值无穷的见证

- 若 `O` 含固定零 owner `z`，则[有限层实轴下界][finite-note]已使联合网、两次迭代极限与 `mathcal Q_(k!)`、`mathcal R_(k!)` 的层数极限均为无穷。对角序列只需最终保留 `z`，不必穷尽全体 `O`。
- 若 `O` 含[已有正 content 族][family-note]的所有 `g_d (d>=2)`，即使完全没有零 owner，同样结论仍成立；对角序列只需最终保留每个固定 `g_d`。伴随笔记给出正实紧区间上一致趋于无穷的具体量词与下界。

对第二种情形，**仅对每层上确界**还可选取移动见证 `d=N>=2`。因为 `g_N in O` 且 `gcd(N,N)=N`，对任意正实紧区间 `I`，

\[
\mathcal Q_N(s)\ge e^{c_I N},\qquad
\mathcal R_N(s)\ge e^{c_I(N-1)},\qquad s\in I,
\]

其中 `c_I>0` 来自伴随笔记。因此这两个扩展上确界甚至沿所有整数层数趋于无穷；但这不保证某个具体截断 `E_k` 包含移动的 `g_N`。全整数的 `gcd(N,d)` 可以振荡，上面的双向单调和一般两极限交换论证仍只按冻结阶乘序列使用。

层数极限为无穷不表示每个固定层的上确界都已经无穷；以上结论没有给出这种断言。

## 3. 附加绝对可求和条件下的有限值全纯产品

本节是另一类条件命题，**不声称实际 P32 owner 已满足它的求和前提**。

设 `J` 是可数索引集，固定 `T_g>0`、整数 `m_g>=1`。假设存在实数 `a>0` 使

\[
S_a:=\sum_{g\in J}m_g e^{-aT_g}<\infty.
\]

单周期全纯对数沿用[有限笔记的级数定义][finite-note]：

\[
L_T(s)=\sum_{r\ge1}\frac{e^{-rsT}}r,\qquad
L_E(s)=\sum_{g\in E}m_gL_{T_g}(s),\qquad Q_E(s)=e^{L_E(s)}.
\]

先证明周期具有正下界，而不把它暗中当作额外输入。集合 `J_1={g:T_g<=1}` 必须有限，因为其每个求和项至少为 `e^(-a)`。取

\[
t_0=\min\bigl(\{1\}\cup\{T_g:g\in J_1\}\bigr)>0,\qquad
c_a=1-e^{-at_0}>0.
\]

于是所有 `T_g>=t_0`，也覆盖空 `J` 或空 `J_1` 的情形。在闭半平面 `D_a={Re(s)>=a}` 上，

\[
\sum_g\sum_{r\ge1}\sup_{s\in D_a}
\left|m_g\frac{e^{-rsT_g}}r\right|
\le\sum_g\frac{m_g e^{-aT_g}}{1-e^{-aT_g}}
\le S_a/c_a<\infty.
\]

因此双级数绝对一致收敛，定义

\[
L(s)=\sum_gm_gL_{T_g}(s),\qquad Q(s)=e^{L(s)}.
\]

两者在 `Re(s)>a` 上全纯、在 `D_a` 上连续；`Q` 处处非零。令

\[
\varepsilon_E=\frac1{c_a}\sum_{g\notin E}m_g e^{-aT_g},
\qquad H_a=S_a/c_a.
\]

直接由绝对尾和与 `|e^z-1|<=e^{|z|}-1` 得

\[
\sup_{D_a}|L-L_E|\le\varepsilon_E,\qquad
\sup_{D_a}\left|Q/Q_E-1\right|\le e^{\varepsilon_E}-1,
\]

\[
\sup_{D_a}|Q-Q_E|\le e^{H_a}(e^{\varepsilon_E}-1),
\qquad e^{-H_a}\le|Q(s)|\le e^{H_a}.
\]

沿所有有限子集网，尾和趋于零，故产品一致收敛且与枚举顺序无关。一个具体截断序列若最终包含每个固定有限子集，也有相同结论；“每次都是有限集合”本身不够。这里给的是条件尾界公式，不是实际 owner 尾和的数值证书。

### 基底可求和条件向固定层的传递

本小节另令 `O` 可数，并假设

\[
S_0(a)=\sum_{g\in\mathcal O}e^{-a\ell_g}<\infty,\qquad a>0,
\]

同一有限短周期论证给出 `ell_0>0` 使所有 `ell_g>=ell_0`。固定层 `N`，令 `m_(N,g)` 依正／零分支取 `gcd(N,d_g)` 或 `N`，并令 `T_(N,g)=ell_g/m_(N,g)`。因为 `1<=m_(N,g)<=N`，

\[
\sum_gm_{N,g}e^{-NaT_{N,g}}
\le N\sum_ge^{-a\ell_g}<\infty.
\]

所以每个固定 `N` 的条件标量产品在 `Re(s)>Na` 上全纯，并在 `Re(s)>=Na` 上有一致有限截断极限。取 `c_0=1-e^{-a ell_0}>0`，还得到

\[
\sup_{\operatorname{Re}s\ge Na}|L_N-L_{N,E}|
\le\frac N{c_0}\sum_{g\notin E}e^{-a\ell_g}.
\]

相对产品尾界是该右侧的指数减一。这里没有从闭双曲曲面的名称推定 `S_0(a)` 已获证明或其尾和已可计算。

这些充分保证域随 `N` 向右移动。任意固定复数 `s` 在 `N` 足够大时不再属于它们，故本判据没有提供固定 `s` 的层数极限或共同域上的统一尾控制。这只是充分判据不再适用，不证明域外产品不存在，也不排除另行论证的延拓。

在本节产品确有定义的正实区域，它的有限截断极限与第 1 节相应有限扩展值一致；这并不把第 1 节其余可能无穷的值变成全纯函数。

## 4. 增长有限集合：复域需要实际控制其余因子的损失

固定非空紧集 `K subset Omega={Re(s)>0}`，记 `a=min_K Re(s)>0`、`R=max_K|s|>0`、`N=k!`。设每个 `E_k` 有限且最终包含同一个零 owner `z`。以下只在 `z in E_k` 的尾端使用。记 `m_(k,g)=m_(N,g)`。

对任何 owner 的三角不等式给出

\[
|F_{N,g}(s)|\ge
\exp\!\left[-m_{k,g}\log(1+e^{-a\ell_g/m_{k,g}})\right].
\]

把指定零见证以外的**所有正、零因子**计入损失：

\[
\mathcal L_k(K)=\sum_{g\in E_k\setminus\{z\}}
m_{k,g}\log(1+e^{-a\ell_g/m_{k,g}}).
\]

对指定见证使用[已有的零因子强下界][complex-note]，得到

\[
\boxed{\inf_K|Q_{N,E_k}|
\ge\left(\frac{N}{R\ell_z}\right)^N e^{-\mathcal L_k(K)}.}
\]

相对基准还需计入

\[
\mathcal P_k(K)=-\sum_{g\in E_k}\log(1-e^{-a\ell_g})\ge0,
\]

因为 `|1-e^(-s ell_g)|>=1-e^(-a ell_g)`，所以

\[
\boxed{\inf_K|R_{N,E_k}|
\ge\left(\frac{N}{R\ell_z}\right)^N
e^{-\mathcal L_k(K)-\mathcal P_k(K)}.}
\]

因此，`N log(N/(R ell_z))-mathcal L_k -> +infinity` 是绝对模长一致发散的充分条件；相对比值则将 `mathcal L_k` 换成 `mathcal L_k+mathcal P_k`。例如 `mathcal L_k+mathcal P_k=o(N log N)` 足以同时推出二者发散。它们不是必要条件，也尚未对任何实际 P32 截断族核实。

可用但较粗的界为

\[
\mathcal L_k\le(\log2)\left(
\sum_{g\in E_{k,+}}d_g+N|E_{k,0}\setminus\{z\}|\right).
\]

故不能遗漏其他零因子，也不能把固定集合时的基准常数自动视为增长集合下仍有正下界。

### 增长混合乘积的移动主项

不要求当层所有正 content 已稳定，直接保留当层精确正乘积

\[
A_k(s)=\prod_{g\in E_{k,+}}F_{N,g}(s).
\]

令 `nu_k=|E_(k,0)|`、`Lambda_k=sum_(E_(k,0))ell_g`、`P_k=prod_(E_(k,0))ell_g`，空零集合分别取 `0,0,1`。定义

\[
H_k(s)=A_k(s)e^{s\Lambda_k/2}
\frac{N^{\nu_kN}}{(s^{\nu_k}P_k)^N}.
\]

若 `sum_(g in E_(k,0))ell_g^2=o(N)`，则对每个固定 `K`，单因子误差所需的门槛 `R max_(E_(k,0))ell_g<=N` 最终成立（空集无门槛）。由[已证单零因子误差][complex-note]和有限乘积展开，

\[
\sup_K\left|Q_{N,E_k}/H_k-1\right|
\le\exp\!\left(\frac{R^2}{6N}
\sum_{g\in E_{k,0}}\ell_g^2\right)-1\longrightarrow0.
\]

这只是相对移动主项的渐近；没有声称 `H_k` 有固定极限，也没有改变归一化。若想把 `A_k` 写成使用全部 `d_g` 的稳定正形式，须另有每个当层 `d_g|k!`；`max_(E_(k,+))d_g<=k` 是充分而非必要条件。逐个固定 owner 的稳定不能替代这项当层条件。

## 5. 完成范围与验证

本轮完成的接口对应如下。

| 对象 | 本轮结论 | 未据此取得的结论 |
| --- | --- | --- |
| 正实扩展上确界，允许无穷 | 有限子集网、阶乘两次迭代次序与满足最终包含条件的对角极限；见证可使共同值无穷 | 有限值复全纯产品、实际规范枚举 |
| 假设加权指数尾和可求和的标量产品 | 新的非零全纯产品、明确一致尾界、顺序无关性 | 实际 P32 计数条件、固定参数下的层数统一控制 |
| 随层增长的有限复乘积 | 显式损失预算下的发散充分条件，长度平方和条件下的移动主项渐近 | 未受控截断族的复域发散、全局行列式或正则化 |

本轮只在内部笔记建立这些明列对象。ARS 的论证流程用于分开假设、推论及反例；同系助手分别检错，主线程整合，不作为独立科学证据。保全、链接及文档边界检查与[同轮主笔记][family-note]共用一次核对，不运行既有 artifact writer、实验、枚举或论文构建。原稿 AN-1–AN-5、冻结输入、来源状态、正式 `FAIL / BLOCK` 与 Stage 5／6 均保持不变。

[finite-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_finite_owner_scalar_classification_20260908.md
[family-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_positive_content_exhaustion_obstruction_20260908.md
[complex-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_zero_content_complex_growth_20260908.md

## 追加进展：求和前提的几何落实（2026-09-08）

后续[几何覆盖、长度计数与固定层产品](internal_geometric_tower_and_length_cutoff_20260908.md)已在固定真实闭双曲曲面上证明 `n(L)<=C_cnt e^L`，从而对每个 `a>1` 落实本笔记的基底求和前提并给出指数尾界；固定层乘积由此在 `Re(s)>N` 上构造并连接全部覆盖本原轨道的归零对数。数学长度截断的有限性与共尾性也已证明。该域仍随层数右移，不能替代固定参数的层数统一控制；本笔记保持当时条件命题原文，数值／规范枚举认证与正式状态不变。

## 追加进展：完整实轴对象的阈值与移动域（2026-09-08）

后续[未缩时覆盖乘积、精确阈值与移动参数主项](internal_unscaled_cover_products_and_moving_parameter_limit_20260908.md)利用指定外部素测地线定理证明：对完整数学 owner 集，`mathcal Q_N(s)` 在 `0<s<=N` 已为无穷、在 `s>N` 有限；`N>=2` 的 `mathcal R_N` 同样，而 `mathcal R_1` 始终为一。因此“层数发散不必意味着每一层无穷”仍是本笔记原接口层的逻辑限制，但实际完整几何对象的足够大固定层已另证无穷。新笔记还在移动参数 `s=Nw` 的共同 `Re(w)>1` 域证明带指数误差的零同调主项；它不是固定 `s` 的有限值延拓或原 AN 合同的完成。旧文保留，未改正式状态。

## 追加进展：两分支的临界接口（2026-09-08）

后续[零同调临界边界、正分支发散与对数偏移渐近](internal_homology_zero_critical_boundary_20260908.md)在固定零同调计数定理支持下，进一步证明：零分支绝对产品在且仅在 `s>=N` 有限，正分支在且仅在 `s>N` 有限；`N>=2` 的各相对分支分别具有同样有限值区域，`N=1` 全部相对分支恒为一。零分支相对产品由局部非负展开证明，不使用无穷相除。新结果同时区分零函数的有限边界值与局部非亚纯延拓障碍、正分支两极限不交换，以及纯零临界截断的日志精度／乘积相对精度。这里没有为本接口中其余无穷值赋予有限复值，也未改正式状态或补认规范枚举。
