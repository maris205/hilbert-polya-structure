# LVM01 — independent raw-card proof

**Result:** full owners and prescribed clocks exist; MAIN and all three controls have J_k=1 and c=0 everywhere.
MAIN, EDGE and LINE have trivial source isotropy. FINITE-MEMORY has the exact return criterion below, not a cycle census.
Every physical stabilizer is {0}; hence there are no positive primitive physical packets or positive-time repetitions.

## 1. Input and provenance

Sole scientific document: [candidate card](../candidate-card.md), original lines 1–86 plus authorized additions 87–104.
Original-prefix SHA256: `770a774cd4cff6bfe43eb4ee3c10996a556cfa1afa4468171072512e427ac28c`.
Released 104-line SHA256, reverified: `821b07ec4510cecb9b6245b4fcd58724512724c7c5c1ad52fc6449eef3864a18`.
All those lines were read during CP1; this proof starts only after root's explicit mathematical release.
No MAIN manuscript, peer result, old 329 proof/card or other scientific document was read for this derivation.
ARS bounded raw-card work; shared history and my prior CP1 access are inherited: NOT blind, NOT_CALIBRATED.
No external source, scientific numerics, auxiliary delegation or model change. Only this file is written; CP1 stays frozen.

## 2. Graph and common owner construction

For MAIN, the multiples av, 2<=a<=v, give v-1 distinct neighbors, and the divisor part is finite.
The two parts lie respectively above and below v, so there are no loops and d(v) is finite and positive.
An upper adjacency v--av occurs exactly when the reverse divisor condition b=v at av holds; conversely every lower adjacency reverses an upper one.
Thus the displayed rule is an undirected locally finite simple graph on all v>=2, with countably many oriented edges.
The permissions are precisely the stated current-vertex factor/divisor tests, not selected prime transitions.

We prove the owner directly for each of the four frozen systems using the following common calculation.
Let V be its countable vertex set, let M_v be K (MAIN/EDGE/LINE) or Z/d(v)Z (FINITE-MEMORY), and let M=product_v M_v.
Write pi_v:M_v->Z/d(v)Z for reduction or the identity, and let nu be the specified product Haar/uniform probability.
K is the inverse limit of finite residue groups; its Haar pushforward to Z/mZ is uniform, since translations permute the m cosets.
Consequently all pi_v are well-defined, onto and uniform; translation by 1 in each M_v preserves its measure, including d(v)=1.
The countable product measure exists from compatible finite-coordinate probabilities; M is compact metrizable and X=E_oriented times M is a countable union of compact fibers.
Each entire edge fiber has mass 1, so edge counting times nu is sigma-finite, on the complete frozen carrier.
No initial memory, unvisited coordinate or null point has been removed.

