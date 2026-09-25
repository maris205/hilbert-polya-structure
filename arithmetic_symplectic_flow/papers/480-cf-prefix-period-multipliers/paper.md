# Continued-fraction prefix maps exclude prime-log primitive times

Paper480-cf-prefix-period-multipliers. Candidate **ANG-AUDIT-20260925-CPM01**.
Date2026-09-25; batch PRE-P0-STRUCTURE-20260925-AA, round1/5.
Outcome: **OWNED CF PREFIX CLASS; NO PRIME-LOG PRIMITIVE — CONDITIONAL FILTER / FORK**.
Type: conditional measured-history CLASS audit, **not a MAIN candidate**.
Classical fields NOT APPLICABLE; T1 NOT PASSED; T3 NOT AUDITED;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

Consider any countably parsed finite-prefix substitution on the full space
of infinite positive-integer words, with the frozen continued-fraction
measure and its geometric inverse IMAGE clock. All source objects, terminal
states, overlapping inverse branches and actual lag triples are retained.
For a real positive physical primitive T, this paper proves that exp(T)
is an irrational root of a monic reciprocal quadratic with integer
coefficients. In particular T cannot equal the logarithm of an ordinary
prime. A scalar projective return instead has zero clock, with its source
isotropy retained. The proof constructs the coordinate and measure, reduces
only ACTUAL legal cycles to integral projective matrices, and computes the
ENTIRE height stabilizer. Identity, full shift and divisor-swap controls
have complete separately owned ledgers. The conclusion is a necessary
filter for this exact class, not an obstruction for arbitrary arithmetic
dynamics, nor a claim that every admissible matrix is dynamically realized.

## 1. Contract, lineage and exact class

Scientific input: the [original 91-line card](candidate-card.md), SHA256
`4138766434cb4f888ba85d7a96b561c87e8aeb6c0327fc44e72d503b4e4eb102`.
The [claim ledger](claim-ledger.md) and [overview](README.md) share this outcome.

| Field | Frozen class owner |
| --- | --- |
| Full source | `X=N_{>=1}^{N0}`, product Borel structure |
| Coordinate | `pi(a)=[0;a0,a1,...]`, onto irrational `(0,1)` |
| Original probability | `mu(E)=(1/log2) integral_(pi(E)) dx/(1+x)` |
| Member data | At most countably many disjoint full source cylinders `[U_i]`, finite output words V_i |
| Actual map | `T(U_i xi)=V_i xi` for every infinite tail xi |
| Partial domain | `Omega=union_i[U_i]`; all remaining objects terminal, not deleted |
| Clock/physical action | Own geometric inverse IMAGE; actual-history height translation on an orbit SET |
| Primitive | Least positive generator of the entire physical stabilizer |
| Classical lift/operator/trace | NOT APPLICABLE / NOT SUPPLIED |

Both U_i and V_i may be empty. An empty U is the sole source branch;
an empty parser has all objects terminal. Output cylinders may overlap.
No finite words or infinite letters are source objects. Arbitrary tails,
units, unbounded words and all null periodic states remain in X.
The class does not include arbitrary Borel parsers or arbitrary tail maps.

This is a conditional upper class. A proposed MAIN member still needs the
separate lineage arrow: actual divisor/composite observation → finite
parsing or prefix writeback → changed future arithmetic input. Generic
members are comparators, not automatically arithmetic candidates. Divisor
swap below supplies an explicit arithmetic control. No external prime
acceptor, prime table or log-prime roof is introduced. The class audit
records the symbolic-to-coordinate relation, not a conservative lift.

The quantified question is whether ANY actual positive primitive of ANY
member can be log an ordinary prime. There is no period census and no
claim of realizing an arbitrary projective matrix as a source itinerary.

## 2. Self-contained coordinate, measure and full inverse IMAGE

Put `H_a(t)=1/(a+t)`, `E_a=[[0,1],[1,a]]`, and let H_w and E_w be ordered
compositions/products; empty words give identities. For a word of length m,
write `E_w=[[A_m,B_m],[C_m,D_m]]`. Direct multiplication gives

