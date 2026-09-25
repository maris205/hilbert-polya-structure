# Quotient-length replication has nonprime fixed-packet clocks

Candidate ID: ANG-20260925-DQR01.
Outcome: OWNED MARKOV CLOCK; NONPRIME FIXED PACKETS — STOP / FORK
Paper481; batch PRE-P0-STRUCTURE-20260925-AA, round2/5; 2026-09-25.
Type: ANG partial measured-history owner. Exact symbolic proof; no numerical census.
Classical symplectic suspension: NOT APPLICABLE. Formal Route coordinates:
UNASSIGNED; Route B NOT INVOKED. T3 NOT AUDITED. Same-model NOT_CALIBRATED.

## Abstract

The frozen divisor-quotient substitution owns an original Markov probability,
an everywhere specified inverse IMAGE density and a signed real cocycle.
Its complete fixed set is \(f_d=(d,(d^2)^\infty)\), \(d\ge2\).
Writing \(\delta_d=d^2-d-1\), every such source packet has positive physical
primitive \(\delta_d\log[(2^{2d^2}-2^{d^2}+1)/(2^{d^2}-1)]\).
The exponent is a reduced noninteger rational, not an ordinary prime.
This is a fixed-packet counterexample to prime-only purity, not an inference
from an empty window. The iid, replication-OFF and combined arithmetic-OFF
controls are separately owned and completely classified at period one.
Full incoming recursion, all actual lags, kernels, entire displacement groups
and real phases are retained; no higher-period census is undertaken.

## 1. Frozen owner, question and lineage

The scientific input is the [version1.1 card](candidate-card.md), all 96 lines,
SHA256 \(18404bee3127748731a39fa6b54c0ccd69ccaa3ae28bdff1db97e2901cee234e\).
Its first 86 lines remain the original scientific prefix. The question is
whether the actual positive physical primitives equal \(\log p\), without
rescaling or merging packets, for ordinary integer primes \(p\).
Nonemptiness, prime-only purity, uniqueness and full-prime coverage are separate.

| Item | This owner and scope |
| --- | --- |
| Carrier | Full \(X=\mathbb N_{\ge1}^{\mathbb N_0}\), product Borel space |
| Arithmetic input | \(D(a,b)\iff1<a<b,\ a\mid b\) |
| Evolution | Actual partial prefix substitution, independently defined controls |
| Original reference law | Markov \(\mu\) for M/R, iid \(\mu_0\) for I/A |
| Clock | Own inverse IMAGE, signed; fixed null-point version retained |
| Packets | Actual source groupoid orbits with full isotropy image |
| Classical / analytic owners | No symplectic form, positive roof, operator or determinant assigned |

The lineage is proper-divisor symbols \(\to\) legal source pairs \(\to\)
quotient-selected block length and divisor-selected replication \(\to\)
changed arithmetic input at the next step. This is a symbolic deformation,
not a claimed Logistic/Hénon or conservative geometric lift.

## 2. Probability, maps and complete inverses

Put \(\eta(a)=2^{-a}\), and define the original transition law by
\[
 Z_a=\sum_{b\ge1}2^{-b}(1+\mathbf1_{D(a,b)}),\qquad
 P_{ab}=\frac{2^{-b}(1+\mathbf1_{D(a,b)})}{Z_a},\qquad
 \mu[a_0,\ldots,a_k]=\eta(a_0)\prod_{i<k}P_{a_i a_{i+1}}.                 \tag{1}
\]
The geometric sum gives \(\sum_a\eta(a)=1\), \(1\le Z_a\le2\);
every transition is positive and its row sums to one. The consistent cylinder
probabilities define a probability: equivalently use independent uniform
variables and the inverse cumulative distributions of \(\eta\) and each row.
Every cylinder has positive mass. Also \(P_{ab}\le1/2\): for \(b=1\) its
numerator is \(1/2\), and for \(b\ge2\) it is at most \(2^{1-b}\le1/2\).
Thus length-\(k\) cylinders have mass at most \(2^{-k}\), proving nonatomicity.
The iid law \(\mu_0=\eta^{\mathbb N_0}\) has the same support and atom bound.
Stationarity is neither used nor asserted.

For M/I/R a legal source has first pair \((d,n)\) satisfying \(D\);
write \(q=n/d\ge2\), \(B=(b_1,\ldots,b_q)\) and \(x=(d,n,B,\xi)\).
The rest of the word is untouched at that step:

