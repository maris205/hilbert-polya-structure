# CPM01 — isolated raw class audit

Candidate ID: ANG-AUDIT-20260925-CPM01. Paper 480, batch
PRE-P0-STRUCTURE-20260925-AA, round 1/5.
Raw outcome: EXACT CF PREFIX CLASS OBSTRUCTION — NO POSITIVE PRIME-LOG
PRIMITIVE; conditional audit, NOT a MAIN candidate or Route result.

## 1. Scientific input, exposure and proof boundary

The sole newly opened scientific input is the original
[candidate card](../candidate-card.md), 91 lines, SHA-256
`4138766434cb4f888ba85d7a96b561c87e8aeb6c0327fc44e72d503b4e4eb102`.
Its line count/hash were rechecked after DISTINCT RAW RELEASE. The separate
[scope review](scope-review.md) has 87 lines, SHA-256
`9c298e2f9a8228e427ecfa4ca99d37278e6dbb7f3aa2f3134d7c2d69d5029f78`.
No current author/helper/peer or old proof file was opened for this audit.
This reused reviewer retains 476/474 work and root history; the derivation
is same-model/shared-history AI, NOT_CALIBRATED, not blind, human, external
or error-independent. The disclosed design exposure is not preregistration.

The personally read ARS/router/workflow/runtime/DA/fallacy and local
governance instructions remain retained as recorded in CP1. The method is
exact coding, change of variables, integer-matrix case analysis and actual
history arguments. The coordinate and measure are proved below, rather
than importing a theorem from 476. No scientific numerical code, search,
network, Git, PDF, old-file write or operator is used. Only this raw record
is written; current manuscript access remains LOCKED until distinct unlock.

## 2. Entire CF coordinate and original probability

For a finite nonempty word w=(a_0,...,a_(m-1)), use
p_-1=1,p_0=0,q_-1=0,q_0=1 and, for j>=1,

    p_j=a_(j-1)p_(j-1)+p_(j-2),
    q_j=a_(j-1)q_(j-1)+q_(j-2).

Induction on H_a(t)=1/(a+t) gives

    H_w(t)=(p_m+p_(m-1)t)/(q_m+q_(m-1)t),
    H'_w(t)=(-1)^m/(q_m+q_(m-1)t)^2.

The image of [0,1] has diameter 1/[q_m(q_m+q_(m-1))]. For any infinite
positive-digit word these image intervals are nested; q grows at least
along a Fibonacci recurrence, so their diameters tend to zero. Their
unique common point defines pi. Each suffix coordinate t_j satisfies
t_j=1/(a_j+t_(j+1)); it is at least 1/(a_j+1)>0 and, since its successor
is positive, is strictly below 1. Thus floor(1/t_j)=a_j recovers the digit.

A rational value p/q in (0,1), in lowest terms, would have successive
reciprocal remainders with strictly decreasing positive denominators
until the remainder is zero. The infinite positive-tail recursion cannot
do that. Hence pi's values are irrational. Conversely an irrational value
in (0,1) has an infinite sequence of positive reciprocal-remainder digits,
and belongs to every associated shrinking interval. This reconstructs it
uniquely. Thus pi is a bijection onto Y=(0,1) minus the rationals.

Shrinking cylinder diameters prove continuity of pi in the product
topology. The inverse digit coordinates are successive Borel floors of
reciprocal remainders, so the inverse is Borel. In particular pi is a
Borel isomorphism; for every finite w, pi([w])=H_w(Y), the open interval
between its rational endpoints with rationals removed. The empty word
has H=id and [empty]=X. Every infinite word, including unit strings,
unbounded digits and null periodic words, remains in X. Rational finite
expansions and an infinite letter were never objects of the frozen source.

Let rho(u)=1/[log(2)(1+u)]. The frozen mu(E)=integral_(pi(E))rho(u)du
is therefore a Borel probability: integral_0^1 du/(1+u)=log2 and the
rationals are null. Every nonempty cylinder has positive measure, since
its real interval has positive length and rho is positive. Singletons
have zero measure. This proves normalization, full support and
nonatomicity without deleting any null source state.

