# DME01 — independent frozen-card derivation

Date: 2026-09-24. Candidate: `ANG-20260924-DME01`, Paper 452.
Batch: `TRANSPORT-PACKET-20260924-U`, round 3/5, exactly 450–454; no 455.
AI-assisted same-model/shared-history internal review: `NOT_CALIBRATED`.
Not blind, human, external, cross-model, or independent peer validation.

## 1. Input, release, and result boundary

Root separately released raw mathematics after reporting a full 111-line CP1 read.
Sole scientific input is candidate-card.md, original lines 1–98/EOF, SHA256
`af564b868a621a58d73ccfda5ecde88ef3265d27062bf1e9d93730693730a1f9`.
The entire original card was read at CP1 and reread by an exact 98-line prefix
after release; no later outcome append was accessed.
Frozen scope-review.md: 111 lines, SHA256
`4c0917d399fd60af9798557bbbdd261522a399e9f8d4d45db203933f723d39e0`.
The refreshed ARS/local-guidance reading receipts and exposure limits are in CP1.
They are retained, not represented as newly reread during this raw derivation.
No author manuscript/README/ledger, current peer/helper report, other new science,
old proof, external literature, scientific code or numerical census was accessed.
No network, Git, PDF, auxiliary agent, model change, or outside write was used.
Exact rational Taylor estimates below are proofs, not numerical experiments.

All three owners have complete actual inverse/IMAGE and history descriptions.
MAIN/G each have one global fixed point; their full inverse basin is a singleton.
Its full-volume density rho satisfies 1/5<rho<1/4, so its primitive time is
log(1/rho), strictly between log 4 and log 5, not any integer logarithm.
L has its own unique global fixed point and singleton basin, with primitive log 4.
The actual adverse MAIN primitive stops the prime-only necessary target.
No higher-period classification, universal no-go, or repair is asserted.

## 2. Full matrix exponential derivative and its exact regular locus

Write X=M2(R), with original four-entry Lebesgue measure mu_4, and C=diag(-1,-2).
For fixed integer q, the MAIN/G analytic extension is F_q(A)=exp(qA)C.
The exponential power series and its differentiated series converge uniformly
on bounded sets. Termwise differentiation, or multiplication of the two
exponential series followed by integration, gives
`D exp_M[H]=integral_0^1 exp((1-s)M) H exp(sM) ds`.
The integral identity follows since integrating `(1-s)^i s^j/(i!j!)` gives
`1/(i+j+1)!`, the coefficient of each differentiated matrix-power term.
Consequently `DF_q(A)[H]=q (D exp_(qA)[H]) C` on all four tangent directions.
There is no differentiation of floor functions and no commuting-source assumption.

Put t=tr A and v=t²/4-det A. Define the real entire function
`h(u)=sum_(j>=0) u^j/(2j+1)!`.
Thus h(0)=1; h(u)=sinh(sqrt u)/sqrt u for u>0 and
h(u)=sin(sqrt(-u))/sqrt(-u) for u<0.
The full four-dimensional determinant is
`Delta_q(A)=4 q^4 exp(2qt) h(q²v)^2`.                                  (1)

To prove (1), first let a complex matrix M have distinct eigenvalues lambda_1,
lambda_2. Similarity induces a change of basis on the whole four-dimensional
matrix space. In the matrix-unit basis the derivative of exp has factors
`exp lambda_1`, `exp lambda_2`, and twice
`(exp lambda_1-exp lambda_2)/(lambda_1-lambda_2)`.
Their product is `exp(2 tr M) h(((lambda_1-lambda_2)/2)^2)^2`.
For M=qA the argument of h is q²v. Scalar multiplication of four input directions
contributes q^4, and right multiplication by C contributes `(det C)^2=4`.
Matrices with distinct complex eigenvalues are dense in M2(R); both the real
determinant and the entire expression are continuous. This extends the identity
to repeated-eigenvalue and nondiagonalizable matrices, including all Jordan cases.
Complex diagonalization here proves a full-volume identity, not a selected carrier.

