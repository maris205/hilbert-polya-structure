# MCR01 — isolated card-only raw derivation

Candidate ID: ANG-20260925-MCR01. Paper 476, batch
PRE-P0-STRUCTURE-20260925-Z, round 2/5.
Raw outcome: OWNED CF IMAGE; NONINTEGER FIXED PRIMITIVE — STOP / FORK.

## 1. Frozen input, exposure and method

The sole new scientific input is [candidate-card.md](../candidate-card.md),
original 105 lines, SHA-256
`7bc0a9f67479b8a5b1f51f2fa752d96d8269a176d0697238733f1ff8f7076a77`.
Its count/hash were rechecked after DISTINCT RAW RELEASE. The separate
[CP1 report](scope-review.md) has 84 lines, SHA-256
`75c9ccd381a4b531f99f1b62eab6b33d099b9be030fe6be1ef09a211e6fdb0a9`.
No current author/helper/peer/raw or historical proof file was opened for
this candidate. This reviewer nevertheless retains completed 474 work and
shared root history. The execution is same-model/shared-history AI,
NOT_CALIBRATED, not blind, human, external or error-independent. The
card's disclosed informal design calculations remain outcome-unsealed.

ARS router, deep workflow, runtime policy, DA and fallacy guidance and the
local governance were personally refreshed at CP1. This is an exact bounded
mathematical derivation, not a literature/submission pipeline. It uses
integer recurrences, interval coding, elementary change of variables and
actual-history arguments. No scientific numerics, code-length/depth cutoff,
external sources, network, Git, old edits, PDF or operator is used. Only
this raw file is writable here; paper access remains LOCKED until a later
distinct root unlock. No conclusion is borrowed from 474's different measure.

## 2. Continued-fraction coding proved on the entire source

Let X be all infinite positive-integer words, with its product topology and
Borel structure. For a positive digit a, H_a(t)=1/(a+t). For a finite word
w=(a_0,...,a_(m-1)), set H_w=H_(a_0) composed ... composed H_(a_(m-1)).
Use p_-1=1,p_0=0 and q_-1=0,q_0=1, and for j>=1 put

    p_j=a_(j-1)p_(j-1)+p_(j-2),
    q_j=a_(j-1)q_(j-1)+q_(j-2).

Direct induction on composition yields

    H_w(t)=(p_m+p_(m-1)t)/(q_m+q_(m-1)t),
    H'_w(t)=(-1)^m/(q_m+q_(m-1)t)^2.

The determinant identity follows from the same recurrence, starting with
H_a. Thus every H_w is a strictly monotone homeomorphism of [0,1] onto
an interval I_w of diameter

    1 / (q_m (q_m+q_(m-1))).

The positive-digit recurrence bounds q_m below by a Fibonacci sequence,
which tends to infinity. For an infinite word, the successive I_w are
nested and their diameters tend to zero; their intersection is one point.
Define pi to be that point, and define each suffix value t_j likewise.
Continuity of H_a gives t_j=1/(a_j+t_(j+1)). Each suffix is positive,
since t_j>=1/(a_j+1)>0; its successor is positive as well, so t_j<1.
In particular

    1/pi(x)=a_0+t_1, with 0<t_1<1.

The integer digit is therefore recovered by the floor, and the suffix by
the fractional part. A rational input p/q in (0,1), in lowest terms,
would have next numerator q-floor(q/p)p strictly below p unless it is
zero. Repeated positive rational remainders cannot continue indefinitely.
Consequently an infinite word's value is irrational.

Conversely, for an irrational u in (0,1), repeatedly apply
G(u)=1/u-floor(1/u). Each remainder stays irrational in (0,1) and gives a
positive digit. The original u belongs to every resulting I_w, so the
shrinking-interval construction recovers u. The floor recovery also proves
uniqueness. This proves pi is a bijection onto Y=(0,1) minus the rationals.
No finite continued-fraction endpoint is added as an object.

The diameter bound proves pi is continuous in the product topology. Its
inverse coordinates are successive floors along the Borel map G, hence
are Borel. Thus pi is a Borel isomorphism. For each finite w,
pi([w])=H_w(Y), the open interval between its rational endpoints with
rationals removed. In particular pi(w xi)=H_w(pi(xi)), for every tail,
not just almost every one. Unit strings, unbounded digits and periodic
words are all included in this construction.

## 3. Original probability and its own baseline shift relation