## 3. Every member's actual inverse and IMAGE

Fix an arbitrary member of the frozen class. Its source words U_i have
pairwise disjoint full cylinders, and Omega is their union. If an input
word is empty it is the sole source branch; if there are no branches,
Omega is empty. Each actual branch T(U_i xi)=V_i xi is a homeomorphism
from its whole source cylinder onto its whole output cylinder, including
empty output words. Its inverse is I_i(V_i xi)=U_i xi on all [V_i].
Both identities hold at every point. Conversely the disjoint source
partition recovers the actual branch of every predecessor, proving that
these inverses are complete. Overlapping output cylinders are kept; a
target's outgoing permission is never imposed on an inverse branch.

For Borel E subset [V_i], write E={V_i xi:xi in B} and C=pi(B).
Change of variables under the finite H maps, or the identity for an
empty word, gives

    mu(I_i E) = integral_C rho(H_Ui(t)) |H'_Ui(t)| dt,
    mu(E)     = integral_C rho(H_Vi(t)) |H'_Vi(t)| dt.

Their ratio is the prescribed

    J_i(V_i xi)=[(1+H_Vi(t))/(1+H_Ui(t))]
                    |H'_Ui(t)|/|H'_Vi(t)|, t=pi(xi).

Every factor is positive finite on Y; H_empty'=1. Substitution proves
mu(I_i E)=integral_E J_i dmu for every Borel E, not merely cylinder
totals. The exact geometric formula is the chosen version at EVERY point,
including null periodic points. It is not inferred from a.e. uniqueness.

On the corresponding real source interval, put
f_i=H_Vi composed H_Ui^-1. For u=pi(x), v=pi(Tx), direct division gives

    kappa(x)=log|f_i'(u)|+b(x)-b(Tx),
    b(x)=log(1+pi(x)).                                      (1)

Thus signs and zeros are kept. The density term is an endpoint difference,
not a second clock. The original measure and its null version never change.

Intersecting an output cylinder with the next source cylinder either
gives the empty set or a comparable longer prefix. Refinement by that
prefix shows inductively that every finite legal iterate has a countable
cover by prefix-substitution charts. The pointwise derivative ratios
compose by the chain rule and density cancellation. Empty words cause no
exception to this refinement argument.

## 4. Full history, kernels and all incoming

For this member let D_r be the actual legal r-step domain, D_0=X, and
S_r(x)=sum_(j<r)kappa(T^j x), S_0=0. Use exactly

    G_T={(x,r-s,y):T^r x=T^s y legally},
    c(x,r-s,y)=S_r(x)-S_s(y).

Equal actual triples are identified, but different lags remain distinct.
Two same-lag witnesses differ by a common increment of both exponents;
the longer witness ensures the extra common future is legal, and its
sums cancel. Hence c descends pointwise. Extending the shorter middle
history when composing arrows cancels the middle sums and proves
additivity and sign reversal. In particular c(Tx,-1,x)=-kappa(x).
No extension after a terminal is inserted.

On an actual history-pair chart a=(T^r)^-1 composed T^s, the preceding
every-Borel identities and their finite compositions give

    mu(aE)=integral_E exp(S_s(y)-S_r(a y))dmu(y)
           =integral_E exp(-c(a y,r-s,y))dmu(y).

The full kernels are the exact following sets, with all depths legal:

    K_lag={(x,0,y):exists r, T^r x=T^r y};
    K_clock={(x,r-s,y):T^r x=T^s y, S_r(x)=S_s(y)};
    K_joint={(x,0,y):exists r, T^r x=T^r y, S_r(x)=S_r(y)}.

These are complete existential descriptions under the member's actual
map and sums; no finite decision procedure or generic equality of kernels
is asserted. They also apply to all three controls below.

For every target y, including a terminal, set

    Pre(y)={U_i xi:y=V_i xi};
    P_0(C)=C,  P_(j+1)(C)=union_(y in P_j(C)) Pre(y).

