# Euclidean complex feedback: full IMAGE ownership and an empty positive fixed window

**Paper ID:** 410-euclidean-complex-feedback  
**Candidate ID:** ANG-20260923-ECF01  
**Date:** 2026-09-23  
Outcome: `OWNED COMPLEX CLOCK; EMPTY POSITIVE FIXED WINDOW — BOUNDED OPEN / FORK`

## Abstract

The current integer coordinates of a full complex-plane source execute signed Euclidean division and enter a cellwise reciprocal map through its numerator, denominator and translation. We prove the prescribed all-point IMAGE identity for MAIN and its three separately owned controls, including every retained boundary, and derive their complete actual-history clock and isotropy ledgers. In the six frozen whole cells, MAIN and two controls each retain exactly one fixed state, $(1-i)/\sqrt2$, whose entire clock isotropy is zero. The remaining control has none. All algebraic roots and floor exclusions are accounted for; all incoming histories to the retained core are described by an unrestricted explicit recursion. The positive fixed window is empty, but the positive ledger beyond that window remains OPEN. No higher-period census or global prime verdict is inferred.

## 1. Frozen owner, question and lineage

The sole new mathematical input is the [candidate card](candidate-card.md), original lines 1–85, personally read through EOF after root's CP1 release. Its SHA-256 was `e735ae89cae73136b6b3b282d06f902bff13b0adf74a9202960af7133949c688`. No author-side peer, raw proof or review file was read.

| Field | Exact owner and boundary |
| --- | --- |
| Carrier and measure | Entire $X=\mathbb C=\mathbb R^2$, usual Borel structure, $\mu=dx\,dy$ |
| Arithmetic execution | Current integer-part pair, its signed Euclidean quotient and remainder |
| Actual transport | Cellwise complex reciprocal feedback, rereading the current point at every step |
| Clock | Negative log of the owner's own prescribed inverse IMAGE density |
| Arrows and packets | All actual tail triples with integer lag; entire isotropy image and actual height phases |
| Controls | Q, R and A, each with its own full action, measure and clock |
| Type/analytic owner | Borel arithmetic groupoid; classical symplectic suspension NOT APPLICABLE; no operator or trace supplied |

For $z=x+iy$, set $n=\lfloor x\rfloor,\ d=\lfloor y\rfloor$. When $d\ne0$, define
\[
q=\lfloor n/d\rfloor,\qquad r=n-qd,\qquad a=n+id.
\]
For integers $N\ge2,\ 1<D_0<N$, the full cell $z=N+\xi+i(D_0+\eta)$, $0\le\xi,\eta<1$, has $n=N,d=D_0$. Its remainder is zero exactly when $D_0\mid N$: one direction follows from $N=qD_0$; in the other, the integer ratio $N/D_0$ is its own floor. Thus proper-divisor/composite admissibility is executed as a current zero/nonzero remainder. Both outcomes remain, but affect the actual translation; the same quotient and integer part enter the denominator and numerator. This is not a prime-labelled component, fixed test integer or symbolic clock attached to another map.

The necessary MAIN target is a nonempty positive ledger with EVERY positive primitive equal to $\log p$ for an ordinary integer prime and at most one actual packet per prime. All-prime coverage is an additional ultimate target. The frozen analytical window is all fixed states in precisely six complete cells for all four owners. It does not authorize a two-step or higher-period census.

## 2. All four actions and actual inverse domains

Use the following table to define each owner's own parameters $(s,\rho,\alpha)$ from its own current cell:

| Owner | $s$ | $\rho$ | $\alpha$ | Actual map $T_O(z)$ |
| --- | --- | --- | --- | --- |
| M MAIN | $q$ | $r$ | $a$ | $ir+a/(z-q)$ |
| Q quotient-subtraction-off | $0$ | $r$ | $a$ | $ir+a/z$ |
| R remainder-translation-off | $q$ | $0$ | $a$ | $a/(z-q)$ |
| A integer-part-numerator-off | $q$ | $r$ | $1$ | $ir+1/(z-q)$ |

