---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-189-oblique-feshbach-determinant-factorization"
canonical_tex: "zeta_mvp0/papers/RH-189-oblique-feshbach-determinant-factorization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-189-oblique-feshbach-determinant-factorization/main.pdf"
source_sha256: "5f8d6d159b9da91dcdcd0c18654727d69a430538118d1478a0abeaaf4fdf3804"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Oblique Feshbach Determinant Factorization Exact Packet--Complement Coordinates for a Biorthogonal Temporal Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-189-oblique-feshbach-determinant-factorization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-189-oblique-feshbach-determinant-factorization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-189-oblique-feshbach-determinant-factorization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-189-oblique-feshbach-determinant-factorization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-189-oblique-feshbach-determinant-factorization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-188 identifies a surviving directional coupling product but leaves the packet and complement resolvents undefined. This paper supplies the exact finite block decomposition for a biorthogonal temporal packet.

  Let $V,W\in\mathbb C^{n\times r}$ satisfy $W^*V=I_r$. Choose a frame $Z$ for $\ker W^*$ and set $S=[V,Z]$. Then $S$ is invertible and its inverse has the form $S^{-1}=[W^*;Y^*]$, with $Y^*V=0$ and $Y^*Z=I$. In these coordinates $$S^{-1}AS=
   \begin{pmatrix}K&B\\C&D\end{pmatrix},
   \quad
   K=W^*AV.$$ Whenever $zI-D$ is invertible, $$\det(zI-A)
   =\det(zI-D)
   \det\!\left(zI-K-B(zI-D)^{-1}C\right).$$ This is a type-correct oblique Feshbach factorization. The self-energy is the exact object controlled by the directed Schur product.

  A 240-case complex random audit verifies coordinate inversion, block similarity, complement-gauge invariance, the one-factor norm bound, and the determinant identity with zero failures. The maximum relative determinant error is $1.85\times10^{-11}$. The theorem converts the local bi-Krylov candidate into a precise next question: validate the complement resolvent on root contours. It does not itself supply those bounds or prove a physical Riesz shell.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Oblique Feshbach Determinant Factorization\
  Exact Packet--Complement Coordinates for a Biorthogonal Temporal Clock
