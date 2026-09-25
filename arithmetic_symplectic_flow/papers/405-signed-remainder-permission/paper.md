# Signed remainder permission: an owned clock with an empty positive short window

**Paper ID:** `405-signed-remainder-permission`  
**Candidate ID:** `ANG-20260923-SRP01`  
**Date:** 2026-09-23  
Outcome: `OWNED CLOCK; EMPTY POSITIVE SHORT WINDOW — BOUNDED OPEN / FORK`

## Abstract

The frozen partial map on the entire real plane reads a signed ratio digit and a dividend floor, permits their integer divisibility, and executes a normalized remainder with reciprocal feedback. All four owners admit their prescribed positive, finite, all-point inverse IMAGE density. Their actual-history groupoids and clocks are well defined, including terminals, cuts, incoming histories and ineffective isotropy. MAIN and permission-off have exactly two fixed states, both with zero clock isotropy; reciprocal-term-off has none; quotient-subtraction-off has two fixed packets of time log of the golden ratio. MAIN has no legal two-step return with either prescribed quotient word. These results leave the MAIN positive ledger outside the frozen window OPEN. They establish neither global absence nor global prime coverage, and no higher-period census is performed.

## 1. Identity, question and source lineage

The [clarified frozen card](candidate-card.md), original lines 1–101, is the sole new mathematical input. Its SHA-256 at author read was `02c8aa8e26bb30dc3ab9e85509db99062e615b578a40a2f30807aea303061b79`. Root released author mathematics after its full CP1 read. The author did not read scope, raw proof, reviewer reports or peer answers.

| Field | Same-object owner and boundary |
| --- | --- |
| Carrier and measure | Full $X=\mathbb R^2$, usual Borel structure, $\mu=\mathrm{Leb}^2$ |
| Arithmetic source | Current signed ratio floor and current second-coordinate floor |
| Actual action | MAIN partial map below, including every failed-permission terminal |
| Clock | Negative log of its own inverse IMAGE density, including null cuts |
| Arrows and packets | Actual integer-lag tail triples; full isotropy image, not selected word labels |
| Controls | D, R and Q, each with its own full source, action, measure and ledger |
| Classical/analytic fields | Classical symplectic suspension NOT APPLICABLE; no operator, trace or determinant supplied |

For integers $N\ge2,\ 1<d<N$, put $y=N+\eta,\ x=(d+\rho)y$, with $0\le\eta,\rho<1$. Then the actual readout is $n=N,q=d$; the proper-divisor test $d\mid N$ determines whether a step exists. The same digit executes the remainder, and the next geometry rereads both symbols. This realizes the prime/composite-admissibility-to-autonomous-geometric-feedback arrow, without a fixed test integer, prime table, prime-labelled component or inserted roof. Failed witnesses remain objects.

The question is whether the complete MAIN positive primitive ledger consists of ordinary-prime times $\log p$, is nonempty, has at most one actual packet per prime and ultimately covers every prime. The frozen test is all fixed states of all four owners and MAIN quotient words $(-1,-2),(-2,-1)$ only. A negative control does not condemn MAIN; an empty finite window does not settle its full ledger.

## 2. Four full sources and all inverse branches

For $y\ne0$, set $q=\lfloor x/y\rfloor,\ n=\lfloor y\rfloor$. Write $D_M=\{y\ne0,q\ne0,q\mid n\}$, where nonzero signed integers divide zero. The owners are
\[
T_M(x,y)=\left(y,{x+1\over y}-q\right),\quad
T_D(x,y)=\left(y,{x+1\over y}-q\right),\quad
T_R(x,y)=\left(y,{x\over y}-q\right),\quad
T_Q(x,y)=\left(y,{x+1\over y}\right).
\]
M, R and Q have domain $D_M$; D has domain $\{y\ne0\}$. A terminal has no forward step, not an absorbing self-loop. Every zero axis, unit, negative point, numerator-zero state and half-open cut remains. There is no replacement of $y$ by $|y|$.

