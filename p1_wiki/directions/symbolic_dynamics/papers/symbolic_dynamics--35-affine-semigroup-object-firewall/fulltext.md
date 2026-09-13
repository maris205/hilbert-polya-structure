---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--35-affine-semigroup-object-firewall"
canonical_tex: "symbolic_dynamics/papers/35-affine-semigroup-object-firewall/main.tex"
canonical_pdf: "symbolic_dynamics/papers/35-affine-semigroup-object-firewall/main.pdf"
source_sha256: "8aac28e3291cd2f99d4d843dccc7e8450c4bb192e98823bb5204fcd4f7492534"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Acyclicity, Backtracks, and Relation Cycles in an Affine Semigroup Benchmark

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/35-affine-semigroup-object-firewall>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/35-affine-semigroup-object-firewall/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/35-affine-semigroup-object-firewall/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/35-affine-semigroup-object-firewall/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/35-affine-semigroup-object-firewall/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The positive affine semigroup already contains addition, multiplication, and the relations underlying the Bost--Connes system, but these data do not by themselves produce a symbolic primitive determinant. We freeze the right Cayley source of $\mathbb N_0\rtimes\mathbb N^{\times}$ and its bounded two-generator slices $P_r=\langle u,v\mid vu=u^rv\rangle^+$. A strict height makes the positive graph acyclic. Formal inverse edges create universal two-step backtracks; Hashimoto reduction deletes those backtracks but retains the primitive affine relation word $vuv^{-1}u^{-r}$. The natural positive, symmetric, and nonbacktracking operators are bounded on the finite-generator slice but noncompact, so none owns an ordinary Fredholm determinant on the uninduced space. Congruence quotients preserve the labelled relation while creating new translation cycles. Separately, the Bost--Connes Gibbs operator satisfies $\mathop{\mathrm{Tr}}(D_\beta)=\zeta(\beta)$, whereas its actual determinant has connected logarithm $\sum_{m\ge1}z^m\zeta(m\beta)/m$; the partition trace is only the first coefficient. An exact audit enumerates 699,040 bounded-slice words, finds 88 primitive cyclically nonbacktracking classes among 126,553 admissible words, verifies all affine witnesses and 48 quotient fixtures, and passes 84/84 tests. The result is a source-locked object firewall and a negative Route-A benchmark, not a new $C^*$-dynamical construction.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Acyclicity, Backtracks, and Relation Cycles\
  in an Affine Semigroup Benchmark
