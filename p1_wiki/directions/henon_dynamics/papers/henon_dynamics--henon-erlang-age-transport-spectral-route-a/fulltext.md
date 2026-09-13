---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-erlang-age-transport-spectral-route-a"
canonical_tex: "henon_dynamics/henon_erlang_age_transport_spectral_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_erlang_age_transport_spectral_route_a/paper/main.pdf"
source_sha256: "f178f117098db551890fd399922af39a68bd40f35f151ac3524ea6c6bd61c29b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Erlang Age-Transport Dynamics: Algebraic Renewal Roots versus the Essential Spectral Edge

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_erlang_age_transport_spectral_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_erlang_age_transport_spectral_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_erlang_age_transport_spectral_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_erlang_age_transport_spectral_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve an Erlang-fertility McKendrick age-transport semigroup at the level of characteristics, renewal poles, and long-time dynamics. The Euler--Lotka denominator has exactly $k$ explicit algebraic roots. \>0 A rank-one resolvent comparison fixes the essential edge at $-\mu$ and proves that a formal root is an $L^1$ eigenvalue only when it lies strictly to the right of that edge. \>1 For $\beta>1$ the dominant real root owns a positive asynchronous rank-one term, while population growth starts only at $\beta=(1+\mu/\gamma)^k$; 2,340 root cells audit the distinction. No renewal pole is promoted to target arithmetic data.
author:
- 'Route-A source-local certificate HCS-C272'
date: 1 September 2026
title: |
  Erlang Age-Transport Dynamics:\
  Algebraic Renewal Roots versus the Essential Spectral Edge
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2722026090100000000000000000000\>\<C2722026090100000000000000000000\>\]

# Erlang age-transport owner

On $X=L^1(\mathbb R_+,da)$, freeze $$\begin{aligned}
 \partial_t n+\partial_a n&=-\mu n,\qquad
 n(t,0)=\int_0^\infty b_k(a)n(t,a)\,da,                 \tag{1}\\
 b_k(a)&=\frac{\beta\gamma^k a^{k-1}e^{-\gamma a}}{(k-1)!},
 \quad \mu,\gamma,\beta>0,\quad k\ge1.                 \tag{2}\end{aligned}$$ Age-structured transport descends from M'Kendrick's mathematical population framework [@McK]; the Erlang specialization and spectral audit are local.

Characteristics transport initial mass to the right with factor $e^{-\mu t}$ and fill the newborn triangle from the boundary. Substitution into (1) produces a scalar renewal equation. Its exponential mode has denominator $$\Delta(\lambda)=1-\beta
 \left(\frac{\gamma}{\gamma+\lambda+\mu}\right)^k.       \tag{3}$$ Therefore the algebraic roots are $$\lambda_j=\gamma\beta^{1/k}e^{2\pi i j/k}-\gamma-\mu,
 \qquad 0\le j<k.                                       \tag{4}$$

\>0

# Resolvent and the eigenvalue gate

Let $Gf=-f'-\mu f$ with the renewal boundary from (1). For $\Re\lambda>-\mu$, direct integration gives $$u(a)=e^{-(\lambda+\mu)a}u(0)+
 \int_0^a e^{-(\lambda+\mu)(a-s)}f(s)\,ds.              \tag{5}$$ The boundary determines $u(0)$ through (3). Relative to the absorbing mortality shift, the remaining term in (5) is one scalar functional times one exponential; the resolvent difference is rank one. The essential spectral edge is consequently $\Re\lambda=-\mu$.

A root in (4) is an $L^1$ eigenvalue exactly when $\Re\lambda_j>-\mu$. Roots on or below the essential edge are not $L^1$ eigenvalues.

Every candidate eigenfunction is a multiple of $e^{-(\lambda_j+\mu)a}$. Its absolute integral is finite exactly under the strict displayed inequality. Equation (3) then supplies, and only then supplies, the renewal boundary.

\>1

# Two distinct transitions

Put $\rho=\beta^{1/k}$. The real root $$\lambda_0=\gamma(\rho-1)-\mu                           \tag{6}$$ has strictly largest real part. It clears the essential edge exactly when $\beta>1$. Let $T(t)$ be the renewal semigroup and $S_\mu(t)f(a)=e^{-\mu t}f(a-t)\mathbf1_{a\ge t}$. Characteristics show that $T(t)-S_\mu(t)$ is the newborn term. On $0\le s\le t$ its initial-data forcing is $$g_f(s)=e^{-\mu s}\int_0^\infty b_k(s+u)f(u)\,du.$$ The bounded derivative and decaying tail of $b_k$ make $f\mapsto g_f$ compact from $L^1$ into $C[0,t]$ by Arzelà--Ascoli. The Volterra renewal resolvent and newborn-triangle map preserve compactness. Thus $T(t)-S_\mu(t)$ is compact, $\lVert S_\mu(t)\rVert_{\rm ess}=e^{-\mu t}$, and the essential growth bound is $-\mu$.

The simple positive residue at $\lambda_0$ defines a positive rank-one projection $P_0$. Quasi-compact spectral decomposition now gives $$\lVert e^{-\lambda_0t}T(t)-P_0\rVert_{L^1\to L^1}\longrightarrow0,          \tag{7}$$ with stable-age profile proportional to $e^{-\gamma(\rho-1)a}$. For $k>1$, its separation from the rest is $$\min\{\gamma(\rho-1),\,\gamma\rho[1-\cos(2\pi/k)]\};    \tag{8}$$ for $k=1$, only the first term remains. When $\beta\le1$, no isolated real pole lies beyond the edge, so we make no universal rank-one claim.

The sign of (6) changes at the later threshold $$\beta_c=(1+\mu/\gamma)^k.                               \tag{9}$$ Thus, for every nonzero positive initial density, $1<\beta<\beta_c$ has an isolated positive eigenprofile whose amplitude still decays, $\beta=\beta_c$ is population-critical, and $\beta>\beta_c$ grows. For $\beta\le1$ the population still decays, but no universal rank-one profile is claimed. At zero fertility, only the mortality-weighted right shift remains.

# Certificate and Route-A boundary

The exact receipt covers 360 parameter cases, all 2,340 roots for $1\le k\le12$, exact polynomials, edge labels, gaps, and six zero-birth faces. Independent polynomial/root reconstruction, 48 symbolic identities, fresh byte replay, and repaired-hash hostile tests audit the release. These finite cells are regression evidence; (3)--(9) prove the parameter theorem.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)},$$ overall `ROUTE_A_REJECTED`; Route B is disabled. The source transport generator and its renewal poles are not a target determinant, divisor, functional equation, or Hilbert--Pólya operator.

9 A. G. M'Kendrick, *Applications of Mathematics to Medical Problems*, Proceedings of the Edinburgh Mathematical Society 44 (1925), 98--130, [doi:10.1017/S0013091500034428](https://doi.org/10.1017/S0013091500034428).