In unified notation,
\[
T_O(z)=i\rho+\frac{\alpha}{z-s},\qquad
D_O=\{d\ne0,\ z-s\ne0\}.
\tag{2.1}
\]
Since $d\ne0$ implies $y<0$ or $y\ge1$, and $s$ is real, the pole cannot occur on those cells. All four actual domains are therefore exactly $\{y<0\}\cup\{y\ge1\}$. The entire strip $0\le y<1$ remains as forward terminals: there is no self-step, reset or added infinity. Negative cells, $d=\pm1$, $n=0$, $q=0$, $r=0$, both axes and all half-open cuts remain. In particular $y=0$ is terminal while $y=1$ is retained.

For every $n,d\in\mathbb Z$ with $d\ne0$, compute the owner's parameters and put
\[
B_{n,d}=\{n\le\Re z<n+1,\ d\le\Im z<d+1\},\qquad
\theta^O_{n,d}(w)=s+\frac{\alpha}{w-i\rho}.
\tag{2.2}
\]
Its exact actual target domain is $w\ne i\rho$ and $\theta^O_{n,d}(w)\in B_{n,d}\cap D_O$, with the reconstructed cell/readout and forward checks. There is no truncation of integer indices.

**Proposition 2.1.** These are Borel, injective inverse branches and enumerate all actual predecessors for each owner, including incoming to terminal targets.

**Proof.** The number $\alpha$ is nonzero: for M/Q/R its imaginary part is the nonzero integer $d$, and for A it is $1$. On the punctured plane the formula (2.2) is a real-analytic bijection onto the plane punctured at $s$, with inverse (2.1). Restricting it to the displayed source cell gives exactly the stated Borel target domain. Conversely any actual predecessor lies in its unique floor cell and solving (2.1) gives (2.2). Reconstructed membership ensures the original quotient and remainder are reread, and direct substitution gives the forward identity. Different labels cannot duplicate the same predecessor, since the actual floor cell is unique. No target outside an individual branch image is deleted from $X$. □

The following real-coordinate test makes the complete incoming enumeration explicit. For $w=u+iv$, write $\alpha=A+iB$ and set
\[
D_\rho=u^2+(v-\rho)^2,\quad
X_{n,d}=s+\frac{Au+B(v-\rho)}{D_\rho},\quad
Y_{n,d}=\frac{Bu-A(v-\rho)}{D_\rho}.
\tag{2.3}
\]
For each integer pair $n,d$ with $d\ne0$, retain $(X_{n,d},Y_{n,d})$ if and only if
\[
D_\rho>0,\qquad n\le X_{n,d}<n+1,\qquad d\le Y_{n,d}<d+1.
\tag{2.4}
\]
Here $A=n,B=d$ for M/Q/R, and $A=1,B=0$ for A. These inequalities already imply the remaining legal-source checks by Proposition 2.1. They are a complete, unbounded integer-index prescription, not a selected finite list of incoming.

## 3. All-point IMAGE for each owner

**Proposition 3.1.** At every actual target of each owner's inverse branch, including null cuts, the frozen version is
\[
J^O_{n,d}(w)=\frac{|\alpha|^2}{|w-i\rho|^4}\in(0,\infty),\qquad
\mu(\theta^O_{n,d}E)=\int_E J^O_{n,d}\,d\mu
\tag{3.1}
\]
for every Borel subset $E$ of its actual domain.

**Proof.** The complex derivative is $-\alpha/(w-i\rho)^2$. Multiplication by a complex number $b$ has real matrix with determinant $|b|^2$, giving the first formula without treating integer labels as continuous coordinates. The displayed extension is a real-analytic diffeomorphism between its two punctured planes; the real change-of-variables formula applies to every Borel subset, including arbitrary restrictions to the actual domain and infinite integrals. Its absolute real derivative determinant is positive finite throughout that domain. The same analytic value is prescribed on retained cuts, not patched from an almost-everywhere density. Every branch and its inverse preserve null sets; countably many cells cover each partial owner. □

