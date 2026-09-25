# Actual parameter-cycle clock rigidity, with admission boundaries

Candidate ID: `ANG-AUDIT-20260923-PCR01`.
Outcome: `ACTUAL PARAMETER-CYCLE RIGIDITY ESTABLISHED; SINGLE-OWNER NONCLAIMS RETAINED`.
Paper443; batch `ADMISSION-CLOCK-20260923-S`, round4/5.
Frozen session: 2026-09-23; author record: 2026-09-24.
Status: exact conditional theorem and complete external controls; author-stage record.
Classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

A continuous, actually admitted least-period branch has a continuous signed cycle clock obtained from its own inverse IMAGE derivatives.
If every separate parameter owner has a prime-only positive primitive ledger, that signed clock is constant, including the possible constant zero case.
A joint-open legal itinerary and a nondegenerate return equation give local actual continuation; joint C2, not merely C1, supplies the stated total sensitivity formula.
Three complete real-line controls distinguish varying cycle multipliers, nonlinear deformation with constant cycle multiplier, and loss of actual admission at a moving threshold.
This is a conditional robustness filter, not a requirement imposed on every single candidate or a construction of an endogenous prime source.

## 1. Candidate identity and same-object ledger

| Item | Frozen owner and scope |
| --- | --- |
| Carrier | For each separate parameter \(\lambda\in I\), the full open \(X\subset\mathbb R^d\) with its own Lebesgue measure |
| Actual evolution | Joint-C1 germs \(f_i\) restricted to the disjoint Borel legal pieces \(E_i(\lambda)\); all other states are terminals |
| Clock | Every-point spatial inverse derivative \(J_\theta=\|\det D_x\theta\|\), \(\kappa_\lambda=-\log J_\theta(T_\lambda x)\) |
| Arrows / physical heights | Full legal lag groupoid and its clock extension on \(X\times\mathbb R\); no parameter coordinate is added |
| Arithmetic / lineage | Conditional filter of prime-symbolic admissibility → parameterized geometric deformation → actual period clock; no arithmetic grammar supplied |
| Primitive convention | Least positive generator of the entire isotropy-clock subgroup; positive integer repetitions; packet multiplicity retained |
| Classical / operator fields | Symplectic base, positive suspension roof, Hamiltonian lift, operator, trace and zeta are not constructed |
| Controls | Separately full A, B and C on \(\mathbb R\), \(I=(-1/2,1/2)\), each with its own \(dx\) and actual legal domains |

Parameters label separate owners: neither nonautonomous dynamics nor an automatic identification of packets between parameters is defined.
Signed step clocks are not asserted to be a positive roof.

## 2. Question and claim boundary

The strongest claim is conditional constancy of a specified continuous actual cycle branch under prime purity of every parameter owner's entire positive ledger.
The hypotheses do not include uniqueness of prime packets, a nonempty ledger, all-prime coverage, or persistence of any other packet.
Local return persistence is a separate theorem: it establishes admission only inside its joint-open legal neighborhood.
There is no single-owner impossibility claim, no claim that all deformations are conjugacies, and no transfer of a clock, measure, determinant or Route credit between owners.

## 3. Frozen inputs and notation

Use the [frozen card](candidate-card.md), scientific prefix lines1–99, SHA256
`f9d2dac20d66d35e7a36ef63c53ca350827bd28a69dd98f36df5547df2ac9f2d`.
The countably many disjoint Borel \(E_i\subset I\times X\) lie in joint-open \(U_i\), where \(f_i:U_i\to X\) is jointly C1 and \(\det D_xf_i\ne0\).
Write \(D_\lambda=\bigcup_iE_i(\lambda)\), and define \(T_\lambda\) only on \(D_\lambda\).
The notation \(T^n x\) always requires all \(n\) actual steps; \(T^0x=x\) exists even at a terminal.
Fixing \(\lambda\), suppress its subscript and set \(S_n(x)=\sum_{j=0}^{n-1}\kappa(T^jx)\), \(S_0=0\).
No exceptional parameter or null cycle is removed, and no prime or target period is used to choose a parameter.

## 4. Full inverse IMAGE, groupoid, isotropy and phases