Define rho(u)=1/(log(2)(1+u)) on (0,1), and
mu(E)=integral_(pi(E)) rho(u) du for Borel E subset X. The Borel
isomorphism makes this a well-defined countably additive measure.
Its total mass is one, because integral_0^1 du/(1+u)=log 2 and the
rationals are Lebesgue-null. Every nonempty cylinder has positive mass:
its real interval has positive length and rho is positive there. Hence
mu has full support. Singletons have zero mass, so mu is nonatomic.
These properties use the frozen density, not a fitted returning-set law.

The baseline left shift sigma on X corresponds exactly to G on Y by
the coding identity above. Its inverse branches are H_a, a>=1. For every
t in Y,

    rho(H_a(t)) |H'_a(t)|
      = 1 / (log(2)(a+t)(a+t+1)).

Summing the telescoping series over all a gives rho(t). For any Borel
E subset Y, change variables on the disjoint inverse branches and use
nonnegative countable additivity to obtain

    integral_(G^-1 E) rho(u) du = integral_E rho(t) dt.

Therefore sigma preserves this original mu. This is an own proof of the
baseline relation, not an appeal to canonicality, and it does NOT assert
that any of the four rewrite maps preserves mu. In particular their
clocks must still be computed from their own actual inverses.

## 4. Complete parser, branch atlas and actual predecessors

Let D(a,b) mean 1<a<b and a divides b. Let E_infinity consist of words
whose EVERY adjacent pair satisfies D. It is Borel as a countable
intersection of coordinate conditions. M and Q have legal domain
X minus E_infinity. For finite first failure k>=1, their source word
U=(a_0,...,a_k) has D true at all earlier pairs and false at its last pair.
These source cylinders form a disjoint countable partition of that domain:
the parser's first failure is unique and does not depend on the unused tail.
A and R instead use their own full two-digit partition of all X.

Each permitted source U has exactly its output V from the frozen table.
On its WHOLE target cylinder [V], define I_U(V xi)=U xi. Prefix insertion
and removal are inverse homeomorphisms of these product cylinders. Hence
I_U is Borel, its image is the whole source cylinder, and both inverse
identities hold at every point. If Tz=y, the actual parser of z recovers
one of these U and the unchanged tail; thus z=I_U(y). Conversely each
listed inverse gives an actual predecessor. Target outgoing legality is
irrelevant to this inverse statement. No shorter parser can replace U.

An explicit all-label predecessor description is useful. Write a target
y=(b_0,b_1,...) and set

    S(y)={(d,n,b_1,b_2,...): d,n>=1, d+n=b_0, not D(d,n)}.

Then

    Pre_A(y)={(d,n,b_1,b_2,...):d,n>=1, d+n=b_0};
    Pre_R(y)=S(y) union
             {(d,d b_0,b_1,b_2,...):d>=2, b_0>=2}.

For M, add to S(y), for EVERY k>=2 and d>=2, the following possible word.
Require b_0,...,b_(k-2)>=2, put a_0=d and

    a_j=d product_(i=0)^(j-1) b_i,  1<=j<=k-1,

and require not D(a_(k-1),b_(k-1)). Include

    (a_0,...,a_(k-1), b_(k-1), b_k,b_(k+1),...).

The displayed requirements are exactly all the earlier successful pairs
and the final failure. This proves both sufficiency and exhaustion of
Pre_M(y), without any bound on k, d or target digits.

For Q the complete simplification is

    Pre_Q(y)=S(y) union
             {(d,b_0,b_1,...): D(d,b_0) and y not in E_infinity}.

Indeed an initial successful pair in the source is followed by precisely
the finite first failure of y. Conversely a Q quotient-branch source
retains that final failure when its first digit is dropped. Thus there
is no quotient-branch predecessor of an infinite-success target; S(y)
still supplies all permissible sum-branch predecessors of such a target.

These are sets of actual points, not labelled multiplicities. Countably
many finite source words cover all branches; overlaps between their target
cylinders are kept. The statements apply to every y in X. For example
the M/Q terminal (2,4,8,16,...) has the actual sum-branch predecessor
(1,1,4,8,16,...). A and R are total on both words and do not acquire
M/Q's terminal convention. A terminal retains units and incoming arrows,
but has no artificial outgoing self-loop.

## 5. Every-Borel original IMAGE, null version and clock

Fix any one permitted U,V pair of any owner. If E subset [V] is Borel,
there is a Borel tail set B subset X with E={V xi:xi in B}. Put C=pi(B).
Ordinary one-variable change of variables along the strictly monotone H
maps gives

    mu(I_U E) = (1/log2) integral_C |H'_U(t)|/(1+H_U(t)) dt,
    mu(E)     = (1/log2) integral_C |H'_V(t)|/(1+H_V(t)) dt.

