---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-292-tail-absorbed-weighted-bridge-clock"
canonical_tex: "zeta_mvp0/papers/RH-292-tail-absorbed-weighted-bridge-clock/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-292-tail-absorbed-weighted-bridge-clock/main.pdf"
source_sha256: "8c14a69aa13af391aca1ecd48c15d053646a0743f576cc455b46719b9f64c437"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Tail Absorption Shortens the Missing Weighted Bridge Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-292-tail-absorbed-weighted-bridge-clock>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-292-tail-absorbed-weighted-bridge-clock/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-292-tail-absorbed-weighted-bridge-clock/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-292-tail-absorbed-weighted-bridge-clock/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-292-tail-absorbed-weighted-bridge-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The projection-free spectral tail was instantiated with the convenient cut $m_\sigma=\lceil4\log(1/\sigma)\rceil$, and the missing determinant leaf was therefore recorded as a weighted coefficient bridge up to that order. We show that this is longer than necessary. Split the prefix again at $h_\sigma=\lceil a_*\log(1/\sigma)\rceil$, where $a_*=1/\log(10/7)$. The intervening noisy-complement coefficients are absorbed by the sharp critical mass-and-cap tail, while the deterministic coefficients are absorbed by the certified target envelope. Hence a direct bridge only to $h_\sigma$, or the two typed constituent bridges to that clock, implies the original slope-four prefix. This is a strict reduction of the reopening input, not a proof that the bridge is present.
author:
- Bin Wang
date: July 2026
title: Tail Absorption Shortens the Missing Weighted Bridge Clock
```

## Markdown 正文

# Budgets

Fix $R=7/5$, $q=1/2$, and let $$m_\sigma=\lceil4L_\sigma\rceil,\qquad
 h_\sigma=\lceil a_*L_\sigma\rceil,\qquad
 L_\sigma=\log(1/\sigma),\qquad
 a_*=\frac1{\log(1/(qR))}.$$ For complement traces $\tau_{\sigma,n}$ and target anchors $a_n$, write $$P_\sigma(u)=\sum_{2\le n<u}
 \frac{|\tau_{\sigma,n}-a_n|R^n}{n}.$$ The RH-282 mass law gives $|\tau_{\sigma,n}|\le\sigma^{-1}q^{n-2}$, and RH-267 gives $|a_n|<48q_*^n$ with $q_*=(0.85\lambda)^{-1}=0.7008752258\ldots$.

# Clock-shortening theorem

[\[thm:shorten\]]{#thm:shorten label="thm:shorten"} For all sufficiently small $\sigma$, $$P_\sigma(m_\sigma)\le P_\sigma(h_\sigma)
+S_\sigma(h_\sigma)+T_\sigma(h_\sigma),$$ where $$S_\sigma(h)=\sum_{n\ge h}\frac{|\tau_{\sigma,n}|R^n}{n},
\qquad
 T_\sigma(h)=\sum_{n\ge h}\frac{|a_n|R^n}{n}.$$ Moreover, $$S_\sigma(h_\sigma)\le
 \frac{40}{3h_\sigma},\qquad
 T_\sigma(h_\sigma)\le
 \frac{48(q_*R)^{h_\sigma}}{h_\sigma(1-q_*R)}
 \longrightarrow0.$$ Consequently $P_\sigma(h_\sigma)\to0$ implies $P_\sigma(m_\sigma)\to0$. It is also sufficient that the RH-288 typed budgets $E_\sigma(h_\sigma)$ and $D_\sigma(h_\sigma)$ both tend to zero.

The triangle inequality on the slab $h_\sigma\le n<m_\sigma$ gives the first display. Since $qR=7/10$ and $a_*\log(10/7)=1$, $$\sigma^{-1}(qR)^{h_\sigma}
 \le \sigma^{-1}(qR)^{a_*L_\sigma}=1.$$ Summing the geometric trace envelope gives $$S_\sigma(h_\sigma)
 \le\frac{\sigma^{-1}q^{-2}(qR)^{h_\sigma}}
 {h_\sigma(1-qR)}
 \le\frac{40}{3h_\sigma}.$$ The target estimate follows similarly from $q_*R<1$. Finally, $P_\sigma(h)\le E_\sigma(h)+D_\sigma(h)$ is the exact typed decomposition of RH-288.

# Protocol and boundary

The accompanying computation evaluates the two certified tail bounds at five noise scales and records the critical and slope-four clocks. It tests only the displayed inequalities; no noisy coefficient data are fitted.

The theorem changes the required bridge horizon from slope $4$ to the sharp mass-and-cap slope $a_*=2.803673252\ldots$. It does not prove $P_\sigma(h_\sigma)\to0$, identify the modulus head with a counterloop, or construct a physical Riesz quotient. Gates A--E remain false/open; no Hilbert--Polya operator, Riemann-zero identification, zeta-divisor equality, von Mangoldt trace, or RH conclusion is asserted.
