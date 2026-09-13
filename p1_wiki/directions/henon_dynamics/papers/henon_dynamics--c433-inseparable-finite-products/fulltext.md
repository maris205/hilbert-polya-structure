---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c433-inseparable-finite-products"
canonical_tex: "henon_dynamics/research_c429_c433/papers/C433_inseparable_finite_products/main.tex"
canonical_pdf: "henon_dynamics/research_c429_c433/papers/C433_inseparable_finite_products/main.pdf"
source_sha256: "f5bade84a98663c6c2db3acede6b56810c1bbb04aeff192f98db9334d28c9cd3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite detection of multiplicative periodic data\newline for inseparable polynomials

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c429_c433/papers/C433_inseparable_finite_products>)
- [规范 TeX](<../../../../../henon_dynamics/research_c429_c433/papers/C433_inseparable_finite_products/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c429_c433/papers/C433_inseparable_finite_products/main.pdf>)
- [BibTeX](<../../../../../henon_dynamics/research_c429_c433/papers/C433_inseparable_finite_products/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $k=\overline{\mathbb F}_p$, let $f\in k[x]$ have degree $d\ge2$ and derivative zero, and let $g=A/B\in k(x)^\times$ have height $m=\max(\deg A,\deg B)$ in coprime form. We give a finite criterion for all but finitely many ordinary primitive cycles of $f$ to avoid the zeros and poles of $g$ and have product one (condition $\mathrm{(CP)}$). Put $b=\lceil m/(d-1)\rceil+1$, $D=2b^2$, and $N=6b^2+1$. For $F_n=f^{\circ n}-x$ and $H_n=\prod_{0\le i<n}A(f^{\circ i})-\prod_{0\le i<n}B(f^{\circ i})$, the condition is equivalent to $F_n\mid S_*H_n$ for every $1\le n\le N$, where $S_*=\prod_{r=1}^{D}F_r$. The proof constructs a general-polynomial Laurent representation, controls one exceptional polynomial factor by a contracting state bound, and combines split coefficient ranks with persistence at arbitrarily long returns. Whenever $\mathrm{(CP)}$ holds, each product-visible exceptional cycle has native period at most $D$; no such bound is asserted for a support cycle on which both whole products vanish. All primes, nonmonic maps, rational weights of height zero, and native periods divisible by the characteristic are included.
author:
- Anonymous authors
bibliography:
- references.bib
title: Finite detection of multiplicative periodic datafor inseparable polynomials
```

## Markdown 正文

# Introduction

Periodic products attach multiplicative data to the ordinary cycles of a polynomial map. For a rational weight $g$, one can ask whether the product of $g$ is one around every cycle outside a finite exceptional collection. Even when each individual product is elementary to define, this is an infinite condition, and the finite set of allowed exceptions is not supplied as part of the input. A finite test must therefore address two distinct issues: how to detect all returns once an exceptional polynomial is fixed, and how to eliminate that unknown polynomial with a coefficient-independent bound.

This paper resolves both issues for every polynomial of derivative zero over an algebraic closure of a finite field. The return polynomials $f^{\circ n}-x$ are then squarefree, even when the ordinary period is divisible by the characteristic. This turns polynomial annihilation into an exact statement about ordinary points. A finite-state representation controls the return tests for a fixed annihilator. Under the cofinite product condition $\mathrm{(CP)}$, a separate rank argument bounds the native period of each visible exceptional cycle, making a universal annihilator available. The resulting return bound depends only on the degree of the map and the height of the rational weight.

Two classical ingredients should be distinguished from this combination. Coefficient functionals, quotient normal forms, and residue pairings are established tools; Cattani, Dickenstein, and Sturmfels give a systematic treatment of normal forms and multidimensional residues, in particular in Section 4 of the preprint version of [@CDS1996]. We do not import a complex-analytic residue formula into positive characteristic: the locally finite Laurent extractor needed here is proved directly. Finite word cutoffs for finite-dimensional weighted representations are also classical. The arbitrary-field formulation in Section 3 and Proposition 3.1 of Kiefer et al. [@Kiefer2013] supplies the relevant context; we include the elementary matrix-span proof rather than use a rational-field Gram argument or a complexity theorem.

The specific work is the general-polynomial coefficient and carry construction for two whole rational-weight products, followed by the elimination of an unknown finite exceptional set. The split rank calculation uses two full-rank evaluation maps. Persistence uses finite multiplicative orders only to keep a specified visible cycle visible at arbitrarily long returns; it does not require simultaneous visibility of every exceptional point. These details are essential to the degree-only conclusion.

Section [2](#sec:statement){reference-type="ref" reference="sec:statement"} states the finite criterion and handles actual conjugacy for nonmonic maps. Section [3](#sec:cycles){reference-type="ref" reference="sec:cycles"} identifies the ordinary-cycle condition with an annihilator ideal and separates product visibility from derivative filtering. Sections [4](#sec:extractor){reference-type="ref" reference="sec:extractor"} and [5](#sec:transfer){reference-type="ref" reference="sec:transfer"} prove the coefficient representation and fixed-annihilator theorem. Section [6](#sec:rank){reference-type="ref" reference="sec:rank"} bounds visible native periods, and Section [7](#sec:decision){reference-type="ref" reference="sec:decision"} completes the finite decision.

# Ordinary cycles and the finite criterion {#sec:statement}

Fix a prime $p$ and write $k=\overline{\mathbb F}_p$. Throughout, $f\in k[x]$ has degree $d\ge2$ and satisfies $f'=0$. Write $g=A/B\in k(x)^\times$ with nonzero coprime $A,B\in k[x]$, and set $$\label{eq:constants}
 m=\max(\deg A,\deg B),\quad
 a=\left\lceil\frac{m}{d-1}\right\rceil,\quad b=a+1,\quad
 D=2b^2,\quad N=3D+1=6b^2+1.$$ There is no norm-one hypothesis, restriction on support multiplicities, or requirement that the numerator and denominator have the same degree. Although $p\mid d$, the degree need not be a power of $p$.

An *ordinary primitive cycle* is the set $O=\{x,f(x),\ldots,f^{\circ(r-1)}(x)\}$ of a point of least positive period $r$. Each distinct point is counted once; one step means one application of the original $f$. A cycle is *admissible* if it avoids $V(AB)$, and its native product is $$\label{eq:product}
 W_O=\prod_{x\in O}g(x)\in k^\times.$$ Condition $\mathrm{(CP)}$ means that all but finitely many ordinary primitive affine cycles are admissible and satisfy $W_O=1$. The single fixed point at infinity would not change this cofinite condition.

The associated rational skew map has the precise one-step domain $$\label{eq:skew}
 T:U\times\mathbb G_m\longrightarrow\mathbb A^1\times\mathbb G_m,
 \qquad (x,y)\longmapsto(f(x),g(x)y),\qquad
 U=\mathbb A^1\setminus V(AB).$$ The set $U$ need not be forward invariant. Further steps require the corresponding iterates of $x$ to remain in $U$. Along an admissible $r$-cycle they are defined and $T^{\circ r}(x,y)=(x,W_Oy)$. No global inverse or extension across the excluded support is being asserted.

For every integer $n\ge1$, put $$\begin{aligned}
 F_n(x)&=f^{\circ n}(x)-x,\label{eq:F}\\
 H_n(x)&=\prod_{i=0}^{n-1}A(f^{\circ i}(x))
          -\prod_{i=0}^{n-1}B(f^{\circ i}(x)),\label{eq:H}\\
 S_*(x)&=\prod_{r=1}^{D}F_r(x),\qquad
 I_g=\{S\in k[x]: F_n\mid SH_n\text{ for all }n\ge1\}.
 \label{eq:ideal}\end{aligned}$$ A point is *product-visible at return $n$* if $F_n(x)=0$ and $H_n(x)\ne0$. A product-visible cycle is one containing a point visible at some return.

[\[thm:main\]]{#thm:main label="thm:main"} For the data above, the following conditions are equivalent:

1.  The ordinary cofinite cycle-product condition $\mathrm{(CP)}$ holds.

2.  $I_g\ne(0)$.

3.  $S_*\in I_g$.

4.  $F_n\mid S_*H_n$ for every integer $1\le n\le N$.

If these conditions hold, every product-visible cycle has ordinary least period at most $D$. This is not a bound of $D$ on the number of all product-visible points. Nor does it bound the period of a support cycle containing both a numerator zero and a denominator zero: both whole products vanish at every return on such a cycle, which remains a legitimate finite support exception.

The statement includes $m=0$, $p=2$, and all native periods divisible by $p$. Its tests use the original map, whether monic or not. They are finite polynomial operations over a finite field containing the input coefficients. The bound is a bound on the return index, not a claim of efficient complexity: the tested polynomial degrees can reach $d^N$.

[\[lem:monic\]]{#lem:monic label="lem:monic"} It suffices to prove Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} for monic $f$. The same reduction preserves every fixed-$S$ divisibility problem and the degree of $S$.

Let $c_d\ne0$ be the leading coefficient of $f$. Choose $t\in k^\times$ with $c_dt^{d-1}=1$ and use the actual conjugacy $\phi(y)=ty$. Define $$\widetilde f(y)=t^{-1}f(ty),\qquad
 \widetilde A(y)=A(ty),\qquad \widetilde B(y)=B(ty).$$ The new map is monic of degree $d$ and derivative zero; the new coprime pair has height $m$. The conjugacy bijects ordinary cycles, preserves least periods and products, and transports the zero/pole exceptions. Iterating the conjugacy gives $$\label{eq:conjugacy}
 \widetilde F_n(y)=t^{-1}F_n(ty),\qquad
 \widetilde H_n(y)=H_n(ty),\qquad
 \widetilde S_*(y)=t^{-D}S_*(ty).$$ Consequently all displayed divisibilities are unchanged by substitution and nonzero scalar factors. A fixed $S$ becomes $S(ty)$, of the same degree. This proves the reduction without rescaling the dynamics or changing its clock. The decision rule itself does not require a choice of $t$.

We assume $f$ monic in the proof below.

# Simple returns, annihilators, and visibility {#sec:cycles}

By the chain rule, for every $n\ge1$, $$\label{eq:simple}
 (f^{\circ n})'=0,\qquad F_n'=-1.$$ Thus $F_n$ has exactly $d^n$ distinct roots. Define $$\label{eq:badsets}
 \mathcal B_n=\{x\in k:F_n(x)=0,\ H_n(x)\ne0\},\qquad
 \mathcal B=\bigcup_{n\ge1}\mathcal B_n.$$ Each root of $F_n$ has ordinary least period dividing $n$. Cyclically permuting the numerator factors, and separately the denominator factors, shows that $H_n$ is constant along its cycle. Hence $\mathcal B_n$ is a union of full native cycles and is permuted by $f$.

[\[prop:ideal\]]{#prop:ideal label="prop:ideal"} For every $S\in k[x]$ and $n\ge1$, $$\label{eq:annihilator}
 F_n\mid SH_n\quad\Longleftrightarrow\quad
 S(x)=0\text{ for every }x\in\mathcal B_n.$$ Moreover, $I_g\ne(0)$ if and only if $\mathcal B$ is finite, and these conditions are equivalent to $\mathrm{(CP)}$. When $\mathcal B$ is finite, $I_g$ is generated by $\prod_{x\in\mathcal B}(X-x)$, with empty product equal to one.

Equation [\[eq:annihilator\]](#eq:annihilator){reference-type="eqref" reference="eq:annihilator"} follows from the simple roots in [\[eq:simple\]](#eq:simple){reference-type="eqref" reference="eq:simple"}. A nonzero polynomial cannot vanish on an infinite set of distinct points. If $\mathcal B$ is finite, its monic vanishing polynomial divides every polynomial vanishing on $\mathcal B$, giving the assertion about the ideal.

Only finitely many periodic cycles meet $V(AB)$: different cycles are disjoint and each such cycle contains a point of this finite set. The full union of those cycles is finite, though its size is not bounded here by the number of support points. On an admissible cycle $O$ of least period $r\mid n$, for $x\in O$, $$\label{eq:repeatproduct}
 H_n(x)=\left(\prod_{i=0}^{n-1}B(f^{\circ i}(x))\right)
                (W_O^{n/r}-1),$$ and the prefactor is nonzero. If $\mathrm{(CP)}$ holds, every cycle outside its finite exceptional collection and the support cycles has $H_n=0$ at every return. Thus $\mathcal B$ is finite. Conversely, each admissible cycle with $W_O\ne1$ contributes all its points to $\mathcal B_r$ at its native period. If $\mathcal B$ is finite, only finitely many such cycles exist. Adding the finite support cycles gives exactly $\mathrm{(CP)}$.

## What derivative filtering does, and does not, see

For clarity, temporarily let $F$ be any nonzero polynomial over $k$, and let $x_0$ be a root of multiplicity $e$. Write $F=(X-x_0)^eV$ with $V(x_0)\ne0$. For arbitrary polynomials $S,H$, local divisibility is characterized by $$\label{eq:filter}
 F\mid SF'H\text{ at }x_0
 \quad\Longleftrightarrow\quad e\,S(x_0)H(x_0)=0\text{ in }k.$$ Indeed, if $p\nmid e$, the derivative has exact order $e-1$, so one additional zero of $SH$ is necessary and sufficient. If $p\mid e$, differentiation gives $F'=(X-x_0)^eV'$, and local divisibility is automatic. This proves [\[eq:filter\]](#eq:filter){reference-type="eqref" reference="eq:filter"} without equating it with the pointwise value $F'(x_0)H(x_0)$.

For return polynomials, put $e_n(x)=\mathop{\mathrm{ord}}_x F_n$. Product visibility means $H_n(x)\ne0$ at a return root. Derivative-filtered visibility means $e_n(x)H_n(x)\ne0$, with the integer $e_n(x)$ interpreted in $k$. Native Jacobian visibility alone means $p\nmid e_r(x)$ at the least period $r$, independently of the weight. These are different notions in general. In the present derivative-zero class, $e_n(x)=1$ at every return by [\[eq:simple\]](#eq:simple){reference-type="eqref" reference="eq:simple"}, so derivative filtering discards no product-visible return.

::: {#tab:comparison}
  Problem or interface                Exact test or visible data                      Scope of the conclusion
  ----------------------------------- ----------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Fixed-$S$ certificate               $F_n\mid SH_n$ for all $n$                      For the present class, returns through $k_S+4b^2$ suffice (Theorem [\[thm:fixed\]](#thm:fixed){reference-type="ref" reference="thm:fixed"}); $S$ is supplied.
  Derivative-filtered visible data    $F_n\mid SF_n'H_n$ tests $e_n(x)S(x)H_n(x)=0$   The local criterion [\[eq:filter\]](#eq:filter){reference-type="eqref" reference="eq:filter"} can ignore product data when $p\mid e_n(x)$; it is not an ordinary cofinite-product conclusion.
  Ordinary derivative-zero decision   $F_n\mid S_*H_n$ for $1\le n\le6b^2+1$          Exactly $\mathrm{(CP)}$; the unknown exceptions are eliminated and all native periods are retained.

  : Three distinct certification roles. The middle row is an exact local interface, not an asserted general separable-map cofinite-product theorem.
:::

In characteristic three, take $f=x^2$. Then $F_2=x(x-1)^3$ and $F_2'=(x-1)^3$. Choose a constant $c\in k^\times$ with $c^2\ne1$ and let $g=c$, so $H_2=c^2-1\ne0$. With $S=x$ one has $F_2\mid SF_2'H_2$ but $F_2\nmid SH_2$. The fixed point $1$ has native multiplicity one in $F_1=x(x-1)$, yet return multiplicity three in $F_2$. This proves only the stated one-return blindness. It is not an all-return rational-weight counterexample and is not used in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# The cyclic digit algebra and coefficient extractor {#sec:extractor}

For $n\ge1$, with indices read modulo $n$, define $$\label{eq:cyclicalgebra}
 \mathcal A_n=k[X_0,\ldots,X_{n-1}]/
       (f(X_i)-X_{i+1}:i\bmod n).$$ The relations determine $X_i=f^{\circ i}(X_0)$ and then impose $F_n(X_0)=0$, yielding $$\label{eq:quotientiso}
 \mathcal A_n\simeq k[x]/(F_n),\qquad X_i\longmapsto f^{\circ i}(x).$$

[\[lem:basis\]]{#lem:basis label="lem:basis"} The monomials $$\label{eq:digits}
 X^\epsilon=\prod_{i=0}^{n-1}X_i^{\epsilon_i},\qquad
        0\le\epsilon_i\le d-1,$$ form a basis of $\mathcal A_n$. Let $L_n$ select the coefficient of $\prod_iX_i^{d-1}$ in that basis. Under [\[eq:quotientiso\]](#eq:quotientiso){reference-type="eqref" reference="eq:quotientiso"}, $L_n$ selects the coefficient of $x^{d^n-1}$ in the remainder of degree below $d^n$. The pairing $(u,v)\mapsto L_n(uv)$ is nondegenerate. In particular, for $U\in\mathcal A_n$, $$\label{eq:alltests}
 U=0\quad\Longleftrightarrow\quad
 L_n(X^\epsilon U)=0\text{ for every digit word }\epsilon.$$

Replacing $X_i^d$ by $X_{i+1}$ minus the lower-degree terms of $f(X_i)$ strictly lowers total degree, so the digit monomials span. Their images in [\[eq:quotientiso\]](#eq:quotientiso){reference-type="eqref" reference="eq:quotientiso"} are monic of distinct degrees $\sum_i\epsilon_i d^i$, covering every integer from zero to $d^n-1$. They are independent. The unique top degree corresponds to the top digit monomial, proving the coefficient assertion. For a nonzero remainder $u$ of degree $q$ and leading coefficient $u_q\ne0$, the product $u x^{d^n-1-q}$ has top coefficient $u_q$ without reduction. This proves nondegeneracy, and testing against the basis proves [\[eq:alltests\]](#eq:alltests){reference-type="eqref" reference="eq:alltests"}.

For a polynomial $J$ in the variables $X_i$, define the formal coefficient expression $$\label{eq:extractor}
 \mathcal R_n(J)=
 [X_0^{-1}\cdots X_{n-1}^{-1}]
 J\prod_{i=0}^{n-1}
 \left(\sum_{q_i\ge0}\frac{X_{i+1}^{q_i}}{f(X_i)^{q_i+1}}\right),$$ where every inverse power of $f(X_i)$ is expanded at infinity.

[\[prop:extractor\]]{#prop:extractor label="prop:extractor"} The expression [\[eq:extractor\]](#eq:extractor){reference-type="eqref" reference="eq:extractor"} is a finite algebraic sum for each polynomial $J$. It annihilates the ideal defining $\mathcal A_n$ and equals $L_n$ on the quotient, including when $n=1$.

Consider one input monomial $\prod_iX_i^{j_i}$ of total degree $J_0$. A term of the inverse power of $f(X_i)$ has exponent $-d(q_i+1)-u_i$, with $u_i\ge0$. A contribution to the required coefficient must satisfy $$j_i+q_{i-1}-d(q_i+1)-u_i=-1
 \quad\text{for every }i.$$ Summing gives $$\label{eq:finiteindices}
 J_0-n(d-1)=(d-1)\sum_iq_i+\sum_i u_i.$$ All indices are nonnegative and therefore bounded. Each inverse-power coefficient is finite as well. Consequently all coefficient rearrangements here are algebraic; no analytic convergence or division by an integer is required.

Multiplying the integrand in [\[eq:extractor\]](#eq:extractor){reference-type="eqref" reference="eq:extractor"} by $f(X_j)-X_{j+1}$ cancels its geometric series. In the remaining factors there are no negative powers of $X_j$, so the coefficient with $X_j^{-1}$ vanishes, even after multiplication by a polynomial. Successive geometric terms telescope, and the unbounded remainder contributes nothing to a fixed coefficient by the same finiteness bound. This justifies the cancellation inside these coefficient expansions. For $n=1$, cancellation simply leaves a polynomial. Thus the defining ideal is annihilated.

For the top digit monomial, [\[eq:finiteindices\]](#eq:finiteindices){reference-type="eqref" reference="eq:finiteindices"} forces every $q_i$ and $u_i$ to be zero, and monicity gives coefficient one. For any other digit monomial, $J_0<n(d-1)$, so no contribution is possible. The resulting quotient functional is exactly $L_n$.

This proof is the characteristic-independent algebraic ingredient needed below. The classical relation between normal forms and residue functionals in [@CDS1996 Section 4 of the preprint version] provides context, not an additional positive-characteristic hypothesis.

# Transfer states and a fixed-annihilator cutoff {#sec:transfer}

For $h\in k[X]$ and nonnegative integers $r,s$, set $$\label{eq:transfer}
 T_h(r,s)=[X^{-1}]\frac{X^r h(X)}{f(X)^{s+1}}.$$ The expansion is the one in Section [4](#sec:extractor){reference-type="ref" reference="sec:extractor"}. For $h\ne0$, a nonzero entry requires $$\label{eq:generalstate}
 ds\le r+\deg h-d+1,$$ because the largest exponent of the fraction is $r+\deg h-d(s+1)$, which must be at least $-1$. The zero polynomial gives a zero matrix and needs no degree convention. Factoring the input of [\[eq:extractor\]](#eq:extractor){reference-type="eqref" reference="eq:extractor"} gives $$\label{eq:cyclicsum}
 L_n\left(\prod_i h_i(X_i)\right)=
 \sum_{r_0,\ldots,r_{n-1}\ge0}
        \prod_iT_{h_i}(r_{i-1},r_i),\qquad r_{-1}=r_{n-1}.$$ Here $r_i=q_i$ is the outgoing power of $X_{i+1}$ in the extractor; the incoming power at $X_i$ is $r_{i-1}$. Finiteness of this cyclic sum was proved in [\[eq:finiteindices\]](#eq:finiteindices){reference-type="eqref" reference="eq:finiteindices"}.

Fix a nonzero polynomial $S$ and write $\ell=\deg S$. Define $$\label{eq:ks}
 k_S=\begin{cases}
       0,&\ell=0,\\
       \lfloor\log_d\ell\rfloor+1,&\ell\ge1.
      \end{cases}$$ We regard the factor containing $S$ as the distinguished site and the remaining factors as bulk sites. For a digit $0\le\epsilon<d$, the degrees of $X^\epsilon A$ and $X^\epsilon B$ are at most $m+d-1$. At the distinguished site the additional degree is $\ell$. Thus [\[eq:generalstate\]](#eq:generalstate){reference-type="eqref" reference="eq:generalstate"} gives $$\label{eq:statebounds}
 ds\le r+m\quad\text{at a bulk site},\qquad
 ds\le r+m+\ell\quad\text{at the distinguished site}.$$ At a maximal index of a nonzero cyclic contribution, the incoming index is no larger. Every index is consequently at most $\lfloor(m+\ell)/(d-1)\rfloor$, and hence at most $$\label{eq:R}
 R=a+\ell.$$ Indeed $(d-1)a\ge m$ and $d-1\ge1$. Restricting all rows and columns to $0,\ldots,R$ therefore loses no cyclic contribution.

On this finite state range let $$\label{eq:blocks}
 \mathsf M_\epsilon=\mathop{\mathrm{diag}}(T_{X^\epsilon A},T_{X^\epsilon B}),
 \qquad
 \mathsf B_\epsilon=\mathop{\mathrm{diag}}(T_{SX^\epsilon A},-T_{SX^\epsilon B}).$$ Applying [\[eq:cyclicsum\]](#eq:cyclicsum){reference-type="eqref" reference="eq:cyclicsum"} to the two whole products yields $$\label{eq:tracerepresentation}
 L_n(S(X_0)X^\epsilon H_n)=
 \mathop{\mathrm{tr}}\bigl(\mathsf B_{\epsilon_0}\mathsf M_{\epsilon_1}
                    \cdots\mathsf M_{\epsilon_{n-1}}\bigr),$$ with $H_n$ understood via [\[eq:quotientiso\]](#eq:quotientiso){reference-type="eqref" reference="eq:quotientiso"}. At $n=1$, the product after $\mathsf B$ is the identity. All scalar factors of $g$ remain in $A$ and occur at every site; no period-dependent phase is removed. The minus sign occurs once, also in characteristic two.

[\[lem:contraction\]]{#lem:contraction label="lem:contraction"} The bulk state range $0,\ldots,a$ is closed. Starting anywhere in $0,\ldots,R$, after $k_S$ bulk transitions every surviving state is at most $a$.

From [\[eq:statebounds\]](#eq:statebounds){reference-type="eqref" reference="eq:statebounds"} and $m\le(d-1)a$, $$s-a\le\frac{r-a}{d}.$$ Thus an incoming state at most $a$ cannot leave the low range. Starting at a state at most $a+\ell$, after $j$ bulk transitions the bound is $a+\ell/d^j$. For $\ell>0$, $d^{k_S}>\ell$, so integrality places every state at most $a$ after $k_S$ transitions. If $\ell=0$, it is low already. These are bounds on paths, not assertions that nonzero terms cannot cancel in a sum.

Let $\mathsf M^0_\epsilon$ be the restrictions to the two closed low ranges. Their common size is $v=2b$. Suppose $n\ge k_S+1$. The input index of the distinguished site in a cyclic contribution is low: its preceding $n-1$ bulk sites include at least $k_S$ transitions. After the distinguished site and the next $k_S$ bulk transitions, the output is low again. Define $\mathsf E_{\epsilon_0\ldots\epsilon_{k_S}}$ to be the low-row, low-column block of $$\mathsf B_{\epsilon_0}\mathsf M_{\epsilon_1}
                    \cdots\mathsf M_{\epsilon_{k_S}}.$$ All high intermediate states in this prefix remain in the sum. Every subsequent bulk path stays low, so [\[eq:tracerepresentation\]](#eq:tracerepresentation){reference-type="eqref" reference="eq:tracerepresentation"} becomes $$\label{eq:prefixtrace}
 \mathop{\mathrm{tr}}\bigl(\mathsf E_{\epsilon_0\ldots\epsilon_{k_S}}
       \mathsf M^0_{\epsilon_{k_S+1}}\cdots
       \mathsf M^0_{\epsilon_{n-1}}\bigr).$$

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} For every nonzero $S\in k[x]$, $$\label{eq:fixed}
 \bigl[F_n\mid SH_n\text{ for every }n\ge1\bigr]
 \quad\Longleftrightarrow\quad
 \bigl[F_n\mid SH_n\text{ for every }1\le n\le k_S+4b^2\bigr].$$

Let $W_j$ be the span of products of the $d$ matrices $\mathsf M^0_\epsilon$ of length at most $j$, including the empty product. Then $$W_{j+1}=W_j+\sum_{\epsilon=0}^{d-1}W_j\mathsf M^0_\epsilon.$$ Equality at one step makes the space stable under every letter and therefore under all words. Otherwise its dimension grows strictly. The initial dimension is one, and the ambient matrix space has dimension $v^2=4b^2$. Hence words of length at most $4b^2-1$ span every word product. This is the elementary finite-word principle underlying arbitrary-field weighted representations such as [@Kiefer2013 Proposition 3.1].

For each fixed prefix in [\[eq:prefixtrace\]](#eq:prefixtrace){reference-type="eqref" reference="eq:prefixtrace"}, its trace functional vanishes on all tail words if it vanishes at those lengths. A prefix has length $k_S+1$, so the largest required total length is $k_S+4b^2$. Include also the short returns $1\le n\le k_S$, before compression applies. By the nondegenerate digit tests [\[eq:alltests\]](#eq:alltests){reference-type="eqref" reference="eq:alltests"}, vanishing of all these coefficients is exactly the required polynomial divisibility, proving the nontrivial implication. The converse is immediate.

No bound on the degree of an unknown exceptional polynomial has been assumed. Theorem [\[thm:fixed\]](#thm:fixed){reference-type="ref" reference="thm:fixed"} controls a polynomial that is already specified; eliminating the unknown one requires the next section.

# Split coefficient rank and persistent visible cycles {#sec:rank}

Take $S=1$. The low state range suffices throughout. Write $M_\epsilon$ for the two-block matrices on this range and $E=\mathop{\mathrm{diag}}(I_b,-I_b)$. Define the coefficient array $$\label{eq:tensor}
 \mathcal T_n(\epsilon)=L_n(H_nX^\epsilon)
   =\mathop{\mathrm{tr}}(E M_{\epsilon_0}\cdots M_{\epsilon_{n-1}}).$$ All word products lie in $$\label{eq:blockalgebra}
 \mathcal D=\mathop{\mathrm{Mat}}_b(k)\oplus\mathop{\mathrm{Mat}}_b(k),\qquad \dim_k\mathcal D=2b^2=D.$$ For a cut $1\le h<n$, form the matrix $\mathcal F_{n,h}$ whose rows are digit words $u$ of length $h$, whose columns are digit words $v$ of length $n-h$, and whose entry is $\mathcal T_n(uv)$. The expression $\mathop{\mathrm{tr}}(E M_uM_v)$ is a bilinear pairing on two elements of $\mathcal D$. Factoring through a vector-space basis gives $$\label{eq:rankupper}
 \mathop{\mathrm{rank}}\mathcal F_{n,h}\le D.$$ No nondegeneracy of the trace pairing is needed.

[\[lem:evalrank\]]{#lem:evalrank label="lem:evalrank"} Put $t_n=|\mathcal B_n|$. If $d^h\ge t_n$ and $d^{n-h}\ge t_n$, then $\mathop{\mathrm{rank}}\mathcal F_{n,h}=t_n$, and in particular $t_n\le D$.

For the monic squarefree polynomial $F_n$ of degree $d^n$, Lagrange interpolation gives, for every polynomial $R$, $$\label{eq:lagrange}
 L_n(R)=\sum_{F_n(x)=0}\frac{R(x)}{F_n'(x)}
       =-\sum_{F_n(x)=0}R(x).$$ Indeed the interpolation polynomial $F_n(X)/((X-x)F_n'(x))$ has top coefficient $1/F_n'(x)$. The identity first applies to the remainder of $R$ and then to $R$, since their values at roots agree. Equation [\[eq:simple\]](#eq:simple){reference-type="eqref" reference="eq:simple"} gives the last equality.

Set $\gamma_n(x)=-H_n(x)\ne0$ for $x\in\mathcal B_n$. Then $$\label{eq:evaluationfactor}
 \mathcal F_{n,h}=V\mathop{\mathrm{diag}}(\gamma_n(x):x\in\mathcal B_n)W^{\mathsf T},$$ where $$\begin{aligned}
 V_{u,x}&=\prod_{i=0}^{h-1}f^{\circ i}(x)^{u_i},\\
 W_{v,x}&=\prod_{i=0}^{n-h-1}
                       f^{\circ i}(f^{\circ h}(x))^{v_i}.\end{aligned}$$ The left digit polynomials form a monic triangular basis in every degree below $d^h$, by the degree argument in Lemma [\[lem:basis\]](#lem:basis){reference-type="ref" reference="lem:basis"}. If $d^h\ge t_n$, evaluation at the $t_n$ distinct points of $\mathcal B_n$ has rank $t_n$: Lagrange polynomials of degree below $t_n$ realize every value vector. Thus $V$ has full column rank. The same argument applies to $W$ when $d^{n-h}\ge t_n$, because $f^{\circ h}$ permutes $\mathcal B_n$ and hence its evaluation points are also distinct.

The diagonal matrix in [\[eq:evaluationfactor\]](#eq:evaluationfactor){reference-type="eqref" reference="eq:evaluationfactor"} is invertible. A left inverse of $V$ and a right inverse of $W^{\mathsf T}$ show that the rank of the product is at least $t_n$; the factorization gives the reverse inequality. For $t_n=0$, both sides have rank zero. This is an ordinary full-rank evaluation argument, not a Gram-matrix or positivity argument. Together with [\[eq:rankupper\]](#eq:rankupper){reference-type="eqref" reference="eq:rankupper"}, it proves the lemma.

[\[prop:period\]]{#prop:period label="prop:period"} If $I_g\ne(0)$, every product-visible cycle has native period at most $D$.

By Proposition [\[prop:ideal\]](#prop:ideal){reference-type="ref" reference="prop:ideal"}, $\mathcal B$ is finite. Fix $x\in\mathcal B_{n_0}$ and let $r$ be its ordinary least period. Put $$\alpha=\prod_{i=0}^{n_0-1}A(f^{\circ i}(x)),\qquad
 \beta=\prod_{i=0}^{n_0-1}B(f^{\circ i}(x)).$$ Since $\alpha-\beta=H_{n_0}(x)\ne0$ and $x$ returns after $n_0$ steps, for every positive integer $q$, $$\label{eq:persistence}
 H_{qn_0}(x)=\alpha^q-\beta^q.$$ Every nonzero element of $k$ has finite multiplicative order: it belongs to a finite subfield. Choose a positive integer $M$ divisible by the orders of every nonzero element among $\alpha$ and $\beta$. For arbitrarily large $q=1+jM$, their nonzero values are fixed by the $q$th power, while a zero value remains zero. Thus [\[eq:persistence\]](#eq:persistence){reference-type="eqref" reference="eq:persistence"} equals $\alpha-\beta\ne0$. This includes a one-sided zero product; both products cannot be zero at a point of $\mathcal B_{n_0}$.

Consequently $x\in\mathcal B_{qn_0}$ at arbitrarily large returns, and each of these sets contains its full $r$-cycle. Write $t=|\mathcal B|$. If $\mathcal B\ne\varnothing$, choose one such return $n$ so large that, with $h=\lfloor n/2\rfloor$, $$h\ge1,\qquad d^h\ge t,\qquad d^{n-h}\ge t.$$ Then $t_n\le t$, so Lemma [\[lem:evalrank\]](#lem:evalrank){reference-type="ref" reference="lem:evalrank"} gives $$\label{eq:periodbound}
 r\le|\mathcal B_n|\le D.$$ Apply this argument separately to each already visible cycle. There is no assumption that all of $\mathcal B$ is visible at one return, and no coefficient-independent multiplicative-order bound is needed. If $\mathcal B$ is empty, the conclusion is vacuous.

The order of the quantifiers matters: finiteness of $\mathcal B$ makes both evaluation halves long enough for a chosen cycle, and that cycle is then bounded by the fixed rank $D$. The proof does not deduce $|\mathcal B|\le D$.

# Eliminating unknown exceptions {#sec:decision}

The equivalence of $\mathrm{(CP)}$ and $I_g\ne(0)$ is Proposition [\[prop:ideal\]](#prop:ideal){reference-type="ref" reference="prop:ideal"}. Suppose $I_g\ne(0)$. By Proposition [\[prop:period\]](#prop:period){reference-type="ref" reference="prop:period"}, every point of $\mathcal B$ is a root of some $F_r$ with $1\le r\le D$. Hence $S_*$ vanishes on $\mathcal B$, and [\[eq:annihilator\]](#eq:annihilator){reference-type="eqref" reference="eq:annihilator"} gives $S_*\in I_g$. Conversely, $S_*\in I_g$ implies $I_g\ne(0)$ because $S_*$ is nonzero.

The degree of this specified polynomial is $$\label{eq:star-degree}
 \ell_* =\sum_{r=1}^{D}d^r
        =\frac{d^{D+1}-d}{d-1}<d^{D+1}.$$ Thus the integer in [\[eq:ks\]](#eq:ks){reference-type="eqref" reference="eq:ks"} satisfies $k_{S_*}\le D+1$. Its fixed-annihilator horizon from Theorem [\[thm:fixed\]](#thm:fixed){reference-type="ref" reference="thm:fixed"} is at most $$\label{eq:finalhorizon}
 k_{S_*}+4b^2\le D+1+2D=3D+1=N.$$ If the stated tests through $N$ pass, they include the entire fixed-$S_*$ horizon, so $S_*\in I_g$. That membership plainly implies every finite test. This proves all four equivalences. Proposition [\[prop:period\]](#prop:period){reference-type="ref" reference="prop:period"} gives the asserted visible-period bound. Finally, Lemma [\[lem:monic\]](#lem:monic){reference-type="ref" reference="lem:monic"} transports the conclusions back to every nonmonic input without changing the stated tests.

## Support, constants, and what the bound measures

The numerator and denominator remain whole products throughout the argument. No individual factor is required to satisfy $\mathrm{(CP)}$, and no support multiplicity is reduced modulo $p$. A support cycle containing both a numerator zero and a denominator zero has both products equal to zero at every return. It belongs to no $\mathcal B_n$ and is a permissible finite exception to admissibility. Its period is not bounded by Proposition [\[prop:period\]](#prop:period){reference-type="ref" reference="prop:period"}. A cycle containing only one type of zero is product-visible, so its period is bounded by $D$ when $\mathrm{(CP)}$ holds. Both cases were retained in Proposition [\[prop:ideal\]](#prop:ideal){reference-type="ref" reference="prop:ideal"} and in the persistence proof; the universal polynomial $S_*$ does not silently impose a period bound on every support cycle.

For $m=0$, the formulas give $a=0$, $b=1$, $D=2$, and $N=7$. The low state range is the single state zero; no separate classification of constant weights is needed. In characteristic two, $-1=1$ is still nonzero, so the simple-root and two-product arguments continue unchanged. All return integers $1,\ldots,N$ are tested, not only prime periods or periods prime to $p$.

This is a finite decision rather than only a necessary condition: failure of a specified remainder proves that $\mathrm{(CP)}$ fails, and passing all of them proves $\mathrm{(CP)}$. Computation can use composition, multiplication, and Euclidean remainders in a finite field containing the finitely many input coefficients. No such tests or mathematical experiments are needed for the proof here. The polynomial $S_*$ and the return polynomials can have large degree; no field-size-independent running time, optimal cutoff, or practical census claim is made.

# Conclusion and scope

For derivative-zero polynomial maps over $\overline{\mathbb F}_p$, the ordinary cofinite cycle-product condition for an arbitrary nonzero rational weight is exactly finite. The argument separates the fixed-annihilator problem from the elimination of unknown exceptions: a contracting Laurent-state representation solves the first, while split coefficient rank and return persistence solve the second. Squarefree returns ensure that the final condition concerns ordinary cycles, including native periods divisible by the characteristic.

The theorem is a periodic-data decision. It does not assert the existence of a rational or algebraic transfer function, such as an $h$ with $g=h\circ f/h$, even after a fixed $p$-power. It proves no general separable-map product theorem and makes no claim about Euler factors or root numbers. Extending the ordinary-product conclusion to maps whose return polynomials have characteristic- divisible multiplicities requires an additional argument not supplied by the derivative-filtered interface.

#### Development and verification.

This article was prepared in an AI-assisted collaborative research workflow. Its construction developed from preceding internal fixed-annihilator and rank/persistence arguments and a coordinator's prior general-polynomial two-block/carry/rank/persistence sketch with the proposed constants. The present account supplies the full argument at the stated scope; it does not claim independent origination of that shared construction. The classical normal-form/residue and finite-word principles are credited above. The underlying argument also underwent current-team internal nonauthor mathematical review; this was not external peer review or publication acceptance. Every mathematical dependency needed for the main theorem is proved in this article; no untyped working report or computational certificate substitutes for a proof.
