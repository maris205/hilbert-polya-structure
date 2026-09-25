# Witness-driven source descent and a prime-only index-clock packet ledger

**Paper ID:** `276-witness-scan-index-flow`  
**Candidate ID:** `ANG-20260919-WSI01`  
**Date:** 2026-09-19; exact construction and adverse controls.  
**Status:** `OWNED PRIME PACKETS AND INDEX CLOCK; NATURALNESS OPEN — SCOPED ADVANCE / FORK`.  
**Route state:** broadened owner-level T0–T2 only; formal `UNASSIGNED`; B `NOT INVOKED`.

## Abstract

The frozen all-integer marked graph executes divisibility scans and gcd
ports; a witness changes the next source integer, and coprime exits enter
one nonrecurrent ray. We prove that its entire path space consists of
eventually escaping paths and eventually prime-scan-periodic paths. The
full prefix groupoid, with root masses one and uniform outgoing weights,
derives a continuous image clock. Its complete cyclic-return ledger has
exactly one packet per prime p, least time log p and repeats r log p.
No composite, phase, transient or parallel mark supplies an extra packet.
The measure is full-support and purely atomic, but every returning path
has zero mass and remains part of the owner. This is an engineered
groupoid result, not a natural arithmetic A0 conclusion: precommitted
controls independently replace the accepted integers and change every
prime period to log 2. No classical geometric lift, coarse-space circle
embedding, trace, zeta, determinant, operator or formal Route is claimed.

## 1. Identity, provenance and question

The [version-1 card](candidate-card.md) was frozen before this proof.
The [prior-work lineage](../../docs/prior_work/README.md) is preserved as
prime/composite observables -> admissible divisor-test words -> executed
source updates -> a measured marked-path groupoid. This is a broadened
realization of that source arrow, not a completed Logistic/Hénon-to-
symplectic lift. It is autonomous, not a time-dependent fitting schedule.

| Item | WSI01 owner and boundary |
| --- | --- |
| Arithmetic state | All hubs H_n, all proper-divisor scan states S_(n,d), all escape states E_k |
| Update and marks | Frozen local divisibility/gcd targets; every port and every infinite path retained |
| Measure | Root mass one; uniform outgoing edges, deterministic scan/escape edges |
| Arrows and clock | Entire lag-retaining prefix groupoid; Borel IMAGE derivative, c=−log J |
| Time and packets | Real-coordinate extension; actual isotropy image and arrow/time equivalence |
| Classical fields | (M,omega,F,tau), mapping torus and classical A0/A1/A2 NOT APPLICABLE |
| Analytic/later owners | T3, Hamiltonian/contact/quantum, trace and operator NOT SUPPLIED |

The question is whether this one source/measure owner supplies a full
prime-only cyclic-return ledger with its own clock. No prime list, prime
predicate input, per-prime parameter, logarithmic roof, von Mangoldt
weight or zero data is used. Ordinary divisibility is tested during the
scan. This does not prove that the declared program architecture or
uniform measure is forced by arithmetic.

The closest changed owners are [218](../218-escape-sieve-screen/candidate-card.md)
(static-label scan and absorbing escape fixed points),
[222](../222-telescoping-divisor-clock/candidate-card.md)
(Hénon witness recurrence with a prescribed telescoping roof),
[228](../228-gcd-defect-cocycle/candidate-card.md)
(gcd-driven counter/geometry without source feedback), and
[274](../274-euclidean-residue-index-flow/candidate-card.md)
(unmodified zero-residue self-loop at every integer). WSI01 replaces
that transition law, not merely an unfavorable subset of 274's paths.
None of their clocks or theorems is transferred. Earlier
[160](../160-source-geometric-return-clock/candidate-card.md) already
provided a different engineered prime-log flow under chosen dilation/
reset timing; prime-log engineering itself is not a novelty claim here.

## 2. Complete graph and all infinite paths

