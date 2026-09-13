---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-survivor-reflection-transversality"
canonical_tex: "henon_dynamics/henon_survivor_reflection_transversality/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_survivor_reflection_transversality/paper/paper.pdf"
source_sha256: "18c6b8449afdfecb93fd864e790e00ed34f75df912efa47d00706aa5b8366bef"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Transverse Reflection Roots on a Certified Hyperbolic Hénon Survivor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_survivor_reflection_transversality>)
- [规范 TeX](<../../../../../henon_dynamics/henon_survivor_reflection_transversality/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_survivor_reflection_transversality/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_survivor_reflection_transversality/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_survivor_reflection_transversality/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the area-preserving Hénon map $H_6(q,p)=(1-6q^2-p,q)$, odd symmetric periodic points are roots of a mixed-axis polynomial $F_n$. We prove that every primitive root lying in a previously certified uniformly hyperbolic four-state survivor is transverse and simple. The proof is geometric: a tangency of the two reversor fixed curves would force eigenvalue $1$ for $DH_6^n$, contradicting hyperbolicity. The symmetry-equivariant coding then gives one root for each primitive reversible necklace, so the physical simple-root population has entropy $\frac12\log\varphi$. The formal mixed-axis degree has entropy $\frac12\log2$; hence physical incidence has density $\Theta((\varphi/2)^{n/2})$ along odd periods. Exact rational isolators through period eleven independently separate all physical and ambient roots. The theorem is local to the survivor: all-period transversality of the ambient algebraic closure remains open.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 14, 2026'
title: Transverse Reflection Roots on a Certified Hyperbolic Hénon Survivor
```

## Markdown 正文

# Introduction

Reversibility turns periodic-orbit equations into intersections of fixed curves of involutions. This viewpoint is classical and remains useful in modern studies of symmetric periodic points [@Kang2014; @YamaguchiTanikawa2005]. It also creates a precise effectivity question: when does an algebraic symmetry-line closure count reduced primitive intersections?

Two predecessor results make that question nontrivial here. First, a certified four-state survivor of $H_6$ is mixing and uniformly hyperbolic. Its primitive reversible cycles have exact entropy $\frac12\log\varphi$. Second, the odd mixed-axis closure satisfies an exact divisor law and has formal primitive degree of entropy $\frac12\log2$. Finite quotients are reduced through period fifteen, but general projective dynatomic effectivity [@Hutz2010] does not automatically attach to this birational symmetry-line slice.

We separate the physical and ambient questions. Our main theorem closes the physical one at every odd period.

[\[thm:main\]]{#thm:main label="thm:main"} Every primitive odd mixed-axis closure root belonging to the certified H6 survivor is simple. The number $P_n$ of such roots is $$P_n=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2},$$ and every one has coefficient $+1$ in the formal mixed-axis dynatomic divisor.

Consequently the physical roots are exponentially sparse in formal degree. This is simultaneously a positive local-effectivity theorem and a warning: hyperbolicity of one real survivor cannot certify the exponentially larger ambient algebraic population.

# Reversors and the mixed-axis closure

Put $f(q)=1-6q^2$ and $$H(q,p)=(f(q)-p,q),\qquad R(q,p)=(p,q),\qquad J=RH.$$ Both $R$ and $J$ are involutions, $RHR=H^{-1}$, and $H=RJ$. The fixed line of $J$ is parameterized by $$\gamma(X)=\left(X,\frac{f(X)}2\right).$$ If $H^j\gamma(X)=(q_j,q_{j-1})$, then $$q_{j+1}=1-6q_j^2-q_{j-1},\qquad q_{-1}=q_1=f(X)/2.$$

Let $n=2m+1$ and $\ell(q,p)=q-p$. Reaching $\operatorname{Fix}(R)$ after $m+1$ iterates is equivalent to $$\label{eq:closure}
F_n(X):=\ell(H^{m+1}\gamma(X))=q_{m+1}(X)-q_m(X)=0.$$ The reversor identities then close a period dividing $n$. Differentiating [\[eq:closure\]](#eq:closure){reference-type="eqref" reference="eq:closure"} gives the exact tangent formula $$\label{eq:tangent}
F_n'(X)=(1,-1)DH^{m+1}(\gamma(X))\gamma'(X).$$ Thus a multiple root is precisely a tangency of $H^{m+1}(\operatorname{Fix}J)$ with $\operatorname{Fix}R$.

# A product-of-involutions tangency lemma

For the odd period $n=2m+1$, define the pulled-back reversor $$K_m=H^{-(m+1)}RH^{m+1}.$$ It is an involution. At a root of $F_n$, $z=\gamma(X)$ lies on both $\operatorname{Fix}(J)$ and $\operatorname{Fix}(K_m)$. Moreover, $$\label{eq:factor}
JK_m=RH H^{-(m+1)}RH^{m+1}=H^mH^{m+1}=H^n.$$

[\[lem:tangent\]]{#lem:tangent label="lem:tangent"} If $F_n(X)=F_n'(X)=0$, then $1$ is an eigenvalue of $DH^n(\gamma(X))$.

The nonzero vector $v=\gamma'(X)$ spans the tangent of $\operatorname{Fix}(J)$, so $DJ(z)v=v$. Equation [\[eq:tangent\]](#eq:tangent){reference-type="eqref" reference="eq:tangent"} says that $DH^{m+1}(z)v$ is tangent to $\operatorname{Fix}(R)$. Pulling back gives $DK_m(z)v=v$. Differentiating [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} now yields $DH^n(z)v=DJ(z)DK_m(z)v=v$.

Only this implication is needed. For arbitrary linear involutions, a parabolic product can have eigenvalue one without coincidence of their positive eigendirections; we therefore do not assert the converse.

[\[cor:hyperbolic\]]{#cor:hyperbolic label="cor:hyperbolic"} Every odd mixed-axis closure root in the certified uniformly hyperbolic H6 survivor is simple.

Every periodic monodromy on a uniformly hyperbolic set has one multiplier of modulus greater than one and one of modulus less than one. Lemma [\[lem:tangent\]](#lem:tangent){reference-type="ref" reference="lem:tangent"} would instead supply multiplier one.

# One physical root per reversible necklace

Label the four state rectangles by the sign pairs $--,-+,+-,++$. Swapping $(q,p)$ fixes the first and fourth labels and interchanges the middle two, exactly the symbol involution $\rho=(0)(1\ 2)(3)$. The signed-square-root construction gives a unique orbit for every admissible itinerary. Applying a geometric reversor thus produces the unique orbit with the reversed $\rho$-itinerary, proving that the coding is symmetry equivariant. In particular, a fixed symbolic reflection gives a geometric point on its calibrated fixed axis.

At odd period every reflection axis is conjugate under rotation. A primitive necklace cannot be fixed by two distinct reflections, because their product would be a nontrivial stabilizing rotation. Therefore its $n$ representatives occur one-to-one on the $n$ axes, and exactly one representative lies on the axis calibrated to $\operatorname{Fix}(J)$.

[\[prop:incidence\]]{#prop:incidence label="prop:incidence"} For odd $n$, the number of distinct primitive roots of $F_n$ in the survivor is $$\label{eq:Pn}
P_n=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2}.$$ Every such root has local coefficient $+1$ in the formal primitive divisor.

The preceding axis argument identifies the roots bijectively with the exact primitive reversible-necklace census, giving [\[eq:Pn\]](#eq:Pn){reference-type="eqref" reference="eq:Pn"}. Distinct necklaces give distinct periodic points, while $X$ parameterizes $\operatorname{Fix}(J)$ injectively. A primitive period-$n$ point is absent from every proper-divisor closure. Corollary [\[cor:hyperbolic\]](#cor:hyperbolic){reference-type="ref" reference="cor:hyperbolic"} gives multiplicity one in $F_n$, so Möbius subtraction leaves coefficient $+1$.

# The incidence entropy gap

The exact reflection census and the formal degree theorem give, along odd periods, $$P_n=\Theta(\varphi^{n/2}),\qquad
D_n=2^{(n+1)/2}+O(n2^{n/6+1/2}).$$ Hence $$\label{eq:density}
\frac{P_n}{D_n}=\Theta\!\left((\varphi/2)^{n/2}\right),
\qquad
\lim_{\substack{n\to\infty\\ n\ \mathrm{odd}}}
\frac1n\log\frac{D_n}{P_n}=\frac12\log\frac2\varphi>0.$$

Since $P_n=o(D_n)$, the formal residual degree $D_n-P_n$ has entropy $\frac12\log2$. This statement is intentionally about divisor degree. It does not promote the residual to a set of distinct roots: outside the survivor, multiplicities and cancellations are still uncontrolled.

Equation [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"} explains why the local theorem cannot settle the global problem by a small correction. Even complete control of every physical reversible orbit addresses an exponentially vanishing fraction of the formal algebraic degree.

# Exact finite certification

The primary implementation reconstructs the closure and primitive quotient without importing predecessor code. Every quotient root through odd period eleven is isolated in a disjoint rational interval of width below $10^{-40}$. Exact interval recurrence classifies the whole orbit against $$\frac{\sqrt{17}}{12}<|q_j|<\sqrt{\frac38},$$ the strict interior of the certified state rectangles. Interval Horner evaluation excludes zero from $F_n'$ at every physical root.

    $n$   $D_n$   physical simple roots $P_n$   residual degree   excluded roots
  ----- ------- ----------------------------- ----------------- ----------------
      1       2                             1                 1                1
      3       2                             1                 1                1
      5       6                             2                 4                4
      7      14                             4                10               10
      9      28                             6                22               22
     11      62                            12                50               50

  : Exact primitive-degree and physical-incidence ledger.

In these six rows all primitive roots are real and simple, so the finite residual degree is also the number excluded from the survivor band. This finite equality is not extrapolated to all periods. A separate checker enumerates all primitive reversible necklaces by Cartesian search and classifies 50-digit roots; it reproduces every count and physical sign word.

# Ambient effectivity remains a separate theorem

The local transversality proof cannot be applied to a root outside the certified survivor: its real orbit may leave the isolating rectangles, or the root may be complex, and no inherited hyperbolic splitting is available. Thus Corollary [\[cor:hyperbolic\]](#cor:hyperbolic){reference-type="ref" reference="cor:hyperbolic"} does not prove that every $F_n$ is squarefree or that the formal Möbius divisor is globally effective.

The narrow next object is the critical resultant $$\operatorname{Res}_X(F_n,F_n').$$ A nonzero all-period formula would close ambient reducedness. More informatively, a divisor-level factorization could identify whether a first zero comes from a genuine primitive tangency or inherited lower-period intersection multiplicity. That is an algebraic recurrence problem, not a consequence of physical pressure.

Nor does simple-root incidence attach Galois heights, rational-prime labels, a completed determinant or a self-adjoint operator. The result strengthens the physical analytic layer of Route A only.

# Reproducibility and hostile controls

The certificate locks six P60 artifacts, the P59 reflection census and three independent hyperbolicity artifacts. Its canonical mathematical payload is SHA-256 frozen. Twenty-two mutations test the tangent sign, involution order, neutral multiplier, entropy rates, finite counts, interval hashes and every claim-promotion boundary.

The independent checker imports no primary research code. It rebuilds the quotients, enumerates symbolic necklaces directly and classifies roots at 50 digits. Unit tests bind the all-period theorem, exact rows, interval transversality, mutation trace and disabled ambient/Route-B claims. All commands are listed in the project README.

# Conclusion

The physical part of the reflection-dynatomic effectivity problem is now closed: every primitive odd reversible orbit in the certified H6 survivor meets the mixed axes transversely and contributes one simple root. The exact population is the reversible-necklace count and has entropy $\frac12\log\varphi$.

The comparison with formal entropy $\frac12\log2$ is equally decisive. Physical roots are exponentially sparse, so ambient effectivity and Galois height cannot be recovered from local survivor hyperbolicity alone. The next rigorous target is therefore the ambient critical resultant, with physical incidence retained as a protected factor rather than used as a surrogate for the whole algebraic population.

# Exact status ledger

  Statement                                         Status
  ------------------------------------------------- ------------------------------
  Tangency implies multiplier $+1$                  proved, all odd periods
  Survivor roots are transverse/simple              proved, all odd periods
  One root per primitive reversible necklace        proved
  Physical local divisor coefficient $+1$           proved
  Physical entropy $\frac12\log\varphi$             proved, inherited census
  Formal entropy $\frac12\log2$                     proved, inherited degree law
  Exact band classification through $n=11$          computer-certified exact
  Ambient all-period squarefreeness/effectivity     open
  Galois-height pressure and rational-prime trace   open
  Route-B operator correspondence                   not testable
