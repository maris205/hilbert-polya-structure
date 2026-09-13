---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--33-relation-homology-operator-non-descent"
canonical_tex: "symbolic_dynamics/papers/33-relation-homology-operator-non-descent/main.tex"
canonical_pdf: "symbolic_dynamics/papers/33-relation-homology-operator-non-descent/main.pdf"
source_sha256: "b1b3705e7e18def4348ad7d5549bd32e6c2637cc889e27b378a3b2b08dd33456"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Relation Homology at the Projective-Residue Boundary: Universal Cusp Survivors, Diamond Collapse, and Operator Non-Descent

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/33-relation-homology-operator-non-descent>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/33-relation-homology-operator-non-descent/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/33-relation-homology-operator-non-descent/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/33-relation-homology-operator-non-descent/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/33-relation-homology-operator-non-descent/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Paper 32 isolated a nonterminal projective-residue grammar that owns an ordinary Fredholm determinant on $\operatorname{Re}s>2$ but fails primitive selectivity through universal $S^2,R^3$ cycles and cusp diamonds. Here we test the only source-natural repair allowed by that result: quotient the same chain object by the presentation relations and fill every $2$--$3$ cusp diamond before any arithmetic label or weight is read. The block quotient is $$M_n=\mathbb Q[P^1(\mathbb Z/n\mathbb Z)]/
    \bigl(\operatorname{im}(1+S)+\operatorname{im}(1+R+R^2)\bigr).$$ Its exact dimension is $|P^1(\mathbb Z/n\mathbb Z)|-o_S(n)-o_R(n)+1$, the first Betti number of the $S$/$R$ orbit-incidence dessin. For every $n\ge2$ the cusp word $[1:0]\xrightarrow{R}[0:1]\xrightarrow{S}[1:0]$ gives a primitive nonbacktracking survivor. Filling all cross diamonds makes the cross grid contractible, so the global homological ledger is $H_1=\bigoplus_n M_n^*$. Ordinary unrestricted cohomology is $\prod_n M_n$, while the program's finite-support cohomology ledger is $L_{\rm fs}=\bigoplus_n M_n$. Finally, the inherited adjacency $S+R$ does not preserve the relation space already at $n=2$, so no same-marker quotient determinant descends. Exact audits through $n=192$ validate 191/191 relative survivors, 148/148 composite survivors, 64/64 generic action controls, 15/15 canonical zero-superdimension twist failures, and 0/191 adjacency descents. The semiring-residue branch is therefore closed.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Relation Homology at the Projective-Residue Boundary:\
  Universal Cusp Survivors, Diamond Collapse, and Operator Non-Descent
