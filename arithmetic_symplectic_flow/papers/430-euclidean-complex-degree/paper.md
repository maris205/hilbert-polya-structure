# Euclidean complex feedback: a global degree obstruction

Candidate ID: ANG-20260923-ECD01. Date: 2026-09-23.
Outcome: `DEGREE-LOCKED CLOCK — GLOBAL STOP / FORK`

This is round 1 of the authorized 430–434 batch, not authorization for a sixth round.
The [frozen card](candidate-card.md), [claim ledger](claim-ledger.md) and [package entry](README.md) bind the same object and scope.
AI agents supplied design, mathematical derivation, drafting and internal workflow review. This is shared-history, same-model NOT_CALIBRATED work, not blind or external peer review; no human/external verification is certified.

## 1. Full source and executed arithmetic

The full source is $X=\mathbb C\simeq\mathbb R^2$, with its ordinary Borel structure and area Lebesgue measure $\mu$.
At $z=x+iy$ set
$$
n=\lfloor x\rfloor,\quad m=\lfloor y\rfloor,\quad d=|m|,\quad
q=\begin{cases}\lfloor n/d\rfloor,&d>0,\\0,&d=0,\end{cases}
$$
$$
r=n-dq,\qquad g=\max(1,\gcd(|n|,|m|)),\qquad A(z)=A_{nm}=g+ir,
$$
with $\gcd(0,0)=0$. In particular every coefficient is finite and nonzero because its real part is at least one.
The three independently owned maps and domains are
$$
T(z)=A(z)z^2,\quad D=\mathbb C\setminus\{0\};\qquad
T_A(z)=z^2,\quad D_A=\mathbb C\setminus\{0\};\qquad
T_L(z)=A(z)z,\quad D_L=\mathbb C.
$$
MAIN and arithmetic-OFF A retain the origin as forward terminal, not a loop. L is total, including the origin.
All signs, axes, scales, floor faces, unit readouts and nondivisible states remain. There is no independent integer label carried beside the actual geometric point.

For integers $n\ge2$ and $2\le d<n$, substitution at the actual source $n+id$ gives
$$
\frac{T(n+id)}{(n+id)^2}
=\gcd(n,d)+i\bigl(n-d\lfloor n/d\rfloor\bigr).
$$
Thus $d\mid n$ is exactly zero imaginary part of this actual transport coefficient; nondivisible remainders also act and alter the complex transport.
The interface is not an invariant-source restriction or a selected prime packet. Updated coordinates determine the next current-cell readout.
The lineage is proper-divisor/prime-composite admissibility $\to$ Euclidean content/remainder $\to$ nonlinear complex transport $\to$ geometric re-reading of arithmetic.
The coefficient combination, cell rule and degree are designs; strong naturalness remains OPEN. No prime table, fitted roof or Logistic/Hénon equivalence is claimed.

## 2. Every inverse, including assigned cuts

Let $C_{nm}=[n,n+1)+i[m,m+1)$ for all integers $n,m$.
On $\mathbb C\setminus\{0\}$ use $\operatorname{Arg}\in[0,2\pi)$ and the disjoint source sectors
$$
E_0=\{0\le\operatorname{Arg}z<\pi\},\qquad
E_1=\{\pi\le\operatorname{Arg}z<2\pi\}.
$$
The CP1 notation clarification reserves $S_a$ for clock sums, not these sectors.
For MAIN, every integer pair and $j\in\{0,1\}$ supplies
$$
\theta_{nmj}(w)=
\sqrt{|w/A_{nm}|}\exp\!\left(\frac{i(\operatorname{Arg}(w/A_{nm})+2\pi j)}2\right).
$$
Its exact target domain is
$$
\Omega_{nmj}=\{w\ne0:\theta_{nmj}(w)\in C_{nm}\cap E_j\},
$$
with the reconstructed source readout and actual forward equality. These latter checks follow from cell membership and the displayed square-root equation, and remain part of the actual-domain prescription.
Conversely any legal source has one cell and one assigned sector. Its square gives exactly the corresponding root above. This proves completeness and injectivity on each source piece.
Every actual predecessor is retained; overlapping target domains are not a permission to pick one branch. Identical actual points, not different formal presentations, are counted once.

