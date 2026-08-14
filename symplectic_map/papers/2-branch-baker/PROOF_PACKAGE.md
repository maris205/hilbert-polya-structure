# Proof Package

## Claim

**Finite-memory locally constant multiplier-clock obstruction.**

Let \(G\) be a finite directed graph defining a subshift of finite type.  Let
\(m\geq 1\), and suppose a multiplicative cocycle assigns to each allowed
length-\(m\) block \(b\) a nonzero scalar
\(\mu_b\in\mathbb C^\times\).  For a
periodic orbit \(C\), define its instability length by

\[
L(C)=\sum_{b\in C}\log|\mu_b|,
\]

where blocks are counted with cyclic multiplicity.  Let

\[
V=\operatorname{span}_{\mathbb Q}
  \{\log|\mu_b|:b\text{ is an allowed length-}m\text{ block}\}.
\]

Then \(V\) has finite dimension, every periodic-orbit length \(L(C)\) belongs
to \(V\), and at most \(\dim_{\mathbb Q}V\) distinct numbers in
\(\{\log p:p\text{ is a rational prime}\}\) can belong to \(V\).  In
particular, the clock cannot contain \(\log p\) for every rational prime.
This is a termwise exact obstruction for one fixed finite model.

## Status

PROVABLE AS STATED

## Assumptions

- The directed graph has finitely many vertices and edges.
- The memory \(m\) is finite.
- Only finitely many length-\(m\) blocks are allowed.
- The cocycle is locally constant on those blocks.
- Every block multiplier satisfies \(\mu_b\neq0\), so
  \(\log|\mu_b|\) is defined.
- The clock is additive after taking the logarithm of the multiplicative
  cocycle.
- The target primes are distinct positive rational primes.

No algebraicity assumption on the multipliers is used.

## Notation

- \(\mathcal B_m\) is the finite set of allowed length-\(m\) blocks.
- \(r=|\mathcal B_m|\).
- \(V\) is the rational span of the \(r\) local log-multipliers.
- \(V_{\mathrm{cyc}}\) is the rational span of lengths of all closed walks.
- \(C\) is a periodic orbit in the finite-block presentation.
- \(N_b(C)\in\mathbb Z_{\geq0}\) counts cyclic occurrences of block \(b\)
  along \(C\).

## Proof Strategy

First recode the finite-memory cocycle as an edge-local cocycle on the standard
finite higher-block graph.  Periodic lengths are then integer combinations of
finitely many local lengths, so they lie in a finite-dimensional rational
space.  Finally prove rational linear independence of distinct prime
logarithms by clearing denominators, exponentiating, and applying unique
factorization in the positive integers.

## Dependency Map

1. Finite-memory recoding uses only finiteness of \(G\) and \(m\).
2. The finite-rank conclusion uses additivity of logarithms and the finite set
   of local block weights.
3. Prime-log independence uses positivity of primes, injectivity of the real
   exponential, and the fundamental theorem of arithmetic.
4. The cardinality bound follows from linear independence inside a
   finite-dimensional vector space.

## Proof

**Step 1: finite-block recoding.**

Construct the standard \(m\)-block presentation of the original shift: its
states are the allowed words of length \(m-1\), and an edge is an allowed word
of length \(m\), joining its length-\(m-1\) prefix to its length-\(m-1\)
suffix.  When \(m=1\), use the original finite edge presentation.  Because
the original alphabet and \(m\) are finite, this higher-block graph has
finitely many states and edges.  The original block weight \(\mu_b\) is now
an edge-local weight on this finite graph.  Periodic sequences and their
cyclic block multiplicities are preserved by the recoding.

**Step 2: every periodic length lies in a finite rational span.**

For any periodic orbit \(C\),

\[
L(C)
=\sum_{b\in\mathcal B_m}N_b(C)\log|\mu_b|.
\]

Each coefficient \(N_b(C)\) is a nonnegative integer and hence a rational
number.  Therefore \(L(C)\in V\).  Since \(V\) is spanned by the finite family
\(\{\log|\mu_b|:b\in\mathcal B_m\}\), it satisfies

\[
\dim_{\mathbb Q}V\leq |\mathcal B_m|<\infty.
\]

Weights with \(|\mu_b|=1\) contribute the zero vector and do not invalidate
the statement.  Negative or complex phases do not enter this instability
clock because it was explicitly defined using the modulus.

