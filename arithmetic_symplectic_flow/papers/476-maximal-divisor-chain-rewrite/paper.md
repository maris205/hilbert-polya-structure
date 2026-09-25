# Maximal divisor-chain rewriting has an owned quadratic return

Paper476-maximal-divisor-chain-rewrite. Candidate **ANG-20260925-MCR01**.
Date2026-09-25; batch PRE-P0-STRUCTURE-20260925-Z, round2/5.
Outcome: **OWNED CONTINUED-FRACTION IMAGE; ACTIVE-DIVISOR QUADRATIC RETURN — STOP / FORK**.
Status: exact negative result for this frozen candidate's necessary prime target.
Classical A0–A2 NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

A partial prefix map reads the maximal initial proper-divisor chain of a
full infinite positive-integer word and rewrites that chain as adjacent
quotients. Its original measure is the pullback of the specified
continued-fraction density, and its clock is the negative logarithm of its
own inverse IMAGE derivative. This paper constructs the coordinate and
measure, proves all-point inverse and history identities, and keeps every
terminal, predecessor and phase. In two precommitted complete cylinders,
MAIN and the run-feedback-OFF control each have exactly one fixed sequence;
the other two controls have none. At that arithmetic-active fixed sequence,
the entire height stabilizer is `2 log(2+sqrt(5)) Z`. Its least positive
generator is not log an ordinary prime. MAIN therefore stops, despite
replacing the former dyadic clock mechanism by a different measured owner.
No conclusion about the rank of the complete periodic clock group is drawn.

## 1. Identity, lineage and bounded question

The sole frozen scientific input is the [original candidate card](candidate-card.md),
105 lines, SHA256
`7bc0a9f67479b8a5b1f51f2fa752d96d8269a176d0697238733f1ff8f7076a77`.
The [ledger](claim-ledger.md) and [overview](README.md) report this same object.

| Field | Frozen owner |
| --- | --- |
| Carrier | Entire `X=N_{>=1}^{N0}`, with the product Borel structure |
| Original measure | Pullback of `dx/((log2)(1+x))` on irrational `(0,1)` |
| Four actual maps | M maximal-chain rewrite and A/Q/R OFF maps in Section3 |
| Arithmetic lineage | Adjacent divisor symbols → maximal admissible chain → multi-digit quotient writeback → next actual input |
| Clock | Own full-point inverse IMAGE, then the actual-history cocycle |
| Physical action | Height translation on the full extension's orbit SET |
| Primitive convention | Least positive generator of the ENTIRE physical stabilizer |
| Classical symplectic/contact/quantum construction | NOT APPLICABLE / NOT SUPPLIED |
| Operator, trace, determinant | NOT SUPPLIED; T3 NOT AUDITED |

There is no fixed external integer, prime acceptor, prime table, fitted
log-prime roof or independent time schedule. The original infinite-word
carrier has no finite-word objects or infinite letter; these are not states
deleted after testing. Every existing infinite word, including units,
unbounded words, null periodic words and terminal divisor chains, remains.
The continued-fraction coordinate is a coordinate of this same source,
not a second physical owner from which a return clock is borrowed.

The gate is the complete fixed classification on
`W=[2,4,4] union [2,4,8,3]`, both WHOLE cylinders with arbitrary infinite tails.
For each resulting core, the task includes the full-X incoming class,
entire stabilizer, phases and repetitions. One positive primitive not equal
to log an ordinary prime, or one duplicate-prime packet, stops MAIN.
All-prime coverage and stronger arithmetic naturalness are additional,
separate questions. No other cylinder or nonfixed-period search is performed.

## 2. Construction of the original CF coordinate and measure

For a positive integer a define `H_a(t)=1/(a+t)` on `[0,1]`.
For a finite word `w=(a_0,...,a_(m-1))`, let `H_w=H_a0 o ... o H_a(m-1)`;
the empty word has H=id. Put `p_-1=1,p_0=0,q_-1=0,q_0=1`, and for j>=1
set `p_j=a_(j-1)p_(j-1)+p_(j-2)`, `q_j=a_(j-1)q_(j-1)+q_(j-2)`.
Direct induction gives

`H_w(t)=(p_m+p_(m-1)t)/(q_m+q_(m-1)t)`,
`|p_m q_(m-1)-p_(m-1)q_m|=1`,
`|H'_w(t)|=1/(q_m+q_(m-1)t)^2`.

