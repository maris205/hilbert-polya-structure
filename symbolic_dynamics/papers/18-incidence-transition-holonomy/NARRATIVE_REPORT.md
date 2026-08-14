# NARRATIVE REPORT — SD-C20

## One-sentence result

An intrinsic \(S_3\)-valued edge cocycle gives genuine noncommutative
holonomy on the tensor-subset shift, but its exact standard Artin block leaks
mixed monomials immediately, so the added symmetry is dynamically real and
arithmetically nonselective.

## Research question

Paper 17 showed that an atom-local one-letter parity fiber produces a genuine
same-object Artin factor, yet it merely clocks total cardinality and therefore
proves too much.  The only live loophole was to let the finite-group label
depend on a transition \((S,T)\) through the subset-incidence grammar.  Could
noncommuting refinement/coarsening holonomy suppress mixed primitives while
retaining the scalar Euler factor?

## Construction

Keep the same tensor-subset full shift and the same Koszul arrival weights.
Pass only to its two-block presentation.  Label strict refinements by
\(r=(12)\), strict coarsenings by \(t=(23)\), and all other transitions by
the identity.  This is natural under atom relabeling, compatible with
restriction, and contains no prime-indexed group data.

The cocycle is not a one-letter clock in disguise.  Singleton loops force any
candidate one-letter reference to be trivial, while the closed two-step word
\([p,pq]\) has holonomy \(rt\ne e\).  A four-step merge-order word has the
commutator holonomy \((rt)^2\), and two independent holonomies do not commute.

## Exact outcome

The trivial and sign blocks both remain \((1-x)(1-y)\).  The two-dimensional
standard block is

\[
(1-x)^2(1-y)^2+3xy(x+y)(xy+1)(x+y-1).
\]

Its logarithm differs from the identity/counting reference first at
\(x^2y\) and \(xy^2\), both with coefficient \(-3\), and at \(x^2y^2\) with
coefficient \(-6\).  Thus the very character capable of seeing the
nonabelian commutator also sees forbidden mixed atom products.  The
edge-separated four-cycle supplies a cancellation-proof marked certificate
with standard-character gap \(3\).

## Evidence beyond the theorem

Exact two-atom enumeration over all five local incidence values found no
all-irrep-clean nongauge table for \(S_3,D_4\), or \(Q_8\).  These finite
counts motivate a restricted rigidity conjecture, but known cospectral
phenomena prevent promotion to a general theorem.

## Analytic status

The same-object finite determinants are genuine.  The symmetric infinite
operator is trace class for every nontrivial incidence block only when
\(\operatorname{Re}s>2\); the trivial rank-one block already works for
\(\operatorname{Re}s>1\).  No continuation into the critical strip is
derived.

## Route decision

The construction clears the local legitimacy test and the weak determinant
stage, but fails arithmetic selectivity and robustness:

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

GO_GENUINE_TRANSITION_HOLONOMY
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH
ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Next in-family move

The failure is now located in the allowed-word grammar, not in the absence of
finite-group decoration.  The next batch should change the symbolic language
itself---for example, a constrained factorization, renewal, or countable
Markov presentation derived from tensor incidence---and demand a primitive
prime/prime-power correspondence before adding another fiber.
