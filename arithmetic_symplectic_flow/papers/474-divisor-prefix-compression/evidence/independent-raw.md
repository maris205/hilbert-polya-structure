# DPC01 — isolated card-only raw derivation

Candidate ID: ANG-20260925-DPC01. Batch SYMBOLIC-RETURN-20260925-Y.
Reviewer: dpc01_independent_review; stage: DISTINCT RAW RELEASE, before any
current author-paper unlock. Scientific verdict: OWNED PREFIX CLOCK;
NONPRIME FIXED PACKET — STOP / FORK.

## 1. Inputs, isolation and exact method

The sole new scientific input is [candidate-card.md](../candidate-card.md),
the original 98-line scientific freeze, SHA-256
`595b1751966b2edd700669757ec791437664f80636752dbe08ca1b26f6977e87`.
The same hash and line count were rechecked after RAW RELEASE. CP1 is the
separate [scope review](scope-review.md), 77 lines, SHA-256
`37a452a50ba320e907f4201efa5c110eb2f2bbf8e86b79cd38fc41353a5e005e`.
No current author paper, author helper, peer raw derivation or old proof file
has been opened. The inherited root design/history exposure remains real:
this is separately executed shared-model AI, NOT_CALIBRATED, not blind,
human, external or error-independent. Outcome-unsealed scouting is not
retroactively relabelled preregistration.

ARS router/workflow/runtime/DA/fallacy instructions were read for CP1; the
83-line anti-leakage reference was additionally read at this stage. That
writing protocol is not activated as a full bibliography-based pipeline;
the stricter caller-imposed current-card-only scientific boundary applies.
The method below is exact word cancellation, product-measure identities,
and all-depth deterministic-history arguments. No scientific numerics,
cutoff, external literature, network, Git, PDF or operator construction is
used. Only this raw file is writable by the reviewer at this stage.

## 2. Full actual maps and complete inverse lists

Write l = log 2 and D(d,n) = [1 < d < n and d divides n]. All four owners
have domain E consisting of sequences with at least two zeros. Its disjoint
source cylinders are U_dn = c(d)c(n), d,n >= 1; all other points remain
terminal objects. Let g(d,n)=n/d on D and d+n otherwise. A map on a source
cylinder is exactly U_dn xi -> V_dn xi, with V from the frozen table.
In particular, an outgoing step is never added at a terminal point.

For any finite binary word V, the map xi -> V xi is a homeomorphism from X
onto the clopen cylinder [V]. Thus I_dn(V_dn xi)=U_dn xi is a Borel inverse
onto the whole source cylinder and is defined on the WHOLE target cylinder.
Conversely every actual predecessor has one unique first input pair d,n,
so one of these inverse branches produces it. There is no extra predecessor
label once the actual point is specified.

Here are complete, untruncated inverse lists. If y has no zero, every list
is empty. If y=c(k)eta, the one-delimiter owners have

    Pred_M(y) = {c(d)c(kd)eta : k >= 2, d >= 2}
                union {c(d)c(n)eta : d+n=k and not D(d,n)};
    Pred_A(y) = {c(d)c(n)eta : d+n=k};
    Pred_Q(y) = {c(d)c(k)eta : 1<d<k and d divides k}
                union {c(d)c(n)eta : d+n=k and not D(d,n)}.

The first set for M is empty if k=1. The sets are sets of actual states,
not sums of labelled copies. These formulas also apply when eta is the
all-ones tail, so a one-zero terminal may have actual incoming arrows.

For L, a target with fewer than two zeros has no predecessors. For
y=c(k)c(n)xi the complete list is

    {c(d)c(n)xi : d=n/k is an integer and D(d,n)}
        union {c(k-n)c(n)xi : k>n and not D(k-n,n)}.

The first alternative automatically has 1<k<n; the second has k>n.
They cannot coexist, and each contains at most one point. Thus L is
globally injective on E. This does not discard overlapping inverse branches
of the other owners: in particular M can have countably many predecessors.

Every list is countable, each of its branches has a Borel cylinder domain,
and the union exhausts the actual source. The formulas preserve targets
that lack outgoing steps. For M/A/Q a finite number of zeros decreases by
one per legal step, while L preserves it. No terminal is made absorbing.

## 3. Every-Borel original IMAGE and the pointwise clock

