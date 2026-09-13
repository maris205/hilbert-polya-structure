---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-35-exact-packet-pair-physical-count"
canonical_tex: "zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count/exact-packet-pair-physical-count.pdf"
source_sha256: "4b245ee32e7b116944030be1d3ad01077d4db8d95ac033b62377aedfa2977637"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Packet-Pair Correction and a Physical Two-Step Eigenvalue Count Rigorous Transfer from a Stored Feshbach Block to the $2048$-Dimensional Perron/Parity-Extracted Matrix

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count/exact-packet-pair-physical-count.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The preceding stored-model analysis proved that a $2048$-dimensional packet--complement Feshbach block has no interior complement pole and exactly one eigenvalue in a certified circle. It did not identify that augmented block with the Perron/parity-extracted physical two-step matrix, because the serialized binary64 packet arrays satisfy $WV\approx\mathrm I_4$ but not the exact algebraic identity $WV=\mathrm I_4$.

  This paper removes that finite-coordinate caveat. Every stored binary64 entry is interpreted as an exact dyadic rational. Exact integer arithmetic forms $$G=WV,\qquad H=G-\mathrm I_4$$ and proves $$\left\lVert H\right\rVert_F\leq 6.50085\times10^{-16}<1.$$ Hence the exact rational correction $$\widehat W=G^{-1}W$$ exists and satisfies $\widehat WV=\mathrm I_4$ identically. With $\widehat Q=\mathrm I-V\widehat W$, the corrected packet and complement are exact oblique projectors for the stored physical two-step matrix $A_{\rm phys}=U^2$.

  The correction is transferred through the complete stored factor graph. Rigorous bounds give $$\left\lVert\widehat W-W\right\rVert_2\leq9.27218\times10^{-16},\qquad
   \left\lVert\widehat Q-Q\right\rVert_2\leq1.05400\times10^{-15},$$ and $$\left\lVert\widehat B-B\right\rVert_2\leq4.70308\times10^{-15}.$$ On every one of the $949$ rational boundary leaves inherited from the certified complement atlas, the resulting complement Neumann product is below $3.76781\times10^{-9}$.

  For the Feshbach map, the complete RH-28 primal--dual remainder $\eta_\ell+M_\ell c_\ell$ is retained on each leaf. The stored Feshbach inverse is then transported to the corrected map by a second matrix Rouché homotopy. Its largest rigorous product is $$0.547184078<1.$$ Consequently the corrected complement count remains zero and the corrected Feshbach winding remains one.

  Exact coordinate algebra finally gives $$z^4\det(z\mathrm I-A_{\rm phys})
   =\det(z\mathrm I-\widehat B)\det\widehat F(z).$$ The exact stored circle excludes zero. Therefore $$\boxed{N_\Gamma(A_{\rm phys})=1}.$$ Thus the exact finite Perron/parity-extracted physical two-step matrix has exactly one eigenvalue in the certified circle, counted algebraically.

  The theorem concerns one finite matrix defined by stored binary64 factors. It does not enclose discretization error, prove a zero-noise or dimension limit, construct a self-adjoint operator, identify zeta zeros, or imply the Riemann hypothesis.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Exact Packet-Pair Correction and a\
  Physical Two-Step Eigenvalue Count**\
  Rigorous Transfer from a Stored Feshbach Block to the\
  $2048$-Dimensional Perron/Parity-Extracted Matrix
