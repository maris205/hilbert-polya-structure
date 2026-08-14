# NARRATIVE REPORT

## Question inherited from Paper 14

Paper 14 produced \(1/\zeta\) from a reduced tensor-word shift, but its
primitive orbits were factorization necklaces rather than tensor atoms.  It
left one precise Symbolic Dynamics question: can bar cancellation be reduced,
before determinant-level aggregation, to an atom-only primitive grammar that
respects repetitions and symmetries?

## Bold hypothesis

The natural candidate was a Koszul-shaped reduction.  For a finite atom set,
keep one scalar edge for each nonempty squarefree subset and give it the
alternating coefficient \((-1)^{|S|+1}\).  Inclusion--exclusion immediately
gives

\[
  1-\sum_{S\ne\varnothing}(-1)^{|S|+1}x_S
  =\prod_a(1-x_a).
\]

The countable tensor specialization is therefore \(1/\zeta(s)\) in
\(\operatorname{Re}s>1\).  This is the strongest plausible algebraic
compression of the Paper 14 bar inventory.

## Where the lift fails

The determinant identity hides three incompatible ledgers.

1. At content \(pq\), the positive primitive \([p][q]\) and negative
   primitive \([pq]\) appear to pair.  At \(p^2q^2\), however, there is one
   positive primitive and two negative primitives.  The missing positive
   unit comes from the second powers of both lower-content \(pq\) cycles.
   Cancellation therefore crosses primitive and temporal-power layers.
2. At squarefree content \(pqr\), positive and negative dimensions both equal
   three, but the positive \(S_3\)-set splits into orbits of sizes \(1+2\)
   while the negative side is one orbit of size \(3\).  The virtual character
   is \((0,0,3)=\mathbf1+\mathrm{sgn}-\mathrm{Std}\).  No equivariant pairing
   exists.
3. A negative scalar edge has repetition sign \((-1)^r\); an odd chain line
   has one fixed supertrace minus sign.  They already disagree at \(r=2\).
   A genuine acyclic even/odd sector has zero supertrace at every power and
   hence graded determinant one.  It is determinant-invisible rather than a
   hidden source of the scalar Euler factor.

The bar differential also refuses to stay inside a primitive-cycle layer:
merging adjacent letters can send a primitive word to an imprimitive word and
vice versa.  Thus "take primitive homology first" is not an available chain
operation.

## Classical algebraic boundary

The normalized bar resolution of a polynomial algebra does reduce to the
Koszul resolution, but its homology is the full exterior algebra
\(\Lambda V\).  Mixed classes such as \(e_p\wedge e_q\) survive.  Hochschild
homology likewise retains mixed differential forms under HKR.  Harrison or
André--Quillen theory isolates indecomposable commutative directions only by
passing to a different quotient/Hodge component; it is not a primitive-cycle
equivalence preserving the symbolic trace.

These are classical facts.  SD-C17's contribution is to combine them with
the exact primitive/power and equivariant ledgers required by the Route-A
source lock.

## Verification snapshot

The exact prototype enumerates cyclic set partitions through seven atoms and
checks the Stirling identity through twelve.  It certifies the
\(p^2q^2\) and \(S_3\) obstructions, checks scalar versus supertrace powers
through repetition eight, and passes 112 rational-inventory controls.  Every
mixed squarefree scalar coefficient cancels, and precisely for that reason
the construction is universal rather than arithmetic-selective.

## Route decision

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The next in-family direction is not another scalar pairing.  It is a
character-resolved cycle-index determinant that retains the nontrivial
\(S_k\) modes erased by scalar dimension.  That direction remains Symbolic
Dynamics and is not a Route-B invocation.
