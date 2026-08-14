# Experiment Report — SD-C21 Stationary Semiring Sieve Shift

## Outcome

The exact suite verifies the first clean primitive/repetition ledger in this
full-shift-semiring line and simultaneously identifies why it is not a Route-A
advance.  The expanded quotient-search graph accepts exactly the rational
primes without a prime table or factor-existence helper.  Its only primitive
cycles are the accepted self-loops, and one trace-class weighted adjacency
satisfies

\[
\operatorname{Tr}(L_s^r)=\sum_p p^{-rs},
\qquad
\det(I-zL_s)=\prod_p(1-zp^{-s})
\]

on (operatorname{Re}s>1).  Yet every computation state is transient.  The
same traces and determinant remain after pruning the verifier to the diagonal
prime-loop core, and arbitrary total deciders compile their own support in
the same way.

Frozen verdict:

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
SELECTOR_TAUTOLOGICAL / PRUNING_EQUIVALENT / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

No target-zero data, root fitting, cross-family carrier, or Route-B operator
was used.

## Explicit no-oracle certificate

The scientific source contains zero occurrences of the forbidden identifiers
`tensor_divides`, `exists_factor`, `factor_exists`, and `has_factor`.  Its
audited verifier functions make zero calls to `any`.  At cutoff 64, the actual
expanded graph contains:

| quantity | exact count |
|---|---:|
| quotient states | 1,651 |
| quotient-source edges | 1,651 |
| quotient-successor edges | 1,521 |
| quotient-to-reject edges | 45 |
| quotient-to-next-divisor edges | 85 |
| accepted/recurrent loops | 18 |

All AST and graph checks pass.  This certificate proves local implementation
of cofactor search; it does not remove the later selector-tautology result.

Primary artifact: `results/source_oracle_certificate.json`.

## Support and recurrent-core certificates

Independent support validation gives zero false positives and false negatives
at every frozen cutoff:

| cutoff | accepted primes | false positives | false negatives |
|---:|---:|---:|---:|
| 32 | 11 | 0 | 0 |
| 64 | 18 | 0 | 0 |
| 128 | 31 | 0 | 0 |
| 256 | 54 | 0 | 0 |
| 512 | 97 | 0 | 0 |

At cutoff 24 the expanded graph has 296 vertices and 282 retained edges.
Exactly nine vertices are recurrent, namely the loops at
(2,3,5,7,11,13,17,19,23); the remaining 287 vertices are transient.

## Trace and determinant certificates

At (s=2), all twelve rational power traces agree exactly with
(sum_{p\le24}p^{-2r}).  The independent dense Bareiss audit at cutoff 8
uses 37 vertices and 34 edges.  At (z=1/3), both the full graph determinant
and the accepted-loop product are

```text
772486 / 893025.
```

These finite checks are regressions for the theorem-level trace and Fredholm
identities; no finite prefix is promoted to a continuation statement.

## Trace-class boundary

Quotient edges use denominator (ndq), so their absolute entry sum is bounded
by a product of three convergent Dirichlet series for every
(operatorname{Re}s>1).  Input/divisor and cemetery sectors have one- or
two-series majorants.  The complete rank-one edge expansion is therefore
trace class and locally holomorphic on that half-plane.

Finite entry-sum rows were generated at five cutoffs and real parts
`1.1,1.25,1.5,2.0`.  At cutoff 512 they are respectively approximately
`17.0961, 8.06511, 3.03265, 0.882212`.  These floats are diagnostic displays;
the analytic majorant is the proof.

## Structural and neighboring controls

- Transporting both semiring operations through a shuffled presentation
  preserves all 97 accepted values at cutoff 512.
- Shuffling entropy relative to objects changes the (s=2) trace.
- The additive-only parent accepts 511 values and has 414 false positives.
- Bounded trial depths `2,3,5,7,11` leave respectively
  `159,75,42,23,13` false positives.
- Replacing the target by (n+1) has symmetric difference 191 from the prime
  support.
- Across 32 matched random supports, prime overlap accuracy ranges from about
  `0.124` to `0.227`.

These controls confirm that the expanded integer-semiring verifier is exact
and nontrivially uses both operations.  They do not establish uniqueness of
its dynamical mechanism.

## Compiler controls and decisive no-go

The polynomial-UFD control enumerates monic irreducibles over
(mathbf F_2) through degree eight.  Its Euler coefficients are exactly

```text
1, 2, 4, 8, 16, 32, 64, 128, 256.
```

Four total-decider wrappers select squares, powers of two, Fibonacci values,
and a fixed hash predicate.  In every case the recurrent SCCs equal the
declared accepted loops and an independent rational determinant equals the
corresponding loop product.

This is stronger than a failed random control: it proves that the wrapper is
a generic compiler

\[
S\longmapsto\prod_{n\in S}(1-zn^{-s})
\]

for any decidable support (S).  The rational-prime result is therefore
source-intrinsic and exact, but not arithmetically selective.

## Verification status

- thirteen exact tests: passed;
- explicit Q-state/no-oracle audit: passed;
- support at all five cutoffs: exact;
- SCC and twelve power traces: exact;
- independent dense determinant: exact;
- polynomial-UFD compiler: exact;
- four arbitrary total-decider wrappers: exact;
- target-zero fields: not applicable and unused;
- Route B invocation: false.

The deterministic orchestrator regenerates the scientific artifacts,
analysis, tests, schema/integrity audit, and SHA ledger twice and requires
byte-identical ledger bytes.

## Next smallest in-family obligation

The next candidate must forbid verifier-generated accept self-loops.  It
should place alphabet successor and tensor multiplication inside recurrent
transitions on all nonunit full-shift objects and test primitive-cycle
separation from addition-shuffled, multiplication-shuffled, composite,
random-divisibility, and factorial-monoid controls before any new continuation
or holonomy program.

Any geometric carrier, scattering system, or self-adjoint realization remains
only a `ROUND2_CLUE` outside this Symbolic Dynamics session.
