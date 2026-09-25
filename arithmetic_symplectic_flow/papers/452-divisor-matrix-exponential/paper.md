# An owned matrix-exponential clock with a noninteger fixed return

Candidate ID: ANG-20260924-DME01. Paper 452, version 1.
Outcome: OWNED MATRIX-EXPONENTIAL IMAGE; NONINTEGER FIXED RETURN — STOP / FORK
Date: 2026-09-24. Batch TRANSPORT-PACKET-20260924-U, round 3/5.
Type: measured Borel partial map, retained-lag groupoid and real cocycle extension.
Classical symplectic/suspension fields: NOT APPLICABLE. T3: NOT AUDITED.
Formal Route coordinates: UNASSIGNED. Route B: NOT INVOKED.

## Abstract

We study the matrix exponential driven by the current quotient of two floor
readouts, on all four real matrix entries with their original Lebesgue measure.
The full Fréchet derivative, all real-matrix-logarithm inverses, countable
analytic atlas and every-Borel image formula provide an owned pointwise
clock, including the prescribed values at null and floor-boundary objects.
We classify the global fixed sets of MAIN and both separate controls without
a diagonal ansatz. MAIN's full fixed-basin period group has positive generator
strictly between \(\log4\) and \(\log5\). Hence the generator is not the
logarithm of any integer, in particular not a prime logarithm. All real
inverse roots, incoming depths, source/extension isotropy and phases are
retained. This adverse packet stops the candidate; no higher-period census,
parameter adjustment or auxiliary roof is used.

## 1. Frozen source, scope, and arithmetic interface

The [candidate card](candidate-card.md), original lines 1–98 through its EOF
marker, is the governing input. Its exact-prefix SHA256 is
af564b868a621a58d73ccfda5ecde88ef3265d27062bf1e9d93730693730a1f9.
The [claim ledger](claim-ledger.md) records the claim boundaries; the later
[review record](evidence/review.md) is root-managed and not an author input.

Let \(X=M_2(\mathbb R)\), with its usual Borel structure and Lebesgue measure
\(\mu_4\) in the four original entries. Put \(C=\operatorname{diag}(-1,-2)\).
At the current matrix \(A\) read
\[
m=\lfloor A_{11}\rfloor,\qquad n=\lfloor A_{22}\rfloor.
\]
MAIN requires \(m\ne0,\ m\mid n\), and uses \(q=n/m\). Its fixed-label map is
\[
F_q(A)=e^{qA}C.                                         \tag{1}
\]
The exponential is the convergent matrix power series, not an entrywise
function. The actual legal domain further requires the full real
four-dimensional derivative determinant of (1) to be nonzero.

The permission-OFF owner G uses
\[
q_G(m,n)=
\begin{cases}\lfloor n/m\rfloor,&m\ne0,\\0,&m=0,\end{cases}
\]
and \(F_{q_G}\), with its own derivative guard but no divisibility requirement.
The exponential-linearized owner L retains MAIN's arithmetic permission but
uses its own fixed-label map
\[
F^L_q(A)=(I+qA)C                                       \tag{2}
\]
and its own full derivative guard. All three owners retain the entire \(X\),
measure, actual inverses, incoming histories and pointwise clock convention.

No singular, nonsymmetric, noncommuting, negative, zero, unit-readout or
floor-boundary object is deleted. A point failing its owner's permission or
guard has its unit but no outgoing step or next-step clock. Such a terminal
can have actual incoming arrows; it is not an absorbing fixed point.
Target outgoing permission is never an inverse-source condition.

For integers \(N,d\) with \(N\ge2,\ 1<d<N\), the seed
\(A=\operatorname{diag}(d,N)\)
has MAIN arithmetic permission exactly when \(d\mid N\). Section 2 verifies
the additional geometry when admitted. The preserved interface is proper-
divisor symbolic admission, followed by a quotient inside an actual matrix
function, non-scalar right multiplication and a fresh readout of the output.
There is no independent static integer register or prime table.
The readout positions and \(C\) are declared design choices; this interface
alone does not prove their canonical naturalness.

