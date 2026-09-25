# Frozen candidate — arithmetic successor, carry and gcd descent

**Candidate ID:** `ANG-20260920-SGC01`  
**Paper ID:** `279-successor-gcd-carry-flow`  
**Version:** 1; frozen 2026-09-20 before proof or computation.  
**Initial status:** `OPEN — FULL SUCCESSOR / GCD / CARRY OWNER AUDIT`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Full arithmetic state and deterministic update

Let K=Z_hat, with its full inverse-limit ring topology and normalized
additive Haar probability h. The full state is

    Y = coproduct_(n>=2) {n}×K,
    mu|_({n}×K) = h.

All integers n, all seeds x, negative and zero integer seeds and
every congruence coordinate remain. No units quotient, history
completion, selected itinerary or null-state deletion is allowed.
For j the representative of x mod n in {0,...,n−1}, freeze

    CARRY:      j=n−1                 T(n,x)=(n,(x+1)/n);
    SUCCESSOR:  j=0 or gcd(n,j)=1,
                with j!=n−1           T(n,x)=(n,x+1);
    GCD:        1<=j<=n−2,
                d=gcd(n,j)>=2         T(n,x)=(d,x/d).

The branches are exhaustive and disjoint as ordered above. Division
must be proved well-defined on its indicated congruence domain.
There is no independent scan variable, escape ray, prime predicate,
prime table, per-prime rule, stored acceptance bit or supplied roof.
The SAME arithmetic seed advances, carries, or divides; a gcd hit
changes both the modulus and seed. The particular priority and
branch design are declared, with their naturalness OPEN.

The lineage is prime/composite gcd observables -> full compatible
congruence state -> current-residue successor/carry -> Euclidean
feedback on that state and its modulus -> arithmetic groupoid.
This is a broadened realization, not a claimed Logistic/Henon
conjugacy or finite-dimensional symplectic lift.

## Full arrow, clock and packet owner

Establish T as a local homeomorphism and decide surjectivity without
changing Y. Freeze all retained-lag arrows

    G_T={(z,m−k,w): m,k>=0, T^m(z)=T^k(w)},

with source w, target z. Topology uses pairs of inverse branches
on arbitrary clopen arithmetic subsets of their common terminal
domain, not merely symbolic branch words. Do not adjoin all affine
maps or source translations because local formulas happen to be affine.

Derive the Borel IMAGE Jacobian for each branch and branch-pair
bisection from mu; only then define c=−log J using its proved
continuous full-arrow version. Branch image domains, restricted
inverse domains, sign, additivity, presentation independence and
null-point ownership are required. Rootwise additive homogeneity
is a source-measure condition, not claimed T-equivariance.

The real extension has units Y×R and arrows
(g,u):(w,u)->(z,u+c(g)), with G_T×R topology. Time translates u
by every real t. Prove complete continuous time; deterministic
zero-clock steps are not replaced by a positive roof. Positive
insertion-lag time must be distinguished from forward algorithm runtime.

For every z classify source isotropy, its clock image H_z=c(G_z^z),
and fixed-object extension isotropy separately. A cyclic-return
packet requires H_z=T0 Z with least T0>0; identify packets only by
actual arrows and real-time translation. Positive rth repetitions
are traversals of that same packet. No symbolic cycle is credited
without solving its full arithmetic state equation.

## Precommitted exact tests and adverse controls

1. Prove the complete local-homeomorphism/measure owner; derive all
   three branch domains and images, including n=2 and x=−1,0,1.
   Test a genuine modulus-changing state, such as (6,2).
2. Derive the clock and show why the restricted gcd inverse images
   do not justify importing all affine arrows. Check source
   translation and the conditional nature of Haar normalization.
3. Use modulus descent to constrain an ACTUAL periodic full orbit.
   On a constant modulus examine the affine equation of a word
   with r carry steps, including r=0. Prove any needed intersection
   property of rational numbers and K; K is NOT an integral domain.
4. Classify all integer-seed dynamics, positive, zero and negative,
   then all periodic and eventually periodic full states. Retain
   noninteger seeds whether or not their branch itinerary repeats.
5. Determine the least lag, actual least time, packet multiplicity
   and all repetitions. Keep p=2, composite 4 and 6, null points,
   and same-root different seeds as explicit discriminators.
