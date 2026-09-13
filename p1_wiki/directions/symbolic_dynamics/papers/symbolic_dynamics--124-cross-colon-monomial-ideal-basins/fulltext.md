---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--124-cross-colon-monomial-ideal-basins"
canonical_tex: "symbolic_dynamics/papers/124-cross-colon-monomial-ideal-basins/main.tex"
canonical_pdf: "symbolic_dynamics/papers/124-cross-colon-monomial-ideal-basins/main.pdf"
source_sha256: "a34a431f1e048e3d43871b630dbfee63ac31097a7eff45c134455e80f415ac56"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cross-Colon Dynamics on Rectangular Monomial Ideals: Complete Basins and a Four-State Contact Transfer

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/124-cross-colon-monomial-ideal-basins>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/124-cross-colon-monomial-ideal-basins/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/124-cross-colon-monomial-ideal-basins/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/124-cross-colon-monomial-ideal-basins/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/124-cross-colon-monomial-ideal-basins/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $R_{a,b}=k[x,y]/(x^a,y^b)$, and iterate $$T(I)=x(I:y)+y(I:x)$$ on its monomial ideals. We prove that the first occupied total-degree diagonal and the parities present on that diagonal determine the complete attractor basin: mixed parity leads to a fixed power of $(x,y)$, one parity leads to a checker-boundary two-cycle, and an empty source-free region leads to the terminal fixed power. Encoding ideal staircases by rectangle paths yields a four-state contact-parity recurrence for every basin size, uniformly in $a,b$, together with a ballot closed form for the terminal fixed basin. As supporting results, we classify all recurrent ideals and obtain the sharp maximum transient depth, including its square anomaly. Disjunctive path dynamics, monomial colon and staircase facts, and lattice-path reflection are treated as background. The owner search is bounded; no novelty, priority, or external-release claim is made.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Cross-Colon Dynamics on Rectangular Monomial Ideals:\
  Complete Basins and a Four-State Contact Transfer