```

## Markdown 正文

# Introduction

The preceding projective-residue paper changed the state of the Symbolic Dynamics program in two ways. Positively, it produced a shared recurrent object, not a terminal verifier, whose uninduced graph-step operator is trace class in a half-plane and owns an ordinary Fredholm determinant. Negatively, the same object carried unavoidable presentation cycles: $S^2=1$, $R^3=1$, and the cusp square $$n\longrightarrow 2n\longrightarrow 6n
  \longleftarrow 3n\longleftarrow n .$$ These cycles occur before any roof or Euler weight is applied, including for composite moduli. A positive Route-A continuation therefore had only one honest remaining move: keep the object fixed and remove those relations at chain level.

This paper performs that test. For each $n\ge2$ we keep $$X_n=P^1(\mathbb Z/n\mathbb Z),\qquad
  S[a:b]=[-b:a],\qquad R[a:b]=[-b:a+b],$$ the same cusp $c_n=[1:0]$, the same $2$- and $3$-multiplication cusp correspondences, and the same one-edge marker $z$. Over $\mathbb Q$ we impose the Manin presentation quotient $$M_n=\mathbb Q[X_n]/
  \left(\operatorname{im}(I+S)+\operatorname{im}(I+R+R^2)\right).$$ For the cross-modulus component, we reduce inverse cusp pairs to one cellular edge and attach one two-cell along every $n,2n,6n,3n,n$ square. No state, block, edge, roof, marker, prime label, or field predicate is changed.

The result is decisive but negative. The quotient is not a subtle arithmetic filter; it is the classical Manin-symbol relation module [@manin1972; @merel1991]. Its exact rank is computable from the $S$- and $R$-orbit incidence graph, and that graph always contains a two-edge cusp circuit. Cross-square filling does not select moduli; it contracts the cross grid and leaves a direct sum of nonzero block modules. Character and supercharacter controls either do not kill the cycle words or kill identity relators generically while preserving the cusp word. Finally, the inherited graph-step adjacency $S+R$ is not a chain map for this quotient.

#### Contributions.

Within the frozen Symbolic Dynamics scope, we prove:

1.  the exact all-modulus formula $$\dim_\mathbb QM_n=|X_n|-o_S(n)-o_R(n)+1;$$

2.  a universal primitive nonbacktracking cusp survivor for every modulus $n\ge2$;

3.  contractibility of the filled $2$--$3$ cross grid and the resulting direct-sum residual ledger;

4.  a character firewall separating chain relation polynomials from cycle relator words;

5.  non-descent of the original graph-step adjacency, witnessed already on the three-state block $n=2$;

6.  an exact finite audit through $n=192$ that validates the proofs and rejects all frozen controls.

#### Route-A status.

The quotient remains source-natural, so A0 stays structural. A1 fails because every prime power and mixed composite retains relative homology. A2 fails because the quotient has no induced same-marker graph-step operator. A3 and A4 have no primary determinant, continuation, self-adjoint carrier, or zero correspondence to evaluate. The branch is closed rather than extended.

# Source lock and literature boundary {#sec:source}

For all $n\ge2$, let $X_n=P^1(\mathbb Z/n\mathbb Z)$ and let $S,R$ act by $S[a:b]=[-b:a]$ and $R[a:b]=[-b:a+b]$. The global object is the union of these blocks with inherited cusp correspondences between $n$ and $2n$, and between $n$ and $3n$, at the distinguished cusp $[1:0]$. The roof is the Paper-32 roof and the marker $z$ still counts one inherited graph edge.

The only new operation is a rational chain quotient and an explicit square cell attachment. The candidate is forbidden to consult $|X_n|-(n+1)$, factorization, a prime table, an accepted-support table, target zeros, fitted coefficients, or Route B. Arithmetic strata in the experiment are post-census labels only.

The closest mathematical collision is classical. The quotient by $1+S$ and $1+R+R^2$ on the projective line over $\mathbb Z/N\mathbb Z$ is the Manin-symbol presentation of relative modular-symbol homology [@manin1972; @merel1991]. Ihara, Hashimoto, Bass, and Stark--Terras provide the surrounding graph-zeta and nonbacktracking determinant vocabulary [@ihara1966; @hashimoto1989; @bass1992; @starkterras1996]. Kac--Ward type signed walk determinants require extra embedding or spin data [@kacward1952; @cimasoni2010]. More recent graph-zeta work confirms that weighted and alternating determinant technology is active, but it does not change the present ownership test [@lau2025; @ishikawa2026; @lu2026]. Recent explicit character formulae for congruence subgroups likewise reinforce that character variation is level-wide structure, not a field-only selector [@zhu2025].

Thus the novelty claim is deliberately narrow. We do not present Manin relations, modular symbols, or graph zetas as new. The contribution is the closed-form no-go certificate for this specific Route-A source program: killing the universal cells is possible, but it is generic topology, not prime-selective recurrence.

# The relation quotient {#sec:relation}

Let $V_n=\mathbb Q[X_n]$ and define $$W_n=\operatorname{im}(I+S)+\operatorname{im}(I+R+R^2),\qquad M_n=V_n/W_n .$$ Let $o_S(n)$ and $o_R(n)$ denote the numbers of $S$- and $R$-orbits on $X_n$. Construct a bipartite multigraph $D_n$: left vertices are $S$-orbits, right vertices are $R$-orbits, and each state $x\in X_n$ is an edge connecting the two orbit vertices containing $x$.

[\[thm:rank\]]{#thm:rank label="thm:rank"} For every $n\ge2$, $$\dim_\mathbb QM_n=|X_n|-o_S(n)-o_R(n)+1=\beta_1(D_n).$$

Over $\mathbb Q$, the image of $I+S$ is spanned by the indicator vectors of $S$-orbits, and the image of $I+R+R^2$ is spanned by the indicator vectors of $R$-orbits. If a vector lies in both spans, its coefficient on a state depends only on the $S$-orbit and only on the $R$-orbit. The graph $D_n$ is connected because the $S,R$ action on $P^1(\mathbb Z/n\mathbb Z)$ is transitive. Hence the common intersection is the all-ones line. Therefore $$\dim W_n=o_S(n)+o_R(n)-1,$$ and the displayed formula follows. The same expression is exactly the cycle-rank formula for the connected graph $D_n$.

Equivalently, $M_n=H^1(D_n;\mathbb Q)$ after orienting each state edge from its $S$-orbit vertex to its $R$-orbit vertex. This is why the quotient naturally lands in modular-symbol homology. The interpretation is useful, but it is not a new determinant object.

[\[cor:cuspidal\]]{#cor:cuspidal label="cor:cuspidal"} Removing Eisenstein cusp-boundary directions cannot rescue prime selectivity inside this family.

Classically, the stronger cuspidal dimension is $2g_0(n)$. The exact audit through $n=192$ finds nonzero cuspidal homology on 139 of 148 composite blocks and zero cuspidal homology on five prime blocks. It therefore fails both directions of a field selector.

# Universal cusp survivor and diamond collapse {#sec:cusp}

[\[thm:cusp\]]{#thm:cusp label="thm:cusp"} For every $n\ge2$, the quotient $M_n$ is nonzero. More precisely, $$c=[1:0],\qquad y=Rc=[0:1],\qquad Sy=c$$ give a two-edge circuit in $D_n$, represented by the incidence chain $e_c-e_y$. In the original labelled grammar this is the primitive nonbacktracking word $R$ followed by $S$.

The states $c$ and $y$ are distinct modulo every $n\ge2$, while $Sy=[-1:0]=[1:0]$ projectively. Thus the two state edges $c$ and $y$ share the same $S$-orbit endpoint and the same $R$-orbit endpoint in $D_n$. With the standard orientation from $S$-orbit vertices to $R$-orbit vertices, $\partial(e_c-e_y)=0$. It is the parallel-edge circuit, hence it is not a boundary in the graph and gives a nonzero class in $H_1(D_n;\mathbb Q)$.

The corresponding quotient class is also explicit. In the standard state basis of $V_n=\mathbb Q[X_n]$, put $$z_n=e_c-e_y .$$ For every $S$-orbit indicator and every $R$-orbit indicator $\mathbf 1_O$, the pairing $\langle z_n,\mathbf 1_O\rangle$ is zero, because $c$ and $y$ lie in the same $S$-orbit and in the same $R$-orbit. Hence $z_n\in W_n^\perp$. Since $z_n\ne0$ and the state-basis pairing is positive definite, $z_n\notin W_n$; therefore $[z_n]\ne0$ in $M_n=V_n/W_n$. This is dual to the nonzero two-edge homology circuit under the finite-dimensional identification $M_n=H^1(D_n;\mathbb Q)\cong H_1(D_n;\mathbb Q)^*$.

Thus $\beta_1(D_n)\ge1$ by [\[thm:rank\]](#thm:rank){reference-type="ref" reference="thm:rank"}. In the labelled grammar, the inverse of the first $R$ edge would be $R^2$, not $S$; therefore the two-step word is not immediate backtracking. Its cyclically reduced length in $C_2*C_3$ is two, so it is primitive.

This single theorem refutes the hoped-for primitive ledger before weights: the survivor exists in every prime, prime-power, and mixed-composite block.

[\[thm:diamond\]]{#thm:diamond label="thm:diamond"} After attaching every cusp diamond, each cross-modulus component has zero first homology. The global finite-support residual ledger is $$H_1(\text{filled global complex};\mathbb Q)
  \cong\bigoplus_{n\ge2} M_n^* .$$ Ordinary algebraic cohomology is $\prod_{n\ge2}M_n$; the finite-support cohomology ledger used by the program is $L_{\rm fs}=\bigoplus_{n\ge2}M_n$.

Write $n=m2^a3^b$ with $\gcd(m,6)=1$. Cross edges change one of the exponents $a,b$ by one and preserve $m$. Therefore each component is a quadrant grid, with the $(0,0)$ corner deleted only in the $m=1$ component because $n=1$ is absent. The diamonds are exactly the unit squares of that grid. A full quadrant is contractible; the corner-deleted quadrant is the union of the two contractible half-quadrants $a\ge1$ and $b\ge1$ with contractible intersection. Finite cutoffs are finite down-sets and contract by the same coordinatewise deformation.

Subdivide the cusp edge in each block and attach cross edges at the subdivision vertex. This is an auxiliary CW model for the proof; it does not alter the original graph-step marker. Subdivision does not change block homology, and each block then meets the cross complex in one point. Collapsing the contractible cross components leaves a wedge of block dessins, whose first homology is the direct sum of the block first homologies. Since $M_n=H^1(D_n;\mathbb Q)$, the displayed dual statement follows. Algebraic cohomology of an infinite wedge is a product, so the finite-support ledger is named separately rather than identified with ordinary global $H^1$.

# Twists, signs, and the character firewall {#sec:twists}

The chain quotient and a cycle trace impose different algebraic demands. This distinction is essential.

[\[prop:characters\]]{#prop:characters label="prop:characters"} Some honest one-dimensional characters of $C_2*C_3$ annihilate the relation polynomials $1+S$ or $1+R+R^2$. No honest representation annihilates the cycle relator words $S^2$ and $R^3$ in ordinary trace. The fifteen canonical zero-superdimension differences of distinct one-dimensional characters kill identity relators and commuting diamonds, but all retain the cusp word $SR$.

Let $t$ be a primitive sixth root and enumerate the six one-dimensional characters by $$\chi_k(S)=t^{3k},\qquad \chi_k(R)=t^{2k},\qquad 0\le k<6 .$$ For relation polynomials, $1+\chi_k(S)$ vanishes when $\chi_k(S)=-1$, and $1+\chi_k(R)+\chi_k(R)^2$ vanishes when $\chi_k(R)$ is a nontrivial third root. That is a statement about chain boundaries.

For cycle words, however, every honest representation of $C_2*C_3$ satisfies $\rho(S)^2=\rho(R)^3=I$. The ordinary trace of each relator word is therefore $\dim\rho$, not zero. For virtual differences $\chi_k-\chi_\ell$ with $k\ne\ell$, the superdimension is zero, so identity relators and a commuting diamond have supertrace zero. But on the cusp word $$(\chi_k-\chi_\ell)(SR)=t^{5k}-t^{5\ell}\ne0,$$ because multiplication by $5$ permutes $\mathbb Z/6\mathbb Z$. There are $\binom 62=15$ such differences.

Thus the standard character escape has the wrong granularity. Honest characters can erase relation sums in selected fibers, but an ordinary cycle determinant still sees identity relators. Virtual zero-superdimension differences erase identity relators too broadly and still leave the universal cusp survivor. Neither mechanism creates prime selectivity within the frozen source.

# Operator non-descent and determinant ownership {#sec:operator}

Paper 32's analytic gain was same-object ownership: the unquotiented graph-step operator had an honest trace-class determinant on $\operatorname{Re}s>2$. The relation quotient loses exactly that property.

[\[thm:nondesc\]]{#thm:nondesc label="thm:nondesc"} Let $A_n=S+R$ be the inherited within-block graph-step adjacency. There is no global induced operator $A_n:M_n\to M_n$ with the original marker. The failure already occurs for $n=2$.

Use the ordered states $$e_0=[0:1],\qquad e_1=[1:0],\qquad e_2=[1:1]$$ for $P^1(\mathbb Z/2\mathbb Z)$. The $S$-orbits are $\{e_0,e_1\}$ and $\{e_2\}$; the $R$-orbit is $\{e_0,e_2,e_1\}$. Hence $$W_2=\operatorname{span}\{e_0+e_1,e_2\}.$$ But $S e_2=e_2$ and $R e_2=e_1$, so $$A_2e_2=e_2+e_1\equiv -e_0\pmod{W_2},$$ which is nonzero in the one-dimensional quotient. Therefore $A_2(W_2)$ is not contained in $W_2$, and the quotient operator is not defined.

[\[cor:scalar\]]{#cor:scalar label="cor:scalar"} The scalar comparison $$K_s=\bigoplus_{n\ge2} n^{-s} I_{M_n}$$ is trace class for $\operatorname{Re}s>2$ and has an ordinary Fredholm determinant, but it is not the determinant of the inherited graph-step dynamics.

The dimension bound $\dim M_n\le |P^1(\mathbb Z/n\mathbb Z)|$ is controlled by the same Dedekind-psi majorant used in Paper 32, so $\sum n^{-\operatorname{Re}s}\dim M_n$ converges for $\operatorname{Re}s>2$. This proves trace class for $K_s$. However, the marker in $K_s$ counts a blockwise identity step rather than one inherited $S/R$ graph edge. Orthogonal Hodge compression has the same problem: it is a new nonlocal operator, not an induced chain map. Hopf or graded determinant formulas require a chain map, and [\[thm:nondesc\]](#thm:nondesc){reference-type="ref" reference="thm:nondesc"} proves that $A_n$ is not one.

# Exact finite audit {#sec:audit}

The finite prototype audits the implementation boundary; the infinite nonvanishing, diamond-collapse, character, and non-descent claims have direct proofs above. The frozen parameters are: $$2\le n\le192,\quad \mathbb F_{1000003}\text{ rank audit},\quad
  64\text{ random }C_2*C_3\text{ actions},$$ all six honest one-dimensional characters, all fifteen zero-superdimension differences, and matched opaque relabel seed $1003003+n$.

L0.47r Audit surface & Exact result\
Moduli $2,\ldots,192$ & 191\
Prime / prime-power composite / mixed composite & 43 / 14 / 134\
Relative quotient nonzero & 191 / 191\
Prime / prime-power / mixed relative survivors & 43 / 14 / 134\
Relative Betti sum, prime / prime-power / mixed & 611 / 189 / 3994\
Cuspidal nonzero, prime / prime-power / mixed & 38 / 9 / 130\
Cusp $R,S$ witness returns & 191 / 191\
Original adjacency descends & 0 / 191\
Matched opaque relabel exact & 191 / 191\
Random controls, relators killed / residual nonzero & 64 / 64\
Cross vertices / edges / components & 191 / 158 / 64\
Cross cycle rank before filling / after filling & 31 / 0\
Honest characters killing identity cycle words & 0 / 6\
Honest characters killing both chain norm polynomials & 2 / 6\
Zero-superdimension differences retaining cusp $SR$ & 15 / 15\
Source-only generator checks & 21 / 21\
Prototype bridge checks & 25 / 25\
Independent low-level reconstruction & 8349 / 8349\
Authority unit/integration tests & 1932 / 1932\
Source-separated double run & 20 / 20 payloads\
Paper-root SHA ledger & 40 entries; 21 result payloads\
Source-oracle hits & 0\

The source-oracle scan of the candidate core searches for prime tables, accepted-support predicates, Riemann-zero tokens, target-zero tokens, and similar shortcuts; it has zero hits. The matched clone transports quotient dimension and relation rank exactly for every modulus. The random-action controls show that relation cancellation is presentation topology rather than residue arithmetic. The cross-square boundary rank equals the entire pre-filling cross cycle rank, confirming [\[thm:diamond\]](#thm:diamond){reference-type="ref" reference="thm:diamond"} at the cutoff.

The frozen prototype aggregate is $$\texttt{c5c5f34673590f98e89e6229354a8dc8fc851677c7af8702d4bf54a87e8037d4}.$$ After authority-side evaluator and double-run certification are added, the result ledger is $$\texttt{0cb14d9b25e313f6c34d53983fb01a869175838461cd7e2ca9f27fd0b29d8f30}.$$ The final authority run separates source generation from post-census arithmetic labels. Two isolated canonical runs are byte-identical across all twenty source-separated payloads. The paper-root ledger hashes forty entries: twelve Python source files, seven experiment-control files, and twenty-one generated result payloads. The retained prototype runner is used only as a bridge witness for the frozen eight-payload aggregate above.

# Route-A closure {#sec:route}

L0.25Y Gate & SD-C35 decision\
A0 & `A0_STRUCTURAL_ARITHMETIC_RELATION`. The quotient, diamonds, controls, and labels are source-functorial and frozen before evaluation.\
A1 & `A1_FAIL`. Every modulus has a primitive cusp survivor; all 148 tested composites retain relative homology.\
A2 & `A2_FAIL`. The inherited $S+R$ graph-step adjacency does not preserve the Manin relation space, so no same-marker quotient determinant descends.\
A3 & `A3_FAIL`. There is no primary determinant with continuation, Gamma completion, functional equation, explicit-formula bridge, or Weil compression.\
A4 & `A4_FAIL`. There is no fixed self-adjoint carrier, critical-line mechanism, or zero correspondence; Route B remains locked.\

The adversarial stop is stronger than a single failed experiment. Four independent blocking conditions occur:

1.  relation homology is nonzero on every tested prime power and mixed composite;

2.  the universal cusp word survives all frozen character and supercharacter controls;

3.  diamond filling erases cross linkage rather than selecting a prime family;

4.  the original graph-step operator fails quotient invariance.

Therefore the semiring-residue family is not merely paused. It is closed for this research program: continuing with $P^1(\mathbb Z/n\mathbb Z)$ blocks, fixed $C_2*C_3$ presentations, static field criteria, or Manin-style quotients would replay one of the same obstructions.

# Conclusion

The Paper-32 obligation has now been discharged. The natural chain quotient does exactly what it is supposed to do locally: it kills the $S^2$ and $R^3$ presentation boundaries and the filled cusp diamonds. But the survivor ledger is not arithmetic. Each block retains a primitive cusp class, the global cross complex contracts away, standard twists either do too little or too much, and the original graph-step operator does not descend.

This closes the semiring-residue branch. The next useful direction is not a new quotient of the same residue presentation. A viable source must generate prime primitive orbits before any static projector, return-time compression, regularization, or homological quotient, while the same edge-step object already lies in a determinant class. The highest-value next test is therefore a genuinely global arithmetic dynamical source whose Euler factors arise from primitive recurrence itself, not from block labels.

# Proof details and auxiliary checks {#app:proofs}

## Orbit indicators

If a permutation $p$ has cycles of length dividing $d$ and $d$ is invertible in the coefficient field, then $$I+p+\cdots+p^{d-1}$$ sends every basis vector in a cycle of exact length $e$ to $(d/e)$ times the cycle indicator. Hence its image is exactly the span of orbit indicators. This proves the relation-image statement used in [\[thm:rank\]](#thm:rank){reference-type="ref" reference="thm:rank"} for $(S,d)=(S,2)$ and $(R,d)=(R,3)$.

## Connectedness of the incidence dessin

Two state edges in $D_n$ lie in the same connected component precisely when one can pass between their states by a word in $S$ and $R$. The projective modular action generated by $S[a:b]=[-b:a]$ and $R[a:b]=[-b:a+b]$ is transitive on $P^1(\mathbb Z/n\mathbb Z)$. Therefore $D_n$ is connected.

## Finite-support versus unrestricted cohomology

The global complex contains infinitely many blocks. Cellular chains are finite sums by definition, so the homological primitive ledger is $$H_1=\bigoplus_{n\ge2}M_n^* .$$ If one instead takes unrestricted global cochains, then $$H^1=\prod_{n\ge2}M_n .$$ The project uses the finite-support cohomology ledger $L_{\rm fs}=\bigoplus_{n\ge2}M_n$ only as a ledger, not as ordinary global cohomology and not as determinant ownership.

## Rank field

The rank audit uses $\mathbb F_{1000003}$ only to validate sparse linear algebra at finite cutoffs. The theorems are characteristic-zero statements. The chosen prime avoids the characteristics $2$ and $3$ in which the displayed relation images would degenerate.

# Scope declarations

#### What is proved.

SD-C35 proves the exact Manin-relation rank, a universal cusp survivor for all $n\ge2$, cross-diamond contractibility, complete one-dimensional character and canonical zero-superdimension controls, non-descent of the inherited adjacency at $n=2$, trace-class but non-owned status of the scalar homology comparison, and strict rejection of the frozen Route-A candidate.

#### What is not proved.

The paper does not classify every higher-dimensional superrepresentation, every nonlocal homological functor, every arithmetic groupoid, or every quantum-statistical source. It does not claim novelty for modular symbols, Manin relations, Ihara/Hashimoto zeta, Kac--Ward signs, or Hopf trace identities. It proves no target-zeta equality, analytic continuation, functional equation, self-adjoint carrier, zero correspondence, Riemann Hypothesis statement, or Route-B readiness.

#### Reproducibility.

All finite data are exact JSON/CSV artifacts with SHA-256 ledgers. The canonical authority pipeline is split as follows:

> source\_generator.py\
> audit\_source\_separation.py\
> post\_census\_classifier.py\
> independent\_evaluator.py\
> run\_tests.py

The retained `generate_results.py` runner is a byte-frozen prototype bridge only. The independent evaluator reconstructs the scientific payloads without importing candidate or classifier modules; `audit_artifact_integrity.py` verifies the frozen SHA ledger.
