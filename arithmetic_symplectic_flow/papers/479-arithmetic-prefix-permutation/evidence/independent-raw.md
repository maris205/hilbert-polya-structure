# APP01 — frozen card-only independent derivation

Date: 2026-09-25. Candidate: `ANG-20260925-APP01`.
Package: `479-arithmetic-prefix-permutation`.
Reviewer: `pcr01_independent_review`, not the current author/helper.

## 0. Input, release and method

This derivation began only after the distinct RAW RELEASE reporting root's
full read of the 178-line CP1 report. Its sole scientific input is the
original 103-line `candidate-card.md`, reread here at 1–103 EOF (requested
1–140), SHA-256
`dee878be33686a7a14383adefb27c0228aea00ff05f9da1d894e20a11dd7086d`.
The unchanged scope receipt is
`c8f88d605e623b1eb38d5ec3a8746f08a198351dde47a330af6ee6621f40b433`.
No current author paper/README/ledger, other reviewer/helper answer, or
old proof was opened. No mathematical code, numerical experiment, network,
Git, PDF, new roof, periodic census or work on 480 was used.

The ARS bounded original-mathematics adaptation and complete instruction
reads are recorded in the immutable CP1 report. Here the method is direct
proof from the frozen definitions. No forced objections or numerical
review score is used. Shared history and the same model remain:
`NOT_CALIBRATED`, not blind, human, external or cross-model peer review.
The card's prior-selection/exposure disclosures remain in force; a
separate reviewer and delayed manuscript access do not erase them.

Derivation order is carrier/normalization, exact inverse atlas and original
IMAGE, then global clock and its gate, followed by the required complete
conditional history structure and the one authorized control-image test.
There is no search for a fixed point, cycle or periodic window below.

## 1. Original probability space and actual source partitions

Write the alphabet as B = {1,2,...}, reserving A for the arithmetic-OFF
owner. Let X = B^{N_0}, with its product Borel sigma-algebra. For a finite
word w = (w_0,...,w_{L-1}), write [w] for the whole cylinder of all w xi,
and p(w) = product_{i=0}^{L-1} rho(w_i), with p(empty) = 1.

The given marginal is positive and normalized, since

    sum_{a=1}^m 1/[a(a+1)] = 1 - 1/(m+1)  ->  1.

Thus the countable product probability mu = rho^{N_0} is defined on all X,
and mu([w]) = p(w). Cylinders generate the Borel sigma-algebra. No equal
countable weights are used. In particular, all individual sequences stay
in X even though mu({z}) = 0: every length-n prefix has mass at most
(1/2)^n. This observation is not permission to remove any such point.

Let P_D(a,b) mean 1<a<b and a divides b. Let P_N(a,b) mean 1<a<b and a
does not divide b. Unit/reversed pairs are witnesses for neither; P_N is
not the complement of P_D. For P = P_D or P_N define

    W_L(P) = {w in B^L : P(w_{L-2},w_{L-1}),
                        not P(w_i,w_{i+1}) for 0 <= i <= L-3}, L >= 2.

The earlier tests are empty when L = 2. For the four owners U, define

| U | Allowed source words W_U | Prefix operation pi_U |
| --- | --- | --- |
| M | union_{L>=2} W_L(P_D) | left rotation of that length |
| A | B^2 only | interchange the two coordinates |
| N | union_{L>=2} W_L(P_N) | left rotation of that length |
| R | union_{L>=2} W_L(P_D) | reversal of that length |

Let E_U = union_{w in W_U} [w]. This is Borel, being a countable union.
For M/N/R the cylinders in this union are disjoint: a first hit cannot
occur at two lengths, and distinct words of the same length have disjoint
cylinders. For A the length-two cylinders partition X, so E_A = X.
For the other three owners, X minus E_U is precisely the no-hit set.

On [w] define v = pi_U(w) and

    T_U(w xi) = v xi.

The disjoint source partition makes T_U a well-defined partial Borel map.
It has no outgoing value on X minus E_U. Every future application tests
the new entire sequence afresh. This construction includes all tails,
with no section, root memory, absorbing state or returning-subset choice.
It is a partial Borel symbolic owner, not a symplectic or physical flow.

