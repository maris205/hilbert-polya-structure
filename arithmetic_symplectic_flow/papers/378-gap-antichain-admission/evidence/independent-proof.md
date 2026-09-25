# GAC01 — independent raw-card proof

Result: MAIN and ADJACENT-GAP-ONLY have complete probability sources, but their prefix-1 IMAGE is intrinsically NOT absolutely continuous with respect to its source measure.
Their prescribed clock and dependent physical fields are NOT DEFINED, not zero. Full source ledgers remain; INTERACTION-OFF and EVOLUTION-OFF have their own admitted clocks below.

## 1. Frozen input and access boundary

Sole scientific input: [candidate card](../candidate-card.md), original 85 lines plus pre-release clarification 86–92, all previously fully read at CP1.
Clarified 92-line SHA256, reverified after explicit release: `a29076fda9d37d4bc34ca977d4d24ad678f9d7eb89df2e77a904f09cda7a131b`.
Original 85-line SHA256: `e93aa865f18c54640f498a02a6b48824104de3e543f232005148a5c0c7f5ade8`.
The singleton notation is exactly y=1 0^infinity and z=11 0^infinity, NOT periodic repetition; (10)^infinity remains periodic.
No main manuscript, peer proof, scout result or other scientific document was read. No network, scientific numerical computation, auxiliary delegation or model change.
Retained stream/ARS instructions apply. Same-model shared-history internal derivation with prior CP1 access: NOT blind, NOT_CALIBRATED, not external peer review.
Only this proof is written; card and scope remain unchanged. Candidate ANG-20260922-GAC01, HARD-NONLOCAL-20260922-F, round 4/5.

## 2. Complete MAIN and adjacent-only sources

Write R(d,e) for d=e OR (d does not divide e AND e does not divide d), for positive integers d,e.
MAIN requires R between every pair of completed gaps; ADJ requires R only between successive entries in the ordered completed-gap list.
Using R on occurrences is equivalent to the card's MAIN condition on distinct values because R(d,d) always holds.
Let Y denote either separately instantiated full binary source. A violation has a finite prefix witness, so Y is closed in the compact binary product and has its full subspace Borel structure.
Every legal finite prefix extends by zeros forever; hence its source cylinder is nonempty. Both constants, leading zeros and every legal finite-one or unbounded-gap history are retained.
Shifting deletes no gap or only the first completed gap, and never adds an interaction. Both rules are preserved, so T is continuous and total on Y.
Prepending zero adds no completed gap, giving I_0:Y->[0] and proving T is onto. No gap at infinity is introduced for an eventual-zero path.
For MAIN, E_1 contains the no-1 tail; otherwise, if the first 1 of t is at r, it requires R(r+1,e) for EVERY old completed gap e.
For ADJ, the same new gap is compared only with the FIRST old completed gap, if that gap exists; with fewer than two old ones there is no such comparison.
These are the exact domains of I_1(t)=1t. Both E_1 are closed, as inverse images of Y under continuous insertion, and I_a:E_a->[a] is a homeomorphism onto its range.
T I_a=id on E_a and I_(x_0)T x=x for every x; every predecessor is exactly one of these legal insertions.

For EVERY finite binary word u, D_u={t in Y:ut in Y}; I_u(t)=ut, with empty word the identity and illegal u having empty domain.
An explicit domain test concatenates the completed-gap list of u, one cross-boundary gap if both u and t have a 1, and the list of t.
If |u|=m, its last 1 is at l, and t's first 1 is at r, that cross-boundary gap is m+r-l. If either 1 is absent there is no cross-boundary gap.
Apply the WHOLE MAIN pairwise rule or the own ADJ neighboring rule to this concatenated list. This covers all finite-one tails and all cross-boundary interactions.
Each D_u is closed and I_u is a Borel homeomorphism D_u->[u]. These are ALL finite inverse histories; coherent successive choices give all infinite histories without changing the source.
The domains need not be open. In particular E_1 intersect [10]={1 0^infinity}, whereas that point is not isolated in Y: a second 1 may be put arbitrarily far away in Y.
Thus E_1 is not open. Also [110]={11 0^infinity} is isolated in Y, while its shifted image is not; T is not a local homeomorphism there. No etale assertion is used.

The finite completed-gap list (2,3,4) is illegal for MAIN because 2 divides 4, but legal for ADJ because its two adjacent comparisons pass.
For example the finite binary prefix with ones at positions 0,2,5,9, followed by zeros forever, belongs to ADJ but not MAIN.
This is a finite-list comparison: periodic repetition of (2,3,4) would ALSO require the closing adjacent comparison (4,2), which fails.

