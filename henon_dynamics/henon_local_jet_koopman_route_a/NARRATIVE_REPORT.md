# Narrative report — C114

## Motivation

Earlier Route-A packages often began with orbit witnesses and only then built
a finite transfer object.  C114 reverses that emphasis.  It freezes a local
polynomial germ and asks exactly what can be certified about its induced
pullback before any global function space or global symbolic coding is
available.

## Result

The fixed origin makes composition well defined on
\(A_4=\mathbb Q[u,v]/(u,v)^5\), a 15-dimensional algebra.  Exact substitution
builds the full rational matrix.  The maximal-ideal filtration has homogeneous
dimensions 1, 2, 3, 4, and 5.  Its diagonal blocks are controlled by the
linearization eigenvalues \(1\) and \(1/2\), giving the full finite spectrum

\[
1^{(5)},\ (1/2)^{(4)},\ (1/4)^{(3)},\ (1/8)^{(2)},\ (1/16)^{(1)}.
\]

Thus the trace is \(129/16\), the determinant is \(2^{-20}\), and both the
characteristic polynomial and \(\det(I-zK)\) factor exactly.  The nonlinear
term is not erased: it changes eleven off-graded matrix entries.  The
correction is strictly degree raising and nilpotent of index four, explaining
why the finite characteristic polynomial still agrees with that of the
linearized control.

## Validation

The producer, a checker with an independently written polynomial engine, and
a fresh SymPy reconstruction agree on every matrix cell and spectral datum.
Canonical replay fixes the JSON bytes.  Thirteen mutations target the model,
basis, matrix, hash, traces, determinant, block data, nonlinear correction,
route verdict, and nonclaim ledger; all thirteen are rejected.

## Interpretation and limit

This is an exact operator-first prefix, but only on a finite local quotient.
It does not supply a global invariant Banach or Hilbert space, an analytic
tail estimate, nuclearity, or a Fredholm determinant.  It also does not
classify global orbits.  The package therefore records A1 partial local
evidence, A2 certified-prefix evidence, A3 not addressed, and A4 fail under
the literal `NO_BAD_EULER_OR_ROOT_NUMBER`.