Let U,V be one frozen source/target word pair. For every Borel E0 subset
of [V], there is a Borel tail set B with E0={V xi:xi in B}. Product measure
gives mu(E0)=2^(-|V|)mu(B), and mu(I E0)=2^(-|U|)mu(B). Therefore

    mu(I E0) = integral_E0 2^(|V|-|U|) dmu.

This proves the IMAGE identity on every Borel set, not just cylinder totals.
The card prescribes this same constant at every point of [V], including
null tails. A Radon–Nikodym identity alone would not determine those null
values; here they are the explicitly frozen branch version. The inverse
and forward identities hold pointwise on the whole cylinders.

Consequently kappa=(|U|-|V|)l, with the following exact values:

| Owner | On D(d,n) | Off D(d,n) |
| --- | --- | --- |
| M | (d+n-n/d)l | 0 |
| A | 0 | 0 |
| Q | d l | 0 |
| L | (d-n/d)l | -n l |

M and Q have nonnegative clocks; L has signed and zero values, all retained.
No positivity modification, roof insertion, measure change, or selection
of returning points enters this calculation. Each table entry is derived
from that owner's own actual rewrite and the same original fair-bit law.

## 4. Full history, cocycle and pair IMAGE

Fix one owner. Let D_r and S_r be as in the card and write A_r=S_r/l,
an integer-valued function on D_r. Countable prefix-replacement charts
cover every legal finite iterate: intersect a current target cylinder with
the next source cylinder; prefix compatibility either gives the empty set
or another cylinder, after adding a common tail prefix when necessary.
Induction gives this cover at every finite depth, not a chosen cutoff.

The full groupoid consists of exactly

    (x,r-s,y), with r,s >= 0, x in D_r, y in D_s,
    and T^r x = T^s y.

Identical triples are identified; their integer lag is not forgotten. If
two presentations have the same lag, the larger exponents are obtained
from the smaller ones by the same nonnegative increment. Their common
future contributions cancel in S_r(x)-S_s(y). Hence

    c(x,r-s,y)=S_r(x)-S_s(y)

is well defined, including at null points. To compose two arrows, extend
the two middle-point histories to the larger of their middle exponents;
the required extensions exist along that actual middle history. The sums
then telescope, proving c(gh)=c(g)+c(h) and c(g^-1)=-c(g). No extension
beyond a terminal is used. The actual forward arrow (Tx,-1,x) has
c=-kappa(x), exactly the sign specified on the card.

On a history-pair chart y -> x defined by (T^r)^-1 T^s, the forward s
steps have IMAGE factor exp(S_s(y)), and the inverse r steps have factor
exp(-S_r(x)). The original-measure IMAGE of this chart is therefore
exp(-c). The every-Borel one-step identities prove this by composition
and restriction, on a countable chart cover. They are not identities for
an invented invariant measure or a sum that double-counts overlapping
actual arrows. Same-triple descent also binds the chosen pointwise version.

## 5. Exact full kernels, incoming histories, isotropy and phases

For EVERY owner the following formulas characterize all kernel arrows:

    K_lag = {(x,0,y): exists legal r, T^r x=T^r y};
    K_clock = {(x,r-s,y): T^r x=T^s y,
                                  A_r(x)=A_s(y)};
    K_joint = {(x,0,y): exists legal r, T^r x=T^r y,
                                            A_r(x)=A_r(y)}.

The variables range over all legal nonnegative depths. These are exact
tests, not a claim that any finite search decides every input. A has c=0
on all arrows, so K_clock=G and K_joint=K_lag. For L there is a further
global simplification. On E put p(x)=the first run length. Since the tail
starting at the second codeword is unchanged, kappa=(p(x)-p(Tx))l and

    c(x,k,y)=(p(x)-p(y))l

on every nonterminal L arrow. Terminals have only unit arrows for L.
Injectivity gives K_lag=units. Coalescing L states have the same suffix
starting at their second codeword; if their first run lengths also agree
then the states are equal. Thus K_clock is exactly the entire isotropy
bundle of L, K_joint=units, and every L isotropy clock is zero. This is a
telescoping ownership fact, not a search for additional cycles.

For any owner and ANY z in X define P_0(z)={z} and

    P_(j+1)(z) = union_(w in P_j(z)) Pred(w).

