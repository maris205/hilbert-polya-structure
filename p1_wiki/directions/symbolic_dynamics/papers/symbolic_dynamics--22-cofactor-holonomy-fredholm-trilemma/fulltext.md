---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--22-cofactor-holonomy-fredholm-trilemma"
canonical_tex: "symbolic_dynamics/papers/22-cofactor-holonomy-fredholm-trilemma/main.tex"
canonical_pdf: "symbolic_dynamics/papers/22-cofactor-holonomy-fredholm-trilemma/main.pdf"
source_sha256: "b9a40af45cb5151e3d60d5b54f4ee6c345d9096e752e82c669371d06ce8cb502"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cofactor Holonomy on the Successor--Divisor Shift: Exact Class Resolution and a Fredholm Trilemma

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/22-cofactor-holonomy-fredholm-trilemma>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/22-cofactor-holonomy-fredholm-trilemma/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/22-cofactor-holonomy-fredholm-trilemma/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/22-cofactor-holonomy-fredholm-trilemma/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/22-cofactor-holonomy-fredholm-trilemma/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We expose a multiplicative cocycle on the successor--divisor countable Markov shift: an edge $n\to d$, defined by $d\mid n+1$, carries the source-intrinsic cofactor $q=(n+1)/d$. A closed path has integer holonomy

  $$Q(\gamma)=\prod q
   =\prod_{n\in\gamma}(1+1/n)>1.$$

  Consequently the neutral regular-group sector has no periodic paths. The first non-neutral class is exactly rigid: $Q=2$ if and only if the orbit is, up to rotation, $C_k=(k,k+1,\ldots,2k-1)$, with one simple primitive class at every length $k\ge2$. Character Fourier extraction therefore gives the connected holonomy-two coefficient

  $$\sum_{k\ge2}z^k
   \left((2k-1)!/(k-1)!\right)^{-2s}.$$

  For the endpoint--cofactor adjacency

  $$L_{s,u}e_n=\sum_{d\mid n+1,\ d\ge2}(nd)^{-s}q^{-u}e_d,$$

  we prove the sharp equivalence

  $$L_{s,u}\in\mathcal S_1
   \iff \Re s>1/2\quad\text{and}\quad\Re(s+u)>1/2.$$

  The two boundaries come respectively from the cofactor-one successor spine and a fixed output-row tail. This yields a Fredholm trilemma: the pure cofactor roof has the desired $Q^{-u}$ cycle weight but is noncompact whenever bounded; endpoint regularization gives an honest determinant but factorially damps the canonical classes; unitary characters change phases only and retain every $C_k$. The regular lift is separately semifinite trace class for $\Re s>1/2$ but ordinarily noncompact, while its neutral local determinant is one. Thus the cocycle gives exact same-object class resolution without producing the Riemann prime Euler ledger.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Cofactor Holonomy on the Successor--Divisor Shift:\
  Exact Class Resolution and a Fredholm Trilemma
