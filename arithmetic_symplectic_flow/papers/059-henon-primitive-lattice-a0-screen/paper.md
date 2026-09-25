# A nonlinear integral Hénon map preserves visible vectors but does not own their arithmetic source

**Paper ID:** `059-henon-primitive-lattice-a0-screen`  
**Candidate ID:** `ASFS-20260914-NPH01`  
**Status:** `2026-09-14; P0 FROZEN; A0 SCOPED FAIL`  
**Route state:** A1/A2 not evaluated; Route B `NOT INVOKED`.

## Frozen object

Take `M=R^2`, `omega=dx wedge dy`, and `F(x,y)=(y,y^2-x)`. Its derivative has determinant one, and the displayed inverse is `F^{-1}(x,y)=(x^2-y,x)`, so `F` is one exact symplectomorphism. With `tau=1`, its mapping-torus suspension is complete and non-Zeno. The proposed prime-symbolic ancestry is the visible lattice set `V={(m,n) in Z^2:gcd(m,n)=1}` from 056, lifted through a nonlinear Hénon-type conservative map.

For integers, `gcd(y,y^2-x)=gcd(y,x)`. The inverse has the analogous identity. Hence `F` preserves `Z^2` and every set `V_d={(m,n):gcd(m,n)=d}`, including `V=V_1`.

## A0 audit

The invariant arithmetic decoration is not an internally generated prime mechanism. The map formula is defined on all real points and makes no reference to the integer lattice, primitive vectors, primes, or divisibility. After an analyst selects the lattice, the same calculation preserves every gcd stratum `V_d`, every union of such strata, and many unrelated invariant subsets. Replacing `V_1` by `V_2`, a chosen set of gcd values, or a nonarithmetic lattice subset changes the asserted arithmetic content without changing `F`, the roof, or its dynamics.

Thus the construction fails all four controls: the lattice-removal control leaves the same Hénon map; the gcd-stratum control supplies equally invariant nonprime labels; the arbitrary-label control has no map-level discriminator; and the nonlinear-parent control shows nonlinearity alone does not create arithmetic relevance. `V` is a static selected subset, not a symbolic observable or admissibility rule dynamically derived by this map.

## Gate decision

| Gate | Finding | Status |
| --- | --- | --- |
| P0 | one exact nonlinear symplectic map and one roof frozen | complete |
| A0 | visible arithmetic is analyst-selected static stratum | scoped FAIL |
| A1 | not entered after A0 stop | `NOT EVALUATED` |
| A2 | no same-object analytic owner | `NOT EVALUATED` |
| Route B | no Route-A-ready candidate | `NOT INVOKED` |

No periodic orbit of `F`, numerical observation, or zeta construction may rescue this A0 failure. The same-object ledger remained intact: no orbit data were borrowed from a different Hénon, cat, wheel, or visible-hull carrier.

**Portfolio position: stop/fork.** The nonlinear lift proves that escaping linearity is insufficient. A future Hénon/symplectic proposal must make its own symbolic rule generate or test the arithmetic constraint, rather than merely preserve a preselected arithmetic subset.