Vertices are H_n (n>=2), S_(n,d) (n>=3, 2<=d<=n−1), and E_k
(k>=0). At H_n the n outgoing marked edges are j=0,...,n−1.
Port 0 goes to S_(n,2), except H_2 goes to itself. A nonzero port
goes to H_g for g=gcd(n,j)>=2 and to E_0 for g=1. Each scan vertex
has one edge: to H_d if d divides n; otherwise to S_(n,d+1) if
d<n−1, and to H_n at the final test. Each E_k goes to E_(k+1).

All starting vertices, including scan roots without a predecessor, are
kept. Different parallel edges remain different symbols. Define X_v as
the infinite edge paths from v and X as their topological coproduct,
with finite-prefix cylinders. The shift sigma deletes the first edge.

### Proposition 1 — exhaustive path and directed-cycle classification

Every path eventually follows the escape ray or repeats one of the
following marked cycles, for a unique prime p:

    C_2: H_2 --port 0--> H_2;
    C_p: H_p -> S_(p,2) -> ... -> S_(p,p−1) -> H_p,  p>=3.

Their least edge lengths are ell_p=p−1. There are no other directed
periodic cycles, and all paths are a finite prefix followed by one
of these periodic tails or an escape tail.

**Proof.** A scan is finite and must reach a hub. Every nonzero
hub port either escapes or changes n to a proper divisor: for
1<=j<n, gcd(n,j)<n. A scan witness d also satisfies 2<=d<n,
so changes the next hub to a strictly smaller integer. The remaining
possibility is port 0 followed by a whole scan with no witness.
For composite n a proper divisor is encountered, hence this cannot
return to H_n; for prime n it follows precisely C_n. If a path starts
at a late scan root, it can miss an earlier witness once, but on
returning to H_n the next port-0 scan restarts at 2. This produces
no additional persistent cycle.

Along a nonescaping path the integers at successive hubs cannot
increase. There are only finitely many strict decreases. After the
last one the path must keep following C_p at some prime p; otherwise
it decreases or escapes again. Such a C_p has distinct scan vertices
and only one occurrence of H_p, so has least edge length p−1, including
the p=2 sentinel. The same monotonicity excludes a directed cycle with
a descent or escape. This covers all roots and all marks. QED.

**Fixed controls.** H_4's scan hits 2 and goes to H_2; H_6's scan
also hits 2. A path starting at S_(6,3) instead hits 3 and goes to
H_3, but never closes at a composite hub. A nonzero H_6 port j=3
likewise changes the next source to H_3. These are actual source
changes, not counter increments attached to an invariant n-fibre.

### Proposition 2 — topology and the non-onto shift

X is countable, second countable, locally compact and Hausdorff.
Each X_v and each finite-prefix cylinder is compact open. The shift
is a local homeomorphism but is NOT onto.

**Proof.** Each vertex has finitely many and at least one outgoing
edge. A rooted path tree has finitely many prefixes of each length;
its consistent infinite choices form a compact metrizable space
(equivalently, use the diagonal subsequence argument). Cylinders are
clopen and identify with the terminal-root path space. Distinct roots
are disjoint open pieces, giving the stated coproduct properties.
There are only countably many finite prefixes, periodic tails and
escape tails; Proposition 1 therefore gives countability of X.
On a one-edge cylinder sigma is a homeomorphism onto X at its target.
However S_(6,3) has no incoming edge: its only possible predecessor
would be S_(6,2), whose edge instead goes to H_2. Its nonempty root
space has no shift preimage. Surjectivity is not required or repaired.
QED.

## 3. The full measure, including null returning states

For a prefix alpha, write D_alpha for the product of outgoing degrees
at its traversed source vertices; empty prefixes have D=1. The
specified root probabilities are mu(X_v)=1 and mu([alpha])=1/D_alpha.
The sum over one-edge extensions equals the original cylinder mass.
These consistent finite probabilities define the rooted Borel measure;
the countable coproduct defines mu. Every nonempty cylinder has positive
mass, so mu has full support. Each compact subset meets only finitely
many open root components, each of finite measure; hence mu is locally
finite, Radon and sigma-finite.

