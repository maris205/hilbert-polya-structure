# P208 B: independent proof attack and bounded source subtraction

2026-09-06 UTC. Actual distinct nonauthor `/root/p208_b_reviewer`.
MATH_VALID / GO_NARROW_TWO_AXIS, on immutable Round 1. This is the initial
review, not an accepted delta or an external-specialist opinion.

## Identity, chronology and independence

The reviewed carrier is all triangulations of the convex n-gon with fixed
cyclic labels 0,...,n-1, n>=3. Each iteration snapshots the n-3 original
internal diagonals, orders endpoint pairs lexicographically, and flips
each original exactly once in the current triangulation. The snapshot is
not refreshed within a sweep. The root is (0,n-1); N=n-1 leaves and
m=n-2 internal tree vertices are not interchangeable size variables.

The 487 Round1 referents and their manifest were pinned first. The initial
kernel and design were pinned at 12:11:33 UTC, before any manuscript proof
or author/A scientific code was read. `initial_kernel.py` enumerates
crossing-compatible chord bitmasks, uses cyclic-quadrilateral flips, and
reconstructs all sources by reversing the original scheduler. It is not
the author's nested-tree enumeration or A's face/BFS carrier. The first
actual execution passed before the later proof/code reads.

After this freeze B read the entire manuscript (all eight sections), the
entire 450-line PROOF_PACKAGE, the author scientific original and canonical,
and A's scientific original, source/proof report and canonical. B neither
ran nor imported those scientific implementations. `verify.py` retains
the initial independent kernel verbatim and adds labelled interval-span
pressure on the manuscript's structural identities. That second layer
uses the same F/G/P/K reductions, and its parser is a fresh implementation
of the stated decoder; it is not a claim of an unrelated all-size proof.
The full-payload comparator reads data only after the independent producer
exists. Build/recording infrastructure was informed by earlier recorders;
this is explicitly infrastructure reuse, not mathematical independence.

No candidate-gate or author's proof was contributed to by this reviewer.
No repair lemma, manuscript edit, child reviewer, external model API,
manuscript upload or specialist contact occurred. The installed review
skill's old provider/model defaults were replaced by the project's actual
current-model distinct-process fallback; no unavailable provider was called.

## Independent reverse-scheduler proof

Number all internal chords in endpoint-pair order. At a reverse step, flip
a currently present chord g into a prospective original e; require e's
index to be smaller than the previous restored index, and prohibit
removing any already restored original. After n-3 such steps require the
current triangulation to equal exactly the set of restored originals.

Every genuine forward trajectory reverses to such a history: flips are
involutions and its original indices strictly increase forward. Conversely,
the terminal equality says that the recovered triangulation's entire
original agenda is exactly the restored set. Reading the reverse history
backward therefore executes its original agenda in increasing order and
reaches the target. A recovered source fixes that deterministic agenda,
so two different accepted histories cannot produce the same source.
This gives an independent necessity, sufficiency and no-duplication attack
on complete source sets. It searches reverse histories, unlike the paper's
more efficient carrier-free recursive decoder; B does not claim to replace
the paper's contribution with a new paper theorem.

## All-size manuscript deductions, including failure-prone boundaries

### Protected cells and output shape

A flip removes only the diagonal visited. All unvisited originals remain.
The inserted diagonal crosses the removed original, so it could not have
belonged to the original noncrossing set. It is never scheduled later.
This proves protected boundaries without assuming the desired recursion.

At a nonear vertex 0, its consecutive original fan edges are the first
scheduled group. After the i-th flip the new fan edge is (1,a_(i+1)); the
preceding flip supplies the triangle (0,1,a_i). The protected complement
has seed cell (B1,B2), then cells (e,Bj). Critically, the original root
edge of every nonleaf Bj is in its cell's remaining agenda: treating only
proper descendants as scheduled would give a different map. Increasing
relabelling preserves both endpoints' comparisons. Cells cannot affect
one another across protected edges, so their possible interleaving does
not change the separate smaller sweeps. Leftmost-leaf gluing is exactly P.

