# Proper-divisor tail admission excludes every prime-valued primitive

Candidate ID: ANG-20260925-DTA01.
Outcome: OWNED TAIL CLOCK; NONEMPTY PRIME-ONLY TARGET IMPOSSIBLE — STOP / FORK
Paper475; clarified card version1.1; environment date2026-09-25.
Batch PRE-P0-STRUCTURE-20260925-Z, round1/5; exact analytic owner-level result.

## Abstract

The source is the full countable-alphabet one-sided sequence space with its
original product probability. MAIN permits a shift precisely when the leading
symbol is a proper divisor of the product of its next two symbols minus one.
Its inverse-prefix IMAGE law holds for every Borel set with the frozen
pointwise version, including all periodic null tails. Any actual least-period
word has primitive multiplier equal to the product of its letter factors
\(a(a-1)\). A prime multiplier is possible only for the constant word two,
which MAIN does not admit. Thus the combined nonempty, prime-only target is
impossible. This does not prove that MAIN has a nonprime periodic witness,
or that its positive ledger is empty. The three controls admit every constant
word; their full packets, kernels, entire clock groups and phases are computed.
No other periodic window or longer-word search is used.

## 1. Same frozen source, four separately owned permissions

Let \(B=\{2,3,\ldots\}\), \(X=B^{\mathbb N_0}\) with its discrete-product
topology and Borel structure, and
\[
 \rho(a)=\frac1{a(a-1)},\qquad \mu=\rho^{\mathbb N_0}.
\]
All infinite sequences are objects, including those whose next step is illegal.
For \(z=(a,b,c,\eta)\), put \(n=bc-1\). The four actual maps are the partial
left shift \(T_Uz=(b,c,\eta)\) on the following own domains:

| Owner \(U\) | Legal source predicate \(G_U(a,b,c)\) |
| --- | --- |
| M: MAIN | \(2\le a<bc-1\) and \(a\mid bc-1\) |
| A: permission-OFF | Every triple |
| I: divisibility-OFF | \(2\le a<bc-1\) |
| R: remainder-complement | \(2\le a<bc-1\) and \(a\nmid bc-1\) |

For M/I/R, \(a=bc-1\) is an illegal but retained source. A admits this
boundary and every other triple, as the card's version1.1 clarification states.
No terminal has an added absorbing loop, and no target-outgoing test is imposed.
The alphabet never included zero or one; no source is removed after the freeze.
Every next step rereads its own current triple.

The [card](candidate-card.md) fixes this entire tuple. Its lineage is the
current integer \(bc-1\), its proper-divisor witness \(a\), actual symbolic
permission, then the same partial shift's returns and original-measure clock.
The source is not conditioned on infinite survival. No prime predicate,
prime table, external integer register, selected roof or geometric conjugacy
is introduced. Classical geometry and a later operator owner are not supplied.

## 2. Probability and all-point, every-Borel inverse IMAGE

The finite sums telescope:
\(\sum_{a=2}^{N}\rho(a)=1-1/N\).
Thus \(\rho\) is a probability and its consistent product law defines \(\mu\).
Every finite cylinder has positive mass, so this law has full support.
Since \(\rho(a)\le1/2\), a singleton lies in cylinders of mass at most
\(2^{-r}\) for every \(r\); hence all singletons, including periodic tails,
have mass zero. They remain actual objects.

For every owner and every \(a\ge2\), define
\[
 E_a^U=\{y:G_U(a,y_0,y_1)\},\qquad
 \theta_a^U(y)=ay\quad(y\in E_a^U),\qquad j_a^U(y)=\rho(a).       \tag{1}
\]
These domains and their prefix images are Borel, since the test uses only
the first two target coordinates. The prefix map is a Borel isomorphism
onto its image. It satisfies \(T_U\theta_a^U y=y\);
conversely any actual predecessor of \(y\) has one first letter \(a\),
belongs to this domain and equals \(ay\). Thus (1) is the full inverse atlas.
Its source images are disjoint by first letter. For M/I/R the predecessor
letters are tested among \(2,\ldots,y_0y_1-2\); A retains all \(a\ge2\).

