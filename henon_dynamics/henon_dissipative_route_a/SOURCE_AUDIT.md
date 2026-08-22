# Source audit and boundary

- The source is the explicitly frozen polynomial map
  \(F(x,y)=(x^2-91/16-y,x/2)\); its Jacobian determinant is exactly (1/2),
  so the map is area-contracting.
- All cycle equations, points, Jacobians, and rational weights are derived
  from this map by exact algebra.  The resultant is independently recomputed
  by the checker and the SymPy cross-check.
- The four-state graph contains only the four certified witnesses.  It is not
  asserted to be a Markov partition, a complete real repeller, or a complete
  primitive-orbit atlas.
- The local weight \(\omega(p)=\det(I-DF(p))^{-1}\) is a finite diagnostic
  potential.  The matrix determinant built from it is explicitly labelled a
  discrete witness, not an analytic Fredholm determinant.
- No prime/zero tables, Euler factors, root numbers, automorphy data, or
  Hilbert–Pólya operator are used or claimed.  Novelty is `UNVERIFIED`.