For M and D the inverse on cell $(q,n)$ is
\[
\theta_{q,n}(u,v)=(u(v+q)-1,u),\qquad
u\ne0, n\le u<n+1, 0\le v-1/u<1. \tag{2.1}
\]
M further requires $q\ne0,q\mid n$; D permits every integer $q,n$. For R it is
\[
\theta^R_{q,n}(u,v)=(u(v+q),u),\qquad
u\ne0, n\le u<n+1, 0\le v<1, q\ne0, q\mid n. \tag{2.2}
\]
For Q the single actual inverse is
\[
\theta^Q(u,v)=(uv-1,u),\qquad
u\ne0, q=\lfloor v-1/u\rfloor\ne0, n=\lfloor u\rfloor, q\mid n. \tag{2.3}
\]
All domains include their stated left endpoints and exclude their right endpoints. All listed branches undergo their own reconstructed-source and forward checks; there are no truncated integer indices.

**Proposition 2.1 (complete inverse atlas).** Equations (2.1)–(2.3), with exactly these domains, enumerate every legal predecessor for their respective owner.

**Proof.** A predecessor must have second coordinate $u\ne0$. Solving its displayed second-output equation gives the listed first coordinate. For (2.1), its ratio is $v+q-1/u$, whose floor is $q$ exactly when the indicated half-open inequality holds. For (2.2), the ratio is $v+q$, with the analogous condition $0\le v<1$. Equation (2.3) has no remaining choice once $u,v$ are specified; its permission is exactly the reconstructed one. The dividend floor is $n=\lfloor u\rfloor$. Substitution gives the required output in each case. Conversely these checks make the reconstructed source legal. Each inverse branch is injective: its second coordinate recovers $u$, and the remaining affine equation has nonzero coefficient $u$. Distinct cell labels cannot duplicate a source, as its floors are unique. This also proves completeness when $n=0$ allows infinitely many divisors. □

In particular, targets with $u=0$ have no predecessors, but are not removed. A terminal target with $u\ne0$ can have legal incoming branches. All four maps and their branch domains are Borel; no global smoothness across cuts is asserted.

## 3. Every-Borel IMAGE and the fixed all-point version

**Proposition 3.1.** For each of the four owners, on every inverse branch and at every actual target,
\[
J_\theta(u,v)=|u|\in(0,\infty),\qquad
\mu(\theta E)=\int_E|u|\,d\mu\quad\hbox{for every Borel }E. \tag{3.1}
\]

**Proof.** Every inverse has form $(u(v+q)-a,u)$, or $(uv-a,u)$, with constant $a\in\{0,1\}$. Its displayed analytic derivative has determinant $-u$. To establish IMAGE without ignoring cuts, fix $u$: the $v$-section is transported by an affine bijection with length factor $|u|$. Integrating these one-dimensional identities in $u$, and swapping coordinate order, proves (3.1) by Tonelli, for arbitrary Borel sections and including infinite integrals. Restrictions to all half-open or permission subsets are already restrictions of these sections. The inverse images are Borel by the explicit inverse formulas. Thus the same formula works on boundaries and null sets, not just almost everywhere. Each branch and its inverse preserve null sets in both directions because their density is positive and finite; the full atlas is countable. □

There is no continuous determinant attached to the integer labels. They only index the actual branch bijections. On every legal source step, for all four owners,
\[
\kappa(z)=-\log|y|. \tag{3.2}
\]
This is an inverse-IMAGE clock, not an asserted physical Hamiltonian time. Zero values on $|y|=1$ are legal; no positivity roof is inserted.

## 4. Full actual groupoid, clock and kernels

Fix any one owner and use only its legal histories. For a history $z_i=T^iz=(x_i,y_i)$ of length $m$, define
\[
P_m(z)=\prod_{i=0}^{m-1}|y_i|>0,\quad P_0=1,\quad S_m=-\log P_m.
\]
Every factor exists even if the final endpoint is terminal. The groupoid is
\[
G=\{(z,m-n,w):T^mz=T^nw, m,n\ge0\},\quad
s(z,k,w)=w,\ r(z,k,w)=z,\quad
c(z,k,w)=\log{P_n(w)\over P_m(z)}. \tag{4.1}
\]
Only identical actual triples are identified. Its Borel structure is inherited from $X\times\mathbb Z\times X$: each equality condition is Borel, and the defining union is countable. Inversion sends $(z,k,w)$ to $(w,-k,z)$; multiplication adds lags at a common object.

**Proposition 4.1 (descent and ownership).** The set is a groupoid, $c$ is a well-defined additive cocycle, and its branch holonomy has all-point IMAGE density $e^{-c}$.

