---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--24-kraft-fredholm-log-code-trilemma"
canonical_tex: "symbolic_dynamics/papers/24-kraft-fredholm-log-code-trilemma/main.tex"
canonical_pdf: "symbolic_dynamics/papers/24-kraft-fredholm-log-code-trilemma/main.pdf"
source_sha256: "021d9d64633f0ac8e31db83f459f7b730e79473e69b3514621fc7691452f863f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Kraft--Fredholm Trilemma for Logarithmic Prime Codes

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/24-kraft-fredholm-log-code-trilemma>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/24-kraft-fredholm-log-code-trilemma/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/24-kraft-fredholm-log-code-trilemma/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/24-kraft-fredholm-log-code-trilemma/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/24-kraft-fredholm-log-code-trilemma/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test whether a finite visible symbolic code can compress the rational-prime Euler ledger into a stationary recurrent graph while retaining an honest whole-space Fredholm operator. The test is deliberately literal: one primitive positive orbit $\gamma_p$ for each rational prime, no additional primitive orbit, total roof $T(\gamma_p)=\log p$, and a finite local code that separates the intended cycles. We prove a Kraft--Fredholm trilemma. Sharing recurrent states creates mixed primitive roots. Separating the cycles makes a finite code logarithmically long on an infinite subsequence; the fixed total roof then leaves uniformly large one-step weights, so the natural graph-coordinate adjacency is noncompact in every positive half-plane. Replacing every codeword by one countable atom loop restores the Euler Fredholm determinant but is precisely the supplied-inventory realization and passes arbitrary controls unchanged. Exact finite audits verify the coding bound, positive-roof obstruction, renewal cycle flood, and graph-step marker mismatch. The result closes this positive scalar compression branch, not signed, matrix-valued, or anisotropic analytic extensions.
author:
- 'Symbolic Dynamics Route-A Program'
bibliography:
- references.bib
date: 14 August 2026
title: '**The Kraft--Fredholm Trilemma for Logarithmic Prime Codes**'
```

## Markdown 正文

# Introduction

The tensor monoid of finite full shifts contains a canonical arithmetic skeleton: $$\mathsf F_m\boxtimes\mathsf F_n\cong\mathsf F_{mn},
  \qquad h_{\mathrm{top}}(\mathsf F_n)=\log n.$$ Its tensor-indecomposable objects are the $\mathsf F_p$. Earlier papers in this program used those atoms as countably many isolated primitive loops and obtained $$\det(I-zD_s)=\prod_{p\in\mathbb P}(1-zp^{-s}),
  \qquad \operatorname{Re}s>1.$$ That identity is exact but structurally sparse: the recurrent core already contains one state per atom. The present question is whether the same ledger can be compressed into a finite visible symbolic grammar of $O(\log p)$ code length without forfeiting the whole Fredholm operator.

Coding and zeta-function interactions are classical [@keller1991; @bealperrin2005; @hong2011; @bealperrinrestivo2024], as are finite-state graph determinants [@bowenlanford1970] and zeta functions of formal languages [@berstelreutenauer1990]. Our contribution is not a new Kraft inequality or a general classification of possible period sets. It is the following source-locked incompatibility.

[\[thm:trilemma\]]{#thm:trilemma label="thm:trilemma"} On the natural vertex space $\ell^2(V)$, the following four requirements cannot hold simultaneously:

1.  a stationary directed graph with a finite local code separating the intended rational-prime cycles;

2.  a positive scalar primitive ledger containing exactly one primitive orbit $\gamma_p$ for every prime and no other primitive orbit;

3.  the additive total roof $T(\gamma_p)=\log p$;

4.  compactness of the whole one-step weighted adjacency for some real $\sigma>0$.

The proof has two independent pieces. Literal positivity forces different prime cycles into disjoint recurrent components. Finite visible separation then forces $\ell(p)\ge c\log p$ along infinitely many primes. Since the total roof of such a cycle is only $\log p$, one edge retains a uniformly large weight; distinct cycle vertices give a weakly null sequence on which the adjacency does not tend to zero.

The theorem is intentionally attached to the uninduced graph-coordinate operator. Holomorphic transfer spaces can be nuclear even when a vertex adjacency is not [@mayer1990]; signed or graded cancellation can remove cycles that positivity cannot. Those are successor obligations, not counterexamples to the theorem.

#### Contributions.

We prove cycle-separation, coding, compactness, roof-rank, and marker firewalls; audit prefix tries, renewal and factorization grammars, and finite-prefix S-adic controls; and identify the only clean positive escape as the countable atom diagonal. The exact suite contains 35 tests and no zero data or fitted spectral targets.

# Prior work and claim boundary

Kraft--McMillan theory constrains uniquely decipherable codes [@mcmillan1956]; its extension inside sofic constraints is already known [@bealperrin2005]. We therefore use Kraft theory as an ingredient, not as novelty. Circular codes and renewal systems already provide determinant and loop-counting formulas [@keller1991; @hong2011; @bealperrinrestivo2024]. Countable Markov thermodynamic formalism [@sarig1999] and weighted infinite-graph determinants [@deitmar2015] likewise delimit the analytic terminology.

Nor do we claim that symbolic systems cannot realize prime period sets: modern realization results are substantially broader [@dejong2026]. Direct prime in symbolic dynamics refers to topological product indecomposability, a different notion [@kopra2023]. Automata do not recognize binary primes [@hartmanisshank1968], but short non-finite-state certificates exist [@pratt1975]; hence code length alone is not an arithmetic no-go.

The defensible statement is narrower: no searched primary source combines finite visible separation, a positive literal prime-only orbit ledger, total roof $\log p$, and the whole natural graph-coordinate Fredholm gate. We make no priority claim beyond that conjunction. We also do not infer a universal operator-space obstruction from the natural $\ell^2(V)$ result.

# Frozen symbolic object

Let $G=(V,E)$ be a countable simple directed graph, let $\mathcal A$ be a finite alphabet of cardinality $b\ge2$, and let $$\lambda:E\to\mathcal A,\qquad \tau:E\to[0,\infty)$$ be the visible edge code and roof. A primitive directed orbit $\gamma=e_0\cdots e_{\ell-1}$ has length $\ell(\gamma)$, roof $$T(\gamma)=\sum_{j=0}^{\ell-1}\tau(e_j),$$ and cyclic visible word $\Lambda(\gamma)=[\lambda(e_0)\cdots
\lambda(e_{\ell-1})]_{\mathrm{cyc}}$.

[\[def:literal\]]{#def:literal label="def:literal"} The graph has a literal prime ledger if its primitive directed orbits are exactly $\{\gamma_p:p\in\mathbb P\}$, with $$T(\gamma_p)=\log p,$$ and the cyclic words $\Lambda(\gamma_p)$ are pairwise distinct.

For real $\sigma>0$ the frozen column-source adjacency is $$L_\sigma e_u
    =\sum_{e:u\to v}e^{-\sigma\tau(e)}e_v
    \quad\text{on }\ell^2(V).$$ If this formula is unbounded, the Fredholm gate has already failed. All compactness claims below are conditional on boundedness.

The connected orbit expression is $$-\log D_G(s,z)
   =\sum_{[\gamma]\ {\rm primitive}}\sum_{r\ge1}
      \frac{z^{r|\gamma|}}r e^{-srT(\gamma)}.$$ The marker $z$ counts original graph edges. First-return induction is a different object and must retain a separate marker.

#### Excluded mechanisms.

The source lock excludes cancellation by signed, complex, matrix, exterior, or super weights; an infinite visible alphabet; a prime-indexed hidden state declared finite; target-zero data; and a post hoc replacement of $z^{\ell(p)}$ by $z$. These exclusions define the theorem's scope rather than a claim about every symbolic model.

# Positivity separates the recurrent prime cycles

[\[lem:separate\]]{#lem:separate label="lem:separate"} Under [\[def:literal\]](#def:literal){reference-type="ref" reference="def:literal"}, $\gamma_p$ and $\gamma_q$ are vertex-disjoint for $p\ne q$.

If the cycles meet at a vertex, rotate them into based closed words $x$ and $y$. Their concatenation is legal. Write $xy=z^m$, where $z$ is its primitive word root. The literal ledger makes $z=\gamma_r$ for some prime $r$. Roof additivity gives $$\log p+\log q=m\log r,\qquad\text{hence}\qquad pq=r^m,$$ contradicting unique factorization.

[\[cor:scc\]]{#cor:scc label="cor:scc"} Every recurrent strongly connected component contains at most one prime cycle. Bidirectional recurrent connectors between two prime cycles are impossible.

Connector paths in both directions, together with segments of the two cycles, form an additional mixed closed word; its primitive root contradicts [\[lem:separate\]](#lem:separate){reference-type="ref" reference="lem:separate"}.

[\[lem:simple\]]{#lem:simple label="lem:simple"} Every $\gamma_p$ is a simple directed cycle.

A repeated vertex splits $\gamma_p$ into two nonempty closed words. Their primitive roots are ledger cycles $\gamma_q,\gamma_r$, repeated $m,n\ge1$ times. Thus $p=q^mr^n$, impossible. A zero-roof primitive subword is also excluded because every primitive orbit in the literal ledger has positive prime roof.

The conclusion is stronger than saying mixing is inconvenient: in the positive literal class, recurrent compression itself is forbidden. Transient prefix sharing remains possible, but it cannot alter the periodic determinant.

# Finite coding forces the Fredholm failure

[\[lem:counting\]]{#lem:counting label="lem:counting"} There exist infinitely many primes $p$ such that $$\ell(p)\ge \frac{\log p}{4\log b}.$$

The number of nonempty words of length at most $L$ is less than $b^{L+1}/(b-1)$, and the number of cyclic words is no larger. If $p_N$ is the $N$th prime and $M_N=\max_{k\le N}\ell(p_k)$, visible separation gives $$N<\frac{b^{M_N+1}}{b-1}.$$ For sufficiently large $N$, the elementary estimate $p_N\le N^2$ holds. Passing to record indices of $M_N$ and absorbing the fixed additive constant yields the stated subsequence bound.

Under unique decipherability, Kraft--McMillan gives the sharper familiar constraint $$\sum_p b^{-\ell(p)}\le1.$$ The divergence of $\sum_p1/p$ again forces logarithmic length on a subsequence. We keep the elementary counting lemma because it needs only cyclic separation.

[\[thm:noncompact\]]{#thm:noncompact label="thm:noncompact"} For every $\sigma>0$ for which $L_\sigma$ is bounded, it is noncompact and hence belongs to no finite Schatten class.

Choose distinct primes $p_j$ from [\[lem:counting\]](#lem:counting){reference-type="ref" reference="lem:counting"}. The average roof on $\gamma_{p_j}$ is at most $4\log b$, so some edge $e_j:u_j\to v_j$ satisfies $\tau(e_j)\le4\log b$. By [\[lem:separate\]](#lem:separate){reference-type="ref" reference="lem:separate"}, the sources $u_j$ are distinct. The standard basis vectors $e_{u_j}$ are weakly null, while positivity gives $$\|L_\sigma e_{u_j}\|_2
    \ge e^{-\sigma\tau(e_j)}
    \ge b^{-4\sigma}.$$ A compact operator maps bounded weakly null sequences to norm-null sequences. The contradiction proves noncompactness; every $\mathcal S_q$ operator is compact [@simon2005].

[\[cor:roofrank\]]{#cor:roofrank label="cor:roofrank"} No finite roof inventory can produce all values $\log p$.

Period sums of finitely many roof values lie in their finite-dimensional $\mathbb Q$-span. The numbers $\{\log p:p\in\mathbb P\}$ are $\mathbb Q$-linearly independent: clearing denominators in a relation and exponentiating gives a multiplicative relation among distinct primes.

now follows from [\[lem:separate,lem:counting,thm:noncompact\]](#lem:separate,lem:counting,thm:noncompact){reference-type="ref" reference="lem:separate,lem:counting,thm:noncompact"}. The exact private-cycle blocks make the mechanism transparent: their singular values are precisely $e^{-\sigma\tau(e)}$, and $$\|L_{p,\sigma}\|_1
   \ge \ell(p)p^{-\sigma/\ell(p)}.$$ No redistribution of a fixed positive total roof repairs the weak-null witness.

# Marker and renewal firewalls

Even before compactness, the standard graph marker detects a mismatch.

[\[cor:marker\]]{#cor:marker label="cor:marker"} Suppose a positive trace-class graph adjacency satisfies, in a common half-plane and as a germ at $z=0$, $$\det(I-zL_s)=\prod_{p\in\mathbb P}(1-zp^{-s}).$$ Then every prime orbit has graph length one.

An orbit of graph length $\ell$ contributes first at degree $z^\ell$. The coefficient of $z$ in the graph trace logarithm is therefore $$\sum_{\ell(p)=1}p^{-s},$$ while the target coefficient is $\sum_pp^{-s}$. Positivity, equivalently uniqueness of an absolutely convergent Dirichlet series, forces $\ell(p)=1$ for every prime.

Thus a long graph cycle naturally gives $1-z^{\ell(p)}p^{-s}$. Poincaré first return may replace the cycle by one induced symbol and recover $1-zp^{-s}$, but that changes both phase space and marker. It is a useful factor map, not an identity of the original graph-step determinant.

[\[prop:renewal\]]{#prop:renewal label="prop:renewal"} If a recurrent hub admits distinct first returns $R_p,R_q$ of roofs $\log p,\log q$, then the positive connected ledger contains an additional mixed primitive orbit.

The concatenation $R_pR_q$ is closed. If primitive, it is already the extra orbit. If it equals $\delta^m$, its primitive root belongs to the literal ledger, so $T(\delta)=\log r$ for a prime $r$ and $pq=r^m$, impossible.

For a finite prefix trie whose terminals return to the root, deleting the root leaves an acyclic matrix block. A Schur complement gives $$\det(I-A)=1-\sum_n w_n,
  \qquad
  -\log\det(I-A)=\sum_{r\ge1}\frac1r\Bigl(\sum_nw_n\Bigr)^r.$$ This is a connected renewal series. It includes every mixed necklace and is not $\prod_n(1-w_n)$.

There is no injective monoid morphism from $(\mathbb N_{\ge1},\times)$ into a finite-alphabet free monoid that contains two distinct prime images.

For distinct primes $p,q$, commutativity makes $c(p)c(q)=c(q)c(p)$. The commuting-word theorem writes the two nonempty words as powers $u^a,u^b$ of a common word. Then $c(p^b)=c(q^a)$, contradicting injectivity.

# Candidate families and their first failing gates

#### Private prefix-coded cycles.

Binary and self-delimiting codes achieve logarithmic word length and exact positive primitive purity when each code is placed on a private recurrent cycle. then rules out the whole natural adjacency. This is the best-case family used in the theorem.

#### Shared prefix tries and renewal graphs.

They save transient vertices, but every terminal return shares the root. and the Schur complement expose the mixed necklaces. The root-deleted transient trie is harmless; the recurrent closure is not.

#### Factorization and arithmetic renewal.

Splitting an integer into factors supplies arithmetic edges, but allowing successive factors creates many ordered histories for the same product. Removing the histories by first return or Möbius aggregation changes the periodic object. The exact control is therefore useful as a compiler but does not pass the literal-orbit gate.

#### Finite-prefix S-adic constructions.

Nonstationary directives can store increasingly long arithmetic instructions. A finite stationary closure either repeats only a bounded prefix, losing cutoff independence, or permits cross-stage concatenations and additional cycles. We record this as a scoped control, not a theorem against all S-adic systems.

#### Countable atom diagonal.

For any supplied set $S\subseteq\{2,3,\ldots\}$, $$D_{S,s}e_n=n^{-s}e_n,\qquad
  \det(I-zD_{S,s})=\prod_{n\in S}(1-zn^{-s}),\quad\operatorname{Re}s>1.$$ This is honest and exact, but its state inventory is the selected set. Primes, composites, pseudorandom supports, and hashes pass identically. For $S=\mathbb P$ it is the earlier tensor-atom loop object, not a compressed finite code.

summarizes why no family receives combined A1/A2 credit. The result does not forbid a canonical graded analytic complex; that precise loophole is the next paper.

# Exact finite audit

The implementation uses exact integers, rational exponents, combinatorial enumeration, and theorem flags; it does not use a Riemann-zero table, root fitting, or floating spectral matching. The canonical suite passes 35 of 35 tests. Two complete generations are byte-identical, with combined SHA-256

cef9a0d70bde1646e9834b41b76fc92d7058a8a77670519613725bdf77e68d3e.

::: {#tab:audit}
  --------------------------------------------------------------------------------------------------
  ledger                             rows frozen outcome
  -------------------------------- ------ ----------------------------------------------------------
  finite visible code                 112 distinct cyclic words and counting certificate

  private positive roofs              672 every allocation retains the noncompactness witness

  shared prime pairs                   28 every pair creates a mixed primitive firewall

  shared tries                         28 exact $1-\sum w_n$ closure and noncompactness diagnostic

  mixed necklaces                     112 mixed terms present at every audited return length

  marker controls                      20 graph-step and induced-return determinants differ

  arbitrary inventories                84 identical clean diagonal mechanism

  diagonal controls                    28 exact Fredholm product, no selectivity

  factorization renewal                 4 ordered histories survive

  finite-prefix stationarization      140 no cutoff-independent literal escape

  finite roof rank                      5 clock span obstruction exact
  --------------------------------------------------------------------------------------------------

  : Frozen exact evidence. Row counts are descriptive checksums; proofs do not rely on finite cutoff extrapolation.
:::

For prime supports through $127$, the shared renewal census finds $465$, $9{,}920$, and $230{,}640$ mixed primitive necklaces at return lengths $2$, $3$, and $4$, respectively. These counts are not asymptotic evidence; they expose the exact algebra already proved by [\[prop:renewal\]](#prop:renewal){reference-type="ref" reference="prop:renewal"}. The private-cycle singular-value audit verifies $$\max_j e^{-\sigma\tau_{p,j}}\ge p^{-\sigma/\ell(p)},
 \qquad
 \|L_{p,\sigma}\|_1\ge\ell(p)p^{-\sigma/\ell(p)}$$ for all frozen positive roof allocations.

The artifact integrity gate checks the Route schema, code/evaluator firewall, line endings, control bytes, deterministic regeneration, 30-file result checksum ledger, and absence of build caches. All checks pass.

# Route-A evaluation

The strict tuple is $$\begin{aligned}
(&\texttt{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
 &\texttt{A1\_FAIL},\
 \texttt{A2\_FAIL},\
 \texttt{A3\_FAIL},\
 \texttt{A4\_FAIL}).
\end{aligned}$$

#### A0.

The clock $\log n$, tensor multiplication, and factorization controls are source-derived. This is a structural arithmetic relation, not yet an intrinsic finite recurrent selector.

#### A1.

Shared source-derived grammars create mixed primitive cycles. The ideal private-cycle ledger is exact only after one recurrent component has been allocated per selected prime and is therefore a best-case obstruction object, not the desired compression.

#### A2.

The whole natural graph-coordinate adjacency of the separated finite-code model is noncompact. The countable atom diagonal has an honest Fredholm determinant but is the supplied-inventory control and is not spliced into this candidate.

#### A3 and A4.

There is no continuation, Gamma factor, functional equation, zero divisor, counting law, Weil form, self-adjoint generator, or scattering object. Consequently the overall verdict is $$\texttt{ROUTE\_A\_REJECTED},\qquad
 \texttt{ROUTE\_B\_LOCKED}.$$ The positive result is the obstruction label `GO_KRAFT_FREDHOLM_OBSTRUCTION`; the branch stops at `STOP_FINITE_SYMBOL_LOG_CODE` and `STOP_LITERAL_RECURRENT_COMPRESSION`.

# Conclusion

A finite visible code can describe integers in logarithmic length, and a countable diagonal operator can reproduce an arbitrary Euler inventory. The difficulty is satisfying both facts inside one unchanged recurrent symbolic operator. Literal positive recurrence prevents prime cycles from sharing a recurrent core. Once separated, the finite code and total roof $\log p$ leave infinitely many one-step weights bounded away from zero, so the whole adjacency cannot be Fredholm. Collapsing every long cycle to one return symbol restores the determinant only by changing the marker and reintroducing one symbol per supplied atom.

The remaining plausible escape is now sharply specified. It must change the function space or introduce a source-canonical graded numerator, prove all-repetition cancellation of local stability factors, retain the original symbolic marker, and avoid reducing on cohomology to the countable atom inventory. That is a constructive obligation, not a loophole left vague.

# Auxiliary exact identities

Let positive edge weights satisfy $$\prod_{e\in\gamma_p}a_\sigma(e)=p^{-\sigma}.$$ Under the coding and literal-ledger hypotheses, the weighted adjacency is noncompact whenever bounded.

For the logarithmic subsequence of [\[lem:counting\]](#lem:counting){reference-type="ref" reference="lem:counting"}, at least one edge has $$a_\sigma(e)\ge p^{-\sigma/\ell(p)}
 \ge \exp(-4\sigma\log b).$$ The sources lie on disjoint cycles, so the weak-null argument from [\[thm:noncompact\]](#thm:noncompact){reference-type="ref" reference="thm:noncompact"} applies verbatim.

A private two-cycle for each selected integer $n$, with both edge weights $n^{-s/2}$, may be compact or trace class in a right half-plane. Its local factor is nevertheless $1-z^2n^{-s}$.

The two singular values are $|n^{-s/2}|$. Summability is therefore a standard Dirichlet condition. The unique primitive cycle has graph length two, so its determinant factor contains $z^2$, not $z$.

This control shows why the theorem needs finite visible separation plus unbounded code lengths; roof $\log n$ by itself does not imply noncompactness.

The spectrum and compactness of transfer operators depend on the chosen space. Nuclear holomorphic operators for expanding maps [@mayer1990] do not contradict [\[thm:noncompact\]](#thm:noncompact){reference-type="ref" reference="thm:noncompact"}, which is about the frozen whole graph-coordinate adjacency. A successor must state the intertwining map between the symbolic graph and its analytic space and must keep the full repetition ledger.

# Scope and reproducibility ledger

  --------------------------------------------------------------------------------------------------------------
  item                 frozen boundary
  -------------------- -----------------------------------------------------------------------------------------
  system family        one-sided stationary symbolic graphs derived from finite-full-shift arithmetic

  weights              positive scalar, nonnegative additive roofs

  operator             whole column-source adjacency on natural $\ell^2(V)$

  target               literal prime primitive ledger and standard graph marker

  proved               cycle separation, logarithmic code subsequence, noncompactness, marker rigidity

  not proved           signed/matrix cancellation, infinite alphabet, anisotropic spaces, nonstationary limits

  data                 no target zeros, no root fitting, no von Mangoldt feedback

  controls             composites, pseudorandom inventories, renewal, factorization, S-adic prefixes
  --------------------------------------------------------------------------------------------------------------

All finite counts are reproducible with `python experiments/run_sdc26_exact_suite.py`. The theorem statements are cutoff-independent; the finite suite audits the implementation and adversarial controls rather than extrapolating a proof.
