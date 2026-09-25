# Full-volume obstruction for divisor-quotient matrix reassembly

Candidate ID: ANG-20260923-DCR01.
Outcome: OWNED EIGHT-DIMENSIONAL IMAGE; ENTIRE POSITIVE RETURN LEDGER EMPTY — STOP / FORK
Date: 2026-09-23. Batch GLOBAL-GATE-FEEDBACK-20260923-Q, round 431.
Type: ANG partial Borel transport and retained-lag groupoid.
Classical symplectic/suspension fields NOT APPLICABLE; T3 NOT AUDITED.
Formal Route UNASSIGNED; Route B NOT INVOKED.

## Abstract

The frozen source is a pair of arbitrary real \(2\times2\) matrices.
Current off-diagonal integer readings decide divisibility and a conjugating
integer power. We prove the complete inverse atlas and the prescribed
every-point, every-Borel IMAGE law on the original eight-dimensional
Lebesgue space. Its density is exactly one on every actual inverse branch.
This is a full-coordinate calculation, including derivatives of the
conjugating matrix, not an eigenvalue or commuting-slice calculation.
The permission-off and exponent-off controls independently have the same
volume identity. Consequently every clock arrow is zero, the entire
return subgroup at every source point is \(\{0\}\), and height translation
has no positive return anywhere. All incoming histories, terminals, zero-clock
isotropy and distinct packets remain. Empty positive data fail the required
nonemptiness; they do not constitute a vacuous prime-period success.

## 1. Frozen source and exact arithmetic interface

The governing input is the original 90-line [candidate card](candidate-card.md),
SHA256 ac780971592ee4b848898560e48290a2a2ab7e6a7b5de157d7b6cf605613be65.
No measure, terminal convention, clock or phase-space restriction is changed.
Write \(X=M_2(\mathbb R)^2\), with its usual Borel structure and
\(\mu=\operatorname{Leb}_8\) in the original matrix entries. For \(z=(A,B)\), set
\[
 m=\lfloor B_{12}\rfloor,\qquad n=\lfloor A_{12}\rfloor,\qquad
 D_T=\{\det B\ne0,\ m\ne0,\ m\mid n\}.
\]
On \(D_T\), \(q=n/m\in\mathbb Z\), and
\[
 T(A,B)=(B,B^{-q}AB^q).                                      \tag{1}
\]
There is no condition on \(\det A\). Negative entries, negative exponents,
zero quotient, units and every assigned integer face remain. Points outside
the legal domain are forward terminals, with identities and all actual
incoming arrows, not absorbing loops. In particular a legal source can
have a terminal target. Integer powers are only taken of invertible \(B\).

For positive integers \(N\ge2\) and \(1<d<N\), the frozen interface is
\[
 A_N=\begin{pmatrix}1&N\\0&1\end{pmatrix},\qquad
 B_d=\begin{pmatrix}1&d\\1&d+1\end{pmatrix}.
\]
Here \(\det B_d=1\), \(n=N,m=d\), so MAIN permission is exactly \(d\mid N\).
The actual quotient enters the matrix word relation
\(A_NB_d^q=B_d^qC\), with \(C=B_d^{-q}A_NB_d^q\).
This preserves the proper-divisor symbolic permission as an interface to
noncommutative transport; future readings are taken from the actual output.
The interface is not an invariant restriction or a selected periodic section.
Primes, prime logs and zero data are not inputs. The particular entry readout
is a declared design whose strong naturalness is not established.

The two controls have their own full \(X,\mu\), domains and arrows:

| Owner | Legal source | Exponent in \((B,B^{-e}AB^e)\) |
| --- | --- | --- |
| MAIN \(T\) | \(D_T\) | \(e=n/m\) |
| Permission-off \(G\) | \(\det B\ne0\) | \(e=\lfloor n/m\rfloor\) if \(m\ne0\), otherwise \(0\) |
| Exponent-off \(Q\) | \(D_T\) | \(e=1\) |

