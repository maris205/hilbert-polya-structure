---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-304-minimal-clock-complement-mass-demand"
canonical_tex: "zeta_mvp0/papers/RH-304-minimal-clock-complement-mass-demand/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-304-minimal-clock-complement-mass-demand/main.pdf"
source_sha256: "0c09f67545d8cb49b8d55fb518a5360ed4df6861d00481597864843eba63d4ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Complement Spectral-Mass Demand at the Minimal Bridge Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-304-minimal-clock-complement-mass-demand>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-304-minimal-clock-complement-mass-demand/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-304-minimal-clock-complement-mass-demand/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-304-minimal-clock-complement-mass-demand/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-304-minimal-clock-complement-mass-demand/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The exact odd deterministic anchors give a direct lower bound on the amount of modulus-complement spectral mass needed for relative coefficient matching. If all complement eigenvalues have modulus at most $q=1/2$ and their squared mass is $M$, then relative matching at an odd order $n$ forces $M$ to grow like $(q_*/q)^n$. At the minimal tail-absorbed bridge slope $1/\log(10/7)$ this demand is $\sigma^{-0.9468615163\ldots}$, leaving only $0.0531384836\ldots$ of the available $\sigma^{-1}$ mass exponent. This is a necessary condition under relative matching, not a proof that such matching occurs or fails.
author:
- Bin Wang
date: July 2026
title: 'Complement Spectral-Mass Demand at the Minimal Bridge Clock'
```

## Markdown 正文

# Odd anchors and spectral cap

Let $(\mu_j)$ be a square-summable multiset with $|\mu_j|\le q=1/2$, and put $$M=\sum_j|\mu_j|^2,
 \qquad \tau_n=\sum_j\mu_j^n.$$ Then $|\tau_n|\le Mq^{n-2}$. For every odd $n\ge3$, the deterministic anchor is exactly $$a_n=\frac{q_*^n}{1+\lambda^{-n}},\qquad
 q_*=(0.85\lambda)^{-1}=0.700875225854775\ldots.$$

# Mass-demand theorem

[\[thm:mass\]]{#thm:mass label="thm:mass"} Let $n\ge3$ be odd and $0\le\theta<1$. If $$|\tau_n-a_n|\le\theta a_n,$$ then $$\boxed{
 M\ge
 \frac{(1-\theta)q^2}{1+\lambda^{-n}}
 \left(\frac{q_*}{q}\right)^n.}$$

The relative bound and positivity of $a_n$ give $|\tau_n|\ge(1-\theta)a_n$. Combine this with $|\tau_n|\le Mq^{n-2}$ and rearrange.

[\[cor:clock\]]{#cor:clock label="cor:clock"} Suppose $n_\sigma=a\log(1/\sigma)+O(1)$ is odd and the relative matching hypothesis of Theorem [\[thm:mass\]](#thm:mass){reference-type="ref" reference="thm:mass"} holds with a fixed $\theta<1$. Then $$\liminf_{\sigma\downarrow0}
 \frac{\log M_\sigma}{\log(1/\sigma)}
 \ge a\log(q_*/q).$$ At $$a_*=\frac1{\log(10/7)}=2.803673252057129\ldots$$ the required exponent is $$\gamma_*=a_*\log(q_*/q)
 =0.9468615163684616\ldots.$$ The slope at which the demand reaches exponent one is $$a_{\rm mass}=\frac1{\log(q_*/q)}
 =2.961017216974005\ldots.$$ Thus every slope strictly above $a_{\rm mass}$ is incompatible with the archived cap $M_\sigma\le\sigma^{-1}$ under uniform relative odd matching.

Take logarithms in Theorem [\[thm:mass\]](#thm:mass){reference-type="ref" reference="thm:mass"}; fixed factors and the $O(1)$ displacement of $n_\sigma$ contribute $o(\log(1/\sigma))$.

# Protocol and exact scope

The computation evaluates the lower bound at odd orders $9,19,39$ with $\theta=1/2$, and records $q_*/q$, $\gamma_*$, its slack $1-\gamma_*$, and $a_{\rm mass}$. No noisy coefficient is assumed or fitted.

Weighted-prefix convergence does not by itself imply relative matching at a moving odd order. The theorem therefore supplies a conditional necessary mass law, not a contradiction at the minimal clock. Gates A--E remain false/open; no operator identification or RH conclusion follows.
