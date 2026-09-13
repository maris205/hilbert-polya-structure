---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-5-renormalized-gaussian-response"
canonical_tex: "zeta_mvp0/papers/RH-5-renormalized-gaussian-response/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-5-renormalized-gaussian-response/renormalized-gaussian-response.pdf"
source_sha256: "4d365f33929cf1389179c73cfa1e4c4495322e3d0dc760b4c6a4f45df2a22612"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Renormalized Spectral Response of Gaussian Quadratic Transfer Matrices Exact Derivatives, Occupation Weighting, and Resolution Scaling

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-5-renormalized-gaussian-response>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-5-renormalized-gaussian-response/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-5-renormalized-gaussian-response/renormalized-gaussian-response.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-5-renormalized-gaussian-response/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-5-renormalized-gaussian-response/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Logarithmically driven quadratic maps have been studied numerically through Gaussian-smoothed finite transition matrices. A preceding analysis proved that an unweighted fixed-resolution operator average freezes at the limiting matrix and that its first nonzero renormalized term is a parameter derivative. The numerical construction, however, accumulates probability flow and then normalizes each source row. This produces an occupation-weighted matrix rather than the unweighted operator average. We determine exactly when the two have the same response.

  For the row-stochastic Gaussian kernel of the quadratic map $f_u(x)=1-u x^2$, we derive closed formulas for the first and second parameter derivatives. Both derivative matrices have zero row sums. If a fixed Gaussian window is retained and renormalized, its exact rowwise $\ell^1$ error is twice the omitted probability mass. These identities give direct finite-difference, normalization, and truncation tests.

  For an unanchored schedule $u_n=u_{\mathrm c}+\kappa(\log(n+c))^{-p}+O((\log n)^{-p-1})$, we prove a weighted slow-variation theorem. At fixed dimension, every bounded collection of source weights with positive time density has the same leading response: $$(\log T)^p\bigl(Q_T-K(u_{\mathrm c})\bigr)\longrightarrow \kappa K'(u_{\mathrm c}),$$ row by row, even when the weights are endogenous. A finite-state non-autonomous Markov estimator inherits this limit in probability under the same occupation condition. Endpoint anchoring is different. Its leading term is of order $(\log T)^{-p-1}$ and contains a diagonal matrix of rowwise logarithmic-age moments; it is generally not the unweighted response.

  At fixed physical Gaussian width, midpoint discretization and its first two parameter derivatives converge at second order, while fixed-window storage still grows quadratically with grid dimension. Scaling the width with one grid cell gives linear storage but changes the limiting operator and destroys the fixed-norm derivative hypothesis. Sparse experiments through dimension $50{,}000$ verify all finite-matrix identities, resolve a stable nonreal resonance and its eigenphase derivative, and exhibit second-order grid convergence. No Riemann-zero ordinates are loaded or compared in these experiments. The benchmark width is inherited from a target-informed exploratory scale and is not an arithmetic prediction; no spectral realization of the zeros is claimed.
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
  **Renormalized Spectral Response of Gaussian**\
  **Quadratic Transfer Matrices**\
  Exact Derivatives, Occupation Weighting, and Resolution Scaling