```

## Markdown 正文

# Introduction {#sec:introduction}

Arithmetic symbolic dynamics faces a recurrent design tension. A transition grammar can be sufficiently rigid to encode a desired arithmetic list, but then the recurrence may merely replay a verifier. Conversely, an intrinsic recurrent grammar may possess a robust determinant while producing far too many primitive cycles. The successor--divisor shift sits on the second side of this divide. Its vertex $n$ represents the full shift on $n$ symbols, and its edge rule

$$n\longrightarrow d
 \quad\Longleftrightarrow\quad d\ge2,\quad d\mid n+1$$

uses only alphabet successor and tensor factorization. The resulting countable Markov graph is recurrent and its endpoint-weighted adjacency has a sharp trace-class half-plane. It also contains the simple cycle

$$C_k=(k,k+1,\ldots,2k-1)$$

for every $k\ge2$. The analytic determinant is therefore real structure, but its primitive species is not selective.

This paper asks whether information already present on an allowed edge can resolve that flood. The edge equation $n+1=dq$ exposes the unique cofactor

$$q(n,d)=\frac{n+1}{d}.$$

No rational-prime table or target spectral data are needed to define it. Multiplying these labels around a closed path produces a canonical positive monoid cocycle. Passing to the group completion gives regular extensions, unitary character fibers, and exact Fourier coefficients of a connected Fredholm ledger. These are standard kinds of constructions in dynamical zeta and graph-cover theory [@BowenLanford1970; @AdachiSunada1987; @GrossTucker1977; @StarkTerras1996]; the question is what this particular source-derived cocycle actually knows.

The answer has a strong positive part. The cycle product telescopes to

$$Q(\gamma)=\prod_{n\in\gamma}\left(1+\frac1n\right)>1.$$

The class $Q=2$ consists exactly of the canonical cycles $C_k$, one primitive class at every length. More generally, an atomic holonomy $p$ has exactly the representatives

$$C_{k,p}=(k,k+1,\ldots,pk-1),\qquad k\ge2.$$

Temporal repetitions cannot enter an atomic class. Thus the character family resolves a nontrivial arithmetic grading exactly, rather than merely decorating an uncontrolled orbit sum.

The analytic part is equally sharp. On $\ell^2\{2,3,\ldots\}$, define

$$L_{s,u}e_n=
 \sum_{d\mid n+1,\ d\ge2}
 (nd)^{-s}q(n,d)^{-u}e_d.$$

We prove

$$\boxed{
 L_{s,u}\in\mathcal S_1
 \iff
 \Re s>\frac12,
 \quad \Re(s+u)>\frac12.}$$

The two conditions are independent. Output-row tails detect the combined endpoint--cofactor decay. A contractive Fourier projection detects the $q=1$ successor spine, on which the cofactor twist disappears completely. This gives a full phase diagram, not a finite-cutoff heuristic.

The same theorem also identifies the obstruction. At $s=0$, the pure cofactor roof would assign the attractive cycle weight $Q^{-u}$, but its successor component is the unweighted unilateral shift. The matrix is never trace class and is noncompact whenever bounded. Restoring endpoint decay produces an honest Fredholm determinant but assigns the $Q=2$ cycle the factorial weight

$$\left(\frac{(2k-1)!}{(k-1)!}\right)^{-2s}.$$

Unitary characters supply phases only: all $C_k$ carry the same phase $\chi(2)$. We call this the *Fredholm trilemma*.

The regular group lift sharpens the distinction. Relative to its natural semifinite group trace it is $L^1$ for $\Re s>1/2$, yet it is not an ordinary compact operator because of infinite deck multiplicity. Moreover, the neutral group trace sees no periodic path and its normalized local determinant is exactly one. Semifinite integrability, ordinary Fredholm theory, and neutral recurrence are therefore three different statements.

Our contributions are:

1.  an exact positive-holonomy and gauge theorem for the source cofactor;

2.  complete $Q=2$ and atomic-holonomy classifications, with exact connected character coefficients;

3.  the sharp two-parameter trace-class theorem and the separate regular lift analysis;

4.  a source-level no-go showing that abelian product holonomy is blind to the index $k$, stable under positive-inventory controls.

These results are constructive but not a Riemann representation. For every atom $p$, the graph produces an infinite grid $(p,k)$, not one primitive orbit per rational prime, and its honest endpoint roofs are factorial. The strict evaluation is therefore

$$\begin{aligned}
(&\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
 &\mathrm{A1\_WEAK},\\
 &\mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 &\mathrm{A3\_FAIL},\\
 &\mathrm{A4\_FAIL}).
\end{aligned}$$

with $\mathrm{ROUTE\_A\_REJECTED}$. No target-zero data enter any theorem, and Route B remains locked.

#### Organization.

fixes the literature boundary. defines the symbolic object and determinant conventions. prove the algebraic classification. resolves connected coefficients. prove the scalar and lifted operator theorems. give the no-go and controls, and records the route decision.

# Classical machinery and the model-specific boundary {#sec:classical}

The general ingredients of SD-C24 are classical. Determinant and primitive cycle expansions for shifts go back to @BowenLanford1970; the broader periodic-orbit zeta framework is developed systematically by @ParryPollicott1990. Twisted Perron--Frobenius operators and dynamical $L$-functions appear in @AdachiSunada1987. Voltage assignments organize graph coverings in @GrossTucker1977, and graph-cover zeta functions with multivariable weights are treated by @StarkTerras1996. We use this language to locate the construction, not to claim any of these mechanisms as new.

Infinite covers require a trace distinction. The $L^2$-zeta framework of @Clair2009 and the amenable group-extension approximation studied by @Sharp2020 are close conceptual precedents for traces per fundamental domain. In SD-C24 the regular deck group is the countable abelian group $\mathbb Q_{>0}^{\times}$, and the decisive calculation is unusually stark: no base cycle has identity holonomy. The resulting semifinite determinant is locally one, while the ordinary lifted operator remains noncompact.

The cohomological vocabulary is also standard. Livšic theory relates periodic data and cocycle coboundaries under dynamical regularity hypotheses; see, for example, the matrix-cocycle theorem of @Kalinin2011. We do not invoke such a theorem on the present countable graph. The exact identity

$$q(n,d)=\frac nd\left(1+\frac1n\right)$$

is proved directly and contains its own gauge boundary.

For operator determinants we rely only on standard trace-ideal facts after proving trace class for the concrete matrix; @Simon1977 is the reference point. Recent generalized weighted zeta formulas on finite digraphs, such as @IshikawaMorita2026, show that weighted Euler, Hashimoto, and Ihara expressions remain active adjacent machinery. They do not supply the successor--divisor cofactor classification or the Schatten phase diagram below.

L0.26YY Source family & Shared mechanism & Difference here\
Bowen--Lanford; Parry--Pollicott & trace, primitive, and repetition expansions & concrete countable graph, cofactor classes, and sharp nuclear domain\
Adachi--Sunada & character-twisted dynamical operators & source-derived multiplicative cofactor and exact class census\
Gross--Tucker; Stark--Terras & voltages, covers, and cycle weights & infinite successor--divisor grammar and endpoint operator\
Clair; Sharp & infinite/group extensions and normalized traces & empty neutral periodic sector and separate ordinary noncompactness\
Kalinin & cocycle cohomology and periodic data & elementary exact gauge identity; no Livšic theorem invoked\
Simon & trace ideals and Fredholm determinants & candidate-specific iff threshold proved from the matrix\
Ishikawa--Morita & generalized weighted finite-digraph zeta & countable graph and two-parameter Schatten theorem\

The scoped search behind this paper combined the phrases "successor--divisor graph," "cofactor cocycle," "multiplicative holonomy," "group extension of a countable Markov shift," and "twisted graph zeta," including 2024--2026 records. We found no directly comparable analysis that combines

$$Q(\gamma)=\prod(1+1/n),
 \qquad Q=2\iff\gamma=C_k,$$

with the exact two-parameter trace-class domain proved here. This is a search-bounded statement, not a proof of priority. In particular, we do not claim invention of character twists, voltage graphs, group traces, cocycle gauges, or Fredholm trace logarithms.

Two further boundaries matter. First, $L_{s,u}$ is a weighted vertex adjacency on $\ell^2(V)$, not a Ruelle operator on a Hölder function space. Second, a coefficient of the connected trace logarithm records one primitive class and its repetitions; a coefficient of the determinant itself can mix products of distinct primitives. All holonomy resolution below is therefore performed on the normalized germ of $-\log D$.

# Source-derived graph, cocycle, and operators {#sec:source}

## Full-shift skeleton

Let $F_n=A_n^{\mathbb Z}$ denote the full shift on an $n$-letter alphabet, up to topological conjugacy. We freeze

$$F_m\mathbin{\boxtimes}F_n:=F_{A_m\times A_n}\cong F_{mn},
 \qquad
 F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n}.$$

Here $\boxplus$ means alphabet disjoint union followed by the full-shift functor; it is not the categorical coproduct in a category of subshifts. The successor and entropy are

$$S(F_n)=F_n\boxplus F_1\cong F_{n+1},
 \qquad h(F_n)=\log n.$$

The vertex set is $V=\{2,3,\ldots\}$, with $n$ representing $F_n$. An edge is an exposed tensor factorization:

$$n\to d
 \quad\Longleftrightarrow\quad
 d\ge2,\quad d\mid n+1
 \quad\Longleftrightarrow\quad
 S(F_n)\cong F_d\mathbin{\boxtimes}F_q.
\label{eq:edge-rule}$$

The factor witness is unique and defines the cofactor label

$$q(n,d)=\frac{n+1}{d}\in\mathbb N_{\ge1}.
\label{eq:cofactor}$$

The one-sided countable Markov shift is

$$X_G^+=\{(n_0,n_1,\ldots)\in V^{\mathbb N}:n_j\to n_{j+1}\}.$$

No primality predicate occurs in [\[eq:edge-rule,eq:cofactor\]](#eq:edge-rule,eq:cofactor){reference-type="ref" reference="eq:edge-rule,eq:cofactor"}. Rational primes will enter only after freezing, as the atoms of the coefficient monoid used to evaluate the resulting ledger.

## Monoid, group completion, and periodic conventions

Let

$$\mathsf M=(\mathbb N_{\ge1},\cdot),
 \qquad
 \Gamma=\operatorname{gp}(\mathsf M)=\mathbb Q_{>0}^{\times}.$$

Every edge voltage $q(n,d)$ lies in $\mathsf M\subset\Gamma$. For a rooted closed path $\gamma=(n_0,\ldots,n_{r-1})$, with $n_r=n_0$, define

$$Q(\gamma)=\prod_{j=0}^{r-1}q(n_j,n_{j+1}),
 \qquad
 N(\gamma)=\prod_{j=0}^{r-1}n_j.$$

Directed paths are identified under cyclic rotation when called orbits; reflection is not quotiented. A primitive orbit is not a positive temporal power of a shorter orbit.

The compact dual

$$\widehat\Gamma\cong\prod_{p\ \mathrm{prime}}\mathbb T$$

has normalized Haar measure $\,\mathrm d\chi$, with convention

$$\int_{\widehat\Gamma}\overline{\chi(m)}\chi(g)\,\,\mathrm d\chi
 =\mathbf 1_{\{g=m\}}.
\label{eq:haar}$$

This is coefficient extraction in a source-label group, not a spectral transform of the Riemann zeta function.

## Roofs and scalar fibers

The endpoint and cofactor roofs are

$$\tau(n,d)=\log n+\log d,
 \qquad
 \rho(n,d)=\log q(n,d).$$

On $\mathcal H=\ell^2(V)$, with standard basis $e_n$, use the column-source weighted adjacency

$$L_{s,u}e_n=
 \sum_{\substack{d\ge2\\d\mid n+1}}
 (nd)^{-s}q(n,d)^{-u}e_d.
\label{eq:Lsu}$$

For a unitary character $\chi\in\widehat\Gamma$, set

$$L_{s,\chi}e_n=
 \sum_{\substack{d\ge2\\d\mid n+1}}
 (nd)^{-s}\chi(q(n,d))e_d.
\label{eq:Lschi}$$

Around a closed path, endpoint weights telescope by cyclicity to

$$\prod_j(n_jn_{j+1})^{-s}=N(\gamma)^{-2s}.
\label{eq:endpoint-cycle-weight}$$

Thus the full power-twist weight is

$$w_{s,u}(\gamma)=N(\gamma)^{-2s}Q(\gamma)^{-u}.$$

The factor two in the endpoint exponent is part of the source roof and will not be changed after target comparison.

## Scalar and lifted determinant conventions

Whenever $L_{s,u}\in\mathcal S_1$, define

$$D(s,u;z)=\det_{\mathcal H}(I-zL_{s,u}).$$

For a character fiber, write

$$D_\chi(s,z)=\det_{\mathcal H}(I-zL_{s,\chi}).$$

These are entire in $z$, and near $z=0$,

$$-\log D_\chi(s,z)=
 \sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_{s,\chi}^r.
\label{eq:trace-log}$$

The logarithm is the normalized local germ. No global branch through determinant zeros is asserted.

For the regular representation $\lambda$ of $\Gamma$, define on $\mathcal H\otimes\ell^2(\Gamma)$

$$\mathbb L_s(e_n\otimes\delta_g)=
 \sum_{\substack{d\ge2\\d\mid n+1}}
 (nd)^{-s}e_d\otimes\delta_{q(n,d)g}.
\label{eq:regular-lift}$$

Its natural semifinite algebra and trace are

$$\mathcal N=B(\mathcal H)\bar\otimes L(\Gamma),
 \qquad
 \Phi=\operatorname{Tr}\bar\otimes\tau_\Gamma.$$

When its trace series is defined, the normalized local semifinite determinant means

$$\det_\Phi(I-z\mathbb L_s)=
 \exp\left[-\sum_{r\ge1}\frac{z^r}{r}
 \Phi(\mathbb L_s^r)\right].
\label{eq:phi-det}$$

It is not an ordinary Fredholm determinant of $\mathbb L_s$ on the lifted Hilbert space.

# Positive holonomy, neutral extinction, and gauge {#sec:holonomy}

The cofactor is positive on edges, but its periodic product is more rigid than positivity alone suggests.

[\[thm:positive-holonomy\]]{#thm:positive-holonomy label="thm:positive-holonomy"} Every closed path $\gamma=(n_0,\ldots,n_{r-1})$ satisfies

$$Q(\gamma)=
 \prod_{j=0}^{r-1}\left(1+\frac1{n_j}\right)
 \in\{2,3,\ldots\}.
\label{eq:positive-holonomy}$$

The edge equation gives

$$Q(\gamma)
 =\prod_j\frac{n_j+1}{n_{j+1}}
 =\frac{\prod_j(n_j+1)}{\prod_jn_{j+1}}.$$

Because the path closes, $\prod_jn_{j+1}=\prod_jn_j$, giving [\[eq:positive-holonomy\]](#eq:positive-holonomy){reference-type="ref" reference="eq:positive-holonomy"}. The original expression is a product of positive integers, whereas every factor in the telescoped real expression is strictly greater than one. Hence $Q(\gamma)$ is an integer at least two.

[\[cor:no-neutral\]]{#cor:no-neutral label="cor:no-neutral"} The skew graph

$$(n,g)\longrightarrow(d,q(n,d)g)$$

has no periodic path. Equivalently, the identity coefficient of every rooted group trace vanishes.

A lifted path closes in the deck coordinate exactly when its base holonomy is one. This is excluded by [\[thm:positive-holonomy\]](#thm:positive-holonomy){reference-type="ref" reference="thm:positive-holonomy"}.

The conclusion is deliberately stronger and less useful than a selective neutral sector: it removes every recurrent orbit. We postpone the operator consequence $\det_\Phi=1$ until [8](#sec:lift){reference-type="ref" reference="sec:lift"}, where its trace domain and ordinary compactness boundary are explicit.

[\[thm:gauge\]]{#thm:gauge label="thm:gauge"} On every allowed edge,

$$q(n,d)=\frac nd\left(1+\frac1n\right).
\label{eq:gauge}$$

Thus the multiplicative cocycle is cohomologous to the source potential $a(n)=1+1/n$, and

$$Q(\gamma)=\prod_{n\in\gamma}a(n).$$

For $D_ue_n=n^ue_n$, on the algebraic core,

$$D_u^{-1}L_{s,u}D_u e_n=
 \sum_{\substack{d\ge2\\d\mid n+1}}
 (nd)^{-s}\left(1+\frac1n\right)^{-u}e_d.
\label{eq:operator-gauge}$$

If $u\in i\mathbb R$, this is a unitary conjugacy. If $\Re u\ne0$, it is only an algebraic or finite-window identity unless a separate bounded-similarity theorem is proved.

Since $dq=n+1$,

$$q=\frac{n+1}{d}=\frac nd\frac{n+1}{n}.$$

The factor $n/d$ is a vertex coboundary and telescopes on a closed path. For [\[eq:operator-gauge\]](#eq:operator-gauge){reference-type="ref" reference="eq:operator-gauge"}, conjugation changes the edge coefficient by

$$d^{-u}q^{-u}n^u
 =\left(\frac n{dq}\right)^u
 =\left(1+\frac1n\right)^{-u}.$$

Finally $D_u$ is unitary precisely when $|n^u|=1$ for all $n$, which holds for purely imaginary $u$. Otherwise $D_u$ or its inverse is unbounded.

The cocycle is not a pure coboundary: its periodic products are nontrivial by [\[thm:positive-holonomy\]](#thm:positive-holonomy){reference-type="ref" reference="thm:positive-holonomy"}. The gauge theorem says that its periodic data are already encoded by a positive source potential, not that they disappear.

summarizes the three levels used below. The base cocycle supplies the periodic label. The regular lift tests the neutral class. Character fibers retain all labels as phases and allow a chosen non-neutral coefficient to be reconstructed by Haar orthogonality.

# Exact minimal and atomic holonomy classes {#sec:atomic}

The positive integer monoid turns the smallest non-neutral class into a complete orbit classification.

[\[thm:q2\]]{#thm:q2 label="thm:q2"} A closed path satisfies $Q(\gamma)=2$ if and only if, up to cyclic rotation,

$$\gamma=C_k=(k,k+1,\ldots,2k-1),
 \qquad k\ge2.
\label{eq:Ck}$$

Each $C_k$ is simple and primitive, has length $k$, and has endpoint mass

$$M_k=N(C_k)=\frac{(2k-1)!}{(k-1)!}.
\label{eq:Mk}$$

Write $Q(\gamma)=\prod_jq_j$, where every $q_j$ is a positive integer. If the product equals two, exactly one factor equals two and every other factor equals one. An edge has $q(n,d)=1$ exactly when $d=n+1$. Rotate the closed path so that the unique $q=2$ edge is the closing edge, and denote its target by $k$. The remaining path is a successor run

$$k\to k+1\to\cdots\to N\to k.$$

The closing cofactor equation gives $2=(N+1)/k$, hence $N=2k-1$. Conversely, [\[eq:Ck\]](#eq:Ck){reference-type="ref" reference="eq:Ck"} has $q=1$ on every successor and $q=2$ on its closing edge. Its vertices are distinct, so it is simple and cannot be a nontrivial temporal power. Its vertex count and product give the claimed length and [\[eq:Mk\]](#eq:Mk){reference-type="ref" reference="eq:Mk"}.

This theorem is stronger than a census: it gives exactly one primitive rotation class in holonomy two at every length $k\ge2$, with no omitted cycles.

[\[thm:atomic\]]{#thm:atomic label="thm:atomic"} Let $p$ be an atom of $(\mathbb N_{\ge1},\cdot)$, equivalently a rational prime. Then $Q(\gamma)=p$ if and only if, up to rotation,

$$C_{k,p}=(k,k+1,\ldots,pk-1),
 \qquad k\ge2.
\label{eq:Ckp}$$

The orbit is simple and primitive, with

$$\ell(C_{k,p})=(p-1)k,
 \qquad
 M_{k,p}=N(C_{k,p})=\frac{(pk-1)!}{(k-1)!}.
\label{eq:Mkp}$$

Atomicity of $p=\prod_jq_j$ forces exactly one cofactor to equal $p$ and all others to equal one. Rotate after that nontrivial edge. The $q=1$ segment is a successor run beginning at $k$, and the closing equation $(N+1)/k=p$ gives $N=pk-1$. The converse follows by direct substitution. The inclusive vertex count is $(pk-1)-k+1=(p-1)k$, and multiplying consecutive vertices gives [\[eq:Mkp\]](#eq:Mkp){reference-type="ref" reference="eq:Mkp"}. Simplicity implies primitivity.

[\[cor:no-atomic-repeat\]]{#cor:no-atomic-repeat label="cor:no-atomic-repeat"} If a temporal power $\eta^\nu$ has atomic holonomy $p$, then $\nu=1$. In particular, the class $Q=2$ receives no repeated-orbit contribution.

By [\[thm:positive-holonomy\]](#thm:positive-holonomy){reference-type="ref" reference="thm:positive-holonomy"}, $Q(\eta)\ge2$, and $Q(\eta^\nu)=Q(\eta)^\nu$. An atom is not a nontrivial positive power.

::: {#tab:atomic-ledger}
  Holonomy     Primitive family            Period     Endpoint mass
  ------------ --------------------------- ---------- ------------------
  $2$          $C_k=(k,\ldots,2k-1)$       $k$        $(2k-1)!/(k-1)!$
  $p$ atomic   $C_{k,p}=(k,\ldots,pk-1)$   $(p-1)k$   $(pk-1)!/(k-1)!$

  : Exact atomic-holonomy ledger. The graph is frozen before the atom $p$ is used to classify a coefficient.
:::

The uniformity in $p$ is positive source structure: no table constructs the edges. It is also the immediate target obstruction. Each atom has infinitely many primitive representatives, indexed by $k$, rather than one representative.

# Character-resolved connected Fredholm ledger {#sec:ledger}

Character resolution is meaningful only if fixed-period group traces have finite support. That follows from the inherited confinement geometry, for which we include the short proof.

[\[lem:confinement\]]{#lem:confinement label="lem:confinement"} Every length-$r$ closed path lies in

$$\{2,3,\ldots,2r-1\}.$$

Let $M$ be the largest visited vertex. The edge leaving an occurrence of $M$ cannot be the successor edge, because that would visit $M+1$. Its target $d$ is therefore a proper divisor of $M+1$, so $d\le(M+1)/2$. Every edge increases its source by at most one. The remaining $r-1$ edges can return to $M$ only if

$$M\le d+r-1\le\frac{M+1}{2}+r-1,$$

which rearranges to $M\le2r-1$.

For a rooted length-$r$ closed path, [\[eq:endpoint-cycle-weight\]](#eq:endpoint-cycle-weight){reference-type="ref" reference="eq:endpoint-cycle-weight"} gives the coefficient $N(\gamma)^{-2s}$. Define the finite group-algebra trace

$$\mathcal T_r(s)=
 \sum_{\gamma\in\operatorname{Fix}_r}N(\gamma)^{-2s}[Q(\gamma)]
\label{eq:group-trace}$$

and the connected germ

$$\mathcal L_s(z)=\sum_{r\ge1}\frac{z^r}{r}\mathcal T_r(s).
\label{eq:connected-ledger}$$

At every fixed $r$, [\[lem:confinement\]](#lem:confinement){reference-type="ref" reference="lem:confinement"} makes [\[eq:group-trace\]](#eq:group-trace){reference-type="ref" reference="eq:group-trace"} an exact finite sum.

[\[thm:coefficient\]]{#thm:coefficient label="thm:coefficient"} For $m\in\Gamma$, in the scalar trace-class half-plane and for sufficiently small $|z|$,

$$\begin{aligned}
 \mathcal H_m(s,z)
 &:=[m]\mathcal L_s(z) \notag\\
 &=\int_{\widehat\Gamma}\overline{\chi(m)}
   [-\log D_\chi(s,z)]\,\,\mathrm d\chi \notag\\
 &=\sum_{\substack{[\gamma]\ \mathrm{primitive},\ \nu\ge1\\
                    Q(\gamma)^\nu=m}}
   \frac{z^{\nu\ell(\gamma)}}{\nu}
   N(\gamma)^{-2s\nu}.
\label{eq:coefficient-formula}\end{aligned}$$

Evaluate the finite coefficient [\[eq:group-trace\]](#eq:group-trace){reference-type="ref" reference="eq:group-trace"} at a character. The result is $\operatorname{Tr}L_{s,\chi}^r$. Insert it into the local trace logarithm [\[eq:trace-log\]](#eq:trace-log){reference-type="ref" reference="eq:trace-log"}, multiply by $\overline{\chi(m)}$, and use Haar orthogonality [\[eq:haar\]](#eq:haar){reference-type="ref" reference="eq:haar"}. Regrouping rooted closed paths by primitive rotation class and temporal repetition gives the last line.

The use of $-\log D_\chi$ is essential. A Fourier coefficient of $D_\chi$ itself can multiply holonomies from distinct primitive factors and would not isolate one connected orbit class.

[\[thm:h2\]]{#thm:h2 label="thm:h2"} In the honest Fredholm half-plane,

$$\boxed{
 \mathcal H_2(s,z)=
 \sum_{k\ge2}z^k
 \left(\frac{(2k-1)!}{(k-1)!}\right)^{-2s}.}
\label{eq:H2}$$

At rooted trace level,

$$\mathcal T_r(s)=
 r\left(\frac{(2r-1)!}{(r-1)!}\right)^{-2s}.
\label{eq:T2r}$$

By [\[thm:q2\]](#thm:q2){reference-type="ref" reference="thm:q2"}, $C_r$ is the unique primitive rotation class of period $r$ and holonomy two. Its $r$ rooted rotations give [\[eq:T2r\]](#eq:T2r){reference-type="ref" reference="eq:T2r"}; the factor $1/r$ in [\[eq:connected-ledger\]](#eq:connected-ledger){reference-type="ref" reference="eq:connected-ledger"} cancels them. excludes repetitions.

The series in [\[eq:H2\]](#eq:H2){reference-type="ref" reference="eq:H2"} has infinite radius in $z$ when $\Re s>0$, radius one when $\Re s=0$, and radius zero when $\Re s<0$. Only the subdomain $\Re s>1/2$ will arise from the whole Fredholm operator. Convergence of one coefficient for $0<\Re s\le1/2$ is not continuation of the determinant.

[\[cor:Hp\]]{#cor:Hp label="cor:Hp"} For every atom $p$,

$$\boxed{
 \mathcal H_p(s,z)=
 \sum_{k\ge2}z^{(p-1)k}
 \left(\frac{(pk-1)!}{(k-1)!}\right)^{-2s}.}
\label{eq:Hp}$$

No repetition contributes.

[\[cor:character-persistence\]]{#cor:character-persistence label="cor:character-persistence"} For every unitary character $\chi$, the primitive factor associated to $C_k$ is

$$1-z^kM_k^{-2s}\chi(2).$$

It is nontrivial for every $k\ge2$, and all canonical cycles receive the same holonomy phase.

The exact coefficient is therefore both the strongest positive result and a no-cancellation certificate. Within the $Q=2$ class there is one positive term at each length and no repeated term. Any vanishing observed only after summing different $Q$-classes is neither orbit deletion nor a stable selector.

# Sharp two-parameter trace-class theorem {#sec:traceclass}

The endpoint and cofactor roofs control different directions in the matrix. The following theorem identifies both boundaries exactly.

[\[thm:traceclass\]]{#thm:traceclass label="thm:traceclass"} Let $\sigma=\Re s$ and $a=\Re u$. Then

$$\boxed{
 L_{s,u}\in\mathcal S_1(\mathcal H)
 \quad\Longleftrightarrow\quad
 \sigma>\frac12
 \quad\text{and}\quad
 \sigma+a>\frac12.}
\label{eq:S1-domain}$$

On this domain, $(s,u)\mapsto L_{s,u}$ is locally holomorphic in trace norm, and $D(s,u;z)$ is jointly holomorphic in $(s,u,z)$ and entire in $z$.

Group the matrix by output row $d$. Every source entering row $d$ is $n=dq-1$. The restriction $n\ge2$ gives

$$q_0(2)=2,
 \qquad q_0(d)=1\quad(d\ge3).$$

Set

$$R_d(s,u)=
 \sum_{q\ge q_0(d)}[d(dq-1)]^{-s}q^{-u}E_{d,dq-1}.
\label{eq:row-block}$$

Each $R_d$ is rank one. Its trace norm equals its Hilbert--Schmidt norm, and

$$\|R_d(s,u)\|_1^2=
 \sum_{q\ge q_0(d)}
 d^{-2\sigma}(dq-1)^{-2\sigma}q^{-2a}.
\label{eq:row-norm}$$

Because $dq\ge3$, one has

$$\frac23dq\le dq-1<dq.$$

Consequently, whenever $\sigma+a>1/2$,

$$\|R_d(s,u)\|_1^2
 \asymp_{\sigma,a}
 d^{-4\sigma}
 \sum_{q\ge q_0(d)}q^{-2(\sigma+a)}
 \asymp_{\sigma,a}d^{-4\sigma}
\label{eq:row-asymptotic}$$

for $d\ge3$. The upper constant is uniform in $d$, and the $q=1$ term supplies the lower constant. Therefore

$$\sum_{d\ge2}\|R_d(s,u)\|_1<\infty$$

exactly when $\sigma>1/2$. Under both strict inequalities, the sum $\sum_dR_d$ converges in trace norm and agrees with [\[eq:Lsu\]](#eq:Lsu){reference-type="ref" reference="eq:Lsu"} on finitely supported vectors.

On a compact subset of the two strict half-planes, both exponent margins are uniform. Differentiating the entries introduces only powers of $\log d$, $\log(dq-1)$, and $\log q$, which are absorbed by a smaller positive margin in [\[eq:row-asymptotic\]](#eq:row-asymptotic){reference-type="ref" reference="eq:row-asymptotic"}. The row series is therefore locally trace-norm holomorphic. Standard Fredholm theory [@Simon1977] yields the determinant statement.

If the frozen matrix had a bounded extension, each fixed output row would be an $\ell^2$ coefficient vector. At $d=2$, its squared norm is

$$\sum_{q\ge2}|[2(2q-1)]^{-s}q^{-u}|^2
 \asymp
 \sum_{q\ge2}q^{-2(\sigma+a)}.$$

This diverges when $\sigma+a\le1/2$. In that region the matrix is not even bounded, hence cannot be trace class.

Let $U_te_n=\mathrm e^{int}e_n$. The first-superdiagonal Fourier projection

$$\mathcal P_1(T)=\frac1{2\pi}
 \int_0^{2\pi}\mathrm e^{-it}U_tTU_t^{-1}\,\,\mathrm dt
\label{eq:fourier-projection}$$

is contractive on $\mathcal S_1$. On a matrix unit $E_{d,n}$, the conjugation has phase $\mathrm e^{i(d-n)t}$, so [\[eq:fourier-projection\]](#eq:fourier-projection){reference-type="ref" reference="eq:fourier-projection"} retains exactly $d=n+1$. In the successor--divisor graph this is the cofactor-one spine. Therefore

$$\mathcal P_1(L_{s,u})e_n=
 [n(n+1)]^{-s}e_{n+1}.
\label{eq:successor-extraction}$$

The twist disappears because $1^{-u}=1$. The singular values of this weighted unilateral shift are the moduli of its weights, so

$$\|\mathcal P_1(L_{s,u})\|_1
 =\sum_{n\ge2}[n(n+1)]^{-\sigma}.$$

This converges exactly when $\sigma>1/2$. Trace-class membership of $L_{s,u}$ would force membership of its contractive projection, proving the remaining necessity.

[\[cor:character-S1\]]{#cor:character-S1 label="cor:character-S1"} For every $\chi\in\widehat\Gamma$,

$$L_{s,\chi}\in\mathcal S_1
 \quad\Longleftrightarrow\quad
 \Re s>\frac12.
\label{eq:character-domain}$$

Unitary phases do not change the row norms, and $\chi(1)=1$ leaves [\[eq:successor-extraction\]](#eq:successor-extraction){reference-type="ref" reference="eq:successor-extraction"} unchanged. The proof of [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"} with $a=0$ applies uniformly in $\chi$.

L0.21L0.24Y Region & Exact conclusion & Witness\
$\sigma>1/2,\ \sigma+a>1/2$ & $L_{s,u}\in\mathcal S_1$ & summable rank-one output rows\
$\sigma+a\le1/2$ & no bounded extension & fixed output row $d=2$ is not in $\ell^2$\
$\sigma\le1/2$ & not trace class & cofactor-one successor Fourier component\
$u=it$ & base threshold $\sigma>1/2$ & phases preserve all row magnitudes\

The exact iff statement is the analytic advance of SD-C24. It also explains why increasing cofactor decay cannot repair the endpoint boundary: the successor spine carries the identity label and is invisible to $u$.

# Regular lift: semifinite integrability and ordinary noncompactness {#sec:lift}

The regular lift [\[eq:regular-lift\]](#eq:regular-lift){reference-type="ref" reference="eq:regular-lift"} admits a natural trace per deck fiber. Its semifinite $L^1$ theorem parallels the scalar character theorem, but it does not imply ordinary compactness.

[\[thm:lift-L1\]]{#thm:lift-L1 label="thm:lift-L1"} In $(\mathcal N,\Phi)$,

$$\mathbb L_s\in L^1(\mathcal N,\Phi)
 \quad\Longleftrightarrow\quad
 \Re s>\frac12.
\label{eq:lift-domain}$$

For output row $d$, set

$$\mathbb R_d=
 \sum_{q\ge q_0(d)}[d(dq-1)]^{-s}
 E_{d,dq-1}\otimes\lambda(q).$$

Distinct $q$'s have distinct input matrix units, so

$$\mathbb R_d\mathbb R_d^*
 =\left(\sum_{q\ge q_0(d)}
 |d(dq-1)|^{-2\sigma}\right)E_{dd}\otimes1.$$

It follows that

$$\|\mathbb R_d\|_{L^1(\Phi)}
 =\left(\sum_q|d(dq-1)|^{-2\sigma}\right)^{1/2}
 \asymp d^{-2\sigma}$$

when $\sigma>1/2$. Summing over $d$ proves sufficiency. The trace-preserving first-superdiagonal Fourier projection retains the same successor block as [\[eq:successor-extraction\]](#eq:successor-extraction){reference-type="ref" reference="eq:successor-extraction"}, whose $L^1$-norm is $\sum_n[n(n+1)]^{-\sigma}$. This proves necessity.

[\[thm:lift-noncompact\]]{#thm:lift-noncompact label="thm:lift-noncompact"} For $\Re s>1/2$, the nonzero operator $\mathbb L_s$ is not compact on $\mathcal H\otimes\ell^2(\Gamma)$.

The left deck shifts in [\[eq:regular-lift\]](#eq:regular-lift){reference-type="ref" reference="eq:regular-lift"} commute with the right regular representation $\rho$ of $\Gamma$. Choose a unit vector $\xi$ such that $\mathbb L_s\xi\ne0$, and choose a sequence $g_j$ escaping every finite subset of $\Gamma$. The vectors $\rho(g_j)\xi$ are bounded and, after the standard finite-support approximation, weakly converge to zero. Their images are

$$\mathbb L_s\rho(g_j)\xi
 =\rho(g_j)\mathbb L_s\xi,$$

all with the same nonzero norm. A compact operator sends a weakly null bounded sequence to a norm-null sequence, yielding a contradiction.

[\[cor:phi-one\]]{#cor:phi-one label="cor:phi-one"} For $\Re s>1/2$,

$$\Phi(\mathbb L_s^r)=0\quad(r\ge1),
 \qquad
 \det_\Phi(I-z\mathbb L_s)=1$$

as a normalized local trace-series identity.

The group trace extracts the identity coefficient. By [\[cor:no-neutral\]](#cor:no-neutral){reference-type="ref" reference="cor:no-neutral"}, no lifted periodic path has identity holonomy, so all power traces vanish. Substitution into [\[eq:phi-det\]](#eq:phi-det){reference-type="ref" reference="eq:phi-det"} gives one.

L0.25L0.25Y Question & Answer & Reason\
Ordinary compact on $\mathcal H\otimes\ell^2(\Gamma)$? & No & infinite right-translation copies of every nonzero image\
Semifinite $L^1(\mathcal N,\Phi)$? & Yes iff $\Re s>1/2$ & row $L^1$ sum and successor extraction\
Neutral local determinant? & $1$ & no closed path has $Q=1$\

The last line earns no arithmetic credit. It is a determinant made trivial by a trace that is blind to every recurrent orbit. Equally, the middle line does not promote the first line to an ordinary Fredholm theorem.

# The Fredholm trilemma {#sec:trilemma}

The exact phase diagram separates three natural attempts to exploit the cofactor.

## Pure cofactor roof

Set $s=0$ in [\[eq:Lsu\]](#eq:Lsu){reference-type="ref" reference="eq:Lsu"} and write

$$Q_ue_n=\sum_{d\mid n+1,\ d\ge2}q(n,d)^{-u}e_d.$$

[\[thm:pure-obstruction\]]{#thm:pure-obstruction label="thm:pure-obstruction"} For every $u\in\mathbb C$, $Q_u$ is not trace class. Whenever it has a bounded extension, it is noncompact.

The trace-class conclusion follows immediately from [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"}, which would require $0>1/2$. More directly, the Fourier component [\[eq:successor-extraction\]](#eq:successor-extraction){reference-type="ref" reference="eq:successor-extraction"} is now the unweighted unilateral shift

$$e_n\longmapsto e_{n+1}.$$

Fourier averaging maps compact operators to compact operators, while this shift is not compact. Thus a bounded $Q_u$ cannot be compact.

For example, Schur's test proves boundedness when $\Re u>1$: the row and column sums are controlled by the convergent series $\sum_{q\ge1}q^{-\Re u}$. We do not need a complete boundedness classification in the remaining strip.

[\[thm:pure-series\]]{#thm:pure-series label="thm:pure-series"} As a formal or $|z|<1$ connected series,

$$\mathcal H_2^{\mathrm{cof}}(u,z)
 =2^{-u}\sum_{k\ge2}z^k
 =2^{-u}\frac{z^2}{1-z}.
\label{eq:pure-H2}$$

It diverges at $z=1$ for every finite $u$. More generally, for an atom $p$,

$$\mathcal H_p^{\mathrm{cof}}(u,z)
 =p^{-u}\frac{z^{2(p-1)}}{1-z^{p-1}},
 \qquad |z|<1.$$

Every $C_k$ has cofactor weight $2^{-u}$ and period $k$; summing over $k\ge2$ gives [\[eq:pure-H2\]](#eq:pure-H2){reference-type="ref" reference="eq:pure-H2"}. For $C_{k,p}$, the period is $(p-1)k$ and the cofactor weight is $p^{-u}$, giving the second geometric series.

The formula [\[eq:pure-H2\]](#eq:pure-H2){reference-type="ref" reference="eq:pure-H2"} is not a Fredholm coefficient of a trace-class whole operator. Its attractive atomic weight comes with infinite multiplicity at the unmarked specialization.

## Endpoint regularization

In the honest domain [\[eq:S1-domain\]](#eq:S1-domain){reference-type="ref" reference="eq:S1-domain"}, the combined class is

$$\mathcal H_2(s,u;z)=
 2^{-u}\sum_{k\ge2}z^kM_k^{-2s}.
\label{eq:regularized-H2}$$

It is entire in $z$, because $M_k$ grows factorially. The same growth is the arithmetic defect: the orbit indexed by $k$ has roof $2\log M_k$, not an atomic roof $\log2$. For general $p$, the factor $M_{k,p}^{-2s}$ remains.

## Unitary characters

By [\[cor:character-S1\]](#cor:character-S1){reference-type="ref" reference="cor:character-S1"}, a unitary character has the base threshold $\Re s>1/2$. By [\[cor:character-persistence\]](#cor:character-persistence){reference-type="ref" reference="cor:character-persistence"}, it multiplies every canonical primitive by the same nonzero phase $\chi(2)$. It changes no magnitude and deletes no $C_k$.

[\[thm:trilemma\]]{#thm:trilemma label="thm:trilemma"} For the frozen successor--divisor cofactor cocycle, the three natural choices have the following mutually obstructing outcomes:

0.96L0.24L0.30Y Choice & Analytic outcome & Arithmetic outcome\
$s=0$, pure cofactor & never trace class; noncompact whenever bounded & weight $Q^{-u}$, but infinitely many canonical representatives\
endpoint regularized & honest Fredholm determinant in the two-half-plane domain & factorial $M_{k,p}^{-2s}$ dependence\
unitary character & same $\Re s>1/2$ threshold as the base & phases only; every $C_k$ survives\

No choice gives both an honest same-object Fredholm determinant and the one-atom/one-primitive target ledger.

The three rows are respectively [\[thm:pure-obstruction,thm:pure-series\]](#thm:pure-obstruction,thm:pure-series){reference-type="ref" reference="thm:pure-obstruction,thm:pure-series"}, [\[thm:traceclass,eq:regularized-H2\]](#thm:traceclass,eq:regularized-H2){reference-type="ref" reference="thm:traceclass,eq:regularized-H2"}, and [\[cor:character-S1,cor:character-persistence\]](#cor:character-S1,cor:character-persistence){reference-type="ref" reference="cor:character-S1,cor:character-persistence"}. Their conclusions are properties of the frozen graph and weights, so there is no remaining choice among these three that changes the stated ledger.

## First-return collapse

One might attempt to collapse the long successor segments by inducing on edges with $q>1$.

[\[prop:return\]]{#prop:return label="prop:return"} Every $C_k$ becomes one fixed first-return branch indexed by $k\ge2$. Its diagonal entry is $2^{-u}z^k$ for the pure cofactor-time marking and $2^{-u}z^kM_k^{-2s}$ for the endpoint-regularized marking.

At $s=0,z=1$, the induced pure diagonal has the constant nonzero entry $2^{-u}$ with infinite multiplicity and is noncompact. Endpoint regularization restores summability only while retaining the factorial $k$-ledger.

By [\[thm:q2\]](#thm:q2){reference-type="ref" reference="thm:q2"}, every $C_k$ has exactly one $q>1$ edge. It therefore defines one return branch. Multiplication of its time, cofactor, and endpoint weights gives the two entries. The compactness and summability claims are the corresponding diagonal-operator criteria.

Thus Poincaré collapse trades the original graph for a countable return grammar; it does not turn the family indexed by $k$ into a single atom.

# Controls and the scoped abelian no-go {#sec:controls}

The canonical family is not an artifact of the native endpoint inventory. It is fixed by admissibility and the cofactor word.

[\[thm:blindness\]]{#thm:blindness label="thm:blindness"} Let $F:\Gamma\to\mathcal A$ be any map into any set, algebra, or coefficient space. The statistic

$$\gamma\longmapsto F(Q(\gamma))$$

has the common value $F(2)$ on every $C_k$, $k\ge2$. Consequently, no statistic depending only on the abelian product $Q$ can distinguish prime from composite values of $k$.

By [\[thm:q2\]](#thm:q2){reference-type="ref" reference="thm:q2"}, $Q(C_k)=2$ for all $k\ge2$. Substitution gives the common value.

The theorem applies to scalar characters, finite- or infinite-dimensional linear combinations of holonomy coefficients, and holonomy-only masks. It does not apply to a genuinely new ordered-word cocycle: the abelian product has already forgotten how many identity labels precede the closing two.

[\[prop:inventory\]]{#prop:inventory label="prop:inventory"} Let $\mu:V\to(0,\infty)$ be any positive object inventory and weight an edge $n\to d$ by

$$[\mu(n)\mu(d)]^{-s}.$$

The holonomy-two primitive support remains exactly $\{C_k:k\ge2\}$, and its connected coefficient is

$$\mathcal H_{2,\mu}(s,z)=
 \sum_{k\ge2}z^k
 \left(\prod_{n=k}^{2k-1}\mu(n)\right)^{-2s}.
\label{eq:inventory-H2}$$

Positive weights do not change the edge set or the cofactor product, so [\[thm:q2\]](#thm:q2){reference-type="ref" reference="thm:q2"} remains valid. Around $C_k$, every vertex inventory occurs once as a source and once as a target, producing the square in [\[eq:inventory-H2\]](#eq:inventory-H2){reference-type="ref" reference="eq:inventory-H2"}.

Matched controls may use, for example,

$$\mu(n)=n,\quad n+1,\quad n^2+n,\quad n^2+1,\quad 2^n,$$

or a deterministic positive perturbation. Their magnitudes differ, while their holonomy-two support is identical. These are roof controls, not claims that a generic unique-factorization domain carries a canonical additive successor.

L0.28L0.31Y Control & Invariant & Permitted conclusion\
positive inventory substitution & graph, $Q$, and all $C_k$ & magnitudes are not structural selectors\
transported presentation & successor and tensor transported together & theorem is presentation-natural\
character grid & exact finite group-algebra coefficients & verifies Fourier convention, not orbit deletion\
first-return grammar & one branch for every $k$ & compression preserves multiplicity\
successor Fourier extraction & $q=1$ component & analytic lower-bound witness\

## Exact finite audit protocol

The infinite theorems above are analytic and algebraic. A finite program is useful only as a regression certificate. On an induced prefix $V_N=\{2,\ldots,N\}$, a compliant audit should:

1.  construct an edge only from $(n+1)\bmod d=0$, and compute the label by exact division;

2.  verify $\prod q=\prod(n+1)/n$ for each enumerated cycle using rational arithmetic;

3.  certify that every $Q=2$ cycle is a rotation of $C_k$, and, only after freezing, audit several atomic $p$-classes;

4.  propagate sparse dictionaries $(d,Q)\mapsto$ exact weight and verify $[1]\mathcal T_r=0$ and [\[eq:T2r\]](#eq:T2r){reference-type="ref" reference="eq:T2r"};

5.  use a nonaliasing finite character grid to reconstruct the same coefficients;

6.  compare the two row-nuclear boundary witnesses and the first-return diagonals without treating finite growth as proof.

The graph constructor must contain no primality routine, prime list, von Mangoldt weight, Riemann zero, or target-fitted parameter. An atomicity test may appear only in post-freeze evaluation code. These firewalls distinguish classifying a coefficient of a frozen object from compiling the desired coefficient into that object.

## Cancellation firewall

A particular character may make a total scalar trace vanish through cancellation between different holonomy classes. Such a zero does not delete a primitive orbit and need not persist under another character or inventory. Exact Fourier resolution exposes the $Q=2$ coefficient as one nonzero term at every length. We therefore give no selectivity credit to an unresolved scalar cancellation.

# Target comparison and Route-A evaluation {#sec:route}

The marked connected prime Euler ledger is

$$\mathcal E_{\mathbb P}(s,z)=
 \sum_{r\ge1}\frac{z^r}{r}\sum_p p^{-rs},
 \qquad \Re s>1.
\label{eq:target-ledger}$$

It represents one primitive factor per rational prime and its temporal repetitions. SD-C24 differs before analytic continuation or zero comparison:

-   the graph has no period-one closed word;

-   the minimal holonomy class contains one primitive at every length $k\ge2$;

-   each atom $p$ has infinitely many primitives $C_{k,p}$;

-   their periods are $(p-1)k$;

-   their endpoint roofs are $2\log[(pk-1)!/(k-1)!]$, not $\log p$;

-   removing the endpoint roof produces constant atomic weight with infinite multiplicity and a non-Fredholm whole operator.

Selecting all atomic values of $Q$ would be describable after the monoid is frozen, but it still leaves the two-dimensional grid $(p,k)$. Selecting prime values of the auxiliary index $k$ would be a new postselection not supplied by the cofactor product and is forbidden.

L0.12L0.36Y Gate & Verdict & Reason\
A0 & `STRUCTURAL_ARITHMETIC_RELATION` & graph and cofactor use only successor and tensor factorization\
A1 & `WEAK` & exact primitive/repetition classes, but infinitely many representatives per atom\
A2 & `ANALYTIC_DETERMINANT` & scalar fibers are trace class on the sharp domain; neutral lift determinant is trivial\
A3 & `FAIL` & primitive support, period, multiplicity, and roof differ from [\[eq:target-ledger\]](#eq:target-ledger){reference-type="ref" reference="eq:target-ledger"}\
A4 & `FAIL` & no self-adjoint carrier, functional equation, or critical-line mechanism\

Thus the frozen tuple is

$$\boxed{\begin{aligned}
(&\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
 &\mathrm{A1\_WEAK},\\
 &\mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 &\mathrm{A3\_FAIL},\\
 &\mathrm{A4\_FAIL}).
\end{aligned}}
\label{eq:route-tuple}$$

The overall decision is

$$\boxed{\mathrm{ROUTE\_A\_REJECTED}}.$$

The positive labels are

$$\begin{gathered}
 \mathrm{GO\_COFACTOR\_HOLONOMY\_RESOLUTION},\\
 \mathrm{GO\_EXACT\_HOLONOMY\_TWO\_CLASSIFICATION},\\
 \mathrm{GO\_SHARP\_CHARACTER\_FREDHOLM\_DOMAIN}.
\end{gathered}$$

The stop labels are

$$\begin{gathered}
 \mathrm{STOP\_NEUTRAL\_SECTOR},\\
 \mathrm{STOP\_PRIME\_ORBIT\_LEDGER},\\
 \mathrm{CYCLE\_FLOOD},\\
 \mathrm{GAUGE\_REDUCIBLE\_TO\_SOURCE\_POTENTIAL},\\
 \mathrm{PROVES\_TOO\_MUCH},\\
 \mathrm{ROUTE\_B\_LOCKED}.
\end{gathered}$$

No functional equation, Gamma factor, completed divisor, explicit formula, Riemann--von Mangoldt law, Weil compression, RH statement, or Hilbert--Pólya operator is constructed. A2 is not promoted to A3 merely because the candidate's determinant is holomorphic on an open half-plane.

The smallest future symbolic obligation is to leave the abelian product itself. The ordered cofactor word of $C_k$ is $1^{k-1}2$; retaining the numeric identity as a letter would be a new free-word cocycle, not a representation of $\Gamma$. Any later project would first need to prove the finite-state eventual-periodicity barrier and justify an infinite-memory function space without compiling a primality decider. That project is not started here.

# Conclusion {#sec:conclusion}

The successor--divisor cofactor is a genuine arithmetic cocycle of a single symbolic object. It yields positive cycle holonomy, exact atomic-class resolution, a closed holonomy-two connected coefficient, and a sharp two-parameter trace-class theorem. These are substantive positive results.

They also close the most natural abelian holonomy route. Identity-holonomy trace removes all recurrence. Pure cofactor weights retain atomic magnitude but lose compactness. Endpoint weights restore a Fredholm determinant by introducing factorial orbit masses. Unitary characters attach a common phase to every canonical cycle. The ordinary regular lift remains noncompact even where its separate semifinite trace is integrable.

Accordingly, SD-C24 is an exact class-resolution theorem and a sharp Fredholm no-go, not a Riemann determinant. Its strict outcome is $\mathrm{ROUTE\_A\_REJECTED}$, with Route B locked. No target-zero data are needed for that decision.

# Proof details and analytic firewalls {#app:proofs}

## Why the row decomposition is nuclear rather than entrywise

An entrywise $\ell^1$ estimate would sum

$$\sum_{d\ge2}\sum_{q\ge q_0(d)}
 d^{-\sigma}(dq-1)^{-\sigma}q^{-a},$$

which imposes unnecessarily strong exponents. The correct structure is that all entries with the same output $d$ form one rank-one row. The nuclear cost of the row is its $\ell^2$, not $\ell^1$, norm. This is the source of the exact inner threshold $2(\sigma+a)>1$, followed by the outer threshold $2\sigma>1$.

For uniform constants, $dq\ge3$ gives

$$(dq)^{-2\sigma}
 \le (dq-1)^{-2\sigma}
 \le (3/2)^{2|\sigma|}(dq)^{-2\sigma}$$

after choosing the inequality direction according to the sign and absorbing it into a compact-parameter constant. Thus on every compact subset of the claimed domain,

$$C_1d^{-4\sigma}
 \le\|R_d\|_1^2
 \le C_2d^{-4\sigma}.$$

The $q=1$ lower bound applies for every $d\ge3$; the exceptional row $d=2$ does not affect outer summability.

## Trace-norm holomorphy

Let $K$ be a compact subset of

$$\Re s>\frac12,
 \qquad
 \Re(s+u)>\frac12.$$

There is an $\varepsilon>0$ such that both real parts exceed their boundaries by $2\varepsilon$ throughout $K$. A derivative of order $(j,k)$ in $(s,u)$ multiplies an entry by a polynomial in

$$\log d,\quad\log(dq-1),\quad\log q.$$

For every fixed polynomial degree these logarithms are bounded by a constant times $(dq)^\varepsilon$. Replacing the margin $2\varepsilon$ by $\varepsilon$ reproduces a summable row majorant. The differentiated row series therefore converges locally uniformly in trace norm. This proves Fréchet holomorphy into $\mathcal S_1$, and the standard determinant map is holomorphic on that ideal.

## The Fourier projection on ideals

The diagonal unitary action

$$U_te_n=\mathrm e^{int}e_n$$

acts isometrically on every Schatten ideal by conjugation. Bochner integration therefore gives a contraction

$$\mathcal P_j(T)=\frac1{2\pi}\int_0^{2\pi}
 \mathrm e^{-ijt}U_tTU_t^{-1}\,\,\mathrm dt.$$

It retains the matrix diagonal $d-n=j$. For $j=1$, the graph relation forces $d=n+1$, whose cofactor is one. This proves both the scalar necessity and the pure-cofactor noncompactness. The same averaging preserves the compact ideal because it is an operator-norm closed convex ideal.

## A bounded pure-cofactor regime

Put $a=\Re u>1$. For fixed output $d$, sources are $dq-1$, so the absolute row sum is at most

$$\sum_{q\ge1}q^{-a}=\zeta(a).$$

For fixed input $n$, every allowed edge corresponds to a divisor $q\mid n+1$, and the absolute column sum is at most the same full series. Schur's test gives $\|Q_u\|\le\zeta(a)$. Combined with [\[thm:pure-obstruction\]](#thm:pure-obstruction){reference-type="ref" reference="thm:pure-obstruction"}, this provides an explicit nonempty regime in which the matrix is bounded but noncompact. No claim is made for the entire strip $1/2<a\le1$.

## Character coefficients and local logarithms

In the trace-class domain, $D_\chi(s,z)$ is entire in $z$, but its logarithm need not be globally single-valued across zeros. For $|z|\|L_{s,\chi}\|<1$, the normalized logarithm is uniquely determined by

$$-\log D_\chi(s,z)=
 \sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_{s,\chi}^r.$$

Every fixed-period trace has finite group support by [\[lem:confinement\]](#lem:confinement){reference-type="ref" reference="lem:confinement"}. Haar coefficient extraction may therefore be performed term by term. This local procedure is all that is needed for [\[thm:coefficient\]](#thm:coefficient){reference-type="ref" reference="thm:coefficient"}; no global logarithm branch or primitive-product convergence at $z=1$ is used.

## Radius of the isolated holonomy-two series

Stirling's formula gives

$$\log M_k
 =\log\frac{(2k-1)!}{(k-1)!}
 =k\log k+O(k).$$

Hence for $\sigma=\Re s$,

$$\left|M_k^{-2s}\right|^{1/k}
 =\exp[-2\sigma\log k+O(1)].$$

The root tends to zero for $\sigma>0$, to one for $\sigma=0$, and to infinity for $\sigma<0$. This proves the stated radii. The calculation belongs to one Fourier coefficient and does not enlarge the whole-operator domain [\[eq:S1-domain\]](#eq:S1-domain){reference-type="ref" reference="eq:S1-domain"}.

## Regular lift in the semifinite algebra

The row estimate for $\mathbb R_d$ proves more than formal integrability: the sum of row operator norms is bounded by the same summable row $\ell^2$-norms for $\Re s>1/2$. Thus the lift is a bounded element of $\mathcal N$ as well as an element of $L^1(\mathcal N,\Phi)$ there. Its powers remain in $L^1$, and the local trace series in [\[eq:phi-det\]](#eq:phi-det){reference-type="ref" reference="eq:phi-det"} is meaningful.

Ordinary noncompactness is independent of this estimate. If the chosen vector in [\[thm:lift-noncompact\]](#thm:lift-noncompact){reference-type="ref" reference="thm:lift-noncompact"} is first taken with finite deck support, an escaping sequence of right translates is eventually orthogonal. A general nonzero image is approximated by such a vector. This gives the required weakly null witness without assuming a spectral decomposition of the lift.

## First-return and repetition conventions

The induced return section consists of edges with $q>1$. Each $C_k$ visits it once, so inducing turns a length-$k$ primitive orbit into one fixed branch with a retained time marker $z^k$. Setting $z=1$ forgets that time; it does not make the branches identical as source histories, but it does make the pure cofactor diagonal entries identical. Endpoint regularization retains the full source history through $M_k^{-2s}$.

This is distinct from a temporal repetition. A repetition of an orbit raises its holonomy to a power. Atomic holonomy therefore admits no repetitions by [\[cor:no-atomic-repeat\]](#cor:no-atomic-repeat){reference-type="ref" reference="cor:no-atomic-repeat"}, even though it has infinitely many different primitive representatives indexed by $k$.

# Claim, evidence, and route ledger {#app:scope}

L0.28L0.20Y Statement & Status & Evidence\
cofactor is source intrinsic & proved & edge factorization [\[eq:edge-rule\]](#eq:edge-rule){reference-type="ref" reference="eq:edge-rule"}\
every cycle has $Q\ge2$ & proved & [\[thm:positive-holonomy\]](#thm:positive-holonomy){reference-type="ref" reference="thm:positive-holonomy"}\
neutral skew recurrence is empty & proved & [\[cor:no-neutral\]](#cor:no-neutral){reference-type="ref" reference="cor:no-neutral"}\
cofactor gauge decomposition & proved & [\[thm:gauge\]](#thm:gauge){reference-type="ref" reference="thm:gauge"}\
$Q=2$ classification & proved & [\[thm:q2\]](#thm:q2){reference-type="ref" reference="thm:q2"}\
atomic $Q=p$ classification & proved & [\[thm:atomic\]](#thm:atomic){reference-type="ref" reference="thm:atomic"}\
no atomic repetition & proved & [\[cor:no-atomic-repeat\]](#cor:no-atomic-repeat){reference-type="ref" reference="cor:no-atomic-repeat"}\
finite fixed-period support & proved & [\[lem:confinement\]](#lem:confinement){reference-type="ref" reference="lem:confinement"}\
exact connected coefficient & proved & [\[thm:coefficient\]](#thm:coefficient){reference-type="ref" reference="thm:coefficient"}\
closed $Q=2$ coefficient & proved & [\[thm:h2\]](#thm:h2){reference-type="ref" reference="thm:h2"}\
sharp scalar $\mathcal S_1$ domain & proved & [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"}\
unitary character domain & proved & [\[cor:character-S1\]](#cor:character-S1){reference-type="ref" reference="cor:character-S1"}\
semifinite lift $L^1$ domain & proved & [\[thm:lift-L1\]](#thm:lift-L1){reference-type="ref" reference="thm:lift-L1"}\
ordinary lift noncompact & proved & [\[thm:lift-noncompact\]](#thm:lift-noncompact){reference-type="ref" reference="thm:lift-noncompact"}\
neutral local determinant $1$ & proved & [\[cor:phi-one\]](#cor:phi-one){reference-type="ref" reference="cor:phi-one"}\
pure cofactor noncompactness & proved & [\[thm:pure-obstruction\]](#thm:pure-obstruction){reference-type="ref" reference="thm:pure-obstruction"}\
Fredholm trilemma & proved & [\[thm:trilemma\]](#thm:trilemma){reference-type="ref" reference="thm:trilemma"}\
first-return persistence & proved & [\[prop:return\]](#prop:return){reference-type="ref" reference="prop:return"}\
abelian-holonomy blindness & proved & [\[thm:blindness\]](#thm:blindness){reference-type="ref" reference="thm:blindness"}\
positive-inventory persistence & proved & [\[prop:inventory\]](#prop:inventory){reference-type="ref" reference="prop:inventory"}\
direct literature collision absent & search-bounded & documented primary-source audit\
Riemann Euler identity & rejected & [11](#sec:route){reference-type="ref" reference="sec:route"}\
functional equation / critical line & not claimed & outside candidate\
RH / Hilbert--Pólya mechanism & not claimed & outside candidate\

#### Source firewall.

The graph constructor may use only alphabet successor, tensor factorization, integer multiplication, divisibility, and exact quotient witnesses. It may not call a primality predicate, a prime table, a von Mangoldt table, Riemann zeros, or a target-fitted parameter. Atomicity appears only after the object is frozen, to classify a coefficient already generated by the source.

#### Determinant firewall.

Scalar $D(s,u;z)$ and $D_\chi(s,z)$ are ordinary Fredholm determinants on $\mathcal H$ only in their proved trace-class domains. The regular lift is ordinarily noncompact; $\det_\Phi$ is a separate normalized local semifinite trace-series determinant. The formal pure-cofactor class series is not promoted to a whole-operator determinant.

#### Target firewall.

No target zero is used for construction, tuning, stopping, or evaluation. The Route-A rejection follows from primitive support, multiplicity, period, and roof. An accidental scalar equality or character cancellation would not repair the marked connected ledger.

#### Literature firewall.

Classical references support only general determinant, twist, voltage, cohomology, group-trace, and trace-ideal machinery. Every candidate-specific identity is proved in this manuscript. The novelty statement is bounded by the recorded search and is not a priority theorem.

#### Future-work firewall.

The abelian product-holonomy branch is closed by [\[thm:blindness\]](#thm:blindness){reference-type="ref" reference="thm:blindness"}. An ordered word $1^{k-1}2$ would be a different free-word cocycle because a group homomorphism sends the numerical identity label $1$ to the identity. Any later ordered extension must first pass a finite-state eventual-periodicity theorem and a non-compiler test. No such extension, no cross-family construction, and no Route-B project is part of SD-C24.

#### Reproducibility boundary.

All infinite claims are theorem-level. Finite exact audits may check edge construction, holonomy identities, rotations, group-algebra coefficients, character inversion, and row prefixes, but they do not substitute for the proofs. The manuscript uses no stochastic fit, numerical root search, or unreported hyperparameter.
