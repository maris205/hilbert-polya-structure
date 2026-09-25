# Countable auxiliary memory: finite return cycles and retained escape

Paper458; candidate `ANG-AUDIT-20260924-CFE01`.
Date2026-09-24; EXACT CONDITIONAL THEOREMS AND EXTERNAL CONTROLS.
outcome: COUNTABLE-FIBRE PACKET CRITERION ESTABLISHED; ESCAPE IS NOT ARITHMETIC ADMISSION

## Abstract

A total measured map with prescribed all-point inverse densities is lifted
to its full product with countably many auxiliary states. The counting-measure
lift owns the unchanged local clock. Its finite periodic packets correspond
exactly to finite cycles of the return endomorphism over each parent core;
all escaping and transient states remain in the full groupoid. For rational
nonzero parent multipliers, a prime-pure, prime-unique nonempty ledger requires
that every active return cycle be a single fixed vertex over a prime parent,
with global multiplicity at most one per prime. Unlike finite fibres, a
countable return graph may have no finite cycle, so some parent cores may
contribute no positive lifted packet. That freedom is a recurrence-selection
mechanism, not a derivation of an endogenous prime source. Three full real-line
controls distinguish escape, merging and countable duplication without
deleting any states. No classical symplectic or Route claim is made.

## 1. Identity, ownership and question

The authoritative definitions are the [frozen card](candidate-card.md).
The parent is a total Borel T:X->X on a standard Borel, sigma-finite measured
space, with complete disjoint injective source pieces P_i, actual inverses
I_i and specified every-point positive finite J_i satisfying every-Borel
inverse IMAGE. Let kappa_T(x)=-log J_i(Tx), x in P_i. The full lift is
Y=X times N_0 with ORIGINAL nu=mu times counting and

    F(x,e)=(Tx,sigma(x,e)).

sigma is any fixed Borel map to N_0. No integer state is removed. A state
without predecessors is not a terminal because F is total.

| Ledger item | Owner and boundary |
| --- | --- |
| Carrier and action | T on X; new F on full Y, separately named |
| Arithmetic | Conditional auxiliary-memory audit; no main source supplied |
| Measure/clock | Original counting product; actual inverse density below |
| Packets | Actual retained-lag groupoid, entire return group and all phases |
| Classical geometry/roof | NOT APPLICABLE; no positive suspension roof |
| Operator/trace/determinant | NOT AUDITED; no borrowed analytic owner |

The lineage arrow is symbolic auxiliary memory -> full measured realization.
It is not a general arithmetic-space proposal. The question is what countable
escape changes in the finite-fibre packet mechanism, without selecting a
finite subsystem. A class theorem does not supply the missing prime-symbolic
parent or establish naturalness of sigma.

## 2. Own inverse IMAGE and complete histories

For i,e,f define the source piece

    P_ief={(x,e):x in P_i, sigma(x,e)=f}.

These countably many pieces partition Y. Their target domain is
{(y,f):y in T(P_i), sigma(I_i y,e)=f}; it is Borel, and the actual inverse
is (y,f)->(I_i y,e). Every predecessor occurs on its unique source piece.
For every Borel E in this target domain, only one target and source sheet
occur, so the parent identity gives

    nu(theta_ief E)=integral_E J_i(y) dnu(y,f).

Thus the prescribed J_F=J_i is positive finite everywhere, including null
points, and kappa_F(x,e)=kappa_T(x). Different predecessors are different
inverse branches, not summands in one branch density. No partition indexed
by the uncountable space of all endomorphisms is needed.

Write Sigma_0(x)e=e and
Sigma_n(x)e=sigma(T^(n-1)x, ... sigma(x,e)...). Then
F^n(x,e)=(T^n x,Sigma_n(x)e) and S_n^F(x,e)=S_n^T(x). Consequently ALL
arrows from w=(y,f) to z=(x,e) are exactly the triples (z,k,w) for which
there exist m,n>=0 with

    k=m-n, T^m x=T^n y, Sigma_m(x)e=Sigma_n(y)f.                 (2.1)

For such an arrow c=S_m^T(x)-S_n^T(y). Two witnesses for the same triple
have the same depth difference, hence differ by adding the same number
to both depths. Their added clock sums coincide after the meeting, proving
descent. For composition, pad the two meetings to align their middle-point
depths; totality permits this, and the middle clock cancels. This proves
additivity. The forward arrow(Fz,-1,z) has clock -kappa_F(z).

Formula(2.1) is an exact full relation, not a claim that every parent arrow
lifts to every pair of fibres. All finite-depth predecessors of (y,f) are

    {(x,e):T^n x=y, Sigma_n(x)e=f},                            (2.2)

using ALL parent inverse words and all e, deduplicating actual points.
It gives every depth, including arbitrary parent incoming tails.

The lag kernel is (2.1) with m=n; the clock kernel is (2.1) with equal
parent clock sums; the joint kernel has both. These formulas retain
nonunit merging arrows. They also specify all relations on escaping and
non-eventual classes, without a finite graph approximation.

