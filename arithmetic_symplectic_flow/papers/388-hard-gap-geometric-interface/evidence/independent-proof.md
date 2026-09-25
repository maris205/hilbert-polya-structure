# Independent definition audit — hard-gap/geometric interface, NOT a physical theorem

Screen `ANG-SCREEN-20260922-HGI01`; batch `GEOMETRIC-RETURN-20260922-H`, round 4/5.
Sole scientific input: clarified `candidate-card.md`, full 59 lines, SHA256 `d3a25f5853d867e4d28cb8852a7d3f9602f226e154e8643e32ee6c808b131c06`.
Original lines 1–51 retain SHA256 `56dd6b3e38d798dd1f401a15285535cbd84966c7967381c4f5b16ce5641b074e`; lines 52–59 fix source-arrow identification before mathematics.
Root reported reading CP1 and explicitly released this card-only audit after that clarification was verified. No manuscript, peer/scout, 357 text or other new package was read.
ARS/stream instructions are retained. Internal shared-history, inherited-model, **NOT_CALIBRATED**, not blind or external peer review.
No network, numerical experiment, delegation, Git, PDF or new candidate; only this raw evidence is written. This report does not define a physical flow or clock.

## 1. Common partial-map source convention, including terminals

For a partial deterministic map F, F^0 is the identity on the entire carrier, including terminals.
A history of length n is legal exactly when all n steps are defined; reaching a terminal permits no further positive step.
Use the clarified actual triples G_F={(z,m−n,w):F^m z=F^n w with both histories legal}, source w and range z.
Equal triples are one arrow even when several pairs (m,n) witness them. No free-path or germ labels are added.
Inversion exchanges m,n and endpoints. To compose witnesses through w, compare the two iteration lengths at w.
If the second is larger, extend the first meeting along that existing longer w-history; if the first is larger, extend the second instead.
This gives a legal common meeting and adds their lags, without extending any path past a terminal. Associativity follows from endpoint composition and integer addition.
All (z,0,z) are units, including terminal units. The integer-lag homomorphism is a SOURCE bookkeeping field, not elapsed time.
These are Borel source groupoids here: each partial map/iterate is Borel and the witnessing equality sets form a countable union.
Below S is written in the same meeting-lag convention: (sigma^{-k}x,k,x). If shift-action arrows instead use (sigma^j x,j,x), then j=−k.
This sign change of label convention does not alter any stabilizer subgroup and introduces no clock.

## 2. D HARD-OFF: complete inverse and terminal ledger

The carrier is the entire closed cone C=[0,∞)^2; E is defined exactly when both coordinates are positive.
For a>=b>0, E(a,b)=(a−b,b); for b>a>0, E(a,b)=(a,b−a). The equality case belongs only to the first branch.
If E(a,b)=(u,v) through the first branch, then (a,b)=(u+v,v) with u>=0,v>0.
If it occurs through the second, then (a,b)=(u,u+v) with u>0,v>0; the strict condition v>0 records b>a.
Conversely those conditions place the proposed L/R images in the correct positive forward branch and give the required target.
Thus L(u,v)=(u+v,v), domain u>=0,v>0, and R(u,v)=(u,u+v), domain u>0,v>0, are the entire inverse atlas.
At an interior target both predecessors exist and are distinct. At (0,v), v>0, only L exists and gives (v,v).
At (u,0), u>0, and at (0,0), no predecessor exists. All of these axis/origin targets are nevertheless forward terminals with identity arrows.
In particular a forward terminal need not be an incoming-isolated point: the positive vertical axis has a genuine incoming tree.
L maps onto the first forward region a>=b>0; R maps onto b>a>0. They do not double-count the diagonal.
No missing branch is supplied at the equality boundary. E is Borel; no continuity across that boundary or étale structure is needed for the source audit.

All inverse histories are obtained by successive legal L/R choices. Starting at an interior target every finite L/R word is legal.
Starting at a positive vertical terminal, the first reverse step must be L, after which the point is interior and both choices are available.
Starting at a horizontal terminal or the origin, the only reverse history is the empty one.
For any target z, every incoming triple is obtained by choosing m legal forward steps to r=E^m z and any legal inverse word of length n from r to w.
The resulting arrow is (z,m−n,w); this recipe includes all witnesses and then identifies equal triples as required, rather than treating words as extra labels.

## 3. D source returns, all forward lifetimes and lag kernel