For an ear at 0 and B=(e,C), flipping (1,n-1) inserts protected (0,2).
Contracting that triangle leaves precisely G(C), then expansion replaces
its first leaf by c. For nonleaf-left B, the successive 1-fan flips and
the last (1,n-1) flip leave a cherry over P(LS(B)). The triangle has no
agenda. These cases establish all displayed F/G/P equations by strictly
smaller-cell induction, including F(e)=e, F(c)=c and G(e)=c. They also
establish the comb-left F shape and the stronger left-length>=2 G shape
for nonleaf input, rather than postulating them from enumerations.

### Every inverse branch and the source-set bijection

Noncomb root-left targets have no F or G source by that shape theorem.
A comb target cannot arise from a P seed because P's output is nonleaf;
stripping forced leading leaves therefore ends at the unique right-comb
source, with the G source one leaf smaller. This includes the small bases.

For a target (e,R) with R nonleaf, G has no source. F must come from the
nonear branch and is exactly Fold(Lists(R)). At (c,R), the G ear-one
branch would require the excluded smaller G-output (e,R), so only the
ear-many branch survives; F adds one leading leaf. At longer left combs,
only ear-one can enlarge the left comb and each reduction removes exactly
one source wrapper. This proves every row simultaneously and shows why
the G l=1 exception must not be quietly counted.

For list reconstruction, LS(iota(S,A))=LS(A) followed by LS(S).
Cutting LS(R) into consecutive nonempty blocks thus recovers a seed
F-output and subsequent G-outputs. The seed inverse is a genuine ordered
pair. Every source list determines its seed and every later branch;
their output-spine lengths determine all cuts. Consequently different
cut/source choices cannot collapse to one list. Forced wrapper cases are
disjoint. Recursion terminates because Lists(R) only uses inverse targets
of at most |R| leaves while its enclosing target has strictly more.
Ordered intervals recover actual endpoints, with no rotation/reflection
quotient or unlabeled multiplicity hidden in the count.

### Gap evaluation and all equality cases

Each nonleaf decoration must end its block. A seed may have no leading
leaf, but a later decorated block must have at least one. Therefore a
zero internal leaf gap kills every cut. A positive gap of length a has
one choice when wholly absorbed plus 2^(j-1) choices for a remaining
nonempty composition of length j; their sum is 2^(a-1). Empty leading
and trailing gaps have one choice, not a negative exponent. An all-leaf
list of length a has 2^(a-1) cuts. Independent boundary/gap factors and
smaller decoration factors give exactly h, including recursive zeros.

For r>=1 decorations and total A gap leaves, q(R)=A+r+sum q(Dj).
The gap exponent is <=A and each positive decoration contributes at most
q(Dj)-1. Thus log2 h(R)<=q(R)-2r<q(R)-1. Zero h cannot attain the
positive upper bound. Equality h(R)=2^(q(R)-1) occurs exactly for a
left comb. In a target (LC_l,R) of internal size m, q(R)=m-l. A leaf
right child gives only one source. For m>=3 the maximum 2^(m-2)
forces l=1 and R=LC_m, precisely the labelled fan at 1. At m=1,2 every
target has one source; the manuscript correctly does not claim unique
attainment there. This is a strict whole-target comparison, not merely
the observation that several fibres are powers of two.

### K, strong closure, and the two different sweep phases

For a>=2, let Da(R)=iota(G(R),LC_(a-1)). The all-leaf prefix in the
protected-cell product gives F((LC_a,R))=(e,Da(R)) and
G((LC_a,R))=(c,Da(R)); a=2 includes G((c,R))=(c,G(R)).
Writing G(B)=(LC_l,Q) defines K(B)=Dl(Q). Then G²(B)=(c,K(B)),
also for B=e; two added leaves cancel the prefixed cherry, so K preserves
size. Computing G³ in its two associations and canceling the common
cherry proves KG=GK. Applying the a=2 identity twice proves
K((c,R))=(c,K(R)). These are equalities, not inferred commutations.

