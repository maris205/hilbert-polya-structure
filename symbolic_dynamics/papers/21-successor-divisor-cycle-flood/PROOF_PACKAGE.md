# Proof Package — SD-C23

## 0. Conventions and theorem status

The vertex set is \(V=\{2,3,\ldots\}\), and

\[
 n\longrightarrow d
 \quad\Longleftrightarrow\quad
 d\ge2,\qquad d\mid n+1.
\]

Closed paths are rooted when they are counted by a trace and unrooted modulo
cyclic rotation when they are counted as primitive orbits.  Reflections are
not identified.  On \(\mathcal H=\ell^2(V)\),

\[
 L_s e_n=
 \sum_{\substack{d\ge2\\d\mid n+1}}(nd)^{-s}e_d,
 \qquad \sigma=\operatorname{Re}s.
\]

All results below are proved analytically.  Finite calculations are exact
regression certificates and are not premises of the proofs.

## 1. Elementary edge bounds

### Lemma 1.1 — successor and maximal-growth bounds

For every \(n\ge2\), the edge \(n\to n+1\) is present.  Every edge
\(n\to d\) satisfies \(d\le n+1\).

**Proof.**  The integer \(n+1\) divides itself, and every positive divisor of
\(n+1\) is at most \(n+1\).  ∎

### Lemma 1.2 — forced drop from a cyclic maximum

Let a directed closed walk contain a maximal vertex \(M\), and write its next
vertex as \(d\).  Then

\[
 d\le \frac{M+1}{2}.
\]

**Proof.**  Since \(d\mid M+1\), either \(d=M+1\) or \(d\) is a proper
divisor of \(M+1\).  The first case contradicts maximality of \(M\).  A
proper positive divisor of an integer \(N\\) is at most \(N/2\).  ∎

## 2. Recurrence and mixing

### Theorem 2.1 — constructive strong connectivity

The successor–divisor graph is strongly connected.

**Proof.**  If \(n\) is odd, then \(2\mid n+1\), hence \(n\to2\).  If \(n\)
is even, then

\[
 n\to n+1\to2.
\]

Thus every vertex reaches \(2\) in at most two edges.  Conversely, repeated
successor edges give

\[
 2\to3\to\cdots\to m
\]

for every \(m\ge2\).  Concatenating these paths connects any ordered pair of
vertices.  ∎

### Proposition 2.2 — path-sense topological mixing

For every pair \(u,v\in V\), there is \(N(u,v)\) such that for every
\(n\ge N(u,v)\) there is a path of length \(n\) from \(u\) to \(v\).
Consequently the one-sided countable Markov shift is topologically mixing in
the path sense.

**Proof.**  The cycles

\[
 3\to2\to3,
 \qquad
 3\to4\to5\to3
\]

have lengths two and three and are based at \(3\).  Fix paths from \(u\) to
\(3\) and from \(3\) to \(v\), of total length \(b\).  Every integer at least
two is of the form \(2a+3c\) with \(a,c\ge0\).  Hence every sufficiently
large \(n-b\) is obtained by concatenating the two based loops before the
fixed exit path.  ∎

## 3. Primitive-cycle flood

### Theorem 3.1 — one canonical primitive cycle at every length

For every \(k\ge2\),

\[
 C_k=(k,k+1,\ldots,2k-1)
\]

is a simple primitive directed cycle of length \(k\).

**Proof.**  Consecutive vertices are joined by successor edges.  The last
edge is present because \(k\mid2k=(2k-1)+1\).  The displayed vertices are
distinct, so the closed word is simple and therefore cannot be a positive
temporal power of a shorter closed word.  ∎

Its orbit mass and endpoint-weight product are

\[
 M_k=\prod_{j=k}^{2k-1}j=\frac{(2k-1)!}{(k-1)!},
 \qquad
 w_s(C_k)=M_k^{-2s}.
\]

### Proposition 3.2 — divisor-indexed subflood

If \(d\mid r\) and \(d\ge2\), then

\[
 C_{r,d}=(d,d+1,\ldots,d+r-1)
\]

is a simple primitive cycle of length \(r\).  Therefore, if \(P_r\) denotes
the number of primitive rotation classes of length \(r\), then

\[
 P_r\ge \tau(r)-1.
\]

**Proof.**  The closing edge exists because
\(d\mid d+r=(d+r-1)+1\).  Simplicity gives primitivity.  Distinct divisors
give cycles with distinct minimal vertices, so their rotation classes are
distinct.  ∎

