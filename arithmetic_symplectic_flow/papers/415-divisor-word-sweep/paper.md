# Current divisor-word geometric sweeps: an owned nonprime fixed multiplier

Candidate ID: `ANG-20260923-DWS01`  
Session date: 2026-09-23. Carrier: arithmetic Borel partial-action groupoid.
Outcome: `OWNED DIVISOR-WORD CLOCK; NONINTEGER FIXED MULTIPLIER — STOP / FORK`

## Abstract

We execute the complete increasing word of proper divisors selected by a current real coordinate, then use the actual output to select a second word. The full carrier is $\mathbb R^2$, including signs, axes, integer cuts and literal intermediate poles. MAIN and its three separately owned controls are Borel partial bijections with positive finite, prescribed all-point inverse-IMAGE densities for Lebesgue measure. We give their full actual-lag groupoids and conditional orbit ledgers, without a global cycle census. In the six frozen floor rectangles, MAIN has one nonempty-word fixed source packet and two full empty-word fixed squares. The positive packet has primitive time $\log\lambda^2$, where $\lambda=(43+9\sqrt5)/38$ and $\lambda^2$ is not an integer. This is an exact counterexample to the necessary ordinary-prime-time condition. Every incoming history and every height phase is retained. The controls diagnose order, one-sweep and multiplicity effects, but do not adjudicate MAIN.

## 1. Frozen question and ownership

The [candidate card](candidate-card.md), original lines 1–90, fixes the entire object and the six-cell test. Its SHA-256 is `187e6326ebe494cc581ba1e556c81d8069d0e55d7b8022b464655260a59f7e03`. Root released the author proof after reading the complete CP1 scope review; the author did not read that review, a raw proof, or any peer manuscript.

The necessary target requires a nonempty positive primitive ledger, every positive primitive equal to $\log p$ for an ordinary integer prime, and at most one source packet per prime. All-prime coverage is an additional obligation. A genuine MAIN counterexample is sufficient to stop; a control failure alone is not.

The lineage is precise: proper-divisor admissibility $\longrightarrow$ the complete ordered divisor word $\longrightarrow$ actual geometric execution $\longrightarrow$ the output regenerating the next word. Prime/composite information is therefore used by the current update, not carried as an inert label. For integers $N\ge2$, the word is empty exactly when $N$ is prime; the retained values $N=0,1$ also have empty words and are not called primes.

The formula, increasing order, macrostep granularity and Lebesgue measure are declared design choices, not established canonical consequences of that lineage. No prime table, prescribed prime roof, zero data, factor-count time or per-prime fit is used. Strong naturalness and the broader `PROVES_TOO_MUCH` question remain OPEN.

## 2. All states, literal words and four actual owners

Each owner separately has $X=\mathbb R^2$, its usual Borel structure, and $\mu=dx\,dy$. Put
$$
N(t)=|\lfloor t\rfloor|,\qquad
\mathcal D_N=(d_1<\cdots<d_k)=\{d\in\mathbb Z:2\le d<N,\ d\mid N\},
\qquad h_d(t)=\frac{dt+d^2+1}{t-d}.
$$
The actual domain of $h_d$ is $\mathbb R\setminus\{d\}$. Set
$$
C_N=h_{d_k}\circ\cdots\circ h_{d_1},\qquad
R_N=h_{d_1}\circ\cdots\circ h_{d_k}.
$$
Thus $C_N$ executes increasing divisors and $R_N$ decreasing divisors. Empty words are the identity on all of $\mathbb R$. A word is legal only when every individual step is finite and avoids the next pole. Cancellation in a combined rational expression never repairs an omitted intermediate step.

The four forward laws and their own domains are:

| Owner | Actual forward law | Own forward domain |
|---|---|---|
| MAIN $T$ | $u=C_{N(y)}(x)$, then $T(x,y)=(u,C_{N(u)}(y))$ | Both displayed literal sweeps are legal |
| U | $U(x,y)=(C_{N(y)}(x),y)$ | This single literal sweep is legal |
| V | $V(x,y)=(x,C_{N(x)}(y))$ | This single literal sweep is legal |
| R | $a=R_{N(y)}(x)$, then $T_R(x,y)=(a,R_{N(a)}(y))$ | Both displayed reverse-order sweeps are legal |

The actual first output selects the second word in MAIN and R. All other source points remain in $X$ as forward terminals: they retain identity arrows and every actual incoming arrow, but have no reset, artificial self-loop or continuation through a pole. Empty-word identities are legal updates, not terminal repairs. No sign, axis, unit, cut or null state is removed. Each owner's full displayed execution is one macrostep; the internal factors are neither additional source coordinates nor separate time steps.

