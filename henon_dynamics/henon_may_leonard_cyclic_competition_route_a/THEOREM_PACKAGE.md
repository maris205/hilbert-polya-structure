# HCS-C358 theorem package: May--Leonard cyclic competition

## Status, convention, and claim boundary

**Status:** `PROVED` for the frozen cyclic chamber and the explicitly listed
closure faces.  **Route-A verdict:** `ROUTE_A_REJECTED`.  **Scope:**
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Let `a,b>=0` and assume the strict intransitive condition

```text
(a-1)(b-1)<0.
```

On the closed positive octant consider

```text
x' = x(1-x-a y-b z),
y' = y(1-b x-y-a z),
z' = z(1-a x-b y-z).                         (1)
```

The theorem does not classify the founder-control chamber `a>1,b>1` or the
nonhyperbolic walls `a=1` and `b=1`, except for their common point
`a=b=1`.  It makes no finite-population, stochastic-extinction, arithmetic,
target-determinant, target-zero, or quantization claim.

## Main theorem

Put

```text
S=x+y+z,       Q=xy+yz+zx,       R=xyz/S^3
```

in the interior.  Write

```text
e=(1,1,1)/(1+a+b),   E1=(1,0,0), E2=(0,1,0), E3=(0,0,1).
```

### Theorem (complete cyclic-chamber trichotomy)

1. The positive octant is forward invariant, its interior is preserved, and
   every solution is forward complete and bounded.  The origin is repelling
   relative to the positive octant, and `e` is the unique interior
   equilibrium.

2. Along every interior solution,

   ```text
   S' = S-S^2+(2-a-b)Q,                                      (2)
   (log xyz)' = 3-(1+a+b)S,                                 (3)
   (log R)' = (2-a-b)(S^2-3Q)/S.                            (4)
   ```

   Moreover

   ```text
   S^2-3Q=((x-y)^2+(y-z)^2+(z-x)^2)/2,
   ```

   so the sign in (4) is strict away from the positive diagonal.

3. If `a+b<2`, every interior solution converges to `e`.  There is no
   nonconstant interior periodic orbit.

4. Suppose `a+b=2`.  Set `(u,v,w)=(x,y,z)/S` and

   ```text
   tau(t)=log(1+S(0)(exp(t)-1)).                             (5)
   ```

   Then `S'=S(1-S)`, `d tau/dt=S`, and, with `delta=1-a=b-1`,

   ```text
   du/dtau=delta u(v-w),
   dv/dtau=delta v(w-u),
   dw/dtau=delta w(u-v).                                   (6)
   ```

   The product `h=uvw` is constant.  The centre `u=v=w=1/3` is fixed.  For
   every `0<h<1/27`, the level `u+v+w=1, uvw=h` is one periodic orbit.  If
   `r_-(h)<1/3<r_+(h)<1` are the two roots in `(0,1)` of

   ```text
   r(1-r)^2=4h,
   ```

   its least normalized period is

   ```text
   T(h)=2/|delta| integral_[r_-(h)]^[r_+(h)]
        dr/sqrt(r(r(1-r)^2-4h)).                            (7)
   ```

   Every noncentral original solution approaches exactly one phase translate
   of this periodic orbit: if `U` is its normalized periodic solution with
   `U(0)=(u(0),v(0),w(0))`, then

   ```text
   (x,y,z)(t)-U(t+log S(0)) -> 0.                           (8)
   ```

5. If `a+b>2`, the coexistence equilibrium has radial eigenvalue `-1` and a
   complex tangent pair with

   ```text
   Re lambda=(a+b-2)/(2(1+a+b))>0,
   (Im lambda)^2=3(a-b)^2/(4(1+a+b)^2).                    (9)
   ```

   Its complete stable set in the interior is the positive diagonal.  Every
   other interior solution has `R(t)->0`, approaches the full oriented
   heteroclinic cycle on the boundary, and spends an unbounded time near each
   successive axial saddle.  Consequently it is not periodic and it does not
   converge to any one axial equilibrium.

