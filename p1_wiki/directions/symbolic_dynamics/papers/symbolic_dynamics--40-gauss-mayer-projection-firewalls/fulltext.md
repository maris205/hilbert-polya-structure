---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--40-gauss-mayer-projection-firewalls"
canonical_tex: "symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls/main.tex"
canonical_pdf: "symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls/main.pdf"
source_sha256: "b51729bc88ea550736260996cb01094c3de0d8d15ff4fea74a3f41094eb49faf"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Trace, Order-Discriminant, and Norm Firewalls for the Two-Digit Gauss--Mayer Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The two-digit Gauss--Mayer return has an intrinsic primitive-pair ledger, positive integer monodromies, a derivative clock, and a nuclear Fredholm determinant. We ask whether any of three canonical scalar projections---the matrix trace, the order discriminant, or the expanding norm---turns that full ledger into the rational-prime reciprocal Euler product without changing its objects, repetitions, marker, weights, or operator owner. For the precisely typed pair return, we prove an exact negative answer. The order discriminant factors as $(t-2)(t+2)$ and is prime only at the boundary value $5$; the norm $\lambda^2$ is irrational; trace and order discriminant fail the derivative clock and temporal powers; and three explicit collision classes expose duplicate primitive-pair species. Moreover, even the formal assignment $p=\lambda^2$ leaves the Mayer stability denominator, while none of the scalar selectors is a declared reducing sector of the frozen untwisted operator. In parallel, we derive the positive intrinsic pair expansion of $\det(I-u^2\mathcal L_s^2)$ directly from Fredholm traces, keeping pair, digit, and geodesic primitivity separate. Thus the modular pair ledger and same-space determinant remain valid, but the complete rational-prime interpretation is rejected for exactly the three stated projections. The result is a contract-relative theorem and audit closure, not a new transfer operator, zeta mechanism, or universal obstruction.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 17, 2026'
title: |
  Trace, Order-Discriminant, and Norm Firewalls\
  for the Two-Digit Gauss--Mayer Determinant
