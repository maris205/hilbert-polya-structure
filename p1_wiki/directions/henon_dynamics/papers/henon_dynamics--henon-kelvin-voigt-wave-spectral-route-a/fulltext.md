---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kelvin-voigt-wave-spectral-route-a"
canonical_tex: "henon_dynamics/henon_kelvin_voigt_wave_spectral_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kelvin_voigt_wave_spectral_route_a/paper/main.pdf"
source_sha256: "ce9f59f7bcf50d92b87f2e1ca790f2cf02d31e358f44902cffe260b12e04d74a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Essential Spectral Accumulation and Optimal Damping for a Kelvin--Voigt Wave

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kelvin_voigt_wave_spectral_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kelvin_voigt_wave_spectral_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kelvin_voigt_wave_spectral_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kelvin_voigt_wave_spectral_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We analyze the Dirichlet Kelvin--Voigt equation on the normalized interval $(0,\pi)$ at its physical time clock. Sine modes give an exact quadratic pencil. As the damping crosses $bn=2$, modes pass through underdamped, critical-Jordan, and overdamped regimes. The overdamped slow roots approach the non-eigenvalue essential spectral point $-1/b$, while the fast roots escape to minus infinity. Comparing this high-frequency mechanism with the first-mode real part yields the exact spectral-abscissa gap $\min(b/2,1/b)$ and its unique optimizer $b=\sqrt 2$. We prove the energy identity and explicitly distinguish spectral abscissa from a uniform operator-norm decay assertion at a Jordan parameter. Independent numerical, symbolic, replay, and hostile-mutation controls accompany the theorem.
author:
- HCS Research Program
date: 28 August 2026(revision 2)
title: 'Essential Spectral Accumulation and Optimal Damping for a Kelvin--Voigt Wave'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and generator

Let $$u_{tt}-u_{xx}-b\,u_{txx}=0,\qquad
 u(0,t)=u(\pi,t)=0,\qquad b\geq0 .$$ The energy is $$E(t)=\frac12\int_0^\pi \bigl(|u_t|^2+|u_x|^2\bigr)\,dx .$$ Thus the energy norm of a state is $\|(u,v)\|_E^2=\int_0^\pi(|u_x|^2+|v|^2)\,dx=2E$. For $b>0$, the first-order generator on $H_0^1(0,\pi)\times L^2(0,\pi)$ is $A(u,v)=(v,(u+bv)_{xx})$ with exact domain $$D(A)=\{(u,v)\in H_0^1(0,\pi)\times L^2(0,\pi):v\in H_0^1(0,\pi),\
u+bv\in H^2(0,\pi)\cap H_0^1(0,\pi)\}.$$ This domain statement is kept separate from the spectral-abscissa calculation.

# Root atlas

Writing $u(x,t)=\sum_{n\ge1}q_n(t)\sin(nx)$ gives $$q_n''+bn^2q_n'+n^2q_n=0,\qquad
 \lambda_{n,\pm}=\frac{-bn^2\pm\sqrt{b^2n^4-4n^2}}2 .$$

