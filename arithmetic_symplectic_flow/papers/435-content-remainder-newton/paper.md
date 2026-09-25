# Content/remainder Newton return: an owned composite two-cycle

Candidate ID: ANG-20260923-CRN01. Date: 2026-09-23.
Outcome: `OWNED NEWTON CLOCK; COMPOSITE TWO-CYCLE — STOP / FORK`

This is round 1 of the authorized 435–439 batch, not authorization for a sixth round.
The [frozen card](candidate-card.md), [claim ledger](claim-ledger.md) and [package entry](README.md) refer to the same object.
AI agents supplied design, mathematical derivation, drafting and internal workflow review. Shared-history, same-model NOT_CALIBRATED work is not blind or external peer review; no human/external verification is certified.

## 1. Full owners and executed arithmetic

Every owner uses $X=\mathbb C\simeq\mathbb R^2$, its ordinary Borel structure and area Lebesgue measure $\mu$.
At the actual current point $z=x+iy$ set
$$
a=1+\lfloor|x|\rfloor,\quad b=1+\lfloor|y|\rfloor,\quad
g=\gcd(a,b),\quad q=\lfloor a/b\rfloor,\quad r=a-bq.
$$
All readouts exist at every point, including zero and every axis. In particular $g\ge1$.
For MAIN, content-OFF C and remainder-OFF E respectively, use
$$
(G_O,R_O)=(g,r),\quad(1,r),\quad(g,0),
$$
$$
P_O(z)=z^2-R_Oz+G_O,\qquad
T_O(z)=\frac{z^2-G_O}{2z-R_O},\qquad
D_O=\{z:2z-R_O\ne0,\ P_O(z)\ne0\}.
$$
Coefficients in these expressions are re-read at each actual point. Every control has its own domain, inverse, clock and history groupoid.
All of $X\setminus D_O$ remains forward terminal, with identities and all actual incoming; there is no added loop, reset or point at infinity.
No sign, unit, floor face, critical point or nondivisible state is removed from the carrier.

For integers $n\ge2$, $2\le d<n$, the source $(n-1)+i(d-1)$ has $a=n,b=d$ and
$$
g=\gcd(n,d),\qquad r=n-d\lfloor n/d\rfloor.
$$
Thus proper divisibility is exactly the vanishing of the actual rational denominator's remainder displacement.
Nondivisors also determine an actual update or their specified terminal condition. This interface is not a selected invariant subsystem.
The lineage is divisor/prime-composite symbolic observation $\to$ current Euclidean content/remainder $\to$ quadratic Newton rational transport $\to$ geometric re-reading of arithmetic.
The readout, rational design and area measure are declared choices; strong naturalness remains OPEN, without a prime table, fitted roof or claimed Logistic/Hénon equivalence.

## 2. Complete inverse branches and pole/critical exceptions

Let $B_a=\{x:a-1\le|x|<a\}$ and $C_{ab}=B_a+iB_b$ for all $a,b\ge1$.
These cells partition all signed boundaries; $B_1=(-1,1)$.
Fix an owner and one cell's constants $G,R$. For a target $w$ the cross-multiplied inverse equation is
$$
Q(z,w)=z^2-2wz+Rw-G=0,\qquad \Delta(w)=w^2-Rw+G.
$$
Use $\operatorname{Arg}\in[0,2\pi)$ to specify the square-root notation. Both candidate inverses are
$$
\theta_{ab,\pm}(w)=w\pm\sqrt{\Delta(w)}.
$$
The exact domain of each candidate requires $\Delta(w)\ne0$, $\theta\in C_{ab}$, its own reconstructed readouts, $\theta\in D_O$, and $T_O(\theta)=w$.
The target may itself be terminal. There is no cutoff on $a,b$ or choice of one root.

To prove completeness, let $z$ be any legal source and put $w=T_Oz$, using its actual cell coefficients.
Then $Q(z,w)=0$ and
$$
z-w=\frac{P_O(z)}{2z-R},\qquad
\Delta(w)=(z-w)^2\ne0.
$$
Thus every legal predecessor is one of the two roots and none is lost by the nonzero-discriminant condition.
Conversely the complete source checks turn each retained root into an actual predecessor; the denominator exclusion is indispensable.
Indeed substituting a formal pole $z=R/2$ into $Q$ gives $R^2/4-G$.
When $R^2=4G$, cross multiplication can produce that formal pole as an extraneous root; it is excluded from this branch even if cancellation gives an extension.
The point is terminal if these are its actual cell coefficients; otherwise its own cell, not this formal branch, decides its status.
At $\Delta=0$ a formal repeated root would have $z=w$ and, if its denominator were nonzero, $P_O(z)=0$, so it could not be legal.
This handles the exceptions without silently filling poles or importing another owner's critical set.

