# Theorem package: rotation-reduced circular hard rods

Frozen obstruction identifier: `HEN-O280`.

## Frozen owner

Let `N>=1`, `a>0`, `ell>N*a`, and `L=ell-N*a`.  The state is the
collision-glued phase space of `N` indistinguishable, equal unit-mass,
clockwise rods on `T_ell`, modulo **constant global spatial rotations**.
Velocities, including their common drift, are retained.

## Main theorem — `PROVABLE AS CORRECTED`

Choose a cyclic lift of left endpoints and set
`y_i=x_i-(i-1)a`.  Compression induces a bijection to

`((T_L x R)^N)/(S_N x T_L)`,

where `S_N` permutes position–velocity pairs and `T_L` translates every
position by one common constant.  It conjugates the all-real-time hard-rod
flow to free motion `y_i(t)=y_i+t v_i (mod L)`.  At a maximal coincidence
block, incoming spatial velocities are descending and outgoing velocities are
the same multiset in ascending order.  Consequently momentum and kinetic
energy are conserved, simultaneous multiple/disjoint collisions are unique,
and no Zeno accumulation occurs.

A state returns at `T>0` exactly when there are `sigma in S_N` and
`c in T_L` such that

`y_i+T v_i = y_sigma(i)+c (mod L)` and `v_i=v_sigma(i)` for all `i`.

For each distinct velocity `u`, let `Y_u` be its position multiset and let its
translation stabilizer have order `d_u`.  Return is equivalent to

`lcm(d_u,d_w) T (u-w) in L Z`

for every velocity pair.  Thus distinct velocities require all velocity
differences to be commensurable.  Repeated velocity classes may shorten the
period through their spatial symmetries.  A single velocity class is a fixed
shape and has no least positive period.

## Essential obstruction

The theorem is false without rotation reduction.  Changing the cyclic start
adds a common translation by `a` to the compressed points, and for `N=1` the
full moving rod returns after `ell/abs(v)`, not `L/abs(v)`.  Recovering the
complete physical angle requires an additional cocycle and is not claimed.

## Route-A verdict

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, overall
`ROUTE_A_REJECTED`; Route B is disabled.  The A4 entry records only the
natural hard-core kinetic/Friedrichs quantization of the reduced collision
chamber, not a target spectrum or Hilbert–Polya construction.