## 4. Exact finite confinement

### Theorem 4.1 — maximal-vertex confinement and rigidity

Every directed closed walk of length \(r\ge1\) lies in

\[
 \{2,3,\ldots,2r-1\}.
\]

If such a walk reaches \(2r-1\), then it is \(C_r\), up to cyclic rotation.

**Proof.**  The assertion is vacuous for \(r=1\), because \(n\nmid n+1\).
Let \(r\ge2\), choose a maximal vertex \(M\) on the walk, and denote its next
vertex by \(d\).  Lemma 1.2 gives

\[
 d\le\frac{M+1}{2}.
\]

There are \(r-1\) edges left before the walk returns to the chosen occurrence
of \(M\).  Lemma 1.1 says that each can increase the current vertex by at
most one.  Hence

\[
 M\le d+r-1
 \le\frac{M+1}{2}+r-1,
\]

and therefore \(M\le2r-1\).

If \(M=2r-1\), equality must hold at every step of the inequality chain.
Thus \(d=(M+1)/2=r\), and every remaining edge is a successor edge.  Starting
at \(M\), the walk is

\[
 2r-1\to r\to r+1\to\cdots\to2r-1,
\]

which is a rotation of \(C_r\).  ∎

### Corollary 4.2 — certified finite trace cutoff

For each fixed \(r\\), every rooted closed walk of length \(r\) is contained
in the induced prefix \(2\le n\le2r-1\).  Thus the order-\(r\) trace computed
at any cutoff \(N\ge2r-1\) equals the infinite-graph closed-walk sum exactly.

For every \(s\in\mathbb C\), that formal sum is finite.  On the operator
domain \(\sigma>1/2\), it is the operator trace \(\operatorname{Tr}L_s^r\).

**Proof.**  The confinement theorem gives the first statement.  Each vertex
has finitely many outgoing edges, so the induced finite prefix has finitely
many length-\(r\) paths.  When \(L_s\) is trace class, the usual diagonal
trace equals this finite diagonal sum.  ∎

### Corollary 4.3 — extremal certificate

At the sharp cutoff \(2r-1\), the only primitive rotation class that uses the
top vertex is \(C_r\), and it contributes exactly \(r\) rooted walks.

## 5. Primitive/repetition bookkeeping

### Proposition 5.1 — necklace recurrence

Let \(T_r\) be the number of rooted length-\(r\) closed walks in the
unweighted graph and \(P_r\) the number of primitive length-\(r\) rotation
classes.  Then

\[
 T_r=\sum_{d\mid r}dP_d,
 \qquad
 P_r=\frac1r\sum_{d\mid r}\mu(r/d)T_d.
\]

**Proof.**  Every rooted length-\(r\) closed word is a temporal repetition of
a unique primitive class of length \(d\mid r\).  That primitive class has
exactly \(d\) rooted representatives, even after repetition.  Summing over
\(d\mid r\) proves the first identity; Möbius inversion proves the second.
∎

The same reasoning with weights gives the trace/primitive factorization in
the local convergence domain.  Temporal repetition and cyclic rotation are
never identified with one another.

## 6. Sharp trace-class theorem

### Theorem 6.1 — exact nuclear half-plane

\[
 L_s\in\mathcal S_1(\ell^2(V))
 \quad\Longleftrightarrow\quad
 \operatorname{Re}s>\frac12.
\]

#### Sufficiency

For each \(d\ge2\), let \(R_{d,s}\) be the operator consisting of row \(d\)
of \(L_s\).  Its nonzero source columns are \(n=kd-1\ge2\), and it is rank
one.  Therefore

\[
 \|R_{d,s}\|_1
 =\left(
   \sum_{\substack{k\ge1\\kd-1\ge2}}
   [d(kd-1)]^{-2\sigma}
  \right)^{1/2}.
\]

Since \(kd-1\ge kd/2\),

\[
 \|R_{d,s}\|_1
 \le
 2^\sigma\zeta(2\sigma)^{1/2}d^{-2\sigma}.
\]

For \(\sigma>1/2\), the sum over \(d\\) converges.  Hence

\[
 L_s=\sum_{d\ge2}R_{d,s}
\]

converges in trace norm and is trace class.

#### Necessity

Let \(U_t e_n=e^{int}e_n\).  If \(L_s\in\mathcal S_1\), then its first
Fourier diagonal

