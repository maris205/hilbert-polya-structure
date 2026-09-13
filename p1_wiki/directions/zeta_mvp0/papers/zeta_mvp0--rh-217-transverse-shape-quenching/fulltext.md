---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-217-transverse-shape-quenching"
canonical_tex: "zeta_mvp0/papers/RH-217-transverse-shape-quenching/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-217-transverse-shape-quenching/main.pdf"
source_sha256: "3da611219080bac8472fdc8f5eeb779750d6d8006a07537f75c2394f6445b375"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Transverse Quenching in Quartet Coefficient Space Exact Anisotropy Near the Degenerate Axial Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-217-transverse-shape-quenching>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-217-transverse-shape-quenching/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-217-transverse-shape-quenching/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-217-transverse-shape-quenching/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-217-transverse-shape-quenching/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The centered conjugate-quartet manifold has axial coordinate $u$ and asymmetry coordinate $\eta$. RH-216 proves that $u\to1$ forces the polynomial toward $(z^2-1)^2$ uniformly in $\eta$. We sharpen that statement by computing the full coefficient Jacobian and proving an exact transverse Lipschitz bound.

  For $$\Phi(u,\eta)=(2-4u,\ 4\sqrt u(1-u)\eta,\
                   1-\eta^2(1-u)^2),$$ the $\eta$ derivative satisfies $$\sup_{|\eta|\le1}\left\lVert\partial_\eta\Phi(u,\eta)\right\rVert_2
   \le 2(1-u)\sqrt{4u+(1-u)^2}.$$ The same constant controls every finite transverse chord. It vanishes linearly as $u\to1$. In contrast, $\left\lVert\partial_u\Phi\right\rVert\ge4$ because the first component is always $-4$. Thus coefficient space becomes intrinsically anisotropic: axial motion remains visible while transverse motion is quenched.

  On the sixteen-level physical atlas, the maximum channelwise transverse-to-axial Jacobian ratio decreases from $0.3752$ at $\sigma=0.02$ to $0.2389$ at $\sigma=0.00125$. The finest left/right transverse coefficient leg is only $0.00136$. These finite values support the geometric mechanism but do not prove $u\to1$, convergence of $\eta$, or a one-dimensional physical flow.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Transverse Quenching in Quartet Coefficient Space\
  Exact Anisotropy Near the Degenerate Axial Boundary
