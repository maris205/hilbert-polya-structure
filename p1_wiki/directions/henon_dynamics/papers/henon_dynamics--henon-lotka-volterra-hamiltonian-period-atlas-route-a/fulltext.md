---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lotka-volterra-hamiltonian-period-atlas-route-a"
canonical_tex: "henon_dynamics/henon_lotka_volterra_hamiltonian_period_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lotka_volterra_hamiltonian_period_atlas_route_a/paper/main.pdf"
source_sha256: "75bce384d40de8d3f4c63646a15df7c7c286748d0ece359858754239ac78227a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Global Hamiltonian Period Atlas for Positive Lotka--Volterra Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lotka_volterra_hamiltonian_period_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lotka_volterra_hamiltonian_period_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lotka_volterra_hamiltonian_period_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lotka_volterra_hamiltonian_period_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a global, source-native description of the positive two-species Lotka--Volterra flow at its physical time clock. A logarithmic normalization turns the system into a strictly convex proper Hamiltonian flow. Every positive energy is therefore one compact periodic oval. The two real Lambert-W branches of the exponential potential give exact one-dimensional quadratures for the enclosed area and period, and coarea gives the action identity $J'(h)=T(h)/(2\pi)$. Linearization supplies the center-period limit, while integrating the log equations gives exact prey and predator cycle averages. An independent certificate checks 24 levels in six rational parameter sets and re-integrates the period with a SciPy event ODE. We do not assert period monotonicity or a high-energy asymptotic, and we make no target arithmetic or operator claim.
author:
- HCS Research Program
date: 28 August 2026(revision 2)
title: 'A Global Hamiltonian Period Atlas for Positive Lotka--Volterra Flow'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and global claim

Consider $$\dot x=x(a-by),\qquad \dot y=y(-c+dx),\qquad a,b,c,d>0,$$ on $x,y>0$, with physical time $t$. Put $x_*=c/d$, $y_*=a/b$ and $u=\log(x/x_*),v=\log(y/y_*)$. Then $$\dot u=a(1-e^v),\qquad \dot v=c(e^u-1),\qquad
 H=c(e^u-u-1)+a(e^v-v-1).$$

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} $H$ is a strict convex proper first integral with unique critical point $(0,0)$. Every level $H=h>0$ is a smooth compact periodic oval. If $F(s)=e^s-s-1$, let $$\ell(r)=-W_0(-e^{-1-r})-1-r,\qquad
 q(r)=-W_{-1}(-e^{-1-r})-1-r.$$ With $u_-=\ell(h/c)$, $u_+=q(h/c)$, and $r(u)=(h-cF(u))/a$, its area and period are $$\begin{aligned}
 A(h)&=\int_{u_-}^{u_+}\bigl[q(r(u))-\ell(r(u))\bigr]\,du,\\
 T(h)&=\frac1a\int_{u_-}^{u_+}\left[
 \frac1{1-e^{\ell(r(u))}}+\frac1{e^{q(r(u))}-1}\right]\,du.\end{aligned}$$ The endpoint singularities are integrable. For $J(h)=A(h)/(2\pi)$, $J'(h)=T(h)/(2\pi)$, and $\lim_{h\downarrow0}T(h)=2\pi/\sqrt{ac}$. Every periodic orbit obeys $\langle x\rangle=c/d$ and $\langle y\rangle=a/b$.

The Hessian is $\operatorname{diag}(ce^u,ae^v)$ and $F$ tends to infinity at both ends, giving strict convexity and properness. The sublevel $K_h=\{H\le h\}$ is a compact convex body with nonempty interior, so its boundary $H=h$ is connected; regularity follows because the only critical point is the origin. The canonical equations are $\dot u=-H_v,\dot v=H_u$, and the vector field is nonzero on this boundary. Thus the connected compact one-manifold is one periodic oval. Solving $F(s)=r$ gives the two displayed Lambert branches. Splitting the oval into lower and upper graphs gives the quadratures. Along the level, $|\dot{(u,v)}|=|\nabla H|$, hence $dt=ds/|\nabla H|$; the coarea formula then gives $dA/dh=\int_{H=h}ds/|\nabla H|=T$. The center matrix is $\left(\begin{smallmatrix}0&-a\\c&0\end{smallmatrix}\right)$. Finally, integrating $\dot u$ and $\dot v$ over a period gives $\langle e^u\rangle=\langle e^v\rangle=1$.

\>0

# Branches, action, and boundaries

The branch labels matter: $W_0$ gives the negative graph and $W_{-1}$ the positive graph. A trigonometric substitution in the certificate cancels the square-root endpoint singularities without changing the physical clock. The geometric action is positive by definition; no orientation convention is needed. The axes are invariant one-dimensional flows, not members of the positive period annulus. If a rate is zero, coercivity or the interior Hamiltonian statement can fail and the resulting boundary equation is treated separately. We intentionally leave period monotonicity and large-energy asymptotics outside the theorem.

\>1

# Independent audit and Route-A boundary

The released ledger contains six positive rational $(a,b,c,d)$ cases and four energies per case. It serializes 24 areas, periods, actions, branch endpoints, and residuals. The producer uses high-precision Lambert-W quadrature; the checker independently repeats those identities and then integrates the log flow with a DOP853 event solver from the right turning point. The checker passes 732 assertions, including all 24 heterogeneous center-period checks; SymPy passes 12 identities, byte replay is exact, and twelve repaired/stale hash attacks are rejected.

This is a continuum of real-energy cycles, not a discrete arithmetic primitive ledger. Accordingly the Route-A tuple is

(A0\_FAIL, A1\_WEAK, A2\_FAIL, A3\_FAIL, A4\_FORMAL\_HINT),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. No target prime, zero, local factor, root number, automorphy statement, target functional equation, or Hilbert--Polya operator is claimed.

# Source note {#source-note .unnumbered}

Period-analysis context includes Waldvogel [@waldvogel1983; @waldvogel1986] and Hsu [@hsu1983]. We do not use the historical monotonicity result as a claim here and make no priority statement.

9 J. Waldvogel, "The Period in the Volterra--Lotka Predator-Prey Model," *SIAM Journal on Numerical Analysis* 20(6) (1983), 1264--1272, DOI:[10.1137/0720098](https://doi.org/10.1137/0720098). J. Waldvogel, "The period in the Volterra-Lotka system is monotonic," *Journal of Mathematical Analysis and Applications* 114(1) (1986), 178--184, DOI:[10.1016/0022-247X(86)90076-4](https://doi.org/10.1016/0022-247X(86)90076-4). S.-B. Hsu, "A Remark on the Period of the Periodic Solution in the Lotka-Volterra System," *Journal of Mathematical Analysis and Applications* 95(2) (1983), 428--436, DOI:[10.1016/0022-247X(83)90117-8](https://doi.org/10.1016/0022-247X(83)90117-8).

# Declarations {#declarations .unnumbered}

**Scope.** The exact registered literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. **Data and code.** The theorem, ledger, independent checks, and build instructions are released with HCS-C211. **Competing interests.** None declared. **AI-use disclosure.** Generative tools assisted drafting and code generation. The released theorem, numerical values, source metadata, and scope boundaries were checked by the internal artifact chain; this is not external peer review.
