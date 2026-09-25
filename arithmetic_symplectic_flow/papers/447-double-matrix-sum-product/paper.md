# An owned eight-dimensional image clock with a composite fixed return

Candidate ID: ANG-20260924-DMS01. Paper 447, version 1.
Outcome: OWNED EIGHT-DIMENSIONAL IMAGE; COMPOSITE FIXED RETURN — STOP / FORK
Date: 2026-09-24. Batch ADMISSION-EXIT-20260924-T, round 3/5.
Type: arithmetic Borel retained-lag groupoid and real cocycle extension.
Classical symplectic/suspension fields: NOT APPLICABLE. T3: NOT AUDITED.
Formal Route coordinates: UNASSIGNED. Route B: NOT INVOKED.

## Abstract

We audit the frozen double-matrix map on all eight real entries with their
original Lebesgue measure. A current divisibility quotient enters the product
update, while the updated matrix supplies the next arithmetic observation.
We construct all actual inverse branches, prove their every-Borel image
formula with a specified analytic pointwise density at all legal points, and
derive the complete retained-lag clock and isotropy conventions. The global
fixed sets of MAIN and permission-OFF each consist of one matrix pair; the
displacement-OFF control has none. The MAIN fixed basin, with all its actual
incoming branches, has entire period group \((\log 4)\mathbb Z\). Thus its
primitive time is \(\log 4\), not the logarithm of an ordinary prime. This
one owned adverse packet stops the candidate without a higher-period census.

## 1. Identity, scope, and source interface

The governing input is the [frozen card](candidate-card.md), original lines
1–99, SHA256 d245ab75ce70b7eab010d3c525cd8846950b093aade6587fab3b24e9a318a7ac.
All proofs below concern that object and its two separately owned controls.
The [claim ledger](claim-ledger.md) separates established claims from limits.
The later [review record](evidence/review.md) is a root-managed artifact, not
an input to this author proof.

Put \(X=M_2(\mathbb R)^2\), with its usual topology, Borel sets, and Lebesgue
measure \(\mu_8\) in the original entries. Fix \(C=\operatorname{diag}(1,2)\)
and \(I=I_2\). For \(z=(A,B)\) read
\[
m(z)=\lfloor B_{11}\rfloor,\qquad n(z)=\lfloor B_{22}\rfloor.
\]
MAIN, denoted \(T_M\), requires \(m\ne0,\ m\mid n\) and uses \(q=n/m\).
The permission-OFF owner \(T_G\) instead uses
\[
q_G=\begin{cases}\lfloor n/m\rfloor,&m\ne0,\\0,&m=0.\end{cases}
\]
The displacement-OFF owner \(T_D\) has MAIN's arithmetic rule.
For \(O=M,G,D\), write \(\delta_M=\delta_G=1,\ \delta_D=0\), and
\[
T_O(A,B)=(A+B-\delta_O I,\ AB+q_O(A,B)C).                 \tag{1}
\]
Every owner additionally requires its own full eight-dimensional derivative
guard specified below. There is no restriction to diagonal, commuting,
symmetric, invertible, positive, or integer matrices.

All objects outside an owner's source domain are terminal: no next iterate
and no next-step clock are assigned there. They retain their units and every
actual incoming history. In particular, a legal image may be terminal.
Floor cuts, zeros, signed quotients, and measure-zero objects are not removed.
No terminal is replaced by a reset or an absorbing loop.

The exact proper-divisor interface is
\[
(A,B)=(0,\operatorname{diag}(d,N)),\quad
N,d\in\mathbb Z,\quad N\ge2,\quad 1<d<N.                 \tag{2}
\]
We prove below that its geometric guard is nonzero, so MAIN admission there
is exactly \(d\mid N\). This realizes divisor-symbolic admission followed by
active matrix sum/product transport and a fresh observation of the resulting
matrix. It is not a passive integer register. The positions of the readouts
and the choices of \(C,I\) are declared design data, not proved canonical.

## 2. Full derivative and complete actual inverse relation

