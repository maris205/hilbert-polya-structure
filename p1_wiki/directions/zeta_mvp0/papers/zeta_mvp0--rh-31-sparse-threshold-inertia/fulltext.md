---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-31-sparse-threshold-inertia"
canonical_tex: "zeta_mvp0/papers/RH-31-sparse-threshold-inertia/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-31-sparse-threshold-inertia/sparse-threshold-inertia.pdf"
source_sha256: "a26eadb1e8d688d9e888766510437de55d6ccced7966af1c413320752eac0e7c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two-Shift Sparse Inertia Certification of Lifted Grushin Resolvents Exact-Target Weyl Certificates at Three Quadratic Band-Merging Scales

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-31-sparse-threshold-inertia>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-31-sparse-threshold-inertia/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-31-sparse-threshold-inertia/sparse-threshold-inertia.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-31-sparse-threshold-inertia/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-31-sparse-threshold-inertia/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A preceding sparse Grushin linearization reduced a lifted nonnormal resolvent gate to the inverse norm of one bordered matrix, but its rigorous certificate constructed every physical inverse column. This paper replaces that all-column calculation by a fixed number of sparse factorizations.

  For a square Grushin matrix $\mathcal G\in\mathbb C^{m\times m}$ and threshold $\alpha>0$, consider the Hermitian singular-value dilation $$H_\alpha=
   \begin{pmatrix}
    -\alpha\mathrm I&\mathcal G\\
    \mathcal G^*&-\alpha\mathrm I
   \end{pmatrix}.$$ Its inertia is $(m,m,0)$ exactly when $s_{\min}(\mathcal G)>\alpha$. An unnormalized pairwise Hadamard congruence turns this matrix into $$\mathcal T_\alpha=
   \begin{pmatrix}
    \mathcal G+\mathcal G^*-2\alpha\mathrm I&\mathcal G^*-\mathcal G\\
    \mathcal G-\mathcal G^*&-\mathcal G-\mathcal G^*-2\alpha\mathrm I
   \end{pmatrix},$$ using only integer coefficients. For independently chosen $\delta_-,\delta_+>0$, sparse no-pivot LU factorizations of $\mathcal T_\alpha-\delta_-\mathrm I$ and $\mathcal T_\alpha+\delta_+\mathrm I$ are converted to exact Hermitian matrices $\widehat B_\pm=L_\pm\operatorname{Re}(\operatorname{diag}U_\pm)L_\pm^*$. If their normwise backward errors satisfy $\varepsilon_-<\delta_-$ and $\varepsilon_+<\delta_+$ and their inertias agree, Weyl monotonicity sandwiches the exact inertia of $\mathcal T_\alpha$ between them. The two shift distances need not agree.

  The target is not a rounded surrogate. Peripheral, packet, and normalized rank-one lift channels are enclosed componentwise from the exact archived binary64 factors; channel balancing uses exactly reversible powers of two. The resulting Grushin enclosure, threshold-transform rounding, shifted assembly, complex sparse-LU backward error, and $LU$-to-$LDL^*$ conversion are all included in one Frobenius majorant. No inverse norm of $L$ and no inverse columns are required.

  At $\sigma=10^{-2}$, $4\times10^{-3}$, and $2\times10^{-3}$, the exact target certificates have Grushin dimensions $4109$, $10255$, and $20497$. The largest threshold matrix has dimension $40994$, $5.424\times10^7$ nonzeros, and $2.979\times10^8$ factor nonzeros per side. Its two verified errors are $1.43035\times10^{-3}$ and $1.43152\times10^{-3}$, both below $1.5\times10^{-3}$, with common inertia $(20497,20497,0)$. At every scale we choose $\alpha>2/K_*^-$, where $K_*^-$ is the preceding rigorous lifted inverse budget. Hence $\|\widetilde A^{-1}\|_2\leq\|\mathcal G^{-1}\|_2<K_*^-/2$, closing the three selected stored-model lifted gates.

  The result is finite-dimensional and local to three archived scales. It does not prove a full-contour root count, a continuum limit, a Hilbert--Pólya construction, an identification with zeta zeros, or the Riemann hypothesis.
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
  **Two-Shift Sparse Inertia Certification of\
  Lifted Grushin Resolvents**\
  Exact-Target Weyl Certificates at Three\
  Quadratic Band-Merging Scales
