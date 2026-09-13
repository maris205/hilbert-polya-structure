---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-one-dimensional-iid-rwre-solomon-phase-route-a"
canonical_tex: "henon_dynamics/henon_one_dimensional_iid_rwre_solomon_phase_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_one_dimensional_iid_rwre_solomon_phase_route_a/paper/main.pdf"
source_sha256: "7d51e03d0c2638af0ef516af74944830cc586884570ad8ca05ecafcfb7ca746c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Direction, Ballisticity, and the Zero-Speed Chamber for One-Dimensional IID Random Environment

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_one_dimensional_iid_rwre_solomon_phase_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_one_dimensional_iid_rwre_solomon_phase_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_one_dimensional_iid_rwre_solomon_phase_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_one_dimensional_iid_rwre_solomon_phase_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-complete reconstruction of the one-dimensional iid nearest-neighbour random walk in random environment. One theorem joins the quenched finite-interval scale function, the log-bias direction trichotomy, the annealed almost-sure velocity, and the full transient zero-speed region. The latter is proved analytically: stationary ergodic crossing times are truncated before Birkhoff's theorem, forcing infinite passage time per unit distance and hence zero speed. Beta and constant environments close all stated parameter faces. Exact finite ledgers are regression receipts only. No priority, arithmetic-target, Euler-factor, root-number, target-zero, or Hilbert--Pólya claim is made.
author:
- 'HCS-C348 source-local reconstruction'
date: 3 September 2026
title: |
  Direction, Ballisticity, and the Zero-Speed Chamber\
  for One-Dimensional IID Random Environment