For an arbitrary Borel \(E\subset X\), the product-cylinder identity extends
by the monotone-class theorem to
\(\mu(aE)=\rho(a)\mu(E)\). In particular, for every Borel \(E\subset E_a^U\),
\[
 \mu(\theta_a^U E)=\int_E j_a^U\,d\mu=\rho(a)\mu(E).              \tag{2}
\]
This independently verifies each owner's restricted inverse and original
probability. There is no division by the total mass of legal letters.
The constant value in (1) is the frozen version at every point, not a value
inferred from a.e. uniqueness on the null periodic set.
Consequently, writing \(v(a)=a(a-1)\), the only step clock is
\[
 \kappa_U(z)=-\log j_{z_0}^U(T_Uz)=\log v(z_0)\ge\log2>0.       \tag{3}
\]
Every legal step has a finite positive clock. A terminal has no step clock;
its unit arrow, like every unit, has clock zero.

## 3. All legal histories and actual cocycle

For each \(U\), \(D_r^U\) consists exactly of the \(z\) satisfying
\(G_U(z_i,z_{i+1},z_{i+2})\) for every \(0\le i<r\); \(D_0^U=X\).
On this domain set
\[
 Q_r(z)=\prod_{i<r}v(z_i),\quad Q_0=1,\quad
 S_r(z)=\log Q_r(z),\qquad
 G_U=\{(z,r-s,w):T_U^rz=T_U^sw\text{ legally}\}.                \tag{4}
\]
The source of this triple is \(w\), its range is \(z\), its lag is \(r-s\),
and equal triples are identified. Define
\[
 c_U(z,r-s,w)=S_r(z)-S_s(w).                                   \tag{5}
\]
Two witnesses of the same triple differ by adding the same integer to
both depths. Passing to the larger witness appends the same legal tail,
whose clock cancels. This proves descent. To compose two arrows, extend
their middle histories to the larger middle depth; the common clocks
cancel and the lags add. The required extensions are legal because both
middle depths occur in actual histories. Inversion negates lag and clock.
The countable Borel witness relations, with a first-witness enumeration,
also show that \(G_U\) and \(c_U\) are Borel. The forward arrow
\((T_Uz,-1,z)\) has \(c_U=-\kappa_U(z)\).

For a finite prefix \(u=(u_0,\ldots,u_{r-1})\), let \(E_u^U\) be all
tails \(y\) for which every one of the first \(r\) triples in \(uy\) is
legal. The complete inverse word is \(y\mapsto uy\) on \(E_u^U\),
with every-point density \(\rho(u)=\prod_{i<r}\rho(u_i)\).
Repeated (2) proves its every-Borel IMAGE. For two actual prefixes \(u,v\)
of lengths \(r,s\) and a common tail domain, the map \(vy\mapsto uy\) has IMAGE
\[
 J_{uv}(vy)=\frac{\rho(u)}{\rho(v)}
          =\frac{Q_s(vy)}{Q_r(uy)}=e^{-c_U(uy,r-s,vy)}.         \tag{6}
\]
Indeed any Borel set in the prefix-\(v\) image pulls back to a Borel tail
set, on which both prefix identities apply. Formula (5) proves consistency
for alternative witnesses, including null tails.

On actual arrows only, the full kernels are exactly
\[
 \begin{split}
 \ker c_U&=\{(z,r-s,w):Q_r(z)=Q_s(w)\},\\
 \ker\ell&=\{(z,0,w):T_U^rz=T_U^rw\text{ for some legal }r\},\\
 \ker c_U\cap\ker\ell
   &=\{(z,0,w):T_U^rz=T_U^rw,\ Q_r(z)=Q_r(w)
                           \text{ for some legal }r\}.
 \end{split}                                                  \tag{7}
\]
These include every merging arrow. Positivity of single-step clocks does
not imply that the clock kernel consists only of units.

