---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--207-upper-neighbor-rank-dynamics"
canonical_tex: "symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/main.pdf"
source_sha256: "60f96c5fc8834582e4cafb37c2d7b20860dc8689f212024b054a3d92c1076a5b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two-Period Cores and Largest Fibres\protect of Upper-Neighbor Rank Dynamics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On a labelled ternary cycle, replace each height synchronously by the number of its two neighbors having strictly greater height. We classify the complete two-period core of this map and prove that every trajectory reaches it in at most $4n+2$ steps. This nonsharp bound uses an explicitly computer-assisted, fixed radius-six local lemma: failure of two-step equality creates a new permanent strict extremum. The all-length consequence is deductive, and the recurrent language has a separate two-time-column proof. An eight-role graph counts the core, and an exact single-seed wave gives entrance time $\lfloor n/2\rfloor+1$ for every $n\ge4$. Independently, we prove that the largest one-step fibre has size $L_{2\lfloor n/2\rfloor}$ and classify all attaining labelled targets, including both odd-length families and the length-three exception. The extremal argument compares noncommuting transfer kernels with different length costs; evaluating an alternating fibre alone does not give the comparison. Static rank decoders, classical Lucas counts, and the input-complement transfer from lower rank are separated from these temporal and global extremal statements.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Two-Period Cores and Largest Fibres\
  of Upper-Neighbor Rank Dynamics
