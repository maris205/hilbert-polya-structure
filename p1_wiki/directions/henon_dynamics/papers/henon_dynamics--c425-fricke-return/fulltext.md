---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c425-fricke-return"
canonical_tex: "henon_dynamics/research_c424_c428/papers/C425_fricke_return/main.tex"
canonical_pdf: "henon_dynamics/research_c424_c428/papers/C425_fricke_return/main.pdf"
source_sha256: "1d9df3c901777f5993ea4ac586be1b4aa29c4a8c3aa729bfef8d7caffbe4cc8a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Integral periodic orbits of a general Fricke return word

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c424_c428/papers/C425_fricke_return>)
- [规范 TeX](<../../../../../henon_dynamics/research_c424_c428/papers/C425_fricke_return/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c424_c428/papers/C425_fricke_return/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c424_c428/papers/C425_fricke_return/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c424_c428/papers/C425_fricke_return/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give an effective classification of the integral periodic points of the ordered return map obtained by applying the three Vieta involutions of a Fricke cubic once each. For every ordered integer coefficient triple $(A,B,C)$, the classification holds on the entire integer lattice and simultaneously on every invariant level, including singular levels. Put $H=\max(|A|,|B|,|C|)$ and $R=100(H+1)$. The periodic locus is the union of at most 27 explicitly constructed affine integer lines and the cyclic vertices of an exact partial map on $[-R,R]^3\cap\mathbb Z^3$. Every line has a certified return time at most 54 in the original three-involution clock. A global maximum on a periodic scalar sequence forces two neighboring coordinates into $\{-1,0,1\}$; above the threshold, successive transitions in a 27-state phase-labelled graph are forced. Bijective affine parameter maps then place every large periodic orbit in a finite union of whole periodic lines. Polynomial greatest common divisors determine the least periods and all exceptional line parameters, while a terminating finite rule determines the residual cycles. Each invariant level meets each line in at most two points, giving at most $54+(2R+1)^3$ periodic integer points per level and effective ordinary cycle counts. The bounds are not claimed sharp, and the residual procedure is proved rather than reported as an executed census.
author:
- Anonymous
bibliography:
- references.bib
date: 9 September 2026
title: Integral periodic orbits of a general Fricke return word
```

## Markdown 正文

# The classification and its scope {#sec:introduction}

An integral periodic orbit of one polynomial automorphism is a different object from a finite orbit of the group containing that automorphism. For Fricke cubics this distinction matters: the geometry of the Vieta group provides reduction methods, but the periodic points of one prescribed word must still be exhausted in that word's own time. We study the word containing the three Vieta involutions in a fixed order. The result separates its unbounded integral periodic families from a bounded, effectively decidable remainder, with one bound for all levels.

Fix an arbitrary ordered triple $(A,B,C)\in\mathbb Z^3$, and define $$\label{eq:invariant}
 K(x,y,z)=x^2+y^2+z^2-xyz-Ax-By-Cz.$$ The Vieta involutions are $$\begin{aligned}
 s_x(x,y,z)&=(A+yz-x,y,z),\notag\\
 s_y(x,y,z)&=(x,B+xz-y,z),\label{eq:involutions}\\
 s_z(x,y,z)&=(x,y,C+xy-z).\notag\end{aligned}$$ Our native map is $$\label{eq:native}
 T=s_z\circ s_y\circ s_x,$$ so the rightmost factor acts first. One application of $T$, not one individual involution, is one unit of time. Each factor preserves $K$, and each is a polynomial involution of $\mathbb Z^3$. In particular, no point is removed when a level $K=D$ is singular.

Write $\operatorname{Per}_\mathbb Z(T)=\{P\in\mathbb Z^3:T^nP=P\text{ for some }n\ge1\}$, and set $$\label{eq:bounds}
 \begin{gathered}
 H=\max(|A|,|B|,|C|),\qquad B_0=H+1,\qquad R=100B_0,\\
 Q_R=[-R,R]^3\cap\mathbb Z^3,\qquad N_R=(2R+1)^3.
 \end{gathered}$$ For a periodic point, its *least period* is its first positive return time. A *certified return time* need not be the least period.

[\[thm:main\]]{#thm:main label="thm:main"} For every ordered $(A,B,C)\in\mathbb Z^3$, there is an explicit construction of a union $\mathcal L$ of at most 27 affine integer lines such that:

1.  Each line has a parametrization $P(t)=p+tv$, with $p,v\in\mathbb Z^3$, containing a coordinate of slope $1$ or $-1$. It consists entirely of periodic points and has a certified native return time $r\le54$: $T^rP(t)=P(t)$ for all $t\in\mathbb Z$.

2.  If $\mathcal C_R$ denotes the cyclic vertices of the exact partial map $T:Q_R\dashrightarrow Q_R$, then $$\label{eq:exhaustive_union}
        \operatorname{Per}_\mathbb Z(T)=\mathcal L\cup\mathcal C_R.$$ Every periodic orbit not contained in $\mathcal L$ lies entirely in $Q_R$.

3.  A finite parameterwise procedure determines coincident lines, all integral intersections, the generic least period and every exceptional parameter on each line, and all remaining finite cycles. Thus all least periods and their coexistence are effective. Every native least period is at most $\max(54,N_R)$.

4.  For every $D\in\mathbb Z$, the level $K=D$ contains at most $54+N_R$ periodic integer points. Their exact least periods and their ordinary primitive-cycle counts are effectively determined.

The construction uses the 27-state graph of Section [3](#sec:graph){reference-type="ref" reference="sec:graph"} and its affine-return test. Neither the numerical bounds nor the resulting algorithmic complexity are asserted optimal.

The line part is a finite list of free integer parametrizations. The core part is a proved terminating rule for the given coefficients, not a table that has been computed for every coefficient triple. There is no empirical parameter window or period cutoff in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Its proof is given completely below.

## Related results and the contribution retained here {#subsec:ownership}

Shin's reduction theory uses height graphs and low-coordinate Vieta identities to study integral group orbits [@shin2026character Theorems 1.1--1.3 and §2]. In particular, the orbit-equivalence algorithms concern the full Vieta group and the mapping class group. Remark 3.1 in the accepted manuscript explicitly removes the boundary-trace relations between the coefficients. Independent coefficients and the height-graph and low-coordinate mechanisms are therefore prior work, not an extension claimed here. The integral change $(x,y,z)\mapsto(-x,y,z)$ identifies our sign convention with Shin's, with parameters $(\alpha_1,\alpha_2,\alpha_3,\beta)=(-A,B,C,D)$, and conjugates the respective ordered involutions. The additional assertion proved here is the fixed-word, level-uniform line/core exhaustion, not decidability of whole-group orbit equivalence.

Cantat studies positive-entropy automorphisms on the same cubic family [@cantat2009bers Proposition 2.2 and §3]. The fixed-fibre escape neighborhoods in that analysis imply compact containment of periodic points, and hence integral finiteness on a fixed fibre. This consequence is already available and is not our novelty claim. It does not furnish the particular level-independent radius or integer line construction used here. Our periodic lines cross invariant levels; they are not invariant curves inside a fixed cubic surface, so they do not conflict with Cantat's Corollary 3.4.

The equal-forcing slice is also prior work. The local working manuscript C421 classifies all integer periodic orbits of $F_a(x,y,z)=(y,z,yz+a-x)$, including its exceptional families and computer-assisted finite core [@c4212026integral]. When $A=B=C=a$, our map is exactly $F_a^3$. That slice is not counted as a new classification here, and its finite certificate is not an input to our proof. The phase-dependent argument below handles every ordered coefficient triple without importing a homogeneous difference identity or assuming a reversal symmetry of its forcing sequence.

Other nearby questions have different observables. Vishkautsan studies strong residual periodicity for products of two reflections on the unforced Markoff surface, with periodic conics explaining the local--global phenomenon [@vishkautsan2016residual]. Abboud proves rigidity statements comparing periodic sets of loxodromic affine-surface automorphisms [@abboud2025rigidity Theorem A]. Planat, Chester and Irwin discuss selected algebraic Painlevé VI solutions in their study of Fricke surfaces [@planat2024dynamics]. These are contextual comparisons, not dependencies of the present exhaustion proof.

@\>p0.20YY@ Input or comparison & Scope already available & Scope proved here\
Shin [@shin2026character] & Independent coefficients; height and low-coordinate group-orbit reduction & Exhaustion for the prescribed three-factor word, uniformly in the level\
Cantat [@cantat2009bers] & Fixed-fibre dynamics and the resulting integral finiteness & An explicit residual radius depending only on $A,B,C$\
C421 [@c4212026integral] & The complete equal-forcing scalar classification & Phase-dependent forcing, including unequal ordered coefficients\
Elementary algorithms & Affine returns, finite graphs, polynomial gcds and cycle products & Their applicability to every remaining point, by the global exhaustion proof\

The mathematical step is the implication that every periodic orbit above $R$ belongs to a finite union of whole periodic lines. We prove it by a global-maximum entry, forced finite-state propagation and backward exhaustion using bijective line maps. The source comparisons above concern the inspected statements and are not a worldwide priority certificate. Section [2](#sec:phase){reference-type="ref" reference="sec:phase"} fixes the clock and maximum; Sections [3](#sec:graph){reference-type="ref" reference="sec:graph"}--[5](#sec:lines){reference-type="ref" reference="sec:lines"} prove the line exhaustion; Sections [6](#sec:effective){reference-type="ref" reference="sec:effective"}--[7](#sec:levels){reference-type="ref" reference="sec:levels"} give the exact residual and level-count procedures.

# The phase lift and entry at a global maximum {#sec:phase}

Set $a_0=A$, $a_1=B$, $a_2=C$, with all forcing subscripts interpreted modulo three. Introduce the auxiliary map $$\label{eq:lift}
 F(i;x,y,z)=(i+1;y,z,yz+a_i-x),
 \qquad i\in\mathbb Z/3\mathbb Z.$$ It is a bijection, with inverse $$\label{eq:lift_inverse}
 F^{-1}(i;x,y,z)=(i-1;xy+a_{i-1}-z,x,y).$$ Three lifted steps from phase zero update the first coordinate using $A$, then the second using $B$, then the third using $C$. Consequently $$\label{eq:clock}
 F^3(0;P)=(0;T(P)).$$ The phase label is part of the auxiliary state and is never discarded while taking returns.

If $T^nP=P$, write $P=(x_0,x_1,x_2)$ and read successive coordinates along the lifted orbit. They form a two-sided periodic scalar sequence satisfying $$\label{eq:recurrence}
 x_{j+3}+x_j=x_{j+1}x_{j+2}+a_j,\qquad j\in\mathbb Z.$$ Its period divides $3n$. Define $$\label{eq:global_max}
 M=\max_{j\in\mathbb Z}|x_j|.$$ This maximum exists because the scalar sequence is periodic. Moreover, $T^kP=(x_{3k},x_{3k+1},x_{3k+2})$, so these native triples partition the scalar positions and $$\label{eq:max_native}
 M=\max_{0\le k<n}\operatorname{ht}(T^kP),\qquad
 \operatorname{ht}(x,y,z)=\max(|x|,|y|,|z|).$$ Thus no intermediate factor update can hide a larger maximum than the one present among the native orbit's coordinates.

[\[lem:entry\]]{#lem:entry label="lem:entry"} Suppose $M>H+2$ and $|x_j|=M$ in a periodic scalar sequence satisfying [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. Then $x_{j-1},x_{j+1}\in\{-1,0,1\}$.

The recurrences at $j-2$ and $j-1$ give $$x_{j-1}x_j=x_{j+1}+x_{j-2}-a_{j-2},\qquad
 x_jx_{j+1}=x_{j+2}+x_{j-1}-a_{j-1}.$$ Every coordinate has absolute value at most $M$, whence $$|x_{j-1}|,|x_{j+1}|\le 2+H/M<3.$$ Integrality first bounds both neighbors by two. If $|x_{j+1}|=2$, the second recurrence yields $$|x_{j+2}|\ge2M-|x_{j-1}|-H
             \ge2M-2-H>M,$$ a contradiction. If $|x_{j-1}|=2$, use the first recurrence in the form $x_{j-2}=x_{j-1}x_j+a_{j-2}-x_{j+1}$ to obtain the same contradiction on the left. Both neighbors therefore have absolute value at most one.

Put $S=\{-1,0,1\}$. The lemma places the lifted orbit on one of the 27 labelled state lines $$\label{eq:state_line}
 L_{i,u,v}(t)=(i;u,t,v),\qquad
 (i,u,v)\in(\mathbb Z/3\mathbb Z)\times S^2,\quad t\in\mathbb Z,$$ with $|t|=M$. Entry is justified by a genuine global maximum. We will not apply Lemma [\[lem:entry\]](#lem:entry){reference-type="ref" reference="lem:entry"} again to a merely large, possibly nonmaximal coordinate; the next section's identities and Section [4](#sec:forcing){reference-type="ref" reference="sec:forcing"}'s estimates supply the needed propagation.

# The exact 27-state graph {#sec:graph}

The graph $\mathcal G_{A,B,C}$ has state set $(\mathbb Z/3\mathbb Z)\times S^2$. Each state $s=(i,u,v)$ has at most one outgoing edge. An edge carries a lifted length $h_s$ and an affine integer parameter map $\phi_s$. The edge identity is $$\label{eq:edge_identity}
 F^{h_s}L_s(t)=L_{s'}(\phi_s(t))\qquad(t\in\mathbb Z),$$ where $s'$ is its terminal state. Table [\[tab:edges\]](#tab:edges){reference-type="ref" reference="tab:edges"} defines all edges; the conditions are part of the definition.

\@p0.10Yp0.21cp0.18@ Type & Existence condition & Terminal state $s'$ & $h_s$ & $\phi_s(t)$\
I & $v=\pm1$, $b=a_i-u$, $c=vb+a_{i+1}\in S$ & $(i+2,v,c)$ & 2 & $vt+b$\
II & $v=0$, $a_i=u$, $a_{i+2}\in S$ & $(i,0,a_{i+2})$ & 3 & $-t+a_{i+1}$\

[\[lem:edges\]]{#lem:edges label="lem:edges"} Every edge in Table [\[tab:edges\]](#tab:edges){reference-type="ref" reference="tab:edges"} satisfies [\[eq:edge\_identity\]](#eq:edge_identity){reference-type="eqref" reference="eq:edge_identity"} for all integer parameters. Its map $\phi_s(t)=\epsilon_s t+\delta_s$ has $\epsilon_s\in\{1,-1\}$ and $|\delta_s|\le B_0$. Every intermediate image $F^rL_s(\mathbb Z)$, $0\le r<h_s$, is an affine integer line with an injective parametrization containing a coordinate of slope $1$ or $-1$.

For Type I, direct substitution gives $$\begin{aligned}
 F(i;u,t,v)&=(i+1;t,v,vt+b),\\
 F^2(i;u,t,v)&=(i+2;v,vt+b,v(vt+b)+a_{i+1}-t)\\
             &=(i+2;v,vt+b,c).\end{aligned}$$ The last equality uses $v^2=1$. If $c\in S$, this is precisely the required terminal line. The additional intermediate line has triple $(t,v,vt+b)$.

For Type II, the assumptions $v=0$ and $a_i=u$ give $$\begin{aligned}
 F(i;u,t,0)&=(i+1;t,0,0),\\
 F^2(i;u,t,0)&=(i+2;0,0,-t+a_{i+1}),\\
 F^3(i;u,t,0)&=(i;0,-t+a_{i+1},a_{i+2}).\end{aligned}$$ The final triple is the stated terminal line exactly when $a_{i+2}\in S$. The displayed intermediate triples prove all the line assertions. Finally, $|a_i-u|\le H+1=B_0$ and $|a_{i+1}|\le H\le B_0$, proving the translation bounds.

The edge identities concern whole lines, not asymptotic expansions. In particular the affine parameter maps are bijections of $\mathbb Z$. An omitted edge need not rule out a small periodic parameter at its state. The uniform height argument below rules it out only for a periodic orbit whose current parameter remains sufficiently close to the global maximum.

# Uniform forcing above the residual radius {#sec:forcing}

[\[lem:forcing\]]{#lem:forcing label="lem:forcing"} Let a lifted periodic orbit have global scalar maximum $M>100B_0$. Suppose it visits $L_{i,u,v}(t)$ with $$\label{eq:parameter_lower}
 |t|\ge M-jB_0,\qquad 0\le j\le27.$$ Then the outgoing edge from $(i,u,v)$ in $\mathcal G_{A,B,C}$ exists. The parameter at its terminal state has absolute value at least $M-(j+1)B_0$.

All scalar coordinates on the orbit are bounded by the same $M$. We check each way in which Table [\[tab:edges\]](#tab:edges){reference-type="ref" reference="tab:edges"} could omit an edge.

If $v=\pm1$, put $b=a_i-u$, $t'=vt+b$ and $c=vb+a_{i+1}$. The two-step identity in Lemma [\[lem:edges\]](#lem:edges){reference-type="ref" reference="lem:edges"} still holds without assuming $c\in S$, and $$|t'|\ge |t|-B_0\ge M-28B_0.$$ If $|c|\ge2$, the next scalar coordinate, following $(v,t',c)$, is $t'c+a_{i+2}-v$. Its magnitude is at least $$\label{eq:typeI_bound}
 2(M-28B_0)-H-1=2M-57B_0>M.$$ This contradicts the global maximum. Hence $c\in S$, and a Type I edge exists.

Now suppose $v=0$. Write $b=a_i-u$ and $t'=-t+a_{i+1}$, so once more $|t'|\ge M-28B_0$. Starting with $(u,t,0)$, the next scalar coordinates are exactly $$\label{eq:zero_successors}
 b,\qquad t',\qquad bt'+a_{i+2},\qquad
 t'(bt'+a_{i+2})-b+a_i.$$ There are three exhaustive possibilities for $b$.

If $|b|\ge2$, the third coordinate in [\[eq:zero\_successors\]](#eq:zero_successors){reference-type="eqref" reference="eq:zero_successors"} has magnitude at least $$2(M-28B_0)-H=2M-56B_0-H>M,$$ which is impossible. If $|b|=1$, that coordinate has magnitude at least $M-29B_0$. Since $a_i-b=u$ and $|u|\le1\le B_0$, the fourth coordinate has magnitude at least $$\label{eq:quadratic_bound}
 (M-28B_0)(M-29B_0)-B_0>M.$$ To verify the strict inequality, both factors exceed $M/2$, and $M>100B_0\ge100$ implies $M^2/4-B_0>M^2/4-M/100>M$. Thus $|b|=1$ is also impossible.

It follows that $b=0$, or $a_i=u$. If $|a_{i+2}|\ge2$, the fourth coordinate in [\[eq:zero\_successors\]](#eq:zero_successors){reference-type="eqref" reference="eq:zero_successors"} has magnitude at least $$2(M-28B_0)-H>M,$$ another contradiction. Therefore $a_{i+2}\in S$, exactly the remaining Type II condition. For either edge type the new parameter is $\epsilon t+\delta$, with $|\delta|\le B_0$, and hence is bounded below by $M-(j+1)B_0$ in absolute value.

[\[prop:graph\_cycle\_entry\]]{#prop:graph_cycle_entry label="prop:graph_cycle_entry"} Every native periodic orbit of height greater than $R$ has a lift that reaches a directed cycle of $\mathcal G_{A,B,C}$.

By [\[eq:max\_native\]](#eq:max_native){reference-type="eqref" reference="eq:max_native"}, its global scalar maximum satisfies $M>R=100B_0>H+2$. Lemma [\[lem:entry\]](#lem:entry){reference-type="ref" reference="lem:entry"} supplies a state-line point with parameter of absolute value $M$. Apply Lemma [\[lem:forcing\]](#lem:forcing){reference-type="ref" reference="lem:forcing"} successively for $j=0,1,\ldots,26$. This produces 27 exact transitions and 28 visited states. The state set has size 27, so a state repeats. Since each state has at most one outgoing edge, the segment between its first two appearances is a directed cycle, and the path has entered that cycle.

This is a finite propagation argument, not an indefinitely iterated height estimate. It uses the lower bound only until a state repeats. After the repetition, the exact whole-line identities control all subsequent returns.

# Affine returns and exhaustion by whole lines {#sec:lines}

Let $C$ be a directed cycle of $\mathcal G_{A,B,C}$. Write $$\label{eq:cycle_length}
 \ell_C=\sum_{s\in C}h_s.$$ The edge phase changes are their lifted lengths modulo three. Returning to the same state therefore forces $3\mid\ell_C$. At any chosen base state $s\in C$, composing the edge maps gives $$\label{eq:cycle_return}
 F^{\ell_C}L_s(t)=L_s(\epsilon_Ct+\beta_C),\qquad
 \epsilon_C\in\{1,-1\},\quad\beta_C\in\mathbb Z.$$ Call $C$ *retained* if $\epsilon_C=-1$, or if $\epsilon_C=1$ and $\beta_C=0$. Moving the base state conjugates the return map by a bijective affine parameter map, so retention is independent of the chosen base state.

\@p0.25Yp0.27@ Parameter return & Decision and reason & Certified native return\
$t\mapsto t$ & Retain: identity on the entire line & $r_C=\ell_C/3$\
$t\mapsto-t+\beta_C$ & Retain: the square is the identity & $r_C=2\ell_C/3$\
$t\mapsto t+\beta_C$, $\beta_C\ne0$ & Do not retain: no integer parameter is periodic under translation & None\

[\[lem:cycle\_lines\]]{#lem:cycle_lines label="lem:cycle_lines"} A nonretained cycle contains no $F$-periodic point on its state lines. Every integer point on a retained cycle's state lines and all their intermediate images is $F$-periodic, with a return time $\ell_C$ or $2\ell_C$ as in Table [\[tab:returns\]](#tab:returns){reference-type="ref" reference="tab:returns"}.

For a nonretained cycle the iterates of the parameter at the base state are $t+k\beta_C$, with $\beta_C\ne0$. They are unbounded, whereas every subsequence of a periodic orbit is bounded. For a retained cycle the affine return has order at most two, so [\[eq:cycle\_return\]](#eq:cycle_return){reference-type="eqref" reference="eq:cycle_return"} fixes every parameter after the stated number of lifted steps. The same return fixes every intermediate image because powers of $F$ commute. The edge identities transport the assertion around the cycle.

For all retained cycles form the union $$\label{eq:lift_line_union}
 \widetilde{\mathcal L}=
 \bigcup_{\substack{C\text{ retained}\\s\in C}}
 \ \bigcup_{0\le r<h_s}F^rL_s(\mathbb Z).$$ Let $\mathcal L\subset\mathbb Z^3$ be the phase-zero part of this union, with the phase label omitted. The use of every intermediate image in [\[eq:lift\_line\_union\]](#eq:lift_line_union){reference-type="eqref" reference="eq:lift_line_union"} is necessary: state lines alone need not form an invariant set for one lifted step.

[\[lem:backward\]]{#lem:backward label="lem:backward"} The union $\widetilde{\mathcal L}$ satisfies $F(\widetilde{\mathcal L})=\widetilde{\mathcal L}=F^{-1}(\widetilde{\mathcal L})$. Any point whose forward orbit reaches $\widetilde{\mathcal L}$ already belongs to $\widetilde{\mathcal L}$.

Along an edge, $F$ takes each intermediate image onto the next. At its last image, [\[eq:edge\_identity\]](#eq:edge_identity){reference-type="eqref" reference="eq:edge_identity"} and $\phi_s(\mathbb Z)=\mathbb Z$ show that the image is the entire next state line, not a proper subset. As the edges run around cycles, every line image in the union has a predecessor there. Thus $F(\widetilde{\mathcal L})=\widetilde{\mathcal L}$. Bijectivity of $F$ on the ambient phase-labelled lattice gives the inverse-image equality. Repeatedly applying it proves the final assertion.

[\[prop:exhaustion\]]{#prop:exhaustion label="prop:exhaustion"} Every native periodic orbit of height $M>R$ is contained in $\mathcal L$. The set $\mathcal L$ is a union of at most 27 affine integer lines, each having a certified native return time at most 54.

By Proposition [\[prop:graph\_cycle\_entry\]](#prop:graph_cycle_entry){reference-type="ref" reference="prop:graph_cycle_entry"}, the lifted orbit reaches a directed graph cycle. Since the orbit is periodic, Lemma [\[lem:cycle\_lines\]](#lem:cycle_lines){reference-type="ref" reference="lem:cycle_lines"} excludes a nonretained cycle. It therefore reaches $\widetilde{\mathcal L}$. Lemma [\[lem:backward\]](#lem:backward){reference-type="ref" reference="lem:backward"} puts the entire preceding orbit in the same union, including any graph path before entry into the cycle. Its native phase-zero points lie in $\mathcal L$.

Distinct directed cycles of a graph with outdegree at most one have disjoint state sets. A cycle of lifted length $\ell_C$ has exactly $\ell_C/3$ phase-zero positions among its intermediate images, because the phase advances by one at each lifted step. Every such position is an affine line by Lemma [\[lem:edges\]](#lem:edges){reference-type="ref" reference="lem:edges"}. Consequently the number of phase-zero lines, before coincidences, is at most $$\sum_{C\text{ retained}}\frac{\ell_C}{3}
 \le \sum_{C\text{ retained}}|C|\le27.$$ Also $\ell_C\le3|C|\le81$. Dividing the lifted returns in Lemma [\[lem:cycle\_lines\]](#lem:cycle_lines){reference-type="ref" reference="lem:cycle_lines"} by three, using [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, gives $r_C=\ell_C/3$ or $r_C=2\ell_C/3\le54$.

The assertion concerns pointwise periodicity along each line, not setwise invariance of each separate line under $T$. The union $\mathcal L$ is $T$-invariant, and its points can pass between different lines before returning. Line coincidences only lower the bound of 27; they create no missing family.

# The finite core, least periods and disjoint output {#sec:effective}

## An exhaustive finite residual rule

Define a directed graph on $Q_R$ by assigning an arrow $P\to T(P)$ exactly when $T(P)\in Q_R$. Let $\mathcal C_R$ be its cyclic vertices. All operations use the integer polynomial map [\[eq:involutions\]](#eq:involutions){reference-type="eqref" reference="eq:involutions"}--[\[eq:native\]](#eq:native){reference-type="eqref" reference="eq:native"}; no reduction modulo a prime or approximate orbit is involved.

[\[lem:core\]]{#lem:core label="lem:core"} The directed cycles in this graph are exactly the native periodic orbits contained in $Q_R$. From any seed in $Q_R$, exact iteration either exits the box or repeats within $N_R+1$ visited vertices. If a first repetition occurs before exit, the repeated vertex is the initial seed.

A directed cycle in the partial graph is a cycle of the actual map, and a native periodic orbit contained in the box supplies the converse. There are $N_R$ vertices, so a nonexiting path repeats among its first $N_R+1$ vertices. Write it as $P_0,P_1,\ldots$, with $P_j=T(P_{j-1})$, and suppose its first repetition is $P_k=P_j$, where $0\le j<k$. If $j>0$, then $T(P_{k-1})=T(P_{j-1})$; injectivity of $T$ forces $P_{k-1}=P_{j-1}$, an earlier repetition. Hence $j=0$.

An exit only rejects the seed as a member of a cycle *entirely contained in the box*. A periodic point on a retained line can leave the box and later return. That point is already accounted for by $\mathcal L$; no claim of nonperiodicity is inferred from its box exit.

Every point on $\mathcal L$ is periodic by Lemma [\[lem:cycle\_lines\]](#lem:cycle_lines){reference-type="ref" reference="lem:cycle_lines"}, and every point of $\mathcal C_R$ is periodic by Lemma [\[lem:core\]](#lem:core){reference-type="ref" reference="lem:core"}. Conversely, a periodic orbit not contained in $\mathcal L$ cannot have height greater than $R$, by Proposition [\[prop:exhaustion\]](#prop:exhaustion){reference-type="ref" reference="prop:exhaustion"}. All its points are therefore in $Q_R$, and the orbit is one of the finite graph's directed cycles. This proves [\[eq:exhaustive\_union\]](#eq:exhaustive_union){reference-type="eqref" reference="eq:exhaustive_union"}.

## Integral lines and their intersections

Every phase-zero line supplied by [\[eq:lift\_line\_union\]](#eq:lift_line_union){reference-type="eqref" reference="eq:lift_line_union"} has an integer affine parametrization $P(t)=p+tv$ containing a coordinate of slope $1$ or $-1$. If a rational point $P(q)$, $q\in\mathbb Q$, has all integer coordinates, that coordinate implies $q\in\mathbb Z$. Thus $P(\mathbb Z)$ is precisely the set of integer points on the corresponding rational affine line, and $P$ is injective.

Coincidence of two rational affine lines is decided by linear equations over $\mathbb Q$. Coincident lines have the same full integer point set, so one parametrization may be discarded. Two distinct lines have at most one intersection. Solving $P(t)=P'(t')$ and checking $t,t'\in\mathbb Z$ therefore finds all integral intersections. The same linear membership test decides which finite-core points are on the retained lines.

## Exact least-period labels

[\[prop:periods\]]{#prop:periods label="prop:periods"} For a constructed line $P(t)$ with certified return $r\le54$, the least native period is effectively determined for every integer parameter. It is constant outside an effectively computable finite set, and all exceptional parameters are determined exactly.

Every point on the line is fixed by $T^r$, so its least period divides $r$. For each positive divisor $d\mid r$, form the three integer polynomials $$\label{eq:period_polynomials}
 \Delta_{d,k}(t)=\bigl(T^dP(t)-P(t)\bigr)_k,
 \qquad k=1,2,3.$$ The integer parameters of period dividing $d$ are exactly their common zeros. If all three polynomials vanish identically, every integer parameter qualifies. Otherwise, take the gcd over $\mathbb Q[t]$ of the nonzero polynomials. Its common integer roots form a finite set. This set can be found by exact rational polynomial arithmetic and the rational-root theorem: remove any power of $t$, record zero if applicable, clear denominators, and test the finitely many integer divisors of the remaining nonzero constant term. A nonzero constant gcd gives the empty set.

Let $E$ be the union of the finite root sets from those divisors whose polynomial vector is not identically zero. At least the divisor $r$ has identically zero vector. The smallest divisor with this property is the least period for every $t\notin E$. For $t\in E$, choose the smallest divisor for which [\[eq:period\_polynomials\]](#eq:period_polynomials){reference-type="eqref" reference="eq:period_polynomials"} vanishes at that parameter. This determines the exact least period, including every exception.

For a completely disjoint presentation, order the distinct lines and assign each integral intersection to the first line containing it. Omit its parameter from later lines; there are only finitely many such omissions. Apply Proposition [\[prop:periods\]](#prop:periods){reference-type="ref" reference="prop:periods"} to the retained parameters and delete all line points from $\mathcal C_R$. The latter deletion removes entire cycles because $\mathcal L$ is invariant. The remaining finite-graph cycles have least period equal to their number of distinct vertices. In particular, their periods are at most $N_R$, proving the least-period bound in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Intersections cannot receive contradictory periods: each label is the first return of the same actual point.

[\[proc:atlas\]]{#proc:atlas label="proc:atlas"} Given $(A,B,C)\in\mathbb Z^3$, the following finite procedure describes the entire periodic locus and its least periods.

1.  Construct the 27 states and every edge in Table [\[tab:edges\]](#tab:edges){reference-type="ref" reference="tab:edges"}. Find the directed cycles; compose their parameter maps and apply Table [\[tab:returns\]](#tab:returns){reference-type="ref" reference="tab:returns"}.

2.  For each retained cycle, list its phase-zero intermediate line images. Attach the certified return $r_C$, and discard coincident lines using exact linear algebra.

3.  Apply [\[eq:period\_polynomials\]](#eq:period_polynomials){reference-type="eqref" reference="eq:period_polynomials"} for every divisor of each attached return. Record the generic least-period label and the finite exceptional parameter list. Resolve line intersections by the preceding disjointness convention.

4.  Set $R=100(1+\max(|A|,|B|,|C|))$. For each seed of $Q_R$, follow $T$ until exit or first return. Record a returning cycle only once, for example from its lexicographically smallest vertex. Remove every cycle contained in $\mathcal L$.

5.  Output the line parametrizations with their exact labels and finite exclusions, and the remaining finite cycles with their exact lengths. For a specified level, apply the quadratic filtering in Section [7](#sec:levels){reference-type="ref" reference="sec:levels"} before the final point count.

Steps 1--3 involve a fixed finite graph and finitely many polynomial calculations; Step 4 terminates by Lemma [\[lem:core\]](#lem:core){reference-type="ref" reference="lem:core"}. The procedure therefore decides more than whether a proposed point is periodic: it outputs the complete locus for the given coefficients, including simultaneously occurring periods. Its box can be large, and we make no practical running-time guarantee. No execution of this procedure is needed to establish its termination or exhaustive character.

# All invariant levels and ordinary cycle counts {#sec:levels}

Define a phase-dependent polynomial $$\label{eq:phase_invariant}
 K_i(x,y,z)=x^2+y^2+z^2-xyz-a_ix-a_{i+1}y-a_{i+2}z.$$ If $F_i(x,y,z)=(y,z,yz+a_i-x)$, direct expansion gives $$\label{eq:invariant_transport}
 K_{i+1}\circ F_i=K_i.$$ One way to check it is to put $w=yz+a_i-x$. The part of $K_{i+1}(y,z,w)$ involving $w$ is $$w^2-yzw-a_iw=w(w-yz-a_i)=-xw
                =x^2-xyz-a_ix.$$ Adding the remaining terms gives [\[eq:phase\_invariant\]](#eq:phase_invariant){reference-type="eqref" reference="eq:phase_invariant"}. Since $K_0=K$, three applications also verify $K\circ T=K$.

On a state line the restriction is $$\label{eq:quadratic_level}
 K_i(u,t,v)
 =t^2-(uv+a_{i+1})t+u^2+v^2-a_iu-a_{i+2}v.$$ It is monic quadratic in the integer parameter. By [\[eq:invariant\_transport\]](#eq:invariant_transport){reference-type="eqref" reference="eq:invariant_transport"}, every intermediate line image has the same invariant polynomial when parametrized by its originating state parameter. An affine reparametrization of slope $1$ or $-1$ also leaves the leading coefficient equal to one.

[\[cor:level\]]{#cor:level label="cor:level"} For every $(A,B,C,D)\in\mathbb Z^4$, $$\#\bigl(\operatorname{Per}_\mathbb Z(T)\cap\{K=D\}\bigr)\le54+N_R.$$ The points in this set and their least native periods are effective.

For each retained line, set its monic quadratic restriction equal to $D$. There are at most two integer solutions, each giving a single point because the parametrization is injective. Thus at most 27 lines contribute at most 54 points before deduplication. There are at most $N_R$ finite-core vertices. Solving the quadratic equations and filtering the finite core by $K(P)=D$, with the disjointness and least-period rules of Section [6](#sec:effective){reference-type="ref" reference="sec:effective"}, proves both claims.

This finishes the proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The level bound includes every affine singular point; the proof never uses smoothness, positivity, nonzero coordinates or a genericity restriction on the coefficients.

For completeness, let $c_d(A,B,C,D)$ be the number of primitive native cycles of length $d$ on the integral level $K=D$. Here a primitive cycle means one orbit of least period $d$, counted once rather than once per vertex. All these integers are effective, nonnegative, and zero for all but finitely many $d$. The ordinary fixed-point counts are $$\label{eq:fixed_counts}
 \#\{P\in\mathbb Z^3:K(P)=D,\ T^nP=P\}
    =\sum_{d\mid n}d\,c_d(A,B,C,D).$$ Consequently the ordinary dynamical zeta function on this integral level is the finite product $$\label{eq:zeta}
 \begin{aligned}
 \zeta_{A,B,C,D}(z)
 &=\exp\left(\sum_{n\ge1}
   \#\operatorname{Fix}\bigl(T^n|_{\{K=D\}\cap\mathbb Z^3}\bigr)\frac{z^n}{n}\right)\\
 &=\prod_{d\ge1}(1-z^d)^{-c_d(A,B,C,D)}.
 \end{aligned}$$ Indeed, a primitive $d$-cycle contributes $d$ fixed points exactly for iterates divisible by $d$, and its contribution to the exponent is $\sum_{m\ge1}z^{dm}/m=-\log(1-z^d)$.

Equation [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is a fibrewise ordinary counting identity. If a retained line is present, some iterate fixes infinitely many integer points on the whole lattice. In that case the usual finite-fixed-count definition does not give an ordinary all-lattice zeta function. No weighting, intersection multiplicity or change of time is used to replace those infinite counts.

# Limitations and evidence statement {#sec:scope}

The classification is exact for the specified ordered word and integer domain. It gives a finite construction for every coefficient triple, not a sharp universal table of periods or a complexity-efficient implementation. The constants 27, 54 and $100(H+1)$ are certified bounds from the argument; no optimality is asserted. The equal-forcing case, general Fricke geometry, group-orbit reduction and routine finite-graph or zeta identities are not independent contributions of this article.

The new ingredient is the all-level implication in Proposition [\[prop:exhaustion\]](#prop:exhaustion){reference-type="ref" reference="prop:exhaustion"}. It is proved by inequalities, exact polynomial identities and bijectivity. No mathematical program, finite-core enumeration or numerical experiment was executed for this proof-only result. The pseudocode-style Procedure [\[proc:atlas\]](#proc:atlas){reference-type="ref" reference="proc:atlas"} states a terminating algorithm; it is not an execution receipt. The previous equal-forcing manuscript's computer-assisted certificate is credited but is neither imported as a proof dependency nor rerun. There is no experimental dataset underlying the theorem.

The article was prepared with AI assistance. The underlying argument received internal review within the current research team; this does not represent external human peer review. Source comparisons are bounded by the cited versions and inspected statements. The accompanying source audit records access limits and bibliographic provenance; unperformed retraction, venue-policy and conflict-of-interest checks are not represented as completed checks.

Finally, the ordinary counts in [\[eq:fixed\_counts\]](#eq:fixed_counts){reference-type="eqref" reference="eq:fixed_counts"} and [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} concern this source dynamical system only. They do not identify target Euler factors, root numbers, an automorphic object, or a Hilbert--Pólya realization. No such arithmetic interpretation is inferred from the existence of a finite cycle product.
