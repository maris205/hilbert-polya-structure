---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-sine-gordon-kink-breather-route-a"
canonical_tex: "henon_dynamics/henon_sine_gordon_kink_breather_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_sine_gordon_kink_breather_route_a/paper/main.pdf"
source_sha256: "4bfcb7154183b6fddbab42d0a9533615207ca34da325919a55dc251733f8575c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Kinks, Breathers, and the Rest-Kink Spectrum in the Sine--Gordon Equation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_sine_gordon_kink_breather_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_sine_gordon_kink_breather_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_sine_gordon_kink_breather_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_sine_gordon_kink_breather_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a source-local theorem for the one-dimensional sine--Gordonequation $u_{tt}-u_{xx}+\sin u=0$. The declared coherent families close exactly: finite-energy monotone travelling heteroclinics in every integer vacuum layer are the subluminal Lorentz kink and antikink, while the zero-charge breathers have an explicit rest frequency and a Lorentz energy--momentum ledger. At the rest kink the Hessian is the factored Pöschl--Teller operator with translation kernel and essential edge one. The period $2\pi/\Omega$ is a comoving breather clock, not a fixed-laboratory-point period after a nonzero boost. This is not a classification of every finite-energy solution and it is not an arithmetic or Hilbert--Pólya construction.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Kinks, Breathers, and the Rest-Kink Spectrum in the Sine--Gordon Equation'
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen model and travelling heteroclinics

We use the potential $V(u)=1-\cos u$, with vacua $u=2\pi k$, and define $$E[u]=\int_{\mathbb R}\left[\frac12(u_t^2+u_x^2)+1-\cos u\right]\,\mathrm dx,
 \qquad P[u]=-\int_{\mathbb R}u_tu_x\,\mathrm dx .
 \label{eq:ledger}$$ The minus sign in $P$ is fixed here and in the certificate. We begin with the unrestricted ansatz $u(x,t)=U(x-vt)$, whose profile equation is $(v^2-1)U''+\sin U=0$; the speed inequality in the theorem justifies the Lorentz coordinate $\xi=\gamma_v(x-vt-x_0)$.

