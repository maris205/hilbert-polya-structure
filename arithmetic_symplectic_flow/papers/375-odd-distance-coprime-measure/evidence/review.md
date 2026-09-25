# 375 — Manuscript comparison and final adverse review

Candidate: `ANG-20260922-ODC01`; batch `HARD-NONLOCAL-20260922-F`, round 1/5.
Review verdict: **CP2 PASS after one closed precision correction; CP3 PASS, bounded scope.**
Candidate status: **EXACT MEASURED SOURCE; STRICTLY POSITIVE IMAGE FAIL; CLOCK NOT DEFINED; STOP.**
The review pass accepts the scoped negative result; it is not a candidate-promotion pass.

## 1. Inputs, complete access and chronology

All paths below belong to this package; hashes are SHA-256, measured from current bytes.

- paper.md — 229 lines, read 1–120 and 121–229 through EOF; `743a825dc40fdd615eeb066018d3fb389305d863802c3e8e9c9bd91ddc10eb7b`.
- candidate-card.md — 136 lines, read 1–136 through EOF; `bac6d157476742176da3db7594bbffb28483c154565dd0fb5e5ca19131f2c6ae`.
- claim-ledger.md — 54 lines, read 1–54 through EOF; `3330154577f8836916d478dc67cc126934d997f622716fba7190d7bbc2524a87`.
- README.md — 83 lines, read 1–83 through EOF; `6c62ae5e33a6a70f924db030423684bc16ccbc18bf2c21304482c18126340572`.
- scope-review.md — frozen 76 lines; `35c02c3e840c1b305951bd2b1a0f73da25890c9049bb8e5db5f5fc0d4fd773a7`.
- independent-proof.md — frozen 195 lines; `401fb8415463765abc62e057f940cb7319c4532be5711d1beca9e2fb2d82b54c`.
- Original candidate-card.md prefix — 88 lines, independently rehashed; `e7e4fa21a66ebd823d391720731a1448867f6d488dfe4399755979621d0fa149`.

CP1 read the entire original 88-line card before mathematics and returned entry-scope PASS.
After explicit release, my independent main/control derivation used only that original card.
The 195-line raw proof was frozen and parent-reported fully read before separate PAPER UNLOCK.
Only afterward did I read the initial 229-line manuscript fully, through EOF:
paper.md initial reviewed SHA `f085fef8852922228545b69ebd3154da85cde6a4dc513bb0f66fd7fbbb4b5469`.
At that point the support surfaces were incomplete; I explicitly withheld CP3 completion.
I reported the one correction below, then read all four final surfaces fully after READY.
The card outcome was read only in this authorized final stage, never used as raw input.
Both frozen evidence files and the original card prefix remain byte-identical.
No author-helper report, other candidate proof, peer proof or external scientific source was read.
The paper discloses an author-side helper; that is author provenance, not a review seat I used.
I claim no ordering of private author derivations beyond these actual accesses and messages.

## 2. The one correction and its disposition

Initial Proposition 1 said that the one-sided shift “swaps the two parity sets”.
Taken literally for actual symbol sets this fails: for x=(4,3,2,3,...),
the old even set is {4,2}, but the odd set of Tx is only {2}.
Deletion can lose the unique initial symbol; this does not invalidate shift admissibility.
I requested the precise statement that shifting preserves odd differences among retained coordinates.
The author accepted it; final paper line 40 now uses exactly that argument.
Replacing that phrase by the original phrase in a read-only stream reconstructs the initial hash above.
Thus this is the only manuscript byte change between my initial and final versions.
Disposition: **CLOSED, minor proof-language precision; no definition, theorem or decision changed.**
There is no remaining required manuscript amendment in the reviewed scope.

## 3. CP2 — Complete source and actual inverses

