# Actual packet counts for expanding circle covers

Candidate ID: `ANG-AUDIT-20260924-CPB01`. Paper449.
Outcome: `EXACT CIRCLE-COVER PACKET BUDGET; NO PRIME-CLOCK ADMISSION`
Context date:2026-09-24. Status: conditional theorem with external controls.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal UNASSIGNED; B NOT INVOKED.

## Abstract

A full expanding degree-N circle covering has exactly N^q-1 fixed points
of its qth iterate. Divisor inversion therefore fixes its complete number
of least-source-period packets. This count concerns actual circle points,
including their endpoint identifications, not free symbolic words. The same
object owns an inverse-Jacobian clock and a retained-lag height extension;
its positive primitives depend on return derivatives, not degree alone.
Three complete external controls exhibit a composite primitive, duplicate
prime primitives, and a noninteger fixed multiplier. They do not supply
an endogenous arithmetic candidate or a formal Route result.

## 1. Frozen class, lineage and owners

The [card](candidate-card.md) freezes X=R/Z with normalized flat length.
Fix integer N>=2 and a C1 lift f with f(x+1)=f(x)+N and f'(x)>=lambda>1.
Each such lift determines a separate map F([x])=[f(x)] on the entire circle.
There are no terminals, deleted cuts, fitted roofs or hidden selected subsets.
All map and inverse germs in this class are C1, not a silently stronger C-infinity
assumption. Three analytic controls below have higher regularity independently.

This audits the symbolic-admissibility to compact-geometric-realization arrow.
The full N-symbol alphabet is a comparator for an unpruned cover; it is not
the project's prime-symbolic admissibility. An arithmetic source would have to
be supplied within a future exact owner. This class and A/B/C are EXTERNAL
CONTROLS, not main candidates merely because they admit precise counting.
The full source, flat measure, map, germ clock, histories and height action
below always belong to the same chosen f. No symplectic form, suspension
roof, Hamiltonian lift, operator, determinant or trace is constructed.

## 2. Every inverse and every-point IMAGE

Since f'>0, f is strictly increasing. Its integer translation rule implies
limits plus/minus infinity, so it has a global C1 inverse g. For a lift y of
a target, all predecessors are [g(y+j)], j in Z. The identity
g(y+j+N)=g(y+j)+1 proves periodicity in the sheet index. Conversely,
g(y+i)-g(y+j)=k in Z implies i-j=Nk. Thus exactly N distinct predecessors
occur, represented by j=0,...,N-1; changing the target lift permutes them.
Local circle charts give honest C1 inverse germs through every such source.
No globally continuous ordering of the N sheets is assumed.

For any injective local inverse theta, its derivative at target Fz is
J_theta(Fz)=1/f'(x)>0 for any lift x of z. Periodicity of f' makes this
independent of lift and chart. Every Borel subset E of that inverse-chart
domain satisfies mu(theta E)=integral_E J_theta dmu, by one-dimensional
change of variables. Borel restrictions and cut partitions preserve this
identity. Germs give the same assigned value at every retained point,
including null cuts; the measure identity alone would not fix null values.
The actual step clock is consequently

\[
 \kappa([x])=\log f'(x),\qquad
 S_r(z)=\log (f^r)'(x),\quad S_0=0.                         \tag{1}
\]

The derivative product proves (1), including every inverse history. This is
derived from IMAGE, not a roof set equal to log N. Compactness gives a finite
upper bound M=max f', so log lambda<=kappa<=log M at every point.

## 3. Full histories, kernels and height primitives

Use all actual triples

\[
 G_F=\{(z,r-s,w):F^rz=F^sw,\ r,s\ge0\},\qquad
 c(z,r-s,w)=S_r(z)-S_s(w).                                 \tag{2}
\]

Source is w, range z. Equal triples are identified, retaining lag. Two
witnesses for the same triple differ by equal additional iterates on the
two sides, whose common-tail sums cancel. To compose, extend both middle
histories to their larger depth; the middle sums cancel. Thus c descends
and adds, inversion negates it, and the forward arrow(Fz,-1,z) has -kappa(z).
Let P_r=exp S_r. The complete three kernels are

\[
\begin{split}
 \ker c&=\{(z,r-s,w)\in G_F:P_r(z)=P_s(w)\},\\
 \ker\ell&=\{(z,0,w):F^rz=F^rw\text{ for some }r\ge0\},\\
 \ker c\cap\ker\ell&=\{(z,0,w):F^rz=F^rw,\ P_r(z)=P_r(w)
                                      \text{ for some }r\ge0\}.
\end{split}                                                \tag{3}
\]

These retain nonunit coalescence; clock equality alone never creates an arrow.
All incoming to a core C form B_C=union_(d>=0) F^(-d)(C), with every N-fold
inverse retained at each step. A general source class is the union of
F^(-r)({F^s z}) over all r,s>=0. These are exact untruncated descriptions.
Distinct deterministic cycles have disjoint eventual basins: a common
eventual point would force the two forward cycles to coincide.

