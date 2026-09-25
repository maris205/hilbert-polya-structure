# Frozen broadened screen — witness-scan index flow

**Candidate ID:** `ANG-20260919-WSI01`  
**Paper ID:** `276-witness-scan-index-flow`  
**Version:** 1; frozen 2026-09-19 before proof or computation.  
**Initial status:** `OPEN — SOURCE / IMAGE CLOCK / FULL PACKET AUDIT`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Complete marked arithmetic graph

Freeze the countable directed graph with ALL the following vertices:

    H_n                 for n>=2;
    S_(n,d)             for n>=3 and 2<=d<=n−1;
    E_k                 for k>=0.

Each H_n has n distinct marked edges j=0,...,n−1. Their targets are:

    j=0, n=2:           H_2;
    j=0, n>=3:          S_(n,2);
    j>=1, gcd(n,j)>=2:  H_gcd(n,j);
    j>=1, gcd(n,j)=1:   E_0.

Every S_(n,d) has exactly one edge, with target

    H_d                 if d divides n;
    S_(n,d+1)           if d does not divide n and d<n−1;
    H_n                 if d does not divide n and d=n−1.

Every E_k has exactly one edge, to E_(k+1). All coprime ports enter
the SAME E_0. Parallel marks are not identified. Retain all scan
roots, including ones unreachable from their own H_n, and the whole
escape ray. No absorbing escape loop, chosen centre or post-result
path restriction is allowed. All integer values occur in one graph.

Lineage: prime/composite divisibility observable -> finite admissible
scan -> witnessed update of the NEXT source integer -> marked-path
groupoid realization. Witness hits and nonzero residue ports change
the subsequent hub and its available tests/ports. This replaces the
static-label and counter-fibre mechanisms of earlier source controls;
it is an autonomous state rule, not a fitted non-autonomous schedule.
No Logistic/Hénon conjugacy or conservative geometric lift is asserted.

## Path carrier, measure and complete arrow owner

Let X be the disjoint union, over every graph vertex v, of all infinite
outgoing marked edge paths starting at v. Use finite-prefix cylinders
and the disjoint-union topology. Let sigma delete the first edge.
Local homeomorphism, topology and any failure of surjectivity are
obligations, not assumptions licensed by the word shift.

Each root space X_v has measure 1. At each visited vertex choose its
outgoing edges uniformly; hence a cylinder with prefix alpha has
mass 1/D_alpha, where D_alpha is the product of the outgoing degrees
along alpha, D_empty=1. Root masses and marks are part of the owner.
Prove consistency, full support, Radon/sigma-finite properties and
the complete atom/null classification, retaining null paths.

Freeze the entire shift-tail groupoid

    G={(xi,m−k,eta): m,k>=0, sigma^m(xi)=sigma^k(eta)}.

The arrow is eta -> xi; the integer lag is retained. Multiplication
adds lags when endpoints match, and inversion reverses endpoints
and lag. Prefix replacement beta zeta -> alpha zeta is a basic
bisection when the terminal vertices of alpha and beta agree.
Its Borel IMAGE Jacobian J is to be derived from this same measure,
not prescribed from a desired prime time. Freeze the convention
c=−log J, using a proved continuous version on all arrows, including
null periodic points. Check presentation independence and additivity.

The real extension has objects X×R, with an arrow (g,u) from
(eta,u) to (xi,u+c(g)). Physical time translates u by every real t.
Prove completeness of this action without interpreting it as the
number of scan steps or imposing a positive roof on every edge.
Zero clock increments on deterministic scan edges are not replaced.

For every path xi compute the FULL time-return subgroup

    H_xi={c(g): source(g)=range(g)=xi}.

Only H_xi=T Z with a least T>0 gives a cyclic-return packet. Packet
identity uses actual groupoid/time equivalence, not equal lengths.
Repetition traverses that same packet r times. Distinguish base
isotropy, extension fixed-object isotropy and time stabilizers.
An abstract R/(T Z) time orbit is not a proved embedded circle in
a Hausdorff coarse space; coarse topology is OPEN unless established.

## Precommitted obligations and controls

1. Classify ALL infinite paths and all directed periodic cycles,
   including arbitrary scan roots, n=2, composite n=4 and n=6,
   every residue mark, finite witness descents and the escape ray.
   No favorable-subgraph census or finite-cutoff inference.
2. Derive the image clock, then solve full return subgroups,
   primitive multiplicity and repetitions. No period formula is
   admitted as a definition; no phase or tail is discarded.
3. Determine measure strata. A purely atomic full-support measure
   need not give positive mass to every path. Test the positive-atom
   coboundary obstruction on its actual domain only.
