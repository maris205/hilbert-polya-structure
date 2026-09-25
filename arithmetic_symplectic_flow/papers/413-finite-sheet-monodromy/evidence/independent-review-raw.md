# FSM01 — independent card-only raw mathematics

Candidate: `ANG-AUDIT-20260923-FSM01`; date 2026-09-23.
Reviewer: `/root/nonlocal_source_review`; batch `NONLINEAR-LIFT-20260923-M`.
Input: complete candidate-card.md, 88 lines, SHA256 a3fcaecf9fcaab1f2c7052346ac0aab015adf1cd78ccc678f3de725d49e9e8bb.
CP1: scope-review.md, 91 lines, SHA256 271029f1febd4309840be1aede7726b37065e6eaa9d2d9bbdaa862f00ce8d093.
Root reported a full CP1 read and separately released this raw derivation.
The card was reread fully and its hash verified before the derivation.
No author manuscript, README, ledger, helper answer, peer or sibling output
was read. Shared prior history and the card's disclosed design expectations
remain: this is NOT_CALIBRATED, not blind/cross-model/human/external review.
AI supplies the derivation and checking. No external source, scientific code,
numerical search, Git action, operator, PDF or publication is used.

## 1. Full inverse IMAGE owner and the prescribed version

Write S={1,...,d}. The legal extension domain is D times S; all of
(X minus D) times S remains terminal. For a parent piece P_i and pi in S_d set
A_(i,pi)={y in T(P_i): sigma(I_i y)=pi}. This is Borel by the frozen maps.
The refined forward branch is

    (P_i intersect sigma^(-1){pi}) times {j}
       -> A_(i,pi) times {pi j},     (x,j) -> (Tx,pi j).

It is a Borel bijection, with actual inverse
I_(i,pi,j)(y,pi j)=(I_i y,j). For a Borel E in that target sheet, write E_0
for its base projection. Counting measure gives

    nu(I_(i,pi,j) E)=mu(I_i E_0)=integral_(E_0) q_i(y) dmu(y).

Thus the prescribed extension IMAGE version is exactly q_i(y) at EVERY
actual target, finite and positive. There is no factor d or 1/d: one target
sheet has one source sheet in this branch. These pieces form a countable
disjoint partition of the whole legal domain. The resulting point clock is

    kappa_F(x,j)=-log q_i(Tx)=kappa(x),  x in P_i.

The IMAGE identity alone would not determine null-point values; their exact
ownership here comes from the card's separate all-point version prescription.
No invariant probability or canonical choice among other versions is claimed.
For each parent predecessor x of y and each target sheet k there is exactly
one predecessor (x,sigma(x)^(-1)k). None is dropped, even when y is terminal.
Summing the disjoint inverse images in source pieces gives, for every Borel E,

    nu(F^(-1)E)=integral_E [sum_i 1_(T(P_i))(y) q_i(y)] dnu(y,k).

Each summand is read as zero off T(P_i), not as an inverse version there.
All integrands are nonnegative, so countable sums and infinite values are
allowed. This is a full preimage law, not a choice of a preferred predecessor.

## 2. All histories, cocycle descent and complete kernels

For every legal parent prefix define

    Sigma_0(x)=id,
    Sigma_m(x)=sigma(T^(m-1)x)...sigma(x),
    K_0(x)=0,  K_m(x)=sum_(r=0)^(m-1) kappa(T^r x).

Induction gives F^m(x,j)=(T^m x,Sigma_m(x)j) and S_m(x,j)=K_m(x).
For any legal depth-m predecessor x of y and target sheet k, its unique
depth-m source sheet is Sigma_m(x)^(-1)k. This describes every inverse history.
Composing the branch IMAGE identities gives the inverse-history version
product_(r=0)^(m-1) q_(i_r)(T^(r+1)x)=exp(-K_m(x)) on its actual domain.
The formula remains all-point by the fixed branch versions; nonexistent
steps at a terminal are never appended.