**Proof.** Two witnesses for the same triple have $(m',n')=(m+r,n+r)$; compare the shorter pair with the longer pair. The extra factors are the same legal common-tail factors, so the ratio in (4.1) is unchanged. For composable witnesses $T^mz=T^nw$ and $T^aw=T^bv$, if $a\ge n$ extend the first equality by $a-n$, and if $a<n$ extend the second by $n-a$. The required extensions exist on the common segment of $w$'s legal future; this proves closure without continuing through a terminal. The same cancellation proves cocycle additivity. On a piece with fixed finite branch itineraries, the local map $w\mapsto z$ first follows the forward $n$-history and then the inverse $m$-history. Iterating (3.1) gives density $P_m(z)/P_n(w)=e^{-c}$. The equality persists on all retained cuts with the prescribed versions. Countably many itinerary restrictions cover the groupoid. □

The complete lag kernel is
\[
\ker\ell=\{(z,0,w):T^mz=T^mw\text{ for some legal }m\}.
\]
The complete clock kernel consists of the actual triples in (4.1) for which $P_m(z)=P_n(w)$. Their intersection imposes both this equality and a common-depth witness. These describe actual kernels, not arbitrary word relations.

**Proposition 4.2 (all-source isotropy ledger).** If $z$ does not eventually enter an actual legal periodic cycle, then $I_z=G_z^z=\{0\}$ in lag coordinates, $H_z=\{0\}$, and extension isotropy is trivial. If it enters a cycle of least source period $p\ge1$, put
\[
A=\prod_{i=0}^{p-1}|y_i|\quad\hbox{on that cycle}.
\]
Then, in integer-lag coordinates,
\[
I_z=p\mathbb Z,\qquad c(kp)=-k\log A,\qquad H_z=(\log A)\mathbb Z. \tag{4.2}
\]
Extension isotropy is all $p\mathbb Z$ if $A=1$, and zero otherwise.

**Proof.** A nonzero equality $T^mz=T^nz$ gives a repeated state and hence an actual perpetual cycle; a terminal cannot be repeated with distinct legal times. On the eventual cycle, equality of two positions occurs exactly at multiples of its least period. This gives exactly $p\mathbb Z$, including negative lags by inversion. Common transient factors cancel in (4.1), leaving the product of complete cycles. The extension-isotropy claim is the kernel of this homomorphism. □

Retain all $X\times\mathbb R_h$ with arrows $(w,h)\to(z,h+c)$. Height translation acts on its orbit set. Over one actual source orbit this set is a height torsor $\mathbb R/H_z$: an arrow from a reference point transports every height, and two transports differ exactly by $H_z$. If $A\ne1$, the least positive time is $L=|\log A|$, with repeats $kL$; if $A=1$ there is no positive primitive although source isotropy survives. Nonperiodic and terminal classes likewise have no positive time isotropy. This classification follows from the actual source, not a global census of its cycles.

All incoming arrows to $r$ are enumerated as follows: choose every legal $m\ge0$, then every source-checked inverse word of length $n\ge0$ ending at $T^mr$, producing $w$; include $(r,m-n,w)$, removing only identical triples. The inverse arrows are all outgoing arrows. Empty words retain every object. This enumeration includes every incoming history at every terminal and periodic core; it never inserts a terminal self-step.

## 5. Complete fixed sets of all four owners

A fixed state has $(x,y)=(a,a)$ with $a\ne0$, hence $q=1$. This permission is legal for every integer $\lfloor a\rfloor$. The equations and complete solutions are

| Owner | Fixed equation | Full fixed set | Source isotropy and entire $H$ |
| --- | --- | --- | --- |
| M | $a=1/a$ | $(1,1),(-1,-1)$ | $I=\mathbb Z,\ H=0$ at both |
| D | $a=1/a$ | $(1,1),(-1,-1)$ | $I=\mathbb Z,\ H=0$ at both |
| R | $a=0$ | Empty: $a=0$ is terminal | No fixed packet |
| Q | $a^2-a-1=0$ | $(\phi,\phi),(\psi,\psi)$ | $I=\mathbb Z,\ H=(\log\phi)\mathbb Z$ at both |

Here $\phi=(1+\sqrt5)/2>1,\ \psi=(1-\sqrt5)/2=-1/\phi$. These lists are complete over the entire real plane, not selected cells. The inequalities $1<\phi<2$ show that the Q time is not log of any ordinary integer prime. This is a Q-only adverse result, not evidence against MAIN.

