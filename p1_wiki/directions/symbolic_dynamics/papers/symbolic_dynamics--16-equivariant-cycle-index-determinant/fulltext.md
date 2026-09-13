---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--16-equivariant-cycle-index-determinant"
canonical_tex: "symbolic_dynamics/papers/16-equivariant-cycle-index-determinant/main.tex"
canonical_pdf: "symbolic_dynamics/papers/16-equivariant-cycle-index-determinant/main.pdf"
source_sha256: "fbdc3229673beb7d5e53a62831ea8f45894baddea8f87375965523bc15ed3628"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Character-Resolved Cycle-Index Determinants of the Tensor-Atom Shift: A Formal Burnside Lift and an Arithmetic Fredholm No-Go

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/16-equivariant-cycle-index-determinant>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/16-equivariant-cycle-index-determinant/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/16-equivariant-cycle-index-determinant/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/16-equivariant-cycle-index-determinant/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/16-equivariant-cycle-index-determinant/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The scalar Koszul-subset shift has determinant $\prod_p(1-x_p)$, yet its mixed primitive cycles cancel only after scalar dimension. We retain the lost label symmetry in a $C_2$-colored Burnside/species cycle ledger and calculate its smallest nonzero residual. At squarefree content $pqr$, the virtual Burnside class is $[S_3/S_3]+[S_3/C_3]-[S_3/C_2]$, with subgroup marks $(0,0,3,1)$; its permutation representation is $\mathbf 1\oplus\mathbf{sgn}-\mathbf{Std}$ with character $(0,0,3)$. Adams powers cannot remove this squarefree class. We then prove a scoped incompatibility theorem for the canonical rank-one and diagonal realizations. Distinct arithmetic weights $x_p=p^{-s}$ make atom relabeling semilinearly covariant rather than a symmetry of one fixed operator. Equal weights restore symmetry but leave only the trivial rank-one image. The diagonal subset operator retains representation lines, yet replaces the scalar ghosts $b(x)^r$ by $b(x^r)$ and has mixed superdeterminant $\prod_{S\ne\varnothing}(1-x_S)^{(-1)^{|S|+1}}$. Its prime-subset specialization belongs to $\mathcal S_q$ exactly when $q\operatorname{Re}s>1$, but this analytic determinant remains the mixed product. Any linear readout detecting the isolated $pqr$ residual inserts a mixed primitive trace-log term absent from the pure Euler ledger. Thus the formal equivariant lift survives, while arithmetic character-Fredholm fibers stop for the canonical models studied here. The resolved Route-A tuple is $(\text{A0 analytic},\text{A1 weak},\text{A2 fail},\text{A3 fail},
  \text{A4 fail})$; Route B remains locked.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Character-Resolved Cycle-Index Determinants of the Tensor-Atom Shift:\
  A Formal Burnside Lift and an Arithmetic Fredholm No-Go