Their density ratio is exactly the frozen value

    J_UV(V xi) = [(1+H_V(t))/(1+H_U(t))]
                  |H'_U(t)|/|H'_V(t)|,  t=pi(xi).

All H derivatives are nonzero and finite on (0,1), with positive
denominators in Section 2, and 1+H values are positive finite. Thus J is
positive finite at EVERY target point. Substituting the ratio proves
mu(I_U E)=integral_E J_UV dmu for EVERY Borel E, not merely whole-cylinder
totals. Its values on null periodic words are the prescribed geometric
version. The integral identity alone would determine them only a.e.;
no such uniqueness is asserted here.

Let u=pi(x), v=pi(Tx) on this source cylinder. The actual coordinate map
f=H_V composed H_U^-1 has |f'(u)|=|H'_V(t)|/|H'_U(t)|. Hence

    kappa(x) = -log J_UV(Tx)
             = log |f'(u)| + log(1+u)-log(1+v).

This is the owner's original signed clock. It is not a product-letter
mass ratio. The density contribution is an endpoint difference and
cancels on a genuine periodic itinerary; local variation alone therefore
does not prove noncancellation or an infinite-rank periodic clock group.
No positivity repair, reweighting or separately chosen roof is introduced.

Finite compositions again admit countably many prefix charts. Intersect
the target prefix cylinder with the next actual source prefix cylinder;
the intersection is empty or one prefix extends the other. In the latter
case refine by that finite extra prefix. Induction covers every finite
legal itinerary. The chosen derivatives compose at every point by the
chain rule and density cancellation, including at null words.

## 6. Full histories, pair IMAGE and exact global tests

Fix any one owner and use its own T, legal domains D_r and sums S_r,
with D_0=X and S_0=0. The full actual groupoid is

    G={(z,r-s,w):r,s>=0, T^r z=T^s w legally},

source w, range z, with identical triples identified and lag retained.
If two witnesses have the same lag, their exponents differ by a common
integer. Ordering them gives a common nonnegative extension; the longer
witness ensures it is legal. Its extra sums at the common endpoint cancel,
so c(z,r-s,w)=S_r(z)-S_s(w) is well defined. For composition, extend the
shorter middle-endpoint history to the longer legal one and cancel the
middle sums. This proves addition and reversal of c. No extension beyond
a terminal is used. In particular c(Tz,-1,z)=-kappa(z).

On every actual history-pair chart a=(T^r)^-1 composed T^s, from w to z,
Section 5 and its finite-iterate chain rule give, for every Borel E in
that chart's domain,

    mu(a E)=integral_E exp(S_s(w)-S_r(a w)) dmu(w)
           =integral_E exp(-c(a w,r-s,w)) dmu(w).

This is the original IMAGE, proved chartwise over the countable actual
atlas. It is not a sum over duplicate labels or a changed invariant law.
The descent argument also fixes the pointwise clock version on equal
triples, including null triples.

The full kernels, without a finite-depth restriction, are exactly

    K_lag={(z,0,w):exists legal r, T^r z=T^r w};
    K_clock={(z,r-s,w):T^r z=T^s w legally, S_r(z)=S_s(w)};
    K_joint={(z,0,w):exists legal r, T^r z=T^r w,
                                            S_r(z)=S_r(w)}.

These are exact existential tests for each owner's actual sums, not a
claim that a finite search decides every input. In particular no binary
product-measure control simplification is imported into this CF measure.

The full extension has arrows (w,h)->(z,h+c). It uses all X times R;
height translation acts on the orbit SET. The exact base-orbit test is
the common-iterate predicate above. The exact extended-orbit test adds
h_z-h_w=S_r(z)-S_s(w) for some legal witness. No regular quotient, section,
selected fibre or prime-labelled subset is assumed.

For all owners and all target sets C define P_0(C)=C and

    P_(j+1)(C)=union_(y in P_j(C)) Pre(y).

The exhaustive inverse identities prove by induction that this is exactly
the legal j-step predecessor set, at EVERY j. Thus the full incoming set
is union_(j>=0) P_j(C). Compatible infinite incoming histories are precisely
the sequences (x_0,x_-1,...) with x_0 in C and x_(-j-1) in Pre(x_-j) for
every j. This inverse-limit condition imposes compatibility, not merely
existence of unrelated vertices at different depths. Such histories are
retained, not adjoined as extra X states or duplicate arrows. It also
applies to terminals; no nonempty infinite history space is presumed.

## 7. Entire isotropy, H, all phases and repetition law

