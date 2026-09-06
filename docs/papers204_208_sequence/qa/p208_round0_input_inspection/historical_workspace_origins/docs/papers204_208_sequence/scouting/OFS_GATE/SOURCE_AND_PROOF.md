# OFS independent proof, source and value assessment

2026-09-06 UTC. Assessor: `/root/ofs_candidate_gate`. Scope: the unnumbered
original-diagonal lexicographic sweep on **all** labelled convex-polygon
triangulations, not a modified scheduler or a restricted family.

Mathematical verdict: **VALID AS STATED in the submitted author proof**.
Candidate value verdict: **GO_NARROW_TWO_AXIS**, subject to the deductions
and access limits below, not global novelty, admission or manuscript review.
Authors are `batch197_fosp_gate` and `batch197_lzk_gate`. The assessor supplied
no missing scientific lemma or author repair. The reconstruction below checks
their existing arguments; the alternative reverse-snapshot and poset routines
are diagnostic checks, not replacements for their all-size proof.

## 1. Exact object and geometric induction

Let F snapshot the n-3 original internal diagonals, ordered by their sorted
endpoint pairs. Flip each in that order in the current triangulation. An
unvisited original is present because a flip removes only the visited edge.
Every inserted diagonal crosses the one it replaces, so it cannot have been
in the original noncrossing set. Therefore **no inserted diagonal is ever
scheduled**, and no original can reappear. This verifies and strengthens the
relevant protection statement without the desk's earlier incorrect warning.
That warning and its correction remain preserved in the pinned originals.

Use the ordinary triangle rooted at (0,n-1) to encode a tree (L,R). A leaf e
is a boundary interval, c=(e,e), N=n-1 counts leaves, and m=n-2 counts internal
vertices. The auxiliary leaf is not an additional polygon carrier. Write
LS(T)=[B1,...,Bk] for T=(((e,B1),B2),...,Bk), and first(S,A) for replacement
of S's leftmost leaf by A. The author's G(B)=F(e,B) increases leaf count by
one. Its P has seed F(B1,B2) and subsequent attachments first(G(Bj),P).

When 0 is not an ear, its ordered original neighbours are
1=a0<a1<...<ak=n-1 with k>=2. The initial fan edges (0,ai), i=1,...,k-1,
flip successively to (1,a(i+1)): the two incident triangles at step i are
(0,1,ai) and (0,ai,a(i+1)). The replacement at the preceding step supplies
the first triangle. The final new edge (1,n-1) bounds ear 0. These protected
edges partition the remaining old diagonals into independent cells. The
first cell's tree is (B1,B2); each later cell is (e,Bj), with the earlier
prefix contracted to one boundary interval. This identification includes
the original root edge of a nonleaf Bj, not just its proper descendants.
Order-preserving relabelling preserves comparisons of endpoint pairs;
thus each restricted schedule is exactly the smaller F, not an arbitrary
sequence of flips. Gluing along the protected boundaries concatenates
left-spine lists and gives

    F(T) = (e,P(LS(T)))                 if |LS(T)| >= 2.

When 0 is an ear, write T=(e,B). If B=e there are no diagonals. If B=(e,C),
the only initial 1-fan edge is (1,n-1), whose flip creates (0,2). Contracting
the protected ear (0,1,2) leaves exactly the smaller tree (e,C); expanding
the contracted boundary leaf gives first(G(C),c). If B has at least two
left-spine branches, the earlier 1-fan flips create the same cells rooted
at 2, followed by the final (1,n-1)->(0,2) flip. The output is
(c,P(LS(B))). Every recursive call is smaller. Triangle cells use F(c)=c.
These cases exhaust the carrier and prove the submitted recursion by
induction, including both exceptional fan configurations.

Ear 0 toggles for n>=4: it is created in the first case and its bounding
edge is removed in the second. Every first image has left child e or a
nonleaf left comb. The checking program separately reconstructs the polygon
cells after the fan and executes their remaining schedules in reversed cell
order; this agrees on every original state, but is not the induction proof.

