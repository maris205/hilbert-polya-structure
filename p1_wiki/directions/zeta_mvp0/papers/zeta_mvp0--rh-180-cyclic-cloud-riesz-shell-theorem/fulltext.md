---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-180-cyclic-cloud-riesz-shell-theorem"
canonical_tex: "zeta_mvp0/papers/RH-180-cyclic-cloud-riesz-shell-theorem/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-180-cyclic-cloud-riesz-shell-theorem/main.pdf"
source_sha256: "75e403757af226a19054cf6e678e3ee504de25247f2b782659a3dffe300716b4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Cyclic-Cloud Riesz-Shell Theorem Explicit Root Geometry, Directed Schur Budgets, and Rank-Two Persistence

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-180-cyclic-cloud-riesz-shell-theorem>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-180-cyclic-cloud-riesz-shell-theorem/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-180-cyclic-cloud-riesz-shell-theorem/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-180-cyclic-cloud-riesz-shell-theorem/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-180-cyclic-cloud-riesz-shell-theorem/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The double-cycle model gives an exact finite cloud determinant, but a physical application requires its roots to persist as Riesz shells of a generally nonnormal transfer operator. We specialize the RH-162--166 packet-to-Riesz architecture to the normal cyclic seed and obtain completely explicit contour geometry.

  Let $L\ge3$, let $\rho>0$, and let $K_L$ be the doubled reduced cycle with roots $\zeta_k=\rho e^{2\pi ik/L}$, $1\le k<L$, each of multiplicity two. The half-spacing is $$s_L=\rho\sin(\pi/L).$$ Embed $K_L$ isometrically into a Hilbert space and write a candidate physical operator in packet/complement blocks $$A=\begin{pmatrix}K_L+E&B\\C&D\end{pmatrix}.$$ Choose circles $\Gamma_k=\partial D(\zeta_k,\delta)$ with $\delta<s_L$. If $\left\lVert E\right\rVert=\varepsilon<\delta$, the complement disks contain no spectrum, their contour resolvent is bounded by $d$, and $$\frac{d\left\lVert B\right\rVert\left\lVert C\right\rVert}{\delta-\varepsilon}<1,$$ then every $\Gamma_k$ remains in the resolvent of $A$ and encloses a Riesz projection of rank exactly two. The proof uses an explicit packet resolvent bound $(\delta-\varepsilon)^{-1}$ and a coupling homotopy controlled by the directed Schur product.

  A 192-matrix complex audit covers 1,248 root contours for $L=4,5,6,8,10,12$. Every admissible contour encloses rank two, with zero certificate or rank failures. The theorem is conditional: no physical embedding, perturbation ball, complement resolvent, or all-level uniform margin is supplied. It converts a future physical cycle fit into explicit Riesz obligations but does not close interface R or Gate A.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Cyclic-Cloud Riesz-Shell Theorem\
  Explicit Root Geometry, Directed Schur Budgets, and Rank-Two Persistence
