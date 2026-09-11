# Receiver-limited cyclic transfer: bounded author theorem package

Author: /root/round211_fresh_residual_scout, 2026-09-09 UTC.
Status: DEDUCTIVE_AUTHOR_CANDIDATE / INDEPENDENT_GATE_REQUIRED.
No manuscript number, admission, independent review or global novelty claim.
Sections 1–3 were articulated before the fixed pilot. Sections 4–6 are
post-pilot deductions and were NOT checked by that executable.

## 1. Literal, assumptions and claimed conjunction

For integers n>=1 and N>=0 put
\[
X_{n,N}=\{a\in\mathbb Z_{\ge0}^n:\sum_i a_i=N\}.
\]
Labels and cyclic orientation are fixed; indices are modulo n. Define
\[
q_i(a)=\min(a_i,a_{i+1}),\qquad
F(a)_i=a_i-q_i(a)+q_{i-1}(a).                 \tag{1}
\]
All currents use the old state. There is no scheduler or hidden variable.
This is an abstract conservative flow, not a chemical-realizability claim.

The bounded conjunction is:

- Every recurrent state is fixed. Subtracting the initial global minimum,
  each initial positive run is absorbed at its original right endpoint.
  The full-carrier worst entrance time is exactly the piecewise formula
  in Theorem 1, including n<=2 and N=0.
- Theorem 2 gives every target's one-step fibre as an evaluated finite sum
  of explicit integer-interval products and dyadic integrality tests.
  The construction is bijective, including ties and empty fibres.
  Theorem 3 deduces the sharp polynomial growth exponent floor(n/3) of
  the largest fibre at fixed n>=3.

The complete pointwise clock for n>=4, an exact largest-fibre value for
every (n,N), all its maximizers, all-time fibres and a basin census are
NOT claimed. Generic current conservation, permanent-zero arguments,
piecewise-linear branch partitioning and ordinary interval counting receive
no independent novelty credit. The substantive residual to assess is the
specific endpoint absorption/sharp clock together with the fully eliminated
inverse chambers and their sharp degree.

## 2. Mass, minimum and original-run terminal map

Since 0<=q_i<=a_i, (1) is nonnegative. Summing (1) telescopes, proving
F:X_{n,N}->X_{n,N}. For c>=0,
\[
F(a+c\mathbf1)=F(a)+c\mathbf1.                \tag{2}
\]
If a_i=0, then both adjacent currents in (1) vanish, so F(a)_i=0.
Let m=min_i a_i and r=a-m\mathbf1. The residual r has a zero, remains
nonnegative, and retains every zero it already has. Equation (2) therefore
shows min_i F(a)_i=m: the minimum is an exact invariant, not just a bound.

If r is not zero, split its positive sites into maximal cyclic runs,
using its zero sites as separators. In a run ending at e, let M be its
initial total mass and b=r_e its initial rightmost mass. No mass crosses
either zero boundary, so M is invariant for that original interval.

A positive site i can become zero only if its previous site is zero:
if r_{i-1},r_i>0 then F(r)_i >= min(r_{i-1},r_i)>0.
With r_{i-1}=0, disappearance occurs exactly when r_i<=r_{i+1}.
Consequently a run can shorten only by deletion of its first positive
site, at most one site in that run per update. It cannot split internally
or gain a positive site through an existing zero.

Its original right endpoint e never disappears. While its current run
has length at least two,
\[
F(r)_e=r_e+\min(r_{e-1},r_e)\ge r_e+1.
\]
Thus that run has at most M-b nonfixed rounds. Its positive length cannot
remain at least two indefinitely, since r_e<=M. It therefore eventually
consists of the sole mass M at e, after which it is fixed. Independent
original zero boundaries make the global entrance time the maximum of
the run entrance times.

It follows that the terminal residual places each original run mass at
that run's original rightmost site and is zero elsewhere. Add m back
coordinatewise for the terminal state of a. In particular,
\[
F(a)=a\quad\Longleftrightarrow\quad
(a_i-m)(a_{i+1}-m)=0\quad\hbox{for every }i.   \tag{3}
\]
For the reverse direction, every residual current is zero. For the forward
direction, any residual run of length at least two makes its endpoint
strictly increase. Uniform states are included by residual r=0. All
orbits eventually fix, so (3) is also the full recurrent classification.

## 3. Sharp worst clock and the short-cycle boundary

Let tau(a) be the least t>=0 for which F^t(a) is fixed, and set
H(n,N)=max_{a in X_{n,N}} tau(a).

