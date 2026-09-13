---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-162-ambient-realization-reset-riesz-gate"
canonical_tex: "zeta_mvp0/papers/RH-162-ambient-realization-reset-riesz-gate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-162-ambient-realization-reset-riesz-gate/main.pdf"
source_sha256: "24693e35d07c05310be5cbf8b75d7df852702f3f98072e2da9cc2276dc5d946a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Ambient-Realization Gate Between Reset Packets and Riesz Clouds A Type-Correct Primal--Adjoint Coupling Theorem

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-162-ambient-realization-reset-riesz-gate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-162-ambient-realization-reset-riesz-gate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-162-ambient-realization-reset-riesz-gate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-162-ambient-realization-reset-riesz-gate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-162-ambient-realization-reset-riesz-gate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-161 reduced the first determinant gate to a packet-to-Riesz estimate, but its abstract theorem places the reset projection and transfer operator on one Hilbert space. In the archived physical construction the reset packet is a spectral subspace of a source-memory Gram matrix, while the moving cloud is a Riesz subspace of a noisy two-step transfer operator. Equal rank does not identify these spaces.

  We make the missing ambient realization explicit. Let $J:\mathcal E\to\mathcal H$ be an isometry, let $P$ reduce a source operator $M$, and put $\widehat P=JPJ^*$. For a transfer operator $A$ define the primal and adjoint defects $$D=AJ-JM,\qquad D^\sharp=A^*J-JM^*.$$ We prove the directed bounds $$\lVert(I-\widehat P)A\widehat P\rVert\leq\lVert DP\rVert,\qquad
   \lVert\widehat PA(I-\widehat P)\rVert\leq\lVert D^\sharp P\rVert.$$ Thus a type-correct realization supplies exactly the two feedback couplings needed by a Schur resolvent argument. A two-dimensional witness proves that without $J$ the source packet gives no coupling information. We also record the polar repair and its commutator debt for a near-isometric map. A 512-case finite audit has zero bound failures. No canonical prime-dynamics $J$ or all-level defect estimate is constructed, so physical interface R and Gate A remain open.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  The Ambient-Realization Gate Between Reset Packets and Riesz Clouds\
  A Type-Correct Primal--Adjoint Coupling Theorem
