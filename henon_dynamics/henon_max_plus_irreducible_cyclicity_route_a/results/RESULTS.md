# C188 results

## Exact evidence

- Evidence payload SHA-256:
  `168e569e18292d551025a039d90998c1740d1af45de8de089de9e4f85671f438`.
- Evidence file SHA-256:
  `d7fc6d5211b5c716ef2f507ce6ba07646a40653ee2a1bb5bc2ac792c43d21b4e`.
- Evidence bytes: 781,170.
- Matrices: 177.
- Vector/projective rows: 901.
- Simple cycles: 441.
- Critical components: 189.
- CSR cells checked by the producer: 5,469.
- Period-propagation cells checked by the producer: 7,471.

The `gamma` spectrum is: 120 matrices with `gamma=1`, 48 with `gamma=2`, five
with `gamma=3`, one with `gamma=4`, one with `gamma=5`, and two with
`gamma=6`.  Twenty-eight tested raw vector orbits and the same 28 projective
orbits have period strictly smaller than their matrix's `gamma`.

The largest observed exact transient and CSR transient are both 24, attained
inside the declared `B_m` family.  The family proof covers every `m>=1`; the
finite cutoff at 24 is regression only.

## Verification

- Independent checker: 7,924 assertions.
- SymPy reconstruction: 10,615 checks.
- Canonical replay: byte exact.
- Mutation suite: 137 repaired-hash and one stale-hash rejection.

## Verdict

`A0_FAIL / A1_WEAK / A2_FAIL / A3_FAIL / A4_FAIL`, overall
`ROUTE_A_REJECTED`, Route B false.
