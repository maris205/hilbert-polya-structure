# P162 claims--evidence ledger

**Artifact:** Random Translation Intersection (RTI)  
**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`

| Claim | All-parameter proof engine | Exact falsification pressure | Ownership subtraction |
|---|---|---|---|
| A history `v_1,...,v_t` acts as `E_{span(v_i)}` | erosion composition `E_K E_H=E_{H+K}` and characteristic-two subset sums | literal update versus independently computed span erosion for every tested source/history | erosion algebra is classical; zero contribution credit |
| rank law `[d r]_2 S(t,r)/2^(dt)` | histories spanning fixed `H` are surjections `F_2^t -> H` | brute history rank census and full-rank boundary | finite-field random-rank law is classical; zero contribution credit |
| `V\{0}` makes the full-span clock sharp | pointwise identity `E_H(V\{0})=V\H` | every enumerated subspace through `d=6` | the paper claims only this witness as part of the conjunction |
| worst-source CDF and mean clock | full-rank product plus geometric waiting time at each rank | exact rank counts, pre-`d` zero boundary, rational mean recurrence | no standalone novelty claim for the rank/clock machinery |
| every-target source-size/history polynomial | `H<=Stab(B)` plus independent proper-subset selection on every outside `H`-coset | every target, source weight, and time in exhaustive literal boxes; total-mass identity | residual axis after subtracting morphology and random rank |
| one-step boundary | only zero and rank-one histories; separate `s=0` branch | trivial-stabilizer odd targets and nontrivial stabilizers checked explicitly | hostile-gate minor repair incorporated, not hidden by convention |
| phase/fibre recovery | injectivity of `2^(2^d)` and strict increase of `(2^s-1)` at fixed `(d,b)` | realized stabilizer values grouped by target size and checked for unique, ordered inverse mass | inverse-statistical consequence of the target polynomial |

## Boundary contract

- `d=0`: `V` has one point, only the zero translation exists, and every state
  is unchanged.
- `t=0`: `F_0(B;z)=z^|B|`; the only source is the target itself.
- `B=V`: `F_t(V;z)=2^(dt) z^(2^d)`; the full set is fixed.
- `B=empty`: the general formula remains literal and counts sources missing at
  least one point from every relevant coset.
- `s=0`: `F_1(B;1)=1`; no half-integer exponent is evaluated.
- `s>=1`: `B` is a union of two-point orbits, so `|B|` is even and the second
  branch is integral.
- The sharp clock is worst-source equality, not a common exact absorption time
  for all non-full sources.

## Evidence limits

The verifier is finite counterexample pressure, not a proof.  The source
search is bounded and does not establish novelty, priority, or freedom to
publish.  P109/P115 subtract generic deterministic finite-linear mechanisms;
P158 uses graph-cut signatures and occupancy/surjection fibres rather than
translation subspaces, affine cosets, and target stabilizers.  A future direct
owner would require reopening the claim boundary.
