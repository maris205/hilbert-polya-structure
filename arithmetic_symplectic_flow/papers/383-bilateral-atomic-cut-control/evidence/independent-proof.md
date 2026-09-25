# Independent card-only proof — bilateral atomic cut CONTROL

Candidate `ANG-CONTROL-20260922-BAC01`; internal shared-history, inherited-model, **NOT_CALIBRATED**, not blind or external peer review.
Sole scientific input: `candidate-card.md`, all 59 lines, SHA256 `d9f5a9215dc603ab848a67900f8ca6cde9b751f5cb302fb2e693fbf9bf9ffe25`.
Root explicitly released mathematics after reading CP1. No main, peer, scout, old proof or other new package was read.
No network, numerical experiment, delegation, Git or PDF; only this raw report is written. ARS/stream instructions remain as recorded in CP1.
All assertions below are analytic deductions from the frozen card, not claims that the card itself proves them.

## 1. Complete carrier and exact cut domains

Represent x by its support S⊂Z. Let Γ(S) be the collection of consecutive-support gaps, keeping occurrences when removing a particular gap.
Write AC(Γ) for: distinct gap values do not divide one another. Empty and singleton collections satisfy AC.
X={S:AC(Γ(S))} is closed: two violating gap occurrences are witnessed on a finite coordinate interval. It is shift invariant and compact.
No finite, one-ended, two-ended or null configuration is discarded.
Use t=T, p_a=I_a, d_a=I_a^{-1}; letters act in chronological order in this report.
The exact support updates are

    tS=S−1; t^{-1}S=S+1;
    p_a S=(S∩Z_{<0}) ∪ ((S∩Z_{≥0})+1) ∪ ({0} if a=1);
    d_a S=(S∩Z_{<0}) ∪ ((S∩Z_{>0})−1), requiring 1_S(0)=a.

For each update, require AC of its output. This already gives the entire domain, including every null point.
A more local insertion test is useful. Let p=max(S∩Z_{<0}), q=min(S∩Z_{≥0}), omitting a missing endpoint.
Remove the crossing occurrence q−p if both endpoints exist, leaving Γ_rest (its value may still occur elsewhere).
For p_0 add q+1−p if both exist. For p_1 add −p if p exists and q+1 if q exists.
The resulting occurrence collection is exactly Γ(p_a S); requiring AC is the complete insertion-domain test.
For deletion use p=max(S∩Z_{<0}), q=min(S∩Z_{>0}). If a=0 remove crossing q−p when both exist.
If a=1 remove incident gaps −p and q when present. In either case add q−1−p when both endpoints exist.
The other occurrences are unchanged; require the stated symbol and AC. All absent-endpoint cases are included.
These rules matter globally: testing only newly adjacent gaps against each other would omit their compatibility with retained distant gaps.
Insertion/deletion are inverse continuous maps between their exact closed domains/ranges; neither openness nor étaleness is assumed.
Every finite chart domain is closed by successive pullback of these closed generator domains; the chart is a homeomorphism onto its closed range.

## 2. Labelled partial-path groupoid, without extra relations

For a finite word w, evaluate the support rules successively and require every intermediate legality and deletion-symbol test.
Call that unreduced path domain D_path(w). If an adjacent generator/inverse pair occurs in an admissible path, it returns to the preceding state.
Removing that pair leaves an admissible path with identical endpoints. Repeating gives the unique freely reduced word red(w).
On D_path(w), the path map equals the map for red(w); D_path(w) can be smaller than D_path(red(w)).
This possible domain enlargement is not an identification of arbitrary points or of additional word relations.
For each reduced w set D_w=D_path(w), θ_w its actual map; D_empty=X and θ_empty=id.
Arrows are (θ_w x,w,x), x∈D_w. Equal labelled triples alone are identified.
Concatenate two composable admissible paths and reduce: the preceding cancellation observation proves closure and endpoint consistency.
Associativity follows from associativity of free-word reduction and of endpoint composition; inverse reverses the letters and uses actual inverse charts.
Units are (x,empty,x). This is a groupoid, with a standard Borel arrow space given by a countable disjoint union of the D_w.
The reduced-word map ℓ:G→F(t,p_0,p_1)^{op} is a homomorphism (the opposite group matches our chronological words), with ker ℓ equal to the units.
No globally defined free-group action, equality of all unreduced/reduced domains, germ quotient or extra action relation has been asserted.
All incoming arrows to z are obtained by every reduced v with z∈D_v: put x=θ_v z and take (z,v^{-1},x).
This enumerates all finite histories admitted by the card, with their actual labels; no chosen inverse branch or orbit representative is substituted.