Every legal source has one actual cell and one of the two distinct roots. On each retained inverse branch $T_O\theta(w)=w$, which makes $\theta$ injective.
Duplicate actual points or triples are identified, not counted as extra formal labels.
These are countably many Borel branches. Square-root cuts and cell faces are assigned; no usual-topology continuity across a cell boundary is claimed.

## 3. Owned all-point IMAGE and clock

Holding the actual cell's coefficients fixed, the rational germ has
$$
T'_{G,R}(z)
=\frac{2z(2z-R)-2(z^2-G)}{(2z-R)^2}
=\frac{2P_O(z)}{(2z-R)^2}.
$$
This is finite and nonzero at every prescribed legal source.
Its real-area determinant and the inverse-germ density are
$$
\rho_O(z)=\left|T'_{G,R}(z)\right|^2
=\frac{4|P_O(z)|^2}{|2z-R|^4},\qquad
J_\theta(w)=\frac{|2\theta(w)-R|^4}{4|P_O(\theta(w))|^2}.
$$
They are positive and finite at every actual source/inverse point, including assigned null boundaries.
The inverse density uses the analytic local inverse through the assigned root, not a derivative of the discontinuous global root expression across its cut.

For every Borel subset $E$ of an actual inverse domain,
$$
\mu(\theta E)=\int_E J_\theta(w)\,d\mu(w).
$$
To justify the full assertion, cover the regular source by countably many analytic inverse charts for the fixed rational germ.
Partition the actual branch into disjoint Borel pieces subordinate to those charts. Branch injectivity makes the corresponding target pieces disjoint.
Ordinary change of variables on each chart and countable additivity prove the identity, also for infinite-measure subsets.
The same argument includes assigned root rays and floor faces without deleting them. On a null set the integral cannot choose a version, but the frozen local germ fixes the displayed value there.
All these arguments apply independently with each owner's own $G,R,D_O$; no control borrows MAIN's inverse density.

The legal source clock is therefore
$$
\kappa_O(z)=-\log J_{\mathrm{actual\ inverse}}(T_Oz)
=\log\rho_O(z).
$$
Signed and zero clocks are permitted. No next-step clock is assigned to a terminal; it is NOT DEFINED, whereas the empty clock sum is zero.
Area is the full two-dimensional reference measure, not length on a selected real-axis subsystem.

## 4. Full actual groupoid, kernels and incoming

For each owner separately retain
$$
\mathcal G_O=\{(z,m-n,w):T_O^mz=T_O^nw,\ m,n\ge0\text{ legal}\},
\qquad s(z,k,w)=w,\quad r(z,k,w)=z.
$$
Equal triples are identified and integer lag remains. This is a Borel subspace of $X\times\mathbb Z\times X$; the equality sets are Borel and the inverse atlas makes both arrow fibres countable.
Composition adds lags: align the middle point at the longer of the two already legal histories. No continuation through a terminal is added.
Inversion exchanges endpoints and negates lag.
Define finite positive products and actual sums
$$
W_m(z)=\prod_{i=0}^{m-1}\rho_O(T_O^iz),\qquad
S_m(z)=\log W_m(z),\qquad W_0=1,\quad S_0=0.
$$
For two witnesses of the same triple the lengths differ by a common integer. Advancing their shared future adds the same clock to both sides, proving descent of
$$
c_O(z,m-n,w)=S_m(z)-S_n(w)=\log\frac{W_m(z)}{W_n(w)}.
$$
The same alignment proves additivity under composition. In particular $(T_Oz,-1,z)$ has clock $-\kappa_O(z)$.
An actual finite-history arrow germ has IMAGE factor $e^{-c_O}$ by the forward/inverse determinant ratio. No infinite product is used.

The entire kernels are
$$
\ker k=\{(z,0,w):T_O^mz=T_O^mw\text{ for some legal }m\ge0\},
$$
$$
\ker c_O=\{(z,m-n,w)\in\mathcal G_O:W_m(z)=W_n(w)\},
$$
$$
\ker k\cap\ker c_O
=\{(z,0,w):T_O^mz=T_O^mw,\ W_m(z)=W_m(w)\text{ for some legal }m\ge0\}.
$$
These retain nonunit and nonzero-lag arrows whenever their actual conditions hold; no equality alone creates a formal arrow.