```

## Markdown 正文

# The map and the scope of the results

For $n\ge3$, let $X_n=\{0,1,2\}^n$ with indices modulo $n$, and define $$\label{eq:map}
 U(x)_i=\mathbf 1_{\{x_{i-1}>x_i\}}+\mathbf 1_{\{x_{i+1}>x_i\}}.$$ The two neighbors are distinct, updates are synchronous, and equality contributes zero. Coordinates stay labelled throughout. Put $$h(x)=\min\{t\ge0:U^{t+2}x=U^t x\},\qquad H(n)=\max_{x\in X_n}h(x),$$ where existence of the minimum will be proved. We obtain an exact description of $\mathop{\mathrm{Fix}}(U^2)$, the nonsharp upper bound $H(n)\le4n+2$, an exact all-length seed clock, and a sharp maximum over all one-step target fibres. The temporal and extremal proofs use different information: permanent extrema constrain successive states, whereas a target's zero-run decomposition constrains its possible predecessors.

Local rank is a classical primitive. Zabih and Woodfill [@zabih1994nonparametric] define rank by the number of lower neighbors. If $F$ denotes that strict-lower rule on $X_n$ and $Jx=2-x$, then $$\label{eq:complement}
 U=FJ,\qquad U^{-1}(b)=J\bigl(F^{-1}(b)\bigr).$$ The inverse-set transfer is exact but gives no new inverse theorem by itself. It is not the conjugacy $JFJ$, so it does not identify the two iterations. For example, $0202$ is fixed by $F$ but is exchanged with $2020$ by $U$.

Mukherjee [@mukherjee2011local] directly studies iterative local rank. The primary preview inspected for this work defines strict lower rank and announces convergence; its convergence theorem and proof were not accessible. We do not infer their full scope, a dual iteration theorem, or a priority claim from that preview. The present results are self-contained for the literal map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, subject to the explicit finite certificate below. The sharp global entrance time for $n\ge4$, larger alphabets, and all-time inverse counts are not claimed.

Static comparison decoders and ordinary finite-graph traces are background tools here. In particular, the alternating extremal fibre is an independent-set set, or equivalently a two-chain crown order-map set; fence and crown enumeration has a classical literature [@currie1991number]. The distinct inverse assertion proved below is the maximum over *every* target, with all equality cases, not the Lucas count of that known family alone.

# A finite growth lemma and the exact two-period core

Call a site a strict extremum when it is strictly larger than both neighbors or strictly smaller than both; let $E(x)$ be their set.

[\[lem:permanent\]]{#lem:permanent label="lem:permanent"} $E(x)\subseteq E(Ux)$. Each such site alternates between strict minimum and strict maximum, and its values alternate between $0$ and $2$ after the first update.

A strict minimum becomes two, while either neighbor can count at most its other neighbor as greater and so becomes at most one. A strict maximum becomes zero, while both neighbors count the old maximum and so become at least one. The argument repeats at each step.

The following fixed finite lemma is the sole computer-assisted step in the all-orbit convergence proof. Its quantifiers and exhaustiveness argument are included to distinguish a finite certificate from an extrapolation of short cyclic trajectories.

[\[lem:local\]]{#lem:local label="lem:local"} Let $w=(w_{-6},\ldots,w_6)\in\{0,1,2\}^{13}$ and define its truncated forward cone by $v^0=w$ and $$v^{t+1}_j=\mathbf 1_{\{v^t_{j-1}>v^t_j\}}+\mathbf 1_{\{v^t_{j+1}>v^t_j\}},
 \qquad |j|\le5-t,\quad 0\le t<4.$$ If $v^4_0\ne v^2_0$, there are $1\le s\le4$ and $|j|\le5-s$ such that $j$ is a strict extremum in $v^s$ but not in $v^0$.

The accompanying standalone verifier enumerates all $3^{11}=177147$ inner words $(w_{-5},\ldots,w_5)$, forming their cones on $|j|\le5-t$. The time-two and time-four centers are determined there. Exactly $158643$ inner words have equal centers, so the premise is false for all nine exterior-letter choices. For $18300$ inner words with unequal centers, a witness satisfies $|j|\le4-s$; its row-$s$ neighbors and initial extremum test use only inner coordinates and persist for every exterior choice. The remaining $204$ inner words are each checked with all nine pairs $(w_{-6},w_6)$. All $1836$ extensions have a witness in the stated larger cone. The complete canonical output records these inner words and every extension witness.

These three disjoint cases exhaust every thirteen-letter word. Cone locality proves independence of the outer letters in the first two cases, rather than assuming it in the exceptions. Evolution is computed from edge signs and each witness is also tested by direct height inequalities. Thus the certificate covers all $3^{13}=1594323$ words, not a sample. Its successful finite execution is a declared proof dependency. A separate candidate checker has additionally enumerated all thirteen-letter words directly.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For every $n\ge3$, $U^{4n+4}=U^{4n+2}$ on $X_n$. In particular $H(n)\le4n+2$ and all periods are one or two.

Read thirteen coordinates around any site of a cycle, allowing repeated coordinates for $n<13$. This is one of the certified words. Its cone agrees with the cyclic trajectory wherever computed, by induction on time. If $E(U^4a)=E(a)$, monotonicity from Lemma [\[lem:permanent\]](#lem:permanent){reference-type="ref" reference="lem:permanent"} forbids a new extremum at any intermediate time. Applying Lemma [\[lem:local\]](#lem:local){reference-type="ref" reference="lem:local"} at every center gives $U^4a=U^2a$.

The $n+1$ inclusions between $E(U^{4q}x)$ for $q=0,\ldots,n+1$ cannot all be strict subsets of an $n$-element set. For some $0\le q\le n$, the four-step endpoint sets coincide. Hence $U^{4q+4}x=U^{4q+2}x$, so the orbit enters $\mathop{\mathrm{Fix}}(U^2)$ by $4q+2\le4n+2$. This set is forward invariant because $U$ commutes with its square. The claimed uniform identity follows.

The recurrent language below has a separate deductive proof; it does not depend on the local certificate. A run is maximal in the cyclic word, and the word's left-to-right orientation fixes its left and right boundaries.

[\[thm:core\]]{#thm:core label="thm:core"} The sole fixed point is $0^n$. Every other point of $\mathop{\mathrm{Fix}}(U^2)$ has both zero and positive entries and has the following run language:

1.  every zero run has length one or two;

2.  every positive run is $2,11,12,21$, or $121$;

3.  a positive run $12$ or $121$ has a singleton zero run on its left; a positive run $21$ or $121$ has one on its right.

Conversely every such labelled cyclic word belongs to $\mathop{\mathrm{Fix}}(U^2)$. All its nonzero members have exact period two.

Let $y=Ux$ and $x=Uy$. A height two maps to zero, so the possible temporal columns $(x_i,y_i)$ are $$S_0=(0,2),\quad S_1=(2,0),\quad W_0=(0,1),\quad
 W_1=(1,0),\quad N=(1,1),\quad (0,0).$$ At a $(0,0)$ column the two zero-output equations force both neighbors to be $(0,0)$. Connectedness then gives the all-zero state. Exclude that case. A neutral column $N$ needs one height-two neighbor at each time. They are distinct, hence are $S_0,S_1$ in either order. In particular a neutral column cannot neighbor a weak column.

At $W_0$, exactly one neighbor is positive in $x$, and no neighbor has height two in $y$. The zero $x$-neighbor must consequently be $W_0$, while the other is $S_1$ or $W_1$. The exclusion of $N$ uses the neutral site's *own* equation just proved. Interchanging the two times proves the rule for $W_1$. Each weak site therefore has exactly one same-phase weak neighbor: weak sites form unique adjacent dimers, with opposite-phase strong or weak exterior neighbors. An $S_0$ has neighbors $S_1,W_1$, or $N$, since both are positive in $x$; interchanging time gives the rule for $S_1$. Substitution shows these column rules are also sufficient for both time equations.

In the emitted word $x$, a zero run is one $S_0$ or one $W_0$ dimer. A positive run is one $S_1$ with an optional neutral on either side, or a $W_1$ dimer. The neutral's other neighbor must be a strong singleton zero, which gives precisely the two boundary restrictions. Conversely the stated run language recovers strong roles at twos and singleton zeros, weak roles on $00$ and $11$ dimers, and neutral roles on the remaining ones. The column rules hold at each coordinate, proving sufficiency. No zero-free exception occurs: a global maximum in a source gives a zero in every image of $U$.

A fixed point cannot contain two, since two maps to zero. Without twos, every one maps to zero as well. Thus only $0^n$ is fixed; the remaining core points have exact period two.

# Enumeration and an exact seed clock

Split weak dimers into left and right roles, and orient each neutral by its adjacent strong phases. In the order $$S_0,S_1,W_{0L},W_{0R},W_{1L},W_{1R},N_{01},N_{10},$$ the emitted heights are $0,2,0,0,1,1,1,1$. Let $Q$ be the adjacency matrix of the following complete transition list.

  Role       Following roles       Role       Following roles
  ---------- --------------------- ---------- ---------------------
  $S_0$      $S_1,W_{1L},N_{01}$   $S_1$      $S_0,W_{0L},N_{10}$
  $W_{0L}$   $W_{0R}$              $W_{0R}$   $S_1,W_{1L}$
  $W_{1L}$   $W_{1R}$              $W_{1R}$   $S_0,W_{0L}$
  $N_{01}$   $S_1$                 $N_{10}$   $S_0$

[\[prop:count\]]{#prop:count label="prop:count"} For $n\ge3$ the core size is $1+\mathop{\mathrm{tr}}Q^n$ and the number of two-cycles is $\mathop{\mathrm{tr}}Q^n/2$. Moreover $$\label{eq:det}
 D(z):=\det(I-zQ)=1-z^2-4z^3-2z^4+z^8.$$

Theorem [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"} uniquely recovers the role at each labelled position, including both ends of each weak dimer. Thus closed labelled walks of length $n$ are in bijection with nonzero core words. No rotation quotient is taken. Exchanging phase labels applies $U$ and pairs every such word with its distinct partner.

To evaluate the determinant, compress deterministic dimer and neutral roles. Strong blocks have length one, weak blocks length two; a neutral may appear only between successive strong blocks. Successive blocks have opposite phases, and the strong/weak block transfer is $$B(z)=\begin{pmatrix}z(1+z)&z^2\\z&z^2\end{pmatrix}.$$ Eliminating the intermediate roles from $I-zQ$ leaves $\bigl(\begin{smallmatrix}I&-B(z)\\-B(z)&I\end{smallmatrix}\bigr)$; the eliminated diagonal blocks have determinant one. Therefore $$\det(I-zQ)=\det(I-B(z))\det(I+B(z))
 =(1+z^4)^2-(z+2z^2)^2,$$ which is [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"}. This identity can also be checked by the explicit eight-by-eight determinant, as in the finite certificate.

Writing $a_n=\mathop{\mathrm{tr}}Q^n$, the standard formal identity $\sum_{n\ge1}a_nz^n=-zD'(z)/D(z)$ gives $$a_n=a_{n-2}+4a_{n-3}+2a_{n-4}-a_{n-8}\quad(n\ge9),$$ with $a_1,\ldots,a_8=0,2,12,10,20,62,84,154$. This is an enumeration of the proved language, not an additional dynamical assertion.

[\[prop:seed\]]{#prop:seed label="prop:seed"} $H(3)=1$. For every $n\ge4$, $$h(01^{n-1})=\lfloor n/2\rfloor+1,
 \qquad \lfloor n/2\rfloor+1\le H(n)\le4n+2.$$

Put $m=\lfloor n/2\rfloor$ and $z^s=U^s(20^{n-1})$. For $d(i)=\min\{i,n-i\}$ and $0\le s<m$, the exact profile is $$\label{eq:seed}
 z_i^s=\begin{cases}
 2\mathbf 1_{\{s\text{ even}\}},&d(i)=0,\\
 2\mathbf 1_{\{s-d(i)\text{ even}\}},&0<d(i)<s,\\
 1,&d(i)=s>0,\\
 0,&d(i)>s.
 \end{cases}$$ At $s=0$ this is the initial seed. Before the fronts meet, an interior site has opposite-phase neighbors and alternates; the frontier one has two zero neighbors and becomes zero. The next outer zero sees one positive neighbor and becomes one. Just inside the old front, a zero sees two positive neighbors and becomes two. The central seed alternates by Lemma [\[lem:permanent\]](#lem:permanent){reference-type="ref" reference="lem:permanent"}; more distant sites have zero neighbors. These cases prove the induction.

At time $m$, for $n=2m$ the sole remaining zero sees two frontier ones and becomes two, giving an alternating $02$ word. For $n=2m+1$, the two remaining zeros each see one frontier one and become the weak dimer $11$; the other sites are alternating strong sites. Both words lie in the core. For $1\le s<m$ a frontier is a strict maximum of height one, hence its value after two further updates is two by Lemma [\[lem:permanent\]](#lem:permanent){reference-type="ref" reference="lem:permanent"}; it is not in the core. The initial seed is outside the core because its zero run has length $n-1\ge3$. Thus $h(20^{n-1})=m$. Since $U(01^{n-1})=20^{n-1}$ and the latter is not initially recurrent, the source has entrance $m+1$.

For $n=3$ the cycle is the complete three-vertex graph. Equal heights map to $000$; two equal lower heights map to a rotation of $110$; two equal higher heights map to a rotation of $200$; three distinct heights map to a permutation of $210$. Each lies in the core. The nonrecurrent source $001$ shows the upper bound one is attained.

# The largest one-step fibres

Let $L_0=2$, $L_1=1$, $L_{t+2}=L_{t+1}+L_t$. Equation [\[eq:complement\]](#eq:complement){reference-type="eqref" reference="eq:complement"} allows us to count the strict-lower map $F$; the targets and their fibre sizes are unchanged for $U$. The full inverse sources for $U$ are obtained by complementing each source constructed below.

[\[thm:max\]]{#thm:max label="thm:max"} For every $n\ge3$, $$\max_{b\in X_n}|U^{-1}(b)|=L_{2\lfloor n/2\rfloor}.$$ For even $n=2m\ge4$, equality holds exactly at the two rotations of $(02)^m$. For odd $n=2m+1\ge5$, it holds exactly at all rotations of $$00(20)^{m-1}2\quad\text{and}\quad011(02)^{m-1},$$ giving $2n$ labelled targets. For $n=3$, the seven equality targets are $000$ and the rotations of $002$ and $011$.

## A complete static decoder

Every $F$-image has a zero at a source minimum. The fibre of $0^n$ consists of the three constant sources, because zero outputs at both ends of an edge force equality of its source heights. Otherwise, write the target's cyclic zero runs as $Z_1,\ldots,Z_r$ and its intervening nonempty positive runs as $w_1,\ldots,w_r$. The source is constant, say $a_j\in\{0,1,2\}$, on $Z_j$. If $u$ is the source on $w_j$, the two boundary inequalities are $a_j\le u_1$ and $a_{j+1}\le u_{|u|}$, with $a_{r+1}=a_1$.

A positive target position cannot have source height zero. An interior source one in a positive run would have two positive neighbors and output zero. Thus all interior source heights are two. Length five would contain three interior twos and give a zero at the middle one, so positive runs have length at most four. For outside heights $a,b$, the following list gives every possible positive source string $u$. Overlapping conditions on different rows describe distinct sources.

  Target $w$      Source $u$      Outside condition
  --------------- --------------- ------------------------------------------------------
  $2$             $1$; $2$        $a=b=0$; $a,b\in\{0,1\}$
  $1$             $1$; $2$        $(a,b)=(0,1),(1,0)$; $(a,b)=(0,2),(1,2),(2,0),(2,1)$
  $11$            $11$; $22$      $a=b=0$; $a,b\in\{0,1\}$
                  $12$; $21$      $(a,b)=(0,2)$; $(a,b)=(2,0)$
  $12$; $21$      $12$; $21$      $a=0,\ b\le1$; $a\le1,\ b=0$
  $111$           $122$; $221$    $a=0,\ b\le1$; $a\le1,\ b=0$
  $121$; $1111$   $121$; $1221$   $a=b=0$ in either case

For length one this checks heights one and two; for length two it checks $11,12,21,22$. At length three the middle is two, $222$ fails, and the remaining possibilities are $122,221,121$. At length four the middle pair is $22$ and positivity there forces both endpoints to one. This proves completeness of the list. Every unlisted target run is impossible.

Let $K_w[a,b]$ count the listed strings, with row and column order $0,1,2$. The eight nonzero word kernels are $$\begin{gathered}
 A=K_2=\begin{pmatrix}2&1&0\\1&1&0\\0&0&0\end{pmatrix},\quad
 J_0=K_1=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},\quad
 B_0=K_{11}=\begin{pmatrix}2&1&1\\1&1&0\\1&0&0\end{pmatrix},\\
 D_0=K_{12}=\begin{pmatrix}1&1&0\\0&0&0\\0&0&0\end{pmatrix},\quad
 K_{21}=D_0^{\mathsf T},\quad
 C_0=K_{111}=\begin{pmatrix}2&1&0\\1&0&0\\0&0&0\end{pmatrix},\\
 K_{121}=K_{1111}=E_0=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix}.\end{gathered}$$ The subscripts distinguish $J_0$ from input complement $J$, and $B_0$ from the generating-function matrix $B(z)$. Choose $a_1,\ldots,a_r$, fill the actual zero-run coordinates with those heights, and independently choose one listed source string for each positive run. The boundary inequalities enforce the required zero outputs. Conversely every source recovers exactly these choices. This labelled bijection gives $$\label{eq:fibretrace}
 |F^{-1}(b)|=\sum_{a_1,\ldots,a_r=0}^2
 \prod_{j=1}^r K_{w_j}[a_j,a_{j+1}]
 =\mathop{\mathrm{tr}}(K_{w_1}\cdots K_{w_r}).$$ It includes $r=1$, when both outside heights coincide. A different start cyclically permutes factors, without multiplying by rotations. Zero-run lengths affect reconstructed coordinates but not the kernels.

This decoder is static background. More generally, the source edge signs are recoverable; contracting their zero edges and orienting every remaining edge from lower to higher gives strict order-map sets on the resulting posets. The fibre is the disjoint union over compatible sign words, with no lost labels. The issue in Theorem [\[thm:max\]](#thm:max){reference-type="ref" reference="thm:max"} is to compare the sizes of these *whole* unions across rank targets.

## Uniform comparison of mixed kernels

Set $\lambda=(3+\sqrt5)/2$. We use the standard Schatten Hölder bound $$\label{eq:holder}
 |\mathop{\mathrm{tr}}(M_1\cdots M_r)|\le\prod_{j=1}^r\lVert M_j\rVert_{r}
 \qquad(r\ge2)$$ for real square matrices of equal size, with no commutation or invertibility hypothesis. Here $\lVert M\rVert_{p}$ is the $\ell^p$ norm of its singular values. To specify the source and exponents precisely, the two-factor unitarily invariant norm inequality in @tropp2022matrix [Example 6.18 and Theorem 6.32] yields $\lVert VW\rVert_{t}\le\lVert V\rVert_{pt}\lVert W\rVert_{qt}$ for $t\ge1$, $p,q>1$ conjugate. In the induction on the first $s$ factors use $t=r/s$, $p=s/(s-1)$, $q=s$, for $2\le s\le r$. Finally $|\mathop{\mathrm{tr}}P|\le\lVert P\rVert_{1}$ follows from an SVD, since the diagonal entries of the intervening orthogonal matrix have absolute value at most one. This proves [\[eq:holder\]](#eq:holder){reference-type="eqref" reference="eq:holder"} from that standard inequality with valid exponents throughout.

All kernels have nonnegative entries, and $D_0,D_0^{\mathsf T},C_0,E_0\le A$ entrywise. Replacing any of the five corresponding target-word kernels by $A$ cannot decrease the trace in [\[eq:fibretrace\]](#eq:fibretrace){reference-type="eqref" reference="eq:fibretrace"}: expand it as a sum of products of entries. No positive-semidefinite order claim is involved. In a resulting length-$r$ product, let $k$ count $B_0$ factors and $j$ count $J_0$ factors. The positive eigenvalues of $A$ are $\lambda,\lambda^{-1}$; write $$a_r=\lVert A\rVert_{r}=(\lambda^r+\lambda^{-r})^{1/r}.$$ The singular values of $J_0$ are $2,1,1$, and $\lVert B_0\rVert_{2}=3$. Monotonicity of vector norms gives $$\label{eq:normbounds}
 \lVert J_0\rVert_{r}\le\sqrt6<\lambda<a_r,\qquad
 \lVert B_0\rVert_{r}\le3\qquad(r\ge2).$$ For $r\ge3$ we also have $\lVert J_0\rVert_{r}\le\sqrt[3]{10}$ and $3\sqrt[3]{10}<\lambda^2\le a_r^2$. For instance $\lambda>13/5$ and $169^3>270\cdot25^3$ prove the strict cubic inequality; $\lambda^2=(7+3\sqrt5)/2>6$ proves the first strict comparison in [\[eq:normbounds\]](#eq:normbounds){reference-type="eqref" reference="eq:normbounds"}.

If $k=0$, Hölder bounds the trace by $a_r^r=\lambda^r+\lambda^{-r}$, strictly when $j>0$. If $k=1$ and $j=0$, cyclicity and the leading two-by-two block give $$\label{eq:oneb}
 \mathop{\mathrm{tr}}(B_0A^{r-1})=\mathop{\mathrm{tr}}A^r=\lambda^r+\lambda^{-r},$$ because $r-1\ge1$ removes the third-coordinate contribution. If $k=1$ and $j>0$, the case $r=2$ gives $\mathop{\mathrm{tr}}(B_0J_0)=4<7=\mathop{\mathrm{tr}}A^2$. For $r\ge3$, combine one $B_0$ and one $J_0$ in the *scalar product of norm bounds* using $3\sqrt[3]{10}<a_r^2$; every additional $J_0$ has smaller norm than $A$. The resulting bound is again strict below $a_r^r$.

For $k\ge2$, Hölder instead gives $$\label{eq:manyb}
 \mathop{\mathrm{tr}}(M_1\cdots M_r)\le a_r^{r-k}3^k
 <\frac{10}{9}\lambda^{r-k}3^k
 <\lambda^{r+\lfloor k/2\rfloor}.$$ Indeed $(a_r/\lambda)^r=1+\lambda^{-2r}<10/9$, since $r\ge2$ and $\lambda^4>9$; this also handles $r=k$. The last inequality is equivalent to $(10/9)3^k<\lambda^{k+\lfloor k/2\rfloor}$. For $k=2,3$ it is $10<\lambda^3$ and $30<\lambda^4$; increasing $k$ by two multiplies the two sides by $9$ and $\lambda^3>9$, respectively. This proves every mixed-product bound without commuting the factors.

## Length budget and complete equality analysis

Each positive run and a following nonempty zero run use at least two target positions, and each $B_0=K_{11}$ costs one extra. Consequently $$\label{eq:budget}
 n\ge2r+k.$$ The even Lucas subsequence satisfies $L_{2s}=\lambda^s+\lambda^{-s}$, since both sides start at $2,3$ and satisfy $V_{s+2}=3V_{s+1}-V_s$; it is strictly increasing for $s\ge1$. If $r\ge2$ and $k\le1$, the preceding bounds give a trace at most $L_{2r}\le L_{2\lfloor n/2\rfloor}$. For $k\ge2$, [\[eq:manyb\]](#eq:manyb){reference-type="eqref" reference="eq:manyb"} and [\[eq:budget\]](#eq:budget){reference-type="eqref" reference="eq:budget"} give a strict bound below $L_{2\lfloor n/2\rfloor}$.

Targets without zeros have no source. The all-zero target has fibre three. For $r=1$, the traces of $J_0,A,B_0,D_0,D_0^{\mathsf T},C_0,E_0$ are $0,3,3,1,1,2,1$; all other kernels vanish. These are below $L_4=7$ for $n\ge4$. At $n=3$, at most one positive run exists, so precisely $000$ and rotations of $002,011$ attain three. This proves the bound and all small-length cases.

For equality with $n\ge4$, we must have $r\ge2$, $k\le1$, and $q:=n-2r\in\{0,1\}$: if $q\ge2$, then $L_{2r}<L_{2\lfloor n/2\rfloor}$. If $q=0$, all positive and zero runs have length one. A positive run one gives $J_0$ and strictness, so equality holds exactly for alternating $02$ targets, which attain $\mathop{\mathrm{tr}}A^r=L_{2r}$.

If $q=1$, exactly one run has one extra position. If this is a zero run, all positive runs must again be two and the targets are the rotations of $00(20)^{r-1}2$. If it is a positive run, its nonzero kernel is $B_0,D_0$, or $D_0^{\mathsf T}$. For $B_0$, any $J_0$ factor gives strictness, and all remaining factors $A$ give equality by [\[eq:oneb\]](#eq:oneb){reference-type="eqref" reference="eq:oneb"}. This is the family $011(02)^{r-1}$. For $D_0$ or $D_0^{\mathsf T}$, a $J_0$ factor again makes the entrywise-replaced bound strict. Without $J_0$, the leading two-by-two block of $A^{r-1}$ is strictly positive, while $A-D_0$ and $A-D_0^{\mathsf T}$ are nonnegative and nonzero in that block. The trace expansion yields a strict inequality below $\mathop{\mathrm{tr}}A^r$. No longer run fits the single extra position. This exhausts all equality cases and proves Theorem [\[thm:max\]](#thm:max){reference-type="ref" reference="thm:max"}. The two odd families each have a unique doubled run, forbidding a nontrivial rotational stabilizer; the presence of ones distinguishes them. Each therefore gives $n$ labelled targets.

For completeness, the attainer's classical counting mechanism is explicit. For an alternating lower-rank target, source valleys have heights in $\{0,1\}$, peaks in $\{1,2\}$, and every valley is strictly lower than its adjacent peaks. Mark exactly the sites of source height one. These marks are an independent set of the labelled cycle, and the inverse construction puts zero on unmarked valleys, two on unmarked peaks, and one on marked sites. Its count is $L_{2m}$. Doubling a valley source height gives the odd $00$ family. Doubling a peak gives the odd $11$ family: its boundary valleys are in $\{0,1\}$, so the local source choices are precisely $11$ or $22$. Deleting the repeated position reverses either construction. These full set bijections explain attainment, but the mixed-target comparison above is needed to prove global optimality.

# Verification and limitations

The accompanying `verify.py` is a standalone author producer with complete canonical stdout and actual execution receipts. Its fixed local certificate is a proof dependency of Lemma [\[lem:local\]](#lem:local){reference-type="ref" reference="lem:local"}; the arbitrary-length implication is the separate argument in Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}. The certificate's decomposition accounts for every inner word and all required exterior extensions, including their literal witnesses. The independently implemented candidate check used all $3^{13}$ windows directly and an $81$-state height-overlap graph for $\mathop{\mathrm{Fix}}(U^2)$, rather than the author's inner-window partition and eight-role graph. These are process-separated internal checks, not external expert review.

Complete cyclic boxes $n=3,\ldots,10$ check every trajectory and every target fibre; seed profiles at further lengths check witnesses only. Those finite cyclic tests are not proofs of an all-length theorem. The entrance bound $4n+2$ is nonsharp, while the seed entrance and the one-step fibre maximum are exact. The local certificate is not a claimed short handwritten proof of its finite implication.

The static source decoder, edge-sign/order-map strata, independent-set attainer sets and Lucas identities are all deducted background. The whole-target extremal theorem is shared once with lower rank through input complement, not counted again as a separate family. The related lower-rank convergence theorem body discussed in Section 1 remains an access limitation; no claim of global novelty or exhaustive source clearance is made. A sharp uniform entrance formula, larger-alphabet classification, all-time fibres, and basin counts remain outside the results proved here.
