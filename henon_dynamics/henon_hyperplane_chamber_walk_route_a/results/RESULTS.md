# Exact results

The canonical producer emits eight cases: six separating and two
nonseparating.  Their aggregate census is:

| Quantity | Count |
|---|---:|
| faces | 316 |
| chambers | 94 |
| flats | 75 |
| transition cells | 1,604 |
| nonzero stationary probabilities | 62 |
| mixing rows | 24 |
| trace rows | 48 |

The independent checker passes 20,609 assertions.  The separate SymPy oracle
passes 3,398 checks, including exact characteristic-polynomial, determinant,
trace, and diagonalizability checks.  Byte replay reproduces the 116,204-byte
evidence file.  The hostile suite rejects 74 semantic repaired-hash mutations
and one stale-hash mutation.

Evidence payload SHA-256:
`82b486a8f4e1dcfd9f532c9cc76847874276e7c214783c92a51b399817a876d9`.

Evidence file SHA-256:
`7a6e111aeb06f2d47ec9f0830958edca762f1f7d73ef3f6e6c1b26f3e4539b8b`.

These are finite regression results.  The all-arrangement theorem is attributed
to Brown--Diaconis and is not inferred from the census.
