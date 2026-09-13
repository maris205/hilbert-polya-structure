---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--25-holomorphic-lefschetz-code-collapse"
canonical_tex: "symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/main.tex"
canonical_pdf: "symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/main.pdf"
source_sha256: "e22f629fe771ae79ee15870312f365c92e2b9430092f7fefc3ac98aa2c4d5d79"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Holomorphic Lefschetz Fibers over Logarithmic Codes: Exact Stability Cancellation, Renewal Flooding, and Atom-Loop Collapse

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A self-delimiting binary history of an integer $n$ can be realized by an affine holomorphic contraction with intrinsic ratio $q_n=2^{-O(\log n)}$. We classify whether analytic function spaces repair the resulting orbit determinant. On zero-forms, the $r$-fold weighted composition trace is $w^r/(1-q^r)$. Matching its first trace by a scalar normalization fails at the second, and no ordinary trace-class tensor fiber can provide moments $1-q^r$: its forced Fredholm determinant $(1-t)/(1-qt)$ would have a pole. The canonical de Rham $0|1$ pullback does provide the missing numerator. Its supertrace equals $w^r$ for every $r$, and the graded ratio of two honest degreewise Fredholm determinants is exactly $1-zw$. This is a genuine all-order holomorphic escape, not an ordinary block determinant. We then compute its global ceiling. On one shared renewal disk the ratio is $1-z\sum_jw_j$, so every mixed primitive return necklace survives. On disjoint disks it is $\prod_j(1-zw_j)$, but the analytic complex retracts to one constant mode per supplied label and is determinant-equivalent to diagonal atom loops. The construction therefore works unchanged for primes, squares, random sets, and arbitrary inventories. At the original digit marker it retains $u^{\ell(n)}$, and prime cohomology modes keep the trace-class boundary at $\Re s>1$. Thus the analytic determinant gate succeeds in a graded sense, while arithmetic selection, continuation, and spectral gates fail; Route A is rejected.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Holomorphic Lefschetz Fibers over Logarithmic Codes:\
  Exact Stability Cancellation, Renewal Flooding, and Atom-Loop Collapse
