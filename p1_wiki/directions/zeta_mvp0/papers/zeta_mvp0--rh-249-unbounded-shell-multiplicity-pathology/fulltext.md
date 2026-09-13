---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-249-unbounded-shell-multiplicity-pathology"
canonical_tex: "zeta_mvp0/papers/RH-249-unbounded-shell-multiplicity-pathology/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-249-unbounded-shell-multiplicity-pathology/main.pdf"
source_sha256: "2d13af4275027481af90847f751090345357dd5a16d46d033ee085fa566db10a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Unbounded Shell-Multiplicity Pathology

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-249-unbounded-shell-multiplicity-pathology>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-249-unbounded-shell-multiplicity-pathology/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-249-unbounded-shell-multiplicity-pathology/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-249-unbounded-shell-multiplicity-pathology/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-249-unbounded-shell-multiplicity-pathology/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We relax the RH-248 single-use shell zonotope to the full nonnegative cone. Six of 32 frozen endpoints remain outside the anchored tolerance, with primal--dual certificates. The other 26 can be fitted only by shell weights whose minimum necessary maxima range from $40.58$ to $5.80\times10^{10}$. Such arbitrary real multiplicities are not a spectral cloud. The formal success is therefore a moment-reweighting pathology, not coefficient identification.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Unbounded Shell-Multiplicity Pathology'
```

## Markdown 正文

# Cone relaxation and dual

Retain the real shell power matrix $V$, target difference $d$, and weights $\omega_n=1/n$ from RH-248 [@WangRH248]. Remove the upper bounds on shell use and define $$\label{eq:cone}
 \delta_+=\min_{w\ge0}\sum_{n=2}^{12}omega_n|d_n-(Vw)_n|.$$

[\[thm:dual\]]{#thm:dual label="thm:dual"} The cone distance satisfies $$\label{eq:dual}
 \delta_+=
 \max_{\substack{|y_n|\le\omega_n\\V^Ty\le0}}y^Td.$$ Thus any feasible dual vector with value greater than $\sigma$ excludes all nonnegative shell weights, regardless of their size.

Dualize the weighted $\ell^1$ residual as in RH-248. The infimum of $-y^TVw$ over $w\ge0$ is finite exactly when $V^Ty\le0$, in which case it is zero. Finite-dimensional LP strong duality gives [\[eq:dual\]](#eq:dual){reference-type="eqref" reference="eq:dual"}.

For endpoints with $\delta_+\le\sigma$, a second LP quantifies the pathology: $$\label{eq:cap}
 W_*=\min\{W:\ 0\le w_j\le W,
 \ \sum_n\omega_n|d_n-(Vw)_n|\le\sigma\}.$$ This is the smallest possible maximum shell weight, not the weight of an arbitrary optimal cone solution.

# Finite result

The frozen RH-222 windows and RH-243 anchor give 26 cone passes and six failures [@WangRH222; @WangRH243]. The failing endpoints are $$(0.04,L),\ (0.02,L),\ (0.02,R),\ (0.016,R),\
 (0.00625,L),\ (0.00625,R).$$ Their smallest distance-minus-tolerance margin is $2.826242139956541\times10^{-4}$, while the maximum recorded primal--dual gap is $4.08\times10^{-7}$. Hence the finite separation is much larger than the LP consistency error.

For the 26 formal passes, solving [\[eq:cap\]](#eq:cap){reference-type="eqref" reference="eq:cap"} gives $$40.58443731031147\le W_*
 \le58018432630.629776.$$ Seventeen cone fits can drive the order-12 jet objective to floating zero, yet may still require thousands to billions of repetitions. With the common cap $W=40$, no endpoint passes; at $W=41$, exactly one endpoint passes.

  quantity                                                 value
  ----------------------------------- --------------------------
  unbounded cone passes/failures                          26 / 6
  minimum required cap among passes                   40.5844373
  maximum required cap among passes     $5.8018433\times10^{10}$
  passes with cap 40                                        0/32
  passes with cap 41                                        1/32

# Interpretation and boundary

An algebraic spectral multiset has fixed nonnegative integer multiplicities. The variables in [\[eq:cone\]](#eq:cone){reference-type="eqref" reference="eq:cone"} are arbitrary real repetitions of already resolved shells, often enormous. They alter the moment problem without constructing a corresponding noisy operator or invariant root space. The 26 LP passes therefore do not supply the RH-243 coefficient bridge.

The six failures and multiplicity explosion concern only the frozen candidate windows and orders 2--12. They do not exclude expanded windows, deeper roots, signed/complex quotient grouping, or continuum mechanisms. No all-order envelope follows. Gate A remains open and Gates B--E are untouched; no Hilbert--Polya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is claimed.
