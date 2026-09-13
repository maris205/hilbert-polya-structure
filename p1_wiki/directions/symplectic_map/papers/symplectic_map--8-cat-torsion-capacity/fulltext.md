---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--8-cat-torsion-capacity"
canonical_tex: "symplectic_map/papers/8-cat-torsion-capacity/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/8-cat-torsion-capacity/paper/manuscript.pdf"
source_sha256: "95ebccff1eb5f2b939be92c9a8b7020b625d4b8056cc5b6bda3b3814fcae580c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Primitive-Divisor Audit of Prime-Order Torsion Periods for Hyperbolic Toral Automorphisms

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/8-cat-torsion-capacity>)
- [规范 TeX](<../../../../../symplectic_map/papers/8-cat-torsion-capacity/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/8-cat-torsion-capacity/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/8-cat-torsion-capacity/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/8-cat-torsion-capacity/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a hyperbolic matrix $M\in\mathrm{SL}_2(\mathbb{Z})$, we ask which prescribed dynamical periods can be carried by a torus point of prime additive order. A primitive rational prime divisor of $\det(M^n-I)$ produces such a point of exact period $n$. Flatters' primitive-divisor theorem therefore gives every period $n>12$ when $\operatorname{tr}M>2$. We extend the corollary to $\operatorname{tr}M<-2$ by a separate three-case parity argument for $B=-M$. The case $n\equiv2\pmod4$ requires a primitive divisor at index $n/2$, not at index $n$. For the standard cat matrix $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$, an exact prime-order carrier exists precisely when $n\notin\{1,6,12\}$. The nonprimitive period-ten case is repaired by the nilpotent Jordan structure modulo five, which gives twenty points in two ten-cycles. Finally, all periodic points of the cat map are torsion, and the invariant label $L(x)=\log\operatorname{ord}(x)$ realizes every positive integer after exponentiation. This is capacity without specificity: $L$ treats primes and composites identically, is locally unbounded on torsion, yields $n\log p$ rather than $\log p$ as its unnormalized orbit sum, and is invisible to derivative monodromy at fixed period.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'Pre-review manuscript, August 14, 2026'
title: |
  A Primitive-Divisor Audit of Prime-Order Torsion Periods\
  for Hyperbolic Toral Automorphisms
```

## Markdown 正文

**Keywords:** hyperbolic toral automorphism; Arnold cat map; primitive prime divisor; torsion point; exact period; arithmetic dynamics.

# Introduction {#sec:introduction}

Let $T_M\colon\mathbb{T}^{2}\to\mathbb{T}^{2}$ be the automorphism induced by a hyperbolic matrix $M\in\mathrm{SL}_2(\mathbb{Z})$. The bounded question of this note is: for a prescribed least dynamical period $n$, does there exist a nonzero periodic point whose additive group order is a rational prime? Additive order and dynamical period are independent attributes. Keeping them separate distinguishes the question from the total fixed-point count $\lvert\det(M^n-I)\rvert$, from the order of a matrix on one fixed rational lattice, and from the unconstrained existence of a period- $n$ point.

For that unconstrained baseline, Kannan et al. show that the ordinary period set of a hyperbolic two-torus automorphism is either $\mathbb{N}$ or $\mathbb{N}\setminus\{2\}$ [@KannanEtAl2011Periods], while Seibt develops a period formula for torus automorphisms on rational lattices [@Seibt2003Period]. Neither result imposes prime additive order; that extra constraint is the bounded distinction studied here.

Arithmetic descriptions of cat-map orbits have long used modular and ideal theory [@PercivalVivaldi1987Arithmetic; @Gaspari1994Arnold]. Matrix periods on rational lattices and local or global orbit counts supply further context [@DysonFalk1992Period; @BaakeRobertsWeiss2008Periodic; @BaakeNeumaerkerRoberts2013Orbit]. The arithmetic engine used here comes from a different direction: Flatters proved uniform primitive-divisor results for norm sequences of positive quadratic units [@Flatters2009Primitive]. The carrier theorem below is a short corollary of that theorem for positive trace, followed by an elementary but essential parity conversion for negative trace.

We record four conclusions. First, every hyperbolic $M\in\mathrm{SL}_2(\mathbb{Z})$ carries a prime-additive-order point of each exact period $n>12$. Second, for the standard cat map the exact exception set is $\{1,6,12\}$. Period ten exists despite the absence of a primitive divisor at that index. Third, the proposed torsion-order clock has full integer capacity and no prime specificity. Fourth, a single registered exact audit over $n=1,\ldots,12$ corroborates the finite ledger and the small finite-field profiles without computing any period above twelve. The infinite tail is proof-derived, not extrapolated from a finite scan.

Recent work on permutation maps over $\mathbb{Z}/p^k\mathbb{Z}$ gives neighboring fixed-residue-ring cycle information [@TanLi2025Graph]. A recent preprint for the same cat map studies arithmetic landscape and transparent Green/transfer identities [@Chandra2026Arithmetic]. Those results, together with the classical dynamical-zeta literature [@Ruelle1976Zeta; @ParryPollicott1990Zeta], make broad spectral novelty claims inappropriate here. Quantum cat maps form another established theory [@HannayBerry1980Quantization; @KurlbergRudnick2000Hecke]. The present arguments are classical and produce no quantum operator or eigenstate statement.

The scope is deliberately narrow. We derive and audit carrier existence. We do not construct a prime-orbit bijection, an Euler product, a transfer or Fredholm determinant, a trace formula, a quantization, or a prime/zero matching. Primitive divisibility is used as a sufficient criterion, not a necessary one. Section [2](#sec:preliminaries){reference-type="ref" reference="sec:preliminaries"} fixes notation and attribution. Section [3](#sec:uniform){reference-type="ref" reference="sec:uniform"} proves the uniform theorem, including the negative-trace parity lemma. Section [4](#sec:cat){reference-type="ref" reference="sec:cat"} gives the sharp cat classification. Section [5](#sec:clock){reference-type="ref" reference="sec:clock"} proves the capacity-versus- specificity obstruction, and Section [6](#sec:audit){reference-type="ref" reference="sec:audit"} describes the exact audit and its provenance boundary.

# Arithmetic and dynamical preliminaries {#sec:preliminaries}

Write $$T_M(x)=Mx\pmod{\mathbb{Z}^2},\qquad
  \Delta_n(M)=\det(M^n-I),\qquad
  V_p=(\mathbb{Z}/p\mathbb{Z})^2.
  \label{eq:notation}$$ A nonzero vector $v\in V_p$ represents the torus point $x_v=v/p\pmod{\mathbb{Z}^2}$, which has exact additive order $p$. The *period* of $x$ is its least positive return time under $T_M$.

Let $(a_j)_{j\ge1}$ be a sequence of nonzero integers. A rational prime $p$ is a *primitive prime divisor* of $a_n$ when $p\mid a_n$ and $p\nmid a_j$ for every $1\le j<n$. For determinant sequences we apply the same definition after omitting any zero earlier term. Hyperbolicity ensures that $\Delta_j(M)\ne0$ for every $j\ge1$.

The aggregate identity $$\#\operatorname{Fix}(T_M^n)=\lvert\Delta_n(M)\rvert
  \label{eq:fixed-count}$$ is useful background, but it does not identify the additive order or least period of any individual point. Prime-lattice orbit decompositions, global matrix order, and rational-lattice zeta counts answer related but different questions [@Gaspari1994Arnold; @DysonFalk1992Period; @BaakeRobertsWeiss2008Periodic]. Our bridge is the elementary kernel lemma in Section [3](#sec:uniform){reference-type="ref" reference="sec:uniform"}.

For a positive quadratic unit $\alpha$, the associated Lehmer--Pierce sequence is $$\operatorname{N}_{\mathbb{Q}(\alpha)/\mathbb{Q}}(\alpha^n-1).$$ We use two results of Flatters [@Flatters2009Primitive]: for a positive quadratic unit of norm one, every index $n>12$ has a primitive rational prime divisor, and the complete norm-one small-index classification shows that indices $7,9,11$ are never exceptions. These are imported arithmetic statements. The kernel conversion, all matrix-period arguments, and the negative-trace reduction below are derived here. In particular, Flatters is not cited as proving the negative-trace toral theorem.

# Prime-order carriers above the uniform threshold {#sec:uniform}

## The primitive-kernel bridge

[\[lem:primitive-kernel\]]{#lem:primitive-kernel label="lem:primitive-kernel"} Suppose $p$ is a primitive prime divisor of $\Delta_n(M)$. Every nonzero vector in $\operatorname{ker}(M^n-I\colon V_p\to V_p)$ represents a torus point of additive order $p$ and exact $T_M$-period $n$. If the kernel has dimension $r\in\{1,2\}$, it supplies exactly $$\frac{p^r-1}{n}
  \label{eq:cycle-count}$$ distinct primitive cycles.

The divisibility $p\mid\det(M^n-I)$ makes $M^n-I$ singular over $\mathbb{F}_p$, so the kernel contains a nonzero $v$. The point $x_v=v/p$ has additive order $p$ and is fixed by $T_M^n$. Its least period $d$ divides $n$. If $d<n$, then $(M^d-I)v=0$, hence $p\mid\Delta_d(M)$, contrary to primitivity. Thus $d=n$.

The kernel is invariant under $M$, because $M$ commutes with $M^n-I$. All of its $p^r-1$ nonzero vectors have exact period $n$ and partition into disjoint $n$-element orbits. This proves [\[eq:cycle-count\]](#eq:cycle-count){reference-type="eqref" reference="eq:cycle-count"}.

No diagonalization, splitting, or unramifiedness assumption is needed in Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"}. It also covers $p=2$ and both possible kernel dimensions.

## Positive trace

[\[prop:positive\]]{#prop:positive label="prop:positive"} If $M\in\mathrm{SL}_2(\mathbb{Z})$ and $\operatorname{tr}M>2$, then $T_M$ has a point of prime additive order and exact period $n$ for every $n>12$.

Set $t=\operatorname{tr}M$. The expanding eigenvalue $$\alpha=\frac{t+\sqrt{t^2-4}}2>1$$ is a positive quadratic unit of norm one, with conjugate $\alpha^{-1}$. Consequently $$\begin{aligned}
  \operatorname{N}_{\mathbb{Q}(\alpha)/\mathbb{Q}}(\alpha^n-1)
  &=(\alpha^n-1)(\alpha^{-n}-1) \\
  &=2-\alpha^n-\alpha^{-n}
   =\det(M^n-I)=\Delta_n(M).
  \label{eq:norm-det}\end{aligned}$$ Flatters' norm-one theorem gives a primitive rational prime divisor of this integer for every $n>12$ [@Flatters2009Primitive Theorem 1.4]. Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"} supplies the carrier.

## Negative trace: the three-case parity conversion

The direct citation in Proposition [\[prop:positive\]](#prop:positive){reference-type="ref" reference="prop:positive"} does not cover a negative expanding eigenvalue. Let $M\in\mathrm{SL}_2(\mathbb{Z})$ have $\operatorname{tr}M<-2$, and put $B=-M$. Then $B\in\mathrm{SL}_2(\mathbb{Z})$ has positive trace, so its determinant sequence has the primitive divisors just used. The index to use depends on the parity of the requested $M$-period.

::: {#tab:negative-routing}
  Requested $M$-period   primitive index for $B$   decisive relation
  ---------------------- ------------------------- --------------------------
  $n$ odd                $2n$                      $B^n v=-v$
  $4\mid n$              $n$                       $n\nmid2m$ for odd $m<n$
  $n=2k$, $k$ odd        $k=n/2$                   $p\ne2$ and $M^kv=-v$

  : Primitive index for the negative-trace conversion. The third row is the half-index repair. Using index $n$ there can produce an unwanted half-period under $M=-B$.
:::

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} Let $M\in\mathrm{SL}_2(\mathbb{Z})$ satisfy $\lvert\operatorname{tr}M\rvert>2$. For every integer $n>12$, the automorphism $T_M$ has a point of prime additive order and exact dynamical period $n$.

Proposition [\[prop:positive\]](#prop:positive){reference-type="ref" reference="prop:positive"} handles $\operatorname{tr}M>2$. Assume $\operatorname{tr}M<-2$ and write $B=-M$.

If $n$ is odd, choose a primitive prime divisor $p$ of $\Delta_{2n}(B)$, which exists because $2n>12$. Choose $0\ne v\in\operatorname{ker}(B^{2n}-I)$. Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"} gives exact $B$-period $2n$. Primitivity at $2n$ implies $p\nmid\Delta_n(B)$, so $B^n-I$ is invertible on $V_p$. The factorization $$(B^n-I)(B^n+I)v=(B^{2n}-I)v=0$$ therefore yields $B^nv=-v$. This also forces $p\ne2$, since in characteristic two it would contradict exact $B$-period $2n$. As $n$ is odd, $M^nv=(-B)^nv=v$. A smaller return $M^mv=v$, $0<m<n$, would imply $B^{2m}v=v$. Exact $B$-period $2n$ would then give $2n\mid2m$, impossible.

Suppose next that $4\mid n$. Choose a primitive divisor of $\Delta_n(B)$ and a nonzero $v$ of exact $B$-period $n$. Since $n$ is even, $M^nv=B^nv=v$. If $M^mv=v$ for $m<n$, then an even $m$ gives $B^mv=v$, contradicting exact $B$-period. An odd $m$ gives $B^mv=-v$, hence $B^{2m}v=v$ and $n\mid2m$. Writing $n=4q$ shows that the even integer $2q$ would divide the odd integer $m$, again impossible.

It remains that $n=2k$ with $k$ odd. Here $k\ge7$. A primitive prime divisor $p$ of $\Delta_k(B)$ exists by Flatters' uniform theorem when $k>12$. The remaining indices $k=7,9,11$ are nonexceptional by the complete norm-one classification [@Flatters2009Primitive Theorem 3.1]. The prime $p$ cannot be two. Indeed, $B\bmod2$ permutes the three nonzero vectors of $\mathbb{F}_2^2$. A nonzero vector fixed by $B^k$ has exact $B$-period $d\in\{1,2,3\}$ dividing the odd integer $k$, so $d\in\{1,3\}<k$. Then $2\mid\Delta_d(B)$, contradicting primitivity at $k$.

Choose $v$ of exact $B$-period $k$. We have $M^{2k}v=B^{2k}v=v$. If $M^mv=v$ for some $0<m<2k$, an even $m$ yields $B^mv=v$, hence $k\mid m$. No positive even multiple of the odd number $k$ is below $2k$. An odd $m$ yields $B^mv=-v$, so $B^{2m}v=v$ and $k\mid m$. The only possible odd multiple below $2k$ is $m=k$, but $M^kv=-B^kv=-v\ne v$ because $p$ is odd. Thus the exact $M$-period is $2k=n$.

These cases exhaust all $n>12$.

[\[rem:half-index\]]{#rem:half-index label="rem:half-index"} For $n=2k$ with $k$ odd, a primitive divisor at index $n$ does not give the requested conclusion. A resulting vector of exact $B$-period $2k$ satisfies $B^kv=-v$, because $B^k-I$ is invertible modulo the primitive prime and $(B^k-I)(B^k+I)v=0$. Then $M^kv=(-B)^kv=-B^kv=v$, so its $M$-period already divides $k=n/2$. Selecting at index $k$, and separately proving $p\ne2$, is therefore essential.

![From primitive determinant divisors to prescribed prime-order periods. Flatters supplies primitive rational primes for positive norm-one quadratic units. Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"} converts a primitive divisor to exact finite-field and torus period. For negative trace, the conversion through $B=-M$ is separate and uses primitive indices $2n$, $n$, and $n/2$ in the three parity branches. The certified tail $n>12$ is proof-derived. No tail period was computed.](figures/fig1_carrier_bridge.pdf){#fig:primitive-bridge width="99%"}

# The standard cat: an exact boundary and a Jordan repair {#sec:cat}

Fix $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad \operatorname{tr}A=3.
  \label{eq:cat}$$ If $s_n=\operatorname{tr}(A^n)$, then $s_0=2$, $s_1=3$, and $$s_{n+2}=3s_{n+1}-s_n,\qquad \Delta_n(A)=2-s_n.
  \label{eq:trace-recurrence}$$ The exact ledger in Table [2](#tab:ledger){reference-type="ref" reference="tab:ledger"} agrees term by term with direct integer matrix powers and with the standard-unit small table of @Flatters2009Primitive [Theorem 3.1 and its proof table]. A "new divisor" means a primitive determinant divisor. The carrier column is logically separate, because period ten has a carrier without such a divisor.

::: {#tab:ledger}
    $n$   $\Delta_n$ exact factorization     new divisor  carrier conclusion
  ----- ------------ ---------------------- ------------- ----------------------
      1         $-1$ $-1$                        --       excluded
      2         $-5$ $-5$                         5       $p=5$
      3        $-16$ $-2^4$                       2       $p=2$
      4        $-45$ $-3^2\cdot5$                 3       $p=3$
      5       $-121$ $-11^2$                     11       $p=11$
      6       $-320$ $-2^6\cdot5$                --       excluded
      7       $-841$ $-29^2$                     29       $p=29$
      8      $-2205$ $-3^2\cdot5\cdot7^2$         7       $p=7$
      9      $-5776$ $-2^4\cdot19^2$             19       $p=19$
     10     $-15125$ $-5^3\cdot11^2$             --       $p=5$, Jordan repair
     11     $-39601$ $-199^2$                    199      $p=199$
     12    $-103680$ $-2^8\cdot3^4\cdot5$        --       excluded

  : Standard-cat determinant, factor, and carrier ledger for $1\le n\le12$. The factors and finite-field classifications were checked exactly in the registered audit.
:::

Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"} immediately gives carriers at $n=2,3,4,5,7,8,9,11$. Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"} gives all $n>12$. Four small indices remain.

[\[prop:jordan\]]{#prop:jordan label="prop:jordan"} On $V_5\setminus\{0\}$, the cat matrix has four points of exact period two and twenty points of exact period ten. The latter form two primitive ten-cycles.

Over $\mathbb{F}_5$, put $$N=A+I=\begin{pmatrix}3&1\\1&2\end{pmatrix}.$$ Direct multiplication gives $N^2=0$, while $N\ne0$ and $\operatorname{rank}N=1$. Since $A=-I+N$, the binomial expansion truncates: $$A^j=(-1)^jI+j(-1)^{j-1}N.
  \label{eq:jordan-power}$$ For $0\ne v\in\operatorname{ker}N$, one has $Av=-v$, so $v$ has exact period two. The one-dimensional kernel has five vectors, hence four nonzero period-two points.

Now suppose $Nv\ne0$ and $A^jv=v$. If $j$ is even, [\[eq:jordan-power\]](#eq:jordan-power){reference-type="eqref" reference="eq:jordan-power"} gives $jNv=0$, so $5\mid j$. If $j$ is odd, it gives $jNv=2v$. Applying $N$ yields $0=2Nv$, a contradiction. Therefore the least return is ten. Exactly $25-5=20$ vectors lie outside $\operatorname{ker}N$, and division by ten gives two cycles.

For completeness, the other relevant support primes admit equally short classifications. Modulo two, $$A=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad A^3=I,$$ and $A-I$ is invertible, so all three nonzero vectors have exact period three. Modulo three, $A^2=-I$, while $A-I$ is invertible. All eight nonzero vectors have exact period four.

[\[thm:cat\]]{#thm:cat label="thm:cat"} For the matrix $A$ in [\[eq:cat\]](#eq:cat){reference-type="eqref" reference="eq:cat"}, a nonzero torus point of prime additive order and exact dynamical period $n$ exists if and only if $$n\notin\{1,6,12\}.$$ Period ten is carried by order-five points but has no primitive prime divisor in the determinant sequence.

Existence outside $\{1,6,10,12\}$ follows from the primitive divisors in Table [2](#tab:ledger){reference-type="ref" reference="tab:ledger"} and from Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"}, while Proposition [\[prop:jordan\]](#prop:jordan){reference-type="ref" reference="prop:jordan"} supplies $n=10$.

For $n=1$, $\det(A-I)=-1$, so $A-I$ is invertible modulo every prime. If a prime-order point had period six, its order prime would divide $\Delta_6$, whose support is $\{2,5\}$. The complete profiles above give period three modulo two and periods two or ten modulo five. None is six. Similarly, the support of $\Delta_{12}$ is $\{2,3,5\}$. The possible nonzero periods are respectively three, four, and two or ten. None is twelve.

The failure at $n=12$ makes the uniform bound in Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"} sharp: a smaller integer threshold would include period twelve for this hyperbolic matrix. The success at $n=10$ also separates two exception sets. Primitive divisors fail at $1,6,10,12$, whereas prime-order carriers fail only at $1,6,12$.

![The exact standard-cat boundary for $1\le n\le12$. Primitive divisors certify the ordinary positive cases. Period ten is instead repaired by the modulo-five Jordan calculation: twenty points form two primitive ten-cycles. The determinant supports and complete profiles $p=2:\{3:3\}$, $p=3:\{4:8\}$, and $p=5:\{2:4,10:20\}$ exclude precisely $1,6,12$.](<../../../../../symplectic_map/papers/8-cat-torsion-capacity/paper/figures/fig2_standard_cat_boundary.pdf>){#fig:cat-boundary width="99%"}

# Capacity is not specificity {#sec:clock}

The carrier classification might suggest using additive order as an arithmetic clock. The next theorem gives the exact scope of that idea and its obstruction.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For any hyperbolic $A\in\mathrm{SL}_2(\mathbb{Z})$, $$\operatorname{Per}(T_A)=\operatorname{Tor}(\mathbb{T}^{2}).
  \label{eq:per-tor}$$ On this set define $L(x)=\log\operatorname{ord}(x)$. Then:

1.  $L(Ax)=L(x)$, and $\exp L(\operatorname{Per}(T_A))=\mathbb{N}$.

2.  $L$ is unbounded in every relative neighborhood of every torsion point and discontinuous at every point of its domain.

3.  if $x$ has additive order $p$ and exact period $n$, then $S_nL(x)=n\log p$, while an $r$-fold traversal gives $S_{rn}L(x)=rn\log p$.

4.  $D(T_A^n)_x=A^n$ is independent of $x$ and hence cannot read the carrier prime at fixed period.

If $x$ has additive order $m$, then $x$ lies in the finite group $\mathbb{T}^{2}[m]$. The unimodular matrix $A$ permutes this group, so $x$ is periodic. Conversely, if $A^nx=x$ and $\widetilde x\in\mathbb R^2$ is a lift, then $$(A^n-I)\widetilde x\in\mathbb{Z}^2.$$ Hyperbolicity excludes the eigenvalue one from $A^n$. Thus $A^n-I$ is a nonsingular integer matrix and its inverse is rational, which forces $\widetilde x\in\mathbb{Q}^2$. This proves [\[eq:per-tor\]](#eq:per-tor){reference-type="eqref" reference="eq:per-tor"}.

Both $A$ and $A^{-1}$ have integer entries. If $x$ has order $m$, then $\operatorname{ord}(Ax)\mid m$. Applying the same argument to $A^{-1}$ gives the reverse divisibility. Hence order, and therefore $L$, is orbit-invariant. The point $$x_m=(1/m,0)\pmod{\mathbb{Z}^2}$$ has exact additive order $m$ and is periodic by [\[eq:per-tor\]](#eq:per-tor){reference-type="eqref" reference="eq:per-tor"}. Every positive integer occurs, with no distinction between primes and composites.

Fix a torsion point $x$ of order $m$, choose $N_k=km+1$, and set $y_k=x+(1/N_k,0)$. Then $y_k\to x$ and $\gcd(N_k,m)=1$. If $qy_k=0$, multiplication first by $N_k$ and then by $m$ gives $m\mid q$ and $N_k\mid q$. Coprimality implies $mN_k\mid q$, while $mN_k y_k=0$ is immediate. Therefore $$\operatorname{ord}(y_k)=mN_k,\qquad L(y_k)=\log(mN_k)\longrightarrow\infty.
  \label{eq:clock-unbounded}$$ This proves local unboundedness and discontinuity on the relative torsion topology. Since torsion is dense, every nonempty torus open set contains such witnesses. In particular, $L$ has no continuous or Hölder extension to $\mathbb{T}^{2}$.

Orbit invariance gives $$S_nL(x)=\sum_{j=0}^{n-1}L(T_A^jx)=nL(x).$$ For order $p$ this is $n\log p$, and repeating the orbit $r$ times multiplies the sum by $r$. Finally, linearity gives $D(T_A^n)_x=A^n$ at every point. If $\rho(A)>1$ denotes the spectral radius, then the logarithm of the modulus of the unstable multiplier is $n\log\rho(A)$, and contains no dependence on $p$.

The raw orbit label $\log p$, the normalized orbit average, the unnormalized sum $n\log p$, and the native unstable log-multiplier $n\log\rho(A)$ are different objects. Dividing a point weight by the least return time can force the sum to equal $\log p$, but the denominator is global orbit information. It does not define a fixed local continuous potential. The same warning applies to orbit selection: selecting one carrier after the fact is an external rule, not an intrinsic consequence of the order clock.

![Capacity versus specificity of the torsion-order clock. The witnesses $x_m=(1/m,0)$ realize prime and composite orders by the same construction. At a frozen order-18 point, coprime perturbation denominators $19,55,127$ give exact orders $342,990,2286$, illustrating the general proof of local unboundedness. On an order-five, period-ten carrier, $S_{10}L=10\log5$ and repetitions scale this sum, whereas $A^{10}=\left(\begin{smallmatrix}10946&6765\\6765&4181
  \end{smallmatrix}\right)$ and its characteristic polynomial $X^2-15127X+1$ depend on the period but not on torsion order.](<../../../../../symplectic_map/papers/8-cat-torsion-capacity/paper/figures/fig3_capacity_specificity.pdf>){#fig:capacity-specificity width="99%"}

# Exact audit and falsification controls {#sec:audit}

The computational component was an exact consistency audit of frozen mathematics, not a numerical discovery experiment. One registered run evaluated precisely $n=1,\ldots,12$. It used no external prime table, generated prime-target array, Riemann-zero data, floating comparison, parameter search, or period above twelve. Direct matrix powers and the recurrence [\[eq:trace-recurrence\]](#eq:trace-recurrence){reference-type="eqref" reference="eq:trace-recurrence"} agreed at all twelve indices, as did every exact factorization and every locked finite-field count. All residuals were exactly zero. Stochastic error bars are inapplicable.

::: {#tab:profiles}
    $p$   nonzero vectors exact-period profile (period: points)     residual
  ----- ----------------- --------------------------------------- ----------
      2                 3 $3:3$                                            0
      3                 8 $4:8$                                            0
      5                24 $2:4,\ 10:20$                                    0
      7                48 $8:48$                                           0
     11               120 $5:120$                                          0
     19               360 $9:360$                                          0
     29               840 $7:840$                                          0
    199            39,600 $11:39{,}600$                                    0

  : Complete registered finite-field profiles. The audit enumerated 41,003 nonzero vectors over the eight frozen support primes.
:::

The execution/proof firewall is substantive. The raw result records empty lists for periods above twelve and for tail computations. Sample indices used to test the three negative-trace branch contracts contain only symbolic branch bookkeeping, each marked as performing no matrix or orbit calculation. Thus Table [2](#tab:ledger){reference-type="ref" reference="tab:ledger"} checks the finite boundary, while Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"} alone supports the infinite tail.

The source lock, raw result, and final result manifest have SHA-256 digests

`87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269d`,\
`0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0`,\
`045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`,

respectively. A fresh independent result-integrity audit reproduced the twelve determinants, all finite-field profiles, the modulo-five counts, and the closed manifest inventory without rerunning the candidate. Its report digest is

`5f544f637ccbe9e9f584cfdd41a3188ab76153670bd5d3cdbc881ea5cbf2229d`.

These hashes identify the evidence used by this pre-review manuscript. They do not convert a finite audit into proof of the tail.

# Limitations, novelty boundary, and conclusion {#sec:conclusion}

Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"} has a precise novelty boundary. Its positive- trace part is an immediate Flatters corollary after the norm--determinant identity and Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"}. The negative-trace part is a separate parity conversion. Theorem [\[thm:cat\]](#thm:cat){reference-type="ref" reference="thm:cat"} is an exact synthesis of the primitive-divisor table, the kernel lemma, and small finite-field calculations. A bounded search completed on August 14, 2026 did not locate either packaged statement verbatim, but this is not evidence of priority. The appropriate verbs are *derive*, *record*, *audit*, and *synthesize*.

Several limitations are structural rather than technical. Primitive divisors are not necessary for carriers, as period ten demonstrates. The order clock realizes every composite order along with every prime order and is nowhere locally bounded on its natural dense domain. Its pointwise label does not acquire the desired repetition law until it is summed, at which point the extra factor $n$ appears. Native monodromy sees $n$ but not $p$. No argument here supplies canonical orbit selection, multiplicity compensation, amplitudes, signs, a prime-power law, a transfer determinant, or a quantization.

The correct conclusion is therefore two-sided. Hyperbolic toral automorphisms possess abundant intrinsic prime-order torsion carriers, with a sharp exact classification for the standard cat. That abundance does not make torsion order a prime-specific dynamical clock. In the route language that motivated the audit, the frozen decision is

`INTRINSIC_TORSION_CAPACITY_CERTIFIED / A0_FAIL_PROVES_TOO_MUCH`.

No Route-A layer beyond the failed A0 specificity gate, and no Route-B experiment, is opened by this note.

# Auxiliary exact identities {#app:identities}

For the standard cat matrix one may verify by induction that $$A^n=\begin{pmatrix}
    F_{2n+1} & F_{2n}\\
    F_{2n}   & F_{2n-1}
  \end{pmatrix},
  \label{eq:fibonacci}$$ where $F_0=0$, $F_1=1$. This is consistent with [\[eq:trace-recurrence\]](#eq:trace-recurrence){reference-type="eqref" reference="eq:trace-recurrence"} and gives a second exact route to the entries of Table [2](#tab:ledger){reference-type="ref" reference="tab:ledger"}. The registered audit instead treated direct matrix powers and the trace recurrence as independent exact engines and required termwise equality.

The primitive-kernel cycle count can also be read group-theoretically. If $K_{p,n}=\operatorname{ker}(A^n-I\colon V_p\to V_p)$, then $A$ acts freely on $K_{p,n}\setminus\{0\}$ in blocks of length $n$ whenever $p$ is primitive at index $n$. Hence $n\mid p^r-1$, where $r=\dim_{\mathbb{F}_p}K_{p,n}$. This divisibility is a consequence of exact period, not an extra hypothesis.

# Claim, evidence, and nonclaim map {#app:claim-map}

::: {#tab:claim-map}
  ID   Claim                                                                                             Evidence and boundary
  ---- ------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ID   Claim                                                                                             Evidence and boundary
  C1   Every hyperbolic $\mathrm{SL}_2(\mathbb{Z})$ matrix has a prime-order carrier for every $n>12$.   Flatters for positive norm-one units, the norm--determinant identity, Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"}, and the three-case $B=-M$ conversion. No tail computation.
  C2   A primitive determinant prime yields $(p^r-1)/n$ exact cycles.                                    Lemma [\[lem:primitive-kernel\]](#lem:primitive-kernel){reference-type="ref" reference="lem:primitive-kernel"}, using an elementary finite-field kernel and orbit partition.
  C3   The standard-cat exception set is $\{1,6,12\}$.                                                   Exact ledger, primitive-kernel bridge, complete modulo $2,3,5$ profiles, and Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"}.
  C4   Period ten is a nonprimitive repair.                                                              Proposition [\[prop:jordan\]](#prop:jordan){reference-type="ref" reference="prop:jordan"}: twenty order-five points and two ten-cycles.
  C5   The order clock has all-integer capacity and is locally unbounded.                                Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}. The same witness produces prime and composite orders.
  C6   Orbit sums and monodromy do not isolate $\log p$.                                                 Invariance gives $n\log p$. Linearity gives $D(T_A^n)=A^n$, independent of $p$.
  C7   A0 fails by proving too much.                                                                     Interpretation of C1--C6. No transfer, zeta, quantization, or prime/zero theorem is claimed.

  : Pre-review claim-to-evidence map.
:::

# Artifact and disclosure statements {#app:statements}

#### Data and code availability.

No external dataset was used. The exact source lock, implementation, registered raw result, validation reports, and final result manifest are archived in the accompanying Paper 8 project directory. The result inventory is closed by the manifest digest reported in Section [6](#sec:audit){reference-type="ref" reference="sec:audit"}. This manuscript is outside that frozen result inventory.

#### Ethics declaration.

The work uses no human participants, personal data, animals, or sensitive datasets. Human-subjects or animal-research approval is not applicable.

#### Author contributions.

For anonymous review, contributor identities are withheld. The authors are responsible for conceptualization, formal analysis, validation, writing, visualization oversight, and project administration.

#### Funding.

No external funding is declared in this anonymous pre-review version.

#### Conflicts of interest.

The authors declare no conflict of interest.

#### AI-assistance disclosure.

An AI system assisted with source-organized drafting, LaTeX formatting, and artifact bookkeeping under a frozen proof/result scope. No AI-generated citation was admitted without the separate metadata-and-role verification record, and no candidate computation was run during manuscript production. The authors retain responsibility for every statement. This package is explicitly awaiting a fresh independent manuscript review.