For fixed \(q,\delta\), let
\[
F_{q,\delta}(A,B)=(A+B-\delta I,\ AB+qC).
\]
Its real derivative on the full tangent space is
\[
DF_{q,\delta}(H,K)=(H+K,\ HB+AK)=\mathcal L_{A,B}(H,K).  \tag{3}
\]
Let \(L_AH=AH,\ R_BH=HB\) on the four-dimensional matrix space and put
\[
\Delta(A,B)=\det_{\mathbb R^4}(L_A-R_B).
\]
In column-vectorization, the eight-dimensional block derivative is
\[
\begin{pmatrix}I_4&I_4\\B^{\mathsf T}\otimes I_2&I_2\otimes A\end{pmatrix}.
\]
Subtracting \(B^{\mathsf T}\otimes I_2\) times its first block row from its
second gives
\[
\det_{\mathbb R^8}DF_{q,\delta}
=\det(I_2\otimes A-B^{\mathsf T}\otimes I_2)=\Delta(A,B). \tag{4}
\]
This is the determinant of the entire map, not a selected tangent direction.
The regular locus \(\mathcal R=\{\Delta\ne0\}\) is open. Each owner's domain
is its arithmetic domain intersected with \(\mathcal R\), a Borel set.
Neither \(q\) nor \(\delta\) directly enters (3); both change actual transport,
and hence can change subsequent arithmetic and geometric derivatives.

At (2), \(L_A-R_B=-R_B\). Right multiplication by this invertible diagonal
matrix has determinant \((dN)^2\), with no sign change in dimension four.
Thus \(\Delta=d^2N^2>0\), proving the exact admitted divisor interface.

For a target \(y=(U,V)\), enumerate MAIN or D labels \(m\ne0,n\in\mathbb Z\)
with \(m\mid n,\ q=n/m\). For G enumerate all \(m,n\in\mathbb Z\) and use
its own \(q_G(m,n)\). For each label take every real matrix solution
\[
A^2-A(U+\delta_O I)+V-qC=0,\qquad
B=U+\delta_O I-A.                                     \tag{5}
\]
Retain it exactly when its two \(B\) floors equal the enumerated labels,
its owner's arithmetic rule holds, \(\Delta(A,B)\ne0\), and (1) gives \(y\).
Denote the resulting set of actual points by \(\mathcal P_O(y)\).
Repeated descriptions of one point are identified, not distinct arrows.

This is necessary because the first component of (1) determines \(B\);
substitution into \(AB+qC=V\) gives (5), preserving multiplication order.
It is sufficient because reversing that substitution verifies both components.
All nonsymmetric and noncommuting real roots are retained. Target permission
is irrelevant to this one inverse step. D uses \(U\), not MAIN's \(U+I\).
No assumption of finitely many algebraic roots is needed.

For completeness, the derivative of a local inverse can also be specified
without a chosen matrix-root formula. Given a target tangent \((P,Q)\), solve
\[
H=(R_B-L_A)^{-1}(Q-AP),\qquad K=P-H.                   \tag{6}
\]
The source guard makes this a unique eight-dimensional inverse derivative.

## 3. Countable atlas and every-point IMAGE owner

For each fixed \(q,\delta\), use the card's ordered rational open balls whose
closures lie in \(\mathcal R\) and on which \(F_{q,\delta}\) is injective.
The inverse function theorem supplies an injective neighborhood of every
regular point; a sufficiently small rational ball containing that point has
closure inside this neighborhood. Hence the eligible balls cover \(\mathcal R\).
This proves coverage, not an algorithm for deciding an injectivity predicate.

Intersect these balls with an owner's actual \(q\)-source and subtract earlier
eligible source pieces. Actual \(q\) is single-valued, so the resulting
countable pieces \(E_\alpha\) partition its entire legal domain.
The restriction of \(F_{q,\delta}\) to an eligible ball is an analytic
diffeomorphism onto an open set: it is both injective and a local
diffeomorphism. Its inverse restricted to
\(B_\alpha=F_{q,\delta}(E_\alpha)\) is an actual inverse \(\theta_\alpha\).
Both \(E_\alpha\) and \(B_\alpha\) are Borel. These pieces also show that every
actual inverse fibre is at most countable; this is not a finite-root assertion.
Equation (5) and this atlas give exactly the same predecessor relation.

The smooth change-of-variables formula on the ambient ball, restricted to any
Borel \(E\subseteq B_\alpha\), proves the precise IMAGE convention
\[
\mu_8(\theta_\alpha(E))
 =\int_E J_\alpha(y)\,d\mu_8(y),\qquad
J_\alpha(y)=\frac1{|\Delta(\theta_\alpha(y))|}.           \tag{7}
\]
The formula holds for every Borel set, with extended integrals when necessary.
The displayed density is specified at every actual point and satisfies
\(0<J_\alpha(y)<\infty\). On overlapping local inverse germs through the
same actual source, local uniqueness and (6) make the values agree.