**Theorem 1.**
\[
H(n,N)=
\begin{cases}
0,&n\le2\ \hbox{or }N=0,\\
\lceil\log_2 N\rceil,&n=3,\ N\ge1,\\
N-1,&n\ge4,\ N\ge1.
\end{cases}                                  \tag{4}
\]
The logarithm branch is equivalently the least t>=0 with 2^t>=N.

For n=1 there is only one current, and for n=2 the two currents both equal
min(a_0,a_1); hence (1) is the identity. N=0 is immediate.

For n>=3, Section 2 bounds every nontrivial residual run by M-b<=N-1.
When n=3 such a run has length two. Orient it as (A,B) followed by a zero,
where B is the right endpoint and A,B>0. A literal update is
\[
(A,B)\longmapsto((A-B)_+,\ B+\min(A,B)).
\]
With M=A+B, induction gives, for all t>=0,
\[
A_t=(M-2^tB)_+,\qquad B_t=\min(2^tB,M).       \tag{5}
\]
This holds after saturation too, since (0,M) is fixed. Its exact clock is
the least t with 2^tB>=M, at most ceil(log_2 N). All other residual runs
are singletons and fixed. For N>=2 the cyclic state (N-1,1,0) attains
ceil(log_2 N); N=1 is fixed.

For n>=4,N>=3 use (N-2,1,1,0,...,0). For 0<=t<=N-2 its positive
three-position part is
\[
(N-2-t,\ 1,\ 1+t).
\]
While the first entry is positive the middle site's inflow and outflow
are both one, and the last entry gains one. At t=N-2 the first entry is
zero; one further round gives (0,0,N). Thus its clock is N-1.
N=2 uses (1,1,0,...,0), with clock one; N=1 is fixed. This proves (4)
for every parameter, without extrapolation from the pilot. \(\square\)

## 4. Full inverse: orient comparisons, then eliminate them

The following proof is POST-PILOT and UNTESTED BY THE SAVED PILOT.

We give the formula for n>=3. For n<=2 the map is the identity and every
target has one predecessor. Fix any y in X_{n,N}.

For a source a define its UNIQUE comparison word
\[
s_i=\begin{cases}
1,&a_i\le a_{i+1},\\
0,&a_i>a_{i+1}.
\end{cases}                                  \tag{6}
\]
Assigning equality to 1 is essential. It prevents chamber double counting.
The all-zero word is impossible on a cycle. The all-one word forces all
a_i equal; its contribution is exactly 1 if y is uniform and 0 otherwise.

Consider any other word s containing both symbols. It is a cyclic
alternation of nonempty runs of ones and zeros. A **valley** v has
s_{v-1}=0,s_v=1. Let p be the following **peak**, s_{p-1}=1,s_p=0,
and let w be the next valley. Unwrap cyclic indices along v,...,p,...,w.
Write r=p-v>=1 for the number of one-edges and d=w-p>=1 for the number
of zero-edges. Repeat this convention once around the labelled cycle;
there is no quotient by rotation. Formulas never depend on which valley
is used merely to start reading the cycle.

Substitution of (6) into (1) gives the exhaustive local table
\[
\begin{array}{c|c|c}
s_{i-1}&s_i&F(a)_i\\ \hline
0&1&a_i\\
1&1&a_{i-1}\\
0&0&2a_i-a_{i+1}\\
1&0&a_i+a_{i-1}-a_{i+1}
\end{array}                                  \tag{7}
\]
The table is valid on ties with the convention (6).

### 4.1 Force every valley and every strict descent chain

Set A_v=y_v at every valley v. For the zero-run from p to w, define
backwards for j=w-1,w-2,...,p+1:
\[
A_j=(y_j+A_{j+1})/2.                         \tag{8}
\]
If any value in (8) is not an integer or is negative, or if
A_j<=A_{j+1}, assign weight zero to this comparison word and stop.
The valley values are already nonnegative because y is nonnegative.
For d=1 there is no recursion and A_{p+1}=A_w is already known.

These tests account for all strict descent edges except the edge leaving
each peak, which will be tested next. There is no choice in (8).

### 4.2 An isolated one-edge leaves no free variable

If r=1, then p-1=v. Set
\[
A_p=y_p-A_v+A_{p+1}.                         \tag{9}
\]
Require A_v<=A_p and A_p>A_{p+1}; otherwise the comparison word has
weight zero. These conditions also give nonnegativity. If they pass,
this rising run contributes weight one. Its peak equation in (7) holds
by (9), and it shares no unknown variable with a different rising run.

### 4.3 A longer one-run leaves exactly one integer interval