For each \(i,\lambda\), the spatial inverse-function theorem gives an injective neighborhood at every point of \(E_i(\lambda)\).
The fixed enumeration of rational balls supplies a countable cover by balls contained in \(U_i(\lambda)\) on which \(f_i(\lambda,\cdot)\) is injective.
Restrict each ball to the actual piece and remove all earlier eligible balls; this gives disjoint Borel source pieces \(A_{i,r}\) covering \(E_i(\lambda)\).
On each image \(f_i(A_{i,r})\), retain the restriction of the ambient inverse \(\theta_{i,r}\); these are Borel since the ambient map is a homeomorphism.
Distinct roots are all retained. The source's unique \(E_i\) fixes its derivative germ even on piece boundaries; the ball choice does not change that germ.
Every Borel \(B\subset f_i(A_{i,r})\) satisfies
\[
 \mu(\theta_{i,r}B)=\int_B J_{\theta_{i,r}}(y)\,dy,\qquad
 J_{\theta_{i,r}}(y)=\frac1{|\det D_xf_i(\lambda,\theta_{i,r}y)|}>0.
\]
This is ordinary change of variables on the ambient ball, then restriction; the displayed version is fixed at every actual point, not just almost everywhere.
Consequently \(\kappa(x)=\log|\det D_xf_i(\lambda,x)|\) on \(E_i(\lambda)\); no next-step clock is assigned to a terminal.
All finite inverse histories are arbitrary legal compositions of these restricted inverses; every infinite inverse history is retained through all its compatible finite prefixes.
The full source packet of \(w\) is exactly all legal inverse images, of every depth, of every defined forward iterate \(T^n w\).
An inverse is defined at a terminal forward target whenever that target has a legal preimage; legality is imposed on the forward source, not by adding a target outgoing gate.

Define \(G=\{(z,m-n,w):T^mz=T^nw,\ m,n\ge0\text{ legal}\}\), identifying equal triples.
The arrow \((z,k,w)\) has source \(w\) and range \(z\); put \(c(z,k,w)=S_m(z)-S_n(w)\).
Two witnesses for the same triple differ by a common integer shift of \(m,n\); the longer sums add the identical common-tail sum, so \(c\) descends.
For composable witnesses \((m,n)\) and \((p,q)\), extend the shorter middle history to \(\max(n,p)\); the two middle sums cancel.
Thus \(c(gh)=c(g)+c(h)\), \(c(g^{-1})=-c(g)\), and the actual forward arrow \((Tx,-1,x)\) has clock \(-\kappa(x)\).
The complete kernels, without assuming injectivity of \(T\), are
\[
 K_{\rm lag}=\{(z,0,w):T^nz=T^nw\text{ for some legal }n\},\quad
 K_c=\{(z,m-n,w):T^mz=T^nw,\ S_m(z)=S_n(w)\},\quad
 K_{\rm joint}=K_{\rm lag}\cap K_c .
\]
These retain possible nonunit equal-depth merging arrows and all clock-cancelling arrows; there is no unproved simplification to units.
If a state never eventually reaches a periodic cycle, a nonzero-lag loop would force an eventual repetition, a contradiction; its source isotropy and \(H=c(G_w^w)\) are zero.
If its tail reaches a least-\(q\) cycle with signed sum \(C\), every loop lag is a multiple of \(q\), all such lags occur after reaching the cycle, and its clock is the corresponding multiple of \(C\).
Hence \(G_w^w=q\mathbb Z\), \(H_w=C\mathbb Z\), and extension isotropy is all \(q\mathbb Z\) when \(C=0\), but zero when \(C\ne0\).
The extension acts \((w,h)\mapsto(z,h+c(g))\); unrestricted vertical translation acts on its orbit set.
For each full source packet choose a reference \(w\), and an actual arrow \(g_z:w\to z\), with \(a_z=c(g_z)\).
Its complete extension-orbit phases are \([h-a_z]\in\mathbb R/H_w\); another reference arrow changes \(a_z\) by an element of \(H_w\).
Changing reference merely translates this phase coordinate, without deleting a phase or requiring a measurable global selector.
Vertical-translation stabilizer is exactly \(H_w\); if \(C\ne0\), the primitive is \(|C|\) and its positive returns are \(n|C|\), \(n\ge1\).
If \(H=0\), including a zero-clock periodic core, there is no positive physical return; all real phases remain.
The preceding statements retain the entire incoming tree and every terminal unit.

## 5. Rigidity and actual local continuation

### 5.1 Continuous actual branches

