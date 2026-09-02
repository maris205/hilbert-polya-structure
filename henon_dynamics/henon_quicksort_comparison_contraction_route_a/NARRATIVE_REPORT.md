# Narrative report — HCS-C302

C302 connects every finite comparison-cost distribution of classical
single-pivot Quicksort with its limiting distributional dynamics in one
auditable paper.  Conditioning on the uniform pivot rank yields the exact PGF
convolution.  Its derivatives give the harmonic mean and variance, while exact
centering by `(n+1)` exposes two random branch weights and the entropy-like
toll `C(u)`.

The limiting transform contracts quadratic Wasserstein distance by
`sqrt(2/3)`.  A key improvement over the first proof sketch is that fixed-point
contraction is not treated as automatic convergence of the varying finite
recurrences.  Uniform normalized variances bound all `d_2` distances, and a
subproblem cutoff turns their limsup into `D <= sqrt(2/3)D`, forcing `D=0`.

A second closure precedes the third-moment calculation.  The endogenous
binary-tree toll series has level weights with second and third sums
`(2/3)^r` and `(1/2)^r`.  Conditional Rosenthal bounds make its levels
summable in `L3`, so cubing the fixed-point equation is legitimate.  Exact
beta derivatives then give variance `7-2*pi^2/3` and third moment
`16*zeta(3)-19`; the first six zeta terms already give the positive lower
bound `67/1500`.  The centered limit is therefore nondegenerate and
non-Gaussian.

The result is substantial probability theory but Route-A negative.  Input
size is not an intrinsic arithmetic clock, a recursion tree is not a primitive
periodic-orbit ledger, finite PGFs are not target determinants, and a law-valued
contraction is not a self-adjoint zero operator.  All five rungs fail and Route
B remains locked.