`H_w(t)=(A_m t+B_m)/(C_m t+D_m)`, `det E_w=(-1)^m`,
`C_m=D_(m-1)`, `D_m=a_(m-1)D_(m-1)+D_(m-2)` for m>=2,
`D_0=1,D_1=a_0`, and `|H'_w(t)|=1/(C_m t+D_m)^2`.

For nonempty words C_m,D_m are positive. The nested prefix intervals
`H_w([0,1])` have diameter `1/[D_m(C_m+D_m)]`; the denominator recurrence
dominates an unbounded Fibonacci recurrence. Hence each infinite word
defines a unique limit pi(a). Every shifted tail has coordinate r_j with
`r_j=1/(a_j+r_(j+1))`. The first interval gives `r_j>=1/(a_j+1)>0`, and
the positive next tail gives `r_j<1`. Thus digit recovery is exactly
`a_j=floor(1/r_j)` and the reciprocal remainder is r_(j+1).

For a reduced rational p/q in `(0,1)`, a nonzero reciprocal remainder has
denominator at most p<q, so iteration eventually reaches zero. Our infinite
positive tail recursion never does; its limits are irrational. Conversely
every irrational in `(0,1)` has reciprocal remainders in that same set,
giving positive digits and membership in every associated nested interval.
Shrinking diameters prove that its reconstructed word maps back to it.
This proves bijectivity. Prefix diameters prove continuity of pi; Borel
floor/remainder digit recovery proves its inverse Borel. In particular
`pi([w])=H_w((0,1) minus Q)`: the open rational-endpoint interval with its
rational points removed. Integer Möbius maps with nonzero determinant and
their inverses preserve rational/irrational type. Images of Borel sets are
Borel by the Borel inverse; no finite-expansion convention is needed.

Let `rho(t)=1/((log2)(1+t))`. Its integral on `(0,1)` is 1. Removing the
countable rationals does not change it, so `mu(E)=integral_pi(E) rho(t)dt`
is a probability. Nonempty cylinders have positive interval length and
positive density, proving full support. Singletons have measure zero,
proving nonatomicity without dropping any null source object.

For a member branch U->V, define `I(V xi)=U xi` on ALL `[V]`.
Prefix removal/insertion proves both inverse identities and Borel bijection
onto `[U]`. Any actual predecessor has the unique source U containing it,
so this list exhausts every predecessor. Overlapping target cylinders are
not pruned; identical actual states/triples are not multiplied by labels.
An outgoing permission test on the target is never imposed.
The legal domain is a countable union of clopen cylinders, and its forward
pieces are homeomorphisms; consequently the partial T is Borel.

In coordinates I is `H_U o H_V^-1`. For `y=V xi`, `t=pi(xi)`, set

`J(y)=[(1+H_V(t))/(1+H_U(t))] |H'_U(t)|/|H'_V(t)|`.

The derivative formula, including the empty-word derivative 1, proves
strict positivity and finiteness at EVERY point. For Borel `E subset [V]`
put `B=H_V^-1(pi(E))`. Ordinary change of variables shows that both
`mu(IE)` and `integral_E J dmu` equal
`(1/log2) integral_B |H'_U(t)|/(1+H_U(t)) dt`.
This is the every-Borel IMAGE identity, not a cylinder-total calculation.
The frozen formula specifies null-point values; a.e. uniqueness does not.
The actual source clock is `kappa(x)=-log J_actual(Tx)`, with signs and
zeros retained. No other density or independent positive roof is used.

## 3. Full histories, incoming, kernels and physical primitives

Let D_r be the legal r-step domain, `D_0=X`, and
`S_r(x)=sum_(j<r)kappa(T^j x)`, with S_0=0. Use actual triples
`G_T={(x,r-s,y):T^r x=T^s y legally}`, source y, range x, lag retained.
Units include terminal objects; no positive iteration after a terminal is added.
Equal actual triples are identified. Define `c=S_r(x)-S_s(y)`.