```

## Markdown 正文

# Why an exact coordinate theorem is needed

The RH-185 packet is not orthogonal. Writing $Q=I-VW^*$ and informally calling $QAQ$ the complement block hides two issues: $Q$ is oblique, and an operator on $\operatorname{Ran}Q$ needs a chosen coordinate norm. A determinant identity should be derived from an actual similarity, not from a symbolic orthogonal block matrix.

Finite-dimensional Feshbach and Schur complement identities are classical [@GohbergGoldbergKaashoek1990]. The contribution here is to state them in the exact packet type produced by RH-184--185 and to make the complement coordinates explicit.

# Biorthogonal packet coordinates

Let $A\in\mathbb C^{n\times n}$ and let $V,W\in\mathbb C^{n\times r}$ satisfy $$\label{eq:biorthogonal}
 W^*V=I_r.$$ The associated oblique projector is $P=VW^*$.

Choose any full-rank $$\label{eq:Z}
 Z:\mathbb C^{n-r}\longrightarrow\ker W^*.$$

[\[prop:coordinates\]]{#prop:coordinates label="prop:coordinates"} The matrix $$\label{eq:S}
 S=[V,Z]$$ is invertible. Its inverse has a unique block-row representation $$\label{eq:Sinv}
 S^{-1}=\begin{bmatrix}W^*\\Y^*\end{bmatrix}$$ with $$\label{eq:dual-relations}
 Y^*V=0,
 \qquad Y^*Z=I_{n-r}.$$

Suppose $Va+Zb=0$. Applying $W^*$ and using $W^*V=I$, $W^*Z=0$ gives $a=0$. Then $Zb=0$, hence $b=0$ because $Z$ has full rank. Thus $S$ is invertible. Multiplying $S^{-1}S=I$ shows that its top row must be $W^*$ and its bottom row satisfies [\[eq:dual-relations\]](#eq:dual-relations){reference-type="eqref" reference="eq:dual-relations"}.

The choice of $Z$ is a complement-coordinate gauge. Different choices are related by an invertible block-triangular similarity and do not change the full determinant.

For norm estimates there is a canonical convenient choice.

[\[prop:orthonormal-complement\]]{#prop:orthonormal-complement label="prop:orthonormal-complement"} Let $Z$ have orthonormal columns spanning $\ker W^*$ and put $Q=I-VW^*$. Then the lower block row of $S^{-1}$ is $$\label{eq:Y-orthonormal}
 Y^*=Z^*Q.$$ Consequently $$\label{eq:D-orthonormal}
 D=Z^*QAZ,
 \qquad
 \left\lVert D\right\rVert\le\left\lVert Q\right\rVert\left\lVert A\right\rVert.$$

Because $QZ=Z$ and $QV=0$, the row $Z^*Q$ satisfies $(Z^*Q)V=0$ and $(Z^*Q)Z=I$. Uniqueness in Proposition [\[prop:coordinates\]](#prop:coordinates){reference-type="ref" reference="prop:coordinates"} gives [\[eq:Y-orthonormal\]](#eq:Y-orthonormal){reference-type="eqref" reference="eq:Y-orthonormal"}. The block formula and its norm bound follow immediately.

This removes one unnecessary oblique factor from the elementary complement bound. The ambient operator $QAQ$ obeys the valid but looser estimate $\left\lVert QAQ\right\rVert\le\left\lVert Q\right\rVert^2\left\lVert A\right\rVert$; the actual Feshbach coordinate block in an orthonormal complement needs only one factor $\left\lVert Q\right\rVert$.

# Exact block operator

Define $$\label{eq:blocks}
 S^{-1}AS=
 \begin{pmatrix}
 K&B\\C&D
 \end{pmatrix},$$ where $$\begin{aligned}
 K&=W^*AV,
 &B&=W^*AZ,
 \label{eq:KB}\\
 C&=Y^*AV,
 &D&=Y^*AZ.
 \label{eq:CD}\end{aligned}$$ The packet block $K$ is exactly the RH-185 compression. The off-diagonal blocks are coordinate forms of the RH-188 directed couplings.

[\[prop:residual\]]{#prop:residual label="prop:residual"} The ambient right residual satisfies $$\label{eq:right-residual}
 AV-VK=ZC,$$ and the left residual satisfies $$\label{eq:left-residual}
 A^*W-WK^*=YB^*.$$

From $AS=S\begin{psmallmatrix}K&B\\C&D\end{psmallmatrix}$, the first block column gives $AV=VK+ZC$. Taking the adjoint of the top block row of $S^{-1}A=\begin{psmallmatrix}K&B\\C&D\end{psmallmatrix}S^{-1}$ gives the second identity.

Thus the numerical residuals and the Feshbach couplings are the same data in different coordinate norms.

If $Z$ is replaced by $Z'=ZG$ for an invertible complement gauge $G$, then $Y'^*=G^{-1}Y^*$ and $$\label{eq:complement-gauge}
 B'=BG,
 \qquad C'=G^{-1}C,
 \qquad D'=G^{-1}DG.$$ It follows that $$\label{eq:complement-self-energy-invariance}
 B'(zI-D')^{-1}C'=B(zI-D)^{-1}C.$$ Thus the self-energy is independent of the complement basis, even though the three separate block norms depend on that basis.

# Feshbach determinant identity

For a spectral parameter $z$ with $zI-D$ invertible, define the self-energy $$\label{eq:self-energy}
 \Sigma(z)=B(zI-D)^{-1}C$$ and the reduced Feshbach matrix $$\label{eq:feshbach-matrix}
 F(z)=zI-K-\Sigma(z).$$

[\[thm:determinant\]]{#thm:determinant label="thm:determinant"} Whenever $zI-D$ is invertible, $$\label{eq:determinant}
 \boxed{
 \det(zI-A)=\det(zI-D)\det F(z).
 }$$

Similarity by $S$ gives $$\det(zI-A)
 =\det\begin{pmatrix}zI-K&-B\\-C&zI-D\end{pmatrix}.$$ Multiply on the left by the determinant-one block matrix $$\begin{pmatrix}I&B(zI-D)^{-1}\\0&I\end{pmatrix}.$$ The result is block lower triangular with diagonal blocks $F(z)$ and $zI-D$. Taking determinants proves [\[eq:determinant\]](#eq:determinant){reference-type="eqref" reference="eq:determinant"}.

[\[cor:schur\]]{#cor:schur label="cor:schur"} If $zI-K$ and $zI-D$ are invertible and $$\label{eq:schur-condition}
 \left\lVert(zI-K)^{-1}\right\rVert
 \left\lVert B\right\rVert
 \left\lVert(zI-D)^{-1}\right\rVert
 \left\lVert C\right\rVert<1,$$ then $F(z)$ is invertible and $z\notin\sigma(A)$.

Factor $F(z)=(zI-K)[I-(zI-K)^{-1}\Sigma(z)]$ and apply the Neumann lemma.

This is the exact location of the four factors recorded architecturally in RH-163 and numerically separated in RH-188.

# Riesz rank consequence

The determinant identity also gives the precise counting statement. The complement count cannot be silently omitted.

[\[thm:riesz-count\]]{#thm:riesz-count label="thm:riesz-count"} Let $\Gamma$ be a positively oriented simple contour on which both $zI-K$ and $zI-D$ are invertible. Suppose $$\label{eq:uniform-schur}
 \sup_{z\in\Gamma}
 \left\lVert(zI-K)^{-1}\right\rVert\left\lVert B\right\rVert
 \left\lVert(zI-D)^{-1}\right\rVert\left\lVert C\right\rVert<1.$$ Then the algebraic eigenvalue count satisfies $$\label{eq:count-sum}
 N_A(\Gamma)=N_K(\Gamma)+N_D(\Gamma).$$ Here $N_T(\Gamma)$ denotes the algebraic multiplicity of the spectrum of $T$ inside $\Gamma$. In particular, $N_A(\Gamma)=N_K(\Gamma)$ if the complement block has no eigenvalues inside $\Gamma$.

For $0\le t\le1$, define $$A_t=S\begin{pmatrix}K&tB\\tC&D\end{pmatrix}S^{-1}.$$ Its reduced matrix is $F_t(z)=zI-K-t^2B(zI-D)^{-1}C$. The bound [\[eq:uniform-schur\]](#eq:uniform-schur){reference-type="eqref" reference="eq:uniform-schur"} makes $F_t(z)$ invertible on $\Gamma$ for every $t$. The full determinant therefore has no contour zero during the homotopy, so its winding number is constant. At $t=0$ the operator is block diagonal and its count is $N_K+N_D$.

The theorem is conditional on continuous packet and complement inverse bounds. To isolate one packet root, one must either validate $N_D(\Gamma)=0$ or compute and retain the complement contribution. Small residuals alone imply neither fact.

# Finite identity audit

The audit uses dimensions $5,7,9,11$, packet ranks $1,2,3$, and twenty complex random trials per pair, for 240 cases. The left frame is corrected to satisfy $W^*V=I$ exactly at floating precision. A numerical nullspace of $W^*$ supplies $Z$, and $Y$ is read from $S^{-1}$.

The maximum errors are:

  identity                                      maximum error
  ------------------------------------ ----------------------
  $S^{-1}S=I$                            $3.22\times10^{-14}$
  block similarity                       $1.01\times10^{-11}$
  relative determinant factorization     $1.85\times10^{-11}$
  orthonormal complement dual row        $2.38\times10^{-12}$
  one-factor norm-bound violation                         $0$
  complement-gauge self-energy           $2.64\times10^{-12}$

All 240 cases pass the declared $10^{-8}$ tolerance.

The identity audit includes nominal recomputation of the self-energy in a second complement gauge. A later validated implementation must additionally enclose that equality. This catches a numerically important failure mode: separate block norms can change greatly under a poor complement basis even though the exact reduced determinant is fixed.

For outward work, the orthonormal choice in Proposition [\[prop:orthonormal-complement\]](#prop:orthonormal-complement){reference-type="ref" reference="prop:orthonormal-complement"} is the baseline because it gives the one-factor bound $\left\lVert D\right\rVert\le\left\lVert Q\right\rVert\left\lVert A\right\rVert$. Another gauge is useful only if the transformation and its improved product bound are both validated.

# Physical next step

For each surviving RH-185 window, the theorem defines a finite exact program:

1.  build outward enclosures of $V,W,K,B,C,D$;

2.  choose root contours from the predeclared length-four geometry;

3.  validate $(zI-D)^{-1}$ on a finite contour mesh;

4.  combine mesh, operator-ball, and coupling errors using the RH-167--168 machinery summarized in RH-171 [@WangRH171];

5.  apply [\[eq:schur-condition\]](#eq:schur-condition){reference-type="eqref" reference="eq:schur-condition"}, compute $N_D$, and use Theorem [\[thm:riesz-count\]](#thm:riesz-count){reference-type="ref" reference="thm:riesz-count"} to count the full Riesz rank.

The only genuinely new hard object is the physical complement resolvent. The packet and coupling types are now exact.

# Boundary

This paper proves a finite determinant identity for every biorthogonal packet pair. It does not validate any physical complement inverse, establish a continuous Schur margin, prove a physical Riesz shell, transport shells across scales, close R or Gate A, or approach a self-adjoint Hilbert--Polya operator or the Riemann Hypothesis.
