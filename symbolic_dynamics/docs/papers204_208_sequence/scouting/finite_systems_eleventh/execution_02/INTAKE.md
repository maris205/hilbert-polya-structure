# Eleventh finite-systems lane: bounded intake

2026-09-06 UTC. Owner/proof contributor: `batch197_fosp_gate`.
Scope: this directory only. No paper ID, admission, reserve, independent
review, central-state/Git operation, or modification of the sealed tenth
lane is authorized by this intake.

This file is written before any eleventh-lane pilot code or execution.
The parent requested six fresh literals across at least three carriers,
but expressly permitted fewer executed rules when remaining proposals are
duplicates. The six-rule desk slate below spans four carriers. Four desk
rules are excluded before execution. Only WZS and ACP enter the fixed
full-box pilot; this is **two executed literals**, not six. Their two
carriers do not satisfy a fictitious claim of three executed carriers.

## Six-rule desk slate and historical deductions

1. HEP, simple labelled graphs: new edge `{u,v}` exactly when the old
   graph has a spanning Hamiltonian path with endpoints `u,v`. This is
   exactly the Hamiltonian path graph of Chartrand--Kapoor--Nordhaus
   (1983), DOI `10.1002/jgt.3190070406`. Primary indexed publisher abstract
   states the literal; direct body access failed. **DESK_EXCLUDE_DIRECT**.
2. WZS, subsets of a binary vector space: the signed Walsh-zero feedback
   defined below. Classical Walsh inversion, Boolean correlation immunity,
   sign transforms, and earlier P125/P177 Fourier calculations receive
   zero credit. No exact historical literal located in the bounded search;
   this is not an absence/novelty theorem. **PILOT_ONLY**.
3. ACP, monic polynomials of fixed degree over a prime field: the anchored
   critical-value feedback defined below. The classical critical-value/
   Lyashko--Looijenga map and resultant/characteristic-polynomial adapter
   receive zero credit. Old CRS extracts finite-field derivative roots,
   a different carrier/map already rejected for its elementary descent.
   Any new dynamic claim must not be inferred from these static facts.
   **PILOT_ONLY**.
4. BPF, bounded nonnegative voting-weight vectors: for `n>=1`, carrier
   `{0,...,2^(n-1)}^n`; put `W=sum w_i`, and let new coordinate `i` count
   subsets `S` of the other voters satisfying `2 sum_(j in S) w_j <= W`
   and `2(sum_(j in S) w_j+w_i)>W`. All-zero weights map to zero.
   This is raw Banzhaf swing reweighting. Normalizing any nonzero weight
   vector by its sum intertwines the literal with Arnell et al.'s
   strict-half Banzhaf reweighting (arXiv:2010.08672, Introduction).
   Scaling changes no strict-half coalition and raw counts differ from
   normalized Banzhaf indices only by their common sum. Zero is a trivial
   adjoined fixed state. **DESK_EXCLUDE_DIRECT_FACTOR**, no pilot.
5. GFC, labelled graphs: complement the lexicographically greedy spanning
   forest in the complete graph. This was already proposed in the eighth
   desk; greedy-basis external activity/Boolean intervals and earlier GCM
   are the occupied mechanism. **DESK_EXCLUDE_HISTORICAL**, no pilot.
6. CRS, subsets of `F_p`: replace `S` by roots in `F_p` of the derivative
   of `prod_(a in S)(X-a)`. This is the identical fourth graph/geometry
   rule, including the derivative-zero convention. **DESK_EXCLUDE_DIRECT**,
   no repeat pilot.

## Frozen executable literal WZS

For integer `d>=0`, let `V=F_2^d` with its standard coordinate dot
product. A state is a subset `S` of `V`, equivalently the Boolean indicator
`f_S`. Define the integer signed Walsh transform

`W_S(xi)=sum_(x in V) (-1)^(1_S(x)+xi dot x)`.

The next state is exactly `{xi in V : W_S(xi)=0}`. The output is a subset
of the same labelled vector space; no translation, orbit quotient, rank,
threshold, or normalization is applied. At `d=0` the two singleton-space
Boolean functions both have nonzero Walsh value and map to the empty set.

Frozen full boxes: `d=0,1,2,3,4`, every `2^(2^d)` subset.
Use exact integer arithmetic and independently compare butterfly output
with a direct character sum for all states through `d=3` and the full
`d=4` box as well. Record all-cycle census, transient height, image size,
complete target-fibre histogram and explicit longest-cycle/height/max-fibre
witnesses. Candidate directions only: parity forcing, signed spectral
support geometry, zero-pattern inverse constraints. No all-d theorem is
preasserted. Complement symmetry of source indicators is a deducted fact.

## Frozen executable literal ACP

For degree `r>=2` and prime `p>r`, carrier all monic degree-r polynomials
`f(X)=X^r+a_(r-1)X^(r-1)+...+a_0` over `F_p`. Let

`C_f(Y)=r^(-r) Res_X(f'(X),Y-f(X))`

and define `T(f)(Y)=(Y-f(0))*C_f(Y)`. The critical points are counted
with algebraic multiplicity over an algebraic closure. Since `p>r`,
`f'` has degree `r-1` and leading coefficient `r`, and `C_f` is monic
degree `r-1`; hence the map preserves the literal degree-r carrier.
No assumption that critical points or values split over `F_p` is made.
The anchor is the actual value at 0, not a padded arbitrary root.

Frozen full boxes `(r,p)=(2,3),(2,5),(2,7),(2,11),(3,5),(3,7),(4,5)`.
Every `p^r` coefficient vector is included. A quotient-algebra
characteristic polynomial implements the literal critical-value resultant;
the `r=2` direct formula is independently checked for every state:
`T(a,b)=(a*a/4-2*b, b*b-a*a*b/4)` in coefficient order `(a,b)`.
Record the same complete finite census as WZS. Potential proof directions:
weighted homogeneous factors, anchor-root inverse branching, and a genuine
all-parameter recurrence classification. No such classification is assumed.

## Stop and evidence rules

These are the original small full boxes. Do not add a box, increase a
cutoff, sample a larger carrier, or change a map to rescue weak evidence.
Any implementation or guessed identity failure is retained with an explicit
correction and a fresh immutable execution. Each pilot is run twice from
separate fresh input-frozen directories; the actual child exit, stderr,
complete stdout, before/after input pins, and raw `cmp` result are recorded.
Finite output is author evidence, not a proof or nonauthor review.
The novelty-check skill's dedicated external Codex reviewer is unavailable
in the active tool list; no Phase C PASS is claimed. The project-approved
separate gate can occur only on a completed proof package. HOLD_EXTERNAL.