Two witnesses of one lag differ by the same added number of steps on both
sides. The longer legal witness ensures those extra steps exist at the
common endpoint; both sums gain the same value. This proves descent.
For composition, align the two middle histories at the longer legal
length; the middle sums cancel. Hence c is additive, reverses sign under
inversion, and has `c(Tx,-1,x)=-kappa(x)` on a forward arrow.

Finite itinerary charts are again prefix substitutions: two cylinders are
disjoint or their finite prefixes are comparable, and a nonempty cylinder
intersection pulls back to a cylinder. Induction gives countably many
legal charts with no word-length bound. Chain rule with density cancellation
gives their pointwise derivatives. On a history-pair chart
`b=(T^r|C)^-1 o(T^s|D)`, for every Borel E in its domain,

`mu(bE)=integral_E exp(S_s(y)-S_r(by))dmu(y)
       =integral_E exp(-c(by,r-s,y))dmu(y)`.

The complete kernels are
`K_lag={(x,0,y):some legal equal-length iterates meet}`,
`K_clock={(x,r-s,y):T^r x=T^s y legally,S_r(x)=S_s(y)}`,
and `K_joint=K_lag intersect K_clock`. No equality of kernels is presumed.
The full extension sends `(y,h)` to `(x,h+c)` on `X times R`.
Physical translation acts on the orbit SET, without a manifold or regular
quotient assertion. Base orbits meet exactly when legal iterates meet;
lifted points meet exactly when an actual arrow has `h_x-h_y=c(x,k,y)`.

The complete predecessor prescription is
`Pre(y)={U_i xi:y=V_i xi}`. For every core set C set `Pre^0(C)=C` and
`Pre^(j+1)(C)=union_(y in Pre^j(C))Pre(y)`.
The inverse identities prove inductively that Pre^j(C) is EXACTLY the
legal j-step incoming set. Its union over ALL j gives the complete basin.
Infinite compatible incoming histories are precisely chains with each next
past point in Pre of the current point. This retains all finite prefixes
of every such chain without adjoining new states or duplicate arrows.

Nonzero source isotropy gives `T^(s+p)x=T^s x` with p>0, so x is eventually
periodic. Conversely a least-period-p cycle gives EXACTLY isotropy lags pZ:
every return lag is divisible by p on that cycle, and each multiple is
realized after any incoming tail. If x is not eventually periodic,
including any terminal basin, source isotropy is zero.
For an eventual p-cycle let `C_p=sum_cycle kappa`. Tail cancellation gives
`c(x,mp,x)=mC_p`; changing cycle phase does not change the sum.
Extension isotropy is `{mp:mC_p=0}`, so zero-clock isotropy is kept.

The ENTIRE physical stabilizer is `H_x=C_p Z` for eventual-cycle objects,
and `{0}` otherwise: `[x,h+t]=[x,h]` is equivalent to an isotropy arrow at
x with c=t. Thus a non-eventually-periodic source CANNOT generate positive H.
When C_p is nonzero, the physical primitive is `|C_p|`, with positive
repetitions `m|C_p|`; negative traversals remain. When C_p=0 there is no
positive primitive, despite nontrivial source/extension isotropy.
Each full base orbit contributes one physical orbit `R/H`: transport to
any anchor, then reduce the height modulo its entire H. Different transport
arrows differ by isotropy, proving phase consistency. Different base
orbits remain different packets even at the same time.

For a terminal t, an incoming x has a unique arrival depth ell(x), since
two depths would require forward evolution after t. The entire class is
its all-depth basin; lag is `ell(x)-ell(y)`, clock is
`S_{ell(x)}(x)-S_{ell(y)}(y)`, and the phase at t is
`h-S_{ell(x)}(x)` in R. These are ordinary retained objects, not fake fixed loops.

## 4. Actual cycle reduction and exhaustive multiplier classification

Each actual forward branch U_i->V_i has coordinate expression
`H_Vi o H_Ui^-1` represented by `B_i=E_Vi E_Ui^-1`.
Since the word matrices have determinant +/-1, B_i has integer entries
and determinant +/-1. For a legal least-period-p point x, finite chart
refinement gives a genuine neighborhood on which T^p is represented by
`Q=B_(i_(p-1))...B_(i_0)`. The rightmost matrix acts first.
Write `Q=[[a,b],[c,d]]`, `epsilon=det Q in{1,-1}`, `tau=a+d`, and `r=pi(x)`.
This matrix comes from the ACTUAL itinerary; no converse realization is assumed.

