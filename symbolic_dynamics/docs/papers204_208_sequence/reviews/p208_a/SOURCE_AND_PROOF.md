# P208 A — proof reconstruction and bounded source subtraction

2026-09-06 UTC. Actual nonauthor review of frozen Round 0. Mathematical
conclusion: MATH_VALID. Residual value: GO_NARROW_TWO_AXIS, with all the
deductions below. None of the arguments is an author repair supplied by A.

## 1. Literal dictionary: why every cell really runs the smaller map

Let e denote a boundary interval, c=(e,e), N=n-1 the leaf count, and q the
internal-node count. Ordered children retain all vertex labels. Let
LS(T)=[B1,...,Bk] mean T=(((e,B1),B2),...,Bk), let iota(S,A) replace S's
leftmost leaf by A, and put G(B)=F(e,B). The author's P uses seed
F(B1,B2) and then iota(G(Bj),previous product).

The scheduling invariant needs the original noncrossing set, not a claim
that arbitrary flips commute. Only the visited diagonal is removed.
Consequently every original not yet visited remains. A replacement crosses
that original, hence was absent from the initial noncrossing triangulation.
It is never on the snapshot list and remains protected.

If 0 is not an ear, its original neighbours are
1=a0<a1<...<ak=n-1. The initial fan edge (0,ai) has incident triangles
(0,1,ai) and (0,ai,a(i+1)); the previous replacement supplies the former.
Its replacement is (1,a(i+1)). The final one bounds ear 0. In the remaining
polygon, the initial first cell is (B1,B2), while each subsequent cell is
(e,Bj), with earlier material contracted to one boundary interval.
Crucially the still-scheduled original root of a nonleaf Bj belongs to
that cell too. The manuscript explicitly includes it; omitting it would
give the wrong recursion. Restricted lexicographic comparisons are
unchanged by increasing relabelling. Protected boundaries isolate the
interiors, so the possible interleaving of cells does not change their
individual updates. Gluing their final trees by iota proves
F(T)=(e,P(LS(T))).

For T=(e,B), if B=e this is the triangle. If B=(e,C), the sole original
1-fan edge (1,n-1) becomes (0,2). Contracting that new cherry leaves the
smaller original sweep on (e,C), including C's root when present; expansion
gives G(e,C)=iota(G(C),c). For a longer left spine of B, the preceding
1-fan flips protect the cells based at 2, and the final edge again makes
the cherry; the result is G(B)=(c,P(LS(B))). The smaller cells and triangle
base make induction well founded. These cases prove the literal F/G/P
dictionary on all sizes. Output root-left children are e or left combs;
a nonleaf G input has a left comb of length at least two.

## 2. Complete inverse, not only a count

Write W_j(T) for j forced leading-e wrappers. For a target Y=(LC_l,R)
with nonleaf R, F sources are W_(l-1) Fold(D(R)). G sources are
W_(l-2) Fold(D(R)) when l>=2 and none when l=1. A root-comb LC_s instead
has exactly the right-comb source RC_s for F and RC_(s-1) for G; noncomb
root-left targets have no sources. The formal e base is not another
polygon state.

For l=1 the source must have nonleaf left child, so it is directly the
spine list in the protected-cell equation. For l=2 in G, the longer-spine
branch gives the lists D(R). The other branch would require a G image with
root left child e and nonleaf right child; output shape excludes it.
For larger l, the cherry-substitution branch removes exactly one leading
e and reduces l by one. When R=e the product of a seed pair cannot be a
leaf, so reductions end only at F(c)=c or G(e)=c. This is why root-comb
targets do not acquire an extra branch.

The exact identity LS(iota(S,A))=LS(A)LS(S) now identifies D(R).
Cut LS(R) into nonempty consecutive blocks. Invert the first block as an
F target to obtain the ordered pair (B1,B2); invert each later block as a
G target to obtain one Bj. All problems are smaller than the whole target
currently being inverted. Folding reconstructs one source list, and its
P output is R. Conversely, the source list itself determines
F(B1,B2),G(B3),...,G(Bk), whose spine lengths recover every cut. It also
determines each selected source. Therefore no two choices yield the same
list, and no source is omitted. This establishes a labelled source-set
bijection without searching the carrier.