## 3. Exact sequential probabilities, support and all atoms

For either source define o_Y(h) as the number of positions i<|h| where appending 1 to the earlier prefix h[0:i] is legal.
At each such position the actual allowed bit has probability 1/2; at any other position only 0 is legal and its probability is 1.
Therefore P_Y(h)=2^(-o_Y(h)) for every legal finite h, and P_Y(h)=0 for an illegal h. This is an exact formula for EVERY forced and optional bit, not a stationary law.
The two or one allowed child masses sum to the parent mass. Consistent binary-cylinder probabilities extend to a probability on the binary product.
Every illegal-prefix cylinder has mass zero, and their countable union is the complement of Y; the probability is carried by Y.
Every nonempty legal cylinder has positive mass, so support is the whole Y. No generated-typical subset replaces Y.
Nested cylinders give mu_Y({x})=lim_n 2^(-o_Y(x[0:n])); a point is an atom precisely when it has only finitely many optional positions.

Every actual 1 is optional because 0 is always legal. Thus infinitely many ones imply infinitely many optional positions and singleton mass zero.
With no completed gap, every later candidate 1 is legal; eventual-zero paths with zero or one 1 also have singleton mass zero.
Suppose a finite-one path has completed gaps but none equals 1. For MAIN let L be their lcm; arbitrarily large 1+kL are coprime to every old gap and therefore legal next gaps.
For ADJ use 1+kd with d the last completed gap. In either case a zero tail encounters infinitely many optional positions and has singleton mass zero.
If a completed gap is 1, MAIN forces every completed gap to be 1. In ADJ the same follows by propagation along the finite list, since R(1,e) iff e=1.
Consequently the complete atom set in BOTH owners is exactly
{0^r 1^k 0^infinity : r>=0, k>=2}, with mass 2^(-(r+k+1)).
Indeed the initial r+k bits and the first trailing zero are all optional; after that zero, every future candidate gap exceeds 1 and is forbidden, so ALL later zeros are forced.
Their total mass is (sum_(r>=0)2^-r)(sum_(k>=2)2^(-k-1))=2*(1/4)=1/2. The remaining measure has mass 1/2 and no atoms.
There are no additional non-singleton Borel atoms: the finite cylinder partitions would select nested full-atom-mass cells, whose intersection is one singleton of that mass.
The measures need not agree off these atoms: their distinct legal-prefix rules define distinct owners.

The prescribed test paths all belong to both sources. Exact optional/forced rules along their prefixes are as follows (O means optional, F forced zero).

- 0^infinity and 1^infinity: every bit is O, so their length-n cylinder masses are 2^-n and both singleton masses are zero.
- (10)^infinity: the first three bits through the first completed gap 2 are O; every later gap 2 uses F,O. Every prefix probability follows by counting these O positions.
- (100)^infinity: the first four bits through the first gap 3 are O; every later gap 3 uses F,O,O.
- (10100)^infinity: the first three bits are O; the next gap 3 uses F,O,O; subsequent gap 2 and gap 3 blocks use respectively F,O and F,O,O, in both owners.
- 1 0^infinity: EVERY position is O, so mu([1 0^n])=2^(-n-1) and the singleton mass is zero.
- 11 0^infinity: the first three positions are O and every later zero is F, so mu([11 0^n])=1/8 for n>=1 and the singleton mass is 1/8.

For the finite (2,3,4) test prefix above, ADJ has 3+2+3 optional choices and mass 2^-8; MAIN's last 1 is illegal and its mass is zero.
The formula o_Y covers every later extension, including any later forced/optional bit not encountered by these displayed paths.

## 4. Restricted-cylinder IMAGE and the intrinsic obstruction

Leading zero changes neither a completed gap nor a legal extension decision, so P_Y(0h)=P_Y(h)/2 for every finite h.
Cylinder agreement and finite-measure uniqueness give mu_Y(I_0 D)=mu_Y(D)/2 for EVERY Borel D subset Y.
Every cylinder denominator is positive by full support, and every I_0 prescribed ratio at EVERY point and level equals 1/2. Thus j_0=1/2 is an owned all-point version.

