# An owned nonlinear residue clock with uncountably many prime-time packets

Candidate ID: `ANG-20260920-NRF01`.
Paper ID: `287-nonlinear-two-seed-residue-flow`. Date: 2026-09-20.
Status: `OWNED NONLINEAR CLOCK; UNCOUNTABLE PRIME-PACKET MULTIPLICITY — STOP / FORK`.
Result type: exact owner construction and decisive fixed-core obstruction.

## Abstract

A full two-register profinite source consumes an actual residue, updates
its integer root by a greatest-irreducible-factor rule, and feeds a fixed
Logistic polynomial into the next seed. Its complete tail groupoid owns
a nonzero joint-Haar IMAGE clock. Thus the nonlinear source is not rejected
for lacking a nonsingular local-arrow owner. Nevertheless its full fixed
equation has uncountably many solutions at every prime root. Their complete
time groups are all (log p)Z, but distinct fixed cores are inequivalent
packets. The desired one-packet-per-prime structure therefore fails before
any higher-cycle search. Every noninteger seed and null fixed point remains
in the owner; no real or integer polynomial root count is substituted.

## 1. Frozen object, lineage and provenance

The [version-1 card](candidate-card.md) was frozen before this audit's
claims, SHA-256:

    451eb56764544d77e21ece5458e2a465bdcec756d23aca37aaa4a9b0e5cfd362

Let K=Z_hat and let h be normalized additive Haar. For each ordinary
integer m>=2, g(m) is its largest irreducible integer divisor. Such a
divisor exists: the least divisor greater than one has no proper divisor
greater than one. The largest among the finitely many irreducible divisors
is therefore defined. Equivalently g is the greatest prime factor, computed
from ordinary divisibility rather than a supplied list.

The full source and map are

    Y = coproduct_(n>=2) {n} x K^2,
    mu|_(root n) = h x h,
    j = x mod n,  0<=j<n,
    Q(y)=y(1-y),
    T(n,x,y)=(g(n+j), y, (x-j)/n+Q(y)).

All roots and seeds remain, including composite starting roots and every
noninteger or zero-divisor seed. The lineage is current prime/composite
divisibility observables -> residue-dependent factor/root update ->
Logistic-type two-register nonlinear deformation. This is not a conjugacy
to an earlier source, a finite-dimensional conservative map, or a
symplectic lift. Naturalness of g, Q, completion and measure remains OPEN.
Computing a prime-valued root is not already a prime closed-orbit theorem.

The [283 E-lane proposal](../283-nonlinear-residue-clock-screen/evidence/scout-record.md)
already combined division, register swapping and a quadratic term with a
different integer-pair feedback law. It was not admitted. This template
is not claimed as newly invented, and its old definition is not modified.
[273](../273-factor-branching-index-flow/candidate-card.md) supplies a
different factor-readout marked-path comparison, not our clock or returns.
[286](../286-radix-return-rigidity/candidate-card.md) excludes additional
seed operations and does not apply to this nonlinear K² owner.

## 2. Full local map and joint Haar scaling

**Lemma 1.** T is a local homeomorphism. On the clopen branch
U_(n,j)={n} x (j+nK) x K it maps homeomorphically onto the entire
root g(n+j), with inverse

    theta_(n,j)(u,v)=(n,j+n(v-Q(u)),u).

For every Borel B subset K², its inverse-branch image has measure

    mu(theta_(n,j)(B)) = (h x h)(B)/n.

The image of T is exactly the union of prime roots, not all Y.

*Proof.* Integer multiplication is injective on K, and nK is precisely
the kernel of reduction modulo n. Thus division after removing j is
well-defined and continuous. Direct substitution verifies both inverse
identities for theta, with the correct source residue j. Each target
is an entire K² copy, so the branch is a homeomorphism onto an open root.

To prove the Borel measure statement, first use the shear/swap map
(u,v)->(v-Q(u),u). For each u it translates the v coordinate, and Fubini
with Haar translation invariance proves preservation of joint Haar.
Multiplication of the first coordinate by n, followed by translation j,
then scales every Borel measure by 1/n: nK has Haar mass 1/n and its
normalized Haar is the transported measure. Combining these two exact
operations gives the formula. A formal polynomial determinant alone
would not have established the Borel claim.

Every g(n+j) is prime. Conversely root p is reached from n=p,j=0,
whose branch is onto the full root p. Thus composite roots have no
incoming T branch, but remain legitimate source components. QED.

The actual seed operation changes volume: it is not the joint-Haar
preserving Hénon replacement in 283. Nor does the singular image of
the one-coordinate quadratic map in 283 determine this two-coordinate
branch image; the retained first seed makes the shear invertible.