[\[thm:kv\]]{#thm:kv label="thm:kv"} For $b>0$, $bn<2$ is underdamped, $bn=2$ is a defective Jordan root $-n$, and $bn>2$ is overdamped. There are finitely many underdamped modes and at most one critical mode. In the overdamped regime, $$\lambda_{n,+}=-\frac{2n^2}{bn^2+\sqrt{b^2n^4-4n^2}}
 \longrightarrow-\frac1b\quad\hbox{from below},\qquad
 \lambda_{n,-}\longrightarrow-\infty .$$ We use the Weyl singular-sequence definition of essential spectrum. The point $-1/b$ belongs to it as an accumulation point but is not an eigenvalue of the energy generator. Indeed, if $A(u,v)=-(1/b)(u,v)$, then $v=-(1/b)u$ and the second component gives $b^{-2}u=0$ in $L^2$, hence $u=v=0$. Equivalently, substituting $\lambda=-1/b$ into $$\bigl(\lambda^2-(1+b\lambda)\partial_{xx}\bigr)u=0$$ leaves $b^{-2}u=0$. More explicitly, let $e_n(x)=\sqrt{2/\pi}\sin(nx)$, $a_n=(n^2+|\lambda_{n,+}|^2)^{-1/2}$, and $w_n=(a_ne_n,\lambda_{n,+}a_ne_n)$ for the slow overdamped roots. Then $\|w_n\|_E=1$, $w_n\rightharpoonup0$, and $$\|(A+1/b)w_n\|=|\lambda_{n,+}+1/b|\longrightarrow0 .$$ Thus the $w_n$ form a Weyl singular sequence. Since $e^{tA}w_n=e^{t\lambda_{n,+}}w_n$, their image norms tend to $e^{-t/b}>0$ for each $t>0$; consequently the positive-time semigroup is not compact or Schatten (and at $t=0$ it is the identity).

The spectral-abscissa gap is exactly $$\gamma(b)=-\sup\{\Re\lambda_{n,\pm}:n\ge1\}
          =\min\left(\frac b2,\frac1b\right).$$ It has the unique maximizer $b_\star=\sqrt2$ and $\gamma(b_\star)=1/\sqrt2$. This is a spectral-abscissa statement; at a critical Jordan parameter it does not assert a uniform operator-norm bound with the exact exponent. Finally, $$E'(t)=-b\int_0^\pi |u_{tx}|^2\,dx\leq0 .$$ At $b=0$, $\lambda_{n,\pm}=\pm in$ and the undamped wave group is unitary.

The sine expansion proves the quadratic pencil. The discriminant gives the three regimes and the double-root Jordan form. For an overdamped mode, rationalizing the plus root gives the displayed expression; it is strictly below $-1/b$, and its limit is $-1/b$. In the underdamped range the largest real part is $-bn^2/2$, maximized at $n=1$; in the overdamped range every slow root is below $-1/b$. Therefore the supremum of real parts is $\max(-b/2,-1/b)$, proving the gap formula. The two positive branches $b/2$ and $1/b$ meet only at $b=\sqrt2$, which is the unique maximizer. The direct substitution above proves non-eigenvalue status. The displayed eigenvectors are orthogonal across sine modes, so they converge weakly to zero; their eigenvalue equation gives the residual identity, and the slow-root limit makes it vanish. Multiplication of the PDE by $u_t$, integration by parts, and the Dirichlet boundary conditions give the energy identity.

\>0

# Boundary and interpretation

The critical faces $b=2/n$ are retained rather than smoothed away. A Jordan block produces a polynomial prefactor in its modal solution, so the spectral-abscissa gap should not be silently upgraded to an exact uniform norm-decay constant. The point $-1/b$ is a limit point of eigenvalues, not a hidden eigenmode. The $b=0$ unitary problem is a separate boundary model.

\>1

# Independent audit and Route-A boundary

The released ledger contains six damping cases and 384 modal roots through $n=64$, including the first critical and undamped faces. An independent checker recomputes every root, Vieta identity, regime, asymptotic side, gap, and optimizer. SymPy checks the pencil and energy algebra; byte replay is exact, and repaired/stale hash mutations are all rejected.

The Route-A tuple is

(A0\_FAIL, A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_FORMAL\_HINT),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.

The registered scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. The sine index is not claimed to be an arithmetic primitive owner; no target prime, zero, local factor, root number, automorphy statement, functional equation, or Hilbert--Polya operator is introduced.

# Source note {#source-note .unnumbered}

Kelvin--Voigt spectral context includes Guo, Wang, and Zhang [@gwz2010] and Jing Wang and Jun-Min Wang [@ww2014]. Damped-string decay and interval determinant context are recorded by Cox and Zuazua [@cz1994] and Freitas and Lipovský [@fl2019]; none is used to assert an unproved norm estimate.

9 B. Z. Guo, J. M. Wang, and G. D. Zhang, *Spectral analysis of a wave equation with Kelvin--Voigt damping*, *ZAMM* 90 (2010), 323--342. DOI: 10.1002/zamm.200900275. Jing Wang and Jun-Min Wang, *Spectral analysis and exponential stability of one-dimensional wave equation with viscoelastic damping*, *Journal of Mathematical Analysis and Applications* 410 (2014), 499--512. DOI: 10.1016/j.jmaa.2013.08.034. S. Cox and E. Zuazua, *The rate at which energy decays in a damped string*, *Communications in Partial Differential Equations* 19 (1994), 213--243. DOI: 10.1080/03605309408821015. P. Freitas and J. Lipovský, *Spectral determinant for the damped wave equation on an interval*, *Acta Physica Polonica A* 136 (2019), 817--823. DOI: 10.12693/APhysPolA.136.817.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic or operator claim. **Data and code.** The theorem, ledger, independent checks, and build instructions are released with HCS-C218. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked the displayed claims and metadata. This is not external peer review.
