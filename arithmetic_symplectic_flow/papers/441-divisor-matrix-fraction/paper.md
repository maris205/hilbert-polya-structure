# A noninteger fixed return of a divisor-matrix fraction

Candidate ID: ANG-20260923-DMF01.
Outcome: OWNED MATRIX-FRACTION IMAGE; NONINTEGER FIXED RETURN — STOP / FORK
Batch ADMISSION-CLOCK-20260923-S, round 441.
Frozen session: 2026-09-23; author completion: 2026-09-24 UTC.
Type: ANG partial Borel transport with its full retained-lag IMAGE extension.
Classical fields NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED.
Route B NOT INVOKED. Strong naturalness remains OPEN.

## Abstract

The complete real matrix source uses current-entry divisibility to select
a numerator, and its moving matrix denominator feeds the next readout.
We prove every actual inverse branch and the prescribed four-dimensional,
every-point/every-Borel IMAGE clock for MAIN and its two separate controls.
In the frozen window \(2\le A_{11},A_{12}<3\), with the other two entries
unrestricted, MAIN and permission-off each have exactly one actual fixed
matrix, determined by a unique positive algebraic root. The moving-denominator-off
control has none in that window. At the MAIN core the whole return subgroup
has primitive \(4\log z\), where exact rational inequalities give
\(29<z^4<30\). This is not an ordinary-prime log. All incoming histories,
phases, source and extension isotropy remain; no chosen inverse, direction,
height or matrix subspace creates the result. No higher-period census is needed.

## 1. Frozen full source and precise lineage

Input: the original 104-line [candidate card](candidate-card.md), SHA256
773843abf3378c2bb2351f57b9a1c559f5243eefb9ce0e5d05e85e97e36da687.
The full carrier is \(X=M_2(\mathbb R)\), with usual Borel structure and
Lebesgue measure in the four original entries. Define
\[
 C=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 m=\lfloor A_{11}\rfloor,\quad n=\lfloor A_{12}\rfloor,\quad
 K_q=C-qJ.
\]
MAIN requires \(m\ne0,m\mid n\), sets \(q=n/m\), and additionally requires
\(\det(A+C)\ne0,\det K_q\ne0\). Its actual map is
\[
              T(A)=(A+qJ)(A+C)^{-1}=I-K_q(A+C)^{-1}.        \tag{1}
\]
All quotients are signed integers, including zero. Indeed
\(\det K_q=2-q^2\ne0\) for every integer \(q\); this verifies, rather than
changes, the frozen second geometric condition.
There is no invertibility, symmetry or positivity requirement on \(A\).
All illegal sources remain terminal objects with identities and all incoming.
No absorbing loop, infinity or new atom is introduced. Every floor face retains
its usual assignment, and a legal forward step may end at a terminal.

The owners and their complete legal domains are:

| Owner | Quotient and permission | Actual map / additional domain |
| --- | --- | --- |
| MAIN \(T\) | \(m\ne0,m\mid n,q=n/m\) | (1), \(\det(A+C)\ne0,\det K_q\ne0\) |
| \(G\), permission-off | \(q=\lfloor n/m\rfloor\) if \(m\ne0\), otherwise \(0\) | (1), only its own two geometric conditions |
| \(L\), moving-denominator-off | MAIN permission and quotient | \((A+qJ)C^{-1}\), with NO extra geometric condition |

For integers \(N\ge2,1<d<N\), the interface
\(A_{N,d}=\left(\begin{smallmatrix}d&N\\0&1\end{smallmatrix}\right)\)
has exact readings \(m=d,n=N\). If \(d\mid N\), its integer quotient is
\(q=N/d\), its denominator determinant is \(3(d+1)>0\), and
\(\det K_q\ne0\). Thus the complete MAIN step is legal exactly when \(d\mid N\).
This proves the full declared proper-divisor interface, not just its readout.
The quotient changes the actual numerator; the next integer reading is taken
from the actual matrix output. The source is not restricted to this interface.
Readout, matrices and volume are declared design choices; their strong
naturalness is unestablished. No prime table, fitted roof or zero input occurs.

## 2. Complete actual inverses and owned full-entry IMAGE

