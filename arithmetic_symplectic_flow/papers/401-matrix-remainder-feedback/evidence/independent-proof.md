# 401 — frozen card-only independent derivation

Candidate: `ANG-20260922-MRF01`. Internal shared-history `NOT_CALIBRATED`.
Role: raw mathematical derivation after root accepted CP1 and explicitly released mathematics.
Sole scientific input: `candidate-card.md`, lines 1–88, read through its actual EOF.
Card SHA256: `97c81980e34b430191329cd1ef63965239c57cf0ab707a6fdcc6b587a404a4e5`.
Frozen CP1: `scope-review.md`, 77 lines, SHA256 `54b3ec265103eaeca151155e6f534119baf1f2a8641b746221f2437738585055`.
The card was read again in full during this derivation; metadata checks confirm both receipts.
At final raw verification the card had grown to 107 lines; its appended outcome was NOT read.
Hashing only the preserved first 88 lines again returned the released card SHA256 above; the original 88-line EOF receipt does not claim access to the later append.
No current manuscript, README, claim ledger, author output, peer output, or other new scientific package was read.
This is not blind review, external peer review, or an independent-model calibration.
The ARS academic-research-suite skill, model-runtime policy and Devil's Advocate instructions were fully read during this 401 task; workflow/reference instructions retained from CP1 were not falsely recorded as newly read.
ARS supplies the staged evidence boundary: raw work now freezes before any separate PAPER UNLOCK.
No web, numerical experiment, orbit census, auxiliary agent, model change, or external data was used.

## 1. Common source cells and four genuinely separate transports

Write a state as $z=(X,Y)\in\mathcal Y=M_2(\mathbb R)^2$, with eight-dimensional Lebesgue measure.
For invertible $X,Y$, put $A=XY^{-1}$, $Q=\lfloor A\rfloor$, $P=\lfloor A^{-1}\rfloor$, and let $d$ be the frozen content of the eight integer entries.
For a fixed integer pair $(Q,P)$, write
\[
B=\begin{pmatrix}I&-Q\\-P&I\end{pmatrix},\qquad b=\det B.
\]
The digit cell imposes both displayed floors, not only a forward formula using guessed digits.
MAIN, N and R retain precisely its points with $X,Y$ invertible, $d\ge2$, and $b\ne0$.
G instead permits every $d\ge0$, still requires $X,Y,B$ invertible, and uses $e=\max(1,d)$.
These source cells are Borel: inversion is continuous on the open invertible locus, and entrywise floor is Borel including every integer cut.
They are disjoint for distinct digit pairs and countably cover each owner's legal domain.
Every point outside that owner's domain remains in its full source as a terminal, not an absorbing periodic point.

On each cell, the four forward maps are restrictions of nonsingular linear maps of the entire ambient space.
On each column of the stacked pair of matrices, these linear maps are respectively
\[
B/d,\quad B/e,\quad B,\quad d^{-1}\begin{pmatrix}I&-Q\\0&I\end{pmatrix}
\]
for MAIN, G, N, R. R still keeps the frozen condition $b\ne0$ and the reverse floor $P$; neither is dropped because its triangular formula could exist without them.
Their ambient columnwise linear inverses are respectively
\[
dB^{-1},\quad eB^{-1},\quad B^{-1},\quad
\begin{pmatrix}dI&dQ\\0&dI\end{pmatrix}.
\]
Multiplication in either order gives the identity; these are exactly the four reconstruction formulas in the card.
For each owner and digit pair let $D_{QP}$ be its actual source cell and define
\[
E_{QP}=\{v:\Theta_{QP}(v)\in D_{QP}\}.
\]
This is Borel. Its definition is precisely the required reconstructed-source checks; substitution also verifies the original forward equality.
No check requires that $v$ itself have a legal next step, or even invertible matrix coordinates.
The restricted map $\Theta_{QP}:E_{QP}\to D_{QP}$ is a Borel bijection with inverse the owner's forward restriction.
Thus both inverse identities hold, including boundary and terminal-target points.
Conversely, every actual predecessor supplies its unique two floor matrices and belongs to this enumerated inverse branch.
Distinct pairs cannot reconstruct the same predecessor, because its floors would then have two values.
Different branches can nevertheless have the same target: the global partial map is not asserted injective.
Repeated inverse enumeration gives every finite incoming history, with each intermediate source checked under that owner's own law.