## 4. Entire incoming, isotropy and all real phases

Let \(\mathcal I_U(y)=\{ay:y\in E_a^U,\ a\ge2\}\).
The recursion \(\mathcal I_U^0(y)=\{y\}\),
\(\mathcal I_U^{r+1}(y)=\bigcup_{x\in\mathcal I_U^r(y)}\mathcal I_U(x)\)
is exactly all depth-\(r+1\) predecessors: removing or adding the first
legal prefix letter proves both directions by induction. Equivalently,
\(\mathcal I_U^r(y)=\{uy:|u|=r,\ y\in E_u^U\}\).
There is no length cutoff and no permission test at \(y\) itself.
The full source orbit is
\[
 [y]_{G_U}=\bigcup_{\substack{s\ge0\\y\in D_s^U}}
                       \ \bigcup_{r\ge0}\mathcal I_U^r(T_U^sy). \tag{8}
\]
Compatible infinite incoming histories are precisely left-infinite
extensions \((\ldots,a_{-2},a_{-1},y_0,y_1,\ldots)\) whose triples satisfy
\(G_U\) at every negative index. No nonnegative-index permission is
required merely to be an incoming history to \(y\). This retains histories
ending at terminals and does not infer infinite existence from finite depth.

A nonzero isotropy lag is a coincidence of two different iterates of
the same source and therefore produces an actual eventual periodic core.
If no such core exists, source isotropy is trivial and its entire
\(H_z=c_U(\operatorname{Iso}_{G_U}(z))\) is zero.
For an actual least-\(\ell\) core \(f_0,\ldots,f_{\ell-1}\), put
\[
 C_i=\sum_{j<i}\kappa_U(f_j),\qquad C=C_\ell>0.
\]
All coincidences on this cycle have exactly lags \(\ell\mathbb Z\).
Their clocks are exactly \(C\mathbb Z\), since traversal of the least
cycle realizes \(C\), and any coincidence traverses an integer number of
these cycles. Incoming tails cancel. Hence, on its entire source basin,
\[
 \operatorname{Iso}_{G_U}(z)=\ell\mathbb Z,\qquad H_z=C\mathbb Z. \tag{9}
\]
In particular this is the whole image, not a selected repeated subgroup.

Let \(\tau_z\) be first arrival at this core and \(\epsilon_z\) its arrival
index. Define \(d_z=\tau_z-\epsilon_z\),
\(B_z=S_{\tau_z}(z)-C_{\epsilon_z}\). All arrows between two basin points are
\[
 \ell(g)=d_z-d_w+j\ell,\qquad
 c_U(g)=B_z-B_w+jC,\qquad j\in\mathbb Z.                        \tag{10}
\]
Extending to sufficiently late common core meetings realizes every \(j\);
any earlier meeting extends to one of these and gives the converse.
For a terminal-ending class, let \(\tau_z\) be its termination depth and
\(e_z=T_U^{\tau_z}z\). Exactly the points with the same actual terminal
belong together, and all their arrows have
\(\ell(g)=\tau_z-\tau_w,\ c_U(g)=S_{\tau_z}(z)-S_{\tau_w}(w)\).
Infinite non-eventual classes retain precisely the cofinality test (4)/(8)
and kernels (7); no claim that all infinite histories become periodic is made.

On all \(X\times\mathbb R\), arrows act by
\((w,t)\mapsto(z,t+c_U(g))\). Height translation descends to the orbit set.
Choose a reference \(a\) in one source class and any connector \(a\to z\)
of clock \(B_z\). Its extension classes are exactly
\[
 t-B_z\pmod{H_a}.                                             \tag{11}
\]
Different connectors change \(B_z\) by an element of the entire \(H_a\).
This is a classwise set description, not a measurable global selector.
For (9) all phases \(\mathbb R/C\mathbb Z\) are retained and the translation
primitive is \(C\), with all integer repetitions. For \(H=0\) phases are real
and translation has no positive period.
Extension isotropy is the source isotropy in \(\ker c_U\).
It is trivial everywhere: a nontrivial periodic loop has a nonzero multiple
of \(C>0\), while a non-eventual source has no such loop.
Thus no nontrivial zero-clock isotropy is hidden or discarded.

