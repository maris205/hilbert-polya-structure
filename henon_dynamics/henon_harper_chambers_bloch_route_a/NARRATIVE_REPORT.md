# Narrative report

The advance is a single complete rational-flux Bloch theorem, not five
small observations.  The principal source of mistakes in this model is
convention drift: one author writes the boundary character itself while
another writes a quasimomentum whose magnetic-cell character is its
`q`-th power.  C371 removes that ambiguity.  Its stored variables are the
total phases `X=q k_x` and `Y=q k_y`, and its characteristic polynomial is
always `det(EI-H)`.

The transfer monodromy first separates horizontal Floquet dependence as
`tr M-2cos X`.  Coprimality makes a vertical phase shift cycle the entire
potential, so the trace is invariant and its Laurent support collapses to
`0,+q,-q`.  Computing the two extreme monomials fixes both signs.  This
gives the full anisotropic Chambers identity, after which the spectral
preimage is immediate because the two cosines independently fill one
closed interval.

The second step is structural rather than numerical.  Axis exchange gives
Aubry duality, complex conjugation reverses flux, and bipartite conjugation
gives polynomial parity.  The edge polynomial then provides a clean
multiplicity criterion: its factors are the characteristic polynomials of
the real endpoint fibers at total phases `(0,0)` and `(pi,pi)`.  Even
magnetic cells force a multiple central edge.  The all-denominator constant
term is mapped to Lamoureux--Mingo with `lambda_LM=2 lambda`, and parity
supplies the zero derivative; the finite exact lane is only a check.

The evidence is deliberately redundant.  The producer uses transfer
polynomials; the checker uses Hermitian characteristic polynomials; and the
exact lane works in a cyclotomic quotient ring.  Across all 78 reduced
fractions through denominator 16 and five anisotropies, 74,880 fibers and
825,600 eigenvalues agree with the frozen identity.

The history boundary is equally explicit.  Lamoureux--Mingo directly own
the cyclic matching cancellation and even-cell constant term; C371 owns
only its convention-locked reconstruction and executable atlas.  C15 already contains critical
Harper blocks along one Heisenberg tower.  C371 does not recycle that
spectral-edge theorem: it owns the all-rational, two-phase, anisotropic
Chambers--duality--edge atlas.  Since the model remains a source magnetic
Hamiltonian without a prime-orbit carrier or target determinant, the strict
Route-A verdict is rejection despite natural quantization.
