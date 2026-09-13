---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-234-projection-free-det2-spectral-factor"
canonical_tex: "zeta_mvp0/papers/RH-234-projection-free-det2-spectral-factor/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-234-projection-free-det2-spectral-factor/main.pdf"
source_sha256: "a98576e6897417ace227906d41564beb85e1803ee705e38ef28ac6c06355e2ca"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Projection-Free Spectral Factorization of the Regularized Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-234-projection-free-det2-spectral-factor>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-234-projection-free-det2-spectral-factor/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-234-projection-free-det2-spectral-factor/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-234-projection-free-det2-spectral-factor/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-234-projection-free-det2-spectral-factor/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The direct moving-cloud Riesz projectors of RH-232 are severely ill-conditioned, but the regularized determinant depends on eigenvalues, not eigenvectors. Let $A\in\mathcal S_2$ have nonzero eigenvalues $(\lambda_j)$ with algebraic multiplicity. For any finite submultiset $C$, the canonical product splits exactly: $$\det_2(I-zA)
   =\prod_{\lambda\in C}(1-z\lambda)e^{z\lambda}
    \prod_{\lambda_j\notin C}(1-z\lambda_j)e^{z\lambda_j}.$$ Both factors are entire and no projector norm appears.

  We apply this identity to the selected and resolved omitted roots of every RH-222 endpoint. On a 192-point unit-disk grid, all 6,144 factorization cases pass with maximum absolute discrepancy $1.83\times10^{-15}$, despite the inherited projector norm $2.26\times10^{12}$. This establishes a projection-free finite cloud factor. It does not prove that the selected multisets form the correct small-noise divisor or that the complementary products have a locally uniform limit.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'Projection-Free Spectral Factorization of the Regularized Determinant'
