# Card-only independent proof — ECF01

Candidate `ANG-20260923-ECF01`; internal inherited-model/shared-history AI work,
`NOT_CALIBRATED`, not blind, external peer review or error-independent evidence.

## 1. Actual input and release

Sole scientific input: `candidate-card.md`1–85 through EOF,5094 bytes,
SHA256 `e735ae89cae73136b6b3b282d06f902bff13b0adf74a9202960af7133949c688`.
CP1 `scope-review.md`:84 lines,
SHA256 `1d1cb489ac2e277f90f146d5369031d970695d50f252705c9b4ed0b0fe8e6c28`.
Root reported its complete CP1 reading and explicitly released card-only mathematics;
I reread the full card after release. No author/peer/sibling science or other new
surface was read. Previously read ARS workflow/DA/runtime instructions are retained.
No scientific code/numerics, external source, auxiliary, Git or model change was used.
Only this raw file is written. No PAPER UNLOCK has been received.

## 2. All four full inverses and exact image tests

Use the card's n,d,q,r,a on EVERY cell B_nd with d!=0. Uniform notation for each
owner is F(z)=c+A0/(z-b), theta(w)=b+A0/(w-c), with its OWN constants:

| Owner | b | c | A0 |
|---|---|---|---|
| MAIN | q | i r | a=n+i d |
| Q | 0 | i r | a |
| R | q | 0 | a |
| A | q | i r | 1 |

All A0 are nonzero. Moreover d!=0 implies Im z<0 or Im z>=1, hence Im z!=0.
Thus no such source equals the real b. All four complete active domains are
{Im z<0 or Im z>=1}; the retained terminal strip is 0<=Im z<1.
This verifies, rather than deletes, the additional displayed denominator checks.

For a target w=s+i t, write A0=alpha+i beta, c=i gamma and
Delta=s^2+(t-gamma)^2. Its branch is present EXACTLY when Delta>0 and

    n <= b+[alpha*s+beta*(t-gamma)]/Delta < n+1,
    d <= [beta*s-alpha*(t-gamma)]/Delta < d+1.                 (1)

These are explicit real inequalities for every n,d in Z,d!=0, with the constants
in the table. They are a complete enumeration of the image and every predecessor:
the image is the union of these domains and each passing pair contributes theta(w).
Solving the forward equation gives theta; conversely(1) restores precisely the
declared cell/readouts, activity and forward equality. No index cutoff is needed.
Different passing cells cannot duplicate a predecessor, since its half-open floors
are unique. There are at most countably many predecessors; no finite bound is assumed.
The maps and all domains are Borel. Branch poles are excluded only for that branch,
not deleted globally from X or from other branches' target domains.

Terminal incoming is genuinely retained: MAIN/Q/R take z=i in B_01 to the
terminal1; A takes z=1/2-i in B_(0,-1) to(2+4i)/5 in the terminal strip.
Every further terminal incoming history is governed by(1), without an outgoing
terminal step, added infinity, reset or absorbing loop.

## 3. Every-Borel IMAGE and the full-point clock

The complex derivative of theta is -A0/(w-c)^2. Its real derivative matrix has
determinant equal to the squared modulus, so the prescribed EVERY-point density is

    J_theta(w)=abs(A0)^2/abs(w-c)^4 >0, finite.                (2)

This includes actual cuts and terminal targets. For the every-Borel law, translate
by -c, apply complex inversion, multiply by A0 and translate by b. In polar
coordinates inversion sends rho to1/rho and angle to its negative; comparison of
rho d rho d angle gives the area factor rho^(-4). Multiplication contributes
abs(A0)^2. Integration gives mu(theta E)=integral_E J_theta dmu for arbitrary
Borel E in the actual domain, including infinite integrals. Restriction to(1)
preserves this law. The analytic derivative specifies null-point values; the
integral law alone would not uniquely determine its values on null cuts.

At every legal source the resulting OWN clock is

    kappa_F(z)=log abs(A0)^2 - 4 log abs(z-b),
    J_theta(Fz)=abs(z-b)^4/abs(A0)^2.                         (3)

All logarithms have strictly positive arguments. In MAIN/Q/R, abs(A0)^2=n^2+d^2;
in A it is1. These equalities are proved separately by the four substitutions in
the table; no control borrows MAIN's transport. Neither branchwise IMAGE nor(3)
asserts a globally invariant measure or a positive roof.

## 4. Full actual history ledger, kernels, isotropy and phases

