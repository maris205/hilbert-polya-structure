---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--120-odd-fringe-mirror-plane-trees"
canonical_tex: "symbolic_dynamics/papers/120-odd-fringe-mirror-plane-trees/main.tex"
canonical_pdf: "symbolic_dynamics/papers/120-odd-fringe-mirror-plane-trees/main.pdf"
source_sha256: "c6d4c8e038653b1b750b606202ef07bb955ec43ac771a8ab6a7bcfd94ff3f1c8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Odd-Fringe Mirror Dynamics on Plane Rooted Trees: Algebraic Fixed Points and the Exact Cycle Census

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/120-odd-fringe-mirror-plane-trees>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/120-odd-fringe-mirror-plane-trees/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/120-odd-fringe-mirror-plane-trees/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/120-odd-fringe-mirror-plane-trees/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/120-odd-fringe-mirror-plane-trees/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At every vertex of a plane rooted tree, read the order of its fringe subtree and reverse the child list exactly when that order is odd; apply all such reversals simultaneously. The resulting finite self-map preserves every fringe order and is an involution. We give a root-local fixed-point criterion: an even-order root requires its children to be fixed pointwise, whereas an odd-order root requires a twisted palindrome whose paired children are $(T,\mathsf M(T))$. If $E(x)$ and $O(x)$ enumerate nonempty fixed trees of even and odd order and $A=x/(1-A)$ is the ordinary plane-tree series, this criterion gives $$E=\frac{xO}{(1-E)^2-O^2},\qquad
   O=\frac{x(1+E)}{1-A(x^2)}.$$ For $F=E+O$ we eliminate the auxiliary series and display an explicit degree-six equation $P(x,F)=0$; the condition $P_y(0,0)=-3$ singles out the zero-constant branch. Thus, if $f_n=[x^n]F$ and $a_n=C_{n-1}$ for $n\geq1$, the order-$n$ system has exactly $f_n$ fixed points and $(a_n-f_n)/2$ two-cycles, with zeta function $(1-z)^{-f_n}(1-z^2)^{-(a_n-f_n)/2}$. The empty lane is handled separately. Mirror symmetry, Catalan enumeration, plane-tree involutions, algebraic generating-function machinery, and zeta bookkeeping receive zero contribution credit. The residual scope is only this conjunction for the specified odd-fringe update; priority and external circulation remain on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Odd-Fringe Mirror Dynamics on Plane Rooted Trees: Algebraic Fixed Points and the Exact Cycle Census'