A has just the two roots
$$
\theta^A_j(w)=\sqrt{|w|}\exp\!\left(\frac{i(\operatorname{Arg}w+2\pi j)}2\right),
\qquad w\ne0,
$$
in the same assigned sectors, without redundant integer-cell labels.
L has every branch
$$
\theta^L_{nm}(w)=w/A_{nm},\qquad
\Omega^L_{nm}=A_{nm}C_{nm}=\{w:w/A_{nm}\in C_{nm}\}.
$$
These exact domains impose all own source readouts and forward equality. They include $w=0$ when the reconstructed source belongs to its actual cell.
L imports neither the sector split nor MAIN's terminal condition.
No inverse-domain prescription asks whether the target's next step is legal.

All maps and domains are Borel. Square-root cuts and cell faces are assigned, not deleted; the global map is not asserted to be a usual-topology local homeomorphism.
The real Jacobian at such a point is the frozen analytic local inverse germ through its assigned actual root, not a derivative of the discontinuous piecewise formula across a cut.

## 3. All-point IMAGE and the clock identity

For a fixed nonzero coefficient $a$, the real determinant of the complex derivative of $f_a(z)=az^2$ is
$$
|\det_{\mathbb R}Df_a(z)|=|2az|^2=4|a|^2|z|^2.
$$
Consequently MAIN's prescribed inverse density is
$$
J_{nmj}(w)=\frac1{4|A_{nm}|^2|\theta_{nmj}(w)|^2}
=\frac1{4|A_{nm}||w|},\qquad w\in\Omega_{nmj}.
$$
It is positive and finite at every point of its actual domain. A independently has $J^A_j(w)=1/(4|w|)$.
L's full complex-linear germ instead gives
$$
J^L_{nm}(w)=|A_{nm}|^{-2}>0,\qquad w\in\Omega^L_{nm},
$$
including its origin branch.

For completeness, the displayed pointwise versions also give IMAGE on every Borel actual target subset $B$:
$$
\mu(\theta B)=\int_B J_\theta(w)\,d\mu(w).
$$
For MAIN/A, cover the nonzero source by countably many open disks on which the fixed-coefficient polynomial has a smooth inverse.
Partition each actual source piece into disjoint Borel subsets subordinate to these disks. The source-sector restriction is injective, so their images are disjoint.
Ordinary change of variables on each local chart, then countable additivity, gives the formula on arbitrary Borel $B$, including infinite-measure cases.
This argument retains source rays and floor faces; it does not require differentiability of the globally assigned root expression across its cut.
On null subsets the integral alone cannot choose a version, but the frozen local germ explicitly fixes the values above at every point.
For L, global linear change of variables restricted to $\Omega^L_{nm}$ proves the same every-Borel identity directly.

At every legal MAIN source and every legal A source, respectively,
$$
\kappa(z)=\log4+2\log|A(z)|+2\log|z|,\qquad
\kappa_A(z)=\log4+2\log|z|.
$$
Write $\ell=\log4$ and $V(z)=2\log|z|$ on $\mathbb C\setminus\{0\}$.
The actual radial equation $|Tz|=|A(z)||z|^2$ yields the all-point identity
$$
\kappa(z)=\ell+V(Tz)-V(z),\qquad
\kappa_A(z)=\ell+V(T_Az)-V(z).
$$
These are derived from the owned area IMAGE, not an inserted constant roof.
Individual clocks can have either sign or be zero. The origin has no MAIN/A next-step clock; it is NOT DEFINED, not zero.
L's separate calculation gives $\kappa_L(z)=2\log|A(z)|$ everywhere. At nonzero points its own radial equation gives
$$
\kappa_L(z)=V(T_Lz)-V(z).
$$
The origin is treated independently in §7; no formula here evaluates $\log0$.

## 4. Full actual groupoid and every incoming history