```

## Markdown 正文

# Why the ambient space is part of the theorem

The RH-160 reset construction diagonalizes positive memory Grams on a source or clock space [@WangRH160]. RH-80 and RH-161 require a reducing Riesz cloud for a transfer operator. Writing both outputs as a rank-$r$ projection suppresses the domain and is therefore not type-correct. A rank, a list of eigenvalues, or a fitted frame does not define a functorial map between the two spaces.

Let $\mathcal E$ be the source-memory Hilbert space and $\mathcal H$ the transfer space. Let $M\in\mathcal B(\mathcal E)$, $A\in\mathcal B(\mathcal H)$, and let $P$ be a finite-rank orthogonal projection satisfying $PM=MP$. An *ambient realization* is an isometry $J:\mathcal E\to\mathcal H$. Its realized packet is $$\widehat P=JPJ^*,\qquad \widehat Q=I-\widehat P.$$ The complement includes both $J(\operatorname{ran}(I-P))$ and any directions outside $J\mathcal E$; this is essential when the dimensions differ.

# The primal--adjoint realization theorem

[\[thm:realization\]]{#thm:realization label="thm:realization"} With the notation above, define $$D=AJ-JM,\qquad D^\sharp=A^*J-JM^*.$$ Then $$\begin{aligned}
 \lVert\widehat QA\widehat P\rVert&\leq\lVert DP\rVert,\label{eq:out}\\
 \lVert\widehat PA\widehat Q\rVert&\leq\lVert D^\sharp P\rVert.\label{eq:in}\end{aligned}$$ Consequently the two-way feedback product obeys $$\lVert\widehat PA\widehat Q\rVert\,
 \lVert\widehat QA\widehat P\rVert
 \leq \lVert D^\sharp P\rVert\,\lVert DP\rVert.$$

For $x\in\operatorname{ran}P$, reduction gives $MPx\in\operatorname{ran}P$, and hence $JMPx\in\operatorname{ran}\widehat P$. Therefore $$\widehat QAJx=\widehat Q(JMx+Dx)=\widehat QDx.$$ Since $J$ is isometric on $\operatorname{ran}P$, taking the supremum proves [\[eq:out\]](#eq:out){reference-type="eqref" reference="eq:out"}. Applying the same argument to $A^*$ and $M^*$ gives $\lVert\widehat QA^*\widehat P\rVert\leq\lVert D^\sharp P\rVert$. Taking adjoints proves [\[eq:in\]](#eq:in){reference-type="eqref" reference="eq:in"}. Multiplication gives the final inequality.

The adjoint defect is not a cosmetic duplication. Nonnormal dynamics can have a small right residual and a large left residual. Later Schur bounds use their product, while directional graph bounds distinguish them.

If $AJ=JM$ and $A^*J=JM^*$ on $\operatorname{ran}P$, then $\widehat P$ reduces $A$. Any contour separating the realized packet spectrum from its complement already has $\widehat P$ as its Riesz projection.

Both off-diagonal blocks vanish by Theorem [\[thm:realization\]](#thm:realization){reference-type="ref" reference="thm:realization"}.

# No coupling bound without a realization

Fix the one-dimensional source data $\mathcal E=\mathbb C$, $M=0$, and $P=I$. Let $A=\operatorname{diag}(0,1)$ on $\mathbb C^2$. There are isometries $J_0,J_1:\mathcal E\to\mathbb C^2$ realizing the identical source packet for which $$\lVert(I-J_0J_0^*)AJ_0J_0^*\rVert=0,qquad
 \lVert(I-J_1J_1^*)AJ_1J_1^*\rVert=\frac12.$$

Take $J_0(1)=e_1$ and $J_1(1)=2^{-1/2}(e_1+e_2)$. The first range is an eigenspace. In the orthonormal basis $2^{-1/2}(e_1+e_2),2^{-1/2}(e_1-e_2)$, the off-diagonal entry of $A$ has absolute value $1/2$.

Thus packet positivity, overlap floors, and source-space rank do not bound a transfer-space coupling. The map $J$ and its dynamical defects are genuine physical inputs, not coordinate notation.

# Near-isometries and polar repair

Suppose a proposed map $J_0$ obeys $$\lVert J_0^*J_0-I\rVert\leq\eta<1.$$ Then $G=J_0^*J_0$ is positive invertible and $J=J_0G^{-1/2}$ is an isometry. Functional calculus gives $$\lVert G^{-1/2}\rVert\leq(1-\eta)^{-1/2},\qquad
 \lVert G^{-1/2}-I\rVert\leq(1-\eta)^{-1/2}-1.$$ However, $$\begin{aligned}
 AJ-JM={}&(AJ_0-J_0M)G^{-1/2}\\
 &+J_0\bigl(MG^{-1/2}-G^{-1/2}M\bigr).\end{aligned}$$ The second term vanishes only when the source dynamics commutes with the Gram correction. A numerical orthogonalization that omits this commutator does not certify the physical intertwining defect [@StewartSun1990].

# Gauge covariance and a canonicity test

An ambient realization should depend on the source subspace, not on a chosen basis. The following elementary identity is useful in implementation.

Let $U$ be unitary on $\mathcal E$ and transform the source data by $$M'=UMU^*,\qquad P'=UPU^*,\qquad J'=JU^*.$$ Then the realized packet and directed defect norms are unchanged: $$J'P'J'^*=JPJ^*,$$ and $$\lVert(AJ'-J'M')P'\rVert=\lVert(AJ-JM)P\rVert,$$ with the analogous identity for the adjoint defect.

The first identity follows by cancellation of adjacent $U^*U$ factors. Also $$(AJ'-J'M')P'=(AJ-JM)PU^*,$$ and right multiplication by a unitary preserves the norm. Apply the same calculation to $A^*$ and $M^*$.

This gives a direct falsifier for a proposed physical construction: if a rotation of the reset frame changes the realized transfer packet, the map is frame-fitted rather than packet-canonical. Three further tests remain independent: $J$ must not use target zero data; its normalization must remain controlled as the dimensions grow; and its common-coordinate transports must be compatible with refinement. Gauge covariance is necessary but not sufficient for those stronger requirements.

# Finite audit and physical frontier

The companion audit samples 512 random triples $(A,M,J)$ with dimensions $10$, $7$, and packet rank $3$. It evaluates both sides of [\[eq:out\]](#eq:out){reference-type="eqref" reference="eq:out"}--[\[eq:in\]](#eq:in){reference-type="eqref" reference="eq:in"}; no failure occurs. This checks the implementation, not the prime-dynamics hypotheses.

For the archived route, the new subinterface X consists of:

1.  a target-independent ambient map $J_j$ from each reset-memory space to the transfer/determinant space;

2.  a normalization and polar repair with controlled commutator;

3.  primal and adjoint packet-defect bounds;

4.  compatibility of these maps across the moving cloud schedule.

Only after X is supplied can RH-161's contour estimate be applied to the physical reset packet. RH-162 proves the type-correct implication and the impossibility of deleting X from this architecture. It does not construct X, a Riesz cloud, a canonical determinant, a scattering completion, a self-adjoint operator, a zeta identity, or the Riemann Hypothesis.
