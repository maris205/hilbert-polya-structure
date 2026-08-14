# Preregistration — Paper 33 / SD-C35

## Research question

Can the exact Paper-32 projective-residue recurrent object be repaired by a
source-natural chain quotient or twist that kills the universal presentation
cycles and cusp diamonds while preserving a prime-selective primitive ledger
and same-marker determinant ownership?

## Frozen candidate

Use the same `P^1(Z/nZ)` blocks, `S,R` actions, cusp correspondences, roofs,
and marker as Paper 32.  Over `Q`, quotient by `im(1+S)+im(1+R+R^2)` and fill
every `n,2n,6n,3n,n` square as a two-cell.  No block selection, field defect,
prime table, factor table, target zero, fitted sign, replacement roof, or
Route-B input is permitted.

## Primary success condition

The positive candidate would require all of the following:

1. composite primitive cycles are removed before weights;
2. the quotient/twist is not equivalent to the static field projector;
3. the inherited graph-step operator descends with the same free edge marker;
4. the resulting determinant is owned by the same object;
5. controls do not reproduce the same ledger generically.

## Stop conditions

Stop and close the semiring-residue family if any of the following is proved:

- relative quotient homology is nonzero on prime powers or mixed composites;
- a universal cusp or generic presentation-action survivor remains;
- diamond filling removes all cross linkage rather than selecting primes;
- character/supercharacter cancellation is generic rather than arithmetic;
- `S+R` fails to preserve the relation subspace.

Paper 33 realizes all five stop conditions.

## Finite audit

- Moduli: `2..192`.
- Coefficient field for rank checks: `F_1000003`.
- Matched relabels: seed `1003003+n`.
- Random controls: 64 transitive `C2*C3` actions, seeds `330000..330063`.
- Characters: all six 1D characters of `C6`.
- Zero-superdimension controls: all 15 pairwise differences.
- Target-zero data: none.

## Route rule

If stopped, record the tuple

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

and set `route_b_invocation_allowed: false`.