For each owner $O$ separately, retain
$$
G_O=\{(z,a-b,w):T_O^az=T_O^bw,\ a,b\ge0\text{ legal}\},
\qquad s(z,k,w)=w,\quad r(z,k,w)=z.
$$
Equal triples are identified, while the integer lag remains. The Borel structure is inherited from $X\times\mathbb Z\times X$.
Legal iterate domains and equality sets are Borel; the inverse atlas makes the source and range fibres countable.
Composition adds lags and inversion negates lag. To compose witnesses, align the middle trajectory at the longer of its already legal lengths, never extending through a terminal.

Define the finite actual sums $S_a(z)=\sum_{i=0}^{a-1}\kappa_O(T_O^iz)$ and $S_0(z)=0$.
For nonzero endpoints, telescoping the identities of §3 gives
$$
c_O(z,a-b,w)=S_a(z)-S_b(w)=
\begin{cases}
k\ell+V(w)-V(z),&O=\mathrm{MAIN},A,\\
V(w)-V(z),&O=L,
\end{cases}\qquad k=a-b.
$$
This proves independence of witnesses, additivity and sign change under inversion, directly on every actual nonzero arrow.
The actual forward arrow $(T_Oz,-1,z)$ has clock $-\kappa_O(z)$.
On any finite-history arrow germ its IMAGE density is $e^{-c_O}$: the forward-history determinant and inverse-history determinant have ratio $\exp(S_b(w)-S_a(z))$.
This is a finite-branch calculation, not an infinite product or an assumption that arbitrary label words are realizable.

Here is the complete incoming construction, not an enumerated finite basin.
Let $P_O(t)$ be all actual one-step inverse values in §2, including every integer label and both roots where appropriate.
Put $B^O_0(t)=\{t\}$ and $B^O_{b+1}(t)=\bigcup_{w\in B^O_b(t)}P_O(w)$, identifying only repeated actual points.
Induction shows that $B^O_b(t)$ is exactly the legal depth-$b$ predecessor set.
All arrows incoming to a fixed range $z$ are therefore precisely
$$
\bigcup_{\substack{a,b\ge0\\T_O^az\text{ legal}}}
\{(z,a-b,w):w\in B^O_b(T_O^az)\}.
$$
This retains every incoming depth, source label, null point and preperiodic tail.
For A one can equivalently use $T_A^az=z^{2^a}$ and all $2^b$ roots of $t$ for $B_b^A(t)$ when $t\ne0$, with no root selection.
These finite-history formulas do not classify periodic points or claim arbitrary symbolic realizability.

Since every coefficient is nonzero, no legal nonzero source of any owner maps to zero.
For MAIN/A the origin has no predecessor and no forward step; its entire groupoid component is just $(0,0,0)$.
Nonzero histories of all owners stay nonzero, so the previous formulas cover every other actual component. L's origin component is computed in §7.

## 5. Full kernels, not merely isotropy kernels

Let $k:G_O\to\mathbb Z$ be the lag. In every owner,
$$
\ker k=\{(z,0,w):T_O^az=T_O^aw\text{ for some legal }a\ge0\}.
$$
On the nonzero part, MAIN and A each have
$$
\ker c_O=\{(z,k,w)\in G_O:|z|=2^k|w|\},
$$
$$
\ker k\cap\ker c_O
=\{(z,0,w)\in G_O:|z|=|w|\}.
$$
Indeed $k\log4+2\log|w|-2\log|z|=0$ is exactly the stated radius equation.
For nonzero L,
$$
\ker c_L=\{(z,k,w)\in G_L:|z|=|w|\},\qquad
\ker k\cap\ker c_L=\{(z,0,w)\in G_L:|z|=|w|\}.
$$
All sets above are restricted to actual arrows: the radius equation alone does not create an arrow.
No lag kernel is silently replaced by units, and no nonzero-lag, zero-clock arrow is discarded.
The MAIN/A origin contributes its unit to all three kernels. L's origin contribution is separate below.

## 6. Entire return group, extension and phases

For a deterministic partial map, a nonzero isotropy lag at $z$ is a repetition $T_O^az=T_O^bz$ with $a\ne b$.
It produces an eventual legal cycle. Conversely an eventual cycle produces such witnesses.
If the eventual cycle has least source period $p\ge1$, then the full isotropy lag group is $I_z=p\mathbb Z$: every repeated-state difference is a multiple of $p$, and every multiple is realized after the tail.
If the point is not eventually periodic, $I_z=\{0\}$. This criterion distinguishes preperiodic-to-cycle points from non-eventually-periodic points without enumerating either.

