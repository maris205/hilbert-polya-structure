---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-8-time-ordered-cycle-curvature"
canonical_tex: "zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/time-ordered-cycle-curvature.pdf"
source_sha256: "4d79ed5cafedc07b4ceb26a6153d5be57b1bfac4a873b33113544a938442ad40"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Time-Ordered Cycle Curvature for Gaussian Quadratic Markov Cocycles Two-Step Spectral Blindness, Commutator Response, and Parity-Compatible Directed Traces

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/time-ordered-cycle-curvature.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Frozen cycle traces encode the resonances of a Gaussian quadratic Markov operator, but they do not determine which scalar spectral quantities retain the order of a non-autonomous drive. We identify an exact obstruction and construct the first nontrivial time-directed replacements.

  Let $\mathcal K_u$ be the normalized fixed-noise kernel centered at $f_u(x)=1-u x^2$ on $[-1,1]$. Each $\mathcal K_u$ is Hilbert--Schmidt, so every two-step block $\mathcal K_a\mathcal K_b$ is trace class. Nevertheless, $$\operatorname{spec}(\mathcal K_a\mathcal K_b)\setminus\{0\}
   =\operatorname{spec}(\mathcal K_b\mathcal K_a)\setminus\{0\},
   \qquad
   \det(I-z\mathcal K_a\mathcal K_b)=\det(I-z\mathcal K_b\mathcal K_a).$$ Thus no two-step eigenvalue or Fredholm determinant can detect reversal inside one pair. Order is not absent: for symmetric parameters, $$\mathcal K_{u-\varepsilon}\mathcal K_{u+\varepsilon}
   -\mathcal K_{u+\varepsilon}\mathcal K_{u-\varepsilon}
   =2\varepsilon[\mathcal K_u,\mathcal K_u']+O(\varepsilon^3).$$ The stationary measures and every separating state--observable expectation have corresponding first-order responses, although the spectra remain identical.

  For the logarithmic schedule $u_n=u_{\mathrm c}+\kappa(\log(n+c))^{-p}$, paired commutator corrections are summable but have a nonzero renormalized tail. If $m_j=(u_{2j-1}+u_{2j})/2$, then in operator norm $$(\log(2J+c))^p\sum_{j\ge J}
   \left(\mathcal K_{u_{2j-1}}\mathcal K_{u_{2j}}-\mathcal K_{m_j}^2\right)
   \longrightarrow-\frac{\kappa}{4}[\mathcal K_{u_{\mathrm c}},\mathcal K_{u_{\mathrm c}}'].$$

  The minimal scalar orientation trace requires three parameter values: $$\Omega_{\mathcal A}(a,b,c)
   =\operatorname{tr}\bigl(\mathcal A_a[\mathcal A_b,\mathcal A_c]\bigr).$$ For every analytic Hilbert--Schmidt family it factors exactly as $$\Omega_{\mathcal A}(a,b,c)
   =(a-b)(b-c)(c-a)G_{\mathcal A}(a,b,c),
   \quad
   G_{\mathcal A}(u,u,u)=\frac12\operatorname{tr}\bigl(\mathcal A_u[\mathcal A_u',\mathcal A_u'']\bigr).$$ Taking $\mathcal A_u=\mathcal K_u^2$ gives the minimal parity-compatible scalar, a directed six-step trace. Under a macroscopic logarithmic schedule its first nonzero scale is $(\log T)^{-3p-3}$; consecutive directed traces are of order $n^{-3}(\log n)^{-3p-3}$ and are absolutely summable.

  Target-independent computations verify two-step spectral coincidence to $5.3\times10^{-12}$ while the matrices, stationary laws, and observables differ linearly in $\varepsilon$. The one-step and parity-block orientation curvatures are nonzero and converge under midpoint discretization at order $d^{-2}$. The results close the route through raw two-step eigenphases but leave a precise commutator and directed-determinant route. No Riemann zero or arithmetic target is used.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Time-Ordered Cycle Curvature for Gaussian** **Quadratic Markov Cocycles**\
  Two-Step Spectral Blindness, Commutator Response, and\
  Parity-Compatible Directed Traces
```

## Markdown 正文

**Keywords:** non-autonomous Markov operator; time ordering; commutator; Fredholm determinant; orientation curvature; parity block; logarithmic schedule.

**MSC 2020:** 47A10; 47B47; 47G10; 37H20; 60J10; 65R20.

# Introduction

A non-autonomous product remembers order at the operator level, but not every spectral statistic does. The elementary identity that $AB$ and $BA$ have the same nonzero spectrum becomes a serious obstruction when a two-step block is proposed as the primitive time-directed observable. Eigenvectors, invariant measures, and subsequent products can change under reversal even while all nonzero eigenvalues and the complete Fredholm determinant remain fixed.

This distinction is relevant near the first quadratic band-merging parameter $$\label{eq:uc}
 u_{\mathrm c}^3-2u_{\mathrm c}^2+2u_{\mathrm c}-2=0,
 \qquad u_{\mathrm c}=1.543689012692\ldots.$$ The deterministic map has a period-two decomposition and a parity eigenvalue $-1$, so the natural autonomous primitive is a two-step block [@WangParity2026]. Gaussian smoothing turns the finite matrices into a compact analytic continuum Markov family, and midpoint matrices recover its nonzero isolated resonances [@WangGaussianResponse2026; @WangContinuum2026]. The preceding paper then constructed centered cycle traces and a regularized determinant for each frozen operator [@WangCycleSpectrum2026].

The remaining issue is temporal. An unweighted operator average forgets order, and its first logarithmic response depends only on the mean parameter offset [@WangObstructions2026]. Products are order sensitive, often organized through commutator or Magnus-type expansions [@BlanesEtAl2009], but a claim about a product spectrum must still specify which order information survives cyclic trace invariance.

The present paper supplies that audit. The first result is negative and exact: one paired spectrum is blind to reversal. The positive replacement has two levels. At operator level, a first-order commutator changes stationary laws and observable responses. At scalar level, the minimal directed trace needs three factors and begins cubically in parameter separations. If parity blocks are retained, the minimal scalar uses three two-step blocks, hence six one-step kernels.

The logarithmic schedule separates these levels sharply. Accumulated within-pair commutators survive at the same $(\log J)^{-p}$ tail scale as the ordinary response. A scalar orientation trace at three macroscopic times is smaller, of order $(\log T)^{-3p-3}$, while the consecutive version is summable. This scale hierarchy determines what a future cocycle or trace formula can plausibly measure.

## Main results {#main-results .unnumbered}

1.  Every two-step product $\mathcal K_a\mathcal K_b$ is trace class, but reversal preserves its entire nonzero spectrum and Fredholm determinant. The two stationary measures are transported into one another by one factor.

2.  Symmetric order reversal has the operator expansion $2\varepsilon[\mathcal K,\mathcal K']+O(\varepsilon^3)$. A Poisson equation gives the first stationary response, so order remains visible to states and observables despite spectral blindness.

3.  For a logarithmic drive, the sum of late paired corrections converges in operator norm and has the explicit renormalized commutator limit $-(\kappa/4)[\mathcal K_{u_{\mathrm c}},\mathcal K_{u_{\mathrm c}}']$.

4.  The three-factor directed trace is a fully alternating analytic function of its parameters. It factors by the Vandermonde polynomial, and its diagonal quotient is the intrinsic orientation curvature $\frac12\operatorname{tr}(\mathcal A[\mathcal A',\mathcal A''])$.

5.  The frozen parity family $\mathcal Q_u=\mathcal K_u^2$ yields a directed six-step trace. This is the minimal parity-compatible scalar that distinguishes an ordering of frozen blocks.

6.  Macroscopic and consecutive logarithmic schedules have exact directed scales. Midpoint approximations of both curvatures converge as $d^{-2}$, and all predicted small-separation powers are recovered numerically.

## Scope {#scope .unnumbered}

The paper studies fixed $\sigma>0$. It proves statements about Markov products, trace ideals, and logarithmic schedules, not a small-noise theorem. The numerical widths are untuned, no Riemann zero is loaded, and no Markov product is identified with a self-adjoint energy operator. In particular, the paper tests one proposed bridge in a longer Hilbert--Pólya research program; it does not assert that another bridge exists [@BerryKeating1999].

# Fixed-noise operators and two-step trace ideals {#sec:operators}

Let $I=[-1,1]$, fix $\sigma>0$, and put $$\begin{aligned}
 f_u(x)&=1-u x^2,\label{eq:map}\\
 w_u(x,y)&=\exp\left[-\frac{(y-f_u(x))^2}{2\sigma^2}\right],\\
 Z_u(x)&=\int_Iw_u(x,z)\,dz,
 \qquad q_u(x,y)=\frac{w_u(x,y)}{Z_u(x)}.\label{eq:kernel}\end{aligned}$$ The observable Markov operator is $$\label{eq:operator}
 (\mathcal K_u g)(x)=\int_Iq_u(x,y)g(y)\,dy.$$ On $C(I)$ it is a compact strongly positive contraction with $\mathcal K_u\mathbf 1=\mathbf 1$. On $H=L^2(I,dx)$ it is Hilbert--Schmidt. The family is analytic in operator norm on $C(I)$ and in Hilbert--Schmidt norm on $H$; all kernel derivatives are smooth and bounded on compact parameter intervals [@Kress2014; @WangContinuum2026].

Write $\mathfrak S_1(H)$ and $\mathfrak S_2(H)$ for the trace-class and Hilbert--Schmidt ideals. Since the product of two Hilbert--Schmidt operators is trace class, $$\label{eq:block}
 \mathcal B_{a,b}=\mathcal K_a\mathcal K_b\in\mathfrak S_1(H).$$ It remains a strongly positive Markov operator on $C(I)$; hence its Perron root $1$ is algebraically simple.

# Two-step spectral blindness {#sec:blindness}

[\[thm:ab-ba\]]{#thm:ab-ba label="thm:ab-ba"} For every real $a,b$, $$\label{eq:ab-spectrum}
 \operatorname{spec}(\mathcal B_{a,b})\setminus\{0\}
 =\operatorname{spec}(\mathcal B_{b,a})\setminus\{0\},$$ including algebraic multiplicity and Jordan structure. Moreover, for every $z\in\mathbb C$, $$\label{eq:sylvester}
 \det(I-z\mathcal K_a\mathcal K_b)=\det(I-z\mathcal K_b\mathcal K_a).$$ After removing the simple Perron factor, the entire non-Perron determinants $$\label{eq:two-step-centered-det}
 \Delta_{a,b}(z)=\frac{\det(I-z\mathcal K_a\mathcal K_b)}{1-z}$$ satisfy $\Delta_{a,b}=\Delta_{b,a}$.

For bounded operators $A,B$, the maps $B$ and $A$ identify the generalized eigenspaces of $AB$ and $BA$ at every $\lambda\ne0$. This gives [\[eq:ab-spectrum\]](#eq:ab-spectrum){reference-type="eqref" reference="eq:ab-spectrum"}. Because $\mathcal K_a,\mathcal K_b\in\mathfrak S_2$, both products are trace class. The trace-ideal Sylvester identity gives [\[eq:sylvester\]](#eq:sylvester){reference-type="eqref" reference="eq:sylvester"} [@GohbergEtAl2000; @Simon2005]. Strong positivity makes the zero of the determinant at $z=1$ simple, so division gives the entire identity for $\Delta$.

The spectrum is blind, but the eigenvectors are not. If $\mathcal K_a\mathcal K_b r=\lambda r$ with $\lambda\ne0$, then $\mathcal K_b r$ is a generalized eigenvector of $\mathcal K_b\mathcal K_a$ at the same eigenvalue. This transport depends on the order.

[\[prop:stationary-transport\]]{#prop:stationary-transport label="prop:stationary-transport"} Let $\pi_{a,b}$ be the unique invariant probability of $\mathcal K_a\mathcal K_b$. Then $$\label{eq:stationary-transport}
 \pi_{b,a}=\pi_{a,b}\mathcal K_a,
 \qquad
 \pi_{a,b}=\pi_{b,a}\mathcal K_b.$$

Since $\mathcal K_a\mathbf 1=\mathbf 1$, $\pi_{a,b}\mathcal K_a$ is a probability. Associativity and invariance give $$(\pi_{a,b}\mathcal K_a)(\mathcal K_b\mathcal K_a)
 =\pi_{a,b}(\mathcal K_a\mathcal K_b)\mathcal K_a
 =\pi_{a,b}\mathcal K_a.$$ Uniqueness of the invariant probability proves the first identity. The second is symmetric.

Thus equality of eigenvalues cannot be promoted to equality of the two Markov dynamics. A statistic based only on the eigenvalues of one two-step block cannot identify which kernel came first.

# Commutator response inside one pair {#sec:commutator}

Fix $u$ and abbreviate $$\mathcal K=\mathcal K_u,
 \qquad \dot\mathcal K=\partial_u\mathcal K_u,
 \qquad \ddot\mathcal K=\partial_u^2\mathcal K_u,
 \qquad \mathcal C_u=[\mathcal K_u,\mathcal K_u'].$$ Define the forward and reversed symmetric blocks $$\label{eq:arrows}
 \mathcal B_\to(u,\varepsilon)
 =\mathcal K_{u-\varepsilon}\mathcal K_{u+\varepsilon},
 \qquad
 \mathcal B_\leftarrow(u,\varepsilon)
 =\mathcal K_{u+\varepsilon}\mathcal K_{u-\varepsilon}.$$

[\[thm:commutator\]]{#thm:commutator label="thm:commutator"} Locally uniformly in $u$, in operator norm on $C(I)$ and trace norm on $H$, $$\begin{aligned}
 \mathcal B_\to(u,\varepsilon)
 &=\mathcal K^2+\varepsilon[\mathcal K,\dot\mathcal K]
 +\varepsilon^2\left\{
 \frac12(\mathcal K\ddot\mathcal K+\ddot\mathcal K\mathcal K)-\dot\mathcal K^2
 \right\}+O(\varepsilon^3),\label{eq:forward-expansion}\\
 \mathcal B_\to(u,\varepsilon)-\mathcal B_\leftarrow(u,\varepsilon)
 &=2\varepsilon[\mathcal K,\dot\mathcal K]+O(\varepsilon^3).
 \label{eq:commutator-expansion}\end{aligned}$$ In particular, the leading order difference is traceless and invisible to the determinant in [\[thm:ab-ba\]](#thm:ab-ba){reference-type="ref" reference="thm:ab-ba"}.

Insert the operator-norm Taylor expansions $$\mathcal K_{u\pm\varepsilon}
 =\mathcal K\pm\varepsilon\dot\mathcal K
 +\frac{\varepsilon^2}{2}\ddot\mathcal K+O(\varepsilon^3)$$ and multiply. Reversal is equivalent to replacing $\varepsilon$ by $-\varepsilon$, so all even terms cancel in the difference. The products of two Hilbert--Schmidt remainders give the same expansion in trace norm.

The first-order change can be seen by a state and an observable: $$\label{eq:weak-order-response}
 \mu\left(\mathcal B_\to-\mathcal B_\leftarrow\right)g
 =2\varepsilon\,\mu[\mathcal K,\dot\mathcal K]g+O_{\mu,g}(\varepsilon^3).$$ It also changes the stationary law. Let $\pi_u$ be invariant for $\mathcal K_u$.

[\[prop:stationary-response\]]{#prop:stationary-response label="prop:stationary-response"} There is a unique signed measure $\eta_u$ satisfying $$\label{eq:poisson}
 \eta_u(I-\mathcal K_u^2)=\pi_u[\mathcal K_u,\mathcal K_u'],
 \qquad \eta_u(\mathbf 1)=0.$$ In total variation, $$\label{eq:stationary-expansion}
 \pi_\to(u,\varepsilon)-\pi_\leftarrow(u,\varepsilon)
 =2\varepsilon\eta_u+O(\varepsilon^3).$$

The fixed-noise kernel has a simple Perron root and all other spectral values strictly inside the unit disk. Thus $I-(\mathcal K_u^*)^2$ is invertible on the zero-mass measures [@Seneta2006; @WangCycleSpectrum2026], proving existence and uniqueness in [\[eq:poisson\]](#eq:poisson){reference-type="eqref" reference="eq:poisson"}. Differentiate the stationarity equation for [\[eq:forward-expansion\]](#eq:forward-expansion){reference-type="eqref" reference="eq:forward-expansion"}; its first derivative is exactly [\[eq:poisson\]](#eq:poisson){reference-type="eqref" reference="eq:poisson"}. Since reversal sends $\varepsilon$ to $-\varepsilon$, the stationary difference is odd and the next term is cubic [@Kato1995].

## Renormalized tail of a logarithmic pairing

Let $$\label{eq:schedule}
 u_n=u_{\mathrm c}+\frac{\kappa}{(\log(n+c))^p},
 \qquad c>1,\quad p>0.$$ For pair $j$, put $$\label{eq:pair-coordinates}
 m_j=\frac{u_{2j-1}+u_{2j}}2,
 \qquad
 \varepsilon_j=\frac{u_{2j}-u_{2j-1}}2,
 \qquad
 L_J=\log(2J+c).$$

[\[thm:pair-tail\]]{#thm:pair-tail label="thm:pair-tail"} The series $$\label{eq:tail-operator}
 \mathcal E_J=\sum_{j=J}^{\infty}
 \left(\mathcal K_{u_{2j-1}}\mathcal K_{u_{2j}}-\mathcal K_{m_j}^2\right)$$ converges in operator norm on $C(I)$. Moreover, $$\begin{aligned}
 J L_J^{p+1}\varepsilon_J&\longrightarrow-\frac{\kappa p}{4},
 \label{eq:increment-limit}\\
 L_J^p\sum_{j=J}^{\infty}\varepsilon_j
 &\longrightarrow-\frac{\kappa}{4},\label{eq:scalar-tail}\\
 L_J^p\mathcal E_J
 &\longrightarrow-\frac{\kappa}{4}
 [\mathcal K_{u_{\mathrm c}},\mathcal K_{u_{\mathrm c}}'].
 \label{eq:operator-tail}\end{aligned}$$ If every pair is reversed, the last limit changes sign. Therefore the renormalized forward-minus-reverse tail is $-(\kappa/2)[\mathcal K_{u_{\mathrm c}},\mathcal K_{u_{\mathrm c}}']$.

The mean-value theorem applied to [\[eq:schedule\]](#eq:schedule){reference-type="eqref" reference="eq:schedule"} gives $$\varepsilon_j
 =-\frac{\kappa p}{4j(\log(2j+c))^{p+1}}(1+o(1)).$$ This proves [\[eq:increment-limit\]](#eq:increment-limit){reference-type="eqref" reference="eq:increment-limit"}. Integral comparison gives [\[eq:scalar-tail\]](#eq:scalar-tail){reference-type="eqref" reference="eq:scalar-tail"}; in particular, $\sum_j|\varepsilon_j|<\infty$.

Apply [\[eq:forward-expansion\]](#eq:forward-expansion){reference-type="eqref" reference="eq:forward-expansion"} at $m_j$: $$\mathcal K_{u_{2j-1}}\mathcal K_{u_{2j}}-\mathcal K_{m_j}^2
 =\varepsilon_j\mathcal C_{m_j}+O(\varepsilon_j^2).$$ The squared remainder is summable. Also $\mathcal C_{m_j}-\mathcal C_{u_{\mathrm c}}=O((\log j)^{-p})$, so $$\sum_{j\ge J}|\varepsilon_j|
 \left\lVert \mathcal C_{m_j}-\mathcal C_{u_{\mathrm c}}\right\rVert
 =O((\log J)^{-2p}).$$ Combine this estimate with [\[eq:scalar-tail\]](#eq:scalar-tail){reference-type="eqref" reference="eq:scalar-tail"} to obtain [\[eq:operator-tail\]](#eq:operator-tail){reference-type="eqref" reference="eq:operator-tail"}. Reversal negates every odd-order term.

[\[rem:sum-product\]]{#rem:sum-product label="rem:sum-product"} The object [\[eq:tail-operator\]](#eq:tail-operator){reference-type="eqref" reference="eq:tail-operator"} is an additive tail exposure. A product cocycle inserts each commutator between earlier and later blocks, and its limit additionally requires uniform memory loss and control of the internal parity bundle. identifies the forcing term but does not replace that cocycle theorem.

# Minimal directed scalar traces {#sec:directed}

The failure of two-step eigenvalues does not mean that every trace is blind. Let $\mathcal A_u$ be an analytic family in $\mathfrak S_2(H)$ and define $$\label{eq:omega}
 \Omega_{\mathcal A}(a,b,c)
 =\operatorname{tr}\left(\mathcal A_a\mathcal A_b\mathcal A_c-\mathcal A_a\mathcal A_c\mathcal A_b\right)
 =\operatorname{tr}\left(\mathcal A_a[\mathcal A_b,\mathcal A_c]\right).$$ The product is trace class. Cyclicity shows that $\Omega_{\mathcal A}$ changes sign under every transposition of $(a,b,c)$ and is invariant under cyclic rotation.

[\[thm:vandermonde\]]{#thm:vandermonde label="thm:vandermonde"} There is an analytic symmetric function $G_{\mathcal A}$ such that $$\label{eq:vandermonde-factor}
 \Omega_{\mathcal A}(a,b,c)
 =(a-b)(b-c)(c-a)G_{\mathcal A}(a,b,c).$$ On the diagonal, $$\label{eq:curvature}
 \chi_{\mathcal A}(u):=G_{\mathcal A}(u,u,u)
 =\frac12\operatorname{tr}\left(\mathcal A_u[\mathcal A_u',\mathcal A_u'']\right).$$ In particular, $$\label{eq:symmetric-curvature}
 \frac{\Omega_{\mathcal A}(u-\varepsilon,u,u+\varepsilon)}
 {2\varepsilon^3}
 =\chi_{\mathcal A}(u)+O(\varepsilon^2).$$

An analytic alternating function vanishes on each diagonal $a=b$, $b=c$, and $c=a$. Successive analytic division gives the three linear factors in [\[eq:vandermonde-factor\]](#eq:vandermonde-factor){reference-type="eqref" reference="eq:vandermonde-factor"}; the quotient is symmetric.

Expand $\mathcal A_{u+t}=\sum_{r\ge0}t^r\mathcal A_u^{(r)}/r!$. The first possible alternating term uses derivative orders $0,1,2$. Its scalar operator coefficient is $\operatorname{tr}(\mathcal A_u[\mathcal A_u',\mathcal A_u''])$, while the corresponding polynomial alternant is $$\frac12\det
 \begin{pmatrix}
 1&a-u&(a-u)^2\\
 1&b-u&(b-u)^2\\
 1&c-u&(c-u)^2
 \end{pmatrix}
 =\frac12(a-b)(b-c)(c-a).$$ This proves [\[eq:curvature\]](#eq:curvature){reference-type="eqref" reference="eq:curvature"}. The linear Taylor term of the symmetric quotient is proportional to $(a-u)+(b-u)+(c-u)$, which vanishes for the symmetric triple. Hence the relative error in [\[eq:symmetric-curvature\]](#eq:symmetric-curvature){reference-type="eqref" reference="eq:symmetric-curvature"} is quadratic.

For the one-step family, write $$\label{eq:chi-k}
 \chi_{\mathcal K}(u)=\frac12\operatorname{tr}\left(
 \mathcal K_u[\mathcal K_u',\mathcal K_u'']\right).$$ This is the minimal scalar orientation curvature. To preserve the deterministic parity architecture, define the frozen two-step family $$\label{eq:q-family}
 \mathcal Q_u=\mathcal K_u^2,
 \quad
 \mathcal Q_u'=\mathcal K_u'\mathcal K_u+\mathcal K_u\mathcal K_u',
 \quad
 \mathcal Q_u''=\mathcal K_u''\mathcal K_u+2(\mathcal K_u')^2+\mathcal K_u\mathcal K_u''.$$ Its orientation curvature is $$\label{eq:chi-q}
 \chi_{\mathcal Q}(u)=\frac12\operatorname{tr}\left(
 \mathcal Q_u[\mathcal Q_u',\mathcal Q_u'']\right).$$

[\[cor:six-step\]]{#cor:six-step label="cor:six-step"} One frozen block $\mathcal Q_a$ has no ordering, and every two-block trace and determinant is invariant under $\mathcal Q_a\mathcal Q_b\leftrightarrow\mathcal Q_b\mathcal Q_a$. The first possible parity-compatible scalar orientation is $$\label{eq:omega-six}
 \Omega_6(a,b,c)
 =\operatorname{tr}\left(\mathcal Q_a\mathcal Q_b\mathcal Q_c-\mathcal Q_a\mathcal Q_c\mathcal Q_b\right),$$ a six-step trace. It satisfies $$\Omega_6(u-\varepsilon,u,u+\varepsilon)
 =2\varepsilon^3\chi_{\mathcal Q}(u)+O(\varepsilon^5).$$

This construction also produces order-sensitive Fredholm determinants. Put $$\label{eq:directed-determinants}
 M_\to=\mathcal A_a\mathcal A_b\mathcal A_c,
 \qquad M_\leftarrow=\mathcal A_a\mathcal A_c\mathcal A_b.$$ When $\mathcal A=\mathcal K$ or $\mathcal Q$, both are trace-class Markov operators. After dividing out the Perron factor, for small $z$, $$\label{eq:det-difference}
 \log\frac{\det(I-zM_\to)}{\det(I-zM_\leftarrow)}
 =-z\Omega_{\mathcal A}(a,b,c)+O(z^2).$$ Thus three factors are not merely a convenient statistic: they are the first coefficient at which the two directed determinants can separate [@Bornemann2010; @Baladi2018].

# Directed logarithmic scales {#sec:schedule}

The Vandermonde factor determines the first possible time-oriented scale. Let $u_t$ be the schedule [\[eq:schedule\]](#eq:schedule){reference-type="eqref" reference="eq:schedule"} with real $t>0$, and fix three distinct constants $\alpha,\beta,\gamma>0$.

[\[thm:schedule\]]{#thm:schedule label="thm:schedule"} For $\mathcal A=\mathcal K$ or $\mathcal A=\mathcal Q$, $$\begin{aligned}
 &(\log T)^{3p+3}
 \Omega_{\mathcal A}(u_{\alpha T},u_{\beta T},u_{\gamma T})
 \longrightarrow
 -(\kappa p)^3\chi_{\mathcal A}(u_{\mathrm c})
 V(\log\alpha,\log\beta,\log\gamma),
 \label{eq:macro-limit}\\
 &n^3(\log n)^{3p+3}
 \Omega_{\mathcal A}(u_n,u_{n+1},u_{n+2})
 \longrightarrow-2(\kappa p)^3\chi_{\mathcal A}(u_{\mathrm c}),
 \label{eq:local-limit}\end{aligned}$$ where $$\label{eq:v-definition}
 V(x,y,z)=(x-y)(y-z)(z-x).$$ Consequently, the consecutive directed traces are absolutely summable.

Let $L=\log T$. Uniformly for fixed $\alpha>0$, $$u_{\alpha T}
 =u_{\mathrm c}+\kappa L^{-p}
 -\kappa p(\log\alpha)L^{-p-1}+O(L^{-p-2}).$$ The common $\kappa L^{-p}$ term cancels from all differences. Hence $$L^{3p+3}V(u_{\alpha T},u_{\beta T},u_{\gamma T})
 \longrightarrow-(\kappa p)^3
 V(\log\alpha,\log\beta,\log\gamma).$$ Combine this with [\[eq:vandermonde-factor\]](#eq:vandermonde-factor){reference-type="eqref" reference="eq:vandermonde-factor"} and continuity of $G_{\mathcal A}$.

For consecutive times, $$u_n-u_{n+1}
 =\frac{\kappa p}{n(\log n)^{p+1}}(1+o(1)),$$ the next difference has the same leading value, and $u_{n+2}-u_n$ has negative twice that value. This proves [\[eq:local-limit\]](#eq:local-limit){reference-type="eqref" reference="eq:local-limit"}. The resulting magnitude is bounded by a constant times $n^{-3}(\log n)^{-3p-3}$.

For the commonly used exploratory exponent $p=2$, a macroscopic scalar orientation first appears at $(\log T)^{-9}$, much smaller than the $(\log T)^{-2}$ frozen first response. By contrast, the additive commutator tail in [\[thm:pair-tail\]](#thm:pair-tail){reference-type="ref" reference="thm:pair-tail"} remains at $(\log J)^{-2}$. Time direction is therefore stronger in state--observable or cocycle insertions than in a bare three-time scalar trace.

# Midpoint convergence of orientation curvature {#sec:nystrom}

Let $K_d(u)$ be the full midpoint matrix of dimension $d$ and let primes denote its exact normalized parameter derivatives. Define $$\begin{aligned}
 \chi_{K,d}(u)
 &=\frac12\operatorname{tr}\left(K_d[K_d',K_d'']\right),\label{eq:chi-kd}\\
 Q_d&=K_d^2,
 \quad Q_d'=K_d'K_d+K_dK_d',
 \quad Q_d''=K_d''K_d+2(K_d')^2+K_dK_d'',\label{eq:qd}\\
 \chi_{Q,d}(u)
 &=\frac12\operatorname{tr}\left(Q_d[Q_d',Q_d'']\right).
 \label{eq:chi-qd}\end{aligned}$$ The exact even-state folding from @WangCycleSpectrum2026 may be used in every product without changing these traces.

[\[thm:curvature-convergence\]]{#thm:curvature-convergence label="thm:curvature-convergence"} Fix $\sigma>0$ and a compact real parameter interval. Uniformly on that interval, $$\label{eq:curvature-order}
 \chi_{K,d}(u)=\chi_{\mathcal K}(u)+O(d^{-2}),
 \qquad
 \chi_{Q,d}(u)=\chi_{\mathcal Q}(u)+O(d^{-2}).$$ For fixed $a,b,c$, the midpoint directed traces $\Omega_3$ and $\Omega_6$ have the same second-order convergence.

Each trace expands into a fixed finite-dimensional midpoint sum of products of the smooth kernels $q_u$, $\partial_uq_u$, and $\partial_u^2q_u$ around a closed cycle. Row normalizers and their first two derivatives converge at second order uniformly. Composite multidimensional midpoint quadrature then gives [\[eq:curvature-order\]](#eq:curvature-order){reference-type="eqref" reference="eq:curvature-order"} and the corresponding directed-trace estimates [@Atkinson1997; @WangCycleSpectrum2026].

# Target-independent numerical audit {#sec:numerics}

The computations use the full untruncated Gaussian formula, symmetric midpoint grids, and exact first and second score derivatives. NumPy, SciPy, and Matplotlib provide dense linear algebra and figures [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007]. The parameter $u_{\mathrm c}$ is selected by the algebraic band-merging condition [\[eq:uc\]](#eq:uc){reference-type="eqref" reference="eq:uc"}; the widths $0.03,0.05,0.08,0.12$ form an untuned grid. No arithmetic target is loaded.

## Two-step equality and first-order order response

At $d=768$, $\sigma=0.05$, and $\varepsilon=0.02$, the 22 two-step eigenvalues with modulus above $10^{-7}$ agree under reversal to $5.3\times10^{-12}$. Nevertheless, $$\left\lVert K_-K_+-K_+K_-\right\rVert_\infty=0.444002.$$ The exact stationary transport identity [\[eq:stationary-transport\]](#eq:stationary-transport){reference-type="eqref" reference="eq:stationary-transport"} holds to $4.8\times10^{-17}$.

For eleven separations from $2\times10^{-4}$ to $3\times10^{-2}$, the operator difference, stationary total variation, and one smooth observable have fitted exponents $0.99985$, $0.99988$, and $1.00010$, respectively. After division by $2\varepsilon$, the error from the analytic commutator has exponent $1.99986$. The limiting coefficients in [1](#tab:pair-response){reference-type="ref" reference="tab:pair-response"} come from the commutator and Poisson formulas, not from free fits.

::: {#tab:pair-response}
  quantity                                  fitted exponent   analytic coefficient after division by $\varepsilon$
  --------------------------------------- ----------------- ------------------------------------------------------
  $\|K_-K_+-K_+K_-\|_\infty$                      $0.99985$                                             $22.49550$
  stationary total variation                      $0.99988$                                              $9.19105$
  one smooth observable at $x\simeq0.8$           $1.00010$                                            $0.0215342$
  normalized commutator error                     $1.99986$                                                    ---

  : Small-separation two-step order response at $(u,\sigma)=(u_{\mathrm c},0.05)$ and full dimension $d=768$.
:::

![Two-step spectral blindness and operator order response. Left: matrix, stationary-law, and observable differences are first order in the half separation. Middle: forward and reverse non-Perron spectra at $\varepsilon=0.02$ coincide visually and to the quantitative tolerance in the text. Right: after subtracting $[K,K']$, the normalized operator remainder is quadratic.](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/figures/two_step_blindness.pdf>){#fig:pair width="\\textwidth"}

## Orientation curvatures and the cubic law

At $\sigma=0.05$, extrapolation through full dimension $2048$ gives $$\label{eq:numerical-curvatures}
 \chi_{\mathcal K}(u_{\mathrm c})=-1.591713748,
 \qquad
 \chi_{\mathcal Q}(u_{\mathrm c})=20.958960007.$$ Their resolution-error slopes are $-1.99714$ and $-2.00115$. Thus neither minimal directed invariant vanishes at the tested parameter. The parameter atlas in [2](#fig:curvature){reference-type="ref" reference="fig:curvature"} shows that signs and magnitudes vary strongly with $u$ and $\sigma$; the curvatures are dynamical quantities, not universal constants.

For symmetric triples, the relative errors in [\[eq:symmetric-curvature\]](#eq:symmetric-curvature){reference-type="eqref" reference="eq:symmetric-curvature"} have fitted powers $2.00013$ for $\mathcal K$ and $1.99933$ for $\mathcal Q$, confirming both the cubic Vandermonde factor and the quadratic quotient correction.

![Orientation curvature. Left and middle: one-step and frozen parity-block curvature over $1.35\le u\le1.75$; the signed logarithmic axis is linear between $-1$ and $1$. The dashed line marks $u_{\mathrm c}$. Right: relative error of the symmetric Vandermonde quotient, with the predicted $\varepsilon^2$ law.](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/figures/orientation_curvature.pdf>){#fig:curvature width="\\textwidth"}

## Resolution and logarithmic scales

The left panel of [3](#fig:schedule){reference-type="ref" reference="fig:schedule"} verifies the second-order continuum limit. For the macroscopic schedule experiment we set $$p=2,\qquad \kappa=0.5,\qquad
 (\alpha,\beta,\gamma)=(1/4,1/2,1).$$ At the finite schedule dimension $d=512$, the predicted limits of $(\log T)^9\Omega_3$ and $(\log T)^9\Omega_6$ are $1.05249$ and $-13.96417$. Direct traces through $\log T=20$ move toward those limits; the approach is slow because the next expansion is only one inverse logarithm smaller.

The paired half increment and its Euler-transformed infinite tail satisfy the constants from [\[thm:pair-tail\]](#thm:pair-tail){reference-type="ref" reference="thm:pair-tail"}: the normalized values approach $-\kappa p/4=-0.25$ and $-\kappa/4=-0.125$. This independently checks the coefficient in the renormalized commutator tail.

![Continuum and schedule scaling. Left: $d^{-2}$ convergence of both orientation curvatures. Middle: direct macroscopic traces for $p=2$ after the $(\log T)^9$ renormalization; dashed lines are the finite-resolution limits. Right: normalized within-pair increment and infinite tail converging to $-0.25$ and $-0.125$.](<../../../../../zeta_mvp0/papers/RH-8-time-ordered-cycle-curvature/figures/resolution_schedule.pdf>){#fig:schedule width="\\textwidth"}

# Consequences for the spectral program {#sec:implications}

## The route that closes

The most direct two-step proposal is now ruled out: reversing the order of two frozen Gaussian kernels cannot change a nonzero eigenvalue, its algebraic multiplicity, or any coefficient of the Fredholm determinant. Therefore a numerical difference between two such spectra is discretization, branch matching, or roundoff---not a continuum arrow of time.

This is a structural statement, not a failure of the preceding continuum spectrum. The frozen resonances and cycle determinant remain valid. What fails is the additional interpretation that one two-step spectral list can recover the orientation inside its pair.

## The route that remains

Order survives in three increasingly demanding objects:

1.  the commutator $[\mathcal K,\mathcal K']$, observed through states, stationary laws, or inserted cocycle responses;

2.  the three-factor directed determinant, whose first distinguishing coefficient is $\Omega_3$; and

3.  the parity-compatible six-step determinant generated by three two-step blocks.

The commutator tail is the largest of these for a logarithmic drive, but it is traceless and state dependent. Turning it into a universal scalar requires a controlled cocycle, an observable, or an additional block. The bare scalar orientation is target independent but starts at $(\log T)^{-3p-3}$.

For a possible Hilbert--Pólya route, this paper therefore replaces a vague "time-ordered spectrum" with falsifiable requirements. A later object must retain at least three-factor order, survive the relevant continuum and small-noise limits, and eventually acquire a self-adjoint or scattering interpretation with a correct counting law and arithmetic trace side. None of those later properties follows from the nonzero curvatures in [\[eq:numerical-curvatures\]](#eq:numerical-curvatures){reference-type="eqref" reference="eq:numerical-curvatures"}. In particular, no Riemann-zero conclusion is drawn.

# Conclusion

Two-step Gaussian quadratic products remember order in their action but not in their nonzero spectrum. The exact $AB$--$BA$ identity makes every two-step eigenvalue and determinant reversal blind. At the same time, a first-order commutator changes stationary measures and weak observables, and its accumulated logarithmic pair tail has an explicit nonzero renormalized limit.

The first scalar orientation invariant requires three parameter values. Its Vandermonde factorization produces the intrinsic curvature $\frac12\operatorname{tr}(\mathcal A[\mathcal A',\mathcal A''])$. Applied to $\mathcal K_u^2$, it yields a minimal parity-compatible six-step trace. Macroscopic logarithmic orientation is cubic in parameter differences, while consecutive orientation is summable.

These results are a useful negative gate and a constructive replacement. A route through raw paired eigenphases closes; a route through commutator insertions and directed determinants remains mathematically defined. Whether that route survives small noise or admits a self-adjoint arithmetic lift is a separate question.

# Data and code availability {#data-and-code-availability .unnumbered}

The manuscript source, tests, machine-readable results, and figure scripts are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-8-time-ordered-cycle-curvature>. Exact reproduction commands are listed in the accompanying README.

# Acknowledgments {#acknowledgments .unnumbered}

The author acknowledges the use of an AI language model for assistance with mathematical cross-checking, code auditing, manuscript organization, and typesetting. The author verified the final arguments and assumes responsibility for the content.
