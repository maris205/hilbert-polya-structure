# A non-atomic arithmetic index clock with mixed primitive returns

**Paper ID:** `273-factor-branching-index-flow`  
**Candidate ID:** `ANG-20260919-FBI01`  
**Date:** 2026-09-19.  
**Status:** `OWNED NON-ATOMIC PRIME CLOCK; MIXED PRIMITIVE COLLISIONS — STOP / FORK`.  
**Type:** exact broadened-owner source, measure and first-return audit.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

We freeze a full branching graph on positive integer pairs. The current
greatest factor determines the number of branches, and the branch mark
changes the next arithmetic state. Its complete one-sided path space
has a full-support non-atomic Markov measure. Prefix-replacement image
Jacobians give a continuous real cocycle and complete groupoid time
action, with no separately imposed prime roof. Each prime p has exactly
one primitive packet of least time log p. However, a retained marked
two-cycle has least time 2 log 5 and is not the second traversal of the
prime-5 packet. A second precommitted mixed four-cycle has least time
log 210. Thus the nonzero source-owned clock survives the atomic
obstruction of 272, but the full primitive ledger fails the prime-only
target. No branch, transient, packet or inverse arrow is removed; no
trace or operator is introduced after the decisive mixed-packet stop.

## 1. Frozen identity and lineage

All definitions belong to the [version-1 card](candidate-card.md).
For every s=(x,y) in V=N_(>0)^2 set

    d(s)=gpf(x+y),
    e=(s,j),  0<=j<d(s),
    source(e)=s,  target(e)=(y,gpf(x+y+j)).

Different marks remain different edges even if their endpoints agree.
Since x+y>=2, every vertex has finite outdegree d(s)>=2. Let X_s be
all infinite edge paths starting at s, and X the disjoint union of
all X_s. The map sigma deletes the first edge. Define the measure by

    mu(X_s)=1,
    mu([e_0...e_(m−1)])=1/D_m,
    D_m=product_(i<m)d(source(e_i)),        D_0=1.

The groupoid retains the triples

    G={(xi,m−n,eta):m,n>=0, sigma^m xi=sigma^n eta},

with source eta, range xi, and integer lag m−n. Its local arrows replace
a finite prefix beta by a prefix alpha ending at the same vertex.
The proposed clock is minus the logarithm of that actual local image
Jacobian, not a time assigned to a prime label.

| Field | Same frozen owner / boundary |
| --- | --- |
| Source | Every initial integer pair and every marked infinite path |
| Arithmetic evolution | Current factor readout; j changes the next state and hence subsequent branch count |
| Measure | Full rooted Markov measure above; sigma-finite, not normalized over all roots |
| Clock | Derived prefix-replacement image cocycle, Section 3 |
| Time | Real translation in the full cocycle extension of G |
| Packets | Full time-return orbits of extension isomorphism classes, preserving marked-edge multiplicity |
| Classical symplectic base, mapping torus, Hamiltonian/contact lift | NOT APPLICABLE / NOT SUPPLIED |
| Trace, determinant, operator, quantum owner | NOT SUPPLIED; T3 not pursued |

The [prior-work arrow](../../docs/prior_work/README.md) is precise:
current divisibility/prime-composite observables -> greatest-factor
readout -> second-order branching symbolic feedback -> measured
groupoid realization. Both d(s) and gpf(x+y+j) are re-evaluated from
the current integers; j affects the arithmetic state rather than an
unrelated extra fiber. These are observables, not invariants. No prime
table, frozen prime vector, fitted parameter, zero data or prescribed
prime-log roof is an input. This is a broadened replacement of the
symbolic source interface, not a Logistic/Hénon semiconjugacy.

Naturalness is still OPEN: using d(s)=gpf(x+y), this marked transition
law and uniform branch probabilities are structural choices. Deriving
their clock exactly does not prove that arithmetic uniquely selects
those choices. The j=0 subgraph contains the source used in
[266](../266-prime-source-return-rescreen/paper.md), but its old full
cycle classification does not classify this larger graph. We verify
the two precommitted mixed words directly below.

## 2. Complete path space, measure and groupoid topology

### Proposition 1 — non-atomic full owner, with a non-surjective shift

Each X_s is a nonempty compact metrizable zero-dimensional space.
X is locally compact Hausdorff and second countable. The cylinder
prescription defines a sigma-finite locally finite Radon measure mu
with full support and no atoms. The full sigma is a local homeomorphism
but is not onto X.