On a legal source point write
\[
j_O(z)=J^O_{n,d}(T_Oz)=\frac{|z-s|^4}{|\alpha|^2}>0,\qquad
\kappa_O(z)=-\log j_O(z).
\tag{3.2}
\]
These are the inverse-IMAGE direction. Forward branch density is $1/j_O(z)$, not $j_O(z)$. For M and R, $j=|z-q|^4/(n^2+d^2)$; for Q, $j=|z|^4/(n^2+d^2)$; for A, $j=|z-q|^4$. Every formula belongs to its own current branch. No invariant area measure, positive roof or physical Hamiltonian clock is asserted.

## 4. Full actual histories, kernels and periodic ledger

Fix one owner throughout this section. For every legal history of length $m$, put
\[
P_m(z)=\prod_{i=0}^{m-1}j(T^iz),\qquad P_0=1,\qquad S_m=-\log P_m.
\]
The final endpoint may be terminal; no factor after that endpoint is introduced. Define
\[
G=\{(z,m-n,w):T^mz=T^nw,\ m,n\ge0\text{ legal}\},\qquad
s(z,k,w)=w,\quad r(z,k,w)=z,
\]
\[
c(z,k,w)=S_m(z)-S_n(w)=\log\frac{P_n(w)}{P_m(z)}.
\tag{4.1}
\]
The Borel structure is inherited from $X\times\mathbb Z\times X$, with identical triples identified and all integer lags retained. No free word, germ quotient or ambient Möbius arrow is added. Each range fibre is countable: it is enumerated by countably many finite forward lengths and finite words in the countable inverse atlas. Inversion gives the same property for source fibres.

**Proposition 4.1.** This is a Borel groupoid; the displayed cocycle descends, is Borel and additive, and owns the all-point holonomy IMAGE density $e^{-c}$.

**Proof.** The domains of finite iterates and their equality sets are Borel; the union over $m,n$ is countable. Identities have $m=n=0$ at every object. Inversion reverses the endpoints and lag. For multiplication of witnesses $T^mz=T^nw$ and $T^aw=T^bv$, extend the first equality if $a\ge n$, or the second if $a<n$. The required segment exists in the witnessed future of $w$, so a terminal is never crossed without permission. This produces the sum of the lags. Two witnesses for an identical triple differ by a common increment of $m,n$; their additional factors are on the same legal common tail and cancel. This proves descent, and the same cancellation proves additivity. On a piece with fixed branch itineraries, the actual map $w\mapsto z$ follows the forward $n$-history and the inverse $m$-history. Repeated (3.1) gives density $P_m(z)/P_n(w)=e^{-c}$. These prescribed derivative products agree on alternative witnesses by the cancellation already proved, including null cuts. Countably many Borel itinerary pieces cover all arrows, and the formulas on each piece are Borel; thus the descended cocycle is Borel. □

The complete lag kernel is
\[
\ker\ell=\{(z,0,w):T^mz=T^mw\text{ for some legal }m\}.
\]
The complete clock kernel consists of actual triples for which $P_m(z)=P_n(w)$. Their intersection requires both a common-depth witness and that product equality. Empty histories are included, not converted to terminal self-steps.

All incoming arrows to any object $r$ are constructively enumerated by choosing each legal $m\ge0$, applying (2.3)–(2.4) recursively for every inverse word of length $n\ge0$ ending at $T^mr$, and including $(r,m-n,w)$ for each resulting source $w$. Only equal triples are deduplicated. Their inverses are all outgoing arrows. This covers arbitrary terminal incoming as well as arbitrarily deep periodic incoming.

**Proposition 4.2 (complete conditional all-source ledger).** If $z$ never enters an actual periodic cycle, then its source isotropy is trivial and its entire clock image is $H_z=\{0\}$. If it enters a least-period-$p$ cycle, set
\[
\Lambda=\prod_{i=0}^{p-1}j(z_i)>0
\]
on that cycle. Then, in integer-lag coordinates,
\[
I_z=p\mathbb Z,\qquad c(kp)=-k\log\Lambda,\qquad
H_z=(\log\Lambda)\mathbb Z.
\tag{4.2}
\]
**Proof.** Any equality of two different legal future times yields a repeated state and hence a perpetual actual cycle. Conversely a least-period-$p$ cycle gives exactly the multiples of $p$ after any transient path. Common transient products cancel, and each turn contributes its complete cycle product. A finite terminal future cannot create a nonzero time equality. This proves both alternatives without enumerating higher cycles. □

