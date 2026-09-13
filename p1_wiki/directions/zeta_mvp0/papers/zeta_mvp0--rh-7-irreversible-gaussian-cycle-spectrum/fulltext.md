---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-7-irreversible-gaussian-cycle-spectrum"
canonical_tex: "zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/irreversible-gaussian-cycle-spectrum.pdf"
source_sha256: "219f821de288a156b3d4c116645695aedc1ccf780173a7cfe6553c27f8171067"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Irreversible Resonance Geometry of Gaussian Quadratic Markov Operators Exact Folding, Dobrushin Enclosures, and Centered Cycle Determinants

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/irreversible-gaussian-cycle-spectrum.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The fixed-noise Gaussian quadratic Markov operator has a rigorous continuum spectrum, but convergence of finite matrices does not identify the internal structure of that spectrum. We derive exact reductions, contraction enclosures, and branch-free spectral invariants for the normalized kernel centered at $f_u(x)=1-u x^2$ on $[-1,1]$.

  Because every kernel row depends on the source only through $x^2$, the range of the operator is even. Folding the destination states $y$ and $-y$ gives a positive Markov operator on $[0,1]$ whose spectrum, generalized eigenspaces, and algebraic multiplicities agree with the full operator away from zero. For the unreduced signed-state chain, the oriented three-cycle affinity is the exact polynomial $$\log\frac{q(x,y)q(y,z)q(z,x)}{q(x,z)q(z,y)q(y,x)}
   =\frac{u}{\sigma^2}(x-y)(y-z)(z-x).$$ Thus the chain is reversible with respect to a positive density if and only if $u=0$; in particular, for $u\ne0$ no positive weighted-$L^2$ self-adjoint realization exists.

  The one-step Dobrushin coefficient is evaluated exactly as the total variation distance between two endpoint truncated normal laws. More strongly, if $\delta_n$ is the coefficient of the $n$-step kernel, then $$r_\perp=\max_{\lambda\ne1}|\lambda|
   =\lim_{n\to\infty}\delta_n^{1/n},$$ so the multistep coefficients form computable resonance enclosures converging to the non-Perron spectral radius.

  After subtracting the stationary rank-one projector, the centered operator $\mathcal N$ is Hilbert--Schmidt and $\mathcal N^n$ is trace class for $n\ge2$. Its power traces are centered cycle integrals, $$c_n=\operatorname{tr}\mathcal N^n
   =\int q(x_0,x_1)\cdots q(x_{n-1},x_0)\,d\boldsymbol{x}-1
   =\sum_{j\ge1}\lambda_j^n.$$ They generate the regularized determinant $\det_2(I-z\mathcal N)$, whose zeros are the reciprocal non-Perron resonances. An exact score formula gives $c_n'(u)$ without selecting or tracking individual eigenvalue branches, and midpoint Nyström traces and their derivatives converge at order $d^{-2}$.

  Target-independent computations recover this second-order law, verify the folding reduction to near machine precision, exhibit the noisy remnant of the deterministic $-1$ parity mode, and show that centered traces remain smooth through numerically ill-conditioned resonance collisions. These resonances are decay modes of a nonself-adjoint Markov operator. They are not identified with Riemann zeros or self-adjoint energies.
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
  **Irreversible Resonance Geometry of Gaussian** **Quadratic Markov Operators**\
  Exact Folding, Dobrushin Enclosures, and Centered Cycle Determinants
