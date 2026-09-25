# 399 — Card-only full-torus packet gate

`ANG-AUDIT-20260922-FTG01`; batch J, round 5/5.
Conditional conclusion: every existing primitive base cycle with Q>1 fails
at least one of the two frozen necessary packet conditions on its FULL fibre.
No expansiveness is needed. Q=1 gives zero return clock, not missing isotropy.
This is a passive-linear-fibre filter, not a new arithmetic candidate.

## 1. Exact inputs, disclosure and ownership

- candidate-card.md SHA256 5852176dc65b6378d006e7d3697501398a846064bc0a326880cc16e047e664d8 — frozen 71 lines, read through EOF.
- scope-review.md SHA256 7d61b5707880383f178bd5ef4a5341f492ea0b67b08ff9f9884418bf9538b46e — frozen 74 lines.

Root read CP1 and explicitly released card-only mathematics. No manuscript,
final author surface, peer proof, 392 output or other new scientific source was
read. Earlier shared history is retained; this AI derivation and self-review
are NOT_CALIBRATED, not blind/cross-model/human/external verification. Model
settings are inherited; served identity/effective reasoning are not attested.
No scientific numerical search, network, auxiliary agent, Git or PDF was used.
Elementary exact arguments below supply their own evidence; no novelty claim.

Fix ONE X,T,A,n as in the card. Let E be the nonterminal base domain,
Y=X times T^n and D(x)=abs(det A(x))>=1 on E. No fibre point is removed.
The base permission is unchanged by the fibre. Haar probability m_n on T^n
means ordinary Lebesgue measure on the half-open cube [0,1)^n modulo Z^n.
No measure on X, probability on Y, smooth total space or positive roof is assumed.

## 2. Every inverse sheet and every Borel fibre IMAGE

For a nonsingular integer matrix C, put d=abs(det C). The quotient
Z^n/C Z^n has exactly d elements. Indeed det(C) Z^n is contained in C Z^n
by the adjugate identity, so the index is finite. A union of unit cubes over
coset representatives is a fundamental domain of C Z^n, as is C[0,1)^n;
their volumes give index=abs(det C). Choose representatives j_1,...,j_d once.
For u in the canonical half-open cube, define all inverse sections

    s_j(u)=C^(-1)(u+j) modulo Z^n.

They are distinct for different cosets. Any solution Cv=u modulo Z^n is of
this form, because its integer discrepancy has exactly one such coset. Thus
there are precisely d preimages at EVERY u, including boundary representatives.
Each section is injective and Borel. Its range S_j can be described explicitly:
for canonical v in [0,1)^n, the integer floor(Cv) lies in j+C Z^n.
These Borel S_j partition the whole torus, without duplicated boundary points.

On finitely many pieces each s_j is affine with linear part C^(-1), followed
by an integer translation back to the cube. Change of variables gives, for
EVERY Borel B in T^n,

    m_n(s_j(B))=d^(-1)m_n(B).

The finitely many cut boundaries have zero measure and are retained in the
half-open partition. A chosen Borel section can jump across a cut; its IMAGE
law is not a claim that this global section is differentiable there. The smooth
torus covering has a local inverse germ at EVERY point, with volume Jacobian
1/d. The clock is owned by that covering's global Jacobian, not by a fictitious
derivative of a discontinuous choice of representatives.
Equivalently, for every Borel H contained in one S_j,
m_n(C H)=d m_n(H). For arbitrary Borel H, define
N_H(u)=#(C^(-1){u} intersect H). The complete all-sheet statement is

    integral N_H(u) dm_n(u)=d m_n(H),
    m_n(C H)=integral 1_(N_H>=1) dm_n,
    m_n(C^(-1)(B))=sum_j m_n(s_j(B))=m_n(B).

