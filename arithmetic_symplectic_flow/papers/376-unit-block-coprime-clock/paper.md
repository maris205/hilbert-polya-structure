# Hard coprime unit-block histories: a whole-source IMAGE clock with composite primitive packets

**Paper:** `376-unit-block-coprime-clock`  
**Candidate:** `ANG-20260922-UBC01`  
**Batch / date:** `HARD-NONLOCAL-20260922-F`, round 2/5; 2026-09-22  
**Status:** `OWNED HARD-BLOCK IMAGE CLOCK; COMPOSITE PRIMITIVE PACKETS — STOP / FORK`  
**Scope:** broadened T0–T2; classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The source consists of all one-sided positive-integer histories whose letters between visible units are pairwise coprime. We retain unbounded segments, marker-free tails, and all null histories. The frozen length-biased block construction gives a stationary nonatomic probability of full support. Its suffix sum \(F\) proves the exact every-Borel inverse-branch IMAGE identity. The declared completion on marker-free tails is a valid Borel version, but is not determined uniquely by that identity. We compute complete clock and lag kernels, source and extension isotropy, incoming histories, height phases, and the entire primitive block-necklace ledger. The packets \(1^\infty,(12)^\infty,(1213)^\infty\) have least times \(\log2,\log8,\log192\), respectively. Thus a correct first prime packet does not meet the full target. Three separately specified controls receive whole-source ledgers. Hard nonlocal constraints do not remove this owner's free block splicing, and the candidate stops without changing its measure or null completion.

## 1. Frozen object, lineage, and full inverse domains

All definitions refer to the [88-line original card](candidate-card.md), including root's pre-freeze replacement of the scout's generic limit/fallback rule by the explicit \(F\) law. Write \(A=\{2,3,\ldots\}\), \(B=\{1,2,\ldots\}\). Let \(X\subset B^{\mathbb N_0}\) contain precisely those sequences in which any two nonunit letters having no intervening unit are coprime. Unit \(1\) is a visible delimiter. The source includes \(1^\infty\), finite-marker histories, and entirely marker-free histories; none is adjoined or removed after calculating returns.

The topology is the discrete-product subspace topology and its Borel structure. A violation is witnessed by a finite interval, so \(X\) is closed in the Polish product. Left shift \(T\) is everywhere defined and preserves \(X\). Every actual inverse is \(I_a(y)=ay\), with \(E_a=\{y:ay\in X\}\). Here \(E_1=X\); for \(a\ge2\), membership means coprimality with every letter before the first unit, or every letter of the entire tail if no unit occurs. These are Borel domains, and \(I_a:E_a\to[a]\cap X\) is a Borel bijection with inverse \(T\). Exhaustiveness follows by reading the first letter of any predecessor. There are no terminal states or omitted incoming branches; no étale assertion is needed.

The preserved arithmetic interface is the full vector \(1_{d\mid a}\), \(d\ge2\): a legal new letter cannot share a nontrivial divisor with any earlier letter of its unfinished segment. Proper-divisor witnesses therefore affect actual admissibility, not an external label. This is common-divisor exclusion, not an equivalence between admissibility and primality. The visible unit ends a segment; it does not softly permit an illegal extension inside that segment. Declared block weights and the null completion remain design choices; strong naturalness is OPEN.

## 2. Construction and the common measured-block lemma

Put \(\rho(a)=1/[a(a-1)]\). Its sum is one by telescoping. For MAIN, let \(W\) be all finite pairwise-coprime \(A\)-words, including \(\varnothing\), and set
\[
Z_n=\sum_{\substack{w\in W\\|w|=n}}\prod_i\rho(w_i),\quad Z_0=1,\qquad
p(w)=2^{-|w|-1}\frac{\prod_i\rho(w_i)}{Z_{|w|}},\qquad
M=\sum_w(|w|+1)p(w).
\tag{1}
\]
For every \(n\), a length-\(n\) pairwise-coprime word exists: start at 2 and repeatedly append one plus the product of all previous letters. Any common divisor with a preceding letter would divide one. Thus \(0<Z_n\le1\). Summing (1) by length gives total mass one, length law \(2^{-n-1}\), and \(M=\sum_{n\ge0}(n+1)2^{-n-1}=2\). In particular \(0<p(w)\le2^{-|w|-1}\le1/2\).

