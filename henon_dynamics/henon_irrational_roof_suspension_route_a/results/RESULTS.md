# C130 results

## Exact construction

```text
B = [[1,1],[1,1]]
M(u,v) = [[u,v],[u,v]]
Delta(u,v) = det(I-M) = 1-u-v
d_tau(s) = 1-exp(-s)-exp(-sqrt(2)*s)
```

For every `n>=1`, `Tr M^n=(u+v)^n`.  Regrouping all rooted closed words by
primitive root gives the all-period intrinsic dynamical Euler product.  The
analytic product is absolutely convergent for `Re(s)>h`, where
`e^-h+e^-sqrt(2)h=1`; the explicit exponential polynomial is entire.

## Replay prefix

| period | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rooted words | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |
| primitive cycles | 2 | 1 | 2 | 3 | 6 | 9 | 18 | 30 | 56 | 99 |
| clock sectors | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

Totals are 2,046 rooted words, 226 primitive cycles, and 65 clock sectors.

## Separation and control

Distinct integer count vectors have distinct lengths under `(1,sqrt(2))`.
This is sector separation only: primitive necklaces `000111` and `001011`
share vector `(3,3)` and roof `3+3sqrt(2)`.  The irrational determinant has no
nonzero imaginary period.

For control roof `(1,2)`, sectors `(2,0)` and `(0,1)` collide at time 2 and
`d_rat(s)=1-e^-s-e^-2s=1-q-q^2` satisfies
`d_rat(s+2*pi*i)=d_rat(s)`.

## Boundary

The result is internal to one symbolic suspension.  It supplies no arithmetic
Euler factors, root number, target divisor match, functional equation,
counting-law comparison, or natural self-adjoint lift.  The verdict is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` and Route B is disabled.