6. If `a<1<b`, the cycle orientation is

   ```text
   E1 -> E3 -> E2 -> E1;
   ```

   if `b<1<a`, it is the reverse cycle.  At `a=b=1`, equation (1) becomes
   `x_i'=x_i(1-S)`: all ratios are constant and the whole simplex `S=1`
   consists of equilibria.

## Proof

### Step 1: positive global flow and an absorbing annulus

Each coordinate equation has the form `x_i'=x_i g_i(x,y,z)`.  Hence a zero
coordinate stays zero and a positive coordinate is an exponential of an
integral and cannot reach zero at finite time.  Because the cross
coefficients are nonnegative,

```text
x'<=x(1-x), y'<=y(1-y), z'<=z(1-z).
```

Scalar comparison bounds every coordinate by `max{1,x_i(0)}` and proves
forward completeness.  Conversely, for a constant `C=C(a,b)>0`, the exact
quadratic expression for `S'` gives

```text
S'>=S-C S^2.
```

Thus an interior orbit is eventually bounded away from the origin.  These
two comparisons make every interior positive semiorbit precompact in an
annulus of the positive octant.

At an interior equilibrium the circulant linear system

```text
[1 a b; b 1 a; a b 1](x,y,z)^T=(1,1,1)^T
```

has determinant

```text
(1+a+b)(1+a^2+b^2-a-b-ab).
```

The second factor is half the sum of `(a-b)^2,(a-1)^2,(b-1)^2`; it vanishes
only at `a=b=1`, outside the strict chamber.  Subtracting cyclic rows or
inverting the matrix gives the unique positive solution `e`.

### Step 2: the decisive normalized-product identity

Adding the three equations and using
`x^2+y^2+z^2=S^2-2Q` proves (2).  Dividing each coordinate equation by its
coordinate and adding proves (3).  Subtracting `3S'/S` from (3) proves (4).
The displayed sum-of-squares identity supplies its strict sign.

This identity is global information, not a local linearization.  It also
immediately excludes every non-diagonal periodic orbit whenever `a+b!=2`.

### Step 3: the coexistence phase `a+b<2`

Here `R` increases strictly off the diagonal and is bounded above by `1/27`
by AM--GM.  Since `R(t)>=R(0)>0` and `S` stays in a compact positive annulus,
the normalized coordinates stay away from the boundary of the simplex.
LaSalle's invariance argument applied to `log R` puts the omega-limit set in
`x=y=z`.  That diagonal is invariant and obeys

```text
r'=r(1-(1+a+b)r),
```

whose only positive limiting state is `r=1/(1+a+b)`.  Hence the entire orbit
converges to `e`.

### Step 4: the critical periodic foliation

When `a+b=2`, equation (2) is the logistic equation.  Its exact solution is

```text
S(t)=S0 exp(t)/(1+S0(exp(t)-1)).                            (10)
```

Direct differentiation proves (5) has derivative `S`.  Differentiating
`u=x/S`, and then using `a+b=2`, gives (6).  Its components sum to zero and
the derivative of `uvw` vanishes.

For `0<h<1/27`, the set `u+v+w=1, uvw=h` is a smooth compact circle around
the centre.  Equation (6) has no zero on it, so its flow traverses that circle
periodically.  At an extremum of `u`, `v=w`; hence

```text
(du/dtau)^2=delta^2 u[u(1-u)^2-4h].                        (11)
```

One trip from `r_-` to `r_+` and back gives (7).  Finally
`S(t)->1` and `tau(t)-t->log S0`; continuity of the periodic flow proves (8)
and uniqueness modulo its least period.

### Step 5: the exceptional diagonal above criticality

At `e`, direct differentiation gives one radial eigenvector `(1,1,1)` with
eigenvalue `-1`.  Diagonalizing the remaining circulant block gives (9).
For `a+b>2`, the local stable manifold is one dimensional.  The positive
diagonal is invariant and tangent to that eigenspace, so uniqueness in the
stable-manifold theorem identifies the two locally.  If an interior orbit
converges to `e`, it eventually lies on this local stable manifold and hence,
by uniqueness of solutions, lay on the diagonal from the start.  Thus the
global interior stable set of `e` is exactly the diagonal.