For z=(x,j), w=(y,k), the full G consists exactly of triples (z,m-n,w) with

    T^m x=T^n y,   Sigma_m(x)j=Sigma_n(y)k,

where both prefixes are legal. Its clock is c=K_m(x)-K_n(y).
If two witnesses have the same lag, their exponents differ by common padding.
The longer witness certifies legal continuation of the common endpoint, and
the identical added sum cancels. This proves descent for the partial map.
For composable witnesses (m,n) and (p,r), align n,p by padding the shorter
middle prefix up to max(n,p). Its legality is certified by the longer one.
The aligned middle sums cancel, proving additivity. Reversing a triple negates
lag and c; a forward arrow z -> Fz has lag -1 and clock -kappa_F(z).

The complete kernels, always subject to those actual common-tail conditions,
are: clock kernel K_m(x)=K_n(y); lag kernel m=n; intersection both conditions.
They need not be units for a noninjective parent. No germ quotient, sheet
selection or suppression of equal-length mergers has been taken. Empty
prefixes retain every unit, including each terminal-sheet unit.

## 3. Source isotropy, full H and all physical phases

In any deterministic partial map, nonzero source isotropy means
F^m z=F^n z with m>n, hence an eventual periodic orbit. Conversely if z
eventually lands on a least-Q cycle, equal-tail loops have exactly lags QZ:
after landing, all such lags are realized; any loop can be padded onto the
cycle and its lag must be divisible by Q. Let D be that cycle's signed sum.
Preperiod clocks cancel and cyclic changes of core phase leave D unchanged.
Thus, on its ENTIRE finite common-tail saturation,

    Iso_G(z)=QZ,   c(z,rQ,z)=rD,   H_z=DZ,
    Iso_extension(z,h)={rQ:rD=0},  for every real h.

If D is nonzero, extension isotropy is trivial, the least positive physical
period is |D| and repetitions are k|D|. If D=0, source/extension isotropy
are both QZ but H={0}: there is NO positive period. Negative D is retained.
All other sources, including every terminating history, have trivial source
and extension isotropy and H={0}. A terminal step clock is undefined, not zero.

For any source orbit O fix z_* in O. For z in O choose an actual arrow
g_z:z -> z_* and write b_*(z)=c(g_z). Its complete height coordinate is
h+b_*(z) modulo H_(z_*). Changing g_z changes this by a loop clock in H,
and every such change is available. Hence the full extension orbit SET over
O is R/H, with physical time acting by translation. This proves that the
ENTIRE source orbit, not a selected history, supplies one physical orbit.
It is a positive packet only when H has a positive generator. For H={0}
it is a free physical R. No Borel transversal or quotient manifold is needed
for this set-level statement. Different source orbits are not merged by time.

## 4. Full monodromy theorem and all incoming

Fix a parent least-q cycle gamma=(x_0,...,x_(q-1)); let
P_t=Sigma_t(x_0), 0<=t<=q, and Pi=P_q in precisely the frozen order.
Let its COMPLETE permutation decomposition consist of cycles O_alpha of
lengths ell_alpha, with every cycle included, sum_alpha ell_alpha=d.
Choose j_alpha in O_alpha merely as a coordinate origin. The corresponding
lifted core consists of all

    z_(rq+t)=(x_t,P_t Pi^r j_alpha),
    0<=r<ell_alpha, 0<=t<q.

Iteration gives this displayed sequence and closes it after q ell_alpha.
A return must be a multiple of q since the parent cycle is least-q. At x_0
it then requires Pi^r j_alpha=j_alpha, whose least positive r is ell_alpha.
Therefore the lifted LEAST period is Q_alpha=q ell_alpha. Distinct alpha
give disjoint cycles; together they contain ALL qd points over gamma.
If C_gamma=sum_(t=0)^(q-1) kappa(x_t), the lifted signed sum is
D_alpha=ell_alpha C_gamma, since the step clock is sheet-independent.