Fix any integer \(q\). The fractional map in (1) is a rational diffeomorphism
from \(\Omega=\{\det(A+C)\ne0\}\) onto
\(\Omega'=\{\det(I-B)\ne0\}\), with inverse
\[
 \theta_q(B)=(I-B)^{-1}K_q-C
            =(B-I)^{-1}(qJ-BC).                            \tag{2}
\]
In fact \(I-B=K_q(A+C)^{-1}\), and
\(\theta_q(B)+C=(I-B)^{-1}K_q\); these equations prove both inverse identities,
all geometric conditions and the exact image. The multiplication order matters.

For MAIN, enumerate every \(m\ne0,n\) with \(m\mid n\), insert its \(q=n/m\)
in (2), and restrict the target to exactly the reconstructed source floors
\(\lfloor(\theta_q B)_{11}\rfloor=m,\lfloor(\theta_q B)_{12}\rfloor=n\).
For \(G\), enumerate all integers \(m,n\), use its OWN quotient rule and the
same reconstructed-floor restriction. Keep each owner's own complete source
and forward checks. The inverse identities show their necessity and sufficiency.
There is no target-next-step legality test. Each actual source has its own
unique readings, so duplicate labels never create extra predecessors.
Different actual sources are retained even if their target agrees.

For \(L\), every fixed-\(q\) map is an affine diffeomorphism of all \(X\),
with inverse \(\theta^L_q(B)=BC-qJ\). Enumerate MAIN-admitted integer labels
and check the reconstructed source's own floors and quotient.
Neither \(\det(A+C)\) nor \(\det K_q\) is an \(L\) source or target restriction.
This is the complete actual inverse list; no integer or depth cutoff is used.

All these actual domains are Borel. Each branch is a restriction of the displayed
analytic diffeomorphism, hence its Borel images and actual target sets are Borel.
The countable source-floor partition covers every legal source, including all
integer faces. For MAIN and \(G\), matrices with \(\det(I-B)=0\) have no
predecessor, but remain objects and may have their own legal forward step.
No finite-fibre assertion is made for any owner.

For the fractional owners, write \(S=A+C\). Full matrix differentiation gives
\[
 DT_q(A)[H]=K_qS^{-1}HS^{-1},\qquad
 D\theta_q(B)[H]=(I-B)^{-1}H(I-B)^{-1}K_q.                  \tag{3}
\]
On all four real entries the map \(H\mapsto PHQ\) has determinant
\((\det P)^2(\det Q)^2\): left multiplication acts separately on two columns,
and right multiplication on two rows. Consequently
\[
 \delta_q(A)=\det_{\mathbb R^4}DT_q(A)
     =\frac{(2-q^2)^2}{\det(A+C)^4}>0,\qquad
 J_{\theta_q}(B)=\frac{(2-q^2)^2}{\det(I-B)^4}>0.            \tag{4}
\]
In particular the frozen geometry ensures full-dimensional regularity, with
no missing critical source inside the legal domain.
For \(L\), \(D\theta^L_q[H]=HC\), so its own inverse determinant is \(4\)
and its forward determinant is \(1/4\), on every actual branch.

Analytic change of variables now proves for EVERY Borel subset \(E\) of
each actual inverse target
\[
                 \mu(\theta E)=\int_E J_\theta\,d\mu.       \tag{5}
\]
The displayed germs assign these positive finite densities at every retained
integer face, not merely almost everywhere. Equivalent charts returning the
same source have the same quotient and derivative, so no extra null-set
choice is needed. An image union is not an uncorrected sum of overlapping images.
Each legal owner therefore has its own signed step clock
\[
 \kappa_O(A)=2\log|2-q_O(A)^2|-4\log|\det(A+C)|
 \quad(O=T,G),\qquad \kappa_L=-\log4.                      \tag{6}
\]
with each fractional formula evaluated using THAT owner's actual quotient.
Terminal next-step clocks remain undefined, not artificially zero.

## 3. All fixed points in the entire frozen window

Let \(W=\{2\le A_{11}<3,2\le A_{12}<3\}\), with the other entries arbitrary.
Each owner has \(m=n=2,q=1\) throughout this window. For MAIN and \(G\),
write \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\),
and \(t=a+d\). Any actual fixed matrix must satisfy
\[
 a^2+bc=0,\quad b(t+1)=1,\quad ct=1,\quad d^2+d+bc=0.       \tag{7}
\]
These are the four entries of \(A(A+C)=A+J\), without a matrix ansatz.
Since \(2\le b<3\), \(t\in(-2/3,-1/2]\).
The first and last equations give \(a^2=d^2+d\), hence
\(a(2t+1)=t(t+1)\). Thus \(t=-1/2\) is impossible.
Put \(u=-t(t+1)>0\). Then \(bc=-1/u\), \(a^2=1/u\), and \(a>0\).
With \(r=\sqrt u\), these identities imply
\[
 a=1/r,\quad 2t+1=-r^3,\quad
                 f(r):=r^6+4r^2-1=0.                     \tag{8}
\]
The function \(f\) is strictly increasing for \(r>0\), so at most one
positive root, and thus at most one actual fixed matrix, is possible.

