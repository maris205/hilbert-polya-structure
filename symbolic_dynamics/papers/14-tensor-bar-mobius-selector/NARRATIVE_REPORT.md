# NARRATIVE REPORT

## Research question

Paper 13 left a precise obligation: determine whether tensor product,
entropy, and a finite-description local symbolic grammar can generate an
integer or abelian character that isolates the tensor-prime inventory without
loading a prime table.  Paper 14 answers that question and tests the closest
same-family escape.

## What failed

The abelian-character route is rigid for three independent reasons.

1. A monoidal charge is a valuation sum, so vanishing on both `p^2` and
   `p^3` forces vanishing on `p`.
2. A coherent cocycle on the thin tensor-divisor category is a coboundary and
   changes a transfer operator only by gauge conjugacy.
3. A regular entropy character merely translates `s` vertically, while pure
   presentation shuffles are conjugacies and cannot be forced to collapse.

This is a scoped no-go for standard functorial abelian characters, not for
all conceivable symbolic rules.

## What worked

The correct same-family escape is nonlinear incidence inversion.  SD-C16
stores every nonempty ordered factorization word as a return edge of one
countable symbolic shift, uses the entropy sum as its roof, and assigns the
fixed reduced-bar sign.  The raw weighted adjacency can be summed in
`Re(s)>sigma_bar`, its scalar Fredholm determinant is exactly `1/zeta(s)` at
`z=1`, and finite endpoint cancellation gives the tensor Möbius coefficient.
Differentiating the same determinant with respect to the roof parameter then
produces `Lambda_tensor=mu_tensor*h`.

This closes the narrow same-object concern: the signed factorization paths,
their repetitions, the determinant, and the roof derivative all belong to
one frozen symbolic object.

## Why the route still stops

The bar identity is universal.  Replacing the full-shift inventory by any
weighted countable inventory changes `B` but still yields
`D=1/(1+B)`.  The match to `1/zeta` is therefore inherited from the fact that
the all-full-shift entropy partition already equals `zeta`.  Moreover, the
primitive code cycles are factorization necklaces, not tensor atoms; the
prime-power ledger appears only after signed aggregation.

The correct conclusion is deliberately asymmetric: SD-C16 earns a genuine
analytic determinant and a derived Mangoldt-shaped coefficient, but earns no
orbitwise prime correspondence, arithmetic selectivity, new continuation,
critical-strip theorem, or RH consequence.

## Verification snapshot

All 18 unit tests and all 18 code/result checksum checks passed.  The global
incidence ledger contains 960 exact rows; at cutoff 512 all 117 prime-power
endpoints have the predicted support and all 394 mixed-factor endpoints have
exact zero innovation.  All 512 formal bar endpoints satisfy
`[n]F_bar=-mu_tensor(n)` and `[n]D_bar=mu_tensor(n)`.  The raw 80-digit audit
has maximum geometric-identity residual `1.913e-81`, and the 81-row trace-log
audit has final maximum residual `7.16e-30`.  Most importantly, all ten
generic-inventory controls satisfy the same reciprocal inversion exactly.
The numerical package therefore confirms both the construction and its
`PROVES_TOO_MUCH` obstruction.

## Route evaluation

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Next obligation

Paper 15 should act before determinant-level regrouping.  It must seek a
canonical primitive-cycle quotient or sign-reversing homological reduction
that is compatible with temporal repetition.  Success would leave exactly
one atom class and its powers for structural reasons; failure should be
promoted to a theorem that bar cancellation is universal algebraic inversion
and cannot support an orbitwise Euler realization.
