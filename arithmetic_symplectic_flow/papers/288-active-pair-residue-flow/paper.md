# Active arithmetic feedback with one owned primitive packet per prime

Candidate ID: `ANG-20260920-APR01`.
Paper ID: `288-active-pair-residue-flow`. Date: 2026-09-20.
Status: `OWNED ACTIVE-SOURCE PRIME PACKETS; NATURALNESS OPEN — SCOPED ADVANCE / FORK`.
Result type: exact partial-owner, full-periodic-set and packet theorems.

## Abstract

An active integer pair and two complete profinite seeds evolve by a
partial residue/shear map. The current proper-divisor count and the actual
seed digit enter the integer second difference. We establish the full
partial-tail groupoid, retaining all terminal objects, and derive its
continuous joint-Haar IMAGE clock. The complete periodic set is exactly
one zero-seed fixed point at each prime root pair. A cyclic nonnegative
sum forces the arithmetic root, while an integer-matrix argument excludes
every nonzero profinite seed at every period. All finite preimages remain.
The resulting full time ledger has exactly one primitive packet per prime,
least time log p and repetitions r log p. Three arithmetic controls expose
both source selectivity and a generic constraint-encoding limitation.
Naturalness, coarse topology and analytic ownership remain open; this is
a broadened owner-level result, not a formal Route or classical lift.

## 1. Frozen definition and lineage

The [card](candidate-card.md) was frozen before this audit's claims,
with version-1 SHA-256

    1459ec2252afe8d84736c986ac4f572104bc4c6b0d3031672ac780a1f03fc3d4

