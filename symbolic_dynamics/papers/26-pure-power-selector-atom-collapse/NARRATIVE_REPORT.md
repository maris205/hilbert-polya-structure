# Narrative Report — SD-C28

## Outcome

Paper25 found a genuine holomorphic all-order cancellation but left mixed
return necklaces in a shared renewal system.  SD-C28 asks for a cyclic
incidence selector that keeps `a_i^r` with coefficient one and kills every
word containing two colors, without first separating the colors.

The selector exists twice.  An exterior algebra on the reduced support of a
completed word has superdimension `(1-1)^(|S|-1)`.  Coordinate projectors give
a fixed stationary trace realization.  The first is exact but word-indexed;
the second is exact but visibly allocates one line per supplied color.

The main theorem shows that this is not an artifact of the obvious
construction.  The selector's Hankel rank is `m` under the trace-compatible
empty-word convention and `m+1` under the literal language convention.  Its
observable syntactic algebra is `C^m` or `C^(m+1)`.  Every finite ordinary
trace realization semisimplifies to one one-dimensional character per color,
plus dormant zero-action modules.  Every even graded realization has the same
virtual class, up to matched even/odd sectors.  Triangular radicals may make
the literal matrices connected and noncommuting, but they change no cyclic
trace or determinant.

The full determinant therefore equals the product of supplied color factors.
This conclusion requires wordwise traces.  A three-color matrix-unit adversary
passes all commuting aggregate power identities while assigning `+1` and
`-1` to the two opposite oriented words `012` and `210`.

Canonical homological constructions do not reopen the route.  A shared free
bar complex retains mixed necklaces.  The separable algebra `C^m` deletes
them, but its Hochschild homology is only its `m` degree-zero atom classes.
Tensoring with the Paper25 holomorphic de Rham sector gives an honest
trace-class graded determinant on `Re(s)>1`; orthogonal coordinate projectors
make it unitarily the disjoint direct sum of supplied atom blocks.

## Strongest result

The exact selector is classified at all three relevant levels: minimal
recognizable memory, semisimplified/virtual character, and full cyclic
determinant.  Radical and parity freedoms are retained honestly, while their
invisibility to the determinant is proved rather than assumed.

## Main obstruction

Exact wordwise cancellation costs one observable simple sector per supplied
label.  In the countable limit that sector becomes `ell^2` coordinate memory.
The construction selects any inventory equally well and therefore does not
derive arithmetic atoms from finite source dynamics.

## Route verdict

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The A2 credit belongs to the separately honest degreewise trace-class
operators and their graded ratio on `Re(s)>1`.  No same-object continuation or
self-adjoint spectral mechanism is constructed.

## Paper27 minimum obligation

The next candidate must derive a countable incidence compiler from the source
factorization/divisibility structure rather than install coordinate
projectors for a supplied inventory.  It must preserve necklace-resolved
coefficients, all repetitions, and the digit marker; prove an honest
trace-class or relative-determinant domain; and either escape finite
recognizability with controlled infinite memory or accept atom collapse and
use new analytic geometry to obtain same-object continuation.  Aggregate
Euler matching alone is inadmissible.