| Owner | Law | Output |
| --- | --- | --- |
| M MAIN | \(\mu\) | \((q,B^d,\xi)\) |
| I Markov arithmetic-OFF | \(\mu_0\) | \((q,B^d,\xi)\) |
| R replication-OFF | \(\mu\) | \((q,B,\xi)\) |
| A combined divisor arithmetic-OFF | \(\mu_0\) | \((n,B^d,\xi)\), all \(d,n\ge1\), here \(\lvert B\rvert=n\) |

M/I/R retain every illegal first pair as a terminal object, not an absorbing
loop. A is total, including all units; it is a combined, not single-factor,
ablation. All owners retain every infinite and null word. There are no
finite-word objects or infinite letters.

For every actual source prefix \(U\), let \(V\) be its output prefix.
The source cylinders \([U]\) partition the legal domain: the first pair
determines the read length, and the actual letters determine \(B\).
The branch is a Borel bijection \([U]\to[V]\) with inverse
\[
 I_U:[V]\longrightarrow[U],\qquad I_U(V\xi)=U\xi.                     \tag{2}
\]
For M/I enumerate all \(d,q\ge2\), and accept a target beginning with \(q\)
whose next \(dq\) letters are \(d\) copies of its next \(q\)-block \(B\).
The inverse is \((d,dq,B,\xi)\). For R, every target \(y=(q,\zeta)\) with
\(q\ge2\) has precisely the predecessors \((d,dq,\zeta)\), \(d\ge2\);
the card's \(B\) is the first \(q\) letters of \(\zeta\).
No M/I/R target beginning with \(1\) has a predecessor.
For A, take \(n=y_0\), its next \(n\)-block \(B\), and enumerate all \(d\ge1\)
for which \(y=(n,B^d,\xi)\); recover \((d,n,B,\xi)\).
These tests are necessary and sufficient by substitution, proving both inverse
identities and exhaustiveness. No outgoing test is imposed on the target.
For example \((2,1^\infty)\) is M-terminal but receives
\((2,4,1^\infty)\). Equal actual predecessors are counted once.

## 3. Every-Borel IMAGE and all-point signed clocks

For a nonempty finite word \(W\) and tail beginning with \(t\), set
\[
 F_\mu(W,t)=\eta(W_0)\prod_{i<|W|-1}P_{W_iW_{i+1}}P_{W_{\rm last},t},
 \qquad F_0(W,t)=\prod_{w\in W}\eta(w).
\]
The prescribed version is positive and finite at every point:
\[
 J_U(V\xi)=F(U,\xi_0)/F(V,\xi_0),\qquad
 \nu(I_UE)=\int_EJ_U\,d\nu\quad(E\subset[V]\text{ Borel}).             \tag{3}
\]
Here \(\nu\) is the owner's original law. For a tail cylinder
\([t_0,\ldots,t_m]\), the two measures contain respectively \(F(U,t_0)\)
and \(F(V,t_0)\), with exactly the same subsequent transition product.
This proves (3) on cylinders; the monotone-class argument proves it on every
Borel set. The iid proof is the same cylinder calculation without transitions.
Thus the prescribed everywhere-defined formula is a valid IMAGE version;
the identity does not assert uniqueness of its values on null points.

Let \(s(B)=\sum_i b_i\), and for Markov owners define
\[
 \alpha(d,q,b_1)=\frac{\eta(d)P_{d,dq}P_{dq,b_1}}{\eta(q)P_{q,b_1}},
 \qquad C(B)=P_{b_q,b_1}\prod_{i<q}P_{b_i,b_{i+1}}.
\]
For M/R both words in (2) end in \(b_q\), so their final seam factors cancel.
The exact all-point clock \(\kappa(x)=-\log J_U(Tx)\) is
\[
\begin{array}{c|c|c}
 &J_U&\kappa\\ \hline
 M&\alpha/C(B)^{d-1}&-\log\alpha+(d-1)\log C(B)\\
 R&\alpha&-\log\alpha\\
 I&2^{-\{d-(d-1)(s(B)-q)\}}&
       [d-(d-1)(s(B)-q)]\log2\\
 A&2^{-\{d-(d-1)s(B)\}}&[d-(d-1)s(B)]\log2 .
\end{array}                                                        \tag{4}
\]
These formulas include signs and zeros, not an absolute-value roof.
M has zero exactly when \(\alpha=C(B)^{d-1}\), R when \(\alpha=1\).
I has zero exactly when \(d=2,\ s(B)=q+2\); A exactly when \(d=2,\ s(B)=2\).
Indeed the iid zero equations require \(d-1\mid d\), hence \(d=2\);
for A the case \(d=1\) always has clock \(\log2\).

## 4. Complete global fixed sets and their clocks