For q=0, F_0 is the constant C and its derivative is zero, as also shown by (1).
For q!=0, the regularity condition is exactly h(q²v)!=0. If v>=0 it always holds.
If v<0 it fails exactly when `abs(q) sqrt(-v)=k pi` for an integer k>=1.
These conclusions determine the full real regular locus, not just diagonal inputs.
On the regular locus Delta_q>0. Let rho_q=Delta_q there.

For L, the separate extension is K_q(A)=(I+qA)C, so
`DK_q(A)[H]=q H C`, `Delta^L_q=4q^4`.                              (2)
Its full regular locus is all X when q!=0 and empty when q=0.
Thus q=0 has no legal outgoing branch for any of the three owners, by their
own frozen guards. Its source objects remain in X; no object has been deleted.

At A=diag(d,N), with integers 1<d<N, an admitted MAIN quotient q=N/d is positive
and nonzero, and v=(N-d)^2/4>0. Equation (1) is strictly positive there.
Hence MAIN's actual admission at the proper-divisor interface is exactly d|N.
G's quotient floor(N/d) is also positive, so its own geometric guard holds even
when divisibility fails. L has its own positive determinant (2) at admitted seeds.
The new matrix is the next arithmetic input; q is not a passive fixed register.
These facts establish the stated lineage mechanism, not canonical naturalness.

## 3. Every actual inverse, including q=0, and the countable atlas

For MAIN enumerate integers m!=0,n with m|n and q=n/m. G enumerates all integer
m,n, with its own floor quotient for m!=0 and q=0 for m=0. L uses MAIN's labels.
For MAIN/G and q!=0, every actual inverse of Y is exactly
`A=Z/q`, where Z is ANY real matrix satisfying `exp Z=Y C^{-1}`,
retained precisely when A has those two floors, the owner's quotient/permission,
its full regularity, and the actual forward equality.
Necessity uses Z=qA; sufficiency substitutes the equality back into F_q(A)=Y.
This keeps all real matrix logarithms, not a principal logarithm or a selected
spectrum. If no real logarithm exists the corresponding set is empty.
In particular exp Z is invertible, as exp Z exp(-Z)=I follows from the series;
this is an image fact, not an extra source-invertibility restriction.

For L and q!=0, its complete candidate is `A=(Y C^{-1}-I)/q` for that label,
with its own actual reconstructed floor and permission tests and (2).
For q=0 each owner has constant forward equation Y=C: before guards every A
solves it when Y=C, and none does otherwise. Its own zero derivative then
rejects all those candidates as legal inverses. No division by zero or unique
inverse has been manufactured. Target outgoing permission is never imposed.
Deduplicating actual A gives each owner's exact predecessor set P_O(Y).

For every fixed-label extension, the regular locus is open and the inverse
function theorem gives an injective analytic neighborhood at each regular point.
A rational-center/rational-radius ball containing the point can have its closure
inside that neighborhood. Thus the card's eligible rational balls form a
countable cover. On each ball the map is an analytic diffeomorphism onto its open
image: local inverses agree by injectivity. Keep the specified order.
Intersect with actual source label cells and assign each point to its first
eligible ball. These pieces are Borel, disjoint, and cover the exact legal source.
Their images are Borel because the ambient inverse homeomorphism pulls them back.
Restricting the inverse gives a countable Borel actual inverse atlas.
The preceding algebraic equivalences show that this atlas and P_O coincide.
Each target has at most countably many actual predecessors, one per injective
piece; no finite-root claim or finite matrix-log branch selection is needed.

## 4. Every-point IMAGE version and own clocks

At an actual branch value theta(Y)=A, analytic inverse differentiation gives
`J_theta(Y)=1/rho_q(A)` for MAIN/G and `J_theta(Y)=1/(4q^4)` for L.
These are strictly positive and finite at every actual point. At cuts and floor
faces the inverse is still the restriction of an ambient analytic inverse germ.
Two eligible germs with the same source and actual q agree locally by inverse
uniqueness, so the prescribed pointwise value is consistent.
For every Borel E in its branch target, ordinary change of variables on the
open ambient extension, restricted to E, proves
`mu_4(theta(E))=integral_E J_theta(Y) d mu_4(Y)`.
This includes null faces; their clock values come from the specified germ,
not from an arbitrary a.e. representative. No measure or normalization changes.