It adopts, without alteration, the separately untested proposal in
[287's scout record](../287-nonlinear-two-seed-residue-flow/evidence/scout-record.md).
The old proposal supplied no clock or return theorem. The present proof
is for this new candidate only.

Let K=Z_hat with normalized additive Haar h. The full source is

    Y = coproduct_(a,b>=2) {(a,b)} x K²,
    mu on each root = h x h.

For each ordinary b>=2 define w(b)=#{d:1<d<b, d divides b}. At a
state (a,b,x,y), write j=x mod b in {0,...,b-1} and define

    c_pair=2b-a+w(b)+j,
    D={states with c_pair>=2},
    T(a,b,x,y)=(b,c_pair,y,(x-j)/b+y), on D only.

States outside D have no forward T step but remain source objects.
No artificial continuation, prime-only root selection, integer-only
seed restriction or chosen geometric centre is used.

The exact lineage is proper-divisor prime/composite admissibility ->
current integer second-order feedback -> a coupled full residue source.
The arithmetic pair is active: its next modulus depends on an actual
seed digit. This is a stated deformation of the witness-symbolic source,
not a conjugacy to the prior sieve or a claimed symplectic realization.
The witness law and aggregation cost remain explicit structural choices.

## 2. Partial-domain and joint-measure owner

Integer multiplication is injective on K: if m x=0 for nonzero integer
m, reduction modulo |m|q forces x=0 modulo every q. Moreover bK is
the kernel of reduction modulo b, and multiplication by b is a
homeomorphism K->bK. These facts justify every exact division below
without treating K as an integral domain.

**Lemma 1.** D is clopen in Y. For each permitted triple (a,b,j), its
branch U={(a,b)} x (j+bK) x K is mapped homeomorphically onto the
ENTIRE target root (b,c_pair), with inverse

    theta_(a,b,j)(u,v)=(a,b,j+b(v-u),u).

Every Borel terminal B subset K² satisfies

    mu(theta_(a,b,j)(B))=(h x h)(B)/b.

The image of T contains exactly the full target roots (u,v) with

    2<=v<=3u+w(u)-3.

*Proof.* The condition c_pair>=2 depends only on a,b and the finite
residue j, so both domain and complement are unions of clopen branches.
Direct substitution verifies the stated inverse and its source residue.
For the measure formula, the map (u,v)->(v-u,u) preserves joint Haar
by translation in each v fibre and Fubini. Scaling its first coordinate
by b and translating by j has Borel IMAGE factor 1/b, since bK has
Haar mass 1/b. This is a joint Borel argument, not a marginal density
or a formal determinant calculation.

For a target (u,v), the possible predecessors have b=u and
a=2u+w(u)+j-v, with 0<=j<u and a>=2. At least one exists exactly
when the largest possible a, namely 3u+w(u)-1-v, is at least 2.
Every permitted predecessor branch is onto the entire target K².
QED.

The precommitted endpoint controls are exact: root (4,2) is entirely
terminal; at (3,2), digit zero is terminal and digit one has target
(2,2); target (2,4) has no incoming branch. Thus neither totality nor
surjectivity is assumed. Nothing is removed to obtain either property.

For m>=0 let D_m be the domain of T^m, D_0=Y. By induction these
domains are clopen: D_(m+1) consists of points in D whose T-image
belongs to D_m. Every admissible finite branch word has a clopen image
of its entire terminal root under its composed inverse. Write D_alpha
for the product of the consumed b indices along such a prefix; its
image factor is 1/D_alpha, with D_empty=1.

## 3. Full partial-tail groupoid and all-point time

Keep the full retained-lag set

    G={(z,m-k,w):z in D_m,w in D_k,T^m z=T^k w},

with source w and target z. In particular every terminal state has
its identity arrow, because D_0=Y.

**Proposition 2.** This set is a locally compact Hausdorff second-countable
étale groupoid with the full finite branch-pair topology. It owns the
continuous Borel IMAGE derivative and clock

    J(g)=D_beta/D_alpha,
    c_G(g)=log D_alpha-log D_beta

on every actual beta-to-alpha bisection, including null states. Its real
extension has complete jointly continuous real translation on all Y x R.

*Proof.* To compose (x,m-n,y) and (y,p-q,z), align the two iterates
of y at max(n,p). If n>=p, the extra n-p steps exist because T^n y
is already defined; the equality T^p y=T^q z gives the same defined
continuation on z. The other case is symmetric. Inverse and units
are immediate. Thus composition never assumes a continuation past a
terminal point which was not supplied by a represented arrow.

Actual finite inverse-branch pairs on clopen terminal congruence sets
give a countable compact-open basis. For two presentations of the same
arrow, equal retained lag means the longer presentation extends BOTH
prefixes by the same number of steps along their actual common tail.
Those steps exist by the longer presentation. Restricting to its finite
branches supplies common refinements and the topological composition
law. Source/range are local homeomorphisms; continuous endpoints and
integer lag separate distinct arrows. This proves the topology claims.

Lemma 1 gives source mass mu(B)/D_beta and target mass mu(B)/D_alpha
for every Borel terminal restriction. Their ratio proves J. A synchronous
continuation multiplies both D values by the same product, so J is
representation-independent; composition multiplies J and adds c_G.
They are locally constant on bisections. Full support of source measure
there forces uniqueness of the continuous density version even on null
states: a continuous discrepancy would persist on a positive-measure
open set.

Extension arrows are (w,t)->(z,t+c_G(g)), with arrow topology G x R.
These formulas give local source/range homeomorphisms. Translation of
every real coordinate by s commutes with all arrows and is jointly
continuous for all s in R. The partially defined base iteration does
NOT make this real action partial. QED.

The sign is inverse-prefix insertion. No log-prime roof is supplied;
all time values come from the exact joint measure on this same source.
No Hausdorff coarse quotient or circle-embedding result is asserted.

## 4. Complete periodic-state classification

**Lemma 3 (arithmetic closure).** Every full periodic state has a constant
root pair (p,p), where p is prime, and uses digit zero at every step.

*Proof.* Write a putative periodic root sequence as (b_(i-1),b_i),
with indices modulo its period L. All those steps are defined. The
actual recurrence is

    b_(i+1)-2b_i+b_(i-1)=w(b_i)+j_i.

Sum over the cycle. The left side is zero, while each right summand
is a nonnegative ordinary integer. Hence every w(b_i)=0 and every
j_i=0. The remaining recurrence has constant first difference, which
must be zero on a finite cycle. Thus all b_i equal one p>=2. The
condition w(p)=0 says precisely that p has no proper divisor greater
than one, i.e. is prime. QED.

It remains essential to exclude nonzero profinite seed cycles; root
closure by itself is not full-state closure.

**Lemma 4 (all-period seed rigidity).** At a constant root (p,p) with
zero digits, the only seed pair returning after ANY positive number of
steps is (0,0).

*Proof.* Its inverse branch on the seeds is the integer matrix

    B_p = [[-p,p],[1,0]],

so a seed pair returning after L steps satisfies (B_p^L-I)v=0 in K².
The characteristic polynomial of B_p is t²+pt-p. Its positive real
root lies strictly between 0 and 1, because the polynomial is negative
at zero and positive at one. Its other root equals -p minus that root,
so is less than -p<=-2. Neither root has any positive power equal to
one. Consequently det(B_p^L-I) is a NONZERO ordinary integer for every
L>=1.

Multiply the matrix equation by the integer adjugate. Each seed
coordinate is annihilated by that nonzero integer determinant, and
integer multiplication on K is injective. Therefore both coordinates
are zero. This is not a field argument over K, and it handles all
noninteger seeds and every period, not just fixed states. QED.

**Theorem 5.** The ENTIRE periodic set of T is

    z_p=(p,p,0,0), one fixed state for each prime p.

There are no other fixed, higher-period, composite-root or noninteger
periodic states. Conversely every displayed state is in D and fixed.

*Proof.* Lemmas 3 and 4 give necessity; substitution gives sufficiency.
The argument also covers p=2. QED.

## 5. Full basins, primitive packets and repetitions

Let B_p contain every source state whose defined forward trajectory
eventually reaches z_p, including z_p itself and every finite preimage.

**Theorem 6.** For every z in B_p, source isotropy has lags Z and

    H_z=c_G(G_z^z)=(log p)Z.

There is exactly ONE primitive cyclic-time packet per prime, with least
time log p and repetitions r log p. Outside the union of all B_p,
source isotropy is trivial and H_z={0}. Fixed-object isotropy in the
real extension is trivial everywhere.

*Proof.* Nonzero-lag isotropy means T^m z=T^k z with m>k and both
iterates defined. The segment between them is an actual cycle. It
therefore gives eventual periodicity, including indefinite continuation
by that same cycle; a terminating trajectory cannot do this. Theorem 5
identifies every possible periodic core as some z_p.

At z_p all integer lags occur. Each actual inverse step consumes b=p,
so c_G(z_p,r,z_p)=r log p. This is the full source isotropy, not a
selected subgroup; log p is its least positive clock value. An actual
finite-prefix arrow conjugates this isotropy to any z in B_p. Its
clock and its inverse clock cancel, leaving the same return group.

Every B_p is one full G orbit through its fixed core. Distinct primes
cannot share a forward tail, so their basins are disjoint full orbits.
All real phases over each orbit give one packet under real translation.
There are no additional periodic cores or nonzero-lag isotropy elsewhere,
so the packet list is exhaustive. The clock is injective on each
nontrivial source isotropy group; this proves the extension-isotropy
assertion as well. QED.

**Proposition 7 (finite-preimage accounting).** All returning seed pairs
are ordinary integer pairs, but not every integer-seed state returns.
Each B_p intersects every root (a,b) in finitely many points, is countable,
and is joint-Haar-null. If a state first hits z_p after h steps, then
h=0 or h<=b-p+1<=b-1, and p<=b at its initial root.

*Proof.* Every inverse branch is integer-affine on the seeds. Starting
from (0,0), any finite inverse word therefore gives an integer pair.
All such actual words remain; no chosen centre replaces a larger
periodic set. There are finitely many inverse branches into a given
root (u,v), since j ranges over 0,...,u-1 and determines a uniquely.
Thus finite inverse trees and their countable union give countability.

For the rootwise assertion, set delta_i=b_i-a_i. Along any defined
step, delta_(i+1)=delta_i+w(b_i)+j_i, so these ordinary integer
differences are nondecreasing. A trajectory hitting z_p has final
delta_h=0 and cannot previously have positive delta. If delta_i=0
at any i<h, all subsequent increments must vanish. That gives the
constant prime root and zero digits thereafter; the inverse matrix
B_p then sends a zero terminal seed back to zero at time i. This
would already be z_p, contradicting first hitting at h.

Hence delta_i<0 for i<h and delta_h=0. Since b_i-b_(i-1)=delta_i,
the h-1 steps with i=1,...,h-1 decrease b by at least one, while
the last step leaves b unchanged. Thus p<=b-(h-1), proving the bound.
Along these words b_i<=b, so their finite lengths and finite digit
choices give only finitely many words from a fixed starting root.
For each word the inverse of the specified terminal point is unique.
This proves rootwise finiteness. Haar has no atoms, so the countable
returning set is null. Entirely terminal root (4,2), for example,
shows why an integer seed alone does not imply return. QED.

For an explicit all-preimage control, the immediate predecessors of
z_p are exactly (p+j,p,j,0), 0<=j<p. The j=0 state is the core;
the others are genuine retained transient points, not extra packets.

No topological reduction of Y to these countable basins is made.
The rest of the profinite source and every terminal point remain.

## 6. Three separate arithmetic controls

Replace w by each precommitted v and recompute its partial domain.
These are three different complete owners, not modifications of APR01.
For each, the permitted branch inverse is still (j+b(v_seed-u),u);
the scale/shear proof gives its own factor 1/b and the same clock
formula on its actual branches. Here v_seed denotes the second
terminal seed, not the replacement witness function.

The periodic root sum now contains the corresponding nonnegative
v(b_i)+j_i. For each control it forces a constant root n with v(n)=0
and all digits zero. The matrix B_n argument, valid for every n>=2,
then gives exactly one zero-seed periodic core at each such n. Its
own full isotropy gives least time log n. Therefore:

| Frozen control | Complete primitive packet ledger | What it tests |
|---|---|---|
| WITNESS-OFF, v=0 | One packet of least log n for EVERY n>=2 | Composite primitives survive when divisibility is removed |
| WITNESS-ON, v=1 | No periodic states and no positive-time packets | Constant positive drift prevents closure |
| SHIFTED TEST, v(b)=w(b+1) | One packet of least log n exactly when n+1 is prime, n>=2 | Source relation changes the selected root family |

For instance the shifted control retains n=4 with least time log 4;
it is a different primitive packet from n=2 and not its second traversal.
These are exact formula consequences, not a finite-prime experiment.

The same cyclic-sum reasoning depends on nonnegativity and the witness
zero set. This is a real PROVES_TOO_MUCH warning: it explains arithmetic
selectivity for the chosen w but does not make the witness-engineering
principle uniquely natural for primes. A direct evaluation of w(b)
uses b-2 possible divisor tests. Log b is the measure-derived clock,
not an assertion that this aggregation costs logarithmic runtime.

## 7. Assessment and next obligation

| Gate / obligation | Result | Remaining boundary |
|---|---|---|
| T0 partial carrier and full arrows | ESTABLISHED | Terminal and missing-incoming states retained |
| T1 actual arithmetic feedback and joint clock | OWNED, scoped | Naturalness and generic constraint encoding OPEN |
| T2 full periodic, primitive and repetition ledger | ESTABLISHED: exactly one log-p packet per prime | Coarse packet topology not assessed |
| T3 operator / trace / zeta / determinant | NOT SUPPLIED / NOT PURSUED | Requires its own explicit same-object contract |
| Classical symplectic / A0/A1/A2 fields | NOT APPLICABLE | No finite-dimensional geometric lift supplied |
| Formal Route coordinates / Route B | UNASSIGNED / NOT INVOKED | Owner-level results are not formal Route passage |

Portfolio: **scoped advance / fork**. Advance this unchanged candidate's
complete owner-level T0-T2 record. Keep architectural breadth open for
stronger naturalness; do not present the engineered witness rule as an
inevitable arithmetic mechanism. The named next same-object obligation
is the topology of these packets in the FULL coarse extension quotient,
before any claim that they are ordinary embedded closed flow circles.
Any analytic-owner proposal needs a separate frozen operator/domain/trace
contract and cannot borrow a determinant merely from the prime ledger.
Neither further obligation is carried out here.

The same-object ledger remained intact. No source, domain, clock or
packet multiplicity was repaired after testing. Old candidates stay
unchanged; 241/242 remain paused; the programme goal stays active.

## Evidence and disclosure

See the [claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal adverse review](evidence/independent-review.md) and
[source/control record](evidence/source-controls.md). All results use
exact inequalities, matrix algebra, residue topology and Borel Haar
laws. There is no scientific numerical run, finite cutoff, parameter
search, target data or external novelty claim. AI-assisted authorship
used the ARS freeze and adverse-check workflow. Internal same-model,
shared-context checks are not external peer review, independent-error
guarantees or formal verification.