The full extension retains $X\times\mathbb R_h$ and arrows $(w,h)\to(z,h+c)$. Height translations commute with all arrows. Over each actual source orbit the orbit set is a torsor for $\mathbb R/H_z$: reference-point transport changes heights only by the full isotropy image. If $\Lambda\ne1$, the least positive primitive is $L=|\log\Lambda|$ and its repetitions are $kL$; extension isotropy is trivial. If $\Lambda=1$, source isotropy $p\mathbb Z$ survives in the extension but there is no positive primitive. Nonperiodic and terminal classes likewise have no positive time isotropy. All kernels and multiplicities remain; equal times do not merge different actual source orbits. This is a conditional classification, not a global source-cycle census.

## 5. Every algebraic root in the six whole cells

On a fixed cell, all candidate roots are exactly
\[
(z-i\rho)(z-s)=\alpha,\qquad
z_\pm=\frac{s+i\rho\ \pm\sqrt{\Delta}}2,\qquad
\Delta=(s-i\rho)^2+4\alpha.
\tag{5.1}
\]
Both square-root signs are included; either choice of the complex square root enumerates the same pair. Since $\alpha\ne0$, neither root is a cleared-denominator pole. Actual fixed membership still requires the complete original floor cell.

| Cell $(n,d)$ | $(q,r)$ | $\Delta_M$ | $\Delta_Q$ | $\Delta_R$ | $\Delta_A$ |
| --- | --- | --- | --- | --- | --- |
| $(-1,-1)$ | $(1,0)$ | $-3-4i$ | $-4-4i$ | $-3-4i$ | $5$ |
| $(0,-1)$ | $(0,0)$ | $-4i$ | $-4i$ | $-4i$ | $4$ |
| $(0,1)$ | $(0,0)$ | $4i$ | $4i$ | $4i$ | $4$ |
| $(1,1)$ | $(1,0)$ | $5+4i$ | $4+4i$ | $5+4i$ | $5$ |
| $(4,2)$ | $(2,0)$ | $20+8i$ | $16+8i$ | $20+8i$ | $8$ |
| $(5,2)$ | $(2,1)$ | $23+4i$ | $19+8i$ | $24+8i$ | $7-4i$ |

Together with the owner's $(s,\rho)$ in Section 2, this table lists all two algebraic roots in each of the 24 cell/owner cases. None is selected or discarded by a preferred sign.

### 5.1 MAIN and R: all floor checks

For MAIN, the imaginary part of (5.1) is
\[
(2x-q)y-rx=d;
\tag{5.2}
\]
for R it is $(2x-q)y=d$. They coincide on the first five cells, where $r=0$.

- On $(-1,-1)$, both $2x-1$ and $y$ are negative, so their product is positive, not $d=-1$. Equivalently the two roots are $1-i$ and $i$, neither in the cell.
- On $(0,-1)$ the two roots are $\pm\zeta$, where $\zeta=(1-i)/\sqrt2$. Exactly $\zeta$ satisfies $0\le x<1,-1\le y<0$; its negative does not.
- On $(0,1)$ the roots are $\pm(1+i)/\sqrt2$. The positive sign has $0<y<1$, not $1\le y<2$, and the negative sign has $x<0$. Neither belongs. In particular the positive root is in the retained terminal strip.
- On $(1,1)$, $(2x-1)y\ge1$, and equality to $d=1$ forces $x=y=1$. At this point the real equation $x^2-x-y^2=n$ reads $-1=1$, so it is not a fixed state.
- On $(4,2)$, $(2x-2)y\ge12>2$.
- On $(5,2)$ MAIN has $(2x-2)y-x\ge3x-4\ge11>2$, while R has $(2x-2)y\ge16>2$.

These inequalities cover the entire half-open cells, not sampled roots. Thus M and R each have exactly $\zeta$ in their frozen fixed window.

