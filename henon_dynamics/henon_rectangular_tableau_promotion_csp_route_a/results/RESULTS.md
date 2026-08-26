# C187 results

## Exact evidence

- Evidence payload SHA-256: `f783bb20cb45c9787024e753c2f8719c7e378fa90d8aed4edf9811062c6a5b0c`.
- Evidence file SHA-256: `7a56357284d543999d3ea7fab794629873743e0c9076ec044c55548239a8a801`.
- Evidence bytes: 265,851.
- Formula rectangles: 36.
- Every-iterate rows: 441.
- Period rows: 162.
- Spectral rows: 441.
- Direct-enumeration rectangles: 26.
- Directly constructed tableaux: 37,401.

The largest formula sentinel is `6 x 6`, with
`1,671,643,033,734,960` tableaux.  It is handled by exact formulas, not by
enumeration.  The `2 x 2` sentinel has q-hook polynomial `1+q^2`, one
two-cycle, and actual promotion order two.

## Verification

- Independent checker: 230,034 assertions.
- Separate SymPy reconstruction: 3,065 checks.
- Byte replay: exact.
- Mutation suite: 107 repaired-hash rejections and one stale-hash rejection.

## Verdict

The full finite-dynamical structure is exact and source native.  It supplies no
intrinsic rational-prime semantics or target divisor.  Verdict:

`A0_FAIL / A1_WEAK / A2_FAIL / A3_FAIL / A4_NATURAL_QUANTIZATION`, overall
`ROUTE_A_REJECTED`, Route B false.