For x=((u,v),rho), put w=iota_v^-1(iota_v(u)+pi_v(rho_v)); F(x)=((v,w),rho+1_v).
Given y=((v,w),rho'), subtract 1_v FIRST, obtaining rho; then u=iota_v^-1(iota_v(w)-pi_v(rho_v)).
This produces a legal neighbor and exactly one predecessor. Substitution in either order proves F^-1 F=F F^-1=id.
The finite residue tests are clopen and coordinate translations are homeomorphisms; hence F and F^-1 are continuous on the edge-discrete product space.
Thus each system has a genuine full homeomorphism, not a selected-history relation. All integer iterates exist at every state.

## 3. EVERY-Borel measure law, not merely cylinder counting

Fix neighbors u,w of v and let
P_(u,v,w)={((u,v),rho):pi_v(rho_v)=iota_v(w)-iota_v(u)}.
These clopen pieces partition X as (u,v,w) varies. On this piece F changes edge to (v,w) and translates memory by 1_v.
Its image is
P'_(u,v,w)={((v,w),rho'):pi_v(rho'_v)=iota_v(w)-iota_v(u)+1}.
For each target edge (v,w), the residues on the right run through ALL Z/d(v)Z as u runs through N(v).
Therefore the image pieces are disjoint and partition the ENTIRE target X, not just a conull subset.
For every Borel A subset P_(u,v,w), product translation invariance and unit edge mass give mu(F A)=mu(A).
For arbitrary Borel E subset X, partition E by the countably many P pieces; their images are disjoint Borel sets.
Countable additivity, also for infinite measure, gives mu(F E)=sum_P mu(F(E intersect P))=sum_P mu(E intersect P)=mu(E).
Applying this equality to F^-1 E and iterating proves mu(F^k E)=mu(E) for EVERY Borel E and EVERY k in Z.
This proves both directions of nonsingularity and the actual IMAGE law on each own full measure space.

## 4. Frozen all-point versions and complete action groupoids

The MAIN cylinder fixes one edge and N-1 coordinates modulo N!, hence mu(C_N(x))=(N!)^(-(N-1))>0.
For EDGE the own cylinder mass is (N!)^-2; for LINE it is (N!)^(-(2N+1)).
For FINITE-MEMORY it is product_(v=2..N) 1/d(v)>0. These are finite masses for every retained x and N>=2.
The preceding EVERY-Borel proof gives mu(F^k C_N(x))/mu(C_N(x))=1 for each x,k,N, not just almost everywhere.
No active-vertex cutoff or divisibility d(v)|N! is used: the routing-piece measure proof precedes and covers every cylinder.
Thus all four prescribed limits exist and satisfy J_k(x)=1 at EVERY x,k, including arbitrary null memory states.
They are positive finite Borel versions, satisfy the every-Borel integral identity, and require no null-point reassignment.
In particular J_(k+l)(x)=J_l(F^k x)J_k(x) and J_(-k)(F^k x)=1/J_k(x); the frozen c=-log J is identically zero.

Write G={(k,x):x->F^k x}. Composition is (l,F^k x)(k,x)=(k+l,x), and inverse is (-k,F^k x).
The arrow space Z times X and these Borel maps give the full transformation groupoid; distinct k are never identified by endpoints.
All incoming arrows to y are EXACTLY (k,F^-k y), k in Z. There is one for each k, even when different k have the same source point.
Let lag(k,x)=k. The FULL clock kernel is G, the FULL lag kernel is G^(0)={(0,x)}, and their intersection is G^(0).
These are arrow-level statements; they do not discard ineffective isotropy at periodic states.
Below, source isotropy is identified with its retained integer parameters k, not with an endpoint-only relation.

## 5. All-point source isotropy for profinite memories

For n>=0 write the actual trajectory as F^i x=((v_(i-1),v_i),rho^(i)), with initial edge (v_(-1),v_0).
Let L_w(n,x)=#{0<=i<n:v_i=w}. Only finitely many counts are nonzero and sum_w L_w(n,x)=n.
Induction using the exact update gives rho^(n)_w=rho_w+L_w(n,x), in the own coordinate group, for EVERY w.
For MAIN, EDGE and LINE, that group is K. The embedding Z->K is injective: a nonzero integer a is nonzero modulo any integer m>|a|.
If n>0, some L_w(n,x)>0, so the corresponding K-coordinate cannot equal its initial value.
Hence F^n x!=x at every state, independently of whether the token edge closes and independently of the initial memory values.
A negative-period equality would imply a positive one by applying the opposite iterate. Thus Stab_G(x)={0} for ALL x in these three owners.
This proof retains every memory coordinate and applies to null, integer and noninteger states alike.

## 6. FINITE-MEMORY: exact criterion, not recurrence classification

Here rho_w is a residue modulo d(w). The same exact update identity yields, for n>0,
F^n x=x iff (v_(n-1),v_n)=(v_(-1),v_0) AND d(w) divides L_w(n,x) for EVERY w.
Unvisited coordinates have count zero and remain unchanged; this is a full-state equality, not a projected token return.
Equivalently, a proposed finite walk starting at x's initial edge is the actual trajectory precisely when each step satisfies
iota_(v_i)(v_(i+1))=iota_(v_i)(v_(i-1))+rho_(v_i)+L_(v_i)(i) mod d(v_i),
where L_w(i) counts visits in that proposed prefix and rho is x's initial memory. Thus the test presumes no unknown future orbit.
Together with the closing-edge and ALL-count congruences, these equations are a necessary and sufficient return test.
Necessity follows from the update; sufficiency follows inductively from deterministic routing and equality of every final coordinate.
Let R(x) be the set of positive n satisfying this test. If empty, source isotropy is {0}; otherwise set ell(x)=min R(x).
The periods of a bijection form a subgroup of Z, so Stab_G(x)=ell(x)Z in the latter case (Euclidean division by the least positive period proves this).
This fully specifies isotropy by the frozen exact criterion. No assertion that all, none, or a selected family of infinite-graph trajectories recur is made.
All multiples of ell remain distinct isotropy arrows; no effective quotient replaces this owner.

## 7. Own-control instantiations and full physical returns

EDGE: the two-vertex graph has one neighbor at each vertex; take M=K^2, its two-coordinate Haar, and the stated both-memory cylinders.
The inverse and EVERY-Borel partition proof above apply to its own spaces. Its token alternates, but positive visit counts prohibit any full-state period.
LINE: every integer vertex has the two ordered neighbors v-1,v+1; take ALL K^Z and the stated |v|<=N cylinders.
Its own countably many edge fibers, residue partitions and translations satisfy every step of the proof, and all source isotropy is trivial.
FINITE-MEMORY: retain MAIN's entire graph, take the own finite residue products and exact-coordinate cylinders; uniform translation gives its own IMAGE law.
Its possible source isotropy is precisely Section6's criterion, not MAIN's no-period result transferred across changed memories.
Thus the four separate instantiations establish all inverse, measure, cylinder, clock, incoming and kernel claims for the frozen owners.

For EACH owner the extension arrows are (k,x,h):(x,h)->(F^k x,h), since c=0.
All incoming arrows to (y,h) are exactly (k,F^-k y,h), k in Z; every real height and every source state is retained.
Extension isotropy at (x,h) equals Stab_G(x): trivial for MAIN/EDGE/LINE and the criterion-defined group for FINITE-MEMORY.
Its clock image H_x=c(Stab_G(x))={0} at EVERY x, regardless of finite-memory source periodicity.
Directly, the full orbit SET is bijective to (X/F^Z) times R_real by [(x,h)]->([x],h).
Equality of extension classes preserves height exactly, and equality at fixed height is exactly an actual F-orbit relation; this proves the bijection.
Height translation is therefore ([x],h)->([x],h+t), a complete free real action. Its entire stabilizer is {0}, not merely absence of one tested return.
Each F-orbit contributes its full real line of physical phases; incoming states in that orbit are already identified by actual arrows, not selected representatives.
There are NO positive primitive physical packets or positive repetitions in any owner; finite-memory source cycles survive only as zero-clock isotropy.
No quotient topology, quotient invariant measure, graph-length clock or positive roof has been substituted.

## 8. Scoped decision and limits

MAIN's owner, all-point IMAGE and kernels are established, but its frozen physical-time gate fails: no positive physical periods exist.
Disposition: STOP/FORK LVM01 at that gate; the controls confirm the same clock outcome without erasing their different source isotropy.
The 329 collision is only the disclosed prior context; no theorem from it or another owner was used in this proof.
This is a variant's exact negative result, not a universal no-go for other measures, clocks or local-memory dynamics.
Sigma-finite measure preservation is not asserted to imply ergodic conservativity or recurrence.
No finite-memory replacement, high-period census or graph roof is warranted; FINITE-MEMORY classification stops at the exact authorized criterion.
Strong naturalness remains OPEN; T3 NOT AUDITED; classical A0–A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

EOF — raw-card proof frozen; full owner and controls proved, no positive physical packets, no finite-memory cycle census.
