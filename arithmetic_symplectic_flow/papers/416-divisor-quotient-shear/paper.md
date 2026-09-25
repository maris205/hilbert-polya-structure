# Divisor quotient–shear: owned clocks and continuous nonprime fixed times

Candidate ID: `ANG-20260923-DQS01`. Paper416; 2026-09-23.
Batch `SYNCHRONOUS-FEEDBACK-20260923-N`, round2/5.
Outcome: `OWNED QUOTIENT-SHEAR CLOCK; CONTINUOUS NONPRIME FIXED TIMES — STOP / FORK`.

Contract: [frozen card](candidate-card.md), original88 lines, fully read before proof.
Scope: full inverse/IMAGE and history ledger; complete fixed sets in two
specified source cells for four owners, not a global fixed-set or cycle census.
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; Route B NOT INVOKED.
AI-assisted mathematical derivation/drafting, shared-history NOT_CALIBRATED.

## Abstract

The full real plane carries a partial map combining a quotient coordinate
with a current-digit shear, permitted by signed integer divisibility.
Its complete rational inverse atlas owns a positive finite IMAGE density
at every actual point, including all assigned cuts. The resulting signed
clock, retained-lag groupoid and real height action remain on the same object.
In the frozen cell \(a=1,b=0\), MAIN has the complete fixed curve
\((s/(1-s),s)\), \(0<s<1/2\), with primitive time \(-\log s\).
The full period group proves in particular that \((1/3,1/4)\) has primitive
\(\log4\), not an unexamined repetition of \(\log2\).
The permission-off and shear-off controls have the same curve and own times;
division-off has no fixed state in either prescribed cell. No owner has a
fixed state in the second cell \(a=b=1\). All incoming histories, phases and
zero-clock isotropy are retained. MAIN fails the ordinary-prime condition.

## 1. Source, exact lineage and separate controls

Each owner has all \(X=\mathbb R^2\), usual Borel structure, and \(\mu=dx\,dy\).
Only for \(y\ne0\), read
\[
a=\lfloor x/y\rfloor,\qquad b=\lfloor y\rfloor,\qquad r=y-bx,\qquad K=1-ab.
\]
Set \(D=\{y\ne0,r\ne0,a\ne0,a\mid b\}\), using signed integer divisibility.

| Owner | Own legal domain | Own actual successor |
| --- | --- | --- |
| MAIN | \(D\) | \((x/y-a,\ y-bx)\) |
| G, permission-off | \(y\ne0,r\ne0\) | \((x/y-a,\ y-bx)\) |
| P, division-off | \(D\cap\{K\ne0\}\) | \((x-ay,\ y-bx)\) |
| S, shear-off | \(y\ne0,a\ne0,a\mid b\) | \((x/y-a,\ y)\) |

The S domain does not retain the removed \(r\ne0\) restriction.
All floors are left-closed/right-open; units, \(b=0\), all signs and all null
points remain. A point outside an owner's legal domain is a forward terminal
with \(T^0\) and all actual incoming, not an absorbing fixed state.
Undefined ratios at \(y=0\) are not evaluated, and no terminal-step clock
is assigned zero in place of NOT DEFINED.

For integers \(N\ge2,\ 1<d<N\), the interface \((x,y)=(dN,N)\)
has digits \((d,N)\) and \(r=N(1-dN)\ne0\). MAIN is therefore legal there
exactly when \(d\mid N\). This is a precise deformation of the
[proper-divisor/prime-symbolic lineage](../../docs/prior_work/README.md):
current geometric digits determine permission and transport, and the
successor regenerates them. The full source is not this integer interface.
The term \(y-bx\) is a shear residual, not a Euclidean remainder:
\(b=\lfloor y\rfloor\) is not the division quotient of y by x.
No prime alphabet, fixed arithmetic label, per-prime parameter, roof or
fitted measure is supplied. Strong naturalness remains a separate question.

## 2. Actual inverse domains and all incoming branches