The same measured-block argument below is applied to each row using that row's own source and block probability:

| Owner | Legal blocks and block probability | \(M\) | Marker-free completion |
| --- | --- | --- | --- |
| MAIN | \(W,p\) in (1) | \(2\) | \(\beta=1\) below |
| ARITHMETIC-OFF | all finite \(A\)-words; \(p(w)=2^{-\lvert w\rvert-1}\prod_i\rho(w_i)\) | \(2\) | own source, \(\beta=1\) |
| SINGLE-LETTER-BLOCK | \(W=\{\varnothing\}\cup A\); \(p(\varnothing)=1/2,\ p((a))=\rho(a)/2\) | \(3/2\) | no marker-free source points |
| BOUNDARY-SWITCH | MAIN's exact \(X,\mu,p,F\) | \(2\) | \(\beta=2\) below |

OFF has full source \(B^{\mathbb N_0}\). SINGLE has the whole source with no two consecutive nonunit letters, not a source enlarged by impossible infinite unmarked paths. Each first three rows constructs its own probability: choose the origin block \(1w_0\) with probability \((|w_0|+1)p(w_0)/M\), choose its origin offset uniformly, and concatenate independent \(p\)-blocks on both sides. BOUNDARY-SWITCH intentionally retains MAIN's measure but changes the declared null-point version. Auxiliary blocks and offsets construct the measure only; they are not extra dynamical objects later discarded.

For any of the three block distributions and bounded Borel \(f\) on its source, the resulting right-tail law satisfies
\[
\int f\,d\mu=\frac1M\mathbb E\sum_{j=0}^{|w_0|}
 f\bigl(T^j(1w_0\,1w_1\,1w_2\cdots)\bigr),
\tag{2}
\]
where \(w_0,w_1,\ldots\) on the right are independent with law \(p\). This proves normalization directly. The difference between (2) for \(f\circ T\) and \(f\) telescopes to
\[
\frac1M\mathbb E\left[f(1w_1\,1w_2\cdots)-f(1w_0\,1w_1\cdots)\right]=0.
\]
Thus the measure is stationary. The concatenation is measurable, has only finite blocks, belongs to the declared source, and has infinitely many units almost surely. In particular the marker-free set \(N\), and the eventually-marker-free set \(\bigcup_{j\ge0}T^{-j}N\), have measure zero. These statements concern measure, not removal of any source points.

For a legal finite nonunit word \(v\), define
\[
F(v)=\sum_{\substack{u\ {\rm finite}\\uv\in W}}p(uv),\qquad
F(\varnothing)=1,\qquad
F(v)=p(v)+\sum_{\substack{a\in A\\av\in W}}F(av).
\tag{3}
\]
Each word ending in \(v\) occurs at most once in the defining sum, so \(p(v)\le F(v)\le1\). The last equality partitions its left extension into the empty word or a word whose last letter is \(a\); all series are nonnegative. Let \(\nu\) denote the law of \(w_0\,1w_1\,1w_2\cdots\) for independent \(p\)-words. For every Borel \(E\) in the row's source,
\[
\mu(v1E)=\frac{F(v)}M\nu(E),\qquad
\mu(1v1E)=\frac{p(v)}M\nu(E).
\tag{4}
\]
For nonempty \(v\), the first identity sums the terms of (2) at offsets where the origin block has suffix \(v\). The next block is independent, giving \(\nu(E)\). For empty \(v\), the origin is at a unit, and (2) gives \(F(\varnothing)\nu(E)/M\). The second identity fixes the entire origin block to \(1v\). This proves (4) for all Borel tails, not only cylinders.

Every legal finite prefix can be followed by a unit. Applying (4) and then the independent subsequent block probabilities makes that extended cylinder positive. Hence \(\mu\) has full support on the whole declared source. A history with infinitely many units fixes successively more completed blocks; its cylinder masses are bounded by \(F(v_0)M^{-1}\prod_{i=1}^kp(v_i)\le M^{-1}2^{-k}\). Its singleton mass is zero. Histories with finitely many units are already in the null set above. Thus each measure is nonatomic, including at every periodic point.