The global forward IMAGE is a UNION, not the sum when sheets overlap.
In particular m_n(CH)=d m_n(H) is NOT asserted for arbitrary H; H=T^n
already refutes it when d>1. Haar preservation of full inverse preimages and
branchwise volume expansion d are compatible, not competing clocks.
The local volume Jacobian of C is abs(det C) at every point. Orientation
reversal or contracting directions do not change this full-volume formula.

For the variable owner, restrict each Borel base branch further by A(x)=C.
There are countably many integer C and finitely many fibre sheets for each.
The corresponding restrictions of F are injective Borel branches with explicit
Borel inverses (base inverse, then the displayed fibre section). Their union
is the complete actual inverse relation. No additional permission or sheet is
selected. D=1 means one torus-automorphism sheet and zero log-volume clock.

## 3. Composition, all-sheet transport and Borel owner

For a valid m-step base history define

    J_0(x)=I,  J_m(x)=A(T^(m-1)x)...A(Tx)A(x),
    d_m(x)=abs(det J_m(x))=product_(i<m)D(T^i x),
    F^m(x,v)=(T^m x,J_m(x)v),   S_m(x,v)=log d_m(x).

All products are exact and every d_m is a positive integer. Reversing a
history requires every inverse choice at every step. These choices give
exactly d_m distinct inverse points: a final inverse point determines all
its forward intermediates, so two different sheet histories cannot duplicate
it. Conversely every inverse point supplies that history. Their Borel sections
each have IMAGE factor d_m^(-1), by composition or the preceding matrix proof.
Thus the same volume factors, branch count and log clock compose exactly.