An admissible all-leaf block has positive length and one source. A block
ending in nonleaf D has form e^a D; the seed permits a=0, a later G block
requires a>=1, and its source multiplicity is h(D). These restrictions
are consequences of the simultaneous inverse, not guessed language rules.

## 3. Gap evaluation and strict extremum

For LS(R)=e^a0 D1 e^a1 ... Dr e^ar, an all-leaf spine of length s has
2^(s-1) compositions. If r>0 and an internal gap is zero, two consecutive
decorations cannot be assigned to admissible successive blocks; the count
is zero. A vanishing nested factor also makes it zero.

For an internal gap of a>=1 leaves, the following decorated block must
take a nonempty final segment. The rest is an arbitrary composition,
giving 1+sum_(j=1)^(a-1)2^(j-1)=2^(a-1). At the beginning, either the
decoration ends the seed or follows a nonempty all-leaf composition;
an empty boundary run gives one, otherwise the same 2^(a-1) factor.
The trailing run is any composition. Thus

    h(e)=1,
    h(R)=2^E product_j h(Dj),
    E=max(a0-1,0)+sum_(1<=i<r)(ai-1)+max(ar-1,0)

on the positive branch, with the stated zero/all-leaf cases. The complete
F fibre is h(R) exactly for Y=(LC_l,R), zero otherwise. This includes
unreachable targets and every comb/seed boundary.

For strictness put A=sum ai. A positive decorated spine has
q(R)=A+r+sum q(Dj). The gap exponent is at most A and induction bounds
each nested exponent by q(Dj)-1. Hence

    log2 h(R) <= A+sum(q(Dj)-1) = q(R)-2r <= q(R)-2.

An undecorated left comb instead attains 2^(q(R)-1). Therefore equality
in h(R)<=2^(q(R)-1) is equivalent to R being a left comb. For a whole
target of internal size m, q(R)=m-l. If m>=3, a leaf R gives one, strictly
below 2^(m-2). A nonleaf gives at most 2^(m-l-1)<=2^(m-2), and equality
forces l=1 and R=LC_m. In the fixed ordered dictionary that is exactly
the labelled fan at 1. Thus the maximum is 2^(n-4) and uniquely attained
for n>=5. The one- and two-internal-node carriers have all fibres one.

## 4. K and the phase clock

The protected product gives, for a>=2,
G(LC_a,R)=(c,D_a(R)), where D_a(R)=iota(G(R),LC_(a-1)).
If G(B)=(LC_l,Q), define K(B)=D_l(Q), with K(e)=e.
Then G^2(B)=(c,K(B)); this also holds at e since G(c)=(c,e).
G adds one leaf, so K preserves size.

Compute G^3(B) in its two associations and use G(c,S)=(c,G(S)).
Cancelling the common c gives KG=GK. Applying the same equation twice
to G^2(c,R) gives K(c,R)=(c,K(R)). These are identities of the already
proved map; no arbitrary edge-order commutation is needed.

For N>=3 let C_N consist of (LC_a,R) with a>=2; let C_1={e}, C_2={c}.
The formula for K puts every N-leaf tree into C_N. When Q is nonleaf,
G(Q)'s nonleaf left comb cannot be shortened by substitution. When Q=e,
K(B) is a comb with l=N, and N>=3 excludes the only small obstruction.
For T=(LC_a,R) in C_N and N>=4, D_a(R) lies in C_(N-1): if R=e it is
LC_a with a=N-1>=3, otherwise the same comb-preservation argument applies.
Now K(T)=G(D_a(R))=(c,S). Applying the two cases once more puts S in
C_(N-2) when N-2>=3. At N=4 the right child is uniquely c; at N=3 the
only class element LC_3 is fixed. Thus the stronger inclusion really is
K(C_N) subset {(c,S):S in C_(N-2)}, including both boundary sizes.

Put Z_1=e, Z_2=c, Z_N=(c,Z_(N-2)). The intertwiner fixes them. Once the
first cherry is fixed, every further K step acts only on its right child.
Induction on N gives class entrance at most floor((N-2)/2), and one
preliminary step gives arbitrary entrance at most floor(N/2). This proves
unique K recurrence, not merely a selected attracting orbit.

Both square identities are necessary:

    F^2(e,R)=(e,K(R)),
    F^2(T)=K(T) whenever T has nonleaf left child.