The complete lists in Section 2 imply by induction that P_j(z) is exactly
the set of legal j-step predecessors. Thus union_(j>=0) P_j(z) retains
every finite incoming depth. Compatible infinite incoming histories are
exactly sequences (z_0,z_-1,z_-2,...) with z_0=z and
z_-(j+1) in Pred(z_-j) for every j. This inverse-limit condition keeps
compatibility; it does not infer an infinite path merely from unrelated
points at different depths. Empty path spaces remain empty. These rules
apply also to terminal z and use no finite depth bound.

The exact source-orbit test is the common-iterate predicate above. The
exact extended-orbit test for (x,h_x),(y,h_y) is that some such r,s also
satisfy h_x-h_y=S_r(x)-S_s(y). All incoming points, forward points and
their legal coalescences remain in this test; no section is selected.

For completeness, the source isotropy at x is nonzero precisely when
x eventually reaches a genuine periodic core. Indeed r>s with
T^r x=T^s x supplies a periodic point, and an eventual cycle supplies
all integer multiples of its least period. If the core has least source
period e and total cycle clock C, the ENTIRE source isotropy is eZ,
its clock image is H=CZ, and the extended isotropy is

    eZ if C=0, and {0} if C is nonzero.

Transients cancel in every isotropy clock. If no periodic core is reached,
source and extended isotropy and H are all trivial. These statements
follow from the deterministic map and its legal histories; they do not
classify extra periods outside the frozen gate.

Choose one base b in a source orbit and an actual arrow b -> x of clock
t_x for each x. The set of all arrow clocks y -> x is exactly
t_x-t_y+H: compose with isotropy at b, and conversely subtract two such
arrows. Hence the full extended orbit set above that source orbit is
parametrized by h-t_x modulo H. Physical height translation adds its
parameter to this phase. Its stabilizer is the ENTIRE H, not the subgroup
generated by one arbitrarily selected arrow. Nonzero H=CZ has primitive
|C| and every integer repetition; H=0 has no positive period even when
zero-clock source/extended isotropy remains. No nice quotient is assumed.

## 6. ALL fixed sequences in the nine complete cylinders

The frozen W has d,n in {2,3,4}, with arbitrary infinite tails. For a
one-delimiter output c(k)xi, equality

    c(d)c(n)xi = c(k)xi

first forces k=d by the position of the first zero. Cancelling c(d)
then forces c(n)xi=xi, whose unique solution is xi=c(n)c(n)c(n)...:
iterate the equality to determine every finite prefix. Thus no finite
set of sample tails stands in for the full-cylinder calculation.

For M, off-D gives k=d+n>d. On D the first-zero requirement is n/d=d.
Within the nine frozen pairs, the only D pair is (2,4), and it satisfies
that equality. Therefore the ENTIRE fixed set of M in W is

    {b}, where b=c(2)c(4)c(4)c(4)... .

For A, k=d+n>d on every branch, so there are no fixed points in W.
For Q, off-D is the same obstruction; on D, k=n>d. Q has no fixed
points in W either. For L, compare

    c(d)c(n)xi = c(g(d,n))c(n)xi.

Equality holds exactly when g(d,n)=d, and then imposes NO condition on
xi. Thus its ENTIRE fixed set in W is the full cylinder

    Z=[c(2)c(4)].

This includes every arbitrary infinite tail, including eventually all-ones
tails. A subset of Z or one preferred representative would be incorrect.

## 7. Full-X packets of every gate core

### 7.1 MAIN: one fixed core, its entire incoming basin, and primitive log 16

At b the actual input pair is (2,4), D is true, the output first word is
c(2), and kappa(b)=(2+4-2)l=4l=log 16. Let

    B = union_(j>=0) P_j(b)

using the MAIN predecessor list. This is exactly the full source orbit
of b: coalescence with b is equivalent to some legal iterate reaching b.
Every level is countable, so B is countable, but no level is discarded.
For example the COMPLETE first level is

    P_1(b) = {c(1)c(1)c(4)^infinity}
             union {c(d)c(2d)c(4)^infinity : d>=2}.

The core itself is the d=2 member. The all-depth recursion, not this
example level, is the full incoming specification. Compatible infinite
histories are precisely the inverse-limit paths defined above; the
constant history at b is one such path, not the only allowed history.

