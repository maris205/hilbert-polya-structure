# GRF01 — independent raw derivation of the global periodic-core gate

Audit: `ANG-AUDIT-20260924-GRF01`; unchanged underlying owner `ANG-20260924-GOF01`.
Result: every legal periodic point of each owner has inactive gcd observable.
MAIN and gcd-OFF have identical complete periodic cores with identical core clocks;
fold-OFF has only the origin periodic. No equality of full basins/groupoids is asserted.

## 1. Inputs, isolation and proof boundary

Scientific input: `candidate-card.md`, original lines 1–91 through EOF, SHA256
`e96d599790a383ada12996bda67363a308713cd7cfd1e5bfa184191a0d3a543d`.
Named background: `../456-gcd-oblique-fold/paper.md`, 242 total lines, whole-file SHA256
`10174a938cae1b5c38fd2e94c44a098b95f9abed4c23bfae857dd8137fdc9220`.
Actual dependency read is only lines 1–167: header/abstract and complete Sections 1–4;
later headings were exposed by navigation, but Sections 5–8 and old raw/review were not read.
The old abstract's fixed/two-step results are exposure, not proof of the new global gate.
CP1 `scope-review.md`: 82 lines, SHA256
`9ab08962a8a334cf662049587f2e24437f3b824695fb974de1116bb6f70a6f01`.
Root issued a distinct RAW release after fully reading CP1. No current author manuscript,
README, ledger, helper/peer answer or appended outcome was read for this derivation.
ARS/router/runtime/DA/fallacy/anti-leakage and local governance full reads are retained
as recorded in CP1. No new source, scientific code, numerics, network, Git or PDF was used.
Inherited model and shared prior history are `NOT_CALIBRATED`, not blind or external review.
No reviewer helper was used. Only this new raw file is written; old files and CP1 stay fixed.

## 2. Exact owners and complete inverse/measure data

All owners retain X=R² and its original Lebesgue area. Set
g(x,y)=Gamma(floor x,floor y), with Gamma(a,b)=gcd(|a|,|b|) except Gamma(0,0)=1.
Thus g is always a positive integer. Write f(t)=t/(1+t²).
MAIN uses t=x−gy and T_M=(f(t),gx+y), legal exactly t²≠1.
G uses t=x−y and T_G=(f(t),x+y), legal exactly t²≠1, without integer-cell labels.
L uses T_L=(x−gy,gx+y) on ALL X. It has no fold guard.
No illegal source is deleted or given an absorbing loop; all targets remain objects.

For replay of the inherited owner data put
B_-=(−∞,−1), B_0=(−1,1), B_+=(1,∞),
U_-=(−1/2,0), U_0=(−1/2,1/2), U_+=(0,1/2).
The fold maps each B_j analytically and one-to-one onto U_j, with
f'(t)=(1−t²)/(1+t²)². Its roots are
rho_0(u)=2u/(1+sqrt(1−4u²)), and rho_±(u)=(1+sqrt(1−4u²))/(2u)
on their respective U_j. At u=0 only rho_0(0)=0 is a finite root.
At |u|=1/2 only the forbidden critical root exists; outside that interval no root exists.
There is no infinite or outer-sheet predecessor at u=0.

Let C_ab=[a,a+1)×[b,b+1), a,b integers, and g=Gamma(a,b).
For MAIN and each sheet j take exactly
theta_abj(u,v)=((rho_j(u)+gv)/(1+g²),(v−g*rho_j(u))/(1+g²))
on {(u,v) in U_j×R: theta_abj(u,v) belongs to C_ab}.
For G use this formula with g=1 and domain U_j×R, without a cell restriction.
For L take theta_ab(u,v)=((u+gv)/(1+g²),(v−gu)/(1+g²))
on {Z in X: theta_ab(Z) belongs to C_ab}; no sheet or fold permission is imposed.
These are every actual inverse: forward sources determine their actual cell/sheet,
and the inverse linear mixing and fold root recover that source. Conversely each listed
source passes its own cell and permission tests and maps back to the target.
All domains are Borel; duplicate actual sources are identified, not different predecessors.

The fixed-cell/sheet ambient analytic germ gives at every assigned point
J_M=(1+rho²)²/((1+g²)|1−rho²|), J_G=(1+rho²)²/(2|1−rho²|),
and J_L=1/(1+g²). Each is positive finite on its actual domain.
Ambient change of variables restricted to every Borel subset E of that domain gives
mu(theta(E))=integral_E J dmu, including integer faces/null sets and infinite-area E.
The prescribed germ fixes the null-point version; whole-map continuity at cuts is not used.
Consequently the own legal clocks are
kappa_M=log((1+g²)|1−(x−gy)²|/(1+(x−gy)²)²),
kappa_G=log(2|1−(x−y)²|/(1+(x−y)²)²), and kappa_L=log(1+g²).
They equal −log J_actual(Tz); signed and zero clocks stay. Terminals have no next summand.
This restates and checks owner definitions, not a new general-history contribution.