For I_1 define the finite measure nu_1(B)=mu_Y(I_1(E_1 intersect B)) on Y. If h has length N, insertion gives EXACTLY
I_1(E_1 intersect [h])=[1h], so the prescribed ratio is P_Y(1h)/mu_Y(E_1 intersect [h]), NOT P_Y(1h)/P_Y(h).
Take y=1 0^infinity. For N>=2, E_1 intersect C_N(y)={y}: any later 1 would create an old gap >1 incompatible with the newly inserted gap 1, in either owner.
The denominator is therefore zero, while the numerator is mu_Y({11 0^infinity})=1/8. These finite-level prescribed ratios are undefined, already violating admission.
More strongly, D={y} is Borel in E_1, mu_Y(D)=0 but nu_1(D)=1/8. Hence nu_1 is NOT absolutely continuous with respect to mu_Y restricted to E_1.
No nonnegative measurable Radon–Nikodym density, let alone a finite strictly positive full-point version, can satisfy every-Borel IMAGE: an integral over this null D is zero.
This is intrinsic IMAGE absolute-continuity failure for the frozen measured owner, not merely a bad prescribed limit or a removable null-set choice.

Strict positivity is a DIFFERENT direction. In fact nu_1 >= (1/2) mu_Y|E_1 for both owners, so no positive-source-measure subset of E_1 has zero IMAGE measure.
To prove it, whenever 1h is legal, removing the initial 1 preserves legality: L_Y(1v) subset L_Y(v) at each prefix v of h.
Thus P_Y(1h)/P_Y(h)=(1/2) product_(i<|h|)|L_Y(h[0:i])|/|L_Y(1h[0:i])| >=1/2.
If 1h is illegal then E_1 intersect [h] is empty. Otherwise nu_1([h])=P_Y(1h)>=(1/2)P_Y(h)>=(1/2)mu_Y(E_1 intersect [h]).
Summing on finite cylinder algebras and using monotone limits proves the measure inequality on all Borel sets. In particular mu_Y|E_1 << nu_1, while the reverse absolute continuity fails.
This lower inequality does not furnish a density in the missing direction and does not admit the clock.
Also T^-1{1 0^infinity} consists of its 0-prefix singleton of mass zero and its 1-prefix singleton of mass 1/8.
Therefore T_*mu_Y is not absolutely continuous with respect to mu_Y, and shift stationarity fails as well. Neither had been assumed.

## 5. The remaining prescribed inverse-1 tests, including the all-zero tail

For each owner, 1^infinity and 11 0^infinity belong to E_1. On every cylinder with first two bits 11, all gaps must remain 1, so E_1 imposes no further restriction.
Their ratios equal 1/2 for all N>=2, by the exact run probabilities above; hence the individually prescribed j_1 values there are 1/2.
The three listed periodic phases (10)^infinity, (100)^infinity and (10100)^infinity begin with 1 and have old gaps >1, so they are NOT in E_1.
Their prefix-1 insertions are illegal; no j_1 value is required there. This does not delete their other legal incoming phases or imply that they lack source isotropy.

For 0^infinity, every E_1-restricted cylinder denominator IS positive, but the prescribed ratios do not converge. The following exact argument handles the whole tail, not just a first finite prefix.
This is a supplementary check of a predeclared test point; neither intrinsic IMAGE failure nor the STOP decision depends on it, and no campaign over remaining legal-point limits is undertaken.
Given the generated prefix 1, the first completed gap e has probability 2^-e: before any completed gap every candidate 1 is optional, and a second 1 occurs almost surely.
For MAIN define b_d as the conditional probability that ALL subsequently completed gaps are R-compatible with d. For ADJ define b_d by compatibility of the FIRST such gap with d only.
These are probabilities within the already frozen law, not replacement measures. In MAIN b_d>=2^-d, because choosing first gap d then protects compatibility forever.
In ADJ b_d=sum_(e>=1,R(d,e))2^-e, so again b_d>=2^-d. In either case 0<b_d<=1.
Leading zeros do not change the subsequent sequential law. Splitting at the first 1, for N>=0 we therefore have the EXACT identities
mu_Y(E_1 intersect [0^N])=sum_(r>=N)2^(-r-1)b_(r+1)>0, and mu_Y([1 0^N])=2^(-N-1).
The ratio is R_N=1/B_N, where B_N=sum_(k>=0)2^-k b_(N+k+1), and B_N=b_(N+1)+(1/2)B_(N+1).

