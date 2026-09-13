---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--200-lex-first-alternating-switch"
canonical_tex: "symbolic_dynamics/papers/200-lex-first-alternating-switch/main.tex"
canonical_pdf: "symbolic_dynamics/papers/200-lex-first-alternating-switch/main.pdf"
source_sha256: "0827a2bf6d3162699074bbfbe5152108bd9bda897c8b1a08e924b514cc83e8ea"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Least Alternating-Rectangle Switching: A Width-Uniform Tail Bound and Exact Predecessors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/200-lex-first-alternating-switch>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/200-lex-first-alternating-switch/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/200-lex-first-alternating-switch/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/200-lex-first-alternating-switch/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/200-lex-first-alternating-switch/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $r,s\ge2$, on labelled binary $r$ by $s$ matrices, repeatedly complement the lexicographically first alternating rectangle, with the row pair ordered before the column pair. A matrix without such a rectangle is held fixed. We prove that the first selected row is invariant and classify every recurrent state: all nonfixed cycles have length two. Every entrance time is at most $2r-3$, and this bound is attained for every $r\ge2$ and $s\ge r+1$. The exact maximum for narrower boxes is not asserted. For each target, an exclusive-column prefix and row-containment test reconstruct every predecessor without running the full selector on candidate sources. The maximum fibre is $(r-1)(s-1)$, attained at exactly two targets except at $2$ by $2$, where all sixteen targets maximize. The local interchange, margin invariants, and lonesum fixed class are classical; the results concern the specified autonomous schedule.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Least Alternating-Rectangle Switching:\
  A Width-Uniform Tail Bound and Exact Predecessors
