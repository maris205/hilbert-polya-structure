---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kramers-harmonic-langevin-mehler-route-a"
canonical_tex: "henon_dynamics/henon_kramers_harmonic_langevin_mehler_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kramers_harmonic_langevin_mehler_route_a/paper/main.pdf"
source_sha256: "fe8ed33ffeebb163c1d592784df135353afad4fcca064e300c52297674a861dd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Damping Mehler and Critical-Rate Identities for the Harmonic Kramers Diffusion

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kramers_harmonic_langevin_mehler_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kramers_harmonic_langevin_mehler_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kramers_harmonic_langevin_mehler_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kramers_harmonic_langevin_mehler_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give one exact finite-dimensional theorem for the harmonic Kramers--Langevin diffusion across underdamped, critically damped, overdamped, and zero-damping faces. A single matrix-exponential formula yields the Gaussian Mehler transition and the Lyapunov covariance difference. The Gibbs law, the positive-damping Kalman bracket, stationary correlations, and the drift spectral-abscissa rate are then explicit. Critical damping maximizes the asymptotic exponent but retains a $t e^{-\omega t}$ Jordan prefactor. This is a stochastic Markov result, not an arithmetic zeta or a Hilbert--Pólya construction. Independent exact reconstruction (411 assertions), symbolic checks (26 identities), byte replay and 32 hostile mutations accompany the two substantive revisions. The boundary atlas is independently checked row by row, including the underdamped, critical, overdamped and zero-damping cases.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'All-Damping Mehler and Critical-Rate Identities for the Harmonic Kramers Diffusion'
```

## Markdown 正文

suppressoptionalinfo 611

# Object and boundary atlas

Fix physical time $t\geq0$ and $$dQ_t=P_t\,dt,\qquad
dP_t=(-\omega^2Q_t-\gamma P_t)\,dt+\sqrt{2\gamma/\beta}\,dW_t,
\quad \omega,\beta>0,\ \gamma\geq0. \tag{1}$$ For $X=(Q,P)^T$, let $A=\left[\begin{smallmatrix}0&1\\-\omega^2&-\gamma\end{smallmatrix}\right]$. The $\gamma=0$ face is a deterministic Hamiltonian oscillator. The $\omega=0$ face is kept separate: position is unconfined and there is no finite Gibbs probability with the covariance below.

[\[thm:flow\]]{#thm:flow label="thm:flow"} Put $\alpha=\gamma/2$. If $\alpha<\omega$, set $\nu=(\omega^2-\alpha^2)^{1/2}$ and $(c,s)=(\cos(\nu t),\sin(\nu t)/\nu)$. If $\alpha=\omega$, set $(c,s)=(1,t)$. If $\alpha>\omega$, set $\delta=(\alpha^2-\omega^2)^{1/2}$ and $(c,s)=(\cosh(\delta t),\sinh(\delta t)/\delta)$. Then $$M_t=e^{tA}=e^{-\alpha t}
\begin{pmatrix}c+\alpha s&s\\-\omega^2s&c-\alpha s\end{pmatrix},
\quad M_0=I,\quad \det M_t=e^{-\gamma t}. \tag{2}$$ For $\gamma>0$ and $t>0$, $$X_t\mid X_0=x\sim\mathcal N(M_tx,C_t),\qquad
C_t=\Sigma-M_t\Sigma M_t^T,\qquad
\Sigma=\operatorname{diag}\!\left(\frac1{\beta\omega^2},\frac1\beta\right), \tag{3}$$ and $C_t$ is positive definite. For $\gamma=0$, $C_t=0$ and the law is the Dirac mass at $M_tx$.

The characteristic polynomial is $\lambda^2+\gamma\lambda+\omega^2$. Applying the standard exponential formula to $A+\alpha I$, whose square is $(\alpha^2-\omega^2)I$, gives (2), with the limiting Jordan expression at equality. With $B=(0,\sqrt{2\gamma/\beta})^T$, direct multiplication gives $$A\Sigma+\Sigma A^T+BB^T=0. \tag{4}$$ Differentiating $M_t\Sigma M_t^T$ and integrating (4) proves (3). For $\gamma>0$, the bracket matrix $[B,AB]$ has determinant $-2\gamma/\beta\ne0$; hence the controllability Gramian, and therefore $C_t$, is positive definite for every $t>0$.

# Gibbs law, correlations, and damping rate

Equation (4) immediately gives the invariant centered Gaussian density $$\pi(q,p)=\frac{\beta\omega}{2\pi}
\exp\!\left[-\frac\beta2(\omega^2q^2+p^2)\right]. \tag{5}$$ For $\omega>0$ and $\gamma>0$ it is the unique invariant probability. Under this law, $$\operatorname{Cov}(X_t,X_0)=M_t\Sigma,\quad
C_{QQ}=\frac{m_{11}}{\beta\omega^2},\quad C_{QP}=\frac{m_{12}}\beta,
\quad C_{PQ}=\frac{m_{21}}{\beta\omega^2},\quad C_{PP}=\frac{m_{22}}\beta. \tag{6}$$

[\[prop:rate\]]{#prop:rate label="prop:rate"} The drift eigenvalues are $-\gamma/2\pm\sqrt{\gamma^2/4-\omega^2}$. The spectral-abscissa decay exponent is $$r(\omega,\gamma)=
\begin{cases}
\gamma/2,&0\leq\gamma\leq2\omega,\\
\gamma/2-\sqrt{\gamma^2/4-\omega^2},&\gamma\geq2\omega.
\end{cases} \tag{7}$$ It is maximized at critical damping, where $r=\omega$. At exactly $\gamma=2\omega$, $$M_t=e^{-\omega t}\bigl[I+t(A+\omega I)\bigr], \tag{8}$$ so the polynomial prefactor is genuine: (7) is an asymptotic exponent and not a uniform sharp bound $\|M_t\|\leq Ce^{-\omega t}$. For every $r'<\omega$ such a bound does hold.

The two roots of the characteristic polynomial give (7). The first branch increases with $\gamma$ and the second has derivative $1/2-\gamma/[4\sqrt{\gamma^2/4-\omega^2}]<0$ for $\gamma>2\omega$. The repeated-root formula gives (8), proving the prefactor statement.

# What the theorem does not claim

At $\gamma=0$, $M_t\Sigma M_t^T=\Sigma$, the transition covariance vanishes, and energy-level measures remain invariant; there is no noise or mixing. At $\omega=0$, the position coordinate is unconfined, so (5) is not a probability density. These faces do not inherit the positive-damping theorem.

The producer uses 40 exact rational regression rows (6 matrix, 8 transition, 5 correlation, 7 rate, 5 Kalman, 4 Gibbs, 5 boundary). The independent checker passes 411 assertions; SymPy passes 26 identities; clean replay is byte identical; and 32/32 hostile mutations are rejected, including repaired- hash semantic mutations for every boundary row. LuaLaTeX is built twice per round at fixed `SOURCE_DATE_EPOCH=1787875200`, with embedded subset fonts and no layout/reference warnings.

The strict Route-A verdict is $$(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},
\mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),
\qquad \mathtt{ROUTE\_A\_REJECTED}.$$ There are no prime tables, target zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, or Hilbert--Pólya operators. The Mehler kernel is a Gaussian Markov transition, not a primitive-orbit Fredholm determinant. This internal audit is not external peer review; Route B is false.

9 H. A. Kramers, "Brownian motion in a field of force and the diffusion model of chemical reactions," *Physica* 7 (1940), 284--304. [DOI](https://doi.org/10.1016/S0031-8914(40)90098-2). G. E. Uhlenbeck and L. S. Ornstein, "On the theory of the Brownian motion," *Physical Review* 36 (1930), 823--841. [DOI](https://doi.org/10.1103/PhysRev.36.823). L. Hörmander, "Hypoelliptic second order differential equations," *Acta Mathematica* 119 (1967), 147--171. [DOI](https://doi.org/10.1007/BF02392081). C. Villani, *Hypocoercivity*, Memoirs AMS 202 (2009).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, determinant or Hilbert--Pólya claim. **Data and code.** Exact formulas, controls and audit programs accompany HCS-C237. **AI-use.** Generative tools assisted drafting; internal checks validate the displayed identities. This is not external peer review.