For the latter, writing P=P(LS(T)) gives F(T)=(e,P), G(T)=(c,P),
and both sides equal G(P). It does not require T already to lie in C_N.
Also G(Z_j)=Z_(j+1) and F(Z_N)=(e,Z_(N-1)); for N>=3 these distinct
states form a two-cycle.

Every first image is in C_N or has form (e,R). The first branch needs at
most 2 floor((N-2)/2)<=N-2 further steps. The leaf-left branch has even
iterates (e,K^t(R)), yielding 2 floor((N-1)/2). Its odd iterates can also
be written K^t G(R), and G(R) is in C_N, giving
1+2 floor((N-2)/2). Their minimum is N-2 for N>=4; this is the essential
odd-phase saving. Adding the first step gives N-1=n-2, and eliminates all
other periodic components. N=2 is the fixed triangle; the two N=3 states
already form the whole quadrilateral carrier.

Finally S_3=(e,c), S_N=(S_(N-1),e) gives
F(S_N)=(e,S_(N-1)), K(S_4)=LC_4 and K(S_N)=(c,S_(N-2)) for N>=5.
Its left spine is [c,e,...,e], so these follow directly from the seed and
later cherry products. With J(R)=(c,R), the time-(N-2) state is
J^(k-2)(LC_4) at N=2k and (e,J^(k-2)(LC_4)) at N=2k+1. The nonleaf/leaf
root distinguishes the opposite phase, while LC_4!=Z_4=(c,c) excludes
its own phase. The upper bound therefore makes the entrance exactly
N-1 in both parities. Finite boxes are not used in this argument.

## 5. Actual primary-source bodies and their limits

The actual six frozen bibliography entries, rather than shorthand names in
the assignment, were audited. sources/web01.json through web04.json retain
the returned web contexts; sources/primary retains exact primary PDFs,
layout text, download/extraction argv/env/exits/streams and BODY_PINS.json.
Only the following selected bodies were read. No full-article read is
claimed where it did not occur.

