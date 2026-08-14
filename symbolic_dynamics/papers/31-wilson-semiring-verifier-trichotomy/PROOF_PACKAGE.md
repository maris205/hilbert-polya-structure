# Proof package — Paper 31 / SD-C33

## 1. Purpose and scope

This package proves the exact algebraic, periodic-orbit, and operator claims
used by Paper 31.  The main conclusion is a trichotomy.  Alphabet sum breaks
Paper 30's **bare** polynomial-UFD monomial clone, but it does not produce a
positive Route-A object: an isomorphic matched semiring clone copies the
construction; a transient verifier prunes to its accepted loops; and the
recurrent Wilson realization is noncompact under the exact entropy clock.

The abstract disjoint-cycle compactness criterion, first-return marker
warning, and universal-decider obstruction are inherited from Paper 20.  They
are restated only in the specialization needed here.  Paper 31 does not claim
those general statements as new.

## 2. Source and notation

Let \(A_n\) be an alphabet of cardinality \(n\) and write
\[
  F_n=(A_n^{\mathbb Z},\sigma_n),\qquad n\geq0,
\]
for its two-sided full shift, with \(F_0\) the empty system.  On conjugacy
classes define
\[
  F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n},
  \qquad
  F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn}.
\]
Here \(\boxplus\) means alphabet-sum followed by the full-shift functor.  No
categorical coproduct claim is made in the category of subshifts and block
maps.  The source norm is
\[
  \mathcal N(F_n)=e^{h(F_n)}=n\quad(n\geq1).
\]

The additive successor is \(S(F_n)=F_n\boxplus F_1\).  Its iterates generate
the successor order.  Quotient and remainder are characterized by
\[
  F_a\cong (F_q\boxtimes F_n)\boxplus F_r,
  \qquad 0\preceq_+F_r\prec_+F_n,
\]
and source congruence \(F_a\equiv_nF_b\) means equality of their unique
remainders modulo \(F_n\).

## 3. Algebraic separation and its exact boundary

### Theorem 3.1 — additive reconstruction

Let \(S\) be a commutative semiring with zero and unit.  Suppose:

1. every element of \(S\) equals \(n\cdot1\) for some \(n\in\mathbb N_0\);
2. \(n\cdot1=m\cdot1\) implies \(n=m\).

Then
\[
  \iota:\mathbb N_0\longrightarrow S,
  \qquad n\longmapsto n\cdot1,
\]
is a semiring isomorphism.

**Proof.**  Additive generation makes \(\iota\) surjective, and the second
assumption makes it injective.  Concatenating sums of the unit gives
\(\iota(m+n)=\iota(m)+\iota(n)\).  Distributivity gives
\[
  \iota(m)\iota(n)
  =(m\cdot1)(n\cdot1)
  =mn\cdot1
  =\iota(mn).
\]
The map also preserves zero and unit.  Hence it is a bijective semiring
homomorphism.  \(\square\)

### Corollary 3.2 — the full-shift skeleton is \(\mathbb N_0\)

The map \(n\mapsto[F_n]\) is a semiring isomorphism from \(\mathbb N_0\) to
the alphabet-sum/product skeleton of finite full shifts.

**Proof.**  The two operations reproduce addition and multiplication of
alphabet cardinalities.  Every class is an iterated alphabet-sum of \(F_1\).
If \(F_m\) and \(F_n\) are conjugate for positive \(m,n\), entropy gives
\(\log m=\log n\), so \(m=n\); the zero object is also distinct.  Apply
Theorem 3.1.  \(\square\)

### Proposition 3.3 — failure of the bare polynomial-UFD clone

Let \(M\) be the monomial submonoid of
\(\mathbb Z[x_p:p\text{ prime}]\), and let
\[
  \Phi(n)=\prod_p x_p^{v_p(n)}
\]
be Paper 30's multiplicative clone map.  No restriction of ordinary
polynomial addition to \(M\) turns \(\Phi\) into a semiring homomorphism.

**Proof.**  Such an extension would satisfy
\[
  x_2=\Phi(2)=\Phi(1+1)=\Phi(1)+\Phi(1)=1+1=2,
\]
which is false in the polynomial ring.  In particular, \(M\) is not closed
under ordinary polynomial addition.  \(\square\)

This proposition is deliberately narrow.  It separates the new source from
the exact bare control used in Paper 30; it does not separate it from every
possible clone.

### Proposition 3.4 — matched semiring-clone indistinguishability

