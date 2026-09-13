---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-frobenius-scheme-obstruction"
canonical_tex: "henon_dynamics/henon_frobenius_scheme_obstruction/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_frobenius_scheme_obstruction/paper/main.pdf"
source_sha256: "0b2be01dfa30ae58bae071b7e29055ed6f38286051701119efa9d28425226da9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Zero-Dimensional Frobenius Obstruction for Periodic Schemes of an Area-Preserving Hénon Family

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_frobenius_scheme_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_frobenius_scheme_obstruction/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_frobenius_scheme_obstruction/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_frobenius_scheme_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_frobenius_scheme_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the fixed-period arithmetic of the area-preserving Hénon family $H_a(q,p)=(1-aq^2-p,q)$ while keeping chronological iteration and Frobenius extension degree as independent variables. The periodic-point scheme of $H_a^n$ admits a cyclic recurrence presentation whose equations form a monic Gröbner basis over $\mathbb Z[a,a^{-1}]$. It is therefore finite flat of rank $2^n$. This exact structure also gives an obstruction: at any finite reduced fiber, Frobenius acts only as a permutation of a zero-dimensional set. The fixed-$n$ local zeta is consequently a finite permutation determinant, all of its eigenvalues are roots of unity, and ordinary point counts ignore nilpotents and local intersection multiplicities. An exact certificate with 36 finite-field cells, eight unit tests, and an independent field implementation verifies the good-prime, ramified, and degree-drop cases. A matched reversible two-cycle control further proves that rectangular point counts do not determine a joint Frobenius/dynamical action even among reversible finite controls. Finally, a promising period-five sextic with Galois group $S_6$ is shown, coefficient by coefficient, to coincide with a published Hénon orbital polynomial. Thus fixed-period Frobenius rationality does not furnish a distinguished Hilbert--Pólya mechanism; any surviving arithmetic program must use genuinely joint actions or positive-dimensional parameter geometry.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 6, 2026'
title: |
  A Zero-Dimensional Frobenius Obstruction for Periodic Schemes\
  of an Area-Preserving Hénon Family