Let B_gamma be all parent points that land on gamma after finitely many
legal steps. Every point of B_gamma times S lands on one of the displayed
lifted cycles and is eventually periodic. Its full lifted saturation B_alpha
is the union of ALL legal inverse histories landing on that lifted core.
For an explicit membership test, if T^a x=x_t, then (x,j) belongs to B_alpha
exactly when P_t^(-1) Sigma_a(x)j belongs to O_alpha. Different landing times
change the reference sheet only by powers of Pi, so membership is unchanged.
The test is a permutation of all d sheets: each x in B_gamma has exactly
ell_alpha sheets in B_alpha, and the B_alpha partition B_gamma times S.
They are disjoint complete source orbits; a shared history would eventually
have two different periodic cores, impossible for deterministic iteration.
Every inverse branch, including its uniquely transported sheet, is present.

Consequently each alpha gives exactly one physical R/(ell_alpha C_gamma Z),
with source isotropy q ell_alpha Z and the extension isotropy of Section 3.
For C_gamma nonzero there is one positive packet per permutation cycle,
primitive ell_alpha |C_gamma|, multiplier exp(ell_alpha |C_gamma|), and
repetitions k ell_alpha |C_gamma|. Repeated permutation-cycle lengths produce
different equal-time packets; they are not identified. For C_gamma=0 all
these source orbits retain isotropy but yield free physical R orbits instead.

At reference phase x_t the monodromy Pi_t satisfies Pi_t P_t=P_t Pi:
both sides are the permutation of the same length q+t history, grouped in
the two possible ways. Thus Pi_t=P_t Pi P_t^(-1). Its entire decomposition
is transported bijectively, and C_gamma is unchanged by cyclic summation.
Least periods, signed sums, multiplicities and H are reference-independent.
Choosing another j_alpha in the same cycle only shifts a coordinate origin.

Finally, a periodic F point projects to a periodic T point, and an eventual
F cycle projects to an eventual T cycle. Conversely every lift of an eventual
T cycle is eventual periodic because Pi is a permutation of a finite set.
This exhausts all periodic/eventual sources. Every remaining source has the
nonperiodic or terminating ledger of Sections 2–3; it cannot hide a positive H.

## 5. Explicit full-saturation lags, kernels and phase coordinates

These formulas refine Section 3 without excluding incoming or zero clocks.
For one lifted core write z_t=F^t z_0, least length Q and signed sum D.
Let A_t=S_t(z_0) and extend t to all integers by A_(t+Q)=A_t+D.
Set beta=D/Q and V_t=A_t-t beta, which is Q-periodic. For any incoming z
and any landing F^a z=z_t define

    eta(z)=t-a modulo Q,
    b(z)=S_a(z)-a beta-V_t.

Both are independent of landing choice: advancing r core steps adds
A_(t+r)-A_t to S_a, and V_(t+r)-V_t equals that increment minus r beta.
Different landing times can be compared by advancing the earlier one.
For sufficiently large m, F^m z=z_(eta(z)+m) and
S_m(z)=b(z)+m beta+V_(eta(z)+m), with core indices read modulo Q.
Hence between any two points z,w of this full saturation the allowed lags
are EXACTLY r=eta(w)-eta(z) modulo Q. Necessity follows from the core phases;
sufficiency follows by choosing both witnesses sufficiently large with that
lag. For every such actual arrow,

    c(z,r,w)=b(z)-b(w)+r beta.

Thus the full clock kernel imposes that expression zero; the lag kernel has
r=0 and equal eta; their intersection additionally has b(z)=b(w).
All heights have phase

    Phi(z,h)=h-b(z)+eta(z) beta modulo DZ.

Changing an integer representative of eta changes this by a multiple of D.
Arrow invariance follows because r+eta(z)-eta(w) is divisible by Q.
Equivalently Phi=h-S_a(z)+A_t modulo DZ, so it includes every incoming.
For D=0 take beta=0 and modulo {0}; this is an exact real coordinate, not
a circle or a zero-length primitive. Loops still have lag QZ and zero clock.
Interphase arrows need not be loops and cannot enlarge H using their clocks.

## 6. Rational-target obstruction and exact boundaries

