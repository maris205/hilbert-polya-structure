---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-caputo-fractional-dirichlet-heat-route-a"
canonical_tex: "henon_dynamics/henon_caputo_fractional_dirichlet_heat_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_caputo_fractional_dirichlet_heat_route_a/paper/main.pdf"
source_sha256: "a0f5bce8b0fd95646177de83e3c0eb3211003062403eb8642d674bc750809433"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Caputo Dirichlet Heat Flow: Sharp Smoothing, Schatten, and Resolvent Limits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_caputo_fractional_dirichlet_heat_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_caputo_fractional_dirichlet_heat_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_caputo_fractional_dirichlet_heat_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_caputo_fractional_dirichlet_heat_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the Caputo time-fractional heat equation on $(0,\pi)$ in its exact Dirichlet sine basis and prove inverse-stable subordination, positivity, and contraction for every $0<\beta\leq1$. \>0 For $0<\beta<1$ the solution family is not a semigroup; at every positive time it gains exactly two spatial derivatives and belongs to $\mathcal S_p$ exactly when $p>1/2$. \>1 Its scaled long-time limit is the Dirichlet resolvent in operator norm, whereas $\beta=1$ recovers all-order heat smoothing and exponential decay; 378 executable cells audit every endpoint. No source operator ideal is promoted to target arithmetic data.
author:
- 'Route-A source-local certificate HCS-C277'
date: 1 September 2026
title: |
  Caputo Dirichlet Heat Flow:\
  Sharp Smoothing, Schatten, and Resolvent Limits
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2772026090100000000000000000000\>\<C2772026090100000000000000000000\>\]

# The frozen memory owner

Let $X=L^2(0,\pi)$ and $$A=-\frac{d^2}{dx^2},\qquad
 D(A)=H^2(0,\pi)\cap H_0^1(0,\pi).$$ The normalized eigenvectors $e_n=(2/\pi)^{1/2}\sin(nx)$ satisfy $Ae_n=n^2e_n$. We freeze $${}^C D_t^\beta u(t)+Au(t)=0,\qquad u(0)=u_0\in X,
 \qquad 0<\beta\leq1.                                      \tag{1}$$ For $0<\beta<1$, $${}^C D_t^\beta f(t)=\frac1{\Gamma(1-\beta)}
 \int_0^t(t-s)^{-\beta}f'(s)\,ds,$$ and $\beta=1$ means the ordinary derivative. Bounded-domain fractional diffusion-wave problems admit eigenfunction constructions of this type [@SY]; here the interval permits sharp operator thresholds.

Writing $$E_\beta(z)=\sum_{k=0}^\infty\frac{z^k}{\Gamma(\beta k+1)},$$ the coefficient identity $${}^C D_t^\beta\frac{t^{\beta k}}{\Gamma(\beta k+1)}
 =\frac{t^{\beta(k-1)}}{\Gamma(\beta(k-1)+1)},\quad k\geq1,$$ gives the unique solution family $$S_\beta(t)u_0=\sum_{n\geq1}
 E_\beta(-n^2t^\beta)\langle u_0,e_n\rangle e_n.          \tag{2}$$

Pollard proved that $E_\beta(-x)$ is completely monotone on $x\geq0$ for $0<\beta<1$ [@Pollard]. More precisely, if $\eta_\beta(t,s)$ is the inverse-stable density characterized by $$\int_0^\infty e^{-zt}\eta_\beta(t,s)\,dt
 =z^{\beta-1}e^{-sz^\beta},$$ then scalar Laplace inversion in (2) yields $$S_\beta(t)=\int_0^\infty e^{-sA}\eta_\beta(t,s)\,ds.     \tag{3}$$ Thus $S_\beta(t)$ is self-adjoint and positive, preserves nonnegative functions, and is contractive. Dominated convergence in (2) gives strong continuity at zero.

\>0

# The sharp memory theorem

We use the spectral Sobolev scale $X^s=D(A^{s/2})$. In particular, $X^2=D(A)=H^2\cap H_0^1$; "two derivatives" includes this endpoint.

Fix $0<\beta<1$ and $t>0$.

1.  The strongly continuous family $S_\beta$ is not a semigroup.

2.  Within the declared domain $\theta\geq0$, $A^\theta S_\beta(t)$ is bounded on $X$ if and only if $\theta\leq1$. Equivalently, within $s\geq0$, $S_\beta(t):X\to X^s$ is bounded if and only if $s\leq2$.

