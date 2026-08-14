# Derivation Package — SD-C26

**Candidate:** SD-C26  
**Purpose:** compact algebraic ledger for manuscript and implementation
cross-checking  
**Arithmetic mode:** exact integer/rational/symbolic whenever possible  
**Zero-data use:** none

## D1. Finite-code count

For an alphabet of size (b\ge2),

\[
        W_b(L)=\sum_{j=1}^Lb^j
        <\frac{b^{L+1}}{b-1}.
\]

If the first (N) primes have distinct cyclic visible words and maximum
length (M_N), then

\[
        N\le W_b(M_N),\qquad
        M_N>\frac{\log((b-1)N)}{\log b}-1.
\]

Using (p_N\le N^2) for large (N) and passing to record maxima gives an
infinite subsequence

\[
        \ell(p)\ge \frac{\log p}{4\log b}.
\]

For a binary prefix-free inventory with counting function
(A(x)\ge Cx^\delta) along an unbounded sequence, Kraft counting gives the
sharper audit form

\[
        \ell(n)\ge\frac{\delta}{\log2}\log n+O(1)
\]

on a subsequence.

## D2. Shared-vertex norm equation

If prime cycles (\gamma_p,\gamma_q) meet, rotate them to based closed words
(x,y).  Write (xy=z^m) with primitive root (z=\gamma_r).  Additivity
gives

\[
 \log p+\log q=m\log r
 \quad\Longleftrightarrow\quad
 pq=r^m,
\]

contradicting unique factorization for (p\ne q).

## D3. Average roof and a nonvanishing column

On a prime cycle,

\[
        \sum_{e\in\gamma_p}\tau(e)=\log p.
\]

Therefore some edge satisfies

\[
        \tau(e)\le\frac{\log p}{\ell(p)}.
\]

Along the long-code subsequence,

\[
        \tau(e)\le4\log b,
        \qquad
        e^{-\sigma\tau(e)}\ge b^{-4\sigma}.
\]

Vertex-disjointness supplies distinct source basis vectors, so these lower
bounds contradict compactness.

## D4. Exact cycle-block singular ledger

For a weighted cyclic permutation block (L_{n,\sigma}),

\[
 s_j(L_{n,\sigma})=e^{-\sigma\tau_{n,j}}.
\]

The geometric mean is

\[
 \left(\prod_{j=1}^{\ell(n)}e^{-\sigma\tau_{n,j}}\right)^{1/\ell(n)}
 =n^{-\sigma/\ell(n)}.
\]

Thus

\[
 \|L_{n,\sigma}\|
 \ge n^{-\sigma/\ell(n)},
 \qquad
 \|L_{n,\sigma}\|_1
 \ge\ell(n)n^{-\sigma/\ell(n)}.
\]

The inequalities are allocation-independent for positive roofs.

## D5. Graph marker comparison

A primitive graph orbit of length (\ell) contributes

\[
        \sum_{r\ge1}\frac{z^{r\ell}}r e^{-srT}
\]

to the connected trace logarithm.  Hence the coefficient of (z) in a
prime-only graph is

\[
        \sum_{p:\ell(p)=1}p^{-s}.
\]

The standard target coefficient is (\sum_pp^{-s}).  Positive equality
forces (\ell(p)=1) for all primes.  Replacing graph steps with first-return
steps changes the invariant rather than solving this mismatch.

## D6. Prefix-trie Schur complement

Order the finite trie vertices with the root first.  The root-deleted block
is nilpotent because the trie is acyclic.  Eliminating that block in
(I-zA) sums all root-to-leaf-to-root first returns:

\[
        \det(I-zA)=1-F(z),
        \qquad F(z)=\sum_nw_n(z).
\]

Therefore

\[
        -\log(1-F)=\sum_{r\ge1}\frac{F^r}{r}.
\]

Cross terms (w_pw_q), (w_pw_qw_r), and their necklaces are connected
mixed primitive cycles.  The disconnected Euler product instead has

\[
        -\log\prod_n(1-w_n)
        =\sum_n\sum_{r\ge1}\frac{w_n^r}{r},
\]

with no mixed terms.

## D7. Free-word multiplicative obstruction

If (c) is a monoid homomorphism, distinct primes satisfy

\[
        c(p)c(q)=c(q)c(p).
\]

Commuting free words are powers of a common word:

\[
        c(p)=u^a,\qquad c(q)=u^b.
\]

Then

\[
        c(p^b)=u^{ab}=c(q^a),
\]

so (c) cannot be injective.  Temporal concatenation cannot faithfully
replace commutative multiplication.

## D8. Diagonal control

For a supplied inventory (S),

\[
        L_se_n=n^{-s}e_n,
        \qquad
        \|L_s\|_1=\sum_{n\in S}n^{-\Re s},
\]

and

\[
        \det(I-zL_s)=\prod_{n\in S}(1-zn^{-s}).
\]

The formula is independent of what predicate produced (S).  Exact success
for primes therefore has no selectivity credit unless the inventory itself
is derived inside the recurrent primitive algebra.

## D9. Candidate decision ledger

| Candidate | finite logarithmic code | primitive ledger | whole Fredholm gate | result |
|---|---:|---:|---:|---|
| private code cycles | yes | clean | fail | `STOP_KRAFT_CLOCK_NONCOMPACT` |
| shared prefix trie | yes | mixed necklaces | fail in frozen roof | `STOP_MIXED_PRIMITIVES` |
| factorization renewal | source-derived | connected/disconnected mismatch | irrelevant after A1 | `CYCLE_FLOOD` |
| frozen S-adic union | yes | lane/share dichotomy | fail | `NONAUTONOMOUS_INFORMATION_OR_CYCLE_FLOOD` |
| countable atom diagonal | no | clean | pass on (\Re s>1) | `ESCAPE_PAPER04 | PROVES_TOO_MUCH` |

This table is a classification inside the source lock, not a universal
symbolic-dynamics no-go theorem.
