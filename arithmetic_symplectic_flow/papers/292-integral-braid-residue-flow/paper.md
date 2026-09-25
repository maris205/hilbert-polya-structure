# Integral refactorization gives owned clocks but composite primitive packets

Candidate ID: `ANG-20260920-BRF01`.
Paper ID: `292-integral-braid-residue-flow`. Date: 2026-09-20.
Status: `OWNED REFACTORIZATION CLOCK; COMPOSITE PRIMITIVES AND MISSING ODD-PRIME TIMES — STOP / FORK`.
Result type: exact full-state arithmetic/groupoid and return audit.

## Abstract

We test a new three-integer divisibility rule with actual residue
feedback, rather than a stationary witness-zero acceptor. Its admissible
branches implement an integral three-letter unipotent refactorization.
On the entire profinite two-register source, each branch owns a joint
Haar index and the full tail groupoid owns the resulting time cocycle.
The total integer sum increases by the consumed digit, forcing every
periodic digit to be zero. The remaining root operation is an involution;
integer matrix arguments exclude every nonzero profinite periodic seed.
Thus the entire primitive ledger is explicit: fixed cores have times
log(2a), and nonfixed two-cycles have times log(b(a+c)). Distinct
composite primitives remain. Only log 2 is a prime primitive time;
for odd prime p there are instead exactly (p-1)/2 primitives of time
2 log p. The candidate stops target promotion, without changing a
clock or deleting a state. Analytic and quantum work is not pursued.

## 1. Frozen identity, lineage and scope

The original [card](candidate-card.md) has SHA-256

    c6a64634a95a0cbcae762b80450deeec84768a6ab84c450fd11a56ac3dddc3d0

The definition-only scout proposed the rule before the root freeze;
the mathematical claims below follow that freeze. All positive integers
a,b,c and all seeds (x,y) in K², K=Z_hat, are retained. Each root fibre
has normalized joint additive Haar measure. At a source state set

    d=a+c, j=x mod d in {0,...,d-1}, u=b+j.

On EXACTLY the domain d|au and d|cu define

    T(a,b,c,x,y)=(uc/d,d,ua/d,y,(x-j)/d+y).

All other objects are terminal, not erased. The concrete lineage is
prime/composite divisibility admissibility -> integral refactorization
of three arithmetic symbols -> digit feedback into their next factors.
This is not a Logistic/Hénon conjugacy or a symplectic lift. Completion,
measure and time extension are declared designs; naturalness is OPEN.

| Object | Owner in this paper | Limit |
|---|---|---|
| Arithmetic action | The displayed partial T on every root and seed | No external prime selector |
| Symbolic integrality | d|a(b+j), d|c(b+j) on the same branch | Actual arithmetic, not a prime-return theorem |
| Clock | Joint-Haar IMAGE law on actual inverse branches | Not a supplied roof |
| Packets/repeats | Full retained-lag tail groupoid and its real extension | No arbitrary packet identification |
| Coarse topology | Full orbit quotient retained | Embedded circles / Hausdorffness NOT AUDITED |
| Operator/zeta/trace/quantum | NOT SUPPLIED | No T3 rescue |

Nearest definitions [232](../232-source-feedback-frontier/candidate-card.md),
[269](../269-factor-redistribution-lattice/candidate-card.md) and
[282](../282-gcd-normalized-residue-flow/candidate-card.md) use different
actions. The seed shear resembles 288, but neither its source nor its
clock theorem is imported. The [scout record](evidence/scout-record.md)
states the bounded comparison and the separate carry lane's nonadmission.

## 2. Actual branches and arithmetic refactorization

**Lemma 1.** The displayed arithmetic identity is exact. The domain
of T is clopen, and every admissible root/digit branch maps
homeomorphically onto a complete target root fibre.

*Proof.* Put X_1(t)=I+tE_12 and X_2(t)=I+tE_23. The product
X_1(a)X_2(u)X_1(c) has upper entries (1,2)=a+c,
(2,3)=u and (1,3)=au. The product
X_2(uc/d)X_1(d)X_2(ua/d) has the same three entries.
The two divisibility conditions are precisely integrality of its two
outer parameters. No global matrix-product invariant is inferred:
the actual rule changes b to b+j before each such identity.

For fixed root/digit, its seed domain is (j+dK) x K. Division by d
is well defined on dK and is a homeomorphism to K. Indeed integer
multiplication is injective on K: if nx=0, reducing modulo nm forces
x=0 modulo m for every positive m. Surjectivity onto dK and the
compact/Hausdorff property give the stated inverse continuity.
Each root domain is a union of finitely many clopen residue sets.

For target seeds (v,w) the inverse branch is

    (v,w) -> (d(w-v)+j,v).

This lands in exactly the stated residue class, so the image is the
entire target fibre, not a chosen recurrent subset. QED.

The complete predecessor list of target root (A,B,C) is also explicit.
Put U=A+C. Its possible source roots are

    a=BC/U, c=BA/U, b=U-j,
    0<=j<B, j<U,

