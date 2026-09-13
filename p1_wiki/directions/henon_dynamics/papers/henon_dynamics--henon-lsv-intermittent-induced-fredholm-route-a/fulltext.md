---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lsv-intermittent-induced-fredholm-route-a"
canonical_tex: "henon_dynamics/henon_lsv_intermittent_induced_fredholm_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lsv_intermittent_induced_fredholm_route_a/paper/main.pdf"
source_sha256: "1b9331dcc0b7ba3b33d420f462b45489c508e5b83e523076a3238e8e0f81fc2a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Alpha-One Intermittency: Complete Periodic Coding and Exact First Returns

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lsv_intermittent_induced_fredholm_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lsv_intermittent_induced_fredholm_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lsv_intermittent_induced_fredholm_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lsv_intermittent_induced_fredholm_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We fix the alpha-one intermittent map with its partition endpoint assigned to the left branch. Every binary periodic word then gives exactly one based periodic point, so the fixed-point count is $2^n$ at every iterate. The all-zero orbit is neutral; every other periodic orbit is expanding. The first return to $(1/2,1]$ has an explicit countable family of inverse branches, including all literal interval endpoints. An exact reciprocal recurrence gives the unnormalized Lebesgue return tail $1/(4n)$ and the corresponding infinite mean under normalized Lebesgue measure on the base. Nonneutral primitive cycles correspond bijectively to induced cycles, preserving the total multiplier and original time. This first version closes coding, boundary conventions, and exact inducing; it makes no stationary-density claim at the alpha-one endpoint. We carry an exact first-return construction for alpha-one intermittency into one fixed complex disk. All countably many inverse return branches map that disk into a common strictly interior disk, and a reciprocal-growth identity gives uniformly summable quadratic derivative decay. A direct Hardy-basis rank-one expansion proves trace-class convergence for every original-time parameter in the closed unit disk. The induced Fredholm determinant is entire in the return-count parameter and has a derivative-weighted primitive product with both clocks recorded explicitly. Its trace denominator accounts for all repetitions, while the neutral fixed point remains outside the induced hyperbolic ledger. The defining branch series fails beyond the unit disk, which is not a claim of a natural boundary. The construction is an explicit source-system proof, with classical intermittency and inducing credited to their literature. We close a single-domain inducing construction for the alpha-one intermittent map. Exact binary coding gives the all-period census, and a fixed endpoint convention gives every first-return branch and the sharp Lebesgue tail. The induced branches share an explicit complex disk and have quadratic derivative decay, yielding a trace-class Hardy operator throughout the closed original-clock disk. Its Fredholm determinant has an exact primitive product that distinguishes the number of returns from elapsed original iterations. On the original Lebesgue $L^1$ space, the Perron operator is noncompact; localized differences near the neutral point make one an approximate eigenvalue on the zero-integral subspace. Every power of the restricted operator has norm exactly one, excluding uniform exponential relaxation there. This does not exclude regularized determinants on other specified spaces. The package combines these analytic boundaries with independently reconstructible finite receipts. No new discovery of classical intermittency is claimed, and no arithmetic Route-A conclusion follows from the source induced determinant.
author:
- 'HCS-C381 theorem and reproducibility package'
date: 5 September 2026
title:
- |
  Alpha-One Intermittency:\
  Complete Periodic Coding and Exact First Returns
- |
  Alpha-One Intermittency:\
  A Common Complex Domain and Induced Fredholm Product
- |
  Alpha-One Intermittency:\
  Nuclear Inducing, Two Clocks, and the Uninduced $L^1$ Obstruction