For the first closed inclusion, Q nonleaf supplies a nonleaf root comb
in G(Q), which substitution cannot shorten; Q=e gives LC_l, and size
N>=3 forces l>=3. For T=(LC_a,R) in C_N, K(T)=G(Da(R)). When
N>=4, Da(R) is in C_(N-1); applying the same comb action yields
(c,Ds(Q)), and its right child is in C_(N-2). The leaf-Q case uses its
actual size, not a nonexistent general nonleaf argument. At N=4 that
child must be c. At N=3 the sole closed state LC_3 is fixed and its
right child is e. Thus the stronger inclusion holds at both boundaries.

The cherry-transport equality freezes one cherry while K continues on
the right child. Induction gives the class clock floor((N-2)/2), and one
initial entry gives the global clock floor(N/2); e,c are fixed separately.
Every K orbit therefore reaches the single recursively defined Z_N.

The first sweep-square identity is F²((e,R))=(e,K(R)). For arbitrary
nonleaf-left T, not merely a comb-left tree, put P_T=P(LS(T)); then
F(T)=(e,P_T), G(T)=(c,P_T), and G²(T)=(c,G(P_T)), proving
F²(T)=K(T). This unrestricted clause is needed for the sharp witnesses.
The core action G(Z_j)=Z_(j+1) and F(Z_N)=(e,Z_(N-1)) follows from
the cherry equation and the bases. For N>=3 these are distinct root phases.

Every first image is in C_N or is (e,R). The closed phase costs at most
2 floor((N-2)/2). In the leaf phase, even iterations cost at most
2 floor((N-1)/2), but the odd representation is also essential:
F^(2t+1)((e,R))=G(K^t(R))=K^t(G(R)). The latter starts in C_N,
giving 1+2 floor((N-2)/2). The minimum of the two bounds is N-2.
Adding the first-image step gives N-1=n-2. The complete N=2,3 carriers
are respectively the fixed cherry and the two-cycle, so their entrance
maxima are zero. Convergence excludes every other recurrent component.

### Sharpness retains the final unit in both parities

Use S3=(e,c), S_N=(S_(N-1),e), J(S)=(c,S). Its spine has first
decoration c followed by leaves; the seed is S3 and each later G(e)=c
appends a right leaf. Hence F(S_N)=(e,S_(N-1)), K(S4)=LC4, and
K(S_N)=J(S_(N-2)) for N>=5. The established KJ=JK and GJ=JG
then transport the exact tails.

At even N=2k, time N-2 has tail J^(k-2)(LC4). It is in the nonleaf
root phase and differs from Z_N because LC4 differs from Z4=(c,c).
At odd N=2k+1, time N-2 is (e,J^(k-2)(LC4)); the root phase excludes
Z_N, and the same LC4/Z4 difference excludes the other core member.
Both are still outside at N-2, while the upper bound enters by N-1.
No even-only argument, unproved final step or experimental extrapolation
is needed. B supplied no new lemma to make this work.

## Primary bodies actually read and exact limits

Exact downloaded PDFs, layout texts, tool commands, hashes and web receipts
are retained under `sources/`. Downloading six complete files does not
mean reading six complete papers. Locators below refer to the retained
layout text and named mathematical statements, not certified PDF line
numbers. No secondary source is used to supply a theorem.

