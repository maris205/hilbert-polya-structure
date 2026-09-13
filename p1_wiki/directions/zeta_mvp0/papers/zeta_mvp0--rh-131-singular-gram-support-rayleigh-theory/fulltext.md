---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-131-singular-gram-support-rayleigh-theory"
canonical_tex: "zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory/main.pdf"
source_sha256: "9ca3b21dec83d30b6b1983da1be0fec94991d5480b171953d843c966b8b250e0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rayleigh Transport on Singular Gram Supports Kernel Compatibility, Pseudovolume, and Outward Certification

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-130 showed that positive conditioning floors conceal a genuine semidefinite obstruction: discarded-memory tails can create rank across scales. We develop the singular-Gram theory needed to state the remaining directional argument without regularization. For $G,D\succeq0$, the global inequality $D\preceq\gamma^2G$ has a finite constant if and only if $\operatorname{Ker}G\subseteq\operatorname{Ker}D$. Under this compatibility condition its sharp constant is $$\gamma^2=\lambda_{\max}(G^{\dagger/2}DG^{\dagger/2}\big|_{\operatorname{Ran}G}).$$ If $G=A^*A$ has rank $r$ and $R^*R\preceq\gamma^2G$ with $\gamma<1$, then the product of the $r$ nonzero singular values satisfies the sharp bound $$\operatorname{vol}_r(A+R)\geq
   (1-\gamma)^r\sqrt{\operatorname{pdet}G}.$$ We also derive an outward support formula: a compressed numerical quotient $q$ with Gram and tail radii $r_G,r_D$ becomes $q+(r_D+qr_G)/(\widehat g-r_G)$, where $\widehat g$ is the compressed Gram gap.

  A 4,096-instance compatible audit verifies the pseudoinverse formula, its sharp volume example, and all outward bounds; 1,024 injected kernel-leakage examples are all rejected. Applied to RH-130, the theorem finds 54 zero-tail states and 66 full-tail states. The 24 transitions that create tail rank coincide exactly with the 24 infinite multiplicative factors. Singular support is therefore controllable, but only after the full-space kernel gate and the additive birth term are kept explicit.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Rayleigh Transport on Singular Gram Supports\
  Kernel Compatibility, Pseudovolume, and Outward Certification
