# Narrative report

The delta comb looks elementary only after its operator convention has been
fixed.  Treating `sum delta(x-na)` as an ordinary multiplication function can
hide the domain, while discussing only the familiar cosine dispersion can
miss the attractive negative band and the singular event at zero energy.

HCS-C327 starts from the `H1(R)` quadratic form.  A periodized trace inequality
controls the sampled values for either sign of `g`; the represented
self-adjoint operator is free between lattice sites, continuous at them, and
has derivative jump `g psi(na)`.  One-cell propagation then has determinant
one and half trace

\[
\Delta(E)=\cos(ka)+\frac{g}{2k}\sin(ka).
\]

The zero value `1+ga/2` is not cosmetic.  For attraction, writing `h=-ga`
reduces the negative edges to two monotone equations:

\[
h=2y\tanh(y/2),\qquad h=2y\coth(y/2).
\]

The first has one root for every `h>0`; the second begins at four.  Therefore
weak attraction carries the first band through zero, `ga=-4` makes zero an
antiperiodic edge, and stronger attraction opens a gap from a negative upper
edge across zero.

At positive energy, every nonfixed partner of the Bragg point `n pi` obeys

\[
ga=2x_n\tan((x_n-n\pi)/2).
\]

Its cellwise monotonicity provides the whole band ordering and proves that no
gap collapses unless `g=0`.  Analytic inversion at high energy gives a full
displacement expansion and hence gap width `2|g|/a+O(n^-2)`, with the next
coefficient and controlled remainder retained in the theorem.

Finally, unwrapping the alternating Bloch phase assigns exactly one state per
cell to each band.  This yields a continuous IDS, constant values in gaps, and
the DOS `|Delta'|/(pi a sqrt(1-Delta^2))`, including its nonzero-coupling edge
singularities and free limit.

This is a complete source-dynamics result.  Natural quantization is genuine,
but no arithmetic bridge appears; Route A is rejected and Route B remains
locked.