```

## Markdown 正文

# Introduction {#sec:introduction}

The affine semigroup $$P=\mathbb N_0\rtimes\mathbb N^{\times},\qquad
(b,a)(d,c)=(b+ad,ac),$$ is a natural test of whether arithmetic source structure can become a symbolic primitive-orbit determinant. It supports the relations used by the Bost--Connes quantum statistical mechanical system [@BostConnes1995], the $ax+b$ semigroup $C^*$-algebra [@Cuntz2008], and the affine Toeplitz system [@LacaRaeburn2010]. Those theories supply genuine arithmetic partition functions. The question here is deliberately different: does the *unprojected one-step symbolic source*, with its original edge marker, own the same primitive ledger and Fredholm determinant?

This distinction matters because four constructions can share the symbols $u,v$, $\log n$, and $\zeta$ while acting on different spaces:

1.  the positive Cayley graph, whose edges append affine generators;

2.  its formal symmetrization, which adjoins a reverse arc to every edge;

3.  the Hashimoto edge graph, which forbids immediate reversal;

4.  a diagonal Gibbs operator, whose trace is a partition function.

We prove that these are not interchangeable. The positive graph has a strict height and no periodic path. Symmetrization manufactures backtracks. Nonbacktracking removes only the immediate reversals, not the relation polygon forced by $vu=u^rv$. On the natural infinite space the corresponding whole operators are noncompact. The trace-class Gibbs operator is therefore a different object even before its determinant is computed.

#### Contributions.

The paper gives four exact results.

-   A right-Cayley trichotomy separates positive acyclicity, symmetric backtracks, and primitive nonbacktracking affine relation cycles.

-   A whole-operator theorem proves boundedness and noncompactness for the two-generator slice and explains why the full all-$n$ unweighted adjacency is not even defined on a basis vector in $\ell^2(P)$.

-   A finite-quotient theorem proves labelled relation descent while exhibiting the new cycle $U_q^q$ and small-modulus polygon degeneration.

-   A trace/determinant firewall computes the genuine Fredholm determinant of the Bost--Connes Gibbs operator and isolates the prime-seeded bosonic comparison.

The canonical finite benchmark uses the composite value $r=4$. Theorems are uniform in $r\ge2$, so neither primality nor factorization is used to define the source. The exact computation includes $r=2,3,4,5$, congruence controls, generic presentation controls, and signed/matrix counter-boundaries. Its role is verification and falsification of finite proxy claims; the infinite operator conclusions are proved analytically.

#### Scope.

We claim neither a new Bost--Connes model nor a new Ihara determinant. The novelty sought is the narrow source-locked synthesis: a single accounting of source, path clock, connected ledger, natural operator, and partition trace. The conclusion is negative. It closes this positive affine benchmark under ordinary scalar path semantics while leaving graded, matrix, groupoid, and semifinite constructions as separate obligations.

# Primary literature and claim boundary {#sec:literature}

The closest collision is the original Bost--Connes construction. It gives a Hamiltonian with zeta partition trace and also a bosonic determinant, but the one-particle space of the latter is explicitly indexed by primes [@BostConnes1995]. The $ax+b$ relations and canonical time evolution are standard in the associated semigroup algebra [@Cuntz2008]. The affine Toeplitz system has an exact KMS phase diagram and a low-temperature GNS partition function $\zeta(\beta-1)$ [@LacaRaeburn2010]. In that representation the additive coordinate has finite residue-class multiplicity; this is not the full Cayley representation used below.

KMS states for non-principal groupoids require quasi-invariant measures and isotropy traces [@Neshveyev2013]. Monoid growth and type-I partition functions likewise depend on a frozen representation and degree map [@BruceLacaRamaggeSims2019; @BruceLacaTakeishi2021]. Recent algebraic-action groupoids faithfully encode arithmetic actions [@BruceLi2024], and their homology and $K$-theory now have systematic computations [@BruceKubotaTakeishi2026]. These advances do not by themselves identify a KMS normalization with a primitive closed-path trace-log.

On the symbolic side, higher-rank graphs provide path categories with factorization rules [@KumjianPask2000]. Ihara theory gives genuine Euler products and determinant formulas for reduced primitive graph cycles [@StarkTerras1996]; periodic infinite graphs require a specified finite trace and bounded geometry [@GuidoIsolaLapidus2008]. Simple-cycle and line-graph determinant formulas continue to develop [@Watanabe2026]. Their ledger is the set of *all* reduced prime cycles, including cycles induced by group or semigroup relations.

Graph $C^*$-partition functions furnish a particularly useful firewall: their graph example is a fixed-target sum over finite open paths, not a primitive closed-cycle product [@BruceTakeishi2024]. Crystallization can produce boundary or vacuum reductions [@LacaNeshveyevYamashita2025], but using such a reduction would change the support object that this paper keeps unprojected.

Directed labelled Cayley conventions are standard [@Caucal2020], and trace-class determinant identities used below are classical [@Simon2005]. We claim no novelty for any of these components. A bounded primary-source search through 2026-08-15 located no direct instance of the exact conjunction studied here: the all-integer affine source, its original generator marker, the complete positive/symmetric/nonbacktracking ledger, the natural whole operator, and a theorem identifying its Fredholm trace-log with the Bost--Connes partition trace. This is a scoped search statement, not a priority claim.

# Frozen affine source and path semantics {#sec:source}

## The full positive semigroup

Let $$P=\mathbb N_0\rtimes\mathbb N^{\times},\qquad
(b,a)(d,c)=(b+ad,ac).
\label{eq:affine-product}$$ Set $u=(1,1)$ and $d_n=(0,n)$ for every $n\ge2$. The labelled right Cayley graph has edges $$x\xrightarrow{u}xu,\qquad x\xrightarrow{d_n}xd_n.$$ The identity generator is excluded. The alphabet contains every $n\ge2$, not a prime subalphabet.

The full graph has countably infinite outdegree. It is therefore used for a formal path theorem, while the natural bounded whole-operator benchmark is the following finite-generator slice.

## The bounded slice

For $r\ge2$, define $$P_r=\mathbb N_0\rtimes\langle r\rangle
=\{(b,k):b,k\in\mathbb N_0\},\qquad
(b,k)(d,\ell)=(b+r^kd,k+\ell).
\label{eq:slice-product}$$ Writing $u=(1,0)$ and $v=(0,1)$ gives $$vu=u^rv.
\label{eq:affine-relation}$$ Every element has the unique normal form $u^bv^k$. Right multiplication is $$U(b,k)=(b+r^k,k),\qquad V(b,k)=(b,k+1).
\label{eq:right-actions}$$

Every original edge has roof one and contributes one power of a free marker $z$. In a formally symmetrized graph, a reverse arc is a distinct edge and also contributes one step. A primitive orbit is a nonempty closed oriented edge word modulo cyclic rotation that is not a positive temporal power. Reflection is not identified. Cyclic nonbacktracking forbids an oriented edge followed by its formal reverse, including at the cyclic join.

No first return, acceleration, quotient clock, accepted-support projector, KMS support, prime symbol, or target spectral data enters this definition.

## Natural operators

On $\mathcal H_r=\ell^2(P_r)$ let $$S\delta_x=\delta_{xu},\qquad T\delta_x=\delta_{xv}.$$ For fixed $a,b>0$, set $$A_{+}=aS+bT,\qquad
A_{\leftrightarrow}=a(S+S^*)+b(T+T^*).
\label{eq:vertex-operators}$$ Let $E_r^{\mathrm{or}}$ be the oriented edges of the symmetrized graph. Give $U$-type arcs weight $a$ and $V$-type arcs weight $b$. The Hashimoto operator on $\ell^2(E_r^{\mathrm{or}})$ is $$B\delta_e=\sum_{\substack{o(f)=t(e)\\f\ne\bar e}}w(f)\delta_f.
\label{eq:hashimoto}$$ These spaces and operators remain uninduced. A determinant, if owned, would be $\det(I-zA)$ with the same marker $z$.

# Positive acyclicity, backtracks, and relation cycles {#sec:trichotomy}

[\[thm:full-trichotomy\]]{#thm:full-trichotomy label="thm:full-trichotomy"} For the full right Cayley graph of [\[eq:affine-product\]](#eq:affine-product){reference-type="ref" reference="eq:affine-product"}:

1.  $h(b,a)=b+a$ strictly increases along every positive edge, so there is no nonempty directed closed path.

2.  Adjoining a distinct reverse arc to every edge creates a primitive length-two backtrack $e\bar e$ at every retained edge.

3.  After immediate reversals are forbidden, each $n\ge2$ and base vertex $x$ supports the simple primitive relation cycle $$C_{n,x}=d_nu\,\bar d_n\,\bar u^n,$$ of length $n+3$.

4.  The unweighted all-$n$ adjacency does not map any basis vector into $\ell^2(P)$.

For $x=(b,a)$, $$h(xu)-h(x)=a>0,
\qquad h(xd_n)-h(x)=a(n-1)>0.$$ This proves acyclicity. Formal reversal makes $e\bar e$ closed, and no positive loop exists from which it could be a square. Finally, $d_nu=u^nd_n$. The two positive paths have common endpoint; their internal vertices are disjoint because the $d_nu$ branch has multiplier $an$ while the $u^nd_n$ branch keeps multiplier $a$ until the final edge. Traversing one path and the reverse of the other is simple and cyclically reduced, hence primitive. The unweighted image of $\delta_x$ contains the orthonormal family $\{\delta_{xd_n}:n\ge2\}$, so it has infinite norm.

The same result has a bounded finite-generator form.

[\[thm:bounded-benchmark\]]{#thm:bounded-benchmark label="thm:bounded-benchmark"} For every $r\ge2$ and $a,b>0$:

1.  the positive graph of $P_r$ is acyclic;

2.  $\|A_{+}\|\le a+b$ and $A_{+}$ is noncompact;

3.  $A_{\leftrightarrow}$ is bounded selfadjoint, noncompact, and contains a two-step backtrack at every edge;

4.  $B$ is bounded and noncompact, and it retains the primitive relation cycle $$C_{r,x}=vu\,\bar v\,\bar u^r
    \label{eq:relation-cycle}$$ of length $r+3$ and weight $a^{r+1}b^2$;

5.  infinitely many translated copies of [\[eq:relation-cycle\]](#eq:relation-cycle){reference-type="ref" reference="eq:relation-cycle"} are edge-disjoint, so its formal order-$(r+3)$ diagonal sum diverges.

The frozen height $h_r(b,k)=b+r^k$ increases by $r^k$ along $U$ and by $(r-1)r^k$ along $V$. Boundedness and noncompactness of the three operators are proved in [\[prop:noncompactness\]](#prop:noncompactness){reference-type="ref" reference="prop:noncompactness"} and [10](#app:proofs){reference-type="ref" reference="app:proofs"}. closes the word in [\[eq:relation-cycle\]](#eq:relation-cycle){reference-type="ref" reference="eq:relation-cycle"}. It is cyclically reduced, and its single positive $v$ occurrence excludes a proper temporal power. The word uses $r+1$ $U$-type arcs and two $V$-type arcs, giving weight $a^{r+1}b^2$. Base vertices $(0,2j)$ use disjoint pairs of height levels; a subsequence therefore gives infinitely many edge-disjoint translated cycles. Their order-$(r+3)$ diagonal contributions are uniformly positive, so the formal diagonal sum diverges.

The relation cycle is presentation algebra, not arithmetic selection. It is present for prime, composite, and prime-power values of $r$. The composite baseline $r=4$ makes this control explicit.

# Whole-operator ownership {#sec:ownership}

The path ledger and the analytic determinant must belong to the same operator. This condition fails before any zeta comparison.

[\[prop:noncompactness\]]{#prop:noncompactness label="prop:noncompactness"} The operators $A_{+}$, $A_{\leftrightarrow}$, and $B$ in [\[eq:vertex-operators,eq:hashimoto\]](#eq:vertex-operators,eq:hashimoto){reference-type="ref" reference="eq:vertex-operators,eq:hashimoto"} are noncompact. In particular, none is trace class and none owns an ordinary trace-class Fredholm determinant on its stated infinite space.

For $x_j=(0,j)$, $$A_{+}\delta_{x_j}
=a\delta_{(r^j,j)}+b\delta_{(0,j+1)}.$$ These images have pairwise disjoint supports and constant nonzero norm. For $A_{\leftrightarrow}$, restrict to $x_{4j}$; the forward and predecessor supports are again pairwise disjoint. For $B$, take the oriented $V$ edge beginning at $(0,j)$. It has nonbacktracking $U$ and $V$ continuations, and translated choices have disjoint output support. A compact operator cannot map an orthonormal sequence to such a family. Trace class implies compactness [@Simon2005].

The degree bound also gives $$\|A_{\leftrightarrow}\|\le2(a+b),\qquad
\|B\|\le3\max(a,b)$$ by the triangle inequality and the Schur test. Boundedness therefore does not repair Fredholm ownership.

There is a subtle but important formal boundary. Positive acyclicity gives $$\langle\delta_x,A_{+}^m\delta_x\rangle=0
\quad(m\ge1).$$ Because $A_{+}^m$ is not trace class, summing these diagonal entries is not an operator trace theorem. Finite height cutoffs are upper triangular and have determinant one, but this does not manufacture an infinite ordinary Fredholm determinant.

The complete word-level nonbacktracking ledger is also infinite. Embed $P_r$ in $$G_r=\mathbb Z[1/r]\rtimes\mathbb Z.$$ Closed paths based at $x$ are precisely the words in $u,v,\bar u,\bar v$ whose group evaluation is the identity and whose partial products remain admissible in $P_r$. Cyclically reduced admissible identity words give the nonbacktracking classes; removing positive cyclic powers gives the primitive classes. This is a complete classification rule, not a convergent Euler product.

# Congruence quotients preserve relations, not ledgers {#sec:quotients}

For a modulus $q\ge1$, let $$M_{r,q}=\{r^k\bmod q:k\ge0\},\qquad
X_{r,q}=(\mathbb Z/q\mathbb Z)\rtimes M_{r,q}.$$ The labelled maps are $$U_q(b,c)=(b+c,c),\qquad V_q(b,c)=(b,rc).
\label{eq:quotient-actions}$$ When $V_q$ is not injective, reverse arcs remain formal reverses of edge instances rather than inverse maps.

[\[thm:quotient\]]{#thm:quotient label="thm:quotient"} For every $q\ge1$:

1.  $U_qV_q=V_qU_q^r$, so the labelled affine relation word remains closed and cyclically nonbacktracking in the formally symmetrized quotient;

2.  the quotient also has the positive translation cycle $U_q^q(0,1)=(0,1)$, primitive of length $q$ for $q\ge2$;

3.  the affine relation polygon can lose vertex simplicity at small moduli---for example at $(r,q)=(2,2)$;

4.  if $q>r$, the relation polygon based at $(0,1)$ is vertex-simple, but the quotient-created translation cycle still remains.

Consequently the labelled relation descends, whereas the complete primitive ledger does not.

Starting at $(b,c)$, both $V_q$ then $U_q$ and $U_q^r$ then $V_q$ end at $(b+rc,rc)$. Moreover $U_q^j(0,1)=(j\bmod q,1)$, so the first positive return is $j=q$. At $(r,q)=(2,2)$, the $V_q$ branch reaches multiplier zero, where $U_q$ is a self-loop, while the $U_q^2$ branch already returns to its initial vertex. For $q>r$, residues $0,1,\ldots,r$ are distinct and the two branches are internally disjoint.

This result rules out a common shortcut. A family of finite matrices may own finite determinants, but it cannot be identified with the determinant of the infinite positive Cayley graph without a separate convergence and descent theorem. The cycle $U_q^q$ is a concrete obstruction to ledger fidelity.

# The Bost--Connes trace/determinant firewall {#sec:bc-firewall}

In the standard Bost--Connes representation on $\ell^2(\mathbb N^{\times})$, $$H\varepsilon_n=(\log n)\varepsilon_n,
\qquad D_{\beta}=e^{-\beta H}.$$ For $\beta>1$, $D_{\beta}$ is positive trace class and $$\mathop{\mathrm{Tr}}(D_{\beta})=\sum_{n\ge1}n^{-\beta}=\zeta(\beta).
\label{eq:partition-trace}$$ This celebrated identity is genuine; the firewall concerns its ownership.

[\[thm:bc-determinant\]]{#thm:bc-determinant label="thm:bc-determinant"} For $\beta>1$ and $|z|<1$, $$\begin{aligned}
\det(I-zD_{\beta})
 &=\prod_{n\ge1}(1-zn^{-\beta}),
\label{eq:diagonal-det}\\
-\log\det(I-zD_{\beta})
 &=\sum_{m\ge1}\frac{z^m}{m}\zeta(m\beta).
\label{eq:diagonal-log}\end{aligned}$$ Thus $\zeta(\beta)$ is the coefficient of $z$ in the connected logarithm, not the determinant or its reciprocal. At $z=1$ the determinant vanishes because $1$ is an eigenvalue, whereas $\zeta(\beta)$ is finite.

The eigenvalues $n^{-\beta}$ are summable. The trace-class spectral product gives [\[eq:diagonal-det\]](#eq:diagonal-det){reference-type="ref" reference="eq:diagonal-det"}; absolute expansion of $-\log(1-zn^{-\beta})$ and Tonelli summation give [\[eq:diagonal-log\]](#eq:diagonal-log){reference-type="ref" reference="eq:diagonal-log"}.

The comparison with the graph-step operators is now exact. $D_{\beta}$ is compact and trace class; $A_{+}$, $A_{\leftrightarrow}$, and $B$ are noncompact. Compactness is invariant under unitary equivalence and bounded invertible similarity, so these cannot be the same operator in disguise.

The original bosonic construction gives another honest determinant. On the prime-indexed one-particle space $\ell^2(\mathcal P)$, put $$K_{\beta}\varepsilon_p=p^{-\beta}\varepsilon_p.$$ Then $$\det(I-zK_{\beta})^{-1}
=\prod_{p\in\mathcal P}(1-zp^{-\beta})^{-1}
=\sum_{n\ge1}z^{\Omega(n)}n^{-\beta}.
\label{eq:bosonic-det}$$ At $z=1$, this is $\zeta(\beta)$. simultaneously shows why it is not a discovery mechanism here: the basis was already indexed by primes, and $z$ counts boson number $\Omega(n)$ rather than one original affine generator step.

On the full affine space $\ell^2(P)$, the apparently analogous Hamiltonian $H\delta_{(b,a)}=(\log a)\delta_{(b,a)}$ has infinite multiplicity in the additive coordinate $b$. Hence $e^{-\beta H}$ is never compact or trace class there. The finite multiplicities in KMS/GNS constructions are a representation change, not a same-space trace theorem.

# Exact audit and adversarial controls {#sec:audit}

The computation is an exact finite audit of claims that have finite witnesses; it is not a numerical approximation of an infinite determinant. Candidate generation and evaluation are source-separated. The generator uses affine multiplication, words, finite boxes, and quotient actions. The independent evaluator reconstructs normal forms, heights, cyclic reduction, primitive roots, quotient cycles, determinant coefficients, and control labels without importing the source core.

\@Y r Y@ Audit block & Exact size & Frozen conclusion\
positive height edges & 520 & every retained edge strictly increases height\
symmetric backtracks & 520 & one formal two-step class per retained edge\
word census & 699,040 & 126,553 admissible words\
primitive cyclic-NB classes & 88 & complete within the frozen word cutoff\
affine witnesses & 8 & all primitive of length $r+3$\
finite quotients & 48 & relation retained; $U_q^q$ retained; degeneration flagged\
fresh artifacts & 23 & two cleared runs byte-identical\
tests & 84/84 & includes five mutation-sensitivity assertions\
evaluator gates & 10/10 & independent exact checks pass\

The canonical baseline is $r=4$; the suite also uses $r=2,3,5$, multiple bases, mutated exponent relations, generic monoid words, and commutator controls. All eight declared affine witnesses have the predicted length and primitive status. The 48 quotient rows simultaneously verify the relation and the extra translation cycle, including the $(2,2)$ polygon degeneration.

For $\beta=2,3$ and a finite diagonal cutoff, exact rational arithmetic checks [\[eq:partition-trace,eq:diagonal-log\]](#eq:partition-trace,eq:diagonal-log){reference-type="ref" reference="eq:partition-trace,eq:diagonal-log"} coefficient by coefficient. A separate evaluator-only prime-Fock fixture verifies the free-$z$ marker in [\[eq:bosonic-det\]](#eq:bosonic-det){reference-type="ref" reference="eq:bosonic-det"}; it is explicitly labelled a prime-seeded control.

Boundary fixtures prevent an overbroad conclusion. A nonzero signed scalar does not erase all repetitions. The matrix $M=\mathop{\mathrm{diag}}(1,-1)$ has $\mathop{\mathrm{Tr}}M=0$ but $\mathop{\mathrm{Tr}}M^2=2$. More generally a finite matrix local factor is identically one exactly when the holonomy is nilpotent: $$\det(I-tM)\equiv1
\quad\Longleftrightarrow\quad M\text{ is nilpotent}.
\label{eq:nilpotent-boundary}$$ Thus signed, matrix, graded, and groupoid mechanisms are genuine boundary axes; the positive scalar theorem does not claim to eliminate them.

Fresh A/B and cache-free cold C reproduce all $23$ scientific artifacts byte-identically, with aggregate `94df5a68ef2a3a9a05bedddea2b6f210e437622a3d77cb1f9ec4aff351a55fed`. The final $47$-entry canonical code/result ledger has SHA-256 `8ca89e858fadd9069916eeba3584aeae005ba0f1189dc7ec7c51c6cdde6b7e36`. The integration also verifies exact-one-terminal-LF text, source/evaluator separation, Route-A v0.2 schema, dependency provenance, idempotence, and metadata-seal stability.

# Route decision and conclusion {#sec:conclusion}

The benchmark cleanly separates structural arithmetic origin from primitive and analytic success.

\@L0.14L0.20Y@ Gate & Status & Reason\
A0 & structural origin & the all-integer affine semigroup is source-derived and uses no prime oracle\
A1 & fail & positive paths are acyclic; symmetric and nonbacktracking ledgers contain generic relation cycles\
A2 & fail & the natural graph operators are noncompact; finite quotients do not descend ledger-faithfully\
A3 & fail & zeta partition analytics belong to a different diagonal or prime-seeded object\
A4 & fail & no fixed arithmetic spectral carrier or zero mechanism is reached\

The strict repository tuple is $$\texttt{(A0\_STRUCTURAL\_ARITHMETIC\_RELATION, A1\_FAIL,
A2\_FAIL, A3\_FAIL, A4\_FAIL)}.$$ The overall decision is `ROUTE_A_REJECTED`; Route B is locked. No target-zero data, functional equation, critical-line statistic, Weil compression, or RH implication is used.

The positive affine source therefore presents a trilemma rather than a candidate advance: $$\begin{array}{ccl}
\text{positive source}&\Longrightarrow&\text{strict height, no recurrence},\\
\text{formal inverses}&\Longrightarrow&\text{backtracks and reduced relation cycles},\\
\text{KMS/GNS or bosonic object}&\Longrightarrow&\text{partition analytics on changed support}.
\end{array}$$ The conclusion is $$\boxed{\texttt{CLOSE\_AFFINE\_SEMIGROUP\_PARTITION\_IDENTIFICATION\_BRANCH}.}$$

Paper 36 has one admissible obligation. It may construct a source-natural chain-level or quotient-aware cancellation only on one uninduced symbolic object, with the original marker, and must kill backtracks and all affine or commutation relation cycles while retaining a nonzero arithmetic recurrent sector. The same descended operator must own an all-orders connected trace-log, and the mechanism must fail matched generic presentations. A KMS support, boundary/crystal projection, prime basis, first return, or another scalar character is not an eligible repair.

# Proof details and complete ledgers {#app:proofs}

## Bounds and translated witnesses

Right multiplication in $P_r$ is injective, so $S$ and $T$ are isometries. This gives $\|A_{+}\|\le a+b$ and $\|A_{\leftrightarrow}\|\le2(a+b)$. The symmetrized graph has degree at most four. From an oriented edge there are at most three nonbacktracking successors, each of weight at most $\max(a,b)$; the Schur test gives $\|B\|\le3\max(a,b)$.

For $x_j=(0,j)$, the supports of $A_{+}\delta_{x_j}$ are pairwise disjoint. For $A_{\leftrightarrow}$, the subsequence $x_{4j}$ separates predecessor and successor supports. For $B$, use the oriented $V$ edges at levels $j$; the $U$ and $V$ continuations are distinct and remain disjoint across translated levels. These are the orthogonal witnesses used in [\[prop:noncompactness\]](#prop:noncompactness){reference-type="ref" reference="prop:noncompactness"}.

## Primitivity and infinite multiplicity

The cyclic word $v u\bar v\bar u^r$ has one positive $v$ and one negative $v$. It is freely and cyclically reduced: no adjacent pair, including the cyclic join, consists of an edge and its reverse. If it were a $k$-fold cyclic power for $k\ge2$, the count of positive $v$ occurrences would be divisible by $k$, a contradiction. Choosing base vertices at sufficiently separated height levels yields infinitely many edge-disjoint translates.

Ordinary closed words at a base $x$ are exactly admissible identity words in $G_r=\mathbb Z[1/r]\rtimes\mathbb Z$. This proves completeness of the word-level classification: free and cyclic reduction impose the Hashimoto rule, and the usual least-period test imposes temporal primitivity. Infinite translate multiplicity is part of the obstruction.

## Matrix local-factor boundary

For a $d$-dimensional holonomy $M$ with eigenvalues $\lambda_j$, $$\det(I-tM)=\prod_{j=1}^d(1-t\lambda_j).$$ This polynomial is identically one precisely when every eigenvalue is zero, equivalently when $M$ is nilpotent. An invertible or unitary holonomy cannot delete its complete Euler factor. Cancellation between different primitive orbits is a different coefficientwise statement and is not supplied by this lemma.

# Scope declarations and ownership ledger {#app:scope}

\@Y L0.16L0.16Y@ Object & compact? & ordinary Fredholm? & Ledger or analytic output\
full all-$n$ unweighted adjacency & not defined & no & infinite outdegree\
$A_{+}$ on $\ell^2(P_r)$ & no & no & no positive closed paths\
$A_{\leftrightarrow}$ on $\ell^2(P_r)$ & no & no & universal backtracks\
$B$ on $\ell^2(E_r^{\mathrm{or}})$ & no & no & reduced affine relation cycles\
finite quotient matrices & yes & yes, finite & relation plus quotient-created cycles\
$D_{\beta}$ on $\ell^2(\mathbb N^\times)$ & yes & yes & all-integer diagonal trace-log\
$K_{\beta}$ on $\ell^2(\mathcal P)$ & yes & yes & prime-seeded bosonic determinant\

The no-go is limited to the frozen positive scalar, one-step, whole-space objects. It does not rule out regularized or von Neumann determinants, source-derived supertraces, matrix or nilpotent fibers, non-Cayley groupoid isotropy, or an explicitly derived nonnegative inverse-edge roof. Each such proposal must freeze its unit/path space, trace, marker, and source descent and must re-audit every mixed primitive class.

Three distinctions remain mandatory for any continuation. First, deleting a relation word by a group presentation is not the same as cancelling its graph-step Euler factor: the quotient map must intertwine the path operator and every temporal power. Second, a finite trace on a von Neumann or groupoid algebra is additional analytic data; it cannot be inferred from the Hilbert trace that fails here. Third, a nonnegative inverse-edge roof may restore summability, but it is no longer the signed logarithmic cocycle of the standard affine time evolution. These are eligible new objects, not hidden exceptions to the theorem proved above.

The exact matrix boundary is similarly narrow. Nilpotent holonomy can make one local determinant factor equal to one, but its derivation, compatibility with concatenation, and behavior on every mixed relation class remain to be proved. An invertible or unitary transport cannot use this isolated-factor escape. A supertrace can cancel a contractible complex only after a genuine source-derived grading and differential have been supplied.

The words "partition function", "graph", and "determinant" do not imply same-object ownership. Equality after $z=1$ cannot replace equality of free $z$-germs. A boundary, KMS, GNS, crystal, Fock, or accepted-support reduction must be named as a changed representation rather than recurrence already present in the unprojected source.

No peer-review or LLM review loop was run, following the project instruction. The mathematical proofs, primary-source audit, exact computation, compilation, typography, and provenance checks are separate deterministic evidence layers.
