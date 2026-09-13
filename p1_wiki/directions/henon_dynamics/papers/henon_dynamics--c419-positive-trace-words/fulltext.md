---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c419-positive-trace-words"
canonical_tex: "henon_dynamics/research_c419_c423/papers/C419_positive_trace_words/main.tex"
canonical_pdf: "henon_dynamics/research_c419_c423/papers/C419_positive_trace_words/main.pdf"
source_sha256: "e034a05eb06d2643847b55c4068bf1635ed477c124e1fb4a44913e28be5ee7c5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Integer periodicity of positive trace-map words

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c419_c423/papers/C419_positive_trace_words>)
- [规范 TeX](<../../../../../henon_dynamics/research_c419_c423/papers/C419_positive_trace_words/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c419_c423/papers/C419_positive_trace_words/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c419_c423/papers/C419_positive_trace_words/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c419_c423/papers/C419_positive_trace_words/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify ordinary integer periodic points uniformly over all positive words containing both trace maps $A(x,y,z)=(x,z,xz-y)$ and $B(x,y,z)=(z,y,yz-x)$. The union of their periodic loci is exactly 39 explicit affine lines together with four points; every point in this set is in fact fixed by some positive word. On each integer level of the invariant $K=x^2+y^2+z^2-xyz$, the universal candidate set has at most 40 points. Exact quadratic root tests and partial permutations on these points give the complete ordinary cycle structure of every word, retaining all intermediate letter phases. The possible nonempty levels lie in the three families $m^2$, $m^2+1$ and $m^2-m+2$. Every nonperiodic integer point tends to infinity in both forward and backward word time. The proof combines a common escape cone, integral descent, finite rotations at small coordinates and explicit positive-word realization of the resulting lines. The generator formulas and general trace-map escape mechanisms are classical; the contribution is their exact direction-sensitive integer exhaustion for the whole positive-word family. The bound 40 is not asserted to be an attained least period.
bibliography:
- references.bib
date: 'September 8, 2026'
title: 'Integer periodicity of positive trace-map words'
```

## Markdown 正文

# An exact universal integer locus {#sec:intro}

Periodicity for one trace-map word is different from finiteness of an entire group orbit. An integer point can be fixed by a positive word whose substitution matrix is hyperbolic and still escape under another positive word. We determine the exact union of these single-word periodic loci and use it to classify each individual word.

Let $$\label{eq:maps}
 A(x,y,z)=(x,z,xz-y),\qquad B(x,y,z)=(z,y,yz-x),
 \qquad K(x,y,z)=x^2+y^2+z^2-xyz.$$ A word $w=\ell_1\cdots\ell_s$ is *admissible* if each $\ell_i\in\{A,B\}$ and both letters occur. The notation is chronological: $$\label{eq:clock}
 W=\ell_s\circ\cdots\circ\ell_1,\qquad
 P,\ W(P),\ W^2(P),\ldots .$$ One application of $W$, not one letter or one substitution length, is the ordinary time step. In particular $AB$ means $B\circ A$.

Put $C=\{-1,0,1\}$ and define $$\label{eq:locus}
 \begin{aligned}
 \mathcal D_0&=\{(t,a,b),(a,t,b),(a,b,t):t\in\mathbb Z,\ a,b\in C\},\\
 \mathcal D_x&=\{(c,t,ct+b):t\in\mathbb Z,\ c\in\{-1,1\},\ b\in C\},\\
 \mathcal D_y&=\{(t,c,ct+b):t\in\mathbb Z,\ c\in\{-1,1\},\ b\in C\},\\
 \mathcal D&=\mathcal D_0\cup\mathcal D_x\cup\mathcal D_y,\\
 \mathcal E&=\{(2\epsilon,2\eta,2\epsilon\eta):
                  \epsilon,\eta\in\{-1,1\}\}.
 \end{aligned}$$ Here a line means its set of integer points. The line collections have respectively $27,6,6$ distinct members. Lines may intersect as sets of points. For $k\in\mathbb Z$ set $$\label{eq:Xk}
 X_k=(\mathcal D\cup\mathcal E)\cap\{K=k\}.$$

[\[thm:main\]]{#thm:main label="thm:main"} For the maps [\[eq:maps\]](#eq:maps){reference-type="eqref" reference="eq:maps"}, the following assertions hold.

1.  For every admissible word, every integer periodic point of $W$ belongs to $\mathcal D\cup\mathcal E$. Every intermediate letter phase of a periodic orbit belongs to the same set.

2.  Every point of $\mathcal D\cup\mathcal E$ is fixed by some admissible word. Consequently $$\bigcup_w\mathop{\mathrm{Fix}}(W;\mathbb Z^3)=\bigcup_w\mathop{\mathrm{Per}}(W;\mathbb Z^3)=\mathcal D\cup\mathcal E.$$

3.  For every integer $k$, $|X_k|\le40$, and $X_k$ is empty unless $$k\in\{m^2,\ m^2+1,\ m^2-m+2:m\in\mathbb Z\}.$$ The quadratic-root and partial-permutation algorithm of Section [6](#sec:classifier){reference-type="ref" reference="sec:classifier"} gives every ordinary cycle for every admissible word on every level. In particular every least period is at most $40$.

4.  If an integer point $P$ is not periodic for an admissible $W$, then $\left\lVert W^n(P)\right\rVert_\infty\to\infty$ and $\left\lVert W^{-n}(P)\right\rVert_\infty\to\infty$ as $n\to\infty$.

The union in the theorem is existential over words. It is not the set periodic under every group element. Nor does the candidate bound assert a word with 40 periodic points or a 40-cycle. The exact word-dependent cycles, rather than such an unproved sharpness claim, are the output of the algorithm.

## Classical inputs and the residual question

The trace-map structure, invariant and reversible substitutions are classical [@RobertsBaake1994]. The exact displayed generators appear in full-trace coordinates in @SasakiYoshida2008 [Section 2.1], together with their iterate formulas and conic dynamics. General infinite-order trace-map escape methods already occur in @Roberts1996. Our cone arguments below are proved directly and are not offered as the introduction of escape theory for general words.

Character-variety group dynamics [@CantatLoray2009], finite whole-group orbits [@Humphries2016], and integer Markoff group descent [@GhoshSarnak2022] address neighboring but different quantifiers. The difference is exhibited by an explicit fixed-line/escaping-word calculation in Section [2.1](#sec:separators){reference-type="ref" reference="sec:separators"}; it is not inferred only from titles. The entire integer classification for the single Fibonacci trace map in the predecessor manuscript [@C413] is also deducted. The present family includes a new level family and words that are not powers of that map.

::: {#tab:sources}
  Prior framework                          Deducted content                                                Additional question here
  ---------------------------------------- --------------------------------------------------------------- ---------------------------------------------------------------------------
  Trace substitutions and conic dynamics   Maps, invariant, matrix correspondence, small-trace rotations   Exact integer locus for every positive word.
  General trace-map escape                 Escape criteria and mechanisms for broad word classes           Integral boundary descent and the full 39-line exhaustion.
  Markoff/character group actions          Group-orbit structure and descent                               Periodicity under one specified word, with the word arbitrary.
  Single Fibonacci map                     Its complete integer periodic classification                    All positive two-twist words, including the $m^2+1$ level family.
  Finite partial permutations              Cycle traces and determinant products                           The exact, uniformly bounded arithmetic state space on which to use them.

  : Source subtraction. The first column refers to the primary works discussed in the introduction; no new ownership of these classical mechanisms is asserted.
:::

The proof proceeds from a common cone and complete integral descent in Section [3](#sec:escape){reference-type="ref" reference="sec:escape"} to the small-coordinate rotation argument and converse in Section [4](#sec:locus){reference-type="ref" reference="sec:locus"}. Exact level intersections in Section [5](#sec:levels){reference-type="ref" reference="sec:levels"} produce the finite classifier. Section [7](#sec:twosided){reference-type="ref" reference="sec:twosided"} proves proper two-sided escape. All these arguments are included; no external theorem is a hidden premise for the integer exhaustion.

# Coordinates, reversibility and separating examples {#sec:conventions}

Direct substitution gives $$\label{eq:inverses}
 A^{-1}(x,y,z)=(x,xy-z,y),\qquad
 B^{-1}(x,y,z)=(xy-z,y,x).$$ Both are integer polynomial automorphisms. The invariant identity for the first is $$K(A(x,y,z))=x^2+z^2+(xz-y)^2-xz(xz-y)=K(x,y,z).$$ The coordinate exchange $J(x,y,z)=(y,x,z)$ satisfies $JAJ=B$ and $JBJ=A$, and preserves $K$. It proves the other identity. We will use this exact conjugacy whenever the first and second coordinate cases are interchanged.

For determinant-one matrices $X,Y$, use the full traces $x=\mathop{\mathrm{tr}}X$, $y=\mathop{\mathrm{tr}}Y$, $z=\mathop{\mathrm{tr}}(XY)$. Cayley--Hamilton gives $\mathop{\mathrm{tr}}(X^2Y)=xz-y$ and $\mathop{\mathrm{tr}}(XY^2)=yz-x$. The corresponding pair substitutions are $(X,Y)\mapsto(X,XY)$ and $(X,Y)\mapsto(XY,Y)$. With rows for exponent vectors, $$\label{eq:matrices}
 R_A=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
 R_B=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 R_w=R_{\ell_s}\cdots R_{\ell_1}.$$ These are the same lower/upper unipotent generators as in @SasakiYoshida2008, with the stated order convention. An adjacent pair of distinct letters has trace three. Multiplication on either side by a nonnegative elementary unipotent cannot decrease any entry. Thus every admissible product has determinant one and trace at least three, so its eigenvalues are positive reciprocal numbers, one greater than one. This is a matrix statement, not uniform hyperbolicity of every real surface orbit.

The four points $\mathcal E$ already form an invariant finite set. Writing a point by its signs $(\epsilon,\eta)$ as in [\[eq:locus\]](#eq:locus){reference-type="eqref" reference="eq:locus"}, the letter actions are $$\label{eq:E}
 A:(\epsilon,\eta)\mapsto(\epsilon,\epsilon\eta),\qquad
 B:(\epsilon,\eta)\mapsto(\epsilon\eta,\eta).$$ Each has square the identity there. In particular a point outside $\mathcal E$ cannot enter $\mathcal E$ under either bijection.

## Why the group and predecessor results do not suffice {#sec:separators}

The powers $A^6$ and $B^6$ are identities on the planes $x=1$ and $y=1$, respectively, as also follows from the explicit rotations in Section [4](#sec:locus){reference-type="ref" reference="sec:locus"}. Hence the conventional composition $A^6\circ B^6$ fixes $(1,1,m)$ for every $m\in\mathbb Z$. Its exponent matrix is $$R_A^6R_B^6=\begin{pmatrix}1&6\\6&37\end{pmatrix}.$$ In contrast, $$\label{eq:groupseparator}
 (A\circ B)(1,1,m)=(m,m-1,m^2-m-1)$$ belongs to the forward escape cone defined below whenever $m\ge3$. The whole-group orbit is therefore infinite. Finite-group-orbit classifications cannot supply the periodic locus of this word. Half-trace sources such as @RobertsBaake1994 and @Humphries2016 also require doubling coordinates; an integer lattice in half traces is not the full integer lattice used here.

For the chronological word $ABB$, namely $B^2\circ A$, direct application of its letters gives the four-cycle $$\label{eq:ABB}
 (1,m,m),\quad(-1,m,-m),\quad(1,-m,-m),\quad(-1,-m,m)
 \qquad(m\in\mathbb Z\setminus\{0\}).$$ The four triples are distinct and have level $m^2+1$. For $|m|\ge2$ this level family is absent from the predecessor's Fibonacci-map periodic levels, which are of the forms $n^2$ and $n^2-n+2$ [@C413]. The matrix for $ABB$ has trace four. Even positive powers of the Fibonacci matrix have traces $3,7,18,\ldots$, strictly increasing; odd powers have determinant minus one. Thus this is not merely a power of that single map. Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} treats the entire admissible family, not only the separating example.

# A common escape cone and integral descent {#sec:escape}

For $P=(x,y,z)$ write $\left\lVert P\right\rVert_\infty=\max(|x|,|y|,|z|)$ and put $$\label{eq:domains}
 \begin{aligned}
 \mathcal S&=\{P\in\mathbb Z^3:\min(|x|,|y|,|z|)\le1\},\\
 \mathcal C_+&=\{P\in\mathbb Z^3:|x|,|y|\ge2,\
 |z|\ge\max(|x|,|y|),\ |z|>2,\ xyz>0\}.
 \end{aligned}$$ Both sets are invariant under the coordinate exchange $J$. The gap between integer absolute values at most one and at least two is used essentially in the following arguments.

[\[lem:cone\]]{#lem:cone label="lem:cone"} Each letter maps $\mathcal C_+$ into itself. Along any infinite letter sequence in which both letters occur infinitely often, a starting point in $\mathcal C_+$ has third-coordinate modulus tending to infinity.

Put $(a,b,c)=(|x|,|y|,|z|)$. Since $xyz>0$, the numbers $xz$ and $y$ have the same sign. Under $A$ the third modulus is $ac-b>0$, and $$ac-b\ge ac-c=(a-1)c\ge c.$$ The first two new moduli are $a,c$, and their product with the new third coordinate is positive. Thus the image lies in $\mathcal C_+$. Equality $ac-b=c$ requires and is equivalent to $a=2$, $b=c$. Applying $J$ gives the $B$ statement, with equality exactly when $b=2$, $a=c$.

The successive third moduli are nondecreasing integers. If bounded, they eventually equal a fixed $c>2$. A late $A$ step then forces the absolute triple $(2,c,c)$ and leaves it unchanged. Any intervening $A$ steps do the same. The next $B$ step gives third modulus $c^2-2>c$, a contradiction. Such a later $B$ exists by hypothesis. Hence the moduli tend to infinity.

[\[lem:descent\]]{#lem:descent label="lem:descent"} A forward letter trajectory outside $\mathcal E$ that never enters $\mathcal C_+$ reaches $\mathcal S$ after finitely many steps.

While the trajectory is outside $\mathcal S$, all three moduli $a,b,c$ are at least two. If $xyz<0$, the new third modulus is $ac+b$ under $A$ and $bc+a$ under $B$; either image has positive product and belongs to $\mathcal C_+$. Thus this case cannot persist on the stipulated trajectory.

Suppose $xyz>0$. If $c\ge\max(a,b)$, the point is in $\mathcal C_+$ unless $a=b=c=2$, in which case it belongs to $\mathcal E$. Both alternatives are excluded. If $a=b>c$, either letter gives third modulus $a(c-1)\ge a>2$ and enters the cone.

It remains, after possibly applying $J$, that $a>\max(b,c)$. An $A$ step gives $ac-b>a(c-1)\ge a$ and enters the cone. For a $B$ step let $d=bc-a$ be the signed new magnitude relative to the sign of $x$. There are four exhaustive possibilities:

1.  If $d\le-2$, the image has all moduli at least two and negative product; the following letter enters the cone.

2.  If $-1\le d\le1$, the image belongs to $\mathcal S$.

3.  If $d\ge\max(b,c)$, the image belongs to the cone unless $b=c=d=2$. That exceptional image would be in $\mathcal E$, which has no preimage outside $\mathcal E$ by [\[eq:E\]](#eq:E){reference-type="eqref" reference="eq:E"}.

4.  Otherwise $2\le d<\max(b,c)<a$, and the new maximum is strictly smaller than the old maximum $a$.

The strict second-coordinate maximum is exactly the conjugate case under $J$, with $A$ and $B$ exchanged. Thus, as long as the stipulated trajectory remains outside $\mathcal S$, the only surviving case is strict descent of a positive integer maximum. It cannot continue indefinitely.

[\[lem:exit\]]{#lem:exit label="lem:exit"} If $P\in\mathcal S$ and either letter takes $P$ outside $\mathcal S$, its image belongs to $\mathcal C_+$.

For $A$, such an exit requires $|x|,|z|\ge2$ and $|y|\le1$. The product $xz$ strictly dominates $y$, so the image has positive coordinate product and $$|xz-y|\ge |x||z|-1>\max(|x|,|z|),\qquad |xz-y|\ge3.$$ These are the cone inequalities. The $B$ case follows by $J$.

[\[cor:periodicsmall\]]{#cor:periodicsmall label="cor:periodicsmall"} Every letter phase in the expansion of a periodic admissible word orbit lies either in $\mathcal E$ or in $\mathcal S$. In the latter case no phase has the third coordinate as its only small coordinate.

Expand the ordinary word cycle into all chronological letter phases. This is a finite repeating trajectory whose schedule contains both letters. Lemma [\[lem:cone\]](#lem:cone){reference-type="ref" reference="lem:cone"} excludes the cone. If one phase is in $\mathcal E$, all are, by invariance and bijectivity. Otherwise Lemma [\[lem:descent\]](#lem:descent){reference-type="ref" reference="lem:descent"} forces any all-large phase to reach $\mathcal S$, which cannot subsequently be left by Lemma [\[lem:exit\]](#lem:exit){reference-type="ref" reference="lem:exit"}. A finite repeating trajectory therefore has all its phases in $\mathcal S$.

If $|x|,|y|\ge2$ and $|z|\le1$, both possible predecessor phases in [\[eq:inverses\]](#eq:inverses){reference-type="eqref" reference="eq:inverses"} are outside $\mathcal S$: $$|xy-z|\ge |x||y|-1\ge3.$$ Such a phase cannot occur. This directional predecessor constraint is essential to the precise line count.

# The 39 lines and their positive-word realization {#sec:locus}

[\[prop:cover\]]{#prop:cover label="prop:cover"} Every periodic letter phase outside $\mathcal E$ belongs to $\mathcal D$.

By Corollary [\[cor:periodicsmall\]](#cor:periodicsmall){reference-type="ref" reference="cor:periodicsmall"} the phase has a small coordinate. If two coordinates are small, it is in $\mathcal D_0$. If exactly one is small, it cannot be the third. Suppose it is $x=c\in C$, so $|y|,|z|\ge2$. Repeated applications of $A$ transform the last two coordinates by $$M_c=\begin{pmatrix}0&1\\-1&c\end{pmatrix}.$$ Direct multiplication gives $$\label{eq:rotations}
 M_0^4=I,\qquad M_1^3=-I,\qquad M_1^6=I,\qquad
 M_{-1}^3=I.$$ The encountered absolute coordinate values lie in $$\begin{cases}
 \{|y|,|z|\},&c=0,\\
 \{|y|,|z|,|y-z|\},&c=1,\\
 \{|y|,|z|,|y+z|\},&c=-1.
 \end{cases}$$ These lists follow by applying the matrices for four, six or three steps, respectively, after which they repeat.

If $c=0$, or if $c=\pm1$ and $|y-cz|\ge2$, both other coordinates stay large through every $A$ step. The next $B$ in the repeated admissible schedule removes the sole small coordinate and, by Lemma [\[lem:exit\]](#lem:exit){reference-type="ref" reference="lem:exit"}, enters the cone. This is impossible for a periodic orbit. Therefore $c=\pm1$ and $|y-cz|\le1$. Equivalently $z=cy+b$ for $b\in C$, which is $\mathcal D_x$. The unique-small-$y$ case is its conjugate under $J$ and gives $\mathcal D_y$.

[\[prop:realize\]]{#prop:realize label="prop:realize"} Every line in $\mathcal D$ is fixed pointwise by an admissible positive word. The set $\mathcal E$ is fixed pointwise by $B^2\circ A^2$.

Equations [\[eq:rotations\]](#eq:rotations){reference-type="eqref" reference="eq:rotations"} show that $A^{12}$ is the identity on every plane $x=c$, $c\in C$, and $B^{12}$ is the identity on every plane $y=c$, $c\in C$. Thus $F=B^{12}\circ A^{12}$ fixes every point whose first two coordinates lie in $C$.

For each line choose $G$ and $r$ as in Table [2](#tab:realize){reference-type="ref" reference="tab:realize"}. The displayed images are obtained by one or two direct substitutions; no interpolation in the free integer parameter $t$ is used.

::: {#tab:realize}
  Line, with $a,b\in C$, $c=\pm1$   $(G,r)$   $G^r$-image
  --------------------------------- --------- --------------
  $(a,b,t)$                         $(A,0)$   $(a,b,t)$
  $(a,t,b)$                         $(A,1)$   $(a,b,ab-t)$
  $(t,a,b)$                         $(B,1)$   $(b,a,ab-t)$
  $(c,t,ct+b)$                      $(A,2)$   $(c,cb,-ct)$
  $(t,c,ct+b)$                      $(B,2)$   $(cb,c,-ct)$

  : The explicit line realization used in [\[eq:lineword\]](#eq:lineword){reference-type="eqref" reference="eq:lineword"}.
:::

In each row the image under $G^r$ has its first two coordinates in $C$, and the coordinate preserved by $G$ is a fixed member of $C$ on the original line. Therefore $$\label{eq:lineword}
 W_L=G^{12-r}\circ F\circ G^r$$ fixes every point of that line. Indeed, $F$ fixes $G^r(P)$, and the remaining composition is $G^{12}(P)=P$. The word is positive and contains both letters, including when $r=0$. Finally [\[eq:E\]](#eq:E){reference-type="eqref" reference="eq:E"} proves the assertion on $\mathcal E$.

Propositions [\[prop:cover\]](#prop:cover){reference-type="ref" reference="prop:cover"} and [\[prop:realize\]](#prop:realize){reference-type="ref" reference="prop:realize"}, together with Corollary [\[cor:periodicsmall\]](#cor:periodicsmall){reference-type="ref" reference="cor:periodicsmall"}, prove the first two parts of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Points on a listed line need not be periodic for an arbitrary admissible word; their realizing word is allowed to depend on the line.

# All level intersections and the bound forty {#sec:levels}

The directions of the varying coordinates distinguish $\mathcal D_0,\mathcal D_x,\mathcal D_y$. Within each family the fixed coordinates and intercept distinguish its lines. Thus there are precisely $27+6+6=39$ distinct lines.

On an axis-parallel line with fixed coordinates $a,b\in C$, restriction of the invariant gives $$\label{eq:axisform}
 K(t)=t^2-abt+a^2+b^2.$$ On a line of $\mathcal D_x$ or $\mathcal D_y$ with parameters $c=\pm1$, $b\in C$, it gives $$\label{eq:slantform}
 K(t)=t^2+cbt+b^2+1.$$ In particular the cubic term has vanished by the explicit line parametrization, not by a numerical quadratic fit. Counting the choices of fixed coordinates gives Table [3](#tab:forms){reference-type="ref" reference="tab:forms"}.

::: {#tab:forms}
  Form, allowing $t\mapsto-t$     Axis lines   Slanted lines   Total
  ----------------------------- ------------ --------------- -------
  $t^2$                                  $3$             $0$     $3$
  $t^2+1$                               $12$             $4$    $16$
  $t^2-t+2$                             $12$             $8$    $20$

  : Exact invariant forms on the 39 lines.
:::

[\[lem:leveloverlap\]]{#lem:leveloverlap label="lem:leveloverlap"} The three families of integer values in Table [3](#tab:forms){reference-type="ref" reference="tab:forms"} are pairwise disjoint above four.

If $u^2=v^2+1$, then $(u-v)(u+v)=1$, giving only common level one. If $u^2=v^2-v+2$, then $$((2v-1)-2u)((2v-1)+2u)=-7.$$ The signed integer factor pairs of $-7$ give $u^2=4$. For $u^2+1=v^2-v+2$ the same factorization has right side $-3$; its signed pairs give $u^2+1=2$. This covers negative as well as positive parameters.

For $k>4$, each line has at most two integer points of level $k$, and at most one form family is active. Thus the respective upper bounds are $6,32,40$. There are no $\mathcal E$ points above level four.

It remains to count the low levels with overlaps removed. Every line form is nonnegative, and the only values at most four are $0,1,2,4$. Direct substitution of their integer roots gives Table [4](#tab:low){reference-type="ref" reference="tab:low"}. The descriptions in each row are disjoint by their absolute coordinate patterns and product signs. They also show that no point has been counted twice merely because it lies on two lines.

::: {#tab:low}
   $k$  Exact candidate set $X_k$                                                                                                                                               Size
  ----- ------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
   $0$  The origin                                                                                                                                                               $1$
   $1$  Signed unit-axis points                                                                                                                                                  $6$
   $2$  All triples with absolute coordinates $(1,1,0)$ in any positions; also all-unit triples of positive product                                                        $12+4=16$
   $4$  Signed axis points of height two; all-unit triples of negative product; triples with absolute coordinates $(2,1,1)$ and positive product; and $\mathcal E$     $6+4+12+4=26$

  : Low-level intersections after pointwise deduplication. Negative levels and level three are empty.
:::

We have proved $|X_k|\le40$ for every integer $k$, together with the asserted necessary level families. These statements do not say that every candidate is periodic for a fixed word.

There is a uniform exact construction without a height cutoff. For each line write its proved restriction as $t^2+\beta t+\gamma$. Compute $$\label{eq:root}
 \Delta=\beta^2-4(\gamma-k).$$ There is no integer root unless $\Delta$ is a nonnegative integer square. If $\Delta=d^2$ with $d\ge0$, the candidates are $(-\beta+d)/2$ and $(-\beta-d)/2$, retaining only integral values. Substitute them on all 39 lines, deduplicate the coordinate triples and add $\mathcal E$ precisely when $k=4$. Equations [\[eq:axisform\]](#eq:axisform){reference-type="eqref" reference="eq:axisform"}--[\[eq:root\]](#eq:root){reference-type="eqref" reference="eq:root"} prove both completeness and termination of this finite construction.

# The exact ordinary-cycle classifier {#sec:classifier}

Fix $k$ and an admissible chronological word $w=\ell_1\cdots\ell_s$. Index the finite set $X_k$ once. For $L\in\{A,B\}$ define $$\label{eq:partial}
 (T_L)_{P,Q}=
 \begin{cases}
 1,&L(P)=Q\in X_k,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad P,Q\in X_k.$$ Each row and column has at most one nonzero entry, since each letter is a bijection on the full lattice. These are partial-permutation matrices, not stochastic matrices with an absorbing state. With row actions the chronological matrix product is $$\label{eq:Tw}
 T_w=T_{\ell_1}\cdots T_{\ell_s}.$$ The order differs from [\[eq:matrices\]](#eq:matrices){reference-type="eqref" reference="eq:matrices"} because [\[eq:Tw\]](#eq:Tw){reference-type="eqref" reference="eq:Tw"} acts on point-indexed rows, whereas [\[eq:matrices\]](#eq:matrices){reference-type="eqref" reference="eq:matrices"} acts on exponent-coordinate columns.

[\[prop:classifier\]]{#prop:classifier label="prop:classifier"} The directed cycles of $T_w$ are exactly the ordinary integer cycles of $W$ on $\{K=k\}$, with their actual least periods.

A nonzero entry in [\[eq:Tw\]](#eq:Tw){reference-type="eqref" reference="eq:Tw"} is precisely a word transition all of whose intermediate letter phases stay in $X_k$. By the proved periodic cover, every genuine periodic point and all its phases do so. Its whole cycle is therefore retained. Conversely each directed matrix cycle is an actual sequence of the original letter applications and returns under the indicated powers of $W$. The bijection between its distinct vertices and actual triples preserves the least period.

An explicit implementation need not form matrices. Construct $X_k$ by [\[eq:root\]](#eq:root){reference-type="eqref" reference="eq:root"}. Starting from each $P\in X_k$, apply the $s$ letters in order; declare its partial successor undefined immediately if an intermediate image leaves $X_k$. Otherwise record the final image. Traverse this finite partial map to obtain its directed cycles, retaining distinct coordinate triples and identifying cycles only by cyclic rotation. Reversal is not an additional quotient.

This prescription terminates after finitely many root tests and walks on at most 40 vertices. It has no guessed coordinate radius and no trial-period cutoff. A component of a finite partial injection is either a directed chain or a directed cycle; a tail cannot enter a cycle, since the joining vertex would then have two predecessors. Hence a traversal cannot lose a cycle by discarding a previously examined chain. The exact pointwise construction also handles intersections between different lines at small integer parameters.

Let $c_d(w,k)$ be the number of directed cycles of length $d$. Proposition [\[prop:classifier\]](#prop:classifier){reference-type="ref" reference="prop:classifier"} gives, for every $n\ge1$, $$\label{eq:counts}
 \#\mathop{\mathrm{Fix}}(W^n;\{K=k\}(\mathbb Z))
   =\mathop{\mathrm{tr}}(T_w^n)=\sum_{d\mid n}d\,c_d(w,k).$$ There are no cycles longer than $|X_k|\le40$. The ordinary dynamical zeta function on this fixed level is $$\label{eq:zeta}
 \begin{aligned}
 \zeta_{w,k}(u)
  &=\exp\left(\sum_{n\ge1}
       \#\mathop{\mathrm{Fix}}(W^n;\{K=k\}(\mathbb Z))\frac{u^n}{n}\right)\\
  &=\prod_{d=1}^{40}(1-u^d)^{-c_d(w,k)}
    =\det(I-uT_w)^{-1}.
 \end{aligned}$$ These are identities of formal power series, hence of the resulting rational functions. To see the last equality directly, order vertices componentwise: each directed chain has nilpotent adjacency matrix and determinant contribution one, while each $d$-cycle contributes $1-u^d$. For an empty $X_k$, the determinant and zeta are both one. This finite-permutation identity is a classical consequence of the new arithmetic reduction, not an additional independent theorem about Euler factors.

Merely checking that a word returns the starting triple to $X_k$ is not the partial matrix construction above: every intermediate phase is part of its definition. Likewise, a generic affine-line automaton need not detect whether a line return fixes its integer parameter. Neither shortcut replaces the exact pointwise classifier.

# Proper escape in both time directions {#sec:twosided}

[\[prop:forward\]]{#prop:forward label="prop:forward"} For an admissible word $W$, an integer point is either periodic or satisfies $\left\lVert W^n(P)\right\rVert_\infty\to\infty$ as $n\to\infty$.

Consider its repeated-word forward letter trajectory. If it enters $\mathcal C_+$, Lemma [\[lem:cone\]](#lem:cone){reference-type="ref" reference="lem:cone"} proves proper escape, including at the ordinary word times. Suppose it never does. If it meets $\mathcal E$, invariance of that finite set and bijectivity make the original point periodic. We may therefore exclude $\mathcal E$.

By Lemmas [\[lem:descent\]](#lem:descent){reference-type="ref" reference="lem:descent"} and [\[lem:exit\]](#lem:exit){reference-type="ref" reference="lem:exit"}, the trajectory eventually enters $\mathcal S$ and stays there. After one further letter, the third coordinate cannot be the only small one: both its possible predecessors would lie outside $\mathcal S$, as in the proof of Corollary [\[cor:periodicsmall\]](#cor:periodicsmall){reference-type="ref" reference="cor:periodicsmall"}.

For a later phase with only a small first coordinate, the rotation argument in Proposition [\[prop:cover\]](#prop:cover){reference-type="ref" reference="prop:cover"} uses no backward recurrence: unless the point lies in $\mathcal D_x$, it enters the cone by the next $B$ occurrence. That occurrence exists in a repeated admissible word. The corresponding assertion for a sole small second coordinate follows by $J$. Every sufficiently late phase is consequently in $\mathcal D$ and has the fixed invariant value $k=K(P)$. It lies in the finite set $X_k$.

In particular the ordinary forward $W$-orbit is eventually finite. For some $0\le i<j$ we have $W^i(P)=W^j(P)$; applying $W^{-i}$ gives $P=W^{j-i}(P)$. Thus a cone-free orbit is periodic, and every nonperiodic point properly escapes forward.

Define the polynomial involution $$\label{eq:reverser}
 R(x,y,z)=(x,y,xy-z).$$ Substitution in the explicit maps and inverses gives $$RAR=A^{-1},\qquad RBR=B^{-1}.$$ If $U=\ell_1\circ\cdots\circ\ell_s$ is the map associated with the reversed chronological word, these identities imply $$\label{eq:inverseword}
 W^{-1}=RUR.$$ The reversal of word order is indispensable; no commutativity of the letters is used.

If $P$ is not periodic for $W$, then $R(P)$ is not periodic for $U$, since any return for the latter, conjugated by $R$, would give a return under $W^{-1}$. Proposition [\[prop:forward\]](#prop:forward){reference-type="ref" reference="prop:forward"} implies $\left\lVert U^n(R(P))\right\rVert_\infty\to\infty$. The involution $R$ is proper on the integer lattice: if $\left\lVert R(Q)\right\rVert_\infty\le M$, then $$Q=R(R(Q)),\qquad
 \left\lVert Q\right\rVert_\infty\le\max\{M,M^2+M\}.$$ It therefore sends a sequence tending to infinity to a sequence tending to infinity. Equation [\[eq:inverseword\]](#eq:inverseword){reference-type="eqref" reference="eq:inverseword"} now gives $$W^{-n}(P)=R(U^n(R(P))),\qquad
 \left\lVert W^{-n}(P)\right\rVert_\infty\longrightarrow\infty .$$ This completes the fourth part of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} and, with the level/classifier arguments, its entire proof.

# Reproducibility and limitations {#sec:scope}

The classification is a proof over the entire integer lattice and the entire admissible word family. Its only finite reduction is the exact level construction proved above. The accompanying implementation uses integer square roots and exact point transitions, with the chronological word convention stated in its interface.

The retained research record contains the original finite implementation checks: small-box cover comparisons, actual cycle closure for specified words and levels, and symbolic checks of the 39 line-realizing words and reverser identities. Those are historical supporting checks, not premises substituted for the all-word proof and not newly repeated executions during manuscript preparation. The supplement preserves the exact original classifier and its helper. The helper also contains an older 45-line generic diagnostic; the classifier uses exactly its first 39 lines as proved here. The other six lines and any observed generic-period histogram are not part of the theorem.

The positive-word condition, the occurrence of both letters, the integer lattice and ordinary word clock are essential to the argument. We do not classify nonintegral rational points, complex periodic schemes or their multiplicities, finite-field fixed points, or finite whole-group orbits. The upper bound 40 is a universal candidate bound and not a claim of optimality. The source comparison is bounded by the inspected primary statements. The inaccessible Humphries--Manning (2015) follow-up, *Curves of period two points for trace maps*, was not silently declared irrelevant in every theorem.

The levelwise determinant in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} describes ordinary source dynamics. It proves no target Euler factor, root number, automorphic correspondence, Riemann-zero identification or Hilbert--Pólya realization. No such promotion follows from the integer invariant or rational dynamical zeta.

#### Preparation.

This manuscript was prepared with AI assistance. The accompanying full proof and source review and manuscript reviews are internal AI-assisted checks, not human peer review or worldwide-priority certification. All central mathematical arguments are included in the article, independently of local research-note links.