```

## Markdown 正文

# Introduction {#sec:introduction}

A holomorphic inverse branch remembers more than its symbolic label. If $\phi(z)=a+qz$ is a strict affine contraction and $W_0=w(f\mapsto f\circ\phi)$, then its repeated nuclear trace is $$\operatorname{Tr}W_0^r=\frac{w^r}{1-q^r}.$$ The factor $(1-q^r)^{-1}$ is the local stability denominator in the holomorphic fixed-point formula. It prevents the ordinary composition determinant from being the one-loop factor $1-zw$. This is the precise analytic obstacle left open by the preceding finite-code and Kraft--Fredholm analysis: perhaps a better function space or an internal fiber can supply the missing numerator without reducing the branch to a formal atom.

The first answer of this paper is positive. Holomorphic zero- and one-forms carry the canonical pullbacks $$U_{\phi,0}f=f\circ\phi,
 \qquad
 U_{\phi,1}(g\,dz)=q(g\circ\phi)\,dz.$$ Their alternating trace cancels the denominator exactly: $$\operatorname{Tr}(wU_{\phi,0})^r-\operatorname{Tr}(wU_{\phi,1})^r=w^r
 \qquad(r\ge1).$$ Consequently $$\frac{\det(I-zwU_{\phi,0})}
      {\det(I-zwU_{\phi,1})}=1-zw.$$ Both determinants are ordinary trace-class Fredholm determinants on frozen Bergman spaces. Their quotient is a graded or relative determinant. This distinction matters: the ordinary determinant of the ungraded direct sum is the product of the two degreewise determinants, not their ratio.

The second answer is the ceiling. The exterior numerator removes tangent stability for every legal closed word; it does not ask which return labels occur in that word. Put many completed code returns on one shared disk and the full supertrace becomes $$\operatorname{Str}L^r=\left(\sum_jw_j\right)^r.$$ The graded determinant is $1-z\sum_jw_j$, the determinant of a full renewal alphabet, and all mixed primitive necklaces survive. Put the same branches on disjoint disks and the graded determinant becomes $\prod_j(1-zw_j)$. That product is exact, but cohomology identifies it with one diagonal atom loop per supplied label. The logarithmic code, affine translation, and contracting modes lie in an acyclic sector that cancels from the answer.

This shared/disjoint fork is the central source-integrity test. If $w_n=n^{-s}$ and the disjoint inventory is the rational primes, the ratio is $1/\zeta(s)$ in $\Re s>1$. The same construction, unchanged, returns the corresponding Euler product for squares, Fibonacci numbers, a seeded random inventory, a hash inventory, or any supplied decidable set. The analytic mechanism factors an inventory; it does not select the primes.

The distinction between symbolic clocks is equally strict. We freeze an Elias gamma history $c(n)$ of length $\ell(n)=O(\log n)$ and realize its digits by two affine disk maps. A variable $u$ that marks the original binary digit edges assigns $u^{\ell(n)}n^{-s}$ to a completed word. A variable $z$ assigning one mark per completed code return arises only after induction, or after declaring every whole codeword to be one symbol of a countable return alphabet. Exterior cancellation changes neither marker.

The construction belongs to the classical line of holomorphic transfer operators and dynamical zeta functions [@Ruelle1976; @Ruelle1990]. Explicit Bergman-space trace estimates come from @BandtlowJenkinson2008; the alternating numerator belongs to Lefschetz and exterior-form cancellation [@AtiyahBott1967; @HadfieldKandelSchiavina2020]. We do not claim a new general determinant theory. The contribution is an exact model-specific classification of what this machinery buys inside a logarithmic arithmetic code, including two rigidity results that force the canonical grading and a global cohomological collapse that closes the arithmetic route.

Our contributions are:

1.  We freeze a prefix-free logarithmic integer code and an explicit compactly contained affine disk realization with $q_n=2^{-\ell(n)}$, giving honest shared and disjoint trace-class operators for $\Re s>1$.

2.  We prove that scalar normalization fails at the second repetition unless $q=0$, and that no ordinary finite-dimensional or trace-class tensor fiber can have the required moments $1-q^r$.

3.  We prove the positive all-order de Rham escape by three compatible certificates: nuclear traces, exact finite polynomial complexes, and spectral telescoping.

4.  We compute the complete shared and disjoint graded determinants, identify mixed primitive necklaces in the former, and prove determinant-equivalence to atom loops in the latter.

5.  We retain the digit/return marker firewall and prove that the surviving prime cohomology modes prevent a trace-class continuation of the same family through $\Re s=1$.

displays both the advance and the obstruction. fixes the novelty boundary; defines the code, spaces, and assemblies; proves scalar and ordinary-fiber rigidity; constructs the canonical graded escape; prove the global dichotomy; and close the marker, analytic, and route ledgers.

# Literature boundary and bounded novelty {#sec:literature}

## Holomorphic traces and symbolic determinants

The periodic-point interpretation of holomorphic transfer determinants is classical. In the expanding-map setting, @Ruelle1976 related holomorphic transfer operators, fixed points, and dynamical zeta functions. @Ruelle1990 later developed a broader Fredholm-determinant framework for contracting and Hölder-type systems. The primitive-orbit and trace-log conventions used here follow the standard symbolic ledger described, for example, by @ParryPollicott1990.

The analytic input closest to our frozen system is the map-weight framework of @BandtlowJenkinson2008. Under common compact containment and absolute summability of the weights, their Bergman-space operators have strong eigenvalue decay and nuclear trace formulas. Periodic words carry the fixed-point denominator $\det(I-D\phi_\alpha)^{-1}$. In one complex dimension and for an affine word with derivative $q_\alpha$, this is exactly $(1-q_\alpha)^{-1}$. We specialize this established result rather than claiming a new nuclearity theorem.

## The exterior numerator

Alternating traces on complexes and their fixed-point numerators go back to Lefschetz theory; @AtiyahBott1967 is the conceptual source relevant to elliptic complexes. In one dimension the algebra required here is the elementary exterior identity $$\operatorname{tr}\Lambda^0 A-
 \operatorname{tr}\Lambda^1 A=\det(I-A).$$ Modern Ruelle factorizations make this cancellation explicit across form degrees; see, for example, the exterior-power trace formulas discussed by @HadfieldKandelSchiavina2020. Therefore the statement that a zero-/one-form pair cancels a local stability denominator has low novelty.

Our question is narrower and source-sensitive. What does this classical cancellation do when the inverse branches are the analytic image of a self-delimiting arithmetic code? Does it preserve the intended primitive ledger on a shared recurrent object, or does it merely expose a supplied component inventory? The shared/disjoint cohomology theorem answers that question exactly.

## Coding and determinant ownership

Universal self-delimiting representations of the integers originate with @Elias1975. We use the gamma code because it gives a transparent prefix-free length $2\lfloor\log_2n\rfloor+1$. Neither the code nor its length bound is claimed as novel.

For ordinary trace-class operators, the Fredholm determinant is entire in its scalar parameter and is locally controlled by power traces [@Simon1977]. That elementary ownership fact drives our ordinary tensor-fiber obstruction. It also distinguishes three expressions that must not be conflated: $$\det(I-zL_0),\qquad
 \det(I-zL_1),\qquad
 \frac{\det(I-zL_0)}{\det(I-zL_1)}.$$ The first two are ordinary determinants. The third is a graded ratio.

A non-peer-reviewed 2026 preprint by @Randolph2026 considers the local operator $p^{-s}f(z/p)$ and records its spectral product $\prod_{m\ge0}(1-p^{-s-m})$, which is not the symbolic one-loop factor $1-p^{-s}$. We cite that overlap only as an ownership firewall. No theorem here relies on the preprint, and its broader RH language is not adopted.

L3.4cmL3.6cmY Component & Closest source & Claim boundary\
holomorphic nuclearity and fixed-point trace & Ruelle; Bandtlow--Jenkinson & established technology, specialized to explicit logarithmic-code branches\
exterior cancellation of stability & Atiyah--Bott; form-degree Ruelle factorizations & established mechanism, not a new determinant theory\
scalar all-power rigidity & implicit in the trace formula & explicit two-power theorem and rank-one boundary\
ordinary tensor-fiber obstruction & trace-class determinant theory & entire-versus-pole proof for the required moment sequence\
shared/disjoint collapse & symbolic full shifts and direct-sum cohomology & model-specific source-integrity theorem and arbitrary-inventory control\
prime/RH mechanism & none & explicitly absent\

The literature search through 2026-08-14 found no primary source combining the four pieces of our diagnostic: logarithmic self-delimiting histories, scalar all-repetition rigidity, canonical de Rham repair, and the shared-versus-disjoint arithmetic collapse. This is a bounded search statement, not proof of global novelty. The strongest contribution is the classification in the last three rows of ; the analytic ingredients themselves remain classical.

# Frozen code and analytic source {#sec:source}

## Arithmetic skeleton and prefix-free histories

The source-side integer relation remains the full-shift semiring skeleton $$F_m\mathbin{\boxtimes}F_n\cong F_{mn},\qquad
 F_m\mathbin{\boxplus}F_n\cong F_{m+n},\qquad
 S(F_n)\cong F_{n+1},\qquad h(F_n)=\log n.$$ Rational primes are the multiplicative atoms of this skeleton. The analytic construction below is frozen over all integers before an inventory $S\subseteq\{2,3,\ldots\}$ is chosen. Selecting $S=\mathbb P$ is therefore an evaluation restriction, not an intrinsic output of the code.

For $n\ge1$, put $$L(n)=\lfloor\log_2n\rfloor+1.$$ The Elias gamma word $c(n)$ consists of $L(n)-1$ zeros followed by the $L(n)$-digit binary expansion of $n$. It is prefix-free and has length $$\ell(n)=2L(n)-1=2\lfloor\log_2n\rfloor+1.
 \label{eq:gamma-length}$$ For example, $$c(2)=010,\qquad c(3)=011,\qquad c(4)=00100.$$ The choice supplies a fixed $O(\log n)$ history. It supplies no prime-selection predicate.

## Affine digit maps

On the unit disk $\mathbb D$, freeze $$\psi_0(z)=\frac z2-\frac14,
 \qquad
 \psi_1(z)=\frac z2+\frac14.
 \label{eq:digit-maps}$$ Both maps send the closed disk into $|z|\le3/4$. For a binary word $c=c_1\cdots c_\ell$, let $\phi_c$ denote the corresponding ordered composition, and define $$\phi_n=\phi_{c(n)}.$$ It is affine: $$\phi_n(z)=a_n+q_nz,
        \qquad q_n=2^{-\ell(n)}.
 \label{eq:code-branch}$$ The translation $a_n$ distinguishes ordered histories; the derivative records their lengths. Composition orientation affects the explicit translation but not any derivative product or theorem below. Every $\phi_n(\mathbb D)$ lies in a common compact subset of $\mathbb D$.

## Zero- and one-form pullbacks

Let $$\mathcal H^0=A^2(\mathbb D),\qquad \mathcal H^1=A^2(\mathbb D)\,dz$$ with their usual Bergman norms. For $\phi(z)=a+qz$, define $$U_{\phi,0}f=f\circ\phi,
 \qquad
 U_{\phi,1}(g\,dz)=q(g\circ\phi)\,dz.
 \label{eq:form-pullbacks}$$ The densely defined holomorphic differential intertwines them: $$dU_{\phi,0}=U_{\phi,1}d.$$ For exact finite algebra we use $$0\longrightarrow\mathbb C\longrightarrow P_N
 \xrightarrow{d}P_{N-1}dz\longrightarrow0,
 \label{eq:polynomial-complex}$$ where $P_N$ contains polynomials of degree at most $N$. Affine pullback preserves this complex. We do not infer that $d$ is bounded between the two infinite Bergman spaces; infinite identities will be proved by nuclear fixed-word traces.

## Shared and disjoint assemblies

Let $w_n(s)=n^{-s}$. The *shared renewal* pair is $$\mathcal L^k_{S,s}=\sum_{n\in S}w_n(s)U_{\phi_n,k},
 \qquad k=0,1.
 \label{eq:shared-pair}$$ All returns act on one disk. Once a code return is completed, every next return label is legal; the induced symbolic object is a countable full shift.

The *disjoint* pair is $$\mathcal E^k_{S,s}=\bigoplus_{n\in S}w_n(s)U_{\phi_n,k}.
 \label{eq:disjoint-pair}$$ Every label acts on a private disk. This removes mixed cycles by separating recurrent components, so the component index visibly contains the supplied inventory.

[\[prop:trace-class\]]{#prop:trace-class label="prop:trace-class"} For every inventory $S\subseteq\{2,3,\ldots\}$ and $\Re s>1$, all four operators in [\[eq:shared-pair,eq:disjoint-pair\]](#eq:shared-pair,eq:disjoint-pair){reference-type="ref" reference="eq:shared-pair,eq:disjoint-pair"} are trace class.

Common compact containment gives a uniform trace-norm estimate for the zero-form composition operators in the holomorphic map-weight framework of @BandtlowJenkinson2008. Multiplication by $q_n$, with $|q_n|\le1$, gives the same type of estimate in degree one. Since $$\sum_{n\in S}|n^{-s}|\le\sum_{n\ge2}n^{-\Re s}<\infty,$$ the shared sums converge in trace norm, and the trace norm of each disjoint sum is bounded by the same componentwise series.

## Determinant convention

For any trace-class pair $L=(L_0,L_1)$, put $$D_{\mathrm{gr}}(z;L)=\frac{\det(I-zL_0)}{\det(I-zL_1)}.
 \label{eq:graded-det}$$ Near $z=0$, $$D_{\mathrm{gr}}(z;L)
 =\exp\left[-\sum_{r\ge1}\frac{z^r}{r}
 \left(\operatorname{Tr}L_0^r-\operatorname{Tr}L_1^r\right)\right].
 \label{eq:graded-log}$$ This quotient is a graded or relative determinant. The ordinary ungraded block determinant is $$\det(I-z(L_0\oplus L_1))
 =\det(I-zL_0)\det(I-zL_1).
 \label{eq:block-product}$$ Equations [\[eq:graded-det\]](#eq:graded-det){reference-type="eqref" reference="eq:graded-det"} and [\[eq:block-product\]](#eq:block-product){reference-type="eqref" reference="eq:block-product"} have different ownership and will never be interchanged.

# Scalar and ordinary-fiber rigidity {#sec:rigidity}

We first test repairs that stay within an ordinary, ungraded trace. The result is rigid already for one affine branch.

[\[lem:fixed-trace\]]{#lem:fixed-trace label="lem:fixed-trace"} Let $\phi(z)=a+qz$ map $\mathbb D$ compactly into itself, with $0<|q|<1$, and let $W_0=wU_{\phi,0}$. Then $$\operatorname{Tr}W_0^r=\frac{w^r}{1-q^r},\qquad r\ge1.
 \label{eq:zero-trace}$$ Its ordinary Fredholm determinant is $$\det(I-zW_0)=\prod_{m\ge0}(1-zwq^m).
 \label{eq:q-pochhammer}$$

The iterate $\phi^r$ has derivative $q^r$ and one fixed point. The holomorphic fixed-point trace formula gives [\[eq:zero-trace\]](#eq:zero-trace){reference-type="eqref" reference="eq:zero-trace"}. One may also center the coordinate at that fixed point. The monomials then have eigenvalues $1,q,q^2,\ldots$, and the trace is $$w^r\sum_{m\ge0}q^{rm}=\frac{w^r}{1-q^r}.$$ The trace-log formula yields [\[eq:q-pochhammer\]](#eq:q-pochhammer){reference-type="eqref" reference="eq:q-pochhammer"}; equivalently, it is the product over the centered spectrum.

The translation $a$ affects the upper-triangular part of a monomial matrix but not its diagonal. Thus the local obstruction is intrinsic to the code length through $q_n=2^{-\ell(n)}$.

[\[prop:scalar-rigidity\]]{#prop:scalar-rigidity label="prop:scalar-rigidity"} Suppose a scalar $\alpha(q)$ satisfies $$\operatorname{Tr}\bigl(\alpha(q)wU_{\phi,0}\bigr)^r=w^r$$ for every $r\ge1$ and nonzero $w$. Then $q=0$ or $q=1$. For a strict contraction, the only possibility is $q=0$.

At $r=1$, [\[lem:fixed-trace\]](#lem:fixed-trace){reference-type="ref" reference="lem:fixed-trace"} forces $\alpha=1-q$. At $r=2$, the same requirement becomes $$\frac{(1-q)^2}{1-q^2}=1.$$ Hence $2q(q-1)=0$. The solution $q=1$ is not a strict contraction.

The first-trace normalization therefore has the exact second-order residual $$\frac{(1-q)^2}{1-q^2}-1=-\frac{2q}{1+q}.
 \label{eq:scalar-residual}$$ At $q=0$, composition evaluates a function at the fixed point and includes the resulting constant. The operator has rank one: the purported analytic repair has become an atom loop.

A larger ordinary fiber might try to manufacture the missing moment $1-q^r$. Trace-class determinant theory rules out that attempt for every ordinary tensor fiber at once.

[\[thm:tensor-rigidity\]]{#thm:tensor-rigidity label="thm:tensor-rigidity"} Let $B$ be a finite-dimensional matrix or a trace-class operator, and let $$T=w(B\otimes U_{\phi,0}).$$ For $0<|q|<1$, it is impossible that $\operatorname{Tr}T^r=w^r$ for every $r\ge1$.

The tensor trace formula and [\[lem:fixed-trace\]](#lem:fixed-trace){reference-type="ref" reference="lem:fixed-trace"} would require $$\operatorname{Tr}B^r=1-q^r
        \qquad(r\ge1).$$ For sufficiently small $t$, the Fredholm trace logarithm then gives $$\begin{aligned}
 \det(I-tB)
 &=\exp\left(-\sum_{r\ge1}\frac{1-q^r}{r}t^r\right)\\
 &=\frac{1-t}{1-qt}.\end{aligned}$$ The determinant of a trace-class operator is entire in $t$ [@Simon1977], whereas the last expression has a genuine pole at $t=q^{-1}$. Since $q\ne1$, the numerator does not cancel it. This is a contradiction.

For a finite matrix the forced power sums formally ask for eigenvalue multiplicity (+1) at (1) and multiplicity (-1) at (q). Negative multiplicity identifies the missing structure: an odd sector. The theorem does not exclude every possible nontensor nuclear operator; it isolates the ordinary tensor loophole and motivates the canonical grading rather than an arbitrary signed fit.

Matching only $\operatorname{Tr}T$ cannot distinguish a valid determinant from a first-order normalization. The scalar residual [\[eq:scalar-residual\]](#eq:scalar-residual){reference-type="eqref" reference="eq:scalar-residual"} and the entire-versus-pole theorem are full cyclic tests. They prevent a first trace-log coefficient from being promoted to an Euler factor.

# The canonical de Rham escape {#sec:escape}

The odd sector suggested by [\[thm:tensor-rigidity\]](#thm:tensor-rigidity){reference-type="ref" reference="thm:tensor-rigidity"} is already present in the source geometry. Pullback on one-forms contributes exactly one derivative factor at every step.

[\[thm:local-cancellation\]]{#thm:local-cancellation label="thm:local-cancellation"} For an affine branch $\phi(z)=a+qz$, set $$W_0=wU_{\phi,0},\qquad W_1=wU_{\phi,1}.$$ Then for every $r\ge1$, $$\operatorname{Tr}W_0^r-\operatorname{Tr}W_1^r=w^r.
 \label{eq:local-supertrace}$$ The degreewise Fredholm determinants obey $$\det(I-zW_0)=(1-zw)\det(I-zW_1).
 \label{eq:local-det-identity}$$ Consequently the graded ratio equals $1-zw$ wherever it is defined.

Since $U_{\phi,1}=qU_{\phi,0}$, the one-form repetition trace is $$\operatorname{Tr}W_1^r=\frac{w^rq^r}{1-q^r}.$$ Subtracting it from [\[eq:zero-trace\]](#eq:zero-trace){reference-type="eqref" reference="eq:zero-trace"} proves [\[eq:local-supertrace\]](#eq:local-supertrace){reference-type="eqref" reference="eq:local-supertrace"}. Substitute the full power identity into the two trace logarithms. The resulting equality holds near $z=0$, and both sides of [\[eq:local-det-identity\]](#eq:local-det-identity){reference-type="eqref" reference="eq:local-det-identity"} are entire, so the identity theorem extends it to every $z$.

The numerator is the one-dimensional exterior character $$\operatorname{tr}\Lambda^0(q^r)-
 \operatorname{tr}\Lambda^1(q^r)=1-q^r.
 \label{eq:exterior-character}$$ It depends on the repeated derivative $q^r$, unlike a hand-assigned odd scalar whose sign or value would be raised incorrectly under repetition.

## Exact polynomial certificate

Write $\phi(z)=a+qz$. On the monomial bases of $P_N$ and $P_{N-1}dz$, the pullback matrices are $$\begin{aligned}
 (M_0)_{j,k}
 &=\binom{k}{j}a^{k-j}q^j,
 &&0\le j\le k\le N,
 \label{eq:M0}\\
 (M_1)_{j,k}
 &=q\binom{k}{j}a^{k-j}q^j,
 &&0\le j\le k\le N-1.
 \label{eq:M1}\end{aligned}$$ If $D_{k-1,k}=k$ is the differentiation matrix, direct binomial algebra gives $$DM_0=M_1D.$$ The sequence [\[eq:polynomial-complex\]](#eq:polynomial-complex){reference-type="eqref" reference="eq:polynomial-complex"} is exact. Constants carry the scalar $w$, while differentiation identifies the nonconstant zero-form quotient with the one-form space. Hence $$\det(I-zwM_0)=(1-zw)\det(I-zwM_1)
 \label{eq:finite-characteristic}$$ as a polynomial identity for every $N$. This is a full characteristic- polynomial certificate, not a finite list of trace checks.

## Spectral telescoping

Centering the fixed point makes the two ordinary spectra transparent: $$\operatorname{spec}(W_0)=\{wq^m:m\ge0\},\qquad
 \operatorname{spec}(W_1)=\{wq^{m+1}:m\ge0\}.$$ Therefore $$\frac{\det(I-zW_0)}{\det(I-zW_1)}
 =\frac{\prod_{m\ge0}(1-zwq^m)}
        {\prod_{m\ge0}(1-zwq^{m+1})}
 =1-zw.
 \label{eq:spectral-telescope}$$ All positive-degree modes pair. The constant zero-form is the sole cohomological survivor.

[\[prop:ordinary-graded\]]{#prop:ordinary-graded label="prop:ordinary-graded"} The identity [\[eq:local-det-identity\]](#eq:local-det-identity){reference-type="eqref" reference="eq:local-det-identity"} concerns the graded quotient. The ordinary determinant on $\mathcal H^0\oplus\mathcal H^1$ is $$\det(I-z(W_0\oplus W_1))
 =\det(I-zW_0)\det(I-zW_1),$$ and is not $1-zw$ for $0<|q|<1$ and $w\ne0$.

Fredholm determinants multiply under direct sums. The product retains both degree spectra, while [\[eq:spectral-telescope\]](#eq:spectral-telescope){reference-type="eqref" reference="eq:spectral-telescope"} cancels their paired factors by division.

L3.2cmL5.2cmY Object & Formula & Meaning\
zero-form ordinary determinant & $\prod_{m\ge0}(1-zwq^m)$ & honest composition spectrum; stability tower retained\
one-form ordinary determinant & $\prod_{m\ge0}(1-zwq^{m+1})$ & honest derivative-twisted spectrum\
ordinary block determinant & product of the two rows above & no cancellation between parity sectors\
graded/relative determinant & quotient of the first two rows, $1-zw$ & exact Lefschetz cancellation; not an ordinary block determinant\

The escape is therefore genuine but typed. Each parity sector has a valid trace-class operator; their ratio supplies the desired local factor. The next question is not local analytic legitimacy but what survives when many code returns share one recurrent object.

# Shared renewal: stability cancels, mixed words remain {#sec:shared}

Let $J$ be finite, or countable with $\sum_{j\in J}|w_j|<\infty$, and let $\phi_j(z)=a_j+q_jz$ satisfy the common compact-containment condition. On one shared disk define $$L_k=\sum_{j\in J}w_jU_{\phi_j,k},
        \qquad S_w=\sum_{j\in J}w_j.$$

[\[thm:shared-collapse\]]{#thm:shared-collapse label="thm:shared-collapse"} For every $r\ge1$, $$\operatorname{Tr}L_0^r-\operatorname{Tr}L_1^r=S_w^r.
 \label{eq:shared-supertrace}$$ The degreewise determinants satisfy $$\det(I-zL_0)=(1-zS_w)\det(I-zL_1).
 \label{eq:shared-det}$$ Hence the shared graded determinant is $1-zS_w$.

Expand $L_k^r$ over ordered words $\alpha=(j_1,\ldots,j_r)\in J^r$. The corresponding composition is affine with derivative $$q_\alpha=\prod_{m=1}^rq_{j_m},$$ and its scalar weight is $w_\alpha=\prod_{m=1}^rw_{j_m}$. The fixed-word trace formula gives $$\operatorname{Tr}U_{\alpha,0}=\frac1{1-q_\alpha},\qquad
 \operatorname{Tr}U_{\alpha,1}=\frac{q_\alpha}{1-q_\alpha}.$$ Their weighted difference is $w_\alpha$. Absolute weight summability justifies the word sum, so $$\operatorname{Tr}L_0^r-\operatorname{Tr}L_1^r
 =\sum_{\alpha\in J^r}w_\alpha
 =\left(\sum_{j\in J}w_j\right)^r.$$ Substitution in the trace logarithm proves [\[eq:shared-det\]](#eq:shared-det){reference-type="eqref" reference="eq:shared-det"} near the origin. Both degreewise determinants are entire, and the identity theorem completes the proof.

On the exact polynomial complex, every weighted sum still obeys $dL_0=L_1d$. Constants carry multiplication by $S_w$, and the nonconstant quotient is intertwined with the one-form action. Thus the finite characteristic-polynomial identity is $$\det(I-zL_0|P_N)
 =(1-zS_w)\det(I-zL_1|P_{N-1}dz).$$ This is the cohomological meaning of [\[thm:shared-collapse\]](#thm:shared-collapse){reference-type="ref" reference="thm:shared-collapse"}: the whole shared disk retracts to one constant state. The infinite proof, however, is the fixed-word trace proof above and does not assume a bounded Bergman differential.

## Primitive necklace ledger

The one-state return alphabet with weights $w_j$ has the standard primitive-necklace factorization $$1-z\sum_jw_j
 =\prod_{[\alpha]\ \mathrm{primitive}}
   \left(1-z^{|\alpha|}w_\alpha\right)
 \label{eq:necklace-product}$$ as a formal identity, or analytically near the origin. The product ranges over cyclic rotations of primitive return words. Thus the linear-looking left side does not mean that only one-letter primitive objects exist; its trace logarithm contains every primitive necklace on the shared alphabet.

[\[cor:mixed-survive\]]{#cor:mixed-survive label="cor:mixed-survive"} For two return weights $x,y$, the shared and disjoint connected logarithms differ by $$\begin{aligned}
 &-\log(1-z(x+y))
 +\log((1-zx)(1-zy))\\
 &\hspace{16mm}=z^2xy+z^3(x^2y+xy^2)+O(z^4).
\end{aligned}
 \label{eq:mixed-expansion}$$ In particular, the primitive mixed necklace $[xy]$ survives at length two, and $[xxy]$, $[xyy]$ survive at length three.

At the power-trace level, $$\operatorname{Str}L^2=x^2+2xy+y^2,$$ while a disjoint two-loop ledger has $x^2+y^2$. Expanding the two logarithms gives [\[eq:mixed-expansion\]](#eq:mixed-expansion){reference-type="eqref" reference="eq:mixed-expansion"}. The indicated monomials have the stated primitive cyclic representatives.

The mechanism is now exact. For each word $\alpha$, exterior grading cancels $(1-q_\alpha)^{-1}$ and leaves $w_\alpha$. It cannot then cancel a word merely because the labels in $\alpha$ differ. In a constrained branch graph, the identical proof leaves all legal graph cycles on degree-zero cohomology. A tangent exterior complex repairs local stability; it is not a branch-combinatorial selector.

For the arithmetic weights $w_n=n^{-s}$, [\[thm:shared-collapse\]](#thm:shared-collapse){reference-type="ref" reference="thm:shared-collapse"} becomes $$D_{\mathrm{gr}}(z;\mathcal L_{S,s})=1-z\sum_{n\in S}n^{-s}.
 \label{eq:shared-dirichlet}$$ Even when $S=\mathbb P$, this is the determinant of a shared return full shift, not the disconnected Euler product over prime loops.

# Disjoint components and atom-loop collapse {#sec:disjoint}

Mixed necklaces disappear if every label is placed on a private recurrent disk. That modification produces the desired product, but it also exposes where the arithmetic inventory resides.

[\[thm:disjoint-factor\]]{#thm:disjoint-factor label="thm:disjoint-factor"} Let $S\subseteq\{2,3,\ldots\}$. For $\Re s>1$, the disjoint pair $$\mathcal E^k_{S,s}=\bigoplus_{n\in S}n^{-s}U_{\phi_n,k}$$ satisfies $$\det(I-z\mathcal E^0_{S,s})
 =\left[\prod_{n\in S}(1-zn^{-s})\right]
   \det(I-z\mathcal E^1_{S,s}).
 \label{eq:disjoint-det}$$ Thus $$D_{\mathrm{gr}}(z;\mathcal E_{S,s})
        =\prod_{n\in S}(1-zn^{-s}).
 \label{eq:disjoint-product}$$

makes both degreewise direct sums trace class. Apply [\[thm:local-cancellation\]](#thm:local-cancellation){reference-type="ref" reference="thm:local-cancellation"} on each component and multiply. Absolute convergence of $\sum_{n\in S}|n^{-s}|$ gives convergence of the product and permits the componentwise Fredholm factorization.

[\[thm:atom-collapse\]]{#thm:atom-collapse label="thm:atom-collapse"} The graded determinant in [\[eq:disjoint-product\]](#eq:disjoint-product){reference-type="eqref" reference="eq:disjoint-product"} is the ordinary Fredholm determinant of the diagonal trace-class operator $$C_{S,s}=\operatorname{diag}(n^{-s})_{n\in S}
        \quad\text{on }\ell^2(S).
 \label{eq:cohomology-diagonal}$$ Equivalently, every disk contributes one constant cohomology state, and all nonconstant analytic modes cancel.

The finite complex [\[eq:polynomial-complex\]](#eq:polynomial-complex){reference-type="eqref" reference="eq:polynomial-complex"} has one-dimensional cohomology represented by constants. On the component labelled $n$, the weighted pullback acts on that class by $n^{-s}$. Direct-sum cohomology is therefore $\bigoplus_{n\in S}\mathbb C$, and its induced map is [\[eq:cohomology-diagonal\]](#eq:cohomology-diagonal){reference-type="eqref" reference="eq:cohomology-diagonal"}. Its ordinary determinant is precisely [\[eq:disjoint-product\]](#eq:disjoint-product){reference-type="eqref" reference="eq:disjoint-product"}. The same conclusion also follows directly from the telescoping component spectra.

The theorem is stronger than saying that the output resembles an Euler product. It identifies a determinant-equivalent minimal model: one one-dimensional loop per supplied label. The affine translations $a_n$, contractions $q_n$, and logarithmic digit histories occur only in paired acyclic modes.

## Arbitrary-inventory control

The disjoint construction is functorial in $S$. Without changing a digit map, function space, form degree, or local determinant rule, it returns a product for every inventory.

L3.2cmL5.1cmY Inventory $S$ & Surviving graded factor & Source-selectivity verdict\
rational primes & $\prod_p(1-zp^{-s})$ & desired unmarked factor only after the prime component list is supplied\
squares & $\prod_{m\ge2}(1-zm^{-2s})$ & identical analytic mechanism\
Fibonacci values & $\prod_{n\in S_{\rm Fib}}(1-zn^{-s})$ & identical analytic mechanism\
all integers & $\prod_{n\ge2}(1-zn^{-s})$ & identical analytic mechanism\
seeded random or hash set & $\prod_{n\in S_{\rm ctrl}}(1-zn^{-s})$ & matched nonarithmetic control succeeds\
arbitrary decidable inventory & $\prod_{n\in S}(1-zn^{-s})$ & construction factors whatever it is given\

For $S=\mathbb P$ and $z=1$, the product equals $1/\zeta(s)$ in the Euler half-plane. This equality earns analytic determinant credit but no prime-selection credit. The prime set appears as the recurrent component index, and [\[thm:atom-collapse\]](#thm:atom-collapse){reference-type="ref" reference="thm:atom-collapse"} deletes every other trace of the code. In the project's control language, the disjoint architecture [Proves Too Much]{.smallcaps}.

Shared and disjoint assemblies are therefore not two representations of one dynamical object. Shared recurrence is connected and contains mixed necklaces. Disjoint recurrence removes them by changing the recurrent component structure. The next section adds the independent clock distinction.

# Marker ownership and the analytic ceiling {#sec:ceiling}

Two independent modeling choices determine the final determinant: whether returns share recurrence, and whether the marker counts digits or completed returns.

## Digit time versus return time

[\[conv:markers\]]{#conv:markers label="conv:markers"} The variable $u$ marks one edge of the original binary code history. The variable $z$ marks one completed code return after induction, or one symbol in a countable alphabet whose symbols are whole codewords.

At digit time, the weight of label $n$ is $$\widetilde w_n(s,u)=u^{\ell(n)}n^{-s}.
 \label{eq:digit-weight}$$ Every theorem in [\[sec:escape,sec:shared,sec:disjoint\]](#sec:escape,sec:shared,sec:disjoint){reference-type="ref" reference="sec:escape,sec:shared,sec:disjoint"} remains valid after substituting $w_n=\widetilde w_n$. Hence $$\begin{aligned}
 D_{\mathrm{gr}}^{\rm shared}(s,u)
 &=1-\sum_{n\in S}u^{\ell(n)}n^{-s},
 \label{eq:digit-shared}\\
 D_{\mathrm{gr}}^{\rm disjoint}(s,u)
 &=\prod_{n\in S}\left(1-u^{\ell(n)}n^{-s}\right).
 \label{eq:digit-disjoint}\end{aligned}$$

At completed-return time, the corresponding expressions are $$\begin{aligned}
 D_{\mathrm{gr}}^{\rm shared}(s,z)
 &=1-z\sum_{n\in S}n^{-s},
 \label{eq:return-shared}\\
 D_{\mathrm{gr}}^{\rm disjoint}(s,z)
 &=\prod_{n\in S}(1-zn^{-s}).
 \label{eq:return-disjoint}\end{aligned}$$ Passing from [\[eq:digit-shared\]](#eq:digit-shared){reference-type="eqref" reference="eq:digit-shared"}--[\[eq:digit-disjoint\]](#eq:digit-disjoint){reference-type="eqref" reference="eq:digit-disjoint"} to [\[eq:return-shared\]](#eq:return-shared){reference-type="eqref" reference="eq:return-shared"}--[\[eq:return-disjoint\]](#eq:return-disjoint){reference-type="eqref" reference="eq:return-disjoint"} is not an algebraic cancellation of $\ell(n)$. It is a change of clock. Setting $u=1$ hides the marked mismatch but does not identify the two symbolic systems.

is deliberately a square of object-changing arrows, not a commutative diagram of equalities. Exterior grading acts vertically inside each analytic branch; it cancels tangent stability but cannot erase symbolic code duration or separate mixed return content.

## The surviving trace-class boundary

The common compact-containment estimate gives degreewise trace class in $\Re s>1$. Could cancellation extend the same operator pair farther? For the prime-indexed disjoint assembly, cohomology answers exactly.

[\[cor:no-halfplane-gain\]]{#cor:no-halfplane-gain label="cor:no-halfplane-gain"} Let $S=\mathbb P$. Any trace-class realization of the frozen disjoint pair that retains its constant cohomology modes must satisfy $\Re s>1$. Removing those modes makes the graded determinant identically one.

By [\[thm:atom-collapse\]](#thm:atom-collapse){reference-type="ref" reference="thm:atom-collapse"}, the cohomology operator has eigenvalues $p^{-s}$. Eigenvalues of a trace-class operator are absolutely summable, so trace class requires $$\sum_p|p^{-s}|=\sum_pp^{-\Re s}<\infty.$$ The prime harmonic series diverges, and for $\Re s\le1$ its terms dominate or equal $p^{-1}$ once $\Re s>0$; for $\Re s\le0$ they do not even tend to zero. Thus the necessary and sufficient absolute-summability domain is $\Re s>1$. Deleting the constants deletes the only unpaired spectral factors, so the quotient is one.

A bounded equivalent renorming cannot change these eigenvalues. More general anisotropic constructions are not universally excluded, but they must either retain the same cohomological spectrum and its boundary or explain which source-derived object replaces it.

The scalar function $1/\zeta(s)$ has a meromorphic continuation beyond its Euler half-plane. That fact does not continue the two degreewise trace-class families $\mathcal E^0_{\mathbb P,s}$ and $\mathcal E^1_{\mathbb P,s}$. SD-C27 constructs no same-object meromorphic Fredholm family, Gamma factor, functional equation, completed divisor, or critical-line mechanism.

# Exact audit protocol and falsifiers {#sec:audit}

The infinite conclusions are theorems, not extrapolations from truncations. Exact finite algebra remains useful because it catches orientation, truncation, determinant-ownership, and marker errors. The following audit is frozen independently of an inventory cutoff.

## Code and branch checks

For every registered $n$, the audit records the gamma word $c(n)$, its length, and the exact affine coefficients $(a_n,q_n)$. It verifies $$q_n=2^{-\ell(n)}$$ and checks prefix freeness on the full integer registry before any prime, square, or control filter is applied. Branch coefficients are rational, so floating point is unnecessary.

## Polynomial-chain checks

For rational $a,q,w$ and degrees $N$, the matrices [\[eq:M0\]](#eq:M0){reference-type="eqref" reference="eq:M0"}--[\[eq:M1\]](#eq:M1){reference-type="eqref" reference="eq:M1"} are formed exactly. The primary certificate is the polynomial identity $$\det(I-zwM_0)=(1-zw)\det(I-zwM_1),$$ alongside $DM_0=M_1D$. Power supertraces through a fixed display depth serve as readable checksums but are not substituted for the characteristic polynomial identity.

For weighted branch sums the corresponding identities are $$DL_0=L_1D,
 \qquad
 \det(I-zL_0)=\left(1-z\sum_jw_j\right)\det(I-zL_1).$$ The ordinary block product is computed separately and must differ from the graded ratio.

## Global and control checks

The audit uses identical branches and weights in both assemblies. It must recover $$1-z\sum_jw_j
 \quad\text{and}\quad
 \prod_j(1-zw_j)$$ for shared and disjoint recurrence, respectively. Primitive cyclic words up to a frozen length are canonicalized by rotation and classified as pure or mixed. Their connected-log coefficients must account exactly for the difference between the two expressions.

The full construction is rerun without a code change on primes, squares, Fibonacci values, all integers, a seeded matched-density random set, a SHA-derived set, and an explicit arbitrary decidable inventory. Success of every disjoint control is an expected failure of arithmetic selectivity.

L1.1cmL5.7cmY ID & Exact certificate & Falsified shortcut\
E1 & prefix-free code registry and $q_n=2^{-\ell(n)}$ & fitted or inconsistent branch histories\
E2 & scalar residual $-2q/(1+q)$ & first-trace normalization promoted to all powers\
E3 & entire-versus-pole symbolic check & ordinary matrix advertised as negative multiplicity\
E4 & $DM_0=M_1D$ & parity actions that do not form a chain map\
E5 & full characteristic-polynomial quotient & finite power table advertised as all-order proof\
E6 & ordinary block product beside graded ratio & quotient relabelled as ordinary determinant\
E7 & shared/disjoint determinant comparison & component separation hidden inside one object\
E8 & primitive mixed-necklace ledger & mixed trace coefficients silently dropped\
E9 & arbitrary-inventory and matched controls & supplied inventory mistaken for arithmetic selection\
E10 & digit and return marker outputs & first-return induction presented as graph-step equality\

## Finalized exact evidence

The independent exact implementation passed all 53 registered tests. Its source registry contained 4,095 branches for $2\le n\le4096$; the prefix-free audit included $n=1$ and found zero collision pairs among 4,096 gamma words. All branch derivatives equalled $2^{-\ell(n)}$ exactly, and the source registry was generated before inventory tags were applied.

L3.3cmL3.5cmY Audit block & Census & Outcome\
scalar and ordinary fiber & 3,066 scalar rows; 5 matrix firewalls & all 511 first-power fits pass; all 2,555 power-two-through-six scalar rows fail as predicted\
de Rham chain and local determinants & 40 chain/characteristic rows; 320 supertrace rows; 20 telescoping and 20 ownership rows & every chain, characteristic quotient, power through eight, local telescope, and ordinary/graded distinction passes\
shared/disjoint recurrence & 21 determinant rows; 168 power rows on the first four labels of each finite fixture & mixed difference appears from power two; shared and disjoint formulas match their distinct frozen objects\
primitive necklaces & 1,183 primitive rows through length six; 1,174 mixed & every enumerated mixed row survives the shared de Rham grading\
inventory, marker, and domain & 42 inventory rows; 4,095 marker rows; 21 nuclearity rows & all inventory controls prove too much; every digit history keeps $u^{\ell(n)}$; the prime cohomology boundary remains $\Re s>1$\

At $n=2$, for example, $q=1/8$ and the normalized scalar second-power residual is exactly $-2/9$. All 20 ordinary-block controls also differ from their graded ratios, preventing the successful exterior identity from being relabelled as an ungraded determinant. The enumeration and controls contain no target-zero or target-root data.

The 42 inventory controls separately use full-inventory sums and the corresponding $z=1$ products at their frozen cutoffs. The finalized runner produced two fresh byte-identical 30-artifact *code/results* snapshots, and its 32-entry SHA-256 ledger passed; manuscript and documentation files are outside that byte-comparison claim. Generated result files and the full snapshot digest are reported separately from the theorem source. A failed implementation check would trigger correction of the implementation or a theorem hypothesis; it would never license parameter tuning against a target Euler coefficient.

# Route evaluation and the next gate {#sec:route}

The analytic-function-space loophole produces one genuine promotion and no arithmetic promotion. records the strict evaluation.

L1.0cmL4.2cmY Gate & Verdict & Certificate\
A0 & `STRUCTURAL_``ARITHMETIC_RELATION` & the integer code, entropy-scale length, and affine digit maps are fixed from source-side relations; selecting the prime inventory is not credited\
A1 & `FAIL` & shared recurrence retains mixed primitive necklaces; disjoint recurrence imports components and collapses to atom loops; digit time also retains $u^{\ell(n)}$\
A2 & `ANALYTIC_DETERMINANT` & both parity operators are honest trace-class holomorphic transfers on $\Re s>1$, and their full graded/relative Fredholm determinant is exact\
A3 & `FAIL` & constant prime cohomology modes keep the $\Re s>1$ boundary; no same-object continuation, Gamma factor, functional equation, or divisor law\
A4 & `FAIL` & no natural self-adjoint, unitary, scattering, or quantum generator with the Riemann divisor is constructed\

The frozen tuple is

(A0\_STRUCTURAL\_ARITHMETIC\_RELATION, A1\_FAIL, A2\_ANALYTIC\_DETERMINANT, A3\_FAIL, A4\_FAIL).

Thus `ROUTE_A_REJECTED`. Route B remains locked.

The A2 credit is deliberately narrow but real. It belongs to a pair of degreewise ordinary Fredholm determinants and their graded ratio. It does not belong to the ordinary ungraded block determinant. It also does not transfer the disjoint Euler ledger to the shared object or the return marker to digit time.

## The smallest Paper26 obligation

The tangent/exterior loophole is now classified. Any next signed escape inside shared recurrence must act on branch combinatorics rather than local stability. Freeze a shared prefix-renewal or factorization grammar before target comparison, and seek a source-derived cyclic incidence complex with $$\chi_{\rm cyc}(\alpha)=
 \begin{cases}
 1,&\alpha\text{ is a monochromatic primitive cyclic word},\\
 0,&\alpha\text{ uses at least two return colors}.
 \end{cases}
 \label{eq:selector-target}$$

The candidate must pass five gates:

1.  its chain groups, differential, and grading are functorially derived from the frozen multiplication/factorization source, with no hidden prime-support bit;

2.  the full cyclic supertrace, not merely the Euler characteristic of one word, satisfies [\[eq:selector-target\]](#eq:selector-target){reference-type="eqref" reference="eq:selector-target"} at every temporal repetition;

3.  pure words survive with coefficient one while every mixed primitive necklace cancels;

4.  all degrees are trace class on the same shared analytic space, or a legitimate relative determinant is proved;

5.  the identity holds at the original digit marker and passes prime, square, Fibonacci, random, hash, and arbitrary-inventory controls.

The decisive alternative is a selector-or-collapse dichotomy: either the first source-derived shared complex cancels mixed primitive necklaces while retaining pure repetitions, or its surviving cohomology splits into one monochromatic sector per supplied label and is determinant-equivalent to the disjoint atom inventory. Bar, Hochschild, divisor-incidence, and Möbius analogies remain clues until they meet these operator and ownership gates.

# Conclusion {#sec:conclusion}

The holomorphic loophole is real. A logarithmic-code contraction with $q>0$ need not collapse to rank one: its canonical zero-/one-form pair removes the fixed-point denominator at every repetition, and the full graded determinant gives the exact one-loop factor. Scalar normalization and ordinary tensor fibers cannot do this. The positive result is therefore both analytic and structural.

Its arithmetic ceiling is equally exact. Lefschetz cancellation removes tangent stability from every legal word; it does not decide which branch words should exist. One shared disk retains all mixed renewal necklaces. Disjoint disks produce an Euler product only because recurrent components have already been separated, and cohomology reduces them to a diagonal atom-loop inventory. The same mechanism factors arbitrary sets. It also retains logarithmic code duration at digit time and the prime $\Re s>1$ trace-class boundary.

SD-C27 therefore advances the determinant gate without advancing the primitive arithmetic, continuation, or spectral gates. The next viable experiment must attach a source-derived cyclic complex to branch content and survive a selector-or-collapse test on the original shared marked object. Until that happens, Route A is rejected and Route B remains locked.

# Proof details {#app:proofs}

## Triangular affine pullback

For $\phi(z)=a+qz$, $$U_{\phi,0}z^k=(a+qz)^k
 =\sum_{j=0}^k\binom{k}{j}a^{k-j}q^jz^j.$$ Thus the finite monomial matrix is upper triangular by degree and has diagonal $1,q,\ldots,q^N$. On one-forms, $$U_{\phi,1}(z^kdz)=q(a+qz)^kdz,$$ whose diagonal is $q,q^2,\ldots,q^N$ on $P_{N-1}dz$. This proves directly that $$\begin{aligned}
 \operatorname{Tr}(wU_{\phi,0}|P_N)^r
 &=w^r\sum_{m=0}^Nq^{rm},\\
 \operatorname{Tr}(wU_{\phi,1}|P_{N-1}dz)^r
 &=w^r\sum_{m=1}^Nq^{rm},\end{aligned}$$ so their difference is $w^r$ for every $N$ and $r$.

To check the chain identity on a monomial, compute $$\begin{aligned}
 dU_{\phi,0}z^k
 &=kq(a+qz)^{k-1}dz,\\
 U_{\phi,1}d z^k
 &=U_{\phi,1}(kz^{k-1}dz)
 =kq(a+qz)^{k-1}dz.\end{aligned}$$ This is $DM_0=M_1D$ in matrix form.

## Finite cohomological determinant identity

Choose the invariant constants $C\subset P_N$ and the quotient $P_N/C$. Differentiation induces an isomorphism $$\overline d:P_N/C\longrightarrow P_{N-1}dz.$$ The chain identity makes the induced zero-form quotient action similar to the one-form action. In a basis adapted to $C\subset P_N$, the weighted zero-form matrix is block upper triangular with the scalar $w$ on $C$ and a block similar to $wM_1$ on the quotient. Therefore $$\det(I-zwM_0)=(1-zw)\det(I-zwM_1).$$

For a weighted sum $L_k=\sum_jw_jM_{j,k}$, constants carry $S_w=\sum_jw_j$, and the same quotient similarity yields $$\det(I-zL_0)=(1-zS_w)\det(I-zL_1).$$ No commutativity among the branch matrices is used.

## Tensor moment obstruction in full detail

For trace-class $B$, the Fredholm determinant has the local expansion $$\log\det(I-tB)=-\sum_{r\ge1}\frac{t^r}{r}\operatorname{Tr}B^r.$$ If $\operatorname{Tr}B^r=1-q^r$, then $$\begin{aligned}
 \log\det(I-tB)
 &=-\sum_{r\ge1}\frac{t^r}{r}
   +\sum_{r\ge1}\frac{(qt)^r}{r}\\
 &=\log(1-t)-\log(1-qt).\end{aligned}$$ Exponentiation gives $(1-t)/(1-qt)$ on a neighborhood of zero. By analytic continuation it would equal the entire Fredholm determinant away from its alleged pole, which is impossible. The argument applies equally to a finite matrix. It uses the full moment sequence; a search over small matrices is only a regression test.

## Absolute fixed-word summation

For the code inventory $n\ge2$, one has $|q_n|\le2^{-3}$. Hence for every nonempty word $\alpha$, $$\left|\frac1{1-q_\alpha}\right|
 \le\frac1{1-2^{-3}}.$$ If $\sum_j|w_j|<\infty$, then at power $r$ $$\sum_{\alpha\in J^r}|w_\alpha|
 =\left(\sum_j|w_j|\right)^r<\infty.$$ The degree-zero and degree-one fixed-word traces are therefore absolutely summable. Termwise subtraction is justified and yields $$\sum_{\alpha\in J^r}
 w_\alpha\left(\frac1{1-q_\alpha}
 -\frac{q_\alpha}{1-q_\alpha}\right)
 =\sum_{\alpha\in J^r}w_\alpha=S_w^r.$$

## Primitive-necklace identity

Let $A_r=(\sum_jw_j)^r$. The shared connected trace logarithm is $$\sum_{r\ge1}\frac{z^r}{r}A_r
 =-\log\left(1-z\sum_jw_j\right).$$ Every word has a unique representation as a positive power of a primitive cyclic word together with a choice of starting point. Grouping the word sum by this primitive root gives $$-\log\left(1-z\sum_jw_j\right)
 =-\sum_{[\alpha]\ \mathrm{primitive}}
   \log(1-z^{|\alpha|}w_\alpha),$$ which exponentiates to [\[eq:necklace-product\]](#eq:necklace-product){reference-type="eqref" reference="eq:necklace-product"}. Pure one-letter roots generate the repeated terms $w_j^r$; roots using multiple labels generate the mixed ledger.

## Direct-sum determinant and trace class

For a direct sum $T=\bigoplus_nT_n$, the sufficient trace-class condition $\sum_n\lVert T_n\rVert_1<\infty$ gives $$\det(I-zT)=\prod_n\det(I-zT_n)$$ locally uniformly in $z$. Here the common compact-containment estimate gives $\lVert U_{\phi_n,k}\rVert_1\le C_k$, uniformly in $n$. Thus $$\sum_{n\in S}\lVert n^{-s}U_{\phi_n,k}\rVert_1
 \le C_k\sum_{n\ge2}n^{-\Re s}<\infty$$ for $\Re s>1$. Componentwise application of [\[eq:local-det-identity\]](#eq:local-det-identity){reference-type="eqref" reference="eq:local-det-identity"} proves [\[eq:disjoint-det\]](#eq:disjoint-det){reference-type="eqref" reference="eq:disjoint-det"}.

## Prime cohomology boundary

The diagonal cohomology operator $C_{\mathbb P,s}$ is normal with singular values $p^{-\Re s}$. Hence $$\lVert C_{\mathbb P,s}\rVert_1=\sum_pp^{-\Re s}.$$ Euler's divergence of $\sum_pp^{-1}$ gives the boundary at $1$. This is an operator statement, independent of any meromorphic continuation of the scalar determinant ratio.

# Scope, provenance, and ownership ledger {#app:scope}

L3.4cmL4.3cmY Object & Frozen definition & Authorized conclusion\
zero-form determinant & $\det(I-zL_0)$ & ordinary trace-class Fredholm determinant with stability denominators\
one-form determinant & $\det(I-zL_1)$ & ordinary derivative-twisted Fredholm determinant\
ungraded block determinant & $\det(I-z(L_0\oplus L_1))$ & product of degreewise determinants; no parity cancellation\
graded determinant & $\det(I-zL_0)/\det(I-zL_1)$ & relative quotient and full supertrace; not one ordinary block determinant\
cohomology determinant & determinant of the surviving constant-state action & equal to the graded ratio in this frozen complex\

L2.5cmL3.3cmL4.1cmY Choice & Recurrent object & Graded factor & Surviving obstruction\
shared, digit time & one disk; binary histories & $1-\sum_nu^{\ell(n)}n^{-s}$ & mixed returns and nonuniform digit length\
shared, return time & induced full return shift & $1-z\sum_nn^{-s}$ & mixed primitive necklaces\
disjoint, digit time & one disk per supplied label & $\prod_n(1-u^{\ell(n)}n^{-s})$ & imported inventory and nonuniform digit length\
disjoint, return time & induced atom-loop union & $\prod_n(1-zn^{-s})$ & imported inventory; cohomological atom collapse\

L4.0cmL2.6cmY Statement & Status & Boundary\
holomorphic fixed-point trace and nuclearity & external theorem specialized & compactly contained affine map-weight systems\
scalar all-power rigidity & proved here & scalar normalization of one affine branch\
ordinary tensor-fiber obstruction & proved here & finite or trace-class tensor fiber; not every nontensor nuclear operator\
canonical de Rham cancellation & classical mechanism, exact model proof here & zero-/one-form pullbacks; graded ratio only\
shared renewal collapse & proved here & finite or absolutely summable branch families on one disk\
disjoint atom-loop equivalence & proved here & supplied component inventory on private disks\
A3 failure & theorem consequence & frozen operator pair and cohomology spectrum\
A4 failure & evaluation & no mechanism constructed; no universal spectral no-go\

The source code is frozen before evaluation. Prime, square, Fibonacci, random, hash, and arbitrary-inventory labels belong to post-freeze controls. No Riemann-zero data, Euler-coefficient fit, cutoff-dependent branch rule, or hidden prime return is admissible.

The finite polynomial complex supplies exact characteristic-polynomial certificates. The infinite Bergman theorem uses nuclear word traces and does not assert boundedness of $d:A^2(\mathbb D)\to A^2(\mathbb D)dz$. The equality of the graded ratio and a cohomology determinant is a theorem for this frozen pair, not a blanket assertion for arbitrary unbounded complexes.

The following statements are explicit nonclaims:

-   no universal obstruction to all signed, anisotropic, nontensor, or nonlocal transfer constructions;

-   no intrinsic prime selector in the Elias code or affine translations;

-   no identification of the graded ratio with an ordinary ungraded Fredholm determinant;

-   no identification of shared and disjoint recurrence;

-   no identification of digit and completed-return markers;

-   no same-object continuation into the critical strip;

-   no functional equation, Riemann divisor, RH implication, or Hilbert--Pólya operator.

The final route record is

(A0\_STRUCTURAL\_ARITHMETIC\_RELATION, A1\_FAIL, A2\_ANALYTIC\_DETERMINANT, A3\_FAIL, A4\_FAIL),\
ROUTE\_A\_REJECTED,ROUTE\_B\_LOCKED.