**M and I.** A fixed point has \(d=q\), \(n=d^2=:a\), \(d\ge2\).
After cancelling the first symbol, the complete word equation is
\[
       aB\xi=B^d\xi,\qquad |B|=d.                                  \tag{5}
\]
Comparison of its first \(d\) symbols gives \(b_1=a\) and
\(b_i=b_{i-1}\) for \(2\le i\le d\); thus \(B=a^d\).
The remaining equation is \(a^{d+1}\xi=a^{d^2}\xi\).
Since \(\delta_d=d^2-d-1>0\), cancellation gives \(\xi=a^{\delta_d}\xi\),
forcing every tail symbol to be \(a\). Conversely \(f_d=(d,a^\infty)\)
satisfies the legal branch and (5). Therefore both complete fixed sets are
\(\{f_d:d\ge2\}\), with no unexamined tail or branch.

**R.** The first-symbol argument again gives \(d=q,n=d^2=a\).
Writing \(\zeta=B\xi\), the remaining equation is \(a\zeta=\zeta\).
It forces \(\zeta=a^\infty\), and the converse is direct. R has exactly
the same fixed set, under its own law and clock.

**A.** A fixed point first requires \(d=n=k\). For \(k\ge2\), the equation
is \(kB\xi=B^k\xi\), \(|B|=k\). The preceding symbol comparison, with
\(a=k\), forces \(B=k^k\) and \(\xi=k^\infty\).
For \(k=1\), writing \(B=(b)\), the equation \(1b\xi=b\xi\) forces
\(b=1\) and then \(\xi=1^\infty\).
Thus \(\operatorname{Fix}(T_A)=\{g_k=k^\infty:k\ge1\}\) globally.

For \(a\ge2\), the legal multiples in the row normalization are \(2a,3a,\ldots\);
hence, putting \(m=2^a\),
\[
 Z_a=1+\frac{2^{-2a}}{1-2^{-a}}
     =\frac{m^2-m+1}{m(m-1)},\qquad
 p_a:=P_{aa}=\frac{m-1}{m^2-m+1},\quad
 Q_a:=p_a^{-1}=m+\frac1{m-1}.                                      \tag{6}
\]
At \(f_d\), \(\alpha=p_{d^2}\) and \(C(B)=p_{d^2}^{\,d}\).
Applying (4), with no rescaling, gives the complete fixed-clock ledger:

| Owner/core | Signed fixed clock \(\lambda=\kappa(\text{core})\) | Positive generator \(L\) of entire \(H\) |
| --- | --- | --- |
| M, \(f_d\), \(d\ge2\) | \(-\delta_d\log Q_{d^2}\) | \(\delta_d\log Q_{d^2}\) |
| I, \(f_d\), \(d\ge2\) | \(-d^2\delta_d\log2\) | \(d^2\delta_d\log2\) |
| R, \(f_d\), \(d\ge2\) | \(\log Q_{d^2}\) | \(\log Q_{d^2}\) |
| A, \(g_1\) | \(\log2\) | \(\log2\) |
| A, \(g_k\), \(k\ge2\) | \(-k\delta_k\log2\) | \(k\delta_k\log2\) |

Every listed clock is nonzero. Section 5 proves that the positive primitive
is \(|\lambda|\), not that a negative signed clock removes the packet.
The numerator and denominator of \(Q_a=(m^2-m+1)/(m-1)\) are coprime:
the numerator is \(1\) modulo \(m-1\). For \(a\ge2\) its denominator exceeds
one, and the same remains true of every positive integer power.
Consequently every M and R fixed primitive has noninteger rational exponent.
In particular M at \(f_2=(2,4^\infty)\) has \(L=\log(241/15)\).
All I exponents are composite powers of two. A has one prime-valued fixed
packet, \(g_1\) at \(\log2\), and composite exponents for every \(k\ge2\).