## 5. Complete constant-word comparison, with full packets

A fixed source of a one-step left shift must be \(f_q=q^\infty\),
for an integer \(q\ge2\). Conversely such a source is fixed exactly when
its own triple \((q,q,q)\) is legal. Now
\[
 q^2-q-1=(q-2)(q+1)+1>0,\qquad q^2-1\equiv-1\pmod q.
\]
Therefore MAIN has no fixed source. A, I and R each admit every \(f_q\).
Their complete fixed-core clock is
\(\Lambda_q=\log[q(q-1)]>0\); source isotropy is \(\mathbb Z\),
the entire \(H\) is \(\Lambda_q\mathbb Z\), and extension isotropy is trivial.

For each of A/I/R its full incoming packet at \(f_q\) is exactly
\[
 \mathcal P_q^U=\{u q^\infty:u\in B^{<\infty},\
                    G_U(z_i,z_{i+1},z_{i+2})\ (0\le i<|u|)\},
 \quad z=uq^\infty.                                           \tag{12}
\]
All finite prefixes are allowed for A. For I, each displayed prefix triple
must satisfy \(2\le z_i<z_{i+1}z_{i+2}-1\); R additionally requires
nondivisibility. These tests include every existing triple across the
prefix/tail boundary, without any other-tail truncation.
This is the whole source class: a meeting with \(f_q\) is exactly eventual
arrival at \(f_q\), and (12) spells out all legal steps to that arrival.
Use the shortest such prefix to define \(\tau_z\) and
\(B_z=\sum_{i<\tau_z}\log v(z_i)\). Trailing copies of \(q\) in a
description do not create extra source points or packets.

For all \(z,w\in\mathcal P_q^U\), the complete arrows are
\[
 \ell(g)=\tau_z-\tau_w+j,\qquad
 c_U(g)=B_z-B_w+j\Lambda_q,\qquad j\in\mathbb Z.                \tag{13}
\]
Thus the lag kernel sets \(\tau_z-\tau_w+j=0\); the clock kernel sets
\(B_z-B_w+j\Lambda_q=0\); the joint kernel sets both.
All phases are \(t-B_z\pmod{\Lambda_q\mathbb Z}\).
Equation (1) iterated without a cutoff gives all incoming depths and the
compatible infinite histories of each packet. Different constants cannot
meet under shifts, so different \(q\)'s give different full packets.
The strictly increasing integers \(q(q-1)\) give different fixed-core clocks.

The original boundary distinction has an actual effect:
\((3,2^\infty)\) enters \(f_2\) for A but is terminal for I and R.
For I/R, any predecessor of \(f_2\) requires \(2\le a<3\), hence \(a=2\).
Induction shows that \(\mathcal P_2^I=\mathcal P_2^R=\{f_2\}\).
For A, \(\mathcal P_2^A\) is the whole set of eventually-two sequences.
The singleton control source packet still carries every real phase modulo
\(\log2\), all nonzero source lags and all repeated traversals.

MAIN retains each \(f_q\) as a terminal, not a fixed dynamical source.
Its entire terminal class is the same legal-prefix expression as (12)
with M's guard and endpoint \(f_q\); equations (8) and the terminal rule
above retain all its incoming. In particular \(f_2\) has none, because
the only range-eligible letter two does not divide three.
Nothing turns these terminals' identity arrows into periodic steps.

## 6. Arbitrary-period arithmetic prefilter and precise failure

