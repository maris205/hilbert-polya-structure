---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-343-equal-rank-equal-mass-first-alias-underdetermination"
canonical_tex: "zeta_mvp0/papers/RH-343-equal-rank-equal-mass-first-alias-underdetermination/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-343-equal-rank-equal-mass-first-alias-underdetermination/main.pdf"
source_sha256: "612502c73326b001dd417d5d3bf9b391f5d339bdfad47cbd37b902eb1fb88432"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Equal Rank and Equal Spectral Mass Do Not Determine the First-Alias Weighted Prefix

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-343-equal-rank-equal-mass-first-alias-underdetermination>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-343-equal-rank-equal-mass-first-alias-underdetermination/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-343-equal-rank-equal-mass-first-alias-underdetermination/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-343-equal-rank-equal-mass-first-alias-underdetermination/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-343-equal-rank-equal-mass-first-alias-underdetermination/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct two finite normal spectral models on the physical first-alias clock that agree in a stringent package of coarse invariants compatible with the noisy Hardy-head ceilings but have opposite strict-prefix behavior. Let $\mathcal U_L(r)$ be the complete $L$th-root shell of radius $r$, let $\mathcal Y_k$ be the RH-342 counterloop, and set $$a=\frac34,\qquad b=\frac45,\qquad
   c=\sqrt{\frac{481}{800}}.$$ The multisets $$\mathcal X_k^{\mathrm{inv}}=\mathcal Y_k\sqcup\mathcal U_{4k}(c),
   \qquad
   \mathcal X_k^{\mathrm{vis}}=\mathcal Y_k\sqcup
   \mathcal U_{2k}(a)\sqcup\mathcal U_{2k}(b)$$ both have rank $6k-2$ and squared spectral mass $(2k-2)\beta_k^2+481k/200$. They are conjugation closed, eventually simple, normally realizable, contained in the same Hardy annulus, and have the same maximum modulus $\beta_k$. Both agree with $\mathcal Y_k$ at every order $2\le n<2k$, hence at every fixed order eventually, but they split at the first alias $n=2k$.

  For the RH-299 budget $$D_m(X,Y)=\sum_{2\le n<m}\frac{|p_n(X)-p_n(Y)|R^n}{n},
   \qquad R=\frac75,$$ the strict endpoint is decisive: $$D_{4k}(\mathcal X_k^{\mathrm{inv}},\mathcal Y_k)=0,
   \qquad
   D_{4k}(\mathcal X_k^{\mathrm{vis}},\mathcal Y_k)
   =\left(\frac{21}{20}\right)^{2k}
    +\left(\frac{28}{25}\right)^{2k}\longrightarrow\infty.$$ The genus-one quotient factors are respectively $1-(cz)^{4k}$ and $[1-(az)^{2k}][1-(bz)^{2k}]$. Thus equal rank, squared mass, cap, maximum modulus, normal simplicity, and all pre-alias or eventual fixed-order data do not determine the moving strict-prefix budget. This is an exact finite spectral information-class theorem, not an actual noisy-operator theorem. No physical head transport, determinant gluing, Gate progress, or Riemann-hypothesis claim follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Equal Rank and Equal Spectral Mass Do Not Determine the\
  First-Alias Weighted Prefix
