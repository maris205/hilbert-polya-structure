# Independent internal review — subtract-and-factor word flow

Candidate ID: ANG-20260920-SFW01.
Paper ID: 298-subtract-factor-word-flow. Date: 2026-09-20.
Status: OWNED WORD IMAGE CLOCK; COMPOSITE FIXED-CORE TIMES — STOP / FORK.

## 1. Bindings, scope and actual order

The entire 156-line raw card was read and hash-verified before any
298 manuscript access. Original frozen SHA-256:

    10b23181087e28469c7490e4dc3ae5cc018eb274ed4684a7482d3d0add762ecd

This binds the initial card, excluding a later administrative appendix.
Complete raw source, measure, IMAGE, fixed-family and control findings
were sent before opening the manuscript. The subsequent full paper read
covered 314 lines, with verified SHA-256:

    f8a154d7743ae951d8254b08bf2921308df629aae19e79e05785d98e79cc0220

ARS's three checkpoints were raw-card analysis, manuscript comparison
and final adverse review. The native auxiliary atomic_clock_scope
independently checked only FACTORIZATION-OFF and MEASURE-CHANGE from
the raw card, including the fixed-core equation needed for the latter.
It received no reviewer conclusions or manuscript. Its control formulas
were checked against the reviewer's own derivations before manuscript
access. Main-source and measured-owner proofs and the original fixed
family were independently derived by this reviewer.

This is inherited same-model/shared-context internal AI-assisted review,
not external peer review, formal verification or independent-error
evidence. Older definition/provenance records were not independently
reread or used as theorem inputs. No auxiliary writes, external lookup,
scientific computation or other-file edits occurred. Only this report
was written; no eventual or higher-period census was undertaken.

## 2. Checkpoint 1 — full source, map and measure

Divisibility atoms are precisely primes. Descending integer division
constructs the factor word, retaining every multiplicity; the elementary
prime-divisor lemma gives uniqueness and sorting fixes the order.
The equality convention always gives q>=2, and unequal inputs give
q>=1. Empty factor output leaves an infinite tail, hence still an
element of X, without introducing symbol 1.

Every finite cylinder is clopen and projects onto the infinite discrete
alphabet at an unused coordinate. It is therefore noncompact. A compact
neighbourhood would contain such a cylinder closed inside it, impossible.
Thus X is nowhere locally compact; no finite-alphabet substitute is used.

The restriction C(a,b)->C(w), w=fct(q(a,b)), is the exact prefix
homeomorphism in the card, including C(empty)=X. The (2,3) chart
has empty output and is onto all X, proving the full map onto.
All equal-input and composite-symbol branches remain.

The telescoping sum of nu(n)=1/(n-1)-1/n equals one, so the
countable product probability exists with the stated cylinder weights.
Every nonempty open set contains a positive-weight cylinder. Since each
symbol has mass at most 1/2, a singleton has mass at most 2^(-N)
for every prefix length N, and hence zero. This product is nonatomic:
a positive atom, successively partitioned by the countable coordinate
cylinders, would select nested prefixes of that same positive mass,
contradicting the singleton result. Full support and nonatomicity coexist.

## 3. Checkpoint 1 — full-point IMAGE clock and time

For every Borel tail set, adjoining a prefix multiplies its product
measure by that prefix's weight. Applying this separately to (a,b)
and w proves on the ENTIRE inverse-branch domain

    mu(h_(a,b)(E))=R(a,b)*mu(E),
    R(a,b)=nu(a)*nu(b)/product_(d in w)nu(d).

This is the inverse IMAGE factor; the forward factor is reciprocal.
The boundary checks give R(2,3)=1/12 and R(2,2)=1/2.
No branch value alone is thereby a periodic-orbit length.

Writing L=-log R and L_m=sum_(i<m)L(T^i x), an actual branch
pair from y to x has

    J(x,m-k,y)=exp(-L_m(x)+L_k(y)),
    c(x,m-k,y)=L_m(x)-L_k(y).

Common extension of equal-lag presentations cancels the same terminal
factors, and middle-count alignment proves additivity. Local inverse
charts and finite-cylinder refinements give a locally constant full-point
cocycle on the retained-lag topological groupoid. No additional swaps,
free prefix replacements or germ identification enter this argument.

