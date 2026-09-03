# HCS-C336 research question

For the finite binary Crow--Kimura mutation--selection equation with one
distinguished master sequence, can the full `2^L`-dimensional spectrum and the
nonlinear normalized dynamics be closed exactly, including every multiplicity,
rank-one secular root, convergence rate and reducible boundary, without
turning a finite-genome crossover into an unsupported error-threshold claim?

The frozen operator is

```text
A_L = (U/L) sum_i (F_i-I) + s |0><0|,
p'  = A_L p - (1^T A_L p)p,
```

with integer `L>=1` and `U,s>0`.  The `s=0` and `U=0` faces are part of the
boundary theorem, not part of the irreducible main chamber.

The required advance is one complete theorem: exact projectivization,
Perron convergence, retained Walsh/Hamming eigenspaces, the remaining
strictly interlacing secular spectrum, the sharp generic projective decay
rate, and all frozen boundaries.  Finite computation is only a convention and
regression receipt.

Route-A scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic data,
Euler factor, root number, target divisor, target zero match, automorphy,
Hilbert--Polya operator or Route-B input is permitted.