For any interior q=(a,b), let s(q)=a+b. Then s(Eq)=max(a,b)<s(q).
Hence E^m q=E^n q with legal histories forces m=n; if m>n the strictly decreasing segment between n and m is a contradiction.
There is no positive-iterate return anywhere, and the entire source isotropy is the unit group at every point.
Terminals are not fixed points of E: E is undefined there. Their identity arrows do not change that fact.
Two arrows with the same endpoints must have the same lag, since their quotient would otherwise yield nontrivial source isotropy.
The lag-zero kernel is nevertheless generally larger than the units: it is exactly {(z,0,w):E^m z=E^m w for some common legal m}.
For any interior r, distinct Lr and Rr have the same one-step image, giving a nonunit lag-zero arrow (Lr,0,Rr).
This is a source-lag kernel, not a physical extension kernel or clock kernel.

Forward lifetimes can also be classified without a truncation of C. If a,b>0 and a/b is rational, write (a,b)=d(p,q), d>0, p,q positive coprime integers.
Each subtraction preserves the integer gcd and strictly decreases p+q; consequently it reaches an axis in finitely many steps.
Only equality can create a zero coordinate, and its frozen first-branch rule gives (0,d), not (d,0).
Conversely, a finite history to a positive vertical terminal reverses through the integral maps L,R, which preserve the gcd of the integer coefficient pair.
It therefore starts at d(p,q) for positive coprime p,q. An interior irrational-ratio state never reaches an axis and has all finite forward histories.
No interior state reaches the origin or the positive horizontal axis. Already terminal points have lifetime zero.
For each distinct real d>0, the COMPLETE basin/source orbit of (0,d) is

    B_d = {(0,d)} ∪ {d(p,q):p,q∈Z_{>0}, gcd(p,q)=1}.

The equivalence with this source orbit follows by eventual meeting at the same terminal; a meeting with its terminal cannot run forward from that terminal.
Distinct d are not normalized or combined. The origin and every positive horizontal-axis point each form a singleton source orbit.
Write ell(q) for the finite number of steps to (0,d) on B_d. The unique source lag from w to z in that basin is ell(z)−ell(w).
Infinite-history irrational states have the full orbit/incoming description of §2; they cannot meet a finite-lifetime orbit.
No additional limiting point, scale section, compactification or asymptotic physical time is asserted for them.

## 4. S GEOMETRY-OFF: full bilateral symbolic source

Let Gamma(x) collect the gaps between consecutive occupied sites. The condition is that any two distinct values are proper-divisor incomparable.
A violation has two gap occurrences witnessed on a finite interval; thus X_gap is closed in {0,1}^Z. All finite and infinite supports remain.
Translation of occupied sites preserves Gamma, so sigma is a bijection of X_gap with actual inverse sigma^{-1}; neither map has terminals.
Every integer iterate is legal. Its complete source arrows in the common convention are (sigma^{-k}x,k,x), k∈Z.
Thus every incoming source at z is sigma^k z with its retained lag k; no periodic lag is identified with the identity merely because its endpoints agree.
Source isotropy is {k∈Z:sigma^k x=x}. It is pZ if x is globally periodic with least positive period p, and {0} otherwise.
Indeed any nonzero element yields a positive period, whose smallest value divides every other period by the integer division algorithm.
Allzero and allone are admissible and have source isotropy Z; alternating (10)^Z and its shifted phase are admissible and have isotropy 2Z.
A nonempty finite support cannot be invariant under a nonzero translation, so it has trivial source isotropy; the empty support is the allzero exception.
One-sided or eventual periodicity without global bilateral periodicity does not produce nonzero isotropy. Those points are not deleted.
For completeness, a nonzero periodic configuration is admissible exactly when the distinct values in its cyclic gap list satisfy the same divisibility condition.
Remove repetitions of that cyclic gap word; the sum of the least repeated block is the least positive BIT-shift period.
To see this, every return translation must take a 1 to a 1 and preserve the subsequent ordered gaps; conversely repetition of the gap block supplies precisely that translation.
The allzero configuration is separate with least shift period 1. These are integer source periods, not physical orbit lengths or a chosen clock.
The lag-zero kernel of this actual invertible shift action consists only of units. Full shift orbits, points and nonzero stabilizing lags remain.

## 5. P PASSIVE-PRODUCT: exact combined histories, not independent lags

The full carrier is X_gap×C. On q interior, P(x,q)=(sigma x,Eq); every axis fibre is terminal, including fibres over the origin.
P^n(x,q)=(sigma^n x,E^n q) exactly when the n geometric steps are legal. Symbolic evolution does not continue separately after geometric termination.
Its full immediate predecessors of (y,r) are (sigma^{-1}y,Lr) on D_L and (sigma^{-1}y,Rr) on D_R.
This follows from uniqueness of the shift inverse and the complete geometric atlas. Interior, vertical, horizontal and origin cases are exactly those of §2, for EVERY y.
After an inverse word of length n the symbolic coordinate is sigma^{-n}y; all geometric words and their actual domains are retained.

