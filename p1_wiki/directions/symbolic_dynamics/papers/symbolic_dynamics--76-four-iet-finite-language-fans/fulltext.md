---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--76-four-iet-finite-language-fans"
canonical_tex: "symbolic_dynamics/papers/76-four-iet-finite-language-fans/main.tex"
canonical_pdf: "symbolic_dynamics/papers/76-four-iet-finite-language-fans/main.pdf"
source_sha256: "d70f299c8273642f9e299a019804c355624c79dd79009903a4e02876bf8b66e5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Language Polyhedral Fans and Cylinder Measures for Four-Interval Exchanges

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/76-four-iet-finite-language-fans>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/76-four-iet-finite-language-fans/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/76-four-iet-finite-language-fans/main.pdf>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/76-four-iet-finite-language-fans/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix a permutation of four intervals and a finite language horizon $N$. We show that the length simplex admits an effective rational polyhedral complex on whose relatively open cells the complete natural-coding language through length $N$ is constant. More precisely, the cylinder of a word $w=w_0\cdots w_{n-1}$ is the interval $$\left[
   \max_j(\ell_{w_j}-c_j),
   \min_j(r_{w_j}-c_j)
   \right),
   \qquad c_j=\sum_{q<j}\tau_{w_q},$$ where every endpoint is an integer linear form in the length vector. Consequently the admissibility region of each word is a rational convex polyhedron, every cylinder measure is piecewise integer-linear, and finite parameter realizability is an exact rational linear-feasibility problem. At a fixed parameter, membership is a direct endpoint comparison. Language change along a parameter path must cross a cylinder-collapse hyperplane. Exact rational controls for the reverse four-IET compare all cylinders through length six with a separate discontinuity-preimage partition.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: 'Finite-Language Polyhedral Fans and Cylinder Measures for Four-Interval Exchanges'
