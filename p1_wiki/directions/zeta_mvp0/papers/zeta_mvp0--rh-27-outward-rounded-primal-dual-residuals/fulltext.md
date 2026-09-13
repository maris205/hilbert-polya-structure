---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-27-outward-rounded-primal-dual-residuals"
canonical_tex: "zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/outward-rounded-primal-dual-residuals.pdf"
source_sha256: "2b1029ba49cd4807fce18c6aa2fb84eea7135b1aa703d0cec58ec4565d210776"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Outward-Rounded Primal--Dual Residual Enclosures at a Quadratic Band-Merging Map: Stored-Factor Error Graphs, a Normwise False Failure, and Componentwise Recovery

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/outward-rounded-primal-dual-residuals.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Primal--dual residual squaring can make a directional Feshbach error proportional to the product of two residuals, but the residuals reported in the preceding calculation were ordinary binary64 values near the floating recurrence floor. This paper replaces them by outward-rounded enclosures for an exact finite model defined by the stored binary64 factors. If $M,R,L,\Lambda,V,W$ denote the stored sparse transfer matrix, peripheral factors, and packet pair, we define exactly $$U=M-R\Lambda L^*,\qquad Q=\mathrm I-VW,$$ $$B=QU^2Q,\quad C=QU^2V,\quad D=WU^2V,\quad E=WU^2Q.$$ No computed projector or eigensystem is assumed exact beyond this stored-factor definition. For $A_z=z\mathrm I-B$, a base and deep primal pair $X_J,X_K$, and a dual approximation $Z$, set $$r=C-A_zX_K,\qquad s=E^*-A_z^*Z,$$ and retain the base-consistency term $\delta_J=z\mathrm I-D-EX_J-F_J$. We prove the exact identity $$F-F_J=\delta_J-E(X_K-X_J)-Z^*r-s^*A_z^{-1}r.$$

  Under the standard round-to-nearest model, with no overflow or harmful underflow, we propagate two nested enclosure geometries through the complete sparse/dense computation graph. A normwise scheme stores one Frobenius radius, whereas a componentwise scheme stores one complex-disc radius per entry. Dot products use conservative $\gamma_{4k+8}$ bounds for real matrices acting on complex data and $\gamma_{16k+16}$ for fully complex products; every bound operation is rounded outward. Small packet inverses are certified by a Neumann defect. The resulting quantities $\bar\eta$ and $\bar c$ satisfy $$\left\lVert F_J^{-1}(F-F_J)\right\rVert_2
   \leq \bar\eta+\left\lVert A_z^{-1}\right\rVert_2\bar c,$$ and therefore give a downward-rounded conditional inverse budget $M_*^-=(1-\bar\eta)/\bar c$.

  The normwise audit covers seven stored matrices with $2048\leq n\leq204800$ and 32 nodes per contour. It succeeds at the first six scales, but gives a transparent false failure at $\sigma=10^{-4}$: four nodes have $\bar\eta\geq1$, with maximum $5.66$, although the corresponding floating-centre ratio is only $4.97\times10^{-11}$. Componentwise refinement of the two finest scales reduces the maximum ratios to $2.38\times10^{-4}$ and $1.32\times10^{-3}$. At the finest scale it lowers the worst nodal bound by a factor $4.29\times10^3$ and restores a minimum conditional budget $4.78\times10^{11}$. A hybrid normwise/componentwise audit has $\max\bar\eta=2.33\times10^{-2}$ and $\min M_*^-=6.30\times10^8$ across all seven scales. An independent 63-bit-significand reevaluation consumes at most $9.30\times10^{-5}$ of the corresponding componentwise radius.

  These results certify outward residual and small-matrix budget calculations for the stored finite factors, subject to the stated floating-point model. They do not supply an upper bound for $\left\lVert A_z^{-1}\right\rVert_2$, validate contour arcs, enclose construction error from the continuous Gaussian kernel, or prove a root count for the continuous transfer operator.
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
  **Outward-Rounded Primal--Dual Residual Enclosures** **at a Quadratic Band-Merging Map:**\
  Stored-Factor Error Graphs, a Normwise False Failure,\
  and Componentwise Recovery