For MAIN/G and every integer pair \(a,b\), write
\[
L_{ab}(u)=1-b(a+u),\qquad
\theta_{ab}(u,v)=\left(\frac{(a+u)v}{L_{ab}(u)},\frac v{L_{ab}(u)}\right).
                                                               \tag{1}
\]
For MAIN use only \(a\ne0,a\mid b\); G uses all integer pairs.
The exact inverse domain is
\[
E_{ab}=\{0\le u<1,\ v\ne0,\ L_{ab}(u)\ne0,\
                 b\le v/L_{ab}(u)<b+1\}.                       \tag{2}
\]
Indeed any source with these digits has \(x/y=a+u\) and
\(v=y-bx=yL_{ab}(u)\). Its legal \(y,v\ne0\) force \(L\ne0\),
and (1) follows. Conversely (1)--(2) recover nonzero y, the correct quotient
floor a and height floor b, and residual v; both inverse identities follow.
The arithmetic permission is exactly the restriction on labels above.
Thus there are no hidden additional source checks or omitted predecessors.

For P, enumerate all \(a\ne0,a\mid b,K=1-ab\ne0\), and set
\[
\theta^P_{ab}(u,v)=\left(\frac{u+av}{K},\frac{bu+v}{K}\right)
                     =:(x_*,y_*).                             \tag{3}
\]
The exact domain consists of all real targets satisfying
\[
v\ne0,\quad y_*\ne0,\quad a\le x_*/y_*<a+1,\quad b\le y_*<b+1. \tag{4}
\]
There is no \(0\le u<1\) requirement for P.
Inverting the two-by-two linear system gives (3);
\(y_*-bx_*=v\) verifies its residual condition and both inverse identities.
The frozen \(K=0\) source cells remain terminal, not collapsed into images.

For S, for each integer \(a\ne0\), use
\[
\theta^S_a(u,v)=((a+u)v,v),\qquad
E^S_a=\{0\le u<1,\ v\ne0,\ a\mid\lfloor v\rfloor\}.             \tag{5}
\]
Its quotient digit is exactly a, its height digit is the actual \(\lfloor v\rfloor\),
and substitution proves necessity and sufficiency. No redundant b label is used.
No target-forward condition replaces a source condition in any owner.
Source digits are unique, so different labels never create copies of one
actual predecessor; each displayed inverse is injective on its own domain.

All these domains are Borel. They include their assigned floor faces,
and no division is made at a forbidden denominator.
For any owner O and target w let \(\mathcal P_O(w)\) be exactly the accepted
inverse points in (1)--(5). Define, with no label/depth cutoff,
\[
\mathcal P_O^0(w)=\{w\},\qquad
\mathcal P_O^{j+1}(w)=\bigcup_{z\in\mathcal P_O^j(w)}\mathcal P_O(z). \tag{6}
\]
One-step completeness proves by induction that these are exactly all sources
of legal j-step histories into w. This is an exact full incoming specification,
also for terminal targets, not a selected branch or finite experiment.
All targets with second coordinate0 have no predecessors for any owner:
MAIN/G/P output the required nonzero r, and S preserves its nonzero y.
They remain terminal objects with their identities and real phase lines.
Other terminals may have incoming; (6) retains all of them.

## 3. Full-point IMAGE and each owner's clock

Differentiate the rational extension (1) on \(vL\ne0\).
With \(A=a+u\), its derivative matrix is
\[
D\theta_{ab}=
\begin{pmatrix}v/L^2&A/L\\ bv/L^2&1/L\end{pmatrix},\qquad
\det D\theta_{ab}=v/L^2.
\]
For (3), \(\det D\theta^P_{ab}=1/K\); for (5),
\(\det D\theta^S_a=v\). Hence the prescribed full-point densities are
\[
J_{ab}=\frac{|v|}{L^2}\quad(\mathrm{MAIN/G}),\qquad
J^P_{ab}=\frac1{|1-ab|},\qquad J^S_a=|v|.                     \tag{7}
\]
They are finite and strictly positive at every actual inverse point.
The fixed-branch analytic formulas extend across every included floor face;
this is not an assertion that the piecewise forward map is differentiable
across a change of digit. If chart names agree on an actual source, its
unique digits and the displayed derivatives give the same point value.

