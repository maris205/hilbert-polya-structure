---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--165-low-weight-support-shortening"
canonical_tex: "symbolic_dynamics/papers/165-low-weight-support-shortening/main.tex"
canonical_pdf: "symbolic_dynamics/papers/165-low-weight-support-shortening/main.pdf"
source_sha256: "bf245d0d0e968edf921af76bae15a77fc8068c3e196b0e880f48ec2a4e3275e4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Iterated Low-Weight Support Shortening of Finite Linear Codes

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/165-low-weight-support-shortening>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/165-low-weight-support-shortening/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/165-low-weight-support-shortening/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/165-low-weight-support-shortening/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/165-low-weight-support-shortening/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix a prime power $q$ and keep the coordinates of $\mathbb F_q^n$ labelled. From a nonzero linear code $C$, take the union of the supports of all words whose weight is strictly below twice the minimum distance, and shorten $C$ on that union, padding the removed coordinates by zeros. Iterating this state-dependent operation gives a finite descending dynamics. After assigning zero contribution credit to the one-step low-weight hitting-set shortening principle, we determine the residual temporal and inverse structure. Minimum distance at least doubles at every nonzero step, zero is the unique recurrent state, and the sharp height is $\lfloor\log_2(n+1)\rfloor$. A prescribed nonzero target $D$ occurs at time $t$ exactly when $d(D)\geq2^t$ and it has at least $2^t-1$ zero coordinates. Every such preimage needs at least $t$ new dimensions and $2^t-1$ newly supported coordinates. We classify and count precisely the preimages attaining both bounds; we do not count the complete fibre. An exact paper-local audit checks all binary codes through length seven and codes over three further finite fields in smaller boxes.
author:
- Anonymous
bibliography:
- references.bib
title: 'Iterated Low-Weight Support Shortening of Finite Linear Codes'
```

## Markdown 正文

# Literal map and contribution boundary

Let $q$ be a prime power, write $[n]=\{1,\ldots,n\}$, and let $C\leq\mathbb F_q^n$ be a labelled linear code. For $C\ne0$, put $$\begin{aligned}
 d(C)&=\min\{\operatorname{wt}(c):0\ne c\in C\},\\
 L(C)&=\{c\in C:0<\operatorname{wt}(c)<2d(C)\},\\
 U(C)&=\bigcup_{c\in L(C)}\operatorname{supp}(c),\\
 T(C)&=\{c\in C:c_j=0\text{ for every }j\in U(C)\},\end{aligned}$$ and set $T(0)=0$. Coordinates in $U(C)$ remain present and are forced to zero. Thus $T$ is a padded shortening self-map on the subspaces of one fixed ambient space; it is not puncturing. The strict inequality in the definition of $L(C)$ is part of the map.

Shortening and puncturing are standard coding-theory operations. Grassl and White use low-weight support information for special puncturings [@GrasslWhite2004]. More directly, Jibril et al. construct hitting sets for low-weight words and prove distance-increasing shortening statements [@JibrilEtAl2013]. Taking their distance parameter up to $2d-1$ contains the one-step route used here. We therefore assign zero contribution credit to that entire hitting-set shortening principle, including the fact that the surviving minimum distance is at least $2d$. The residual studied below is the autonomous iteration, its sharp clock, the all-time image criterion, and the extremal target-preimage atlas.

Write $$\operatorname{Supp}(C)=\bigcup_{c\in C}\operatorname{supp}(c),\qquad
 z(C)=n-|\operatorname{Supp}(C)|,
 \qquad s_t=2^t-1,$$ and let $\tau(C)=\min\{t\geq0:T^t(C)=0\}$. In particular, $\tau(0)=0$. Sources and targets are labelled subspaces, not generator matrices or equivalence classes.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For every prime power $q$, every $n\geq0$, and the map $T$ above, the following statements hold.

(A) If $C\ne0$, then $T(C)$ is a proper subcode. If also $T(C)\ne0$, then $$\label{eq:doubling}
     d(T(C))\geq2d(C).$$ Zero is the unique recurrent state, and $$\label{eq:height}
     \max_{C\leq\mathbb F_q^n}\tau(C)=\lfloor\log_2(n+1)\rfloor.$$

(B) Let $D\ne0$ and $t\geq0$. Then $$\label{eq:image}
     D\in\operatorname{im}(T^t)
     \quad\Longleftrightarrow\quad
     d(D)\geq2^t\ \text{ and }\ z(D)\geq s_t.$$

(C) If $D\ne0$ and $T^t(C)=D$, then $$\label{eq:lower}
     \dim C-\dim D\geq t,
     \qquad
     |\operatorname{Supp}(C)\setminus\operatorname{Supp}(D)|\geq s_t.$$ When [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} holds, simultaneous equality in [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"} is attained precisely as follows. Choose pairwise disjoint sets $$\label{eq:blocks}
     B_i\subseteq[n]\setminus\operatorname{Supp}(D),\qquad |B_i|=2^i
     \quad(0\leq i<t),$$ choose on each $B_i$ a full-support one-dimensional code $M_i$, and set $$\label{eq:source}
     C=D\oplus M_0\oplus\cdots\oplus M_{t-1}.$$ The number of these simultaneous extremizers is $$\label{eq:count}
     \frac{z(D)!}{(z(D)-s_t)!\prod_{i=0}^{t-1}(2^i)!}
     (q-1)^{s_t-t}.$$ Empty products make [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"} equal to one at $t=0$.

Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}(C) classifies only the slice attaining both lower bounds. Formula [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"} is not a formula for the complete fibre.

# Dyadic descent and the sharp clock

Let $C_i=T^i(C)$ and, while $C_i\ne0$, abbreviate $d_i=d(C_i)$ and $U_i=U(C_i)$.

[\[lem:budget\]]{#lem:budget label="lem:budget"} If $C_0,\ldots,C_{r-1}$ are nonzero, then the sets $U_0,\ldots,U_{r-1}$ are pairwise disjoint and $$\label{eq:budget}
 |U_i|\geq d_i\geq2^i.$$ Moreover, every nonzero transition has positive codimension.

A minimum-weight word of $C_i$ lies in $L(C_i)$, so $U_i$ is nonempty and that word does not survive the shortening. Hence $C_{i+1}$ is a proper subcode. Every nonzero word of $C_{i+1}$ is zero on $U_i$; if its weight were below $2d_i$, it would itself belong to $L(C_i)$ and its nonempty support would be contained in $U_i$, a contradiction. This proves [\[eq:doubling\]](#eq:doubling){reference-type="eqref" reference="eq:doubling"}. All later codes are zero on $U_i$, so later purge sets avoid it. Finally a minimum word has $d_i$ coordinates inside $U_i$, and repeated use of [\[eq:doubling\]](#eq:doubling){reference-type="eqref" reference="eq:doubling"} gives $|U_i|\geq d_i\geq2^id_0\geq2^i$.

If $\tau(C)=r$, Lemma [\[lem:budget\]](#lem:budget){reference-type="ref" reference="lem:budget"} gives $$n\geq\sum_{i=0}^{r-1}|U_i|
 \geq\sum_{i=0}^{r-1}2^i=2^r-1,$$ which proves the upper bound in [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"} and rules out every nonzero cycle. For sharpness, put $r=\lfloor\log_2(n+1)\rfloor$. Choose disjoint blocks $B_i$ of sizes $2^i$ and take the direct sum of full-support lines on those blocks. At stage $i$, the unique low-weight summand is the line on $B_i$: later blocks have weight at least $2^{i+1}$ and disjoint supports make mixed-word weights additive. The blocks disappear in order, so the depth is $r$. This also covers $r=0$ by the empty direct sum.

# Every-time images

Suppose $T^t(C)=D\ne0$. Each intermediate code is nonzero. Iterating [\[eq:doubling\]](#eq:doubling){reference-type="eqref" reference="eq:doubling"} gives $d(D)\geq2^td(C)\geq2^t$. The sets $U_0,\ldots,U_{t-1}$ are disjoint zero coordinates of $D$, and Lemma [\[lem:budget\]](#lem:budget){reference-type="ref" reference="lem:budget"} gives $$z(D)\geq\sum_{i=0}^{t-1}|U_i|\geq s_t.$$ This proves necessity in [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

Conversely, assume the two conditions in [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. There is room among the zero coordinates of $D$ for blocks as in [\[eq:blocks\]](#eq:blocks){reference-type="eqref" reference="eq:blocks"}. Construct $C$ by [\[eq:source\]](#eq:source){reference-type="eqref" reference="eq:source"}. At time $i$ the current code is $$D\oplus M_i\oplus\cdots\oplus M_{t-1}$$ and has distance $2^i$. Its words of weight strictly below $2^{i+1}$ are exactly the nonzero words of $M_i$: a later line has weight at least $2^{i+1}$, a nonzero target word has weight at least $2^t$, and components on disjoint supports cannot cancel. Therefore the next shortening removes exactly $M_i$. After $t$ steps the target is $D$, proving sufficiency.

# The extremal inverse layer

For a source in Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}(C), every transition is a proper subspace inclusion, so the $t$ codimension drops sum to at least $t$. Also $U_0\sqcup\cdots\sqcup U_{t-1}$ lies in $\operatorname{Supp}(C)\setminus\operatorname{Supp}(D)$. Lemma [\[lem:budget\]](#lem:budget){reference-type="ref" reference="lem:budget"} proves both lower bounds in [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"}.

Suppose both bounds are equalities. Every step then has codimension one, and equality in the support budget forces $$\label{eq:forced}
 |U_i|=d_i=2^i\qquad(0\leq i<t).$$ Choose a minimum word $w_i\in C_i$. Its support lies in $U_i$ by the definition of $U_i$, while [\[eq:forced\]](#eq:forced){reference-type="eqref" reference="eq:forced"} says that both sets have the same size. Thus $\operatorname{supp}(w_i)=U_i$: this is a word supported purely on the purge block, not merely a lift modulo $C_{i+1}$. Since $C_{i+1}$ is the kernel of restriction to $U_i$ and has codimension one, $$C_i=C_{i+1}\oplus\operatorname{span}(w_i).$$ Descending through the times proves the decomposition [\[eq:source\]](#eq:source){reference-type="eqref" reference="eq:source"}. This argument also excludes cancellation between a purge line and later layers. The converse was established by the image construction.

It remains to count. The number of ordered disjoint labelled blocks of sizes $2^0,\ldots,2^{t-1}$ selected from $z(D)$ coordinates is $$\frac{z(D)!}{(z(D)-s_t)!\prod_{i=0}^{t-1}(2^i)!}.$$ A labelled block of size $m$ supports $(q-1)^{m-1}$ full-support lines: there are $(q-1)^m$ full-support vectors and $q-1$ nonzero representatives of each line. Multiplication over the $t$ blocks contributes $(q-1)^{s_t-t}$ and proves [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"}.

# Boundary audit and exact controls

The boundary conventions prevent several false readings of the theorem. If $n=0$, zero is the only code and the height is zero. For $t=0$, every nonzero target satisfies [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}, and its sole simultaneous extremizer is itself. The zero target belongs to every time image, using itself as a source, but its complete fibre is $$(T^t)^{-1}(0)=\{C:\tau(C)\leq t\},$$ not the extremal count [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"}. Among codes of exact depth $t\geq1$, the minimum dimension and support are respectively $t$ and $s_t$; their simultaneous minimizers have the same block form and are counted by [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"} with $z(D)$ replaced by $n$. This exact-depth statement is not the full fibre.

A nonzero full-support target has $z(D)=0$ and hence no positive-time preimage. If $2^t-1>n$, the positive part of the time-$t$ image is empty, although zero remains. Replacing the strict inequality $\operatorname{wt}(c)<2d(C)$ by a weak one removes a block of weight $2d(C)$ one stage too early and changes the atlas. The proofs use only finite-field linear algebra, so they include nonprime prime powers. No efficient algorithm is claimed: computing a code's minimum distance is intractable in general [@Vardy1997].

The paper-local verifier starts from the literal padded shortening map. It enumerates every binary code through $n=7$, every ternary code through $n=4$, and every code through $n=3$ over $\mathbb F_4$ and $\mathbb F_5$. It checks pointwise descent, exact heights, all targets in each tested time image, both preimage lower bounds, the simultaneous-equality classification and count, and dedicated statement sentinels for all boundaries above. These finite checks are counterexample pressure, not an all-parameter proof or an ownership test.

The direct-owner search was bounded. A non-hit is not evidence of novelty, and no claim of priority or absolute novelty is made. External posting, circulation, submission, or author contact remains `HOLD_EXTERNAL`.

## Data, ethics, and conflict statement {#data-ethics-and-conflict-statement .unnumbered}

No external dataset, training data, human subjects, or animals are involved. The deterministic exact verifier and frozen transcript accompany the note. The anonymous author declares no conflict of interest.