The inverse identities prove by induction that P_j(C) is exactly the
legal j-step predecessor set for EVERY j. Full incoming is their union.
Compatible infinite histories are precisely chains (x_0,x_-1,...),
x_0 in C, x_(-j-1) in Pre(x_-j) for every j. This compatibility condition
does not infer an infinite path from unrelated finite-depth vertices and
does not adjoin extra states or multiply actual arrows. All labels and
all depths remain; no source/outgoing test is added at the target.

Base orbit membership is exactly the existence of meeting legal iterates.
On full X times R, (y,h)->(x,h+c) gives the exact lifted-orbit test
h_x-h_y=c(x,k,y) for some actual arrow. Height translation acts on the
orbit SET, without a section, topological closure of the relation, or
assumed regular quotient.

## 5. Entire stabilizers and the non-eventual case

A nonzero source-isotropy lag gives T^(s+p)x=T^s x for some p>0, hence
an eventual actual cycle. If its least discrete period is p, all and only
lags in pZ occur in isotropy: necessity follows on that cycle and every
multiple is realized after a sufficiently long legal prefix. If the
primitive discrete cycle sum is C, transient cancellation gives

    c(x,mp,x)=mC,   H_x=CZ,
    extension isotropy={mp:mC=0}.                            (2)

If x is not eventually periodic, source isotropy is trivial, hence so
are extension isotropy and H_x. It CANNOT produce a positive physical
stabilizer. Clock values on incoming or off-diagonal arrows are not loop
periods, and taking limits or closure of them is not part of this owner.

To verify the physical claim in (2), [x,h+t]=[x,h] means precisely that
an isotropy arrow at x has clock t. More generally choose an anchor a in
a source orbit and one arrow a->x of clock t_x. All arrow clocks y->x
are exactly t_x-t_y+H_a, by comparison with anchor isotropy. Hence the
full phases above that source orbit are h-t_x modulo H_a. Every base
orbit yields one entire height-translation packet R/H_a. If C is nonzero,
its positive primitive is |C| and all positive repeats are m|C|; if C=0,
no positive primitive exists but source and extension isotropy pZ remain.
Distinct base orbits remain distinct packets even at equal times.

For a terminal t, an incoming x has a unique arrival depth ell(x), since
two depths would require evolution after t. Its full orbit is P_*(t),
all arrow lags are ell(x)-ell(y), and their clocks are
S_ell(x)(x)-S_ell(y)(y). The exact phase at t is h-S_ell(x)(x) in R;
all isotropy and H are zero. In particular the empty parser has only
unit arrows on all X, zeroth-depth incoming set {x}, empty positive-depth
incoming sets and no infinite predecessor chain: there is no outgoing
step to supply one. Its height
orbits are free lines, not periodic or absorbing source loops.

## 6. Actual matrix reduction, neighborhood and cancellation

Associate E_a=[[0,1],[1,a]] to H_a, with ordered products E_w and
E_empty=I. These are integral unimodular matrices with determinant
(-1)^|w|. Their standard fractional action is precisely H_w, as direct
composition or Section 2's formula verifies. The actual branch map f_i
therefore has representative

    B_i=E_Vi E_Ui^(-1) in GL(2,Z).

For an actual least-period-p point x_0, follow its actual branch itinerary
i_0,...,i_(p-1). Finite prefix refinement supplies a cylinder neighborhood
on which that entire itinerary is legal. Equivalently, each intermediate
coordinate lies in its open real source interval, so a small real
neighborhood avoids their finitely many boundaries and poles. There the
actual return map has fractional representative

    Q=B_(i_(p-1)) ... B_(i_0)=[[a,b],[c,d]],
    delta=det Q in {1,-1},  tau=a+d.

All orderings are thus tied to the actual map, not a chosen matrix word.
Writing u=pi(x_0), we have Q.u=u. Equation (1) telescopes around this
actual cycle, and the chain rule gives its signed sum

    C=log|(T^p_coordinate)'(u)|
      =log(|delta|/(c u+d)^2)=-2 log|c u+d|.                (3)