Elementary arithmetic lemma: if M>1 is rational, ell>=1 an integer and
M^ell=p is an ordinary integer prime, then ell=1 and M=p.
Indeed write M=a/b in lowest positive terms. From a^ell=p b^ell,
coprimality forces b=1. For integer a>=2, a^ell is composite if ell>=2.
This proof uses neither a prime table nor a fitted multiplier.

Suppose d>=2 and the card's rational hypothesis holds for EACH nonzero-clock
parent cycle. If there is no such cycle, Section 4 proves that the positive
lifted ledger is empty, so the nonempty part of the target fails. This covers
absence of all parent cycles as well as the case where every cycle has C=0.
Otherwise choose any nonzero-clock parent cycle gamma and retain EVERY
monodromy cycle. Its primitive multipliers are M_gamma^(ell_alpha).
If any fails to be an ordinary prime, prime-only already fails. If all are
prime, the lemma forces every ell_alpha=1 and M_gamma to be that same prime.
There are then exactly d>=2 different packets at log M_gamma, violating
uniqueness. Other parent cycles cannot remove these packets or this failure.

Therefore NO full finite-sheet extension with d>=2 under this rational
hypothesis satisfies the entire stated necessary target. Negative parent
clock is covered by abs(C); zero clock is not falsely treated as positive.
This is a conditional obstruction, not a statement about every finite lift,
every arithmetic source, a selected sheet, or a changed clock/measure version.

For d=1 the only permutation is identity and the owner identifies exactly
with the parent, including its packets, clock, kernels and H. No new universal
obstruction is obtained; the parent may or may not satisfy the target.
The proof's arithmetic lemma does not apply to irrational M. Control C below
shows why that hypothesis cannot simply be deleted. No global theorem about
all irrational parents is inferred. All-prime coverage and strong naturalness
remain different obligations even when these necessary conditions hold.

## 7. Three controls: independent full IMAGE laws and global ledgers

For EACH listed pair (a,pi), keep full R times {1,2} with its own Lebesgue
times counting measure. The map is a global Borel bijection with inverse
I(y,k)=(y/a,pi^(-1)k). Real one-dimensional change of variables gives
nu(I E)=a^(-1)nu(E) for EVERY Borel E; the point version is the inverse
derivative 1/a everywhere, including 0. Counting sheets adds no factor 2.
Thus A owns density 1/2 and clock log2; B separately owns density 1/2 and
clock log2; C owns density 1/sqrt(2) and clock log(sqrt(2)). These are real
line Jacobians, not complex area Jacobians or clocks borrowed across controls.

Put b=log a for the applicable control. Its complete groupoid is

    ((a^(-r)x,pi^(-r)j), r, (x,j)),  x in R, j in {1,2}, r in Z,
    c=r b.

Indeed global invertibility reduces every equal-tail witness to F^r z=w,
and every integer r is realized. Since b>0, clock kernel, lag kernel and
their intersection are all units. This does not contradict the nontrivial
source isotropy at periodic points: those loops have nonzero clock.
No terminals exist in these total controls and every point has one actual
predecessor, with all integer forward and inverse histories retained.

For every a in the card, a>1. A periodic point must satisfy a^n x=x for some
n>0, hence x=0. A point with x nonzero can never reach 0 and is not eventual
periodic. At x=0 the source periods are precisely the cycle lengths of pi;
there are no incoming points from x nonzero. This exhausts the periodic and
eventual ledger, not merely a finite-period search.

The entire nonzero ledger also has explicit coordinates. Uniquely write
x=epsilon a^n u with epsilon in {+1,-1}, 1<=u<a and n in Z. Set
rho=pi^(-n)j. For each (epsilon,u,rho) the FULL source orbit is

    {(epsilon a^m u,pi^m rho):m in Z}.

These are distinct and exhaust all x nonzero. Each has trivial source and
extension isotropy, H={0}, all physical real phases Phi=h+n b, and no
positive primitive or repetitions. The coordinate is invariant under the
extension arrow (x,j,h)->(ax,pi j,h-b). The radial interval labels orbits;
it is not a restriction of the carrier or deletion of their other points.

