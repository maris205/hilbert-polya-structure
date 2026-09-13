---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--176-first-frequency-rotation"
canonical_tex: "symbolic_dynamics/papers/176-first-frequency-rotation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/176-first-frequency-rotation/main.pdf"
source_sha256: "ff1f7d45c7ac7146a06f737a7187a9cedd451591ab9cbffeccf2d35eadc5874a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# First-Frequency Rotation on Binary Pointed Necklaces

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/176-first-frequency-rotation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/176-first-frequency-rotation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/176-first-frequency-rotation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/176-first-frequency-rotation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/176-first-frequency-rotation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $R$ be left rotation of a binary word and let $m_a(w)=|\{i:w_i=a\}|$. We study the finite map $T_n(w)=R^{m_{w_0}(w)}w$ on $\{0,1\}^n$. On a cyclic word of least period $d$ and weight $k$, the pointed dynamics splits into $\gcd(k,d)$ disjoint $\mathord{\pm}k$ generator cycles. A constant component is periodic; every nonconstant component flows into its directed $10$ edges. This gives the exact possible periods, the sharp maximum preperiod $n-2$, and exactly two deepest states for $n\geq3$. Independently, we give the complete predecessor list of every target, the global $0/1/2$ fibre distribution, and a primitive-block Möbius fixed census. Hamming-weight-controlled frozen rotations and the internal P166 cyclic phase architecture receive zero contribution credit. The retained status is `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'First-Frequency Rotation on Binary Pointed Necklaces'
```

## Markdown 正文

# Literal map and subtraction boundary

For $n\geq1$, write a word as $w=w_0w_1\cdots w_{n-1}$, with indices in $\mathbb Z/n\mathbb Z$, and set $$R(w_0w_1\cdots w_{n-1})=w_1\cdots w_{n-1}w_0.$$ For $a\in\{0,1\}$, let $m_a(w)=|\{i:w_i=a\}|$. Our literal map is $$\label{eq:literal}
 T_n(w)=R^{m_{w_0}(w)}w,\qquad w\in\{0,1\}^n.$$ It preserves both the cyclic necklace and the weight $k=\operatorname{wt}(w)=m_1(w)$. On a fixed weight layer its two branches are $$\label{eq:branches}
 w_0=1:\quad T_n(w)=R^k w,
 \qquad
 w_0=0:\quad T_n(w)=R^{n-k}w=R^{-k}w.$$