```

## Markdown 正文

**Keywords:** quadratic map; transfer matrix; logarithmic schedule; linear response; non-autonomous Markov chain; sparse eigenvalue problem; occupation measure.

**MSC 2020:** 37M25; 37H20; 47A55; 65P20; 60J10.

# Introduction

The prime-dynamics program began with a numerical correspondence between prime-sieve words and low-dimensional quadratic dynamics [@Wang2026Published]. Subsequent work separated exact symbolic statements from admissibility hypotheses, constructed an exact prime kneading orbit after sparse repair, and isolated the period-two mode at the relevant band-merging parameter [@WangReformulation2026; @WangPrimeSpectrum2026; @WangParity2026]. These results concern sieve words, kneading coordinates, and observable spectral measures.

A different numerical direction extracts complex eigenvalues from transition matrices associated with a logarithmically driven quadratic map and compares their phases with low-lying Riemann-zero ordinates [@WangSpectralFlow2026]. A theoretical audit established several exact limitations of such comparisons [@WangObstructions2026]. In particular, joint pair occupation is not a conditional transition matrix, static sorted phase unwrapping is an identity, conjugate doubling forces a zero regression intercept, and a smooth Riemann--von Mangoldt envelope can already produce excellent relative errors. That audit also identified a positive object: for a differentiable finite matrix family $A(u)$, $$(\log T)^p\left(\frac1T\sum_{n\le T}A(u_n)-A(u_{\mathrm c})\right)
  \longrightarrow \kappa A'(u_{\mathrm c}).$$

The remaining gap is structural. The motivating computation does not average the matrices $K(u_n)$ uniformly. It propagates a source distribution, accumulates the flows $\nu_{n,i}K_{ij}(u_n)$, and only then normalizes each source row. The resulting row weights are generated by the same dynamics. Pointwise continuity of $K$ alone does not identify the limit.

This paper closes that gap at fixed finite resolution for the unanchored logarithmic schedule. The mechanism is not mixing but slow variation: $(\log n)^{-p}$ is asymptotically constant over every positive-density portion of $\{1,\ldots,T\}$. Consequently any bounded source weights whose total is comparable to $T$ preserve the same first derivative. The theorem applies pathwise to deterministic expected flows and, after a martingale estimate, in probability to a finite-state inhomogeneous Markov trajectory.

Endpoint anchoring reveals a complementary effect. Subtracting the terminal value cancels the common slowly varying part. The next coefficient remembers where in the observation window each source row was occupied. It is a logarithmic-age moment and need not be common across rows. Thus anchoring improves the nominal decay rate while making occupation bias visible at the leading surviving order.

## Main results {#main-results .unnumbered}

The contributions are as follows.

1.  The Gaussian row kernel has exact score formulas for $K'$ and $K''$. Both derivative matrices annihilate $\mathbf 1$, providing stringent implementation checks.

2.  Renormalizing a hard Gaussian cutoff changes row $i$ by exactly $2q_i$ in $\ell^1$, where $q_i$ is the omitted full-kernel mass.

3.  The row-normalized expected-flow matrix differs from the unweighted average by an exact rowwise covariance between source occupation and the instantaneous kernel.

4.  For the unanchored logarithmic schedule, every bounded weighting with positive density has the same first response. The result is uniform over all such weight arrays and does not require the weights to be independent of the dynamics.

5.  A finite-state time-inhomogeneous Markov estimator has sampling error $O_{\mathbb P}(T^{-1/2})$, which is smaller than every logarithmic response scale. Positive source occupation therefore suffices to transfer the deterministic response to the empirical estimator, and the condition is automatic for the full fixed-dimensional Gaussian kernel on a compact parameter interval.

6.  For endpoint anchoring, the leading row-$i$ coefficient is $p\kappa\beta_i$, where $\beta_i$ is a logarithmic-age moment. For weights proportional to $(n/T)^a$, one has $\beta_i=(a+1)^{-1}$.

7.  Fixed physical noise and cell-scaled noise are different continuum paths. The former gives second-order midpoint consistency but quadratic fixed-window storage; the latter gives linear storage while approaching deterministic composition in a smooth-observable topology.

## Scope {#scope .unnumbered}

All derivative and truncation results, together with the weighted response and finite-state Markov results, are finite-dimensional theorems. The fixed-width midpoint statement concerns a specified smooth integral kernel. No theorem here identifies that kernel with a natural self-adjoint operator, and a row-stochastic Gaussian matrix is not a quantum Hamiltonian. The numerical section performs no new target fit and evaluates no zeta zero, but its inherited width is not target-independent. Nothing here makes a statement about the Riemann hypothesis.

# Four finite-time operators and an exact covariance identity {#sec:four}

Let $d\ge2$, let $K_n\in\mathbb R^{d\times d}$ be row stochastic, and let $\nu_n$ be a row probability vector. In the non-autonomous Markov interpretation, $$\nu_{n+1}=\nu_n K_n.$$ There are four natural but generally different finite-time objects: $$\begin{aligned}
  \overline K_T&=\frac1T\sum_{n=1}^T K_n,
  \label{eq:unweighted-average}\\
  C_T&=\frac1T\sum_{n=1}^T\operatorname{diag}(\nu_n)K_n,
  \label{eq:flow-matrix}\\
  Q_T&=D_T^{-1}C_T,\qquad
  D_T=\operatorname{diag}\left(\frac1T\sum_{n=1}^T\nu_n\right),
  \label{eq:weighted-kernel}\\
  \Pi_T&=K_1K_2\cdots K_T.
  \label{eq:product}\end{aligned}$$ The last convention acts on row distributions. The matrix $C_T$ is expected joint flow, $Q_T$ is its row-conditional normalization, and $\Pi_T$ retains operator order. Their spectra need not agree.

Write $K_{n,i\bullet}$ for row $i$, and define $$\overline\nu_{i,T}=\frac1T\sum_{n=1}^T\nu_{n,i}.$$

[\[prop:covariance\]]{#prop:covariance label="prop:covariance"} If $\overline\nu_{i,T}>0$, then $$\label{eq:covariance}
  Q_{T,i\bullet}-\overline K_{T,i\bullet}
  =
  \frac{
    T^{-1}\sum_{n=1}^T
    (\nu_{n,i}-\overline\nu_{i,T})
    (K_{n,i\bullet}-\overline K_{T,i\bullet})
  }{\overline\nu_{i,T}}.$$ Thus occupation weighting is absent exactly when the displayed rowwise covariance vanishes.

Expand the numerator in [\[eq:covariance\]](#eq:covariance){reference-type="eqref" reference="eq:covariance"}. It equals $$\frac1T\sum_n\nu_{n,i}K_{n,i\bullet}
  -\overline\nu_{i,T}\overline K_{T,i\bullet}.$$ Division by $\overline\nu_{i,T}$ gives [\[eq:weighted-kernel\]](#eq:weighted-kernel){reference-type="eqref" reference="eq:weighted-kernel"} minus [\[eq:unweighted-average\]](#eq:unweighted-average){reference-type="eqref" reference="eq:unweighted-average"}.

[\[rem:csr\]]{#rem:csr label="rem:csr"} For a compressed sparse row matrix, the array of stored indices contains *column* indices. Correct normalization multiplies the stored values by the row factors repeated according to consecutive differences of the row pointer. Indexing row sums by the column-index array instead performs a destination-dependent rescaling and does not produce a stochastic matrix. The reproducibility implementation tests this distinction explicitly. The numerical values reported below are newly computed with row-pointer normalization and are not a reproduction of earlier phase-fit lists.

# The Gaussian quadratic family {#sec:gaussian}

Let $$I=[-1,1],\qquad
  c_i=-1+\left(i-\frac12\right)h,\qquad
  h=\frac2d,\qquad 1\le i\le d.$$ For $f_u(x)=1-u x^2$ and fixed $\sigma>0$, put $$\begin{aligned}
  m_i(u)&=f_u(c_i)=1-u c_i^2,\label{eq:mean}\\
  w_{ij}(u)&=\exp\left(
    -\frac{(c_j-m_i(u))^2}{2\sigma^2}
  \right),\label{eq:weight}\\
  K_{ij}(u)&=\frac{w_{ij}(u)}{Z_i(u)},\qquad
  Z_i(u)=\sum_{k=1}^d w_{ik}(u).
  \label{eq:kernel}\end{aligned}$$ Every entry is positive and analytic in $u$, and $K(u)\mathbf 1=\mathbf 1$.

## Exact first and second derivatives

Define $$\label{eq:score}
  a_{ij}(u)=\partial_u\log w_{ij}(u)
  =-\frac{c_i^2}{\sigma^2}\bigl(c_j-m_i(u)\bigr),
  \qquad
  \overline a_i(u)=\sum_kK_{ik}(u)a_{ik}(u).$$

[\[thm:derivatives\]]{#thm:derivatives label="thm:derivatives"} The first two derivatives of [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} are $$\begin{aligned}
  K'_{ij}(u)
  &=K_{ij}(u)\bigl(a_{ij}(u)-\overline a_i(u)\bigr),
  \label{eq:first-derivative}\\
  K''_{ij}(u)
  &=K_{ij}(u)\left[
    \bigl(a_{ij}(u)-\overline a_i(u)\bigr)^2
    -\operatorname{Var}_{K_i(u)}(a_i(u))
  \right].
  \label{eq:second-derivative}\end{aligned}$$ In particular, $$\label{eq:zero-row-sums}
  K'(u)\mathbf 1=0,\qquad K''(u)\mathbf 1=0.$$

Logarithmic differentiation of $K_{ij}=w_{ij}/Z_i$ gives $$\partial_u\log K_{ij}=a_{ij}-\overline a_i,$$ which proves [\[eq:first-derivative\]](#eq:first-derivative){reference-type="eqref" reference="eq:first-derivative"}. Moreover, $$\partial_u a_{ij}=-\frac{c_i^4}{\sigma^2}$$ is constant in $j$ for fixed row $i$. Differentiating [\[eq:first-derivative\]](#eq:first-derivative){reference-type="eqref" reference="eq:first-derivative"}, the centered contribution from $\partial_u a_{ij}$ therefore cancels. The derivative of $\overline a_i$ contributes $\operatorname{Var}_{K_i}(a_i)$, proving [\[eq:second-derivative\]](#eq:second-derivative){reference-type="eqref" reference="eq:second-derivative"}. Summing the two formulas over $j$ proves [\[eq:zero-row-sums\]](#eq:zero-row-sums){reference-type="eqref" reference="eq:zero-row-sums"}.

The formulas also identify the response scale without a finite difference. Let $Z_i$ be the row-$i$ random variable taking value $c_j-m_i(u)$ with probability $K_{ij}(u)$.

[\[prop:derivative-norms\]]{#prop:derivative-norms label="prop:derivative-norms"} For every row, $$\begin{aligned}
  \sum_j|K'_{ij}(u)|
  &=
  \frac{c_i^2}{\sigma^2}
  \mathbb E\left|Z_i-\mathbb EZ_i\right|,
  \label{eq:first-norm}\\
  \sum_j|K''_{ij}(u)|
  &=
  \frac{c_i^4}{\sigma^4}
  \mathbb E\left|
    (Z_i-\mathbb EZ_i)^2-\operatorname{Var}(Z_i)
  \right|.
  \label{eq:second-norm}\end{aligned}$$

By [\[eq:score\]](#eq:score){reference-type="eqref" reference="eq:score"}, $a_{ij}-\overline a_i=-c_i^2(Z_i-\mathbb EZ_i)/\sigma^2$. Substitution into [\[eq:first-derivative\]](#eq:first-derivative){reference-type="eqref" reference="eq:first-derivative"} and [\[eq:second-derivative\]](#eq:second-derivative){reference-type="eqref" reference="eq:second-derivative"} gives the two identities.

[\[rem:norm\]]{#rem:norm label="rem:norm"} For an interior row resolved by several cells, the typical centered displacement is of order $\sigma$. Equations [\[eq:first-norm\]](#eq:first-norm){reference-type="eqref" reference="eq:first-norm"}--[\[eq:second-norm\]](#eq:second-norm){reference-type="eqref" reference="eq:second-norm"} then give the characteristic scales $\left\lVert K'\right\rVert_\infty=O(\sigma^{-1})$ and $\left\lVert K''\right\rVert_\infty=O(\sigma^{-2})$. Thus a family with $\sigma=\sigma_d\to0$ need not have a uniformly bounded derivative in raw matrix $\ell^\infty$ norm, even though its action on smooth observables may converge. A resolution-time response theorem must specify the common operator topology.

## Exact cutoff error

Let $S_i\subset\{1,\ldots,d\}$ be a nonempty retained set for row $i$, and renormalize the full kernel on that set: $$\label{eq:truncated-kernel}
  K^S_{ij}=
  \begin{cases}
    K_{ij}/(1-q_i),&j\in S_i,\\
    0,&j\notin S_i,
  \end{cases}
  \qquad
  q_i=\sum_{j\notin S_i}K_{ij}.$$

[\[prop:tail\]]{#prop:tail label="prop:tail"} For every row, $$\label{eq:tail-identity}
  \sum_j|K_{ij}-K^S_{ij}|=2q_i.$$ Consequently $$\label{eq:tail-infinity}
  \left\lVert K-K^S\right\rVert_\infty=2\max_iq_i.$$

On the retained set, $K^S_{ij}-K_{ij}=K_{ij}q_i/(1-q_i)$, whose sum is $q_i$. The omitted entries also sum to $q_i$.

[\[rem:nonnormal\]]{#rem:nonnormal label="rem:nonnormal"} The norm estimate [\[eq:tail-infinity\]](#eq:tail-infinity){reference-type="eqref" reference="eq:tail-infinity"} is an operator statement, not an unconditional one-to-one eigenvalue bound. Gaussian Markov matrices are generally nonnormal. A simple eigenvalue has a first-order condition number determined by its left-right overlap, while a global eigenvalue enclosure requires a resolvent or a diagonalizability estimate [@Kato1995; @StewartSun1990].

## Simple resonance and eigenphase response

Let $\lambda(u)\ne0$ be a simple eigenvalue near $u=u_{\mathrm c}$, with $$K(u_{\mathrm c})r=\lambda r,\qquad
  \ell^*K(u_{\mathrm c})=\lambda\ell^*,\qquad
  \ell^*r=1.$$ Analytic matrix perturbation theory gives $$\label{eq:eigen-derivative}
  \lambda'(u_{\mathrm c})=\ell^*K'(u_{\mathrm c})r,
  \qquad
  \theta'(u_{\mathrm c})=
  \operatorname{Im}\frac{\ell^*K'(u_{\mathrm c})r}{\lambda},
  \quad \theta=\operatorname{Arg}\lambda.$$ These are responses of a finite Markov resonance. They do not turn its phase into an energy.

# Weighted logarithmic response {#sec:weighted}

Put $$L_T=\log(T+c),\qquad s_T=L_T^{-p},$$ where $c>1$ and $p>0$. The following uniform weighted form of slow variation is the key step. It is a concrete Cesaro property of a slowly varying sequence [@BinghamGoldieTeugels1987].

[\[lem:weighted-slow\]]{#lem:weighted-slow label="lem:weighted-slow"} Let $0\le a_{n,T}\le M$ and $A_T=\sum_{n=1}^T a_{n,T}\ge\alpha T$ for fixed $M,\alpha>0$. Then, uniformly over all such triangular weight arrays, $$\label{eq:weighted-slow}
  \frac1{A_T}\sum_{n=1}^Ta_{n,T}
  \frac{L_T^p}{(\log(n+c))^p}
  \longrightarrow1.$$ The same assertion holds with $p$ replaced by every positive exponent.

The ratio in [\[eq:weighted-slow\]](#eq:weighted-slow){reference-type="eqref" reference="eq:weighted-slow"} is at least one. Therefore its weighted mean excess is bounded by $$\frac{M}{\alpha}
  \left[
    \frac1T\sum_{n=1}^T
    \frac{L_T^p}{(\log(n+c))^p}-1
  \right].$$ The bracket tends to zero by the logarithmic Cesaro asymptotic $$\frac1T\sum_{n=1}^T(\log(n+c))^{-p}
  =L_T^{-p}\bigl(1+O(L_T^{-1})\bigr).$$

Consider $$\label{eq:unanchored-schedule}
  u_n=u_{\mathrm c}+\delta_n,\qquad
  \delta_n=
  \frac{\kappa}{(\log(n+c))^p}
  +O\left((\log(n+c))^{-p-1}\right).$$ The error is assumed uniform in $n$ once a fixed initial segment is removed. For each source row $i$, allow arbitrary weights $a_{n,i,T}\in[0,M]$ and set $$\label{eq:general-weighted-row}
  Q_{T,i\bullet}
  =
  \frac{\sum_{n=1}^T a_{n,i,T}K_{i\bullet}(u_n)}
       {\sum_{n=1}^T a_{n,i,T}}.$$

[\[thm:unanchored\]]{#thm:unanchored label="thm:unanchored"} Assume $K(u)$ is differentiable at $u_{\mathrm c}$ and bounded along the schedule. For fixed $d$, suppose that for every row $$\label{eq:positive-density}
  \sum_{n=1}^T a_{n,i,T}\ge\alpha_iT$$ for all sufficiently large $T$, with $\alpha_i>0$. Then $$\label{eq:unanchored-response}
  L_T^p\bigl(Q_T-K(u_{\mathrm c})\bigr)
  \longrightarrow \kappa K'(u_{\mathrm c})$$ in matrix infinity norm. The conclusion is uniform over all weights satisfying the displayed bounds.

Differentiability gives, row by row, $$K_{i\bullet}(u_{\mathrm c}+t)
  =K_{i\bullet}(u_{\mathrm c})+tK'_{i\bullet}(u_{\mathrm c})+r_i(t),
  \qquad
  \frac{\left\lVert r_i(t)\right\rVert_1}{|t|}\longrightarrow0.$$ By [\[lem:weighted-slow\]](#lem:weighted-slow){reference-type="ref" reference="lem:weighted-slow"}, the weighted mean of $\delta_n/s_T$ converges to $\kappa$. Applying the same lemma with exponent $p+1$ shows that the error term in [\[eq:unanchored-schedule\]](#eq:unanchored-schedule){reference-type="eqref" reference="eq:unanchored-schedule"} contributes $O(L_T^{-1})$ after division by $s_T$.

For the Taylor remainder, fix $\varepsilon>0$ and choose $N$ so that $\left\lVert r_i(\delta_n)\right\rVert_1\le\varepsilon|\delta_n|$ for $n\ge N$. The first $N-1$ terms contribute $O((Ts_T)^{-1})=o(1)$ after weighted normalization, while the remaining terms are bounded by $\varepsilon$ times a uniformly bounded weighted mean of $|\delta_n|/s_T$. Letting $\varepsilon\downarrow0$ proves the row limit. Since $d$ is fixed, the maximum over rows gives [\[eq:unanchored-response\]](#eq:unanchored-response){reference-type="eqref" reference="eq:unanchored-response"}.

[\[cor:expected-flow\]]{#cor:expected-flow label="cor:expected-flow"} Let $\nu_n$ be any sequence of source probability vectors and put $a_{n,i,T}=\nu_{n,i}$. If $$\liminf_{T\to\infty}\frac1T\sum_{n=1}^T\nu_{n,i}>0$$ for every fixed row, then the row-normalized expected-flow matrix [\[eq:weighted-kernel\]](#eq:weighted-kernel){reference-type="eqref" reference="eq:weighted-kernel"} satisfies [\[eq:unanchored-response\]](#eq:unanchored-response){reference-type="eqref" reference="eq:unanchored-response"}. No independence, stationarity, or mixing of the weights is required.

This corollary applies directly to a propagated probability cloud. A single random trajectory adds transition noise, handled next.

[\[cor:markov\]]{#cor:markov label="cor:markov"} Let $(X_n)$ be a finite-state time-inhomogeneous Markov chain with $$\mathbb P(X_{n+1}=j\mid X_1,\ldots,X_n)
  =K_{X_nj}(u_n).$$ Define source counts and the empirical conditional matrix by $$\begin{aligned}
  N_{i,T}&=\sum_{n=1}^T\mathbf1_{\{X_n=i\}},\\
  \widehat K_{ij,T}
  &=\frac{\sum_{n=1}^T
    \mathbf1_{\{X_n=i,X_{n+1}=j\}}}{N_{i,T}}.\end{aligned}$$ Suppose that for every $i$ there is $\alpha_i>0$ such that $$\label{eq:random-occupation}
  \mathbb P(N_{i,T}\ge\alpha_iT)\longrightarrow1.$$ Then $$\label{eq:markov-response}
  L_T^p\bigl(\widehat K_T-K(u_{\mathrm c})\bigr)
  \longrightarrow\kappa K'(u_{\mathrm c})$$ in probability.

Condition on the realized source indicators and define $$M_{ij,T}=\sum_{n=1}^T\mathbf1_{\{X_n=i\}}
  \left(\mathbf1_{\{X_{n+1}=j\}}-K_{ij}(u_n)\right).$$ This is a martingale with bounded increments and $\mathbb E|M_{ij,T}|^2\le T$. On the event in [\[eq:random-occupation\]](#eq:random-occupation){reference-type="eqref" reference="eq:random-occupation"}, $$\frac{M_{ij,T}}{N_{i,T}}=O_{\mathbb P}(T^{-1/2})
  =o_{\mathbb P}(L_T^{-p}).$$ The conditional mean term is [\[eq:general-weighted-row\]](#eq:general-weighted-row){reference-type="eqref" reference="eq:general-weighted-row"} with $a_{n,i,T}=\mathbf1_{\{X_n=i\}}$, so [\[thm:unanchored\]](#thm:unanchored){reference-type="ref" reference="thm:unanchored"} applies on the same event. There are finitely many entries.

[\[cor:gaussian-occupation\]]{#cor:gaussian-occupation label="cor:gaussian-occupation"} Fix $d<\infty$ and $\sigma>0$, and let the parameters $u_n$ remain in a compact interval $J$. For the full kernel [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}, the occupation conditions in [\[cor:expected-flow,cor:markov\]](#cor:expected-flow,cor:markov){reference-type="ref" reference="cor:expected-flow,cor:markov"} hold automatically. Consequently both conclusions apply without a separate occupation hypothesis.

Continuity, strict positivity, and finiteness give $$\varepsilon=\min_{u\in J}\min_{i,j}K_{ij}(u)>0.$$ For a propagated source distribution, $\nu_{n+1,i}=\sum_j\nu_{n,j}K_{ji}(u_n)\ge\varepsilon$. For a Markov trajectory, put $p_{n,i}=\mathbb P(X_n=i\mid X_1,\ldots,X_{n-1})\ge\varepsilon$. The sum $$\sum_{n=2}^T\bigl(\mathbf1_{\{X_n=i\}}-p_{n,i}\bigr)$$ is a bounded-increment martingale and is $o_{\mathbb P}(T)$. Thus $N_{i,T}/T\ge\varepsilon+o_{\mathbb P}(1)$.

[\[rem:occupation-limit\]]{#rem:occupation-limit label="rem:occupation-limit"} At fixed $d$, strict Gaussian positivity makes positive occupation plausible, and [\[cor:gaussian-occupation\]](#cor:gaussian-occupation){reference-type="ref" reference="cor:gaussian-occupation"} makes it automatic for the full kernel. A hard sparse cutoff introduces exact zeros, so its occupation condition must again be checked. In either case, the lower bound is not uniform for free when $d\to\infty$: source probabilities must sum to one, so a common lower density cannot remain independent of $d$. The theorem therefore closes the fixed-resolution occupation gap but does not interchange the long-time and continuum limits.

# Endpoint anchoring exposes logarithmic age {#sec:anchored}

For a triangular schedule ending exactly at $u_{\mathrm c}$, define $$\label{eq:anchored-schedule}
  u_{n,T}=u_{\mathrm c}+\delta_{n,T},\qquad
  \delta_{n,T}=\kappa\left[
    \frac1{(\log(n+c))^p}-\frac1{L_T^p}
  \right].$$ The unweighted average has coefficient $p\kappa L_T^{-p-1}$. Weighted rows need not have the same coefficient.

For row weights $a_{n,i,T}$, let $$\label{eq:log-age}
  r_{n,T}=\log\frac{T+c}{n+c},\qquad
  \beta_{i,T}=
  \frac{\sum_{n=1}^Ta_{n,i,T}r_{n,T}}
       {\sum_{n=1}^Ta_{n,i,T}}.$$

[\[thm:anchored\]]{#thm:anchored label="thm:anchored"} Assume the boundedness and positive-density conditions of [\[thm:unanchored\]](#thm:unanchored){reference-type="ref" reference="thm:unanchored"}. Suppose in addition that, for every row, $$\label{eq:age-assumptions}
  \beta_{i,T}\longrightarrow\beta_i,\qquad
  \frac{\sum_{n=1}^Ta_{n,i,T}r_{n,T}^2}
       {\sum_{n=1}^Ta_{n,i,T}}=O(1).$$ If $K$ is differentiable at $u_{\mathrm c}$, then $$\label{eq:anchored-matrix-response}
  L_T^{p+1}\bigl(Q_T-K(u_{\mathrm c})\bigr)
  \longrightarrow p\kappa B K'(u_{\mathrm c}),
  \qquad
  B=\operatorname{diag}(\beta_1,\ldots,\beta_d).$$

Since $\log(n+c)=L_T-r_{n,T}$, Taylor expansion gives $$(\log(n+c))^{-p}-L_T^{-p}
  =p\,r_{n,T}L_T^{-p-1}
   +O(r_{n,T}^2L_T^{-p-2})$$ whenever $n\ge T^{1/2}$. The total weighted contribution of $n<T^{1/2}$ is $o(L_T^{-p-1})$ because the weights are bounded and their denominator is at least $\alpha_iT$. Averaging the expansion and using [\[eq:age-assumptions\]](#eq:age-assumptions){reference-type="eqref" reference="eq:age-assumptions"} yields $$\frac{\sum_na_{n,i,T}\delta_{n,T}}{\sum_na_{n,i,T}}
  =
  \frac{p\kappa\beta_i+o(1)}{L_T^{p+1}}.$$ The differentiability remainder is handled as in [\[thm:unanchored\]](#thm:unanchored){reference-type="ref" reference="thm:unanchored"}; the weighted mean absolute displacement has the same $O(L_T^{-p-1})$ scale under [\[eq:age-assumptions\]](#eq:age-assumptions){reference-type="eqref" reference="eq:age-assumptions"}. This proves each row of [\[eq:anchored-matrix-response\]](#eq:anchored-matrix-response){reference-type="eqref" reference="eq:anchored-matrix-response"}.

[\[cor:power\]]{#cor:power label="cor:power"} If $a_{n,i,T}=(n/T)^{a_i}$ with $a_i\ge0$, then $$\label{eq:power-age}
  \beta_i=
  \frac{\int_0^1x^{a_i}(-\log x)\,dx}
       {\int_0^1x^{a_i}\,dx}
  =\frac1{a_i+1}.$$ The unweighted row has $\beta_i=1$, while a row occupied later in the window has $\beta_i<1$.

Both weighted sums in [\[eq:log-age\]](#eq:log-age){reference-type="eqref" reference="eq:log-age"}, after division by $T$, are improper Riemann sums with integrable logarithmic moments. The displayed integrals equal $(a_i+1)^{-2}$ and $(a_i+1)^{-1}$, respectively.

[\[cor:anchored-eigen\]]{#cor:anchored-eigen label="cor:anchored-eigen"} Let $\lambda\ne0$ be a simple eigenvalue of $K(u_{\mathrm c})$ with normalized left and right eigenvectors $\ell,r$. Under [\[thm:anchored\]](#thm:anchored){reference-type="ref" reference="thm:anchored"}, the corresponding eigenvalue $\lambda_T$ of $Q_T$ satisfies $$\begin{aligned}
  L_T^{p+1}(\lambda_T-\lambda)
  &\longrightarrow p\kappa\,\ell^*BK'(u_{\mathrm c})r,\label{eq:anchored-eigen}\\
  L_T^{p+1}(\operatorname{Arg}\lambda_T-\operatorname{Arg}\lambda)
  &\longrightarrow
  p\kappa\,\operatorname{Im}
  \frac{\ell^*BK'(u_{\mathrm c})r}{\lambda}.
  \label{eq:anchored-phase}\end{aligned}$$ Only when $B$ is scalar on the relevant rows does this reduce to the unweighted anchored coefficient.

# Resolution scaling and the sparsity tradeoff {#sec:resolution}

## Fixed physical width

For fixed $\sigma>0$, define the continuum Markov operator on $I=[-1,1]$ by $$\label{eq:continuum-kernel}
  (\mathcal K_{\sigma,u}g)(x)=
  \frac{\int_{-1}^1
    e^{-(y-f_u(x))^2/(2\sigma^2)}g(y)\,dy}
       {\int_{-1}^1
    e^{-(y-f_u(x))^2/(2\sigma^2)}\,dy}.$$ The full matrix [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} is its midpoint quotient quadrature.

[\[prop:midpoint\]]{#prop:midpoint label="prop:midpoint"} Let $u$ range over a compact interval and keep $\sigma>0$ fixed. For every $g\in C^2(I)$, $$\label{eq:midpoint}
  \max_i\left|
    \sum_jK_{ij}^{(d,\sigma)}(u)g(c_j)
    -(\mathcal K_{\sigma,u}g)(c_i)
  \right|
  \le C_{\sigma,u}\,h^2\left\lVert g\right\rVert_{C^2}.$$ The same conclusion holds after one or two parameter derivatives, with constants depending on $\sigma$ and the compact parameter interval.

Multiply numerator and denominator of [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} by $h$. Composite midpoint quadrature has error $O(h^2)$ for the smooth numerator and denominator integrands. The continuum denominator is uniformly positive for $x\in I$ and $u$ in a compact interval. The quotient estimate follows. Parameter differentiation only multiplies the Gaussian by smooth polynomials in $x,y$, so the same argument applies twice.

This proposition concerns the full Gaussian sum. A fixed $L\sigma$ cutoff adds the explicit error from [\[prop:tail\]](#prop:tail){reference-type="ref" reference="prop:tail"}. To converge to the exact full kernel in operator norm as $d\to\infty$, the omitted mass must also be sent to zero; choosing $L=6$ makes it numerically small but not mathematically zero.

## Fixed width is not asymptotically sparse

Suppose a support fixed at $u=u_{\mathrm c}$ retains every center in $$|c_j-m_i(u_{\mathrm c})|\le L\sigma+\Delta c_i^2,$$ where $\Delta$ covers a parameter neighborhood. An interval of radius $R$ contains at most $1+2R/h$ midpoint centers.

[\[prop:storage\]]{#prop:storage label="prop:storage"} Assume $u_{\mathrm c}\in(0,2)$. The number of retained entries satisfies $$\label{eq:nnz-bound}
  \operatorname{nnz}(K)
  \le d\left(1+\frac{2(L\sigma+\Delta)}h\right).$$ For fixed positive $\sigma$ and fixed $L$, a positive fraction of interior rows has $\Theta(d)$ retained entries, so $\operatorname{nnz}(K)=\Theta(d^2)$. If instead $\sigma_d=qh$ and $\Delta_d=O(h)$, then $\operatorname{nnz}(K)=O(d)$.

The upper bound follows from counting grid centers in each retained interval and using $c_i^2\le1$. For fixed $\sigma$, rows whose means stay a fixed distance from the boundary retain an interval of fixed positive length, hence $\Theta(d)$ centers. If $\sigma_d$ and $\Delta_d$ are $O(h)$, the parenthesis in [\[eq:nnz-bound\]](#eq:nnz-bound){reference-type="eqref" reference="eq:nnz-bound"} is bounded independently of $d$.

[\[rem:two-paths\]]{#rem:two-paths label="rem:two-paths"} At fixed $\sigma$, [\[prop:midpoint\]](#prop:midpoint){reference-type="ref" reference="prop:midpoint"} approaches the noisy integral operator [\[eq:continuum-kernel\]](#eq:continuum-kernel){reference-type="eqref" reference="eq:continuum-kernel"}. If $\sigma_d=qh\to0$, then for every continuous $g$ and every row whose image remains in $I$, the Gaussian average concentrates and approaches $g(f_u(c_i))$. The limit is deterministic composition on smooth observables. Meanwhile [\[prop:derivative-norms\]](#prop:derivative-norms){reference-type="ref" reference="prop:derivative-norms"} shows why raw matrix derivative norms can grow. Linear storage is therefore obtained by changing both the limiting operator and the topology in which response can remain bounded. It is not a cheaper discretization of the same fixed-noise limit.

# Reproducible sparse experiments {#sec:experiments}

## Protocol

The implementation uses the exact formulas [\[eq:first-derivative\]](#eq:first-derivative){reference-type="eqref" reference="eq:first-derivative"}--[\[eq:second-derivative\]](#eq:second-derivative){reference-type="eqref" reference="eq:second-derivative"} on a support pattern fixed at $u_{\mathrm c}$. Fixing the pattern prevents artificial finite-difference jumps when an entry crosses the cutoff. All matrices are compressed sparse row arrays. The tests verify:

1.  row sums of $K$, $K'$, and $K''$ are $1$, $0$, and $0$;

2.  analytic derivatives agree with centered finite differences;

3.  sparse full-support output agrees with an independent dense reference;

4.  cutoff error obeys [\[eq:tail-identity\]](#eq:tail-identity){reference-type="eqref" reference="eq:tail-identity"};

5.  row-pointer normalization differs from column-index rescaling; and

6.  weighted schedule coefficients approach the limits in [\[thm:unanchored,thm:anchored\]](#thm:unanchored,thm:anchored){reference-type="ref" reference="thm:unanchored,thm:anchored"}.

All ten tests pass.

The benchmark parameters are $$u_{\mathrm c}=1.5437,\qquad \sigma=0.00785,\qquad L=6.$$ The width is retained from the exploratory numerical scale only as a fixed-noise benchmark. That historical scale was obtained in target-informed zero-fitting scans, so it is not a prediction. No zero ordinate is loaded, optimized against, or compared in the present experiments. For each $d$, we build $K,K',K''$, time seven matrix-vector products, and compute 12 eigenvalues of largest modulus using implicitly restarted Arnoldi iteration [@LehoucqSorensenYang1998; @VirtanenEtAl2020]. We choose the largest-modulus nonreal branch in the open upper half-plane, compute its left and right eigenvectors, and compare [\[eq:eigen-derivative\]](#eq:eigen-derivative){reference-type="eqref" reference="eq:eigen-derivative"} with a two-sided parameter step $2\times10^{-6}$. NumPy and Matplotlib provide array and plotting infrastructure [@HarrisEtAl2020; @Hunter2007].

The server has one NUMA node, 32 physical cores and 64 hardware threads of an Intel Xeon Platinum 8163, 125 GiB of RAM, and no GPU. OpenBLAS was limited to 16 threads. Timings are wall-clock values from one run and should be read as reproducibility measurements rather than architecture-independent complexity constants.

## Finite-matrix validation and scaling

::: {#tab:benchmark}
           $d$                 nnz   matrix MiB   build s    matvec s     eigs s   peak GiB          response error
  ------------ ------------------- ------------ --------- ----------- ---------- ---------- -----------------------
     $2{,}000$         $177{,}434$       $2.04$   $0.072$   $0.00023$    $0.029$    $0.112$   $2.44{\times}10^{-8}$
     $5{,}000$     $1{,}108{,}946$      $12.71$   $0.201$   $0.00161$    $0.144$    $0.124$   $2.44{\times}10^{-8}$
    $10{,}000$     $4{,}435{,}902$      $50.80$   $0.445$   $0.00752$    $0.774$    $0.274$   $2.42{\times}10^{-8}$
    $20{,}000$    $17{,}743{,}554$     $203.14$   $1.135$   $0.03065$    $2.668$    $0.913$   $2.43{\times}10^{-8}$
    $50{,}000$   $110{,}897{,}392$    $1269.31$   $4.439$   $0.19245$   $12.477$    $5.000$   $2.41{\times}10^{-8}$

  : Sparse fixed-width benchmark. Memory is logical CSR storage for one matrix; peak RSS includes three derivative orders, Arnoldi work arrays, and the Python runtime.
:::

Across all resolutions, the largest stochastic row-sum error is $6.7\times10^{-16}$; the largest zero-row-sum errors for $K'$ and $K''$ are $2.4\times10^{-14}$ and $8.3\times10^{-12}$. The maximum six-sigma omitted-mass diagnostic decreases from $2.68\times10^{-9}$ at $d=2000$ to $2.00\times10^{-9}$ at $d=50000$, giving a maximum rowwise $\ell^1$ difference below $5.4\times10^{-9}$. Arnoldi residuals remain below $1.4\times10^{-10}$.

shows the predicted distinction between practical sparsity and asymptotic sparsity. Only about $4.44\%$ of entries are retained, but the fraction stays constant because $\sigma$ is physical, so storage follows $d^2$. The selected branch and its phase derivative converge at the midpoint $d^{-2}$ scale: $$\begin{aligned}
  \lambda_{2000}&=-0.474026207+0.505994196\,i,\\
  \lambda_{50000}&=-0.473827646+0.506120556\,i,\\
  \theta'_{2000}&=2.302416751,\qquad
  \theta'_{50000}=2.282068196.\end{aligned}$$ The left-right overlap at the finest grid is $0.06764$ for unit-norm vectors, so the branch is moderately nonnormal but well resolved. Its analytic eigenvalue derivative and centered finite difference agree to $2.42\times10^{-8}$ relative error.

![Fixed-width resolution study. Left: CSR storage is a small fraction of dense storage but remains quadratic. Middle: measured build, Arnoldi, and matrix-vector times. Right: the selected upper-half-plane resonance and its analytic phase derivative exhibit second-order grid convergence relative to the $d=50000$ computation.](<../../../../../zeta_mvp0/papers/RH-5-renormalized-gaussian-response/figures/operator_scaling.pdf>){#fig:operator-scaling width="\\textwidth"}

## Weighted schedule scaling

For a direct scalar test of the two weighted lemmas, use $a_{n,T}=(n/T)^a$ with $a=0,1,3$, horizons from $10^3$ through $10^7$, and $p=2$. In the unanchored panel of [2](#fig:schedule-scaling){reference-type="ref" reference="fig:schedule-scaling"}, every coefficient $$\frac{L_T^p}{\kappa}
  \frac{\sum_na_{n,T}\delta_n}{\sum_na_{n,T}}$$ approaches one, although the convergence is only logarithmic. In the anchored panel, the scale is $L_T^{p+1}/(p\kappa)$ and the three limits are $1$, $1/2$, and $1/4$, exactly as in [\[cor:power\]](#cor:power){reference-type="ref" reference="cor:power"}. The finite-horizon curves also warn against treating $T=10^6$ as asymptotic: the unweighted anchored coefficient is still $1.324$ rather than $1$.

![Weighted logarithmic coefficients. Unanchored driving forgets every positive-density power weight at leading order. Endpoint anchoring removes that common term and exposes the logarithmic-age limits $1/(a+1)$. Horizontal lines show the theoretical limits.](<../../../../../zeta_mvp0/papers/RH-5-renormalized-gaussian-response/figures/schedule_scaling.pdf>){#fig:schedule-scaling width="88%"}

# Discussion {#sec:discussion}

## What has been proved beyond operator freezing

The previous fixed-resolution theorem applied to $T^{-1}\sum_nK(u_n)$. now applies to the row-normalized expected flow actually produced by propagating a probability cloud. Its assumptions are explicit: finite $d$, differentiability of the matrix family, and positive time density for every retained source row. For a full Gaussian kernel on a compact parameter interval, positivity supplies the density automatically; a hard sparse cutoff must be checked separately. For a genuinely random finite-state Gaussian chain, [\[cor:markov\]](#cor:markov){reference-type="ref" reference="cor:markov"} shows that the transition-count fluctuation is polynomially smaller than the logarithmic response. This is a rigorous positive extension, not merely a numerical observation.

The extension also has a sharp boundary. Endpoint anchoring cancels the occupation-universal part. The resulting diagonal age matrix $B$ enters before spectral perturbation, so a single scalar calibration cannot in general remove the bias. Moreover, as the partition is refined, positive occupation density and derivative bounds must be proved uniformly in the chosen operator topology. Neither follows from finite Gaussian positivity.

## What the computations do not establish

The stable quantities in [1](#fig:operator-scaling){reference-type="ref" reference="fig:operator-scaling"} are finite-noise Markov resonances. Their convergence demonstrates that the discretized object is numerically well posed at fixed $\sigma$. It does not show that its phases are self-adjoint energies, that an unbounded phase lift exists, or that its resonances encode arithmetic fluctuations. In particular:

-   no Riemann zero is loaded or compared in this study; however, $\sigma$ is inherited from a target-fitted exploratory scan and is explicitly not treated as target-independent;

-   the eigenvalues lie inside the unit disk and belong to a nonnormal stochastic matrix;

-   refining $d$ at fixed $\sigma$ approaches one noisy integral operator, whereas shrinking $\sigma$ approaches a different deterministic object; and

-   a Hilbert--Polya claim would require an independently constructed self-adjoint operator and a complete spectral identity, neither of which is supplied here.

## Next theoretical step

The present paper identifies and validates the first derivative retained by long exposure. Such an average forgets operator order. A possible next object is therefore a parity-resolved two-step cocycle or a centered trace observable that survives after subtracting the frozen operator and the occupation-age response. Any arithmetic comparison should then be made against independently unfolded zero fluctuations and under a controlled joint limit in time, resolution, and noise width. That bridge remains open.

# Conclusion

Gaussian quadratic transfer matrices admit an exact and computationally useful response calculus. Their first and second derivatives are centered score moments, hard cutoff has a twice-the-tail error, and simple resonance response follows from left-right perturbation theory. More importantly, row-normalizing accumulated flow does not destroy the first response of an unanchored logarithmic drive: positive-density source weights are too slowly varying to alter its leading coefficient. A finite-state Markov trajectory inherits the result because its sampling error is polynomially smaller.

Endpoint anchoring changes the conclusion. Once the universal slowly varying component is canceled, rowwise logarithmic age appears at leading order and modifies both eigenvalue and eigenphase response. Resolution scaling introduces a second distinction: fixed noise gives a well-defined second-order continuum discretization with quadratic storage, while cell-scaled noise gives linear storage by changing the limit and its operator topology.

The 50,000-dimensional experiments validate these finite-matrix statements without loading or comparing arithmetic target data, while retaining the declared historically target-informed width. They provide a rigorous and reproducible foundation for studying renormalized dynamical resonances, while placing no Riemann zeros in the spectrum and making no claim about the Riemann hypothesis.

# Data and code availability {#data-and-code-availability .unnumbered}

The manuscript source, tests, sparse implementation, machine-readable benchmark outputs, and figure scripts are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-5-renormalized-gaussian-response>. The exact commands are listed in the accompanying README.

# Acknowledgments {#acknowledgments .unnumbered}

The author acknowledges the use of an AI language model for assistance with mathematical cross-checking, code auditing, manuscript organization, and typesetting. The author verified the final arguments and assumes responsibility for the content.