Let $\operatorname{Pre}_O(v)$ consist of every root of §2 passing all source checks, for every cell and both signs.
Set $\operatorname{Pre}_O^0(v)=\{v\}$ and recursively apply the full predecessor operator, removing only duplicate actual points.
Induction identifies $\operatorname{Pre}_O^n(v)$ with all legal depth-$n$ predecessors.
All arrows incoming to any range $z$ are exactly
$$
\bigcup_{\substack{m,n\ge0\\T_O^mz\text{ legal}}}
\{(z,m-n,w):w\in\operatorname{Pre}_O^n(T_O^mz)\}.
$$
This includes every boundary and terminal target. At a terminal, $m$ must be zero, so incoming clocks are $-S_n(w)$; the terminal's source isotropy itself is trivial.
This is an exact unrestricted recursion, not a claim that any basin has been finitely enumerated.

## 5. General entire return groups and phases

A nonzero isotropy lag is an equality between two different forward times, hence an eventual actual cycle. Conversely an eventual cycle supplies such lags.
If its least source period is $p$, the complete source isotropy is $I_z=p\mathbb Z$; otherwise $I_z=\{0\}$.
Let $C$ be the actual clock sum once around that least cycle. Identical preperiodic portions cancel, giving
$$
c_O(z,jp,z)=jC,\qquad H_z=c_O(\mathcal G_{O,z}^z)=C\mathbb Z.
$$
For a non-eventually-periodic point, including every terminal, $H_z=\{0\}$.
These are exact conditional full-source formulas, not an enumeration of all cycles.

The full extension has objects $(z,h)\in X\times\mathbb R$ and arrows $(w,h)\mapsto(z,h+c_O)$.
Its isotropy is $I_z\cap\ker c_O$: trivial when $C\ne0$, the full $p\mathbb Z$ when $C=0$, and trivial for non-eventually-periodic points.
Unrestricted height translation on the orbit SET has stabilizer exactly $H_z$, since returning to a class over the same source requires an actual isotropy arrow with that clock.
Every phase over an anchored source orbit is retained as $\mathbb R/H_z$.
If $H_z=C\mathbb Z\ne0$, the positive primitive is $|C|$ and repetitions are $j|C|$, $j\ge1$.
Zero return clock does not erase source isotropy, and equal lengths do not merge distinct actual source orbits.
No quotient manifold, classical symplectic suspension or alternative physical roof is asserted.

## 6. Entire fixed gate and the complete unit-cell two-step gate

For any owner, a legal fixed point would satisfy
$$
z^2-G=z(2z-R),\qquad P_O(z)=z^2-Rz+G=0,
$$
contradicting its own domain. Thus every owner's actual fixed set is empty on the entire source.
Terminal identity arrows are not fixed iterations of $T_O$ and do not evade this conclusion.

On the complete cell $U=C_{11}=\{|\Re z|<1,\ |\Im z|<1\}$, every owner reads $g=1,r=0$ and has the same local expression
$$
f(z)=\frac{z^2-1}{2z}.
$$
Its legal unit-cell points are $U\setminus\{0\}$, because the additional local roots $\pm i$ of $z^2+1$ lie outside $U$.
For a two-step return staying in $U$, both steps must be legal. Hence $z\ne0$ and $f(z)\ne0$, the latter implying $z^2\ne1$.
Only under these necessary nonzero-denominator conditions may we use
$$
f^2(z)=\frac{z^4-6z^2+1}{4z(z^2-1)},\qquad
f^2(z)=z\ \Longrightarrow\ (3z^2-1)(z^2+1)=0.
$$
The four complex polynomial roots are $\pm1/\sqrt3$ and $\pm i$.
The last two fail the unit-cell requirement; no assertion about their different actual cells is imported.
The first two lie in $U$, are regular, and substitute back to
$$
z_0=1/\sqrt3,\qquad z_1=-1/\sqrt3,\qquad
T_Oz_0=z_1,\quad T_Oz_1=z_0.
$$
They are distinct, so they form exactly one least-source-period-two core in this window, not fixed-point repeats.
This proves completeness of the frozen whole-cell test for each owner separately; no other period or cell is classified.

At either core point, the full complex germ has
$$
f'(z)=\frac{z^2+1}{2z^2}=2,\qquad
\rho_O(z)=4,\qquad J_{\mathrm{actual}}(T_Oz)=1/4,\qquad
\kappa_O(z)=\ell:=\log4.
$$
These null real-axis points remain in the two-dimensional area owner. Its Jacobian is the real-area value $4$, not the one-dimensional value $2$.

## 7. The complete incoming packet, without truncating its basin