```

## Markdown 正文

# The map, the question, and the claim boundary

Fix a field $k$ and positive integers $a,b$. Put $$R_{a,b}=k[x,y]/(x^a,y^b),\qquad
 \mathfrak m=(x,y),
 \qquad
 T(I)=x(I:y)+y(I:x).                                      \tag{1.1}\label{eq:map}$$ The state space $\mathcal M_{a,b}$ is the finite set of *monomial* ideals of $R_{a,b}$. Both colons in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} are taken from the same input, so the update is synchronous. Our main question is not only which periodic ideals occur, but which initial ideals feed each periodic orbit and how large each basin is.

Several interfaces are established and are assigned no contribution credit. Monomial ideals are classically encoded by exponent upper sets and staircases; colon operations on monomial ideals are standard [@MillerSturmfels2005; @AmbhoreSengupta2024]. After a change of coordinates, [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} becomes a family of disjunctive Boolean networks. The graph and Boolean-matrix theory of such networks, including periodic structure and transients, is well developed [@GolesHernandez2000; @JarrahLaubenbacherVelizCuba2010; @Gadouleau2021]. Likewise, boundary paths and reflection are standard enumerative tools [@Stanley2012], and general algebraic descriptions of Boolean-network basins are known [@AustinDinwoodie2015].

The same state space is visually adjacent to rowmotion and toggle dynamics on products of chains [@StrikerWilliams2012; @EinsteinPropp2021]. There is no conjugacy: rowmotion and toggle products are bijections, whereas [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} has transients in every rectangle. This comparison is a scope firewall, not contribution mass.

After these deductions, the residual package is:

1.  the literal cross-colon-to-diagonal translation and the upper-set compatibility that classifies recurrent ideals;

2.  a complete basin characterization by the first occupied diagonal and its parity trace; and

3.  a four-state contact transfer that counts every basin without enumerating the exponentially large ideal set.

The second and third items are the center of the paper. The recurrent census and sharp maximum depth support them. A bounded search found no direct statement of the literal map together with these conclusions; that non-hit is not a novelty or priority certificate.

# Staircase and diagonal coordinates

The residue classes $$\{x^iy^j:0\leq i<a,\ 0\leq j<b\}              \tag{2.1}$$ form a $k$-basis. A monomial ideal is an upper set in the exponent rectangle. Write its staircase as $$h(I)=(h_0,\ldots,h_{a-1}),\qquad
 b\geq h_0\geq\cdots\geq h_{a-1}\geq0,                    \tag{2.2}$$ where $x^iy^j\in I$ exactly when $j\geq h_i$.

[\[prop:normal\]]{#prop:normal label="prop:normal"} For $a\geq2$, the staircase $h'=h(T(I))$ is $$\begin{aligned}
h'_0&=\min(b,h_1+1),\\
h'_i&=\min\!\bigl(\max(0,h_{i-1}-1),h_{i+1}+1\bigr)
      &&(1\leq i\leq a-2),\\
h'_{a-1}&=\min\!\bigl(\max(0,h_{a-2}-1),1\bigr).
\end{aligned}                                             \tag{2.3}\label{eq:stair}$$ For $a=1$, $T(I)=(y)$ for every $I$.

On total degree $d$, put $$L_d=\max(0,d-b+1),\qquad U_d=\min(a-1,d),$$ and list membership along the diagonal as a binary word $w^{(d)}=(w_{L_d},\ldots,w_{U_d})$. Then diagonals do not interact and $$(G_d w)_s=w_{s-1}\vee w_{s+1},                           \tag{2.4}\label{eq:path}$$ where a missing left neighbor is the constant $\lambda_d=\mathbf1_{d\geq b}$, and a missing right neighbor is $\rho_d=\mathbf1_{d\geq a}$.

The threshold of $(I:y)$ in column $i$ is $\max(h_i-1,0)$: either multiplication by $y$ reaches $I$, or the top monomial is annihilated by $y$. Multiplication by $x$ shifts these thresholds one column. Similarly, $(I:x)$ has thresholds $h_1,\ldots,h_{a-1},0$, and multiplication by $y$ raises them by one with clipping at $b$. A sum of monomial ideals takes the coordinatewise minimum of thresholds, giving [\[eq:stair\]](#eq:stair){reference-type="eqref" reference="eq:stair"}. When $a=1$, $x=0$ and $(I:x)=R_{1,b}$, so $T(I)=(y)$.

For a basis cell $(i,j)$, literal membership is $$\begin{split}
x^iy^j\in T(I)\Longleftrightarrow\
&[\,i\geq1\ \text{and}\ (j=b-1\ \text{or}\ x^{i-1}y^{j+1}\in I)\,]\\
{}\vee{}&
[\,j\geq1\ \text{and}\ (i=a-1\ \text{or}\ x^{i+1}y^{j-1}\in I)\,].
\end{split}                                               \tag{2.5}$$ Both predecessors have total degree $i+j$. Reading them along the diagonal yields [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"} and the two wall sources.

Put $m=\min(a,b)$ and $M=\max(a,b)$. The component geometry is $$\begin{array}{c|c|c}
\text{degree range}&\text{word length}&(\lambda_d,\rho_d)\\ \hline
0\leq d<m&d+1&(0,0)\\
m\leq d<M&m&\text{exactly one source}\\
M\leq d\leq a+b-2&a+b-1-d&(1,1).
\end{array}                                               \tag{2.6}\label{eq:bands}$$ The middle band is absent precisely on a square.

# Supporting recurrent and depth classification

We record the path facts needed below. They are specialized background from disjunctive-network theory, included to fix endpoint conventions.

[\[lem:path\]]{#lem:path label="lem:path"} For a binary path word of length $n$ under [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"}:

1.  without sources and $n\geq2$, the recurrent words are the four words constant on each vertex-parity class; the two checkerboards form a two-cycle, and the maximum depth is $n-2$;

2.  without sources and $n=1$, only $0$ is recurrent and the maximum depth is one;

3.  with one source, $1^n$ is the unique recurrent word and the maximum depth is $n$;

4.  with two sources, $1^n$ is the unique recurrent word and the maximum depth is $\lceil n/2\rceil$.

With no sources, the $t$-th iterate records endpoints of length-$t$ walks in the path. For $t\geq n-2$, inserting or deleting an immediate backtrack shows $G^{t+2}=G^t$. A word satisfies $G^2w=w$ exactly when it is constant on each parity class. A single one at an endpoint attains depth $n-2$. The one-vertex exception is immediate.

A fixed source contributes all vertices within increasing graph distance. One source fills after $n$ updates, and two sources fill after $1+\max_i\min(i,n-1-i)=\lceil n/2\rceil$; the zero word attains both bounds. Any periodic state must equal the all-one future state.

For $1\leq r<m$ and $\epsilon\in\{0,1\}$, define $$C_r^\epsilon=
\bigl\langle x^iy^j:i+j>r\ \text{or}\
(i+j=r\ \text{and}\ i\equiv\epsilon\!\!\pmod2)\bigr\rangle. \tag{3.1}$$ This set is upward closed because every monomial of degree greater than $r$ is explicitly included.

[\[thm:support\]]{#thm:support label="thm:support"} The recurrent set is $$\operatorname{Rec}(T)=
\{\mathfrak m^r:1\leq r\leq m\}\ \dot\cup\
\{C_r^0,C_r^1:1\leq r<m\}.                               \tag{3.2}\label{eq:rec}$$ The $m$ powers are fixed, and $C_r^0,C_r^1$ form a two-cycle for each $r<m$. Thus there are $3m-2$ recurrent states and no other periods. Moreover, the sharp maximum transient depth is $$D(a,b)=
\begin{cases}
m,&a\ne b,\\
\max(1,m-2),&a=b=m.
\end{cases}                                               \tag{3.3}\label{eq:depth}$$

Every sourced recurrent diagonal is all one by [\[lem:path\]](#lem:path){reference-type="ref" reference="lem:path"}. A source-free recurrent diagonal is zero, all one, or a checkerboard. The upper shadow of an all-one diagonal is all one. If the next diagonal is still source-free, the shadow of a checkerboard contains adjacent occupied positions, while only the all-one recurrent word contains such a pair. If the next diagonal is sourced, it is already forced to be all one. Hence a recurrent ideal has a first nonzero diagonal $r$, every lower diagonal is zero, and every higher diagonal is all one. The first diagonal is all one, giving $\mathfrak m^r$, or is a checkerboard, giving $C_r^\epsilon$; the latter requires $r<m$. The actions on these words give the stated fixed points and two-cycles.

The diagonal projections commute with $T$, so an ideal's entrance time is the maximum of its component entrance times. Off the square, the one-source band in [\[eq:bands\]](#eq:bands){reference-type="eqref" reference="eq:bands"} contains a length-$m$ word and gives upper bound $m$, attained by the zero ideal. On a square this band is absent. The longest source-free contribution is $m-2$, while the two-source contribution is at most $\lceil(m-1)/2\rceil\leq\max(1,m-2)$. For $m\geq3$, the ideal $(y^{m-1})$ has a single endpoint one on the length-$m$ source-free diagonal and attains $m-2$. The unit ideal for $m=1$ and the zero ideal for $m=2$ attain depth one.

# The first-trace basin theorem

For a periodic orbit $\mathcal O$, let $$\mathcal B(\mathcal O)=
 \{I\in\mathcal M_{a,b}:T^t(I)\in\mathcal O\text{ for some }t\geq0\}. \tag{4.1}$$ For nonzero $I$, define $$\nu(I)=\min\{i+j:x^iy^j\in I\},\qquad
S_r(I)=\{i:x^iy^{r-i}\in I\},                             \tag{4.2}\label{eq:trace}$$ and put $\nu(0)=\infty$.

[\[thm:basins\]]{#thm:basins label="thm:basins"} If $m=1$, all monomial ideals lie in $\mathcal B(\{\mathfrak m\})$. Suppose $m\geq2$. Then:

1.  $\mathcal B(\{\mathfrak m\})$ consists of the unit ideal and the ideals with $\nu(I)=1$ whose first trace meets both parities;

2.  for $2\leq r<m$, $$I\in\mathcal B(\{\mathfrak m^r\})
    \Longleftrightarrow
    \nu(I)=r\ \text{and }S_r(I)\text{ meets both parities};   \tag{4.3}\label{eq:fixedbasin}$$

3.  $\mathcal B(\{\mathfrak m^m\})=\{I:\nu(I)\geq m\}$;

4.  for $1\leq r<m$, $$I\in\mathcal B(\{C_r^0,C_r^1\})
    \Longleftrightarrow
    \nu(I)=r\ \text{and }S_r(I)\text{ lies in one parity class}. \tag{4.4}\label{eq:checkerbasin}$$ If that parity is $\epsilon$, then, for every sufficiently large $t$, $$T^t(I)=C_r^{\epsilon+t\bmod2}.    \tag{4.5}\label{eq:phase}$$

Every diagonal below $\nu(I)$ is zero and remains zero. Take $1\leq r=\nu(I)<m$. Degree $r$ is a source-free path of length $r+1$. For all sufficiently large $t$, a vertex is occupied exactly when a length-$t$ walk reaches it from $S_r(I)$. If the initial support lies in one parity $\epsilon$, this fills precisely parity $\epsilon+t\bmod2$. If it meets both parities, it fills the whole diagonal.

The orbit eventually enters the recurrent set. The upper-set compatibility in the proof of [\[thm:support\]](#thm:support){reference-type="ref" reference="thm:support"} leaves only one recurrent ideal with the specified first diagonal: the relevant checker phase in the first case and $\mathfrak m^r$ in the second. This proves [\[eq:fixedbasin\]](#eq:fixedbasin){reference-type="eqref" reference="eq:fixedbasin"}--[\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"}.

If $\nu(I)\geq m$, all source-free diagonals stay zero and every sourced diagonal eventually fills, giving $\mathfrak m^m$. If $\nu(I)=0$, then $I=R$ and $T(R)=(x)+(y)=\mathfrak m$. These cases also show that, when $m=1$, every ideal enters the sole fixed basin.

The theorem is stronger than the recurrent census: it assigns every one of the $\binom{a+b}{a}$ monomial ideals to an attractor using a single diagonal trace. It also retains phase information inside each checker basin.

# A four-state contact-parity transfer

We now count the sets in [\[thm:basins\]](#thm:basins){reference-type="ref" reference="thm:basins"}. Encode a staircase $h=(h_0,\ldots,h_{a-1})$ by the unique east/south path from $(0,b)$ to $(a,0)$ that descends to height $h_i$ before its east step from abscissa $i$. This is a bijection between $\mathcal M_{a,b}$ and the $\binom{a+b}{a}$ rectangle paths.

Fix $1\leq r<m$. For $Q\subseteq\{E,O\}$, let $F^{(r)}_{i,j}(Q)$ count path prefixes from $(0,b)$ to $(i,j)$ that stay in $i+j\geq r$, where $Q$ records the parities of abscissae at which the prefix contacts $i+j=r$. Initialize $$F^{(r)}_{0,b}(\varnothing)=1.       \tag{5.1}$$ Entries outside the rectangle or below the barrier are zero. At an allowed vertex different from the start, set $$A_{i,j}(Q)=F^{(r)}_{i-1,j}(Q)+F^{(r)}_{i,j+1}(Q).          \tag{5.2}$$ If $i+j>r$, set $F^{(r)}_{i,j}=A_{i,j}$. If $i+j=r$, set $$F^{(r)}_{i,j}(Q)=
\sum_{Q':\,Q'\cup\{i\bmod2\}=Q}A_{i,j}(Q'),               \tag{5.3}\label{eq:transfer}$$ identifying parity zero with $E$ and parity one with $O$. Finally put $$A_r^E=F^{(r)}_{a,0}(\{E\}),\quad
A_r^O=F^{(r)}_{a,0}(\{O\}),\quad
A_r^M=F^{(r)}_{a,0}(\{E,O\}).                             \tag{5.4}$$

[\[thm:counts\]]{#thm:counts label="thm:counts"} For $m\geq2$, $$\begin{aligned}
|\mathcal B(\{\mathfrak m\})|&=1+A_1^M=2,\\
|\mathcal B(\{\mathfrak m^r\})|&=A_r^M &&(2\leq r<m),\\
|\mathcal B(\{C_r^0,C_r^1\})|&=A_r^E+A_r^O &&(1\leq r<m),\\
|\mathcal B(\{\mathfrak m^m\})|
 &=\binom{a+b}{a}-\binom{a+b}{m-1}.
\end{aligned}                                             \tag{5.5}\label{eq:counts}$$ For $m=1$, the sole basin has size $\binom{a+b}{a}$. Moreover, $$A_r^E+A_r^O+A_r^M
=\binom{a+b}{r}-\binom{a+b}{r-1},                         \tag{5.6}\label{eq:layer}$$ and the basin sizes in [\[eq:counts\]](#eq:counts){reference-type="eqref" reference="eq:counts"} partition $\binom{a+b}{a}$.

The condition $\nu(I)\geq r$ is $$h_i\geq r-i\quad(0\leq i\leq r), \tag{5.7}$$ equivalent to the boundary path staying above $i+j=r$. It contacts the barrier at $(i,r-i)$ exactly when $h_i=r-i$, equivalently when $x^iy^{r-i}\in I$. Thus the contact-parity mask is the parity mask of $S_r(I)$. The last-step recurrence [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"} counts each path once, so [\[thm:basins\]](#thm:basins){reference-type="ref" reference="thm:basins"} gives the first three lines of [\[eq:counts\]](#eq:counts){reference-type="eqref" reference="eq:counts"}. For $r=1$, the only mixed trace is $\{0,1\}$, whose upper closure is $\mathfrak m$, hence $A_1^M=1$.

For the remaining formulas, write $z=i+j-r$. East and south steps change $z$ by $+1$ and $-1$; the endpoints have heights $b-r$ and $a-r$. Reflecting a bad path through its first visit to $-1$ produces an unrestricted path with $r-1$ south steps. Hence the number staying above the barrier is $$B_{\geq r}=\binom{a+b}{a}-\binom{a+b}{r-1}.               \tag{5.8}$$ At $r=m$, this is the last fixed basin. For $r<m$, paths that touch barrier $r$ are counted by $$B_{\geq r}-B_{\geq r+1}
=\binom{a+b}{r}-\binom{a+b}{r-1}.$$ The three nonempty masks partition them, proving [\[eq:layer\]](#eq:layer){reference-type="eqref" reference="eq:layer"}. Adding the degree-zero unit ideal and the terminal class gives the total $\binom{a+b}{a}$.

For fixed $r$, [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"} uses $4(a+1)(b+1)$ integer entries. All basin sizes require $O(abm)$ arithmetic operations and reusable $O(ab)$ storage; this is not an ideal-by-ideal enumeration.

::: {#tab:example}
     orbit       $P_1$   $C_1$   $P_2$   $C_2$   $P_3$   $C_3$   $P_4$   $C_4$   $P_5$
  ------------ ------- ------- ------- ------- ------- ------- ------- ------- -------
   basin size        2      10       9      45      38     116      90     185     297

  : Basin sizes for $(a,b)=(5,7)$. Here $P_r$ denotes the fixed power $\mathfrak m^r$, and $C_r$ denotes the checker two-cycle.
:::

The entries in [1](#tab:example){reference-type="ref" reference="tab:example"} sum to $\binom{12}{5}=792$. The transfer further splits the checker counts into even-only and odd-only traces: $(4,6),(30,15),(44,72),(139,46)$ for $r=1,2,3,4$.

# Exact controls, limitations, and conclusion

Two paper-local standard-library programs give independent finite controls. The first compares literal basis arithmetic, [\[eq:stair\]](#eq:stair){reference-type="eqref" reference="eq:stair"}, and [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"}; it exhausts all $184{,}736$ ideals for $1\leq a,b\leq9$, all source types through path length $14$, the recurrent families, and sharp depths. It makes $1{,}469{,}669$ exact assertions.

The second reimplements literal colon arithmetic without importing the first program. It follows all $48{,}602$ ideals for $1\leq a,b\leq8$, compares their actual attractors with [\[thm:basins\]](#thm:basins){reference-type="ref" reference="thm:basins"}, and compares every basin count with [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"}. It also checks reflection, partition, and transpose identities through $a,b\leq30$, for $265{,}987$ assertions. The combined total is $1{,}735{,}656$. These computations are falsification controls, not proofs of quantified statements or ownership.

The scope remains narrow. We do not treat nonmonomial ideals, asynchronous updates, higher-dimensional truncations, iterated fibre counts, or scalar closed forms for the separate even-only and odd-only contact counts. We claim no new OR-network theorem, ballot method, staircase theory, rowmotion action, novelty, or priority. Public release remains on hold.

Within that boundary, the literal crossed-colon map admits a complete finite dynamical description centered on basins: one first trace chooses the attractor, and four contact states count every basin for all rectangle sizes. The recurrent census and square depth anomaly are supporting shadows of the same diagonal geometry.
