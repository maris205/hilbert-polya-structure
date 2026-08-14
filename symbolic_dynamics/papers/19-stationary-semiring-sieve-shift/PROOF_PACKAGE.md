# PROOF PACKAGE — SD-C21

## Claim

The alphabet product, alphabet-sum, order, successor, and entropy of finite
full shifts support a completely expanded trial-division program.  Its
one-sided countable Markov graph has one accepted self-loop exactly for each
rational prime.  A single trace-class weighted vertex adjacency on the whole
graph has the exact prime power traces and reciprocal Euler determinant on
(\operatorname{Re}s>1).  Nevertheless, every arithmetic computation state
is transient and determinant-invisible.  Positive exact ledgers prune to
simple cycles, and a universal total-decider wrapper compiles every decidable
support, proving a scoped no-go for arithmetic selectivity.

## Status

`PROVABLE AS STATED`, subject to four explicit scopes.

1. The exact-ledger pruning theorem assumes nonzero positive formal weights
   and forbids extra primitive orbit classes before specialization.
2. Pruning preserves periodic traces and determinants, not topological
   conjugacy of the full one-sided systems.
3. Contracting an (\ell)-cycle changes the graph-step marker from (z^\ell)
   to (z) unless (z^\ell) is explicitly retained.
4. No claim is made for signed, complex-cancelling, homological, or
   supertrace ledgers.

## Assumptions and notation

- (F_n=A_n^{\mathbb Z}), up to conjugacy.
- (F_m\boxtimes F_n\cong F_{mn}) and
  (F_m\boxplus F_n\cong F_{m+n}).
- (G) is exactly the expanded (I,T,Q,A,R) graph in `SOURCE_LOCK.md`.
- (X_G^+) is one-sided.
- (L_s\delta_u=\sum_{e:u\to v}e^{-s\tau(e)}\delta_v) on
  (\ell^2(V(G))).
- (D_{\rm SV}(s,z)=\det(I-zL_s)).

## Dependency map

1. Theorem 1 proves trial correctness and the full cycle census.
2. Theorem 2 proves trace class and (\mathcal S_1)-holomorphy.
3. Theorem 3 derives power traces and the Euler determinant.
4. Theorem 4 proves block pruning and determinant invisibility.
5. Theorem 5 proves the positive exact-ledger SCC obstruction.
6. Corollary 6 specializes the obstruction to deterministic verifiers.
7. Theorem 7 proves the universal total-decider compiler.
8. Theorem 8 gives the factorial-monoid specialization and polynomial
   control.

## Theorem 1 — trial-division correctness

For every (n\ge2), the forward orbit of (I_n) reaches (A_n) if and only
if (n) is prime.  The only directed cycles in (G) are the self-loops at
(A_p), one for every rational prime (p).

### Proof

Fix (n,d) with (d^2\le n).  Starting at (Q_{n,d,2}), the quotient index
(q) increases by one while (dq<n).  Since (dq) strictly increases, the
chain reaches either equality or the first strict overshoot after finitely
many steps.  Equality occurs exactly when (d\mid n), with no existential
edge guard.  An overshoot advances the divisor from (d) to (d+1).

If (n=ab) is composite with (2\le a\le b), then (a\le\sqrt n).  The
divisor chain reaches (d=a) before the strict-square stop, and quotient
search reaches (q=b), hence the cemetery.  Conversely, equality (dq=n)
with (d,q\ge2) proves compositeness.  If the first (d) with (d^2>n) is
reached without equality, (n) has no proper factor and is prime.  The
square test precedes quotient search, so this also accepts (2) and (3).

Outside accepted states, either (q), (d), or the cemetery index strictly
increases along the unique forward path.  No such state lies on a directed
cycle.  Therefore the declared accepted self-loops are all and only the
cycles.  ∎

## Theorem 2 — trace class and holomorphic family

For (\sigma=\operatorname{Re}s>1), (L_s\in\mathcal S_1), and
(s\mapsto L_s) is holomorphic with values in (\mathcal S_1) on that
half-plane.

### Proof

Write each edge as the rank-one matrix unit

\[
e^{-s\tau(e)}\,|\delta_{t(e)}\rangle
\langle\delta_{o(e)}|.
\]

Its trace norm is (e^{-\sigma\tau(e)}).  The accepted loops and input edges
give

\[
\sum_p p^{-\sigma}+\sum_{n\ge2}(2n)^{-\sigma}<\infty.
\]

There is at most one terminal (T)-edge for each reachable pair with
(2\le d\le\lfloor\sqrt n\rfloor+1).  Whether it ends at (A_n) or starts
the (q=2) search, the factor (2) only decreases its weight, so

