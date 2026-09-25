# DRR01 — divisor-driven two-sweep rational relaxation

ID: ANG-20260923-DRR01. Paper437. Version1, session2026-09-23.
Batch NONHOMOGENEOUS-FEEDBACK-20260923-R, round3/5. Initial result OPEN.
Full X=R3 with ORIGINAL coordinates(u,v,w), ordinary Lebesgue du dv dw.
Every source point is legal; all signed axes, units, integer faces/null points
and unbounded states remain. w is a SOURCE coordinate, not physical height.

## Frozen main and two control owners

n=flooru,m=floorv, gcd(0,0)=0, d=max(1,gcd(|n|,|m|)). Read d once from
the ORIGINAL state for this complete step; next state recomputes it.
MAIN: U=(u+d v^2)/(1+v^2), V=(v+d U^2)/(1+U^2),
W=w+d(u^2-v^2), with updated U in the second sweep.
D content-OFF: identical formulas but constant d=1, no gcd admission or
formal extra branch labels. N denominator-OFF: U=u+d v^2,V=v+d U^2,
W=w+d(u^2-v^2), with original current-source d and its own next readout.
All three have their OWN total source, actual inverse/IMAGE, clock and G.
The denominator constant1 is one design constant, not a per-prime parameter.

At integer cells with1<m<n, proper divisibility m|n iff d=m. This SAME d
enters both actual nonhomogeneous geometric sweeps and the w drift; updated
U,V generate the next gcd. Lineage: divisor/prime-composite symbolic interface
-> current arithmetic-gated geometry -> geometry reselects arithmetic.
No independent integer seed, prime table, log-prime roof, zero or fitted input.
Readout/design/measure are declared choices; strong naturalness remains OPEN.

## Entire inverse and all-point clock

For MAIN target(U,V,W), enumerate EVERY integer d>=1:
v=(1+U^2)V-dU^2, u=(1+v^2)U-dv^2, w=W-d(u^2-v^2).
Keep iff reconstructed source has actual readout d and full forward equality.
D uses the same inverse with sole d=1 and no gcd guard.
N enumerates EVERY d>=1 with v=V-dU^2,u=U-dv^2,w=W-d(u^2-v^2),
checking its own reconstructed content and forward equality.
No index/depth cutoff; duplicate actual predecessors/triples are identified.
Prove inverse completeness and Borel domains rather than assuming bijectivity
of the assembled source map. No terminal is introduced by branch failure.

For every branch freeze the displayed fixed-d smooth inverse germ at ALL
actual points, including floor faces. J=|det_R3 Dtheta| is the FULL3D
Jacobian: retain all mixing blocks involving w. Do not differentiate floor,
claim a smooth assembled map, or borrow the base2D determinant without proof.
Derive positive finite J and every-Borel IMAGE mu(theta(E))=integral_E J dmu
on its actual inverse domain. No changed density or atomic weight.
kappa(x)=-log J_actual(Tx), S_0=0, S_j actual own clock sums.

## Full ledger and global discriminator

G={(z,r-s,y):T^r z=T^s y,r,s>=0}, source y,range z; equal triples
identified, integer lag retained. c=S_r(z)-S_s(y), forward arrow has -kappa.
Prove descent/additivity; retain all lag/clock/joint kernels, source/extension
isotropy, entire H_z=c(G_z^z), all incoming depths and every real phase.
Full X x R_h extension is (y,h)->(z,h+c); physical time translates h on
its set-level orbit space. No quotient regularity or chosen w-section.
Primitive means only the least positive generator of ENTIRE H, with positive
integer repeats. Equal clocks alone never merge distinct source packets.

Frozen GLOBAL test: alpha_t(u,v,w)=(u,v,w+t), EVERY real t. Prove or refute
that it preserves every actual readout/branch/measure/ownedclock and commutes
with the complete T for EACH owner, and whether (x,h)->(alpha_t x,h) is an
actual extension action. Source translation is not physical h translation.
For any actual positive-clock finite core, decide whether its translated
family yields distinct FULL source packets with the same wholeH; different
points alone are not proof of different packets. No quotient or w=0 selection.
429's global C1 diffeomorphism theorem may NOT be applied to a piecewise,
possibly many-to-one source; establish any required result here from definitions.
Separately classify the ENTIRE fixed sets for MAIN/D/N, with allincoming,
wholeH and phases. No higher-cycle census. Keep conditional symmetry reasoning
distinct from existence of actual positive cores.

Necessary benchmark: nonempty positive ledger, EVERY primitive log ordinary
prime, at most one packet per prime; all-prime coverage additional. Decisive
MAIN failure stops/forks; otherwise OPEN/FORK at this gate without repairs.
D/N are arithmetic/geometric ablations; free w is a declared multiplicity and
PROVES_TOO_MUCH risk, not an invitation to delete fibres or borrow a clock.

## Provenance and stages

Scout bilateral_transport_review FULLread430summary110,416card104 and
429card105, including outcomes. Two card hashes respectively:
71c175aa1b9ba202c81df16a486b77365c36e9cde9d1e879f586eb722326f4b0;
7e20089a8100181637d997bc9425e2420ad1eb5db0e2fc47c860b7858f1f077a.
Retained older author/shared history exists. Informal inverse/fixed-feasibility
algebra informed design; not blind/sealed preregistration or a proven result.
Helper direct_controls saw proposal messages only for domain/translation names,
no files/tools or mathematical derivation; not another reviewer seat.
No new sibling/peer report, scientific numerical run or external lookup read.
This is a definition distinction, not a novelty or nonconjugacy claim.
Root owns card/integration; author paper/README/claims; separate reviewer
CP1/card-only raw/final evidence. Raw freezes before author access, root FULLread
before DISTINCT PAPER UNLOCK. Final four-surface CP2/CP3 required.
Same-model shared-history AI review NOT_CALIBRATED, not human/external validation.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. Exactly435–439, no440. Markdown only,
no Git/PDF/publication/upload. Frozen scientific prefix is append-only.

## Outcome — original96-line scientific prefix preserved

Outcome: OWNED RATIONAL IMAGE CLOCK; COMPOSITE FIXED FAMILIES — STOP / FORK

The [paper](paper.md) proves full3D own inverse/IMAGE and each complete fixed
set. MAIN's (j,j,w),integerj>=1 have singleton fullincoming, ENTIRE
H=2log(1+j²)Z and composite-square primitives, already log4 atj1.
The direct actual-history translation argument gives continuum distinct
equal-primitive packets for any actual positive finite core, without429borrow.
D/N keep their own full ledgers; N has globalc0/H0, not deleted isotropy.
Same-object intact; STOP/FORK without selectingw0, quotient or clock repair.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. Internal review NOT_CALIBRATED.
[Claims](claim-ledger.md) · [Overview](README.md).