The intervals `H_(a0,...,a(m-1))([0,1])` are nested and have diameter
`1/[q_m(q_m+q_(m-1))]`. Since all digits are positive, the denominator
recurrence bounds q below by an unbounded Fibonacci recurrence, so these
diameters tend to zero. Their unique common point defines pi of the word.
For every shifted word the same construction gives a tail coordinate r_j
with `r_j=1/(a_j+r_(j+1))`. Initially `r_j>=1/(a_j+1)>0`; the positive
next tail then gives `r_j<1`, including when a_j=1. Thus every r_j lies
strictly in `(0,1)`, and `floor(1/r_j)=a_j` recovers its digit.

These coordinates are irrational. Indeed, for a rational `p/q in(0,1)`
in lowest terms, the positive remainder of `q/p` has reduced denominator
at most p<q. Repeated reciprocal remainder therefore eventually reaches
zero. Our positive infinite tail recursion never does, a contradiction.
Conversely, on any irrational x in `(0,1)`, successive reciprocal
remainders stay irrational in `(0,1)` and produce positive digits. The
original x belongs to every resulting nested interval and is its unique
limit. This proves bijectivity onto precisely the irrationals in `(0,1)`.

The shrinking cylinder diameters prove continuity of pi at each word.
Digit extraction by the Borel floor/remainder maps proves its inverse Borel.
More explicitly, pi sends a cylinder `[w]` to
`H_w((0,1) minus Q)`, the open rational-endpoint interval with its rational
points removed. Hence pi is a Borel bijection, and images of Borel sets are
Borel by its Borel inverse. No convention for finite rational expansions is needed.

Define `rho(x)=1/((log2)(1+x))` and
`mu(E)=integral_(pi(E)) rho(x) dx`.
This is a probability: `integral_0^1 dx/(1+x)=log2`, and removing countably
many rational points does not change the integral. Every nonempty cylinder
has positive mass because its coordinate interval has positive length and
rho is strictly positive. Thus mu has full support. Every singleton has
zero mass, proving nonatomicity without removing any such state.

For the baseline left shift sigma, pi intertwines sigma with
`G(x)=1/x-floor(1/x)` on irrationals. Its inverse branches are H_a. Their
mu-IMAGE densities at t are

`j_a(t)=rho(H_a(t)) |H'_a(t)| /rho(t)
        =(1+t)/[(a+t)(a+t+1)]`.

The sum over ALL a>=1 telescopes to 1:
`sum_a j_a(t)=(1+t)sum_a(1/(a+t)-1/(a+t+1))=1`.
Change of variables on each branch and nonnegative countable additivity
therefore give `mu(sigma^-1 E)=mu(E)` for EVERY Borel E. This is an own
proof of the frozen baseline relation. It does not establish invariance
for M/A/Q/R, canonical uniqueness of mu, or prime naturalness; none is assumed.

## 3. Four maps, genuine terminals and complete inverse prescriptions

Write `D(a,b)` for `1<a<b` and `a|b`.
For `x=(a_0,a_1,...)` define `k(x)=min{k>=1:not D(a_(k-1),a_k)}` when finite.
Let Omega be this finite-k domain, and Z its complement. Omega is the
countable disjoint union of the cylinders `[U]` with
`U=(a_0,...,a_k)`, all earlier adjacent tests true and the last false.
Z is the Borel set of infinite success chains. It is terminal for M/Q,
with units and all incoming retained, and is not terminal for the total A/R.

Every displayed rewrite leaves its remaining infinite tail xi untouched:

| Owner | Own domain | Input U and actual output V |
| --- | --- | --- |
| M | Omega | k=1: `(a0,a1)->(a0+a1)`; k>=2: `(a0,...,a_k)->(a1/a0,...,a_(k-1)/a_(k-2),a_k)` |
| A | X | Every `(a,b)->(a+b)` |
| Q | Omega | k=1: same sum; k>=2: `(a0,...,a_k)->(a1,...,a_k)` |
| R | X | Every `(a,b)->(b/a)` if D(a,b), otherwise `(a+b)` |

Each M/Q prefix U is determined by the ACTUAL first failure, not a chosen
shorter successful prefix. Every output is a positive finite word, and
each source cylinder is mapped homeomorphically onto its full `[V]`.
Thus the four maps are Borel. They need not be globally one-to-one.