Here are exact root bounds, not a numerical root computation:
\[
                 \frac{99}{200}<r<\frac{149}{300}<\frac12. \tag{9}
\]
Indeed \(f(99/200)<1/64+9801/10000-1<0\).
At \(v=149/300\), \(v^2>6/25\), so
\(f(v)>216/15625-1196/90000>0\).
Continuity and strict monotonicity prove existence and (9).
Define the candidate entirely by that unique root:
\[
 t=-\frac{1+r^3}{2},\qquad
 A_\circ=
 \begin{pmatrix}
  1/r&1/(t+1)\\
  1/t&t-1/r
 \end{pmatrix}.                                           \tag{10}
\]
Equation (8) implies \(t(t+1)=-r^2\) and
\(a(2t+1)=t(t+1)\), which verify every equation in (7).
Moreover \(2<a<3\); and \(b=2/(1-r^3)\) lies strictly between \(2\) and
\(16/7<3\). Thus all readout conditions hold strictly inside \(W\).
The polynomial fixed equation also gives
\((I-A_\circ)(A_\circ+C)=C-J\), whose determinant is \(1\).
Hence both factors are invertible: the reconstructed root is actually legal
and fixed for EACH fractional owner, not an extraneous denominator root.
We have proved the ENTIRE MAIN and \(G\) fixed sets in \(W\) are each
\(\{A_\circ\}\). In particular no lower window face was silently removed.

For \(L\), fixedness in \(W\) would require \(A(C-I)=J\).
Its left side has first column zero, while \(J_{21}=1\).
There is no such matrix, including every window boundary.
Thus \(\operatorname{Fix}(L)\cap W=\varnothing\), without applying either
fractional geometric restriction to \(L\).

## 4. Exact fixed clock and the noninteger return exponent

Using (7), \(\det A_\circ=at\). Its moving denominator determinant is
\[
 z:=\det(A_\circ+C)=at+2a+d+2
  =1+(a+1)(t+1)=\frac{r^{-1}+3-r^2-r^3}{2}.                \tag{11}
\]
We next prove bounds strong enough to decide the prime test:
\[
                 \frac{65}{28}<z<\frac73,\qquad
                         29<z^4<30.                      \tag{12}
\]
The expression on the right in (11) is strictly decreasing for positive \(r\).
At \(v=149/300\), the inequality \(z(v)>65/28\) reduces to
\[
 \frac{773}{2086}>\frac{9968249}{27000000};
 \quad 773\cdot27000000-9968249\cdot2086=77232586>0.
\]
This and (9) prove the lower bound. Also (9) implies
\(r^2>6/25,\ r^3>3/25,\ 1/r<200/99\). Therefore
\(2z<200/99+66/25<14/3\), proving the upper bound.
Finally \(65^4-29\cdot28^4=25601>0\), and \(7^4=2401<30\cdot3^4=2430\).
All bounds use exact rational inequalities; no scientific numerical sampling occurs.

At either fractional fixed core, \(q=1,\det K_1=1\).
The OWN full inverse density, forward determinant and signed clock are
\[
             J_{\rm actual}=z^4,\quad
             \delta_{\rm actual}=z^{-4},\quad
             C_\circ=-4\log z<0.                          \tag{13}
\]
This is the four-entry determinant, not a directional rate or half-clock.
To determine the actual primitive, rather than just a selected loop value,
we now retain the complete history and entire isotropy image.

