# Frozen candidate — triangular divisibility-mutation maximal paths

Candidate ID: `ANG-20260920-TDP01`.
Paper ID: `328-triangular-divisibility-paths`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL PATH OWNER AND RETURN-TIME RANGE`.

## 1. All integer vertices and actual deduplicated adjacency

Let V=N_(>=1)^3. At v=(a_1,a_2,a_3) and i in {1,2,3},
let j,k be the other coordinates. Permit i exactly when
a_i divides N_i=1+a_j*a_k. Replace only a_i by N_i/a_i,
calling the resulting vertex R_i(v). Set N(v)={all actual R_i(v)}
and D(v)=|N(v)|. Distinct coordinate instructions with the SAME resulting
vertex create only one neighbor. Keep a genuine self-edge once when
it occurs. No extra self-edge is added; immediate backtracking is allowed.
All units, composite entries and coordinate orders remain. Recompute adjacency
from the actual new vertex, not a static tested integer or
an external port. Symmetry/involution and degree properties are obligations, not assumptions.

## 2. Entire maximal-path carrier and deterministic partial shift

P_infinity consists of ALL legal one-sided infinite vertex paths. For each
L>=0, P_L^term consists of ALL legal L-edge paths ending at
a vertex of degree0. Freeze P as their disjoint union. Each
finite layer is discrete; P_infinity has the restricted discrete-V product
topology; use the disjoint-union topology and Borel structure. No selected
nonbacktracking/periodic subspace or finite cutoff replaces P.

A nonterminal finite prefix is NOT another completed state: no spontaneous
stopping. A degree0 vertex has its unique length-zero terminal, not an
absorbing loop, reset or cemetery point. Every actual incoming history remains.
T deletes the first vertex on infinite paths and finite paths with
at least one edge. Length-zero terminals have identity T^0 but no step.
The full path, not the multivalued vertex graph, is the deterministic state.

For any legal finite prefix alpha, C(alpha) is the set of
ALL completed finite/infinite paths extending it. At a terminal-ending prefix
it is that finite-path singleton. Put P(v)=C(v). For each
actual edge u->v prescribe the complete inverse

    I_(u,v):P(v)->C(u,v), add u before the full target path.

Given a target's first vertex v, propose all old u by
testing each i with v_i|(1+v_j*v_k), restoring
u_i=(1+v_j*v_k)/v_i, keeping other coordinates, checking v in N(u),
and deduplicating the actual u. Prove exhaustiveness, both inverse identities,
exact image and all terminal boundaries. Missing-inverse objects are not deleted.

## 3. One fixed path measure and full-point IMAGE prescription

Give every root P(v) mass1. At D(v)>0 choose uniformly among
its ACTUAL distinct next neighbors; at D(v)=0 assign the mass
to its unique length-zero terminal. Precisely prescribe

    mu(C(v_0,...,v_r))=product_(0<=j<r) 1/D(v_j).

Use the sum over ALL roots. Establish existence and the full
Borel law, including finite/infinite paths, atoms and null configurations. No
nonatomic/conull selection is authorized. Root mass1 and uniform actual-neighbor
probabilities are DECLARED DESIGN, not a canonical natural A0 claim.

For I_(u,v), freeze the all-point constant-on-domain candidate version

    J_(u,v)(z)=mu(C(u,v))/mu(P(v)), z in P(v).

Prove mu(I E)=integral_E J dmu for EVERY Borel E subset
P(v), not only the whole-cylinder ratio. Prove finite prefix-pair IMAGE
and compatibility under actual refinements/compositions. The same version must hold
at every null returning path; do not choose a new density
there or evaluate a missing terminal step. No numerical ratios are preassigned.

## 4. Whole retained-lag owner, full time and primitive convention

Freeze G_T={(z,m-n,w):m,n>=0,T^m z=T^n w,both histories legal},
source w, range z, with Borel structure from P x Z x P.
Same triples one arrow. No additional coordinate labels, free histories,
germ quotient or graph reversal identification. For the actual inverse
B_z:Tz->z set kappa(z)=-log J_Bz(Tz),
S_m(z)=sum_(0<=i<m)kappa(T^i z), S_0=0, and

    c(z,m-n,w)=S_m(z)-S_n(w).

Prove pointwise descent/additivity with correct direction, including terminal identity.
Keep ALL P x R_h, arrows (w,h)->(z,h+c), and all
real translations in h. No operation-count time or independently inserted roof.
Only set/Borel quotient statements initially; no Hausdorff/smooth coarse flow,
invariant mu dh or embedded-circle theorem is presumed.

Use ENTIRE source isotropy G_z^z, H_z=c(G_z^z), and extension
kernel. A positive primitive requires the entire H_z=LZ with LEAST
L>0. Repetition traverses that SAME packet. All ancestors, phases, terminal
objects, self-edges, backtracks, zero-clock and nonperiodic paths remain. Equal
times or roots do not merge packets; cyclic phases merge only
when actual shift/tail arrows say so. No selected incoming representative.

## 5. Exact prime-symbolic lineage and type limits

For n>=2,d>=1, the vertex v(n,d)=(d,1,n-1) has first-coordinate
permission exactly d|n. Proper part1<d<n is the original observable,
not a restriction. Use the WHOLE P(v(n,d)), retaining every
other legal coordinate mutation. The specific arrow is

    divisor admissibility -> a_i*a_i'=1+a_j*a_k
      -> current actual adjacency -> new-vertex adjacency feedback
        -> all maximal paths with their own measure-time owner.

This is a declared symbolic deformation, not a Logistic/Henon conjugacy.
No prime selector, table, log-prime assignment, passive real scale or zero
data. Constant1, triangular structure, deduplication, path completion and probability
are designs; stronger naturalness and geometric realization OPEN. Classical symplectic
base, mapping torus and positive classical roof NOT APPLICABLE.

## 6. Three independently owned controls

Each keeps ALL V but reconstructs its OWN adjacency, maximal-path source,
topology, terminals, root-mass1/uniform-neighbor measure, inverse IMAGE, lag and packets.

ROUNDED-INTEGRALITY-OFF: allow every i and replace a_i by
max(1,floor((1+a_j*a_k)/a_i)), deduplicating actual targets. For target v,
enumerate all i and EVERY positive q such that
max(1,floor((1+v_j*v_k)/q))=v_i; restore u_i=q with other
coordinates v_j,v_k, check actual adjacency and deduplicate. No inverse cutoff.

CONSTANT-OFF: permit exactly a_i|a_j*a_k and replace a_i by
a_j*a_k/a_i. Proposed inverses restore u_i=v_j*v_k/v_i when integral,
check the actual reverse edge and deduplicate. Keep all genuine self-edges.

SINGLE-COORDINATE: only i=1 of main's actual formula/permission is allowed.
All vertices remain, not a choice of fixed other coordinates. Rebuild
its own missing-edge terminals and complete prefix inverses. No main domain,
degree, measure or clock is transferred to any control.

## 7. Range-first gate, finite controls and review sequence

First establish complete owner/measure/IMAGE. Then audit the FULL possible return-
time range forced by actual degrees, with entire isotropy and repetition,
before any general self-edge/two-cycle or higher-cycle census. A decisive arithmetic
range obstruction ends target promotion; do not tune weights or restrict paths.

Root names these finite witnesses BEFORE freeze, supplementing the author's
range-first proposal without changing any object: v=(1,1,1), w=(2,1,1),
f=(2,1,3), u=(2,2,1), t=(2,2,2), h=(3,2,4).
For main and EACH own control test the proposed words v,w,v,w,...;
f,f,...; w,u,w,u,...; h,h,... and root t's outgoing status.
First check legality: an illegal infinite word is not a retained source.
For legal periodic words prove least source period, FULL H/kernel and
ALL incoming paths/phases, not just the selected core. These are short
ownership/positive/negative controls, NOT an all-cycle enumeration. Generic exact
path/atom/isotropy classifications may resolve a whole obligation at once.
Other cycle realization/multiplicity remains OPEN after a decisive range result.

Root owns all files except evidence/independent-review.md. Reviewer reads ONLY
this original card, personally derives main+ALL controls without auxiliary work,
then sends metadata-only ALL raw ready. Root locks a first paper
before ANY raw mathematical receipt; explicitly releases ALL raw through FINAL;
then separately unlocks paper for synthesis/adverse and the final report.
ARS three checkpoints are inherited-runtime/shared-history NOT_CALIBRATED internal
scrutiny, not external peer review, blind ideation or independent-error evidence.

## 8. Definition provenance and authority

Root read the complete204-line327 frontier, including the pending definition
and later original-author QA; its source lock and completed327 proof remain
unchanged. Original author read136-card1–36 and312-card1–84, not EOF/outcome
bodies; heading exposure included outcome titles37/182. The old totals61/230
are root metadata, not author-attested counts. Later QA read ONLY then-
327-frontier51–179, restoring explicit m,n>=0, S_m and changed CONSTANT-OFF
permission, not new rules. No old paper/review or current327 science
entered its source delivery; no web, numerical work, write or auxiliary.
Root's previous definition reads1361–36 and3121–82 were likewise partial with
outcome-heading exposure. Related path/exchange structures are acknowledged; no global
novelty, nonconjugacy or theorem transfer is asserted. Shared history remains.

T0--T3 are owner labels; formal UNASSIGNED; B NOT INVOKED. T3
NOT SUPPLIED. Markdown only; no PDF/LaTeX, publication/upload or Git
staging/commit. Positive304, partial-positive320 and older packages unchanged;241/242
paused; programme goal active. Preserve original prefix and all scoped findings.

## Appended outcome — original177 lines above unchanged

Candidate ID: `ANG-20260920-TDP01`.
Status: `OWNED PATH CLOCK; 2–3 RETURN RANGE — STOP / FORK`.
Portfolio decision: **stop / fork**. Exact owner-level findings; no retuning.

Main/constant-off/single-coordinate coordinate involutions exhaust predecessors;
their terminal vertices cannot have incoming edges. Rounded has the exact
floor inverse intervals, including infinite predecessor lists and onto shift.
The full path measure exists, retains atoms and null paths, and
satisfies inverse IMAGE on EVERY Borel set. Its frozen full-point clock
is log D for the ACTUAL distinct-neighbor degree, including null returns.
Prefix-pair IMAGE proves the retained-lag cocycle with correct forward sign.

Every eventually least-period-ell path has entire source group ell Z and
time group L Z, where L sums log D over that cycle.
Kernel0 when L>0, entire source when L=0; all other sources
have trivial isotropy. All finite incoming prefixes, cyclic phases and real
height offsets remain. The complete atom classification follows isolated deterministic
components; no conull or selected-core owner replaces the original source.

ALL positive primitive times in main belong to log(2^a 3^b),
a,b>=0 not both zero. Thus every log p for prime p>=5
is absent, a global range obstruction. This is not a statement
that all such products occur or that no returns exist. Main's
f fixed path has primitive log3 and v,w two-cycle primitive log9;
the latter is NOT a repetition of another packet. Main h is
zero-time fixed, while t is terminal. The frozen w,u word is illegal.

Every control was rebuilt independently. Rounded preserves the tested log9/log3,
changes h to positive log3 and t to a zero-time fixed point.
Constant-off has the tested w,u primitive log6, illegal v,w/f/h
words and zero-time fixed t. Single-coordinate has global clock0, the
two-point v,w zero basin, fixed f/h and terminal t. All
legal finite witnesses have full source/time/kernel, complete ancestors and phases.
Every positive tested basin is countably infinite and null; the tested
zero basins/terminals are isolated mass1 atoms, with distinct isotropy labels.

T0 / declared owned T1 established; stronger naturalness OPEN. T2 owned
packet convention established, prime target FAILS; T3 NOT SUPPLIED / NOT
PURSUED. Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED;
B NOT INVOKED. Other cycle realization/multiplicity and geometric realization OPEN.
No higher-cycle census or changed weights after the decisive range gate.

See the [paper](paper.md), [ledger](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md) and [frontier](evidence/scout-record.md).
Factor-pair/coefficient scouting NONE is a scoped definition collision, not
a mathematical no-go. A complete moving-divisibility rotor-field tuple is
pending, without next ID/freeze/audit. Original-owner and review source
boundaries are recorded, not external peer review. Positive304,
partial-positive320 and older packages unchanged;241/242 paused; goal active.