If z is not eventually periodic, its source isotropy is trivial: unequal
equal iterates would give a periodic tail. If its tail has least period q,
the isotropy lags are exactly qZ, and its clock image is the ENTIRE group
H_z=CZ, where C=sum_(j<q)kappa(x_j)>0 on that core. This follows by
cancelling transient sums and then counting whole traversals, not selecting
one loop subgroup. The full extension sends(w,h)to(z,h+c), all h in R.
Its isotropy is the kernel of the source character, hence trivial here.
Physical height translation on the extension orbit SET has stabilizer H_z.
Thus the positive primitive is C, never C/q, with ordinary integer repeats.
Non-eventual classes have H=0 and no positive primitive.

For complete explicit coordinates on B_C choose core x_j=F^j x_0,
0<=j<q; P_j^*=sum_(i<j)kappa(x_i). If d_z is first arrival at x_(j_z), put
chi_z=j_z-d_z, ell_C=C/q and beta_z=S_(d_z)(z)-P_(j_z)^*+chi_z*ell_C.
Every actual basin arrow is exactly

\[
 (z,k,w),\quad k\equiv\chi_w-\chi_z\pmod q,\qquad
 c=k\ell_C+\beta_z-\beta_w.                                \tag{4}
\]

Necessity follows by advancing a meeting onto the core. Conversely, any
congruent lag is realized by sufficiently long nonnegative core meetings.
The full height phase is

\[
 h-S_{d_z}(z)+P_{j_z}^*\pmod {C\mathbb Z}.                  \tag{5}
\]

Equations(4)–(5) give every kernel restriction and all real phases, not just
those at a chosen core representative. For a non-eventual class choose any
reference object and an arrow to z of clock b_z. H=0 makes b_z independent
of that arrow, so h-b_z supplies all real phases. This pointwise coordinate
construction asserts no globally measurable selector or regular quotient.

## 4. Exact all-period source packet budget

The qth lift satisfies f^q(x+1)=f^q(x)+N^q. Let D_q(x)=f^q(x)-x.
Its derivative is at least lambda^q-1>0 and
D_q(x+1)=D_q(x)+(N^q-1). Hence D_q maps [0,1) bijectively onto
[D_q(0),D_q(0)+N^q-1). A half-open interval of integer length K contains
exactly K integers, including an integer left endpoint and excluding its
right counterpart. Integer values of D_q correspond exactly to fixed
circle points of F^q. Therefore

\[
 A_q:=\#\operatorname{Fix}(F^q)=N^q-1.                       \tag{6}
\]

Let E_q count points of least period q. A fixed point of F^q has least
period dividing q: division with remainder of q by its least period proves
this directly. Thus A_q=sum_(d|q)E_d. Define the integer Moebius function
mu_ar(n)=0 if a square of a prime divides n, and(-1)^r for a product of r
distinct primes, with mu_ar(1)=1. Expanding(1-1)^r over the prime divisors
gives sum_(d|n)mu_ar(d)=0 for n>1 and1 for n=1. Reordering finite divisor
sums now proves

\[
 E_q=\sum_{d\mid q}\mu_{\rm ar}(q/d)(N^d-1),\qquad
 a_q=E_q/q.                                                \tag{7}
\]

Here a_q counts actual full source packets with least core period q, because
each cycle has q points and distinct cycles' incoming basins do not merge.
The arithmetic function in this counting proof is not an inserted dynamical
prime label or clock. For q>=2, subtracting all shorter fixed-point counts
is an overestimate of the proper-divisor contribution. Since
sum_(d=1)^(q-1)N^d<=N^q-2, (6) gives E_q>0; also E_1=N-1>0.
Consequently every positive source period occurs. This is an exact infinite
claim proved for the frozen class, not an extrapolated finite orbit table.

On each such cycle the actual primitive is instead

\[
 L_C=\log\prod_{j=0}^{q-1} f'(x_j),\qquad
 q\log\lambda\le L_C\le q\log M.                           \tag{8}
\]

Degree fixes (7), not the factors in (8). It supplies neither log-prime
support, prime uniqueness nor coverage. Choosing a multiplier afterward
or identifying equal lengths would change the packet audit.

## 5. Complete linear controls A and B

Write F_N([x])=[Nx], with N=2 for A and N=3 for B. The inverse branches
are[(y+j)/N], j=0,...,N-1, with J=1/N and kappa=log N, now derived from
their own maps. For all arrows c=k log N. Their exact arrow condition is

\[
 \exists s\ge\max(0,-k):N^{s+k}z=N^s w\pmod1.               \tag{9}
\]

