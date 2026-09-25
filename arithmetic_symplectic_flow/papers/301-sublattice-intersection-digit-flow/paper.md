# Full sublattice digits own a clock but retain uncountable packet multiplicity

Paper ID: `301-sublattice-intersection-digit-flow`.
Candidate ID: `ANG-20260920-SID01`. Date: 2026-09-20.
Status: `OWNED SUBLATTICE IMAGE CLOCK; UNCOUNTABLE INTEGER-TIME MULTIPLICITY — STOP / FORK`.
Route state: broadened owner audit only; formal coordinates UNASSIGNED;
classical A0/A1/A2 NOT APPLICABLE; Route B NOT INVOKED.

## Abstract

The frozen source retains every finite-index sublattice of Z^2,
every ordered lattice pair, and every seed in K^2, K=Z_hat.
A canonical Hermite digit is adjoined to the intersection of the
current lattices. The resulting map is a globally defined local
homeomorphism, not a surjection. Its full retained-lag groupoid
owns a joint-Haar IMAGE clock and complete continuous real time.
The exact divisor-symbolic interface uses reverse lattice inclusion.
Nevertheless, already at equal roots L_n=nZ x Z, every n>=2
has a distinct primitive log-n packet for EACH t in K. All these
cores are retained, including their Haar-null seeds; excursions
through other lattices cannot merge them. Thus n=2 alone violates
finite target multiplicity, and n=4 supplies composite primitives.
The candidate stops at this bounded family, not after a full
period census. Two changed-source controls own their own clocks.

## 1. Identity, question and same-object ledger

The question is whether this all-lattice deformation of divisor
symbols supplies an owned clock and the required primitive packet
ledger without choosing one seed or manually supplying prime times.
The [original card](candidate-card.md) was frozen before this audit.

| Field | This exact owner | Scope |
| --- | --- | --- |
| Carrier | Discrete ordered pairs of ALL finite-index L,M in Z^2, each with full K^2 | ANG, not a manifold lift |
| Evolution | Hermite quotient; N=(L intersect M)+Z*j; T(L,M,x)=(M,N,y) | All roots and seeds retained |
| Arithmetic | Actual intersection, actual integral digit vector, divisor/inclusion interface | No prime predicate or table |
| Measure and clock | Rootwise normalized joint Haar; c=-log IMAGE density | Derived below, no roof |
| Time owner | Full retained-lag groupoid and its real cocycle extension | Two-sided complete continuous time |
| Packets | Actual tail equivalence and phase; full isotropy image H | Equal lengths never merge packets |
| Symplectic base, mapping torus, Hamiltonian/contact lift | NOT APPLICABLE / NOT SUPPLIED | No Logistic/Henon conjugacy asserted |
| Trace, zeta, determinant, operator, quantization | NOT SUPPLIED / NOT PURSUED | No T3 or later credit |

The source and basis choice are declared designs. Their stronger
naturalness, representative-independence and GL_2(Z)-equivariance
are OPEN. This paper does not identify the broadened construction
with the original finite-dimensional ASFS contract.

## 2. Full lattice and digit construction

### 2.1 Unique coordinates and root closure

For a finite-index L, its second-coordinate projection is cZ,
and L intersect (Z x {0}) is aZ x {0}, with a,c>=1.
Choose (b,c) in L and reduce b modulo a to 0<=b<a.
Every vector of L subtracts an integer multiple of (b,c) to
reach the horizontal kernel. Thus

    A_L=[[a,b],[0,c]], L=A_L Z^2.

The projection, kernel and reduced lift respectively determine
c,a,b uniquely. Reducing any integer vector first in its second
coordinate and then in its first gives unique representatives
j=(j_1,j_2), 0<=j_1<a, 0<=j_2<c. Hence [Z^2:L]=ac.
There are countably many such actual lattices, not basis classes.
Two finite-index lattices contain a common rZ^2 for some r>=1;
their intersection, and its enlargement by Z*j, have finite index.
Consequently every proposed next root is in the original carrier.

### 2.2 Division in K and the entire digit partition

