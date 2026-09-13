---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-285-uniform-det2-tail-derivative-envelope"
canonical_tex: "zeta_mvp0/papers/RH-285-uniform-det2-tail-derivative-envelope/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-285-uniform-det2-tail-derivative-envelope/main.pdf"
source_sha256: "3a3d44e0cdcb674daa35f161487f96427a2c9b3ce468b4ca2c5f504695d26a55"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Derivative Envelopes for Projection-Free $\det_2$ Tails

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-285-uniform-det2-tail-derivative-envelope>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-285-uniform-det2-tail-derivative-envelope/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-285-uniform-det2-tail-derivative-envelope/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-285-uniform-det2-tail-derivative-envelope/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-285-uniform-det2-tail-derivative-envelope/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The modulus-complete complement of RH-282 has an all-order geometric trace envelope. We show that the same estimate controls every fixed derivative of the omitted logarithmic determinant tail. If $|\tau_{\sigma,n}|\le M_\sigma q^{n-2}$, $M_\sigma\le C\sigma^{-\alpha}$, and $qR<1$, then the $s$th derivative of $\sum_{n\ge m}\tau_{\sigma,n}z^n/n$ on $|z|\le R$ is bounded by a constant times $M_\sigma m^{s-1}(qR)^m$. A logarithmic clock strictly above the sharp RH-283 threshold therefore gives convergence in every fixed $C^s$ norm. In the Hardy-disk instance the gain is a positive power of noise. This theorem controls only the complementary spectral factor; the finite head-to- monodromy bridge remains open.
author:
- Bin Wang
date: July 2026
title: 'Uniform Derivative Envelopes for Projection-Free $\det_2$ Tails'
```

## Markdown 正文

# Derivative estimate

Assume $$|\tau_{\sigma,n}|\le M_\sigma q^{n-2},\qquad n\ge2,$$ and define $$E_{\sigma,m}(z)=\sum_{n\ge m}\frac{\tau_{\sigma,n}}n z^n.$$

[\[thm:derivative\]]{#thm:derivative label="thm:derivative"} Let $x=qR<1$ and fix an integer $s\ge0$. There is a finite constant $$B_{s,x}=\sum_{k\ge0}(1+k)^{\max(s-1,0)}x^k$$ such that, for $m\ge\max(2,s)$, $$\label{eq:bound}
 \sup_{|z|\le R}|E_{\sigma,m}^{(s)}(z)|
 \le M_\sigma q^{-2}R^{-s}B_{s,x}
 m^{\max(s-1,0)}x^m.$$

For $s=0$, use $1/n\le1/m$. For $s\ge1$, differentiating $z^n/n$ gives a coefficient no larger than $n^{s-1}R^{n-s}$. Write $n=m+k$ and use $(m+k)^{s-1}\le m^{s-1}(1+k)^{s-1}$. The remaining series is exactly $B_{s,x}$.

If $M_\sigma\le C\sigma^{-\alpha}$ and $m_\sigma=\lceil a\log(1/\sigma)\rceil$ with $a\log(1/(qR))>\alpha$, then $$E_{\sigma,m_\sigma}\longrightarrow0
 \quad\text{in }C^s(|z|\le R)$$ for every fixed $s$. The canonical-product tail $\exp(-E_{\sigma,m_\sigma})$ converges to $1$ in the same topology.

The right side of [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"} is a fixed power of $\log(1/\sigma)$ times $\sigma^{a\log(1/(qR))-\alpha}$. It tends to zero. The exponential claim follows from the chain rule on a bounded neighborhood of zero.

# Certified instance

For $\alpha=1$, $q=1/2$, $R=7/5$, and $a=4$, the exponent is $$4\log(10/7)-1=0.426699775\ldots>0.$$ Thus the high-order noisy spectral factor from RH-282 tends to one together with every fixed derivative on the full target disk.

Derivative control of the tail cannot identify the finite head. In particular it does not show that the modulus-selected noisy roots lie on the finite monodromy shell. Gates A--E remain false/open, and no arithmetic or Hilbert--Polya conclusion is drawn.
