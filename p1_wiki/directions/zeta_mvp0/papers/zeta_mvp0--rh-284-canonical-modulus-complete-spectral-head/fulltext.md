---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-284-canonical-modulus-complete-spectral-head"
canonical_tex: "zeta_mvp0/papers/RH-284-canonical-modulus-complete-spectral-head/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-284-canonical-modulus-complete-spectral-head/main.pdf"
source_sha256: "484c3cd3d19380c4bac35bbe325cf0975e60389ef3124b01ef3966b44aef1641"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Canonical Modulus-Complete Heads for Projection-Free Spectral Factors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-284-canonical-modulus-complete-spectral-head>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-284-canonical-modulus-complete-spectral-head/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-284-canonical-modulus-complete-spectral-head/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-284-canonical-modulus-complete-spectral-head/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-284-canonical-modulus-complete-spectral-head/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The rank-growing tail theorem of RH-282 requires an actual noisy spectral head, not a fitted root list. For any Hilbert--Schmidt operator and threshold $q>0$, we define the head to contain every algebraic eigenvalue of modulus strictly larger than $q$. The head is finite, conjugation complete for real operators, and has cardinality at most the squared spectral mass divided by $q^2$. It is the unique smallest spectral submultiset whose complement has spectral radius at most $q$. The strict threshold convention also resolves ties. Its genus-one product is an exact finite factor of $\det_2$, independent of eigenvector conditioning. Canonicality is relative to $q$ and does not identify the selected roots with the deterministic monodromy shell.
author:
- Bin Wang
date: July 2026
title: 'Canonical Modulus-Complete Heads for Projection-Free Spectral Factors'
```

## Markdown 正文

# Definition

Let $A\in\mathcal S_2(H)$ and let $(\mu_j)$ be its nonzero eigenvalues with algebraic multiplicity. For $q>0$ set $$H_q(A)=\{\mu_j:|\mu_j|>q\},\qquad
 T_q(A)=\{\mu_j:|\mu_j|\le q\}.$$ The equality case belongs to the tail. This strict convention is part of the definition.

# Minimal head theorem

[\[thm:head\]]{#thm:head label="thm:head"} Write $M=\sum_j|\mu_j|^2$. Then $H_q(A)$ is finite and $$\#H_q(A)\le M/q^2\le\|A\|_2^2/q^2.$$ If a finite spectral submultiset $F$ has the property that every eigenvalue outside $F$ has modulus at most $q$, then $H_q(A)\subseteq F$. Thus $H_q(A)$ is the unique smallest admissible head.

Every member of $H_q$ contributes more than $q^2$ to the convergent squared sum, proving finiteness and the count. If $F$ omitted an eigenvalue with modulus greater than $q$, its complement would violate the radius condition. Hence every admissible $F$ contains $H_q$.

If $A$ commutes with a real conjugation, then $H_q(A)$ is closed under complex conjugation, with equal algebraic multiplicities. Its finite canonical product has real Taylor coefficients.

The algebraic spectrum of a real operator is conjugation invariant, and modulus is unchanged by conjugation.

# Exact determinant split

The genus-one products $$D_{H,q}(z)=\prod_{\mu\in H_q}(1-z\mu)e^{z\mu},\qquad
 D_{T,q}(z)=\prod_{\mu\in T_q}(1-z\mu)e^{z\mu}$$ are well defined, the first finite and the second locally normally convergent. RH-234 gives the exact identity $$\det_2(I-zA)=D_{H,q}(z)D_{T,q}(z).$$ No invariant-subspace basis is needed.

The threshold $q$ is an explicit design parameter. The theorem is canonical after $q$ is fixed, not a claim that the dynamics chooses $q=1/2$. It also does not prove that $H_q$ equals the RH-272 counterloop atoms. Gates A--E remain false/open.