Multiplication by any integer d>=1 is injective on K: if dz=0,
reduction modulo dN forces z=0 modulo N for every N.
Its image is exactly the kernel of reduction modulo d. For a
compatible residue in that kernel, division of its residues modulo
dN by d constructs the compatible quotient modulo N. This gives
a continuous inverse onto dK, a clopen subgroup of index d.

For every x in K^2 define

    j_2=x_2 mod c,             y_2=(x_2-j_2)/c,
    j_1=(x_1-b*y_2) mod a,     y_1=(x_1-b*y_2-j_1)/a.

All digits are their ordinary nonnegative integer representatives.
Then x=j+A_L*y. This expression is unique: second-coordinate
division determines j_2,y_2 and first-coordinate division determines
j_1,y_1. The matrix is injective by the same triangular argument.
The ac cosets j+A_L K^2 form a complete clopen partition of K^2.

Set Y=coproduct_(L,M) {(L,M)} x K^2 and

    N=(L intersect M)+Z*j,       T(L,M,x)=(M,N,y).

For every actual L,M,j the branch U={(L,M)} x (j+A_L K^2)
maps homeomorphically onto V={(M,N)} x K^2, with inverse

    theta(M,N,y)=(L,M,j+A_L*y).

These are ALL inverses: the original root and its unique digit
must satisfy exactly the displayed equality for N. Distinct
determinants do not parametrize branches, and no rational-matrix
completion or selected sublattice sector is added. T is a global
local homeomorphism on the locally compact, second-countable
Hausdorff space Y. At L=Z^2 it has j=0,y=x without an extra step.

T is not onto. At target (M,N)=(2Z^2,Z^2), any predecessor
would have N=(L intersect M)+Z*j. Modulo M, this subgroup has
cyclic image generated by j. But Z^2/M=(Z/2Z)^2 is not cyclic.
Every seed over this missing-image root remains an object of Y.

## 3. The same measure, groupoid and continuous clock

Let mu restrict to normalized joint additive Haar h x h on each
root fibre, with root mass one. It is locally finite, sigma-finite
and full support. Since A_L K^2 has index ac, its ambient Haar
mass is 1/(ac). The injective group map A_L transports normalized
Haar to normalized Haar on that subgroup. Therefore for EVERY
Borel E in the target fibre, translation invariance gives

    mu(theta(E))=mu(E)/(ac).

This is an IMAGE law for the actual inverse branch, not a
postulated determinant roof. The direction theta is target to
predecessor; its J is 1/det A_L and its c=-log J is log det A_L.

Retain the full groupoid

    G_T={(z,m-k,w): T^m z=T^k w, m,k>=0},

with source w, range z and integer lag. Charts are all actual
finite inverse-branch pairs over common terminal domains, including
clopen refinements. Finite branch restrictions give local source
and range homeomorphisms. Their intersections are locally refinable
by extending common histories; multiplication aligns middle histories.
This supplies the usual etale topology directly from this action,
not from free branch words. Compact-open restrictions give local
compactness. Range, source and discrete lag separate distinct
triples, so G_T is Hausdorff. None of this proves its coarse
orbit quotient Hausdorff.

Write D_m(z) for the product of det A_L over the ACTUAL first
m roots on the history from z, with D_0=1. A branch pair from
w to z, sharing T^m z=T^k w, has IMAGE density D_k(w)/D_m(z).
Indeed the terminal-to-z and terminal-to-w inverse maps respectively
scale Haar by 1/D_m and 1/D_k. Thus

    c(z,m-k,w)=log D_m(z)-log D_k(w).

Another presentation of the same lag extends both histories by
the same number of steps, introducing identical terminal products
which cancel. Aligning middle histories proves additivity under
composition. These densities are locally constant and continuous.
Full support makes the continuous version uniquely determined on
each open chart by its almost-everywhere density, including at
null seeds. The clock is not assigned independently at fixed points.

Use ALL extension objects Y x R and arrows

    (w,s) -> (z,s+c(g)).