The full partial maps are Borel and nonsingular in the preimage-null-set sense
by the countable branch decomposition. Overlapping images need not give global
injectivity or an invariant measure. The actual branch clock is not a sum of
densities over unrelated preimages.
The own legal clocks are
`kappa_M/G(A)=log 4+4 log abs(q)+2q tr A+2 log abs(h(q²v))`,
`kappa_L(A)=log 4+4 log abs(q)`.
Here each q and domain belong to that owner. MAIN/G clocks may be signed;
L's legal integer q!=0 gives kappa_L>=log 4. Terminals have no next-step clock,
not an assigned zero, and legal zero clocks are not removed.

## 5. Entire history groupoids and all kernels

Work separately with each own T. Let D_r be its Borel domain of r legal steps,
D_0=X, and define S_r=sum_(j=0)^(r-1) kappa(T^j z), S_0=0, M_r=exp S_r.
Thus M_0=1 and M_r is the product of the actual positive forward densities.
For L specifically `M_r=4^r product_(j=0)^(r-1) abs(q(T^j z))^4`;
it is not generally 4^r because the actual quotient can change.
The full source groupoid consists of all triples (z,r-s,w) with legal common
tail T^r z=T^s w, identifying equal triples but retaining the integer lag.
It is Borel as a countable union of Borel common-tail equalities.

Set `c(z,r-s,w)=S_r(z)-S_s(w)=log(M_r(z)/M_s(w))`.
Two witnesses of the same lag differ by the same number of extra steps on both
sides. Using the longer witness, their extra sums start at the same common point
and cancel. This proves descent without requiring any unavailable terminal step.
For composable witnesses (r,s) and (u,v), align the middle object's lengths by
t=max(s,u). The longer middle history exists; equal tails give the required
outer continuations. The composite witnesses (r+t-s,v+t-u) have the sum of the
lags, and middle-sum cancellation proves additivity. Inversion negates c.
The actual forward arrow `(Tz,-1,z)` has clock -kappa(z), its inverse +kappa(z).

Finite itineraries of the inverse atlas give injective Borel history pieces with
ambient analytic germs. On any common-image pair the actual arrow w->z is
`(T^r|piece)^{-1} composed with (T^s|piece)` and its determinant modulus is
`M_s(w)/M_r(z)=exp(-c)`. Change of variables on these germs proves the full
history every-Borel IMAGE formula, including assigned null-boundary points.

All three kernels on the whole owner are exactly
`K_lag={(z,0,w): some legal r has T^r z=T^r w}`;
`K_c={(z,r-s,w): T^r z=T^s w legally and M_r(z)=M_s(w)}`;
`K_joint={(z,0,w): some legal r has T^r z=T^r w and M_r(z)=M_r(w)}`.
The same witness cancellation proves these descriptions independent of choices.
They include every source and incoming class, not just fixed basins or units.
In particular the variable quotient in L does not license identifying its clock
kernel with its lag kernel without the displayed product condition.

## 6. Full extension, entire H, incoming, and every phase

On all X x R an actual arrow (z,k,w) acts `(w,h)->(z,h+c)`.
Additivity makes this a well-defined groupoid extension. Its lag kernel lifts
K_lag and can change height; height-preserving arrows lift K_c; both conditions
lift K_joint. Every real height and all vertical translations are retained.
Only the extension's orbit SET is used, not a regular quotient or global selector.

If a point is not eventually periodic, including any terminal-ending history,
it has trivial source isotropy: unequal equal iterates would generate a legal
cycle and hence an infinite periodic continuation. Then its entire H is {0}
and extension isotropy is trivial, though inter-object arrows can have clock.
If the orbit eventually reaches a least-p cycle, exactly the lags pZ occur as
source isotropy. Necessity follows by comparison of late cycle positions;
sufficiency uses witnesses after entry with any integer number of full turns.
If C_gamma is the clock sum around that least cycle, transient sums cancel,
so `c(z,kp,z)=k C_gamma` and the ENTIRE subgroup is `H_z=C_gamma Z`.
Extension isotropy is `{kp:k C_gamma=0}`. Thus it is pZ for zero cycle clock
and trivial for nonzero cycle clock; zero-clock source isotropy is not discarded.