## 3. Arbitrary-period MAIN bound, including every sign and cut case

Take ANY legal M cycle z_i=(x_i,y_i), i modulo p, p≥1, with its actual g_i.
Indices may coincide when p=1 or 2; none of the following identities requires distinct states.
Since 2|t|≤1+t² with equality only at |t|=1, every legal fold output satisfies
|f(t)|<1/2. Every point of a cycle is an output, hence −1/2<x_i<1/2 for all i.
Thus floor x_i is −1 for x_i<0 and 0 for x_i≥0.
In particular g_i=1 whenever x_i<0, and g_i*x_i=x_i whenever x_i≤0.

Choose i with y_i minimal on this finite cycle. From y_i−y_(i−1)=g_(i−1)*x_(i−1)
we have h=x_(i−1)≤0. Put u=x_(i−2), v=y_(i−2), a=g_(i−2), t=u−av.
Then h=f(t), so t≤0. Since g_(i−1)*h=h,
                         y_i=v+au+f(t).                         (1)
If u≥0, t≤0 implies v≥u/a≥0. Equation (1) gives y_i≥h>−1/2.
This case includes u=0 without assuming its gcd is 1.
If u<0, its actual a=1, so v=u−t and
              y_i=2u−t+f(t)=2u−t³/(1+t²)≥2u>−1.               (2)
The non-strict intermediate inequality includes t=0/h=0.
These two cases exhaust the minimum, proving y_i>−1 at EVERY cycle point.
No lower bound was assumed to obtain this conclusion.

Now choose i with y_i maximal. Then h=x_(i−1)≥0. Use the same u,v,a,t notation.
We have t≥0 and v≤u/a<1/2. Together with the already proved v>−1,
floor v belongs to {−1,0}; also floor u belongs to {−1,0}.
Every Gamma of these four pairs is 1, including the exceptional pair (0,0); hence a=1.
Next y_(i−1)=v+u=2u−t≤2u<1, and the global lower bound gives y_(i−1)>−1.
Since 0≤h<1/2, its floor is 0, so g_(i−1)=1 as well.
Therefore
              y_i=v+u+f(t)=2u−t³/(1+t²)≤2u<1.                 (3)
This exhausts the maximum, including t=0/h=0 and all integer readout faces.
Every legal MAIN cycle therefore lies in
                        R=(-1/2,1/2)×(-1,1).                 (4)
On R both floor coordinates lie in {−1,0}, and the actual gcd is exactly 1.
Thus Per(M) intersect A_act is EMPTY, for all periods at once.

The rectangle is a proved periodic-point bound, not an assumed invariant carrier.
No claim is made that all transient trajectories stay in it. The strict bounds cover
y=−1,1,2 by exclusion on cycles; y=0 and x=0 are included with their assigned floors.
Critical mixed values t=±1 remain illegal throughout; they were not crossed by continuity.

## 4. Independently owned controls and equality of periodic cores

For any legal G cycle the same fold bound gives |x_i|<1/2, while g is identically 1
in its map, irrespective of the separately evaluated activity observable.
With h=x_(i−1)=f(t), t=x_(i−2)−y_(i−2), one always has
                        y_i=2x_(i−2)−t³/(1+t²).               (5)
At a minimum of y, h≤0 gives t≤0, hence y_i≥2x_(i−2)>−1.
At a maximum, h≥0 gives t≥0, hence y_i≤2x_(i−2)<1.
Thus every G cycle also lies in R, where the read-only Gamma observable equals 1.
Per(G) intersect A_act is independently EMPTY; this is not the tautology that its map uses 1.

For L the exact identity
                ||T_L(z)||²=(1+g(z)²)||z||²≥2||z||²            (6)
holds on its entire domain. Iterating around a period-p cycle forces z=0.
Conversely the origin is legal and fixed, with Gamma(0,0)=1.
So Per(L)={0} and Per(L) intersect A_act is EMPTY.
This is one global analytic control argument, not a period-by-period classification.

Every M cycle lies in R and therefore follows precisely the G map and permission;
every G cycle likewise has actual Gamma=1 and follows the M map and permission.
Consequently Per(M)=Per(G), with the same action of the maps on this entire set.
The correspondence preserves each actual cycle, its least period p and its cyclic rotation class.
At each core point the two clocks also coincide with
                 log(2|1−(x−y)²|/(1+(x−y)²)²).                (7)
This proves equality of complete periodic cores, not a census of the cycles they contain.
No identity of legal transient maps, incoming basins, or full groupoids follows.

## 5. Full histories, kernels, incoming, isotropy and physical phases