## 3. Frozen all-point versions and every-Borel IMAGE

On \(C_v=\{v1\xi:\xi\in X\}\), the finite-first-marker formulas are
\[
q_1(y)=p(v)/F(v),\qquad
q_a(y)=F(av)/F(v)\ \ (av\in W),\qquad q_a(y)=0\ \ (ay\notin X).
\tag{5}
\]
The sets \(C_v\) are Borel and partition \(X\setminus N\). Equations (3)–(5) prove normalization, finiteness, and strict positivity on precisely the legal inverse domains. These formulas use the appropriate row's \(F,p,X\).

On the entire marker-free part of MAIN, OFF, or BOUNDARY-SWITCH, put
\[
\mathcal A(y)=\{a\ge2:ay\in X\},\qquad
R(y)=\sum_{a\in\mathcal A(y)}\rho(a),\qquad
q_1(y)=\frac{\beta}{\beta+R(y)},\quad
q_a(y)=\frac{\rho(a)1_{\mathcal A(y)}(a)}{\beta+R(y)}.
\tag{6}
\]
Here \(\beta=1\) for MAIN/OFF and \(\beta=2\) for BOUNDARY-SWITCH. This is exactly the frozen normalization of \(b_1,b_a\). It remains defined when \(\mathcal A(y)\) is empty: then \(q_1=1\). The indicators of the actual Borel domains make (6) Borel; its denominator is positive, its sum is one, and every legal branch has positive finite value. SINGLE has no \(N\) and uses only (5).

**Every-Borel identity.** For each actual branch and every Borel \(E\subset E_a\),
\[
\mu(I_aE)=\int_Eq_a\,d\mu.
\tag{7}
\]
On \(C_v\), write a Borel subset as \(v1D\). For \(a=1\), the two equations (4) give ratio \(p(v)/F(v)\). For legal \(a\ge2\), the first equation at \(av\) and at \(v\) gives ratio \(F(av)/F(v)\). Integrating and summing over the countably many \(C_v\) proves (7) off \(N\). On \(N\), both the integral and image measure are zero: \(I_aN\) has at most one unit, hence lies in the already proved null eventually-marker-free set. This finishes (7) on the whole source. It proves that (6) is an admissible Borel version, not that it is forced by a limiting or continuity principle.

All-point version dependence is explicit. Let \(y_n=2^{2^n}+1\), \(n\ge0\). The identity \(\prod_{j<n}y_j=y_n-2\) follows by induction from \(y_{n+1}=(y_n-1)^2+1\). If \(m<n\), a common divisor of \(y_m,y_n\) divides 2, while both are odd; hence these letters are pairwise coprime. Thus the entire marker-free tail \(y\) belongs to MAIN, and 2 is a legal predecessor. Consequently \(R(y)\ge\rho(2)>0\), and
\[
q_1^{\rm MAIN}(y)=\frac1{1+R(y)}
\ne \frac2{2+R(y)}=q_1^{\rm SWITCH}(y).
\tag{8}
\]
Both satisfy (7) for the same measure and actual map. The inverse-unit clock values differ at this retained history. We claim neither continuity nor canonical uniqueness of MAIN's completion; changing a null version after inspecting returns would change the frozen clock owner.

## 4. All finite histories and explicit full kernel formulas

For a finite visible word \(u=a_0\cdots a_{m-1}\), let \(E_u=\{\xi:u\xi\in X\}\) and
\[
Q_u(\xi)=\prod_{j=0}^{m-1}q_{a_j}(a_{j+1}\cdots a_{m-1}\xi),\qquad Q_\varnothing=1.
\tag{9}
\]
Iteration of the nonnegative-Borel change-of-variable form of (7) proves \(\mu(uE)=\int_EQ_u\,d\mu\) for every Borel \(E\subset E_u\). For the full domain \(D_{u,v}=E_u\cap E_v\), the actual replacement \(v\xi\mapsto u\xi\) has IMAGE derivative \(Q_u(\xi)/Q_v(\xi)\) at \(v\xi\), by applying this identity twice. No unconstrained full-shift branch is inserted.

