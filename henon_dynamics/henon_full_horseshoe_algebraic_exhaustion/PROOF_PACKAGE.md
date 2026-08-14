# Proof package

## 1. Parameter conjugacy

Let

\[
H_6(q,p)=(1-6q^2-p,q),\qquad S(q,p)=(6q,6p).
\]

Then

\[
S H_6 S^{-1}(x,y)=(6-x^2-y,x)=:H_{6,-1}(x,y).
\]

The exact lower endpoint of Arai's certified hyperbolic plateau at `b=-1`
is

\[
a_0=5.699951171875=\frac{23347}{4096}<6.
\]

## 2. Full-horseshoe transport

Devaney--Nitecki use `(x,y)->(1+y-Ax^2,Bx)`. At `B=-1`, the scaling
`(X,Y)=(Ax,-Ay)` gives `(X,Y)->(A-X^2-Y,X)`, exactly Arai's convention.
Their threshold `(5+2sqrt(5))(1+|B|)^2/4` becomes `A>5+2sqrt(5)`. The
anchor `A=10` satisfies this inequality because `(10-5)^2=25>20`.

Arai proves that the chain recurrent set is uniformly hyperbolic throughout
`[a0,infinity)` and records R-stability on the hyperbolic plateau. The path
`[6,10]` lies in one connected plateau, so its chain recurrent dynamics are
conjugate. The full two-shift at `a=10` therefore transports to `a=6`.
Conjugating back by `S` proves:

> The real chain recurrent set of `H6` is uniformly hyperbolic and conjugate
> to the full two-shift.

In particular, `H6^n` has exactly `2^n` distinct real hyperbolic fixed points
for every `n>=1`.

## 3. Complex algebraic exhaustion

Friedland--Milnor prove that a cyclically reduced plane polynomial
automorphism of degree `d` has algebraic fixed-point count `d`, counted with
complex intersection multiplicity. Applying the theorem to the degree-two
iterate `H6^n` gives total complex multiplicity `2^n`.

The full shift already supplies `2^n` distinct real fixed points. Every one
has multiplicity at least one, so they consume the complete algebraic count.
Hence there are no additional complex points and every listed point has
multiplicity exactly one. Since the real chain recurrent set is uniformly
hyperbolic, all points are hyperbolic. Thus, for every `n>=1`,

\[
\operatorname{Fix}_{\mathbb C}(H_6^n)
=\operatorname{Fix}_{\mathbb R}(H_6^n),
\qquad \#\operatorname{Fix}(H_6^n)=2^n,
\]

and the fixed-point scheme is reduced.

## 4. Mixed-axis total reality and simplicity

Write `H6=RJ`, where

\[
R(q,p)=(p,q),\qquad
\gamma(X)=\left(X,\frac{1-6X^2}{2}\right)\in\operatorname{Fix}(J).
\]

For odd `n=2m+1`, P60 proves that

\[
F_n(X)=q_{m+1}(X)-q_m(X),\qquad \deg F_n=2^{m+1},
\]

and that every complex root gives a complex point fixed by `H6^n`.
Algebraic exhaustion forces that point, and hence `X`, to be real.

P61 proves that a multiple mixed-axis root forces multiplier `+1` for
`DH6^n`. Every real periodic point now lies in the hyperbolic chain recurrent
set, where multiplier `+1` is impossible. Therefore every `F_n` is totally
real and squarefree.

## 5. Primitive effectivity

P60's exact divisibility gives recursively

\[
F_n=\prod_{d\mid n}\Psi_d
\]

over odd divisors. If a root of `F_n` has odd least period `e`, then `e|n`.
For `z` on `Fix(J)`, reversibility gives

\[
H_6^{(e+1)/2}z\in\operatorname{Fix}(R),
\]

so the same coordinate is a root of `F_e`. Since every `F_d` is squarefree,
recursive division removes precisely all proper lower-period roots. Thus
`Psi_n` is a reduced effective divisor of exact least-period roots.

Its degree is

\[
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}.
\]

The algebra `Q[X]/(Psi_n)` is finite étale and totally real. Moreover,

\[
D_n=2^{(n+1)/2}+O\!\left(n2^{n/6+1/2}\right),
\qquad
\lim_{\substack{n\to\infty\\ n\ \mathrm{odd}}}\frac1n\log D_n
=\frac12\log2.
\]

## 6. Relation to P59 physical incidence

P59/P61 count the roots in the previously certified small-content physical
survivor with entropy `(1/2)log(phi)`. P62 shows that the formal population
is also an actual real hyperbolic population, but the physical subset still
has density

\[
\Theta\!\left((\varphi/2)^{n/2}\right).
\]

The former obstruction was ambient effectivity; the surviving obstruction is
the absence of an arithmetic compiler for the much larger real population.

## 7. Finite exact certificate

For odd `n<=13`, the primary checker reconstructs the primitive quotient and
isolates every root by disjoint exact Sturm intervals. The exact primitive
degrees are `2,2,6,14,28,62,126`, and every root is real and simple. Exact
rational orbit propagation through period 11 gives the same number of unique
half-itineraries. Period 13 deliberately omits that denominator-heavy optional
diagnostic and is certified by the all-period theorem plus Sturm isolation.

An independent checker separately enumerates binary full-shift words through
period 13 and recomputes high-precision primitive roots through period 11.
Twenty-six adversarial mutations are rejected.

## 8. Boundary

This package resolves the P60/P61 ambient resultant/effectivity gate at the
single frozen parameter `H6`. It proves no intrinsic rational-prime labels,
no von Mangoldt amplitudes, no completed Riemann determinant, and no
Hilbert--Pólya operator. The next non-micro theorem is uniform height or
Galois-excess pressure for the effective totally real primitive reflection
divisors.
