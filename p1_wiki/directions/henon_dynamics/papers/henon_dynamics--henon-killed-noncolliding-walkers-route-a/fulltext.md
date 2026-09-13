---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-killed-noncolliding-walkers-route-a"
canonical_tex: "henon_dynamics/henon_killed_noncolliding_walkers_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_killed_noncolliding_walkers_route_a/paper/main.pdf"
source_sha256: "b88d86733c5232c377db7b9bf51c29184477d5ce2b2e78d737673f7703d3aa94"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Killed Noncolliding Walkers on a Finite Interval: Determinantal Spectrum, Absorption, and the Q-Process

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_killed_noncolliding_walkers_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_killed_noncolliding_walkers_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_killed_noncolliding_walkers_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_killed_noncolliding_walkers_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every $1\leq k\leq L$, we diagonalize $k$ continuous-time symmetric nearest-neighbour walks on $\{1,\ldots,L\}$ killed at the first boundary hit or collision. The one-particle sine kernel and the Karlin--McGregor determinant yield a complete Slater basis of all $\binom Lk$ chamber states. \>0 The same expansion gives the entire absorption law, every absorption-time moment, sharp leading survival asymptotics, the unique quasi-stationary law, and the conservative Doob transform with invariant density $h^2$. \>1 We close the one-particle and full-occupancy faces, the singleton spectral-gap boundary, and the distinction from reflecting exclusion, and accompany the all-parameter proof with an independently reconstructed finite atlas.
author:
- 'Route-A source-local certificate HCS-C306'
date: 3 September 2026
title: |
  Killed Noncolliding Walkers on a Finite Interval:\
  Determinantal Spectrum, Absorption, and the Q-Process
