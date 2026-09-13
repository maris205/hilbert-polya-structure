---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-finite-blaschke-ruelle-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_finite_blaschke_ruelle_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_finite_blaschke_ruelle_spectrum_route_a/paper/main.pdf"
source_sha256: "5253a396723b86e7250a41b20225afaa50889236fc688c7b01b4b3f597b9fd8d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Nonlinear Blaschke Circle Dynamics: Complete Periodic Census and Stability

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_finite_blaschke_ruelle_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_finite_blaschke_ruelle_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_finite_blaschke_ruelle_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_finite_blaschke_ruelle_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the real family $B_a(z)=z(z-a)/(1-az)$, $0\leq a<1$, we give a complete circle periodic-point census and its nonconstant stability multipliers. An explicit increasing lift proves that every positive iterate has exactly $2^n-1$ fixed points, while off-circle contraction isolates the two attracting channels. \>0 We construct a parameter-dependent annulus on which the angular Perron operator is trace class. Invariant Laurent sections determine its entire nonzero spectrum, including the reflected-channel multiplicity. \>1 A rational fixed-point index calculation closes the stability-weighted primitive product. We prove a uniform logarithmic determinant-tail bound and distinguish the degree-two limit at zero from the noncompact rotation at the unit parameter wall. Exact rational computations and an independent direct-orbit calculation audit the normalization. The spectral mechanism is classical; the present contribution is a verified specialization and quantitative boundary analysis, with no Riemann-target identification.
author:
- 'HCS-C380 research manuscript'
date: 5 September 2026
title:
- |
  Nonlinear Blaschke Circle Dynamics:\
  Complete Periodic Census and Stability
- |
  Nonlinear Blaschke Circle Dynamics:\
  An Explicit Annulus and Complete Transfer Spectrum
- |
  Nonlinear Blaschke Circle Dynamics:\
  Primitive Determinants, Quantitative Tails, and Singular Limits
