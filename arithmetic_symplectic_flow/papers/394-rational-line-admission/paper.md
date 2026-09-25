# Rational-line admission for one-dimensional projective clocks

Candidate ID: `ANG-AUDIT-20260922-RLA01`. Paper394; 2026-09-22.
Outcome: NONZERO-CLOCK RATIONAL MULTIPLIER REQUIRES RATIONAL LINE — CONDITIONAL FILTER / FORK
Batch I, round5/5. CONDITIONAL THEOREM, not a new dynamical candidate.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

For an independently owned one-dimensional real return system with rational
fractional-linear inverse branches and its actual derivative clock, a nonzero
primitive cycle has rational exponential time if and only if its projective
fixed line is rational. The restriction permits arbitrary nonzero integer
determinants, not merely unimodular branches. Thus an irrational-only carrier
in this exact class cannot supply prime logarithmic primitive times. This is
an elementary follow-up to387, not a novelty claim or a restriction on other
clocks, nonlinear branches or higher-dimensional projective volume. Three
separate local-germ controls exhibit a rational positive clock, an irrational
positive clock and a finite-order zero clock; all stabilizers are retained.

## 1. Same-object contract and question

The [frozen card](candidate-card.md) quantifies over ONE separately fixed full
deterministic, possibly partial, real map T on X. Every actual inverse branch
is f_A(x)=(a x+b)/(c x+d), A integral nonsingular, with fixed primitive matrix
and sign. Products are the exact ordered products, without content reduction.
All valid incoming, terminal and null points are kept; no pole is in a branch
domain. The actual metric derivative and its all-point cocycle are assumptions
already owned by the input system, NOT constructions of this conditional audit.

| Field | Exact scope |
| --- | --- |
| Carrier/map | Whole fixed X/T; this paper supplies no new X |
| Clock | Negative log absolute inverse derivative, no rescale |
| Arrows | Actual common-tail triples with retained lag |
| Time | Full real-height extension and height translations |
| Arithmetic lineage | Conditional filter on divisor-symbolic fractional geometry; application-specific mechanism still required |
| Symplectic/roof/operator | NOT APPLICABLE / no positive roof asserted / NOT AUDITED |

Question: can allowing nonunit determinants by itself make an irrational
periodic point acquire a positive time whose exponential is rational?
The scope is a restriction on a proved input owner, not proof that such an
owner exists, a new prime-only map or a result inherited by all geometry.

## 2. Actual arrows, kernels, incoming and physical time

Let a(x) be the log absolute forward derivative and
A_m(x)=sum_(j<m)a(T^j x), defined only for valid iterates, A_0=0.
Then G={(z,m-n,w):T^m z=T^n w} and c=A_m(z)-A_n(w).
Two representations of a triple differ by adding the same number of steps
on a common tail, so the added sums cancel. Refining two composable histories
to common tails proves additivity. For an inverse prefix this is precisely
minus its log derivative by the chain rule. No separate measured clock is used.

The complete kernels, for ALL actual arrows, are

    K={g=(z,m-n,w): A_m(z)=A_n(w)},
    M={g=(z,0,w): T^m z=T^m w for some m},
    K intersect M={same-depth coalescence with equal derivative sums}.

These are generally different: equal-depth coalescence does not force equal
derivatives, and zero clock need not imply zero lag. No finer universal list
exists without specifying T; these formulas define the entire sets exactly.

If z is eventually periodic with least FULL source cycle q, its isotropy is
qZ. Indeed a nonzero equality T^m z=T^n z is exactly eventual periodicity;
the least eventual period divides every such difference and supplies all its
multiples. If it has no eventual period (including finite terminal histories),
source isotropy is trivial. For a periodic core x with cycle sum C=A_q(x),
the closed prefix into x cancels with its inverse, so at every incoming z

    c(kq)=kC; H_z=C Z;
    extension isotropy=0 if C!=0, and qZ if C=0.

For C!=0 the least positive physical time is L=|C|, not q|C| or a selected
positive word's time. A source orbit gives one translation orbit with phases
R/H_z; all incoming histories and heights remain. Distinct source orbits are
not identified by equal C. For nonperiodic source orbits H=0 and there is no
positive return; the clock is defined, so this is not NOT DEFINED.

## 3. Cycle algebra, including both signs

At a finite periodic core x, let A=[[a,b],[c,d]] be its exact inverse cycle
matrix, D=det A, t=tr A, and lambda=cx+d. The fixed equation gives
A(x,1)=lambda(x,1), lambda!=0. Direct differentiation yields

    f_A'(x)=D/lambda^2,
    C=log(lambda^2/|D|), R=exp(C)=lambda^2/|D|,
    lambda^2-t lambda+D=0.                                  (1)

Assume C!=0. If exp(L) is rational, R is that number or its reciprocal, hence
lambda^2 is rational. If t=0, (1) gives lambda^2=-D, so D<0 and R=1,
contradicting C!=0. Thus t!=0 and lambda=(lambda^2+D)/t is rational.
For c!=0 this forces x=(lambda-d)/c rational. If c=0 and x is irrational,
the fixed equation (d-a)x=b forces a=d,b=0: A is scalar, again C=0.
Therefore every such finite fixed x is rational.

Conversely, if x is rational, lambda=cx+d is nonzero rational, so R and
exp(|C|)=max(R,R^-1) are rational. The nonzero C hypothesis is indispensable.
This proves the equivalence, with no positivity assumption on signed C or D.

