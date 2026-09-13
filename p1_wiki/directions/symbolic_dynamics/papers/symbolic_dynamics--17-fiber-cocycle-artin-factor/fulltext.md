---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--17-fiber-cocycle-artin-factor"
canonical_tex: "symbolic_dynamics/papers/17-fiber-cocycle-artin-factor/main.tex"
canonical_pdf: "symbolic_dynamics/papers/17-fiber-cocycle-artin-factor/main.pdf"
source_sha256: "51cc2c2c3f0600b2984a352a3549e6dd954d1b72a4faabdb414afa52de680587"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Genuine Fiber Symmetry after Relabeling Failure: Artin Character Factors of the Tensor-Atom Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/17-fiber-cocycle-artin-factor>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/17-fiber-cocycle-artin-factor/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/17-fiber-cocycle-artin-factor/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/17-fiber-cocycle-artin-factor/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/17-fiber-cocycle-artin-factor/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Relabeling tensor atoms is not a symmetry once distinct arithmetic roofs are frozen. We replace relabeling by a genuine $C_2$ fiber over the signed complete subset shift, using the intrinsic cocycle $\alpha(S)=|S|\bmod2$. Deck translations then commute with the weighted shift without moving any atom or roof. At the fixed normalization $z=1$, the trivial and sign isotypic determinants of the same regular transfer are $$D_+=\prod_p(1-x_p),\qquad D_-=\prod_p(1+x_p),$$ while the whole-extension determinant is $D_{\mathrm{reg}}=D_+D_-=\prod_p(1-x_p^2)$. Arithmetic specialization on $\operatorname{Re}s>1$ gives $\zeta(s)^{-1}$, $\zeta(s)/\zeta(2s)$, and $\zeta(2s)^{-1}$, respectively. We prove a matching rigidity theorem: an inclusion-compatible, relabeling-natural one-letter cocycle satisfying an operator-coherent atom-local identity must have $\alpha(S)=a^{|S|}$; its image is cyclic, and a transitive full extension forces the fiber group to be cyclic. The result is lawful but not an arithmetic selector. A primitive base necklace of degree $c$ closes after $m/\gcd(m,c)$ traversals in a $C_m$ cover, so singleton clocks are multiplied and mixed lifted primitives remain. Exact certificates comprise 300 repetition coefficients, 350 cyclic-character rows, 72,079 natural cocycle tables, 64 matched inventory controls, and 14 unit tests. Every control reproduces the identities, giving zero identity pass-rate margin. Thus the construction is a same-object Artin factor and a scoped one-letter obstruction, not a Riemann-hypothesis mechanism.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Genuine Fiber Symmetry after Relabeling Failure:\
  Artin Character Factors of the Tensor-Atom Shift