### 2.1. Exact inverses and their domains

Let $K_d=2d^2+1$. Directly,
$$
h_d(t)-d=\frac{K_d}{t-d},\qquad h_d'(t)=-\frac{K_d}{(t-d)^2},
\qquad h_d(h_d(t))=t .
$$
Consequently $h_d$ bijects its actual domain onto itself. Reversing a legal finite word reverses every legal step, so $C_N$ and $R_N$ are mutually inverse partial bijections with exactly reversed literal domains. This statement includes empty words and does not fill rationally removable holes.

For a target $w=(u,v)$, the complete inverse procedures are:

| Owner | Reconstruction of the unique possible source |
|---|---|
| MAIN | $y=R_{N(u)}(v)$, then $x=R_{N(y)}(u)$ |
| U | $(x,y)=(R_{N(v)}(u),v)$ |
| V | $(x,y)=(u,R_{N(u)}(v))$ |
| R | $y=C_{N(u)}(v)$, then $x=C_{N(y)}(u)$ |

For each row its actual inverse domain consists exactly of targets for which every indicated inverse step is legal, the reconstructed source belongs to that owner's forward domain, and its complete own forward execution returns $(u,v)$. These are source checks, not permission to borrow MAIN's domain. Targets that are themselves forward terminal may pass these inverse checks.

U is a partial bijection because the unchanged second coordinate determines the word; V is one because the unchanged first coordinate determines it. MAIN is $V\circ U$, and R is $V^{-1}\circ U^{-1}$, on their actual composition domains. In particular R is not being declared MAIN's inverse, which is $U^{-1}\circ V^{-1}$. These facts prove uniqueness and exhaustiveness of the four reconstructions.

For MAIN an explicit inverse atlas runs over every $N,M\ge0$:
$$
\theta_{NM}(u,v)=(R_N(u),R_M(v)),\qquad
N(u)=M,\quad N(R_M(v))=N,
$$
with all literal inverse and reconstructed forward checks above. For R the atlas is $(C_N(u),C_M(v))$, with $N(u)=M$ and $N(C_M(v))=N$, with its own checks. U and V use their single-index versions in the table. Indices are uniquely determined at each actual target; duplicate descriptions never create arrows. There is no index cutoff. Finite rational operations and the countable floor partition give Borel domains and maps.

## 3. Own all-point IMAGE admission

On each actual scalar domain define
$$
A_N(t)=|C_N'(t)|,\qquad B_N(t)=|R_N'(t)|.
$$
They are the products of $K_d/(t_{\rm previous}-d)^2$ along their respective literal words, and are $1$ for an empty word. Every factor is positive and finite. Reversing a legal word gives
$$
B_N(C_N(t))A_N(t)=1 .
$$
All derivatives here are the card's specified analytic germs of the displayed literal branch, including points on assigned floor cuts, not derivatives across a discontinuous label change.

The actual inverse-IMAGE versions at targets, and their values $j_F(z)=J_F(Fz)$ at legal sources, are:

| Owner | $J_F(u,v)$ on its actual inverse branch | $j_F(x,y)$ |
|---|---|---|
| MAIN | $B_N(u)B_M(v)$ | $[A_N(x)A_M(y)]^{-1}$, $N=N(y)$, $M=N(C_N(x))$ |
| U | $B_{N(v)}(u)$ | $A_{N(y)}(x)^{-1}$ |
| V | $B_{N(u)}(v)$ | $A_{N(x)}(y)^{-1}$ |
| R | $A_N(u)A_M(v)$ | $[B_N(x)B_M(y)]^{-1}$, $N=N(y)$, $M=N(R_N(x))$ |

The inverse-table indices for MAIN and R are those in Section 2.1. A literal scalar word is an analytic diffeomorphism on each component of its finite-hole domain. One-dimensional change of variables, followed by the product formula, proves the displayed density for the diagonal two-coordinate branches; the one-sweep cases have an identity coordinate. Restricting those formulas to any Borel subset of the exact branch domain preserves the identity. Summing over the countable uniquely assigned branches proves, for every actual branch and every Borel $E$ in its domain,
$$
\mu(\theta E)=\int_E J_F\,d\mu .
$$
The identity also permits infinite nonnegative integrals. Floor-boundary subsets have Lebesgue measure zero but retain the prescribed positive finite branch-germ value; actual intermediate poles have no inverse branch. Unique labels and mutually inverse words give atlas consistency without choosing a later a.e. representative.