## 2. Exact every-point IMAGE and same-transport clocks

Block row elimination gives
\[
b=\det(I-PQ)=\det(I-QP)\in\mathbb Z\setminus\{0\}.
\]
This calculation requires no invertibility of $Q$ or $P$.
Grouping coordinates by columns gives two copies of the four-dimensional column transformation; coordinate permutations do not change an absolute determinant.
Consequently the inverse eight-dimensional determinants are
\[
J_{\rm MAIN}=d^8/b^2,\qquad J_G=e^8/b^2,\qquad
J_N=b^{-2},\qquad J_R=d^8.
\]
For R, each column's triangular inverse has determinant $d^4$; the off-diagonal block $dQ$ does not change it.
All four displayed values are finite and strictly positive on every actual branch domain.
For every Borel $E\subseteq E_{QP}$, ordinary nonsingular linear change of variables proves
\[
\mu(\Theta_{QP}E)=J_{QP}\mu(E).
\]
This holds for null, integer-cut, and other lower-dimensional restrictions as well as open sets.
The displayed ambient linear determinant is the card's frozen all-point version; a null-set IMAGE identity alone would not uniquely determine a version there.
The source measure is full-support, nonatomic and sigma-finite; no invariant probability or canonical coordinate-free measure is asserted.
The countable atlas also supplies measure-class nonsingularity on the respective legal source and image pieces.

It is useful to define the owner's strictly positive rational branch factor
\[
\beta_{\rm MAIN}=|b|/d^4,\quad \beta_G=|b|/e^4,\quad
\beta_N=|b|,\quad \beta_R=d^{-4}.
\]
Then $J=\beta^{-2}$ and the frozen clock is exactly $\kappa=2\log\beta$.
This clock is defined only on legal steps, not at forward terminals.
It is not a positive roof: N has nonnegative local clock, R has strictly negative local clock, and positivity is not imposed on MAIN or G.

## 3. Actual arrows, descent and full kernels

The following construction is performed separately for all four owners.
Let $\mathcal D_m$ be the states having $m$ legal steps, with $\mathcal D_0=\mathcal Y$; the final state may be terminal.
Define
\[
R_m(z)=\prod_{0\le i<m}\beta(T^iz),\qquad R_0=1,\qquad S_m=2\log R_m.
\]
Each $R_m$ is a positive rational-valued Borel function on its history domain.
The arrow set is the actual subset of $\mathcal Y\times\mathbb Z\times\mathcal Y$
\[
G=\{(z,m-n,w):z\in\mathcal D_m,\ w\in\mathcal D_n,\ T^mz=T^nw\}.
\]
It is Borel by countably many equalities between Borel iterates; incoming fibres are countable by the full inverse atlas.
Equal triples, not equal inverse words alone, are identified. Source is $w$, range is $z$.
Set
\[
c(z,m-n,w)=2\log\frac{R_m(z)}{R_n(w)}.
\]
For two witnesses of the same triple, their indices differ by the same integer.
Order them so the second uses more steps; the extra factors are taken along the identical shared forward tail and cancel from this quotient.
That tail exists because the longer witness exists; no continuation through a terminal is presumed.
This proves all-point descent to actual retained-lag arrows.
For composition, align the two witnesses' legal histories on their common middle state at the larger of their two middle indices.
Both added tails then exist, their factors cancel, and $c(gh)=c(g)+c(h)$; inversion negates $c$.
This also proves closure of the displayed arrow set under the usual multiplication and inversion.

