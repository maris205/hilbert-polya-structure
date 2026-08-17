# Strict Route-A v0.2 status audit for SD-C42

Status: `POST_CANONICAL_DEPENDENT_RENDERING`
Source lock: `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041`
Mayer boundary: `a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5`
Control result: `d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f`
Independent control: `729287849f36046b8aa21d8dba615650f4289dd1d3202c1783cc41af207c4d92`

This audit re-evaluates every coordinate from the literal strict Route-A
v0.2 obligations after the canonical replacement run.  It is not an inherited
SD-C04 or P39 verdict and is not a prospective preregistration.

## A0: `A0_WEAK_ARITHMETIC_RELATION`

The positive continued-fraction digit grammar and exact `SL_2(Z)` monodromy
are intrinsic arithmetic data.  This earns weak arithmetic relevance only.
The exact three-projection disjunction fails: trace and order discriminant are
integer-valued but fail full rational-prime support, multiplicity, clock, and
powers; geodesic norm passes clock and powers but is irrational and retains
the Mayer stability amplitude.

All seven literal A0 controls execute: shuffled generated primes,
prime-density-matched random integers, composites only, composite base-2
pseudoprimes, randomized arithmetic labels, neighboring digits, and the
simpler digit-shift parent.  Each has a raw-record mutation that both
implementations reject.  Because no positive rational-prime signal exists,
the rung cannot exceed weak arithmetic relation.

Verdict: `A0_WEAK_ARITHMETIC_RELATION`, evidence `PROVED`.

## A1: `A1_PASS_ANALYTIC`

Paper 40 newly derives the `rho` pair ledger; it does not inherit pair A1
credit from the SD-C04 `sigma` digit ledger.  The grouping conjugacy
`rho iota=iota sigma^2`, pair primitivity, exact splitting law, rotation-only
orientation, reversal metadata, complete bounded census, monodromy,
multiplicity, sign, phase, derivative multiplier, stability weight, temporal
powers, digit marker, and raw `K_s^k` branch order are all recomputed.

All six literal A1 controls execute: shuffled source periods, signed rational
weights, nonzero phases modulo 97, same-density random lengths, neighboring
parameters, and the simpler parent.  Mutations cover identity shuffles,
canonical weights/phases, length-density mismatch, wrong parent/neighbor,
missing or silently quotiented reversal data, multiplicity, sign, exact root
selectors, and stability denominator.

This rung is typed only to `RhoPrimitivePair`; it supplies no
`SigmaPrimitiveDigit` or `GeodesicPrimitiveClass` bridge and no rational-prime
ledger.

Verdict: `A1_PASS_ANALYTIC`, evidence `PROVED`.

## A2: `A2_ANALYTIC_DETERMINANT`

On Mayer's source-supported holomorphic Banach-space realization,
`K_s=L_s^2` is nuclear in the stated domain and owns

\[
D_{42}(s,u)=\det(I-u^2K_s).
\]

For `u=1`, Mayer's Proposition 3 gives the holomorphic identity

\[
Z(s)=\det(I-L_s)\det(I+L_s)=\det(I-L_s^2)
\]

on `Re(s)>1/2`.  The Euler-product interpretation is initially absolutely
convergent on `Re(s)>1`; Corollary 3 gives meromorphic continuation to the
complex plane.  These three domains are not conflated.  The arbitrary-`u`
marker is bookkeeping, and the `u=1` function identity is not an objectwise
pair/geodesic bijection.

The A2 target comparison is the reciprocal determinant `D_42^-1`.
Coefficientwise/formally in `u^2`, or analytically for sufficiently small
`|u|`, its positive trace coefficient is
`u^(2kr)d_w^(rs)/(r(1-d_w^r))`.  No single-valued logarithm is continued
through determinant zeros; `u=1` uses only Mayer's separate theorem.  No
finite matrix determinant, selected scalar subproduct, or target-zero fit
earns this rung.

Verdict: `A2_ANALYTIC_DETERMINANT`, evidence `PROVED`.

## A3: `A3_PARTIAL_ANALYTIC_STRUCTURE`

The same source-owned determinant has the modular Selberg-zeta/Fredholm
identity and its source-supported continuation.  This is genuine global
analytic structure.  It is nevertheless the modular Selberg divisor, not the
completed rational-prime Riemann divisor.  The required Gamma/pole/trivial-
zero ledger, Riemann--von Mangoldt count, target multiplicities, and same-clock
Weil compression are absent.  No objectwise primitive-orbit bridge is inferred
from the function identity.

Verdict: `A3_PARTIAL_ANALYTIC_STRUCTURE`, evidence `PROVED`.

## A4: `A4_FORMAL_HINT`

Known modular geometry supplies a spectral carrier for the Selberg function
and hence formal Hilbert--Polya context.  SD-C42 does not define a new quantum
operator, domain, phase/weight theorem, target multiplicity theorem, or
same-clock rational-prime lift.  Known modular geometry cannot manufacture
the missing rational-prime selector.

Verdict: `A4_FORMAL_HINT`, evidence `PROVED`.

## Exact projection truth matrix

| Projection | Integer-valued | Exact clock | Temporal powers | Full rational-prime GO |
|---|---:|---:|---:|---:|
| trace | pass | fail | fail | fail |
| order discriminant | pass | fail | fail | fail |
| geodesic norm | fail | pass | pass | fail |

The geodesic norm row is essential: the final terminal code does not assert
that every projection fails clock or repetition.  It asserts only that no
integer-valued projection passes both.

## Overall verdict and terminal tuple

```text
(A0_WEAK_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false

GO_MODULAR_PRIMITIVE_LEDGER
GO_SAME_OBJECT_MAYER_DETERMINANT
STOP_CANONICAL_INTEGER_PROJECTION
STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION
STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED
ROUTE_A_REJECTED
```

`STOP_CANONICAL_INTEGER_PROJECTION` is the failure of the complete
rational-prime reciprocal-Euler-ledger conjunction.  The separately named
`STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION` is the empty intersection
of integer-valued support with exact clock and powers.  The ownership STOP is
an absence-of-declared-owner fact for the hash-frozen untwisted schema, not a
universal nonexistence theorem.

The GO codes refer only to the intrinsic pair ledger and its same-object Mayer
determinant.  They carry no rational-prime, digit-primitive, or
geodesic-primitive credit.  Route B remains locked.

## Canonical evidence

The producer derived fourteen conjunctive gates with zero failures.  The
no-import independent evaluator recomputed twenty-three checks with zero
failures and rejected producer-payload tampering.  The exact prototype and
independent replay add six bounded runs, 39,622 scientific rows, all three
collision classes, the return-map/splitting certificates, and the direct raw
branch/weight fixture, with zero theorem failures.  These results verify the
locked finite obligations; they do not change the pre-run projection family
or decision rule.

## Chronology and novelty boundary

The v1 outputs and several in-flight corrective smoke outputs were known
during M1--M20.  Only the exact fifteen-file corrected input set in
`CONTROL_LOCK.md` was frozen before the one canonical replacement rerun.
This audit, the proof files, and the literature renderings are post-run and
nonprospective.  Post-run M21--M25 repair a proof implication, supply the
intrinsic pair Fredholm regrouping, restore holomorphic branch language,
restore the literal Route schema, and localize the Fredholm logarithm/product
in `u`, without changing any locked input, canonical output, theorem
conclusion, or Route coordinate.  No correction, witness, or Route rendering
receives novelty or priority credit.