provided a,c are positive integers. These formulas recover every
predecessor and its unique seed via Lemma 1. Hence each state has
finitely many immediate preimages. Roots with no predecessors and
all terminal states still belong to Y. For example (1,1,1,0,0) is terminal:
d=2,u=1 fails integrality, although its digit-1 branch is admissible.

## 3. Full measured groupoid and physical time

**Proposition 2.** The entire retained-lag partial-tail groupoid owns
the continuous cocycle

    c_G(z,m-k,w)=log D_m(z)-log D_k(w),

where T^m z=T^k w and D_m is the consumed-index product. Its real
extension has a complete continuous real-translation action.

*Proof.* In the inverse formula, (v,w)->(w-v,v) is an integer
unimodular automorphism of K² and preserves joint Haar. Multiplication
by d on the first coordinate maps to a subgroup of index d, with
normalized image law 1/d; translation by j preserves this law. Thus
each inverse branch phi satisfies mu(phi E)=mu(E)/d for every Borel E.
Composing gives 1/D_m, with exact continuous versions at all null points.

For a branch pair alpha,beta on the same terminal set, the actual
beta-to-alpha IMAGE derivative is J=D_beta/D_alpha. Hence -log J
is the displayed cocycle. If two descriptions have the same endpoints
and lag, increase both prefix lengths to a common pair. The identical
added terminal prefix multiplies numerator and denominator equally.
This proves presentation independence; the same cancellation proves
additivity under composable arrows.

Actual paired inverse branches on arbitrary common clopen domains
give local bisections. They cover the groupoid, including identity
arrows at terminal objects. The branch charts are locally compact and
second countable; endpoint coordinates and discrete lag separate
different arrows. Thus this is a Hausdorff étale groupoid, not a claim
that its coarse quotient is Hausdorff. The cocycle is continuous on
these charts. On all Y x R let an arrow act by
(w,t)->(z,t+c_G(g)). Translation by any real time commutes with all
arrows and is continuous and defined for both time directions. QED.

The rule consumes indices d>=2 wherever defined. We do not replace
the extension with a separately clocked mapping torus. Completeness
of real translation does not require every source state to have
an infinite forward T itinerary.

## 4. Complete periodic states, not just root patterns

Write R(a,b,c)=(bc/(a+c),a+c,ba/(a+c)) on the zero-digit
integrality domain D_0.

**Theorem 3.** Every periodic state of T has seed (0,0) and root in
D_0. Conversely every such root with seed (0,0) is periodic. Its
least period is one at (a,2a,a), and two at every other root of D_0.

*Proof.* Along every defined step the new root sum is

    uc/d+d+ua/d = u+d = a+b+c+j.

A periodic sum cannot strictly increase. Summing around a cycle gives
sum j=0; every digit is nonnegative, so every digit is zero. With
j=0, the next outer sum is b. Direct substitution gives R²=id and
shows R preserves D_0. All new outer integers are positive. Also b>=2
on D_0, since b=1 would require d|a despite 0<a<d.

The root fixed equations force b=a+c and a=c, giving (a,2a,a).
All other admissible roots form genuine two-cycles. This does not
yet classify the seeds: a root may repeat while a seed does not.

On zero-digit steps the inverse seed matrix is

    B_d=[[-d,d],[1,0]].

Over two steps the inverse matrix is P=B_d B_b, with

    tr P=db+d+b, det P=db.

Its characteristic polynomial is positive at 0, negative at 1
(value 1-d-b), and positive for sufficiently large real arguments.
Its two roots therefore lie respectively in (0,1) and (1,infinity).
No positive power has eigenvalue 1. If a full state has period m,
it also has period 2m, and its seed v obeys (P^m-I)v=0.
The determinant here is a nonzero integer. Applying the adjugate and
integer-multiplication injectivity on K forces v=0. This covers
EVERY period and ALL profinite seeds, including noninteger ones.
Conversely zero seeds have digit zero forever on D_0, and R²=id
gives the asserted least periods. QED.

An exact parametrization makes the arithmetic admissibility transparent.
Write a=g alpha,c=g gamma, with gcd(alpha,gamma)=1. Then

    s=alpha+gamma>=2, b=k s, g,k>=1,
    (a,b,c)=(g alpha,k s,g gamma).

Indeed d|ab reduces to s|alpha b, equivalent to s|b; the second
divisibility follows as well. R acts by

    (g,k,alpha,gamma) -> (k,g,gamma,alpha).

Its only fixed parameters are g=k and alpha=gamma=1. No prime
alphabet or selected factor family was used to obtain this description.

## 5. Full primitive packet and repetition ledger

**Theorem 4.** Nonzero time returns occur exactly in basins eventually
reaching the zero-seed cycles of Theorem 3. Every such cycle, modulo
cyclic phase, gives one packet, with all its finite preimages retained:

| Core | Least source period | Full time group | Least positive time |
|---|---:|---|---|
| (a,2a,a,0,0) | 1 | log(2a) Z | log(2a) |
| Nonfixed D_0 two-cycle | 2 | log(b(a+c)) Z | log(b(a+c)) |
| No eventual periodic core | none | {0} | none |

Each packet's repeated traversals have times r times its listed least
time. Distinct core cycles are distinct packets, even at coincident times.
Fixed-object isotropy of the real extension is trivial everywhere.