For each actual inverse chart and every Borel \(E\) in its domain,
\[
\mu(\theta E)=\int_EJ_\theta\,d\mu.                           \tag{8}
\]
Each formula is an injective analytic map with nonzero derivative on an open
neighbourhood of each point of its actual domain. Cover by countably many local
diffeomorphism charts, partition E into disjoint Borel pieces, and apply change
of variables. Injectivity makes the image pieces disjoint.
Restricting to the Borel digit conditions preserves (8), including null subsets.
Thus the point version is owned by the analytic extension, not invented
from an almost-everywhere density. No change of measure or null-point patch is used.

For a legal source define \(d_O(z)=J_{\theta_z}(T_Oz)^{-1}>0\) and
\(\kappa_O=\log d_O\). Substituting \(v=r,L=r/y\) into (7) yields
\[
\begin{array}{c|c|c}
O&d_O(x,y)&\kappa_O(x,y)\\ \hline
\mathrm{MAIN/G}&|r|/y^2&\log|r|-2\log|y|\\
\mathrm P&|1-ab|&\log|1-ab|\\
\mathrm S&1/|y|&-\log|y|
\end{array}.                                                \tag{9}
\]
These are four owned transport clocks, not a common borrowed clock.
MAIN/G/S clocks can have either sign or be zero; P is nonnegative,
but may vanish. No positive roof, invariant probability or smooth flow is claimed.

## 4. Entire groupoid, kernels, isotropy and phase direction

All statements below are made for each owner's actual legal histories.
Set \(M_j(z)=\prod_{i=0}^{j-1}d_O(T_O^iz)\), \(M_0=1\), and \(S_j=\log M_j\).
Keep precisely the actual triples
\[
G_O=\{(z,m-n,w):T_O^mz=T_O^nw,\ m,n\ge0\text{ legal}\},
\qquad c(z,m-n,w)=\log\frac{M_m(z)}{M_n(w)}.                 \tag{10}
\]
The source is w, range z; equal triples are identified and all integer lags kept.
Countably many inverse branches give countable source fibres; the graph is a
countable union of Borel equal-iterate relations.
Two presentations of the same triple differ by extending both histories by
the same number of steps. Their common tail factors cancel, proving c descends.
To compose arrows, align the two middle histories using only the steps
already present in the longer history. Their factors cancel as well,
proving additivity without continuing beyond a terminal.
Inverse arrows negate c. The actual forward arrow \((T_Oz,-1,z)\) has
clock \(-\kappa_O(z)\). Finite local inverse-word densities multiply,
and any local arrow graph from w to z has density \(e^{-c}\) by (8).

The full kernels are the following exact sets, with the legal relations
in (10) always imposed:
\[
\begin{aligned}
\ker\ell&=\{(z,0,w):T_O^mz=T_O^mw\text{ for some legal }m\},\\
\ker c&=\{(z,m-n,w):M_m(z)=M_n(w)\},\\
\ker\ell\cap\ker c&=\{(z,0,w):T_O^mz=T_O^mw,\ M_m(z)=M_m(w)
                                      \text{ for some legal }m\}. \tag{11}
\end{aligned}
\]
Merging predecessors are retained, so lag0 is not equated with an identity.
On every S arrow away from the isolated \(y=0\) objects, both endpoints have
the same y and \(c=-\ell\log|y|\). Thus its clock kernel consists exactly of
lag0 arrows and arrows over \(|y|=1\), together with the isolated identities;
its intersection with the lag kernel is the whole lag kernel.
No value of \(\log|y|\) is assigned at \(y=0\).

A nonzero-lag source-isotropy arrow equates two different forward iterates,
so it exists exactly when the history is eventually periodic.
Let the least eventual core period be p and its full cycle sum be C.
Comparing equal iterates on that least cycle, and cancelling any incoming prefix,
gives
\[
G_z^z=p\mathbb Z,\qquad H_z=c(G_z^z)=C\mathbb Z,\qquad
\operatorname{Iso}_{G^c}(z,h)=\{kp:kC=0\}.                   \tag{12}
\]
For non-eventually-periodic histories, including finite terminal histories,
both isotropy groups are trivial and H is zero.
The general cycle clocks, without asserting cycle existence, are
\[
C_{\mathrm{MAIN/G}}=-\sum_{j=0}^{p-1}\log|y_j|,\qquad
C_P=\sum_{j=0}^{p-1}\log|1-a_jb_j|,\qquad C_S=-p\log|y|.
                                                               \tag{13}
\]
The first formula telescopes the \(\log|y_{j+1}|\) term in (9);
all legal cycle coordinates y are nonzero. The S coordinate y is constant.

