---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--167-minimum-inverse-position-feedback"
canonical_tex: "symbolic_dynamics/papers/167-minimum-inverse-position-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/167-minimum-inverse-position-feedback/main.pdf"
source_sha256: "500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Minimum Inverse-Position Feedback on Finite Endofunctions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/167-minimum-inverse-position-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/167-minimum-inverse-position-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/167-minimum-inverse-position-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/167-minimum-inverse-position-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/167-minimum-inverse-position-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $[n]=\{0,\ldots,n-1\}$ and replace an endofunction $f$ by the vector whose $i$th coordinate is the least position carrying $i$, using $i$ itself when $i$ is absent. We determine the resulting feedback dynamics. Every first image is a disjoint union of directed cycles and loop-rooted paths; cycles invert, while a path reverses or loses an endpoint according to an order comparison. This gives sharp tail heights $2n-2$ on the full carrier and $2n-3$ after one update. Recurrent components admit an exact labelled census, yielding a closed exponential generating function, all fixed-iterate counts, and the finite dynamical zeta function. Fixed states are involutions. Separately, a forced-first-position construction gives the one-step fibre over every target, including unsupported targets, and proves that the maximum fibre is the Bell number $B_n$. The cases $n=1,2,3$ are included explicitly. All classical transversal, first-occurrence, set-partition, functional-graph, and zeta ingredients are treated as background; external circulation remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Minimum Inverse-Position Feedback on Finite Endofunctions'
```

## Markdown 正文

# The literal feedback map and theorem ceiling

For $n\geq1$, put $\mathcal X_n=[n]^{[n]}$ and regard $f\in\mathcal X_n$ both as an endofunction and as the word $f(0)\cdots f(n-1)$. Define the self-map $\mathcal M_n:\mathcal X_n\to\mathcal X_n$ by $$\label{eq:literal}
 (\mathcal M_n f)(i)=
 \begin{cases}
   \min\{j\in[n]:f(j)=i\},&f^{-1}(i)\ne\varnothing,\\
   i,&f^{-1}(i)=\varnothing.
 \end{cases}$$ The second line is part of the map, not an arbitrary completion of a partial section. Powers $\mathcal M_n^k$ below mean repeated feedback under [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}, not composition powers of the original $f$.

The first line chooses the least member of each kernel class. Least kernel transversals and inverse matchings in transformation semigroups are established background [@FernandesEtAl2009; @Higgins2019]. Indeed, $f\circ\mathcal M_n(f)\circ f=f$, and $e_f=\mathcal M_n(f)\circ f$ is the idempotent retraction sending each position to the least member of its $\ker f$ block. This does not make $\mathcal M_n$ a mutual inverse selection: for $f=(0,0)$, $\mathcal M_2(f)=\operatorname{id}$ but $\mathcal M_2(f)\circ f\circ\mathcal M_2(f)=f\ne\mathcal M_2(f)$. The identity-on-missing rule is what controls subsequent path splitting.

First-occurrence encodings and their set-partition interpretation are also classical [@BeanEtAl2026], as are functional-digraph decomposition [@FlajoletOdlyzko1989] and periodic-point zeta functions [@ArtinMazur1965]. These ingredients, involution and Bell numbers, and labelled-set calculus receive no contribution credit. The result proved here is only the exact conjunction forced by the literal rule [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}. No novelty or priority conclusion is drawn from the bounded owner search.

For $x\in\mathcal X_n$, let $\operatorname{tail}(x)$ be its least entrance time into the recurrent set and let $\operatorname{per}(x)$ be its eventual period. Write $\mathcal Y_n=\mathcal M_n(\mathcal X_n)$, let $R_n$ be the number of recurrent points, and let $I_n$ be the number of involutions of $[n]$. Thus $$\label{eq:involution-egf}
 \sum_{n\geq0}I_n\frac{x^n}{n!}=\exp(x+x^2/2).$$

We also prepare the target-local inverse notation. Given $g\in\mathcal X_n$, put $$U_g=\{i:g(i)\ne i\}.$$ If the values $\{g(i):i\in U_g\}$ repeat, define $\Phi_n(g)=0$. Otherwise set $$F_g=\{i:g(i)=i,\ i\notin g(U_g)\}.$$ For $A\subseteq F_g$, let $P_A=U_g\cup A$ and $$r_A(i)=\begin{cases}g(i),&i\in U_g,\\i,&i\in A,\end{cases}
 \qquad R_A=\{r_A(i):i\in P_A\},$$ and define $$\label{eq:phi}
 \Phi_n(g)=\sum_{A\subseteq F_g}
 \prod_{\substack{0\leq j<n\\j\notin R_A}}
 \bigl|\{i\in P_A:r_A(i)<j\}\bigr|.$$ Empty products have value one; a zero factor rejects that choice of $A$.

[\[thm:main\]]{#thm:main label="thm:main"} For the literal map [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}, the following hold.

(i) Every component of every $g\in\mathcal Y_n$ is either a directed cycle or a loop-rooted directed path. One update inverts each cycle. If a path of size $s>1$ in root-to-leaf order is $P=(p_0,\ldots,p_{s-1})$, one update reverses $P$ when $p_0>p_1$, and otherwise splits off $p_0$ and reverses the remaining path; a singleton is fixed. For $n\geq2$, $$\label{eq:heights}
     \max_{f\in\mathcal X_n}\operatorname{tail}(f)=2n-2,
     \qquad \max_{g\in\mathcal Y_n}\operatorname{tail}(g)=2n-3.$$ Both maxima are zero at $n=1$.

(ii) A path of size $s>1$ is recurrent exactly when $p_0>p_1$ and $p_{s-1}>p_{s-2}$; a singleton is fixed. On a prescribed $s$-set, the number $c_s$ of connected recurrent states is $$\label{eq:connected}
      c_1=1,\quad c_2=1,\quad c_3=4,\qquad
      c_s=(s-1)!+\frac{s!}{4}\quad(s\geq4).$$ Consequently $$\label{eq:rec-egf}
      \sum_{n\geq0}R_n\frac{x^n}{n!}
      =\frac{1}{1-x}\exp\!\left(\frac{x^3}{3}
            +\frac{x^4}{4(1-x)}\right).$$

(iii) The fixed states are precisely the involutions. For every $k\geq1$, $$\label{eq:iterate-fix}
       |\operatorname{Fix}(\mathcal M_n^k)|=
       \begin{cases}I_n,&k\text{ odd},\\R_n,&k\text{ even}.
       \end{cases}$$ The finite-map dynamical zeta function, as a formal power series, is $$\label{eq:zeta}
       \zeta_{\mathcal M_n}(z)=(1-z)^{-I_n}
       (1-z^2)^{-(R_n-I_n)/2}.$$

(iv) For every target $g\in\mathcal X_n$, including targets outside $\mathcal Y_n$, $$\label{eq:fibre}
      |\mathcal M_n^{-1}(g)|=\Phi_n(g).$$ If $B_n$ is the $n$th Bell number, then $$\label{eq:bell}
      \max_{g\in\mathcal X_n}|\mathcal M_n^{-1}(g)|=B_n,$$ and the identity target attains the maximum.

(v) The first three nonempty carriers have the following boundary data; "two-orbits" counts dynamical orbits rather than points.

       $n$    $|\mathcal X_n|$   $|\mathcal Y_n|$   $R_n$   $I_n$   two-orbits   full $H$   image $H$   max fibre
      ----- ------------------ ------------------ ------- ------- ------------ ---------- ----------- -----------
        1                    1                  1       1       1            0          0           0           1
        2                    4                  3       2       2            0          2           1           2
        3                   27                 14       8       4            2          4           3           5

# Component action and the two sharp clocks

[\[lem:components\]]{#lem:components label="lem:components"} If $g=\mathcal M_n(f)$, then the off-diagonal values $\{g(i):g(i)\ne i\}$ are distinct. Its functional digraph therefore has only directed-cycle and loop-rooted-path components. On these components $\mathcal M_n$ acts exactly as in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(i), components never merge, and the recurrent-path criterion in part (ii) holds.

Whenever $g(i)\ne i$, its value is the first position of symbol $i$ in $f$. Distinct symbols have distinct first positions. Hence every vertex has at most one incoming nonloop edge. A nonloop cycle can support no attached vertex, while a loop can support at most one chain, proving the component classification.

Write a path as $P=(p_0,\ldots,p_{s-1})$, so $g(p_0)=p_0$ and $g(p_j)=p_{j-1}$ for $j\geq1$. In the word $g$, symbol $p_0$ occurs at positions $p_0,p_1$, symbol $p_j$ for $1\leq j\leq s-2$ occurs at $p_{j+1}$, and $p_{s-1}$ is absent. If $p_0>p_1$, the least occurrence of $p_0$ is $p_1$ and the entire path reverses. If $p_0<p_1$, the root remains a singleton and the other labels form the reversed path. A cycle has exactly one occurrence of every symbol, so its orientation is inverted. All relevant positions and symbols lie in the original component, including the identity default at an absent leaf; no merge is possible.

For $s>1$, the path returns after reversal precisely when its new root also has the descending comparison, namely $p_{s-1}>p_{s-2}$. If the first comparison fails, a split occurs immediately. If only the last comparison fails, one reversal is followed by a split. Since splits cannot be undone, these paths are not recurrent. This proves the criterion.

[\[lem:path-clock\]]{#lem:path-clock label="lem:path-clock"} For a path $P$ of size $s$, its tail $D(P)$ satisfies $$\label{eq:path-bound}
 D(P)\leq2s-2.$$ For $s\geq2$, equality holds exactly for the strictly decreasing order $p_0>p_1>\cdots>p_{s-1}$.

Induct on $s$. A recurrent path has tail zero. If $p_0<p_1$, one update splits off $p_0$ and leaves a path of size $s-1$, so induction gives $D(P)\leq1+2(s-1)-2=2s-3$. It remains to take $p_0>p_1$ with $P$ nonrecurrent. Lemma [\[lem:components\]](#lem:components){reference-type="ref" reference="lem:components"} then gives $p_{s-1}<p_{s-2}$: one update reverses the path, the next splits off $p_{s-1}$, and the surviving path is the original prefix $P^-=(p_0,\ldots,p_{s-2})$. Therefore $$D(P)=2+D(P^-)\leq2s-2.$$ Equality is equivalent by induction to strict decrease of $P^-$; the last displayed endpoint inequality then extends the decrease through $p_{s-1}$. Conversely, the same recurrence proves equality for every strictly decreasing path.

Components update in parallel, so a state's tail is the maximum of its path tails. Lemma [\[lem:path-clock\]](#lem:path-clock){reference-type="ref" reference="lem:path-clock"} gives the global component bound. Every $g=\mathcal M_n(f)$ contains the coordinate value zero, because the symbol $f(0)$ has first occurrence zero. The unique full-label path attaining $2n-2$ has order $(n-1,\ldots,0)$, and its coordinate values are $\{1,\ldots,n-1\}$; it cannot belong to $\mathcal Y_n$. Any other full-label path has integer tail at most $2n-3$, while a path on at most $n-1$ labels has tail at most $2n-4$. Thus the second maximum in [\[eq:heights\]](#eq:heights){reference-type="eqref" reference="eq:heights"} is at most $2n-3$.

For $n\geq2$, let $w_n(j)=j+1$ for $0\leq j\leq n-2$ and $w_n(n-1)=1$; in word notation this is $w_n=(1,2,\ldots,n-1,1)$, and it maps to the increasing path $(0,1,\ldots,n-1)$. The path recursion in the previous proof gives tail $2n-3$ for this image. Since it is transient, $w_n$ has tail $2n-2$. Conversely, every source enters $\mathcal Y_n$ after one update, so its tail is at most $1+(2n-3)$. At $n=1$ the sole state is fixed. The component assertions were proved in Lemma [\[lem:components\]](#lem:components){reference-type="ref" reference="lem:components"}.

# Recurrent species, fixed iterates, and zeta

On a prescribed $s$-set, directed cycles contribute $(s-1)!$ for $s\geq2$. There is one singleton. Recurrent paths contribute none at $s=2$ and two at $s=3$, since the middle position must contain the smallest label. For $s\geq4$, the two endpoint inequalities concern disjoint pairs of positions. Swapping either pair is a free involution on the $s!$ linear orders, so exactly $s!/4$ orders satisfy both. This proves [\[eq:connected\]](#eq:connected){reference-type="eqref" reference="eq:connected"}.

A recurrent state is an unordered labelled set of connected recurrent components. The labelled-set formula gives $$\exp\!\left(\sum_{s\geq1}c_s\frac{x^s}{s!}\right)
 =\exp\!\left(-\log(1-x)+\frac{x^3}{3}
                   +\frac{x^4}{4(1-x)}\right),$$ which is [\[eq:rec-egf\]](#eq:rec-egf){reference-type="eqref" reference="eq:rec-egf"}.

Every nonsingleton recurrent path is exchanged with its distinct reversal. Cycle inversion fixes exactly the two-cycles. Thus a fixed state is a set of singleton loops and disjoint two-cycles, equivalently an involution, and [\[eq:involution-egf\]](#eq:involution-egf){reference-type="eqref" reference="eq:involution-egf"} applies. Every recurrent point has period one or two, while any point fixed by a positive iterate is recurrent. This proves [\[eq:iterate-fix\]](#eq:iterate-fix){reference-type="eqref" reference="eq:iterate-fix"}. Substitution into the Artin--Mazur definition $$\zeta_{\mathcal M_n}(z)=\exp\!\left(
    \sum_{k\geq1}|\operatorname{Fix}(\mathcal M_n^k)|\frac{z^k}{k}\right)$$ and separation of odd and even $k$ gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The first coefficients of [\[eq:rec-egf\]](#eq:rec-egf){reference-type="eqref" reference="eq:rec-egf"} are $$R_0,\ldots,R_7=1,1,2,8,38,220,1540,12460,$$ whereas $I_1,\ldots,I_7=1,2,4,10,26,76,232$.

# The inverse atlas and its Bell ceiling

Fix a target $g$. For every $i\in U_g$, any source above $g$ must contain symbol $i$ first at position $g(i)$. These forced positions must be distinct, proving the zero case in the definition of $\Phi_n$. A fixed coordinate $i$ either represents an absent symbol or a symbol first appearing at $i$. The latter choice is impossible when position $i$ is already in $g(U_g)$, so the optional present symbols are exactly a subset $A\subseteq F_g$.

Once $A$ is chosen, the positions $r_A(i)$ are forced to carry $i$. At an unforced position $j$, the legal letters are precisely the symbols already opened before $j$, namely $\{i\in P_A:r_A(i)<j\}$. These choices are independent across unforced positions. Their product, summed over $A$, is [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"}; conversely, every word constructed this way has target $g$. This proves the every-target identity [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, including the support test $g\in\mathcal Y_n\Longleftrightarrow\Phi_n(g)>0$.

Now fix the kernel partition of a possible source. A block with minimum position $j$ has a uniquely determined label: it is the unique off-diagonal $i$ with $g(i)=j$ if such an $i$ exists, and otherwise it can only be $j$. Hence at most one source over $g$ realizes each kernel partition, giving the upper bound $B_n$. Over $g=\operatorname{id}$, every set partition does occur: label each block by its least position. Present labels then first occur at themselves and every other label is absent. Distinct partitions give distinct sources, proving [\[eq:bell\]](#eq:bell){reference-type="eqref" reference="eq:bell"}.

The case $n=1$ is immediate. At $n=2$ the word dynamics are $$00\mapsto01,\qquad01\mapsto01,\qquad
 10\mapsto10,\qquad11\mapsto00,$$ which gives the second row. At $n=3$, the connected census gives $R_3=1+3+4=8$, while the involutions give $I_3=4$ and hence two dynamical two-orbits. Direct substitution of the $27$ targets into [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} gives the nonzero-fibre histogram $$6u+5u^2+2u^3+u^5,$$ so $|\mathcal Y_3|=14$ and the maximum is five. The two height entries follow from part (i). This proves the boundary table.

# Exact controls and scope

A standalone standard-library verifier reconstructs [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"} without importing the scouting implementation. It exhausts every state and target through $n=7$, every path order and canonical cycle through size nine, the component EGF through order fourteen, positive iterates through six, all target fibres, Bell injections, sharp witnesses, and the complete graphs at $n=1,2,3$. Its frozen run records $12{,}603{,}676$ exact assertions. Two fresh processes produced byte-identical transcripts. These computations are falsification controls; the proofs above are uniform and do not rely on enumeration.

The off-diagonal injection in Lemma [\[lem:components\]](#lem:components){reference-type="ref" reference="lem:components"} is necessary but not sufficient for first-image membership; the product [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} is the exact test. The Bell bound does not assert that the identity is the unique maximizing target. The paper gives a finite exact theorem for the stated identity-default selector and makes no assertion about other completions of a kernel section.

**Lifecycle:** anonymous internal manuscript; `HOLD_EXTERNAL`.