For complete, directly evaluable kernel sets we give \(Q\) without truncating histories. Parse a prefix uniquely as \(u=u_0\,1\,u_1\,1\cdots1\,u_k\), where each \(u_i\) is nonunit and \(k\) is the number of units. On \(\xi=v1\eta\),
\[
Q_u(\xi)=
\begin{cases}
F(u_0v)/F(v),&k=0,\\
\displaystyle\frac{F(u_0)\left(\prod_{i=1}^{k-1}p(u_i)\right)p(u_kv)}{F(v)},&k\ge1.
\end{cases}\tag{10}
\]
All expressions are restricted to the actual legal domain; empty nonunit pieces are allowed. To prove (10), insert the last nonunit piece, whose successive \(F\)-ratios telescope, then the preceding unit, whose numerator is \(p\); repeat leftward. This works for MAIN, OFF, SINGLE, and SWITCH with their own data.

For a marker-free \(\xi\), and a nonunit prefix \(t=t_0\cdots t_{\ell-1}\), define on its legal domain
\[
D_t^\beta(\xi)=\prod_{j=0}^{\ell-1}
\frac{\rho(t_j)}{\beta+R(t_{j+1}\cdots t_{\ell-1}\xi)},\qquad D_\varnothing^\beta=1.
\]
Then the complete remaining cases are
\[
Q_u(\xi)=
\begin{cases}
D_{u_0}^{\beta}(\xi),&k=0,\\
\displaystyle F(u_0)\left(\prod_{i=1}^{k-1}p(u_i)\right)
\frac{\beta D_{u_k}^{\beta}(\xi)}{\beta+R(u_k\xi)},&k\ge1.
\end{cases}\tag{11}
\]
Indeed, until the first inserted unit, (6) gives exactly the factors in \(D\) and the final unit factor. After that unit is inserted, all remaining prefix insertions use (5) with first-marker suffix empty, yielding the displayed \(F,p\) factors. Formula (11) is not used on SINGLE's nonexistent boundary.

Use the actual Borel groupoid
\[
G=\{(z,m-n,y):m,n\ge0,\ T^mz=T^ny\},
\tag{12}
\]
with source \(y\), range \(z\), inverse \((y,-k,z)\), and composition \((z,k,y)(y,l,w)=(z,k+l,w)\). Equal triples are identified and integer lag is retained. Its Borel structure is inherited from \(X\times\mathbb Z\times X\). Every arrow has a legal prefix presentation \((u\xi,|u|-|v|,v\xi)\).

Set \(\kappa(z)=-\log q_{z_0}(Tz)\), \(A_m(z)=\sum_{i=0}^{m-1}\kappa(T^iz)\), \(A_0=0\). All terms are finite on the whole source. The same IMAGE owner has
\[
c(z,m-n,y)=A_m(z)-A_n(y)
 =\log\frac{Q_v(\xi)}{Q_u(\xi)}.
\tag{13}
\]
The product identity \(Q_{uw}(\xi)=Q_u(w\xi)Q_w(\xi)\) cancels the common extension of two prefix presentations of the same triple. Such presentations have the same lag and can always be aligned by extending the shorter one. Hence (13) descends at every point. Aligning the middle prefixes of composable arrows cancels their middle density, proving additivity; inverse arrows negate \(c\). No almost-everywhere descent is substituted for this all-point identity.

Writing \(\lambda(z,k,y)=k\), the full kernels and their intersection are exactly
\[
\begin{aligned}
\ker\lambda&=\{(u\xi,|u|-|v|,v\xi):\xi\in D_{u,v},\ |u|=|v|\},\\
\ker c&=\{(u\xi,|u|-|v|,v\xi):\xi\in D_{u,v},\ Q_u(\xi)=Q_v(\xi)\},\\
\ker\lambda\cap\ker c&=\{(u\xi,0,v\xi):\xi\in D_{u,v},\
|u|=|v|,\ Q_u(\xi)=Q_v(\xi)\}.
\end{aligned}\tag{14}
\]
Here (10) and (11) explicitly supply every equality test, including all infinite tails and empty prefixes; these are full sets, not just isotropy kernels or finite samples. Different presentations are identified as in (12), not counted as extra arrows. Kernel equality for one boundary version is not silently transferred to another.