\[
 S_s=
 \frac1{2\pi}\int_0^{2\pi}
 e^{-it}U_tL_sU_t^*\,dt
\]

is an \(\mathcal S_1\)-valued Bochner integral.  It selects precisely matrix
entries with row index minus column index equal to one.  In this graph those
are the successor edges, so

\[
 S_se_n=[n(n+1)]^{-s}e_{n+1}.
\]

The singular values of this unilateral weighted shift are
\([n(n+1)]^{-\sigma}\), \(n\ge2\).  Consequently

\[
 \|S_s\|_1
 =\sum_{n\ge2}[n(n+1)]^{-\sigma},
\]

which is finite exactly when \(2\sigma>1\).  Trace class of \(L_s\) would
force trace class of \(S_s\), proving necessity.  ∎

### Proposition 6.2 — trace-norm holomorphy

The map

\[
 s\longmapsto L_s
\]

is holomorphic from \(\{\operatorname{Re}s>1/2\}\) to \(\mathcal S_1\).

**Proof.**  On a compact set with \(\operatorname{Re}s\ge\sigma_0>1/2\),
the \(m\)-th derivative of an entry introduces
\(\log^m(nd)\).  Choose \(0<\varepsilon<\sigma_0-1/2\).  The elementary
bound \(\log^m x\le C_{m,\varepsilon}x^\varepsilon\) reduces every derivative
row estimate to the preceding nuclear bound at real part
\(\sigma_0-\varepsilon>1/2\).  The row series and all derivative series
therefore converge locally uniformly in trace norm.  ∎

## 7. Fredholm determinant and orbit product

### Theorem 7.1 — same-object determinant ledger

For \(\sigma>1/2\),

\[
 D_{\rm SD}(s,z)=\det(I-zL_s)
\]

is holomorphic in \(s\) and entire in \(z\).  For

\[
 |z|<\|L_s\|^{-1}
\]

(and, by local uniformity, on compact subdomains with a uniform smaller
radius),

\[
 -\log D_{\rm SD}(s,z)
 =\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_s^r.
\]

If \(\gamma=(n_0,\ldots,n_{\ell-1})\) is a primitive rotation class and

\[
 N(\gamma)=\prod_{j=0}^{\ell-1}n_j,
\]

then its cyclic edge product is \(N(\gamma)^{-2s}\), and

\[
 D_{\rm SD}(s,z)
 =\prod_{[\gamma]\ \mathrm{primitive}}
  \left(1-z^{\ell(\gamma)}N(\gamma)^{-2s}\right)
\]

in the corresponding local absolute-convergence domain.

**Proof.**  Trace-class Fredholm theory gives the determinant and logarithmic
trace series.  Expanding every trace as its finite closed-walk sum, grouping
each closed word by its unique primitive root, and summing temporal
repetitions with

\[
 \sum_{m\ge1}\frac{x^m}{m}=-\log(1-x)
\]

gives the product.  Absolute convergence justifies the regrouping locally in
\(z\).  No claim at \(z=1\) follows without an additional estimate.  ∎

### Corollary 7.2 — conjugation symmetry

\[
 D_{\rm SD}(\overline s,\overline z)
 =\overline{D_{\rm SD}(s,z)}.
\]

This is entrywise conjugation of the same operator family, not a functional
equation.

## 8. Low-order exact ledger

### Proposition 8.1 — first four traces

\[
 \operatorname{Tr}L_s=0,
\]

\[
 \operatorname{Tr}L_s^2=2\,6^{-2s},
\]

\[
 \operatorname{Tr}L_s^3=3\,60^{-2s},
\]

\[
 \operatorname{Tr}L_s^4
 =2\,6^{-4s}+4\,120^{-2s}+4\,840^{-2s}.
\]

**Proof.**  There are no loops.  At length two the only primitive class is
\((2,3)\); at length three it is \((3,4,5)\).  At length four there is the
double traversal of \((2,3)\) and the two primitive classes
\((2,3,4,5)\) and \((4,5,6,7)\).  Their vertex products are respectively
\(6,60,120,840\), and a primitive class of length \(r\) has \(r\) rooted
representatives.  Confinement reduces each classification to the relevant
finite prefix.  ∎

At \(s=1\), these become

\[
 0,\qquad \frac1{18},\qquad \frac1{1200},\qquad \frac{29}{15876}.
\]