Any two continuous IMAGE versions on a chart must agree: a difference
at a point persists on a nonempty open source set of positive measure,
contradicting the Borel measure identities. Thus singleton-null returning
words inherit the same continuous version; it is not reset at those words.

The derived map T_tilde(x,u)=(Tx,u-L(x)) has iterate
(T^m x,u-L_m(x)). Its retained-lag tail equality gives exactly
the displayed extension, including the sign. Extension bisections make
the orbit projection open; commuting translations descend jointly
continuously for every real time. No separate roof or clock is added.

For K(d)=product p(p-1) over the full factor word, K(d)<=d(d-1)
when d>=2, and K(1)=1. Since q<=B=max(a,b), this gives
R<=1/[A(A-1)]<=1/2 with A=min(a,b), including q=1.
Therefore L>=log 2. This is a derived branch bound, not classical
symplectic, locally compact analytic or embedded-circle structure.

## 4. Checkpoint 1 — complete fixed-member discriminator

The fixed equation is w*b^infinity=a*b^infinity. Empty w would
force a=b and contradict q=1. A nonempty w must begin with a,
so a=p is prime. If w had at least two letters, its second
would be b and q=product(w)>=ab>max(a,b), impossible.
Thus w=(p), q=p, and precisely b=p or b=2p are allowed.

At each listed fixed core, R(p,b)=nu(b). Every lag in Z occurs,
and ALL its presentations give c=lag*log[b(b-1)]. Hence the
entire stabilizer is log[b(b-1)]Z with least positive time
log[b(b-1)] and trivial fixed-object extension isotropy.
This yields the two prime-indexed families of primitive times

    log[p(p-1)] and log[2p(2p-1)].

Different fixed words cannot have common forward tails, even after
excursions through finite preimages. They remain different packets
under actual arrows and real-time translation. The constant-3 core
has primitive log 6; (2,4,4,...) has primitive log 12.
These decisive composite primitives stop the target without classifying
nonfixed members, eventual returns, other fixed words or higher periods.

## 5. Checkpoint 2 — manuscript comparison and controls

The manuscript's full proof agrees with the raw conclusions, including
all factor multiplicities, the inverse IMAGE sign, uniqueness on null
words, the derived T_tilde and the uniform positive branch bound.
It expressly avoids a global absence claim for any specific prime time.

FACTORIZATION-OFF rebuilds its own ratio as nu(a)nu(b)/nu(q) for
q>=2 and nu(a)nu(b) for q=1. Its fixed family is exactly
(a,a,a,...) and (a,2a,2a,...) for EVERY a>=2. Each has
H=log[b(b-1)]Z. Distinct fixed cores stay distinct; constant 4
and (2,4,4,...) are two different least-log-12 primitives.

MEASURE-CHANGE has sum nu_0(n)=1, positive cylinder weights and
zero singleton masses. Its own inverse ratio, for a length-k word w, is
R_0=2^(2-a-b-k+sum_(d in w)d). The main fixed cores do not
change, but their least times become (b-1)log 2. Integer-related
times do not merge packets: constant 3 is not constant 2 traversed twice.

The extra composite chart check is also correct: at (4,4), main
output (2,2) gives R=1/36, while the control's output (4) gives
R=1/12. Neither is asserted to be a main return of constant 4.
No manuscript correction was requested, and neither control is
promoted to a complete returning-locus classification.

## 6. Checkpoint 3 — strongest counterarguments and verdict

Singleton nullness cannot remove the counterexamples: all words belong
to the frozen source, and their clock is fixed by the full-support
continuous IMAGE version. Equal lengths or arithmetic decompositions
cannot merge different fixed cores or redefine their least returns.
The positive constant-2 control does not override the other fixed cores.

Unlike a merely assigned scale, the main clock really follows from
this measure's branch law. Nevertheless the all-integer measure,
equal-input convention and factor ordering are design choices. The
measure-change control demonstrates dependence on that choice, not
a failure of ownership or a universal obstruction to word dynamics.

**Verdict: no outstanding blocking issue or requested correction.**
The measured owner is established and the target fails at the frozen
fixed-family gate: STOP / FORK. Remaining returns and coarse topology
stay OPEN / NOT PURSUED; strong naturalness is not established.
T3/quantum owners are not supplied, classical route fields are not
applicable, formal coordinates are unassigned and Route B is not
invoked. Earlier packages and paused 241/242 remain unchanged.
