# C241 theorem package: Lüroth words, points, and weighted source identity

## Frozen map and endpoint convention

For \(x\in(0,1]\), let \(m=\lfloor1/x\rfloor+1\) and define
\[
T_L(x)=m(m-1)x-(m-1),\qquad T_L(0)=0.
\]
Thus
\(I_m=(1/m,1/(m-1)]\) for \(m\ge2\).  The half-open intervals partition
\((0,1]\).  On each \(I_m\), \(T_L\) has derivative
\(a_m=m(m-1)\) and image **\((0,1]\)**: 1 is attained at the right endpoint,
whereas 0 is only the limit at the excluded left endpoint.  The inverse
formula \(\phi_m(y)=(y+m-1)/a_m\) is used for \(y\in(0,1]\); formally
\(\phi_m(0)=1/m\) lies in the excluded boundary.

## Finite words

For a word \(w=(w_1,\ldots,w_r)\) over \(\{2,3,\ldots\}\), compose inverse
branches in itinerary order,
\[
\Phi_w=\phi_{w_1}\circ\cdots\circ\phi_{w_r}(y)=u_wy+v_w,
\quad
u_w=\prod_{j=1}^r a_{w_j}^{-1},\quad 0<u_w<1.
\]
The contraction theorem gives a unique fixed point
\(x_w=v_w/(1-u_w)\).  Direct interval inequalities (or the exact itinerary
calculation in the receipt) put \(x_w\) in the coded cylinder, with boundary
ambiguities isolated by the half-open convention.  Consequently
\[
(T_L^r)'(x_w)=A_w=\prod_{j=1}^r a_{w_j}
\]
and the forward itinerary is \(w\).  Cyclic rotations represent the same
oriented periodic orbit.  A word is primitive when its least repetition period
is \(r\); primitive necklaces are primitive words modulo cyclic rotation.

For a finite alphabet of size \(q=M-1\), Möbius inversion gives
\[
N_r(q)=\frac1r\sum_{d\mid r}\mu(d)q^{r/d}
\]
primitive necklaces of length \(r\).  For the actual countable alphabet,
there are countably infinitely many words and periodic points at every
positive period (the finite rows only certify slices).

## Weighted identity and its domains

Put \(w_m(s)=a_m^{-s}\) and
\(A_M(s)=\sum_{m=2}^{M}w_m(s)\).  The finite word generating series is the
exact rational identity
\[
Z_M(z,s)=\sum_{r\ge0}z^rA_M(s)^r
       =\frac1{1-zA_M(s)}.
\]
Its primitive-necklace factorization agrees with the geometric series in the
ordinary domain \(|z|A_M(\Re s)<1\), and as a formal power series in \(z\).

For the countable alphabet,
\[
A(s)=\sum_{m=2}^{\infty}[m(m-1)]^{-s}
\]
converges absolutely for \(\Re(s)>1/2\), by comparison with
\(\sum(m-1)^{-2\Re(s)}\).  Two domains must not be conflated:

1. The primitive product/log expansion is absolutely convergent only when
   \(\Re(s)>1/2\) **and** \(|z|A(\Re(s))<1\).
2. The closed expression \(1/(1-zA(s))\) is a meromorphic function throughout
   \(\Re(s)>1/2\) away from its denominator zeros.  This is a continuation
   statement, broader than absolute product convergence; at \(\Re(s)=1/2\),
   \(A(s)\) itself diverges and no full-alphabet value is asserted.

At \(s=1\),
\[
A(1)=\sum_{m=2}^{\infty}\frac1{m(m-1)}
 =\sum_{m=2}^{\infty}\left(\frac1{m-1}-\frac1m\right)=1,
\]
so \(z=1\) is the denominator pole/boundary.  For a cutoff \(M\), the exact
tail is \(\sum_{m>M}1/[m(m-1)]=1/M\); the receipt records this rather than
rounding it to zero.

## Evidence and scope

The producer/checker pair locks 11 branch rows, 780 words, 30 necklace rows,
88 weighted rows, 3 limit rows, and 2 formal-product rows.  All fractions,
periods, itineraries, and multipliers are independently reconstructed; SymPy,
byte replay, and hostile repaired-hash mutations provide separate checks.
This theorem is source-local.  It does not assert target primes or zeros,
arithmetic local data, Euler factors, root numbers, automorphy, a target
divisor/functional equation, a Hilbert–Pólya operator, or Route-B input.

## Sources

Barrionuevo, Burton, Dajani & Kraaikamp, *Ergodic properties of generalized
Lüroth series*, Acta Arithmetica 74(4), 311–327 (1996), DOI
10.4064/aa-74-4-311-327; Galambos, *Some remarks on the Lüroth expansion*,
Czechoslovak Mathematical Journal 22(2), 266–271 (1972), DOI
10.21136/CMJ.1972.101097.