\[
\sum_{n\ge2}n^{-\sigma}
 \sum_{2\le d\le\sqrt n+1}d^{-\sigma}
\le C_\sigma\sum_{n\ge2}n^{-\sigma}<\infty,
\quad C_\sigma=2\sum_{d\ge2}d^{-\sigma}.
\]

For quotient edges, enlarge all finite reachable ranges:

\[
\sum_{n\ge2}\sum_{d\ge2}\sum_{q\ge2}(ndq)^{-\sigma}
=\left(\sum_{n\ge2}n^{-\sigma}\right)
 \left(\sum_{d\ge2}d^{-\sigma}\right)
 \left(\sum_{q\ge2}q^{-\sigma}\right)<\infty.
\]

The cemetery contribution is bounded by

\[
\sum_{\substack{n\ge2\\ n\ {\rm composite}}}
 \sum_{k\ge1}[n(k+1)]^{-\sigma}
\le
\left(\sum_{n\ge2}n^{-\sigma}\right)
\left(\sum_{j\ge2}j^{-\sigma}\right)<\infty.
\]

Thus the rank-one edge series converges absolutely in trace norm.  On every
compact subset of (\operatorname{Re}s>1), replace (\sigma) by the compact
lower bound.  The same majorants give locally uniform trace-norm convergence
of holomorphic finite partial sums, hence Banach-valued holomorphy.  ∎

## Theorem 3 — exact traces and Fredholm--Euler identity

For every (r\ge1), (\operatorname{Re}s>1), and (z\in\mathbb C),

\[
\operatorname{Tr}L_s^r=\sum_p p^{-rs},\qquad
D_{\rm SV}(s,z)=\prod_p(1-zp^{-s}).
\]

At (z=1), (D_{\rm SV}(s)=\zeta(s)^{-1}).

### Proof

By Theorem 1, every length-(r) closed walk is the (r)-fold traversal of a
unique (A_p)-loop.  Its weight is (p^{-rs}).  Trace class justifies
summing diagonal matrix coefficients, proving the trace formula and the
primitive/repetition ledger.

For (|z|) small, the trace-class logarithm gives

\[
\log\det(I-zL_s)
=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_s^r
=-\sum_p\sum_{r\ge1}\frac{(zp^{-s})^r}{r}
=\sum_p\log(1-zp^{-s}).
\]

For fixed (s) in the half-plane, both sides define entire functions of
(z): the Fredholm determinant is entire and the genus-zero product is
normally convergent because (\sum_pp^{-\sigma}<\infty).  Equality near zero
therefore extends to all (z).  Euler's product gives the specialization at
(z=1).  ∎

## Theorem 4 — off-diagonal DAG invisibility

Let (\mathcal H_A) be the closed span of all accepted states and
(\mathcal H_T=\mathcal H_A^\perp).  Relative to
(\mathcal H_A\oplus\mathcal H_T),

\[
L_s=\begin{pmatrix}D_s&B_s\\0&Q_s\end{pmatrix},\qquad
D_s\delta_{A_p}=p^{-s}\delta_{A_p}.
\]

For every (r\ge1),

\[
\operatorname{Tr}Q_s^r=0,\quad
\operatorname{Tr}L_s^r=\operatorname{Tr}D_s^r,
\]

and, for all (z\),

\[
\det(I-zQ_s)=1,\qquad
\det(I-zL_s)=\det(I-zD_s).
\]

### Proof

The accepted span is invariant; the sole cross-block kind maps the terminal
prime trial state into (A_p).  The transient graph has no closed walk, so
every diagonal coefficient of every (Q_s^r) is zero.  Since (Q_s) is
trace class, its trace is the sum of these diagonal coefficients.  The
trace-log expansion gives determinant one near (z=0), and entireness
extends the equality to all (z).  The same argument applied to the
block-triangular powers proves the remaining formulas.  ∎

## Theorem 5 — positive exact-ledger pruning

