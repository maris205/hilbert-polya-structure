---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-237-dual-channel-trace-jet-coherence"
canonical_tex: "zeta_mvp0/papers/RH-237-dual-channel-trace-jet-coherence/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-237-dual-channel-trace-jet-coherence/main.pdf"
source_sha256: "381b7d1da926a377ddb1d48a76aefa2727bff7a829b9f3cce4973e7697763405"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Dual-Channel Coherence of Cloud-Extracted Determinant Jets

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-237-dual-channel-trace-jet-coherence>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-237-dual-channel-trace-jet-coherence/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-237-dual-channel-trace-jet-coherence/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-237-dual-channel-trace-jet-coherence/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-237-dual-channel-trace-jet-coherence/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-236 replaces the divergent complement Frobenius budget by cloud-extracted trace moments through order twelve. We test whether those moments are stable under the independent fine and Haar-coarse discretizations. For two trace vectors $\tau,\eta$, define $$d_{m,R}(\tau,\eta)
   =\sum_{n=2}^{m}\frac{|\tau_n-\eta_n|}{n}R^n.$$ This seminorm bounds the difference of their truncated logarithmic determinant jets on $|z|\le R$.

  At $R=0.5$, $0.75$, and $1$, the maximum fine/coarse distances over all 16 noise levels are $0.00347$, $0.00789$, and $0.01415$. All unit-disk cases pass the frozen $0.02$ gate. This agrees with, and slightly sharpens at the coefficient level, the selected-product coherence found in RH-230. It does not control the all-order determinant tail or establish convergence between different noise levels.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'Dual-Channel Coherence of Cloud-Extracted Determinant Jets'
```

## Markdown 正文

# A metric for finite logarithmic germs

The regularized determinant starts at order two. Hence the first trace is a nuisance for the present comparison and is deliberately ignored.

[\[prop:distance\]]{#prop:distance label="prop:distance"} For $$L_\tau^{(m)}(z)=-\sum_{n=2}^m\frac{\tau_n}{n}z^n,$$ one has $$\sup_{|z|\le R}|L_\tau^{(m)}(z)-L_\eta^{(m)}(z)|
 \le d_{m,R}(\tau,\eta).$$ Moreover $d_{m,R}$ is a seminorm distance and is nondecreasing in $R$.

Apply the triangle inequality term by term. Homogeneity, symmetry, and the triangle inequality follow from the absolute value. Monotonicity follows because every order is at least two and all coefficients in the bound are nonnegative.

The metric is branch-free: it compares Taylor coefficients rather than choosing logarithm branches on a grid.

[\[cor:radius\]]{#cor:radius label="cor:radius"} For $0\le r\le R$ with $R>0$, $$d_{m,r}(\tau,\eta)
 \le \left(\frac rR\right)^2d_{m,R}(\tau,\eta).$$ Moreover, for every $2\le n\le m$, $$|\tau_n-\eta_n|
 \le \frac{n}{R^n}d_{m,R}(\tau,\eta).$$

Since $n\ge2$, one has $r^n\le(r/R)^2R^n$. Summing gives the first inequality. Each nonnegative summand in $d_{m,R}$ is at most the full sum, which gives the second.

Thus a unit-disk gate controls every archived trace coefficient and yields strictly stronger determinant-jet control on smaller disks. It does not, however, say anything about coefficient number thirteen.

# Two discretization channels

The left channel uses the fine folded Gaussian matrix. The right channel compresses the same matrix by the Haar embedding used in RH-222 [@WangRH222]. Both channels use the same Hardy scaling, peripheral subtraction, and shell-complete cloud schedule. Thus their distance tests discretization sensitivity rather than a change of normalization.

    Radius $R$   cases   maximum $d_{12,R}$
  ------------ ------- --------------------
        $0.50$      16          $0.0034706$
        $0.75$      16          $0.0078827$
        $1.00$      16          $0.0141455$

  : Dual-channel cloud-extracted trace-jet distances.

The maxima conceal substantial nonmonotonicity in the noise. Representative values are

     $\sigma$            $d_{12,0.5}$           $d_{12,0.75}$              $d_{12,1}$
  ----------- ----------------------- ----------------------- -----------------------
    $0.04000$   $3.1051\times10^{-4}$   $7.8680\times10^{-4}$   $1.5824\times10^{-3}$
    $0.01600$   $2.9875\times10^{-3}$   $6.7780\times10^{-3}$   $1.2170\times10^{-2}$
    $0.00800$   $3.3325\times10^{-3}$   $7.6794\times10^{-3}$   $1.3986\times10^{-2}$
    $0.00500$   $1.0407\times10^{-4}$   $2.3650\times10^{-4}$   $4.2476\times10^{-4}$
    $0.00400$   $1.4396\times10^{-5}$   $3.7271\times10^{-5}$   $7.5326\times10^{-5}$
    $0.00200$   $3.4706\times10^{-3}$   $7.8827\times10^{-3}$   $1.4145\times10^{-2}$
    $0.00125$   $3.0669\times10^{-3}$   $6.9087\times10^{-3}$   $1.2300\times10^{-2}$

  : Representative channel discrepancies, showing shell-transition spikes rather than monotone mesh convergence.

All unit-disk distances are below $0.02$. The maximum is also below the $0.01786$ selected-product grid difference reported by RH-230, although the two quantities are not identical: one is a finite coefficient majorant and the other is an observed grid supremum [@WangRH230].

# Coherence is not small-noise convergence

Let $\tau^L_\sigma$ and $\tau^R_\sigma$ denote the two channels. The present test bounds $d(\tau^L_\sigma,\tau^R_\sigma)$ at a common noise. A Cauchy theorem for the left channel would instead require bounds on $d(\tau^L_\sigma,\tau^L_{\sigma'})$. The triangle inequality gives $$d(\tau^R_\sigma,\tau^R_{\sigma'})
 \le d(\tau^R_\sigma,\tau^L_\sigma)
    +d(\tau^L_\sigma,\tau^L_{\sigma'})
    +d(\tau^L_{\sigma'},\tau^R_{\sigma'}),$$ so channel coherence can transfer a genuine convergence estimate from one channel to the other. It cannot create the middle estimate.

This distinction explains the role of the $0.02$ gate. It is a robustness test against discretization choice, not a fitted convergence rate and not an asymptotic error bar. The spikes in the second table occur near changes in the selected shell rank and are therefore useful diagnostics for the adaptive selection rule of RH-238.

# Interpretation

The positive conclusion is that the small trace jet of RH-236 is not an artifact of one mesh. Both channels resolve nearly the same first eleven nontrivial logarithmic coefficients. This justifies using the trace jet as a selection criterion in RH-238.

There are three explicit limits:

1.  the calculation stops at order twelve;

2.  the unit-disk bound is a triangle majorant, not an interval supremum;

3.  channel coherence at fixed noise does not imply adjacent-noise contraction.

In particular no full relative determinant, zero divisor, or small-noise limit is identified. Gate A and the Hilbert--Polya route remain open.