### 5.1 MAIN: all incoming, kernels and phases of both fixed cores

Let $e_\varepsilon=(\varepsilon,\varepsilon)$, $\varepsilon\in\{1,-1\}$. At this target (2.1) has $n=\varepsilon$, remainder zero and $q\in\{1,-1\}$, giving exactly $e_\varepsilon$ and $f_\varepsilon=(-\varepsilon,\varepsilon)$. At $f_\varepsilon$, the inverse remainder $v-1/u=2\varepsilon$ is outside $[0,1)$, so there are no predecessors. Thus the entire two source orbits are exactly
\[
\mathcal O_\varepsilon=\{e_\varepsilon,f_\varepsilon\},\qquad
f_\varepsilon\mapsto e_\varepsilon\mapsto e_\varepsilon.
\]
They are disjoint. On each, every pair of objects supports every integer lag: after both have entered the fixed core, arbitrary common future lengths realize the lag. All products $P_m=1$, so every arrow has $c=0$. The lag kernel is the zero-lag pair relation; the clock kernel is the whole restricted groupoid; their intersection is the lag kernel. Source and extension isotropy are both $\mathbb Z$ at either object. Each extension class consists of both objects at the same height; the height-translation orbit is a line with no positive period. No unit lag has been promoted to unit time.

### 5.2 D: complete backward trees, including the larger positive tree

For any target $(u,v)$, define
\[
\mathcal P_D(u,v)=
\begin{cases}
\{(u(v+q)-1,u):q\in\mathbb Z\},&u\ne0, 0\le v-1/u<1,\\
\varnothing,&\text{otherwise}.
\end{cases} \tag{5.1}
\]
This is an explicit source-checked recursion, not a finite truncation. Starting at $e_\varepsilon$, put $B_0=\{e_\varepsilon\}$, $B_{j+1}=\bigcup_{z\in B_j}\mathcal P_D(z)$. Then $\mathcal O^D_\varepsilon=\bigcup_{j\ge0}B_j$ is the full actual source orbit: the forward core is fixed, and every orbit relation to it supplies such a finite inverse word. The two trees cannot intersect, since their deterministic futures would then have two different fixed limits.

The immediate predecessors are $\{(k,\varepsilon):k\in\mathbb Z\}$. For $\varepsilon=-1$, only $k=-1$ meets the next inverse inequality, so the whole negative tree is exactly that displayed integer line. For $\varepsilon=1$, precisely the positive integers $k\ge1$ admit another level; (5.1) retains every subsequent level, with no bound or selection.

For $z\in\mathcal O^D_\varepsilon$, let $t(z)$ be its first entry into the fixed core and $b(z)=P_{t(z)}(z)$, including $b(e_\varepsilon)=1$. Every pair in the tree again supports every integer lag, and its exact clock is
\[
c(z,k,w)=\log b(w)-\log b(z). \tag{5.2}
\]
Thus $I_z=\mathbb Z,\ H_z=0$, and extension isotropy is $\mathbb Z$ throughout. Its lag kernel imposes $k=0$; its clock kernel imposes $b(z)=b(w)$; their intersection imposes both. Extension phases are exactly the real invariant $h+\log b(z)$, and have no positive time isotropy. For the negative tree $b=1$; the positive recursion need not have zero clock on arrows between different objects. Zero $H$ is not a claim that its whole clock is zero.

### 5.3 Q and R

Q has at most one predecessor anywhere, by (2.3). At either fixed point its inverse is the point itself, so its complete source orbit is a singleton. At $a=\phi,\psi$, the lag $k$ has clock $-k\log|a|$. The lag and clock kernels on this orbit are both the identity, and their intersection is the identity. Source isotropy is $\mathbb Z$, extension isotropy is zero, and the height phases form $\mathbb R/(\log\phi)\mathbb Z$. There are two distinct actual primitive packets of the same non-prime time, not one merged representative. Their repetitions are the positive integer multiples of that time. R has no fixed core; its entire remaining incoming and isotropy ledger is exactly Sections 2–4. No R higher-cycle assertion is required or made.

## 6. MAIN's complete prescribed two-word window