Floor boundaries are included using their actual assigned floor and the
analytic fixed-label extension. Their density is thus the displayed value,
not an arbitrary almost-everywhere modification. We do not assert that the
piecewise arithmetic map or its clock is globally continuous across cuts.
Equation (7) alone would not determine values on null sets; the frozen
analytic-germ prescription does. All three owners use this same prescription
on their own source domains and actual histories, with no reweighting.
Consequently their legal one-step clocks are
\[
\kappa_O(z)=-\log J_{\alpha(z)}(T_Oz)=\log|\Delta(z)|.    \tag{8}
\]
Equality of the displayed function on common sources does not identify the
different domains, maps, future orbits, or groupoids.

## 4. Full retained-lag groupoid, kernels, and real extension

All statements in this section apply separately to \(O=M,G,D\). Write \(T\)
for that owner, \(D_r\) for the Borel domain of \(r\) legal steps, and
\[
S_0=0,\quad S_r(z)=\sum_{j=0}^{r-1}\kappa(T^jz),\quad
M_r(z)=e^{S_r(z)}=\prod_{j=0}^{r-1}|\Delta(T^jz)|.       \tag{9}
\]
Here \(D_0=X,\ M_0=1\); \(S_r,M_r\) are used only on \(D_r\).
Take all triples
\[
\mathcal G=\{(z,r-s,w):z\in D_r,\ w\in D_s,\ T^rz=T^sw\}.
\]
Source is \(w\), range is \(z\). Equal actual triples are identified while
their integer lag remains; no free inverse-word multiplicity is added.
This is a Borel groupoid, since for each lag its relation is a countable
union of equality sets of Borel iterates on their actual domains.
Multiplication adds lags and inversion interchanges the endpoints.

Set
\[
c(z,r-s,w)=S_r(z)-S_s(w)=\log\frac{M_r(z)}{M_s(w)}.      \tag{10}
\]
Two representations of the same triple differ by a common number of extra
iterations on the shared endpoint. Their additional clock sums are equal,
so (10) descends. For composable triples, align their two iteration lengths
at the middle object by their maximum; this is legal because the longer
middle iterate exists. Cancellation of its common sum proves additivity.
Thus \(c(g^{-1})=-c(g)\); the actual forward arrow
\((Tz,-1,z)\) has clock \(-\kappa(z)\), not \(+\kappa(z)\).

The cocycle belongs to actual transport beyond one step as well. Refine any
finite histories into the countable injective pieces from §3. The resulting
arrow branch \(w\mapsto z=(T^r)^{-1}(T^sw)\) has full determinant modulus
\[
\frac{M_s(w)}{M_r(z)}=e^{-c(z,r-s,w)}.
\]
Composition of the corresponding smooth local extensions and their Borel
restrictions proves its every-Borel IMAGE formula with this pointwise value.
No total-map invariant measure or globally smooth quotient is claimed.

The full kernels, including all null and terminal objects, are exactly
\[
\begin{split}
K_{\rm lag}&=\{(z,0,w)\in\mathcal G\},\\
K_c&=\{(z,r-s,w)\in\mathcal G:M_r(z)=M_s(w)\},\\
K_{\rm joint}&=K_{\rm lag}\cap K_c.
\end{split}                                           \tag{11}
\]
These formulas include every witness \(r,s\ge0\) and are representation
independent; no kernel is asserted to consist only of units.

Extend every object to \(X\times\mathbb R\). An arrow \(g:w\to z\) acts by
\((w,h)\mapsto(z,h+c(g))\). Height translations act on the full orbit SET.
For \(H_b=c(\operatorname{Iso}_{\mathcal G}(b))\), choose any actual arrow
\(g_z:z\to b\) within one source orbit. Its extension orbits are parametrized by
\[
h+c(g_z)\pmod {H_b}.                                  \tag{12}
\]
Another such arrow changes this value by an isotropy clock in \(H_b\).
Conversely equality modulo \(H_b\) supplies an isotropy arrow, proving (12)
is a complete orbit-set description. This is an orbitwise argument, not a
claim of a measurable global selector, Hausdorff quotient, or classical flow.

