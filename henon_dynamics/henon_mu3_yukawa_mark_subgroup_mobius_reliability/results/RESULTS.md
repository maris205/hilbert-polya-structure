# C77 results

The canonical C77 evidence JSON records the complete subgroup-lattice
reliability atlas.  It is source-bound to C73, C75, and C76 authorities.  The
canonical C77 evidence hash is
`f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634`.
The C76 evidence and manifest hashes are:

```text
42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94
55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5
```

The top row is also checked against C73 evidence hash
`e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5`.

## Ordered subgroup summary

| index | `|H|` | `n_H` | direct supports |
|---:|---:|---:|---:|
|0|1|5|32|
|1|2|6|32|
|2|3|7|96|
|3|3|6|32|
|4|3|7|96|
|5|3|6|32|
|6|6|8|96|
|7|6|7|32|
|8|6|8|96|
|9|6|7|32|
|10|9|11|1760|
|11|9|7|64|
|12|9|7|64|
|13|9|8|192|
|14|18|12|1760|
|15|18|8|64|
|16|18|8|64|
|17|18|9|192|
|18|27|15|30400|
|19|54|16|30400|

The direct support totals sum to `65536`.  For every row, the polynomial
obtained from direct support sizes equals the Möbius inversion of
`q^(16-n_H)` over the actual subgroup poset.

## Top reliability law

```text
P_{=Q}(q) = 1-q-q^4+q^5-q^7-q^8+5q^9-3q^10
          = (1-q)(1-q^4-q^7-2q^8+3q^9).
```

This is exactly the C73 homogeneous deletion reliability polynomial.  The
equality is a cross-generation consistency check, not a new arithmetic claim.

## Scope

The result is a finite generating-closure probability atlas for the named
coordinates.  It does not claim a full Burnside ring/table of marks,
arithmetic or local data, Euler factors, root numbers, automorphy, or a
Hilbert--Polya operator.