Translation (z,s)->(z,s+t), for every real t, commutes with every
arrow and is jointly continuous and two-sided complete. It descends
as a continuous action on the quotient with its quotient topology:
the groupoid orbit projection is open, hence so is its product
with R. No Hausdorff quotient, embedded circle or classical mapping
torus is asserted. Unit-index branches keep clock zero.

For each z set H_z=c(G_z^z). A positive primitive packet requires
H_z=T_z Z with least T_z>0. Extension fixed-object isotropy is
ker(c restricted to G_z^z), which must not be confused with H_z.
Repetition means ell traversals of the SAME actual packet.

## 4. Exact divisor-symbolic interface

Use [the prior-work lineage](../../docs/prior_work/README.md), not
the generic presence of an integer index. Define L_n=nZ x Z.
Then n divides m exactly when L_m is a subset of L_n: the
order is REVERSED. Also L_n intersect L_m=L_lcm(n,m).
Every lattice between L_n and Z^2 contains {0} x Z and is
therefore some L_d with d dividing n. Thus prime n corresponds
to a cover below Z^2 even among all intermediate sublattices.
This order property is not a prime-only periodic-packet theorem.

The actual dynamics on ALL scalar-pair seeds is

    j=(x_1 mod n,0),   y=((x_1-j_1)/n,x_2),
    N=L_g,            g=gcd(lcm(n,m),j_1), gcd(r,0)=r.

Hence this sector is invariant and supplies a precise deformation
of divisibility/admissibility into an intersection-and-residue rule.
The full source still contains all non-diagonal lattices and their
branches. No previous scalar gcd source, clock or theorem is
substituted for this owner. The arrow realised is divisor-symbolic
admissibility -> full sublattice/digit deformation on the ANG track;
a Logistic/Henon geometric lift is NOT established.

## 5. Decisive fixed-family theorem and full packet identity

**Theorem.** Among ALL full states with roots L=M=L_n, the
fixed states are exactly

    n>=2: z_(n,t)=(L_n,L_n,(0,t)), t in K;
    n=1:  (Z^2,Z^2,x), every x in K^2.

For n>=2, root fixedness requires gcd(n,j_1)=n. The canonical
range 0<=j_1<n forces j_1=0. Seed fixedness then says
(n-1)x_1=0, hence x_1=0 by injectivity on K. There is no
constraint on x_2=t. Conversely these states are fixed. For n=1
the entire matrix and digit rule are the identity, giving every seed.

At z_(n,t), the full source isotropy is Z: every integer lag is
represented, and the retained-lag triple contains no extra label.
Its cocycle is ell log n. Therefore, for n>=2,

    G_z^z=Z,   H_z=(log n)Z,   extension fixed-object isotropy=0.

The least positive time is log n. Two distinct fixed cores have
different constant tails, so no actual arrow connects them. Paths
through non-diagonal lattices or finite preimages cannot change this:
any composition is still an arrow of the same full tail groupoid
and would require equality of the two constant tails. Real phases
give one time packet over each core, not an identification between
cores. Finite preimages belong to a core's packet class without
merging different cores.

K has continuum cardinality: arbitrary binary sequences prescribe
compatible 2-power residues, and zero residues on odd prime powers
extend them by the Chinese remainder rule; conversely K embeds
in a countable product of finite sets. Thus EVERY n>=2 already
has continuum many different primitive log-n packets in this family.
The n=2 prime-time multiplicity alone is decisive. The n=4 cores
are distinct composite primitive packets, not repeats of n=2 cores,
even though log 4=2 log 2. No representative seed may be selected.

For n=1 source and extension fixed-object isotropy are both Z,
but H=0. This is not a positive primitive packet. For n>=2 the
fixed seed set {0} x K is Haar null, because a singleton has
mass at most 1/N for all N. The proved continuous density still
owns its clock there; a conull deletion would change the frozen
object and cannot repair this ledger. The unit-root fixed fibre
has full rootwise mass one and likewise remains.

This theorem classifies only the frozen equal-scalar-root fixed
family. Other fixed roots, higher periods, eventual returns outside
its basins and the full coarse topology are OPEN / NOT PURSUED.

## 6. Separately owned controls and adverse findings

### ADJOIN-OFF

