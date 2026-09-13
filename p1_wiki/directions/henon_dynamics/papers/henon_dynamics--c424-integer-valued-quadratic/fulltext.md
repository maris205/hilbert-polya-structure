---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c424-integer-valued-quadratic"
canonical_tex: "henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/main.tex"
canonical_pdf: "henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/main.pdf"
source_sha256: "587e29254e55491511d1c18338a3dddbddc95b080923b3233fb87a6e57f8599f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rational periodic points of integer-valued\protect quadratic Hénon maps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic>)
- [规范 TeX](<../../../../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify every rational periodic point of $G_P(x,y)=(y,P(y)-x)$ for every degree-two polynomial $P\in\mathbb Q[t]$ that takes integer values on $\mathbb Z$. An elementary affine normalization reduces this coefficient class to the previously classified monic integral branch and the missing family $F_a(x,y)=(y,y(y+1)/2+a-x)$, $a\in\mathbb Z$. For the latter family all rational periodic points are integral, and we give four parametric cycle families and eleven exceptional cycles, with exact least periods and no height or period cutoff. The proof adapts the earlier annulus and six-symbol method to the half-integral normal form, classifies every $a\le-146$ analytically, and exhausts the remaining 147 parameters, including one analytic control, by exact finite certificates independently reconstructed in the original coordinates. The entire integer-valued quadratic class has the sharp uniform bound of seventeen rational periodic points and the exact possible period set $\{1,2,3,4,5,6,7,9,10\}$. We determine the full coefficient locus attaining seventeen and record the ordinary-time return counts. The new conclusion is the complete coefficient-class classification; the elementary normalization and inherited proof mechanisms are not claimed as new methods.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  Rational periodic points of integer-valued\
  quadratic Hénon maps
```

## Markdown 正文

# The complete coefficient-class theorem {#sec:introduction}

Integer-valued polynomials need not have integer coefficients. In degree two this distinction changes the rational periodic orbits of conservative Hénon maps: the missing coefficient branch admits an exact five-cycle, whereas monic integral quadratic maps have only periods one through four. We give the complete rational cycle classification for the whole class $$\mathop{\mathrm{Int}}(\mathbb Z)_2=\{P\in\mathbb Q[t]:\deg P=2,\ P(\mathbb Z)\subseteq\mathbb Z\},\qquad
 G_P(x,y)=(y,P(y)-x).
 \label{eq:class}$$ The domain is all of $\mathbb Q^2$. The Jacobian determinant is $+1$, and a time step always means one application of the displayed map.

For a map $G$ on $\mathbb Q^2$ write $$\mathop{\mathrm{Per}}(G,\mathbb Q)=\{p\in\mathbb Q^2:G^d(p)=p\text{ for some }d\ge1\}.$$ The least such $d$ is the exact period of $p$. A coordinate word $(x_0,\ldots,x_{d-1})$ denotes the states $(x_i,x_{i+1})$, with indices modulo $d$. We identify words under cyclic rotation only, not under reversal. Repeated coordinates are allowed. Because adjacent coordinates determine both past and future, the least period of a valid primitive word is the least period of its state orbit.

[\[thm:whole\_class\]]{#thm:whole_class label="thm:whole_class"} Let $P\in\mathop{\mathrm{Int}}(\mathbb Z)_2$. Write uniquely $$P(t)=m\frac{t(t-1)}2+nt+r,
 \qquad m,n,r\in\mathbb Z,\quad m\ne0.
 \label{eq:newton}$$ The following rules give all rational periodic points of $G_P$ and their exact periods.

If $m=2\kappa$ is even, use the complete monic integral classification in Theorem [\[thm:imported\]](#thm:imported){reference-type="ref" reference="thm:imported"} for $$H(u,v)=(v,v^2+(n-\kappa)v+\kappa r-u),$$ and divide every coordinate of its cycles by $\kappa$. If $m$ is odd, put $$q=n-\frac{m+1}{2},\qquad
 A=mr+\frac{3q-q^2}{2}.
 \label{eq:odd_parameter}$$ Take exactly the cycles of $F_A$ in Theorem [\[thm:half\_classification\]](#thm:half_classification){reference-type="ref" reference="thm:half_classification"} and replace every coordinate $u$ by $(u-q)/m$.

For every such $P$, $$\#\mathop{\mathrm{Per}}(G_P,\mathbb Q)\le17.
 \label{eq:bound17}$$ Equality holds exactly when $m$ is odd and $A=-1$ in [\[eq:odd\_parameter\]](#eq:odd_parameter){reference-type="eqref" reference="eq:odd_parameter"}. The set of possible exact periods, as $P$ ranges over the entire class, is exactly $$\{1,2,3,4,5,6,7,9,10\}.
 \label{eq:periodset}$$ Original coordinates of periodic points of $G_P$ need not be integers.

The new classification needed in this theorem is the half-integral coefficient family $$F_a(x,y)=\left(y,\frac{y(y+1)}2+a-x\right),\qquad a\in\mathbb Z.
 \label{eq:F}$$ The subscript $a$ in [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} is an arbitrary integer parameter; it becomes $A$ when the theorem is applied to [\[eq:newton\]](#eq:newton){reference-type="eqref" reference="eq:newton"}.

[\[thm:half\_classification\]]{#thm:half_classification label="thm:half_classification"} For every $a\in\mathbb Z$, all rational periodic points of $F_a$ are integral. Its complete oriented cycles are the words in Tables [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"} and [1](#tab:exceptions){reference-type="ref" reference="tab:exceptions"} at parameter $a$. In Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"}, $k$ runs through all nonnegative integers. At a parameter satisfying multiple rows, take their union. Every displayed cycle is distinct and has the stated exact period; there are no omitted degeneracy exclusions. The sharp bound is $17$, attained exactly at $a=-1$.

\@L.27L.56c@ Parameter $a$ & Coordinate words & Period\
$1-k(k+1)/2$ & $(1-k)$, $(k+2)$ & $1$ each\
$-7-k(k+1)/2$ & $(-k-3,k-2)$ & $2$\
$-3-k(k+1)/2$ & $(-k-3,k,k)$, $(k-2,-k-1,-k-1)$ & $3$ each\
$-1-k(k+1)/2$ & $(-k-1,-k-1,k,k)$ & $4$\

::: {#tab:exceptions}
    Parameter $a$ Exceptional coordinate word     Exact period
  --------------- ------------------------------- --------------
            $-12$ $(-6,-1,-6,4,4)$                $5$
            $-11$ $(-5,-2,-5,1)$                  $4$
             $-8$ $(-4,-2,-3,-3,-2,-4,0)$         $7$
             $-6$ $(-3,-2,-2,-3,-1)$              $5$
             $-5$ $(-4,-1,-1,-4,2,2)$             $6$
             $-3$ $(-3,-1,0,-2,-2,0,-1,-3,1,1)$   $10$
             $-2$ $(-2,-1,0,-1,-2,0,0)$           $7$
             $-1$ $(-2,-1,1,1,-1,-2,1,2,1)$       $9$
             $-1$ $(-2,0,1,0)$                    $4$
              $0$ $(-1,-1,1,2,2,1)$               $6$
              $0$ $(-1,0,1,1,0)$                  $5$

  : The eleven cycles not in Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"}. Each word is the lexicographically smallest of its rotations. These are exact finite-certificate outputs, not samples used to infer the all-parameter theorem.
:::

#### What is inherited and what is completed.

The monic integral classification is the prior internal working manuscript C412 [@c412]; its exact statement is reproduced in Appendix [9](#app:integral){reference-type="ref" reference="app:integral"}. We also use its maximum-coordinate, annulus, six-symbol, and finite-partial-permutation mechanisms. The local word argument is reproduced at the point of use, with attribution. The elementary Newton-basis normalization is not a new method. The contribution here is the complete missing normal form, and hence a full natural coefficient-class atlas with a different sharp bound and period spectrum. The exceptions, equality locus, and return law are consequences of that one classification.

The all-parameter proof has three parts: no cycles for $a\ge2$ and two fixed points at $a=1$; a uniform symbolic exhaustion for $a\le-146$; and exact finite certificates for $-145\le a\le1$, where $a=1$ is an independently proved control. The finite certificate is a proof dependency, not an empirical experiment. It was independently reconstructed using a different graph algorithm before this manuscript was prepared [@am1certificate].

#### Relation to the wider problem.

Ingram [@ingram2014canonical] develops canonical-height and specialization results for Hénon maps and studies a quadratic rational-period conjecture for $(y,x+y^2+b)$. That displayed map has Jacobian determinant $-1$, whereas [\[eq:class\]](#eq:class){reference-type="eqref" reference="eq:class"} has determinant $+1$. Our statement is not a solution of that conjecture or of uniform boundedness for arbitrary rational-coefficient Hénon maps. Kim, Krieger, Postolache, and Szeto [@kim2025many Theorems A--B] construct conservative Hénon maps with many rational periodic points and long integer cycles from integer-valued polynomials in growing odd degree. Their construction motivates keeping the coefficient class explicit; its degree range is different from the fixed degree-two classification here. These comparisons assert scope and dependence, not worldwide priority.

# Affine normalization of the full class {#sec:normalization}

The normalization is elementary but must act on all rational points, not just an integral sublattice. Negative leading coefficients are included throughout.

[\[lem:newton\]]{#lem:newton label="lem:newton"} Every $P\in\mathop{\mathrm{Int}}(\mathbb Z)_2$ has the unique representation [\[eq:newton\]](#eq:newton){reference-type="eqref" reference="eq:newton"}. Conversely, every expression there is a degree-two integer-valued polynomial.

Set $$r=P(0),\qquad n=P(1)-P(0),\qquad
 m=P(2)-2P(1)+P(0).$$ These are integers. The polynomial in [\[eq:newton\]](#eq:newton){reference-type="eqref" reference="eq:newton"} agrees with $P$ at $0,1,2$, so the two degree-at-most-two polynomials agree identically. The condition $\deg P=2$ gives $m\ne0$. Uniqueness follows by evaluating at the same three arguments. Conversely, $t(t-1)$ is even for every $t\in\mathbb Z$.

[\[prop:normalization\]]{#prop:normalization label="prop:normalization"} For even $m=2\kappa$, the rational linear bijection $T(x,y)=(\kappa x,\kappa y)$ conjugates $G_P$ to $$(u,v)\longmapsto
 (v,v^2+(n-\kappa)v+\kappa r-u).
 \label{eq:even_conjugacy}$$ For odd $m$, define $q,A$ by [\[eq:odd\_parameter\]](#eq:odd_parameter){reference-type="eqref" reference="eq:odd_parameter"}. Then $q,A\in\mathbb Z$, and the rational affine bijection $$T(x,y)=(mx+q,my+q)
 \label{eq:odd_conjugacy}$$ satisfies $TG_PT^{-1}=F_A$. Both conjugacies preserve rational periodic points and exact native periods.

When $m=2\kappa$, one has $P(t)=\kappa t^2+(n-\kappa)t+r$ and $\kappa\ne0$. Substitution gives [\[eq:even\_conjugacy\]](#eq:even_conjugacy){reference-type="eqref" reference="eq:even_conjugacy"}.

If $m$ is odd, $q\in\mathbb Z$ and $q(3-q)$ is even, so $A\in\mathbb Z$. First scale both coordinates by $m$. The scalar polynomial becomes $$\frac{v^2}{2}+\left(n-\frac m2\right)v+mr
 =\frac{v^2}{2}+\left(q+\frac12\right)v+mr.$$ Translating both coordinates by $q$ makes the linear coefficient $1/2$ and the constant term $$mr+\frac{q^2}{2}-\left(q+\frac12\right)q+2q
 =mr+\frac{3q-q^2}{2}=A.$$ This is [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} with parameter $A$. Each change has nonzero rational slope and a rational inverse. Applying the conjugacy and its inverse to $G_P^d(p)=p$ proves preservation of the least positive $d$.

The even branch is therefore exactly an application of C412, not a new classification proof. Appendix [9](#app:integral){reference-type="ref" reference="app:integral"} gives every word and parameter restriction of the imported theorem, including its small-index degeneracies. Its bound of eight points will exclude even $m$ from the equality case of [\[eq:bound17\]](#eq:bound17){reference-type="eqref" reference="eq:bound17"}. It remains to prove Theorem [\[thm:half\_classification\]](#thm:half_classification){reference-type="ref" reference="thm:half_classification"}.

The periodic coordinates for $F_A$ will be integers, but their inverse images are $(u-q)/m$; in the even branch they are $u/\kappa$. For example, $P(t)=2t^2$ gives the fixed point $(1/2,1/2)$. The theorem concerns rational periodic points of every map in [\[eq:class\]](#eq:class){reference-type="eqref" reference="eq:class"}, not just those periodic orbits contained in $\mathbb Z^2$.

# Integrality, the upper boundary, and a finite height bound {#sec:integrality}

The inverse of $F_a$ is $(x,y)\mapsto(x(x+1)/2+a-y,x)$. A rational periodic orbit, with any positive period $d$, gives a cyclic scalar sequence satisfying $$x_{i-1}+x_{i+1}=\frac{x_i(x_i+1)}2+a
 \qquad(i\in\mathbb Z/d\mathbb Z).
 \label{eq:recurrence}$$ All estimates below allow repeated coordinates and the periods one and two.

[\[lem:integrality\]]{#lem:integrality label="lem:integrality"} Every rational periodic point of $F_a$, $a\in\mathbb Z$, belongs to $\mathbb Z^2$.

Normalize $|p|_p=p^{-1}$ for each prime $p$. For an odd prime set $M=\max_i|x_i|_p$. If $M>1$, choose $j$ with $|x_j|_p=M$. The terms $x_j^2/2$, $x_j/2$, and $a$ have norms $M^2$, $M$, and at most one. The first is uniquely largest, so the right side of [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} has norm $M^2$, whereas the left side has norm at most $M$. This is impossible.

At $p=2$, the same terms have norms $2M^2$, $2M$, and at most one. For $M>1$ the unique largest term gives norm $2M^2>M$, again a contradiction. Thus every $x_i$ is integral at every prime, hence belongs to $\mathbb Z$.

Both $F_a$ and its inverse preserve $\mathbb Z^2$ because consecutive integers have even product. This invariance does not say that every integer point is periodic. Nor does the scalar polynomial descend to a function modulo two: $0$ and $2$ are congruent, but their triangular values are $0$ and $3$. An integral-coefficient finite quotient argument would not apply without a separate justification.

[\[lem:upper\]]{#lem:upper label="lem:upper"} If $a\ge2$, then $\mathop{\mathrm{Per}}(F_a,\mathbb Q)$ is empty. At $a=1$ it consists exactly of the fixed points $(1,1)$ and $(2,2)$.

Sum [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} over the cycle and complete the square: $$\sum_i\left(x_i-\frac32\right)^2
 =d\left(\frac94-2a\right).
 \label{eq:summed}$$ For $a\ge2$ the right side is negative. At $a=1$, Lemma [\[lem:integrality\]](#lem:integrality){reference-type="ref" reference="lem:integrality"} makes each summand at least $1/4$, and their average is exactly $1/4$. Every coordinate is therefore one or two. If some $x_i=1$, its equation forces both neighbors to be one, and propagation around the cycle makes the word constant. Otherwise every coordinate is two. Both constant words satisfy [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}.

[\[lem:height\]]{#lem:height label="lem:height"} For every real cyclic solution of [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}, $$M:=\max_i|x_i|\le\frac{5+\sqrt{25+8|a|}}2.
 \label{eq:height}$$

At a coordinate $t$ with $|t|=M$, the triangle inequality gives $$\left|\frac{t(t+1)}2\right|\ge\frac{M^2-M}{2},
 \qquad
 \frac{M^2-M}{2}-|a|\le2M.$$ The resulting quadratic inequality $M^2-5M-2|a|\le0$ yields [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}.

For a fixed parameter, integrality and [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"} give a finite state set containing every periodic point. This alone is not the all-parameter classification: its size grows with $|a|$. The next two sections supply the uniform reduction.

The rational affine map $S(x,y)=(x/2+1/4,y/2+1/4)$ conjugates $F_a$ to $$(u,v)\longmapsto(v,v^2+a/2+7/16-u).$$ Indeed, [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} gives $u_{i-1}+u_{i+1}=u_i^2+a/2+7/16$. The constant has reduced denominator sixteen, and the integral coordinate lattice maps to $1/4+(1/2)\mathbb Z$. At $a=0$ the states $$(0,1),(1,1),(1,0),(0,-1),(-1,0)$$ form an exact five-cycle. By the period statement in C412, $F_0$ cannot be rationally conjugate to any monic integral member. This is a separation witness for this parameter, not a claim that every individual $F_a$ has such a nonconjugacy property.

# The uniform annulus for large negative parameters {#sec:annulus}

We adapt the annulus and coefficient-separation argument of C412 [@c412 Sections 3--4]. The scaling and the threshold must be checked anew: the centered recurrence here has a factor of two on its neighbor sum.

For the rest of this section assume $a\le-146$ and put $$v_i=x_i+\frac12,\qquad c=-2a-\frac74,
 \qquad N=-2a-2.
 \label{eq:center}$$ Then [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} becomes $$v_i^2-c=2(v_{i-1}+v_{i+1}),\qquad c=N+\frac14.
 \label{eq:center_recurrence}$$ There is a unique integer $k\ge0$ such that $k^2\le N\le k^2+2k$; these intervals partition the nonnegative integers. Set $$\rho=k+\frac12,\qquad s=N-k(k+1),\qquad c=\rho^2+s.
 \label{eq:rho_s}$$ Our hypothesis gives $N\ge290$, $k\ge17$, and $$\rho\ge\frac{35}{2},\qquad
 -\rho+\frac12\le s\le\rho-\frac12.
 \label{eq:s_range}$$

[\[lem:annulus\]]{#lem:annulus label="lem:annulus"} Every rational periodic orbit at $a\le-146$ satisfies $$\rho-2\le |v_i|\le\rho+2.
 \label{eq:annulus}$$ Consequently it has a unique representation $$v_i=\varepsilon_i\rho+\delta_i,
 \qquad \varepsilon_i\in\{-1,1\},\quad
 \delta_i\in\{-2,-1,0,1,2\}.
 \label{eq:ten_symbols}$$

Let $R=\max_i|v_i|$. The recurrence gives $$R\le2+\sqrt{c+4},\qquad |v_i^2-c|\le4R.
 \label{eq:center_bounds}$$ The first inequality follows from $R^2-c\le4R$. By [\[eq:s\_range\]](#eq:s_range){reference-type="eqref" reference="eq:s_range"}, $$c+4\le\rho^2+\rho+\frac72<(\rho+1)^2,$$ where the strict inequality holds for $\rho>5/2$. Thus $R<\rho+3$. By Lemma [\[lem:integrality\]](#lem:integrality){reference-type="ref" reference="lem:integrality"}, both $R$ and $\rho$ are half-integers, so $R\le\rho+2$.

If $|v_i|\le\rho-3$ at an index, then $$c-v_i^2\ge\rho^2-\rho+\frac12-(\rho-3)^2
 =5\rho-\frac{17}{2}>4\rho+8\ge4R.$$ The strict inequality requires $\rho>33/2$, which our threshold satisfies. This contradicts [\[eq:center\_bounds\]](#eq:center_bounds){reference-type="eqref" reference="eq:center_bounds"}. The half-integral lattice therefore gives the lower bound in [\[eq:annulus\]](#eq:annulus){reference-type="eqref" reference="eq:annulus"}. The two center intervals are disjoint and their offsets are integers, proving uniqueness in [\[eq:ten\_symbols\]](#eq:ten_symbols){reference-type="eqref" reference="eq:ten_symbols"}.

[\[lem:separation\]]{#lem:separation label="lem:separation"} In [\[eq:ten\_symbols\]](#eq:ten_symbols){reference-type="eqref" reference="eq:ten_symbols"}, every offset is even and $s$ is divisible by four. Writing $\delta_i=2d_i$ and $t=s/4$, the entire cyclic sequence satisfies exactly $$\varepsilon_{i-1}+\varepsilon_{i+1}=2\varepsilon_i d_i,
 \qquad d_{i-1}+d_{i+1}=d_i^2-t,
 \qquad d_i\in\{-1,0,1\}.
 \label{eq:local}$$

Substitution into [\[eq:center\_recurrence\]](#eq:center_recurrence){reference-type="eqref" reference="eq:center_recurrence"} gives $$2\rho(\varepsilon_{i-1}+\varepsilon_{i+1}
              -\varepsilon_i\delta_i)
 =\delta_i^2-2\delta_{i-1}-2\delta_{i+1}-s.
 \label{eq:separation}$$ The right side has absolute value at most $$12+|s|\le\rho+\frac{23}{2}<2\rho.$$ The coefficient multiplying $2\rho$ on the left is an integer. It must be zero, and so must the right side. The sum of two neighboring signs is even, hence every $\delta_i$ is even. On writing $\delta_i=2d_i$, the vanishing right side gives $s=4(d_i^2-d_{i-1}-d_{i+1})$. Division gives [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"}.

The six pairs $(\varepsilon_i,d_i)$ and both local equations [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"} are exactly the symbol system already classified in C412. We reproduce its elementary word exhaustion to make the dependence transparent and to keep the present proof readable without an external proof-file lookup.

# The inherited local-word classification and its application {#sec:symbols}

[\[lem:local\_words\]]{#lem:local_words label="lem:local_words"} Every cyclic solution of [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"} has $t\in\{-1,0,1,3\}$. Up to rotation its signs and offsets are exactly the following patterns and their repetitions: $$\begin{array}{c|c|c}
t&\text{offset word }(d_i)&\text{sign word }(\varepsilon_i)\\ \hline
-1&(1)&(\varepsilon)\\
0&(0,0,0,0)&(-1,-1,1,1)\\
1&(-1,0,0)&(\varepsilon,-\varepsilon,-\varepsilon)\\
3&(-1,-1)&(-1,1)
\end{array}
\qquad \varepsilon\in\{-1,1\}.
\label{eq:patterns}$$

This is the local argument of [@c412 Section 4]. If $d_i=1$, the two neighboring signs equal $\varepsilon_i$; if $d_i=-1$, both equal $-\varepsilon_i$; and if $d_i=0$, the two neighboring signs are opposite. Adjacent offsets $1,-1$ are therefore impossible: the first rule would make their signs equal, and the second would make them opposite. The offset equation gives $t=d_i^2-d_{i-1}-d_{i+1}\in\{-2,-1,0,1,2,3\}$. We exhaust these six possibilities.

For $t=-2$, each neighbor sum is $d_i^2+2\le2$, so every $d_i=0$; the offset equation would then read $0=2$.

For $t=-1$, an offset $-1$ would have two neighbors $1$, which is forbidden. A zero would need a neighboring $1$, but that $1$ needs two neighbors $1$, contradicting the zero. All offsets are $1$, and their signs are constant.

For $t=0$, an offset $-1$ would need a neighbor $1$, which is forbidden. A zero then has two zero neighbors. An offset $1$ would require one neighbor $1$ and one zero, contradicting the rule at the zero. Thus every offset vanishes. The sign equation is $\varepsilon_{i+1}=-\varepsilon_{i-1}$, whose solutions are precisely the rotations of the four-period word in [\[eq:patterns\]](#eq:patterns){reference-type="eqref" reference="eq:patterns"}.

For $t=1$, an offset $1$ can have no neighbor $-1$, so its two neighbors would have to be zero. Such a zero, adjacent to $1$, would require its other neighbor to be $-2$. This is impossible. With only offsets $-1,0$ remaining, each $-1$ has two zero neighbors and each zero has one zero neighbor and one $-1$ neighbor. The offset word is therefore a repetition of $(-1,0,0)$. The sign rule at $-1$ gives $(\varepsilon,-\varepsilon,-\varepsilon)$, and the rules at the two zeros make this triple repeat with the same $\varepsilon$.

For $t=2$, an offset $1$ would need a neighbor $-1$, forbidden. A zero would need two $-1$ neighbors. Both those neighbors would have sign opposite to that of the zero, hence equal to each other, contradicting the sign rule at zero. All offsets would consequently be $-1$, giving $-2=-1$ in the offset equation.

For $t=3$, a zero would need neighbors summing to $-3$, impossible. Every nonzero offset needs two $-1$ neighbors, so $1$ is forbidden. The offsets are all $-1$ and the signs alternate. These arguments are cyclic and impose no upper bound on the period.

[\[prop:large\_classification\]]{#prop:large_classification label="prop:large_classification"} For every $a\le-146$, Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"} gives the entire rational periodic locus. For every $k\ge0$, all words in that table are valid at their displayed parameters and have their stated exact periods, even outside the large-parameter region.

In the large-parameter region, Lemmas [\[lem:annulus\]](#lem:annulus){reference-type="ref" reference="lem:annulus"} and [\[lem:separation\]](#lem:separation){reference-type="ref" reference="lem:separation"} reduce every rational cycle to [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"}. Lemma [\[lem:local\_words\]](#lem:local_words){reference-type="ref" reference="lem:local_words"} exhausts its cyclic solutions. Recovering $x_i=\varepsilon_i\rho+2d_i-1/2$ and using [\[eq:rho\_s\]](#eq:rho_s){reference-type="eqref" reference="eq:rho_s"} gives $$a=-\frac{k(k+1)}2-2t-1.
 \label{eq:t_parameter}$$ The four values $t=-1,3,1,0$ give respectively the fixed, two-, three-, and four-period rows of Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"}. For a fixed $a\le-146$, the integer $k$ chosen from $N$ is unique and $s=4t$ is fixed. Thus at most one of these four rows occurs in this large-parameter derivation, and there are at most six periodic points at such a parameter.

For existence at every $k\ge0$, take each symbol pattern in [\[eq:patterns\]](#eq:patterns){reference-type="eqref" reference="eq:patterns"}, set $\rho=k+1/2$ and $s=4t$, and use [\[eq:t\_parameter\]](#eq:t_parameter){reference-type="eqref" reference="eq:t_parameter"}. Both sides of [\[eq:separation\]](#eq:separation){reference-type="eqref" reference="eq:separation"} vanish, so [\[eq:center\_recurrence\]](#eq:center_recurrence){reference-type="eqref" reference="eq:center_recurrence"} and then [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} hold algebraically. No annulus inequality is needed for this direction.

The two fixed coordinates differ by $2k+1>0$. The two entries of the two-cycle also differ by $2k+1$. In the four-cycle the two values are distinct; its doubled-pair pattern is not of period two. Each three-cycle has two distinct values, hence least period three. The value repeated in the first three-cycle is $k\ge0$, while the value repeated in the second is $-k-1<0$, so these cycles never coincide. Thus there are no small-index degeneracies in Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"}.

In particular, the only unresolved parameters after the analytic argument are $-145\le a\le0$. The separate boundary value $a=1$ will be included as a control in the exact certificate. The finite range is deduced before the computation, not selected by observing when exceptional cycles disappear.

# The complete finite residual certificate {#sec:finite}

We now describe the exact finite dependency, including why its graph contains every periodic point and why its terminal set contains only periodic points. The original producer, output, independent checker, and independent output are retained as byte-identical evidence copies [@am1certificate]. Appendix [10](#app:certificate){reference-type="ref" reference="app:certificate"} prints the mathematical producer code and every parameter's cycle histogram. No mathematical certificate was rerun to prepare this manuscript.

## A proved finite alphabet

Use the odd coordinates $z_i=2x_i+1$. Equation [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} becomes $$z_i^2+8a+7=4(z_{i-1}+z_{i+1}),\qquad
 \mathcal G_a(z,w)=\left(w,\frac{w^2+8a+7}{4}-z\right).
 \label{eq:odd_map}$$ For odd $w$, $w^2+8a+7$ is divisible by eight. Consequently $\mathcal G_a$ and its inverse preserve the odd lattice; the displayed quotient is an even integer and its difference with odd $z$ is odd.

For every $-145\le a\le1$ set $$\begin{split}
 B_a&=4+\lfloor\sqrt{9-8a}\rfloor,\\
 S_a&=\{z\in\mathbb Z:z\text{ odd},\ |z|\le B_a,
                   \ |z^2+8a+7|\le8B_a\}.
 \end{split}
 \label{eq:alphabet}$$ The maximum estimate [\[eq:center\_bounds\]](#eq:center_bounds){reference-type="eqref" reference="eq:center_bounds"} applies here as well: $c=-2a-7/4$ has $c+4>0$ for this entire range. Since $z_i=2v_i$, it gives $|z_i|\le4+\sqrt{9-8a}$ and hence $|z_i|\le B_a$. Equation [\[eq:odd\_map\]](#eq:odd_map){reference-type="eqref" reference="eq:odd_map"} gives the second restriction in [\[eq:alphabet\]](#eq:alphabet){reference-type="eqref" reference="eq:alphabet"}. Every rational periodic point therefore corresponds to a state of the finite set $V_0=S_a^2$. All operations defining it are integer comparisons and an integer square root; no floating-point bound is used.

[\[lem:pruning\]]{#lem:pruning label="lem:pruning"} Let $G$ be an injective map on a set $X$, and let $V_0\subset X$ be finite and contain every periodic point of $G$. Define $$V_{j+1}=\{p\in V_j:G(p)\in V_j\}.
 \label{eq:prune}$$ The sets stabilize after finitely many strict decreases, and the stable set is exactly the periodic locus of $G$.

This is the finite-graph mechanism used in [@c412 Section 5]. The descending sequence of finite sets must stabilize. Every periodic orbit lies in $V_0$ and, by induction, in every $V_j$. At stabilization, $G$ restricts to an injective self-map of a finite set, so that restriction is a permutation. Every surviving point is consequently periodic. The two inclusions give the conclusion.

The inverse in [\[eq:odd\_map\]](#eq:odd_map){reference-type="eqref" reference="eq:odd_map"} verifies injectivity, so the lemma applies. It places no independent upper cutoff on the length of a cycle. Iterating each survivor until its first return yields every oriented cycle, and distinct adjacent states certify its least period.

## What the finite execution certifies

The author certificate ran once on precisely the 147 integers $a=-145,-144,\ldots,1$. For each $a$ it records $B_a$, the complete alphabet $S_a$, every strictly decreasing pruning cardinality, and all canonically rotated primitive coordinate words. The program verifies the recurrence for each word, the distinctness of its states, disjointness of different cycles, and equality between the union of the expanded words and the entire stable set. It also verifies inclusion of every valid parametric family from Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"} and records all unmatched cycles. The unmatched cycles are exactly Table [1](#tab:exceptions){reference-type="ref" reference="tab:exceptions"}.

The output has 306 periodic states and 113 oriented cycles *across 147 different maps*. Its largest alphabet has sixteen coordinates; its largest initial graph has 256 states; and no parameter needs more than sixteen strict pruning decreases. These totals are bookkeeping for the proved residual family, not a claim that one map has 306 periodic points. Every row of the result is summarized in Table [2](#tab:residual){reference-type="ref" reference="tab:residual"}; the complete alphabets, trajectories, and words remain in the accompanying exact output.

## Independent reconstruction in original coordinates

The nonauthor check used the same fixed square $$W=\{-19,-18,\ldots,19\}^2
 \label{eq:independent_box}$$ for every residual parameter. This is a proved complete box: by Lemma [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"}, $M^2-5M-290\le0$ when $|a|\le145$. At the integer $M=20$ the left side is $10>0$, and it increases thereafter. Therefore $M\le19$.

For each $a$, the independent checker forms the successor of every state in $W$ under the original map $F_a$. An edge leaving $W$ terminates a path. It visits each uncompleted state, following a path until escape, a previously completed vertex, or a repeated vertex on the present path. In the last case, precisely the suffix beginning at that repeat is a cycle. Marking the whole path completed and continuing processes every vertex exactly once. Every cycle is found because a walk entering a finite cycle cannot escape, and a previously completed walk already contains its cycle. The retained suffixes are genuine cycles, so there are no false positives.

All 147 graphs were computed before the author output was loaded. The check then compared every full oriented word and expanded periodic-state set, not merely their total cardinalities. All 223,587 vertices were processed once, and all 147 cycle and state sets matched. The checker uses neither doubled coordinates, the filtered alphabet, nor iterative pruning. Its finite completeness thus has a different implementation from the producer.

The author run and independent run both completed successfully on 8 September 2026, with exact outputs retained. These are current-team computer-assisted checks, not a claim of human peer review. The finite results, Lemma [\[lem:upper\]](#lem:upper){reference-type="ref" reference="lem:upper"}, and Proposition [\[prop:large\_classification\]](#prop:large_classification){reference-type="ref" reference="prop:large_classification"} exhaust every integer parameter and hence establish the cycle-list part of Theorem [\[thm:half\_classification\]](#thm:half_classification){reference-type="ref" reference="thm:half_classification"}.

# Coexistence, sharp bounds, and ordinary return counts {#sec:counts}

The parameter rows in Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"} are not disjoint sets of parameters. We first account for all cycles without overlap subtractions.

For $b\in\mathbb Z$, define the triangular-number indicator $$\tau(b)=
 \begin{cases}
 1,& b=k(k+1)/2\text{ for an integer }k\ge0,\\
 0,&\text{otherwise}.
 \end{cases}
 \label{eq:tau}$$ Equivalently, $b\ge0$ and $8b+1$ is an odd square. The triangular values are strictly increasing in $k\ge0$, so a fixed row of Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"} has at most one index at each parameter.

[\[prop:counts\]]{#prop:counts label="prop:counts"} Let $C_d(a)$ be the number of oriented rational cycles of exact period $d$ under $F_a$. Then $$\begin{aligned}
 C_1(a)&=2\tau(1-a),& C_2(a)&=\tau(-7-a),\notag\\
 C_3(a)&=2\tau(-3-a),&
 C_4(a)&=\tau(-1-a)+\mathbf{1}_{\{a\in\{-11,-1\}\}},\notag\\
 C_5(a)&=\mathbf{1}_{\{a\in\{-12,-6,0\}\}},&
 C_6(a)&=\mathbf{1}_{\{a\in\{-5,0\}\}},\notag\\
 C_7(a)&=\mathbf{1}_{\{a\in\{-8,-2\}\}},&
 C_9(a)&=\mathbf{1}_{\{a=-1\}},\notag\\
 C_{10}(a)&=\mathbf{1}_{\{a=-3\}},&&
 \label{eq:counts}\end{aligned}$$ and $C_d(a)=0$ for every other positive integer $d$.

Different period rows cannot describe the same cycle. The two fixed points and two three-cycles within their rows are distinct by Proposition [\[prop:large\_classification\]](#prop:large_classification){reference-type="ref" reference="prop:large_classification"}. The exceptional four-cycle at $a=-11$ is $(-5,-2,-5,1)$, while its parametric four-cycle is $(-5,-5,4,4)$, obtained with $k=4$. At $a=-1$ the corresponding words are $(-2,0,1,0)$ and $(-1,-1,0,0)$, with $k=0$. These pairs are not rotations of one another. All other exceptional periods are absent from the parametric table. Thus no listed cycles coincide, including at overlapping parameters. Reading the complete tables gives [\[eq:counts\]](#eq:counts){reference-type="eqref" reference="eq:counts"}.

[\[prop:sharp\]]{#prop:sharp label="prop:sharp"} For all $a\in\mathbb Z$, $\#\mathop{\mathrm{Per}}(F_a,\mathbb Q)\le17$, with equality exactly at $a=-1$. Every period in [\[eq:periodset\]](#eq:periodset){reference-type="eqref" reference="eq:periodset"} occurs.

For $a\le-146$, Proposition [\[prop:large\_classification\]](#prop:large_classification){reference-type="ref" reference="prop:large_classification"} shows that there are at most six points. For $a\ge2$ there are none. The complete finite certificate, whose per-parameter counts are displayed in Table [2](#tab:residual){reference-type="ref" reference="tab:residual"}, has maximum seventeen only at $a=-1$. At that parameter the disjoint cycles are $$(-1,-1,0,0),\quad (-2,0,1,0),\quad
 (-2,-1,1,1,-1,-2,1,2,1),$$ of lengths four, four, and nine. This proves the bound and its exact equality locus. Tables [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"} and [1](#tab:exceptions){reference-type="ref" reference="tab:exceptions"} exhibit every period in [\[eq:periodset\]](#eq:periodset){reference-type="eqref" reference="eq:periodset"}, and the exhaustive classification excludes all others.

Proposition [\[prop:normalization\]](#prop:normalization){reference-type="ref" reference="prop:normalization"} reduces every polynomial in [\[eq:class\]](#eq:class){reference-type="eqref" reference="eq:class"} to one of the stated branches by a bijection of $\mathbb Q^2$. The half-integral branch is now completely classified by Theorem [\[thm:half\_classification\]](#thm:half_classification){reference-type="ref" reference="thm:half_classification"}. The even branch is Theorem [\[thm:imported\]](#thm:imported){reference-type="ref" reference="thm:imported"}, with at most eight points and periods in $\{1,2,3,4\}$. Counts and exact periods are preserved by the affine changes, and their inverse formulas give all original rational coordinates. Equality at seventeen is therefore possible exactly in the odd branch with $A=-1$. Every map $F_a$ belongs to [\[eq:class\]](#eq:class){reference-type="eqref" reference="eq:class"}, so all nine periods already occur within the full coefficient class.

[\[cor:returns\]]{#cor:returns label="cor:returns"} For every $a\in\mathbb Z$ and $N\ge1$, $$\#\mathop{\mathrm{Fix}}(F_a^N,\mathbb Q)=\sum_{d\mid N}dC_d(a),\qquad
 \zeta_{F_a,\mathbb Q}(z)=\prod_{d\ge1}(1-z^d)^{-C_d(a)}.
 \label{eq:returns}$$ The product is finite. For $G_P$ in the odd branch use $a=A$; for its even branch use the cycles of Theorem [\[thm:imported\]](#thm:imported){reference-type="ref" reference="thm:imported"}.

A cycle of exact length $d$ contributes all its $d$ points to $\mathop{\mathrm{Fix}}(F_a^N,\mathbb Q)$ exactly when $d$ divides $N$. For the formal power series $$\zeta_{F_a,\mathbb Q}(z)
 =\exp\left(\sum_{N\ge1}\frac{\#\mathop{\mathrm{Fix}}(F_a^N,\mathbb Q)}{N}z^N\right),$$ substitute the first formula and use $\sum_{j\ge1}z^{dj}/j=-\log(1-z^d)$. Conjugacy preserves the same return counts for $G_P$.

# Scope and evidence status {#sec:scope}

The classification covers degree exactly two, all polynomials in $\mathop{\mathrm{Int}}(\mathbb Z)$ of that degree, and all rational points of the plane under the native map $(y,P(y)-x)$. It does not classify arbitrary rational-coefficient quadratic polynomials that fail to be integer-valued, other determinant parameters, higher degree, or finite-residue periodicity. No number-field or local-field extension is implicit.

The resulting sharp bound, equality locus, exceptional periods, and zeta function are parts of a single cycle classification. The zeta in [\[eq:returns\]](#eq:returns){reference-type="eqref" reference="eq:returns"} is an ordinary-time finite-orbit generating function; it supplies no arithmetic-prime Euler factor, root number, automorphy, or spectral realization.

The proof has a finite computer-assisted dependency, with exact integer code, complete parameter coverage, and a separately implemented nonauthor reconstruction. Its algorithms and completion logic are printed below. The evidence directory retains the full executed programs and outputs, rather than regenerating a certificate during typesetting. The imported C412 theorem is an anonymous, unpublished internal working manuscript, not a journal publication; an exact PDF copy accompanies this article. Current-team AI-assisted preparation and internal checks are disclosed here and in the source audit. They are not represented as human peer review or external publication acceptance.

# The precisely imported monic integral classification {#app:integral}

This appendix states the exact prior result used for even $m$. It is Theorem 1.1 and Tables 1--2 of the anonymous internal manuscript C412 [@c412]; its proof is not claimed as part of the present increment. The accompanying file is an exact copy of that complete manuscript, whose proof contains its own analytic reduction and finite-complement evidence.

[\[thm:imported\]]{#thm:imported label="thm:imported"} Let $\alpha,\beta\in\mathbb Z$ and $H_{\alpha,\beta}(x,y)=(y,y^2+\beta y+\alpha-x)$. Write uniquely $\beta=2h+e$, $h\in\mathbb Z$, $e\in\{0,1\}$, and put $$D=\alpha-h^2+(2-e)h.
 \label{eq:C412_parameter}$$ Every rational periodic point is integral. The complete rational periodic cycles are obtained by taking Table [\[tab:C412\_even\]](#tab:C412_even){reference-type="ref" reference="tab:C412_even"} for $e=0$ or Table [\[tab:C412\_odd\]](#tab:C412_odd){reference-type="ref" reference="tab:C412_odd"} for $e=1$, and subtracting $h$ from every listed coordinate. At overlapping parameters take the union, counting a coincident cycle only once. All exact periods are in $\{1,2,3,4\}$, and there are at most eight rational periodic points. Equality holds exactly when $e=1$ and $D=-4$.

\@L.18L.39L.34@ Parameter $D$ & Coordinate words of $H_{D,0}$ & Exact period and range\
$1-k^2$ & $(1-k)$, $(1+k)$ & $1$; $k\ge0$; coincide at $k=0$\
$-k^2-3$ & $(-k-1,k-1)$ & $2$; $k\ge1$\
$-k^2-1$ & $(-k-1,k,k)$, $(k-1,-k,-k)$ & $3$; $k\ge0$; coincide at $k=0$\
$-k^2$ & $(-k,-k,k,k)$ & $4$; $k\ge1$\

\@L.23L.37L.30@ Parameter $D$ & Coordinate words of $H_{D,1}$ & Exact period and range\
$-k(k+1)$ & $(-k)$, $(k+1)$ & $1$; $k\ge0$; always distinct\
$-k(k+1)-4$ & $(-k-2,k-1)$ & $2$; $k\ge0$\
$-k(k+1)-2$ & $(-k-2,k,k)$ & $3$; $k\ge0$\
$-k(k+1)-2$ & $(k-1,-k-1,-k-1)$ & $3$; $k\ge1$\
$-k(k+1)-1$ & $(-k-1,-k-1,k,k)$ & $4$; $k\ge0$\

The translation underlying this statement is $(x,y)\mapsto(x+h,y+h)$, which sends $H_{\alpha,\beta}$ to $H_{D,e}$ by direct substitution. For the even branch of Theorem [\[thm:whole\_class\]](#thm:whole_class){reference-type="ref" reference="thm:whole_class"} use $\alpha=\kappa r$, $\beta=n-\kappa$ and [\[eq:C412\_parameter\]](#eq:C412_parameter){reference-type="eqref" reference="eq:C412_parameter"}. A displayed coordinate $w$ then corresponds to the original coordinate $$x=\frac{w-h}{\kappa}.
 \label{eq:even_recovery}$$ All small-index clauses in the imported tables remain necessary after this affine recovery. They should not be confused with Table [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"}, where both three-cycles have exact period three even at $k=0$.

# The finite certificate in reproducible form {#app:certificate}

## Executed mathematical producer

The following listing is included directly from the byte-identical executed producer, rather than rewritten as a new implementation. It contains canonical rotation, the exact transition, word verification, parametric-family generation, exhaustive pruning, cycle extraction, and the complete per-parameter output construction. The omitted outer wrapper calls `certificate(a)` for `a in range(-145, 2)` and serializes those records with metadata and the aggregate summary; the entire wrapper remains in .

``` {.python firstline="4" lastline="132"}
import argparse
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import sys


def canonical(word):
    word = tuple(word)
    return min(word[i:] + word[:i] for i in range(len(word)))


def step_z(point, parameter):
    z, w = point
    numerator = w * w + 8 * parameter + 7
    assert z % 2 == w % 2 == 1
    assert numerator % 8 == 0
    result = (w, numerator // 4 - z)
    assert result[0] % 2 == result[1] % 2 == 1
    return result


def states_z(word):
    return {
        (2 * word[i] + 1, 2 * word[(i + 1) % len(word)] + 1)
        for i in range(len(word))
    }


def verify_word(word, parameter):
    length = len(word)
    assert length > 0
    assert len(states_z(word)) == length, "nonprimitive state word"
    for i, value in enumerate(word):
        assert value * (value + 1) % 2 == 0
        assert (
            word[i - 1] + word[(i + 1) % length]
            == value * (value + 1) // 2 + parameter
        )


def symbolic_words(parameter):
    result = {}
    k = 0
    while k * (k + 1) // 2 <= 1 - parameter:
        triangular = k * (k + 1) // 2
        choices = [
            (1 - triangular, (1 - k,), "fixed_lower", k),
            (1 - triangular, (k + 2,), "fixed_upper", k),
            (-1 - triangular, (-k - 1, -k - 1, k, k), "period_four", k),
            (-3 - triangular, (-k - 3, k, k), "period_three_upper", k),
            (-3 - triangular, (k - 2, -k - 1, -k - 1), "period_three_lower", k),
            (-7 - triangular, (-k - 3, k - 2), "period_two", k),
        ]
        for value, word, label, index in choices:
            if value == parameter:
                verify_word(word, parameter)
                result.setdefault(canonical(word), []).append(
                    {"family": label, "k": index}
                )
        k += 1
    return result


def certificate(parameter):
    bound = 4 + isqrt(9 - 8 * parameter)
    alphabet = tuple(
        z for z in range(-bound, bound + 1)
        if z % 2 == 1 and abs(z * z + 8 * parameter + 7) <= 8 * bound
    )
    current = {(z, w) for z in alphabet for w in alphabet}
    sizes = [len(current)]
    while True:
        following = {point for point in current if step_z(point, parameter) in current}
        if following == current:
            break
        assert len(following) < len(current)
        current = following
        sizes.append(len(current))
    assert {step_z(point, parameter) for point in current} == current

    visited = set()
    words = []
    for start in sorted(current):
        if start in visited:
            continue
        local_seen = set()
        orbit = []
        point = start
        while point not in local_seen:
            assert point in current and point not in visited
            local_seen.add(point)
            orbit.append(point)
            point = step_z(point, parameter)
        assert point == start
        visited.update(local_seen)
        word = canonical(tuple((point[0] - 1) // 2 for point in orbit))
        verify_word(word, parameter)
        assert states_z(word) == local_seen
        words.append(word)
    assert visited == current
    assert len(words) == len(set(words))
    words.sort()
    symbolic = symbolic_words(parameter)
    assert set(symbolic).issubset(words), "missing proved symbolic family"
    covered = set()
    for word in words:
        assert not covered.intersection(states_z(word))
        covered.update(states_z(word))
    assert covered == current

    cycles = [
        {"word": word, "least_period": len(word), "symbolic_families": symbolic.get(word, [])}
        for word in words
    ]
    return {
        "a": parameter,
        "doubled_coordinate_bound": bound,
        "doubled_coordinate_alphabet": alphabet,
        "strict_pruning_sizes": sizes,
        "stable_next_step_equal": True,
        "periodic_points": len(current),
        "oriented_cycles": len(cycles),
        "least_period_cycle_counts": dict(sorted(Counter(map(len, words)).items())),
        "cycles": cycles,
    }
```

The code divides only quantities already proved to be integral. The predicate $$\texttt{len(states\_z(word)) == length}$$ establishes that all states before the first return are distinct; coupled with the verified recurrence, it certifies exact period. The union equality `covered == current` certifies that no stable state is omitted from the reported cycles. The family generator is bounded by the largest possible triangular argument $1-a$; its role is comparison to proved families, not the exhaustion of the state graph.

## Independent mathematical checker

The second listing is the mathematical core of the separately implemented checker. Its box completeness and functional-graph logic were proved in Section [6](#sec:finite){reference-type="ref" reference="sec:finite"}. The full source subsequently computes all 147 graphs, loads the author result only after that computation, and compares every oriented word and expanded state set, with individual period labels and aggregate fields checked as well.

``` {.python firstline="4" lastline="86"}
import argparse
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import sys


BOUND = 19
PARAMETERS = tuple(range(-145, 2))


def original_step(point, a):
    x, y = point
    return (y, y * (y + 1) // 2 + a - x)


def rotation_minimum(word):
    return min(tuple(word[j:] + word[:j]) for j in range(len(word)))


def states_of(word):
    return {(word[j], word[(j + 1) % len(word)]) for j in range(len(word))}


def verify_cycle(word, a):
    states = states_of(word)
    if not word or len(states) != len(word):
        raise AssertionError((a, "nonprimitive cycle", word))
    for j in range(len(word)):
        expected = (word[(j + 1) % len(word)], word[(j + 2) % len(word)])
        if original_step((word[j], word[(j + 1) % len(word)]), a) != expected:
            raise AssertionError((a, "wrong recurrence", word, j))
    return states


def independent_graph(a):
    vertices = tuple((x, y) for x in range(-BOUND, BOUND + 1)
                     for y in range(-BOUND, BOUND + 1))
    vertex_set = set(vertices)
    successor = {v: original_step(v, a) for v in vertices}
    completed = set()
    cycles = []
    cycle_states = set()
    traversed = 0
    for start in vertices:
        if start in completed:
            continue
        path = []
        position = {}
        point = start
        while point in vertex_set and point not in completed and point not in position:
            position[point] = len(path)
            path.append(point)
            traversed += 1
            point = successor[point]
        if point in position:
            cycle = path[position[point]:]
            word = rotation_minimum([v[0] for v in cycle])
            expanded = verify_cycle(word, a)
            if expanded != set(cycle) or expanded.intersection(cycle_states):
                raise AssertionError((a, "cycle extraction mismatch"))
            cycle_states.update(expanded)
            cycles.append(word)
        completed.update(path)
    if completed != vertex_set or traversed != len(vertices):
        raise AssertionError((a, "functional graph not completely processed"))
    if len(cycles) != len(set(cycles)):
        raise AssertionError((a, "duplicate oriented cycle"))
    if {successor[v] for v in cycle_states} != cycle_states:
        raise AssertionError((a, "periodic set is not invariant"))
    return {
        "a": a,
        "original_coordinate_bound": BOUND,
        "graph_vertex_count": len(vertices),
        "vertices_processed_once": traversed,
        "out_of_box_edges": sum(v not in vertex_set for v in successor.values()),
        "oriented_cycle_words": sorted(cycles),
        "least_period_histogram": dict(sorted(Counter(map(len, cycles)).items())),
        "periodic_points": len(cycle_states),
        "periodic_states": sorted(cycle_states),
    }
```

## The complete per-parameter receipt

Table [2](#tab:residual){reference-type="ref" reference="tab:residual"} is a direct formatting of stored fields of ; it does not execute either mathematical program. The columns are the parameter $a$, bound $B_a$, alphabet size $|S_a|$, number $j$ of strict pruning decreases, number $p_a$ of periodic points, and multiset of cycle lengths. The notation $d^{[c]}$ means $c$ distinct cycles of length $d$, not a point count; a dash means no cycle. Every row has an independent full cycle-and-state match. Complete alphabets, every pruning cardinality, and actual words are present in the unabridged exact output. The four universal families and all unmatched words are printed in Tables [\[tab:families\]](#tab:families){reference-type="ref" reference="tab:families"} and [1](#tab:exceptions){reference-type="ref" reference="tab:exceptions"}.

::: {#tab:residual}
                                     $a$   $B_a$   $|S_a|$   $j$   $p_a$ Cycle lengths
  -------------------------------------- ------- --------- ----- ------- ---------------

                                     $a$   $B_a$   $|S_a|$   $j$   $p_a$ Cycle lengths

    -145 & 38 & 8 & 1 & 0 & $\text{---}$

  : All 147 residual/control parameter records, with no period cutoff. The unique maximum $p_a=17$ occurs at $a=-1$.
:::

## Artifact identity and actual execution history

The author program executed once on 2026-09-08 at 14:25:24 UTC, using Python 3.12.3 and the standard library only. The independent program executed once on the same date at 14:32:39 UTC. Both runs succeeded; the original records report no failed attempt or retry. Typesetting and read-only hash checks are not additional mathematical executions.

The following SHA-256 values identify the exact finite proof inputs supplied with the manuscript. Line breaks inside hashes are for display only.

Author producer.

:   \
    `f80ffcf177fd7a8e98b8ea4d3112b7cca5e`\
    `f986b5725025e70c836aa088132a0`.

Author output.

:   \
    `44ccf0f5d062587eb07d2837c455a9c3843`\
    `c3ce0b9e0c8df033d2223d227196a`.

Independent checker.

:   \
    `b5953b44db6042a81cff542972566499f02a`\
    `ff698ffc1048966e25e0b43cb29b`.

Independent output.

:   \
    `17561a62401766018f68baf75e3439d33f0`\
    `4e6cba7c5c6f5c398e5263618e842`.

The full input inventory, source locations, and current file hashes are retained in and . These establish provenance and permit byte verification; hashes are not a substitute for the mathematical arguments or for examining the code and results.
