---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--18-incidence-transition-holonomy"
canonical_tex: "symbolic_dynamics/papers/18-incidence-transition-holonomy/main.tex"
canonical_pdf: "symbolic_dynamics/papers/18-incidence-transition-holonomy/main.pdf"
source_sha256: "ab9fb83e81e0e116b5195fd6eff52f23070a5c5fea14ef5da6b6f9ce186e482d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Transition Holonomy on the Tensor-Subset Shift: Noncommutative Artin Blocks and an Arithmetic Selectivity No-Go

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/18-incidence-transition-holonomy>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/18-incidence-transition-holonomy/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/18-incidence-transition-holonomy/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/18-incidence-transition-holonomy/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/18-incidence-transition-holonomy/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test whether a transition-dependent finite-group cocycle can repair the arithmetic overproduction of the tensor-subset full shift. Relabeling naturality and restriction compatibility classify every source-locked local rule by the three incidence counts $(|S\setminus T|,|S\cap T|,|T\setminus S|)$; this leaves $\binom{n+3}{3}-(2n+1)$ types on $n$ atoms. We then assign $r=(12)$ to strict refinements, $t=(23)$ to strict coarsenings, and the identity otherwise. The resulting $S_3$ extension is a genuine deck symmetry of the same two-block symbolic object and is not cohomologous to a one-letter cardinality clock. Its two-atom trivial and sign determinants are both $(1-x)(1-y)$, whereas its standard block is exactly $$(1-x)^2(1-y)^2+3xy(x+y)(xy+1)(x+y-1).$$ The relative trace logarithm leaks at $x^2y,xy^2,x^2y^2$ with coefficients $-3,-3,-6$. A primitive four-edge word has commutator holonomy $(rt)^2$ and an edge-separated standard-character gap of three, so the nonabelian signal cannot be dismissed as a coboundary or an unmarked-orbit cancellation. Exhaustive two-atom searches in $S_3,D_4,Q_8$ found that every all-irrep-clean table belongs to the counting-gauge class; this is finite evidence, not a general theorem. The infinite nontrivial block is trace class for $\operatorname{Re}s>2$, while the trivial block is already defined for $\operatorname{Re}s>1$. Thus transition holonomy is dynamically genuine but inventory-blind: it preserves the scalar Euler factor yet cannot select prime or prime-power primitives. The strict outcome is `ROUTE_A_REJECTED`; no claim about Riemann zeros is made.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Transition Holonomy on the Tensor-Subset Shift:\
  Noncommutative Artin Blocks and an Arithmetic Selectivity No-Go