For each own branch define `I_U(V xi)=U xi` on the WHOLE `[V]`.
Both inverse identities follow from removing/inserting these finite prefixes.
If `Tz=y`, the unique source parser (or the actual first pair for A/R)
recovers a branch U and gives `z=I_U(y)`. Conversely every listed inverse
is a genuine predecessor. This proves completeness over every label and
length. Target outgoing permission is never imposed. Actual predecessor
sets, not label lists with multiplicity, are used when domains overlap.
In particular, full incoming to M/Q's terminal set is not discarded.

## 4. Every-point own IMAGE and original-measure histories

For a branch `U->V` and `y=V xi`, set `t=pi(xi)`.
The coordinate of I_U is the differentiable map `H_U o H_V^-1` on the
full real coordinate interval of `[V]`. Its derivative has absolute value
`|H'_U(t)|/|H'_V(t)|`. The positive q-denominators above and `0<t<1`
prove positive finiteness. Change of variables with the ORIGINAL density gives

`J_UV(y)=[(1+H_V(t))/(1+H_U(t))] |H'_U(t)|/|H'_V(t)|`,
`mu(I_U E)=integral_E J_UV dmu` for EVERY Borel `E subset [V]`.

Explicitly, for `B=H_V^-1(pi(E))`, both sides equal
`(1/log2) integral_B |H'_U(t)|/(1+H_U(t)) dt` by substitution.
Thus the statement holds on arbitrary Borel sets, not just whole cylinders;
rational endpoints have no symbolic objects. The displayed
formula is prescribed at every infinite word, including null returning
words. It is an explicit geometric version, not a consequence of a.e.
uniqueness on those points. For each owner's actual branch put
`kappa(x)=-log J_UV(Tx)`. No other measure, word-mass ratio or positive roof
replaces this possibly signed or zero value.

Finite itinerary charts are again finite-prefix substitutions on cylinders:
intersect the current output cylinder with the next input cylinder; finite
prefixes are comparable or disjoint. Pulling back a nonempty intersection
gives a cylinder with another prefix substitution. Induction gives countably
many charts for each legal iterate, even though the parser length is unbounded.
The prescribed derivative multiplies along these charts by the ordinary
chain rule and density cancellation, pointwise as well as in every-Borel IMAGE.

For EACH owner, let D_r be its legal r-step domain, `D_0=X`, and put
`S_r(x)=sum_(0<=j<r) kappa(T^j x)`, `S_0=0`.
The actual groupoid is

`G={(z,r-s,w):z in D_r,w in D_s,T^r z=T^s w}`,

with source w, range z, lag retained and equal actual triples identified.
Multiplication adds lags and inversion reverses them. Terminal units are
present, but positive iterates through a terminal are not invented.

Define `c(z,r-s,w)=S_r(z)-S_s(w)`.
For two witnesses of the same lag, their pairs `(r,s)` differ by a common
integer. Ordering the pairs, the longer witness guarantees that their common
endpoint admits the extra steps. Both sums gain the same added segment,
so c is well defined. In a product of arrows, extend the shorter middle
history to the longer legal middle history; its two sums then cancel.
This proves additivity, inverse sign reversal, and `c(Tz,-1,z)=-kappa(z)`.

On any history-pair chart `b=(T^r|C)^-1 o (T^s|D)` from w to z, chain
rule and the previous IMAGE formula give, for every Borel E in its domain,

`mu(bE)=integral_E exp(S_s(w)-S_r(bw)) dmu(w)
       =integral_E exp(-c(bw,r-s,w)) dmu(w)`.

Refinements and alternate legal witnesses have the same c as just proved.
Hence this is the full history-pair IMAGE for the ORIGINAL mu of each owner.

## 5. Full kernels, incoming, entire isotropy and exact phase tests

The full three kernels, always using the current owner's T and sums, are

`K_lag={(z,0,w):some legal equal-length iterates of z,w meet}`;
`K_clock={(z,r-s,w):T^r z=T^s w legally,S_r(z)=S_s(w)}`;
`K_joint=K_lag intersect K_clock`.

No equivalence of these kernels is assumed. In particular the baseline
shift's invariant measure does not imply a zero clock for any rewrite.
The extension uses the FULL `X times R_h`, with arrows
`(w,h)->(z,h+c(z,k,w))`. Height translation acts on its orbit SET only;
no regular quotient, section, manifold or positive suspension is asserted.
Base orbit membership is exactly the existence of meeting legal iterates.
Two lifted points are equivalent exactly when some ACTUAL `(z,k,w)` has
`h_z-h_w=c(z,k,w)`. These tests keep every allowable history.