## 2. Full four-dimensional Fréchet derivative

On compact matrix sets the exponential series and its termwise derivative
converge uniformly. Indeed the norm of the differentiated degree-\(k\) term
is at most \(|q|^k k\|A\|^{k-1}\|H\|/k!\).
Consequently the derivative of (1), on unrestricted \(H\in M_2(\mathbb R)\), is
\[
\mathcal D_q(A)[H]
=\sum_{k=1}^{\infty}\frac{q^k}{k!}
       \sum_{j=0}^{k-1}A^jHA^{k-1-j}\,C
=q\int_0^1 e^{(1-t)qA}H e^{tqA}\,dt\,C.               \tag{3}
\]
Expanding both exponentials and integrating their monomials proves the
integral identity: the coefficient for powers of total degree \(k-1\)
is \(q^k/k!\). No derivative of a floor is taken.
Write
\[
\Delta_q(A)=\det_{\mathbb R^4}\mathcal D_q(A).
\]
For \(q=0\), (3) vanishes, so no exponential-owner zero-quotient source is
regular. These matrices remain objects; the definition's separate \(q=0\)
inverse candidate prescription has no retained legal predecessor.
For L, differentiation of (2) gives \(H\mapsto qHC\), hence
\[
\Delta^L_q(A)=q^4(\det C)^2=4q^4.                     \tag{4}
\]
Its own regular domain also excludes \(q=0\); this uses L's map, not (3).

For later exact volume calculations one can evaluate the full determinant
without restricting the carrier. Let \(\lambda_1,\lambda_2\) be the complex
eigenvalues of the real matrix \(A\), with multiplicity, and define
\[
d_q(a,b)=
\begin{cases}(e^{qa}-e^{qb})/(a-b),&a\ne b,\\
q e^{qa},&a=b.\end{cases}
\]
Then
\[
\Delta_q(A)=4q^2 e^{q(\lambda_1+\lambda_2)}
                   d_q(\lambda_1,\lambda_2)^2.        \tag{5}
\]
To prove this first take distinct eigenvalues and diagonalize over \(\mathbb C\).
The derivative of \(A\mapsto e^{qA}\) is conjugated on the full complex
four-dimensional matrix space to the derivative at the diagonal matrix.
Its two diagonal directions have factors \(qe^{q\lambda_1},qe^{q\lambda_2}\);
its two off-diagonal directions both have factor \(d_q(\lambda_1,\lambda_2)\),
as follows directly from (3). Similarity on the full tangent space cancels
in the determinant. Right multiplication by \(C\) contributes
\((\det C)^2=4\). The determinant of the complexification of a real linear
map is its real determinant, yielding (5). Repeated-eigenvalue matrices
follow by continuity from the dense distinct-eigenvalue set and the stated
confluent value; this includes nondiagonalizable matrices.

For real \(A\), its eigenvalues are either real or a conjugate pair, and the
divided difference in (5) is real. Thus the formula is real and nonnegative;
the source guard removes exactly its zeros. No positivity of eigenvalues or
restriction to a diagonal tangent slice was used.
The general formula permits resonant critical matrices; they remain terminal
objects with all incoming, rather than being removed from \(X\).

At an admitted proper-divisor seed, \(q=N/d\) is a positive integer and the
two real eigenvalues \(d,N\) are distinct. Their divided difference in (5)
is nonzero, so the full geometric guard is positive. Therefore actual MAIN
admission at this integer interface is exactly \(d\mid N\). G's own positive
integer quotient there is likewise regular, while L uses (4).

## 3. Every real-log inverse, atlas, and all-point IMAGE