The precise source-arrow characterization is

    ((x,q),k,(y,r)) ∈ G_P
    iff (q,k,r) ∈ G_D and x=sigma^{-k}y.

For necessity use k=m−n in P^m(x,q)=P^n(y,r). Conversely any legal geometric witnessing pair m,n satisfies the symbolic equality under the displayed constraint.
This is a common-lag condition, not the unrestricted Cartesian product of two source groupoids with independently chosen lags.
For every target, the forward-segment/reverse-word construction of §2, with the corresponding sigma powers, gives all incoming triples and no extra arrows.
Geometric strict descent excludes every positive-iterate P return. The geometric part of an isotropy arrow forces k=0, so every P source stabilizer is trivial.
The source lag-zero kernel is exactly {((x,q),0,(x,r)):E^m q=E^m r for some legal common m}; it can contain nonunit arrows.
No nonzero symbolic stabilizer creates a P loop: a globally periodic symbol is insufficient to overcome the actual geometric requirement.

Each P source orbit projects bijectively onto its geometric D orbit: for any geometric endpoint r the unique geometric lag fixes the required symbolic shift.
Existence follows from §2; uniqueness uses the absence of nonzero D isotropy. Different symbol states over the same geometric point do not merge.
In a finite-lifetime geometric basin, the terminal symbolic value is xi=sigma^{ell(q)}x.
The COMPLETE P basin/source orbit of (xi,(0,d)) is therefore

    { (sigma^{-ell(q)}xi,q) : q∈B_d }.

Every (x,(u,0)), u>=0, is an incoming-isolated terminal singleton; vertical terminal fibres instead have the preceding full basins, one for each xi.
For irrational geometric histories the common-lag formula still gives the whole source orbit, without choosing a new normalization or omitting any symbolic state.
Allzero and allone symbols stay constant along the joint steps but do not produce P returns. Alternating symbols change phase with the parity of the geometric step count.
Their inverse histories keep that parity information; both alternating phases, all finite supports and all other infinite supports remain in the full product.

## 6. What this screen does and does not define

D, S and P are fully specified comparison MODULES for this source-level audit. Their elementary source results do not provide the desired coupled geometric realization.
P advances both coordinates at the same step, but its geometric branch domains never read symbols and its symbolic update never reads geometry.
It therefore supplies no rule by which divisor-incompatible gap histories become geometrically inaccessible; the symbol admissibility is imposed in its separate factor.
The desired owner still lacks an exact coupled carrier, actual symbol-sensitive geometric transition law, complete coupled inverse domains and boundary behaviour.
It also lacks a probability/IMAGE construction or other stated clock law, a physical extension/flow, and a same-object physical packet/repetition convention.
These are missing interface data, not false theorem statements and not tasks to fill by inserting a convenient roof during this screen.
For ALL THREE modules, physical H, extension kernel, physical flow/periods, measure-IMAGE and T3 remain **NOT DEFINED**.
In particular trivial D/P source isotropy and integer S periods are not reported as H={0}, positive physical times or a unit-roof suspension.
The monotone function a+b is used solely to prove an elementary source-return statement, not promoted into a roof or elapsed time.
No probability or physical primitive-packet multiplicity is inferred from counting source branches or shift periods.

The frozen card records a finite design collision with 357's Euclidean/cotangent direction. Without reading 357 this report does not independently certify conjugacy or historical proof identity.
Nothing here borrows its clock, geometry, result or authorization. The card expressly distinguishes design overlap from equality of complete objects.
The warranted disposition is **STOP BEFORE P0 / definition interface incomplete** for the desired coupled realization, while preserving the module audits above.
This is not a no-go theorem for all coupled realizations, all geometric carriers or all future clocks, and supplies no formal Route credit.
One useful next architecture question is: what explicit geometric branch-domain rule could read the full hard-gap divisibility constraint, with an exact inverse atlas on its entire carrier?
That question is not answered by adding a rule here; a proposed answer needs a fresh exact card and a separately authorized round after this batch.
Classical A0/A1/A2 NOT APPLICABLE; broadened T0 completeness screen only; physical T1/T2 NOT DEFINED; formal UNASSIGNED; Route B NOT INVOKED.

EOF — independent DEFINITION AUDIT, not a physical theorem; complete module source ledgers; physical H NOT DEFINED; raw frozen pending separate PAPER UNLOCK.