If r>=2, require
\[
y_{v+1}=y_v,\qquad
y_{v+1}\le y_{v+2}\le\cdots\le y_{p-1}.       \tag{10}
\]
For r=2 the chain in (10) has one term, so only its equality is nonvacuous.
Assign
\[
A_j=y_{j+1}\quad(v\le j\le p-2).
\]
This is consistent with the already assigned valley by (10).
The only still unknown variables are the prepeak a_{p-1} and the peak a_p.
Put
\[
S_p=y_p+A_{p+1},\quad L_p=y_{p-1},\quad
U_p=\min\left(\left\lfloor S_p/2\right\rfloor,\ y_p-1\right). \tag{11}
\]
Here \(y_{p-1}\) is a neighboring coordinate, whereas \(y_p-1\) is the
peak target coordinate minus the integer one.

Choose any integer t_p with L_p<=t_p<=U_p and set
\[
a_{p-1}=t_p,\qquad a_p=S_p-t_p.             \tag{12}
\]
The rising comparisons require the last forced value L_p<=t_p and
t_p<=S_p-t_p. The strict descent from the peak requires
S_p-t_p>A_{p+1}, equivalently t_p<=y_p-1. These are exactly (11).
All source entries are nonnegative: the forced entries and L_p are
nonnegative and a_p>A_{p+1}>=0. The peak equation in (7) holds by (12).
This run's number of choices is
\[
c_p=\max(0,U_p-L_p+1).                      \tag{13}
\]
All remaining ascending-interior equations are already enforced by the
shifted assignments and (10).

### 4.4 Formula and two-direction bijection

Let W_s(y)=0 if a test in (8), (9) or (10) fails. Otherwise let
\[
W_s(y)=\prod_{\substack{\text{one-runs of }s\\r\ge2}}
             \max(0,U_p-L_p+1),             \tag{14}
\]
with empty product one. A factor zero in (14) also rejects the word.

**Theorem 2.** For every y in X_{n,N}, n>=3,
\[
|F^{-1}(y)|=
\mathbf1_{\{y\text{ uniform}\}}+
\sum_{\substack{s\in\{0,1\}^n\\s\ne0^n,\ s\ne1^n}}W_s(y).  \tag{15}
\]
Each positive summand supplies all its sources explicitly through
(8)–(12). This is an evaluated formula: no search over mass compositions,
unbounded currents or feasibility predicates remains inside a summand.

**Necessity.** For an actual source a, its word (6) is unique. In the
uniform branch the assertion is immediate. Otherwise (7) forces the
valley assignments, then forces (8) along every strict descent. Its actual
strict comparisons make all tests in (8) pass. If r=1, (7) forces (9) and
its comparisons. If r>=2, every ascending-interior equation in (7)
forces the shifted assignments and (10). The peak equation forces the
sum in (12), and the last rising comparison plus strict peak descent
force exactly the interval bounds (11). Thus every actual source supplies
one admitted word and one integer from each stated interval.

**Sufficiency.** Conversely choose an admitted word and independent
integers in all its nonempty intervals. The disjoint cyclic valley,
descent-interior, ascent-interior, prepeak and peak roles assign every
coordinate once, except the consistent valley assignment already checked
by (10). The tests prove every one-edge is weak ascent and every zero-edge
is strict descent, including the two edges at each peak. Hence the
constructed vector has exactly the chosen word (6), not just a refinement.
All entries are nonnegative. Every line of (7) is satisfied with target y,
so the literal update is F(a)=y. Telescoping (1) now gives
sum_i a_i=sum_i y_i=N; no extra mass constraint was lost. Therefore
a belongs to the declared carrier.

Different interval choices differ at their prepeak coordinates, so they
give distinct vectors. Different words cannot give the same vector by
the uniqueness in (6). This proves both directions and all multiplicities
in (15). \(\square\)

There are at most 2^n-2 nonconstant words, each evaluated with O(n) rational
or integer arithmetic operations. This is an arithmetic-operation count,
not a bit-cost bound independent of N. No linear-time image criterion is
claimed. The image is precisely the targets with a positive value in (15).

## 5. A complete fixed-target specialization and sharp fibre degree

This section is also POST-PILOT and UNTESTED BY THE SAVED PILOT.

First consider a nonuniform fixed target y. Subtract m=min y and let
its positive residual masses be p_e at isolated spike sites e.
Let d_e be the number of zero sites immediately preceding spike e,
backwards to the previous spike; for a sole spike d_e=n-1.
Every d_e>=1.