On the full \(X\times\mathbb R\) extension use
\((w,h)\mapsto(z,h+c(g))\). Height translation acts on its orbit SET.
Its full stabilizer is H: returning to the same base object requires
precisely a source-isotropy arrow. The phase fibre is \(\mathbb R/H\).
If C is nonzero, the primitive is \(|C|\), repetitions are \(k|C|\),
and extension isotropy is trivial. If C is zero, all \(p\mathbb Z\) source
isotropy remains in the extension; the height line is free and no positive
primitive exists. No Hausdorff quotient, positive suspension or ODE is asserted.

More explicitly, choose a base object b in a source orbit and an actual arrow
\(g_z:z\to b\). Its phase is \(h+c(g_z)\pmod{H_b}\); two choices differ by
a loop at b, hence an element of \(H_b\). If \(T_O^a z=F\) is a fixed core
and \(C=\kappa_O(F)\), the arrow \((F,-a,z)\) gives
\(h-S_a(z)\pmod{C\mathbb Z}\).
The complete fixed-core packet is
\(\mathcal B_O(F)=\bigcup_{j\ge0}\mathcal P_O^j(F)\), with (6) using every
integer branch at every depth. Every such point has the same H by (12).
Different fixed cores have disjoint packets, since their deterministic
constant forward tails cannot meet. Convergence without a finite hit
does not add arrows. These formulas determine all incoming and phases,
not only the recurrent points or a selected inverse history.

## 5. Complete fixed probe in the two frozen cells

The actual source cells are
\[
C_{10}=\{0<y<1,\ y\le x<2y\},\qquad
C_{11}=\{1\le y<2,\ y\le x<2y\}.
\]
These are just the conditions \(a=1,b=0\) and \(a=1,b=1\), including their
assigned lower faces. In both cells \(1\mid b\), so permission is automatic.
For each owner first intersect with its own legal domain:

| Owner | Legal part of \(C_{10}\) | Fixed set there | Legal part of \(C_{11}\) | Fixed set there |
| --- | --- | --- | --- | --- |
| MAIN | all \(C_{10}\) | \(\Gamma\) below | \(1\le y<2,\ y<x<2y\) | empty |
| G | all \(C_{10}\) | \(\Gamma\) | \(1\le y<2,\ y<x<2y\) | empty |
| P | all \(C_{10}\) | empty | empty | empty |
| S | all \(C_{10}\) | \(\Gamma\) | all \(C_{11}\) | empty |

Here the complete curve is
\[
\Gamma=\{F_s=(s/(1-s),s):0<s<1/2\}.                         \tag{14}
\]
In \(C_{10}\), \(r=y\ne0,K=1\). MAIN/G/S all reduce to
\((x/y-1,y)\). The fixed equation gives \(x=y/(1-y)\); its ratio has floor1
exactly when \(1\le1/(1-y)<2\), hence \(0<y<1/2\).
Every point in (14) is therefore legal and fixed. The endpoint y=0 is outside
the ratio domain. At y=1/2 the ratio equals2, so that point is not in this
cell; it is not deleted from the full source. For P the first coordinate is
x-y, whose fixed equation requires the forbidden y=0.

In \(C_{11}\), \(r=y-x\). MAIN/G retain precisely the strict x>y part;
fixedness of their second coordinate would require x=0, impossible.
P has no legal source there because K=0; this is a terminal cell, not a
family of fixed self-loops. S retains even the boundary x=y, but its first
output lies in \([0,1)\), whereas \(x\ge y\ge1\), precluding fixedness.
This also handles y=1 and all included ratio boundaries.
The table exhausts the two cells only, with no claim about any other cell.

## 6. Full packets and decisive primitive obstruction