For EACH owner define the entire source orbit of this core by
$$
\mathcal B_O=\bigcup_{d\ge0}\operatorname{Pre}_O^d(\{z_0,z_1\}),
$$
using every cell, both roots and all source checks. A point in the core's groupoid orbit must eventually reach its common future, so this union is exactly that orbit.
Different owners need not have the same basin; nothing outside the tested cell is restricted to the unit formula.
For $z\in\mathcal B_O$, let $d(z)$ be its least arrival depth, $T_O^{d(z)}z=z_{\varepsilon(z)}$, with $\varepsilon(z)\in\{0,1\}$.
Put
$$
\beta(z)=S_{d(z)}(z)-d(z)\ell,\qquad \chi(z)=\varepsilon(z)-d(z).
$$
These are actual finite-history values, not chosen weights. At the two core points, $\beta=0$ and $\chi=0,1$ respectively.
For all sufficiently large $m$, $T_O^mz=z_{\chi(z)+m\pmod2}$ and $S_m(z)=m\ell+\beta(z)$.
Any witness can be advanced to this core, and conversely sufficiently large witness lengths realize every compatible lag. Therefore
$$
\mathcal G_O|_{\mathcal B_O}
=\{(z,k,w):z,w\in\mathcal B_O,\ k\equiv\chi(w)-\chi(z)\pmod2\},
$$
$$
c_O(z,k,w)=k\ell+\beta(z)-\beta(w).
$$
This describes all incoming arrows to every point of the packet, not only arrows whose endpoints are the two core points.
The lag kernel is the zero-lag pair relation with equal $\chi$ parity.
The clock kernel consists of actual compatible lags satisfying $k\ell=\beta(w)-\beta(z)$; the joint kernel further requires $k=0$, hence equal parity and equal $\beta$.

At every point of this full basin, source isotropy is $2\mathbb Z$ and
$$
H_z=2\ell\mathbb Z=(\log16)\mathbb Z.
$$
Extension isotropy is trivial. Extra incoming branches cannot shorten this ENTIRE return group.
All height phases are represented exactly by
$$
h-\beta(z)+\chi(z)\ell\pmod{2\ell\mathbb Z}.
$$
Indeed an arrow changes this expression by $(k+\chi(z)-\chi(w))\ell$, an even multiple of $\ell$; comparison with the anchor $z_0$ proves completeness.
The two core points and all their incoming tails constitute ONE packet per owner, with positive primitive $2\ell=\log16$ and repetitions $j\log16$.
Keeping both core positions and every height phase does not turn the packet into two packets or halve its primitive.

## 8. Decision, limits and provenance

MAIN has an actual positive primitive $\log16$, whose exponential is composite, not an ordinary integer prime.
Thus its prime-only necessary condition fails: STOP / FORK. This is a witnessed failure, not a vacuous nonemptiness argument or a control-only objection.
C and E separately have the same unit-core obstruction, but their actual domains and full incoming basins remain their own.
No global periodic census, finite-basin enumeration, parameter repair, half-clock, selected root or measure substitution is inferred or authorized.
The same-object ledger is intact. T0 ownership is established; arithmetic T1 is NOT PASSED, T3 NOT AUDITED, classical fields NOT APPLICABLE, formal Route UNASSIGNED and Route B NOT INVOKED.
Strong naturalness remains OPEN; the decisive stop is the owned composite primitive.

The author personally read frozen card lines 1–96 through its measured EOF, SHA256 `6f2c412141bb7bd87945ad054e9d426f5c70a96a8771bb35cf155326814da4d9`, after root's CP1 release.
No reviewer raw, scope report, peer result or other current manuscript was read. Retained ARS and paper-template instructions supplied scope and evidence discipline.
Definition preparation read 430's summary 1–110 through EOF and plan 289–321; only old card content 410:1–28 and 420:1–37 was newly read, neither to EOF.
Their prefix hashes and outcome-heading exposures 410:87/420:90 are in the frozen card; no outcome body was newly read. The author previously worked on those packages and retains shared history.
Informal private inverse/window algebra informed design before freezing; this was not blind preregistration, and no historical clock theorem was transferred.
One bounded shared-history author helper, `drd_pc_author`, read only the same 96-line card and supplied C/E inverse, IMAGE and frozen-gate derivations; the main author independently derived MAIN and checked the integrated controls.
The helper is not an independent review seat. Additional control terminal-set simplifications were not adopted or needed for this paper's exact frozen-domain proofs.
Methods are exact rational inversion, local real change of variables, legal-denominator polynomial factorization and unrestricted actual-history recursion.
No numerical orbit search, larger census, external lookup, Git/PDF/publication or operator work was used. Full self-reads, hashes, local-link and formatting checks bind artifacts, not mathematical truth.
