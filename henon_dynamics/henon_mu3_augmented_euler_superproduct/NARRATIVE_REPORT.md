# Narrative Report

This project asked for a non-scalar way to couple the homogeneous
area-preserving Hénon map to an arithmetic Euler determinant.  Direct cubic
Kummer lifts of the scalar phase fail because the degree-three cover is a
constant-field cover.  The successful structural move is instead to use the
full generating kernel \(qQ+2q^3\), whose two variables transform with
opposite cubic weights.

The resulting finite-field quantum map is a Fourier--cubic unitary.  Its
order-three permutation does not commute with one Hénon step; it is inverted
by that step.  Two steps therefore preserve the three character sectors.  The
canonical integer augmentation weights \((2,-1,-1)\) produce a rational local
superdeterminant and an exact twisted-orbit trace formula.  Deligne's smooth
leading cubic bound proves a nonzero Euler germ on
\(\operatorname{Re}s>1\).

The construction then meets two sharp falsification gates.  Exact reductions
at all nine split primes through 73 show that the trivial and nontrivial sector
polynomials are coprime; virtual rank two does not mean actual rank-two local
spectral complexity.  More decisively, an exact enumeration at \(p=7\) shows
that the first augmentation coefficient is nonreal.  The raw product thus
fails conjugation symmetry and is rejected by Route A despite its valid
analytic germ and natural quantization.

The finite-dimensional Eisenstein repair is already closed by the companion
C41--C42 controls: a \(j=0\) CM elliptic carrier is genuine arithmetic, but a
finite Tate--CM virtual combination matches the Riemann local factor only by
deleting its new \(H^1\).  The remaining large door is not another local
factor repair.  It asks whether the conjugate-paired full-kernel moments, over
split and inert places together, form a pure self-dual compatible system over
one fixed number field, with uniformly bounded rank and conductor.  The first
gate is algebraic descent: a fixed coefficient field uniformly bounds the
degrees of all paired first moments.  Only after that gate survives does a
fixed-rank system force a uniform recurrence, equivalently bounded Hankel
rank, for every chronological moment sequence.  Unbounded coefficient degree
or unbounded Hankel rank closes this Eisenstein route; passing both authorizes
the functional-equation construction.