Let \(Y=\{y_n:n\in\mathbb N_0\}\) be a relabeled copy of the source, with
\[
  y_m\oplus_Yy_n=y_{m+n},
  \qquad
  y_m\otimes_Yy_n=y_{mn}.
\]
Transport the successor order, quotient, remainder, congruence, entropy,
Wilson states, edge roofs, and graph-step markers through
\(F_n\mapsto y_n\).  The resulting decorated source is isomorphic to the
full-shift semiring source.  Every isomorphism-natural Wilson path, cycle,
roof, marked trace ledger, and formal product agrees term by term.

**Proof.**  The displayed operations commute with the relabeling by
definition.  Each later datum is obtained from those operations, source
equality, the successor order, and transported decorations.  Induction over
the construction depth transports every state and edge.  It therefore
preserves cycle words, roofs, return times, and all derived ledgers.
\(\square\)

## 4. The stationary Wilson graph

For \(n\geq2\), set
\[
  r_{n,1}=1,
  \qquad
  r_{n,k+1}\equiv r_{n,k}(k+1)\pmod n,
  \qquad 1\leq k\leq n-2,
\]
with \(0\leq r_{n,k}<n\).  Thus \(r_{n,k}=k!\bmod n\), but the recurrence is
the frozen local source rule.

The single countable graph \(G_W\) has states
\[
  v_{n,k}=(F_n,F_k,F_{r_{n,k}}),
  \qquad n\geq2,\quad1\leq k\leq n-1,
\]
and edges \(v_{n,k}\to v_{n,k+1}\) for \(k<n-1\).  The terminal state has an
edge back to \(v_{n,1}\) exactly when
\[
  F_{r_{n,n-1}}\cong F_{n-1};
\]
otherwise it has no recurrent return.  The rule is stationary because one
local definition applies to all \(n\); it contains no supplied prime table.

### Theorem 4.1 — Wilson prime-cycle classification

For every \(n\geq2\), the \(n\)-block of \(G_W\) is recurrent if and only if
\(n\) is prime.  Each recurrent block is one oriented simple primitive cycle
\(\Gamma_p\) of graph length \(p-1\), up to cyclic rotation.

**Proof.**  The recurrence gives
\(r_{n,n-1}\equiv(n-1)!\pmod n\).  If \(p\) is prime, the nonzero residues
form a group.  Pair each residue with its inverse.  A self-inverse residue
satisfies \((a-1)(a+1)=0\) in the field \(\mathbb Z/p\mathbb Z\), so only
\(1\) and \(-1\) remain unpaired (for \(p=2\) they coincide).  Consequently
\((p-1)!\equiv-1\pmod p\), and the terminal edge closes.

Conversely, let \(n>1\) be composite.  For \(n=4\),
\(3!=6\equiv2\pmod4\).  If \(n=ab>4\) with
\(2\leq a<b\leq n-2\), the distinct factors \(a,b\) occur in
\((n-1)!\), so \(n\mid(n-1)!\).  If \(n=a^2\) with \(a\geq3\), the distinct
factors \(a\) and \(2a\leq a^2-1\) occur, so again
\(a^2\mid(n-1)!\).  Every composite \(n>4\) therefore has terminal residue
zero, not \(n-1\).  A closed deterministic block passes once through the
distinct states \(v_{p,1},\ldots,v_{p,p-1}\); hence it is a simple primitive
cycle.  \(\square\)

### Corollary 4.2 — exact prime-power repetition ledger

Give \(\Gamma_p\) nonnegative edge roofs whose sum is \(\log p\).  Its
\(r\)-fold temporal repetition has total roof \(r\log p\) and weight
\(p^{-rs}\).  These repetitions are the legitimate prime-power terms.  There
is no additional primitive orbit indexed by the integer \(p^r\).

## 5. Formal trace and marked product

For the uniform allocation
\[
  \tau_{p,k}=\frac{\log p}{p-1},
  \qquad
  w_{p,k}(s)=p^{-s/(p-1)},
\]
let \(L_s\) be the weighted vertex adjacency on the recurrent subspace
\(\ell^2(V_{\mathrm{rec}}(G_W))\).

### Proposition 5.1 — finite periodic diagonal ledger

For every positive integer \(r\), the basis-diagonal periodic sum is
\[
  \operatorname{Tr}_{\mathrm{per}}(L_s^r)
  =\sum_{p-1\mid r}(p-1)p^{-sr/(p-1)}.
\]
The sum is finite.

