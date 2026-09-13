---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-297-natural-counterloop-alias-ledger"
canonical_tex: "zeta_mvp0/papers/RH-297-natural-counterloop-alias-ledger/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-297-natural-counterloop-alias-ledger/main.pdf"
source_sha256: "53ca0d065be5e85b054902e329f4c7ef8654210cc55c93b859b3acb7b79aca22"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The One- and Two-Alias Ledger at the Natural Counterloop Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-297-natural-counterloop-alias-ledger>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-297-natural-counterloop-alias-ledger/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-297-natural-counterloop-alias-ledger/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-297-natural-counterloop-alias-ledger/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-297-natural-counterloop-alias-ledger/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The finite-radius counterloop bridge is usually stated before its first alias. We compare that alias clock with both relevant weighted bridge cuts. If the counterloop period is tied to the intrinsic endpoint-resolution rank, then the minimal tail-absorbed cut crosses exactly one alias and the original slope-four cut crosses exactly two. The exact counterloop power ledger gives their absolute weighted sizes. Because $\beta R>1$, the first two impulses grow with explicit powers of $1/\sigma$. This does not prove that the actual typed errors diverge: noisy head or full-trace terms may cancel the shell impulses. It proves that a natural-rank bridge must be alias-inclusive or aggregate, rather than a direct reuse of fixed pre-alias moments.
author:
- Bin Wang
date: July 2026
title: 'The One- and Two-Alias Ledger at the Natural Counterloop Clock'
```

## Markdown 正文

# Clock comparison

Let $$k_\sigma=\frac{L_\sigma}{2\log\lambda}+O(1),\qquad
 L_\sigma=\log(1/\sigma),$$ be the RH-16 endpoint-resolution clock, and suppose the counterloop period is chosen on this scale. Put $$h_\sigma=\left\lceil\frac{L_\sigma}{\log(10/7)}\right\rceil,\qquad
 m_\sigma=\lceil4L_\sigma\rceil.$$ The exact counterloop moment is $$s_{k,n}=\beta_k^n
 \bigl(2k\,\mathbf1_{2k\mid n}-1-(-1)^n\bigr),
\qquad
 \beta_k\to\beta=\frac1{0.85\sqrt\lambda}.$$

# Alias theorem

[\[thm:aliases\]]{#thm:aliases label="thm:aliases"} For all sufficiently small $\sigma$, $$2k_\sigma<h_\sigma<4k_\sigma<m_\sigma<6k_\sigma.$$ Thus the prefix below $h_\sigma$ contains the first alias order $2k_\sigma$ but not $4k_\sigma$, while the prefix below $m_\sigma$ contains the first two alias orders but not $6k_\sigma$. At $n=2\ell k$, $$\frac{|s_{k,2\ell k}|R^{2\ell k}}{2\ell k}
 =\frac{1-k^{-1}}{\ell}(\beta_kR)^{2\ell k}.$$ For $R=7/5$ and $\ell=1,2$, these quantities have logarithmic growth exponents $$\chi_\ell=
 \frac{\ell\log(\beta R)}{\log\lambda},
\quad
 \chi_1=0.463406944517003\ldots,\quad
 \chi_2=0.926813889034006\ldots.$$

The alias orders $2\ell k_\sigma$ have slopes $\ell/\log\lambda$. Direct calculation gives $$\begin{aligned}
 \frac1{\log\lambda}=1.930709\ldots
 &<\frac1{\log(10/7)}=2.803673\ldots\\
 &<\frac2{\log\lambda}=3.861418\ldots
 <4<\frac3{\log\lambda}=5.792128\ldots.
\end{aligned}$$ The exact moment formula at a multiple of $2k$ reduces to $(2k-2)\beta_k^{2\ell k}$, proving the weighted identity. Since $\beta_k\to\beta$ and $k_\sigma=L_\sigma/(2\log\lambda)+O(1)$, taking logarithms and dividing by $L_\sigma$ gives $\chi_\ell$.

# Protocol and scope

The computation reports all five slopes, the alias counts below each bridge cut, $\beta R$, and the first two growth exponents. It also evaluates the exact limiting-radius impulse formula for moderate integer $k$.

RH-16 proves an endpoint singular-value rank, not equality with the noisy modulus-head cardinality. The clock identification in this paper is therefore a typed route audit. Moreover, a large shell term can cancel against a large noisy term; no lower bound for $E_\sigma$ or $D_\sigma$ is claimed. Gates A--E remain false/open.
