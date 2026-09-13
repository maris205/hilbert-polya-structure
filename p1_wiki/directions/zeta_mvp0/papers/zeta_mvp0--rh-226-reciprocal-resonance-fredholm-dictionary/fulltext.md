---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-226-reciprocal-resonance-fredholm-dictionary"
canonical_tex: "zeta_mvp0/papers/RH-226-reciprocal-resonance-fredholm-dictionary/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-226-reciprocal-resonance-fredholm-dictionary/main.pdf"
source_sha256: "c305466cf922eba58b9f1f9bb7afcd93b8ad4b11bb2da8a5f98085f99beb3e1e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Reciprocal Resonance--Fredholm Dictionary Reconnecting Rank-Growing Clouds to the Fixed-Noise Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-226-reciprocal-resonance-fredholm-dictionary>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-226-reciprocal-resonance-fredholm-dictionary/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-226-reciprocal-resonance-fredholm-dictionary/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-226-reciprocal-resonance-fredholm-dictionary/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-226-reciprocal-resonance-fredholm-dictionary/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The rank-growing atlas records operator resonances $\lambda$, while a Fredholm determinant in spectral variable $z$ vanishes at $z=1/\lambda$. This paper makes that change of variable explicit and prevents the direct resonance divisor rejected in RH-225 from being confused with the correct determinant divisor.

  For a finite resonance multiset $\Lambda$ of size $n$ and characteristic polynomial $p_\Lambda(w)=\prod_{\lambda\in\Lambda}(w-\lambda)$, $$\prod_{\lambda\in\Lambda}(1-z\lambda)
   =z^n p_\Lambda(1/z).$$ Second regularization multiplies each factor by $e^{z\lambda}$ and therefore does not change the zeros. Conjugate resonance clouds produce conjugate reciprocal-zero clouds and real entire products.

  Across the 32 physical endpoints, the identity is evaluated on 3,072 complex grid points with maximum error $9.16\times10^{-15}$. Reciprocal moduli range from $1.15129$ to $13.54281$, and the maximum scale-free zero-factor residual is $2.29\times10^{-16}$. Direct evaluation of the full regularized product at the outer zeros is numerically unstable, reaching a raw residual of $6.51\times10^4$; this illustrates why factorwise or logarithmic diagnostics are required.

  The infinite fixed-positive-noise Hilbert--Schmidt determinant is already a rigorous result of RH-7. The contribution here is the exact dictionary from the new finite clouds to that determinant. No locally uniform small-noise limit or self-adjoint spectral interpretation is asserted.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  The Reciprocal Resonance--Fredholm Dictionary\
  Reconnecting Rank-Growing Clouds to the Fixed-Noise Determinant