```

## Markdown 正文

# Introduction

Separating arithmetic time from dynamical time is necessary when a map is reduced modulo primes, but that separation does not by itself create a new zeta mechanism. This note makes the limitation explicit for the conservative quadratic recurrence $$\label{eq:henon}
 H_a(q,p)=(1-aq^2-p,q),
 \qquad q_{i+1}+q_{i-1}+a q_i^2-1=0.$$ The map has Jacobian determinant one and the rational reversor $R(q,p)=(p,q)$, with $RH_aR=H_a^{-1}$. It is a standard area-preserving Hénon normalization [@henon1969; @friedland1989].

For an integer $a$, a prime $p$, a Frobenius extension degree $r$, and a chronological period $n$, consider $$\label{eq:N}
 X_{a,n}=\operatorname{Fix}(H_a^n),\qquad
 N_{a,p}(r,n)=\#X_{a,n}(\mathbb F_{p^r}).$$ The indices in [\[eq:N\]](#eq:N){reference-type="eqref" reference="eq:N"} have different meanings: $n$ iterates the Hénon map, whereas $r$ iterates Frobenius. A previous finite-field experiment that identified these clocks had no cohomological justification. The natural repair was to hold $n$ fixed and construct the Hasse--Weil series in $r$.

The repair is mathematically coherent but too weak. We prove that the universal fixed scheme $\mathcal X_n$ is finite flat of rank $2^n$ over $\mathbb Z[a,a^{-1}]$. At a reduced finite-field fiber its entire $r$-dependence is the cycle type of one finite Frobenius permutation. Hence the desired trace decomposition and rational local zeta are automatic zero-dimensional facts, not anomalous evidence. Nonreduced fibers do not help because ordinary rational points and $\ell$-adic cohomology see only the reduction.

The obstruction has four concrete parts.

1.  We give a scheme-theoretic cyclic presentation and a monic Gröbner basis proof of finite flatness with rank exactly $2^n$.

2.  We distinguish coefficient degree-goodness from ètaleness and show that direct reduction at $p\mid a$, outside the inverted base, can make $\operatorname{Fix}(H_a^4)$ positive-dimensional.

3.  We prove that the fixed-$n$ local factor is a root-of-unity permutation determinant and that $N(r,n)$ loses the relative Frobenius/Hénon phase.

4.  We reproduce the first tempting period-five Galois signal and identify an exact collision with the Endler--Gallas sextic [@endler2006].

The conclusion is deliberately scoped. It rejects fixed-$n$ recurrence discovery as a Hilbert--Pólya route. It does not exclude arithmetic structure in higher-period Galois towers or in positive-dimensional parameter quotients.

# Setup and source boundaries

#### Polynomial automorphisms.

Friedland and Milnor prove that a cyclically reduced complex polynomial automorphism of degree $d$ has $d$ fixed points counted with local multiplicity; its $n$-th iterate has total multiplicity $d^n$ [@friedland1989 Theorem 3.1]. Their generic distinctness lemma is followed by explicit collision examples. Our integral finite-flat statement agrees with this complex count, but its proof is independent and works before choosing a field.

#### Frobenius zeta functions.

Grothendieck's trace formula expresses the zeta function of a finite-type scheme over a finite field through Frobenius on compactly supported $\ell$-adic cohomology [@grothendieck1965]. In dimension zero the theorem reduces to elementary permutation linear algebra. This reduction, rather than general rationality, is the main obstruction below.

#### Formal and primitive period.

Hutz develops dynatomic cycles for morphisms of nonsingular projective varieties and records the characteristic-dependent difference between formal and primitive period [@hutz2010]. A Hénon map extends birationally to $\mathbb P^2$, not as the projective morphism assumed there. We therefore use the affine fixed scheme directly and invoke set-level Möbius inversion only on reduced fibers. Diller--Favre's surface theory supplies the corresponding compactification caution [@diller2001].

#### Reversibility and higher-rank actions.

Reversibility imposes exact finite-field cycle identities [@roberts2005]; it must be matched by controls rather than interpreted as an arithmetic anomaly. Lind's $\mathbb Z^d$ zeta uses common fixed counts for every finite-index subgroup [@lind1996]. The table $N(r,n)$ samples only rectangular subgroups of the commuting Frobenius--Hénon action. Moreover, $\mathbb A^2(\overline{\mathbb F}_p)$ is not the compact metric phase space in Lind's analytic hypotheses. Walton's finite-field periodic zeta gives another warning: for an automorphism, every point of each finite phase space is periodic, so the union-over-all-periods count forgets the map [@walton2018]. Walton's Definition 4.6 also directly precedes our twisted counts by using $\#\operatorname{Fix}(gF_q^r)$ and character averages.

#### Low-period arithmetic.

Exact orbital polynomials for Hénon maps have a substantial history. Endler--Gallas treat period four arithmetically [@endler2002], and their 2006 paper already gives the period-five $Z$ sextic used below, its discriminant, and symmetric Galois group [@endler2006]. Brison--Gallas later publish transformations between the companion sextics [@brison2018]. These sources are a novelty firewall for the calculation in Section [5](#sec:certificate){reference-type="ref" reference="sec:certificate"}.

# Finite-flat periodic schemes

Let $B=\mathbb Z[A,A^{-1}]$ and let $H_A$ denote [\[eq:henon\]](#eq:henon){reference-type="eqref" reference="eq:henon"} over $B$.

[\[thm:flat\]]{#thm:flat label="thm:flat"} For every $n\geq1$, the fixed scheme $\mathcal X_n=\operatorname{Fix}(H_A^n)$ is scheme-theoretically isomorphic to $$\label{eq:cyclicscheme}
 \operatorname{Spec}B[x_0,\ldots,x_{n-1}]/(f_0,\ldots,f_{n-1}),
 \qquad
 f_i=A x_i^2-1+\sum_{j\in\{i-1,i+1\}}x_j,$$ where neighbors are counted as a multiset modulo $n$. The morphism $\mathcal X_n\to\operatorname{Spec}B$ is finite flat of rank $2^n$.

Writing $H_A^i(x_0,x_{-1})=(x_i,x_{i-1})$ gives the recurrence in [\[eq:henon\]](#eq:henon){reference-type="eqref" reference="eq:henon"}. The scheme map sends $(q,p)$ to $x_i=\pi_1H_A^i(q,p)$; its inverse sends a cyclic tuple to $(x_0,x_{n-1})$. The recurrence verifies both compositions on coordinate rings. For $n=1$ the inverse is $x_0\mapsto(x_0,x_0)$, and for $n=2$ it is $(x_0,x_1)\mapsto(x_0,x_1)$. In particular, the multiset convention gives $$n=1:\quad Ax_0^2+2x_0-1,$$ and $$n=2:\quad Ax_0^2+2x_1-1,\qquad Ax_1^2+2x_0-1.$$ After division by the unit $A$, every $f_i$ is monic with leading monomial $x_i^2$ under any degree-compatible order. These monomials are pairwise coprime, so Buchberger's product criterion applies over $B$. The standard monomials are $\prod_i x_i^{e_i}$ with $e_i\in\{0,1\}$, giving a free $B$-basis of size $2^n$.

The theorem separates total scheme length from geometric support size. The latter equals $2^n$ only at a reduced fiber.

[\[prop:degree-drop\]]{#prop:degree-drop label="prop:degree-drop"} For an integer $a\ne0$, every prime $p\nmid a$ has fiber scheme length $2^n$. A prime $p\mid a$ is not a point of $\operatorname{Spec}\mathbb Z[A,A^{-1}]$. Direct reduction of the original uninverted $\mathbb Z[A]$-family instead gives $$H_0(q,p)=(1-p,q),\qquad H_0^4=I.$$ In particular, $\operatorname{Fix}(H_0^n)=\mathbb A^2$ whenever $4\mid n$.

Thus 'degree-good' means $p\nmid a$; it does not mean ètale. Let $J_n$ be the Jacobian of the cyclic equations and let $M_n$ be the derivative monodromy of the Hénon orbit. Linearizing the scalar recurrence identifies $\ker J_n$ with $\ker(I-M_n)$: a cyclic tangent vector satisfies $$\binom{v_{i+1}}{v_i}
 =DH_a(x_i,x_{i-1})\binom{v_i}{v_{i-1}}.$$ Thus a degree-good fiber is ètale precisely when no geometric periodic point has multiplier one. Every degree-good characteristic-two fiber ($a\ne0$) is non-ètale, since then $$DH_a=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$ and every power has eigenvalue one. The qualifier is necessary: at $a=0$ some fixed schemes are empty, hence ètale, whereas $\operatorname{Fix}(H_0^4)=\mathbb A^2$.

For later use, exact norm calculations at the first two periods give $$\label{eq:discriminants}
 D_{a,1}=-4(a+1),\qquad
 D_{a,2}=2^8(a+1)(a-3)^3.$$

# The zero-dimensional Frobenius obstruction

Fix a degree-good fiber over $\mathbb F_p$ and write $$S_{a,p,n}=X_{a,n}(\overline{\mathbb F}_p)_{\mathrm{red}}.$$

[\[thm:collapse\]]{#thm:collapse label="thm:collapse"} For every fixed $n$ and every $r\geq1$, $$\label{eq:trace}
 N_{a,p}(r,n)
 =\operatorname{Tr}\!\left(\operatorname{Frob}_p^r\mid\mathbb Q_\ell[S_{a,p,n}]\right).$$ If $c_d$ denotes the number of Frobenius orbits of length $d$, then $$\label{eq:zeta}
 Z_{a,p,n}(u)
 =\exp\!\left(\sum_{r\geq1}N_{a,p}(r,n)\frac{u^r}{r}\right)
 =\prod_d(1-u^d)^{-c_d}
 =\det(I-u\operatorname{Frob}_p\mid\mathbb Q_\ell[S_{a,p,n}])^{-1}.$$ Every Frobenius eigenvalue in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is a root of unity, and ordinary point counts are unchanged if $X_{a,n}$ is replaced by its reduction.

Frobenius permutes the finite set $S_{a,p,n}$. The trace of its $r$-th power counts fixed basis vectors, which are exactly the $\mathbb F_{p^r}$-points. Summing the contribution of one cycle of length $d$ gives $\exp(\sum_{d\mid r}d u^r/r)=(1-u^d)^{-1}$. Field-valued points factor through the reduction, so nilpotents do not change either side.

The theorem applies to every finite zero-dimensional fiber, reduced or not, and mechanically supplies periodicity in $r$, a finite linear recurrence, sealed-$r$ validation, and local rationality for every finite scheme control. Nonreduced points can be recorded separately by local Artin length. Explicitly, our nonstandard statistic is $$N^{\mathrm{len}}(r)=
 \sum_{x\in X(\mathbb F_{p^r})}
 \operatorname{length}(\mathcal O_{X_{\overline{\mathbb F}_p},x}).$$ An orbit of degree $d$ and geometric local length $m$ contributes $(1-u^d)^{-m}$, so the weighted series is still a product of root-of-unity cycle factors with integer exponents.

Over characteristic zero, a reduced finite algebra decomposes as $\prod_i K_i$. Away from finitely many primes, the product of $Z_{a,p,n}(p^{-s})$ is therefore $\prod_i\zeta_{K_i}(s)$. This is a canonical Dedekind, equivalently permutation-Artin, interpretation. Such a global product can certainly have nontrivial zeros and can contain a Riemann-zeta factor. For example, $$\zeta_{\mathbb Q(\sqrt7)}(s)=\zeta(s)L(s,\chi_{28}),\qquad
 \zeta_{\mathbb Q(\sqrt3)}(s)=\zeta(s)L(s,\chi_{12}).$$ These invariant-line factors are classical arithmetic components accompanied by extra Artin data. The obstruction is therefore not the absence of global zeros; it is that local rationality supplies no distinguished Hénon-derived Riemann divisor.

## What the rectangular table forgets

We use arithmetic Frobenius $F_p:x\mapsto x^p$; geometric Frobenius reverses the sign convention in the second index. Because $H_a$ is defined over $\mathbb F_p$, it commutes with Frobenius. The joint finite representation has the character $$\label{eq:joint}
 T_{a,p,n}(r,s)=
 \operatorname{Tr}\!\left(\operatorname{Frob}_p^rH_a^{-s}\mid\mathbb Q_\ell[S_{a,p,n}]\right)
 =\#\{x:\operatorname{Frob}_p^r x=H_a^s x\}.$$ The original data retain only $T(r,0)$.

[\[prop:loss\]]{#prop:loss label="prop:loss"} The sequence $r\mapsto N(r,n)$ does not determine the joint action of Frobenius and chronological Hénon time.

On $\{\pm1\}\times\mathbb Z/5\mathbb Z$, define $$H(\varepsilon,i)=(\varepsilon,i+1),\quad
 R(\varepsilon,i)=(-\varepsilon,-i),\quad
 F_c(\varepsilon,i)=(\varepsilon,i+\varepsilon c).$$ Then $RHR=H^{-1}$, and each $F_c$ commutes with both $H$ and $R$. The choices $c=1,2$ both consist of two five-cycles, so $\operatorname{Tr}(F_1^r)=\operatorname{Tr}(F_2^r)=10$ when $5\mid r$ and zero otherwise. However, $\operatorname{Tr}(F_1H^{-1})=5$ whereas $\operatorname{Tr}(F_2H^{-1})=0$.

Thus a faithful two-axis continuation must retain twisted traces or all finite-index subgroup counts, not only rectangular fixed sets. Twisted counts of the form $\#\operatorname{Fix}(gF_p^r)$ already occur in equivariant finite-field zeta constructions [@walton2018 Definition 4.6]; the refinement is structurally appropriate but not a new construction type. Proposition [\[prop:loss\]](#prop:loss){reference-type="ref" reference="prop:loss"} is a control in the category of reversible finite actions, not a claim that the concrete $a=6,n=5$ fiber realizes both alternatives.

# Exact certificate and prior-work collision {#sec:certificate}

All computations use exact integers, rational functions, and explicit finite fields. No target zeros, prime tables, or floating-point roots enter the protocol.

## The first two periods at parameter six

At $a=6$ the characteristic-zero algebras split as $$X_{6,1}=\operatorname{Spec}\mathbb Q(\sqrt7),\qquad
 X_{6,2}=\operatorname{Spec}\bigl(\mathbb Q(\sqrt7)\times\mathbb Q(\sqrt3)\bigr).$$ The second factor is the primitive period-two pair. At primes outside $\{2,3,7\}$, $$\begin{aligned}
 N_{6,p}(r,1)&=1+\left(\frac7p\right)^r,\label{eq:n1}\\
 N_{6,p}(r,2)&=2+\left(\frac7p\right)^r
                  +\left(\frac3p\right)^r.\label{eq:n2}\end{aligned}$$

Table [1](#tab:counts){reference-type="ref" reference="tab:counts"} reports the complete frozen support-count rows. An independent polynomial-quotient implementation of every $\mathbb F_{p^r}$ enumerates solutions directly.

::: {#tab:counts}
    $p$ status        $N(r,1)$    $N(r,2)$
  ----- ------------- ----------- -----------
      5 ètale-good    $0,2,0,2$   $0,4,0,4$
     11 ètale-good    $0,2,0,2$   $2,4,2,4$
      7 nonreduced    $1,1,1,1$   $1,3,1,3$
      3 degree-drop   $1,1,1,1$   $1,1,1,1$

  : Ordinary support counts for $r=1,2,3,4$. Weighted counts are kept in a separate ledger and coincide only in the ètale rows.
:::

At $p=7$, the local-length-weighted rows are $(2,2,2,2)$ and $(2,4,2,4)$; ordinary counts discard the double fixed-point length. At $p=3$, direct reduction of the original uninverted family gives $H_0^4=I$, so the $n=4$ counts are $9,81,729,6561$. This is not a fiber of the finite-flat family over $\mathbb Z[A,A^{-1}]$; mixing it into the uniform quadratic family would create a spurious large signal.

## A tempting period-five signal

Restricting $\operatorname{Fix}(H_a^5)$ to the reversor line $q=p$ and removing the fixed branch gives a generic sextic $G_a(q)$ recorded in Appendix [8.2](#app:marker){reference-type="ref" reference="app:marker"}. At $a=6$ it is $$\label{eq:g6}
 46656q^6+15552q^5-20736q^4-4752q^3+3060q^2+360q-151.$$ Its discriminant is $2^{36}3^{30}\cdot31\cdot241\cdot389$. The modular factor degrees at the unramified primes $37$, $5$, and $157$ are $$[6],\qquad [5,1],\qquad [2,1,1,1,1].$$ They give a transitive subgroup of $S_6$ containing a 5-cycle and a transposition. A 5-cycle excludes nontrivial blocks in degree six; conjugates of the transposition then generate $S_6$.

This exact result initially looks like a useful Galois-theoretic refinement. The rescaling $x=6q$, however, turns [\[eq:g6\]](#eq:g6){reference-type="eqref" reference="eq:g6"} into $$x^6+2x^5-16x^4-22x^3+85x^2+60x-151.$$ Endler--Gallas already publish precisely this period-five $Z$ polynomial, its discriminant $2^6\cdot31\cdot241\cdot389$, and its symmetric Galois group [@endler2006]. The scaling law $$\operatorname{Disc}(Z(6q))=6^{30}\operatorname{Disc}(Z)$$ explains our powers $2^{36}3^{30}$. Brison--Gallas later republish the polynomial and supply companion sextics and polynomial bridges [@brison2018]. Equality holds in all seven coefficients. We therefore classify the calculation as a successful reproduction and a failed novelty gate no later than 2006.

## Reproducibility summary

Eight unit tests pass. The independent checker verifies all 36 data cells, all 16 frozen field constructions, the period-five recurrence derivation, and the expected-fail joint-action control. Exact artifact hashes and commands appear in Appendix [8.3](#app:repro){reference-type="ref" reference="app:repro"}.

# Route-A evaluation and residual question

The local determinant in Theorem [\[thm:collapse\]](#thm:collapse){reference-type="ref" reference="thm:collapse"} is exact. Its exactness does not make it a candidate Riemann determinant: the determinant is universal for finite schemes and has no target divisor. Table [2](#tab:routea){reference-type="ref" reference="tab:routea"} records the resulting Route-A decision.

::: {#tab:routea}
  layer   verdict     decisive reason
  ------- ----------- ----------------------------------------------------------
  A1      `A1_WEAK`   intrinsic cycles, but no prime-like clock or amplitude
  A2      `A2_FAIL`   universal root-of-unity permutation determinant
  A3      `A3_FAIL`   no completed Riemann divisor or counting law
  A4      `A4_FAIL`   no natural operator lift of the arithmetic scheme factor

  : Scoped Route-A evaluation.
:::

The overall label is `ROUTE_A_REJECTED`; Route B is not authorized for this registered candidate. The failure is structural rather than numerical. This ruling does not deny the nontrivial zeros of the classical global Dedekind/Artin factors, nor does it close every joint or positive-dimensional mechanism. It says that the fixed-$n$ local rationality and finite trace decomposition are universal controls and hence have no discriminating value for a new Hénon-derived Riemann divisor.

A narrower arithmetic problem survives. On exact-period points, absolute Galois commutes with $H_a$ and with the reversor $R$. Its image therefore lies in the centralizer of a dihedral action, which is generally smaller than the cyclic wreath-product bound. Low-period polynomial and Galois calculations are already well represented in the literature, so a new result would need to determine a genuinely new higher-period image, a uniform proper-subgroup obstruction, or the cohomology of a parameter-varying quotient. None of these claims follows from fixed-$n$ rationality.

# Conclusion

The area-preserving Hénon recurrence has a clean arithmetic periodic scheme: away from coefficient degree-drop primes, its $n$-th fixed scheme is finite flat of rank $2^n$. That clean structure also closes the registered local-zeta route. At fixed $n$, Frobenius acts on a zero-dimensional support, so local rationality and finite trace reconstruction are inevitable finite-permutation facts. Nilpotents disappear from ordinary counts, and rectangular counts do not retain relative chronological phase.

The obstruction is one of novelty, not a theorem forbidding global zeros. Fixed finite algebras globalize to classical Dedekind/Artin zeta functions, and may inherit a Riemann-zeta factor together with additional $L$-data. Nothing here rules out a genuinely new joint or positive-dimensional construction.

The exact certificate matters mainly as a firewall. It verifies good, ramified, and degree-drop conventions and prevents a known period-five $S_6$ sextic from being misreported as a new arithmetic signal. Future work should not enlarge the same $r$-scan. A defensible next candidate must introduce new geometry---for example a positive-dimensional exact-period parameter quotient---or prove a new theorem about the full dihedral-compatible Galois tower. Neither direction currently supplies a Hilbert--Pólya operator.

# Proof details and reproducibility

## The low-period normalized Jacobian norms

For $n=1$, set $f=ax^2+2x-1$ and $j=2ax+2$. Taking the norm of $j$ in $\mathbb Q(a)[x]/(f)$ gives $$\operatorname{Norm}(j)=-4(a+1).$$ For $n=2$, the cyclic Jacobian determinant is $$j_2=4a^2x_0x_1-4.$$ Multiplication by $j_2$ on the standard basis $1,x_0,x_1,x_0x_1$ has determinant $$2^8(a+1)(a-3)^3.$$ These $D_{a,n}$ are normalized transversality resultants/Jacobian norms, not ordinary polynomial discriminants (the ordinary $n=1$ quadratic discriminant is $4(a+1)$). The factorization $$f_0-f_1=(x_0-x_1)(a(x_0+x_1)-2)$$ separates the fixed branch from the primitive period-two branch. With $u=ax+1$ and $v=ax_0-1$ the two quadratic relations are $$u^2=a+1,\qquad v^2=a-3.$$ The branch ideals are comaximal over $\mathbb Q(a)$, so this gives the scheme-theoretic product there. At $a=3$ the primitive branch collides with the fixed branch; the splitting is not asserted at that specialization.

## The generic reversor-line marker {#app:marker}

The exact period-five marker before specialization is $$\begin{aligned}
G_a(q)={}&a^6q^6+2a^5q^5+(-3a^5+2a^4)q^4
 +(-4a^4+2a^3)q^3\\
&+(3a^4-4a^3+a^2)q^2+(2a^3-2a^2)q
 -a^3+2a^2-a-1.\end{aligned}$$ It is obtained as the greatest common divisor of the two equations defining $\operatorname{Fix}(H_a^5)$ after setting $p=q$, divided by the fixed-point factor $aq^2+2q-1$. The producer derives this expression; it is not inserted as a fit.

## Reproducibility ledger {#app:repro}

From the repository root, run

    python henon_frobenius_scheme_obstruction/code/test_c12a.py
    python henon_frobenius_scheme_obstruction/code/c12a_producer.py
    python henon_frobenius_scheme_obstruction/code/c12a_checker.py

The frozen artifacts have SHA-256 values

  artifact            SHA-256
  ------------------- --------------------------------------------------------------------
  certificate JSON    `851ca31f62fb508ad806c26084eab9fe092d5ee037bf99f0cb811cbccf7f8eb8`
  count CSV           `d07d9558dd9036507b89699452edc1494bea2faca8344d5ce6cf2d031f9bc480`
  independent check   `4784e8b2fbf98ad835a5f1c0ef9217de14537adcff486046e74a6b0f47e93778`

The checker does not import the producer. It constructs each frozen finite field as an explicit polynomial quotient, verifies directly that every nonzero element is a unit, and enumerates the cyclic equations. The period-five checker starts instead from the scalar recurrence on the reversor line. It also enumerates all states of the reversible joint-action control and verifies $RHR=H^{-1}$ and both commutation relations. The v2 amendment that introduced this control is recorded in `AMENDMENT_LOG.md`.

## Limitations

We do not prove that $X_{a,n}$ is reduced in characteristic zero for every fixed $a$ and $n$. Scheme-level formal period requires extra care when the characteristic divides $n$. The global Dedekind factors discussed in the main text can have nontrivial zeros and may contain $\zeta(s)$; what they do not provide is a new Hénon-specific gamma factor, exact Riemann divisor, or self-adjoint realization required by Hilbert--Pólya.
