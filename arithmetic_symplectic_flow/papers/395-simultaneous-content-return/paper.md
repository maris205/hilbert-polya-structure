# Simultaneous content return: an owned planar clock and a wrong primitive

**Candidate:** `ANG-20260922-SCR01`; paper395, 2026-09-22.
Outcome: `OWNED 2D IMAGE CLOCK; NONINTEGER PRIMITIVE — STOP / FORK`

The full Borel/IMAGE owner is established; prime-time target fails; strong naturalness OPEN.
No global census/coverage claim. Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

Two real coordinates generate reciprocal/ratio digits whose gcd normalizes both
next remainders. Every branch has a positive finite prescribed all-point Lebesgue
IMAGE density, including null cuts and axes. The complete retained-lag extension,
eventual-cycle ledger and four frozen fixed-cell sets are determined for all owners.
MAIN's retained axis has primitive multiplier 2+sqrt(5), not an integer prime.
No roof, null-version change or selected subsystem is introduced to remove it.

## 1. Full source, arithmetic execution and own controls

The [frozen card](candidate-card.md) specifies X=[0,infinity)^2 with its usual
Borel structure and two-dimensional Lebesgue mu. Put gamma(a,b)=gcd(a,b)
except gamma(0,0)=1, so d=gamma(a,b) is always a positive integer.
For MAIN (M), D and R, x=0 is terminal, but x>0,y=0 remains active.
For S both axes are terminal. No terminal receives a forward self-loop.
All nonnegative digits, unbounded states, units, cuts and zero remainders remain;
an empty history is legal at every point.

| Owner | Current digits on its active domain | Actual next state |
|---|---|---|
| M | a=floor(1/x), b=floor(y/x), d=gamma(a,b) | ((1/x-a)/d,(y/x-b)/d) |
| D CONTENT-OFF | a=floor(1/x), b=floor(y/x) | (1/x-a,y/x-b) |
| R RATIO-OFF | a=floor(1/x), b=floor(y), d=gamma(a,b) | ((1/x-a)/d,(y-b)/d) |
| S SPLIT-RECIPROCAL | a=floor(1/x), b=floor(1/y), d=gamma(a,b) | ((1/x-a)/d,(1/y-b)/d) |

Each owner is an autonomous partial Borel map into its SAME full X. Floor assigns
every cut to its half-open remainder interval [0,1); no boundary branch is
unspecified and no prime filter acts.
For MAIN and integers 1<=m<n, the whole cell (x,y)=(1/(n+rho),(m+eta)/(n+rho)),
0<=rho,eta<1, has digits(n,m). Thus m|n is exactly gcd(n,m)=m;
the same d changes both remainders. This proves the divisor-symbolic interface,
not a claim that the chosen common denominator or normalization is canonical.

## 2. Exhaustive inverses and every-Borel IMAGE

At target(u,v), write A=a+d u,B=b+d v for M/R/S; for D write
A=a+u,B=b+v. Enumerate EVERY pair a,b>=0, with its prescribed d.

| Owner | Inverse theta_ab(u,v) | Exact target domain | J_theta(u,v) |
|---|---|---|---|
| M | (1/A,B/A) | 0<=d u,d v<1, A>0 | d^2/A^3 |
| D | (1/A,B/A) | 0<=u,v<1, A>0 | 1/A^3 |
| R | (1/A,B) | 0<=d u,d v<1, A>0 | d^2/A^2 |
| S | (1/A,1/B) | 0<=d u,d v<1, A>0,B>0 | d^2/(A^2 B^2) |

These inequalities imply all frozen source checks. For M the reconstructed
reciprocal and ratio are A=a+d u and B=b+d v; their floors are exactly a,b,
and substitution returns(u,v). D is the same verification with scale1.
For R the reconstructed y itself is B; for S its reciprocal is B.
Their floors and forward identities follow from their own displayed bounds.
Conversely any actual source has unique floor digits; solving its two
equations gives precisely the displayed inverse and bounds. Hence this is
the complete predecessor list, with no duplicate source from different digits.

This includes incoming to terminals: u=0 requires a>0 in M/D/R, and S's
zero target coordinates require the corresponding positive digit. Otherwise
apply all inequalities unchanged. Empty inverse domains do not delete a target.
There are no predecessors outside [0,1)^2, but all such sources remain. The formulas, not
a bounded integer search, specify all terminal incoming and all other branches.

