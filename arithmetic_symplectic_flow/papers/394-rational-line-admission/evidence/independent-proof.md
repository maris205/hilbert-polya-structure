# 394 — Card-only rational-line admission proof

`ANG-AUDIT-20260922-RLA01`; batch I, round 5/5.
Conditional result: for a nonzero physical primitive of a legal projective
cycle, exp(L) is rational if and only if its fixed projective line is rational.
In particular an irrational-only real carrier cannot supply such a primitive.
The zero-clock exception is essential. No dynamical carrier is constructed.

## 1. Inputs, execution and precise ownership

- `candidate-card.md` — frozen 80 lines, read in full; SHA256 `329aec0ab00f3a69900024bccce2d8e60bc3393c78c11b6b2b5079b0d7756efd`.
- `scope-review.md` — frozen 69 lines; SHA256 `c39e825103a35a3fbb455de99a7b9c788325fef64315d6e129961fd5bc812450`.

Root explicitly released card-only mathematics after reading CP1. No current
manuscript, final surfaces, peer proof or other new scientific source was read.
The earlier 387 author/raw context is retained, not concealed; its files were
not reopened. This is an elementary follow-up, not a novelty or priority claim.
This AI agent supplies the derivation and self-check; shared-history internal
NOT_CALIBRATED, not blind/cross-model/external peer or human verification.
Inherited model settings are retained; served identity/effective reasoning are
not independently attested. No network, numerics, auxiliary agents or Git/PDF.

Fix ONE owner satisfying the card. Write T for its possibly partial map, and
I_z for its owned inverse branch taking Tz to z when that edge exists. Its
domain, actual derivative and compatibility with the assigned metric are input,
not inferred from a formula on an isolated set. Every legal intermediate point,
incoming branch and terminal is retained. No matrix word creates a legal edge.
All initial branch representatives stay fixed, and all cycle products below
are exact ordered products, never content-reduced or subsequently normalized.

## 2. Whole actual-lag groupoid and both global kernels

Set kappa(z)=-log|I_z'(Tz)| on valid edges and
S_m(z)=sum_(0<=i<m) kappa(T^i z) for a legal m-step history; S_0(z)=0.
Terminal points need no fictitious outgoing edge. Let

    G={(z,m-n,w): m,n>=0, both histories legal, T^m z=T^n w},
    ell(z,m-n,w)=m-n,       c(z,m-n,w)=S_m(z)-S_n(w).

The arrow is from w to z and is the triple, not its presentation or germ.
Two presentations of the same triple shift both exponents by the same integer.
For a nonnegative shift, their added sums start at the same meeting point and
cancel; interchange the presentations for a negative shift. Thus c is defined.
For composable (z,m-n,w) and (w,p-r,v), use j=max(n,p). Advance the first
meeting to T^j w and the second to that same point using their known legal
histories. The resulting outer exponents are m+j-n and r+j-p, respectively;
the two S_j(w) terms cancel. This proves closure, addition of ell and c, and
the required composition law. Inversion swaps endpoints and negates both.

The complete global clock and lag kernels, including non-isotropy arrows, are

    K=ker c={(z,m-n,w) in G: S_m(z)=S_n(w)},
    M=ker ell={(z,0,w): T^m z=T^m w for some legal m},
    K intersect M={(z,0,w): for some legal m,
                    T^m z=T^m w and S_m(z)=S_m(w)}.

These are exact exhaustive descriptions for the supplied owner, independent
of presentation; no extra arrows or selected prefixes replace them. A single
cycle matrix cannot enumerate zero-clock arrows between arbitrary different
points, and no further universal containment between K and M is assumed.
The full extension has arrows (w,h)->(z,h+c(g)) for every g:w->z and h in R.
Its isotropy over (z,h) is G_z^z intersect K, not the whole global K.
Since actual triples have no extra lag-zero labels, G_z^z intersect M={id_z}.

## 3. Entire H, repetitions, incoming and phase

If (z,k,z) exists with k!=0, an equality of two forward iterates exhibits an
eventually periodic tail. Let q be its least period. All equalities of iterates
have lag divisible by q, by minimality of that tail period; conversely, passing
into the tail realizes EVERY positive or negative multiple of q. Thus
G_z^z=qZ. Points without a periodic tail, including all terminal basins, have
trivial isotropy. Nonperiodic points that DO enter a cycle are in the former
case; they are not mistakenly put in the trivial case.

