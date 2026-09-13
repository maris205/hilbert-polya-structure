---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-308-hardy-dominant-annular-coefficient-conversion"
canonical_tex: "zeta_mvp0/papers/RH-308-hardy-dominant-annular-coefficient-conversion/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-308-hardy-dominant-annular-coefficient-conversion/main.pdf"
source_sha256: "8c0ca72c8eb4fcdc56e9a717ca1bee4e3b57dd700a0f7e113031cc0421111e95"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Hardy-Dominant Annular Coefficient Conversion and Its Sharp Gap Order

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-308-hardy-dominant-annular-coefficient-conversion>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-308-hardy-dominant-annular-coefficient-conversion/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-308-hardy-dominant-annular-coefficient-conversion/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-308-hardy-dominant-annular-coefficient-conversion/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-308-hardy-dominant-annular-coefficient-conversion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The direct $H^\infty$ coefficient estimate of RH-300 used Cauchy's bound and has gap constant of order $\eta^{-1}$ when $\rho=Re^\eta$. Since normalized $H^\infty$ embeds contractively into $H^2$, the Hardy estimate improves this to order $\eta^{-1/2}$. We prove the Hardy constant exactly and show that its square-root order is optimal: equality is attained in $H^2$, while dyadic Rudin--Shapiro blocks give the same order on the $H^\infty$ unit ball. At $R=1.4$, $\rho=1.41$, the constants are $139.007\ldots$ and $8.292\ldots$. No norm decay for the actual mismatch is asserted.
author:
- Bin Wang
date: July 2026
title: 'Hardy-Dominant Annular Coefficient Conversion and Its Sharp Gap Order'
```

## Markdown 正文

# Coefficient functional

Let $f(z)=\sum_{n\ge2}b_nz^n$ be analytic on $|z|<\rho$, put $x=R/\rho<1$, and define $$P_R(f)=\sum_{n\ge2}|b_n|R^n.$$ Boundary $H^2$ norms use normalized angular measure.

# Hardy-dominant theorem

[\[thm:hardy\]]{#thm:hardy label="thm:hardy"} For every $f\in H^2(\rho)$, $$P_R(f)\le
 \|f\|_{H^2(\rho)}\frac{x^2}{\sqrt{1-x^2}}.$$ In particular, for $f\in H^\infty(\rho)$, $$P_R(f)\le
 \|f\|_{H^\infty(\rho)}\frac{x^2}{\sqrt{1-x^2}}.$$ The $H^2$ constant is exact. If $\rho=Re^\eta$, then the best uniform order on the $H^\infty$ unit ball is also $\Theta(\eta^{-1/2})$ as $\eta\downarrow0$.

Write $u_n=|b_n|\rho^n$. Cauchy--Schwarz gives $$P_R(f)=\sum_{n\ge2}u_nx^n
 \le\left(\sum_{n\ge2}u_n^2\right)^{1/2}
 \left(\sum_{n\ge2}x^{2n}\right)^{1/2},$$ which is the first estimate. The second uses $\|f\|_{H^2}\le\|f\|_{H^\infty}$. Equality in the Hilbert-space estimate is obtained by taking the boundary-scaled coefficient vector proportional to $(x^n)_{n\ge2}$.

For the $H^\infty$ lower order, let $N=2^m$ and choose Rudin--Shapiro signs $\varepsilon_0,\ldots,\varepsilon_{N-1}$ with $$\sup_{|w|=1}\left|\sum_{j=0}^{N-1}\varepsilon_jw^j\right|
 \le\sqrt{2N}.$$ Then $$f_N(z)=\frac1{\sqrt{2N}}
 \sum_{j=0}^{N-1}\varepsilon_j(z/\rho)^{j+2}$$ has $H^\infty(\rho)$ norm at most one and $$P_R(f_N)=
 \frac{x^2(1-x^N)}{\sqrt{2N}(1-x)}.$$ Choose a dyadic $N$ with $(2\eta)^{-1}\le N\le\eta^{-1}$. Since $x=e^{-\eta}$, the last expression is bounded below by $c\eta^{-1/2}$. The Hardy upper bound is asymptotic to $(2\eta)^{-1/2}$, proving the order.

# Constants and protocol

At $R=1.4$, $\rho=1.41$, $$\frac{x^2}{1-x}=139.0070921986\ldots,\qquad
 \frac{x^2}{\sqrt{1-x^2}}=8.2924678943\ldots.$$ The computation evaluates the Hardy scale and admissible dyadic Rudin--Shapiro lower examples at $\eta=10^{-1},10^{-2},10^{-3}$, using lengths $8,64,512$. Non-dyadic lengths are rejected by the implementation because the displayed normalization is then not certified by the standard identity.

This theorem optimizes the conversion of a known norm into an absolute coefficient budget. It does not prove that the actual $g_\sigma$ norm decays. Gates A--E remain false/open and no Hilbert--Polya or RH statement follows.
