# C144 results

- Structural theorem: `X_TM` is nonempty, minimal, uniformly recurrent, and
  contains no shift-periodic point.
- Fixed-point counts: zero for every positive shift period; replay receipts
  through period 32.
- Artin--Mazur zeta: exactly `1`.
- Language complexities for widths 1 through 16:
  `2,4,6,10,12,16,20,22,24,28,32,36,40,42,44,46`.
- Periodic approximants: levels 2 through 12, all with least period `2^k`.
- Local defect cells: 145; all audited width-at-most-16 rooted windows are
  intrinsic.
- Macroscopic control: at levels 2 through 9 all rooted windows of width
  `2^(k+1)+1` are extrinsic.
- Independent checker: 172,437 assertions.
- SymPy: 83 exact checks.
- Mutation audit: 36 repaired-hash and one stale-hash case rejected.

Evidence SHA-256 is filled and checked by the release manifest.  The result
does not invoke Route B or compare a target divisor.