On a legal forward chart f, inverse IMAGE gives
`kappa=log(rho(f(r)) |f'(r)|/rho(r))`.
Multiplying around a closed orbit cancels the original density factors,
so, with `f_Q(r)=(ar+b)/(cr+d)`,

`C_p=log|f'_Q(r)|`, `f'_Q(r)=epsilon/(cr+d)^2`.

All signs are inside the absolute derivative, not discarded from the map.
The denominator is nonzero on the actual chart. Any finite pole of an
integer Möbius map is rational, hence is not a source coordinate here;
the branch-domain constraints are still required for legality.

The fixed equation is `c r^2+(d-a)r-b=0`. If c=0, irrationality of r
forces d=a and b=0. Unimodularity then forces `Q=I` or `Q=-I`.
More generally every scalar Q in this class is one of these two matrices.
It is projectively identity, so C_p=0. The refined legal neighborhood is
fixed by T^p; its whole continuum remains, even if least periods vary there.
No selected center replaces that identity family.

For a NONSCALAR actual return, therefore c!=0. Its fixed quadratic has
discriminant `Delta=(a+d)^2-4epsilon=tau^2-4epsilon`.
Negative Delta cannot give a real fixed point; zero or a positive square
Delta gives rational roots, not our irrational r. Thus the only remaining
case is positive nonsquare Delta. This includes all possible determinant
signs while excluding every incompatible degenerate case.
For epsilon=1 it requires `|tau|>=3`; for epsilon=-1, tau=0 would give
the excluded square Delta=4. No elliptic, parabolic or trace-zero exception
is silently removed; each is decided by this same fixed-point equation.

Set `lambda=cr+d`. The fixed equation gives
`Q(r,1)^T=lambda(r,1)^T`, so
`lambda^2-tau lambda+epsilon=0`, and the other eigenvalue is `epsilon/lambda`.
Because c!=0 and r is irrational, lambda is real, nonzero and irrational.
In particular `|lambda|!=1`. Consequently

`C_p=-2log|lambda| !=0`,
`T_primitive=|C_p|`,
`P=exp(T_primitive)=max(lambda^2,lambda^(-2))>1`.

These primitive statements use the ENTIRE isotropy calculation in Section3,
not merely this loop's derivative. Squaring the trace relation yields

`P+P^(-1)=tau^2-2epsilon=:N`,
`P^2-NP+1=0`, with integer `N>2`.

If P were rational, the rational-root argument for this monic integer
polynomial first makes P an integer, and its constant term then makes
P divide 1. That contradicts P>1. Hence P is irrational. Equivalently it
is the larger positive root `(N+sqrt(N^2-4))/2`, a reciprocal quadratic
unit. This formula does not assert that every such N or matrix is realized.

Replacing Q by -Q changes tau and lambda signs but neither its projective
map, absolute derivative, N nor primitive. These are the only scalar
rescalings between unimodular representatives, since rescaling changes
determinant by the scalar's square. Empty words and all cancellations
were already included in the matrix products and scalar case.

**Conditional theorem.** For EVERY member of the frozen class, every actual
positive primitive has irrational exponential P of the displayed form.
No such primitive is log of an ordinary prime (indeed, of any rational >1).
Scalar actual returns instead have zero clock and no positive primitive.
Non-eventually-periodic objects have no positive H. Thus there is no
unclassified source type from which a prime-log primitive is being ignored.

## 5. Three separately owned complete controls

### 5.1 Identity

The sole empty->empty branch has inverse identity, J=1, kappa=0 on ALL X.
It satisfies every-Borel IMAGE directly. Its groupoid is
`{(x,k,x):x in X,k in Z}`; different x never meet. The lag and joint
kernels are the units, the clock kernel is all G. Every x has least
discrete period1, source and extension isotropy Z, and entire H={0}.
Each complete base orbit is a singleton with phase space R and no positive
primitive. Pre(x)={x}; all finite/infinite histories are constant in x.
All states and heights are retained, not one representative of X.