In particular \(Q\) keeps MAIN permission but does not retain unused exponent
labels, while \(G\) must not acquire MAIN divisibility restrictions.

## 2. Complete actual inverse atlases

For any integer \(e\), define on the two open eight-dimensional sets
\[
 \Omega=\{(A,B):\det B\ne0\},\quad
 \Omega'=\{(U,V):\det U\ne0\},\qquad
 \theta_e(U,V)=(U^eVU^{-e},U).                               \tag{2}
\]
The map \(F_e(A,B)=(B,B^{-e}AB^e)\) and (2) are mutually inverse real-analytic
maps \(\Omega\leftrightarrow\Omega'\): substitution cancels the adjacent
integer powers. This holds for arbitrary, including singular, \(A,V\).

For MAIN, enumerate every \(m,n\in\mathbb Z\) with \(m\ne0,m\mid n\).
Put \(e=n/m\) and retain the target set
\[
 E^T_{mn}=\{(U,V)\in\Omega':
     \lfloor U_{12}\rfloor=m,\qquad
     \lfloor(U^eVU^{-e})_{12}\rfloor=n\}.                     \tag{3}
\]
The actual inverse is \(\theta_e\) restricted to (3). Its source satisfies
the full MAIN domain, and direct substitution gives the specified target.
Conversely any actual preimage has \(B=U\), its own unique readings \(m,n\),
and then \(A=U^eVU^{-e}\); it is in this list.

For \(G\), enumerate all integers \(m,n\), compute its own exponent from the
table, and use (3) with that exponent and without \(m\ne0,m\mid n\).
The same substitution proves both directions with precisely the \(G\) domain.
For \(Q\), there is just one candidate \(\theta_1(U,V)\); its actual domain is
\[
 E^Q=\{(U,V)\in\Omega':\theta_1(U,V)\in D_T\}.                 \tag{4}
\]
No quotient label produces another copy of this single actual preimage.
For MAIN and \(G\), two labels cannot describe the same actual predecessor:
its two floors recover the labels. Different predecessors are never merged.

All sets above are Borel; each branch is a restriction of a global analytic
diffeomorphism between \(\Omega'\) and \(\Omega\). Thus branch images of Borel
sets are Borel. No target-next-step permission is imposed. Targets with
singular \(U\) have no one-step preimage; singular \(V\) is not excluded.
There are no missing floor endpoints or artificial eigenbasis boundaries.

## 3. The complete eight-dimensional IMAGE calculation

Fix any integer \(e\), and order input coordinates as \((U,V)\) and output
coordinates as \((U^eVU^{-e},U)\). Its derivative has block form
\[
 D\theta_e=\begin{pmatrix}E_e&L_e\\ I_4&0\end{pmatrix},
 \qquad L_e(H)=U^eHU^{-e}.                                  \tag{5}
\]
Here \(E_e\) contains all derivatives with respect to the changing matrix
\(U\); these are not discarded. Swapping the two four-row blocks has sign
\((-1)^{16}=1\), and gives a block triangular matrix. Consequently
\(\det D\theta_e=\det L_e\), independently of \(E_e\).
Left multiplication by a \(2\times2\) matrix \(P\) on \(M_2(\mathbb R)\)
has determinant \((\det P)^2\), by its separate action on two columns.
Right multiplication has the same determinant, by two rows. Therefore
\[
 \det L_e=(\det U^e)^2(\det U^{-e})^2=1,\qquad
 J_e=|\det D\theta_e|=1.                                    \tag{6}
\]
This calculation covers every invertible real \(U\), every real \(V\) and
every signed integer exponent. It uses all eight coordinates, including
noncommuting and singular-second-matrix points.

For every Borel set \(E\) contained in any actual inverse target domain,
change of variables for the analytic diffeomorphism (2) gives
\[
       \mu(\theta_e(E))=\int_E J_e\,d\mu=\mu(E).              \tag{7}
\]
The prescribed analytic germ is available on the open set \(\Omega'\)
even when the actual branch target lies on an integer cut. Equation (6)
therefore supplies the required positive finite pointwise version there
as well, not merely an almost-everywhere density. Null exceptional fibres
and legal integer interfaces are included. The version is fixed by the
card's germ rule, not inferred uniquely from a null-set measure equation.

For MAIN apply (5)–(7) separately to every actual \(e=n/m\) branch.
For \(G\) apply them to each of its own floor-quotient branches, including
\(m=0,e=0\). For \(Q\) apply them to the single germ \(\theta_1\) on (4).
Thus each owner independently has the complete IMAGE law and
\[
             \kappa_F(z)=-\log J_F(Fz)=0\quad(z\in D_F),
             \qquad F\in\{T,G,Q\}.                         \tag{8}
\]
There is no next-step \(\kappa_F\) at a terminal. A terminal identity still
has clock zero. Branchwise volume preservation must not be confused with
preservation of measure by a possibly many-to-one whole forward map:
overlapping branch images are united, not blindly summed. Nothing here
asserts a globally invertible MAIN or \(G\), or a symplectic form.

## 4. Every history, kernel and incoming branch

For each owner separately let \(D_F^{(0)}=X\), and let \(D_F^{(r)}\) consist
of points whose first \(r\) steps are legal. All are Borel. Define
\[
 {\cal G}_F=\{(z,r-s,w):z\in D_F^{(r)},w\in D_F^{(s)},
                       F^rz=F^sw,\ r,s\ge0\}.              \tag{9}
\]
This has the inherited Borel structure in \(X\times\mathbb Z\times X\).
Equal triples, not differently written iteration witnesses, are identified;
different lags remain. Source is \(w\), range is \(z\), inverse reverses them
and the lag, and composition adds lags. To verify composition for witnesses
\((r,s)\) and \((a,b)\) through \(w\), advance the first pair if \(a\ge s\),
or the second if \(s\ge a\). The required advance exists along the known
legal orbit of \(w\), including when its later endpoint is terminal.
This gives another valid equality, without adding a future step at a terminal.
Countable unions of the corresponding Borel equalities give (9).

Set \(S_0=0\) and \(S_r=\sum_{j=0}^{r-1}\kappa_F(F^jz)=0\) on its legal domain.
Then the prescribed cocycle
\[
 c_F(z,r-s,w)=S_r(z)-S_s(w)=0                               \tag{10}
\]
is independent of every witness and additive under composition.
The forward arrow \((Fz,-1,z)\) has clock \(-\kappa_F(z)=0\);
an inverse one-step arrow \((z,1,Fz)\) has clock \(+\kappa_F(z)=0\).
There is no sign reversal hidden by choosing a positive roof.
For a fixed finite choice of actual forward and inverse branches, the arrow
from \(w\) to \(z\) is their composition, restricted by every intermediate
source check. Both directions of every branch have determinant one, so
the chain rule gives IMAGE density \(\exp(-c_F)=1\) for this arrow germ.
Repeated change of variables proves its every-Borel IMAGE identity.
These countably many finite branch choices cover (9); (10) agrees even
where different choices describe the same triple. This is the history
IMAGE owner, not a separate clock attached to the formal lag.

The exact full kernels are
\[
 \ker c_F={\cal G}_F,\qquad
 \ker\ell_F=\ker(\ell_F,c_F)
 =\{(z,0,w):\exists r\ge0,\ F^rz=F^rw\text{ legally}\}.       \tag{11}
\]
Equal-level coalescence is not silently identified with the unit arrows.
For \(Q\) specifically, (2) and (4) show that its partial forward map is
injective. Every legal iterate is injective, so its last kernel in (11)
is precisely the units. For MAIN and \(G\), (11) is the full exact kernel,
with all its potential distinct equal-level predecessors retained.

Here is an unrestricted constructive description of every incoming history.
Let \(P^F_1(y)\) be the entire actual inverse list (3) or (4), and set
\[
 P^F_0(y)=\{y\},\qquad
 P^F_{j+1}(y)=\bigcup_{v\in P^F_j(y)}P^F_1(v).              \tag{12}
\]
Induction proves \(P^F_j(y)=\{z\in D_F^{(j)}:F^jz=y\}\): the last statement
follows by splitting or appending the first legal step. In particular (12)
works for terminal \(y\), all integer cuts and singular fibres.
No depth, integer exponent or cardinality cutoff occurs. Set unions remove
duplicate actual points, not different source points or retained lags.
For a source \(w\), every arrow ending at a point \(z\) is captured by
choosing \(s\) with \(w\in D_F^{(s)}\), then \(r\ge0\) and
\(z\in P^F_r(F^sw)\), with lag \(r-s\). This describes the entire source
orbit and all arrows, including any multiple witnesses of the same triple.
Finite inverse-history strings and all their infinite compatible continuations
are retained by these rules; they are not promoted to extra packet labels.
For a terminal \(\tau\), its full source orbit is
\(\bigcup_{j\ge0}P^F_j(\tau)\). For a least cycle \(C\), it is
\(\bigcup_{y\in C,j\ge0}P^F_j(y)\). Any tail equality with the terminal
or the cycle forces precisely this eventual entry, proving both descriptions.
The unrestricted general formula above covers all other source orbits.

## 5. Entire isotropy, phases and the global empty ledger

For a deterministic partial map, a nonzero isotropy lag at \(z\) means
\(F^rz=F^sz\) for distinct \(r,s\). Assume \(r>s\). The segment starting at
\(F^sz\) repeats legally, hence \(z\) is eventually periodic and never
subsequently terminates. Conversely an eventual least cycle of length
\(p\ge1\) supplies every lag in \(p\mathbb Z\), by comparing sufficiently
late legal iterates. Any equality of two iterates can be advanced to that
cycle, so its difference is divisible by the least period. Thus exactly
\[
 {\cal G}_{F,z}^{z}\simeq
 \begin{cases}
 p\mathbb Z,&z\text{ eventually reaches a least }p\text{-cycle},\\
 \{0\},&z\text{ is not eventually periodic}.
 \end{cases}                                               \tag{13}
\]
The second case includes terminals and every eventually terminating point.
This is an exhaustive conditional classification, not an enumeration of
the actual matrix cycles. It applies to MAIN and each control on its own.

For every source point, including every case in (13), its ENTIRE image is
\[
       H_{F,z}=c_F({\cal G}_{F,z}^{z})=\{0\}.                \tag{14}
\]
On the complete height extension \(X\times\mathbb R\), every arrow acts as
\((w,h)\mapsto(z,h)\). Its isotropy at \((z,h)\) is therefore the full
source isotropy (13), not just the unit arrow.
At every fixed height its lag, clock and joint kernels are exactly the
corresponding kernels in (11); there are no arrows between distinct heights.
For each source orbit \(O\), the extension orbits are exactly
\(O\times\{h\}\), one for every \(h\in\mathbb R\). Thus its full physical
phase space is \(\mathbb R/H=\mathbb R\), not a chosen phase or a circle.
For any choice of actual arrow from \(z\) to a base point \(b\), the transported
phase is \(h+c(g_z)=h\); changing that arrow adds an element of \(H=\{0\}\).
In particular an incoming point with \(F^az=b\) carries phase
\(h-S_a(z)=h\). These formulas include every depth in (12).

Height translation on the orbit SET is \([z,h]\mapsto[z,h+t]\). If it
returned for \(t\ne0\), an actual extension arrow would have to change height
by \(t\), contrary to (10). It is free everywhere. No regular Borel quotient
or classical suspension is assumed in this set-level argument.
Consequently MAIN, \(G\) and \(Q\) all have an EMPTY positive primitive
return ledger. A nontrivial source cycle is not erased: its least symbolic
period \(p\), all multiples \(kp\) and all zero-clock isotropy remain.
None has a least positive clock generator. Selecting a repetition, changing
orientation or taking an absolute value cannot turn zero into a positive time.
Different source orbits are never merged because their clocks agree.
The conclusion is global and independent of whether any particular cycle exists.

## 6. Controls, gate and limits

| Owner / test | Established on the full frozen owner | Decision |
| --- | --- | --- |
| MAIN | Exact arithmetic interface, complete inverse atlas, \(J=1\), \(H=0\) everywhere | Nonempty-positive benchmark fails |
| \(G\), permission-off | Its own all-integer atlas, including \(m=0\); \(J=1,H=0\) | Removing the arithmetic gate does not restore time |
| \(Q\), exponent-off | Its single actual inverse and retained MAIN domain; \(J=1,H=0\) | Fixing the exponent does not restore time |
| Full-coordinate ownership | The \(U\)-derivative block is retained in the eight-dimensional determinant | No scalar, commuting or eigenbasis selection |
| Null and terminal ownership | Prescribed germ on every legal cut; (9)–(14) retain terminal incoming and zero isotropy | No almost-everywhere exception |

T0 Borel/IMAGE/history ownership is established for the specified category.
The proper-divisor source interface is exact, but the necessary endogenous
positive-clock target fails: T1 is NOT PASSED. T2's full packet and repetition
convention is established and its required positive nonemptiness fails.
Neither the universal prime-time condition nor uniqueness is credited from
the empty set; all-prime coverage is impossible for this positive ledger.
Strong naturalness of the entry-based arithmetic design remains OPEN.
Classical A0–A2 coordinates are NOT APPLICABLE, formal Route UNASSIGNED,
T3 NOT AUDITED and Route B NOT INVOKED.

The precommitted global gate therefore decides STOP / FORK. There is no
fixed-point table, higher-period census or chosen family of cycles.
This is not a no-go for every arithmetic action or every possible physical
clock: it concerns these three specified transports, original Lebesgue
measure, prescribed full-dimensional IMAGE and retained-lag extension.
Replacing the measure, using an unstable subdeterminant, adding a roof or
restricting to a section would create a different owner, not rescue this one.
Local branch volume preservation alone is not symplectic or global
many-to-one measure preservation.

## 7. Methods, exposure and reproducibility

The author read the frozen card completely before proof and the local paper
template. The method is exact inverse substitution, an eight-dimensional
block determinant, analytic change of variables, and elementary partial-map
history algebra. There are no numerical experiments, orbit cutoffs,
external data, new literature claims, operators, PDFs or Git operations.
The card's original 90-line prefix is the input lock; later root-owned
outcome text is not an input to this derivation.

Definition scouting read 408 card lines 1–75 and 407 card lines 1–55, both
non-EOF original prefixes, with respective SHA256
e510fd67204c529c745e272cb9ac38673446efb7c2fb510321084763396fb00b and
e6d438a4aa4eecec919d522c6819ff7d64a5d5c7935eff9b8238ee98bc903aa2.
Outcome headings for those cards and heading-only 345/336 metadata were
exposed; their outcome bodies were not read. These were definition comparisons,
not theorem imports. The informal pre-freeze expectation of volume cancellation
is disclosed; this was not blind discovery or sealed preregistration.

An author-side helper read only the frozen 431 card to check the conditional
zero-clock general history/isotropy ledger. The author independently derived
the inverse/IMAGE proof and checked the helper's history reasoning before
integration. That helper is not an additional independent review seat.
No current raw/reviewer or sibling scientific text was consulted by the author.
Shared history and same-model internal checks are NOT_CALIBRATED.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified.

Author surfaces are this paper, the [claim ledger](claim-ledger.md) and
[package README](README.md). Root owns the candidate card and separate review
integration. This paper supplies the complete proof behind those summaries;
it does not claim independent peer validation or global architectural novelty.