```

## Markdown 正文

# Introduction

An interval exchange transformation (IET) cuts an interval into finitely many subintervals and rearranges them by translations. Natural coding records the visited interval labels. Keane's foundational work [@Keane1975] supports a rich interaction between geometry, ergodic theory, and combinatorics. Languages of $k$-IETs have strong global characterizations [@FerencziZamboni2008], with more general coding classes treated in recent work [@FerencziHubertZamboni2026]. Cylinder intervals and admissible subintervals also enter branching Rauzy induction [@DolcePerrin2017; @DolceHughes2025]; our residual question is how all words through one fixed horizon vary jointly over the length-parameter simplex.

This note asks a finite-parameter question. Fix the permutation and inspect only words of length at most $N$. How does that truncated language vary with the interval lengths? Along a prescribed itinerary, every iterate is the initial point plus a sum of branch translations. Since those translations are integer linear forms in the length vector, the entire word cylinder is an intersection of explicitly translated intervals. Its nonemptiness is a finite strict linear system.

Taking the common hyperplane arrangement for all words through length $N$ gives a rational polyhedral complex on the length simplex. On each cell, not only the finite language but the entire vector of cylinder measures is linear. This is an effective finite-horizon parameterization, not a new global characterization of IET languages and not a replacement for Rauzy induction. We use four intervals, and especially the reverse permutation, to keep the result away from the Sturmian and three-IET regimes.

# Fixed-permutation interval exchanges

Let $d=4$ and let $\pi$ be a fixed irreducible permutation of $\{1,2,3,4\}$. A length vector $$\lambda=(\lambda_1,\ldots,\lambda_4)\in\mathbb R_{>0}^4,
 \qquad \sum_{a=1}^4\lambda_a=1,$$ defines domain intervals $$I_a=[\ell_a,r_a),\qquad
 \ell_a=\sum_{b<a}\lambda_b,
 \quad r_a=\ell_a+\lambda_a.$$ In the image order prescribed by $\pi$, the left endpoint of the copy of $I_a$ is $$\ell'_a=\sum_{\pi(b)<\pi(a)}\lambda_b.$$ The IET $T_{\pi,\lambda}$ translates $I_a$ by $$\label{eq:translation}
 \tau_a(\lambda)=\ell'_a-\ell_a.$$ Thus $\ell_a,r_a,$ and $\tau_a$ are integer linear forms in $\lambda$.

The natural coding of $x\in[0,1)$ is the word whose $j$th symbol is $a$ when $T^jx\in I_a$. For a finite word $w=w_0\cdots w_{n-1}$, its cylinder is $$C_w(\lambda)=\{x:T^jx\in I_{w_j}\text{ for }0\leq j<n\}.$$ We use half-open intervals consistently and work with the positive-cylinder (equivalently nonsingular finite-factor) language. A finite intersection of the intervals below is again $[L,R)$, so it is nonempty exactly when it has positive length, namely when $L<R$.

# An exact cylinder formula

For a proposed word $w$, define $$\label{eq:displacements}
 c_0=0,
 \qquad c_j(\lambda)=\sum_{q=0}^{j-1}\tau_{w_q}(\lambda),
 \quad 1\leq j<n.$$

[\[thm:cylinder\]]{#thm:cylinder label="thm:cylinder"} For every word $w=w_0\cdots w_{n-1}$, $$\label{eq:cylinder}
 C_w(\lambda)=[L_w(\lambda),R_w(\lambda)),$$ where $$\begin{aligned}
 L_w(\lambda)&=\max_{0\leq j<n}
 \{\ell_{w_j}(\lambda)-c_j(\lambda)\},\label{eq:left}\\
 R_w(\lambda)&=\min_{0\leq j<n}
 \{r_{w_j}(\lambda)-c_j(\lambda)\}.\label{eq:right}\end{aligned}$$ In particular, $w$ is admissible if and only if $L_w<R_w$.

As long as the itinerary begins with $w_0\cdots w_{j-1}$, the map is a composition of the corresponding translations, so $$T^jx=x+c_j(\lambda).$$ The condition that the $j$th symbol is $w_j$ is therefore $$\ell_{w_j}-c_j\leq x<r_{w_j}-c_j.$$ Intersect these $n$ half-open intervals. Their intersection is exactly [\[eq:cylinder\]](#eq:cylinder){reference-type="eqref" reference="eq:cylinder"}--[\[eq:right\]](#eq:right){reference-type="eqref" reference="eq:right"}, and it has positive length exactly when $L_w<R_w$.

The formula also gives the Lebesgue measure of the cylinder: $$\label{eq:measure}
 \mu_\lambda(C_w)=\bigl(R_w(\lambda)-L_w(\lambda)\bigr)_+.$$

# Word polyhedra

Let $a_j(\lambda)=\ell_{w_j}-c_j$ and $b_k(\lambda)=r_{w_k}-c_k$. Every $a_j,b_k$ is an integer linear form.

[\[cor:polyhedron\]]{#cor:polyhedron label="cor:polyhedron"} The parameter region $$\mathcal A_w=\{\lambda\in\mathbb R_{>0}^4:\textstyle\sum_a\lambda_a=1,
 \ w\in\mathcal L(T_{\pi,\lambda})\}$$ is the relatively open rational convex polyhedron cut out by $$\label{eq:all-pairs}
 a_j(\lambda)<b_k(\lambda),\qquad 0\leq j,k<n.$$ Its relative closure in the positive simplex is contained in the weak polyhedron obtained by replacing $<$ with $\leq$. If $\mathcal A_w$ is nonempty, the two sets are equal.

The inequality $\max_j a_j<\min_k b_k$ is equivalent to all $n^2$ inequalities in [\[eq:all-pairs\]](#eq:all-pairs){reference-type="eqref" reference="eq:all-pairs"}. Their coefficients are integers. Every limit point satisfies the corresponding weak inequalities. If $\lambda^*$ satisfies all inequalities strictly, then the segment from $\lambda^*$ to any positive weakly feasible point, with the latter endpoint removed, is strictly feasible. This proves the final assertion whenever $\mathcal A_w$ is nonempty.

This has an exact witness consequence. The existence of some positive length vector realizing $w$ is decided by rational linear programming: maximize a common slack $\delta$ subject to $$a_j+\delta\leq b_k,\qquad \lambda_i\geq\delta,
 \qquad \sum_i\lambda_i=1.$$ The strict system is feasible exactly when the optimum has $\delta>0$. Whenever it is feasible, it contains a rational length vector, and the midpoint $(L_w+R_w)/2$ is an explicit rational initial condition. For a fixed rational $\lambda$, by contrast, membership requires only direct evaluation of $L_w<R_w$ and no optimization.

# The finite-language fan

Fix a horizon $N$. For every word $w$ with $1\leq|w|\leq N$, consider the central rational hyperplanes $$\label{eq:arrangement}
 a_j=a_{j'},\qquad b_k=b_{k'},\qquad a_j=b_k.$$ All forms are homogeneous in $\lambda$, so these hyperplanes define a rational polyhedral fan in $\mathbb R^4$. Intersect it with the positive length cone and then with $\sum\lambda_a=1$; denote the resulting finite polyhedral complex by $\mathcal F_{\pi,N}$.

[\[thm:fan\]]{#thm:fan label="thm:fan"} On every relatively open cell $\sigma$ of $\mathcal F_{\pi,N}$:

1.  the complete truncated language $\mathcal L_{\leq N}(T_{\pi,\lambda})$ is independent of $\lambda\in\sigma$;

2.  for each $|w|\leq N$, either $C_w$ is empty throughout $\sigma$, or $\mu_\lambda(C_w)$ is one fixed integer linear form in $\lambda$ throughout $\sigma$;

3.  existence of a parameter realizing a word, together with a rational parameter and initial-point witness, is computable by exact rational linear programming; membership at a fixed parameter is a direct comparison.

If the truncated language changes along a continuous path in the positive simplex, the path meets a collapse hyperplane $a_j=b_k$ for some $|w|\leq N$.

On a relatively open arrangement cell, the weak and strict orders among all the forms in [\[eq:arrangement\]](#eq:arrangement){reference-type="eqref" reference="eq:arrangement"} are fixed. Hence the active maximum in [\[eq:left\]](#eq:left){reference-type="eqref" reference="eq:left"}, the active minimum in [\[eq:right\]](#eq:right){reference-type="eqref" reference="eq:right"}, and the sign of $R_w-L_w$ are fixed for every word through length $N$. This proves the first two claims, and [\[cor:polyhedron\]](#cor:polyhedron){reference-type="ref" reference="cor:polyhedron"} gives the algorithmic claim.

Along a continuous path, a word can enter or leave the positive-length language only when $R_w-L_w$ passes through zero. At that parameter, an active lower endpoint equals an active upper endpoint, so the path meets one of the hyperplanes $a_j=b_k$.

Not every formal wall must be essential: a hyperplane can lie outside the positive simplex, fail to be active, or leave the truncated language unchanged. The theorem asserts the necessary wall-crossing direction and an effective common refinement, not irredundancy.

[\[cor:size-bound\]]{#cor:size-bound label="cor:size-bound"} Let $$H_N=\sum_{n=1}^N4^n(2n^2-n).$$ The construction of $\mathcal F_{\pi,N}$ uses at most $H_N$ distinct hyperplanes, and its intersection with the three-dimensional length simplex has at most $$\sum_{q=0}^3\binom{H_N}{q}$$ full-dimensional cells. Each length-$n$ word region itself has a description using at most $n^2$ strict rational inequalities.

There are $4^n$ words of length $n$. For each word, the displayed arrangement lists two families of $\binom n2$ same-side comparisons and one family of $n^2$ lower--upper comparisons, for at most $2n^2-n$ hyperplanes. Summing gives $H_N$; coincidences only decrease the number. An arrangement of $H$ affine hyperplanes in dimension three has at most $\sum_{q=0}^3\binom Hq$ full-dimensional regions, by the standard induction that a newly added hyperplane cuts at most as many old regions as its induced two-dimensional arrangement has. Finally, [\[eq:all-pairs\]](#eq:all-pairs){reference-type="eqref" reference="eq:all-pairs"} contains $n^2$ inequalities.

# Reverse four-IET control example

Take the reverse permutation $\pi=(4,3,2,1)$. The accompanying exact-rational control uses three integer length vectors, normalized to total length one: $$(11,17,23,37),\qquad(7,13,29,47),\qquad(19,31,41,53).$$ For every word length through six, it computes the positive cylinders using [\[thm:cylinder\]](#thm:cylinder){reference-type="ref" reference="thm:cylinder"}. As a separate route, it constructs the partition by all preimages, through the same horizon, of the three IET discontinuities and reads the itinerary at the midpoint of every partition interval. The two languages agree in $18$ complete set equalities containing $207$ positive cylinders. The script also computes every endpoint as an integer coefficient vector, checks the all-pairs inequalities, and preserves two wall tests: a word that appears on exactly one side of an essential collapse wall, and an empty strict word region whose weak inequalities are nevertheless feasible.

For the first vector, the checked complexity profile is $$p(1),\ldots,p(6)=(4,7,10,13,16,19),$$ the generic $3n+1$ profile expected for a four-IET satisfying the relevant finite no-connection conditions. This profile is a control observation, not the theorem: [\[thm:fan\]](#thm:fan){reference-type="ref" reference="thm:fan"} applies equally on nongeneric cells, where some cylinders collapse.

# Scope and owner boundary

Keane's foundational IET dynamics [@Keane1975], the global characterization of $k$-IET languages by Ferenczi--Zamboni [@FerencziZamboni2008], and the broader classes in Ferenczi--Hubert--Zamboni [@FerencziHubertZamboni2026] are prior theory. Branching Rauzy work already owns admissible/cylinder-interval structure and its extension to arbitrary standard IETs [@DolcePerrin2017; @DolceHughes2025]. We do not claim the complexity law, minimality, unique ergodicity, Rauzy induction, or any global classification. We also avoid the three-IET and Sturmian/Ostrowski specialization.

The residual claim is finite-horizon and parameter-explicit: a word's admissibility region is one rational convex polyhedron, the joint language and cylinder-measure vector have a computable common polyhedral refinement with the explicit bound in [\[cor:size-bound\]](#cor:size-bound){reference-type="ref" reference="cor:size-bound"}, and every change is witnessed by a cylinder collapse. The source search was bounded and does not establish worldwide priority. This internal manuscript is not authorized for external release.
