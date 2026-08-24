# Theorem package

Let `D` be the unit disk and `L_(a,b)=C_phi_a+C_phi_b` on normalized Bergman space, where `phi_x(z)=1/(x+z)` and `(a,b)∈R*=[3,7/2]×[6,7]`.

## Theorem 1 — uniform geometry

`phi_x(closed D)` is the closed disk with center `x/(x^2-1)` and radius `1/(x^2-1)`.  The two closed images have gap

`g(a,b)=1/(a+1)-1/(b-1) >= 1/45`.

The minimum occurs at `(7/2,6)`.  On `[3,4]×[6,7]`, the minimum is instead zero at `(4,6)`, so that larger rectangle cannot inherit a positive closed-image gap.

## Theorem 2 — trace class and trace-norm continuity

Every `L_(a,b)` is trace class and

`||L_(a,b)||_1 <= 4+25/16=89/16`.

For two parameters in `R*`,

`||L_(a,b)-L_(a',b')||_1 <= 4|a-a'|+(5/32)|b-b'|`.

The proof uses the Bergman rank-one expansion and the exact majorant `sum_(n>=1)(n+1)n r^(n-1)delta=2delta/(1-r)^3`.

## Theorem 3 — every word and every period

For `M_w=[[A,B],[C,D]]`, `t=tr(M_w)`, `delta=(-1)^|w|`, and `Delta=t^2-4delta`, the attracting fixed point, multiplier, and composition trace are

`z_w=(A-D+sqrt(Delta))/(2C)`,

`lambda_w=(t-sqrt(Delta))/(t+sqrt(Delta))`,

`Tr C_Phi_w=1/2+t/(2sqrt(Delta))`.

Consequently all power traces are word sums and

`det(I-zL)=product_[p primitive] product_(k>=0)(1-z^|p| lambda_p^k)`

as an absolutely convergent raw product for `|z|<1/2`.  The trace-class determinant is entire; no raw-factor convergence is claimed beyond that disk.

## Theorem 4 — uniform order sensitivity

The non-cyclic same-count words `aaabb` and `aabab` satisfy

`t_aaabb-t_aabab=a(b-a)^2 >= 175/8`.

The first trace polynomial has positive coefficients and is coordinatewise increasing, so `t_aaabb <= t_aaabb(7/2,7)=10731/4`.  Since `F(t)=1/2+t/(2sqrt(t^2+4))` has derivative `2/(t^2+4)^(3/2)`, their composition traces differ by at least

`2800/(10731^2+64)^(3/2)>0`.

## Boundary

The result is exactly `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.  It proves a uniform nonlinear source family, not a target divisor, arithmetic Euler factors, root number, automorphy, or a Hilbert–Pólya operator.