For one source orbit choose a base b only to describe its phases. Transporting
(z,h) by any actual arrow z->b yields a real height modulo H_b. Different
choices differ precisely by source isotropy clocks; conversely every such
difference is realized. Hence all phases are R/H_b, with transitive vertical
translation action and stabilizer exactly H_b. For a cycle base reached by a
depth d, the phase is `h-S_d(z) modulo H_b`; another entry differs by whole
cycle clock sums. For H=0 it is a line, not a positive periodic orbit.
For C_gamma!=0 the least positive period is abs(C_gamma), with repetitions
j abs(C_gamma), j>=1. Different phases lie on the same height-translation orbit;
distinct source orbits remain distinct packets even when lengths coincide.
These are structural formulas, not a classification or census of higher cycles.

At every target Y, including terminal targets, define P_O^0(Y)={Y} and
`P_O^(d+1)(Y)=union_(Z in P_O^d(Y)) P_O(Z)`.
Induction proves equality with all sources whose d legal steps reach Y.
Thus all logarithm branches, own source labels and every incoming depth are
retained. A target without incoming may still have an outgoing step, and a
terminal target may have incoming; those are separate questions throughout.
More explicitly, for terminal b its full source orbit is the union of P_O^d(b).
Each point z in it has a unique hitting depth d_z, since b has no next step.
Common-tail continuation to b shows that the only lag between z,w is d_z-d_w,
with clock S_(d_z)(z)-S_(d_w)(w); conversely the terminal itself supplies this
witness. Thus terminal lag/clock/joint kernels impose, respectively, equal
depths, equal entry sums, and both. All terminal phases are the real values
`h-S_(d_z)(z)`, with no quotient identification because H_b={0}.

## 7. GLOBAL exponential fixed sets: derive the reduction

For a legal MAIN/G fixed point A=exp(qA)C, multiply on the left by exp(-qA):
`C=exp(-qA)A`. The right side commutes with A by its power-series definition.
Thus A commutes with C. Since C has two distinct diagonal entries, the two
off-diagonal entries of A must vanish. This is a derived restriction on fixed
solutions, not an assumption on the full carrier or its tangent determinant.
Write A=diag(a,b). Its fixed equations give
`a=-exp(qa)<0`, `b=-2 exp(qb)<0`.
Thus both floor labels are negative. MAIN's actual q=n/m is a positive integer;
G's actual floor(n/m) is nonnegative, and q=0 is excluded by its own derivative.
In either case any legal fixed quotient therefore has q>=1.

Put x_q=-a>0,y_q=-b>0. The equations become
`x_q exp(q x_q)=1`, `y_q exp(q y_q)=2`.
The function u->u exp(qu) increases strictly from 0 to infinity for q>=1,
so each equation has exactly one positive root. At u=1 its value exp(q)>2,
since exp(1)>1+1. Both roots lie in (0,1). Consequently m=n=-1, forcing
the owner's actual quotient q=1 in both MAIN and G.

Let x,y be the unique roots `x exp x=1`, `y exp y=2`.
Then 0<x<y<1 and y<2x, the last inequality following from
`(2x)exp(2x)=2 exp x>2` and strict monotonicity.
The only possible fixed matrix is `A_E=diag(-x,-y)`.
It has actual floors m=n=-1 and q=1; its two eigenvalues are distinct real,
so (1) is strictly positive. Substitution verifies fixedness.
Therefore `Fix(T_MAIN)=Fix(T_G)={A_E}` globally on all four entries.

## 8. GLOBAL linearized fixed set, using its own rule