For a deterministic partial map a nonzero isotropy lag occurs exactly when
the forward orbit eventually reaches a periodic cycle. Indeed unequal legal
iterates that coincide give a repeated point and thereafter a legal cycle.
If its least period is \(p\), every and only lag in \(p\mathbb Z\) occurs.
Writing \(C_\gamma\) for the sum of (8) around that least cycle gives
\[
\operatorname{Iso}_{\mathcal G}(z)=p\mathbb Z,\quad
c(kp)=kC_\gamma,\quad H_z=C_\gamma\mathbb Z.             \tag{13}
\]
The entry path cancels in this formula. Extension isotropy is all \(p\mathbb Z\)
if \(C_\gamma=0\), and just lag zero otherwise. Without eventual periodicity,
source isotropy, extension isotropy, and \(H_z\) are all trivial.
In particular this latter case includes all terminal-ending histories.
Their inter-object arrows may still have nonzero clock; they are not deleted.

Thus a positive closed height orbit exists over that source orbit precisely
when \(C_\gamma\ne0\); its primitive time is \(|C_\gamma|\), with every positive
integer repetition. If \(C_\gamma=0\), the height fibre is \(\mathbb R\), not a
positive-time circle, even though nontrivial zero-clock source isotropy remains.
These are exact entire-group descriptions, not selected return-word values.
Other higher-period cycles are not classified by this paper.

## 5. Complete global fixed sets and their full basins

For either MAIN or G, equality of the first component of (1) with \(A\)
forces \(B=I\), without a commutativity assumption. Its actual readings are
\(m=n=1\); hence each owner's own quotient is \(q=1\).
Equality of the second component with \(B\) then forces \(A+C=I\).
The only possible fixed point of either owner is therefore
\[
F=(I-C,I).                                             \tag{14}
\]
It is actually legal: divisibility holds, and at this point
\[
(L_A-R_B)H=-CH,\qquad \Delta(F)=(\det C)^2=4.            \tag{15}
\]
Left multiplication by \(C\) acts on each of the two columns, which explains
the square in (15); using only one column would not be this owner.
Direct substitution verifies (14) is fixed. Thus this is a complete global
classification on all eight coordinates for each of MAIN and G.

For D, equality of its first component with \(A\) forces \(B=0\).
Its own actual \(m=0\) violates its arithmetic permission, irrespective of
any formal second equation. Hence D has no legal fixed points anywhere in
\(X\). No terminal is counted as a fixed point by adjoining an identity step.
This is not a statement that D has no higher-period returns.

At \(F\), the all-point inverse density is \(1/4\) and the forward clock is
\[
C_F=\kappa(F)=\log4.                                  \tag{16}
\]
The fixed point is null for \(\mu_8\), but §3 supplies its specified analytic
pointwise density; it cannot be changed by choosing another null-set version.

For each \(O=M,G\), define its full incoming sets by the exact recursion
\[
\mathcal B^O_0=\{F\},\qquad
\mathcal B^O_{j+1}=\bigcup_{y\in\mathcal B^O_j}\mathcal P_O(y),
\qquad \mathcal B^O=\bigcup_{j\ge0}\mathcal B^O_j.       \tag{17}
\]
Here \(\mathcal P_O\) is the unrestricted real-root relation (5), with every
integer label and all actual source checks. Since \(F\) is fixed, the sets
are nested; they are at most countable. Induction proves that
\(\mathcal B^O_j=\{z:T_O^jz=F\text{ legally}\}\), so (17) is an exact entire
basin, not a diagonal, finite-depth, bounded-entry, or fixed-quotient census.
The two owners' basins are not identified. The same inverse recursion starting
at any object specifies all its finite incoming histories, including terminals.

The full source orbit of \(F\) equals \(\mathcal B^O\): an arrow to a fixed
point says some iterate of the other endpoint is \(F\), and the converse is
immediate. Every retained lag \(k\in\mathbb Z\) occurs between any two points
of this basin, by taking sufficiently long iterates beyond their entry times.
For \(z\in\mathcal B^O\) let \(a(z)\) be its first entry time and put
\[
\beta_O(z)=S_{a(z)}(z)-a(z)\log4.
\]
Every longer entry gives the same value. Formula (10) becomes, for all basin
arrows, the complete identity
\[
c(z,k,w)=\beta_O(z)-\beta_O(w)+k\log4.                  \tag{18}
\]
Thus on this whole orbit \(K_{\rm lag}\) contains all pairs with \(k=0\);
\(K_c\) consists exactly of the triples with
\(\beta_O(z)-\beta_O(w)+k\log4=0\); the joint kernel imposes both conditions.
At every basin point the entire source isotropy is \(\mathbb Z\), its entire
clock image is \((\log4)\mathbb Z\), and extension isotropy is trivial.
Incoming branch multiplicity creates no extra isotropy beyond the actual
retained triples, so it cannot shrink the positive generator.