For z in B let m(z) be its least entry time to b and E(z)=S_m(z)(z).
Every arrow z <- w has some integer lag k, and the COMPLETE possibilities
are all k in Z with

    c(z,k,w)=E(z)-E(w)+(k-m(z)+m(w))4l.

To prove completeness, extend both entries by independently chosen
nonnegative numbers of fixed-point steps; their difference realizes every
integer. Conversely any coalescence can be extended to b, which yields
this formula without changing the arrow. In particular, source isotropy
at every z in B is Z, its ENTIRE clock image is 4l Z, and extended
isotropy is trivial. Incoming histories cannot reduce this subgroup.

For clarity, all three kernels on this entire basin are explicit too:
K_lag has k=0; K_clock has
k=m(z)-m(w)-(E(z)-E(w))/(4l), when that number is an integer; their
intersection has k=0 and E(z)-E(w)=4l(m(z)-m(w)). Globally the exact
kernel tests in Section 5 still apply to every other source orbit.

The exact extended-orbit test on B is

    h_z-E(z) = h_w-E(w) modulo 4l Z.

Thus the full basin gives ONE physical translation packet, with every
phase in R/(4l Z), primitive 4l=log 16, and repetitions r log 16 for
all positive integers r. The primitive is not log 2: log 2 is absent
from the entire stabilizer. Interpreting this return as a fourth repeat
of an unowned smaller orbit would change the candidate.

### 7.2 L: the entire full-cylinder family and zero-clock isotropy

Every z in Z is fixed and has kappa(z)=0. Since L is globally injective
and z is its own predecessor, Pred_L(z)={z}; hence P_j(z)={z} for every
j. Its entire full-X source orbit is the singleton {z}, and its only
compatible infinite incoming history is the constant one. Distinct tails
in Z give distinct source orbits; none are identified by a hidden basin.

Each z has entire source isotropy Z and H={0}. Its extended isotropy
is still Z. The extended orbit set above z has all real heights as
distinct phases, physical translation is free, and there is NO positive
primitive. The whole cylinder, an uncountable family of distinct free
translation packets with zero-clock isotropy, is retained. It is not an
uncountable family of positive-period packets or a chosen singleton.

### 7.3 A and Q

There are no fixed cores in W, so there are no W-fixed-core packets to
complete for A or Q. Their global inverse/history/kernel rules in
Sections 2–5 still retain every state, terminal and incoming history.
No claim that they lack other-period returns follows from this short gate.

## 8. Decisive gate, controls, scope and handoff

MAIN has a genuinely active proper-divisor return at its gate core:
D(2,4) holds and quotient writeback is used. At that same actual state,
A writes c(6)c(4)^infinity and Q writes c(4)^infinity, neither equal to b.
Thus neither A nor Q reproduces this fixed return. L fixes b and all of
Z, but with its own zero clock and singleton source packets; its enlarged
family cannot supply or erase MAIN's positive return.

The owned MAIN primitive is log 16, and 16 is not an ordinary prime.
Therefore the frozen necessary prime-purity condition is refuted by an
actual whole-basined packet. This is a STOP / FORK, notwithstanding the
positive ownership result and the arithmetic activity of that return.
No duplicate-prime or all-prime-coverage argument is needed for this stop.

The fair-bit law visibly constrains all branch clocks to integer multiples
of log 2; this explains a PROVES_TOO_MUCH / naturalness concern rather than
establishing a prime mechanism. No arbitrary data-fitting theorem or
global periodic ledger is asserted. The inverse recursion has no cutoff;
the fixed-point classification is limited exactly to W. No additional
cylinders, measure changes or period searches were performed.

T0 and the original-measure clock/history ownership have explicit proofs.
The T2 gate packet and repetition claims above are scoped exact results;
global positive-orbit enumeration remains unaudited. Arithmetic T1 is
NOT PASSED: an internally active divisor rule is not the required prime
ledger. T3 is NOT AUDITED, classical fields are NOT APPLICABLE, formal
Route coordinates remain UNASSIGNED, and Route B is NOT INVOKED. The
same-object ledger stayed intact separately for all four owners.

Portfolio: STOP / FORK, because the entire MAIN stabilizer gives a
nonprime primitive. Preserve this raw record unchanged; do not retune
the map, clock, cylinders or prime convention. This reviewer now HOLDs
for DISTINCT PAPER UNLOCK before reading or judging final author surfaces.