## 3. Same-object full groupoid clock

Keep ALL retained-lag arrows

    G={(z,m-k,w):T^m z=T^k w},

from w to z, with the full finite inverse-branch-pair topology. For a
finite inverse prefix alpha let D_alpha be the product of its consumed
integer roots, with D_empty=1. Iterating Lemma 1 gives image factor
1/D_alpha for every Borel terminal set. No linearity of the composed
polynomial prefix is needed.

**Proposition 2.** G is locally compact, Hausdorff, second-countable
and étale, and owns the continuous all-point IMAGE derivative and clock

    J(g)=D_beta/D_alpha,
    c(g)=log D_alpha-log D_beta

on an actual beta-to-alpha branch pair. Its real extension owns complete
continuous real translation on all source objects.

*Proof.* Finite inverse-branch pairs on clopen terminal congruence sets
give a countable compact-open basis. Source and range restrict to
homeomorphisms. Two presentations of one arrow have the same lag; the
longer one extends both prefixes along the same actual forward tail.
Restricting to its finite branch gives common refinements, compatible
inverse and composition. Endpoint coordinates and the retained integer
lag separate distinct arrows. This proves the stated topology without
assuming T onto or removing the composite roots.

For a Borel terminal B, source and target masses are respectively
mu(B)/D_beta and mu(B)/D_alpha. Their ratio gives J. Synchronous
extension multiplies both D values by the same tail product, so this
ratio is well-defined independently of presentation. Ratios multiply
under composition and invert under inverse; c is additive. Both are
locally constant on bisections. Source measure has full support there,
so the continuous derivative version is uniquely determined even at
null points: a continuous discrepancy would persist on an open set
of positive measure.

On Y x R use arrows (w,u)->(z,u+c(g)), with product topology on
G x R. Source/range are locally homeomorphisms and translation in the
real coordinate is jointly continuous, two-sided and complete. QED.

Positive clock orientation is inverse-prefix insertion. No positive
roof, log-prime period or time from a separate geometry was supplied.
This proposition does not assert that the coarse orbit space is
Hausdorff or that its abstract cyclic packets are embedded circles.

## 4. The full fixed-state set

**Lemma 3.** There are no fixed states at composite roots. At every
prime p, the full fixed states are exactly

    F_p = {(p,z,z): z in K, p z^2=z}.

Equivalently, putting E_p={e in K:e^2=e, e in pK}, the map
e->(p,e/p,e/p) is a bijection from E_p to F_p.

*Proof.* A fixed root n satisfies n=g(n+j), hence n is prime, say p.
Since g(p+j)=p, p divides p+j. The standard digit range 0<=j<p
forces j=0. Conversely g(p)=p. Equality of the two seed coordinates
forces x=y=z; the remaining fixed equation is

    z=z/p+z(1-z),

equivalent to pz²=z. This polynomial equation itself forces z=0
modulo p, so division by p and the required zero digit are valid.
No zero-divisor factor is cancelled.

If z solves it, e=pz lies in pK and satisfies e²=e. Conversely, for
e in E_p write e=pz using integer injectivity. The idempotent equation
gives p(pz²-z)=0, and multiplication by p is injective on K, so
pz²=z. These constructions are inverse. QED.

**Proposition 4.** For each prime p, F_p has cardinality 2^(aleph_0).
Its only ordinary-integer seed is z=0. The union of all F_p is Haar-null
in the full source, despite that uncountable multiplicity.

*Proof.* At each prime power ell^a the only idempotents are 0 and 1:
if ell^a divides e(e-1), the coprime consecutive integer factors force
all powers of ell into one of them. Compatibility across powers makes
the choice constant for each prime ell. The Chinese remainder theorem
therefore identifies idempotents of K with independent binary choices
at all primes. The condition e in pK fixes the p choice to zero and
leaves every other prime choice free. There are countably infinitely
many other primes, hence 2^(aleph_0) choices. Each compatible family is
an actual profinite element, not a finite-modulus approximation.

For embedded integer z, the equality pz²=z is an ordinary integer
equality, since integers embed injectively in K. Its only integer
solution is zero. Thus every nonzero idempotent choice above supplies
a noninteger fixed seed. The argument applies unchanged to p=2.

Normalized Haar on K has no atoms: any singleton lies in a residue
coset of mass 1/m for every positive integer m. At each root the fixed
set lies in the diagonal {(x,y):x=y}, whose joint Haar measure is zero
by Fubini. Countably many roots still give a null fixed-state set. QED.

This is where an integer-only or real-polynomial fixed-point check
would give the wrong multiplicity. No restriction to the diagonal
was made in the source: it arose by solving the full fixed equation.

