---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--31-wilson-semiring-verifier-trichotomy"
canonical_tex: "symbolic_dynamics/papers/31-wilson-semiring-verifier-trichotomy/main.tex"
canonical_pdf: "symbolic_dynamics/papers/31-wilson-semiring-verifier-trichotomy/main.pdf"
source_sha256: "aaa9ad5f6acc46b26755174f7c99e00148cc6ff1ad87ced466772b7512371601"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Wilson Semiring Verifiers in Symbolic Dynamics: Matched-Clone, Pruning, and Clock-Dilution Obstructions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/31-wilson-semiring-verifier-trichotomy>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/31-wilson-semiring-verifier-trichotomy/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/31-wilson-semiring-verifier-trichotomy/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/31-wilson-semiring-verifier-trichotomy/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/31-wilson-semiring-verifier-trichotomy/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Paper 30 shows that the multiplicative, divisibility, incidence, roof, and Gram data of finite full shifts are indistinguishable from a transported formal UFD clone. We test the minimal nonmultiplicative escape by adjoining alphabet sum, successor, and congruence. Alphabet sum reconstructs the nonnegative-integer semiring and provably breaks the old bare clone, yet an isomorphic matched semiring clone transports the entire enrichment. A stationary Wilson residue graph then has exactly one primitive cycle of length $p-1$ for each prime $p$, giving the marked periodic product $\prod_p(1-z^{p-1}p^{-s})$. This product specializes to $1/\zeta(s)$ at $z=1$, but the whole recurrent adjacency is noncompact for every nonnegative exact-clock allocation with total roof $\log p$. First return recovers a trace-class Euler determinant only by changing the marker to $z$, while a transient realization prunes to its accepted-loop diagonal. Exact controls through 4096 confirm bare-clone failure, matched-clone equality, composite and pseudoprime rejection, and universal-compiler replication. Thus source-natural addition escapes multiplicative indistinguishability but not matched-clone, pruning, or entropy-clock obstructions. Route A is rejected, Route B remains locked, and the terminal semiring-verifier branch is closed.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Wilson Semiring Verifiers in Symbolic Dynamics:\
  Matched-Clone, Pruning, and Clock-Dilution Obstructions