At an already admitted infinity point use y=1/x, NOT an added carrier point.
The condition f_A(infinity)=infinity is c=0. Its y-map is
(c+d y)/(a+b y), derivative D/a^2 at0. The fixed eigenvalue is a and
R=a^2/|D|=|a/d| is rational. Thus the same rational-projective-line statement
holds in its own local chart. Rational fractional-linear maps and inverses
preserve Q union {infinity}, so all legal incoming of a rational cycle also
lie on rational projective points (where present in the frozen carrier).

### Consequence for search

If the entire frozen finite carrier contains only irrational real points,
every positive primitive in this class has IRRATIONAL exp(L). Hence no such
primitive equals log p for an ordinary integer prime. Nonunit determinants
do not rescue this class. Zero-clock cycles, nonperiodic states and the absence
of any positive packet remain possible; none supplies all-prime coverage.
This is not a statement about rational-point carriers or all dynamical clocks.

## 4. Exact rational spectral boundary and zero cases

For coprime integers a>b>=1 with exp(L)=a/b, let s=sign D. Eliminating lambda
in (1), for either R=a/b or b/a, gives

    ab t^2=|D|(a+s b)^2.                                   (2)

Since gcd(ab,a+s b)=1, ab divides |D|. Write |D|=ab h; then
t^2=h(a+s b)^2. The rational number t/(a+s b) has integral square h,
so it is an integer k!=0 (reduce its fraction; a denominator would divide
its coprime numerator). Consequently

    D=sab k^2,       t=(a+s b)k.                           (3)

Conversely those spectral data factor the characteristic polynomial as
(lambda-ak)(lambda-sbk), and either real eigenline has exp(|C|)=a/b.
This is only a matrix/eigenline fact. It supplies no legal domain, least cycle,
intrinsic derivative on a proposed carrier, endogenous parameters, coverage
or packet multiplicity. The prime case a=p,b=1 specializes the387 condition.

If C=0, then lambda^2=|D|. For D>0, (1) forces t^2=4D; scalar products
are projective identity, whereas nonscalar parabolic products have a repeated
eigenline and derivative1. Nontrivial parabolic powers remain distinct germs.
For D<0, (1) forces t=0, and A^2=-D I by direct multiplication. The projective
map is a nonidentity involution, with derivative-1 at its real fixed lines.
These may be irrational and still have C=0. Germ order does not erase actual
lag labels of an input owner. Scalar products may fix arbitrary irrational
points with zero clock; they do not contradict the nonzero theorem.

## 5. Three independently calculated local-germ controls

These have the one fixed-point germ object and every integer power identified
ONLY when the germs agree. They are different owners from a hypothetical
point-lag return system. Finite powers may use different neighborhoods.

| Control | Own fixed point and derivative | Entire germ group / H / extension isotropy |
| --- | --- | --- |
| R: x/2 | 0; derivative1/2 | Z; (log2)Z; trivial |
| I: 2/(2+x) | sqrt3-1; derivative -(2-sqrt3) | Z; log(2+sqrt3)Z; trivial |
| Z: 2/x | sqrt2; derivative-1 | C2; H=0; all C2 |

For R every power has derivative2^-k, so different k give distinct germs,
clock k log2, and only the identity lies in the clock kernel. For I the fixed
equation x^2+2x-2=0 gives the stated positive root; its derivative has magnitude
2-sqrt3 strictly between0 and1. Powers again distinguish all k and give clock
k log(2+sqrt3). Each has one positive translation packet, all phases and the
ordinary multiples of its primitive time. These are LOCAL controls only.

For Z, f^2 is identity on a positive neighborhood but f is not identity,
so its whole germ group is C2 and its clock kernel is all of C2. The extension
has all C2 isotropy, while physical height translation has NO positive return.
In a separately hypothesized least-q point-lag cycle with this same return
germ, source isotropy is qZ, all qZ has zero clock, and the homomorphism to
germs has kernel2qZ. These three groups must not be conflated. R's assigned
coefficient2 is EXTERNAL, not an arithmetic mechanism; I/Z do not repair it.

## 6. Assessment, limits and next decision

T1/T2: a conditional necessary gate is established, not an evaluated new
owner. The same-object invariant is maintained by keeping input assumptions,
literal control germs and actual point-lag owners separate. Strong arithmetic
naturalness and application-specific lineage are not established by this audit.
PROVES_TOO_MUCH checks: R permits rational positive multipliers; Z permits
irrational zero-clock fixed points; higher-dimensional volume is outside the
one-dimensional proof. No finite numerical check or literature claim is used.

Portfolio FORK: do not continue an irrational-only rational-fractional source
with this derivative clock merely by changing determinants. A future proposal
must specify a genuinely different allowed owner/clock or rational periodic
carrier AND preserve its full arithmetic and multiplicity obligations.
This fifth round ends at the five-round handoff; no sixth round is authorized.

## Evidence and disclosure

Exact elementary differentiation, characteristic-polynomial arithmetic and
full-history arguments above are the methods; no scientific script, cutoff,
precision, prime list, fitted roof, zero data, PDF or external release exists.
See [card](candidate-card.md), [claims](claim-ledger.md), [overview](README.md),
[CP1](evidence/scope-review.md), [raw independent derivation](evidence/independent-proof.md)
and [final review](evidence/review.md).387 is a disclosed algebraic dependency
and motivation, not a donor of a missing owner or a novelty certificate.
AI-assisted authorship and separated card-only internal review follow ARS;
shared history is NOT_CALIBRATED, not blind, human or external peer review.