### 5.2 Q: all floor checks

Q has imaginary fixed equation $x(2y-r)=d$. On $(-1,-1)$ its left side is positive, not $-1$. On $(1,1)$ it is at least $2>1$; on $(4,2)$ at least $16>2$; and on $(5,2)$ at least $15>2$. The two remaining cells have the same equations $z^2=-i$ and $z^2=i$ and both-root checks as above. Q therefore retains exactly $\zeta$, not the positive-imaginary root in the wrong floor cell.

### 5.3 A: all floor checks

The A equation implies
\[
y\left(1+\frac1{|z-q|^2}\right)=r.
\tag{5.3}
\]
On the first five cells $r=0$, so it forces $y=0$, outside each specified cell and in the terminal strip. Their full root pairs are respectively $(1\pm\sqrt5)/2,\ \pm1,\ \pm1,\ (1\pm\sqrt5)/2,\ 1\pm\sqrt2$. On $(5,2)$, (5.3) gives $0<y<1$, not $2\le y<3$. Explicitly, write $\sqrt{7-4i}=U-iV$ with $V=\sqrt{(\sqrt{65}-7)/2}\in(0,1)$; its two roots have imaginary parts $(1-V)/2,(1+V)/2$, both in the terminal strip. Hence A has no fixed state in any of the six cells. These rejected algebraic points remain actual source objects and may retain incoming; they are not absorbing fixed points.

## 6. The retained core, all incoming, kernels and phases

For each of M, Q and R separately, the point $\zeta$ has actual readout $n=0,d=-1,q=r=0,a=-i$ and satisfies $T_O\zeta=-i/\zeta=\zeta$. It is legal, and $|\zeta|=|a|=1$ gives
\[
j_O(\zeta)=1,\qquad \kappa_O(\zeta)=0,\qquad
I_\zeta=\mathbb Z,\quad H_\zeta=\{0\}.
\tag{6.1}
\]
The entire integer isotropy persists in the extension. This is not a positive packet, and lag one has not become a unit roof.

Here is an explicit description of all its incoming, not merely its cell-local inverse. Put $t=1/\sqrt2$. At target $\zeta=t-it$, for every integer pair $n,d$ with $d\ne0$, compute the owner's $s,\rho$ and
\[
D_\rho=1+2t\rho+\rho^2,\quad
X_{n,d}=s+\frac{t(n-d)-d\rho}{D_\rho},\quad
Y_{n,d}=\frac{t(n+d)+n\rho}{D_\rho}.
\tag{6.2}
\]
Retain exactly the pairs satisfying (2.4); this is the full first incoming layer for M/Q/R. No integer pair or sign is omitted. For all later layers use (2.3)–(2.4) at each resulting target. Define $B_0^O=\{\zeta\}$ and let $B_{k+1}^O$ be the union of all such predecessors of every point in $B_k^O$. Then
\[
\mathcal O_\zeta^O=\bigcup_{k\ge0}B_k^O
=\{z:T_O^kz=\zeta\text{ for some legal }k\}.
\tag{6.3}
\]
This is the entire actual source orbit: a tail relation to the fixed core must end at that core, and every displayed finite inverse history supplies that relation. The exact inequalities and unrestricted recursion specify every level without presuming finite branching, a bound or a selected history.

For $z$ in this orbit let $\tau(z)$ be its first hitting time of $\zeta$, and $b_O(z)=P_{\tau(z)}(z)>0$, with $b_O(\zeta)=1$. The forward path is deterministic, and further fixed steps have factor one, so this definition makes no inverse-history choice. Every ordered pair of objects in this orbit supports every integer lag, by extending both histories at the fixed core. For all these arrows,
\[
c(z,k,w)=\log b_O(w)-\log b_O(z).
\tag{6.4}
\]
Consequently the lag kernel imposes $k=0$, the clock kernel imposes $b_O(z)=b_O(w)$, and their intersection imposes both. At every object the full source and extension isotropy are $\mathbb Z$, the entire $H$ is zero, and height classes are exactly the real invariant $h+\log b_O(z)$. Height translation is free on this line of phases; no arbitrarily deep incoming creates an extra positive time. The three owners are not identified merely because they share the geometric point $\zeta$. A has no fixed core in the window; its remaining histories retain the full general ledger of Section 4.