### Proposition 3 — exact atom/null dichotomy

Let A be all paths eventually reaching the escape ray. Each xi in A
is an isolated positive atom, of mass 1/D_alpha if alpha ends at the
first escape vertex on that path. Every path outside A has mass zero.
A is open, dense and conull; mu is purely atomic, but not positive
at every point of X.

**Proof.** After entering E_k there is only one continuation, so its
singleton is a cylinder with the displayed positive mass. Any path
outside A eventually repeats C_p, and each traversal uses one hub of
degree p. Nested cylinders after r extra traversals have mass bounded
by a fixed constant times p^(−r), which tends to zero. Proposition 1
and countability show that the whole complement is a countable null
set. Every finite prefix has an escape continuation: finish its scan
to a hub if necessary and use port j=1 there. Thus A is dense. QED.

Null paths have not been discarded. The all-states return ledger and
the almost-everywhere positive-atom ledger answer different questions.
Countability alone would not justify assigning positive mass everywhere.

## 4. Prefix groupoid and its derived continuous image clock

Retain exactly G={(xi,m−k,eta):sigma^m xi=sigma^k eta}, with source
eta, range xi and integer lag. For prefixes alpha,beta ending at v,
the set B(alpha,beta) consists of

    (alpha zeta, |alpha|−|beta|, beta zeta),  zeta in X_v.

These are compact open bisections. Common refinements add the SAME
finite tail prefix to alpha and beta. Intersections at equal lag are
given by such refinements; inversion exchanges prefixes and composition
uses matched extensions. These facts prove the groupoid topology and
continuous operations. Source and range restrict to homeomorphisms on
each bisection. The countable basis makes G second countable and locally
compact; different arrows are separated by an endpoint or lag, proving
Hausdorffness. Thus G is étale even though sigma is not onto.

