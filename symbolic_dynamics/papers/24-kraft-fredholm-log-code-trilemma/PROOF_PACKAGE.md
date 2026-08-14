# Proof Package — SD-C26

**Candidate:** SD-C26  
**Proof status:** complete for every manuscript theorem  
**Primary family:** Symbolic Dynamics  
**External ingredients:** elementary prime bounds, unique factorization,
the commuting-word theorem, the compact-operator weak-null criterion, and
the standard trace-class Fredholm expansion  
**Imported internal boundary:** Paper04/Paper19 atom-diagonal selector control

## 0. Frozen notation

Let (G=(V,E)) be a countable simple directed graph.  Fix a finite alphabet
(\mathcal A), (b=|\mathcal A|\ge2), an edge code
(\lambda:E\to\mathcal A), and a nonnegative roof
(\tau:E\to[0,\infty)).  For a primitive directed orbit (\gamma), write

\[
 |\gamma|=\ell(\gamma),\qquad
 T(\gamma)=\sum_{e\in\gamma}\tau(e),
\]

and let (\Lambda(\gamma)) be the cyclic word of visible edge labels.
The intended literal ledger contains exactly one primitive orbit
(\gamma_p) for every rational prime (p), no other primitive orbits, and

\[
        T(\gamma_p)=\log p.
\]

For real (\sigma>0), the positive vertex adjacency is

\[
 L_\sigma e_u
 =\sum_{e:u\to v}e^{-\sigma\tau(e)}e_v.
\]

If this rule is unbounded, the Fredholm gate fails before the claims below.
Hence every operator statement assumes boundedness.

## 1. Finite visible coding forces long prime orbits

### Lemma 1.1 — counting lower bound

Suppose the cyclic words (\Lambda(\gamma_p)) are pairwise distinct.  Then
for infinitely many primes (p),

\[
        \ell(p):=|\gamma_p|
        \ge \frac{\log p}{4\log b}.
\]

**Proof.**  The number of ordinary nonempty words over (\mathcal A) of
length at most (L) is

\[
 W_b(L)=\sum_{j=1}^{L}b^j
       <\frac{b^{L+1}}{b-1}.
\]

The number of cyclic words is no larger.  Let
(p_1<\cdots<p_N) be the first (N) primes and

\[
        M_N=\max_{1\le k\le N}\ell(p_k).
\]

Separation gives (N\le W_b(M_N)), so

\[
 M_N>\frac{\log((b-1)N)}{\log b}-1.
\]

For all sufficiently large (N), the elementary bound (p_N\le N^2)
holds.  Choose (q_N\le p_N) with (\ell(q_N)=M_N).  The maxima are
unbounded; pass to record indices so that the chosen (q_N) are distinct.
After absorbing the fixed additive constant,

\[
 \ell(q_N)=M_N
 \ge\frac{\log N}{2\log b}
 \ge\frac{\log q_N}{4\log b}.
\]

This proves the claim.  The constant is deliberately nonoptimal.
(\square)

**Boundary.**  The lemma gives an infinite subsequence, not a lower bound for
every prime.  An infinite visible alphabet or a nonseparating finite code
with hidden countable state names violates its hypothesis.

## 2. A positive prime-only ledger separates its cycles

### Lemma 2.1 — distinct prime cycles cannot meet

If the only primitive directed orbits are the (\gamma_p), then
(\gamma_p) and (\gamma_q) are vertex-disjoint whenever (p\ne q).

**Proof.**  If the cycles meet at (v), rotate their edge words to based
closed words (x) and (y) at (v).  Their concatenation is legal.  Write

\[
        xy=z^m,
\]

where (z) is the primitive word root and (m\ge1).  The literal ledger
identifies (z=\gamma_r) for a rational prime (r).  Roof additivity gives

\[
        \log p+\log q=m\log r,
\]

so (pq=r^m), contrary to unique factorization for distinct primes.
(\square)

### Corollary 2.2 — no shared recurrent core

A strongly connected component contains at most one prime cycle.  Directed
connector paths in both directions between two disjoint prime cycles would
again concatenate to an additional mixed closed word and contradict
Lemma 2.1.

### Corollary 2.3 — each prime cycle is simple

Assume every primitive orbit has positive roof (\log r).  Then every
(\gamma_p) is a simple directed cycle.

**Proof.**  A repeated vertex splits (\gamma_p) into two nonempty closed
words.  Taking primitive roots and using the literal ledger yields primes
(q,r) and integers (m,n\ge1) such that

\[
        \log p=m\log q+n\log r,
\]

