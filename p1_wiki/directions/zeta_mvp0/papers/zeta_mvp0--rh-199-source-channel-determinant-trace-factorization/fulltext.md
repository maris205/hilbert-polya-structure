---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-199-source-channel-determinant-trace-factorization"
canonical_tex: "zeta_mvp0/papers/RH-199-source-channel-determinant-trace-factorization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-199-source-channel-determinant-trace-factorization/main.pdf"
source_sha256: "70e38238a62793209ebed0adae778bb0fe92c11663adace5a302b08b445702c8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Source-Channel Determinant and Trace Factorization Separating Spectral Newton Sums from Residue-Weighted Physical Moments

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-199-source-channel-determinant-trace-factorization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-199-source-channel-determinant-trace-factorization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-199-source-channel-determinant-trace-factorization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-199-source-channel-determinant-trace-factorization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-199-source-channel-determinant-trace-factorization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The canonical source-channel packet carries two related but different data sets. Its spectral determinant and Newton traces are $$D_E(z)=\det(zI-K)=\prod_j(z-\lambda_j),
   \qquad
   \operatorname{tr}K^q=\sum_j\lambda_j^q.$$ The physical source-observation moments retain the channel residues: $$h_q=c^*K^qb=\sum_jr_j\lambda_j^q.$$ Conflating these ledgers would erase the input-output weights needed by any later trace formula.

  This paper gives an exact determinant encoding of the weighted transfer: $$\frac{\det(zI-(K+bc^*))}{\det(zI-K)}
   =1-c^*(zI-K)^{-1}b.$$ Thus one finite pair of characteristic determinants contains both the pole set and the residue-weighted response. A 240-case complex nonnormal audit verifies the determinant lemma, modal weighted moments, and Newton traces with zero failures.

  For the physical length-four windows, the temporal determinant and traces converge to the exact quartet ledger despite canonical frame norm products as large as $950$. At the latest starts the relative determinant error is below $10^{-4}$ and the maximum relative trace error through power eight is below $8\times10^{-4}$.

  These are finite physical channel identities. They do not provide von Mangoldt weights, a prime-power orbit formula, a zeta determinant, or a Hilbert--Pólya operator.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Source-Channel Determinant and Trace Factorization\
  Separating Spectral Newton Sums from Residue-Weighted Physical Moments