### A: a=2, pi=identity

The two origin points (0,1) and (0,2) are distinct fixed cycles and source
orbits, each with source isotropy Z, extension isotropy {0}, full H=(log2)Z,
phase h modulo log2, primitive log2 and repetitions k log2. Together they
give TWO different log2 packets. There are no other positive packets.
The nonzero orbits above have rho=j, b=log2 and u in [1,2); both sheet
families remain, each with the full free physical R and all kernels as above.
The parent has rational M=2. A satisfies prime-only/nonempty but fails
uniqueness. Its d=1 parent has just the one origin packet, illustrating the
d=1 boundary without giving it an arithmetic-origin or all-prime claim.

### B: a=2, pi=(12)

The two origin points form ONE least-two cycle and ONE source orbit, not
two packets. At either phase, source isotropy is 2Z, extension isotropy {0},
and full H=2 log2 Z=(log4)Z. Primitive time is log4, with repetitions k log4.
Writing eta(1)=0, eta(2)=1, its complete phase is h+eta(j)log2 modulo log4.
Odd-lag arrows connect the two phases. In particular, a lag-one arrow has
clock log2 but is not a loop and does not supply a physical return period.
There are no additional incoming or positive packets. For every nonzero x
the global orbit formula applies with rho=(12)^(-n)j, b=log2 and u in [1,2).
The parent again has rational M=2. B avoids duplicate origin packets by
combining sheets, but its primitive multiplier 4 is composite: prime-only
fails. The step clock cannot be substituted for the primitive full H.

### C: a=sqrt(2), pi=(12), NONRATIONAL PARENT COMPARATOR

Its own step clock is b=log(sqrt(2))=(log2)/2. The complete origin ledger
is ONE least-two source cycle/packet with source isotropy 2Z, extension
isotropy {0}, full H=2bZ=(log2)Z, primitive log2 and repetitions k log2.
All origin phases have coordinate h+eta(j)b modulo log2. The two source
phases do not give two packets, and their one-step arrows do not shrink H.
All nonzero source orbits are exactly the displayed (epsilon,u,rho) families
with u in [1,sqrt(2)), rho=(12)^(-n)j, phase h+n b and H={0}.
This exhausts all points, inverse histories, kernels and physical orbits.

The parent has its one fixed point 0 with M=sqrt(2), which is not rational:
in a reduced equality sqrt(2)=a/b, a^2=2b^2 makes both a and b even.
Consequently C is outside the rational premise and is not a counterexample
to the conditional theorem. It DOES meet the stated nonempty prime-only
and uniqueness conditions, with only prime 2 covered. This refutes deleting
the rational hypothesis, not supplies all-prime coverage or a natural source.
Its coefficient is explicitly prescribed by the frozen external control;
no endogenous prime generation or candidate admission follows.

## 8. Bounded conclusions and release boundary

The stipulated all-point parent version extends to the full counting-sheet
owner without an added roof or sheet factor. The monodromy theorem retains
every permutation cycle, every incoming history, all real heights, signed
and zero clock, kernels, source/extension isotropy and full H. The rational
d>=2 necessary-target obstruction is proved, including the empty-ledger case.
All three controls have separately owned IMAGE laws and complete ledgers.

This is a conditional filter on finite symbolic memory/admissibility ->
geometric realization; it constructs no missing prime-symbolic parent.
Portfolio: STOP the target for the stated rational full-sheet class; retain
the structural theorem and irrational comparator as scoped FORK information.
Controls remain EXTERNAL. Strong naturalness and PROVES_TOO_MUCH are not
resolved. Classical fields NOT APPLICABLE; T3 NOT AUDITED; formal Route
UNASSIGNED; Route B NOT INVOKED. No external novelty or global no-go is claimed.

Raw ends here. After full self-read and hash freeze, HOLD for root's complete
read and separate PAPER UNLOCK. This raw grants no manuscript access or round415.
