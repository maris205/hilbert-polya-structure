# Theorem and boundary package — C118

## Structural proposition

For

```text
F(q,p)=(grad U(q)-gamma p,q),  gamma=1/2,
```

the exact inverse is `(Q,P) -> (P,gamma^{-1}(grad U(P)-Q))`.  With the standard
two-site symplectic matrix `Omega`, the Jacobian obeys

```text
J(q)^T Omega J(q) = gamma Omega,    det J(q)=gamma^2=1/4.
```

For `lambda=q dot dp`, the exact primitive relation is

```text
F^*lambda-gamma lambda=d(U(q)-gamma p dot q).
```

## Orbit and mode proposition

The synchronous fixed states are `0` and `5`; the synchronous states `2,6`
form a primitive period-two orbit.  The dimer Laplacian eigenvalues are `0,2`.
The period-two mode traces are `-59/4,-13`, both mode determinants are `1/4`,
and

```text
det(I-zM)=(1+59z/4+z^2/4)(1+13z+z^2/4).
```

The direct four-dimensional calculation equals this reconstruction exactly.

## Boundary

Only named low-period witnesses and their tangent monodromy are certified.
Completeness, a transfer/Fredholm/nuclear owner, analytic continuation, and
Route B remain unestablished.
