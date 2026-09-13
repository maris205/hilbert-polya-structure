---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-170-rank-growing-riesz-shell-atlas"
canonical_tex: "zeta_mvp0/papers/RH-170-rank-growing-riesz-shell-atlas/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-170-rank-growing-riesz-shell-atlas/main.pdf"
source_sha256: "4c4d5d1fedfd9fc39db6be2c8948063c9284e442cef62ba7f9e8ad2d831f877c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Shell Atlas for Rank-Growing Riesz Clouds The Global Norm Obstruction and a Coherent Replacement

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-170-rank-growing-riesz-shell-atlas>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-170-rank-growing-riesz-shell-atlas/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-170-rank-growing-riesz-shell-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-170-rank-growing-riesz-shell-atlas/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-170-rank-growing-riesz-shell-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-169 proves norm convergence for a summably transported fixed-rank Riesz packet. The determinant cloud of RH-80 has increasing degree, so its full Riesz projection changes rank. We prove the sharp obstruction: finite-rank idempotents $P,Q$ of different ranks satisfy $$\lVert P-Q\rVert\ge1.$$ Hence a rank-growing cloud cannot converge in operator norm, regardless of how accurately individual eigenvalues stabilize. We replace the impossible target by a shell atlas. Decompose each finite cloud into disjoint Riesz shells. If every fixed shell has a common-coordinate transport with summable projector defects, that shell converges in norm. Limiting shells remain mutually annihilating, and every finite partial sum is an idempotent of the expected rank. No bounded infinite sum is asserted. This is both a negative global result and a positive shellwise closure theorem; physical shell identification and summability remain open.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  A Shell Atlas for Rank-Growing Riesz Clouds\
  The Global Norm Obstruction and a Coherent Replacement