### 5.2 Full shift

Every branch `(a)->empty` has inverse `I_a(xi)=(a,xi)` on ALL X.
For `t=pi(xi)`, its OWN formula is
`J_a(xi)=(1+t)/[(a+t)(a+t+1)]`, and `kappa(a,xi)=-log J_a(xi)`.
The every-Borel proof is Section2 applied to these actual words.
Moreover `sum_(a>=1)J_a(t)=1` by the telescoping series
`(1+t)sum_a[1/(a+t)-1/(a+t+1)]`; hence the full shift preserves mu.
Invariance of this many-to-one map does not set its branch clocks to zero.

All predecessors of y are `(a,y)`, and its depth-j predecessors are exactly
`u y` for every positive-integer word u of length j. All infinite compatible
prefix extensions remain. Actual histories are precisely lagged equality
of shifted tails, with c and the three full kernels from Section3 under
these own sums. No terminal objects exist.

All periodic cores are `w^infinity`, where w is a finite primitive word;
least discrete period is |w|. To justify completeness, sigma^p x=x forces
the first p digits to repeat forever; if w is a power its true period is
the shorter primitive block. Two such least-period cores share a base
orbit exactly when their primitive words differ by cyclic rotation:
equality of shifted periodic tails aligns their repeating blocks, and
the converse is a shift within the cycle. Retain ALL primitive cyclic
words, not one chosen period or one packet per numerical time.

For one primitive word w of length p, let `r=pi(w^infinity)` and
`E_w=[[A,B],[C,D]]`. The actual inverse of sigma^p on that branch is H_w,
with H_w(r)=r. Put `Lambda_w=Cr+D>1`: C,D are positive, D>=1 and r>0.
Its own density ratio cancels at r, giving
`K_w=S_p(w^infinity)=2log Lambda_w>0`.
Entire source isotropy is pZ, extension isotropy zero, and `H=K_w Z`.
The full packet is the all-depth incoming class of all rotations of
w^infinity; this is exactly all eventually periodic words with that
primitive cyclic tail. Its primitive is K_w and repeats are mK_w.
For any x in this class choose an arrival r_x at one fixed cycle phase;
its phase is `h-S_(r_x)(x) mod K_w`. Arrivals differ by multiples of p,
so this phase is well defined. Every phase and every finite-prefix arrival
is kept. Different primitive cyclic words remain different packets when
their K values coincide; no injectivity of w->K_w is asserted.
Non-eventually-periodic tails have trivial source/extension isotropy and
H=0, with the exact orbit/phase test of Section3. The class theorem applies
to all K_w, without enumerating words or assuming matrix realizability.

### 5.3 Divisor swap

Let `D(a,b)` mean `1<a<b` and `a|b`; put `s(a,b)=D(a,b) or D(b,a)`.
On every full `(a,b)` cylinder, T swaps the first pair when s is true and
is identity otherwise, leaving ALL tails unchanged. The predicate is
symmetric, so T^2=id and its full inverse is T itself. Thus every y has
exactly one predecessor T(y), and all finite/infinite incoming histories
are its alternating orbit or its constant orbit. No extra basin is omitted.

When s is false, each `(a,b,xi)` is a distinct fixed core, its actual
prefix replacement is identity, J=1 and kappa=0. When s is true, a!=b,
and `(a,b,xi),(b,a,xi)` form a least-period2 core. Both source points
remain; different tails or different unordered pairs give different cores.
Each branch uses its own U=(a,b), V=(b,a) in Section2's every-Borel IMAGE.
Their two prescribed derivatives multiply to 1 at EVERY point because
the second prefix replacement is the exact inverse of the first.
Thus the two-step clock is zero; this is not an a.e. or selected-tail claim.