```

## Markdown 正文

# Correcting the spectral variable

RH-225 proves that a tight rank-growing cloud cannot itself be a locally finite zero divisor [@WangRH225]. That result concerns the points $\lambda_j$ in the operator spectrum. A Fredholm determinant is instead a function of a spectral parameter $z$: $$\label{eq:fredholm}
 D_A(z)=\operatorname{det}(I-zA).$$ If $A$ has nonzero eigenvalues $\lambda_j$, the zeros of [\[eq:fredholm\]](#eq:fredholm){reference-type="eqref" reference="eq:fredholm"} are their reciprocals. This distinction is standard but decisive for the current route.

# Finite polynomial dictionary

Let $$p_\Lambda(w)=\prod_{j=1}^n(w-\lambda_j).$$

[\[prop:identity\]]{#prop:identity label="prop:identity"} For every $z\in\mathbb C$, $$\label{eq:identity}
 F_\Lambda(z):=\prod_{j=1}^n(1-z\lambda_j)
 =z^n p_\Lambda(1/z),$$ where the expression at $z=0$ is interpreted by continuity. The finite zeros are exactly $\lambda_j^{-1}$ for nonzero $\lambda_j$, with the same algebraic multiplicities.

For $z\ne0$, $$z^n p_\Lambda(1/z)
 =z^n\prod_j\frac{1-z\lambda_j}{z}
 =\prod_j(1-z\lambda_j).$$ Both sides equal one at $z=0$. The factorization gives the zero statement.

If $\Lambda$ is the complete spectrum of a finite matrix $A$, then $F_\Lambda(z)=\operatorname{det}(I-zA)$. If it is a selected spectral cloud, $F_\Lambda$ is the selected finite factor, not the determinant of the unresolved complement.

# Second regularization

For a finite multiset define $$\label{eq:det2}
 F_{\Lambda,2}(z)=
 \prod_{j=1}^n(1-z\lambda_j)e^{z\lambda_j}.$$

[\[cor:zeros\]]{#cor:zeros label="cor:zeros"} The zeros of $F_{\Lambda,2}$ are exactly $\{\lambda_j^{-1}\}$ with algebraic multiplicity.

The exponential factors are entire and nowhere zero.

The logarithm normalized by $\log F_{\Lambda,2}(0)=0$ is $$\label{eq:log}
 \log F_{\Lambda,2}(z)
 =\sum_j\bigl[\log(1-z\lambda_j)+z\lambda_j\bigr]
 =-\sum_{m\ge2}\frac{z^m}{m}\sum_j\lambda_j^m$$ whenever $|z|\max_j|\lambda_j|<1$. The missing linear term is the purpose of second regularization.

# Conjugation symmetry

[\[prop:real\]]{#prop:real label="prop:real"} If $\Lambda$ is conjugate closed, then $$\overline{F_{\Lambda,2}(\overline z)}=F_{\Lambda,2}(z).$$ In particular $F_{\Lambda,2}$ is real on the real axis and its reciprocal zero divisor is conjugate closed.

Conjugation permutes the factors in [\[eq:det2\]](#eq:det2){reference-type="eqref" reference="eq:det2"}.

Thus the shell-completion work of RH-222--RH-223 passes exactly to the Fredholm variable; no new pair matching is required [@WangRH222; @WangRH223].

# Fixed-noise infinite completion is inherited

For every fixed $\sigma>0$, RH-7 proves that the centered folded Gaussian operator $\mathcal N_\sigma$ is Hilbert--Schmidt and constructs $$\label{eq:infinite}
 \mathcal D_\sigma(z)
 =\det{}_2(I-z\mathcal N_\sigma)
 =\prod_j(1-z\lambda_{\sigma,j})e^{z\lambda_{\sigma,j}}.$$ Its zeros are the reciprocal non-Perron resonances [@WangRH7; @Simon2005]. Removing the negative parity mode as an additional finite factor gives the bulk determinant used by the later small-noise route.

Equation [\[eq:infinite\]](#eq:infinite){reference-type="eqref" reference="eq:infinite"} is not reproved or claimed as new here. The rank-growing atlas samples its bulk resonance factors after the inherited Hardy scaling and Haar channel construction. What remains open is uniform control as $\sigma\downarrow0$, not existence at fixed positive noise.

# Numerical audit

For each endpoint, Proposition [\[prop:identity\]](#prop:identity){reference-type="ref" reference="prop:identity"} is evaluated at 96 points: 24 equally spaced angles at radii $0.25,0.5,0.75,1$. The archive also compares newly computed reciprocals with those stored by RH-222.

  diagnostic                                           result
  ------------------------------------ ----------------------
  endpoint count                                           32
  polynomial identity evaluations                       3,072
  maximum identity error                 $9.16\times10^{-15}$
  maximum archived reciprocal error             floating zero
  maximum reciprocal conjugacy error           binary64 scale
  minimum reciprocal modulus                        $1.15129$
  maximum reciprocal modulus                       $13.54281$
  maximum zero-factor residual           $2.29\times10^{-16}$

All reciprocal zeros lie outside the unit disk because all selected Hardy-scaled resonances have modulus below one in the finite atlas.

## Why the raw zero residual is misleading

At $z=1/\lambda_k$, the mathematically stable test is $$\min_j|1-z\lambda_j|.$$ Directly multiplying all factors in [\[eq:det2\]](#eq:det2){reference-type="eqref" reference="eq:det2"} can be unstable: other linear and exponential factors may become very large before multiplication by a factor of size $10^{-16}$. The largest raw product residual in the audit is $6.51\times10^4$ even though the scale-free factor residual is $2.29\times10^{-16}$.

This is not evidence that the zero is absent. It is a conditioning warning, consistent with standard numerical practice for Fredholm determinants [@Bornemann2010]. Later comparisons use logarithms on a disk satisfying $|z\lambda|<1$.

# What inversion repairs and what it does not

Inversion repairs the local-finiteness architecture at fixed noise: eigenvalues of a compact operator accumulate only at zero, so reciprocal zeros escape to infinity. It does not automatically repair a singular family in $\sigma$. As noise decreases, more resonances may remain away from zero, putting more reciprocal zeros in one fixed disk. A small-noise determinant family therefore needs:

1.  local reciprocal-zero count stability;

2.  omitted-factor control uniform on compact $z$-sets;

3.  a moving-cloud or relative determinant if near-unit factors proliferate.

The next paper tests the first item on five fixed radii. Gate A remains open; the present determinant is nonself-adjoint and carries no established arithmetic trace formula or zeta divisor.