For a target \(Y\) the exponential owners enumerate their own integer source
labels. When their actual \(q\ne0\), take every
\[
L\in\operatorname{Log}_{\mathbb R}(YC^{-1})
 :=\{L\in M_2(\mathbb R):e^L=YC^{-1}\},\qquad A=L/q.    \tag{6}
\]
Retain exactly the reconstructed floors, own quotient/arithmetic permission,
full derivative guard and forward equality. This gives all and only actual
predecessors: multiplying (1) by \(C^{-1}\) gives necessity, and substitution
gives sufficiency. Scaling by nonzero \(q\) is a bijection between the stated
logarithms and matrix candidates before the source checks.
It is not a principal-logarithm inverse or a finite-root algorithm.
The identity \(e^Xe^{-X}=I\), obtained from the absolutely convergent power
series, shows in particular that a singular target has no exponential
predecessor; that target still remains in the object space.

For L the complete nonzero-quotient inverse candidates are
\[
A=(YC^{-1}-I)/q,                                      \tag{7}
\]
with L's own reconstructed label, permission and regularity checks.
All labels are enumerated; the target itself need not be an L source.
For each owner the \(q=0\) forward equation was included by the card, and
§2 shows why its regularity test retains none. This is not a division by zero.
Identical actual predecessors are identified; branch names alone do not
create multiplicity. Write \(\mathcal P_O(Y)\) for this full relation.

For each label map use the frozen rational-ball order, retaining balls with
closure in the full regular locus and injective analytic extension.
The inverse function theorem supplies a sufficiently small injective
neighborhood at every regular source. A rational ball containing the point
with closure inside that neighborhood exists, proving that the eligible
balls cover. This is a mathematical cover, not a claimed decision algorithm.
Intersect with each owner's actual label set and remove earlier source
pieces. These countably many Borel pieces partition its full legal domain.

The fixed-label map on an eligible ball is an analytic diffeomorphism onto
an open image. Hence each actual source piece \(E_\alpha\) has Borel image
\(B_\alpha\), with actual inverse \(\theta_\alpha\) given by restriction of
that analytic inverse. Equations (6)–(7) and the atlas have identical
predecessor sets. Each inverse fibre is at most countable because the source
partition is countable and each piece is injective; no finite bound follows.

Let \(\Delta_O(A)\) mean (5) or (4), with that owner's actual quotient.
The inverse derivative and smooth change of variables on the ambient ball
give, for every Borel \(E\subseteq B_\alpha\),
\[
\mu_4(\theta_\alpha E)=\int_E J_\alpha(Y)\,d\mu_4(Y),
\qquad J_\alpha(Y)=\frac1{|\Delta_O(\theta_\alpha Y)|}. \tag{8}
\]
Extended integrals are allowed. Every displayed value is finite and positive.
Local uniqueness makes the derivative value independent of the eligible
inverse germ through the same actual source and label.
At an assigned integer floor face the same analytic fixed-label prescription
defines the value; no a.e. alteration is made at a periodic null object.
The measure identity alone would not determine a null-point value, whereas
the frozen analytic-germ prescription does.

Thus the actual own one-step clock is
\[
\kappa_O(A)=-\log J_{\alpha(A)}(T_OA)
           =\log|\Delta_O(A)|.                        \tag{9}
\]
There is no next-step value at a terminal and no claim of global continuity
across floor cuts. All signs and legal zero clock values remain. This is a
volume cocycle on this owner, not a claimed classical positive roof.

## 4. Whole history, kernels, isotropy, and phases

The following construction and proof apply separately to each \(O=M,G,L\).
Let \(D_r\) be its Borel domain of \(r\) legal iterates, \(D_0=X\), and put
\[
S_0=0,\quad S_r(z)=\sum_{j=0}^{r-1}\kappa_O(T_O^jz),
\qquad M_r(z)=e^{S_r(z)}
=\prod_{j=0}^{r-1}|\Delta_O(T_O^jz)|,\quad M_0=1.       \tag{10}
\]
All nonempty sums and products are only used on their actual legal domains.
The groupoid consists of all triples
\[
\mathcal G_O=\{(z,r-s,w):z\in D_r,\ w\in D_s,\quad
                           T_O^rz=T_O^sw\}.
\]
Its source is \(w\), range \(z\); equal actual triples are identified and
integer lag retained. For each lag, the defining relation is a countable
union of equality sets of Borel maps, so this is a Borel groupoid.
Composition adds lags, inversion reverses endpoints and negates the lag.
The common-forward-iterate property ensures composition remains in the set.

