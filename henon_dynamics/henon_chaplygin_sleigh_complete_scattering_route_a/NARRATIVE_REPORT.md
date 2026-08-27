# Narrative report

The signed offset is not a cosmetic parameter.  It chooses which half of the
equilibrium line attracts and reverses the orientation of the heteroclinic
connection.  Once that sign is retained, the energy ellipse reduces the
dynamics to a hyperbolic tangent/sech pair.  The same formula supplies a finite,
energy-independent blade rotation even though contact position escapes along
two different affine lines.

Reconstruction is the main geometric trap.  `theta` describes the blade, but
the contact velocity is `u e(theta)`.  At the end where `u<0`, its heading is
`theta+pi`; reporting blade scattering as velocity scattering would therefore
be wrong.  A second trap is invariant measure: `1/|omega|` is a reduced density
on each open half-plane and its configuration-Haar lift is invariant off the
line, but it is necessarily singular at the reduced equilibrium line.  The
pointwise obstruction excludes smooth reduced and Haar-factor densities, not
every conceivable configuration-dependent density for the translating full
flow.

The zero-offset limit changes the phase portrait rather than merely slowing
it.  Both reduced velocities become constant; rotations close after one turn,
creating genuine periodic `SE(2)` trajectories.  This gives a sharp recurrence
boundary and completes the parameter atlas.

Despite this unusually large dynamical step, Route A still stops.  The
half-plane Poisson form merits `A4_FORMAL_HINT`, but there is no intrinsic
prime-power periodic-orbit carrier or target determinant, and no operator with
the required target spectrum is constructed.
