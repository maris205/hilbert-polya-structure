---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-289-finite-moment-shell-nonidentifiability"
canonical_tex: "zeta_mvp0/papers/RH-289-finite-moment-shell-nonidentifiability/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-289-finite-moment-shell-nonidentifiability/main.pdf"
source_sha256: "4ffe4e755d583e86ff1987fe529dcbfe2359f8d8b7475375b777b19def20bf01"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Moment Nonidentifiability by Hidden Root-of-Unity Shells

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-289-finite-moment-shell-nonidentifiability>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-289-finite-moment-shell-nonidentifiability/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-289-finite-moment-shell-nonidentifiability/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-289-finite-moment-shell-nonidentifiability/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-289-finite-moment-shell-nonidentifiability/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Growing coefficient prefixes do not by themselves identify a spectral cloud. For every prescribed prefix length $N$, we construct a conjugation-symmetric shell whose power sums vanish through order $N$ but whose next selected moment is nonzero. Appending the shell to any spectral multiset preserves the entire observed prefix while multiplying the regularized determinant by $1-(\gamma z)^L$ for some $L>N$. Thus arbitrarily long finite agreement is compatible with a new divisor immediately beyond the checked window. The result is scoped: weighted tail bounds, root transport, or contour control can exclude the construction. It shows exactly why the rate-free prefix theorem of RH-287 cannot replace the weighted gluing leaf of RH-288.
author:
- Bin Wang
date: July 2026
title: 'Finite-Moment Nonidentifiability by Hidden Root-of-Unity Shells'
```

## Markdown 正文

# Hidden shell

Fix $L\ge2$ and $\gamma>0$. Let $$\mathcal S_{L,\gamma}
 =\{\gamma e^{2\pi i j/L}:0\le j<L\}.$$ This multiset is closed under conjugation.

[\[thm:shell\]]{#thm:shell label="thm:shell"} For every integer $n\ge1$, $$\sum_{\zeta\in\mathcal S_{L,\gamma}}\zeta^n
 =L\gamma^n\mathbf1_{L\mid n}.$$ Consequently, if $L>N$, every power sum through order $N$ vanishes, while the order-$L$ sum equals $L\gamma^L$.

Factor out $\gamma^n$ and sum the finite geometric progression $\sum_{j=0}^{L-1}e^{2\pi i jn/L}$.

The genus-one shell factor is $$\prod_{\zeta\in\mathcal S_{L,\gamma}}
 (1-z\zeta)e^{z\zeta}=1-(\gamma z)^L.$$

The linear exponential terms cancel because the first shell moment is zero. The remaining polynomial identity is the factorization of $1-(\gamma z)^L$ over the $L$th roots of unity.

# Nonidentifiability consequence

Let $C$ be any finite spectral multiset and set $\widetilde C=C\sqcup\mathcal S_{L,\gamma}$. If $L>N$, then $$\sum_{\lambda\in C}\lambda^n
 =\sum_{\lambda\in\widetilde C}\lambda^n,
 \qquad1\le n\le N,$$ but the associated canonical products differ by $1-(\gamma z)^L$. No rule reading only the first $N$ moments can distinguish them.

The same construction can be applied at a moving $N=N_\sigma$. Without a weighted estimate that suppresses $\gamma_\sigma^{L_\sigma}R^{L_\sigma}$, even a diverging prefix does not determine the analytic factor on $|z|\le R$.

This counterexample does not show that the physical folded Gaussian spectrum contains hidden shells. It only proves insufficiency of prefix data. A root-$\ell^1$, weighted-Fourier, or contour theorem would add information that the construction ignores. Gates A--E remain false/open.
