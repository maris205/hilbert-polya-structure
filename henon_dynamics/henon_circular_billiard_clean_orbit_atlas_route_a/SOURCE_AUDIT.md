# C247 source and scope audit

**Locks.** Source baseline
5f357e2d2b78604f6c286bfbd05da922e1d6791f; evaluator v0.2.0 authority
6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c; fixed
epoch 1788048000; date 2026-08-30; scope literal
NO_BAD_EULER_OR_ROOT_NUMBER.

**Primary sources.**

* G. D. Birkhoff, “On the periodic motions of dynamical systems,” *Acta
  Mathematica* 50 (1927), 359–379, DOI
  [10.1007/BF02421325](https://doi.org/10.1007/BF02421325).  The publisher
  record fixes the bibliographic metadata and the periodic twist-map context.
* R. L. Bishop, “Circular Billiard Tables, Conjugate Loci, and a Cardioid,”
  *Regular and Chaotic Dynamics* 8 (2003), 83–95, DOI
  [10.1070/RD2003v008n01ABEH000227](https://doi.org/10.1070/RD2003v008n01ABEH000227);
  publisher page [MathNet](https://www.mathnet.ru/rcd767).  This is the
  circle-table/caustic source.

The certificate's formulas are re-derived locally.  In particular, \(\alpha\)
is the signed half-chord angle defined by the oriented central increment
\(\theta'-\theta=2\alpha\pmod{2\pi}\); \(|\alpha|\) is the acute
angle-to-tangent magnitude and its sign records direction.  The quantity
\(p=\sin\alpha\) is only an auxiliary incidence amplitude, not a claimed
canonical momentum.  The working chart is \((\theta,\alpha)\), whose
derivative is the constant shear \(DB^n=[[1,2n],[0,1]]\).

**Boundary and clean audit.** The diameter signs are merged into one
endpoint-equivalent row.  Grazing is one zero-chord row with two one-sided
orientation limits.  The checker and SymPy script verify the exact kernel
\(\ker(DB^n-I)=T(S^1_\theta)\), not merely a zero determinant.  Unit-speed
action equals geometric length; a general speed factor is stated explicitly.
The Dirichlet/Neumann disk Laplacians are only a finite natural-quantization
definition, with no spectral target match.

**Forbidden claims.** All nine scope flags are false and Route B is not
invoked.  No prime/zero table, arithmetic local datum, Euler factor, root
number, automorphy claim, target determinant, or Hilbert–Pólya operator appears.