3.  For every $p>0$, $S_\beta(t)\in\mathcal S_p$ exactly when $p>1/2$. The endpoint $p=1/2$ fails.

If $S_\beta$ were a semigroup, the continuous first-mode multiplier $E_\beta(-t^\beta)$ would be an exponential. But $$E_\beta(-t^\beta)=1-\frac{t^\beta}{\Gamma(1+\beta)}
 +O(t^{2\beta}),$$ which is not exponential when $\beta<1$.

On the positive ray, the standard Mittag--Leffler expansion gives $$E_\beta(-x)=\frac1{x\Gamma(1-\beta)}+O(x^{-2})
 \quad(x\to\infty).                                      \tag{4}$$ If a later reciprocal-Gamma coefficient vanishes, (4) only improves. Hence $$n^{2\theta}E_\beta(-n^2t^\beta)
 \sim\frac{t^{-\beta}}{\Gamma(1-\beta)}n^{2\theta-2}.$$ Continuity on compact $x$-intervals supplies the upper bound at $0\leq\theta\leq1$, and the positive asymptotic proves failure at every $\theta>1$. If $\theta<0$, then $A\geq I$ makes $A^\theta$ bounded, so $A^\theta S_\beta(t)$ is also bounded; these negative powers lie outside the declared $\theta\geq0$ smoothing domain. The singular values themselves are asymptotic to a positive constant times $n^{-2}$, so their $p$th powers sum exactly for $2p>1$.

The endpoint is substantive: memory retains only one bounded power of the second-order generator. This differs from merely asserting some unspecified regularization, and it prevents importing the heat flow's analytic smoothing into the fractional clock.

\>1

# Long time and the classical face

For $0<\beta<1$, $$t^\beta S_\beta(t)\longrightarrow
 \frac{A^{-1}}{\Gamma(1-\beta)}\quad\hbox{in }\mathcal B(X),          \tag{5}$$ and $t^\beta\lVert S_\beta(t)\rVert\to1/\Gamma(1-\beta)$. For $\beta=1$, $S_1(t)=e^{-tA}$, $\lVert S_1(t)\rVert=e^{-t}$, $A^\theta S_1(t)$ is bounded for every $\theta\geq0$, and $S_1(t)\in\mathcal S_p$ for every $p>0$.

Set $g(x)=xE_\beta(-x)-1/\Gamma(1-\beta)$. Equation (4) gives $g(x)\to0$. The $n$th diagonal entry of the difference in (5) is $$\frac{g(n^2t^\beta)}{n^2},$$ whose supremum is bounded by $\sup_{x\geq t^\beta}|g(x)|\to0$. Complete monotonicity makes the first multiplier the norm, proving the scalar limit. At $\beta=1$, (2) becomes $e^{-n^2t}$; exponential mode decay proves all remaining claims.

The heat face is therefore a singular structural boundary, not a uniform extension of (4): algebraic memory tails disappear, the solution family becomes a semigroup, and finite smoothing saturates to all orders.

# Executable certificate and Route-A boundary

The receipt contains 24 scalar Mittag--Leffler cells, 192 spectral cells, six composition witnesses, 96 large-time cells using the independent identity $E_{1/2}(-x)=e^{x^2}\operatorname{erfc}(x)$, 35 smoothing cells, and 25 Schatten cells. A producer-independent checker, 90 symbolic identities, fresh byte replay, and repaired-hash mutations audit the package. These finite cells test conventions; (2)--(5) prove the parameter theorem.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)},$$ overall `ROUTE_A_REJECTED`; Route B is disabled. Trace-ideal membership of this dissipative memory family is not a target determinant, functional equation, divisor, or Hilbert--Pólya operator.

9 H. Pollard, *The completely monotonic character of the Mittag-Leffler function $E_a(-x)$*, Bull. Amer. Math. Soc. 54 (1948), 1115--1116, [doi:10.1090/S0002-9904-1948-09132-7](https://doi.org/10.1090/S0002-9904-1948-09132-7). K. Sakamoto and M. Yamamoto, *Initial value/boundary value problems for fractional diffusion-wave equations and applications to some inverse problems*, J. Math. Anal. Appl. 382 (2011), 426--447, [doi:10.1016/j.jmaa.2011.04.058](https://doi.org/10.1016/j.jmaa.2011.04.058).
