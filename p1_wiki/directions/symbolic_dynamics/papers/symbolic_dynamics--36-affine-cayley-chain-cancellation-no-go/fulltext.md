---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--36-affine-cayley-chain-cancellation-no-go"
canonical_tex: "symbolic_dynamics/papers/36-affine-cayley-chain-cancellation-no-go/main.tex"
canonical_pdf: "symbolic_dynamics/papers/36-affine-cayley-chain-cancellation-no-go/main.pdf"
source_sha256: "ba2034ec3034834a4ccbbcc48418ebce80944f04778d58f68ab5c90e2f52dc60"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fill the Relations, Lose the Clock: Chain Quotients of an Affine Symbolic Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/36-affine-cayley-chain-cancellation-no-go>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/36-affine-cayley-chain-cancellation-no-go/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/36-affine-cayley-chain-cancellation-no-go/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/36-affine-cayley-chain-cancellation-no-go/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/36-affine-cayley-chain-cancellation-no-go/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test a source-derived chain cancellation on the affine monoids $M_r=\langle u,v\mid vu=u^rv\rangle^+$, $r\ge2$, using one formally symmetrized Cayley graph, its cyclically nonbacktracking edge shift, and the original unit generator-step marker. Filling every translated relation polygon is exact but total: the resulting Cayley complex is contractible, so no primitive recurrent homotopy class or positive-dimensional homology survives. Independently, the relation identifies a two-step path with an $(r+1)$-step path; any torsion-free additive degree invariant under the cell has $\deg(u)=0$, so the unit marker does not descend. Before quotienting, the source-coordinate damping $T_{r,\theta}=D_\theta H_rD_\theta$ is trace class on the full oriented-edge space. Its order-$(r+3)$ Fredholm trace is strictly positive because the affine relation polygon contributes $(r+3)\theta^{r(r+1)+4r+10}$. Thus the prequotient determinant and empty chain quotient are different objects. The diagonal chain superlift cancels all powers only through the generic multiplier $1-2+1=0$, so it also cancels every two-generator one-relator control and retains no arithmetic sector. An independently split exact audit passes 53/53 authority tests and locates the first excess over free-group identity-word counts at the relator length for $r=2,3,4,5$. The result is a narrow Cayley-chain no-go and a negative Route-A closure, not a new homology or zeta theory.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Fill the Relations, Lose the Clock:\
  Chain Quotients of an Affine Symbolic Shift
