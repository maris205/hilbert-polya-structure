# Divisor renewal: an owned conditional clock with nonprime primitive packets

**Paper:** 370-divisor-renewal-clock. **Candidate:** ANG-20260922-DRE01.
**Date:** 2026-09-22. **Batch:** MEASURED-HISTORY-20260922-E, round 1/5.
**Status:** OWNED RENEWAL CLOCK; NONPRIME GAP PRIMITIVES — STOP / FORK.
**Formal coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

All integer-divisibility tests determine a finite-gap law. We construct its complete stationary renewal source, actual
inverse branches and every-Borel IMAGE law, with the frozen versions retained
at every null periodic history. Every primitive cyclic gap word owns exactly
one physical packet, with least time equal to minus the logarithm of its
gap-probability product; source lag instead counts the sum of the gaps.
The complete tests (2),(3),(4),(2,3) give least times log2, log3, log12,
log6. The latter two violate the frozen prime-time target. All incoming
histories, kernels and phases remain; three controls have their own ledgers.
This is an owned renewal construction, not a general Markov escape or proof of stronger naturalness.

## 1. Frozen identity, question and permitted inputs

The [card](candidate-card.md), including CP1, fixes the source, measure, versions and tests before analysis.

| Item | Exact owner | Boundary |
| --- | --- | --- |
| Arithmetic seed | First failed integer divisor of Haar q in Z-hat | No supplied prime alphabet |
| Source | Residual wait and every future finite gap | No never-renewing boundary point |
| Measure / clock | Stationary renewal probability / actual inverse IMAGE | No added roof |
| Packets | Full actual lag groupoid and real-height quotient | Entire return group, no selected representative |
| Classical geometry / later analysis | None supplied | A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED |

The arithmetic q defines a distribution, not a subsequently discarded coordinate. The lineage is divisor readout -> first failed divisor
symbol -> all renewal histories. This probabilistic deformation and its law
are declared designs. No source or clock theorem is transferred from 365.
The target is least time log p with at most one primitive per prime; all-prime coverage is additional. No rescaling.

## 2. The arithmetic gap law and finite mean

Let L_0=L_1=1, L_n=lcm(1,...,n). In K=Z-hat, q in dK for all 2<=d<=r specifies L_r K, of Haar mass 1/L_r.
Their intersection is {0}: each finite-modulus residue must vanish.
Its Haar mass is zero since it lies in n!K for every n. Thus the
first failed divisor b is finite off zero and has Borel level sets, with
\[
w_d=\frac1{L_{d-1}}-\frac1{L_d},\qquad
S_r=\sum_{d>r}w_d=\frac1{L_r}\quad(r\ge0).
\tag{1}
\]
Here w_d=0 when no lcm change occurs. Unique factorization makes L_d change precisely at prime powers: a new maximal prime-power
factor appears exactly then. Hence D={d:w_d>0} is derived, not selected.
Telescoping gives sum_d w_d=1; every S_r is strictly positive.
For r>=2, the coprime integers r and r-1 both divide L_r, so
\[
M=\sum_{r\ge0}S_r
 =\sum_d d\,w_d
 \le2+\sum_{r\ge2}\frac1{r(r-1)}=3,\qquad M>2.
\tag{2}
\]
The equality is Tonelli; the mean is finite. Every d in D is at least two and 0<w_d<1.

## 3. Complete probability source, coding and actual inverses

Put nu=product(w) on D^N and X=N_0 times D^N, with product Borel structure. Define mu({r} times E)=S_r nu(E)/M. Equations (1)--(2)
give a probability on the ENTIRE X, with positive mass on every nonempty
finite cylinder. Every individual future gap sequence is null: w_d<=1/2,
so its first n prescribed gaps have mass at most 2^(-n). These points remain.
The frozen total map is
\[
T(r,g)=
\begin{cases}(r-1,g),&r>0,\\(g_1-1,\sigma g),&r=0.\end{cases}
\tag{3}
\]
Its exact predecessors are W(r,g)=(r+1,g) everywhere, and E(r,g)=(0,(r+1,g)) when r+1 is in D. Both are Borel.
Substitution gives TW=TE=id on their domains. Conversely a predecessor
of positive residual must be W, and one of residual zero must be E;
the images partition X by positive versus zero residual. There are no
terminals or omitted incoming branches.