Write a two-step return as $(a,b)\mapsto(b,a)\mapsto(a,b)$. Both $a,b\ne0$ are necessary for its two steps. If the two actual quotient digits are $q,r$, its forward equations imply
\[
ab=a+1-qb=b+1-ra,\qquad (1+r)a=(1+q)b. \tag{6.1}
\]
For $(q,r)=(-1,-2)$, (6.1) forces $a=0$; for the cyclic rotation $(-2,-1)$, it forces $b=0$. Each contradicts legal division. Therefore there are no solutions satisfying the necessary nonzero denominators, even before the remaining floor and divisibility checks. Clearing denominators can retain illegal polynomial solutions; these are not source returns. This excludes every dividend floor, boundary and incoming/phase possibility for this prescribed window. The rotation is not an additional packet. No claim about other two-step words or higher periods follows.

## 7. Gate decision, controls and limits

| Gate or target | Established result | Boundary |
| --- | --- | --- |
| T0 ownership | All four full Borel owners, inverse atlases, groupoids and extensions are defined | No classical smooth/conservative claim |
| T1 mechanism/clock | Current divisibility controls MAIN execution; own all-point IMAGE clock proved | Strong naturalness/canonicity and arbitrary-encoding risks OPEN |
| T2 ledger | Complete general conditional ledger, all fixed cores/incoming, prescribed word exclusion | MAIN global positive ledger and prime target OPEN |
| Controls | D fixed ineffective trees; R no fixed state; Q two non-prime fixed packets | No control result transfers to MAIN |
| T3 | NOT AUDITED; no operator/trace/zeta constructed | No analytic rescue |
| Formal routes | Classical fields NOT APPLICABLE; formal Route UNASSIGNED | Route B NOT INVOKED |

The positive MAIN short window is empty: its fixed isotropy has $H=0$, and the two prescribed words yield no source cycles. Accordingly this is **BOUNDED OPEN / FORK**, not a demonstrated MAIN arithmetic failure. Nonemptiness, prime-only, uniqueness and all-prime coverage of the full MAIN ledger all remain OPEN. No implication from finite-window absence to global absence is used. The allowed short gate is complete, so this owner is not prolonged by a higher census, parameter tuning, a new density or a replacement roof.

## 8. Provenance, reproducibility and disclosure

The definition scout read current `AGENTS.md` 1–221 through EOF, `plan.md` 1–411 through EOF with the truncated display gap filled by a separate 77–180 read, and the authorized [400 batch summary](../400-nonlinear-exchange-return/batch-summary.md) 1–96 through EOF. That summary exposed 400–404 outcomes, not their linked proofs. Exact collision reading was [335's original card](../335-direct-euclidean-remainder/candidate-card.md) 1–120, not EOF; heading-only inspection exposed its appended-outcome title at160 but no outcome body. The original158 count came from that title, not a measured total. Earlier shared [320 card](../320-divisible-sum-quotient-register/candidate-card.md) 1–96 was retained, not reread for 405. The author previously supplied 335's definition. Its displayed unnormalized remainders differ from this permission and normalized reciprocal update; no nonconjugacy or global novelty is claimed.

The scout disclosed informal diagonal-unit and negative-word design expectations before freezing. This was not a blind test choice. Floors, permission direction, normalization and the additive unit are design inputs, not derived canonical principles. The lineage cell in the final clarification uses integer $N,d$ only, without narrowing the full real source.

After release the author personally read clarified card 1–101 through EOF, using `nl -ba` and a separate 85–115 tail request to fill a truncated combined display; `sha256sum` produced the input hash in Section 1. Proofs here are exact algebra, explicit inverse recursion and sectionwise Lebesgue transport. No scientific code, numerical orbit search, external literature search or higher census was used. Tool use was confined to scoped reads, Markdown edits and artifact checks. The [claim ledger](claim-ledger.md) and [README](README.md) are support surfaces, not independent evidence.

AI assistance: AI agents supplied the candidate design, mathematical derivation, drafting and internal workflow review. This author had shared historical context; internal model review is NOT_CALIBRATED, not external peer review. No human or external verification is certified. The author did not access peer mathematical files. ARS drafting guidance supported explicit claim boundaries, limitations and this disclosure, not a correctness certificate or enlarged authorization.

Data availability: the frozen card and self-contained proofs contain the complete inputs; there is no empirical dataset. Ethics: no human subjects, private data or external upload were involved. Contributions: AI-assisted conceptualization, formal analysis and writing are disclosed above; human authorship credit is not assigned by this record. Funding and conflicts: no declarations were supplied, so neither funding nor absence of conflicts is certified. No venue-specific compliance or publication readiness is asserted.
