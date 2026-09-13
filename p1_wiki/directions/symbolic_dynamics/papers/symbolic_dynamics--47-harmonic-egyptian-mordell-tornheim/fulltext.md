---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--47-harmonic-egyptian-mordell-tornheim"
canonical_tex: "symbolic_dynamics/papers/47-harmonic-egyptian-mordell-tornheim/main.tex"
canonical_pdf: "symbolic_dynamics/papers/47-harmonic-egyptian-mordell-tornheim/main.pdf"
source_sha256: "b8390c79134e9c9825faae7447bc013a006b91a4459218c3ed70ac484fc281be"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Harmonic-Quotient Graph Operator: Sharp Ideal Thresholds and a Mordell--Tornheim Trace

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/47-harmonic-egyptian-mordell-tornheim>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/47-harmonic-egyptian-mordell-tornheim/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/47-harmonic-egyptian-mordell-tornheim/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/47-harmonic-egyptian-mordell-tornheim/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/47-harmonic-egyptian-mordell-tornheim/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let the positive integers be the vertices of a looped graph in which $m$ and $n$ are adjacent exactly when $m+n$ divides $mn$, and weight an ordered edge by $(mn)^{-s/2}$ using the real logarithm. We prove that the resulting coefficient array defines a bounded, necessarily compact, operator on $\ell^2(\mathbb N)$ exactly for $\Re s>0$. Its sharp Hilbert--Schmidt and trace-class domains are $\Re s>1/2$ and $\Re s>1$. Every ordered edge has unique coordinates $m=t a(a+b)$, $n=t b(a+b)$ with $(a,b)=1$, while the neighbors in each fixed row are parametrized by $d\mid m^2$, $d<m$, through $n=m^2/d-m$. These two descriptions expose different parts of the proof. The even loops give, in the trace-class domain, $\operatorname{Tr}E_s=2^{-s}\zeta(s)$. In the larger Hilbert--Schmidt domain the ordered-edge ledger gives $$\operatorname{Tr}(E_s^2)
    =\frac{\zeta(2s)}{\zeta(4s)}\,
      \zeta_{\mathrm{MT}}(s,s;2s),$$ with absolute convergence and no factor of two. Consequently, $[z^2]\log\det_2(I-zE_s)=-\mathop{\mathrm{Tr}}(E_s^2)/2$ locally, so the displayed Mordell--Tornheim series supplies the quadratic trace term. An exact mixed triangle and a negative principal minor rule out scale-fiber and positivity simplifications. Finally, two independent finite implementations agree at four complete cutoffs; those exact checks are reported only as implementation replay, not as evidence for an infinite endpoint or for priority.
author:
- Anonymous
bibliography:
- references.bib
title: |
  The Harmonic-Quotient Graph Operator:\
  Sharp Ideal Thresholds and a Mordell--Tornheim Trace