A source has the same minimum m. If a positive residual source site i
maps to zero, Section 2 shows its previous source site is zero and
a_i<=a_{i+1}, with a_{i+1}>0. Then the output at i+1 is positive,
because its inflow is a_i>0. Thus such a new zero can only be the
last zero immediately before a positive target site, and there must
be another zero immediately before it. In a fixed target, every source
run therefore ends at one of its isolated spikes and has length one
or two. There can be no hidden source run elsewhere, because each
nonempty run has a positive output at its rightmost site.

If d_e=1, the prospective extra head would be preceded by the previous
positive spike, so it cannot disappear; no extra head is allowed.
If d_e>=2, the source at positions e-1,e can be
\[
(h,p_e-h),\qquad 0\le h\le\lfloor p_e/2\rfloor.
\]
Indeed the head disappears exactly for h<=p_e-h, and the receiver then
holds p_e. Heads at distinct spikes cannot overlap because there are
at least two available separating zeros when a head is nonzero.
All source possibilities and all their inequalities have now been
exhausted, proving the exact specialization
\[
|F^{-1}(y)|=
\prod_{\{e:\ d_e\ge2\}}\bigl(\lfloor p_e/2\rfloor+1\bigr).  \tag{16}
\]
For a uniform target, the invariant minimum and total mass force the
unique uniform predecessor. The empty product in (16) is one.

For fixed n let M_n(N)=max_{y in X_{n,N}} |F^{-1}(y)|.

**Theorem 3.** For every fixed n>=3, with k=floor(n/3),
\[
M_n(N)=\Theta_n(N^k)\qquad(N\longrightarrow\infty).        \tag{17}
\]
The power k is exact. This does not specify the exact maximum or every
maximizer for each finite N.

For the upper bound, each interval factor in (14) comes from a one-run
of length at least two. Every such one-run is followed by at least one
zero-edge. These disjoint runs therefore consume at least three edges
per factor, giving at most k factors. Every chosen interval coordinate
is a nonnegative source coordinate and hence at most N. Each factor is
at most N+1. From (15),
\[
M_n(N)\le 1+(2^n-2)(N+1)^k
        \le (2^n-1)(N+1)^k.                 \tag{18}
\]

For the lower bound choose k spikes separated cyclically by at least
two zeros; this is possible since 3k<=n. For N>=2k put
q=floor(N/(2k)), assign residual mass 2q to every spike, and add the
remaining N-2kq to one of them. All these spike masses are positive.
Take global minimum zero. Formula (16) yields at least (q+1)^k sources,
and q+1>=N/(2k). Thus
\[
M_n(N)\ge \left(\frac{N}{2k}\right)^k
\qquad(N\ge2k).                              \tag{19}
\]
Together (18)–(19) prove (17). For n<=2, M_n(N)=1 by identity. \(\square\)

For example, the symbolic target (0,0,2q,0,0,2q) at n=6,N=4q
has exactly (q+1)^2 predecessors by (16). This is a deductive family,
NOT an n=6 numerical run. It is deliberately outside the unchanged pilot.

## 6. Independence, source deductions and residual risks

The temporal proof uses the preserved minimum, immutable zero separators
and strictly increasing original run-end mass. It does not determine
which comparison words can produce a particular target, any dyadic
integrality constraints, or the independent peak/prepeak intervals.
Conversely the one-step chamber inverse has no argument about repeated
original-run absorption or the sharp worst clock. The fibre-degree bound
uses the packing of two one-edges and one zero-edge per free interval,
not the mass-increase time argument. These are two proof obligations,
not a clock restated as a fibre count.

This distinction does not establish external novelty. The exact UUC
source law and proof are deducted: (1) is not its binary uphill current,
and our inverse claim is not its generic current-word predicate. MNA's
generic run language and transfer-count machinery are deducted too.
Its specific merging map, triangular birth clock and threshold grammar
are not reused here. Ordinary ordered piecewise-linear chamber methods
and elementary dyadic/interval arithmetic remain background techniques.
A primary owner of the literal or of (15)/(17) would remove that credit.

The pilot pressures (1)–(5) only at n=3,4,5 and N<=6. It was run once
before Sections 4–5 were completed. The actual all-target indegrees it
printed do not constitute an executable test of (15), (16), or (17).
No inverse implementation, extended enumeration, replay or independently
authored verification has occurred. A fresh noncontributor gate must
check the complete deduction, including ties, r=1/r=2, wraparound,
n<=2, N=0, interval independence and the degree lower-bound spacing,
as well as direct ownership and residual value.
