# Uniform admission exit for divisor radial compression

Paper ID: `445-radial-admission-exit`.
Audit ID: `ANG-AUDIT-20260924-RAE01`.
Audited owner: `ANG-20260923-DRC02`, unchanged.
Outcome: `UNIFORM TWO-STEP EXIT; EMPTY GLOBAL POSITIVE LEDGER — STOP / FORK`
Date: 2026-09-24. Status: exact global exit theorem and full-owner consequences.
Batch: `ADMISSION-EXIT-20260924-T`, round 1/5, 445–449 only.
Arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED.

## Abstract

For the full divisor-admitted radial map, no point has three legal iterates:
\(D^{(3)}=\varnothing\). The two-step domain is exactly the positive-coordinate
part of the arithmetic domain and is nonempty. Thus the frozen eight-step
question has a sharp two-step exit certificate, without a spatial cutoff or
orbit census. Every source history terminates, but all terminal objects and
their incoming trees remain. The actual retained-lag groupoid has a global
terminal normal form, all source and extension isotropy is trivial, and every
entire isotropy-clock image is zero. All physical height phases are retained
and none is periodic. The complete positive ledger is empty, failing the
benchmark's nonemptiness requirement. Separate controls re-establish one
arithmetic-off recurrent packet and an empty denominator-off fixed set.
This is a newly authorized audit of the unchanged DRC02 owner, not a revision
of Paper 442 or a control-to-MAIN transfer.

## 1. Exact object, lineage and question

The sole scientific input is the [89-line frozen card](candidate-card.md).
Each owner has full source \(X=\mathbb R^2\) and reference measure
\(\mu=dx\,dy\), a sigma-finite measure, not a claimed invariant probability.
For \(z=(x,y)\), write \(R=x^2+y^2\), \(n=|\lfloor x\rfloor|\),
\(d=|\lfloor y\rfloor|\), \(A=\{n,d\geq1,\ d\mid n\}\), and \(q=n/d\) only
on \(A\). These are absolute values AFTER flooring.
\[
\begin{array}{c|c|c}
O&D_O&T_O(x,y)\\ \hline
\mathrm{MAIN}&A\cap\{R\ne1\}&(1+dx/(1+R),-1+qy/(1+R))\\
G&\{R\ne1\}&(1+x/(1+R),-1+y/(1+R))\\
N&A&(1+dx,-1+qy).
\end{array}                                                     \tag{1}
\]
No point is deleted. Outside its own legal domain a point is terminal,
with a unit and every actual incoming arrow, but no artificial self-loop.
Integer cuts, negative cells, units and null sets follow the explicit guards.
The \(G\) origin is legal; \(N\) does not inherit the radial circle exclusion.

In the positive integer cell \([N_0,N_0+1)\times[D_0,D_0+1)\), with
\(1<D_0<N_0\), admission is exactly \(D_0\mid N_0\); regularity also holds.
Thus an actual proper-divisor/composite permission controls both geometric
coefficients. The output changes the next readouts. The audit asks whether
that same geometry sustains its arithmetic permission over time.
There is no external prime input, separate integer register, passive fibre,
fitted roof, symplectic suspension, operator or trace owner.

For MAIN, \(D^{(0)}=X\) and
\(D^{(j+1)}=\{z\in D_{\mathrm{MAIN}}:Tz\in D^{(j)}\}\).
The frozen gate is whether \(D^{(8)}\) is empty; a smaller proved uniform
bound is expressly admissible. The controls' global fixed sets, not their
higher-period classifications, are the other authorized discriminators.

## 2. All actual inverses and full planar IMAGE

