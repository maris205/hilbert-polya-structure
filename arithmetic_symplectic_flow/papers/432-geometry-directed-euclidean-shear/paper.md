# Geometry-directed Euclidean shear: global termination and zero isotropy clocks

Candidate ID: `ANG-20260923-GES01`. Paper 432; 2026-09-23.
Outcome: OWNED EUCLIDEAN SHEAR CLOCK; EMPTY GLOBAL POSITIVE LEDGER — STOP / FORK
Batch: `GLOBAL-GATE-FEEDBACK-20260923-Q`, round3/5.
Type: exact global negative result for three partial Borel/IMAGE owners.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED. Internal review NOT_CALIBRATED.

## Abstract

The geometry-directed subtractive Euclidean map, geometry-update-OFF
control C and memory-HOLD control H own complete actual inverse atlases
and all-point inverse IMAGE versions for counting-times-flat-area measure.
MAIN/C terminate globally by integer descent. MAIN/H have nontrivial
step clocks but exact potential differences, so every entire isotropy
clock image is zero. We classify H's complete dynamics, coalescence
classes, kernels and phases, not only its fixed sources. H retains its
zero-clock fixed-point isotropy, while all nonfixed legal orbits are
strictly monotone. The positive primitive ledger is empty for each owner,
decisively failing MAIN's nonempty target without a return census.

## 1. Full source, own laws and divisor interface

