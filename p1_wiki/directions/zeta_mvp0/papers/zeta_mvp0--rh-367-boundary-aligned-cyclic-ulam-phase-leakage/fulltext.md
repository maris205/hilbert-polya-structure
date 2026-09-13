---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-367-boundary-aligned-cyclic-ulam-phase-leakage"
canonical_tex: "zeta_mvp0/papers/RH-367-boundary-aligned-cyclic-ulam-phase-leakage/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-367-boundary-aligned-cyclic-ulam-phase-leakage/main.pdf"
source_sha256: "b6d59b16169a73b386db927618e3be198c2a369e13c907fd837d3057f8369ecb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Boundary-Aligned Cyclic-Ulam Structure and Phase-Local Leakage An exact finite-dimensional edge at a postcritically finite quadratic map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-367-boundary-aligned-cyclic-ulam-phase-leakage>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-367-boundary-aligned-cyclic-ulam-phase-leakage/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-367-boundary-aligned-cyclic-ulam-phase-leakage/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-367-boundary-aligned-cyclic-ulam-phase-leakage/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-367-boundary-aligned-cyclic-ulam-phase-leakage/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We isolate an exact finite-dimensional mechanism in a postcritically finite quadratic map. At the algebraic parameter $u_c$ satisfying $u_c^3-2u_c^2+2u_c-2=0$, the invariant interval splits into two bands that are exchanged by one iterate. For every finite exact cell-overlap Ulam partition whose boundary contains the band endpoint $r=u_c-1$, the matrix is anti-diagonal in band coordinates and inherits a sign vector with eigenvalue $-1$. If one cell crosses the endpoint, the projected sign has the exact local defect $4\theta(1-\theta)$, or $4h\theta(1-\theta)$ after weighting by the cell width. A frozen 33-phase scan at four resolutions reproduces the predicted aligned/crossing dichotomy and records the finite near-$-1$ drift. The scan is a diagnostic: no universal power law, continuum isolated-spectrum theorem, canonical arithmetic operator, or Riemann-Hypothesis implication is claimed. An explicit overlap ledger separates this edge from RH-3, RH-10, and RH-55.
author:
- RH research program
date: August 2026
title: |
  Boundary-Aligned Cyclic-Ulam Structure and Phase-Local Leakage\
  An exact finite-dimensional edge at a postcritically finite quadratic map