## 2. Whole-cylinder inverse atlas and exact one-step incoming sets

For each own word w in W_U the actual restriction

    T_U|[w] : [w] -> [v],       v = pi_U(w),

is a Borel bijection with inverse

    theta_{U,w}(v xi) = w xi,  domain(theta_{U,w}) = [v].

Both identities hold at every point: theta_{U,w}(T_U(w xi)) = w xi and
T_U(theta_{U,w}(v xi)) = v xi. The second identity requires only that the
reconstructed source belongs to [w]; it does not require v xi in E_U.
Thus terminal targets, special tails and null points are not discarded.
The atlas is countable since it is indexed by a subset of the union of
the countable sets B^L. Its members are actual cylinder bijections.

An equivalent exact predecessor algorithm avoids guessing the source word.
For a target y = (b_0,b_1,...) and each integer L >= 2 define

    q_L(y) = (b_{L-1}, b_0,...,b_{L-2}, b_L,b_{L+1},...),
    r_L(y) = (b_{L-1}, b_{L-2},...,b_0, b_L,b_{L+1},...).

Here q_L inverts a left rotation and r_L inverts reversal. With braces
denoting sets, not multiplicity-bearing label lists, all four owners have

    Pre_M(y) = {q_L(y) : L>=2, prefix_L(q_L(y)) in W_L(P_D)},
    Pre_N(y) = {q_L(y) : L>=2, prefix_L(q_L(y)) in W_L(P_N)},
    Pre_R(y) = {r_L(y) : L>=2, prefix_L(r_L(y)) in W_L(P_D)},
    Pre_A(y) = {(b_1,b_0,b_2,b_3,...)}.

Every displayed member is an actual legal predecessor, by the two inverse
identities. Conversely, an actual predecessor x has one own first-hit
length L (or the fixed length 2 for A), and inverting its actual prefix
permutation reconstructs exactly x in the displayed set. Hence

    Pre_U(y) = {x in E_U : T_U x = y}

for every y in the full X, regardless of whether y itself has an outgoing
value. The enumeration is over every length, not a length cutoff. Target
cylinders may overlap; labels are not extra incoming points or arrows.
In particular, no assertion that the whole R map is an involution is
needed or follows merely from reversal being an involution at fixed L.

## 3. Every-Borel original IMAGE and the frozen all-point version

Fix any owner branch [w] -> [v] and a Borel set E subset [v]. Under the
Borel prefix/tail identification there is a Borel set F subset X with

    E = {v xi : xi in F},       theta_{U,w}(E) = {w xi : xi in F}.

The product measure therefore gives

    mu(E) = p(v) mu(F),         mu(theta_{U,w}(E)) = p(w) mu(F).

All factors p(v) are strictly positive. Consequently

    mu(theta_{U,w}(E)) = integral_E [p(w)/p(v)] dmu.

This holds for every Borel E, not just a generating class, since the
prefix/tail identification itself preserves the stated product factors.
The frozen every-point version on [v] is exactly

    J_{theta_{U,w}}(v xi) = p(w)/p(v).

For each of the four operations v is a permutation of w. Commutativity
of the finite product gives p(v) = p(w), including repeated letters.
Thus the specified version satisfies

    J_{theta_{U,w}}(y) = 1  for every y in [v], every own branch, every U.

This equality is algebraic at every point; it is not an a.e.-uniqueness
argument. Overlapping target cylinders give no version disagreement.
The actual forward branch is equally measure preserving on all Borel
subsets of its source. This is a branch statement; it does not assert
that a possibly many-to-one partial T_U is a global measure-preserving
automorphism, or replace a local Jacobian by a predecessor multiplicity.

## 4. Global own clock and decisive gate, before any periodic census

For z in E_U, the frozen definition uses its own actual branch:

    kappa_U(z) = -log J_actual(T_U z) = 0.

No kappa value on a terminal source is needed or fabricated. Put

    D_{U,0} = X,
    D_{U,r+1} = {z in D_{U,r} : T_U^r z in E_U},
    S_{U,r}(z) = sum_{j=0}^{r-1} kappa_U(T_U^j z) = 0, z in D_{U,r}.

