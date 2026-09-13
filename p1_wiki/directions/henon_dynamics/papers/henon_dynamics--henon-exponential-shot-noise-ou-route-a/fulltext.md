---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-exponential-shot-noise-ou-route-a"
canonical_tex: "henon_dynamics/henon_exponential_shot_noise_ou_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_exponential_shot_noise_ou_route_a/paper/main.pdf"
source_sha256: "68dfc4ca14c7accecf02b32307aff92891e1f6f57c56bf389a0ba3afea029d59"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exponential Shot-Noise Ornstein--Uhlenbeck Dynamics: Exact Semigroup, Gamma Equilibrium, and Polynomial Filtrations

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_exponential_shot_noise_ou_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_exponential_shot_noise_ou_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_exponential_shot_noise_ou_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_exponential_shot_noise_ou_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the positive Ornstein--Uhlenbeck process driven by Poisson arrivals with exponential marks. Its all-time transition Laplace transform follows directly from the marked-Poisson functional. \>0 The same formula yields the unique Gamma equilibrium, sharp Wasserstein contraction, all stationary moments and cumulants, and the exact covariance. \>1 We further determine the generator spectrum on every finite polynomial filtration, while explicitly making no claim about the full $L^2$ spectrum, and close every zero-parameter boundary.
author:
- 'Route-A source-local certificate HCS-C335'
date: 3 September 2026
title: |
  Exponential Shot-Noise Ornstein--Uhlenbeck Dynamics:\
  Exact Semigroup, Gamma Equilibrium, and Polynomial Filtrations