hence (p=q^mr^n), impossible.  A zero-roof primitive subword cannot occur,
because every primitive orbit in the ledger has positive prime roof.
(\square)

**Positivity boundary.**  Signed, complex, matrix, exterior-power, or
supertrace weights may cancel mixed connected cycles coefficientwise.  The
literal positive ledger has no such cancellation.  The proof does not
exclude those other programs.

## 3. The whole operator is noncompact

### Lemma 3.1 — logarithmic disjoint-cycle obstruction

Under the frozen hypotheses, (L_\sigma) is not compact for any real
(\sigma>0) for which it is bounded.  It consequently belongs to no
Schatten class.

**Proof.**  By Lemma 1.1, choose distinct primes (p_j) satisfying

\[
        \ell(p_j)\ge c_b\log p_j,
        \qquad c_b=(4\log b)^{-1}.
\]

Some edge (e_j:u_j\to v_j) of (\gamma_{p_j}) has roof at most the
average:

\[
 \tau(e_j)
 \le\frac{\log p_j}{\ell(p_j)}
 \le c_b^{-1}=4\log b.
\]

Lemma 2.1 makes the source vertices (u_j) distinct.  Thus (e_{u_j}) is a
bounded weakly null sequence in (\ell^2(V)).  Positivity gives

\[
 \|L_\sigma e_{u_j}\|_2
 \ge e^{-\sigma\tau(e_j)}
 \ge b^{-4\sigma}>0.
\]

A compact operator sends bounded weakly null sequences to norm-null
sequences, a contradiction.  Every Schatten operator is compact.
(\square)

### Corollary 3.2 — product-weight form

The same conclusion holds for positive edge weights (a_\sigma(e)) with

\[
        \prod_{e\in\gamma_p}a_\sigma(e)=p^{-\sigma}.
\]

Indeed some edge satisfies

\[
 a_\sigma(e)\ge p^{-\sigma/\ell(p)}
 \ge e^{-\sigma/c_b},
\]

and the weak-null proof is unchanged.  Concentrating almost the entire roof
on one edge cannot repair the remaining long cycle.

## 4. Main incompatibility theorem

### Theorem 4.1 — Kraft--Fredholm trilemma

The following four properties cannot hold simultaneously:

1. a stationary countable directed graph with a prime-orbit-separating
   finite local code;
2. a positive scalar primitive ledger with exactly one primitive orbit per
   rational prime and no other primitive orbit;
3. intrinsic additive total roof (T(\gamma_p)=\log p); and
4. compactness of the whole one-step weighted vertex adjacency on
   (\ell^2(V)) for some real (\sigma>0).

If the first three properties hold, the fourth fails by Lemmas 1.1, 2.1,
and 3.1.  Sharing a recurrent core to avoid disjoint long blocks breaks the
second property.  Replacing the finite code by one countable atom state per
prime breaks the first property and enters the arbitrary-inventory control.
(\square)

### Corollary 4.2 — finite roof inventories are insufficient

If edge roofs take only the values (t_1,\ldots,t_d), every orbit roof
belongs to the (\mathbb Q)-span of those values.  But the set
(\{\log p:p\text{ prime}\}) is linearly independent over (\mathbb Q):
after denominators are cleared, a relation gives
(\prod p_j^{a_j}=1), and unique factorization forces every (a_j=0).
Thus a finite roof inventory cannot supply all prime clocks.  Infinitely
many state-dependent clock values must be source-derived; listing them by
prime index stores the atom inventory in the roof.

## 5. The graph-step marker is a second firewall

### Corollary 5.1 — exact marked identity forces atom loops

Suppose a trace-class positive scalar adjacency has, as a germ at (z=0)
on a half-plane of absolute convergence,

\[
        \det(I-zL_s)=\prod_p(1-zp^{-s}).
\]

Then every prime primitive orbit has graph length one.

**Proof.**  An orbit of length (\ell) contributes only to degrees
(z^{r\ell}) in the connected trace logarithm.  The coefficient of (z)
on the graph side is therefore

\[
        \sum_{p:\ell(p)=1}p^{-s},
\]

whereas the target coefficient is (\sum_pp^{-s}).  Positivity, or
uniqueness of absolutely convergent Dirichlet series, forces every prime
into the first sum.  Hence (\ell(p)=1) for all (p).
(\square)

Infinitely many visible length-one words cannot be separated by a finite
alphabet.  The natural trace-class realization is the countable atom
diagonal.  Inducing a long graph cycle to one first return also changes
(z^{\ell(p)}) to (z); it is not the same graph-step determinant.