**Step 3: distinct rational-prime logarithms are rationally linearly
independent.**

Let \(p_1,\ldots,p_k\) be distinct rational primes and suppose

\[
\sum_{i=1}^{k}q_i\log p_i=0
\qquad(q_i\in\mathbb Q).
\]

Choose a positive integer \(D\) divisible by every denominator of the
\(q_i\), and put \(n_i=Dq_i\in\mathbb Z\).  Multiplying the displayed
identity by \(D\) and applying the real exponential gives

\[
\prod_{i=1}^{k}p_i^{n_i}=1.
\]

Move the factors with negative exponents to the other side:

\[
\prod_{n_i>0}p_i^{n_i}
=
\prod_{n_i<0}p_i^{-n_i}.
\]

Both sides are positive integers.  By uniqueness of prime factorization, the
exponent of each prime \(p_i\) is the same on both sides.  The two products
use disjoint sign classes, so this is possible only when every \(n_i=0\).
Hence every \(q_i=0\), proving rational linear independence.

**Step 4: cardinality bound and obstruction.**

Any subset of \(\{\log p:p\text{ prime}\}\) contained in \(V\) is linearly
independent by Step 3.  A linearly independent subset of the
\(\dim_{\mathbb Q}V\)-dimensional vector space \(V\) has cardinality at most
\(\dim_{\mathbb Q}V\).  Thus \(V\) contains at most that many distinct prime
logarithms, and it cannot contain the infinite family of all prime logarithms.
Every periodic length lies in \(V\) by Step 2, so the periodic multiplier
clock cannot contain every \(\log p\).  This proves the claim. \(\square\)

The same argument gives the sharper bound

\[
\#\{p:\exists C,\ L(C)=\log p\}
\leq \dim_{\mathbb Q}V_{\mathrm{cyc}}
\leq \dim_{\mathbb Q}V.
\]

The first dimension may be smaller because edges outside every closed walk,
or coboundary contributions that cancel on every closed walk, do not enlarge
the periodic length space.

The dimension bound is sharp as an abstract finite-graph statement.  A graph
with one vertex and \(r\) self-loops carrying scalar weights
\(p_1,\ldots,p_r\) realizes the \(r\) independent lengths
\(\log p_1,\ldots,\log p_r\).  This sharpness example explicitly inserts a
finite list of primes and is not an arithmetic-origin construction.

## Candidate Corollary

For the frozen constant-slope PCF Markov--baker, every allowed branch
contributes

\[
\log\sqrt2=\frac12\log2.
\]

Every closed walk has even length \(2k\), hence

\[
L(C)=k\log2,\qquad |\Lambda_u(C)|=2^k.
\]

If \(L(C)=\log p\) for a rational prime \(p\), injectivity of the exponential
gives \(p=2^k\).  Primality forces \(k=1\), so \(p=2\).  Therefore this
candidate's exact multiplier ledger intersects the rational primes only at
\(2\).

## Corrections or Missing Assumptions

The claim would be false if it were stated for arbitrary finite-state smooth
systems without local constancy: a point-dependent derivative or roof
function can generate infinitely many rationally independent orbit lengths.
The locally constant, finite-memory, multiplicative hypothesis is therefore
essential.

## Open Risks

- The theorem excludes exact containment, not approximation, correlation, or
  density-matched statistical resemblance.
- The theorem concerns one fixed graph and one fixed cocycle.  A growing
  sequence of finite models may cover an increasing family whose union is
  infinite.
- It does not cover countably many states, infinite memory, point-dependent
  Hölder roofs, or a model that directly inserts infinitely many arithmetic
  weights.
- It is a scalar multiplicative-cocycle result.  For matrix cocycles, it
  applies to a multiplicative scalar such as the determinant, but not
  automatically to spectral radius, largest eigenvalue, or largest singular
  value.
- Primitive/repetition status does not affect the finite-rank conclusion:
  repetitions merely multiply an already-admissible length by a positive
  integer.
- Phase-sensitive or signed quantum weights are different objects from the
  modulus-based instability clock proved here.
- The proof does not by itself establish inequality of two analytically
  continued zeta functions: termwise cancellation or non-positive weights
  would require a separate uniqueness argument in a common convergence
  half-plane.