## 5. Entire isotropy, incoming histories, and physical phases

Retain every object of \(X\times\mathbb R\) and every arrow
\[
(y,h)\longrightarrow(z,h+c(g)),\qquad g=(z,k,y).
\tag{15}
\]
Height translation commutes with these arrows and acts on their orbit set. No manifold quotient or invariant physical-flow measure is claimed. All incoming arrows at a target \((z,s)\) are enumerated by
\[
m,n\ge0,\quad v\in B^n,\quad y=vT^mz\in X,\quad
g=(z,m-n,y),\quad\text{source height }s-c(g).
\tag{16}
\]
Only equal actual triples are identified. Every legal finite incoming history, every null source object, and every real height is retained.

Source isotropy is trivial precisely at noneventually-periodic histories. At an eventually periodic history with least visible tail period \(d\), it is \(d\mathbb Z\): an equality \(T^mx=T^nx\) with nonzero lag is exactly eventual periodicity, and periods of the eventual tail are multiples of its least period. The clock image \(H_x=c(G_x^x)\) is determined below from the entire generator, not from a selected symbolic return.

For MAIN and SWITCH, a marker-free periodic tail is impossible: any letter repeated one period later would have gcd with itself greater than one, with no separating unit. The same conclusion for SINGLE follows directly from its ban on adjacent nonunits. Thus eventually-marker-free histories have trivial source isotropy and \(H_x=\{0\}\), regardless of their finite prefix or the chosen boundary version. They remain present with all incoming arrows (16). OFF's marker-free periodic histories are retained and classified in Section 7 instead.

Every MAIN, SWITCH, or SINGLE periodic orbit can be cut at its visible units into a cyclic sequence \(\mathcal B=(w_0,\ldots,w_{r-1})\) of its legal blocks. A primitive block necklace means this sequence is not a power, modulo cyclic rotation. Its least visible period and clock generator are
\[
d_{\mathcal B}=\sum_{i=0}^{r-1}(|w_i|+1),\qquad
\mathcal T_{\mathcal B}=-\log\prod_{i=0}^{r-1}p(w_i)>0.
\tag{17}
\]
To prove the least-period assertion, a visible period must take unit positions to unit positions; it therefore induces a rotation fixing the block sequence. A strictly shorter visible period would make that sequence a proper power. Conversely a block repetition gives exactly the corresponding visible repetition. Rotating the visible starting point inside a block does not give another necklace.

For the clock formula, start at a unit of the pure periodic tail and apply (10) with \(v=\varnothing\) to one entire visible period. Its prefix density is exactly \(\prod_i p(w_i)\); all intermediate \(F\)'s cancel. If the source history has a preperiod of length \(N\), then \(c(x,d_{\mathcal B},x)=A_{N+d_{\mathcal B}}(x)-A_N(x)=\mathcal T_{\mathcal B}\); the preperiod cancels. Since each block probability is at most \(1/2\), the generator is strictly positive. Therefore the whole source isotropy maps as \(kd_{\mathcal B}\mapsto k\mathcal T_{\mathcal B}\), and
\[
H_x=\mathcal T_{\mathcal B}\mathbb Z.
\tag{18}
\]
The fixed-object isotropy of the real extension is consequently trivial: it is the clock-zero part of source isotropy. Source isotropy itself has not been deleted; its nontrivial arrows change height. The stabilizer of height translation on an extension orbit-set point is exactly \(H_x\).

All histories eventually following one periodic block necklace lie in one source orbit; tail equality between periodic words forces the same necklace. Distinct necklaces, including those with equal numerical time, are distinct primitive packets. Their full phases are \(\mathbb R/\mathcal T_{\mathcal B}\mathbb Z\), as sets. More generally the phases over any source orbit are \(\mathbb R/H_x\): transport height to any reference source point by an actual arrow; two such transports differ by exactly source isotropy. Choosing that coordinate deletes no objects and imposes no quotient-topology claim. A repeated block word multiplies time by its repetition count and creates no new primitive packet.

## 6. MAIN's full block ledger and the precommitted packets