[\[thm:kink\]]{#thm:kink label="thm:kink"} Every nonconstant finite-energy monotone travelling heteroclinic in the declared family has an integer vacuum layer $k\in\mathbb Z$ and, up to translation, is $$U_{k,+}(\xi)=2\pi k+4\arctan(e^\xi),\qquad
 U_{k,-}(\xi)=2\pi k+4\arctan(e^{-\xi}),
 \label{eq:kink}$$ and necessarily $|v|<1$. Their charges are $Q=+1$ and $Q=-1$, and $$E=8\gamma_v,\qquad P=8\gamma_vv,\qquad E^2-P^2=64 .
 \label{eq:massshell}$$

Multiplying the unrestricted profile equation $(v^2-1)U''+\sin U=0$ by $U'$ and using the vacuum limits gives $$\tfrac12(v^2-1)(U')^2=\cos U-1.$$ The right side is nonpositive and a nonconstant heteroclinic has $U'\ne0$ on an open set, hence $v^2-1<0$ and $|v|<1$. In the resulting Lorentz coordinate, the first integral is $\tfrac12(U')^2=1-\cos U$. Monotonicity and the $2\pi$-periodicity of the potential select the integer-layer profiles [\[eq:kink\]](#eq:kink){reference-type="eqref" reference="eq:kink"}; the opposite sign is the antikink. In the canonical $k=0$ rest frame $U_+'=2\operatorname{sech}\xi$ and $\int 4\operatorname{sech}^2\xi\,\mathrm d\xi=8$. Lorentz change of variables gives [\[eq:massshell\]](#eq:massshell){reference-type="eqref" reference="eq:massshell"} with the convention [\[eq:ledger\]](#eq:ledger){reference-type="eqref" reference="eq:ledger"}.

=0

# Baseline breather identity

The second declared coherent family already appears at the baseline stage. If $0<\Omega<1$ and $\eta^2+\Omega^2=1$, then $$u_B(x,t)=4\arctan\!\left(\frac{\eta\sin(\Omega t)}
 {\Omega\cosh(\eta x)}\right)
 \label{eq:baselinebreather}$$ solves the equation by the rational identity $\sin(4\arctan q)=4q(1-q^2)/(1+q^2)^2$. Its spatial limits agree, so $Q=0$, while the rest-frame clock is $2\pi/\Omega$. This baseline records the exact formulas only; boosts, spectral details, and the reproducibility receipt are deliberately added in the later revision rounds.

The two families therefore have different geometric roles from the outset: the kink is a heteroclinic carrying charge, whereas the breather returns in a continuous frequency family. A continuous frequency label is not an isolated primitive-periodic owner.

\>0

# Breathers and the Lorentz ledger

For $0<\Omega<1$ let $\eta=(1-\Omega^2)^{1/2}$. The exact rest breather is $$u_B(x,t)=4\arctan\!\left(\frac{\eta\sin(\Omega t)}
 {\Omega\cosh(\eta x)}\right).
 \label{eq:breather}$$ It has $Q=0$, rest momentum zero, rest energy $E_0=16\eta$, and internal period $T_0=2\pi/\Omega$. For $|V|<1$, set $$\xi=\gamma_V(x-Vt),\qquad \tau=\gamma_V(t-Vx),\qquad
 \gamma_V=(1-V^2)^{-1/2},
 \label{eq:boost}$$ and replace $(x,t)$ in [\[eq:breather\]](#eq:breather){reference-type="eqref" reference="eq:breather"} by $(\xi,\tau)$. Then $$E=16\eta\gamma_V,\qquad P=16\eta\gamma_VV,
 \qquad E^2-P^2=(16\eta)^2 .
 \label{eq:breatherledger}$$ The period $T_0$ belongs to the rest/comoving proper clock. For $V\ne0$ we make no claim of a strict period at a fixed laboratory $x$; the dependence of $\tau$ on both $t$ and $x$ is essential. At $V=0$ the rest statement is the usual fixed-$x$ period.

For smooth finite-energy solutions, the stress-energy identity gives $\frac{\,\mathrm d}{\,\mathrm dt}E=0$ and $\frac{\,\mathrm d}{\,\mathrm dt}P=0$ (boundary fluxes vanish). Thus the two ledgers above are exact identities, not fitted numerical laws.

  face                  coherent object   limiting statement
  --------------------- ----------------- ----------------------------------------
  $|v|\uparrow1$        kink              width collapses; $E,|P|\to\infty$
  $\Omega\uparrow1$     breather          zero-amplitude vacuum; $E_0\to0$
  $\Omega\downarrow0$   breather          infinite-period separatrix; $E_0\to16$
  $V=0$ / $V\ne0$       breather          rest clock / comoving clock only

  : Boundary faces retained by the certificate.

\>1

# Rest-kink Hessian and spectral boundary

At $v=0$, linearization about $U_+$ gives $$L_K=-\partial_x^2+\cos U_+(x)
     =-\partial_x^2+1-2\operatorname{sech}^2x .
 \label{eq:hessian}$$ With $A=\partial_x+\tanh x$ and $A^*=-\partial_x+\tanh x$, $$L_K=A^*A,\qquad L_K(2\operatorname{sech}x)=0 .
 \label{eq:factor}$$

[\[prop:spectrum\]]{#prop:spectrum label="prop:spectrum"} On $L^2(\mathbb R)$ with the standard $H^2$ domain, $$\sigma(L_K)=\{0\}\cup[1,\infty),\qquad
 \ker L_K=\operatorname{span}\{2\operatorname{sech}x\}.$$ There is no internal discrete mode below the essential edge.

The factorization makes $L_K$ nonnegative and the first-order equation $Af=0$ gives the unique square-integrable zero mode. The potential tends to one at both ends, so Weyl comparison gives essential spectrum $[1,\infty)$. The one-dimensional Pöschl--Teller intertwining (equivalently, the Sturm oscillation count) leaves no additional bound state for this $2\operatorname{sech}^2$ well.

# Scope boundary and reproducibility

The statement above is a declared coherent-family theorem, not a classification of every finite-energy sine--Gordon field, and the rest-kink spectrum is not a boosted-breather nonlinear stability theorem. The breather frequency is a continuous parameter, so these solutions do not furnish an isolated primitive periodic-orbit owner. Accordingly the locked Route-A record is

(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_NATURAL\_QUANTIZATION),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.\
The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target primes or zeros, Euler factors, root numbers, automorphy, target divisors, or Hilbert--Pólya operator are used.

The receipt has 6 kink, 6 breather, 5 Hessian, 8 boundary, and 4 Lorentz rows. Its producer-independent checker (289 assertions), symbolic cross-check, byte replay, and 41/41 repaired-hash hostile mutations are part of the artifact. Two fresh fixed-epoch builds are required for each of the three revision rounds.

# Source note {#source-note .unnumbered}

The classical fluxon context is recorded by McLaughlin and Scott [@ms]; all displayed formulas and limits are re-derived in this source-local artifact, and the citation is not a priority or completeness claim.

9 J. M. McLaughlin and A. C. Scott, "Perturbation analysis of fluxon dynamics," *Physical Review A* 18(4), 1652--1680 (1978). DOI: [10.1103/PhysRevA.18.1652](https://doi.org/10.1103/PhysRevA.18.1652).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, primitive-orbit, or Hilbert--Pólya claim. **Data and code.** The exact profiles, ledgers, spectrum, independent checks, and build instructions are released with HCS-C236. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked displayed claims and metadata. This is not external peer review.