## 5. Complete stabilizers and the decisive multiplicity failure

**Theorem 5.** Each z_star in F_p has source isotropy with lags Z,
clock c(z_star,k,z_star)=k log p, and complete time-return group

    H_(z_star)=(log p)Z.

It owns a primitive cyclic-time packet with least time log p and
repetitions r log p. Distinct points of F_p own distinct packets.
Therefore for EVERY prime there are already uncountably many distinct
prime-time packets from fixed cores alone.

*Proof.* Since z_star is fixed, every integer lag occurs, and the
groupoid's retained-lag convention gives exactly one isotropy arrow
per lag. Each traversal of its actual branch consumes root p, so
Proposition 2 gives k log p, for all positive and negative k. This
is the full stabilizer, not a chosen subgroup. The clock kernel is
zero, so fixed-object isotropy in the real extension is trivial;
that is different from its nontrivial time-return group.

Two fixed cores have a common forward tail only when they are the
same full point: every forward iterate of each is that point itself.
Thus neither equality of p nor equality of log p identifies them.
Their finite preimages stay in their respective disjoint basins;
actual prefix arrows account for all those preimages without adding
a packet. Every real phase over a core belongs to its one time orbit
with the stated stabilizer. Proposition 4 proves the multiplicity.
QED.

This already violates the precommitted one-packet-per-prime target.
It is NOT a classification of all packets: nonfixed periodic cores,
their times and multiplicities remain unexamined. There is no need
to enumerate them after this decisive early stop.

## 6. Separately frozen NONLINEAR-OFF control

The control is the DIFFERENT full owner

    T_off(n,x,y)=(g(n+j), y, (x-j)/n),   j=x mod n.

Its branch inverse is (u,v)->(j+nv,u); the same explicit scale/swap
calculation gives branch factor 1/n. For its fixed-state test, root
equality again forces n=p prime,j=0 and x=y=z. The remaining equation
z=z/p gives (p-1)z=0, so integer injectivity yields z=0. Consequently
there is exactly one fixed core at each prime root in this control.

The nonlinear term thus changes the fixed-core multiplicity in this
precise comparison. The control's higher cycles and full target fit
are NOT classified, and it is not adopted as a repaired main candidate.
The current candidate's Q and full seed space remain unchanged.

## 7. Gate assessment and portfolio decision

| Obligation/control | Result and exact boundary |
|---|---|
| T0 full carrier and arrows | Established, including composite initial roots and non-onto T |
| T1 actual residue feedback / joint-Haar clock | Owned exact mechanism; arithmetic naturalness still OPEN |
| T2 fixed-core primitive and repetitions | Exact full stabilizers; uncountable same-prime multiplicity |
| Prime-single-packet target | FAIL already at fixed cores; STOP promotion |
| Integer versus complete K seeds | Noninteger fixed seeds essential, all retained |
| Null-state ownership | Continuous full-point clock fixed by full support, not reselected a.e. |
| NONLINEAR-OFF | One fixed core per prime only; not a repaired target or higher-cycle result |
| PROVES_TOO_MUCH | Factor readout and chosen polynomial are structural inputs, not a naturalness theorem |

Portfolio: **stop / fork**. Preserve the positive fact that the nonlinear
two-seed source owns a nonsingular, nonzero clock, and the decisive negative
fact that its full prime-time multiplicity is wrong. Do not remove
idempotents, retain only integer seeds, choose one representative, change
Q or attach a later operator to rescue the result.

The same-object ledger remained intact. T0 and scoped T1 are owner-level
facts only; T2 target fails. Classical symplectic base, positive-roof
suspension and A0/A1/A2 are NOT APPLICABLE. T3/operator/trace/determinant
NOT SUPPLIED / NOT PURSUED, formal coordinates UNASSIGNED, Route B NOT
INVOKED. No coarse-topology or geometric-circle result is inferred.

Next authorized decision: continue breadth from a fresh architecture/card
while preserving this fixed-core obstruction. Other cycles of this
stopped candidate are not the next task. 278/285/286 remain unchanged;
241/242 remain paused; the programme goal stays active.

## Evidence and disclosure

See the [claim ledger](claim-ledger.md), [evidence](evidence/README.md),
[internal review](evidence/independent-review.md) and [scout provenance](evidence/scout-record.md).
Methods are exact branch inversion, Borel Haar scaling, full tail isotropy,
the fixed equation and compatible prime-power idempotents. There is no
numerical computation, prime table, finite cutoff, fitted parameter or
external novelty claim. AI-assisted authorship follows ARS freezing and
internal adverse review; same-model/shared-context checks are not external
peer review, formal verification or independent-error guarantees.