## 3. Entire isotropy, phases and finite-cycle classification

For any total deterministic map U with the retained-lag groupoid, nonzero
source isotropy at z is equivalent to eventual periodicity: U^m z=U^n z,
m>n gives a periodic tail, and the converse is immediate. If its eventual
least core period is p, every isotropy lag is in pZ and all those lags occur.
Writing C_U for the signed clock around that core gives

    Iso_G(z)=pZ, c(ap)=a C_U, H_z=C_U Z.                     (3.1)

Otherwise Iso_G(z)={0} and H_z={0}. Clock zero does not delete source
isotropy: extension isotropy is pZ if C_U=0, and trivial if C_U!=0.
For C_U!=0 the least positive height-translation return is abs(C_U),
with all positive integer multiples. All incoming points have the same H.

For completeness, fix one basepoint z0 in ANY source class and one actual
arrow z0->z for each z; let its clock be B(z). This is a setwise description,
not a measurable selector claim. Any other choice changes B(z) by H.
The complete extension-orbit criterion is

    z,w same source class,  h_z-B(z)=h_w-B(w) modulo H.       (3.2)

Indeed the clocks of all arrows w->z form B(z)-B(w)+H. Thus when H=0
all real phases remain distinct; when H=CZ phases are R/(CZ). Height
translation has stabilizer exactly H, not the source-period group pZ.

Now let x_j=T^j x0, j mod q, be one parent least-q core, and C its signed
cycle sum. Define Pi=Sigma_q(x0):N_0->N_0. Every finite Pi-cycle of length
l gives exactly one F-core of least period ql: following q steps returns to
the reference parent phase and applies Pi, and no smaller base phase return
is possible. Conversely every F-core projects to a parent core and intersects
its reference fibre in a finite Pi-cycle. Distinct Pi-cycles give distinct
F-cores, not extra starting-point multiplicity. The whole return data are

    p_F=ql, C_F=l C, H=l C Z, primitive=l abs(C) if C!=0.     (3.3)

Coverage includes all incoming states. If x first reaches parent phase j
at depth n, continue a=(q-j) mod q parent steps to x0. The fibre state
e'=Sigma_(n+a)(x)e belongs to one Pi functional graph. If its forward Pi
orbit eventually enters a finite cycle, (x,e) lies in precisely that full
F-basin. If not, it has no eventual F-core and no nonzero source isotropy.
All such states remain, with their exact merging relation (2.1). A parent
that is not eventually periodic cannot support an eventual F-core.
This covers cyclic, transient and escaping cases; in a countable graph
the last case cannot be excluded by a finite pigeonhole argument.

Changing the parent reference phase preserves cycle/packet data, not
necessarily entire transient graphs. If A transports from phase0 to phasej
and B completes the parent cycle, Pi_0=BA and Pi_j=AB. A intertwines them.
On the union of finite-cycle vertices Pi_0 is a bijection. If Ae=Ae',
then Pi_0 e=Pi_0 e', hence e=e' there. Every periodic vertex at phasej is
in the image of A: take its preceding Pi_j iterate and apply B. Therefore
A bijects periodic vertices, conjugates the two return permutations there,
and preserves their cycle lengths. No injectivity on transients is asserted.

## 4. Exact rational-parent benchmark

Count every parent core separately. For C!=0 write a=exp(abs C)>1 and
let b_gamma(l) be the number, possibly infinite, of its Pi-cycles of length l.
The full positive primitive multiset is exactly

    { l log a_gamma : each parent gamma with C!=0,
                       each finite Pi_gamma cycle of length l }.       (4.1)

Zero-clock parent cores contribute no positive primitive, whatever their
return graphs. They still contribute source and ineffective isotropy.

Assume each a_gamma is rational. Write a=u/v>1 in lowest positive terms.
If a^l is an ordinary prime p, then v^l divides u^l, so v=1; u^l=p then
forces l=1 and u=p. Conversely a=p,l=1 works. Thus nonempty prime purity
and uniqueness hold if and only if ALL of the following hold:

- A nonprime rational parent multiplier has NO finite return-graph cycle.
- A prime parent multiplier has no return cycle of length greater than1.
- For each prime p, the TOTAL number of fixed vertices over ALL parent cores
  with multiplier p is at most1, and at least one prime has total1.

These conditions allow any number of escaping components and arbitrary
incoming merging to the permitted fixed vertex. An otherwise prime parent
may also have no finite cycle. For all-prime coverage, the total must equal1
for EVERY ordinary prime, a separate requirement. Conditions are sufficient
by(4.1) and necessary by the reduced-fraction argument, with no cancellation
between distinct packets. Irrational a is governed by(4.1), not this lemma.

This differs from a finite auxiliary set: a countable self-map can have no
finite cycles, so parent cores need not survive as positive lifted packets.
The conclusion does NOT say any choice of sigma is endogenous arithmetic.
Choosing escape versus recurrence after consulting a prime predicate would
encode a selector, not solve the source-origin obligation. No such selection
is made here; this is a conditional necessary/sufficient ledger criterion.

