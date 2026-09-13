---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c429-polynomial-periodic-rigidity"
canonical_tex: "henon_dynamics/research_c429_c433/papers/C429_polynomial_periodic_rigidity/main.tex"
canonical_pdf: "henon_dynamics/research_c429_c433/papers/C429_polynomial_periodic_rigidity/main.pdf"
source_sha256: "1a607bc23fc307c86f15d4a489d260c0c9bd31ad77475bec9340ee4738e8a7b0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Polynomial periodic-data rigidity for unicritical maps in finite characteristic

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c429_c433/papers/C429_polynomial_periodic_rigidity>)
- [规范 TeX](<../../../../../henon_dynamics/research_c429_c433/papers/C429_polynomial_periodic_rigidity/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c429_c433/papers/C429_polynomial_periodic_rigidity/main.pdf>)
- [BibTeX](<../../../../../henon_dynamics/research_c429_c433/papers/C429_polynomial_periodic_rigidity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every prime $p$, every integer $d\ge2$, and every $c\in\overline{\mathbb F}_p$, we characterize polynomial coboundaries for $f(x)=x^d+c$ by their ordinary periodic data. A polynomial $h$ has zero sum on every primitive affine cycle if and only if $h=Q\circ f-Q$ for a polynomial $Q$. Each cycle point is counted once, including when the period is divisible by $p$. The proof works in full, possibly nonreduced periodic algebras. A weighted base-$d$ reduction gives a coefficient that stabilizes between consecutive returns. When $d\equiv1\pmod p$, a marked Hasse-derivative expansion replaces this stabilization by a nonzero coefficient difference. Both mechanisms give exact finite certificates: for any integer $M\ge1$ and $\deg h\le M$, two consecutive returns suffice, starting at $3\lfloor\log_d M\rfloor+4$ outside the latter congruence class and at $7\lfloor\log_d(PM)\rfloor+22$ within it, where $P=p^{v_p(d-1)}$. The result includes characteristic two, derivative-zero maps, arbitrary coefficients, and constant observables. The bounds concern return levels and iterate degrees, not optimized running time.
author:
- Anonymous Authors
bibliography:
- references.bib
title: 'Polynomial periodic-data rigidity for unicritical maps in finite characteristic'
```

## Markdown 正文

# Introduction and main results {#sec:introduction}

Periodic orbit sums are the immediate obstruction to solving a cohomological equation. In finite characteristic, their relationship with polynomial regularity is complicated by two elementary facts: an ordinary period may vanish as a scalar, and a polynomial defining periodic points may have multiple roots. We prove that neither phenomenon creates a polynomial defect for the entire family $x^d+c$. The proof also identifies two explicit return levels at which the periodic data already decides the equation.

Throughout, $p$ is a prime, $k=\overline{\mathbb F}_p$, $d\ge2$ is an integer, $c\in k$, and $$f(x)=x^d+c,\qquad \Delta_fQ=Q\circ f-Q.
 \label{eq:setup}$$ An *ordinary primitive cycle* is a finite orbit $O=\{a,f(a),\ldots,f^{\circ(r-1)}(a)\}$ of least period $r$. Its points are distinct, and we define $$S_h(O)=\sum_{a\in O}h(a),\qquad
 K_f=\{h\in k[x]:S_h(O)=0\text{ for every such }O\},
 \qquad B_f=\Delta_fk[x].$$ All cycles here are affine and geometric over $k$. In particular, cycles whose least period is divisible by $p$ are included with each point counted once. One application of $f$ is always the time step.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} For every prime $p$, every integer $d\ge2$, and every $c\in k$, one has $K_f=B_f$. Thus a polynomial has zero ordinary sum on every primitive $f$-cycle if and only if it equals $Q\circ f-Q$ for some $Q\in k[x]$.

The conclusion is polynomial, with no genericity restriction on $c$. It is not a statement for rational observables or for arbitrary polynomial base maps. The constant $Q(0)$ is immaterial, and the transfer is otherwise unique, as follows from the degree argument in [\[lem:normal\]](#lem:normal){reference-type="ref" reference="lem:normal"}.

Here is the finite form of the theorem. For every integer $j\ge1$ set $$F_j=f^{\circ j}-x,\qquad
 H_j(h)=\sum_{i=0}^{j-1}h\circ f^{\circ i}.
 \label{eq:returns}$$ The Hasse derivative $D^{[E]}u(x)$ is the coefficient of $z^E$ in $u(x+z)$. Fix an integer degree cap $M\ge1$, and put $$\begin{aligned}
 n_J&=3\lfloor\log_dM\rfloor+4,\label{eq:nj}\\
 P&=p^{v_p(d-1)},\qquad
 n_H=7\lfloor\log_d(PM)\rfloor+22
       &&\text{if }p\mid d-1.\label{eq:nh}\end{aligned}$$ The symbol $P$ in [\[eq:nh\]](#eq:nh){reference-type="eqref" reference="eq:nh"} is used only in that last regime.

::: {#tab:tests}
  Regime            Test at each return $j$          Returns tested
  ----------------- -------------------------------- ----------------
  $p\nmid d(d-1)$   $F_j\mid F_j'H_j(h)$             $n_J,n_J+1$
  $p\mid d$         $F_j\mid H_j(h)$                 $n_J,n_J+1$
  $p\mid d-1$       $F_j\mid D^{[P]}F_j\,H_j(h)^P$   $n_H,n_H+1$

  : Three disjoint and exhaustive finite certificates. The second row uses $F_j'=-1$, and the third uses $P=p^{v_p(d-1)}$. Each row requires both displayed returns.
:::

[\[thm:finite\]]{#thm:finite label="thm:finite"} Let $M\ge1$ be an integer and $h\in k[x]$ have degree at most $M$, including $h=0$. Let $n$ be $n_J$ or $n_H$ as prescribed by [1](#tab:tests){reference-type="ref" reference="tab:tests"}. The following are equivalent:

1.  $h\in B_f$;

2.  both polynomial divisibilities in the applicable row of [1](#tab:tests){reference-type="ref" reference="tab:tests"} hold;

3.  $H_j(h)(a)=0$ for every ordinary root $a$ of $F_j$, for both $j=n,n+1$.

If $h\notin B_f$, some primitive cycle with nonzero sum has period dividing $n$ or $n+1$, and hence period at most $n+1$. The two iterate polynomials have degrees bounded by $$\max_{j\in\{n,n+1\}}\deg F_j\le
 \begin{cases}
  d^5M^3,&p\nmid d-1,\\
  d^{23}(PM)^7,&p\mid d-1.
 \end{cases}
 \label{eq:degree-bounds}$$

Condition (iii) concerns full $j$-step return sums on *all* roots of $F_j$, not just cycles of exact period $j$. The zero polynomial is included without taking a logarithm of its degree; all logarithms use the positive cap $M$. The bounds in [\[eq:degree-bounds\]](#eq:degree-bounds){reference-type="eqref" reference="eq:degree-bounds"} concern the iterates. They are neither bounds on every unreduced product in a divisibility test nor optimized running-time or optimal-cutoff assertions.

## Prior work and the precise contribution

The periodic obstruction criterion belongs to the classical Livšic problem. For example, Kalinin's matrix-cocycle theorem assumes a transitive homeomorphism of a compact metric space with the closing property and obtains a Hölder transfer [@kalinin2011livsic Theorem 1.1]. Those hypotheses and that regularity class differ from the present polynomial equation over $k$. Li and Zhang prove a real Hölder Livšic theorem for expanding Thurston maps and for postcritically finite rational maps without periodic critical points on the Riemann sphere [@li2025ground Theorem 1.1]. These are genuine antecedents for the question, not specialization results supplying [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"}.

Finite periodic information also has an established role. Zou and Wei obtain approximate Hölder coboundaries from finite small periodic data for transitive Anosov diffeomorphisms [@zou2025finite Theorem 1.1]. Here the conclusion is exact, and the cutoff depends on the polynomial degree rather than an approximation tolerance. We make no claim to have introduced the finite Livšic problem.

The algebraic infrastructure is likewise classical. Cattani--Dickenstein--Sturmfels relate normal-form coefficients, global residues, and Jacobian traces in zero-dimensional complete intersections [@cattani1996residues Section 4 of the accessible preprint]. Cvitanović--Hansen--Rolf--Vattay derive finite binomial matrices and successive multiplier-weighted trace relations for quadratic maps [@cvitanovic1998beyond Section 4]. They credit the earlier finite-matrix construction to Levin--Sodin--Yuditskii [@levin1994ruelle]. We use the directly inspected 1998 formulas for this comparison; only the publisher abstract of the 1994 article was accessible in the source check. No unread theorem from that article is invoked below.

The additional step is a specific coefficient comparison as the number of cyclic variables changes. In the first derivative regime, insertion of a forced weight-one carry transition stabilizes a short-support coefficient. In the congruence class $d\equiv1$ modulo $p$, an inserted marked transition produces instead a nonzero difference equal to a nonzero scalar multiple of the leading normal coefficient raised to a characteristic power. The necessary derivative certificates at two adjacent levels then eliminate every normal-form defect. All algebraic ingredients needed for this argument are proved below; complex residue formulas are not transplanted into finite characteristic. The source comparison is bounded and carries no worldwide-priority guarantee.

## Proof organization

gives the normal form, cyclic digit basis, leading-digit detector, and multiplicity-safe certificates. proves the stable coefficient by a full weight-preserving path bijection, and [4](#sec:jacobian){reference-type="ref" reference="sec:jacobian"} handles $p\nmid d-1$. The Hasse proof occupies [\[sec:hasse,sec:insertion\]](#sec:hasse,sec:insertion){reference-type="ref" reference="sec:hasse,sec:insertion"}; it is written with $P\ge2$ so that characteristic two is included in the argument itself. records the skew-map interpretation and the boundary of the derivative tests.

# Normal forms and full periodic algebras {#sec:algebra}

We first separate two statements that need not coincide at a multiple return root: a polynomial can vanish at every ordinary root of $F_n$ without being zero in $k[x]/(F_n)$. The coefficient arguments will take place in the latter, full algebra.

[\[lem:normal\]]{#lem:normal label="lem:normal"} For $$V_d=k\oplus\bigoplus_{\substack{r\ge1\\d\nmid r}}kx^r$$ one has the direct sum of $k$-vector spaces $k[x]=B_f\oplus V_d$. Thus every polynomial has a unique normal part $v$ in a decomposition $h=\Delta_fQ+v$. The elimination does not increase degree, and $Q$ is unique up to a constant.

For $t\ge1$, the polynomial $\Delta_fx^t=(x^d+c)^t-x^t$ is monic of degree $dt$. Eliminate the largest positive exponent divisible by $d$ using the corresponding multiple of this polynomial, and continue. Each subtraction introduces only smaller exponents, so the process terminates without increasing degree. This proves existence. If $Q$ is nonconstant, then $\deg\Delta_fQ=d\deg Q$, whereas a nonzero element of $V_d$ has degree zero or a positive degree not divisible by $d$. Their intersection is therefore zero. The same degree argument shows that the kernel of $\Delta_f$ on $k[x]$ is the constants. For $h=0$, take $Q=v=0$.

Telescoping gives $B_f\subseteq K_f$. It also shows that on a root $a$ of $F_n$ of native period $r$, $$H_n(h)(a)=(n/r)S_h(O_a),
 \label{eq:ordinary-repetition}$$ where $n/r$ is an integer counting repetitions. This formula is not division in $k$. In particular, $h\in K_f$ implies ordinary-root vanishing of every $H_n(h)$.

[\[lem:basis\]]{#lem:basis label="lem:basis"} For $n\ge1$, with indices taken modulo $n$, set $$\mathcal A_n=k[X_0,\ldots,X_{n-1}]/
       (X_i^d+c-X_{i+1}:0\le i<n).$$ The substitutions $X_i\mapsto f^{\circ i}(x)$ and $x\mapsto X_0$ identify $\mathcal A_n$ with $k[x]/(F_n)$. The monomials $$X^{\mathbf e}=\prod_{i=0}^{n-1}X_i^{e_i},\qquad
                  0\le e_i<d,
 \label{eq:digit-basis}$$ are a basis, including when $F_n$ is not squarefree.

The first $n-1$ relations eliminate all variables except $X_0$; the last becomes $F_n(X_0)=0$. The substitutions are inverse, and the dimension is $d^n$. Replacing a factor $X_i^d$ by $X_{i+1}-c$ strictly lowers total degree in each resulting term, including at wraparound. These replacements terminate at the $d^n$ monomials in [\[eq:digit-basis\]](#eq:digit-basis){reference-type="eqref" reference="eq:digit-basis"}. They span and their number equals the dimension, proving linear independence.

Write $[M]U$ for the coefficient of a digit-basis monomial $M$ in $U\in\mathcal A_n$. We use the notation $$\mathcal H_n(v)=\sum_{i=0}^{n-1}v(X_i),\qquad
 \Pi_n=\prod_{i=0}^{n-1}X_i^{d-1}.
 \label{eq:class-notation}$$ The first is the class of $H_n(v)$. Telescoping and the chain rule give, respectively, $$\mathcal H_n(\Delta_fQ)=0,\qquad [F_n']=d^n\Pi_n-1.
 \label{eq:telescoping-jacobian}$$ Integer coefficients such as $d^n$ are interpreted in $k$; digits and reduction exponents remain integers.

[\[lem:leading\]]{#lem:leading label="lem:leading"} Let $v\in V_d$ have positive leading degree $D$ and leading coefficient $a_D\ne0$. Put $m=\lfloor\log_dD\rfloor$, and write $D=\sum_{j=0}^m e_jd^j$ in base $d$. For $n>2m$, the digit monomial $M_D=\prod_{j=0}^mX_j^{e_j}$ satisfies $$\mathcal H_n(v)=a_D.
 \label{eq:leading-coefficient}$$

Reduce a term $X_i^r$, where $r\le D<d^{m+1}$, in the forward window $X_i,\ldots,X_{i+m}$, with local weights $1,d,\ldots,d^m$. Choosing the next variable in $X_{i+j}^d=X_{i+j+1}-c$ preserves weight; choosing the constant strictly lowers it. No term can reach $X_{i+m}^d$, whose weight would exceed $r$. The reduction stays inside a window of distinct variables. For a fixed reduction order, the unique branch choosing no constants produces the base-$d$ digits of $r$ with coefficient one and weight $r$. Every other branch has smaller weight.

Normality gives $e_0>0$, and positivity gives $e_m>0$. For $m\ge1$, only the circular window starting at zero can contain both endpoints $0,m$: the other directed distance $n-m$ exceeds $m$. If $m=0$, the same assertion holds for singleton windows. Thus only source zero can reach $M_D$. Its target weight is $D$, so only $a_DX_0^D$ contributes, and it contributes exactly $a_D$. Constants have empty support. This proves [\[eq:leading-coefficient\]](#eq:leading-coefficient){reference-type="eqref" reference="eq:leading-coefficient"}, regardless of any cancellation among smaller-weight terms.

[\[lem:root-certificates\]]{#lem:root-certificates label="lem:root-certificates"} Let $G\ne0$ and $U$ belong to $k[x]$. If $U$ vanishes at every ordinary root of $G$, then for every integer $E\ge1$, $$G\mid D^{[E]}G\,U^E.
 \label{eq:hasse-necessary}$$ In particular $G\mid G'U$.

At a root $a$ of multiplicity $e$, write $G=(x-a)^eV$ with $V(a)\ne0$. The coefficient-of-$z^E$ product rule gives $$\operatorname{ord}_a D^{[E]}G\ge\max(e-E,0).$$ The factor $U^E$ has order at least $E$, so the product has order at least $e$. Check this at each root of $G$ to obtain the divisibility. Vanishing Hasse coefficients only increase the relevant order and cause no exception.

Neither this lemma nor [\[lem:leading\]](#lem:leading){reference-type="ref" reference="lem:leading"} assumes reducedness. The first gives a necessary passage from ordinary roots to the full algebra. Its converse at one level is not required; the two-level arguments below supply the stronger finite equivalence.

# Stable full-background coefficients {#sec:carry}

Multiplication by $\Pi_n$ changes the leading-digit problem: a reduction can now pass around the whole cycle. The next proposition controls that passage and compares all contributing paths at consecutive levels. It is valid in every characteristic; the restriction on $d$ enters only when it is applied to the Jacobian.

[\[prop:stabilization\]]{#prop:stabilization label="prop:stabilization"} Let $M\ge1$, $m=\lfloor\log_dM\rfloor$, and $v\in V_d$ have degree at most $M$. Fix digits $e_0,\ldots,e_m\in\{0,\ldots,d-1\}$, not all zero, and let $M_{\mathbf e}=\prod_{j=0}^mX_j^{e_j}$. For $n\ge3m+4$, $$(\Pi_{n+1}\mathcal H_{n+1}(v))
       =[M_{\mathbf e}](\Pi_n\mathcal H_n(v)).
 \label{eq:stabilization}$$ The coefficients are taken in their respective full periodic algebras.

## A complete one-circuit expansion

It suffices first to treat a positive exponent $r\le M$ with $d\nmid r$. Put $L=m+1$ and suppose $n\ge L$. For a source $i\in\mathbb Z/n\mathbb Z$, process the sites of $\Pi_nX_i^r$ in the order $i,i+1,\ldots,i+n-1$. Set $t_0=r$. At step $s$ the current exponent is $d-1+t_s$; define $$b_s=(d-1+t_s)\bmod d,\qquad
 q_s=\left\lfloor\frac{d-1+t_s}{d}\right\rfloor.
 \label{eq:carry-quotient}$$ The exact local expansion is $$X_{i+s}^{d-1+t_s}
   =\sum_{t_{s+1}=0}^{q_s}
      \binom{q_s}{t_{s+1}}(-c)^{q_s-t_{s+1}}
      X_{i+s}^{b_s}X_{i+s+1}^{t_{s+1}}.
 \label{eq:carry-expansion}$$ A path is a finite sequence $(t_0,\ldots,t_n)$ obeying these transitions, with weight $$w(t)=\prod_{s=0}^{n-1}
      \binom{q_s}{t_{s+1}}(-c)^{q_s-t_{s+1}}\in k.
 \label{eq:carry-weight}$$ We retain zero-weight paths, and a factor with exponent zero is one also when $c=0$.

Induction from $t_{s+1}\le(d-1+t_s)/d$ yields $$t_s\le1+\frac{r-1}{d^s}.
 \label{eq:carry-bound}$$ Since $d^L>M-1$, the carry at step $L$ is at most one. The states zero and one cannot return to a larger state, so $t_n\le1$. At the source the first output digit satisfies $$b_0=(r-1)\bmod d\le d-2,$$ because $d\nmid r$. The final carry therefore lands legally: $b_0+t_n\le d-1$. No second circuit is necessary.

Let $\mathbf e(t,i)$ have digit $b_0+t_n$ at the source and digit $b_s$ at site $i+s$ for $1\le s<n$. Repeated use of [\[eq:carry-expansion\]](#eq:carry-expansion){reference-type="eqref" reference="eq:carry-expansion"} now proves an equality in the digit basis, $$\Pi_nX_i^r=\sum_t w(t)X^{\mathbf e(t,i)}.
 \label{eq:whole-circuit}$$ This is a finite polynomial expansion with a legal final digit at every site. Its validity does not rely on coefficients avoiding cancellation. The eventual-state transitions will be used explicitly:

   Incoming carry   Output digit   Outgoing carry   Weight
  ---------------- -------------- ---------------- --------
        $0$            $d-1$            $0$          $1$
        $1$             $0$             $1$          $1$
        $1$             $0$             $0$          $-c$

Here $d-1$ is a positive integer digit, not a scalar reduced modulo $p$.

## Localization of every source

Let $E=\{j\in[0,m]:e_j>0\}$ be the nonempty support of the target. If a path in [\[eq:whole-circuit\]](#eq:whole-circuit){reference-type="eqref" reference="eq:whole-circuit"} produces this target and $n\ge L+1$, its source satisfies $$i\in\left(\bigcup_{s=0}^{L-1}(E-s)\right)\cup(E+1)
       \subseteq[-m,m+1]\pmod n.
 \label{eq:source-localization}$$ To prove this, consider a source outside $E$ for which none of the next $L-1$ sites lies in $E$. Its final source digit is zero, so $b_0+t_n=0$ as an equality of nonnegative integers. In particular $t_n=0$, and the first $L-1$ nonsource outputs are zero.

If $t_L=0$, all subsequent carries are zero. Since $n-1\ge L$, the last output is $d-1>0$, and hence $i-1\in E$. If $t_L=1$, there must be a first drop from one to zero before the circuit ends. Were it at the last step, there would be no subsequent nonzero outputs, and the entire target would be empty. It occurs no later than step $n-2$, after which the last output is again $d-1>0$. Thus $i-1\in E$ in either case, proving [\[eq:source-localization\]](#eq:source-localization){reference-type="eqref" reference="eq:source-localization"}.

For $n\ge3m+4$, every contributing source lies in the two disjoint blocks $$I_n=\{0,\ldots,m+1\}\cup\{n-m,\ldots,n-1\}.
 \label{eq:source-blocks}$$ The second block is empty if $m=0$. The argument is uniform in the normal exponent $r\le M$ and preserves all target digits, including digits greater than one.

## Insertion and deletion of one forced transition

Set $a=2m+2$. At level $n\ge3m+4$, neither $a$ nor $a+1$ is a source or a nonzero target site: the lower source block ends at $m+1<a$, and the upper block begins at $n-m\ge2m+4>a+1$. The forward distance from a source to $a$ is at least $L$. Indeed it is $a-i\ge m+1$ for $0\le i\le m+1$, and $a+n-i\ge a+1$ for $n-m\le i<n$.

By [\[eq:carry-bound\]](#eq:carry-bound){reference-type="eqref" reference="eq:carry-bound"}, the incoming carry at $a$ is at most one. Its zero output forces it to be one. The zero output at the following nonsource site forces the outgoing carry at $a$ also to be one. The transition at $a$ is therefore $1\to1$ with weight exactly one.

Insert a new site just after $a$, with output zero and transition $1\to1$, and relabel old indices by $$\iota_n(u)=
 \begin{cases}u,&0\le u\le a,\\u+1,&a+1\le u<n.
 \end{cases}
 \label{eq:ordinary-insertion}$$ The target supported in $[0,m]$ is unchanged. The source becomes $\iota_n(i)$; every old transition occurs in the same cyclic order, and the initial carry, final carry, and source digit are preserved. The inserted transition has weight one.

Conversely, a target-producing path at level $n+1$ has its source in $I_{n+1}$. It is neither $a+1$ nor $a+2$, and those sites have zero target digits. The forward distance to $a+1$ is at least $L$. The same two-output argument forces the transition at $a+1$ to be $1\to1$ of weight one. Delete it and relabel later indices down by one. This recovers a legal path at level $n$ with the same weight and full target vector. The blocks in [\[eq:source-blocks\]](#eq:source-blocks){reference-type="eqref" reference="eq:source-blocks"} correspond under [\[eq:ordinary-insertion\]](#eq:ordinary-insertion){reference-type="eqref" reference="eq:ordinary-insertion"}, so no new source at the inserted site is missed.

Insertion and deletion are mutual inverses on *all pairs* of a source and a target-producing path. Summing [\[eq:whole-circuit\]](#eq:whole-circuit){reference-type="eqref" reference="eq:whole-circuit"} therefore proves [\[eq:stabilization\]](#eq:stabilization){reference-type="eqref" reference="eq:stabilization"} for $v=x^r$. If $v=a_0$ is constant, $\Pi_n\mathcal H_n(a_0)=na_0\Pi_n$ has zero target coefficient, since $n>m+1$ and the target has short support. Taking the linear combination over all normal monomials of $v$ proves [\[prop:stabilization\]](#prop:stabilization){reference-type="ref" reference="prop:stabilization"}.

For $d=2$ the digit basis is squarefree, and this is precisely the binary full-product stabilization. The proof above retains the source digit and all higher base-$d$ digits, so the general degree statement requires no unverified analogy with that case.

# The first two derivative regimes {#sec:jacobian}

We prove both main theorems when $p\nmid d-1$. The common normalization and coefficient lemmas hold in every characteristic. We first treat the nonzero Jacobian scalar, then the derivative-zero branch separately.

## Adjacent Jacobians when $p\nmid d(d-1)$

Fix $M\ge1$, $\deg h\le M$, and $n=n_J$. Suppose $$F_j\mid F_j'H_j(h),\qquad j=n,n+1.
 \label{eq:two-jacobians}$$ Write $h=\Delta_fQ+v$ by [\[lem:normal\]](#lem:normal){reference-type="ref" reference="lem:normal"}. Telescoping in [\[eq:telescoping-jacobian\]](#eq:telescoping-jacobian){reference-type="eqref" reference="eq:telescoping-jacobian"} shows that [\[eq:two-jacobians\]](#eq:two-jacobians){reference-type="eqref" reference="eq:two-jacobians"} is unchanged upon replacing $h$ by $v$, and $\deg v\le M$.

Suppose $v$ has positive leading degree $D$ and leading coefficient $a_D\ne0$. For the target $M_D$ of [\[lem:leading\]](#lem:leading){reference-type="ref" reference="lem:leading"}, put $$C_j=[M_D](\Pi_j\mathcal H_j(v)).$$ Both selected levels exceed $2\lfloor\log_dD\rfloor$ and meet the stabilization bound for the cap $M$. Equations [\[eq:leading-coefficient\]](#eq:leading-coefficient){reference-type="eqref" reference="eq:leading-coefficient"}, [\[eq:telescoping-jacobian\]](#eq:telescoping-jacobian){reference-type="eqref" reference="eq:telescoping-jacobian"}, and [\[eq:two-jacobians\]](#eq:two-jacobians){reference-type="eqref" reference="eq:two-jacobians"} yield $$d^nC_n=a_D,\qquad d^{n+1}C_{n+1}=a_D.
 \label{eq:two-leading-jacobians}$$ By [\[prop:stabilization\]](#prop:stabilization){reference-type="ref" reference="prop:stabilization"}, $C_{n+1}=C_n$. Subtract $d$ times the first equality from the second to get $(1-d)a_D=0$. The hypothesis $p\nmid d-1$ contradicts $a_D\ne0$.

Thus $v=a_0$ is constant. At return $j$ the remaining condition is $F_j\mid ja_0F_j'$. Here $F_j'$ has nonzero leading coefficient $d^j$ and degree $d^j-1<\deg F_j$, so $ja_0=0$. Applying this at $j=n,n+1$ and subtracting gives $a_0=0$. The two Jacobian tests therefore imply $h\in B_f$.

## Squarefree returns when $p\mid d$

In this case $f'=0$, and hence $$F_j'=-1\qquad(j\ge1).
 \label{eq:derivative-zero}$$ Every $F_j$ is squarefree. The tests in the second row of [1](#tab:tests){reference-type="ref" reference="tab:tests"} give $\mathcal H_n(v)=\mathcal H_{n+1}(v)=0$ after normalization. A positive normal degree $D\le M$ is excluded at either level by [\[lem:leading\]](#lem:leading){reference-type="ref" reference="lem:leading"}. For a constant normal part, the two equations are $na_0=0$ and $(n+1)a_0=0$, and again $a_0=0$. This argument includes $p=2$, for which $-1=1$; it does not replace the iteration of $f$ by another clock.

## Finite equivalence and ordinary detection

If $h=\Delta_fQ$, then $$H_j(h)=Q(f^{\circ j}(x))-Q(x)
\quad\text{is divisible by }F_j
 \label{eq:polynomial-telescoping}$$ for every $j$. It satisfies both the applicable divisibilities and the ordinary-root tests. In the first regime, ordinary-root vanishing implies the Jacobian test by [\[lem:root-certificates\]](#lem:root-certificates){reference-type="ref" reference="lem:root-certificates"}; in the second it is equivalent to divisibility because of [\[eq:derivative-zero\]](#eq:derivative-zero){reference-type="eqref" reference="eq:derivative-zero"}. Together with the two preceding subsections, this proves the three-way equivalence in [\[thm:finite\]](#thm:finite){reference-type="ref" reference="thm:finite"} whenever $p\nmid d-1$.

If $h\in K_f$, formula [\[eq:ordinary-repetition\]](#eq:ordinary-repetition){reference-type="eqref" reference="eq:ordinary-repetition"} supplies the two ordinary-root tests, so $h\in B_f$. The reverse inclusion is telescoping. This proves [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"} in these regimes. Alternatively, after excluding every positive normal part, an ordinary fixed point of $f$ directly excludes a nonzero constant: the polynomial $f(x)-x$ has a root in the algebraically closed field $k$.

For a noncoboundary, one ordinary-root test fails at a point $a$ of period $r\mid j$, where $j=n$ or $n+1$. Then $$H_j(h)(a)=(j/r)S_h(O_a)\ne0$$ implies $S_h(O_a)\ne0$, without division in $k$. In particular the detecting primitive period is at most $n+1$. With $m=\lfloor\log_dM\rfloor$, $$\deg F_j\le d^{n+1}=d^{3m+5}\le d^5M^3.$$ This is the first bound in [\[eq:degree-bounds\]](#eq:degree-bounds){reference-type="eqref" reference="eq:degree-bounds"}, including zero and constant inputs in the equivalence proved above.

# A marked Hasse detector {#sec:hasse}

Assume now that $p\mid d-1$. The scalars $d^n$ and $d^{n+1}$ coincide in $k$, so [\[eq:two-leading-jacobians\]](#eq:two-leading-jacobians){reference-type="eqref" reference="eq:two-leading-jacobians"} cannot give the required contradiction. We replace the ordinary derivative by the first nonlinear Hasse derivative and compare a different target digit string. Write $$P=p^{v_p(d-1)},\qquad A=(d-1)/P,\qquad
 \alpha=A\bmod p\in k^\times.
 \label{eq:hasse-parameters}$$ The integer inequalities used below are $2\le P<d$ and $d-1\ge2$. They include $p=2$.

## The exact marked backgrounds

Since $d=PA+1$ and $P$ is a characteristic power, $$f(x+z)=(x+z)(x^P+z^P)^A+c.$$ There are no Taylor terms of orders $2,\ldots,P-1$, and $$f'(x)=x^{d-1},\qquad D^{[P]}f(x)=\alpha x^{d-P}.
 \label{eq:hasse-first-term}$$ The absence of those intermediate orders is preserved by composition. If $g(x+z)=g(x)+a(x)z+b(x)z^P+O(z^{P+1})$, the coefficient of $z^P$ in $f(g(x+z))$ is $$f'(g(x))b(x)+D^{[P]}f(g(x))a(x)^P.$$ For $P=2$ the interval of absent intermediate orders is empty, but this coefficient formula is unchanged.

Induction gives, in $\mathcal A_n$, $$J_n:=[D^{[P]}F_n]=\alpha\sum_{j=0}^{n-1}B_{n,j},
 \label{eq:marked-formula}$$ where $$B_{n,j}=
 \left(\prod_{a<j}X_a^{P(d-1)}\right)X_j^{d-P}
 \left(\prod_{a>j}X_a^{d-1}\right).
 \label{eq:marked-background}$$ The term $-x$ has zero $P$th Hasse derivative because $P>1$. We call $j$ the *mark*. Its background exponents are $$b_a(j)=
 \begin{cases}
  P(d-1),&a<j,\\
  d-P,&a=j,\\
  d-1,&a>j.
 \end{cases}
 \label{eq:background-digits}$$

Normal exponents remain normal after multiplication by $P$, since $\gcd(d,P)=1$. Moreover, $$\mathcal H_n(v)^P=\mathcal H_n(v^P).
 \label{eq:frobenius-trace}$$ All coefficients of $v$ are raised to their $P$th powers in this identity; none is assumed to lie in the prime field. By [\[lem:root-certificates\]](#lem:root-certificates){reference-type="ref" reference="lem:root-certificates"}, ordinary-root vanishing of $H_n(h)$ implies $F_n\mid D^{[P]}F_nH_n(h)^P$ without any root-multiplicity bound.

## The target digit string and reduction paths

Fix a cap $M\ge1$ and a normal polynomial $v$ with positive leading degree $D\le M$ and leading coefficient $a_D\ne0$. For this argument put $$m=\lfloor\log_d(PM)\rfloor,\qquad L=m+2,
 \qquad s\ge4L+4,\qquad n\ge s+3L+4.
 \label{eq:hasse-spacing}$$ Define a digit-basis monomial $T_{n,s,D}$ by the following digits:

1.  $d-P+1$ at site $0$;

2.  $d-1$ at sites $1,\ldots,s-1$;

3.  the base-$d$ digits of $PD-1$, padded to $m+1$ digits, at sites $s,\ldots,s+m$;

4.  zero at all later sites.

These are legal digits. Because $d\nmid PD$, the first digit after the long block satisfies $$e_s=(PD-1)\bmod d\le d-2.
 \label{eq:first-small-digit}$$ Equivalently, this is the digit string of the integer $PDd^s-P+1$. This description does not identify its univariate representative with a pure power when $c\ne0$.

Expand a term $B_{n,j}X_i^{Pr}$, where $1\le r\le D$ is a normal exponent of $v$ and $i$ is its *source*. At a processed site with incoming carry $t_a$, divide the exponent $b_a+t_a+Pr\mathbf 1_{a=i}$ by $d$: $$q_a=\left\lfloor\frac{b_a+t_a+Pr\mathbf 1_{a=i}}d\right\rfloor,
 \qquad e_a=(b_a+t_a+Pr\mathbf 1_{a=i})\bmod d.$$ The choice of an outgoing carry $0\le t_{a+1}\le q_a$ has weight $$\binom{q_a}{t_{a+1}}(-c)^{q_a-t_{a+1}}.
 \label{eq:marked-weight}$$ Writing $\kappa_a=q_a-t_{a+1}\ge0$, a legal closed-circuit path satisfies the integer identity $$e_a=b_a+t_a+Pr\mathbf 1_{a=i}-dt_{a+1}-d\kappa_a.
 \label{eq:marked-conservation}$$ We must first justify this closed-circuit description at the cut; an unchecked wraparound could change both its digit and its weight.

## Adaptive cuts and exclusion of overflow

Choose a nonsource cut $a\in[1,s-1]$ whose forward cyclic distance from the source is at least $L$. Such a choice exists: only $L$ consecutive positions are forbidden by the source and this distance requirement, whereas the long block has more than $L$ positions. Start a one-circuit expansion at $a$ with no incoming carry. The carry produced by the last site will be added to its retained digit at the end.

Before the source is processed, every incoming carry is at most $P-1$, since $b_u\le P(d-1)$ and the initial carry is zero. After $h\ge1$ steps from the source, the carry satisfies $$t\le P+\frac{Pr-1}{d^h}.
 \label{eq:marked-carry-bound}$$ At the source its incoming carry is at most $P-1$, giving the bound for $h=1$. Each subsequent nonsource step obeys $t_{\mathrm{next}}\le(P(d-1)+t)/d$, proving the induction. Since $d^{L-1}=d^{m+1}>PM-1$, the carry is at most $P$ after $L-1$ steps and stays at most $P$ thereafter.

The cut initially retains digit $d-P$ if it is before or at the mark, and digit $d-1$ if it is after the mark. Its final incoming carry is at most $P$. In the latter case, the preceding site is after the mark or is the mark itself; it is not the source, and its incoming carry is at most $P$. Its outgoing carry is therefore at most one. Thus the final exponent at the cut is at most $d$ in all cases.

If that exponent is below $d$, one circuit already gives a digit monomial. If it equals $d$, reduce the cut once more. Its digit becomes zero, and a carry zero or one is sent forward. All other sites already have digits below $d$. A carry one continues only through a digit $d-1$, leaving zero there. It either stops or completes a further circuit; on returning to the cut, it raises its zero digit to at most one and stops. Every overflowing branch consequently has final cut digit at most one. The target cut digit is $d-1\ge2$, so no such branch can contribute.

For a contributing branch, the retained cut digit plus its final incoming carry is still below $d$. Including that final carry does not change the quotient used at the cut initially. Thus its binomial weight is exactly [\[eq:marked-weight\]](#eq:marked-weight){reference-type="eqref" reference="eq:marked-weight"} with this incoming carry included, and [\[eq:marked-conservation\]](#eq:marked-conservation){reference-type="eqref" reference="eq:marked-conservation"} holds cyclically at every site. Conversely, the legal paths with this cut quotient reconstruct the same nonoverflow branches of the one-circuit expansion. No contributing branch or weight has been discarded except for the explicitly excluded overflow. This argument is termwise and does not require nonzero or cancellation-free weights.

## Localization of all sources

For a fixed mark $j$, define a baseline carry $$\ell_a=\begin{cases}P-1,&a\le j,\\0,&a>j.
 \end{cases}$$ For $a<n-1$, it satisfies $$b_a+\ell_a=d-1+d\ell_{a+1}.
 \label{eq:baseline}$$ Put $u_a=t_a-\ell_a$. The conservation identity becomes $$e_a=d-1+u_a+Pr\mathbf 1_{a=i}-du_{a+1}-d\kappa_a
                  \qquad(a<n-1).
 \label{eq:excess}$$ At a nonsource site, $u_a\le0$ implies $du_{a+1}\le d-1$, hence the integer $u_{a+1}\le0$. Nonpositive excess cannot become positive without passing the source.

At a nonsource site with incoming carry between zero and $P$, a target digit $d-1$ forces $t_a=\ell_a$, while a zero digit requires $t_a=\ell_a+1$. To verify this, reduce each of the three backgrounds in [\[eq:background-digits\]](#eq:background-digits){reference-type="eqref" reference="eq:background-digits"} modulo $d$ and use $P<d$. In particular a zero digit is impossible when $u_a\le0$.

Let $b=s+m+1$, a zero target site. Every contributing source lies in $$I_{n,s}=\{s-L,s-L+1,\ldots,b\}.
 \label{eq:hasse-source-interval}$$ Indeed, if $i\le s-L-1$, choose the adaptive cut $a=i+L$. It lies in $[1,s-1]$ at the required distance from the source. Its carry is at most $P$, and its target digit is $d-1$, so $u_a=0$. The ordinary index interval $[a,b]$ contains no source. Equation [\[eq:excess\]](#eq:excess){reference-type="eqref" reference="eq:excess"} keeps the excess nonpositive until the zero site $b$, a contradiction. If $i\ge b+1$, choose $a=L$. Its forward distance from the source is $n-i+L\ge L+1$. Starting again with $u_a=0$, the same argument reaches $b$ before the source and gives the contradiction.

There is also no target contribution from a background $B_{n,j}$ without a source. Use the cut $a=L$. The carry bounds and overflow exclusion remain valid; the excess starts at zero and cannot become positive before $b$. Thus constants in $v^P$ contribute zero to the coefficient under consideration, regardless of the scalar $n$ in their return sum.

## A common cut after localization

All sources in [\[eq:hasse-source-interval\]](#eq:hasse-source-interval){reference-type="eqref" reference="eq:hasse-source-interval"} are positive, and $$n-i\ge n-b\ge2L+5.$$ We can now process every contributing term in the common order $0,1,\ldots,n-1$. Site zero is not a source. Its retained initial digit is $d-P$, whether it is the mark or precedes the mark. By [\[eq:marked-carry-bound\]](#eq:marked-carry-bound){reference-type="eqref" reference="eq:marked-carry-bound"}, the incoming carry at the last site is at most $P$. That site is the mark or follows it, so its outgoing carry is at most one. The final digit at zero is at most $d-P+1<d$, and no second circuit occurs.

To produce the specified anchor digit it must be exactly $d-P+1$. Every contributing path therefore has the convention $$t_0=t_n=1.
 \label{eq:common-cut}$$ At site zero this fictitious initial carry leaves the initial quotient and weight unchanged, because $d-P+1<d$. Hence [\[eq:marked-weight\]](#eq:marked-weight){reference-type="eqref" reference="eq:marked-weight"}--[\[eq:marked-conservation\]](#eq:marked-conservation){reference-type="eqref" reference="eq:marked-conservation"}, with [\[eq:common-cut\]](#eq:common-cut){reference-type="eqref" reference="eq:common-cut"}, describe all contributing branches in one fixed order. Before the source, all carries after site zero are at most $P-1$.

# Marked insertion and the remaining congruence class {#sec:insertion}

Retain the parameters, target, and normal polynomial from [5](#sec:hasse){reference-type="ref" reference="sec:hasse"}. Define $$C(n,s)=[T_{n,s,D}]\bigl(J_n\mathcal H_n(v^P)\bigr).
 \label{eq:marked-coefficient}$$ The needed comparison is not stabilization. Instead, one new marked position contributes a nonzero leading term.

[\[prop:marked-difference\]]{#prop:marked-difference label="prop:marked-difference"} Under [\[eq:hasse-spacing\]](#eq:hasse-spacing){reference-type="eqref" reference="eq:hasse-spacing"}, $$C(n+1,s+1)-C(n,s)=\alpha a_D^P\ne0.
 \label{eq:marked-difference}$$ This holds for every prime $p$ in the regime $p\mid d-1$.

## Every old marked path is paired

Insert a site at index $a=2L$ and map old indices by $$\iota(u)=\begin{cases}u,&u<a,\\u+1,&u\ge a.
 \end{cases}
 \label{eq:marked-insertion}$$ The new parameters are $(n+1,s+1)$ with $m,L,D$ unchanged. The target inserts a digit $d-1$ at $a$ and preserves all old digits. The spacing conditions still hold. The source intervals in [\[eq:hasse-source-interval\]](#eq:hasse-source-interval){reference-type="eqref" reference="eq:hasse-source-interval"} correspond under $\iota$; their lower endpoint $s-L\ge3L+4$ is larger than $a+1$. No source can occur at the inserted site or its immediate neighbors.

Take an old mark $j$, now located at $\iota(j)$. At the insertion position the source is still ahead, the target digit is $d-1$, and the incoming carry is at most $P-1$. It is therefore the low baseline: $P-1$ if the mark is ahead and zero if the mark is behind. Insert an unmarked nonsource site with the same incoming and outgoing baseline. In the first case its background is $P(d-1)$, quotient $P-1$, and digit $d-1$; in the second its background is $d-1$, quotient zero, and digit $d-1$. In both cases its weight is one. All old transitions and the fixed-cut convention [\[eq:common-cut\]](#eq:common-cut){reference-type="eqref" reference="eq:common-cut"} are preserved.

Conversely, take a new target-producing path whose mark is not the inserted site. That site and its successor are nonsources with digit $d-1$ and with the source ahead. Their incoming carries are their low baselines. Since the mark is not at the inserted site, these baselines are equal, including when the mark is immediately before it or is its successor. The inserted transition has weight one and can be deleted. The remaining path is legal with the old target and the same cut convention.

These operations are inverse for all old marks, all sources, and all target-producing branches. Constants contribute no target paths by [5](#sec:hasse){reference-type="ref" reference="sec:hasse"}. Consequently the difference in [\[eq:marked-difference\]](#eq:marked-difference){reference-type="eqref" reference="eq:marked-difference"} consists exactly of the paths whose mark is at the newly inserted site $a$.

## The new mark isolates the leading source

For this subsection put $N=n+1$ and $S=s+1$, with the mark at $a=2L$. Every source lies after $a+1$. The mark has incoming carry $P-1$, so its exponent is $(d-P)+(P-1)=d-1$. Its quotient and outgoing carry are zero, and its weight is one.

After the mark and before the source, the background is $d-1$. Starting with carry zero, each such site has output $d-1$ and outgoing carry zero. The smaller target digit at $S$ in [\[eq:first-small-digit\]](#eq:first-small-digit){reference-type="eqref" reference="eq:first-small-digit"} therefore forces the source index to satisfy $i\le S$.

The source term is $X_i^{Pr}$ with $1\le r\le D$ and incoming carry zero. Multiply [\[eq:marked-conservation\]](#eq:marked-conservation){reference-type="eqref" reference="eq:marked-conservation"} by $d^{u-i}$ and sum over the suffix $u=i,\ldots,N-1$. Every background in this interval is $d-1$, and the final carry is one. The telescoping identity is $$\sum_{u=i}^{N-1}e_ud^{u-i}
       =Pr-1-\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}.
 \label{eq:suffix-weight}$$ For the target and $i\le S$, the left side equals $PDd^{S-i}-1$. Thus $$Pr=PDd^{S-i}+\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}.
 \label{eq:loss-identity}$$ This is an equality of nonnegative integers. Since $r\le D$ and $i\le S$, it forces $$i=S,\qquad r=D,\qquad \kappa_u=0\quad(i\le u<N).
 \label{eq:unique-source}$$

The remaining path exists and is unique. Before the mark, the long-block digits force the baseline transitions. At site zero, the outgoing carry is $P-1$, equal to its quotient, and the anchor is $d-P+1$. The mark resets the carry to zero. At the source $S$, ordinary base-$d$ division of $PD-1$ gives exactly the target digits at $S,\ldots,S+m$. After those digits, the suffix carry is one, producing all later zeros and the final carry in [\[eq:common-cut\]](#eq:common-cut){reference-type="eqref" reference="eq:common-cut"}. At every step the outgoing carry equals the quotient; every binomial weight is one.

Including $\alpha$ from [\[eq:marked-formula\]](#eq:marked-formula){reference-type="eqref" reference="eq:marked-formula"} and $a_D^P$ from the leading term of $v^P$, this unique path contributes $\alpha a_D^P$. All old paths were paired, so [\[eq:marked-difference\]](#eq:marked-difference){reference-type="eqref" reference="eq:marked-difference"} follows. This proves [\[prop:marked-difference\]](#prop:marked-difference){reference-type="ref" reference="prop:marked-difference"} with all marks, source positions, constant terms, and wraparound branches accounted for.

## Completion of both main theorems

Fix $M\ge1$ and set $$m=\lfloor\log_d(PM)\rfloor,\quad L=m+2,\quad
 s=4L+4,\quad n=s+3L+4=7m+22=n_H.$$ Suppose the two Hasse tests in [1](#tab:tests){reference-type="ref" reference="tab:tests"} hold. Normalize $h=\Delta_fQ+v$. By [\[eq:telescoping-jacobian\]](#eq:telescoping-jacobian){reference-type="eqref" reference="eq:telescoping-jacobian"} and [\[eq:frobenius-trace\]](#eq:frobenius-trace){reference-type="eqref" reference="eq:frobenius-trace"}, the tests become $$J_j\mathcal H_j(v^P)=0\quad\text{in }\mathcal A_j,
                    \qquad j=n,n+1.
 \label{eq:two-hasse-tests}$$ If $v$ has positive leading degree $D$, both coefficients in [\[eq:marked-difference\]](#eq:marked-difference){reference-type="eqref" reference="eq:marked-difference"} are zero by [\[eq:two-hasse-tests\]](#eq:two-hasse-tests){reference-type="eqref" reference="eq:two-hasse-tests"}. This contradicts $\alpha a_D^P\ne0$. Hence $v=a_0$ is constant.

At least one of $n,n+1$, say $j$, is not divisible by $p$. Every univariate term in the marked formula [\[eq:marked-formula\]](#eq:marked-formula){reference-type="eqref" reference="eq:marked-formula"} has degree $d^j-P$ and leading coefficient one before multiplication by $\alpha$. For a mark at $t$, the degree calculation is $$P(d^t-1)+(d-P)d^t+(d^j-d^{t+1})=d^j-P.$$ Thus the leading term of $D^{[P]}F_j$ is $j\alpha x^{d^j-P}$, nonzero and of degree below $\deg F_j$. Since $(ja_0)^P=ja_0^P$, the remaining divisibility is $$F_j\mid ja_0^PD^{[P]}F_j.$$ It forces $a_0=0$. Therefore the two Hasse tests imply $h\in B_f$.

Conversely, a polynomial coboundary satisfies [\[eq:polynomial-telescoping\]](#eq:polynomial-telescoping){reference-type="eqref" reference="eq:polynomial-telescoping"}, so it satisfies both the ordinary-root tests and the Hasse tests. Ordinary-root vanishing implies the Hasse tests by [\[lem:root-certificates\]](#lem:root-certificates){reference-type="ref" reference="lem:root-certificates"}. This proves the three-way finite equivalence in the last regime. For $h\in K_f$, formula [\[eq:ordinary-repetition\]](#eq:ordinary-repetition){reference-type="eqref" reference="eq:ordinary-repetition"} supplies those tests, proving $K_f=B_f$. The zero polynomial is covered by $Q=v=0$ throughout.

If a finite ordinary-root test fails at return $j=n$ or $n+1$, then [\[eq:ordinary-repetition\]](#eq:ordinary-repetition){reference-type="eqref" reference="eq:ordinary-repetition"} gives a primitive cycle with nonzero sum and period dividing $j$. Finally, $$\deg F_j\le d^{n+1}=d^{7m+23}\le d^{23}(PM)^7.$$ Together with [4](#sec:jacobian){reference-type="ref" reference="sec:jacobian"}, this proves [\[thm:rigidity,thm:finite\]](#thm:rigidity,thm:finite){reference-type="ref" reference="thm:rigidity,thm:finite"} for every prime and every degree.

## The characteristic-two boundary

The proof has used $P\ge2$, $P<d$, and $d-1>1$, not oddness of $p$. When $p=2$ and $d$ is odd, $\alpha=1$ and these inequalities hold. In the smallest case $d=3$, $P=2$, the anchor digit $d-P+1=2$ equals the long-block digit $d-1=2$. No argument required these digits to be different. The adaptive cut target two still exceeds every overflow outcome, which is at most one. The fixed-cut digit remains below $d$, and $(2D-1)\bmod3\le1$ for a normal leading degree retains the strict comparison at the first post-block site. The coefficient identity remains $C(n+1,s+1)-C(n,s)=a_D^P\ne0$.

For even $d$ in characteristic two, [\[eq:derivative-zero\]](#eq:derivative-zero){reference-type="eqref" reference="eq:derivative-zero"} reads $F_j'=1$, and the direct proof in [4](#sec:jacobian){reference-type="ref" reference="sec:jacobian"} applies. The range $p\nmid d(d-1)$ has no characteristic-two instance. These observations verify that the three rows of [1](#tab:tests){reference-type="ref" reference="tab:tests"} are disjoint and exhaustive without losing constants, non-prime-field coefficients, or ordinary wild periods.

# Consequences and limits of the certificates {#sec:consequences}

## Polynomial shears and native additive returns

The cohomological equation has a direct interpretation for the polynomial map of the full affine plane $$T_h(x,y)=(f(x),y+h(x)).$$ If $h=\Delta_fQ$, the polynomial automorphism $\Phi_Q(x,y)=(x,y-Q(x))$ satisfies $$\Phi_Q\circ T_h\circ\Phi_Q^{-1}(x,y)=(f(x),y).$$ Conversely, this identity for such a shear forces $h=Q\circ f-Q$. Thus [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"} identifies the complete ordinary additive obstruction to removing the vertical increment by a polynomial shear. It does not assert that the noninvertible base map or the skew map has a global inverse.

For a primitive base cycle $O$ of length $r$ and $a\in O$, direct iteration gives $$T_h^{\circ r}(a,y)=(a,y+S_h(O)).$$ Every return above that cycle has length divisible by $r$. Translation by a nonzero scalar has additive order $p$ in $k$, so the lifted primitive period is $r$ when $S_h(O)=0$ and $pr$ otherwise. No division by a period is involved, even when $p\mid r$. These return formulas explain the observable in the theorem; the polynomial regularity conclusion is the content of the preceding coefficient proof.

## Why the derivative regimes cannot be merged

[\[ex:blind-jacobian\]]{#ex:blind-jacobian label="ex:blind-jacobian"} Suppose $d\equiv1\pmod p$, take $c=0$, and let $h=x$. For every $n\ge1$, $$F_n=xR_n,\qquad R_n=x^{d^n-1}-1,
 \qquad F_n'=R_n.$$ The last equality uses the scalar identity $d^n=1$ in $k$. Since $x\mid H_n(x)$, every ordinary-Jacobian test $F_n\mid F_n'H_n(x)$ holds. Nevertheless $1$ is a fixed point with ordinary sum $1\ne0$, and $x\notin B_f$ by [\[lem:normal\]](#lem:normal){reference-type="ref" reference="lem:normal"}. Thus even all those Jacobian tests cannot replace the Hasse row of [1](#tab:tests){reference-type="ref" reference="tab:tests"}.

This is a failure of a proposed test, not a counterexample to [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"}. More generally, at a root of multiplicity $e$ divisible by $p$, the derivative of $(x-a)^eV(x)$ has order at least $e$ and may annihilate a nonvanishing value in the full quotient. Our proofs use only the valid necessary root-to-derivative implication, followed by a comparison at two carefully chosen levels. They do not claim a single-level converse in the possibly nonreduced regime.

## Scope and further questions

The result is an exact equality for polynomial observables over $\overline{\mathbb F}_p$ and the full family $x^d+c$. The two-return certificate and the shear interpretation are consequences of that same equality. We have not extended the observable class to rational functions, the base family to arbitrary polynomials, or the assertion to a different clock. The proof also gives no optimized period cutoff or running-time bound. In particular, a smaller iterate-degree bound would require a separate argument; it does not follow by replacing the three derivative regimes with one cost estimate.

The algebraic mechanism isolates what must be controlled for such extensions: a normal representative must be detected in a full periodic algebra, ordinary roots must supply a valid annihilation condition there, and an exact relation between different return levels must eliminate the possible defect. The stable carry and marked-insertion identities accomplish these steps here without a bound on periodic-root multiplicities.

#### Preparation and review disclosure.

This article was prepared with AI assistance. Its underlying proof packages received current-team internal mathematical and source checks. This version is the author draft for separate manuscript review; those internal checks are not external peer review or publication acceptance. The argument is proof-only, and no empirical computation is used as evidence for its infinite or all-parameter assertions.