The full clock cocycle is
\[
c_O(z,r-s,w)=S_r(z)-S_s(w)=\log\frac{M_r(z)}{M_s(w)}.   \tag{11}
\]
Changing representations of one triple adds the same number of legal steps
at a common endpoint to both histories. Their added sums cancel.
For composable arrows, advance the two middle histories to the longer
middle length; it exists by hypothesis. Cancel that middle sum to obtain
additivity of (11). The actual forward arrow is \((T_Oz,-1,z)\), with
clock \(-\kappa_O(z)\). Inversion reverses the clock sign.

Refining finite histories into the countable injective atlas produces actual
arrow branches \(w\mapsto z=(T_O^r)^{-1}(T_O^s w)\).
Their full volume modulus is
\[
M_s(w)/M_r(z)=e^{-c_O(z,r-s,w)}.
\]
Chain rule and change of variables on the smooth extensions, restricted to
the actual Borel source pieces, prove the corresponding every-Borel IMAGE
formula. Thus the history cocycle belongs to actual transport, not merely
to a formal word assignment.
The full kernels are exactly
\[
\begin{split}
K_{\rm lag}&=\{(z,0,w)\in\mathcal G_O\},\\
K_c&=\{(z,r-s,w)\in\mathcal G_O:M_r(z)=M_s(w)\},\\
K_{\rm joint}&=K_{\rm lag}\cap K_c .
\end{split}                                           \tag{12}
\]
All legal witness lengths, null objects, zero clocks and terminal histories
are included. These kernels need not consist only of units.

On the whole \(X\times\mathbb R\), an arrow \(g:w\to z\) sends
\((w,h)\) to \((z,h+c_O(g))\). Height translations act on its entire orbit SET.
For a fixed source orbit choose an object \(b\), and let
\[
H_b=c_O(\operatorname{Iso}_{\mathcal G_O}(b)).
\]
Choose any actual arrow \(g_z:z\to b\) for a particular point in this orbit.
Then its complete extension-orbit phase is
\[
h+c_O(g_z)\pmod{H_b}.                                 \tag{13}
\]
Changing the chosen arrow changes the coordinate by an isotropy clock.
Conversely equality modulo \(H_b\) supplies an isotropy arrow, proving
completeness. No global measurable selector or regular topological quotient
is asserted by this orbitwise description.

For a deterministic partial map, nonzero source isotropy exists exactly on
eventually periodic forward orbits. Unequal legal iterates that coincide
produce a periodic tail; conversely every periodic tail produces such lags.
If its least period is \(p\) and its signed cycle sum is \(C_\gamma\), then
\[
\operatorname{Iso}_{\mathcal G_O}(z)=p\mathbb Z,\qquad
c_O(kp)=kC_\gamma,\qquad H_z=C_\gamma\mathbb Z.          \tag{14}
\]
All incoming-path sums cancel. In particular there is no extra isotropy
from freely concatenating inverse words with the same actual triple.
Extension isotropy is \(p\mathbb Z\) if \(C_\gamma=0\), and trivial otherwise.
A non-eventually-periodic orbit, including every terminal-ending orbit, has
trivial source/extension isotropy and \(H_z=\{0\}\).
Nonzero inter-object clocks can still occur in such an orbit.

The height action over a periodic source orbit is a circle exactly when
\(C_\gamma\ne0\), with primitive \(|C_\gamma|\) and all positive integer
repetitions. If \(C_\gamma=0\), its phase space is \(\mathbb R\), with no
positive period, despite surviving zero-clock source isotropy.
Distinct source orbits are not merged because their times coincide.
This is the full structural ledger, not a classification of higher cycles.

