# Proof Package

## Claim

Put

```text
D(t)=((1-t^2)/(1+t^2), 2t/(1+t^2)),  0<t<1,
```

and define the open-branch Romik map

```text
T(t)=t/(1-2t) on (0,1/3),
T(t)=1/t-2     on (1/3,1/2),
T(t)=2-1/t     on (1/2,1).
```

The terminal point `1/2` represents the primary `(a odd,b even)` root
`(3,4,5)`; `1/3` represents the leg-swapped mirror root `(4,3,5)`.  The
periodic phase space is `X=(0,1)\Q`.  The inverse branches are

```text
F_1(t)=t/(1+2t),  F_2(t)=1/(2+t),  F_3(t)=1/(2-t),
```

with disjoint open images `(0,1/3)`, `(1/3,1/2)`, `(1/2,1)`.

For the primary orientation, let `M_1,M_2,M_3` be the Barning matrices

```text
[-1  2  2]   [1 2 2]   [ 1 -2 2]
[-2  1  2],  [2 1 2],  [ 2 -1 2].
[-2  2  3]   [2 2 3]   [ 2 -2 3]
```

Then:

1. Every primitive Pythagorean triple with first leg odd and second leg even
   is `M_(w_1)...M_(w_n)(3,4,5)^t` for one and only one possibly empty finite
   word `w`; the empty word gives the root `(3,4,5)`.
   Its rational coordinate terminates at `1/2`.  Leg swap is a separate
   mirror orientation terminating at `1/3`.
2. For every word `w` of length `n`, let `F_w=F_(w_1)...F_(w_n)`.  The pure
   words `1^n` and `3^n` have only the boundary fixed points `0` and `1`.
   Every other word has exactly one fixed point in its open cylinder.  It is
   quadratic irrational, and distinct words of length `n` give distinct
   points of `Fix(T^n|X)`.
3. Consequently

```text
#Fix(T^n|X)=3^n-2,
E_n=sum_(d|n) mu(d)(3^(n/d)-2),
pi_n=E_n/n,
zeta_T(z)=exp(sum_(n>=1)(3^n-2)z^n/n)=(1-z)^2/(1-3z).
```

4. If `F_w(t)=(at+b)/(ct+d)`, then its fixed point satisfies
   `ct^2+(d-a)t-b=0`, `det(F_w)=(-1)^(number of 2 digits)`, and

```text
|(T^n)'(t_w)|=rho(F_w)^2,
rho(F_w)=(tr(F_w)+sqrt(tr(F_w)^2-4det(F_w)))/2.
```

   Repeated words raise the monodromy and multiply the logarithmic instability
   exactly.  A negative determinant records source orientation reversal; it
   is not silently promoted to an element of `PSL_2`.

## Status

PROVABLE AS STATED.

## Proof strategy

The Euclid coordinate proves rational descent and the Barning tree.  The
inverse branches provide disjoint symbolic cylinders.  A contraction lemma
classifies the two parabolic words and every other hyperbolic word.  Coding
injectivity then gives the fixed count; Möbius inversion and the trace series
give primitive cycles and zeta.  A derivative/eigenvector identity gives the
multiplier.

## Proof

### 1. The parity-oriented rational tree

Let `t=n/m` be reduced with `m>n>0` and opposite parity.  Then

```text
a=m^2-n^2,  b=2mn,  c=m^2+n^2
```

is primitive, has `a` odd and `b` even, and `D(t)=(a/c,b/c)`.  Conversely, if
`a^2+b^2=c^2` is primitive with `a` odd and `b` even, the coprime integers
`(c+a)/2` and `(c-a)/2` have square product `(b/2)^2`.  Each is therefore a
square, say `m^2,n^2`.  This recovers the displayed parametrization with
coprime `m,n` of opposite parity, uniquely.

For `t=n/m`, the three inverse branches replace `(m,n)` by

```text
(m+2n,n),  (2m+n,m),  (2m-n,m),
```

respectively.  Direct substitution in the three quadratic expressions for
`a,b,c` gives exactly multiplication by `M_1,M_2,M_3`.  These pairs remain
coprime and of opposite parity, and their new first coordinate is larger than
`m`; hence the hypotenuse increases.

In the forward direction, the three intervals replace `n/m` by

```text
n/(m-2n),  (m-2n)/n,  (2n-m)/n.
```