All three kernels coincide with k=0 coalescence, equivalently
z-w in Z[1/N]/Z; they include nonunits. Every rational circle point is
eventually periodic because its iterates stay among finitely many residues
of a denominator. Conversely an eventual equality forces
(N^(d+q)-N^d)x to be an integer, so every nonrational point is non-eventual.
Fixed points of F_N^q are precisely j/(N^q-1),0<=j<N^q-1.
For every least-q cycle C, all its depth-d predecessors number q*N^d;
the nested union is its entire incoming packet. Equations(4)–(5) specialize
to beta=0, c=k log N and phase h+(j_z-d_z)log N modulo q log N.
Source isotropy is qZ, extension isotropy trivial and ENTIRE H=q log N Z.
Non-eventual classes retain(9),H=0 and all real phases as in Section3.

For N=2 there is one fixed packet with primitive log2, but the unique
least-two cycle {1/3,2/3} has primitive log4. It is not a repetition of the
fixed packet. For N=3 there are two fixed packets {0},{1/2}, both log3;
their full basins remain distinct. Every q>1 core in either control has
primitive log(N^q), a composite-integer logarithm. Formula(7) gives all
their multiplicities without selecting a convenient representative.

There are N^q length-q digit words. Repeating a word with integer value
j in{0,...,N^q-1} gives the circle point[j/(N^q-1)]. Only the two extreme
values0 and N^q-1 coincide. Thus actual qth-fixed points number N^q-1,
not N^q. For completeness, two unequal digit expansions can agree on the
line only when the first differing digit is followed by opposite all-zero
and all-(N-1) tails, from equality in the geometric tail bound. Periodic
digit strings with such tails must be constant. This accounts for the
endpoint identification and no other periodic-word collision. It does not
turn a full shift into the required prime-symbolic source.

## 6. Complete fixed gate for nonlinear control C

Let f_C(x)=2x+sin(2pi*x)/(4pi). Its derivative2+cos(2pi*x)/2 lies in
[3/2,5/2], so every class hypothesis and all source counts hold with N=2.
The unique increasing real inverse g_C exists by Section2; all actual
circle predecessors are[g_C(y+j)],j=0,1. Their own J is the reciprocal
of2+cos(2pi*x)/2 at the reconstructed point. This is an exact inverse
definition, not a claim of a closed elementary solver or constant clock.

The displacement f_C(x)-x=x+sin(2pi*x)/(4pi) increases strictly from0
to1 on[0,1], so the only fixed circle point is0. Its derivative is5/2,
giving L_0=log(5/2), not a log of an ordinary integer prime. The two
immediate predecessors are0 and1/2. The whole fixed basin B is
union_(d>=0)F_C^(-d)({0}); each level has exactly2^d points and is nested.
No predecessor outside that union belongs to the fixed packet.

For first arrival d(z), define beta(z)=S_d(z)-d(z)L_0 using the actual
cosine-derivative sum. The full restriction is BxZxB with
c(z,k,w)=kL_0+beta(z)-beta(w). Its lag kernel has k=0, its clock kernel
has precisely kL_0+beta(z)-beta(w)=0, and its joint kernel has k=0 and
beta(z)=beta(w). These are exact functions on the full recursively specified
basin, with no depth cutoff. Source isotropy is Z, extension isotropy trivial,
ENTIRE H=L_0 Z, and all phases are h-beta(z) mod L_0.
Every other source retains the complete Section3 descriptions. No higher
cycle-clock census for C is claimed. Its degree-two counts agree with A,
but even its fixed multiplier differs, disproving determination by degree.

## 7. Decision, evidence and integrity boundaries

The exact source-period packet budget and own Jacobian-clock formula are
established for the stated expanding-cover class. The controls respectively
exhibit composite time, duplicate prime time, and noninteger time. None is
an admitted arithmetic main candidate. Retain this conditional filter and
FORK the search; do not insert a roof or prune endpoints to rescue a control.
Arithmetic T1 NOT PASSED; T3 NOT AUDITED; classical NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. Strong naturalness/PROVES_TOO_MUCH of
a future arithmetic realization remain OPEN. No RH, zero, trace or operator claim.

The [claim ledger](claim-ledger.md) and [summary](README.md) state the same
scope. Definitions and proofs here are the evidence; no scientific numerical
experiment, external literature campaign, Git mutation, PDF or publication
artifact was used. Counts and bounds are exact, without precision cutoffs.
Root's card records targeted old392/430 definition reads and prior440summary
exposure, with exact ranges/hashes; no nonconjugacy or global novelty claim.
Informal counting/control feasibility preceded freeze and is disclosed. Root
wrote this author text before reading the current449 raw derivation; its
RAWREADY notification supplied only a receipt. No helper supplied this proof.
ARS separates the frozen question, scope review, raw derivation and final
comparison; a checkpoint is not mathematical evidence by itself.
AI agents derived, drafted and internally checked the work; same-model shared
history is NOT_CALIBRATED, not human/external/cross-model validation. No human
authorship or reading attestation is fabricated. Data availability: definitions
and exact proofs in this package; no empirical dataset. No human/animal subjects
or personal data. Funding not supplied; conflicts not assessed; venue criteria
unavailable. No submission-readiness or calibrated correctness claim.

EOF — CPB01 author proof; no further research initiated.