```

## Markdown 正文

# Introduction {#sec:introduction}

Finite-group extensions sharpen periodic-orbit information: a closed word now carries both a scalar weight and a conjugacy class of holonomy. This observation makes them a natural test for a persistent defect in exploratory arithmetic symbolic dynamics. The tensor-subset shift produces the exact finite inclusion--exclusion factor $\prod_{p\in P}(1-x_p)$, but its full primitive language also contains mixed subset words that have no prime or prime-power interpretation. A one-letter parity fiber gives a genuine Artin factor, yet only clocks total cardinality. The remaining in-family loophole is transition holonomy: let the group label depend intrinsically on how one subset changes into the next.

This paper closes that loophole for one explicit and deliberately strong candidate. We keep the same full shift, the same tensor-derived atom weights, and the same roof function. We merely use the two-block presentation and put a finite-group cocycle on its directed edges. Strict refinements receive one transposition of $S_3$ and strict coarsenings a noncommuting transposition. The construction therefore distinguishes merge order without reading atom names or numerical prime data.

The result has a positive and a negative half. Positively, the extension is genuinely nonabelian and not a cardinality cocycle plus a coboundary. Its regular determinant decomposes into character blocks on one symbolic object, and a primitive four-edge word records a nontrivial commutator. Negatively, the standard two-dimensional block sees mixed atom products at the first available degrees. The noncommutative detector does not cancel the unwanted primitives; it certifies them.

Our main contributions are the following.

1.  We classify relabeling-natural, restriction-compatible local edge data by the incidence triple $(u,v,w)$ and count the stable types exactly.

2.  We identify the natural gauge orbit of a one-letter counting cocycle and prove its atom-local character determinant.

3.  We give an explicit $S_3$ cocycle outside that orbit and prove noncohomology using closed-word holonomy.

4.  We compute all two-atom irreducible blocks. The standard determinant has an exact factored correction and mixed trace-log coefficients $-3,-3,-6$.

5.  We isolate a primitive commutator contribution with directed-edge markers and prove the general character-separation lemma needed to prevent an aggregation error.

6.  We state the precise Fredholm half-plane and report finite exhaustive evidence without converting it into a universal rigidity theorem.

The logical outcome is summarized in [\[fig:no-go\]](#fig:no-go){reference-type="ref" reference="fig:no-go"}. Clean one-dimensional blocks coexist with a leaking nonabelian block; checking only abelian characters would therefore give a false positive.

The paper stays within Symbolic Dynamics. Gain and voltage terminology is used only for a finite edge presentation of the shift. We do not introduce a geometric carrier or a self-adjoint operator, and we make no RH claim.

#### Organization.

places the mechanism against the classical literature. freezes the symbolic object and determinant. treats naturality and gauge. fixes primitive bookkeeping. gives the exact $S_3$ certificate. separate finite evidence from the analytic limit. applies the strict route evaluation, and the appendices contain proofs and the scope ledger.

# Classical boundary and closest collisions {#sec:boundary}

For a finite-state shift, the determinant representation of the zeta function is classical [@BowenLanford1970ShiftZeta]. Periodic orbit weights twisted by representations, and the ensuing Artin-type factorizations, likewise belong to established thermodynamic formalism [@AdachiSunada1987TwistedPF; @ParryPollicott1990Zeta; @Pollicott1994TwistedOrbits]. Finite-group extensions of shifts of finite type and their equivalence problems have been studied at substantially greater generality than is needed here [@BoyleSchmieding2017FiniteExtensions].

The correct invariant for a group cocycle is periodic holonomy, not an individual edge label. Livšic theory relates periodic data to cohomology under regularity and hyperbolicity hypotheses [@Livsic1972Cohomology; @ParryPollicott1997Livsic; @Kalinin2011MatrixLivsic]. On a finite edge presentation, changing vertex coordinates is also the standard switching operation of voltage or gain descriptions [@GrossTucker1977Voltage; @Zaslavsky1989Gain]. We use these languages as finite combinatorial coordinates for the same edge shift, not as a second dynamical family.

Graph-covering zeta functions provide another close model for regular and irreducible factorization [@StarkTerras1996GraphCoverings; @StarkTerras2000GraphCoveringsII]. This collision fixes an important novelty boundary: the block decomposition in [\[prop:artin\]](#prop:artin){reference-type="ref" reference="prop:artin"} is machinery, not the claimed discovery. The model-specific content lies in the tensor-subset incidence grammar, the exact $S_3$ block, and its arithmetic failure.

There is also a negative literature boundary. Spectral or zeta data need not determine a switching class; modern gain-graph constructions make this failure particularly concrete [@CavaleriDonno2022Cospectral; @AbiadBelardoKhramova2024Gain; @CavaleriDonnoSpessato2025Gain]. Accordingly, we never infer cohomology from equality of unmarked character determinants. Our exhaustive finite tables support only the explicitly bounded conjecture stated in [7](#sec:evidence){reference-type="ref" reference="sec:evidence"}.

Finally, the infinite determinant is subject to the usual trace-class requirements [@Simon1977InfiniteDeterminants]. A finite symbolic identity is not silently promoted to the critical strip. The exact domain we can justify appears in [8](#sec:fredholm){reference-type="ref" reference="sec:fredholm"}.

The classical ingredients are finite-state determinant identities, finite-group Fourier decomposition, switching, and periodic-data cohomology. The new object-level result is that the source-locked incidence rule realizes noncommutative holonomy but necessarily exhibits explicit mixed leakage in its standard block. We do not claim a general classification of finite-group edge cocycles.

# The frozen tensor-subset edge shift {#sec:frozen}

Let $P$ be a finite nonempty set of tensor atoms and put $$\mathcal E_P=2^P\setminus\{\varnothing\},\qquad X_P=\mathcal E_P^{\mathbb Z}.$$ The left shift on $X_P$ is full. Independent commuting variables $(x_p)_{p\in P}$ determine $$x_S=\prod_{p\in S}x_p,\qquad
 \varepsilon(S)=(-1)^{|S|+1},\qquad w(S)=\varepsilon(S)x_S.$$ For the arithmetic specialization, $x_p=p^{-s}$ and $T(S)=\sum_{p\in S}\log p$, so that $x_S=e^{-sT(S)}$. All algebraic claims are proved before this substitution.

We use the two-block presentation of the same full shift: the vertices are $\mathcal E_P$ and every ordered pair $(S,T)$ is an edge. Fix a finite group $G$ and an edge cocycle $\alpha_P:\mathcal E_P^2\to G$. Our convention is $$\widetilde\sigma_\alpha(x,g)
   =(\sigma x,g\alpha_P(x_0,x_1)).
 \tag{3.1}\label{3.1}$$ Left fiber translations commute with [\[3.1\]](#3.1){reference-type="eqref" reference="3.1"}; they do not change atom labels, weights, or roofs. The group fiber is therefore a genuine deck symmetry, not a post-processing of unrelated determinants.

For an irreducible unitary representation $\rho:G\to U(V_\rho)$, $d_\rho=\dim V_\rho$, define the arrival matrix $$B_{\rho,P}(S,T)=w(T)\rho(\alpha_P(S,T)),\qquad
 D_{\rho,P}=\det(I-B_{\rho,P}).
 \tag{3.2}\label{3.2}$$

[\[prop:artin\]]{#prop:artin label="prop:artin"} For the right regular representation, $$D_{\mathrm{reg},P}=\prod_{\rho\in\widehat G}D_{\rho,P}^{d_\rho}.
 \tag{3.3}\label{3.3}$$ The trivial block is independent of $\alpha_P$ and satisfies $$D_{\mathbf 1,P}=\prod_{p\in P}(1-x_p).
 \tag{3.4}\label{3.4}$$

The proof in [11.1](#app:artin-proof){reference-type="ref" reference="app:artin-proof"} is only finite-dimensional Fourier decomposition plus inclusion--exclusion. Equation [\[3.4\]](#3.4){reference-type="eqref" reference="3.4"} is the exact scalar Euler factor at finite cutoff. It does not say that the remaining primitive language has selected arithmetic atoms.

## Gauge and based holonomy

A vertex map $b_P:\mathcal E_P\to G$ acts by $$\alpha_P^b(S,T)=b_P(S)^{-1}\alpha_P(S,T)b_P(T).
 \tag{3.5}\label{3.5}$$ For a closed directed word $\gamma=(S_0,\ldots,S_{n-1},S_0)$, define $$H_\alpha(\gamma)=\prod_{j=0}^{n-1}\alpha(S_j,S_{j+1}).
 \tag{3.6}\label{3.6}$$

[\[prop:gauge\]]{#prop:gauge label="prop:gauge"} Every $D_{\rho,P}$ is invariant under [\[3.5\]](#3.5){reference-type="eqref" reference="3.5"}, and $H_\alpha(\gamma)$ changes by conjugation with $b_P(S_0)$. On the finite connected presentation, two cocycles are gauge equivalent exactly when a spanning-tree recursion satisfies all non-tree edges, equivalently when all fundamental based holonomies agree through one simultaneous root conjugator.

Character determinants aggregate closed words. gives a test for gauge equivalence, but its converse is not replaced by a claim that equal determinants classify gauges.

# Functorial incidence grammar and the counting gauge class {#sec:incidence}

The target group carries no action of the atom relabeling group. We require one-step locality, naturality under bijections of atom sets, and compatibility with restriction to a smaller inventory. For an ordered pair $(S,T)$ write $$u=|S\setminus T|,\qquad v=|S\cap T|,\qquad w=|T\setminus S|.
 \tag{4.1}\label{4.1}$$

[\[thm:incidence\]]{#thm:incidence label="thm:incidence"} Every source-locked local cocycle has the form $$\alpha_P(S,T)=g_{u,v,w}.
 \tag{4.2}\label{4.2}$$ On an inventory of size $n$, the number of stable incidence types is $$N(n)=\binom{n+3}{3}-(2n+1),
 \qquad N(1),N(2),N(3),N(4)=1,5,13,26.
 \tag{4.3}\label{4.3}$$ Conversely, a stable table on these triples defines such a natural local rule.

The three counts in [\[4.1\]](#4.1){reference-type="eqref" reference="4.1"} preserve more information than the arrival cardinality $|T|=v+w$. Thus naturality does not collapse transition cocycles to one-letter clocks.

To identify the clocks that are present, take $a\in G$ and define $$\alpha_a(S,T)=a^{|T|}.
 \tag{4.4}\label{4.4}$$ A natural vertex gauge is constant on cardinality orbits, so write $b_P(S)=q_{|S|}$.

[\[thm:count-gauge\]]{#thm:count-gauge label="thm:count-gauge"} The natural gauge orbit of [\[4.4\]](#4.4){reference-type="eqref" reference="4.4"} is exactly $$g_{u,v,w}=q_{u+v}^{-1}a^{v+w}q_{v+w}.
 \tag{4.5}\label{4.5}$$ Every member of this orbit has $$D_{\rho,P}=\prod_{p\in P}\det(I-x_p\rho(a)).
 \tag{4.6}\label{4.6}$$ For two atoms, denote the five values by $(a_0,c,h,u_0,v_0)$: singleton loop, pair loop, disjoint-singleton edge, refinement, and coarsening. After $q_1=e$, membership in [\[4.5\]](#4.5){reference-type="eqref" reference="4.5"} is equivalent to $$h=a_0,\qquad v_0=u_0^{-1}a_0^3,\qquad
 c=u_0^{-1}a_0^2u_0.
 \tag{4.7}\label{4.7}$$

Equation [\[4.6\]](#4.6){reference-type="eqref" reference="4.6"} is the clean benchmark: every irreducible block factors atom by atom. The central question is whether a cocycle outside [\[4.5\]](#4.5){reference-type="eqref" reference="4.5"} can remain comparably clean while carrying noncommuting holonomy. The answer for our frozen candidate is no.

# Primitive convention and character-separated leakage {#sec:primitive}

Primitive closed words are quotiented by cyclic rotation, never by reflection. For a primitive class $[\gamma]$ set $$w(\gamma)=\prod_j w(S_{j+1}),\qquad
 H_\alpha(\gamma)=\prod_j\alpha(S_j,S_{j+1}).$$ Formally, $$D_{\rho,P}
 =\prod_{[\gamma]\ \mathrm{primitive}}
   \det\!\left(I-w(\gamma)\rho(H_\alpha(\gamma))\right).
 \tag{5.1}\label{5.1}$$ The $m$-fold traversal uses both $w(\gamma)^m$ and $H_\alpha(\gamma)^m$. Koszul signs stay ordinary scalar coefficients; no supertrace is introduced.

An unmarked monomial such as $x^3y^3$ generally aggregates many primitive words and temporal repetitions. To isolate a particular cycle, attach a commuting marker $z_{S,T}$ to each directed edge. This works when the edge multiset has a unique connected cyclic traversal; otherwise a finer cyclic-word marker is required.

[\[thm:separated-leak\]]{#thm:separated-leak label="thm:separated-leak"} Let $\gamma$ be a primitive directed cycle isolated by such a marker. If $H_\alpha(\gamma)$ is not conjugate to the reference holonomy $H_0(\gamma)$, then some irreducible block has a different first-traversal coefficient. If $H_0(\gamma)=e$ and $H_\alpha(\gamma)\ne e$, then $$\chi_\rho(H_\alpha(\gamma))\ne d_\rho
 \tag{5.2}\label{5.2}$$ for at least one irreducible $\rho$.

Indeed, the trace-log identity $$\log\det(I-B_\rho)
 =-\sum_{n\ge1}\frac{\operatorname{tr}(B_\rho^n)}n
 \tag{5.3}\label{5.3}$$ assigns the isolated first traversal the coefficient $-\chi_\rho(H_\alpha(\gamma))w(\gamma)z_\gamma$. Irreducible characters separate conjugacy classes. The full proof, including the identity-reference case, is in [11.4](#app:leak-proof){reference-type="ref" reference="app:leak-proof"}.

is deliberately one-way. It does not assert that unmarked character determinants classify cocycles, and it does not prevent collisions among aggregated orbit data.

# The frozen $S_3$ transition certificate {#sec:s3}

Let $G=S_3$, $r=(12)$, and $t=(23)$. Freeze the intrinsic rule $$\alpha(S,T)=
\begin{cases}
r,&S\subsetneq T,\\
t,&T\subsetneq S,\\
e,&\text{otherwise}.
\end{cases}
\tag{6.1}\label{6.1}$$ It depends only on the incidence triple: refinement means $(u,w)=(0,>0)$ and coarsening means $(u,w)=(>0,0)$.

[\[prop:not-clock\]]{#prop:not-clock label="prop:not-clock"} The cocycle [\[6.1\]](#6.1){reference-type="eqref" reference="6.1"} is not gauge equivalent, even by an arbitrary two-atom vertex gauge, to any reference $a^{|T|}$.

The singleton loop $p\to p$ forces $a=e$. But the closed two-step word $p\to pq\to p$ has holonomy $rt\ne e$, contradicting gauge invariance of closed-word conjugacy classes. This proof also shows that the escape from the one-letter classification is not merely a failure of natural gauge.

There are explicitly noncommuting based holonomies once three atoms are present. At the vertex $p$, the two-cycle $p\to\{p,q\}\to p$ gives $rt$, whereas $p\to\{p,q\}\to\{p,q,\ell\}\to p$ gives $rrt=t$. Since $rt$ and $t$ do not commute, the holonomy image is not cyclic. A complementary merge-order witness is the four-cycle $$\gamma_\square=[p,pq,q,pq]
\tag{6.2}\label{6.2}$$ has $$H(\gamma_\square)=rtrt=(rt)^2=[r,t]\ne e.
\tag{6.3}\label{6.3}$$ It is primitive and its scalar weight is $x^3y^3$.

## Exact irreducible blocks

Order the states as $(p,q,pq)$, with arrival weights $(x,y,-xy)$. The one-dimensional blocks satisfy $$D_{\mathbf 1}(x,y)=D_{\mathrm{sgn}}(x,y)=(1-x)(1-y).
 \tag{6.4}\label{6.4}$$ The sign character therefore misses the obstruction completely.

Use the exact standard matrices $$R=\begin{pmatrix}-1&1\\0&1\end{pmatrix},\qquad
 T=\begin{pmatrix}1&0\\1&-1\end{pmatrix}.
 \tag{6.5}\label{6.5}$$ They satisfy $R^2=T^2=I$ and $(RT)^3=I$.

[\[thm:standard-block\]]{#thm:standard-block label="thm:standard-block"} For [\[6.1\]](#6.1){reference-type="eqref" reference="6.1"}, $$\boxed{
D_{\mathrm{std}}(x,y)
=(1-x)^2(1-y)^2
+3xy(x+y)(xy+1)(x+y-1).}
\tag{6.6}\label{6.6}$$ Relative to the identity/counting reference, $$[x^2y],\Delta\log D=-3,\qquad
[xy^2],\Delta\log D=-3,\qquad
[x^2y^2],\Delta\log D=-6.
\tag{6.7}\label{6.7}$$

Thus leakage starts at squarefree support on both atoms, with temporal multiplicity. The term $x^2y^2$ is the requested degree-four audit. These coefficients are formal and exact; no numerical fitting is involved. For a complete total-degree-four ledger, one also has $[x^3y]\Delta\log D=[xy^3]\Delta\log D=-3$.

For the cycle [\[6.2\]](#6.2){reference-type="eqref" reference="6.2"}, the four directed edges have a unique connected cyclic traversal. The other pairing splits into two disconnected two-cycles. Since the standard character is $-1$ on a nonidentity three-cycle and $2$ at the identity, [\[thm:separated-leak\]](#thm:separated-leak){reference-type="ref" reference="thm:separated-leak"} gives an edge-marked character gap of magnitude $$|{-1}-2|=3.
\tag{6.8}\label{6.8}$$ The unmarked value $[x^3y^3]\Delta\log D=-9$ remains an aggregate and is not identified with [\[6.8\]](#6.8){reference-type="eqref" reference="6.8"}.

[\[cor:noncomm-no-go\]]{#cor:noncomm-no-go label="cor:noncomm-no-go"} The frozen cocycle has genuine transition holonomy but no clean nonabelian Artin block. Its first faithful irreducible detector exposes mixed subset primitives rather than suppressing them.

# Finite exhaustive evidence and controls {#sec:evidence}

For two atoms, every natural local rule is a five-tuple $(a_0,c,h,u_0,v_0)\in G^5$. Exact enumeration compared every irreducible determinant with the atom-local counting benchmark and independently applied the gauge conditions [\[4.7\]](#4.7){reference-type="eqref" reference="4.7"}. The completed counts are:

::: {#tab:enumeration}
  group         all tables        weak clean   all-irrep clean   gauge/count   nongauge clean
  ------- ---------------- ----------------- ----------------- ------------- ----------------
  $S_3$      $6^5=7{,}776$       sign: $972$              $36$          $36$              $0$
  $D_4$     $8^5=32{,}768$      not promoted              $64$          $64$              $0$
  $Q_8$     $8^5=32{,}768$   all $1$D: $512$              $64$          $64$              $0$

  : Exact two-atom enumeration. "All-irrep clean" means equality with the count-reference determinant in every irreducible representation under the frozen comparison. These are finite data, not a theorem for arbitrary groups or presentations.
:::

The cutoff is exact and explicit: all of $G^5$ was visited for each displayed group. We used $D_4=\langle a,b\mid a^4=b^2=e,\,bab=a^{-1}\rangle$ and $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$. Modular grids were only screening devices; every survivor was recertified by exact symbolic coefficients and the spanning-tree gauge test. No random seed enters this exhaustive result. The pre-registered cutoff for any higher-inventory search is squarefree atom support through four atoms and temporal exponents through four; no universal claim is attached to that cutoff. The decisive two-atom comparison uses the full determinant rather than a truncation. The explicit three-atom words in [6](#sec:s3){reference-type="ref" reference="sec:s3"} supply the merge-order/noncommutativity control.

The contrast inside the table matters. In $S_3$, $972$ tables look clean to the sign character, but only $36$ survive the standard representation; all $36$ are in the gauge/count class. In $Q_8$, even all one-dimensional characters leave $512$ candidates, whereas the two-dimensional block reduces the number to $64$. Abelian audits are therefore structurally insufficient.

For a finite group $G$ and the five-type two-atom incidence grammar, equality with the one-letter counting determinant in every irreducible representation forces the gauge conditions [\[4.7\]](#4.7){reference-type="eqref" reference="4.7"}.

We do not prove this conjecture. Known cospectral and zeta-equivalent gain assignments make a general "determinant implies switching" principle unsafe [@CavaleriDonno2022Cospectral; @AbiadBelardoKhramova2024Gain; @CavaleriDonnoSpessato2025Gain].

## Matched-inventory controls

The construction is defined over independent formal variables. Its local rule tests only subset incidence. Consequently, each of the following matched controls reproduces the same symbolic identities after substitution:

-   replace primes by composites with the same number of atom labels;

-   randomly shuffle numerical values among atom labels;

-   use algebraically independent formal variables;

-   use random positive or rational weights;

-   preserve the subset grammar while changing the arithmetic inventory.

Every substitution is a homomorphism from the free commutative polynomial ring. Therefore the clean trivial factor, the standard leakage, and the commutator certificate all survive with zero symbolic control margin. This is the precise meaning of `PROVES_TOO_MUCH`: the mechanism does not distinguish primes from matched nonprime inventories.

No zero data enter the construction or the controls. There is no fitted phase, selected truncation, or prime-indexed group element.

# Fredholm realization and its honest boundary {#sec:fredholm}

Let $\mathcal E_\infty$ be the set of all nonempty finite subsets of the primes. Pick $\eta_S^2=\varepsilon(S)$ and set $$q_S(s)=\eta_S e^{-sT(S)/2},\qquad
 K_\rho(s)_{S,T}=q_S(s)\rho(\alpha(S,T))q_T(s)
 \tag{8.1}\label{8.1}$$ on $\ell^2(\mathcal E_\infty)\otimes V_\rho$. For finite $P$, Sylvester's identity gives $$\det(I-K_{\rho,P}(s))=D_{\rho,P}(s).
 \tag{8.2}\label{8.2}$$

[\[thm:trace-class\]]{#thm:trace-class label="thm:trace-class"} If $\sigma=\operatorname{Re}s>2$, then $K_\rho(s)$ is trace class and $$\left\lVert K_\rho(s)\right\rVert_1
 \le d_\rho\left(
   \prod_p(1+p^{-\sigma/2})-1
 \right)^2.
 \tag{8.3}\label{8.3}$$ Cutoffs to the first $N$ primes converge in trace norm, and their Fredholm determinants converge locally uniformly on $\operatorname{Re}s>2$.

The estimate follows from the nuclear decomposition of each matrix block and $$\sum_{S\in\mathcal E_\infty}|q_S(s)|
 =\prod_p(1+p^{-\sigma/2})-1<\infty.
 \tag{8.4}\label{8.4}$$ If $L$ is the sum in [\[8.4\]](#8.4){reference-type="eqref" reference="8.4"} and $L_N$ its cutoff, the explicit tail bound is $$\left\lVert K_\rho-\Pi_NK_\rho\Pi_N\right\rVert_1
 \le d_\rho(L^2-L_N^2)\longrightarrow0.
 \tag{8.5}\label{8.5}$$

The trivial block is exceptional. Its arrival matrix has rank one, and the scalar inclusion--exclusion determinant converges already for $\operatorname{Re}s>1$ to $1/\zeta(s)$. We do not infer that the nontrivial incidence blocks are trace class on $1<\operatorname{Re}s\le2$.

This asymmetry is not a technical footnote. The finite exact standard block and its mixed leakage are rigorous polynomial statements, while the infinite nontrivial Fredholm determinant presently lives farther to the right. No meromorphic continuation, Gamma factor, functional equation, Riemann--von Mangoldt law, or critical-zero realization follows.

# Strict route evaluation and limitations {#sec:route}

The construction was designed to test one specific Route-A loophole, so we evaluate the frozen object rather than combining certificates from different candidates. The strict tuple is $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\
  \texttt{A1\_WEAK},\\
 &\texttt{A2\_ANALYTIC\_DETERMINANT},\
  \texttt{A3\_FAIL},\
  \texttt{A4\_FAIL}).
\end{split}
\tag{9.1}$$

#### A0: credited with a restriction.

The tensor factorization and logarithmic roof supply a noncircular arithmetic origin. The incidence cocycle itself is inventory-blind, so A0 does not certify arithmetic selectivity.

#### A1: weak only.

Primitive words and holonomies are exact, including the commutator witness. There is no bijection between symbolic primitives and primes or prime powers; mixed subset primitives persist.

#### A2: analytic determinant.

The finite same-object character determinants are genuine, and the nontrivial blocks have a trace-class Fredholm realization on $\operatorname{Re}s>2$. This is enough for the stated A2 label, but not for critical strip access.

#### A3 and A4: failed.

The standard block leaks mixed products, matched inventories reproduce the same result, and the analytic domain supplies neither robustness near the critical line nor the missing arithmetic primitive correspondence.

Thus the frozen decision is

  --------------------------------------
     `GO_GENUINE_TRANSITION_HOLONOMY`
      `GO_SAME_OBJECT_ARTIN_BLOCKS`
      `STOP_NONABELIAN_CLEAN_FACTOR`
      `STOP_ARITHMETIC_SELECTIVITY`
            `PROVES_TOO_MUCH`
   `ROUTE_A_REJECTED` `ROUTE_B_LOCKED`.
  --------------------------------------

The limitations are equally concrete. We have no general classification of all-irrep-clean cocycles, no theorem beyond the frozen local grammar, no analytic continuation of the nontrivial block, and no zero correspondence. These are not deferred details of a positive RH argument; they explain the negative route decision.

# Conclusion {#sec:conclusion}

Transition dependence is a real enlargement of the tensor-subset symbolic model. The strict-refinement/strict-coarsening cocycle is intrinsic, non-one-letter, and noncommutative. It yields honest same-object Artin blocks and a primitive commutator certificate. In that sense, the candidate successfully escapes the cyclic parity clock.

It does not escape arithmetic overproduction. The standard representation that detects noncommutativity also detects $x^2y$, $xy^2$, and $x^2y^2$. One-dimensional cleanliness is therefore misleading, and the finite search suggests that full character cleanliness may force a return to the counting gauge class in the minimal grammar. The matched controls then show why neither branch is arithmetically selective.

The next in-family move should alter the allowed-word language before adding another fiber. A constrained factorization shift, a renewal grammar, or a countable Markov presentation derived from tensor incidence is worth testing only if it first supplies a precise primitive prime/prime-power correspondence and survives the same formal/composite/shuffled controls. That is a Symbolic Dynamics question and does not require unlocking Route B.

# Proofs {#app:proofs}

## Same-object factorization and gauge {#app:artin-proof}

The right regular representation decomposes as $\bigoplus_{\rho\in\widehat G}\rho^{\oplus d_\rho}$, with contragredients if one uses the opposite multiplication convention. Applying the same fiber Fourier transform at every state block-diagonalizes $B_{\mathrm{reg},P}$ and gives [\[3.3\]](#3.3){reference-type="eqref" reference="3.3"} after taking determinants.

For the trivial representation, $B_{\mathbf 1,P}(S,T)=w(T)$, so all rows are identical. Its only possible nonzero eigenvalue is $\sum_Tw(T)$, whence $$D_{\mathbf 1,P}=1-\sum_{\varnothing\ne T\subseteq P}
(-1)^{|T|+1}x_T=\prod_{p\in P}(1-x_p)$$ by finite inclusion--exclusion.

Let $C_b$ be block diagonal with state block $\rho(b(S))$. Scalar arrival weights commute with the representation matrices, and therefore $B_\rho^{\alpha^b}=C_b^{-1}B_\rho^\alpha C_b$. This proves determinant invariance. Multiplication around a based closed word telescopes the intermediate gauge values and leaves $$H_{\alpha^b}(\gamma)=b(S_0)^{-1}H_\alpha(\gamma)b(S_0).$$

For the converse test, adjoin to every directed edge a formal inverse dart with inverse gain. Fix a root, spanning tree, and proposed root conjugator. The gauge equation uniquely propagates the vertex values along the tree. Every non-tree edge is then satisfied exactly when its fundamental based closed-walk holonomy agrees under the same root conjugator. This is both necessary and sufficient.

## Incidence classification and counting gauges

Partition $P$ into $S\setminus T$, $S\cap T$, $T\setminus S$, and $P\setminus(S\cup T)$. Two ordered pairs lie in the same orbit under atom bijections exactly when these four region sizes agree. At fixed $|P|=n$, the fourth is determined by $(u,v,w)$. Relabeling naturality makes the cocycle constant on each triple, while restriction compatibility identifies the same triple across larger inventories. Conversely, any stable table on the triples defines a natural local rule.

There are $\binom{n+3}{3}$ nonnegative triples with $u+v+w\le n$. The condition $S=\varnothing$ removes $n+1$ triples with $u=v=0$; the condition $T=\varnothing$ removes $n+1$ triples with $v=w=0$. Their intersection is the zero triple. Inclusion--exclusion therefore gives $\binom{n+3}{3}-2(n+1)+1$, which is [\[4.3\]](#4.3){reference-type="eqref" reference="4.3"}.

Atom relabelings act transitively on subsets of a given cardinality, so a natural vertex map has the form $b_P(S)=q_{|S|}$. Gauging [\[4.4\]](#4.4){reference-type="eqref" reference="4.4"} gives [\[4.5\]](#4.5){reference-type="eqref" reference="4.5"} because $|S|=u+v$ and $|T|=v+w$.

Before gauging, the blocks in every row of $B_\rho$ agree. The determinant lemma reduces the state-space determinant to $$\det\!\left(I-\sum_{\varnothing\ne T\subseteq P}
 (-1)^{|T|+1}x_T\rho(a)^{|T|}\right).$$ All powers of $\rho(a)$ commute, so matrix-valued inclusion--exclusion turns the matrix inside the determinant into $\prod_{p\in P}(I-x_p\rho(a))$. Gauge invariance proves [\[4.6\]](#4.6){reference-type="eqref" reference="4.6"} on the whole orbit.

For two atoms set $q_1=e$. The refinement equation gives $u_0=a_0^2q_2$, hence $q_2=a_0^{-2}u_0$. Substitution into the remaining four types yields [\[4.7\]](#4.7){reference-type="eqref" reference="4.7"}; reversing the substitution proves sufficiency.

## The exact $S_3$ block

Suppose [\[6.1\]](#6.1){reference-type="eqref" reference="6.1"} were gauge equivalent to $a^{|T|}$. The candidate holonomy on the singleton loop $p\to p$ is $e$, while the reference holonomy is $a$. Conjugacy forces $a=e$. The reference then has identity holonomy on every closed word, but $p\to pq\to p$ has candidate holonomy $rt$, a nonidentity three-cycle. This contradicts [\[prop:gauge\]](#prop:gauge){reference-type="ref" reference="prop:gauge"}.

In the state order $(p,q,pq)$ the arrival weights are $(x,y,-xy)$. The trivial block follows from [\[prop:artin\]](#prop:artin){reference-type="ref" reference="prop:artin"}. Since both $r$ and $t$ act by $-1$ in the sign representation, direct evaluation of the $3\times3$ determinant gives the same factor $(1-x)(1-y)$.

With the matrices in [\[6.5\]](#6.5){reference-type="eqref" reference="6.5"}, the standard arrival matrix is $$B_{\mathrm{std}}=
\begin{pmatrix}
xI&yI&-xyR\\
xI&yI&-xyR\\
xT&yT&-xyI
\end{pmatrix}.
\tag{A.1}$$ Exact expansion of the $6\times6$ determinant, followed by collection relative to $(1-x)^2(1-y)^2$, gives $$\det(I-B_{\mathrm{std}})-(1-x)^2(1-y)^2
=3xy(x+y)(xy+1)(x+y-1),$$ which proves [\[6.6\]](#6.6){reference-type="eqref" reference="6.6"}. Since this is a polynomial identity, it may also be checked by direct multiplication. Expanding $$\log\frac{D_{\mathrm{std}}}{(1-x)^2(1-y)^2}$$ through total degree four gives $-3x^2y-3xy^2-3x^3y-6x^2y^2-3xy^3+O_{\mathrm{tot}}(5)$, proving [\[6.7\]](#6.7){reference-type="eqref" reference="6.7"}. Continuing the same exact formal expansion to total degree six gives $[x^3y^3]\Delta\log D=-9$.

## Marked-cycle separation {#app:leak-proof}

Attach directed-edge markers and use [\[5.3\]](#5.3){reference-type="eqref" reference="5.3"}. If $\gamma$ has primitive length $\ell$, its $\ell$ cyclic starting points contribute the same scalar marker and conjugate holonomies to $\operatorname{tr}(B_\rho^\ell)$. Division by $\ell$ leaves the first-traversal coefficient $$-\chi_\rho(H_\alpha(\gamma))w(\gamma)z_\gamma.$$ The isolation hypothesis excludes a second connected primitive word with the same marker. Irreducible characters form a basis of the class functions on $G$, so nonconjugate candidate and reference holonomies differ in some irreducible character.

If the reference is $e$ and every irreducible character took the value $d_\rho$ at $H_\alpha(\gamma)$, unitarity and finite order would force all eigenvalues of every $\rho(H_\alpha(\gamma))$ to be one. The regular representation, which contains every irreducible, is faithful; hence the holonomy would equal $e$, a contradiction.

For $\gamma_\square$, the edge values are $r,t,r,t$, so its holonomy is the nonidentity three-cycle $(rt)^2$. The alternative pairing of its four directed edges gives the two disconnected cycles $[p,pq]$ and $[q,pq]$; there is no competing connected cyclic traversal. The standard-character values $-1$ and $2$ give the gap in [\[6.8\]](#6.8){reference-type="eqref" reference="6.8"}.

## Trace class and cutoff convergence

For $\sigma>2$, $$\sum_{S\in\mathcal E_\infty}|q_S(s)|
=\sum_{\varnothing\ne S\subset_{\mathrm{fin}}\mathbb P}
 \prod_{p\in S}p^{-\sigma/2}
=\prod_p(1+p^{-\sigma/2})-1<\infty,$$ because $\sum_pp^{-\sigma/2}$ converges. Decompose each finite-dimensional block into matrix units. Since $\rho(\alpha(S,T))$ is unitary, its trace norm is $d_\rho$. Summing the entrywise nuclear norms proves [\[8.3\]](#8.3){reference-type="eqref" reference="8.3"}.

For projection $\Pi_N$ onto subsets of the first $N$ primes, the same sum with at least one index outside the cutoff yields [\[8.5\]](#8.5){reference-type="eqref" reference="8.5"}. Hence the operators converge in trace norm, and continuity of Fredholm determinants gives locally uniform convergence on every closed half-plane $\sigma\ge2+\delta$.

For finite $P$, let $Q=\operatorname{diag}(q_S)$ and $A_\rho(S,T)=\rho(\alpha(S,T))$. Then $K=QA_\rho Q$, while the arrival matrix is $A_\rho Q^2$. Sylvester's identity applied to $U=QA_\rho$ and $V=Q$ proves [\[8.2\]](#8.2){reference-type="eqref" reference="8.2"}.

# Scope, evidence, and anti-claim ledger {#app:scope}

L0.22L0.31X item & frozen choice & consequence\
main family & Symbolic Dynamics & no geometric or spectral-operator carrier is imported\
base object & full shift on nonempty finite subsets & the two-block graph is a presentation of the same shift\
local data & incidence triple $(u,v,w)$ & no atom names or numerical prime values enter the cocycle\
group action & right cocycle, commuting left translations & genuine deck symmetry with unchanged roofs\
primitive quotient & cyclic rotation only & reflection is not identified; temporal powers are explicit\
determinant & ordinary finite/Fredholm determinant & Koszul signs are coefficients, not a supertrace\
function space & $\ell^2(\mathcal E_\infty)\otimes V_\rho$ & nontrivial trace-class claim is limited to $\operatorname{Re}s>2$\
controls & formal, composite, shuffled, random, rational & arithmetic selectivity margin is zero\

## Claim-status table

L0.30L0.18X statement & status & boundary\
incidence classification and type count & theorem & source-locked natural local rules\
counting-gauge determinant & theorem & natural gauge orbit; exact finite $P$\
$S_3$ non-one-letter certificate & theorem & arbitrary gauge allowed on the two-atom graph\
standard determinant and leak & exact identity & finite two-atom polynomial ring\
marked commutator gap & theorem & unique connected edge traversal\
$S_3,D_4,Q_8$ clean-class counts & exhaustive evidence & five-type, two-atom tables only\
all-irrep clean implies gauge & conjecture & not promoted beyond the finite searches\
Fredholm determinant & theorem & nontrivial blocks only for $\operatorname{Re}s>2$\
arithmetic selectivity & failed & matched inventories reproduce the mechanism\
RH or critical-zero realization & not claimed & no such object or theorem is present\

## Primitive and repetition audit

The two-cycle $[p,pq]$ is primitive and has holonomy $rt$; its $m$-fold traversal carries $(rt)^m$ and scalar weight $(-x^2y)^m$ in the frozen arrival convention. The four-cycle $[p,pq,q,pq]$ is not a square of a shorter cyclic word. Its unmarked scalar monomial is $x^3y^3$, but its directed-edge marker is the object used in the character-gap theorem. The degree-four coefficient $x^2y^2=-6$ in [\[6.7\]](#6.7){reference-type="eqref" reference="6.7"} is an aggregate trace-log coefficient and is not assigned to one primitive orbit. Likewise the unmarked coefficient $[x^3y^3]\Delta\log D=-9$ aggregates several orbit and repetition contributions; only the directed-edge marker isolates the commutator gap.

## Explicit anti-claims

We do not claim that character determinants are complete gauge invariants; that the finite tables settle arbitrary finite groups; that every incidence cocycle is one-letter plus coboundary; that the trace-class domain continues past $\operatorname{Re}s=2$; that mixed symbolic primitives are prime powers; or that any zero of any determinant corresponds to a Riemann zero. Route B remains locked throughout this paper.
