---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--87-chain-ring-socle-product-shifts"
canonical_tex: "symbolic_dynamics/papers/87-chain-ring-socle-product-shifts/main.tex"
canonical_pdf: "symbolic_dynamics/papers/87-chain-ring-socle-product-shifts/main.pdf"
source_sha256: "b9d319802f4e0a126c4da8e027a64a20e31ecae0d9e3de11a48de86e67c486fe"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Socle-Product Shifts over Finite Chain Rings: Equal-Entropy Splitting, Parity, and Four-Period Rigidity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/87-chain-ring-socle-product-shifts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/87-chain-ring-socle-product-shifts/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/87-chain-ring-socle-product-shifts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/87-chain-ring-socle-product-shifts/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/87-chain-ring-socle-product-shifts/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $R$ be a finite commutative chain ring with maximal ideal $\mathfrak m=(\pi)$, residue-field size $q$, and $\mathfrak m^{a+1}=0\ne\mathfrak m^a$. We study the nearest-neighbor shift whose allowed pairs satisfy $xy\in\operatorname{Soc}(R)\setminus\{0\}$. Valuation turns this condition into the exact boundary equation $\operatorname{v}(x)+\operatorname{v}(y)=a$. The adjacency graph therefore splits into complete bipartite components and, when $a$ is even, one full-shift component. If $$\rho=(q-1)q^{a/2},$$ then every component has Perron value $\rho$, the adjacency rank is $a+1$, and the topological entropy is $\log\rho$. There are $\lfloor a/2\rfloor+1$ ergodic maximal-entropy measures. For odd $a$ all of them have period two; for even $a$ exactly one is mixing. We compute every fixed-point count and the full dynamical zeta function. The first four fixed-point counts recover $(q,a)$, whereas the shift forgets all finer ring structure: any two chain rings with the same $(q,a)$ give one-block conjugate shifts. The relation is a union of nonzero-socle product fibres, rather than the classical zero-product graph or a single fixed-product matrix; those ownership distinctions are kept explicit.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: |
  Socle-Product Shifts over Finite Chain Rings:\
  Equal-Entropy Splitting, Parity, and Four-Period Rigidity