```

## Markdown 正文

# Scope and claim boundary

The object of this paper is a finite exact Ulam matrix, not an unnamed continuum transfer operator. We use the phrase "cyclic mode" for the two-band exchange and "leakage" for a projected finite-cell diagnostic. The following statements are outside the paper's claim ceiling: a strong-Banach-space isolated eigenvalue or a common resolvent contour as the mesh is refined; a universal $\sqrt{\sigma}$ law (or any exponent inferred from a finite log--log fit); and a canonical global Hénon operator, zeta factor, von Mangoldt trace, Hilbert--Polya construction, Riemann-zero identification, or proof of RH. All numerical rows are frozen source diagnostics and are not asymptotic evidence. The exact route verdict is Route A $=\texttt{GO}$ and Route B $=\texttt{STOP\_SCOPED}$.

# The postcritically finite two-band map

Let $$p(u)=u^3-2u^2+2u-2,
 \qquad u_c=1.5436890126920764\ldots,
 \qquad r=u_c-1.$$ The map and its invariant interval are $$f(x)=1-u_cx^2,
 \qquad J=[-r,1].$$ The symbolic source certificate records $$f(0)=1,\qquad f(1)=-r,\qquad f(-r)=r,\qquad f(r)=r.
 \label{eq:critical}$$ Define the two closed bands (with their common endpoint understood in the usual measure-zero convention) $$B_0=[-r,r],\qquad B_1=[r,1].$$ Monotonicity on either side of zero and [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} give $$f(B_0)=B_1,\qquad f(B_1)=B_0.
 \label{eq:exchange}$$

The source paper also records the normalized invariant density $h$ and the $L^1$ sign mode $$g=h(\mathbf 1_{B_0}-\mathbf 1_{B_1}),
 \qquad \mathcal P g=-g,
 \label{eq:l1mode}$$ in the invariant-density normalization. Equation [\[eq:l1mode\]](#eq:l1mode){reference-type="eqref" reference="eq:l1mode"} is an $L^1$ statement. It does not assert that $-1$ is isolated on a selected strong space.

# Exact aligned Ulam inheritance

Let $\mathcal D_h=\{D_i\}_{i=1}^N$ be a finite interval partition of $J$. The row-stochastic exact cell-overlap matrix is $$(P_h)_{ij}=\frac{\operatorname{Leb}(D_i\cap f^{-1}(D_j))}{\operatorname{Leb}(D_i)}.
 \label{eq:ulam}$$ We call the partition aligned when $r$ is a cell boundary. Source cells are split at the turning point and inverse-branch breakpoints before the overlap integrals are evaluated.

[\[thm:block\]]{#thm:block label="thm:block"} For every aligned finite partition, after ordering cells by band, $$P_h=\begin{pmatrix}0&A\\B&0\end{pmatrix}.
 \label{eq:block}$$ If $s_i=+1$ on $B_0$ cells and $s_i=-1$ on $B_1$ cells, then $$P_hs=-s.
 \label{eq:sign}$$ In particular, $-1\in\operatorname{spec}(P_h)$ in exact arithmetic.

Every source cell belongs to one band. By [\[eq:exchange\]](#eq:exchange){reference-type="eqref" reference="eq:exchange"}, its image belongs to the opposite band, so an overlap between cells in the same band is zero. This is exactly the anti-diagonal form [\[eq:block\]](#eq:block){reference-type="eqref" reference="eq:block"}. Every nonzero row therefore sends its mass to cells carrying the opposite sign; multiplication by $P_h$ changes $s$ to $-s$, which proves [\[eq:sign\]](#eq:sign){reference-type="eqref" reference="eq:sign"}. No uniform mesh assumption is used.

The theorem is finite-dimensional and normalization-specific. It does not identify the vector $s$ with a right eigenfunction of an arbitrary Lebesgue reference Perron--Frobenius operator, and it does not control the rest of the finite spectrum or its limit as $h\to0$.

# Crossing-cell projection defect

Suppose a single cell $D_*$ crosses $r$. Define the band fraction and the projected sign by $$q_i=\frac{\operatorname{Leb}(D_i\cap B_0)}{\operatorname{Leb}(D_i)},
 \qquad s_i^{(h)}=2q_i-1.
 \label{eq:q}$$ For an aligned cell, $q_i\in\{0,1\}$. For the crossing cell, $q_* =\theta\in(0,1)$. The elementary identity below is the exact local phase law.

[\[prop:defect\]]{#prop:defect label="prop:defect"} For $\theta\in[0,1]$, $$1-(2\theta-1)^2=4\theta(1-\theta).
 \label{eq:identity}$$ If the crossing cell has width $h$, its width-weighted defect is $4h\theta(1-\theta)$.

Expand $(2\theta-1)^2=4\theta^2-4\theta+1$ and subtract from one. Multiplying by $h$ gives the second assertion.

The global diagnostic used by the source is the stationary same-band mass $$L_h=\sum_i\pi_iq_i\sum_j(P_h)_{ij}q_j
 +\sum_i\pi_i(1-q_i)\sum_j(P_h)_{ij}(1-q_j),
 \label{eq:global}$$ where $\pi$ is a stationary cell-mass vector. If the partition is aligned, the anti-diagonal theorem makes $L_h=0$ exactly. When a cell crosses $r$, $L_h$ depends on the stationary weights and all other cells; it is not equal to the local expression in every discretization. This distinction matters: the local identity is a theorem, while the global phase scan is an observed finite quantity.

# Frozen numerical protocol

The external source uses analytic inverse-branch overlap assembly, row normalization, stationary iteration, and a tracked eigenvalue nearest $-1$. The retained deterministic scan has four resolutions $$N\in\{256,512,1024,2048\}$$ and 33 translated phases at each resolution, together with one snapped aligned phase. Thus there are 136 rows: 4 aligned and 132 crossing. The aligned rows have zero projected same-band mass and an exact sign residual up to floating assembly error. Crossing rows have positive projected mass and a nonzero finite displacement of the tracked near-$-1$ eigenvalue.

::: {#tab:scan}
  quantity                                                                     value
  ------------------------------------- --------------------------------------------
  resolutions                                                    $256,512,1024,2048$
  phases per resolution                                                         $33$
  total rows                                                                   $136$
  aligned / crossing rows                                                    $4/132$
  crossing $L_h$ range                    $1.14\times10^{-4}$ to $7.71\times10^{-3}$
  maximum crossing distance from $-1$                            $4.91\times10^{-3}$
  maximum row-sum error                                           $6.4\times10^{-9}$
  maximum stationary $L^1$ residual                              $1.9\times10^{-13}$

  : Frozen phase-scan counts and ranges. These values are diagnostics.
:::

The source also contains direct, split, and cycle-constrained noisy matrices. Their fitted slopes over a finite range are deliberately not promoted here. The boundary convention and kernel change the finite intercepts, and no common strong-space perturbation theorem is supplied.

# Overlap audit and route decision

RH-3 uses the same band-merging map to prove a continuum parity eigenmode, periodogram limits, and conditional two-step operator decompositions. It does not contain the arbitrary aligned finite-Ulam block theorem or the crossing-cell identity. RH-10 studies exact periodic counts, exponentially close boundary cycles, noncommuting long-cycle/noise limits, and a parity-renormalized determinant; it does not state the phase-local Ulam defect. RH-55 proves midpoint--Ulam strong--weak contour transfer for a conditioned folded-Gaussian kernel; it does not prove deterministic PCF sign inheritance for arbitrary aligned partitions. The overlap is therefore structural context, not duplication.

Route A is `GO` for Theorems [\[thm:block\]](#thm:block){reference-type="ref" reference="thm:block"} and [\[prop:defect\]](#prop:defect){reference-type="ref" reference="prop:defect"}, together with the source-locked finite protocol. Route B is `STOP_SCOPED`: the first missing bridge is a common strong-space projector/resolvent theorem connecting the finite matrices to a continuum operator. In particular, no finite scan proves a universal noise exponent, an isolated continuum resonance, or any arithmetic/RH statement.

# Conclusion

The exact content of RH-367 is a reusable finite-volume fact: a genuine band-boundary alignment preserves a two-cycle sign mode in every exact cell-overlap matrix, while a crossing cell has an explicit phase defect. The global leakage and near-$-1$ displacement are useful diagnostics for choosing what must be proved next, but they are not substitutes for a strong-space limit theorem. The physical route coordinate remains `actual_same_clock_unnormalized_head_transport_open`; all five RH gates remain false/open.

9 Cyclic Ulam Map, source package and proof bundle, 2026. Frozen commit `e7d21f646498d77e1c3213d1e4f35dc8466038ff`. RH-3, *Parity-Resolved Dynamics at a Quadratic Band-Merging Parameter*, repository artifact. RH-10, *Parity-Renormalized Long-Cycle Determinants*, repository artifact. RH-55, *Strong--Weak Adaptive Cutoff Transfer for Intrinsic Riesz Factors*, repository artifact. G. Froyland, "On Ulam approximation of isolated spectrum and eigenfunctions of hyperbolic maps," *DCDS* 17 (2007), 671--689.