For a MAIN target \(Z=(X,Y)\), enumerate every \(d,q\geq1\). Set
\(a=(X-1)/d,\ b=(Y+1)/q,\ t=a^2+b^2\). The two inverse formulas are
\[
\theta_{\rm in}(Z)=\frac{2(a,b)}{1+\sqrt{1-4t}},\quad 0\leq t<1/4,
\qquad
\theta_{\rm out}(Z)=\frac{2(a,b)}{1-\sqrt{1-4t}},\quad 0<t<1/4. \tag{2}
\]
Retain precisely the reconstructed sources in the owner domain with
\(|\lfloor x\rfloor|=dq,\ |\lfloor y\rfloor|=d\) and literal forward equality.
The target need not admit another step. At \(t=0\), the inner formula is a
smooth germ with finite source zero; MAIN rejects that source by its guard.
There is no outer point at infinity. At \(t=1/4\), the only source has \(R=1\)
and is excluded; for \(t>1/4\), there is no real regular reconstruction.

Here is complete coverage, not just an inverse ansatz. Every forward source
obeys \((a,b)=z/(1+R)\). With \(\lambda=1+R\), this gives
\(t\lambda^2-\lambda+1=0\). For \(0<t<1/4\), its two roots are exactly
(2), with source squared radii below and above one respectively.
Conversely each root satisfies \(\lambda=1+\lambda^2t\), so substitution
recovers the target; the source guards recover the actual coefficients.
At \(t=0\), the vector equation forces the unique finite source zero.
These arguments prove both actual inverse identities and all edge cases.

For \(G\), use exactly (2) with the independent constants \(d=q=1\), without
arithmetic readout checks. Its origin inverse survives. For \(N\), every
pair \(d,q\geq1\) gives the affine reconstruction
\[
                 \theta^N_{d,q}(X,Y)=((X-1)/d,(Y+1)/q).       \tag{3}
\]
Keep precisely its actual floor labels \(n=dq,\ |\lfloor y\rfloor|=d\).
There is no radial target restriction or critical-circle test in (3).
Substitution proves both identities and complete coverage for this owner.
Distinct reconstructed source points are retained; duplicate actual points
are not extra arrows. No inverse-label or depth cutoff is introduced.

At fixed labels let \(B=\operatorname{diag}(d,q)\).
The full two-dimensional radial derivative is
\[
D T=B\frac{(1+R)I-2zz^{\mathsf T}}{(1+R)^2},\qquad
\det_{\mathbb R^2}DT=dq\,\frac{1-R}{(1+R)^3}.                 \tag{4}
\]
Before multiplication by \(B\), the radial and tangential eigenvalues are
\((1-R)/(1+R)^2\) and \(1/(1+R)\); the zero-source matrix also verifies (4).
Thus each actual inverse germ has the following finite positive density,
where \(R\) is evaluated at its reconstructed source:
\[
J_{\mathrm{MAIN}}=\frac{(1+R)^3}{dq|1-R|},\qquad
J_G=\frac{(1+R)^3}{|1-R|},\qquad J_N=\frac1{dq}.                \tag{5}
\]
These are branch-indexed values, not one common value for two predecessors.
The inner formula supplies the smooth \(G\) value \(J_G(1,-1)=1\).

The fixed-label forward radial map is a diffeomorphism on each of \(R<1\)
and \(R>1\), onto an affinely rescaled disk or punctured disk; (2) proves
injectivity and surjectivity there. All actual floor restrictions are Borel.
Change of variables on these smooth sheets, or on the affine map (3), gives
for EVERY Borel subset \(E\) of an actual inverse domain
\[
                         \mu(\theta E)=\int_E J_\theta\,d\mu. \tag{6}
\]
Infinite values are permitted. At cuts the card selects the fixed-label,
fixed-sheet analytic germ, not a derivative of the floor function. Measure
identities alone do not choose null-set values; this all-point version is
the specified germ version. No global smoothness across floor cuts is claimed.

The own source clock \(\kappa_O=-\log J_{\rm actual}(T_Oz)\) is therefore
\[
\kappa_{\mathrm{MAIN}}=\log\frac{n|1-R|}{(1+R)^3},\quad
\kappa_G=\log\frac{|1-R|}{(1+R)^3},\quad \kappa_N=\log n.       \tag{7}
\]
The MAIN zero-step criterion is \(n|1-R|=(1+R)^3\) on its legal domain.
For \(G\), zero occurs only at the origin; for \(R>0\),
\(|1-R|<(1+R)^3\). For \(N\), it means \(n=d=q=1\).
Terminals have no next-step clock. For finite legal histories, the chain rule
and (6) give the product inverse density \(e^{-S_j(z)}\), where
\(S_j(z)=\sum_{i=0}^{j-1}\kappa(T^iz)\) and \(S_0=0\), including all cuts.