```

## Markdown 正文

# The rank-change obstruction

The result applies to nonorthogonal Riesz projections as well as orthogonal ones.

[\[thm:floor\]]{#thm:floor label="thm:floor"} Let $P,Q$ be bounded finite-rank idempotents on one Banach space. If $\operatorname{rank}P\ne\operatorname{rank}Q$, then $$\boxed{\ \lVert P-Q\rVert\ge1.\ }$$

Suppose $\lVert P-Q\rVert<1$. If $x\in\operatorname{ran}P$ and $Qx=0$, then $$\lVert x\rVert=\lVert Px-Qx\rVert\le\lVert P-Q\rVert\lVert x\rVert,$$ so $x=0$. Thus $Q|_{\operatorname{ran}P}$ is injective and $\operatorname{rank}P\le\operatorname{rank}Q$. Interchanging $P,Q$ gives the reverse inequality. Hence the ranks are equal, a contradiction.

If finite-rank cloud projections $\Pi_j$ change rank infinitely often, then $(\Pi_j)$ is not operator-norm Cauchy and cannot converge in operator norm.

This obstruction is structural, not a weakness of the RH-169 estimate. A request for global norm convergence of the full moving projection would make physical interface R impossible by definition.

# Disjoint Riesz shells

At scale $j$, let $\Gamma_{j,1},\ldots,\Gamma_{j,N_j}$ be pairwise disjoint contours and let $\Pi_{j,m}$ be their Riesz projections. Standard holomorphic functional calculus gives $$\Pi_{j,m}\Pi_{j,n}=0=\Pi_{j,n}\Pi_{j,m}\quad(m\ne n),$$ and the finite cloud projection is $$\Pi_j^{\le N_j}=\sum_{m=1}^{N_j}\Pi_{j,m}.$$ The shell index may represent one conjugate pair or another fixed finite packet; its definition must be target-independent.

# Shellwise convergence theorem

Embed the scale operators into a common space as in RH-169. For each fixed $m$, assume the shell exists for all $j\ge j(m)$, its rank is constant, and there are step bounds $$\lVert\Pi_{j+1,m}-\Pi_{j,m}\rVert\le\beta_{j,m},
 \qquad
 \sum_{j\ge j(m)}\beta_{j,m}<\infty.$$

[\[thm:shell\]]{#thm:shell label="thm:shell"} For every fixed $m$, $\Pi_{j,m}$ converges in norm to a finite-rank idempotent $\Pi_{\infty,m}$ of the same rank. Distinct limits annihilate one another. Consequently, for every finite $M$, $$\Pi_\infty^{\le M}:=\sum_{m=1}^{M}\Pi_{\infty,m}$$ is an idempotent and $$\operatorname{rank}\Pi_\infty^{\le M}
 =\sum_{m=1}^{M}\operatorname{rank}\Pi_{\infty,m}.$$

For fixed $m$, summability makes the sequence norm-Cauchy, so the RH-169 argument gives an idempotent limit of stable rank [@WangRH169]. For $m\ne n$, choose scales where both shells exist. Since their products are zero, norm continuity of multiplication gives $\Pi_{\infty,m}\Pi_{\infty,n}=0$ in both orders. The finite sum is therefore idempotent, and its range is the algebraic direct sum of the shell ranges, giving rank additivity.

The theorem does not claim that $\sum_{m\ge1}\Pi_{\infty,m}$ converges strongly or in norm. Such a claim would require uniform unconditional-decomposition bounds and is unnecessary for identifying every finite cloud factor.

# Determinant interpretation

At each finite scale, disjoint reducing shells give an exact product of finite-dimensional cloud determinants. The shell atlas permits one to ask for coefficient stabilization of every fixed partial product while the degree grows. This is compatible with RH-80's moving factor [@WangRH80]. It does not by itself prove the cloud coefficient ledger Q or the complementary Schatten limit U.

Fix $M$. Suppose, after the shell transports of Theorem [\[thm:shell\]](#thm:shell){reference-type="ref" reference="thm:shell"}, the finite-dimensional restrictions $T_{j,m}=A_j|_{\operatorname{ran}\Pi_{j,m}}$ converge in operator norm to $T_{\infty,m}$ for every $m\le M$. Then $$C_j^{\le M}(w)=\prod_{m=1}^{M}\det(I-wT_{j,m})$$ converges locally uniformly in $w$ to $$C_\infty^{\le M}(w)=
 \prod_{m=1}^{M}\det(I-wT_{\infty,m}).$$

Each shell has fixed finite dimension. Matrix entries converge after the chosen transports, so the determinant polynomial converges coefficientwise and hence locally uniformly. A finite product preserves local uniform convergence.

The proposition is deliberately finite in $M$. Passing $M\to\infty$ would need coefficient tails, normalization, and trace-ideal control belonging to interfaces Q and U. The shell atlas prevents a false projection limit but does not erase those later proof debts.

# Shell labels are an additional compatibility datum

Disjoint contours identify a set of Riesz projections, but shellwise limits also require stable labels. This is not automatic from the full cloud.

There is a constant rank-two cloud projection with two rank-one shell decompositions for which each displayed shell alternates and has no limit.

On $\mathbb C^2$, let $E_1,E_2$ be the coordinate rank-one projections. At even scales label $(\Pi_{j,1},\Pi_{j,2})=(E_1,E_2)$ and at odd scales label them $(E_2,E_1)$. The full cloud sum is always $I$, but neither labeled sequence converges.

A physical shell atlas must therefore derive its labels from a canonical quantity---for example contour homology, a coefficient order, or an orientation rule---rather than nearest-neighbor fitting alone. Establishing that the labels match the intended deterministic pole ledger belongs to Q; R supplies the coherent Riesz carriers once the labels are specified.

# Audit and route consequence

The audit uses 64-dimensional diagonal projections with rank increasing by one. Every one of the 63 consecutive global distances is exactly one, confirming Theorem [\[thm:floor\]](#thm:floor){reference-type="ref" reference="thm:floor"}. Eight synthetic fixed shells are given geometrically summable transport ledgers and pass their finite tail checks. These are algebraic regression examples, not physical evidence.

RH-170 changes the all-level R specification: require same-rank lifting and summable transport for every fixed shell, not norm convergence of the full rank-growing cloud projection. Physical shell contours, realization maps, and summability remain open. Gate A and all Hilbert--Polya conclusions are unchanged.