The empty sum S_{U,0} is zero. The domains are Borel by induction and
encode all and only the legal iterates. Every retained history-pair clock
S_{U,r}(z)-S_{U,s}(w) is therefore zero, whatever the legal meeting point.

Any source cycle, if one exists, has total owned clock zero. Its repetitions
also have zero clock. More generally every isotropy arrow has zero clock,
so no height orbit can have a positive primitive period. Hence each of M,
A, N and R fails the requirement of a NONEMPTY positive primitive ledger.
This is a global clock obstruction, independently of where source cycles
may occur or how many there are. The frozen main gate is STOP / FORK.

No periodic point has been located, tested or counted to reach this gate.
No repair by a positive roof, branch count, density or selected subset is
made. The remainder supplies the promised full history and phase objects;
it does not reopen the periodic census after the decisive obstruction.

## 5. Complete actual retained-lag groupoid and cocycle

Fix one owner U throughout this section and suppress U in the notation.
The full groupoid has units X and arrows

    G = {(z,r-s,w) : r,s>=0, z in D_r, w in D_s, T^r z = T^s w}.

An arrow (z,k,w) has source w and range z. Different witnesses for the
same triple are the same arrow. Distinct lags at the same endpoint pair
remain distinct. Units (z,0,z) exist even at no-hit and terminal points.
Inversion is (z,k,w)^-1 = (w,-k,z), and composition is

    (z,k,w)(w,l,u) = (z,k+l,u).

For completeness, suppose witnesses for the two factors are (r,s) and
(a,b). If a>=s, legally continue T^r z = T^s w for a-s steps to obtain
T^{r+a-s}z = T^b u. If s>=a, legally continue T^b u = T^a w for s-a
steps to obtain T^r z = T^{b+s-a}u. These continuations exist because the
corresponding segment of the w history exists. In both cases the lag is
r-s+a-b, proving closure without assuming a total map. Associativity,
inverses and units follow from the triple operations.

Define

    c(z,r-s,w) = S_r(z)-S_s(w) = 0.

It descends to triples, since every witness gives zero, and adds under
composition. It is a Borel cocycle on the countable Borel history atlas.
The required forward-arrow sign is explicitly

    (Tz,-1,z),  witnesses (0,1),  c = -kappa(z) = 0, z in E_U.

The trivial clock does not discard lag, collapse source packets, identify
all units, or remove nontrivial source isotropy when it exists.

### 5.1 Every-Borel history-pair IMAGE

A finite legal itinerary fixes finitely many successive own branch words.
Let N be the largest of their lengths. All steps are permutations of the
first N coordinates, with the remaining tail untouched. When a step of
length N is specified, its entire prefix word, pulled back by preceding
permutations, fixes the initial N-letter word. Thus the consistent
itinerary source is one whole cylinder (or empty), and T^r on that source
is a cylinder bijection given by a permutation of its first N letters.
Its exact inverse and forward measure versions are both 1. Equivalently,
this follows by composing the branch identities of Section 3, restricted
to the legal itinerary domains. The zero-step itinerary is identity on X.
There are countably many finite itineraries, and they cover every legal
finite history; no uniform bound on N or on the number of steps is used.

Take two such forward history charts F:U_0 -> V and Q:W_0 -> Y, for r
and s steps. On their common-meeting image K = V intersect Y define

    alpha = F^-1 o Q : Q^-1(K) -> F^-1(K).

It is the history-pair bisection w -> z with arrow (z,r-s,w). For every
Borel E subset Q^-1(K), both original branch identities give

    mu(alpha(E)) = mu(Q(E)) = mu(E)
                = integral_E exp[-c(alpha(w),r-s,w)] dmu(w).

The version exp(-c) = 1 holds at every chart point, including null points.
The countable set of all such charts covers all arrows, with equal triples
identified, not summed as new arrows. No incoming chart is lost when one
of its endpoints has no further outgoing action.

## 6. Exact all-depth incoming recursion and full orbit tests