```

## Markdown 正文

# Introduction

A plane rooted tree equips the children of every vertex with a linear order. Reversing all child lists gives the classical global mirror involution. We study a state-dependent version: reverse the child list at a vertex precisely when the fringe subtree rooted there has odd order. All vertices read their trigger from the unchanged input before the reversals are applied.

The period law is immediate only after one identifies the correct invariant: changing child order does not change any fringe order. The fixed set is more delicate. At odd roots, componentwise recursion interacts with reversal, so the children need not be individually fixed. Instead, the child list is a palindrome twisted by the same map. Keeping the parity of a possible central child produces a coupled, rather than scalar, generating-function system.

The paper proves four parts of one exact finite-map package.

1.  The update preserves the underlying rooted tree and every fringe order, and it squares to the identity.

2.  Fixed trees have an exact parity-sensitive root decomposition by ordinary fixed sequences and twisted palindromes.

3.  The decomposition gives coupled series $E,O$ and an explicit degree-six algebraic equation for $F=E+O$.

4.  Since all cycles have length one or two, the fixed coefficients give every iterate-fixed count and the complete fixed-order zeta function.

The constituent neighborhoods are mature. Plane trees and the equation $A=x/(1-A)$ are standard instances of symbolic enumeration [@FlajoletSedgewick2009]. Direct involution neighbors include the parity-reversing construction of Chen--Shapiro--Yang [@ChenShapiroYang2006], Deutsch's ordered-tree bijection [@Deutsch2000], and recent binary/plane-tree involutions [@LiLinZhao2024]. Claesson--Kitaev--Steingrímsson--Wang give a 2026 abstract Catalan-involution framework, global reversal factorization, and a Donaghey connection [@ClaessonEtAl2026]; current cyclic actions on corner-rooted plane trees appear in [@BousquetMelouKrattenthaler2025]. These papers do not use the literal odd-fringe update below, but every general involution, mirror, Catalan, and generating-function ingredient receives zero contribution credit. A bounded search miss is not a priority certificate. We claim neither asymptotics nor minimality of the displayed polynomial, and external dissemination remains **HOLD**.

# The update, involution, and fixed criterion {#sec:update}

For $n\geq1$, let $\mathcal P_n$ be the set of unlabelled plane rooted trees with $n$ vertices. A tree is represented recursively by the ordered tuple $$T=[T_1,\ldots,T_k]$$ of the fringe subtrees rooted at the children of its root; the leaf is $\bullet=[]$. Its order is $|T|=1+\sum_i|T_i|$. We also adjoin a separate empty state by setting $\mathcal P_0=\{\boldsymbol\varepsilon\}$. It is not identified with the leaf.

[\[def:update\]]{#def:update label="def:update"} Set $\mathsf M(\boldsymbol\varepsilon)=\boldsymbol\varepsilon$. For a nonempty tree $T=[T_1,\ldots,T_k]$, define $$\label{eq:update}
\mathsf M(T)=
\begin{cases}
[\mathsf M(T_1),\ldots,\mathsf M(T_k)],& |T|\text{ even},\\
[\mathsf M(T_k),\ldots,\mathsf M(T_1)],& |T|\text{ odd}.
\end{cases}$$ Equivalently, every vertex reads the order of its old fringe subtree, and all child lists with odd trigger are reversed simultaneously. Write $\mathsf M_n$ for the restriction to $\mathcal P_n$.

The recursion in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} records nested reversals but does not make the clock asynchronous: every fringe order on the right is an input-tree quantity.

For a nonempty input tree, define its induced vertex transport to the image recursively. The root maps to the root. At a vertex with $k$ children, child position $i$ maps to position $i$ when that vertex's old fringe order is even and to position $k+1-i$ when it is odd; inside the matched child subtrees use their recursively induced transports.

[\[thm:involution\]]{#thm:involution label="thm:involution"} The empty state is fixed. For every $n\ge1$ and $T\in\mathcal P_n$:

1.  $\mathsf M(T)$ has the same order, the same underlying nonplane rooted tree, and the same fringe order at each vertex under the induced transport;

2.  $\mathsf M^2(T)=T$;

3.  if $T=[T_1,\ldots,T_k]$ is nonempty, then $$\begin{aligned}
    |T|\text{ even}:\quad
     T\in\operatorname{Fix}(\mathsf M)&\Longleftrightarrow
     T_i\in\operatorname{Fix}(\mathsf M)\quad(1\leq i\leq k),                 \label{eq:even-fixed}\\
    |T|\text{ odd}:\quad
     T\in\operatorname{Fix}(\mathsf M)&\Longleftrightarrow
     T_i=\mathsf M(T_{k+1-i})\quad(1\leq i\leq k).              \label{eq:odd-fixed}\end{aligned}$$

Together with the empty lane, every orbit has period one or two.

Induction on $|T|$ shows that applying [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} to a child preserves its order and descendants. The root step only reverses a list, so it also preserves order and the underlying nonplane tree. Following the induced transport just defined, the fringe subtree at each source vertex is sent to the image of that same subtree and hence has the same order. This proves the pointwise fringe-order assertion.

For the second assertion, use induction again. The root has the same parity after one update. At an even root, the second update applies $\mathsf M^2$ to each child without reversing the list. At an odd root, it applies $\mathsf M^2$ to the children and reverses the list a second time. Both cases return $T$. Equivalently, the input determines a fixed set of local reversals; those order-two operations act on distinct child lists and commute. Finally, comparing the child tuple in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} with the original tuple gives [\[eq:even-fixed\]](#eq:even-fixed){reference-type="eqref" reference="eq:even-fixed"} and [\[eq:odd-fixed\]](#eq:odd-fixed){reference-type="eqref" reference="eq:odd-fixed"} in both directions.

[\[rem:mirror\]]{#rem:mirror label="rem:mirror"} Let $\mathsf J[T_1,\ldots,T_k]=[\mathsf J(T_k),\ldots,\mathsf J(T_1)]$ reverse every child list. Put $L=[]$, $U=[L]$, $A=[L,U]$, and $B=[U,L]$. The order-four tree $A$ is $\mathsf M$-fixed but not $\mathsf J$-fixed. Conversely, the order-nine tree $[A,B]$ is $\mathsf J$-fixed but not $\mathsf M$-fixed. Hence the two fixed sets are incomparable, not merely presented by different recursions.

# The twisted-palindrome fixed grammar {#sec:grammar}

Let $$A(x)=\sum_{n\geq1}|\mathcal P_n|x^n
     =\sum_{n\geq1}C_{n-1}x^n
     =\frac{x}{1-A(x)}.$$ Let $E(x)$ and $O(x)$ enumerate the nonempty $\mathsf M$-fixed trees of even and odd order, respectively, and put $F=E+O$. Thus all four series in this section lie in $\mathbb Q[[x]]$ and have zero constant term; $A$ is the unique Catalan branch with $A(0)=0$.

[\[thm:coupled\]]{#thm:coupled label="thm:coupled"} The fixed-tree series are the unique pair $(E,O)\in x\mathbb Q[[x]]^2$ satisfying $$\label{eq:coupled}
\boxed{
 E=\frac{xO}{(1-E)^2-O^2},
 \qquad
 O=\frac{x(1+E)}{1-A(x^2)}.}$$ for the specified Catalan branch $A$.

Suppose first that the root has even order. By [\[eq:even-fixed\]](#eq:even-fixed){reference-type="eqref" reference="eq:even-fixed"}, its children form an arbitrary sequence of fixed trees. Their total order must be odd. Since $F(-x)=E-O$, the odd part of the sequence series is $$\frac12\left(\frac1{1-F(x)}-\frac1{1-F(-x)}\right)
 =\frac{O}{(1-E)^2-O^2}.$$ Multiplication by the root marker $x$ gives the first equation.

Now suppose that the root has odd order. Condition [\[eq:odd-fixed\]](#eq:odd-fixed){reference-type="eqref" reference="eq:odd-fixed"} says that its child tuple is a twisted palindrome. If there are $2r$ children, the first $r$ are arbitrary trees and determine the remaining children as their reversed componentwise $\mathsf M$-images. Each such pair has total order $2|T|$, so one pair has series $A(x^2)$ and a sequence of pairs has series $1/(1-A(x^2))$. If the child count is odd, the central child must be fixed. The off-centre pairs have even total order, and the root's children must also have even total order; hence the central child must have even order and contributes $E$, not $F$. The optional centre gives the factor $1+E$. Multiplying by $x$ proves the second equation. After clearing the two unit denominators, the Jacobian with respect to $(E,O)$ at $(x,E,O)=(0,0,0)$ is the identity. The formal implicit-function theorem in $\mathbb Q[[x]]$ therefore gives the asserted coupled uniqueness.

# An explicit algebraic equation {#sec:algebraic}

The coupled system proves algebraicity over the standard Catalan series. In this case the auxiliary series can be removed completely.

[\[thm:polynomial\]]{#thm:polynomial label="thm:polynomial"} Let $F=E+O$. Then $P(x,F(x))=0$, where $$\begin{aligned}
P(x,y)={}&(2x^2-x)y^6+(1-2x)y^5
 +(4x^3+6x^2+4x)y^4 \notag\\
&+(4x^3-12x^2-11x-6)y^3 \notag\\
&+(2x^4-11x^3+10x^2+26x+8)y^2 \label{eq:polynomial}\\
&+(4x^4-2x^3-20x^2-19x-3)y
 +2x^4+9x^3+14x^2+3x. \notag\end{aligned}$$ Moreover, $F$ is the unique series in $\mathbb Q[[x]]$ satisfying $P(x,F)=0$ and $F(0)=0$.

Put $$G=E-O,\qquad B=A(x^2),\qquad c=1-B.$$ Factoring the denominator in the first equation of [\[eq:coupled\]](#eq:coupled){reference-type="eqref" reference="eq:coupled"} and rewriting the second gives $$\begin{aligned}
 (F+G)(1-F)(1-G)&=x(F-G),                                  \label{eq:FG1}\\
 (c+x)G&=(c-x)F-2x,                                        \label{eq:FG2}\\
 B^2-B+x^2&=0.                                             \label{eq:B}\end{aligned}$$ The factor $c+x$ has constant term one, so [\[eq:FG2\]](#eq:FG2){reference-type="eqref" reference="eq:FG2"} can be used in the formal power-series ring. Eliminating $G$ from [\[eq:FG1\]](#eq:FG1){reference-type="eqref" reference="eq:FG1"}--[\[eq:FG2\]](#eq:FG2){reference-type="eqref" reference="eq:FG2"} and then $B$ using [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} gives the resultant $4x^2P(x,F)$. Since $\mathbb Q[[x]]$ has no zero divisors, [\[eq:polynomial\]](#eq:polynomial){reference-type="eqref" reference="eq:polynomial"} follows. This is a direct expansion using only the three displayed identities. The exact-control script independently reconstructs this identity: it takes the quadratic--linear resultant in $G$, reduces its coefficients modulo $B^2-B+x^2$, and evaluates the resulting quadratic norm coefficient by coefficient.

Finally, $$P(0,0)=0,\qquad P_y(0,0)=-3.$$ The formal implicit-function theorem therefore gives exactly one zero-constant branch. The series obtained in [\[thm:coupled\]](#thm:coupled){reference-type="ref" reference="thm:coupled"} lies on that branch.

For $n\geq1$, write $f_n=[x^n]F(x)$ and put $f_0=1$ for the separately adjoined empty lane. The first coefficients, together with the total carrier and two-cycle counts proved below, are shown in [1](#tab:coefficients){reference-type="ref" reference="tab:coefficients"}. A machine-readable table through order thirty is included with the exact controls.

::: {#tab:coefficients}
    $n$   $a_n$   $f_n$   $c_{n,2}$
  ----- ------- ------- -----------
      0       1       1           0
      1       1       1           0
      2       1       1           0
      3       2       2           0
      4       5       5           0
      5      14       8           3
      6      42      36           3
      7     132      48          42
      8     429     303          63
      9    1430     368         531
     10    4862    2792        1035
     11   16796    3248        6774
     12   58786   27310       15738

  : Carrier size $a_n$, fixed count $f_n$, and number $c_{n,2}$ of two-cycles. The $n=0$ row uses the separate empty-state convention.
:::

# The complete temporal census {#sec:census}

For $n\geq1$, put $a_n=C_{n-1}$, and retain $a_0=1$. Define the fixed-order Artin--Mazur zeta function in the usual way [@ArtinMazur1965]: $$\zeta_{\mathsf M,n}(z)
 =\exp\left(\sum_{q\geq1}
       |\operatorname{Fix}(\mathsf M_n^q)|\frac{z^q}{q}\right).$$

[\[cor:census\]]{#cor:census label="cor:census"} For every $n\geq0$, the order-$n$ functional graph consists of $$\label{eq:cycle-counts}
       f_n\text{ fixed points}
       \quad\text{and}\quad
       c_{n,2}=\frac{a_n-f_n}{2}\text{ two-cycles}.$$ For every $q\geq1$, $$\label{eq:iterate-fixed}
 |\operatorname{Fix}(\mathsf M_n^q)|=
 \begin{cases}
 f_n,&q\text{ odd},\\
 a_n,&q\text{ even},
 \end{cases}$$ and $$\label{eq:zeta}
 \boxed{\displaystyle
 \zeta_{\mathsf M,n}(z)
 =(1-z)^{-f_n}(1-z^2)^{-(a_n-f_n)/2}.}$$ In particular, both the empty and one-vertex lanes have zeta $(1-z)^{-1}$.

By [\[thm:involution\]](#thm:involution){reference-type="ref" reference="thm:involution"}, every component is a fixed point or a two-cycle. The fixed points are counted by $f_n$, so the remaining $a_n-f_n$ states pair to give [\[eq:cycle-counts\]](#eq:cycle-counts){reference-type="eqref" reference="eq:cycle-counts"}. An odd iterate fixes only the one-cycles, whereas an even iterate fixes every state, proving [\[eq:iterate-fixed\]](#eq:iterate-fixed){reference-type="eqref" reference="eq:iterate-fixed"}. The standard cycle product for the zeta function then gives one factor $(1-z)$ per fixed point and one factor $(1-z^2)$ per two-cycle, which is [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

# Owner subtraction, firewalls, and controls {#sec:scope}

The literal action separates the present map from its closest neighbors. Chen--Shapiro--Yang locate one illegal vertex and transfer a prefix of siblings in order to reverse leaf parity [@ChenShapiroYang2006]; Deutsch redistributes ordered-tree statistics [@Deutsch2000]; and the recent binary/plane-tree involutions of Li--Lin--Zhao are transported mirror and statistic symmetries [@LiLinZhao2024]. None applies simultaneous odd-fringe child reversals.

The 2026 Catalan involution $h$ is the strongest current owner objection [@ClaessonEtAl2026]. On plane trees, $h$ sends the root with three leaf children to a path of depth three, so it changes the parent--child relation; the same star is fixed by $\mathsf M$. Claesson et al. grade plane trees by edges, whereas our order is the number of vertices. Thus their Proposition 2.11 translates to one $h$-fixed tree at our order one, $C_k$ fixed trees at order $2k+2$, and none at odd order at least three. In particular, their counts at orders four and six are $1$ and $2$, while [1](#tab:coefficients){reference-type="ref" reference="tab:coefficients"} gives $f_4=5$ and $f_6=36$. Their global reversal factor, Donaghey map, fixed census, and abstract framework receive zero credit, but they are not the map in [\[def:update\]](#def:update){reference-type="ref" reference="def:update"}. Likewise, the cyclic actions of Bousquet-Mélou--Krattenthaler move a distinguished root corner, leaf, or nonleaf corner around a plane tree [@BousquetMelouKrattenthaler2025]; they do not reverse parity-selected child lists.

::: {#tab:firewall}
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Feature        odd-fringe mirror $\mathsf M$                                  global mirror $\mathsf J$                      parallel leaf peeling (P114)
  -------------- -------------------------------------------------------------- ---------------------------------------------- --------------------------------------------
  Local action   reverse iff old fringe order is odd                            reverse every child list                       delete eligible nonroot leaves

  State size     all vertices and edges retained                                all vertices and edges retained                rank decreases off the recurrent core

  Temporal law   every state has period $1$ or $2$                              every state has period $1$ or $2$              height-governed absorption

  Fixed test     even root pointwise; odd root $\mathsf M$-twisted palindrome   $\mathsf J$-twisted palindrome at every root   edgeless rooted-forest endpoint

  Enumeration    Catalan carrier and coupled $E/O$ grammar                      classical self-mirror census                   Cayley basins, height layers, local fibres
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Objectwise collision firewall. Classical global mirror and tree pruning are inputs/neighbors, not contribution claims.
:::

Parallel tree contraction and dynamical pruning are established mechanisms [@MillerReif1985; @KovchegovZaliapin2020]. The internal P114 lane deletes vertices, has transient states and a height clock, and counts labelled Cayley forest basins. The current map preserves the full tree and has no transient state. Thus the phase, update, temporal primitive, and enumerative objects are distinct despite the shared word "tree."

The accompanying standard-library verifier generates every plane rooted tree through order twelve. It compares recursive and snapshot-trigger updates, checks the underlying unordered shape, the pointwise induced vertex transport, involution, root-local fixed test, and the first six iterates on every state. An independent parity recurrence is compared with exhaustive fixed counts; the coupled equations and $P(x,F(x))$ are checked coefficientwise through degree thirty. A sparse exact lane additionally reconstructs the full resultant identity $4x^2P$. The stored CSV table contains the exact carrier, fixed, and two-cycle counts through that order. These computations attack conventions and arithmetic; the proofs above establish the arbitrary-order statements.

All Catalan enumeration, mirror symmetry, context-free algebraicity, resultant manipulation, involution cycle conversion, and zeta machinery are zero-credit. After subtraction, the residual is only the exact conjunction for [\[def:update\]](#def:update){reference-type="ref" reference="def:update"}: invariant odd-fringe triggers, the twisted-palindrome fixed grammar, the coupled parity system, its explicit degree-six branch, and the fixed-order cycle census. The bounded owner search does not prove priority. No asymptotic, irreducibility, minimal-polynomial, or general Catalan-action claim is made. External circulation remains **HOLD**.

# Conclusion

Odd-fringe mirroring is a finite involutive dynamics whose fixed trees are controlled by a parity-sensitive twisted palindrome. That local condition gives the coupled $E/O$ grammar, the explicit algebraic equation for the fixed series, and every one- and two-cycle count. The claim stops there: asymptotics, priority, and broader Catalan-involution conclusions lie outside the present scope.
