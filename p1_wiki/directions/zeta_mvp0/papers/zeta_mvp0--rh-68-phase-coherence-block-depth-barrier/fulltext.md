---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-68-phase-coherence-block-depth-barrier"
canonical_tex: "zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier/main.pdf"
source_sha256: "e668181099cf2d7ebc2c61236db9c1e53221ec722a0222d3d69bdbbc68f953b4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Phase-Coherence Barriers to Uniform Block Krylov Depth An Exact Fourier-Ring No-Go Theorem and the Phase-Compression Escape

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-66 and RH-67 built phase-preserving block Krylov residual certificates, but left open whether the required block depth can remain uniform in a growing physical family. This paper proves that no such conclusion follows from stability, spectral radius, or Lyapunov conditioning alone.

  Let $\omega_d=e^{2\pi i/d}$, $$A_d=q\,\operatorname{diag}(1,\omega_d,\ldots,\omega_d^{d-1}),
   \qquad z_d=d^{-1/2}(1,\ldots,1)^T,$$ with fixed $0<q<1$. The normalized Krylov vectors $v_m=q^{-m}A_d^mz_d$ are the discrete Fourier basis. Hence, for every $k\le L<d$, $$\operatorname{dist}\!\left(v_L,\operatorname{span}\{v_0,\ldots,v_{k-1}\}\right)=1.$$ The canonical Lyapunov metric is $(1-q^2)^{-1}I$, with condition number one, and every residual still propagates with exact contraction $q$. Thus a depth-$k$ projection gives no directional reduction at horizon $L\ge k$; exact inclusion of that horizon requires depth $L+1$.

  We also prove a robust block version. If $p$ normalized block Krylov vectors have mutual coherence at most $\mu$, and the target has the same coherence, then $$\operatorname{dist}^2\ge
   1-\frac{p\mu^2}{1-(p-1)\mu}.$$ For block width $r$, one takes $p=kr$. A sharper computable lower bound uses the minimum Gram eigenvalue and target correlation norm.

  The numerical audit confirms the boundary. Exact rings at horizons $8,16,32,64$ require depths $9,17,33,65$ for ten-percent error. Even a half-cell deterministic phase perturbation leaves error $0.9851$ at depth $32$, horizon $32$. Conversely, phase compression opens the route: at the same horizon, arcs of widths $0,0.03,0.1,0.3,1,3,2\pi$ require depths $1,2,3,7,16,28,33$. A 256-bit Arb/Acb calculation certifies the displayed eight-point Fourier ring. This is a no-go result for universal fixed depth, not for a physical family with proved phase compression or effective-rank decay. No Stage A1 closure, arithmetic trace formula, or Hilbert--Polya conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Phase-Coherence Barriers to Uniform Block Krylov Depth\
  An Exact Fourier-Ring No-Go Theorem and the Phase-Compression Escape
