# Divisor-controlled spherical degree: owned clock and complete fixed-point gate

Candidate ID: `ANG-20260924-DSD01`.
Outcome: `OWNED SPHERICAL CLOCK; EMPTY GLOBAL FIXED WINDOW — BOUNDED OPEN / FORK`.
Paper: `461-divisor-spherical-degree`; date: 2026-09-24.
Batch: `RECURRENCE-ADMISSION-20260924-W`, round 2/5.
Status: exact owner and global fixed-set results; higher-period target OPEN.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
AI-assisted, shared-history, same-model work is `NOT_CALIBRATED`.

## Abstract

The frozen partial maps act on the entire Riemann sphere with its original
spherical area. Current integer coordinate readouts determine divisibility
permission and the actual rational degree. Every legal inverse branch has
an everywhere-defined spherical-area IMAGE modulus, including assigned cuts
and reciprocal-chart targets. The MAIN and degree-feedback-OFF owners have
no fixed point anywhere. The permission-OFF owner has exactly the two fixed
points \(i,-i\), each with singleton full incoming class and zero clock.
An exhaustive radius bound, not a finite degree search, proves completeness.
The full actual-history groupoid, kernels, isotropy image and height phases
are retained. An empty global fixed set does not decide the MAIN's
higher-period ledger; the frozen short gate therefore ends BOUNDED OPEN / FORK.

## 1. One object, question and lineage

Write \(X=\widehat{\mathbb C}\), with its usual Borel structure, and
\[
 d\mu(z)=\frac{dx\,dy}{\pi(1+|z|^2)^2},\qquad \mu\{\infty\}=0.
 \tag{1}
\]
In the reciprocal coordinate \(\zeta=1/z\) the density has the same formula:
the factor \(|\zeta|^{-4}\) cancels the transformed denominator.
Polar integration gives \(\mu(X)=2\int_0^\infty r(1+r^2)^{-2}dr=1\).
Both \(0\) and \(\infty\), and every other null or boundary state, remain objects.
For finite \(z=x+iy\), put \(N=1+\lfloor|x|\rfloor\), \(D=1+\lfloor|y|\rfloor\).
The following are three separate partial owners, each with (1):

| Owner | Legal source | Actual degree |
| --- | --- | --- |
| M (MAIN) | \(z\in\mathbb C\setminus\{0\},\ D\mid N\) | \(q=N/D\) |
| O (permission OFF) | \(z\in\mathbb C\setminus\{0\}\) | \(q=\max(1,\lfloor N/D\rfloor)\) |
| F (degree feedback OFF) | \(z\in\mathbb C\setminus\{0\},\ D\mid N\) | \(q=1\) |

Every legal step is
\[
 T(z)=R_q(z)=\frac{z^q-1}{z^q+1},
 \tag{2}
\]
interpreted as sphere-valued, including a pole's target \(\infty\).
An illegal object has its identity arrow and incoming histories, not a loop
or reset. In particular even the degree-one owners exclude \(0,\infty\)
as sources. No target-next-step permission is added to an inverse.

The exact symbolic interface is the whole collection of sign copies
\(|x|\in[N-1,N)\), \(|y|\in[D-1,D)\), with integers \(1<D<N\).
MAIN admits exactly the proper-divisor alternatives \(D\mid N\), and their
quotient changes the rational degree in (2). The new coordinates are read
again at the next step. Thus divisor/composite admissibility changes both
execution and geometry; this is not a passive arithmetic label.
Naturalness of this deformation and of the formula/measure is OPEN.
No prime table, prime selector, prescribed \(\log p\), or fitted roof is used.

| Same-object field | Owner and limit |
| --- | --- |
| Carrier and reference measure | Full sphere and (1), not an invariant-measure assertion |
| Evolution | Actual partial Borel map (2), with its own degree rule |
| Clock and packets | Inverse-germ area IMAGE; full retained-lag groupoid below |
| Physical extension | \(X\times\mathbb R\) and height translation on its orbit set |
| Classical symplectic suspension | NOT APPLICABLE; no positive roof supplied |
| Trace, determinant, zeta, operator | Not constructed; T3 NOT AUDITED |