Let an actual periodic source for any of the four owners have least
source period \(\ell\), with period word \(a_0,\ldots,a_{\ell-1}\).
All cyclic phases are legal by actuality. By (3) and the entire-image result (9),
its positive primitive \(C\), not a source-period-normalized value, satisfies
\[
 C=\sum_{i<\ell}\log[a_i(a_i-1)],\qquad
 e^C=\prod_{i<\ell}a_i(a_i-1).                                 \tag{14}
\]
Every factor is an integer at least two. If \(\ell\ge2\), (14) is
composite. If \(\ell=1\), the factor \(a(a-1)\) is prime exactly when
\(a=2\): for \(a\ge3\) both factors exceed one.
Thus a prime-valued primitive anywhere in these owners must be the
actual fixed core \(2^\infty\), with primitive \(\log2\).
This argument ranges over arbitrary actual least periods without enumerating them.

Let \(\mathscr L_U\) denote the positive primitive packet ledger, retaining
multiplicities. MAIN excludes the only possible prime core, so
\[
 \mathscr L_M\cap\{\log p:p\text{ an ordinary integer prime}\}
       =\varnothing.                                         \tag{15}
\]
If \(\mathscr L_M\) is nonempty, every entry is nonprime-valued; if it is
empty, the required nonemptiness fails. In either case the combined target
of nonemptiness and prime-only purity is false, before uniqueness or
all-prime coverage could help.
Equation (15) is NOT a proof that \(\mathscr L_M=\varnothing\), and this
paper supplies no MAIN nonprime periodic witness or higher-period census.

Each of A/I/R instead has exactly one prime-valued full packet globally,
namely its \(\mathcal P_2^U\), and no packet at any other ordinary prime.
This uniqueness follows from (14) and the complete packet (12), not a
selection among incoming prefixes. Each control also has the actual fixed
source \(3^\infty\) of primitive \(\log6\), and indeed every \(q\ge3\)
constant gives a composite multiplier. Thus permission-OFF discriminates
the survival of a prime-valued packet but does not achieve a prime-only ledger.
No control transfers a missing positive claim to MAIN.

## 7. Scope, integrity and handoff

The frozen probability and prefix IMAGE are owned on the entire source.
The necessary combined arithmetic target is refuted, so this candidate stops.
The obstruction depends on this exact \(\rho\) and these permissions:
it is not a theorem about every divisor process or every admissibility law.
The original coding weights already restrict prime support, a
PROVES_TOO_MUCH risk distinct from the actual arithmetic-OFF comparison.
Stronger arithmetic naturalness remains OPEN.
T0 and measured clock ownership are established; arithmetic T1 NOT PASSED;
T3 NOT AUDITED; classical fields NOT APPLICABLE; formal Route coordinates
UNASSIGNED; Route B NOT INVOKED. No operator or classical flow is constructed.

Scientific inputs were only the full clarified 110-line
[card](candidate-card.md) and repository paper template.
Clarified card SHA256:
b6f84995856bfdb16e2ec2703a620d1c1d5e22fd4688d4e5078d42b9707e4dcd.
The proof uses exact product measures, prefix identities and integer factors,
not numerical experiments. See [claim ledger](claim-ledger.md),
[README](README.md), [batch exposure record](batch-log.md) and the
[evidence directory](evidence/) for separately staged materials.
No scope, raw, reviewer or peer proof body was read; final review is not
certified by this author handoff.

AI assistance: the AI author supplied derivation, drafting and internal checks.
Same-author helper direct_controls read the clarified card only for bounded
A/I/R constant-core and incoming analysis, which the author independently
checked; its design-stage role inspected filenames only. It was not a reviewer.
Inherited authorship and informal prefreeze factorization/interface exposure
remain disclosed, not blind or outcome-sealed. ARS writing guidance informed
claim bounds and disclosure; same-model review is NOT_CALIBRATED, with no
human/external verification certified. Data are the definitions/proofs here;
no external dataset or human subjects were used. Human authorship, funding
and conflicts were not supplied and are not invented.
