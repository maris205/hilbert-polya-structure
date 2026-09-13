---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--10-cat-centralizer-quotient"
canonical_tex: "symplectic_map/papers/10-cat-centralizer-quotient/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/10-cat-centralizer-quotient/paper/manuscript.pdf"
source_sha256: "65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Centralizer-Quotient Audit for Cat-Map Torsion Shells

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient>)
- [规范 TeX](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the standard cat matrix $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$, we test whether centralizer symmetry can turn a finite torsion shell into one intrinsic arithmetic Euler factor. The vector $e_1$ is cyclic over $\mathbb Z/q\mathbb Z$ for every $q\ge2$; hence the commutant is $R_q[A]$, whose unit group acts simply transitively on the cyclic-vector locus. The full-centralizer quotient has one class, but it also divides out $A$, so the induced map is the identity with primitive period one. Replacing its formal variable by $q^{-s}$ therefore supplies the modulus clock externally. The symplectic centralizer instead leaves norm classes, numbering $\varphi(q)$ when $5\nmid q$ and $\varphi(q)/2$ when $5\mid q$, while its induced dynamics is still trivial. Over prime fields, the full nonzero shell has one, three, or two full-centralizer strata in the inert, split, or ramified cases. A source-locked exact audit at five primes and four predeclared composites matches the proof-controlled ledger; the same one-class construction holds at composites. Thus this deliberately modest structural audit supplies neither a prime selector nor a native $\log q$ clock and closes only the coarse full-centralizer route. Enriched equivariant, orbifold, groupoid, Hecke, and quantized refinements remain untested.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'Pre-review manuscript, August 15, 2026'
title: 'A Centralizer-Quotient Audit for Cat-Map Torsion Shells'
```

## Markdown 正文

**Keywords:** cat map, finite-module centralizer, cyclic-vector torsor, norm class, quotient dynamics, arithmetic Euler factor.

# Introduction and bounded question {#sec:introduction}

Let $T_A\colon\mathbb{T}^{2}\to\mathbb{T}^{2}$ be the toral automorphism induced by $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
  \label{eq:cat-matrix}$$ For an integer $q\ge2$, write $R_q=\mathbb{Z}/q\mathbb{Z}$ and view $A$ as an automorphism of $R_q^2$. Earlier multiplicity analysis leaves a natural escape: perhaps a symmetry quotient can compress the many $A$-orbits on a torsion shell to one local object. The bounded question here is whether the finite-module centralizer supplies that compression without importing the modulus label or discarding the native dynamics.

The answer separates an exact algebraic success from a dynamical failure. There is a natural cyclic-vector locus on which the full centralizer acts simply transitively. Its coarse quotient is one point. However, the group being divided out contains $A$, so the quotient map is the identity and has period one for every modulus. If one instead restricts to determinant one, the quotient retains norm classes but still no nontrivial motion. The mechanism therefore removes multiplicity only by removing the clock that was supposed to generate a modulus-dependent local factor.

## Prior-art boundary

This audit assembles established ingredients rather than proposing a new centralizer classification. The closest algebraic collision is @BaakeNeumaerkerRoberts2013. Their rational-lattice framework treats finite cat-map symmetries, cyclic-matrix commutants, finite-field normal types, reversing groups, and prime-power orbit data. In particular, the field-level split, inert, and Jordan cases below are classical. Our fixed-matrix proof over every $R_q$ serves the audit by making the cyclic-vector torsor and its construction cost explicit. It is not a claim that cyclic commutants or finite-lattice symmetry groups were previously unknown. General ring centralizers require care over zero divisors, while regular-matrix and companion-ring work supplies the broader terminology and context [@Marais2014; @Stasinski2016; @NoferiniWilliams2024]; none of those sources substitutes for the fixed-basis proof below.

The determinant-one layer has an equally direct precedent. Norm-one elements of quadratic orders modulo the quantization level form the Hecke centralizers used by @KurlbergRudnick2000. That work prevents us from presenting $C_q^1$, the norm formula, or the local arithmetic split as a new Hecke mechanism. The invariant-form formulation is also established in the quantum cat-map setting [@KurlbergRosenzweigRudnick2007]. We instead give an elementary proof for the specific order $R_q[T]/(T^2-3T+1)$ and use it only to show what remains after the full $\mathrm{GL}_2$ centralizer is restricted to $\mathrm{SL}_2$.

The quotient-dynamical observation also has decisive direct prior art. @GuseinZadeLuengoMelle2015 explicitly separates transformation order in a space from order in its quotient and notes the trivial induced action when the transformation belongs to the acting group. Their Burnside-ring, equivariant, and orbifold refinements retain information absent from the coarse quotient. Quotient closed-orbit semantics and group-action zeta functions provide further adjacent boundaries [@Zegowitz2017; @Miles2017]. Accordingly, the clock-erasure statement below is an application of a known quotient principle to this frozen Route-A candidate, not a new zeta definition or an impossibility result for enriched quotients.

Prime-lattice orbit structure is classical [@Gaspari1994], as are finite and rational-lattice cycle products [@BaakeRobertsWeiss2008]. Recent prime-power cycle analysis [@TanLi2025] and finite-torus determinant packaging [@Chandra2026] further rule out broad finite-ring or cycle-product novelty. These sources do not make the present negative decision for us, but they sharply limit its defensible contribution to the explicit full-versus-symplectic quotient comparison and the resulting semantic audit.

The note's contribution is consequently diagnostic and deliberately modest:

1.  give an all-$q$, field-free proof that the cyclic-vector locus is a torsor under the full local centralizer.

2.  prove that its one-class coarse quotient has identity induced dynamics, so $z=q^{-s}$ is an external specialization rather than a return-time law.

3.  identify the symplectic quotient with the image of a quadratic norm and determine its exact size, including the binary and ramified-five boundaries.

4.  separate the cyclic locus from the complete prime shell, classify the full-centralizer and reversing strata, and extend the count formulas to composite moduli by Chinese remaindering.

5.  record a one-shot, development-seen exact audit as an implementation control without using nine finite rows to prove an all-$q$ theorem.

The scope exclusions are part of the claim. We do not define a new equivariant, Burnside, orbifold, stacky, groupoid, or twisted-sector zeta function. We do not construct Hecke operators, a quantization, a transfer operator, a Fredholm determinant, a prime selector, a prime--zero correspondence, or a Riemann-hypothesis mechanism. The note makes no historical-priority claim. It evaluates only the coarse quotient and the closely related determinant-one quotient for the frozen matrix [\[eq:cat-matrix\]](#eq:cat-matrix){reference-type="eqref" reference="eq:cat-matrix"}.

Section [2](#sec:setup){reference-type="ref" reference="sec:setup"} fixes the three symmetry layers. Section [3](#sec:torsor){reference-type="ref" reference="sec:torsor"} proves the centralizer torsor. Section [4](#sec:quotient){reference-type="ref" reference="sec:quotient"} separates quotient cardinality from quotient dynamics. Section [5](#sec:strata){reference-type="ref" reference="sec:strata"} treats the complete prime shell and reversal. Section [6](#sec:composite-audit){reference-type="ref" reference="sec:composite-audit"} gives the composite formulas and the registered exact ledger. Section [7](#sec:decision){reference-type="ref" reference="sec:decision"} states the route decision and its limitations.

# Setup and three symmetry layers {#sec:setup}

Define the exact additive-order shell $$E_q=\{v\in R_q^2:\operatorname{ord}_+(v)=q\}.
  \label{eq:exact-shell}$$ The cyclic determinant and cyclic-vector locus are $$\Delta_q(v)=\det[v,Av],
  \qquad
  \mathrm{CV}_q=\{v\in R_q^2:\Delta_q(v)\in R_q^\times\}.
  \label{eq:cyclic-locus}$$ Thus $v\in\mathrm{CV}_q$ precisely when $(v,Av)$ is an $R_q$-basis. The distinction $\mathrm{CV}_q\subseteq E_q$ will matter: equality holds in the inert cases below, but it fails at split and ramified primes.

We use three different symmetry groups. The full commuting group is $$C_q=\operatorname{Cent}_{\mathrm{GL}_2(R_q)}(A).
  \label{eq:full-centralizer}$$ The symplectic commuting group is $$C_q^1=C_q\cap\mathrm{Sp}_2(R_q)=C_q\cap\mathrm{SL}_2(R_q),
  \label{eq:symplectic-centralizer}$$ where the equality follows from $D^t\Omega D=(\det D)\Omega$ in dimension two. For a prime $p$, the reversing group is $$\mathcal R_p(A)=
  \{G\in\mathrm{GL}_2(\mathbb{F}_p):GAG^{-1}=A^{\pm1}\}.
  \label{eq:reversing-group}$$ The first two groups commute with $A$, while the third also permits time reversal. Conflating these layers would conceal both the determinant cost of the one-class quotient and the limits of the reversor.

The characteristic identity $$A^2-3A+I=0
  \label{eq:characteristic}$$ defines the quadratic algebra $$S_q=R_q[T]/(T^2-3T+1).
  \label{eq:quadratic-algebra}$$ For $a,b\in R_q$, its norm is $$N_q(a+bT)=a^2+3ab+b^2.
  \label{eq:norm}$$ The discriminant is five, so the local algebra is split, inert, or ramified according to the behavior of five at the relevant prime.

# Universal cyclic basis and the centralizer torsor {#sec:torsor}

The key field-free fact is visible in one determinant: $$e_1=\binom10,
  \qquad
  Ae_1=\binom21,
  \qquad
  P=[e_1,Ae_1]=\begin{pmatrix}1&2\\0&1\end{pmatrix},
  \qquad \det P=1.
  \label{eq:universal-cyclic-basis}$$ Hence $(e_1,Ae_1)$ is a basis over every $R_q$, including nonfields and nonreduced residue rings.

[\[thm:torsor\]]{#thm:torsor label="thm:torsor"} For every integer $q\ge2$, the following statements hold.

1.  The full matrix commutant is $\operatorname{Cent}_{\operatorname{Mat}_2(R_q)}(A)=R_q[A]$, and $C_q=R_q[A]^\times$.

2.  The map $$C_q\longrightarrow\mathrm{CV}_q,
              \qquad U\longmapsto Ue_1,
              \label{eq:torsor-map}$$ is a $C_q$-equivariant bijection. Thus $\mathrm{CV}_q$ is a $C_q$-torsor.

3.  Every cyclic vector has exact additive order $q$, so $\mathrm{CV}_q\subseteq E_q$.

4.  Every $A$-orbit in $\mathrm{CV}_q$ has length $\operatorname{ord}_q(A)$, and the orbit set is $$\Gamma_q^{\mathrm{cyc}}
              \simeq C_q/\langle A\rangle.
              \label{eq:A-orbit-cosets}$$

Let $X\in\operatorname{Mat}_2(R_q)$ commute with $A$. There are unique $a,b\in R_q$ such that $Xe_1=ae_1+bAe_1$. Commutation determines the other basis vector: $$X(Ae_1)=A(Xe_1)=aAe_1+bA^2e_1.$$ Therefore $X$ and $aI+bA$ agree on the basis $(e_1,Ae_1)$, which proves $\operatorname{Cent}_{\operatorname{Mat}_2(R_q)}(A)=R_q[A]$. Taking units gives $C_q=R_q[A]^\times$. No division or field hypothesis enters this argument.

Every $v\in R_q^2$ is uniquely $v=Ue_1$ for some $U=aI+bA\in R_q[A]$. Because $U$ commutes with $A$, $$=[Ue_1,AUe_1]=U[e_1,Ae_1]=UP,
  \qquad
  \Delta_q(v)=\det U.
  \label{eq:delta-is-determinant}$$ A square matrix over the finite commutative ring $R_q$ is invertible exactly when its determinant is a unit. Hence $v\in\mathrm{CV}_q$ if and only if $U\in C_q$, proving bijectivity of [\[eq:torsor-map\]](#eq:torsor-map){reference-type="eqref" reference="eq:torsor-map"}. Left multiplication is then free and transitive.

A cyclic vector is a member of an $R_q$-basis and is therefore unimodular. Its reduction modulo every prime divisor of $q$ is nonzero. Componentwise over each $p^k\parallel q$, at least one coordinate is a unit and has additive order $p^k$. Chinese remaindering gives global additive order $q$, proving $\mathrm{CV}_q\subseteq E_q$.

Under $\mathrm{CV}_q\simeq C_q$, the matrix $A$ acts by multiplication by $A\in C_q$. If $A^kUe_1=Ue_1$, then commutativity and invertibility of $U$ give $A^ke_1=e_1$. The same equality applied after $A$ shows that $A^k$ fixes the cyclic basis, so $A^k=I$. Every orbit therefore has exact length $\operatorname{ord}_q(A)$, and its orbit set is the coset space in [\[eq:A-orbit-cosets\]](#eq:A-orbit-cosets){reference-type="eqref" reference="eq:A-orbit-cosets"}.

Theorem [\[thm:torsor\]](#thm:torsor){reference-type="ref" reference="thm:torsor"} is an explicit fixed-matrix derivation of standard cyclic-module algebra. It is not presented as a new cyclic-matrix theorem. Its role is to make the later quotient and its construction cost completely visible. Finite-lattice cyclic commutants, rational-lattice centralizers, and reversing symmetries have a substantial prior theory [@BaakeNeumaerkerRoberts2013]; the proof here is scoped to the frozen matrix and every residue ring $R_q$.

# Coarse quotient dynamics and the symplectic boundary {#sec:quotient}

## Multiplicity one also kills the clock

Because $R_q[A]$ is commutative, the residual group $C_q/\langle A\rangle$ acts simply transitively on $\Gamma_q^{\mathrm{cyc}}$. Equivalently, $$\mathrm{CV}_q/C_q=\{*\}.
  \label{eq:one-point-quotient}$$ This is the desired set-theoretic multiplicity-one statement.

It is not a retained source orbit. Since $A\in C_q$, the induced map on the quotient is $$\bar A(*)=*.
  \label{eq:identity-quotient-map}$$ The ordinary Artin--Mazur zeta of this one-point map is $$\zeta_{\bar A}(z)
  =\exp\!\left(\sum_{n\ge1}\frac{z^n}{n}\right)
  =(1-z)^{-1}.
  \label{eq:one-point-zeta}$$ Its primitive period is one for every $q$. The original period $\operatorname{ord}_q(A)$ and the original number $|C_q|/\operatorname{ord}_q(A)$ of cyclic $A$-orbits have both disappeared. Consequently $$z=q^{-s}
  \label{eq:external-specialization}$$ is an external modulus specialization. It is not a Birkhoff sum, quotient return period, monodromy invariant, or other datum of [\[eq:identity-quotient-map\]](#eq:identity-quotient-map){reference-type="eqref" reference="eq:identity-quotient-map"}. This clock-erasure mechanism is a direct instance of the coarse-quotient distinction already emphasized in the equivariant-zeta and quotient-orbit literature [@GuseinZadeLuengoMelle2015; @Zegowitz2017].

## The determinant-one quotient leaves norm classes

The assignment $T\mapsto A$ gives an algebra isomorphism $$S_q\xrightarrow{\sim}R_q[A].
  \label{eq:algebra-isomorphism}$$ Indeed, the map is onto and both displayed bases have rank two. The cyclic basis also shows directly that $I$ and $A$ are independent. For $U=aI+bA$, a determinant calculation gives $$\det U=a^2+3ab+b^2=N_q(a+bT).
  \label{eq:determinant-norm}$$ Thus $$C_q^1=\ker\!\left(N_q:S_q^\times\to R_q^\times\right).
  \label{eq:norm-one-centralizer}$$ This is the elementary finite-module counterpart of the familiar norm-one centralizers used in quantum cat-map Hecke theory [@KurlbergRudnick2000]. No Hecke or quantum claim is made here.

[\[thm:symplectic-quotient\]]{#thm:symplectic-quotient label="thm:symplectic-quotient"} For every $q\ge2$, the fibers of $\Delta_q$ on $\mathrm{CV}_q$ are exactly the $C_q^1$-orbits. Hence $$\mathrm{CV}_q/C_q^1\simeq\operatorname{im}N_q.
  \label{eq:symplectic-quotient}$$ Moreover, $$|\operatorname{im}N_q|=
  \begin{cases}
    \varphi(q),&5\nmid q,\\
    \varphi(q)/2,&5\mid q.
  \end{cases}
  \label{eq:norm-image-cardinality}$$ The induced action of $A$ on every quotient class is the identity.

For $D\in C_q$ and $v\in\mathrm{CV}_q$, commutation gives $$\Delta_q(Dv)
  =\det[Dv,ADv]
  =\det D\,\Delta_q(v).
  \label{eq:delta-covariance}$$ In particular $C_q^1$ preserves $\Delta_q$. Conversely, write $v=Ue_1$ and $w=Ve_1$ under the torsor identification. Equation [\[eq:delta-is-determinant\]](#eq:delta-is-determinant){reference-type="eqref" reference="eq:delta-is-determinant"} gives $\Delta_q(v)=N_q(U)$ and $\Delta_q(w)=N_q(V)$. These values agree exactly when $N_q(VU^{-1})=1$, or equivalently when $VU^{-1}\in C_q^1$. The fibers are therefore the symplectic-centralizer orbits, proving [\[eq:symplectic-quotient\]](#eq:symplectic-quotient){reference-type="eqref" reference="eq:symplectic-quotient"}.

Write $q=\prod p^{k_p}$. Chinese remaindering decomposes both $S_q$ and its norm into the corresponding local factors. If $p\ne5$, the quadratic algebra is etale. In the split case its norm $(u,v)\mapsto uv$ is onto. In the inert case, the residue-field norm is onto and the trace maps on successive principal-unit quotients are onto, so the unit norm is onto at every $p^k$. This includes $p=2$, where $T^2+T+1$ is irreducible over $\mathbb{F}_2$.

At $p=5$, put $\pi=2T-3$. Then $\pi^2=5$, every element is uniquely $c+d\pi$, and $$N(c+d\pi)=c^2-5d^2.
  \label{eq:ramified-norm}$$ The residue of a unit norm modulo five is therefore a square. Conversely, every unit with square residue modulo five has a square root modulo $5^k$ by Hensel lifting. A scalar square root realizes that unit as a norm. The local image is the index-two subgroup of units with square residue. The Chinese remainder product proves [\[eq:norm-image-cardinality\]](#eq:norm-image-cardinality){reference-type="eqref" reference="eq:norm-image-cardinality"}.

Finally, $A\in C_q^1$ because $\det A=1$. It follows that $A$ fixes every $C_q^1$-orbit class.

If $r_q=|\operatorname{im}N_q|$, the ordinary zeta of the symplectic coarse quotient is therefore $$\zeta_{\mathrm{id}}(z)=(1-z)^{-r_q}.
  \label{eq:symplectic-identity-zeta}$$ Restricting to symplectic symmetry restores multiplicity, not a clock. The full quotient obtains one class only by using the generally nonsymplectic part of the local $\mathrm{GL}_2$ centralizer. Figure [\[fig:quotient-layers\]](#fig:quotient-layers){reference-type="ref" reference="fig:quotient-layers"} summarizes the information retained by the three symmetry layers.

![image](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient/paper/figures/fig1_quotient_layers.pdf>){width="\\textwidth"}

# Prime-shell strata and reversal {#sec:strata}

For $v=(x,y)^t\in\mathbb{F}_p^2$, $$\Delta_p(x,y)=x^2-xy-y^2,
  \qquad \operatorname{disc}(\Delta_p)=5.
  \label{eq:prime-quadratic-form}$$ The complete nonzero shell is $E_p=\mathbb{F}_p^2\setminus\{0\}$. Its noncyclic part is the nonzero zero locus of $\Delta_p$. The split, inert, ramified, and reversing cases belong to the established prime- and rational-lattice orbit setting [@Gaspari1994; @BaakeNeumaerkerRoberts2013]; the proposition records the specialized strata used by this audit.

[\[prop:prime-strata\]]{#prop:prime-strata label="prop:prime-strata"} The full nonzero prime shell has the following structure.

1.  At $p=2$, and at every odd inert prime $\left(\frac5p\right)=-1$, one has $\mathrm{CV}_p=E_p$, and $C_p$ is transitive on the shell.

2.  If $p\ne5$ is split, then $$|\mathrm{CV}_p|=(p-1)^2,
              \qquad |E_p\setminus\mathrm{CV}_p|=2(p-1).
              \label{eq:split-counts}$$ The discarded set consists of two punctured eigenlines, and $E_p/C_p$ has three classes: the cyclic complement and the two eigenlines.

3.  At $p=5$, $$|\mathrm{CV}_5|=20,
              \qquad |E_5\setminus\mathrm{CV}_5|=4,
              \label{eq:ramified-counts}$$ and $E_5/C_5$ has two classes: the punctured Jordan eigenline and its cyclic complement.

At $p=2$, the form $x^2+xy+y^2$ is nonzero at all three nonzero vectors. At an odd inert prime, [\[eq:prime-quadratic-form\]](#eq:prime-quadratic-form){reference-type="eqref" reference="eq:prime-quadratic-form"} is anisotropic. In both cases every nonzero vector is cyclic, and the torsor theorem makes $C_p$ simply transitive on the shell.

At a split prime, the form factors into two distinct linear factors. Its nonzero zero set is the disjoint union of two punctured lines and has $2(p-1)$ points. The complement consequently has $(p-1)^2$ points. In an eigenbasis, $C_p$ consists of invertible diagonal matrices. It is transitive on the complement and separately on each punctured eigenline, giving three classes.

At $p=5$, the form is the square of one nonzero linear form. The punctured zero line has four points. In Jordan coordinates the centralizer has the form $\{aI+bN:a\ne0,\ N^2=0\}$, which is transitive separately on that line and on its complement. This gives the two ramified classes.

The fixed integer matrix $$J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
  \label{eq:reversor}$$ satisfies $$JAJ^{-1}=A^{-1},
  \qquad J^2=-I,
  \qquad \Delta_p(Jv)=-\Delta_p(v).
  \label{eq:reversor-identities}$$ Every reversor differs from $J$ by a commuter, so the group in [\[eq:reversing-group\]](#eq:reversing-group){reference-type="eqref" reference="eq:reversing-group"} is $C_p\cup JC_p$. In the split case, $J$ interchanges the two eigenlines. It cannot merge their union with the cyclic complement because [\[eq:reversor-identities\]](#eq:reversor-identities){reference-type="eqref" reference="eq:reversor-identities"} preserves zero versus unit values of $\Delta_p$. At the ramified prime, the unique eigenline is preserved. The full-shell reversing-orbit counts at the frozen primes $2,3,5,7,11$ are therefore $$1,\ 1,\ 2,\ 1,\ 2.
  \label{eq:reversing-counts}$$ This casewise statement concerns the explicitly defined reversing group. It does not assert a broader classification of every normalizer that may act on $\langle A\rangle$ through arbitrary power automorphisms.

The prime analysis exposes a second cost of the torsor quotient. In the split and ramified cases, the torsor is only the cyclic locus. Calling it the complete shell would silently discard two eigenlines or one Jordan eigenline, respectively.

# Composite formulas and the exact audit {#sec:composite-audit}

## All-modulus cardinalities

Membership in $\mathrm{CV}_q$ is equivalent to $\Delta_q(v)$ being a unit, so it can be tested modulo each prime divisor of $q$. Every admissible pair modulo $p$ has $p^{2(k-1)}$ lifts modulo $p^k$. Therefore $$|\mathrm{CV}_q|
  =\prod_{p^k\parallel q}p^{2(k-1)}c_p,
  \label{eq:CV-general-count}$$ where $$c_p=
  \begin{cases}
    p^2-1,&p=2\text{ or }\left(\frac5p\right)=-1,\\
    (p-1)^2,&p\ne5\text{ and }\left(\frac5p\right)=1,\\
    p(p-1),&p=5.
  \end{cases}
  \label{eq:local-CV-count}$$ The exact-order shell has the Jordan-totient cardinality $$|E_q|=J_2(q)=q^2\prod_{p\mid q}(1-p^{-2}),
  \label{eq:jordan-totient}$$ with the product explicitly over prime divisors. Equations [\[eq:CV-general-count\]](#eq:CV-general-count){reference-type="eqref" reference="eq:CV-general-count"} and [\[eq:jordan-totient\]](#eq:jordan-totient){reference-type="eqref" reference="eq:jordan-totient"} determine the discarded set by subtraction.

Since Theorem [\[thm:torsor\]](#thm:torsor){reference-type="ref" reference="thm:torsor"} holds for every $q$, the identity $$|\mathrm{CV}_q/C_q|=1
  \label{eq:all-q-one-class}$$ also holds for every composite modulus. This is a theorem, not an extrapolation from the four finite controls below. It proves too much for a prime-specific mechanism: primality is nowhere used in the one-class quotient.

## Registered nine-modulus ledger

The finite audit used the ordered, source-locked tuple $$(2,3,5,7,11,4,6,9,10).
  \label{eq:frozen-moduli}$$ The five primes were inherited controls. The composites were predeclared to test an inert lift, CRT products, and the ramified-five boundary. No modulus was scanned, added, removed, or replaced after source lock. Figure [\[fig:nine-modulus-ledger\]](#fig:nine-modulus-ledger){reference-type="ref" reference="fig:nine-modulus-ledger"} displays the exact counts before the same values are recorded in compact tables.

![image](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient/paper/figures/fig2_nine_modulus_ledger.pdf>){width="\\textwidth"}

::: {#tab:registered-core-ledger}
    $q$   $|E_q|$   $|\mathrm{CV}_q|$   discard   $|C_q|$   $|C_q^1|$   $\operatorname{ord}_q(A)$   $A$-orbits
  ----- --------- ------------------- --------- --------- ----------- --------------------------- ------------
      2         3                   3         0         3           3                           3            1
      3         8                   8         0         8           4                           4            2
      5        24                  20         4        20          10                          10            2
      7        48                  48         0        48           8                           8            6
     11       120                 100        20       100          10                           5           20
      4        12                  12         0        12           6                           3            4
      6        24                  24         0        24          12                          12            2
      9        72                  72         0        72          12                          12            6
     10        72                  60        12        60          30                          30            2

  : Exact shell, centralizer, and $A$-orbit counts in frozen order. The finite rows are implementation controls. The all-$q$ authority is the proof above.
:::

::: {#tab:registered-quotient-ledger}
    $q$   $|\mathrm{CV}_q/C_q|$   $|\mathrm{CV}_q/C_q^1|$   $|E_q/C_q|$   $|E_q/C_q^1|$   reversing $|E_q/\mathcal R_q|$
  ----- ----------------------- ------------------------- ------------- --------------- --------------------------------
      2                       1                         1             1               1                                1
      3                       1                         2             1               2                                1
      5                       1                         2             2               4                                2
      7                       1                         6             1               6                                1
     11                       1                        10             3              12                                2
      4                       1                         2             1               2                               --
      6                       1                         2             1               2                               --
      9                       1                         6             1               6                               --
     10                       1                         2             2               4                               --

  : Exact cyclic and full-shell quotient counts. A dash means that the prime-only reversing control was not part of the registered composite contract.
:::

The audit compared two independently structured exact engines. One enumerated the matrix commutant, centralizers, shells, determinant fibers, orbits, quotient transitions, and prime reversing relation. The other used $aI+bA$, the algebra norm, and the torsor map. Every row passed object-level equality, not only agreement of summary counts. In particular, the audit checked that the $C_q^1$-orbits equal the $\Delta_q$-fibers, that both quotient transitions are identity maps, and that reversing symmetry never mixes cyclic and noncyclic strata.

The independent first deployment review rejected an earlier semantic validator because a hollow fabricated row could satisfy its shallow checks. Deployment remained locked. The repaired validator imposed exact recursive schemas, residue types, uniqueness and partition checks, and canonical comparison with a fresh fixed-$q$ recomputation. The same fabricated row became a negative test, after which a second independent review issued a hash-bound deployment pass. Exactly one registered audit was then executed. An independent result reviewer reconstructed every stored object without importing the candidate and issued `RESULT_PASS`.

Four findings matter for the route decision. First, every full cyclic quotient has one class and identity dynamics. Second, the symplectic quotient counts are $$1,2,2,6,10,2,2,6,2,
  \label{eq:observed-norm-classes}$$ which exactly equal the norm-image sizes. Third, the cyclic locus is not the complete shell at $q=5,11,10$. Fourth, all four composite controls have the same one-class full cyclic quotient. The finite data are exact falsification controls for the implementation. They do not prove any of the all-modulus statements.

# Route decision, construction cost, and limitations {#sec:decision}

The positive algebraic mechanism is exact. The cyclic-vector locus is a full-centralizer torsor, and the full quotient has one class. Two independent failures prevent that fact from becoming an intrinsic Riemann-style local factor.

First, the coarse quotient removes the dynamical clock. Its native factor is $(1-z)^{-1}$ because the quotient contains one fixed point. The symbol $q$ does not occur in the induced dynamics. Writing $(1-q^{-s})^{-1}$ therefore attaches the modulus after quotienting. The same problem remains for the symplectic quotient: it consists of several fixed classes and has formal zeta $(1-z)^{-|\operatorname{im}N_q|}$. Figure [\[fig:clock-semantics\]](#fig:clock-semantics){reference-type="ref" reference="fig:clock-semantics"} separates this native identity factor from the externally attached modulus label.

![image](<../../../../../symplectic_map/papers/10-cat-centralizer-quotient/paper/figures/fig3_clock_semantics.pdf>){width="\\textwidth"}

Second, the construction is not prime-specific. The torsor proof and one-class quotient hold for every modulus. The predeclared composites do not merely imitate the prime controls numerically. They instantiate the same all-$q$ theorem. Restricting the product to prime labels would consequently be another external choice.

The full centralizer also carries a geometric cost. The group $C_q$ is defined using every commuter over $R_q$, including determinant values outside one. Reduction of the global integral centralizer gives a homomorphism into $C_q$, but the quotient used here does not require a local element to arise from one fixed global torus symmetry group. It uses all $q$-dependent local pseudo-symmetries. We make no converse claim that every local commuter fails to lift. No global-lift classification is needed for the audit.

The result does not rule out finer objects. A non-effective quotient, Burnside-ring invariant, equivariant Lefschetz theory, orbifold or groupoid zeta, stacky quotient, or twisted-sector construction may retain stabilizer and source-orbit information erased by the coarse set quotient. Such objects require their own definitions and source locks. The present note neither constructs nor rejects them. Equivariant, group-action, and twisted quotient approaches provide concrete adjacent precedents [@GuseinZadeLuengoMelle2015; @Miles2017; @Walton2018]. Likewise, norm-one Hecke centralizers may act nontrivially after quantization even though their coarse class space is fixed. No conclusion about Hecke spectra, quantum eigenstates, equidistribution, transfer operators, Fredholm determinants, or zeros follows from Theorem [\[thm:symplectic-quotient\]](#thm:symplectic-quotient){reference-type="ref" reference="thm:symplectic-quotient"}.

Within the frozen scope, the exact terminal decision is

`CENTRALIZER_CYCLIC_TORSOR_CERTIFIED`\
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC`\
`ROUTE_B_NOT_OPENED`.

The first line certifies the torsor and the associated exact finite audit. The second records that the local factor still needs an external modulus clock and an external prime restriction. The third prevents the negative coarse-quotient result from being promoted to a spectral or quantization claim.

# Conclusion {#sec:conclusion}

For the standard cat matrix, a single universal cyclic basis controls the finite centralizer over every $\mathbb{Z}/q\mathbb{Z}$. This yields a clean torsor: the unit group of $R_q[A]$ acts freely and transitively on the cyclic-vector locus. The same identification exposes why the apparent one-factor repair does not solve the dynamical problem. Quotienting by the full centralizer also quotients by $A$, leaving one fixed class with period one. The symplectic subgroup preserves the determinant norm and leaves exactly the norm-image classes, all fixed. Prime-shell and reversing strata show that the torsor is not always the complete shell, while CRT shows that the one-class construction is not restricted to primes.

The resulting conclusion is narrow but complete: the coarse local centralizer quotient compresses multiplicity only after erasing the clock, and $z=q^{-s}$ reintroduces that clock as a label. The note closes this coarse Route-A variant. Whether an explicitly defined equivariant or groupoid refinement can retain the necessary source information without becoming another global normalization is a separate question, not an unstated extension of the present theorem.

# Proof and evidence firewall {#app:firewall}

The claims in the main text have three distinct evidence roles.

C0.08 p0.39 p0.42

\
claim & authority & boundary\
claim & authority & boundary\
C1 & Theorem [\[thm:torsor\]](#thm:torsor){reference-type="ref" reference="thm:torsor"}, item 1 & all $q$. Standard cyclic-module algebra for the frozen matrix, not a new centralizer classification\
C2 & Theorem [\[thm:torsor\]](#thm:torsor){reference-type="ref" reference="thm:torsor"}, items 2--3 & torsor and exact-order inclusion. The cyclic locus need not equal the full shell\
C3 & Theorem [\[thm:torsor\]](#thm:torsor){reference-type="ref" reference="thm:torsor"}, item 4 & cyclic $A$-orbits are $C_q/\langle A\rangle$ with uniform source period\
C4 & equations [\[eq:one-point-quotient\]](#eq:one-point-quotient){reference-type="eqref" reference="eq:one-point-quotient"}--[\[eq:one-point-zeta\]](#eq:one-point-zeta){reference-type="eqref" reference="eq:one-point-zeta"} & one coarse class and identity induced dynamics; no new zeta definition\
C5 & equation [\[eq:external-specialization\]](#eq:external-specialization){reference-type="eqref" reference="eq:external-specialization"} & $q^{-s}$ and $\log q$ are external labels, not quotient return-time laws\
C6 & Theorem [\[thm:symplectic-quotient\]](#thm:symplectic-quotient){reference-type="ref" reference="thm:symplectic-quotient"}, first statement & symplectic orbits are norm fibers; no Hecke or representation result\
C7 & equation [\[eq:norm-image-cardinality\]](#eq:norm-image-cardinality){reference-type="eqref" reference="eq:norm-image-cardinality"} & all-$q$ norm-image formula, including binary and ramified-five boundaries\
C8 & Proposition [\[prop:prime-strata\]](#prop:prime-strata){reference-type="ref" reference="prop:prime-strata"} and equation [\[eq:reversing-counts\]](#eq:reversing-counts){reference-type="eqref" reference="eq:reversing-counts"} & prime full-shell strata and fixed reversor only; no broad normalizer theorem\
C9 & equations [\[eq:CV-general-count\]](#eq:CV-general-count){reference-type="eqref" reference="eq:CV-general-count"}--[\[eq:all-q-one-class\]](#eq:all-q-one-class){reference-type="eqref" reference="eq:all-q-one-class"} & CRT theorem for all moduli. Composite rows are controls only\
C10 & Tables [1](#tab:registered-core-ledger){reference-type="ref" reference="tab:registered-core-ledger"} and [2](#tab:registered-quotient-ledger){reference-type="ref" reference="tab:registered-quotient-ledger"} & one development-seen exact audit, not proof, statistical inference, or novelty evidence\
X1 & Section [7](#sec:decision){reference-type="ref" reference="sec:decision"} & Burnside-ring, equivariant, orbifold, stacky, groupoid, and twisted-sector refinements remain untested\
X2 & Section [7](#sec:decision){reference-type="ref" reference="sec:decision"} & Hecke, transfer, Fredholm, and quantum constructions remain untested; Route B is unopened\

The all-$q$ centralizer, torsor, norm image, and CRT formulas are theorem-derived. The exact audit can falsify a faulty implementation or a misstated control row, but no finite collection of moduli proves those formulas. Conversely, the proof does not certify that software stored the correct orbit partitions, determinant fibers, quotient transitions, or reversing groups. Independent object-level reconstruction provides that separate implementation check.

The audit used exact residue arithmetic only. It accessed no external prime table, generated modulus target, Riemann-zero data, random draw, fitted parameter, numerical $s$, numerical $\log q$, or numerical $q^{-s}$. No matrix search, equivariant construction, Hecke operator, transfer operator, Fredholm determinant, or quantum system was run.

# Frozen provenance {#app:provenance}

Manuscript production was bound to the following independently reviewed upstream artifacts:

Source lock

:   `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2`.

Proof package

:   `2eafe71f32c452ff8a20a6818ccb43082e02b866db7353e26c36ff432f1b2a4c`.

Independent source review

:   `a551784d205d9ef52ce6a493ab66cb7295a4a9dadbeb8bb2353fc58e3011dff5`.

Reviewed execution tree

:   `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436`.

Independent two-round code review

:   `990b1762e2aea6c379288854cca918cc4bbe87b7ea7ccadef7458ecfcf6988f0`.

Registered exact result

:   `8dceb1b8a63db462c1fd55a242ea35de974f73b6c80da68517b91c9eebb214ff`.

Independent result review

:   `29264a8fd97d3acf4435ed807294bffcda0844a48728d8572083d92a3bcf5b58`.

Strict result manifest

:   `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`.

Official result report

:   `1ece7db3fbee75bcecaecb0ad05f89fe88699c4231bea80581f382f33ed3aa6e`.

Official validation report

:   `f94dbfb28a71aea4dac5e89a8bc2a622bba092b66098c2fc2217ceba19a8ad5a`.

The manuscript also binds the independently released planning, citation, and figure package:

Paper plan

:   `972c13d2551e51bb2781bf7f177314812460c161af0ce1daa748eeff413cbe8a`.

Citation verification

:   `b4596ed56aee5eb47314221bba681098e45011a3fdc9dafc201315e597a1bfc6`.

Frozen bibliography

:   `1ccce7ade3079ca995f00058f4811bdd02a9062d8038b27be2f967f480fe8699`.

Exact LaTeX figure includes

:   `dfd829b896edcfd02b8d7b02fd9d30bfe8ec49ce42adaba79e1d627cd930708b`.

Figure manifest

:   `1a2c7de68772ddeb5c614d0ade89a48710e93a3e5a5ff4a393db5c6f3cd4c2ab`.

Framed asset tree

:   `33b8e1d767221529ff2b97fddca0145b1f9724cae924c37afa2847ecfc2bc9d6`.

Round-1 bounded-repair history

:   `97f971328996efae866356bdc2c4715a68fcb470dcbe64029d7758d1ec73256a`.

Round-2 independent asset pass

:   `9277132df8400c550f108c9a71d466a1c3752bbf3c1be2ae39d565e932bc3e87`.

Figure 1 publication PDF

:   `ac8b29c810881e6383fb3f8b7cb55c602e052ef1677def5643d540b8ee12feb3`.

Figure 2 publication PDF

:   `f86ff8e50c5a138996c8f379fa0309ddc6071cffca1d540b81e07304dae2dd73`.

Figure 3 publication PDF

:   `0df9de8544c05e60749d456244c2920ac15c03a8bc5f5011a66f8d2c5e8cee33`.

The registered audit occurred once before manuscript production. No candidate, test suite, source computation, or scientific experiment was rerun for writing. Compilation, bibliography processing, and visual QA are mechanical manuscript-production steps and do not alter the frozen source, code, or result authority.

# Availability and declarations {#availability-and-declarations .unnumbered}

#### Data and code availability.

The accompanying local research package contains the source lock, proof package, reviewed exact-arithmetic implementation, single registered result, independent reviews, and strict result manifest. No external dataset is used by the mathematical claims or the finite audit.

#### Ethics declaration.

The work involves no human participants, animals, personal data, or intervention study.

#### Author contributions.

Authorship and CRediT-role metadata are withheld in this anonymous pre-review copy and will be supplied by the authors for any non-anonymous release.

#### Conflict of interest.

Conflict-of-interest metadata are withheld with the anonymous author record and must be completed before an external submission.

#### Funding acknowledgment.

Funding metadata are withheld during anonymous pre-review and must be completed before an external submission.

#### AI-assisted workflow disclosure.

AI-assisted research and writing tools were used to organize source-locked materials, draft text, and support mechanical checks. Mathematical claims, citations, finite outputs, and lifecycle statements were separately bound to recorded source, code, result, and manuscript review gates. Responsibility for the released content remains with the authors.
