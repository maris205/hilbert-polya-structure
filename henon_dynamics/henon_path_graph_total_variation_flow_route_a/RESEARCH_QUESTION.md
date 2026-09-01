# Research question

Let `P_n` be the unweighted path on `n>=1` vertices and set

```text
(Dx)_i=x_{i+1}-x_i,
J(x)=sum_{i=1}^{n-1}|(Dx)_i|.
```

Can the nonlinear differential inclusion

```text
x'(t) in -partial J(x(t)),   x(0)=x^0 in R^n,
```

be solved globally by an exact finite event rule, with a proof that facets do
not split, all simultaneous collisions are handled, consensus is finite, and
the semigroup value is exactly the ROF proximal point

```text
argmin_y  (1/2)||y-x^0||_2^2+tJ(y)
```

for every real datum and every time?

The question freezes the unweighted path, the Euclidean vertex norm, the
physical semigroup clock, and the anisotropic edge `l1` energy.  General graph
equivalence, numerical Euler discretization, continuum TV flow, and arithmetic
or spectral interpretations are outside the theorem.
