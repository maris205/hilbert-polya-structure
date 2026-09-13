---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-302-annular-tail-moving-head-reduction"
canonical_tex: "zeta_mvp0/papers/RH-302-annular-tail-moving-head-reduction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-302-annular-tail-moving-head-reduction/main.pdf"
source_sha256: "e088176a3b3ea7f9e23f6451d1b1b4295498b37320229e0230d43e286c373bf0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Annular Tail Reduction to the Moving Spectral Head

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-302-annular-tail-moving-head-reduction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-302-annular-tail-moving-head-reduction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-302-annular-tail-moving-head-reduction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-302-annular-tail-moving-head-reduction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-302-annular-tail-moving-head-reduction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The direct annular criterion of RH-300 was left inactive because no norm estimate was known for the actual complement-to-anchor logarithmic mismatch. We prove that its high-order part is already controlled. For every fixed $1.4<\rho<\rho_*=1.426787\ldots$, the noisy modulus-complement tail and the deterministic target tail beyond $m_\sigma=\lceil4\log(1/\sigma)\rceil$ vanish in both $H^\infty(\rho)$ and $H^2(\rho)$ with explicit bounds. Consequently full annular convergence is equivalent to convergence of the moving polynomial head below $m_\sigma$. This locates the remaining obstruction without proving that the moving head converges.
author:
- Bin Wang
date: July 2026
title: Annular Tail Reduction to the Moving Spectral Head
```

## Markdown 正文

# Setup

Put $$q=\frac12,\qquad R=\frac75,\qquad
 q_*=(0.85\lambda)^{-1}=0.700875225854775\ldots,
 \qquad \rho_*=q_*^{-1}.$$ Let $C_\sigma$ be the modulus-complete spectral complement from RH-282, with squared spectral mass $M_\sigma\le\sigma^{-1}$, and write $$\tau_{\sigma,n}=\operatorname{Tr}C_\sigma^n,
 \qquad |\tau_{\sigma,n}|\le\sigma^{-1}q^{n-2}.$$ The deterministic numerator anchors satisfy the all-order RH-267 envelope $|a_n|<48q_*^n$. Define $$g_\sigma(z)=\sum_{n\ge2}
 \frac{\tau_{\sigma,n}-a_n}{n}z^n,
 \qquad
 g_\sigma^{<m}(z)=\sum_{2\le n<m}
 \frac{\tau_{\sigma,n}-a_n}{n}z^n.$$ For $q\rho<1$ and $q_*\rho<1$, both series are well defined on the closed disk of radius $\rho$.

# Tail theorem

[\[thm:tail\]]{#thm:tail label="thm:tail"} Fix $R<\rho<\rho_*$ and put $m_\sigma=\lceil4\log(1/\sigma)\rceil$, $x=q\rho$, and $y=q_*\rho$. Then $$\begin{aligned}
 \|g_\sigma-g_\sigma^{<m_\sigma}\|_{H^\infty(\rho)}
 &\le
 \frac{4\sigma^{-1}x^{m_\sigma}}
 {m_\sigma(1-x)}
 +\frac{48y^{m_\sigma}}
 {m_\sigma(1-y)},\\
 \|g_\sigma-g_\sigma^{<m_\sigma}\|_{H^2(\rho)}
 &\le
 \frac{4\sigma^{-1}x^{m_\sigma}}
 {m_\sigma\sqrt{1-x^2}}
 +\frac{48y^{m_\sigma}}
 {m_\sigma\sqrt{1-y^2}}.\end{aligned}$$ Both right sides tend to zero. More precisely, apart from the common $1/\log(1/\sigma)$ factor, their two powers of $\sigma$ are $$4\log(2/\rho)-1
 \quad\hbox{and}\quad
 4\log(\rho_*/\rho).$$ Hence for $X=H^\infty(\rho)$ or $H^2(\rho)$, $$\|g_\sigma\|_X\longrightarrow0
 \quad\Longleftrightarrow\quad
 \|g_\sigma^{<m_\sigma}\|_X\longrightarrow0.$$

For the noisy tail, use $|\tau_{\sigma,n}|\le4\sigma^{-1}q^n$ and $$\sum_{n\ge m}\frac{x^n}{n}
 \le\frac{x^m}{m(1-x)},\qquad
 \left(\sum_{n\ge m}\frac{x^{2n}}{n^2}\right)^{1/2}
 \le\frac{x^m}{m\sqrt{1-x^2}}.$$ The same estimates with $48y^n$ give the target terms. Since $m_\sigma\ge4\log(1/\sigma)$ and $x,y<1$, the displayed powers follow. They are positive throughout $R<\rho<\rho_*$. The equivalence is the triangle inequality applied to the vanishing tail.

# Numerical protocol and scope

The reproducible computation evaluates the two certified bounds at $\rho=1.405,1.41,1.42$. At $\rho=1.41$ the noisy and target exponents are $0.3982299047\ldots$ and $0.0473427916\ldots$. The small target exponent explains why finite-noise upper bounds can remain large even though the asymptotic theorem is strict.

The theorem closes only the analytic high-order tail. It supplies no estimate for the moving polynomial $g_\sigma^{<m_\sigma}$ and therefore does not activate RH-300. Gates A--E remain false/open; no Hilbert--Polya, Riemann-zero, zeta-divisor, von Mangoldt trace, or RH conclusion is made.
