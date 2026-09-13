---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-265-certified-deterministic-tail-ladder"
canonical_tex: "zeta_mvp0/papers/RH-265-certified-deterministic-tail-ladder/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-265-certified-deterministic-tail-ladder/main.pdf"
source_sha256: "98cf2d9694db91f4ea8c7fe341d4ecbd37f52d70336bfce8c76364d1812215fb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Certified First-Omitted-Order Ladder for the Deterministic Tail

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-265-certified-deterministic-tail-ladder>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-265-certified-deterministic-tail-ladder/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-265-certified-deterministic-tail-ladder/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-265-certified-deterministic-tail-ladder/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-265-certified-deterministic-tail-ladder/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We organize the direct factorwise target-tail estimate into a certified ladder of first omitted orders. Arb replay gives explicit logarithmic and multiplicative budgets for $N=13,21,29,37,45,53,61$. Only $N=29$ matches the currently archived order-28 deterministic head; higher rows are conditional interfaces, not newly constructed heads. The ladder is a target-side result and leaves the cloud bridge and uniform quotient theorem open.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'A Certified First-Omitted-Order Ladder for the Deterministic Tail'
```

## Markdown 正文

# Definition of the ladder

Let $E_N$ denote the direct factorwise upper bound for $\sum_{n\ge N}|a_n|/n$ from RH-264 [@WangRH264]. We restrict to odd $N$ so that the even trace threshold is $(N+1)/2$ and the odd endpoint series starts at $N$.

For the fixed unit disk and the RH-13 certificate, the direct majorants satisfy $E_{N'}<E_N$ whenever $N'>N$ are successive listed orders. The same holds for $\exp(E_N)-1$.

Each component is a positive tail of an absolutely convergent majorant. The first omitted order increases, so every component decreases; the exponential map is increasing on the nonnegative reals.

# Certified values

The 100- and 200-decimal Arb replays evaluate the same outward interval expressions independently. The resulting safe endpoints are

    $N$            $E_N$                   $\exp(E_N)-1$
  ----- --------------------------- ---------------------------
     13  $<2.3243607\times10^{-2}$   $<2.3515845\times10^{-2}$
     21   $<8.73261\times10^{-4}$     $<8.73642\times10^{-4}$
     29  $<2.6624745\times10^{-5}$   $<2.6625100\times10^{-5}$
     37   $<9.32147\times10^{-7}$     $<9.32147\times10^{-7}$
     45  $<4.432615\times10^{-8}$    $<4.432615\times10^{-8}$
     53  $<1.705725\times10^{-9}$    $<1.705725\times10^{-9}$
     61  $<7.175542\times10^{-11}$   $<7.175542\times10^{-11}$

The RH-253 head through order 28 and the $N=29$ row form a certified deterministic target-side interface with logarithmic tail below $2.6624745\times10^{-5}$. No head through order 36 is present in the archive, so the rows $N\ge37$ are conditional interfaces only.

The order-28 extent is the finite dictionary of RH-253 [@WangRH253]; the $N=29$ bound is RH-264. The remaining rows are evaluated by the same analytic majorant but require coefficients not claimed here.

This ladder is not a cloud envelope, a selector, or a uniform quotient theorem. The five obligation vector remains $(0,0,0,1,1)$; all Gates A--E, Hilbert--Polya claims, zeta-divisor equality, and RH implications remain false/open.
