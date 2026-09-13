---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-295-exact-clock-unweighted-prefix-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-295-exact-clock-unweighted-prefix-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-295-exact-clock-unweighted-prefix-obstruction/main.pdf"
source_sha256: "eb35acb1a24c3b87fb03453bd8f69fe04f3043d96fed58f1d0a4fa2098773c88"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Agreement on the Exact Clock Need Not Control a Weighted Prefix

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-295-exact-clock-unweighted-prefix-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-295-exact-clock-unweighted-prefix-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-295-exact-clock-unweighted-prefix-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-295-exact-clock-unweighted-prefix-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-295-exact-clock-unweighted-prefix-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The weighted diagonal theorem gives agreement on an unspecified growing window. One might hope that merely synchronizing its unweighted maximum to the minimal logarithmic bridge clock would suffice. We give a sharp scoped counterexample. For any prescribed moving cut and any radius greater than one, place one coefficient spike at the last visible order, with amplitude equal to the inverse square root of its geometric weight. The maximum error on the entire prescribed window tends to zero and every fixed coefficient is eventually exact, while the weighted prefix diverges. Hence clock synchronization without a rate is still insufficient. The construction is an information-theoretic coefficient array, not a physical spectral shell.
author:
- Bin Wang
date: July 2026
title: Uniform Agreement on the Exact Clock Need Not Control a Weighted Prefix
```

## Markdown 正文

# Escaping spike

Let $R>1$ and let $m_\sigma\to\infty$ be any integer-valued clock. For small $\sigma$, define $$e_{\sigma,n}=
 \begin{cases}
 R^{-(m_\sigma-1)/2},&n=m_\sigma-1,\\
 0,&2\le n<m_\sigma-1.
 \end{cases}$$

# Obstruction theorem

[\[thm:spike\]]{#thm:spike label="thm:spike"} The array above has $$\max_{2\le n<m_\sigma}|e_{\sigma,n}|
 =R^{-(m_\sigma-1)/2}\longrightarrow0.$$ For every fixed $n$, $e_{\sigma,n}=0$ for all sufficiently small $\sigma$. Nevertheless, $$\sum_{2\le n<m_\sigma}\frac{|e_{\sigma,n}|R^n}{n}
 =\frac{R^{(m_\sigma-1)/2}}{m_\sigma-1}
 \longrightarrow\infty.$$

The first two claims follow because the support order tends to infinity. Only one term is nonzero in the weighted sum, giving the displayed identity. An exponential in $m_\sigma$ dominates its linear denominator.

# Minimal-clock specialization

At the RH-292 clock $$m_\sigma=\left\lceil
 \frac{\log(1/\sigma)}{\log(10/7)}\right\rceil,$$ put $$\beta_*=\frac{\log(7/5)}{\log(10/7)}
 =0.9433582098747317\ldots.$$ The spike in Theorem [\[thm:spike\]](#thm:spike){reference-type="ref" reference="thm:spike"} then has the explicit scales $$\max_{n<m_\sigma}|e_{\sigma,n}|
 =\Theta(\sigma^{\beta_*/2}),
\qquad
 W_\sigma(R)=
 \Theta\!\left(
 \frac{\sigma^{-\beta_*/2}}{\log(1/\sigma)}
 \right).$$ Thus the unweighted maximum decays with exponent $0.4716791049373659\ldots$ while its weighted image grows with the same power. The construction can be placed at any moving cut, so it also applies to the original slope-four clock.

# Experiment protocol

The computation sets $m_\sigma=\lceil\log(1/\sigma)/\log(10/7)\rceil$ and records the spike amplitude and weighted budget over five noise scales. It verifies an exact formula and performs no fit.

This result does not assert that the physical noisy traces contain such a spike. It proves only that fixed-order convergence, even upgraded to an unweighted maximum on the exact clock, cannot by itself imply the RH-288 weighted leaf. Gates A--E remain false/open and no RH conclusion follows.