```

## Markdown 正文

# The distinction between a support theorem and a full theorem

Let $H$ be finite dimensional and let $G,D\succeq0$. The generalized Rayleigh quotient $$\mathcal R_{D,G}(x)=\frac{\langle Dx,x\rangle}{\langle Gx,x\rangle}$$ is defined whenever the denominator is positive. If $G\succ0$, its supremum is the largest eigenvalue of $G^{-1/2}DG^{-1/2}$. If $G$ is singular, two statements that are often conflated must be separated.

First, on $E=\operatorname{Ran}G=(\operatorname{Ker}G)^\perp$, the compression $G_E$ is positive definite and the quotient is ordinary. Second, an operator inequality on all of $H$ additionally asks that $D$ vanish on $\operatorname{Ker}G$. No matter how small a positive mass on the kernel is, it cannot be dominated by any finite multiple of $G$. Thus support restriction is stable under a spectral gap, while full-space compatibility is a discontinuous yes/no condition. This is the same rank boundary exposed numerically in RH-130.

Write $P$ for the orthogonal projector onto $E$ and $Q=I-P$. The Moore--Penrose inverse $G^\dagger$ acts as $G_E^{-1}$ on $E$ and as zero on $\operatorname{Ker}G$.

# Sharp singular Rayleigh theorem

[\[thm:kernel\]]{#thm:kernel label="thm:kernel"} For positive semidefinite $G,D$ the following are equivalent:

1.  there is a finite $c$ such that $D\preceq cG$ on $H$;

2.  $\operatorname{Ker}G\subseteq\operatorname{Ker}D$;

3.  $D=PDP$ and $\operatorname{Ran}D\subseteq\operatorname{Ran}G$.

When they hold, the least constant is $$c_* = \lambda_{\max}
 \bigl(G^{\dagger/2}DG^{\dagger/2}\vert_E\bigr).$$ Without compatibility, the sharp full-space constant is $+\infty$, although the compressed constant on $E$ remains finite.

If $D\preceq cG$ and $x\in\operatorname{Ker}G$, positivity gives $0\leq\langle Dx,x\rangle\leq0$, hence $D^{1/2}x=0$ and $Dx=0$. This proves the kernel inclusion. For self-adjoint operators the inclusion is equivalent to $\operatorname{Ran}D\subseteq\operatorname{Ran}G$ and to $D=PDP$. On $E$, conjugate $D_E\preceq cG_E$ by $G_E^{-1/2}$. The least $c$ is the largest eigenvalue of the resulting positive matrix. Extending by zero on $\operatorname{Ker}G$ proves the full inequality. If compatibility fails, a kernel vector with positive $D$-energy makes every finite comparison impossible.

Theorem [\[thm:kernel\]](#thm:kernel){reference-type="ref" reference="thm:kernel"} is also an immediate finite-dimensional instance of Douglas range factorization [@Douglas1966]. It supplies an exact meaning for a "relative tail constant" even when the recent action loses rank; no positive floor is required.

[\[cor:leakage\]]{#cor:leakage label="cor:leakage"} For every $\varepsilon>0$ there are $G,D\succeq0$ with $\|D Q\|=\varepsilon$ such that the support quotient is bounded but the full-space quotient is infinite.

Take $G=\operatorname{diag}(1,0)$ and $D=\operatorname{diag}(c,\varepsilon)$. The support constant is $c$, while the second coordinate violates every finite full-space inequality.

This sharp negative statement prevents an outward numerical radius from being silently interpreted as a full-space theorem. One must either prove exact kernel compatibility from the construction or state a theorem only on a certified support.

# Pseudovolume under a relative tail

Suppose $A,R:H\to K$ and $G=A^*A$ has rank $r$. Define $$\operatorname{vol}_r(A)=\prod_{j=1}^r s_j(A)
 =\sqrt{\operatorname{pdet}(A^*A)},$$ where only nonzero singular values enter. This is the natural exterior volume on the effective support.

[\[thm:volume\]]{#thm:volume label="thm:volume"} If $$R^*R\preceq\gamma^2A^*A,
 \qquad 0\leq\gamma<1,$$ then $\operatorname{Ker}A\subseteq\operatorname{Ker}R$, $A+R$ has rank $r$, and $$\operatorname{vol}_r(A+R)
 \geq(1-\gamma)^r\operatorname{vol}_r(A)
 =(1-\gamma)^r\sqrt{\operatorname{pdet}G}.$$ The constant is sharp in every rank.

Theorem [\[thm:kernel\]](#thm:kernel){reference-type="ref" reference="thm:kernel"} first gives $\operatorname{Ker}A\subseteq\operatorname{Ker}R$. Douglas factorization then gives $R=TA$ on the closure of $\operatorname{Ran}A$, with $\|T\|\leq\gamma$. For $y\in\operatorname{Ran}A$, $\|(I+T)y\|\geq(1-\gamma)\|y\|$. The min--max principle therefore lowers each of the $r$ nonzero singular values by at most the factor $1-\gamma$; multiplication gives the result. Taking $R=-\gamma A$ gives equality.

For $r=4$ this recovers the determinant factor used upstream. For $r<4$ it does not manufacture a four-volume: it gives the correct $r$-dimensional exterior statement. In particular, a future varying-rank packet may carry a rigorous pseudovolume while still failing the four-directional Stage A target. Keeping the exterior order visible prevents that logical jump.

# Outward support certification

Let $U$ be an orthonormal basis for a proposed $r$-dimensional support and suppose $$\|G-\widehat G\|\leq r_G,\qquad
 \|D-\widehat D\|\leq r_D.$$ Assume the smallest eigenvalue of $\widehat G_U=U^*\widehat G U$ is $\widehat g>r_G$, and let $q$ be the largest generalized eigenvalue of $(U^*\widehat D U,\widehat G_U)$.

[\[prop:outward\]]{#prop:outward label="prop:outward"} On $U\mathbb C^r$ one has $$U^*DU\preceq q_{\rm out}\,U^*GU,
 \qquad
 q_{\rm out}=q+\frac{r_D+qr_G}{\widehat g-r_G}.$$

The numerical comparison gives $U^*\widehat DU\preceq qU^*\widehat GU$. Hence $$U^*DU\preceq qU^*GU+(r_D+qr_G)I.$$ Weyl's bound gives $U^*GU\succeq(\widehat g-r_G)I$, so the identity term is at most $U^*GU/(\widehat g-r_G)$. Substitution yields the formula.

The correction is additive in the squared Rayleigh constant and becomes large exactly when the support gap approaches the Gram radius. This is the singular-support analogue of the RH-127 congruence guard. It certifies the compressed theorem only; a separate exact or structural argument is still needed for kernel compatibility.

# Audit and application to the floor-free packet

We generate 4,096 random positive semidefinite Gramians of ambient dimension seven and ranks one through four. Compatible tails are constructed from a random relative spectrum with prescribed maximum $\gamma^2<1$. Every pseudoinverse quotient recovers the prescribed $\gamma$ to numerical error, the extremal choice $R=-\gamma A$ attains the volume bound, and all 4,096 independently perturbed outward estimates dominate the hidden exact quotient. A second set of 1,024 examples injects kernel mass between $10^{-8}$ and $10^{-3}$; every example retains a finite compressed quotient and is correctly rejected as an infinite full-space quotient.

![RH-130 tail ranks, outward support reserves, and the discontinuous kernel-leakage obstruction.](<../../../../../zeta_mvp0/papers/RH-131-singular-gram-support-rayleigh-theory/figures/singular_gram_support_rayleigh.pdf>){#fig:audit width="\\textwidth"}

The RH-130 archive provides a non-synthetic application. Its 120 states split into 54 states with zero normalized-tail rank and 66 with rank four; no intermediate ranks occur in this frozen packet. At $\sigma=0.16$ all 24 tails are zero. Nonzero tails enter at later scales and phases. Across the 96 phase-matched adjacent pairs, exactly 24 transitions increase tail rank from zero to four. This count equals the 24 infinite exact-Gram multiplicative factors, case by case. Thus the extended-real minimax result of RH-130 and the kernel-support theorem here diagnose the same structural event from two directions.

The data also clarify what remains viable. The recent-action Gramians in RH-130 are rank four, so their local four-volume does not need a singular replacement. Singularity enters through the tail pencil and through future validated support choices. The next cross-scale construction must transport the old supported tail by a partial isometry and place newly born tail range into an additive forcing block. A post hoc full-rank gauge cannot do this without hiding the rank event.

We have proved the exact singular Rayleigh formula, a sharp pseudovolume theorem, the impossibility of a small-leakage full-space relaxation, and an outward compressed bound. We have not proved a natural all-level support projector, a dynamical partial-isometry gauge, uniform affine coefficients, a normalized-base liminf, uniform Stage A, a Hilbert--Polya operator, zeta-zero identification, or the Riemann Hypothesis.