```

## Markdown 正文

# Introduction

Finite commutative chain rings have a single ideal filtration, but rings with the same residue-field size and filtration length need not be isomorphic. Their structure and classification are classical [@ClarkLiang1973; @Hou2001]. This makes them a useful test for a symbolic question: which parts of a ring survive after multiplication is reduced to a nearest-neighbor constraint?

Fix a chain ring $R$ and allow $x$ to be followed by $y$ precisely when their product is a nonzero element of the socle. The answer is unusually rigid at the dynamical level and unusually coarse at the ring level. The ring valuation decomposes the shift into finitely many irreducible components of exactly equal entropy. The parity of the filtration length decides whether one of these components is mixing. At the same time, the entire adjacency matrix has only $a+1$ nonzero eigenvalues, regardless of the size $q^{a+1}-1$ of its alphabet.

There is an important ownership boundary. Anderson and Livingston's zero-divisor graph joins distinct nonzero zero divisors when their product is zero [@AndersonLivingston1999]. Spectra and ranks of that graph over finite chain rings and principal ideal rings have already been studied by Rattanakangwanwong and Meemark [@RattanakangwanwongMeemark2022]. Our graph instead includes units, retains loops, and selects the single valuation boundary on which the product is in $\operatorname{Soc}(R)\setminus\{0\}$. More directly, Dolžan defines the fixed-product matrix $A_u(R)=(\mathbf 1_{\{xy=u\}})_{x,y\in R}$ and determines characteristic polynomials in broad finite-local-ring regimes [@Dolzan2026]. After deleting its zero row and column, our adjacency matrix is exactly $$A_R=\sum_{u\in\operatorname{Soc}(R)\setminus\{0\}}A_u(R).$$ Thus fixed-product matrices and their spectral study are prior art. We claim only the residual union-of-socle-values relation and its symbolic consequences; we do not claim the zero-divisor graph, either prior spectral framework, the finite-type zeta determinant [@BowenLanford1970], or the Parry construction [@Parry1964].

The residual calculation has four parts. First, valuation gives an exact complete-bipartite normal form and the adjacency rank. Second, the normal form gives the complete maximal-measure simplex and an odd/even mixing transition. Third, it gives all periodic counts and the rational zeta function. Finally, four fixed-point counts recover the two surviving parameters, while an explicit layerwise conjugacy proves that no finer ring invariant survives.

# The valuation boundary {#sec:valuation}

Let $R$ be a finite commutative chain ring. Its unique maximal ideal is principal, say $\mathfrak m=(\pi)$, and for some $a\geq1$ its ideal chain is $$R=\mathfrak m^0\supsetneq\mathfrak m^1\supsetneq\cdots
 \supsetneq\mathfrak m^a\supsetneq\mathfrak m^{a+1}=0.$$ We call $a+1$ the length and write $|R/\mathfrak m|=q$. For $x\ne0$ define $$\operatorname{v}(x)=i\quad\Longleftrightarrow\quad
 x\in\mathfrak m^i\setminus\mathfrak m^{i+1},
 \qquad 0\leq i\leq a,$$ and put $V_i=\{x\in R:\operatorname{v}(x)=i\}$. We use $R^\bullet=R\setminus\{0\}$. Here $\operatorname{Soc}(R)=\operatorname{Ann}_R(\mathfrak m)$ is the socle of the regular $R$-module.

[\[lem:valuation\]]{#lem:valuation label="lem:valuation"} For $0\leq i\leq a$, $$\label{eq:weights}
 |\mathfrak m^i|=q^{a+1-i},
 \qquad
 w_i:=|V_i|=(q-1)q^{a-i}.$$ Moreover, $$\operatorname{Soc}(R)=\mathfrak m^a,
 \qquad
 xy\in\operatorname{Soc}(R)\setminus\{0\}
 \quad\Longleftrightarrow\quad
 \operatorname{v}(x)+\operatorname{v}(y)=a.$$

Multiplication by $\pi^i$ identifies $R/\mathfrak m$ with $\mathfrak m^i/\mathfrak m^{i+1}$ as additive groups. Every successive quotient therefore has $q$ elements. Counting upward from $\mathfrak m^{a+1}=0$ gives [\[eq:weights\]](#eq:weights){reference-type="eqref" reference="eq:weights"}.

Every nonzero $x\in V_i$ has the form $x=\pi^i u$ for a unit $u$. Hence, if $i+j\leq a$, the product of elements in $V_i$ and $V_j$ lies in $V_{i+j}$; if $i+j\geq a+1$, it is zero. Also $\mathfrak m\mathfrak m^a=0$, whereas an element in $V_i$ with $i<a$ is not annihilated by $\pi$. Thus $\operatorname{Soc}(R)=\mathfrak m^a$, and the final equivalence follows.

Define the socle-product shift $$\label{eq:shift}
 X_R=\left\{x\in(R^\bullet)^\mathbb Z:
 x_nx_{n+1}\in\operatorname{Soc}(R)\setminus\{0\}
 \text{ for every }n\in\mathbb Z\right\},$$ with the left shift $\sigma$. Let $A_R$ be its zero-one adjacency matrix, indexed by $R^\bullet$. The same shift results if the alphabet is declared to be all of $R$, because zero has no allowed predecessor or successor.

# Normal form, rank, and entropy {#sec:normal}

Write $J_{r,s}$ for the $r\times s$ all-ones matrix and set $$\label{eq:rho}
 N=q^{a+1}-1,
 \qquad
 \rho=(q-1)q^{a/2}.$$ Although $\rho$ can be irrational when $a$ is odd, its square $\rho^2=(q-1)^2q^a$ is always an integer.

[\[thm:normal\]]{#thm:normal label="thm:normal"} After the alphabet is ordered by valuation, $A_R$ is the direct sum, over $0\leq i<a-i\leq a$, of the blocks $$\label{eq:bipartite-block}
 B_i=
 \begin{pmatrix}
 0&J_{w_i,w_{a-i}}\\
 J_{w_{a-i},w_i}&0
 \end{pmatrix},$$ and, when $a=2b$ is even, the additional block $J_{w_b,w_b}$. Consequently $$\operatorname{rank}_{\mathbb R}A_R=a+1,
 \qquad
 h_{\mathrm{top}}(X_R)=\log\rho.$$ More precisely, if $a=2b$, then $$\label{eq:char-even}
 \det(tI-A_R)=
 t^{N-a-1}(t-\rho)^{b+1}(t+\rho)^b,$$ whereas, if $a=2b+1$, then $$\label{eq:char-odd}
 \det(tI-A_R)=
 t^{N-a-1}(t^2-\rho^2)^{b+1}.$$

By [\[lem:valuation\]](#lem:valuation){reference-type="ref" reference="lem:valuation"}, every vertex of $V_i$ is joined to every vertex of $V_{a-i}$ and to no other vertex. This gives the displayed direct sum. For $i<a-i$, the block $B_i$ has rank two and its only nonzero eigenvalues are $$\pm\sqrt{w_iw_{a-i}}=\pm(q-1)q^{a/2}=\pm\rho.$$ If $a=2b$, the central all-ones block has rank one and sole nonzero eigenvalue $w_b=(q-1)q^b=\rho$. Summing the ranks and multiplicities gives [\[eq:char-even\]](#eq:char-even){reference-type="eqref" reference="eq:char-even"}--[\[eq:char-odd\]](#eq:char-odd){reference-type="eqref" reference="eq:char-odd"}. Every irreducible block has spectral radius $\rho$, so the entropy of their finite disjoint union is $\log\rho$.

The compression can also be recorded without the full matrix. On functions constant on valuation layers, $A_R$ acts through the $(a+1)\times(a+1)$ matrix $$\label{eq:quotient}
 Q_{ij}=w_j\,\mathbf 1_{\{i+j=a\}}.$$ All other directions are killed. The matrix $Q$ is anti-diagonal with no zero entry, so it is nonsingular; this gives a second proof of the exact rank $a+1$.

# Equal-entropy components and maximal measures {#sec:mme}

For $i<a-i$, let $C_i$ be the shift supported on $V_i\cup V_{a-i}$. It is an irreducible complete-bipartite shift of exact period two. When $a=2b$, let $C_b$ be the full shift on $V_b$; it is mixing. These are precisely the irreducible components of $X_R$.

[\[thm:mme\]]{#thm:mme label="thm:mme"} The shift $X_R$ has $$\label{eq:mme-count}
 c(a)=\left\lfloor\frac a2\right\rfloor+1$$ ergodic measures of maximal entropy, one on each irreducible component. Their convex hull is the full simplex of maximal-entropy measures.

If $a$ is odd, every ergodic maximal-entropy measure has period two and none is mixing. If $a$ is even, exactly one ergodic maximal-entropy measure is mixing: the uniform Bernoulli measure on the central full shift $C_{a/2}$. The other ergodic maximal-entropy measures still have period two.

Each complete-bipartite component has Perron value $\sqrt{w_iw_{a-i}}=\rho$, and the central full shift, when present, has Perron value $w_{a/2}=\rho$. Thus every component has entropy $\log\rho$. An irreducible finite-type shift has a unique Parry measure [@Parry1964]; hence every component supplies one ergodic maximal-entropy measure. There are $c(a)$ components. Since they are pairwise disjoint invariant clopen sets, every invariant measure decomposes over them, and entropy is the corresponding affine average. This proves the simplex statement. The period and mixing assertions follow from the complete-bipartite blocks and the looped all-ones central block.

The component measures are explicit. On $C_i$ with $i<a-i$, each layer has stationary mass $1/2$; conditional on the current layer, the next symbol is uniform on the opposite layer. On $C_{a/2}$ the coordinates are independent and uniform on $V_{a/2}$. Thus the odd/even statement concerns the existence of a mixing maximal component. The full shift $X_R$ itself is reducible, and hence not topologically transitive, for every $a\geq2$. At the boundary case $a=1$ there is just one complete-bipartite component, so $X_R$ is irreducible of exact period two (and is still not mixing).

# All periods and the zeta function {#sec:periods}

Put $$F_n(R)=\#\operatorname{Fix}_{X_R}(\sigma^n)=\operatorname{tr}(A_R^n),
 \qquad n\geq1.$$

[\[thm:periods\]]{#thm:periods label="thm:periods"} If $a=2b$ is even, then $$\label{eq:fixed-even}
 F_n(R)=\rho^n\bigl((b+1)+b(-1)^n\bigr)
 =
 \begin{cases}
  \rho^n,&n\text{ odd},\\
  (a+1)\rho^n,&n\text{ even}.
 \end{cases}$$ If $a=2b+1$ is odd, then $$\label{eq:fixed-odd}
 F_n(R)=(b+1)\bigl(1+(-1)^n\bigr)\rho^n
 =
 \begin{cases}
  0,&n\text{ odd},\\
  (a+1)\rho^n,&n\text{ even}.
 \end{cases}$$ The Artin--Mazur zeta function is $$\label{eq:zeta}
 \zeta_{X_R}(z)
 =\exp\left(\sum_{n\geq1}\frac{F_n(R)}n z^n\right)
 =
 \begin{cases}
  \displaystyle\frac{1}{(1-\rho z)(1-\rho^2z^2)^b},&a=2b,\\[8pt]
  \displaystyle\frac{1}{(1-\rho^2z^2)^{b+1}},&a=2b+1.
 \end{cases}$$

Sum the $n$th powers of the nonzero eigenvalues in [\[eq:char-even\]](#eq:char-even){reference-type="eqref" reference="eq:char-even"} and [\[eq:char-odd\]](#eq:char-odd){reference-type="eqref" reference="eq:char-odd"}. This gives [\[eq:fixed-even\]](#eq:fixed-even){reference-type="eqref" reference="eq:fixed-even"} and [\[eq:fixed-odd\]](#eq:fixed-odd){reference-type="eqref" reference="eq:fixed-odd"}. The Bowen--Lanford determinant identity $\zeta_{X_R}(z)=\det(I-zA_R)^{-1}$ [@BowenLanford1970], followed by the same factorization, gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

For completeness, the number $E_n(R)$ of points of least period $n$ and the number $O_n(R)$ of length-$n$ orbits are therefore $$\label{eq:least-period}
 E_n(R)=\sum_{d\mid n}\mu(n/d)F_d(R),
 \qquad
 O_n(R)=\frac1n\sum_{d\mid n}\mu(n/d)F_d(R),$$ where $\mu$ is the Möbius function. Thus [\[thm:periods\]](#thm:periods){reference-type="ref" reference="thm:periods"} determines the complete orbit census, not only the fixed-point sequence.

# Ring collapse and four-period rigidity {#sec:rigidity}

The normal form proves that the shift remembers less than its ring, while the first four periods prove that it remembers exactly two parameters.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} Let $R$ and $S$ be finite commutative chain rings, with parameter pairs $(q_R,a_R)$ and $(q_S,a_S)$. Then $$X_R\text{ and }X_S\text{ are topologically conjugate}
 \quad\Longleftrightarrow\quad
 (q_R,a_R)=(q_S,a_S).$$ When the parameters agree, the conjugacy can be chosen as a one-block code induced by arbitrary bijections between corresponding valuation layers.

More explicitly, $(q,a)$ is recovered from $F_1,F_2,F_3,F_4$ as follows. If $F_1>0$, then $a$ is even and $$\label{eq:recover-even}
 a=\frac{F_2}{F_1^2}-1,
 \qquad
 (q-1)^2q^a=F_1^2.$$ If $F_1=0$, then $a$ is odd and $$\label{eq:recover-odd}
 a=\frac{F_2^2}{F_4}-1,
 \qquad
 (q-1)^2q^a=\frac{F_4}{F_2}.$$ In the odd case $F_3=0$; in the even case $F_3=F_1^3$, providing internal consistency checks.

Suppose first that $(q_R,a_R)=(q_S,a_S)=(q,a)$. By [\[eq:weights\]](#eq:weights){reference-type="eqref" reference="eq:weights"}, $|V_i(R)|=|V_i(S)|$ for every $i$. Choose bijections $\phi_i:V_i(R)\to V_i(S)$ and let $\phi$ be their union. The valuation boundary in [\[lem:valuation\]](#lem:valuation){reference-type="ref" reference="lem:valuation"} shows $$xy\in\operatorname{Soc}(R)\setminus\{0\}
 \quad\Longleftrightarrow\quad
 \phi(x)\phi(y)\in\operatorname{Soc}(S)\setminus\{0\}.$$ Thus $\phi$ is an adjacency-graph isomorphism and its coordinatewise extension is a one-block conjugacy.

Conversely, conjugacy preserves all fixed-point counts. If $F_1>0$, the even formula [\[eq:fixed-even\]](#eq:fixed-even){reference-type="eqref" reference="eq:fixed-even"} gives [\[eq:recover-even\]](#eq:recover-even){reference-type="eqref" reference="eq:recover-even"}. If $F_1=0$, [\[eq:fixed-odd\]](#eq:fixed-odd){reference-type="eqref" reference="eq:fixed-odd"} gives $F_2=(a+1)\rho^2$ and $F_4=(a+1)\rho^4$, hence [\[eq:recover-odd\]](#eq:recover-odd){reference-type="eqref" reference="eq:recover-odd"}. For a fixed recovered $a$, the function $(t-1)^2t^a$ is strictly increasing on integers $t\geq2$, so the displayed value recovers $q$ uniquely. Therefore conjugate members have the same parameter pair.

This collapse is genuine. For every prime $p$ and $a\geq1$, the rings $$\mathbb Z/p^{a+1}\mathbb Z
 \qquad\text{and}\qquad
 \mathbb F_p[t]/(t^{a+1})$$ have the same $(q,a)=(p,a)$ and therefore conjugate socle-product shifts, but the rings are not isomorphic: their characteristics are $p^{a+1}$ and $p$, respectively.

# Exact controls and ownership boundary

The accompanying standard-library program checks the valuation layers, component count, rank quotient, zeta determinant, fixed counts through period ten, and four-period recovery for $q\in\{2,3,4,5\}$ and $1\leq a\leq5$. It separately realizes the valuation law in both $\mathbb Z/p^{a+1}\mathbb Z$ and $\mathbb F_p[t]/(t^{a+1})$ for $p=2,3,5$, verifies an explicit layerwise collapse, and checks $\mathbb F_4[t]/(t^{a+1})$ for the nonprime residue field. These finite controls guard indexing and implementation; the proofs above establish the full parameter range.

The zero-divisor firewall remains substantive. In a chain ring the classical zero-product condition is a valuation inequality at or beyond the nilpotence threshold, while [\[eq:shift\]](#eq:shift){reference-type="eqref" reference="eq:shift"} selects the preceding equality boundary and allows units and loops. The cited zero-divisor graph literature therefore owns the surrounding graph framework and the closest zero-product spectral calculations. Dolžan's fixed-product matrices are a still closer owner: the displayed sum identity exhibits our matrix as their sum over the nonzero socle. That work does not, by itself, give the complete-bipartite union, equal-entropy component simplex, periodic ledger, four-period recovery, or layerwise conjugacy proved here. A bounded search through 28 August 2026 found no exact collision for that owner-subtracted symbolic package. This dated statement is not an absolute priority claim; public posting, submission, and specialist priority clearance remain on hold.