Let \(x_0(\lambda)=x(\lambda)\) be the frozen continuous least-\(q\) representative on connected open \(J\), and \(x_{j+1}=f_{i_j}(\lambda,x_j)\).
Every \(x_j\) is continuous, every phase belongs to its specified actual piece, and \(x_q=x_0\).
Joint C1 and spatial nonsingularity give a continuous signed cycle sum
\[
 C(\lambda)=\sum_{j=0}^{q-1}\log|\det D_xf_{i_j}(\lambda,x_j(\lambda))|.
\]
Section4 identifies the entire subgroup of its full incoming packet as \(C(\lambda)\mathbb Z\), not a subgroup inferred from one selected loop.
If the whole positive ledger of every parameter is prime-only, then
\[
 C(\lambda)\in\{0\}\cup\{\log p,-\log p:p\text{ an ordinary prime}\}.
\]
This subset of \(\mathbb R\) is discrete: each bounded interval meets finitely many \(\pm\log p\), and zero has the gap \(\log2\).
A continuous image of connected \(J\) is connected, so \(C\) is constant.
Either it is identically zero, with \(H=0\) and no positive return, or it is a single fixed \(\pm\log p\), with \(H=(\log p)\mathbb Z\) and primitive \(\log p\).
The sign cannot change through a silently deleted zero parameter. Least source period remains \(q\) by hypothesis, and positive physical repetitions remain \(n\log p\), not \(n\log p/q\).
This proves no constancy of individual step clocks, geometry, other cycles or their multiplicities; the prime-only hypothesis is necessary here, not sufficient for arithmetic admission.

### 5.2 Persistence under a genuinely legal joint neighborhood

At \((\lambda_0,x_0)\), let \(R(\lambda,x)=T_\lambda^q x\) be the stated word on the joint-open neighborhood where every nearby pair follows that complete legal word.
Its composition is joint C1; write \(M=D_xR(\lambda_0,x_0)\).
The equation \(R(\lambda,x)-x=0\) has spatial derivative \(M-I\), invertible by the frozen hypothesis.
The implicit-function theorem gives a unique local C1 solution \(\gamma(\lambda)\) near \(x_0\), with \(\gamma(\lambda_0)=x_0\).
Shrinking its open parameter interval keeps \((\lambda,\gamma(\lambda))\) within the legal joint neighborhood, so the returned branch is actual.
For each \(1\le r<q\), \(T_{\lambda_0}^r x_0\ne x_0\); all these finitely many inequalities persist by continuity of the legal prefix germs.
The continued points therefore have least period \(q\), not merely period dividing \(q\). For \(q=1\) no such exclusions are needed.
No invariance of the neighborhood under \(R\) was used; only the return equation and the full local legality assumption were used.
This proves local continuation, not global continuation through a permission boundary, singularity or changed least period.

### 5.3 Total sensitivity only in the joint-C2 subclass