For any target \(Y\), the recursion
\(\mathcal P_O^0(Y)=\{Y\}\),
\(\mathcal P_O^{j+1}(Y)=\bigcup_{Z\in\mathcal P_O^j(Y)}\mathcal P_O(Z)\)
gives every finite incoming depth by induction, with no target permission
test and no restriction of matrix entries or logarithms.
Infinite backward histories, when present, are precisely compatible sequences
\((Y_j)_{j\ge0}\) with \(Y_0=Y,\ Y_{j+1}\in\mathcal P_O(Y_j)\).
Recording these sequences adds no new objects or free arrows to this owner.

## 5. Complete global fixed sets of all three owners

First consider any legal exponential fixed point with its actual integer \(q\).
Section 2 excludes \(q=0\). From \(A=e^{qA}C\), invertibility of \(e^{qA}\)
gives \(C=e^{-qA}A\). The right side commutes with \(A\), so \([A,C]=0\).
The two distinct diagonal entries of \(C\) force both off-diagonal entries
of \(A\) to vanish. This is a consequence of the full fixed equation, not
a diagonal restriction on the carrier or inverse relation.

Write \(A=\operatorname{diag}(-u,-v)\). Its diagonal fixed equations require
\[
u>0,\quad v>0,\qquad u=e^{-qu},\quad v=2e^{-qv}.        \tag{15}
\]
For \(q=-r\le-1\), the first equation is impossible:
\(e^{ru}>ru\ge u\). For \(q\ge1\), the function \(t e^{qt}\) is strictly
increasing on \(t>0\), with range \((0,\infty)\). The two scalar equations
therefore each have exactly one solution, and \(0<u<v<1\), since
\(e^q\ge e>2\). Both actual floors are consequently \(m=n=-1\).
MAIN's own quotient and G's own floor quotient are both \(q=1\).

Define \(u,v\) uniquely by
\[
u e^u=1,\qquad v e^v=2,\qquad 0<u<v<1,
\quad A_E=\operatorname{diag}(-u,-v).                 \tag{16}
\]
Its arithmetic checks hold for both MAIN and G. Formula (5), or (3) directly
on all four matrix units, gives
\[
\eta=\frac{e^{-u}-e^{-v}}{v-u}
     =\frac{u-v/2}{v-u}>0,\qquad
\Delta_E=2uv\eta^2>0.                                \tag{17}
\]
Thus it is an actual regular fixed point. We have proved globally
\(\operatorname{Fix}(T_M)=\operatorname{Fix}(T_G)=\{A_E\}\).
Their identical core does not identify their inverse trees or source orbits.

For L the full fixed equation is
\[
A(C^{-1}-qI)=I.                                      \tag{18}
\]
When \(q=-1\), the first diagonal entry of the right factor is zero, so
there is no solution. For every other integer \(q\), that factor is invertible
and (18) has the only possible solution
\[
A_q=\operatorname{diag}\left(-\frac1{q+1},
                            -\frac2{2q+1}\right).
\]
The case \(q=0\) is not regular for L. When \(q\ge1\), both diagonal
entries lie in \((-1,0)\), so its own floors are \((-1,-1)\) and force \(q=1\).
When \(q=-k\le-2\), the first entry is \(1/(k-1)\).
For \(k=2\) the floors are \((1,0)\), whose own quotient is zero rather
than \(-2\). For \(k\ge3\) the first floor is zero, outside L permission.
Hence
\[
\operatorname{Fix}(T_L)=\{A_L\},\qquad
A_L=\operatorname{diag}(-1/2,-2/3).
\]
It is legal with actual \(q=1\); its full determinant is \(4\) by (4).
All three global fixed classifications include every matrix in \(X\).

## 6. Exact fixed-volume bounds, without numerical evaluation

