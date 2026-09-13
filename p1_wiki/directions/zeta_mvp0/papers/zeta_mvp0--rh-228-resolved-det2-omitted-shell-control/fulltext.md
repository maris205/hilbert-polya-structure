---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-228-resolved-det2-omitted-shell-control"
canonical_tex: "zeta_mvp0/papers/RH-228-resolved-det2-omitted-shell-control/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-228-resolved-det2-omitted-shell-control/main.pdf"
source_sha256: "c3e9ea4e12d1bad003a556d3122802df1596909f5a9257d0583abf0f2a5eae6e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Resolved Omitted-Shell Control for Regularized Determinants A Quantitative Unit-Disk Tail Bound

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-228-resolved-det2-omitted-shell-control>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-228-resolved-det2-omitted-shell-control/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-228-resolved-det2-omitted-shell-control/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-228-resolved-det2-omitted-shell-control/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-228-resolved-det2-omitted-shell-control/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The reciprocal local-count audit does not stabilize, but the Arnoldi window contains additional complete shells beyond every selected RH-222 cloud. This paper asks whether those resolved omitted shells are small in the second-regularized determinant.

  For $|w|<1$, $$|\log(1-w)+w|\le\frac{|w|^2}{2(1-|w|)}.$$ Consequently, if a finite omitted resonance multiset $T$ satisfies $q=R\max_{\lambda\in T}|\lambda|<1$, then on $|z|\le R$, $$\left|\sum_{\lambda\in T}
   [\log(1-z\lambda)+z\lambda]\right|
   \le \frac{R^2}{2(1-q)}
   \sum_{\lambda\in T}|\lambda|^2.$$ This gives a branch-consistent uniform bound for the omitted $\det_2$ logarithm.

  Each physical endpoint has 12--14 complete resolved roots beyond the selected cloud. On the closed unit disk, $q\le0.29818$. The maximum analytic upper bound is $0.16804$, the maximum observed 192-point grid tail is $0.07532$, and every bound has positive slack.

  The result controls the candidate-window tail only. It does not bound the unresolved infinite operator complement, and therefore does not establish a uniform small-noise determinant family.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Resolved Omitted-Shell Control for Regularized Determinants\
  A Quantitative Unit-Disk Tail Bound