```

## Markdown 正文

trailerid \[\<C3352026090300000000000000000000\>\<C3352026090300000000000000000000\>\]

# Frozen process and semigroup

Fix $\gamma,\kappa,\beta>0$. Let $N_t$ be Poisson of rate $\kappa$, let $T_j$ be its jump times, and let the independent marks $Y_j$ have exponential rate $\beta$. On $[0,\infty)$ consider $$\label{eq:sde}
 dX_t=-\gamma X_t\,dt+dJ_t,
 \qquad J_t=\sum_{T_j\leq t}Y_j,
 \qquad X_0=x\geq0.$$

[\[thm:main\]]{#thm:main label="thm:main"} For $t,s\geq0$, with $\alpha=\kappa/\gamma$, $$\begin{aligned}
 X_t&=e^{-\gamma t}x+
 \sum_{T_j\leq t}e^{-\gamma(t-T_j)}Y_j,\label{eq:path}\\
 \mathbb E_xe^{-sX_t}&=e^{-se^{-\gamma t}x}
 \left(\frac{\beta+se^{-\gamma t}}{\beta+s}\right)^\alpha.
 \label{eq:LT}\end{aligned}$$ The unique invariant probability is Gamma with shape $\alpha$ and rate $\beta$. For every $p\geq1$, $$\label{eq:Wp}
 W_p(P_t(x,\cdot),P_t(y,\cdot))=e^{-\gamma t}|x-y|.$$ In stationarity, $$\label{eq:statistics}
 \mathbb EX^n=\frac{(\alpha)_n}{\beta^n},\qquad
 \operatorname{cum}_n(X)=\frac{\alpha(n-1)!}{\beta^n},\qquad
 \operatorname{Cov}(X_t,X_0)=\frac{\alpha}{\beta^2}e^{-\gamma|t|}.$$ Finally, the generator preserves $\mathcal P_m=\operatorname{span}\{1,x,\ldots,x^m\}$, and its restriction has exactly the simple eigenvalues $0,-\gamma,\ldots,-m\gamma$. This last assertion concerns each fixed finite-dimensional filtration only; it is not a statement about the full $L^2$ spectrum, completeness, normality, or reversibility.

Variation of constants between successive jumps proves [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"}. The Laplace functional of a marked Poisson process gives $$\begin{aligned}
 \log\mathbb E\exp\left[-s\sum_{T_j\leq t}
 e^{-\gamma(t-T_j)}Y_j\right]
 &=\kappa\int_0^t\left(\frac{\beta}{\beta+se^{-\gamma u}}-1\right)du\\
 &=\frac\kappa\gamma\log\frac{\beta+se^{-\gamma t}}{\beta+s}.\end{aligned}$$ Multiplication by the deterministic initial term proves [\[eq:LT\]](#eq:LT){reference-type="eqref" reference="eq:LT"}. Factoring the right side first at decay $r_1=e^{-\gamma t_1}$ and then at $r_2=e^{-\gamma t_2}$ cancels the intermediate denominator and leaves $r_1r_2$, proving the Chapman--Kolmogorov law directly.

The phrase *shot-noise Laplace semigroup owner* is the round-zero certificate. Formula [\[eq:LT\]](#eq:LT){reference-type="eqref" reference="eq:LT"}, not a simulation, owns the transition law.

\>0

# Equilibrium, contraction, and correlations

Sending $t\to\infty$ in [\[eq:LT\]](#eq:LT){reference-type="eqref" reference="eq:LT"} gives $$\left(\frac\beta{\beta+s}\right)^\alpha,$$ the Gamma$(\alpha,\text{rate }\beta)$ transform. Substitution into the semigroup formula proves invariance. If two copies use the same marked Poisson process, [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"} gives the deterministic difference $e^{-\gamma t}(x-y)$. Their laws are translates, so this coupling gives the upper bound in [\[eq:Wp\]](#eq:Wp){reference-type="eqref" reference="eq:Wp"}; Jensen's inequality applied to their mean difference gives the same lower bound. Any invariant law must, after its Laplace transform is propagated and $t\to\infty$, have the Gamma transform. This proves uniqueness without presupposing a moment.

Expansion of the logarithm of the Gamma transform yields the cumulants in [\[eq:statistics\]](#eq:statistics){reference-type="eqref" reference="eq:statistics"}; differentiation gives its rising-factorial moments. The conditional mean is $$\mathbb E[X_t\mid X_0]=e^{-\gamma t}X_0+
 \frac{\kappa}{\gamma\beta}(1-e^{-\gamma t}).$$ After stationary centering, multiplication by $X_0$ gives the covariance for $t\geq0$. Scalar stationarity supplies the displayed even extension. These identities also agree with the classical shot-noise and Lévy-driven OU sources [@Kotler; @Sato; @BN].

\>1

# Exact finite polynomial filtration

For suitable $f$, the generator is $$\label{eq:generator}
 Lf(x)=-\gamma x f'(x)+\kappa\int_0^\infty
 \beta e^{-\beta y}[f(x+y)-f(x)]\,dy.$$ Because $\mathbb EY^r=r!/\beta^r$, binomial expansion gives, for every $n\geq0$, $$\label{eq:monomial}
 Lx^n=-n\gamma x^n+
 \kappa\sum_{j=0}^{n-1}\binom nj
 \frac{(n-j)!}{\beta^{n-j}}x^j.$$ Thus $L\mathcal P_m\subseteq\mathcal P_m$. In the ordered monomial basis, the matrix is triangular with pairwise distinct diagonal $0,-\gamma,\ldots,-m\gamma$. It is therefore diagonalizable, every listed eigenvalue is simple, and backward substitution gives one monic eigenpolynomial of each degree. This is a complete finite-dimensional statement for every $m$; taking an unsupported limit in $m$ would not prove a full $L^2$ spectral theorem, and we do not take it.

# Degenerate faces and Route-A boundary

If $\kappa=0$ but $\gamma>0$, the process is deterministic decay and its unique invariant probability is $\delta_0$. If $\gamma=0<\kappa$, it is a nondecreasing compound-Poisson subordinator and has no invariant probability. At $\gamma=\kappa=0$ it is static and every initial law is invariant. The value $\beta=0$ is not an exponential probability law; $\beta\to\infty$ is only a weak zero-mark limit. These faces are not silently inserted into formulas containing $\kappa/\gamma$.

The finite certificate records exact Gamma moments and generator matrices through degree 12, sixty transition values, and ten semigroup products. Independent and symbolic implementations recompute them. These rows are regression evidence, not the proof of an infinite-time theorem.

C229 is a square-root diffusion, C233 is a discrete immigration--death chain, C265 has self-exciting arrivals, and C328 has dichotomous velocities and compact support; none owns the present positive-jump Gamma semigroup. All five Route-A layers fail: there is no intrinsic prime owner, isolated periodic ledger, orbit determinant, target analytic bridge, or natural self-adjoint target lift. Route B is not invoked. No target local data, Euler factors, root numbers, automorphy, target divisor law, functional equation, zero match, or Hilbert--Pólya operator is claimed.

9 G. Kotler, V. Kontorovich, V. Lyandres, and S. Primak, *On the Markov model of shot noise*, Signal Processing (1999), [doi:10.1016/S0165-1684(98)00226-6](https://doi.org/10.1016/S0165-1684(98)00226-6). K. Sato and M. Yamazato, *Operator-selfdecomposable distributions as limit distributions of processes of Ornstein--Uhlenbeck type*, Stochastic Processes Appl. 17 (1984), 73--100, [doi:10.1016/0304-4149(84)90312-0](https://doi.org/10.1016/0304-4149(84)90312-0). O. E. Barndorff-Nielsen and N. Shephard, *Non-Gaussian Ornstein--Uhlenbeck-based models and some of their uses in financial economics*, J. Roy. Statist. Soc. B 63 (2001), 167--241, [doi:10.1111/1467-9868.00282](https://doi.org/10.1111/1467-9868.00282).
