---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-bcz-horocycle-farey-cycles-route-a"
canonical_tex: "henon_dynamics/henon_bcz_horocycle_farey_cycles_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_bcz_horocycle_farey_cycles_route_a/paper/main.pdf"
source_sha256: "0191821f4eb8d9f4e277eb46cfa7a66921b4bcadd9d04e3ab09ea198c548427e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Complete BCZ Farey Cycles: Rational Layers and Exact Least Periods

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_bcz_horocycle_farey_cycles_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_bcz_horocycle_farey_cycles_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_bcz_horocycle_farey_cycles_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_bcz_horocycle_farey_cycles_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We reconstruct the complete periodic dynamics of the classical Boca--Cobeli--Zaharescu map on its half-open Farey triangle. A direct primitive-lattice-vector calculation proves the exact first-return map and excludes every irrational-slope periodic point. Each rational point has a unique positive scale and a reduced pair of integer coordinates. At each fixed scale these coordinates form one complete Farey denominator cycle, with least period equal to a totient sum. An elementary neighbor proof handles both endpoints of the Farey list without double counting, while the included upper and excluded lower scale boundaries are kept distinct. The map is an invertible area-preserving return with an exact coordinate-swap reversor. Independent exact controls compare floor iteration against separately sorted Farey fractions for all orders one through sixty-four. This is an explicitly classical, owner-heavy reconstruction, not a new-priority claim or a conversion of native denominator arithmetic into target prime data. We connect every primitive cycle of the classical Farey-triangle return to its least physical horocycle period and its complete branch cocycle. The discrete cycle length is a totient sum, whereas the physical period is the inverse square of its real scale. Summing successive Farey gaps proves the physical formula with no unrecorded rescaling. Transposing the lattice basis-update identity then determines a nontrivial unipotent return matrix at every starting point and all its powers. These formulas retain the full rational-layer classification and irrational exclusion. At included floor walls the map can be discontinuous: the exact branch cocycle remains meaningful, but a two-sided smooth return derivative is not asserted. At interior scales the derivative has two unit multipliers, as required by the continuous radial family. The result supplies a boundary-safe classical source ledger, with independently checked exact matrix and clock identities rather than a target determinant. We give a boundary-explicit reconstruction of the classical Farey-triangle return, joining its complete periodic classification, physical horocycle clock and parabolic branch cocycle to an exact continuous-family stopping result. Each positive scale determines one primitive cycle whose discrete length is a totient sum and whose physical period is the inverse square scale. Every irrational slope is nonperiodic. The roof has mean pi squared over three and belongs to the positive Lebesgue-power spaces precisely below exponent two. An explicit number-theoretic error bound compares the two clocks asymptotically, without identifying them within a scale layer. The fixed set at every iterate is a finite union of radial segments and is uncountable already at the first iterate. Thus ordinary finite-cardinality dynamical zeta is undefined for the whole section, despite its native coprime arithmetic. The source Koopman operator is unitary but noncompact. All results are source-local with classical ownership; no target divisor, functional equation or quantum-generator construction is claimed.
author:
- 'HCS-C395 source-theorem and reproducibility package'
date: 5 September 2026
title:
- 'Complete BCZ Farey Cycles: Rational Layers and Exact Least Periods'
- 'Complete BCZ Farey Cycles: Physical Clocks and Boundary-Safe Parabolic Returns'
- 'Complete BCZ Farey Cycles: Two Clocks and the Continuous-Family Obstruction'
```

## Markdown 正文

=3em

中文摘要

本文重建经典法里三角形返回映射的完整周期分类。原始格点向量的首次横向返回给出精确映射， 并排除全部无理斜率周期点。每个有理斜率点唯一确定实尺度和互素整数坐标； 固定尺度下，全部坐标组成一个完整法里分母循环，最小周期等于欧拉函数之和。 法里邻点证明明确处理首尾端点，不重复计数；尺度层的上端点包含、下端点排除。 交换坐标给出精确反演对称，归一化面积保持不变。 生成端与独立排序法里分数的检查端核对全部一至六十四阶有限循环。 这是明确承认经典归属的源系统重建，不把分母算术改名为目标素数数据。 本文进一步连接每条本原法里循环的离散长度、物理横流周期和完整分支返回矩阵。 离散长度是欧拉函数之和，物理周期则是尺度平方的倒数；法里间隙求和证明两者不能混用。 格基更新恒等式确定每个起点的非平凡幂零剪切及全部重复。 完整有理层分类与无理斜率排除仍然保留。 包含的取整边界处映射可能不连续，因此只保留精确分支矩阵，不虚称双侧光滑导数。 内部尺度处的返回导数具有两个单位乘子，与径向连续周期族一致。 所有结论均属于经典源动力学，不构造目标行列式。 本文把完整法里周期分类、物理时钟和抛物分支矩阵闭合为连续周期族的明确停止结论。 每个正实尺度对应一个本原循环，离散长度为欧拉函数之和，物理周期为尺度平方倒数； 全部无理斜率均不周期。顶函数均值为圆周率平方的三分之一， 其正指数可积性恰在指数小于二时成立。 显式误差界连接两种时钟的渐近均值，但不把层内变化的物理时间等同于恒定离散长度。 每次迭代的固定集都是有限条径向线段之并，第一次已不可数，故整体普通点计数动力学 齐塔函数没有有限系数的初始定义。源库普曼算子酉而非紧。 本文明确经典归属，不声称目标除子、函数方程或量子生成元。

**Keywords:** Farey triangle; horocycle return; primitive cycles; parabolic cocycle; roof integrability; source boundary

# One section, native arithmetic, and classical ownership

The presence of exact arithmetic in a dynamical system does not by itself give a discrete prime-bearing orbit ledger. The Farey-triangle return is a particularly explicit test: its integer pairs are intrinsic primitive lattice coordinates, not labels added after the dynamics is computed. This paper keeps the source object, its clocks and its boundary conventions fixed throughout the argument.

The section and periodic classification are classical results of Athreya and Cheung [@AC2014]. Their construction identifies the Boca--Cobeli--Zaharescu map as a horocycle first return and relates its rational layers to Farey fractions. We reconstruct the needed arguments with explicit endpoint and matrix conventions and an independent finite verification package. This is an owner-heavy source reconstruction, not a claim of new literature priority. Cheung and Quas later established weak mixing [@CQ2024]; that theorem is acknowledged as background and is neither reproved nor used below. Strong mixing and a complete spectral type are not claims of this paper.

Set $$\label{eq:model}
\Omega=\{(a,b):0<a,b\leq1,\ a+b>1\},\qquad
T(a,b)=(b,kb-a),\quad k=\left\lfloor\frac{1+a}{b}\right\rfloor.$$ The roof is $R(a,b)=1/(ab)$. The floor takes its integer value at equality; the lower edge is excluded and the upper edges are included. We use column vectors, with branch matrix $A_k=\left(\begin{smallmatrix}0&1\\-1&k\end{smallmatrix}\right)$. One application of $T$ is one discrete return, not one unit of physical horocycle time.

# Exact first return, inverse, and irrational exclusion

Let $$p_{a,b}=\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix},\qquad
h_s=\begin{pmatrix}1&0\\-s&1\end{pmatrix},\qquad
\mathcal L_{a,b}=p_{a,b}\mathbb Z^2 .$$ A lattice with a primitive positive horizontal generator of length $a\leq1$ has a unique representation in this section: the second basis vector has height $1/a$, and its horizontal coordinate has a unique representative $b\in(1-a,1]$ modulo $a\mathbb Z$. A lattice vector is $(x,n/a)$, where $x=am+bn$ and $m,n$ are integers. At a positive horizontal-return time $s$, it obeys $0<x\leq1$ and $n/a=sx$, hence $n\geq1$. If $s<1/(ab)$, then $x>nb$, so $m\geq1$ and $x\geq a+b>1$, a contradiction. At $s=1/(ab)$ the primitive vector $(b,1/a)$ becomes $(b,0)$. This proves the exact first return.

The new oriented basis is $(b,0),(-a+kb,1/b)$. The floor inequality gives $c=kb-a\leq1<c+b$, so $(b,c)\in\Omega$, including at equality. With $B_k=A_k^{\mathsf T}$, the basis identity is $$\label{eq:basis}
p_{T(a,b)}=h_{R(a,b)}p_{a,b}B_k,\qquad
B_k=\begin{pmatrix}0&-1\\1&k\end{pmatrix}.$$ We assert this first-return description for the stated section. We do not assert that this section exhausts every orbit of the whole lattice-space flow; the short closed horocycles omitted by the classical global section statement remain outside this claim.

If $T(a,b)=(b,c)$, then $(1+c)/b=k+(1-a)/b$ and $0\leq(1-a)/b<1$. Thus $$T^{-1}(a,b)=\left(\left\lfloor\frac{1+b}{a}\right\rfloor a-b,a\right).$$ The swap $J(a,b)=(b,a)$ therefore satisfies $JTJ=T^{-1}$ and $R\circ J=R$, with the same endpoint convention. Every open branch has determinant one. Its countably many walls have area zero, and the inverse shows that branch images partition $\Omega$ up to this null set. Consequently $d\mu=2\,da\,db$ is invariant probability.

[\[lem:irrational\]]{#lem:irrational label="lem:irrational"} Every periodic point of $T$ has rational slope $b/a$.

If $T^n(a,b)=(a,b)$ and $s_n=\sum_{j=0}^{n-1}R(T^j(a,b))$, iteration of [\[eq:basis\]](#eq:basis){reference-type="eqref" reference="eq:basis"} gives $$\label{eq:integer}
B_{k_0}\cdots B_{k_{n-1}}
=p_{a,b}^{-1}h_{-s_n}p_{a,b}
=\begin{pmatrix}1-abs_n&-b^2s_n\\a^2s_n&1+abs_n\end{pmatrix}.$$ The left side is integral. Hence $a^2s_n$ is a positive integer and $abs_n$ is an integer; their ratio is $b/a$. No continuity of the branch itinerary was used.

# All rational layers and exact least periods

For $N\geq1$, define $$S_N=\{(q,r):1\leq q,r\leq N,\ \gcd(q,r)=1,\ q+r>N\},
\quad L_N=\sum_{j=1}^N\varphi(j),\quad\varphi(1)=1.$$ Let $\mathcal F_N$ be the sorted reduced fractions in $[0,1]$ with denominator at most $N$, including $0/1$ and $1/1$. There are $1+L_N$ fractions, hence $L_N$ gaps. Extend the list by integer translation when passing from the last gap to the first; the two endpoints are not two distinct marked points of the cyclic denominator list.

[\[lem:farey\]]{#lem:farey label="lem:farey"} Consecutive denominator pairs in this cyclic list are exactly $S_N$, each once, and their successor is $(q,r)\mapsto(r,kr-q)$ with $k=\lfloor(N+q)/r\rfloor$.

For determinant-one neighbors $p/q<s/r$, an intermediate fraction $c/d$ satisfies $$d=q(sd-rc)+r(qc-pd)\geq q+r.$$ Both parentheses are positive integers. This proves the absence of an intermediate denominator at most $N$ whenever $q+r>N$. All neighbors have determinant one: induct from order one by inserting mediants exactly when the denominator sum is $N+1$. Every new reduced $c/d$, $d=N+1$, has these parents. Choose $q\in\{1,\ldots,d-1\}$ with $cq\equiv1\pmod d$, set $p=(cq-1)/d$, $r=d-q$, and $s=c-p$. The parents lie in $[0,1]$, have determinant one and denominator sum $d$, and the previous inequality proves they were neighbors at order $N$.

For a given $(q,r)\in S_N$, choose the unique $0\leq p<q$ such that $pr\equiv-1\pmod q$, setting $p=0$ when $q=1$. Then $s=(1+pr)/q$ gives its unique neighboring fractions in $[0,1]$. Finally $t=kr-q$ obeys $0<t\leq N$ and $t+r>N$. The fraction $(ks-p)/t$ has determinant one with $s/r$; it is the next neighbor in the translated list. This proves the successor formula.

[\[thm:cycles\]]{#thm:cycles label="thm:cycles"} Every rational-slope point is uniquely $(\delta q,\delta r)$ with positive coprime $q,r$. For $N=\lfloor1/\delta\rfloor$ its membership in $\Omega$ is equivalent to $$\frac1{N+1}<\delta\leq\frac1N,\qquad(q,r)\in S_N.$$ At each such scale, $\delta S_N$ is exactly one primitive cycle of least period $L_N$. These are all periodic cycles of the map.

Write $1/\delta=N+\theta$, $0\leq\theta<1$. Integer division gives $$\left\lfloor\frac{1+\delta q}{\delta r}\right\rfloor
=\left\lfloor\frac{N+q+\theta}{r}\right\rfloor
=\left\lfloor\frac{N+q}{r}\right\rfloor,$$ since an integer remainder is at most $r-1$. Lemma [\[lem:farey\]](#lem:farey){reference-type="ref" reference="lem:farey"} then visits every denominator pair exactly once. No earlier return is possible. The scale and the reduced pair are unique; Lemma [\[lem:irrational\]](#lem:irrational){reference-type="ref" reference="lem:irrational"} excludes any other periodic points.

For clarity, $L_1=1$, $L_2=2$, $L_3=4$, and the third cycle is $(1,3),(3,2),(2,3),(3,1)$ before scaling. The lower scale endpoint belongs to the next order, not to this cycle. The map at the upper endpoint retains the exact floor values.

\>0

# Physical return time and complete parabolic cocycle

[\[thm:clock\]]{#thm:clock label="thm:clock"} The least positive horocycle period of the cycle at scale $\delta$ is $\delta^{-2}$, and its complete branch cocycle starting at $(\delta q,\delta r)$ is $$\label{eq:M}
M_{q,r}=\begin{pmatrix}1-qr&q^2\\-r^2&1+qr\end{pmatrix}.$$ Both eigenvalues are one. If $D=M_{q,r}-I$, then $D\ne0$, $D^2=0$, and $M_{q,r}^{\ell}=I+\ell D$ for all integers $\ell$. Physical repetitions have $\ell\geq1$ and total roof $\ell\delta^{-2}$.

A Farey gap is $s/r-p/q=1/(qr)$. Summing all gaps of one unit interval gives $$\sum_{(q,r)\in S_N}\frac1{qr}=1,\qquad
\sum_{j=0}^{L_N-1}R(T^j(\delta q,\delta r))=\delta^{-2}.$$ This is the least positive flow period, not merely a return period: integrality of $p_{a,b}^{-1}h_s p_{a,b}$ requires $s\delta^2q^2,s\delta^2qr,s\delta^2r^2$ to be integers. Their integer coefficients have greatest common divisor one. Bezout's identity therefore forces $s\delta^2\in\mathbb Z$. The positive value $s=\delta^{-2}$ works.

Transpose [\[eq:integer\]](#eq:integer){reference-type="eqref" reference="eq:integer"}, use $s_{L_N}=\delta^{-2}$, and keep the last branch on the left. This gives $A_{k_{L_N-1}}\cdots A_{k_0}=M_{q,r}$. Finally $D=(q,r)^{\mathsf T}(-r,q)$ is nonzero, has rank one, and squares to zero. The binomial identity gives all powers, including algebraic negative powers; negative integers are not physical repeat periods.

#### Why the floor-wall distinction is essential.

At strict interior scale $1/(N+1)<\delta<1/N$, every floor argument has a nonzero fractional part, and every coordinate lies below one. The finite itinerary is constant in an open neighborhood, so [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"} is the actual derivative of $T^{L_N}$. At $\delta=1/N$, the orbit contains $(1,1/N)$ and a floor argument $2N$. For example, $T(1,1/2)=(1/2,1)$, but $$\lim_{\varepsilon\downarrow0}T(1-\varepsilon,1/2+\varepsilon)
=(1/2,1/2).$$ The map is discontinuous there. Its exactly specified branch product still satisfies [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"}; calling it a two-sided smooth derivative would be false. Even in the smooth interior case, $\det(I-M_{q,r})=0$ because the fixed points vary in a radial family. An isolated nondegenerate periodic-orbit trace formula cannot be imposed on that family.

#### A reversal is not an extra cycle quotient.

The swap carries a cycle to its inverse-time presentation and preserves the roof. It acts within the fixed-scale cycle because the complete denominator set is invariant under swapping $q,r$. The primitive cycle remains a cycle with $L_N$ marked points; it is not divided by two when this reversal is applied. The shear formula retains the specified starting pair, and cyclic changes of starting point conjugate the return matrix by the intervening branch matrices.

\>1

# Roof integrability and the continuous-family obstruction

[\[thm:roof\]]{#thm:roof label="thm:roof"} For $p>0$, the roof belongs to $L^p(\Omega,\mu)$ exactly when $p<2$. Its mean is $\pi^2/3$. Moreover $$\label{eq:bound}
\left|L_N-\frac{3N^2}{\pi^2}\right|
\leq N(1+\log N)+\frac N2+\frac12.$$ Uniformly over scale layer $N$, the physical-to-discrete period ratio $\delta^{-2}/L_N$ tends to $\pi^2/3$ as $N$ tends to infinity.

Monotone convergence applied to the logarithmic series gives $$\int_\Omega R\,d\mu
=2\int_0^1\frac{-\log(1-a)}a\,da
=2\sum_{j\geq1}j^{-2}=\frac{\pi^2}{3}.$$ For $0<a<1/2$, the interval $1-a<b\leq1$ has length $a$ and $1/2<b\leq1$. The integral of $(ab)^{-p}$ on this interval is therefore bounded above and below by positive constant multiples of $a^{1-p}$. Its integral at zero is finite exactly for $p<2$; at $p=2$ it diverges logarithmically. Interchanging the coordinates handles the other cusp. On $a,b\geq1/2$ the roof is bounded.

Write $\mu_{\rm M}$ for the Moebius function, distinct from the invariant measure. Counting coprime pairs in the square gives $$2L_N-1=\sum_{d=1}^N\mu_{\rm M}(d)\lfloor N/d\rfloor^2.$$ Use $|\lfloor x\rfloor^2-x^2|\leq2x$, the harmonic-sum bound $\sum_{d\leq N}d^{-1}\leq1+\log N$, and $\sum_{d>N}d^{-2}\leq1/N$. Absolute Dirichlet convolution with the constant-one sequence yields $\sum_{d\geq1}\mu_{\rm M}(d)d^{-2}=6/\pi^2$ and proves [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"}. Finally $N\leq1/\delta<N+1$ gives the uniform period-ratio limit.

Within a layer the discrete least period is constant while the physical period varies continuously. Their limiting ratio is therefore a relation between two clocks, not permission to replace either clock by the other.

[\[thm:stop\]]{#thm:stop label="thm:stop"} For every integer $n\geq1$, $$\label{eq:fix}
\operatorname{Fix}(T^n)=
\bigcup_{\substack{N\geq1\\L_N\mid n}}
\ \bigcup_{(q,r)\in S_N}
\{(\delta q,\delta r):1/(N+1)<\delta\leq1/N\}.$$ The displayed union is finite and its point cardinality is uncountable. The ordinary finite-cardinality Artin--Mazur zeta for the entire section is undefined. Its native probability-space Koopman operator is unitary and noncompact, hence not trace class.

Theorem [\[thm:cycles\]](#thm:cycles){reference-type="ref" reference="thm:cycles"} gives [\[eq:fix\]](#eq:fix){reference-type="eqref" reference="eq:fix"} with unique representations. The inequality $L_N\geq N$ bounds the number of contributing layers. Layer one contributes the entire diagonal $\{(\delta,\delta):1/2<\delta\leq1\}$ for every $n$. Thus $\exp(\sum_{n\geq1}\#\operatorname{Fix}(T^n)z^n/n)$ has no finite first coefficient; analytic continuation cannot repair this missing initial definition. On one specified scale alone, its finite-cycle zeta is $(1-z^{L_N})^{-1}$, a different and explicitly restricted object.

The invariant invertible probability map gives a unitary Koopman operator on $L^2(\Omega,\mu)$. An infinite orthonormal sequence keeps all pairwise distances under a unitary operator, ruling out compactness. No ordinary trace-class Fredholm determinant follows on this space.

These statements do not forbid other spaces, distributional traces or regularizations. None is constructed here, and a determinant on one of them cannot be asserted from the finite-cycle formula.

# Independent evidence and scope

The canonical producer follows integer floor iteration from $(1,N)$. The independent checker imports no producer code: it constructs and sorts every reduced Farey fraction, compares every consecutive denominator pair, and verifies the floor inequalities, inverse recurrence and scalar lattice-return identity at an interior scale and at the included endpoint. All $N=1,\ldots,64$ cycles contain 27,833 marked points in total. The two scales give 55,666 exact step controls. There are 27,833 starting-position return matrices, 320 positive repetition controls, 16 explicit floor-wall discontinuity controls and 128 fixed-iterate descriptions. These are complete finite populations, not an all-order proof by extrapolation.

The symbolic lane separately checks 14 universal matrix identities and 256 exact layer identities. Its 65 ninety-digit numerical controls are quadrature and asymptotic consistency checks, not certified enclosures. Two unrelated-directory producer replays are byte identical. Repaired-hash semantic attacks, strict literal-type and unknown-key checks, actual release-write rejection of malformed evaluation files, and refusal of optimized Python modes protect the declared evidence contract. Universal quantifiers are supplied by the proofs, not by these finite checks or by the release hash.

The source has intrinsic coprime arithmetic and complete primitive dynamics, but no natural correspondence from rational primes to primitive cycles of length $\log p$. Neither the totient sum nor the continuous physical roof supplies target amplitudes or signs. \>1 The ordinary global zeta obstruction and source-operator noncompactness give stopping results, not a target construction. No target local arithmetic, Euler factors, root number, automorphy, divisor, functional equation, zero match or Hilbert--Polya operator is claimed. Route B remains disabled.

`NO_BAD_EULER_OR_ROOT_NUMBER`.

*Round zero: complete rational layers and exact least periods. Round one: physical clocks and boundary-safe parabolic returns. Round two: roof threshold, two clocks and continuous-family stopping.*

9 J. S. Athreya and Y. Cheung. A Poincaré section for the horocycle flow on the space of lattices. *International Mathematics Research Notices*, 2014(10):2643--2690, 2014. [doi:10.1093/imrn/rnt003](https://doi.org/10.1093/imrn/rnt003). Primary preprint [arXiv:1206.6597](https://arxiv.org/abs/1206.6597). Y. Cheung and A. Quas. BCZ map is weakly mixing. [arXiv:2403.14976](https://arxiv.org/abs/2403.14976), 2024.