The L fixed equation is `A(I-qC)=C` with an actual nonzero integer q.
For q=-1 the first column on the left vanishes, contradicting C's first column.
For every other integer q the diagonal matrix I-qC is invertible, so the sole
formal solution is `A=diag(-1/(1+q),-2/(1+2q))`.
For q>=1 both entries lie strictly in (-1,0), forcing m=n=-1 and actual q=1.
For q=-2 the entries are 1 and 2/3, giving m=1,n=0 and actual quotient 0,
not -2. For q<=-3 both entries lie in (0,1), so m=0 violates permission.
The q=0 case has no regular source independently by (2).
Thus the only actual fixed point is `A_L=diag(-1/2,-2/3)` with q=1,
and (2) gives rho_L=4 there. Direct substitution verifies it.
Hence `Fix(T_L)={A_L}` globally, not just on a selected diagonal slice.

## 9. Full-volume fixed clock: exact rational bounds

At A_E, the four factors of D exp are x, y/2 and twice
`d=(x-y/2)/(y-x)>0`. Right multiplication by C contributes determinant 4.
Thus the FULL four-dimensional forward density is
`rho_E=2xy ((x-y/2)/(y-x))^2`.                                    (3)
The off-diagonal tangent factors in (3) are indispensable.
We now prove 1/5<rho_E<1/4 using exact inequalities, without floating evaluation.

For t>=0 let `S4(t)=sum_(j=0)^4 t^j/j!`. For 0<=t<6 the positive series tail
satisfies `exp t-S4(t) <= (t^5/120)/(1-t/6)`, because successive terms after
the fifth have ratios at most t/6. Strict bounds below use t strictly below
their displayed comparison endpoints.

First `S4(17/30)=34250281/19440000 < 881/500`.
Using 17/30<3/5, the tail is less than 9/12500, so
`exp(17/30)<11017/6250<30/17`; the last cross-products are 187289<187500.
Also 71/125>17/30 and
`S4(17/30)>125/71`, since 2431769951>2430000000.
Strict monotonicity of u exp u therefore gives
`17/30 < x < 71/125`.                                            (4)

Next `S4(213/250)=73124564387/31250000000 < 117/50`.
Since 213/250<6/7, its tail is less than
`((6/7)^5/120)/(1-1/7)=54/12005<9/2000`.
Thus `exp(213/250)<4689/2000<500/213`, because 998757<1000000.
On the other side `S4(6/7)=5647/2401>7/3`, since 16941>16807.
Strict monotonicity gives
`213/250 < y < 6/7`.                                              (5)

The entire rectangle (4)–(5) lies in 0<x<y<2x. For the expression (3),
`partial_x log rho=1/x+4/(2x-y)+2/(y-x)>0`, while
`partial_y log rho=1/y-2/(2x-y)-2/(y-x)<0`.
Consequently its lower corner bound is
`rho_E > 2*(17/30)*(6/7)*(29/61)^2 = 28594/130235 > 1/5`,
where 142970>130235 verifies the final inequality.
Its upper corner bound, where the divided difference is 1/2, is
`rho_E < 2*(71/125)*(213/250)*(1/2)^2 = 15123/62500 < 1/4`,
where 60492<62500 verifies the final inequality.
Hence `4 < 1/rho_E < 5` exactly. In particular kappa_E=log rho_E is negative,
and the positive generator of kappa_E Z is `-log rho_E=log(1/rho_E)`.
This sign choice uses the full group, not a modified positive roof or a rescaling.

## 10. All incoming branches of every fixed core: closed classification

For MAIN/G, the target A_E has `A_E C^{-1}=diag(x,y/2)` with distinct positive
entries because y<2x. Any REAL matrix logarithm Z of this diagonal matrix
commutes with its own exponential, hence commutes with that distinct-entry
diagonal matrix. Its off-diagonal entries must therefore be zero.
Real scalar exponential is injective, so the only such real logarithm is
`Z=diag(log x,log(y/2))=diag(-x,-y)=A_E`.
This proves completeness at this target; it does not choose a principal
logarithm in the general inverse relation or exclude a noncommuting root by fiat.