```

## Markdown 正文

# Introduction {#sec:introduction}

Multiplicative structure alone cannot distinguish the positive integers from a transported free-commutative monoid. In the finite-full-shift setting, Paper 30 makes this obstruction exact: divisibility, finite joins, incidence Möbius data, compatible cutoffs, entropy roofs, Gram kernels, and any natural functional built from those decorations are copied by a formal UFD clone. The result closes a broad family of local and nonlocal selectors. It also leaves a precise opening. A source operation that is not determined by the multiplicative monoid may invalidate the clone.

Alphabet sum is the smallest such operation. If $F_n$ denotes the full shift on an $n$-letter alphabet, disjoint union of alphabets and Cartesian product give $$F_m\boxplus F_n\cong F_{m+n},
  \qquad
  F_m\boxtimes F_n\cong F_{mn}.$$ The two operations recover the nonnegative-integer semiring, while entropy recovers the cardinality norm. Semiring structures on dynamical objects and categorical formulations of symbolic dynamics are established themes [@SaloTorma2015; @NaquinGadouleau2024]. Here they are used as a falsification device: does addition--multiplication compatibility yield an arithmetic recurrence that the multiplicative clone cannot reproduce?

There is an immediate positive answer and an equally immediate limitation. Paper 30's monomial map $\Phi(n)=\prod_p x_p^{v_p(n)}$ preserves multiplication. It cannot preserve integer addition using ordinary polynomial addition, since $\Phi(1+1)=x_2$ but $\Phi(1)+\Phi(1)=2$. The old bare clone is genuinely broken. However, a relabeling $F_n\mapsto y_n$ equipped with transported operations $y_m\oplus_Yy_n=y_{m+n}$ and $y_m\otimes_Yy_n=y_{mn}$ is an isomorphic semiring source. It copies every isomorphism-natural construction. The new operation therefore separates a specific control presentation, not all transported clones.

Congruence supplies the cleanest exact stress test. Starting from $r_{n,1}=1$, the local recurrence $$r_{n,k+1}\equiv r_{n,k}(k+1)\pmod n$$ reaches $(n-1)!\bmod n$. Closing a graph block when the terminal residue is $n-1$ gives one simple primitive cycle of length $p-1$ for each prime $p$. Automata-theoretic prime recognition and computation embedded in symbolic dynamics have a long history [@HartmanisShank1968; @Kurka1997]; the claim here is not a new primality algorithm. Wilson's congruence is chosen because it makes the source relation, orbit census, graph time, and entropy time simultaneously exact.

The exact orbit product exposes the obstruction. If the total roof of the $p$-cycle is $h(F_p)=\log p$, then one traversal has weight $p^{-s}$ and graph-step marker $z^{p-1}$. The primitive product is $$D_{\mathrm W}(s,z)=\prod_p(1-z^{p-1}p^{-s}).$$ At $z=1$ this is the Euler product for $1/\zeta(s)$ in $\operatorname{Re}s>1$. Nevertheless, the whole recurrent vertex adjacency is noncompact. A cycle has $p-1$ edges but only $\log p$ total roof, so some edge has weight at least $p^{-\operatorname{Re}(s)/(p-1)}\to1$. Those near-isometric edges lie in mutually orthogonal blocks. The formal periodic product is therefore not an ordinary Fredholm determinant of the primary operator.

Two repairs reproduce earlier failure modes. First return contracts a $p-1$-step cycle to the trace-class diagonal entry $p^{-s}$, but it changes $z^{p-1}$ to $z$. A transient trace-class verifier also yields the prime diagonal, yet its acyclic computation occurs in no closed walk and prunes from every power trace. The state expansion/return-time distinction is classical [@ParrySullivan1975], and the ordinary infinite-determinant claim requires trace-class ownership [@Simon1977]. Equality after setting $z=1$ cannot erase either boundary.

This paper makes four scoped contributions.

1.  It proves that alphabet sum reconstructs the full-shift characteristic-zero semiring and invalidates the exact bare monomial UFD clone used in Paper 30.

2.  It gives the mandatory matched-semiring control and proves that this clone transports successor, congruence, Wilson states, cycles, roofs, and markers term by term.

3.  It constructs the stationary Wilson graph, proves its complete prime-cycle census, and derives the marked formal product without a prime table.

4.  It separates formal periodic data from operator ownership: the whole recurrent operator is noncompact, first return changes time, and transient verification prunes to a diagonal core. Universal total-decider controls show that the analytic architecture is support-generic.

The conclusion is negative but sharper than Paper 30. Source-natural addition does escape multiplicative indistinguishability. It does not create a noncompiled prime recurrence. Under the frozen information boundary, the first exact terminal congruence witness falls into a matched-clone, transient-pruning, or recurrent clock-dilution alternative. This yields the strict route record $$(\mathrm{A0}_{\rm structural},\mathrm{A1}_{\rm pass},
   \mathrm{A2}_{\rm fail},\mathrm{A3}_{\rm fail},
   \mathrm{A4}_{\rm fail}),$$ rejects Route A, locks Route B, and closes the terminal semiring-verifier branch.

# Source and literature boundary {#sec:source-literature}

## Finite-full-shift semiring skeleton

Let $A_n$ be an alphabet with $n$ elements and set $$F_n=(A_n^{\mathbb Z},\sigma_n),\qquad n\geq0,$$ with $F_0$ the empty system. We work with conjugacy classes. Alphabet sum and alphabet product are $$F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n},
  \qquad
  F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn}.$$ The word *alphabet-sum* matters. The operation is not asserted to be a categorical coproduct in the category of subshifts and block maps; categorical structures in symbolic dynamics require more careful choices [@SaloTorma2015]. The source norm and roof are $$\mathcal N(F_n)=e^{h(F_n)}=n,
  \qquad h(F_n)=\log n\quad(n\geq1).$$ The additive successor is $S(F_n)=F_n\boxplus F_1$, and its iterates generate the source order used for quotient and remainder.

Full shifts also have a separate direct-product primeness theory [@Kopra2023]. Paper 31 does not identify prime alphabet cardinality with a newly discovered symbolic notion. The semiring skeleton is used only to derive integer arithmetic from source operations and to test the naturality of a stationary verifier.

## Four neighboring literatures

#### Symbolic zeta functions.

Finite-state shift zeta functions and determinant identities go back to @BowenLanford1970. Countable-state thermodynamic formalism requires recurrence and summability hypotheses that are absent from a bare finite-block calculation [@GurevichSavchenko1998; @Sarig1999]. Renewal systems further show how flexible code-based zeta functions can be [@Hong2011]. These sources support the formal periodic context; none licenses an ordinary determinant for the noncompact Wilson adjacency.

#### Computation and prime recognition.

Prime recognition by automata is classical [@HartmanisShank1968], and register machines already realize broad classes of recursive computations [@ShepherdsonSturgis1963]. Topological and symbolic dynamical systems can encode computation and universality [@Kurka1997; @DelvenneKurkaBlondel2006]. Consequently, a graph that computes a prime predicate is not by itself an arithmetic-dynamical contribution. The relevant question is whether the computation changes primitive recurrence and operator ownership.

#### Semirings of dynamics.

Addition and product of finite dynamical systems support a nontrivial factorization theory [@NaquinGadouleau2024]. Recent work extends this language to formal sums and injective partial transformations [@GadouleauJohnson2026]. Paper 31 uses a narrower full-shift source and does not claim the semiring viewpoint as new. Its contribution is the exact comparison between the bare multiplicative clone, the matched semiring clone, and the resulting analytic failure modes.

#### State expansion and operator determinants.

State expansion changes discrete graph time even when it preserves an unmarked flow invariant [@ParrySullivan1975]. Weighted shifts on directed trees provide a general operator-theoretic setting for graph weights [@JablonskiJungStochel2012], while infinite weighted-graph zeta functions require their own hypotheses [@Deitmar2015]. Ordinary Hilbert-space Fredholm determinants belong to trace-class perturbations [@Simon1977]. We therefore track the free marker $z$, state the operator space explicitly, and distinguish raw adjacency, first return, and transient replacement.

## Nearest collisions and bounded novelty

The nearest prior constructions are internal. Paper 19 proves that a trace-class semiring verifier can carry the Euler determinant while all transient arithmetic prunes to the atom diagonal. Paper 20 proves the exact compactness criterion for disjoint weighted cycles, entropy-clock dilution, first-return marker change, and a universal total-decider control. Those results are inherited, not renamed.

To our knowledge, based on the primary-source searches recorded in `LITERATURE_AUDIT.md` and completed on 2026-08-14, no external paper found in that search combines the specific Paper-30 bare-clone separation, matched-semiring transport, Wilson graph-step product, and whole-operator compactness trichotomy. This is a search-bounded positioning statement. It does not assert the absence of every equivalent formulation.

## Functional and data conventions

The candidate may use the source semiring, equality, quotient/remainder, congruence, entropy, exact arithmetic, and deterministic cutoffs. It may not read a prime, prime-power, factor, atom-color, orbit-projector, or target-zero table. Target-zero ordinates, root matching, and post-control fitting are excluded. A matched isomorphic relabeling is a mandatory control. Formal periodic products, ordinary traces, Fredholm determinants, and induced return operators remain different functional types throughout.

# Bare-clone separation and matched-clone collapse {#sec:semiring-clones}

[\[thm:additive-reconstruction\]]{#thm:additive-reconstruction label="thm:additive-reconstruction"} Let $S$ be a commutative semiring with zero and unit. Assume every element of $S$ equals $n\cdot1$ for some $n\in\mathbb N_0$, and assume $n\cdot1=m\cdot1$ only when $n=m$. Then $$\iota:\mathbb N_0\longrightarrow S,
  \qquad n\longmapsto n\cdot1,$$ is a semiring isomorphism.

Additive generation makes $\iota$ surjective, and the characteristic-zero assumption makes it injective. Concatenating sums of the unit gives $\iota(m+n)=\iota(m)+\iota(n)$. Distributivity gives $$\iota(m)\iota(n)=(m\cdot1)(n\cdot1)=mn\cdot1=\iota(mn).$$ The map also preserves zero and unit.

The map $n\mapsto[F_n]$ identifies the alphabet-sum/product skeleton of finite full shifts with $\mathbb N_0$ as a commutative semiring.

The alphabet operations reproduce cardinality addition and multiplication, and repeated alphabet sum of $F_1$ produces every $F_n$. Distinct positive indices have distinct entropy $\log n$, so the characteristic-zero assumption holds. The zero object is separate.

The theorem isolates what Paper 30 did not see. Its decorated source retained the multiplicative monoid and incidence structure. Alphabet sum fixes the additive generator and reconstructs the indices themselves. This enrichment is independently motivated by the full-shift alphabets, rather than by a supplied prime predicate.

[\[prop:bare-clone\]]{#prop:bare-clone label="prop:bare-clone"} Let $M$ be the monomial submonoid of $\mathbb Z[x_p:p\text{ prime}]$, and let $$\Phi(n)=\prod_p x_p^{v_p(n)}.$$ Ordinary polynomial addition does not restrict to a semiring operation on $M$ that extends $\Phi$.

Any extension would require $$x_2=\Phi(2)=\Phi(1+1)=\Phi(1)+\Phi(1)=1+1=2,$$ which is false in the polynomial ring. Equivalently, the monic monomial submonoid is not closed under ordinary addition.

This contradiction is enough to discharge the immediate Paper-30 obligation. It is not enough to claim that addition identifies a literal integer presentation. A natural invariant must survive isomorphic transport of its entire source language.

[\[prop:matched-clone\]]{#prop:matched-clone label="prop:matched-clone"} Let $Y=\{y_n:n\in\mathbb N_0\}$ and define $$y_m\oplus_Yy_n=y_{m+n},
  \qquad
  y_m\otimes_Yy_n=y_{mn}.$$ Transport successor, order, quotient/remainder, congruence, entropy, Wilson states, edge roofs, and graph-step markers through $F_n\mapsto y_n$. The resulting decorated source is isomorphic to the full-shift source. Every isomorphism-natural Wilson path, cycle, marked trace ledger, and periodic product agrees term by term.

Both displayed operations commute with the relabeling by definition. Source equality and successor order also transport. Quotient and remainder are defined by semiring equations and the successor bounds, so uniqueness carries them to $Y$. Induction over the Wilson recurrence then transports every residue state and edge. The edge words, return times, roofs, and markers are therefore identical.

The matched clone is not an adversarial exception to be excluded. Its exact agreement is the expected consequence of functoriality. The distinction in [\[fig:semiring-clone-boundary\]](#fig:semiring-clone-boundary){reference-type="ref" reference="fig:semiring-clone-boundary"} is therefore the paper's first firewall: alphabet sum breaks the *bare* multiplicative control, while the matched clone fixes the remaining naturality boundary.

Arbitrary semiring controls clarify the scope. Boolean and finite modular semirings collapse the unbounded successor chain. Polynomial semirings have elements not additively generated by the unit. Tropical addition is idempotent. A randomly relabeled finite modular semiring can pass every finite semiring identity and still fail characteristic zero. The source is selected by explicit axioms, not by the spelling of its elements.

# The stationary Wilson grammar {#sec:wilson-grammar}

## Source-derived congruence

For $n\geq2$, define $F_a\equiv_nF_b$ when $a$ and $b$ have the same least remainder modulo $n$. Internally, the remainder $F_r$ is characterized by $$F_a\cong(F_q\boxtimes F_n)\boxplus F_r,
  \qquad 0\preceq_+F_r\prec_+F_n.$$ The source order generated by $F_1$ gives existence and uniqueness. No factorization is needed. The prototype uses integer remainder only as the exact implementation of this semiring quotient scan.

For every $n\geq2$, set $$r_{n,1}=1,
  \qquad
  r_{n,k+1}\equiv r_{n,k}(k+1)\pmod n,
  \qquad1\leq k\leq n-2,$$ with $0\leq r_{n,k}<n$. Induction gives $r_{n,k}=k!\bmod n$.

## One graph for all moduli

The stationary countable graph $G_{\mathrm W}$ has vertices $$v_{n,k}=(F_n,F_k,F_{r_{n,k}}),
  \qquad n\geq2,\quad1\leq k\leq n-1,$$ and deterministic edges $v_{n,k}\to v_{n,k+1}$ for $k<n-1$. At the terminal state, an edge returns to $v_{n,1}$ precisely when $$F_{r_{n,n-1}}\cong F_{n-1}.$$ Otherwise the block has no recurrent return. This is a single graph rule for all moduli, not a family selected from a prime list.

Let $V_{\mathrm{rec}}(G_{\mathrm W})$ be the vertices on recurrent bi-infinite components. The primary operator will act on $\ell^2(V_{\mathrm{rec}}(G_{\mathrm W}))$. Rejected finite paths are presentation scaffolding. They do not enter the primary recurrent operator, and they are treated separately in the transient comparison of [7](#sec:transient-controls){reference-type="ref" reference="sec:transient-controls"}.

[\[thm:wilson-cycles\]]{#thm:wilson-cycles label="thm:wilson-cycles"} For every $n\geq2$, the $n$-block of $G_{\mathrm W}$ is recurrent if and only if $n$ is prime. A recurrent block is one oriented simple primitive cycle $\Gamma_p$ of graph length $p-1$, up to cyclic rotation.

The recurrence gives $r_{n,n-1}\equiv(n-1)!\pmod n$. If $p$ is prime, the nonzero residues form a group. Pair every residue with its inverse. A self-inverse residue satisfies $(a-1)(a+1)=0$ in the field $\mathbb Z/p\mathbb Z$, so only $1$ and $-1$ remain unpaired; for $p=2$ they coincide. Therefore $(p-1)!\equiv-1\pmod p$, and the terminal edge closes.

Conversely, $3!=6\equiv2\pmod4$, so $n=4$ does not close. If a nonsquare composite $n>4$ is written $n=ab$ with $2\leq a<b\leq n-2$, both distinct factors occur in $(n-1)!$, hence $n\mid(n-1)!$. If $n=a^2$ with $a\geq3$, the distinct factors $a$ and $2a\leq a^2-1$ occur, hence $a^2\mid(n-1)!$. Every composite $n>4$ has terminal residue zero rather than $n-1$. In a closed block, the $k$ coordinate distinguishes the $p-1$ visited states, so the deterministic cycle is simple and primitive.

[\[cor:prime-powers\]]{#cor:prime-powers label="cor:prime-powers"} Assign nonnegative edge roofs on $\Gamma_p$ with total $\log p$. The $r$-fold temporal repetition has total roof $r\log p$ and weight $p^{-rs}$. It does not create a second primitive orbit indexed by the integer $p^r$.

The theorem is exact, but its mechanism is terminal. The return edge is present exactly after evaluating a congruence equivalent to primality. The graph is table-free and source-derived, yet the periodic decision is still a Boolean conclusion at the end of a finite computation. This distinction is why an exact orbit census can pass while arithmetic selectivity remains selector-tautological.

# The marked periodic ledger {#sec:periodic-product}

Put a nonnegative roof $\tau(e)$ on each edge of $\Gamma_p$ and impose the source-clock identity $$\sum_{e\in\Gamma_p}\tau(e)=h(F_p)=\log p.$$ On $\ell^2(V_{\mathrm{rec}}(G_{\mathrm W}))$, the recurrent weighted successor is defined on the vertex basis by $$L_s\delta_{s(e)}=e^{-s\tau(e)}\delta_{t(e)}.$$ For $\operatorname{Re}s\geq0$ this is a bounded direct sum of finite cyclic weighted shifts. The uniform representative has $$\tau_{p,k}=\frac{\log p}{p-1},\qquad
  L_s|_{\Gamma_p}=p^{-s/(p-1)}P_{p-1},$$ where $P_{p-1}$ is the cyclic permutation matrix.

The next definition records closed walks without asserting an operator trace.

For $r\geq1$, set $$\operatorname{Tr}_{\mathrm{per}}(L_s^r)
  :=\sum_{v\in V_{\mathrm{rec}}(G_{\mathrm W})}
  \langle L_s^r\delta_v,\delta_v\rangle,$$ whenever the displayed basis-diagonal sum has finite support. The subscript "per" distinguishes this ledger from the Hilbert-space trace.

[\[prop:periodic-ledger\]]{#prop:periodic-ledger label="prop:periodic-ledger"} For every $r\geq1$ and every exact-clock allocation, $$\operatorname{Tr}_{\mathrm{per}}(L_s^r)
  =\sum_{p-1\mid r}(p-1)p^{-sr/(p-1)}.$$ In particular, the sum contains only finitely many terms.

The $p$-block returns a vertex to itself after $r$ graph steps exactly when $p-1$ divides $r$. Writing $r=m(p-1)$, a closed walk makes $m$ complete turns and has weight $$\left(\prod_{e\in\Gamma_p}e^{-s\tau(e)}\right)^m
  =e^{-sm\log p}=p^{-sm}.$$ There are $p-1$ possible starting vertices. Finally, $p-1\mid r$ implies $p\leq r+1$, proving finite support.

The finiteness is combinatorial: each fixed graph power sees only cycles with length at most that power. It does not imply that $L_s^r$ is trace class.

[\[prop:marked-product\]]{#prop:marked-product label="prop:marked-product"} For $\operatorname{Re}s\geq0$ and $|z|<1$, define from the absolutely convergent periodic trace-log $$D_{\mathrm W}(s,z):=\exp\!\left(
    -\sum_{r\geq1}\frac{z^r}{r}\operatorname{Tr}_{\mathrm{per}}(L_s^r)\right).$$ Then, as a periodic-orbit identity, $$D_{\mathrm W}(s,z)=\prod_p\left(1-z^{p-1}p^{-s}\right).$$ The product on the right converges normally on compact subsets of $\mathbb C\times\{z:|z|<1\}$ and thereby extends the trace-log definition in $s$. At $z=1$ and $\operatorname{Re}s>1$, $$D_{\mathrm W}(s,1)=\prod_p(1-p^{-s})=\zeta(s)^{-1}.$$

For $\operatorname{Re}s\geq0$ and $|z|<1$, insert [\[prop:periodic-ledger\]](#prop:periodic-ledger){reference-type="ref" reference="prop:periodic-ledger"}, use absolute convergence, and write $r=m(p-1)$. The exponent contributed by one prime is $$-\sum_{m\geq1}\frac{z^{m(p-1)}}{m}p^{-sm}
 =\log\left(1-z^{p-1}p^{-s}\right).$$ For the extension, let $|z|\leq\rho<1$ and let $s$ range over a compact set with $\operatorname{Re}s\geq-M$. The factor increment is bounded by $\rho^{p-1}p^M$. The latter is summable even when summed over all positive integers, so the Weierstrass criterion gives normal convergence of the product. Equality on $\operatorname{Re}s\geq0$ and the identity theorem give the stated continuation. At $z=1$, absolute Euler-product convergence holds in $\operatorname{Re}s>1$.

The factor $z^{p-1}$ is not decoration: it owns the original graph clock. Although the specialization at $z=1$ is the reciprocal Euler product, the identity in [\[prop:marked-product\]](#prop:marked-product){reference-type="ref" reference="prop:marked-product"} does not license the notation $\det(I-zL_s)$. The operator required by that notation fails even compactness, as the next section proves.

# Clock dilution and first-return ownership {#sec:clock-return}

The same exact source clock that gives the desired return weight forces a large-edge obstruction. The conclusion does not depend on uniform roofs.

[\[thm:noncompact\]]{#thm:noncompact label="thm:noncompact"} Suppose $\tau(e)\geq0$ on every edge and $\sum_{e\in\Gamma_p}\tau(e)=\log p$. For every $s$ with $\sigma=\operatorname{Re}s>0$, the primary recurrent adjacency $L_s$ on $\ell^2(V_{\mathrm{rec}}(G_{\mathrm W}))$ is noncompact. Consequently $L_s\notin\mathcal S_q$ for every finite $q\geq1$, and it owns no ordinary trace-class Fredholm determinant.

Choose on each $\Gamma_p$ an edge $e_p$ of minimum roof. Since the block has $p-1$ edges, $$\tau(e_p)\leq\frac{\log p}{p-1},\qquad
  |e^{-s\tau(e_p)}|
  \geq p^{-\sigma/(p-1)}\longrightarrow1.$$ Let $\delta_p$ be the basis vector at the source of $e_p$. The vectors $\delta_p$ are orthonormal, hence weakly null, and their images lie in mutually orthogonal prime blocks with norms that do not tend to zero. A compact operator must send a weakly null bounded sequence to a norm-null sequence. This contradiction proves noncompactness. Every finite Schatten-class operator is compact.

The argument gives the exact design condition for the entire class of vertex-disjoint cyclic successors.

[\[cor:length-criterion\]]{#cor:length-criterion label="cor:length-criterion"} Consider finite directed cycles of lengths $\ell_n$ with nonnegative edge roofs totaling $T_n$. For fixed $\sigma>0$, there exists an allocation for which the direct-sum weighted successor is compact if and only if $$\frac{T_n}{\ell_n}\longrightarrow\infty.$$ Thus a prime-indexed disjoint successor with $T_p=\log p$ requires $\ell(p)=o(\log p)$; an $O(\log p)$ bound is insufficient.

For necessity, compactness forces the largest edge modulus in the $n$th block to tend to zero. This modulus is determined by a minimum-roof edge, so its roof tends to infinity; the average roof $T_n/\ell_n$ is at least that minimum and also tends to infinity. Conversely, allocate the roof uniformly. Every block norm is then $e^{-\sigma T_n/\ell_n}\to0$. A direct sum of finite-dimensional operators whose norms tend to zero is compact.

Uniform roofs make the spectral accumulation explicit.

[\[cor:essential-circle\]]{#cor:essential-circle label="cor:essential-circle"} For the uniform Wilson allocation and every $s$ with $\operatorname{Re}s>0$, every point of the unit circle admits an orthonormal approximate-eigenvector sequence for $L_s$. In particular, the unit circle lies in the essential approximate point spectrum.

The eigenvalues in the $p$-block are $$\lambda_{p,j}=p^{-s/(p-1)}
  \exp\!\left(\frac{2\pi i j}{p-1}\right),
  \qquad0\leq j<p-1.$$ Their radii tend to one, their additional phase from $\Im s$ tends to zero, and their angular mesh tends to zero. Given $|\lambda|=1$, choose eigenvalues from distinct prime blocks converging to $\lambda$. The corresponding normalized block eigenvectors are orthogonal and satisfy $\|(L_s-\lambda)u_p\|\to0$.

This circle is a noncompactness witness, not a Hilbert--Pólya spectrum. It has no asserted relation to the nontrivial zeros of $\zeta$.

## First return: an honest determinant of another clock

Choose one base vertex $b_p$ on each prime cycle and induce to the base set. The first-return operator acts on $\ell^2(\{b_p\})$.

[\[thm:first-return\]]{#thm:first-return label="thm:first-return"} The induced operator is diagonal, $$R_sb_p=p^{-s}b_p.$$ It is trace class exactly when $\operatorname{Re}s>1$, and in that half-plane $$\det(I-zR_s)=\prod_p(1-zp^{-s}).$$ The raw and induced factors are respectively $1-z^{p-1}p^{-s}$ and $1-zp^{-s}$. Hence the induced determinant does not preserve the free graph-step marker.

One first return multiplies every edge weight around $\Gamma_p$, giving $e^{-s\log p}=p^{-s}$. Its trace norm is $\sum_p p^{-\sigma}$, finite exactly for $\sigma>1$. The standard diagonal Fredholm product follows in that region. A return traverses $p-1$ original edges but is one induced step, which proves the marker statement.

At $z=1$ the products agree in the Euler half-plane. That equality forgets the coordinate which distinguishes the two time evolutions. State expansion and return-time changes are familiar in symbolic dynamics [@ParrySullivan1975]; here the free marker turns the distinction into an exact finite certificate, while trace-class theory fixes which object owns the ordinary determinant [@Simon1977].

# Transient pruning and universal controls {#sec:transient-controls}

A second repair moves the computation into feed-forward states. It can be made trace class, but then the verification never participates in a closed walk. This is the pruning alternative.

For each input $n$, let a finite deterministic DAG compute the terminal Wilson relation and feed an accept vertex. Put a loop of weight $n^{-s}$ on that vertex precisely when it accepts. Multiply the DAG and feed edges by a fixed summable regulator so that their direct-sum operators are trace class. On accepted-loop and transient subspaces the full operator has the form $$T_s=\begin{pmatrix}
      D_s&B_s\\[2pt]
      0&Q_s
    \end{pmatrix},
  \qquad D_s=\mathop{\mathrm{diag}}_{p}(p^{-s}),$$ where $Q_s$ is the regulated acyclic part.

[\[prop:transient-pruning\]]{#prop:transient-pruning label="prop:transient-pruning"} Assume $Q_s$ and $B_s$ are trace class. For $\operatorname{Re}s>1$, $T_s$ is trace class and $$\operatorname{Tr}(T_s^r)=\sum_p p^{-sr},\qquad
  \det(I-zT_s)=\prod_p(1-zp^{-s}).$$ Deleting all verifier-DAG states preserves every power trace and the Fredholm determinant.

Order the vertices of every finite DAG topologically. No positive-length closed walk uses a DAG edge, so every basis-diagonal coefficient of $Q_s^r$ vanishes. Since $Q_s^r$ is trace class, its trace is the sum of these diagonal coefficients and is zero. The countable direct sum need not be globally nilpotent; acyclicity, not a nonexistent uniform nilpotence index, is the relevant fact.

Block triangularity gives $$\operatorname{Tr}(T_s^r)
  =\operatorname{Tr}(D_s^r)+\operatorname{Tr}(Q_s^r)
  =\sum_p p^{-sr}.$$ The trace-log identity near $z=0$, followed by analytic continuation of the entire Fredholm determinants, gives $$\det(I-zT_s)=\det(I-zD_s)\det(I-zQ_s)
  =\prod_p(1-zp^{-s}).$$ The same formula remains after deleting the transient block and feed edges.

Thus the honest determinant belongs to the accepted-loop diagonal. The Wilson computation supplies which loops are installed but contributes no periodic term after installation. Calling this a dynamical Wilson cancellation would confuse an algorithm that populates a support with the closed-walk mechanism that owns its determinant.

[\[cor:universal-decider\]]{#cor:universal-decider label="cor:universal-decider"} Let $P:\mathbb N\to\{0,1\}$ be any total decidable predicate. Replacing the Wilson DAG by a terminating computation of $P$ and installing the loop exactly when $P(n)=1$ produces the same pruning identity. If instead the accepted computations are closed into vertex-disjoint cycles of lengths $\ell_P(n)$ and exact total roofs $\log n$, the recurrent operator has the same minimum-roof obstruction whenever $\log n/\ell_P(n)$ fails to diverge along an unbounded accepted subsequence.

The exact controls instantiate the compiler for Wilson primes, squares, powers of two, Fibonacci numbers, and a seeded computable support. These supports have different arithmetic meanings; the point is that their terminal analytic wrappers are identical. The architecture therefore proves too much at the compiler level.

The three outcomes in [\[fig:verifier-trichotomy\]](#fig:verifier-trichotomy){reference-type="ref" reference="fig:verifier-trichotomy"} are mutually compatible. The matched clone defeats presentation selectivity, the transient model loses the computation from recurrence, and the recurrent model retains the computation only by diluting $\log p$ across $p-1$ disjoint steps. Neither repair supplies an honest determinant of the original Wilson adjacency with its original marker.

# Exact audit and adversarial controls {#sec:exact-audit}

The infinite claims above are proofs. The finite experiment is a separate implementation audit: it verifies every serialized residue path, exercises the clone and compiler controls, and checks exact marker ownership. Candidate code uses the semiring recurrence only. A physically separate evaluator recomputes paths, implements trial division for evaluation, regenerates the control tables, and checks artifact hashes without importing the candidate core.

## Cutoff census

The frozen cutoff is $4096$. All arithmetic comparisons use integers or exact rational numbers; floating-point values are display witnesses and decide no gate.

\@L47mmrY@ Surface & Count & Exact outcome\
Candidate integers $2\leq n\leq4096$ & 4,095 & every residue path and cycle length independently verified\
Accepted cycles & 564 & exactly the primes; largest accepted value $4093$\
Composite controls & 3,531 & every composite rejected\
Base-2 Fermat pseudoprimes & 13 & all rejected, including $341,561,1729,2047$\
Bare-UFD addition pairs & 144 & $0/144$ ordinary-addition matches\
Matched-clone operation rows & 169 & $169/169$ equal; all Wilson paths copied\
Named semiring controls & 7 & only the baseline and matched clone pass the full source lock\
Operation-table controls & 33 & $0/32$ random magma pairs pass; the matched $\mathbb Z/11\mathbb Z$ relabel passes\
Entropy-budget rows & 1,692 & 564 cycles at $\sigma=1,2,3$\
Formal trace orders & 16 & every periodic contribution list finite\
Universal wrapper families & 5 & every transient wrapper prunes; every unbounded recurrent wrapper dilutes\
Source-separated evaluator checks & 26,620 & $26{,}620/26{,}620$ pass\
Regression tests & 18 & $18/18$ pass\

The named controls separate failure of an axiom from failure of an algorithm. The Boolean semiring and $\mathbb Z/11\mathbb Z$ have finite characteristic; $\mathbb N[t]$ is not additively generated by its unit; tropical addition is idempotent; bare monomials are not closed under ordinary addition. A random relabeling of $\mathbb Z/11\mathbb Z$ passes the finite semiring identities but still fails characteristic zero and unbounded successor. Printed labels therefore play no role in the source lock.

## Two exact analytic certificates

At the largest accepted cutoff value and $\sigma=2$, every nonnegative exact-clock allocation has an edge of modulus at least $$4093^{-2/4092}=0.99594322976540206.$$ This finite row illustrates the lower bound in [\[thm:noncompact\]](#thm:noncompact){reference-type="ref" reference="thm:noncompact"}; the limit proof, not this decimal, establishes noncompactness.

For the marker audit, let the product range over $p\leq31$ and put $s=2$. At $z=1$, both raw and induced products equal the exact rational number $$\frac{50722704772300800}{82920037520482019}.$$ At $z=1/3$, exact rational arithmetic gives $$\prod_{p\leq31}\left(1-\frac{(1/3)^{p-1}}{p^2}\right)
  \neq
  \prod_{p\leq31}\left(1-\frac{1}{3p^2}\right).$$ Thus equality after erasing graph time is verified, and free-marker inequality is also verified, without numerical root finding.

The authority generator reproduces the 14 frozen prototype payloads semantically exactly, with JSON byte equality and CSV equality after the sole CRLF-to-LF normalization. Two fresh isolated authority runs produce the same 16 core result artifacts byte for byte, with aggregate SHA-256 `c0be3f65d26d655aba06343766c734f19da3349b29cf4f0d731bba23fc33a449`. Neither run reads target-zero data.

## What the audit can and cannot establish

Composite and pseudoprime rejection validate the Wilson implementation; they do not make its terminal predicate non-tautological. Bare-clone failure validates the precise escape from Paper 30; matched-clone equality supplies the stronger naturality boundary. Exact power ledgers validate [\[prop:periodic-ledger\]](#prop:periodic-ledger){reference-type="ref" reference="prop:periodic-ledger"}; they are not ordinary traces. Finally, the five support families validate the generality of [\[cor:universal-decider\]](#cor:universal-decider){reference-type="ref" reference="cor:universal-decider"}; they do not identify the arithmetic meanings of those supports.

# Route evaluation and branch closure {#sec:route-closure}

The candidate succeeds at the source and primitive-orbit layers and fails at same-object determinant ownership. The distinction is encoded in the frozen Route-A record $$\boxed{(
\texttt{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
\texttt{A1\_PASS\_ANALYTIC},
\texttt{A2\_FAIL},
\texttt{A3\_FAIL},
\texttt{A4\_FAIL})}.$$

#### A0: structural arithmetic relation.

Alphabet sum and product reconstruct $\mathbb N_0$, and source-derived congruence implements Wilson's relation without a prime table. The bare multiplicative clone is broken. The verdict is structural rather than analytic because the matched semiring clone copies the complete construction.

#### A1: analytic primitive-orbit pass.

The one-cycle-per-prime theorem is complete, temporal repetitions have the correct $p^{-rs}$ weights, and the free-marker product converges normally for $|z|<1$. The "analytic" label applies to this proved primitive-orbit function, not to an ordinary trace of $L_s$.

#### A2: same-object determinant failure.

The primary recurrent adjacency is noncompact under every allowed roof allocation. Its formal product is not its Fredholm determinant. First return owns an honest determinant only after changing $p-1$ graph steps to one, and the transient comparison owns only the pruning-equivalent accept diagonal.

#### A3 and A4: no completion or spectral carrier.

There is no owned determinant continued to the critical line, Gamma completion, functional equation, intrinsic Weil compression, fixed self-adjoint carrier, critical-line mechanism, or zero correspondence. Because A4 fails, Route B is not invocable.

It follows that the overall verdict is $$\texttt{ROUTE\_A\_REJECTED},\qquad
  \texttt{ROUTE\_B\_LOCKED},$$ and the research action is $$\texttt{CLOSE\_TERMINAL\_SEMIRING\_VERIFIER\_BRANCH}.$$ This closure covers terminal/feed-forward total verifiers and vertex-disjoint recurrent verifier cycles with nonnegative exact source roofs. Replacing Wilson's theorem by another terminal primality test does not reopen it.

The conclusion is deliberately not universal. It does not rule out a source-derived grammar in which arithmetic branches overlap and interact recurrently before any Boolean decision; nor does it analyze signed, supersymmetric, or homological cancellations. Such a candidate starts with no inherited A2 credit. It must prove compactness or an honest determinant for its uninduced whole operator, preserve the original free marker, and pass matched-clone and universal-wrapper controls before any critical-line claim.

# Conclusion {#sec:conclusion}

Alphabet sum is a genuine post-Paper-30 advance: it reconstructs additive arithmetic from finite-full-shift source operations and invalidates the exact bare monomial UFD clone. Wilson congruence then gives a table-free stationary grammar with one primitive cycle per prime, exact prime-power repetitions, and a normally convergent marked periodic product.

The advance stops before a spectral mechanism. A matched semiring relabel copies the entire construction. Keeping the Wilson computation recurrent spreads the entropy clock $\log p$ across $p-1$ disjoint edges and forces a noncompact whole operator. Inducing restores trace class only by changing graph time, while a feed-forward implementation deletes the computation from all periodic traces. These are exact ownership obstructions, not failures of finite accuracy.

Accordingly, SD-C33 is retained as a negative closure theorem rather than a positive Hilbert--Pólya candidate. The next admissible test is concrete: construct a source-derived, nonterminal, overlapping recurrent grammar whose arithmetic transition algebra changes before acceptance is known, and prove an honest determinant for the uninduced operator while retaining its original marker. Until that obligation is met, the terminal semiring-verifier branch remains closed.

# Supplementary proof details {#app:proof-details}

## Source quotient and transport

The successor relation used in [4](#sec:wilson-grammar){reference-type="ref" reference="sec:wilson-grammar"} is $F_a\preceq_+F_b$ when $F_b\cong F_a\boxplus F_c$ for some $c$. Additive reconstruction makes this the usual order on indices. For $a,n\in\mathbb N_0$ with $n>0$, repeated successor comparison produces unique $q,r$ satisfying $$F_a\cong(F_q\boxtimes F_n)\boxplus F_r,
  \qquad F_0\preceq_+F_r\prec_+F_n.$$ Existence is the finite subtraction algorithm; if two pairs existed, the semiring isomorphism of [\[thm:additive-reconstruction\]](#thm:additive-reconstruction){reference-type="ref" reference="thm:additive-reconstruction"} would give two Euclidean divisions of $a$ by $n$. This description uses addition, multiplication, equality, and successor order, not factorization.

Under $F_n\mapsto y_n$, the same equations and bounds have the same unique solutions. Consequently each residue update and terminal equality transports. Induction in $k$ gives equality of the full words $(r_{n,1},\ldots,r_{n,n-1})$, not merely equality of the accept/reject bit. This is why the matched-clone control copies paths, roofs, graph lengths, and free markers term by term.

## Normal convergence of the marked product

Fix a compact $K\subset\mathbb C\times\{z:|z|<1\}$. There are $M\geq0$ and $\rho<1$ such that $\operatorname{Re}s\geq-M$ and $|z|\leq\rho$ on $K$. Put $u_p(s,z)=z^{p-1}p^{-s}$. Then $$\sup_K|u_p|\leq\rho^{p-1}p^M,
  \qquad
  \sum_p\sup_K|u_p|<\infty.$$ After removing finitely many factors, $|u_p|\leq1/2$ uniformly, and $|\log(1-u_p)|\leq2|u_p|$. The logarithm series therefore converges uniformly on $K$, giving a holomorphic product there. The same majorant justifies interchanging the prime and repetition sums in [\[prop:marked-product\]](#prop:marked-product){reference-type="ref" reference="prop:marked-product"}. This argument says nothing about trace ideals of $L_s$.

## Compact direct sums and the Wilson obstruction

For a direct sum $A=\bigoplus_n A_n$ of operators on finite-dimensional mutually orthogonal blocks, $A$ is compact exactly when $\|A_n\|\to0$. Sufficiency follows by truncating to finitely many blocks; necessity follows by choosing unit vectors realizing a fixed fraction of any nonvanishing subsequence of block norms. A weighted cyclic successor has block norm equal to the largest edge modulus. Thus compactness forces every minimum roof to diverge, and hence forces the average roof to diverge. The uniform allocation proves the converse in [\[cor:length-criterion\]](#cor:length-criterion){reference-type="ref" reference="cor:length-criterion"}.

For uniform Wilson blocks, the Fourier basis diagonalizes $P_{p-1}$. Given $\lambda\in\mathbb C$ with $|\lambda|=1$, choose $j(p)$ so that the root of unity $e^{2\pi i j(p)/(p-1)}$ approaches $\lambda$. Because $p^{-s/(p-1)}\to1$, the corresponding eigenvalues approach $\lambda$. Their block eigenvectors are orthonormal and converge weakly to zero. This is the singular-sequence formulation used in [\[cor:essential-circle\]](#cor:essential-circle){reference-type="ref" reference="cor:essential-circle"}.

## Return and transient determinant identities

For $\sigma>1$, $R_s=\mathop{\mathrm{diag}}_p(p^{-s})$ has singular values $p^{-\sigma}$. The convergence of $\sum_p p^{-\sigma}$ gives trace class and the standard Fredholm product. For $0<\sigma\leq1$, divergence of the prime reciprocal sum (and comparison for smaller $\sigma$) prevents trace class; for $\sigma\leq0$ the diagonal entries do not even tend to zero. This proves the "exactly" clause in [\[thm:first-return\]](#thm:first-return){reference-type="ref" reference="thm:first-return"}.

For the transient comparison, $Q_s$ is trace class by the declared regulator. Every diagonal matrix element of $Q_s^r$ is a sum over length-$r$ closed walks based at that vertex, and acyclicity makes the sum empty. Hence $\operatorname{Tr}(Q_s^r)=0$. The Fredholm expansion $$\log\det(I-zQ_s)
  =-\sum_{r\geq1}\frac{z^r}{r}\operatorname{Tr}(Q_s^r)$$ first gives $\det(I-zQ_s)=1$ near zero; both sides are entire in $z$, so the identity holds globally. Applying the same expansion to the trace-class block-triangular $T_s$ proves [\[prop:transient-pruning\]](#prop:transient-pruning){reference-type="ref" reference="prop:transient-pruning"} without assuming that the countable DAG direct sum is nilpotent.

# Scope, ownership, and declarations {#app:scope}

## Information boundary

\@Y Y@ Allowed & Forbidden\
Alphabet sum/product, zero, unit, successor order, source equality, quotient/remainder, congruence, and entropy & Supplied prime, prime-power, factor, von Mangoldt, atom-color, orbit-projector, or accepted-support tables\
Exact integer/rational arithmetic, deterministic cutoffs, frozen seeds, and source-separated evaluator trial division & Candidate-side primality/factorization oracles, file/network lookup, or evaluator feedback used to choose closing edges\
Nonnegative source roofs totaling $\log n$, a free graph-step marker, and isomorphic transports of all decorations & Parameter-dependent graphs, post-control roof or marker changes, and transferring induced ownership to the raw graph\
Matched semiring, composite, pseudoprime, arbitrary-semiring, random-table, and universal-decider controls & Target-zero ordinates, root matching, coefficient fitting, Route-B operators, or RH inference\

## Functional ownership

\@L31mmL29mmY Y@ Object & Marker & Analytic status & Ownership verdict\
Recurrent Wilson adjacency $L_s$ & $z^{p-1}$ per return & bounded for $\operatorname{Re}s\geq0$; noncompact for $\operatorname{Re}s>0$ & exact cycles, no ordinary Fredholm determinant\
Formal product $D_{\mathrm W}(s,z)$ & $z^{p-1}$ & normal for $|z|<1$; Euler specialization at $z=1$, $\operatorname{Re}s>1$ & periodic function, not an operator determinant\
First-return $R_s$ & $z$ & trace class exactly for $\operatorname{Re}s>1$ & honest determinant of a changed time object\
Transient verifier $T_s$ & $z$ & trace class under the declared regulator & determinant equals the accepted-loop diagonal after pruning\
Matched semiring clone & copies either marker & copies each analytic status & mandatory naturality control\

## Limitations

The branch theorem covers the frozen Wilson grammar, feed-forward terminal verifiers with trace-class regulators, and vertex-disjoint recurrent cycles with nonnegative exact roofs. It does not classify overlapping recurrent grammars, signed or complex roof cancellation, supertraces, homological weights, or arbitrary semiring enrichments. No determinant of the primary operator, analytic continuation to the critical line, Gamma factor, functional equation, Weil compression, fixed self-adjoint carrier, target-zero correspondence, or implication for the Riemann hypothesis is proved.

## Reproducibility and research declarations

#### Data and code availability.

All candidate code, source-separated evaluation code, exact result ledgers, hash certificates, theorem packages, and LaTeX sources are distributed with the Paper 31 authority directory. The calculation uses no private dataset and no target-zero dataset. Deterministic parameters and commands are frozen in the experiment plan and environment lock.

#### Ethics.

The work uses mathematical proofs and synthetic deterministic computations; it involves no human participants, animals, personal data, or field intervention. Ethics approval and informed consent are not applicable.

#### Author contributions.

The anonymous authors contributed conceptualization, methodology, formal analysis, software, validation, visualization, writing, and artifact curation.

#### Competing interests and funding.

The authors declare no competing interests and no external funding specific to this study.

#### Generative-AI disclosure.

Generative-AI tools assisted with research organization, code and proof drafting, LaTeX preparation, and language editing under author direction. The authors retained responsibility for source verification, exact computation, mathematical claims, and the final manuscript. No automated manuscript review loop was used.