**Proof.** Every vertex has a finite nonempty set of outgoing marked
edges. At each fixed depth there are only finitely many prefixes from
a fixed root. The compatible finite-prefix inverse limit is therefore
nonempty and compact, with its cylinder topology. Cylinders are clopen
and metrizable by their first differing edge. Taking a countable
disjoint union over roots gives the stated properties of X and a
countable compact-open cylinder basis.

The mass of every prefix is the sum of its d(s) equal child masses.
The compatible probability distributions on each finite-prefix level
thus extend uniquely to a Borel probability on X_s. Sum these measures
over all roots to obtain mu. Every cylinder has positive measure; each
root component has mass one. This gives full support, sigma-finiteness
and local finiteness; the compact-metric component probabilities are
Radon. For any path xi, its length-m cylinder has measure at most
2^(−m). Continuity from above implies mu({xi})=0.

On a first-edge cylinder [e], sigma is a homeomorphism onto X_target(e),
with inverse given by prefixing e. It is consequently a local
homeomorphism. Every target vertex has prime second coordinate, so,
for example, X_(1,4) is outside its image. More precisely all roots
(x,p) with p prime do occur in its image: choose k with p^k>x, use
the predecessor (p^k−x,x), and its j=0 edge. This proves both the
non-surjectivity and its exact root scope, without removing any root. ∎

For finite prefixes alpha and beta ending at the same vertex v, let

    Z(alpha,beta)={(alpha zeta, |alpha|−|beta|, beta zeta):zeta in X_v}.

Length-zero prefixes are included. Multiplication and inversion are

    (xi,k,eta)(eta,l,zeta)=(xi,k+l,zeta),
    (xi,k,eta)^−1=(eta,−k,xi).

To verify multiplication belongs to G, enlarge the two prefix-length
representations until their powers on the common middle path agree.
They then give an equality of forward tails for the displayed product.
These formulas also verify associativity, units and inverse laws.

### Proposition 2 — full Hausdorff étale groupoid

The sets Z(alpha,beta) form a countable basis of compact-open bisections
for a locally compact Hausdorff topological groupoid G. No surjectivity
of sigma is required.

**Proof.** Each arrow has finite prefixes giving one such neighborhood.
If two basis sets intersect, their lags agree. At an intersecting arrow,
the longer prefix pair is obtained from the shorter pair by appending
the SAME finite word to both prefixes: the two residual tails are equal.
This is a simultaneous refinement, and gives the usual nested-cylinder
intersection basis. Range and source identify each basis set with its
respective cylinder; the tail parameter identifies it with compact X_v.
Inversion exchanges the prefixes. Composition on compatible refined
bisections is another prefix replacement, so is continuous, as are
range and source. Both are local homeomorphisms.

Distinct arrows are separated either by their integer lags or by
disjoint cylinders at a differing source or range path. Thus G is
Hausdorff. Compact-open bisections give local compactness, and the
countable set of finite prefix pairs gives second countability. ∎