For every full-source y define
`Pre_T(y)={U xi:y=V xi for some actual own branch U->V}`.
For a core set C let `Pre^0(C)=C` and
`Pre^(j+1)(C)=union_(y in Pre^j(C)) Pre(y)`.
The two inverse identities prove by induction that this is EXACTLY the
set of all states whose legal j-th iterate lies in C. Thus
`B_T(C)=union_(j>=0) Pre^j(C)` is complete at ALL depths, with no label,
length or outgoing-target cutoff. Compatible infinite histories are exactly
chains `(x_0,x_-1,...)` with `x_0 in C` and `x_(-j-1) in Pre(x_-j)` for all j.
Every actual chain satisfies this prescription, and each prescribed chain
has every legal finite prefix. No inverse-limit points or duplicate arrows
are silently added to X. This applies to every owner, including terminal targets.

A nonzero isotropy lag gives `T^(s+p)x=T^s x` for some p>0 and hence an
actual eventual cycle. Conversely eventual cycles supply isotropy.
If the least discrete cycle period is p, all isotropy lags are exactly pZ:
any returning lag must be divisible by p on the eventual cycle, and all
multiples occur after extending beyond the arrival tail. If there is no
eventual cycle, isotropy is zero. Put `C=sum_cycle kappa` for one primitive
discrete cycle. Cancellation of the common incoming segment gives
`c(x,mp,x)=mC`. This is independent of the chosen cycle phase.
Source isotropy is pZ and extension isotropy is `{mp:mC=0}`; in particular
zero-clock isotropy remains in the extension rather than being deleted.

The ENTIRE physical stabilizer is `H_x=C Z` at any eventual-cycle state,
and `{0}` otherwise. Indeed `[x,h+t]=[x,h]` holds precisely when an
isotropy arrow at x has clock t. This argument uses all isotropy, not one
selected loop. Every base orbit supplies one translation orbit `R/H_x`:
transport to a fixed anchor and reduce the transported height modulo H;
different transport arrows differ by isotropy and yield the same coset.
If C is nonzero, its positive primitive is `|C|`, with positive repeats
`m|C|`; signed inverse traversals remain. If C=0 there is no positive
primitive, even when source and extension isotropy are nontrivial.
Different base orbit classes remain different packets at equal times.

For a terminal t of M/Q, an incoming state has a unique arrival depth ell(x):
two depths would require legal evolution after t. Its entire orbit is
`B_T({t})`. An arrow there has lag `ell(z)-ell(w)` and clock
`S_{ell(z)}(z)-S_{ell(w)}(w)`. Source/extension isotropy and H are zero;
its exact phase at t is `h-S_{ell(x)}(x)` in R, not modulo a fictitious period.
A/R have no terminal objects. These statements, the recursion and the general
tests specify all incoming and phases without a global periodic census.

## 6. Complete fixed classification in the two full cylinders

Write `W_1=[2,4,4]`, `W_2=[2,4,8,3]`.
For EVERY tail xi, the maximal-chain parser on W_1 has k=2: `(2,4)` passes
and `(4,4)` fails. On W_2 it has k=3: `(2,4),(4,8)` pass and `(8,3)` fails.
These statements are independent of the tail, including any terminal tail.

| Owner | Image of `(2,4,4,xi)` | Image of `(2,4,8,3,xi)` |
| --- | --- | --- |
| M | `(2,4,xi)` | `(2,2,3,xi)` |
| A | `(6,4,xi)` | `(6,8,3,xi)` |
| Q | `(4,4,xi)` | `(4,8,3,xi)` |
| R | `(2,4,xi)` | `(2,8,3,xi)` |

On W_1, M and R fix a state precisely when `xi=(4,xi)`.
Iterating this equation forces every digit of xi to be 4; conversely that
tail satisfies it. Thus there is exactly one such fixed state
`P=(2,4,4,4,...)`. A and Q fail already at the first digit.
On W_2, M and R fail at the second digit, while A/Q fail at the first.
Therefore the complete classifications are

`Fix(M) intersect W=Fix(R) intersect W={P}`,
`Fix(A) intersect W=Fix(Q) intersect W=empty`.

No infinite tail was sampled or selected; these equations exhaust both
whole cylinders. There are no omitted cylinder families of fixed states.

## 7. Owned fixed clocks, unrestricted basins and entire packets

