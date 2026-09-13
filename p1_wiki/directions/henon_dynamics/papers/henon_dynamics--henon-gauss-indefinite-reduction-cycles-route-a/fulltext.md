---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-gauss-indefinite-reduction-cycles-route-a"
canonical_tex: "henon_dynamics/henon_gauss_indefinite_reduction_cycles_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_gauss_indefinite_reduction_cycles_route_a/paper/main.pdf"
source_sha256: "9bbd890030ecc782f8479315bd6d24c5d00feb451f17d350c823d4a967bac1ed"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fixed-Discriminant Gauss Reduction: Cycles, Stabilizers, Reversal, and a Finite Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_gauss_indefinite_reduction_cycles_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_gauss_indefinite_reduction_cycles_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_gauss_indefinite_reduction_cycles_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_gauss_indefinite_reduction_cycles_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At one positive nonsquare binary-form discriminant we freeze an exact primitive reduced phase space and prove that the Gauss shift is its permutation. Every orbit has a primitive continued-fraction word whose positive matrix product is a hyperbolic stabilizer; the same matrix gives an exact cycle multiplier and its discriminant identity. \>0 Conjugate reciprocity reverses the dynamics, while the complete cycle inventory yields every fixed-point count, the finite Artin--Mazur zeta, and the Koopman determinant. \>1 Square, zero, negative, invalid-congruence, imprimitive, and norm-sign faces are closed explicitly. No class-group convention or target arithmetic is silently imported. Finite exact computations audit conventions only; the theorem is analytic.
author:
- 'HCS-C364 source-local theorem package'
date: 'September 4, 2026'
title: 'Fixed-Discriminant Gauss Reduction: Cycles, Stabilizers, Reversal, and a Finite Determinant'
```

## Markdown 正文

trailerid \[\<C3642026090400000000000000000000\>\<C3642026090400000000000000000000\>\]

# The convention and the finite phase space

Fix a positive nonsquare integer $\Delta\equiv0,1\pmod4$. Let $\mathcal R_\Delta$ contain the numbers $$\label{eq:state}
 \alpha=\frac{P+\sqrt\Delta}{Q},\qquad Q=2A>0,
 \qquad A=\frac Q2,\quad B=-P,\quad C=\frac{P^2-\Delta}{2Q},$$ for which $A,B,C\in\mathbb Z$, $\gcd(A,B,C)=1$, and $$\label{eq:reduced}
 \alpha>1,\qquad -1<\bar\alpha=\frac{P-\sqrt\Delta}{Q}<0.$$ The polynomial $Ax^2+Bx+C$ has discriminant exactly $\Delta$ and roots $(P\pm\sqrt\Delta)/Q$. Thus [\[eq:state\]](#eq:state){reference-type="eqref" reference="eq:state"} is a binary-form discriminant convention, not a radicand convention that accidentally changes the discriminant to $4\Delta$.

Define $$\label{eq:gauss}
 G(\alpha)=\frac1{\alpha-\lfloor\alpha\rfloor}.$$

[\[thm:main\]]{#thm:main label="thm:main"} The set $\mathcal R_\Delta$ is finite and $G$ is a bijection. Let $\alpha_0,\ldots,\alpha_{\ell-1}$ be a minimal cycle and $a_j=\lfloor\alpha_j\rfloor$. Let $A(a)$ denote the two-by-two matrix with rows $(a,1)$ and $(1,0)$. Then $$\label{eq:matrix}
 M=A(a_0)A(a_1)\cdots A(a_{\ell-1}).$$ Writing $M_{11}=a,M_{12}=b,M_{21}=c,M_{22}=d$, this matrix fixes $\alpha_0$, has $\det M=(-1)^\ell$, and is the primitive positive inverse-branch stabilizer. For some integer $k>0$, $$\label{eq:disc}
 (c,d-a,-b)=k(A,B,C),\qquad
 (\operatorname{tr}M)^2-4\det M=k^2\Delta.$$ If $\lambda=c\alpha_0+d$, then $\lambda>1$ and $$\label{eq:multiplier}
 \left|(G^\ell)'(\alpha_0)\right|=\lambda^2.$$

From [\[eq:reduced\]](#eq:reduced){reference-type="eqref" reference="eq:reduced"}, $|P|<\sqrt\Delta$ and $0<Q<P+\sqrt\Delta<2\sqrt\Delta$, proving finiteness. Put $a=\lfloor\alpha\rfloor$, $$\label{eq:update}
 P_1=aQ-P,\qquad Q_1=\frac{\Delta-P_1^2}{Q}.$$ Rationalization gives $G(\alpha)=(P_1+\sqrt\Delta)/Q_1$. Because $0<\alpha-a<1$, this root exceeds one; because $-a-1<\bar\alpha-a<-a$, its conjugate lies in $(-1,0)$. The original integrality says $2Q\mid P^2-\Delta$, while $P_1^2-P^2=a^2Q^2-2aPQ$ is divisible by $2Q$; hence $Q_1$ is positive and even and the new form is integral. The inverse branch $x\mapsto a+1/x$ is unimodular, so form content, and hence primitivity, is preserved.

Conversely, for reduced $\beta$, set $$\label{eq:predecessor}
 t=-1/\bar\beta,\qquad a=\lfloor t\rfloor,\qquad
 \alpha=a+1/\beta.$$ Here $t>1$ is irrational, so $\alpha>1$ and $\bar\alpha=a-t\in(-1,0)$. The inverse unimodular substitution preserves the integral primitive form and $G(\alpha)=\beta$. The conjugate interval determines $a$ uniquely, proving bijectivity.

Writing $H_a(x)=a+1/x$, one has $\alpha_j=H_{a_j}(\alpha_{j+1})$; therefore [\[eq:matrix\]](#eq:matrix){reference-type="eqref" reference="eq:matrix"} fixes $\alpha_0$. A shorter digit word would, by uniqueness of an infinite simple continued fraction, give a shorter state return. Each factor has determinant minus one. The integral stabilizer of a real quadratic irrational maps through $N\mapsto c_N\alpha+d_N$, after choosing the positive representative, to units of its quadratic order that are positive at the $\alpha$-embedding. We use the classical reduction--automorph cross-section lemma in its exact return form: an expanding positive projective stabilizer preserves the oriented geodesic from $\bar\alpha$ to $\alpha$ and advances its reduced cross-section by an integer $r\geq1$ of complete Gauss digits. Thus $$[N]=[A(a_0)\cdots A(a_{r-1})],\qquad G^r(\alpha_0)=\alpha_0,$$ and every complete return gives such a stabilizer. This standard continued-fraction correspondence is source-anchored to Uspensky and Buell below. Minimality of $\ell$ makes every $r=n\ell$, and periodicity makes the corresponding product $M^n$; a representative first written with mixed signs therefore cannot yield a smaller positive return. Hence $M$ generates the positive projective stabilizer. Since $\det(M^n)=(-1)^{\ell n}$, the determinant-one stabilizer up to $\pm I$ is generated by $M$ for even $\ell$ and by $M^2$ for odd $\ell$.

The fixed-point equation of $M$ is $cx^2+(d-a)x-b=0$. Its coefficient vector is an integral multiple of the primitive vector $(A,B,C)$, giving [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"}. Finally $M'(\alpha)=\det M/(c\alpha+d)^2$; since $M$ is the local inverse of $G^\ell$, reciprocal differentiation gives [\[eq:multiplier\]](#eq:multiplier){reference-type="eqref" reference="eq:multiplier"}. Positive digit matrices give $\lambda>1$. This is the *reduced-permutation owner*.

\>0

# Reversal and the complete determinant

Define $$\label{eq:reversal}
 R(\alpha)=-\frac1{\bar\alpha},\qquad
 R(P,Q)=(P,(\Delta-P^2)/Q).$$

[\[prop:reverse\]]{#prop:reverse label="prop:reverse"} The map $R$ preserves $\mathcal R_\Delta$, satisfies $R^2=1$, and $RGR=G^{-1}$. It sends every cycle word to its reversal.

The two inequalities in [\[eq:reduced\]](#eq:reduced){reference-type="eqref" reference="eq:reduced"} are exchanged by conjugate reciprocity; rationalization gives the pair formula in [\[eq:reversal\]](#eq:reversal){reference-type="eqref" reference="eq:reversal"}, from which $R^2=1$. Since the digit matrices are symmetric, transposing $A(a_0)\cdots A(a_{\ell-1})$ reverses its word. Equivalently, $$[\overline{a_0,\ldots,a_{\ell-1}}]
 \longmapsto
 [\overline{a_{\ell-1},\ldots,a_0}].$$ Reversal conjugates a left shift to a right shift, proving $RGR=G^{-1}$.

Let $c_m$ count cycles of length $m$, and let $U_Gf=f\circ G$ on $\ell^2(\mathcal R_\Delta)$. A length-$m$ cycle contributes all its states to $\operatorname{Fix}(G^n)$ exactly when $m\mid n$, hence $$\label{eq:fixed}
 \#\operatorname{Fix}(G^n)=\sum_{m\mid n}m c_m.$$ Substitution into the finite Artin--Mazur definition, followed by the determinant of a cyclic permutation matrix, gives $$\label{eq:zeta}
 \zeta_{G,\Delta}(z)=\prod_m(1-z^m)^{-c_m},
 \qquad
 \det(I-zU_G)=\prod_m(1-z^m)^{c_m}=\zeta_{G,\Delta}(z)^{-1}.$$ This is the *reversal-determinant owner*. It is a finite source cycle identity, not an Euler product over rational primes.

# Exact regression receipt

An independent implementation enumerates primitive form coefficients rather than the producer's pair loop. For all 469 admissible discriminants through 1000, it checks 5,387 states, 775 complete cycles, 11,256 fixed-power rows, the update and inverse, $RGR=G^{-1}$, every matrix identity in [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"}, and every factor in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. The independent checker passes 117,887 assertions; a separate SymPy lane passes 3,403 exact identities; 47 repaired-hash attacks are rejected. Two isolated directories reproduce the same 3,307,442 evidence bytes. These finite facts test conventions; they do not prove the infinite family.

\>1

# Boundary atlas and Route-A interpretation

The theorem has six sharp boundary rules.

1.  If $\Delta=s^2>0$, the roots are rational and the regular continued fraction terminates. There is no reduced-quadratic-irrational permutation.

2.  At $\Delta=0$ the polynomial has a repeated rational root. For $\Delta<0$ it has no ordered real conjugates.

3.  Integers $2$ or $3\pmod4$ are not discriminants of integral binary quadratic forms.

4.  The primitive filter is structural: $[2,-2,-2]$, of discriminant 20, divides to $[1,-1,-1]$, of discriminant 5. Dropping content one would duplicate a lower-discriminant state.

5.  If $\ell$ is odd, $\det M=-1$; the determinant-one stabilizer is generated by $M^2$, not $M$. For even $\ell$, it is generated by $M$, up to $\pm I$.

6.  No proper-class or narrow-class bijection is claimed. Such a bridge would require a separate orientation and nonmaximal-order convention audit.

This is the *boundary-firewall owner*.

The strict evaluator tuple is $$(\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},
  \mathrm{A1\_PASS\_ANALYTIC},
  \mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},
  \mathrm{A4\_FORMAL\_HINT}).$$ The source has genuine quadratic-order arithmetic and a complete analytic cycle taxonomy. Its finite determinant is not a target divisor, and the finite unitary Koopman permutation is only a formal operator hint. Overall Route A is exploratory. Route B is false. No target arithmetic local data, target Euler factor, root number, automorphy, target functional equation, target-zero match, or Hilbert--Pólya operator is claimed.

# Source and collision boundary {#source-and-collision-boundary .unnumbered}

Uspensky's reduction paper appears in the *Bulletin of the AMS* (1930), 710--718, [doi:10.1090/S0002-9904-1930-05043-0](https://doi.org/10.1090/S0002-9904-1930-05043-0). Buell's chapter "Indefinite Forms" fixes authoritative form conventions, [doi:10.1007/978-1-4612-4542-1\_3](https://doi.org/10.1007/978-1-4612-4542-1_3). Zagier supplies real-quadratic arithmetic context, [doi:10.1007/978-3-642-61829-1](https://doi.org/10.1007/978-3-642-61829-1). These sources establish lineage, not priority for this packaging. C16 uses continued fractions in an S-arithmetic clock, C193 is a Markoff--Vieta descent tree, and C330 is Romik's Pythagorean map; none owns this fixed-discriminant finite reduction permutation.