Let (G') be a directed graph with nonzero edge weights in the positive
power-series semiring over independent variables (x_a).  Suppose its
orbitwise target ledger contains one declared primitive class (\gamma_a)
of total weight (x_a) for each (a), all powers are temporal repetitions,
and no other primitive class is allowed.  Then every recurrent strongly
connected component is one simple declared cycle.  Every edge outside those
cycles occurs in no power trace, and pruning it preserves every raw power
trace and the full (z)-determinant.

Contracting a simple cycle of graph length (\ell) and total weight (w)
to a first-return loop preserves the unmarked factor (1-w).  It preserves
the marked factor only if the new loop retains (z^\ell), because the
original factor is (1-z^\ell w).

### Proof

Every recurrent edge lies on a directed cycle.  If one recurrent SCC
contains two declared cycles, strong connectivity gives finite connector
paths in both directions.  Traversing the two cycles and connectors produces
a closed word not equal to a temporal repetition of either declared cycle.
Removing its least period gives an additional primitive orbit.  If an SCC
contains one declared cycle and any extra recurrent edge or vertex, that
edge lies on another cycle and the same argument applies.  Positivity and
independent formal variables prevent the extra orbit from disappearing by
cancellation or being silently identified after specialization.  Hence each
recurrent SCC is exactly one simple declared cycle.  Nonrecurrent edges lie
on no closed walk and are absent from all power traces.  The determinant and
contraction statements follow from the trace-log expansion and the direct
cycle factor (1-z^\ell w).  ∎

## Corollary 6 — deterministic verifier collapse

An outdegree-one verifier graph is a functional digraph: recurrent
components are directed cycles with feeding trees.  Under an exact
one-primitive-per-accepted-object ledger, computation in the feeding trees is
determinant-invisible.  Computation placed on an accepted cycle is only a
state subdivision after first-return contraction, with graph-step length
retained by (z^\ell).  This is an orbit/determinant statement, not a
topological conjugacy.

## Theorem 7 — universal total-decider wrapper

Let (S\subseteq\{2,3,\ldots\}) be decided by a total deterministic machine
with finite runtime (T(n)\ge1).  There is a one-sided countable functional
graph and an (\mathcal S_1)-holomorphic adjacency (L_{S,s}), for
(\operatorname{Re}s>1), such that

\[
\operatorname{Tr}L_{S,s}^r=\sum_{n\in S}n^{-rs},\qquad
\det(I-zL_{S,s})=\prod_{n\in S}(1-zn^{-s}).
\]

### Proof

Expose the full configuration chain
(C_{n,0}\to\cdots\to C_{n,T(n)}).  Send the terminal state to an
(A_n)-loop when (n\in S), and otherwise to a one-way cemetery ray.  Give
the (t)-th computation/terminal edge weight ([n(t+2)]^{-s}), the (k)-th
cemetery edge weight ([n(k+1)]^{-s}), and the accept loop weight (n^{-s}).
Then

\[
\begin{aligned}
\|L_{S,s}\|_1
&\le \sum_{n\ge2}\sum_{t=0}^{T(n)}[n(t+2)]^{-\sigma}
 +\sum_{n\notin S}\sum_{k\ge1}[n(k+1)]^{-\sigma}
 +\sum_{n\in S}n^{-\sigma}\\
&\le 2\left(\sum_{n\ge2}n^{-\sigma}\right)
       \left(\sum_{j\ge2}j^{-\sigma}\right)
 +\sum_{n\ge2}n^{-\sigma}<\infty.
\end{aligned}
\]

The estimate is independent of the growth of (T(n)).  Compact
sub-half-plane bounds give (\mathcal S_1)-holomorphy.  Only the (A_n)
loops close, so Theorems 3 and 4 apply verbatim.  ∎

## Theorem 8 — factorial-monoid compiler

Let (M) be a countable effective factorial monoid with atom set
(\mathcal A), a terminating atom verifier, a multiplicative norm
(N:M\to(1,\infty)), and source-defined transient roofs summable on a
half-plane.  If (\sum_{a\in\mathcal A}N(a)^{-\sigma}<\infty), the verifier
compiler satisfies

\[
\operatorname{Tr}L_{M,s}^r=\sum_{a\in\mathcal A}N(a)^{-rs},\qquad
\det(I-zL_{M,s})=\prod_{a\in\mathcal A}(1-zN(a)^{-s}).
\]

For monic (\mathbb F_q[t]), with (N(f)=q^{\deg f}),

\[
\det(I-L_{M,s})
=\prod_{\pi\ {\rm monic\ irreducible}}
 (1-q^{-s\deg\pi})=1-q^{1-s}.
\]

### Proof

The atom verifier supplies the configuration chains of Theorem 7, now
indexed by effective monoid objects and weighted by the norm.  Correctness,
summability, and the absence of reject cycles are the only ingredients in
the trace/determinant proof.  Unique factorization of monic polynomials gives

\[
\prod_\pi(1-u^{\deg\pi})^{-1}
=\sum_{f\ {\rm monic}}u^{\deg f}
=\sum_{d\ge0}q^du^d=(1-qu)^{-1};
\]

put (u=q^{-s}) and invert.  ∎

## Final proof verdict

The positive theorems establish an exact source-built verifier and an exact
same-object determinant.  The pruning and compiler theorems establish the
scope of the failure: the determinant records accepted support, not the
arithmetic computation that selected it.  The result is therefore
`SELECTOR_TAUTOLOGICAL`, `PRUNING_EQUIVALENT`, and `PROVES_TOO_MUCH`, while
remaining mathematically non-oracular and noncircular.
