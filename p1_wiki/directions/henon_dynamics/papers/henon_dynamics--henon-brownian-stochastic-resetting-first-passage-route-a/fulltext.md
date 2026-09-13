---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-brownian-stochastic-resetting-first-passage-route-a"
canonical_tex: "henon_dynamics/henon_brownian_stochastic_resetting_first_passage_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_brownian_stochastic_resetting_first_passage_route_a/paper/main.pdf"
source_sha256: "465377805bc97ebd1e43c9203ffe0453f6336363e2c737ae9b69fdc275583004"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Brownian Resetting: A Renewal and First-Passage Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_brownian_stochastic_resetting_first_passage_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_brownian_stochastic_resetting_first_passage_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_brownian_stochastic_resetting_first_passage_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_brownian_stochastic_resetting_first_passage_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close a source-level theorem for one-dimensional Brownian motion with a Poisson reset to its starting point. The free process has an absolutely continuous Laplace stationary law, while the separately killed search process has an exact first-passage renewal transform. The mean hitting time, all Laplace moments, the unique positive reset optimum, and singular boundaries follow in one dimensionless calculation. The denominator is a renewal resolvent, not a dynamical zeta or a Fredholm determinant.
author:
- 'HCS--C214 research certificate'
date: 28 August 2026
title: 'Brownian Resetting: A Renewal and First-Passage Atlas'
```

## Markdown 正文

suppressoptionalinfo 611

# Two realizations

Fix $D,r,a>0$. In the free realization on $\mathbb R$, $dX_t=\sqrt{2D}\,dW_t$ between independent rate-$r$ resets to $0$. In the search realization the same process starts at $0$ and is killed at $T_a=\inf\{t\geq0:X_t=a\}$; its law on $(-\infty,a)$ is therefore sub-Markov after absorption. The stationary statement below belongs only to the free realization. The clock is physical elapsed time.

# Free renewal theorem

Let $$G_D(x,t)=\frac{1}{\sqrt{4\pi Dt}}\exp\!\left(-\frac{x^2}{4Dt}\right).$$ Conditioning on the last reset gives $$p_r(x,t\mid0)=e^{-rt}G_D(x,t)+r\int_0^t e^{-ru}G_D(x,u)\,du .
\label{eq:renewal}$$ For $x\ne0$, the integral equals $$\frac{e^{-|x|\sqrt{r/D}}\operatorname{erfc}(\frac{|x|}{2\sqrt{Dt}}-\sqrt{rt})
-e^{|x|\sqrt{r/D}}\operatorname{erfc}(\frac{|x|}{2\sqrt{Dt}}+\sqrt{rt})}{4\sqrt{Dr}},$$ and its continuous $x=0$ value is $\operatorname{erf}(\sqrt{rt})/(2\sqrt{Dr})$. For every $t>0$ this is an absolutely continuous Lebesgue density. Letting $t\to\infty$ gives the normalized free stationary law $$p_{\rm st}(x)=\frac12\sqrt{\frac rD}\,e^{-|x|\sqrt{r/D}},
\qquad \int_{\mathbb R}p_{\rm st}(x)\,dx=1.
\label{eq:stationary}$$ Equation [\[eq:stationary\]](#eq:stationary){reference-type="eqref" reference="eq:stationary"} is not a stationary claim for the killed search.

## A realization check {#a-realization-check .unnumbered}

The distinction is operational, not cosmetic. At a fixed positive time the free law is a Lebesgue density: a reset at an exactly prescribed instant has probability zero, so the renewal integral does not hide a point mass. For the search process the state space is $(-\infty,a)$ with a Dirichlet boundary at $a$; probability that has reached the boundary is removed. Thus [\[eq:stationary\]](#eq:stationary){reference-type="eqref" reference="eq:stationary"} can be used to describe long-time resetting on $\mathbb R$, but never to normalize the killed survival law.

# Killed first passage

The no-reset transform from $0$ to $a$ is $f_0(q)=e^{-a\sqrt{q/D}}$. A first-reset decomposition yields $$F_r(s):=\mathbb E[e^{-sT_a}]
 =\frac{(s+r)e^{-a\sqrt{(s+r)/D}}}
 {s+r e^{-a\sqrt{(s+r)/D}}},
\qquad s\geq0,
\label{eq:fpt}$$ and the survival transform $$S_r(s):=\int_0^\infty e^{-st}\Pr(T_a>t)\,dt
 =\frac{1-e^{-a\sqrt{(s+r)/D}}}
 {s+r e^{-a\sqrt{(s+r)/D}}}.
\label{eq:survival}$$ For $s>0$, $1-F_r(s)=sS_r(s)$; continuity at zero gives $$\mathbb E[T_a]=-F_r'(0)=S_r(0)=\frac{e^{a\sqrt{r/D}}-1}{r}.$$ All moments are finite for positive $D,r,a$. For every $n\geq0$, $$(-1)^nF_r^{(n)}(0)=\mathbb E[T_a^n],\qquad
(-1)^nS_r^{(n)}(0)=\frac{\mathbb E[T_a^{n+1}]}{n+1}.
\label{eq:moments}$$

One direct way to see [\[eq:fpt\]](#eq:fpt){reference-type="eqref" reference="eq:fpt"} is to write $f=f_0(s+r)$ for the no-reset transform during one exponentially distributed attempt. A reset before absorption contributes the factor $r(1-f)/(s+r)$ and starts an independent copy, hence $$F_r(s)=f+\frac{r(1-f)}{s+r}F_r(s).$$ This scalar renewal equation also shows why its denominator is a resolvent of attempts rather than a periodic-orbit product.

# Universal optimum and boundaries

Put $z=a\sqrt{r/D}$. Then $$\frac D{a^2}\mathbb E[T_a]=g(z):=\frac{e^z-1}{z^2}.$$ The derivative has the sign of $h(z)=z-2(1-e^{-z})$: $g(z)\to\infty$ at both endpoints, $h$ has exactly one root in $(0,\infty)$ other than the limiting root at zero, and $$z_*=1.5936242600400400923\ldots,
\qquad r_*=D(z_*/a)^2.$$ At $r=0$ there is no normalizable stationary density and the half-line MFPT is infinite; at $a=0$, $T_a=0$; at $D=0$, a reset path cannot reach a positive target. These are boundaries, not substitutions into Eq. [\[eq:fpt\]](#eq:fpt){reference-type="eqref" reference="eq:fpt"}.

# Independent certificate and scope

The JSON certificate uses 81 propagator, 27 stationary, 9 normalization, 108 transform, and 27 MFPT rows at fixed rational sentinels. The checker recomputes the renewal integral by an independent $u=y^2$ quadrature and normalizes Eq. [\[eq:stationary\]](#eq:stationary){reference-type="eqref" reference="eq:stationary"}; SymPy checks the heat equation, renewal algebra, moment jet, and optimality derivative. Byte replay and hostile repaired-hash, stale-hash, and unknown-key tests are included.

As a second-pass audit, we also test the zero-reset, zero-target, and zero-diffusivity boundaries separately. This prevents a formal substitution of a singular boundary into the positive-parameter square-root formula and makes the theorem's scope machine-checkable.

  realization     state space         quantity certified
  --------------- ------------------- -----------------------------------------------
  free reset      $\mathbb R$         density and normalized Laplace stationary law
  killed search   $(-\infty,a)$       survival mass and first-passage transform
  boundary        $r=0,\ a=0,\ D=0$   separate limiting behavior

The source formulas are attributed to Evans--Majumdar (2011); the finite certificate is a reproducibility artifact, not a priority claim. No numerical row selects $z_*$. It follows from the exact derivative of $g$, with the positive-root sign bracket independently checked at $z=1$ and $z=2$.

The release ledger records the source commit and evaluator hash alongside the payload hash. It therefore distinguishes a mathematical identity from a finite regression observation: changing even one serialized row, citation locator, or scope flag is rejected after a repaired hash. This is a provenance check, not an external peer-review score.

The source attribution is Evans--Majumdar (2011) and the resetting review by Evans--Majumdar--Schehr (2020); no priority or novelty is claimed. The strict Route-A verdict is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)},\qquad
\texttt{ROUTE\_A\_REJECTED}.$$ The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. There is no intrinsic rational-prime carrier, primitive periodic-orbit clock, arithmetic divisor, or Hilbert--Polya operator. In particular, the denominator in Eq. [\[eq:fpt\]](#eq:fpt){reference-type="eqref" reference="eq:fpt"} is never called a dynamical zeta.

9 M. R. Evans and S. N. Majumdar, "Diffusion with stochastic resetting," *Phys. Rev. Lett.* 106, 160601 (2011), [doi:10.1103/PhysRevLett.106.160601](https://doi.org/10.1103/PhysRevLett.106.160601). M. R. Evans and S. N. Majumdar, "Diffusion with optimal resetting," *J. Phys. A* 44, 435001 (2011), [doi:10.1088/1751-8113/44/43/435001](https://doi.org/10.1088/1751-8113/44/43/435001). M. R. Evans, S. N. Majumdar and G. Schehr, "Stochastic resetting and applications," *J. Phys. A* 53, 193001 (2020), [doi:10.1088/1751-8121/ab7cfe](https://doi.org/10.1088/1751-8121/ab7cfe).
