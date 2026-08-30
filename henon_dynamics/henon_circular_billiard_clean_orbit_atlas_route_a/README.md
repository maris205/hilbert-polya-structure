# HCS-C247 — circular billiard clean-orbit atlas (Route A)

For a disk of radius \(R\), the frozen working Birkhoff coordinates are
\((\theta,\alpha)\), where \(\theta\) is boundary angle and \(\alpha\) is a
signed half-chord angle defined by the oriented central increment
\(\theta'-\theta=2\alpha\pmod {2\pi}\); \(|\alpha|\) is the acute
angle-to-tangent magnitude and its sign records direction.  The exact map is
\[
 B(\theta,\alpha)=(\theta+2\alpha,\alpha)\pmod {2\pi}.
\]
The auxiliary incidence amplitude \(p=\sin\alpha\) is not called a canonical
momentum.  In these coordinates \(DB^n=[[1,2n],[0,1]]\).

For every \(\gcd(m,n)=1\), \(1\le m<n/2\), the values
\(\alpha=\pm\pi m/n\) give all primitive rational families.  Each orientation
has a clean \(S^1_\theta\) fixed manifold, chord length
\(2R\sin(\pi m/n)\), total length
\(L_{m,n}=2nR\sin(\pi m/n)\), concentric caustic radius
\(R\cos(\pi m/n)\), and unit-speed geometric action \(S=L\).  Repetitions
\((km,kn)\) are recorded but never merged with primitive rows.

The diameter \((m,n)=(1,2)\) is one endpoint-equivalent boundary family
\(\alpha=\pm\pi/2\); grazing \(\alpha=0\) is the zero-chord boundary with two
one-sided orientation limits.  Neither boundary is silently treated as an
interior regular family.  Since
\(\ker(DB^n-I)=\operatorname{span}(1,0)\) is exactly the clean family tangent
and \(\det(I-DB^n)=0\), an isolated-orbit determinant denominator is
obstructed.

The package includes 44 primitive rows (\(n\le12\)), six repetition rows, two
boundary rows, independent algebra/SymPy checks, byte replay, and 31
repaired-hash hostile mutations.  The natural-quantization note is limited to
the disk Dirichlet or Neumann Laplacian; no spectrum is matched to a target.

Locks: source baseline
5f357e2d2b78604f6c286bfbd05da922e1d6791f; evaluator SHA
6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c; epoch
1788048000; date 2026-08-30; scope NO_BAD_EULER_OR_ROOT_NUMBER.  Route tuple:
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION), overall
ROUTE_A_REJECTED.
