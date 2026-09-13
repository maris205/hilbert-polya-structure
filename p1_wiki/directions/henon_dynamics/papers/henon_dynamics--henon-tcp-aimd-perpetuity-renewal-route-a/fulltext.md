---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-tcp-aimd-perpetuity-renewal-route-a"
canonical_tex: "henon_dynamics/henon_tcp_aimd_perpetuity_renewal_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_tcp_aimd_perpetuity_renewal_route_a/paper/main.pdf"
source_sha256: "fa0228b696032a9fc36964a48e153cbb463326a6b73c51ed5c8e73a8a9d36e92"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Affine Perpetuity and Palm Occupation Certificate for Linear-Rate AIMD

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_tcp_aimd_perpetuity_renewal_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_tcp_aimd_perpetuity_renewal_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_tcp_aimd_perpetuity_renewal_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_tcp_aimd_perpetuity_renewal_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the hybrid process $\dot X=a>0$ with jump intensity $\rho X$ and multiplicative decrease $X\mapsto\beta X$, $0<\beta<1$. For the pre-jump value $Y_n$, completing the integrated hazard gives the exact square-affine chain $Y_{n+1}^2=\beta^2Y_n^2+2aE_{n+1}/\rho$. This yields a unique stationary affine perpetuity, a source-local Laplace q-product, all squared moments, the generator moment recursion, and a stationary Markov-renewal/Palm occupation formula. The receipt covers 27 rational parameter tuples and exact reward skeletons, with independent checking, symbolic identities, replay, and hostile mutations. For positive $\beta$ the jump sequence is Markov rather than iid regenerative; $\beta=0$ is the separate reset face. No arithmetic target determinant is claimed, so the strict Route-A verdict is `ROUTE_A_REJECTED`.
author:
- HCS Research Program
date: 30 August 2026(revision 2)
title: 'An Exact Affine Perpetuity and Palm Occupation Certificate for Linear-Rate AIMD'
```

## Markdown 正文

suppressoptionalinfo 611

# Process and the pre-jump chain

Between jumps let $X_t=\beta Y_n+at$, where $Y_n$ is the value immediately before the preceding jump. The next waiting time $T_{n+1}$ is determined by the integrated hazard $$\rho\left(\beta Y_nT_{n+1}+\frac{aT_{n+1}^2}{2}\right)=E_{n+1},
 \qquad E_{n+1}\sim\operatorname{Exp}(1),
 \tag{1}$$ and $Y_{n+1}=\beta Y_n+aT_{n+1}$.

For every $a,\rho>0$ and $0<\beta<1$, $$Y_{n+1}^2=\beta^2Y_n^2+\frac{2a}{\rho}E_{n+1}. \tag{2}$$

Expand $(\beta Y_n+aT)^2-\beta^2Y_n^2=2a(\beta Y_nT+aT^2/2)$ and use (1). The factor $a$ cannot be dropped.

With $Z_n=Y_n^2$, synchronous coupling under common exponentials satisfies $|Z_n-Z_n'|=\beta^{2n}|Z_0-Z_0'|$. Consequently $$Z_\infty=\frac{2a}{\rho}\sum_{j\ge0}\beta^{2j}E_{-j}$$ converges almost surely and is the unique stationary jump-chain law; every finite initial state converges to it.

The geometric coefficients have finite sum $\mathbb E Z_\infty=(2a/\rho)/(1-\beta^2)<\infty$, so the nonnegative perpetuity series is finite almost surely. The coupling identity contracts every initial pair, so two stationary versions coincide and the finite-start law converges weakly (indeed in Wasserstein metrics with a finite first moment).

# Laplace product and moments

Independence of the exponential innovations gives the source-local transform $$\psi(s)=\mathbb E[e^{-sZ_\infty}]
 =\prod_{j\ge0}\left(1+\frac{2a}{\rho}\beta^{2j}s\right)^{-1}. \tag{3}$$ The release stores a 12-factor rational prefix and three rational spot values for every frozen parameter tuple. Equation (3) is probability bookkeeping, not an arithmetic Euler product or a target determinant.

For the continuous-time stationary law let $\varphi(s)=\mathbb E[e^{-sX}]$. Applying the generator (6) to $e^{-sx}$ gives the source-local Laplace-generator identity $$\varphi'(s)-\varphi'(\beta s)=\frac{a}{\rho}s\,\varphi(s). \tag{4}$$ It is not a target continuation or functional equation.

Writing $m_k=\mathbb E[Z^k]$, expansion of (2) yields $$(1-\beta^{2k})m_k=
 \sum_{j=0}^{k-1}\binom{k}{j}\beta^{2j}
 \left(\frac{2a}{\rho}\right)^{k-j}(k-j)!m_j,\qquad m_0=1. \tag{5}$$ All entries in the finite receipt are exact rational numbers.

# Stationary occupation formula

The continuous-time generator is $$(Lf)(x)=a f'(x)+\rho x\,[f(\beta x)-f(x)]. \tag{6}$$ For stationary moments $M_m=\mathbb E[X^m]$, applying (6) to $x^m$ gives $$\rho(1-\beta^m)M_{m+1}=amM_{m-1},\qquad m\ge1. \tag{7}$$ Thus $M_0=1$, $M_1=\mu$, and all higher moments are exact affine expressions in the single Palm-determined mean $\mu$.

Let $\pi$ denote the stationary pre-jump law. A cycle from $\beta Y_n$ to $Y_{n+1}$ has duration $T=(Y_{n+1}-\beta Y_n)/a$ and monomial reward $$\int_0^T(\beta Y_n+at)^m\,dt
 =\frac{Y_{n+1}^{m+1}-(\beta Y_n)^{m+1}}{a(m+1)}. \tag{8}$$ The stationary Markov-renewal/Palm ratio is therefore $$M_m=\frac{1-\beta^{m+1}}{(m+1)(1-\beta)}
 \frac{\mathbb E_\pi[Y^{m+1}]}{\mathbb E_\pi[Y]},
 \qquad
 \mu=\frac{a}{\rho(1-\beta)\mathbb E_\pi[Y]}. \tag{9}$$ For $\beta>0$, $\pi$ is a stationary Markov jump-cycle law: (8) is not an iid regeneration assertion.

\>0

# Finite certificate and literature context

The exact receipt evaluates all $3^3=27$ tuples $\beta\in\{1/2,2/3,3/4\}$, $a\in\{1/2,1,3/2\}$, and $\rho\in\{1/2,1,2\}$. It records orders 0--8, a 12-factor prefix, and a six-step rational hazard skeleton chosen by $Y_{n+1}-\beta Y_n=1$. The producer-independent checker passes 75 assertions, SymPy passes 96 identities, byte replay matches two fresh runs, and 36 hostile mutations are rejected.

Dumas, Guillemin, and Robert give a Markovian AIMD analysis and invariant probabilities [@dumas2002]; Guillemin, Robert, and Zwart analyze AIMD algorithms through exponential functionals [@guillemin2004]. These are publisher/DOI references for context, not arithmetic or target spectral certificates.

\>1

# Boundary faces and Route-A scope

At $\beta=0$ the post-jump state is zero and successive cycles are iid: this is the genuine reset/regeneration face. Its pre-jump density is $f_Y(y)=(\rho/a)y e^{-\rho y^2/(2a)}$, and its continuous-time occupation density is the half-normal $f_X(x)=\sqrt{2\rho/(\pi a)}e^{-\rho x^2/(2a)}$, with mean $\sqrt{2a/(\pi\rho)}$. At $\beta=1,a>0,\rho>0$ contraction is lost and positive drift has no finite invariant law. On the closed half-line, $a=0,0\le\beta<1,\rho>0$ has only the invariant atom $\delta_0$, hence no invariant probability on $X>0$; $a=0,\beta=1,\rho>0$ leaves every law invariant, as does $a=\rho=0$. If $\rho=0,a>0$, linear escape gives no invariant law. There is no intrinsic prime carrier (A0\_FAIL), no target determinant or zero matching (A2\_FAIL), and no target continuation or functional equation (A3\_FAIL). The strict tuple is $$(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},\mathtt{A3\_FAIL},
 \mathtt{A4\_FORMAL\_HINT}),$$ with `ROUTE_A_REJECTED`, `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B disabled. The q-product remains source-local probability data.

9 V. Dumas, F. Guillemin, and P. Robert, "A Markovian analysis of additive-increase multiplicative-decrease algorithms," *Advances in Applied Probability* 34 (2002), DOI: [10.1239/aap/1019160951](https://doi.org/10.1239/aap/1019160951). F. Guillemin, P. Robert, and B. Zwart, "AIMD algorithms and exponential functionals," *Annals of Applied Probability* 14 (2004), DOI: [10.1214/aoap/1075828048](https://doi.org/10.1214/aoap/1075828048).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no arithmetic, target-zero, Euler-factor, root-data, automorphy, or Hilbert--Pólya claim is made. **Data and code.** Exact receipts, independent checker, replay, and mutation audit are included. **AI-use disclosure.** Generative tools assisted drafting and code generation; formulas and metadata are checked by the deterministic artifact chain.