A nonzero isotropy lag at z implies T^(s+p)z=T^s z for some p>0, so z
eventually reaches an actual periodic core. Conversely any eventual core
supplies nonzero lags. If its least discrete period is p, every isotropy
lag is divisible by p, and every multiple is realized after sufficiently
many core traversals. Hence the ENTIRE source isotropy is pZ. If the
cycle sum is C, the common transient cancels and c(z,mp,z)=mC. Thus

    H_z=CZ,
    extension isotropy={mp:mC=0}.

If there is no eventual cycle, source and extension isotropy and H_z are
all trivial. At a terminal and throughout its incoming class there is no
eventual cycle. More explicitly, arrivals at a terminal have a unique
depth ell(z); every arrow within that class has lag ell(z)-ell(w) and
clock S_ell(z)(z)-S_ell(w)(w). Its phase at the terminal is
h-S_ell(z)(z), with no modular reduction and no positive period.

For a general source orbit choose an anchor b and an actual arrow b->z
of clock t_z at each z. All arrow clocks w->z are exactly
t_z-t_w+H_b: compose with anchor isotropy, and conversely compare two
such arrows. Therefore the orbit set above that entire source class is
parametrized by h-t_z modulo H_b. Physical translation adds its real
parameter, so its ENTIRE stabilizer is H_b. Each source orbit gives one
physical translation packet, with all phases retained. If C is nonzero,
its positive primitive is |C| and its positive repetitions are m|C|,
m>=1; if C=0 there is no positive primitive, while source and extension
isotropy pZ remain. Different source classes remain different packets
even if their clock values agree. No loop is selected to shrink H.

## 8. Complete fixed classification on the two whole cylinders

Let W_1=[2,4,4] and W_2=[2,4,8,3], with arbitrary infinite tails xi.
The actual first failure makes the M/Q parser stop after the displayed
prefix in each case. Directly applying each owner's frozen rule gives

| Owner | Image of (2,4,4,xi) | Image of (2,4,8,3,xi) |
| --- | --- | --- |
| M | (2,4,xi) | (2,2,3,xi) |
| A | (6,4,xi) | (6,8,3,xi) |
| Q | (4,4,xi) | (4,8,3,xi) |
| R | (2,4,xi) | (2,8,3,xi) |

A and Q have a first-digit mismatch on both cylinders. M and R have a
second-digit mismatch on W_2. On W_1, either M or R is fixed exactly
when (4,xi)=xi. Iterating this equality determines every digit of xi,
so its unique solution is the infinite constant 4 word. Consequently

    Fix(M) intersect W = Fix(R) intersect W = {P},
    P=(2,4,4,4,...),
    Fix(A) intersect W = Fix(Q) intersect W = empty.

This quantifies over ALL tails, including nonperiodic and unbounded ones.
There is no finite tail sample and no fixed-cylinder family hidden behind
the check. No other cylinder or higher period is searched.

## 9. The fixed clock and its nonprime primitive

Let t=pi(4,4,...). The coding relation gives t=1/(4+t), 0<t<1, hence
t=sqrt(5)-2. For M at P, U=(2,4,4), V=(2,4), with tail value t.
Both H_U(t) and H_V(t) equal pi(P)=H_2(t), so the density ratio in J
is one. The chain-rule derivative ratio cancels the common H_2 and H_4
factors, leaving

    J_M(P)=|H'_4(t)|=t^2,
    K=kappa_M(P)=-2 log t
      =2 log(2+sqrt(5))=log(9+4sqrt(5)).

For R the actual U=(2,4), V=(2), and its own tail is again constant 4.
Its own derivative ratio likewise equals t^2, so kappa_R(P)=K. This
coincidence follows from the actual rules and versions, not an imported
control clock. In fact M and R agree on W_1 as actual prefix maps.

Since 2<sqrt(5)<9/4, we have 17<9+4sqrt(5)<18. Thus exp(K) is not an
integer, and certainly not an ordinary prime. K is positive. The entire
stabilizer calculation below, rather than this one return alone, shows
that K is the physical primitive.

## 10. Complete full-X incoming packets and control distinctions

For O=M or R let B_O=union_(j>=0) P_j^O({P}), using that owner's own
complete predecessor formula. This is exactly P's full source orbit:
coalescence with P is equivalent to eventually reaching P, since every
iterate of P is P. Countable inverse branches make B_O countable, with
every depth retained. Each singleton remains mu-null but is not deleted.

