# Narrative report

C230 changes subtype to a finite open Hamiltonian lattice with a genuine Lax
pair.  The source Hamiltonian has exponential nearest-neighbour interactions,
while the Flaschka map turns its equations into an isospectral flow of a real
Jacobi matrix.  This closes a theorem-scale step unavailable in the preceding
scattering, queue, free-boundary, dissipative, and coagulation packages.

The main result has four linked parts.  First, conserved traces bound every
Flaschka coordinate and prove global existence; the scalar edge equation keeps
all \(a_j\) positive at finite time, so no finite collision is hidden.  Second,
irreducibility gives a simple real spectrum and the Moser sorting theorem
identifies the two asymptotic velocity orders with the eigenvalues.  Third,
the Weyl residues \(\rho_k\) obey an exact softmax/exponential law, supplying
inverse-scattering coordinates and a careful action-angle statement.  The
physical positive isospectral leaf is an open noncompact scattering chamber;
only a complex phase compactification has torus angles.  Fourth, \(N=2\) is
solved in closed sech/tanh form and the repeated-root block boundary is
explicitly separated.
In the complex inverse-spectral chart, nonzero residues modulo their common
\(\mathbb C^\times\) gauge have phase fiber
\((S^1)^N/S^1\cong\mathbb T^{N-1}\) over each simple spectrum; this local
torus is not identified with the physical real leaf.

The inverse map can be written with Hankel/Cauchy--Binet minors
\(\tau_j=\sum_{|S|=j}(\prod_{k\in S}\rho_k(0)e^{2\lambda_k t})
\Delta(\lambda_S)^2\), giving
\(a_j=\sqrt{\tau_{j-1}\tau_{j+1}}/\tau_j\) and
\(b_j=\frac12\partial_t\log(\tau_j/\tau_{j-1})\).  This makes the sorting
limit a direct dominance statement rather than a finite-time fit.

The executable ledger covers six rational source rows, 30 finite Lax states,
15 exact N=2 comparisons, six finite endpoint sorting diagnostics, and nine
norming-coordinate comparisons.  Numerical drifts are reported as controlled
RK4 errors rather than promoted to exact statements.  The strict Route-A
assessment remains rejected: an integrable Lax spectrum is not an arithmetic
owner, primitive periodic-orbit repetition law, target determinant, or
Hilbert--Polya bridge.
