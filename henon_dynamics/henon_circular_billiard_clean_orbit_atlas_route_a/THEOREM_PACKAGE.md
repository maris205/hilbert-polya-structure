# C247 theorem package — circular billiard

## Coordinates and map

Let \(D_R=\{x^2+y^2<R^2\}\).  Use boundary angle \(\theta\) and signed
half-chord angle \(\alpha\in(-\pi/2,\pi/2)\), defined by the oriented
central increment \(\theta'-\theta=2\alpha\pmod {2\pi}\).  Its absolute value
is the acute angle-to-tangent magnitude and its sign records direction.  The
auxiliary \(p=\sin\alpha\) is not a canonical momentum; the physical canonical boundary momentum depends
on the chosen generating-function branch.  The exact circle map is
\[
B(\theta,\alpha)=(\theta+2\alpha,\alpha)\pmod{2\pi},\qquad
DB=\begin{pmatrix}1&2\\0&1\end{pmatrix}.
\]
Thus \(DB^n=[[1,2n],[0,1]]\).

## Primitive families and geometry

For every \(\gcd(m,n)=1\) and \(1\le m<n/2\), set
\(\alpha_\varepsilon=\varepsilon\pi m/n\), \(\varepsilon=\pm1\).  These and
only these interior rational rotations close after \(n\) bounces.  The two
signs are orientation-separated:
\[
\ell=2R\sin(\pi m/n),\qquad
L_{m,n}=2nR\sin(\pi m/n),\qquad
r_c=R\cos(\pi m/n).
\]
At unit speed the geometric action is \(S_{m,n}=L_{m,n}\); at speed \(p_0\)
it is \(p_0L_{m,n}\).  The \(k\)-fold repetition has \(kn\) bounces,
length/action multiplied by \(k\), and unreduced label \((km,kn)\).

## Clean return and boundaries

\(\operatorname{Fix}(B^n)\) contains the one-dimensional family
\(\{(\theta,\alpha_\varepsilon):\theta\in S^1\}\).  Since
\[
DB^n-I=\begin{pmatrix}0&2n\\0&0\end{pmatrix},
\quad \ker(DB^n-I)=\operatorname{span}\{(1,0)\}=T(S^1_\theta),
\quad \det(I-DB^n)=0,
\]
the return is unipotent and no isolated-orbit determinant denominator is
defined.  The diameter \((m,n)=(1,2)\), \(\alpha=\pm\pi/2\), is one
endpoint-equivalent family; its angle-chart return matrix is recorded but it
is not an interior row.  At \(\alpha=0\), \(p=0\), the chord has zero length;
the two one-sided signs are limiting orientations, not a genuine flight.

## Natural quantization and route boundary

For this geometric disk the natural quantizations considered here are the
standard self-adjoint Dirichlet and Neumann realizations of the Laplacian,
\(-\Delta_{D_R}\) with \(f|_{\partial D_R}=0\) or
\(\partial_\nu f|_{\partial D_R}=0\).  This definition motivates
A4_NATURAL_QUANTIZATION only; no eigenvalue table or target match is used.
The locked tuple is
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION), overall
ROUTE_A_REJECTED.  No arithmetic local data, Euler factors, root numbers,
automorphy, target divisor/function equation, target determinant, zero match,
or Hilbert--Pólya operator is claimed.