| Primary source | Actual relevant read; contribution deducted and ceiling |
|---|---|
| [Bose–Lubiw–Pathak–Verdonschot, arXiv 1310.1166v2](https://arxiv.org/pdf/1310.1166v2) | Introduction and sections 1–3 through persistent label transfer, canonical fan and sorting; section 4's sorting-model simulation, Lemma 3 proof and Theorem 6 context. This supplies reversible labelled flips and sorting primitives. Later spiral/combinatorial polygon sections were not read. Published metadata were independently retrieved: Computational Geometry 68 (2018), 309–326, DOI 10.1016/j.comgeo.2017.06.005. No publisher-body read is claimed. |
| [Pallo, published 2006 PDF](https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf) | First-page identity, tree/triangulation and weight dictionaries, selected leftmost rotation in sections 2–3, section 4 opening and join algorithm. The selected coordinate reaches its maximal value and stays fixed. Deterministic fan building and this prefix-fixing primitive are deducted; remaining mirror/distance analysis is not used. |
| [Hong, arXiv 2201.10030v1](https://arxiv.org/pdf/2201.10030v1) | Introduction, Definition 2.2, section 4's Theorem 4.7 characterization and its proof, and the image enumeration proof. The meet-of-lower-covers operator and image results are precedents. No entire section 3 proof read is claimed. The abstract/body Motzkin indexing discrepancy is not imported as an OFS count. Published metadata: Advances in Applied Mathematics 139 (2022), 102362, DOI 10.1016/j.aam.2022.102362. |
| [Barnard–Defant–Hanson, arXiv 2312.03959v1](https://arxiv.org/pdf/2312.03959v1) | Section 5.2, Theorem 5.3 and its full proof; section 9 quotient setup, Lemma 9.3/Proposition 9.4, Theorem 9.6 statement and opening proof, later Lemma 9.16/Theorem 9.17 context. The torsion-class preimage theorem is a genuine all-target predecessor precedent, not just an image count. Its semibrick/Pop hypotheses require an actual dictionary to apply. Most representation theory and the full section 9 proof were not read. |
| [Ajran–Defant, arXiv 2501.10311v1](https://arxiv.org/pdf/2501.10311v1) | Introduction 1.1–1.3, local Lemmas 2.3/2.4/2.6, section 3 bounds and extremal witness including Proposition 3.3 proof, and section 4's complete image criterion and explicit preimage construction proof. Section 5 only at its opening; no full higher-image comparison. The actual v1, not an unverified later publication, is cited. |
| [Mansour, published JIS 9 (2006), 06.1.5](https://cs.uwaterloo.ca/journals/JIS/VOL9/Mansour/mansour86.pdf) | First page, section 2.1 first-return framework, Theorem 2.5 and Corollary 2.1 including the displayed UUDU specialization and relevant proof. This owns the whole static series identified below. A did not visually inspect the source's table; the gate's table observation is not represented as an A page view. No inference uses those table entries. |

The two published metadata records are also corroborated by actual primary
publisher search returns in web04; other sources retain their exact
actually read versions. Bounded fresh literal snapshot/lexicographic
triangulation queries returned unrelated material or no direct result.
Those nonhits are not priority evidence. No inaccessible source theorem,
external review call, upload, specialist contact or future publication
status has been invented.

## 6. Complete primitive adapters and deductions

There is an exact enlarged-carrier adapter to edge-labelled flips.
Let R assign labels 1,...,n-3 to the initial lexicographically sorted
diagonals; let tau_i flip label i and transfer it to the new edge; let E
erase labels. Then

    F = E tau_(n-3) ... tau_1 R.

Until tau_i, flips of other labels leave its original edge intact. Thus
the projected sequence is exactly the snapshot update. Each tau_i is an
involution, but the repeated erasure/reset is not invertible. Noninjectivity
of F does not refute this complete lift. All elementary flip, scheduling,
reset and composition credit is therefore zero. The cited persistent-label
sorting results do not themselves determine this reset section's complete
source intersections or iterated E/R dynamics; the protected-cell and K
lemmas do that work.

On the quadrilateral, the ordinary Tamari poset is a two-element chain.
Descending Pop sends both elements to the minimum; F exchanges them.
Their ranks are one and two. Hence there is no direct conjugacy there,
and any composition on that same two-element carrier containing that Pop
has rank at most one, regardless of the surrounding functions. This
excludes a uniform same-carrier such formula for the whole family already
at its small boundary. A does not claim a new full-size Pop computation,
an all-n rank inequality, or exclusion of larger carriers, phased lifts,
different posets or every possible adapter.

The scalar cuts and products are fully old once the geometric source
bijection is established. Nor is the image generating function a third
result. The submitted expression

    I=1+z/(1-z)^2 C(z^2/(1-z)^3),    C(w)=1+w C(w)^2

satisfies I=1+z^2 I+z(1-z)I^2. Mansour's displayed UUDU specialization
A=C(z/((1-z)(1+z)^2))/(1-z^2) satisfies the identical equation:
(1-z^2)A=1+z(1-z)A^2. The constant-one formal solution is coefficientwise
unique, since all coefficients of the unknown higher terms are multiplied
by z. This deducts the entire series, not merely matching initial values.
Equality of counts is not equality of the standard-word image. The
preserved hexagon source {(0,3),(0,4),(1,3)} maps to
{(1,4),(1,5),(2,4)}, whose standard word UDUUDUDD contains UUDU. A's full
literal records support that transition; no avoidance image theorem is
claimed. Generic prefix/cherry freezing is also deducted. What remains
is proving this exact geometric map has the K closure and both transported
phases, not naming the generic method.

## 7. Historical literal mechanisms, not title-only noncollisions

HISTORY_CONTEXT_PINS.sha256 was captured before the substantive historical
reads. It is a union of relevant archives and contextual pins, not a claim
that every listed file was read. The relevant original definitions/proof
sections actually read support these comparisons:

| Original inspected | Exact mechanism deducted; limit of the transfer |
|---|---|
| P144, papers/144-leftmost-dyck-reassociation/main.tex, primitive-factor update/iterate and complete terminal depth-source proof | Its move merges the next primitive factor into the first; entrance is factor count minus one. Every terminal depth-source lifts one final suffix of interior components. Grafting, leftmost scheduling, Catalan dictionaries and suffix clocks receive zero credit. That endpoint inverse is not a theorem about the recursively decorated, multi-cell one-step OFS source set, and its fixed endpoint dynamics does not supply the alternating K transport. |
| P90, papers/90-rule184-particle-periodic-zeta/main.tex, literal Rule 184 and conserved-layer/min-plus proof; GCM in docs/papers162_166_sequence/scouting/open_fresh_p167/SCOUT.md and its collision firewall | The traffic law preserves particle count and uses the min-plus moving-defect clock. The graph-matching wrapper has 2->11 and 1^r->2^floor(r/2)1^(r mod 2), with regular flat-run source parsing. Run decompositions, binary placements and defect/prefix stabilization are deducted. Neither these exact rules nor the flat inverse transports the size-varying OFS cell map or K square phases. GCM here means graph matching, not Gram cubes. |
| Q09 least-ear, C14 parity-selected edge, TFE root-fan frontier, LDL illegal Delaunay, PTR polygon rotation, in the pinned original scout files | Q09 flips the opposite edge of a selected least ear; C14 is a parity-conditioned one-edge selector; TFE increases rooted-fan degree under a refreshed frontier; LDL uses illegality on fixed generic coordinates; PTR is rotation. These own selectors, fan building, geometric flips and permutation dynamics. The exact reset-labelled lift above deducts the composition that does exist; calling OFS another schedule is not a contribution by itself. |
| COMB_PARITY_ROOT_ROTATION_REPORT.md, literal rule, parity analysis and section 4.4 forced inverse | The old selector applies one oriented root rotation, and its inverse has at most the forced left and right branches. Its parity-Catalan failure/kill remains unchanged. It does not reconstruct the recursively chosen OFS seed/later blocks or their unbounded fibres. Only the stated relevant proof sections were read, not a claimed whole historical archive audit. |
| P139 factor-start feedback, original definition and leading-one amplifier; P202 ternary ordered reset, original definition and inverse | The former owns its factorization and prefix-amplification primitive. The latter has forbidden 21 targets and independent 01 binary choices. This is concrete reason to deduct static factorization, prefix growth and power-of-two fibres. Neither supplies the labelled OFS block decoder or exact phase transport. Only the named sections, not both full papers, were read. |
| P204 A, exact scaled-descent adapter; P206 A, complete weak-record template adapter | The actual formula D_(r,m)(A)=binom(r+m,m) beta_m(A-1) and P206's maximum-position roots/reversed binary W/O interval bijection transfer the corresponding whole source restrictions to old evaluated templates. Those adverse results were read as complete-adapter standards, not dismissed because the maps have different names. No equivalent whole OFS template adapter follows merely from its binary factors: the recursively dependent geometric seed/later interface still has to be proved. |
| MNC gate, full coloured-tail adapter through sections 1.1–1.4; UGR gate, full source/rank deduction report | MNC enters after two steps the labelled bijection (p,D), evolves as (ECA36(p),D), and then deletes nonsingleton pulses. That kills its temporal mechanism after a bounded front end. UGR's full union of TCSD sign fibres deducts static inverse enumeration but does not automatically transfer an aggregated-target maximum. These are precise transfer boundaries, not a license to count generic freezing or a shared number sequence as a new OFS axis. |

Some other historical inputs are pinned only as provenance/context, not
freshly re-read science. In particular no fresh complete P1–P196 census,
full P205/P207 proof review, all-paper noncollision, or all-composite
classification is claimed here. Existing gate judgments were not used in
place of the actual all-size proof and primary comparisons above.

## 8. Historical/current provenance and final residual

The seven workspace origins of the author freeze have exact historical
copies under qa/p208_round0_input_inspection_v2/historical_workspace_origins.
A verifies those against the immutable provenance seal. The live seven
still matched at the actual inspections, but mutable context is not
silently promoted to an immutable proof input.

The root/batch recovery indexes changed during A's work. Their assignment
hashes were contemporaneously recorded, not their original bytes copied.
Later read-only Git retrieval from commit
076cfbd45446e4a803de495d009f186a54bea503 recovered the exact two assignment
versions and matched those original pins; assignment_context_recovery
records this later recovery explicitly. It does not claim a pre-read
physical copy or rewrite historical provenance.

After every deduction, the residual is exactly: (1) the all-target labelled
operational source-set construction, all excluded boundaries and strict
unique fan extremum; (2) the exact geometric-to-K transport, strong
closed inclusion, commuting odd phase, unique recurrence and sharp
all-size clock with both parities. Their proofs are distinct consequences
of a shared map-specific geometric dictionary. This conjunction survives
the particular complete adapters inspected, not every imaginable source.
An applicable earlier owner theorem or full adapter reopens it. No
arbitrary scheduling, unlabelled quotient, all-time inverse/basin census,
global priority or external release is endorsed.
