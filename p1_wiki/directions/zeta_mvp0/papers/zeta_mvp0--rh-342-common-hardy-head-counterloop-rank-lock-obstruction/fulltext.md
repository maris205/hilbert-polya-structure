---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-342-common-hardy-head-counterloop-rank-lock-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-342-common-hardy-head-counterloop-rank-lock-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-342-common-hardy-head-counterloop-rank-lock-obstruction/main.pdf"
source_sha256: "0c1f69eb717ce1b44000796d99f421237d73108d1f97f608680c3350de165756"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Common-Hardy Head/Counterloop Rank Lock and a Hidden-Shell Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-342-common-hardy-head-counterloop-rank-lock-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-342-common-hardy-head-counterloop-rank-lock-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-342-common-hardy-head-counterloop-rank-lock-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-342-common-hardy-head-counterloop-rank-lock-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-342-common-hardy-head-counterloop-rank-lock-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We lock the actual modulus-complete noisy head and the finite graded counterloop in the same Hardy normalization and on the physical first-alias clock. The actual head consists of the algebraic nonperipheral eigenvalues of $K_\sigma/r_H$ with modulus greater than $q=1/2$; the counterloop is the $2k$th-root shell with the two real roots removed, hence has rank $2k-2$. Their finite genus-one quotient has local logarithmic coefficients $-d_{\sigma,k,n}/n$ for $n\ge2$. This is an analytic comparison, not a physical determinant decomposition.

  We prove two exact finite-spectral theorems. First, zero-padded root $\ell^1$ matching has a cardinality floor: its cost is at least $q(r_\sigma-2k+2)_++\beta_k(2k-2-r_\sigma)_+$. Thus any actual matching cost tending to zero would force the eventual exact rank law $r_\sigma=2k-2$. No such law is presently sourced. Second, two nonzero finite multisets of ranks at most $N$ are identical if their power sums agree for orders $2$ through $2N+1$. The missing first moment causes no ambiguity once the rank cap is known.

  The cap is indispensable. Adding a complete $4k$th-root shell of radius $3/4$ preserves every strict-prefix moment $2\le n<4k$, while the padded root cost is at least $2k$ and the added genus-one factor is $1-(3z/4)^{4k}$. This is a conjugation-closed finite normal information-class counterexample, not an actual noisy operator. Finally, the RH-299 transport criterion at the cut $4k$ requires the source-safe global rate $\gamma>1.926813889034\ldots$; the smaller $0.926813889034\ldots$ threshold assumes an unproved local actual-head cap. Root transport without a rank law, cap, and actual matching rate is therefore `STOP_SCOPED`. Aggregate and annular routes remain `NOT_TESTABLE`/open, and no Gate or Riemann-hypothesis claim follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A Common-Hardy Head/Counterloop Rank Lock and a\
  Hidden-Shell Obstruction