Replace N by L intersect M, keeping the full source, digit quotient
and joint Haar. For each L,M,j its inverse is still j+A_L*y,
now onto the target (M,L intersect M). Its OWN IMAGE factor is
1/det A_L by the subgroup argument above; it has the corresponding
continuous cocycle and real extension, not borrowed main packets.

For L=M=L_n with n>=2 every digit now preserves the root.
Fixed seeds solve (n-1)x_1=-j_1. Reduction modulo n-1 forces
j_1=0 or n-1; for n=2 these are also the two possible digits.
Injectivity gives exactly x_1=0 or -1, with every x_2=t in K.
Both ordinary boundary seeds have the required canonical residues.
Each of these two disjoint K-indexed families has source isotropy
Z, time group (log n)Z and zero extension fixed-object isotropy.
Distinct fixed cores cannot be merged by the actual tail arrows.
For n=1 all K^2 is fixed with source/extension isotropy Z and H=0.
The main feedback removes the -1 family: j_1=n-1 changes its
next root to L_1. It does not eliminate the surviving multiplicity.

### UNIT-INDEX

The changed action is T_u(L,M,x)=(M,L intersect M,x), with
j=0 and identity seed transport. Every root-fibre branch has
IMAGE factor 1 under the same equal-mass Haar fibres. Every finite
branch pair therefore has c=0 and EVERY time group H is zero.
Attaching log det A_L to this changed action would be a false owner.

For completeness, let I=L intersect M. The root sequence is
(L,M)->(M,I)->(I,I), and the seed never changes. Thus every
state reaches a fixed state in at most two steps; every integer
lag occurs in its full source isotropy. Source and extension
fixed-object isotropy are Z everywhere despite zero time groups.
This bounded control observation was also supplied in the reviewer's
raw-card findings and checked here before manuscript comparison.

The ownership controls retain missing-image roots, unit steps,
null cores and all non-diagonal lattices. The PROVES_TOO_MUCH
risk is realised as uncountable integer-time primitives, not resolved
by the prime-cover property of the inclusion poset. Removing t,
changing measure, choosing a centre or altering representatives is
a new object, not a permissible repair of this frozen card.

## 7. Gate assessment and decision

| Gate | Evidence | Status and limit |
| --- | --- | --- |
| T0 | Full lattice/seed action, exact inverse branches and full tail owner | ESTABLISHED for this ANG object |
| T1 | Exact divisor interface and own continuous Haar IMAGE clock | SCOPED MEASURED RESULT; stronger naturalness OPEN |
| T2 | ALL fixed seeds in the frozen diagonal-root family and their full H/packet identity | ESTABLISHED FAMILY; target multiplicity/prime-primitive requirement FAILS |
| T3 | No trace, zeta or operator supplied | NOT PURSUED |
| Classical A0/A1/A2 | No classical symplectic candidate constructed | NOT APPLICABLE; formal coordinates UNASSIGNED |
| Route B | No same-candidate formal readiness or evaluation | NOT INVOKED |

Portfolio: **stop target promotion / fork**. The decisive reason
is already continuum many distinct log-2 primitives, independently
reinforced by composite log-4 primitives. The same-object ledger
remained intact; the clock result is useful but not Route credit.
No further lattice/period census or T3 construction is warranted.
A separate finite integral-affine word definition is pending in
the [scout record](evidence/scout-record.md), with no candidate ID
or result. A Euclidean-renewal lane has no complete restart rule
and stops before admission. Neither modifies this candidate.

## Reproducibility, review and limits

The proof is exact for arbitrary lattices and every seed in the
tested families. There is no numerical cutoff, precision choice,
scientific computation, external data or literature-dependent lemma.
[Evidence](evidence/README.md) records input/output hashes, proof
reproduction, internal review and Markdown QA. See the
[claim ledger](claim-ledger.md), [package index](README.md) and
[raw-card/manuscript/adverse report](evidence/independent-review.md).
ARS internal review uses the inherited model and shared context;
it is not external peer review or independent-error evidence.
Historical packages/mirrors stay unchanged; 241/242 remain paused.
Markdown only; no publication, PDF, LaTeX, staging or commit.