The phase of a lifted basin point \((z,h)\), transported to \(F\), is exactly
\[
h-S_{a(z)}(z)\pmod {(\log4)\mathbb Z}
 =h-\beta_O(z)\pmod {(\log4)\mathbb Z}.                 \tag{19}
\]
The first expression uses the actual forward arrow of lag \(-a(z)\).
All phases are retained. They form one circle of the height-translation action
over this single full source orbit, not a separately selected centre or one
new packet for each phase. Its primitive period is \(\log4\), and its complete
positive repetition list is \(j\log4,\ j=1,2,\ldots\).
There is no isotropy clock \(\log2\) in (18) at one object; halving the period
would change the frozen clock or groupoid. D has no fixed basin to which this
argument could transfer, while its full general ledger remains §4.

## 6. Decision, controls, and limits

The MAIN packet in §5 is nonempty and fully owned, but \(4\) is composite.
If \(\log4=\log p\) for an ordinary prime \(p\), injectivity of the real
logarithm would give \(p=4\), impossible. Thus the benchmark requiring every
positive primitive to be a prime logarithm fails. The same local fixed result
in G is separately proved; arithmetic permission does not eliminate this
packet. D's empty fixed set checks the displacement mechanism, not a rescue
of MAIN or a positive-ledger result for D.

| Obligation | Same-object finding | Decision or boundary |
| --- | --- | --- |
| T0 source and inverse owner | Full \(X,\mu_8\), every actual inverse, all terminals | Established |
| Pointwise IMAGE clock | Full eight-dimensional analytic branch density (7) | Established, not a positive roof |
| Divisor-symbolic interface | Exact integer proper-divisor admission (2) | Established; strong naturalness OPEN |
| T1/T2 prime-packet target | Entire MAIN fixed-basin primitive is \(\log4\) | Failed; STOP / FORK |
| Global fixed scope | MAIN/G exactly (14); D empty | Complete; higher periods unclassified |
| Full histories and phases | (9)–(19), unrestricted inverse recursion | Retained; no chosen-root thinning |
| T3 / formal Routes | No operator, trace, quantization, or formal evaluation | NOT AUDITED / UNASSIGNED; B NOT INVOKED |

Uniqueness per prime and all-prime coverage are not established. No higher
period table, scientific numerical experiment, external literature campaign,
or parameter repair is part of this result. The proper-divisor seed survives,
but neither that lineage nor a valid volume clock supplies a natural prime
ledger. The same fixed packet in G is a PROVES_TOO_MUCH warning, not proof of
global equivalence of the two owners. All negative and OPEN findings remain.

## 7. Evidence, design exposure, and assistance disclosure

The author read the complete original 99-line card, including its EOF marker,
and the local paper template. The card records pre-freeze informal fixed
equation/derivative feasibility work; the explicit probe was not a blind or
sealed prediction. This proof independently supplies the full arguments.
Current CP1, raw review, final review, sibling scientific outputs and old
proofs were not author inputs. Root manages the card and review integration.

Pre-freeze collision reads were the 341 card lines 1–65 and the 322 card
lines 1–90, both non-EOF, with the two prefix hashes in the governing card.
Heading metadata exposed appended outcome titles at 341:153 and 322:163, not
their bodies. The 322 prefix included the older 104 negative-status assertion.
No global novelty or absence-of-collision claim follows from these reads.

Same-author helper /root/arithmetic_feedback_scout/dss_g_fixed_author received
only this card's original lines 1–99 for a bounded fixed-set/full-volume and
interface check, not an independent review seat; it wrote no manuscript file.
It independently measured the exact original-prefix hash stated in §1.
The author retained responsibility for the full proof and integration.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Shared-history, same-model
execution is NOT_CALIBRATED, not cross-model or independent external validation.
ARS was used as a bounded card-first, claim/evidence and author-isolation
workflow, not as publication authorization or a mathematical certification.

The reproducibility method is exact matrix algebra, the inverse function and
change-of-variables theorems, and explicit deterministic-history identities.
Mechanical UTF-8, link, identity and hash checks verify artifacts only.
The final handoff links this [paper](paper.md), the [claim ledger](claim-ledger.md)
and [package overview](README.md); no PDF, Git operation, network request,
external upload or operator calculation was performed.
