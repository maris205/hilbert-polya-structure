# Entropy-Paired Relative Determinants

Paper10 freezes **SD-C12**. Tensor-prime full-shift atoms are ordered by
entropy and paired by a fixed `1|1` modeling rule:

```text
(p1,p2), (p3,p4), ...
```

The paired difference is trace class on the full half-plane `Re(s)>0`:

```text
p_(2n-1)^(-s) - p_(2n)^(-s)
  = s integral_[p_(2n-1),p_(2n)] x^(-s-1) dx.
```

This yields the exact relative Fredholm determinant

```text
R(s,z) = product_n (1-z p_(2n-1)^(-s))/(1-z p_(2n)^(-s)).
```

On `Re(s)<=1`, this is not a quotient of two separately defined Fredholm
determinants. It is the determinant of a single `I+S_1` relative quotient.
The adjacent `1|1` pairing is a modeling rule canonical only after fixing the
entropy list's starting point and grading orientation.

Its reflected completion `H(s,z)=R(s,z)R(1-s,z)` is holomorphic and exactly
reflection symmetric on `0<Re(s)<1`; at `z=1` it is zero-free yet moves
nontrivially on the critical line. The obstruction is arithmetic orientation:
entropy-rank parity assigns `+1,-1,+1,-1,...` to primes, and this sector sign
does not exponentiate with orbit repetition.

```text
GO_COMMON_STRIP_RELATIVE_DETERMINANT
STOP_POSITIVE_EULER_ORIENTATION
STOP_DIVISOR
ROUTE_A_REJECTED
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```
