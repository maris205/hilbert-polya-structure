# C185 narrative report

## One-sentence result

The simple-spectrum Brockett flow admits a complete all-size convergence and
Morse/inversion theorem, yet its arbitrary real inputs and strict Lyapunov law
force an immediate Route-A arithmetic and primitive-orbit stop.

## Mathematical story

The phase space is a compact orthogonal orbit of symmetric matrices.  The
double commutator is simultaneously a Lax equation and gradient ascent for
`Tr(HN)`.  Those two structures close the global dynamics: compactness gives
complete solutions, the Lax generator preserves the spectrum, and the exact
derivative is the squared commutator norm.

With simple source spectrum and a strict diagonal target, the critical set is
finite and explicit.  Its `n!` points are diagonal permutations.  Each tangent
pair evolves independently to first order; the sign is positive precisely at
an inversion.  Thus the inversion count is both the unstable dimension of the
ascent flow and the Morse index of the sorting energy.  Compact gradient
convergence and stable manifolds then yield sorting for full-volume initial
data.  Strict monotonicity excludes every nonconstant recurrent orbit.

Repeated source or target spectra change the theorem qualitatively.  Source
repetition collapses diagonal labels; a zero in the ambient pair-rate formula
then lies in a stabilizer/non-tangent direction on the smaller orbit.  Target
repetition instead produces genuine tangent zero modes and continuous
commuting critical families, the Morse--Bott component of the separate
degenerate boundary.  The paper does not pretend the simple theorem survives
unchanged.

## Route-A story

The dynamical theorem is strong but non-arithmetic.  Its input spectra may be
any ordered reals, the continuous clock is not logarithmic prime time, and the
flow has no nonconstant periodic trajectories.  Local tangent determinants do
not supply a global dynamical determinant.  The skew Lax matrix depends on the
current state and therefore supplies only a formal A4 orthogonal-lift hint.

The final tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall rejected.

## Evidence boundary

Exact code exhausts 5,912 permutation equilibria and 118,004 pair modes for
`n<=7`, while the written proof covers all `n`.  The sole citation assigns the
classical flow and sorting framework to Brockett.  Internal checks are not
external peer review.