Thus all four owners pass their IMAGE admission. Each has its own clock
$$
\kappa_F(z)=-\log j_F(z)
$$
on legal macrosteps. A missing step has undefined clock, not clock zero. This is an inverse-IMAGE arithmetic groupoid clock; it is not an asserted physical flight time, invariant Lebesgue flow or classical symplectic construction.

## 4. Full actual-lag and clock ledger

Fix any one of the four owners $F$. All statements in this section concern its full source, not just the test cells. For legal iterates let
$$
P_m(z)=\prod_{i=0}^{m-1}j_F(F^iz),\quad P_0=1,\qquad
S_m(z)=-\log P_m(z).
$$
Keep precisely the Borel groupoid
$$
G_F=\{(z,m-n,w):F^mz=F^nw,\ m,n\ge0,\ \text{all steps legal}\},
\quad s(z,k,w)=w,\quad r(z,k,w)=z .
$$
Identical triples, but not different integer lags, are identified. Multiplication adds lags and inversion negates them. Because $F$ is injective on its actual domain, common iterates cancel. Hence this definition has the following non-tautological complete membership rule:
$$
(z,k,w)\in G_F\ \Longleftrightarrow
\begin{cases}
F^kz=w\text{ legally},&k\ge0,\\
F^{-k}w=z\text{ legally},&k<0.
\end{cases}
$$
This proves closure and reduces the owner to an actual partial $\mathbb Z$-action, with no hidden branching histories.

For any presentation set
$$
c(z,m-n,w)=S_m(z)-S_n(w)=\log\frac{P_n(w)}{P_m(z)} .
$$
Extending two presentations by a common future multiplies numerator and denominator by the same factors. Equivalently canceling common iterates gives the unique actual finite path in the membership rule. The formula therefore descends and is additive under composition. For the forward arrow $(Fz,-1,z)$ it is $-\kappa_F(z)$, not $+\kappa_F(z)$.

The actual source-to-range map of that arrow has IMAGE factor $e^{-c}$: forward steps contribute $1/j_F$ and inverse steps contribute $j_F$. Iterated change of variables proves this on every Borel branch; the prescribed germs multiply at all retained points.

The complete lag kernel is the unit space, since lag zero forces $z=w$. The complete clock kernel consists of exactly the actual triples with $P_m(z)=P_n(w)$; equivalently, on the membership domains above it requires $P_k(z)=1$ for $k\ge0$ and $P_{-k}(w)=1$ for $k<0$. Its intersection with the lag kernel is the units. These assertions do not erase nonzero-lag zero-clock arrows.

All arrows incoming to a given range $z$ are exactly
$$
(z,k,F^kz)\quad(k\ge0,\ F^kz\text{ legal}),\qquad
(z,-\ell,(F^{-1})^\ell z)\quad(\ell>0,\ (F^{-1})^\ell z\text{ legal}).
$$
This includes terminals and all available backward histories without extending an undefined step. A periodic cycle cannot acquire an outside incoming tail: its predecessor is already supplied by the cycle and the inverse is unique.

For a nonperiodic point the source isotropy is trivial and $H_z=\{0\}$. On a least-period $p$ cycle the isotropy is $p\mathbb Z$: division of any positive return length by $p$ leaves a smaller return remainder, which must be zero. Writing
$$
\Lambda(z)=\prod_{i=0}^{p-1}j_F(F^iz),\qquad
c(z,kp,z)=-k\log\Lambda(z),\qquad H_z=(\log\Lambda(z))\mathbb Z ,
$$
gives the entire isotropy image, not a selected loop. This is a structural formula conditional on an actual cycle, not a classification of cycles outside the frozen window.

The extension retains every $(z,h)\in X\times\mathbb R$, with product Borel structure, and sends $(w,h)$ to $(z,h+c)$ for every actual arrow. Its isotropy at $(z,h)$ is the source isotropy intersected with the clock kernel: it is $p\mathbb Z$ when $\Lambda=1$, trivial when $\Lambda\ne1$, and trivial on a nonperiodic source orbit. Height translations commute with these arrows and descend to the extension's orbit set. The translation by $t$ fixes $[z,h]$ exactly when an actual source-isotropy arrow has clock $t$, so its full period group is $H_z$. No smooth quotient or classical suspension is inferred. A source orbit carries all height phases $\mathbb R/H_z$; when $H_z=0$ this is $\mathbb R$, not a selected phase.

Only when $H_z=L\mathbb Z$ with $L>0$ is there a primitive positive generator $L$, with repetitions $kL$ for $k\ge1$. One source packet means the actual source orbit together with this entire clock and phase data. It is not one selected extension orbit. Different source orbits remain different packets even when their times coincide; ineffective isotropy remains when $H_z=0$.