## 9. Exact target obstruction

### Theorem 9.1 — marked degree-one mismatch

On their common comparison domain \(\operatorname{Re}s>1\), the holomorphic
germs at \(z=0\)

\[
 D_{\rm SD}(s,z)
 \quad\text{and}\quad
 D_{\mathbb P}(s,z)=\prod_p(1-zp^{-s})
\]

are unequal.

**Proof.**  Since no integer \(n\ge2\) divides \(n+1\), the graph has no
loops and

\[
 [z]D_{\rm SD}(s,z)=-\operatorname{Tr}L_s=0.
\]

For real \(s>1\), absolute convergence of the prime sum gives

\[
 [z]D_{\mathbb P}(s,z)=-\sum_pp^{-s}<0.
\]

Thus even the first marked Taylor coefficients differ.  ∎

This theorem does not exclude an isolated numerical equality between the two
specializations at \(z=1\); such an equality would not repair the marked
primitive/repetition ledger.

### Theorem 9.2 — wrong orbit-norm species

Every primitive orbit has length at least two.  For every closed orbit
\(\gamma\), \(N(\gamma)\) is composite and

\[
 e^{T_\gamma}=N(\gamma)^2
\]

is a composite perfect square.

**Proof.**  Absence of loops gives length at least two.  Every vertex is at
least two, so \(N(\gamma)\) is a product of at least two integers greater than
one.  The endpoint roof is \(T_\gamma=2\log N(\gamma)\).  ∎

Even if one informally halved the frozen roof, the norm \(N(\gamma)\) would
remain composite.  Such halving is not an authorized change of SD-C23.

## 10. Pruning controls

Let \(G_{\{1,2\}}\) retain exactly the edges whose quotient

\[
 q(n,d)=\frac{n+1}{d}
\]

belongs to \(\{1,2\}\).

### Theorem 10.1 — quotient-spine persistence

The spine \(G_{\{1,2\}}\) is strongly connected and path-sense mixing, has no
loops, contains every canonical cycle \(C_k\), and its weighted adjacency is
trace class exactly for \(\sigma>1/2\).

**Proof.**  Quotient one gives every successor edge.  Quotient two gives

\[
 2k-1\to k.
\]

An odd vertex \(2k-1\\) descends to \(k\).  An even vertex \(n>2\) follows

\[
 n\to n+1\to\frac{n+2}{2}<n.
\]

Iteration reaches \(2\); successor edges again reach every vertex from
\(2\).  The cycles \(C_2,C_3\) and all \(C_k\) use only these two quotient
types, proving mixing and the flood.  There is still no loop.

For each target row \(d\), at most the two sources \(d-1\) and \(2d-1\)
occur.  The row nuclear norms are \(O(d^{-2\sigma})\), proving trace class for
\(\sigma>1/2\).  Fourier extraction of the retained successor diagonal gives
the same necessity argument as in Theorem 6.1.  ∎

Thus the full graph and this severe pruning have zero margin for the
properties that trigger rejection.

### Proposition 10.2 — successor-only negative control

The quotient-one graph has only the edges \(n\to n+1\), hence is acyclic and
has no periodic orbit.

### Proposition 10.3 — general two-quotient families

Fix \(q\ge2\).  If a quotient inventory retains \(1\) and \(q\), then for
every \(d\ge2\)

\[
 C_{d,q}=(d,d+1,\ldots,qd-1)
\]

is a simple primitive cycle of length \(d(q-1)\).

**Proof.**  Successor edges traverse the interval and the final edge has
quotient

\[
 \frac{(qd-1)+1}{d}=q.
\]

The vertices are distinct.  ∎

## 11. Proof dependency and route boundary

The logical dependency is

\[
 \text{edge grammar}
 \Longrightarrow
 \begin{cases}
   \text{recurrence and cycle flood},\\
   \text{finite confinement},\\
   \text{sharp }\mathcal S_1\text{ theorem},
 \end{cases}
\]

followed by the same-object Fredholm determinant and the marked target
comparison.  No target zero, continuation theorem, functional equation, or
spectral ansatz enters any proof.

The exact route tuple supported by these proofs is

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}).
\]

The overall verdict is \(\mathrm{ROUTE\_A\_REJECTED}\).  A2 certifies only
the determinant of this symbolic object.  A3 fails because no target
completion, Gamma factor, functional equation, global divisor law, or Weil
compression is obtained.  Route B remains locked.