This is standard graph/local-homeomorphism groupoid language; see
Aidan Sims, [Hausdorff étale groupoids and their C*-algebras, Examples 2.4.6–2.4.7](https://www.aidansims.com/papers/Sims2017.pdf).
That source uses the opposite graph source/range naming convention.
The outward paths and prefix laws above are proved in our stated
convention; no onto-shift assumption or C*-algebra theorem is imported.

## 3. Borel branch index and the actual time extension

### Proposition 3 — a well-defined continuous image clock

On a prefix replacement theta:beta zeta↦alpha zeta, where
m=|alpha| and n=|beta|, every Borel E contained in [beta] satisfies

    mu(theta E)=(D_n(beta)/D_m(alpha)) mu(E).

Consequently the pointwise continuous cocycle is

    c(xi,m−n,eta)=log D_m(xi)−log D_n(eta).

It is independent of the representing m,n and of simultaneous prefix
refinements, and is additive on composable groupoid arrows.

**Proof.** If alpha ends at v, then for any Borel B contained in X_v,

    mu(alpha B)=mu_v(B)/D_m(alpha).

This identity holds first on tail cylinders by the defining product
rule, then on all Borel sets by uniqueness of finite measures on the
generating cylinder algebra. Apply it to alpha B and beta B to obtain
the image ratio. This also fixes the sign: deleting a first edge has
image Jacobian d(s); its inverse prefixing branch has clock +log d(s).

For a triple with a second representation m',n', equality of lags
means m'−m=n'−n. Enlarge the shorter representation. The extra factors
in D on the two sides agree along their common tail and cancel. Thus
the formula belongs to the arrow triple, not its presentation.
The same argument checks bisection refinement. To check composition,
align the forward lengths on the common middle path; its log D then
cancels from the sum. Units have c=0 and inverses negate c. On each
prefix bisection c is constant, hence continuous. ∎

The measure is non-atomic, including at periodic paths. Nonetheless
the continuous image Jacobian is fixed on those paths too: each
bisection's source cylinder has full-support measure. Two continuous
versions agreeing almost everywhere cannot differ at a point without
differing on a positive-measure open set. We use this continuous
version, not arbitrary reassignment on null periodic points.

The extension objects are X×R; the arrow (g,u), with g from eta to xi,
goes from (eta,u) to (xi,u+c(g)). Its topology is G×R. On a bisection,
source and range are homeomorphisms onto open object subsets, with
the real coordinate shifted by the continuous c. It is therefore a
locally compact Hausdorff étale groupoid. Translation u↦u+t is a
jointly continuous automorphism for all real t, with inverse t↦−t.
This is the complete physical-time owner. No extra roof has been
inserted, and no claim of a Hausdorff coarse space or embedded flow
circle follows merely from these arrow/object properties.

## 4. Actual returns, eventual periods and packet equivalence

### Proposition 4 — full return rule without a graph-cycle census

A path has nontrivial base isotropy exactly when its MARKED edge
sequence is eventually periodic. If the least eventual edge period
is h and the product of d(s) over that primitive cyclic word is B,
then

    isotropy lags = h Z,
    H_xi = (log B) Z,       B>=2^h,

and its least positive time is log B, with repeats r log B. A path
that is not eventually periodic has H_xi={0}. Extension fixed-object
isotropy is trivial at every path. Returning packets are in one-to-one
correspondence with primitive marked edge cycles modulo cyclic phase.

**Proof.** A nonzero lag means sigma^m xi=sigma^n xi with m!=n,
precisely eventual repetition of a finite marked edge word. The lags
form a subgroup of Z by the groupoid laws; its positive generator h
is the least eventual period. Choose N beyond the transient prefix.
The positive generator is represented by m=N+h,n=N, for which

    c=log(D_(N+h)(xi)/D_N(xi))=log B>0.

Every other lag is a multiple of h, and concatenation around the
period gives the stated clock multiple; negative lags give negatives.
The product B is invariant under cyclic phase. Thus the time group
is discrete with exactly the claimed positive generator. If no
nonzero lag exists, only the unit isotropy arrow remains.

For extension fixed-object isotropy both the endpoints and the real
coordinate must agree. In the periodic case c=q log B vanishes only
for q=0, while the nonperiodic case has no nonunit isotropy already.
This proves the triviality assertion without collapsing lag labels.

Every eventual periodic path has an actual groupoid arrow to a purely
periodic tail. Conversely two purely periodic edge words have equal
shifted tails exactly when they represent the same primitive marked
cycle up to cyclic phase. A groupoid arrow followed by actual time
translation aligns any real coordinates; a finite chain yields
nothing larger because time commutes with arrows. This proves the
packet statement, retaining rather than deleting transient paths. ∎

These are groupoid time-return packets: each cyclic time orbit is an
abstract homogeneous R-set R/((log B)Z). No identification with its
coarse subspace topology or a classical geometric closed orbit is
asserted. There is no need to list all graph cycles to prove the rule.

### Proposition 5 — exactly one log-prime packet per prime

The only self-loop edges are ((p,p),0), one for each prime p. Their
infinite repetitions have least time log p. Moreover these are all
packets whose least time is the logarithm of a prime.

**Proof.** A self-loop at (x,y) requires x=y=n and
gpf(2n+j)=n. Since a greatest prime factor is prime, n must be a
prime p. Then d(p,p)=p and 0<=j<p. For gpf(2p+j) to equal p, p
must divide 2p+j, forcing j=0 in this range. This edge works since
gpf(2p)=p. Unit and composite vertices give no self-loop.

The marked period is one and B=d(p,p)=p, so Proposition 4 gives
log p. Any different primitive cycle of length h>=2 has B a product
of at least two integers >=2, hence composite. Such a cycle cannot
have least time log p. All eventual tails of the displayed loop
belong to its one packet, not extra copies of that packet. ∎

The cocycle is therefore not an endpoint state difference, even as
an arbitrary real-valued function: a state difference would vanish
on every isotropy arrow, whereas the prime loop has c=log p>0.
This is a genuine escape from the positive-atom hypothesis of
[272](../272-power-divisibility-index-clock/paper.md), not a
contradiction of that paper. The change is the full non-atomic
branching owner, not a reweighting of its discrete source atoms.

## 5. The precommitted mixed controls stop target promotion

The first mixed marked cycle is

    (2,3) --j=3--> (3,2) --j=1--> (2,3).

Both outdegrees are gpf(5)=5. The first update uses gpf(8)=2 and
the second gpf(6)=3; both marks lie in {0,1,2,3,4}. The two source
vertices are distinct, so its least marked edge period is two. Thus

    B=25,       H=(log 25) Z,       T_min=2 log 5.

This is a primitive packet, not the second repetition of the
prime-5 packet. Their infinite tails alternate (2,3),(3,2) versus
remaining at (5,5), so no forward shifts have equal marked tails.
They are distinct groupoid/time packets despite the collision of
this primitive time with a repetition time of the prime-5 packet.
The full prime-only primitive target already fails here.

The second fixed control in the card is verified without expanding
the cycle search:

| Source vertex | j | Current degree d | Target |
| --- | --- | --- | --- |
| (7,3) | 0 | gpf(10)=5 | (3,5) |
| (3,5) | 0 | gpf(8)=2 | (5,2) |
| (5,2) | 0 | gpf(7)=7 | (2,7) |
| (2,7) | 0 | gpf(9)=3 | (7,3) |

All four vertices differ, so the least marked period is four. On
this SAME measure/clock owner its least positive time is

    log(5*2*7*3)=log 210.

Its periodic tail is distinct from every constant loop and the
two-cycle. This is not an old GPF-flow time transferred by analogy:
the four degrees above derive it in this new groupoid. These are the
two predeclared controls only. No further cycle census, degree
adjustment, branch filtering or analytic product follows the stop.

## 6. Gates, adverse controls and decision

| Gate/control | Result on this owner | Limit |
| --- | --- | --- |
| T0: full source, topology, measure and time | ESTABLISHED, locally compact Hausdorff groupoid and complete time | Coarse embedded-circle geometry not established |
| T1: source feedback and branch-index clock | Exact non-atomic image clock; nonzero prime returns; not an endpoint difference | Degree law, transition rule and uniform measure remain designed; naturalness OPEN |
| T2: prime and mixed returns | One log-prime packet per prime, plus independent mixed primitives | Prime-only full ledger FAILS; other cycles not enumerated |
| T3 | NOT SUPPLIED / NOT PURSUED | No trace, zeta, operator or target correction |
| Composite/unit self-loop control | No self-loops | Does not exclude longer mixed primitive cycles |
| Non-surjective shift | All nonimage roots and their futures retained | Local homeomorphism does not mean onto |
| Marks and transient prefixes | Full marked cycles counted; eventual tails identified only by actual arrows | Neither vertex-only collapse nor selected recurrent core |
| Null paths | Every point is null but the continuous clock is fixed by full support | No arbitrary null-stratum retiming |
| Equal time versus same packet | Primitive log 25 collides with a prime-5 repetition, yet packets differ | No multiplicity repair by relabelling |

Portfolio: **retain the scoped non-atomic source/clock advance; stop
target promotion; fork**. The decisive reason is an independent mixed
primitive packet, not the absence of a genuine logarithmic return
cocycle. This narrows the next search requirement: nonzero intrinsic
index time alone does not control mixed-word primitiveness. A changed
admissibility relation or branch rule would need a fresh card and
cannot delete these counterexamples under FBI01.

The same-object ledger remained intact. Classical A0/A1/A2 are NOT
APPLICABLE, formal coordinates UNASSIGNED, Route B NOT INVOKED. This
is not a general impossibility theorem for non-atomic arithmetic
dynamics. 241/242 remain paused; the programme goal remains active.

## 7. Reproducibility and integrity

Inputs are the frozen graph, all paths, uniform rooted measure and
arrow/time conventions. Proofs use finite branching, compatible
cylinder measures, prefix replacement, subgroup structure of Z and
the two exact finite words. No numerical approximation, period cutoff,
optimization or scientific program was run. Arithmetic checks in the
table are exact, not a finite completeness argument for all cycles.

See the [claim ledger](claim-ledger.md), [evidence/source record](evidence/README.md),
[bounded scout dispositions](evidence/scout-record.md), and
[separate internal review](evidence/independent-review.md).
AI-assisted authorship and native model review were used. Shared
context/model lineage is not external peer review, formal proof
verification or evidence of independent errors. No old candidate,
Phase-I source, PDF or publication artifact was modified.