```

## Markdown 正文

# The literal scheduler and classical background

Fix $r,s\ge2$ and let $\mathcal X_{r,s}=\{0,1\}^{r\times s}$, with row indices $0,\ldots,r-1$ and column indices $0,\ldots,s-1$. Order rectangles $$q=(i,k,a,b),\qquad i<k,\quad a<b,$$ lexicographically in the displayed coordinate order. A rectangle is alternating when its selected submatrix is one of $$\begin{pmatrix}1&0\\0&1\end{pmatrix},
 \qquad
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.$$ Write $q(A)$ for the least alternating rectangle, when one exists, and $A^q$ for the matrix obtained by complementing its four entries. Define $$\label{eq:map}
 F(A)=
 \begin{cases}A^{q(A)},&q(A)\text{ exists},\\ A,&\text{otherwise}.\end{cases}$$ All entries outside the chosen rectangle remain unchanged. The rule is autonomous and deterministic on the full labelled carrier.

The move is Ryser's classical interchange [@ryser1957combinatorial Section 3]. Each changed row and column contains one zero and one one, so all margins are invariant. The fixed matrices are the classical lonesum matrices, equivalently those without an alternating rectangle; this characterization and the poly-Bernoulli census are background [@brewbaker2008combinatorial Section 1]. No new fixed-class counting result is claimed here. Baggett and Yan [@baggett2026interchange Section 2.1 and the proof of Lemma 5.10] study the full fixed-margin interchange graph using line fibres, quotients and compression. Their row-line fibres fix a row pattern, whereas the fibres below are preimages of the self-map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. The inspected compression chooses moves toward a prescribed basis, not the repeated least-current-rectangle update. This is a comparison with that specified preprint version, not a claim that the general interchange framework is new.

Let $A_i\subseteq\{0,\ldots,s-1\}$ be the support of row $i$. Two sets are comparable if one contains the other; write $P\mathrel{\|}Q$ for incomparability. For an incomparable row pair put $D=A_i\setminus A_k$ and $E=A_k\setminus A_i$. Its least alternating rectangle uses the two columns $\min D$ and $\min E$, sorted increasingly. Indeed every alternating rectangle chooses one element of each set, and this choice lexicographically minimizes the sorted pair. Thus [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} first chooses the least incomparable row pair. No rectangle exists exactly when all row supports form a containment chain.

For any finite map, let $\tau(A)$ denote the first time its orbit enters a directed cycle. The row geometry below gives an explicit recurrent criterion, a sharp bound on wide boxes, and a separate complete inverse.

# The invariant pivot and every recurrent state

[\[lem:pivot\]]{#lem:pivot label="lem:pivot"} Let $(i,k)$ be the least incomparable row pair of a nonfixed state. Along its entire orbit, the first index $i$ is constant and the least partner index $k$ is nonincreasing. A nonfixed state never maps to a fixed state.

For $h<i$, row $A_h$ is comparable with every row: otherwise some incomparable pair would have first index at most $h$. A set comparable with two incomparable sets $P,Q$ is either contained in $P\cap Q$ or contains $P\cup Q$. In fact the mixed alternatives $P\subseteq A_h\subseteq Q$ and $Q\subseteq A_h\subseteq P$ would make $P,Q$ comparable.

A switch preserves the intersection and union of its two changed row supports. Therefore every row before $i$ remains comparable with both, and with all unchanged rows. The changed rows are still incomparable, as the switched rectangle remains alternating. The first index stays $i$, and its least partner is at most the previous $k$. That surviving rectangle also prevents the output from being fixed. Apply the same argument at each subsequent epoch.

[\[thm:recurrent\]]{#thm:recurrent label="thm:recurrent"} Every cycle of $F$ has length one or two. A nonfixed matrix $A$ with least incomparable pair $(i,k)$ is recurrent if and only if the following two conditions hold. The first two columns $j<\ell$ where $A_i,A_k$ differ have opposite types, and $$\label{eq:recurrent}
 A_i\mathbin{\triangle}\{j,\ell\}\text{ is comparable with }A_h
 \quad\text{for every }i<h<k.$$ Here opposite types mean that exactly one of $j,\ell$ lies in $A_i\setminus A_k$, and $\triangle$ denotes symmetric difference. Every such nonfixed recurrent state has exact period two. Fixed states have their unique self-predecessor.

The selected rectangle remains alternating after its flip, so $q(F(A))\le q(A)$ in lexicographic order. If equality holds, the next step reverses the same four entries, giving $F^2(A)=A\ne F(A)$. If strict inequality holds, a return to $A$ is impossible, since the selector can never increase along a nonfixed orbit. Consequently a nonfixed state is recurrent exactly when its selector is unchanged. This also excludes cycles longer than two.

The set of differing columns in the selected row pair is unchanged by a switch. In their increasing order, mark each by which row contains it. The selected columns are the first difference and the first difference of the opposite type. If they are already the first two differences, interchanging their types leaves the column selector unchanged. Otherwise the second difference has the old first type, so after the switch it supplies an earlier opposite type and the column selector strictly decreases. Hence opposite first two differences are necessary and sufficient for the column part to stay unchanged.

Lemma [\[lem:pivot\]](#lem:pivot){reference-type="ref" reference="lem:pivot"} handles every possible earlier first-row index. With those two columns chosen, the row pair stays least precisely when the changed pivot is comparable with every intervening row, which is [\[eq:recurrent\]](#eq:recurrent){reference-type="eqref" reference="eq:recurrent"}. This proves the criterion. A fixed target cannot be the output of any switch by Lemma [\[lem:pivot\]](#lem:pivot){reference-type="ref" reference="lem:pivot"}; its only source is itself.

# A row bound attained on every wide box

[\[thm:tail\]]{#thm:tail label="thm:tail"} For every $r,s\ge2$ and $A\in\mathcal X_{r,s}$, $$\label{eq:bound}
 \tau(A)\le 2r-3 .$$ If a nonfixed orbit visits $p$ distinct partner rows at times $0,\ldots,\tau(A)$, and $i$ is its invariant pivot, then $\tau(A)\le2p-1$ and $p\le r-i-1$. For every $s\ge r+1$, $$\max_{A\in\mathcal X_{r,s}}\tau(A)=2r-3.$$ The last equality is asserted only in this wide regime.

Consider a consecutive stretch in which the same pair $(i,k)$ is selected. The positions of its differing columns stay fixed. The first switch swaps the first difference with the first opposite type. If the opposite type is already second, then either an earlier partner appears after the switch, or the starting state is already recurrent by Theorem [\[thm:recurrent\]](#thm:recurrent){reference-type="ref" reference="thm:recurrent"}.

If the first opposite type is later than second and this pair remains selected, its next switch uses the first two differences: the new first type is opposite to the unchanged second one. After that next switch, the pair's column selector cannot change again. Either an earlier partner appears, or the state just before that switch was already recurrent. Thus each partner appears at most twice among the selector states at times $0,\ldots,\tau(A)$, including the first recurrent state. By Lemma [\[lem:pivot\]](#lem:pivot){reference-type="ref" reference="lem:pivot"}, departed partners never reappear. Hence $$\tau(A)+1\le2p\le2(r-i-1)\le2(r-1).$$ A fixed state has $\tau=0$ and separately satisfies [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"}.

For sharpness, first use columns $0,\ldots,r$ and define $$\label{eq:witness}
 A_0=\{r\},\qquad
 A_k=\{0,k\}\cup\{k+2,\ldots,r\}
 \quad(1\le k\le r-1).$$ When $s>r+1$, every extra column is zero. The selected rectangles through the first recurrent state are, in the following order, $$\label{eq:itinerary}
 (0,k,0,k+1),\ (0,k,0,k)
 \qquad\text{for }k=r-1,r-2,\ldots,1.$$ To check the whole itinerary, at the start of partner $k$ the pivot is $\{k+1\}$. Every earlier row $h$ with $1\le h<k$ contains $k+1$, while row $k$ lacks it and has least exclusive element zero. The first switch sends the pivot to $\{0\}$ and row $k$ to $\{k,\ldots,r\}$. The earlier rows still contain the pivot, so the next selector uses columns $0,k$. This sends the pivot to $\{k\}$ and row $k$ to $\{0,k+1,\ldots,r\}$. For $k>1$, row $k-1$ is now the first row missing the pivot, while every row before it contains the pivot. This proves the induction.

At $k=1$ there is no intervening partner and the second selector in [\[eq:itinerary\]](#eq:itinerary){reference-type="eqref" reference="eq:itinerary"} has opposite first two differences, so that state is recurrent. Every earlier selector in the list strictly decreases at the next step, so no earlier state is recurrent. The list has $2r-2$ selector states, and therefore entrance time $2r-3$.

The row-first ordering is essential. Transposition exchanges the priority of row and column pairs and does not conjugate this scheduler to itself. In particular, the finite image counts at $3\times4$ and $4\times3$ differ (Table [1](#tab:checks){reference-type="ref" reference="tab:checks"}). No column bound is inferred by transposing [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"}; exact square or narrow maximum tails remain outside the proved assertion.

# Target-only inverse sets and sharp fibre equality

Let $Y$ be nonfixed and let $i$ be the first index of its least incomparable pair. Put $P=Y_i$. For every $k>i$ with $P\mathrel{\|}Y_k$, define $$D_k=P\setminus Y_k,\quad E_k=Y_k\setminus P,\quad
 j_k=\min(D_k\cup E_k).$$ Let $S_k$ be whichever of $D_k,E_k$ contains $j_k$, and $O_k$ the other set. With $\min\varnothing=s$, set $$\begin{aligned}
 b_k&=\min(S_k\setminus\{j_k\}),\nonumber\\
 \mathcal T_k(Y)&=\{\ell\in O_k:\ell<b_k,\
 P\triangle\{j_k,\ell\}\text{ is comparable with }Y_h
 \text{ for all }i<h<k\}. \label{eq:admissible}\end{aligned}$$ For other $k$ put $\mathcal T_k(Y)=\varnothing$. Since $j_k$ is the first difference, every candidate $\ell$ exceeds $j_k$. The interval part of [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"} is simply the initial run of opposite-type differences after $j_k$, stopped by the next same-type difference.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} For every nonfixed target $Y$, its entire inverse set is $$\label{eq:inverse}
 F^{-1}(Y)=
 \{Y^{(i,k,j_k,\ell)}: k>i,\ \ell\in\mathcal T_k(Y)\},
 \qquad
 |F^{-1}(Y)|=\sum_{k>i}|\mathcal T_k(Y)|.$$ There is no repetition in this set. A fixed target has only its self-source. Thus $Y\in\operatorname{im}F$ if and only if it is fixed or some $\mathcal T_k(Y)$ is nonempty. The test uses only target differences and containments, without running the full selector on reconstructed sources.

Any nonfixed source has the same first pivot as its image by Lemma [\[lem:pivot\]](#lem:pivot){reference-type="ref" reference="lem:pivot"}. Its switched rows remain incomparable in the target. Fix such a target pair and abbreviate its exclusive sets by $D,E$. Reverse a candidate rectangle using $a\in D$, $b\in E$. The source exclusive sets become $(D\setminus\{a\})\cup\{b\}$ and $(E\setminus\{b\})\cup\{a\}$. That rectangle is the least within this source row pair exactly when $$\label{eq:minima}
 b<\min(D\setminus\{a\}),\qquad
 a<\min(E\setminus\{b\}).$$ Here the same sentinel $s$ is valid for an empty remainder. If $a<b$, the two inequalities force $a$ to be the first target difference and $b$ to precede the next difference in $D$. Conversely those conditions imply both inequalities, because all other elements of $E$ exceed the first difference $a$. The case $b<a$ is the same argument with $D,E$ interchanged. This proves precisely the interval condition in [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"}.

Every row before $i$ is comparable with all target rows. Applying the intersection/union argument of Lemma [\[lem:pivot\]](#lem:pivot){reference-type="ref" reference="lem:pivot"} to the inverse switch shows that no earlier first pivot appears. Among pairs with first index $i$, all partners before $k$ are unchanged, so their comparability with the reconstructed pivot is exactly the remaining condition in [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"}. These conditions are necessary and sufficient for the reconstructed source to select the specified rectangle. Different $k,\ell$ flip different four-entry sets and hence produce different matrices. The fixed-target assertion was proved in Theorem [\[thm:recurrent\]](#thm:recurrent){reference-type="ref" reference="thm:recurrent"}.

[\[thm:maximum\]]{#thm:maximum label="thm:maximum"} For all $r,s\ge2$, $$\max_{Y\in\mathcal X_{r,s}}|F^{-1}(Y)|=(r-1)(s-1).$$ Except when $(r,s)=(2,2)$, exactly two targets attain this maximum: the matrix with supports $$\label{eq:maximizers}
 (\{0\},\,\{1,\ldots,s-1\},\,\ldots,\,\{1,\ldots,s-1\})$$ and its entrywise complement. At $2\times2$, all sixteen matrices have fibre one and maximize.

There are at most $r-i-1$ partner terms in [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"}, each with at most $s-1$ columns. A fixed target has fibre one, so the displayed product is an upper bound. For [\[eq:maximizers\]](#eq:maximizers){reference-type="eqref" reference="eq:maximizers"}, each partner has $j_k=0$, $S_k=\{0\}$ and $O_k=\{1,\ldots,s-1\}$. Reconstructing with any $\ell\in O_k$ gives pivot $\{\ell\}$, contained in every intervening row. All $(r-1)(s-1)$ choices are admissible. Entrywise complement preserves alternating rectangles and their lexicographic order, so it commutes with $F$ and gives the other target.

Suppose $(r-1)(s-1)>1$ and equality holds. The target is nonfixed, $i=0$, and every partner contributes exactly $s-1$ columns. Since $\mathcal T_k\subseteq O_k$, this forces $|O_k|=s-1$ and $S_k=\{j_k\}$, with all columns differing. The minimum difference is therefore $j_k=0$. Thus $P$ and every other row are complements, with $P$ either $\{0\}$ or $\{1,\ldots,s-1\}$. The fixed pivot support chooses the same alternative for all partners, leaving only the two targets stated. Finally, at $2\times2$ the sole rectangle exchanges its two alternating matrices and the other fourteen matrices hold. The map is a bijection, so all fibres equal one.

# Exact checks and the remaining boundary

The paper-local verifier enumerates column-major binary matrices and scans the four literal rectangle entries. Complete functional graphs give tails and periods by indegree peeling and cycle extraction. A separate target-prefix construction is compared with every complete graph predecessor set. It also checks pivot invariance, partner descent, the two-visits bound, all maximizing targets, and margin preservation. Two fresh executions agree byte for byte: each exhausts thirteen boxes, 273,040 states, and 3,595,488 assertions. An additional thirty-eight wide witnesses use $r=2,\ldots,20$ and widths $r+1,r+5$, checking the entire itinerary [\[eq:itinerary\]](#eq:itinerary){reference-type="eqref" reference="eq:itinerary"}, not only its final tail length.

::: {#tab:checks}
   $(r,s)$    states   image   fixed   max. tail   max. fibre
  --------- -------- ------- ------- ----------- ------------
   $(2,2)$        16      16      14           0            1
   $(3,3)$       512     456     230           2            4
   $(3,4)$      4096    3292    1066           3            6
   $(4,3)$      4096    3290    1066           3            6
   $(4,4)$     65536   47114    6902           4            9

  : Selected complete boxes. Finite maximum tails in square or narrow boxes are data, not an all-size sharpness theorem.
:::

The proofs concern row-support geometry coupled to the specified least-rectangle schedule. Classical interchanges, fixed-margin connectivity and lonesum enumeration remain fully credited. The internal comparison also subtracts the earlier randomized two-switch and generic least-defect/inverse-admissibility methodology; merely choosing a deterministic scheduler is not the asserted progress. The external owner screen was bounded, and historical manuscripts P51--P56 were unavailable. There is no priority or publication-readiness claim. The exact square/narrow tail maximum and an all-time inverse atlas are not proved here. The manuscript remains `HOLD_EXTERNAL`; finite controls do not replace the separate paper-review and owner-assessment processes.
