---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-253-extended-deterministic-anchor-atlas"
canonical_tex: "zeta_mvp0/papers/RH-253-extended-deterministic-anchor-atlas/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-253-extended-deterministic-anchor-atlas/main.pdf"
source_sha256: "ca164ecec26bf053ac0a997da3541b82d9a9b8a844d5da81d63f677d24cb4b5e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Extended Deterministic Numerator Anchor Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-253-extended-deterministic-anchor-atlas>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-253-extended-deterministic-anchor-atlas/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-253-extended-deterministic-anchor-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-253-extended-deterministic-anchor-atlas/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-253-extended-deterministic-anchor-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The analytic-tail theorem of RH-252 is exact but does not identify the finite target coefficients beyond the order-12 table of RH-243. We evaluate the same deterministic periodic-point formula through order $28$. This adds 16 orders and enumerates $32767$ physical fixed points at the largest order. The new order block contributes $0.0021942543$ to the unit-disk logarithmic norm, and its descriptive log-linear root rate is $0.7009986$. These are finite reproducible facts. They do not prove a uniform trace envelope, a cloud coefficient bridge, or any statement about Riemann zeros.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: Extended Deterministic Numerator Anchor Atlas
```

## Markdown 正文

# Exact target dictionary

Let $P_n$ denote the deterministic flat periodic trace from the quadratic band-merging map. The RH-243 dictionary is $$a_n=r_H^{-n}\left[P_n-1-(-1)^n+2\mathbf 1_{2\mid n}\lambda^{-n/2}\right],
 \qquad r_H=0.85,
 \label{eq:anchor}$$ with $\lambda=1.6785735104283177\ldots$ [@WangRH243]. The periodic point and multiplier formulas used to evaluate $P_n$ are the exact finite formulas archived with the Collet--Eckmann completion [@WangRH11].

[\[prop:finite\]]{#prop:finite label="prop:finite"} For every integer $2\le n\le28$, equation [\[eq:anchor\]](#eq:anchor){reference-type="eqref" reference="eq:anchor"} defines an exact finite deterministic target value. The order-$28$ computation enumerates $32767$ distinct physical fixed points before summing their flat weights.

The inverse-branch construction in RH-11 enumerates all cyclic Markov words, removes the duplicated shared endpoint, and verifies the physical fixed-point count. Applying the displayed finite sum for each order and then the explicit algebraic correction in [\[eq:anchor\]](#eq:anchor){reference-type="eqref" reference="eq:anchor"} gives the claim.

# The new order block

The following values are representative rows from the 16 new orders. The last column is the Hardy-scaled target, not a noisy trace.

    $n$        $P_n$   unscaled $g_n$          $a_n$
  ----- ------------ ---------------- --------------
     13   0.00118921       0.00118921     0.00983586
     16   1.96851809      0.000250789     0.00337758
     20   1.98876937     0.0000316550    0.000816703
     24   1.99600689    0.00000399130    0.000197269
     28   1.99858189   0.000000502810   0.0000476073

For the unit disk and the logarithmic norm $$J_{I}(1):=\sum_{n\in I}\frac{|a_n|}{n},
 \label{eq:norm}$$ the archived computation gives $$\begin{aligned}
 J_{2:12}(1)&=0.49450543569144195,\\
 J_{13:28}(1)&=0.0021942543215719553,\\
 J_{2:28}(1)&=0.496699690013014.
 \label{eq:values}\end{aligned}$$ At radius $0.8$, the new block contributes only $8.7150803572\times10^{-5}$.

# Finite slope diagnostic and its boundary

Fitting $\log|a_n|$ linearly against $n$ on the new block gives $$\widehat q_{13:28}=0.7009986349256669,
 \quad
 \widehat q_{\rm odd}=0.7009206511866494,
 \quad
 \widehat q_{\rm even}=0.7011096165507584.
 \label{eq:fit}$$ The agreement between parity subsequences is a useful finite consistency check with the RH-252 radius budget [@WangRH252]. It is not a proof of $|a_n|\le Cq^n$ for all $n$: a finite fit has no control over orders $29$ and beyond, nor over the constant needed in the Cauchy tail theorem.

The atlas is deterministic and finite. It does not select a noisy spectral cloud, certify a quotient block, or identify the coefficients of a moving operator. The target is an anchor, not an observed eigenvalue list.

# Route decision

RH-252 provides an all-order analytic existence statement for the target tail, while this paper supplies a longer finite target table. The next genuinely new input must come from the spectral side: an expanded resolved candidate window or an invariant quotient selector. Reusing the frozen RH-248 shell window would not be progress. Gates A--E remain false/open; no Hilbert--Polya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is asserted.