```

## Markdown 正文

# Introduction {#sec:introduction}

A permutation of symbolic labels and a symmetry of a frozen dynamical system are different objects. Before arithmetic weights are assigned, tensor atoms may be relabeled freely. After the variables are specialized to distinct values $x_p=p^{-s}$, a nontrivial atom permutation changes the weighted transfer rather than commuting with it. Character resolution based on that permutation therefore cannot be interpreted as a decomposition of one fixed arithmetic operator.

Finite-group extensions supply a lawful alternative. Their deck action lives on a separate fiber, commutes with the base dynamics, and resolves a regular transfer into representation blocks. This framework is classical in hyperbolic and symbolic dynamics [@ParryPollicott1986; @AdachiSunada1987; @ParryPollicott1990]; the question here is whether the signed tensor-subset grammar carries an intrinsic cocycle whose blocks retain its exact Euler ledger.

The minimal answer is positive. A symbol is a nonempty subset $S$ of a finite atom set, its scalar weight is $(-1)^{|S|+1}x_S$, and its $C_2$ fiber increment is $$\alpha(S)=|S|\pmod2.
\tag{1.1}\label{1.1}$$ This label is subset degree, not a prime-indexed table. Singleton symbols switch the fiber, so the extension has nontrivial periodic data. Deck translations never move the variables or roofs. The regular transfer has a trivial block and a sign block with determinants $$D_+(x)=\prod_p(1-x_p),\qquad
D_-(x)=\prod_p(1+x_p).
\tag{1.2}\label{1.2}$$ Their product $$D_{\mathrm{reg}}(x)=\prod_p(1-x_p^2)
\tag{1.3}\label{1.3}$$ is the determinant of the whole two-dimensional fiber. Equations [\[1.2\]](#1.2){reference-type="eqref" reference="1.2"} and [\[1.3\]](#1.3){reference-type="eqref" reference="1.3"} come from one transfer and one normalization. This same-object statement is the positive result.

It also exposes the obstruction. The clean product follows from degree count alone. If a relabeling-natural one-letter cocycle is required to satisfy the same atom-local matrix identity, coefficient comparison forces its cardinality-$k$ label to be the $k$th power of the singleton label. The image is cyclic. Enlarging the finite group cannot create a clean nonabelian escape without leaving the theorem's one-letter hypotheses.

Even the lawful $C_2$ extension does not align its primitive cycles with primes. A singleton base loop closes in the full extension after two traversals, whereas the mixed symbol $\{p,q\}$ closes after one. More generally, a primitive base orbit of total subset degree $c$ has $\gcd(m,c)$ primitive lifts, each traversing the base orbit $m/\gcd(m,c)$ times. Atom-locality is therefore a determinant statement, not a prime-orbit bijection.

The paper makes four claims.

1.  **Genuine same-object factorization.** The intrinsic parity extension is transitive at every nonempty finite cutoff, mixing from two atoms onward, and its regular determinant factors exactly into the two character blocks in [\[1.2\]](#1.2){reference-type="eqref" reference="1.2"}.

2.  **Functorial one-letter rigidity.** Under inclusion compatibility, relabeling naturality, and operator-coherent atom locality in a faithful representation, every label is $a^{|S|}$. A transitive full fiber is consequently cyclic.

3.  **Primitive obstruction.** The exact lift formula distinguishes primitive base necklaces from primitive lifted cycles and proves that mixed lifts persist. No orbitwise $p\leftrightarrow\gamma_p$ ledger survives in the whole extension.

4.  **Adversarial stop.** The factorization is a polynomial identity for arbitrary inventories. Prime, shuffled-prime, composite, and random-rational controls all pass with the same rate, so the identity pass-rate margin is zero.

The exact prototype supports the algebraic theorems without fitting: all formal determinant checks through ten atoms have zero mismatch; 300 trace-repetition rows and 350 $C_m$ character rows are exact; the naturality enumeration contains 72,079 tables; all 64 inventory controls and all 14 unit tests pass. These numbers certify implementation and boundary cases. They do not substitute for the proofs.

The resulting Route-A tuple is $$\begin{aligned}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
\texttt{A1\_WEAK},
\texttt{A2\_ANALYTIC\_DETERMINANT},\\
&\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\texttt{A4\_FAIL}).
\end{aligned}
\tag{1.4}\label{1.4}$$ The A3 coordinate credits only the exact same-object Artin structure in the honest domain; it does not borrow an external continuation theorem. Primitive mismatch and zero control margin force `ROUTE_A_REJECTED / STOP_SCOPED / PROVES_TOO_MUCH`. No Hilbert space generator, self-adjointness argument, completed divisor, or Weil compression is present, so Route B is locked.

separates the classical Artin machinery from the scoped claim. freezes the symbolic object. proves the exact character factors, and proves cyclic rigidity. The primitive and control obstructions occupy [\[sec:lifts,sec:certificates\]](#sec:lifts,sec:certificates){reference-type="ref" reference="sec:lifts,sec:certificates"}; [8](#sec:route){reference-type="ref" reference="sec:route"} records the analytic and Route-A boundary.

# Classical Artin machinery and the scoped contribution {#sec:classical}

#### Shift determinants.

For a finite weighted shift of finite type, periodic-path traces and adjacency determinants are two descriptions of the same zeta data. The determinant and rationality framework goes back at least to @BowenLanford1970. SD-C19 uses its smallest weighted instance: one base vertex, parallel subset edges, and a finite group fiber. The finite matrix is not presented as a new definition of dynamical zeta.

#### Group extensions and twisted transfer operators.

Representation-resolved dynamical $L$-functions for genuine group extensions are classical. @ParryPollicott1986 develop Frobenius and Chebotarev structure for Galois covers of Axiom-A flows; @AdachiSunada1987 establish twisted Perron--Frobenius and $L$-function machinery; and Chapter 8 of @ParryPollicott1990 gives a systematic account of group extensions and their character factors. Those works justify the regular/isotypic decomposition used below. We do not claim priority for that mechanism.

#### Cohomology and periodic data.

The periodic obstruction to a cocycle coboundary is rooted in Livšic theory [@Livsic1972]. Compact-group and matrix versions sharpen this principle in hyperbolic settings [@ParryPollicott1997; @Kalinin2011]. The direction needed here is elementary: a coboundary has identity product on every periodic word, whereas the singleton fixed point of [\[1.1\]](#1.1){reference-type="eqref" reference="1.1"} has product $a\ne e$. This observation prevents a gauge-trivial construction from being counted as fiber motion.

#### Graph and hypergraph covers.

Artin factorization for finite graph coverings is developed by @StarkTerras1996 [@StarkTerras2000]. The hypergraph extension of @EylerJun2024 is particularly close in vocabulary because its objects also carry incidence and subset structure. In those theories, local factors come from covering prime cycles and their Frobenius elements. SD-C19 instead starts with a signed complete subset alphabet and a uniform degree cocycle. The algebraic resemblance is real, but the orbit ledger is different.

#### A determinant is not a complete extension invariant.

@BoyleSchmieding2017 show that finite-group extensions of shifts of finite type can share zeta or periodic data without being conjugate. This is an important claim boundary: the exact character determinants below do not classify the cocycle or its symbolic extension.

L0.24 \>X \>X Component & Classical boundary & SD-C19 claim\
Finite shift determinant & weighted adjacency and periodic traces & signed tensor-subset specialization\
Finite-group Artin blocks & regular representation decomposes into irreducibles & intrinsic degree cocycle repairs frozen-roof commutation\
Cocycle cohomology & periodic identity is necessary for a coboundary & singleton fixed point proves genuine motion\
Cover local factors & Frobenius factors for graph/hypergraph prime cycles & atom-local factor plus primitive-lift mismatch\
Rigidity & no general novelty claim & one-letter natural operator-clean rules have cyclic power image\

The contribution is therefore an exact synthesis plus a scoped theorem. The specific signed tensor-subset transfer admits a lawful parity cover, and the same coefficient calculation that makes the cover clean proves that the natural one-letter branch is only cyclic degree count. Transition-dependent cocycles remain outside this conclusion.

# The frozen tensor-subset shift and its parity fiber {#sec:source}

## Tensor source and signed alphabet

Let $$\mathcal M=\{F_n:n\ge1\},\qquad
F_m\otimes F_n=F_{mn},\qquad h(F_n)=\log n.
\tag{3.1}\label{3.1}$$ The tensor-indecomposable elements are $F_p$. Fix a finite atom set $P$ and assign a commuting variable $x_p$ to each atom. The alphabet and full shift are $$\mathcal E_P=\{S:\varnothing\ne S\subseteq P\},\qquad
X_P=\mathcal E_P^{\mathbb Z},\qquad \sigma:X_P\to X_P.
\tag{3.2}\label{3.2}$$ For $S\in\mathcal E_P$, set $$x_S=\prod_{p\in S}x_p,\qquad
\varepsilon(S)=(-1)^{|S|+1},\qquad
w(S)=\varepsilon(S)x_S.
\tag{3.3}\label{3.3}$$ The sign in [\[3.3\]](#3.3){reference-type="eqref" reference="3.3"} is an ordinary scalar edge coefficient. On a temporal repetition it is raised to the corresponding scalar power; it is not replaced by a chain or supertrace convention.

Arithmetic specialization takes $x_p=p^{-s}$ and $$T(S)=\sum_{p\in S}\log p,\qquad
w_s(S)=\varepsilon(S)e^{-sT(S)}.
\tag{3.4}\label{3.4}$$ The polynomial identities are established before this specialization. Thus primality is part of the source interpretation but not an ingredient in the factorization proof.

## The intrinsic $C_2$ extension

Write $C_2=\{0,1\}$ additively and define $$\alpha_P(S)=|S|\pmod2.
\tag{3.5}\label{3.5}$$ The skew product is $$\sigma_\alpha(x,g)=\bigl(\sigma x,g+\alpha_P(x_0)\bigr).
\tag{3.6}\label{3.6}$$ For $h\in C_2$, deck translation $R_h(x,g)=(x,g+h)$ satisfies $$R_h\sigma_\alpha(x,g)
=\bigl(\sigma x,g+\alpha_P(x_0)+h\bigr)
=\sigma_\alpha R_h(x,g).
\tag{3.7}\label{3.7}$$ Equation [\[3.7\]](#3.7){reference-type="eqref" reference="3.7"} remains true after every roof specialization because $R_h$ acts only on the fiber. It never permutes $P$, $x_p$, or $T(S)$.

[\[prop:mixing\]]{#prop:mixing label="prop:mixing"} For every nonempty finite $P$, the $C_2$ extension is topologically transitive. It has period two when $|P|=1$ and is mixing when $|P|\ge2$.

Every singleton symbol has odd degree and switches the two fiber states, so the two-state presentation is strongly connected. If $|P|=1$, every edge switches the fiber and every closed path has even length. If $|P|\ge2$, an even subset symbol gives a loop at each fiber state. Strong connectivity together with a length-one loop makes the period one.

The singleton fixed point has cocycle product $1\in C_2$, which is nonidentity. Since a vertex coboundary telescopes to identity on every periodic orbit, the parity cocycle is not a coboundary. This is the finite full-shift instance of the periodic-data firewall familiar from Livšic theory [@Livsic1972; @Kalinin2011].

## Honest countable domain

The compatible countable atom limit is used only where its finite-fiber weighted adjacency series converges absolutely. For $\sigma_0=\operatorname{Re}s>1$, $$\sum_{\varnothing\ne S\subset_{\rm fin}\mathbb P}|x_S|
=\prod_p(1+p^{-\sigma_0})-1<\infty.
\tag{3.8}\label{3.8}$$ Consequently the series defining the $2\times2$ fiber matrix converges in operator norm, locally uniformly on $\operatorname{Re}s>1$, and defines a holomorphic matrix family there. We do not replace this finite-fiber quotient with an unproved nuclear Ruelle operator on a larger countable-shift Banach space.

# Same-object Artin character factors {#sec:factorization}

## Regular and isotypic transfers

Let $L_a=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ denote left translation by the nonidentity element of $C_2$. The frozen regular transfer is $$B_{\mathrm{reg},P}(x)=
\sum_{\varnothing\ne S\subseteq P}\varepsilon(S)x_SL_a^{|S|},
\qquad
D_{\mathrm{reg},P}(x)=\det(I-B_{\mathrm{reg},P}(x)).
\tag{4.1}\label{4.1}$$ For the characters $\chi_+(a)=1$ and $\chi_-(a)=-1$, set $$B_{\chi,P}(x)=\sum_S\varepsilon(S)x_S\chi(a)^{|S|},
\qquad D_{\chi,P}(x)=1-B_{\chi,P}(x).
\tag{4.2}\label{4.2}$$

[\[thm:artin\]]{#thm:artin label="thm:artin"} Let $G$ be finite and let $\alpha:\mathcal E_P\to G$ be any one-letter cocycle. For $$B_{\mathrm{reg}}=\sum_S\varepsilon(S)x_SL_{\alpha(S)}$$ and $$B_\rho=\sum_S\varepsilon(S)x_S\rho(\alpha(S)),
\qquad D_\rho=\det(I-B_\rho),$$ one has $$\det(I-B_{\mathrm{reg}})=\prod_{\rho\in\widehat G}D_\rho^{d_\rho},
\qquad d_\rho=\dim\rho.
\tag{4.3}\label{4.3}$$ The trivial block is independent of the cocycle and equals $$D_{\mathbf 1}(x)=\prod_{p\in P}(1-x_p).
\tag{4.4}\label{4.4}$$

Left convolution commutes with right deck translations. The regular representation decomposes into $d_\rho$ copies of each irreducible $\rho$, so determinants multiply blockwise. Equation [\[4.4\]](#4.4){reference-type="eqref" reference="4.4"} is finite inclusion--exclusion. Full details appear in [10.1](#app:proof-artin){reference-type="ref" reference="app:proof-artin"}.

Theorem [\[thm:artin\]](#thm:artin){reference-type="ref" reference="thm:artin"} is classical machinery, not the novelty claim. Its role is logical: every factor below belongs to the same regular transfer.

## Degree-power factorization

[\[thm:degree-power\]]{#thm:degree-power label="thm:degree-power"} Fix $a\in G$, set $\alpha(S)=a^{|S|}$, and write $A=\rho(a)$. Then $$I-B_\rho(x)=\prod_{p\in P}(I-x_pA),
\qquad
D_\rho(x)=\prod_{p\in P}\det(I-x_pA).
\tag{4.5}\label{4.5}$$

Expanding the commuting matrix product gives $$\prod_p(I-x_pA)=
I+\sum_{k\ge1}(-1)^ke_k(x)A^k
=I-B_\rho(x).$$ Taking determinants proves the second identity.

For the primary $C_2$ extension, [\[thm:degree-power\]](#thm:degree-power){reference-type="ref" reference="thm:degree-power"} gives $$D_+(x)=\prod_p(1-x_p),\qquad
D_-(x)=\prod_p(1+x_p),\qquad
D_{\mathrm{reg}}(x)=\prod_p(1-x_p^2).
\tag{4.6}\label{4.6}$$ At $x_p=p^{-s}$, $\operatorname{Re}s>1$, $$D_+(s)=\frac1{\zeta(s)},\qquad
D_-(s)=\frac{\zeta(s)}{\zeta(2s)},\qquad
D_{\mathrm{reg}}(s)=\frac1{\zeta(2s)}.
\tag{4.7}\label{4.7}$$

#### Whole versus block.

Only $D_{\mathrm{reg}}$ in [\[4.6\]](#4.6){reference-type="eqref" reference="4.6"} is the determinant of the whole regular extension. The quantities $D_+$ and $D_-$ are determinants of invariant isotypic blocks of that same operator. Calling either block the whole-extension determinant would erase the Artin decomposition rather than use it.

#### Two-atom certificate.

For variables $x,y$, the singleton symbols have weights $x,y$ and fiber label $a$, while $\{p,q\}$ has weight $-xy$ and identity fiber label. Thus $$B_{\mathrm{reg}}=(x+y)L_a-xyI,\qquad
\det(I-B_{\mathrm{reg}})=(1-x^2)(1-y^2),
\tag{4.8}\label{4.8}$$ and diagonalizing $L_a$ yields $$D_+=(1-x)(1-y),\qquad D_-=(1+x)(1+y).
\tag{4.9}\label{4.9}$$ This is the smallest direct certificate that motion, character factors, and the whole cover use one matrix and one normalization.

#### General cyclic fiber.

For $C_m=\langle a\rangle$, $\omega=e^{2\pi i/m}$, and $\chi_j(a)=\omega^j$, $$D_j(x)=\prod_p(1-\omega^jx_p),\qquad
D_{\mathrm{reg}}(x)=\prod_{j=0}^{m-1}D_j(x)=\prod_p(1-x_p^m).
\tag{4.10}\label{4.10}$$ The local factors in [\[4.5\]](#4.5){reference-type="eqref" reference="4.5"} and [\[4.10\]](#4.10){reference-type="eqref" reference="4.10"} are indexed by single atoms. This does not say that their coefficient expansions lack mixed monomials or that the symbolic extension lacks mixed primitive cycles.

# Rigidity of natural one-letter factorizations {#sec:rigidity}

The degree cocycle was not selected merely because it produces a convenient example. Within the frozen one-letter class, it is forced by a natural operator-level no-leak requirement. We make the quantifiers explicit because weakening any one of them changes the conclusion.

[\[def:natural-family\]]{#def:natural-family label="def:natural-family"} For every finite atom set $P$, let $\alpha_P:\mathcal E_P\to G$. The family is *relabeling-natural* if $$\alpha_{P'}(\phi S)=\alpha_P(S)$$ for every bijection $\phi:P\to P'$, and it is *inclusion-compatible* if $\alpha_Q(S)=\alpha_P(S)$ whenever $P\subseteq Q$ and $\varnothing\ne S\subseteq P$. These are conditions on the symbolic alphabet rule, not changes of coordinates on the transfer operator.

Naturality makes the label depend only on subset cardinality. Compatibility then makes that dependence independent of the ambient inventory: there are elements $g_k\in G$ such that $$\alpha_P(S)=g_{|S|}
\quad\text{whenever}\quad |P|\ge |S|.
\tag{5.1}\label{5.1}$$ Let $\rho:G\to \mathrm{GL}(V)$ be a representation and put $A=\rho(g_1)$.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} Suppose the family in [\[def:natural-family\]](#def:natural-family){reference-type="ref" reference="def:natural-family"} is inclusion-compatible and relabeling-natural. Assume that, for every finite $P$, the same matrix-valued transfer obeys the operator-coherent atom-local identity $$I-\sum_{\varnothing\ne S\subseteq P}
  \varepsilon(S)x_S\rho(g_{|S|})
=\prod_{p\in P}(I-x_pA).
\tag{5.2}\label{5.2}$$ Then $$\rho(g_k)=A^k\qquad(k\ge1).
\tag{5.3}\label{5.3}$$ If $\rho$ is faithful, then $g_k=g_1^k$. In particular, for the faithful regular representation the cocycle has the degree-power form $$\alpha_P(S)=a^{|S|},\qquad a=g_1.
\tag{5.4}\label{5.4}$$ If the corresponding skew-product shift is transitive on the entire fiber $G$, then $G=\langle a\rangle$, so $G$ is cyclic.

The symmetric group on $P$ is transitive on its $k$-subsets; this and inclusion compatibility give [\[5.1\]](#5.1){reference-type="eqref" reference="5.1"}. Fix $k$ and choose $|P|\ge k$. For any squarefree monomial $x_S$, $|S|=k$, its coefficient on the left of [\[5.2\]](#5.2){reference-type="eqref" reference="5.2"} is $(-1)^k\rho(g_k)$, while expansion of the right side gives $(-1)^kA^k$. Thus [\[5.3\]](#5.3){reference-type="eqref" reference="5.3"} holds. Faithfulness gives $g_k=g_1^k$.

Every edge label in the skew product then lies in $\langle a\rangle$. Starting from one fiber state, all reachable fiber states remain in one coset of that subgroup. Transitivity on all of $G$ therefore forces a single coset, hence $G=\langle a\rangle$. A more detailed coefficient proof is recorded in [10.3](#app:proof-rigidity){reference-type="ref" reference="app:proof-rigidity"}.

The theorem explains both the strength and the limitation of the construction. Genuine finite-fiber motion is compatible with exact atom locality, but in the natural one-letter class the motion must be carried by powers of one element. Transitivity consequently reduces the regular fiber to a cyclic group. This is a classification statement about the present class, not a classification of finite-group extensions of shifts.

[\[cor:first-leak\]]{#cor:first-leak label="cor:first-leak"} For a one-dimensional character $\chi$, put $\lambda_k=\chi(g_k)$. If $k$ is the least index for which $\lambda_k\ne\lambda_1^k$, then the first squarefree discrepancy between the actual block and the atom product is $$\left[
D_\chi(x)-\prod_{p\in P}(1-\lambda_1x_p)
\right]_{\mathrm{degree}\ k}
=(-1)^k(\lambda_k-\lambda_1^k)e_k(x).
\tag{5.5}\label{5.5}$$ At matrix level, the two-atom discrepancy is $$xy\bigl[\rho(g_2)-\rho(g_1)^2\bigr].
\tag{5.6}\label{5.6}$$

In $D_\chi=1-B_\chi$, the degree-$k$ term is $(-1)^k\lambda_ke_k(x)$; in the proposed product it is $(-1)^k\lambda_1^ke_k(x)$. The matrix formula is the same coefficient comparison before taking a determinant.

#### Two firewalls.

First, [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"} assumes equality of matrix polynomials. Equality of one determinant in a selected higher-dimensional representation may hide spectral coincidences and is not covered. Second, the theorem is deliberately one-letter: it does not constrain a transition cocycle $\alpha(S,T)$, a higher-memory cocycle, or a cocycle obtained after a state-splitting presentation. Those objects are outside the theorem rather than counterexamples to it.

[\[prop:not-coboundary\]]{#prop:not-coboundary label="prop:not-coboundary"} If $a\ne e$, the cocycle $\alpha(S)=a^{|S|}$ is not cohomologous to the identity cocycle on the full subset shift.

The period-one orbit repeating a singleton has cocycle product $a\ne e$. Every coboundary has identity product around every periodic orbit, because its transfer terms telescope. The periodic obstruction therefore rules out a coboundary. This is the smallest witness that the fiber motion is genuine; it does not depend on a relabeling of the original symbols [@Livsic1972; @ParryPollicott1997; @Kalinin2011].

# Primitive lifting and the orbit-level mismatch {#sec:lifts}

The determinant factorization is exact, but an Artin block is not an independent inventory of base primitive cycles. This section separates the three objects that are easiest to conflate:

1.  a primitive necklace in the base subset shift;

2.  its Frobenius displacement in the finite fiber; and

3.  the primitive cycles lying above it in the skew-product shift.

Let $$\gamma=[S_0S_1\cdots S_{r-1}]
\tag{6.1}\label{6.1}$$ be a primitive base necklace of least period $r$. Its total subset degree is $$c(\gamma)=\sum_{i=0}^{r-1}|S_i|.
\tag{6.2}\label{6.2}$$ For the $C_m=\langle a\rangle$ degree cocycle, one base traversal translates the fiber by $a^{c(\gamma)}$.

[\[thm:primitive-lift\]]{#thm:primitive-lift label="thm:primitive-lift"} Put $$q(\gamma)=\operatorname{ord}(a^{c(\gamma)})
=\frac{m}{\gcd(m,c(\gamma))}.
\tag{6.3}\label{6.3}$$ The preimage of $\gamma$ contains exactly $$\gcd(m,c(\gamma))
\tag{6.4}\label{6.4}$$ primitive lifted cycles, and every such cycle has least period $$r\,q(\gamma)
=r\,\frac{m}{\gcd(m,c(\gamma))}.
\tag{6.5}\label{6.5}$$

On the $m$ fiber points, the return map after one base traversal is translation by $c(\gamma)$ modulo $m$. Every orbit of this translation has length $q(\gamma)$, and there are $m/q(\gamma)=\gcd(m,c(\gamma))$ such orbits. A lifted return must project to a return of the primitive base cycle, hence its time is a multiple of $r$; the fiber closes for the first time after $q(\gamma)$ such traversals. Therefore the lifted period is exactly $rq(\gamma)$, and each translation orbit produces one primitive lift. See also [10.4](#app:proof-lifts){reference-type="ref" reference="app:proof-lifts"}.

For $C_2$, an odd-degree base primitive has one lifted primitive of period $2r$, whereas an even-degree base primitive has two lifted primitives of period $r$. Thus a repeated singleton does not close at the original clock, but many mixed words do. For example, the base fixed point $[\{p,q\}]$ has total degree two and therefore gives two period-one lifted cycles. The mixed base word $[\{p\}\{q\}]$, when primitive as a necklace, also has even total degree and closes after a single base traversal.

## Exact primitive-necklace recurrence

For an $n$-atom inventory define $$A_n(y)=\sum_{k=1}^{n}\binom nk y^k=(1+y)^n-1.
\tag{6.6}\label{6.6}$$ The coefficient $[y^c]A_n(y)^r$ counts length-$r$ base words of total degree $c$. If $Q_r(c)$ counts those with least period exactly $r$, unique least period gives $$Q_r(c)=[y^c]A_n(y)^r-
\sum_{\substack{d\mid r,\ d<r\\(r/d)\mid c}}
Q_d\!\left(\frac{c}{r/d}\right).
\tag{6.7}\label{6.7}$$ Every primitive necklace has $r$ distinct rotations, so the number of primitive base necklaces at $(r,c)$ is $Q_r(c)/r$. Only after this base count is fixed may [\[thm:primitive-lift\]](#thm:primitive-lift){reference-type="ref" reference="thm:primitive-lift"} be applied. Consequently the lifted count at period $rq$ is a weighted sum over base periods and degrees; it is not obtained by calling every base necklace a lifted cycle.

As a scale certificate, at $n=5,r=10,m=2$ the exact census contains $$\begin{array}{lr}
\text{primitive base necklaces}&81{,}962{,}825{,}835{,}072,\\
\text{mixed base primitives closing immediately}&40{,}981{,}411{,}486{,}080,\\
\text{primitive lifted cycles contributed by the census}&
122{,}944{,}237{,}321{,}152.
\end{array}
\tag{6.8}\label{6.8}$$ These integers answer different questions. Their simultaneous appearance is a bookkeeping check, not an identity between inventories.

## Why local products do not delete mixed dynamics

Equation [\[4.10\]](#4.10){reference-type="eqref" reference="4.10"} has one local factor per atom. Nevertheless its expanded coefficients include mixed monomials, and $-\log D_\chi$ collects all repetitions of the one-step transfer. With all $n$ variables specialized to $t$, $$B_+(t)=1-(1-t)^n,\qquad
B_-(t)=1-(1+t)^n,
\tag{6.9}\label{6.9}$$ and the determinant convention gives $$-\log D_\chi(t)=\sum_{\ell\ge1}\frac{B_\chi(t)^\ell}{\ell}.
\tag{6.10}\label{6.10}$$ Therefore $$[t^k]-\log D_+=\frac nk,\qquad
[t^k]-\log D_-=\frac{n(-1)^k}{k},
\tag{6.11}\label{6.11}$$ and $$[t^k]-\log D_{\mathrm{reg}}=
\begin{cases}
0,&k\ \text{odd},\\[2pt]
2n/k,&k\ \text{even}.
\end{cases}
\tag{6.12}\label{6.12}$$ The cancellation of odd trace coefficients is a character sum across isotypic blocks. It does not assert that odd-degree base primitives do not exist; [\[thm:primitive-lift\]](#thm:primitive-lift){reference-type="ref" reference="thm:primitive-lift"} says instead that their closing time changes. Likewise, absence of a mixed local factor means neither absence of a mixed coefficient nor absence of a mixed primitive cycle. This separation is the orbit-level reason that the exact Artin factorization does not solve the prime-singleton selection problem.

# Exact certificates, adversarial controls, and the transition boundary {#sec:certificates}

The results in [\[sec:factorization,sec:rigidity,sec:lifts\]](#sec:factorization,sec:rigidity,sec:lifts){reference-type="ref" reference="sec:factorization,sec:rigidity,sec:lifts"} are algebraic theorems. The finite computations reported here serve a narrower purpose: they certify sign conventions, repetitions, phase bookkeeping, primitive enumeration, and the scope of the hypotheses. All calculations use integers, rational numbers, sparse formal polynomials, or exact matrices. There is no floating-point root search and no target-zero input.

L0.27L0.22X Certificate & Frozen extent & Outcome\
$C_2$ block and regular determinants & $n=1,\ldots,10$ & zero formal mismatch terms\
Trace and repetition ledger & 300 rows & 300 exact coefficient identities\
$C_m$ character phases & 350 rows, $2\le m\le8$ & 350 exact cyclotomic phase ledgers\
Regular $C_m$ local determinants & seven group orders & $\prod_p(1-x_p^m)$ in every row\
Primitive base/lift census & 350 rows & recurrence, $q$, and multiplicity exact\
Natural one-letter tables & 72,079 tables in 35 cells & one operator-clean power table per cell\
Inventory controls & 64 runs & every identity exact; pass-rate margin zero\
Implementation tests & 14 tests & 14 passed, zero failures\

## Independent coefficient ledgers

The formal $C_2$ certificate constructs the regular $2\times2$ matrix and the two character blocks separately, then compares their sparse determinants. The trace certificate does not reuse the closed determinant: it expands $$\sum_{\ell\ge1}\frac{\operatorname{tr}(B^\ell)}{\ell}
\tag{7.1}\label{7.1}$$ through degree ten and compares the result with $-\log\det(I-B)$. The 300 exact agreements therefore test temporal repetitions and the scalar sign $\varepsilon(S)^\ell$, not just the inclusion--exclusion polynomial at one step.

For $C_m$, roots of unity are stored by exponent modulo $m$. The coefficient of a squarefree degree-$k$ monomial in the $j$th character block is recorded as $$\bigl((-1)^k,jk\bmod m\bigr).
\tag{7.2}\label{7.2}$$ This exact phase ledger is compared with the product $\prod_p(1-\omega^jx_p)$; multiplying all character blocks is compared independently with the determinant of the $m\times m$ regular permutation matrix.

## Finite audit of the rigidity quantifiers

After fixing the singleton label to the chosen generator $a$, relabeling naturality reduces a truncated rule to a size table $$(r_1,\ldots,r_K)\in(\mathbb Z/m\mathbb Z)^K,\qquad r_1=1,
\qquad \alpha(S)=a^{r_{|S|}}.
\tag{7.3}\label{7.3}$$ For every $m=2,\ldots,8$ and $K=2,\ldots,6$, all such tables were enumerated. Across the resulting 35 cells there are 72,079 tables. Exactly 35 satisfy all regular-representation squarefree coefficient identities: one table per cell, namely $$r_k\equiv kr_1\pmod m.
\tag{7.4}\label{7.4}$$ The enumeration is not the proof of [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"}; it is an independent finite audit that uses faithful regular coefficients and therefore does not mistake a nonfaithful character coincidence for operator coherence.

## Inventory universality and zero selectivity

The factor identities live in the free commutative polynomial ring $\mathbb Z[x_p:p\in P]$. Any substitution of commuting values preserves them. The adversarial inventory test makes that formal universality visible. It uses four matched families---prime, shuffled-prime, composite-only, and random rational---with 16 frozen seeds per family. All 64 runs satisfy all four determinant identities. Thus every family has identity pass rate one and $$\text{identity pass-rate margin}=0.
\tag{7.5}\label{7.5}$$ Equation [\[7.5\]](#7.5){reference-type="eqref" reference="7.5"} compares truth of the identities, not equality of their numerical determinant values. Different substitutions generally produce different numbers; what fails to distinguish the arithmetic inventory is the mechanism's success criterion.

This control is decisive for scope. The construction has an intrinsic arithmetic source when $x_p=p^{-s}$, but its clean factorization does not use the property of being prime. It therefore proves too much to serve as an arithmetic selector.

## Cohomology and transition countercontrols

Gauge controls separate genuine motion from a presentation artifact. In 63 vertex-coboundary rows, all audited periodic holonomies are identity and every edge label is recovered by the declared gauge. The 21 constant-holonomy negative controls all have a nonidentity periodic witness. These checks support the elementary firewall in [\[prop:not-coboundary\]](#prop:not-coboundary){reference-type="ref" reference="prop:not-coboundary"}.

Four minimal two-symbol transition rules probe exactly where the one-letter theorem stops. Their determinants are compared with the nearest atom-local character baseline: $$\begin{array}{llll}
\toprule
\text{rule}&\text{coboundary}&\text{first leakage}&\text{periodic witness}\\
\midrule
\text{vertex coboundary degree}&\text{yes}&\text{none}&\text{none}\\
\text{diagonal return}&\text{no}&-2xy&(1)\\
\text{incidence-intersection parity}&\text{no}&+2xy^2&(1)\\
\text{strict symbol change}&\text{no}&-4x^2y^2&(1,2,3)\\
\bottomrule
\end{array}
\tag{7.6}\label{7.6}$$ The coboundary row is exactly atom-local after gauge conjugacy. Each of the three noncoboundary rows has a periodic witness and eventually leaks. Notably, strict symbol change is clean at lower squarefree degrees but first fails at a temporal-power monomial. Transition dependence is therefore a real loophole in [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"}, while low-degree squarefree cleanliness is not enough to exploit it.

The next symbolic test must combine the two merge orders on a $p,q,r$ incidence/refinement grammar with their commutator holonomy and the $p^2q^2$ repetition ledger. That is a forward obligation within Symbolic Dynamics, not a theorem claimed in this paper.

# Analytic boundary and strict route evaluation {#sec:route}

## What is analytic on the honest domain

For each finite $P$, every transfer in this paper is a finite matrix with polynomial entries. In the countable prime limit, $$\sum_{\varnothing\ne S\subset_{\mathrm{fin}}\mathbb P}
|x_S|
=\prod_p(1+p^{-\sigma})-1<\infty,
\qquad \sigma=\operatorname{Re}s>1.
\tag{8.1}\label{8.1}$$ The $C_2$ regular adjacency series consequently converges locally uniformly in operator norm to a holomorphic $2\times2$ matrix family. Its determinant and both isotypic block determinants are holomorphic on $\operatorname{Re}s>1$, and the Euler identities in [\[4.7\]](#4.7){reference-type="eqref" reference="4.7"} hold there by absolute convergence. This is an honest analytic determinant statement.

It is not a new continuation theorem. Once $\zeta$ is named, the displayed ratios may of course be continued using external number theory, but that continuation is not generated by the symbolic transfer construction. Accordingly no continuation, functional equation, gamma factor, completed divisor, or zero-counting law is imported into the Route-A score.

## The fixed-normalization and finite-fiber firewalls

Introduce an auxiliary temporal parameter $z$ in a scalar character block. Since $$B_j(x)=1-\prod_p(1-\omega^jx_p),$$ one obtains $$\det(I-zB_j)
=1-z+z\prod_p(1-\omega^jx_p).
\tag{8.2}\label{8.2}$$ At $z=1$ the first two terms cancel. For generic $z\ne1$, [\[8.2\]](#8.2){reference-type="eqref" reference="8.2"} is not a product of independent atom factors. The clean formula is therefore an exact identity at the frozen determinant normalization, not an off-shell family of local factors.

Finiteness of the regular fiber is also load-bearing. Replacing $C_m$ by $\mathbb Z$ sends its generator to the bilateral shift $U$ on $\ell^2(\mathbb Z)$, and the formal degree-power identity becomes $$I-B=\prod_p(I-x_pU).
\tag{8.3}\label{8.3}$$ For a nonzero finite inventory, $B$ is a nonzero translation-invariant band operator. It is not compact and hence not trace class. The ordinary Fredholm determinant of the full regular object is unavailable; the standard trace-class determinant theory cannot simply be invoked [@Simon1977]. Bloch characters retain scalar products $\prod_p(1-wx_p)$, but their direct integral is not an ordinary determinant of $I-B$. Thus the finite Artin certificate does not pass automatically to an infinite regular fiber.

## Route A

L0.13 \>X \>X Coordinate & Credited evidence & Strongest failure\
`A0`\
analytic arithmetic origin & Tensor indecomposability identifies $F_p$, and entropy supplies $\log p$ before specialization. & Every matched nonprime inventory satisfies the same identity.\
`A1`\
weak & Base primitives, Frobenius degree, traversal number, and lift multiplicity are intrinsic and exact. & Singleton clocks multiply; mixed primitives close immediately whenever $m\mid c$.\
`A2`\
analytic determinant & One finite-fiber transfer has exact regular and isotypic determinants, holomorphic for $\operatorname{Re}s>1$. & Atom locality holds only at $z=1$ and does not give a primitive prime-orbit bijection.\
`A3`\
partial analytic structure & The same object has a genuine Artin block decomposition on its honest domain. & No intrinsic completion, functional equation, counting law, global target divisor, or Weil compression is produced.\
`A4`\
fail & The symbolic skew extension and all finite transfer operators are explicit. & No natural quantization, self-adjoint generator, operator domain, or Hilbert--Pólya spectral carrier is supplied.\

The tuple is therefore fixed as $$\boxed{
\begin{aligned}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
\texttt{A1\_WEAK},
\texttt{A2\_ANALYTIC\_DETERMINANT},\\[-1pt]
&\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\texttt{A4\_FAIL}).
\end{aligned}}
\tag{8.4}\label{8.4}$$ The A3 coordinate is deliberately narrow: it credits the Artin structure of the same symbolic object and the holomorphic honest domain, not meromorphic continuation imported after identifying a classical Euler product.

At orbit level, [\[thm:primitive-lift\]](#thm:primitive-lift){reference-type="ref" reference="thm:primitive-lift"} leaves A1 weak. At control level, [\[7.5\]](#7.5){reference-type="eqref" reference="7.5"} proves arithmetic nonselectivity. At whole-object level, the two isotypic factors combine to $D_{\mathrm{reg}}(s)=\zeta(2s)^{-1}$; neither block may be substituted for that whole determinant. These independent stops yield $$\texttt{ROUTE\_A\_REJECTED},\qquad
\texttt{STOP\_SCOPED / PROVES\_TOO\_MUCH}.
\tag{8.5}\label{8.5}$$

## Route B remains locked

No self-adjoint operator with target spectral ordinates, no domain theorem, no resolvent or scattering construction, and no trace-formula positivity statement arises from SD-C19. Route B is therefore not invoked: $$\texttt{ROUTE\_B\_LOCKED}.
\tag{8.6}\label{8.6}$$ This lock is a scope decision, not evidence against the existence of an operator in some other framework. Such a move would change the main system family and is recorded only as a `ROUND2_CLUE`.

# Conclusion {#sec:conclusion}

The parity cocycle repairs the precise defect left by atom relabeling. It lives on a separate finite fiber, its deck action commutes with the frozen weighted shift, and its two character determinants are invariant blocks of one regular transfer. The resulting identities $$D_+=\prod_p(1-x_p),\qquad
D_-=\prod_p(1+x_p),\qquad
D_{\mathrm{reg}}=\prod_p(1-x_p^2)$$ are exact and analytically honest on $\operatorname{Re}s>1$.

The same calculation also closes the natural one-letter branch. Functorial operator-level atom locality forces $\alpha(S)=a^{|S|}$, and transitivity of the whole fiber forces a cyclic group. This cleanliness does not align primitive cycles with atoms: base and lifted primitives have different clocks, mixed immediate closures persist, and arbitrary control inventories reproduce the determinant identities with zero pass-rate margin. The outcome is a genuine same-object Artin factor and a useful rigidity obstruction, but not an RH mechanism.

The next admissible step stays inside Symbolic Dynamics and leaves one-letter cocycles behind. A transition label derived from subset incidence or refinement must be tested simultaneously for noncommuting merge-order holonomy and temporal-power leakage. Until that test is passed, the strict status remains $\texttt{ROUTE\_A\_REJECTED / STOP\_SCOPED / PROVES\_TOO\_MUCH}$ with $\texttt{ROUTE\_B\_LOCKED}$.

#### Data and reproducibility.

The claims use exact formal and finite computations with frozen cutoffs and controls; no target-zero data are used. The certificate definitions needed to reconstruct each reported count are summarized in [11](#app:certificates){reference-type="ref" reference="app:certificates"}.

#### Ethics statement.

This work uses no human participants, personal data, animals, or sensitive datasets.

#### Author contributions.

The anonymous authors jointly developed the construction, proofs, exact certificate design, analysis, and manuscript.

#### Conflicts of interest.

The authors declare no conflicts of interest.

#### Funding.

No external funding is declared.

#### Use of generative tools.

Generative tools assisted algebraic drafting and implementation checks. Every theorem, displayed identity, citation, and reported certificate was audited against the frozen source and exact artifacts; no generated output is used as mathematical evidence by itself.

# Expanded algebraic proofs {#app:proofs}

## Regular decomposition and the determinant convention {#app:proof-artin}

Let $\mathbb C[G]$ have basis $\{\delta_h:h\in G\}$, and define $L_g\delta_h=\delta_{gh}$. The finite regular representation has the Fourier decomposition $$\mathbb C[G]\cong\bigoplus_{\rho\in\widehat G}V_\rho^{\oplus d_\rho},
\qquad d_\rho=\dim V_\rho.
\tag{A.1}\label{A.1}$$ Under [\[A.1\]](#A.1){reference-type="eqref" reference="A.1"}, left multiplication by $g$ acts as $d_\rho$ copies of $\rho(g)$ on the $\rho$-summand. Linearity therefore sends $$B_{\mathrm{reg}}=\sum_S\varepsilon(S)x_SL_{\alpha(S)}$$ to $d_\rho$ copies of $$B_\rho=\sum_S\varepsilon(S)x_S\rho(\alpha(S)).$$ Since [\[A.1\]](#A.1){reference-type="eqref" reference="A.1"} is a similarity transformation over $\mathbb C$, $$\det(I-B_{\mathrm{reg}})
=\prod_{\rho\in\widehat G}\det(I-B_\rho)^{d_\rho}.
\tag{A.2}\label{A.2}$$ This proves [\[thm:artin\]](#thm:artin){reference-type="ref" reference="thm:artin"}. Notice that [\[A.2\]](#A.2){reference-type="eqref" reference="A.2"} fixes the terminology: the determinant on the left belongs to the whole regular extension, while an individual factor on the right belongs to an isotypic block.

For $\rho=\mathbf 1$, every group element maps to one. Hence $$D_{\mathbf 1}
=1-\sum_{\varnothing\ne S\subseteq P}(-1)^{|S|+1}x_S
=\prod_{p\in P}(1-x_p).
\tag{A.3}\label{A.3}$$ The sign in [\[A.3\]](#A.3){reference-type="eqref" reference="A.3"} is the ordinary scalar coefficient of an edge. In a length-$\ell$ closed word, the coefficient is the product of its $\ell$ edge coefficients; no supertrace or homological sign is inserted.

## Degree powers, characters, and the regular local factor

For $A=\rho(a)$, all factors $I-x_pA$ commute. Expanding by squarefree monomials gives $$\prod_{p\in P}(I-x_pA)
=I+\sum_{\varnothing\ne S\subseteq P}(-1)^{|S|}x_SA^{|S|}
=I-B_\rho.
\tag{A.4}\label{A.4}$$ Taking determinants gives [\[thm:degree-power\]](#thm:degree-power){reference-type="ref" reference="thm:degree-power"}. In $C_m$, every irreducible is the character $\chi_j(a)=\omega^j$, so $$D_j=\prod_p(1-\omega^jx_p).
\tag{A.5}\label{A.5}$$ Multiplication over the $m$ characters may be reordered atom by atom: $$\prod_{j=0}^{m-1}D_j
=\prod_p\prod_{j=0}^{m-1}(1-\omega^jx_p)
=\prod_p(1-x_p^m).
\tag{A.6}\label{A.6}$$ This is also $\det(I-x_pL_a)=1-x_p^m$ locally in the regular representation. For $m=2$, [\[A.5\]](#A.5){reference-type="eqref" reference="A.5"} and [\[A.6\]](#A.6){reference-type="eqref" reference="A.6"} yield $D_+$, $D_-$, and $D_{\mathrm{reg}}$ in [\[4.6\]](#4.6){reference-type="eqref" reference="4.6"}.

## Naturality and operator-coherent rigidity {#app:proof-rigidity}

Fix $k$. If $S,T\subseteq P$ both have $k$ elements, a permutation of $P$ takes $S$ to $T$. Relabeling naturality gives $\alpha_P(S)=\alpha_P(T)$; call this value $g_{k,P}$. If $P\subseteq Q$, inclusion compatibility gives $g_{k,P}=g_{k,Q}$. Any two finite ambient sets embed into a larger one, so the common value is a single element $g_k$ independent of $P$.

Now assume [\[5.2\]](#5.2){reference-type="eqref" reference="5.2"}. For a fixed squarefree $x_S$, $|S|=k$, the coefficient on its left side is $$-\varepsilon(S)\rho(g_k)=(-1)^k\rho(g_k).
\tag{A.7}\label{A.7}$$ The coefficient obtained by choosing $-x_pA$ for $p\in S$ and $I$ elsewhere on the right side is $$(-1)^kA^k.
\tag{A.8}\label{A.8}$$ Equating [\[A.7\]](#A.7){reference-type="eqref" reference="A.7"} and [\[A.8\]](#A.8){reference-type="eqref" reference="A.8"} proves $\rho(g_k)=A^k$ for all $k$. If $\rho$ is faithful, then $$g_k=g_1^k.
\tag{A.9}\label{A.9}$$

Let $H=\langle g_k:k\ge1\rangle$. Along every skew-product path, the fiber increment lies in $H$, so a path starting at $g\in G$ stays in the coset $gH$ (with the left/right choice adjusted to the cocycle convention). Strong connectivity of the whole fiber forces $H=G$. Under [\[A.9\]](#A.9){reference-type="eqref" reference="A.9"}, $H=\langle g_1\rangle$, hence $G$ is cyclic. This completes the detailed proof of [\[thm:rigidity\]](#thm:rigidity){reference-type="ref" reference="thm:rigidity"}.

The faithful or operator-level hypothesis cannot be dropped silently. A nonfaithful one-dimensional character only sees the quotient by its kernel, and a determinant in dimension greater than one records eigenvalue products rather than every matrix coefficient. Such tests may miss $\rho(g_k)-\rho(g_1)^k$.

## Primitive base necklaces and lifted cycles {#app:proof-lifts}

Let $\gamma$ be a primitive base orbit of period $r$, choose one base phase, and identify the $C_m$ fiber with $\mathbb Z/m\mathbb Z$. One traversal of $\gamma$ sends $$u\longmapsto u+c(\gamma)\pmod m.
\tag{A.10}\label{A.10}$$ The least positive $h$ for which $hc(\gamma)\equiv0\pmod m$ is $$q=\frac{m}{\gcd(m,c(\gamma))}.
\tag{A.11}\label{A.11}$$ Thus the translation in [\[A.10\]](#A.10){reference-type="eqref" reference="A.10"} partitions the fiber into $m/q=\gcd(m,c(\gamma))$ orbits, each of length $q$.

If a lifted point returned after $d$ shift steps, its base projection would return after $d$ steps. Primitivity of the base orbit gives $r\mid d$; write $d=rh$. Its fiber returns precisely when $hc(\gamma)\equiv0\pmod m$, whose least positive solution is $h=q$. Every fiber-translation orbit therefore yields one primitive lifted orbit of least period $rq$, proving [\[thm:primitive-lift\]](#thm:primitive-lift){reference-type="ref" reference="thm:primitive-lift"}.

For completeness, the recurrence [\[6.7\]](#6.7){reference-type="eqref" reference="6.7"} follows from unique minimal period. There are $[y^c]A_n(y)^r$ length-$r$ words of total degree $c$. A word of minimal period $d<r$ is an $(r/d)$-fold repetition, so its primitive block has degree $c/(r/d)$; this contribution exists only if $(r/d)\mid c$. Subtracting every proper divisor contribution gives $Q_r(c)$. A word of minimal period $r$ has exactly $r$ distinct rotations, so $Q_r(c)/r$ is the primitive-necklace count.

## The countable honest domain and the infinite-fiber stop

For $\sigma>1$, $\sum_pp^{-\sigma}<\infty$, and therefore $$\prod_p(1+p^{-\sigma})
\le \exp\!\left(\sum_pp^{-\sigma}\right)<\infty.
\tag{A.12}\label{A.12}$$ Expanding the positive product proves [\[8.1\]](#8.1){reference-type="eqref" reference="8.1"}. On every closed half-plane $\operatorname{Re}s\ge1+\delta$, the same bound is uniform. The finite-fiber adjacency series is dominated in matrix norm by [\[A.12\]](#A.12){reference-type="eqref" reference="A.12"}, so the Weierstrass test gives local uniform convergence and holomorphy.

By contrast, let $P(U)\ne0$ be a finite Laurent polynomial in the bilateral shift. The vectors $P(U)e_n$ are translates of one nonzero finitely supported vector. A subsequence with mutually disjoint supports has constant nonzero norm and no convergent subsequence. Hence $P(U)$ is not compact. In particular it is not trace class, which blocks the ordinary determinant of an identity plus trace-class operator. This proves the finite/infinite fiber distinction used in [8](#sec:route){reference-type="ref" reference="sec:route"}.

# Exact certificate definitions {#app:certificates}

## Formal determinant and trace certificates

For a cutoff $n$, the formal certificate uses independent indeterminates $x_1,\ldots,x_n$. It constructs $$B_+=\sum_{\varnothing\ne S}\varepsilon(S)x_S,\qquad
B_-=\sum_{\varnothing\ne S}\varepsilon(S)(-1)^{|S|}x_S
\tag{B.1}\label{B.1}$$ and the regular matrix $$B_{\mathrm{reg}}=\sum_{\varnothing\ne S}\varepsilon(S)x_SL_a^{|S|}.
\tag{B.2}\label{B.2}$$ Sparse polynomial comparison tests $$1-B_+=\prod_i(1-x_i),\quad
1-B_-=\prod_i(1+x_i),\quad
\det(I-B_{\mathrm{reg}})=(1-B_+)(1-B_-).
\tag{B.3}\label{B.3}$$ No block is reconstructed by dividing the regular determinant after the fact.

The repetition ledger specializes all $x_i=t$, expands $$\sum_{\ell=1}^{K}\frac{\operatorname{tr}(B^\ell)}{\ell}
\tag{B.4}\label{B.4}$$ with enough temporal powers to determine degrees through $K$, and compares each coefficient with the truncated series of $-\log\det(I-B)$. In particular, the scalar sign attached to each symbol is multiplied along a word. The 300 reported rows comprise the three transfers $+$, $-$, and regular, ten atom cutoffs, and ten coefficient degrees.

## Cyclic phases and primitive recurrence

For a $C_m$ character, a coefficient is stored as a pair $(q,r)$ representing $q\omega^r$, with $q\in\mathbb Z$ and $r\in\mathbb Z/m\mathbb Z$. Multiplication adds phase exponents modulo $m$, so no floating approximation to $\omega$ enters. The independent regular test forms the exact cyclic permutation matrix and verifies $$\det(I-xL_a)=1-x^m.
\tag{B.5}\label{B.5}$$

Primitive words are counted first in the base. The dynamic recurrence is initialized by $Q_1(c)=\binom nc$ for $1\le c\le n$ and zero outside the allowed range; higher $Q_r(c)$ use [\[6.7\]](#6.7){reference-type="eqref" reference="6.7"}. Divisibility by $r$ is checked before forming $Q_r(c)/r$. For each base cell, the separate lift ledger records $$\operatorname{Frob}(\gamma)=a^c,\qquad
q=\frac{m}{\gcd(m,c)},\qquad
\text{lift multiplicity}=\gcd(m,c).
\tag{B.6}\label{B.6}$$ The base-necklace count, immediate mixed-closure count, and lifted-cycle count remain separate output fields.

## Naturality, gauges, and transition controls

The naturality audit fixes $r_1=1$ and enumerates $$(r_2,\ldots,r_K)\in(\mathbb Z/m\mathbb Z)^{K-1}
\tag{B.7}\label{B.7}$$ for $m=2,\ldots,8$ and $K=2,\ldots,6$. A table is operator-coefficient-clean only when every full-regular coefficient satisfies $$L_{a^{r_k}}=L_a^k,\qquad 1\le k\le K.
\tag{B.8}\label{B.8}$$ Character-clean counts are retained separately because a nonfaithful character can satisfy $\chi(a^{r_k})=\chi(a)^k$ without satisfying [\[B.8\]](#B.8){reference-type="eqref" reference="B.8"}. This convention accounts for 72,079 enumerated tables and the unique normalized power table in each of 35 cells.

For a vertex gauge $b$, the transition label has the form $$\alpha(i,j)=b(j)b(i)^{-1}
\tag{B.9}\label{B.9}$$ up to the fixed left/right convention. Products of [\[B.9\]](#B.9){reference-type="eqref" reference="B.9"} around closed words telescope. The gauge audit therefore checks both edge recovery and periodic identity. Negative controls retain an explicit shortest periodic witness.

The four transition countercontrols are not evidence for a clean extension. They test the boundary of the one-letter theorem by comparing an independently formed two-symbol transition determinant with its nearest atom-local baseline. The first nonzero coefficient of their difference is the leakage reported in [\[7.6\]](#7.6){reference-type="eqref" reference="7.6"}. Squarefree degrees and temporal powers are both retained, which is why the strict-symbol-change control is detected at $x^2y^2$.

## Adversarial inventories and evidence policy

The inventory control substitutes exact rational values into the same four formal determinant identities. Sixteen frozen seeds are used for each of four families. An inventory passes only if every identity is exact; numerical closeness is not a criterion. The pass-rate margin compares these Boolean outcomes across families and is zero.

All reported calculations are deterministic finite certificates. They have no training split, fitted parameter, uncertainty estimate, or statistical generalization claim. Riemann-zero tables, target spectra, target-derived phases, and fitted clocks are forbidden and were not used. The certificates support the implementation of proved finite identities; they do not provide evidence for RH, meromorphic continuation, or a Hilbert--Pólya operator.