```

## Markdown 正文

# Why second regularization helps

For a resonance multiset $T$, the finite second-regularized factor is $$\label{eq:factor}
 P_{T,2}(z)=
 \prod_{\lambda\in T}(1-z\lambda)e^{z\lambda}.$$ The exponential removes the linear term in the logarithm. Near $z=0$, the tail is therefore quadratic in the omitted resonances rather than linear.

This is the finite-product counterpart of the Hilbert--Schmidt determinant used at fixed noise in RH-7 [@WangRH7; @Simon2005]. It is exactly the regularization required when square summability is available but absolute summability is not.

# The logarithmic tail theorem

Choose the logarithm by analytic continuation from zero on a disk where no factor vanishes.

[\[lem:one\]]{#lem:one label="lem:one"} For $|w|<1$, $$\label{eq:one}
 |\log(1-w)+w|
 \le\frac{|w|^2}{2(1-|w|)}.$$

The convergent power series gives $$\log(1-w)+w=-\sum_{m=2}^{\infty}\frac{w^m}{m}.$$ Since $m^{-1}\le1/2$ for $m\ge2$, $$\sum_{m=2}^{\infty}\frac{|w|^m}{m}
 \le\frac12\sum_{m=2}^{\infty}|w|^m
 =\frac{|w|^2}{2(1-|w|)}.$$

[\[thm:tail\]]{#thm:tail label="thm:tail"} Let $T$ be a finite resonance multiset and let $$q=R\max_{\lambda\in T}|\lambda|<1.$$ Then the logarithm of [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"}, normalized to vanish at zero, satisfies $$\label{eq:bound}
 \sup_{|z|\le R}|\log P_{T,2}(z)|
 \le B_R(T):=
 \frac{R^2}{2(1-q)}\sum_{\lambda\in T}|\lambda|^2.$$

Apply Lemma [\[lem:one\]](#lem:one){reference-type="ref" reference="lem:one"} to $w=z\lambda$. Since $|z\lambda|\le q$, $$|\log(1-z\lambda)+z\lambda|
 \le\frac{|z|^2|\lambda|^2}{2(1-q)}.$$ Sum over $T$ and use $|z|\le R$.

[\[cor:mult\]]{#cor:mult label="cor:mult"} On the same disk, $$|P_{T,2}(z)-1|\le e^{B_R(T)}-1.$$

Write $P_{T,2}=e^L$ and use $|e^L-1|\le e^{|L|}-1$.

The logarithmic form is more informative when composing factors and comparing channels.

# Resolved selected and omitted shells

At one endpoint, let $$\Lambda_{\rm cand}
 =\Lambda_{\rm sel}\sqcup T_{\rm res}$$ be the complete-shell part of the Arnoldi candidate window, split after the RH-222 selected cloud. A nonreal candidate root whose conjugate lies outside the Arnoldi window is excluded from both sides; no synthetic partner is added.

Then $$\label{eq:split}
 P_{\Lambda_{\rm cand},2}
 =P_{\Lambda_{\rm sel},2}P_{T_{\rm res},2},$$ and Theorem [\[thm:tail\]](#thm:tail){reference-type="ref" reference="thm:tail"} controls the exact ratio of the two finite products.

Each endpoint contains 12--14 roots in $T_{\rm res}$. The count varies because real singleton shells and a possible incomplete candidate-boundary root alter parity.

# Physical unit-disk audit

The disk radius is frozen at $R=1$. The observed logarithmic tail is sampled at 48 angles on each of the radii $$0.25,\quad0.5,\quad0.75,\quad1.$$ The analytic bound itself holds at every point of the closed unit disk; the grid is used only to assess its slack.

  diagnostic                                      result
  ----------------------------------------- ------------
  endpoint count                                      32
  resolved omitted roots                          12--14
  grid points per endpoint                           192
  maximum $q$                                 $0.298172$
  maximum $\sum_{T_{\rm res}}|\lambda|^2$       archived
  maximum logarithmic upper bound             $0.168037$
  maximum observed grid log tail              $0.075315$
  minimum bound slack                         $0.011053$

Every omitted reciprocal zero has modulus at least $q^{-1}>3.35$ when $q$ is taken at its worst endpoint, so the unit disk is safely zero-free for every resolved omitted factor.

# What the result does not bound

The full bulk spectrum decomposes as $$\Lambda_{\rm bulk}
 =\Lambda_{\rm sel}\sqcup T_{\rm res}\sqcup T_{\rm unres}.$$ Theorem [\[thm:tail\]](#thm:tail){reference-type="ref" reference="thm:tail"} controls $T_{\rm res}$ because its roots are explicitly stored. It supplies no value for $$\sum_{\lambda\in T_{\rm unres}}|\lambda|^2.$$ At fixed noise, Hilbert--Schmidt theory guarantees that the infinite sum is finite and the truncations converge locally uniformly [@WangRH7; @Simon2005]. The missing requirement is a bound uniform as $\sigma\downarrow0$ after the chosen moving factors have been removed.

A whole-matrix Frobenius norm gives one formal upper bound on the unresolved eigenvalue square sum. The next paper tests it. Because the operators are nonnormal, that bound sees singular-direction mass that may be invisible to the resonance product and can be extremely pessimistic.

# Claim boundary

The exact advance is a quantitative omitted-shell theorem and its successful application to every resolved candidate window. It does not certify Arnoldi roots, control the unresolved complement, or prove a small-noise normal family. The failed local-count gate of RH-227 is not repaired merely by a small resolved tail [@WangRH227]. Gate A remains open.