The sequence b_d does not converge in either owner. Let L_n=lcm(1,...,n), n>=3; it exceeds n since it is divisible by n(n-1).
Each e<=n is a proper divisor of L_n, hence incompatible; the first-gap law gives b_(L_n)<=2^-n ->0 for both owners.
For ADJ, any odd prime p is compatible with e=2, so b_p>=1/4. Infinitely many such primes exist by Euclid's elementary argument; no prime table or model input is used.
For MAIN we also have a uniform lower bound b_p>=1/8 for odd primes p, as follows.
Condition on first gap 2, an event of probability 1/4. Until the first completed gap incompatible with p or equal to p, the existing finite gap set remains compatible with p and excludes 1.
At each subsequent gap trial, candidate p is legal, with probability at least 2^-p of being chosen. Every incompatible candidate is a multiple of p larger than p.
The probability of choosing any such larger multiple in that trial is at most the probability of reaching p and rejecting it, which equals the probability of choosing p at that trial.
No next-gap trial is infinite with positive probability: for a finite gap set without 1, the infinitely many legal candidates 1+k lcm(S) provide infinitely many fair optional decisions.
Thus either p or an incompatible multiple is eventually chosen, with probability one (the per-trial p probability is at least 2^-p).
Summing the preceding success-versus-failure inequalities until that first choice gives probability at least 1/2 of choosing p first. Thereafter the MAIN rule enforces compatibility with p forever.
Multiplying by the initial first-gap-2 probability proves b_p>=1/8. This is an analytic stopping argument, not a finite numerical simulation.

If R_N had a finite positive limit, B_N would converge and b_(N+1)=B_N-(1/2)B_(N+1) would converge, contradicting the two subsequences.
R_N cannot tend to zero since B_N<=2; it cannot tend to infinity since then B_N->0 would force b_d->0, contradicting the prime lower bound.
Consequently no extended limit exists at 0^infinity for either owner. This additional chosen-version failure is distinct from the stronger intrinsic null-to-atom IMAGE obstruction already proved.
All prescribed tests have now been accounted for; no restricted denominator was replaced by an unrestricted cylinder mass.

## 6. Full retained-lag source ledger survives clock failure

For MAIN and ADJ retain G_Y={(z,k,y):T^m z=T^n y, m,n>=0, k=m-n}, with source y, range z and only equal triples identified.
This is a Borel groupoid: each fixed-witness equality is closed, the witnesses are countable, and composition/inverse use the declared endpoints and integer lag.
Every arrow has the legal common-tail representation (ut,|u|-|v|,vt), with t in D_u intersect D_v. Padding changes witnesses, not the actual triple.
The FULL lag kernel is {(ut,0,vt):|u|=|v| and both insertions legal}, including nonunit equal-lag replacements.
For every range point z, ALL incoming arrows are (z,m-|v|,v T^m z), with m>=0 and ANY legal prefix v for T^m z, modulo equality of triples only.
The entire source orbit is {u T^n z:n>=0, u legal for that tail}; this includes every admissible predecessor, not just a chosen periodic core.

A nonzero isotropy lag is exactly equality of two different shifts, hence eventual periodicity. A non-eventually-periodic point has trivial source isotropy.
If its eventual binary tail has least bit period L, the entire isotropy is LZ: every multiple is witnessed past the preperiod, and every tail period is a multiple of the least one.
The latter divisibility follows by reducing any tail period modulo L on a sufficiently shifted L-periodic tail; a nonzero remainder would contradict minimality.
Direct T^n x=x requires x ITSELF to be purely periodic with least period dividing n; arbitrary incoming prefixes need not themselves return.
In particular EVERY legal finite-one path has eventual-zero tail and source isotropy Z, although only the all-zero path among these is directly periodic.
All such legal finite-one paths lie in the source orbit of 0^infinity. The all-one tail also has least period 1, with precisely its legal predecessors retained by D_u.

Here is the exact periodic admission test. For a nonzero periodic binary word, list its cyclic distances d_1,...,d_r between successive ones, including the closing distance.
MAIN admits it exactly when all distinct cyclic gap values are divisibility-incomparable; ADJ admits it exactly when R(d_i,d_(i+1)) holds at EVERY cyclic adjacency, including the closing pair.
The all-zero word is handled separately and is admitted. Equal gaps and the gap-1 constant-one word are admitted in both sources.
Reduce the cyclic gap list to its primitive block before computing the binary period: if that block is e_1,...,e_s, the least bit period is L=e_1+...+e_s, not s.
Indeed repeating a gap block translates the one-set by its sum, while any binary period permutes consecutive ones and yields a repeating gap block; the two minimalities are equivalent.
Primitive binary necklaces with this admission, modulo rotations only, classify the eventual-periodic source orbits with all legal incoming prefixes. A repeated traversal has retained source lag jL.
For the listed periodic states the core least bit periods are respectively 1,1,2,3,5; the associated full eventual classes have source isotropy Z,Z,2Z,3Z,5Z.

MAIN and ADJ FAIL full clock admission. Thus kappa, A_m, the full real cocycle, clock kernel, its intersection with lag kernel, clock extension, extension isotropy, H and physical packets/phases/repetitions are NOT DEFINED for these proposed owners.
The source results and individually valid I_0 or special-point ratios do not define a patched physical action. They are not replaced by c=0, H={0} or a selected conull subsystem.

