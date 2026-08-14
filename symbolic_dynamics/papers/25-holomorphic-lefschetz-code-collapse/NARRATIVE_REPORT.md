# Narrative Report — Paper25 / SD-C27

## Outcome

Paper25 closes the holomorphic-function-space loophole in the strongest
useful way: it finds a real positive escape and then identifies its exact
ceiling.  A scalar logarithmic-code composition branch carries the repeated
fixed-point factor \((1-q^r)^{-1}\).  No scalar normalization and no
ordinary trace-class tensor fiber can remove that factor at every power for
\(0<|q|<1\).  The canonical holomorphic de Rham \(0|1\) pair does remove it,
exactly and at the level of the full determinant.

The success is not cosmetic.  Each degree is an honest trace-class
holomorphic transfer operator on the frozen Bergman space for \(\Re s>1\),
and the numerator is the exterior character \(1-q^r\), not an ad hoc sign.
This is the first point in the current sequence where an analytic fiber
survives every repetition without collapsing the branch itself to rank one.

The independent exact suite passed 53/53 tests.  It verified 4,095 code
branches, 40 chain/characteristic identities, 320 power supertraces, and
1,183 primitive necklaces; all 1,174 mixed necklaces survived in the shared
assembly.  Forty-two inventory controls proved too much.  Two fresh
30-artifact code/results runs were byte-identical, and the 32-entry SHA-256
ledger passed; that certificate does not cover manuscript or documentation
files.  The 21 determinant and 168 power rows use the first four labels of
each finite fixture, while the 42 inventory controls use full-inventory sums
and \(z=1\) products at their frozen cutoffs.

The decisive failure occurs after cancellation.  The graded determinant
depends only on degree-zero cohomology.  A shared renewal disk has one
constant state, so its factor is

\[
 1-z\sum_jw_j,
\]

and every mixed primitive return necklace remains.  A disjoint family has
one constant state per disk, so its factor is

\[
 \prod_j(1-zw_j).
\]

That exact Euler product is determinant-equivalent to the diagonal operator
with one atom loop per supplied label.  The logarithmic code and all
nonconstant analytic modes live in an acyclic sector that cancels out.

## What advanced

The paper upgrades “anisotropic/analytic spaces might help” from an open
loophole to a classified mechanism:

1. positive contraction ratios \(q_n=2^{-\ell(n)}\) are compatible with
   full all-order cancellation;
2. the cancellation is canonical de Rham/Lefschetz functoriality;
3. both ordinary degreewise determinants are legitimate;
4. the full graded ratio, rather than a first-trace fit, is exact;
5. the shared and disjoint global assemblies can be computed without
   approximation.

This earns scoped `A2_ANALYTIC_DETERMINANT` credit.  It also corrects a
possible overstatement in SD-C26: holomorphic nuclearity is not universally
blocked.

## Why Route A still closes

The successful numerator cancels tangent stability for every return word.
It does not inspect branch content.  Shared recurrence therefore preserves
all legal mixed words, which fails the primitive prime ledger.  Removing
mixed words by putting labels on disjoint disks imports the selected
inventory as recurrent components.  The resulting cohomology operator
works without change for primes, squares, Fibonacci numbers, random sets,
hash sets, and arbitrary decidable inventories.

Two further ceilings remain.  At the original digit scale, codeword \(n\)
carries \(u^{\ell(n)}\), not one common marker \(u\).  Replacing it by one
\(z\) is an induced-return convention.  Analytically, the surviving prime
cohomology modes are \(p^{-s}\), so absolute trace class stops at
\(\Re s>1\).  Continuing the scalar function \(1/\zeta(s)\) does not
continue this operator family.

The frozen record is therefore

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Manuscript posture

The paper is written as a repair-and-collapse theorem, not a universal
no-go.  The exterior escape is presented prominently and credited to the
classical Lefschetz/Ruelle mechanism.  Novelty is confined to the explicit
scalar/tensor rigidity and the source-integrity classification of shared
versus disjoint logarithmic-code assemblies.

Three ownership distinctions remain visible throughout:

- ordinary degreewise determinants versus their graded ratio;
- shared recurrence versus disjoint recurrent components;
- original binary digit time versus induced completed-return time.

## Next obligation

Paper26 must move from tangent stability to branch combinatorics.  The
smallest live target is a source-derived cyclic incidence, bar, or
Hochschild-type complex on a shared renewal/factorization grammar whose
cyclic supertrace kills every mixed primitive necklace while retaining each
pure label and all of its repetitions.  The decisive alternative is that
its surviving cohomology again splits into one monochromatic sector per
supplied atom, proving determinant-equivalence to the disjoint inventory.