A fixed finite inverse-history chart has determinant $R_m^{-2}$.
An arrow chart obtained from two histories to one common future has source-to-range IMAGE factor
\[
J_g=R_n(w)^2/R_m(z)^2=e^{-c(g)}.
\]
Linear change of variables on each fixed branch-word chart proves this for every Borel restriction.
All-point versions agree on different presentations by the descent just proved; no new null-set choice is made.

With $\ell(z,j,w)=j$, the entire kernels, not just their isotropy parts, are
\[
\begin{aligned}
\ker\ell&=\{(z,0,w):\exists m\text{ legal},\ T^mz=T^mw\},\\
\ker c&=\{(z,m-n,w)\in G:R_m(z)=R_n(w)\},\\
\ker\ell\cap\ker c&=\{(z,0,w):\exists m\text{ legal},\ T^mz=T^mw,\ R_m(z)=R_m(w)\}.
\end{aligned}
\]
These are exact full-state descriptions using finite histories and rational equality, independent of the chosen witnesses.
They do not collapse to units merely because each individual branch is invertible.
For an explicit check in all four owners, take $z_n=(\operatorname{diag}(n,1/2),I)$, $n=4,6$.
Both have $Q=\operatorname{diag}(n,0)$, $P=\operatorname{diag}(0,2)$, $d=2$, $b=1$.
MAIN and G send both states to $(\operatorname{diag}(0,1/4),\operatorname{diag}(1/2,0))$.
N sends both to $(\operatorname{diag}(0,1/2),\operatorname{diag}(1,0))$.
R sends both to $(\operatorname{diag}(0,1/4),I/2)$.
These targets are retained terminals, and the two branch factors agree within each owner.
Thus $(z_4,0,z_6)$ is an actual nonunit arrow in both kernels and their intersection for each owner.
This is an exact source-check witness, not a numerical census.

## 4. Entire isotropy, all incoming histories and all phases

For a deterministic partial map, nonzero self-lag occurs exactly at an eventually periodic state.
Indeed $T^mz=T^nz$ with $m>n$ exhibits a legal periodic tail; conversely any such tail supplies self-arrows of its period.
If the least eventual period is $r\ge1$, every return difference is a multiple of $r$, and every multiple is realized after following sufficiently many legal cycle steps.
Therefore the entire source isotropy is $r\mathbb Z$, retaining integer lag even when clocks vanish.
Put
\[
\rho=\prod_{i=0}^{r-1}\beta(T^i z_*)\in\mathbb Q_{>0},\qquad C=2\log\rho,
\]
where $z_*$ is any point of that least periodic core.
The finite preperiod cancels, cycle phase does not change the product, and $c(kr)=kC$.
Consequently the ENTIRE clock subgroup is $H_z=C\mathbb Z$, not the group generated by a selected presentation or selected loop.
At a state with no eventually periodic tail, source isotropy and $H_z$ are both zero.

The extension has every point $(z,h)\in\mathcal Y\times\mathbb R$, with arrow $(w,h)\mapsto(z,h+c(g))$.
Its isotropy is the clock kernel inside source isotropy: $r\mathbb Z$ when $C=0$, and zero when $C\ne0$; states without a periodic tail have zero extension isotropy.
In particular, $C=0$ does not delete the original lag isotropy or its arrows.
All extension orbits over any one source orbit are parametrized by $\mathbb R/H_z$, after choosing a base point in that orbit.
To see completeness, use any incoming arrow to bring a representative to that base point; two choices differ exactly by a source-isotropy clock in $H_z$.
Vertical translation has stabilizer $H_z$ on the orbit SET, so a positive primitive exists precisely when $C\ne0$, and then
\[
L=|C|,\qquad H_z=L\mathbb Z,
\]
with positive repetitions $kL$, $k=1,2,\ldots$.
Negative cycle clock is not an absence of positive physical time; its absolute value is the positive generator.
When $H_z=0$, all real phases remain and there is no positive period, whether or not extension isotropy is nontrivial.
Distinct source orbits with the same $C$ remain distinct packets; eventual backward trees attach to their actual periodic core, not to a chosen representative.

