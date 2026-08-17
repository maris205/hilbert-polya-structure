# Theorem targets and falsifiers

## T0 — source convention fidelity

Target: the frozen full-shift convention gives `q^r` fixed points,
`N_q(n)` primitive necklaces, and `D_q(s,z)=1-zq^(1-s)`.

Defeat the package if an independent derivation under the exact `SD-C01`
normalization gives a different fixed-point count, marker exponent, clock, or
determinant. A transposed graph presentation is harmless only if it preserves
these owned quantities exactly.

## T1 — total same-clock rational-prime map

Target: no total `pi:Prim_q -> P` preserves
`log pi(gamma)=|gamma| log q`.

Falsifier: exhibit a rational prime equal to `q^2` for any frozen `q`, or show
that `[01]` is not a primitive necklace in the frozen full shift.

Non-falsifiers: omit `[01]`, use a partial map, alter the clock, map to prime
powers or finite-field prime polynomials, or enlarge the object.

## T2 — factor marker/weight/multiplicity non-descent

Target: no factorwise identification preserves all three fields.

Falsifier: provide a bijection of all source factors to rational-prime factors
such that each identity

```text
z^n q^(-ns) = z p^(-s)
```

holds and target multiplicity is exactly one.

Non-falsifiers: merge the `q` length-one source factors, delete factors,
specialize `z=1`, replace `z^n` by `z`, or retain only one orbit. Each changes
a locked field.

## T3 — first marked coefficient mismatch

Target: `q^(1-s) != P(s)` as analytic functions on `Re(s)>1`.

Falsifier: prove equality on a nonempty open subset of the common domain. A
single accidental numerical equality at one `s` is not a falsifier of the
analytic statement.

Independent check: verify the large-real-`s` limits after multiplication by
`2^s` for `q=2,3,5`.

## T4 — source positive control

Target: the source ledger remains exact for monic irreducible polynomials over
`F_q` by degree and norm.

Defeat the package if the necklace polynomial fails to count both aperiodic
necklaces and monic irreducibles, or if the affine-line zeta normalization is
not `1/(1-qT)` with `T=q^(-s)`.

This target is critical: if the negative theorem is obtained by breaking the
source ledger itself, the paper has changed the historical object.

## T5 — repair classification

Target: every row in the declared repair matrix loses at least one locked
field.

Falsifier: identify a listed row that actually preserves rational-prime
support, exact source clock, original marker, full multiplicity, and source
operator ownership simultaneously.

Non-falsifier: propose an unlisted new construction. That narrows the
exhaustiveness claim and requires a new source lock; it does not falsify the
row-by-row statements.

## T6 — strict Route tuple

Target:

```text
(A0_WEAK_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)
```

Defeat or revise the tuple if the narrowed object changes a source coordinate,
if the theorem incorrectly converts its own valid function-field ledger into
an A1/A2 failure, or if the same object acquires completed analytic or natural
lift structure. No coordinate may be borrowed from another candidate.

## Stop codes

```text
STOP_SOURCE_CONVENTION_MISMATCH
STOP_INVALID_TOTALITY_OR_MARKER_REQUIREMENT
STOP_DUPLICATE
REVISE_QUANTIFIER_SCOPE
REVISE_ROUTE_TUPLE
```
