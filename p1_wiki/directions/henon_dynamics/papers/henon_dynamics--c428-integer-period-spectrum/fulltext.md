---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c428-integer-period-spectrum"
canonical_tex: "henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/main.tex"
canonical_pdf: "henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/main.pdf"
source_sha256: "78f37bfdff0df51b80014c6df82dcea5b7490db6ef7075e495a06ec3b43a52dd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Integer periods of single-factor Hénon maps of arbitrary degree

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum>)
- [规范 TeX](<../../../../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $p\in\mathbb Z[t]$ of any degree at least two, consider $F_{a,p}(x,y)=(y,p(y)-ax)$ on the whole integer lattice, with $a=1$ or $a=-1$. We prove that the union of native least periods over this family is exactly $\{1,2,3,4,6\}$ for $a=1$, and $\{1,2,3,4,6,8\}$ for $a=-1$. The leading coefficient and degree are unrestricted. An integer secant remainder and its value-difference congruences reduce every large-diameter nonaffine orbit to three finite endpoint templates. Small diameters are handled by an exact integer-interpolation certificate; large diameters by identity graphs and every exceptional integer root of an affine edge equation. The proof is computer-assisted, with two recorded author executions and one independently implemented reconstruction. We provide the full analytic reduction, exact tables, reproducible pseudocode and eleven realization witnesses. The positive spectrum and the endpoint-graph framework already occur in the earlier monic cubic classification; the result here is the complete all-degree, double-sign extension, not a new general endpoint method or a per-polynomial point atlas.
bibliography:
- references.bib
title: |
  Integer periods of single-factor Hénon maps\
  of arbitrary degree
```

## Markdown 正文

# The exact spectra and their scope {#sec:theorem}

We consider the polynomial automorphism $$\label{eq:map}
 F_{a,p}(x,y)=(y,p(y)-ax),\qquad
 a\in\{1,-1\},\quad p\in\mathbb Z[t],\quad\deg p\ge2.$$ Its Jacobian determinant is $a$, and its inverse is $(x,y)\mapsto((p(x)-y)/a,x)$, again integral. A *native least period* is the smallest positive $n$ with $F_{a,p}^n(P)=P$; a single application of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is always one step. Define $$\operatorname{Spec}_{\mathrm{per}}(a,p)=\{n\ge1:\text{some }P\in\mathbb Z^2
                    \text{ has native least period }n\}.$$

[\[thm:spectra\]]{#thm:spectra label="thm:spectra"} For the full coefficient families in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, $$\label{eq:spectra}
 \bigcup_{\substack{p\in\mathbb Z[t]\\\deg p\ge2}}\operatorname{Spec}_{\mathrm{per}}(1,p)
 =\mathcal S_+:=\{1,2,3,4,6\},\qquad
 \bigcup_{\substack{p\in\mathbb Z[t]\\\deg p\ge2}}\operatorname{Spec}_{\mathrm{per}}(-1,p)
 =\mathcal S_-:=\{1,2,3,4,6,8\}.$$ The exclusion proof is computer-assisted through the two exact finite certificates in Sections [4](#sec:small){reference-type="ref" reference="sec:small"} and [5](#sec:symbolic){reference-type="ref" reference="sec:symbolic"}. Every member of each union is realized by an explicit polynomial and integer cycle in Table [4](#tab:witnesses){reference-type="ref" reference="tab:witnesses"}.

The unions in [\[eq:spectra\]](#eq:spectra){reference-type="eqref" reference="eq:spectra"} are important: the theorem does not assert that every fixed polynomial realizes every listed period. It also gives neither a complete point table for one polynomial nor a sharp bound on the number of its periodic points. No bound on the degree or leading coefficient appears in the hypotheses.

## What is already known

For arbitrary integral-coefficient polynomial maps of the plane, Pezda proves that the union of possible least periods is $$\label{eq:pezda}
 \{1,2,3,4,6,8,9,12,16,18,24\}
 \quad\text{\cite[Theorem~2.1]{Pezda2002}}.$$ Uniform boundedness is therefore not new here. The Hénon subfamily and its two Jacobian signs require a sharper exclusion. Our proof does not use [\[eq:pezda\]](#eq:pezda){reference-type="eqref" reference="eq:pezda"} as a cutoff: finite graph decomposition finds every cycle, whatever its length. A five-element set also appears in Pezda's local discussion of special cycles whose points are congruent modulo the maximal ideal; that local statement is not the global positive-sign Hénon theorem.

Two earlier internal working manuscripts supply closer ownership. C412 classifies all rational cycles for monic integral quadratic maps with $a=1$, with periods $1,2,3,4$ [@C412Working]. C417 classifies the monic integral conservative cubic family, with periods $1,2,3,4,6$, all positive-period realizations, a detailed parameter atlas and a sharp eleven-point bound [@C417Working]. In particular, the positive list in [\[eq:spectra\]](#eq:spectra){reference-type="eqref" reference="eq:spectra"} is not a new list. Integer translation, the secant inequality, endpoint bounds, affine recurrence classification and symbolic endpoint graphs are already part of C417's framework. The change needed here is that the secant remainder is an arbitrary element of $\mathbb Z[t]$, not a single monic linear factor. Its integer value-difference congruences give a complete replacement reduction. Integer interpolation then handles every small-support restriction without limiting the original degree.

The coefficient ring cannot be weakened to integer-valued rational polynomials. Kim, Krieger, Postolache and Szeto construct long integer cycles for a rational integer-valued family [@KimEtAl2025 Theorem 5.1]. Their odd-degree polynomial $s_d$ has leading coefficient $1/d!$ [@KimEtAl2025 Section 4.1], so it is not in $\mathbb Z[t]$ for $d\ge3$. Separately, Ingram's Conjecture 3 in Section 11 of [@deHenon2024] predicts the negative list in [\[eq:spectra\]](#eq:spectra){reference-type="eqref" reference="eq:spectra"} for rational periodic points of $(y,y^2+c+x)$ over $\mathbb Q$. Our integral-coefficient, integer-point, all-degree theorem does not settle that rational quadratic conjecture.

The present article develops the frozen IH6 proof package [@IH6Working] and its independent reconstruction [@IH6Review]. These are actual unpublished AI-assisted internal records, not invented journal publications or human peer review. The contribution is one integrated all-degree, double-sign exclusion and realization theorem. Classical interpolation, affine linear algebra, finite graph decomposition and the individual low-degree witnesses are not presented as separate new results.

## Proof organization

An integer translation normalizes the coordinate support of one periodic orbit to have endpoints $0,D$. Section [2](#sec:secant){reference-type="ref" reference="sec:secant"} constructs its integer secant remainder. For $D\ge10$, Section [3](#sec:reduction){reference-type="ref" reference="sec:reduction"} proves that the orbit is either secant-affine or belongs to one of three finite endpoint-template classes. The affine branch is proved directly. Sections [4](#sec:small){reference-type="ref" reference="sec:small"} and [5](#sec:symbolic){reference-type="ref" reference="sec:symbolic"} state the exact finite certificates for the remaining cases, with full pseudocode in Appendix [8](#app:pseudocode){reference-type="ref" reference="app:pseudocode"}. Explicit witnesses close the realizability direction.

# One periodic support and its integer secant remainder {#sec:secant}

Let an orbit of least period $n$ have successive states $P_i=(x_i,x_{i+1})$, with indices read modulo $n$. Its coordinate word satisfies $$\label{eq:recurrence}
 p(x_i)=x_{i+1}+a x_{i-1}.$$ Let $E=\{x_i:0\le i<n\}$, put $m=\min E$ and $D=\max E-m$. The integer translation $(x,y)=(m+u,m+v)$ replaces $p$ by $$\label{eq:translation}
 p_m(t)=p(m+t)-(a+1)m\in\mathbb Z[t].$$ It preserves degree, the Jacobian sign, the integer lattice and native least period. We may therefore assume $\min E=0$ and $\max E=D$. Unlike a global point-count argument, these extrema are taken for one orbit, not for all periodic points of a map. If $D=0$, the only state is $(0,0)$ and the period is one. Assume below that $D\ge1$, and again denote the translated polynomial by $p$.

For each actual letter $t\in E$, equation [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} gives $$\label{eq:outputs}
 p(t)\in E+aE\subset J_a(D),\qquad
 J_1(D)=[0,2D],\quad J_{-1}(D)=[-D,D].$$ Both intervals have length $2D$. Set $$\label{eq:secantparams}
 A=p(0),\qquad q=\frac{p(D)-p(0)}D.$$ An integral-coefficient polynomial satisfies $s-t\mid p(s)-p(t)$ for distinct integers $s,t$. Thus $q\in\mathbb Z$; the endpoint output bounds imply $-2\le q\le2$.

[\[lem:secant\]]{#lem:secant label="lem:secant"} There exists $h\in\mathbb Z[t]$ such that $$\label{eq:secant}
 p(t)=A+qt+t(t-D)h(t).$$ For each actual interior letter $t\in E\cap(0,D)$, $$\label{eq:errorbound}
 |h(t)|\,t(D-t)\le2D.$$ For all distinct integers $s,t$ one also has $$\label{eq:congruence}
 h(s)-h(t)\in(s-t)\mathbb Z.$$

The polynomial $p(t)-A-qt$ is integral and vanishes at $0$ and $D$. Divide first by the monic factor $t$. The quotient remains integral and vanishes at $D$, since $D\ne0$; division by $t-D$ gives [\[eq:secant\]](#eq:secant){reference-type="eqref" reference="eq:secant"}. No assumption on the leading coefficient was used. The line $A+qt$ interpolates the two endpoint outputs, so its value lies in $J_a(D)$ throughout $[0,D]$. At an actual letter, both it and $p(t)$ lie in that interval of length $2D$. Their difference proves [\[eq:errorbound\]](#eq:errorbound){reference-type="eqref" reference="eq:errorbound"}. Formula [\[eq:congruence\]](#eq:congruence){reference-type="eqref" reference="eq:congruence"} is the usual value-difference divisibility for an integral polynomial.

If $D\ge10$, the bound in Lemma [\[lem:secant\]](#lem:secant){reference-type="ref" reference="lem:secant"} gives $$\label{eq:endbounds}
 \begin{array}{c|c}
 \text{actual letter }t&\text{possible integer }h(t)\\ \hline
 1,\ D-1&-2,-1,0,1,2\\
 2,\ D-2&-1,0,1\\
 3\le t\le D-3&0
 \end{array}$$ The last row follows from $t(D-t)\ge3(D-3)>2D$; it remains strict at $D=10$. These constraints are imposed only on letters belonging to $E$. Missing integers between the endpoints are not inserted into the orbit.

# The complete large-diameter reduction {#sec:reduction}

A normalized periodic orbit is *secant-affine* if $p(t)=A+qt$ for every $t$ in its actual coordinate support $E$. This is a statement about the restriction to $E$, not about the degree of the original polynomial.

[\[lem:templates\]]{#lem:templates label="lem:templates"} Suppose $D\ge10$ and the orbit is not secant-affine. Its full support and its interior remainder values have one of the following forms.

1.  *Left end:* $E=\{0,D\}\cup S$, where $\varnothing\ne S\subseteq\{1,2,3\}$. The selected remainder values satisfy [\[eq:endbounds\]](#eq:endbounds){reference-type="eqref" reference="eq:endbounds"} and all pairwise congruences [\[eq:congruence\]](#eq:congruence){reference-type="eqref" reference="eq:congruence"}; at least one is nonzero.

2.  *Right end:* the reflection of the preceding form under $t\mapsto D-t$, with the same remainder bounds and congruences.

3.  *Both ends:* $E=\{0,D\}\cup L\cup\{D-b:b\in R\}$, where $\varnothing\ne L,R\subseteq\{1,2\}$. All interior values of $h$ equal the same nonzero integer $c$. If either $L$ or $R$ contains $2$, then $|c|\le1$; otherwise $|c|\le2$.

The first two classes have at most five letters, and the third at most six.

Suppose first that $e\in E\cap[4,D-4]$. Its remainder is zero by [\[eq:endbounds\]](#eq:endbounds){reference-type="eqref" reference="eq:endbounds"}. Its distance to $1,D-1$ is at least three, and its distance to $2,D-2$ is at least two. A nonzero integer of absolute value at most two cannot be divisible by the first kind of distance; an integer of absolute value at most one cannot be divisible by the second. Comparing $e$ with each of these positions that actually belongs to $E$ forces its remainder to vanish. All other interior remainder values already vanish. The orbit would be secant-affine, a contradiction. Hence a nonaffine support is contained in $$\label{eq:eightpositions}
 \{0,1,2,3,D-3,D-2,D-1,D\}.$$

If $3\in E$ and some right interior letter $r\in\{D-3,D-2,D-1\}$ belongs to $E$, then $r-3\ge4$. Since $h(3)=0$ and $|h(r)|\le2$, congruence [\[eq:congruence\]](#eq:congruence){reference-type="eqref" reference="eq:congruence"} forces $h(r)=0$. Its distance to either selected left letter $1$ or $2$ is at least five, so those remainder values also vanish. Every selected right letter has zero remainder by direct comparison with $3$. This again makes the orbit affine. The reflected argument applies to $D-3$. Therefore a nonaffine support containing $3$ is left-sided, and one containing $D-3$ is right-sided.

The remaining interior letters lie in the two distance-one/two clusters. If only one cluster occurs, the support is already left- or right-sided. If both occur, each cross-cluster distance is at least $D-4\ge6$, whereas two allowed remainder values differ by at most four. Their difference must vanish. Since both clusters are nonempty, all interior remainder values are equal. The common value is nonzero by nonaffinity, and its bound is that imposed by the furthest selected distance, giving the third case.

## The affine branch

[\[lem:affine\]]{#lem:affine label="lem:affine"} For $a=1$, the least period of a secant-affine orbit belongs to $\mathcal S_+$. For $a=-1$, it belongs to $\{1,2\}$.

At each step the orbit is also an orbit of $T(x,y)=(y,A+qy-ax)$. Its centroid $C=n^{-1}\sum_{j=0}^{n-1}T^j(P)$ is a rational fixed point of $T$. Translation by $C$ reduces the question to periodic vectors for $$\label{eq:matrix}
 B=\begin{pmatrix}0&1\\-a&q\end{pmatrix}.$$ The centroid need not be integral, because only a necessary period restriction is being proved.

For $a=1$ and $q=-1,0,1$, the respective identities are $$B^2+B+I=0,\qquad B^2+I=0,\qquad B^2-B+I=0.$$ They imply periods dividing three, four and six, respectively. For $q=2$, write $B=I+N$ with $N^2=0$. If $B^n v=v$, then $nNv=0$, hence $Nv=0$ in characteristic zero and $v$ is fixed. For $q=-2$, write $B=-I+N$ with $N^2=0$. A periodic vector is fixed by an even power, for which $B^{2n}=I-2nN$; again $Nv=0$, so its period divides two. These cases give $\mathcal S_+$.

For $a=-1$, the characteristic polynomial is $\lambda^2-q\lambda-1$. If $q=0$, then $B^2=I$. For $q\ne0$, its two roots are distinct real numbers and neither is $1$ or $-1$. Neither root is a root of unity, so $B^n-I$ is invertible for every $n\ge1$ and the only periodic vector is zero. The possible least periods are therefore one and two.

No period bound from another theorem enters either lemma. The nonaffine branch now consists of finitely many remainder templates, but $D$ itself is still unrestricted. Section [5](#sec:symbolic){reference-type="ref" reference="sec:symbolic"} will account for every integer $D\ge10$ exactly.

# Small diameters: all integral-polynomial restrictions {#sec:small}

For $0\le D\le9$ we enumerate every nonempty $E\subseteq\{0,\ldots,D\}$ with endpoints $0,D$, and every restriction $v:E\to E+aE$ realizable by an integral polynomial. The word "restriction" removes the unbounded degree from this finite step without restricting the original family.

[\[lem:newton\]]{#lem:newton label="lem:newton"} Write $E=\{e_0<\cdots<e_{k-1}\}$. The values $v(e_j)$ are the restriction of a polynomial in $\mathbb Z[t]$ if and only if the unique degree-less-than-$k$ interpolating polynomial has integer Newton coefficients: $$\label{eq:newton}
 r(t)=\sum_{j=0}^{k-1}b_j\prod_{i<j}(t-e_i),\qquad b_j\in\mathbb Z.$$ Every such restriction can be realized by a polynomial of degree at least two.

Starting with an integral realizing polynomial $p$, subtract $p(e_0)$ and divide by the monic factor $t-e_0$. The quotient is integral. Repeating at the remaining nodes gives the integer Newton coefficients; any remaining term is divisible by $W_E(t)=\prod_{e\in E}(t-e)$. Equivalently, monic division by $W_E$ leaves the unique interpolant as an integral remainder. Conversely, [\[eq:newton\]](#eq:newton){reference-type="eqref" reference="eq:newton"} is itself an integral polynomial with the prescribed values. If its degree is below two, add $W_E$ when $|E|\ge2$, or $(t-e_0)^2$ when $|E|=1$. The added polynomial vanishes on $E$ and makes the degree at least two.

For an already chosen prefix $r_{<j}$ of [\[eq:newton\]](#eq:newton){reference-type="eqref" reference="eq:newton"}, put $B_j=\prod_{i<j}(e_j-e_i)>0$ (the empty product is one). The finite extension rule is $$\label{eq:extension}
 v(e_j)\in E+aE,\qquad
 v(e_j)\equiv r_{<j}(e_j)\pmod{B_j},\qquad
 b_j=\frac{v(e_j)-r_{<j}(e_j)}{B_j}.$$ Every admissible value is considered, and the coefficient is then forced. Hence the recursive rule enumerates every realizable restriction exactly once for the fixed ordered alphabet.

[\[lem:graph\]]{#lem:graph label="lem:graph"} For a completed restriction $v$, put a directed edge $$\label{eq:edge}
 (x,y)\longrightarrow(y,v(y)-ax)
 \quad\text{on }E^2\text{ whenever }v(y)-ax\in E.$$ Its directed cycles whose coordinate support is exactly $E$ are precisely the periodic orbits of the restriction with full support. Their graph lengths are their native least periods. Enumerating all alphabets and retaining only full-support cycles misses no integer periodic orbit.

The edge equation is exactly one native application of the map. A directed cycle consists of distinct ordered states, so its first return has length equal to that cycle's length. Conversely, any native orbit yields such a cycle in the graph of its restriction. It is checked at its own complete alphabet, whether or not it is also contained in a larger alphabet. Traversing a finite partial function graph until exit or a repeated state extracts all cycles; there is no bound on the allowed period. The explicit traversal and its stopping conditions are given in Appendix [8](#app:pseudocode){reference-type="ref" reference="app:pseudocode"}.

[\[lem:smallcertificate\]]{#lem:smallcertificate label="lem:smallcertificate"} The complete enumeration [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"}--[\[eq:edge\]](#eq:edge){reference-type="eqref" reference="eq:edge"} for $0\le D\le9$ has the counts in Table [1](#tab:small){reference-type="ref" reference="tab:small"}. It yields no period outside $\mathcal S_+$ for $a=1$, or outside $\mathcal S_-$ for $a=-1$.

The author implementation is `check_integer_periods.py` in the frozen package [@IH6Working]. It uses arbitrary-precision integers, exact divisibility, all endpoint-containing alphabets and the complete partial-graph traversal of Lemma [\[lem:graph\]](#lem:graph){reference-type="ref" reference="lem:graph"}. Its recorded execution reached $D=10$; only the $D\le9$ prefix is needed here. The independent implementation in [@IH6Review] reconstructed that prefix using alternating-extreme node order, exact Lagrange coefficient congruences and indegree-zero peeling rather than the author's Newton expansion and path traversal. It matched all ten cumulative counts, totaling $35778$ restrictions, and both period spectra. Appendix [9](#app:independent){reference-type="ref" reference="app:independent"} proves the equivalence of its different interpolation criterion and cycle extraction. The execution receipts and exact-code identities are recorded in Section [7](#sec:evidence){reference-type="ref" reference="sec:evidence"}; no certificate was rerun for typesetting.

::: {#tab:small}
    $D$   $R_1(D)$   $R_{-1}(D)$   $C(D)$  $a=1$ periods    $a=-1$ periods
  ----- ---------- ------------- -------- ---------------- ----------------
      0          1             1        2     $\{1\}$          $\{1\}$
      1          9             9       20  $\{1,2,3,4\}$      $\{1,2\}$
      2         74            74      168  $\mathcal S_+$   $\{1,2,3,4\}$
      3        320           350      838  $\mathcal S_+$   $\{1,2,3,4\}$
      4        650           744     2232  $\mathcal S_+$   $\mathcal S_-$
      5        808          1088     4128  $\mathcal S_+$   $\mathcal S_-$
      6       1184          1550     6862  $\mathcal S_+$   $\mathcal S_-$
      7       1838          2410    11110  $\mathcal S_+$   $\mathcal S_-$
      8       3586          4486    19182  $\mathcal S_+$   $\mathcal S_-$
      9       7392          9204    35778  $\mathcal S_+$   $\mathcal S_-$

  : Complete small-diameter restriction counts. $R_a(D)$ counts restrictions at diameter exactly $D$ for sign $a$; $C(D)$ is the double-sign cumulative count through $D$. The last two columns are cumulative sets of full-support least periods. $\mathcal S_+$ and $\mathcal S_-$ are defined in Theorem [\[thm:spectra\]](#thm:spectra){reference-type="ref" reference="thm:spectra"}. Counts concern restriction graphs across a family, not periodic points of one polynomial.
:::

Pairwise divisibility alone is not a sufficient replacement for Lemma [\[lem:newton\]](#lem:newton){reference-type="ref" reference="lem:newton"}. For instance the data $E=(0,2,4)$ and $v=(0,0,4)$ satisfy every pairwise value-difference congruence, but their interpolating polynomial is $t(t-2)/2$, not an element of $\mathbb Z[t]$. The independent checker correctly rejected these data. In the large-diameter templates we will deliberately use only necessary congruences, but there the logic is an overapproximation for exclusion, not an exact realizability test.

# Large diameters: identity graphs and every exceptional root {#sec:symbolic}

## Finite symbolic models for the infinite diameter range

Represent each possible letter by an affine polynomial in $D$, $$\label{eq:letters}
 u(D)=\alpha D+\beta,\qquad
 0=(0,0),\quad D=(1,0),\quad b=(0,b),\quad D-b=(1,-b).$$ The ordered pairs here encode coefficients, not dynamical states. For $D\ge10$, all selected letters in a template remain distinct. The left and right template families from Lemma [\[lem:templates\]](#lem:templates){reference-type="ref" reference="lem:templates"} each have $32$ remainder assignments after the stated congruences and the nonzero requirement; the two-sided family has $20$. They are generated by all nonempty subsets and the finite remainder choices, not by a chosen set of sample polynomials.

For a template with letter list $U$, enumerate $$\label{eq:intercepts}
 A\in\{u+av:u,v\in U\}\subset\mathbb Z[D],\qquad
 q\in\{-2,-1,0,1,2\}.$$ Any actual orbit is included, since its actual $p(0)$ is a sum or difference of two actual letters. Distinct affine representatives may coincide at isolated diameters, but keeping both cannot omit an orbit. For an interior letter at distance $b$ from either endpoint, $$\label{eq:linearcorrection}
 t(t-D)=-bD+b^2.$$ Thus every assigned value $A+qt+t(t-D)h(t)$ is affine in $D$. At the endpoints, the correction vanishes regardless of the true values $h(0),h(D)$; zeros used for these values in code are only placeholders, not additional hypotheses.

Not every remainder assignment in a template need interpolate to an element of $\mathbb Z[t]$. The symbolic graphs form a finite superset of the restrictions of all true nonaffine orbits. That is sufficient for exclusion. A cycle in the superset is not automatically an integer-polynomial realization; the explicit witnesses are provided separately.

[\[lem:roots\]]{#lem:roots label="lem:roots"} For a symbolic template, intercept and slope, there is a finite set $\mathcal R\subset\mathbb Z_{\ge10}$ such that its full-support cycles for every integer $D\ge10$ are determined by one identity graph and the numerical graphs at all $D\in\mathcal R$.

For any ordered source letters $x,y$ and candidate target letter $z$, the edge condition is $$\label{eq:affineedge}
 p(y)-ax-z=\mu D+\nu=0,\qquad\mu,\nu\in\mathbb Z.$$ If $\mu=\nu=0$, it is an identity. If $\mu=0\ne\nu$, it never holds. Otherwise it has only the possible root $D=-\nu/\mu$; keep that root precisely when it is an integer at least ten. There are finitely many ordered letter triples, so the union $\mathcal R$ of all such roots is finite. Outside $\mathcal R$, exactly the identity edges occur. At each member of $\mathcal R$, direct substitution gives the entire graph. Distinctness of the letters prevents an additional alphabet-collision branch. Every integer $D\ge10$ belongs to one of these cases.

The lemma is not a sampling assertion. One may build the generic graph from affine identities directly, as the independent checker does, or evaluate at $1+\max(\{9\}\cup\mathcal R)$ after proving that it avoids all changing-edge parameters, as the author code does. Both give the graph at every nonexceptional diameter.

## The author's necessary-output pruning

Let $W=U+aU\subset\mathbb Z[D]$. Every actual restriction satisfies $p(t)\in E+aE$ at every selected letter. If a symbolic value has no identical affine representative in $W$, the actual diameter must lie among the integer roots of its equations with members of $W$. Intersect these finite root sets for all values lacking an identity match. An empty intersection rejects the model. A nonempty intersection leaves only those finitely many diameters to check. If every value has an identity match, the model has no output-based restriction on $D$ and Lemma [\[lem:roots\]](#lem:roots){reference-type="ref" reference="lem:roots"} applies directly. This pruning is logically necessary, not a sufficiency claim about polynomial interpolation.

[\[lem:largecertificate\]]{#lem:largecertificate label="lem:largecertificate"} For the three template classes and both signs, the complete symbolic enumeration has the six rows in Table [2](#tab:largeauthor){reference-type="ref" reference="tab:largeauthor"}. For $a=1$ there is no full-support nonaffine cycle with $D\ge10$. For $a=-1$, every such cycle has least period four.

The author implementation is `check_large_diameter.py` in [@IH6Working]. It enumerates all template assignments, all intercepts [\[eq:intercepts\]](#eq:intercepts){reference-type="eqref" reference="eq:intercepts"} and all five slopes. Values and edge differences are stored as pairs of exact integers. It applies the necessary-output pruning just proved and then checks the complete graph partition of Lemma [\[lem:roots\]](#lem:roots){reference-type="ref" reference="lem:roots"}, using the full-support cycle extraction of Lemma [\[lem:graph\]](#lem:graph){reference-type="ref" reference="lem:graph"}. The result is Table [2](#tab:largeauthor){reference-type="ref" reference="tab:largeauthor"}. No exceptional integer diameter survives the author's output pruning; this is an output of exact root filtering, not a preset search bound.

The independent implementation [@IH6Review] deliberately omits that pruning. It directly constructs all $9020$ identity graphs and checks $512$ exceptional graphs from all nonidentity edge roots. Its six rows are Table [3](#tab:largeindependent){reference-type="ref" reference="tab:largeindependent"}. The roots that actually occur are $10,11,12$; their maximum is a result, not an input cutoff. Only four generic full-support cycles occur, all in the negative-sign two-ended class and all of length four. Every exceptional graph has no full-support cycle. The different execution scope therefore independently confirms the exclusion. The pseudocode in Appendix [8](#app:pseudocode){reference-type="ref" reference="app:pseudocode"} includes the complete unpruned graph-partition rule, as well as the author's optional pruning.

::: {#tab:largeauthor}
   $a$   Class     $H$    $M$   $V$  Generic periods   Exceptional periods
  ------ ------- ----- ------ ----- ----------------- ---------------------
   $1$   Left       32   1490    76   $\varnothing$       $\varnothing$
   $1$   Right      32   1490    76   $\varnothing$       $\varnothing$
   $1$   Both       20   1120    80   $\varnothing$       $\varnothing$
   $-1$  Left       32   1840   126   $\varnothing$       $\varnothing$
   $-1$  Right      32   1840   126   $\varnothing$       $\varnothing$
   $-1$  Both       20   1240   104      $\{4\}$          $\varnothing$

  : Author symbolic certificate for every integer $D\ge10$. $H$ is the number of remainder templates; $M$ counts triples (template, intercept, slope); $V$ counts models surviving the necessary-output test. The last two columns are sets of full-support least periods, not numbers of cycles. After this pruning there were no exceptional integer diameters to test.
:::

::: {#tab:largeindependent}
   $a$   Class     $G_0$   $M_*$   $G_*$     Root set       $C_0$   $C_*$
  ------ ------- ------- ------- ------- ---------------- ------- -------
   $1$   Left       1490      93     158  $\{10,11,12\}$        0       0
   $1$   Right      1490       0       0  $\varnothing$         0       0
   $1$   Both       1120      20      20     $\{10\}$           0       0
   $-1$  Left       1840     174     310  $\{10,11,12\}$        0       0
   $-1$  Right      1840       0       0  $\varnothing$         0       0
   $-1$  Both       1240      24      24     $\{10\}$           4       0

  : Independent unpruned symbolic reconstruction. $G_0$ counts identity graphs; $M_*$ counts models with exceptional roots; $G_*$ counts exceptional graphs, one for each (model, root). $C_0$ and $C_*$ count full-support cycles in those graphs. All four generic cycles have least period four. Unlike Table [2](#tab:largeauthor){reference-type="ref" reference="tab:largeauthor"}, no necessary-output pruning was used.
:::

Take any periodic orbit of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} and normalize it by [\[eq:translation\]](#eq:translation){reference-type="eqref" reference="eq:translation"}. If $D\le9$, apply Lemma [\[lem:smallcertificate\]](#lem:smallcertificate){reference-type="ref" reference="lem:smallcertificate"}. If $D\ge10$ and the orbit is secant-affine, apply Lemma [\[lem:affine\]](#lem:affine){reference-type="ref" reference="lem:affine"}. Otherwise Lemma [\[lem:templates\]](#lem:templates){reference-type="ref" reference="lem:templates"} places its complete support and remainder data in the symbolic enumeration, and Lemma [\[lem:largecertificate\]](#lem:largecertificate){reference-type="ref" reference="lem:largecertificate"} applies. Every diameter, degree, leading coefficient and native cycle is covered. Thus no period outside the stated sign-dependent set can occur.

# All eleven realization witnesses {#sec:witnesses}

For a cyclic word $(x_0,\ldots,x_{n-1})$, its states are the ordered pairs $(x_i,x_{i+1})$, with indices modulo $n$. Repeated letters are permitted; distinctness of the states, not distinctness of the letters, certifies the least period.

[\[prop:witnesses\]]{#prop:witnesses label="prop:witnesses"} Every row of Table [4](#tab:witnesses){reference-type="ref" reference="tab:witnesses"} gives an integral-coefficient polynomial of degree at least two and an integer orbit of the indicated native least period. Therefore every member of $\mathcal S_+$ and $\mathcal S_-$ occurs for its respective sign.

For each row substitute every displayed letter into $p(x_i)=x_{i+1}+a x_{i-1}$. These equalities give every edge and the closing edge. The $n$ adjacent ordered pairs in each row are pairwise distinct, so the first return is exactly $n$. The eleven direct checks were also included in the independent exact reconstruction [@IH6Review].

For emphasis, the negative-sign eight-cycle has states $$\begin{aligned}
 &(-2,-1),\ (-1,0),\ (0,-1),\ (-1,2),\\
 &(2,1),\ (1,0),\ (0,1),\ (1,-2).\end{aligned}$$ For $p(t)=t^3-3t$, the values at its cyclic letters are $(-2,2,0,2,2,-2,0,-2)$, equal to the successive differences $x_{i+1}-x_{i-1}$. The eight displayed states are distinct. No reversal, quotient or second-iterate clock is used. Together with the exclusion already proved, this completes Theorem [\[thm:spectra\]](#thm:spectra){reference-type="ref" reference="thm:spectra"}.

::: {#tab:witnesses}
   $a$     $n$ $p(t)$          Cyclic coordinate word
  ------ ----- --------------- ------------------------
   $1$       1 $t^2$           $(0)$
   $1$       2 $t^2-3t+2$      $(0,1)$
   $1$       3 $(t-1)^2$       $(0,0,1)$
   $1$       4 $t^2-t+1$       $(0,0,1,1)$
   $1$       6 $t^3$           $(-1,-1,0,1,1,0)$
   $-1$      1 $t^2$           $(0)$
   $-1$      2 $t^2-t$         $(0,1)$
   $-1$      3 $-3t^2+2$       $(-1,0,1)$
   $-1$      4 $-2t^2+1$       $(-1,0,0,1)$
   $-1$      6 $-t^4+4t^2-1$   $(-2,1,0,0,-1,2)$
   $-1$      8 $t^3-3t$        $(-2,-1,0,-1,2,1,0,1)$

  : Realizations of every period in the two unions. Each word lists $x_0,\ldots,x_{n-1}$; native states are adjacent ordered pairs with cyclic indices. Every polynomial belongs to $\mathbb Z[t]$ and has degree at least two.
:::

These examples certify the unions, not simultaneous occurrence of all periods for one polynomial. The positive-period list and its realization mechanism already occur in C417; the low-degree witnesses themselves are not asserted to be new.

# Execution evidence and limitations {#sec:evidence}

The proof has two distinct layers. The analytic lemmas cover every degree and diameter and reduce the question to explicit finite objects. The finite outputs are computational dependencies, not illustrative experiments. Their implementation correctness relies on the stated exact algorithms and ordinary Python integer and rational arithmetic; no proof-assistant formalization is claimed.

## Recorded mathematical executions

The author record [@IH6Working] contains exactly two executions:

1.  `python check_integer_periods.py --diameter 10`, exit code $0$, recorded monotonic time $33.877$ seconds. It examined $71068$ restrictions through $D=10$; the proof uses the $35778$ restrictions through $D=9$. The extra layer is not a substitute for the all-diameter reduction.

2.  `python check_large_diameter.py`, exit code $0$, recorded monotonic time $0.094$ seconds. It checked the complete symbolic endpoint models with the necessary-output pruning.

Those times are historical author records, not independently reproduced benchmark measurements. The immutable author ledger records their output summaries; it does not contain a separate full captured transcript for each execution.

The nonauthor reconstruction [@IH6Review] executed once with the command

> `python3 -B independent_check.py`

It imported no author implementation and did not execute the author scripts. It exited $0$, recorded $1.470911$ seconds, and preserved all $611$ output lines, including ten progress records and a final JSON object with status `PASS`. The environment was Python $3.12.3$ packaged by Anaconda, GCC $11.2.0$, on Linux $5.15.0$ x86-64 with glibc $2.35$. Its changed interpolation order, Lagrange congruences, indegree peeling and unpruned identity graphs provide an algorithmically different reconstruction. The checker had read the expected results, so it was not blind.

It verified all eleven witnesses, four interpolation controls and three graph controls. All ten small-diameter counts matched; the unpruned large-diameter results were $9020$ generic and $512$ exceptional graphs. No mathematical execution was added or repeated while preparing this manuscript. All three historical runs were CPU-only, used no floating-point tolerance or external mathematical library, and were separate from PDF builds.

## Exact artifacts

The author files reside in relative to the accompanying batch root: the frozen contract, full proof, source audit, , and the two named scripts. The independent contract, code, full output, run receipt and source spot-check are in . The executable identities used by the accepted proof are

> Author small-diameter script:
>
> Author large-diameter script:
>
> Independent checker:
>
> Independent full output:

These SHA-256 values identify bytes; they do not by themselves establish mathematical correctness. The complete argument and reconstruction pseudocode are typeset here so that a local Markdown link is not substituted for the central proof.

## Boundaries

The theorem concerns one factor, integer coefficients, integer points and $a=\pm1$. It does not classify rational nonintegral integer-valued coefficients, arbitrary rational points, nonunit Jacobian, number-field points or compositions of factors. It does not give a per-polynomial atlas, a simultaneous-period statement, a sharp total-point bound or an Euler interpretation of the ordinary periods. No bad Euler factor, root number, spectral determinant or Hilbert--Pólya conclusion is obtained.

This manuscript was prepared with AI assistance. The originating proof and reconstruction received current-team internal nonauthor review, not human peer review or a global priority certification. The bibliography audit distinguishes original statements, accessed versions and unpublished working sources; unperformed retraction, venue and competing-interest checks are not silently certified. The mathematical increment is the complete arbitrary-degree extension of an existing endpoint framework, with the two signs handled together.

# Complete finite-reduction pseudocode {#app:pseudocode}

The following pseudocode specifies exact integer arithmetic; sets deduplicate identical values or affine coefficient pairs. It is a typeset description of the frozen algorithms, not a newly executed implementation. A missing arrow is denoted by `EXIT`.

## Complete partial-function cycle extraction

The argument `v` is a map whose keys are the actual integer letters of $E$, and `v[y]` is the assigned value at the letter $y$. It is not a list indexed by the position of $y$ in an ordering of $E$. The support comparison uses the set of letters even when $E$ is ordered for interpolation.

``` {fontsize="\\small"}
FULL_CYCLES(E, v, a):
    done := empty set; answers := empty list
    for each state s in E x E:
        if s in done: continue
        path := empty list; position := empty dictionary; t := s
        while t != EXIT and t not in done and t not in position:
            position[t] := length(path); append t to path
            (x,y) := t; z := v[y] - a*x
            t := (y,z) if z in E else EXIT
        if t != EXIT and t in position:
            C := path[position[t]:]
            if union of both coordinates of states in C equals set(E):
                append C to answers
        add every state in path to done
    return answers
```

Every loop either exits the finite state space, joins a previously completed path, or repeats on the current path. In the last case the suffix is exactly one cycle; in the second case any accessible cycle has already been processed. Starting from every unmarked state proves that no cycle is lost, and no orbit-length cutoff is imposed.

## All small-diameter restrictions

Polynomial arithmetic below uses ascending integral coefficients or any equivalent exact representation. The empty Newton product is the constant polynomial one.

``` {fontsize="\\small"}
EXTEND(E=(e[0],...,e[k-1]), W, j, r, B, values):
    if j == k: emit values; return
    old := r(e[j]); step := B(e[j])
    for each z in W:
        if step divides z-old:
            c := (z-old)/step
            EXTEND(E,W,j+1,r+c*B,B*(t-e[j]),values+[z])

SMALL_CERTIFICATE:
    for D = 0,...,9:
        alphabets := {(0)} if D == 0
                     else all {0,D} union S, S subset {1,...,D-1}
        for each increasing alphabet E=(e[0],...,e[k-1]) in alphabets:
            for a in {1,-1}:
                W := {x+a*y: x,y in E}
                for each values emitted by EXTEND(E,W,0,0,1,[]):
                    v := {e[j]: values[j] for 0 <= j < k}
                    count this restriction
                    record lengths of FULL_CYCLES(E,v,a)
```

The positive basis value at each increasing node is $B_j$ in [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"}. The recursion is exactly the necessary and sufficient test in Lemma [\[lem:newton\]](#lem:newton){reference-type="ref" reference="lem:newton"}. Counts are cumulative across both signs only where explicitly stated in Table [1](#tab:small){reference-type="ref" reference="tab:small"}.

## Generating all endpoint templates

Affine coordinates are stored as pairs $(\alpha,\beta)$ for $\alpha D+\beta$. Componentwise addition and multiplication by an integer are exact. Set $H(1)=\{-2,-1,0,1,2\}$, $H(2)=\{-1,0,1\}$ and $H(3)=\{0\}$. The symbols $0,D,b,D-b$ below denote their affine coefficient pairs. A template is a pair $(U,h)$, where $h$ is a map keyed by the affine letters in $U$. The temporary values `eta[b]` are keyed by endpoint distance: on the right, `eta[b]` is assigned to the letter $D-b$, not to the letter $b$.

``` {fontsize="\\small"}
TEMPLATES:
    for side in {left,right}:
        for each nonempty S subset {1,2,3}:
            for each tuple (eta[b]: b in S) in product H(b):
                if every eta[b] == 0: continue
                if some distinct b,c in S have
                        b-c not dividing eta[b]-eta[c]:
                    continue
                U := [0] + [b if side==left else D-b for b in S] + [D]
                h := {0: 0, D: 0}
                for b in S:
                    u := b if side==left else D-b
                    h[u] := eta[b]
                emit (U,h)
    for nonempty L subset {1,2}:
        for nonempty R subset {1,2}:
            bound := 1 if 2 in L union R else 2
            for integer c with 0 < abs(c) <= bound:
                U := [0] + [b for b in L] + [D-b for b in R] + [D]
                h := {u: c for u in U}
                h[0] := 0; h[D] := 0
                emit (U,h)
```

The zeros at the endpoints multiply the identically zero remainder factor. They impose no condition on the original $h$ there.

## All large diameters without a preset upper bound

For affine forms $u,w$, let `ROOT(u,w)` return the exact integer root at least ten of $u(D)=w(D)$ when its slope difference is nonzero and divides the negative constant difference. Otherwise it returns the empty set. Identities are handled separately.

``` {fontsize="\\small"}
LARGE_CERTIFICATE:
    for each (U,h) emitted by TEMPLATES:
        for a in {1,-1}:
            W := distinct affine forms {u+a*v: u,v in U}
            for A in W:
                for q in {-2,-1,0,1,2}:
                    V := empty dictionary keyed by affine letters in U
                    for each u=(alpha,beta) in U:
                        b := abs(beta)
                        V[u] := A + q*u + h[u]*(-b*D+b*b)
                    roots := empty set; identity_arrows := empty
                    for x,y in U:
                        w := V[y] - a*x
                        for z in U:
                            if w == z in Z[D]:
                                insert arrow (x,y)->(y,z)
                            add ROOT(w,z) to roots
                    extract all full-support identity-graph cycles
                    for D0 in roots:
                        E := {u(D0): u in U}
                        v := {u(D0): V[u](D0) for u in U}
                        record FULL_CYCLES(E,v,a)
```

At an endpoint $D=(1,0)$ the formula sets $b=0$, again giving the correct zero remainder factor. The unpruned algorithm is the independent reconstruction's scope. The author first prunes as follows; this can be inserted immediately after constructing $V$:

``` {fontsize="\\small"}
allowed := ALL
for value in V.values():
    if value is identical to some member of W: continue
    hits := union of ROOT(value,w) over w in W
    allowed := hits if allowed == ALL else intersection(allowed,hits)
if allowed is empty: discard model
if allowed != ALL: check only graphs at D in allowed
else: check generic graph and all exceptional edge roots
```

The correctness of this pruning was proved in Section [5](#sec:symbolic){reference-type="ref" reference="sec:symbolic"}. In the last branch the author evaluates at $D=1+\max(\{9\}\cup\mathrm{roots})$ for the generic graph; the unpruned algorithm builds it from identities. Neither procedure replaces an infinite range by an unproved finite sample.

# Why the independent reconstruction is equivalent {#app:independent}

## Different interpolation order and criterion

The independent checker orders an alphabet by alternating its smallest and largest remaining elements. For any such ordering $e_0,\ldots,e_{k-1}$, the highest coefficient of the interpolant on the first $j+1$ nodes is the Lagrange expression $$\label{eq:lagrange}
 c_j=\sum_{i=0}^j
 \frac{v(e_i)}{\prod_{\substack{0\le l\le j\\l\ne i}}(e_i-e_l)}.$$ The weights are computed as exact fractions, cleared to a common denominator, and tested by an integer congruence while enumerating the next value from $E+aE$. No Newton-basis polynomial is expanded.

To justify this different test, let $r_j$ interpolate the first $j+1$ values and let $r_{j-1}$ interpolate the preceding prefix. The difference vanishes at the first $j$ nodes and has degree at most $j$, so $$r_j-r_{j-1}=c_j\prod_{i<j}(t-e_i).$$ Starting with the constant prefix, induction proves that all $c_j\in\mathbb Z$ imply $r_j\in\mathbb Z[t]$. Conversely, an integral realizing polynomial has an integral monic-division remainder at each prefix, so every $c_j$ is integral. This proves equivalence to Lemma [\[lem:newton\]](#lem:newton){reference-type="ref" reference="lem:newton"} without requiring increasing node order.

## Indegree-zero peeling instead of path traversal

For a finite partial-function graph, the checker calculates indegrees and repeatedly removes an indegree-zero vertex, reducing the indegree of its successor if it has one. After this process, every remaining vertex has indegree at least one and outdegree at most one. No remaining edge points to a removed vertex: that vertex could not have been removed while such a predecessor remained. Counting edges now forces every remaining vertex to have exactly one incoming and one outgoing edge. The remaining graph is therefore a disjoint union of directed cycles. Reading them from their smallest unread state and retaining full coordinate support gives exactly the same cycle objects as Lemma [\[lem:graph\]](#lem:graph){reference-type="ref" reference="lem:graph"}.

The actual interpolation controls were $(0,1,2)\mapsto(0,1,4)$ and $(4,0,2)\mapsto(8,0,4)$, which pass, together with $(0,2)\mapsto(0,1)$ and $(0,2,4)\mapsto(0,0,4)$, which fail. For the graph controls, encode the four states of a two-letter alphabet by $0,1,2,3$. The arrow lists $$(\mathrm{EXIT},2,1,3),\qquad
 (1,2,3,\mathrm{EXIT}),\qquad (1,2,1,0)$$ produce, respectively, the full-support two-cycle $(1,2)$, no cycle, and the same two-cycle with incoming tails. The fixed state $3$ in the first control is excluded by the full-support condition. These checks test a distinction that simple orbit-return assertions would not catch.

## Unpruned roots and interpretation of the output

The independent symbolic implementation builds identity arrows directly from coefficient-pair equality, then solves every nonidentity edge equation for its integer root. It does not import the author graph function, apply the author output pruning or use a numerical representative for the generic graph. Left and right templates are both explicitly enumerated rather than removed by an assumed symmetry. This explains why it checks $512$ extra exceptional graphs while agreeing with the author's exclusion.

The independent code and complete output identify this actual reconstruction. The full-support cycle counts refer to instances in restriction graphs, not distinct cycles after identifying all polynomials with overlapping restrictions. In particular, these counts cannot be converted into a total-point bound for the original infinite family. The reconstruction validates the finite certificates conditional on the analytic reduction proved above; it does not replace that reduction or constitute a formal proof assistant certificate.
