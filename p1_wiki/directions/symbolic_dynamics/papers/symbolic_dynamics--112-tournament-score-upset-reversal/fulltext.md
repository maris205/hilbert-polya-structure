---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--112-tournament-score-upset-reversal"
canonical_tex: "symbolic_dynamics/papers/112-tournament-score-upset-reversal/main.tex"
canonical_pdf: "symbolic_dynamics/papers/112-tournament-score-upset-reversal/main.pdf"
source_sha256: "ef4ac3d6efcc2dba4c40c39e0261b1c12d75906f6d035633cad01a52b40d301c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Synchronous Score-Upset Reversal in Tournaments: Energy, Recursive Blocks, and Fixed-Point Enumeration

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/112-tournament-score-upset-reversal>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/112-tournament-score-upset-reversal/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/112-tournament-score-upset-reversal/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/112-tournament-score-upset-reversal/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/112-tournament-score-upset-reversal/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a labelled tournament, simultaneously reorient every edge between vertices of unequal outdegree from the higher-score endpoint to the lower-score endpoint, while retaining edges whose endpoints have equal score. For this specified finite self-map, a strict squared-score Lyapunov identity and a separate equal-score-block factorization prove termination. The factorization identifies the pointwise hitting time with the height of a well-founded score-refinement tree and gives the non-sharp universal bound $\tau(T)\leq n-1$ for $n\geq1$. It also identifies the fixed tournaments as the unique ordered sums of regular tournaments. Routine labelled bookkeeping then gives, for regular-tournament counts $r_j$ and fixed counts $f_n$, $$f_0=1,\qquad f_n=\sum_{j=1}^n\binom nj r_jf_{n-j},\qquad
   \sum_{n\geq0}f_n\frac{x^n}{n!}
   =\frac{1}{1-\sum_{j\geq1}r_jx^j/j!}.$$ All periodic points are fixed, so routine finite-map zeta bookkeeping gives $(1-z)^{-f_n}$. Score sequences, regular tournaments, ordinal sums, regular-tournament enumeration, labelled exponential generating functions, and zeta functions receive zero contribution credit. After comparison with static and iterative Copeland procedures and with arc/cycle-reversal work, the residual scope is only the map-specific conjunction of the Lyapunov identity, permanent block factorization, recursive depth and bound, and fixed-set identification. Ownership, priority, and external circulation remain on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Synchronous Score-Upset Reversal in Tournaments: Energy, Recursive Blocks, and Fixed-Point Enumeration'