```

## Markdown 正文

# Two ledgers that must not be conflated

Let $K\in\mathbb C^{r\times r}$ be the exact canonical packet of RH-196, and let $b,c\in\mathbb C^r$ be source and observation coordinates. In a residue-labeled simple-mode basis one may take $$\label{eq:modal-data}
 K=\operatorname{diag}(\lambda_1,\ldots,\lambda_r),
 \qquad b=(1,\ldots,1)^T,
 \qquad \overline{c_j}=r_j.$$

The spectral ledger ignores source and observation: $$\label{eq:spectral-ledger}
 D_E(z)=\det(zI-K),
 \qquad s_q=\operatorname{tr}K^q.$$ The physical transfer ledger is $$\label{eq:transfer-ledger}
 g_E(z)=c^*(zI-K)^{-1}b,
 \qquad h_q=c^*K^qb.$$ Both are similarity invariant if $b,c$ transform with the state coordinates, but they answer different questions.

# Spectral determinant and Newton traces

[\[prop:determinant\]]{#prop:determinant label="prop:determinant"} For the selected simple modes, $$\label{eq:determinant}
 D_E(z)=\prod_{j=1}^r(z-\lambda_j).$$ Its logarithmic derivative is $$\label{eq:log-derivative}
 \frac{D_E'(z)}{D_E(z)}
 =\operatorname{tr}(zI-K)^{-1}
 =\sum_{j=1}^r\frac{1}{z-\lambda_j}.$$

The logarithmic derivative assigns unit multiplicity to each channel pole. It does not recover the physical residues $r_j$ unless all happen to equal one.

For $|z|>\rho(K)$, $$\label{eq:trace-expansion}
 \operatorname{tr}(zI-K)^{-1}
 =\sum_{q\ge0}\frac{\operatorname{tr}K^q}{z^{q+1}}.$$ Thus the Newton sums are the unweighted resolvent coefficients.

# Residue-weighted moments

The source-observation transfer has expansion $$\label{eq:weighted-expansion}
 g_E(z)=\sum_{q\ge0}\frac{h_q}{z^{q+1}},
 \qquad h_q=c^*K^qb.$$

[\[thm:moments\]]{#thm:moments label="thm:moments"} In the simple residue-labeled basis, $$\label{eq:modal-moments}
 \boxed{h_q=\sum_{j=1}^r r_j\lambda_j^q.}$$

Insert [\[eq:modal-data\]](#eq:modal-data){reference-type="eqref" reference="eq:modal-data"} into $c^*K^qb$.

The distinction $s_q$ versus $h_q$ is the finite prototype of a later trace problem. A prime-power trace formula would require specific arithmetic weights analogous to von Mangoldt coefficients. The physical residues in this paper are not identified with those weights.

# A determinant ratio for the transfer

The matrix determinant lemma gives the exact bridge.

[\[thm:feedback\]]{#thm:feedback label="thm:feedback"} For $z\notin\sigma(K)$, $$\label{eq:feedback}
 \boxed{
 \frac{\det(zI-(K+bc^*))}{\det(zI-K)}
 =1-c^*(zI-K)^{-1}b.
 }$$

Factor $$zI-(K+bc^*)=(zI-K)
 \left[I-(zI-K)^{-1}bc^*\right]$$ and use $\det(I-uv^*)=1-v^*u$.

Consequently the scalar transfer is encoded by a pair of finite spectral determinants: $$\label{eq:transfer-pair}
 g_E(z)=1-\frac{D_{E,\rm fb}(z)}{D_E(z)}.$$ Zeros of the numerator ratio reflect the feedback realization; poles are the uncanceled channel eigenvalues. This is a standard system-theoretic identity, here attached to the physical source-observation packet [@Kailath1980].

# Gauge covariance

Under an invertible state gauge $$\label{eq:gauge}
 K'=G^{-1}KG,
 \qquad b'=G^{-1}b,
 \qquad c'=G^*c,$$ one has $$\label{eq:gauge-invariance}
 D_E'=D_E,
 \quad \operatorname{tr}(K')^q=\operatorname{tr}K^q,
 \quad (c')^*(zI-K')^{-1}b'=c^*(zI-K)^{-1}b.$$ The determinant ratio is therefore invariant. This explains why large balanced frame norms need not spoil the finite determinant/trace ledger: coordinate amplification cancels in exact similarity invariants.

# Complex identity audit

The implementation uses dimensions 2--9 and thirty complex random systems per dimension, for 240 cases. It verifies:

1.  the rank-one determinant ratio at an off-spectrum point;

2.  equality of direct moments $c^*K^qb$ and modal residue sums through order seven;

3.  equality of power traces and modal Newton sums through power eight.

All cases pass the $10^{-8}$ tolerance. The modal audit uses independently computed left/right eigenvectors and therefore tests residue normalization as well as the determinant lemma.

# Physical temporal transport

RH-194 stores the temporal compressed matrix and its matched physical quartet ledger for every accepted window [@WangRH194]. Across all twelve windows, the maximum relative determinant error is $8.56\times10^{-4}$ and the maximum relative power-trace error through order eight is $4.12\times10^{-3}$.

At the latest starts:

  side      relative determinant error   maximum trace error
  ------- ---------------------------- ---------------------
  left             $8.91\times10^{-5}$   $7.66\times10^{-4}$
  right            $4.47\times10^{-5}$   $3.97\times10^{-4}$

The determinant error is not monotone at every start, but both late values are below $10^{-4}$. The power-trace errors exhibit the same overall decay as the subspace gaps in RH-198.

# What the finite determinant accomplishes

The result supplies a strict finite object: $$(D_E,D_{E,\rm fb})
 \quad\leftrightarrow\quad
 (\lambda_j,r_j)_{j=1}^4.$$ It retains both spectral locations and source-observation weights, is independent of balanced gauge, and is approximated by the temporal packet at the audited anchor.

This is precisely the kind of bookkeeping needed before any infinite spectral determinant can be proposed. It also prevents a common overstatement: matching eigenvalues or unweighted traces is not enough to derive an arithmetic explicit formula.

# Boundaries and next step

The determinant is a degree-four polynomial per side. It is not an entire function with zeta growth, has no $T\log T$ zero count, and contains no demonstrated prime-power weights. The residues are physical transfer weights, not von Mangoldt coefficients.

The next problem is selection: why does the finest audited model produce a four-mode nonreal edge packet while the predeclared length-three attempts at coarser scales fail? RH-200 studies the conjugate-pair parity and edge-gap geometry behind the quartet. Cross-scale transport remains the central open leaf of Gate A.