On every nonzero MAIN/A component the complete clock formula, not just one presentation, gives
$$
H_z=c_O(G_z^z)=
\begin{cases}
p\ell\mathbb Z,&z\text{ eventually enters a least-}p\text{ cycle},\\
\{0\},&z\text{ is not eventually periodic}.
\end{cases}
$$
All incoming histories and different inverse presentations leave this ENTIRE group unchanged.
In particular a least-$p$ source cycle has positive primitive $p\ell$, not $\ell/p$, $\ell$ when $p>1$, or $\log2$.
The repetitions are exactly $j p\ell$, $j\ge1$. Different actual source orbits remain different packets even if their least periods coincide.
For L every nonzero isotropy arrow has equal endpoints, so $H_z=\{0\}$ regardless of its source isotropy.

The full extension retains all objects $(z,h)\in X\times\mathbb R$ and arrows
$$
(w,h)\longmapsto(z,h+c_O(z,k,w)).
$$
Its isotropy is the source isotropy restricted to zero clock. Thus every MAIN/A extension isotropy group is trivial, including the terminal origin.
L preserves its full source isotropy, whether trivial or $p\mathbb Z$.
Height translation on the extension orbit SET has stabilizer exactly $H_z$: a translation returns a class precisely when an actual source isotropy arrow realizes that clock.
Over a source orbit with an anchor $z$, all phases are $\mathbb R/H_z$, not an arbitrarily selected height or representative source point.
For MAIN/A this is $\mathbb R/(p\ell\mathbb Z)$ on an eventual-cycle packet, and $\mathbb R$ otherwise; for L it is always $\mathbb R$.

On nonzero objects the derived height coordinate $\eta=h+V(z)$ changes by $k\ell$ under MAIN/A arrows and by zero under L arrows.
This describes the owned cocycle; it does not replace it by a new roof or change the physical height translation.
For MAIN/A, actual allowed lags between a point and an anchor form a coset of $I_z$.
Consequently reducing every phase modulo $\ell$ would lose information when $p>1$; the correct modulus is the entire $p\ell\mathbb Z$.
No well-behaved measurable quotient, symplectic suspension or classical conservative flow is asserted.

## 7. L's origin and its independently owned global control result

At zero, $n=m=0$, $g=1$, $r=0$ and $A_{00}=1$.
Hence $T_L(0)=0$, the linear inverse germ has $J^L_{00}(0)=1$, and $\kappa_L(0)=0$.
Every origin predecessor must solve $A(z)z=0$, and therefore equals zero; only the actual cell $(0,0)$ retains it.
Thus every-depth incoming is the origin itself and
$$
G_L|_{\{0\}}=\{(0,k,0):k\in\mathbb Z\},\qquad c_L=0.
$$
Its source and extension isotropy are both $\mathbb Z$, its clock kernel is the whole component, and its lag and joint kernels are only the unit.
Its entire $H_0=\{0\}$ and phases are $\mathbb R$, with no positive primitive. This is not MAIN/A's terminal-origin ledger.

Together with §6, L has $H_z=\{0\}$ at EVERY source and hence an empty positive primitive ledger.
This does not say that its one-step or general-arrow clock is zero: $\kappa_L=2\log|A(z)|$, while its nonzero-arrow clock is the potential difference $V(w)-V(z)$.
If desired one may set $V(0)=0$ solely as notation after this separate calculation; no logarithm of zero or arbitrary IMAGE reassignment has been used.
The control's empty positive ledger is its own result, not a substitute for MAIN's argument.

## 8. The global degree gate