## 5. Full history, all incoming and whole packet conventions

For each actual owner \(F\), let legal \(F^r\) mean exactly \(r\) defined
steps; \(F^0\) is defined at every object. Let \(D_F^{(r)}\) be that Borel domain,
\(M_r(A)\) the product of its OWN forward densities (4) or \(1/4\),
\(M_0=1\), and \(S_r=\log M_r\).
Retain all triples
\[
 {\cal G}_F=\{(A,r-s,B):F^rA=F^sB\text{ legally},\ r,s\ge0\},
 \qquad c_F=\log\frac{M_r(A)}{M_s(B)}.                     \tag{14}
\]
Source is \(B\), range is \(A\); equal triples are one arrow, different lags remain.
The relation is Borel by countable unions of equalities of Borel iterates.
Composition aligns the two middle trajectories at their larger time, using
only known legal segments; inversion reverses source, range and lag.
Two representations of the same triple differ by a common time advance;
their extra clock sums at the common endpoint cancel. This proves descent,
and the same alignment proves the cocycle law.
The forward arrow \((FA,-1,A)\) has clock \(-\kappa_F(A)\).
Every finite actual branch history has IMAGE density \(e^{-c_F}\) by composing
(5); assigned face values use the same composed germs.

The full lag kernel consists of (14) with \(r=s\); the full clock kernel
has \(M_r(A)=M_s(B)\); the joint kernel has both conditions.
For \(L\) specifically, \(c_L=-(r-s)\log4\), so its clock and joint kernels
are exactly its lag kernel, not presumed to be units.
For every owner, let \(P_1^F(Y)\) be ALL actual inverses established in Section 2.
Set
\[
       P_0^F(Y)=\{Y\},\qquad
       P_{j+1}^F(Y)=\bigcup_{Z\in P_j^F(Y)}P_1^F(Z).        \tag{15}
\]
Induction gives \(P_j^F(Y)=\{A:F^jA=Y\text{ through }j\text{ legal steps}\}\).
This is unrestricted in integers and depth, including terminal targets.
For any range \(A\), every arrow is obtained by choosing legal \(F^rA\),
any \(s\ge0\), and every \(B\in P_s^F(F^rA)\), with lag \(r-s\).
Thus every source orbit, all finite histories and all compatible infinite
inverse histories are retained. Different witnesses of one triple do not
create extra packet labels.

A source point is isotropic with nonzero lag exactly when it is eventually
periodic: an equality of distinct iterates forces a legal indefinitely
repeating cycle. For eventual least period \(p\), its source isotropy is
\(p\mathbb Z\); comparing sufficiently late iterates realizes all multiples,
and least periodicity excludes any other lag.
If the actual clock around that cycle is \(C_\gamma\), the ENTIRE image is
\(H_A=C_\gamma\mathbb Z\), since all preperiod sums cancel.
For non-eventually-periodic points, including terminals and eventual terminals,
source isotropy and \(H_A\) are trivial. This is a general exact ledger,
not an existence or census claim for higher cycles.

The full extension has arrows \((B,h)\mapsto(A,h+c_F)\), all real heights,
and isotropy given by \(kp\) with \(kC_\gamma=0\).
Physical height translation is defined on its orbit SET, with return group
exactly \(H_A\) and all phases \(\mathbb R/H_A\); no nice quotient is assumed.
For an actual arrow \(g_A:A\to b\), phase transport is
\(h+c_F(g_A)\bmod H_b\), independent of the chosen arrow modulo the entire \(H_b\).
Extension lag-kernel arrows have \(r=s\), possibly changing height; clock-kernel
arrows have \(M_r(A)=M_s(B)\) and preserve height. Joint-kernel arrows satisfy
both conditions. These are the full lifted kernels with the actual height equation.