## 5. Complete fixed sets in the six full rectangles

Put $I_6=[-6,-5)$, $I_8=[-8,-7)$, $E_0=[0,1)^2$ and $E_1=[1,2)^2$. The only nonempty words required by the fixed-state equations are $\mathcal D_6=(2,3)$ and $\mathcal D_8=(2,4)$. Literal composition gives:

| Word | Combined formula | Actual domain |
|---|---|---|
| $C_6$ | $(16t-5)/(11-t)$ | $\mathbb R\setminus\{2,11\}$ |
| $R_6$ | $(11t+5)/(t+16)$ | $\mathbb R\setminus\{3,-16\}$ |
| $C_8$ | $(25t-14)/(13-2t)$ | $\mathbb R\setminus\{2,13/2\}$ |
| $R_8$ | $(13t+14)/(2t+25)$ | $\mathbb R\setminus\{4,-25/2\}$ |

For example, $C_6=h_3h_2$ excludes $2$ and also the solution $11$ of $h_2(t)=3$; $R_6=h_2h_3$ excludes $3$ and the solution $-16$ of $h_3(t)=2$. Replacing $3$ by $4$ gives the two $8$-word domains. Thus the first-step holes remain even when absent from the combined denominator.

The scalar fixed equation for $C_6$ is $t^2+5t-5=0$, with the legal roots
$$
\alpha=\frac{-5-3\sqrt5}{2},\qquad \beta=\frac{-5+3\sqrt5}{2}.
$$
Here $\alpha\in I_6$ and $\beta\in(0,1)$, using $2<\sqrt5<7/3$. The $C_8$ equation is $t^2+6t-7=0$, with legal roots $-7,1$. The value $-7$ is the excluded upper endpoint of $I_8$, not a point in that floor cell. None of these $8$-word roots lies in $I_6$. Reverse words have exactly the same fixed roots, since they are actual inverses. Empty words have every real number fixed.

At a MAIN fixed point its first output is $x$, so its two equations are $C_{N(y)}(x)=x$ and $C_{N(x)}(y)=y$. R has the corresponding two reverse-word equations; U or V has just its own equation. The scalar lists above therefore yield the complete table, with every listed point legal:

| $(\lfloor x\rfloor,\lfloor y\rfloor)$ | MAIN | U | V | R |
|---|---|---|---|---|
| $(-6,-6)$ | $\{(\alpha,\alpha)\}$ | $\{\alpha\}\times I_6$ | $I_6\times\{\alpha\}$ | $\{(\alpha,\alpha)\}$ |
| $(-6,-8)$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ |
| $(-8,-6)$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ |
| $(-8,-8)$ | $\varnothing$ | $\varnothing$ | $\varnothing$ | $\varnothing$ |
| $(0,0)$ | $E_0$ | $E_0$ | $E_0$ | $E_0$ |
| $(1,1)$ | $E_1$ | $E_1$ | $E_1$ | $E_1$ |

Indeed a $6$-word has no fixed root in $I_8$, and an $8$-word has none in either negative interval; these facts eliminate both crossed cells for each one-sweep owner as well as for MAIN/R. The positive squares use their actual empty words, not the scalar $8$-word root at $1$. Their lower boundaries are included and their upper boundaries excluded exactly as prescribed by the floor rule. There is no assertion about other cells or higher cycles.

## 6. Exact clocks, all incoming and the decisive obstruction

Define
$$
\lambda=\frac{43+9\sqrt5}{38}=\frac{9+\sqrt5}{9-\sqrt5}>1 .
$$
From the displayed word formulas,
$$
C_6'(\alpha)=\frac{171}{(11-\alpha)^2}=\lambda^{-1},
\qquad R_6'(\alpha)=\frac{171}{(\alpha+16)^2}=\lambda .
$$
Applying each owner's inverse-IMAGE formula, not borrowing the MAIN density, gives:

| Fixed core and owner | Own $j_F=J_F(Fz)$ | $\kappa_F$ | Entire $H_z$ | Positive primitive |
|---|---|---|---|---|
| MAIN at $(\alpha,\alpha)$ | $\lambda^2$ | $-2\log\lambda$ | $(2\log\lambda)\mathbb Z$ | $2\log\lambda$ |
| R at $(\alpha,\alpha)$ | $\lambda^{-2}$ | $2\log\lambda$ | $(2\log\lambda)\mathbb Z$ | $2\log\lambda$ |
| Each U or V line point | $\lambda$ | $-\log\lambda$ | $(\log\lambda)\mathbb Z$ | $\log\lambda$ |
| Every $E_0$ or $E_1$ point, each owner | $1$ | $0$ | $\{0\}$ | None |

