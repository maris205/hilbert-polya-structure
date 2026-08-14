# Proof package

## Theorem 1: all-width incidence ladder

For `m >= 3`, let

```text
A_m = 0^(m-2) 2 1
B_m = 0^(m-3) 2 3 1.
```

Both are admissible and primitive: each contains exactly one symbol `2`, so
neither can be a proper power.  Direct cancellation of cyclic `m`-windows
after inserting one zero gives

```text
N_m(A_(m+1))-N_m(A_m)
 = e_(0^(m-1)2)+e_(10^(m-1))-e_(10^(m-2)2),

N_m(B_(m+2))-N_m(B_(m+1))
 = e_(0^(m-1)2)+e_(10^(m-1))-e_(10^(m-2)2).
```

Subtracting proves

```text
N_m(A_m)+N_m(B_(m+2))=N_m(A_(m+1))+N_m(B_(m+1)).
```

## Theorem 2: exact period-six algebra

Put

```text
c = -sqrt(7)/6
D = sqrt(25+4sqrt(7))
a = (-1-D)/12
d = (-1+D)/12.
```

The tuple `(a,a,c,d,d,c)` has sign word `---++-` and each cyclic residual
`1-6q_j^2-q_(j-1)-q_(j+1)` is exactly zero.  Its monodromy has determinant
one and trace

```text
18062+5352sqrt(7).
```

The trace polynomial is

```text
T^2-36124T+125728516,
```

and eliminating `T=z+z^-1` gives the irreducible reciprocal polynomial

```text
z^4-36124z^3+125728518z^2-36124z+1.
```

Modulo `13` this is `z^4+3z^3+6z^2+3z+1`.  Its gcds with
`z^13-z` and `z^169-z` both have degree zero, so it has neither a linear
nor a quadratic factor over `F_13`.  A reducible quartic must have one of
those factors; hence the displayed quartic is irreducible over `Q`.

The nonphysical expanding pair contributes

```text
E_B6=acosh(9031-2676sqrt(7)).
```

The exact interval `1950 < 9031-2676sqrt(7) < 1951` follows from square
margins `13729` and `432`.

## Theorem 3: width-at-most-four obstruction

The locked period-five trace polynomial has a root in `(-711,-710)` that is
nonphysical for both `A5` and `B5`.  Hence each excess exceeds `acosh(355)`.
The P55 period-four conjugate half-trace lies in `(51,52)`, while the new
period-six conjugate half-trace lies in `(1950,1951)`.  Thus

```text
E_A5+E_B5 > 2acosh(355)
E_A4+E_B6 < acosh(52)+acosh(1951).
```

For `x>1`, `log(2x-1)<acosh(x)<log(2x)`, and

```text
709^2=502681 > 405808=104*3902.
```

Therefore `E_A5+E_B5>E_A4+E_B6`, contradicting the `m=4` incidence
identity for every width-four potential.  Lower widths embed into width four.

## Proposition 4: finite sharpness

For rows `(C1,A3,A4,B4,A5,B5,B6)`, where `C1=(0)`, and columns

```text
00000, 00021, 00023, 00210, 00231, 02102, 02310
```

the incidence matrix has determinant `+1`.  Its inverse gives block values

```text
E1, -E4A+E5A, -E5B+E6, E4A, -E4B+E5B, E3, E4B.
```

So the finite witness is interpolable at width five.

## Corollary 5: one-sided Hölder gate

Approximating an alpha-Hölder potential on an `m`-cylinder incurs uniform
error at most `C theta^(alpha*m)`.  The ladder kills the approximant, and the
four orbit lengths sum to `4m+4`.  Hence

```text
|Delta_m| <= C(4m+4)theta^(alpha*m).
```

This is necessary, not sufficient.  The unrestricted two-sided problem
also requires a future-dependent cohomological reduction.