For a non-diagonal orbit, `R` decreases to a limit.  If that limit were
positive, precompactness and LaSalle applied to `-log R` would force the orbit
to converge to `e`, contradicting the preceding paragraph.  Therefore
`R->0`, so the normalized orbit approaches the boundary simplex.

### Step 6: exhaustion of the boundary omega-limit set

Assume first `a<1<b`.  On `z=0`,

```text
d/dt log(y/x)=-(b-1)x-(1-a)y<0,
```

so the open edge connects `E2` to `E1`.  Cyclic permutation gives the other
two connections and the orientation in the theorem.  Swapping `y,z` swaps
`a,b` and reverses this orientation.

At every axial equilibrium, the stable manifold inside the closed octant is
the incoming coordinate face; the remaining missing-species eigenvalue is
`1-min(a,b)>0`.  Hence no interior orbit converges to one axial equilibrium.
The omega-limit set of a precompact orbit is compact, connected, invariant,
and internally chain transitive.  It is also bounded away from the origin.
A point of this omega-limit set lying in the relative interior of a
coordinate plane must therefore lie on a bounded complete orbit whose
alpha-limit stays in the same compact set.  In that plane the Dulac
multiplier 1/(xy) has divergence -1/x-1/y<0.  Poincare--Bendixson, the
strict edge-ratio above, and the absence of a positive two-species
equilibrium leave only the unique connection from the losing axial
equilibrium to the winning one: the other positive-plane orbits have the
origin in their backward limit or leave every compact set in negative time.
Non-equilibrium points on an axis are excluded for the same reason, since
their backward limit is the origin.
Thus the omega-limit set is contained in the three axial equilibria and the
three just-classified connections.  A single axis point is excluded by its
stable face, and the closure of a proper directed subchain is not internally
chain transitive.  Indeed, choose disjoint small axial neighbourhoods and
compact middle arcs on its included connections.  The strict ratio has a
uniform sign on each middle arc, and the flow crosses the two boundary
sections in only the directed order.  For sufficiently small jump size, no
long-time pseudo-orbit inside a proper subchain can return from its terminal
axial neighbourhood to its initial one.  The only remaining set is therefore
the entire three-connection cycle.

The orbit consequently enters arbitrarily small neighbourhoods of every
axial saddle.  Its outgoing coordinate at entry tends to zero.  Inside a
fixed sufficiently small neighbourhood that coordinate grows at rate at most
`1-min(a,b)+epsilon`; the time required to reach the fixed exit section is
bounded below by a logarithm of the reciprocal entry coordinate.  These
residence times diverge.  This finishes the supercritical statement.

### Step 7: closure faces

Coordinate axes carry scalar logistic flow; open coordinate edges are the
connections used above.  The origin is repelling by the lower comparison in
Step 1.  Interchanging `a,b` and `y,z` reverses the cycle.  When `a=b=1`, all
three equations share the factor `1-S`, so the ratios are fixed, `S` is
logistic, and `S=1` is precisely the equilibrium simplex.  On `a=1` or
`b=1` away from that point an axial transverse eigenvalue vanishes; these
nonhyperbolic dominance walls are recorded but deliberately excluded from the
strict-chamber theorem.

## Exact evidence and independence map

- Canonical producer: exact rational phase, invariant, critical-leaf,
  logistic, edge and boundary ledgers.
- Independent checker: reconstructs every row without importing producer
  code and locks strict JSON/YAML semantics.
- Symbolic lane: verifies the source identities, coexistence characteristic
  polynomial, critical quartic and time change.
- Replay: two isolated producer/checker executions must be byte identical.
- Hostile lane: repaired-hash attacks change identities, signs, phases,
  critical conservation, orientation, Route-A gates and scope flags.

These computations audit conventions and algebra.  They do not prove the
global LaSalle, stable-manifold, omega-limit, or periodic-leaf arguments.

## Route-A conclusion

The critical simplex has a real analytic continuum of source periodic leaves,
which justifies only `A1_WEAK`.  The model has no intrinsic rational-prime
objects, no prime-power repetition law, no logarithmic-prime clock, and no
target determinant or natural target-zero quantization.  The strict tuple is

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL).
```

Route B remains locked.
