---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-313-parity-orthogonal-endpoint-hardy-splitting"
canonical_tex: "zeta_mvp0/papers/RH-313-parity-orthogonal-endpoint-hardy-splitting/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-313-parity-orthogonal-endpoint-hardy-splitting/main.pdf"
source_sha256: "5c002f948ae52944c98cf25f9633ee615321d6ebcf3cb6b611dfbd0b3f55a7c7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Parity-Orthogonal Hardy Channels at the Endpoint Logarithm

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-313-parity-orthogonal-endpoint-hardy-splitting>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-313-parity-orthogonal-endpoint-hardy-splitting/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-313-parity-orthogonal-endpoint-hardy-splitting/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-313-parity-orthogonal-endpoint-hardy-splitting/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-313-parity-orthogonal-endpoint-hardy-splitting/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The endpoint singularity found in RH-312 admits an exact even--odd decomposition. We identify the two closed forms and prove that the Hardy norm is their orthogonal sum. Endpoint convergence is therefore equivalent to convergence in both parity channels separately. This criterion does not assert that either actual noisy channel converges.
author:
- Bin Wang
date: July 2026
title: 'Parity-Orthogonal Hardy Channels at the Endpoint Logarithm'
```

## Markdown 正文

# The two singular channels

Let $L(w)=\log(1-w)+w=-\sum_{n\ge2}w^n/n$. Its parity projections are $$L_{\rm ev}(w)=\frac{L(w)+L(-w)}2=\frac12\log(1-w^2),$$ and $$L_{\rm odd}(w)=\frac{L(w)-L(-w)}2
 =w+\frac12\log\frac{1-w}{1+w}.$$ Both belong to $H^2$ on the unit disk, and their Taylor supports are disjoint.

For every $f\in H^2$, define $f_{\rm ev}(w)=\{f(w)+f(-w)\}/2$ and $f_{\rm odd}(w)=\{f(w)-f(-w)\}/2$. Then $$f=f_{\rm ev}+f_{\rm odd},\qquad
 \|f\|_{H^2}^2=\|f_{\rm ev}\|_{H^2}^2+
 \|f_{\rm odd}\|_{H^2}^2.$$ Consequently $f_\sigma\to0$ in $H^2$ if and only if both parity projections tend to zero.

The even and odd Taylor coefficients occupy disjoint subsets of the orthonormal monomial basis. Parseval gives the identity and the equivalence.

# Application to the deterministic endpoint

RH-312 writes the endpoint target as $L+H_{\rm reg}$ with $H_{\rm reg}$ analytic past the unit circle. Projecting gives $$(L_{\rm ev}+H_{{\rm reg},{\rm ev}})
 +(L_{\rm odd}+H_{{\rm reg},{\rm odd}}),$$ and both regular pieces retain the larger analytic radius. Thus the two displayed logarithms contain the entire parity-resolved endpoint singularity.

The theorem is an exact criterion, not a proof that the noisy modulus complement approximates either channel. No spectral cloud, Gate A--E, or RH conclusion is obtained.