**Proof.**  A block of length \(p-1\) contributes to the diagonal of
\(L_s^r\) precisely when \(p-1\mid r\).  It then has \(p-1\) starting
vertices, each with repeated-cycle weight \(p^{-sr/(p-1)}\).  The divisibility
condition implies \(p\leq r+1\), so only finitely many primes contribute.
\(\square\)

The notation \(\operatorname{Tr}_{\mathrm{per}}\) is intentional:
\(L_s^r\) is not trace class, even though this basis-diagonal periodic sum is
finite.

### Proposition 5.2 — formal primitive product

For \(\Re s\geq0\) and \(|z|<1\), define from the absolutely convergent
periodic trace-log
\[
  D_W(s,z)
  :=\exp\left(-\sum_{r\geq1}\frac{z^r}{r}
  \operatorname{Tr}_{\mathrm{per}}(L_s^r)\right).
\]
As a periodic-orbit identity,
\[
  D_W(s,z)=\prod_p(1-z^{p-1}p^{-s}).
\]
The product on the right converges normally for \(|z|<1\) on every compact
subset of the \(s\)-plane and therefore continues the trace-log definition
in \(s\).  At \(z=1\) and \(\Re s>1\),
\[
  D_W(s,1)=\prod_p(1-p^{-s})=\zeta(s)^{-1}.
\]

**Proof.**  For \(\Re s\geq0\), substitute Proposition 5.1, use absolute
convergence, and write \(r=m(p-1)\).  The contribution of a fixed prime to
the exponent is
\[
  -\sum_{m\geq1}\frac{z^{m(p-1)}}{m}p^{-sm}
  =\log(1-z^{p-1}p^{-s}).
\]
Exponentiation gives the product in the initial region.  On
\(|z|\leq\rho<1\) and a compact \(s\)-set with \(\Re s\geq-M\), the factor
increments are dominated by \(\rho^{p-1}p^M\), whose sum converges.  This
normally convergent product supplies the continuation to all \(s\).  At
\(z=1\), absolute convergence in \(\Re s>1\) is the usual Euler region.
\(\square\)

This proposition licenses a formal periodic product, not
\(\det(I-zL_s)\).  The next theorem supplies the decisive ownership
obstruction.

## 6. Entropy-clock dilution

### Theorem 6.1 — whole recurrent operator noncompactness

On every prime cycle let \(\tau(e)\geq0\) and require
\[
  \sum_{e\in\Gamma_p}\tau(e)=\log p.
\]
For every \(s\) with \(\sigma=\Re s>0\), the primary recurrent weighted
vertex adjacency \(L_s\) is noncompact.  Hence it belongs to no finite
Schatten class.

**Proof.**  Choose on each \(\Gamma_p\) an edge \(e_p\) of minimum roof.
Since the cycle has \(p-1\) edges,
\[
  \tau(e_p)\leq\frac{\log p}{p-1},
  \qquad
  |w(e_p)|\geq p^{-\sigma/(p-1)}\longrightarrow1.
\]
Let \(\delta_p\) denote the basis vector at the source of \(e_p\).  The
vectors \(\delta_p\) are orthonormal, and their images lie in distinct prime
blocks.  Thus they have orthogonal images whose norms do not tend to zero.
A compact operator maps every weakly null orthonormal sequence to a norm-null
sequence, which gives a contradiction.  Every finite Schatten-class operator
is compact.  \(\square\)

### Corollary 6.2 — exact length criterion for a disjoint successor

For disjoint cycles with lengths \(\ell_n\), total nonnegative roofs \(T_n\),
and weights \(e^{-s\tau}\), some allocation can be compact for fixed
\(\Re s>0\) only if \(T_n/\ell_n\to\infty\); uniform allocation proves the
condition is also sufficient.  With \(T_p=\log p\), a disjoint successor
therefore requires \(\ell(p)=o(\log p)\).  Merely
\(\ell(p)=O(\log p)\) is not enough.

**Proof.**  Necessity follows from the minimum-roof edge in Theorem 6.1.
For sufficiency use \(\tau_{n,j}=T_n/\ell_n\); every block norm is then
\(e^{-\sigma T_n/\ell_n}\to0\), and a direct sum of finite blocks whose norms
tend to zero is compact.  \(\square\)

### Corollary 6.3 — uniform essential approximate spectrum