The bit observation is a_i=1 exactly when the residual of T^i x is zero.
It is a bijection onto the binary sequences with infinitely many ones
and successive one-distances in D. The first one is at r, and its
successive distances recover every g_i; this also proves Borel inverse and
shift intertwining. The finite r and finite gaps ensure infinitely many
events, including for unbounded gaps. The binary compact closure is not
the carrier; words with finitely many ones, including all-zero, are absent.

## 4. Every-Borel conditional IMAGE and all histories

For Borel A, the W image has mass sum_r S_(r+1)nu(A_r)/M. For A in the E domain, its E image
has mass sum_r w_(r+1)nu(A_r)/M: its first gap is fixed and its remaining
tail has law nu. These identities, valid for arbitrary Borel sections, prove
\[
j_W(r,g)=\frac{S_{r+1}}{S_r},\qquad
j_E(r,g)=\frac{w_{r+1}}{S_r},\qquad
\mu(\theta A)=\int_A j_\theta\,d\mu.
\tag{4}
\]
Both frozen versions are positive and finite on their ENTIRE domains. Put w_(r+1)=0 outside D only in branch sums.
Since S_r=S_(r+1)+w_(r+1), the disjoint inverse images give
mu(T^(-1)A)=mu(A); this is source probability invariance.

Write V(x)=log S_r and let P_m(x) be the product of w_d over exactly
the renewal events in source steps 0,...,m-1, with empty product one.
The step clock is log(S_(r-1)/S_r) at r>0 and log(S_(d-1)/w_d) at r=0,g_1=d. Therefore
\[
A_m(x)=V(T^m x)-V(x)-\log P_m(x).
\tag{5}
\]
This is a finite telescoping sum, not a roof. On each legal inverse-history chart theta:T^m x->x, composition of
(4) gives every-Borel IMAGE exp(-A_m(x)), evaluated at x=theta(y) on the target variable y.
Fixing the finitely many encountered gaps and residuals gives countably
many such charts; iterated Borel change of variables proves the assertion
for arbitrary Borel subsets, not merely finite cylinders.

For an actual arrow gamma=(z,m-n,y) with T^m z=T^n y,
\[
c(\gamma)=A_m(z)-A_n(y)
 =\log\frac{S_{r_y}P_n(y)}{S_{r_z}P_m(z)}.
\tag{6}
\]
Equal triples have witnesses differing by a common number of forward
steps; clocks of their common tail cancel, proving witness independence.
To compose arrows, extend their witnesses until the middle histories meet
at the same iterate; the middle clocks cancel, proving additivity.
The prefix-replacement map from y to z has every-Borel IMAGE exp(-c),
by composing its actual forward chart with its actual inverse chart.
This proves overlapping-chart agreement at EVERY point, including null periodic histories.

The FULL kernels have the following finite, necessary-and-sufficient tests:
\[
\ker c=\{\gamma:S_{r_z}P_m(z)=S_{r_y}P_n(y)\},\quad
\ker\ell=\{\gamma:m=n\},\quad
\ker c\cap\ker\ell=\{\gamma:m=n,\ S_{r_z}P_m(z)=S_{r_y}P_m(y)\}.
\tag{7}
\]
All triples in (7) must be actual arrows. Lag zero need not mean identity: different prefixes can merge. Formula (7) includes every
nonidentity kernel arrow and every signed lag, not just returning cores.

## 5. Entire isotropy, gap necklaces and all physical phases