The odd-distance constraint is exactly cross-coprimality between all even and odd coordinates.
Its violations are cylinder-open, hence X is closed and Borel in the full countable product.
T is a continuous total self-map; y_1y is a legal preimage of every y, so T is onto.
Every inverse is exactly I_a on E_a, with gcd(a,y_(2j))=1 for every j.
Insertion is a homeomorphism from its entire closed domain onto the clopen cylinder [a] in X.
These domains need not be open. I checked the manuscript's general witness separately:
b=a+1, c=a(a+1)+1, and a prime divisor r of a give (b,c)^infinity in E_a;
changing a remote even letter b to r stays in X but leaves E_a, because gcd(r,c)=1.
Thus the manuscript does not infer etaleness or discard exceptional infinite histories.
Finite-prefix permission (1) correctly tests internal pairs and all odd-separated cross-tail pairs.

Common-tail padding proves closure of actual retained-lag triples under composition.
All incoming states are exactly legal uT^n x; equal triples, not witnesses, identify arrows.
The lag kernel is equal-iterate tail equivalence, not the unit relation in MAIN.
Full source isotropy is dZ at every eventually least-d history and zero otherwise.
Odd source periods are impossible; even words require all cross-parity pairs to be coprime.
Primitive source necklaces are identified by cyclic rotation only, with all legal ancestors retained.
In particular a null prefix-4 ancestor of the alternating 23 tail still has source isotropy 2Z.
No source periodicity is converted into a physical period after failed clock admission.

## 4. CP2 — Measure, every-Borel IMAGE and decisive gate

Finite nonempty set codes enumerate the positive integers, giving a finite total weight bound.
The allowed pairs have positive total weight B; an excluded pair also proves B<1.
Each alternating product law is supported on X; swapping the ordered component labels proves stationarity.
Every legal finite cylinder receives positive weight, including cylinders extending unbounded histories.
Mixing labels are not source coordinates, and almost-sure finite alphabets do not shrink X.
Only singleton/singleton components yield point atoms: alternating coprime pairs with the stated weights.
All other components have vanishing singleton masses; atomic mass is strictly between zero and one.
The manuscript also justifies that any Borel atom must be a singleton atom by nested coordinate cells.

I checked both restricted-cylinder sums (3)–(4), including parity counts and the swapped-label numerator.
At every legal point the denominators are positive; the numerator is a nonempty legal prefix cylinder.
For every Borel D subset E_a, equation (5) is the actual insertion law:
mu(I_a D)=sum w_(S,U) 1_(a in U)/|U| times nu_(S,U)(D), bounded above by mu(D).
This proves ordinary absolute continuity and nonnegative IMAGE densities, not strict positivity.
It is an every-Borel calculation, not an extrapolation from the tested cylinders alone.

At y=(3,2)^infinity, mu{y}=mu{I_2y}=1/(8B), while mu{I_4y}=0.
Restricted cylinders decrease to the singleton and their images decrease to its actual image.
Finite-measure continuity therefore gives the prescribed limits j_2(y)=1 and j_4(y)=0.
The singleton IMAGE identity forces zero for any density version at this positive-mass atom.
Both alternating phases and all legal predecessors are tested without assigning values to illegal branches.
MAIN fails the frozen strictly-positive admission intrinsically; it does not fail ordinary absolute continuity.
Its kappa, additive cocycle, clock kernel/intersection, extension/isotropy, physical H, packets and times
are **NOT DEFINED**, not zero, infinite, or supplied by a separate control.
Convergence at all other legal tails is not established or needed after this decisive gate.

## 5. CP2 — The three own controls

**FIXED-TWO.** On its entire two-point carrier, only the two alternating closing insertions are legal.
Both masses are 1/2, every legal finite IMAGE equals one, and c=0 descends on the whole lag groupoid.
The clock kernel is the entire groupoid; the lag kernel and their intersection are units.
Source and extension isotropy are 2Z; the complete orbit set at varying height is R, with H={0}.
All incoming states are the two phases. No positive physical period follows from source period two.

