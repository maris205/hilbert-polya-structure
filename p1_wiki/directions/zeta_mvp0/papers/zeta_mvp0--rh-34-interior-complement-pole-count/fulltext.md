---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-34-interior-complement-pole-count"
canonical_tex: "zeta_mvp0/papers/RH-34-interior-complement-pole-count/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-34-interior-complement-pole-count/interior-complement-pole-count.pdf"
source_sha256: "f459be5b103cdcbfdf8acdf966543e96396e2498cccda5e615a9eaef67e63bf4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Certified Schur-Similarity Closure of the Interior Complement Pole Count From Relative Winding One to an Ordinary Stored Feshbach Zero

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-34-interior-complement-pole-count>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-34-interior-complement-pole-count/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-34-interior-complement-pole-count/interior-complement-pole-count.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-34-interior-complement-pole-count/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-34-interior-complement-pole-count/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A certified complement-resolvent atlas for a finite packet--complement spectral model proved a full-boundary Feshbach winding of one and the exact relative count $$N_\Gamma(\mathcal M_{\rm st})-N_\Gamma(B)=1,$$ but left the interior complement count $N_\Gamma(B)$ open. This paper closes that remaining gate for the exact $2048$-dimensional operator defined by the stored binary64 factors at $\sigma=10^{-2}$.

  A floating complex Schur decomposition is used only to generate stored candidate matrices $Z$ and $T_{\rm ref}=\operatorname{triu}(T)$. The proof does not trust the computed eigenvalues or the floating Schur identity. Instead, the complete componentwise stored-factor graph independently certifies $$\left\lVert BZ-ZT_{\rm ref}\right\rVert_F\leq 9.55227\times10^{-10},
   \qquad
   \left\lVert Z^*Z-\mathrm I\right\rVert_F\leq5.33031\times10^{-9}.$$ The second bound proves that $Z$ is invertible. For the exact similar matrix $C=Z^{-1}BZ$, the first gives a rigorous perturbation bound from $C$ to the exact stored upper-triangular matrix $T_{\rm ref}$.

  The $949$-leaf rational resolvent atlas from the preceding work is then transported through this similarity. Its largest inherited complement resolvent bound is $8.01138\times10^5$, while the largest rigorous Neumann product along the complete boundary homotopy from $C$ to $T_{\rm ref}$ is only $$7.65268\times10^{-4}<1.$$ Thus $B$ and $T_{\rm ref}$ have the same eigenvalue count in the circle. Finally, every diagonal entry of $T_{\rm ref}$, the circle center, and the radius is treated as an exact dyadic number. Exact rational signs place all $2048$ diagonal entries outside the circle and none on its boundary. Consequently $$N_\Gamma(B)=0,\qquad N_\Gamma(\mathcal M_{\rm st})=1.$$ The stored Feshbach determinant is therefore holomorphic in the enclosed disk and has exactly one zero there, counted with multiplicity.

  This is a rigorous computer-assisted theorem for one exact finite stored model. It is not a continuum or zero-noise result, does not identify the augmented stored block with the original physical discretization without an additional packet-pair argument, and makes no claim about zeta zeros, a Hilbert--Pólya operator, or the Riemann hypothesis.
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
  **A Certified Schur-Similarity Closure of the\
  Interior Complement Pole Count**\
  From Relative Winding One to an Ordinary Stored Feshbach Zero