Every q!=0 candidate predecessor is therefore A_E/q. For positive integer q,
both entries are strictly in (-1,0), so actual m=n=-1 forces actual q=1 for
MAIN and G. For negative integer q both entries lie in (0,1), so MAIN fails
m!=0 and G actually reads q_G=0, not that negative q. The q=0 branch has no
regular source. Thus `P_MAIN(A_E)=P_G(A_E)={A_E}` exactly.
The all-depth recursion consequently yields singleton basins for both owners.

For L, `A_L C^{-1}-I=A_L`, so every q!=0 candidate predecessor of A_L is A_L/q.
Positive integer q again produces two entries in (-1,0), forcing actual q=1.
Negative q produces two entries in (0,1), violating MAIN's retained permission.
Its q=0 branch independently has no regular source. Hence `P_L(A_L)={A_L}`,
and L's complete all-depth basin is also a singleton.
These are exact unrestricted inverse classifications, not finite-depth searches.

The full source orbit of a fixed core equals its all-depth inverse basin:
any common tail with a fixed point forces an iterate of the other endpoint to
equal that core. Therefore each core's whole source orbit is the singleton just
proved, though its retained-lag source isotropy is still all Z.
On MAIN/G's core, `c(A_E,k,A_E)=k log rho_E` and ENTIRE H=(log rho_E)Z.
On L's core, `c(A_L,k,A_L)=k log4` and ENTIRE H=(log4)Z.
All three cycle clocks are nonzero, so extension isotropy is trivial at every
height. Restricted to each full fixed-source orbit, lag/clock/joint kernels
are all the lag-zero unit; this does not trivialize the global kernels in §5.

Every real phase is retained: MAIN/G have R/((log rho_E)Z), L has R/((log4)Z).
Each is one closed height-translation packet, not one packet per phase or
inverse word. MAIN/G's least positive time is log(1/rho_E), with repetitions
j log(1/rho_E); L's is log4, with repetitions j log4, for every j>=1.
No incoming branch, omitted real logarithm or source isotropy can shrink these
generators. All other incoming classes retain the exact recursion in §6.

## 11. Controls, necessary target, and stop

MAIN retains exact proper-divisor admission, the full four-dimensional analytic
IMAGE clock, all real logarithm branches, and a nonempty owned fixed packet.
Its primitive satisfies `log4 < log(1/rho_E) < log5`, so it cannot be log n
for any ordinary integer n, in particular for any ordinary prime.
This single actual adverse primitive refutes the necessary prime-only target.
Its repetitions and positive-time orientation come from the ENTIRE H; no
different packet elsewhere can remove the adverse one from this owner's ledger.

G is a separately owned permission-off map with its own quotient and inverse
checks. Its same fixed core/packet was obtained from its own readout, not
transferred from MAIN. L owns its linearized transport, determinant, inverses,
full groupoid and singleton fixed packet; its primitive log4 is composite.
Neither control rescues MAIN or establishes global equivalence with it.
The full-volume/noncommuting-root/terminal/null-point/phase checks supply
ownership diagnostics, not a fabricated extra control owner or numeric score.

The same-object ledger stayed intact. Full carrier/IMAGE/clock ownership is
established within this ANG screen; strong naturalness remains OPEN, arithmetic
T1 is NOT PASSED, and the T2 prime-only necessary target fails.
T3 is NOT AUDITED; classical fields are NOT APPLICABLE; formal Route coordinates
are UNASSIGNED and Route B is NOT INVOKED. Higher periods, prime multiplicity
elsewhere and all-prime coverage remain unclassified; no such census was run.
Portfolio: STOP / FORK for frozen DME01, not a general impossibility claim.

## 12. Raw freeze and stage separation

After full self-read this report is bound by its measured line count and SHA256
in the handoff; the original 98-line card prefix and CP1 are checked unchanged.
The raw is immutable after that receipt. HOLD for root full raw read and a
distinct PAPER UNLOCK before any manuscript comparison. A later discrepancy
must be reported explicitly, not silently repaired in this independent record.
No work on 455 or beyond is authorized by this stage or its outcome.
