# DRC01 — original-card independent derivation

Candidate: ANG-20260923-DRC01. Internal same-model review, **NOT_CALIBRATED**.
Result: the prescribed Borel owners and clocks exist. MAIN has exactly one
fixed core, with a four-point full basin and primitive time `log 2`.
The prescribed two-step word is empty for all three owners. This bounded
test leaves MAIN **OPEN / FORK**, not a global target pass or a proved failure.

## 1. Inputs and method

The sole scientific input was `candidate-card.md`, original lines 1–93,
personally read through original EOF: 5702 bytes, SHA-256
`d51292ce726c02338670acb5ad7da4bc2b28f115522f3dd1da855097d3b0fb46`.
This prefix was reread and remeasured after the separate card-only release.
CP1 preceded that release; its frozen report was not changed. ARS router and
previously read workflow/DA/runtime instructions govern the staged audit.
No author paper, README, ledger, appended outcome, sibling or peer scientific
material was accessed. No auxiliary, web, scientific code or numerical search
was used. All calculations below are exact algebra from this card.
Retained historical context is disclosed; no blindness, error independence,
external peer review, calibration or model change is claimed.

## 2. Readout, full inverse sets and terminals

For an integer `d>0`, `floor(floor(x)/d)=floor(x/d)`. Thus a given second
coordinate fixes `d=|floor(y)|`, and its quotient cells are exactly
`dq <= x < d(q+1)`. These unions of original unit cells do not change labels
or the rule; when `d=0`, the prescribed quotient is zero.
For integer interface data, MAIN sends `(n,d,d^2)` to
`(d,d^2,d(n-d floor(n/d)))`, so the stated zero-remainder test is exact.
Nothing restricts the subsequent source to this integer embedding.

For a target `t=(u,v,w)`, the following are exhaustive predecessor formulas.

- MAIN: if `u=0`, there is no predecessor. If `u!=0` and `d=|floor(u)|=0`,
  the unique predecessor is `(w/u,u,v)`. If `d>0`, set
  `A=w/u`, `E=v/u-d`, and `I={q in Z: 0<=A+Eq<d}`.
  The complete predecessor set is `{(A+(v/u)q,u,v):q in I}`.
- Q: there is exactly the predecessor `(w/u,u,v)` when `u!=0`, and none
  when `u=0`. No artificial quotient label is retained.
- L: put `d=|floor(u)|`. If `d=0`, the unique predecessor is `(w,u,v)`,
  including `u=0`. If `d>0`, set `A=w`, `E=v-d`; use the same set `I`,
  giving every predecessor `(w+vq,u,v)`.

In either integer enumeration, `E>0` gives
`-A/E <= q < (d-A)/E`; `E<0` gives
`(d-A)/E < q <= -A/E`. These are finite, possibly empty sets.
When `E=0`, every integer is admissible exactly when `0<=A<d`; otherwise
none is. In the all-integer case different integers give different points
because the coefficient of `q` in the reconstructed first coordinate is `d`.
In general any repeated point would have the same prescribed `floor(x/d)`,
so the enumeration introduces no multiplicity of actual predecessors.
Its original label is recovered uniquely as `n=floor(x),m=floor(u)`.
These criteria give the exact images and counts, without a finite cutoff.
For example MAIN and L both have infinitely many predecessors of `(1,1,0)`;
L, despite its total forward domain, has none at `(1,3,1)`.

MAIN/Q have precisely the terminal plane `y=0`; L has no terminals.
A MAIN/Q terminal target `(u,0,w)` with `u!=0` has the unique legal
predecessor `(w/u,u,0)`. If `u=0`, it has none. The permission of the target's
next step is never added to an inverse test. In particular the strip with
`floor(y)=0` and `y!=0` remains legal. These statements include all cuts.
Iterating the displayed full predecessor operations gives every finite
incoming history, including histories ending at a terminal state.

## 3. Every-Borel IMAGE and the prescribed full-point clocks

Fixing an original integer cell, the MAIN inverse has determinant `1/u`;
Q has the same determinant. The L inverse determinant is `1`.
Consequently the prescribed versions are

`J_MAIN=J_Q=1/|u|`, `kappa_MAIN=kappa_Q=log|y|`, and `J_L=1`, `kappa_L=0`.