On the ambient open sets where their denominators are positive, these
rational maps have smooth injective inverses. Differentiation gives the
table: M's determinant is -d^2/A^3, R's is -d^2/A^2, S's is
d^2/(A^2 B^2), and D uses d=1 in M. Every displayed absolute value is
finite and positive at EVERY retained point of its branch domain.
Successive one-variable substitutions in the first coordinate and the linear
second coordinate (reciprocal for S), with Fubini, prove

    mu(theta E)=integral_E J_theta dmu

for every Borel subset E of the exact domain, including cuts and axes: restrict
the ambient change-of-variables identity to E. Both sides may be infinite.
The all-point values are the stipulated rational-extension derivatives, not
forced by an a.e. identity alone. No null-version or measure is changed.

## 3. Actual histories, clock and both global kernels

For each owner, G consists of the frozen triples(z,m-n,w) with legal
T^m z=T^n w, m,n>=0, source w and range z; equal triples are equal arrows.
Its Borel structure is inherited from X times Z times X. Finite-history
domains and their endpoint equalities are Borel. At source r enumerate each
legal T^n r, then every finite inverse word of length m whose intermediate
domains ALL pass. If its output is q, this gives exactly(q,m-n,r), outgoing
from r. Taking inverses gives ALL arrows incoming to r. The empty word is
included; no length or digit cutoff is imposed. Thus source/range fibres
are countable, including at every terminal.

Inversion swaps endpoints and negates lag. For composable witnesses with
intermediate histories of lengths n and p, extend the shorter equality to
the longer already-existing history. This proves closure with added lag,
without continuing past a terminal. Equality of triples makes composition
associative and independent of the chosen common-history witnesses.

For a legal history of length m define D_m=product_(i<m)d_i,
X_m=product_(i<m)x_i, Y_m=product_(i<m)y_i; empty products are1.
D omits D_m, and Y_m is used only for S's interior histories. The inverse
branch Jacobian product evaluated along this history is

    K_m^M=D_m^2 X_m^3,    K_m^D=X_m^3,
    K_m^R=D_m^2 X_m^2,    K_m^S=D_m^2 X_m^2 Y_m^2.

All are positive finite. Consequently S_m=-log K_m, exactly the frozen
sum of kappa=-log J_theta(Tz), and on every actual arrow

    ell(z,m-n,w)=m-n,    c(z,m-n,w)=log[K_n(w)/K_m(z)].

Changing witnesses by adding a common tail multiplies both K products by
the same factor; any two witnesses of the same lag align this way. Thus c
is all-point presentation-independent. Aligning composable histories proves
additivity, and inversion negates c. For the associated actual branch pair
w->z, the IMAGE density is K_m(z)/K_n(w), by the chain rule and the
every-Borel identities above. Hence c is the negative log of this SAME owner.

The complete global kernels are now explicit, not conflated with isotropy:
ker ell consists of triples(z,0,w) admitting T^m z=T^m w;
ker c consists of all legal triples with K_m(z)=K_n(w);
their intersection consists of the former triples with K_m(z)=K_m(w).
These owner-specific monomial tests cover every source and incoming branch,
without a periodic census. Unit lag is not unit time; kappa need not be positive.

## 4. Full isotropy, return groups, packets and phases

A source has nonzero isotropy exactly when its actual forward history is
eventually periodic. If the eventual cycle has least length p, its full
source isotropy is pZ; otherwise it is{0}, including every terminal and
every history that terminates. Indeed a repeated actual iterate yields a
cycle, and conversely every multiple of p is witnessed after the transient.
There are no additional labelled-word or germ stabilizers.

Every actual cycle has a strictly positive total clock. To see this without
a census, take products D,X,Y over ONE least cycle. M/R satisfy
d_i x_(i+1)<1, so DX<1 and X<1; D has X<1. The respective cycle
multipliers exp(tau) are 1/(D^2 X^3),1/X^3,1/(D^2 X^2), all >1.
For S, both d_i x_(i+1)<1 and d_i y_(i+1)<1 hold. Thus
D^2 XY<1 and exp(tau)=1/(D^2 X^2 Y^2)=D^2/(D^2 XY)^2>1.
This uses legal cycles only; no terminal is made periodic.

For an eventual cycle, c on its source isotropy sends kp to k tau.
Therefore H_z=tau Z with least positive tau, and isotropy intersect ker c
is trivial. For a noneventually-periodic source H_z={0}. Extension isotropy
is trivial at EVERY(z,h), while the full groupoid ker c can still connect
different units and remains exactly the product-equality relation in section3.