## 3. Probability, atom status and every-Borel IMAGE

The map e is a bijection Z→N_0. Binary coding therefore bijects all finite subsets of Z with the nonnegative integers.
The allowed coding set C is a subset of N_0 containing 0 and 1. Thus 1<B=Σ_{n∈C}2^{-n}≤2.
The countable sum μ=Σ_{F allowed}B^{-1}2^{-code(F)}δ_{1_F} is a probability on the Borel space X.
Every allowed finite F is an atom of its prescribed strictly positive mass; every infinite-support point has mass zero.
The set A of finite-support points is countable Borel, μ(A)=1, and its complement N remains part of the carrier with μ(N)=0.
For every nonempty finite-window cylinder in X, take the support inside that window and set all other coordinates to zero.
Its gaps form a subcollection of those of a cylinder point, so this is an allowed finite-support point in the cylinder. Hence μ has full support.
Each generator and its inverse preserve finite versus infinite support. Therefore every actual chart bijects its atomic and null parts separately.
The frozen b is positive finite Borel everywhere: b(F)=2^{-code(F)}/B<1 on A and b=1 on N.
For any reduced or unreduced actual chart θ and Borel E in its domain, injectivity and countable summation give

    μ(θE)=Σ_{x∈E∩A} b(θx)=∫_E [b(θx)/b(x)] dμ(x).

Images are Borel because the chart is a homeomorphism between closed subspaces. Null parts contribute zero on both sides and are not removed.
This proves every-Borel IMAGE for the prescribed J, with 0<J(x)<∞ at every domain point, including N.
For composable charts J_{v∘w}(x)=J_v(θ_w x)J_w(x) by cancellation of b(θ_w x).
Inverse factors reciprocate; admissible path cancellation preserves J; any two paths with the same endpoints have the same J even when their labels remain distinct.
Thus the frozen all-point version is admitted, not merely an almost-everywhere density selected after testing.
Only now define c(z,w,x)=−log J_w(x)=log b(x)−log b(z). It is a real additive groupoid cocycle.
On atomic arrows c=(code(z)−code(x))log 2; on null arrows c=0. Atomic/null cross-arrows do not exist.
The code is injective, so two atomic endpoints have equal b exactly when they are the same point.

## 4. Named points first: complete stabilizer tests, not selected loops

Let L_x={reduced w:x∈D_w and θ_w x=x}; this is the source isotropy group, faithfully retained in the free group with the same chronological convention.
At 0^Z, t and p_0 are distinct fixed-point labels, while p_1 sends it to {0}, with J=1/2 and c=log 2; the inverse clock has the opposite sign.
Its COMPLETE L_0 is given by this finite test: start S=∅, apply the support/gap/symbol rules for every letter, reject illegal steps, and accept exactly when the final finite set is empty.
This tests every reduced label, including excursions through arbitrary allowed finite supports; L_0 is not being equated with the subgroup generated by t,p_0.
At 1^Z, t^{±1},p_1,d_1 fix the point. Inserting 0 creates a gap 2 among surviving gaps 1, so p_0 is illegal; d_0 fails its symbol test.
Consequently every admissible path from 1^Z stays there and uses only t^{±1},p_1^{±1}; its full orbit is a singleton and L_1=F(t,p_1).
All of these labels have zero clock, but they remain nontrivial source arrows.
For x=(10)^Z with support 2Z, t^2 is a fixed-point label. The direct p_0 update replaces one gap 2 by 3 and is legal.
The direct p_1 update introduces gap 1 beside surviving gap 2 and is illegal; d_1 replaces two incident gaps 2 by 3 and is legal, while d_0 fails at this phase.
These are diagnostics, not its full stabilizer: the complete test is the finite-tail criterion in the next section, specialized to period 2.
All points reached from this infinite-support point are null, so every such path has J=1 and c=0.

## 5. Constructive full-label membership at every point

Given any reduced word w of length n, first use the exact support update and gap tests of §1 at every step.
These explicitly specify the entire domain, not just endpoint admissibility; checking distant gap values is necessary when x is infinite.
There is also a finite-template test for the final equality θ_w x=x, rather than an unspecified return assertion.
Let a be the signed number of t letters and h the signed number of insertions p_0,p_1 (deletions count negatively).
Each generator moves an original coordinate by at most one. Outside the interval [−n,n], backward tracking cannot encounter the cut.
Therefore the actual output satisfies (θ_w x)_i=x_{i+a} for i<−n and (θ_w x)_i=x_{i+a−h} for i>n.
For −n≤i≤n, track backwards through the finitely many letters: the output is either a prescribed inserted symbol or one input symbol x_j with |j|≤2n.
All intermediate legality plus the following three conditions are necessary and sufficient for w∈L_x:

    x_{i+a}=x_i for every i<−n;
    x_{i+a−h}=x_i for every i>n;
    the tracked output equals x_i at every −n≤i≤n.