For the same fixed owner, take Pre from the explicit owner-specific
formulas in Section 2 and set

    Pre^0(y) = {y},
    Pre^{n+1}(y) = union_{v in Pre^n(y)} Pre(v).

Induction proves the exact identity, for every y and every n>=0,

    Pre^n(y) = {x in D_n : T^n x = y}.

The base n=0 is identity. For the induction step, T^{n+1}x=y is equivalent
to x in E, Tx in D_n and T^n(Tx)=y, exactly the displayed union. This
establishes both soundness and exhaustiveness, without length/depth cutoff
or a target-survival hypothesis. It applies separately to M, A, N and R.

All finite incoming histories ending at y are the compatible chains
x_0=y, x_1,...,x_n with x_{j+1} in Pre(x_j). All infinite incoming
histories are exactly the infinite compatible chains satisfying the same
condition at every j. This is an exact characterization, not an assertion
that a compatible infinite chain exists for every y. In a countably
branching tree, nonempty sets at every finite depth alone do not justify
such an assertion; compatibility is explicitly retained.

For any base point z, the complete set of arrows with range z is

    G^z = {(z,r-s,w) : r>=0, z in D_r, s>=0,
                       w in Pre^s(T^r z)},

with equal triples deduplicated. Therefore the full source orbit is

    O(z) = union_{r>=0, z in D_r} union_{s>=0} Pre^s(T^r z).

This is an exact necessary-and-sufficient test, not an upper envelope:
the recursion supplies actual witnesses for sufficiency, and every arrow
has a witness captured by one of the terms for necessity. A specific lag
k is present from w to z exactly when one can choose r,s in this formula
with r-s=k. All terminal and transient incoming branches are included.

If z is terminal, only r=0 is legal and O(z) = union_{s>=0} Pre^s(z).
This does not assert that z is isolated or that its incoming sets are
nonempty beyond depth zero. If z has finitely many outgoing steps, all
legal r up to that endpoint are retained. If it never terminates, every
legal forward segment is retained regardless of eventual periodicity.
No terminal is converted into a fixed point by an added outgoing loop.

## 7. All kernels, conditional source isotropy and extension isotropy

The lag homomorphism is ell(z,k,w)=k. The exact kernels are

    ker ell = {(z,0,w) : some n>=0 has z,w in D_n and T^n z = T^n w},
    ker c = G,
    ker(ell,c) = ker ell.

These formulas include zero-depth units and every actual equal-depth
merger. They do not replace ker ell by the diagonal, or confuse the
vanishing clock with vanishing lag. The incoming recursion above is an
exact test for all the displayed memberships on the full source.

For source isotropy at z write

    I_z = {k in Z : (z,k,z) in G}.

If the forward path terminates, I_z = {0}. Indeed a repeated point at
two legal times r>s would repeat the legal block from s to r forever,
contradicting termination. If the path is infinite but not eventually
periodic, no two iterates agree and again I_z = {0}.

If the path is eventually periodic with least eventual cycle length p>=1,
then I_z = p Z, including when z is transient before the cycle. To see
sufficiency, place both witness times beyond cycle entry with difference
any chosen multiple of p. Conversely any nonzero repeated-time witness
creates a cycle, and on the eventual least-p cycle its time difference
must be divisible by p. Negative lags follow by inversion. Thus these
cases exhaust all z without determining any periodic location.

Retain the full extension X times R, with arrows

    (w,h) -> (z,h+c(z,k,w)) = (z,h).

Since c is zero, every source-isotropy arrow survives at every height.
The extension isotropy at (z,h) is I_z: either the trivial group or p Z
in the conditional eventual-cycle case. This is a group of retained-lag
arrows, not a nonzero real period group. At a least-p source cycle the
positive-lag generator has clock zero; its m-fold repetition has lag mp
and clock zero. The same statement holds at transient points in that
eventual cycle component. No nonzero clock generator is created by it.

## 8. Entire H, all real phases and uncollapsed packets

The full extension orbit at (z,h) is exactly

    O_tilde(z,h) = O(z) times {h}.