Two sources (r,g),(s,h) share an orbit exactly when sigma^a g=sigma^b h for some a,b>=0; residuals are arbitrary.
Indeed advance each finite residual to an event, then consume the finite
gap prefixes; conversely any common future preserves a common gap tail.
Thus all incoming states are ALL finite admissible gap prefixes of every
shifted tail, with ALL residuals, equivalently union_(m,n)(T^n)^(-1){T^m x}.

If g is not eventually periodic, source isotropy is {0}. A nonzero lag equality would make the future bit sequence eventually
periodic, hence its successive finite gaps eventually periodic. Conversely
an eventually periodic g reaches a periodic core. Write its least repeating
cyclic gap word as delta=(d_0,...,d_(l-1)), reduced before cyclic rotation, and set
\[
P_\delta=\sum_{j=0}^{l-1}d_j,\qquad
B_\delta=-\sum_{j=0}^{l-1}\log w_{d_j}>0.
\tag{8}
\]
The complete periodic core consists of
(r,sigma^j(delta^infinity)), 0<=j<l, 0<=r<d_(j-1), with cyclic indices.
It has P_delta states. A source time period must take event positions to
event positions and rotate the gap sequence through a multiple of its
least gap period l. The least positive source period is consequently
P_delta, not l. Outside this core incoming states may have no literal
point return, but their ENTIRE groupoid isotropy is still P_delta Z:
any eventual equality has lag a multiple of the least core period.

Around one core traverse (5) gives c(P_delta)=B_delta. For every state
in its full incoming orbit,
\[
G_x^x=P_\delta\mathbb Z,\qquad H_x=B_\delta\mathbb Z,\qquad
\ker(c|G_x^x)=\{0\}.
\tag{9}
\]
For aperiodic gap tails both groups are zero. Extension isotropy is trivial everywhere, despite periodic-tail source isotropy.
Distinct primitive gap necklaces modulo cyclic rotation have distinct
groupoid orbits, even if their B values coincide.

Keep ALL X times R, with gamma:y->z sending (y,h) to (z,h+c(gamma));
physical time is height translation on this full orbit quotient as a SET.
Choose any reference a in a source orbit.
For an actual arrow gamma:y->a, the class of (y,h) has phase
h+c(gamma) modulo H_a. A different arrow changes it by exactly H_a,
which proves the full orbit fiber is R/H_a as a SET. At a periodic
core reference with T^n y=a the phase is h-A_n(y) modulo B_delta.
All such incoming histories and every real h are retained. Translation
therefore gives exactly ONE primitive physical packet of least B_delta
per primitive gap necklace; its repetitions have times k B_delta on that
same packet. Aperiodic tails instead give real-line orbits with no nonzero
return. No spatial, null-state or equal-time identification is added.

The frozen four tests are complete packets, not selected source points:

| Primitive gap word | Gap probabilities | Least source period / isotropy | Entire H and least physical time |
| --- | --- | --- | --- |
| (2) | w_2=1/2 | 2; 2Z | (log2)Z; log2 |
| (3) | w_3=1/3 | 3; 3Z | (log3)Z; log3 |
| (4) | w_4=1/12 | 4; 4Z | (log12)Z; log12 |
| (2,3) | 1/2,1/3 | 5; 5Z | (log6)Z; log6 |

The values use L_1=1,L_2=2,L_3=6,L_4=12 in (1). All four necklaces are primitive and distinct. Their entire
incoming sets and phases are those above; extension isotropy is zero.
Neither the log12 nor log6 packet is a repetition of a different packet.
Each is a decisive nonprime primitive under CP1's frozen target.

## 6. Three independently measured controls