```

## Markdown 正文

# Introduction

A tournament records the outcome of every pairwise contest. Its most basic local statistic is the score, or outdegree, of each vertex. We study the synchronous correction rule that points every unequal-score contest from the currently higher-scoring vertex to the lower-scoring vertex and leaves a score tie unchanged. The rule looks like a one-pass ranking projection, but it is not: changing contests also changes the next score classes.

Two simple structures control the resulting temporal feedback. Reversing a score upset strictly increases a quadratic score energy, even when many reversals occur simultaneously. Independently, the first update is an ordinal sum over the old equal-score classes. The score intervals of these blocks cannot overlap, so every subsequent update runs separately inside the unchanged induced subtournaments. This second route gives a literal recursive model of each orbit, not only a termination certificate.

The paper records four parts of one map-specific exact conjunction.

1.  The squared-score energy has an exact positive increment on every nonfixed update; consequently, there are no nontrivial temporal cycles.

2.  Equal-score blocks give an exact factorization of every positive iterate. The pointwise depth equals the height of the associated refinement tree and is at most $n-1$.

3.  Fixed tournaments are precisely unique ordered sums of regular tournaments. A standard labelled-sequence corollary gives the recurrence and exponential generating function displayed in the abstract.

4.  Every positive iterate has the same fixed set. Standard finite-map zeta bookkeeping therefore reduces to one cycle factor.

Tournament scores, their feasibility conditions, regular tournaments, and score-based measures are classical topics [@Landau1953; @Moon1968; @Monsuur2005]. Static points rankings and Copeland choice are likewise established [@Rubinstein1980; @Henriet1985], and successive-choice procedures already iterate score-based selections [@Bouyssou2004; @LinaresBodanza2025]. Score-preserving triangle reversals and broader arc/cycle-reversal questions form another direct neighborhood [@Ryser1964; @Thomassen1988; @GhoshEtAl2026]. Regular-tournament enumeration, labelled generating functions, and the periodic-point zeta construction are also prior tools [@McKay1990; @FlajoletSedgewick2009; @ArtinMazur1965]. Every one of these ingredients receives zero contribution credit here. The residual scope is only the conjunction of the exact statements for the specific synchronous edge update. A bounded owner search did not locate that identical conjunction, but a search miss is neither novelty evidence nor a priority certificate. We make no claim about a sharp global depth or a complete transient enumerator. External dissemination remains **HOLD**.

# Definition and the energy route {#sec:energy}

For $n\geq0$, put $$[n]=\{i\in\mathbb Z:0\leq i<n\},$$ so $[0]=\varnothing$ literally. For a finite label set $V$, let $\mathcal T(V)$ be the set of tournaments on $V$, and put $\mathcal T_n=\mathcal T([n])$. Thus $\mathcal T_0$ and $\mathcal T_1$ are both singletons. Write $u\to_Tv$ when $T\in\mathcal T(V)$ directs the edge $\{u,v\}$ from $u$ to $v$, and let $$s_T(v)=d_T^+(v)$$ be the score of $v$.

[\[def:update\]]{#def:update label="def:update"} For $T\in\mathcal T(V)$ and distinct $u,v\in V$, define $\Phi_V(T)\in\mathcal T(V)$ by $$\label{eq:update}
 u\to_{\Phi_V(T)}v
 \quad\Longleftrightarrow\quad
 s_T(u)>s_T(v)
 \quad\text{or}\quad
 \bigl(s_T(u)=s_T(v)\ \text{and}\ u\to_Tv\bigr).$$ Every score on the right side is evaluated in the unchanged input $T$; all edge decisions are then applied simultaneously. We write $\Phi_n=\Phi_{[n]}$ and suppress the subscript when the label set is clear. For $C\subseteq V$, $T[C]$ denotes the induced tournament on $C$, and $\Phi_C$ means this same definition on the label set $C$, using scores internal to $T[C]$.

The hitting time is $$\tau(T)=\min\{t\geq0:\Phi_V^{t+1}(T)=\Phi_V^t(T)\}.$$ Before termination is proved, the minimum is understood as $\infty$ when the displayed set is empty.

Let $$R(T)=\{(x,y)\in V^2:x\to_Ty\ \text{and}\ s_T(x)<s_T(y)\};$$ these are exactly the arcs reversed by [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. Put $$\delta_v=s_{\Phi_V(T)}(v)-s_T(v),\qquad
 \mathcal E(T)=\sum_{v\in V}s_T(v)^2.$$

[\[thm:energy\]]{#thm:energy label="thm:energy"} For every $T\in\mathcal T(V)$, $$\label{eq:energy}
 \mathcal E(\Phi_V(T))-\mathcal E(T)
 =2\sum_{(x,y)\in R(T)}\bigl(s_T(y)-s_T(x)\bigr)
  +\sum_{v\in V}\delta_v^2.$$ Moreover, $$\label{eq:local-fixed}
             \Phi_V(T)=T\quad\Longleftrightarrow\quad R(T)=\varnothing.$$ Thus the energy difference is positive if and only if $\Phi_V(T)\ne T$. Every orbit reaches a fixed point, and every periodic point is fixed.

The simultaneous score change has the incidence formula $$\label{eq:incidence}
 \delta_v=
 \bigl|\{x\in V:(x,v)\in R(T)\}\bigr|
 -\bigl|\{y\in V:(v,y)\in R(T)\}\bigr|.$$ Expand the left side of [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"} as $$2\sum_{v\in V}s_T(v)\delta_v+\sum_{v\in V}\delta_v^2.$$ By [\[eq:incidence\]](#eq:incidence){reference-type="eqref" reference="eq:incidence"}, $$\sum_{v\in V}s_T(v)\delta_v
 =\sum_{(x,y)\in R(T)}\bigl(s_T(y)-s_T(x)\bigr),$$ so [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"} follows without treating simultaneous reversals as independent updates. Each summand in its first term is a positive integer. The definition reverses precisely the arcs in $R(T)$ and retains every other arc, proving [\[eq:local-fixed\]](#eq:local-fixed){reference-type="eqref" reference="eq:local-fixed"} and strictness.

The phase space is finite. Along a nonconstant orbit the integer $\mathcal E$ strictly increases, so every orbit terminates and no temporal cycle of length greater than one can occur.

# Equal-score blocks and recursive depth {#sec:blocks}

For tournaments $S_1,\ldots,S_k$ on disjoint vertex sets, their *ordinal sum* $S_1\oplus\cdots\oplus S_k$ retains every internal edge and directs every edge from $S_i$ to $S_j$ when $i<j$.

Fix $T\in\mathcal T_n$. Let $C_1,\ldots,C_k$ be its equal-score classes, ordered so that their common scores decrease, and set $$T_i=T[C_i],\qquad L_i=\sum_{j>i}|C_j|.$$

[\[thm:factor\]]{#thm:factor label="thm:factor"} The first update is $$\label{eq:first-factor}
       \Phi_n(T)=T_1\oplus T_2\oplus\cdots\oplus T_k.$$ For $v\in C_i$, $$\label{eq:new-score}
       s_{\Phi_n(T)}(v)=L_i+s_{T_i}(v).$$ In particular, the score intervals belonging to distinct old classes are disjoint and retain their strict order. For every $t\geq1$, $$\label{eq:iterate-factor}
 \boxed{\displaystyle
 \Phi_n^t(T)=
 \Phi_{C_1}^{\,t-1}(T_1)\oplus\cdots\oplus
 \Phi_{C_k}^{\,t-1}(T_k),}$$ Here $T_i=T[C_i]$ throughout, and $\Phi_{C_i}$ is the restriction/update operator defined before [\[thm:energy\]](#thm:energy){reference-type="ref" reference="thm:energy"}; in particular, its scores are internal to $C_i$.

If $i<j$, every vertex of $C_i$ has larger old score than every vertex of $C_j$. The update therefore directs all edges from $C_i$ to $C_j$. An edge inside one class is tied and remains unchanged. This proves [\[eq:first-factor\]](#eq:first-factor){reference-type="eqref" reference="eq:first-factor"}. A vertex in $C_i$ beats all $L_i$ vertices in lower blocks, loses to all vertices in higher blocks, and retains its internal wins. This gives [\[eq:new-score\]](#eq:new-score){reference-type="eqref" reference="eq:new-score"}.

The scores of block $C_i$ lie in the integer interval $$[L_i,L_i+|C_i|-1].$$ The maximum of the next lower interval is $L_i-1$, so distinct block intervals are disjoint. Thus future updates never reverse an interblock edge or merge two old classes. Within $C_i$, every global score has the same additive term $L_i$, so comparing global scores is the same as comparing internal scores. Applying this observation inductively proves [\[eq:iterate-factor\]](#eq:iterate-factor){reference-type="eqref" reference="eq:iterate-factor"}.

The factorization supplies a second, non-energy proof of convergence. We first justify the recursion it uses. A tournament with one score class has all scores tied, so [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} retains every edge and the tournament is fixed. Consequently, a nonfixed tournament has at least two nonempty score classes. Each class is then a proper subset of the label set, so each induced child has strictly smaller order. The following recursion is therefore well-founded: the score-refinement tree $\mathcal R(T)$ is a leaf, with no children, when $T$ is fixed; otherwise its children are precisely the trees $\mathcal R(T[C_i])$ of its score classes. Let $h(T)$ be its height, with a leaf of height zero.

[\[cor:depth\]]{#cor:depth label="cor:depth"} For every tournament, $$\label{eq:tree-depth}
                       \tau(T)=h(T).$$ For $n\geq1$, $$\label{eq:depth-bound}
                       \tau(T)\leq n-1.$$ The unique tournaments of orders zero and one have depth zero.

We use strong induction on the number of vertices. The fixed case has $\tau(T)=h(T)=0$. If $T$ is nonfixed, every child has smaller order by the well-foundedness argument, so the induction hypothesis gives finite $\tau_i=h(T[C_i])$ for all children. Since the blocks have fixed labels and all interblock arcs are frozen, restriction to each $C_i$ shows that, for every $q\geq1$, $$\Phi_n^{q+1}(T)=\Phi_n^q(T)
 \quad\Longleftrightarrow\quad
 \Phi_{C_i}^{q}(T_i)=\Phi_{C_i}^{q-1}(T_i)
 \quad\text{for every }i.$$ Equality at one time makes that factor fixed and hence persists at all later times. Thus all blocks are stable in the displayed equivalence if and only if $q-1\geq\max_i\tau_i$. Because the nonfixed parent is not stable at $q=0$, this proves both directions of $$\label{eq:depth-recursion}
             \tau(T)=1+\max_i\tau(T[C_i]).$$ This is exactly the recursive definition of $h(T)$.

For the bound, use induction on $n$. A nonfixed tournament has at least two score classes by the well-foundedness argument above. Hence every $C_i$ has size at most $n-1$. Induction in [\[eq:depth-recursion\]](#eq:depth-recursion){reference-type="eqref" reference="eq:depth-recursion"} gives $$\tau(T)\leq1+\max_i(|C_i|-1)\leq n-1.$$ The cases $n=0,1$ follow directly from the definition.

The proof of [\[cor:depth\]](#cor:depth){reference-type="ref" reference="cor:depth"} is structurally independent of [\[thm:energy\]](#thm:energy){reference-type="ref" reference="thm:energy"}: it terminates the orbit by induction on block size and also records the full pointwise recursion. Conversely, the energy proof excludes cycles without first identifying a score-class tree.

# Fixed points, enumeration, and zeta {#sec:fixed}

A tournament on $j$ vertices is *regular* when every vertex has outdegree $(j-1)/2$. Nonempty regular tournaments therefore have odd order.

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} A tournament is fixed by score-upset reversal if and only if it is an ordinal sum of nonempty regular tournaments. This ordered decomposition is unique: its blocks are the equal-score classes. The empty tournament is the empty ordinal sum.

Suppose $T$ is fixed and order its score classes as in [3](#sec:blocks){reference-type="ref" reference="sec:blocks"}. By the local criterion [\[eq:local-fixed\]](#eq:local-fixed){reference-type="eqref" reference="eq:local-fixed"}, every interclass edge points from the higher-score class to the lower-score class. Thus $T=T[C_1]\oplus\cdots\oplus T[C_k]$. Every vertex in $C_i$ has the same $L_i$ external wins. Since the vertices also have equal global scores, their internal scores are equal, and $T[C_i]$ is regular.

Conversely, let $T=S_1\oplus\cdots\oplus S_k$ with regular block sizes $m_1,\ldots,m_k$. Every vertex in block $i$ has score $$a_i=\sum_{j>i}m_j+\frac{m_i-1}{2}.$$ For adjacent blocks, $a_i-a_{i+1}=(m_i+m_{i+1})/2>0$. Hence each block is one score class, all interclass edges already point downward in score, and tied internal edges remain unchanged. The decomposition is unique because score classes are intrinsic to $T$.

Let $r_j$ be the number of regular tournaments on a fixed labelled $j$-set. We use $r_0=0$ because a block is required to be nonempty, while $r_j=0$ for positive even $j$. Let $$f_n=|\operatorname{Fix}(\Phi_n)|,$$ where $f_0=1$ counts the empty ordered sum.

[\[cor:enumeration\]]{#cor:enumeration label="cor:enumeration"} For $n\geq1$, $$\label{eq:fixed-rec}
 \boxed{\displaystyle
 f_n=\sum_{j=1}^n\binom nj r_jf_{n-j}.}$$ With $$R(x)=\sum_{j\geq1}r_j\frac{x^j}{j!},\qquad
 F(x)=\sum_{n\geq0}f_n\frac{x^n}{n!},$$ one has the formal identity $$\label{eq:egf}
                       \boxed{F(x)=\frac{1}{1-R(x)}.}$$ The first values are $$(f_0,f_1,\ldots,f_6)=(1,1,2,8,40,264,2048).$$

For a nonempty fixed tournament, choose its unique highest-score regular block. If its size is $j$, there are $\binom nj$ choices of labels, $r_j$ internal orientations, and $f_{n-j}$ choices for the ordered sum below it. This proves [\[eq:fixed-rec\]](#eq:fixed-rec){reference-type="eqref" reference="eq:fixed-rec"}. Multiplying by $x^n/n!$ and summing gives $F(x)=1+R(x)F(x)$, which is equivalent to [\[eq:egf\]](#eq:egf){reference-type="eqref" reference="eq:egf"}; this is the standard labelled-sequence construction [@FlajoletSedgewick2009]. The displayed values follow from $(r_1,r_3,r_5)=(1,2,24)$, part of the prior regular-tournament enumeration literature [@McKay1990].

For a self-map $G$ of a finite set, write $$\zeta_G(z)=\exp\left(\sum_{m\geq1}
                \frac{|\operatorname{Fix}(G^m)|}{m}z^m\right).$$

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} For every $n\geq0$ and $m\geq1$, $$\operatorname{Fix}(\Phi_n^m)=\operatorname{Fix}(\Phi_n),$$ and therefore $$\label{eq:zeta}
                 \boxed{\zeta_{\Phi_n}(z)=(1-z)^{-f_n}.}$$ In particular, the boundary systems $n=0,1$ both have zeta function $(1-z)^{-1}$.

Every fixed point of $\Phi_n$ is fixed by every positive iterate. The reverse inclusion follows from [\[thm:energy\]](#thm:energy){reference-type="ref" reference="thm:energy"}, which excludes temporal cycles of length greater than one. Substitution in the defining series and $\sum_{m\geq1}z^m/m=-\log(1-z)$ give [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}; the definition itself is classical [@ArtinMazur1965].

# Exact controls, owner subtraction, and scope {#sec:controls}

The accompanying standard-library verifier exhausts every labelled tournament for $0\leq n\leq6$, a total of $33{,}868$ states. It compares bit-coded and literal set-of-arcs updates, checks the exact energy identity, the score-interval formula, every factorized iterate through time $n$, the tree-depth equality, the regular-block criterion, the recurrence, and fixed sets of the first eight positive iterates. Its $1{,}677{,}508$ assertions all pass. Selected complete lanes are

    $n$   $|\mathcal T_n|$   fixed   maximum observed depth depth histogram
  ----- ------------------ ------- ------------------------ -----------------------------
      0                  1       1                        0 $\{0:1\}$
      1                  1       1                        0 $\{0:1\}$
      2                  2       2                        0 $\{0:2\}$
      3                  8       8                        0 $\{0:8\}$
      4                 64      40                        1 $\{0:40,1:24\}$
      5              1,024     264                        1 $\{0:264,1:760\}$
      6             32,768   2,048                        2 $\{0:2048,1:26400,2:4320\}$

The same exhaustion actively searches for idempotence failure. Order the edges lexicographically as $$(0,1),(0,2),\ldots,(0,5),(1,2),\ldots,(4,5),$$ and let bit one mean that the smaller endpoint wins. The six-vertex mask $148$ has the exact orbit $$148\;\xmapsto{\Phi_6}\;4\;\xmapsto{\Phi_6}\;0
 \;\xmapsto{\Phi_6}\;0$$ and score vectors $$(2,2,2,2,3,4),\qquad(1,1,2,2,4,5),\qquad(0,1,2,3,4,5).$$ Thus the system is not a projection. More precisely, the program scans $n=0,1,\ldots,6$ increasingly and, at each order, scans the numerical masks in increasing order. Mask $148$ is the least mask with $\Phi_n^2(T)\ne\Phi_n(T)$ in this specified finite scan; no lower scanned order has such a state. This order-dependent statement is the entire minimality claim. It neither identifies a sharp global depth nor replaces the infinite proofs.

#### Mechanics of the closest procedure families.

Every row in the comparison below receives zero contribution credit.

  work                             state/output and deletion                                                      arc action, score timing, and ties
  -------------------------------- ------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Rubinstein; Henriet              static ranking or choice from a tournament; the input is not advanced          no arc changes and no temporal tie-retention rule; scores are evaluated for a static output [@Rubinstein1980; @Henriet1985]
  Bouyssou                         ranking by successive choice; selected alternatives are removed                no arc reorientation; stages are sequential and the choice rule is recomputed on a shrinking set [@Bouyssou2004]
  Linares Lejarraga--Bodanza       an iterative collective-choice procedure, not an orientation-valued self-map   no synchronous all-edge correction from one old score vector; its "Iterative Copeland from below" vocabulary is not our update [@LinaresBodanza2025]
  Ryser; Thomassen; Ghosh et al.   tournament orientations; no vertex deletion                                    chosen triangle/cycle or arc reversals, sequential or controlled; Ryser's and the ESA score-sequence setting is score-preserving, rather than the present simultaneous score-changing rule [@Ryser1964; @Thomassen1988; @GhoshEtAl2026]
  present map                      the complete orientation is the state; no vertex deletion                      all unequal-score pairs are oriented simultaneously from one unchanged old score vector; tied edges are retained; scores are recomputed only for the next time step

#### Zero-credit owner ledger.

Landau's score-sequence theorem receives zero credit [@Landau1953]. Moon's tournament terminology, regular-tournament and ordinal-sum background, including the route to Ryser's triangle-reversal theorem, receives zero credit [@Moon1968; @Ryser1964]. Static score ranking and Copeland choice receive zero credit [@Rubinstein1980; @Henriet1985]; successive and current iterative Copeland-family choice procedures receive zero credit [@Bouyssou2004; @LinaresBodanza2025]. Score-upset and inconsistency language receives zero credit [@Monsuur2005]. The arc/cycle-reversal lineage, including the contemporary ESA 2026 score-sequence neighbor, receives zero credit [@Thomassen1988; @GhoshEtAl2026]. Regular-tournament counts receive zero credit [@McKay1990]; the generic labelled-sequence recurrence and exponential generating function receive zero credit [@FlajoletSedgewick2009]; and the zeta definition and its one-factor specialization receive zero credit [@ArtinMazur1965].

After these subtractions, the only residual scope under consideration is the exact finite-map conjunction for [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}: the simultaneous incidence/Lyapunov identity, permanent score-class factorization, recursive pointwise depth formula with its universal upper bound, and the map-specific identification of the fixed set. The recurrence, exponential generating function, regular counts, and zeta line are low-credit corollaries, not independent contributions. The bounded audit covered tournament score correction, synchronous/parallel score updates, Copeland iteration and ranking by choosing, arc/cycle reversal, and regular-tournament enumeration. Its failure to locate an identical update is not evidence of novelty or priority. Discovery of a temporal owner would supersede the residual scope; owner clearance remains **HOLD**.

#### Internal P106 firewall.

The P106 MIS-polarity system evolves subsets of the vertex set of a fixed undirected graph by an antitone neighborhood operator. Its proof engine is a Galois polarity and its recurrent objects are independent dominating sets. Here the state is the entire orientation of a complete graph, every update may change edges, regular cyclic tournaments can be fixed, and the proof engines are score energy and ordinal-sum refinement. Shared words such as "synchronous," "fixed point," and "zeta" receive no contribution credit; neither phase space nor update is a parameter variant of P106.

#### Limits.

We do not determine the sharp maximum of $\tau$ as a function of $n$, and we do not enumerate all transient tree heights. The bound $n-1$ is the proved universal statement. The bounded owner search is not an external literature certificate. The anonymous working manuscript remains under external **HOLD**.

# Conclusion

Synchronous correction of score upsets has more structure than a one-pass ranking operation. A strict quadratic energy rules out recurrence, while disjoint score intervals turn every orbit into a recursive refinement of unchanged induced subtournaments. That recursion gives the exact pointwise hitting time and the universal $n-1$ bound. At equilibrium, the same score classes become the unique regular blocks, which yields the fixed recurrence, its exponential generating function, and the one-factor zeta formula as zero-credit bookkeeping consequences. The six-vertex state from the specified finite scan shows why a recursive step can be necessary.