They are positive finite at every assigned inverse point, and legal clocks
are finite; MAIN/Q never take `log 0`. L is defined on its entire source.
Each inverse is the restriction of a smooth injective germ on `u!=0`
for MAIN/Q, or an affine determinant-one map for L. Its exact domain above
is Borel, including the assigned half-open faces. Change of variables on
that germ therefore proves, for EVERY Borel subset `B` of the domain,
`mu(theta(B))=integral_B J dmu`. Restriction to null subsets does not supply
uniqueness of the pointwise version; the card's specified germ supplies it.
This is branchwise IMAGE, not invariance under the many-to-one global map.
Two distinct arrows with the same endpoints need not have the same clock.

Finite legal branch itineraries are countable. On each, forward and inverse
maps are injective Borel restrictions of their composed analytic germs.
Their prescribed determinants multiply, including assigned null faces;
successive change of variables proves the corresponding every-Borel law.
For a finite-pair arrow `g=(z,a-b,w)`, the partial range map from `w` to `z`
has IMAGE density `exp(S_b(w)-S_a(z))=exp(-c(g))` on each such branch pair.
This also checks the sign: `(Fz,-1,z)` has clock `-kappa(z)` and forward
IMAGE density `exp(kappa(z))`.

## 4. Actual histories, all groups, kernels and phases

Every legal iterate domain is Borel. The actual triples form a Borel
groupoid in `X x Z x X`, as a countable union of equal-iterate sets.
Every point has countably many predecessors, so its full orbit is countable.
This is a Borel/set-level owner; no continuity, etaleness, Hausdorff or
contact structure of the coarse quotient is asserted.

If two witnesses represent the same triple, their two exponents differ by
the same integer. Extending the shorter pair through the longer legal common
future adds identical clock sums, which cancel. Thus `c` descends. The same
synchronization on composition proves additivity. No extension past a
terminal point is used. Countable witness selection also proves `c` Borel.
Translation of height commutes with all extension arrows and hence descends
to the set quotient of the full `X x R`, without deleting any null states.

Write `K_lag={g:k(g)=0}`, `K_clock={g:c(g)=0}` and
`K_joint=K_lag intersect K_clock`. These are full arrow kernels, not merely
isotropy kernels. For ANY point, nonzero source isotropy is equivalent to
an eventual legal cycle. If its least eventual source period is `p`, then
`Iso_z=p Z`. Otherwise, including every terminating history, `Iso_z={0}`.
For a cycle `v_0,...,v_(p-1)`, put `K=sum_i kappa(v_i)`.
On its entire basin, `c(np)=nK`, `H_z=K Z` and extension isotropy is
`{np:nK=0}`. Thus `K!=0` gives least positive physical time `|K|`, while
`K=0` retains all source isotropy but gives no positive physical return.
On non-eventual sources `H_z={0}`. There is no padding with terminal loops.

For MAIN/Q, `K=log(prod_i |y(v_i)|)`; on a legal cycle every factor is
nonzero. For L, `c=0` on ALL arrows, so globally `H_z={0}`,
`K_clock=G`, `K_joint=K_lag`, and extension isotropy equals source isotropy.
There is also a direct Q clock identity without a cycle census: write any
actual cyclic coordinate sequence as `x_(i+3)=x_i x_(i+1)`. Multiplication
over the cycle yields `P=P^2`, where `P=prod_i x_i!=0`; hence `P=1` and
`K=0`. Thus ALL Q isotropy clocks vanish and `H_z={0}` globally. This does
not say Q's arrow cocycle is identically zero or classify its longer cycles.

For a fully explicit basin/phase description, let `A_j=sum_(i<j) kappa(v_i)`.
If `z` first reaches `v_j` in `r` steps, choose
`lambda_z=r-j`, `b_z=S_r(z)-A_j`. For any two basin points the complete
arrows are precisely
`k=lambda_z-lambda_w+np`, `c=b_z-b_w+nK`, for `n in Z`.
Therefore their kernel memberships are exactly the vanishing of the first,
second, or both expressions; their height phase is `h-b_z mod K Z`.
For `K=0`, this is a real-valued phase, not a circle. Different choices of
cycle phase or later entrance give the same quotient description.

Every basin is exactly `union_(r>=0) Inv^r({v_0,...,v_(p-1)})`, using ALL
inverse branches above, with no cell restriction. More generally the whole
source orbit of `x` is `union_(a,b>=0, F^b x legal) Inv^a(F^b x)`.
For a non-eventual or terminal orbit choose any base and an arrow to each
point; its clock `b_z` is independent of that choice because isotropy clocks
vanish. Then `c=b_z-b_w` and `h-b_z` describes the full real phase.
These formulas cover all incoming and kernel tests, conditionally where the
periodic-core classification itself is outside the frozen window.

## 5. ALL fixed points and their ENTIRE basins