For completeness, the local clock need not vanish on a swapped edge.
For a<b satisfying s, put u=(a,b,xi), v=(b,a,xi), t=pi(xi), L=ab+1 and
`A(t)=(L+a t)(L+b+(a+1)t)`, `B(t)=(L+b t)(L+a+(b+1)t)`.
The explicit CF derivatives give `kappa(u)=log(A(t)/B(t))=:theta`,
`kappa(v)=-theta`. In particular theta=0 exactly when
`L(1-2t)-(a+b+1)t^2=0`, with t restricted to the actual irrational source.
This is an exact all-point predicate, not an assumption that the edge clock
is nonzero. On that two-point orbit define b(u)=0,b(v)=-theta merely as
phase coordinates, retaining BOTH states. Every actual arrow has
`c(z,k,w)=b(z)-b(w)`, with even k for equal endpoints and odd k otherwise.
The clock kernel consists exactly of equal-b endpoints; the lag and joint
kernels are units. Source isotropy is 2Z and extension isotropy is the
same 2Z. For fixed cores these groups are Z, the clock kernel is all
isotropy, and lag/joint kernels are again units.
Thus ENTIRE H is zero for EVERY source state, with phase `h-b(x)` in R
on swapped orbits and height h on fixed ones. There are no positive
primitives; zero-clock isotropy and all continuum families survive.
The arithmetic D test changes actual evolution, but does not create a
prime packet in this control.

## 6. Scope of the conditional filter

The proof establishes the full measured-history class and excludes a
prime-log positive primitive for every actual member under these hypotheses.
It does not assume a positive ledger exists, reinterpret empty/zero-clock
ledgers as prime success, or classify which nonprime multipliers are realized.
The three controls cover empty words, all inverse branches, arithmetic
permutations, zero-clock isotropy and whole identity families.

This is not a MAIN or T1 pass. Application to a future arithmetic member
requires verifying its full carrier, complete prefix parser, actual map,
original measure, all-point version and packet convention against this
class; a symbolic resemblance is insufficient. Arbitrary Borel parsers,
other geometric carriers, tail-changing maps and other time prescriptions
are outside the theorem. Leaving a hypothesis is not itself a successful
escape and grants no transferred Route credit. No general RH or dynamical
no-go statement is made.

T0 is established for the conditional class owner. The prime compatibility
question has the negative answer proved above. Arithmetic T1 NOT PASSED,
T3 NOT AUDITED; classical fields NOT APPLICABLE; formal Route coordinates
UNASSIGNED; B NOT INVOKED. The disposition is CONDITIONAL FILTER / FORK,
without modifying stopped476 or selecting any new MAIN candidate.

## 7. Evidence, access and disclosure

The author read the original card1–91 through EOF and verified its Section1
SHA. No current reviewer/raw answer, old proof or sibling manuscript was
read. Root reported a separate CP1 PASS before author release; that report
was not read by this author. At author freeze final independent review was
pending; subsequent review is recorded separately in `evidence/review.md`.
No CP2/CP3, human or external verification is awarded here.

Same-author helper `cpm_matrix_author` was assigned only the frozen card's
integer projective fixed-point/degeneracy/multiplier algebra, with no files
or control census. This is author-side assistance, not an independent review.
The main author owns the coordinate/history/control proofs and integration.
The helper read card1–91 through EOF with the same frozen SHA and returned
its full algebra proof; the author compared its cases and clock interface
against Section4 before freezing. No reviewer/raw access was involved.
The scout read only476 original definition1–70/125 and325 definition1–72/197;
their exact prefix hashes and heading-only Outcome exposure are in the card.
Inherited exposure includes this author's full476/474 work and shared
research history. Earlier informal design mechanisms were not outcome-sealed.
No global novelty or nonconjugacy claim is made, and old results are not proof inputs.

ARS guidance informed stage separation, explicit adverse controls and
evidence/claim limits; this is not a complete submission pipeline. Author
and helper are same-model shared-history AI, internally NOT_CALIBRATED,
not blind/human/external peer reviewers. No scientific numerical code,
network, Git mutation, PDF, external upload, old edit or round485 work was
performed. No empirical data, human authorship, funding or conflict statement
was supplied or fabricated. Mechanical file checks do not prove the mathematics.

EOF — ANG-AUDIT-20260925-CPM01 author manuscript.
