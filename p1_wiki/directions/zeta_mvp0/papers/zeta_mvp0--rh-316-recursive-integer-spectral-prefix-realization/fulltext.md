---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-316-recursive-integer-spectral-prefix-realization"
canonical_tex: "zeta_mvp0/papers/RH-316-recursive-integer-spectral-prefix-realization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-316-recursive-integer-spectral-prefix-realization/main.pdf"
source_sha256: "7cd752a8910d7ef378fd63c5a05ca9d22b05265a1e082b6ecd3043ae51d1aa3f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Recursive Integer Spectra for Exact Deterministic Moment Prefixes

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-316-recursive-integer-spectral-prefix-realization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-316-recursive-integer-spectral-prefix-realization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-316-recursive-integer-spectral-prefix-realization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-316-recursive-integer-spectral-prefix-realization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-316-recursive-integer-spectral-prefix-realization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The isolated packets of RH-315 can be iterated because the order-$d$ packet does not alter any lower moment. We obtain a finite conjugate-closed spectrum inside the modulus cap whose power sums match any prescribed finite real prefix exactly. All multiplicities are integers, so the construction is a finite normal matrix rather than a weighted measure. It remains synthetic and is not identified with the actual noisy operator.
author:
- Bin Wang
date: July 2026
title: Recursive Integer Spectra for Exact Deterministic Moment Prefixes
```

## Markdown 正文

# Triangular construction

Fix $q>0$ and real moments $a_1,\ldots,a_N$. Begin with the empty multiset. After steps $1,\ldots,d-1$, let $$w_d=a_d-\sum_{\mu\in\mathcal S_{d-1}}\mu^d.$$ If $w_d\ne0$, choose $$L_d\ge |w_d|/(dq^d)$$ and adjoin the packet $\mathcal P_d(w_d,L_d)$ of RH-315.

The final multiset $\mathcal S_N$ is finite, conjugate closed, and contained in $|\mu|\le q$. For every $1\le n\le N$, $$\sum_{\mu\in\mathcal S_N}\mu^n=a_n.$$ Thus $\mathcal S_N$ is the spectrum of a finite normal matrix with integer multiplicities and the exact prescribed power-sum prefix.

At step $d$, the new packet has moment $w_d$ at order $d$ and zero moments at all lower orders. Induction therefore fixes the $d$th moment without disturbing the preceding ones. The radius criterion and conjugate closure hold packet by packet. A diagonal matrix with these entries is normal.

# Application to the deterministic anchor

Taking $a_n$ to be the RH-263 all-order deterministic numerator anchors gives an exact finite spectral realization for every prefix. The construction is not fitted from the RH-253 table; that table is unnecessary once the all-order anchors are known.

The reproducibility experiment reads the archived RH-263 anchor rows through order eight and runs the packet recursion in floating arithmetic. This is a finite implementation check of the exact theorem, not evidence for an all-order noisy spectral fit.

Finite normal realizability does not prove that the actual noisy complement has these eigenvalues, this rank, or this moment transport. Gates A--E remain false/open.