For any owner put P_m(z)=product_(j<m) J_j(F^(j+1)z), P_0=1 on legal histories.
Equations(2)–(3) give every factor explicitly; a last terminal endpoint is allowed.
For the actual triple(z,m-n,w), F^m z=F^n w,

    c=log[P_n(w)/P_m(z)],    ell=m-n.                         (4)

Equal triples have witnesses differing by common legal padding, whose extra
factors cancel. Composition aligns the middle histories and cancels the same way;
the required segment already exists, so no terminal is passed. This proves the
actual groupoid and all-point cocycle, including null cuts. On fixed finite
itineraries its branch-pair IMAGE is P_m(z)/P_n(w)=exp(-c), by iterating the
every-Borel law. Countable itinerary domains give a Borel G and c.

The full lag kernel is equal-depth coalescence(z,0,w); the full clock kernel is
the actual triples with P_m(z)=P_n(w). Their intersection imposes both conditions.
These are complete all-source tests, not just tests on the six-cell window.
For any reference r, enumerate every legal F^n r and every finite inverse word
I_p at that point satisfying(1) at EACH stage. This gives ALL source-orbit points
z=I_p(F^n r) and arrows(z,|p|-n,r), plus inverse arrows. Empty histories retain
all objects. This is a countable, exact, untruncated incoming/outgoing description.

Nonzero source isotropy means two distinct legal iterates agree and hence the
history eventually enters a genuine cycle. If its least source period is h,
the ENTIRE source isotropy is hZ; otherwise it is0, including terminal histories.
On that cycle put P_C=product_(j<h) J_j. Common transient factors cancel, giving

    c(kh)=-k log P_C,    H=(-log P_C)Z.                       (5)

If P_C!=1, primitive positive time is abs(log P_C), repetitions are its positive
integer multiples, and extension isotropy is0. If P_C=1, H=0 but all hZ survives
in the extension. The lag kernel inside source isotropy is0 in either case.
This is a conditional full ledger, not an enumeration of untested cycles.

All X times R and arrows(w,t)->(z,t+c) remain. Height translation commutes with
every arrow for all real times. If F^r z=F^n a, phase relative to a is
t+S_n(a)-S_r(z) modulo H_a; alternative transports differ by that entire group.
Thus all phases over a source orbit are R/H_a. No Hausdorff, smooth, conservative
or Hamiltonian coarse quotient is claimed. Equal times do not merge actual orbits.

## 5. Exhaustion of ALL roots in the six whole cells

A fixed root must satisfy(z-c)(z-b)=A0, followed by its exact source-cell test.
A root cannot equal b because A0!=0, so multiplying introduces no legitimate
pole solution. The cell constants are

| (n,d) | q | r | a |
|---|---|---|---|
| (-1,-1) | 1 | 0 | -1-i |
| (0,-1) | 0 | 0 | -i |
| (0,1) | 0 | 0 | i |
| (1,1) | 1 | 0 | 1+i |
| (4,2) | 2 | 0 | 4+2i |
| (5,2) | 2 | 1 | 5+2i |

The following table lists BOTH algebraic roots in every case. Each ± includes
both signs, not a chosen branch. Put u=1/sqrt2 and p=u(1-i).

| Cell | MAIN roots | Q roots | R roots | A roots |
|---|---|---|---|---|
| (-1,-1) | i,1-i | ±sqrt(-1-i) | i,1-i | (1±sqrt5)/2 |
| (0,-1) | ±p | ±p | ±p | ±1 |
| (0,1) | ±u(1+i) | ±u(1+i) | ±u(1+i) | ±1 |
| (1,1) | (1±sqrt(5+4i))/2 | ±sqrt(1+i) | (1±sqrt(5+4i))/2 | (1±sqrt5)/2 |
| (4,2) | 1±sqrt(5+2i) | ±sqrt(4+2i) | 1±sqrt(5+2i) | 1±sqrt2 |
| (5,2) | (2+i±sqrt(23+4i))/2 | (i±sqrt(19+8i))/2 | 1±sqrt(6+2i) | (2+i±sqrt(7-4i))/2 |

Exact exclusions (no decimal root approximation is used):

- In(-1,-1), i and1-i fail respectively the imaginary and real cuts.
  The square roots of -1-i have opposite signs on their two coordinates, whereas
  this cell requires both negative. A's real roots lie outside its imaginary interval.
- In(0,-1), exactly p has 0<Re p<1 and -1<Im p<0. The negative root has
  negative real part. In(0,1), the positive root's imaginary part u<1 fails
  the lower cut, and the negative root also fails. A's real roots fail both cells.