The sole return gate is the complete global fixed set of each owner.
All other histories must retain their exact ledger, but no higher-period
existence/classification test is performed.

## 2. Complete inverse atlas and every-point IMAGE

Let \(W=X\setminus\{-1,1\}\), \(t(w)=(1+w)/(1-w)\) for finite \(w\),
and \(t(\infty)=-1\). For every integer \(q\geq1\) and \(0\leq j<q\), define
\[
 \theta_{qj}(w)=|t(w)|^{1/q}
 \exp\!\left(\frac{i(\operatorname{Arg}t(w)+2\pi j)}q\right),
 \quad \operatorname{Arg}\in[0,2\pi).
 \tag{3}
\]
For an owner A, retain precisely \(E^A_{qj}\subset W\) where this root is
a legal A-source of actual degree \(q\). F uses only \(q=1\).
Reconstructed readouts and (2) are checked; equation (3) then gives
\(T\theta_{qj}(w)=w\). There are no sources over \(1\): finite \(z^q\)
cannot solve (2) with that value. A source over \(-1\) would be \(z=0\),
which is excluded for all three owners. No formal source at infinity is added.

Completeness follows by solving \(z^q=t(w)\). A nonzero finite legal \(z\)
has exactly one actual degree and one half-open sector
\(2\pi j/q\leq\operatorname{Arg}z<2\pi(j+1)/q\).
These sets form a countable disjoint partition of the legal source.
Their inverse graphs, not necessarily their target images, are disjoint.
The argument and all arithmetic guards are Borel, so \(E^A_{qj}\) is Borel.
For Borel \(E\subset E^A_{qj}\), its root image equals the sector/source
piece intersected with \(R_q^{-1}(E)\), and is therefore Borel.
No multiplicity is attached to extra descriptions of an identical source.

At every legal root \(z\), \(R_q\) has a nonzero holomorphic derivative
in the appropriate sphere charts: \(z\neq0,\infty\). Its inverse germ
defines the frozen pointwise version at floor boundaries and Arg seams,
even where the assigned piecewise map has no global derivative.
Set \(r=|z|>0\) and
\[
 \lambda_q(r)=\frac{q r^{q-1}(1+r^2)}{1+r^{2q}},\qquad
 J_{qj}(w)=\lambda_q(|\theta_{qj}(w)|)^{-2},\qquad
 \kappa(z)=2\log\lambda_q(|z|).
 \tag{4}
\]
These are positive finite moduli and a finite real clock at EVERY actual
point, not merely almost everywhere.