For a complete incoming prescription at any $z$, choose any legal $m\ge0$, then any length-$n\ge0$ source-checked inverse history ending at $T^mz$.
If its initial state is $w$, retain the actual triple $(z,m-n,w)$, deduplicating only equal triples.
Its source height for an arrow ending at $(z,h)$ is exactly $h-c(z,m-n,w)$.
The exhaustive atlas proves that this enumerates every incoming arrow and every allowed source phase.
For a terminal $z$, necessarily $m=0$, but all such backward histories remain; its own source isotropy and $H_z$ are zero and its phase set is $\mathbb R$.
No orbit tree, singular target, null branch, or failed forward permission has been removed.

## 5. Complete fixed sets of MAIN and all controls

These fixed sets mean $z$ belongs to the legal domain and $Tz=z$; $T^0z=z$ at a terminal is not a fixed return.
For MAIN, or G with its scale $s=e\ge2$, the fixed equations give
\[
Q=(1-s)A,\qquad P=(1-s)A^{-1}.
\]
The same equations use $s=d\ge2$ for MAIN.
Let $h=s-1\ge1$. Each entry $q$ of $Q$ satisfies $q=\lfloor-q/h\rfloor$, so
\[
q\le -q/h<q+1\quad\Longrightarrow\quad -h/(h+1)<q\le0.
\]
Thus $q=0$ for every entry, forcing $A=0$, contrary to invertibility.
This excludes every such cell, with no sign or cut exception.

For G at scale $e=1$, the fixed equations imply $QY=0$ and $PX=0$, hence $Q=P=0$ and $d=0$.
The putative cell would require both $A$ and $A^{-1}$ entrywise in $[0,1)$.
Write $A=\begin{pmatrix}a&b_0\\c_0&f\end{pmatrix}$ with these bounds and determinant $\Delta\ne0$.
If $\Delta>0$, nonnegative inverse off-diagonal entries force $b_0=c_0=0$; then $a,f>0$ and the inverse has diagonal entries $1/a,1/f>1$, a contradiction.
If $\Delta<0$, nonnegative inverse diagonal entries force $a=f=0$; then $b_0,c_0>0$ and the inverse has off-diagonal entries $1/c_0,1/b_0>1$, again a contradiction.
Thus this actual digit cell is empty, rather than removed by a new permission.

For N, being fixed implies $QY=PX=0$, hence $Q=P=0$, contradicting its retained $d\ge2$ gate.
For R, being fixed implies $Y/d=Y$; invertibility of $Y$ forces $d=1$, again contradicting its gate.
Therefore ALL FOUR complete fixed sets are empty.
There are no actual fixed cores to which an $H$ or phase packet could be assigned; the full incoming and isotropy prescriptions of Section 4 nevertheless apply to every retained state.
An empty fixed set alone says nothing about MAIN's higher-period states or its global target.

## 6. All-cycle algebraic clock filter and separately owned control ledgers

For MAIN, every actual least periodic core has the rational number $\rho>0$ of Section 4.
If $\rho=1$, its full $H=0$ gives no positive primitive, with its lag isotropy retained.
If $\rho\ne1$, its least positive multiplier is
\[
\exp L=\exp|2\log\rho|=
\begin{cases}\rho^2,&\rho>1,\\\rho^{-2},&0<\rho<1.\end{cases}
\]
It is a rational square greater than one, and cannot equal an ordinary integer prime.
Indeed, if a reduced positive fraction $u/v$ has $(u/v)^2=p\in\mathbb Z$, then $v^2\mid u^2$, so $v=1$; an integer square greater than one is not prime.
The same conclusion holds for every positive repetition, since its multiplier is another rational square.
All possible positive primitives arise from the full isotropy classification above; there is no additional positive packet at a non-eventually-periodic state.
Thus MAIN has NO ordinary-integer-prime positive primitive, whether or not any positive primitive or higher cycle exists at all.
The target is explicitly NONEMPTY, so this is a decisive global necessary-target failure, not a vacuous positive result.
Cycle existence, higher-period census, multiplicities of nonprime packets, and their numerical values are not needed or asserted.