```

## Markdown 正文

**Keywords:** outward rounding; componentwise error; primal--dual residual; Feshbach map; matrix Rouché theorem; Arnoldi method; nonnormal resolvent; quadratic map.

**MSC 2020:** 37E05; 47A10; 47A55; 47B65; 65F10; 65F15; 65G20; 65P30.

# Introduction {#sec:introduction}

Goal-oriented error estimation uses an adjoint residual to estimate a small quantity of interest without first controlling a full state error [@BeckerRannacher2001; @GilesSuli2002]. This is especially natural for a Feshbach reduction: the quantity of interest is a packet matrix of rank at most nine, whereas the complement has up to 204800 coordinates and is strongly nonnormal. The preceding primal--dual calculation proved that the unresolved Feshbach term contains the product of a primal and a dual residual [@WangPrimalDual2026]. Its smallest reported conditional inverse budget was $3.35\times10^{24}$.

That number was intentionally not presented as a certificate. Both residuals were evaluated in ordinary binary64 arithmetic, often at $10^{-15}$--$10^{-13}$ relative scale. A residual near machine precision can be numerically informative and still be unsuitable for a proof. Matrix construction, sparse products, oblique packet removal, two-step composition, residual subtraction, and small goal solves all contribute errors. Moreover, a single global norm can erase the spatial structure that makes these errors benign.

The present paper resolves this finite-dimensional arithmetic layer. Its main contributions are as follows.

1.  **A coherent exact stored-factor model.** The sparse matrix and all low-rank factors are treated as exact binary64 numbers. The blocks $B,C,D,E$ are defined by their exact algebraic composition. A base consistency defect is retained explicitly, so the argument does not assume that a floating projected Feshbach matrix is exactly equal to a separately reconstructed ambient formula.

2.  **An outward floating-point calculus.** Frobenius balls and componentwise complex discs are propagated through the entire factor graph using standard $\gamma_k$ estimates [@Higham2002], with all scalar and array bounds rounded toward increasing radius. The proof is an induction over the actual operation graph, not an appeal to an unrecorded solver tolerance.

3.  **A certified small inverse interface.** The packet matrix inverse and all products involving it are bounded by a Neumann defect. This turns the residual balls into an explicit upper Rouché contribution and a downward conditional inverse budget.

4.  **A resolved false failure.** The deliberately coarse normwise scheme fails at four nodes of the finest contour. The componentwise scheme, with identical centres and no model or parameter change, reduces the worst bound by more than three orders of magnitude and restores a positive budget. Thus enclosure geometry, not the floating centre, is the limiting object at that scale.

The hierarchy of claims is central. Exact algebraic identities and floating-point enclosure lemmas are theorem-level statements under their explicit arithmetic assumptions. The seven-scale numbers are reproducible finite-matrix calculations. The sampled winding is a diagnostic only. There is still no validated upper bound for the complement resolvent, no arcwise continuation of the nodal bounds, and no passage to a continuous or zero-noise operator.

# Exact stored-factor Feshbach identity {#sec:identity}

## The finite model

Fix stored binary64 arrays $$M\in\mathbb R^{n\times n},\quad
 R,L\in\mathbb R^{n\times2},\quad
 \Lambda\in\mathbb R^{2\times2},\quad
 V\in\mathbb R^{n\times m},\quad
 W\in\mathbb R^{m\times n}.$$ The sparse matrix $M$ is stored in CSR format and $\Lambda$ is diagonal. Define, in exact arithmetic on these stored numbers, $$U=M-R\Lambda L^*,
 \qquad Q=\mathrm I-VW.
 \label{eq:stored-uq}$$ The notation $Q$ is convenient, but no exact idempotence is assumed: rounding in the construction of $V,W$ is part of the stored data. Set $$B=QU^2Q,
 \quad C=QU^2V,
 \quad D=WU^2V,
 \quad E=WU^2Q.
 \label{eq:stored-blocks}$$ For a spectral parameter $z$, let $$A_z=z\mathrm I-B,
 \qquad
 F(z)=z\mathrm I-D-EA_z^{-1}C,
 \label{eq:exact-feshbach}$$ whenever $A_z$ is invertible. This model is finite and unambiguous. It does not claim that the stored factors are exact eigenvectors, exact packet duals, or exact quadrature data for an underlying continuum operator.

## Base consistency and primal--dual correction

Let $F_J\in\mathbb C^{m\times m}$ be a stored base Feshbach matrix, and let $X_J,X_K,Z\in\mathbb C^{n\times m}$ be stored base primal, deep primal, and dual approximations. Define $$\begin{aligned}
 Y&=X_K-X_J, \\
 r&=C-A_zX_K, \\
 s&=E^*-A_z^*Z, \\
 \delta_J&=z\mathrm I-D-EX_J-F_J.
 \label{eq:all-defects}\end{aligned}$$ The consistency term $\delta_J$ closes a small but important logical gap. Even when $F_J$ and $X_J$ come from the same Arnoldi construction, their separately rounded reconstructions need not satisfy $F_J=z\mathrm I-D-EX_J$ exactly.

[\[thm:stored-identity\]]{#thm:stored-identity label="thm:stored-identity"} If $A_z$ is invertible, then $$F(z)-F_J
 =\delta_J-EY-Z^*r-s^*A_z^{-1}r.
 \label{eq:stored-pd-identity}$$

Since $r=C-A_zX_K$, $A_z^{-1}C=X_K+A_z^{-1}r$. Therefore $$F-F_J
 =z\mathrm I-D-EX_J-F_J-E(X_K-X_J)-EA_z^{-1}r.$$ The first four terms give $\delta_J$, and $s^*=E-Z^*A_z$ implies $EA_z^{-1}r=Z^*r+s^*A_z^{-1}r$.

Define the computable part $$\Delta=\delta_J-EY-Z^*r.
 \label{eq:computed-delta}$$ Then all unresolved inverse dependence is confined to the bilinear remainder $-s^*A_z^{-1}r$. The identity is exact for arbitrary stored approximations; small residuals are not needed for its validity.

# Outward enclosure calculus {#sec:enclosures}

## Arithmetic assumptions

Let $u=2^{-53}$ and $$\gamma_k=\frac{ku}{1-ku}.
 \label{eq:gamma}$$ We assume IEEE-754 binary64 round-to-nearest arithmetic [@IEEE7542019], no overflow, and no underflow large enough to invalidate the relative-error model. Every BLAS or sparse reduction is assumed to be a sequence of correctly rounded elementary operations with no more than the operation count reserved below. Fused multiply-add or a tree reduction only decreases this conservative count. Bound arithmetic uses `nextafter` toward increasing radius after each scalar or array operation.

For a real matrix times complex data, a length-$k$ dot product is assigned $4k+8$ real operations. For a fully complex product it is assigned $16k+16$. The first count covers two real dot products and the Euclidean recombination; the second covers complex multiplication and accumulation. Complex addition and scalar multiplication use guards $\gamma_8$ and $\gamma_{16}$, respectively. These constants are intentionally larger than implementation-specific sharp bounds.

## Normwise Frobenius balls

A Frobenius ball $[X]_F=(\widehat X,\rho_X)$ represents every matrix $X$ satisfying $$\left\lVert X-\widehat X\right\rVert_F\leq\rho_X.$$

Suppose $A$ is an exact stored matrix and $\alpha_A\geq\left\lVert|A|\right\rVert_2$. If a matrix product has inner dimension $k$, the implemented normwise rule is $$\rho_{AX}
 =\operatorname{up}\!\left(
 \alpha_A\rho_X+\gamma_{\kappa(k)}\alpha_A
 \left\lVert\widehat X\right\rVert_F
 \right),
 \label{eq:normwise-product}$$ centred at $\operatorname{fl}(A\widehat X)$. The bound $\alpha_A$ is the smaller of an outward Frobenius bound and the outward estimate from $\left\lVert|A|\right\rVert_1$ and $\left\lVert|A|\right\rVert_\infty$. Sparse products use the maximum stored row count in $\kappa(k)$; adjoint sparse products use the maximum stored column count.

For two uncertain factors, submultiplicativity gives $$\begin{aligned}
 \rho_{XY}=\operatorname{up}\big(&
 \left\lVert|\widehat X|\right\rVert_2\rho_Y
 +\rho_X\left\lVert\widehat Y\right\rVert_F
 +\rho_X\rho_Y \\
 &+\gamma_{\kappa(k)}\left\lVert|\widehat X|\right\rVert_2
 \left\lVert\widehat Y\right\rVert_F\big).
 \label{eq:normwise-uncertain-product}\end{aligned}$$ This global geometry is cheap, but every intermediate error is immediately allowed to point in the worst possible direction.

## Componentwise complex discs

A componentwise ball $[X]_c=(\widehat X,P_X)$, with $P_X\geq0$, represents every matrix $X$ satisfying $$|X-\widehat X|\leq P_X$$ entrywise.

For exact stored $A$, the componentwise multiplication rule is $$P_{AX}=\operatorname{up}\!\left(
 |A|P_X+\gamma_{\kappa(k)}|A||\widehat X|
 \right),
 \label{eq:component-product}$$ centred at the same $\operatorname{fl}(A\widehat X)$. Positive products used on the right-hand side are themselves enlarged by division by $1-\gamma_{\kappa(k)}$. For uncertain factors, $$\begin{aligned}
 P_{XY}=\operatorname{up}\big(&|\widehat X|P_Y+P_X|\widehat Y|+P_XP_Y \\
 &+\gamma_{\kappa(k)}|\widehat X||\widehat Y|\big).
 \label{eq:component-uncertain-product}\end{aligned}$$ Addition, subtraction, conjugation, diagonal scaling, and scalar multiplication are handled entrywise. Finally, $$_c\subseteq
 [X]_F=\left(\widehat X,\ \operatorname{up}\left\lVert P_X\right\rVert_F\right).
 \label{eq:component-to-frobenius}$$

[\[lem:local-enclosure\]]{#lem:local-enclosure label="lem:local-enclosure"} Under the arithmetic assumptions above, [\[eq:normwise-product,eq:normwise-uncertain-product\]](#eq:normwise-product,eq:normwise-uncertain-product){reference-type="ref" reference="eq:normwise-product,eq:normwise-uncertain-product"} enclose the exact stored-matrix products in Frobenius norm, and [\[eq:component-product,eq:component-uncertain-product\]](#eq:component-product,eq:component-uncertain-product){reference-type="ref" reference="eq:component-product,eq:component-uncertain-product"} enclose them entrywise.

The standard dot-product model gives $|\operatorname{fl}(A\widehat X)-A\widehat X|
\leq\gamma_{\kappa(k)}|A||\widehat X|$ [@Higham2002]. Add $|A|P_X$ for uncertain input. For two uncertain factors, expand $(\widehat X+\Delta X)(\widehat Y+\Delta Y)$, take entrywise absolute values, and include the centre-product rounding term. Taking Frobenius norms and using submultiplicativity gives the normwise formulas. Outward rounding of every nonnegative bound operation preserves the inequalities.

[\[thm:graph-enclosure\]]{#thm:graph-enclosure label="thm:graph-enclosure"} Apply either enclosure calculus to the operation graph [\[eq:stored-uq,eq:stored-blocks,eq:all-defects,eq:computed-delta\]](#eq:stored-uq,eq:stored-blocks,eq:all-defects,eq:computed-delta){reference-type="ref" reference="eq:stored-uq,eq:stored-blocks,eq:all-defects,eq:computed-delta"}. Then the returned balls contain the exact stored-factor values of $D,C,E^*,r,s,\delta_J,Y$, and $\Delta$.

The source factors are radius-zero balls. Each graph node is an operation covered by [\[lem:local-enclosure\]](#lem:local-enclosure){reference-type="ref" reference="lem:local-enclosure"}; induction over the directed acyclic graph proves the claim. Notice that both occurrences of $U$, both packet removals, the construction of $D,C,E^*$, and all final subtractions are included.

This is a standard-model verification in the spirit of floating-point validation methods [@MooreKearfottCloud2009; @Rump2010]; it is not a claim that the hardware centre operations were executed under a global directed-rounding mode.

# Small inverse and conditional Rouché budget {#sec:budget}

The packet matrices have order at most nine, so their inverse action can be certified separately. Let $G$ be a stored approximate inverse of $F_J$, and let an outward calculation give $$q\geq\left\lVert\mathrm I-F_JG\right\rVert_F,
 \qquad q<1.
 \label{eq:neumann-defect}$$

[\[prop:neumann\]]{#prop:neumann label="prop:neumann"} Under [\[eq:neumann-defect\]](#eq:neumann-defect){reference-type="ref" reference="eq:neumann-defect"}, $$\left\lVert F_J^{-1}\right\rVert_2
 \leq \frac{\left\lVert G\right\rVert_F}{1-q}=:\mathcal I_J.
 \label{eq:inverse-upper}$$ For any matrix $H$, $$\left\lVert F_J^{-1}H\right\rVert_2
 \leq \left\lVert GH\right\rVert_F+\mathcal I_Jq\left\lVert H\right\rVert_F.
 \label{eq:inverse-product-upper}$$ The same formulas remain valid when every right-hand quantity is replaced by an outward upper enclosure.

Writing $D_J=\mathrm I-F_JG$ gives $F_J^{-1}=G+F_J^{-1}D_J$. Rearranging the norm inequality proves [\[eq:inverse-upper\]](#eq:inverse-upper){reference-type="ref" reference="eq:inverse-upper"}; multiplying the identity by $H$ proves [\[eq:inverse-product-upper\]](#eq:inverse-product-upper){reference-type="ref" reference="eq:inverse-product-upper"}.

Let the graph calculation and [\[prop:neumann\]](#prop:neumann){reference-type="ref" reference="prop:neumann"} provide $$\begin{aligned}
 \bar\eta&\geq\left\lVert F_J^{-1}\Delta\right\rVert_2,\\
 \bar r&\geq\left\lVert r\right\rVert_2,\\
 \bar w&\geq\left\lVert F_J^{-1}s^*\right\rVert_2,
 \qquad \bar c=\operatorname{up}(\bar w\bar r).
 \label{eq:eta-c}\end{aligned}$$

[\[thm:outward-budget\]]{#thm:outward-budget label="thm:outward-budget"} For every $M\geq\left\lVert A_z^{-1}\right\rVert_2$, $$\left\lVert F_J^{-1}(F-F_J)\right\rVert_2
 \leq\bar\eta+M\bar c.
 \label{eq:outward-rouche}$$ If $\bar\eta<1$, define $$M_*^-=\operatorname{down}\!\left(\frac{1-\bar\eta}{\bar c}\right),
 \label{eq:downward-budget}$$ with the usual infinite value when $\bar c=0$. Then any validated $M<M_*^-$ is sufficient for the matrix Rouché inequality at that node. If $\bar\eta\geq1$, the returned budget is zero.

Apply $F_J^{-1}$ to [\[eq:stored-pd-identity\]](#eq:stored-pd-identity){reference-type="ref" reference="eq:stored-pd-identity"}, group the first three terms as $\Delta$, and use $$\left\lVert F_J^{-1}s^*A_z^{-1}r\right\rVert_2
 \leq\left\lVert F_J^{-1}s^*\right\rVert_2\left\lVert A_z^{-1}\right\rVert_2\left\lVert r\right\rVert_2.$$ The matrix Rouché conclusion follows from the usual strict norm condition [@GohbergSigal1971]. Downward rounding makes [\[eq:downward-budget\]](#eq:downward-budget){reference-type="ref" reference="eq:downward-budget"} conservative.

The theorem produces an admissible threshold, not the missing inverse upper bound. The inverse-information no-go theorem in the preceding paper shows that nonzero primal and dual residuals cannot remove this requirement in general [@WangPrimalDual2026].

# Seven-scale protocol {#sec:protocol}

## Centres and factor graph

The physical centres are reconstructed from the same stored factors and shift-invariant Arnoldi families used in the preceding contour calculations [@WangContourFeshbach2026; @WangDirectionalRouche2026]. For each noise scale:

1.  build the sparse folded Gaussian midpoint matrix and the two stored peripheral mode pairs;

2.  build the packet synthesis/analysis pair $V,W$, then independently reconstruct the exact stored-factor blocks $D,C,E^*$ through the enclosure graph;

3.  construct primal and adjoint Arnoldi families to depth $J+16$;

4.  at 32 stored contour nodes, reconstruct $X_J,X_{J+16},Z$, enclose $r,s,\delta_J,Y,\Delta$, certify the small inverse products, and compute $\bar\eta,\bar c,M_*^-$;

5.  record the determinant phase of the corrected centre as a sampled diagnostic.

The dimensions span 2048--204800, packet ranks span 4--9, and maximum primal/dual depths span 52--78. The largest CSR matrix has 67667810 nonzeros. Every row has at most 333 stored nonzeros; the maximum column count grows from 664 to 6642. Across all scales the smallest nonzero stored magnitude is about $7.09\times10^{-17}$, no stored input is subnormal, and all computed centres and radii remain finite. These checks support, but do not replace, the no-harmful-underflow assumption.

## Two enclosure geometries

The inexpensive normwise graph is run at all seven scales. Its purpose is both practical and diagnostic: it shows where loss of direction becomes fatal. The componentwise graph is then run at $\sigma=2\times10^{-4}$ and $10^{-4}$, with the same centres, contour, depths, and factors. It carries nonnegative radius arrays through two additional positive products per sparse action. No contour or tolerance is retuned after observing the normwise failure.

An independent cross-check casts the $\sigma=10^{-2}$, node-zero stored factors to the platform `longdouble` type, which has a 63-bit significand on the test machine. Sparse products are reevaluated by explicit CSR row reductions rather than the binary64 SciPy kernel. This is a diagnostic of enclosure utilization, not part of the formal binary64 proof.

# Results {#sec:results}

## Normwise closure and its boundary

reports the maximum outward correction ratio and the minimum downward budget on each 32-node contour. Relative residual columns divide the outward Frobenius bound by the Frobenius norm of the corresponding stored centre block; they are scale diagnostics rather than interval quotients.

::: {#tab:normwise}
                $\sigma$      $n$   $m$   $J/K$             $\max\bar\eta$               $\min M_*^-$   $\max\bar r/\left\lVert C\right\rVert_F$   $\max\bar s/\left\lVert E^*\right\rVert_F$
  ---------------------- -------- ----- ------- -------------------------- -------------------------- ------------------------------------------ --------------------------------------------
               $10^{-2}$     2048     4   36/52   $2.123\!\times\!10^{-6}$   $8.924\!\times\!10^{14}$                   $5.798\!\times\!10^{-9}$                     $2.111\!\times\!10^{-9}$
    $4\!\times\!10^{-3}$     5120     5   42/58   $3.548\!\times\!10^{-5}$   $1.190\!\times\!10^{13}$                   $4.209\!\times\!10^{-8}$                     $1.101\!\times\!10^{-8}$
    $2\!\times\!10^{-3}$    10240     6   46/62   $7.797\!\times\!10^{-4}$   $1.596\!\times\!10^{11}$                   $3.113\!\times\!10^{-7}$                     $6.060\!\times\!10^{-8}$
               $10^{-3}$    20480     7   50/66   $6.359\!\times\!10^{-3}$    $5.888\!\times\!10^{9}$                   $3.543\!\times\!10^{-6}$                     $3.874\!\times\!10^{-7}$
    $5\!\times\!10^{-4}$    40960     7   54/70   $2.325\!\times\!10^{-2}$    $6.301\!\times\!10^{8}$                   $4.253\!\times\!10^{-6}$                     $4.544\!\times\!10^{-7}$
    $2\!\times\!10^{-4}$   102400     8   58/74   $4.388\!\times\!10^{-1}$    $4.294\!\times\!10^{6}$                   $4.660\!\times\!10^{-5}$                     $2.928\!\times\!10^{-6}$
               $10^{-4}$   204800     9   62/78                    $5.658$                        $0$                   $4.959\!\times\!10^{-4}$                     $1.840\!\times\!10^{-5}$

  : Seven-scale normwise audit. A zero budget means that at least one node has $\bar\eta\geq1$.
:::

The first six scales satisfy $\bar\eta<1$ at every sampled node. At the finest scale, four nodes fail; node 12 at angle $3\pi/4$ is worst with $\bar\eta=5.6575$. The floating-centre ratio there is only $4.9736\times10^{-11}$. The discrepancy is not caused by a large computed correction. It comes from repeatedly replacing structured error vectors by one adversarial Frobenius direction. The maximum normwise residual inflation over the observed centre norm reaches $1.79\times10^9$.

![Normwise seven-scale audit. Top left: floating-centre residuals and outward relative bounds. Top right: RH-26 floating budgets, outward lower budgets, and the RH-23 one-vector resolvent lower bound shown only as a scale comparison. Bottom left: centre and outward correction ratios. Bottom right: residual inflation caused by the global ball.](<../../../../../zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/figures/outward_residual_summary.pdf>){#fig:normwise width="\\textwidth"}

## Componentwise recovery

compares the two geometries at the finest two scales. The tightening-factor interval is the minimum and maximum of $\bar\eta_{\rm norm}/\bar\eta_{\rm comp}$ over the contour.

::: {#tab:componentwise}
                $\sigma$      $n$   $\max\bar\eta_{\rm norm}$   $\max\bar\eta_{\rm comp}$                                   tightening    $\min M_{*,\rm comp}^-$      $\max(\bar r,\bar s)$
  ---------------------- -------- --------------------------- --------------------------- -------------------------------------------- -------------------------- --------------------------
    $2\!\times\!10^{-4}$   102400    $4.388\!\times\!10^{-1}$    $2.381\!\times\!10^{-4}$   $1.41\!\times\!10^3$--$2.46\!\times\!10^3$   $5.379\!\times\!10^{12}$   $7.241\!\times\!10^{-8}$
               $10^{-4}$   204800                     $5.658$    $1.317\!\times\!10^{-3}$   $2.91\!\times\!10^3$--$5.65\!\times\!10^3$   $4.784\!\times\!10^{11}$   $3.259\!\times\!10^{-7}$

  : Componentwise refinement. The centres are unchanged.
:::

At the formerly failing node 12, componentwise propagation gives $$\bar r=2.02\times10^{-7},\qquad
 \bar s=3.39\times10^{-8},\qquad
 \left\lVert\delta_J\right\rVert_F\leq5.29\times10^{-8},$$ $$\bar\eta=1.3173\times10^{-3},\qquad
 M_*^-=4.7841\times10^{11}.$$ The nodal ratio is tightened by a factor $4.29\times10^3$. The finest scale is therefore not close to failure once locality is retained.

Using the normwise result for the first five scales and the componentwise result for the final two gives a seven-scale hybrid audit with $$\max_{\sigma,z_j}\bar\eta=2.3254\times10^{-2},
 \qquad
 \min_{\sigma,z_j}M_*^-=6.3013\times10^8.
 \label{eq:hybrid-result}$$ The maximum comes from the normwise $\sigma=5\times10^{-4}$ layer, not from either componentwise layer.

![Normwise and componentwise bounds on the two finest contours. Top: outward correction ratio; the horizontal line is the Rouché threshold one. Bottom: downward conditional inverse budget. The four zero-budget normwise nodes at $\sigma=10^{-4}$ reappear as positive, large-budget componentwise nodes.](<../../../../../zeta_mvp0/papers/RH-27-outward-rounded-primal-dual-residuals/figures/componentwise_refinement.pdf>){#fig:componentwise width="\\textwidth"}

## Cross-checks and sampled centres

The 63-bit-significand physical reevaluation lies inside every tested componentwise ball. Its maximum radius utilization is $9.30\times10^{-5}$, attained in the observation-adjoint block; primal, dual, base-consistency, and total-correction utilizations are all below $2.42\times10^{-5}$. Synthetic unit tests independently cover dense and sparse multiplication, uncertain products, the full factor graph, the Neumann inverse certificate, and both ball geometries.

Every corrected centre has sampled winding one on its 32-node contour. The largest phase increment in the hybrid audit is $2.998$, below $\pi$ but not accompanied by a validated arc image. This is reproducible evidence that the outward corrections do not alter the observed centre winding; it is not an argument-principle proof.

# Evidence hierarchy and limitations {#sec:limitations}

## What is proved

The following statements are exact or conditional theorem-level results.

-   is an exact finite-dimensional identity for the stored factors, including the base consistency term.

-   Under the stated standard floating-point model, [\[lem:local-enclosure,thm:graph-enclosure\]](#lem:local-enclosure,thm:graph-enclosure){reference-type="ref" reference="lem:local-enclosure,thm:graph-enclosure"} enclose every listed graph output. Bound arithmetic is outward-rounded.

-   rigorously reduces the small inverse and inverse products to an outward Neumann defect under the same model.

-   is a sufficient nodal matrix-Rouché condition for any independently validated complement-inverse upper bound below $M_*^-$.

## What the computations establish

For the specified stored arrays and software environment, the archived data show:

-   six-scale normwise success and a four-node normwise false failure at the finest scale;

-   componentwise recovery at both refined scales, with worst ratio $1.32\times10^{-3}$;

-   the hybrid bounds in [\[eq:hybrid-result\]](#eq:hybrid-result){reference-type="ref" reference="eq:hybrid-result"};

-   no stored subnormal inputs, finite computed radii, Neumann defects at most $4.60\times10^{-11}$, and a successful independent extended- precision diagnostic.

## What remains open

Five boundaries must not be blurred.

1.  **Complement inverse.** No upper bound for $\left\lVert A_z^{-1}\right\rVert_2$ is supplied. The values $M_*^-$ are admissible thresholds, not estimates of that inverse. Earlier one-vector resolvent lower bounds cannot fill this role.

2.  **Contour arcs.** Bounds are evaluated at 32 stored nodes. Neither $\bar\eta$, $\bar c$, nor the inverse is extended over complete arcs. The sampled winding therefore remains nonrigorous.

3.  **Matrix construction.** The binary64 entries of the sparse Gaussian matrix and the computed peripheral/packet factors are exact inputs to this paper. Their error relative to exact quadrature, eigenspaces, or analytic packet data is not enclosed.

4.  **Underflow model.** The stored-data audit rules out subnormal inputs and all observed outputs are finite, but a formal hardware-level audit of every elementary intermediate is not provided.

5.  **Operator limits.** Nothing here proves convergence of the finite sections, a small-noise limit, a self-adjoint spectral realization, or any statement about zeta zeros.

The extended-precision reevaluation is deliberately not promoted to an interval proof. Its role is to detect gross implementation mistakes and measure conservatism.

# Next gate and conclusion {#sec:conclusion}

The arithmetic gate left open by the primal--dual paper has now been crossed for the stored finite factors. Ordinary residuals near machine precision were replaced by outward bounds that include sparse action, low-rank deflation, oblique packet removal, two-step composition, block construction, residual subtraction, base consistency, and small inverse products. A global Frobenius ball already succeeds through six scales. Its failure at the seventh is informative rather than terminal: preserving componentwise locality changes the same node from $5.66$ to $1.32\times10^{-3}$.

The next mathematical gate is now sharply defined. One needs an arcwise, validated upper bound for $\left\lVert(z\mathrm I-B)^{-1}\right\rVert_2$, or a direct validated action bound strong enough to replace it, together with arc extensions of the small correction quantities. A uniform bound below $6.30\times10^8$ would fit the most conservative hybrid nodal budget, but this numerical threshold is not itself an existence theorem. Possible routes include a validated preconditioned contraction, a block Grushin inverse, or componentwise interval Krylov actions [@SjoestrandZworski2007; @TrefethenEmbree2005; @Rump2010].

The main conceptual result is that certificate geometry is part of the problem. A normwise failure can be a proof of excessive information loss, not evidence against the underlying spectral mechanism. Here the componentwise route retains enough structure to keep all seven stored finite scales open while making the remaining inverse and contour requirements explicit.

# Reproducibility and archived artifacts {#app:reproducibility}

The repository directory [@WangOutwardCode2026] contains:

-   , implementing normwise outward balls, Neumann inverse certificates, and downward budgets;

-   , implementing componentwise complex-disc propagation;

-   and , implementing the complete stored-factor primal/dual graph;

-   , the seven-scale normwise audit;

-   , the two-scale refinement and hybrid summary;

-   , the independent physical extended-precision diagnostic;

-   seven unit tests, 224 normwise contour rows, 64 componentwise rows, scale summaries, source/input hashes, and PDF/PNG figures.

From this directory, run

    /root/math/.venv/bin/python -m pytest -q
    PYTHONPATH=src /root/math/.venv/bin/python \
      experiments/run_outward_residual_audit.py --reuse
    PYTHONPATH=src /root/math/.venv/bin/python \
      experiments/run_componentwise_refinement.py --reuse

The full recomputation is obtained by omitting `–reuse`; the two finest scales require the large retained Arnoldi bases.

# Operation graph in compact form {#app:graph}

For reference, the primal graph is $$X\mapsto QX\mapsto UQX\mapsto U^2QX\mapsto QU^2QX=BX,$$ and the adjoint graph reverses these factors. The static blocks are $$V\mapsto U^2V\mapsto
 \begin{cases}
 WU^2V=D,\\
 QU^2V=C,
 \end{cases}
 \qquad
 W^*\mapsto (U^*)^2W^*\mapsto Q^*(U^*)^2W^*=E^*.$$ Every arrow is represented by a centre and either a scalar Frobenius radius or a full componentwise radius array. The final conversion to [\[eq:eta-c\]](#eq:eta-c){reference-type="ref" reference="eq:eta-c"} occurs only after $r,s,\delta_J$, and $\Delta$ have been formed.