## 6. Factorization and renewal grammars

### Proposition 6.1 — no injective free-word multiplicative compiler

There is no injective monoid homomorphism

\[
 c:(\mathbb N_{\ge1},\times)\longrightarrow(\mathcal A^*,\cdot)
\]

whose domain contains two distinct primes.

**Proof.**  For distinct primes (p,q), commutativity gives

\[
        c(p)c(q)=c(pq)=c(qp)=c(q)c(p).
\]

The commuting-word theorem gives a word (u) and positive integers (a,b)
with (c(p)=u^a) and (c(q)=u^b).  Hence

\[
        c(p^b)=u^{ab}=c(q^a),
\]

contradicting injectivity because (p^b\ne q^a).
(\square)

### Proposition 6.2 — a renewal hub creates mixed primitives

Suppose a hub has distinct first-return words (R_p,R_q) with roofs
(\log p,\log q).  Their concatenation is a legal hub-based closed word.
If it is primitive, it is an extra connected orbit of roof (\log(pq)).  If
it is a proper (m)th power, its primitive root must be a prime orbit
(\gamma_r), giving (r^m=pq), again impossible.  Thus a positive renewal
graph cannot carry both returns and retain the prime-only primitive ledger.

The first-return determinant has a connected return series such as

\[
        1-\sum_pw_p,
\]

while the desired disconnected Euler selection is
(\prod_p(1-w_p)).  Passing to the induced return system simplifies the
series but changes the original edge marker.

## 7. Exact finite-closure identities

### Proposition 7.1 — disjoint cycle singular values

For a private directed cycle of length (\ell(n)) with positive edge roofs
(\tau_{n,j}), the cyclic weighted adjacency has singular values exactly

\[
        e^{-\sigma\tau_{n,1}},\ldots,
        e^{-\sigma\tau_{n,\ell(n)}}.
\]

If their sum is (\log n), then

\[
 \max_j e^{-\sigma\tau_{n,j}}
 \ge n^{-\sigma/\ell(n)},
\]

and AM--GM gives

\[
 \|L_{n,\sigma}\|_1
 \ge\ell(n)n^{-\sigma/\ell(n)}.
\]

These statements are exact finite-block certificates for Lemma 3.1.

### Proposition 7.2 — shared prefix-trie determinant

Let a finite rooted prefix trie have an edge from every selected terminal
leaf back to the root.  Delete the root; the remaining graph is acyclic.
If (w_n(z)) is the product of weights and graph-step markers around the
first-return loop indexed by (n), then a Schur complement, equivalently
first-return decomposition, gives

\[
        \det(I-zA)=1-\sum_nw_n(z).
\]

Consequently

\[
 -\log\det(I-zA)
 =\sum_{r\ge1}\frac1r\left(\sum_nw_n(z)\right)^r,
\]

which contains mixed primitive necklaces.  It is not
(\prod_n(1-w_n(z))).

## 8. Sharp controls

### Control 8.1 — arbitrary diagonal inventory

For any (S\subseteq\{2,3,\ldots\}), put one loop at each (n\in S):

\[
        L_se_n=n^{-s}e_n,
        \qquad
        \det(I-zL_s)=\prod_{n\in S}(1-zn^{-s})
\]

for (\Re s>1) whenever (S\subseteq\mathbb N).  This realizes primes,
squares, Fibonacci numbers, random sets, hashes, or any supplied inventory.
It is an honest Fredholm operator and no arithmetic explanation.

### Control 8.2 — private two-cycles

One private two-cycle per selected (n), with both weights (n^{-s/2}),
may be compact and even trace class in a suitable half-plane.  It violates
finite visible orbit separation and contributes (1-z^2n^{-s}), not
(1-zn^{-s}).  This prevents overclaiming that prime roof alone always
forces noncompactness.

### Control 8.3 — weighted star

A hub with private spokes can be finite rank when the spoke vector is in
(\ell^2), but alternating spokes creates mixed primitive hub cycles.  This
shows that primitive purity, rather than logarithmic roof alone, is the
decisive hypothesis.

## 9. Route consequence and open boundary

The proved tuple is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

Theorems 4.1 and 5.1 reject the positive finite-local-code branch.  They do
not reject signed or matrix-valued cancellation, nonlocal orbit weights,
infinite visible alphabets, quotient operators, or anisotropic function
spaces.  Any successor must prove coefficientwise cancellation in the full
connected trace logarithm for every repetition and must establish
whole-space nuclearity before receiving A2 credit.