```

## Markdown 正文

**Keywords:** Markov resonance; nonreversibility; Dobrushin coefficient; Hilbert--Schmidt operator; regularized determinant; cycle trace; quadratic map.

**MSC 2020:** 47A10; 47B10; 47G10; 60J10; 37H20; 65R20.

# Introduction

Finite transition matrices can display stable complex eigenvalues without revealing whether those values are intrinsic, reversible, or robust under branch collisions. The distinction matters especially for nonnormal Markov operators: a visually continuous eigenvalue path can become badly conditioned, and sorting eigenvalues by modulus is not a spectral invariant. Trace powers and Fredholm determinants provide a complementary description that is symmetric in the eigenvalues and remains analytic when individual branches exchange labels [@Kato1995; @Simon2005; @Bornemann2010].

The prime-dynamics program began with a deterministic-chaos model of sieve words [@Wang2026Published]. Subsequent work separated exact symbolic and parity statements from conjectural arithmetic interpretations. At the first quadratic band-merging parameter $$\label{eq:uc}
 u_{\mathrm c}^3-2u_{\mathrm c}^2+2u_{\mathrm c}-2=0,
 \qquad u_{\mathrm c}=1.543689012692\ldots,$$ the deterministic map has a period-two decomposition and a Koopman eigenfunction with eigenvalue $-1$ [@WangParity2026]. A later audit showed why smooth counting laws and conjugate symmetry can create excellent but non-diagnostic zero fits [@WangObstructions2026].

For the Gaussian-smoothed finite matrices, exact parameter derivatives, occupation-weighted response formulas, and second-order resolution scaling were then obtained [@WangGaussianResponse2026]. The continuum step was completed in @WangContinuum2026: at fixed physical width $\sigma>0$, the normalized Gaussian kernel is a compact strongly positive analytic Markov family on $C([-1,1])$, and midpoint Nyström matrices recover every nonzero isolated resonance without nonzero spectral pollution.

The present paper begins the intrinsic spectral analysis of that continuum operator. Three questions are basic.

1.  Can the exact quadratic symmetry reduce the nonzero eigenproblem?

2.  Can irreversibility and the non-Perron spectral radius be described quantitatively rather than inferred from a complex eigenvalue plot?

3.  Is there a branch-free trace object that survives eigenvalue collisions and can support later order-sensitive spectral work?

The answers are respectively an exact folding to $[0,1]$, an explicit cycle affinity together with a convergent Dobrushin hierarchy, and a centered Hilbert--Schmidt determinant generated by periodic kernel integrals. The cycle determinant is analogous in architecture, but not in arithmetic content, to dynamical determinants used for hyperbolic systems [@Ruelle1976; @Baladi2018]. No prime-orbit identity is asserted here.

## Main results {#main-results .unnumbered}

1.  Every nonzero generalized eigenfunction is even. The folded Markov operator on $[0,1]$ has exactly the nonzero spectrum of the signed-state operator, including algebraic multiplicity. The same statement is exact for every even-dimensional midpoint matrix.

2.  The normalized boundary factors cancel from every oriented three-cycle ratio. The resulting affinity is $u(x-y)(y-z)(z-x)/\sigma^2$, which proves reversibility precisely at $u=0$ and excludes a self-adjoint realization in any positive stationary weighted $L^2$ space when $u\ne0$.

3.  The one-step Dobrushin coefficient has a closed truncated-normal formula. The $n$-step roots $\delta_n^{1/n}$ converge to the largest modulus of the non-Perron spectrum; they are not merely sufficient upper bounds.

4.  The centered operator $\mathcal N=\mathcal K-\Pi$ is Hilbert--Schmidt. For $n\ge2$, its trace $c_n$ is both a closed noisy-cycle integral and the absolutely convergent power sum of the non-Perron resonances. The regularized determinant $\det_2(I-z\mathcal N)$ is therefore an intrinsic spectral object.

5.  Centered trace derivatives are cyclic score expectations. They stay analytic through eigenvalue collisions and avoid left--right normalization of individual nonnormal eigenvectors.

6.  Midpoint approximations of each fixed $c_n$ and $c_n'$ converge at order $d^{-2}$. Numerical experiments recover slopes between $-1.97$ and $-2.01$ for the reported traces and responses.

## Scope {#scope .unnumbered}

All operator statements concern fixed $\sigma>0$. The numerical widths $0.03,0.05,0.08,0.12$ are a target-independent geometric grid; no zeta zero, zero table, fitted arithmetic scale, or inherited target-informed width is loaded. The determinant zeros are reciprocal Markov resonances. A compact nonnormal contraction is structurally different from the unbounded self-adjoint operator sought in the Hilbert--Pólya program [@Edwards1974; @BerryKeating1999; @Connes1999].

# The Gaussian operator and exact folding {#sec:folding}

Let $I=[-1,1]$, fix $\sigma>0$, and define $$\begin{aligned}
 f_u(x)&=1-u x^2,\label{eq:map}\\
 w_u(x,y)&=\exp\left[-\frac{(y-f_u(x))^2}{2\sigma^2}\right],\label{eq:weight}\\
 Z_u(x)&=\int_Iw_u(x,z)\,dz,
 \qquad q_u(x,y)=\frac{w_u(x,y)}{Z_u(x)}.\label{eq:kernel}\end{aligned}$$ The Markov operator on observables is $$\label{eq:operator}
 (\mathcal K_u g)(x)=\int_Iq_u(x,y)g(y)\,dy.$$ The kernel is smooth and strictly positive on $I^2$. Thus $\mathcal K_u$ is a compact strongly positive contraction on $C(I)$, $\mathcal K_u\mathbf 1=\mathbf 1$, the Perron root is algebraically simple, and every other spectral value has modulus strictly below one [@Schaefer1974; @WangContinuum2026].

## Stationary centering

[\[prop:stationary\]]{#prop:stationary label="prop:stationary"} There is a unique invariant probability $\pi_u$, and it has a smooth strictly positive density $\rho_u$ with respect to Lebesgue measure. On $H=L^2(I,dx)$ define $$\varpi_u(g)=\int_I\rho_u(x)g(x)\,dx,
 \qquad \Pi_u g=\varpi_u(g)\mathbf 1,
 \qquad \mathcal N_u=\mathcal K_u-\Pi_u.$$ Then $$\Pi_u^2=\Pi_u,
 \qquad \mathcal K_u\Pi_u=\Pi_u\mathcal K_u=\Pi_u,
 \qquad \mathcal N_u^n=\mathcal K_u^n-\Pi_u \quad(n\ge1).$$ The nonzero spectrum of $\mathcal N_u$ is precisely $\operatorname{spec}(\mathcal K_u)\setminus\{1\}$, with algebraic multiplicity.

Strong positivity and compactness give a unique invariant probability by the dual Krein--Rutman theorem. If $\pi_u$ is invariant, then $$\pi_u(dy)=\left(\int_Iq_u(x,y)\,d\pi_u(x)\right)dy.$$ The expression in parentheses is smooth and strictly positive. This proves the density assertion. Invariance gives $\varpi_u\mathcal K_u=\varpi_u$, while $\mathcal K_u\mathbf 1=\mathbf 1$; the projection identities follow. The direct decomposition $H=\operatorname{span}\{\mathbf 1\}\oplus\ker\varpi_u$ is invariant. On its first summand $\mathcal N_u=0$, and on the second $\mathcal N_u=\mathcal K_u$, which proves the spectral statement.

## The folded state space

Let $C_{\rm even}(I)$ be the even continuous functions and define the isometric isomorphism $$E:C([0,1])\longrightarrow C_{\rm even}(I),
 \qquad (Eh)(x)=h(|x|).$$ For $r,s\in[0,1]$ put $$\label{eq:folded-kernel}
 p_u(r,s)=q_u(r,s)+q_u(r,-s),
 \qquad
 (\mathcal P_u h)(r)=\int_0^1p_u(r,s)h(s)\,ds.$$ Since $p_u>0$ and its rows integrate to one, $\mathcal P_u$ is itself a compact strongly positive Markov operator.

[\[thm:folding\]]{#thm:folding label="thm:folding"} The operator $\mathcal K_u$ maps all of $C(I)$ into $C_{\rm even}(I)$, and $$\label{eq:intertwining}
 \mathcal K_uE=E\mathcal P_u.$$ Every generalized eigenspace of $\mathcal K_u$ belonging to $\lambda\ne0$ is even. Consequently, $$\label{eq:folded-spectrum}
 \operatorname{spec}(\mathcal K_u)\setminus\{0\}
 =\operatorname{spec}(\mathcal P_u)\setminus\{0\},$$ including algebraic multiplicities and Jordan structure.

The identity $f_u(-x)=f_u(x)$ implies $q_u(-x,y)=q_u(x,y)$, so $\mathcal K_ug$ is even for every $g$. If $g=Eh$, split the integral in [\[eq:operator\]](#eq:operator){reference-type="eqref" reference="eq:operator"} into negative and positive halves and reflect the negative variable. This gives [\[eq:intertwining\]](#eq:intertwining){reference-type="eqref" reference="eq:intertwining"}.

Let $Q:C(I)\to C(I)/C_{\rm even}(I)$ be the quotient map. Since the range of $\mathcal K_u$ is even, the induced quotient operator is zero. If $(\mathcal K_u-\lambda I)^m g=0$ and $\lambda\ne0$, applying $Q$ gives $(-\lambda)^mQg=0$, hence $g$ is even. Restriction to the even subspace and the similarity [\[eq:intertwining\]](#eq:intertwining){reference-type="eqref" reference="eq:intertwining"} now identify every nonzero generalized eigenspace.

There is an exact finite-dimensional counterpart. For even $d=2m$, let $$c_j=-1+\frac{2}{d}\left(j-\frac12\right),
 \qquad
 K_{ij}^{(d)}(u)=
 \frac{w_u(c_i,c_j)}{\sum_{k=1}^dw_u(c_i,c_k)}.$$ Index the positive centers increasingly by $s_j=c_{m+j}$. The folded matrix is $$\label{eq:folded-matrix}
 P_{ij}^{(d)}=K_{m+i,m+j}^{(d)}+K_{m+i,m+1-j}^{(d)},
 \qquad 1\le i,j\le m.$$ The same block argument proves that $P^{(d)}$ contains every nonzero eigenvalue of $K^{(d)}$, while the row-reflection symmetry forces at least $m$ zero eigenvalues of the full matrix. Folding therefore reduces dense storage by a factor four and dense eigensolver work by approximately a factor eight without discarding a nonzero resonance.

# Irreversibility and contraction geometry {#sec:irreversibility}

## An exact three-cycle obstruction

For three states $x,y,z\in I$, define the oriented cycle affinity $$\label{eq:affinity-def}
 \mathcal A_u(x,y,z)
 =\log\frac{q_u(x,y)q_u(y,z)q_u(z,x)}
 {q_u(x,z)q_u(z,y)q_u(y,x)}.$$ The row normalizers occur once in each orientation and cancel.

[\[thm:affinity\]]{#thm:affinity label="thm:affinity"} For every $x,y,z\in I$, $$\label{eq:affinity}
 \mathcal A_u(x,y,z)
 =\frac{u}{\sigma^2}(x-y)(y-z)(z-x).$$ The Gaussian quadratic chain is reversible with respect to a positive density if and only if $u=0$.

After cancellation of the normalizers, $-2\sigma^2\mathcal A_u$ is $$\begin{aligned}
 &(y-f_u(x))^2+(z-f_u(y))^2+(x-f_u(z))^2\\
 &\quad -(z-f_u(x))^2-(y-f_u(z))^2-(x-f_u(y))^2.\end{aligned}$$ The pure squares cancel, leaving $$\mathcal A_u=\frac{1}{\sigma^2}
 \{f_u(x)(y-z)+f_u(y)(z-x)+f_u(z)(x-y)\}.$$ The constant terms in $f_u=1-u(\cdot)^2$ cancel and the remaining alternating polynomial factors as [\[eq:affinity\]](#eq:affinity){reference-type="eqref" reference="eq:affinity"}.

If detailed balance holds, multiplication of $\rho(x)q(x,y)=\rho(y)q(y,x)$ around any three-cycle gives $\mathcal A_u=0$ [@Kelly1979; @Norris1997]. For $u\ne0$, any three distinct states contradict this condition. If $u=0$, the row density is independent of $x$; taking that common row as $\rho$ gives detailed balance.

[\[cor:no-selfadjoint\]]{#cor:no-selfadjoint label="cor:no-selfadjoint"} If $u\ne0$, there is no strictly positive density $r$ for which $\mathcal K_u$ is self-adjoint on $L^2(I,r(x)dx)$.

Self-adjointness of the integral operator in the weighted space would imply $$r(x)q_u(x,y)=r(y)q_u(y,x)$$ almost everywhere. Continuity promotes the identity to all $(x,y)$, contradicting [\[thm:affinity\]](#thm:affinity){reference-type="ref" reference="thm:affinity"}.

The corollary is specific to self-adjointness by a positive change of density. It does not say that every resonance must be nonreal, nor does it exclude an unrelated self-adjoint operator constructed by adding new degrees of freedom. It does exclude the direct identification of this Markov kernel with a weighted self-adjoint Hamiltonian.

## An exact Dobrushin coefficient

Write a row with Gaussian mean $m$ as $$\label{eq:qmean}
 q_m(y)=\frac{\exp(-(y-m)^2/(2\sigma^2))}{Z_\sigma(m)},
 \qquad
 Z_\sigma(m)=\int_{-1}^1\exp(-(y-m)^2/(2\sigma^2))\,dy,$$ and let $F_m$ be its distribution function on $I$. The possible means are the interval with endpoints $1-u$ and $1$. Put $$a=\min(1-u,1),\qquad b=\max(1-u,1).$$ For $u\ne0$ define $$\label{eq:crossing}
 y_*=\frac{a+b}{2}+\frac{\sigma^2}{b-a}
 \log\frac{Z_\sigma(b)}{Z_\sigma(a)}.$$

For a Markov kernel $Q$, use the total-variation convention $$\label{eq:dobrushin}
 \delta(Q)=\frac12\sup_{x,x'}\int_I|Q(x,dy)-Q(x',dy)|.$$ Let $q_u^{(n)}$ be the $n$-step density and $\delta_n=\delta(\mathcal K_u^n)$.

[\[thm:dobrushin\]]{#thm:dobrushin label="thm:dobrushin"} If $u=0$, then $\delta_1=0$. If $u\ne0$, then $y_*\in(-1,1)$ and $$\label{eq:delta-exact}
 \delta_1=F_a(y_*)-F_b(y_*).$$ Let $$\label{eq:rperp}
 r_\perp=\max\{|\lambda|:\lambda\in\operatorname{spec}(\mathcal K_u),\ \lambda\ne1\},$$ with $r_\perp=0$ if there is no nonzero non-Perron eigenvalue. Then $$\label{eq:dobrushin-limit}
 r_\perp
 =\lim_{n\to\infty}\delta_n^{1/n}
 =\inf_{n\ge1}\delta_n^{1/n}.$$ In particular, every $n$ gives the certified enclosure $|\lambda|\le\delta_n^{1/n}$ for all $\lambda\ne1$.

Apart from a factor absorbed into the normalizer, $$q_m(y)=\frac{e^{my/\sigma^2}e^{-y^2/(2\sigma^2)}}
 {\int_Ie^{mt/\sigma^2}e^{-t^2/(2\sigma^2)}dt}.$$ Thus $\{q_m\}$ is a strict monotone-likelihood-ratio family. For $m_1<m_2$, the ratio $q_{m_2}/q_{m_1}$ is strictly increasing and crosses one exactly once. Solving the crossing equation for the endpoint pair $(a,b)$ gives [\[eq:crossing\]](#eq:crossing){reference-type="eqref" reference="eq:crossing"}. Hence $$\operatorname{TV}(q_{m_1},q_{m_2})
 =\max_t\{F_{m_1}(t)-F_{m_2}(t)\}.$$ Stochastic ordering gives $F_a\ge F_{m_1}\ge F_{m_2}\ge F_b$ pointwise, so the largest pairwise distance occurs at $(a,b)$ and [\[eq:delta-exact\]](#eq:delta-exact){reference-type="eqref" reference="eq:delta-exact"} follows.

Let $M(I)$ be the finite signed measures with total-variation norm and $M_0(I)=\{\nu:\nu(I)=0\}$. The Dobrushin coefficient is exactly the operator norm of $\mathcal K_u^*$ restricted to $M_0(I)$ [@Seneta2006]. Therefore $$\delta_n=\left\lVert (\mathcal K_u^*|_{M_0})^n\right\rVert.$$ The Gelfand formula gives the limit in [\[eq:dobrushin-limit\]](#eq:dobrushin-limit){reference-type="eqref" reference="eq:dobrushin-limit"}; submultiplicativity gives the infimum identity. Since the adjoint of a compact operator is compact, every nonzero spectral value is an eigenvalue. The simplicity of the Perron root and the identity $\mathcal K_u^*\nu=\lambda\nu\Rightarrow(1-\lambda)\nu(I)=0$ show that the spectrum on $M_0$ is exactly the non-Perron spectrum.

For small $\sigma$, the endpoint rows can have exponentially small overlap, so $\delta_1$ is mathematically below one but numerically indistinguishable from one. Equation [\[eq:dobrushin-limit\]](#eq:dobrushin-limit){reference-type="eqref" reference="eq:dobrushin-limit"} shows that this is a limitation of a one-step minorization argument, not evidence for a peripheral resonance. The dynamics can create substantial overlap after several iterates.

# Centered cycle traces and the regularized determinant {#sec:traces}

The kernel $q_u$ belongs to $L^2(I^2)$, so [\[eq:operator\]](#eq:operator){reference-type="eqref" reference="eq:operator"} defines a Hilbert--Schmidt operator on $H=L^2(I,dx)$. The nonzero spectra on $H$ and $C(I)$ agree: if $\mathcal K_ug=\lambda g$ in $H$ and $\lambda\ne0$, then $g=\lambda^{-1}\mathcal K_ug$ is smooth; the same induction applies to generalized eigenvectors.

Enumerate the nonzero non-Perron resonances by $\lambda_1,\lambda_2,\ldots$, including algebraic multiplicity.

[\[thm:trace\]]{#thm:trace label="thm:trace"} For every integer $n\ge2$, the operator $\mathcal N_u^n$ is trace class and $$\begin{aligned}
 c_n(u):=\operatorname{tr}\mathcal N_u^n
 &=\operatorname{tr}\mathcal K_u^n-1\label{eq:centered-trace}\\
 &=\int_{I^n}\prod_{j=0}^{n-1}q_u(x_j,x_{j+1})
 \,dx_0\cdots dx_{n-1}-1\label{eq:cycle-integral}\\
 &=\sum_{j\ge1}\lambda_j(u)^n,
 \qquad x_n=x_0.\label{eq:power-sum}\end{aligned}$$ The series in [\[eq:power-sum\]](#eq:power-sum){reference-type="eqref" reference="eq:power-sum"} is absolutely convergent.

Both $\mathcal K_u$ and the rank-one $\Pi_u$ are Hilbert--Schmidt, hence so is $\mathcal N_u$. The product of two Hilbert--Schmidt operators is trace class, so $\mathcal N_u^n$ is trace class for $n\ge2$ [@Simon2005]. By [\[prop:stationary\]](#prop:stationary){reference-type="ref" reference="prop:stationary"}, $\mathcal N_u^n=\mathcal K_u^n-\Pi_u$ and $\operatorname{tr}\Pi_u=\varpi_u(\mathbf 1)=1$.

The trace of a product of two Hilbert--Schmidt integral operators is the integral of the corresponding paired kernels. Iteration and Fubini's theorem give the closed cycle integral [\[eq:cycle-integral\]](#eq:cycle-integral){reference-type="eqref" reference="eq:cycle-integral"}. Finally, Lidskii's trace theorem applied to the trace-class operator $\mathcal N_u^n$ gives the absolutely convergent eigenvalue sum. Spectral mapping and [\[prop:stationary\]](#prop:stationary){reference-type="ref" reference="prop:stationary"} identify its nonzero eigenvalues as $\lambda_j^n$.

Because $\mathcal N_u$ is Hilbert--Schmidt, its two-regularized determinant is the entire function $$\label{eq:det2}
 \mathcal D_u(z)=\det{}_2(I-z\mathcal N_u)
 =\prod_{j\ge1}(1-z\lambda_j)e^{z\lambda_j}.$$

[\[cor:determinant\]]{#cor:determinant label="cor:determinant"} The nonzero zeros of $\mathcal D_u$ are exactly $z=\lambda_j^{-1}$, with algebraic multiplicity. For sufficiently small $|z|$, $$\label{eq:logdet}
 \log\mathcal D_u(z)=-\sum_{n=2}^{\infty}\frac{c_n(u)}{n}z^n.$$

This is a noisy-cycle determinant in a precise operator-theoretic sense. It does not require a symbolic periodic-orbit coding: the coefficient $c_n+1$ is the total weight of all closed $n$-step kernel paths integrated over their base points.

## Branch-free parameter response

Define the centered score $$\label{eq:score}
 s_u(x,y)=\partial_u\log q_u(x,y)
 =-\frac{x^2}{\sigma^2}(y-f_u(x))
 -\int_Iq_u(x,t)\left[-\frac{x^2}{\sigma^2}(t-f_u(x))\right]dt.$$ Then $\partial_uq_u=q_us_u$ and every row score has mean zero [@WangGaussianResponse2026; @WangContinuum2026].

[\[thm:trace-response\]]{#thm:trace-response label="thm:trace-response"} For $n\ge2$, the map $u\mapsto c_n(u)$ is real analytic and $$\begin{aligned}
 c_n'(u)
 &=n\operatorname{tr}(\mathcal K_u'\mathcal K_u^{n-1})\label{eq:trace-derivative}\\
 &=n\int_{I^n}s_u(x_0,x_1)
 \prod_{j=0}^{n-1}q_u(x_j,x_{j+1})
 \,d\boldsymbol{x}.
 \label{eq:score-cycle}\end{aligned}$$ For sufficiently small $|z|$, $$\label{eq:det-response}
 \partial_u\log\mathcal D_u(z)
 =-\sum_{n=2}^{\infty}\frac{c_n'(u)}{n}z^n.$$ These formulas remain analytic at parameters where individual eigenvalue branches collide or exchange labels.

The kernel and all its $u$ derivatives are uniformly bounded on compact parameter intervals, so $u\mapsto\mathcal K_u$ is analytic in Hilbert--Schmidt norm. Differentiate $\operatorname{tr}\mathcal K_u^n$. Cyclicity of the trace makes its $n$ summands equal and gives [\[eq:trace-derivative\]](#eq:trace-derivative){reference-type="eqref" reference="eq:trace-derivative"}. Substituting $\mathcal K_u'(x,y)=q_u(x,y)s_u(x,y)$ and writing the product kernel gives [\[eq:score-cycle\]](#eq:score-cycle){reference-type="eqref" reference="eq:score-cycle"}. Termwise differentiation of [\[eq:logdet\]](#eq:logdet){reference-type="eqref" reference="eq:logdet"} in its disk of convergence proves [\[eq:det-response\]](#eq:det-response){reference-type="eqref" reference="eq:det-response"}. Analyticity follows at the operator level and therefore does not depend on a local labeling of the roots [@Kato1995].

## Second-order midpoint cycle traces

Let $K_d(u)$ be the midpoint matrix in [2](#sec:folding){reference-type="ref" reference="sec:folding"}, set $h=2/d$, and define $$\label{eq:discrete-traces}
 c_{n,d}(u)=\operatorname{tr}K_d(u)^n-1,
 \qquad
 c_{n,d}'(u)=n\operatorname{tr}\left(K_d'(u)K_d(u)^{n-1}\right).$$

[\[thm:nystrom-traces\]]{#thm:nystrom-traces label="thm:nystrom-traces"} Fix $\sigma>0$, an integer $n\ge2$, and a compact real parameter interval. Then, uniformly on that interval, $$\label{eq:trace-order}
 c_{n,d}(u)=c_n(u)+O(h^2),
 \qquad
 c_{n,d}'(u)=c_n'(u)+O(h^2).$$ The same quantities are obtained by replacing $K_d$ with its folded matrix $P_d$.

Write $$Z_{d,u}(x)=h\sum_{j=1}^dw_u(x,c_j),
 \qquad q_{d,u}(x,c_j)=\frac{w_u(x,c_j)}{Z_{d,u}(x)}.$$ Then $K_{ij}^{(d)}=h q_{d,u}(c_i,c_j)$. Composite midpoint quadrature and its parameter derivative give $q_{d,u}=q_u+O(h^2)$ at all grid pairs, uniformly in $u$. Expanding the matrix trace as a closed $n$-fold sum yields $$\operatorname{tr}K_d^n
 =h^n\sum_{i_0,\ldots,i_{n-1}}
 \prod_{j=0}^{n-1}q_{d,u}(c_{i_j},c_{i_{j+1}}),
 \qquad i_n=i_0.$$ This is the $n$-dimensional midpoint rule for the smooth integrand in [\[eq:cycle-integral\]](#eq:cycle-integral){reference-type="eqref" reference="eq:cycle-integral"}, with a uniform $O(h^2)$ normalization perturbation [@Atkinson1997]. Differentiation gives the same argument for the score integral. Finally, the full and folded matrices have identical nonzero spectra, so their trace powers agree.

# Target-independent numerical spectrum {#sec:numerics}

All computations use the full, untruncated Gaussian kernel and symmetric midpoint grids. The implementation uses NumPy, SciPy, and Matplotlib [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007]. Machine-readable tables, tests, and plotting scripts accompany the manuscript.

The algebraic parameter [\[eq:uc\]](#eq:uc){reference-type="eqref" reference="eq:uc"} is selected by deterministic quadratic dynamics, not by arithmetic data. The widths $$\sigma\in\{0.03,0.05,0.08,0.12\}$$ were fixed before the spectral scan. The code contains no zero ordinates, and the output metadata explicitly records that no target data were loaded.

## Folding and the resonance atlas

At full dimension $d=192$ and $\sigma=0.12$, reflected rows agree to $8.3\times10^{-17}$. All eleven folded eigenvalues with modulus above $10^{-4}$ match full-matrix eigenvalues within $2.3\times10^{-13}$. The smallest computed eigenvalues are less reliable, as expected for a rapidly smoothing compact operator, but they do not affect the exact algebraic folding theorem.

At $u_{\mathrm c}$, the leading resonances are shown in [1](#tab:leading){reference-type="ref" reference="tab:leading"}. A real negative eigenvalue is dominant for every displayed width and moves inward as the noise increases. This is the natural noisy remnant of the exact deterministic parity eigenvalue $-1$ proved in @WangParity2026; the present computation does not claim a small-noise perturbation theorem for its discontinuous parity eigenfunction.

::: {#tab:leading}
   $\sigma$   leading resonance              next conjugate pair
  ---------- ------------------- -------------------------------------------
    $0.03$     $-0.9719815645$         $-0.1898526749\pm0.5238126201i$
    $0.05$     $-0.9588415868$         $-0.0267942799\pm0.5884576680i$
    $0.08$     $-0.9373468211$         $-0.0030793741\pm0.4620424167i$
    $0.12$     $-0.9073047454$    $\phantom{-}0.0078301206\pm0.2416781243i$

  : Leading non-Perron resonances at $u=u_{\mathrm c}$ from the folded matrix with full dimension $d=768$. The complex value represents a conjugate pair.
:::

![Intrinsic resonance atlas. Upper left: non-Perron spectra at the algebraic band-merging parameter for four untuned widths. Upper right: ordered resonance moduli over $1.35\le u\le1.75$ at $\sigma=0.05$ and $d=512$; ordering by modulus is descriptive and is not branch tracking. Lower left: centered cycle traces remain smooth while roots rearrange. Lower right: the largest left--right condition number among the eight leading finite-matrix eigenvalues, illustrating increasing branch sensitivity. The dashed vertical line marks $u_{\mathrm c}$.](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/figures/resonance_atlas.pdf>){#fig:atlas width="\\textwidth"}

The upper-right panel of [1](#fig:atlas){reference-type="ref" reference="fig:atlas"} displays several rank exchanges. A fine local inspection shows real-to-complex collisions near the interval $1.66$--$1.68$. These are numerical exceptional-point candidates, not a continuum existence theorem. The condition-number growth explains why a single sorted branch can be unstable there. In contrast, the lower-left panel shows the symmetric trace combinations $c_2,\ldots,c_5$ varying smoothly, as guaranteed by [\[thm:trace-response\]](#thm:trace-response){reference-type="ref" reference="thm:trace-response"}.

## Second-order centered traces

We computed $c_n$ and $c_n'$ for $2\le n\le6$ at dimensions from $128$ to $2048$. A quadratic fit in $h^2$ over $d\ge384$ supplied the continuum intercept; log--log slopes use $d\ge256$. The results in [\[tab:trace-fits,fig:trace-convergence\]](#tab:trace-fits,fig:trace-convergence){reference-type="ref" reference="tab:trace-fits,fig:trace-convergence"} recover the predicted second order without fitting a resonance.

::: {#tab:trace-fits}
    $n$              $c_n(\infty)$   error slope             $c_n'(\infty)$   error slope
  ----- -------------------------- ------------- -------------------------- -------------
      2   $\phantom{-}0.265783238$      $-2.000$             $-2.113092601$      $-2.001$
      3             $-0.823917527$      $-1.990$             $-0.173893150$      $-1.992$
      4   $\phantom{-}1.087357907$      $-1.974$             $-7.144876862$      $-2.000$
      5             $-0.840572835$      $-2.002$   $\phantom{-}3.034749919$      $-2.007$
      6   $\phantom{-}0.696893094$      $-2.004$             $-2.946147729$      $-2.014$

  : Centered trace and response extrapolations at $(u,\sigma)=(u_{\mathrm c},0.05)$. Slopes are powers of the full dimension $d$.
:::

![Second-order midpoint convergence for centered cycle moments (left) and their exact parameter derivatives (right). The displayed continuum values are extrapolated from a quadratic polynomial in $h^2$; dashed lines have slope $-2$.](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/figures/trace_convergence.pdf>){#fig:trace-convergence width="\\textwidth"}

## Contraction roots and determinant zeros

For $\sigma=0.05$, the exact endpoint overlap $1-\delta_1$ is only $1.307\times10^{-53}$. Thus a one-step Dobrushin estimate rounds to one in double precision even though strong positivity guarantees $\delta_1<1$. At $n=30$, the discretized enclosure has fallen to $\delta_{30}^{1/30}=0.963668$, close to the folded non-Perron radius $0.958873$. For $\sigma=0.12$, the corresponding values are $0.913918$ and $0.907317$. These finite calculations illustrate the exact limit in [\[thm:dobrushin\]](#thm:dobrushin){reference-type="ref" reference="thm:dobrushin"}; they are not used to prove it.

The right panel of [3](#fig:determinant){reference-type="ref" reference="fig:determinant"} evaluates the finite regularized product $$\mathcal D_d(z)=\prod_{j\ge1}(1-z\lambda_{j,d})e^{z\lambda_{j,d}}$$ from the folded spectrum. The visible depressions coincide with the marked reciprocal resonances. Unlike an eigenvalue plot, the determinant is a single analytic scalar and its logarithmic Taylor coefficients are exactly the centered traces.

![Left: multistep Dobrushin roots and finite-matrix non-Perron radii at $u=u_{\mathrm c}$, $d=512$. The roots decrease toward the dashed spectral radii. Right: $\log|\det_2(I-zN_d)|$ at $\sigma=0.05$, with crosses at reciprocals of resonances having modulus above $0.1$.](<../../../../../zeta_mvp0/papers/RH-7-irreversible-gaussian-cycle-spectrum/figures/dobrushin_determinant.pdf>){#fig:determinant width="\\textwidth"}

# Implications for a longer spectral program {#sec:program}

## What has been gained

The continuum theorem of @WangContinuum2026 established that finite nonzero resonances converge. The present results identify their internal organization. Half of the signed state is redundant for the nonzero eigenproblem; the remaining operator is genuinely irreversible; its outer spectral radius has a convergent total-variation enclosure; and all of its resonances are encoded by one centered determinant.

The trace response is especially useful for subsequent non-autonomous work. An individual nonnormal eigenvalue requires a simple isolated branch and a left--right normalization. The scalar $c_n(u)$ is analytic without either choice. For a slowly varying or order-sensitive product, centered cycle traces and determinant ratios therefore offer a more stable primitive than sorting instantaneous eigenphases.

## Why this is not a Hilbert--Pólya operator

The Hilbert--Pólya idea seeks a self-adjoint spectral realization of the nontrivial zero ordinates. Any successful realization would need, at a minimum, a real discrete spectrum, an appropriate high-energy counting law, and a trace or scattering formula carrying arithmetic prime-power data [@Edwards1974; @BerryKeating1999; @Connes1999]. The present operator has none of these properties automatically:

1.  $\mathcal K_u$ is a compact nonself-adjoint contraction and its eigenvalues accumulate at zero inside the unit disk;

2.  [\[thm:affinity\]](#thm:affinity){reference-type="ref" reference="thm:affinity"} rules out detailed balance and hence rules out the direct positive-weight symmetrization of $\mathcal K_u$ for $u\ne0$;

3.  the coefficients in [\[eq:cycle-integral\]](#eq:cycle-integral){reference-type="eqref" reference="eq:cycle-integral"} are smooth geometric kernel integrals, not von Mangoldt-weighted prime sums; and

4.  the zeros of [\[eq:det2\]](#eq:det2){reference-type="eqref" reference="eq:det2"} are reciprocal decay resonances, generally complex, not real energy levels.

Two standard constructions do not bridge this gap by themselves. The multiplicative reversiblization $\mathcal K_u^*\mathcal K_u$ is positive and self-adjoint, but it records singular values and discards resonance phases. A unitary dilation of a contraction introduces extra states and is not a canonical discrete Hamiltonian with the required counting law. Either construction may be analytically useful, but self-adjointness alone is not a zero theorem.

## A disciplined sequence of next questions

The centered determinant suggests a route of questions rather than a claimed construction:

1.  Extend $c_n$ from frozen kernels to parity-resolved two-step products, preserving temporal order and proving a continuum limit.

2.  Analyze the small-noise limit in a function space adapted to the deterministic two-component geometry, including the fate of the noisy $-1$ resonance.

3.  Determine whether a target-independent scaling limit of determinant ratios has a unitary or scattering interpretation. Complex Markov phases alone are insufficient.

4.  Before any arithmetic comparison, derive a trace identity whose geometric side naturally produces prime-power weights. Importing zero data into $\sigma$, $u$, or the unfolding would invalidate this test.

5.  Only after a self-adjoint generator, real spectrum, counting law, and arithmetic trace identity are established should one test zero ordinates out of sample.

The present paper supplies the frozen intrinsic determinant needed for **S1**; it does not supply **S3**--**S5**. Stating those gaps is part of the result, because it prevents a Markov resonance plot from being mistaken for a Hilbert--Pólya construction.

# Conclusion

The fixed-noise Gaussian quadratic operator has an exact and computable resonance geometry. Its quadratic source symmetry folds every nonzero generalized eigenspace to $[0,1]$. Its signed-state dynamics are irreversible for every $u\ne0$, with an oriented cycle affinity that is independent of the row normalizers. Its Dobrushin roots converge to, rather than merely bound, the non-Perron spectral radius.

After stationary centering, the operator is Hilbert--Schmidt and its powers have closed cycle traces. These traces generate a regularized determinant, admit exact score derivatives, remain analytic through branch collisions, and converge under midpoint discretization at second order. The target-independent experiments recover each of these numerical consequences and identify the dominant negative resonance as a finite-noise continuation of the deterministic parity geometry at the level of evidence, not theorem.

The resulting determinant is a rigorous transfer-operator spectral object. It is not a self-adjoint energy determinant, contains no proved arithmetic trace formula, and does not identify or constrain Riemann zeros. Its role is to provide a stable next layer on which order-sensitive and small-noise questions can be posed precisely.

# Data and code availability {#data-and-code-availability .unnumbered}

The manuscript source, tested implementation, machine-readable results, and figure scripts are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-7-irreversible-gaussian-cycle-spectrum>. The exact reproduction command is listed in the accompanying README.

# Acknowledgments {#acknowledgments .unnumbered}

The author acknowledges the use of an AI language model for assistance with mathematical cross-checking, code auditing, manuscript organization, and typesetting. The author verified the final arguments and assumes responsibility for the content.