```

## Markdown 正文

# Introduction {#sec:introduction}

The divisibility relation $$m+n\mid mn
  \qquad\Longleftrightarrow\qquad
  \frac1m+\frac1n=\frac1k\quad\text{for some }k\in\mathbb{N}
  \label{eq:harmonic-relation}$$ is elementary, but its weighted adjacency has two rather different analytic faces. Viewed one row at a time, the neighbors of $m$ are indexed by proper divisors of $m^2$; this makes decay at infinity visible. Viewed globally, every ordered edge separates into a scale and a coprime ordered pair; this converts ideal norms and traces into Dirichlet series. Keeping the loops is decisive: they locate two sharp ideal walls and supply a Riemann-zeta first trace. The same operator has a coprime Mordell--Tornheim series as its second trace.

Our object is the coefficient array $$e_s(m,n)=\mathbf{1}_{\{m+n\mid mn\}}(mn)^{-s/2},
  \qquad m,n\in\mathbb{N},
  \label{eq:coefficient-array-intro}$$ where complex powers use the real logarithm and $\sigma=\mathop{\mathrm{Re}}s$. We reserve the operator notation $E_s$ for parameters at which this array actually defines a bounded operator on $\ell^2(\mathbb{N})$. This distinction is not cosmetic: the sharp boundedness wall is $\sigma=0$.

The main results are the following.

-   Every ordered edge has the unique representation $$m=t a(a+b),\qquad n=t b(a+b),\qquad
        t\geq1,\quad (a,b)=1,$$ and every neighbor in row $m$ is independently represented by $d\mid m^2$, $d<m$, through $n=m^2/d-m$. These coordinates prove that $E_s$ is bounded and compact exactly for $\sigma>0$, belongs to $\mathcal{S}_{2}$ exactly for $\sigma>1/2$, and belongs to $\mathcal{S}_{1}$ exactly for $\sigma>1$.

-   In their legal trace domains, $$\begin{aligned}
        \mathop{\mathrm{Tr}}(E_s)&=2^{-s}\zeta(s), && \sigma>1,
          \label{eq:intro-first-trace}\\
        \mathop{\mathrm{Tr}}(E_s^2)&=\zeta(2s)P(s)
          =\frac{\zeta(2s)}{\zeta(4s)}\zeta_{\mathrm{MT}}(s,s;2s),
          && \sigma>\tfrac12,
          \label{eq:intro-second-trace}
      \end{aligned}$$ where $$P(s)=\sum_{\substack{a,b\geq1\\(a,b)=1}}
           a^{-s}b^{-s}(a+b)^{-2s}.$$ The second formula sums ordered edges, so there is no additional factor of two. It is also the exact quadratic trace term in the local logarithm of the Hilbert--Carleman determinant.

-   The triangle $15$--$30$--$60$ has three different harmonic quotients $10,20,12$. For real $s>1$, the principal block on $\{3,6\}$ has determinant $-18^{-s}$; hence in the real trace-class regime the operator need not be positive semidefinite. The global coprime coordinate therefore neither splits the graph into isolated scale fibers nor forces positivity.

The proof uses the two coordinates for complementary purposes. Divisor rows yield a Schur estimate that tends to zero and hence compactness. The coprime--scale coordinate makes the Hilbert--Schmidt sum, absolute entry sum, and ordered-edge trace exact. Even loops and squarefree rows then show that none of the three endpoints can be included. For nonreal $s$, the phase is removed only by left and right unitary multiplication; this preserves singular values but is not a unitary conjugacy and therefore is not used to transfer spectra or traces.

We keep three kinds of support separate throughout. Infinite-dimensional statements are proved analytically. Exact finite computation checks that a direct divisibility implementation and a parameter implementation agree. Artifact and mutation checks concern provenance and reproducibility. In particular, finite agreement is not offered as evidence for an endpoint, for analytic continuation, or for priority. The relation in [\[eq:harmonic-relation\]](#eq:harmonic-relation){reference-type="ref" reference="eq:harmonic-relation"}, the associated Egyptian-fraction algebra, and classical Mordell--Tornheim identities remain prior-owned background.

fixes those ownership boundaries. defines the graph and proves both coordinates. establish the phase diagram. proves the two traces and the legal determinant consequences. treats temporal typing and sign, and [8](#sec:replay){reference-type="ref" reference="sec:replay"} reports the finite replay and limitations.

# Related work and ownership boundaries {#sec:related-work}

For parameters in an absolute-convergence domain, write the depth-two Mordell--Tornheim function as $$\zeta_{\mathrm{MT}}(p,q;r)
  =\sum_{u,v\geq1}u^{-p}v^{-q}(u+v)^{-r}.
  \label{eq:mt-definition}$$ Harmonic double series were studied by Tornheim [@Tornheim1950], and Mordell's work on multiple series is part of the foundational ownership of the family that now bears both names [@Mordell1958]. Later results relate positive-integer Mordell--Tornheim sums to multiple zeta values [@BradleyZhou2012] and develop functional relations with the Riemann zeta function [@Tsumura2007]. We use none of those identities to prove an operator threshold. Their role here is to identify [\[eq:mt-definition\]](#eq:mt-definition){reference-type="eqref" reference="eq:mt-definition"} as a classical comparator after it has appeared from an ordered-edge trace.

There are also other geometric realizations of primitive Mordell--Tornheim-type series. In particular, the tropical boundary construction of @KalininLupercioShkolnikov2026 contains a distinct exponent pattern $(s,s;s)$. The series in the present graph trace has pattern $(s,s;2s)$ and arises from the product $mn$ along a two-step closed walk. We mention the comparison to prevent an ownership ambiguity, not to claim precedence over other realizations.

For Schatten ideals, traces, and regularized determinants we use the standard framework in @Simon2005. The cited theory supplies, for example, that the product of two Hilbert--Schmidt operators is trace class and that $\det_2(I-zA)$ is defined for $A\in\mathcal{S}_{2}$. It does not supply any graph-specific estimate in this paper: the walls $0$, $1/2$, and $1$, the two trace formulas, and all endpoint obstructions are established below from the arithmetic support.

The appropriate scope is therefore narrow. We analyze one frozen, looped graph; one standard-basis adjacency; the weight $(mn)^{-s/2}$; and one marker per edge when determinants are discussed. We make no priority claim for Egyptian fractions, the coprime parameterization, gcd extraction, or Mordell--Tornheim identities. A bounded literature search can support only a bounded-search statement, so it is not elevated here into a novelty theorem. Nor do we infer a completed zeta factor, a functional equation, or a Hilbert--Pólya operator from the occurrence of $\zeta$ in the first two traces.

# The harmonic graph and two exact edge coordinates {#sec:graph-coordinates}

Let $\mathcal G$ be the undirected graph with vertex set $\mathbb{N}$ and with an edge, including a possible loop, whenever $m+n\mid mn$. We distinguish an *ordered edge* $(m,n)$ from the underlying undirected edge. The one-sided edge shift is $$\Sigma_{\mathcal G}
  =\{(x_j)_{j\geq0}\in\mathbb{N}^{\mathbb{N}_0}:x_j+x_{j+1}\mid x_jx_{j+1}
      \text{ for every }j\}.$$ Time advances once per edge. Thus a based closed word of length $r$ is $(v_0,\ldots,v_{r-1},v_r)$ with $v_r=v_0$ and $r$ legal edges; its least temporal period is a property of this word, not of an arithmetic coordinate on one edge. Later, $z$ marks this one-edge clock.

For every $s\in\mathbb{C}$ define the formal coefficient array $$e_s(m,n)=\mathbf{1}_{\{m+n\mid mn\}}
 \exp\!(-\frac{s}{2}(\log m+\log n)).
 \label{eq:coefficient-array}$$ When the array induces a bounded operator on $\ell^2(\mathbb{N})$, we denote that operator by $E_s$. Let $P_N$ be the orthogonal projection onto $\operatorname{span}\{e_1,\ldots,e_N\}$ and put $Q_N=I-P_N$.

The complete analytic statement is collected here so that every later formula can point back to a legal domain.

[\[thm:main\]]{#thm:main label="thm:main"} Let $s=\sigma+i\tau$.

1.  The array [\[eq:coefficient-array\]](#eq:coefficient-array){reference-type="eqref" reference="eq:coefficient-array"} defines a bounded operator, and that operator is compact, if and only if $\sigma>0$.

2.  In the bounded domain, $E_s\in\mathcal{S}_{2}$ if and only if $\sigma>1/2$, and $E_s\in\mathcal{S}_{1}$ if and only if $\sigma>1$.

3.  For $\sigma>1$, $\mathop{\mathrm{Tr}}(E_s)=2^{-s}\zeta(s)$. For $\sigma>1/2$, $$\mathop{\mathrm{Tr}}(E_s^2)=\zeta(2s)P(s)
          =\frac{\zeta(2s)}{\zeta(4s)}\zeta_{\mathrm{MT}}(s,s;2s).$$ Every displayed series is absolutely convergent in the stated domain.

All three endpoint inequalities are strict.

## The coprime--scale coordinate

The global coordinate is the source of every Dirichlet-series factor in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

[\[prop:coprime-coordinate\]]{#prop:coprime-coordinate label="prop:coprime-coordinate"} The map $$(t,a,b)\longmapsto
 (t a(a+b),\,t b(a+b))
 \label{eq:coprime-map}$$ is a bijection from $t\in\mathbb{N}$ and coprime ordered pairs $(a,b)\in\mathbb{N}^2$ to the ordered edges of $\mathcal G$. The harmonic quotient is $k=tab$.

Given an edge, let $g=(m,n)$ and write $m=ga$, $n=gb$ with $(a,b)=1$. The divisibility condition becomes $a+b\mid gab$. Since $(a+b,ab)=1$, it is equivalent to $a+b\mid g$; writing $g=t(a+b)$ gives [\[eq:coprime-map\]](#eq:coprime-map){reference-type="eqref" reference="eq:coprime-map"}. The gcd recovers $g$, then $a,b$, and finally $t$, so the representation is unique. Conversely, substitution in [\[eq:harmonic-relation\]](#eq:harmonic-relation){reference-type="eqref" reference="eq:harmonic-relation"} gives $$\frac1{t a(a+b)}+\frac1{t b(a+b)}=\frac1{tab},$$ which proves legality and the formula for $k$.

The pair $(a,b)$ is primitive only in the gcd-one sense. It contains no information about whether an edge belongs to a closed word of least period $r$.

## The divisor-row coordinate

The second coordinate keeps $m$ fixed and has no coprimality condition.

[\[prop:divisor-row\]]{#prop:divisor-row label="prop:divisor-row"} For fixed $m$, the map $$d\longmapsto n=\frac{m^2}{d}-m
 \label{eq:divisor-map}$$ is a bijection from divisors $d\mid m^2$ with $d<m$ onto the neighbors of $m$. If $k=mn/(m+n)$, then $d=m-k$.

For an edge, $k=mn/(m+n)$ is a positive integer and $$d=m-k=\frac{m^2}{m+n}.$$ Hence $d\mid m^2$, $d<m$, and solving for $n$ gives [\[eq:divisor-map\]](#eq:divisor-map){reference-type="eqref" reference="eq:divisor-map"}. Conversely, a divisor $d<m$ makes the right-hand side of [\[eq:divisor-map\]](#eq:divisor-map){reference-type="eqref" reference="eq:divisor-map"} a positive integer and gives $m+n=m^2/d$ and $mn/(m+n)=m-d\in\mathbb{N}$. Both constructions recover $d$, so they are inverse.

The loops are now visible in either coordinate. Setting $m=n$ in the edge condition gives $2m\mid m^2$, so a loop occurs exactly at $m=2t$. Equivalently, it has $(a,b)=(1,1)$ in [\[prop:coprime-coordinate\]](#prop:coprime-coordinate){reference-type="ref" reference="prop:coprime-coordinate"}.

\@lYY@ Object & Definition & Type / role\
vertex & $m\in\mathbb{N}$ & graph state\
harmonic quotient & $k=mn/(m+n)$ & integer attached to one edge\
edge coordinate & $(t,a,b)$ with $(a,b)=1$ & unique global edge data\
row coordinate & $d\mid m^2$, $d<m$ & unique data after fixing $m$\
closed word & $(v_0,\ldots,v_r)$, $v_r=v_0$ & temporal object of length $r$\
marker & $z$ & one factor per traversed edge\

## The complex phase firewall

Let $U_\tau e_n=n^{-i\tau/2}e_n$. This is a diagonal unitary. Entrywise, and first on every finite compression, $$e_s=U_\tau e_\sigma U_\tau.
 \label{eq:left-right-factorization}$$ Once boundedness has been proved for $\sigma>0$, equality passes to the operators: $$E_s=U_\tau E_\sigma U_\tau.
 \label{eq:operator-left-right}$$ Left and right multiplication by unitaries preserves singular values, operator norm, compactness, Schatten membership, and Schatten norms. Equation [\[eq:operator-left-right\]](#eq:operator-left-right){reference-type="eqref" reference="eq:operator-left-right"} is *not* unitary conjugacy: the right factor is $U_\tau$, not $U_\tau^*$. It therefore transfers none of the spectrum, powers, traces, positivity, or determinants. All trace and determinant identities below are proved directly for the complex matrix in their stated ideal domains.

# Boundedness and compactness {#sec:bounded-compact}

The divisor coordinate turns the absolute row sum into an exact finite expression. Indeed, from $n=m(m-d)/d$ in [\[eq:divisor-map\]](#eq:divisor-map){reference-type="eqref" reference="eq:divisor-map"}, $$R_m(\sigma):=\sum_{n\geq1}|e_s(m,n)|
 =m^{-\sigma}
  \sum_{\substack{d\mid m^2\\d<m}}
  (\frac{d}{m-d})^{\sigma/2}.
 \label{eq:exact-row-sum}$$ Only $\sigma$ occurs on the right.

[\[prop:vanishing-rows\]]{#prop:vanishing-rows label="prop:vanishing-rows"} For every $\sigma>0$, $$R_m(\sigma)
 \ll_\sigma \tau(m^2)
 (m^{-\sigma}+m^{-3\sigma/4})=o(1).
 \label{eq:row-decay}$$

Split the divisors in [\[eq:exact-row-sum\]](#eq:exact-row-sum){reference-type="eqref" reference="eq:exact-row-sum"} at $m/2$. If $d\leq m/2$, then $d/(m-d)\leq1$, so the total contribution is at most $m^{-\sigma}\tau(m^2)$.

If $d>m/2$, put $e=m-d$. The relations $d\mid m^2$ and $m=d+e$ imply $d\mid e^2$. Since $d>m/2$, this gives $e\geq(m/2)^{1/2}$. Also $d<m$, and hence each term in this part satisfies $$m^{-\sigma}(\frac d e)^{\sigma/2}
 \leq m^{-\sigma/2}e^{-\sigma/2}
 \leq 2^{\sigma/4}m^{-3\sigma/4}.$$ There are at most $\tau(m^2)$ terms. This proves the bound in [\[eq:row-decay\]](#eq:row-decay){reference-type="eqref" reference="eq:row-decay"}; the conclusion follows from the standard estimate $\tau(n)=n^{o(1)}$.

Suppose first that $\sigma>0$. The finitely many initial values together with [\[prop:vanishing-rows\]](#prop:vanishing-rows){reference-type="ref" reference="prop:vanishing-rows"} give $\sup_m R_m(\sigma)<\infty$. Because the absolute coefficient matrix is symmetric, the Schur test proves that [\[eq:coefficient-array\]](#eq:coefficient-array){reference-type="eqref" reference="eq:coefficient-array"} induces a bounded operator.

For compactness, write $P_M=P_{\{1,\ldots,M\}}$ and $Q_M=I-P_M$. The same symmetric Schur test applied to the tail block gives $$\|Q_M E_s Q_M\|
 \leq \sup_{m>M}R_m(\sigma)\longrightarrow0.
 \label{eq:tail-schur}$$ On the other hand, $E_s-Q_M E_sQ_M=P_M E_s+Q_M E_sP_M$ is finite rank. Thus $E_s$ is a norm limit of finite-rank operators and is compact. Since $P_N\to I$ strongly, the standard compact-operator approximation then yields the concrete compression statement $$\|E_s-P_NE_sP_N\|\longrightarrow0.
 \label{eq:compression-convergence}$$

Now let $\sigma<0$. At every even vertex $m$ there is a loop and its diagonal coefficient has modulus $m^{-\sigma}$, which is unbounded along the even integers. No bounded operator can have such diagonal matrix coefficients.

It remains to treat $\sigma=0$. Every nonzero coefficient then has modulus one. By [\[prop:divisor-row\]](#prop:divisor-row){reference-type="ref" reference="prop:divisor-row"}, the squared $\ell^2$ norm of row $m$ is the number of divisors $d\mid m^2$ below $m$. Divisor pairs about the central divisor $m$ give $$\deg(m)=\frac{\tau(m^2)-1}{2}.
 \label{eq:degree-formula}$$ For squarefree $m$, this is $(3^{\omega(m)}-1)/2$, which is unbounded as the number of prime factors grows. The row norms of a bounded operator would be uniformly bounded by its operator norm, a contradiction. This proves both necessity and the strict endpoint.

The proof is analytic at every stage. In particular, [\[eq:compression-convergence\]](#eq:compression-convergence){reference-type="eqref" reference="eq:compression-convergence"} follows from the tail estimate and compactness; observing stable singular values in a finite grid would not prove it.

# Sharp Hilbert--Schmidt and trace-class thresholds {#sec:ideal-thresholds}

The global edge coordinate now separates the scale $t$ from the coprime shape $(a,b)$. Since $$mn=t^2ab(a+b)^2,$$ the squared Hilbert--Schmidt norm, whenever finite, is $$\|E_s\|_2^2
 =\zeta(2\sigma)
  \sum_{\substack{a,b\geq1\\(a,b)=1}}
  [ab(a+b)^2]^{-\sigma}.
 \label{eq:hs-exact}$$

[\[prop:hs-wall\]]{#prop:hs-wall label="prop:hs-wall"} The operator $E_s$ belongs to $\mathcal{S}_{2}$ if and only if $\sigma>1/2$.

If $\sigma\leq1/2$, the diagonal terms from the loops $m=n=2t$ already give the divergent subseries $\sum_{t\geq1}(2t)^{-2\sigma}$ in the squared Hilbert--Schmidt sum.

If $\sigma>1/2$, the arithmetic--geometric mean inequality gives $(a+b)^2\geq4ab$, and consequently $$^{-\sigma}
 \leq4^{-\sigma}a^{-2\sigma}b^{-2\sigma}.
 \label{eq:hs-majorant}$$ After dropping the coprimality restriction, the double majorant is $4^{-\sigma}\zeta(2\sigma)^2<\infty$. The scale factor in [\[eq:hs-exact\]](#eq:hs-exact){reference-type="eqref" reference="eq:hs-exact"} is finite as well. This proves sufficiency and the strict endpoint.

Trace class requires a different power of the scale variable. Absolute summability of the entries is sufficient, and the coprime coordinate gives $$\begin{aligned}
 \sum_{m,n\geq1}|e_s(m,n)|
 &=\zeta(\sigma)
  \sum_{\substack{a,b\geq1\\(a,b)=1}}
  [ab(a+b)^2]^{-\sigma/2} \\
 &\leq 2^{-\sigma}\zeta(\sigma)^3,
 \label{eq:absolute-entry-bound}\end{aligned}$$ where the last line again uses $(a+b)^2\geq4ab$ and drops coprimality.

[\[prop:trace-wall\]]{#prop:trace-wall label="prop:trace-wall"} The operator $E_s$ belongs to $\mathcal{S}_{1}$ if and only if $\sigma>1$.

For $\sigma>1$, [\[eq:absolute-entry-bound\]](#eq:absolute-entry-bound){reference-type="eqref" reference="eq:absolute-entry-bound"} is finite. Expanding the matrix as a sum of rank-one matrix units shows $\|E_s\|_1\leq\sum_{m,n}|e_s(m,n)|$, so $E_s$ is trace class.

Conversely, for every trace-class operator $T$ and every orthonormal basis, $\sum_m|\langle Te_m,e_m\rangle|\leq\|T\|_1$. The loops of $\mathcal G$ are exactly the even vertices, hence a hypothetical trace-class $E_s$ would satisfy $$\sum_{m\geq1}|\langle E_se_m,e_m\rangle|
 =\sum_{t\geq1}(2t)^{-\sigma}<\infty.
 \label{eq:diagonal-obstruction}$$ The series diverges for $\sigma\leq1$. Together with the boundedness wall from [4](#sec:bounded-compact){reference-type="ref" reference="sec:bounded-compact"}, this proves necessity for every parameter.

::: {#tab:phase}
  Property              Exact domain       Decisive boundary witness
  --------------------- ------------------ ------------------------------
  Bounded and compact   $\Re s>0$          even loops / squarefree rows
  Hilbert--Schmidt      $\Re s>\tfrac12$   even-loop scale sum
  Trace class           $\Re s>1$          absolute even diagonal
  $\det_2(I-zE_s)$      $\Re s>\tfrac12$   Hilbert--Schmidt wall
  $\det(I-zE_s)$        $\Re s>1$          trace-class wall

  : Sharp operator-ideal and determinant domains. Every endpoint is strict; the witnesses in the last column are analytic proof ingredients, not finite-cutoff diagnostics.
:::

The proofs also explain why the walls cannot be interchanged. At $\sigma=0$ the obstruction is unbounded row degree; at $\sigma=1/2$ it is the squared loop scale; and at $\sigma=1$ it is the absolute diagonal. Hilbert--Schmidt membership in the strip $1/2<\sigma\leq1$ never licenses an ordinary Fredholm determinant.

# Zeta and Mordell--Tornheim traces {#sec:traces-determinants}

Define the coprime double series $$P(s)=\sum_{\substack{a,b\geq1\\(a,b)=1}}
 a^{-s}b^{-s}(a+b)^{-2s}.
 \label{eq:primitive-P}$$ The majorant in [\[eq:hs-majorant\]](#eq:hs-majorant){reference-type="eqref" reference="eq:hs-majorant"} shows that it converges absolutely for $\sigma>1/2$. We first compute traces only where operator ideals make them legal; analytic continuation plays no role.

[\[thm:two-traces\]]{#thm:two-traces label="thm:two-traces"} For $\sigma>1$, $$\mathop{\mathrm{Tr}}(E_s)=2^{-s}\zeta(s).
 \label{eq:first-trace}$$ For $\sigma>1/2$, $$\mathop{\mathrm{Tr}}(E_s^2)=\zeta(2s)P(s)
 =\frac{\zeta(2s)}{\zeta(4s)}\zeta_{\mathrm{MT}}(s,s;2s).
 \label{eq:second-trace}$$ Both statements are identities of absolutely convergent series in the displayed domains.

If $\sigma>1$, [\[prop:trace-wall\]](#prop:trace-wall){reference-type="ref" reference="prop:trace-wall"} makes $E_s$ trace class, so its trace is the absolutely convergent standard-basis diagonal sum. The loops are exactly $m=2t$, and therefore $$\mathop{\mathrm{Tr}}(E_s)=\sum_{t\geq1}(2t)^{-s}=2^{-s}\zeta(s).$$

Now suppose $\sigma>1/2$. By [\[prop:hs-wall\]](#prop:hs-wall){reference-type="ref" reference="prop:hs-wall"}, $E_s$ is Hilbert--Schmidt, hence $E_s^2$ is trace class. Moreover, $$\sum_{m,n}|e_s(m,n)e_s(n,m)|
 =\sum_{m,n}|e_s(m,n)|^2<\infty,$$ so the trace may be evaluated term by term: $$\mathop{\mathrm{Tr}}(E_s^2)
 =\sum_{\substack{m,n\geq1\\m+n\mid mn}}(mn)^{-s}.
 \label{eq:ordered-edge-trace}$$ This is an ordered-edge sum. Applying [\[prop:coprime-coordinate\]](#prop:coprime-coordinate){reference-type="ref" reference="prop:coprime-coordinate"} and using $mn=t^2ab(a+b)^2$ gives $$\mathop{\mathrm{Tr}}(E_s^2)
 =(\sum_{t\geq1}t^{-2s})
  \sum_{\substack{a,b\geq1\\(a,b)=1}}
    a^{-s}b^{-s}(a+b)^{-2s}
 =\zeta(2s)P(s).$$ No factor of two is inserted: $(a,b)$ is already ordered.

Finally, decompose an arbitrary ordered pair $(u,v)$ uniquely as $u=ga$, $v=gb$ with $(a,b)=1$. Absolute convergence permits regrouping, and [\[eq:mt-definition\]](#eq:mt-definition){reference-type="eqref" reference="eq:mt-definition"} becomes $$\begin{aligned}
 \zeta_{\mathrm{MT}}(s,s;2s)
 &=\sum_{g\geq1}g^{-4s}
   \sum_{\substack{a,b\geq1\\(a,b)=1}}
     a^{-s}b^{-s}(a+b)^{-2s}\\
 &=\zeta(4s)P(s).\end{aligned}$$ Substitution proves the second equality in [\[eq:second-trace\]](#eq:second-trace){reference-type="eqref" reference="eq:second-trace"}.

The adjective "coprime" in $P(s)$ refers only to $(a,b)=1$. The arbitrary-pair sum $\zeta_{\mathrm{MT}}(s,s;2s)$ and the elementary gcd extraction remain classical arithmetic objects; the graph-specific statement is that the same operator whose even diagonal gives [\[eq:first-trace\]](#eq:first-trace){reference-type="eqref" reference="eq:first-trace"} has [\[eq:second-trace\]](#eq:second-trace){reference-type="eqref" reference="eq:second-trace"} as its two-step trace.

## Determinant consequences

The ideal walls determine exactly which determinant is available. We use the standard convention $$\det_2(I-zA)=\det((I-zA)e^{zA})
 \qquad(A\in\mathcal{S}_{2}).$$

[\[cor:determinants\]]{#cor:determinants label="cor:determinants"} If $\sigma>1/2$, the function $D_2(z;s)=\det_2(I-zE_s)$ is entire in $z$. On the disk $|z|\,\|E_s\|<1$, with the logarithm normalized by $\log D_2(0;s)=0$, $$\log D_2(z;s)
 =-\sum_{r\geq2}\frac{z^r}{r}\mathop{\mathrm{Tr}}(E_s^r),
 \label{eq:det2-local-log}$$ and in particular $$\log D_2(z;s)
 =-\frac12\frac{\zeta(2s)}{\zeta(4s)}
   \zeta_{\mathrm{MT}}(s,s;2s).
 \label{eq:det2-quadratic}$$ If $\sigma>1$, the ordinary determinant $D_1(z;s)=\det(I-zE_s)$ is entire in $z$ and $$\begin{aligned}
 \log D_1(z;s)&=-\sum_{r\geq1}\frac{z^r}{r}\mathop{\mathrm{Tr}}(E_s^r),
 \label{eq:det1-local-log}\\
 D_2(z;s)&=D_1(z;s)\exp\!(z\mathop{\mathrm{Tr}}(E_s))
 \label{eq:det-overlap}\end{aligned}$$ on the same sufficient local disk for the logarithm.

These are the standard Hilbert--Carleman and Fredholm determinant identities for Schatten operators [@Simon2005]. In the first domain, $E_s^r$ is trace class for every $r\geq2$ because $E_s^2$ is trace class and $E_s$ is bounded. Substituting [\[eq:second-trace\]](#eq:second-trace){reference-type="eqref" reference="eq:second-trace"} in the $r=2$ term gives [\[eq:det2-quadratic\]](#eq:det2-quadratic){reference-type="eqref" reference="eq:det2-quadratic"}. In the trace-class overlap, the definition of $\det_2$ gives [\[eq:det-overlap\]](#eq:det-overlap){reference-type="eqref" reference="eq:det-overlap"}, and [\[eq:first-trace\]](#eq:first-trace){reference-type="eqref" reference="eq:first-trace"} supplies the exponent.

Only the determinant functions are asserted globally in $z$. The logarithmic series and the chosen logarithm are local. We do not use the right side of [\[eq:second-trace\]](#eq:second-trace){reference-type="eqref" reference="eq:second-trace"} to continue a determinant past an ideal wall, and we do not claim a completed divisor or functional equation.

# Mixed cycles, temporal typing, and sign {#sec:cycles-sign}

The scale coordinate in [\[prop:coprime-coordinate\]](#prop:coprime-coordinate){reference-type="ref" reference="prop:coprime-coordinate"} is attached to one ordered edge. It does not decompose the graph into invariant scale blocks. The smallest witness needed here is the exact triangle $$15\longleftrightarrow30\longleftrightarrow60
 \longleftrightarrow15.$$ Indeed, $$\frac{15\cdot30}{15+30}=10,
 \qquad
 \frac{30\cdot60}{30+60}=20,
 \qquad
 \frac{60\cdot15}{60+15}=12.
 \label{eq:mixed-triangle}$$ The three edges lie in different arithmetic scales: their $(t,a,b)$ coordinates may be taken as $(5,1,2)$, $(10,1,2)$, and $(3,4,1)$ in the displayed orientations. Thus even a single temporal cycle mixes scale data.

This example also fixes the terminology used in determinant expansions. For a finite compression, $\mathop{\mathrm{Tr}}((P_NE_sP_N)^r)$ is the weighted sum of based closed vertex words of length $r$. The factor $1/r$ in a logarithmic determinant is cyclic base-point bookkeeping, with the usual multiplicity for repeated temporal words. It does not convert a harmonic quotient $k$, a scale $t$, or a coprime edge pair $(a,b)$ into a least-period temporal primitive. The infinite trace powers in [\[eq:det2-local-log\]](#eq:det2-local-log){reference-type="ref" reference="eq:det2-local-log"} are used only after their trace-class legality has been established.

There is an independent sign obstruction. For real $s>1$, the principal compression to vertices $3$ and $6$ is $$E_s\big|_{\{3,6\}}
 =\begin{pmatrix}
     0&18^{-s/2}\\
     18^{-s/2}&6^{-s}
   \end{pmatrix},
 \qquad
 \det\!(E_s|_{\{3,6\}})=-18^{-s}<0.
 \label{eq:negative-minor}$$ The zero occurs because $6\nmid9$, the off-diagonal entry because $9\mid18$, and the lower diagonal entry because $12\mid36$. Consequently the real symmetric trace-class operator is not positive semidefinite. When $s$ is nonreal the matrix remains complex symmetric, but it is not asserted to be Hermitian; neither positivity nor self-adjointness is imported through the left--right factorization [\[eq:operator-left-right\]](#eq:operator-left-right){reference-type="eqref" reference="eq:operator-left-right"}.

# Canonical replay, limitations, and conclusion {#sec:replay}

The analytic proof above owns every infinite-dimensional claim. As a separate implementation check, the frozen computation evaluates the same finite support in two independent ways: a direct divisibility lane and a coprime-parameter/divisor-row lane. The mechanically extracted counts are shown in [3](#tab:canonical-replay){reference-type="ref" reference="tab:canonical-replay"}. At cutoffs $N=16,32,64,128$, the complete compressions contain respectively $16,40,96,228$ ordered edges and $8,16,32,64$ loops. All twelve named comparison fields pass. Exact rational first- and second-trace projections at $s=2$ and $s=4$ also agree at $N=128$ across the authorized finite lanes.

::: {#tab:canonical-replay}
    $N$   Ordered edges   Loops
  ----- --------------- -------
     16              16       8
     32              40      16
     64              96      32
    128             228      64

  : Canonical State-A implementation replay. The counts and comparison keys are extracted from two independent finite lanes. They validate implementation agreement and make no inference about an infinite endpoint.
:::

::: {#tab:canonical-replay}
  --------------------------------- ---------------------------------
  ``                                ``

  ``                                ``

  ``                                ``

  ``                                ``

  ``                                ``

  ``                                ``
  --------------------------------- ---------------------------------

  : Canonical State-A implementation replay. The counts and comparison keys are extracted from two independent finite lanes. They validate implementation agreement and make no inference about an infinite endpoint.
:::

The qualification "finite" is essential. A cutoff has a truncated scale variable whose upper limit depends on $(a,b)$; it does not contain a common infinite $\zeta(2s)$ factor. That factor is extracted only in the absolutely convergent analytic sum in [\[thm:two-traces\]](#thm:two-traces){reference-type="ref" reference="thm:two-traces"}. Likewise, the finite matrices do not prove compactness, locate a Schatten endpoint, or authorize a determinant outside its ideal domain.

The replay is bound to a protected 91-node input/state tree and a canonical State-A result ledger. Adversarial validation covered 39 theorem/governance mutations, 35 expanded nested mutations, and 15 frozen external-auditor mutations, with no surviving mutation. Those facts support artifact integrity and reproducibility only. The separate route record is rejected and disallows invocation of its alternative route; no spectral target is smuggled into the mathematical conclusions.

Several limitations are deliberate. We treat one loop convention, one edge clock, one standard-basis weight, and the first two legal traces. We do not claim a theorem for every Schatten class, a rational-prime "primitive" ledger, a completed target divisor, a functional equation, or a fixed Hilbert--Pólya operator. The bounded literature check is not a priority theorem. Finally, complex left--right phase removal controls singular values only; it supplies no spectral equivalence.

Within that scope, the conclusion is exact. The same elementary harmonic-quotient graph has a divisor-row geometry that yields the sharp bounded/compact wall, a coprime--scale geometry that yields the sharp ideal walls, an even-loop Riemann-zeta trace, and an ordered-edge Mordell--Tornheim second trace. The mixed triangle confirms that these are features of one arithmetic operator rather than a formal sum of isolated scale fibers.

# Arithmetic details for the two coordinates {#app:arithmetic}

This appendix records several elementary points that are easy to obscure when the coordinates are used inside operator sums.

## Why the coprime representation is unique

Let $(m,n)$ be an ordered edge and set $g=(m,n)$, $a=m/g$, and $b=n/g$. Then $(a,b)=1$. If a prime $p$ divided both $a+b$ and $ab$, it would divide one of $a,b$ and then the other, a contradiction. Hence $$(a+b,ab)=1.
 \label{eq:gcd-elementary}$$ The edge condition $g(a+b)\mid g^2ab$ therefore reduces to $a+b\mid g$. The integer $t=g/(a+b)$ is forced. Conversely, the triple $(t,a,b)$ reconstructs $g=t(a+b)$ and thus $(m,n)$. This proves injectivity and surjectivity without choosing an orientation of an undirected edge; swapping the orientation swaps $a$ and $b$.

The harmonic quotient is also forced: $$\frac{mn}{m+n}
 =\frac{t^2ab(a+b)^2}{t(a+b)^2}=tab.$$ On a loop, coprimality forces $a=b=1$, so $m=n=2t$ and $k=t$.

## Exact row counts

For fixed $m$, the proper divisors $d<m$ of $m^2$ are paired with the divisors $m^2/d>m$; the only unpaired divisor is $m$. Consequently $$\#\{n:m+n\mid mn\}
 =\#\{d:d\mid m^2,\ d<m\}
 =\frac{\tau(m^2)-1}{2}.$$ This is the number of nonzero entries in row $m$, with a loop counted once. When $m$ is squarefree with $r$ prime factors, $\tau(m^2)=3^r$. This exact formula, rather than an asymptotic estimate, is the endpoint obstruction at $\sigma=0$.

The divisor variable can also be recovered from a neighbor without first computing $k$: $$d=\frac{m^2}{m+n}.$$ Thus a direct divisibility test and a divisor-row enumerator describe literally the same finite support; their agreement in the canonical replay is an implementation test of this inverse map.

## The mixed triangle in edge coordinates

For completeness, the three orientations used in [\[eq:mixed-triangle\]](#eq:mixed-triangle){reference-type="eqref" reference="eq:mixed-triangle"} have the following exact data:

    $m$   $n$   $t$   $a$   $b$   $k=tab$
  ----- ----- ----- ----- ----- ---------
     15    30     5     1     2        10
     30    60    10     1     2        20
     60    15     3     4     1        12

The changing $t$ and changing coprime shape make the failure of a single-fiber interpretation explicit.

# Operator-ideal details {#app:operator-details}

## A compactness lemma tailored to symmetric rows

Let $A=(a_{mn})$ be a symmetric coefficient matrix and suppose its absolute row sums $r_m=\sum_n|a_{mn}|$ are finite, uniformly bounded, and tend to zero. The symmetric Schur test gives $\|A\|\leq\sup_m r_m$. Moreover, $$\|Q_MAQ_M\|\leq\sup_{m>M}r_m\longrightarrow0.$$ The operator $A-Q_MAQ_M=P_MA+Q_MAP_M$ is finite rank: the first term has finite-dimensional range and the second has finite-dimensional initial space. Hence $A$ is compact. This argument is the precise "finite tail control" used after [\[eq:row-decay\]](#eq:row-decay){reference-type="eqref" reference="eq:row-decay"}; it does not assume compactness in advance.

For a compact operator $K$ and projections $P_N\to I$ strongly, $(I-P_N)K\to0$ and $K(I-P_N)\to0$ in norm. Therefore $$\|K-P_NKP_N\|
 \leq\|(I-P_N)K\|+\|P_NK(I-P_N)\|\longrightarrow0,$$ which proves [\[eq:compression-convergence\]](#eq:compression-convergence){reference-type="eqref" reference="eq:compression-convergence"} in the exact compression form quoted in the main text.

## Phase removal and its limit

For $s=\sigma+i\tau$, define $U_\tau=\mathop{\mathrm{diag}}(n^{-i\tau/2})_{n\geq1}$. Since $|n^{-i\tau/2}|=1$, $U_\tau$ is unitary, and direct multiplication of matrix entries gives $$(U_\tau E_\sigma U_\tau)_{mn}
 =m^{-i\tau/2}e_\sigma(m,n)n^{-i\tau/2}=e_s(m,n).$$ If $E_\sigma$ is bounded, this matrix identity on finitely supported vectors extends by continuity. Conversely, $E_\sigma=U_\tau^*E_sU_\tau^*$, so boundedness and every unitarily invariant singular-value ideal are equivalent for $s$ and $\sigma$.

The two occurrences of $U_\tau$ point in the same direction. In general $U_\tau\neq U_\tau^*$, and consequently this calculation says nothing about eigenvalues. The direct complex trace calculations in [6](#sec:traces-determinants){reference-type="ref" reference="sec:traces-determinants"} are therefore necessary.

## Absolute entry summability is nuclear

For clarity, the trace-class sufficiency argument uses the expansion $$E_s=\sum_{m,n}e_s(m,n)(e_m\otimes e_n^*).$$ Each matrix unit has trace norm one. If $\sum_{m,n}|e_s(m,n)|<\infty$, the series converges in trace norm and $\|E_s\|_1$ is bounded by that sum. Equation [\[eq:absolute-entry-bound\]](#eq:absolute-entry-bound){reference-type="eqref" reference="eq:absolute-entry-bound"} proves exactly this hypothesis for $\sigma>1$. Necessity comes from the diagonal inequality and is not the converse of entrywise summability.

Similarly, the Hilbert--Schmidt norm is exactly the $\ell^2$ norm of all matrix entries. The loop subseries proves necessity at $1/2$, whereas the coprime double majorant proves sufficiency. No interpolation argument is needed, and no assertion is made for all $\mathcal{S}_{p}$.

# Determinants and closed-walk typing {#app:determinants}

We spell out the domain bookkeeping behind [\[cor:determinants\]](#cor:determinants){reference-type="ref" reference="cor:determinants"}. If $A\in\mathcal{S}_{2}$, the regularized product $\det_2(I-zA)$ is entire in $z$. On $|z|\|A\|<1$, expand the logarithm at the identity. Cancellation of the linear term gives $$\log\det_2(I-zA)
 =-\sum_{r=2}^{\infty}\frac{z^r}{r}\mathop{\mathrm{Tr}}(A^r).$$ If $A\in\mathcal{S}_{1}$, the uncancelled series begins at $r=1$, and $$\det_2(I-zA)=\det(I-zA)e^{z\mathop{\mathrm{Tr}}A}.$$ Applied to $A=E_s$, these facts give the exact permission table

  Domain                             Legal object       First graph-specific trace term
  ---------------------------------- ------------------ -------------------------------------
  $\mathop{\mathrm{Re}}s>\tfrac12$   $\det_2(I-zE_s)$   $-z^2\mathop{\mathrm{Tr}}(E_s^2)/2$
  $\mathop{\mathrm{Re}}s>1$          $\det(I-zE_s)$     $-z\mathop{\mathrm{Tr}}(E_s)$

The ordinary determinant is not used in the Hilbert--Schmidt-only strip.

For a finite compression $A_N=P_NE_sP_N$, multiplication gives $$\mathop{\mathrm{Tr}}(A_N^r)
 =\sum_{v_0,\ldots,v_{r-1}\leq N}
   \prod_{j=0}^{r-1}e_s(v_j,v_{j+1}),
 \qquad v_r=v_0.
 \label{eq:finite-closed-walks}$$ Thus $z^r$ records $r$ traversed edges and the trace chooses a base point. The division by $r$ in the logarithm is the cyclic-orbit normalization. When a temporal orbit is a repetition, the usual stabilizer multiplicity remains; none of this bookkeeping refers to $(a,b)=1$ on an individual edge.

For $r=2$ in the Hilbert--Schmidt domain, the infinite counterpart of [\[eq:finite-closed-walks\]](#eq:finite-closed-walks){reference-type="eqref" reference="eq:finite-closed-walks"} is absolutely summable and is precisely [\[eq:ordered-edge-trace\]](#eq:ordered-edge-trace){reference-type="eqref" reference="eq:ordered-edge-trace"}. We do not need to exchange an arbitrary infinite collection of closed walks for a determinant product, and we make no global logarithm claim across zeros of the determinant.

# Canonical replay and provenance boundary {#app:canonical-replay}

The finite results in [8](#sec:replay){reference-type="ref" reference="sec:replay"} were not transcribed from a plot. A candidate-local extractor checks canonical JSON encoding, rejects duplicate keys, verifies the State-A result ledger and all referenced SHA-256 values, requires the exact twelve-field comparison schema, and rejects any mutation survivor. A second candidate-local generator renders [3](#tab:canonical-replay){reference-type="ref" reference="tab:canonical-replay"} from that checked summary. Both scripts have a read-only check mode used after the final build.

The replay has three logically distinct layers:

1.  a direct evaluator tests $m+n\mid mn$ and constructs literal finite matrices;

2.  an independent parameter evaluator constructs coprime triples and divisor rows;

3.  an exact comparator checks supports, quotients, rows, finite trace powers, the negative minor, and the finite evidence type.

The complete State-A output tree has SHA-256 `328527680d533e34ce3aabc17f2cf5688759b0674b7fc8740d0c2df332b64c42`; the result ledger has SHA-256 `dba161719ef85dee433a13aa14505ab6b0f5ff0fef8c627ea39ddb4bf81bfe47`. These identifiers bind the report to exact bytes. They do not turn a finite equality into a proof of a limit.

In particular, the phrase "termwise finite scale cutoff" means that, for each fixed coprime pair, only scales whose two vertices lie below $N$ are included. Since that maximum scale depends on $(a,b)$, the finite sum must not be rewritten with a common infinite $\zeta(2s)$ factor. The latter appears only after absolute convergence has been proved for the full ordered-edge sum.

Finally, the protected writer intake records 91 authority/state nodes, 67 regular files and 24 directories. The paper artifact is built in a separate candidate tree. Integrity, route, and mutation records are reported as provenance; none is cited as a mathematical premise for [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.