There is no lost sign from orientation reversal: delta=-1 is allowed,
the IMAGE uses absolute derivatives, and the physical primitive is |C|,
not an additional doubling to restore orientation.

An integral unimodular matrix's denominator can vanish only at a rational
point when c is nonzero; if c=0 then d is nonzero. Hence no actual
irrational state is a denominator pole. The finite itinerary additionally
ensures its intermediate states lie in the legal cylinder intervals.
Their rational endpoints are not source objects. These facts justify
the local derivative computation, not a new deletion of problematic states.
Conversely, an algebraic fixed point of a matrix is NOT automatically a
legal source cycle; no such sufficiency or realization claim is made.

## 7. Exhaustive integral algebra, including degenerate cases

The fixed equation is

    c u^2+(d-a)u-b=0,   Delta=tau^2-4delta.                 (4)

If c=0, irrational u forces d=a and b=0. Thus a realizable irrational
fixed point in this case requires Q scalar. A scalar integral unimodular
matrix is exactly I or -I, both projectively identity and delta=1.
Then C=0. Non-scalar c=0 matrices have at most a rational finite fixed
point, or none, and cannot be the return matrix at an actual irrational
periodic state.

For c nonzero, a real irrational solution of (4) requires Delta>0 and
not a square. Delta<0 has no real root; Delta=0 or a positive square
gives only rational roots. For completeness all determinant/trace cases
are as follows (scalar cases were already separated):

| delta and tau | Discriminant case | Consequence for an actual irrational fixed state |
| --- | --- | --- |
| delta=1, abs(tau)<2 | Delta<0 | Impossible |
| delta=1, abs(tau)=2 | Delta=0; non-scalar parabolic | Impossible |
| delta=1, abs(tau)>2 | Delta>0 nonsquare | Only potentially realizable case for this sign |
| delta=-1, tau=0 | Delta=4 | Rational fixed roots only; impossible |
| delta=-1, tau not zero | Delta=tau²+4>0 nonsquare | Only potentially realizable case for this sign |

To check the nonsquare statements, for abs(tau)>=3 the number tau²-4
lies strictly between (abs(tau)-1)² and tau². For tau²+4=m², the positive
integer factors (m-abs(tau))(m+abs(tau)) equal 4 and have the same parity;
the only possibility is 2,2, giving tau=0. Singular matrices are excluded
by the proven GL(2,Z) membership, not omitted as an unexamined case.

In either potentially realizable non-scalar case put

    mu=c u+d,  nu=delta/mu.

The fixed-vector equation Q(u,1)=mu(u,1) proves mu is an eigenvalue,
and the characteristic polynomial gives
mu+nu=tau, mu nu=delta. The two eigenvalues are distinct real conjugate
quadratic units. Neither has absolute value 1: that would force tau=+/-2
when delta=1 or tau=0 when delta=-1, the excluded nonscalar cases above.
By (3), C is nonzero. Its physical primitive L=|C| satisfies

    lambda=exp(L)=max(mu²,mu^(-2))>1,
    {mu²,mu^(-2)}={mu²,nu²},
    lambda+lambda^(-1)=tau²-2delta=:N.                     (5)

Here N is an integer greater than 2. Thus lambda is the greater root of
z²-Nz+1. It is a quadratic irrational: for N>=3, N²-4 lies strictly
between (N-1)² and N². Its conjugate is lambda^(-1), and its norm is 1.
In particular lambda is NOT any rational number and cannot be an ordinary
integer prime. This proves the desired obstruction for every actual
nonzero-cycle clock, with both determinant signs and either clock sign.

If Q is projectively equal to another unimodular integral representative,
the real scalar between them is +/-1: determinants force its square to
be 1. The action, delta, N and |mu| are unchanged. An arbitrary nonzero
scalar representative outside this normalization also leaves
|det Q|/(c u+d)^2 unchanged. No multiplier is obtained by discarding the
determinant normalization or taking the wrong eigenvalue branch.

