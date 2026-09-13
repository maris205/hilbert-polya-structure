---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-260-updated-anchored-head-tail-certificate-ledger"
canonical_tex: "zeta_mvp0/papers/RH-260-updated-anchored-head-tail-certificate-ledger/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-260-updated-anchored-head-tail-certificate-ledger/main.pdf"
source_sha256: "8f6d1f4c4923ac1e8894e61295780d6ebfc58c1ff96f86ea3dd117e06dba5f04"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Updated Anchored Head--Tail Certificate Ledger

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-260-updated-anchored-head-tail-certificate-ledger>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-260-updated-anchored-head-tail-certificate-ledger/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-260-updated-anchored-head-tail-certificate-ledger/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-260-updated-anchored-head-tail-certificate-ledger/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-260-updated-anchored-head-tail-certificate-ledger/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We update the exact finite-head/analytic-tail interface after four distinct inputs. RH-252 gives an all-order analytic existence interface for the deterministic target, but its boundary constant $M_S$ is not numerically certified. RH-255 and RH-258 find no anchored head in their two expanded admissibility classes at any of 32 endpoints. RH-259 supplies a finite 23-endpoint quotient block diagnostic whose worst root rate is $0.505642$, not a uniform small-noise theorem. We prove the updated gluing estimate and a scoped zero-certificate corollary: the current audited classes have exactly zero complete head--tail certificates. This is a route ledger, not a global nonexistence theorem.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Updated Anchored Head--Tail Certificate Ledger'
```

## Markdown 正文

# The updated certificate interface

Let $\tau_{n,\theta}$ be the residual trace coefficients produced by a candidate cloud or quotient at parameter $\theta$, and let $a_n$ be the deterministic target coefficients of RH-243 [@WangRH243]. Write $$L_\theta(z)=-\sum_{n\ge 2}\frac{\tau_{n,\theta}}{n}z^n,
 \qquad
 L_*(z)=-\sum_{n\ge 2}\frac{a_n}{n}z^n.
 \label{eq:logs}$$ For a first omitted order $N\ge 3$, define the three nonnegative budgets $$\begin{aligned}
 H_{<N}(\theta,R)&=\sum_{n=2}^{N-1}
     \frac{|\tau_{n,\theta}-a_n|R^n}{n},\\
 Q_{\ge N}(\theta,R)&=\sum_{n\ge N}
     \frac{|\tau_{n,\theta}|R^n}{n},\\
 A_{\ge N}(R)&=\sum_{n\ge N}
     \frac{|a_n|R^n}{n}.
 \label{eq:budgets}\end{aligned}$$ The convention matters: an order-$2$--$12$ head has $N=13$. This first-omitted-order formulation refines the bookkeeping interface of RH-250 [@WangRH250].

[\[thm:gluing\]]{#thm:gluing label="thm:gluing"} Assume the series in [\[eq:logs\]](#eq:logs){reference-type="eqref" reference="eq:logs"} are absolutely convergent on $|z|\le R$. Then $$|L_\theta(z)-L_*(z)|
 \le H_{<N}(\theta,R)+Q_{\ge N}(\theta,R)+A_{\ge N}(R).
 \label{eq:logbound}$$ If $H_{<N}\le h$, $Q_{\ge N}\le q$, and $A_{\ge N}\le t$ uniformly on a parameter set, and if $|L_*(z)|\le B_*$ there, then with $D_\theta=e^{L_\theta}$ and $D_*=e^{L_*}$, $$|D_\theta(z)-D_*(z)|
 \le e^{B_*}\bigl(e^{h+q+t}-1\bigr).
 \label{eq:detbound}$$ Consequently a sequence of complete certificates yields locally uniform determinant convergence whenever the three budgets tend uniformly to zero.

Subtract the two absolutely convergent series. The terms with $2\le n<N$ give the finite head $H_{<N}$; the remaining terms are bounded separately by the absolute quotient and target tails. This proves [\[eq:logbound\]](#eq:logbound){reference-type="eqref" reference="eq:logbound"}. For the determinant, put $\Delta=L_\theta-L_*$. Since $|L_*|\le B_*$, $$|e^{L_\theta}-e^{L_*}|
 =|e^{L_*}|\,|e^\Delta-1|
 \le e^{B_*}(e^{|\Delta|}-1),$$ and [\[eq:detbound\]](#eq:detbound){reference-type="eqref" reference="eq:detbound"} follows from [\[eq:logbound\]](#eq:logbound){reference-type="eqref" reference="eq:logbound"}.

[\[prop:target\]]{#prop:target label="prop:target"} RH-252 [@WangRH252] gives a scaled zero-free radius $$\rho_*=r_H\lambda=1.42678748386407\ldots>1,
 \qquad r_H=0.85.$$ For every $0\le R<S<\rho_*$, the normalized logarithm has a finite boundary supremum $M_S$ and $$A_{\ge N}(R)\le M_S\frac{(R/S)^N}{1-R/S}.
 \label{eq:targettail}$$ At $R=1$, $N=13$, and $S=1.35$, the geometric factor per $M_S$ is $0.07796985628233917$. The existence of $M_S$ is exact; no certified numerical upper bound for it is available in the archived audit.

This is the Cauchy estimate for the holomorphic logarithm on the disk supplied by RH-252. The coefficient of $z^n$ is $-a_n/n$, so summing the resulting geometric series gives [\[eq:targettail\]](#eq:targettail){reference-type="eqref" reference="eq:targettail"}. The final numerical factor is only the displayed geometric factor; multiplying it by a truncated boundary scan would not certify $M_S$.

# Scoped zero-certificate result

The head classes are deliberately kept separate. RH-255 uses a convex single-use shell box containing every prefix and binary shell subset. Its archived primal--dual audit has 0 passes at all 32 endpoints. RH-258 tests the unit-cap signed-integer lattice $\{-1,0,1\}^J$, with exact-integrality MILP solutions and zero reported MIP gap; it also has 0 passes at all 32 endpoints. Neither audit supplies an operator realization for an arbitrary mask [@WangRH255; @WangRH258].

[\[cor:zero\]]{#cor:zero label="cor:zero"} Restrict the candidate head to the union of the RH-255 box class and the RH-258 unit-cap signed-integer class, with the archived 32-endpoint tolerance protocol. There is no complete head--tail certificate in this restricted class.

Every complete certificate has, as a necessary first component, a passing anchored finite head. The RH-255 audit supplies 0/32 such passes and the RH-258 audit supplies 0/32. Therefore their union supplies no passing head, so the set of complete certificates is empty, independently of the tail budgets. This conclusion is scoped to the two archived classes and their finite tolerance protocol.

The two classes cover 64 class--endpoint cases. The RH-255 audit excludes $$62{,}030{,}604{,}700$$ eligible binary subsets through the box obstruction. RH-258's unit-cap lattice contains $$39{,}417{,}456{,}084{,}975{,}216$$ signed points in aggregate. These counts are finite audit descriptors, not claims about all possible selectors.

# Quotient-tail ledger

RH-259 extends the ordered-Schur quotient calculation to dimension 1024 [@WangRH246; @WangRH259]. All 23 audited twelfth powers are contractive, but the worst root rate is $$q_{12}=0.5056418005507071,$$ at the right channel with $\sigma=0.0025$ and dimension 1024. The finite unit-disk logarithmic tail diagnostic is $5.654507945432548\times10^{-4}$. Nine archived endpoints remain outside the calculation, and the floating matrix norms are not interval enclosures. Thus this is a family of finite diagnostics, not a uniform small-noise quotient certificate.

  ----------------------------------------------------------------------------
  certificate component                 archived status
  ------------------------------------- --------------------------------------
  deterministic target analytic tail    exact existence; $M_S$ not certified

  RH-255 expanded single-use head       0/32 passes

  RH-258 unit-cap signed-integer head   0/32 passes

  RH-259 quotient block tail            23 finite endpoints; uniformity open

  cloud coefficient bridge              open

  complete head--tail certificate       0
  ----------------------------------------------------------------------------

# Protocol, boundary, and next input

The experiment reads the four archived JSON ledgers, checks 44 source consistency predicates, and writes a new structured ledger. It does not rerun the dimension-1024 Schur calculation or fit new moments. The result therefore separates exact inherited interfaces from finite numerical audits: the target-tail existence flag is true, while a certified boundary constant, a legal head pass, a cloud coefficient bridge, and a uniform quotient tail are all false.

The obstruction does not exclude larger integer caps, signed or complex selectors derived from an invariant quotient, larger resolved windows, a future interval bound for $M_S$, or another operator realization. It also does not establish global nonexistence. Gates A--E remain false/open. No Hilbert--Polya operator is constructed; no Riemann zeros are identified; no equality with the completed zeta divisor and no implication of RH is claimed.

The next reopening input must supply at least one genuinely new legal head, a certified $M_S$, a uniform quotient theorem, or an exact coefficient bridge; the useful route requires the relevant obligations together rather than a finite-order extrapolation.