## 7. Gate decision and limits

| Gate or target | Result for this frozen owner | Limit |
| --- | --- | --- |
| T0 | Full Borel source, complete inverse atlas, actual groupoid and extension established | Not a classical smooth or conservative flow claim |
| T1 explicit mechanism/clock | Euclidean arithmetic executes the geometry; own all-point area IMAGE proved | Strong naturalness, canonicity and arbitrary-encoding risks OPEN |
| T2 | All 24 prescribed cell/owner fixed cases, full incoming and conditional all-source ledger established | MAIN positive ledger outside the window OPEN |
| Controls | Q/R same zero-clock fixed core; A empty fixed window | No conclusion borrowed into MAIN |
| T3 | NOT AUDITED; no trace/zeta/operator supplied | No analytic rescue |
| Formal routes | Classical NOT APPLICABLE; formal Route UNASSIGNED | Route B NOT INVOKED |

The MAIN positive fixed window is empty. Its admitted fixed core has zero entire clock isotropy; that is distinct from absent clock ownership. The complete MAIN nonemptiness, prime-only, unique-per-prime and all-prime-coverage questions remain OPEN. No global absence, global success or failure follows from this fixed window. The finite gate is complete and the breadth decision is BOUNDED OPEN / FORK, without a higher census, parameter adjustment, discarded boundary or replacement measure.

## 8. Provenance, reproducibility and AI disclosure

Definition-stage access was `readme.md` 1–100, not EOF, exposing its prior summary outcomes; [397's original card](../397-geometric-content-square/candidate-card.md) 1–52 and [299's original card](../299-quotient-remainder-reciprocal-flow/candidate-card.md) 1–87, neither EOF. Heading-only checks exposed their appended-outcome titles at91 and156, not bodies. 395 received filename/headings only, including its outcome title at95; no third old card body was read. Old totals/hashes were not measured. Prior299 definition/transcription participation and shared history were disclosed. The comparison is to displayed definitions, not old proofs: this is not 397's square/content map or 299's one-real-coordinate GPF subtraction, and no global novelty or nonconjugacy is claimed.

After release the author personally read the complete 410 card via `nl -ba` and measured its hash with `sha256sum`. Two bounded shared-context AUTHOR helpers, `ecf_a_control_author` and `ecf_q_control_author`, each read only the same original card 1–85 and returned exact control-root derivations. They wrote no files and were not independent review seats. The author checked their formulas against all half-open cells; a preliminary helper misclassification of the positive-imaginary root was corrected before this draft. All final fixed claims are supported by the explicit proofs above, not by helper consensus.

No scientific code, numerical roots, orbit census, external search/API, Git, PDF or auxiliary research expansion was used. The proof method is finite exact algebra, explicit Borel inverse domains, analytic change of variables and untruncated symbolic incoming recursion. Mechanical file/hash/link checks are not scientific experiments. See the [README](README.md), [claim ledger](claim-ledger.md) and frozen card; support surfaces are not independent evidence.

AI assistance: AI agents supplied candidate design, mathematical derivation, drafting and internal workflow review. Shared-history same-model assistance is NOT_CALIBRATED, not blind or external peer review. No human or external verification is certified. Quotient placement, imaginary remainder translation and integer-part numerator are disclosed design choices; no pre-freeze Jacobian or periodic result was submitted. ARS guidance supported owner/claim boundaries and explicit disclosure, not a correctness certificate or expanded authorization.

Data availability: the frozen card and complete exact derivations are the inputs and evidence; there is no empirical dataset. Ethics: no human subjects, private data or external upload were involved. Contributions are AI-assisted conceptualization, formal analysis and writing as disclosed; this record does not assign human authorship. Funding/conflicts: no declarations were supplied, so neither funding nor absence of conflicts is certified. No venue compliance or publication readiness is claimed.