```

## Markdown 正文

# One physical data type and one clock

Set $$\label{eq:hardy-constants}
 r_H=\frac{17}{20},\qquad q=\frac12,\qquad R=\frac75,
 \qquad A_\sigma=K_\sigma/r_H.$$ After removing the Perron and negative-parity eigenvalues, let $$\label{eq:actual-head}
 \mathcal H_\sigma
 =\{\mu:\ \mu\text{ is an algebraic eigenvalue of }A_\sigma,
                    \ |\mu|>q\},
 \qquad r_\sigma=\#\mathcal H_\sigma,$$ where algebraic multiplicity is retained, and put $$\label{eq:head-moment}
 h_{\sigma,n}=\sum_{\mu\in\mathcal H_\sigma}\mu^n.$$ This is exactly the modulus-complete head of RH-282 [@WangSpectralTail2026]. Its available rank information is only $$\label{eq:source-rank-bound}
 r_\sigma\le 4\sigma^{-1}.$$ In particular, the half-logarithmic endpoint singular-value rank of RH-16 [@WangEndpointRank2026] is not identified with $r_\sigma$. The former is a singular-resolution count; the latter is an algebraic spectral count.

Let $k=k_\sigma\ge2$ be the physical first-alias clock reviewed in RH-341 [@WangActualFrontier2026]: $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad u=4k.$$ For the boundary multiplier radius $\beta_k$, define the counterloop multiset $$\label{eq:Y-definition}
 \mathcal Y_k=
 \{\beta_k e^{ij\pi/k},\beta_k e^{-ij\pi/k}:1\le j\le k-1\}.$$ It has rank $$\label{eq:model-rank}
 m_k=\#\mathcal Y_k=2k-2,$$ and $\beta_k\to\beta=(r_H\sqrt\lambda)^{-1}>q$ [@WangCounterloop2026]. Since $K_\sigma$ is a strongly positive Markov operator, its nonperipheral eigenvalues have modulus below one. Therefore every member of $\mathcal H_\sigma$ has modulus at most $1/r_H$. Also $\beta<1/r_H$, so $\beta_k<1/r_H$ eventually. Thus $$\label{eq:global-common-cap}
 B=1/r_H$$ is a source-safe eventual common cap for the actual head and counterloop.

[\[prop:counterloop\]]{#prop:counterloop label="prop:counterloop"} For every integer $n\ge1$, $$\label{eq:counterloop-moment}
 s_{k,n}:=\sum_{\nu\in\mathcal Y_k}\nu^n
 =\beta_k^n\bigl(2k\mathbf 1_{2k\mid n}-1-(-1)^n\bigr).$$ The strict prefix $2\le n<4k$ contains the first alias $n=2k$ and excludes the second alias $n=4k$.

The complete set of scaled $2k$th roots has power sum $2k\beta_k^n\mathbf 1_{2k\mid n}$. Removing the roots $\beta_k$ and $-\beta_k$ subtracts $\beta_k^n(1+(-1)^n)$, which proves [\[eq:counterloop-moment\]](#eq:counterloop-moment){reference-type="eqref" reference="eq:counterloop-moment"}. The two alias assertions are the strict inequalities $2\le2k<4k$ and $4k\not<4k$.

This is the counterloop used in the typed RH-290 and RH-297 ledgers [@WangTypedLedger2026; @WangAliasLedger2026]. Define the common-Hardy head defect $$\label{eq:defect}
 d_{\sigma,k,n}=h_{\sigma,n}-s_{k,n}.$$ The point of the source lock is that neither the RH-16 singular rank nor a model cloud may be substituted for the actual multiset [\[eq:actual-head\]](#eq:actual-head){reference-type="eqref" reference="eq:actual-head"}.

# The exact analytic factor interface

For a finite multiset $X$ of nonzero complex numbers, write $$\label{eq:genus-one}
 E_1(w)=(1-w)e^w,
 \qquad \Phi_X(z)=\prod_{x\in X}E_1(xz).$$ The product is entire. Its logarithm has a canonical germ at the origin, since $\Phi_X(0)=1$.

[\[thm:factor-interface\]]{#thm:factor-interface label="thm:factor-interface"} For the actual head $\mathcal H_\sigma$ and counterloop $\mathcal Y_k$, $$\label{eq:factor-log}
 \log\frac{\Phi_{\mathcal H_\sigma}(z)}{\Phi_{\mathcal Y_k}(z)}
 =-\sum_{n\ge2}\frac{d_{\sigma,k,n}}{n}z^n$$ as a convergent power series in a sufficiently small neighborhood of $z=0$.

For $|w|<1$, $$\label{eq:E1-log}
 \log E_1(w)=\log(1-w)+w=-\sum_{n\ge2}\frac{w^n}{n}.$$ Both multisets are finite, so one may choose a common neighborhood of zero on which [\[eq:E1-log\]](#eq:E1-log){reference-type="eqref" reference="eq:E1-log"} holds for every root. Sum first over $\mathcal H_\sigma$, then subtract the sum over $\mathcal Y_k$, and use [\[eq:defect\]](#eq:defect){reference-type="eqref" reference="eq:defect"}.

Theorem [\[thm:factor-interface\]](#thm:factor-interface){reference-type="ref" reference="thm:factor-interface"} compares two finite analytic factors. It does not assert that the quotient is a factor in one physical determinant, that $\mathcal Y_k$ is a spectral submultiset of $A_\sigma$, or that the remaining physical determinant pieces glue. Those distinctions are the missing glue in RH-288 and RH-290 [@WangGluing2026; @WangTypedLedger2026].

# Zero padding forces a rank law

If $X=\{x_1,\ldots,x_r\}$ and $Y=\{y_1,\ldots,y_m\}$ are finite multisets, pad the smaller one with zeros to the common size $N=\max(r,m)$ and define $$\label{eq:padded-distance}
 d_1^0(X,Y)=\min_{\pi\in S_N}
       \sum_{j=1}^N|\widetilde x_j-\widetilde y_{\pi(j)}|.$$ This is the root interface introduced in RH-299 [@WangRootTransport2026].

[\[thm:rank-lock\]]{#thm:rank-lock label="thm:rank-lock"} Let $X$ be a finite multiset with $|x|>q$ for every $x\in X$, and let $Y$ be a finite multiset whose every member has modulus $\beta_0>0$. If $r=\#X$ and $m=\#Y$, then $$\label{eq:rank-lock-general}
 d_1^0(X,Y)\ge
 q(r-m)_++\beta_0(m-r)_+.$$ In particular, $$\label{eq:rank-lock-physical}
 d_1^0(\mathcal H_\sigma,\mathcal Y_k)\ge
 q(r_\sigma-m_k)_++\beta_k(m_k-r_\sigma)_+.$$

Suppose first that $r>m$. The padded copy of $Y$ contains exactly $r-m$ zeros. Every matching pairs those zeros with $r-m$ members of $X$, and each such pair costs $|x|>q$. Hence the total cost is at least $q(r-m)$. If $m>r$, the padded copy of $X$ contains $m-r$ zeros. Exactly $m-r$ members of $Y$ meet those zeros, each at cost $\beta_0$, giving $\beta_0(m-r)$. The equal-rank case has the asserted zero lower bound. Apply the result with $X=\mathcal H_\sigma$, $Y=\mathcal Y_k$, and $\beta_0=\beta_k$.

[\[cor:rank-law\]]{#cor:rank-law label="cor:rank-law"} If $$\label{eq:o1-matching}
 d_1^0(\mathcal H_\sigma,\mathcal Y_{k_\sigma})=o(1),$$ then, for all sufficiently small $\sigma$, $$\label{eq:eventual-rank}
 r_\sigma=2k_\sigma-2.$$ The conclusion also follows from any estimate $d_1^0=O(\sigma^\gamma)$ with $\gamma>0$.

Since $\beta_k\to\beta>q$, both possible nonzero rank-mismatch floors in [\[eq:rank-lock-physical\]](#eq:rank-lock-physical){reference-type="eqref" reference="eq:rank-lock-physical"} are bounded below by a fixed positive constant for large $k$. An integer rank mismatch is therefore incompatible with [\[eq:o1-matching\]](#eq:o1-matching){reference-type="eqref" reference="eq:o1-matching"}. A positive power of $\sigma$ tends to zero.

The corollary is a necessary consequence of a future matching theorem; it is not such a theorem. Bound [\[eq:source-rank-bound\]](#eq:source-rank-bound){reference-type="eqref" reference="eq:source-rank-bound"} is far too broad to give [\[eq:eventual-rank\]](#eq:eventual-rank){reference-type="eqref" reference="eq:eventual-rank"}, and the repository explicitly supplies no identification between the RH-16 endpoint singular rank and $r_\sigma$.

# Shifted moments identify roots under a rank cap

For a finite multiset $X$, let $p_n(X)=\sum_{x\in X}x^n$.

[\[thm:shifted-uniqueness\]]{#thm:shifted-uniqueness label="thm:shifted-uniqueness"} Let $X$ and $Y$ be finite nonempty multisets of nonzero complex numbers with $$\label{eq:rank-cap}
 \#X\le N,\qquad \#Y\le N.$$ If $$\label{eq:shifted-moments}
 p_n(X)=p_n(Y)\qquad(2\le n\le2N+1),$$ then $X=Y$ as multisets.

Define the rational function $$\label{eq:rational-observable}
 F_X(z)=\sum_{x\in X}\frac{x^2}{1-xz}
       =\sum_{j\ge0}p_{j+2}(X)z^j$$ near the origin, and define $F_Y$ analogously. If $r=\#X$ and $s=\#Y$, then $$\label{eq:rational-degree}
 F_X=\frac{A_X}{Q_X},\qquad
 Q_X(z)=\prod_{x\in X}(1-xz),\qquad
 \deg A_X\le r-1,$$ with the analogous bounds for $Y$. Consequently the numerator of $F_X-F_Y$ over $Q_XQ_Y$ has degree at most $$\label{eq:numerator-degree}
 \max\{(r-1)+s,(s-1)+r\}=r+s-1\le2N-1.$$

Condition [\[eq:shifted-moments\]](#eq:shifted-moments){reference-type="eqref" reference="eq:shifted-moments"} says that the first $2N$ Taylor coefficients in [\[eq:rational-observable\]](#eq:rational-observable){reference-type="eqref" reference="eq:rational-observable"} agree. Thus $F_X-F_Y$ has a zero of order at least $2N$ at the origin. Since $Q_X(0)Q_Y(0)=1$, its polynomial numerator is divisible by $z^{2N}$. The degree bound [\[eq:numerator-degree\]](#eq:numerator-degree){reference-type="eqref" reference="eq:numerator-degree"} forces that numerator to vanish identically, so $F_X=F_Y$.

For every distinct nonzero value $a$ occurring in $X$, the partial fraction of $F_X$ contains $$\label{eq:multiplicity-term}
 \frac{m_X(a)a^2}{1-az}.$$ Equality of the rational functions gives the same poles and the same coefficients, hence $m_X(a)=m_Y(a)$ for every $a$. Therefore the multisets are identical.

[\[cor:strict-prefix\]]{#cor:strict-prefix label="cor:strict-prefix"} Let $N=2k-2$. If $X$ is a finite multiset of nonzero complex numbers, has rank at most $N$, and $$\label{eq:strict-prefix-equality}
 p_n(X)=s_{k,n}\qquad(2\le n<4k),$$ then $X=\mathcal Y_k$.

The model has rank $N$. The required terminal order in Theorem [\[thm:shifted-uniqueness\]](#thm:shifted-uniqueness){reference-type="ref" reference="thm:shifted-uniqueness"} is $2N+1=4k-3<4k$, so [\[eq:strict-prefix-equality\]](#eq:strict-prefix-equality){reference-type="eqref" reference="eq:strict-prefix-equality"} contains every required moment.

This corollary shows precisely what the absence of the first moment does *not* obstruct. Its active hypothesis is the rank cap. No such actual cap at $2k-2$ is presently proved.

# A hidden-shell counterexample without the cap

Let $$\label{eq:hidden-shell}
 \mathcal Z_k=\left\{\frac34e^{2\pi ij/(4k)}:0\le j<4k\right\},
 \qquad \mathcal X_k=\mathcal Y_k\sqcup\mathcal Z_k.$$ Both multisets are closed under complex conjugation. They are spectra of finite normal diagonal matrices.

[\[thm:hidden-shell\]]{#thm:hidden-shell label="thm:hidden-shell"} For every $k\ge2$ and every order $2\le n<4k$, $$\label{eq:hidden-moment-equality}
 p_n(\mathcal X_k)=p_n(\mathcal Y_k).$$ Thus the strict-prefix head budget formed from these two multisets is exactly zero: $$\label{eq:hidden-D-zero}
 \sum_{2\le n<4k}
 \frac{|p_n(\mathcal X_k)-p_n(\mathcal Y_k)|R^n}{n}=0.$$ For all sufficiently large $k$, $$\label{eq:hidden-root-distance}
 d_1^0(\mathcal X_k,\mathcal Y_k)\ge4kq=2k.$$ Moreover, $$\label{eq:hidden-factor}
 \frac{\Phi_{\mathcal X_k}(z)}{\Phi_{\mathcal Y_k}(z)}
 =1-\left(\frac{3z}{4}\right)^{4k}.$$

The complete root shell satisfies $$\label{eq:shell-power}
 \sum_{\zeta\in\mathcal Z_k}\zeta^n
 =4k\left(\frac34\right)^n\mathbf 1_{4k\mid n}.$$ It vanishes throughout $2\le n<4k$, which proves [\[eq:hidden-moment-equality\]](#eq:hidden-moment-equality){reference-type="eqref" reference="eq:hidden-moment-equality"} and [\[eq:hidden-D-zero\]](#eq:hidden-D-zero){reference-type="eqref" reference="eq:hidden-D-zero"}.

The rank difference is $\#\mathcal X_k-\#\mathcal Y_k=4k$. For large $k$, every member of $\mathcal Y_k$ has modulus $\beta_k>q$, and every member of $\mathcal Z_k$ has modulus $3/4>q$. Apply the first branch of Theorem [\[thm:rank-lock\]](#thm:rank-lock){reference-type="ref" reference="thm:rank-lock"} to obtain [\[eq:hidden-root-distance\]](#eq:hidden-root-distance){reference-type="eqref" reference="eq:hidden-root-distance"}.

Finally, the genus-one exponential terms cancel because $\sum_{\zeta\in\mathcal Z_k}\zeta=0$. The elementary full-root product gives $$\label{eq:full-root-product}
 \prod_{\zeta\in\mathcal Z_k}(1-\zeta z)
 =1-(3z/4)^{4k},$$ which is [\[eq:hidden-factor\]](#eq:hidden-factor){reference-type="eqref" reference="eq:hidden-factor"}.

Theorem [\[thm:hidden-shell\]](#thm:hidden-shell){reference-type="ref" reference="thm:hidden-shell"} is a finite normal spectral information-class example. It proves that strict-prefix moments do not control padded root distance without a rank cap, and that an entire shell may first appear at the excluded endpoint. It does not realize $K_\sigma$, prove a physical head-rank mismatch, show that the actual $D_{4k}$ diverges, or refute a future signed aggregate theorem.

# The RH-299 threshold on the physical cut

RH-299 proves that if both root multisets lie in $|z|\le B$, then for every integer $m\ge3$ [@WangRootTransport2026] $$\label{eq:rh299-bound}
 D_m(R):=\sum_{n=2}^{m-1}
 \frac{|p_n(X)-p_n(Y)|R^n}{n}
 \le d_1^0(X,Y)R\sum_{j=1}^{m-2}(BR)^j.$$

[\[prop:thresholds\]]{#prop:thresholds label="prop:thresholds"} Put $m=4k$ with the clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, and suppose $BR>1$ and $$\label{eq:matching-rate}
 d_1^0(\mathcal H_\sigma,\mathcal Y_k)=O(\sigma^\gamma).$$ Then the right side of [\[eq:rh299-bound\]](#eq:rh299-bound){reference-type="eqref" reference="eq:rh299-bound"} tends to zero if $$\label{eq:general-threshold}
 \gamma>\frac{2\log(BR)}{\log\lambda}.$$ For the source-safe common cap $B=1/r_H$, this becomes $$\label{eq:global-threshold}
 \gamma>\frac{2\log(R/r_H)}{\log\lambda}
 =1.926813889034004\ldots.$$ If one had the additional local actual-head cap $$\label{eq:local-cap}
 |\mu|\le\beta+o(1)\qquad(\mu\in\mathcal H_\sigma),$$ then the limiting threshold would instead be $$\label{eq:local-threshold}
 \gamma>\frac{2\log(\beta R)}{\log\lambda}
 =0.926813889034004\ldots.$$ The local cap is not supplied by the repository.

Since $BR>1$, the geometric sum in [\[eq:rh299-bound\]](#eq:rh299-bound){reference-type="eqref" reference="eq:rh299-bound"} is $O((BR)^m)$. Equations [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} and $m=4k$ give $$\label{eq:clock-growth}
 m=\frac{2\log(1/\sigma)}{\log\lambda}+O(1),
 \qquad
 (BR)^m=O\!\left(
 \sigma^{-2\log(BR)/\log\lambda}
 \right).$$ Multiplication by [\[eq:matching-rate\]](#eq:matching-rate){reference-type="eqref" reference="eq:matching-rate"} proves [\[eq:general-threshold\]](#eq:general-threshold){reference-type="eqref" reference="eq:general-threshold"}. Substituting $B=1/r_H$ gives [\[eq:global-threshold\]](#eq:global-threshold){reference-type="eqref" reference="eq:global-threshold"}. Substituting $\beta=(r_H\sqrt\lambda)^{-1}$ gives the limiting value in [\[eq:local-threshold\]](#eq:local-threshold){reference-type="eqref" reference="eq:local-threshold"}. More precisely, for every $\gamma$ strictly above that value, choose $\varepsilon>0$ so small that $\gamma>2\log((\beta+\varepsilon)R)/\log\lambda$. Equation [\[eq:local-cap\]](#eq:local-cap){reference-type="eqref" reference="eq:local-cap"} and $\beta_k\to\beta$ then give the common eventual cap $B=\beta+\varepsilon$. The two displayed limiting thresholds differ by exactly one, because $$\label{eq:threshold-gap}
 \frac{2}{\log\lambda}
 \log\frac{R/r_H}{\beta R}
 =\frac{2}{\log\lambda}\log\sqrt\lambda=1.$$

The specialization is only a sufficient interface. Even [\[eq:global-threshold\]](#eq:global-threshold){reference-type="eqref" reference="eq:global-threshold"} requires an actual matching theorem, and Corollary [\[cor:rank-law\]](#cor:rank-law){reference-type="ref" reference="cor:rank-law"} shows that such a rate also contains the eventual exact rank law. The smaller number in [\[eq:local-threshold\]](#eq:local-threshold){reference-type="eqref" reference="eq:local-threshold"} cannot be quoted for the actual head before proving the local cap.

# Protocol, verdict, and next admissible input

The executable artifact uses exact rational constants for $q$, $r_H$, $R$, and the hidden radius. It evaluates the counterloop and full-shell power formulas, the rank-mismatch floor, the rational-function degree ledger, and the two RH-299 thresholds. Finite rows at $k=3,5,9,17$ are reproduction checks only; they are not noisy spectral observations and have no asymptotic evidentiary role.

The results separate three conclusions:

1.  The rank-lock and shifted-moment theorems are exact finite-spectral statements in the declared common-Hardy data type.

2.  The hidden shell proves a strict cap-free information-class obstruction, not a physical nonidentification theorem.

3.  No source supplies an actual rank law, local shell cap, root list, or matching rate. Therefore RH-299 activation without these hypotheses is `STOP_SCOPED`.

Aggregate moment, Fourier, and Hardy routes remain `NOT_TESTABLE`/open: the counterexample prevents a cap-free logical upgrade to root matching but does not decide the actual aggregate defect. The direct annular route of RH-300 [@WangAnnularCriteria2026] also remains `NOT_TESTABLE`/open because no theorem controls $$\label{eq:annular-g}
 g_\sigma(z)=\sum_{n\ge2}
 (\tau_{\sigma,n}-a_n)\frac{z^n}{n}$$ on any annulus $1.4<\rho<r_H\lambda$. The narrow reopen inputs are an actual head-rank theorem, an actual root matching with a proved common cap and sufficient rate, or direct annular convergence for [\[eq:annular-g\]](#eq:annular-g){reference-type="eqref" reference="eq:annular-g"}.

No determinant gluing is activated, and Gates A--E remain false/open. This paper proves neither physical head nonidentification nor physical defect divergence. It constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace or completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
