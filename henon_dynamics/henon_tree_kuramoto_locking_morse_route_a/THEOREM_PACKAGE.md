# Theorem package

## Frozen convention

Let `T=(V,E)` be a connected tree on vertices `0,...,N-1`, rooted at `0`.
Orient every edge from its parent to its child.  Its incidence column has `-1`
at the parent and `+1` at the child.  With positive diagonal edge matrix `K`,

```text
theta' = omega - B K sin(B^T theta).
```

Write `Omega=N^{-1} sum_i omega_i`, `eta=omega-Omega*1`, and
`delta=B^T theta`.  Phase vectors are identified under diagonal rotation.

## Main theorem

For the edge `e=(parent,child)`, let `S_e` be the component containing the
child after deleting `e`, and define

```text
F_e = sum_{i in S_e} eta_i.
```

Then:

1. Every locked solution has common frequency `Omega`, and `F` is the unique
   edge vector satisfying `B F=eta`.
2. A locked state exists if and only if `|F_e|<=K_e` for every edge.
3. If all inequalities are strict, there are exactly `2^(N-1)` locked states
   modulo diagonal rotation.
4. If exactly `s` edges are saturated and none is violated, there are exactly
   `2^(N-1-s)` branches.  The two inverse-sine branches merge on each saturated
   edge.
5. At any branch, the lifted local-potential Hessian is
   `H=B diag(K_e cos(delta_e)) B^T`.  On the rotation quotient its Morse index
   is the number of negative edge cosines, and its nullity is the number of
   saturated edges.
6. In the strict chamber, exactly one branch has all edge cosines positive;
   it is linearly asymptotically stable modulo rotation.  Every other strict
   branch is unstable.  Saturated branches are nonhyperbolic.
7. If one cut is violated, no locked state exists.

## Proof

Summing the laboratory equations shows that any common locked frequency is
`Omega`.  In the rotating frame a locked state obeys `B f=eta`, where
`f=K sin(delta)`.  The tree incidence matrix has rank `N-1`, hence is injective
on its `N-1` dimensional edge space.  Summing `Bf=eta` over `S_e` cancels every
internal edge.  The single cut column contributes `+f_e`, so `f_e=F_e`.  This
both proves the cut formula and uniqueness.

The scalar equation `K_e sin(delta_e)=F_e` is solvable precisely when the cut
inequality holds.  It has two solutions modulo `2*pi` under strict inequality
and one at equality.  A tree has a unique path from the root to every vertex,
so arbitrary edge differences reconstruct a unique phase vector after
`theta_0=0`; there is no cycle constraint.  Multiplication of the independent
edge counts proves the branch formulas.

On a local lift, take
`V(phi)=-eta^T phi-sum_e K_e cos((B^T phi)_e)`.  The rotating-frame flow is
`-grad V`, and its Hessian is `H`.  Let `Q` be any basis matrix for the
rotation quotient `1^perp`.  The square matrix `P=B^T Q` is invertible: its
kernel would give a vector in both `1^perp` and `ker B^T=span{1}`.  Therefore

```text
Q^T H Q = P^T diag(K_e cos(delta_e)) P.
```

Sylvester's law gives the index and nullity.  The linearized vector field is
`-H`; it is strictly stable on the quotient exactly on the all-positive branch.

## Boundary ledger

- `N=1`: the quotient is a point.
- Identical frequencies: all cuts vanish; edge differences are `0` or `pi`.
- Saturation: branch merger and Hessian nullity, not hyperbolic stability.
- `K_e=0`: a nonzero demand forbids locking; zero demand leaves a disconnected
  phase constraint and changes the frozen positive-weight owner.
- Graphs with cycles: `Bf=eta` has cycle-flow freedom, so the theorem does not
  transfer by relabeling.
- Unlocked dynamics: no global classification is claimed.

## Route-A boundary

The strict tuple is

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT).
```

The clean relative equilibria and local gradient structure are exact but have
no intrinsic rational-prime carrier, logarithmic prime clock, target zeta, or
target analytic structure.  Overall status is `ROUTE_A_REJECTED`; Route B is
false.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
