# C187 test report

## Exact executable checks

- Producer: PASS — 36 rectangle rows, 441 iterate rows, 162 period rows, 441
  spectral rows.
- Independent checker: PASS — 230,034 assertions; no producer import.
- Direct enumeration: PASS — 26 rectangles and 37,401 tableaux.
- SymPy reconstruction: PASS — 3,065 checks.
- Canonical replay: PASS — 265,851 bytes, exact SHA-256 match.
- Mutation suite: PASS — 107 repaired-hash and one stale-hash rejection.

## Coverage

The checker reconstructs q-hook polynomials by direct polynomial division,
while the producer uses cyclotomic exponents.  It validates every formula row,
all Möbius populations, zeta/determinant factors, spectral multiplicities,
transpose symmetry, source attribution, exact Route-A qualifications and scope
flags.  Its independent tableau generator verifies promotion closure,
demotion inversion, evacuation involution, `e j e=j^-1`, all direct cycles,
every direct fixed count, and the actual promotion order on each selected
rectangle.

Finite regression does not prove Rhoades's all-rectangle CSP.  The source
theorem and the package's derived proofs are stated in `SOURCE_AUDIT.md` and
`THEOREM_PACKAGE.md`.
