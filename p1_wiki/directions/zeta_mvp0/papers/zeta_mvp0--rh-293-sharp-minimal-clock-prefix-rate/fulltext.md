---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-293-sharp-minimal-clock-prefix-rate"
canonical_tex: "zeta_mvp0/papers/RH-293-sharp-minimal-clock-prefix-rate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-293-sharp-minimal-clock-prefix-rate/main.pdf"
source_sha256: "fe4b53ee57eeb8ea8d4e5b3cc10ec6cf2f3b1380cb95bd8222a56546ab43297e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Sharp Uniform-Error Rate at the Minimal Weighted Bridge Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-293-sharp-minimal-clock-prefix-rate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-293-sharp-minimal-clock-prefix-rate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-293-sharp-minimal-clock-prefix-rate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-293-sharp-minimal-clock-prefix-rate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-293-sharp-minimal-clock-prefix-rate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-292 shortens the unresolved coefficient bridge to the critical mass-and-cap clock. We determine the exact rate needed if the only new input is a uniform bound on the coefficient error over that moving window. The weighted geometric sum is asymptotic to $R^m/(m(R-1))$. Therefore, for $m=\lceil a\log(1/\sigma)\rceil$ and error $O(\sigma^\beta)$, the sharp threshold is $\beta=a\log R$; equality still decays logarithmically, while a saturated family diverges below it. At $R=7/5$ and the minimal bridge slope $a=1/\log(10/7)$, the required exponent is $0.9433582098\ldots$. This theorem quantifies the missing input but does not provide it for the physical noisy traces.
author:
- Bin Wang
date: July 2026
title: 'The Sharp Uniform-Error Rate at the Minimal Weighted Bridge Clock'
```

## Markdown 正文

# Uniform-error class

For $R>1$ and $m\ge3$, put $$A_m(R)=\sum_{n=2}^{m-1}\frac{R^n}{n}.$$ Consider all arrays satisfying $|e_{\sigma,n}|\le\varepsilon_\sigma$ for $2\le n<m_\sigma$. Their weighted budget is $$W_\sigma(R)=\sum_{2\le n<m_\sigma}
\frac{|e_{\sigma,n}|R^n}{n}.$$

# Sharp clock law

[\[thm:rate\]]{#thm:rate label="thm:rate"} As $m\to\infty$, $$A_m(R)\sim\frac{R^m}{m(R-1)}.$$ The supremum of $W_\sigma(R)$ over the uniform-error class is exactly $\varepsilon_\sigma A_{m_\sigma}(R)$. Fix $a>0$, $\beta>0$, and $C>0$. If $$m_\sigma=\lceil a\log(1/\sigma)\rceil,\qquad
 \varepsilon_\sigma=C\sigma^\beta,$$ then every array in the class has $W_\sigma(R)\to0$ when $\beta\ge a\log R$. At equality the worst budget is $\Theta(1/\log(1/\sigma))$. If $\beta<a\log R$, the saturated array $|e_{\sigma,n}|=\varepsilon_\sigma$ has $W_\sigma(R)\to\infty$.

Writing $j=m-n$ gives $$\frac{m}{R^m}A_m(R)=
 \sum_{j=1}^{m-2}\frac{m}{m-j}R^{-j}.$$ For fixed $j$ the summand tends to $R^{-j}$. Splitting at $j=m/2$ controls the first part by a summable geometric sequence and the second by an exponentially small remainder, proving the asymptotic and $\sum_{j\ge1}R^{-j}=1/(R-1)$. The class supremum follows term by term and is attained by the saturated array. Finally, $R^{m_\sigma}=\Theta(\sigma^{-a\log R})$; substitution proves all three regimes.

# Target value and protocol

For the RH-292 slope $$a_*=\frac1{\log(10/7)}$$ and $R=7/5$, the exact threshold is $$\beta_*=\frac{\log(7/5)}{\log(10/7)}
 =0.9433582098747317\ldots.$$ The accompanying computation evaluates saturated budgets below, at, and above this exponent over five noise scales. These rows illustrate the exact formula and are not fits to noisy operator data.

The fixed-order Gaussian localization estimate has constants depending on the fixed order. It is not a uniform estimate over $n<h_\sigma$ and hence does not activate this theorem. Gates A--E remain false/open, with no Hilbert--Polya, Riemann-zero, zeta-divisor, von Mangoldt, or RH claim.