```

## Markdown 正文

# Introduction {#sec:introduction}

Scalar cancellation need not be natural cancellation. A signed collection of primitive symbolic cycles may have total weight zero while retaining a nonzero permutation character, a nontrivial mark at a subgroup, or an incompatible temporal-power ledger. Arithmetic symbolic dynamics cannot discard those distinctions: a proposed prime/prime-power orbit model must carry primitive cycles, repetitions, symmetry, and determinant through one mathematical object.

The tensor-subset program isolates this problem in a rigid setting. Finite full shifts satisfy $$F_m\otimes F_n=F_{mn},\qquad h(F_n)=\log n,
  \tag{1.1}$$ so tensor atoms and their entropy scale arise without a supplied prime mask. For a finite atom set $P$, the preceding Koszul-shaped one-vertex shift used one edge for every nonempty subset $S\subseteq P$, of scalar weight $(-1)^{|S|+1}x_S$. Its adjacency determinant was exactly $$D_P(x)=\prod_{p\in P}(1-x_p).
  \tag{1.2}$$ The countable entropy specialization $x_{F_p}=p^{-s}$ therefore recovered $1/\zeta(s)$ in the ordinary Euler-product half-plane. The determinant was valid, but the primitive objects were subset necklaces rather than atom loops.

The smallest unresolved coefficient occurs at squarefree content $pqr$. Positive and negative primitive cycles both number three, so scalar dimension reports zero. Their atom-permutation actions differ. This suggests a bold same-family continuation: retain the full Burnside, representation, or cycle- index class before applying dimension. Burnside-valued dynamical zeta functions and cycle-index formalisms are classical [@LabelleYeh1989BurnsideSpecies; @GuseinZadeLuengoMelle2015EquivariantZeta]; the question here is whether they produce a character-resolved arithmetic Fredholm determinant for this specific symbolic shift.

The answer is asymmetric. The formal lift exists and retains actual information. At $pqr$, the residual is $$\mathcal R_3=[S_3/S_3]+[S_3/C_3]-[S_3/C_2],
  \tag{1.3}$$ with marks $(0,0,3,1)$ and permutation representation $$R_3=\mathbf 1\oplus\mathbf{sgn}-\mathbf{Std},
  \qquad \chi_{R_3}(e,(12),(123))=(0,0,3).
  \tag{1.4}$$ Dimension erases a nonzero class. A $C_2$ color line also carries the scalar edge signs correctly through Adams powers. These are positive structural results, not failed bookkeeping.

The analytic interpretation fails at the next step. Relabeling atom variables sends one weighted transfer operator to another; after $x_p=p^{-s}$, it does not commute with one fixed operator. Equalizing the weights restores $S_n$ symmetry but leaves a rank-one transfer whose image is the trivial line. A diagonal subset operator keeps representation lines and admits standard supertraces, but it changes the power traces from $b(x)^r$ to $b(x^r)$ and inserts mixed factors into its determinant. The three desired properties---pure Euler ledger, fixed arithmetic character fiber, and nontrivial resolved motion---do not coexist in these canonical realizations.

#### Contributions.

The paper makes four source-locked claims.

1.  We construct the formal $C_2$-colored Burnside/species primitive-cycle ledger of the tensor-subset shift. We calculate the exact $pqr$ Burnside class, its four subgroup marks, its irreducible representation residual, and its persistence under Adams powers.

2.  We distinguish semilinear covariance from fixed-fiber symmetry. The arithmetic rank-one transfer has trivial atom-permutation stabilizer for $\operatorname{Re}s>0$; equal weights restore symmetry only by annihilating every nontrivial isotype.

3.  We prove the ghost and determinant obstruction. For every $r\ge2$, the coefficient of $x_1^{r-1}x_2$ is $r$ in $b(x)^r$ and zero in $b(x^r)$. The diagonal superdeterminant consequently contains mixed subset factors.

4.  We prove a character-readout incompatibility and its analytic boundary. A readout detecting $R_3$ cannot preserve the pure Euler trace-log, while the diagonal prime-subset operator lies in $\mathcal S_q$ exactly for $q\operatorname{Re}s>1$ but retains the wrong mixed determinant.

The result does not conflict with classical equivariant zeta theory. A character factor is natural when a fixed transformation or group extension is genuinely equivariant, as in Lefschetz and twisted-orbit constructions [@GuseinZadeLuengoMelle2015EquivariantZeta; @Pollicott1994TwistedOrbits]. SD-C18 fails that fixed-map hypothesis after distinct entropy weights are substituted. Our no-go is therefore model-specific: it covers the canonical rank-one and diagonal lifts, not every possible finite-group cocycle over a symbolic base.

The strict resolved evaluation is $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
  \texttt{A1\_WEAK},\\
 &\texttt{A2\_FAIL},\texttt{A3\_FAIL},\texttt{A4\_FAIL}).
\end{split}
\tag{1.5}$$ The scalar shadow (1.2) retains the earlier exact determinant theorem, but it has no resolved character fiber and cannot supply A2 to SD-C18 by coordinatewise patching. Accordingly, `ROUTE_A_REJECTED`; Route B is locked.

The remainder separates the classical formalism from the project-specific claims, defines the frozen shift and its sign carrier, proves the $pqr$ certificate, and then audits fixed symmetry, power traces, infinite limits, and controls. No Riemann-zero data or root computation enters the argument.

# Classical boundary and novelty discipline {#sec:boundary}

SD-C18 joins several mature theories. The contribution is not a new Burnside ring, cycle index, or equivariant zeta construction. It is the application of those theories to one frozen signed symbolic shift, followed by a same-object audit that the formal literature does not supply automatically.

## Symbolic zeta and primitive words

For a weighted shift, determinant and trace-log expansions reorganize based closed words into primitive cyclic words and their repetitions. The finite- state relation between shift zeta functions and adjacency determinants is classical [@BowenLanford1970ShiftZeta]. In a one-vertex weighted shift, the transfer reduces to the sum of its edge weights, but the trace-log still remembers all cyclic words before aggregation. The present paper uses this elementary specialization. It does not propose a new symbolic zeta definition.

Necklace enumeration and primitive-root transforms also have a classical Witt-algebra formulation. @MetropolisRota1983Necklaces relate necklace algebras to Witt vectors, while @DressSiebeneicher1989NecklaceWitt identify the infinite-cyclic Burnside ring with necklace, $\lambda$-ring, and universal-Witt structures. These theories justify retaining primitive data before taking scalar ghost coordinates. They do not imply that every refined ghost is the trace of one arithmetically specialized operator.

## Species, cycle indices, and Burnside rings

Joyal's species calculus makes finite-label functoriality and cycle indices systematic [@Joyal1981Species]. Labelle and Yeh connect Burnside rings with virtual species and permutation-group cycle polynomials [@LabelleYeh1989BurnsideSpecies]. Consequently, packaging the squarefree cyclic-partition sets of SD-C18 as a Burnside/species object is classical formalism. Our positive theorem is narrower: the $pqr$ coefficient of this particular shift is a nonzero Burnside class even though its scalar dimension vanishes.

Species are functorial under bijections of finite sets. That fact supplies a canonical relabeling action on formal variables and primitive words. It does not supply inclusions between fixed weighted Hilbert-space operators as the label set grows, nor does it make a prime-weight specialization invariant under relabeling. The distinction between formal functoriality and a commuting fixed operator is the main analytic boundary of this paper.

## $\lambda$-rings, Adams operations, and sign carriers

Burnside and representation rings carry $\lambda$-operations, and their Adams operations encode power maps. The finite-group Burnside construction was developed by @Siebeneicher1976LambdaBurnside; symmetric-group representation rings and their symmetric-function realization are treated by @Knutson1973LambdaRings. Dress and Siebeneicher extend the Witt construction to profinite Burnside rings [@DressSiebeneicher1988ProfiniteWitt], while @Brun2005WittTambara shows that restriction, transfer, and norm compatibility belongs naturally to the richer Tambara framework.

These results expose a sign error that scalar notation can hide. The integer coefficient $-1$ is fixed by a ring endomorphism, whereas a negative edge repeated $r$ times contributes $(-1)^r$. SD-C18 therefore uses the nontrivial $C_2$ character line $\tau$, for which $\psi^r(\tau)=\tau^r$. This is an application of standard $\lambda$-ring power behavior, not a new operation.

## Equivariant and twisted dynamical zeta functions

Equivariant zeta functions are well established when a group acts on a fixed transformation. @GuseinZadeLuengoMelle2015EquivariantZeta construct an integral Burnside-ring-valued zeta function from equivariant Lefschetz numbers. Character and representation factorizations of periodic-orbit zeta functions likewise occur for genuine twists or group extensions [@Pollicott1994TwistedOrbits]. Those constructions require the group action and the dynamical map to be compatible.

SD-C18 begins with a relabeling family $A_x$. A permutation acts on both the subset basis and the weight variables, sending $A_x$ to $A_{g\cdot x}$. After distinct arithmetic weights are substituted, this is not a symmetry of one fixed map. We therefore do not claim that the classical equivariant zeta construction applies. Instead, we prove the precise stabilizer statement and stop the character-Fredholm interpretation at that gate.

## Stable and analytic limits

Changing symmetric groups do not by themselves define an infinite representation-theoretic fiber. FI-modules provide a rigorous language for stable sequences of $S_n$ representations [@ChurchEllenbergFarb2015FI]; the full subset spaces here are not finitely generated because injections preserve subset cardinality. Positive characters of the infinite symmetric group have their own restrictive structure [@Thoma1964InfiniteSymmetric]. The virtual residual $R_3$ has dimension zero but is nonzero, so it is not a positive character: positive definiteness would imply $|\chi(g)|\le\chi(e)=0$.

Analytic determinants impose a separate constraint. Standard Fredholm determinants require trace ideals or related hypotheses [@Simon1977InfiniteDeterminants]. SD-C18 proves a Schatten criterion for its diagonal prime-subset operator. Analytic existence, however, does not identify that operator's determinant with the scalar Euler shadow.

## Exact novelty boundary

The following are not new: Burnside-valued zeta functions, the Burnside/species correspondence, cycle indices, necklace and Witt rings, $\lambda$/Adams operations, twisted character factors, FI-modules, or Fredholm determinant theory. The bounded contribution is:

> For the source-locked tensor-atom subset shift, calculate the first nonzero squarefree Burnside residual and prove that its canonical rank-one and diagonal realizations cannot simultaneously preserve the pure Euler trace-log, fixed arithmetic label symmetry, standard temporal powers, and a nontrivial character readout.

The targeted primary-source search located no direct instance of this exact combined certificate. No priority claim is made, and no universal no-go is asserted beyond the canonical models studied here.

# The frozen tensor-subset shift {#sec:frozen}

## Tensor source and finite edge alphabet

Let $$\mathcal M=\{F_n:n\ge1\},\qquad F_m\otimes F_n=F_{mn},
  \qquad h(F_n)=\log n.
  \tag{3.1}$$ An object $F_n$ is tensor-irreducible precisely when $n$ is prime. Fix a finite set $P$ of such tensor atoms and attach an independent formal variable $x_p$ to every $p\in P$. For a nonempty subset $S\subseteq P$, set $$x_S=\prod_{p\in S}x_p,
  \qquad \varepsilon(S)=(-1)^{|S|+1}.
  \tag{3.2}$$

[\[def:shift\]]{#def:shift label="def:shift"} The phase space is the one-vertex full edge shift with alphabet $$\mathcal E(P)=2^P\setminus\{\varnothing\}.
  \tag{3.3}$$ An edge $S$ has scalar formal weight $w(S)=\varepsilon(S)x_S$. A closed orbit is a cyclic word of subset edges, identified under rotation only. Reflection is not quotiented.

Under the entropy specialization $p=F_\mathfrak p$, $$x_p=e^{-sh(p)}=\mathfrak p^{-s},
  \qquad
  T(S)=\sum_{p\in S}h(p).
  \tag{3.4}$$ The atom set and roof follow from tensor factorization and entropy. No von Mangoldt coefficient, Möbius value, target-zero datum, or fitted phase is part of the edge rule.

## Rank-one edge-state transfer and scalar shadow

Let $V_P=\mathbb C[\mathcal E(P)]$ with orthonormal basis $e_S$, and define $$u_P=\sum_{S\in\mathcal E(P)}e_S,
  \qquad
  \ell_x(e_S)=\varepsilon(S)x_S,
  \qquad
  A_x=u_P\otimes\ell_x.
  \tag{3.5}$$ This is the edge-state presentation of the one-vertex weighted full shift: every arriving edge may be followed by every outgoing edge.

Put $$b_P(x)=\ell_x(u_P)
  =\sum_{S\in\mathcal E(P)}\varepsilon(S)x_S
  =1-\prod_{p\in P}(1-x_p).
  \tag{3.6}$$

[\[thm:rank-one\]]{#thm:rank-one label="thm:rank-one"} For every $r\ge1$, $$A_x^r=b_P(x)^{r-1}A_x,
  \qquad \operatorname{tr}A_x^r=b_P(x)^r,
  \tag{3.7}$$ and $$\det(I-A_x)=1-b_P(x)=\prod_{p\in P}(1-x_p).
  \tag{3.8}$$

The rank-one formula gives $A_x^2(v)=\ell_x(v)\ell_x(u_P)u_P=b_P(x)A_x(v)$, and induction gives (3.7). The trace of $u\otimes\ell$ is $\ell(u)$, while the matrix determinant lemma gives $\det(I-u\otimes\ell)=1-\ell(u)$. Equation (3.6) then proves (3.8).

Where the trace-log is defined formally or analytically, $$-\log\det(I-zA_x)
 =\sum_{r\ge1}\frac{z^r}{r}b_P(x)^r.
 \tag{3.9}$$ Unique primitive-root decomposition regroups (3.9) as a sum over primitive cyclic subset words and their repetitions. A negative scalar edge contributes its actual powered sign $(-1)^r$ at repetition $r$.

Theorem [\[thm:rank-one\]](#thm:rank-one){reference-type="ref" reference="thm:rank-one"} is the scalar shadow inherited from the preceding candidate. SD-C18 asks for more: retain the atom-permutation information of the primitive words and determine whether it defines invariant Fredholm fibers of the same arithmetic transfer.

## Relabeling and the $C_2$ sign carrier

Let $G_P=\mathfrak S(P)$. It acts on subset edges by $$\rho(g)e_S=e_{gS}
  \tag{3.10}$$ and on the coefficient ring by relabeling the variables. Before arithmetic specialization, primitive cyclic words therefore form multigraded $G_P$-sets. Their isomorphism classes can be retained in the Burnside ring and then linearized in the representation ring. The cycle index records the same finite-label action in symmetric-function coordinates.

The scalar sign requires a separate power convention. Let $C_2=\{1,c\}$ and let $\tau$ be its nontrivial character line. Color an edge $S$ by $$\tau^{|S|+1}.
  \tag{3.11}$$ Evaluation at $c$ recovers $\varepsilon(S)$. More importantly, $$\psi^r(\tau^{|S|+1})(c)
  =\tau(c^r)^{|S|+1}
  =\varepsilon(S)^r.
  \tag{3.12}$$ Thus the $C_2$-colored ledger respects the frozen temporal-power sign. By contrast, treating the scalar coefficient $-1$ as an integer under Adams operations would leave it fixed and fail at every even repetition.

[\[def:ledger\]]{#def:ledger label="def:ledger"} For each finite $P$, the SD-C18 ledger is the multigraded primitive-cycle class in the completed $C_2$-colored Burnside/species ring, with color (3.11), $G_P$ relabeling (3.10), and Adams powers acting on both colors and monomial multidegrees.

Definition [\[def:ledger\]](#def:ledger){reference-type="ref" reference="def:ledger"} is formal: it stores orbit types, marks, characters, and powers before a scalar readout. It is not yet a fixed- operator character determinant. The next section shows why retaining this formal layer is nevertheless informative.

# Formal Burnside lift and the squarefree certificate {#sec:burnside}

## Squarefree cycles are cyclic set partitions

Fix $|P|=n$ and consider the full squarefree multidegree $x_P=\prod_{p\in P}x_p$. Every label appears exactly once. The edge subsets of a contributing word are therefore disjoint and cover $P$.

[\[prop:cyclic-partition\]]{#prop:cyclic-partition label="prop:cyclic-partition"} A cyclic word at squarefree content $x_P$ is primitive and is equivalent to a cyclically ordered set partition of $P$. With $m$ blocks, the number of cycles is $$(m-1)!S(n,m),
  \tag{4.1}$$ and their common scalar sign is $(-1)^{n+m}$.

A nontrivial repetition would repeat every label of the shorter root, which is impossible at squarefree content. An unordered set partition into $m$ blocks has $(m-1)!$ cyclic orders. The product of the edge signs is $$\prod_{j=1}^m(-1)^{|S_j|+1}=(-1)^{n+m}.$$

Consequently the total number of squarefree primitive cycles is $$N_n=\sum_{m=1}^n(m-1)!S(n,m).
  \tag{4.2}$$ For $n\ge2$, the positive and negative scalar counts agree. One proof is to observe that their difference is the coefficient of $x_P$ in $$-\log\prod_{p\in P}(1-x_p)
  =\sum_{p\in P}-\log(1-x_p),
  \tag{4.3}$$ which has no mixed monomial. Exact values through seven labels are listed in . These counts show that scalar balance persists; they do not prove equivariant balance.

::: {#tab:squarefree-counts}
    $n$   total   positive   negative   difference
  ----- ------- ---------- ---------- ------------
      2       2          1          1            0
      3       6          3          3            0
      4      26         13         13            0
      5     150         75         75            0
      6   1,082        541        541            0
      7   9,366      4,683      4,683            0

  : Squarefree primitive cyclic-partition counts. The equality of positive and negative columns is scalar cancellation; it does not imply an equivariant pairing.
:::

## The first nonzero Burnside residual

Take $P=\{p,q,r\}$. The six cycles separate by sign as $$C_+=\{[pqr],[p][q][r],[p][r][q]\},
 \tag{4.4}$$ $$C_-=\{[p][qr],[q][pr],[r][pq]\}.
 \tag{4.5}$$ Here $[pqr]$ denotes the one-edge subset $\{p,q,r\}$, while brackets between singletons denote a cyclic word of several edges.

[\[thm:pqr\]]{#thm:pqr label="thm:pqr"} The virtual $S_3$-set at squarefree content $pqr$ is $$\mathcal R_3=[C_+]-[C_-]
  =[S_3/S_3]+[S_3/C_3]-[S_3/C_2].
  \tag{4.6}$$ Its marks at subgroup classes $(1,C_2,C_3,S_3)$ are $$(0,0,3,1).
  \tag{4.7}$$ Under permutation linearization, $$R_3=\mathbf 1\oplus\mathbf{sgn}-\mathbf{Std},
  \tag{4.8}$$ and its character at $(e,(12),(123))$ is $$(0,0,3).
  \tag{4.9}$$ Thus scalar dimension kills a nonzero Burnside and representation class.

The one-block cycle in (4.4) is fixed by all of $S_3$, giving $S_3/S_3$. The two orientations of three singleton blocks form the two-point orbit $S_3/C_3$: a transposition exchanges them, while a three-cycle is a cyclic rotation and fixes both necklaces. The three singleton--pair cycles in (4.5) form the natural orbit $S_3/C_2$. This proves (4.6).

The identity subgroup fixes all objects. A subgroup $C_2$ fixes the one-block positive cycle and one singleton--pair negative cycle. The $C_3$ subgroup fixes all three positive cycles and none of the negative cycles. The full group fixes only the one-block positive cycle. Subtraction gives (4.7).

Finally, $$\mathbb C[S_3/S_3]=\mathbf 1,
 \quad \mathbb C[S_3/C_3]=\mathbf 1\oplus\mathbf{sgn},
 \quad \mathbb C[S_3/C_2]=\mathbf 1\oplus\mathbf{Std}.
 \tag{4.10}$$ Their virtual difference is (4.8). The $S_3$ character table then gives (4.9).

::: {#tab:pqr-marks}
  Subgroup     $|C_+^H|$   $|C_-^H|$   $\phi_H(\mathcal R_3)$
  ---------- ----------- ----------- ------------------------
  $1$                  3           3                        0
  $C_2$                1           1                        0
  $C_3$                3           0                        3
  $S_3$                1           0                        1

  : The exact $pqr$ certificate. Marks count subgroup-fixed objects; the final column is positive minus negative.
:::

An equivariant sign-reversing bijection would induce equal fixed-point counts for every subgroup. The $C_3$ mark rules it out. The failure is stronger than unequal presentation choices: it is invariant under relabeling and is visible in both Burnside and representation rings.

## Adams isolation and formal projectivity

[\[prop:adams-isolation\]]{#prop:adams-isolation label="prop:adams-isolation"} No Adams power $\psi^k$ with $k>1$ maps a monomial of integral nonnegative multidegree to $x_px_qx_r$. Hence no temporal higher-power counterterm removes $\mathcal R_3$ or $R_3$.

On monomials, $\psi^k(x^\alpha)=x^{k\alpha}$. Equality $k\alpha=(1,1,1)$ has no solution in $\mathbb N^3$ when $k>1$.

The $C_2$ carrier from (3.11) handles the sign component simultaneously: $\psi^k(\tau)=\tau^k$. Thus the formal positive result respects both multidegree and scalar temporal powers.

For an inclusion $P\subset Q$, specialize $x_q=0$ for every $q\in Q\setminus P$. Every edge meeting a new label vanishes, while the old edge and primitive-cycle terms remain. These zero-specializations compose, so the multigraded Burnside/species ledgers form a formal projective family. This statement concerns coefficients and cycle indices. It does not yet construct an inductive system of fixed weighted operators; that analytic question is deferred to .

# Fixed arithmetic symmetry obstruction {#sec:symmetry}

The Burnside class of is functorial under relabeling. A character Fredholm factor needs more: the same group must commute with one fixed transfer operator. This section tests that requirement directly.

## Semilinear covariance

For $g\in G_P=\mathfrak S(P)$, let $\rho(g)e_S=e_{gS}$. Define the relabeled variables by $(g\cdot x)_S=x_{g^{-1}S}$.

[\[thm:covariance\]]{#thm:covariance label="thm:covariance"} The rank-one family satisfies $$\rho(g)A_x\rho(g)^{-1}=A_{g\cdot x}.
  \tag{5.1}$$ For a fixed specialization $x$, the following are equivalent:

1.  $[A_x,\rho(g)]=0$;

2.  $x_{gS}=x_S$ for every nonempty $S\subseteq P$;

3.  $x_{gp}=x_p$ for every $p\in P$.

The vector $u_P$ is invariant. On a basis vector, $$(\ell_x\rho(g)^{-1})(e_S)
 =\varepsilon(S)x_{g^{-1}S}=\ell_{g\cdot x}(e_S),
 \tag{5.2}$$ which proves (5.1). Commutation is equivalent to invariance of the covector $\ell_x$, giving the equivalence of the first two statements. Singleton subsets show that the second statement implies the third; multiplicativity of $x_S$ gives the converse.

Equation (5.1) is a semilinear symmetry of a family: the permutation changes both the subset basis and the coefficient point. It is not a decomposition of $A_x$ into invariant character fibers unless the equivalent conditions of hold.

[\[cor:arithmetic-stabilizer\]]{#cor:arithmetic-stabilizer label="cor:arithmetic-stabilizer"} Under $x_{F_p}=p^{-s}$ with $\operatorname{Re}s>0$, the fixed operator $A_x$ has trivial atom-permutation stabilizer.

If $p\ne q$, then $|p^{-s}|=p^{-\operatorname{Re}s}\ne q^{-\operatorname{Re}s}=|q^{-s}|$. A stabilizing permutation must fix every singleton weight and hence every atom.

Central idempotents of $\mathbb C[S_n]$ therefore do not project the fixed arithmetic operator onto invariant character fibers. They project the unweighted permutation representation, but $A_x$ moves those subspaces when the weights are distinct.

## Equal weights and rank-one collapse

One can restore commutation by setting $x_p=t$ for all labels. This removes the arithmetic distinctions and exposes a second obstruction.

[\[thm:equal-weight\]]{#thm:equal-weight label="thm:equal-weight"} At equal weights, $A_t$ is $S_n$-equivariant, $$\operatorname{im}A_t=\mathbb Cu_P,
  \tag{5.3}$$ and its restriction to every nontrivial isotype is zero. Hence $$\det(I-A_t\mid V_\lambda)=1
  \tag{5.4}$$ for every nontrivial irreducible type $\lambda$. The only nonzero eigenvalue is $$b_P(t)=1-(1-t)^n.
  \tag{5.5}$$

Equal weights make $\ell_t$ invariant, so gives equivariance. The rank-one formula (3.5) gives (5.3), and $u_P$ spans a trivial representation. An equivariant map from a nontrivial irreducible summand to the trivial line is zero. The determinant on every such summand is therefore one. Finally, the rank-one eigenvalue is $\ell_t(u_P)=b_P(t)$.

The full subset representation has one trivial basis vector for each subset cardinality, so its trivial isotypic component has dimension $n$. The operator on that component is still rank one. Its determinant at $z=1$ is $$1-b_P(t)=(1-t)^n.
  \tag{5.6}$$ All resolved nontrivial modes are identically one. Equalization thus restores the group only after deleting the label scale that made the specialization arithmetic and the character motion that motivated SD-C18.

## What the finite character still means

The obstruction does not make $R_3$ spurious. It means that $R_3$ belongs to the formal primitive-cycle functor, not to invariant fibers of the fixed prime-weighted rank-one operator. Three statements must be kept separate:

-   the formal variable family is equivariant under simultaneous relabeling;

-   the squarefree primitive coefficient is a nonzero virtual $S_3$ class;

-   the arithmetically specialized transfer has no nontrivial $S_3$ symmetry.

The first two earn `GO_FORMAL_EQUIVARIANT_LEDGER`. The third blocks a character Fredholm interpretation of the canonical rank-one specialization.

# Ghost, determinant, and character-readout incompatibility {#sec:ghost}

The fixed-fiber obstruction concerns the rank-one transfer. A natural alternative keeps each subset edge as a separate line and lets $S_n$ permute those lines. This diagonal lift is genuinely representation-preserving, but its temporal traces reveal that it is a different determinant.

## The diagonal subset operator

Define $$D_xe_S=x_Se_S.
  \tag{6.1}$$ Use the parity $\varepsilon(S)=(-1)^{|S|+1}$ only as a supertrace readout. Then $$\operatorname{Str}(D_x^r)
  =\sum_{S\ne\varnothing}\varepsilon(S)x_S^r
  =b_P(x_1^r,\ldots,x_n^r).
  \tag{6.2}$$ This is the standard Adams ghost. It differs from the rank-one trace $b_P(x)^r$ in (3.7).

[\[thm:ghost-separation\]]{#thm:ghost-separation label="thm:ghost-separation"} For $n\ge2$ and $r\ge2$, $$[x_1^{r-1}x_2]b_P(x)^r=r,
 \qquad
 [x_1^{r-1}x_2]b_P(x_1^r,\ldots,x_n^r)=0.
 \tag{6.3}$$ Hence the rank-one and diagonal ghost sequences disagree at every power $r\ge2$.

Every term of $b_P$ has total degree at least one. A degree-$r$ monomial in $b_P^r$ must choose a degree-one singleton from every factor. Choose $x_2$ from one of the $r$ factors and $x_1$ from all others, giving coefficient $r$. Every exponent in $b_P(x^r)$ is divisible by $r$, so the second coefficient is zero.

The witness is independent of the label inventory. It also shows why a formal $C_2$ sign carrier is not the same as declaring subset edges even and odd. The $C_2$ character reproduces the scalar powered sign inside the formal ledger; a fixed supertrace parity produces (6.2). Replacing one by the other changes even-power traces.

## Mixed-factor superdeterminant

Where the diagonal trace-log is formal or trace class, exponentiation of (6.2) yields $$\begin{split}
 \operatorname{sdet}(I-D_x)
 &=\exp\left(-\sum_{r\ge1}\frac1r
       b_P(x_1^r,\ldots,x_n^r)\right)\\
 &=\prod_{S\ne\varnothing}(1-x_S)^{\varepsilon(S)}.
\end{split}
\tag{6.4}$$

[\[thm:diagonal-determinant\]]{#thm:diagonal-determinant label="thm:diagonal-determinant"} For every $n\ge2$, the superdeterminant (6.4) is not the pure Euler determinant $\prod_{p\in P}(1-x_p)$.

For two labels, $$\operatorname{sdet}(I-D_x)
  =\frac{(1-x_1)(1-x_2)}{1-x_1x_2},
  \tag{6.5}$$ which differs formally from $(1-x_1)(1-x_2)$. For $n>2$, set every other variable to zero. Equality would specialize to the false two-variable identity.

At $x_1=1/4$ and $x_2=1/9$, the distinction is already exact: $$(1-x_1)(1-x_2)=\frac23,
  \qquad
  \operatorname{sdet}(I-D_x)=\frac{24}{35}.
  \tag{6.6}$$ The extra factor is not a small numerical error; the ratio is $36/35$. Regularizing a later infinite product cannot erase a finite trace mismatch while preserving the same operator powers.

## The character-readout theorem

The $pqr$ class provides a direct incompatibility without choosing an analytic realization. Let $L$ be any linear scalar readout of the isolated representation coefficient in .

[\[thm:readout\]]{#thm:readout label="thm:readout"} If $L(R_3)\ne0$, the resolved primitive trace-log has a nonzero mixed $x_px_qx_r$ coefficient. If the readout agrees with the pure Euler trace-log, then $L(R_3)=0$. Thus no linear readout both detects the first resolved motion and preserves the pure Euler trace-log.

The primitive coefficient at squarefree content is $R_3$ by . By , no higher temporal power has that multidegree, so the coefficient after applying $L$ is exactly $L(R_3)$. On the other hand, $$-\log\prod_{a\in P}(1-x_a)
  =\sum_{a\in P}\sum_{k\ge1}\frac{x_a^k}{k}
  \tag{6.7}$$ contains no mixed monomial. Agreement with (6.7) forces $L(R_3)=0$.

The theorem is conditional only on the explicitly verified isolation of the squarefree coefficient. It is not a claim that every nontrivial character zeta contains every mixed composite. It states that the first motion in SD-C18 is itself a mixed primitive coefficient, so a readout cannot both see it and pretend that the trace-log contains atom powers only.

## The incompatibility triangle

establish the three sides summarized in :

1.  augmentation or dimension preserves the scalar Euler determinant but kills $R_3$;

2.  distinct arithmetic weights preserve the entropy scale but destroy the commuting label symmetry, while equal weights restore symmetry and kill every nontrivial rank-one mode;

3.  the diagonal lift retains representation lines and standard powers but changes the ghost sequence and determinant.

No coordinatewise combination is allowed. In particular, one cannot take the scalar determinant from $A_x$, the character spaces from $D_x$, and the arithmetic specialization from a semilinear family, then call the collection one Fredholm determinant.

# Infinite-label analytic boundary {#sec:infinite}

The finite Burnside ledger is coherent under zero-specialization. An infinite arithmetic determinant needs an operator limit as well. The two limits have different variances: restriction of formal variables is contravariant, while an operator inductive limit needs intertwining maps and bounded norms.

## Formal projective family versus raw transfer

For $P\subset Q$, let $i_{P,Q}:V_P\to V_Q$ map $e_S$ to the same subset basis vector. Zero-specialization gives $$b_Q(x_P,x_{Q\setminus P}=0)=b_P(x_P),
  \tag{7.1}$$ and deletes every multigraded primitive term containing a new label. This is the formal projective map used in .

[\[prop:no-inductive-transfer\]]{#prop:no-inductive-transfer label="prop:no-inductive-transfer"} If $P\subsetneq Q$, then $$A_Qi_{P,Q}\ne i_{P,Q}A_P.
  \tag{7.2}$$ Moreover, $$\|A_x\|
  =\sqrt{2^{|P|}-1}
   \left(\prod_{p\in P}(1+|x_p|^2)-1\right)^{1/2}.
  \tag{7.3}$$ Along increasing prime sets and any fixed nonzero specialization, these raw operator norms diverge.

For $T\in\mathcal E(P)$, $$A_Qi_{P,Q}e_T=\varepsilon(T)x_Tu_Q,
 \qquad
 i_{P,Q}A_Pe_T=\varepsilon(T)x_Ti_{P,Q}u_P.
 \tag{7.4}$$ The first vector contains every new subset edge, proving (7.2). Since $A_x=u_P\otimes\ell_x$, $\|A_x\|=\|u_P\|\|\ell_x\|$. Here $\|u_P\|^2=2^{|P|}-1$ and $$\|\ell_x\|^2=\sum_{S\ne\varnothing}|x_S|^2
 =\prod_{p\in P}(1+|x_p|^2)-1,$$ which gives (7.3). The second factor stays bounded below by any fixed singleton weight, while the first diverges.

Compressions are compatible: $i_{P,Q}^*A_Qi_{P,Q}=A_P$. That fact supports the projective viewpoint but does not reverse (7.2). A rescaling or noncanonical embedding could alter the norm, but it would also change the transfer and must be frozen as a new candidate.

The changing symmetric-group representations also lack automatic stability. The FI-object $P\mapsto\mathbb C[2^P\setminus\{\varnothing\}]$ is not finitely generated: a generator supported on a subset of size at most $d$ maps under injections only to subsets of size at most $d$, so it cannot generate basis vectors of size $d+1$. Completed cycle indices remain useful formal ledgers; FI-module theorems do not turn them into a finite-type $S_\infty$ Fredholm fiber [@ChurchEllenbergFarb2015FI].

## The diagonal prime-subset operator

The diagonal lift has a clean infinite realization. Let $\mathcal P$ be the rational primes and $$\mathcal H=\ell^2\bigl(2^{\mathcal P}_{\mathrm{fin}}
                 \setminus\{\varnothing\}\bigr).
  \tag{7.5}$$ For $\sigma=\operatorname{Re}s>0$, define $$D_se_S=\left(\prod_{p\in S}p^{-s}\right)e_S.
  \tag{7.6}$$

[\[thm:schatten\]]{#thm:schatten label="thm:schatten"} For every $q\ge1$, $$D_s\in\mathcal S_q
 \quad\Longleftrightarrow\quad q\sigma>1,
 \tag{7.7}$$ and, in that domain, $$\|D_s\|_{\mathcal S_q}^q
 =\prod_p(1+p^{-q\sigma})-1.
 \tag{7.8}$$

The singular values are $\prod_{p\in S}p^{-\sigma}$. Monotone convergence over finite prime sets gives $$\sum_{S\ne\varnothing}\prod_{p\in S}p^{-q\sigma}
 =\prod_p(1+p^{-q\sigma})-1.
 \tag{7.9}$$ For nonnegative $a_p\to0$, the product $\prod_p(1+a_p)$ is finite exactly when $\sum_pa_p$ is finite, by comparison of $\log(1+a_p)$ with $a_p$. The prime Dirichlet series $\sum_pp^{-\alpha}$ converges exactly for $\alpha>1$. Taking $\alpha=q\sigma$ proves (7.7).

For $q=1$, standard trace-class Fredholm determinants therefore exist when $\sigma>1$, in the sense of the usual trace-ideal theory [@Simon1977InfiniteDeterminants]. Splitting (7.5) by subset parity gives the superdeterminant $$\prod_{S\ne\varnothing}(1-p_S^{-s})^{\varepsilon(S)},
  \qquad p_S=\prod_{p\in S}p,
  \tag{7.10}$$ not the atom-only product $\prod_p(1-p^{-s})$. The analytic half-plane is a positive theorem about $D_s$, but it cannot be credited as A2 for the desired character-resolved Euler determinant.

Equal weights produce the opposite analytic problem. On a countably infinite atom set, every singleton has the same nonzero eigenvalue, so the diagonal equal-weight operator is noncompact. Thus the two repairs do not meet: prime weights give compactness without label symmetry, while equal weights give symmetry without a Fredholm operator or arithmetic scale.

# Exact certificates, controls, and Route-A decision {#sec:controls}

The theorems determine the decision. Exact finite computation checks that the implementation uses the same cyclic convention, group action, multidegrees, and temporal powers. No Riemann-zero data, root finder, parameter fit, or selected character after inspection enters the audit.

## Finite certificate audit

The squarefree enumerator recovers the totals in for $2\le n\le7$ and verifies exact scalar balance at every order. Its $S_3$ action independently returns $$\chi_{R_3}=(0,0,3),\qquad
  (\phi_1,\phi_{C_2},\phi_{C_3},\phi_{S_3})=(0,0,3,1),
  \tag{8.1}$$ and the irreducible multiplicity vector $(1,1,-1)$ for $(\mathbf 1,\mathbf{sgn},\mathbf{Std})$. Higher squarefree orders also contain nonzero character values despite scalar balance; the paper uses only the minimal $pqr$ theorem.

For $2\le n\le8$ and $2\le r\le8$, all 56 frozen ghost rows recover the coefficient witness in . The $C_2$ sign carrier passes 4,008 edge/power comparisons, while the naive integer-Adams substitution disagrees in 988 cases. These checks verify the formal power convention rather than selecting it.

Zero-specialization is exact for the maps $2\to1,\ldots,8\to7$. Distinct weights have stabilizer order one, equal weights have stabilizer order $n!$, and every nontrivial equal-weight rank-one isotype has determinant one. The diagonal superdeterminant differs from the target through every frozen $n=2,\ldots,8$, starting with the exact two-label certificate (6.6).

The project bundle records 12 of 12 theorem-level checks and 17 of 17 unit tests as passing. All 16 code/result checksum entries pass, and the exact tables use integer or rational arithmetic whenever the claim is algebraic. Finite prime cutoffs illustrate the Schatten regimes but do not establish ; the infinite-product proof does.

## Inventory controls and arithmetic selectivity

The finite algebra is applied without change to prime, composite-only, shuffled-prime, distinct random rational, and free-commutative inventories. All 455 frozen control rows reproduce the Burnside, stabilizer, ghost, and diagonal determinant statements.

Passing these controls is negative arithmetic evidence. The Boolean subset grammar produces the formal residual and the incompatibility for any label inventory. Tensor factorization and entropy still provide an intrinsic atom set and analytic prime scale, so A0 remains strong. The character mechanism itself does not distinguish rational primes from matched controls. It therefore receives $$\texttt{STOP\_ARITHMETIC\_SELECTIVITY / PROVES\_TOO\_MUCH}.
  \tag{8.2}$$

## Resolved route decision

evaluates SD-C18 as a resolved candidate. Each row refers to the same formal/analytic object declared in the source lock; no coordinate is borrowed from a different determinant.

L0.14L0.25X Gate & Verdict & Reason\
A0 &

::: {#tab:route}
  --------------------
  A0\_ANALYTIC
  ARITHMETIC\_ORIGIN
  --------------------

  : Strict Route-A decision for the character-resolved candidate SD-C18.
:::

& Tensor-irreducible full shifts give the atom inventory and entropy gives the prime logarithmic scale without target-zero data.\
A1 & `A1_WEAK` & Primitive squarefree cycles and nonzero character motion are intrinsic, but they do not reduce to orbitwise atom loops and the same formal residual occurs for arbitrary inventories.\
A2 & `A2_FAIL` & The fixed prime-weighted rank-one operator has no nontrivial character fibers; the diagonal resolved operator has different power traces and a mixed superdeterminant.\
A3 & `A3_FAIL` & There is no completed functional equation, Gamma factor, global divisor theorem, Riemann--von Mangoldt law, continuation result, or intrinsic Weil compression for the resolved object.\
A4 & `A4_FAIL` & No natural unitary, scattering, Hamiltonian, or self-adjoint lift is defined.\

The scalar rank-one shadow in still has the exact determinant $\prod_p(1-x_p)$ and its countable half-plane specialization. That theorem was already credited to the preceding scalar candidate. It is not a character-resolved determinant and does not change the A2 verdict in . Combining scalar A2 with resolved A1 would violate the same-object rule.

The frozen outcomes are therefore $$\begin{gathered}
 \texttt{GO\_FORMAL\_EQUIVARIANT\_LEDGER},\\
 \texttt{STOP\_CHARACTER\_FREDHOLM\_FIBERS},\qquad
 \texttt{STOP\_STANDARD\_SUPERTRACE\_INTERPRETATION},\\
 \texttt{STOP\_ARITHMETIC\_SELECTIVITY},\qquad
 \texttt{PROVES\_TOO\_MUCH}.
\end{gathered}
\tag{8.3}$$ Overall, `ROUTE_A_REJECTED`. A2, A3, and A4 are not closed, so Route B is not invoked and remains locked.

# Conclusion and next symbolic obligation {#sec:conclusion}

The character refinement was worth testing. The scalar tensor-subset determinant had erased a genuine primitive-cycle class: at $pqr$, the Burnside marks $(0,0,3,1)$ and the character $\mathbf 1+\mathbf{sgn}-\mathbf{Std}=(0,0,3)$ are nonzero. A $C_2$ color line carries the edge signs through temporal powers, and the finite cycle indices form a coherent formal projective family. These results justify `GO_FORMAL_EQUIVARIANT_LEDGER`.

The same refinement does not yield arithmetic character-Fredholm fibers in the canonical realization. Prime entropy weights break fixed-fiber label symmetry. Equal weights restore symmetry but leave only the trivial rank-one image. The diagonal subset operator retains representation lines and has a clean Schatten threshold, yet its ghosts are $b(x^r)$ rather than $b(x)^r$ and its determinant contains mixed factors. At the smallest isolated coefficient, any readout that detects the residual inserts a mixed primitive term absent from the pure Euler trace-log. Analytic existence and formal equivariance therefore belong to different objects.

The strongest lesson is a data-type firewall. A cycle-index ledger, a scalar full-shift determinant, a character decomposition, and a trace-class diagonal operator can each be valid. They are not one determinant unless their powers, symmetry action, specialization, and limit maps agree. SD-C18 fails exactly at those interfaces, so the scalar shadow's A2 result cannot be patched into the resolved route tuple.

The next admissible step remains inside Symbolic Dynamics. A genuine finite-group cocycle or group extension could act in a fiber independently of the arithmetic roof, satisfying the fixed-map hypothesis that base-label relabeling lacks. Such a candidate must derive its cocycle from the symbolic grammar, publish every power trace before its determinant, retain a prime/prime-power ledger, and fail composite, shuffled, random, and free-commutative controls. It begins as a new source-locked object; it is not a reinterpretation of SD-C18.

Ideas that require a geometric orientation bundle, holonomy carrier, scattering system, or self-adjoint generator leave the current system family. They are recorded only as `ROUND2_CLUE`. The present decision is $$\boxed{\texttt{ROUTE\_A\_REJECTED};\quad
        \texttt{ROUTE\_B\_LOCKED}.}$$ No claim about Riemann zeros, the critical line, or the Riemann Hypothesis is made.

# Supplementary proofs and scope ledger {#app:proofs}

## Primitive-root regrouping

Let $F=\sum_{S\in\mathcal E(P)}w(S)$. The coefficient of $z^n$ in $$\sum_{n\ge1}\frac{z^nF^n}{n}
  \tag{A.1}$$ is a weighted sum over based words of length $n$. Every based word has a unique primitive cyclic root $\gamma$ of length $\ell$ and repetition number $r=n/\ell$. A primitive necklace of length $\ell$ has exactly $\ell$ based rotations. Its total coefficient is therefore $$\frac{\ell}{r\ell}w(\gamma)^r
  =\frac{w(\gamma)^r}{r}.
  \tag{A.2}$$ This proves the primitive/repetition expansion of the rank-one trace-log. The full scalar sign is inside $w(\gamma)^r$ and cannot be replaced by a fixed parity after regrouping.

## Complete $S_3$ character calculation

The irreducible character table in class order $e,(12),(123)$ is $$\begin{array}{c|rrr}
 & e & (12) & (123)\\ \hline
\mathbf 1& 1&1&1\\
\mathbf{sgn}& 1&-1&1\\
\mathbf{Std}& 2&0&-1
\end{array}
\tag{A.3}$$ and the residual character is $(0,0,3)$. Using conjugacy-class sizes $1,3,2$, its inner products with the irreducibles are $$\langle\chi,\mathbf 1\rangle=1,
 \qquad
 \langle\chi,\mathbf{sgn}\rangle=1,
 \qquad
 \langle\chi,\mathbf{Std}\rangle=-1.
 \tag{A.4}$$ Hence $R_3=\mathbf 1+\mathbf{sgn}-\mathbf{Std}$. The zero dimension is the value at the identity, not the zero character.

The residual is not the character of a genuine unitary representation: its dimension is zero but its three-cycle value is three. More generally, a positive-definite character satisfies $|\chi(g)|\le\chi(e)$ by positivity of the $2\times2$ matrix at $e,g$. This elementary obstruction is compatible with the classical classification of extreme characters of the infinite symmetric group [@Thoma1964InfiniteSymmetric]. We use the residual only as a virtual finite-label coefficient.

## Why the $C_2$ line is necessary

In a representation $\lambda$-ring, Adams operations are ring endomorphisms, so the additive integer coefficient $-1$ remains $-1$. A negative scalar edge, however, has repetition weights $$-w,+w^2,-w^3,+w^4,\ldots.
  \tag{A.5}$$ For the nontrivial $C_2$ character $\tau$ and nontrivial element $c$, $$\psi^r(\tau)(c)=\tau(c^r)=(-1)^r.
  \tag{A.6}$$ Thus the color line reproduces (A.5). Declaring the line odd in a fixed supertrace instead would contribute $-w^r$ at every $r$, which disagrees at all positive even powers. The formal color and analytic grading are different data types.

## Two-variable determinant coefficients

For two labels, $$b(x,y)=x+y-xy.
 \tag{A.7}$$ The rank-one determinant is $$1-b(x,y)=(1-x)(1-y).
 \tag{A.8}$$ The diagonal ghosts are $x^r+y^r-x^ry^r$, and exponentiation gives $$\frac{(1-x)(1-y)}{1-xy}.
 \tag{A.9}$$ The coefficient of $xy$ in (A.8) is one, whereas in (A.9) it is two. This finite mismatch precedes any convergence or regularization question.

## Raw norm and compression details

For $P\subset Q$, the canonical compression satisfies $$i_{P,Q}^*A_Qi_{P,Q}=A_P,
 \tag{A.10}$$ because the left projection removes every new component of $u_Q$. The intertwining identity fails in the forward direction by (7.4). A compatible family of compressions is therefore projective, not an operator inductive system.

At prime weights $x_p=p^{-s}$, $$\|A_P\|^2
 =(2^{|P|}-1)
  \left(\prod_{p\in P}(1+p^{-2\operatorname{Re}s})-1\right).
 \tag{A.11}$$ The second factor converges to a finite positive limit when $2\operatorname{Re}s>1$ and diverges otherwise; in either case the factor $2^{|P|}-1$ forces raw norm divergence.

## Schatten product criterion

For $a_p=p^{-q\sigma}$, finite prime cutoffs give $$\sum_{\varnothing\ne S\subseteq P}\prod_{p\in S}a_p
  =\prod_{p\in P}(1+a_p)-1.
  \tag{A.12}$$ Taking increasing limits is justified by monotone convergence. For all sufficiently large $p$, $0\le a_p\le1$, and $$\frac{a_p}{2}\le\log(1+a_p)\le a_p.
  \tag{A.13}$$ Therefore the product in (A.12) is finite exactly when $\sum_pa_p$ is finite. Euler's divergence of $\sum_p1/p$ and comparison prove divergence for $q\sigma\le1$; comparison with the integer Dirichlet series proves convergence for $q\sigma>1$.

## Scope and nonclaims

The paper proves no statement about:

-   zeros of $\zeta$ or $\xi$, the critical line, or the Riemann Hypothesis;

-   a Gamma factor, functional equation, trivial zeros, global divisor equality, or Riemann--von Mangoldt counting law;

-   a Weil Hermitian compression or explicit-formula identity;

-   a self-adjoint, unitary, scattering, Hamiltonian, or geometric carrier;

-   all equivariant symbolic group extensions or all regularized determinants;

-   an analytic $S_\infty$ character fiber arising from the formal cycle index.

The no-go applies to the source-locked rank-one edge transfer, the canonical diagonal subset lift, the natural finite-label permutation action, and their declared limit maps. Any model that changes the group action, function space, transfer, power traces, or determinant is a new candidate.

The resolved route tuple remains $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
  \texttt{A1\_WEAK},\\
 &\texttt{A2\_FAIL},\texttt{A3\_FAIL},\texttt{A4\_FAIL}),
\end{split}$$ with `ROUTE_A_REJECTED` and Route B locked.

# Availability, ethics, and contribution statements {#app:statements}

#### Data and code availability.

The paper uses no external dataset and no Riemann-zero data. The project directory contains the exact finite enumerator, frozen tests, result tables, and checksums used to audit the small certificates. The theorem claims do not depend on floating-point extrapolation.

#### Ethics statement.

The study uses formal mathematics and synthetic finite computations. It involves no human participants, animals, personal data, or deployment-facing decision system.

#### Author contributions.

The anonymous authors jointly contributed conceptualization, formal analysis, software, verification, visualization, and manuscript preparation. A final CRediT assignment should be supplied if the manuscript is de-anonymized.

#### Funding.

No external funding information was provided for this exploratory manuscript.

#### Conflict of interest.

No conflict of interest was declared for this exploratory manuscript.

#### Use of automated tools.

Automated tools assisted exact symbolic enumeration, consistency checks, and manuscript compilation. All theorem statements, route labels, and claim boundaries were checked against the frozen source lock; no automated output is treated as a proof without the accompanying derivation.