For the uniform Wilson allocation, the unit circle lies in the essential
approximate spectrum of \(L_s\).

**Proof.**  The \(p\)-block is a scalar multiple of the cyclic permutation
matrix.  Its eigenvalues are
\[
  p^{-s/(p-1)}\omega,
  \qquad \omega^{p-1}=1.
\]
Their radii tend to one and their angular meshes tend to zero.  For every
point of the unit circle, choose eigenvalues from distinct blocks converging
to that point.  The corresponding normalized eigenvectors are orthogonal and
form a Weyl sequence.  \(\square\)

## 7. First return and marker ownership

### Theorem 7.1 — honest induced determinant, changed time

Induce on one marked base vertex in each prime cycle.  The first-return
operator is
\[
  R_se_p=p^{-s}e_p.
\]
It is trace class exactly for \(\Re s>1\), and
\[
  \det(I-zR_s)=\prod_p(1-zp^{-s}).
\]
At \(z=1\) this equals \(D_W(s,1)\).  For a free graph-step marker, however,
the raw and induced factors are respectively
\[
  1-z^{p-1}p^{-s}
  \quad\text{and}\quad
  1-zp^{-s},
\]
so first return changes the time object.

**Proof.**  One complete return multiplies the edge weights around
\(\Gamma_p\), giving \(e^{-s\log p}=p^{-s}\).  The trace norm is
\(\sum_p p^{-\Re s}\), finite exactly when \(\Re s>1\).  The diagonal
Fredholm product follows.  One induced step equals \(p-1\) original graph
steps, which gives the marker comparison.  \(\square\)

## 8. Transient pruning

### Proposition 8.1 — trace-class DAG invisibility

Replace each recurrent Wilson computation by a finite acyclic verifier feeding
an accept vertex, and place a loop of weight \(n^{-s}\) at that vertex exactly
when the verifier accepts.  Choose all nonloop regulator weights so that the
direct sum of DAG-edge operators and feed edges is trace class.  Then, for
\(\Re s>1\), the full operator \(T_s\) is trace class and
\[
  \operatorname{Tr}(T_s^r)=\sum_p p^{-sr},
  \qquad
  \det(I-zT_s)=\prod_p(1-zp^{-s}).
\]
Deleting every verifier state preserves all power traces and the determinant.

**Proof.**  Order each finite DAG before its terminal accept vertex.  The
operator is block triangular.  Every finite DAG block is nilpotent, while the
countable trace-class direct sum need only be quasinilpotent.  Acyclicity is
the relevant property: no positive power has a diagonal walk through a DAG,
so every DAG power trace is zero.  The only closed walks are repetitions of
accept loops.  Trace-log factorization therefore leaves the displayed prime
diagonal determinant.  \(\square\)

### Corollary 8.2 — universal total-decider control

The construction in Proposition 8.1 works for every total decider
\(P(n)\): add an accept loop exactly when \(P(n)=1\).  Squares, powers of two,
Fibonacci numbers, seeded computable supports, and arbitrary decidable
supports therefore reproduce the transient-pruning architecture.  If the
accepted computation is instead closed into disjoint cycles of unbounded
length with exact total roof \(\log n\), the same minimum-roof obstruction
applies whenever \(\log n/\ell_P(n)\) fails to diverge.

This corollary does not say that the arithmetic sources of those predicates
are identical.  It says that terminal compilation supplies no selective
analytic mechanism beyond the accepted support.

## 9. Route corollary

### Corollary 9.1 — terminal semiring-verifier trichotomy

For SD-C33 the following statements hold simultaneously:

1. alphabet sum and congruence break Paper 30's bare polynomial-UFD clone;
2. an isomorphic matched semiring clone copies every source-natural datum;
3. the exact Wilson grammar has one primitive prime cycle and the formal
   graph-step product \(D_W(s,z)\);
4. the primary recurrent operator is noncompact for every nonnegative exact
   entropy-clock allocation;
5. first return gives an honest determinant only on a changed time object;
6. a trace-class transient realization prunes to its accepted-loop diagonal;
7. arbitrary total deciders reproduce the analytic architecture.

Consequently the correct route record is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
CLOSE_TERMINAL_SEMIRING_VERIFIER_BRANCH
```

The closure is scoped to terminal/feed-forward and vertex-disjoint recurrent
verifier architectures with nonnegative exact source roofs.  It does not
classify every overlapping, signed, supersymmetric, or homological grammar.
