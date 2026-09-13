---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--119-regular-engel-unitriangular-dynamics"
canonical_tex: "symbolic_dynamics/papers/119-regular-engel-unitriangular-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/119-regular-engel-unitriangular-dynamics/main.pdf"
source_sha256: "b705827c4db387b7148a0fa2cad92e8b7166194137875fba8812dc4765c64017"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Regular Engel Dynamics on Unitriangular Groups: Exact Filtration Fibres and Depth Layers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/119-regular-engel-unitriangular-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/119-regular-engel-unitriangular-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/119-regular-engel-unitriangular-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/119-regular-engel-unitriangular-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/119-regular-engel-unitriangular-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $q$ be a prime power, let $N$ be the regular upper shift, and fix $J=I+N$ in the unitriangular group $U_n(\mathbb F_q)$. We determine the finite dynamics of the single map $E(X)=X^{-1}J^{-1}XJ$. Bier's arbitrary-field fixed-$J$ theorem already gives $E(\gamma_k)=\gamma_{k+1}$ and the corresponding iterated images [@Bier2013]; those image equalities receive zero contribution credit. We give the finite-field refinement that every target in $\gamma_{k+1}$ has exactly $q^{n-k}$ predecessors in $\gamma_k$, identify each fibre as a left centralizer coset, and derive every iterated restricted fibre and depth layer. For $n\geq2$, the resulting filtration-typed census has sharp height $n-1$ and $(q-1)q^{\binom n2-1}$ vertices in its deepest layer; its zeta function is $(1-z)^{-1}$. A complementary proof counts solutions of $XJ=JXY$ by successive discrete differences on superdiagonals. In $U_4(\mathbb F_q)$, the choice $I+E_{12}+E_{34}$ has image size $q^2$ instead of $q^3$, showing only that the theorem does not extend to arbitrary nonregular second entries. Engel-image existence, Lang terminology, regular centralizers, lower-central descent, and generic zeta bookkeeping receive zero credit. Novelty, priority, and external circulation remain on **HOLD**.
author:
- Anonymous
bibliography:
- references.bib
title: 'Regular Engel Dynamics on Unitriangular Groups: Exact Filtration Fibres and Depth Layers'
```

## Markdown 正文

# Introduction and claim boundary {#sec:intro}

Fixing the second entry of a commutator turns the left Engel sequence into an ordinary finite self-map. We study that map for one specific second entry: the regular unitriangular shift. Nilpotence already says that every orbit eventually reaches the identity, and Bier identifies the exact lower-central images. The question here is the finite-field refinement: how many predecessors does each target have at every time, and what exact depth and filtration-typed census do these fibres determine?

Several ingredients are owned background. The expression $X\mapsto X^{-1}\phi(X)$ is a Lang-type twisted coboundary; Lang and Steinberg are foundational sources for that setting [@Lang1956; @Steinberg1968]. Their global surjectivity theorems do not apply to the inner automorphism used below, so we use only the terminology and the elementary fixed-coset observation. Fixed-second-variable iterated commutators are the classical left Engel sequence, and Engel sinks are studied explicitly in [@AcciarriShumyatsky2019; @KhukhroShumyatsky2026]. Most importantly, @Bier2013 [Lemma 1 and the proof of Theorem 1] use our commutator convention and the same fixed regular element $J=I+N$ over an arbitrary field. In the present notation, Bier proves $E(\gamma_k)=\gamma_{k+1}$ and obtains the corresponding fixed-$J$ iterated Engel images. Every image and existence assertion below is therefore a self-contained reproduction of owned input and receives zero contribution credit. The lower-central filtration of a unitriangular group, the centralizer of a regular Jordan block, and broader conjugacy questions in maximal unipotent groups are also established territory [@Steinberg1968; @Goodwin2006]. Each of these facts receives zero contribution credit.

After that subtraction, this note records one exact conjunction for the literal fixed element $J=I+N$:

1.  refining Bier's owned restricted surjectivity, every finite-field target has a left-coset fibre of the exact uniform size $q^{n-k}$;

2.  every restricted iterated fibre, cumulative depth set, exact depth layer, and sharp terminal layer is explicit;

3.  filtration strata give an exact multitype predecessor census, while the whole graph has one recurrent point and one weak component;

4.  the finite-field fibre count has a centralizer--coset proof and a separate triangular superdiagonal count; and

5.  a near-regular $U_4$ example shows that the fixed regular hypothesis cannot be widened to arbitrary noncentral unipotent elements.

#### Internal firewall.

The closest internal proof shape is P109, where a regular nilpotent linear map sends a subspace to its image on the full subspace lattice. Its phase points are subspaces and its fibres use Grassmannian intersection counts. Here the phase points are group elements, the update is a nonlinear fixed commutator, and the fibres are centralizer cosets. P111 uses random positive products in the integer Heisenberg group and studies a word-area cocycle; neither its update nor its observables occur here. The generic slogans "nilpotent descent," "unique absorber," and "uniform fibre" therefore carry no credit. A bounded follow-up search found no source stating the finite-field fibre, layer, and filtration-typed predecessor census below, but that search miss is not evidence of novelty or priority. External use remains on **HOLD**.

# The fixed regular map and its filtration {#sec:setup}

Let $q$ be a prime power and $n\ge2$. Write $E_{ij}$ for the usual matrix unit and put $$N=\sum_{i=1}^{n-1}E_{i,i+1},\qquad J=I+N,\qquad
 U_n(q)=U_n(\mathbb F_q).$$ Thus $U_n(q)$ is the group of upper triangular matrices with diagonal entries one. We use the commutator convention $$=X^{-1}J^{-1}XJ
 \label{eq:commutator}$$ and define the self-map $$E:U_n(q)\longrightarrow U_n(q),\qquad E(X)=[X,J].$$

For $1\le k\le n$, let $\mathfrak n_k$ be the strictly upper triangular matrices whose entries vanish on superdiagonals $1,\ldots,k-1$, and set $$\gamma_k=I+\mathfrak n_k.$$ Then $\gamma_1=U_n(q)$, $\gamma_n=\{I\}$, and $$|\gamma_k|
   =q^{\sum_{r=k}^{n-1}(n-r)}
   =q^{(n-k)(n-k+1)/2}.
 \label{eq:gamma-size}$$ Since $\mathfrak n_r\mathfrak n_s\subseteq\mathfrak n_{r+s}$, the inverse series for $I+A$ gives $$\subseteq\gamma_{r+s}
 \quad\text{whenever }r+s\le n.
 \label{eq:filtration-product}$$ In particular, $E(\gamma_k)\subseteq\gamma_{k+1}$.

For $X\in U_n(q)$ define its entry depth $$\tau(X)=\min\{t\ge0:E^t(X)=I\}.
 \label{eq:depth}$$ The minimum is finite by [\[thm:iterates\]](#thm:iterates){reference-type="ref" reference="thm:iterates"}. Empty sums below are zero, $E^0$ is the identity map, and every target is understood as an element of the full phase $U_n(q)$ unless a smaller set is displayed.

[\[rem:small-n\]]{#rem:small-n label="rem:small-n"} For $n=1$ the phase is the singleton $\{I\}$, so the depth is zero and the zeta function is $(1-z)^{-1}$. We state the nontrivial filtration formulas for $n\ge2$. When $n=2$, $U_2(q)$ is abelian, $E$ is constant at $I$, and the layers have sizes $1$ and $q-1$, exactly as the general formulas give. No $n=0$ matrix convention is used.

# Exact one-step fibres: the centralizer route {#sec:coset}

[\[thm:one-step\]]{#thm:one-step label="thm:one-step"} For every $1\le k<n$, $$E(\gamma_k)=\gamma_{k+1}.
 \label{eq:restricted-image}$$ More precisely, for $Y\in U_n(q)$, $$\#\{X\in\gamma_k:E(X)=Y\}
 =\begin{cases}
   q^{n-k},&Y\in\gamma_{k+1},\\
   0,&Y\notin\gamma_{k+1}.
  \end{cases}
 \label{eq:one-step-fibre}$$ Every nonempty fibre is a left coset of $C_{\gamma_k}(J)$.

The image equality [\[eq:restricted-image\]](#eq:restricted-image){reference-type="eqref" reference="eq:restricted-image"} is @Bier2013 [Lemma 1] in the notation $\gamma_k=UT_n^{k-1}$ and is included only for a self-contained dynamical statement. The asserted finite-field refinement is the exact cardinality and left-coset description of every fibre.

Let $\phi(X)=J^{-1}XJ$. Normality of $\gamma_k$ makes $\phi$ an automorphism of $\gamma_k$, and $E(X)=X^{-1}\phi(X)$. If $E(X_1)=E(X_2)=Y$, then $\phi(X_i)=X_iY$ and hence $$\phi(X_2X_1^{-1})=X_2Y(X_1Y)^{-1}=X_2X_1^{-1}.$$ Conversely, if $h\in\gamma_k$ satisfies $\phi(h)=h$, then $E(hX)=E(X)$. Thus every nonempty fibre is exactly a left coset $C_{\gamma_k}(J)X$.

We compute this centralizer without importing an orbit formula. Commuting with $J$ is equivalent to commuting with $N$. For a matrix $M$, the equation $MN=NM$ reads $$M_{i,j-1}=M_{i+1,j}$$ where the boundary entries are zero. The boundary equations force $M$ to be upper triangular, and the displayed recurrence makes each superdiagonal constant. Hence the full matrix centralizer is $\mathbb F_q[N]$. Intersecting its unipotent units with $\gamma_k$ gives $$C_{\gamma_k}(J)
  =\left\{I+a_kN^k+\cdots+a_{n-1}N^{n-1}:a_i\in\mathbb F_q\right\},
 \qquad |C_{\gamma_k}(J)|=q^{n-k}.
 \label{eq:centralizer}$$ The coset result therefore makes every nonempty fibre have size $q^{n-k}$. Together with the inclusion $E(\gamma_k)\subseteq\gamma_{k+1}$, [\[eq:gamma-size\]](#eq:gamma-size){reference-type="ref" reference="eq:gamma-size"} gives $$|E(\gamma_k)|
  =\frac{|\gamma_k|}{q^{n-k}}
  =q^{(n-k-1)(n-k)/2}
  =|\gamma_{k+1}|.$$ The inclusion is equality, proving both assertions.

The left-coset orientation in [\[thm:one-step\]](#thm:one-step){reference-type="ref" reference="thm:one-step"} matters: for our convention [\[eq:commutator\]](#eq:commutator){reference-type="eqref" reference="eq:commutator"}, equality of two fibres fixes $X_2X_1^{-1}$ rather than $X_1^{-1}X_2$. The verifier checks the literal left coset for every target in its exhaustive lanes.

# A second route through superdiagonal equations {#sec:triangular}

The next proof counts every solution without the centralizer theorem, orbit--stabilizer, or a cardinality comparison. Bier's earlier block-inductive argument already supplies existence; the point here is the finite-field multiplicity and its explicit free coordinates.

[\[prop:triangular\]]{#prop:triangular label="prop:triangular"} Fix $1\le k<n$ and $Y\in\gamma_{k+1}$. The equation $E(X)=Y$ has exactly $q^{n-k}$ solutions $X\in\gamma_k$.

Write $X=I+A$ and $Y=I+B$. From [\[eq:commutator\]](#eq:commutator){reference-type="eqref" reference="eq:commutator"}, the equation $E(X)=Y$ is equivalent to $XJ=JXY$. Expanding both sides and cancelling their common terms gives the exact matrix equation $$AN-NA=B+NB+AB+NAB.
 \label{eq:triangular-equation}$$

For $r\ge k$, collect the $r$th superdiagonal of $A$ as $$A^{(r)}=(a_{1,1+r},a_{2,2+r},\ldots,a_{n-r,n})\in\mathbb F_q^{n-r}.$$ On superdiagonal $r+1$, the left side of [\[eq:triangular-equation\]](#eq:triangular-equation){reference-type="eqref" reference="eq:triangular-equation"} is $$\Delta_r A^{(r)},\qquad
 \Delta_r(x_1,\ldots,x_{n-r})
       =(x_1-x_2,\ldots,x_{n-r-1}-x_{n-r}).
 \label{eq:difference}$$ The map $\Delta_r:\mathbb F_q^{n-r}\to\mathbb F_q^{n-r-1}$ is onto: after choosing $x_1$, the target differences determine $x_2,\ldots,x_{n-r}$. Its kernel is the one-dimensional space of constant vectors, so every fibre has exactly $q$ elements. For $r=n-1$, the codomain is the zero space and the same statement remains valid.

It remains to verify that these difference equations are triangular in $r$. The target $B$ begins on superdiagonal $k+1$. In the equation on superdiagonal $r+1$, the term $NB$ is fixed, while a term from $AB$ uses a source superdiagonal $u$ with $$u+(k+1)\le r+1,
               \qquad\text{hence }u\le r-k<r.$$ A term from $NAB$ has $u+(k+1)+1\le r+1$, and again $u<r$. Consequently the right side at stage $r$ depends only on the prescribed $B$ and on $A^{(k)},\ldots,A^{(r-1)}$, which have already been chosen. Starting at $r=k$, solve successively through $r=n-1$. Each of the $n-k$ stages contributes one free field coordinate, and no later equation changes an earlier choice. Every target therefore has exactly $q^{n-k}$ solutions.

Route I treats $E$ as a twisted group coboundary and counts a fibre from fixed cosets and a regular centralizer. Route II counts solutions of a nonlinear matrix equation through additive difference maps; it does not use the centralizer, cosets, or domain/image cardinalities. Neither route claims the owned existence theorem as new. The later temporal corollaries share the one-step count and are not advertised as independently derived.

# All iterated fibres and exact depth layers {#sec:temporal}

For $0\le t\le n-k$, put $$S_{k,t}=\sum_{j=k}^{k+t-1}(n-j),\qquad S_{k,0}=0.
 \label{eq:Skt}$$

[\[thm:iterates\]]{#thm:iterates label="thm:iterates"} Let $1\le k<n$.

1.  For $0\le t\le n-k$, $$E^t(\gamma_k)=\gamma_{k+t},
     \label{eq:iterated-image}$$ and for every $Y\in U_n(q)$, $$\#\{X\in\gamma_k:E^t(X)=Y\}
     =\begin{cases}
       q^{S_{k,t}},&Y\in\gamma_{k+t},\\
       0,&Y\notin\gamma_{k+t}.
      \end{cases}
     \label{eq:iterated-fibre}$$ For $t\ge n-k$, the image is $\{I\}$ and the fibre over $I$ is all of $\gamma_k$.

2.  The cumulative and exact depth counts inside $\gamma_k$ are $$\begin{aligned}
     \#\{X\in\gamma_k:\tau(X)\le t\}&=q^{S_{k,t}},
           &&0\le t\le n-k,                       \label{eq:cdf}\\
     L_{k,0}&=1,                                   \label{eq:layer-zero}\\
     L_{k,t}&=
     \left(q^{n-k-t+1}-1\right)
     q^{\sum_{j=k}^{k+t-2}(n-j)},
           &&1\le t\le n-k.                       \label{eq:layers}\end{aligned}$$ Here $L_{k,t}=\#\{X\in\gamma_k:\tau(X)=t\}$.

3.  On the full phase, the sharp maximum depth is $n-1$, and the deepest layer has $$(q-1)q^{\binom n2-1}
     \label{eq:deepest}$$ vertices.

The image equality in part (i) is also the fixed-$J$ Engel-image construction in the proof of @Bier2013 [Theorem 1], or equivalently the iteration of Bier's restricted lemma; it receives zero credit here. Composing the exact finite-field fibre counts in [\[thm:one-step\]](#thm:one-step){reference-type="ref" reference="thm:one-step"} gives multiplicity $$\prod_{j=k}^{k+t-1}q^{n-j}=q^{S_{k,t}},$$ including the empty product at $t=0$. At $t=n-k$ the target is $\gamma_n=\{I\}$ and $S_{k,n-k}$ is the exponent in [\[eq:gamma-size\]](#eq:gamma-size){reference-type="ref" reference="eq:gamma-size"}; all later iterates remain at $I$.

The set in [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} is the $E^t$-fibre of $I$. Subtracting the count at time $t-1$ gives $$q^{S_{k,t}}-q^{S_{k,t-1}}
 =q^{S_{k,t-1}}\bigl(q^{n-k-t+1}-1\bigr),$$ which proves [\[eq:layers\]](#eq:layers){reference-type="eqref" reference="eq:layers"}. Taking $k=1$ shows that every state has depth at most $n-1$. The last factor in [\[eq:layers\]](#eq:layers){reference-type="eqref" reference="eq:layers"} is nonzero for $t=n-1$, so the bound is attained. Substitution yields $$L_{1,n-1}=(q-1)q^{\sum_{j=1}^{n-2}(n-j)}
           =(q-1)q^{\binom n2-1}.$$

::: {#tab:layers}
   $q$   $n$    $t=0$   $t=1$    $t=2$     $t=3$     $t=4$     $t=5$
  ----- ----- ------- ------- -------- --------- --------- ---------
   $2$   $6$      $1$    $31$    $480$    $3584$   $12288$   $16384$
   $3$   $5$      $1$    $80$   $2106$   $17496$   $39366$       ---
   $4$   $4$      $1$    $63$    $960$    $3072$       ---       ---

  : Full-phase exact depth layers $L_{1,t}$. Dashes are depths beyond the sharp maximum. The machine-readable artifact also lists all restricted levels $k$ for these lanes.
:::

The three row sums in [1](#tab:layers){reference-type="ref" reference="tab:layers"} are respectively $2^{15}=32768$, $3^{10}=59049$, and $4^6=4096$. The accompanying file `code/exact_layer_table.tsv` contains 43 rows over every valid pair $(k,t)$ for these three $(q,n)$ lanes; the canonical verifier rebuilds the table from [\[eq:gamma-size,eq:Skt,eq:layers\]](#eq:gamma-size,eq:Skt,eq:layers){reference-type="ref" reference="eq:gamma-size,eq:Skt,eq:layers"} and checks its bytes.

# The rooted component and filtration-type indegrees {#sec:tree}

Put $\Gamma_k^\circ=\gamma_k\setminus\gamma_{k+1}$ for $1\le k<n$.

[\[cor:tree\]]{#cor:tree label="cor:tree"} The functional graph of $E$ has one weak component and one recurrent point, $I$. After retaining the loop $I\to I$, every other vertex lies in its rooted in-tree. For $Y\in U_n(q)$, $$\operatorname{indeg}(Y)=\#E^{-1}(Y)
  =q^{n-1}\mathbf 1_{\gamma_2}(Y).
 \label{eq:full-indegree}$$ The loop-suppressed root has $q^{n-1}-1$ children; any other $Y\in\gamma_2$ has $q^{n-1}$ children; and vertices outside $\gamma_2$ have none.

More finely, for $1\le k\le n-2$, $$\#\{X\in\Gamma_k^\circ:E(X)=Y\}
 =q^{n-k}\mathbf 1_{\gamma_{k+1}}(Y)
  -q^{n-k-1}\mathbf 1_{\gamma_{k+2}}(Y),
 \label{eq:stratum-indegree}$$ while $$\#\{X\in\Gamma_{n-1}^\circ:E(X)=Y\}
 =(q-1)\mathbf 1_{\{I\}}(Y).
 \label{eq:last-stratum}$$ Finally, $$\#\operatorname{Fix}(E^m)=1\quad(m\ge1),\qquad
 \zeta_E(z)=\exp\!\left(\sum_{m\ge1}\frac{z^m}{m}\right)
            =\frac1{1-z}.
 \label{eq:zeta}$$

By [\[thm:iterates\]](#thm:iterates){reference-type="ref" reference="thm:iterates"}, every state reaches $I$ and the deepest layer is nonempty. Hence there is one component, its only directed cycle is the loop at $I$, and its height is exactly $n-1$. Formula [\[eq:full-indegree\]](#eq:full-indegree){reference-type="eqref" reference="eq:full-indegree"} is [\[eq:one-step-fibre\]](#eq:one-step-fibre){reference-type="ref" reference="eq:one-step-fibre"} with $k=1$.

For $k\le n-2$, subtract the number of predecessors lying in $\gamma_{k+1}$ from the number lying in $\gamma_k$. Applying [\[eq:one-step-fibre\]](#eq:one-step-fibre){reference-type="ref" reference="eq:one-step-fibre"} at levels $k$ and $k+1$ gives [\[eq:stratum-indegree\]](#eq:stratum-indegree){reference-type="eqref" reference="eq:stratum-indegree"}. At the last level, all $q$ elements of $\gamma_{n-1}$ map to $I$, and removing the identity leaves $q-1$. The unique recurrent point is fixed by every positive iterate, so the fixed counts and the standard Artin--Mazur conversion [@ArtinMazur1965] give [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

# Failure for one nonregular second entry {#sec:counterexample}

The preceding theorem does not extend to an arbitrary unipotent choice of the second commutator entry.

[\[prop:counterexample\]]{#prop:counterexample label="prop:counterexample"} Let $$J'=I+E_{12}+E_{34}\in U_4(q)$$ and set $E'(X)=X^{-1}(J')^{-1}XJ'$. Then $$|C_{U_4(q)}(J')|=q^4,\qquad |E'(U_4(q))|=q^2<q^3=|\gamma_2|.
 \label{eq:counterexample-counts}$$ Thus $E'(U_4(q))\ne\gamma_2$, and every nonempty full-phase fibre has $q^4$, not $q^3$, elements.

Write $$A=a_{12}E_{12}+a_{13}E_{13}+a_{14}E_{14}
   +a_{23}E_{23}+a_{24}E_{24}+a_{34}E_{34}.$$ Since $X=I+A$ commutes with $J'$ precisely when $A$ commutes with $E_{12}+E_{34}$, direct multiplication gives the two independent conditions $$a_{23}=0,\qquad a_{24}=a_{13}.$$ Four coordinates remain free, proving the centralizer count. The same fixed-coset argument used in [\[thm:one-step\]](#thm:one-step){reference-type="ref" reference="thm:one-step"} applies to $E'$ and gives $|E'(U_4(q))|=q^6/q^4=q^2$. Every commutator in $U_4(q)$ lies in $\gamma_2$, whose order is $q^3$, so the inclusion is strict. The fibre claim follows from the same coset calculation.

This example misses only the middle simple-root entry of the regular shift. It is therefore a structural guard, not the vacuous central choice $J'=I$. The title, abstract, and all theorem statements deliberately keep the fixed regular $J=I+N$ hypothesis.

# Exact controls and conclusion {#sec:controls}

The standard-library verifier constructs literal polynomial-basis models of $\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_8$, and $\mathbb F_9$. It exhausts $55{,}808$ regular phase states, checks 39 restricted surjections and 112 iterated-fibre profiles, and separately exhausts $20{,}514$ states in the $U_4$ counterexample lanes. Its $1{,}491{,}877$ executed assertions include statewise matrix inverses, the equation $XJ=JXY$, literal left centralizer cosets, all depth histograms, all filtration-stratum indegrees, unique periodicity through several iterates, and the exact table artifact. These finite computations are falsification controls, not proofs or owner certificates.

For the fixed regular shift, Bier's owned image descent and our exact finite-field fibres reduce the temporal count to multiplication along the lower-central levels. The centralizer route explains a fibre as a group coset; the triangular route explains each of its $n-k$ free coordinates. Multiplying and subtracting those fibres yields the complete filtration-typed fibre and depth census. The $U_4$ calculation shows failure for one near-regular entry and blocks extension to arbitrary unipotent second entries; it does not classify every nonregular case. No statement is made for another Engel word or for conjugacy dynamics. Bier's image theorem, Lang theory, regular centralizers, lower-central filtrations, and generic finite-map zeta identities retain zero contribution credit. Novelty, priority, specialist clearance, and external circulation remain on **HOLD**.