The new denominator is strictly smaller than `m`.  Coprimality and opposite
parity persist.  Such a fraction cannot equal `1/3`, whose reduced numerator
and denominator are both odd.  Strict descent must therefore end at `1/2`.
At every nonterminal step the three intervals are disjoint, so the removed
digit and parent are unique.  Induction proves existence and uniqueness of
the primary Barning word.  Swapping the legs changes the parity orientation
and moves the terminal owner to `1/3`; it is not merged into the primary tree.

### 2. Periodic words

Every `F_i` maps `(0,1)` bijectively onto the stated open interval, so words of
one length have disjoint open cylinders.  Their derivatives satisfy

```text
|F_1'(t)|=(1+2t)^(-2),
|F_2'(t)|=(2+t)^(-2),
|F_3'(t)|=(2-t)^(-2).
```

The first derivative can reach one only at `0`, the third only at `1`, and the
second is at most `1/4`.  Thus a word using only digit `1` or only digit `3`
is parabolic.  Indeed

```text
F_(1^n)(t)=t/(1+2nt),
```

has only fixed point `0`, while the conjugate formula for `F_(3^n)` has only
fixed point `1`.  Both lie outside `X`.

Every other composition maps `[0,1]` into a compact subinterval of `(0,1)`.
In the derivative product, equality with one would require every factor to be
an equality case at compatible endpoints; the occurrence of digit `2` or a
transition between `1` and `3` prevents that.  Compactness gives
`sup|F_w'|<1`.  The contraction theorem therefore gives one fixed point
`t_w` in the open cylinder.

Write `F_w(t)=(at+b)/(ct+d)`.  The fixed equation is
`ct^2+(d-a)t-b=0`.  Every branch denominator is positive on `[0,1]`, so the
denominator cocycle gives `ct_w+d>0`.  At `t_w`, `(t_w,1)^t` is an eigenvector
with eigenvalue `lambda=ct_w+d>1`; the other eigenvalue is
`det(F_w)/lambda`.  Consequently the trace is
`lambda+det(F_w)/lambda>0`, the positive square-root formula in the claim
equals `lambda=rho(F_w)`, and the discriminant is positive.  It cannot be a
square.  For determinant `1`,
a square discriminant would factor
`tr^2-r^2=4`, forcing the parabolic trace `2`; for determinant `-1`,
`r^2-tr^2=4` would force trace zero.  Neither is compatible with the strict
interior contraction.  Hence `t_w` is quadratic irrational and belongs to
`X`.

Every point fixed by `T^n` has one length-`n` itinerary and hence is the fixed
point of its inverse word.  Conversely every nonparabolic word gives the
point just constructed.  Disjoint cylinders make the correspondence
injective.  Removing the two pure words proves `#Fix(T^n|X)=3^n-2`.

### 3. Exact periods, zeta, and multipliers

If `E_n` counts points of exact period `n`, fixed points partition as
`3^n-2=sum_(d|n)E_d`.  Möbius inversion gives `E_n`, and every oriented orbit
of exact period `n` has `n` points, so `pi_n=E_n/n`.  Finally

```text
sum_(n>=1)(3^n-2)z^n/n = -log(1-3z)+2log(1-z),
```

which exponentiates to the claimed source Artin--Mazur zeta.

The Möbius derivative is `F_w'(t)=det(F_w)/(ct+d)^2`.  At the attracting
fixed point, `ct_w+d` is the positive spectral radius `rho(F_w)>1`; inversion gives
`|(T^n)'(t_w)|=rho(F_w)^2`.  Matrix powers describe repeated words, so the
logarithm of this multiplier scales by the repetition count.  This completes
the theorem.  QED.

## Route-A boundary and risks

Romik's construction is source arithmetic, but its primitive Pythagorean
triples terminate.  The periodic objects are quadratic irrationals.  This
separation blocks a false prime-orbit interpretation.  The complete periodic
ledger earns A1 analytically; A0 remains weak, and A2/A3 fail.  The documented
`Gamma(2)` geodesic-section factor is only an A4 formal hint here because this
package constructs no same-clock quantum or scattering operator.

The source zeta is not a target zeta.  No Euler factor, root number,
automorphy statement, target divisor or functional equation, RH statement,
or Hilbert--Pólya operator is asserted.