For every legal nonunit block \(w\) of length \(n\), its single-block contribution is
\[
-\log p(w)=(n+1)\log2+\log Z_n+\sum_{i=1}^{n}\log(w_i(w_i-1)).
\tag{19}
\]
Summing (19) along every primitive block necklace gives the entire ledger (17), including empty blocks and all mixtures. It is not restricted to a table or to prime-labelled blocks. Since \(Z_1=1\),
\[
p(\varnothing)=\tfrac12,\qquad p((a))=\frac1{4a(a-1)},\qquad
p((2))=\tfrac18,\quad p((3))=\tfrac1{24}.
\]
The three prescribed full packets therefore have:

| Visible periodic history | Primitive block necklace | Least source lag | Entire physical stabilizer |
| --- | --- | --- | --- |
| \(1^\infty\) | \((\varnothing)\) | \(1\) | \((\log2)\mathbb Z\) |
| \((12)^\infty\) | \(((2))\) | \(2\) | \((\log8)\mathbb Z\) |
| \((1213)^\infty\) | \(((2),(3))\) | \(4\) | \((\log192)\mathbb Z\) |

The second packet is primitive: it is a one-block necklace and (18) excludes any smaller positive time in its orbit. It is not the third repetition of the separate \(1^\infty\) packet. Likewise the mixed block necklace \(((2),(3))\) is primitive, since its two blocks differ. Every single-letter nonunit block gives primitive time \(\log(4a(a-1))\), not a prime logarithm.

The within-segment rule is genuinely unbounded in visible-window length: for any window bound \(L\), periodically repeat a pairwise-coprime word of length larger than \(L\) without units. Every length-\(L\) window is a legal finite segment and extends to \(X\) by a unit and then units forever, but the whole repeated sequence violates the rule. This rules out a fixed-window description of \(X\); it does not prove escape from countable-state coding or from free block concatenation.

In fact every finite cyclic concatenation of legal unit-blocks is allowed. The probability construction uses independent blocks, and the clock products telescope exactly to their block probabilities. This is the free block-splicing risk in an explicit owner. We claim no contradiction to the older countable-Markov obstruction and no inherited positive credit from a nonlocal source description.

## 7. Three controls with their own complete ledgers

**ARITHMETIC-OFF.** Its own formulas give \(F(v)=2^{-|v|}\prod_i\rho(v_i)\): sum over each possible left-extension length in (3), using \(\sum_a\rho(a)=1\). Thus on finite-marker tails \(q_1=1/2\) and \(q_a=\rho(a)/2\). On its marker-free tails every \(a\ge2\) is legal, so \(R=1\) and (6) gives these same values. Its measure is the product law with weights \(b_1=1/2,b_a=\rho(a)/2\), as the history IMAGE identities determine all cylinder probabilities. This is derived for OFF, not borrowed from MAIN.

For every visible finite word \(u\), let \(D(u)=2^{|u|}\prod_{u_i\ge2}u_i(u_i-1)\), counting occurrences. Then \(Q_u=1/D(u)\) on the full source. Its clock kernel is exactly \(D(u)=D(v)\), its lag kernel is \(|u|=|v|\), and their intersection requires both. These can differ: \(D((2))=D((1,1))=4\) although the lengths differ. All incoming arrows and phases are (16) and the source-orbit construction above.

OFF's periodic packets are **all** primitive visible necklaces, whether or not they contain a unit. For a word \(u\) of least visible period \(d=|u|\), the source isotropy is \(d\mathbb Z\), \(c(kd)=k\log D(u)\), \(H=(\log D(u))\mathbb Z\), and extension isotropy is trivial. Nonperiodic-tail classes have trivial source isotropy and \(H=0\). This follows by multiplying the constant conditional weights around the period; every \(b_a<1\). Repetitions and phases follow exactly as in Section 5. The three prescribed marked packets have times \(\log2,\log8,\log192\), while the additional primitive \(2^\infty\) has time \(\log4\). No unmarked packet is silently discarded.

**SINGLE-LETTER-BLOCK.** Here \(F(\varnothing)=1\), \(F((a))=p((a))=\rho(a)/2\). At a tail starting with 1, \(q_1=1/2,q_a=\rho(a)/2\); at a tail starting with a nonunit \(a\), the only legal predecessor is 1 and \(q_1=1\). Its own stationarization has \(M=3/2\), with full support and no atoms as proved from its own block law. Formula (10) is its complete history density and (14) its full kernels. There is no marker-free case to complete.