All X times R is retained, with(w,h)->(z,h+c) and height translation.
A translated point is equivalent to itself precisely for t in H_z (the
sign convention gives the same subgroup). Over each complete G-orbit the
time action is R/H_z: a line if H_z={0}, a circle of length tau otherwise.
To describe phases, an arrow w->z sends height h to h+c modulo H_z;
different choices differ by isotropy, so every phase is retained consistently.
No replacement source or preferred phase is chosen. Entire preperiodic incoming
basins belong to their actual cycle packet. Distinct equal-time cycles are not
identified: a common forward iterate would put them on the same cycle.
Repetitions are k tau within that packet; no nice coarse topology is asserted.

## 5. Complete fixed sets in the four frozen cells

Put alpha=(sqrt(5)-1)/2, beta=sqrt(5)-2,
rho=(sqrt(3)-1)/2 and sigma=(sqrt(6)-2)/2. The COMPLETE sets are:

| Owner | (a,b)=(1,0) | (1,1) | (2,2) | (4,2) |
|---|---|---|---|---|
| M | {(alpha,0)} | empty | empty | empty |
| D | {(alpha,0)} | empty | empty | {(beta,alpha)} |
| R | {(alpha,t):0<=t<1} | empty | empty | empty |
| S | empty | {(alpha,alpha)} | {(rho,rho)} | {(sigma,rho)} |

Here is an exhaustive derivation, including all cuts. In M put
f(x)=d x^2+a x-1; it is strictly increasing for x>=0 in these cells,
with exactly one positive root r. The second equation is
y(1-d r)=b r. For b=0 in(1,0), r=alpha and y=0. For b>0,
nonnegativity and the strict digit bound d y<1 require
r<1/[d(b+1)]. At that threshold f equals -1/4,-11/18,-5/18
in the other three cells, respectively. Their root lies ABOVE the threshold,
so none is legal. There is no missing denominator-zero solution with b>0.

D replaces d by1 in these equations. In the three b>0 cells the threshold
values are -1/4,-2/9,4/9. Only(4,2) is admitted; r=beta and
y=2 beta/(1-beta)=alpha. R instead has(d-1)y=-b. Thus(1,0)
retains exactly the entire floor(y)=0 interval, including0 and excluding1;
the other cells have b>0,d>=1 and no nonnegative solution. S requires
the two unique positive roots of d x^2+a x-1 and d y^2+b y-1,
and both strict inequalities d x,d y<1. In(1,0) it gives y=1,
which violates the b=0 cut. The three displayed positive pairs satisfy
their own strict inequalities. Terminal axes are not extra S fixed points.

Each nonempty entry has least source cycle1. Its primitive multiplier is:

| Fixed source(s) | exp(tau) |
|---|---|
| M(alpha,0); D(alpha,0) | alpha^(-3)=2+sqrt(5) |
| D(beta,alpha) | beta^(-3)=38+17 sqrt(5) |
| R(alpha,t), every 0<=t<1 | alpha^(-2)=(3+sqrt(5))/2 |
| S(alpha,alpha) | alpha^(-4)=(7+3 sqrt(5))/2 |
| S(rho,rho) | 1/(4 rho^4)=7+4 sqrt(3) |
| S(sigma,rho) | 1/(4 sigma^2 rho^2) |

All incoming and phases are those already proved, with no finite cutoff.
Distinct fixed sources cannot share a forward iterate; R therefore retains
a continuum of different packets with the same multiplier, not one selected
representative. Controls are separate owners and cannot repair MAIN.

## 6. Necessary-target stop and evidence boundary

MAIN's retained(alpha,0) has H=log(2+sqrt(5)) Z, so this is its actual
least primitive, not a multiple or a branch label. The multiplier is
noninteger, hence cannot be an ordinary integer prime. This single allowed
axis packet refutes the card's necessary prime-time target and decides STOP.
No larger periodic census, second-cycle search, time rescaling, measure
change, axis deletion, prime coverage or trace/operator audit is performed.

The author read the final card1–93 through actual EOF (wc93), SHA256
`d2c74a3fda2d7cc57840bb66a7d367d8dd5852643254a721facb19dbb899d606`.
Root reported CP1 acceptance and released this derivation; no CP1/raw/peer was read.
Earlier inputs:313-card1–102;386-card1–55 (ORIGINAL EOF marker, not current EOF).
313 included its309 historical-result summary; headings exposed313's outcome
title180 and386's title68 plus full status71, all disclosed before freeze.
No old proof/outcome body, clock or Route result is used; no old total/hash measured.
Prior source authorship/shared history: internal NOT_CALIBRATED, not blind or external
peer review; no global novelty/nonconjugacy claim. Retained ARS guidance governed
owner/claim and review boundaries. Proofs use the card's explicit formulas, with
no scientific code/numerics, web, Git mutation or publication. Naturalness and unexamined global arithmetic remain OPEN. See the [ledger](claim-ledger.md).