A companion-map fixed point has the form `(t,t,t)`.
For MAIN legality gives `t!=0`, and the third coordinate gives `t=q+1`.
Thus `t` is an integer. At a positive such integer `q=1`, while at a
negative one `q=-1`; the only solution is `p=(2,2,2)`.
For Q the equation is `t^2=t`, with `t!=0`, giving only `(1,1,1)`.
For L it is `qt=0`: exactly `p_t=(t,t,t)`, `0<=t<1`, including zero.
For nonzero `floor(t)`, the quotient is its sign, so there are no omissions.

For MAIN put
`p=(2,2,2)`, `a=(1,2,2)`, `b=(-2,1,2)`, `d=(-1/2,-2,1)`.
The inverse criteria give, exactly,
`Inv(p)={p,a}`, `Inv(a)={b}`, `Inv(b)={d}`, `Inv(d)=empty`.
For the first three targets their admissible quotients respectively are
`{0,1}`, `{-2}`, `{-1}`; at the last target the condition is
`0<=-2+3q<1`, with no integer solution. Hence the FULL basin is these four
points, with `d -> b -> a -> p -> p`. The predecessorless point `d` is
legal, not terminal. No later inverse generation adds another point.

Let `ell=log 2`. First-entry depths at `(p,a,b,d)` are `(0,1,2,3)`, and
first-entry clock sums are `(0,ell,ell,2ell)`. Put `beta=S_r-r ell`;
then `beta(p)=beta(a)=0`, `beta(b)=beta(d)=-ell`.
The entire restricted source groupoid is `B x Z x B`, where `B={p,a,b,d}`,
with `c(z,k,w)=k ell+beta(z)-beta(w)`. Every point has source isotropy `Z`,
time group `ell Z` and trivial extension isotropy, including nonfixed ancestors.
The full clock kernel has `k=(beta(w)-beta(z))/ell`; its joint lag-zero
part consists exactly of pairs within `{p,a}` or within `{b,d}`.
It contains nonidentity arrows, although its isotropy is trivial.
The lag kernel contains all pairs at lag zero. The complete physical phase
is `h-beta(z) mod ell`, here also `h mod ell`. Thus there is exactly ONE
positive fixed-core packet, with primitive time `log 2` and all repeats.
The four source states are not four packets or four physical primitive copies.

Q's fixed point has itself as its unique predecessor, so its complete basin
is a singleton. Its source and extension isotropy are `Z`, but `H={0}` and
its height phase is the real number `h`.
For L every fixed point `p_t` has `floor(t)=0`, hence exactly itself as its
predecessor. These singleton basins never merge. Each has source/extension
isotropy `Z`, `H={0}` and phase `h`. Their continuum cardinality does not
give a continuum of positive primitive packets.

## 6. The entire prescribed two-step cells

Write an initial point `(x,y,z)` in the complete cube `(4,2,4)`.
Actual two-step closure forces `z=x` and the first new third coordinate to
be `y`; the rotated point is then `(y,x,y)`. Here `x in [4,5)`,
`y in [2,3)`, and the two prescribed quotients are respectively `2` and `0`.
All relevant MAIN/Q permissions are nonzero, so illegality is not being
used to remove an otherwise possible return.

MAIN's first closure equation is `x(y-2)=y`; the second is `xy=x`.
The second forces `y=1`, outside the full half-open interval. Hence none.
Q's first closure equation is `xy=y`, forcing `x=1`, again outside.
L's first closure equation is `x-2x=y`, impossible in these positive cells.
Thus there is no return of period dividing two in this word for any owner,
and its rotation adds none. The unequal coordinate cells exclude a repeated
fixed point as well. No other two-step word or longer cycle was searched.

## 7. Scoped judgment and strongest alternative

MAIN survives the frozen diagnostic: its complete fixed ledger is nonempty,
has ordinary-prime time and no duplicate packet, and the specified word adds
nothing. This is a genuine positive local result, not a reason to manufacture
an obstruction. Q/L prove neither success nor failure of MAIN by proxy.
The strongest positive interpretation is an owned same-source IMAGE clock
and one exact prime-2 packet with all null-state ancestry retained.
The unproved step is the rest of MAIN's periodic ledger: other words may
introduce nonprime lengths, duplicate prime packets, zero clocks or missing
prime coverage. No such existence or absence is asserted here.
Global prime-only/uniqueness/coverage and strong naturalness remain OPEN.
The all-point branch convention is a frozen design, not an a.e.-uniqueness
theorem. No classical suspension, formal Route result, T3 or Route B credit
is claimed. Freeze this raw record before any manuscript/peer exposure;
checkpoint 2 and final checkpoint 3 require a separate paper unlock.