For explicit first levels, write 4^infinity for the constant tail. Then

    Pre_R(P)={(1,1,4^infinity)}
              union {(d,2d,4^infinity):d>=2};
    Pre_M(P)={(1,1,4^infinity)}
              union {(d,2d,8d,...,2*4^(k-2)d,4^infinity):
                                                     d>=2, k>=2}.

For k=2 the latter finite growing prefix is just (d,2d). Its last term
is at least 4, so the final pair with the tail's first 4 fails D; all
earlier pairs are successful. Conversely every M quotient inverse of P
has exactly these output quotients and final failure, proving exhaustion.
The all-depth recursion of Section 6, not these first levels alone,
specifies the complete basins and compatible infinite histories. The
constant history at P is retained for each owner.

These owner basins cannot silently be identified. For example the actual
MAIN predecessor z=(2,4,16,4^infinity) satisfies Mz=P. Under R it goes
to (2,16,4^infinity), then to (8,4^infinity), and for j>=2,

    R^j z=(8+4(j-2),4^infinity).

The last formula follows inductively because its first digit is at least
8, so the proper-divisor guard against 4 is false and the next step adds
4. Thus z never reaches P under R. This is an exact incoming-packet
comparison for the already found core, not an additional period search.
No opposite inclusion or general basin census is inferred.

For either owner O and any z in B_O choose an arrival time ell(z) at P
and put E_O(z)=S_ell(z)(z)-ell(z)K. Later arrivals add the matching
multiple of K, so this is independent of the chosen arrival. Every
integer lag is realized between any two points by taking large enough
arrival depths. The ENTIRE restricted groupoid and clock are therefore

    G_O|B_O = B_O times Z times B_O,
    c_O(z,k,w)=E_O(z)-E_O(w)+kK.

Conversely extending any coalescence to P gives this formula, so no
additional clock has been missed. On B_O, K_lag has k=0, K_clock has
E_O(z)-E_O(w)+kK=0, and K_joint has k=0 and E_O(z)=E_O(w).
At every incoming point the entire source isotropy is Z and its entire
clock image is KZ; extension isotropy is trivial. Transient endpoint
terms cancel in loops and cannot introduce a smaller period.

The exact phase test is

    h_z-E_O(z) = h_w-E_O(w) modulo KZ.

For each owner separately this yields ONE full physical packet, all phases
R/(KZ), primitive K and every positive repetition mK. Equal values in M
and R are not two packets of MAIN. A and Q have no fixed cores in W;
their full histories, including all incoming to their own states, still
remain in the global formulas and are not omitted for that reason.

The proper-divisor operation is active on the MAIN return at P; A/Q do
not reproduce it. However R DOES reproduce its fixed clock and primitive,
so this gate cannot credit maximal-chain feedback as necessary to that
return. The long-chain mechanism is nevertheless a genuine actual-map
change: on all W_2 tails MAIN writes (2,2,3,xi) while R writes
(2,8,3,xi), and their full incoming packets above differ. Neither fact
turns the nonprime primitive into prime adequacy.

## 11. Decision, limitations and release boundary

The entire MAIN packet has primitive log(9+4sqrt(5)), whose exponential
lies strictly between 17 and 18. This is an owned counterexample to the
frozen necessary ordinary-prime purity target. The portfolio decision is
STOP / FORK. MAIN's active arithmetic and its correct original-measure
clock do not rescue the failed target; R's matching return is additional
control evidence, not borrowed MAIN credit or a duplicate MAIN packet.

The proofs establish the full CF Borel/probability owner, baseline shift
invariance, exact four-owner inverse/IMAGE/history constructions, and the
complete two-cylinder fixed gate with its full-X packets. No other fixed
cylinder, higher-period classification, all-prime coverage, operator,
trace or determinant is supplied. Local clock variation has not been
promoted to infinite-rank periodic support. Strong arithmetic naturalness
and PROVES_TOO_MUCH remain separate, not certified by this window.

T0 ownership is established at the stated Borel/history level; arithmetic
T1 is NOT PASSED. T2 has the scoped exact packet/repetition result and a
refuted necessary MAIN prime-purity target, not a complete global positive
orbit ledger. T3 is NOT AUDITED. Classical fields are NOT APPLICABLE,
formal Route coordinates UNASSIGNED, and Route B NOT INVOKED. The
same-object ledger stayed intact separately for all four owners.

Preserve the density, parser, version and this negative record without
retuning or selecting a core. This reviewer now freezes and fully self-reads
raw, reports its receipt, then HOLDs. Current author access remains locked
until DISTINCT PAPER UNLOCK after root's complete raw read. No paper480.

EOF — MCR01 isolated raw derivation.