Consider two fixed legal base histories x,x' meeting at T^m x=T^l x'.
Parameterize a pair of fibre sheets by the common meeting variable u:
v=s_i^(m)(u), v'=s_j^(l)(u). This is the full arrow transport between those
sheets. For EVERY Borel H in its source sheet in the fibre over x',

    m_n(transport(H))=(d_l(x')/d_m(x)) m_n(H)=exp(-c) m_n(H),
    c=log d_m(x)-log d_l(x').

All sheet pairs are retained. This is a fibre IMAGE identity, not a claim
about a nonexistent base probability or a total-source Radon--Nikodym factor.
The Borel base branches, countable matrix values and explicit fibre partitions
make F a countable-to-one Borel partial map. All finite-iterate equality tests
and the following actual-triple groupoid are Borel; this does not make its
orbit quotient a smooth or standard-Borel space.

## 4. Actual groupoid, full global kernels and all heights

Write z=(x,v), w=(x',v'). The entire groupoid consists of triples

    g=(z,m-l,w),  m,l>=0, histories legal,
    T^m x=T^l x',   J_m(x)v=J_l(x')v' modulo Z^n.

It points from w to z, has lag ell(g)=m-l, and clock
c(g)=log d_m(x)-log d_l(x'). Equal triples are equal arrows, not extra words.
Changing a presentation adds the same tail to both legs, whose log factors
cancel. For composition, advance the shared point to the larger of its two
known iterate exponents; the necessary histories are already legal, and the
middle sums cancel. Hence composition adds lag and clock and inversion
negates both, even with partial histories or zero step clocks.

The exact global kernels, including arrows between different points, are

    K=ker c={g in G: d_m(x)=d_l(x')},
    M=ker ell={(z,0,w): F^m z=F^m w for some legal m},
    K intersect M={(z,0,w): for some legal m,
                   F^m z=F^m w and d_m(x)=d_m(x')}.

These are exhaustive descriptions, not just return kernels at a selected core.
Actual lag-zero isotropy is always the identity triple. Every unit and terminal
is present; terminal fibres require no fictitious extra forward iterates.
Use all Y times R with arrows (w,h)->(z,h+c(g)). Its isotropy at (z,h) is
G_z^z intersect K. Height translation by every real t preserves this relation
and descends to a complete SET action; no classical mapping torus is asserted.

## 5. Entire source isotropy, physical H and phases

A nonzero isotropy lag means F^m z=F^l z with m>l, precisely an eventual
periodic tail. If that tail has least FULL F-period q, all isotropy lags are
exactly qZ: every equality has difference divisible by q, and shifting into
the periodic tail realizes every positive and negative multiple. Without an
eventual periodic tail, including a terminal basin, source isotropy is trivial.
Let C be the sum of tau around the least tail cycle. Transient sums cancel,
so the whole character on isotropy is c(kq)=kC. Consequently

| Full source type | Entire H=c(G_z^z) | Extension isotropy |
| --- | --- | --- |
| No periodic tail | {0} | trivial |
| Least tail q, C>0 | C Z | trivial |
| Least tail q, C=0 | {0} | all q Z |

Here C>=0 because all D are positive integers. Negative return lags still
give negative clocks when C>0. The primitive positive physical time is C,
not qC; its repetitions are kC, k>=1, in the SAME packet. Zero clock is
defined and retains qZ, rather than being undefined or a positive period.
The lag kernel on isotropy, and its intersection with the clock kernel there,
are trivial because lag labels of actual triples are retained.

For any incoming g:y->z, conjugation identifies the entire isotropy and
preserves its clock. For each point y in this source orbit choose transport
g_y:y->z. The phase is h+c(g_y) modulo H_z; choices differ by H_z and equal
phases give a connecting arrow after an isotropy correction. The full phase
set is R/H_z, with translation stabilizer exactly H_z. All heights occur.
Different source orbits are never merged merely because their clock groups
coincide. This establishes the complete physical ledger for the supplied owner.

## 6. All monodromy periods and incoming fibres

Fix a primitive base cycle x_0,...,x_(ell-1), with
B=A(x_(ell-1))...A(x_0) and Q=abs(det B)>=1. The first return to the
fibre over x_0 is v->Bv. Its complete period predicates are

    Fix(B^r)={v in T^n:(B^r-I)v=0 modulo Z^n},
    Per_r(B)=Fix(B^r) minus union_(d|r,d<r)Fix(B^d),
    eventual periodic={v: (B^r-I)B^j v=0 for some j>=0,r>=1}.

No expanding assumption is used. If B^r-I is nonsingular, its fixed set has
abs(det(B^r-I)) points by the covering proof above. If it is singular, solving
its integer linear equations gives a nonzero rational nullvector, hence an integer vector;
its real multiples modulo Z^n give a circle of fixed points. This includes
all root-of-unity cases; the congruence predicates remain exact either way.

A least B-cycle of length r corresponds to one least F-cycle of length ell r:
any F-return must be a multiple of the least base period ell. Distinct B-cycles
give distinct F-cycles, including every base phase. Their entire clock and
source isotropy are

    source isotropy=(ell r)Z,   C=r log Q,   H=(r log Q)Z.

For Q>1 extension isotropy is trivial. For Q=1 it is the whole (ell r)Z,
and H={0}. Every factor D on a Q=1 cycle equals 1, but incoming prefixes may
have nonunit factors; they shift phases and do not create a return clock.

For ANY full F-cycle C_0, its entire incoming basin is exactly the union,
over (x_i,v_i) in C_0 and all s>=0, of

    {(y,u): T^s y=x_i is legal, J_s(y)u=v_i modulo Z^n}.

Each such fibre equation retains all d_s(y) solutions. More generally choose
any entrance of a base history into x_0: J_s(y)u must satisfy the eventual
periodic predicate above. If it does not, the full F-point is non-eventual,
even though its BASE is periodic. Bases with no periodic tail cannot produce
an eventual F-cycle. Thus no fibre, incoming history or null packet is omitted.

## 7. A finite decisive obstruction without expansiveness

The zero vector is B-fixed and yields a least ell-cycle, with primitive log Q
when Q>1. If Q is composite, this already violates the prime-log requirement.
It does not establish the prime-Q case, for which a second core is essential.

Suppose Q=p is prime. Set m=Q+1, without changing any parameter of the owner.
The FULL retained torus contains V_m=(m^(-1)Z^n)/Z^n, a finite group with
m^n>1 points. Since gcd(det B,m)=1, the adjugate formula gives an inverse
for B modulo m. Hence B permutes V_m, fixes zero and permutes its nonzero
points. Choose any nonzero v; it belongs to a finite B-cycle of least r>=1.
This uses no eigenvalue bound, period census, prime list or numerical search.

Its full F-cycle is different from the zero cycle. Two deterministic periodic
cycles sharing a forward meeting point are the same cycle; here their points
over x_0 cannot agree. Thus adjoining all actual incoming cannot merge these
two cores into one packet. Their clocks are computed from ENTIRE isotropy.

- If r=1, there are at least two distinct primitive packets of time log p:
  the zero cycle and this nonzero cycle. The multiplicity condition fails.
- If r>1, this packet has primitive r log p=log(p^r), the logarithm of a
  composite integer, not an ordinary prime. The prime-log condition fails.

This exhausts the finite witness. Unit factors, nonexpanding directions and
root-of-unity eigenvalues cannot evade it. V_m is used as a subset of test
points already in the full carrier, NOT as a replacement carrier or selected
surviving ledger. There is no claim that period two must suffice for general B.

For Q=1 the above monodromy ledger gives zero clock on every periodic packet,
while all source isotropy remains. If an entire application has no base cycle
with Q>1, it has no positive physical primitive at all: every F-cycle projects
to a base cycle. The two stated necessary conditions may then hold vacuously,
but that is not prime coverage or a positive arithmetic candidate.

## 8. D control — full doubling circle

D(x)=2x modulo1 on the FULL circle, with Haar m_1. For canonical u in [0,1),
the two inverse sections are u/2 and (u+1)/2, each IMAGE factor 1/2 for
every Borel set. All preimages preserve m_1; forward IMAGE uses the all-sheet
multiplicity formula, not a global factor2 identity. At depth s every inverse
is (u+j)/2^s, j=0,...,2^s-1. Derivative2 gives tau=log2 on every step.

Actual arrows satisfy 2^m x=2^l y modulo1, lag k=m-l and c=k log2.
Thus K=M=K intersect M, with their whole lag-zero relation explicitly

    {(x,0,y): x-y lies in Z[1/2]/Z}.

A point is eventually periodic iff it is rational modulo1. One implication
follows from (2^m-2^l)x integer for m>l. Conversely write a reduced rational
denominator b=2^s b_odd; after s doublings the denominator is odd, and 2 is
invertible on that finite residue group. Its least tail period is the least
q with 2^q=1 modulo b_odd, taking q=1 if b_odd=1. It is periodic already
iff s=0. Irrational points have no periodic tail and are all retained.

The complete periodic sets are Fix(D^q)={j/(2^q-1):0<=j<2^q-1}; least
q points are obtained by subtracting proper-divisor fixed sets. Cyclic D-orbits
of those points are the distinct primitive cores, and ALL their incoming are
the displayed depth-s inverse points of every point of the core. For rational
x, source isotropy=qZ, H=(q log2)Z, extension isotropy trivial and phase
R/(q log2)Z. For irrational x, all three isotropy/return groups are trivial
and phase is R, while its actual common-tail arrows remain. Every height and
every integer-lag arrow uses the same full extension h->h+k log2.

The fixed set is exactly {0}, giving primitive log2. The fixed set of D^2 is
{0,1/3,2/3}; {1/3,2/3} is one least-two core, giving primitive log4.
This is a composite-time packet, not a repetition of the distinct zero core.
The probe decides failure, while the symbolic formulas retain the whole owner.

## 9. U control — unit-volume full torus automorphism

U=[[2,1],[1,1]] has determinant1 and integer inverse [[1,-1],[-1,2]].
Thus it has exactly one inverse sheet on the full T^2. For every Borel H,
m_2(UH)=m_2(H)=m_2(U^(-1)H), and tau=log1=0 everywhere.
Its eigenvalues are (3+sqrt5)/2>1 and (3-sqrt5)/2 in (0,1), so U^q-I
is nonsingular for every q>=1. The exact periodic criterion is v in Q^2/Z^2:
if (U^q-I)v is integral, inverse rational coefficients force rational v;
conversely, U is a permutation modulo each denominator because det U=1.
Injectivity implies every eventually periodic point was periodic already.
No point with an irrational coordinate has periodic or eventual-periodic tail.

All fixed sets are (U^q-I)^(-1)Z^2/Z^2; subtract the proper-divisor sets
to obtain least q, then quotient by the U-cycle to obtain primitive cores.
Every valid inverse is U^(-s), with no off-cycle incoming into a periodic core.
The entire actual groupoid is {(U^(-k)w,k,w):k in Z}; period-related lag
labels are not collapsed. Its global K is G, M consists only of units by
injectivity, and K intersect M consists only of units. At a rational point
of least period q, source and extension isotropy are both qZ; elsewhere both
are trivial. H={0} at EVERY point. Each source orbit has real phase R and
free height translation, with all arrows keeping height unchanged. Unit volume
does not mean absent source periodicity; it means there is no positive clock.

## 10. A control — full affine irrational-rotation boundary

Write alpha=sqrt2. A(x,y)=(2x,y+alpha) modulo Z^2 on the FULL torus.
The derivative matrix is diag(2,1); hence tau=log2 from full area, not a
separately assigned roof. Its two inverse sheets are

    I_j(u,v)=((u+j)/2,v-alpha), j=0,1,

each with IMAGE factor 1/2 for every Borel set. Their union gives all inverse
points and preserves Haar probability. The forward global IMAGE again uses
multiplicity. At depth s all inverse sheets are ((u+j)/2^s,v-s alpha),
0<=j<2^s, and A^s(x,y)=(2^s x,y+s alpha). No boundary is discarded.

If A^m(x,y)=A^l(x,y) with m!=l, the second coordinate would give
(m-l)sqrt2 integer, impossible. Thus there are NO periodic or eventually
periodic points, not merely none in a selected section. All source isotropy,
H and extension isotropy are trivial, although the clock is everywhere defined.
The full actual arrows from (x',y') to (x,y) satisfy

    2^m x=2^l x' modulo1,   y-y'=-(m-l)alpha modulo1,
    k=m-l,                 c=k log2.

Therefore global K=M=K intersect M, explicitly all lag-zero arrows with
y=y' and x-x' in Z[1/2]/Z. These include nonidentity transport between
different points despite trivial isotropy. The displayed inverse formulas
retain all incoming, and the full extension changes h by k log2. Each source
orbit has phase R and free height translation, with no positive primitive.

This control changes the unshifted LINEAR hypothesis; its irrational affine
shift removes the fixed zero-fibre argument. It is not a counterexample to
the stated linear theorem. Absence of packets is no all-prime coverage and
no arithmetic mechanism. The control cannot be pooled with D or U.

## 11. Scoped closure and stop

The full passive linear-torus owner has been handled conditionally, including
all-sheet fibre IMAGE, actual arrows, both global kernels, their intersection,
all incoming, source/extension isotropy, entire H and every height phase.
The finite obstruction covers arbitrary nonzero integer monodromy determinants
without spectral expansion assumptions. It fails one frozen necessary condition
whenever Q>1, and preserves zero-clock source isotropy when Q=1.
The three controls own their full torus/Haar/clock/extensions separately.
No full-source probability, new endogenous base, feedback mechanism, nonlinear
or affine no-go, operator, naturalness, novelty or transferable Route claim follows.
Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.
Only this raw was written; card and CP1 stay frozen. This is round 5/5, with
no sixth-round authority. Await root's full read and a separate PAPER UNLOCK.
EOF — card-only raw complete; freeze after self-read and hash receipt.