We prove the strict inequalities needed to classify the MAIN clock using
finite exact rational certificates, not decimal estimates of (16).
For \(0<t<3\), the exponential series and \(k!\ge2\cdot3^{k-2}\) for \(k\ge2\)
give the strict upper bound
\[
e^t<1+t+\frac{t^2}{2(1-t/3)}.
\]
The strictness follows, for example, from the strict factorial bound at \(k=4\).
Positive Taylor partial sums give strict lower bounds. These yield
\[
\begin{array}{ll}
e^{5/9}<691/396<9/5,&
e^{4/7}>1817/1029>7/4,\\
e^{5/6}<361/156<12/5,&
e^{6/7}>5647/2401>7/3.
\end{array}                                           \tag{19}
\]
The lower estimates use the cubic and quartic partial sums respectively;
all displayed comparisons follow by integer cross-multiplication.
Strict monotonicity of \(t e^t\) now proves
\[
\frac59<u<\frac47,\qquad \frac56<v<\frac67.             \tag{20}
\]

The divided difference in (17) is exactly
\(\eta=\int_0^1 e^{-((1-t)u+tv)}\,dt\).
Strict convexity bounds it above by the integral of its endpoint chord,
whereas pairing \(t\) with \(1-t\) bounds it strictly below by its midpoint
exponential. Therefore
\[
\sqrt{uv/2}<\eta<\frac{u+v/2}{2}.
\]
For the lower bound one may explicitly factor out \(e^{-(u+v)/2}\);
the remaining paired integrand is a nonconstant \(\cosh\), whose integral
is strictly larger than one. Since \(u\ne v\), both bounds are strict.
Equations (17) and (20) give
\[
\Delta_E>(uv)^2>\frac{625}{2916}>\frac15,\qquad
\Delta_E<2\frac47\frac67\left(\frac12\right)^2
=\frac{12}{49}<\frac14.                              \tag{21}
\]
For example \(3125>2916\) and \(48<49\) certify the outside comparisons.
This establishes, with exact evidence,
\[
4<\Delta_E^{-1}<5,\qquad
\kappa_M(A_E)=\kappa_G(A_E)=\log\Delta_E<0.             \tag{22}
\]
These are full four-dimensional values. Discarding the off-diagonal
directions in (3) would omit \(\eta^2\) and change the frozen owner.
L separately has \(\kappa_L(A_L)=\log4>0\).

## 7. Entire fixed basins, phases and decisive primitive packets

For \(O=M,G,L\), let \(F_O=A_E,A_E,A_L\), respectively, and let the signed
core clock be \(C_O=\log\Delta_E,\log\Delta_E,\log4\), respectively.
Define its full basin by
\[
\mathcal B^O_0=\{F_O\},\qquad
\mathcal B^O_{j+1}=\bigcup_{Y\in\mathcal B^O_j}\mathcal P_O(Y),
\qquad \mathcal B^O=\bigcup_{j\ge0}\mathcal B^O_j.      \tag{23}
\]
All real logarithms for the exponential owners, all L inverses, all source
labels and every depth are retained. Induction gives
\(\mathcal B^O_j=\{z:T_O^jz=F_O\text{ legally}\}\);
these sets are nested because the core is fixed, and are at most countable.
Thus (23) is exact full-basin coverage, not a finite inverse enumeration,
diagonal restriction or claim that all upstream quotients equal one.

A source arrow connects a point to \(F_O\) exactly when it is in this basin.
Moreover every lag \(k\in\mathbb Z\) occurs between every two basin points,
by taking sufficiently long forward histories beyond both entry times.
Let \(a(z)\) be the first entry time and set
\[
\beta_O(z)=S_{a(z)}(z)-a(z)C_O.
\]
Any later entry gives the same value. The complete basin cocycle is
\[
c_O(z,k,w)=\beta_O(z)-\beta_O(w)+kC_O.                 \tag{24}
\]
Hence the basin lag kernel is exactly all pairs with \(k=0\), its clock
kernel imposes \(\beta_O(z)-\beta_O(w)+kC_O=0\), and the joint kernel
imposes both conditions. Source isotropy at every basin point is the entire
\(\mathbb Z\), and its entire clock image is \(C_O\mathbb Z\).
Since all three \(C_O\) are nonzero, extension isotropy is trivial.
Additional incoming logarithms cannot introduce a smaller generator:
the actual-triple and lag convention has already exhausted all isotropy.