All SINGLE periodic packets are primitive necklaces over \(\{\varnothing\}\cup A\), with (17)–(18), all incoming arrows (16), trivial extension isotropy, and the full phases stated above. The block times are \(\log2\) for \(\varnothing\) and \(\log(2a(a-1))\) for \((a)\). Thus its three marked test packets have times \(\log2,\log4,\log48\). The zero one-step clock when prefixing the sole legal unit before a nonunit is retained; it is not a zero full-period clock and does not add extension isotropy.

**BOUNDARY-SWITCH.** This control uses the unchanged MAIN probability but its own version (6) with \(\beta=2\). Equations (7) and (8) prove both its every-Borel ownership and its actual difference on the prescribed full arithmetic tail. Equations (10), (11), and (14), with this value of \(\beta\), give its entire history clock and all kernels. All incoming arrows still have (16), with the control's own \(c\).

Its source is exactly MAIN's, so all periodic tails have infinitely many units; all finite-history terms used in their return generator are governed by the unchanged finite-marker formulas. Thus its entire primitive ledger, \(H\), and extension isotropy agree with (17)–(18), not merely with the three test times. Marker-free and eventually-marker-free source histories remain aperiodic with \(H=0\), while their inter-object clocks may differ as in (8). This proves a specific boundary-version nonuniqueness without transferring a clock to MAIN or making a post-failure repair.

## 8. Gate assessment, limitations, and decision

| Obligation | Same-owner evidence | Boundary |
| --- | --- | --- |
| T0 / IMAGE | Explicit probability; every actual predecessor; every-Borel history IMAGE; full retained-lag real extension | Standard Borel owner, not an assumed étale, symplectic, or manifold flow |
| T1 arithmetic / clock | Hard divisor exclusion acts on complete unfinished segments; full Borel clock proved | Block weights and null completion are declared data; no canonical/continuous boundary claim |
| T2 ledger / target | All primitive packets, full stabilizers, repetitions, incoming histories and phases classified | Prime-time target FAILS at the primitive \((12)^\infty\) packet |
| T3 / formal / B | NOT AUDITED / UNASSIGNED / NOT INVOKED | No operator, determinant, roof substitution, or Route transfer |

**Decision: STOP / FORK.** MAIN owns a complete hard-source Borel clock, but the full \(\log8\) primitive packet already violates the fixed target. The positive unit packet is insufficient. The entire source and measure remain unchanged; no illegal within-segment extension, null tail, repeated block, or mixed necklace is deleted. Prime coverage and further arithmetic coincidences among higher block times need not be classified to decide this gate. This is not a universal no-go for hard long-memory sources, other measures, or other geometries.

## 9. Reproducibility, provenance, and disclosure

The [candidate card](candidate-card.md) fixes the object before mathematics. The [claim ledger](claim-ledger.md) and separately assigned [review record](evidence/review.md) are root-owned integration artifacts, not assumed completed by this proof. All evidence here is exact derivation: finite-word sums are nonnegative convergent series, not numerical truncations; all source and kernel descriptions quantify over their entire domains. No external literature, scientific computation, fitted prime data, or novelty claim is used.

The source scout supplied the hard unit-delimited carrier and length-biased measure without results. Root changed the branch law and the third control before freezing this candidate. Prior scouting read 370 summary lines 1–91, original 370 card lines 1–100, and 065 card lines 1–11, including the disclosed historical-status exposure. The author previously worked on 367 and 371. For this proof it read the full 376 original card lines 1–88 and the paper template after CP1 release, but no independent raw proof or peer manuscript. Shared-history internal work is NOT_CALIBRATED; source authorship is not independent review.

Data availability: the frozen definitions and complete derivations are in this Markdown package; no empirical dataset was collected. Author contributions: this AI-assisted source author independently derived and wrote the main proof; root owns the amended freeze, integration, and separate review assignments. Ethics: no human subjects or private data. Funding and conflicts have not been supplied and are not inferred. ARS writing discipline was used for claim/definition and null-version boundaries, not as evidence of mathematical validity or publication readiness.