Let `eta=(4,4,...)` and `t=pi(eta)`. The coordinate construction gives
`t=H_4(t)=1/(4+t)`, whence the positive root is `t=sqrt(5)-2` in `(0,1)`.
In M's actual P branch, `U=(2,4,4)`, `V=(2,4)`, and both H_U(t),H_V(t)
equal pi(P). The density factors in J therefore cancel. Since `U=V(4)`
and H_4(t)=t, the chain rule gives `J_M(P)=|H'_4(t)|=t^2`.
For R independently, the actual prefixes are `U=(2,4)`, `V=(2)` and again
`U=V(4)`, so its OWN IMAGE gives `J_R(P)=t^2`.
Thus both local fixed clocks are

`K=-log(t^2)=2 log(2+sqrt(5))=log(9+4sqrt(5))>0`.

This derives the value from each actual transport at P, not from a chosen
word probability, baseline-shift clock or inserted target period.
Proper divisibility is active: `(2,4)` is the first successful edge and
M's quotient writeback produces 2. A and Q do not return P.
R DOES share this fixed return and clock; the long-chain control does not
separate the tested packet. On all of W_2, M/R have different actual images
as Section6 shows, but this nonreturning distinction is not a prime result.

The full incoming basins are independently defined by
`B_M=union_j Pre_M^j({P})`, `B_R=union_j Pre_R^j({P})` with Section5's
unrestricted, all-depth-complete recursion. Their immediate predecessors
can also be written explicitly, illustrating that the two atlases differ.
For R they are

`Pre_R(P)={(1,1,eta)} union {(d,2d,eta):d>=2}`.

For M they are the first singleton above together with, for every k>=2,d>=2,
the sequence whose digits are

`a_0=d; a_j=2*4^(j-1)*d for 1<=j<=k-1; a_k=4`, followed by eta.

To verify exhaustiveness, a k=1 sum output equal to P's first digit 2
forces `(1,1)`. For k>=2, P's output quotient digits force the first ratio
2 and all subsequent ratios 4; its retained final digit is 4. This gives
exactly the displayed inputs. Their last chain digit is at least 4, so its
edge to 4 fails as required, while all preceding ratios give proper
divisibility. R has just the corresponding two-letter quotient test.
The k=2,d=2 term in both lists is P. No incoming level is restricted to W;
further levels and all infinite compatible prehistories use the full recursion.

For either O=M or O=R, B_O is the ENTIRE base orbit class of P: sharing a
future with a fixed P is equivalent to reaching P. For x in B_O choose any
arrival depth ell and put `E_O(x)=S^O_ell(x)-ell K`.
Any later arrival adds the corresponding multiple of K, so E_O is well
defined and E_O(P)=0. All integer lags between any two points are realized
by choosing r,s sufficiently large after their arrivals. Thus, separately,

`G_O|B_O = B_O times Z times B_O`,
`c_O(z,k,w)=E_O(z)-E_O(w)+kK`.

The formula follows for all histories by extending them to arrivals at P.
The full lag kernel is k=0; clock kernel is `E_O(z)-E_O(w)+kK=0`;
their intersection is k=0 and equal E_O values. At EVERY incoming point,
source isotropy is Z, its ENTIRE clock image is KZ, and extension isotropy
is zero. Arbitrarily long incoming excursions cannot reduce the generator,
because their endpoint terms cancel in every actual isotropy loop.
The exact phase is `h-E_O(x) mod K`, equivalently `h-S^O_ell(x) mod K`.
All phases form one circle packet for each owner; predecessors and phase
choices are not additional packets. The primitive is K and its positive
repetitions are mK for m>=1, with negative traversals also retained.

Finally `9+4sqrt(5)` is irrational. If sqrt(5)=a/b in lowest positive terms,
`a^2=5b^2` forces 5 to divide both a and b, a contradiction. Hence exp(K)
cannot be any ordinary integer prime. Since the ENTIRE H is KZ, K cannot
be shortened into an unproved prime-log divisor of this primitive.
This single owned MAIN packet refutes the necessary universal prime purity.
A/Q have no fixed cores in W and hence no incoming fixed packets there;
their full domains, kernels, histories and possible other cores are not deleted.

## 8. Gate assessment, controls and stop boundary

| Owner | Complete fixed set in W | Entire fixed-packet conclusion |
| --- | --- | --- |
| M | P only | One packet, H=KZ, K=log(9+4sqrt(5)), nonprime |
| A | Empty | No fixed packet in this window; own full IMAGE retained |
| Q | Empty | No fixed packet in this window; own parser terminals retained |
| R | P only | Same K, derived from its own inverse and own full basin |