The [frozen card](candidate-card.md), including its control-name clarification,
fixes \(X=\mathbb N_0^2\times[0,\infty)^2\), coordinates \((a,b,x,y)\),
and the sigma-finite reference measure \(\mu=\#_{\mathbb N_0^2}\times dx\,dy\).
This is not a probability, symplectic suspension or claimed invariant measure.
Each owner has exactly the legal domain \(D=\{a,b\ge1,\ x,y>0\}\).
On \(D\), set \(L\) if \(a\ge b\), including ties, and \(R\) otherwise;
\[
 Q=\left\lfloor\frac{\max(a,b)}{\min(a,b)}\right\rfloor,\quad
 t=\frac{x}{x+y},\quad k=1+\lfloor Qt\rfloor.             \tag{1}
\]
Thus \(1\le k\le Q\). The actual MAIN updates are
\[
 F_L(a,b,x,y)=(a-kb,b,xy^k,y),\qquad
 F_R(a,b,x,y)=(a,b-ka,x,x^ky).                           \tag{2}
\]
The new integer remainder is nonnegative because \(k\min(a,b)\le\max(a,b)\);
positive real coordinates stay positive. Hence (2) maps \(D\) into \(X\),
including integer-axis terminal targets. Every reading is recomputed.
C GEOMETRY-UPDATE-OFF uses the same readings and integer updates but
keeps \((x,y)\). H MEMORY-HOLD keeps \((a,b)\) but executes (2)'s real update.
Their source domains coincide, but their inverse readouts and histories do not.
The card's earlier phrase arithmetic-off was a naming slip, not a third control.

Every point outside \(D\) is retained as a terminal: identities and actual
incoming remain, but no step or step clock is added. No reset, absorbing
loop, coprime restriction, selected prime source or boundary deletion occurs.
All integer units, real units, cuts, axes and unbounded sizes remain.

For every integer \(Q\ge1\), the sector
\[
             (Q-1)/Q\le t<1,\quad 0<t<1                \tag{3}
\]
is nonempty and gives \(k=Q\); for example \(x=Q,y=1\) lies in it.
There the larger register executes its full Euclidean remainder, which
vanishes exactly when the smaller divides it. In particular this retains
the proper-divisor test for \(1<\min(a,b)<\max(a,b)\), not a prime oracle.
All other \(k\) execute too. For \(Q>1\), changing the current geometric
sector changes the actual subtraction and its multiplicative exponent.
This gives the stated divisor-symbolic/geometry feedback arrow, not a
proof of naturalness, prime generation or nonconjugacy to other descriptions.

## 2. Complete inverse atlases and every-Borel IMAGE

For a target \(z'=(A,B,u,v)\), MAIN requires \(u,v>0\), then enumerates
every integer \(k\ge1\), without a cutoff:
\[
 \theta_{L,k}(z')=(A+kB,B,u/v^k,v)\quad(B>0),\qquad
 \theta_{R,k}(z')=(A,B+kA,u,v/u^k)\quad(A>0).            \tag{4}
\]
Retain a candidate exactly when it lies in \(D\), its own \(L/R\) rule,
\(Q,t,k\) agree with the proposed branch, and (2) gives \(z'\).
Target next-step legality is not required. These tests include \(A=0\)
or \(B=0\) targets when the displayed branch permits them.
Conversely an actual forward step forces the unchanged integer and real
coordinates, then uniquely forces the other two as in (4). Therefore both
inverse identities and exhaustion hold. Two passing descriptions count
as one only if they give the same actual source; no formal-word arrows exist.

C uses the same integer candidates in (4) with real source \((u,v)\);
all its own readings are rechecked. H instead requires \(A,B,u,v>0\),
keeps source integers \((A,B)\), fixes its own side and \(Q\), and enumerates
only \(1\le k\le Q\). Its real inverse is \((u/v^k,v)\) on \(L\), or
\((u,v/u^k)\) on \(R\), with all reconstructed readout/forward checks.
MAIN's integer inverse must not be imported into H. These formulas prove
C/H exhaustion by the same coordinate identities, separately for each law.

Every actual branch domain is Borel: integer guards, positive coordinates,
continuous rational readouts, specified half-open floors and equalities
are Borel tests. Hold its side, integer labels and \(k\) fixed. The real
inverse germs for MAIN/H have derivatives
\[
 D\theta_{L,k}=
 \begin{pmatrix}v^{-k}&-kuv^{-k-1}\\0&1\end{pmatrix},\qquad
 D\theta_{R,k}=
 \begin{pmatrix}1&0\\-kvu^{-k-1}&u^{-k}\end{pmatrix}.     \tag{5}
\]
Consequently their prescribed \(J\)'s are \(v^{-k}\) and \(u^{-k}\);
C's own identity real germ has \(J_C=1\). All are positive and finite
at every passing point, including cuts and null states. Floors select
actual domains and are not differentiated at their boundaries.

Each fixed-integer germ is a smooth diffeomorphism of the positive
quadrant. Restricting change of variables to any Borel subset \(E\) of
its actual inverse domain gives
\[
                   \mu(\theta E)=\int_E J\,d\mu.        \tag{6}
\]
The integer reconstruction is injective on each branch and maps each
counting slice to one counting slice. Summing the slice identities proves
(6) even if \(E\) meets infinitely many slices. Atomic labels supply no
additional determinant or weight. The countable atlases cover all legal
steps; overlapping target domains retain separate actual predecessors,
not a single multiplicity-free Jacobian for their union.
Measure alone specifies derivatives only a.e.; the frozen smooth germs
specify these particular all-point values. No density or null-version repair.

## 3. Own clocks and global arithmetic descent

On a legal step define \(\kappa=-\log J(Fz)\), using its source-selected
branch. The separate answers are
\[
 \kappa_F=\kappa_H=
 \begin{cases}k\log y&L,\\k\log x&R,\end{cases}
 \qquad \kappa_C=0.                                    \tag{7}
\]
On the whole positive-real locus \(P=\{x,y>0\}\), including integer axes,
put \(\Psi(a,b,x,y)=\log(xy)\). Direct substitution into the real updates
proves, separately for MAIN and H,
\[
       \kappa(z)=\Psi(Fz)-\Psi(z),\qquad
       S_j(z)=\Psi(F^jz)-\Psi(z)                        \tag{8}
\]
for every legal finite history, with \(S_0=0\). C has \(S_j=0\) by its
own IMAGE calculation. No \(\log0\) is assigned: real-axis states have no
forward step and cannot receive a step from \(D\). The clocks in (7)
may be positive, negative or zero, and are not a positive roof.
For example the legal state \((1,1,1,2)\) has MAIN/H clock \(\log2\);
the conclusion below is not that those arrow clocks vanish everywhere.

For MAIN and, independently, C, let \(V=a+b\). Every legal step gives
\[
             V(Fz)=V(z)-k\min(a,b)<V(z).               \tag{9}
\]
The gcd of the two registers is preserved by either subtraction.
Thus a source in \(D\), of gcd \(g\ge1\), must terminate after finitely
many steps at exactly \((g,0,u,v)\) or \((0,g,u,v)\), with \(u,v>0\).
Indeed an infinite sequence would strictly decrease positive integers;
only an integer zero can end legality, and both registers cannot become
zero in one step. Every decrease is at least \(g\), giving the bound
\(N(z)\le(a+b)/g-1\). A source already terminal has \(N(z)=0\).
This proves global termination and excludes all MAIN/C cycles, not just
fixed points. MAIN and C have their own generally different terminal maps.

## 4. Full groupoid, clocks and terminating-owner phases

For each owner use every actual triple
\(G=\{(z,r-s,w):F^rz=F^sw,\ r,s\ge0\text{ legal}\}\).
Equal triples are identified, lags retained, source is \(w\) and range \(z\).
The Borel actual atlases have countably many predecessors, so \(G\) is
a countable-fibre Borel groupoid. Composition adds lags. Define
\[
                 c(z,r-s,w)=S_r(z)-S_s(w).             \tag{10}
\]
Changing a witness with the same lag adds the same later clock sum at
the meeting point to both terms. This proves descent. Extending the two
middle histories of a composition to their larger meeting iterate makes
the middle sums cancel, proving additivity, including terminal meetings.
The forward arrow \((Fz,-1,z)\) has clock \(-\kappa(z)\).

Extend on all \(X\times\mathbb R\) by \((w,h)\mapsto(z,h+c)\).
For MAIN/H arrows within \(P\), (8) gives
\[
               c(z,\ell,w)=\Psi(w)-\Psi(z);            \tag{11}
\]
C has \(c=0\). Real-axis components contain only their identity.
Hence every isotropy clock image \(H_z=c(G_z^z)\) is \(\{0\}\), already
on the full source. Source and extension isotropy are nevertheless
separate objects: extension isotropy consists of the source loops with
\(c=0\). Height translation acts on the extension orbit SET, with
stabilizer exactly \(H_z\); no smooth or Hausdorff quotient is asserted.

For either terminating owner, let \(N_O(z)\) be its first terminal time
and \(\pi_O(z)\) that actual terminal point, \(O=F,C\). Exactly
\[
 G_O=\{(z,N_O(z)-N_O(w),w):\pi_O(z)=\pi_O(w)\}.          \tag{12}
\]
For a meeting, the remaining terminal time is the same on each side,
forcing this lag; conversely the two terminal histories witness (12).
All source and extension isotropy are trivial. On MAIN's \(P\)-components,
\(\ker\ell\) means equal \(N_F\), \(\ker c\) means equal \(\Psi\), with
\(\pi_F\) equal in both cases; the joint kernel requires both equalities.
On C, \(\ker c=G_C\) and the joint kernel is its equal-\(N_C\) lag kernel.
The isolated real-axis points contribute only units to each kernel.

Let \(\operatorname{Pre}_O(E)\) be the union of every passing own inverse
in §2 over \(E\), counting actual states once. Every terminal \(\eta\)
has complete incoming class \(\bigcup_{j\ge0}\operatorname{Pre}_O^j\{\eta\}\);
these are exactly all full-source components by (12), with no depth bound.
Every real-axis point and every point with both integers zero is isolated.
Other integer-axis terminals keep all passing branches, not an assumed
uniform basin size. At a MAIN terminal in \(P\), the complete real phase is
\[
          h-S_{N_F(z)}(z)=h+\Psi(z)-\Psi(\pi_F(z)).       \tag{13}
\]
C's phase is \(h\); at isolated real-axis terminals it is also \(h\).
Different terminal components remain distinct even with identical phase.

## 5. H: complete dynamics, coalescence, kernels and phases

H keeps its integer pair and side, and never leaves \(D\) when started
there. Fix those integers and write \(\rho=y,w=x\) on \(L\), or
\(\rho=x,w=y\) on \(R\). The held \(\rho>0\) is invariant. Its complete
scalar recurrence, still representing the full state in this stratum, is
\[
 w_j=w_0\rho^{K_j},\quad K_0=0,\quad
 K_{j+1}=K_j+k_j,\quad j\le K_j\le Qj,                 \tag{14}
\]
where \(k_j=1+\lfloor Qw_j/(w_j+\rho)\rfloor\) on \(L\), and
\(k_j=1+\lfloor Q\rho/(\rho+w_j)\rfloor\) on \(R\).
If \(\rho>1\), \(w_j\) strictly increases to infinity; if \(0<\rho<1\),
it strictly decreases to zero but never reaches zero at finite time.
If \(\rho=1\), the full source is fixed. Thus the COMPLETE periodic set is
\[
 \{a\ge b\ge1,\ x>0,\ y=1\}
 \ \cup\ \{1\le a<b,\ x=1,\ y>0\}.                     \tag{15}
\]
Every other legal source is non-eventually-periodic. There are no cycles
of period greater than one, nor nonfixed incoming to (15): the invariant
coordinate must be 1 at any predecessor, where the real map is identity.
All terminals \(X\setminus D\) are isolated for H, since H preserves \(D\).

There is also an exact global description of H's nonfixed coalescence.
For \(\rho\ne1\), digits eventually become the constant
\[
 E=\begin{cases}Q&L,\rho>1\ \text{or}\ R,\rho<1,\\
                 1&L,\rho<1\ \text{or}\ R,\rho>1.\end{cases}           \tag{16}
\]
This follows directly from the two readout fractions tending to 1 or 0
in (14), and the eventual threshold being preserved by monotonicity.
For \(Q=1\) it holds from the start. Put \(u(z)=\log w/\log\rho\).
For any time \(j\) after the constant tail has begun, define
\[
             T(z)=u(H^jz)/E-j.                         \tag{17}
\]
Later choices of \(j\) give the same value, and \(T(Hz)=T(z)+1\).
This is an auxiliary source coordinate, not a roof or replacement clock.
For nonfixed \(z,w\), an actual arrow is characterized exactly by
\[
 (z,\ell,w)\in G_H
 \quad\Longleftrightarrow\quad
 (a,b,\rho)_z=(a,b,\rho)_w,\quad \ell=T(w)-T(z)\in\mathbb Z.            \tag{18}
\]
Necessity follows by applying (17) at a meeting. Conversely choose large
tail times \(r,s\) with \(r-s=\ell\); then
\(u(H^rz)=E(T(z)+r)=E(T(w)+s)=u(H^sw)\), so the states really meet.
Thus \(T\bmod\mathbb Z\), within its invariant stratum, distinguishes all
nonfixed source components. No identification by a bare symbolic word or
by equal clock value has been used.

In (18), \(\ker\ell\) is exactly \(T(z)=T(w)\); fixed and terminal
strata contribute only units to this kernel. Equation (11), with the
held coordinates fixed, gives \(c=\log(w_{\rm source}/w_{\rm range})\).
Therefore \(\ker c\) on every nonfixed stratum consists only of units.
On each fixed point, all integer lags are isotropy with \(c=0\); terminals
have only units. Globally \(\ker c\) is precisely H's isotropy bundle,
and \(\ker\ell\cap\ker c\) is the unit space. Source and extension isotropy
are both \(\mathbb Z\) at (15), and trivial everywhere else; every \(H_z=0\).
The lag kernel need not be trivial: at integers \((2,1)\), points
\((x,y)=(1/3,1/2)\) and \((2/3,1/2)\) have digits 1 and 2 and both map to
\((1/6,1/2)\). This exact coalescence has lag 0 but nonzero clock.

All literal depth-\(j\) incoming is exactly \(\operatorname{Pre}_H^j\),
using its finite own inverse list at each node. The full component of a
nonfixed \(z\) is \(\bigcup_{r,s\ge0}\operatorname{Pre}_H^r\{H^sz\}\),
equivalently (18); direct ancestors must still pass their actual cuts.
Each fixed point and each terminal has singleton incoming.
On \(D\), the complete height phase is \(\theta=h+\Psi(z)\), since
(11) preserves it. Together with its source component, \(\theta\)
classifies the extension orbit: equal phases give exactly the required
height displacement along any actual arrow. At isolated terminals use \(h\).
All phases are real, with no period quotient. The fixed-point ineffective
\(\mathbb Z\) isotropy remains at every height, but physical translation
is free there as everywhere else. Distinct zero-clock fixed cores are not merged.

## 6. Global gate, limits and provenance

All three owners have \(H_z=\{0\}\) at every source. None therefore has a
least positive primitive; the global positive ledger is empty. This fails
MAIN's explicit NONEMPTY requirement, not a vacuous prime-purity success.
MAIN/C lack source cycles by descent; H instead retains all of (15) with
zero loop clock. Their mechanisms and source isotropy must not be conflated.
Arithmetic readout, actual geometric transport, flat reference measure,
germ version, clock and full history stayed on the same owner throughout.
No logarithmic density, atomic-clock transplant, selected section, parameter
tuning, return census or finite-to-global numerical inference was used.
T0/inverse-clock ownership is established; arithmetic T1 NOT PASSED;
T2 has this global negative decision; T3 NOT AUDITED. Strong naturalness
and PROVES_TOO_MUCH remain OPEN. Classical NOT APPLICABLE,
formal UNASSIGNED, B NOT INVOKED. STOP / FORK without local repair.

The [claim ledger](claim-ledger.md) and [README](README.md) bind these scopes.
The complete frozen 101-line card read for proof has SHA256
`76da0d903c9a3f31beb80302dbbc3846f204d03131945fd6e33c36417e6aaf66`.
The author read no current review/raw/sibling manuscript. Definition-stage
access was plan1–411, stream readme1–100, prior-work guide1–441, previous
425 summary1–111, and exactly the complete 400/357 collision cards, including
outcomes; their hashes and design exposure are in the card. No external
novelty/nonconjugacy claim is made. Informal inverse/descent/potential
feasibility reasoning preceded freeze; this was not blind preregistration.
AI agents supplied derivation, drafting and internal checking; no human
or external verification is certified. Same-author helper
`/root/bilateral_transport_review/direct_controls` first saw only
the proposal message for domain completeness, then only the frozen 101-line
card for the disjoint H complete-dynamics/kernel/phase derivation.
The main author derived MAIN/C, common inverse/IMAGE/history ownership
and checked the helper calculation. That helper is not an independent reviewer.
ARS governs stage boundaries and assistance disclosure, not proof validity;
shared-history/same-model review is NOT_CALIBRATED. Only paper/README/ledger
are author-owned; root owns card outcomes and integration. No scientific
numeric code, outside search, old edit, Git/PDF/publication or formal Route work.

EOF — GES01 complete global owner audit; no positive primitive, no follow-on census.