```

## Markdown 正文

**Revision certificate.** =0 Scale and direction closure. =1 Round-one speed and Beta closure. Round-two evidence and boundary closure.

# Frozen model and the two laws

Let $(\Omega,\mathcal F,\mathbf P)$ carry iid variables $\omega=(\omega_x)_{x\in\mathbb Z}$ such that $$0<\omega_x<1,\qquad
\rho_x=\frac{1-\omega_x}{\omega_x},\qquad
\mathbf E|\log\rho_0|<\infty.                                      \tag{1}$$ Given the complete frozen environment, the quenched law $P_\omega^z$ is the Markov law started at $z$ with $$P_\omega(X_{n+1}=x+1\mid X_n=x)=\omega_x,
\quad
P_\omega(X_{n+1}=x-1\mid X_n=x)=1-\omega_x.                 \tag{2}$$ The annealed law is $\mathbb P^z(d\omega,dX)=\mathbf P(d\omega)P_\omega^z(dX)$. Thus the medium is sampled once; annealing does not resample $\omega_x$ on a revisit. Put $T_y=\inf\{n\geq0:X_n=y\}$ and $m=\mathbf E\log\rho_0$.

[\[thm:main\]]{#thm:main label="thm:main"} Under *(1)* the following statements hold.

1.  For integers $a<x<b$, define $R_a=1$ and $R_k=\prod_{j=a+1}^{k}\rho_j$. Then $$P_\omega^x(T_b<T_a)
    =\frac{\sum_{k=a}^{x-1}R_k}{\sum_{k=a}^{b-1}R_k}.            \tag{3}$$

2.  For $\mathbf P$-almost every $\omega$, the following holds $P_\omega^0$-almost surely: $$\begin{array}{c|c}
    m<0&X_n\to+\infty,\\
    m=0&\liminf X_n=-\infty\ \hbox{and}\ \limsup X_n=+\infty,\\
    m>0&X_n\to-\infty.
    \end{array}                                                   \tag{4}$$

3.  Under $\mathbb P^0$, and therefore under $P_\omega^0$ for $\mathbf P$-almost every environment, $$\frac{X_n}{n}\longrightarrow v
    =\begin{cases}
    \dfrac{1-\mathbf E\rho_0}{1+\mathbf E\rho_0},&\mathbf E\rho_0<1,\\[5pt]
    -\dfrac{1-\mathbf E\rho_0^{-1}}{1+\mathbf E\rho_0^{-1}},
       &\mathbf E\rho_0^{-1}<1,\\[5pt]
    0,&\text{otherwise}.
    \end{cases}                                                   \tag{5}$$ The two nonzero cases are disjoint.

# Scale and direction

Let $h(i)=P_\omega^i(T_b<T_a)$. It is the unique solution of $$h(i)=\omega_i h(i+1)+(1-\omega_i)h(i-1),\qquad h(a)=0, h(b)=1.$$ For $\Delta_i=h(i)-h(i-1)$, this becomes $\Delta_{i+1}=\rho_i\Delta_i$. Hence $\Delta_{k+1}=R_k\Delta_{a+1}$. Summing and imposing the two boundary values gives (3); positivity of the denominator gives uniqueness.

For the infinite line define the two-sided potential $$V(0)=0,\quad V(n)=\sum_{j=1}^{n}\log\rho_j\ (n>0),\quad
V(n)=-\sum_{j=n+1}^{0}\log\rho_j\ (n<0).                    \tag{6}$$ The strong law gives $V(n)/n\to m$ at both ends. If $m<0$, scale weights decay to the right and grow to the left. Sending the barriers in (3) to infinity shows that every positive level is hit and every fixed level is visited only finitely often; thus $X_n\to+\infty$. Reflection gives the case $m>0$. If $m=0$, the iid sums in (6) oscillate at both ends unless they vanish identically; the latter is the simple symmetric environment. Both one-sided scale sums diverge in either case, and (3) shows that every integer is hit. This proves (4).

\>0

# Stationary crossings and velocity

The point of this section is to retain the infinite-mean step rather than silently infer zero speed from a divergent expectation.

[\[lem:crossing\]]{#lem:crossing label="lem:crossing"} Suppose every positive level is hit and set $\tau_i=T_i-T_{i-1}$, $i\geq1$. Under $\mathbb P^0$, the sequence $(\tau_i)$ is stationary and ergodic. Moreover $$E_\omega^0T_1=1+2\sum_{k\leq0}\prod_{j=k}^{0}\rho_j,         \tag{7}$$ where infinity is allowed, and in the iid case $$\mathbb E\tau_1=1+2\sum_{r\geq1}(\mathbf E\rho_0)^r.              \tag{8}$$

Quenched strong Markov makes successive post-hitting segments conditionally independent, with spatially shifted one-crossing laws. Thus their joint annealed law has a product-extension representation $$\tau_i=F(\theta^{i-1}\omega,U_i).$$ Here the auxiliary rows $U_i$ are iid and independent of $\omega$. Their simultaneous spatial shift with the iid environment is Bernoulli, hence mixing and ergodic, and the crossing array is its factor. This does not make the annealed $\tau_i$ independent: they share $\omega$. Locally, $\tau_i\wedge K$ uses only $U_i$ and sites reachable before time $K$.

Let $a_i=E_\omega^iT_{i+1}$. First-step decomposition gives $$a_i=1+(1-\omega_i)(a_{i-1}+a_i)
    =1+\rho_i+\rho_i a_{i-1}.$$ Iteration toward $-\infty$, first with a finite barrier and then by monotone convergence, proves (7). Tonelli and iid factorization give (8).

If $r=\mathbf E\rho_0<1$, (8) gives $$\mu:=\mathbb E\tau_1=\frac{1+r}{1-r}.                       \tag{9}$$ Birkhoff yields $T_n/n\to\mu$. Integrability also gives $\tau_n/n\to0$: for every $\varepsilon>0$, $$\sum_{n\geq1}\mathbb P(\tau_n>\varepsilon n)
=\sum_{n\geq1}\mathbb P(\tau_1>\varepsilon n)<\infty,            \tag{10}$$ so Borel--Cantelli applies without independence. Let $M_t=\max_{s\leq t}X_s=\max\{n:T_n\leq t\}$. Inverting passage times gives $M_t/t\to1/\mu$. Before the unfinished crossing to $M_t+1$, the depth below $M_t$ is at most $\tau_{M_t+1}=o(t)$; hence $X_t/t\to1/\mu=(1-r)/(1+r)$.

If $\mathbf E\rho_0\geq1$, then $\mathbb E\tau_1=\infty$. For every finite $K$, Birkhoff applied to $\tau_i\wedge K$ gives $$\liminf_{n\to\infty}\frac{T_n}{n}
\geq\mathbb E(\tau_1\wedge K).$$ Letting $K\to\infty$ proves the almost-sure statement $T_n/n\to\infty$, and therefore $M_t/t\to0$. In the right transient case, eventually $0\leq X_t\leq M_t$, so $X_t/t\to0$. This is the transient zero-speed chamber.

In the recurrent case the same argument controls the positive maximum, while its reflected version controls the negative minimum, proving $|X_t|/t\to0$. For left transience reflect space; its bias is $\rho'_x=\rho_{-x}^{-1}$, giving the second line of (5). Finally $(\mathbf E\rho_0)(\mathbf E\rho_0^{-1})\geq1$ by Cauchy--Schwarz, so both ballistic conditions cannot hold. This completes Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

For any annealed probability-one event $A$ just proved, Fubini gives $1=\mathbb P^0(A)=\int P_\omega^0(A)\,\mathbf P(d\omega)$. Thus $P_\omega^0(A)=1$ for $\mathbf P$-almost every $\omega$, not for every environment.

# Beta and homogeneous faces

[\[cor:beta\]]{#cor:beta label="cor:beta"} If $\omega_0\sim\operatorname{Beta}(\alpha,\beta)$, $\alpha,\beta>0$, direction is right, recurrent, or left according as $\alpha>\beta$, $\alpha=\beta$, or $\alpha<\beta$, and $$v=\begin{cases}
\dfrac{\alpha-\beta-1}{\alpha+\beta-1},&\alpha>\beta+1,\\[5pt]
-\dfrac{\beta-\alpha-1}{\alpha+\beta-1},&\beta>\alpha+1,\\[5pt]
0,&|\alpha-\beta|\leq1.
\end{cases}                                                   \tag{11}$$ For $\omega_x=p$ deterministically, $v=2p-1$.

Beta integrals give $$\mathbf E\log\rho=\psi(\beta)-\psi(\alpha),\quad
\mathbf E\rho=\frac{\beta}{\alpha-1}\ (\alpha>1),\quad
\mathbf E\rho^{-1}=\frac{\alpha}{\beta-1}\ (\beta>1),            \tag{12}$$ with the relevant moment infinite otherwise. The digamma function is strictly increasing. Substitution in (4)--(5) gives (11), including the two unit-difference zero-speed walls. In the constant case $\rho=(1-p)/p$, and $(1-\rho)/(1+\rho)=2p-1$; reflection covers $p<1/2$.

\>1

# Exact receipt, boundaries, and collision audit

The canonical receipt uses rational arithmetic throughout. It contains the following complete finite panels.

  panel                                                       rows
  -------------------------------------------------------- -------
  integer Beta parameters $1\leq\alpha,\beta\leq20$            400
  rational two-atom environment laws                           280
  finite environment words, interior length at most four       780
  finite-interval starting-point probabilities               2,930
  constant environments                                          5

For integer Beta parameters the digamma difference is the exact harmonic number difference $H_{\beta-1}-H_{\alpha-1}$. For a two-atom law with weight $r/m$, the sign of $\mathbf E\log\rho$ is checked by comparing the rational number $\rho_1^r\rho_2^{m-r}$ with one. These ledgers catch normalization and chamber errors. They do not prove an infinite-environment almost-sure theorem; Sections 2--3 do.

Atoms at $\omega=0$ or $1$, non-iid media, dynamic environments, higher dimensions, and non-nearest-neighbour jumps are outside the theorem. No central limit, slowdown, localization, or large-deviation result is asserted. C342 concerns finite directed Dirichlet rows and annealed edge reinforcement, whereas the present owner is a frozen iid scalar medium on $\mathbb Z$. C273 has homogeneous iid increments, and C253 is a finite Moran absorption chain.

The strict Route-A tuple is $(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)$, with overall verdict `ROUTE_A_REJECTED` and Route B false. Scale products and random crossings are source probability objects, not rational-prime carriers, primitive arithmetic orbits, target Euler factors, a target divisor, or a Hilbert--Pólya operator.

# Source and ownership note

Solomon's primary paper [@Solomon1975] owns the classical iid direction and speed theorem. Zeitouni's review [@Zeitouni2004] supplies an authoritative later formulation. Our contribution is a source-local, auditable reconstruction joining the proof, exact regression receipt, boundary atlas, and Route-A evaluation. We make no priority claim.

9 F. Solomon, Random walks in a random environment, *Ann. Probab.* **3** (1975), 1--31. <https://doi.org/10.1214/AOP/1176996444>.

O. Zeitouni, Random walks in random environment, in *Lectures on Probability Theory and Statistics*, Lecture Notes in Mathematics 1837, Springer (2004), 189--312. <https://doi.org/10.1007/978-3-540-39874-5_2>.
