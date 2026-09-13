---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--135-derived-centralizer-orbit-partitions"
canonical_tex: "symbolic_dynamics/papers/135-derived-centralizer-orbit-partitions/main.tex"
canonical_pdf: "symbolic_dynamics/papers/135-derived-centralizer-orbit-partitions/main.pdf"
source_sha256: "cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Derived-Centralizer Orbit Partitions: Tagged Transients, Recurrent Types, and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/135-derived-centralizer-orbit-partitions>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/135-derived-centralizer-orbit-partitions/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/135-derived-centralizer-orbit-partitions/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/135-derived-centralizer-orbit-partitions/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/135-derived-centralizer-orbit-partitions/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let a permutation of $n$ points have cycle type $\lambda=1^{m_1}2^{m_2}\cdots$. We map $\lambda$ to the partition of $n$ formed by the orbit sizes of the derived subgroup of the permutation's centralizer on the original points. A wreath-product calculation gives the local rule: a class $j^m$ becomes $1^j$ for $m=1$, remains $j^2$ for $m=2$, and merges to one part $jm$ for $m\geq3$. We analyze the global iteration of this split--preserve--merge map. A lift that tags every initial part has a strictly decreasing potential exactly at cross-tag merges. Two consecutive transitions without such a merge force the intermediate reachable tagged state to have period at most two. Hence every orbit has eventual period at most two and tail at most $2\ell(\lambda)\leq2n$; the bound is not claimed sharp. We classify all fixed points and strict two-cycles into base, one-oscillator, and two-oscillator forms, derive their ordinary generating functions, and give a multivariate coefficient formula for the one-step fibre over every target partition. Centralizer, wreath-product, and generic partition-dynamics machinery are treated as owned background. Exact finite computation is used only for falsification, and external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Derived-Centralizer Orbit Partitions: Tagged Transients, Recurrent Types, and Exact Fibres'
```

## Markdown 正文

# Definition and complete statement

Write $\mathcal P_n$ for the set of integer partitions of $n$. If $\sigma\in S_n$ has type $\lambda$, define $\mathsf T(\lambda)$ to be the orbit-size partition of $$C_{S_n}(\sigma)'=[C_{S_n}(\sigma),C_{S_n}(\sigma)]$$ on the original $n$ points. Conjugate permutations give conjugate centralizers, so this is a well-defined self-map of $\mathcal P_n$. Orbit partitions in permutation groups and the centralizer setting are established background; see, for example, Britnell and Wildon [@BritnellWildon2014].

A partition is *recurrent* if it lies on a directed cycle of this finite self-map. Define $\operatorname{tail}(\lambda)$ to be the least $t\geq0$ for which $\mathsf T^t(\lambda)$ is recurrent; in particular, every recurrent partition has tail zero.

Use multiplicity notation $\lambda=1^{m_1}2^{m_2}\cdots$ and let $\ell(\lambda)=\sum_jm_j$. For a finite set $A\subseteq\{2,3,\ldots\}$ put $$\label{eq:D}
 \mathcal D_A(q)=\prod_{\substack{j\geq2\\j\notin A}}(1+q^{2j}),
 \qquad \mathcal D(q)=\mathcal D_\varnothing(q),$$ as formal power series. Also write $\Delta_D=\prod_{j\in D}j^2$ for the partition having two parts of each size in $D$.

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq1$, the following hold.

1.  The map $\mathsf T$ is obtained by collecting the local outputs $$\label{eq:local}
     j^m\longmapsto
     \begin{cases}
      1^j,&m=1,\\
      j^2,&m=2,\\
      jm,&m\geq3,
     \end{cases}$$ where $jm$ in the last line is one part.

2.  Every orbit has eventual period one or two, and $$\label{eq:tail}
                      \operatorname{tail}(\lambda)\leq2\ell(\lambda)\leq2n.$$ This is a universal upper bound, not a sharp-clock claim.

3.  The recurrent objects are exactly the disjoint classes $$\begin{aligned}
    {2}
     \mathrm B:\quad &1^e\Delta_D,
         &\quad&e\in\{0,1,2\};                                      \label{eq:B}\\
     \mathrm {O1}:\quad&a\Delta_D\longleftrightarrow1^a\Delta_D,
         &&a\geq3,\ a\notin D;                                     \label{eq:O1}\\
     \mathrm {O2}_{=}:\quad&a1^a\Delta_D,
         &&a\geq3,\ a\notin D;                                    \label{eq:O2e}\\
     \mathrm {O2}_{\ne}:\quad&a1^b\Delta_D\longleftrightarrow
     b1^a\Delta_D,
         &&3\leq a<b,\ D\cap\{a,b\}=\varnothing.                 \label{eq:O2n}\end{aligned}$$ Classes $\mathrm B$ and $\mathrm {O2}_{=}$ are fixed; the other displayed pairs are strict two-cycles.

4.  If $f_n$ counts fixed points and $c_n$ counts strict two-cycles once each for $n\geq1$, and if $f_0=1$, $c_0=0$ by the empty-partition bookkeeping convention, then $$\begin{aligned}
     \sum_{n\geq0}f_nq^n
       &=(1+q+q^2)\mathcal D(q)+\sum_{a\geq3}q^{2a}\mathcal D_{\{a\}}(q),
                                                                   \label{eq:fixed-gf}\\
     \sum_{n\geq0}c_nq^n
       &=\sum_{a\geq3}q^a\mathcal D_{\{a\}}(q)
         +\sum_{3\leq a<b}q^{a+b}\mathcal D_{\{a,b\}}(q).                 \label{eq:cycle-gf}\end{aligned}$$

5.  For a target $\mu=1^{r_1}\cdots n^{r_n}\vdash n$, define $$\label{eq:Psi}
     \Psi_n(\mathbf x)=[z^n]\prod_{j=1}^n
     \left(1+z^jx_1^j+z^{2j}x_j^2
     +\sum_{m=3}^{\lfloor n/j\rfloor}z^{jm}x_{jm}\right).$$ Then the fibre over every target, whether or not it lies in the image, is $$\label{eq:fibre}
                    |\mathsf T^{-1}(\mu)|=[x_1^{r_1}\cdots x_n^{r_n}]
                    \Psi_n(\mathbf x).$$

# The derived wreath-product orbits

Suppose $\sigma$ has $m$ cycles of a fixed length $j$. On their union, its centralizer factor is $$W_{j,m}=C_j^m\rtimes S_m,$$ with $S_m$ permuting the base coordinates. Use additive notation for the base and set $$B_0=\{(a_1,\ldots,a_m)\in C_j^m:a_1+\cdots+a_m=0\}.$$ Commutator subgroups and widths in permutational wreath products have an independent literature [@Skuratovskii2019]; the elementary calculation needed here is included to fix every threshold and orbit.

[\[prop:wreath\]]{#prop:wreath label="prop:wreath"} For $m\geq1$, $$\label{eq:derived}
 W_{j,m}'=
 \begin{cases}
  1,&m=1,\\
  B_0,&m=2,\\
  B_0\rtimes A_m,&m\geq3.
 \end{cases}$$ On the natural $jm$ points, its orbit sizes are respectively $1^j$, $j^2$, and $jm$.

For $m\geq2$, the coordinate-sum homomorphism on $C_j^m$ and the sign homomorphism on $S_m$ show that $W_{j,m}'\leq B_0\rtimes A_m$. If $e_i(a)$ denotes the base element with $a$ in coordinate $i$, then commutation with a transposition interchanging $i$ and $k$ produces a coordinate difference $e_i(a)e_k(-a)$. Such differences generate $B_0$. Commutators in the top copy generate $S_m'=A_m$ for $m\geq3$ and the trivial group for $m=2$. This proves equality in [\[eq:derived\]](#eq:derived){reference-type="eqref" reference="eq:derived"}; for $m=1$ the group $C_j$ is abelian.

For $m=1$ the derived group is trivial, giving $j$ singleton orbits. If $m\geq2$, $B_0$ is transitive within each $j$-point block: translate the chosen block by any amount and compensate in a second block. At $m=2$ the top derived group is trivial, so the two blocks remain separate. At $m\geq3$, $A_m$ is transitive on the blocks, including $A_3$, and the whole union is one orbit. These conclusions remain valid at $j=1$, where the within-block assertion is vacuous.

The full centralizer is the direct product of the factors $W_{j,m_j}$ over the occupied cycle lengths. Derived subgroups commute with finite direct products, and different factors act on disjoint point sets. Collecting the orbits in Proposition [\[prop:wreath\]](#prop:wreath){reference-type="ref" reference="prop:wreath"} proves Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(i).

# Tags, clean transitions, and the tail bound

Give each of the $\ell(\lambda)$ initial parts a distinct atomic tag. A current tag is a set $T$ of initial tags; its mass $w(T)$ is the sum of the sizes of its atoms. Lift [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"} as follows. A unique tagged part of size $j$ splits into $j$ singleton parts carrying the same tag. Two parts of size $j$ are preserved with their separate tags. At multiplicity at least three, replace all parts of size $j$ by one part of size $jm$ whose tag is the union of their distinct tags.

Call a transition *crossing* if the last operation merges at least two distinct current tags, and *clean* otherwise. Write $H_a(T)$ for one whole part of size $a=w(T)$ carrying $T$, and $S_a(T)$ for $a$ singleton parts carrying $T$.

[\[lem:tag\]]{#lem:tag label="lem:tag"} In every tagged state reachable from the atomic lift, each tag $T$ occurs either as $H_{w(T)}(T)$ or as $S_{w(T)}(T)$. Current tags partition the initial tag set. Their number never increases and decreases strictly on every crossing transition.

The claim holds initially in whole form. A multiplicity-one update changes $H_a(T)$ to $S_a(T)$. A multiplicity-two update preserves each represented tag. For a merge at size $j\geq2$, every participating tag is whole and has mass $j$, so the output size is the sum of their masses. At size one, the singleton copies of each participating split tag occur exactly as many times as its mass, so again the output size is the mass of the union tag. These are all cases and prove the form invariant. Unions coarsen the tag partition, and the coarsening is strict exactly when two distinct tags are merged.

Reachability matters in the next lemma. For example, an arbitrarily coloured synthetic state need not obey its conclusion.

[\[lem:normal\]]{#lem:normal label="lem:normal"} Let $X_0\to X_1\to X_2$ be two consecutive clean transitions between reachable tagged states. Then $X_1$ is a disjoint union of tagged dimers $H_j(T)+H_j(U)$ at distinct sizes $j\geq2$ and exactly one of:

1.  a singleton residue of total size $e\in\{0,1,2\}$;

2.  one oscillator phase $H_a(T)$ or $S_a(T)$, with $a\geq3$;

3.  two opposite phases $H_a(T)+S_b(U)$, with $a,b\geq3$ and $T\ne U$.

No dimer has the size of an oscillator, and no singleton residue coexists with an oscillator.

Consider first the non-singleton parts of $X_1$. A pair of equal whole parts in $X_0$ remains a dimer. An unpaired whole part in $X_0$ splits and therefore is not a non-singleton in $X_1$. Because the first transition is clean, the only other way to create a non-singleton is for the entire singleton sector of $X_0$ to be one split tag $S_a(T)$; it then becomes $H_a(T)$. This creates at most one unpaired whole part.

Such a newly created whole has $a\geq3$. Indeed, multiplicity two at size one is preserved rather than merged. More generally, a reachable unpaired $H_2$ can occur only at time zero: at the next update it becomes $S_2$; no local output can later create one unpaired part of size two. A size-two dimer remains paired, and multiplicity at least three merges to size at least six. Thus a split tag already present in $X_0$ cannot coexist with an unpaired $H_2$ that could create an extra two-singleton residue in $X_1$.

The singleton sector of $X_1$ consists of the splits of unpaired whole parts of $X_0$, together with any singleton residue that survived there. Cleanliness of the second transition says that, if this sector has total size at least three, every singleton carries the same tag. Hence it is one $S_b(U)$ with $b\geq3$ and has no residue; otherwise it is a residue of total size at most two. There cannot be two split oscillators.

If $X_1$ contains the whole oscillator $H_a(T)$, then the singleton sector of $X_0$ was exactly $S_a(T)$, so it contained no persistent singleton residue. The preceding size-two observation excludes a delayed residue from an unpaired $H_2$. Thus an oscillator and a residue cannot coexist. If a dimer of size $a$ accompanied $H_a(T)$, then the second transition would merge three distinct whole tags and would be crossing. Finally, if a dimer of size $b$ accompanied $S_b(U)$, then $X_0$ had that dimer together with the unpaired $H_b(U)$ whose split produced $S_b(U)$; its first transition would already have been crossing. This proves all restrictions and the asserted list.

[\[lem:two-clean\]]{#lem:two-clean label="lem:two-clean"} Under the hypotheses of Lemma [\[lem:normal\]](#lem:normal){reference-type="ref" reference="lem:normal"}, $X_1$ has period dividing two under the tagged update.

Dimers and a singleton residue of size at most two are fixed. The remaining local motions are $$H_a(T)\longleftrightarrow S_a(T),\qquad
 H_a(T)+S_b(U)\longleftrightarrow S_a(T)+H_b(U).$$ The exclusions in Lemma [\[lem:normal\]](#lem:normal){reference-type="ref" reference="lem:normal"} prevent either phase from meeting a same-size dimer or an additional singleton tag. Applying the update twice therefore returns every tagged piece of $X_1$.

[\[thm:tail\]]{#thm:tail label="thm:tail"} Every orbit from $\lambda$ has eventual period at most two and satisfies [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}.

There are initially $\ell(\lambda)$ tags. By Lemma [\[lem:tag\]](#lem:tag){reference-type="ref" reference="lem:tag"}, at most $\ell(\lambda)-1$ transitions can be crossing. Before the recurrent part, every two consecutive transitions contain a crossing; otherwise Lemma [\[lem:two-clean\]](#lem:two-clean){reference-type="ref" reference="lem:two-clean"} places the state after the first transition on a cycle of length at most two.

If the tail exceeded $2\ell(\lambda)$, the first $2\ell(\lambda)$ transitions could be grouped into $\ell(\lambda)$ disjoint consecutive pairs, each containing a crossing. This contradicts the preceding maximum of $\ell(\lambda)-1$. Thus the first inequality in [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} holds. The second follows because each part has positive size. Once two consecutive clean transitions occur, the tagged and hence the uncoloured state has period at most two.

This proof intentionally does not identify a sharp maximum tail. The potential loses at least one tag at a crossing but can lose several, so it is suited to a safe uniform bound rather than an equality theory.

# Complete recurrent classification and census

[\[thm:recurrent\]]{#thm:recurrent label="thm:recurrent"} The recurrent partitions are precisely [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"}--[\[eq:O2n\]](#eq:O2n){reference-type="eqref" reference="eq:O2n"}.

First take a recurrent uncoloured orbit and lift one occurrence with atomic tags. Its uncoloured states repeat, while the tag partition can coarsen only finitely many times. After sufficiently many laps there are no crossing transitions. Lemma [\[lem:normal\]](#lem:normal){reference-type="ref" reference="lem:normal"} therefore applies at every phase of this stabilized tagged lift.

Projecting its fixed dimers and singleton residue gives $1^e\Delta_D$ with $e\in\{0,1,2\}$, namely class $\mathrm B$. One whole/split factor has amplitude $a\geq3$ and projects to the two phases in $\mathrm {O1}$. With two opposite-phase factors, equal amplitudes project to the same uncoloured partition $a1^a\Delta_D$, while unequal amplitudes project to the pair in $\mathrm {O2}_{\ne}$; order them as $a<b$. The normal-form exclusions say exactly that $D$ avoids every oscillator amplitude. They also forbid a persistent singleton residue in all oscillator classes. This proves exhaustion and disjointness.

Conversely, direct use of [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"} fixes every dimer and every residue $1^e$ with $e\leq2$, interchanges $a$ with $1^a$ for $a\geq3$, and swaps the two opposite phases in the two-oscillator forms. The stated avoidance conditions prevent an extra equal-size merger. Hence every listed object is recurrent, with the asserted exact period.

A fixed base object independently selects $e\in\{0,1,2\}$ and any set of dimer sizes, giving $(1+q+q^2)\mathcal D(q)$. An equal two-oscillator fixed point of amplitude $a$ has weight $2a$ and forbids a dimer of size $a$, giving the second term of [\[eq:fixed-gf\]](#eq:fixed-gf){reference-type="eqref" reference="eq:fixed-gf"}.

A one-oscillator cycle of amplitude $a$ has total weight $a$ and is counted once after choosing dimers away from $a$. An unequal two-oscillator cycle has weight $a+b$ and is counted once by imposing $a<b$ and excluding both dimer sizes. These are exactly the two terms of [\[eq:cycle-gf\]](#eq:cycle-gf){reference-type="eqref" reference="eq:cycle-gf"}. Theorem [\[thm:recurrent\]](#thm:recurrent){reference-type="ref" reference="thm:recurrent"} makes the transfer exhaustive and disjoint.

In particular, the number of recurrent points of weight $n$ is $f_n+2c_n$.

# Every-target one-step fibres

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Equations [\[eq:Psi\]](#eq:Psi){reference-type="eqref" reference="eq:Psi"}--[\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} hold for every $\mu\vdash n$.

A source partition is uniquely specified by the multiplicities $m_j$. For a fixed size $j$, the four possibilities in [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"} contribute respectively $$1,\qquad z^jx_1^j,\qquad z^{2j}x_j^2,\qquad
 z^{jm}x_{jm}\quad(m\geq3).$$ Here $z$ records source weight and $x_k$ records one output part of size $k$. Different sizes $j$ choose their source multiplicities independently, so multiplication gives the product in [\[eq:Psi\]](#eq:Psi){reference-type="eqref" reference="eq:Psi"}. Extracting $z^n$ restricts to source partitions of $n$, and extracting the target monomial $x_1^{r_1}\cdots x_n^{r_n}$ counts each source multiplicity vector mapping to $\mu$ exactly once. A target outside the image has coefficient zero, so no separate image condition is required.

# Ownership, internal separation, and exact controls

The structural inputs are subtracted aggressively. Britnell and Wildon own centralizer and orbit-partition context [@BritnellWildon2014]; commutator subgroups of wreath products are existing group-theoretic material [@Skuratovskii2019]. Eliahou and Erickson study an iterated multiplicity-description system on integer partitions [@EliahouErickson2013], while Baalbaki et al. provide a recent, different weight-preserving partition dynamics [@BaalbakiEtAl2024]. Thus the wreath decomposition, the calculation in Proposition [\[prop:wreath\]](#prop:wreath){reference-type="ref" reference="prop:wreath"}, generic multiplicity-dynamics language, and formal coefficient extraction receive zero contribution credit. The residual package is the reachable tagged transient theorem, complete recurrent decoder and census, and all-target coefficient for this literal orbit-partition map.

The shared partition carrier does not identify this system with internal P113: that note iterates principal-hook data of Ferrers diagrams and uses a Ferrers-gap potential with a sharp depth, whereas [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"} is a multiplicity-threshold rule with genuine two-cycles and only the nonsharp bound [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}. Nor is the tag lift P123's graph-component complementation. P123 refines actual component structure through graph complements; here tags are auxiliary proof data, coarsen only under mergers, and encode whole/singleton oscillators. The map is also neither permutation powering nor the partition shift--join mechanisms of P105 and P110.

The paper-local exact audit supplies the following finite controls. The observed maximum tail through weight 45 is six, first reached at weight 45, far below the theorem's safe $2n$ ceiling. At weight 30 the exact census is $59$ fixed points, $139$ strict two-cycles, and $337$ recurrent points, agreeing with [\[eq:fixed-gf\]](#eq:fixed-gf){reference-type="eqref" reference="eq:fixed-gf"}--[\[eq:cycle-gf\]](#eq:cycle-gf){reference-type="eqref" reference="eq:cycle-gf"}. A bounded primary-source search did not locate the exact residual package, but a search non-hit is not novelty or priority evidence. External status is `HOLD_EXTERNAL`.

::: {#tab:controls}
  control                                             exact count
  ------------------------------------------------- -------------
  partitions, all $n\leq45$                               540,634
  all target cells, all $n\leq30$                          28,628
  literal wreath products / source group elements      18 / 1,259
  reachable tagged states, all $n\leq30$                  118,634
  two-clean pairs                                          56,961
  exact assertions                                      7,130,840

  : Dependency-free integer/tuple controls. Enumeration is falsification evidence only, not proof or priority evidence.
:::
