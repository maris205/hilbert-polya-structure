# HCS-C56 exact prefreeze results

Status: `PREFREEZE_CODE_RESULTS_PASS`.  This is a code/results milestone, not
a paper, Route, or project release promotion.

The exact replay establishes the following machine gates for the fixed HCS-C55
cubic surface:

- the `U01` line chart has a 21-element degree-order Gröbner basis, quotient
  dimension 27, complete standard-monomial Hilbert counts
  `[1, 4, 10, 12, 0]`, and a degree-27 lex eliminant;
- all five complementary Grassmann charts cut out the unit ideal, so all 27
  geometric lines lie in `U01`;
- the cubic is smooth over `Q` and has good reduction at 7, 19, 29, and 37;
- the eliminant factor degrees are `(3,3,3,3,3,6,6)`, `(1,4,4,6,12)`,
  `(1,2,8,8,8)`, and `(2,5,5,5,10)`, with subset-sum intersection `{0,27}`;
- exact enumeration gives `|W(E6)|=51840`, determinant/Coxeter kernel order
  25920, 5184 elements of the target cycle type outside that kernel, zero odd
  ordinary `S27` line permutations, and Picard-lattice fixed rank 1.

The machine enumeration directly proves the fixed rank.  The derived rational
Picard rank 1 additionally uses the written Hochschild--Serre torsion/rank
bridge; the independent check report exposes both facts separately rather
than labeling the lattice computation alone as the rational-rank proof.

The degree-27 field `E` is not claimed to be Galois.  A line over a finite
extension `L` yields an embedding of a conjugate of `E` into `L`, hence
`27 | [L:Q]`.  The Galois closure, rather than `E`, has group `W(E6)`.

The four independent prime-37 gates separately bind good surface reduction,
nonzero leading coefficient plus squarefreeness/unramifiedness, complete
factor multiplication and cycle type, and exclusion from the index-two
Coxeter kernel.  The kernel is not defined using ordinary `S27` sign.