The phase transported to the fixed core is
\[
h-S_{a(z)}(z)\pmod{C_O\mathbb Z}
=h-\beta_O(z)\pmod{C_O\mathbb Z}.                      \tag{25}
\]
The transporting forward arrow has lag \(-a(z)\) and clock \(-S_{a(z)}(z)\).
Every phase is retained. Over each full source basin these phases form one
closed orbit of the height action, not an extra packet for every chosen
height, root label, or entry path. Its primitive time is \(|C_O|\), with
repetitions \(j|C_O|\) for every positive integer \(j\).

For MAIN and G this is \(-\log\Delta_E=\log(\Delta_E^{-1})\).
By (22) it lies strictly between \(\log4\) and \(\log5\); an integer between
4 and 5 does not exist. MAIN therefore has a fully owned positive primitive
which is not an ordinary prime logarithm. The negative sign of the one-step
clock is not an escape: the entire isotropy clock group contains both signs.
L separately supplies the composite primitive \(\log4\), not a rescue for MAIN.
Distinct owners' packets are not pooled, and no non-fixed packet is classified.

## 8. Assessment, limitations and provenance

| Obligation | Exact same-owner finding | Status |
| --- | --- | --- |
| Carrier and arithmetic interface | Full Lebesgue4, proper-divisor seed, actual matrix function | Established; naturalness OPEN |
| Four-dimensional IMAGE | (3)–(9), all actual logarithms and cut values | Established |
| Complete histories | (10)–(14), all kernels, source/extension isotropy and incoming | Established structural ledger |
| Global fixed gate | MAIN/G exactly \(A_E\); L exactly \(A_L\) | Complete on all \(X\) |
| Entire fixed packets | (23)–(25); MAIN primitive strictly between \(\log4,\log5\) | Prime target failed; STOP / FORK |
| Higher periods / prime coverage | Not classified; not needed to retain this adverse packet | OPEN, no further census |
| T3 / formal Routes | No operator, trace or formal Route evaluation | NOT AUDITED / UNASSIGNED; B NOT INVOKED |

The same-object ledger remains intact. G's same fixed result is an independently
owned PROVES_TOO_MUCH warning, not a theorem that MAIN and G have identical
global dynamics. L tests the matrix-function mechanism with its own measure,
regularity and histories. None of these results proves canonical readouts,
prime uniqueness or all-prime coverage. No null-version repair, principal-root
selection, matrix-slice determinant, time rescaling or fitted roof is allowed.

The author read the whole original 98-line card and used the previously read
paper template. Pre-freeze informal fixed-feasibility/design thoughts by the
scout and root are disclosed in the card; this was not a blind or sealed
prediction. The present results are exact post-release proofs.
Current CP1, raw reviewer, final reviewer and sibling scientific outputs
were not author inputs; root owns the card and staged review integration.

The bounded source collision read was the 448 card lines 1–58, non-EOF,
prefix SHA256 3d286bfc7d493f6a177d0cf76b835ef9a61bacdd8bd9315d35178c4fb8aaf53d.
Heading metadata exposed its appended outcome title at line 100 and only
the 070 card title at line 1; neither outcome body nor old proof was read.
Prior 447 authorship/shared history remains disclosed. These limited
definition comparisons give no global novelty or nonconjugacy claim.

Same-author helper /root/arithmetic_feedback_scout/dss_g_fixed_author read only
this card's original 1–98 through EOF and independently measured the same
prefix hash, for global fixed/full-volume checks and exact inequalities.
It was not an independent reviewer and wrote no manuscript file.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Same-model/shared-history
execution is NOT_CALIBRATED, not cross-model validation.
ARS was used for bounded definition/proof staging and evidence separation,
not as mathematical certification or publication authorization.

Reproducibility consists of exact series, matrix identities, rational
inequalities, analytic local inverses and deterministic history arguments.
No scientific code, numerical root evaluation, higher-period search, network,
Git operation, PDF, operator or external publication was used.
Mechanical identity, UTF-8, link and hash checks concern artifacts only.
See the [claim ledger](claim-ledger.md) and [package overview](README.md)
for the same outcome and its explicit limits.
