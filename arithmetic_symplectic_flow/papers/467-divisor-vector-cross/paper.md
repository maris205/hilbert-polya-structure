# Divisor-driven vector recombination and a noninteger fixed primitive

Candidate ID: ANG-20260925-DVC01. Paper 467, version 1.
Outcome: OWNED SIX-DIMENSIONAL IMAGE; NONINTEGER FIXED RETURN — STOP / FORK
Date: 2026-09-25. Batch ADMISSION-CORE-20260925-X, round 3/5.
Type: ANG measured-history action, not a claimed conservative or symplectic map.
Classical fields NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The frozen divisor-driven double-vector map owns a full-six-dimensional
IMAGE clock on original Lebesgue measure. We derive every actual inverse
branch, including an exhaustive treatment of the zero-quotient critical
case, and prove the prescribed values on all arithmetic cuts.
The complete fixed-window gate has one MAIN core, reproduced by the
permission-OFF owner, and no fixed points for the other two controls.
The MAIN core has multiplier \(11/2\). Its entire fixed-basin isotropy
clock group, with every incoming depth retained, is
\(\log(11/2)\mathbb Z\), not a subgroup inferred from one selected loop.
Its primitive is therefore not the logarithm of an ordinary prime.
An exact unrestricted inverse recursion and phase test retain the complete
basin without claiming a finite tree enumeration. The candidate stops;
no additional window, higher-period search or parameter repair is used.

## 1. Frozen identity, source and controls

The governing [candidate card](candidate-card.md), original lines 1–115
through EOF, has SHA256
ed66e9258ce953584e9bd57c2dac7ea00bac740d8133ebcf3be579f60a89a658.
The [claim ledger](claim-ledger.md) gives the scoped claims and the
root-managed [review record](evidence/review.md) is a separate artifact.
No reviewer material is an author proof input.

Every owner uses the full \(X=\mathbb R^3_u\times\mathbb R^3_v\),
Euclidean topology/Borel sets, and original Lebesgue6 in the ordered
coordinates \((u_1,u_2,u_3,v_1,v_2,v_3)\). Fix \(a=e_3\), \(b=e_1\).
The standard cross product is
\[
u\times v=(u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1).
\]
Set \(m=\lfloor u_1\rfloor,\ n=\lfloor u_2\rfloor\) with the usual
signed floor convention, and
\(\mathcal A=\{(u,v):m\ne0,\ m\mid n\}\).
On \(\mathcal A\), write \(q=n/m\in\mathbb Z\).
G instead uses \(q_G=\lfloor n/m\rfloor\) for \(m\ne0\), and zero for \(m=0\).

| Owner | Fixed-label formula | Arithmetic rule |
| --- | --- | --- |
| M, MAIN | \((u+v-a,\ u\times v+qu+b)\) | \(\mathcal A,\ q=n/m\) |
| G, permission-OFF | Same formula with its own label | \(q_G\), no divisibility permission |
| C, cross-product-OFF | \((u+v-a,\ qu+b)\) | \(\mathcal A,\ q=n/m\) |
| D, constant-drift-OFF | \((u+v,\ u\times v+qu)\) | \(\mathcal A,\ q=n/m\) |

Each row additionally requires its own full-six-dimensional derivative
to be nonsingular. Section 2 proves that this means \(q\ne0\) in each
row, with G using \(q_G\). It is not an imposed sign restriction.
All rejected sources remain terminal objects with their identity and
every actual incoming arrow. There is no added absorbing loop, no
outgoing terminal clock, and \(U^0\) is defined on all \(X\).
Zero vectors, collinear states, every floor face and every sign stay in
the carrier. No condition is imposed on the next-step legality of a target.
The fixed-label germs are analytic; the piecewise arithmetic maps are
Borel partial maps, not asserted globally smooth or symplectic dynamics.

