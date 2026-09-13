---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--14-tensor-bar-mobius-selector"
canonical_tex: "symbolic_dynamics/papers/14-tensor-bar-mobius-selector/main.tex"
canonical_pdf: "symbolic_dynamics/papers/14-tensor-bar-mobius-selector/main.pdf"
source_sha256: "ed28a15d3d1a0377d30d69b9a88d4b3236dad19f52418e49d6d09b076aa3d3da"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Functorial Tensor Characters and Möbius Bar Codes: Valuation Rigidity and Universal Euler Inversion

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/14-tensor-bar-mobius-selector>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/14-tensor-bar-mobius-selector/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/14-tensor-bar-mobius-selector/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/14-tensor-bar-mobius-selector/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/14-tensor-bar-mobius-selector/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We ask whether tensor multiplication, topological entropy, and a local symbolic grammar can generate an integer or abelian character that is nontrivial on tensor-prime full shifts while vanishing on composites and matched controls. The standard character route is rigid. Every abelian monoidal charge is a valuation sum; vanishing on both $p^2$ and $p^3$ forces vanishing on $p$. Every coherent cocycle on the thin tensor-divisor category is a coboundary, a regular entropy character merely translates the Dirichlet parameter, and functorial observables are invariant under pure presentation shuffles. We then freeze SD-C16, a one-vertex countable signed edge shift whose edges are nonempty ordered words of nonunit full shifts, whose roof is the entropy sum, and whose sign is reduced-bar parity. Its raw adjacency sum converges for $\operatorname{Re}s>\sigma_{\rm bar}$, where $\zeta(\sigma_{\rm bar})=2$, and its canonical scalar Fredholm determinant obeys $D_{\rm bar}(s,z)=1-zF_{\rm bar}(s)$ and $D_{\rm bar}(s,1)=1/\zeta(s)$. Finite endpoint grouping gives a tensor-divisor Möbius completion on $\operatorname{Re}s>1$; differentiating the same determinant inserts only the frozen roof and yields $\Lambda_{\!\otimes}=\mu_{\!\otimes}*h$. This is a bounded symbolic realization, not a new Möbius--Mangoldt identity. Primitive code cycles are factorization necklaces rather than primes, and the same bar grammar inverts every weighted inventory. The latter control proves too much: the determinant is genuine but not arithmetically selective. Route A is therefore rejected, Route B remains locked, and no claim about the Riemann hypothesis is made.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Functorial Tensor Characters and Möbius Bar Codes:\
  Valuation Rigidity and Universal Euler Inversion
