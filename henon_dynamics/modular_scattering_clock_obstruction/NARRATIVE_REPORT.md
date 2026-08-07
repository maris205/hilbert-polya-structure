# Research narrative

## Why the system changed

The previous compact \(S\)-arithmetic project produced a genuine two-place
height clock, but its periodic objects were flat families and its direct
compact spectral baseline had \(T^2\) counting.  Varying the compact arithmetic
parameters would not change either mechanism.  HCS-C17 therefore switches to
a noncompact one-cusp system where a natural scattering matrix already
contains the Riemann zeta function.

## The tempting bridge

For the modular group, the lower-left entry \(c\) parametrizes oriented cusp
double cosets together with a reduced residue \(d\bmod c\).  There are
\(\varphi(c)\) channels at level \(c\), their open sojourn time is proportional
to \(2\log c\), and their weighted series is the arithmetic part of the
modular scattering coefficient.  This is exactly the kind of signal a
breadth-first Hilbert--Pólya search should inspect rather than dismiss.

The shortest proposed bridge was to reuse the denominator as the total length
of a closed hyperbolic class.  That would turn the scattering arithmetic into
a primitive-orbit Euler product without inventing a fitted scale.

## The category test

The bridge crosses between two different quotients:

| Open scattering object | Closed hyperbolic object |
|---|---|
| cusp double coset \(P\backslash\Gamma/P\) | conjugacy class in \(\Gamma\) |
| level \((c,d\bmod c)\) | cyclic Gauss word / hyperbolic class |
| sojourn clock \(2\log(cT_0)\) | translation length \(2\operatorname{arcosh}(|t|/2)\) |
| no intrinsic power/repeat operation used here | \([g^n]\) is the \(n\)-fold orbit repeat |

The lower-left entry survives parabolic left/right moves, as it should for an
open double coset, but not hyperbolic conjugacy or cyclic recoding.  An even
Gauss-word witness stays entirely in \(\mathrm{PSL}_2(\mathbb Z)\): the cyclic
words \((1,1,1,2)\) and \((1,2,1,1)\) have conjugate products and equal trace,
but final denominators 3 and 4.

## The large theorem step

A single counterexample to \(2\log|c|\) would be too narrow.  The positive
family

\[
\gamma_{m,n}=\begin{pmatrix}1&m\\n&1+mn\end{pmatrix}
\]

upgrades the failure to every denominator-only function.  If a fixed scaling
\(\alpha\) and a function \(F\) satisfy

\[
F(\alpha|c(\gamma^2)|)=2F(\alpha|c(\gamma)|)
\]

for every hyperbolic \(\gamma\) whose four entries are strictly positive,
then \(F\) is zero on
\(\alpha\mathbb N\).  The proof uses only squares and no analytic assumptions
on \(F\).  This closes the entire frozen final-denominator class in one step.

## The positive closure

The obstruction is not the end of the calculation.  Cayley--Hamilton shows
that the denominator height has a stable linear part.  After division by the
repeat number it converges exactly to hyperbolic translation length.  Thus
the arithmetic denominator is meaningful as an open scattering clock, but
its canonical power-stable closed shadow is the known Selberg clock.

This gives a structural explanation for the failure: closing the channel
erases precisely the endpoint/cusp information that distinguished its
denominator, leaving the conjugacy-invariant eigenvalue growth.

## Divisor and operator assessment

Each nontrivial zeta zero \(\rho\) produces a pole of \(\Phi\) at \(\rho/2\)
and a zero at \((1+\rho)/2\).  A nonconstant affine reparametrization and an
entire zero-free normalization preserve these poles, so they cannot yield one
entire \(\xi\)-function.  A compensator with its own zeta divisor could cancel
them, but would insert the target arithmetic by hand and lies outside the
source lock.

The physical-line scattering matrix is a natural unitary object.  That is a
real positive Route-A signal, but it does not turn scattering resonances into
a discrete self-adjoint spectrum.  Route B is therefore not invoked.

## Computation and result

Exact integer arithmetic checks all frozen algebraic identities.  The word
audit finds cyclic denominator variation in 259 of 274 canonical primitive
even Gauss words and literal square-additivity in none.  The independent
checker reimplements the key calculations without importing the producer.
High-precision calculations are regressions for the Dirichlet/scattering
identities and stable formula, not sources of the proof.

The candidate is closed early rather than subjected to small parameter
sweeps.  Its value is the obstruction: modular scattering contains genuine
Riemann arithmetic, but a direct final-denominator closed-orbit conversion is
mathematically incompatible with primitive repetition.
