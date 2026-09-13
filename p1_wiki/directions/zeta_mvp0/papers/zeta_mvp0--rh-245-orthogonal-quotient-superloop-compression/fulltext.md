---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-245-orthogonal-quotient-superloop-compression"
canonical_tex: "zeta_mvp0/papers/RH-245-orthogonal-quotient-superloop-compression/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-245-orthogonal-quotient-superloop-compression/main.pdf"
source_sha256: "220af4880381244322808a8ab9cfbfd09c3b2e8006c421f0f7f64ace647fce18"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Orthogonal-Quotient Superloop Compression

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-245-orthogonal-quotient-superloop-compression>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-245-orthogonal-quotient-superloop-compression/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-245-orthogonal-quotient-superloop-compression/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-245-orthogonal-quotient-superloop-compression/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-245-orthogonal-quotient-superloop-compression/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Cloud-extracted traces were represented in RH-242 as a graded difference of physical loops and finite atomic counterloops. We give an exact cancellation-preserving grouping. The selected generalized root space is invariant, so its norm-one orthogonal quotient compression has power traces equal to the cloud-extracted traces. This avoids estimating the badly conditioned Riesz projection. A finite ordered-Schur audit verifies the identity on 17 tractable archived endpoints and shows that one-step quotient contraction still fails, motivating a block-power criterion.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Orthogonal-Quotient Superloop Compression'
```

## Markdown 正文

# Invariant root space and orthogonal quotient

Let $A\in\mathcal S_{2}(H)$ and let $\mathcal S$ be a finite algebraic multiset of isolated nonzero eigenvalues of $A$. Let $E$ be the sum of their full generalized root spaces. Then $E$ is finite dimensional and $A$-invariant. Write $\Pi$ for the orthogonal projection onto $E$, $Q=I-\Pi$, and $$\label{eq:C}
 C=QAQ\big|_{E^\perp}:E^\perp\longrightarrow E^\perp.$$ The complement $E^\perp$ need not be $A$-invariant: $C$ is the orthogonal realization of the quotient operator, not a reducing restriction.

[\[thm:quotient\]]{#thm:quotient label="thm:quotient"} For every integer $n\ge2$, $$\label{eq:identity}
 \operatorname{Tr}A^n-\sum_{s\in\mathcal S}s^n=\operatorname{Tr}C^n.$$ The projection used in [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"} satisfies $\|\Pi\|=1$ whenever $E\ne\{0\}$; no norm bound for the oblique Riesz projection is required.

Relative to the orthogonal decomposition $H=E\oplus E^\perp$, invariance of $E$ gives $$A=\begin{pmatrix}A_E&X\\0&C\end{pmatrix}.$$ Every power has the same block upper-triangular form and diagonal blocks $A_E^n$ and $C^n$. Because $A\in\mathcal S_{2}$, these powers are trace class for $n\ge2$. Hence $\operatorname{Tr}A^n=\operatorname{tr}A_E^n+\operatorname{Tr}C^n$. The finite-dimensional trace of $A_E^n$ is the algebraic power sum $\sum_{s\in\mathcal S}s^n$, including multiplicity, which proves [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}. The orthogonal projection norm is elementary.

This is precisely the RH-242 superloop cancellation [@WangRH242] performed before taking absolute values. In an ordered Schur basis, closed block walks cannot contain the one-way coupling $X$: a walk that leaves the quotient block cannot return. The selected-block loops cancel the atomic counterloops, leaving only quotient loops.

[\[prop:kernel\]]{#prop:kernel label="prop:kernel"} If $H=L^2(X,\mu)$ and $A$ has a Hilbert--Schmidt kernel, then $B=QAQ$ has a Hilbert--Schmidt kernel $b$. For every $n\ge2$, $$\operatorname{Tr}C^n=\operatorname{Tr}B^n
 =\int_{X^n}b(x_0,x_1)b(x_1,x_2)\cdots
 b(x_{n-1},x_0)\,d\mu^n.$$ Thus the grouped representation remains a genuine signed or complex periodic-loop formula.

The Hilbert--Schmidt ideal is stable under bounded left and right multiplication, so $B$ is Hilbert--Schmidt and vanishes on $E$ in the orthogonal block form. The standard trace formula for products of Hilbert--Schmidt kernels gives the cyclic integral; its nonzero block is $C^n$.

# Why this differs from a Riesz estimate

RH-232 found enormous Euclidean Riesz projection norms in the moving cloud [@WangRH232]. Orthogonal quotient compression removes that norm from the fixed-operator trace identity, although it does not prove that the spaces $E_\sigma$ vary uniformly.

[\[ex:model\]]{#ex:model label="ex:model"} For distinct $\lambda,\mu$ let $$A_M=\begin{pmatrix}\lambda&M\\0&\mu\end{pmatrix},
 \qquad E=\operatorname{span}\{e_1\}.$$ The Riesz projection onto $E$ is $$P_\lambda=\begin{pmatrix}1&M/(\lambda-\mu)\\0&0\end{pmatrix},
 \qquad
 \|P_\lambda\|=sqrt{1+|M/(\lambda-\mu)|^2},$$ which diverges with $|M|$. Yet $\Pi=\operatorname{diag}(1,0)$, $C=[\mu]$, and $$\operatorname{tr}A_M^n-\lambda^n=\mu^n$$ for every $n$, independently of $M$. Orthogonal grouping deletes purely cross-block nonnormal mass, but says nothing about nonnormality internal to $C$.

# Finite ordered-Schur audit

We reconstruct every RH-222 endpoint of dimension at most 512 [@WangRH222], Hardy-scale the matrix, and order its complex Schur form at the archived radial gap. The leading block contains Perron, parity, and the selected cloud; the trailing block is $C$. We compare its power traces with the projection-free RH-236 archive [@WangRH236].

  quantity                                               value
  ------------------------------------- ----------------------
  audited endpoints                                         17
  selected block dimensions                              6--25
  rank mismatches                                            0
  maximum Schur trace-partition error     $3.99\times10^{-15}$
  maximum RH-236 residual difference      $6.31\times10^{-12}$
  quotient Frobenius square                        5.07--60.09
  old-budget improvement factor                     1.20--1.62
  quotient one-step norm                          1.277--2.346
  first contractive power depth                           3--7
  maximum $\|C^{12}\|$                    $1.370\times10^{-5}$

The exact theorem explains why cross-block mass is irrelevant, but the finite numbers also prevent an overclaim: every audited one-step quotient norm exceeds one, and the Frobenius budget improves only modestly. Deep power contraction is striking finite evidence, not a uniform theorem.

# Boundary and next condition

Theorem [\[thm:quotient\]](#thm:quotient){reference-type="ref" reference="thm:quotient"} is exact at each fixed noise once the algebraic selected subspace exists. It does not provide a noise-uniform method to identify that subspace, a uniform kernel bound, or a uniform contractive power. Only 17 of 32 archived endpoints were densely decomposed, and no interval certification was attempted. The next obligation is therefore an explicit $m$-block trace-envelope theorem and a uniform certificate for its hypotheses. The anchored selector obstruction of RH-244 remains separate.

Gate A remains open and Gates B--E are untouched. No Hilbert--Pólya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is claimed.