*Proof.* A nonzero lag equality T^m z=T^k z is exactly eventual
periodicity; the equality already supplies all subsequent defined
iterations. If the eventual least period is ell, source isotropy is
ell Z. In the cocycle a transient prefix cancels, leaving q times
the log of the index product around one least cycle. This product is
2a for a fixed root, and db for a two-cycle. Both exceed one.
Thus the clock is injective on source isotropy and the time groups
are exactly those stated, not selected subgroups.

All finite preimages of a core share its actual tail orbit. Two
different core cycles cannot share a tail, so cannot be identified by
an arrow. Real translation changes only time phase. This gives one
time-return packet per least core cycle and excludes extra transient
multiplicity. Injectivity of the clock gives trivial extension isotropy.
Non-eventual states have trivial source isotropy to begin with. QED.

The returning source locus is countable and Haar-null: periodic roots
are countable, each has its one zero seed, and for each fixed core
cycle every fixed-depth preimage level is finite by the predecessor
formula. A point has zero joint
Haar measure. These points and all nonreturning points remain in the
owner. We do not prove an embedded-circle or coarse-separation theorem.

**Corollary 5 (decisive arithmetic mismatch).** The only prime-valued
primitive exponent exp(T) is 2. Every odd-prime time log p is absent.
Nevertheless, for each odd prime p there are exactly (p-1)/2 distinct
primitive packets of time 2 log p, none a repeat of a log-p packet.

*Proof.* Fixed-core exponents 2a are prime only at a=1. Two-cycle
exponents db are composite since both factors are at least two.
In the parametrization, their product is g k s². To equal p² for
odd prime p forces s=p and g=k=1. The p-1 ordered positive pairs
alpha+gamma=p are all coprime. Swapping the unequal entries pairs
them into (p-1)/2 two-cycles. There is no fixed-core exponent p²
because it is odd. Theorem 4 excludes other packets. QED.

Already the fixed core (2,4,2,0,0) has primitive time log 4. It is
not the second traversal of the distinct (1,2,1,0,0) packet, although
both traversals take time log 4. The earliest target stop needs only
this retained counterexample; the short full classification explains
why more local tuning of this frozen rule is unwarranted.

## 6. Separate controls and the remaining naturalness boundary

FEEDBACK-OFF keeps d and the seed extraction but uses u=b in the
root rule/domain. Every main zero-seed core still exists with the
same period and clock. More precisely, its fixed root (a,2a,a),
d=2a, now has exactly d fixed seeds (j,j), 0<=j<d: seed equality
requires x=y and x=j. Each is a different fixed packet with least
time log d. In the main owner the root equations forced j=0.
Thus residue feedback genuinely removes these extra fixed packets,
but does not remove the main composite primitive. Higher-period
FEEDBACK-OFF seeds are NOT CLASSIFIED here.

UNIT-INDEX instead uses R on D_0 and the seed automorphism
(x,y)->(y,x+y), with all seeds and terminal roots retained. Its
inverse matrix is integer unimodular, so every actual branch has
joint-Haar IMAGE factor one. Its entire cocycle is zero and every
time group is {0}, even where discrete source isotropy exists.
This is a different owner and not a retiming of the main packet list.

These exact controls distinguish arithmetic admissibility, feedback,
source periodicity and clock ownership. No numerical census, prime
cutoff, fitting, parameter search or external source theorem is used.
The factorization identity does not make the rule uniquely natural,
nor does real arithmetic execution guarantee prime-only returns.

## 7. Gate decision and evidence boundary

| Obligation | Result for BRF01 | Boundary |
|---|---|---|
| T0 full owner | ESTABLISHED | Broadened groupoid, not a symplectic base |
| T1 arithmetic/index-clock ownership | ESTABLISHED in the stated scoped sense | Strong naturalness OPEN; target prime clock fails |
| T2 full primitive/repetition ledger | ESTABLISHED | Composite primitives, missing odd-prime times; coarse topology unaudited |
| T3 analytic owner | NOT SUPPLIED / NOT PURSUED | Stop at the earlier decisive gate |
| Classical A0/A1/A2 | NOT APPLICABLE | No classical suspension claimed |
| Formal Route / B | UNASSIGNED / NOT INVOKED | No transfer of prior Route or scalar-zeta credit |

Portfolio: **STOP target promotion / FORK**. The decisive reason is
the complete primitive clock ledger, already contradicted by the
separate log-4 primitive. Preserve the new arithmetic feedback and
owned-clock construction as a negative design control. Do not retime,
select prime cores, identify coincident lengths or import 291's zeta.
Future breadth needs another genuinely defined action; no repair
is started under BRF01. The 288/289/291 positives remain unchanged.

The [claim ledger](claim-ledger.md), [evidence index](evidence/README.md)
and [internal review](evidence/independent-review.md) record exact inputs,
proof method, controls and the three ARS adverse checkpoints. This is
AI-assisted internal shared-model/context work, not external peer
review or formal verification. Old packages and mirrors are unchanged;
241/242 paused; the original programme goal remains active.