The remaining scalar case is not a discarded degeneracy. If Q=+/-I on
a legal itinerary neighborhood, T^p is identity there by the Borel
coordinate's injectivity. All tails in that neighborhood are retained.
Their least periods divide p, and their p-step clock is zero. Therefore
their least-cycle clock is zero as well; all have H=0 with their own
nonzero source/extension isotropy retained. This includes continuum
identity families rather than selecting one representative from them.
Empty words use identity matrices and are included in every calculation.

Combining Sections 5–7: a non-eventual source has H=0; an actual eventual
cycle either has C=0 and no positive primitive, or has entire H=CZ with
positive primitive L whose exponential is the irrational unit (5).
NO source of any frozen class member has a positive primitive log p for
an ordinary prime p. This is a necessary class filter, not a construction
of all possible multipliers or a positive arithmetic theorem.

## 8. Complete control I — IDENTITY

Its only branch is empty->empty, on all X. The actual inverse is identity,
J=1 at every point, and kappa=0. Every point is fixed with least discrete
period 1. The full groupoid consists of (x,k,x), k in Z; there are no
arrows between different x. Hence K_lag and K_joint are units, K_clock
is the whole groupoid, source isotropy is Z and c=0 everywhere.
Extension isotropy is Z at every height, H=0, and each source singleton
gives one free real-line translation packet with every height retained.
There is no positive primitive or positive repetition. Pre(x)={x}; all
finite incoming sets are {x}, and the only compatible infinite history
is constant. The continuum of different source objects is never collapsed.

## 9. Complete control II — FULL SHIFT

The own branches (a)->empty make T=sigma on all X. At a target tail with
t=pi(y), the exact inverse is a y and its own IMAGE is

    j_a(t)=rho(H_a(t))|H'_a(t)|/rho(t)
          =(1+t)/((a+t)(a+t+1)).

Thus kappa(a y)=log((a+t)(a+t+1)/(1+t)), not zero. The sum of j_a over
all a>=1 telescopes to 1, so the same original measure is shift invariant
by every-Borel change of variables and nonnegative countable additivity.
This global invariance does not replace the actual nonzero branch clocks.