This gives full-label membership using finite coordinate templates and explicit tail/gap predicates. For arbitrary infinite input it is not claimed to be decidable from a bounded observation window.
For 0^Z it reduces to the finite-support test already given. For 1^Z it agrees with the exact free subgroup above.
For (10)^Z the tail conditions are exactly a∈2Z and a−h∈2Z; retain the finite middle-symbol and every-intermediate-legality tests as well.
Every intermediate point in this last test is eventually alternating at both ends. Its gap values are {2} together with finitely many computed exceptional values.
Hence its hard-constraint test and the entire stabilizer-membership test are finite for this named periodic input.
These formulas do not identify labels that act alike; nor do they assert that a word fixing its endpoints was legal at every intervening cut.
The complete orbit of arbitrary x is the set of all outputs of this explicit admissible-word procedure. Combined with §2 it specifies every incoming history and stabilizer, without selecting a preferred packet.
All finite-support points lie in one orbit: shift the leftmost 1 of a nonempty finite support to 0 and delete it.
No 1 remains to its left; this operation removes the first gap and translates all remaining 1s equally, preserving admissibility. Repeat to reach 0^Z, then reverse paths.
Thus finite-point stabilizers are conjugate to L_0 through actual paths. Infinite points cannot enter this orbit.
No assertion that asymptotic-tail equivalence alone suffices for MAIN reachability is made: hard intermediate domains remain essential.

## 6. All kernels, extension isotropy, phases and physical returns

Let q:G→R_X forget labels into the actual orbit equivalence relation. Its kernel consists of ALL source isotropy arrows, not only units.
The full clock kernel is

    ker c = G restricted to N  ∪  { (F,w,F): F∈A, w∈L_F }.

This follows from c=0 on null arrows and injectivity of the atomic masses; there are no cross-partition arrows.
In particular ker q⊂ker c, ker c∩ker q=ker q, and ker c∩ker ℓ consists exactly of units. No new numerical lag has been substituted for the frozen word label.
Fix the extension convention (x,r) --g--> (z,r+c(g)). Every retained source-isotropy label has c=0.
Thus extension isotropy at every (x,r) is exactly L_x, not a trivialization obtained by forgetting labels.
An incoming arrow g=(z,w,x) to (z,s) has source (x,s−c(g)); §2 enumerates all of them with no height or null-point deletion.
For a physical quotient point over the source orbit O, its full return subgroup is H_O={c(g):g∈L_x}={0}, for every x∈O.
This also follows directly without a chosen representative: u=r+log b(x) is invariant under every extension arrow.
The map [(x,r)]↦([x]_G,u) is a bijection of the full quotient SET with (X/G)×R; its converse follows by any actual path between two representatives.
Height translation is ([x],u)↦([x],u+t). Hence no nonzero time fixes any physical point, including the three named cases and all other null points.
There are no positive primitive closed packets, multiplicities or repetitions. Nontrivial zero-clock source/extension isotropy does not produce a positive-time closed orbit.
This is a set/Borel-groupoid result, not a claim of a smooth, contact, Hausdorff orbit-space or classical symplectic realization.

## 7. SHIFT-ONLY: its own lag action and complete ledger

Its whole carrier X and atom recipe are unchanged, so its normalizer equals B and the preceding full-support proof applies directly to this stated recipe.
Its actual arrows are (T^k x,k,x), k∈Z; all domains are X, all inverse histories are T^{-k}z, with retained integer lag k.
Every shift preserves A and N; countable atom summation proves IMAGE J_k(x)=b(T^k x)/b(x) on every Borel set and at every point.
Its c_k=log b(x)−log b(T^k x) is admitted. The lag kernel consists only of units.
Its clock kernel contains every null-point shift arrow and, on A, exactly arrows with T^k F=F.
For nonempty finite F that forces k=0; for F=∅ every integer k is allowed.
The full source stabilizer is {k:T^k x=x}: LZ if x has least positive shift period L, otherwise {0}; at 0^Z,1^Z,(10)^Z it is respectively Z,Z,2Z.
The empty configuration is its own orbit, not the common finite-support orbit of MAIN; all other source orbits are exact shift orbits.
Extension isotropy equals this full stabilizer, H={0} on every orbit, and the full quotient is (X/shift)×R with coordinate u=r+log b(x).
Incoming heights are s−c_k(x); every phase is retained. There are no positive primitive physical packets or repetitions.

