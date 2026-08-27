# Theorem package

## Frozen notation

Let `H` be a finite-dimensional real Hilbert space, let `U,V` be linear
subspaces, and write `P_W` and `R_W=2P_W-I` for orthogonal projection and
reflection.  Define

```text
T = (I+R_V R_U)/2,
T_lambda = (1-lambda)I + lambda T.
```

The discrete clock is iteration number.

## Main theorem — complete relaxed two-subspace atlas

There is an orthogonal decomposition of `H` into

```text
F = (U intersection V) direct-sum (U-perp intersection V-perp),
M = (U intersection V-perp) direct-sum (U-perp intersection V),
```

and mutually orthogonal two-dimensional principal planes `E_j`, with angles
`0<theta_j<pi/2`.  Relative to suitable oriented bases,

```text
T_lambda|F = I,
T_lambda|M = (1-lambda)I,
T_lambda|E_j =
  [[1-lambda sin^2(theta_j), -lambda sin(theta_j)cos(theta_j)],
   [lambda sin(theta_j)cos(theta_j), 1-lambda sin^2(theta_j)]].
```

Consequently:

1. For `lambda != 0`, `Fix(T_lambda)=F`; for `lambda=0`, the whole space is
   fixed.
2. The two eigenvalues on `E_j` are
   `1-lambda sin^2(theta_j) +/- i lambda sin(theta_j)cos(theta_j)` and have
   squared modulus `1-lambda(2-lambda)sin^2(theta_j)`.
3. If `0<lambda<2`, then `T_lambda^n` converges in operator norm to `P_F`.
   The exact off-fixed rate is the largest of `|1-lambda|` on a nonzero
   mismatch space and the generic moduli above.  Thus `lambda=1` is the unique
   uniform minimizer whenever a nonfixed direction exists; at `lambda=1` the
   generic rate is the cosine of the Friedrichs angle.
4. For the same window,
   `P_U T_lambda^n x -> P_(U intersection V)x`.
5. At `lambda=2`, `T_2=R_VR_U` is orthogonal: it is identity on `F`, minus
   identity on `M`, and rotation by `2 theta_j` on `E_j`.  It has finite order
   exactly when every generic `theta_j/pi` is rational; mismatch directions
   add a factor two to the least common order when needed.
6. If `lambda` lies outside `[0,2]` and a nonfixed direction exists, that
   direction has modulus greater than one.  The endpoints `0,2` are therefore
   genuine identity/orthogonal boundaries, not contracting cases.

## Trace and determinant corollary

Let `f=dim F`, `h=dim M`, and put

```text
a_j = 1-lambda sin^2(theta_j),
d_j = 1-lambda(2-lambda)sin^2(theta_j).
```

Then

```text
det(I-zT_lambda)
 = (1-z)^f (1-(1-lambda)z)^h
   product_j (1-2a_j z+d_j z^2).
```

All power traces follow either from the two conjugate eigenvalues or from the
second-order recurrence `tau_n=2a_j tau_(n-1)-d_j tau_(n-2)` with
`tau_0=2,tau_1=2a_j`.

## Proof

The cosine-sine/principal-angle decomposition simultaneously block-diagonalizes
the two orthogonal projections.  On a generic principal plane choose
`U=span(e_1)` and `V=span(cos(theta)e_1+sin(theta)e_2)`.  Direct multiplication
of `R_VR_U` gives the rotation matrix through `2theta`; averaging with the
identity and then relaxing gives the displayed block.  The four intersection
spaces give the scalar blocks by their reflection signs.  Orthogonality of the
decomposition proves the fixed-space, rate, convergence, divergence, trace and
determinant statements block by block.  The shadow identity follows from
`P_U P_F=P_(U intersection V)`.  At `lambda=2`, finite order of a direct sum of
plane rotations is equivalent to every rotation angle being rational in units
of `2pi`.

## Evidence boundary

The executable certificate rebuilds 28 rational generic blocks and 21
eight-dimensional composite models.  It does not prove the principal-angle
decomposition.  Conversely, the proof does not certify implementation signs;
that is why the projector checker, SymPy derivation, replay, and mutations are
kept separately.

## Route-A theorem

The owner is generic projection geometry.  Prime and composite dimensions,
angles, and denominator choices obey the same theorem.  There is no intrinsic
rational-prime primitive carrier, prime-power repetition, `log p` clock, or
arithmetic target determinant.  The exact orthogonal endpoint is a formal A4
hint only.  The strict result is

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT),
ROUTE_A_REJECTED, Route B false.
```