## 5. Complete external controls

Each control has its own full R times N_0, Lebesgue times counting,
F(x,e)=(2x,s(e)); the common parent T(x)=2x is also checked independently.
The parent inverse x->x/2 has J=1/2 on every point and Borel set. Each
actual lifted inverse is (y,f)->(y/2,e) for s(e)=f, with the SAME per-branch
geometric J=1/2 by one-sheet substitution. Thus all clocks are log2.
The step sums are n log2 and any actual lag-k arrow has c=k log2.

The parent classes are {0}, with source isotropy Z and H=(log2)Z, and
{a*2^j:j in Z} for nonzero a, with trivial source isotropy and H=0.
Its lag/clock/joint kernels are all units. Each point has its single
depth-n predecessor x/2^n. The parent extension phases are h mod log2
at0, and h+j log2 on a chosen nonzero class. These are setwise coordinates;
there is no preferred selector a and no arithmetic-source claim.

### A. Unilateral escape, s(e)=e+1

All arrows from (y,f) to (x,e) satisfy exactly

    k=f-e, y=2^k x.                                        (5.1)

Necessity follows from e+m=f+n. For sufficiency choose m,n>=0 with the
displayed difference. Classes are, for each real a,
{(a*2^e,e):e>=0}; a=x*2^(-e) is the invariant. ALL such classes, including
a=0, have no eventual core, trivial source/extension isotropy and H=0.
All three kernels are units. The full extension phase is h+e log2.
Depth-n incoming is the singleton(x/2^n,e-n) when e>=n, otherwise empty.
This is an empty positive ledger with all escaping states retained, not
deletion of the original zero fibre.

### B. Merging countdown, s(e)=max(e-1,0)

For any k choose m,n with m-n=k and then add enough common padding to make
m>=e,n>=f. Both fibres become0. Therefore the full arrow criterion is

    y=2^k x, with arbitrary e,f>=0.                         (5.2)

The origin class contains every(0,e). Its sole core is(0,0), least period1,
source isotropy Z at every incoming point, H=(log2)Z and trivial extension
isotropy. It gives ONE positive packet with primitive log2 and every repeat;
phases are h mod log2 on all origin sheets. Nonzero classes are
{(a*2^j,e):j in Z,e>=0}; their source/extension isotropy is trivial, H=0,
and phases are h+j log2. All three kernels are the actual zero-lag mergers
((x,e),0,(x,f)); these need not be units. A target(x,0) has exactly n+1
depth-n predecessors (x/2^n,e),0<=e<=n; a target(x,f),f>0, has just
(x/2^n,f+n). The infinite eventual origin basin is not a 2^n word count.

### C. Static countable sheets, s(e)=e

The full arrow criterion is e=f and y=2^k x. For each sheet the origin is
a separate fixed core with H=(log2)Z, source isotropy Z and trivial extension
isotropy. There are countably many DISTINCT positive packets of primitive
log2. Every nonzero class is { (a*2^j,e):j in Z } with trivial isotropy,
H=0 and phase h+j log2. Origin phases are h mod log2 on that sheet.
All three kernels are units; depth-n incoming is(x/2^n,e). Equal lengths
do not merge sheets. This fails prime uniqueness, despite prime purity.

These controls establish empty, single and countably duplicated positive
ledgers respectively. They are EXTERNAL: the coefficient2 is a design input,
not a discovered prime mechanism, and B does not supply all-prime coverage.

## 6. Evidence, limits and disposition

All results above are exact deductions from the card. No scientific code,
finite orbit sample, precision cutoff, web retrieval or new external theorem
is used. The unrestricted formulas(2.1)–(2.2) and (3.2) retain every actual
state/ancestor/phase, but assert no effective census or measurable quotient.
No global finiteness of inverse fibres or periodic packets is assumed.
The reference comparison is the finite class in
[454's frozen definition](../454-finite-endomorphism-lift/candidate-card.md),
not imported proof or Route credit. Local proof sections2–5 support every
claim in the [ledger](claim-ledger.md).

Portfolio FORK / retain conditional filter. T0 and packet/clock ownership
are established within this class; arithmetic T1 NOT PASSED, T3 NOT AUDITED.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
Same-object ledger remains intact, including every escaping sheet. A future
source must explain its own arithmetic recurrence without prime-directed
choice of sigma; this paper does not authorize that next candidate.

AI disclosure: root produced this proof/draft with AI assistance; a separate
same-model, shared-history internal reviewer was assigned card-only derivation
before manuscript comparison. This is NOT_CALIBRATED, not human peer review,
cross-model validation or independently distributed errors. Root completed
this paper, [README](README.md) and ledger before first raw access. Informal
design feasibility is disclosed on the card and batch log, not sold as blind
preregistration. No helper assisted root's458 proof. Final review status and
actual access receipts belong to the later evidence, not this statement.

Evidence: [CP1](evidence/scope-review.md),
[raw derivation](evidence/independent-derivation.md),
[final comparison](evidence/review.md),
[batch log](../455-divisor-continued-quotient/batch-log.md).