```

## Markdown 正文

=3em

中文摘要

本文固定一阶间歇映射，并把分割端点明确归入左支。 每个二进制周期字都对应唯一的有基点周期轨道，因此任意迭代的固定点数精确等于二的相应幂。 全零轨道为中性，其余周期轨道至少经过一次右支并具有严格扩张的总乘子。 对右半区间的首次返回具有可显式写出的可数逆分支，半开半闭端点约定保证这些分支确实构成返回划分。 由左逆迭代的倒数递推得到未归一化勒贝格返回尾的尖锐系数四分之一， 基区间归一化后的返回时间均值因此发散。 每条非中性本原轨道与诱导本原轨道一一对应，总乘子不变，原始时间等于各次返回时间之和。 本轮封闭完整编码、端点和首次返回，不把参考勒贝格分布的结论扩张为尚未证明的平稳密度定理。 本文把一阶间歇映射的精确首次返回提升到一个固定复圆盘。 全部可数逆返回分支均把该圆盘送入同一严格内含圆盘；倒数增长与导数望远镜乘积给出统一的二次衰减。 在固定哈代空间的单项式基中直接构造秩一展开，从而证明原始时间参数闭单位圆盘内的迹类收敛。 诱导弗雷德霍姆行列式对返回次数参数为整函数，并在初始收敛域具有精确的本原轨道乘积。 乘积同时记录返回次数与原始迭代次数，稳定性分母保留全部重复轨道的贡献。 中性固定点从诱导扩张轨道中单独分离，不能把其单位乘子塞入通常的平迹分母。 定义所用分支级数在单位圆盘外失败，但这不被误称为禁止一切解析延拓的自然边界。 本文给出可审查的源系统证明，并保留经典间歇性与诱导方法的文献归属。 本文在固定端点和固定复域下贯通一阶间歇映射的完整诱导结构。 二进制编码给出全周期固定点计数，精确逆分支给出首次返回和尖锐勒贝格尾界。 所有诱导分支共享严格内含复圆盘，导数统一二次衰减，故原始时钟参数闭单位圆盘内存在迹类哈代算子。 同一算子的弗雷德霍姆行列式具有保留稳定性分母的本原乘积，其中返回次数与原始迭代次数明确分开。 回到原始勒贝格一阶可积空间，佩龙算子并不紧；中性点附近的局部密度差在零积分子空间产生近似本征值一， 由望远镜估计进一步证明该子空间上每次幂的算子范数恰为一，排除一致指数松弛。 这一结论不被迁移到未定义的各向异性或解析空间，也不否认其他空间上的正则化行列式。 包内进展是轨道、复域、双时钟行列式和未诱导障碍的统一证明与有限审查， 没有把经典间歇性重述为新发现，也没有把源行列式提升为算术目标结果。

**Keywords:** intermittent map; periodic coding; neutral fixed point; first return; endpoint convention; return tail

关键词：间歇映射；周期编码；中性固定点；首次返回；端点约定；返回尾 **Keywords:** inducing; complex domain; Hardy space; trace class; Fredholm determinant; primitive orbit product

关键词：诱导；复域；哈代空间；迹类；弗雷德霍姆行列式；本原轨道乘积 **Keywords:** intermittency; nuclear inducing; two clocks; neutral obstruction; approximate eigenvalue; Route A

关键词：间歇性；核诱导；双时钟；中性障碍；近似本征值；路线甲

# A fixed endpoint and the complete periodic census

Fix $$T(x)=\begin{cases}x+2x^2,&0\le x\le1/2,\\2x-1,&1/2<x\le1.\end{cases}
\qquad
g(z)=\frac{\sqrt{1+8z}-1}{4},\quad h(z)=\frac{1+z}{2}.
\label{eq:map}$$ The endpoint $1/2$ belongs to the left branch, so $T(1/2)=1$. Its assignment changes a countable boundary orbit set relative to the other common convention and will matter for literal return intervals. The complex square root is chosen with positive real part on $\operatorname{Re}z>0$. The neutral point is zero. Original time counts one application of $T$.

For every integer $n\ge1$, $T^n$ has exactly $2^n$ fixed points. Binary length-$n$ words give a bijection with these based points. The number of primitive cycles of period $n$ is $$P_n=\frac1n\sum_{d\mid n}\mu(d)2^{n/d}.
\label{eq:necklaces}$$ Here $\mu$ is the Möbius function. Only the all-zero orbit is neutral. Every other periodic orbit has positive multiplier at least two. Least word period and least orbit period coincide.

On $[0,1]$, the maps $g,h$ are increasing, $0<g'\le1$, and $h'=1/2$. Any inverse composition containing $h$ is a contraction with Lipschitz constant at most $1/2$, so it has exactly one fixed point. The all-$g$ composition has only zero because $g(x)<x$ for positive $x$; the all-$h$ composition has fixed point one.

Before reading forward itineraries, exclude boundary ambiguity. If an intermediate point of a mixed inverse cycle were zero, the inverse step producing it would be $g$ with zero input. Iterating this implication around the cycle forces every branch to be $g$. If it were one, the step would be $h$ with input one, forcing the all-$h$ cycle. Thus mixed cycles avoid zero and one. They also avoid $1/2$, which can arise only as $g(1)$ or $h(0)$. Their forward itineraries are therefore unambiguous and agree with the prescribed branch composition. Two different based words cannot produce the same point because the deterministic forward orbit has only one itinerary. Conversely every fixed point solves the equation for its inverse word. This proves the complete count and identifies least periods.

Möbius inversion of the primitive-power decomposition gives [\[eq:necklaces\]](#eq:necklaces){reference-type="eqref" reference="eq:necklaces"}. Every nonzero periodic word visits the right branch, where $T'=2$, while each left derivative is $1+4x\ge1$. Multiplying these positive derivatives gives the multiplier statement. Under $a$ repetitions, the period is multiplied by $a$ and the multiplier becomes $\Lambda^a$.

Each branch preserves orientation. No time-reversal symmetry is declared for this noninvertible interval map.

# Every first-return branch and the sharp tail

Set $Y=(1/2,1]$, let $\tau$ be the first positive return time to $Y$, and write $R=T^\tau$. Define $$h_n(z)=\frac{1+g^{n-1}(z)}2\quad(n\ge1),\qquad
a_m=g^m(1/2)\quad(m\ge0).
\label{eq:branches}$$

Every point of $Y$ has a finite first return, and $$\{y\in Y:\tau(y)=n\}=h_n(Y),\qquad R\circ h_n=\mathrm{id}_Y.
\label{eq:return}$$ These left-open, right-closed intervals partition $Y$. For $n\ge1$, $$\operatorname{Leb}\{y\in Y:\tau(y)>n\}=\frac{a_{n-1}}2\sim\frac1{4n}.
\label{eq:tail}$$ Under normalized Lebesgue measure on $Y$, the tail is asymptotic to $1/(2n)$ and its mean is infinite.

After a point of $Y$ takes the right branch it is positive. While it remains in $(0,1/2]$, the left branch increases it strictly. If it never escaped, it would converge to a positive fixed point of $x+2x^2$, which is impossible. The inverse of a return of length $n$ first reverses $n-1$ left steps and then one right step, giving [\[eq:branches\]](#eq:branches){reference-type="eqref" reference="eq:branches"}. The preceding inverse left iterates lie in $(0,1/2]$, which proves the first-return assertion. Moreover $g(1)=1/2$ gives $h_{n+1}(1)=h_n(1/2)$. The left-branch assignment at $1/2$ makes the shared upper endpoints return on the claimed iterate. These adjacent intervals exhaust $Y$ as their left endpoints tend to $1/2$.

Their endpoints give the exact tail in [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}; for $n=1$ it is $(1/2,3/4]$, of length $1/4$. The recurrence $a_{m-1}=a_m+2a_m^2$ gives $$\frac1{a_m}-\frac1{a_{m-1}}=\frac2{1+2a_m},\qquad
\frac1{2m+2}\le a_m\le\frac1{m+2}.
\label{eq:reciprocal}$$ The increment lies between one and two. Using the upper bound in $2/(1+2a_m)=2-4a_m/(1+2a_m)$ and summing yields $a_m^{-1}=2m+O(\log(m+2))$. Therefore $a_m=(2m)^{-1}+O(\log m/m^2)$ and [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} follows. Normalization doubles the tail, and the harmonic-series comparison gives the infinite mean. This is a reference-Lebesgue statement; no stationary induced density has been assumed.

Nonneutral primitive $T$ cycles correspond bijectively to primitive $R$ cycles. If an induced cycle has return period $r_p$, return times $n_1,\ldots,n_{r_p}$, and total multiplier $\Lambda_p$, its original period is $N_p=\sum_j n_j$ and its multiplier remains $\Lambda_p$.

Every nonneutral periodic word contains a right symbol and hence visits $Y$. Successive gaps between such visits determine the induced itinerary. Conversely [\[eq:branches\]](#eq:branches){reference-type="eqref" reference="eq:branches"} reconstructs the original cycle. Changing the chosen visit rotates the induced word. Thus no additional multiplicity equal to the number of returns is introduced. A smaller original or induced period would force a smaller period on the other side.

The unweighted zeta and its neutral-point removal are consequently $$Z_T(z)=\frac1{1-2z},\qquad
Z_{T,\mathrm{nonneutral}}(z)=\frac{1-z}{1-2z},\qquad |z|<1/2.
\label{eq:unweighted}$$ Indeed the first is the exponential series of the exact fixed counts; the second removes the single primitive fixed point. The elementary renewal identity $1-\sum_{n\ge1}z^n=(1-2z)/(1-z)$ is consistent with the same original clock. These statements concern unweighted counting.

\>0

# One complex disk for countably many branches

Fix once and for all $$\Omega=\{z:|z-1|<3/4\},\qquad
e_k(z)=\left(\frac{z-1}{3/4}\right)^k\quad(k\ge0),
\label{eq:domain}$$ where the $e_k$ are the normalized monomial basis of $H^2(\Omega)$. The notation $D(c,r)$ denotes the open disk of center $c$ and radius $r$.

Every $h_n$ is holomorphic on a neighborhood of $\overline\Omega$ and $$h_n(\Omega)\subset D(1,1/2)\Subset\Omega,\qquad
\sup_\Omega|h_n'|\le1/2.
\label{eq:range}$$ For $w_m=g^m(z)$, uniformly on $\Omega$, $$|w_m|\le\frac1{4/7+2m/25}\le\frac{25}{2(m+1)}.
\label{eq:complexgrowth}$$

If $\operatorname{Re}z>0$, then $\operatorname{Re}\sqrt{1+8z}>1$, so $w=g(z)$ lies in the right half-plane. The identity $z=w(1+2w)$ yields $$\frac1w=\frac1z+\frac2{1+2w}.
\label{eq:complexreciprocal}$$ The added term has positive real part. The disk $D(1,1)$ is exactly the set of nonzero $z$ with $\operatorname{Re}(1/z)>1/2$; hence $g$ preserves it. Starting from $\Omega$, every $w_m$ stays in that disk. For $n\ge2$ this gives $|h_n(z)-1|<1/2$, while for $n=1$ the bound is $3/8$. The closed initial disk stays inside the right half-plane, where all iterated branches are holomorphic. The estimate $|g'|=|1+8z|^{-1/2}\le1$ there gives the derivative bound in [\[eq:range\]](#eq:range){reference-type="eqref" reference="eq:range"}; convexity also gives a Lipschitz constant $1/2$ on the closed disk.

For $w\in D(1,1)$, $|w|\le2$ and $\operatorname{Re}w>0$. Thus $\operatorname{Re}(2/(1+2w))\ge2/25$. The initial disk has $\operatorname{Re}(1/z)\ge4/7$. Iteration of [\[eq:complexreciprocal\]](#eq:complexreciprocal){reference-type="eqref" reference="eq:complexreciprocal"} proves [\[eq:complexgrowth\]](#eq:complexgrowth){reference-type="eqref" reference="eq:complexgrowth"}.

An explicit uniform constant is $$C_*=1250\exp(625\pi^2/6),\qquad
\sup_\Omega|h_n'|\le\frac{C_*}{n^2}\quad(n\ge1).
\label{eq:derivativebound}$$

Differentiate $w_{k-1}=w_k(1+2w_k)$ and telescope to obtain $$\begin{aligned}
(g^m)'(z)
&=\left(\frac{w_m}{z}\right)^2
\prod_{k=1}^m\frac{(1+2w_k)^2}{1+4w_k}\notag\\
&=\left(\frac{w_m}{z}\right)^2
\prod_{k=1}^m\left(1+\frac{4w_k^2}{1+4w_k}\right).
\label{eq:derivativeproduct}\end{aligned}$$ Since $|1+4w_k|\ge1$, the absolute product is at most $\exp(4\sum_{k\ge1}|w_k|^2)$. Equation [\[eq:complexgrowth\]](#eq:complexgrowth){reference-type="eqref" reference="eq:complexgrowth"} bounds its exponent by $625\pi^2/6$. Also $|z|\ge1/4$, and with $m=n-1$ the leading square is at most $2500/n^2$. The factor $1/2$ in $h_n$ gives [\[eq:derivativebound\]](#eq:derivativebound){reference-type="eqref" reference="eq:derivativebound"}. Its intentionally large constant proves convergence; it is not advertised as a useful numerical cutoff certificate.

# A trace-class operator with two explicit clocks

Let $u$ count returns to $Y$, and let $\zeta$ count original applications of $T$. Define $$A_nf=h_n'f\circ h_n,\qquad
\mathcal L_\zeta=\sum_{n\ge1}\zeta^n A_n,\qquad
\Delta(u,\zeta)=\det(I-u\mathcal L_\zeta).
\label{eq:operator}$$

The branch series converges absolutely in trace norm on $H^2(\Omega)$ for every $|\zeta|\le1$. It is trace-norm continuous on that closed disk and holomorphic inside it. For fixed such $\zeta$, $\Delta$ is entire in $u$; it is jointly holomorphic for $u\in\mathbb C$, $|\zeta|<1$. The displayed branch series fails to converge for $|\zeta|>1$ even on the constant function. This last assertion does not exclude separately proved analytic continuation.

Write $f=\sum c_ke_k$. The coefficient functional has norm one and strict containment in [\[eq:range\]](#eq:range){reference-type="eqref" reference="eq:range"} gives $$\|h_n'e_k\circ h_n\|_{H^2}\le\sup_\Omega|h_n'|(2/3)^k.
\label{eq:rankone}$$ Thus the explicit rank-one expansion has summable norms and $\|A_n\|_1\le3\sup|h_n'|\le3C_*/n^2$. Hilbert-space nuclearity here is trace class. Summing proves the norm convergence and boundary continuity; locally uniform trace-norm convergence proves interior holomorphy. The ordinary trace-class Fredholm determinant gives the asserted parameter regularity and entire dependence on $u$.

For any real $x\in[1/2,1]$, the real reciprocal increment is at most two, so $g^{n-1}(x)\ge1/(2n)$. Every real factor in [\[eq:derivativeproduct\]](#eq:derivativeproduct){reference-type="eqref" reference="eq:derivativeproduct"} is at least one, and $x\le1$, yielding $h_n'(x)\ge1/(8n^2)$. If $|\zeta|>1$, the terms $\zeta^n h_n'(x)$ do not tend to zero. The branch series therefore fails the necessary term test already for $f=1$.

For a primitive induced cycle $p$, let $r_p$ be its number of returns, $N_p$ its total original time, and $\Lambda_p>1$ its forward multiplier. For $|\zeta|\le1$, set $$K(\zeta)=\sum_{n\ge1}|\zeta|^n\sup_\Omega|h_n'|<\infty.
\label{eq:K}$$ For $|u|K(\zeta)<1$, the absolutely regrouped primitive product is $$\Delta(u,\zeta)=
\prod_{p\;\text{primitive induced}}\prod_{k\ge1}
\left(1-\frac{u^{r_p}\zeta^{N_p}}{\Lambda_p^k}\right).
\label{eq:primitive}$$ At $u=1$ this identity holds initially for sufficiently small $|\zeta|$. Entire continuation in $u$ of the determinant does not imply unrestricted convergence of its primitive product.

Every $r$-branch composition $\chi$ maps the closed disk into the common interior disk and has Lipschitz constant at most $2^{-r}$. It has exactly one fixed point $x_\chi$, and invariance of $[1/2,1]$ makes that point real. Write $C_\chi f=f\circ\chi$ for composition by this branch. Summing diagonal Hardy coefficients as a geometric series and applying the residue theorem gives $$\operatorname{tr}(\chi'C_\chi)=\frac1{2\pi\mathrm i}\int_{|z-1|=3/4}
\frac{\chi'(z)}{z-\chi(z)}\,\mathrm dz
=\frac{\chi'(x_\chi)}{1-\chi'(x_\chi)}.
\label{eq:trace}$$ Strict containment justifies summation under the contour. Contraction gives the unique zero of $z-\chi(z)$ and makes it simple. Summing the absolute trace contributions over all compositions gives the bound $2K(\zeta)^r$.

First use the trace-log determinant identity on the smaller domain $|u|\|\mathcal L_\zeta\|<1$. The absolute coefficient bound extends its scalar logarithmic series to $|u|K(\zeta)<1$. The identity theorem then identifies its exponential with the entire determinant throughout that disk. This argument does not identify $K$ with the Hardy operator norm.

For an $a$-fold repeat of $p$, the inverse multiplier is $\Lambda_p^{-a}$, so its trace weight is $$\frac{\Lambda_p^{-a}}{1-\Lambda_p^{-a}}
=\sum_{k\ge1}\Lambda_p^{-ak},
\label{eq:repetitions}$$ and its two clocks are $(ar_p,aN_p)$. Grouping $r_p$ based phases and dividing by $ar_p$ in the logarithm leaves $1/a$. Absolute convergence now permits the primitive and repetition regrouping, giving [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"}. Finally $K(\zeta)\to0$ as $\zeta\to0$, which gives the stated $u=1$ specialization.

The neutral fixed point has multiplier one and would make the flat-trace denominator vanish. It cannot be inserted as another ordinary trace-class branch contribution. Equation [\[eq:unweighted\]](#eq:unweighted){reference-type="eqref" reference="eq:unweighted"} and the derivative-weighted determinant [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"} are distinct objects even though both retain the original iteration clock.

\>1

# The original Perron operator on the specified $L^1$ space

On Lebesgue $L^1([0,1])$, define $$\mathcal Pf(x)=g'(x)f(g(x))+\frac12 f((x+1)/2).
\label{eq:perron}$$ Change of variables on the two monotone branches proves positivity, preservation of integral, and $L^1$ contraction. Endpoint values do not matter in this space.

The operator [\[eq:perron\]](#eq:perron){reference-type="eqref" reference="eq:perron"} is not compact, hence not nuclear, on this $L^1$ space. On its closed zero-integral subspace, one is an approximate eigenvalue, and the exact power norm is $$\|\mathcal P^n|_{\int f=0}\|_{L^1\to L^1}=1
\quad\text{for every integer }n\ge0.
\label{eq:powernorm}$$ There are no constants $0<C<\infty$ and $0<\rho<1$ for which $$\|\mathcal P^n|_{\int f=0}\|_{L^1\to L^1}\le C\rho^n
\quad\text{for all }n\ge0.
\label{eq:nogap}$$

Choose disjoint intervals $I_j\subset(0,1/2)$ and set $f_j=\mathbf1_{I_j}/|I_j|$. Monotonicity makes the images $T(I_j)$ disjoint. Their Perron images have norm one and these disjoint supports, so their pairwise distance is two. The image of the unit ball is therefore not relatively compact. This noncompactness argument alone is not specific to intermittency.

The neutral point yields the stronger assertion. For $0<\epsilon<1/4$, let $f_\epsilon=\epsilon^{-1}\mathbf1_{[0,\epsilon]}$. Direct integration over the common support and the extra interval up to $T(\epsilon)=\epsilon+2\epsilon^2$ gives $$\|\mathcal Pf_\epsilon-f_\epsilon\|_1
=2\left(1-\frac{g(\epsilon)}\epsilon\right)\le4\epsilon.
\label{eq:approx}$$ For the equality, $g'\le1$ on the common support, and the extra mass is $(\epsilon-g(\epsilon))/\epsilon$. The inequality follows from $\epsilon=g(\epsilon)+2g(\epsilon)^2$. Now $v_\epsilon=f_\epsilon-f_{2\epsilon}$ has integral zero and norm one, and $$\|(\mathcal P-I)v_\epsilon\|_1\le12\epsilon\longrightarrow0.
\label{eq:zerointegral}$$ The subspace is invariant because the operator preserves integral. For every fixed integer $n\ge1$, the contraction property and telescoping give $$\|\mathcal P^n v_\epsilon-v_\epsilon\|_1
\le\sum_{j=0}^{n-1}\|\mathcal P^j(\mathcal P-I)v_\epsilon\|_1
\le12n\epsilon.
\label{eq:telescoping}$$ Hence the restricted power norm is at least $1-12n\epsilon$ for every $\epsilon$, and letting $\epsilon\to0$ gives a lower bound one. Contraction gives the matching upper bound; $n=0$ is the identity. This proves [\[eq:powernorm\]](#eq:powernorm){reference-type="eqref" reference="eq:powernorm"}. The right side of [\[eq:nogap\]](#eq:nogap){reference-type="eqref" reference="eq:nogap"} tends to zero, contradicting the exact norm for large $n$.

This theorem is confined to the named Lebesgue $L^1$ space. It does not transfer to an unstated bounded-variation, anisotropic, or analytic space, and it does not contradict a separately defined regularized determinant.

# Executable scope and the Route-A endpoint

The canonical receipt and its independent checker audit finite periodic words, first-return branches, exact endpoint enclosures, and the stated clock conventions. These checks are finite regression evidence; the all-period coding and all-branch trace-class result are the analytic theorems above. The very large constant in [\[eq:derivativebound\]](#eq:derivativebound){reference-type="eqref" reference="eq:derivativebound"} is kept visible and is not substituted for a practical small-error numerical certificate. No target zeros, prime table, or fitted clock enters the model.

The strict assessment is $$(A0_{\rm fail},A1_{\rm weak},A2_{\rm fail},A3_{\rm fail},A4_{\rm fail}),
\qquad\text{Route A rejected}.
\label{eq:route}$$ The source has an exact primitive ledger and induced Fredholm determinant, but no intrinsic rational-prime carrier. A source determinant alone does not clear the target A2 gate. There is no declared natural quantum lift.

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic local data, target Euler factor, root number, automorphy, target divisor or counting law, target functional equation, target-zero match, or Hilbert--Pólya operator is claimed. Route B remains disabled.

# Literature ownership and claim boundary {#literature-ownership-and-claim-boundary .unnumbered}

The intermittent-map lineage is represented by Liverani, Saussol and Vaienti [@LSV]. The alpha-one endpoint is treated by the explicit calculations here; no finite stationary-measure theorem is imported from a different parameter range. Rugh's work [@Rugh] establishes the classical connection between intermittency and regularized Fredholm determinants on carefully specified function spaces. The present package neither claims to discover inducing nor replaces those function-space qualifications. Its increment is the connected audit of one literal endpoint convention, complete primitive coding, sharp reference return tail, and \>0 one all-branch complex domain with two determinant clocks the exact original-time return correspondence \>1 , together with the original $L^1$ obstruction . No worldwide novelty or publication-acceptance claim is made.

9 C. Liverani, B. Saussol and S. Vaienti, "A probabilistic approach to intermittency," *Ergodic Theory and Dynamical Systems* 19 (1999), 671--685, [doi:10.1017/S0143385799133856](https://doi.org/10.1017/S0143385799133856). H. H. Rugh, "Intermittency and Regularized Fredholm Determinants," preprint (1996), [arXiv:chao-dyn/9610011](https://arxiv.org/abs/chao-dyn/9610011).

Round zero: complete periodic coding and exact first returns Round one: common complex domain and induced Fredholm product Round two: two clocks and the uninduced L1 obstruction
