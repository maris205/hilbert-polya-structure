# SD-C18 Obstruction Registry

## O18.1 — Augmentation blindness

At squarefree content `pqr`, positive and negative primitive-cycle counts
agree, but their virtual `S_3` class is
`[S3/S3]+[S3/C3]-[S3/C2]`, with character `(0,0,3)` and subgroup marks
`(0,0,3,1)`. Scalar dimension therefore loses genuine recurrent label
motion.

**Type:** proved representation/Burnside obstruction with exact certificate.

**Decision:** `GO_FORMAL_EQUIVARIANT_LEDGER`; scalar cancellation alone is not
an equivariant cancellation theorem.

## O18.2 — Fixed arithmetic fiber has no relabeling symmetry

The transfer family is semilinearly covariant under simultaneous label and
variable permutation. After distinct prime-weight specialization, its fixed
fiber has stabilizer order one. Equalizing weights restores `S_n`, but the
rank-one image is the trivial line and every nontrivial-isotype determinant
equals one.

**Type:** proved fixed-fiber symmetry/visibility dichotomy.

**Decision:** `STOP_CHARACTER_FREDHOLM_FIBERS` for the canonical rank-one
realization.

## O18.3 — Rank-one and diagonal power ghosts disagree

The rank-one edge transfer satisfies `tr(A_x^r)=b(x)^r`; the canonical
representation-preserving diagonal subset lift satisfies
`str(D_x^r)=b(x^r)`. For every frozen `n=2..8,r=2..8`, the coefficient of
`x_1^(r-1)x_2` is `r` in the former and zero in the latter.

**Type:** proved all-parameter witness, independently checked in 56 rows.

**Decision:** `STOP_STANDARD_SUPERTRACE_INTERPRETATION`.

## O18.4 — Analytic lift changes the determinant

The diagonal lift has
`sdet(I-D_x)=product_(S nonempty)(1-x_S)^epsilon(S)`, hence mixed-subset
factors. For two weights `1/4,1/9`, the pure Euler determinant is `2/3`, while
the diagonal superdeterminant is `24/35`; all frozen `n=2..8` mismatch.

**Type:** proved determinant incompatibility.

**Decision:** `A2_FAIL`; the scalar A2 shadow and resolved lift cannot be
combined coordinatewise.

## O18.5 — Integer Adams signs are the wrong carrier

An ordinary negative edge repeated `r` times contributes `(-1)^r`, whereas
the integer Adams image of `-1` remains `-1`. The auxiliary nontrivial `C_2`
character line reproduces all 4,008 frozen scalar powers; the naive integer
substitution fails in 988 cases.

**Type:** proved ledger-type firewall.

**Decision:** keep `C_2`-colored Adams operations in the formal object.

## O18.6 — Formal projective consistency is not an operator limit

Zero-specialization passes exactly for all maps `2->1,...,8->7`, yielding a
formal multigraded projective family. The raw diagonal infinite object lies in
`S_q` iff `q Re(s)>1`, but its determinant is the wrong mixed-subset product.

**Type:** positive formal limit plus proved analytic boundary, with a failed
target interpretation.

**Decision:** no fixed arithmetic Fredholm limit is obtained from the formal
cycle index.

## O18.7 — Inventory universality

All 455 formal, prime, composite-only, shuffled-prime, and random-rational
controls reproduce the scalar identity, fixed-fiber dichotomy, and mixed
factor mismatch.

**Type:** proved adversarial obstruction.

**Decision:** `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.

## O18.8 — Global and lift obligations remain absent

SD-C18 supplies neither a completed functional equation, Gamma factor,
trivial-zero/pole treatment, target counting law, intrinsic Weil compression,
nor a natural unitary, scattering, or self-adjoint lift.

**Type:** open theorem obligations outside the frozen resolved candidate.

**Decision:** `A3_FAIL`, `A4_FAIL`, `ROUTE_B_LOCKED`.
