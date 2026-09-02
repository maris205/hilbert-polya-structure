# C309 narrative report

The decisive simplification is that every part of the nonlinear matrix flow
is owned by a two-block linear system.  This does more than produce a formula:
the loss of the `U` chart is exactly the Riccati blow-up locus, and the
spectral theorem turns it into a complete signed-time pole atlas.  The
forward boundary `lambda_min=-1` is retained rather than treated as a generic
case; its `-1` eigenspace survives and selects the limiting involution.

The equilibrium set is not discrete.  It is a disjoint union of Grassmann
orbits.  Linearization resolves the apparently degenerate zero modes: they
are exactly tangent to those orbits, while the two diagonal blocks give all
stable and unstable dimensions.  The Loewner formula then describes the
full derivative of the nonlinear solution operator, including repeated
eigenvalues.

This large source theorem still fails Route A.  Strict gradient descent
excludes nonconstant recurrence; continuous eigenvalues provide no prime
carrier or logarithmic clock; and neither the block determinant nor the
finite symmetric lift is a target determinant or Hilbert--Pólya operator.