**ARITHMETIC-OFF.** The telescoping marginal rho(a)=1/[a(a-1)] defines its own full-support nonatomic law.
Every prefix is legal and has its positive product density at every point and on every Borel set.
For prefixes u,v on a common tail, W(u)=product u_i(u_i-1) gives c=log[W(u)/W(v)].
Padding and composition cancel actual common-tail factors; the sign matches the declared insertion clock.
The clock kernel is equality of W; the lag kernel is equality of lengths; their intersection requires both.
Prefixes 4 versus 23 show a nonzero-lag clock-kernel arrow; 23 versus 32 show nonunit intersection arrows.
All incoming prefixes remain. Eventual primitive words have source isotropy dZ, time group L(w)Z,
L(w)=sum log[w_i(w_i-1)]>0, and trivial extension isotropy; non-eventual histories have H={0}.
For a connecting arrow to a reference source, h+c modulo H records all height phases.
One packet per primitive necklace, all repetitions, and the constant-3 primitive log 6 are correctly owned here.

**DROP-SINGLETONS.** The separately normalized restricted mixture is stationary and nonatomic on the same X.
Enlarging finite parity alphabets by suitable integers congruent to one proves full support and positive
restricted denominators without discarding any tail or importing MAIN's density.
Its precommitted entire Borel empirical set D has mass 2^-15/B_*>0 and lies in E_7.
The square-subsequence variance argument plus interpolation proves the needed frequency-one assertion.
Its full prefix-7 image has mass zero: a contributing even alphabet would contain 7 yet be contained in {2,4}.
The manuscript's bound (11), including its factor 1/3, forces the prescribed ratio to zero at every y in D.
Any strictly positive Borel density would have positive integral on D, contradicting the full-image identity.
This atomless positive-set obstruction rules out an atomic-only diagnosis; nonnegative IMAGE still exists.
The source ledger survives unchanged; its clock-dependent fields are NOT DEFINED, as in MAIN.

## 6. Stage distinctions and CP3 strongest-case challenge

Raw already proved the main and three-control conclusions, complete source ledger and admitted-control clocks.
Manuscript-stage checks additionally covered its general nonopen-domain construction, B<1 argument,
Borel-atom justification, explicit positivity of every finite numerator, and the sharper DROP bound with 1/3.
These are not retroactively labelled independently submitted raw claims.
The raw's extra orbit-mass formulas and explicit nonnegative-version construction need not be inserted into the paper.

The strongest positive case is real: the full hard arithmetic source has a stationary full-support law,
an exact source ledger, and every legal branch admits a nonnegative every-Borel density.
Neither those facts nor positivity of every finite cylinder ratio implies the required positive limiting density.
A removable null-point/version objection fails at MAIN's positive atom and DROP's positive atomless set.
Deleting branches or tails, keeping mixing labels, changing the measure, or weakening the clock rule changes the contract.
This proves no universal obstruction to every other law or hard nonlocal source; strong naturalness remains OPEN.

All final surface claims match the checked paper: one candidate, separate controls, unchanged original definition,
SOURCE established but no MAIN/DROP physical owner, T3 NOT AUDITED, classical A0/A1/A2 NOT APPLICABLE,
formal coordinates UNASSIGNED and Route B NOT INVOKED. STOP/FORK carries no transferred theorem credit.
The original card's OPEN header is a historical freeze, explicitly followed by the dated outcome; no contradiction is hidden.
The final report links, rather than stale pending claims, govern CP2/CP3; root owns package navigation QA.

ARS router and retained workflow/DA/runtime/evidence instructions governed the three checkpoints and adverse tests.
No auxiliary reviewer, network lookup, scientific numerical run, Git action or other-file write was used here.
The model and broad shared history are inherited; author expectations were disclosed before raw derivation.
This is internal, non-blind, single-family **NOT_CALIBRATED** review, not external peer review or independent-error evidence.
No venue was bound, no numerical score or forced issue quota was used, and no novelty/venue-readiness verdict is issued.
Final disposition: **bounded CP2/CP3 PASS; one precision correction closed; no unresolved required scientific amendment.**
Only this report was written; the frozen scope and raw records remain unchanged.
