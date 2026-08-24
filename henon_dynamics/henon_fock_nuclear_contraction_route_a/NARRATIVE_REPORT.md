# Narrative report — C119

C119 makes an operator-first move. Instead of extracting a finite determinant
from an orbit atlas, it freezes a strict two-dimensional contraction and takes
its standard bosonic second quantization. The Euclidean contraction estimate
is essential: spectral radius below one alone would not prove convergence of
the Fock singular-value sum for a non-normal matrix.

Once both singular values lie below one, nuclearity follows from a double
geometric series. The eigenvalues of the two-dimensional matrix then determine
every Fock trace, the Fredholm product, and a complete zero divisor. This is a
genuine analytic operator determinant, but it is intentionally source-owned.

The gain exposes a complementary loss. Since neither eigenvalue is a root of
unity, `A^n-I` is always invertible and the only periodic point is zero. Thus
the paper proves a reusable analytic-operator theorem while recording an
unambiguous A1 failure.  Under the strict Route-A evaluator it also receives
`A2_FAIL`: the determinant is not primitive-orbit-owned and its zeros are not
matched to any target.  This distinction prevents a strong structural result
from being promoted into a target-facing Route-A certificate.