```

## Markdown 正文

**Keywords:** block Krylov depth; Fourier ring; mutual coherence; phase compression; Lyapunov metric; projection lower bound.

**MSC 2020:** 47A10; 47B65; 65F35; 42A38; 15A60.

# Introduction

The recent route has separated three losses. RH-65 classified global metric conditioning, RH-66 restored cross-column phases, and RH-67 optimized the positive envelope for a physical coefficient covariance [@WangCovarianceEnvelope2026]. All three are useful only if a moderate block Krylov space captures the reached dynamics. The remaining question is whether that depth can be bounded independently of the small-noise or mesh parameter.

There is an immediate algebraic warning: Krylov dimension is controlled by a minimal polynomial, not by spectral radius [@Saad2003]. The example in this paper makes the warning exact while removing two possible excuses. The operator is normal, its contraction is fixed below one, and its canonical metric has condition number one. The obstruction is pure phase richness.

## Contributions and boundary {#contributions-and-boundary .unnumbered}

1.  We prove an exact Fourier-ring depth obstruction and show that the terminal residual retains the original contraction.

2.  We derive spectral and mutual-coherence lower bounds for perturbed and block Krylov families.

3.  We audit exact rings, deterministic phase perturbations, and compressed phase arcs.

4.  We identify the positive replacement for a fixed-depth theorem: physical phase compression, effective-rank decay, or an admissible growing-depth ledger.

The no-go theorem concerns universal assumptions. It does not assert that the folded-Gaussian packet family contains a Fourier ring.

# Exact Fourier-ring obstruction {#sec:ring}

Fix $d\ge2$, $0<q<1$, and put $$\omega_d=e^{2\pi i/d},\qquad
 A_d=q\,\operatorname{diag}(1,\omega_d,\ldots,\omega_d^{d-1}),
 \qquad
 z_d=\frac1{\sqrt d}(1,\ldots,1)^T.
 \label{eq:ring}$$ Define $v_m=q^{-m}A_d^mz_d$.

[\[thm:ring\]]{#thm:ring label="thm:ring"} The vectors $v_0,\ldots,v_{d-1}$ form an orthonormal basis. In particular, for integers $1\le k\le L<d$, $$\operatorname{dist}\!\left(v_L,
 \mathcal K_k(A_d,z_d)\right)=1,
 \qquad
 \mathcal K_k(A_d,z_d)=
 \operatorname{span}\{z_d,A_dz_d,\ldots,A_d^{k-1}z_d\}.
 \label{eq:unit-distance}$$ The first Krylov depth containing $A_d^Lz_d$ is $L+1$, while invariant closure requires depth $d$.

For $m,n\in\{0,\ldots,d-1\}$, $$\langle v_m,v_n\rangle
 =\frac1d\sum_{j=0}^{d-1}\omega_d^{j(n-m)}
 =\begin{cases}1,&m=n,\\0,&m\ne n.\end{cases}$$ Thus $\mathcal K_k$ is exactly the span of the first $k$ Fourier vectors and $v_L$ is orthogonal to it when $k\le L<d$. Distinct Fourier vectors remain linearly independent until all $d$ have appeared.

[\[prop:metric\]]{#prop:metric label="prop:metric"} The canonical Lyapunov equation gives $$M_d-A_d^*M_dA_d=I,
 \qquad M_d=(1-q^2)^{-1}I.
 \label{eq:ring-metric}$$ Hence $\operatorname{cond}(M_d)=1$ and $\left\lVert A_dx\right\rVert_{M_d}=q\left\lVert x\right\rVert_{M_d}$ for every $x$. For $k<d$, Arnoldi on $z_d$ has projected shift $H_k$ and residual $qv_k$; the residual orbit also contracts exactly by $q$.

Since $A_d=qU_d$ with $U_d$ unitary, [\[eq:ring-metric\]](#eq:ring-metric){reference-type="eqref" reference="eq:ring-metric"} is immediate. Moreover $A_dv_m=qv_{m+1}$, cyclically modulo $d$. Before closure, the next Fourier vector is orthogonal to the current Arnoldi space and has residual norm $q$.

For $L\ge k$, the projected center $V_kH_k^L e_1$ is zero because $H_k$ is a nilpotent shift. The residual identity remains exact, but it has merely moved the entire tail into a direction with the same contraction. This is why the certificate can be valid without producing a shorter horizon.

[\[cor:no-go\]]{#cor:no-go label="cor:no-go"} No bound on block Krylov depth depending only on a fixed contraction $q<1$, the canonical metric condition number, and a fixed block width can approximate all stable normal families at all growing horizons. Even with condition number one, the required scalar depth can equal $L+1$.

# Robust coherence bounds {#sec:coherence}

The exact ring is not needed for a lower bound. Let $X=[x_1,\ldots,x_p]$ have normalized, linearly independent columns, let $y$ be normalized, and set $$G=X^*X,qquad c=X^*y.
 \label{eq:gram-correlation}$$

[\[prop:spectral\]]{#prop:spectral label="prop:spectral"} One has $$\operatorname{dist}(y,\operatorname{ran}X)^2
 =1-c^*G^{-1}c
 \ge1-\frac{\left\lVert c\right\rVert^2}{\lambda_{\min}(G)}.
 \label{eq:spectral-lower}$$

The orthogonal projector is $XG^{-1}X^*$, giving the equality. The inequality follows from $G^{-1}\preceq\lambda_{\min}(G)^{-1}I$.

[\[cor:coherence\]]{#cor:coherence label="cor:coherence"} Suppose $$|\langle x_i,x_j\rangle|\le\mu\quad(i\ne j),
 \qquad |\langle x_i,y\rangle|\le\mu,
 \qquad (p-1)\mu<1.
 \label{eq:coherence-assumption}$$ Then $$\operatorname{dist}(y,\operatorname{ran}X)^2
 \ge1-\frac{p\mu^2}{1-(p-1)\mu}.
 \label{eq:coherence-lower}$$ For block width $r$ and depth $k$, the same statement applies with at most $p=kr$ block Krylov columns.

Gershgorin gives $\lambda_{\min}(G)\ge1-(p-1)\mu$, while $\left\lVert c\right\rVert^2\le p\mu^2$. Insert both estimates into [\[eq:spectral-lower\]](#eq:spectral-lower){reference-type="eqref" reference="eq:spectral-lower"}. A block Krylov matrix has at most $kr$ columns.

The spectral form [\[eq:spectral-lower\]](#eq:spectral-lower){reference-type="eqref" reference="eq:spectral-lower"} is sharper in computation. The coherence form is useful analytically because exponential-sum estimates can bound $\mu$ without diagonalizing a Gram matrix. It is a standard frame stability mechanism [@Christensen2016].

# Phase-family audit {#sec:audit}

The audit fixes $q=0.995$. Since the metric is scalar, all normalized projection errors depend only on phases. Exact rings use $L=d/2$.

::: {#tab:rings}
    $d$   $L$   depth $L$ error   required depth   metric cond.
  ----- ----- ----------------- ---------------- --------------
     16     8          1.000000                9              1
     32    16          1.000000               17              1
     64    32          1.000000               33              1
    128    64          1.000000               65              1

  : Exact Fourier-ring depth scaling.
:::

For $d=64$, $L=32$, perturb the $j$th phase by $$\frac{2\pi\delta}{64}\sin(14\pi j/64),$$ where $\delta$ is measured in phase cells. At depth $32$, errors for $\delta=0,0.05,0.2,0.5$ are respectively $1$, $0.999852$, $0.997636$, and $0.985125$. The spectral lower bounds are $1$, $0.999848$, $0.997309$, and $0.978484$. Thus the obstruction is robust to moderate deterministic perturbation.

![Left: exact required depth grows as $L+1$. Middle: perturbed phase rings retain nearly unit projection error. Right: compressing phases to a short arc sharply reduces the effective depth.](<../../../../../zeta_mvp0/papers/RH-68-phase-coherence-block-depth-barrier/figures/phase_coherence_block_depth_barrier.pdf>){#fig:audit width="99%"}

The right panel is the positive result. At $d=64$, $L=32$, phase arc widths $$0, 0.03, 0.1, 0.3, 1, 3, 2\pi$$ require depths $$1, 2, 3, 7, 16, 28, 33$$ for normalized error at most $0.1$. A narrow phase support has low numerical Krylov rank even when the ambient dimension is large.

A 256-bit Arb/Acb audit certifies the eight-point ring at $L=k=4$: all DFT off-diagonal inner products and all target correlations contain zero, the diagonal norm contains one, and the canonical metric scalar is positive. This is a finite exact witness, not a production phase calculation.

# Route consequence {#sec:route}

The result rules out one tempting theorem target: $$\text{stable family}+\text{well-conditioned metric}
 \not\Longrightarrow \text{uniform fixed Krylov depth}.$$ It does not rule out the active route. Instead, RH-69 must combine three admissible mechanisms:

1.  a phase-compression certificate, for example a short angular support;

2.  weighted effective-rank decay of the physical covariance Gram;

3.  a growing block depth whose cost remains within the Stage A1 budget.

The spectral lower bound in [\[prop:spectral\]](#prop:spectral){reference-type="ref" reference="prop:spectral"} is also a practical gate: if the target correlations and minimum Krylov Gram eigenvalue imply a lower error near one, no amount of residual-weight optimization can rescue that depth. The algorithm should increase depth or change packetization before building the expensive positive envelope.

# No arithmetic or Hilbert--Polya conclusion

This paper constructs no self-adjoint operator, no $T\log T$ counting law, no prime-power trace formula, and no completed-zeta identity. It makes no Hilbert--Polya or Riemann-hypothesis claim. Stage A1 and unconditional Stage A4 remain open.

# Reproducibility

The directory contains coherence algebra, tests, phase-family pilots, the Arb/Acb audit, figures, hashes, and publication artifacts. The main commands are:

    pytest -q -p no:cacheprovider
    python experiments/run_depth_barrier_pilot.py
    python experiments/run_arb_fourier_ring_audit.py
    MPLBACKEND=Agg python experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The Fourier-ring and coherence statements are analytic. Perturbed rings and phase arcs are binary64 diagnostics. Production phase compression, effective-rank decay, an admissible growing-depth theorem, Stage A1, unconditional Stage A4, a self-adjoint Hilbert--Polya operator, an arithmetic trace formula, and a zeta-zero identity remain open.