4. As a separately labelled SOURCE-OFF comparator, replace the
   scan divisibility predicate by false, keeping every other rule.
   Classify which extra cycles this admits. Do not alter WSI01.
5. As a separately labelled WEIGHT comparator, keep the same graph
   but give port 0 probability 1/2 and each other H_n port probability
   1/[2(n−1)], all deterministic edges probability 1. Derive its
   image clock separately. This is not a retiming of WSI01.
6. As a separately labelled PREDICATE comparator, replace the scan
   test by any Boolean h(n,d), keeping target H_d on a hit. Test
   whether arbitrary sets A subset {2,3,...} containing 2 can be
   encoded by h(n,2)=1_(n not in A) for n>=3, all other h=0.
   A is a theoretical adverse control, never input to the main graph.

These controls distinguish exact engineering from natural arithmetic
necessity. Naturalness of the scan/reset, n ports, privileged port 0,
uniform measure and escape routing is OPEN; local execution alone
does not close it. Source steps and image time need not coincide.

## Decision boundary, scope and provenance

Admit only a bounded exact ENGINEERING audit. A full owned arithmetic
packet/clock chain may be retained as a scoped advance. Extra intrinsic
packets, wrong repetition or an ownership failure stop that promotion.
Even a matching packet ledger does not establish natural A0 if the
generic-predicate or alternate-weight controls expose unclosed design
choices. Preserve both positive construction and adverse controls;
do not redefine the graph or measure to improve the conclusion.

T0–T2 are broadened owner-level research labels only. T3 is NOT
SUPPLIED / NOT PURSUED in this screen: no Euler-product, determinant,
trace, operator or quantization rescue. Classical (M,omega,F,tau),
mapping-torus and A0/A1/A2 fields are NOT APPLICABLE; Hamiltonian,
contact and quantum owners NOT SUPPLIED. Any changed source, measure,
action, clock or geometric owner requires a new ID and frozen card.

Nearest comparisons are [218](../218-escape-sieve-screen/candidate-card.md),
[222](../222-telescoping-divisor-clock/candidate-card.md),
[228](../228-gcd-defect-cocycle/candidate-card.md), and
[274](../274-euclidean-residue-index-flow/candidate-card.md).
This graph executes a new source rule; it is not a path selection in
274 or a clock assigned to the Hénon owners of 222/228. No old theorem,
clock or Route credit is transferred. The lineage is reconciled with
the [prior-work guide](../../docs/prior_work/README.md); the classical
dimensional-lift arrow remains unfulfilled. No literature novelty claim.

No prime table, prime-dependent roof, von Mangoldt weight, zero data,
fitted parameter, numerical run, PDF/LaTeX or publication artifact.
Root owns integration; a separate native reviewer receives this raw
card before the manuscript. Internal model review is not external
peer review. 241/242 paused; programme goal active; B NOT INVOKED.

## Appended audit outcome — 2026-09-19

**Outcome status:** `OWNED PRIME PACKETS AND INDEX CLOCK; NATURALNESS OPEN — SCOPED ADVANCE / FORK`.

The version-1 definitions remain byte-preserved. The [paper](paper.md)
proves the complete path, measure, arrow and time owner. Every path
eventually escapes or repeats a prime scan cycle C_p. The rooted
path space is countable and locally compact; sigma is locally
homeomorphic but not onto. No missing-preimage scan root is removed.

The Borel image clock is c=log D_alpha−log D_beta, continuously
fixed on all arrows by the full-support measure. Positive atoms
are exactly the conull escape paths; all returning paths are null
and retained. Each prime p gives exactly one primitive time packet,
least time log p and repeats r log p; there are no composite extras
or phase/transient multiplicities. Escape base isotropy is trivial;
prime base isotropy (p−1)Z maps injectively to time. Extension fixed-
object isotropy is trivial everywhere. The real time action is complete.

SOURCE-OFF gives one primitive at every integer. WEIGHT changes the
same graph's prime times to log 2 under a different measured owner.
PREDICATE can encode arbitrary accepted sets containing 2. These
precommitted controls establish design freedom, not a change to WSI01.

Portfolio: **advance scoped source/clock/packet engineering; stop
natural-A0 promotion; fork for arithmetic justification of the design**.
Naturalness and coarse-quotient topology remain OPEN. Packets are
abstract groupoid/time orbits, not proved embedded classical circles.
T3 NOT SUPPLIED / NOT PURSUED; classical A0/A1/A2 NOT APPLICABLE,
formal UNASSIGNED, Route B NOT INVOKED. Same-object ledger intact;
241/242 paused; programme goal active. No further tuning or rescue.