For the unique fixed core \(Y=A_\circ\) in each fractional owner's window,
its whole source packet is exactly
\({\cal B}_Y=\bigcup_{j\ge0}P_j^F(Y)\), not merely the point in \(W\).
Tail equality with a fixed core is precisely eventual entry.
Different fixed cores, if present elsewhere, cannot share this basin.
Let \(d(A)\) be first entry and \(\beta(A)=S_{d(A)}(A)-d(A)C_\circ\).
Then \(S_r(A)=\beta(A)+rC_\circ\) once \(r\ge d(A)\);
every pair of basin points admits every integer lag, by comparing late iterates.
Consequently on this ENTIRE basin,
\[
 c_F(A,k,B)=\beta(A)-\beta(B)+kC_\circ,\qquad
 {\cal G}_{F,A}^{A}\simeq\mathbb Z,\qquad H_A=C_\circ\mathbb Z. \tag{16}
\]
Its lag kernel is \(k=0\), clock kernel is
\(\beta(A)-\beta(B)+kC_\circ=0\), and joint kernel is \(k=0,\beta(A)=\beta(B)\).
The extension isotropy is trivial because \(C_\circ\ne0\).
All phases are \(h-S_{d(A)}(A)\bmod C_\circ\mathbb Z\), equivalently
\(h-\beta(A)\) modulo the same group.
Neither \(W\) nor \(q=1\) is imposed on the incoming points in (15).
MAIN and \(G\) use their different complete inverse permissions separately.

It follows that the positive primitive is the least generator of the WHOLE
group, namely \(L_\circ=|C_\circ|=4\log z\); all repetitions are integer multiples.
By (12), its exponential lies strictly between \(29\) and \(30\), so it is not
even an integer, hence not an ordinary prime. The negative signed clock does
not remove this positive return: reverse isotropy provides the opposite sign.
There is one fixed-core packet in the MAIN window, with all incoming and
all physical phases, rather than one packet per height or per chosen inverse.
No higher-period or outside-window source is classified or needed for this stop.

## 6. Controls, decision and integrity boundary

The same-object source, four-entry measure, actual germs, whole \(H\) and
packet multiplicity remain intact. T0 inverse/IMAGE/history ownership is
established; MAIN's positive ledger is nonempty but already violates the
ordinary-prime purity requirement. Arithmetic T1 is NOT PASSED and the
T2 prime target fails. Higher-period multiplicity and full-prime coverage
outside the frozen window remain UNCLASSIFIED, not rescued by this core.
The permission-off owner has the same bad window return on its OWN ledger:
this is a PROVES_TOO_MUCH warning, not arithmetic success.
\(L\) has its own density and no fixed point in \(W\); its behavior cannot
supply MAIN with a substitute time. Strong naturalness remains OPEN.
Classical fields NOT APPLICABLE; T3 NOT AUDITED; formal Route UNASSIGNED;
Route B NOT INVOKED. Decision: STOP / FORK, with no parameter or clock repair.

Methods were exact matrix algebra, full-coordinate differentiation and
change of variables, monotonicity and rational inequalities, and complete
partial-map history identities. No scientific code, numerical census,
external source, operator, Git/PDF action or higher-cycle enlargement was used.
The author fully read the original frozen card before proof. An author-side
helper read only that 104-line card to check \(G,L\) fixed sets and their own
four-dimensional IMAGE; the author independently derived and checked the
MAIN algebra, exact noninteger bound and whole-history proof.
This helper is not an independent review seat. No scope/raw/peer material was read.

Prior definition access and SHA locks are recorded in the card: 435 summary
1–107 EOF, 316 card 1–110 non-EOF, 385 card 1–61 through original definition
EOF but not appended-file EOF. Outcome headings and the 316 provenance
references were exposed. Prior 316/411/431/436 authorship and shared history
remain disclosed; no global novelty or nonconjugacy claim is made.
Pre-freeze informal fixed/derivative algebra informed the choice of \(W\);
this was not blind discovery or sealed preregistration.
AI agents supplied derivation, drafting and internal checking; same-model
shared-history work is NOT_CALIBRATED, with no certified human/external
verification or independent peer validation.

The [claim ledger](claim-ledger.md) and [README](README.md) summarize this
complete proof. Root owns the card outcome and separate review integration.
The root-owned [internal review record](evidence/review.md) is separate;
the author has not read it or credited its conclusions here.