Necessity follows because no arrow changes height; sufficiency follows
from the complete source-orbit test in Section 6. In particular,

    (z,h) and (w,k) have the same extension orbit
    iff h=k and some legal r,s satisfy T^r z = T^s w.

Write height translation as theta_t[O_tilde(z,h)] = [O_tilde(z,h+t)].
Its ENTIRE stabilizer, not just an exhibited subgroup, is

    H_z = {t in R : [O_tilde(z,h+t)] = [O_tilde(z,h)]} = {0}.

There are no other stabilizers because equality of the displayed sets
forces equality of their height coordinates. Equivalently H_z=c(I_z)
and c(I_z)={0} in both source-isotropy cases. This conclusion includes all
terminal, transient, non-eventual and hypothetical cycle components.

For each distinct source packet O(z), every real h is a distinct phase
class; the phase space for that packet is R/H_z = R, not a circle and not
a single point. Height translation is free on this orbit set. Distinct
source packets remain distinct even if their heights and clocks coincide.
This also proves globally that no positive-period height orbit, hence no
nonempty positive primitive ledger or its positive repetitions, exists.
It asserts neither a smooth orbit quotient nor a positive physical roof.

## 9. The sole concrete forward-image control test

Use exactly z*=(3,2,4,5,1,1,...), with no iteration of any resulting image.
For D, (3,2) fails the strict order and (2,4) is the first hit, so L=3.
For N, (3,2) fails the strict order, (2,4) fails nondivisibility, and
(4,5) is the first hit, so L=4. A uses L=2 by definition.

| Owner | Own first prefix at z* | One actual image T_U z* |
| --- | --- | --- |
| M | (3,2,4), left rotation | (2,4,3,5,1,1,...) |
| A | (3,2), swap | (2,3,4,5,1,1,...) |
| N | (3,2,4,5), left rotation | (2,4,5,3,1,1,...) |
| R | (3,2,4), reversal | (4,2,3,5,1,1,...) |

All four images are distinct. Thus the frozen predicate and operation
choices do change actual dynamics in this authorized comparison. This is
not a periodic test, a returning core, a cycle witness or prime selectivity.
Each control still has its own atlas, histories, kernels, isotropy and
phases as proved above; their clocks were not borrowed from MAIN.

## 10. Interpretation, controls and final bounded status

Original-measure ownership succeeds at the stated Borel branch/history
level. The same object is kept throughout each owner's chain: its own
parser and actual permutation, original product mu, exact inverse version,
owned kappa, retained-lag groupoid and real-height extension. No clock or
periodic data are transferred from a control to MAIN.

The decisive obstruction is not that an arithmetic rule has no dynamical
effect: the single allowed test shows an effect. It is that a finite
prefix permutation preserves the product of identical marginal factors,
so its prescribed every-point Jacobian and clock cannot distinguish that
arithmetic effect. The cancellation uses no particular divisor identity
or numerical coincidence. In this sense the proposed clock mechanism
PROVES_TOO_MUCH across the frozen controls: each has the same obstruction
despite different actual images. This is not authorization to change the
marginal, reweight a subset, count inverse labels or insert a clock.

Main outcome: OWNED PREFIX IMAGE; GLOBAL ZERO CLOCK — STOP / FORK.
This is a scoped negative result for a nonempty positive primitive ledger,
not a nonexistence theorem for source cycles. Source periodic locations,
their census and their multiplicities remain explicitly OPEN and untested
under this gate. General conditional isotropy/repetition formulas and the
complete inverse-recursive incoming/orbit tests do not constitute a census.
Strong naturalness, prime selection, global novelty and nonconjugacy are
not established. No classical conservative/symplectic lift is asserted.

Classical fields: NOT APPLICABLE. Arithmetic T1: NOT PASSED. T3: NOT AUDITED.
Formal coordinates: UNASSIGNED. Route B: NOT INVOKED. No trace, operator,
zeta, determinant, zero-data or Riemann hypothesis claim is made.

This raw derivation is to remain immutable after full self-read and hash
receipt. HOLD for root's full read and a distinct PAPER UNLOCK before any
author-surface comparison, CP2/CP3 review or author revision discussion.
