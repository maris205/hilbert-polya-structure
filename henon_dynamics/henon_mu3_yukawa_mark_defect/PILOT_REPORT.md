# C65 bounded pilot

From the exact C64 matrix and C63 kernel basis:

```text
old SNF: [2, 8],   saturation index: 16
all SNF: [2, 2, 8], saturation index: 32
relative jump: 2
```

The normalized vectors (m(z_1)/8,m(z_2)/2,m(z_3)/2) have gcd-one maximal
minor and form the all-direction saturation basis.  The new direction is the
order-two class of (m(z_2)/2=-m(R_4)/2).  A second implementation using
SymPy's exact Smith form agrees with the direct determinantal-divisor route.