```

## Markdown 正文

**Keywords:** certified Schur decomposition; spectral count; Feshbach map; complement pole; outward rounding; verified numerical linear algebra; nonnormal spectrum.

**MSC 2020:** 15A18; 47A10; 47A11; 47A55; 65F15; 65F35; 65G20; 65P30.

# Introduction {#sec:introduction}

Finite-dimensional Feshbach reductions separate a small retained packet from an ambient complement. They are especially useful for nonnormal transfer matrices, where the retained determinant can be much smaller than the full operator but inherits poles from the complement resolvent. A boundary winding of the reduced determinant is therefore naturally a *relative* count: zeros of the augmented block minus poles contributed by the complement.

The contour program considered here reached precisely that point in the preceding paper. For a stored quadratic band-merging model at $\sigma=10^{-2}$, a sparse Grushin construction and outward componentwise residual arithmetic produced $109$ rigorous complement inverse certificates. A $256$-bit Arb transport then covered the complete circle by $949$ exact rational leaves. Combined with an independently certified projected winding, this proved $$\operatorname{wind}_\Gamma\det F=1,\qquad
 N_\Gamma(\mathcal M_{\rm st})-N_\Gamma(B)=1$$ for the exact finite matrices defined by the serialized binary64 factors [@WangLedger2026; @WangAtlas2026]. The statement was intentionally not promoted to an ordinary one-zero theorem: an unknown complement eigenvalue count could still contribute poles inside the circle.

The remaining problem is an interior spectral count for a $2048\times2048$ nonnormal dense-looking matrix $$B=QU^2Q.$$ Direct floating eigenvalues strongly suggest that the count is zero, but this is not a theorem. Nonnormal eigenvalues can be highly sensitive, and an eigenvalue plot supplies neither a validated boundary homotopy nor a proof that a computed decomposition belongs to the exact stored target [@TrefethenEmbree2005]. A direct interval eigensolve at dimension $2048$ would also ignore the sparse-plus-low-rank factor structure already available from the preceding certificates.

The route taken here is a posteriori and deliberately simple. A standard floating Schur decomposition produces a candidate change of basis $Z$ and an upper-triangular candidate $T_{\rm ref}$ [@GolubVanLoan2013]. These candidates are merely stored matrices. The exact target $B$ is then reapplied through the full outward-rounded factor graph, yielding a rigorous residual for $$BZ-ZT_{\rm ref}.$$ An independent outward product certifies the near-unitarity defect $Z^*Z-\mathrm I$. Once $Z$ is proved invertible, exact similarity turns the target into $C=Z^{-1}BZ$, and the certified residual becomes a norm bound for $C-T_{\rm ref}$. The already available RH-33 boundary resolvent atlas then provides exactly the information required for a straight-line spectral homotopy from $C$ to $T_{\rm ref}$.

The contributions are:

1.  a general residual theorem converting a candidate Schur pair, a certified unitarity defect, and a boundary resolvent bound into an exact contour-count equivalence;

2.  a blockwise componentwise certificate for $BZ-ZT_{\rm ref}$ and $Z^*Z-\mathrm I$ against the exact stored-factor target;

3.  a leafwise transport of all $949$ RH-33 complement resolvent bounds through the certified similarity;

4.  an exact dyadic classification of the $2048$ stored diagonal entries of $T_{\rm ref}$ relative to the stored circle;

5.  the first rigorous interior complement count for this chain, $N_\Gamma(B)=0$; and

6.  the consequent ordinary count $N_\Gamma(\mathcal M_{\rm st})=1$ and one interior zero of the stored Feshbach determinant.

Three evidence levels remain separate throughout.

-   Similarity, singular-value inequalities, Schur triangular counting, boundary homotopy, and the final count identities are exact algebra.

-   Residual, unitarity, and leafwise product bounds are rigorous computer-assisted statements for exact stored binary64 inputs under the stated floating-point assumptions.

-   The initial full-spectrum eigensolve, timings, and decimal boundary distances are diagnostics only. No floating eigenvalue is used to establish the count.

# Stored model and inherited relative theorem {#sec:stored-model}

## Exact stored factors

Fix $\sigma=10^{-2}$ and $n=2048$. Every serialized binary64 real or complex component is interpreted as an exact dyadic number. Let $M\in\mathbb C^{n\times n}$ be the stored sparse one-step matrix, $R_{\rm p},L_{\rm p}\in\mathbb C^{n\times p}$ the stored peripheral factors with $p=2$, and $\Lambda\in\mathbb C^{p\times p}$ the diagonal matrix of their stored values. Put $$U=M-R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}.
 \label{eq:stored-u}$$ Let $V\in\mathbb C^{n\times m}$ and $W\in\mathbb C^{m\times n}$, $m=4$, be the stored packet synthesis and analysis matrices, and define $$Q=\mathrm I-VW.
 \label{eq:stored-q}$$ No exact idempotence of this stored $Q$ is assumed. The complement and packet blocks are $$B=QU^2Q,\qquad
 C_{\rm pck}=QU^2V,\qquad
 D=WU^2V,\qquad
 E=WU^2Q.
 \label{eq:stored-blocks}$$ The subscript on $C_{\rm pck}$ distinguishes the packet forcing block from the similar matrix introduced later.

For $A(z)=z\mathrm I_n-B$, define the exact stored Feshbach function wherever $A(z)$ is invertible by $$F(z)=z\mathrm I_m-D-EA(z)^{-1}C_{\rm pck}.
 \label{eq:stored-feshbach}$$ Its exact augmented block realization is $$\mathcal M_{\rm st}=
 \begin{pmatrix}
  D&E\\
  C_{\rm pck}&B
 \end{pmatrix}.
 \label{eq:stored-augmented}$$ The Schur determinant identity gives $$\det(z\mathrm I_{m+n}-\mathcal M_{\rm st})
 =\det(z\mathrm I_n-B)\det F(z)
 \label{eq:schur-determinant-identity}$$ whenever $z\notin\operatorname{spec}B$. Consequently, on any positively oriented simple contour meeting neither spectrum, $$\operatorname{wind}_\Gamma\det F
 =N_\Gamma(\mathcal M_{\rm st})-N_\Gamma(B).
 \label{eq:relative-count}$$ These statements do not require $Q^2=Q$.

## The inherited circle and boundary atlas

The counting circle has the exact stored center and radius $$c=-0.3233504401504541-0.5508412474453575i,
 \qquad
 r=0.2624987592858511,
 \label{eq:circle}$$ and $$\Gamma=\{c+r e^{i\theta}:0\leq\theta\leq2\pi\}.$$ The decimals in [\[eq:circle\]](#eq:circle){reference-type="ref" reference="eq:circle"} name exact binary64 values, not exact decimal rationals.

The preceding atlas theorem supplies the following input [@WangAtlas2026].

[\[thm:inherited\]]{#thm:inherited label="thm:inherited"} For the exact stored matrix $B$ and circle $\Gamma$:

1.  $z\mathrm I-B$ is invertible for every $z\in\Gamma$;

2.  an exact rational partition of $\Gamma$ into $949$ leaves carries rigorous bounds $$\left\lVert(z\mathrm I-B)^{-1}\right\rVert_2\leq M_\ell
            \quad\text{for every \(z\) in leaf \(\ell\)};$$

3.  $\max_\ell M_\ell=801137.5445371413$;

4.  the stored Feshbach boundary winding is $\operatorname{wind}_\Gamma\det F=1$; and

5.  the exact relative count is $$N_\Gamma(\mathcal M_{\rm st})-N_\Gamma(B)=1.$$

The theorem controls the complete boundary but says nothing by itself about the number of complement eigenvalues in the disk. That is the only spectral count addressed below.

# A certified Schur-similarity count theorem {#sec:abstract-certificate}

This section isolates the exact linear algebra used by the computation. The candidate matrices need not come from a stable algorithm and need not satisfy a floating Schur identity.

## Near-unitarity and exact similarity

[\[lem:near-unitary\]]{#lem:near-unitary label="lem:near-unitary"} Let $Z\in\mathbb C^{n\times n}$ and suppose $$\left\lVert Z^*Z-\mathrm I\right\rVert_2\leq\eta<1.
 \label{eq:eta}$$ Then $Z$ is invertible and $$\left\lVert Z\right\rVert_2\leq\sqrt{1+\eta},
 \qquad
 \left\lVert Z^{-1}\right\rVert_2\leq\frac{1}{\sqrt{1-\eta}}.
 \label{eq:z-bounds}$$

Every eigenvalue of the Hermitian matrix $Z^*Z$ lies in $[1-\eta,1+\eta]$. These eigenvalues are the squared singular values of $Z$, so the lower endpoint is positive and [\[eq:z-bounds\]](#eq:z-bounds){reference-type="ref" reference="eq:z-bounds"} follows [@HornJohnson2013].

Let $T\in\mathbb C^{n\times n}$ be arbitrary and define the exact residual $$R=BZ-ZT.
 \label{eq:schur-residual}$$ When [\[eq:eta\]](#eq:eta){reference-type="ref" reference="eq:eta"} holds, set $$\widetilde B=Z^{-1}BZ.
 \label{eq:similar-b}$$ This matrix is exactly similar to $B$, regardless of how $Z$ and $T$ were generated.

[\[lem:residual-conversion\]]{#lem:residual-conversion label="lem:residual-conversion"} Under the assumptions of [\[lem:near-unitary\]](#lem:near-unitary){reference-type="ref" reference="lem:near-unitary"}, $$\begin{aligned}
 \left\lVert\widetilde B-T\right\rVert_2
 &\leq \left\lVert Z^{-1}\right\rVert_2\left\lVert R\right\rVert_2,
 \label{eq:transformed-residual}\\
 \left\lVert(z\mathrm I-\widetilde B)^{-1}\right\rVert_2
 &\leq
 \left\lVert Z^{-1}\right\rVert_2\left\lVert Z\right\rVert_2
 \left\lVert(z\mathrm I-B)^{-1}\right\rVert_2
 \label{eq:transformed-resolvent}\end{aligned}$$ whenever $z\notin\operatorname{spec}B$.

From [\[eq:schur-residual,eq:similar-b\]](#eq:schur-residual,eq:similar-b){reference-type="ref" reference="eq:schur-residual,eq:similar-b"}, $$\widetilde B-T=Z^{-1}(BZ-ZT)=Z^{-1}R.$$ Also $$z\mathrm I-\widetilde B=Z^{-1}(z\mathrm I-B)Z,$$ whose inverse is $Z^{-1}(z\mathrm I-B)^{-1}Z$. Taking induced norms proves both bounds.

## Boundary homotopy

For an available complement-resolvent upper bound $M(z)$, define $$q(z)=
 \frac{\sqrt{1+\eta}}{1-\eta}\,
 M(z)\,\rho,
 \qquad
 \rho\geq\left\lVert R\right\rVert_2.
 \label{eq:q-definition}$$

[\[thm:schur-count\]]{#thm:schur-count label="thm:schur-count"} Let $\Gamma$ be a positively oriented simple contour in the resolvent set of $B$. Let $Z,T\in\mathbb C^{n\times n}$, and suppose rigorous bounds satisfy $$\left\lVert Z^*Z-\mathrm I\right\rVert_2\leq\eta<1,\qquad
 \left\lVert BZ-ZT\right\rVert_2\leq\rho.$$ If $M(z)\geq\left\lVert(z\mathrm I-B)^{-1}\right\rVert_2$ on $\Gamma$ and $$\sup_{z\in\Gamma}q(z)<1,
 \label{eq:q-gate}$$ then $T$ has no eigenvalue on $\Gamma$ and $$N_\Gamma(B)=N_\Gamma(T).
 \label{eq:count-equivalence}$$

By [\[lem:near-unitary\]](#lem:near-unitary){reference-type="ref" reference="lem:near-unitary"}, $Z$ is invertible, so $\widetilde B=Z^{-1}BZ$ is defined and has the same eigenvalues as $B$. Let $$H_s=(1-s)\widetilde B+sT
     =\widetilde B-s(\widetilde B-T),
 \qquad 0\leq s\leq1.$$ For $z\in\Gamma$, $$\begin{aligned}
 z\mathrm I-H_s
 &=(z\mathrm I-\widetilde B)
 \left[
  \mathrm I+s(z\mathrm I-\widetilde B)^{-1}(\widetilde B-T)
 \right].\end{aligned}$$ By [\[lem:residual-conversion,eq:z-bounds\]](#lem:residual-conversion,eq:z-bounds){reference-type="ref" reference="lem:residual-conversion,eq:z-bounds"}, $$\begin{aligned}
 &\left\lVert(z\mathrm I-\widetilde B)^{-1}(\widetilde B-T)\right\rVert_2\\
 &\quad\leq
 \left\lVert Z^{-1}\right\rVert_2^2\left\lVert Z\right\rVert_2
 \left\lVert(z\mathrm I-B)^{-1}\right\rVert_2\left\lVert R\right\rVert_2\\
 &\quad\leq
 \frac{\sqrt{1+\eta}}{1-\eta}\,M(z)\rho
 =q(z)<1.\end{aligned}$$ The bracket is therefore invertible by the Neumann lemma for every $(z,s)\in\Gamma\times[0,1]$. No eigenvalue crosses the contour along the homotopy. The argument principle, equivalently finite-dimensional spectral homotopy invariance, gives $$N_\Gamma(B)=N_\Gamma(\widetilde B)=N_\Gamma(T)$$ [@Ahlfors1979; @Kato1995; @GohbergSigal1971].

[\[cor:triangular-count\]]{#cor:triangular-count label="cor:triangular-count"} If $T$ in [\[thm:schur-count\]](#thm:schur-count){reference-type="ref" reference="thm:schur-count"} is upper triangular with diagonal $\tau_1,\ldots,\tau_n$, then $$N_\Gamma(B)
 =\#\{j:\tau_j\text{ lies inside }\Gamma\},
 \label{eq:triangular-count}$$ counting repeated diagonal values with multiplicity.

The characteristic polynomial of $T$ is $\prod_{j=1}^n(z-\tau_j)$.

[\[rem:not-floating-schur\]]{#rem:not-floating-schur label="rem:not-floating-schur"} The exact theorem uses only the stored matrices $Z$ and $T$, the independently certified residual $BZ-ZT$, the independently certified defect $Z^*Z-\mathrm I$, and a rigorous boundary resolvent bound. It does not assert that a floating LAPACK routine computed the exact Schur form of $B$. Any stored candidate pair that passes the same inequalities proves the same count.

# Rigorous construction of the certificate {#sec:construction}

## Candidate generation

For diagnostics, the factorized action is first applied in ordinary binary64 arithmetic to the identity, producing a dense floating center for $B$. A complex Schur decomposition of this center returns floating matrices $T_{\rm fl}$ and $Z$. The exact stored reference is then defined by $$T_{\rm ref}=\operatorname{triu}(T_{\rm fl}),
 \label{eq:tref}$$ where each retained binary64 component and every inserted lower-triangular zero is regarded as exact. The floating eigensolve and Schur routine are candidate generators only.

The ignored local workspace containing $Z$ and $T_{\rm ref}$ has size approximately $128$ MiB. SHA-256 hashes of both exact stored arrays are committed. A complete rerun regenerates the workspace and remeasures all decisive residuals; the compact verification suite checks the committed certificate ledgers.

## Componentwise exact-target action

The RH-27 stored-factor graph evaluates $$X\longmapsto Q\bigl(U(U(QX))\bigr)
 \label{eq:factor-action}$$ without assembling the exact dense matrix $B$ [@WangOutwardCode2026]. Each computed center entry carries an outward complex-disc radius. Sparse and dense dot products use conservative Higham $\gamma_k$ factors, propagated radii are multiplied by entrywise absolute operators, and every positive scalar bound operation is rounded toward $+\infty$ [@Higham2002; @Rump2010].

The $2048$ columns are partitioned into eight blocks of width $256$. For a block $J$, the graph encloses $$R_J=BZ_J-Z(T_{\rm ref})_J.
 \label{eq:block-residual}$$ Separately, direct componentwise dense multiplication encloses $$G_J=Z^*Z_J-\mathrm I_J.
 \label{eq:block-gram}$$ If $r_J$ and $g_J$ are rigorous Frobenius upper bounds for the blocks, then outward Euclidean accumulation gives $$\rho_F=
 \operatorname{up}\sqrt{\sum_J r_J^2},
 \qquad
 \eta_F=
 \operatorname{up}\sqrt{\sum_J g_J^2}.
 \label{eq:block-combination}$$ Because the column blocks are disjoint, $$\left\lVert BZ-ZT_{\rm ref}\right\rVert_2\leq\left\lVert BZ-ZT_{\rm ref}\right\rVert_F\leq\rho_F,
 \qquad
 \left\lVert Z^*Z-\mathrm I\right\rVert_2\leq\left\lVert Z^*Z-\mathrm I\right\rVert_F\leq\eta_F.$$

This evaluation targets the exact algebraic matrix defined by [\[eq:stored-u,eq:stored-q\]](#eq:stored-u,eq:stored-q){reference-type="ref" reference="eq:stored-u,eq:stored-q"}, not the rounded dense center used to obtain the candidate Schur pair. Errors in the candidate decomposition merely increase the measured residual.

## Leafwise similarity transport

For every inherited RH-33 leaf $\ell$, $256$-bit Arb arithmetic treats the binary64 upper bounds $\eta_F,\rho_F,M_\ell$ as exact inputs and computes outward $$\begin{aligned}
 z_{\max}&=\sqrt{1+\eta_F},
 &
 z_{\max}^{-}&=(1-\eta_F)^{-1/2},
 \label{eq:arb-z}\\
 \delta&=z_{\max}^{-}\rho_F,
 &
 K_\ell&=z_{\max}^{-}z_{\max}M_\ell,
 \label{eq:arb-transport}\\
 q_\ell&=K_\ell\delta.
 \label{eq:leaf-product}\end{aligned}$$ The committed leaf ledger stores $M_\ell,K_\ell,\delta,q_\ell$, a downward bound for $1-q_\ell$, and the exact rational leaf endpoints. Arb is used here for convenient directed high-precision scalar arithmetic [@Johansson2017]; the matrix residual enclosures themselves use the componentwise binary64 scheme.

## Exact dyadic triangular classification

Write $\tau_j=a_j+ib_j$ for a diagonal entry of $T_{\rm ref}$, and $c=c_x+ic_y$ for the center in [\[eq:circle\]](#eq:circle){reference-type="ref" reference="eq:circle"}. All five quantities $a_j,b_j,c_x,c_y,r$ are exact dyadic rationals. Define $$\Delta_j=(a_j-c_x)^2+(b_j-c_y)^2-r^2.
 \label{eq:dyadic-margin}$$ The implementation converts each binary64 value to its exact integer fraction and computes the sign of $\Delta_j$ with integer arithmetic. Thus $$\Delta_j<0,\quad \Delta_j=0,\quad \Delta_j>0$$ classify the point as inside, on, or outside the circle with no rounding ambiguity. Decimal distances are retained only as readable diagnostics.

# Certified results {#sec:results}

## Floating pilot

Before certification, an ordinary dense eigensolve of the assembled floating complement center found no eigenvalue inside the circle. The nearest computed eigenvalue was $$-0.0812451464-0.4164220167i$$ with a floating boundary clearance of approximately $0.0144191$. The floating spectral radius was $0.458433$, and $1932$ of the $2048$ eigenvalues had modulus below $10^{-10}$, suggesting a low-effective-rank spectral structure.

These observations motivated the Schur route but prove nothing. In particular, the count below does not use the floating eigenvalues.

## Residual and similarity ledger

gives the decisive outward bounds. The residual centers are near ordinary Schur backward-error scale, while the conservative componentwise radii dominate the final rigorous values.

::: {#tab:certificate}
  Quantity                                                              Rigorous value
  ---------------------------------------------------------- -------------------------
  Residual-center Frobenius upper                              $1.18771\times10^{-14}$
  Residual-radius Frobenius upper                              $9.55216\times10^{-10}$
  $\rho_F=\left\lVert BZ-ZT_{\rm ref}\right\rVert_F$ upper     $9.55227\times10^{-10}$
  Gram-defect-center Frobenius upper                           $5.22638\times10^{-13}$
  Gram-defect-radius Frobenius upper                            $5.32980\times10^{-9}$
  $\eta_F=\left\lVert Z^*Z-\mathrm I\right\rVert_F$ upper       $5.33031\times10^{-9}$
  $\left\lVert Z\right\rVert_2$ upper                                 $1.000000002666$
  $\left\lVert Z^{-1}\right\rVert_2$ upper                            $1.000000002666$
  Maximum inherited $M_\ell$                                           $801137.544538$
  Maximum transformed resolvent $K_\ell$                               $801137.548808$
  Transformed residual $\delta$ upper                          $9.55227\times10^{-10}$
  Maximum $q_\ell=K_\ell\delta$                                 $7.65268\times10^{-4}$
  Minimum $1-q_\ell$ lower                                            $0.999234732068$

  : Certified Schur-similarity ledger for the exact stored $n=2048$ complement at $\sigma=10^{-2}$.
:::

The worst inherited leaf is the rational subarc with parent index $878$, endpoints $68/256$ and $69/256$ in its archived turn convention, and center identifier `arc_00879`. Even there the homotopy product is more than three orders of magnitude below one. All $949$ rows close individually.

[\[thm:full-homotopy\]]{#thm:full-homotopy label="thm:full-homotopy"} Let $Z$ and $T_{\rm ref}$ be the exact stored candidate matrices identified by the committed hashes. Then $Z$ is invertible, and the straight-line homotopy $$H_s=(1-s)Z^{-1}BZ+sT_{\rm ref},\qquad 0\leq s\leq1,$$ has no eigenvalue on $\Gamma$.

gives $\eta_F<1$, so [\[lem:near-unitary\]](#lem:near-unitary){reference-type="ref" reference="lem:near-unitary"} proves invertibility. Every point of $\Gamma$ belongs to one of the $949$ exact rational leaves from [\[thm:inherited\]](#thm:inherited){reference-type="ref" reference="thm:inherited"}. On each leaf, the outward [\[eq:arb-z,eq:arb-transport,eq:leaf-product\]](#eq:arb-z,eq:arb-transport,eq:leaf-product){reference-type="ref" reference="eq:arb-z,eq:arb-transport,eq:leaf-product"} calculation gives $q_\ell<1$. Apply [\[thm:schur-count\]](#thm:schur-count){reference-type="ref" reference="thm:schur-count"} leaf by leaf.

## Exact triangular count

The exact dyadic signs in [\[eq:dyadic-margin\]](#eq:dyadic-margin){reference-type="ref" reference="eq:dyadic-margin"} give $$\#\{\Delta_j<0\}=0,\qquad
 \#\{\Delta_j=0\}=0,\qquad
 \#\{\Delta_j>0\}=2048.
 \label{eq:diagonal-counts}$$ The nearest diagonal entry is index $2$ in zero-based archive indexing, $$\tau_2=
 -0.08124514640528988
 -0.41642201670804313i.$$ Its exact squared margin is the positive rational $$\Delta_2=
 \frac{
 10096296918145525881756484451617
 }{
 1298074214633706907132624082305024
 }>0.
 \label{eq:nearest-exact-margin}$$ The corresponding decimal boundary clearance $0.0144191037$ is only a diagnostic; the sign in [\[eq:nearest-exact-margin\]](#eq:nearest-exact-margin){reference-type="ref" reference="eq:nearest-exact-margin"} is the proof.

![The certified count closure. Top left: the exact stored triangular diagonal, plotted in floating coordinates, and the counting circle. Top right: diagnostic boundary clearances; exact dyadic signs, not these decimal distances, establish the classification. Bottom left: the inherited complement resolvent upper bounds and the transported homotopy products on all $949$ leaves. Bottom right: the exact logical count ledger.](<../../../../../zeta_mvp0/papers/RH-34-interior-complement-pole-count/figures/schur_similarity_closure.pdf>){#fig:closure width="\\textwidth"}

## Main count theorem

[\[thm:complement-zero\]]{#thm:complement-zero label="thm:complement-zero"} For the exact $2048\times2048$ stored complement matrix $B=QU^2Q$ at $\sigma=10^{-2}$, $$N_\Gamma(B)=0.
 \label{eq:complement-zero}$$

By [\[thm:full-homotopy\]](#thm:full-homotopy){reference-type="ref" reference="thm:full-homotopy"}, $$N_\Gamma(B)=N_\Gamma(Z^{-1}BZ)=N_\Gamma(T_{\rm ref}).$$ The matrix $T_{\rm ref}$ is exact upper triangular. give $N_\Gamma(T_{\rm ref})=0$.

[\[cor:ordinary-count\]]{#cor:ordinary-count label="cor:ordinary-count"} For the exact stored augmented block and Feshbach function, $$\begin{aligned}
 N_\Gamma(\mathcal M_{\rm st})&=1,
 \label{eq:augmented-one}\\
 \operatorname{wind}_\Gamma\det F&=1,
 \label{eq:feshbach-winding-one}\end{aligned}$$ and $\det F$ is holomorphic in the enclosed disk with exactly one zero there, counted with multiplicity. Hence that scalar zero has multiplicity one.

Combine [\[thm:complement-zero\]](#thm:complement-zero){reference-type="ref" reference="thm:complement-zero"} with the inherited relative identity in [\[thm:inherited\]](#thm:inherited){reference-type="ref" reference="thm:inherited"} to obtain [\[eq:augmented-one\]](#eq:augmented-one){reference-type="ref" reference="eq:augmented-one"}. The same theorem already gives [\[eq:feshbach-winding-one\]](#eq:feshbach-winding-one){reference-type="ref" reference="eq:feshbach-winding-one"}. Since $B$ has no eigenvalue in the disk or on its boundary, $A(z)^{-1}$ and $F(z)$ are holomorphic throughout the disk. The ordinary argument principle now turns the boundary winding into the number of zeros of $\det F$, with no pole subtraction [@Ahlfors1979].

[\[rem:relative-to-ordinary\]]{#rem:relative-to-ordinary label="rem:relative-to-ordinary"} RH-33 proved winding one without assuming interior holomorphy of $F$. The new statement is stronger for one precise reason: [\[thm:complement-zero\]](#thm:complement-zero){reference-type="ref" reference="thm:complement-zero"} removes all interior complement poles. No new claim about a continuum operator or an external spectral sequence is inserted into that deduction.

# Audit trail and reproducibility {#sec:audit}

The committed archive separates compact verification from the full candidate regeneration.

1.  `schur_similarity_sigma_1e-02.json` records all residual, unitarity, similarity, count, timing, software, and hash fields.

2.  `schur_homotopy_leaves_sigma_1e-02.csv` contains all $949$ inherited rational leaves and their transformed resolvent, perturbation, Neumann product, and denominator bounds.

3.  `schur_diagonal_sigma_1e-02.csv` records each diagonal component in decimal and exact binary64 hexadecimal notation, together with its exact squared-margin sign.

4.  `schur_diagonal_sigma_1e-02.npz` stores the complete triangular diagonal and circle data needed to rerun the exact dyadic classification.

5.  The dependency manifest hashes the consumed RH-28 scale geometry, RH-33 theorem and leaf ledger, RH-27 componentwise arithmetic, and every source file used to reconstruct the target and certificate.

6.  The compact test suite reclassifies the diagonal exactly, checks all $949$ homotopies, verifies the count implications, and tests the abstract theorem on synthetic matrices.

The complete run takes approximately $22.1$ seconds on the reported $64$-logical-core Linux server with NumPy $2.2.6$, SciPy $1.15.3$, and $32$ OpenBLAS threads. Timings are diagnostics and are not theorem inputs.

The trusted arithmetic base is the same as in the outward residual work: IEEE binary64 round-to-nearest operations, conservative operation counts, directed outward bounds, no overflow, and no harmful underflow. The floating Schur algorithm lies outside the trusted base. It proposes $Z,T_{\rm ref}$; the exact-target residual audit decides whether those matrices are useful.

# Scope, limitations, and next gates {#sec:limitations}

The result closes one sharply delimited finite-dimensional gate. It is important not to enlarge its meaning implicitly.

1.  The theorem concerns the exact matrix assembled algebraically from the stored binary64 factors at $\sigma=10^{-2}$. The stored factors are not interval enclosures of exact Gaussian integrals, exact critical constants, or a continuum transfer operator.

2.  No exact idempotence of $Q=\mathrm I-VW$ is assumed. Therefore $\mathcal M_{\rm st}$ is the exact block realization of the stored Feshbach function, but it is not silently identified with the original physical two-step discretization. Such an identification needs an exact packet-pair correction or a separate perturbation theorem.

3.  The proof has not been repeated at the smaller stored noise scales. The present Schur residual route is dense and scales cubically in candidate generation, although the exact-target action remains sparse-plus-low-rank.

4.  The cluster of $1932$ near-zero floating eigenvalues is a diagnostic feature, not a theorem about exact rank or nullity.

5.  No self-adjoint operator, prime-power trace identity, $T\log T$ counting law, zeta-zero identification, Hilbert--Pólya construction, or implication for the Riemann hypothesis is obtained.

The immediate stored-scale contour gate is now complete: boundary resolvent control, relative winding, and interior complement count are all certified. Natural next problems lie in transferring this finite result rather than recounting the same matrix:

1.  certify an exact packet-pair correction relating the stored augmented block to a chosen physical discretization;

2.  repeat the count through a controlled sequence of smaller noise scales and dimensions;

3.  replace the dense Schur candidate by a compressed invariant-subspace construction suggested by the observed low effective spectral rank;

4.  study whether the count and the isolated stored zero persist under a validated operator perturbation or double limit.

Each item requires a new theorem. The present count should be used as a finite anchor, not as a substitute for those limits.

# Conclusion {#sec:conclusion}

The previous boundary atlas reduced the open problem to one integer: $N_\Gamma(B)$. A floating spectrum suggested that the integer was zero, but nonnormality made that observation insufficient. The certified Schur route resolves the issue without a full interval eigensolve.

The key move is to demote the floating Schur decomposition from evidence to candidate generation. Once the exact stored target independently encloses $BZ-ZT_{\rm ref}$ and $Z^*Z-\mathrm I$, exact similarity and the inherited resolvent atlas take over. The worst boundary perturbation product is $7.653\times10^{-4}$, and exact dyadic arithmetic places every triangular diagonal entry outside the circle. Therefore the stored complement has no interior pole.

This turns relative winding one into an ordinary theorem: the exact stored augmented block has one enclosed eigenvalue and the stored Feshbach determinant has one enclosed zero of multiplicity one. The conclusion is finite, rigorous, and auditable. Its value for a broader spectral program depends on the next bridges---packet correction, scale continuation, and continuum control---which remain explicitly open.

# Blockwise certificate formulas {#app:blockwise}

Let the column partition be $\{1,\ldots,n\}=J_1\sqcup\cdots\sqcup J_s$, and let $\mathcal B(X)$ denote the exact action $BX$. For each block, the componentwise graph returns centers and nonnegative radius arrays $$\mathcal B(Z_{J_k})-Z(T_{\rm ref})_{J_k}
 \in [\widehat R_k,P_k],$$ meaning entrywise complex discs. Thus $$\left\lVert R_{J_k}\right\rVert_F
 \leq \left\lVert\widehat R_k\right\rVert_F+\left\lVert P_k\right\rVert_F=:r_k.$$ The exact Frobenius identity for a column partition gives $$\left\lVert R\right\rVert_F^2=\sum_{k=1}^s\left\lVert R_{J_k}\right\rVert_F^2
 \leq\sum_{k=1}^s r_k^2.$$ All norms and the sum of squares are rounded outward. The same argument applies to the Gram defect blocks.

For the archived run, the eight residual block bounds are $$\begin{array}{cccc}
3.462{\times}10^{-10},&
3.536{\times}10^{-10},&
3.392{\times}10^{-10},&
3.316{\times}10^{-10},\\
3.327{\times}10^{-10},&
3.381{\times}10^{-10},&
3.393{\times}10^{-10},&
3.201{\times}10^{-10}.
\end{array}$$ Their outward Euclidean combination is the $\rho_F$ reported in [1](#tab:certificate){reference-type="ref" reference="tab:certificate"}.

# Exact circle test {#app:circle-test}

Python's exact binary64 conversion maps a finite float to the unique rational represented by its sign, significand, and power-of-two exponent. For each diagonal entry, the implementation forms the exact fractions $$a_j=\frac{A_j}{2^{\alpha_j}},\quad
 b_j=\frac{B_j}{2^{\beta_j}},\quad
 c_x=\frac{C_x}{2^{\gamma_x}},\quad
 c_y=\frac{C_y}{2^{\gamma_y}},\quad
 r=\frac{R}{2^\rho}.$$ Clearing powers of two in [\[eq:dyadic-margin\]](#eq:dyadic-margin){reference-type="ref" reference="eq:dyadic-margin"} reduces the classification to the sign of one integer. No transcendental evaluation of the contour parameter is needed because the reference spectrum is compared directly with the circle.

# Reproduction {#app:reproduction}

From this paper directory, the compact archive and figure are rebuilt by

    PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 python experiments/build_archive.py
    MPLBACKEND=Agg python experiments/make_figures.py
    python experiments/verify_archive.py

The full Schur candidate and exact-target residual certificate are rebuilt by

    OPENBLAS_NUM_THREADS=32 OMP_NUM_THREADS=32 \
    PYTHONDONTWRITEBYTECODE=1 python \
      experiments/run_schur_similarity_certificate.py \
      --sigma 0.01 --chunk-size 256

For a local repeat with the ignored Schur workspace, append `–reuse-workspace`. The formal manuscript is compiled with

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