Every fixed source has only itself as a predecessor, by the global partial-bijection proof. Inductively all its incoming histories, including those potentially outside the window, are itself. Thus its actual source orbit is a singleton and all its arrows are exactly $(z,k,z)$, $k\in\mathbb Z$. No outside tail changes the computed entire $H_z$.

At the MAIN fixed point $c(z,k,z)=-2k\log\lambda$; R has the opposite sign; each U/V line point has $c(z,k,z)=-k\log\lambda$. Their source isotropy is $\mathbb Z$, extension isotropy is trivial, and clock and lag kernels on each such core are both the units. Their phase families are respectively $\mathbb R/(2\log\lambda)\mathbb Z$ and $\mathbb R/(\log\lambda)\mathbb Z$. MAIN and R each have one positive source packet in this window, in separate owners. U and V each retain continuum many distinct same-time source packets, one for every free transverse coordinate.

At every empty-word square point the source and extension isotropy are $\mathbb Z$, the entire clock kernel is that $\mathbb Z$, and the lag kernel and joint kernel remain the units. Each retains all phases $\mathbb R$ and no positive primitive. These are defined zero-clock cores, not undefined terminal clocks, and are not deleted.

Finally,
$$
\lambda^2=\frac{1127+387\sqrt5}{722}.
$$
It is irrational: $\sqrt5$ is irrational (a reduced fraction whose square is $5$ would force both numerator and denominator divisible by $5$), and its coefficient here is nonzero. Therefore $\lambda^2>1$ is not an ordinary integer prime. MAIN's genuine positive primitive $\log\lambda^2$ is not $\log p$ for any such prime.

This proves nonemptiness and disproves the necessary EVERY-positive-prime condition for MAIN on its full source by one exact actual packet. It does not claim global uniqueness, classify all prime packets, or settle all-prime coverage outside the window. R's same positive time and U/V's continuous nonprime packets are separately owned diagnostics, not substitute evidence against MAIN. The full target already fails without a larger census or any repair of the word, measure, time version or macrostep.

## 7. Scope, evidence and integrity

T0 ownership is established for these arithmetic Borel partial-action groupoids. T1 has an explicit current-divisor mechanism and admitted own IMAGE clock, while its strong-naturalness question stays OPEN. The six-cell T2 ledger supplies the decisive target failure. T3 is NOT AUDITED; classical symplectic/suspension fields are NOT APPLICABLE, formal Route coordinates UNASSIGNED, and Route B NOT INVOKED. The portfolio decision is STOP / FORK, not advance by altering this frozen owner.

This record uses exact scalar compositions, inverse identities, change of variables and algebraic fixed equations. No scientific code, numerical search, enlarged cell window, higher-cycle census, external literature, PDF, Git operation or publication was used. The author's current scientific input was the full original card, lines 1–90 through EOF, read using `nl -ba`/`sed`; its SHA-256 was measured. Later source-file checks are mechanical text, links, line counts and hashes only.

Definition-stage collision inputs were card 327 lines 1–74 and card 344 lines 1–79, neither through EOF. Appended-outcome headings at lines 173 and 188 respectively were exposed, but not their bodies, proofs or reviews; header statements of original 171/186-line lengths were not independent total measurements. Shared previous author history is retained. The deterministic current divisor sweep differs definitionally from 327's free rational-transformation menu and 344's separate word-root/cotangent carrier. No exhaustive novelty or nonconjugacy claim is made, and no old result is imported.

Informal two-factor fixed-equation algebra and negative-cell expectations occurred during design, before freezing. Accordingly this is not a blind or sealed preregistration, and those expectations are not certified pre-freeze results. Formal proof followed root's CP1 release. One bounded AUTHOR helper, `dws_uv_author`, read only this original card's lines 1–90 and derived the U/V window and own ledger; it supplied no files, peer evidence or independent-review seat. The main author derived MAIN/R, full inverses and the general ledger and integrated the control calculation.

AI assistance is explicit: AI agents supplied candidate design, mathematical derivation, drafting and the internal workflow, including internal scope review managed by root. Shared-history, same-model assistance is `NOT_CALIBRATED` and is not external peer review; no human or external verification is certified here. No human-subject or private-data work is involved. No funding or conflict declaration was supplied. Data and methods are the displayed exact formulas and the local [card](candidate-card.md), [claim ledger](claim-ledger.md) and [package summary](README.md); no numerical dataset exists.