Let C be the sum of kappa along one least tail cycle. Transient sums cancel
between the two legs, and moving the cycle origin permutes its finite sum.
Consequently c(z,nq,z)=nC on the entire tail class, and

| Source class | Entire H_z | Clock kernel on isotropy / extension isotropy |
| --- | --- | --- |
| No periodic tail | {0} | trivial |
| Least tail q with C!=0 | C Z=abs(C) Z | trivial |
| Least tail q with C=0 | {0} | all q Z |

The lag kernel on isotropy, and the intersection of the two kernels there,
are trivial in all rows. In the last row source lag isotropy still equals qZ.
Zero clock is an admitted character, not an undefined clock or missing source.
When C!=0 the physical primitive is L=abs(C), and its repetitions are nL,
n>=1, within the same packet. The sign of C is NOT changed by a fitted roof.

For every incoming g:y->x, conjugation identifies the isotropy groups and
c(g a g^(-1))=c(a). Hence all the above groups are the entire groups throughout
the source orbit. To see every height phase, choose a transport g_z:z->x.
The invariant is h+c(g_z) modulo H_x. Different transports differ by isotropy
at x; equal phases give a connecting arrow after an isotropy correction.
Therefore the full height quotient over that source class is the SET R/H_x.
Translation has stabilizer H_x, all heights occur, and different source classes
are not merged merely because their periods agree. No smooth/Hausdorff quotient,
invariant measure or complete new carrier is deduced from this set calculation.

## 4. Exact cycle derivative, with either sign

Take a legal least cycle x_0,...,x_(q-1) and its inverse return
B=I_(x_0) o ... o I_(x_(q-1)), whose exact integral matrix is
A=A_0...A_(q-1)=[[a,b],[c,d]]. Put D=det A!=0, t=tr A and x=x_0 finite.
The legal composition fixes x and has no pole there. Direct calculation gives

    lambda=cx+d!=0,    A(x,1)^T=lambda(x,1)^T,
    lambda^2-t lambda+D=0,    nu=t-lambda=D/lambda,
    B'(x)=D/(cx+d)^2=nu/lambda,
    C=-log|B'(x)|=log|lambda/nu|.

