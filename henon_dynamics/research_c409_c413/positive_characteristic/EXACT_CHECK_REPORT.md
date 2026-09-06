# Bounded exact checks for the wild cubic scout

Executed on 2026-09-06 with

    python3 -B wild_cubic_exact_checks.py

The process exited with code zero. The script is stdout-only; it does
not mutate any old batch, generate a manuscript, or run a finite-field
parameter census. The non-author proof review is a separate activity.

## Actual checks

- The three expressions in the cubic normal form all map to
  `a^3(z^3-z)^2` over `F_3[a,z]`.
- Their product equals that parameter, and the cubic discriminant is
  exactly `a^3 t` modulo three, including the constant.
- For `a=1` and heights `1,...,5`, polynomial iteration gives degrees
  `3,9,27,81,243`, zero multiplicities `2,4,8,16,32`, and derivative
  degrees `1,4,13,40,121`.
- The height-one zero-place parity matrix has F_2-rank two.
- The four infinity principal-part rows
  `(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)` have global F_3-rank three,
  while each individual row has rank one. These directly check the
  distinct global/local ranks used in the height-two field argument.
- The resulting height-two degree is `6*4*27=648`.

GAP independently constructed the abstract signature kernels by a
two-coset Schreier procedure and computed their orders and the span of
the orbit of an embedded binary-subtree support:

| Height | Group order | Support-orbit size | F_2 valuation-span rank |
|---|---:|---:|---:|
| 1 | 6 | 3 | 2 |
| 2 | 648 | 27 | 6 |
| 3 | 816293376 | 2187 | 18 |

The largest enumerated orbit has 2187 elements. The script imposes a
45-second subprocess limit and does not enumerate the entire height-three
group. GAP constructs the *classical model group*, not a function-field
Galois group; that distinction is an explicit output boundary.

The different/genus formulas were cross-checked with exact rational
arithmetic through height five. The first values are

| Height | e(0) | d(0) | e(infinity) | d(infinity) | Genus |
|---|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 6 | 7 | 0 |
| 2 | 4 | 3 | 18 | 25 | 46 |
| 3 | 8 | 7 | 54 | 79 | 137938465 |

No finite test proves the all-height theorem, and no `p>3` theorem was
tested or inferred. The excluded `a=0` face is purely inseparable and is
not included in any displayed group assertion.