```

## Markdown 正文

trailerid \[\<C3062026090300000000000000000000\>\<C3062026090300000000000000000000\>\] suppressoptionalinfo 767

# Killed chamber dynamics

Fix integers $L\geq1$ and $1\leq k\leq L$. A single particle jumps one site left and right at rate one, and is killed on an attempted jump to $0$ or $L+1$. The $k$ particles have independent clocks until the first such boundary attempt or the first attempted coincidence. Before killing their ordered configuration lies in $$\mathcal W_{L,k}=\{x=(x_1,\ldots,x_k):1\leq x_1<\cdots<x_k\leq L\}.$$ For $f$ on this chamber, extended by zero across collision and boundary faces, the sub-Markov generator is $$\label{eq:Q}
 (Q_kf)(x)=\sum_{a=1}^k\{f(x-e_a)+f(x+e_a)-2f(x)\}.$$ Thus every legal one-coordinate step has rate one and $Q_k(x,x)=-2k$. This diagonal is essential: a forbidden attempt kills; it is not suppressed or reflected as in an exclusion chain.

For one particle put $$\label{eq:sine}
 \phi_r(j)=\sqrt{\frac2{L+1}}\sin\frac{\pi rj}{L+1},\qquad
 \varepsilon_r=2-2\cos\frac{\pi r}{L+1},\quad 1\leq r,j\leq L.$$ The Dirichlet difference equation and sine orthogonality give $$\label{eq:p1}
 p_t^{(1)}(i,j)=\frac2{L+1}\sum_{r=1}^L
 e^{-\varepsilon_rt}\sin\frac{\pi ri}{L+1}\sin\frac{\pi rj}{L+1}.$$

# Determinant and complete spectrum

For increasing mode indices $m=(m_1<\cdots<m_k)$ define $$\label{eq:slater}
 \Phi_m(x)=\det[\phi_{m_a}(x_b)]_{a,b=1}^k,\qquad
 \Lambda_m=\sum_{a=1}^k\varepsilon_{m_a}.$$

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The $\binom Lk$ functions $\Phi_m$ form a complete orthonormal basis of $\ell^2(\mathcal W_{L,k})$ and $Q_k\Phi_m=-\Lambda_m\Phi_m$. For all $t\geq0$, $$\begin{aligned}
 P_t(x,y)&=\Pr_x\{X(t)=y,\ \tau>t\}
     =\det[p_t^{(1)}(x_i,y_j)]_{i,j=1}^k,\label{eq:KM}\\
 P_t(x,y)&=\sum_m e^{-\Lambda_mt}\Phi_m(x)\Phi_m(y).\label{eq:spectral}\end{aligned}$$ Every eigenvalue is displayed with its multiplicity, including coincidences among distinct mode sums.

Tensor products of the one-particle eigenvectors diagonalize the generator of the independent product chain. Antisymmetrizing a tensor product gives the determinant in [\[eq:slater\]](#eq:slater){reference-type="eqref" reference="eq:slater"}; crossing a wall changes sign, so its restriction to the ordered chamber obeys the zero boundary convention in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}. Cauchy--Binet, or direct antisymmetric tensor orthogonality, gives $\sum_{x\in\mathcal W_{L,k}}\Phi_m(x)\Phi_n(x)=\mathbf 1_{m=n}$. There are exactly $\binom Lk=|\mathcal W_{L,k}|$ modes, proving completeness and [\[eq:spectral\]](#eq:spectral){reference-type="eqref" reference="eq:spectral"}.

For [\[eq:KM\]](#eq:KM){reference-type="eqref" reference="eq:KM"}, expand the determinant of [\[eq:p1\]](#eq:p1){reference-type="eqref" reference="eq:p1"} and apply Cauchy--Binet. Equivalently, the Karlin--McGregor path-switching involution pairs product paths at their first collision with opposite permutation sign; only never-coincident paths remain. Boundary killing is already contained in each one-particle kernel. At $t=0$, orthonormal completeness makes either formula the identity kernel.

The lowest mode is $m_0=(1,\ldots,k)$. Its determinant has a fixed sign. Indeed, with $\theta_b=\pi x_b/(L+1)$ and $\sin(a\theta)=\sin\theta\,U_{a-1}(\cos\theta)$, $$\label{eq:positive}
 h(x):=(-1)^{k(k-1)/2}\Phi_{m_0}(x)
 =\left(\frac2{L+1}\right)^{k/2}2^{k(k-1)/2}
 \prod_b\sin\theta_b\prod_{i<j}(\cos\theta_i-\cos\theta_j)>0.$$ Thus $\|h\|_2=1$ and $\Lambda_0=\sum_{r=1}^k\varepsilon_r$ is simple.

\>0

# Absorption, quasi-stationarity, and conditioning

Let $A_m=\sum_{y\in\mathcal W_{L,k}}\Phi_m(y)$, choosing the sign of $m_0$ so $A_0=\sum_yh(y)>0$.

[\[thm:absorb\]]{#thm:absorb label="thm:absorb"} For every starting state $x$ and $t\geq0$, $$\begin{aligned}
 S_x(t):=\Pr_x(\tau>t)&=\sum_m e^{-\Lambda_mt}\Phi_m(x)A_m,\label{eq:surv}\\
 \Pr_x(\tau\leq t)&=1-S_x(t),\qquad
 f_x(t)=\sum_m\Lambda_m e^{-\Lambda_mt}\Phi_m(x)A_m.\label{eq:density}\end{aligned}$$ For every integer $r\geq1$, $$\label{eq:moments}
 \mathbb E_x\tau^r=r!\sum_m\frac{\Phi_m(x)A_m}{\Lambda_m^r}.$$ If $k<L$, let $$\Lambda_1=\sum_{r=1}^{k-1}\varepsilon_r+\varepsilon_{k+1},\qquad
 \gamma_{L,k}=\Lambda_1-\Lambda_0
 =2\left(\cos\frac{k\pi}{L+1}-\cos\frac{(k+1)\pi}{L+1}\right).$$ Then, as $t\to\infty$, $$\begin{aligned}
 S_x(t)&=h(x)A_0e^{-\Lambda_0t}+O_x(e^{-\Lambda_1t}),\label{eq:leadS}\\
 f_x(t)&=\Lambda_0h(x)A_0e^{-\Lambda_0t}+O_x(e^{-\Lambda_1t}).\label{eq:leadf}\end{aligned}$$ The conditioned law converges from every $x$ to the unique QSD $$\label{eq:qsd}
 \nu(y)=\frac{h(y)}{A_0}.$$

Summing [\[eq:spectral\]](#eq:spectral){reference-type="eqref" reference="eq:spectral"} over the terminal state proves [\[eq:surv\]](#eq:surv){reference-type="eqref" reference="eq:surv"}. Differentiation gives [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"}, and integrating $r\int_0^\infty t^{r-1}S_x(t)\,\mathrm dt$ proves [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"}; every $\Lambda_m$ is positive, so these finite operations are valid. Although individual spectral coefficients can have either sign, the semigroup proves the resulting survival and density are nonnegative.

The energies [\[eq:sine\]](#eq:sine){reference-type="eqref" reference="eq:sine"} strictly increase. Therefore the unique smallest mode is $(1,\ldots,k)$ and, when $k<L$, the next energy is obtained only by replacing $k$ with $k+1$. Separating these terms gives [\[eq:leadS\]](#eq:leadS){reference-type="eqref" reference="eq:leadS"}--[\[eq:leadf\]](#eq:leadf){reference-type="eqref" reference="eq:leadf"}. Division of $P_t(x,y)$ by $S_x(t)$ gives [\[eq:qsd\]](#eq:qsd){reference-type="eqref" reference="eq:qsd"}. Finally the chamber adjacency graph is connected (successively move gaps to a packed configuration), so Perron--Frobenius makes the positive left ground eigenvector unique. Since $Q_k$ is symmetric, that left vector is $h$; hence no other QSD exists.

[\[prop:doob\]]{#prop:doob label="prop:doob"} The ground-state transform has off-diagonal and diagonal rates $$\label{eq:doob}
 q^h(x,y)=q(x,y)\frac{h(y)}{h(x)}\quad(x\ne y),\qquad
 q^h(x,x)=q(x,x)+\Lambda_0.$$ It is conservative, irreducible, and reversible with the already normalized invariant law $\pi^h(x)=h(x)^2$. For $k<L$ its relaxation gap is $\gamma_{L,k}$ above.

The identity $Q_kh=-\Lambda_0h$ makes every row sum in [\[eq:doob\]](#eq:doob){reference-type="eqref" reference="eq:doob"} zero. Symmetry of $q$ gives $h(x)^2q^h(x,y)=h(x)h(y)q(x,y)=h(y)^2q^h(y,x)$. Conjugation by multiplication with $h$ shifts the killed spectrum by $\Lambda_0$, so the first positive relaxation energy is $\Lambda_1-\Lambda_0$.

\>1

# Faces, finite evidence, and claim boundary

For $k=1$, Theorem [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} is exactly the ordinary Dirichlet sine kernel. For $k=L$, the chamber contains only $(1,\ldots,L)$: no move is legal, the killing rate is $2L$, $h=1$, and $S(t)=e^{-2Lt}$. Its Doob transform is the stationary singleton. There is no nonzero relaxation mode, so the formula containing $\varepsilon_{k+1}$ is not extended to this face and no finite spectral gap is reported. In particular $L=k=1$ gives an $\operatorname{Exp}(2)$ lifetime. At $t=0$, the survival is one and the right derivative is minus the number of illegal rate-one attempts from the starting state.

The canonical finite artifact independently enumerates all 36 pairs $1\leq k\leq L\leq8$, hence 502 chamber states and 502 modes. A checker reconstructs each integer generator without importing the producer, compares its direct spectrum and matrix exponential with the sine/Slater and Karlin--McGregor formulas, verifies Doob detailed balance, and checks 273 time/state probes. A separate exact SymPy lane compares 15 characteristic polynomials and phase-type resolvent moments. These cutoffs are regression evidence; Theorems [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} and [\[thm:absorb\]](#thm:absorb){reference-type="ref" reference="thm:absorb"} are the all-parameter proof. The absorption formulas are exact finite sums, but we claim no further elementary first-passage closed form.

This system must not be confused with reflecting simple exclusion: here a collision attempt terminates the trajectory. The determinant is a probability kernel, not a target arithmetic determinant. The strict Route-A tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT})$, with overall verdict `ROUTE_A_REJECTED` and Route B locked. The finite symmetric operator is only a candidate-local A4 analogy: no same-clock target-zero identification or Hilbert--Pólya operator is asserted. Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; no arithmetic local datum, Euler factor, root number, automorphy, target divisor law, functional equation, or zero match is claimed.

# Source ownership and AI-use statement {#source-ownership-and-ai-use-statement .unnumbered}

Karlin and McGregor [@KM] established the coincidence determinant for birth--death processes. Darroch and Seneta [@DS] treat quasi-stationarity in finite continuous-time absorbing chains. We claim no priority for those results; the contribution here is a closed source-local derivation and auditable finite certificate for the frozen interval model. AI tools assisted algebra checking, hostile mutation design, and manuscript preparation. Every theorem dependency, numerical cutoff, and nonclaim is exposed in the package.

2 S. Karlin and J. McGregor, "Coincidence probabilities," *Pacific Journal of Mathematics* 9 (1959), 1141--1164, doi:10.2140/pjm.1959.9.1141. J. N. Darroch and E. Seneta, "On quasi-stationary distributions in absorbing continuous-time finite Markov chains," *Journal of Applied Probability* 4 (1967), 192--196, doi:10.2307/3212311.