For each \(s\in(0,1/2)\), all three owners MAIN/G/S have, separately,
\[
\kappa_O(F_s)=-\log s=:L_s>0,\quad
G_{F_s}^{F_s}=\mathbb Z,\quad H_{F_s}=L_s\mathbb Z,\quad
\operatorname{Iso}_{G^c}(F_s,h)=\{0\}.                       \tag{15}
\]
Each owns the entire packet \(\mathcal B_O(F_s)\) from (6), its incoming
phase \(h-S_a\pmod{L_s\mathbb Z}\), and full phase circle
\(\mathbb R/(L_s\mathbb Z)\). P has no fixed core in this window to which such
a packet could be assigned. Outside-window incoming branches of MAIN/G/S
are still included by the unrestricted inverse atlas; they are not cut off
at the two probe cells. Distinct s give distinct packets.

Equation (15) computes the whole return group, not just one displayed loop.
Thus its least positive generator is \(L_s\), and repeated loops give \(kL_s\).
As s ranges over \((0,1/2)\), these fixed primitive times fill \((\log2,\infty)\).
In particular
\[
F_{1/4}=(1/3,1/4),\qquad a=1,\ b=0,\qquad
T(F_{1/4})=F_{1/4},\qquad H=(\log4)\mathbb Z.               \tag{16}
\]
There is no smaller \(\log2\) return in this full H. Since 4 is not an ordinary
prime and the logarithm is injective on positive reals, (16) directly fails
MAIN's necessary prime-only condition. No inference from a control is needed.
The interval statement supplies further nonprime times; no prime multiplicity
or all-prime-coverage assertion is inferred for the unexamined global ledger.

## 7. Decision and limits

The carrier, maps, native measures, full-point IMAGE versions and packet
conventions remain exactly those frozen. T0 and precise measured-clock
ownership are established; the necessary T2 target fails inside the bounded
fixed window. MAIN/G/S share the window because \(a=1\) makes permission
automatic and \(b=0\) turns off the shear there. This is an adverse mechanism
control, not a reason to erase that branch or retune the object.
P has its own empty fixed window, not an assigned zero terminal clock.
All zero-clock loops and all other source points remain in (10)--(13).

Strong naturalness and arbitrary-encoding/PROVES_TOO_MUCH remain OPEN.
There is no global fixed-set classification, higher-period census, operator,
trace or zeta claim. Classical symplectic/suspension fields are NOT APPLICABLE;
T3 NOT AUDITED; formal UNASSIGNED; Route B NOT INVOKED.
Decision: STOP / FORK. No local parameter repair, sign restriction,
first-return rescaling, zero-measure selection or additional cell search.

## Reproducibility, access and AI disclosure

Exact evidence is the [card](candidate-card.md) and the displayed inverse,
change-of-variables, floor and deterministic-history proofs; there is no dataset
or scientific code. See the [claim ledger](claim-ledger.md) and [overview](README.md).
The author fully read original88-line card EOF and the paper template.
Scoped scouting reads were [299 card](../299-quotient-remainder-reciprocal-flow/candidate-card.md)
1--47 and [395 card](../395-simultaneous-content-return/candidate-card.md)1--55,
neither EOF. Heading navigation exposed outcome titles, not their bodies.
An earlier standard reciprocal proposal too close to395 was withdrawn before
freeze. The present shear law is different in formula; no global novelty or
nonconjugacy claim is made. Shared prior scouting/transcription and author
history, including397/401/406/411, are disclosed rather than called blind.

One bounded author-helper derived only the G/P/S fixed states and boundary
conditions in the two prescribed cells. The lead author checked that argument
and derived MAIN, inverses, IMAGE and the full ledger; this is author
collaboration, not an independent reviewer seat. No reviewer/raw/peer science
was read. AI agents supplied derivation, drafting and author-side checking;
the separate internal-review workflow also uses AI agents.
All such work is NOT_CALIBRATED; no human or external verification is certified.
Ethics: no human subjects/personal data. Human contribution attestations,
funding and conflicts were not supplied and are not fabricated.
No external API/literature campaign, numerical experiment, Git mutation,
PDF, publication or formal evaluation was performed.