```

## Markdown 正文

# Why a narrow corridor may become coefficientwise invisible

RH-214 observes that $\eta$ fluctuates in a mature interval of width below $0.038$, while $u$ increases across every sampled transition [@WangRH214]. RH-216 shows that the entire $u=1$ edge of the shape rectangle maps to one polynomial [@WangRH216]. These facts suggest a specific mechanism: the coefficient map may contract transverse differences as the axial coordinate grows.

This paper proves that mechanism directly. It is a statement about the exact quotient geometry of RH-213, independent of any statistical fit or physical limit [@WangRH213].

# Coefficient map

Discarding the fixed leading and cubic coefficients, define $$\label{eq:phi}
 \Phi(u,\eta)=
 \begin{pmatrix}
 c_2\\c_3\\c_4
 \end{pmatrix}
 =\begin{pmatrix}
 2-4u\\
 4\sqrt u(1-u)\eta\\
 1-\eta^2(1-u)^2
 \end{pmatrix},$$ for $0<u\le1$ and $|\eta|\le1$.

[\[prop:jacobian\]]{#prop:jacobian label="prop:jacobian"} For $u>0$, $$\label{eq:jacobian}
 D\Phi(u,\eta)=
 \begin{pmatrix}
 -4 & 0\\[2mm]
 \displaystyle\frac{2\eta(1-3u)}{\sqrt u}
     &4\sqrt u(1-u)\\[3mm]
 2\eta^2(1-u)&-2\eta(1-u)^2
 \end{pmatrix}.$$

Differentiate the three components of [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"}. In particular, $$\frac{d}{du}\bigl[\sqrt u(1-u)\bigr]
 =\frac{1-3u}{2\sqrt u}.$$

The singularity in the displayed $u$ derivative at $u=0$ reflects loss of the positive/negative real branch label there. The physical mature region stays away from that boundary.

# Uniform transverse bound

[\[thm:quench\]]{#thm:quench label="thm:quench"} For fixed $u\in[0,1]$ and any $\eta_1,\eta_2\in[-1,1]$, $$\label{eq:lipschitz}
 \left\lVert\Phi(u,\eta_1)-\Phi(u,\eta_2)\right\rVert_2
 \le L_\eta(u)|\eta_1-\eta_2|,$$ where $$\label{eq:L}
 \boxed{L_\eta(u)=2(1-u)\sqrt{4u+(1-u)^2}.}$$ Consequently $L_\eta(u)=O(1-u)$ as $u\to1$.

At fixed $u$, the coefficient difference is $$\begin{pmatrix}
 0\\
 4\sqrt u(1-u)(\eta_1-\eta_2)\\
 -(1-u)^2(\eta_1+\eta_2)(\eta_1-\eta_2)
 \end{pmatrix}.$$ Since $|\eta_1+\eta_2|\le2$, its squared norm is at most $$4(1-u)^2\bigl[4u+(1-u)^2\bigr]|\eta_1-\eta_2|^2.$$ Taking square roots proves the estimate. The asymptotic order follows because the square-root factor tends to two.

This is a global chord estimate, not merely a local derivative statement. It remains valid at $u=0$ and on the $\eta$ edges.

# Axial sensitivity does not vanish

[\[prop:axial\]]{#prop:axial label="prop:axial"} For every $u>0$ and $|\eta|\le1$, $$\label{eq:axiallower}
 \left\lVert\partial_u\Phi(u,\eta)\right\rVert_2\ge4.$$

The first component of $\partial_u\Phi$ is $-4$.

Combining Theorem [\[thm:quench\]](#thm:quench){reference-type="ref" reference="thm:quench"} and Proposition [\[prop:axial\]](#prop:axial){reference-type="ref" reference="prop:axial"} gives the uniform anisotropy ratio $$\label{eq:ratio}
 \frac{\sup_{\eta}\left\lVert\partial_\eta\Phi(u,\eta)\right\rVert_2}
      {\inf_{\eta}\left\lVert\partial_u\Phi(u,\eta)\right\rVert_2}
 \le \frac{1-u}{2}\sqrt{4u+(1-u)^2}\longrightarrow0.$$

Thus the map itself, not a fitted trajectory, singles out the axial direction near $u=1$.

# Coefficient quenching versus root quenching

The imaginary root heights are $$b=\sqrt{(1-u)(1+\eta)},\qquad
 d=\sqrt{(1-u)(1-\eta)}.$$ Their $\eta$ derivatives can become large near $|\eta|=1$ because of the square root. Therefore Theorem [\[thm:quench\]](#thm:quench){reference-type="ref" reference="thm:quench"} is specifically a coefficient-space theorem. Symmetric polynomials cancel and square the transverse root motion, producing the stronger $O(1-u)$ coefficient scale.

This distinction matters for the divisor-first route. A scalar determinant can stabilize even when individual branch coordinates are less regular, just as RH-210 showed that divisor stability need not imply projector stability [@WangRH210].

# Exact path decomposition between channels

At one scale let the left and right shapes be $(u_L,\eta_L)$ and $(u_R,\eta_R)$. Insert the corner $(u_R,\eta_L)$: $$\label{eq:path}
 \Phi(u_R,\eta_R)-\Phi(u_L,\eta_L)
 =\underbrace{\Phi(u_R,\eta_L)-\Phi(u_L,\eta_L)}_{\text{axial leg}}
 +\underbrace{\Phi(u_R,\eta_R)-\Phi(u_R,\eta_L)}_{\text{transverse leg}}.$$ This is an exact telescoping identity. The transverse leg obeys $$\left\lVert\text{transverse leg}\right\rVert_2
 \le L_\eta(u_R)|\eta_R-\eta_L|.$$

The frozen audit evaluates both legs at all sixteen scales. Eight hundred random chord tests have no positive bound violation, and all path residuals are machine zero.

# Finite physical anisotropy

The exact Jacobian is evaluated at each of the 32 physical shape points. Representative mature values are summarized by

  diagnostic                                  $\sigma=0.02$   $\sigma=0.00125$
  ----------------------------------------- --------------- ------------------
  maximum transverse/axial Jacobian ratio         $0.37516$          $0.23883$
  maximum channel $|\Delta\eta|$                  $0.00145$          $0.00141$
  maximum transverse channel-leg norm                 small         $0.001354$

The ratio decreases as the observed axial clock advances, in agreement with [\[eq:ratio\]](#eq:ratio){reference-type="eqref" reference="eq:ratio"}. It is not yet extremely small: $u\approx0.718$ remains far from the degenerate edge. The numbers therefore support the mechanism without demonstrating an asymptotic regime.

# Implications and limitations

If a future theorem proves $u_\sigma\to1$, then any bounded $\eta_\sigma$ sequence---convergent or not---has vanishing transverse coefficient effect. The coefficient path could become asymptotically one-dimensional even while the transverse coordinate continues to oscillate.

The converse is not supplied here. Finite decline of the sensitivity ratio does not prove $u\to1$, and coefficient anisotropy does not identify a scale-independent map advancing $u$. RH-218 tests that stronger recurrence claim separately.

No growing root cloud, locally uniform determinant, Gate-A closure, Hilbert--Pólya operator, arithmetic trace formula, or zeta identification is obtained.