For a word w of length n and x=w xi, t=pi(xi), the complete finite sum is

    S_n(x)=-log[(1+t)|H'_w(t)|/(1+H_w(t))].                (6)

For n=0 this is zero using H_empty=id. Therefore the generic kernel and
orbit tests of Section 4 are explicit under (6) for every r,s; no kernel
is replaced by measure invariance. The complete inverse set is
Pre(y)={(a,y):a>=1}; all finite predecessors prepend arbitrary finite
words, and every compatible infinite incoming history prepends one new
arbitrary positive digit at each step. None is restricted to a periodic core.

All eventual cores are precisely primitive finite words w repeated
infinitely, with the words identified by cyclic rotation. A core of a
primitive length-m word has exactly m distinct phase states. Conversely
every eventual periodic shift state reaches one of these cores, and two
such primitive cores share a future only when their words are rotations.
Its entire incoming class is

    B_[w]={v sigma^j(w^infinity):v any finite word,
                                             0<=j<m},

as a set of actual states, without multiple copies for repeated descriptions.
This proves the complete orbit classification of the periodic part; it
does not choose one source point in place of all its phases or predecessors.

Let u=pi(w^infinity), A=E_w and beta=c_A u+d_A. Since A represents H_w,
A(u,1)=beta(u,1). Its entries give beta>1: for a nonempty positive word,
c_A>=1 and d_A>=1 and u>0. It is the positive eigenvalue of largest
absolute value, because the other is det(A)/beta. The actual m-step shift
return has Q=A^-1, so its entire cycle clock and primitive are

    K_[w]=2 log beta>0,  H=K_[w] Z.                       (7)

Every positive repetition is n K_[w]. Source isotropy on the whole basin
is mZ, extension isotropy is zero, and all phases are R/(K_[w]Z) by
Section 5. Equations (5)–(7) show this is never log an ordinary prime.
Different primitive necklaces remain different packets even when times
coincide: equality of times is exactly equality of
(tr E_w)^2-2det(E_w), since lambda>1 is the unique greater root in (5).
This is a multiplicity criterion, not a quotient identifying such packets.

Non-eventually-periodic shift states have source/extension isotropy and
H all zero; their exact tail-equivalence and phases are still given by
Sections 4–5 and (6). They cannot create omitted positive-period packets.
The control therefore supplies genuine actual positive returns, while
its complete positive primitive ledger satisfies the class obstruction.

## 10. Complete control III — DIVISOR SWAP

For x=(a,b,xi), let F(a,b)=D(a,b) or D(b,a). It is symmetric, and if
true then a is not b. T swaps the first two digits when F holds and
otherwise fixes the whole word. Hence T²=id on ALL X, and T is its own
unique global inverse. All branches still have their own prescribed
IMAGE: for U=(a,b) and V the actual output pair, put

    w_U(t)=|H'_U(t)|/(1+H_U(t)),  t=pi(xi),
    J_UV(V xi)=w_U(t)/w_V(t).

This is the formula of Section 3, proved there on every Borel set. If F
is false then U=V, so J=1 and kappa=0. Globally define the finite real
prefix-density potential ell(x)=log w_(a,b)(pi(xi)). Its actual clock is

    kappa(x)=ell(Tx)-ell(x).

Consequently on every actual history arrow,

    c(z,k,w)=ell(w)-ell(z).                               (8)

This is an identity for the original clock, not a measure change. The
complete arrows satisfy z=T^k w (the parity of k suffices). Invertibility
gives K_lag=units, hence K_joint=units. K_clock consists of exactly those
actual arrows whose endpoint ell values agree. In an exchanged pair,
even-lag isotropy is always in this kernel; odd-lag arrows are included
if and only if the two explicit w_U(t) values agree. Thus possible zero
local clocks are retained rather than incorrectly deleting the pair.

The full periodic classification is exhaustive: F false gives every such
word least period 1, and F true gives exactly the two-point core
{(a,b,xi),(b,a,xi)} of least period 2, for EVERY infinite tail xi. There
are no other periods and no transient incoming states. Pre(y)={Ty},
so finite incoming is the same singleton or two-point orbit; the unique
compatible infinite history is constant or alternating accordingly.

Every cycle sum is zero by (8). Source isotropy is Z in the fixed case
and 2Z in the exchanged case; extension isotropy is the same at every
height. Entire H is {0} everywhere. All real phases, given on each base
orbit by h+ell(x), remain, and each such base orbit gives a free translation
line, not a positive closed packet. No positive primitive exists. The
continuum of tails and all unordered exchanged digit pairs are retained;
equal values or equal zero clocks do not identify different actual orbits.

## 11. Class decision and limits

The owner, full inverse/history/phase conventions and matrix reduction are
established for EVERY member of the frozen full-cylinder prefix class.
Every eventual least-period core either has zero clock or the positive
physical primitive has exponential the quadratic irrational unit (5).
Non-eventual and terminal sources cannot supply positive H. Therefore
ordinary prime-log primitives are impossible throughout THIS exact class.

This does not assert realization of arbitrary algebraic units, a census
of an unspecified member's cycles, or a result for arbitrary Borel parsers,
different pointwise clock versions, other coordinate actions or other
carriers. It does not substitute the original measure of 476 or alter
that candidate's stopped status. The controls demonstrate actual zero and
nonzero behaviors without transferring their clocks or packet multiplicity.

Portfolio position: STOP / FORK this class as a route to the stated exact
prime-primitive target; retain the audit as a necessary search filter.
It is NOT a MAIN candidate or a positive T1 result. A future main member
still needs its own prime-symbolic lineage and frozen owner; no new member
or altered clock is authorized here. Classical fields are NOT APPLICABLE,
T1 NOT PASSED, T3 NOT AUDITED, formal coordinates UNASSIGNED and Route B
NOT INVOKED. The same-object ledger remains intact separately for every
class member and for each complete control.

This raw record is now to be frozen and fully self-read before receipt.
HOLD for root's complete read and DISTINCT PAPER UNLOCK; no author access
or paper485 is authorized by this raw completion.

EOF — CPM01 isolated exact class audit.