Høyer and Špalek explicitly construct the quantum phase rotation $R_z(\varphi|x|)$ under the heading "rotation by Hamming weight" [@HoyerSpalek2005 Sec. 3.2]. Their object is not a cyclic coordinate shift. Nevertheless, we assign the Hamming-weight-controlled rotation idea and both frozen branches in [\[eq:branches\]](#eq:branches){reference-type="eqref" reference="eq:branches"} zero contribution credit. The adaptive first-symbol gluing is the only literal feature under analysis.

Grošek--Hromada study coordinate-rotation classes at fixed binary weight, and Gupta et al. study literal circular shifts, rotation equivalence, weight, and complementation [@GrosekHromada2016; @GuptaEtAl2022]. Thus coordinate-necklace structure, fixed-weight class enumeration, and ordinary shift symmetries also receive zero contribution credit. Neither source defines the adaptive first-symbol gluing or its functional graph.

There is a closer internal boundary. P166 studies $S_n(x)=x+\operatorname{wt}(x)\mathbf 1$ on $(\mathbb Z/n\mathbb Z)^n$ and, on a diagonal-translation orbit, reduces it to $j\mapsto j+c_j$, where $(c_j)$ is a weak composition of $n$. Our reduction below also has cyclic phase syntax, but its increments are the two values $\mathord{\pm}k$. The exact separation is summarized here.

  ------------------------------------------------------------------------------------------------------------------------------------------------------
  axis              map [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}   internal P166 map
  ----------------- ---------------------------------------------------------------------------------- -------------------------------------------------
  invariant orbit   coordinate-rotation necklace                                                       diagonal alphabet-translation orbit

  phase profile     $a_j\in\{k,-k\}$                                                                   $c_j\geq0$, $\sum_jc_j=n$

  forward engine    disjoint $\mathord{\pm}k$ generator cycles                                         cycle mass exhaustion

  recurrence        possibly several nontrivial components                                             at most one nontrivial cycle per orbit

  periods           $1,2$, and proper divisors of $n$                                                  every value $1,\ldots,n$

  one-step fibres   two labelled rotations; size $0,1,2$                                               histogram-selected translates; unbounded in $n$
  ------------------------------------------------------------------------------------------------------------------------------------------------------

The common phase syntax, generic functional-graph language, the numerical clock value $n-2$, and indicator-style inverse notation all receive zero contribution credit. We retain only the constrained generator-component theorem and its consequences proved below. A direct owner of the adaptive literal map, a literal conjugacy into P166, or a proof that the component theorem is a formal consequence of P166 mass exhaustion triggers `KILL_INTERNAL_P166_PHASE_MAP`. Until that gate is resolved, the status remains $$\texttt{AMBER\_INTERNAL\_NEAR\_P166 / HOLD\_EXTERNAL}.$$

For a point $w$ of a finite self-map, its *preperiod* is the least $t\geq0$ for which $T_n^t(w)$ is periodic. Its eventual exact period is called simply its period.

# Pointed-necklace component theorem

Let $u\in\{0,1\}^n$ have least rotational period $d\mid n$. Its distinct pointed states are $R^ju$, $j\in\mathbb Z/d\mathbb Z$. We use the periodic indexing $u_{j+d}=u_j$ and put $k=\operatorname{wt}(u)$.

[\[lem:phase\]]{#lem:phase label="lem:phase"} On the rotation class of $u$, the identification $j\leftrightarrow R^ju$ conjugates $T_n$ to $$\label{eq:phase}
 \phi_u(j)=
 \begin{cases}
 j+k,&u_j=1,\\
 j-k,&u_j=0,
 \end{cases}
 \qquad j\in\mathbb Z/d\mathbb Z.$$

The weight is constant on the rotation class. At $R^ju$, the first bit is $u_j$. Equations [\[eq:branches\]](#eq:branches){reference-type="eqref" reference="eq:branches"} therefore give increments $k$ and $n-k$. Since $d\mid n$, the latter is $-k$ modulo $d$.

Put $$h=\gcd(k,d),\qquad L=d/h.$$ The undirected Cayley graph on $\mathbb Z/d\mathbb Z$ with generator $k$ consists of $h$ cycles of length $L$. For a component with representative $r$, order its vertices as $r,r+k,\ldots,r+(L-1)k$ and set $b_q=u_{r+qk}$, with $q\in\mathbb Z/L\mathbb Z$. Thus a bit $1$ points forward and a bit $0$ points backward in this generator order.

[\[thm:component\]]{#thm:component label="thm:component"} Each generator component is classified as follows.

(i) If $L=1$, its vertex is fixed.

(ii) If $L=2$, its two vertices form one directed two-cycle.

(iii) If $L\geq3$ and $(b_q)$ is constant, the component is one directed $L$-cycle.

(iv) If $L\geq3$ and $(b_q)$ is nonconstant, its recurrent components are exactly the cyclic occurrences $b_qb_{q+1}=10$, one two-cycle per occurrence. Every other vertex is transient. More precisely, its preperiod is $$\label{eq:pointdepth}
      \tau(q)=
      \begin{cases}
      \min\{t\geq0:(b_{q+t},b_{q+t+1})=(1,0)\},&b_q=1,\\
      \min\{t\geq0:(b_{q-t-1},b_{q-t})=(1,0)\},&b_q=0.
      \end{cases}$$ Consequently the maximum preperiod in the component is one less than the longest cyclic constant run in $(b_q)$.

The first two cases follow because $+1$ and $-1$ in generator coordinates are equal when $L\leq2$. For $L\geq3$, a constant word points coherently around the cycle and gives an $L$-cycle.

Now suppose the component word is nonconstant. Whenever $b_qb_{q+1}=10$, the vertex $q$ points to $q+1$ and $q+1$ points back to $q$, so this edge is a directed two-cycle. Starting from a $1$, successive arrows move forward through its $1$-run until the terminal $1$ of such an edge is reached. Starting from a $0$, they move backward through its $0$-run until the initial $0$ of such an edge is reached. This proves [\[eq:pointdepth\]](#eq:pointdepth){reference-type="eqref" reference="eq:pointdepth"} and shows that every vertex reaches one of the listed edges.

No further directed cycle exists: a cycle that ever reverses direction uses an edge in both directions and is one of the listed two-cycles, while a cycle that never reverses would orient the whole component coherently, contrary to nonconstancy. On a constant run of length $s$, the farthest vertex is $s-1$ arrows from its boundary two-cycle. Taking the longest run proves the final statement.

The theorem is pointwise, not merely a period count: factor the pointed necklace into its $h$ generator cycles, read their constant runs, and obtain every tail and recurrent component without iterating [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}. Several recurrent components can occur in one necklace. For example, the six rotations of $111000$ split into three directed two-cycles.

# Period inventory and sharp clock

[\[thm:periods\]]{#thm:periods label="thm:periods"} For $n=1$, the possible-period set is $\{1\}$. For every $n\geq2$, it is $$\label{eq:periods}
 \{1,2\}\ \cup\ \{\ell:\ell\mid n,\ 3\leq\ell<n\}.$$

Theorem [\[thm:component\]](#thm:component){reference-type="ref" reference="thm:component"} shows that a period longer than two must be the length $L=d/\gcd(k,d)$ of a constant generator component. Hence $L\mid n$. If $L=n$, then $d=n$ and $\gcd(k,n)=1$, so there is only one generator component. Its constancy would make the whole word constant, contradicting least period $d=n>1$. Thus every long period is a proper divisor of $n$.

Constant words realize period one. For $n\geq2$, the rotation class with a single $1$ contains a directed two-cycle, realizing period two. It remains to realize a proper divisor $L\geq3$. Write $n=gL$, where $g\geq2$, and take the $n$-word of weight $g$ whose $1$-support is $$\label{eq:witnesssupport}
 \{0,1,\ldots,g-2,g\}\subset\mathbb Z/n\mathbb Z.$$ The cyclic zero gap after position $g$ is uniquely longest, so a rotation fixing the word must fix that gap and hence is trivial; the word has least period $n$. Under generator $k=g$, the component congruent to $g-1$ modulo $g$ is all zero. It is therefore a directed cycle of length $n/g=L$ by Theorem [\[thm:component\]](#thm:component){reference-type="ref" reference="thm:component"}. This realizes every period in [\[eq:periods\]](#eq:periods){reference-type="eqref" reference="eq:periods"}.

Let $H_n$ be the maximum preperiod of $T_n$ over $\{0,1\}^n$.

[\[thm:clock\]]{#thm:clock label="thm:clock"} One has $$\label{eq:clock}
 H_1=0,\qquad H_n=n-2\quad(n\geq2).$$ For every $n\geq3$, exactly two states have preperiod $n-2$, namely $$\label{eq:deepest}
 010^{n-2}\quad\text{and its bitwise complement}.$$ At the boundaries, both states are deepest for $n=1$ and all four states are deepest for $n=2$.

In a nonconstant generator component of length $L$, a constant run has length at most $L-1$. Theorem [\[thm:component\]](#thm:component){reference-type="ref" reference="thm:component"} bounds its preperiod by $L-2\leq n-2$; constant components contain no transient vertex. This gives the upper bound for $n\geq2$. For $n\geq3$, the first word in [\[eq:deepest\]](#eq:deepest){reference-type="eqref" reference="eq:deepest"} has weight one and, in generator order, a cyclic zero run of length $n-1$. Its displayed pointer is $n-2$ steps from the recurrent $10$ edge. Complementation commutes with [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}, so the second word is another witness.

Equality in the upper bound forces $L=n$ and a constant run of length $n-1$. Hence the word has exactly one minority bit. There are precisely two such rotation necklaces, one for each minority symbol, and in each there is exactly one pointer farthest from the recurrent $10$ edge. These are the two words in [\[eq:deepest\]](#eq:deepest){reference-type="eqref" reference="eq:deepest"}. Directly, both length-one words are fixed, while at length two the constants are fixed and the two nonconstant words form a two-cycle. The boundary claims follow.

The numerical value $n-2$ in [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} is not credited: P166 already has that sharp value. The retained statement is the generator-run proof together with the exact two-state last shell.

# Every-target fibres and fixed census

For a target $y\in\{0,1\}^n$, subscripts such as $y_{-k}$ are interpreted modulo $n$. Let $N_r(n,k)$ be the number of weight-$k$ targets having exactly $r$ one-step predecessors.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} If $y$ is constant, then $T_n^{-1}(y)=\{y\}$. If $0<k=\operatorname{wt}(y)<n$, then its complete predecessor list is $$\begin{aligned}
 x_1&=R^{-k}y &&\text{if and only if }y_{-k}=1,\label{eq:inverseone}\\
 x_0&=R^{k}y  &&\text{if and only if }y_k=0.\label{eq:inversezero}\end{aligned}$$ Here the subscripts label the first bit of the source, so present sources are distinct. In particular every fibre has size $0$, $1$, or $2$.

For $0<k<n$, if $n\mid2k$, then $$\label{eq:halfweight}
 N_1(n,k)=\binom nk,\qquad N_0(n,k)=N_2(n,k)=0.$$ Otherwise, $$\label{eq:fibrehist}
 N_0(n,k)=N_2(n,k)=\binom{n-2}{k-1},\qquad
 N_1(n,k)=\binom nk-2\binom{n-2}{k-1}.$$ The two constant targets contribute two more to the global one-fibre count, and $$\label{eq:image}
 |\operatorname{Im}T_n|=2+\sum_{k=1}^{n-1}
 \left[\binom nk-
 \mathbf1_{\{n\nmid2k\}}\binom{n-2}{k-1}\right].$$

A source beginning in $1$ must use the first branch of [\[eq:branches\]](#eq:branches){reference-type="eqref" reference="eq:branches"}; undoing it gives the sole candidate $R^{-k}y$, whose first bit is $y_{-k}$. Similarly, a source beginning in $0$ uses rotation $n-k$, whose inverse is $R^k$; its first bit is $y_k$. This proves [\[eq:inverseone\]](#eq:inverseone){reference-type="eqref" reference="eq:inverseone"}--[\[eq:inversezero\]](#eq:inversezero){reference-type="eqref" reference="eq:inversezero"}. The two candidates, when present, start with different bits.

The inspected positions $-k$ and $k$ coincide precisely when $n\mid2k$. Then exactly one of the complementary branch conditions holds, proving [\[eq:halfweight\]](#eq:halfweight){reference-type="eqref" reference="eq:halfweight"}. Otherwise they are distinct. Fibre zero prescribes the ordered pair $(y_{-k},y_k)=(0,1)$, and fibre two prescribes $(1,0)$. In either case the remaining $n-2$ positions contain $k-1$ ones, giving $\binom{n-2}{k-1}$. Subtraction gives the one-fibre count. Finally, subtracting the zero-fibre targets from each weight layer and adding the two constants proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

Fixed-density necklace and primitive-word enumeration are classical [@GrosekHromada2016; @HeckenbergerSawada2018; @Mestrovic2018]. We use that background only to record a supporting fixed census.

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} Let $\mu$ be the Möbius function and define $$\label{eq:primitive}
 A(d,j)=\sum_{e\mid\gcd(d,j)}\mu(e)
          \binom{d/e}{j/e}.$$ Then the number of fixed points of $T_n$ is $$\label{eq:fixed}
 |\operatorname{Fix}(T_n)|=
 \sum_{d\mid n}\ \sum_{j=0}^{d}
 \mathbf1_{\{d\mid(n/d)j\}}A(d,j).$$

By Möbius inversion, $A(d,j)$ counts length-$d$ binary linear words of least period $d$ and weight $j$. Repeating such a primitive block $n/d$ times gives a length-$n$ word of least period $d$ and total weight $k=(n/d)j$, and every length-$n$ word arises uniquely in this way.

If the pointed first bit is $1$, the word is fixed exactly when $d\mid k$. If it is $0$, it is fixed exactly when $d\mid n-k$, which is equivalent because $d\mid n$. Thus the fixed condition is independent of the pointer and is exactly the indicator in [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. Summing the primitive blocks proves the formula.

Primitive-word enumeration and Möbius inversion in [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"}--[\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} receive zero contribution credit.

# Exact control and lifecycle

A paper-local, standard-library author/scout-derived regression control starts from the literal update [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"} and enumerates all $2^n$ words for every $1\leq n\leq18$. It checks carrier closure and weight preservation; every target in [\[eq:inverseone\]](#eq:inverseone){reference-type="eqref" reference="eq:inverseone"}--[\[eq:inversezero\]](#eq:inversezero){reference-type="eqref" reference="eq:inversezero"}; the full fibre histogram; every pointed-necklace conjugacy; every component tail and recurrent cycle; the possible-period set; the sharp clock and deepest census; and [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. The frozen transcript reports $2{,}828{,}503$ assertions and has SHA-256

3d0947a4df32f8e583e28d1964a52523602d61c64dde7b259bfdd15e71e4003b.

Finite enumeration is a falsification and regression control, not a substitute for any all-parameter proof.

The retained results are precisely the $\mathord{\pm}k$ pointed-necklace component theorem, the period inventory, the sharp clock with deepest two, the every-target $0/1/2$ fibres, and the Möbius fixed census. No external action is authorized. The terminal status is $$\boxed{\texttt{AMBER\_INTERNAL\_NEAR\_P166 / HOLD\_EXTERNAL}}.$$
