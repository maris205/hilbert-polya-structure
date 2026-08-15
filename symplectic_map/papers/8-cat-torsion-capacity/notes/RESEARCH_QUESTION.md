# Research Question

## Frozen symplectic object

Let

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z)
=\mathrm{Sp}_2(\mathbb Z)
\]

and let \(T_A:\mathbb T^2\to\mathbb T^2\) be multiplication by \(A\)
modulo \(\mathbb Z^2\).  The matrix, torus, and normalization are frozen
before any registered calculation.  They are not selected from a family by
prime, zero, period, or spectral matching.

For a torsion point \(x\in\mathbb T^2\), define its additive order by

\[
\operatorname{ord}(x)=\min\{m\geq1:mx=0\}
\]

and define the candidate arithmetic observable

\[
L(x)=\log\operatorname{ord}(x).
\]

For this hyperbolic toral automorphism, the periodic-point set is exactly the
torsion subgroup.  Thus \(L\) is defined on every periodic point, not on a
selected carrier subset.

A **prime-order exact-period carrier** for \((p,n)\) is a point \(x\) such
that \(p\) is a positive rational prime,
\(\operatorname{ord}(x)=p\), and the least positive \(d\) with
\(T_A^d x=x\) is \(d=n\).

## Primary carrier question

Can prime divisors of

\[
\Delta_n(A)=\det(A^n-I)
\]

produce prime-order torsion points of exact, rather than merely dividing,
period \(n\)?

The frozen theorem target is the following general hyperbolic statement.

> If \(M\in\mathrm{SL}_2(\mathbb Z)\) and
> \(|\operatorname{tr}M|>2\), then
> for every \(n>12\) there is a prime-order exact-period carrier for
> \(T_M\).

For positive trace this follows directly from a positive norm-one quadratic
unit.  For negative trace, write \(B=-M\) and use an explicit parity split:
primitive divisors at index \(2n\) for odd \(n\), at index \(n\) when
\(4\mid n\), and at index \(n/2\) when
\(n\equiv2\pmod4\).  The last case uses Flatters' complete small-index
classification at \(7,9,11\); the negative-trace conclusion is not silently
attributed to Theorem 1.4 alone.

## Frozen-map classification question

For the standard cat map above, determine exactly which positive integers
occur as the dynamical period of at least one prime-order torsion point.

The frozen target classification is

\[
\boxed{\text{a prime-order carrier of exact period }n\text{ exists}
\iff n\notin\{1,6,12\}.}
\]

Primitive divisors supply every case beyond twelve and all required small
cases except ten.  The period-ten carrier must instead be proved directly
from the nonsemisimple reduction

\[
A\equiv-I+N\pmod5,\qquad N^2=0.
\]

The exclusions at periods six and twelve must inspect every prime dividing
the corresponding fixed determinant; absence of a primitive divisor alone
is not an exclusion proof.

## Specificity question

Does the natural torsion-order label solve more than carrier availability?
Specifically:

1. Does \(L\) distinguish primes from composites without an external target
   list?
2. Is \(L\) the restriction of a continuous, locally bounded, or Holder
   observable on \(\mathbb T^2\)?
3. Does the unnormalized orbit sum produce \(\log p\) with the desired repeat
   law?
4. Does the native derivative monodromy distinguish prime-order carriers of
   the same dynamical period?

The frozen expected answers are negative:

- every positive integer order occurs already at \((1/m,0)\);
- \(L\) is invariant but unbounded and discontinuous in every neighborhood
  of every torsion point;
- on a period-\(n\), order-\(p\) orbit,
  \(\sum_{j=0}^{n-1}L(T_A^jx)=n\log p\), so recovering \(\log p\) uses an
  orbit-length average or the global order label itself;
- \(D(T_A^n)=A^n\) is independent of the periodic point and of \(p\).

## Arithmetic provenance and semantic separations

- A primitive prime divisor of \(\Delta_n\) is a rational prime dividing
  \(\Delta_n\) and no nonzero \(\Delta_d\) with \(d<n\).
- A primitive **divisor** is not itself a primitive **orbit**.  The bridge is
  a separate kernel-and-least-period argument over \(\mathbb F_p^2\).
- The carrier prime \(p\), the dynamical period \(n\), the point order \(p\),
  and the number of resulting cycles are separate data.
- A prime factor already seen at an earlier determinant can still support a
  new exact point period; period ten modulo five is the mandatory control.
- The range of \(e^L\) is all of \(\mathbb N\), not the primes.  Prime
  availability may not be promoted to prime specificity.
- Determinant factorization, monodromy eigenvalues, orbit lengths, and
  Riemann explicit-formula amplitudes are not interchangeable.

## Frozen decision scope

If the exact carrier theorem and specificity obstruction pass independent
review, the intended conclusion is

`INTRINSIC_TORSION_CAPACITY_CERTIFIED / A0_FAIL_PROVES_TOO_MUCH`.

This label certifies that rational primes arise internally as orders of some
exact-period torsion points, while the proposed clock fails the Route-A
arithmetic-specificity entry gate because the identical mechanism contains
all composite orders and has no regular local realization.

## Mandatory nonclaims

- No direct attribution of the negative-trace parity extension to Flatters;
  Flatters supplies positive-unit primitive divisors and Paper 8 supplies the
  conversion from \(-M\) to \(M\).
- No extension to determinant \(-1\), nonhyperbolic, or higher-dimensional
  toral maps.
- No bijection, injection chosen canonically in \(n\), or multiplicity match
  between rational primes and primitive cat-map cycles.
- No statement that the determinant values \(|\Delta_n|\) are prime.
- No continuous, smooth, Holder, or finite-jet realization of the order
  clock.
- No Ruelle transfer operator, Fredholm determinant, dynamical zeta match,
  explicit-formula amplitude, Weil compression, quantization, or
  Hilbert--Polya claim.
- No Route-A A1--A4 pass and no Route-B opening after the anticipated A0
  specificity failure.
- No prime table, Riemann-zero list, numerical fitting, or post-hoc change of
  matrix, clock, period range, or determinant convention.