## 7. INTERACTION-OFF: its own full admitted Bernoulli owner

The source is the ENTIRE binary shift, with every inverse I_a defined on it and fair product probability mu_B([h])=2^(-|h|).
Consistency, full support and stationarity follow from summing the two children or the two predecessors; singleton masses are zero by shrinking cylinders.
For every Borel D, mu_B(I_a D)=mu_B(D)/2 by cylinder agreement; every restricted domain is now the whole source, and all point/level ratios equal 1/2.
For a word u the every-Borel history IMAGE is 2^(-|u|). On the full actual triples the owned clock is c(z,k,y)=k log 2, with descent and composition given by retained lag addition.
Its FULL clock kernel equals its FULL lag kernel {(ut,0,vt):|u|=|v|}; their intersection is this same kernel, not merely units.
All finite binary prefixes are legal, so Section 6's incoming parameterization applies with no deleted words. Extension incoming height to target (z,h) is h-k log 2 at the source.
Source isotropy is LZ at an eventual least-L binary tail and {0} otherwise; extension isotropy is trivial everywhere, while H=L log 2 Z or {0}, respectively.
For any source orbit O and chosen base b only as a proof coordinate, [(x,h)] maps to h+c(g:x->b) modulo H_b. Different connecting arrows differ by isotropy, proving the full phase set is R/H_b.
This is only a set with real translation, not an asserted quotient topology or invariant flow measure. All heights and all incoming histories remain.
Each primitive binary necklace of least length L gives one positive physical packet of least time L log 2; every non-eventual source orbit gives a free real line.
Distinct necklaces of the same length remain distinct packets. Their exact multiplicities N_L satisfy 2^L=sum_(d|L)d N_d, by decomposing length-L words by primitive period.
Equivalently N_L=(1/L)sum_(d|L)mobius(d)2^(L/d). The j-th repetition has source lag jL and physical time jL log 2, not a new primitive label.
In particular there are TWO primitive packets at log 2 (the constant necklaces 0 and 1), and the primitive 01 packet has least time 2 log 2=log 4.
This own control fails the target's multiplicity/time conditions without supplying a clock to MAIN. It retains all finite-one states as incoming members of the constant-zero eventual class.

## 8. EVOLUTION-OFF: unchanged measure, changed actual evolution

The carrier and probability are literally MAIN's whole X and mu, including the atomic mass 1/2 proved in Section 3, but the map is id_X and its unique inverse is id.
Its every-Borel IMAGE is exactly 1. Full support makes all its ordinary cylinder denominators positive, and its prescribed all-point version is 1 at every state, including null points.
The full actual groupoid is {(x,k,x):x in X,k in Z}; every integer lag survives although endpoints coincide. The clock is c=0 on ALL these arrows.
The FULL clock kernel is G, the FULL lag kernel is the units and their intersection is the units. At EVERY x source isotropy is Z and extension isotropy is Z.
Here H_x={0} everywhere. All incoming arrows to (x,h) have source (x,h), arbitrary retained k and zero height shift; no other base point is linked by id.
The complete extension orbit SET is X times R, and height translation is free on each line. There are no positive physical primitive packets or repetitions.
Every source point is fixed under the identity, with direct period 1 and all retained source repetitions; this does not create physical closed time or remove ineffective isotropy.
This admitted identity clock is owned by a changed evolution and does not repair the shifted MAIN source.

## 9. Scoped decision and limits

MAIN and ADJ have complete full-support mixed atomic/non-atomic sequential probabilities, exact inverse domains and full source ledgers, but fail intrinsic inverse IMAGE absolute continuity and forward-shift nonsingularity.
Their strict prescribed ratios additionally have zero denominators at 1 0^infinity and no limit at 0^infinity. These are all-state results, not extrapolations from sampled paths.
The opposite positivity direction holds on E_1, so it is specifically the null-source-to-positive-image direction that makes any IMAGE density impossible; no version repair or boundary deletion is permitted.
The two admitted controls have fully owned but target-adverse clocks: Bernoulli lag time and zero identity time. No result is transferred between owners.
Disposition: STOP / FORK GAC01 at clock admission. Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
This is not a universal no-go for all nonlocal sources or other measures. No new measure, roof, effective quotient, owner, external publication or sixth round is authorized.

EOF — full independent raw proof frozen; intrinsic admission failure with source retained; internal NOT_CALIBRATED; await PAPER UNLOCK.