For a finite nonpole target, \(R'_q(z)=2qz^{q-1}/(z^q+1)^2\) and
\(1+|R_q(z)|^2=2(1+r^{2q})/|z^q+1|^2\).
Multiplying the real determinant \(|R'_q|^2\) by the target/source density
ratio in (1) gives exactly \(\lambda_q(r)^2\), proving (4).
At a pole \(z^q=-1\), use the target coordinate
\(\eta=1/R_q=(z^q+1)/(z^q-1)\).
Here \(r=1\), \(|d\eta/dz|=q/2\), and the density ratio is \(4\);
the forward area modulus is \(q^2\), again (4).
Chart changes cancel between the density ratio and determinant by the
chain rule, so the inverse-germ prescription is chart independent.

Every germ is a smooth local diffeomorphism. Cover each assigned source
piece by countably many such coordinate neighborhoods and disjointize this
cover measurably. Ordinary two-dimensional substitution on each piece,
then countable additivity, proves for EVERY Borel \(E\subset E^A_{qj}\)
\[
 \mu(\theta_{qj}(E))=\int_E J_{qj}(w)\,d\mu(w).
 \tag{5}
\]
Singleton poles and all null cuts are kept in this argument; their assigned
values in (4) are fixed by germs, not determined by an a.e. RN class alone.
Thus (5) is an IMAGE formula for each actual inverse, not a stationarity or
global measure-preservation assertion for a many-to-one partial map.

The zero-clock criterion is the exact equality
\(q r^{q-1}(1+r^2)=1+r^{2q}\); either sign otherwise is retained.
In particular \(q=1\) gives \(J=1,\kappa=0\) for all legal points.
F therefore owns the identically zero clock on its entire legal source.
For \(q>1,r=1\), \(\kappa=2\log q\), but an individual step is not a closed
primitive. Replacing (4) by a degree-only roof would change the owner.

## 3. All incoming histories, kernels and physical phases

The following construction is applied separately to M, O and F.
Let \(D^{(m)}\) be the points with \(m\) legal successive steps, \(D^{(0)}=X\).
For \(z\in D^{(m)}\), write \(z_a=T^az\) and define
\[
 P_m(z)=\prod_{a=0}^{m-1}\lambda_{q(z_a)}(|z_a|),\quad
 S_m(z)=2\log P_m(z),\quad P_0=1,\ S_0=0.
 \tag{6}
\]
Only legal sources occur in the product, never a terminal's nonexistent clock.
The FULL actual groupoid and cocycle are
\[
 G=\{(z,m-n,w):T^mz=T^nw,\ z\in D^{(m)},w\in D^{(n)}\},\quad
 c(z,m-n,w)=S_m(z)-S_n(w).
 \tag{7}
\]
Source is \(w\), range is \(z\); equal actual triples are identified.
Two witnesses of the same triple differ by the same number of steps on
both sides. The added common tail has the same clock sum, proving descent.
To compose two witnesses, advance their occurrences of the intermediate
object to the larger of the two legal times. This is allowed along its
existing forward history and proves closure, lag addition and cocycle
addition. Inversion reverses lag and clock; all units are retained.
The forward-history arrow \((z,1,Tz)\) has clock \(+\kappa(z)\).
The maps, legal-history domains and sums are Borel. Meeting loci are Borel
in \(X\times X\); countably many witnesses give a Borel \(G\).
Taking the first witness in any enumeration and using descent makes \(c\)
a Borel function on this same \(G\).

For every \(y\in X\), define
\(I(y)=\{\theta_{qj}(y):y\in E^A_{qj}\}\), with \(I(\pm1)=\varnothing\).
Recursively
\(I^0(B)=B,\ I^{a+1}(B)=\bigcup_{y\in I^a(B)}I(y)\).
This unrestricted recursion is an exact all-depth incoming description:
induction on depth follows from the complete inverse atlas.
The whole source orbit of \(y\) is
\(\bigcup_{b:T^by\ {\rm exists}}\bigcup_{a\geq0}I^a(\{T^by\})\).
It includes merging, transient, terminal and all preperiodic histories;
identical points/triples are deduplicated, not counted as separate paths.

For any witness in (7), the complete three kernels are
\[
 \ker c=\{P_m(z)=P_n(w)\},\quad
 \ker\ell=\{m=n\},\quad
 \ker c\cap\ker\ell=\{m=n,\ P_m(z)=P_m(w)\}.
 \tag{8}
\]
These are conditions on actual arrows, not independent formal words.
Equal lag witnesses do not introduce extra arrows.
For F, \(P_m=1\), so \(\ker c=G_F\). Its partial Möbius map is injective;
therefore equal-time meeting implies equal sources, and both its lag
kernel and joint kernel consist only of units.

If a forward orbit never becomes periodic (including every terminating
orbit), its isotropy is trivial: any nonzero self lag would give two equal
iterates and hence a genuine legal cycle.
Otherwise let \(p\) be the least period of its eventual actual cycle \(C\)
and let \(K=\sum_{u\in C}\kappa(u)\), each cycle point taken once.
Two equal sufficiently late iterates differ exactly by a multiple of \(p\);
earlier equality also forces that divisibility. All such multiples occur.
Consequently at EVERY point in its whole incoming class
\[
 G_z^z=p\mathbb Z,\qquad c(z,kp,z)=kK,\qquad H_z=K\mathbb Z.
 \tag{9}
\]
This proves the ENTIRE image, not a subgroup found from one witness.
When \(K\neq0\), the positive primitive is \(|K|\) and all repeats are
integer multiples; when \(K=0\), the source isotropy remains \(p\mathbb Z\)
but there is no positive primitive. F has \(H_z=\{0\}\) everywhere,
without needing any higher-period census.

The full extension has arrows \((w,h)\longmapsto(z,h+c(z,\ell,w))\).
Thus a forward step identifies \((z,h)\) with \((Tz,h-\kappa(z))\).
Extension isotropy is \(\ker(c|_{G_z^z})\): trivial for nonzero \(K\),
all \(p\mathbb Z\) for zero \(K\), and trivial for nonperiodic classes.
Fix one base object \(o\) in a source orbit and choose an actual arrow
from \(o\) to each \(z\), with clock \(b_z\).
Different choices change \(b_z\) by an element of \(H_o\).
The exact extension-orbit phase is
\[
 h-b_z\pmod{H_o}\quad\hbox{in }\mathbb R/H_o.
 \tag{10}
\]
Indeed clocks of arrows from \(w\) to \(z\) form exactly
\(b_z-b_w+H_o\), by composing with all base isotropy.
Hence (10) is necessary and sufficient, retaining every real height.
Height translation acts by addition on each such phase space. No regular
measurable quotient, chosen section, or identification of different
source packets with equal clock is assumed.

For explicit boundary checks, the only actual degrees on \(|z|=1\) are:
M/O have \(q=2\) at \(\pm1\), degree one at other nonaxis points;
M rejects \(\pm i\), while O admits them with degree one.
F admits the same circle sources as M but always with degree one.
It follows directly from \(z^q=1\) or \(-1\) that
\[
 I_M(0)=I_O(0)=\{-1,1\},\quad I_M(\infty)=I_O(\infty)=\varnothing,
 \qquad I_F(0)=\{1\},\quad I_F(\infty)=\{-1\}.
 \tag{11}
\]
Together with \(I(\pm1)=\varnothing\), these give the complete corresponding
terminal classes. M/O have class \(\{0,-1,1\}\) and isolated \(\infty\);
F has classes \(\{0,1\}\) and \(\{\infty,-1\}\).
All have trivial isotropy and \(H=0\). In the M/O class based at \(0\),
\(b_{\pm1}=\log4,\ b_0=0\); in these F classes every \(b=0\).
Thus the nonzero incoming step \(\log4\) is NOT a positive closed primitive.
Other terminal classes are covered without truncation by the recursion.

## 4. Complete global fixed sets

**Theorem.** \(\operatorname{Fix}(M)=\operatorname{Fix}(F)=\varnothing\),
and \(\operatorname{Fix}(O)=\{i,-i\}\).

Neither \(0\) nor \(\infty\) can be fixed because neither is a legal source.
A finite pole maps to infinity and is not fixed. Values \(\pm1\) have no
incoming at all. Every remaining fixed point satisfies
\[
 z^q=\frac{1+z}{1-z}.
 \tag{12}
\]
If \(q\geq2\) and \(r=|z|\geq2\), the triangle inequalities give
\[
 r^q=\left|\frac{1+z}{1-z}\right|
 \leq\frac{r+1}{r-1}\leq3,\qquad r^q\geq4,
 \tag{13}
\]
a contradiction. This is an exhaustive bound for ALL degrees.
Thus \(r<2\), hence \(N\leq2\). For either M or O, an actual \(q\geq2\)
then forces \(N=2,D=1,q=2\), including all half-open boundaries.
Equation (12) becomes \(P(z)=z^3-z^2+z+1=0\).
On the real line \(P'(x)=3(x-1/3)^2+2/3>0\), and
\(P(-1)=-2,\ P(0)=1\); its unique real root \(a\) lies in \((-1,0)\).
The other two roots are nonreal conjugates, each with real part
\((1-a)/2\in(1/2,1)\), because their sum is \(1-a\).
Every root consequently has \(|\operatorname{Re}z|<1\), contradicting
the actual \(N=2\) requirement. No radical approximation or scan was used.

For \(q=1\), equation (12) is \(z^2=-1\). At each of \(\pm i\) the
exact boundary readout is \(N=1,D=2\). M and F fail divisibility;
O assigns \(\max(1,\lfloor1/2\rfloor)=1\) and admits both.
This exhausts every degree, sign, axis, floor cut and terminal, proving
the theorem for each independent owner.

For O, any predecessor of \(i\) or \(-i\) satisfies
\(z^q=t(\pm i)=\pm i\), so \(|z|=1\).
On that circle only \(\pm1\) have actual O degree two and both map to \(0\).
Every other possible predecessor has degree one, whose unique inverse
of either core is that same core. Therefore \(I_O(i)=\{i\}\) and
\(I_O(-i)=\{-i\}\); induction proves each whole incoming class is a singleton.
At each core \(q=1\), so the full restricted groupoid is \(\mathbb Z\),
its clock vanishes, \(\ker c=\mathbb Z\), and lag/joint kernels are \(\{0\}\).
Source and extension isotropy are \(\mathbb Z\); ENTIRE \(H=\{0\}\);
there is one extension orbit for each \(h\in\mathbb R\) over EACH core.
The two source packets are distinct and neither supplies a positive time.
M and F have no fixed-core class to select or retain artificially.

## 5. Gate, limits and decision

T0 ownership and the measured part of T1 are established for all three
owners. The divisor-feedback rule is explicit, but arithmetic naturalness
and the target are not established. The global fixed gate is fully solved;
its MAIN result is empty, not adverse. The O zero-clock packets neither
repair MAIN nor condemn its untested higher periods.
The necessary target remains nonempty positive ledger, every positive
primitive equal to \(\log p\) for an ordinary integer prime, and at most
one full packet per prime; all-prime coverage is a separate obligation.
No part is inferred from an empty fixed set. T2 is bounded to this fixed
gate and the conditional all-history identities (7)–(10), not a global
periodic census. Formula naturalness and PROVES_TOO_MUCH stay OPEN.
Disposition: BOUNDED OPEN / FORK at the frozen gate, with no further local
return search, parameter change, new window or candidate authorized here.

## 6. Inputs, method and disclosure

The scientific input is the complete 100-line [frozen card](candidate-card.md),
SHA256 `5a0ddcaa691d2c9691ba2487fdcbe13ee247d8fc0a8ccd0c52b347e21fe870c2`,
plus the repository paper template and applicable governance/ARS writing
instructions. Proofs use exact inverse solving, two-dimensional substitution,
finite polynomial algebra, inequalities and actual-history arguments.
There are no numerical experiments, scientific scripts, cutoffs, external
sources, PDFs or operator claims.

Design exposure, not scientific dependence: 430 card lines 1–80/117,
prefix SHA256 `4a25e9fc9c656a8d79cc7d1fc44cbe916d51ff3f25cfe8aaaaac79c8054275dc`;
410 card lines 1–68/100, prefix SHA256
`73aeb18e13e071ff5f277b80c2256843e2e4c446f3c007e8a22004f411059dbb`.
Neither was read to its outcome body. Registry lines 1–230/2552 exposed
batch summaries 400–459, more than needed; root readme lines 1–27 and
prior-work guide lines 1–180/441 were also read during design.
Shared previous authorship and informal inverse/low-degree feasibility
expectations are disclosed, not blind discovery or external novelty evidence.
430's fixed quadratic coefficient law and 410's degree-one reciprocal law
are definition comparisons; no old proof, current peer proof, CP1 scope,
raw review or final review was read for this author draft.

AI assistance: AI agents supplied mathematical derivation, drafting and
internal checking; no human or external verification is certified.
Author helper `direct_controls` first supplied filename metadata only,
then after release read the frozen 461 card and derived O/F controls as a
disjoint same-author task. The author checked and integrated those arguments;
the helper is NOT an independent reviewer. Same-model/shared-history review
is `NOT_CALIBRATED`. ARS guided evidence boundaries, concise proof writing
and disclosure, not mathematical validation or venue certification.
No venue criteria binding was supplied; `criteria_binding_unavailable`.
Data availability: all definitions and proofs are in this Markdown package.
Ethics: no human participants or personal data. Funding and conflicts:
no funding or conflict information was supplied; no external declarations
are inferred. Contributions: author AI conceptualization, formal analysis
and writing; named helper control derivation; root integration separately.

Evidence navigation: [claim ledger](claim-ledger.md), [README](README.md).
Root-owned review receipts are separate from this author proof and must not
be inferred from the completion of these author surfaces.

EOF — DSD01 author proof; no higher-period census.