```

## Markdown 正文

# Source-locked counterloop and complete shells

Fix the common Hardy constants and physical clock $$\label{eq:constants-clock}
 q=\frac12,\qquad r_H=\frac{17}{20},\qquad R=\frac75,
 \qquad
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad u=4k.$$ RH-342 locks the graded counterloop in this normalization as $$\label{eq:Y}
 \mathcal Y_k=\{\beta_k e^{ij\pi/k},\beta_k e^{-ij\pi/k}:
                    1\le j\le k-1\},
 \qquad \#\mathcal Y_k=2k-2,$$ with exact moments $$\label{eq:Y-moments}
 p_n(\mathcal Y_k)=\beta_k^n
 \bigl(2k\mathbf 1_{2k\mid n}-1-(-1)^n\bigr).$$ Here and below $p_n(X)=\sum_{x\in X}x^n$. The radius obeys $$\label{eq:beta-limit}
 \beta_k\longrightarrow
 \beta=(r_H\sqrt\lambda)^{-1}=0.9080523604\ldots$$ by RH-272, and $\beta_k<1/r_H$ eventually [@WangCounterloop2026; @WangRankLock2026]. The strict prefix $2\le n<4k$ contains $2k$ and excludes $4k$.

For $L\ge2$ and $r>0$, define the complete root shell $$\label{eq:full-shell}
 \mathcal U_L(r)=\{re^{2\pi ij/L}:0\le j<L\}.$$

[\[prop:shell-ledger\]]{#prop:shell-ledger label="prop:shell-ledger"} For every integer $n\ge1$, $$\label{eq:shell-ledger}
 p_n(\mathcal U_L(r))=Lr^n\mathbf 1_{L\mid n}.$$

After factoring out $r^n$, the remaining sum is the finite geometric progression $$\sum_{j=0}^{L-1}e^{2\pi ijn/L},$$ which equals $L$ when $L\mid n$ and zero otherwise. This is the complete shell identity used in RH-289 [@WangShellNonidentifiability2026].

Put $$\label{eq:radii}
 a=\frac34,\qquad b=\frac45,\qquad
 c=\sqrt{\frac{481}{800}},
 \qquad c^2=\frac{a^2+b^2}{2},$$ and define two model spectra $$\label{eq:candidates}
 \mathcal X_k^{\mathrm{inv}}=\mathcal Y_k\sqcup\mathcal U_{4k}(c),
 \qquad
 \mathcal X_k^{\mathrm{vis}}=\mathcal Y_k\sqcup\mathcal U_{2k}(a)
                         \sqcup\mathcal U_{2k}(b).$$ The superscripts describe visibility before the strict endpoint. Neither multiset is named or interpreted as the actual spectral head of $K_\sigma/r_H$.

# Equal rank, mass, cap, and normal realizability

We use *squared spectral mass* for the multiset quantity $$\label{eq:squared-mass}
 M_2(X)=\sum_{x\in X}|x|^2.$$ For a normal diagonal realization this also equals its squared Hilbert--Schmidt norm; no such operator-language identification is used for an actual noisy operator.

[\[thm:equal-invariants\]]{#thm:equal-invariants label="thm:equal-invariants"} For every $k\ge2$, $$\begin{aligned}
 \#\mathcal X_k^{\mathrm{inv}}=\#\mathcal X_k^{\mathrm{vis}}&=6k-2,
 \label{eq:equal-rank}\\
 M_2(\mathcal X_k^{\mathrm{inv}})=M_2(\mathcal X_k^{\mathrm{vis}})
 &=(2k-2)\beta_k^2+\frac{481k}{200}.
 \label{eq:equal-mass}\end{aligned}$$ Both multisets are closed under complex conjugation and are spectra of finite normal diagonal matrices. For all sufficiently large $k$, they are simple, every root lies in $$\label{eq:common-annulus}
 q<|z|<1/r_H,$$ and both have maximum root modulus exactly $\beta_k$.

The added ranks are $4k$ on both sides, so [\[eq:equal-rank\]](#eq:equal-rank){reference-type="eqref" reference="eq:equal-rank"} follows from $\#\mathcal Y_k=2k-2$. The invisible shell adds squared mass $$4kc^2=4k\frac{481}{800}=\frac{481k}{200}.$$ The visible shells add $$2ka^2+2kb^2
 =2k\left(\frac9{16}+\frac{16}{25}\right)
 =2k\frac{481}{400}=\frac{481k}{200},$$ which proves [\[eq:equal-mass\]](#eq:equal-mass){reference-type="eqref" reference="eq:equal-mass"}.

Every complete shell and $\mathcal Y_k$ is conjugation closed, hence so are their disjoint unions. Listing the roots on the diagonal gives finite normal realizations. The exact squared comparisons $$\label{eq:radius-squares}
 a^2=\frac{450}{800}<c^2=\frac{481}{800}
 <b^2=\frac{512}{800}$$ give $a<c<b$. Since $q<a$ and the limit in [\[eq:beta-limit\]](#eq:beta-limit){reference-type="eqref" reference="eq:beta-limit"} is larger than $b=0.8$, eventually $$\label{eq:radius-order}
 q<a<c<b<\beta_k<1/r_H.$$ Each individual root shell is simple. Their radii are then pairwise distinct, while the roots in $\mathcal Y_k$ are the distinct nonreal $2k$th roots on radius $\beta_k$. Thus both unions are simple. Equation [\[eq:radius-order\]](#eq:radius-order){reference-type="eqref" reference="eq:radius-order"} also proves [\[eq:common-annulus\]](#eq:common-annulus){reference-type="eqref" reference="eq:common-annulus"} and shows that the common maximum modulus is $\beta_k$.

[\[cor:coarse-compatible\]]{#cor:coarse-compatible label="cor:coarse-compatible"} On the clock [\[eq:constants-clock\]](#eq:constants-clock){reference-type="eqref" reference="eq:constants-clock"}, the rank and squared spectral mass of both candidates satisfy $$\label{eq:coarse-scale}
 O(k)=O(\log(1/\sigma))=o(1/\sigma).$$ Consequently they do not violate the RH-282 ceilings $$\label{eq:rh282-ceilings}
 r_\sigma\le4/\sigma,
 \qquad M_\sigma\le1/\sigma,$$ but those inequalities do not physically realize either candidate.

The rank formula is linear in $k$. Since $\beta_k$ converges, the mass in [\[eq:equal-mass\]](#eq:equal-mass){reference-type="eqref" reference="eq:equal-mass"} is also $O(k)$. Equation [\[eq:constants-clock\]](#eq:constants-clock){reference-type="eqref" reference="eq:constants-clock"} and the elementary relation $\log(1/\sigma)=o(1/\sigma)$ give [\[eq:coarse-scale\]](#eq:coarse-scale){reference-type="eqref" reference="eq:coarse-scale"}. RH-282 proves [\[eq:rh282-ceilings\]](#eq:rh282-ceilings){reference-type="eqref" reference="eq:rh282-ceilings"} for the actual noisy spectral data [@WangSpectralTail2026]; satisfying upper ceilings is only a consistency check, not an identification theorem.

# Pre-alias agreement and the first split

[\[thm:moment-dichotomy\]]{#thm:moment-dichotomy label="thm:moment-dichotomy"} For every $n\ge1$, $$\begin{aligned}
 p_n(\mathcal X_k^{\mathrm{inv}})-p_n(\mathcal Y_k)
 &=4kc^n\mathbf 1_{4k\mid n},
 \label{eq:inv-difference}\\
 p_n(\mathcal X_k^{\mathrm{vis}})-p_n(\mathcal Y_k)
 &=2k(a^n+b^n)\mathbf 1_{2k\mid n}.
 \label{eq:vis-difference}\end{aligned}$$ Hence both candidates agree exactly with $\mathcal Y_k$ for every $$\label{eq:pre-alias}
 2\le n<2k.$$ For every fixed $n\ge2$, this agreement therefore holds for all sufficiently large $k$. The candidates do *not* both agree with $\mathcal Y_k$ throughout $2\le n<4k$: at $n=2k$, $$\label{eq:first-split}
 p_{2k}(\mathcal X_k^{\mathrm{inv}})-p_{2k}(\mathcal Y_k)=0,
 \qquad
 p_{2k}(\mathcal X_k^{\mathrm{vis}})-p_{2k}(\mathcal Y_k)
 =2k(a^{2k}+b^{2k})>0.$$

Apply Proposition [\[prop:shell-ledger\]](#prop:shell-ledger){reference-type="ref" reference="prop:shell-ledger"} to each shell in [\[eq:candidates\]](#eq:candidates){reference-type="eqref" reference="eq:candidates"}. No positive integer $n<2k$ is divisible by either $2k$ or $4k$, proving [\[eq:pre-alias\]](#eq:pre-alias){reference-type="eqref" reference="eq:pre-alias"}. For fixed $n$, eventually $n<2k$. Finally, $2k$ is not divisible by $4k$ but is divisible by $2k$, which gives [\[eq:first-split\]](#eq:first-split){reference-type="eqref" reference="eq:first-split"}.

The distinction in Theorem [\[thm:moment-dichotomy\]](#thm:moment-dichotomy){reference-type="ref" reference="thm:moment-dichotomy"} is essential. The invisible candidate agrees with $\mathcal Y_k$ at every order below $4k$, while the visible candidate first differs at $2k$. Thus the theorem does not claim that the two candidates carry identical data on the whole strict prefix.

# Exact strict-prefix budgets

Following RH-299, define for finite multisets $X,Y$ and $m\ge3$ $$\label{eq:D-definition}
 D_m(X,Y)=\sum_{n=2}^{m-1}
 \frac{|p_n(X)-p_n(Y)|R^n}{n},
 \qquad R=\frac75.$$ The denominator $n$ is part of the determinant-logarithm normalization and must not be dropped [@WangRootTransport2026].

[\[thm:budget-dichotomy\]]{#thm:budget-dichotomy label="thm:budget-dichotomy"} For every $k\ge2$, $$\begin{aligned}
 D_{4k}(\mathcal X_k^{\mathrm{inv}},\mathcal Y_k)&=0,
 \label{eq:inv-budget}\\
 D_{4k}(\mathcal X_k^{\mathrm{vis}},\mathcal Y_k)
 &=\left(\frac{21}{20}\right)^{2k}
  +\left(\frac{28}{25}\right)^{2k}.
 \label{eq:vis-budget}\end{aligned}$$ In particular, the second budget tends to infinity as $k\to\infty$.

There is no multiple of $4k$ in $2\le n<4k$, so [\[eq:inv-difference\]](#eq:inv-difference){reference-type="eqref" reference="eq:inv-difference"} makes every summand in [\[eq:D-definition\]](#eq:D-definition){reference-type="eqref" reference="eq:D-definition"} zero, proving [\[eq:inv-budget\]](#eq:inv-budget){reference-type="eqref" reference="eq:inv-budget"}. The only multiple of $2k$ in the same strict prefix is $n=2k$. Therefore [\[eq:vis-difference\]](#eq:vis-difference){reference-type="eqref" reference="eq:vis-difference"} gives exactly $$\begin{aligned}
 D_{4k}(\mathcal X_k^{\mathrm{vis}},\mathcal Y_k)
 &=\frac{2k(a^{2k}+b^{2k})R^{2k}}{2k}\\
 &=(aR)^{2k}+(bR)^{2k}\\
 &=\left(\frac{21}{20}\right)^{2k}
  +\left(\frac{28}{25}\right)^{2k}.\end{aligned}$$ This retains the exact cancellation between the shell multiplicity $2k$ and the logarithmic denominator $n=2k$. Both bases are larger than one, proving divergence.

The first nonzero moment of $\mathcal U_{4k}(c)$ occurs at $n=4k$. Thus replacing $n<4k$ by $n\le4k$ destroys [\[eq:inv-budget\]](#eq:inv-budget){reference-type="eqref" reference="eq:inv-budget"}. The paper proves a strict-prefix theorem only.

# Exact genus-one quotient factors

For a finite multiset $X$, put $$\label{eq:genus-one}
 E_1(w)=(1-w)e^w,
 \qquad \Phi_X(z)=\prod_{x\in X}E_1(xz).$$

[\[prop:quotient-factors\]]{#prop:quotient-factors label="prop:quotient-factors"} The shell quotients are the exact entire factors $$\begin{aligned}
 \frac{\Phi_{\mathcal X_k^{\mathrm{inv}}}(z)}{\Phi_{\mathcal Y_k}(z)}
 &=1-(cz)^{4k},
 \label{eq:inv-factor}\\
 \frac{\Phi_{\mathcal X_k^{\mathrm{vis}}}(z)}{\Phi_{\mathcal Y_k}(z)}
 &=[1-(az)^{2k}][1-(bz)^{2k}].
 \label{eq:vis-factor}\end{aligned}$$

For every complete shell with $L\ge2$, its first power sum is zero, so all linear exponential terms in [\[eq:genus-one\]](#eq:genus-one){reference-type="eqref" reference="eq:genus-one"} cancel. The elementary root factorization then gives $$\label{eq:shell-factor}
 \prod_{u\in\mathcal U_L(r)}E_1(uz)=1-(rz)^L.$$ Since each candidate is the disjoint union of $\mathcal Y_k$ and its displayed shells, equations [\[eq:inv-factor\]](#eq:inv-factor){reference-type="eqref" reference="eq:inv-factor"} and [\[eq:vis-factor\]](#eq:vis-factor){reference-type="eqref" reference="eq:vis-factor"} follow.

These are finite analytic factor identities. They do not identify either quotient with a factor in one physical noisy determinant.

# Sharp information-class underdetermination

[\[cor:underdetermination\]]{#cor:underdetermination label="cor:underdetermination"} Within the class of finite complex spectral multisets, the following data, even when imposed simultaneously, do not determine the moving strict-prefix quantity $D_{4k}(X,\mathcal Y_k)$:

1.  rank $6k-2$ and squared spectral mass $(2k-2)\beta_k^2+481k/200$;

2.  the common cap $1/r_H$ and common maximum modulus $\beta_k$;

3.  simple, conjugation-closed finite normal realizability;

4.  equality with $\mathcal Y_k$ at every pre-alias order $2\le n<2k$; and

5.  equality with $\mathcal Y_k$ at every fixed order eventually.

Indeed, the same data allow the exact value zero and a value tending to infinity. A future actual rank cap $r_\sigma\le2k-2$ would exclude both examples.

Theorem [\[thm:equal-invariants\]](#thm:equal-invariants){reference-type="ref" reference="thm:equal-invariants"} supplies items 1--3 for both candidates, and Theorem [\[thm:moment-dichotomy\]](#thm:moment-dichotomy){reference-type="ref" reference="thm:moment-dichotomy"} supplies items 4--5. The two values of the moving budget are given by Theorem [\[thm:budget-dichotomy\]](#thm:budget-dichotomy){reference-type="ref" reference="thm:budget-dichotomy"}. Both candidates have rank $6k-2>2k-2$, proving the final exclusion statement.

Corollary [\[cor:underdetermination\]](#cor:underdetermination){reference-type="ref" reference="cor:underdetermination"} is sharp in its declared information class: it preserves not only rank and mass but also the maximum radius and all pre-alias data. It does not refute a future transport theorem that uses actual operator structure, a sharper rank cap, root matching, moving-order moments, contour information, or an annular norm.

RH-303 proves that actual annular convergence would force fixed-order head transport [@WangFixedOrderNecessity2026]. Our examples show only that, in a finite normal information class, eventual fixed-order transport is not by itself sufficient for the moving $4k$ budget. No model-to-actual substitution is made.

# Protocol, verdict, and claim firewall

The executable artifact evaluates the exact shell indicators, common ranks, the rational squared-mass identity, the first split, both strict-prefix budgets, and the radius ordering. Its finite rows at $k=3,5,9,17$ reproduce closed identities only. They are not numerical fits, noisy eigenvalue observations, or asymptotic evidence.

On the physical clock, the examples are compatible with only the coarse RH-282 rank and mass ceilings. Such compatibility cannot identify them with the actual noisy head. Accordingly the exact route verdict is:

1.  equal rank, equal squared mass, common cap, and fixed-order data are `STOP_SCOPED` as an inference to the moving prefix without a sharper actual rank law or moving-order physical input;

2.  actual alias-inclusive head transport remains `NOT_TESTABLE`/open; and

3.  the RH-288 determinant-gluing leaf remains inactive.

In particular, this paper proves neither divergence nor vanishing of the actual $D_{4k}$, no physical rank mismatch, no equivalence of the physical $p$ and $q$ prefixes, and no failure of all future transport mechanisms. It does not activate RH-288, identify the model spectra with $K_\sigma$, or prove determinant gluing. Gates A--E remain false/open as reviewed in RH-341 [@WangActualFrontier2026]. No Hilbert--Polya operator is constructed, no Riemann zero is identified, no von Mangoldt trace formula or completed-zeta divisor equality is proved, and the Riemann Hypothesis is not proved.