## 2. Complete inverse, including excluded branches

The recursion implies every nonleaf image has form (LC_l,R), l>=1. A G
image of nonleaf input has l>=2; its sole l=1 case is G(e)=c. Here LC_l is
the left comb with l leaves. Consequently a target with a noncomb left
child has no source. A comb target has one F source, the right comb; a
comb with at least two leaves has one G source. The reductions end at
F(c)=c and G(e)=c, rather than at an invented nonpolygon state.

For R nonleaf let p(R) count P lists with at least two inputs and output R.
For l=1, F sources are exactly the left-spine lists counted by p(R). For
l=2, G sources are those lists themselves; F sources attach one initial e.
The first-leaf-cherry branch cannot give an additional source: it would
need a G output with left child e and nonleaf right child, which the output
shape excludes. For l>2 the first-leaf branch uniquely reduces l by one;
the corresponding leading e in the source is forced. This is simultaneous
induction on tree size for F and G, not an assumption that their inverses
are interchangeable at the l=1 boundary.

In a P list, LS(first(S,A))=LS(A)LS(S). Thus cut LS(R) into nonempty
blocks. The seed is an F output of a nonleaf pair (B1,B2); all later
blocks are G outputs. A nonleaf-ending block is e^k D, with k>=0 for the
seed and k>=1 later. An all-leaf block may have any positive length.
An all-leaf block has one preimage; a D-ending block has p(D). The seed's
inverse gives its **ordered pair** (B1,B2), and each later inverse gives
one Bj. These data recover a unique original list, and conversely its
smaller output lists recover all the cuts. This proves source-set equality
and disjointness, not only the multiplicative number of possibilities.

Write LS(R)=e^a0 D1 e^a1 ... Dr e^ar with Di nonleaf. For r=0 and s=a0>=1,
the cut count is 2^(s-1). For r>=1 any internal gap ai=0 makes it zero;
a zero recursive h(Di) also makes it zero. Otherwise

    h(e)=1,
    h(R)=2^E product_i h(Di),
    E=max(a0-1,0) + sum_(1<=i<r)(ai-1) + max(ar-1,0).

Indeed an internal run of a>=1 leaves splits into a nonempty final prefix
of the following decorated block and any preceding composition: its count
is 1+sum_(j=1)^(a-1) 2^(j-1)=2^(a-1). The leading run additionally allows
the decoration itself to end the seed, giving the same sum. Empty boundary
runs give one, and the final run is an unrestricted composition. The full
F fibre is h(R) for a target (LC_l,R) and zero otherwise. Binary cut factors
receive no separate novelty credit; the substantive inverse statement is
their exact, recursive attachment to **all sources of this literal F**.

For q(R) internal vertices, h(R)<=2^(q(R)-1) for nonleaf R, with equality
only for a left comb. To see strictness without relying on a numerical
guess, if r>=1 the gap exponent is at most A=sum ai and the recursive
exponents at most sum(q(Di)-1). Since q(R)=A+r+sum q(Di), the resulting
exponent is at most q(R)-2r<=q(R)-2. Hence for m>=3 the maximum is
2^(m-2), attained only at l=1, R=LC_m. This is precisely the fan at vertex
1, so the maximum is 2^(n-4) for n>=5. At n=3 and n=4 every fibre is one;
the unique-max assertion deliberately excludes them.

The allowed-decoration species gives

    (1-z)^2 H = 1-z+z^2 H^2,
    I = 1 + z/(1-z)^2 C(z^2/(1-z)^3).

This static count is deducted in full. Matching it to old UUDU enumeration
does not identify individual targets. The reachable hexagon target
{(1,4),(1,5),(2,4)} has standard word UDUUDUDD, which contains UUDU; a
source is {(0,3),(0,4),(1,3)}. The independent canonical records it exactly.
The old naive left-edge exponent and unrestricted-decoration 58-versus-57
guess remain refuted in the original sealed packages; neither is a lemma
of this assessment.

## 3. K transport, closure and the two parity clocks