The last equality is also the inverse-branch chain rule for the same sum C.
Both eigenvalues are real and nonzero, and sign(B')=sign D. Put r=nu/lambda.
If C!=0, then |r|!=1 and

    exp(L)=max(|r|,|r|^(-1))>1,        L=abs(C).

This includes both contraction C>0 and expansion C<0. A word that repeats the
least cycle does not change the primitive convention or create a new packet.

## 5. Rational multiplier forces a rational line

Assume C!=0 and exp(L) is rational. The preceding formula implies |r|, hence
r itself, is rational. Also r!=-1, since that would give |r|=1. Thus

    lambda=t/(1+r) is rational,       nu=r lambda is rational.

Here t cannot be zero: with nonzero lambda that would force r=-1.
A scalar matrix would have r=1, so A-lambda I is a nonzero singular rational
matrix of rank one. Its kernel is a rational projective line. Since it contains
(x,1), that line has rational finite coordinate x. Equivalently, if c!=0 then
x=(lambda-d)/c is rational; if c=0, the non-scalar finite fixed-point equation
(a-d)x+b=0 gives the same conclusion (a=d would leave only the scalar case
or no finite fixed point). This rules out all irrational finite x when C!=0.

For the reverse boundary, if a finite fixed point x is rational then
lambda=cx+d and nu=D/lambda are rational, so |r| is rational. Provided C!=0,
exp(L) is rational. This establishes the stated equivalence, conditional on
an ACTUAL legal cycle and its nonzero physical primitive; it establishes no
cycle from a rational line and no sufficiency for an arithmetic application.

A useful exact spectral description follows without a new owner. Rational
eigenvalues of an integral matrix are integers: a reduced rational root u/v
of the monic polynomial z^2-tz+D forces v to divide u^2, hence v=1.
Write exp(L)=a_0/b_0>1 in lowest positive terms, s=sign D. The eigenvalues
ordered by larger/smaller absolute value must be a_0 k and s b_0 k, with
nonzero integer k, since the coprime numerator and denominator divide the
respective integer eigenvalues. Therefore the exact product obeys

    t=(a_0+s b_0)k,       D=s a_0 b_0 k^2.

Conversely these equalities factor the characteristic polynomial into those
two distinct integer roots and give the same absolute spectral ratio. They
do not admit domains or least cycles. No product scaling or prime-dependent
coefficient choice is being substituted for the frozen branch representatives.

## 6. Rational projective boundary and infinity

The finite argument is naturally about lines in P^1(Q). Infinity is the line
(1,0), but it is not added to X. If an independently admitted local boundary
germ fixes infinity, c=0 and a,d!=0. In its coordinate u=1/x the same map is

    f_tilde(u)=(c+d u)/(a+b u)=d u/(a+b u),
    f_tilde'(0)=D/a^2=d/a,     C_infinity=log|a/d|.

Thus a nonzero clock there likewise has rational exp(abs(C_infinity)). The
fixed eigenvalue is a, not the finite-chart expression cx+d applied at infinity.
For any change of smooth local coordinate at a fixed point, the two coordinate
derivative factors cancel in the multiplier; this is not a change of clock.
The calculation is a separate boundary statement, not proof that infinity,
an orbit through it or its incoming branches belongs to the frozen real owner.

## 7. Zero clocks, trace zero and degenerate products

C=0 iff the real nonzero eigenvalues have equal absolute value. If D>0 they
are equal: t^2=4D, lambda=nu=t/2. The repeated eigenvalue is an integer.
A scalar A=lambda I gives the identity projective germ at every defined point,
including irrational points. Otherwise write A=lambda(I+N), N^2=0,N!=0.
Its powers represent I+nN for all integer n and are distinct for distinct n;
an equality up to scalar first forces that scalar to be 1, then (n-m)N=0.
This non-scalar parabolic has a rational fixed line, possibly infinity, and
fixed-point derivative +1. At infinity a=d with b!=0 gives precisely the
local form u/(1+(b/a)u); it is not an identity germ despite derivative 1.

If D<0, equal absolute eigenvalues are opposite: t=0 and nu=-lambda.
The identity A^2-tA+D I=0 gives A^2=-D I. Thus the projective germ at any
admitted real fixed point is a nontrivial involution, derivative -1, clock 0.
Its real fixed lines can be rational or irrational. Trace zero with D>0 has
no real nonzero eigenvalue and therefore no admitted real fixed point here.
These exhaust the zero-clock cases; a negative discriminant is not an extra
real cycle. For a nonscalar finite product the fixed-point equation
c x^2+(d-a)x-b=0 also shows that any irrational fixed point is quadratic;
scalar products are the case where that polynomial vanishes identically.

For any actual least cycle q in every zero-clock case, source isotropy and
extension isotropy are both qZ, even when the germ has finite order. A scalar
germ group is trivial, a parabolic germ group is Z and an involution germ group
is C2. These are different owners with the same zero physical H, not reasons
to discard actual point-lags. No positive primitive exists when H={0}.

## 8. The precise irrational-carrier admission filter

Contrapositive of §5: an irrational finite periodic point with C!=0 has
irrational exp(L). If a proposed separately fixed owner has X contained in
R minus Q, it therefore cannot supply a positive primitive with rational
exp(L), in particular no log p or log of any other rational number >1.
If it has only zero-clock or no-periodic-tail packets, that does not rescue the
target: those packets have no positive physical primitive.

More locally, every legal rational fractional-linear edge preserves rational
versus irrational type in both directions. One direction follows by substitution;
the inverse fractional-linear formula gives the other, since the actual finite
endpoints avoid the relevant poles. Hence the whole incoming class of an
irrational cycle remains irrational. This does not authorize deleting rational
points from an owner that originally included them, or treating rational source
classes of that owner as ruled out. The test also does not exclude nonlinear
branches, other coefficient fields, other owned clocks or finite rational cycles.
The actual derivative/clock, complete source and application lineage remain
assumptions/obligations; this algebra supplies none of their existence claims.

## 9. Control convention: full cyclic germs, not imported carriers

For each chosen local fixed-point germ g, use ONLY its entire cyclic germ group
Gamma=<g>, with all positive and negative powers identified by germ equality.
It is a one-basepoint groupoid; all its incoming arrows are exactly Gamma.
The character chi(g^n)=-log|(g^n)'| is well-defined by the chain rule. On all
real heights, h goes to h+chi(gamma); H=chi(Gamma), extension isotropy is
ker chi, and phase is R/H. No fractional roots, other basepoints or unlisted
branches are added. All powers have suitable local domains, not necessarily
one common interval for every integer power. No controls are pooled.

## 10. R — rational external nonzero clock

R(x)=x/2 has chosen fixed point 0, derivative 1/2 and powers R^n(x)=2^(-n)x
for all integers n. Distinct powers have distinct derivatives, so Gamma=Z.
Here chi(n)=n log2, H=(log2)Z, ker chi={e}, extension isotropy trivial;
all phases are R/(log2)Z and repeats of the primitive are n log2, n>=1.
The canonical integer-power lag on this faithful Z has trivial kernel.
A hypothetical actual least point cycle q instead labels its source by qZ;
its character nq->n log2 also has trivial kernel. No such global owner is
being asserted. The given coefficient 2 is EXTERNAL, not prime selection.

## 11. I — irrational nonzero clock

I(x)=2/(2+x) fixes alpha=-1+sqrt3>0; its other algebraic fixed point is
beta=-1-sqrt3. The frozen control is at alpha only, away from its pole -2.
With theta=2+sqrt3>1, lambda=1+sqrt3, nu=1-sqrt3, D=-2 and t=2,

    I'(alpha)=-2/(1+sqrt3)^2=-(2-sqrt3)=-theta^(-1),
    (I^n)'(alpha)=(-1)^n theta^(-n),       chi(n)=n log theta.

For an explicit all-powers description, use u(x)=(x-alpha)/(x-beta).
Direct substitution gives u(I(x))=-theta^(-1)u(x). Therefore with
r=-theta^(-1), the germ I^n is (alpha-r^n beta u(x))/(1-r^n u(x))
for every integer n; each denominator is nonzero near alpha. The use of beta
to express this coordinate does not add a second basepoint to the control.
Distinct derivative magnitudes prove Gamma=Z. Its H=(log theta)Z, clock and
canonical integer-power lag kernels are trivial, as is extension isotropy.
Phase is R/(log theta)Z and all repeats are n log theta. Theta is irrational,
consistent with the gate. Odd powers retain orientation reversal; negative
powers have negative clock and do not require replacing the clock by a roof.

## 12. Z — irrational zero-clock involution

Z(x)=2/x has chosen positive fixed point alpha=sqrt2, away from its pole 0.
At alpha its derivative is -2/alpha^2=-1; D=-2,t=0,lambda=sqrt2,nu=-sqrt2.
Direct composition gives Z^2=id. Thus even powers are the identity germ and
odd powers are Z, a nonidentity germ: the entire Gamma is C2, not Z.
Every power has clock 0; H={0}, ker chi=C2 and extension isotropy is C2 at
each height. Phase is R with free physical translation; no positive primitive
or positive repetition is supplied by this nontrivial zero-clock group.

An integer-valued lag sending the generator of C2 to 1 does NOT descend to
this germ group. The unreduced exponent presentation Z->C2 has kernel 2Z.
If a separately legal actual cycle has least period q and this inverse germ,
its point-lag isotropy is qZ, germ-representation kernel 2qZ, CLOCK kernel
all qZ, and actual lag kernel trivial. Its extension isotropy is qZ, not C2.
These kernels cannot be interchanged. Z explicitly refutes any attempted
version of the admission theorem that omits the nonzero-clock hypothesis.

## 13. Closure and remaining limits

The rational-line equivalence and irrational-only admission exclusion hold
with the full source/clock conventions, both signs and all stated degeneracies.
R demonstrates the rational-line boundary, I the irrational nonzero case and
Z the essential zero-clock exception, each within its own complete germ owner.
The right portfolio decision is a CONDITIONAL FILTER: stop rational-exponential
primitive promotion for irrational-only carriers satisfying these hypotheses,
not a universal no-go for projective dynamics or a new candidate construction.
No prime-only ledger, endogenous naturalness, nonlinear/other-field no-go,
spectral operator or Route credit follows. Classical NOT APPLICABLE;
T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED. This is round 5/5;
the authorized batch ends at its summary, with no sixth-round research here.
Only this raw was written; card and scope remain unchanged. Await separate
PAPER UNLOCK before any manuscript comparison or final-surface reading.
EOF — card-only raw complete; freeze after self-read and hash receipt.