For each owner separately let P_0(t)={t} and let P_(j+1)(t) contain every own inverse
from Section 2 of every point in P_j(t), with all actual domain tests retained.
Induction gives P_j(t)={z:T^j z=t legally}. All j≥0 are retained without a cutoff.
Set S_m(z)=sum_(0≤i<m) kappa(T^i z), S_0=0 and W_m=exp S_m>0 on legal histories.
The complete actual groupoid and clock are
 G_U={(z,m−n,w):T^m z=T^n w legally}, c=S_m(z)−S_n(w), source w/range z.             (8)
Only equal triples are identified. Equal-lag witnesses differ by common extra depths;
their extra sums start at the same meeting point and cancel. Alignment along the middle
legal history proves composition/additivity without padding a terminal with fictitious steps.
Inversion negates c, units occur at all objects, and (Tz,−1,z) has clock −kappa(z).
The countable Borel history equalities make the groupoid and this descended clock Borel.
On a fixed finite-history branch the endpoint IMAGE density is W_n(w)/W_m(z)=exp(−c),
by the own forward/inverse change-of-variables rules, with the prescribed all-point germs.

Every arrow incoming to t is (t,r−j,z), where T^r t is legal and z in P_j(T^r t).
This includes all depths and every incoming to a terminal by r=0; reversing gives outgoing.
Its endpoints are exactly the full source class. The complete kernels are
 ker lag={(z,0,w):z,w in P_j(t) for some j,t},
 ker c={(z,m−n,w):z in P_m(t), w in P_n(t), W_m(z)=W_n(w) for some m,n,t},
 ker lag intersect ker c={(z,0,w):z,w in P_j(t), W_j(z)=W_j(w) for some j,t}.          (9)
These tests preserve coalescing histories and zero clocks, and are not finite orbit samples.

A nonzero source isotropy lag occurs exactly when two unequal legal iterates coincide,
equivalently when the source eventually reaches an actual cycle. If its least period is p
and its signed cycle sum is C, all and only lags kp occur, with c(z,kp,z)=kC, k in Z.
Every incoming prefix cancels, so the ENTIRE H at the core and every feeder is C Z.
Sources not eventually periodic, including all terminal classes, have unit isotropy and H=0.
The full real extension has isotropy pZ if C=0 and only units if C≠0; nonperiodic classes
have units. This distinguishes zero physical returns from nontrivial zero-clock source isotropy.
Over each source class choose an anchor only to describe phases, and an anchor-to-z arrow
of clock b_z. The complete phase coordinate is h−b_z modulo H; different choices differ by H.
Height translation has stabilizer precisely H, without a measurable selector or nice quotient.
For C≠0 there is one physical periodic packet per full source class, primitive |C| and all
positive integer repetitions. For C=0 all real phases remain and there is no positive primitive.

In a deterministic partial map a source class cannot contain two different eventual cycles:
any common legal future of cycle points forces the same cyclic orbit. Thus the identity
of M/G cycles and their sums from Section 4 gives a bijection of their periodic source classes,
including whatever own feeders each has. Corresponding entire H and extension-isotropy type
agree, and positive packets have identical primitive lengths, repetitions and multiplicities.
Different cycles with equal |C| remain different packets. Actual feeder sets, their clocks
and their phase representatives need not agree and are NOT identified between the owners.

For all three owners, the origin has only itself as a predecessor: u=v=0 forces the only
finite fold root tau=0 and the inverse linear source 0; L's linear inverse gives the same.
Its full incoming class is therefore singleton, source isotropy Z, clock k log2, entire
H=(log2)Z, unit extension isotropy, phases h modulo log2, primitive log2 and repeats j log2.
This retains the known prime-2 packet and is not the new recurrence discriminator.
For L no nonzero source can eventually reach 0, since each linear step is nonsingular.
Together with Section 4, every nonzero L source has trivial isotropy, H=0 and free real phases
over its own source class. Its still-complete incoming/kernel description is (8)–(9).

## 6. Exact conclusion and stop boundary

The frozen all-period exclusion exit is established for M, G and L; no active-gcd cycle
witness or missing uniform-bound step remains. The essential new proof is the arbitrary-cycle
extremum argument (1)–(5), not the old fixed/two-step gate or a numerical generalization.
Nontrivial gcd feedback is absent on MAIN's entire periodic core, where the gcd-OFF control
has exactly the same dynamics and clocks. This is recurrence-level PROVES_TOO_MUCH evidence.
All g>1 transient states, their actual clocks and incoming histories remain in the full owner.
Nothing here proves every MAIN primitive nonprime, classifies all remaining cycles, or certifies
global prime uniqueness/coverage. The retained log2 packet does not solve that target either.
The same-object ledger is unchanged. Strong naturalness remains OPEN; arithmetic T1 NOT PASSED,
T3 NOT AUDITED, classical NOT APPLICABLE, formal UNASSIGNED and B NOT INVOKED.
The bounded audit stops here; no object repair, new candidate, old-result rewrite or round 465.

EOF — independent raw, fully self-read before byte freeze; HOLD for distinct PAPER UNLOCK.