Now additionally assume the relevant germs are joint C2, so the local implicit branch and return germ are C2.
On that branch write \(\gamma_j=T_\lambda^j\gamma\), \(v_j=\gamma_j'\), \(A_j=D_xf_{i_j}(\lambda,\gamma_j)\), and \(M(\lambda)=A_{q-1}\cdots A_0\).
Differentiating the actual return and phase equations gives
\[
 v_0=(I-M)^{-1}\partial_\lambda R(\lambda,\gamma),\qquad
 v_{j+1}=\partial_\lambda f_{i_j}(\lambda,\gamma_j)+A_jv_j,\qquad v_q=v_0.
\]
Here the first \(\partial_\lambda R\) holds the initial state fixed; the subsequent \(v_j\) restore the moving-state contribution.
The total derivative of the matrix at phase \(j\) is
\[
 \dot A_j=\partial_\lambda D_xf_{i_j}(\lambda,\gamma_j)
       +D_x(D_xf_{i_j})(\lambda,\gamma_j)[v_j].
\]
Nonsingular determinants have locally fixed sign, and differentiating their logarithmic absolute values yields
\[
 C'(\lambda)=\sum_{j=0}^{q-1}\operatorname{tr}(A_j^{-1}\dot A_j)
           =\operatorname{tr}(M^{-1}\dot M).
\]
The last equality follows by differentiating the ordered matrix product and cyclically moving factors inside each trace.
Thus a nonzero total derivative rules out prime purity on an open interval containing that point while this actual branch persists; it does not rule out that parameter by itself.
Zero derivative at one parameter alone proves no interval rigidity. Joint C1 supplies continuity and the C1 implicit branch, but does not supply the second derivatives in this formula.

## 6. Three complete external controls and adverse findings

All statements below hold at every parameter in \(I=(-1/2,1/2)\), not just sampled parameters.

### A. Varying linear multiplier

Put \(a=2+\lambda\in(3/2,5/2)\). The full diffeomorphism \(T(x)=ax\) has inverse \(\theta(y)=y/a\), \(J=1/a\), and \(\kappa=\log a\).
For every Borel \(B\subset\mathbb R\), \(\mu(\theta B)=\int_B a^{-1}dy\); all source and target states are legal.
Its complete arrows are \((a^{-k}w,k,w)\), \(w\in\mathbb R,k\in\mathbb Z\), with \(c=k\log a\).
Lag, clock and joint kernels are exactly units.
The only periodic core is \(0\), since \(a^n x=x\), \(n\ge1\), implies \(x=0\); its full incoming packet is the singleton \(\{0\}\).
There the least source period is1, source isotropy is \(\mathbb Z\), \(H=(\log a)\mathbb Z\), extension isotropy is0, and phases are \(h\bmod\log a\).
Each nonzero packet is \(\{\epsilon a^n r:n\in\mathbb Z\}\), uniquely labelled by \(\epsilon\in\{-1,1\}\), \(r\in[1,a)\).
Its source and extension isotropy are0, \(H=0\), and its complete real phase is \(h+\log|x|\).
There are no terminals or further incoming branches; every nonzero history is bilateral, approaching0 backward and unbounded forward.
Thus the entire positive primitive ledger is one packet of length \(\log a\), with repeats \(n\log a\).
It is prime-only exactly at \(\lambda=0\), since2 is the only prime in \((3/2,5/2)\); at that parameter it is nonempty and prime-unique, but not all-prime covering.
The actual branch \(0\) persists throughout \(I\), \(I-DT=1-a\ne0\), and \(C'(\lambda)=1/a\ne0\).
The family therefore fails prime purity on every open parameter interval, although its individual parameter \(\lambda=0\) has the stated necessary ledger properties.

### B. Nonlinear deformation with unchanged cycle clock

Write \(f(x)=2x+\lambda^2x^3\), \(d(x)=f'(x)=2+3\lambda^2x^2\ge2\).
The odd strictly increasing map has limits \(\pm\infty\), so it is a global diffeomorphism; its inverse is the unique real root of \(\lambda^2s^3+2s-y=0\), also when \(\lambda=0\).
Every-point \(J(y)=1/d(\theta y)\) gives IMAGE on every Borel set, and \(\kappa(x)=\log d(x)\).
For \(n\in\mathbb Z\), let \(D_n(x)=(f^n)'(x)>0\): for \(n>0\) it is \(\prod_{j=0}^{n-1}d(f^jx)\), \(D_0=1\), and \(D_{-n}(x)=1/D_n(f^{-n}x)\).
The entire groupoid is \((f^{-k}w,k,w)\), with \(c=-\log D_{-k}(w)\).
For \(k>0\), \(c\ge k\log2>0\); for \(k<0\), \(c\le k\log2<0\). All three kernels are units.
Because \(f(x)>x\) for \(x>0\) and \(f(x)<x\) for \(x<0\), the only periodic point is0, a singleton full incoming packet.
It has least period1, source isotropy \(\mathbb Z\), \(H=(\log2)\mathbb Z\), extension isotropy0 and phases \(h\bmod\log2\).
Every nonzero packet has unique labels \(\epsilon\in\{-1,1\}\), \(r\in[1,2+\lambda^2)\), and states \(x=\epsilon f^n(r)\), \(n\in\mathbb Z\).
Indeed \(|f(x)|\ge2|x|\), so all nonzero histories are bilateral, tending to0 backward and to infinity in magnitude forward, and cross this fundamental interval exactly once.
Oddness makes derivatives even, and the reference arrow \(\epsilon r\to\epsilon f^n r\) has lag \(-n\) and clock \(-\log D_n(r)\).
Thus every nonperiodic packet has source/extension isotropy0, \(H=0\), and full phase \(h+\log D_n(r)\); there are no terminal or additional inverse histories.
The complete positive ledger has one \(\log2\) primitive packet and repetitions \(n\log2\) for every parameter.
The branch \(0\) is jointly legal, \(1-f'(0)=-1\), \(\gamma'=0\), and its total cycle derivative is0.
Away from0 the geometry and clock vary with \(\lambda^2\); this is allowed by the theorem. Prime uniqueness holds here, all-prime coverage does not, and no endogenous prime grammar is constructed.

### C. Moving strict permission, with all terminal targets retained

The actual map is \(T(x)=2x\) only on \(x>\lambda\); \(x\le\lambda\) has no outgoing step.
Its whole inverse is \(\theta(y)=y/2\) on \(y>2\lambda\), with \(J=1/2\) and every-Borel IMAGE there.
Thus \(\kappa=\log2\) on the legal source; a terminal target \(y\in(2\lambda,\lambda]\) when \(\lambda<0\) still has its actual incoming arrow.
For \(n\ge1\), \(T^nx=2^nx\) is defined exactly when \(2^jx>\lambda\) for every \(0\le j<n\); this includes a possible terminal final value.
Writing \(D_n=\operatorname{dom}T^n\) and \(R_n=T^n(D_n)\), the complete depth-\(n\) inverse is \(y/2^n\) on \(R_n\), with IMAGE derivative \(2^{-n}\):

| Parameter | \(D_n\) | \(R_n\) |
| --- | --- | --- |
| \(\lambda<0\) | \((\lambda/2^{n-1},\infty)\) | \((2\lambda,\infty)\) |
| \(\lambda=0\) | \((0,\infty)\) | \((0,\infty)\) |
| \(\lambda>0\) | \((\lambda,\infty)\) | \((2^n\lambda,\infty)\) |

The positive-lag-\(n\) arrows are exactly \((w/2^n,n,w)\), \(w\in R_n\), and the negative ones exactly \((2^nw,-n,w)\), \(w\in D_n\).
To see exhaustiveness, cancel the common prefix in any positive-lag witness using injectivity of the corresponding actual iterate; the resulting relation is \(T^nz=w\).
Negative lags are inverses and lag0 gives units.
All nonzero arrows between states in the same packet listed below have the unique integer lag \(k\) satisfying \(z=2^{-k}w\), and clock \(k\log2\).
At0 there are all integer-lag loops only when \(\lambda<0\); when \(\lambda\ge0\) there is only its unit.
Consequently lag, clock and joint kernels are units in every parameter regime.

For \(\lambda<0\), the exhaustive source packets are:

- The fixed singleton \(\{0\}\).
- Positive bilateral packets \(\{2^nr:n\in\mathbb Z\}\), uniquely \(r\in[1,2)\).
- Negative terminating packets \(\{2^{-m}u:m\ge0\}\), uniquely \(u\in(2\lambda,\lambda]\), with final terminal \(u\).
- Isolated terminal singletons \(\{u\}\), \(u\le2\lambda\).

A negative legal state doubles until its unique first terminal value \(u\), and the previous strict inequality gives \(2\lambda<u\le\lambda\).
Each such terminal has the displayed infinite incoming chain tending to0 but never meeting it; a terminal at or below \(2\lambda\) has no inverse.
Hence no omitted incoming branch joins these packets to the fixed point or to one another.

For \(\lambda=0\), the exhaustive packets are the same positive bilateral packets and isolated terminal singletons \(\{u\}\), \(u\le0\).
For \(\lambda>0\), they are isolated terminal singletons \(\{u\}\), \(u\le\lambda\), and forward half-line packets \(\{2^nr:n\ge0\}\), uniquely \(r\in(\lambda,2\lambda]\).
Each latter packet has a legal initial state \(r\) with no predecessor, since \(r/2\le\lambda\), followed by its full infinite forward history.
There is no terminal forward endpoint in these positive packets. The included and excluded endpoints above follow exactly from the strict permission \(x>\lambda\).

The only periodic core is0 for \(\lambda<0\): its least period is1, source isotropy \(\mathbb Z\), \(H=(\log2)\mathbb Z\), extension isotropy0 and phases \(h\bmod\log2\).
Every other packet in every regime has source/extension isotropy0 and \(H=0\).
On each nonsingleton nonzero packet the full real phase is \(h+\log|x|\); on an isolated terminal its full real phase may be taken as \(h\).
Thus the positive primitive ledger has exactly one \(\log2\) packet for \(\lambda<0\), with all repeats \(n\log2\), and is empty for \(\lambda\ge0\).
It is prime-only throughout \(I\), nonempty only for \(\lambda<0\), and never all-prime covering; an empty ledger is not silently made nonempty.
The formal branch0 is actual only for \(\lambda<0\), where it has a joint-open legal neighborhood and return derivative2.
At \(\lambda=0\) and above it is a terminal, not a zero-clock fixed point; its formal derivative does not authorize the implicit-function persistence theorem.
There is therefore no continuous actual least1 branch0 on all of \(I\), and the disappearance at0 does not contradict Section5.

## 7. Results, controls and gate assessment

The three controls retain complete source and extension ledgers, not selected periodic centers or an artificial absorbing completion.
A separates family failure from individual necessary success; B refutes the stronger false claim that prime-only robustness forces constant geometry; C exposes actual-admission loss despite a smooth formal map.
General zero-clock cycles are retained in Sections4–5 even though the three controls' actual periodic cores have nonzero clock.
Arithmetic shuffles are inapplicable to this conditional class, not unreported successes; naturalness and PROVES_TOO_MUCH risks remain OPEN.

| Gate | Evidence | Status / boundary |
| --- | --- | --- |
| T0 | Separate full owners, actual inverse restrictions, complete arrows and phase sets | Established for the conditional class and controls |
| T1 clock component | Every-point IMAGE and spatial determinant clock, with exact cycle rigidity | Established COMPONENT ONLY; arithmetic T1 NOT PASSED |
| T2 | Entire \(H\), source/extension isotropy, all incoming, multiplicity and integer repeats | Established within the frozen class; no arithmetic prime source supplied |
| T3 | No same-owner operator, trace or zeta constructed | NOT AUDITED |
| Classical / formal / B | No classical suspension or formal evaluator invoked | NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

## 8. Conclusion and decision

Decision: retain this completed conditional filter for future admissible deformations and FORK the programme to a genuinely arithmetic carrier; do not promote any external control.
Use it only after an actual continuous least-period family or the stated legal persistence neighborhood has been established.
A nonconstant signed cycle clock defeats prime purity of that robust family, not every isolated parameter; missing legality, a changed least period or lost regularity ends the theorem's scope.
The same-object ledger stayed intact, and no next gate or new candidate is authorized by this paper.

## Reproducibility and evidence index

The complete exact arguments are above; inputs are the [card](candidate-card.md), [template](../paper-template.md), [claim ledger](claim-ledger.md) and [package overview](README.md).
Author reads used `sed -n '1,180p' papers/443-parameter-cycle-rigidity/candidate-card.md`, `sed -n '1,150p' papers/paper-template.md`, `wc -l` and `sha256sum`; card99 and template107 were read through EOF.
Current-entry reads were registry lines1–120 and root overview lines1–85; these contain historical summary outcomes, not any 440–444 manuscript or reviewer result.
Scouting read439card1–104/104 EOF, SHA256 `55e84d964286a4117d0fc6910ef7785f878c619af208211b5d46219652ab9ce3`, and389card1–112/112 EOF, SHA256 `7662964d7ee478b7eaf79bfb103ef3ac5361358cda7b2832a1bacdc7e159b43f`, including their outcomes.
Those collision reads and root's direction are design exposure, not blind selection, and neither prior theorem was imported as this proof.
All scientific work is exact derivation; no floating-point experiment, finite scientific census, target fitting, external literature search, network call, PDF or Git mutation was used.
Mechanical checks are full-file self-read, card-prefix hash, candidate/outcome agreement and local Markdown links; no mechanical check substitutes for a theorem.

### Assistance and integrity disclosure

AI author `/root/batch_clock_scope_review` derived and drafted this manuscript; root defined/integrates the card and performs internal workflow review.
Same-author helper `/root/batch_clock_scope_review/ccg_cotangent_probe` first checked definition ambiguities by messages only, with no files, tools, algebra or proof.
After release the same helper derived only control C's full histories, phases and kernels from the frozen card: its only tool operations were `sed -n '1,140p'` on that card, read through the explicit99-line EOF, and `sha256sum`, matching the scientific-prefix hash in §3.
It reported no other file access, writes, scientific code/numerics, network or additional agents; its formulas were checked against the author's complete C ledger before inclusion.
It is an author aid, not a review seat; the author's final proof and three surfaces remain the author's responsibility.
No 443 review-scope, raw, final comparison or new peer manuscript was read by this author; root's CP1 pass notification contained no proof result.
AI agents supplied mathematical derivation, drafting and internal checking; shared-history same-model assistance is `NOT_CALIBRATED`, not blind, external or cross-model verification.
No human or external mathematical verification is certified. Human contributions, funding and competing interests are unspecified; there are no human-participant data.
ARS was used for bounded proof/draft and disclosure discipline, not a publication pipeline; external journal criteria are `criteria_binding_unavailable`, and publication readiness is not claimed.