The submitted identities, with N always the leaf count, are

    G(LC_a,R) = (c, first(G(R),LC_(a-1)))                 (a>=2),
    G^2(B) = (c,K(B)),
    KG=GK,                     K(c,R)=(c,K(R)).

The first follows from the left-spine product: for a=2 its seed is G(R),
and for a>2 the preceding all-leaf product is LC_(a-1). If G(B)=(LC_l,Q)
and B is nonleaf, the second sets K(B)=first(G(Q),LC_(l-1)); K(e)=e.
This preserves size. At B=e, G^2(e)=LC_3=(c,e), so the base agrees.
Associativity evaluates G^3(B) as both G(G^2(B)) and G^2(G(B)); using
G(c,S)=(c,G(S)) and cancelling c proves commutation. Applying that same
identity twice proves the frozen-cherry intertwiner. No commutation of
arbitrary flips is presumed here.

Let C_N={(LC_a,R):a>=2} for N>=3, with C_1={e}, C_2={c}. The formula
for K gives K(T) in C_N. If Q is nonleaf then G(Q) already has a nonleaf
root left comb and grafting preserves it. If Q=e the result is LC_l, and
N>=3 forces l=N>=3. For T=(LC_a,R) in C_N, put
D=first(G(R),LC_(a-1)). For N>=4 this lies in C_(N-1): for R=e it is
LC_a with a=N-1>=3, and otherwise grafting only lengthens a nonleaf comb.
Then K(T)=G(D)=(c,S); the same two cases put S in C_(N-2). At N=3 the
sole class member LC_3 is fixed; at N=4 the right child is the unique c.
This verifies the stronger closure including the small cases:

    K(C_N) subset {(c,S): S in C_(N-2)}.

For Z_1=e, Z_2=c and Z_N=(c,Z_(N-2)), the intertwiner fixes each Z_N.
One application freezes the first cherry and leaves the same K problem
on N-2 leaves. Therefore C_N enters Z_N in at most floor((N-2)/2) steps;
arbitrary trees enter C_N first and reach Z_N in at most floor(N/2) for
N>=3. Sizes one and two are already fixed. This rules out every other
K recurrent state, not merely longer K cycles.

The geometric recursion gives both

    F^2(e,R)=(e,K(R)),
    F^2(T)=K(T) if T has a nonleaf left child.

The second applies before T reaches C_N: both sides equal G(P(LS(T))).
This is essential for the sharp witness. Also G(Z_j)=Z_(j+1), and
F(Z_N)=(e,Z_(N-1)) for N>=3. Thus those two distinct trees are exchanged.
Every first image is either in C_N or has form (e,R). The former takes
at most 2 floor((N-2)/2)<=N-2 further steps. For the latter, the even
representation gives 2 floor((N-1)/2), while the commuting odd
representation G K^t(R)=K^t G(R), with G(R) in C_N, gives
1+2 floor((N-2)/2). For N>=4 their minimum is N-2. Adding the first step
gives N-1=n-2. The triangle is fixed and the quadrilateral consists of
the two-cycle already. The odd-phase improvement is not optional.

For sharpness use S_3=(e,c), S_N=(S_(N-1),e). Its LS is [c,e,...,e],
so F(S_N)=(e,S_(N-1)), K(S_4)=LC_4, and K(S_N)=(c,S_(N-2)) for N>=5.
Put J(S)=(c,S). At N=2k, time N-2 gives J^(k-2)(LC_4); at N=2k+1 it
gives (e,J^(k-2)(LC_4)). In both cases LC_4 differs from Z_4=(c,c), so
the state is outside the appropriate core phase at that time. The upper
bound places it inside at N-1. This verifies all-n sharpness and both
parities, rather than inferring it from the first eight sizes.

## 4. Primary-source access and what it does, and does not, own

