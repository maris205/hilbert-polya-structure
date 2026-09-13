---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-airy-talbot-revival-route-a"
canonical_tex: "henon_dynamics/henon_airy_talbot_revival_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_airy_talbot_revival_route_a/paper/main.pdf"
source_sha256: "6a3526d7eccb40cead5619193b8f2a4265b777f9679db0eaa0ecc0352e6f5271"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cubic Talbot Revivals and Fixed-Mode Geometry for the Periodic Airy Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_airy_talbot_revival_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_airy_talbot_revival_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_airy_talbot_revival_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_airy_talbot_revival_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give an all-time operator atlas for the periodic Airy equation. Its Fourier flow is a strongly continuous unitary group with least full-space period $2\pi$. At every reduced rational time $2\pi p/q$, the propagator is an exact cubic discrete-Fourier sum of $q$ spatial translations and has global order $q$. \>0 We also classify its full fixed subspace by prime valuations, all minimum periods of finite-spectrum states, and the irrational fixed-space boundary. The receipt independently checks 2,806 strobes and 101 high-precision DFTs. \>1 The canonical cubic generator is source-native, but its unitary maps are noncompact and not trace class. No arithmetic or Hilbert--Pólya claim is made.
author:
- HCS Research Program
date: 31 August 2026(revision 2)
title: |
  Cubic Talbot Revivals and Fixed-Mode Geometry\
  for the Periodic Airy Flow