```

## Markdown 正文

**Keywords:** verified inertia; sparse LU; singular-value dilation; Grushin problem; nonnormal resolvent; interval arithmetic; Weyl monotonicity.

**MSC 2020:** 15A18; 15A23; 47A10; 65F05; 65F15; 65F50; 65G20; 65P30.

# Introduction {#sec:introduction}

The finite packet--complement program considered here studies stored noisy transfer matrices near a quadratic band-merging regime. Earlier layers constructed a contour Feshbach reduction, directional and primal--dual residual identities, componentwise outward enclosures, and an adaptive arcwise cover. A one-channel deflation then isolated a single dangerous singular direction and reduced the remaining analytic gate to a rigorous upper bound for a lifted complement inverse [@WangDeflated2026]. The immediate predecessor supplied an exact sparse two-step Grushin linearization and closed that gate at two scales by constructing all physical inverse columns and checking a direct Frobenius--Neumann residual [@WangSparseGrushin2026].

That method was sharp but structurally expensive. If the physical dimension is $n$, it solves for $n$ right-hand sides and re-evaluates the exact target on every resulting column. The present paper asks a narrower question: can one certify only the threshold inequality actually needed by the preceding theorem, $$s_{\min}(\mathcal G)>\alpha,
 \label{eq:intro-threshold}$$ using a fixed number of sparse factorizations?

The answer is yes at the first three archived scales. The route has four parts.

1.  A Hermitian dilation turns [\[eq:intro-threshold\]](#eq:intro-threshold){reference-type="ref" reference="eq:intro-threshold"} into an inertia statement.

2.  An exact unnormalized Hadamard congruence stabilizes the paired diagonal structure without introducing irrational coefficients.

3.  Each no-pivot sparse LU factorization is converted to an exact Hermitian $LDL^*$ center whose inertia is read from real pivot signs.

4.  Two independently shifted centers sandwich the exact target by Weyl monotonicity.

The key refinement is that the lower and upper shifts need not be symmetric. This matters numerically: at the middle scale, one symmetric choice makes the upper factorization unstable, while a nearby symmetric choice makes the lower factorization unstable. Selecting the stable side of each pair gives a rigorous asymmetric bracket.

The contributions are:

1.  an exact threshold-inertia equivalence and integer pair congruence;

2.  an asymmetric two-shift Weyl sandwich theorem;

3.  a normwise sparse complex-LU and $LDL^*$ conversion certificate using only $O(\operatorname{nnz}(L)+\operatorname{nnz}(U))$ postprocessing;

4.  a componentwise enclosure connecting the factorized center to the exact RH-29 lifted target, including exact vector normalization;

5.  rigorous certificates at three scales, including the first closure at $\sigma=2\times10^{-3}$;

6.  a transparent record of failed scalar comparison bounds, unstable symmetric shifts, and the finite-scale cost of the successful route.

## Evidence hierarchy

Three levels are kept separate throughout.

1.  *Exact mathematics*: Schur complements, singular-value dilations, congruence, Sylvester inertia, and Weyl monotonicity.

2.  *Rigorous stored-model computation*: componentwise channel enclosures, outward Frobenius bounds, sparse-LU backward errors, $LDL^*$ conversion errors, and inertia brackets.

3.  *Floating evidence*: ordering pilots, central factorizations, failed shift choices, timings, memory, and empirical scaling fits.

Only the second level is inserted into the computer-assisted theorem.

# The exact lifted Grushin target {#sec:target}

Fix one archived scale. Let $M\in\mathbb C^{n\times n}$ be the exact dyadic matrix represented by the stored binary64 one-step transfer matrix. Let $R_{\rm p},L_{\rm p}\in\mathbb C^{n\times p}$ collect stored peripheral modes, let $\Lambda\in\mathbb C^{p\times p}$ be diagonal, and define $$U=M-R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}.
 \label{eq:one-step}$$ Let $V\in\mathbb C^{n\times k}$ and $W\in\mathbb C^{k\times n}$ be the packet synthesis and analysis maps, and put $$Q=\mathrm I-VW.
 \label{eq:packet-complement}$$ For a stored spectral parameter $z_0$, stored positive scalar $\widehat s$, and archived nonzero dyadic vectors $u_0,v_0$, the exact normalized lifted target is $$\widetilde A
 =z_0\mathrm I-QU^2Q+
 \frac{1-\widehat s}{\|u_0\|_2\|v_0\|_2}u_0v_0^*.
 \label{eq:lifted-target}$$ The norms in [\[eq:lifted-target\]](#eq:lifted-target){reference-type="ref" reference="eq:lifted-target"} are exact Euclidean norms of the stored dyadic vectors.

The sparse base linearization is $$\mathcal L_0=
 \begin{pmatrix}
  z_0\mathrm I&-M\\
  -M&\mathrm I
 \end{pmatrix}.
 \label{eq:sparse-base}$$ The identities $$\begin{aligned}
 M-QU&=R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}+V(WU),
 \label{eq:top-correction}\\
 M-UQ&=R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}+(UV)W
 \label{eq:bottom-correction}\end{aligned}$$ factor every dense-looking correction into thin channels. With one lift channel, $2p$ peripheral channels, and $2k$ packet channels, write $$X\in\mathbb C^{2n\times r},\qquad
 Y\in\mathbb C^{r\times2n},\qquad
 r=1+2p+2k,
 \label{eq:channel-shapes}$$ so that $$\mathcal L=\mathcal L_0+XY
 =
 \begin{pmatrix}
 z_0\mathrm I+\dfrac{1-\widehat s}{\|u_0\|_2\|v_0\|_2}u_0v_0^*
 &-QU\\
 -UQ&\mathrm I
 \end{pmatrix}.
 \label{eq:linearized-target}$$ The exact Grushin matrix is $$\mathcal G=
 \begin{pmatrix}
  \mathcal L_0&X\\
  Y&-\mathrm I_r
 \end{pmatrix}
 \in\mathbb C^{m\times m},
 \qquad m=2n+r.
 \label{eq:grushin}$$

[\[prop:physical-compression\]]{#prop:physical-compression label="prop:physical-compression"} Let $J:\mathbb C^n\to\mathbb C^m$ inject a vector into the first $n$ coordinates. Whenever $\mathcal G$ is invertible, $$J^*\mathcal G^{-1}J=\widetilde A^{-1}.
 \label{eq:physical-compression}$$ Consequently, $$\left\lVert\widetilde A^{-1}\right\rVert_2\leq\left\lVert\mathcal G^{-1}\right\rVert_2.
 \label{eq:compression-bound}$$

The Schur complement of $-\mathrm I_r$ in [\[eq:grushin\]](#eq:grushin){reference-type="ref" reference="eq:grushin"} is $\mathcal L_0+XY=\mathcal L$. The Schur complement of the lower-right identity in [\[eq:linearized-target\]](#eq:linearized-target){reference-type="ref" reference="eq:linearized-target"} is [\[eq:lifted-target\]](#eq:lifted-target){reference-type="ref" reference="eq:lifted-target"}. The standard block inverse formula gives [\[eq:physical-compression\]](#eq:physical-compression){reference-type="ref" reference="eq:physical-compression"}. The norm bound follows because $J$ is an isometry.

[\[rem:balancing\]]{#rem:balancing label="rem:balancing"} For any invertible diagonal $D\in\mathbb C^{r\times r}$, replacing $X,Y$ by $XD,D^{-1}Y$ preserves $XY$ and [\[eq:physical-compression\]](#eq:physical-compression){reference-type="ref" reference="eq:physical-compression"}. The implementation chooses every diagonal entry of $D$ to be a power of two. The scaling is accepted only when binary64 forward and reverse `ldexp` operations reproduce every center and radius bit-for-bit. Thus balancing changes the full Grushin norm but introduces no arithmetic uncertainty.

# Threshold dilation and integer pair congruence {#sec:threshold}

Let $G\in\mathbb C^{m\times m}$ and $\alpha>0$. Define the shifted Hermitian dilation $$H_\alpha(G)=
 \begin{pmatrix}
  -\alpha\mathrm I_m&G\\
  G^*&-\alpha\mathrm I_m
 \end{pmatrix}.
 \label{eq:dilation}$$ For a Hermitian matrix $A$, write $$\operatorname{In}(A)=(n_+(A),n_-(A),n_0(A))$$ for its inertia.

[\[lem:threshold-inertia\]]{#lem:threshold-inertia label="lem:threshold-inertia"} The eigenvalues of $H_\alpha(G)$ are $$s_j(G)-\alpha,\qquad -s_j(G)-\alpha,
 \qquad j=1,\dots,m.
 \label{eq:dilation-eigenvalues}$$ Hence $$s_{\min}(G)>\alpha
 \quad\Longleftrightarrow\quad
 \operatorname{In}(H_\alpha(G))=(m,m,0).
 \label{eq:threshold-inertia}$$

Take a singular triplet $Gv_j=s_ju_j$, $G^*u_j=s_jv_j$. Then $(u_j,v_j)^{\mathsf T}$ and $(u_j,-v_j)^{\mathsf T}$ are eigenvectors with the two eigenvalues in [\[eq:dilation-eigenvalues\]](#eq:dilation-eigenvalues){reference-type="ref" reference="eq:dilation-eigenvalues"}. Counting their signs proves [\[eq:threshold-inertia\]](#eq:threshold-inertia){reference-type="ref" reference="eq:threshold-inertia"}.

Direct scalar elimination of [\[eq:dilation\]](#eq:dilation){reference-type="ref" reference="eq:dilation"} can encounter tiny initial pivots because its diagonal is the small scalar $-\alpha$. We instead use the exact integer block $$S=
 \begin{pmatrix}
  \mathrm I_m&\mathrm I_m\\
  \mathrm I_m&-\mathrm I_m
 \end{pmatrix}.
 \label{eq:hadamard}$$ No $2^{-1/2}$ normalization is needed.

[\[prop:pair-congruence\]]{#prop:pair-congruence label="prop:pair-congruence"} Let $C=G+G^*$ and $D=G^*-G$. Then $$\mathcal T_\alpha(G)
 :=S^*H_\alpha(G)S
 =
 \begin{pmatrix}
  C-2\alpha\mathrm I_m&D\\
  -D&-C-2\alpha\mathrm I_m
 \end{pmatrix}.
 \label{eq:threshold-transform}$$ Therefore $$\operatorname{In}(\mathcal T_\alpha(G))=\operatorname{In}(H_\alpha(G)).
 \label{eq:congruence-inertia}$$

Block multiplication gives [\[eq:threshold-transform\]](#eq:threshold-transform){reference-type="ref" reference="eq:threshold-transform"}. The matrix $S$ is nonsingular, so Sylvester's law of inertia gives [\[eq:congruence-inertia\]](#eq:congruence-inertia){reference-type="ref" reference="eq:congruence-inertia"}; see, for example, [@HornJohnson2013].

The ordering is chosen on the $m$ paired coordinates and then expanded by keeping the plus and minus members of each pair adjacent. A COLAMD order obtained from the Grushin sparsity pattern gave the smallest factors among the tested orderings. Ordering is heuristic; the final identity permutations and backward bounds are checked independently.

# Enclosing the exact threshold target {#sec:enclosure}

Every archived binary64 input is interpreted as an exact dyadic number. The products $\Lambda L_{\rm p}^{\mathsf T}$, $UV$, and $WU$ are not silently identified with their rounded centers. They are evaluated by the componentwise complex-disc arithmetic of the preceding outward-residual work [@WangOutwardCode2026]. The lift coefficient $$c_0=\frac{1-\widehat s}{\|u_0\|_2\|v_0\|_2}
 \label{eq:lift-coefficient}$$ is enclosed with Arb at 160-bit precision [@Johansson2017].

After exact power-of-two balancing, let $\widehat X,\widehat Y$ be the binary64 centers and let $R_X,R_Y$ be nonnegative entrywise disc radii. There exist exact channel factors $X,Y$ for [\[eq:grushin\]](#eq:grushin){reference-type="ref" reference="eq:grushin"} such that $$|X-\widehat X|\leq R_X,\qquad
 |Y-\widehat Y|\leq R_Y.
 \label{eq:channel-enclosure}$$ The base blocks are copied from exact stored inputs. Thus the center $\widehat\mathcal G$ satisfies $$\left\lVert\mathcal G-\widehat\mathcal G\right\rVert_2
 \leq\left\lVert\mathcal G-\widehat\mathcal G\right\rVert_F
 \leq
 \eta_G
 :=
 \operatorname{up}\sqrt{\left\lVert R_X\right\rVert_F^2+\left\lVert R_Y\right\rVert_F^2}.
 \label{eq:grushin-enclosure}$$

[\[lem:threshold-enclosure\]]{#lem:threshold-enclosure label="lem:threshold-enclosure"} Let $\widehat\mathcal T_\alpha$ be the binary64 matrix produced by applying [\[eq:threshold-transform\]](#eq:threshold-transform){reference-type="ref" reference="eq:threshold-transform"} and the stored pair permutation to $\widehat\mathcal G$. Under IEEE round-to-nearest arithmetic with no overflow or harmful underflow, $$\left\lVert\mathcal T_\alpha(\mathcal G)-\widehat\mathcal T_\alpha\right\rVert_2
 \leq \eta_T,
 \label{eq:threshold-enclosure}$$ where the implementation uses $$\begin{aligned}
 \eta_T
 &=
 \operatorname{up}\!\left(2\sqrt2\,\eta_G+\eta_{\rm form}\right),
 \label{eq:eta-T}\\
 \eta_{\rm form}
 &=
 \operatorname{up}\!\left[
 \gamma_{64}
 \left(8\left\lVert\widehat\mathcal G\right\rVert_F+4\alpha\sqrt m\right)
 \right].
 \label{eq:formation-error}\end{aligned}$$

Write $E=\mathcal G-\widehat\mathcal G$. The exact transform difference has blocks $E+E^*$ and $E^*-E$ with both signs. The Frobenius parallelogram identity gives $$\left\lVert\mathcal T_\alpha(\mathcal G)-\mathcal T_\alpha(\widehat\mathcal G)\right\rVert_F
 =2\sqrt2\,\left\lVert E\right\rVert_F.$$ For the rounded transform of the center, every occurrence of $\widehat\mathcal G$ or $\widehat\mathcal G^*$ is counted separately in the four blocks, giving the conservative coefficient $8$; the two diagonal $2\alpha\mathrm I_m$ terms give $4\alpha\sqrt m$. At most a fixed number of complex additions occurs per entry, and $\gamma_{64}$ dominates that formation path. The symmetric permutation is exact.

For a shift distance $\delta>0$, forming $\widehat\mathcal T_\alpha\pm\delta\mathrm I_{2m}$ contributes $$\eta_{\rm shift}(\delta)
 =
 \operatorname{up}\!\left[
 \gamma_{16}
 \left(\left\lVert\widehat\mathcal T_\alpha\right\rVert_F+\delta\sqrt{2m}\right)
 \right].
 \label{eq:shift-assembly}$$ The total exact-target input error supplied to the factor certificate is $$\eta_{\rm in}(\delta)=\operatorname{up}\bigl(\eta_T+\eta_{\rm shift}(\delta)\bigr).
 \label{eq:input-error}$$

# Sparse LU to an exact Hermitian inertia center {#sec:ldl}

Let $A\in\mathbb C^{N\times N}$ be one stored shifted threshold matrix, where $N=2m$. SuperLU is run with equilibration disabled, zero diagonal pivot threshold, symmetric mode enabled, and natural scalar ordering after the explicit pair permutation [@Davis2006]. The certificate requires both returned permutations to be the identity.

Let $L,U$ be the stored binary64 factors. Put $$D=\operatorname{diag}\!\left(\operatorname{Re}(\operatorname{diag}U)\right),
 \qquad
 \widehat B=LDL^*.
 \label{eq:hermitian-center}$$ The matrix $\widehat B$ is an exact Hermitian matrix defined by the stored factors. Since $L$ is unit lower triangular, $$\operatorname{In}(\widehat B)=\operatorname{In}(D),
 \label{eq:pivot-inertia}$$ so its inertia is obtained from real pivot signs.

## A conservative complex elimination count

Let $u=2^{-53}$ and $$\gamma_q=\frac{qu}{1-qu}.
 \label{eq:gamma}$$ All archived scalar bounds use an additional upward binary64 step.

[\[lem:complex-lu\]]{#lem:complex-lu label="lem:complex-lu"} Assume the no-pivot sparse factorization is composed of conventional binary64 complex multiply-add accumulations and complex divisions, with no overflow or harmful underflow. For a matrix of order $N$, the returned factors satisfy $$|A-LU|
 \leq
 \gamma_{24N+64}|L||U|.
 \label{eq:componentwise-lu}$$

Expand every complex scalar operation into real rounded operations. A complex product uses four real multiplications and two real additions; its accumulation into a complex partial sum uses two more real additions. Allowing additional rounding for loading, sign changes, panel updates, and the component-to-modulus conversion gives fewer than $24$ real rounded operations per elimination level along any scalar dependency path. Complex division contributes only a fixed path length, absorbed by the additive $64$. At most $N$ elimination levels contribute to any entry. The standard product-of-$(1+\delta)$ argument then gives [\[eq:componentwise-lu\]](#eq:componentwise-lu){reference-type="ref" reference="eq:componentwise-lu"}; compare the usual Gaussian-elimination backward analysis in [@Higham2002; @GolubVanLoan2013]. Blocked or supernodal grouping changes the order of accumulation but not this worst-case path count.

The original pilot used $\gamma_{32N+64}$. The first two scales already passed that stronger overestimate. The archived results are uniformly re-evaluated under [\[lem:complex-lu\]](#lem:complex-lu){reference-type="ref" reference="lem:complex-lu"}; the original files and SHA-256 links are retained. At the third lower shift, the $32N$ total was $1.84768\times10^{-3}$, while the proved $24N$ total is $1.43035\times10^{-3}$. No factor or target datum was changed.

## An $O(\operatorname{nnz})$ normwise bound

The dense product $|L||U|$ is never formed. Writing it as a sum of outer products gives $$\left\lVert|L||U|\right\rVert_F
 \leq
 \sum_{j=1}^N\left\lVert L_{:j}\right\rVert_2\left\lVert U_{j:}\right\rVert_2
 =:\beta_{LU}.
 \label{eq:outer-lu}$$ Every segment norm and the final sum are rounded upward. Hence $$\left\lVert A-LU\right\rVert_F
 \leq \gamma_{24N+64}\beta_{LU}.
 \label{eq:lu-frobenius}$$

To convert $LU$ to [\[eq:hermitian-center\]](#eq:hermitian-center){reference-type="ref" reference="eq:hermitian-center"}, define $$R=U-DL^*.
 \label{eq:relation-defect}$$ The stored center of $R$ and its formation radius are bounded separately. If $\widehat R$ is the stored relation defect and $\eta_R$ its formation error, then $$\left\lVert L R\right\rVert_F
 \leq
 \sum_{j=1}^N\left\lVert L_{:j}\right\rVert_2\left\lVert\widehat R_{j:}\right\rVert_2
 +\left\lVert L\right\rVert_F\eta_R
 =:\beta_{\rm conv}.
 \label{eq:conversion-bound}$$

[\[prop:hermitian-bound\]]{#prop:hermitian-bound label="prop:hermitian-bound"} Let $A_{\rm exact}$ be the exact shifted threshold target and let $A$ be its stored input to sparse LU. If $\|A_{\rm exact}-A\|_2\leq\eta_{\rm in}$, then $$\left\lVert A_{\rm exact}-\widehat B\right\rVert_2
 \leq
 \varepsilon
 :=
 \operatorname{up}\!\left(
 \eta_{\rm in}
 +\gamma_{24N+64}\beta_{LU}
 +\beta_{\rm conv}
 \right).
 \label{eq:total-backward}$$

Since $\widehat B=LDL^*$, $$A_{\rm exact}-\widehat B
 =(A_{\rm exact}-A)+(A-LU)+L(U-DL^*).$$ Apply [\[eq:lu-frobenius,eq:conversion-bound\]](#eq:lu-frobenius,eq:conversion-bound){reference-type="ref" reference="eq:lu-frobenius,eq:conversion-bound"}, the triangle inequality, and $\|\cdot\|_2\leq\|\cdot\|_F$.

This construction never bounds $\|L^{-1}\|$, never solves a comparison triangular system, and never constructs an inverse column.

# The asymmetric two-shift Weyl sandwich {#sec:weyl}

The central theorem permits independent lower and upper shifts.

[\[thm:asymmetric-bracket\]]{#thm:asymmetric-bracket label="thm:asymmetric-bracket"} Let $T=T^*\in\mathbb C^{N\times N}$ and let $\delta_-,\delta_+>0$. Suppose exact Hermitian matrices $B_-,B_+$ satisfy $$\begin{aligned}
 \left\lVert B_--(T-\delta_-\mathrm I)\right\rVert_2&<\delta_-,
 \label{eq:lower-condition}\\
 \left\lVert B_+-(T+\delta_+\mathrm I)\right\rVert_2&<\delta_+.
 \label{eq:upper-condition}\end{aligned}$$ Then $$B_-\prec T\prec B_+.
 \label{eq:loewner-sandwich}$$ If $\operatorname{In}(B_-)=\operatorname{In}(B_+)$, then $$\operatorname{In}(T)=\operatorname{In}(B_-)=\operatorname{In}(B_+).
 \label{eq:inertia-sandwich}$$

Write $B_-=T-\delta_-\mathrm I+E_-$. Since $\|E_-\|_2<\delta_-$, one has $E_-\prec\delta_-\mathrm I$, hence $B_-\prec T$. Similarly, $B_+=T+\delta_+\mathrm I+E_+$ and $E_+\succ-\delta_+\mathrm I$, so $T\prec B_+$.

Hermitian eigenvalues are monotone under the Loewner order [@HornJohnson2013]. Therefore $$n_+(B_-)\leq n_+(T)\leq n_+(B_+),
 \qquad
 n_-(B_-)\geq n_-(T)\geq n_-(B_+).$$ If the endpoint counts agree, both inequalities are equalities, proving [\[eq:inertia-sandwich\]](#eq:inertia-sandwich){reference-type="ref" reference="eq:inertia-sandwich"}.

[\[cor:verified-threshold\]]{#cor:verified-threshold label="cor:verified-threshold"} Apply [\[thm:asymmetric-bracket\]](#thm:asymmetric-bracket){reference-type="ref" reference="thm:asymmetric-bracket"} to $T=\mathcal T_\alpha(\mathcal G)$ and to the exact Hermitian centers $B_\pm=L_\pm D_\pm L_\pm^*$ from [\[eq:hermitian-center\]](#eq:hermitian-center){reference-type="ref" reference="eq:hermitian-center"}. If the two bounds from [\[eq:total-backward\]](#eq:total-backward){reference-type="ref" reference="eq:total-backward"} obey $$\varepsilon_-<\delta_-,
 \qquad
 \varepsilon_+<\delta_+,
 \label{eq:verified-shifts}$$ and both real-pivot inertias are $(m,m,0)$, then $$s_{\min}(\mathcal G)>\alpha,
 \qquad
 \left\lVert\mathcal G^{-1}\right\rVert_2<\alpha^{-1}.
 \label{eq:verified-inverse}$$

Use [\[prop:hermitian-bound\]](#prop:hermitian-bound){reference-type="ref" reference="prop:hermitian-bound"} for $\mathcal T_\alpha(\mathcal G)-\delta_-\mathrm I$ and $\mathcal T_\alpha(\mathcal G)+\delta_+\mathrm I$, then [\[thm:asymmetric-bracket,prop:pair-congruence,lem:threshold-inertia\]](#thm:asymmetric-bracket,prop:pair-congruence,lem:threshold-inertia){reference-type="ref" reference="thm:asymmetric-bracket,prop:pair-congruence,lem:threshold-inertia"}.

Shift positions and pair orderings may be explored with floating pilots. This does not enter the theorem probabilistically: every finally selected factorization is rechecked against the exact target by [\[eq:total-backward,eq:verified-shifts\]](#eq:total-backward,eq:verified-shifts){reference-type="ref" reference="eq:total-backward,eq:verified-shifts"}. Failed pilots remain archived.

# Computer-assisted certificates {#sec:results}

At each scale, the threshold is chosen as the next binary64 number above $$\alpha=\frac{2}{K_*^-},
 \label{eq:threshold-choice}$$ where $K_*^-$ is the rigorous downward lifted-inverse budget from RH-29. Thus [\[eq:verified-inverse\]](#eq:verified-inverse){reference-type="ref" reference="eq:verified-inverse"} implies $$\left\lVert\widetilde A^{-1}\right\rVert_2
 \leq\left\lVert\mathcal G^{-1}\right\rVert_2
 <\frac{1}{\alpha}
 <\frac{K_*^-}{2}
 <K_*^-.
 \label{eq:budget-consequence}$$

## Dimensions and factor cost

::: {#tab:cost}
            $\sigma$     $n$     $m$   $N=2m$   $\operatorname{nnz}\mathcal T$          factor nnz   time $-$ (s)   time $+$ (s)   peak GiB
  ------------------ ------- ------- -------- -------------------------------- ------------------- -------------- -------------- ----------
           $10^{-2}$    2048    4109     8218                $9.248\times10^6$   $2.212\times10^7$           20.7           20.8       2.26
    $4\times10^{-3}$    5120   10255    20510                $2.595\times10^7$   $9.523\times10^7$          182.5          183.4       8.69
    $2\times10^{-3}$   10240   20497    40994                $5.424\times10^7$   $2.979\times10^8$         1055.1         1060.6       25.6

  : Sparse threshold systems and shifted factor costs. Factor nonzeros are $\operatorname{nnz}(L)+\operatorname{nnz}(U)$ per side. Time columns are the two selected factorizations. Peak memory is the maximum shifted run, not a complexity theorem.
:::

The pair-ordering times were $2.79$, $12.30$, and $52.36$ seconds; threshold assembly took $1.00$, $2.8$, and $5.9$ seconds. The factorization dominates the third-scale cost.

## Rigorous brackets

[\[thm:computer-assisted\]]{#thm:computer-assisted label="thm:computer-assisted"} Assume the archived binary64 factors are exact dyadic inputs and the IEEE rounding and no-pivot factorization conditions of [\[lem:threshold-enclosure,lem:complex-lu\]](#lem:threshold-enclosure,lem:complex-lu){reference-type="ref" reference="lem:threshold-enclosure,lem:complex-lu"} hold. Then [\[tab:certificates\]](#tab:certificates){reference-type="ref" reference="tab:certificates"} gives valid inertias $$\operatorname{In}(\mathcal T_\alpha(\mathcal G))=(m,m,0)
 \label{eq:three-inertias}$$ at $\sigma=10^{-2}$, $4\times10^{-3}$, and $2\times10^{-3}$. Consequently, $$\begin{aligned}
 \left\lVert\widetilde A^{-1}\right\rVert_2
 &<4748.707259961125
 &&(\sigma=10^{-2}),\label{eq:bound-one}\\
 \left\lVert\widetilde A^{-1}\right\rVert_2
 &<17026.786147026153
 &&(\sigma=4\times10^{-3}),\label{eq:bound-two}\\
 \left\lVert\widetilde A^{-1}\right\rVert_2
 &<44372.232447398855
 &&(\sigma=2\times10^{-3}).\label{eq:bound-three}\end{aligned}$$ Each number is strictly below the corresponding RH-29 admissible budget, so the three selected stored-model lifted-resolvent gates close.

For every row of [\[tab:certificates\]](#tab:certificates){reference-type="ref" reference="tab:certificates"}, the two exact Hermitian centers have the displayed common inertia and satisfy $\varepsilon_\pm<\delta_\pm$. Apply [\[cor:verified-threshold\]](#cor:verified-threshold){reference-type="ref" reference="cor:verified-threshold"}, then [\[eq:budget-consequence\]](#eq:budget-consequence){reference-type="ref" reference="eq:budget-consequence"}. The three displayed bounds are the archived $K_*^-/2$ values.

![Finite-scale diagnostics. Left: factor nonzeros and one-side wall time after a visual rescaling. Right: the rigorous utilization $\varepsilon_\pm/\delta_\pm$; the dotted line is the admissibility boundary. The third scale is close but remains strictly below one.](<../../../../../zeta_mvp0/papers/RH-31-sparse-threshold-inertia/figures/threshold_inertia_scaling.pdf>){#fig:scaling width="98%"}

## Why asymmetric shifts matter

At $\sigma=4\times10^{-3}$ and threshold factor two, the symmetric choice $\delta=5.0\times10^{-4}$ gave correct pivot counts on both sides, but the upper error grew to $1.1293\times10^{-3}$ and failed. Moving symmetrically to $\delta=5.6\times10^{-4}$ reduced the upper error to $1.0457\times10^{-4}$ under the original $32N$ audit, but increased the lower error to $7.0058\times10^{-4}$. The selected asymmetric pair keeps the stable lower factor from the first run and the stable upper factor from the second. This is an actual gain in theorem design, not merely a tuning convenience.

# Complexity, negative findings, and scope {#sec:scope}

## Fixed-factor architecture

The certificate requires exactly two selected sparse factorizations and linear postprocessing in their stored nonzeros. It replaces the $n$ physical right-hand sides of RH-30 by pivot signs and normwise backward errors. This does not imply linear or near-linear asymptotic complexity: fill remains the controlling quantity. Fits over only three finite data points give $$\operatorname{nnz}(L+U)\sim n^{1.61},\qquad
 t_{\rm factor}\sim n^{2.44},\qquad
 M_{\rm peak}\sim n^{1.51}.
 \label{eq:empirical-exponents}$$ These are descriptive fits, not asymptotic theorems. The practical gain is that the third scale closes with two factors and $O(\operatorname{nnz})$ verification; the method is not automatically cheaper at small scales.

## Discarded routes

Three negative findings delimit the successful corridor.

1.  A cancellation-free scalar comparison solve for $\|U^{-1}L^{-1}\|_2$ produced a coarse candidate of order $2.12\times10^{65}$ and is useless here.

2.  Direct elimination of the untransformed shifted dilation starts from the small diagonal $-\alpha$ and suffers tiny-pivot instability. The pair Hadamard congruence repairs that structural defect.

3.  A common symmetric shift is unnecessarily restrictive. Sparse pivot growth can occur on opposite sides at nearby distances, even though exact inertia is unchanged.

These failures do not contradict the spectral target; they identify certificate mechanisms that discard too much cancellation or impose the wrong numerical geometry.

## What is and is not proved

The exact theorem concerns three finite stored matrices. Combined with the preceding one-channel reduction, it closes three selected lifted-resolvent gates. It does *not* by itself:

1.  certify every arc of the archived contour;

2.  prove a contour root count;

3.  pass to zero noise or a continuum operator;

4.  construct a self-adjoint Hilbert--Pólya operator;

5.  identify any eigenvalue with a nontrivial zeta zero;

6.  imply the Riemann hypothesis.

# Outlook {#sec:outlook}

The next technical problem is no longer conceptual. The threshold-inertia route is exact, but the third-scale utilization is about $0.954$. Further progress can come from:

1.  pair-level nested dissection or problem-specific separators to reduce threshold fill;

2.  a sharper verified bound for $\||L||U|\|_F$ that retains block orthogonality instead of summing all outer-product norms;

3.  verified multifrontal $LDL^*$ with symmetric pivot blocks, avoiding the $LU$-to-$LDL^*$ conversion term;

4.  independent asymmetric shift selection at each finer scale;

5.  reuse or updating of symbolic factors across nearby shifts.

Any such extension should preserve the present architecture: exact target enclosure, explicit rounding assumptions, a Hermitian inertia center, and a Weyl sandwich whose final inequalities can be independently audited.

# Reproducibility {#reproducibility .unnumbered}

The repository directory

<https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-31-sparse-threshold-inertia>

contains the source, tests, factorization drivers, original failed pilots, derived operation-count archives with SHA-256 provenance, summary tables, and figure scripts. The principal certificate files are

-   `results/exact_target_inertia_sigma_1e-2_op24.json`,

-   `results/exact_target_inertia_sigma_4e-3_op24.json`,

-   `results/exact_target_inertia_sigma_2e-3.json`.

The tests include dense singular-threshold equivalence, exact pair congruence, asymmetric inertia recovery, exact channel Schur algebra, bit-reversible power-of-two balancing, and a 100-digit enclosure cross-check.

# Acknowledgments {#acknowledgments .unnumbered}

The numerical experiments were performed with NumPy, SciPy/SuperLU, python-flint/Arb, mpmath, and Matplotlib. The author thanks the developers of these open-source packages.