The precommitted radial-product and area-product comparison is now exact at every actual itinerary, including assigned cuts.
For a MAIN or A least-$p$ cycle, the area-clock sum telescopes to
$$
C=p\log4,\qquad \exp C=4^p.
$$
Explicitly put $R_i=|z_i|$ and $a_i=|A(z_i)|$ for MAIN, or $a_i=1$ for A, around a legal cycle with indices modulo $p$.
All $R_i>0$ and $R_{i+1}=a_iR_i^2$, so multiplication gives $\prod_{i=0}^{p-1}a_iR_i=1$.
The independently computed real-area determinants are $4a_i^2R_i^2$; their product is therefore $4^p(\prod_i a_iR_i)^2=4^p$.
For a nonzero L cycle instead $R_{i+1}=a_iR_i$ and the determinant is $a_i^2$; multiplication gives $\prod_i a_i=1$ and determinant product one. The origin is governed by §7, not this radial calculation.
The groupoid calculation in §6 proves this is the primitive multiplier: no additional inverse histories enlarge $H$ to a shorter generator.
For each integer $p\ge1$, $4^p=2^{2p}$ is composite, never an ordinary integer prime.

There are exactly two logical possibilities for MAIN's actual positive ledger.
If it is nonempty, each positive primitive it contains is $\log(4^p)$ for some least source period $p$, and prime-only fails.
If it is empty, the required nonemptiness fails.
Therefore the joint necessary target is impossible for this frozen owner, without deciding whether any nonzero cycle exists.
No ordinary-prime primitive can occur at all, so all-prime coverage is also excluded; vacuous uniqueness is not credited as arithmetic success.

This is a GLOBAL STOP / FORK, not a bounded fixed-window inference and not a classification of the periodic source.
Arithmetic-OFF A independently obeys the same degree constraint; degree-OFF L independently has zero return-clock groups.
Arithmetic coefficients can still change actual source motion, admissible histories and least periods. The result is that their contribution to the return clock cancels, not that MAIN equals or is conjugate to either control.
No parameter repair, new measure, quotient, selected representative, halved clock or additional period census is authorized.

## 9. Scope, access and integrity record

The same frozen source, measure, inverse version and history groupoid own every calculation.
T0 ownership is established; the prime-clock target is globally refuted for this owner. Arithmetic T1 is NOT PASSED; T3 is NOT AUDITED.
Strong naturalness remains OPEN. Classical symplectic/suspension fields are NOT APPLICABLE, formal Route coordinates UNASSIGNED and Route B NOT INVOKED.
MAIN's nonzero-cycle existence and detailed periodic classification remain OPEN and were unnecessary for the stop; L's origin was explicitly audited, not left open.

The author personally read the complete clarified candidate card lines 1–100 through its measured EOF, SHA256 `af74a4508865d5a947ac2527abb97681615c580e878996c37d2428ae45558b74`.
This includes original lines 1–91 and the pre-proof CP1 notation/clock-sum clarification 93–100. No raw derivation, review or other current manuscript was read.
Retained ARS and paper-template instructions supplied definition/claim/provenance discipline, not an external mathematical verification.
Definition preparation read plan lines 1–178 and 289–321, prior-work guide 44–71, and the previous 425 batch summary 1–111 through EOF.
The only collision-card content reads were 307 lines 1–63 and 398 lines 1–46, neither to EOF; their prefix hashes and outcome-heading-only exposures are preserved in the frozen card.
No outcome body or historical proof was imported. The distinction from linear cell/content and projective owners is definitional, not a global novelty or nonconjugacy claim.
Informal anticipation of radial/Jacobian cancellation motivated the design before freezing, so this was not blind or sealed preregistration.

One bounded shared-history author helper, `drd_pc_author`, read only the same 100-line card and supplied L's inverse, IMAGE, origin and full-history derivation.
It was author assistance, not an additional independent review seat. The main author derived the degree gate and checked the integrated control proof.
Methods were exact inverse algebra, local real change of variables, finite clock telescoping and actual-history arguments.
No scientific numerics, fixed-point window, cycle enumeration, external literature, prime tables, fitted roofs, Git/PDF/publication or operator work was used.
Artifact checks comprise complete self-reads, prefix/full SHA256 receipts, identity/status consistency, local links and Markdown/control-character checks; they certify artifact binding, not mathematical truth.
The portfolio decision is to stop this frozen prime-clock owner and fork only under a separately authorized and frozen genuinely different definition.