```

## Markdown 正文

# Introduction {#sec:introduction}

Paper 35 leaves a precise repair problem. The positive affine Cayley graph is acyclic; adjoining formal reverses creates recurrence; and Hashimoto reduction deletes immediate reversals while retaining the primitive relation word $vu\bar v\bar u^r$. Can the relation itself be cancelled directly from the same source, without a boundary representation, accepted-support projector, or changed clock?

We test the most literal answer. For $$M_r=\langle u,v\mid vu=u^rv\rangle^+,
\qquad r\ge2,$$ attach one Cayley $2$-cell at every translate of the defining relation. Read recurrence either by path homotopy or by cellular first homology. Require the free variable $z$ still to count every original oriented edge once, and require one uninduced operator on the same prequotient source to own any claimed Fredholm determinant.

This proposal fails twice before arithmetic selection is considered. The filled Cayley complex is contractible, so complete relation cancellation removes all recurrence. The same cell equates words of lengths two and $r+1$, so the unit edge marker does not descend. These are independent: one is topological, the other is a grading obstruction.

#### Analytic firewall.

The failure cannot be hidden by assigning the quotient the determinant of the unquotiented shift. A source-coordinate diagonal damping makes the full Hashimoto operator trace class, and its Fredholm trace-log has a strictly positive contribution from the relation polygon. The quotient ledger is empty. They are not two descriptions of one determinant-bearing object.

#### Generic-control firewall.

The obvious graded lift has one even vertex orbit, two odd edge orbits, and one even cell orbit. Its supertrace multiplier is $1-2+1=0$ for every power. That cancellation is genuine but relation-blind: it holds for every two-generator one-relator presentation and retains nothing.

#### Contributions.

The paper establishes four source-locked claims.

-   Complete Cayley-cell cancellation is total, by a one-relator monoid contractibility theorem whose hypotheses are checked explicitly.

-   The original generator-step germ fails to descend by the identity $(r-1)\deg(u)=0$.

-   A trace-class damped Hashimoto operator owns a positive relation-cycle Fredholm coefficient on the full prequotient edge space.

-   The scalar chain superdeterminant is identically one for the generic cell-count reason $1-2+1=0$.

The baseline $r=4$ is composite; $r=2,3,5$ and balanced $r=1$ are controls. No prime basis, factorization oracle, terminal support, KMS/GNS slice, fitted coefficient, or target-zero data defines the source.

#### Scope.

We do not claim a new Cayley-complex, Fox-calculus, path-homology, or Ihara theory. The contribution is the narrow incompatibility among total relation filling, nonzero primitive recurrence, the original free marker, and same-object Fredholm ownership. Matrix-valued non-flat coefficient systems on the unquotiented shift remain a separate problem.

# Primary literature and claim boundary {#sec:literature}

The decisive topology is known. Gray and Steinberg construct contractible CW complexes for one-relator monoids and identify when the ordinary Cayley complex is contractible in the torsion-free incompressible case [@GraySteinberg2022]. We verify those hypotheses for $M_r$; we do not claim contractibility as a new theorem. The cellular boundary is the familiar presentation boundary encoded by Fox differential calculus [@Fox1953]. The group completion is the solvable member of the original two-generator one-relator family [@BaumslagSolitar1962].

The analytic comparison belongs to a different literature. Periodic graph Ihara theory uses a specified finite trace and reduced primitive-cycle ledger [@GuidoIsolaLapidus2008]. Weighted infinite graphs with finite total weight admit Fredholm determinant formulas [@Deitmar2015]. These works motivate honest operator ownership, but they retain nonbacktracking relation cycles rather than fill presentation cells.

Three recent directions are especially close. Cayley-digraph path homology and covering digraphs connect directed path invariants to group homology [@DiEtAl2024]. The TR-trace packages iterated traces, characteristic polynomials, and Lefschetz zeta functions in homotopy theory [@CampbellEtAl2025]. A 2026 simple-cycle formula expresses finite-digraph Ihara zeta through a trace-monoid determinant [@Watanabe2026]. None of these primary sources makes an unequal presentation relation preserve the unit edge germ, nor identifies a completely filled Cayley quotient with the ordinary Fredholm determinant of its prequotient Hashimoto operator.

For the finite-trace control, Fuglede and Kadison supply the determinant in a finite factor [@FugledeKadison1952]. Determinant, entropy, and $L^2$-torsion identities for amenable groups are much deeper than the scalar Euler-multiplier control used here [@LiThom2014]; a torsion invariant is not thereby a primitive original-edge ledger.

The source-locked novelty statement is therefore only this: complete Cayley-cell cancellation for the frozen affine source is incompatible with both nonzero primitive recurrence and the original unit edge germ, while a trace-class prequotient Hashimoto operator still assigns a positive Fredholm trace coefficient to the affine relation polygon. Components are established theories, and no broad priority claim is made.

# Frozen affine object and path semantics {#sec:source}

## Positive source and formal reverses

For $r\ge2$, set $$M_r=\mathbb N_0\rtimes_r\mathbb N_0,
\qquad
(b,k)(d,\ell)=(b+r^kd,k+\ell),
\label{eq:affine-product}$$ with $u=(1,0)$ and $v=(0,1)$. Then $vu=u^rv$, every element has the unique normal form $u^bv^k$, and the right generators act by $$U(b,k)=(b+r^k,k),
\qquad
V(b,k)=(b,k+1).
\label{eq:right-actions}$$ The function $b+k$ strictly increases on positive edges, so the positive graph is acyclic.

Adjoin a distinct formal reverse to every positive edge and write $E_r^{\mathrm{or}}$ for the oriented-edge set. The Hashimoto transition is $$e\longrightarrow f
\quad\Longleftrightarrow\quad
t(e)=o(f),\qquad f\ne\bar e,
\label{eq:hashimoto}$$ with the same exclusion at the cyclic join. Every transition advances one original oriented edge and contributes one power of a free variable $z$. This explicit line-graph state change is not first return or acceleration.

At every $x\in M_r$, the word $$C_{r,x}=vu\bar v\bar u^r
\label{eq:relation-cycle}$$ is cyclically nonbacktracking. Its single positive $v$ occurrence excludes a proper temporal power, so it is primitive of length $L_r=r+3$.

## Cells, quotient, and whole operator

At every $x$, attach one $2$-cell comparing the positive paths $xvu$ and $xu^rv$; call the resulting Cayley complex $K_r$. We test both path homotopy and $$H_1(K_r)=\ker\partial_1/\operatorname{im}\partial_2.$$ Neither is silently identified with ordinary path multiplicity.

Fix $0<\theta<1$. If $o(e)=(b(e),k(e))$, define $$d_\theta(e)=\theta^{1+b(e)+k(e)},
\qquad
T_{r,\theta}=D_{\theta}H_rD_{\theta}
\label{eq:damped-operator}$$ on $\ell^2(E_r^{\mathrm{or}})$. The damping is source-derived, frozen uniformly in $r$, and applied unchanged to generic controls.

Any Fredholm determinant must belong to the full operator in [\[eq:damped-operator\]](#eq:damped-operator){reference-type="ref" reference="eq:damped-operator"} and must be compared as a free $z$-germ. Prime labels, factorization support, KMS/GNS or boundary projectors, first return, finite-quotient substitution, target coefficients, and Route B are forbidden.

# Affine Cayley-chain cancellation quadrilemma {#sec:theorem}

[\[thm:quadrilemma\]]{#thm:quadrilemma label="thm:quadrilemma"} Let $r\ge2$ and let all objects be exactly those of [3](#sec:source){reference-type="ref" reference="sec:source"}.

1.  **Complete cancellation is total.** The Cayley complex $K_r$ is contractible. Hence $$\pi_1(K_r)=0,
    \qquad
    H_j(K_r;\mathbb Z)=0\quad(j\ge1).
    \label{eq:contractible}$$ Every reduced closed edge word is null-homotopic after free and relation-cell cancellations; no primitive recurrent class survives.

2.  **The original clock does not descend.** Every cell-invariant additive degree into a torsion-free abelian group obeys $$(r-1)\deg(u)=0.
    \label{eq:marker-obstruction}$$ Thus $\deg(u)=0$, and the unit assignment $\deg(u)=\deg(v)=1$ is impossible.

3.  **The prequotient determinant sees the relation.** The operator $T_{r,\theta}$ is trace class. For sufficiently small $z$, $$-\log\det(I-zT_{r,\theta})
    =\sum_{n\ge1}\frac{z^n}{n}\mathop{\mathrm{Tr}}(T_{r,\theta}^n).
    \label{eq:fredholm-log}$$ Set $S_r=r(r+1)/2+2r+5$. Then the relation polygon gives $$\mathop{\mathrm{Tr}}(T_{r,\theta}^{r+3})\ge(r+3)\theta^{2S_r}>0.
    \label{eq:positive-trace}$$

4.  **The scalar graded repair is nonselective.** For a diagonal scalar lift $\widetilde A$ on the group-completed Cayley chain complex, $$\mathop{\mathrm{Str}}(\widetilde A^n)=(1-2+1)\tau(A^n)=0
    \quad(n\ge1),
    \label{eq:supertrace}$$ and $\mathop{\mathrm{SDet}}(I-z\widetilde A)=1$. The same formula holds for every two-generator one-relator presentation and retains no sector.

Therefore the frozen chain quotient cannot retain nonzero recurrence, preserve the unit marker, own the same prequotient determinant, and fail matched generic controls simultaneously.

[\[cor:finite\]]{#cor:finite label="cor:finite"} Let $q\ge2$ be coprime to $r$ and $t=\mathop{\mathrm{ord}}_q(r)$. In $\mathbb Z/q\mathbb Z\rtimes_r\mathbb Z/t\mathbb Z$, affine cells alone may leave first-homology classes generated by $u^q$ or $v^t$. Adding the complete finite-presentation cells kills those classes. Such residue does not descend from the infinite source.

[\[cor:balanced\]]{#cor:balanced label="cor:balanced"} For $r=1$, the relation $vu=uv$ has equal side lengths and the unit marker descends. Its filled square-grid Cayley complex is nevertheless contractible. Marker homogeneity is necessary for descent but insufficient for survival.

The four conclusions have different proof dependencies. Contractibility uses one-relator monoid topology; marker failure is an elementary degree calculation; Fredholm ownership uses source-coordinate summability; and the supertrace control uses only cell-orbit multiplicity. Their separation is part of the theorem rather than a presentation choice.

# Fill the relations, lose recurrence and clock {#sec:fill-clock}

## Why the fill is total

The affine realization in [\[eq:affine-product\]](#eq:affine-product){reference-type="ref" reference="eq:affine-product"} is injective. If $x=x^m$ for $m\ge2$ and $x=(b,k)$, then the second coordinate gives $k=mk$, hence $k=0$; the first gives $b=mb$, hence $b=0$. This verifies the torsion-free hypothesis relevant to the one-relator monoid theorem.

The words $vu$ and $u^rv$ share no nonempty prefix because their first letters differ, and no nonempty suffix because their last letters differ. The presentation is incompressible with empty compression word. The Gray--Steinberg contractibility theorem therefore specializes to the ordinary Cayley complex $K_r$ [@GraySteinberg2022], proving [\[eq:contractible\]](#eq:contractible){reference-type="ref" reference="eq:contractible"}.

The chain boundary makes the mechanism explicit. With the left $\mathbb ZM_r$-action and edge-orbit basis $e_u,e_v$, $$C_2\cong\mathbb ZM_r,
\qquad
C_1\cong(\mathbb ZM_r)e_u\oplus(\mathbb ZM_r)e_v,
\qquad
C_0\cong\mathbb ZM_r.$$ The first boundary is $\partial_1(e_u)=u-1$ and $\partial_1(e_v)=v-1$. Comparing the two relation paths gives $$\partial_2(1)=
\left(v-\sum_{j=0}^{r-1}u^j\right)e_u+(1-u^r)e_v.
\label{eq:cell-boundary}$$ Substitution yields $$\begin{aligned}
\partial_1\partial_2(1)
&=v(u-1)-\left(\sum_{j=0}^{r-1}u^j\right)(u-1)
 +(1-u^r)(v-1)\\
&=vu-u^rv=0.\end{aligned}$$ This is the presentation boundary familiar from Fox calculus [@Fox1953]. Contractibility, not this single boundary check alone, makes the augmented cellular sequence exact and proves total cancellation.

## Why the clock is lost

Let $\alpha=\deg(u)$ and $\beta=\deg(v)$ in a torsion-free abelian degree group. Cell invariance forces $$\beta+\alpha=r\alpha+\beta,
\qquad
(r-1)\alpha=0,$$ and hence $\alpha=0$. The original unit assignment cannot descend. In free-germ notation the same obstruction is $$z^2\ne z^{r+1}\qquad(r\ge2).$$ Specializing $z$, erasing the $u$ degree, or passing to a return map changes the clock and earns no same-marker credit.

isolates the two obstructions. At $r=1$ the relation is homogeneous, so the marker descends, but complete filling is still total. Conversely, leaving cells unfilled retains the relation polygon but does not perform the desired cancellation.

# The prequotient determinant still sees the relation {#sec:operator}

The formal symmetrization has vertex degree at most four. Each oriented edge has at most three nonbacktracking successors and predecessors, so the Schur test gives $$\|H_r\|\le3.
\label{eq:H-bound}$$ At most four oriented edges originate at a vertex. Hence $$\mathop{\mathrm{Tr}}(D_{\theta})
\le4\sum_{b,k\ge0}\theta^{1+b+k}
=\frac{4\theta}{(1-\theta)^2}<\infty.
\label{eq:D-trace}$$ Thus $D_{\theta}$ is trace class. The trace class is a two-sided ideal, so $T_{r,\theta}=D_{\theta}H_rD_{\theta}$ is trace class and owns the ordinary Fredholm expansion in [\[eq:fredholm-log\]](#eq:fredholm-log){reference-type="ref" reference="eq:fredholm-log"}. This is the weighted infinite-graph ownership regime, not a formal determinant assigned to a noncompact adjacency [@Deitmar2015].

Follow the relation polygon based at $(0,0)$: $$(0,0)\xrightarrow{v}(0,1)\xrightarrow{u}(r,1)
\xrightarrow{\bar v}(r,0)\xrightarrow{\bar u^r}(0,0).$$ The sum of $1+b+k$ over its oriented-edge origins is $$1+2+(r+2)+\sum_{j=1}^r(j+1)
=\frac{r(r+1)}2+2r+5=S_r.
\label{eq:cycle-exponent}$$ A closed cycle in $DHD$ has the square of the product of its diagonal edge weights. Its weight is therefore $\theta^{2S_r}$, and each of its $r+3$ cyclic starts supplies one diagonal term. All entries are nonnegative, which proves [\[eq:positive-trace\]](#eq:positive-trace){reference-type="ref" reference="eq:positive-trace"}.

For the composite baseline $r=4$ and $\theta=1/2$, $$S_4=23,
\qquad
\theta^{2S_4}=2^{-46}
=\frac{1}{70368744177664},
\qquad
\mathop{\mathrm{Tr}}(T_{4,1/2}^7)\ge7\cdot2^{-46}>0.$$ Immediate backtracks have already been forbidden. The surviving coefficient is the affine relation recurrence that the cell quotient removes.

#### Finite-trace group control.

The enveloping group $$G_r=\mathbb Z[1/r]\rtimes_r\mathbb Z
=\langle u,v\mid vuv^{-1}=u^r\rangle$$ belongs to the Baumslag--Solitar family [@BaumslagSolitar1962]. With $$A_r=\tfrac14(\lambda_u+\lambda_{u^{-1}}+
\lambda_v+\lambda_{v^{-1}})$$ and the canonical group von Neumann trace $\tau$, one has $$\tau(A_r^n)=\frac{c_r(n)}{4^n},
\label{eq:group-count}$$ where $c_r(n)$ counts identity words. For real $|z|<1$, $$\log\Delta_r(z)
=-\sum_{n\ge1}\frac{c_r(n)}{n4^n}z^n
\label{eq:FK-log}$$ is a Fuglede--Kadison determinant logarithm [@FugledeKadison1952]. This honest finite-trace control also counts the relator; it is not called the ordinary Fredholm determinant above and is not substituted for the semigroup source.

# Exact supercancellation is generically empty {#sec:superdet}

Over the group completion, use the cellular chains as right group-ring modules. The Fox boundary acts on the right, while left convolution by a finite-trace operator $A$ commutes with it. Lift $A$ diagonally to one copy on $C_0$, two copies on $C_1$, and one copy on $C_2$, with even parity on $C_0\oplus C_2$ and odd parity on $C_1$. Then, for every $n\ge1$, $$\mathop{\mathrm{Str}}(\widetilde A^n)
=\tau(A^n)-2\tau(A^n)+\tau(A^n)=0.$$ Exponentiating the connected supertrace gives $$\mathop{\mathrm{SDet}}(I-z\widetilde A)=1.$$

This is an all-orders result, not first-trace evidence. It is nevertheless a negative control: the relator word never enters. Any two-generator one-relator presentation has the same cell-orbit multiplicities $(1,2,1)$, so affine, balanced, exponent-mutated, and arbitrary relators all receive the same empty answer. The cancellation removes open algebraic content and closed recurrence together.

This firewall is consistent with, but much weaker than, determinant and $L^2$-torsion identities for amenable groups [@LiThom2014]. We do not identify a torsion invariant with an original-edge primitive ledger. Nor do we infer that a matrix-valued, non-flat local coefficient system must share the scalar failure; such a system would be a new candidate with new all-orders and generic-control obligations.

Three objects must therefore remain distinct:

1.  path homotopy and cellular homology after filling $K_r$;

2.  ordinary Hilbert-space traces of the trace-class operator $T_{r,\theta}$;

3.  finite-factor traces and chain supertraces used as analytic controls.

No equality of notation or scalar specialization identifies their ledgers.

# Exact audit and adversarial controls {#sec:audit}

The exact prototype tests finite witnesses and implementation identities; it does not numerically approximate the infinite Fredholm determinant. The source module constructs affine normal forms, words, relation data, and finite semidirect actions. The independent evaluator separately reconstructs rational ranks, boundary-square identities, trace coefficients, marker verdicts, and graded controls.

\@r r r r Y@ $r$ & $L_r$ & first excess & excess count & one relation-cycle weight at $\theta=1/2$\
& 5 & 5 & 10 & $2^{-24}$\
3 & 6 & 6 & 12 & $2^{-34}$\
4 & 7 & 7 & 14 & $2^{-46}$\
5 & 8 & 8 & 32 & $2^{-60}$\

The composite baseline $r=4$ has first excess $14$ at length seven. The balanced $r=1$ control has equal relation-side lengths and a descending unit marker, yet complete filling still removes first homology.

::: {#tab:finite-audit}
  relation     $(q,t)$   vertices   cycle dim.   affine $H_1$   complete $H_1$
  ---------- --------- ---------- ------------ -------------- ----------------
  $r=1$        $(4,3)$         12           13              2                0
  $r=2$        $(3,2)$          6            7              1                0
  $r=3$        $(4,2)$          8            9              1                0
  $r=4$        $(5,2)$         10           11              1                0
  $r=4$        $(7,3)$         21           22              1                0
  $r=5$        $(6,2)$         12           13              1                0

  : Finite semidirect controls. Affine-only cells leave quotient-created generators; complete finite-presentation cells kill them.
:::

All twelve affine/full boundary-square checks pass, and all 48 sampled chain-lift powers have zero supertrace. The source and prototype semantic layers each pass 33/33 checks; independent authority integration passes 35/35, and the authority suite passes 53/53 tests. Fresh A/B and cache-free cold C reproduce all 19 scientific payloads and six stage stdout streams byte-for-byte. The authority scientific aggregate is `58a5d3b404d85163edfe74bea45b077da07ac6ff4f0794aff0bf9f1fbcf6ea9e`. The final set has 27 result files; all 74 integrity checks and all 43 immutable code/result ledger entries pass.

The mutable Route card is schema-audited separately and excluded from that Stage-1 ledger so that its three provenance fields can be sealed metadata-only.

The finite data corroborate the relation length, marker mismatch, quotient boundary, and generic multiplier. Contractibility, marker non-descent, trace-class ownership, and the all-orders scalar identity are proved independently in [\[sec:fill-clock,sec:operator,sec:superdet\]](#sec:fill-clock,sec:operator,sec:superdet){reference-type="ref" reference="sec:fill-clock,sec:operator,sec:superdet"}.

# Route decision and conclusion {#sec:conclusion}

The affine exponent is structural, but every downstream obligation fails for an exact and separately owned reason.

\@L0.14L0.19Y@ Gate & Status & Reason\
A0 & structural origin & $r$ occurs in the source relation $vu=u^rv$; no prime oracle defines it\
A1 & fail & complete Cayley-cell filling is contractible and retains no recurrent class\
A2 & fail & the cell equates lengths $2$ and $r+1$, so the unit marker does not descend\
A3 & fail & the honestly owned prequotient Fredholm trace sees a positive relation coefficient while the quotient ledger is empty\
A4 & fail & the scalar chain lift cancels every two-generator one-relator presentation and recognizes nothing\

The strict repository tuple is $$\texttt{(A0\_STRUCTURAL\_ARITHMETIC\_RELATION, A1\_FAIL,
A2\_FAIL, A3\_FAIL, A4\_FAIL)}.$$ The overall decision is `ROUTE_A_REJECTED`; Route B is not invoked. The branch conclusion is $$\boxed{\texttt{CLOSE\_COMPLETE\_AFFINE\_CHAIN\_QUOTIENT\_BRANCH}.}$$

The result is not that every homological or matrix construction fails. It is that the complete presentation quotient is simultaneously empty, clock incompatible, and analytically different from the prequotient determinant. The simplest superdeterminant removes the discrepancy only by removing every coefficient for generic presentations.

The smallest eligible continuation must keep the unquotiented same-marker Hashimoto object and freeze a source-derived non-flat finite-rank coefficient system. It must cancel every translate, conjugate, mixed relation class, and repetition at all orders; retain one independently proved nonnilpotent primitive arithmetic factor; own one matrix Fredholm trace-log on the same space; and fail matched generic relators. A complete quotient, $\deg(u)=0$, $z=1$, first return, KMS/GNS or boundary support, a Fock or prime basis, and a scalar character remain ineligible substitutions.

No xi completion, functional equation, critical-line divisor, Weil form, target-zero computation, or RH implication appears in the argument.

# Proof details and boundary calculations {#app:proofs}

## Primitivity of the relation polygon

The word $vu\bar v\bar u^r$ is freely reduced: its adjacent generator types are distinct, and the cyclic join from $\bar u$ to $v$ is not an inverse pair. It is therefore cyclically nonbacktracking. If it were a $d$-fold temporal power for $d\ge2$, every oriented-letter count would be divisible by $d$. The word contains exactly one positive $v$, a contradiction. Translation by any $x\in M_r$ preserves these properties.

## Exact chain line

The path-chain of $vu$ is $e_v+ve_u$. The path-chain of $u^rv$ is $$\sum_{j=0}^{r-1}u^je_u+u^re_v.$$ Their difference is [\[eq:cell-boundary\]](#eq:cell-boundary){reference-type="ref" reference="eq:cell-boundary"}. Since $K_r$ is contractible, the augmented cellular sequence $$0\longrightarrow\mathbb ZM_r\xrightarrow{\partial_2}(\mathbb ZM_r)^2
\xrightarrow{\partial_1}\mathbb ZM_r\longrightarrow\mathbb Z\longrightarrow0$$ is exact. Thus every cellular one-cycle is a relation boundary. Simple connectivity separately gives the path-homotopy statement for every reduced closed word.

## Damping exponent

On the based polygon, the oriented-edge origins are $$(0,0),\ (0,1),\ (r,1),\ (r,0),(r-1,0),\ldots,(1,0).$$ Their $1+b+k$ values are $$1,\ 2,\ r+2,\ r+1,r,\ldots,2.$$ The sum is [\[eq:cycle-exponent\]](#eq:cycle-exponent){reference-type="ref" reference="eq:cycle-exponent"}. In a product $DHD\cdots DHD$, every visited oriented-edge state receives one diagonal factor from the left and one from the right. Hence a closed cycle has the square of the product of its $D$-weights. This supplies the exponent $2S_r$ in [\[eq:positive-trace\]](#eq:positive-trace){reference-type="ref" reference="eq:positive-trace"}.

## Finite quotient interpretation

For $q$ coprime to $r$, multiplication by $r$ is an automorphism of $\mathbb Z/q\mathbb Z$ and has order $t$. The quotient adds the closed words $u^q$ and $v^t$. Filling only the affine cell cannot make these new presentation relations into boundaries in general. Adding their cell orbits completes the finite presentation; the exact rank audit in [1](#tab:finite-audit){reference-type="ref" reference="tab:finite-audit"} then gives $H_1=0$. This explains the finite residue without promoting it to an infinite-source class.

## All-orders superdeterminant

For trace-class or finite-trace blocks, define the connected graded logarithm by $$-\log\mathop{\mathrm{SDet}}(I-z\widetilde A)
=\sum_{n\ge1}\frac{z^n}{n}\mathop{\mathrm{Str}}(\widetilde A^n).$$ Equation [\[eq:supertrace\]](#eq:supertrace){reference-type="eqref" reference="eq:supertrace"} makes every coefficient zero, so the germ is identically one. This conclusion uses no property of the affine relation word and is therefore a generic-control failure, not evidence of selective relation removal.

# Scope declarations and ownership ledger {#app:scope}

\@Y L0.17L0.18Y@ Object & marker & trace framework & Frozen output\
positive Cayley graph & unit edge & none needed & acyclic; no closed positive path\
formal reverse/Hashimoto shift & unit edge & path ledger & primitive affine relation polygons\
$T_{r,\theta}$ on $\ell^2(E_r^{\mathrm{or}})$ & unit edge & Hilbert trace; trace class & positive ordinary Fredholm relation coefficient\
filled $K_r$ & marker fails & path homotopy/cellular homology & contractible; no recurrent class\
group operator $A_r$ & group word & canonical finite-factor trace & identity-word determinant control\
scalar chain superlift & inherited formal $z$ & supertrace & determinant one for every matched one-relator control\
finite semidirect blocks & quotient edge & finite matrices & quotient-created residue until all relations are filled\

The no-go applies only to the complete source-derived Cayley-cell mechanism frozen here. It does not rule out a non-flat finite-rank coefficient system, a matrix or derived edge operator, a groupoid with explicitly stated trace, or another uninduced symbolic construction. Each new proposal must freeze its path space, marker, coefficient rule, trace, and complete primitive ledger before labels.

Five substitutions receive no credit. First, a cell quotient is not an operator compression unless an intertwining theorem is proved. Second, a finite-factor determinant is not an ordinary Fredholm determinant. Third, equality after $z=1$ is not equality of free marker germs. Fourth, residual finite-quotient cycles are not infinite-source classes. Fifth, a superdeterminant equal to one is not arithmetic recognition when the same formula holds for arbitrary relators.

No peer-review or LLM review loop was run, following the project instruction. The mathematical proof, primary-source search, exact audit, compilation, typography, and provenance checks are separate deterministic evidence layers.