| Primary source | Actual B read scope and what it owns |
|---|---|
| [Bose–Lubiw–Pathak–Verdonschot, arXiv 1310.1166v2](https://arxiv.org/pdf/1310.1166v2) | Text lines 1–130, 190–307, 590–674: persistent edge-label transfer, canonical-fan/sorting context, local sorting simulation and its proof context. No complete later spiral/combinatorial-triangulation read. Published metadata separately verified in the publisher search return: Computational Geometry 68 (2018), 309–326, DOI 10.1016/j.comgeo.2017.06.005. Reversible edge-labelled flips and their composition are prior. |
| [Pallo, published Acta Cybernetica PDF](https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf) | Lines 1–245, opening through tree/triangulation weights, selected rotation, invariant maximal coordinate and surrounding proof. The full later distance/join theory was not read. This owns the Catalan dictionary, selected-rotation and permanent-coordinate primitives. The published first page verifies Acta Cybernetica 17 (2006), 799–810. |
| [Hong, arXiv 2201.10030v1](https://arxiv.org/pdf/2201.10030v1) | Lines 1–135 and 396–551: introduction's literal meet-of-lower-covers rule, theorem statements, and Theorem 4.7's image criterion with its full proof. No full Section 3 or full final weighted enumeration proof is claimed. The abstract/body Motzkin shift is not imported as an OFS count. Published metadata separately verified: Advances in Applied Mathematics 139 (2022), 102362, DOI 10.1016/j.aam.2022.102362. |
| [Barnard–Defant–Hanson, arXiv 2312.03959v1](https://arxiv.org/pdf/2312.03959v1) | Lines 660–725, 1670–1830, 2070–2090: full Theorem 5.3 inverse characterization and proof, full Theorem 9.6 bound proof and adjacent scope caveat, final Theorem 9.17 statement and concluding proof dependency. The intervening extremal-witness construction and full representation theory were not read. These own substantial inverse and clock results for torsion/Cambrian Pop, not merely static Catalan counts. |
| [Ajran–Defant, arXiv 2501.10311v1](https://arxiv.org/pdf/2501.10311v1) | Lines 1–174 and 320–525: model/introduction, Section 3 rank/height bounds and extremal proof, and Section 4 Lemma 4.1 plus Theorem 4.2 image criterion and explicit-preimage proof to its end. Section 5 was seen only at its opening, not its full higher-image theory. Precise v1 is used; no unverified later publication is asserted. Local inverse construction and sharp lattice-Pop clocks are prior methods. |
| [Mansour, Statistics on Dyck Paths](https://cs.uwaterloo.ca/journals/JIS/VOL9/Mansour/mansour86.pdf) | Published first-page metadata and lines 272–346, Theorem 2.5 proof, Corollary 2.1 and its displayed UUDU specialization. Journal of Integer Sequences 9 (2006), Article 06.1.5 is verified from the original. No complete paper or disputed-table visual inspection is claimed; the displayed formula, not a table guess, supplies the static subtraction below. |

Web query families covered literal snapshot/lexicographic sweep and
triangulation reset, selected/tree rotations, Tamari/Cambrian Pop inverse
and clock, ornamentation Pop, and UUDU avoidance. Returned secondary and
irrelevant hits are retained but are not theorem evidence. A further
orbit-conjecture hit was only an indexed abstract/metadata lead, not a
new body read. Nothing here is a global or exhaustive priority clearance.

## Complete deductions and limits of transfer

Give the initial diagonals persistent labels 1,...,n-3 in their endpoint
order using R; let tau_i flip the edge currently bearing label i and
transfer its label; erase all labels using E. Then
F=E tau_(n-3)...tau_1 R. Before its turn an original edge cannot have
been removed by another labelled flip, so this is an exact adapter on
every labelled source. Each tau_i is an involution. Noninjectivity after
reset/erasure does not refute this larger-carrier lift. The schedule,
resetting, reversible primitive and their composition receive zero credit.

For the static image series, the proof package gives
I=1+z/(1-z)^2 C(z²/(1-z)^3). Eliminating C using C=1+wC² yields
(1-z²)I=1+z(1-z)I². Mansour's displayed
A=C(z/((1-z)(1+z)^2))/(1-z²) satisfies exactly the same equation:
substitute C=(1-z²)A and cancel the explicit factors. Both constant
terms are 1, and the positive-degree coefficients are recursively fixed,
so the full formal series agrees. This deducts the whole static series,
not just several coefficients. It does not identify the literal OFS
image with standard-Dyck UUDU avoidance; the historical false identification
and counterexample remain preserved. The paper does not claim it.

At the quadrilateral, descending Pop on the two-element Tamari chain
sends both elements to its minimum, while OFS exchanges them. This rules
out direct conjugacy there. It does not rule out composites, resetting,
larger-carrier encodings, other ranks, factors or arbitrary time changes.
No unseen general Pop theorem is claimed to have been excluded. The
published inverse/clock precedents above are substantively deducted as
methods; the surviving assertions require the specific OFS cell adapter,
source restrictions, strict whole-target comparison and two-phase K law.

## Exact historical audit, with machine/read separation

`history_context/SEARCH_SUMMARY.json` records an actual search across
1,263 manuscript TeX files covering the 201 available paper numbers below
208 (1–50 and 57–207), plus 654 scout Markdown files: 1,917 inputs total,
two literal/mechanism regex families, 329 matching files snapshotted.
Every input was hashed before/after unchanged. This was a machine search,
not a claim to have read 201 full papers; absent numbers 51–56 are not
silently treated as searched manuscripts. Selected exact originals below
were then read. Source-context snapshots preserve them separately.

| Original actually inspected | Subtraction and precise nontransfer |
|---|---|
| P144 `main.tex`, full original including primitive-factor update, iterates and terminal depth-source proof | Leftmost grafting, factor-count clock and unique lifted suffix description are occupied. Its fixed endpoint and terminal inverse do not identify the recursively decorated complete one-step OFS sources or prove the alternating K transport. |
| P90 `main.tex`, lines 1–212 through complete sharp min-plus entry proof; GCM `open_fresh_p167/SCOUT.md`, lines 1–230 | Conserved traffic layers, moving-defect clock, run decomposition and regular matching parser are occupied. GCM means graph matching here; its 2->11 and paired-one-run rule is not a tree-cell transport law. No full P90 later orbit-enumeration reread is claimed. |
| Full `COMB_PARITY_ROOT_ROTATION_REPORT.md` | Its comb/parity-dependent one-root rotation, short cycles and extremal fibres are concrete prior controls. Root surgery, parity effects and period two alone receive no OFS credit. Its fixed-radius root move is not identified with a sweep over all original edges. |
| Q09 original scout lines 547–623; C14 scout lines 1–68; TFE/LDL scout lines 1–100 | Least-ear opposite edge, parity-selected single edge, refreshed root-frontier fan building, illegal Delaunay legalization and polygon rotation own the selector/flip/sorting primitives. Choosing another deterministic order alone is not new value. Their literal agendas differ; the exact label-reset composition that does apply is deducted above. |
| P139 `main.tex` lines 34–120; P202 `main.tex` lines 30–150 | Lyndon-factor prefix amplification and ordered-reset forbidden-target/binary-choice decoding are occupied. Static factorization, prefix growth and powers of two are zero-credit. These selected sections do not supply the nested labelled OFS source parser or its K phase law; neither full manuscript is claimed read. |
| P204 setup and full fibre section; P206 full dynamics section | Position-flagged ascent/block inclusion–exclusion, bounded collapse and explicit core involutions are concrete prior templates. Generic fibre products, recurrent pairs and post-collapse clocks are zero-credit. P208 claims neither an all-time fibre atlas nor P204's flagged-statistic transport. |
| MNC gate `SOURCE_AND_PROOF.md`, full original | The full tail adapter enters the labelled pair (p,D) after two steps and evolves as (ECA36(p),D). This explicitly kills frozen-colour pulse erasure as a fresh temporal engine; a short sharp front end does not restore it. No analogous complete adapter reducing the OFS K transport to that mechanism is asserted. |
| UGR gate `SOURCE_AUDIT.md`, full original | Its complete disjoint union of TCSD sign fibres deducts whole inverse enumeration but does not automatically transfer a maximum of one stratum to the sum. This guards the same distinction here: all binary factors are old, while the strict OFS whole-target equality proof is actually checked. The gate's inaccessible external bodies are not claimed newly read by B. |

Earlier false-image and naive-fibre-exponent guesses are not rescued by
present agreement. Historical manuscript numbers and failed scout packages
were not changed, repurposed as reviews, or erased. The search excludes
neither every nonlocal encoding nor every undiscovered direct source.

## Decision

No mathematical, contribution-scope or manuscript-artifact defect remains
open. Two narrow theorem-level axes survive the inspected complete
adapters: (1) every labelled one-step source with its evaluated boundary
cases and unique fan maximum, and (2) the exact K-mediated recurrent core
and sharp length-dependent two-phase entrance. They share a geometric
dictionary but require different substantive deductions. Static image
enumeration, binary choices, reset composition and generic prefix freezing
are not additional axes. An applicable prior theorem or complete adapter
must reopen the affected judgment. OWNER_AMBER / HOLD_EXTERNAL continues.