G has its OWN exhaustive cells, histories and factor $|b|/e^4$; the identical rational-square calculation applies to every actual G periodic core.
Its full conditional ledger is $r\mathbb Z$, $C=2\log\rho$, $H=C\mathbb Z$, with precisely the extension isotropy, phases, primitives and repetitions in Section 4.
Permitting smaller contents therefore does not remove this necessary clock obstruction; no G orbit is borrowed for MAIN.
N has its OWN histories and factor $|b|\in\mathbb Z_{\ge1}$.
On any actual N cycle, $\rho$ is an integer; $\rho=1$ yields the retained zero-clock isotropy, while $\rho>1$ gives $L=2\log\rho$ and an integer-square primitive multiplier.
Its complete conditional ledger is again Section 4 with N's own products, not MAIN's histories.
No assertion of cycle existence is needed for either control's all-cycle filter.

R admits a stronger, direct complete empty-periodic-ledger result using its own update.
Along any legal length-$k$ history,
\[
Y_k=Y_0/(d_0d_1\cdots d_{k-1}).
\]
A closed positive-length history would have invertible $Y_0$ and force this integer product to be 1, whereas every $d_i\ge2$.
Therefore R has no actual cycles and no eventually periodic states.
For EVERY R state the source isotropy, extension isotropy and $H$ are zero, all phases are $\mathbb R$, and the positive packet ledger is empty.
R still has all its terminal incoming histories and nonunit off-diagonal kernels, including the witness in Section 3.
This exact coordinate-product argument is an all-cycle algebraic filter, not an expanded orbit search, and is not transferred to MAIN, G or N.

## 7. Exact lineage and disposition

For the frozen integers $n\ge2$, $1<q<n$, set $X=\operatorname{diag}(n,1/q)$, $Y=I$.
Direct floors give $Q=\operatorname{diag}(n,0)$, $P=\operatorname{diag}(0,q)$, so $d=\gcd(n,q)$ and $q\mid n\iff d=q$.
Here $PQ=QP=0$, hence $b=1$, and the source coordinates are invertible.
The MAIN permission on this slice is exactly $d\ge2$; coprime pairs remain terminals rather than being silently declared admissible.
In particular, every proper-divisor witness passes the permission.
For a legal such state the actual MAIN image is
\[
(U,V)=(\operatorname{diag}(0,1/(dq)),\operatorname{diag}(1/d,0)).
\]
Both matrices are singular, so this displayed lineage slice reaches a retained terminal in one step.
This is a fact about that slice, not a replacement of the full source or a no-cycle theorem for the owner.
The proper-divisor/content interface and the current-state rereading mechanism are exact; prime-only admission, GL invariance and stronger arithmetic naturalness are not established.

T0: complete partial Borel owner, actual inverse atlas and retained-lag extension verified on all points.
T1: the frozen all-point determinant clock belongs to that same transport; designed coordinate/measure choices and strong naturalness remain disclosed/OPEN.
T2: the full ledger convention is derived, and the NONEMPTY ordinary-prime primitive target fails by the global rational-square obstruction.
T3 NOT AUDITED; classical NOT APPLICABLE; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
Portfolio: STOP / FORK. Do not repair the measure, tune a roof, delete fibres, borrow a control orbit, or run a longer census on this candidate.
The decisive conclusion was messaged to root before this report was written.
Raw derivation now freezes; CP1 remains unchanged. Manuscript comparison and final-surface review await a separate PAPER UNLOCK.

EOF — card-only independent derivation; no current manuscript access.