For positive integers \(N\ge2,\ 1<d<N\), the seed
\[
u=(d,N,0),\qquad v=e_3                              \tag{1}
\]
has arithmetic permission exactly \(d\mid N\).
If admitted, \(q=N/d\ge2\), so the full derivative proved below is regular.
MAIN's actual first output at this seed is \(u\), while its second is
\[
v'=(N+qd+1,\ -d+qN,\ 0).
\]
The unchanged first output makes the next source arithmetic-admitted too;
its following first vector is \(u+v'-e_3\), which rereads the updated
state. Thus quotient feedback is not a passive register: it changes
one active vector which enters the next current divisor readout.
The precise lineage is proper-divisor symbolic admission
\(\to\) current integer readouts \(\to\) quotient-weighted cross
recombination \(\to\) new arithmetic state. No prime table, fitted roof,
zero data or per-prime choice is present. Strong naturalness of the
chosen operation and constants remains OPEN.

The only return gate is the complete fixed set in
\[
W=\{-1\le u_1<0,\ -1\le u_2<0,\quad
                   u_3,v_1,v_2,v_3\in[-2,2]\}.          \tag{2}
\]
Every derivative is computed on full \(X\), and every found core has
its full-\(X\) incoming basin. The window is not a replacement carrier.

## 2. Complete six-dimensional transport

### 2.1 Own regularity, including zero quotient

For a cross-product owner, let \(s=u+v\) and define
\[
R_s h=h\times s,\qquad L_{q,s}=qI_3+R_s .
\]
For source increments \((h,k)\), the derivative is
\[
(h,k)\longmapsto
\bigl(h+k,\ h\times v+u\times k+qh\bigr).
\]
Change input coordinates to \((t,h)=(h+k,h)\).
That change has determinant \((-1)^3=-1\) on the original six coordinates.
The output becomes
\((t,\ u\times t+L_{q,s}h)\), whose determinant in these new coordinates
is \(\det L_{q,s}\). Direct expansion of
\[
L_{q,s}=
\begin{pmatrix}
q&s_3&-s_2\\
-s_3&q&s_1\\
s_2&-s_1&q
\end{pmatrix}
\]
therefore proves, on every real source,
\[
\delta_{M/G/D}(u,v)=-q(q^2+\|u+v\|^2).                  \tag{3}
\]
The constants in M/G do not enter this derivative; G nevertheless
uses its own actual label. For C the derivative is
\(\begin{pmatrix}I&I\\qI&0\end{pmatrix}\), so independently
\[
\delta_C(u,v)=-q^3.                                    \tag{4}
\]
Equations (3)–(4) prove that all four guards are exactly \(q\ne0\).
At \(q=0\), every formal source is critical, even when the corresponding
inverse equation has many solutions. None is a legal outgoing source.
Those points remain objects; this conclusion does not erase their incoming.
In particular the integer interface (1) passes the full guard whenever
it passes its proper-divisor arithmetic test.

### 2.2 All inverse solutions without a preferred direction

For every nonzero integer \(q\), every \(s,t\in\mathbb R^3\), set
\[
P_q(s,t)=
\frac{qt-t\times s+q^{-1}(s\cdot t)s}{q^2+\|s\|^2}.      \tag{5}
\]
The cross-product identity
\(R_s^2=ss^{\mathsf T}-\|s\|^2I\), together with \(R_s s=0\), gives
\[
(qI+R_s)(qI-R_s+q^{-1}ss^{\mathsf T})
       =(q^2+\|s\|^2)I .
\]
Since (3) makes \(L_{q,s}\) invertible for \(q\ne0\), (5) is exactly
its inverse applied to \(t\). It contains all directions and does not
require a chosen axis, eigenvector or collinearity assumption.

For a target \(z=(x,y)\), the complete fixed-label candidates are:
\[
\begin{array}{ll}
\theta_q^{M/G}(x,y)=
 \bigl(P_q(x+a,y-b),\ x+a-P_q(x+a,y-b)\bigr),\\[3pt]
\theta_q^C(x,y)=
 \bigl((y-b)/q,\ x+a-(y-b)/q\bigr),\\[3pt]
\theta_q^D(x,y)=
 \bigl(P_q(x,y),\ x-P_q(x,y)\bigr),
\qquad q\in\mathbb Z\setminus\{0\}.
\end{array}                                                   \tag{6}
\]
Indeed the first output reconstructs \(s=u+v\); substitution into the
second gives \(L_{q,s}u=t\) for a cross owner, or \(qu=y-b\) for C.
This proves both directions of (6) and uniqueness for each nonzero label.
The zero-label case was exhausted separately in §2.1, before division.

For M/C/D, keep a candidate precisely when its own reconstructed floors
satisfy \(m\ne0,\ m\mid n\), and \(n/m=q\).
For G keep it precisely when its own \(q_G=q\).
The own regularity guard and forward equality then hold by (3)–(6).
No target outgoing permission is tested. Conversely every legal source
has one nonzero label and appears in (6), so the list is exhaustive.
There is no inverse-label, inverse-depth or geometric cutoff.

For a fixed nonzero \(q\), each formula in (6) is analytic on all
\(\mathbb R^6\) and is the global inverse of that owner's fixed-label
analytic map. Restrict these diffeomorphisms to their actual arithmetic
Borel cells. The target domains are exactly the Borel preimages of the
source checks under (6). Their inverse images are Borel by the ambient
homeomorphism. The countable source cells are disjoint and cover the
whole legal domain: each actual source has exactly one used quotient.
Thus (6) supplies the complete countable analytic atlas allowed by the
card, without needing to assume that a formal root enumeration is complete.

### 2.3 Every-point values and every-Borel IMAGE

Inverse differentiation of the full six-dimensional maps gives
\[
\begin{array}{ll}
J_q^{M/G}(x,y)=
 \dfrac1{|q|(q^2+\|x+a\|^2)},\\[5pt]
J_q^C(x,y)=|q|^{-3},\\[3pt]
J_q^D(x,y)=
 \dfrac1{|q|(q^2+\|x\|^2)} .
\end{array}                                                   \tag{7}
\]
Each is positive finite on every actual inverse-domain point.
For every Borel \(E\) in that domain, change of variables on the
ambient analytic diffeomorphism proves
\[
\mu(\theta_q(E))=\int_E J_q(z)\,d\mu(z).                \tag{8}
\]
The restriction to a Borel arithmetic cell permits arbitrary null sets
and assigned floor faces. On such a face, (7) is the prescribed value
of that label's analytic germ, not a derivative of the floor function.
An actual source has a unique label and an ambient inverse germ fixed
by (6), so overlapping local charts cannot change this value.
This proves the frozen all-point version and every-Borel IMAGE; it
does not claim that a Radon–Nikodym identity alone canonically fixes
values on null sets.

At a legal source the own clocks are consequently
\[
\begin{split}
\kappa_{M/G/D}(u,v)
 &=\log\bigl(|q|(q^2+\|u+v\|^2)\bigr),\\
\kappa_C(u,v)&=3\log|q| .
\end{split}                                                   \tag{9}
\]
Here each owner uses its own actual quotient. These clocks are
nonnegative because \(q\) is a nonzero integer, but not necessarily
strictly positive. For a cross owner the value is zero exactly when
\(|q|=1,\ u+v=0\); C has zero value exactly when \(|q|=1\).
Zero values and all zero-clock isotropy remain. No positive roof,
time normalization or new measure is inserted, and terminals receive
no outgoing clock value.

## 3. Whole history ledger

Fix one owner \(U\), using only its own branches and clocks.
Let \(D_r\) be its set of sources with \(r\) legal steps, \(D_0=X\), and
\[
S_r(z)=\sum_{j=0}^{r-1}\kappa_U(U^jz),\quad S_0=0,\qquad
\Lambda_r(z)=e^{S_r(z)},\quad\Lambda_0=1.
\]
For a cross owner \(\Lambda_r\) is the product of the \(r\) factors
\(|q_j|(q_j^2+\|u_j+v_j\|^2)\); for C it is the product of \(|q_j|^3\).
No product uses an undefined terminal step.

The full Borel groupoid and its proposed cocycle are
\[
G_U=\{(z,r-s,w):z\in D_r,\ w\in D_s,\ U^rz=U^sw\},\qquad
c(z,r-s,w)=S_r(z)-S_s(w).                              \tag{10}
\]
It inherits the Borel structure of \(X\times\mathbb Z\times X\);
source is \(w\), range \(z\), and equal actual triples, not free inverse
words, are identified. Its lag remains part of the arrow.
Two witnesses of an equal triple differ by a common legal forward
advance; the extra sums along the common tail cancel. Thus \(c\) descends.
For composition, advance the witness with the smaller middle iterate
to the larger one. Legality of the other's middle history transports
to its equal endpoint, so this works also for partial maps.
Cancellation proves additivity; inversion changes the sign. In particular
\[
c(Uz,-1,z)=-\kappa_U(z) .                              \tag{11}
\]
These identities do not complete a terminal trajectory.

The inverse atlas and its finite compositions cover every actual history
piece. A piece from \(w\) to \(z\) has the form
\((U^r)^{-1}\circ U^s\) with all actual cell checks.
Its IMAGE derivative is
\(\Lambda_s(w)/\Lambda_r(z)=e^{-c}\).
Repeated change of variables proves the corresponding every-Borel
identity, including the specified germs at all assigned cuts.
The three full kernels are
\[
\begin{split}
K_{\rm lag}&=\{(z,k,w)\in G_U:k=0\},\\
K_c&=\{(z,r-s,w)\in G_U:\Lambda_r(z)=\Lambda_s(w)\},\\
K_{\rm joint}&=K_{\rm lag}\cap K_c .
\end{split}                                                   \tag{12}
\]
They need not consist only of units.

Define \(\operatorname{Pre}_U(y)\) by EVERY candidate in (6) passing
that owner's source checks, with no target condition. Then
\[
\operatorname{Pre}_U^0(y)=\{y\},\qquad
\operatorname{Pre}_U^{j+1}(y)
 =\bigcup_{w\in\operatorname{Pre}_U^j(y)}\operatorname{Pre}_U(w).
                                                               \tag{13}
\]
Exhaustiveness of (6), followed by induction, proves that (13) contains
exactly every legal \(j\)-step arrival source, at every depth.
Its forward arrival arrow is \((y,-j,z)\), clock \(-S_j(z)\).
All compatible infinite backward chains are retained, without adjoining
new boundary objects. A repeated source description at one depth is
identified, while its different actual lags are not erased.
This exact recursion applies to all \(X\), including terminal targets;
it is not a finite-tree truncation or a finite decision algorithm.

A nonzero isotropy lag at \(z\) is equivalent to two distinct equal legal
forward iterates, hence to an eventual cycle. If that cycle has least
source period \(p\), the complete isotropy is \(p\mathbb Z\): advancing
into the cycle proves necessity, and sufficiently long witnesses give
every multiple. If its own clock sum is \(C_\gamma\), then
\[
c(kp)=kC_\gamma,\qquad H_z:=c(G_z^z)=C_\gamma\mathbb Z.  \tag{14}
\]
This is the entire group, unchanged by incoming tails.
Terminal-ending and noneventually-periodic orbits have trivial source
isotropy and \(H_z=0\), although clocks between their distinct objects
need not vanish.

On the full \(X\times\mathbb R\), an arrow acts as
\((w,h)\mapsto(z,h+c)\). Extension isotropy is the kernel of \(c\)
in source isotropy: trivial for \(C_\gamma\ne0\), or all \(p\mathbb Z\)
for \(C_\gamma=0\). To describe a source orbit choose a base object \(b_0\)
and any actual arrow \(g_z:z\to b_0\). The complete phase is
\[
h+c(g_z)\pmod{H_{b_0}} .                               \tag{15}
\]
Changing the arrow adds an isotropy clock; conversely equality of these
classes gives the required extension arrow. The quotient SET on this
source orbit is thus \(\mathbb R/H_{b_0}\), with actual height translation.
No good coarse topology, global section or phase choice is presumed.
For nonzero \(C_\gamma\), its primitive is \(|C_\gamma|\), with every
positive integer repetition. For zero group there is no positive period.
Equal times on distinct source orbits do not merge packets.

## 4. Complete fixed-window classification

Every point of \(W\) has \(m=n=-1\), including its lower readout faces.
M/C/D therefore satisfy their arithmetic permission and assign \(q=1\);
G independently assigns \(q_G=1\).
Equations (3)–(4) show every owner's guard is nonzero throughout \(W\).
In particular none of the exclusions below is an imported critical guard.

For M/G the first fixed equation forces \(v=a=e_3\).
Write \(u=(r,t,w)\). The second full vector equation then gives
\[
u\times e_3+u+e_1=e_3
\quad\Longleftrightarrow\quad
r+t+1=0,\quad t-r=0,\quad w=1.
\]
Its unique solution is
\[
z_*=(p,a),\qquad p=(-1/2,-1/2,1).                       \tag{16}
\]
It is in \(W\), has its own actual quotient \(1\), and is regular.
No planar or collinear ansatz was imposed: its coordinates were forced
by the full six fixed equations.

For C the first fixed equation again forces \(v=e_3\), and its own
second equation forces \(u=e_3-e_1=(-1,0,1)\).
The lower face \(u_1=-1\) is included, but \(u_2=0\) is the excluded
upper face of \(W\). It is not made into a boundary fixed point.
For D the first equation forces \(v=0\); the second, with actual \(q=1\),
then forces \(u=0\), again outside both readout intervals.
Thus the entire ACTUAL classification is
\[
\boxed{\operatorname{Fix}(M)\cap W
 =\operatorname{Fix}(G)\cap W=\{z_*\},\qquad
\operatorname{Fix}(C)\cap W=\operatorname{Fix}(D)\cap W=\varnothing.}
                                                               \tag{17}
\]
All outer and null faces were included in these equations.
This says nothing about other fixed points or cycles outside \(W\).

At \(z_*\), \(u+v=(-1/2,-1/2,2)\), whose squared norm is \(9/2\).
The full SIX-dimensional determinant and its own clock are
\[
\delta_{M/G}(z_*)=-11/2,\qquad
J_{\rm actual}(z_*)=2/11,\qquad
C_*:=\kappa_{M/G}(z_*)=\log(11/2)>0.                    \tag{18}
\]
This calculation uses all original directions, not just those remaining
after solving the fixed equations.

## 5. Unrestricted basins, whole \(H\), kernels and phases

For each of M and G separately, define
\[
\mathcal B_U=\bigcup_{j\ge0}\operatorname{Pre}_U^j(z_*). \tag{19}
\]
Equations (5)–(6), the own floor tests and (13) make this an explicit
unrestricted inverse recursion. It includes every integer label, every
allowed real predecessor and every depth, including outside \(W\).
Induction proves that \(z\in\mathcal B_U\) exactly when a legal finite
forward iterate of \(z\) is \(z_*\). This is also exactly its full source
orbit: an arrow to a fixed point has such a witness, and conversely
an arrival supplies that arrow. M and G's basins are not identified
merely because their displayed core agrees.
There is no claim that (19) is a finite tree or has been finitely enumerated.

For \(z\in\mathcal B_U\), let \(a(z)\) be its least arrival time and set
\[
\beta(z)=S_{a(z)}(z)-a(z)C_* .                          \tag{20}
\]
Any later arrival time adds the same number of copies of \(C_*\);
therefore it gives the same \(\beta\).
For every \(z,w\in\mathcal B_U\) and every \(k\in\mathbb Z\), choose
\(r\ge a(z),\ s\ge a(w)\) with \(r-s=k\).
Both endpoints have then reached the fixed core, so the arrow exists.
Advancing any other witness into the core gives exactly
\[
G_U|_{\mathcal B_U}
 =\{(z,k,w):z,w\in\mathcal B_U,\ k\in\mathbb Z\},\qquad
c(z,k,w)=\beta(z)-\beta(w)+kC_* .                       \tag{21}
\]
Thus the complete basin kernels, not just necessary conditions, are
\[
\begin{array}{ll}
K_{\rm lag}:& k=0,\\
K_c:& \beta(z)-\beta(w)+kC_*=0,\\
K_{\rm joint}:& k=0,\ \beta(z)=\beta(w).
\end{array}                                                   \tag{22}
\]
Every source isotropy group here is \(\mathbb Z\).
Equation (21) gives every loop clock and only those, hence
\[
H_z=C_*\mathbb Z,\qquad
\text{extension isotropy}=\{0\}.                       \tag{23}
\]
Unseen incoming branches cannot introduce a smaller clock generator:
the necessity part of (21) already covers every such branch and lag.

Using the actual arrival arrow \(z\to z_*\), the complete phase is
\[
h-S_{a(z)}(z)\pmod{C_*\mathbb Z}
   =h-\beta(z)\pmod{C_*\mathbb Z}.                     \tag{24}
\]
Two lifted basin objects are equivalent exactly when these phases agree.
Together, (19) and (24) are exact orbit and phase tests; no finite-time
decision procedure for arbitrary real inputs is claimed.
All real phases form one height circle over each owner's complete
source orbit. Incoming states and phases are not additional packets.
Its primitive is exactly \(C_*=\log(11/2)\), and repetitions are
\(jC_*\), \(j=1,2,\ldots\), with no fractional normalization.
C/D have no fixed-window core, but their full global inverse/history
ledger remains (6)–(15); emptiness of this window is not global absence.

Since \(11/2\) is not an integer, injectivity of the real logarithm
proves that the MAIN primitive cannot be \(\log p\) for an ordinary prime.
This refutes universal MAIN prime-only purity with an owned positive
packet. It is not a numerical fit or an assertion that the rest of its
global periodic ledger has been classified.

## 6. Scoped decision and controls

| Obligation | Exact evidence | Status and limitation |
| --- | --- | --- |
| Divisor-symbolic interface | (1), actual update and own nonzero guard | Established deformation; strong naturalness OPEN |
| Original full-dimensional IMAGE | (3)–(9), all labels/cuts and own controls | Established; zeros allowed, no positive roof |
| Whole legal histories | (10)–(15), kernels, incoming and isotropy | Complete structural ledger, not a global cycle census |
| Complete fixed window | (16)–(17), all six equations and boundaries | M/G one core; C/D none in \(W\) |
| Full fixed basins | (19)–(24), unrestricted exact inverse recursion | All incoming/clock kernels/entire \(H\)/phases retained |
| MAIN universal prime-only purity | Positive primitive \(\log(11/2)\) | REFUTED; STOP / FORK |
| G comparison | Same core and primitive under own source law | PROVES_TOO_MUCH warning, not equal global basins |
| C/D comparison | Own guards, inverse measures and empty fixed window | No transfer of MAIN clocks; no global absence claim |
| Other returns, uniqueness, coverage, global census | Outside the frozen gate | OPEN; no additional gate or tuning |

The same-object ledger is intact. No label, null face, phase or incoming
branch was selected away to improve the result. No dimensional restriction
supplied the clock. The controls do not repair MAIN or contribute borrowed
prime credit. Classical symplectic/suspension fields are NOT APPLICABLE;
arithmetic T1 NOT PASSED, T3 NOT AUDITED, formal Routes UNASSIGNED and
B NOT INVOKED. The portfolio decision is STOP / FORK, without a new
candidate or continuation beyond this frozen short gate.

## 7. Provenance, assistance and reproducibility

The author fully read the original card 1–115 through EOF and used the
previously fully read paper template and ARS bounded author instructions.
The source proposal arose with shared history and informal fixed-equation
feasibility exposure; it was not a blind or sealed prediction.
The author read no current CP1, raw review, final-reviewer or sibling
scientific output. Root owns the card, outcome append and integration.

The only design collision prefixes were the author's
427-divisor-commutator-transfer card 1–64, non-EOF, SHA256
1863dbdbb1c764f9bafee2926e657c43895387cf18e11158aa7efaf8111edbce,
and the same-author helper's 447-double-matrix-sum-product card 1–58,
non-EOF, SHA256
194ab7000250ae96b875ab347446ba2d1c3d3aea5072fc47303c1988c2cee9a1.
Heading metadata exposed appended Outcome titles at 427:97 and 447:101,
not their bodies. The author did not personally reread the helper's
447 prefix. Their displayed interface, regularity and inverse prescriptions
were definition exposure, not imported proof credit.
The shared double-block/product and commutator ancestry is acknowledged;
there is no global novelty or nonconjugacy claim.

After release, helper /root/arithmetic_feedback_scout/dss_g_fixed_author
read only this card's original 1–115 through EOF and independently measured
its matching frozen hash. Its bounded same-author task checked all four
fixed-window systems and their guards, with no incoming or higher-period
classification. It wrote no file and was not a reviewer seat.
The author integrated that check and owns the full derivative, inverse,
IMAGE, unrestricted incoming and clock/phase arguments.

AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Same-model/shared-history
work is NOT_CALIBRATED, not cross-model or independent-error validation.
ARS supplied bounded card-first/evidence-isolation discipline, not
mathematical certification or external publication authority.
Methods were exact cross-product/linear algebra, analytic change of
variables, floor checks and deterministic history identities.
No scientific code, numerical census, network, Git mutation, PDF,
old-file edit, operator, external publication or paper 470 was used.
Mechanical UTF-8, links, identity and hash checks concern artifacts only.
The [overview](README.md) and [claim ledger](claim-ledger.md) preserve
the identical outcome and its scope.