T0: full coordinate, original probability, branch atlas, pointwise IMAGE,
actual histories and quotient-set physical action are established.
T1: direct symbolic arithmetic feedback and an owned clock are established,
but prime-side adequacy/strong naturalness are NOT PASSED. T2: the bounded
fixed packet and its full repetition law are owned; MAIN's necessary
universal prime-purity condition is REFUTED. T3 is NOT AUDITED. Classical
A0–A2 are NOT APPLICABLE; formal coordinates UNASSIGNED; B NOT INVOKED.

Three OFF maps change actual actions, not just density or acceptance labels.
A/Q separate the divisor and quotient operations at P; R is an explicit
non-separating return control. Long-chain feedback changes W_2's actual
writeback but supplies no additional positive claim. This negative control
must not be hidden behind a claim of superior arithmetic selectivity.
PROVES_TOO_MUCH and strong naturalness remain distinct, unresolved questions.

The geometric derivative is not the former fixed dyadic word-length ratio.
That fact alone does NOT prove infinite-rank periodic support. Neither
infinite rank nor a global finite-rank obstruction is established here.
Other fixed cylinders, higher periods, global packet multiplicities and
all-prime coverage are unclassified; this does not reopen refuted purity.

Decision: STOP / FORK MCR01 immediately on its owned nonprime primitive.
No density, parser, roof, selected-tail or inverse-label repair is made.
No new candidate, operator, formal Route evaluation or round480 is authorized here.

## 9. Reproducibility, access and AI disclosure

The author personally read the 105-line scientific card through its explicit
EOF and verified the Section1 SHA before derivation. No current independent
raw proof, reviewer answer, sibling manuscript or old proof was read.
Root reported CP1 approval before distinct author release; that scope report
was not read by this author. At author freeze, independent final CP2/CP3
review was pending; subsequent review is recorded separately in
`evidence/review.md`, with no verdict presumed by this manuscript.

The same-author helper `cf_foundation_author` was assigned ONLY the original
card's CF coordinate, original measure, baseline shift and IMAGE foundation,
not the fixed-window/packet calculation. It supplies author-side assistance,
not an independent reviewer or validation vote; no helper file writes were
authorized. The main author owns all integrated proofs and three author files.
The helper returned its full self-contained foundation argument after reading
only card1–105 through EOF as new science, with the same Section1 SHA.
The main author compared its recurrence, Borel, telescoping and arbitrary-Borel
change-of-variables arguments against Sections2/4 before author freeze.
This author-side comparison is not CP2/CP3 or an external correctness certificate.

Design exposure is preserved: as scout, this author read370 card1–82 of123,
prefix SHA `b424856771d1678ed0f57c95f9f3ddec58468f3c4e40acd0040d5426ea03b25e`,
and325 card1–72 of197, prefix SHA
`b2520e2775d5f23b4082b94c441b8100fe0fe17e024721f0da0499366da4213f`.
Neither read reached EOF or Outcome bodies; headings-only discovery exposed
Outcome titles. The original definition/status assertions were exposed.
This is also the prior474 author with inherited shared research history,
including earlier review work and summary exposures. Root/scout informal
parsing, fixed-word feasibility and clock-form exploration preceded freeze.
No outcome-blind preregistration, new isolated context, novelty or
nonconjugacy theorem is claimed; old results are not scientific premises.

ARS router and research-architect guidance were personally read in the design
turn; deep workflow, runtime, DA, fallacies, anti-leakage and local governance
were retained from full personal reads. For author writing, the retained
paper workflow, draft-writer, style, title and writing-quality instructions
were used to separate definitions, proof, adverse controls and claim limits.
This scoped mathematical manuscript is not a complete submission pipeline
or a venue-calibrated review. No human-read or external verification is invented.

AI disclosure: author and helper are same-model AI agents with inherited
shared history, internally NOT_CALIBRATED. No blind, human, external or
cross-model peer certification is claimed. Root owns card/integration and
a different reviewer owns independent review. There are no scientific
numerics, data collection, network calls, Git actions, PDFs or external
uploads. No human authorship, funder or conflict declaration was supplied
and none is fabricated. Mechanical line/hash/link checks are not evidence
for an infinite dynamical claim. The outcome is a negative bounded gate,
not an RH, Hilbert–Pólya or prime-spectrum construction.

EOF — ANG-20260925-MCR01 author manuscript.
