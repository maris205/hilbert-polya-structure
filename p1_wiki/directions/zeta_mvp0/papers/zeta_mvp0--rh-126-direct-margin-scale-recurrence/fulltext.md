---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-126-direct-margin-scale-recurrence"
canonical_tex: "zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence/main.pdf"
source_sha256: "e182ddf74b128a6d5d035cb66bf34c0b6ea476fbc7fdf632ec09f19eb257c116"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Direct-Margin Scale Recurrence A Sharp Weyl Law and a Five-Scale Scalar-Alignment Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a threshold $\tau$, define the direct support margin $m_\tau(K)=s_4(K)-\tau s_1(K)$. If, after unitary alignment and a scalar scale $c\geq0$, the operator error is at most $\varepsilon$, then $$m_\tau(K')\geq c\,m_\tau(K)-(1+\tau)\varepsilon.$$ The coefficients are sharp. We also compute the optimal scalar Chebyshev fit of finite singular profiles. On 96 phase-matched archived pairs, only 26 endpoint fits and 6 four-mode fits retain a positive one-step lower; none of 24 endpoint chains remains positive through all five scales. Thus the direct recurrence is rigorous, but the simplest scalar-alignment mechanism is a poor finite route compared with RH-125.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Direct-Margin Scale Recurrence\
  A Sharp Weyl Law and a Five-Scale Scalar-Alignment Barrier
```

## Markdown 正文

# Sharp recurrence

[\[thm:margin\]]{#thm:margin label="thm:margin"} Suppose $\|K'-cUKV\|\leq\varepsilon$ for unitaries $U,V$ and $c\geq0$. Then for every $\tau\geq0$, $$m_\tau(K')\geq c\,m_\tau(K)-(1+\tau)\varepsilon.$$

Weyl--Mirsky perturbation gives $s_4(K')\geq cs_4(K)-\varepsilon$ and $s_1(K')\leq cs_1(K)+\varepsilon$ [@HornJohnson1991]. Subtraction proves the result.

The bound is sharp: take a diagonal operator with separated singular values and perturb its leading entry upward by $\varepsilon$ and its fourth entry downward by $\varepsilon$.

If $m_{n+1}\geq c_nm_n-(1+\tau)\varepsilon_n$, then $$m_N\geq\Bigl(\prod_{j<N}c_j\Bigr)m_0-(1+\tau)
\sum_{k<N}\varepsilon_k\prod_{j=k+1}^{N-1}c_j.$$

# Optimal scalar profile fit

For positive profiles $s,t$, minimize $\varepsilon(c)=\max_j|t_j-cs_j|$ over $c\geq0$. Feasibility at radius $\varepsilon$ is exactly the interval intersection $$\max_j\frac{t_j-\varepsilon}{s_j}\leq c\leq
\min_j\frac{t_j+\varepsilon}{s_j},\qquad c\geq0.$$ This gives a monotone bisection with a certified minimax residual. We use both the endpoint profile $(s_1,s_4)$, which contains exactly the margin information, and the stronger four-mode profile.

# Five-scale barrier

The RH-121 archive supplies 96 adjacent pairs. Every computed recurrence lower is dominated by the target margin. There are zero dominance failures. Yet only 26 endpoint fits retain a positive lower, and only 6 full-profile fits do. Iterating the endpoint recurrence along 24 side--threshold--phase chains leaves zero positive terminal margins; the terminal range is approximately $[-1.40\times10^{-2},-8.45\times10^{-11}]$.

![Best scalar-profile errors and propagated direct margins.](<../../../../../zeta_mvp0/papers/RH-126-direct-margin-scale-recurrence/figures/direct_margin_scale_recurrence.pdf>){width="\\textwidth"}

This is a finite negative result about scalar alignment, not a proof that every direct physical recurrence is impossible. An operator-valued source law could still succeed. The directional route remains primary, and RH-127 adds the outward guards it needs. No uniform Stage A, Hilbert--Polya, zeta-zero, or Riemann Hypothesis claim is made.