```

## Markdown 正文

# Why the determinant can bypass the projector

For $A\in\mathcal S_2$, the two-regularized determinant is the genus-one canonical product associated with the compact spectrum [@GohbergKrein1969; @Simon2005]. Its value is similarity invariant and contains no eigenvector condition number. This distinguishes factor evaluation from invariant-subspace perturbation.

RH-80 formulated the moving factor using a reducing projection because that is the natural route to an operator complement [@WangRH80]. RH-232 and RH-233 show why the projector norm is a difficult small-noise object [@WangRH232; @WangRH233]. The present paper separates the algebraic factor from that operator realization.

# Canonical-product factorization

[\[thm:factor\]]{#thm:factor label="thm:factor"} Let $A\in\mathcal S_2(H)$ and let $(\lambda_j)$ denote its nonzero eigenvalues, with algebraic multiplicity. Let $C$ be any finite submultiset. Then $$D_A(z):=\det_2(I-zA)=C_A(z)R_A(z),$$ where $$C_A(z)=\prod_{\lambda\in C}(1-z\lambda)e^{z\lambda},
\qquad
 R_A(z)=\prod_{\lambda_j\notin C}(1-z\lambda_j)e^{z\lambda_j}.$$ Both products define entire functions. The factorization depends only on the chosen eigenvalue multiset and not on any spectral projector norm.

The eigenvalue sequence belongs to $\ell^2$ by the Weyl inequality for Hilbert--Schmidt operators. Hence the genus-one product converges locally uniformly. Removing finitely many factors preserves convergence, and reordering a normally convergent canonical product does not change its value. Multiplying the finite and complementary products recovers the full product.

[\[prop:trace\]]{#prop:trace label="prop:trace"} On the disk of convergence of the logarithmic germ, $$\log R_A(z)=-\sum_{n\ge2}\frac{z^n}{n}\tau_n,
 \qquad
 \tau_n=\sum_{\lambda_j\notin C}\lambda_j^n.$$ If $A^n$ is trace class, $\tau_n$ equals the trace of $A^n$ after subtracting the selected eigenvalue powers.

Use $\log((1-w)e^w)=-\sum_{n\ge2}w^n/n$ and interchange normally convergent sums near the origin. Lidskii's theorem identifies trace-class power traces with algebraic eigenvalue sums [@Simon2005].

Proposition [\[prop:trace\]](#prop:trace){reference-type="ref" reference="prop:trace"} identifies the replacement for a failed ideal norm estimate: directly control the complement power traces.

Assume the selected multiset contains no zero values. The zeros of $C_A$ are precisely the reciprocals $\lambda^{-1}$ for $\lambda\in C$, with their selected algebraic multiplicities, and $$\frac{C_A'(z)}{C_A(z)}
 =-\sum_{\lambda\in C}\frac{z\lambda^2}{1-z\lambda}$$ away from those zeros. Hence the projection-free quotient removes exactly the selected finite divisor and no additional finite zeros.

The exponential multiplier in each genus-one factor is nonvanishing, so its only zero is $z=\lambda^{-1}$. Differentiating $\log((1-z\lambda)e^{z\lambda})$ gives $-\lambda/(1-z\lambda)+\lambda=-z\lambda^2/(1-z\lambda)$.

This divisor statement is stronger than a grid identity. Once a finite cloud multiset has been chosen, its determinant factor and multiplicities are defined algebraically even when the corresponding invariant subspace is almost defective.

# Finite-factor stability without eigenvectors

The absence of projector norms does not make root approximation irrelevant, but it gives the appropriate conditioning scale. Let $f(w)=\log(1-w)+w$, normalized by $f(0)=0$. If paired finite multisets $C=\{\lambda_j\}_{j=1}^k$ and $\widetilde C=\{\widetilde\lambda_j\}_{j=1}^k$ satisfy $$|z\lambda_j|\le r,
 \qquad |z\widetilde\lambda_j|\le r<1
 \quad (|z|\le R),$$ then the normalized logarithms obey $$\label{eq:lipschitz}
 \left|\log C_A(z)-\log \widetilde C_A(z)\right|
 \le \frac{rR}{1-r}
       \sum_{j=1}^k|\lambda_j-\widetilde\lambda_j|.$$ Indeed $f'(w)=-w/(1-w)$ has modulus at most $r/(1-r)$ on the convex disk $|w|\le r$, and one applies the mean-value integral to every paired factor.

Estimate [\[eq:lipschitz\]](#eq:lipschitz){reference-type="eqref" reference="eq:lipschitz"} depends on root errors and distance from the reciprocal divisor, but not on left/right eigenvector angles. It therefore explains why the $10^{12}$ projector norm and the $10^{-15}$ product identity can coexist without contradiction.

# Finite resolved audit

For each endpoint, the candidate bulk multiset is split into the selected shell-complete cloud and the remaining resolved candidate roots. We evaluate all factors at 48 angles on each of the radii $0.25$, $0.5$, $0.75$, and $1$.

  Quantity                                              value
  ---------------------------------- ------------------------
  Endpoint multisets                                       32
  Grid points per endpoint                                192
  Factorization cases                                   6,144
  Maximum cloud matching error                            $0$
  Maximum product discrepancy          $1.8311\times10^{-15}$
  Inherited maximum projector norm      $2.2610\times10^{12}$

  : Projection-free finite product audit.

The computation is not a surprise algebraically; its role is architectural. It verifies that the numerical determinant factor does not inherit the Riesz conditioning catastrophe.

The audit also separates three finite errors that are sometimes conflated: the cloud-matching error, evaluation roundoff in the selected product, and evaluation roundoff in the complementary product. The first is exactly zero for the archived multisets because the same stored roots are partitioned. The quoted $1.83\times10^{-15}$ maximum is therefore an evaluation identity, not an eigenvalue-certification radius.

# Factorization and the small-noise limit

At fixed noise and fixed finite dimension, Theorem [\[thm:factor\]](#thm:factor){reference-type="ref" reference="thm:factor"} settles the algebra. Passing to $\sigma\to0$ is a different operation because both the ambient matrix and the selected cloud rank change. A valid limiting argument must establish all three of the following:

1.  local uniform control of the complementary products;

2.  compact-set stability of the selected reciprocal divisor;

3.  compatibility of the chosen finite factor with the intended deterministic normalization.

None follows from pointwise finite product multiplication. The first is translated by Proposition [\[prop:trace\]](#prop:trace){reference-type="ref" reference="prop:trace"} into an all-order trace problem; the third becomes the coefficient-anchor problem isolated later in the batch.

# Boundary and next target

Selecting a finite multiset at each positive noise is easy once its roots are listed. The hard questions are now:

1.  whether the selected multisets obey a canonical small-noise rule;

2.  whether the complementary canonical products form a normal family;

3.  whether their coefficient germ is the intended deterministic numerator rather than an over-renormalized remainder.

RH-235 shows that the divergent Hilbert--Schmidt budget does not decide the second question. RH-236 therefore computes the trace germ through order twelve. No Gate A closure or arithmetic zero identification is claimed.
