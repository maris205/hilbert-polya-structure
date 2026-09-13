---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-167-finite-mesh-resolvent-envelope"
canonical_tex: "zeta_mvp0/papers/RH-167-finite-mesh-resolvent-envelope/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-167-finite-mesh-resolvent-envelope/main.pdf"
source_sha256: "4a476f220b182207bf645b934253cc245c46b7de0281ea7ca7085978b8718909"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Mesh Certification of Continuous Resolvent Contours A Banach-Lemma Envelope for Nonnormal Packet Blocks

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-167-finite-mesh-resolvent-envelope>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-167-finite-mesh-resolvent-envelope/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-167-finite-mesh-resolvent-envelope/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-167-finite-mesh-resolvent-envelope/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-167-finite-mesh-resolvent-envelope/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Physical interface R requires a supremum of a nonnormal resolvent on a continuous contour. A finite eigenvalue plot or a list of sampled singular values does not certify that supremum. We prove a finite covering theorem. If every $z$ on the contour lies within $h_k$ of some sample $z_k$, and $$\lVert(z_k-T)^{-1}\rVert\le m_k,\qquad h_km_k<1,$$ then on the associated cell $$\lVert(z-T)^{-1}\rVert\le\frac{m_k}{1-h_km_k}.$$ For $n$ equally spaced points on a circle of radius $s$, the exact covering radius is $2s\sin(\pi/(2n))$. Applying the theorem to both diagonal blocks turns the Schur feedback gate into a finite-input certificate. A dense-grid audit of 256 nonnormal matrices has no envelope failure. Its floating-point sample inverses are diagnostics; validated physical inverse bounds remain an open input.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Finite-Mesh Certification of Continuous Resolvent Contours\
  A Banach-Lemma Envelope for Nonnormal Packet Blocks
```

## Markdown 正文

# A local resolvent covering lemma

Let $T$ be a bounded operator and suppose $z_k\in\rho(T)$. For any $z$, $$z-T=\bigl(I+(z-z_k)(z_k-T)^{-1}\bigr)(z_k-T).$$

[\[thm:mesh\]]{#thm:mesh label="thm:mesh"} Let $\Gamma$ be covered by sets $U_k$ such that $$\sup_{z\in U_k\cap\Gamma}|z-z_k|\le h_k,
 \qquad\lVert(z_k-T)^{-1}\rVert\le m_k.$$ If $h_km_k<1$ for every cell, then $\Gamma\subset\rho(T)$ and $$\sup_{z\in\Gamma}\lVert(z-T)^{-1}\rVert
 \le\max_k\frac{m_k}{1-h_km_k}.$$

For $z\in U_k\cap\Gamma$, the perturbation $(z-z_k)(z_k-T)^{-1}$ has norm at most $h_km_k<1$. The Neumann series inverts the first factor and bounds its inverse by $(1-h_km_k)^{-1}$. Multiplication by the sample resolvent proves the local bound. Taking the maximum over the finite cover proves the theorem [@Kato1995].

The condition is local. Adaptive refinement need only split cells where $h_km_k$ is large; one ill-conditioned sample need not force uniform oversampling elsewhere.

# Exact covering radius for a circle

[\[prop:circle\]]{#prop:circle label="prop:circle"} For $n\ge3$ equally spaced nodes on $|z-\mu|=s$, every contour point is within $$h_n=2s\sin\frac{\pi}{2n}$$ of its nearest node. This radius is sharp.

The farthest point in each arc is its midpoint. Its angular distance from either endpoint is $\pi/n$, and the corresponding chord length is $2s\sin(\pi/(2n))$.

Thus a uniform sample bound $m$ certifies the circle whenever $2sm\sin(\pi/(2n))<1$. Solving this inequality supplies a deterministic minimum mesh density once $m$ is known.

The sufficient integer condition $$n>\pi sm$$ guarantees $h_nm<1$.

Use $\sin x\le x$ to obtain $h_nm\le2sm\,\pi/(2n)=\pi sm/n<1$.

The estimate is conservative but useful before sampling begins. It shows that mesh complexity grows linearly with the contour radius and the expected resolvent amplification. Near a pseudospectral spike, adaptive local cells can be much cheaper than enforcing the worst $m$ around the entire curve.

# Finite-input Schur certificate

Apply Theorem [\[thm:mesh\]](#thm:mesh){reference-type="ref" reference="thm:mesh"} separately to the packet and complementary blocks. Let sample inverse bounds be $m_{P,k},m_{Q,k}$ and covering radii $h_k$. Define $$a=\max_k\frac{m_{P,k}}{1-h_km_{P,k}},\qquad
 d=\max_k\frac{m_{Q,k}}{1-h_km_{Q,k}}.$$

If all mesh products are below one and $$adbc<1,$$ then the full off-diagonal homotopy preserves the packet rank inside $\Gamma$.

The mesh theorem supplies continuous diagonal resolvent bounds. The two-sided Schur theorem then applies [@WangRH163].

The directional graph formulas of RH-166 can use the same $a,d$. Therefore the entire finite rank-and-graph decision requires only certified sample inverses, covering radii, and two residual norms.

# Resolvent disks and adaptive stopping

The local theorem gives an intrinsic certified neighborhood around each sample.

Fix $0<\theta<1$. A sample bound $m_k$ certifies every point in $$\mathbb D_k=\{z:|z-z_k|\le\theta/m_k\}$$ with the uniform local estimate $$\lVert(z-T)^{-1}\rVert\le\frac{m_k}{1-\theta}.$$ If $\Gamma\subset\bigcup_k\mathbb D_k$, these disks form a complete continuous contour certificate.

Insert $h_k=\theta/m_k$ into Theorem [\[thm:mesh\]](#thm:mesh){reference-type="ref" reference="thm:mesh"}; then $h_km_k=\theta$.

This yields a rigorous adaptive stopping rule: add samples only on uncovered arcs, recompute their validated inverse bounds, and stop exactly when the union of certified disks covers the curve. Regions of large resolvent norm automatically receive small disks and finer sampling. Failure to terminate at a fixed precision is a conditioning diagnostic, not evidence that the contour intersects the spectrum.

# What a sample inverse certificate requires

A numerical inverse $R_k$ is not itself an upper bound. A standard a-posteriori route is to compute the defect $$E_k=I-R_k(z_k-T).$$ If $\lVert E_k\rVert<1$, then $$\lVert(z_k-T)^{-1}\rVert\le
 \frac{\lVert R_k\rVert}{1-\lVert E_k\rVert}.$$ For a physical proof, both norms must be outwardly enclosed and the operator $T$ must be related to its assembled matrix by a certified ball. RH-167 does not silently promote floating singular values to such bounds.

# Dense-grid audit and route consequence

The companion audit draws 256 upper-triangular nonnormal matrices, samples a circle at 20--64 nodes, and evaluates the envelope. For every accepted mesh it compares the result with 2048 dense contour evaluations. No dense value exceeds the theorem bound. This exercises strongly nonconstant resolvents but remains a floating-point regression test.

RH-167 removes the uncountable contour quantifier from interface R. The next wall is validation: transport nominal sample inverses and couplings through an operator ball without losing the mesh denominator. No physical sample bound, uniform all-level margin, Gate A, or downstream Hilbert--Polya claim is made.