```

## Markdown 正文

**Keywords:** packet biorthogonalization; Feshbach map; physical two-step operator; matrix Rouché theorem; verified numerical linear algebra; spectral count; nonnormal matrix.

**MSC 2020:** 15A18; 47A10; 47A11; 47A55; 65F35; 65G20; 65P30.

# Introduction {#sec:introduction}

A packet--complement Feshbach reduction becomes an exact coordinate description of a physical matrix only when its synthesis and analysis pair is exactly biorthogonal. If $V\in\mathbb C^{n\times m}$ and $W\in\mathbb C^{m\times n}$ satisfy $$WV=\mathrm I_m,$$ then $P=VW$ and $Q=\mathrm I-P$ are complementary oblique projectors. The packet, forcing, observation, and complement blocks of a matrix $A$ are then exact coordinates of $A$, and the Feshbach determinant counts physical eigenvalues after the complement poles are removed [@WangPhysicalFeshbach2026; @WangContourFeshbach2026].

In floating construction, the canonical dual $W$ is obtained from a small Gram solve, so the computed product $WV$ is indistinguishable from the identity at ordinary precision. Once the arrays are serialized and every binary64 entry is regarded as an exact number, however, the matrix product is no longer exactly the identity. This distinction was deliberately preserved in the outward-rounded chain: $Q=\mathrm I-VW$ was used only as a stored linear factor, with no silent assumption that $Q^2=Q$ [@WangOutwardCode2026; @WangAtlas2026].

That caution produced an exact but intermediate theorem. RH-34 certified, for the stored block realization, $$N_\Gamma(B)=0,\qquad
 N_\Gamma(\mathcal M_{\rm st})=1,$$ and showed that the stored Feshbach determinant has one interior zero [@WangInterior2026]. Because $WV=\mathrm I_m$ was not exact, the theorem did not identify $\mathcal M_{\rm st}$ with the original Perron/parity-extracted physical two-step matrix.

The defect is only of roundoff scale, but size alone is not a proof. The complement resolvent is strongly nonnormal and reaches a rigorous upper bound of $8.01138\times10^5$ on the counting circle. A perturbation of size $10^{-15}$ may therefore be harmless, but the coordinate correction must be propagated through both the complement inverse and the Feshbach map. The latter also requires the complete primal--dual remainder, not only the directly computable correction term.

This paper makes that propagation explicit. It first corrects the dual packet exactly by $$\widehat W=(WV)^{-1}W.$$ No data are refitted and no packet range is changed. This is a finite-dimensional coordinate correction applied to the exact stored arrays. Structured norm identities then bound the changes in all four Feshbach blocks. The RH-33 complement atlas transfers the pole-free count, while the RH-28 projected inverse and complete remainder transfer the Feshbach winding. Exact coordinate algebra then converts the corrected relative count into an eigenvalue count for the physical two-step matrix.

The contributions are:

1.  an exact dyadic computation of the $4\times4$ defect $WV-\mathrm I_4$;

2.  a rigorous exact biorthogonal correction $\widehat W=(WV)^{-1}W$;

3.  structured perturbation bounds for the corrected packet, complement, forcing, observation, and direct blocks;

4.  a $949$-leaf corrected-complement homotopy using the certified RH-33 resolvent atlas;

5.  a $949$-leaf Feshbach Rouché comparison retaining the full RH-28 remainder $\eta_\ell+M_\ell c_\ell$;

6.  an exact determinant identity between the corrected block and $U^2\oplus0_4$; and

7.  the rigorous physical count $N_\Gamma(U^2)=1$.

The evidence hierarchy is again explicit.

-   The packet correction, projector identities, block factorization, determinant identity, and count deduction are exact algebra.

-   Dyadic Gram products are exact rational computations. Block norms and leafwise products are rigorous outward-rounded bounds.

-   The displayed physical eigenvalue plot is a floating diagnostic and is not used to prove the count.

# Exact stored physical matrix and packet defect {#sec:model}

## Perron/parity-extracted two-step matrix

Fix $\sigma=10^{-2}$ and $n=2048$. Let $M\in\mathbb R^{n\times n}$ be the stored sparse folded Gaussian matrix, and let $R_{\rm p},L_{\rm p}\in\mathbb R^{n\times2}$ and $\Lambda\in\mathbb R^{2\times2}$ be the stored Perron/parity factors and values. Define $$U=M-R_{\rm p}\Lambda L_{\rm p}^{\mathsf T},
 \qquad
 A_{\rm phys}=U^2.
 \label{eq:physical}$$ Every factor in [\[eq:physical\]](#eq:physical){reference-type="ref" reference="eq:physical"} is an exact stored binary64 array. The matrix $A_{\rm phys}$ is the finite Perron/parity-extracted physical two-step matrix considered by the contour construction. The adjective *physical* refers to this full $n$-dimensional finite matrix, not to a continuum limit.

Let $V\in\mathbb R^{n\times m}$, $W\in\mathbb R^{m\times n}$, $m=4$, be the stored packet synthesis and analysis arrays. Put $$G=WV,\qquad H=G-\mathrm I_m.
 \label{eq:gram-defect}$$ In exact real arithmetic the canonical construction is designed to satisfy $WV=\mathrm I_m$. The serialized arrays have a nonzero exact dyadic $H$.

## Exact dyadic Gram computation

Each binary64 number is a rational integer times a power of two. The implementation converts every component of $W$ and $V$ to that exact fraction, forms all $16$ dot products in $WV$ with integer arithmetic, and subtracts the exact identity. No floating matrix product is used in this step.

The resulting Frobenius square $$\sum_{i,j=1}^4 H_{ij}^2$$ is an exact rational number. A $256$-bit Arb square root rounded upward gives $$\left\lVert H\right\rVert_2\leq\left\lVert H\right\rVert_F
 \leq h:=6.500848174495279\times10^{-16}<1.
 \label{eq:h-bound}$$ The complete numerators and denominators of all $16$ entries are committed in the exact packet-defect ledger.

[\[lem:packet-correction\]]{#lem:packet-correction label="lem:packet-correction"} The exact matrix $G=\mathrm I_m+H$ is invertible. Define $$\widehat W=G^{-1}W,\qquad
 \widehat P=V\widehat W,\qquad
 \widehat Q=\mathrm I-\widehat P.
 \label{eq:corrected-pair}$$ Then $$\widehat WV=\mathrm I_m,\quad
 \widehat P^2=\widehat P,\quad
 \widehat Q^2=\widehat Q,\quad
 \widehat P\widehat Q=\widehat Q\widehat P=0.
 \label{eq:corrected-identities}$$ Moreover, $$\left\lVert G^{-1}\right\rVert_2\leq\frac{1}{1-h}.
 \label{eq:gram-inverse}$$

The Neumann lemma and [\[eq:h-bound\]](#eq:h-bound){reference-type="ref" reference="eq:h-bound"} prove invertibility and [\[eq:gram-inverse\]](#eq:gram-inverse){reference-type="ref" reference="eq:gram-inverse"}. Then $\widehat WV=G^{-1}WV=G^{-1}G=\mathrm I_m$. The remaining identities follow by direct multiplication.

[\[rem:not-refit\]]{#rem:not-refit label="rem:not-refit"} The synthesis range $\operatorname{ran}V$, the physical matrix $A_{\rm phys}$, and every stored input remain unchanged. The correction only replaces the rounded dual coordinates by the exact dual of the already stored packet basis. Its entries are exact rationals and need not be binary64 numbers.

# Stored and corrected Feshbach systems {#sec:feshbach-systems}

## Stored blocks

The stored external factor is $$Q=\mathrm I-VW.
 \label{eq:stored-q}$$ Without assuming $Q^2=Q$, define $$D=WA_{\rm phys}V,\quad
 C=QA_{\rm phys}V,\quad
 E=WA_{\rm phys}Q,\quad
 B=QA_{\rm phys}Q.
 \label{eq:stored-blocks}$$ For $R(z)=(z\mathrm I-B)^{-1}$, the stored Feshbach map is $$F(z)=z\mathrm I_m-D-E R(z)C.
 \label{eq:stored-f}$$ RH-34 proves on the selected circle $\Gamma$ that $$N_\Gamma(B)=0,\qquad
 \operatorname{wind}_\Gamma\det F=1.
 \label{eq:rh34-input}$$

## Corrected blocks

Using the exact pair in [\[eq:corrected-pair\]](#eq:corrected-pair){reference-type="ref" reference="eq:corrected-pair"}, define $$\widehat D=\widehat WA_{\rm phys}V,\quad
 \widehat C=\widehat QA_{\rm phys}V,\quad
 \widehat E=\widehat WA_{\rm phys}\widehat Q,\quad
 \widehat B=\widehat QA_{\rm phys}\widehat Q
 \label{eq:corrected-blocks}$$ and $$\widehat F(z)
 =z\mathrm I_m-\widehat D
 -\widehat E(z\mathrm I-\widehat B)^{-1}\widehat C.
 \label{eq:corrected-f}$$ These are now genuine packet/complement coordinates of $A_{\rm phys}$.

## Exact coordinate determinant

Set $$\widehat K=
 \begin{pmatrix}\widehat W\\ \widehat Q\end{pmatrix}
 \in\mathbb C^{(m+n)\times n},
 \qquad
 \widehat J=
 \begin{pmatrix}V&\widehat Q\end{pmatrix}
 \in\mathbb C^{n\times(m+n)}.
 \label{eq:coordinate-factors}$$ By [\[eq:corrected-identities\]](#eq:corrected-identities){reference-type="ref" reference="eq:corrected-identities"}, $$\widehat J\widehat K
 =V\widehat W+\widehat Q^2
 =\widehat P+\widehat Q
 =\mathrm I_n.
 \label{eq:left-inverse}$$ The corrected augmented block is $$\widehat{\mathcal M}
 =\widehat KA_{\rm phys}\widehat J
 =
 \begin{pmatrix}
  \widehat D&\widehat E\\
  \widehat C&\widehat B
 \end{pmatrix}.
 \label{eq:corrected-augmented}$$

[\[prop:physical-plus-zero\]]{#prop:physical-plus-zero label="prop:physical-plus-zero"} The corrected augmented block is similar to $A_{\rm phys}\oplus0_m$. Consequently $$\det(z\mathrm I_{n+m}-\widehat{\mathcal M})
 =z^m\det(z\mathrm I_n-A_{\rm phys}).
 \label{eq:physical-determinant}$$ Wherever $z\mathrm I-\widehat B$ is invertible, $$z^m\det(z\mathrm I_n-A_{\rm phys})
 =\det(z\mathrm I_n-\widehat B)\det\widehat F(z).
 \label{eq:corrected-schur-identity}$$

Equation [\[eq:left-inverse\]](#eq:left-inverse){reference-type="ref" reference="eq:left-inverse"} gives the direct sum $$\mathbb C^{m+n}=\operatorname{ran}\widehat K\oplus\ker\widehat J.$$ The corrected block vanishes on $\ker\widehat J$. On $\operatorname{ran}\widehat K$, $$\widehat{\mathcal M}\widehat Kx
 =\widehat KA_{\rm phys}\widehat J\widehat Kx
 =\widehat KA_{\rm phys}x.$$ Thus its restriction is conjugate to $A_{\rm phys}$, while the complementary $m$-dimensional block is zero. This proves [\[eq:physical-determinant\]](#eq:physical-determinant){reference-type="ref" reference="eq:physical-determinant"}. Taking the Schur complement of $z\mathrm I_n-\widehat B$ in [\[eq:corrected-augmented\]](#eq:corrected-augmented){reference-type="ref" reference="eq:corrected-augmented"} proves [\[eq:corrected-schur-identity\]](#eq:corrected-schur-identity){reference-type="ref" reference="eq:corrected-schur-identity"} [@HornJohnson2013].

# Structured correction majorants {#sec:majorants}

Let $$\Delta W=\widehat W-W,\qquad
 \Delta Q=\widehat Q-Q=-V\Delta W.$$ From $G=\mathrm I+H$, $$\Delta W=-G^{-1}HW.
 \label{eq:delta-w}$$ Introduce rigorous upper bounds $$v\geq\left\lVert V\right\rVert_2,\quad
 w\geq\left\lVert W\right\rVert_2,\quad
 x\geq\left\lVert A_{\rm phys}V\right\rVert_2,\quad
 y\geq\left\lVert A_{\rm phys}Q\right\rVert_2,
 \label{eq:base-norms}$$ and $$d\geq\left\lVert D\right\rVert_2,\quad
 c\geq\left\lVert C\right\rVert_2,\quad
 e\geq\left\lVert E\right\rVert_2.
 \label{eq:block-norms}$$ Put $$\delta_W=\frac{h}{1-h}w,\qquad
 \delta_Q=v\delta_W.
 \label{eq:pair-majorants}$$

[\[prop:block-majorants\]]{#prop:block-majorants label="prop:block-majorants"} The exact corrected blocks satisfy $$\begin{aligned}
 \left\lVert\widehat D-D\right\rVert_2
 &\leq \delta_D:=\delta_W x,
 \label{eq:delta-d}\\
 \left\lVert\widehat C-C\right\rVert_2
 &\leq \delta_C:=v\delta_W x,
 \label{eq:delta-c}\\
 \left\lVert\widehat E-E\right\rVert_2
 &\leq \delta_E:=
 \delta_W y+d\delta_W+\delta_Wx\delta_W,
 \label{eq:delta-e}\\
 \left\lVert\widehat B-B\right\rVert_2
 &\leq \delta_B:=
 v\delta_Wy+c\delta_W+v\delta_Wx\delta_W.
 \label{eq:delta-b}\end{aligned}$$ Also $\left\lVert\widehat C\right\rVert_2\leq c+\delta_C$.

The first two bounds follow from $$\widehat D-D=\Delta WA_{\rm phys}V,\qquad
 \widehat C-C=-V\Delta WA_{\rm phys}V.$$ Using $\widehat Q=Q-V\Delta W$, $$\begin{aligned}
 \widehat E-E
 &=\Delta WA_{\rm phys}Q
   -D\Delta W
   -\Delta WA_{\rm phys}V\Delta W,\\
 \widehat B-B
 &=-V\Delta WA_{\rm phys}Q
   -C\Delta W
   +V\Delta WA_{\rm phys}V\Delta W.\end{aligned}$$ Take induced norms and apply [\[eq:pair-majorants\]](#eq:pair-majorants){reference-type="ref" reference="eq:pair-majorants"}.

# Leafwise transfer of the two count gates {#sec:leaf-transfer}

## Corrected complement

Let an inherited RH-33 rational leaf $\ell$ carry $$\left\lVert(z\mathrm I-B)^{-1}\right\rVert_2\leq M_\ell
 \quad(z\in\ell).
 \label{eq:stored-resolvent}$$ Define $$\mu_\ell=M_\ell\delta_B.
 \label{eq:complement-product}$$

[\[lem:corrected-complement\]]{#lem:corrected-complement label="lem:corrected-complement"} If $\mu_\ell<1$, then $z\mathrm I-\widehat B$ is invertible on the leaf and $$\left\lVert(z\mathrm I-\widehat B)^{-1}\right\rVert_2
 \leq
 \widehat M_\ell:=
 \frac{M_\ell}{1-\mu_\ell}.
 \label{eq:corrected-resolvent}$$ The straight-line homotopy from $B$ to $\widehat B$ is boundary invertible on that leaf.

Factor $$z\mathrm I-\widehat B
 =(z\mathrm I-B)
 \left[\mathrm I-(z\mathrm I-B)^{-1}(\widehat B-B)\right]$$ and apply the Neumann lemma.

## Stored Feshbach inverse

For the RH-28 parent arc containing $\ell$, let $\kappa_\ell$ bound the projected Feshbach inverse, $\eta_\ell$ be the computable correction ratio, and $c_\ell$ the primal--dual remainder coefficient. The complete inherited bound is $$r_\ell=\eta_\ell+M_\ell c_\ell.
 \label{eq:full-rh28-ratio}$$ RH-33 proves $M_\ell$ lies below the RH-28 conditional budget, hence $r_\ell<1$ on every refined leaf [@WangArcwise2026; @WangAtlas2026]. Therefore $$\left\lVert F(z)^{-1}\right\rVert_2
 \leq K_\ell:=
 \frac{\kappa_\ell}{1-r_\ell},
 \qquad z\in\ell.
 \label{eq:stored-f-inverse}$$

[\[rem:full-remainder\]]{#rem:full-remainder label="rem:full-remainder"} The archived field called the correction ratio is $\eta_\ell$, not the full quantity in [\[eq:full-rh28-ratio\]](#eq:full-rh28-ratio){reference-type="ref" reference="eq:full-rh28-ratio"}. Omitting $M_\ell c_\ell$ would not change the numerical conclusion at the worst RH-35 leaf, but it would make the inverse ledger logically incomplete. The present certificate includes both terms with outward arithmetic.

## Corrected Feshbach map

The resolvent identity gives $$\widehat R-R
 =\widehat R(\widehat B-B)R,
 \qquad
 \widehat R=(z\mathrm I-\widehat B)^{-1}.
 \label{eq:resolvent-difference}$$ Writing $\widehat C=C+\Delta C$, and similarly for the other blocks, $$\begin{aligned}
 \widehat E\widehat R\widehat C-ERC
 &=(\widehat E-E)\widehat R\widehat C
   +E(\widehat R-R)\widehat C
   +ER(\widehat C-C).
 \label{eq:self-energy-difference}\end{aligned}$$ Thus [\[prop:block-majorants,lem:corrected-complement\]](#prop:block-majorants,lem:corrected-complement){reference-type="ref" reference="prop:block-majorants,lem:corrected-complement"} imply $$\begin{aligned}
 \left\lVert\widehat F-F\right\rVert_2
 \leq\phi_\ell
 &:=
 \delta_D
 +\delta_E\widehat M_\ell(c+\delta_C)
 \notag\\
 &\quad
 +e\widehat M_\ell\delta_BM_\ell(c+\delta_C)
 +eM_\ell\delta_C.
 \label{eq:f-difference-majorant}\end{aligned}$$

[\[thm:leafwise-transfer\]]{#thm:leafwise-transfer label="thm:leafwise-transfer"} If every leaf satisfies $$\mu_\ell<1,\qquad
 q_\ell:=K_\ell\phi_\ell<1,
 \label{eq:two-gates}$$ then $$N_\Gamma(\widehat B)=N_\Gamma(B),
 \qquad
 \operatorname{wind}_\Gamma\det\widehat F
 =\operatorname{wind}_\Gamma\det F.
 \label{eq:transferred-counts}$$

The first gate and [\[lem:corrected-complement\]](#lem:corrected-complement){reference-type="ref" reference="lem:corrected-complement"} keep the complete complement homotopy boundary-invertible. For the Feshbach maps, $$\widehat F
 =F\left[\mathrm I+F^{-1}(\widehat F-F)\right],$$ and [\[eq:stored-f-inverse,eq:f-difference-majorant\]](#eq:stored-f-inverse,eq:f-difference-majorant){reference-type="ref" reference="eq:stored-f-inverse,eq:f-difference-majorant"} give $\left\lVert F^{-1}(\widehat F-F)\right\rVert_2\leq q_\ell<1$. The straight-line matrix homotopy is therefore boundary-invertible on each leaf. The exact rational leaves cover all of $\Gamma$, so spectral-count and determinant-winding invariance give [\[eq:transferred-counts\]](#eq:transferred-counts){reference-type="ref" reference="eq:transferred-counts"} [@Ahlfors1979; @GohbergSigal1971].

# Rigorous computation {#sec:computation}

## Outward block bounds

The exact dyadic Gram computation supplies $h$, while exact $4\times4$ Gram matrices for $V^{\mathsf T}V$ and $WW^{\mathsf T}$ give rigorous small-matrix upper bounds for $v$ and $w$. The remaining quantities are computed by the RH-27 componentwise factor graph [@WangOutwardCode2026].

The graph evaluates $A_{\rm phys}V$, $D$, $C$, and $E$ directly from the stored sparse and low-rank factors. To bound $A_{\rm phys}Q$, the $2048$ columns are divided into eight blocks of width $256$. Each block is propagated through $$X\longmapsto U(U(QX))$$ with one outward complex-disc radius per entry. Block Frobenius bounds are combined by an outward Euclidean sum.

lists the resulting global bounds.

::: {#tab:majorants}
  Quantity                                                       Upper bound
  ------------------------------------------------ -------------------------
  $\left\lVert WV-\mathrm I_4\right\rVert_F$         $6.50085\times10^{-16}$
  $\left\lVert(WV)^{-1}\right\rVert_2$                   $1.000000000000001$
  $v\geq\left\lVert V\right\rVert_2$                              $1.136734$
  $w\geq\left\lVert W\right\rVert_2$                              $1.426303$
  $x\geq\left\lVert A_{\rm phys}V\right\rVert_2$                  $1.536772$
  $y\geq\left\lVert A_{\rm phys}Q\right\rVert_2$                  $3.520528$
  $d\geq\left\lVert D\right\rVert_2$                              $1.195080$
  $c\geq\left\lVert C\right\rVert_2$                              $1.070344$
  $e\geq\left\lVert E\right\rVert_2$                              $1.651090$
  $\delta_W$                                         $9.27218\times10^{-16}$
  $\delta_Q$                                         $1.05400\times10^{-15}$
  $\delta_D$                                         $1.42493\times10^{-15}$
  $\delta_C$                                         $1.61976\times10^{-15}$
  $\delta_E$                                         $4.37240\times10^{-15}$
  $\delta_B$                                         $4.70308\times10^{-15}$

  : Rigorous exact-pair and structured block-correction majorants.
:::

## Leafwise results

All scalar combinations are evaluated with $256$-bit Arb arithmetic and rounded outward. The complete transfer ledger has $949$ rows. Every corrected-complement product and every corrected-Feshbach product is below one.

::: {#tab:leaf-results}
  Quantity                                                   Rigorous value
  ------------------------------------------------ ------------------------
  Stored complement inverse $M_\ell$                        $801137.544538$
  Complement product $\mu_\ell$                      $3.76781\times10^{-9}$
  Corrected complement inverse $\widehat M_\ell$            $801137.547556$
  Stored projected inverse $\kappa_\ell$                    $102.575354330$
  Full stored ratio $r_\ell$                         $1.55882\times10^{-7}$
  Stored Feshbach inverse $K_\ell$                          $102.575370320$
  Corrected Feshbach difference $\phi_\ell$                   $0.005334459$
  Feshbach Rouché product $q_\ell$                            $0.547184078$
  Feshbach denominator $1-q_\ell$                             $0.452815922$

  : Worst leafwise transfer quantities. Both maxima occur on parent arc $878$, with center identifier `arc_00879`.
:::

The largest stored Feshbach inverse over all leaves is approximately $112653.101$, but it occurs where the complement inverse is only $222.619$. The leafwise ledger is therefore materially sharper than multiplying unrelated global maxima.

## Floating physical spectrum

As a diagnostic, a dense floating eigensolve of $A_{\rm phys}$ finds exactly one eigenvalue inside the circle. Its floating value is $$-0.0993604146537115-0.4442017426458019i,$$ with a floating interior boundary clearance of $0.0144191037$. The nearest exterior candidate has clearance $0.0491585001$. These numbers are not used in the proof.

![Exact packet-pair transfer. Top left: floating spectrum of the physical two-step matrix, shown only as a diagnostic. Top right: exact dyadic entries of $WV-\mathrm I_4$. Bottom left: all $949$ rigorous corrected-complement and Feshbach products. Bottom right: the exact coordinate and count ledger.](<../../../../../zeta_mvp0/papers/RH-35-exact-packet-pair-physical-count/figures/packet_pair_physical_count.pdf>){#fig:physical-count width="\\textwidth"}

# Main physical count theorem {#sec:main-theorem}

[\[thm:physical-count\]]{#thm:physical-count label="thm:physical-count"} For the exact $2048\times2048$ Perron/parity-extracted physical two-step matrix $$A_{\rm phys}=U^2$$ defined by the stored binary64 factors at $\sigma=10^{-2}$, $$N_\Gamma(A_{\rm phys})=1.
 \label{eq:physical-count-one}$$ Thus exactly one eigenvalue lies in the circle, counted algebraically.

verifies both gates in [\[thm:leafwise-transfer\]](#thm:leafwise-transfer){reference-type="ref" reference="thm:leafwise-transfer"} on all $949$ leaves. Applying [\[eq:rh34-input,eq:transferred-counts\]](#eq:rh34-input,eq:transferred-counts){reference-type="ref" reference="eq:rh34-input,eq:transferred-counts"} gives $$N_\Gamma(\widehat B)=0,\qquad
 \operatorname{wind}_\Gamma\det\widehat F=1.$$ The exact stored circle has center $$-0.3233504401504541-0.5508412474453575i$$ and radius $0.2624987592858511$. Exact dyadic arithmetic gives $$|c|^2-r^2
 =
 \frac{
 27509112334457289433346968324839
 }{
 81129638414606681695789005144064
 }>0,$$ so zero lies outside the disk and $\operatorname{wind}_\Gamma z^4=0$. Taking the winding of [\[eq:corrected-schur-identity\]](#eq:corrected-schur-identity){reference-type="ref" reference="eq:corrected-schur-identity"} yields $$N_\Gamma(A_{\rm phys})
 =N_\Gamma(\widehat B)
  +\operatorname{wind}_\Gamma\det\widehat F
 =0+1.$$

[\[cor:corrected-zero\]]{#cor:corrected-zero label="cor:corrected-zero"} The corrected complement has no eigenvalue in the closed disk, $\widehat F$ is holomorphic there, and $\det\widehat F$ has exactly one zero in the disk, counted with multiplicity.

The complement homotopy excludes boundary crossings and preserves the RH-34 zero interior count. Hence $(z\mathrm I-\widehat B)^{-1}$ is holomorphic in the disk. The transferred winding is one, so the ordinary argument principle gives the assertion.

[\[rem:what-identifies\]]{#rem:what-identifies label="rem:what-identifies"} The count no longer belongs only to the $(n+m)$-dimensional stored augmented realization. It belongs to the full $n$-dimensional matrix $A_{\rm phys}=U^2$ itself. The theorem still concerns the exact finite serialized discretization; the term *physical* does not mean that a continuum operator limit has been proved.

# Audit trail and reproducibility {#sec:audit}

The committed archive contains:

1.  the exact rational numerator and denominator of every entry of $WV-\mathrm I_4$;

2.  the exact-pair, block-majorant, leaf-extrema, count, timing, and hash fields in the main certificate JSON;

3.  all $949$ leaf rows, including the projected inverse, computable RH-28 ratio, remainder coefficient, full inherited ratio, corrected complement product, corrected Feshbach difference, and both homotopy denominators;

4.  a floating spectrum pilot clearly labeled nonvalidated;

5.  dependency hashes for the RH-28 arc ledger, RH-33 resolvent atlas, RH-34 count theorem, physical model builder, and componentwise arithmetic; and

6.  eight unit and archive tests, including a synthetic proof of the $A_{\rm phys}\oplus0_m$ coordinate identity.

The rigorous certificate takes approximately $8.0$ seconds on the reported server. The exact dyadic Gram stage takes under one second; the dominant step is the blockwise componentwise enclosure of $A_{\rm phys}Q$. Timings are diagnostics.

The outward arithmetic assumes IEEE binary64 round-to-nearest operations, conservative operation counts, no overflow, and no harmful underflow [@Higham2002; @Rump2010]. Exact Gram products use rational integer arithmetic, and the final positive scalar combinations use $256$-bit Arb [@Johansson2017].

# Scope, limitations, and next gates {#sec:limitations}

The theorem closes the finite-coordinate bridge at one stored scale. It does not establish the following.

1.  The stored sparse matrix is not enclosed relative to the exact Gaussian integral kernel or an infinite-dimensional transfer operator.

2.  The count has not been continued through smaller noise scales and increasing dimensions.

3.  No interval enclosure of the physical eigenvalue location is given. The theorem is a contour count, not a validated eigenvalue box.

4.  The floating observation that most eigenvalues have tiny modulus is not an exact rank theorem.

5.  No self-adjoint generator, prime-power trace formula, $T\log T$ counting law, zeta-zero identification, Hilbert--Pólya construction, or implication for the Riemann hypothesis is obtained.

The immediate stored-scale chain is now complete: $$\begin{gathered}
\text{projected winding}
\longrightarrow
\text{stored Feshbach winding}\\
\longrightarrow
\text{zero complement count}
\longrightarrow
\text{physical two-step count}.
\end{gathered}$$

The next mathematically distinct gates are scale continuation and spectral localization. A natural continuation paper would combine:

1.  the exact packet correction at several smaller $\sigma$;

2.  a compressed or sparse replacement for dense full-spectrum diagnostics;

3.  validated disks for the unique physical eigenvalue;

4.  perturbation bounds linking adjacent stored dimensions and noise scales.

Only after such finite-scale continuation would a continuum or zero-noise question become well posed.

# Conclusion {#sec:conclusion}

The stored packet pair missed exact biorthogonality by approximately $6.5\times10^{-16}$. That discrepancy is tiny, but the preceding papers correctly refused to erase it algebraically. Exact dyadic arithmetic now shows that the packet Gram is invertible and supplies a canonical rational dual correction.

The correction changes the complement block by at most $4.704\times10^{-15}$. The inherited nonnormal resolvent atlas amplifies this to a worst complement product of $3.768\times10^{-9}$, still far below one. The more demanding Feshbach comparison retains the complete primal--dual remainder and closes with product $0.547185$.

Consequently the corrected packet/complement system has zero complement count and winding one. Exact coordinate factorization then transfers that count to the full stored physical two-step matrix: $$N_\Gamma(U^2)=1.$$ This is the first point in the chain where the unique contour count belongs to the physical $2048$-dimensional finite matrix rather than only to a projected or augmented stored realization. Extending it across scales remains a separate problem.

# Derivation of the block majorants {#app:majorants}

From $\Delta W=-G^{-1}HW$, $$\left\lVert\Delta W\right\rVert_2
 \leq \left\lVert G^{-1}\right\rVert_2\left\lVert H\right\rVert_2\left\lVert W\right\rVert_2
 \leq \delta_W.$$ Because $\Delta Q=-V\Delta W$, $\left\lVert\Delta Q\right\rVert_2\leq\delta_Q$. The exact block differences are $$\begin{aligned}
 \widehat D-D
 &=\Delta WA_{\rm phys}V,\\
 \widehat C-C
 &=-V\Delta WA_{\rm phys}V,\\
 \widehat E-E
 &=\Delta WA_{\rm phys}Q
   -WA_{\rm phys}V\Delta W
   -\Delta WA_{\rm phys}V\Delta W,\\
 \widehat B-B
 &=-V\Delta WA_{\rm phys}Q
   -QA_{\rm phys}V\Delta W
   +V\Delta WA_{\rm phys}V\Delta W.\end{aligned}$$ These identities explain why the certificate uses the directly enclosed quantities $$A_{\rm phys}V,\qquad A_{\rm phys}Q,\qquad D,\qquad C,\qquad E,$$ instead of a crude global bound for $\left\lVert A_{\rm phys}\right\rVert$.

# Reproduction {#app:reproduction}

From this paper directory, run

    PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 python experiments/build_archive.py
    MPLBACKEND=Agg python experiments/make_figures.py
    python experiments/verify_archive.py

The complete rigorous certificate is rebuilt by

    OPENBLAS_NUM_THREADS=32 OMP_NUM_THREADS=32 \
    PYTHONDONTWRITEBYTECODE=1 python \
      experiments/run_packet_pair_certificate.py \
      --sigma 0.01 --chunk-size 256

The manuscript is compiled with

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
