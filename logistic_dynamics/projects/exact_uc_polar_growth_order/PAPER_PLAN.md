# Paper plan — exact-\(U_c\) polar Fredholm growth order

## One-sentence contribution

For the unchanged exact-\(U_c\) polar Fredholm determinant, we derive a
two-stream coefficient majorant that proves classical order at most two,
an `O(T^2)` fixed-strip zero-count upper bound, and an explicit zero-free
right half-plane.

## Claim--evidence matrix

| Claim | Evidence | Boundary |
|---|---|---|
| The same-object determinant has order at most two. | Two geometric rank-one streams, Hadamard's minor bound, the elementary symmetric-function identity for a geometric sequence, and a Gaussian-in-rank determinant majorant. | No equality or lower growth bound is asserted. |
| Zeros in disks are `O(R^2)`, hence zeros in a fixed real strip through height `T` are `O(T^2)`. | The global quadratic envelope, the nonzero anchor at `s=2`, and Jensen's formula. | This is only an upper bound, not a sharp asymptotic. |
| The determinant is zero-free for `Re(s) > log(2)/log(4/U_c^2)`. | The exact signed trace ledger, the roof lower bound, and absolute convergence of the trace logarithm on a lambda disk extending past `lambda=1`. | No determinant roots are computed. |

## Fixed outline

1. Abstract
2. Frozen determinant and main result
3. Two geometric rank-one streams
4. Quadratic determinant growth
5. Explicit zero-free right half-plane
6. Jensen divisor upper bound
7. Limitations and conclusion
8. Proof appendix

## Reproducibility boundary

The analytic proof uses the inherited exact parameter equation, frozen
stadiums, common logarithmic weight, matching-space determinant, signed
periodic-orbit trace identity, and standard complex-analysis inequalities.
The associated diagnostic certificate evaluates only target-free constants
and finite combinatorial gates; it does not evaluate the determinant or
search for its zeros.
