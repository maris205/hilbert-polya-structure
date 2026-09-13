---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-graded-ruelle-complex"
canonical_tex: "henon_dynamics/henon_graded_ruelle_complex/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_graded_ruelle_complex/paper/main.pdf"
source_sha256: "99a26b3d8459a8d8e954f4889e83a404da7a343b4d47d45bd176b23b7b94ba61"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A conditional graded cross-map blueprint for a switched area-preserving Hénon survivor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_graded_ruelle_complex>)
- [规范 TeX](<../../../../../henon_dynamics/henon_graded_ruelle_complex/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_graded_ruelle_complex/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_graded_ruelle_complex/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_graded_ruelle_complex/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We record an effective three-complex-dimensional cross-map candidate for a two-letter area-preserving Hénon survivor. The common domains, rational clearances, correct mixed-data convention, physical tangent-fibre convention, and block-residue sign are exact. A projective lift also gives a holomorphic one-step instability weight. A final theorem audit, however, found that the all-word vector-kernel composition, nuclear trace formula, enlarged output-variable domains, order-zero nuclear factorization, and approximation property had not been proved. Consequently the alternating Fredholm quotient and its joint meromorphic continuation are presented only as conditional consequences. This note is a corrected analytic blueprint and closure record, not a completed Ruelle--Rugh theorem or a Hilbert--Pólya construction.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: 9 August 2026
title: |
  A conditional graded cross-map blueprint for a switched\
  area-preserving Hénon survivor
```

## Markdown 正文

# Exact dynamics and one-step domains

After interchanging the two base coordinates and adjoining the normalized projective coordinate, write $$\label{eq:lift}
 \widehat F_a(x,y,m)=
 \left(y,1-ay^2-x,\frac{\gamma}{-2ay-\beta m}\right),
 \qquad
 a\in\left\{\frac{59}{10},\frac{61}{10}\right\},
 \quad \gamma=\frac{112}{123},\quad\beta=\frac{123}{112}.$$ Define $$X_\sigma=\overline D\left(\sigma\frac{23}{48},\frac7{48}\right),
 \quad
 Y_\sigma=\overline D\left(\sigma\frac{121}{256},\frac{41}{256}\right),
 \quad M=\overline D(0,1/2).$$ The four states are $(\sigma,t)\in\{-,+\}^2$, with edge $(\sigma,t)\to(r,\sigma)$ exactly when $(t,r)\ne(+,+)$. Both parameter letters occur on every edge and are never averaged.

Put $$P_{a,\sigma}(x,z)=\sigma\sqrt{\frac{1-x-z}{a}},
 \qquad
 G_{a,y}(m)=\frac{\gamma}{-2ay-\beta m}.$$ The BPS mixed-data convention [@BPS2003] fixes the contracting input $c=(x,m)\in Y_t\times M$ and the expanding output $z\in X_r$. The expanding input and contracting output are $$h(c,z)=P_{a,\sigma}(x,z),\qquad
 K(c,z)=\bigl(P_{a,\sigma}(x,z),G_{a,P_{a,\sigma}(x,z)}(m)\bigr),$$ and direct substitution gives $$\label{eq:cross}
 \widehat F_a(c,h(c,z))=(K(c,z),z).$$ Thus an inverse pole obtained by prescribing projective output zero belongs to a different mixed boundary-value problem.

The exact disk estimates give $$\label{eq:strict}
 P_{a,\sigma}(Y_t\times X_r)\Subset X_\sigma,
 \qquad
 (P,G_{a,P}(M))\Subset Y_\sigma\times M,$$ with normalized image ratios $$\label{eq:ratios}
 \rho_1=\frac{39}{41},\qquad
 \rho_2=\frac{250880}{466211},\qquad
 \rho_3=\frac{907}{915}.$$ The minimum coordinate clearance is $7/5490$. Moreover, $$\left|\det D\widehat F_a\right|
 \ge\frac{50176}{3352561},
 \qquad
 \left|\det D_{(x,m)}K\right|
 \ge\frac{401408}{204506221}.$$ These estimates prove the stated one-step holomorphy, pole exclusion, and injectivity. The ratios in [\[eq:ratios\]](#eq:ratios){reference-type="eqref" reference="eq:ratios"} are compactness data; they are not, without an explicit factorization, a proof of nuclear order zero.

# Frozen fibre and contour conventions

For $i=(\sigma,t)$, consider the candidate scalar space $$\mathcal A_i=
 A_0\bigl((\widehat\mathbb C\setminus Y_t)\times
 (\widehat\mathbb C\setminus M)\times X_\sigma\bigr)$$ and $\mathcal B_{i,k}=\mathcal A_i\otimes\bigwedge^k\mathbb C^3_{\rm phys}$. Scalar arguments are ordered $(x,m,u)$, but the fibre always uses the physical basis $$\label{eq:physicalbasis}
 (e_x,e_y,e_m).$$ Consequently $D\widehat F_a$ is the physical derivative from $(x,y,m)$ to $(x',y',m')$, although the scalar target arguments are ordered $(\zeta_1,\zeta_2,z)=(x',m',y')$. In the cross-ordered fibre basis $(e_x,e_m,e_y)$ the matrix must instead be conjugated by $$S=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.$$

Define $$j_{a,\sigma}(u,m)=-\sigma(-2au-\beta m),\qquad
 g_{a,\sigma,s}(u,m)=
 \exp\bigl(-s\operatorname{Log}j_{a,\sigma}(u,m)\bigr),$$ and $$W_{a,\sigma,s,k}(x,m,u)=
 g_{a,\sigma,s}(u,m)\,\wedge^kD\widehat F_a(x,u,m),$$ with the exterior matrix taken in [\[eq:physicalbasis\]](#eq:physicalbasis){reference-type="eqref" reference="eq:physicalbasis"}. The candidate branch kernel is $$\begin{aligned}
\label{eq:kernel}
 (\mathcal K^{a,i\to j}_{s,k}\psi)(\zeta_1,\zeta_2,z)
 =\int_{\partial Y_t\times\partial M\times\partial X_\sigma}
 &\frac{\partial_zP_{a,\sigma}(x,z)}
 {(\zeta_1-P_{a,\sigma}(x,z))
  (\zeta_2-G_{a,P_{a,\sigma}(x,z)}(m))}
 \notag\\[-1mm]
 &\times
 \frac{W_{a,\sigma,s,k}(x,m,u)\psi(x,m,u)}
 {u-P_{a,\sigma}(x,z)}
 \frac{dx}{2\pi i}\frac{dm}{2\pi i}\frac{du}{2\pi i}.\end{aligned}$$ The product orientation is, by definition, $$\label{eq:orientation}
 dx\wedge dm\wedge du.$$ Writing $du\wedge dm\wedge dx$ would reverse the sign of the three-variable residue. The weight and derivative are evaluated at the source integration variable. Cauchy's formula in $u$ makes [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} equivalent at one step to evaluating them at $u=P_{a,\sigma}(x,z)$.

The graph block is the sum of the two letter kernels. This preserves the microstep clock and makes later matrices act on the left. The exact clearances make the displayed one-step integral well-defined and bounded on the original domains. No order-zero conclusion is drawn here.

# Exact residue algebra

[\[lem:sign\]]{#lem:sign label="lem:sign"} Suppose an iterated cross pair has contracting dimension two and expanding dimension one. Write $A=\partial_cK$, $B=\partial_zK$, $C=\partial_ch$, and $D=\partial_zh$. Order both variables and residuals as $(x,m,u)$ and $$R=(x-K_1,m-K_2,u-h).$$ Then $$\det DR=-D\det(I-DF).$$ With orientation [\[eq:orientation\]](#eq:orientation){reference-type="eqref" reference="eq:orientation"}, the simple raw residue with numerator $D$ is $-1/\det(I-DF)$.

Differentiating [\[eq:cross\]](#eq:cross){reference-type="eqref" reference="eq:cross"} gives $$DF=
 \begin{pmatrix}A&B\\0&I\end{pmatrix}
 \begin{pmatrix}I&0\\C&D\end{pmatrix}^{-1},
 \qquad
 DR=\begin{pmatrix}I-A&-B\\-C&I-D\end{pmatrix}.$$ Multiplying by the second triangular block and taking determinants gives the identity. The residue statement follows with the common variable, residual, and product-orientation order.

For every $3\times3$ matrix $M$, $$\sum_{k=0}^3(-1)^k\operatorname{tr}(\wedge^kM)=\det(I-M).$$ Thus, if the proposed word trace is eventually proved, the raw minus forces total parity $k+1$. The real orientation sign used in the scalar surface kernel of [@BPS2003] produces an absolute denominator and is not inserted in [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}.

# Unclosed analytic gates

The following steps are required before the candidate can be called a nuclear Ruelle complex.

1.  Prove a block iterated-pinning lemma. Ordinary composition of cross maps does not solve the intermediate mixed boundary data.

2.  Prove by induction that a product of branch kernels is one iterated kernel with numerator $\partial_z h_w$ and fibre cocycle $$g_s^{(n)}\wedge^kD
     (\widehat F_{a_{n-1}}\circ\cdots\circ\widehat F_{a_0}),$$ with no extra contour sign.

3.  Prove that the canonical nuclear trace equals the diagonal contour integral and that the latter has exactly the declared fixed-point residues, including periods one and two, repetitions, and graph coding multiplicity.

4.  Construct explicit intermediate Banach spaces and an enlarged output $z$-disk. On every enlarged domain retain the square-root branch, pole exclusion, and common logarithm sector.

5.  Factor each branch as a bounded map followed by a restriction with an explicit rank-one expansion. Establish locally uniform $p$-nuclear bounds for a fixed $p\le2/3$, preferably for every $p>0$. The image ratio $\rho_3$ is not automatically the restriction ratio of an enlarged output-$z$ disk.

6.  In reciprocal coordinates identify the infinity-vanishing space with $w_1w_2A(\overline\mathbb D^3)$ and prove its metric approximation property using tensor Fejér projections. The blanket statement that closed ideals inherit the approximation property is insufficient.

7.  Prove $s$-holomorphy locally uniformly in the chosen nuclear quasi-norm. Boundedness of $\operatorname{Log}j$ on the original domains is necessary but does not replace the enlarged-domain factorization.

The accompanying symbolic program verifies rational constants, the finite-dimensional block identity, exterior algebra, and sample chronology. It does not prove any item in this list.

# Conditional Fredholm consequence

Assume all gates in the preceding section. Then the intended trace formula would be $$\label{eq:conditionaltrace}
 \operatorname{tr}\mathcal L_{s,k}^n
 =-\sum_{x\in\operatorname{Fix}\widetilde{\mathcal F}^n}
 \frac{g_s^{(n)}(x)\operatorname{tr}(\wedge^kD\widetilde{\mathcal F}^n_x)}
 {\det(I-D\widetilde{\mathcal F}^n_x)},$$ and hence $$\sum_{k=0}^3(-1)^{k+1}\operatorname{tr}\mathcal L_{s,k}^n=B_n(s).$$ Under the same assumptions, the Grothendieck factors $D_k(z,s)=\operatorname{Det}(I-z\mathcal L_{s,k})$ would be jointly entire and, in the initial normal-convergence domain, $$\label{eq:conditionaldet}
 D_{\rm inst}(z,s)
 =\prod_{k=0}^3D_k(z,s)^{(-1)^{k+1}}
 =\frac{D_1(z,s)D_3(z,s)}{D_0(z,s)D_2(z,s)}.$$ The right side would define a meromorphic germ on $\mathbb C^2$, with polar divisor contained in the zero divisor of $D_0D_2$ after possible cancellation. Equations [\[eq:conditionaltrace\]](#eq:conditionaltrace){reference-type="eqref" reference="eq:conditionaltrace"}--[\[eq:conditionaldet\]](#eq:conditionaldet){reference-type="eqref" reference="eq:conditionaldet"} are conditional statements, not results of this note.

# Research boundary

Analytic pinning, holomorphic nuclear restriction, exterior Lefschetz cancellation, and alternating dynamical determinants are classical [@Ruelle1976; @Ruelle1990; @Rugh1996; @BPS2003]. This package retains exact Hénon domains, constants, conventions, and residue algebra while making the remaining theorem debt explicit. It proves no arithmetic Euler product, Riemann divisor, functional equation, or self-adjoint Hilbert--Pólya operator. Its proper status is conditional analytic blueprint and closure note.
