---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-279-variable-rank-block-power-tail-criterion"
canonical_tex: "zeta_mvp0/papers/RH-279-variable-rank-block-power-tail-criterion/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-279-variable-rank-block-power-tail-criterion/main.pdf"
source_sha256: "14638c558f1e6b140700c9064631d817cd72974d8007eb651fcf31dcf6cf392c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Variable-Rank Block-Power Criterion for Moving Quotient Tails

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-279-variable-rank-block-power-tail-criterion>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-279-variable-rank-block-power-tail-criterion/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-279-variable-rank-block-power-tail-criterion/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-279-variable-rank-block-power-tail-criterion/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-279-variable-rank-block-power-tail-criterion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We replace the fixed-space convergence hypothesis of RH-269 by a direct variable-rank statement. The operators may act on changing quotient spaces, the selected rank and block length may grow, and only trace-norm/operator- norm power bounds are required. A geometric block decomposition then gives the full RH-246 logarithmic tail estimate beyond the moving head. The criterion is exact and conditional; no such uniform moving certificate is currently archived.
author:
- Bin Wang
date: July 2026
title: 'A Variable-Rank Block-Power Criterion for Moving Quotient Tails'
```

## Markdown 正文

# Hypotheses

Let $C_\sigma$ act on a Hilbert space $H_\sigma$, let $m_\sigma\ge2$, and assume uniformly $$\|C_\sigma^{m_\sigma}\|_1\le K_\sigma,\quad
 \|C_\sigma^{m_\sigma}\|\le\eta_\sigma<1,\quad
 \|C_\sigma^r\|\le L_\sigma^r\ (0\le r<m_\sigma).$$

# Theorem

For $n=\ell m_\sigma+r$, $0\le r<m_\sigma$, $n\ge m_\sigma$, $$|\operatorname{Tr}C_\sigma^n|
 \le K_\sigma\eta_\sigma^{\ell-1}L_\sigma^r.$$ Consequently, if $R>0$ and $\eta_\sigma R^{m_\sigma}<1$, $$\sum_{n\ge m_\sigma}\frac{|\operatorname{Tr}C_\sigma^n|R^n}{n}
 \le
 \frac{K_\sigma R^{m_\sigma}}{m_\sigma(1-\eta_\sigma R^{m_\sigma})}
 \sum_{r=0}^{m_\sigma-1}(L_\sigma R)^r.$$

Factor $C^n=(C^m)^{\ell-1}C^mC^r$, use the ideal inequality for the trace, and group the geometric series by residue classes. The denominator $n^{-1}\le(\ell m)^{-1}\le m^{-1}$ gives the displayed bound.

# Route consequence

If $m_\sigma\to\infty$, $\eta_\sigma R^{m_\sigma}\to0$, and $$\frac{K_\sigma R^{m_\sigma}}{m_\sigma}
 \sum_{r=0}^{m_\sigma-1}(L_\sigma R)^r\longrightarrow0,$$ then, with a uniform prefix budget, the moving tail vanishes. A convenient stronger condition is $$\limsup_{\sigma\downarrow0}K_\sigma^{1/m_\sigma}R
 \max\{1,L_\sigma R\}<1.$$ This is precisely the rank-growing replacement for a fixed limiting quotient. Supplying these bounds is an open operator problem; finite twelfth-power contractions do not supply them.