```

## Markdown 正文

# Introduction {#sec:introduction}

The finite full shift on $n$ symbols, denoted $\mathsf F_n$, carries two elementary structures that are unusually well aligned. Cartesian product is again a full shift, $$\mathsf F_m\otimes\mathsf F_n\cong\mathsf F_{mn},$$ and topological entropy converts this tensor multiplication into addition, $h(\mathsf F_n)=\log n$. Tensor-indecomposable objects are consequently the $\mathsf F_p$. This makes the full-shift inventory a natural place to ask a sharp symbolic question: can a character generated only by tensor multiplication, entropy, and a local factorization grammar select those atoms and their repetitions without inserting a prime table?

The phrase "generated only" is the important restriction. An arbitrary assignment of phases to the atom set can reproduce any desired Euler factor, but it does so by loading one free parameter per prime. Likewise, applying a precomputed von Mangoldt coefficient to a closed word would reproduce the target support by definition. Neither maneuver explains the arithmetic inside one symbolic system. We therefore freeze the tensor monoid, the entropy clock, exact local divisor chains, and functorial transfer operations before inspecting any target data.

The first conclusion is negative and stronger than a failed numerical scan. Every abelian monoidal charge is a valuation sum. If it vanishes on the composites $p^2$ and $p^3$, it also vanishes on $p$. This argument works in every abelian group, including groups with torsion. Moving the charge from objects to arrows does not help: the thin tensor-divisor category has an initial object, so every coherent abelian one-cocycle is a coboundary. A regular character obtained from entropy merely translates the complex parameter, and functoriality makes pure presentation shuffles conjugate rather than destructive. These facts close the standard integer/abelian-character route.

The positive response is not another character. It is a higher-chain incidence construction represented by one recurrent symbolic object. Our candidate SD-C16 is the one-vertex countable edge shift whose return edges are all nonempty ordered words $(\mathsf F_{a_1},\ldots,\mathsf F_{a_k})$ of nonunit full shifts. The edge roof is the entropy sum and the sign is $(-1)^{k+1}$. If $$B(s)=\sum_{n\ge2}e^{-s h(\mathsf F_n)}=\zeta(s)-1,$$ then the raw weighted adjacency is the reduced-bar series $$F_{\rm bar}(s)=B(s)-B(s)^2+B(s)^3-\cdots
           =\frac{B(s)}{1+B(s)}.$$ The equality is an absolutely convergent edge-alphabet sum when $\operatorname{Re}s>\sigma_{\rm bar}$, where $\zeta(\sigma_{\rm bar})=2$. Since the vertex space is one-dimensional, the canonical Fredholm determinant is $$D_{\rm bar}(s,z)=1-zF_{\rm bar}(s),
  \qquad
  D_{\rm bar}(s,1)=\frac{1}{\zeta(s)}.$$ This closes a narrow but real source-lock obligation: the factorization words, symbolic recurrence, trace repetitions, and determinant belong to the same frozen shift.

There are two qualifications. First, the raw edge sum and its endpoint-grouped incidence completion have different domains. For a fixed endpoint $n$, the alternating ordered-factorization sum is finite and equals $-\mu_{\!\otimes}(n)$. Grouping endpoints first therefore gives an absolutely convergent completion on $\operatorname{Re}s>1$, but it does not turn the raw countable alphabet into an absolutely summable alphabet there. Second, differentiating the same determinant gives $$\frac{d}{ds}\log D_{\rm bar}(s,1)
  =-\frac{\zeta'(s)}{\zeta(s)}
  =\sum_{n\ge1}\Lambda_{\!\otimes}(n)n^{-s},
  \qquad \Lambda_{\!\otimes}=\mu_{\!\otimes}*h.$$ Only the already-frozen entropy roof is inserted by differentiation. $\mu_{\!\otimes}$ and $\Lambda_{\!\otimes}$ are outputs of signed chain cancellation, not input weights.

The construction is nevertheless not an arithmetic selector. For any weighted inventory with nonunit partition sum $B_X$, the same reduced-word grammar yields $F_X=B_X/(1+B_X)$ and $D_X=(1+B_X)^{-1}$. It returns $1/\zeta$ here because the all-full-shift entropy partition is already $\zeta$. Moreover, primitive cycles of the actual code shift are cyclic necklaces of factorization words, not individual tensor atoms. The exact Euler coefficient ledger appears only after signed aggregation. We record this universal behavior as [proves too much]{.smallcaps}, not as new analytic information about $\zeta$.

The paper makes four bounded contributions. It classifies and rules out the standard functorial abelian selectors; freezes an explicit countable symbolic phase space, clock, potential, function space, and determinant; separates raw convergence from incidence completion while deriving $\mu_{\!\otimes}*h$ from the same roof; and subjects the construction to shuffle, random-grammar, and generic-inventory controls. It does not claim a new Möbius--Mangoldt identity, an orbitwise prime correspondence, a continuation theorem, a functional equation, a spectral operator, or an implication for the Riemann hypothesis.

locates these statements relative to incidence, arithmetical-semigroup, and dynamical Möbius theory. proves the character no-go. defines SD-C16 and its determinant. derives the endpoint completion and entropy innovation. gives the adversarial audit, and records the strict route decision and the next obligation.

# Prior work and claim boundary {#sec:prior}

The ingredients of SD-C16 belong to several classical literatures. Their combination is useful for the present source lock, but the underlying Möbius identities and determinant algebra are not new.

#### Symbolic zeta functions and entropy.

Finite-state shift zeta functions admit determinant descriptions going back to @bowenlanford1970. Entropy is an intrinsic invariant of symbolic systems, and the possible entropies of topological Markov shifts have a rich arithmetic structure [@lind1984]. We use only the elementary full-shift identity $h(\mathsf F_n)=\log n$ and a weighted one-vertex adjacency. No theorem for general countable Markov shifts, pressure, or meromorphic continuation is invoked.

#### Incidence, monoid, and categorical inversion.

The incidence-algebra framework for Möbius inversion is classical [@rota1964]. Möbius functions of monoids were developed by @cartierfoata1969, and categorical formulations with functoriality appear in @contentlemayleroux1980. Our strict tensor-divisor chains and their alternating sums are a concrete instance of that prior framework. Accordingly, the parity $(-1)^{k+1}$ is canonical after choosing the reduced bar resolution, but choosing that resolution as a candidate is a modeling choice and earns no independent arithmetic credit.

#### Arithmetical semigroups.

Abstract analytic number theory transports zeta functions and arithmetic functions to normed unique-factorization semigroups [@knopfmacher1975semigroups; @knopfmacher1975functions]. Möbius inversion for flows of arithmetic semigroups provides a particularly direct neighbor [@benitonavasvarona2008]. Thus the full-shift tensor monoid, with norm $e^{h(\mathsf F_n)}=n$, is not the first abstract arithmetic semigroup, and the transported Möbius and Mangoldt-type functions are not new.

#### Two different Möbius axes.

In dynamical orbit counting, a temporal-period Möbius transform extracts least-period orbit counts from fixed-point counts. Functorial orbit counting and Dold-sequence constraints develop this axis in detail [@pakapongpunward2009; @byszewskigraffward2021]. Our $\mu_{\!\otimes}$ is instead the incidence inverse on the object relation $\mathsf F_d\mid_\otimes\mathsf F_n$. It acts within the internal factorization word of a single code edge. The integer $r$ in the trace-log is temporal repetition of code edges. These two Möbius axes are not identified.

#### The classical logarithmic derivative.

The identities $$\Lambda=\mu*\log,
  \qquad
  -\frac{\zeta'}{\zeta}(s)=\sum_{n\ge1}\Lambda(n)n^{-s}$$ are classical; authoritative formulas are recorded in NIST DLMF [@nistdlmf275]. The tensor notation $\Lambda_{\!\otimes}=\mu_{\!\otimes}*h$ expresses the same incidence relation using the entropy of full-shift objects. We claim neither a new von Mangoldt identity nor the first incidence-algebra, categorical, semigroup, or dynamical Möbius construction.

#### Bounded synthesis claim.

Within the primary sources audited, we did not locate the exact source-locked combination of the Cartesian-product monoid of finite full shifts, its intrinsic entropy norm, an explicit rigidity classification of standard functorial characters, a tensor-divisor Möbius fiber represented by one recurrent signed symbolic trace, and an adversarial route evaluation that marks the realization [proves too much]{.smallcaps}. Our contribution is limited to this synthesis and obstruction. The absence of that precise package from a bounded search is not a claim of global novelty.

Homological language will become relevant only in the next step. Classical Koszul resolutions [@priddy1970] suggest asking whether a sign-reversing reduction can be made compatible with primitive cyclic words. We do not perform that reduction here, and we do not use another dynamical system family to supply it.

# Functorial character rigidity {#sec:rigidity}

We first classify the candidate characters that can be constructed from the tensor monoid itself. This converts an open-ended scan into a finite list of algebraic obstructions.

## Universal valuation charge

Let $$\mathcal M=\{\mathsf F_n:n\ge1\}/\!\cong,
  \qquad
  \mathsf F_m\otimes\mathsf F_n=\mathsf F_{mn}.$$ The tensor unit is $\mathsf F_1$ and the nonunit atoms are $\mathsf F_p$. The Grothendieck group is the free abelian group $$K=\mathcal M^{\mathrm{gp}}\cong\bigoplus_p\mathbb Ze_p,
  \qquad
  v(\mathsf F_n)=\sum_pv_p(n)e_p.$$

[\[thm:valuation\]]{#thm:valuation label="thm:valuation"} For every abelian group $A$, restriction to tensor atoms gives a natural bijection $$\operatorname{Hom}_{\mathrm{Mon}}(\mathcal M,A)\cong\prod_p A.$$ Explicitly, every monoidal charge is $$q(\mathsf F_n)=\sum_pv_p(n)q(\mathsf F_p).
  \tag{3.1}$$ Every multiplicative unitary character similarly satisfies $\chi(\mathsf F_n)=\prod_p\chi(\mathsf F_p)^{v_p(n)}$.

Unique tensor factorization gives (3.1) for any homomorphism. Conversely, any atom assignment extends by (3.1), and the extension is additive under tensor product. Unique factorization also proves uniqueness. Composing with an additive-to-multiplicative character gives the unitary statement.

The theorem identifies both the freedom and the data-loading risk. An arbitrary sequence $q(\mathsf F_p)$ is possible, but it is an independent parameter at every atom. Functorial generation from unmarked tensor structure does not select such a sequence. In particular, if all atoms are treated symmetrically under their permutations, then $q(\mathsf F_n)=a\sum_pv_p(n)$ for one $a\in A$. That character records only the total number of tensor factors with multiplicity.

[\[cor:prime-no-go\]]{#cor:prime-no-go label="cor:prime-no-go"} No abelian monoidal charge can be nonzero on an atom and zero on every decomposable object.

For an atom $p$, the requested composite collapse gives $$2q(\mathsf F_p)=q(\mathsf F_{p^2})=0,
  \qquad
  3q(\mathsf F_p)=q(\mathsf F_{p^3})=0.$$ Subtracting yields $q(\mathsf F_p)=0$. No torsion hypothesis is needed. In multiplicative notation, $\chi(p)^2=\chi(p)^3=1$ forces $\chi(p)=1$.

This also diagnoses an initially tempting but invalid control. Prime powers are composite objects, yet a Route-A Euler ledger requires them as repetitions of a primitive prime object. A control that demands zero on *all* composites erases the target repetition sector. The correct comparison separates prime powers from objects containing at least two distinct atoms.

## Coherent divisor cocycles are gauge

Let $\operatorname{Div}(\mathcal M)$ be the thin category with one arrow $d\to n$ when $\mathsf F_d$ tensor-divides $\mathsf F_n$. An $A$-valued coherent cocycle satisfies $$\kappa(d,d)=0,
  \qquad
  \kappa(d,n)+\kappa(n,m)=\kappa(d,m)
  \quad(d\mid n\mid m).$$

[\[thm:coboundary\]]{#thm:coboundary label="thm:coboundary"} Every coherent abelian cocycle on $\operatorname{Div}(\mathcal M)$ is a coboundary: $$\kappa(d,n)=b(n)-b(d),
  \qquad b(n)=\kappa(1,n).
  \tag{3.2}$$ Consequently a character-twisted divisor transfer is diagonally conjugate to the untwisted transfer and has the same determinant wherever both are defined.

Apply coherence to the chain $1\mid d\mid n$. Then $\kappa(1,d)+\kappa(d,n)=\kappa(1,n)$, which is (3.2). Exponentiating $b$ produces the diagonal gauge implementing the conjugacy.

The initial tensor unit is the source of this rigidity. Nonzero holonomy can be retained only by remembering different ordered factorization histories instead of identifying them as the unique thin-category arrow. That is the higher-chain move made in ; it is not a rescued one-cocycle.

## Entropy and shuffle rigidity

Suppose a real charge is generated regularly from entropy and is additive under tensor product. It has the form $$q_t(\mathsf F_n)=t h(\mathsf F_n)=t\log n.$$ A unitary twist is then $$n^{-s}e^{i\theta q_t(\mathsf F_n)}
  =n^{-(s-i\theta t)},
  \tag{3.3}$$ only a vertical translation of $s$. If $q_t$ is also integer-valued on every $\mathsf F_n$, then $t=0$: otherwise $t\log2$ and $t\log3$ would be integers, making $\log2/\log3$ rational and contradicting unique factorization.

Finally, let a transfer construction be natural under isomorphisms of the structured inventory $(\mathcal M,\otimes,h,\text{grammar})$. A pure presentation shuffle $\sigma$ changes its matrix only by $$L_{\sigma X}=P_\sigma L_XP_\sigma^{-1}.
  \tag{3.4}$$ All traces, determinants, root multisets, and character-response norms are unchanged. Therefore a nonzero arithmetic response cannot be required to collapse under a pure relabeling. If shuffling a list changes adjacency, then the list order was part of the grammar and the observed separation tests that external order, not tensor arithmetic.

The classification may be summarized as $$\begin{array}{c@{\quad\longrightarrow\quad}l}
\text{monoidal object character} & \text{valuation sum},\\
\text{coherent divisor one-cocycle} & \text{coboundary gauge},\\
\text{regular entropy character} & \text{vertical parameter translation}.
\end{array}$$ Together with shuffle naturality, this proves the scoped no-go: no standard functorially generated abelian one-character meets the desired selector criterion. It does not classify arbitrary nonlinear incidence transforms, higher chains, or every computable symbolic rule.

# The reduced tensor bar-code shift {#sec:bar}

The rigidity result says that the next candidate must retain higher factorization chains rather than compress them into an abelian one-cocycle. This section freezes that candidate completely.

## Phase space, clock, and potential

Let $\mathcal M_+=\{\mathsf F_n:n\ge2\}$. Define the countable code alphabet $$\mathcal C=\coprod_{k\ge1}\mathcal M_+^k.
  \tag{4.1}$$ A symbol $\mathbf a=(\mathsf F_{a_1},\ldots,\mathsf F_{a_k})$ is a nonempty ordered tensor word. Equivalently, it is the strict cumulative divisor chain $$\mathsf F_1<\mathsf F_{a_1}<\mathsf F_{a_1a_2}<\cdots<\mathsf F_{a_1\cdots a_k}.
  \tag{4.2}$$ The phase space is the one-vertex countable edge shift with one return edge for each $\mathbf a\in\mathcal C$. Thus a point is a bi-infinite sequence of code edges, and temporal recurrence is the ordinary shift of that sequence.

Freeze the roof, parity, and complex weight $$\begin{split}
  T(\mathbf a)&=\sum_{j=1}^k h(\mathsf F_{a_j})
               =\log(a_1\cdots a_k),\\
  \varepsilon(\mathbf a)&=(-1)^{k+1},\\
  \phi_s(\mathbf a)&=\varepsilon(\mathbf a)e^{-sT(\mathbf a)}.
\end{split}
\tag{4.3}$$ The sign is determined by reduced-bar length after the bar grammar has been chosen. The choice of this grammar is a modeling choice, not an output of the entropy and not evidence for arithmetic selectivity. Crucially, no prime predicate, Möbius coefficient, Mangoldt coefficient, zero table, or per-atom phase occurs in (4.1)--(4.3).

The construction remembers ordered histories. It is functorial under isomorphisms of the tensor monoid, but it does not descend to the unique arrow of the thin divisor category. This is exactly why does not gauge it away.

## Raw alphabet sum

Let $$B(s)=\sum_{n\ge2}e^{-s h(\mathsf F_n)}
      =\sum_{n\ge2}n^{-s}=\zeta(s)-1.
  \tag{4.4}$$ The total weight of length-$k$ code edges is $(-1)^{k+1}B(s)^k$ whenever the sum may be rearranged. Absolute summability of the raw alphabet requires $$\begin{split}
  \sum_{\mathbf a\in\mathcal C}|\phi_s(\mathbf a)|
  &=\sum_{k\ge1}\sum_{a_1,\ldots,a_k\ge2}
    (a_1\cdots a_k)^{-\operatorname{Re}s}\\
  &=\sum_{k\ge1}B(\operatorname{Re}s)^k<\infty.
\end{split}
\tag{4.5}$$

Let $\sigma_{\rm bar}$ be the unique real solution of $$\zeta(\sigma_{\rm bar})=2.$$ Numerically, $\sigma_{\rm bar}=1.7286472389981836181\ldots$.

Uniqueness follows because $\zeta(\sigma)-1$ is continuous and strictly decreasing from $+\infty$ to $0$ on $\sigma>1$. Equation (4.5) is finite exactly for $\operatorname{Re}s>\sigma_{\rm bar}$.

[\[prop:raw\]]{#prop:raw label="prop:raw"} For $\operatorname{Re}s>\sigma_{\rm bar}$, the raw edge sum is absolutely convergent and $$F_{\rm bar}(s)
  :=\sum_{\mathbf a\in\mathcal C}\phi_s(\mathbf a)
  =\sum_{k\ge1}(-1)^{k+1}B(s)^k
  =\frac{B(s)}{1+B(s)}.
  \tag{4.6}$$

In the stated half-plane, $|B(s)|\le B(\operatorname{Re}s)<1$. The absolute bound (4.5) permits Fubini rearrangement by internal word length. The resulting series is geometric, which proves (4.6).

The domain in belongs to the source lock. An analytic formula obtained by regrouping coefficients below $\sigma_{\rm bar}$ must not be mislabeled as the raw sum over code edges.

## Function space and canonical determinant

The weighted vertex adjacency of a one-vertex edge shift acts on $$\mathcal B=\ell^2(\{*\})\cong\mathbb C.$$ After the alphabet sum has converged, define $$L_{\mathrm{bar},s}c=F_{\rm bar}(s)c.
  \tag{4.7}$$ This is a one-dimensional trace-class operator. Its $r$th trace is $F_{\rm bar}(s)^r$, the weight sum of all based temporal words of $r$ code edges. Thus the scalar operator is the weighted adjacency of the frozen recurrent shift, rather than an unrelated scalar attached after factorization.

[\[thm:determinant\]]{#thm:determinant label="thm:determinant"} For $\operatorname{Re}s>\sigma_{\rm bar}$, the canonical determinant of SD-C16 is $$D_{\rm bar}(s,z)
  :=\det_{\mathbb C}(I-zL_{\mathrm{bar},s})
  =1-zF_{\rm bar}(s).
  \tag{4.8}$$ At the frozen specialization $z=1$, $$D_{\rm bar}(s,1)=\frac{1}{\zeta(s)}.
  \tag{4.9}$$

Equation (4.8) is the determinant of the one-dimensional operator (4.7). Using (4.4) and (4.6), $$1-F_{\rm bar}(s)=1-\frac{B(s)}{1+B(s)}
             =\frac1{1+B(s)}=\frac1{\zeta(s)}.$$

The theorem is stronger than merely rewriting the classical logarithmic derivative: it identifies a single weighted symbolic adjacency whose determinant has the required value in a proved raw domain. It is also much weaker than an RH mechanism. The partition sum $1+B(s)$ equals $\zeta(s)$ because the source inventory already contains exactly one $\mathsf F_n$ at every integer entropy $\log n$.

## Trace-log and primitive cycles

Whenever $|zF_{\rm bar}(s)|<1$, the determinant has the convergent trace expansion $$\log D_{\rm bar}(s,z)
  =-\sum_{r\ge1}\frac{z^r}{r}\operatorname{tr}L_{\mathrm{bar},s}^r
  =-\sum_{r\ge1}\frac{z^r}{r}F_{\rm bar}(s)^r.
  \tag{4.10}$$ The sign in (4.3) is an ordinary scalar edge weight. Repeating a single code edge $\mathbf a$ exactly $r$ times contributes $$\varepsilon(\mathbf a)^r e^{-rsT(\mathbf a)}.
  \tag{4.11}$$ It is not a chain grading or supertrace parity: an odd supertrace sector would carry one fixed minus sign at every repetition order, whereas a negative scalar edge alternates with $r$. We therefore claim no chain complex, contractible-pair cancellation, or homological reduction in this paper.

The primitive cycles behind (4.10) are cyclic necklaces in the countable alphabet $\mathcal C$. A one-cycle may itself be an ordered factorization chain, and longer primitive cycles concatenate several such chains. There is no canonical bijection between these necklaces and the tensor atoms $\mathsf F_p$.

At $z=1$, (4.9) gives a nonzero analytic logarithm throughout $\operatorname{Re}s>1$. We do not silently identify that logarithm with the power series (4.10) at points where $|F_{\rm bar}(s)|\ge1$. The distinction between analytic logarithm, trace-log germ, and raw alphabet sum will be maintained in the audit.

# Endpoint incidence and entropy innovation {#sec:incidence}

The raw bar shift is defined by ordered words. Tensor arithmetic appears when those words are grouped by their endpoint object. Because each endpoint has only finitely many ordered factorizations, this grouping is exact before any infinite endpoint sum is taken.

## Tensor-divisor Möbius coefficient

For functions on $\mathcal M$, define tensor-divisor convolution by $$(f*g)(n)=\sum_{d\mid n}f(d)g(n/d).
  \tag{5.1}$$ Let $\mathbf1(n)=1$ and define $\mu_{\!\otimes}$ intrinsically by $$\mu_{\!\otimes}*\mathbf1=\delta_1.
  \tag{5.2}$$ No factorization table is used in the symbolic transfer; (5.2) names the coefficient that emerges after finite endpoint cancellation.

For $n\ge2$, set $$c(n)=\sum_{k\ge1}\ \sum_{\substack{a_1,\ldots,a_k\ge2\\
                         a_1\cdots a_k=n}}
       (-1)^{k+1}.
  \tag{5.3}$$ The sum is finite because $k\le\log_2n$.

[\[thm:endpoint\]]{#thm:endpoint label="thm:endpoint"} For every $n\ge2$, $$c(n)=-\mu_{\!\otimes}(n).
  \tag{5.4}$$ The endpoint-first series $$F_{\rm bar}^{\mathrm{inc}}(s)
  =-\sum_{n\ge2}\mu_{\!\otimes}(n)n^{-s}
  \tag{5.5}$$ converges absolutely for $\operatorname{Re}s>1$ and agrees with the raw transfer in $\operatorname{Re}s>\sigma_{\rm bar}$.

The coefficient of $n^{-s}$ in $B(s)^k$ is the number of ordered factorizations in (5.3). As a formal Dirichlet series, $$1-\bigl(B-B^2+B^3-\cdots\bigr)=(1+B)^{-1}.$$ The coefficient of $(1+B)^{-1}$ is the convolution inverse in (5.2), so the nonunit coefficient in the parenthesized series is $-\mu_{\!\otimes}(n)$. For $\sigma>1$, $$\sum_{n\ge1}|\mu_{\!\otimes}(n)|n^{-\sigma}
  =\prod_p(1+p^{-\sigma})
  =\frac{\zeta(\sigma)}{\zeta(2\sigma)}<\infty,$$ which proves absolute convergence after endpoint grouping. Equality in the common domain follows from .

The theorem extends the coefficient-grouped formula, not the raw countable edge sum. In the strip $1<\operatorname{Re}s\le\sigma_{\rm bar}$, cancellation must be completed at each finite endpoint before endpoints are summed. This order is part of the mathematical object called the incidence completion.

## Möbius entropy innovation

Define the entropy newly appearing at endpoint $\mathsf F_n$ by $$\Lambda_{\!\otimes}=\mu_{\!\otimes}*h.
  \tag{5.6}$$ Equivalently, $$\Lambda_{\!\otimes}(n)=h(\mathsf F_n)-
  \sum_{\substack{d\mid n\\d<n}}\Lambda_{\!\otimes}(d),
  \qquad
  h(\mathsf F_n)=\sum_{d\mid n}\Lambda_{\!\otimes}(d).
  \tag{5.7}$$

[\[prop:lambda\]]{#prop:lambda label="prop:lambda"} The unique solution of (5.7) is $$\Lambda_{\!\otimes}(p^r)=\log p,
  \qquad
  \Lambda_{\!\otimes}(n)=0$$ when $n$ contains at least two distinct tensor atoms.

Write $n=\prod_jp_j^{a_j}$. The prime-power divisors contribute $$\sum_j\sum_{r=1}^{a_j}\log p_j
  =\sum_ja_j\log p_j=\log n=h(\mathsf F_n).$$ Thus the displayed support rule solves (5.7); induction on divisibility gives uniqueness.

The result is the classical identity $\mu*\log=\Lambda$ on the frozen tensor monoid. It must not be described as an additive cocycle: $\Lambda_{\!\otimes}(pq)=0$ for distinct atoms while $\Lambda_{\!\otimes}(p)+\Lambda_{\!\otimes}(q)>0$. Nor may it be inserted after the fact as a weight on a completed closed word. Its relevance here is that it is derived by the same bar cancellation and entropy roof.

[\[cor:derivative\]]{#cor:derivative label="cor:derivative"} On $\operatorname{Re}s>1$, $$\frac{d}{ds}\log D_{\rm bar}(s,1)
  =-\frac{\zeta'(s)}{\zeta(s)}
  =\sum_{n\ge1}\Lambda_{\!\otimes}(n)n^{-s}.
  \tag{5.8}$$

Differentiate (4.9) in the raw domain. The derivative inserts the roof $T(\mathbf a)$ from (4.3). Endpoint grouping and identify its coefficient with (5.6). Both sides of (5.8) are absolutely convergent Dirichlet series for $\operatorname{Re}s>1$, extending the coefficient identity there.

This derivation answers a delicate source-lock question. If one began with $\Lambda_{\!\otimes}(n)n^{-s}$ as the edge potential, the construction would simply rewrite $-\zeta'/\zeta$. SD-C16 instead begins with the local tensor word, the entropy roof, and its bar parity. The determinant is formed first; its canonical roof derivative produces the Mangoldt-shaped output. The result is still classical arithmetic after endpoint grouping, but it is not inserted as a von Mangoldt weight.

## Universal inversion theorem

The same calculation also supplies the sharpest obstruction.

[\[prop:universal\]]{#prop:universal label="prop:universal"} Let $X$ be any countable weighted nonunit inventory with partition sum $B_X(s)$, and form the same one-vertex ordered-word shift with product weight and reduced-bar parity. Wherever the raw geometric series converges, $$F_X(s)=\frac{B_X(s)}{1+B_X(s)},
  \qquad
  D_X(s,1)=\frac1{1+B_X(s)}.
  \tag{5.9}$$

The total weight at internal length $k$ is $(-1)^{k+1}B_X(s)^k$. Geometric summation and the one-dimensional determinant give (5.9). No atom, divisor, or entropy property is used.

Thus $D=1/\zeta$ is exact, but the inversion mechanism is universal. It does not distinguish the full-shift tensor inventory from composite-only, randomized, or synthetic positive inventories. This is the central [proves too much]{.smallcaps} result.

# Adversarial audit and finite verification {#sec:audit}

The theorems determine the route decision; computation checks the implementation, finite local escape routes, convergence bookkeeping, and control semantics. The protocol used no Riemann zeros, root search, fitted phase, or fitted cutoff. All 18 unit tests and all 18 code/result checksum checks passed.

## Local character search

The local audit was inherited from the preceding character-resolved symbolic grammar and evaluated at the fixed parameters $s=2$, $z=1/3$, and cutoffs $N\in\{16,32,64,128\}$. It contains 2,574 exact rational rows from 18 named rules, with 16 presentation shuffles and 16 random-increasing controls.

Several rules that encode three through eight consecutive tensor-prime adjacency tokens pass a naive random control. They all fail when the control is strengthened to a nontrivial prefix- or block-preserving shuffle of the same marked tokens. An exhaustive scan of 256 binary radius-one truth tables found one naive pass, the prime mask itself, and zero robust passes. A scan of 260 labelled one- and two-state Mealy rules also found zero robust passes. Rank, factor-depth, $v_2$, and entropy-bin coboundaries produce the same exact continuant as their constant representative.

These finite results do not prove the algebraic no-go; they show that the implementation reproduces it and that plausible finite-local exceptions are either data-loaded masks or generic positive motion. The evidence label is `STOP_FINITE_LOCAL_SELECTOR`, consistent with .

## Global incidence and entropy controls

The global audit computed $\mu_{\!\otimes}$ recursively from the tensor-divisor relation without supplying a prime coefficient table. It represented entropy exactly in the free formal basis $\{\log p\}$ and tested cutoffs $64,128,256,512$. All 960 ledger rows satisfy the convolution inverse and the profile in ; every overlap between cutoffs agrees exactly.

At cutoff $512$, there are 117 prime-power endpoints and 394 mixed-factor endpoints. Every one of the 394 mixed-factor entropy innovations is the zero vector. The 136 inventory-control rows distinguish relabeling from changing the ambient monoid: ordered and shuffled atom lists become divisor closed after the tensor unit is adjoined, whereas composite-only and generic random lists do not redefine $\mu_{\!\otimes}$. Evaluated in the ambient tensor monoid, each inventory has the predicted prime-power support.

Eight seeded entropy relabelings at four cutoffs give 32 further controls. All 32 break the selector and each creates at least 36 mixed-factor leaks. This is useful source evidence: incidence syntax alone does not carry the support rule; it is the compatibility of the tensor product with the intrinsic entropy $\log n$ that makes (5.7) close.

## Raw and grouped bar regimes

An 80-digit solve gives $$\begin{split}
\sigma_{\rm bar}={}&1.728647238998183618135103010297691464234109849335035732321285908423179
\ldots.
\end{split}$$ All 28 raw convergence rows satisfy $\operatorname{Re}s>\sigma_{\rm bar}$ and $\zeta(\operatorname{Re}s)-1<1$. The maximum 80-digit residual in the exact geometric remainder identity is $1.913\times10^{-81}$, and the maximum residual in $1-F_{\rm bar}=1/\zeta$ is $1.055\times10^{-81}$.

The experiment deliberately resolves slow convergence near the raw boundary. At internal word length $64$, the absolute truncation errors are shown in .

::: {#tab:raw}
  $s$            $|F_{\rm bar}-F_{64}|$               tail bound
  ------------ ------------------------ ------------------------
  $1.75$          $4.1976\times10^{-2}$                 $2.1861$
  $1.8$           $1.5422\times10^{-4}$    $2.4647\times10^{-3}$
  $2$            $2.5255\times10^{-13}$   $1.1701\times10^{-12}$
  $1.9+0.6i$     $4.5195\times10^{-14}$    $2.9584\times10^{-8}$

  : Raw word-length residuals and rigorous absolute geometric tail bounds at $L=64$. The complex point uses the same absolute bound $B(\operatorname{Re}s)^{L+1}/(1-B(\operatorname{Re}s))$.
:::

Independently, all 512 formal endpoint rows enumerate ordered factorization layers and compute the Dirichlet inverse. Every row satisfies exactly $$[n]F_{\rm bar}=-\mu_{\!\otimes}(n),
  \qquad
  [n]D_{\rm bar}=\mu_{\!\otimes}(n).$$ This verifies the endpoint completion separately from raw word summation. As a numerical observation only, an 80-digit Möbius sieve through $10^5$ gives determinant residuals ranging from $1.55\times10^{-4}$ at $s=1.1$ to $1.59\times10^{-7}$ at $s=1.7$; these conditional partial sums are not used as proof or zero-fitting metrics.

The trace-log matrix contains 81 rows over three source points, three $z$ values, and repetition cutoffs through $256$, always with $|zF_{\rm bar}(s)|<1$. At the final cutoff its maximum trace-log residual is $7.16\times10^{-30}$. This verifies temporal repetitions of the scalar return sum, not an atom-to-primitive-cycle bijection.

## Universal controls

The identical alternating grammar was applied to ten inventories, including all-object, composite-only, prime-only, random-positive, random-support, synthetic-signed, shuffled-ramp, and scalar examples. Explicit word layers and an independent Dirichlet inverse agree exactly in all ten cases, with zero convolution mismatch. Every case satisfies (5.9).

This successful control is negative evidence. It gives $$\texttt{STOP\_ARITHMETIC\_SELECTIVITY / PROVES\_TOO\_MUCH}.$$ The arithmetic content lies in the chosen tensor inventory and compatible entropy; the reduced-bar inversion itself is universal. Pure shuffles remain invariant, as functoriality requires, rather than collapsing.

## Audit summary

L0.33X Label & Reason\

  --------------------
  `GO_FUNCTORIAL_`
  `COCYCLE_RIGIDITY`
  --------------------

  : Frozen evidence labels. Exact finite verification does not upgrade the route beyond the analytic theorems.

& Valuation, coboundary, entropy, and shuffle classifications are exact.\

  -------------------------
  `GO_TENSOR_MOBIUS_`
  `INCIDENCE_DETERMINANT`
  -------------------------

  : Frozen evidence labels. Exact finite verification does not upgrade the route beyond the analytic theorems.

& One frozen shift yields the raw determinant, endpoint completion, and roof derivative.\

  -------------------------
  `STOP_PRIME_EXCLUSIVE_`
  `ABELIAN_CHARACTER`
  -------------------------

  : Frozen evidence labels. Exact finite verification does not upgrade the route beyond the analytic theorems.

& The $p^2,p^3$ relations erase every abelian atom charge.\

  -------------------------
  `STOP_ORBITWISE_PRIME_`
  `CORRESPONDENCE`
  -------------------------

  : Frozen evidence labels. Exact finite verification does not upgrade the route beyond the analytic theorems.

& Primitive code cycles are factorization necklaces.\

  --------------------
  `STOP_ARITHMETIC_`
  `SELECTIVITY`
  --------------------

  : Frozen evidence labels. Exact finite verification does not upgrade the route beyond the analytic theorems.

& All ten generic inventories obey the same reciprocal inversion.\

# Route decision and next obligation {#sec:route}

SD-C16 establishes two exact statements that were absent from the preceding local-character search. First, it proves that standard functorial abelian charges cannot supply the desired tensor selector. Second, it places signed factorization histories, temporal repetition, a Fredholm determinant, finite endpoint incidence cancellation, and the entropy derivative inside one source-locked symbolic object.

Those gains do not satisfy Route A. The frozen evaluation is

The A0 credit is analytic: the tensor atoms, their powers, the entropy norm, and the incidence coefficients arise from one full-shift source without target spectra. A1 is weak because the actual primitive cycles are factorization necklaces and the prime-power ledger appears only after signed endpoint aggregation. A2 is analytic in the declared domains: the raw one-dimensional trace-class determinant exists for $\operatorname{Re}s>\sigma_{\rm bar}$, and its endpoint-first incidence completion is analytic for $\operatorname{Re}s>1$.

A3 fails decisively. Universal reciprocal-partition inversion gives no arithmetic selectivity, new continuation, completed functional equation, Gamma factor, global divisor theorem, Riemann--von Mangoldt counting law, or Weil-type compression. A4 fails because no natural unitary, scattering, Hamiltonian, or self-adjoint lift is constructed. Route B is false for this candidate and remains locked.

#### Paper 15 obligation.

The next step stays inside the same symbolic family and acts before determinant-level regrouping. Starting from SD-C16, construct a canonical sign-reversing involution, quotient grammar, or bar-to-Koszul reduction at the level of primitive cyclic code words. Exactly one of two outcomes should be accepted:

1.  A reduced shift has primitive classes $p\leftrightarrow\gamma_p$ and $p^r\leftrightarrow\gamma_p^r$ before the trace-log, retains a trace-class determinant and a nontrivial same-object sector, and fails randomized-factorization controls for a structural reason.

2.  A rigidity theorem proves that Möbius bar cancellation is compatible only with universal algebraic inversion, not with primitive cyclic reduction; any reduction either collapses to diagonal atom loops or becomes determinant invisible.

Pure presentation shuffles must remain invariant in either outcome, and composite controls must continue to distinguish prime powers from mixed-factor composites. No other system family is authorized as a repair.

The present result is therefore a useful rejection, not a weak success claim: the determinant identity is exact, the inserted-weight objection is closed, and the remaining gap has been localized to primitive cyclic reduction.

# Proof details and scope ledger {#app:proofs}

## Finite incidence matrices

For a finite divisor-closed set $S\subset\mathcal M$ containing $\mathsf F_1$, order objects by entropy and let $R_S(d,n)=1$ when $d$ strictly tensor-divides $n$. The matrix $R_S$ is strictly upper triangular and therefore nilpotent. Its zeta matrix and inverse are $$Z_S=I+R_S,
  \qquad
  Z_S^{-1}=I-R_S+R_S^2-\cdots.
  \tag{A.1}$$ The $(1,n)$ entry of $R_S^k$ counts strict divisor chains with $k$ arrows, while the reduced ordered-factorization convention counts the corresponding nonunit increments. Alternating chain cancellation gives the same $\mu_{\!\otimes}(n)$ coefficient as . Because every fixed endpoint has finitely many chains, this coefficient stabilizes once the principal ideal of $n$ lies in $S$.

Equation (A.1) also explains cutoff overlap in the experiment: enlarging a divisor-closed principal ideal cannot change a completed coefficient already present in the smaller ideal. Random subsets that are not divisor closed do not define a competing intrinsic Möbius function; they are source controls, not alternative versions of $\mathcal M$.

## Why inverse local cocycles do not repair the character no-go

On a bidirected local grammar, an inverse-compatible edge charge satisfies $q(\bar e)=-q(e)$. Every immediate return $e\bar e$ then has neutral total charge, so the target neutral character reappears at temporal power two. On a bidirected tree, choose a root and integrate charges along the unique path to define a vertex function $b$. Then $q(e)=b(t(e))-b(o(e))$, so the charge is a coboundary and its transfer is gauge-conjugate to the untwisted one.

Pointed-positive charges avoid neutral two-cycles, but their first transverse coefficient is a generic positive sum of local cross amplitudes. It becomes arithmetically supported only if an atom mask or an equivalent support rule has already been supplied. This is why the finite-local scan in is a falsification audit rather than the source of SD-C16.