## 3. Sharp global admission-exit theorem

Let \(D=D_{\mathrm{MAIN}}\) and \(Q=A\cap\{x>0,y>0\}\).
Then
\[
              D^{(2)}=Q\ne\varnothing,\qquad
              D^{(3)}=\varnothing,\qquad D^{(8)}=\varnothing. \tag{8}
\]
In particular every point has at most two legal steps. This bound is sharp.

To prove the global first-coordinate bound, put \(u=|x|,\ v=|y|\).
The actual readout obeys \(d<v+1\), while
\[
u(v+1)\leq u^2+\frac{v^2+1}{2}<1+u^2+v^2.                   \tag{9}
\]
The first inequality is the sum of \(2uv\leq u^2+v^2\) and
\(2u\leq u^2+1\). Thus every legal source has
\[
              0<x'=1+\frac{dx}{1+R}<2,\quad
              \operatorname{sign}(x'-1)=\operatorname{sign}(x). \tag{10}
\]
Legal sources have \(x\ne0\), so the sign is nonzero.

Suppose \(Tz=(x',y')\) is also legal. By (10), its positive integer readout
must be \(n'=1\), forcing \(d'=q'=1\). Hence \(x'\geq1\) and \(x>0\).
If \(y<0\), then \(y'=-1+qy/(1+R)<-1\), so \(d'\geq2\), impossible;
\(y=0\) was already excluded by source admission. Therefore \(y>0\).
This proves \(D^{(2)}\subseteq Q\), including every possible negative-cell cut.

Conversely let \(z\in Q\). Then \(x,y\geq1\), \(d=\lfloor y\rfloor\geq1\),
and \(q=n/d\leq x/d\). Consequently
\[
  1<x'<2,\qquad
  0<\frac{qy}{1+R}\leq\frac{xy}{d(1+R)}
       \leq\frac{xy}{1+x^2+y^2}<\frac12,\qquad
  -1<y'<-\frac12.                                           \tag{11}
\]
So \(n'=d'=q'=1\), and \(R'>1\) since \(x'>1\).
The target is genuinely legal, proving \(Q\subseteq D^{(2)}\).
The point \((1,1)\in Q\) shows that this domain is nonempty.

At any target in (11), the next step has its actual coefficients \(d'=q'=1\).
The elementary strict bound \(|x'|/(1+R')<1/2\) gives
\[
                        1<x''<3/2,\qquad y''<-1.             \tag{12}
\]
Thus \(n''=1\) but \(d''\geq2\), so the next target is terminal.
No source can have three legal steps. This proves (8) on the whole plane,
not on a finite collection of cells or a sampled trajectory table.
The inequalities are strict where needed; no boundary orbit is omitted.

## 4. Full groupoids and consequences of termination

For any one owner, retain every legal meeting triple
\[
\mathcal G_O=\{(z,r-s,w):T_O^rz=T_O^sw\text{ legally}\},\qquad
c_O(z,r-s,w)=S_r(z)-S_s(w).                                  \tag{13}
\]
Source is \(w\), range is \(z\); equal triples are identified with lag retained.
For two representations with equal lag, both meeting depths shift by the
same integer. Their common-forward clock sums cancel. Thus \(c_O\) descends.
For composition, extend the two meeting representations to the larger of
their middle-source depths; cancellation proves additivity. Inversion negates
clock and lag. The actual forward arrow \((T_Oz,-1,z)\) has clock \(-\kappa_O(z)\).

For clarity the exact whole-source kernel descriptions, for EACH owner, are
\[
\begin{split}
\ker c_O&=\{(z,r-s,w)\in\mathcal G_O:S_r(z)=S_s(w)\},\\
\ker\ell_O&=\{(z,0,w):T_O^jz=T_O^jw\text{ for some legal }j\},\\
\ker c_O\cap\ker\ell_O&=\{(z,0,w):T_O^jz=T_O^jw,\ S_j(z)=S_j(w)
                                           \text{ for some legal }j\}.
\end{split}                                                   \tag{14}
\]
No kernel is silently reduced to the units.

MAIN admits a stronger complete normal form. Define the number of remaining
legal steps, terminal endpoint, and actual total clock by
\[
\nu(z)=
\begin{cases}0&z\notin D,\\1&z\in D\setminus Q,\\2&z\in Q,\end{cases}
\qquad \pi(z)=T^{\nu(z)}z,\qquad \Psi(z)=S_{\nu(z)}(z).         \tag{15}
\]
The value \(\Psi=0\) at a terminal is an empty sum, not a new outgoing clock.
Every \(\pi(z)\) is terminal by (8). A meeting \(T^rz=T^sw\) has equal
remaining lifetimes, so \(\nu(z)-r=\nu(w)-s\) and \(\pi(z)=\pi(w)\).
Conversely identical endpoints provide a meeting at depths \(\nu(z),\nu(w)\).
Cancellation of the clocks after any earlier meeting now proves
\[
\mathcal G_{\mathrm{MAIN}}
 =\{(z,\nu(z)-\nu(w),w):\pi(z)=\pi(w)\},\qquad
c(z,\nu(z)-\nu(w),w)=\Psi(z)-\Psi(w).                         \tag{16}
\]
Every pair in one terminal class has exactly one lag, which lies in
\(\{-2,-1,0,1,2\}\). This is a consequence of global exit, not imposed pruning.
All source isotropy is trivial. MAIN has no actual periodic point of any
period and no eventually periodic history.

Writing \(k=\nu(z)-\nu(w)\), the complete MAIN kernels specialize to
\[
\begin{array}{ll}
\ker c:&\pi(z)=\pi(w),\ \Psi(z)=\Psi(w),\ \text{arrow }(z,k,w),\\
\ker\ell:&\pi(z)=\pi(w),\ \nu(z)=\nu(w),\ \text{arrow }(z,0,w),\\
\ker c\cap\ker\ell:&\pi(z)=\pi(w),\ \nu(z)=\nu(w),\
                    \Psi(z)=\Psi(w),\ \text{arrow }(z,0,w).
\end{array}                                                   \tag{17}
\]
These retain all merging points, not just individual forward trajectories.
The exact-potential form in (16) was derived from actual termination and (7);
it is not a replacement or inserted coboundary clock.

Let \(\mathcal I_O(B)=\bigcup_\theta\theta(B\cap\operatorname{dom}\theta)\)
use ALL actual inverse branches (2) or (3). For every MAIN terminal \(t\),
its entire class is
\[
                  \pi^{-1}\{t\}
                 =\bigcup_{j=0}^{2}\mathcal I_{\mathrm{MAIN}}^j(\{t\}). \tag{18}
\]
Complete inverse coverage proves this by induction. Depths \(j\geq3\)
are empty by (8), rather than removed by an experimental cutoff.
All labels and both sheets remain at each available depth, including null
and excluded-circle terminal targets. For any owner without an exit result,
the full class of \(z\) is the union of
\(\mathcal I_O^r(\{T_O^sz\})\) over all legal \(s\) and every \(r\geq0\).

The full extension sends \((w,h)\) to \((z,h+c_O(g))\). For MAIN, (16) gives
the exact orbit-set invariant
\[
                         (\pi(z),\,h-\Psi(z)).                \tag{19}
\]
Two extension objects have equal (19) exactly when an actual extension arrow
joins them. Thus the orbit SET is identified with the terminal set times
\(\mathbb R\), retaining every real phase. No quotient-topology regularity
is asserted. Physical height translation adds \(t\) to the second coordinate
of (19), hence is free. All extension isotropy is trivial and
\[
                 H_z=c(\mathcal G_z^z)=\{0\}\quad
                 \text{for EVERY MAIN source object }z.      \tag{20}
\]
There is no positive generator, primitive or positive repetition. The entire
positive ledger is empty, not merely its fixed-source part.

## 5. Separate controls, full fixed packets and limits

The general isotropy rule used here follows directly from (13). A nonzero
isotropy lag gives two unequal iterates of the same source with equal output;
the later of their two depths is legal, so the repeated finite segment is a
legal cycle. Conversely any periodic tail supplies unequal equal iterates.
If the tail's least source period is \(p\) and own cycle-clock sum is \(K\),
the isotropy lags are \(p\mathbb Z\), the character is \(mp\mapsto mK\),
and the ENTIRE image is \(H=K\mathbb Z\). Otherwise both isotropy and \(H\)
are trivial. Indeed every return on the tail is a multiple of \(p\), all such
multiples occur after reaching it, and cancellation removes the incoming
clock while each extra traversal contributes \(K\).
Extension isotropy is \(\{mp:mK=0\}\); a nonzero \(K\) supplies
positive primitive \(|K|\) and its integer repetitions, while \(K=0\) retains
source periodicity but no positive height primitive. All phases in
\(\mathbb R/H\) remain. In a source class choose any arrows from one reference
object to \(z\), with clocks \(b_z\); its phase is \(h-b_z\bmod H\).
Changing arrows changes \(b_z\) by \(H\), not the phase. No global selector
or nice quotient is assumed. A height translation fixes an extension orbit
exactly when an isotropy arrow realizes that height change, so its stabilizer
is the entire \(H\). Equal clock lengths do not merge distinct classes.

### G: radial geometry alone permits recurrence

The fixed equation is \(z=(1,-1)+z/(1+R)\). Zero is not fixed; otherwise it
forces \(z=a(1,-1)\) with \(a=(1+R)/R>1\). Thus, without a line ansatz,
\[
               f=(a,-a),\qquad 2a^3-2a^2-1=0,\quad 1<a<3/2. \tag{21}
\]
The polynomial is strictly increasing on \(a>1\), negative at \(1\), positive
at \(3/2\). This proves exactly one GLOBAL fixed point, which is regular.
Set \(\rho=2a^2>2\). The complete two-sheet inverse (2) gives
\[
                     T_G^{-1}\{f\}=\{f,b\},\qquad b=f/\rho.   \tag{22}
\]
Substitution verifies both preimages. Every \(G\)-image has first coordinate
strictly between \(1/2\) and \(3/2\), whereas \(b_x=1/(2a)<1/2\).
So \(b\) has no predecessor; the entire incoming class is exactly \(\{f,b\}\).
It is one packet, not two selected inverse-sheet packets.

Its clocks follow from its own (7):
\[
\kappa_G(f)=-L,\quad L=\log\frac{(1+\rho)^3}{\rho-1}>0,\qquad
\kappa_G(b)=-L+2\log\rho<0.                                  \tag{23}
\]
Set \(\sigma(f)=0,\ \sigma(b)=2\log\rho\). Thus \(0<\sigma(b)<L\).
Every ordered pair of these points has every integer lag, because sufficiently
advanced iterates meet at \(f\). Cancellation of the initial feeder step gives
\[
                  c_G(z,k,w)=-kL+\sigma(z)-\sigma(w).         \tag{24}
\]
Hence the lag kernel has all four ordered pairs at lag zero; the clock and
joint kernels have only the two units. Both source isotropy groups are
\(\mathbb Z\), entire \(H=L\mathbb Z\), and extension isotropy is trivial.
Every phase \(h-\sigma(z)\bmod L\) is present, with positive repetitions \(mL\).

For completeness this control's \(e^L\) is irrational. The cubic in (21) has
no root among its only rational candidates \(\pm1,\pm1/2\), so \(a\) has degree
three. Using \(a^3=a^2+1/2\) gives
\((1+2a^2)^3=34a^2+10a+13\). If \(e^L=m\in\mathbb Q\), then
\((34-2m)a^2+10a+13+m=0\), an impossible nonzero quadratic relation.
The recurrent control disproves universal exit from radial geometry alone;
its nonprime primitive is not a MAIN witness.

### N: denominator removal has no fixed core

A fixed point would satisfy \((1-d)x=1\). For \(d=1\) this is impossible.
For \(d\geq2\), it forces \(x=-1/(d-1)\in[-1,0)\), hence actual \(n=1\),
contradicting \(n=dq\geq2\). Thus the complete GLOBAL fixed set is empty,
including the negative cut \(x=-1\) and all own legal circle states.
Its full affine inverses, IMAGE and zero clocks remain (3), (5)–(7);
all its histories, kernels, conditional isotropy and phases remain (13)–(14)
and the opening rule of this section. No fixed-core incoming class is invented,
and no conclusion about higher \(N\) periods or global exit is drawn.

## 6. Gate decision and reproducibility

The exact three-owner definitions and all-point clock versions remain intact.
MAIN's uniform exit answers the frozen eight-step question globally and gives
the empty positive ledger. This FAILS nonemptiness and all-prime coverage.
Prime purity and at-most-one-packet statements are merely vacuous on that
empty set, not positive arithmetic achievements; no adverse MAIN length is
fabricated. Decision: STOP this audit / FORK the search under separate authority.

| Coordinate | Evidence for this exact audit and owner | State |
| --- | --- | --- |
| T0 | Full source, actual inverse, own IMAGE, groupoid and extension | OWNED |
| T1 | Actual divisor admission and geometric clock; no prime-law success | NOT PASSED |
| T2 | \(D^{(3)}=\varnothing\), entire \(H=0\), empty positive ledger | Global negative: nonemptiness FAILS |
| T3 | No operator, trace, determinant or zeta audit | NOT AUDITED |
| Classical / formal / B | No classical suspension evaluation | NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

Strong naturalness and PROVES_TOO_MUCH remain OPEN. No general theorem about
all divisor maps, all radial maps or the controls' higher dynamics is claimed.
The bounds are exact for the unchanged owner, not a map repair or new
normalization. No numerical census, larger window or further candidate was run.
Paper 442 remains a frozen record of its narrower authorized question.

The scientific input is the [card](candidate-card.md), fully read lines 1–89 EOF,
SHA256 `272374c01e2576df1e0c274c353b11d9cb47d87c895d2adad7723b0ff7b8d0ad`.
The [claim ledger](claim-ledger.md) and [summary](README.md) index this proof.
All results are re-established above by exact inequalities, algebra and calculus.
Mechanical hash/line/link checks do not constitute scientific evidence.

## 7. Access and AI disclosures

The author previously authored the 442 proof and participated in its design.
That shared exposure remains; this is not blind or zero-exposure derivation.
No old proof/raw file or new CP1/raw/reviewer/peer answer was opened for this
audit. The card records root's earlier informal short-admission thought;
this disclosure is not a claimed preregistered prediction.
Only the complete 445 card and required ARS instruction files were scientific
intake reads this turn; author-created outputs were read back for verification.

AI agents supplied mathematical derivation, drafting and internal checking.
The named helper `direct_controls`, also previously exposed as 442 author
aid, reread only the complete 445 card plus ARS instructions and re-established
the \(G/N\) control facts. MAIN's exit proof and terminal normal form were
derived by the main author. The helper is same-author aid, not a reviewer seat;
no human, external or cross-model verification is certified.
Shared-history same-model review is `NOT_CALIBRATED`.
ARS bounded-writing rules governed scope, evidence language and disclosure.
There was no network, Git, PDF, operator work or old-file mutation.

Data availability: definitions and exact proofs are in this package; no
experimental dataset exists. Ethics: no human/animal subjects or personal data.
Contributions: AI author derivation/writing/internal validation, bounded helper
control derivation, root integration; human authorship not certified.
Funding: not supplied. Conflicts: not assessed. Venue criteria binding:
unavailable; no publication or submission-readiness claim.

EOF — ANG-AUDIT-20260924-RAE01; unchanged DRC02 owner, global exit proved.
