# Proof Package: Renewal Flexibility and Mixed-Orbit Obstructions

## Claim

For a shared-base renewal shift:

1. every holomorphic germ \(H(0)=1\) is an inverse renewal determinant;
2. nonnegative coefficients force a positive real determinant zero whenever
   the first-return series crosses one;
3. two or more freely concatenable atoms create mixed primitive factors, so
   the zeta is not an independent product over atoms;
4. finite-dimensional unitary twists do not erase an individual mixed
   primitive factor;
5. a unary regular or context-free return grammar cannot select exactly the
   rational-prime lengths.

## Status

**PROVED**

## Assumptions

The first four parts use a unique shared-base renewal code.  The fifth uses a
unary alphabet and a regular or context-free language.  No claim is made about
arbitrary context-sensitive or computational grammars.

## Notation

\[
F(z)=\sum_{n\ge1}a_nz^n,\qquad D(z)=1-F(z).
\]

For distinct return atoms \(a,b\), use formal weights \(x_a,x_b\).

## Strategy

Use coefficient matching for inverse design, the intermediate value theorem
for positive weights, formal power-series comparison for mixed cycles,
invertibility of unitary matrices for twisted factors, and ultimate
periodicity of unary context-free length sets.

## Dependency Map

Parts 1–4 are elementary analytic or formal-algebraic arguments.  Part 5 uses
Parikh's theorem in its unary specialization: every unary context-free
language has a semilinear, hence ultimately periodic, set of lengths.

## Proof

### Part 1: inverse design

Let \(H(z)=1+\sum_{n\ge1}h_nz^n\) be holomorphic on \(|z|<R\).  Set
\(a_n=-h_n\).  Then, on the same disk,

\[
D(z)=1-\sum_{n\ge1}a_nz^n
=1+\sum_{n\ge1}h_nz^n=H(z).
\]

Thus the representation is exact and requires no dynamical inference.

### Part 2: the positive real zero

Assume \(a_n\ge0\), not all zero, and let \(R\) be the radius of convergence.
For \(0<r<R\), \(F(r)\) is continuous and strictly increasing, with \(F(0)=0\).
If

\[
\lim_{r\uparrow R}F(r)>1,
\]

the intermediate value theorem gives a unique \(r_*\in(0,R)\) with
\(F(r_*)=1\).  Therefore \(D(r_*)=0\).  Positivity by itself is not enough;
the crossing hypothesis is explicit.

### Part 3: mixed primitive words

With two freely concatenable atoms,

\[
Z_{\rm ren}=\frac1{1-x_a-x_b}.
\]

The coefficient of \(x_ax_b\) is two, corresponding to the based words \(ab\)
and \(ba\).  In contrast,

\[
Z_{\rm ind}=(1-x_a)^{-1}(1-x_b)^{-1}
\]

has coefficient one.  At the cyclic level the discrepancy is the new
primitive necklace represented by \(ab\).  Thus a common reset base does not
give only the two atomic primitive cycles and their powers.

If \(a\) and \(b\) were meant to encode the prime factors \(2\) and \(3\), the
Dirichlet coefficient at \(6\) is already wrong.  Prohibiting every switch
\(a\to b\) splits the graph into atom-indexed components, which is precisely
the forbidden hand-built prime-component construction.

### Part 4: finite unitary twists

Let the cocycle products on \(a,b\) be \(U_a,U_b\in U(d)\).  The mixed
primitive orbit contributes

\[
\det(I-x_ax_bU_aU_b)^{-1}.
\]

Because \(U_aU_b\) is invertible,

\[
\det(I-tU_aU_b)
\]

is a degree-\(d\) polynomial in \(t=x_ax_b\) with constant coefficient one
and leading coefficient \((-1)^d\det(U_aU_b)\ne0\).  It cannot be identically
one.  A finite unitary cocycle therefore does not delete the mixed primitive
factor.

### Part 5: unary low-complexity prime grammar

For a unary context-free language, Parikh's theorem makes the accepted length
set semilinear.  In one dimension, semilinear sets are ultimately periodic.
Regular unary languages satisfy the same conclusion directly.

Suppose the rational primes were ultimately periodic with period \(m\) beyond
some threshold.  Choose a prime \(q\) beyond that threshold.  Then
\(q(1+m)\equiv q\pmod m\), so periodicity would classify \(q(1+m)\) as prime.
But \(q(1+m)\) is composite, a contradiction.  Hence no unary regular or
context-free return grammar accepts exactly the prime lengths.

Reference for the modern constructive form of Parikh's theorem:
[Esparza–Ganty–Kiefer–Luttenberger](https://doi.org/10.1016/j.ipl.2011.03.019).

## Corrections and Edge Cases

1. Part 1 is local to the holomorphy disk; it gives no automatic meromorphic
   continuation.
2. If positive \(F\) never crosses one, Part 2 makes no zero claim.
3. Binary encodings or computation shifts are not covered by the unary
   language theorem, but their arithmetic naturalness must be audited
   separately.
4. A fixed primality verifier would generate analogous determinants for
   composite-only, pseudoprime, or matched-density controls; that is a
   PROVES_TOO_MUCH risk, not an automatic escape.

## Open Risks

It remains **OPEN** whether a non-target-designed, low-description-complexity
countable grammar stronger than context-free can simultaneously generate
rational primes, an intrinsic logarithmic clock, the exact prime-power ledger,
and a canonical nuclear determinant.