## 8. HARD-OFF: own normalizer, full domains and labels

Here Y={0,1}^Z; all finite subsets are allowed, so its OWN normalizer B_off=Σ_{m≥0}2^{-m}=2 exactly.
Its atom masses are 2^{-code(F)−1}; finite supports are all atoms, their complement has mass zero but is retained, and finite-window truncation proves full support.
Insertions have domain all Y; deletions have exactly the matching-symbol domain. Shifts are total. Remove AC tests, not the deletion-symbol tests.
The §2 labelled groupoid construction and §5 finite-template membership proof apply to these expressly different domains; they do not import MAIN reachability restrictions.
Own atom/null preservation and atom summation give every-Borel IMAGE with b_off on all points, c_off=log b_off(x)−log b_off(z).
At 0^Z the full finite-support word test now has no AC rejection. All six generators can occur along paths from 1^Z, subject to deletion symbols; its stabilizer must not be replaced by MAIN's F(t,p_1).
For example, chronological p_0 p_1 t d_0 is a reduced return label at 1^Z: its unique zero moves from 0 to 1 to 0 and is then deleted.
For both constants use the all-word finite middle-symbol test; for (10)^Z also require a and a−h even. This describes every retained stabilizer label for the named points.
For general x the full §5 tail/template test, with only symbol-domain checks, is exact.
Here there is additionally a complete orbit description: x and y are equivalent iff there exist integers a,b and N with y_i=x_{i+a} for i<−N and y_i=x_{i+b} for i>N.
Necessity is the finite-template tail formula. For sufficiency first apply T^a, then replace a sufficiently long finite block by the desired block of y.
Choose its source/right endpoint so the net insertion length is a−b; arbitrarily large endpoints make both block lengths nonnegative.
Finite deletions and insertions at any chosen site are conjugates of the cut generators by shifts, are legal here, and realize that replacement with the required unchanged tails.
Thus its zero orbit is all finite-one configurations and its all-one orbit is all cofinite-one configurations; neither statement merges the two or discards other source orbits.
Its complete incoming labels are still all admissible reduced words, not one arrow per equivalent pair.
Clock kernel: every null arrow plus all finite-point stabilizer arrows; word kernel: units; endpoint-forgetting kernel: all stabilizers, contained in the clock kernel.
Extension isotropy equals its own full L_x. All H={0}, all phases form (Y/G_off)×R, and no positive physical primitive packets or repetitions exist.

## 9. ENDPOINT: actual relation quotient, not a borrowed action

Its carrier, μ and b are MAIN's prescribed ones, but the source is R_X={(z,x):some MAIN admissible word sends x to z}.
This is a countable Borel equivalence relation, being the countable union of the Borel chart graphs. All actual MAIN orbits remain, including every null point.
The formula c(z,x)=log b(x)−log b(z) depends only on endpoints, hence descends through q and is additive.
Its word-chart IMAGE proofs remain valid on charts, since changing labels did not change their endpoint maps or prescribed ratio.
Every source stabilizer is the single unit (x,x); extension stabilizers are also units. These are not MAIN's retained L_x groups.
Its clock kernel is the full relation restricted to N together with the diagonal on A, by the same own atomic-mass injectivity.
No retained free-word or integer-lag map is part of this owner. Forgetting word labels is the declared control change, not a theorem that MAIN labels were redundant.
Incoming arrows to z are all (z,x), x in its entire actual MAIN orbit, with incoming height s−log b(x)+log b(z).
All H={0}; the complete quotient is (X/R_X)×R with the same invariant u and free height translation.
The quotient SET agrees with MAIN's physical quotient, while the source and extension isotropy groups differ; there are no positive primitive packets or repetitions in this control either.

## 10. Scoped conclusion and frozen boundary

The full atomic law admits every actual chart with the exact predeclared all-point J. All null states and all MAIN word labels survive.
The decisive return computation is the global endpoint potential difference, not a census of three loops: every physical return subgroup is zero for MAIN and all three own controls.
This completes the atomic boundary-control audit but supplies no positive-time prime packets and no nonatomic escape from 368.
Naturalness remains OPEN; the atom recipe and null-point version are chosen control data, not an endogenous prime-clock construction.
No formal Route coordinate, classical realization or T3 object is claimed. A different measure, version, arrow quotient or physical clock would be a different frozen object.
Scope report and candidate card are unchanged. This raw report is to be frozen before any separately authorized manuscript read.

EOF — complete card-only raw proof; all-source atomic transport admitted; full H={0}; retained-label isotropy not discarded; internal NOT_CALIBRATED.
