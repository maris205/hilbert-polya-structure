---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-276-small-noise-hilbert-schmidt-mass-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-276-small-noise-hilbert-schmidt-mass-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-276-small-noise-hilbert-schmidt-mass-obstruction/main.pdf"
source_sha256: "57e98f7c9f1b79201bfec38a1020d3cd0c0bf9b891df8b625967839befd46b4e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Sharp Small-Noise Hilbert--Schmidt Mass of the Folded Gaussian Operator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-276-small-noise-hilbert-schmidt-mass-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-276-small-noise-hilbert-schmidt-mass-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-276-small-noise-hilbert-schmidt-mass-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-276-small-noise-hilbert-schmidt-mass-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-276-small-noise-hilbert-schmidt-mass-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We compute the exact leading Hilbert--Schmidt mass of the continuum folded Gaussian operator. In the natural $L^2(0,1)$ geometry, $\sigma\|K_\sigma\|_2^2\to(2\sqrt\pi)^{-1}$; after the Hardy scaling $r_H=0.85$, the constant is $0.390442618372\ldots$. Hence the raw family cannot converge in $\mathcal S_2$ at zero noise. The conclusion is scoped: it does not exclude a rank-growing cloud quotient or a cancellation-sensitive trace theorem.
author:
- Bin Wang
date: July 2026
title: 'The Sharp Small-Noise Hilbert--Schmidt Mass of the Folded Gaussian Operator'
```

## Markdown 正文

# Exact row formula

Let $u_c=1.5436890126920753\ldots$, $a=f(x)=1-u_cx^2$, and let $k_\sigma(x,y)$ be the normalized folded row $$k_\sigma(x,y)=\frac{
 e^{-(y-a)^2/(2\sigma^2)}+e^{-(y+a)^2/(2\sigma^2)}}{Z_\sigma(a)},
 \qquad 0\le y\le1.$$ Direct Gaussian integration gives $$\int_0^1 k_\sigma(x,y)^2dy=\frac{J_\sigma(a)}{Z_\sigma(a)^2},$$ where $$\begin{aligned}
J_\sigma(a)&=\frac{\sigma\sqrt\pi}{2}
\left[\operatorname{erf}\frac{1-a}{\sigma}
+\operatorname{erf}\frac{1+a}{\sigma}
+2e^{-a^2/\sigma^2}\operatorname{erf}\frac1\sigma\right],\\
Z_\sigma(a)&=\sigma\sqrt{\frac\pi2}
\left[\operatorname{erf}\frac{1-a}{\sqrt2\sigma}
+\operatorname{erf}\frac{1+a}{\sqrt2\sigma}\right].\end{aligned}$$

# Sharp law

For $A_\sigma=r_H^{-1}K_\sigma$, $$\lim_{\sigma\downarrow0}\sigma\|A_\sigma\|_{\mathcal S_2}^2
 =\frac{1}{2\sqrt\pi r_H^2}=0.3904426183721497\ldots .$$ In particular no sequence $A_{\sigma_j}$ with $\sigma_j\downarrow0$ can converge in $\mathcal S_2$.

For almost every $x$, $a\in(-1,1)\setminus\{0\}$. In the row formula the opposite folded Gaussian and both boundaries become exponentially negligible, so $\sigma J_\sigma(a)/Z_\sigma(a)^2\to(2\sqrt\pi)^{-1}$. The normalizer is uniformly bounded below by a half-Gaussian mass, while $(p+q)^2\le2(p^2+q^2)$ gives $\sigma\int k_\sigma(x,y)^2dy\le C$ uniformly in $x$ and small $\sigma$. Dominated convergence over $x\in[0,1]$ proves the limit. Hardy scaling multiplies the square norm by $r_H^{-2}$.

An independent interior-window estimate gives $\|K_\sigma\|_2^2\ge0.0700325262/\sigma$, while the inherited upper bound is $4.5135/\sigma$. The exact limit identifies the sharp leading constant.

# Audit and boundary

One-dimensional quadrature gives ratios to the limit decreasing from $1.1579$ at $\sigma=0.04$ to $1.0104$ at $\sigma=0.00025$. This is a reproduction check, not part of the proof. The theorem closes only the raw zero-noise $\mathcal S_2$ option; Gates A--E remain open.