**GEOMETRIC.** D_G={1,2,...}, v_d=2^(-d), tails V_r=2^(-r), mean two, and mu_G({r} times E)=2^(-r-1)product(v)(E).
Its own map is (3), W exists everywhere, and E exists everywhere because
every r+1 is allowed. The two inverse identities and exhaustive positive/
zero-residual partition follow directly from this rule.
For every Borel section, W replaces root mass 2^(-r-1) by 2^(-r-2);
E gives root mass 1/2 times v_(r+1)=2^(-r-2). Thus both IMAGE
versions are 1/2 at EVERY point. Their sum gives invariance and finite
histories give c_G=ell log2. Its clock and lag kernels and intersection
are all the full lag-zero tail relation. Its own bit image is exactly
the binary sequences with infinitely many ones, not the full binary shift.
The event-position argument gives source isotropy P_delta Z on every
eventually periodic gap orbit, with P_delta=sum d_j, and zero otherwise.
Its H is (P_delta log2)Z there, extension isotropy zero everywhere.
All incoming states are its own arbitrary residuals and finite positive-gap
prefixes of shifted tails; phases are h+c_G(gamma) modulo H.
Each primitive positive-gap necklace owns one least-P_delta log2 packet,
with its repetitions; the omitted all-zero binary boundary supplies none.

**DETERMINISTIC.** Only (0,2^infinity),(1,2^infinity), each of mass 1/2, remain. The map exchanges them; its unique inverse is
the same exchange. Branch W exists only at target residual zero; E only
at target residual one. Each singleton and hence every Borel subset has
IMAGE one. Consequently c=0 for all retained lags. Every source isotropy
is 2Z and remains 2Z in the extension; H={0}. The full clock kernel is
the whole two-point action groupoid, while lag kernel and intersection are
units. There is one actual source orbit with both incoming states, all
real height phases, and a real-line physical orbit without positive period.

**REINDEX-OFF.** On MAIN's X and mu, T_I=id has just inverse id, with every-Borel IMAGE and fixed version one.
Its groupoid is ALL (x,k,x), k in Z, not an effective identity relation.
The clock is zero, its kernel the whole groupoid, and lag kernel and
intersection the units. Source and extension isotropy are Z at EVERY x;
H_x={0}. Incoming states consist only of that x. Its full quotient is
X times R, with all height phases and one nonperiodic physical line per x.
No MAIN renewal branch, packet or clock is transferred to this control.

## 7. Markov boundary, gates and handoff

The residual Markov process moves from r>0 to r-1, and from zero to d-1 with probability w_d.
The stationary root law is S_r/M. Gap words concatenate freely at events.
The [364 card](../364-symbolic-index-branching-gate/candidate-card.md) requires
finite outgoing sets and unit mass on each starting-vertex path fiber.
This residual graph has infinitely many choices at zero and different
root masses, so that frozen theorem is not applied verbatim. This does
not establish escape from its concatenation mechanism: the actual mixed
gap word (2,3) already survives. Nonproduct bit observations do not imply
non-Markov dynamics or a positive arithmetic-selection result.

| Gate | Evidence for DRE01 | Status / limit |
| --- | --- | --- |
| T0 / declared T1 | Full probability source, inverses, every-Borel/all-point IMAGE and clock | ESTABLISHED; strong naturalness OPEN |
| T2 bounded prime-time target | Full necklace ledger; primitive log12 and log6 | FAIL — STOP / FORK |
| T3 / classical / formal / B | No analytic or classical owner / no formal evaluation | NOT AUDITED / NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

**Decision: stop this ID's target promotion; any fork needs a new card.** The wrong primitive packets
cannot be removed, relabelled as repetitions, or repaired by changing weights.
No all-prime coverage, target spectrum, stronger naturalness or novelty follows.
The same-object ledger is intact and all negative tests remain.

## Reproducibility and disclosure

The [card](candidate-card.md) specifies all inputs. No numerical cutoff, simulation, external literature or fitted data
are used. Author reads were this card, the paper template and 364's card
including its recorded outcome, not a current independent proof or review.
Root integrates separate claim/evidence records and review receipts; their
completion is not preclaimed here. Internal shared-history AI-assisted work
is NOT_CALIBRATED, not external peer review or a novelty certification.