- If sqrt(5+4i)=U+iV with U,V>0, V^2=(sqrt41-5)/2<1. Hence both MAIN/R
  roots in(1,1) have imaginary part<1. For Q, the positive square root of1+i
  has imaginary square(sqrt2-1)/2<1; its negative has negative imaginary part.
  A's roots again have imaginary part0. None is in(1,1).
- In(4,2), the positive real part of sqrt(5+2i) has square(sqrt29+5)/2<9,
  so MAIN/R roots have real part<4. For sqrt(4+2i) the positive real part
  has square(sqrt20+4)/2<16, so Q roots also have real part<4. A's roots are real.
- In(5,2), the positive real parts U of the radicals in the MAIN,Q,R,A columns
  respectively satisfy U^2=(sqrt545+23)/2<25, (sqrt425+19)/2<25,
  (sqrt40+6)/2<9, and(sqrt65+7)/2<9. The displayed root formulae therefore
  give real parts respectively<7/2,<5/2,<4,<5/2, all strictly below5.

Thus the COMPLETE fixed-window sets are {p} for each of MAIN,Q,R, and empty
for A. At p the actual readouts are n=0,d=-1,q=0,r=0,a=-i. In each of
MAIN/Q/R, F(p)=-i/p=p, all denominators are nonzero and all source checks pass.
No other root from the table is silently reassigned a different cell to rescue it.

## 6. Full incoming and all groups for the found cores

For EACH F in{MAIN,Q,R}, its entire source orbit/basin of p is exactly

    B_F={theta_(j_k)^F ... theta_(j_1)^F(p): k>=0,
         j_l=(n_l,d_l), d_l!=0, every intermediate test(1) passes}.       (6)

This is an explicit whole-source parameterization, not a restriction to six cells:
each theta is the displayed rational function, and its real inequalities are(1).
Equivalently a branch has matrix [[b,A0-bc],[1,-c]]; a finite product gives
(A p+B)/(C p+D), with all original intermediate pole/cell tests still mandatory.
This supplies every finite generation, not a cutoff or a claim that p is its
only predecessor. Conversely any arrow to a fixed core gives a finite forward
hit, so (6) exhausts every ancestor and its source orbit. The three B_F are
owned separately and are not assumed equal merely because the core is the same.

At p, abs(p)=abs(a)=1 and b=c=0 for all three owners; (2) gives J(p)=1 and
kappa(p)=0. For z in B_F let h_F(z) be its first forward hit of p and
b_F(z)=P_(h_F(z))(z), with b_F(p)=1. Every pair in B_F supports every integer
lag, by padding histories at p. Its exact full-arrow clock is

    c(z,k,w)=log b_F(w)-log b_F(z).                           (7)

Hence EVERY source in B_F has source isotropy Z, ENTIRE H=0 and extension
isotropy Z. The restricted lag kernel is the zero-lag pair relation; the clock
kernel imposes b_F(z)=b_F(w); their intersection imposes both. Transient arrows
are not assumed to have zero clock just because the core clock does.
All extension phases are the real invariant t+log b_F(z), with complete height
translation on a line and no positive primitive. A has no found core needing
such a basin classification; its other histories retain sections2–4 unchanged.

## 7. Lineage, bounded decision and remaining scope

In the card's integer family n=N,d=D0, q=floor(N/D0) and r=N-qD0.
Since D0>0, r=0 iff D0 divides N. Both outcomes are legal on the whole cell,
with their own i r translation, q shift and a=N+iD0 numerator in MAIN.
Thus the stated Euclidean divisor readout enters actual feedback. This is not
a claim of canonical naturalness or a prime table hidden in external parameters.

All four owners pass the inverse/IMAGE/history checks. MAIN's complete frozen
fixed-cell window contains one source fixed core with H=0, hence no positive
primitive in that window. Neither this absence nor any control proves a global
no-cycle statement, a global wrong time, duplicate packet or failed coverage.
The strongest positive alternative is a legal positive MAIN packet outside this
window; it has not been established or excluded. Other fixed cells and all higher
periods remain unclassified here. End this short gate BOUNDED OPEN / FORK.
Strong naturalness and arbitrary-encoding risks OPEN; classical NOT APPLICABLE;
T3 NOT AUDITED; formal Route UNASSIGNED; B NOT INVOKED. No owner defect remains
unresolved in this audit. CP2/CP3 and author-surface access await separate unlock.

EOF — card-only raw proof, frozen after complete self-read and lock checks.