6. Inspect closure of an extension orbit on a prime root, if cyclic
   packets occur. Establish only warranted coarse-quotient facts;
   abstract cyclic time groups do not imply embedded Hausdorff circles.
7. SOURCE-OFF comparator: replace every GCD branch by SUCCESSOR,
   retaining the CARRY rule and the whole Y, Haar, arrows/time recipe.
   Test all-integer packet contamination, including 4 versus a 2-repeat.
8. UNIT-ROOF comparator: the same noninvertible T does not itself
   become an invertible classical suspension. Merely counting its
   steps is an algorithmic-lag control, not an alternative owned flow.
9. PREDICATE comparator: for arbitrary A subset {2,3,...} containing
   2, keep CARRY; at j=1 when n>=3 and n not in A use (2,x), and
   use SUCCESSOR at every other non-carry branch. Keep all roots
   and seeds. Determine its complete packet ledger. This is a
   distinct theoretical encoding control, not input to SGC01;
   noncomputable A is not a claimed finite algorithm.

The image clock must be derived, not taken from 278. Any extra
primitive, missing full-state clock or changed owner stops the
corresponding promotion. Preserve a valid scoped construction but
stop natural-A0 promotion if source-program naturalness is unresolved.
No parameter tuning, trace/zeta rescue or further census is authorized
after a decisive failure. A changed carrier/action/clock needs a new ID.

## Collision, limits and review

Nearest actual definitions are [278](../278-haar-seeded-witness-flow/candidate-card.md)
(hub/scan/escape roots and residue consumption),
[274](../274-euclidean-residue-index-flow/candidate-card.md) (marked
residue-path branching), [238](../238-nonconfining-source-frontier/candidate-card.md)
(reversible finite divisor scan), [228](../228-gcd-defect-cocycle/candidate-card.md)
(gcd-defect register and symplectic unit-clock lift), and
[225](../225-euclid-edge-scattering/candidate-card.md) (word/port geometry).
Targeted definition checks found no identical owner; this is not a
global novelty claim. No prior theorem, review, clock or credit transfers.

This is a separately type-labelled ANG candidate. Classical
(M,omega,F,tau), mapping torus and A0/A1/A2 are NOT APPLICABLE;
Hamiltonian/contact/quantum owners NOT SUPPLIED. T0–T2 are owner-level
labels only; T3 NOT SUPPLIED / NOT PURSUED. No scientific numerical
run, PDF/LaTeX, staging, commit, publication or external-model upload.
Root owns integration; native raw-card review precedes manuscript
comparison and final adverse review. Shared model/context limitations
are disclosed; internal review is not external peer review. 241/242
remain paused; the programme goal remains active.

## Appended audit outcome — 2026-09-20

**Final status:** `OWNED ARITHMETIC CARRY CLOCK; EXTRA PRIME-TWO PACKET — STOP / FORK`.

The original version-1 definition above is unchanged, SHA-256
`440e90ebb6f3c4e3531b24d8a241df8184f6687f0db2d81ebf94b633affefcc7`.
The [paper](paper.md) proves the complete arithmetic local-homeomorphism
owner, its exact Haar image clock and exhaustive full-state returns.
Every odd prime has one least-log-p packet, but root 2 has two:
the fixed seed 1 and the actual 2<->3 cycle. Each has least time
log 2. They never share a forward tail, so the second is an extra
primitive, not a repetition of the first.

All periodic seeds are positive integers; every integer seed eventually
enters one of the classified cycles. All nonintegers remain, never
become integer and have no actual return. The full returning locus
is countable, dense and Haar-null. Some extension orbits are nonclosed,
so the coarse quotient is not T1. SOURCE-OFF and PREDICATE retain
the duplicate at 2; architecture naturalness remains OPEN.

Portfolio: **stop target promotion / fork**. Preserve the scoped
source/index construction and complete negative packet record, without
special-case retuning, state deletion or T3 rescue. T0 is established,
T1 scoped with naturalness OPEN, and T2's prime-single-packet target
fails. T3 NOT SUPPLIED / NOT PURSUED; classical A0/A1/A2 NOT APPLICABLE,
formal UNASSIGNED and B NOT INVOKED. Same-object ledger intact.
The [claim ledger](claim-ledger.md) and [evidence](evidence/README.md)
record review and verification separately from mathematical claims.
241/242 remain paused; the programme goal remains active.
