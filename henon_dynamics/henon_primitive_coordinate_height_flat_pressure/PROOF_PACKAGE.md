# Proof package

## 1. Integral and real-conjugate input

P46 proves that after `x=6q`, every coordinate of every geometric periodic
point is an algebraic integer.  P62 proves that every complex periodic point
is real and simple and that every odd primitive mixed-axis quotient is a
reduced effective totally real divisor.

Thus

\[
\widetilde\Psi_n(T)=6^{D_n}\Psi_n(T/6)\in\mathbb Z[T]
\]

is monic, squarefree, and totally real.  Every conjugate of any root is
another real periodic coordinate.

## 2. Uniform coordinate bound

On a period-`n` orbit of the integral recurrence

\[
x_{j+1}=6-x_j^2-x_{j-1},
\]

choose an index with `|x_j|=M`.  Then

\[
M^2=|6-x_{j-1}-x_{j+1}|\le6+2M.
\]

The positive solution of `M^2-2M-6=0` is `1+sqrt(7)`, hence

\[
M\le1+\sqrt7.
\]

The bound is sharp: the negative fixed coordinate is `-1-sqrt(7)`.

## 3. Height bound

For an algebraic integer `alpha`, all nonarchimedean terms in the absolute
logarithmic Weil height vanish.  Every archimedean conjugate of a primitive
scaled root satisfies the coordinate bound, so

\[
0\le h(\alpha)\le C:=\log(1+\sqrt7).
\]

## 4. Flat pressure

Let

\[
Z_n(s)=\sum_{\widetilde\Psi_n(\alpha)=0}e^{-s h(\alpha)}.
\]

For fixed real `s`,

\[
e^{-|s|C}D_n\le Z_n(s)\le e^{|s|C}D_n.
\]

P62 gives

\[
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2},\qquad
\frac1n\log D_n\longrightarrow\frac12\log2.
\]

Dividing the logarithm of the sandwich by `n` proves

\[
\lim_{n\to\infty,\ n\text{ odd}}\frac1n\log Z_n(s)
=\frac12\log2
\]

for every fixed `s in R`.

For fixed nonzero algebraic `c`, the standard height inequality
`h(c*alpha)<=h(alpha)+h(c)` gives another uniform bound.  Therefore every
fixed algebraic coordinate rescaling has the same flat pressure.

## 5. Exact sentinels

The first scaled primitive polynomials are

\[
T^2+2T-6,\qquad T^2-2T-4.
\]

Their root heights are respectively `(1/2)log(6)` and `log(2)`.  The primary
implementation reconstructs through period 11; the independent checker
reconstructs through period 9 and checks exact rational isolators against the
closed bound.  Period one is handled as an exact boundary equality.

## 6. Boundary

The obstruction is specific to the ordinary individual coordinate height.
Multiplying height by period, taking a whole-packet Mahler height, or using a
discriminant/ramification observable changes the object and remains open.