Each parameter labels a distinct actual source packet: two different fixed
points cannot acquire a common forward image. The fixed times are also
distinct within each owner. Indeed \(Q_a\) increases strictly with \(a\):
\(Q(m')-Q(m)=(m'-m)[1-1/((m'-1)(m-1))]>0\) for \(m'>m\ge4\).
Combine this with increasing positive \(\delta_d,d^2\delta_d,k\delta_k\);
for A, the first two time coefficients are \(1,2\).
This preserves multiplicity without identifying equal-time source packets.

## 5. Actual histories, entire isotropy and all phases

For each owner let \(D_r\) be its legal \(r\)-step domain,
\(S_r(z)=\sum_{j<r}\kappa(T^jz)\), \(D_0=X,S_0=0\). Use precisely
\[
 G=\{(z,r-s,w):z\in D_r,\ w\in D_s,\ T^rz=T^sw\},\qquad
 c(z,r-s,w)=S_r(z)-S_s(w).                                         \tag{7}
\]
Equal triples, not witnesses, are the arrows; source is \(w\), range is \(z\).
If two witnesses have the same lag, their indices differ by a common integer.
Extending the shorter witness adds the identical legal tail sum on both
sides, so \(c\) is well-defined at every point. The same cancellation after
matching middle iterates proves additivity; inverse changes the sign.
In particular \((Tz,-1,z)\) has clock \(-\kappa(z)\).

On any history chart the inverse \(r\)-step IMAGE is \(e^{-S_r(z)}\),
by composing (3). Every finite history has such a chart after restricting
to its finite sequence of actual branches. A pair chart carrying \(w\) to
\(z\) has IMAGE \(e^{-S_r(z)}/e^{-S_s(w)}=e^{-c}\), on every Borel subset.
There are countably many charts; this is a branchwise formula, not an
incorrect sum over multiple presentations of one arrow.
The exact lag, clock and joint kernels are respectively
\[
 \ker\ell=\{(z,0,w):T^rz=T^rw\text{ legally for some }r\},\quad
 \ker c=\{g:S_r(z)=S_s(w)\},\quad
 \ker(\ell,c)=\ker\ell\cap\ker c.                                  \tag{8}
\]

For any \(x\), nontrivial source isotropy exists iff its actual forward
trajectory eventually enters a finite legal cycle. A loop with unequal
indices makes the common image periodic; conversely a cycle supplies loops.
If its least period is \(e\), source isotropy is exactly \(e\mathbb Z\):
after entry, equality of iterates holds exactly at differences divisible
by \(e\). Let \(\Lambda\) be the sum of \(\kappa\) once around that cycle.
Tail cancellation gives \(c(x,je,x)=j\Lambda\), for every integer \(j\).
Without such a cycle, including every terminal trajectory, isotropy is zero.

The real extension has objects \(X\times\mathbb R\) and arrows
\((w,h)\mapsto(z,h+c)\). Its isotropy consists of the source loops with
\(j\Lambda=0\): it is trivial if \(\Lambda\ne0\), and all \(e\mathbb Z\)
if \(\Lambda=0\). Height translation stabilizes an orbit exactly when a loop
over its base point realizes that translation. Therefore its ENTIRE stabilizer
is \(H=\Lambda\mathbb Z\), or \(\{0\}\) for non-eventual trajectories.
If \(\Lambda\ne0\), the positive physical primitive is \(|\Lambda|\);
if \(\Lambda=0\), there is no positive generator. This does not insert a roof.

To display every phase on an eventual-cycle class, fix one actual cycle point
\(p\), let \(\tau(z)\) be first entry to that point and \(A(z)=S_{\tau(z)}(z)\).
All arrows between two objects in its basin have, exactly,
\[
 k=\tau(z)-\tau(w)+je,\qquad
 c=A(z)-A(w)+j\Lambda,\qquad j\in\mathbb Z.                          \tag{9}
\]
Any \(j\) is realized by taking enough complete turns on both sides.
Their real phases are \(h-A(z)\pmod{\Lambda\mathbb Z}\), with all real
representatives retained. When \(\Lambda=0\), phases are real numbers.
For any other source class choose a base point and one arrow from it to each object;
all such arrows have the same clock because isotropy is zero. Subtracting
that clock gives its full real phase parameter. No regular orbit quotient
or topology on the phase set is presumed.

## 6. Whole fixed-core incoming, not selected forward pieces

For \(O\in\{M,I,R,A\}\), let \(\mathcal P_O(y)\) be the complete
predecessor set in Section 2, using that owner's actual action.
For each of its fixed cores \(p\), define
\[
 E_0(p)=\{p\},\qquad E_{r+1}(p)=\bigcup_{y\in E_r(p)}\mathcal P_O(y),
 \qquad \mathcal B_p=\bigcup_{r\ge0}E_r(p).                         \tag{10}
\]
This is an exact all-label, all-depth description of the WHOLE source orbit
of \(p\). Induction gives \(E_r(p)=\{z:T^rz=p\text{ legally}\}\);
an arrow from or to a fixed point forces that equality at some finite time.
Repeated appearances of \(p\) add no objects or packet labels.
As checks on the complete seed sets,
\[
 \mathcal P_{M,I,R}(f_a)=\{(d,da,(a^2)^\infty):d\ge2\},\quad a\ge2;
 \qquad
 \mathcal P_A(g_k)=\{(d,k^\infty):d\ge1\},\quad k\ge1.               \tag{11}
\]
Further stages use the full tests of Section 2, not an unrestricted
eventually-constant-tail superset. Countable branching makes these basins
countable, hence null, but (3) assigns all their clock values.

On \(\mathcal B_p\), take \(\tau\) as the least entry time and
\(b(z)=S_{\tau(z)}(z)-\tau(z)\lambda\).
The ENTIRE restricted groupoid and cocycle reduce to
\[
 G|_{\mathcal B_p}=\mathcal B_p\times\mathbb Z\times\mathcal B_p,\qquad
 c(z,k,w)=b(z)-b(w)+k\lambda.                                      \tag{12}
\]
Thus the lag kernel is \(k=0\); the clock kernel is
\(b(z)-b(w)+k\lambda=0\); their intersection imposes both.
Source isotropy is \(\mathbb Z\), entire \(H=\lambda\mathbb Z\),
extension isotropy is trivial, and all phases are
\(h-b(z)\pmod{\lambda\mathbb Z}\). All repetitions are \(j\lambda\),
including their actual lag \(j\), not labels discarded after taking a clock.
Positive physical repetitions are \(m|\lambda|\), \(m\ge1\).

Zero steps do not enlarge this \(H\). For example the A zero branch
\((2,1,2^\infty)\to(1,2^\infty)\) subsequently reaches \(g_2\);
the next step has clock \(\log2\), while the entire packet still has
\(H=2\log2\,\mathbb Z\). Taking a gcd of unrelated incoming step clocks
would therefore be incorrect.
For an arbitrary target, the same recursion as (10) enumerates all finite
predecessors. Infinite incoming histories are exactly compatible chains
\(z_0=y,\ z_{j+1}\in\mathcal P_O(z_j)\) for every \(j\).
This is an untruncated inverse-limit condition; arbitrarily deep finite
branches alone do not assert that a compatible infinite chain exists.

## 7. Gate, limitations and reproducibility

M owns its source, inverse atlas, measure version and full history cocycle.
Its positive fixed-packet ledger is nonempty and violates prime-only purity.
The single actual packet \(f_2\) already decides STOP / FORK under the card.
No conclusion about higher-cycle prime uniqueness or all-prime coverage is
needed or claimed. R shows that replication is not necessary for the
noninteger fixed-clock obstruction; I gives composite integer exponents;
A produces \(\log2\) without the divisor mechanism and also composite packets.
These are separately proved controls, not transferred MAIN results.
Strong arithmetic naturalness stays OPEN; T1 is NOT PASSED, the fixed T2 gate
fails, T3 is NOT AUDITED, and no formal Route coordinate was evaluated.

All scientific claims above use exact cylinder and finite-word arguments
from this card; no scientific code, numerical truncation, external source,
old proof, current scope/raw/review or independent-reviewer answer was read.
Records: [card](candidate-card.md), [claim ledger](claim-ledger.md),
[package README](README.md). Root owns evidence integration; no future review
completion or external verification is certified by these author files.

Design exposure is inherited, not blind: 325/474 definitions, 471/475
authorship, and informal word-overlap feasibility consideration before freeze.
Scout reads were 476card lines1–68/125, prefix SHA256
\(c3888a18651eb1ea655a3c7162394fad7291f79adb3143a38f5ad832e4cf59d3\),
and 479card lines1–65/122, prefix SHA256
\(cc7667b052c6e68d1b453eb40764647b391aef32718d507659a44b6d92bfa1ed\);
neither read included Outcome/proof. These bound collision checks, not novelty.
ARS drafting guidance informed scope separation, limitations and disclosure.
AI assistance: AI agents supplied mathematical derivation, drafting and
internal author checking. Author helper
\(\texttt{/root/bilateral\_transport\_review/direct\_controls}\) read this
96-line card only as scientific input for its disjoint A-control fixed,
clock and incoming calculation; the main author checked and integrated it.
That helper is not an independent reviewer. Same-model/shared-history work
is NOT_CALIBRATED; no human or external mathematical verification is certified.

Data availability: all mathematical inputs and proofs are in this package;
there are no experimental data. Ethics: no human subjects or private data.
Contributions: author lane performed formal analysis, writing and self-check;
the disclosed helper supplied bounded A-control author assistance; root owns
contract and integration. Funding and human conflicts were not supplied;
none is inferred. No novelty, publication-readiness or RH claim is made.
The author handoff stops here; any different map, law or gate needs new authority.