```

## Markdown 正文

suppressoptionalinfo 611 trailerid \[\<C2612026083100000000000000000000\>\<C2612026083100000000000000000000\>\]

Periodic and nonperiodic Airy revival phenomena provide the surrounding context [@Pelloni2024; @Boulton2021]. The periodic strobe, fixed-space, and state-period classifications below are derived directly.

# Frozen flow and the global clock

On $\mathbb T=\mathbb R/(2\pi\mathbb Z)$ fix $$u_t+u_{xxx}=0,\qquad e_n(x)=\mathrm e^{\mathrm inx}.                 \label{eq:airy}$$ Writing $D=-\mathrm i\partial_x$, Fourier evolution gives $$U(t)e_n=\mathrm e^{\mathrm in^3t}e_n=\mathrm e^{\mathrm itD^3}e_n.             \label{eq:mode}$$ The real Fourier multiplier $n^3$ makes $D^3$ self-adjoint on its Sobolev domain. Parseval and dominated convergence therefore prove that $U(t)$ is a strongly continuous unitary group on $L^2(\mathbb T)$.

If $U(t)=I$, the mode $n=1$ forces $t\in2\pi\mathbb Z$; conversely every integer cube has integral phase at such times. Thus $2\pi$ is the least positive return of the *whole* phase space. This is distinct from the often shorter return of an individual state.

# Complete rational-revival theorem

[\[thm:revival\]]{#thm:revival label="thm:revival"} Let $(p,q)=1$ and $q\ge1$. At $t=2\pi p/q$, $$U(t)f=\sum_{r=0}^{q-1}A_{p,q}(r)\,
 \tau_{2\pi r/q}f,
 \quad
 A_{p,q}(r)=\frac1q\sum_{s=0}^{q-1}
 \mathrm e^{2\pi\mathrm i(ps^3-sr)/q},                              \label{eq:dft}$$ where $\tau_a f(x)=f(x+a)$. Moreover

1.  $\sum_r|A_{p,q}(r)|^2=1$ and the strobe has exact order $q$;

2.  its fixed space is $$\overline{\operatorname{span}}\{e_n:q\mid n^3\}
     =\overline{\operatorname{span}}\{e_n:L(q)\mid n\},
     \quad L(q)=\prod_{\ell^a\parallel q}\ell^{\lceil a/3\rceil};$$

3.  if $t/(2\pi)$ is irrational, the fixed space of $U(t)$ consists exactly of constants.

#### Proof.

The identity $$(n+q)^3-n^3=q(3n^2+3nq+q^2)$$ makes the multiplier in [\[eq:mode\]](#eq:mode){reference-type="eqref" reference="eq:mode"} $q$-periodic in $n$. Finite Fourier inversion yields [\[eq:dft\]](#eq:dft){reference-type="eqref" reference="eq:dft"}; its unit-modulus input vector gives Parseval. The $q$th power is the identity, while the mode-one phase forces any order to be divisible by $q$. Finally, $q\mid n^3$ is equivalent prime by prime to $v_\ell(n)\ge\lceil v_\ell(q)/3\rceil$. At irrational time, fixing a nonzero mode would make $n^3t/(2\pi)$ an integer, a contradiction.

=0 The baseline stops with the all-rational revival theorem. Fixed-support state periods, executable receipts, and operator boundaries are added only in later revisions.

\>0

# Individual periods and independent receipt

Let a nonconstant state have finite nonzero Fourier support $S$. Simultaneous return requires $Tn^3\in2\pi\mathbb Z$ for every $n\in S$, hence its least positive period is $$T_S=\frac{2\pi}{\gcd\{|n|^3:n\in S,\ n\ne0\}}.          \label{eq:state}$$ Constants are fixed at every time and have no least positive period. Formula [\[eq:state\]](#eq:state){reference-type="eqref" reference="eq:state"} separates state recurrence from the global $2\pi$ clock.

The producer covers all reduced $(p,q)$ through $q=96$: 2,806 exact phase vectors are retained by cryptographic digest, together with the valuation stride and a 1,025-mode fixed-count window. For every reduced pair through $q=18$, it also stores the full 90-decimal DFT and inverse: 101 transforms.

  receipt                rows    independent tests mathematical sentinel
  ------------------- ------- -------------------- -----------------------------
  rational strobes      2,806         50,765 total mode-one order, $q\mid n^3$
  cubic DFT               101   inverse + Parseval translated-copy identity
  finite supports          10   gcd reconstruction least state period
  symbolic/modular        ---              301,200 cubic and valuation laws
  hostile mutations        41          41 rejected repaired payload hashes

The checker imports no producer function. It reconstructs modular phases, prime valuations, complex coefficients, inverse DFTs, and support gcds. Finite rows test implementation; Theorem [\[thm:revival\]](#thm:revival){reference-type="ref" reference="thm:revival"} is not inferred from a cutoff.

\>1

# Operator, collision, and Route-A boundaries

For every $t$, the sequence $\{U(t)e_n\}$ is orthonormal and therefore has no norm-convergent subsequence. Thus $U(t)$ is noncompact on $L^2(\mathbb T)$, in particular neither trace class nor a source for the desired infinite-dimensional Fredholm determinant. The self-adjoint $D^3$ is a natural source quantization, but its integer-cube spectrum has no target-zero identification.

C195 (viscous Burgers), C206 (Couette), C217 (rotating shallow water), C221 (cubic NLS), and C256 (KdV cnoidal profiles) do not own the cubic rational- time revival operator. This is workspace bookkeeping, not a priority claim. The strict assessment is $$\texttt{(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,
A4\_NATURAL\_QUANTIZATION)},$$ with `ROUTE_A_REJECTED` and Route B false. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. There is no arithmetic local data, Euler factor, root number, automorphy, target divisor or functional equation, target determinant, target zero match, or Hilbert--Pólya operator.

# Conclusion and limitations

One theorem now controls the complete periodic Airy group, every rational revival, every sampled fixed subspace, and every finite-support period. It does not classify nonperiodic third-order boundary conditions, evaluate all cubic Gauss sums in closed form, or extend to nonlinear KdV.

9 B. Pelloni and D. A. Smith, "Revivals, or the Talbot effect, for the Airy equation," *Studies in Applied Mathematics* 153 (2024), e12699, [doi:10.1111/sapm.12699](https://doi.org/10.1111/sapm.12699). L. Boulton, G. Farmakis, and B. Pelloni, "Beyond periodic revivals for linear dispersive PDEs," *Proceedings of the Royal Society A* 477 (2021), 20210241, [doi:10.1098/rspa.2021.0241](https://doi.org/10.1098/rspa.2021.0241).