This terminology agrees with the local-homeomorphism and graph examples
in [Sims, Examples 2.4.6–2.4.7](https://www.aidansims.com/papers/Sims2017.pdf).
Here graph edges point outward; the source uses the opposite naming
convention. The prefix, measure and arithmetic arguments here are
self-contained; no C*-algebra or operator result is imported.

### Proposition 4 — image formula and same-owner clock

On the bisection beta zeta -> alpha zeta, for every Borel subset E
of its source cylinder,

    mu(theta E) = (D_beta / D_alpha) mu(E),
    J = D_beta / D_alpha,
    c = −log J = log D_alpha − log D_beta.

This is an everywhere-defined continuous additive cocycle on G,
uniquely extending its Borel image densities as a continuous version.

**Proof.** Both prefix cylinders identify with X_v. Prefix insertion
scales its measure by 1/D_alpha or 1/D_beta, first on cylinders and
then on all Borel sets by uniqueness of the finite measures. Their
ratio gives the formula. Two representations of the same arrow have
the same lag, so after ordering their deletion lengths they differ by
adding a common tail prefix. Its degree product cancels in the ratio.
Thus the formula is independent of the presentation. Refining two
composable bisections to matched prefixes proves multiplication of J
and additivity of c; inversion changes the sign. Each bisection has
constant J and c, so they are continuous. Any different continuous
image-density version on that bisection would differ on a nonempty
open set of positive measure, contradicting almost-everywhere equality.
This uses full support, not positive singleton mass at a periodic point.
QED.

On A let L(xi)=−log mu({xi}). Applying the image formula to a singleton
gives c(g)=L(range g)−L(source g). This is an endpoint potential on A
only. Section 5 proves why it cannot be an everywhere-defined potential.
The positive-finite-atom obstruction from 272 therefore does not apply
to every state of WSI01. There is no contradiction or null-state repair.

## 5. Complete real time and the full primitive-packet ledger

The extension has objects X×R and arrows (g,u) from (eta,u) to
(xi,u+c(g)). Additivity supplies composition and inverse arrows.
Its arrow topology is G×R; on bisection products the source and range
are local homeomorphisms. It is locally compact, Hausdorff, second
countable and étale. Physical time Phi_t translates every real
coordinate by t and commutes with arrows. It is continuous and defined
for all t in R. This is not a positive-edge-roof suspension: scan/escape
edges have zero clock, and no interpretation as scan runtime is made.
Completeness comes from real translation, not an unproved non-Zeno sum.

Let Q denote the set of extension orbits, with the induced time action.
A time t fixes the class of (xi,u) exactly when it is the clock of a
base isotropy arrow at xi. Thus the FULL time stabilizer is H_xi as
frozen in the card. No individual arrow is chosen as the stabilizer.

### Theorem 5 — exactly one prime packet, no extras

For xi in A, base isotropy is trivial and H_xi={0}. If xi eventually
repeats C_p, its base isotropy lags are exactly (p−1)Z and

    c(xi, r(p−1), xi) = r log p,       r in Z,
    H_xi = (log p) Z.

Extension fixed-object isotropy is trivial at EVERY object. On Q
there is exactly one cyclic-return time orbit for each prime p, of
least period log p; its rth positive repetition has time r log p.
There are no composite or additional primitive packets. All escaping
paths give one nonperiodic time orbit, abstractly R.

**Proof.** Nonzero lag isotropy is equivalent to two equal shifted
tails, hence to eventual periodicity with the corresponding period.
An escape tail has strictly increasing E indices and cannot be
eventually periodic. Proposition 1 classifies every remaining tail;
its least edge period is ell_p=p−1. Finite transient prefixes cancel
when expressing isotropy by deleting into that periodic tail. Every
turn of C_p meets H_p once and deterministic scan vertices otherwise,
so its degree product is p. Proposition 4, with the prescribed image
orientation, gives the displayed clock, including p=2. Its restriction
to base isotropy is injective; extension fixed-object isotropy requires
c=0 and is consequently trivial on this stratum too.

Two paths eventually following C_p have equal shifted tails after
choosing the same phase. Actual groupoid arrows identify their finite
prefixes and phases; time translation absorbs the corresponding real
coordinate differences. Tails of C_p and C_q for different primes never
agree, so no arrow or time action identifies their packets. Parallel
transient marks give different paths, but not additional packets.
Likewise all escape tails eventually agree after aligning their E
indices; all escaping paths belong to one base orbit with zero time
stabilizer. Finally Proposition 1 exhausts X. QED.

In particular c is not a pointwise endpoint difference on all X:
an isotropy generator at C_p has value log p rather than zero. There
is no selected prime sector, hidden k-register multiplicity, extra
composite packet or zero-time isotropy kernel in this owner.

The orbit set is abstractly one free R orbit plus one R/(log p)Z
orbit for each prime. We do NOT give it the disjoint-union topology
by declaration. Hausdorffness of the extension groupoid does not prove
Hausdorffness of its coarse quotient Q or that these abstract packets
are embedded classical circles. Those coarse-topology claims remain
OPEN and are unnecessary for this explicitly typed packet theorem.

## 6. Precommitted adverse controls: what the theorem does not establish

These are distinct comparator owners fixed in the card, not changes
to WSI01 and not pooled candidate credit.

**SOURCE-OFF.** Replace each divisibility hit by false. No scan now
changes n; nonzero ports still descend or escape. The monotonicity
argument gives exactly one cycle at EVERY n>=2, with length n−1
and degree product n. Its least time is log n. In particular 4 and
6 become independent primitives; log 4 is not a repeat of the H_2
packet because their marked tails never agree. Executed witnesses
are therefore necessary for prime specificity in this design.

**WEIGHT.** Keep the graph, give H_n port 0 probability 1/2 and
each of its other n−1 ports probability 1/[2(n−1)], keeping deterministic
edges at probability one and root masses one. The same prefix proof,
with cylinder probabilities replacing reciprocal degrees, derives a
different continuous image clock. A complete C_p turn has probability
1/2, so every distinct prime packet has least time log 2. Thus the
unweighted graph, source decisions and full packet identity do NOT
force WSI01's logarithmic prime time. Its uniform degree law is an
explicit normalization/design choice, not a derived arithmetic necessity.

**PREDICATE / PROVES_TOO_MUCH.** For any K subset {2,3,...} containing
2, replace the witness by h(n,2)=1_(n not in K) for n>=3, all other
h=0. A hit goes to H_2;
an accepted scan closes at H_n. All other hub changes strictly descend,
so precisely the n in K carry primitive scan cycles, each with the
uniform-weight clock log n. This proves arbitrary-set encodability
within the comparator family, not that its prescribed set is generated
endogenously. For a noncomputable set it is only a mathematical graph,
not an algorithm; WSI01 itself uses the computable divisibility law.
No such arbitrary-set input is fed to WSI01. Nevertheless a correct
packet list alone cannot distinguish a natural mechanism from a
programmed predicate-and-branching construction of comparable form.

These controls are exact, not finite randomized trials. Geometric
parameter controls do not apply to a missing classical geometric owner;
normalization sensitivity is addressed by WEIGHT. No numerical cutoff,
precision, optimization or orbit-table extrapolation is used. Source-off
prime specificity is a positive engineering discriminator, while WEIGHT
and PREDICATE prevent a naturalness inference. Neither disproves every
possible future arithmetic justification of this architecture.

## 7. Gate assessment and decision

| Gate | Evidence for WSI01 | Scoped state / limitation |
| --- | --- | --- |
| T0 | Entire source, paths, measure, prefix arrows and real extension constructed | ESTABLISHED as a groupoid owner; classical fields N/A; coarse topology OPEN |
| T1 | Witnesses/gcd change subsequent source; continuous image clock derived | ENGINEERING ESTABLISHED; source/measure naturalness OPEN; not scan-runtime time |
| T2 | Exhaustive path/isotropy proof; exactly one least-log-p packet per prime, repeats retained | ESTABLISHED for abstract groupoid/time packets, not a symplectic orbit theorem |
| T3 | No trace, zeta, determinant or operator constructed | NOT SUPPLIED / NOT PURSUED by this bounded contract |
| Classical A0/A1/A2 | No finite-dimensional symplectic suspension owner | NOT APPLICABLE; no natural A0 promotion |
| Formal Route A / B | No formal evaluation | UNASSIGNED / NOT INVOKED |

Portfolio: **advance the scoped owned source/clock/packet construction;
stop natural-A0 promotion; fork the search for an arithmetic justification
of the carrier and timing choices**. This is not a universal no-go result
or a demand to abandon the positive engineering theorem. Do not change
the graph, weights or time owner under WSI01. Any different source,
geometric lift or clock needs a fresh frozen ID and full ledger audit.
No T3 rescue or repeated local tuning follows this bounded screen.

The same-object ledger remained intact. All marked paths, roots and
null return states survive. 241/242 remain paused and the programme
goal remains active. Internal model review and document checks do not
constitute external peer review, formal verification or Route evidence.

## Reproducibility and evidence index

The inputs are exactly the version-1 graph, integer tests, uniform
rooted cylinder law and full prefix-arrow/time convention. The method
is strict hub descent, finite scans, compatible cylinder probabilities,
Borel prefix replacement and complete isotropy classification. There
are no numerical outputs, cutoffs or empirical extrapolations.

- [Candidate card and appended outcome](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence, source check, hashes and verification](evidence/README.md)
- [Parallel breadth and collision dispositions](evidence/scout-record.md)
- [Separate raw-card, comparison and adverse review](evidence/independent-review.md)