```

## Markdown 正文

# Why the cyclic model helps the Riesz problem

The general physical interface R of RH-171 requires an ambient realization, validated block data, uniform Schur margins, and shellwise transport [@WangRH171]. For an arbitrary packet block, even choosing contours is difficult because a nonnormal spectral gap does not control the resolvent.

The cyclic seed removes that ambiguity. It is finite and normal, its roots are explicit, and the nearest-neighbor separation is known exactly. A physical theorem would still need to show that some transfer-space block is close to the seed, but once such closeness is available the packet resolvent budget is closed form.

# The doubled reduced cycle

Fix $L\ge3$ and $\rho>0$. Let $$\label{eq:roots}
 \zeta_k=\rho e^{2\pi ik/L},
 \qquad 1\le k\le L-1.$$ Let $K_L$ be the normal diagonalizable operator whose eigenvalue multiset contains two copies of every $\zeta_k$. Equivalently, $K_L$ is the direct sum of two reduced length-$L$ cycles scaled by $\rho$.

The chord distance between adjacent roots is $$|\zeta_{k+1}-\zeta_k|=2\rho\sin(\pi/L).$$ Define the half-spacing $$\label{eq:spacing}
 s_L=\rho\sin(\pi/L).$$ For every $0<\delta<s_L$, the closed disks $\overline D(\zeta_k,\delta)$ are pairwise disjoint.

[\[prop:normal-resolvent\]]{#prop:normal-resolvent label="prop:normal-resolvent"} On $\Gamma_k=\partial D(\zeta_k,\delta)$, $$\label{eq:seed-resolvent}
 \left\lVert(z-K_L)^{-1}\right\rVert=\frac1\delta.$$ If $\left\lVert E\right\rVert\le\varepsilon<\delta$, then $$\label{eq:perturbed-packet-resolvent}
 \left\lVert(z-K_L-E)^{-1}\right\rVert
 \le\frac1{\delta-\varepsilon}
 =:a.$$

For a normal finite matrix the resolvent norm is the reciprocal of the distance to its spectrum. The contour has distance $\delta$ from its central root and greater distance from every other root. The perturbation estimate follows from $$z-K_L-E=(I-E(z-K_L)^{-1})(z-K_L)$$ and the Neumann series.

# Physical block form

Let $J:\mathbb C^{2(L-1)}\to\mathcal H$ be an isometry and let $P=JJ^*$, $Q=I-P$. In the corresponding orthogonal decomposition, write $$\label{eq:block}
 A=\begin{pmatrix}
 K_L+E&B\\
 C&D
 \end{pmatrix}.$$ Here $E$ is the packet-block modeling error, while $B$ and $C$ are the two directed couplings. They need not be adjoints.

Assume for every $k$ that $$\label{eq:complement-free}
 \overline D(\zeta_k,\delta)\subset\rho(D),
 \qquad
 \sup_{z\in\Gamma_k}\left\lVert(z-D)^{-1}\right\rVert\le d.$$ The disk condition ensures that the baseline complement contributes no enclosed spectral rank. A boundary inverse estimate alone would be insufficient: complement eigenvalues could lie inside the contour.

# The cyclic Riesz-shell theorem

[\[thm:riesz\]]{#thm:riesz label="thm:riesz"} Assume $$\label{eq:geometry-assumptions}
 0<\delta<s_L,
 \qquad
 \left\lVert E\right\rVert\le\varepsilon<\delta,$$ and [\[eq:complement-free\]](#eq:complement-free){reference-type="eqref" reference="eq:complement-free"}. If $$\label{eq:schur}
 \kappa:=\frac{d\left\lVert B\right\rVert\left\lVert C\right\rVert}{\delta-\varepsilon}<1,$$ then every $\Gamma_k$ lies in $\rho(A)$ and its Riesz projection $$\label{eq:riesz-projection}
 \Pi_k=\frac1{2\pi i}\int_{\Gamma_k}(z-A)^{-1}\,dz$$ has rank two.

Consider the homotopy $$A_s=\begin{pmatrix}
 K_L+sE&sB\\
 sC&D
 \end{pmatrix},
 \qquad 0\le s\le1.$$ For $z\in\Gamma_k$, Proposition [\[prop:normal-resolvent\]](#prop:normal-resolvent){reference-type="ref" reference="prop:normal-resolvent"} gives $$\left\lVert(z-K_L-sE)^{-1}\right\rVert
 \le\frac1{\delta-s\varepsilon}
 \le\frac1{\delta-\varepsilon}=a.$$ The upper-left Schur complement after eliminating $z-D$ is $$z-K_L-sE-s^2B(z-D)^{-1}C.$$ Relative to $z-K_L-sE$, the feedback norm is at most $$a\,s^2\left\lVert B\right\rVert\,d\,\left\lVert C\right\rVert\le\kappa<1.$$ Hence the Schur complement and therefore $z-A_s$ are invertible for every $s$ and every point of the contour.

Riesz projections vary continuously in operator norm along a resolvent- preserving homotopy, so their finite rank is constant [@Kato1995]. At $s=0$, the operator is $K_L\oplus D$. The disk contains exactly one doubled cycle root and, by [\[eq:complement-free\]](#eq:complement-free){reference-type="eqref" reference="eq:complement-free"}, no complement spectrum. Therefore the enclosed rank is two at $s=0$ and at $s=1$.

# Full resolvent and projector-distance budgets

The Schur argument also gives an explicit full resolvent envelope. Put $a=(\delta-\varepsilon)^{-1}$, $b=\left\lVert B\right\rVert$, and $c=\left\lVert C\right\rVert$. On a root contour, let $$\kappa=adbc<1.$$ The inverse of the upper-left Schur complement has norm at most $a/(1-\kappa)$. The standard block inverse formula therefore yields $$\begin{aligned}
 \left\lVert R_{11}(z)\right\rVert&\le\frac{a}{1-\kappa},
 \label{eq:r11}\\
 \left\lVert R_{12}(z)\right\rVert&\le\frac{abd}{1-\kappa},
 \label{eq:r12}\\
 \left\lVert R_{21}(z)\right\rVert&\le\frac{dca}{1-\kappa},
 \label{eq:r21}\\
 \left\lVert R_{22}(z)\right\rVert&\le\frac{d}{1-\kappa}.
 \label{eq:r22}\end{aligned}$$ For example, the sum $$\label{eq:full-resolvent}
 M=\frac{a+abd+dca+d}{1-\kappa}$$ is a conservative bound for the full block operator resolvent under the direct-sum one-norm.

[\[prop:projector-distance\]]{#prop:projector-distance label="prop:projector-distance"} Along the homotopy in Theorem [\[thm:riesz\]](#thm:riesz){reference-type="ref" reference="thm:riesz"}, suppose the full contour resolvent is uniformly bounded by $M$. Then $$\label{eq:projector-distance}
 \left\lVert\Pi_k(A)-\Pi_k(K_L\oplus D)\right\rVert
 \le \delta M^2(\varepsilon+b+c).$$ If the right side is less than one, the physical rank-two shell is a graph over the corresponding doubled cycle eigenspace.

Differentiate the Riesz projection along $A_s$: $$\frac{d\Pi_k(s)}{ds}
 =\frac1{2\pi i}\int_{\Gamma_k}
 (z-A_s)^{-1}A_s'(z-A_s)^{-1}\,dz.$$ The derivative block has norm at most $\varepsilon+b+c$. Since the contour length is $2\pi\delta$, integration over $s\in[0,1]$ gives [\[eq:projector-distance\]](#eq:projector-distance){reference-type="eqref" reference="eq:projector-distance"}. Projection distance below one gives the usual invertible graph map [@Kato1995].

These bounds turn RH-180 into a direct validation target: a physical audit can report not only rank preservation but also graph distance and directional off-diagonal resolvent blocks.

# Asymptotic scaling forced by growing cycle length

For large $L$, $$\label{eq:spacing-asymptotic}
 s_L=\rho\sin(\pi/L)\sim\frac{\pi\rho}{L}.$$ Choose a fixed fraction $\delta=\theta s_L$ and require $\varepsilon\le\gamma\delta$ with $0<\gamma<1$. Then $$a=\frac1{\delta-\varepsilon}
 \in\left[\frac1{\theta s_L},
 \frac1{(1-\gamma)\theta s_L}\right]
 \asymp L.$$ If the complement resolvent bound $d$ remains $O(1)$, the Schur condition forces $$\label{eq:coupling-scaling}
 \left\lVert B\right\rVert\left\lVert C\right\rVert=O(L^{-1}).$$ Thus bounded nonvanishing two-way coupling cannot support individually resolved shells of unbounded cycle length. At least one of the following is needed: improving packet approximation, decaying directed feedback, complement resolvent improvement, or grouping several nearby roots into a coarser shell.

This scaling law is a genuine constraint on any all-level cyclic route. The finite RH-180 audit uses fixed small lengths and therefore tests the theorem, not the required $L\to\infty$ decay.

The criterion uses $a\,d\,\left\lVert B\right\rVert\,\left\lVert C\right\rVert<1$. A large coupling in one direction may be harmless if the return coupling is small. Replacing the product by a symmetric requirement on $\left\lVert B\right\rVert+\left\lVert C\right\rVert$ discards this nonnormal structure, as emphasized in RH-163 [@WangRH163].

# Consequences for the cloud determinant

The Riesz projections $\Pi_k$ are pairwise annihilating because their contours are disjoint. Their sum $$\Pi_{\rm cyc}=\sum_{k=1}^{L-1}\Pi_k$$ has rank $2(L-1)$. On its invariant range, the physical finite cloud factor is $$\label{eq:physical-factor}
 C_A(w)=\det_{\operatorname{Ran}\Pi_{\rm cyc}}
 (I-wA|_{\operatorname{Ran}\Pi_{\rm cyc}}).$$ The theorem guarantees its degree and shell multiplicities. It does not make $C_A$ exactly equal to the geometric polynomial when $E,B,C$ are nonzero. That stronger identification requires root-location or coefficient bounds.

If $E=B=C=0$, then $\Pi_{\rm cyc}=P$ and $$C_A(w)=\Pi_{L-1}(\rho w)^2.$$ For small nonzero data satisfying Theorem [\[thm:riesz\]](#thm:riesz){reference-type="ref" reference="thm:riesz"}, the divisor splits into the same $L-1$ rank-two shells but may move within the contours.

This distinction separates physical interface R (existence and rank of Riesz shells) from physical interface Q (identification of their determinant coefficients).

# Omission mechanisms

Each hypothesis has a distinct role.

Root spacing.

:   If $\delta\ge s_L$, adjacent doubled roots can share a contour, so individual rank-two shells are not defined.

Packet perturbation.

:   If $\varepsilon\ge\delta$, a packet eigenvalue can cross its contour even with zero complement coupling.

Complement exclusion.

:   A bounded contour inverse does not rule out complement eigenvalues inside the disk; rank two can fail at the baseline.

Directed Schur margin.

:   In scalar blocks the contour determinant can vanish exactly when the feedback product reaches one.

Ambient isometry.

:   Without a target-independent $J$, the decomposition [\[eq:block\]](#eq:block){reference-type="eqref" reference="eq:block"} is not a physical statement and can be fitted after seeing the desired spectrum.

Thus the theorem is explicit but not self-instantiating.

# Finite matrix audit

The audit uses $$L=4,5,6,8,10,12,
 \qquad \rho=\lambda^{-1},
 \qquad \delta=0.35s_L,
 \qquad \varepsilon=0.15\delta.$$ For each length, 32 independent complex perturbations and directed couplings are generated. The complement has three normal eigenvalues on radius $2.5\rho$, and the coupling norms are chosen so that the certified Schur product equals $0.20$.

This gives 192 full matrices and 1,248 individual root contours. Every budget is admissible, every contour encloses exactly two numerical eigenvalues, and the audit records zero rank failures and zero certificate failures. These tests validate the formula and counting implementation; they are not samples of the physical transfer operator.

# Physical obligations and next frontier

Theorem [\[thm:riesz\]](#thm:riesz){reference-type="ref" reference="thm:riesz"} provides a finite conditional route from a cyclic model to Riesz shells. To apply it physically one must still:

1.  construct an isometry $J$ from a data-derived cycle into the noisy transfer/determinant space;

2.  validate $\left\lVert E\right\rVert$, both coupling norms, and complement resolvents with outward bounds;

3.  prove an eventual uniform margin as $L$ grows and root spacing shrinks like $\pi\rho/L$;

4.  transport every fixed shell in common coordinates across scales;

5.  separately identify the resulting cloud factor and directed marks.

The shrinking spacing is important: a fixed absolute modeling error cannot support arbitrarily long cycles. The physical approximation must improve at least on the $L^{-1}$ contour scale.

No physical input above is proved here. Interface R, the cloud ledger Q, the Schatten complement U, normalization Z, directed limit T, macro Gate A, and all Hilbert--Polya or Riemann-hypothesis conclusions remain open.