```

## Markdown 正文

**Keywords:** Blaschke products; periodic orbits; stability multipliers; transfer operators; Fredholm determinants; singular limits.

chinese-simplified

中文摘要

本文研究实参数有限布拉施克圆周映射，证明所有迭代的不动点数量及本原 周期数量，并记录随轨道变化的稳定性乘子。严格递增的提升给出完整性， 圆内与圆外的收缩则隔离两个吸引通道。 \>0 进一步构造显式参数环域，证明角密度转移算子属于迹类，并从不变洛朗 有限维子空间确定全部非零谱及其重数。 \>1 通过有理映射不动点指标恒等式连接本原轨道乘积，给出定量截断尾界， 并区分零参数的二倍映射与单位参数边界的非紧旋转。精确有理数复算及 直接周期求解独立检验公式。本文明确承认既有谱定理的文献来源，贡献为 完整专门化、可复核证据及定量边界分析，不宣称目标黎曼行列式。

关键词：布拉施克乘积；周期轨道；稳定性乘子；转移算子； 弗雷德霍姆行列式；奇异极限。

# Object, provenance, and an all-period orbit theorem

The time variable is integer iteration of $\tau_a=B_a|_{\mathbb T}$, where $\mathbb T=\{z:|z|=1\}$ and $0\leq a<1$. All complex phases below retain their sign. The explicit transfer spectra of analytic circle maps are prior work of Slipantschuk, Bandtlow and Just [@explicit], and the finite-Blaschke spectral theorem is due to Bandtlow, Just and Slipantschuk [@BJS]. We give a direct real-family proof and a quantitative finite-section certificate. The nonlinear multiplier atlas differs from the workspace's linear expanding-circle and quadratic inverse-branch systems. This owner distinction is not a claim of literature priority.

Choose the lift $\psi_a(0)=0$ of $B_a(e^{i\theta})=e^{i\psi_a(\theta)}$. Logarithmic differentiation gives $$\psi_a'(\theta)=1+\frac{1-a^2}{1-2a\cos\theta+a^2},\qquad
 \frac2{1+a}\leq\psi_a'(\theta)\leq\frac2{1-a}. \label{eq:expansion}$$ The extrema occur at $\theta=\pi$ and $0$. Thus every map in the chamber is expanding, orientation preserving and of degree two.

For every $n\geq1$ the circle fixed count and primitive cycle count are $$F_n=2^n-1,\qquad
 P_n=\frac1n\sum_{d\mid n}\mu(n/d)(2^d-1). \label{eq:census}$$ Every circle fixed point of every iterate is simple. For a primitive cycle $\gamma$ of length $p$, its multiplier is $\Lambda_\gamma=\prod_{j=0}^{p-1}\psi_a'(\theta_j)>1$; its $s$th repetition has length $sp$ and multiplier $\Lambda_\gamma^s$.

The lift of the $n$th iterate satisfies $\psi_{a,n}(\theta+2\pi)=\psi_{a,n}(\theta)+2\pi2^n$. The function $\psi_{a,n}(\theta)-\theta$ has positive derivative by [\[eq:expansion\]](#eq:expansion){reference-type="eqref" reference="eq:expansion"} and increases by exactly $2\pi(2^n-1)$ on a half-open fundamental interval. It meets that many multiples of $2\pi$, each exactly once. Nonzero derivative of the fixed-point equation proves simplicity. The identity $F_n=\sum_{d\mid n}dP_d$ gives Moebius inversion; the chain rule proves the repetition law.

Complex conjugation commutes with $B_a$. It pairs or fixes circle cycles, preserving their multipliers; it does not reverse time. Since the map is two-to-one, there is no globally defined inverse dynamics on the circle. The orientation is positive, and the real Perron weights have phase zero. Their multiplier dependence cannot be removed when constructing traces.

For $0<s<1$ the Blaschke factor satisfies $$|B_a(z)|\leq q_a(s):=s\frac{s+a}{1+as}<s\quad (|z|\leq s).
 \label{eq:disk}$$ The maximum modulus of $(z-a)/(1-az)$ on $|z|=s$ is $(s+a)/(1+as)$, as follows by differentiating its squared modulus with respect to $\cos\theta$. Therefore no nonzero interior point is periodic. The reflection identity $B_a(1/\bar z)=1/\overline{B_a(z)}$ gives the same result outside the circle. The only off-circle fixed points of an iterate are $0$ and $\infty$, with local multipliers $(-a)^n$.

The unweighted Artin--Mazur zeta already follows from [\[eq:census\]](#eq:census){reference-type="eqref" reference="eq:census"}: $$\zeta_{\rm AM}(u)=\exp\sum_{n\geq1}\frac{F_nu^n}{n}
 =\frac{1-u}{1-2u}\quad(|u|<1/2). \label{eq:AM}$$ It is independent of $a$, whereas the stability weights are not.

*Round-zero certificate: complete orbit census, stability, repetitions, orientation, and off-circle separation.*

\>0

# An explicit trace-class annulus and the exact spectrum

Put $r=(1+a)/2$, $A_r=\{r<|z|<r^{-1}\}$ and $t=(r+q_a(r))/2$. Then $0<t<r<1$. The Hardy norm on this annulus is $$\|f\|_r^2=\sum_{m\in\mathbb Z}|f_m|^2(r^{2m}+r^{-2m}).$$ Define the angular-density Perron operator by the local branch sum $$(\mathcal P_a f)(w)=\sum_{B_a(z)=w}\frac{w}{zB_a'(z)}f(z).
 \label{eq:operator}$$ The branches themselves are not global functions on the annulus. Their sum is single valued. Multiplication by $z$ conjugates the derivative transfer convention of [@BJS] to [\[eq:operator\]](#eq:operator){reference-type="eqref" reference="eq:operator"}.

The operator in [\[eq:operator\]](#eq:operator){reference-type="eqref" reference="eq:operator"} is trace class on $H^2(A_r)$.

Choose $s>r$, $s<1$ with $q_a(s)<t$. Formula [\[eq:disk\]](#eq:disk){reference-type="eqref" reference="eq:disk"} and its reflection put every preimage of $\overline{A_t}$ strictly inside $A_r$, in $s<|z|<s^{-1}$. The critical points are $c=a/(1+\sqrt{1-a^2})$ and $1/c$ for $a>0$; their images lie outside $\overline{A_t}$ since $c<a<r$. At zero parameter the critical points are zero and infinity. Consequently all local weights are bounded near the compact target boundary. Cauchy--Schwarz on the Laurent series bounds evaluation on the compact source subannulus. This proves boundedness of the extension $\widetilde{\mathcal P}_a:H^2(A_r)\to H^2(A_t)$.

The restriction $J:H^2(A_t)\to H^2(A_r)$ is diagonal with singular values $$s_m(J)=\sqrt{\frac{r^{2m}+r^{-2m}}{t^{2m}+t^{-2m}}}
 \leq\sqrt2(t/r)^{|m|}\ (m\ne0),\qquad s_0=1.$$ They are summable. The factorization $\mathcal P_a=J\widetilde{\mathcal P}_a$ proves trace class by the ideal property [@Simon].

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} For $0<a<1$, the nonzero spectrum consists of $1$ with algebraic multiplicity one and $(-a)^k$, $k\geq1$, each with algebraic multiplicity two. Zero is in the spectrum. The entire Fredholm determinant and traces are $$\begin{aligned}
 D_a(u)&=\det(I-u\mathcal P_a)=(1-u)\prod_{k\geq1}(1-(-a)^ku)^2,
 \label{eq:det}\\
 \operatorname{Tr}\mathcal P_a^n&=\frac{1+(-a)^n}{1-(-a)^n}\quad(n\geq1). \label{eq:trace}\end{aligned}$$ At $a=0$, $D_0(u)=1-u$, but $\mathcal P_0$ is not rank one.

Since $B_a(0)=0$, the mean-value formula for positive powers of $B_a$ and complex conjugation for negative powers prove Lebesgue invariance. Hence $\mathcal P_a1=1$. A branchwise change of angular variable gives, for $m,k\geq1$, $$\mathcal P_a z^m=[z^m]B_a(z)^k. \label{eq:matrix}$$ The Taylor coefficients are real. Negative output modes would require the constant coefficient of $z^mB_a(z)^k$, which vanishes; the constant output mode also vanishes. Because $B_a(z)^k$ has order at least $k$ at zero, [\[eq:matrix\]](#eq:matrix){reference-type="eqref" reference="eq:matrix"} is zero for $k>m$, and its diagonal is $(-a)^m$. Conjugation gives the second block.

Thus the spaces $V_N=\operatorname{span}(z^{-N},\ldots,z^N)$ are invariant with the advertised diagonal. For their orthogonal projections $Q_N$, trace class implies $\|\mathcal P_a-Q_N\mathcal P_aQ_N\|_1\to0$: first approximate by a finite sum of rank-one maps and use strong convergence on their vectors, then bound the remaining trace norm by boundedness of the projections. Fredholm continuity [@Simon] gives [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"} locally uniformly, proving all algebraic multiplicities and excluding additional nonzero eigenvalues. Taking traces of powers gives a geometric series and [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"}. At zero parameter, [\[eq:matrix\]](#eq:matrix){reference-type="eqref" reference="eq:matrix"} yields $\mathcal P_0z^{2m}=z^m$, so the zero-spectral part has not vanished.

*Round-one certificate: explicit annular extension, trace class, both spectral channels, and their entire determinant.*

\>1

# Primitive product, quantitative tails, and the singular wall

For every $n\geq1$, $$\sum_{\tau_a^nx=x}\frac{1}{(\tau_a^n)'(x)-1}
 =\frac{1+(-a)^n}{1-(-a)^n}. \label{eq:orbittrace}$$ For $|u|<1$ the Fredholm determinant has the absolutely convergent logarithmic primitive product $$D_a(u)=\prod_{\gamma\ {m primitive}}\prod_{j\geq1}
 \left(1-\frac{u^{p_\gamma}}{\Lambda_\gamma^j}\right).
 \label{eq:primitive}$$

The rational fixed-point index formula on the sphere states that $\sum_{Rz=z}(1-R'(z))^{-1}=1$ when the fixed points are simple; it is the residue theorem for $dz/(z-R(z))$ with the infinity term evaluated in coordinate $1/z$. For $R=B_a^n$, the two off-circle terms are each $1/(1-(-a)^n)$. Moving them to the other side proves [\[eq:orbittrace\]](#eq:orbittrace){reference-type="eqref" reference="eq:orbittrace"}. At a circle fixed point the complex and angular iterate derivatives agree because the endpoint factor $B_a^n(z)/z$ is one.

The trace sequence is bounded for fixed $a<1$. Thus $-\sum_{n\geq1}u^n\operatorname{Tr}\mathcal P_a^n/n$ converges absolutely for $|u|<1$. Group fixed points by their primitive cycles, using $p_\gamma$ starting points per repetition and $1/(\Lambda^s-1)=\sum_{j\geq1}\Lambda^{-js}$. All absolute sums converge by the same trace bound, so regrouping proves [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"}. The entire continuation comes from [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"}; no everywhere-convergent orbit product is asserted.

Let $D_{a,N}(u)=(1-u)\prod_{k=1}^N(1-(-a)^ku)^2$. If $|u|\leq R$ and $Ra^{N+1}<1$, its omitted tail has an analytic logarithm satisfying $$\left|\log\frac{D_a(u)}{D_{a,N}(u)}\right|
 \leq E_{a,N,R}:=\frac{2Ra^{N+1}}{(1-a)(1-Ra^{N+1})}. \label{eq:tail}$$ The quotient is extended across the common finite-product zeros. The relative tail error is at most $e^{E_{a,N,R}}-1$. For $0<a<1$ the number of determinant zeros in $|u|\leq R$ is $${\bf1}_{R\geq1}+2\#\{k\geq1:a^{-k}\leq R\}. \label{eq:roots}$$ The limit $a\downarrow0$ gives $D_a\to1-u$ locally uniformly. At $a=1$ the cancelled rational map is $-z$ and its Perron operator is noncompact.

Use $|\log(1-v)|\leq |v|/(1-|v|)$ on each omitted factor and sum $2R\sum_{k>N}a^k/(1-Ra^{N+1})$. Exponentiation gives the relative bound. The exact spectral product gives [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"}, including points on the boundary, without a floating logarithm decision. Formula [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} proves the zero-parameter determinant limit. At $a=1$, $z(z-1)/(1-z)=-z$ after removal of the cancelled point. Every even iterate is the identity. Its angular Perron operator is a unitary rotation on the infinite-dimensional Hardy space and therefore is not compact. Its fixed sets and operator class differ from every $a<1$ member.

With $q=-a$, another exact check is $$(1-u)(1-qu)D_a(qu)=D_a(u). \label{eq:qdiff}$$ This shift relation is internal to the parameter $a$ and is not a target functional equation. In particular [\[eq:AM\]](#eq:AM){reference-type="eqref" reference="eq:AM"}, [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"}, and [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"} must retain their different weights and reciprocals.

# Evidence, limitations, and Route A

Five exact rational parameters $0,1/7,1/3,1/2,3/4$ audit 24 unweighted iterate counts, 16 trace/coefficient orders, the Laurent section through degree 10, four spectral cutoffs, and nine tail domains per parameter. The independent checker computes map coefficients by series division and convolution rather than the producer's binomial expansion. It checks determinant coefficients by [\[eq:qdiff\]](#eq:qdiff){reference-type="eqref" reference="eq:qdiff"}, while the producer uses the logarithmic trace recurrence. An additional symbolic/direct-orbit lane checks 171 periodic points with 65-digit arithmetic and monotone bisection; the largest weighted-trace discrepancy is below $3\cdot10^{-54}$. These are formula audits, not finite-data proofs of the all-period theorem.

Thirty semantic evidence variants are rejected after repairing their outer hashes, alongside two raw parser attacks. They attack multiplier signs, channel multiplicities, orbit counts, annulus direction, tail bounds, zero counts, parameter faces, schema/type substitutions and target-claim flags. The output reproduces byte-for-byte from two unrelated working directories. Exact data, source proof, scripts and manuscript revisions accompany this paper.

The strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ There is a complete native orbit/trace/determinant chain, but no rational-prime carrier, logarithmic-prime clock or Riemann divisor bridge. The exact source spectrum cannot upgrade these absent target ingredients. The adjoint Koopman construction is only a formal lift hint; no same-clock unitary quantization is supplied. Route B remains disabled. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Contribution and disclosure.

This is an AI-assisted mathematical research manuscript with executable verification and model-family peer checks, not human peer review or a literature-novelty certificate. The prior finite-Blaschke spectrum is explicitly attributed. The package closes its specialization, orbit multiplier identity, explicit annular certificate, tail bound and singular faces. No target Euler data, root number, automorphy or Hilbert--Polya operator is claimed.

*Round-two certificate: primitive determinant identity, quantitative tail/root counts, parameter-wall obstruction, and audited scope.*

9 J. Slipantschuk, O. F. Bandtlow and W. Just, *Analytic expanding circle maps with explicit spectra*, arXiv:1306.0445 (2013). <https://arxiv.org/abs/1306.0445>. O. F. Bandtlow, W. Just and J. Slipantschuk, *Spectral structure of transfer operators for expanding circle maps*, Ann. Inst. H. Poincare C Anal. Non Lineaire **34** (2017), 31--43, Theorem 5.4. <https://doi.org/10.1016/j.anihpc.2015.08.004>. B. Simon, *Trace Ideals and Their Applications*, second edition, Mathematical Surveys and Monographs **120**, American Mathematical Society (2005). <https://bookstore.ams.org/SURV/120>.