Actual multi-query requests and full returned results are in `sources/`.
Seven archived query groups contain 24 queries: literal lexicographic and
snapshot flips; tree sweeps and greedy/zigzag sorting; Pop/rotation and
inverse/fibre terms; UUDU; named primary sources; and 2024/2025/2026 and
180-day filtered searches. The preliminary three-query exploration was
not archived at the instant it ran; its scope was repeated and archived as
group 1. This is disclosed, not a claim that every initial search receipt
was preserved. Unrelated returns and nonhits are not priority evidence.

The following are primary-source comparisons. No secondary search result
is used as a theorem. Read coverage is deliberately not inflated to the
whole article when only relevant sections were inspected.

* [Ajran--Defant, ornamentation Pop (2025 v1)](https://arxiv.org/html/2501.10311v1):
  read sections 1.1--1.3, the model, Lemmas 2.3--2.4, relevant upper-bound
  proof context, and section 4's image criterion and proof; section 5 was
  read only through Lemma 5.2/Proposition 5.3 context. This is a lattice
  meet-of-lower-covers map; its chain specialization is Tamari. Its local
  image constraints and removal mechanism are not imported as OFS results.
  No full higher-image theorem comparison is claimed.
* [Hong, Tamari Pop (2022)](https://arxiv.org/pdf/2201.10030): read the
  introduction/definition and the image enumeration proof portion. Plain
  Pop has the Motzkin image count. An abstract/body indexing discrepancy
  is avoided by independently constructing the actual finite poset maps.
  The paper is not evidence that every rotation/Pop composite was treated.
* [Barnard--Defant--Hanson, torsion/Cambrian Pop](https://arxiv.org/pdf/2312.03959):
  the conference introduction and definitions, and the full-version
  introduction, Theorem 5.1 context, section 5.2's preimage theorem and
  proof, and type-A specialization context were read. Theorem 5.3 concerns
  torsion-class Pop preimages via semibrick data. This is genuinely an
  all-target predecessor precedent, not just a matching image count.
  Applying it to OFS would require an actual commuting dictionary to that
  map; the same-carrier obstruction below applies. Most of the 50-page
  representation-theoretic article was not read, and no claim rests on it.
  The attempted v3 HTML URL returned 404; the actual PDF was accessible.
* [Defant--Williams, Coxeter Pop-Tsack Torsing](https://alco.centre-mersenne.org/item/10.5802/alco.226.pdf):
  read the introduction and map definition in the primary published PDF.
  The operator w -> w pi_T(w)^(-1) is on a Coxeter group. Noncrossing
  inputs map to the identity, so simply identifying triangulations with
  Catalan objects does not yield the OFS step. No full-body classification
  or exclusion of an enlarged Coxeter encoding is claimed.
* [Pallo, rotational tree structures (2006)](https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf):
  read sections 1--3's dictionaries, uniquely selected leftmost rotation,
  and monotone weight update, plus section 4's path/join algorithm context.
  The selected weight reaches its maximum and stays there. This owns a
  deterministic fan-building rotation and a prefix-fixing proof primitive.
  It does not state OFS's whole original-snapshot update or its recursive
  one-step source sets. The remaining distance analysis was not used.
* [Bose--Lubiw--Pathak--Verdonschot, edge-labelled flips](https://arxiv.org/html/1310.1166):
  read sections 1--3 through the canonical fan and sorting construction,
  and section 4's sorting-model simulation and proof. Flip labels are
  inherited by the inserted edge. This gives the exact elementary lift
  discussed below. Their sorting construction returns selected edges and
  sorts persistent labels; it is not a theorem about repeated erase-and-
  reset snapshots. Later spiral/combinatorial sections were not used.
* [Mansour, Statistics on Dyck paths (2006)](https://cs.uwaterloo.ca/journals/JIS/VOL9/Mansour/mansour86.pdf):
  read the pinned primary text through section 2.1's first-return argument,
  Theorem 2.5 and Corollary 2.1. The displayed UUDU specialization agrees
  algebraically with the old count. The pinned rendered Table 1 was also
  actually viewed: its alpha_2 zero column prints 10 and 26 where the
  displayed series gives 9 and 22. Those table entries are excluded. The
  entire static series is deducted despite this source inconsistency.

OEIS A105633 is discovery only. Ordered-trees/inorder and 2-binary-tree
papers remain author/desk abstract or discovery leads; their bodies were
not read by this assessor and no applicable theorem is asserted. The
Stout--Warren title query did not supply a primary body; no reading or
complete adapter is fabricated. No external Codex-MCP reviewer, Zotero or
Obsidian search tool was callable; no unavailable call, upload, purchase,
specialist contact or external API review was invented. The installed
proof-writer, novelty-check and research-lit instructions were applied
under the repository's model and HOLD_EXTERNAL overrides. This independent
assessment is the authorized process-separated fallback, not a fictitious
external review certificate.

## 5. Complete adapters and explicit value deductions

### Same-carrier Pop compositions: stronger than nonconjugacy

For the usual oriented flip poset, direct lower ideals and upper filters
compute Pop-down as the meet of all lower covers (including the input)
and Pop-up dually. No author data or source formula is loaded. Their
ranks on n=3,...,10 are 1,1,2,4,9,21,51,127, whereas F has ranks
1,2,4,9,22,57,154,429. Complete maps, not only totals, are in the canonical.

For finite same-carrier functions, rank(A P B)<=rank(P), regardless of
whether A and B are rotations, reflections, other permutations, arbitrary
functions, or longer compositions. Thus **every** composition containing
one of those Pops on the complete same-sized carrier is excluded in each
tested size n>=4. In particular the quadrilateral already rules out a
uniform such formula for the full n>=4 family. This is not an all-n rank
inequality claim beyond the declared boxes. Plain descending Pop and its
powers also cannot be conjugate to an OFS two-cycle. Neither argument
excludes a map on a larger carrier followed by projection, a different
poset, a size-dependent exceptional construction, or a phased extension.
The residual verdict below does not pretend otherwise.

### Exact edge-labelled lift: map-primitive credit is zero

There **is** a complete elementary composition, not merely an analogy.
Give the original diagonals labels 1,...,n-3 in their lexicographic order;
let tau_i flip the edge carrying label i and transfer that label to its
replacement. Write E for forgetting edge labels and R for the initial
lexicographic labelling section. Then

    F = E tau_(n-3) ... tau_1 R.

The reason this is exact is that a flip of a different label leaves the
edge with label i untouched until tau_i. Every tau_i is an involution on
the larger labelled carrier; the composition is bijective there. E and
the repeated reset R remove that invertibility. Thus noninjectivity of F
does not exclude this lift, and **the ordered-flip scheduler and its
representation as a composition receive no standalone originality credit**.
The cited labelled-flip results prove reachability/distance and sorting
with persistent labels; they do not evaluate intersections of this
particular labelled image with the reset section, nor repeated E/R
iteration. The actual protected-cell and inverse lemmas supply that work.
This exact adapter therefore deducts the primitive without eliminating
the submitted two-axis theorem.

### Static inverse primitives: fully deduct the counted cuts

Once the source-set bijection in section 2 is established, all scalar
factors of h follow from independent binary cuts and recursive products.
Their powers-of-two values, species equation and Catalan substitution are
old mathematics. A balanced-parenthesis language can of course implement
the same grammar; calling it a new regular-language method adds nothing.
The precise remaining inverse content is the geometric identification
of which seed and G blocks are admissible and which **labelled polygon
source** each choice produces, including l=1, l=2, comb and zero cases.
The strict exponent budget gives the specific unique fan attainer, not
a claim that binary-composition maxima are themselves new.

### Historical maps: compare the actual mechanisms

The root-relative input and history pin lists identify every inspected
original. Specific proof sections, not completion tables, were read.

| Original | Complete relevant transfer deducted; limit of that transfer |
|---|---|
| P144, `papers/144-leftmost-dyck-reassociation/main.tex` | Its primitive-factor iterate and terminal source proof give one source at each feasible depth by lifting a suffix of root children. Graft/lift, Catalan coding, factor clocks and deterministic leftmost scheduling receive zero credit. That endpoint map is not OFS's one-step map: the old inverse moves one terminal suffix, whereas OFS requires a recursively chosen seed and later blocks at many decorated cells. A shared contour dictionary alone does not transport those source sets or the alternating phase. |
| P90, `papers/90-rule184-particle-periodic-zeta/main.tex`, and the graph-matching GCM section of `docs/papers162_166_sequence/scouting/open_fresh_p167/SCOUT.md` plus its collision firewall | P90's hard-core traffic/min-plus clock and GCM's old 2->11, 1-run->2-pairs map supply regular run parsing, independent placements, moving defects and prefix stabilization. Their flat word inverse and conserved/transported occupancy information are deducted. Neither original supplies the recursively size-varying OFS cell map or the K square identities. No distinction is inferred merely from the carrier's name; the inverse structure and clock transport are the comparison. |
| Q09 least-ear, C14 parity-selected diagonal, TFE rooted-fan frontier, LDL illegal Delaunay, PTR polygon rotation | Their original selector definitions were read in the pinned scout files. Local ear selection, a fan-building sweep, greedy improvements and rotations are owned primitives. Iterating a local selector with a dynamically refreshed order is not the fixed original list; the exact label-reset lift above explicitly accounts for the composition that does exist. No separate credit is awarded to having selected another order. |
| P139 factor-start feedback | Selected original static suffix-record/factorization and leading-prefix proof sections were read. The owned factorization dictionary and prefix-amplification strategy are deducted. They are not a literal inverse or K transport for the triangulation sweep. No claim of rereading its entire paper. |
| P202 ternary ordered reset | Original setup and inverse/theorem proof sections were read. Its independent 0/1 source choices show why powers-of-two fibres are not a new axis by themselves. Those choices do not reconstruct the OFS recursive source blocks or determine its phase clock. |
| P204 and P206 adverse A source/proof reports; MNC candidate gate | Their actual descent/template and coloured-tail reductions were read. They exemplify complete adapter kills, and generic prefix/record templates are deducted here too. No such whole OFS adapter is asserted merely because its clock also freezes a prefix. |
| UGR gate, P205 and P207 proof packages | UGR's actual full sign-fibre union demonstrates that transferring each stratum is not automatically transferring a global extremal theorem. The actual activation-graph P205 and strict ternary-rank P207 maps are unrelated literals; their finite termination and periodic-state bookkeeping supply no OFS source decoder. No additional family seat is claimed from common proof tools. |

The historical alias GCM here is graph matching, not the unrelated Gram
cube abbreviation. The old comb-parity root-rotation report was also
inspected; its parity-Catalan adapter failure/kill is retained and does not
turn OFS into a parity variant. This is a mechanism audit of the named
relevant originals, not a declaration that every historical manuscript
was reread or that the history's numbering anomalies were repaired.

### Surviving conjunction and limits

After the exact labelled lift, all static enumeration/cut factors, ordinary
rotations and generic prefix freezing are deducted, the meaningful
candidate conjunction is:

1. The all-target labelled **source-set** decoder and its recursive
   zero/comb/seed boundary analysis for this reset sweep, with the sharp
   unique fan extremum as a consequence.
2. The exact geometric-to-K square transport, stronger closed-class
   inclusion and commuting odd phase that yield the **complete** unique
   two-cycle and the sharp all-size n-2 clock, with both witness parities.

These are not granted on the basis of a no-hit search or plain rotation/
Pop nonconjugacy. They require the actual lemmas reconstructed above after
the complete primitive adapters have been applied. None of the inspected
applicable primary or historical results supplies that conjunction under
an explicit commuting dictionary. This is a bounded mathematical/value
judgment supporting internal candidate development, **not proof of priority
or a classification of every possible composite adapter**. A later exact
owner or full two-axis reduction reopens the value finding. Repackaging
the image series, binary choices, deterministic scheduler or generic
prefix clock as separate contributions would violate this narrow gate.