```

## Markdown 正文

# Introduction {#sec:introduction}

A Fredholm determinant may have a genuine primitive-orbit expansion and a genuine spectral interpretation without being the Euler product over rational primes. That distinction is easy to blur in symbolic models: a periodic word can carry an integer matrix, a scalar trace, a geodesic length, and a determinant factor, yet these data need not preserve the label, multiplicity, repetition, or weight convention of the target arithmetic ledger. The Gauss transfer operator is an especially sharp test case. Its thermodynamic formalism is classical [@Mayer1990Gauss], its modular Selberg-zeta identity is exact [@Mayer1991Selberg; @Mayer1990SelbergPreprint], and its continued-fraction coding is geometric [@Series1985Modular]. Those positive facts deserve to be retained, rather than weakened by an overextended rational-prime interpretation.

We study the even iterate $K_s=\mathcal{L}_s^2$ as a return on ordered digit pairs. The phrase "even iterate" refers only to two applications of the ordinary Gauss operator; it is not the distinct even-continued-fraction algorithm. The pair return has its own primitive necklaces and one original-digit marker $u$ per digit. For a pair word $w$, its ordered monodromy $M(w)$ has trace $t(w)$, order discriminant $\Delta_{\mathbb{Z}[M]}=t(w)^2-4$, expanding eigenvalue $\lambda(w)$, and derivative roof $T(w)=2\log\lambda(w)$. We freeze exactly three scalar projections, $$P_t(w)=t(w),\qquad
  P_\Delta(w)=t(w)^2-4,
  \qquad P_N(w)=\lambda(w)^2,$$ and ask whether any one of them yields the rational-prime reciprocal Euler ledger on the full, unchanged pair object.

The comparison is deliberately conjunctive. A successful projection must have rational-prime support, exactly one primitive source factor per target prime, correct temporal powers, the unchanged derivative clock and digit marker, the target sign, orientation and phase, the target orbit amplitude, and a declared operator sector owning the selected traces. Matching a single scalar is insufficient. In particular, deleting factors after a primality test does not by itself construct a reducing projector or a new Fredholm determinant.

Our contribution has three parts.

1.  We type the digit and pair systems separately and prove the exact grouping conjugacy, orbit-splitting law, branch--matrix bridge, raw transfer-index order, and derivative clock. Starting from the Fredholm trace series, we then derive the intrinsic primitive-pair product of $\det(I-u^2K_s)$ without importing an objectwise pair-to-geodesic correspondence.

2.  We prove a projection-by-projection firewall. The factorization $t^2-4=(t-2)(t+2)$ closes the order-discriminant label; a consecutive-square interval makes $\lambda^2$ irrational; Cayley--Hamilton closes temporal powers; and three exact collision classes close one-to-one multiplicity. The source stability denominator supplies an independent amplitude obstruction.

3.  We state the ownership conclusion at its correct strength: the frozen untwisted $K_s$ schema declares no reducing projector for any of the three scalar selections. Twists, extensions, direct sums, changed roofs, and changed spaces remain outside the theorem.

The qualitative trace/discriminant/norm mismatch and a much larger finite collision census predate this paper. Our claim is therefore not discovery of that mismatch or of the displayed collisions. The contribution is the theorem-grade closure of one pre-existing, exactly-three-projection audit: universal algebra where the quantifier is universal, explicit contract falsifiers where it is existential, and a typed ownership statement where the conclusion is schema-relative. Figure [\[fig:object-gate\]](#fig:object-gate){reference-type="ref" reference="fig:object-gate"} summarizes this separation between retained modular structure and rejected rational-prime credit.

The remainder is organized as follows. Section [2](#sec:related){reference-type="ref" reference="sec:related"} fixes the prior-art and claim boundaries. Section [3](#sec:source){reference-type="ref" reference="sec:source"} defines the typed source, marker, operator, and analytic domains. Section [4](#sec:firewall){reference-type="ref" reference="sec:firewall"} states the main theorem. Section [5](#sec:types){reference-type="ref" reference="sec:types"} treats primitivity and operator ownership. Section [6](#sec:audit){reference-type="ref" reference="sec:audit"} reserves the independently sealed finite audit, and Section [7](#sec:route){reference-type="ref" reference="sec:route"} gives the exact disposition and limitations. Detailed proofs and source/contract boundaries appear in Appendices [8](#app:proofs){reference-type="ref" reference="app:proofs"} and [9](#app:boundaries){reference-type="ref" reference="app:boundaries"}.

# Prior ownership and claim boundary {#sec:related}

#### Gauss and modular determinants.

Mayer's thermodynamic formalism for the Gauss map supplies the operator, holomorphic function space, nuclearity statement, and Fredholm determinant used here [@Mayer1990Gauss]. The modular identity $Z_{\mathrm{PSL}_2(\mathbb{Z})}(s)=\det(I-\mathcal{L}_s^2)$ is likewise prior work [@Mayer1991Selberg; @Mayer1990SelbergPreprint]. Our pair bookkeeping and free marker do not define a new two-variable zeta mechanism: two-variable Ruelle and Selberg families arising from Gauss/Farey dynamics are already developed by @BonannoIsola2014TwoVariable. We use $u$ only to count original Gauss digits and invoke modular Selberg semantics only at $u=1$.

#### Coding and primitive types.

The relation between continued fractions and the modular geodesic flow is classical [@Series1985Modular]; recent models refine this coding from a geometric viewpoint [@ArnouxSchmidt2026Elegant]. These sources do not license an untyped identification of every pair-primitive necklace with a digit-primitive necklace or a primitive geodesic class. We therefore keep the three types explicit throughout. We also distinguish the even iterate of the ordinary Gauss map from odd/even continued-fraction algorithms, whose coding is a separate subject [@BocaMerriman2017Coding].

#### Geodesic arithmetic, discriminants, and multiplicity.

Class numbers and primitive hyperbolic classes on the modular surface have a substantial arithmetic theory [@Sarnak1982ClassNumbers]. Prime-geodesic questions, including arithmetic progressions and periods of automorphic forms, concern primitive geodesics rather than the rational-prime Euler ledger [@ChatzakosHarcosKaneko2024; @ConstantinescuNordentoft2025]. The trace expression $t^2-4$ is specifically the discriminant of the order $\mathbb Z[M]$ (or the characteristic polynomial); it must not be conflated with a field fundamental discriminant or a larger multiplier-ring discriminant [@Maucourant2025Discriminants]. Trace and length multiplicities are also established phenomena [@Peter2002Multiplicity; @BelolipetskyEtAl2026Multiplicity]. Accordingly, our collision examples receive neither priority nor size-optimality credit.

#### Strict and twisted transfer operators.

Twisted Selberg zeta functions and their meromorphic continuation already have transfer-operator realizations [@FedosovaPohl2020Twists], while strict transfer-operator approaches can require accelerations and carefully chosen sections [@PohlWabnitz2026Strict]. Recent work on divisors of twisted Selberg zeta functions further rules out any universal claim that no operator sector can carry refined data [@DollPohl2026Divisor]. Our ownership theorem is narrower: no reducing projector for the three scalar postselections is declared in one frozen, untwisted $K_s$ schema.

#### Internal priority and candidate selection.

The qualitative projection mismatch and a large finite collision census were recorded before this manuscript, together with a request for the next trace/composite-discriminant audit. The current paper closes that request and does not rebrand it as a new mechanism. Candidate selection was also independent of the preceding paper: a literal six-card rule retained cards with a nonempty intrinsic primitive/repetition ledger and historical verdict `A2_ANALYTIC_DETERMINANT`. Three cards survived that first filter; the Gauss--Mayer parent then won the declared A3 followed by A4 comparison. The preceding paper supplies terminal-clean provenance only, not a ranking or authorization.

The resulting novelty posture is intentionally modest. The literature audit rates the work as a scoped synthesis and closure. We claim no new transfer operator, no new Selberg identity, no new two-variable zeta construction, no first multiplicity example, no primitive-pair/geodesic bijection, and no universal obstruction across twists or changed dynamical objects.

# Typed source object, marker, and determinant {#sec:source}

## Digit and pair returns

Let $$X=\mathbb{N}^{\mathbb{N}},\qquad
  \sigma(a_1,a_2,a_3,\ldots)=(a_2,a_3,a_4,\ldots)$$ be the digit space with its one-digit shift. Let $$\mathcal{X}_2=(\mathbb{N}^2)^{\mathbb{N}},\qquad
  \rho((a_1,a_2),(a_3,a_4),\ldots)
  =((a_3,a_4),(a_5,a_6),\ldots)$$ be the ordered-pair space with its one-pair shift. Grouping adjacent digits defines the bijection $$\iota(a_1,a_2,a_3,a_4,\ldots)
  =((a_1,a_2),(a_3,a_4),\ldots),$$ for which $$\rho\circ\iota=\iota\circ\sigma^2.
  \label{eq:grouping-conjugacy}$$ The typing matters: $\sigma^2$ acts on $X$, whereas $\rho$ acts on $\mathcal{X}_2$. A `RhoPrimitivePair` object is a finite cyclic word in the pair alphabet with least period under $\rho$, quotiented by pair rotation only. Digit reversal is metadata, not an additional quotient.

For $w=((a_1,a_2),\ldots,(a_{2k-1},a_{2k}))$, flatten in displayed pair order and set $$A(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix},
  \qquad
  M(w)=A(a_1)A(a_2)\cdots A(a_{2k}).
  \label{eq:monodromy}$$ Every digit matrix has determinant $-1$, so $M(w)\in\mathrm{SL}_2(\mathbb{Z})$. All entries are positive and $t(w)=\operatorname{tr}M(w)\ge3$. We write $$\Delta(w):=\Delta_{\mathbb{Z}[M]}(w)=t(w)^2-4,
  \quad
  \lambda(w)=\frac{t(w)+\sqrt{\Delta(w)}}2,
  \quad
  T(w)=2\log\lambda(w).
  \label{eq:labels-clock}$$ The free variable $u$ counts original Gauss digits. Thus one pair return carries $u^2$, and a pair word of length $k$ repeated $r$ times carries $u^{2kr}$.

## Gauss branches and raw operator order

For $\phi_a(z)=(a+z)^{-1}$, use $$B(a)=\begin{pmatrix}0&1\\1&a\end{pmatrix},
  \qquad J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.$$ Since $A(a)=JB(a)J$, the stored branch $\Phi_w=\phi_{a_1}\circ\cdots\circ\phi_{a_{2k}}$ is represented by $B(a_1)\cdots B(a_{2k})$, conjugate to $M(w)$. At its positive attracting fixed point $x_w$, $$d_w:=|\Phi_w'(x_w)|=\lambda(w)^{-2},
  \qquad -\log d_w=T(w).
  \label{eq:branch-clock}$$

The stored order is not the raw nesting order of the transfer operator. Writing $j_{a,s}(z)=(a+z)^{-2s}$ on Mayer's fixed holomorphic logarithm branch, $$\mathcal{L}_s(\mathcal{L}_sf)(z)
  =\sum_{a,b\ge1}j_{a,s}(z)j_{b,s}(\phi_a z)
    f(\phi_b\circ\phi_a z).$$ Hence raw indices must be globally reversed to recover stored composition order in $\mathcal{L}_s^{2k}$. The resulting complex weight is the nested product of the $j_{a,s}$ factors; only at the positive real fixed point is it written using the modulus in [\[eq:branch-clock\]](#eq:branch-clock){reference-type="eqref" reference="eq:branch-clock"}. Global reversal is a bijection on words and descends to cyclic pair classes, so it changes bookkeeping but not the primitive-pair inventory.

## Mayer space and three analytic domains

Let $$D=\{z\in\mathbb{C}:|z-1|<3/2\}$$ and let $A_\infty(D)$ denote the functions holomorphic on $D$ and continuous on $\overline D$, with the supremum norm. On this realization, $$(\mathcal{L}_sf)(z)=\sum_{n\ge1}(z+n)^{-2s}
  f\!\left((z+n)^{-1}\right)
  \label{eq:mayer-operator}$$ is nuclear of order zero for $\operatorname{Re}s>1/2$ [@Mayer1990Gauss; @Mayer1990SelbergPreprint]. Mayer's Proposition 3 gives the holomorphic Fredholm identity on the same half-plane, $$Z_{\mathrm{PSL}_2(\mathbb{Z})}(s)
  =\det(I-\mathcal{L}_s^2)
  =\det(I-\mathcal{L}_s)\det(I+\mathcal{L}_s).
  \label{eq:mayer-selberg}$$ The initial Selberg Euler product is absolutely convergent for $\operatorname{Re}s>1$, and the separately sourced meromorphic continuation extends to $\mathbb{C}$. These are three distinct statements: nuclear/Fredholm existence and the holomorphic identity, initial Euler-product convergence, and meromorphic continuation.

Set $K_s=\mathcal{L}_s^2$ and $$D_{42}(s,u)=\det(I-u^2K_s).
  \label{eq:marked-det}$$ For fixed $s$ in the nuclear half-plane, this is a same-space Fredholm family. The logarithmic trace series and primitive product below are understood coefficientwise/formally in $u^2$, or analytically for sufficiently small $|u|$ with the local logarithm at $u=0$. We neither continue that logarithm through determinant zeros nor import a Selberg interpretation for arbitrary $u$.

[\[prop:pair-fredholm\]]{#prop:pair-fredholm label="prop:pair-fredholm"} In the preceding domain and local/formal sense, $$\begin{aligned}
 -\log D_{42}(s,u)
 &=\sum_{n\ge1}\frac{u^{2n}}{n}\operatorname{Tr}(K_s^n) \\
 &=\sum_{[v]\ \rho\text{-primitive}}\sum_{r\ge1}
   \frac{u^{2k(v)r}d_v^{rs}}{r(1-d_v^r)},
 \label{eq:pair-trace-series}\end{aligned}$$ and consequently $$D_{42}(s,u)^{-1}
  =\prod_{[v]}\prod_{j\ge0}
    \left(1-u^{2k(v)}d_v^{s+j}\right)^{-1}.
  \label{eq:pair-product}$$ This ledger is typed to `RhoPrimitivePair` and asserts no objectwise correspondence with primitive geodesics.

The proof is given in Appendix [8.3](#app:fredholm-proof){reference-type="ref" reference="app:fredholm-proof"}. The object, marker, monodromy, branch, clock, and determinant ownership summarized above are displayed in Figure [\[fig:object-gate\]](#fig:object-gate){reference-type="ref" reference="fig:object-gate"}.

# The three-projection firewall {#sec:firewall}

## Exact comparison target

The positive trace-series comparison object is the reciprocal determinant $D_{42}(s,u)^{-1}$. For a primitive pair word $w$ of pair length $k$, its source repetition-$r$ coefficient in $-\log D_{42}$ is $$c_{w,r}^{\mathrm{src}}(s,u)
  =\frac{u^{2kr}d_w^{rs}}{r(1-d_w^r)}.
  \label{eq:source-coefficient}$$ Under a hypothetical one-to-one assignment $w_p\leftrightarrow p$ to rational primes, the marked target would be $$D_{\mathrm{prime}}(s,u)^{-1}
  =\prod_p\left(1-u^{2k(w_p)}p^{-s}\right)^{-1},
  \label{eq:prime-target}$$ whose repetition coefficient is $$c_{p,r}^{\mathrm{tar}}(s,u)
  =\frac{u^{2k(w_p)r}p^{-rs}}{r}.
  \label{eq:target-coefficient}$$ At $u=1$, [\[eq:prime-target\]](#eq:prime-target){reference-type="eqref" reference="eq:prime-target"} is the ordinary reciprocal Euler product for the Riemann zeta function. The exponent $2k(w_p)r$ is inherited from the source digit marker; it is not replaced by $r$ after comparison.

For $P\in\{P_t,P_\Delta,P_N\}$, let $\mathrm{ProjectionGO}(P)$ mean the conjunction, on the full intrinsic primitive-pair ledger, of:

-   rational-integer and rational-prime support, with infinitely many labels and no composite source species;

-   exactly one primitive source factor for each target prime;

-   target powers under every temporal repetition;

-   unchanged derivative clock and original digit marker;

-   equality of [\[eq:source-coefficient\]](#eq:source-coefficient){reference-type="eqref" reference="eq:source-coefficient"} and [\[eq:target-coefficient\]](#eq:target-coefficient){reference-type="eqref" reference="eq:target-coefficient"}, including sign, orientation, phase, and logarithmic-derivative amplitude;

-   a declared invariant or reducing operator sector owning the selected traces, multiplicities, and marker degrees; and

-   separation from the mandatory arithmetic and dynamical controls.

Thus the rational-prime projection claim is the existential statement $\bigvee_P\mathrm{ProjectionGO}(P)$. It is not enough for one theorem clause to fail one projection; every projection conjunction must be covered.

## Main theorem

[\[thm:main\]]{#thm:main label="thm:main"} Let $w$ range over cyclic primitive words for the pair shift $\rho$, with monodromy [\[eq:monodromy\]](#eq:monodromy){reference-type="eqref" reference="eq:monodromy"}, and let the source operator and domain be those of Section [3](#sec:source){reference-type="ref" reference="sec:source"}. Then:

1.  the pair return, primitive-pair ledger, monodromy, Gauss branch, derivative roof, digit marker, raw $K_s^k$ summand, and Fredholm determinant are one typed source construction;

2.  $P_t$, $P_\Delta$, and $P_N$ are the complete frozen projection family, and no member satisfies $\mathrm{ProjectionGO}$;

3.  no integer-valued member simultaneously preserves the exact source clock and temporal powers;

4.  the frozen untwisted operator schema declares no reducing owner for any rational-prime scalar postselection.

The theorem is relative to these three maps and this operator schema. It does not assert universal nonexistence across twists or changed objects, an objectwise pair/geodesic equivalence, or novelty of any collision witness.

The positive construction in item 1 follows from Proposition [\[prop:pair-fredholm\]](#prop:pair-fredholm){reference-type="ref" reference="prop:pair-fredholm"} and the branch--matrix bridge; the full derivation is in Appendices [8.2](#app:branch-proof){reference-type="ref" reference="app:branch-proof"} and [8.3](#app:fredholm-proof){reference-type="ref" reference="app:fredholm-proof"}. The projection coverage is summarized below.

For every source word, $t\ge3$ and $$\Delta=t^2-4=(t-2)(t+2).
  \label{eq:delta-factorization}$$ At $t=3$ this is $5$; for $t>3$ both factors exceed one. Moreover, $$(t-1)^2<\Delta<t^2,
  \label{eq:square-interval}$$ so $\Delta$ is nonsquare. The reciprocal numbers $P_N=\lambda^2>1$ and $d=\lambda^{-2}\in(0,1)$ are the two roots of $$x^2-(t^2-2)x+1=0.
  \label{eq:norm-polynomial}$$ Its discriminant $t^2\Delta$ is nonsquare, proving $P_N\notin\mathbb Q$.

Equation [\[eq:square-interval\]](#eq:square-interval){reference-type="eqref" reference="eq:square-interval"} also gives $\lambda>t-1$, hence $P_N=\lambda^2>t$ for $t\ge3$. Therefore $T=\log P_N>\log P_t$. Every integer $t\ge3$ is realized by $$w_t=((1,t-2)),\qquad
  M(w_t)=\begin{pmatrix}t-1&1\\t-2&1\end{pmatrix}.
  \label{eq:trace-family}$$ Since $\log\lambda(t)^2/\log t\to2$ but $\lambda(t)^2<t^2$ at every finite $t$, no constant rescales $\log t$ to the source clock on all realized traces.

Cayley--Hamilton gives, for $q_r=\operatorname{tr}(M^r)$, $$q_0=2,\quad q_1=t,\quad q_r=tq_{r-1}-q_{r-2}.
  \label{eq:trace-recurrence}$$ Thus $q_2=t^2-2\ne t^2$, and $\Delta(M^2)=t^2\Delta(M)\ne\Delta(M)^2$. In contrast, $P_N(w^r)=P_N(w)^r$ and $T(w)=\log P_N(w)$ exactly. The norm therefore passes powers and clock but fails integer support. Finally, all three maps are functions of $t$ and collide on the explicit species below, while [\[eq:source-coefficient\]](#eq:source-coefficient){reference-type="eqref" reference="eq:source-coefficient"} retains the stability factor $(1-d_w^r)^{-1}$ even under the formal assignment $p=d_w^{-1}$. The operator-owner conclusion is proved in Section [5.2](#sec:ownership){reference-type="ref" reference="sec:ownership"}. These facts make each of the three complete conjunctions false. Detailed algebra appears in Appendix [8.4](#app:algebra-proof){reference-type="ref" reference="app:algebra-proof"}.

## Explicit in-domain collision classes

The six matrices in Table [\[tab:collisions\]](#tab:collisions){reference-type="ref" reference="tab:collisions"} are computed in the stored left-to-right digit convention. One-pair words are pair-primitive; the two-pair trace-$10$ word is not a proper pair power. Because reversal is not part of the object quotient, the trace-$4$ reversal phases are distinct primitive factors. The trace-$6$ and trace-$10$ pairs are not reversal-related, and the last pair also crosses pair length.

\@lY Y c c@ Class & First word and matrix & Second word and matrix & $t$ & $\Delta$\
Reversal phase & $((1,2))$, $\left(\begin{smallmatrix}3&1\\2&1\end{smallmatrix}\right)$ & $((2,1))$, $\left(\begin{smallmatrix}3&2\\1&1\end{smallmatrix}\right)$ & $4$ & $12$\
One-pair non-reversal & $((1,4))$, $\left(\begin{smallmatrix}5&1\\4&1\end{smallmatrix}\right)$ & $((2,2))$, $\left(\begin{smallmatrix}5&2\\2&1\end{smallmatrix}\right)$ & $6$ & $32$\
Cross-length non-reversal & $((2,4))$, $\left(\begin{smallmatrix}9&2\\4&1\end{smallmatrix}\right)$ & $((1,1),(1,2))$, $\left(\begin{smallmatrix}8&3\\5&2\end{smallmatrix}\right)$ & $10$ & $96$\

The first word in Table [\[tab:collisions\]](#tab:collisions){reference-type="ref" reference="tab:collisions"} also shows that the full pair ledger contains a composite trace species. Hence the untwisted full determinant cannot equal a trace-prime selected product. Figure [\[fig:algebra\]](#fig:algebra){reference-type="ref" reference="fig:algebra"} collects the universal and existential dependencies without turning a finite census into a universal proof.

# Primitivity and ownership firewalls {#sec:types}

## Three primitive types and the exact split

The digit, pair, and geodesic primitive objects are:

1.  `SigmaPrimitiveDigit`: a cyclic digit word of least period under $\sigma$;

2.  `RhoPrimitivePair`: a cyclic ordered-pair word of least period under $\rho$, modulo pair rotation only;

3.  `GeodesicPrimitiveClass`: a primitive hyperbolic/geodesic conjugacy class.

Equation [\[eq:grouping-conjugacy\]](#eq:grouping-conjugacy){reference-type="eqref" reference="eq:grouping-conjugacy"} relates the first two dynamical systems, but it does not identify their primitive classes object by object. Nor does the function identity [\[eq:mayer-selberg\]](#eq:mayer-selberg){reference-type="eqref" reference="eq:mayer-selberg"} provide a bridge to the third type.

[\[prop:splitting\]]{#prop:splitting label="prop:splitting"} If a $\sigma$ orbit has least period $n$, then its restriction to $\sigma^2$ has $\gcd(n,2)$ cycles, each of length $n/\gcd(n,2)$. Consequently odd periods remain one cycle and even periods split into two. If $N_D(n)$ counts primitive digit necklaces over a $D$-digit alphabet and $N_{D^2}(k)$ counts primitive ordered-pair necklaces, then $$N_{D^2}(k)=2N_D(2k)+\mathbf1_{k\ \mathrm{odd}}N_D(k).
  \label{eq:splitting-law}$$

Index a least-period-$n$ orbit by $\mathbb Z/n\mathbb Z$. The map $\sigma^2$ adds $2$, whose generated subgroup has index $\gcd(n,2)$ and orbits of length $n/\gcd(n,2)$. A pair cycle of length $k$ therefore arises twice from a digit cycle of length $2k$, or once from a digit cycle of length $k$ when $k$ is odd. Summing primitive cyclic classes gives [\[eq:splitting-law\]](#eq:splitting-law){reference-type="eqref" reference="eq:splitting-law"}.

For example, $((1,2))$ and $((2,1))$ are the two $\rho$ phases of one $\sigma$-period-two orbit. Conversely, $((2,2))$ is pair-primitive through the odd-period contribution although its flattened digit word is $\sigma$-imprimitive. These examples demonstrate why pair A1 credit must be proved on the pair object rather than inherited from the digit ledger.

## Owner required for scalar postselection {#sec:ownership}

The full pair ledger is owned by $K_s$ through Proposition [\[prop:pair-fredholm\]](#prop:pair-fredholm){reference-type="ref" reference="prop:pair-fredholm"}. A scalar predicate on its primitive rows is a different kind of object. In the frozen schema, a selected-owner claim requires a declared operator $K$, projector $P$, common space, multiplicities, and marker stride, together with $$P^2=P,\qquad PK=KP,\qquad
  \operatorname{Tr}(PK^r)
  =\operatorname{Tr}\!\left((K|_{\operatorname{ran}P})^r\right)
  \label{eq:owner-predicate}$$ at every declared repetition. Marker degrees and multiplicities must agree as well. The three scalar projections provide no such $P$; the schema's selected projector is undeclared. This proves absence of a declared owner, not nonexistence across all possible twists or extensions.

The ownership ledger is therefore:

\@lY Y@ Entity & Marker/repetition & Status\
Digit space $(X,\sigma)$ & one digit carries $u$ & inherited Gauss source\
Pair space $(\mathcal{X}_2,\rho)$ & one pair carries $u^2$ & typed return object\
`RhoPrimitivePair` & $u^{2kr}$ at repetition $r$ & complete intrinsic ledger\
$K_s=\mathcal{L}_s^2$ & raw indices globally reversed into stored order & same-object owner\
$D_{42}(s,u)$ & coefficient [\[eq:source-coefficient\]](#eq:source-coefficient){reference-type="eqref" reference="eq:source-coefficient"} & Fredholm family in nuclear domain\
$P_t,P_\Delta,P_N$ & scalar row labels & no declared selected owner\
Rational-prime target & coefficient [\[eq:target-coefficient\]](#eq:target-coefficient){reference-type="eqref" reference="eq:target-coefficient"} & comparison target only\

## Sharp scope controls

Five countermodels prevent the scoped STOP from becoming a universal slogan. An odd one-digit word has determinant $-1$ and lies outside the even-word $\mathrm{SL}_2(\mathbb{Z})$ domain. A prime-indexed diagonal operator has an honest finite determinant but changes the source object. A changed roof or marker is a new contract. A scalar-prime subproduct is a valid filter but has no declared projector in this schema. Finally, a finite directed cycle has a genuine primitive-cycle determinant but is not the Mayer operator. The exact fixtures are recorded in Appendix [9.2](#app:countermodels){reference-type="ref" reference="app:countermodels"}.

Figure [\[fig:type-owner\]](#fig:type-owner){reference-type="ref" reference="fig:type-owner"} combines the type, source-domain, and ownership boundaries. In particular, the two analytic half-planes are not two versions of the same claim: $\operatorname{Re}s>1/2$ supports nuclearity and the holomorphic Fredholm identity, whereas $\operatorname{Re}s>1$ is the initial Euler-product domain.

# Exact bounded audit {#sec:audit}

The theorem is algebraic and source-bound; finite computation is used only to check exact fixtures, bounded enumeration, control schemas, and reproducibility. The locked audit design independently reconstructs the return-map typing, pair primitivity and splitting, ordered monodromies, branch values and nested transfer weights, projection truth records, orientation metadata, source amplitudes, and operator-owner predicates. Its negative mutations alter raw inputs rather than merely flipping reported booleans. Relocation checks ensure that the emitted records do not depend on an installation path.

No finite run is interpreted as an evaluation of the infinite Fredholm determinant, a proof of nuclearity or continuation, a novelty search, or a replacement for the all-orders arguments in Appendix [8](#app:proofs){reference-type="ref" reference="app:proofs"}. Likewise, a finite collision census corroborates displayed species but does not prove the universal projection theorem.

This block is the designated integrator's sole canonical quantitative statement. It verifies the bounded checker, mutation, packaging, and reproducibility contract. The scientific conclusion of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} rests on the displayed proofs and is not inferred from finite enumeration.

# Route disposition, limitations, and conclusion {#sec:route}

The pair system earns genuine positive credit. The typed $\rho$ ledger is complete for its own primitive objects, and the same-space even iterate owns its Fredholm determinant. These facts give the two narrow GO statements

GO\_MODULAR\_PRIMITIVE\_LEDGER\
GO\_SAME\_OBJECT\_MAYER\_DETERMINANT.

They carry no rational-prime, digit-primitive, or geodesic-primitive credit.

For the rational-prime branch, the exact Route-A coordinates are $$\begin{aligned}
(&\texttt{A0\_WEAK\_ARITHMETIC\_RELATION},
\ \texttt{A1\_PASS\_ANALYTIC},\\
 &\texttt{A2\_ANALYTIC\_DETERMINANT},
\ \texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\ \texttt{A4\_FORMAL\_HINT}).
\end{aligned}$$ The terminal codes are

STOP\_CANONICAL\_INTEGER\_PROJECTION\
STOP\_RATIONAL\_INTEGER\_CLOCK\_REPETITION\_CONJUNCTION\
STOP\_OPERATOR\_VISIBLE\_SELECTOR\_NOT\_OWNED\
ROUTE\_A\_REJECTED,

with Route B locked.

The second STOP has a deliberately narrow quantifier. Trace and order discriminant are integer-valued but fail both the derivative clock and temporal powers. The norm passes clock and powers exactly but is irrational. Thus no integer-valued projection lies in the intersection of the clock and power columns; we do not claim that every projection separately fails those columns. The first STOP is stronger in a different direction: the complete rational-prime conjunction is false for every one of the three projections.

Several limitations are structural. The theorem fixes one pair return, one digit marker, one derivative roof, one Mayer space, one untwisted operator, and exactly three scalar maps. It neither excludes a newly constructed operator-visible sector nor evaluates a twist. The order discriminant is not a field fundamental discriminant. The modular Selberg identity is not a primitive-pair/geodesic bijection, still less a rational-prime dictionary. The local marked Fredholm logarithm is not asserted across determinant zeros or at arbitrary $u$; the $u=1$ identity is sourced separately. Finally, the explicit collisions are evidence for this contract and not claims of first discovery.

Within those boundaries, the conclusion is sharp. An honest primitive-orbit determinant survives, but scalar arithmetic shadows do not inherit its object, clock, amplitude, or operator ownership. Reopening the rational-prime branch therefore requires a new, separately locked operator-visible invariant that does not factor through $t$, $t^2-4$, or $\lambda^2$, together with a proof that it preserves the full target ledger rather than one label at a time.

# Full algebra and source-object proofs {#app:proofs}

## Return map, repetition, and splitting {#app:return-proof}

For $a=(a_1,a_2,a_3,\ldots)\in X$, $$(\rho\circ\iota)(a)
  =((a_3,a_4),(a_5,a_6),\ldots)
  =(\iota\circ\sigma^2)(a),$$ which proves [\[eq:grouping-conjugacy\]](#eq:grouping-conjugacy){reference-type="eqref" reference="eq:grouping-conjugacy"}. Concatenating a stored pair word $r$ times gives $$M(w^r)=M(w)^r.
  \label{eq:matrix-repetition}$$ Since $M(w)$ has determinant one and positive entries, its eigenvalues are $\lambda$ and $\lambda^{-1}$ with $\lambda>1$. Equation [\[eq:matrix-repetition\]](#eq:matrix-repetition){reference-type="eqref" reference="eq:matrix-repetition"} therefore gives $\lambda(w^r)=\lambda(w)^r$ and $$T(w^r)=rT(w).
  \label{eq:roof-repetition}$$

For completeness, Proposition [\[prop:splitting\]](#prop:splitting){reference-type="ref" reference="prop:splitting"} follows directly on a single periodic orbit. Label its points by $\mathbb Z/n\mathbb Z$. The one-digit shift adds $1$ and its square adds $2$. The subgroup generated by $2$ has index $\gcd(n,2)$, which proves both the number and length of the cycles. Passing through $\iota$ turns those $\sigma^2$ cycles into $\rho$ cycles. A pair cycle of length $k$ thus comes either from a digit cycle of length $2k$, in two phases, or from a digit cycle of length $k$ when $k$ is odd, in one phase. This is exactly [\[eq:splitting-law\]](#eq:splitting-law){reference-type="eqref" reference="eq:splitting-law"}.

Digit reversal of $w=((a_1,a_2),\ldots,(a_{2k-1},a_{2k}))$ is the metadata map $$R(w)=((a_{2k},a_{2k-1}),\ldots,(a_2,a_1)).$$ If $\tau$ is pair rotation, global digit reversal intertwines $\tau$ with $\tau^{-1}$. It therefore descends to cyclic pair classes and preserves least pair period, but it does not identify a class with its reverse.

## Branch--matrix bridge and raw transfer order {#app:branch-proof}

Direct multiplication gives $A(a)=JB(a)J$. The intermediate $J$ factors cancel in an even product, so $$M(w)=J B(a_1)\cdots B(a_{2k})J.
  \label{eq:ABJ}$$ Under the column-vector Möbius convention, $B_w=B(a_1)\cdots B(a_{2k})=
\left(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\right)$ represents $\Phi_w$. Its positive fixed point satisfies $$\gamma x^2+(\delta-\alpha)x-\beta=0.$$ The vector $(x,1)^{\mathsf T}$ is an eigenvector of $B_w$, with eigenvalue $\gamma x+\delta$. Conjugacy in [\[eq:ABJ\]](#eq:ABJ){reference-type="eqref" reference="eq:ABJ"} and positivity identify this eigenvalue with $\lambda_+(M(w))$. Because $\det B_w=1$, $$|\Phi_w'(x)|=(\gamma x+\delta)^{-2}=\lambda_+(M(w))^{-2},$$ which proves [\[eq:branch-clock\]](#eq:branch-clock){reference-type="eqref" reference="eq:branch-clock"}. Repeating the word raises $B_w$ and $M(w)$ to the $r$th power, so the branch and matrix repetition conventions agree.

Now expand $\mathcal{L}_s^{m}$ directly. For raw indices $(r_1,\ldots,r_m)$, let $x_0=z$ and $x_i=\phi_{r_i}(x_{i-1})$. The nested transfer summand has weight $$\prod_{i=1}^{m}j_{r_i,s}(x_{i-1})
  \label{eq:raw-weight}$$ and final branch $\phi_{r_m}\circ\cdots\circ\phi_{r_1}(z)$. Therefore the stored word $(a_1,\ldots,a_m)$ is obtained from raw indices $(a_m,\ldots,a_1)$. Substitution into [\[eq:raw-weight\]](#eq:raw-weight){reference-type="eqref" reference="eq:raw-weight"} gives precisely the fixed-branch holomorphic derivative weight of $\Phi_w=\phi_{a_1}\circ\cdots\circ\phi_{a_m}$.

The nonpalindromic fixture $$w=(1,2,2,3,1,4),\qquad z=\frac14$$ detects any silent reversal error. The stored matrix is $$B_w=\begin{pmatrix}22&105\\31&148\end{pmatrix},$$ so at $s=1$ $$\Phi_w(1/4)=\frac{442}{623},
  \qquad G_{w,1}(1/4)=\frac{16}{388129}.$$ Using the stored digits as raw indices instead gives the reversed-word matrix $$\begin{pmatrix}22&31\\105&148\end{pmatrix},$$ and the different values $146/697$ and $16/485809$. The equal traces of the two matrices explain why the branch value and nested weight, not trace alone, must check the operator order.

## Fredholm trace regrouping {#app:fredholm-proof}

Fix $s$ in Mayer's nuclear half-plane. Nuclear Fredholm theory gives, as a formal series in $u^2$ and analytically for sufficiently small $|u|$, $$-\log\det(I-u^2K_s)
  =\sum_{n\ge1}\frac{u^{2n}}{n}\operatorname{Tr}(K_s^n).
  \label{eq:fredholm-log-proof}$$ The logarithm is the local branch at $u=0$. By Appendix [8.2](#app:branch-proof){reference-type="ref" reference="app:branch-proof"}, raw-index reversal bijectively writes every summand of $K_s^n$ in stored pair-composition order and respects cyclic classes and repetition.

For one stored pair word $w$, the one-dimensional holomorphic weighted-composition trace is $$\frac{d_w^s}{1-d_w},
  \label{eq:composition-trace}$$ where $d_w=|\Phi_w'(x_w)|$ is the positive fixed-point multiplier. The complex weight before evaluation uses Mayer's fixed holomorphic logarithm branch, not a nonholomorphic modulus.

Write a length-$n$ word as $v^r$, where $v$ is a primitive pair necklace of length $k$ and $n=kr$. Its multiplier is $d_v^r$. The primitive necklace $v$ has $k$ cyclic representatives in the word trace, so its contribution to [\[eq:fredholm-log-proof\]](#eq:fredholm-log-proof){reference-type="eqref" reference="eq:fredholm-log-proof"} is $$\frac{k}{kr}u^{2kr}\frac{d_v^{rs}}{1-d_v^r}
  =\frac{u^{2kr}d_v^{rs}}{r(1-d_v^r)}.$$ Summing proves [\[eq:pair-trace-series\]](#eq:pair-trace-series){reference-type="eqref" reference="eq:pair-trace-series"}. Expanding $(1-d_v^r)^{-1}=\sum_{j\ge0}d_v^{jr}$ and exponentiating in the same local/formal sense gives [\[eq:pair-product\]](#eq:pair-product){reference-type="eqref" reference="eq:pair-product"}. This argument neither asserts convergence of that primitive product at arbitrary $u$ nor continues a single-valued logarithm through zeros. At $u=1$, the modular identity is invoked only through Mayer's separate theorem.

## Label, clock, and repetition algebra {#app:algebra-proof}

The order-discriminant claim follows from [\[eq:delta-factorization\]](#eq:delta-factorization){reference-type="eqref" reference="eq:delta-factorization"}. If $t=3$, the value is $5$. If $t>3$, both integer factors $t-2$ and $t+2$ exceed one, so the value is composite. For $t\ge3$, $$t^2-4-(t-1)^2=2t-5>0,$$ which proves [\[eq:square-interval\]](#eq:square-interval){reference-type="eqref" reference="eq:square-interval"}. Thus $\Delta$ is strictly between consecutive squares and is nonsquare. Squaring $\lambda+\lambda^{-1}=t$ gives $\lambda^2+\lambda^{-2}=t^2-2$, hence [\[eq:norm-polynomial\]](#eq:norm-polynomial){reference-type="eqref" reference="eq:norm-polynomial"}. Its discriminant is $t^2\Delta$, also nonsquare, so $\lambda^2$ is irrational.

The stronger clock inequality follows from $t^2-4>(t-2)^2$, which is equivalent to $4t-8>0$. Hence $$\lambda=\frac{t+\sqrt{t^2-4}}2>t-1,
  \qquad \lambda^2>(t-1)^2\ge t.$$ To rule out a constant rescaling on the realized source rather than on an abstract trace variable, use [\[eq:trace-family\]](#eq:trace-family){reference-type="eqref" reference="eq:trace-family"}. As $t\to\infty$, $\lambda=t+O(t^{-1})$, so $\log\lambda^2/\log t\to2$. Any global constant would be $2$. But $\sqrt{t^2-4}<t$ gives $\lambda<t$ for every finite $t$, and hence $\lambda^2<t^2$, a contradiction.

Cayley--Hamilton gives $M^2-tM+I=0$. Multiplying by $M^{r-2}$ and taking traces proves [\[eq:trace-recurrence\]](#eq:trace-recurrence){reference-type="eqref" reference="eq:trace-recurrence"}. At $r=2$, $q_2=t^2-2$, so trace does not preserve target powers. Moreover, $$\Delta(M^2)=q_2^2-4=(t^2-2)^2-4=t^2(t^2-4)=t^2\Delta(M),$$ which differs from $\Delta(M)^2$. Norm and clock do preserve repetition by [\[eq:matrix-repetition\]](#eq:matrix-repetition){reference-type="eqref" reference="eq:matrix-repetition"}--[\[eq:roof-repetition\]](#eq:roof-repetition){reference-type="eqref" reference="eq:roof-repetition"}, but the norm is irrational.

Finally, [\[eq:pair-product\]](#eq:pair-product){reference-type="eqref" reference="eq:pair-product"} gives one primitive source factor $$\prod_{j\ge0}(1-u^{2k}d_w^{s+j})^{-1}.$$ Its repetition-$r$ logarithmic coefficient is [\[eq:source-coefficient\]](#eq:source-coefficient){reference-type="eqref" reference="eq:source-coefficient"}. The rational-prime target coefficient [\[eq:target-coefficient\]](#eq:target-coefficient){reference-type="eqref" reference="eq:target-coefficient"} lacks $(1-d_w^r)^{-1}$. Setting $p=d_w^{-1}=\lambda^2$ matches the exponential base formally but not the stability amplitude or the associated tower.

## Collision and ownership closure {#app:collision-proof}

Multiplying the matrices in the displayed order gives exactly the six entries of Table [\[tab:collisions\]](#tab:collisions){reference-type="ref" reference="tab:collisions"}. A one-pair word cannot be a proper pair power. The two-pair word $((1,1),(1,2))$ has unequal pair symbols and is likewise not a proper pair power. The reversal metadata map exchanges $((1,2))$ and $((2,1))$ but neither pair rotation nor primitivity identifies them. The trace-$6$ and trace-$10$ pairs are not reversals, and the latter has different pair lengths. Since both $P_\Delta$ and $P_N$ are functions of $t$, common trace implies collision under every frozen projection.

For ownership, the accepted schema predicate is [\[eq:owner-predicate\]](#eq:owner-predicate){reference-type="eqref" reference="eq:owner-predicate"} together with common dimension, multiplicity, and marker support. The full $K_s$ ledger has an owner by Proposition [\[prop:pair-fredholm\]](#prop:pair-fredholm){reference-type="ref" reference="prop:pair-fredholm"}. None of the three scalar records declares a projector, so none satisfies the selected-owner predicate. This is sufficient for the contract-relative ownership STOP and does not imply universal nonexistence.

# Source, scope, and reproducibility boundaries {#app:boundaries}

## Analytic-domain ledger

Table [\[tab:domains\]](#tab:domains){reference-type="ref" reference="tab:domains"} records the three source-supported analytic claims. The first two share the inequality $\operatorname{Re}s>1/2$ but have distinct content; the Euler product begins in the narrower half-plane. No finite digit cutoff is used to strengthen any row.

\@l l Y@ Claim & Domain & Limitation\
Nuclearity/order zero and Fredholm existence on $A_\infty(D)$ & $\operatorname{Re}s>1/2$ & fixed Mayer realization\
Holomorphic identity $Z_{\mathrm{PSL}_2(\mathbb{Z})}(s)=\det(I-\mathcal{L}_s^2)$ & $\operatorname{Re}s>1/2$ & functional equality, not orbitwise bijection\
Initial absolute convergence of the Selberg Euler product & $\operatorname{Re}s>1$ & narrower initial product domain\
Meromorphic continuation & $s\in\mathbb{C}$ & only the source-qualified continuation and singular set\
Marked Fredholm logarithm/product & formal in $u^2$ or small $|u|$ & local at $u=0$; no arbitrary-$u$ Selberg semantics\

The order-discriminant notation has an equally strict boundary: $\Delta_{\mathbb{Z}[M]}=t^2-4$ is the discriminant of the characteristic order. No claim about field fundamental discriminants or a larger multiplier ring is deduced from it.

## Countermodel ledger {#app:countermodels}

The exact scope controls in Table [\[tab:countermodels\]](#tab:countermodels){reference-type="ref" reference="tab:countermodels"} demonstrate that a broader universal statement would be false or ill-typed.

\@lY Y@ Control & Exact fact & Why outside the theorem\
Odd word & $A(3)=\left(\begin{smallmatrix}3&1\\1&0\end{smallmatrix}\right)$ has determinant $-1$ and discriminant $13$ & not an even pair return in $\mathrm{SL}_2(\mathbb{Z})$\
Prime direct sum & $\det(I-u\operatorname{diag}(2,3,5))=(1-2u)(1-3u)(1-5u)$ & changed object, marker, roof, and function space\
Roof/marker mutation & changing either field changes exactly one contract coordinate & a repair is a new contract, not scalar relabeling\
Selected subproduct & primality filters $\{3,4\}$ to $\{3\}$ & no reducing projector is declared\
Finite cycle & for the three-cycle matrix $C$, $\det(I-uC)=1-u^3$ & genuine finite determinant, but not the Mayer operator\

## Selection and chronology

The candidate rule was fixed at the field level: a historical card had to contain a nonempty intrinsic primitive/repetition ledger and the exact proved verdict `A2_ANALYTIC_DETERMINANT`; subsequent comparison used the declared A3 and then A4 coordinates. This rule retained the one-orbit candidate rather than adding a post-hoc nontriviality filter. The Gauss--Mayer card was selected independently, and terminal status of the preceding paper served only as a promotion gate.

The correction chronology is retrospective. An initial package and several in-flight corrective smoke outputs were known while the selection parser, controls, witnesses, typing, operator order, analytic domains, and exact comparison predicate were repaired. Only one exact corrected input set preceded the canonical replacement execution. The proof, Route, literature, and package renderings followed that run, and a later whitespace-only normalization changed no scientific claim or canonical output. No stage of this correction history earns novelty or priority credit.

## Lock roles

The authority research lock enumerates eleven immutable source, proof, ownership, type, Route, literature, selection, and counterexample files. It deliberately excludes executable code, result artifacts, experiment and evaluation directories, manuscript files, figures, compilation outputs, and writer metadata. The pre-execution control lock is narrower still: it binds only the corrected scientific inputs, source cards, code, tests, seeds, and fixtures that preceded the canonical replacement run. Post-run proof and literature files are never relabeled as pre-execution inputs.

The manuscript consumes the immutable research bytes and the designated integrator's single `FINAL / POST-OUTPUT CLEAN` statement without modifying integration-owned artifacts. That statement binds the scientific projection to `340aff6f08e7cf9360d57d34ff9c66e99f9322343b3069fe37e5acc2f55aa7c5`, the 83/83-check integrity audit to `61ff8805dd5bcc44dec3ea8a960786ccb72f211bf7c8d30d013eb749a536110c`, and the 102/102-entry results ledger to `ddcda6a450c662be8432f14510569a4097f6f3909ea17a68f499d21e47edeb31`. Section [6](#sec:audit){reference-type="ref" reference="sec:audit"} is the sole manuscript result block; this appendix records provenance only. The separation prevents a writer-side summary from becoming a second, inconsistent source of result truth.
