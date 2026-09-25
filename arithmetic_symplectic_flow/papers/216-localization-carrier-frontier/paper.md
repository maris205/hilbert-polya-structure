# Relative localization and two exact full-carrier boundaries

**Paper ID:** 216-localization-carrier-frontier  
**Portfolio ID:** ASFS-FRONTIER-20260916-23  
**Research date:** 2026-09-16  
**Status:** PORTFOLIO CONTROL ADVANCE — RELATIVE PERIODIC LOCALIZATION; BOUNDARY AND LOCAL-COMPACTNESS STOPS; FULL-STATE TRACE AND NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

Three bounded tests separate periodic-channel localization from a
trace on the entire completed arithmetic flow. The separate 213
construction derives the actual positive-time orbit distribution as
a prescribed circle-minus-cover relative heat-trace limit. Its finite
blocks are ordinary trace-class operators, but its two infinite sectors
diverge separately, and its periodic-measure representation still loses
mixed-state observations. Two short tests identify different obstacles
on the retained full carrier. At an actual two-atom section corner,
smooth approximants to the same ambient delta give half, full or zero
boundary weight, so the unqualified restriction prescription is not
regularization independent. The full section, quotient and ordinary
transformation-groupoid arrow space are nowhere locally compact;
their continuous compact-support scalar functions vanish. These are
scoped stops, not universal trace or groupoid no-go theorems. All
states, actual clocks and owner distinctions remain intact. Intrinsic
full-state localization and arithmetic naturalness remain open.

## 1. Three contracts, not one assembled analytic owner

The [version-1 scope card](candidate-card.md) freezes exactly three
questions. Root's [213 card](../213-relative-periodic-heat-trace/candidate-card.md)
proposes circle-versus-cover relative heat localization on an
explicitly external periodic representation. SC23-BC tests one
unqualified ambient-delta prescription at actual section corners.
SC23-LC tests the conventional locally compact Hausdorff starting
assumption on the entire completed carrier. The short tests do not
make finite faces or periodic circles into a new full-state carrier.

The retained geometry is [194](../194-rapid-decay-cone-completion/paper.md):
the all-integer multiplication algebra, nonunit ideal I and declared
indecomposable quotient I/I^2 derive atom classes q_a. Set

\[
 p_k(v)=\sum_a a^k|v_a|,\quad
 E=\{v:p_k(v)<\infty\text{ for every integer }k\ge0\},
\]
\[
 \widehat P=\{v\in E:v_a\ge0\}\setminus\{0\},\quad
 Dv=(a v_a),\quad
 \widehat X=\widehat P/\langle D\rangle,\quad
 \phi_t[v]=[e^t v].
 \tag{1}
\]

The topology uses all p_k and the original quotient, not a single
norm, coordinate-product topology or disjoint-support topology.
Every finite and rapidly decreasing infinite support stays present.
The full mass-one section and actual return are

\[
 \widehat S=\{u\in\widehat P:p_0(u)=1\},\quad
 c(u)=\sum_a u_a/a,\quad
 F(u)=D^{-1}u/c(u),\quad \tau(u)=-\log c(u).
 \tag{2}
\]

The completed-state orbit equation e^t v=D^jv gives exactly one
singleton circle C_a of least time L_a=log a per derived atom,
all positive repeats, and no mixed periodic state. Neither short
test changes this ledger or the physical clock.

The [lineage](../../docs/prior_work/README.md) is proper-factor
symbolic admissibility -> indecomposable arithmetic observable ->
completed positive geometry -> analytic observations of the actual
flow. This is not an executed sieve or a Logistic/Henon conjugacy.
Declared source, cone and scale choices retain naturalness OPEN.
Classical symplectic, Hamiltonian, contact and quantum owners are
NOT APPLICABLE / NOT SUPPLIED. No natural A0 or formal Route is
evaluated.

## 2. SC23-BC: ambient delta does not determine its corner restriction

Let B be a finite nonempty set of derived atoms and let S_B be the
closed coordinate face of (2) supported on B. It is invariant under
the actual F and its inverse. Direct normalization gives, for r>=1,

\[
 (F_B^r(u))_b
 =\frac{b^{-r}u_b}{\sum_{d\in B}d^{-r}u_d}.
 \tag{3}
\]

Indeed, composing normalized positive diagonal maps cancels the
intermediate normalization. Writing s_j(u)=sum_(b in B)b^(-j)u_b,
the actual roof at F^j u is -log(s_(j+1)(u)/s_j(u)); hence its
r-step accumulated time is -log s_r(u), and is exactly r log a
at q_a. Thus (3) retains the actual repetition clock. Near a
vertex q_a use z_b=u_b for
b different from a, with u_a=1-sum z_b. The denominator equals
a^(-r) at that vertex. The numerator for each such b vanishes
there, so its derivative is diagonal:

\[
 D F_B^r(q_a)\big|_{\text{face coordinates}}
   =\operatorname{diag}_{b\in B\setminus\{a\}}((a/b)^r).
 \tag{4}
\]

This is the derivative of a smooth local ambient extension of the
actual finite-face formula. It does not assert a differentiable
manifold structure or a trace on the full completed section.

### 2.1 Exact two-atom return and the nonzero Jacobian

Take B={a,b}, a different from b, and z=u_b in [0,1] near q_a.
Writing lambda=(a/b)^r, which is positive and not one, (3) gives

\[
 f_r(z)=\frac{\lambda z}{1+(\lambda-1)z},\qquad
 h(z):=z-f_r(z)
  =\frac{(1-\lambda)z(1-z)}{1+(\lambda-1)z},\qquad
 d:=h'(0)=1-\lambda\ne0.
 \tag{5}
\]

Choose once a small delta>0 such that delta<1 and h' has the
constant sign of d on [0,delta]. Fix a smooth chi, supported in
[0,delta) on the half-line, with chi(0)=1. Thus its support meets
no other fixed point. The expression below is a local integral:
only this neighborhood is used, and the integrand is set to zero
outside the test support. Any extension of f_r farther away is
irrelevant.

Let psi be any nonnegative smooth compactly supported function on
R of integral one, and put delta_epsilon(y)=epsilon^(-1)psi(y/epsilon).
For every compactly supported smooth ambient test g,

\[
 \int_{\mathbb R}g(y)\delta_\epsilon(y)\,dy
    =\int_{\mathbb R}g(\epsilon t)\psi(t)\,dt
       \longrightarrow g(0).
 \tag{6}
\]

Uniform continuity on the compact support of psi proves this
limit. Symmetric and both one-sided choices therefore approximate
the same ambient delta distribution.

### 2.2 The half-line limit remembers a one-sided mass

The frozen corner prescription is

\[
 I_\epsilon(\psi)=\int_0^\infty
       \chi(z)\epsilon^{-1}\psi(h(z)/\epsilon)\,dz.
 \tag{7}
\]

For small epsilon the support of the integrand near zero lies in
the interval where h is one-to-one. Use y=abs(h(z))>=0 and let
z=z(y) be its inverse. With s=sign(d), substitute y=epsilon t:

\[
 I_\epsilon(\psi)
  =\int_0^\infty
       \frac{\chi(z(\epsilon t))}
            {|h'(z(\epsilon t))|}\psi(s t)\,dt
  \longrightarrow
  \frac{1}{|1-\lambda|}
       \int_0^\infty\psi(s t)\,dt.
 \tag{8}
\]

For sufficiently small epsilon this equality covers the entire
possible contribution: on a compact portion of the test support
away from zero, abs(h) has a positive minimum, while psi has compact
support. The prefactor converges uniformly on the bounded t interval
where psi(s t) can be nonzero, and h' is bounded away from zero.
This proves (8), including the absolute Jacobian and orientation.

Choose smooth unit-mass bumps psi_+ supported in (0,1),
psi_-(t)=psi_+(-t), and psi_sym=(psi_++psi_-)/2. For example
normalize exp(-1/((t-1/4)(3/4-t))) on (1/4,3/4), extended
by zero; its closed support [1/4,3/4] lies inside (0,1).

| Same fixed return and chi | psi_sym limit | psi_+ limit | psi_- limit |
| --- | --- | --- | --- |
| a<b, so lambda<1 and d>0 | 1/(2 abs(1-lambda)) | 1/abs(1-lambda) | 0 |
| a>b, so lambda>1 and d<0 | 1/(2 abs(1-lambda)) | 0 | 1/abs(1-lambda) |

All three ambient limits are (6); their restrictions (8) disagree.
For the explicit genuine face B={2,3} and r=1 at q_2,
lambda=2/3: the three numbers are 3/2, 3 and 0. No timing,
test cutoff or face was changed between these comparisons.

### 2.3 Controls and precise stop

A singleton face is one point; scalar pullback on its one-dimensional
function space is the identity and its finite-dimensional trace is
one. This elementary control has no transverse boundary variable and
cannot normalize the two-atom problem. It is not a trace on the
entire carrier.

On the same two-atom face, a test supported in its interior (0,1)
has h bounded away from zero on its compact support; the integral
is therefore zero for sufficiently small epsilon. No interior fixed
point was omitted from the corner calculation.

For an interior simple zero of a smooth h, integrating over both
sides of the zero instead gives the full mass
1/abs(h'(z_0)), independently of the same unit-mass psi. This follows
by the same change of variable, now over both positive and negative
y. The distinction is boundary restriction, not a failure of the
ambient approximate identity.

**Decision: STOP the unqualified ambient-delta diagonal prescription.**
The ambient distribution alone does not select among (8). Choosing
a boundary convention would be additional input for another card,
not a repair of this one. This does not say that the Radon measure
delta_0 cannot be restricted to the closed half-line: that restriction
is well-defined and retains its entire atom. The operation of first
restricting smooth approximants and then taking their limit need not
commute with taking the ambient limit first and restricting that
measure. The half-line indicator is discontinuous at the limiting
atom; ambient distribution convergence does not settle this extra
operation. No full-dimensional flat trace was defined,
no Lefschetz theorem was used, and no universal boundary-trace
impossibility was proved. The face dimension and transverse multipliers
also remain face-dependent; no infinite determinant is inferred.

## 3. SC23-LC: the completed carrier is nowhere locally compact

Here a compact neighborhood means a compact set containing an open
neighborhood of the specified point. Fix an arbitrary u in S_hat.
Every open neighborhood N of u contains a basic set

\[
 V=\{v\in\widehat S:p_{k_j}(v-u)<\delta_j,\ 1\le j\le m\}
 \tag{9}
\]

with finitely many norm constraints. We may take m>=1 by adding
an inessential p_0 constraint. Let K=max k_j. Derived atoms are
unbounded: were there only finitely many primes, a prime divisor of
one plus their product would contradict the list. Choose distinct
a_n tending to infinity and the positive rational weights

\[
 \epsilon_n=a_n^{-(K+1)},\qquad
 u_n=(1-\epsilon_n)u+\epsilon_n q_{a_n}.
 \tag{10}
\]

Every u_n belongs to the unchanged E, is nonnegative and has mass
one. This holds for arbitrary infinite-support u; only epsilon_n is
asserted rational, not all coordinates of u_n. For k<=K,

\[
 p_k(u_n-u)
  \le \epsilon_n(p_k(u)+a_n^k)
  \le p_k(u)a_n^{-(K+1)}+a_n^{-1}
   \longrightarrow0.
 \tag{11}
\]

Thus eventually every u_n belongs to V and N. Positivity gives,
in a higher continuous norm,

\[
 p_{K+2}(u_n)
  =(1-\epsilon_n)p_{K+2}(u)+\epsilon_n a_n^{K+2}
  \ge a_n\longrightarrow\infty.
 \tag{12}
\]

Any compact subset C of S_hat has bounded p_{K+2}: the norm is
continuous by the triangle inequality, its image is compact in R,
and the open intervals (-j,j) show that a compact real set is
bounded. If C were a compact neighborhood of u, choose N open
with u in N subset C. Equations (9)--(12) then put an unbounded
norm sequence in C, a contradiction. Since u was arbitrary,
S_hat is nowhere locally compact. This is not merely the statement
that one particular norm ball or the entire space is noncompact.

### 3.1 The quotient and transformation-groupoid arrow space

The proved [204 homeomorphism](../204-quotient-orbit-feature-hilbert/paper.md)
is

\[
 \widehat X\cong\widehat S\times(\mathbb R/\mathbb Z).
 \tag{13}
\]

It follows from the auxiliary real-power deck gauge, not from a
physical-time periodicity assumption. For each angle theta, the
slice S_hat times {theta} is closed. If a point in the product had
a compact neighborhood C, intersecting C with this slice would be
a compact neighborhood of its S_hat coordinate in the slice topology.
This contradicts the result above. Hence X_hat is nowhere locally
compact in exactly its original topology.

For the transformation groupoid R acting by the actual continuous
flow, the ordinary arrow topology is R times X_hat. A compact
neighborhood of any (t,x) would, by intersecting the closed slice
{t} times X_hat, yield a compact neighborhood of x. Thus this
arrow space too is nowhere locally compact. In particular the
closed zero-time unit slice cannot inherit local compactness from
a locally compact arrow space. These are topological statements,
not an invocation of a groupoid algebra or Haar-system theorem.

### 3.2 No nonzero continuous compactly supported scalar functions

Let f be continuous on X_hat and suppose its support, the closure
of its nonzero set, is compact. If f(x) is nonzero, put
eta=abs(f(x))/2. The set

\[
 C_f=\{y:|f(y)|\ge\eta\}
 \tag{14}
\]

is a closed subset of that compact support, hence compact. It
contains the open neighborhood {y:abs(f(y))>eta} of x. This
contradicts nowhere local compactness. Consequently

\[
 C_c(\widehat X)=\{0\}.
 \tag{15}
\]

The identical argument applies to S_hat and to the arrow space if
their continuous compact-support scalar functions are proposed. No assertion about
discontinuous, cylindrical, distributional or other test objects is
made.

**Decision: STOP the conventional locally compact Hausdorff /
compact-support starting contract on this exact full carrier.**
Each finite-coordinate closed face is an ordinary finite simplex
and is compact, but replacing the whole space by such a face changes
the owner. The tail proof uses only unbounded labels and the frozen
family of weighted norms; it is not an arithmetic-naturalness
obstruction. The existing 204 bounded continuous state-separating
Hilbert space and 209 covariance are compatible with (15), since
their nonzero observables were never required to have compact support.
General non-locally-compact groupoids, cylindrical function spaces,
proobjects and other distributional constructions remain undecided.

## 4. Separate relative heat-trace control

The following is a summary of the complete separate
[213 proof](../213-relative-periodic-heat-trace/paper.md), not a
new fourth contract or a transfer to 204 H. Its exact status is:

> CONTROL ADVANCE — RELATIVE PERIODIC-CHANNEL TRACE RECOVERS THE
> POSITIVE-TIME ORBIT COMB; FULL-STATE TRACE NOT SUPPLIED;
> NATURALNESS OPEN.

### 4.1 Genuine finite operator traces before any subtraction limit

Retain the full underlying flow (1), but use the explicit external
observation channel

\[
 H_{\rm per}=L^2(\widehat X,\mu),\qquad
 \mu=\sum_a w_a\lambda_a,\quad
 w_a=2^{-a}/\sum_b2^{-b},
 \tag{16}
\]

where lambda_a is normalized actual time on C_a. The
[205 classification and blindness result](../205-invariant-measure-support/paper.md)
remains a dependency: mixed states exist in the topology but (16)
does not distinguish every continuous observation of them.

For L=L_a use the actual circle R/(L Z), its covering physical-time
line, and

\[
 G_\epsilon(t)=(4\pi\epsilon)^{-1/2}e^{-t^2/(4\epsilon)},\qquad
 K_{\epsilon,L}(t)=\sum_{m\in\mathbb Z}G_\epsilon(t-mL).
 \tag{17}
\]

Let H_epsilon^L be convolution with the periodization on the circle,
H_epsilon^R convolution with G_epsilon on the line, and V_t actual
forward translation. The indicator chi_L of [0,L] is a line window.
The circle kernel is bounded on a finite period, so both half-heat
factors are Hilbert--Schmidt. On the line the factors
A=chi_L H_(epsilon/2)^R and B=V_t H_(epsilon/2)^R chi_L satisfy
norm(A)_HS^2=norm(B)_HS^2=L G_epsilon(0). Their product is exactly
the windowed operator. These are genuine trace-class products, not
formal diagonal integrals.

The absolutely integrable Hilbert--Schmidt product kernels give

\[
 \operatorname{Tr}(H_\epsilon^L V_t)
     =L\sum_{m\in\mathbb Z}G_\epsilon(t-mL),\qquad
 \operatorname{Tr}(\chi_L H_\epsilon^{\mathbb R}V_t\chi_L)
     =L G_\epsilon(t).
 \tag{18}
\]

The L factor is integration over one whole actual time circle.
The probability weights in (16) do not multiply operator traces:
constant changes of circle measure are unitarily intertwined.
The covering window uses this same circle's universal cover, not
an unrelated comparator.

### 4.2 Paired infinite limit and positive-time localization

At a finite integer cutoff N the prescribed difference is therefore

\[
 R_{\epsilon,N}(t)
   =\sum_{a\le N}L_a\sum_{m\ne0}G_\epsilon(t-mL_a).
 \tag{19}
\]

For abs(t)<=T and L>=max(2T+1,1), the proof gives

\[
 L\sum_{m\ne0}G_\epsilon(t-mL)
 \le\frac{L}{\sqrt{\pi\epsilon}}\,
       \frac{e^{-L^2/(16\epsilon)}}{1-e^{-L^2/(16\epsilon)}}.
 \tag{20}
\]

For fixed epsilon this is bounded by C_epsilon L exp(-L^2/(16epsilon));
for 0<epsilon<=1 it is bounded by C L exp(-L^2/32), uniformly in
that heat range. The exact all-integer comparison

\[
 \sum_a L_a e^{-cL_a^2}
 \le\sum_{n\ge2}(\log n)e^{-c(\log n)^2}<\infty
 \quad(c>0)
 \tag{21}
\]

needs no prime-distribution asymptotic. It proves local uniform
convergence in real t when N tends to infinity at fixed epsilon.
The finitely many small circles have their own summable winding
tails. The Gaussian approximate identity on each circle, together
with the uniform small-heat bound (20) for the atom tail, then gives

\[
 \lim_{\epsilon\downarrow0}\lim_{N\to\infty}
       \int h(t)R_{\epsilon,N}(t)\,dt
     =\sum_a\sum_{m\ge1}L_a h(mL_a),
 \qquad h\in C_c^\infty(0,\infty).
 \tag{22}
\]

This is the exact primitive-period-weighted repeat distribution on
open positive time. Its local finiteness follows from a<=exp(T)
and m<=T/log2 on a time support bounded by T. The coefficients
and repeats were derived from the actual circle-cover kernels;
no prime-power output weight was inserted into their definition.
The proof does not assert an extension to t=0, arbitrary joint
cutoffs, an Euler determinant or a continuation theorem.

### 4.3 Costs that localization does not remove

Each unpaired infinite sector diverges for every fixed epsilon>0
and real t: its block traces include the positive contribution
G_epsilon(t) sum_a L_a. Thus (22) is a prescribed relative scalar
limit of paired finite traces, not the ordinary trace or supertrace
of an infinite direct sum. The circle block direct sum is already
noncompact because the constants on different circles are orthonormal
fixed vectors.

Zero winding m=0 in (18) is not the Fourier constant mode k=0.
The former contributes L G_epsilon(t), whereas the latter contributes
one to a single circle's spectral trace. This subtraction is therefore
not the projected time filter stopped in Round22 SC22-PF.

Moving the cover window without changing its length and changing
the positive circle weights leave (18) unchanged. In contrast to
209's sampling-sensitive covariance, those controls do not alter
this trace; they also do not prove it intrinsic to every full-state
observation. The same heat argument works for generic period families
bounded away from zero with sum_j L_j exp(-cL_j^2)<infinity for
every c>0, including all integer logarithms. It localizes a supplied
circle family rather than selecting arithmetic atoms itself.

Finally, (22) does not repair the mixed-observation blindness of
(16). No heat operator on mixed directions, full-state kernel,
trace on exact 204 H or transport from (16) to that H is constructed.
Adding mutually canceling full-state summands would not prove
localization on them. The explicit control advances; its promotion
to an intrinsic full-state trace stops.

## 5. Portfolio decision and exact compatibility

| Question | Outcome | Remaining boundary |
| --- | --- | --- |
| 213 relative heat trace | CONTROL ADVANCE for (22) | External periodic channel; paired relative limit, not ordinary infinite-sector or full-state trace |
| SC23-BC, reserved 214 | STOP unqualified corner delta prescription | One-sided masses in (8) differ; separately declared boundary theories remain undecided |
| SC23-LC, reserved 215 | STOP conventional LCH/C_c starting contract | Exact full topology is nowhere locally compact; not a prohibition of every groupoid or observable space |

There is one substantive external representation-control package,
213, and two short screens. Neither reservation 214 nor 215 is
created, and this portfolio is an integration record, not an extra
candidate. No object is repaired after its decisive test.

There is no contradiction between 213's positive distributional limit
and C_c(X_hat)=0. Its compactly supported tests h live in physical
time (0,infinity), not on X_hat. Its circle and line heat kernels
belong to the declared external representation, not a local chart
of the whole completed carrier. Nor does BC reject the circle's
boundary-free periodic heat kernel: BC concerns a different,
precisely frozen corner prescription. The retained full-state H
and covariance of 204/209 remain valid at their prior boundaries.

The current gain is a correct relative localization benchmark plus
two precise full-carrier constraints. Intrinsic full-state trace
localization and arithmetic naturalness remain OPEN. A future
boundary prescription, non-locally-compact analytic construction or
full-state relative mechanism would need a new card and compatibility
proof. No such fourth line is opened here; zero-mass filtering on
exact 204 H is not re-evaluated.

## 6. Evidence, review and formal limits

Two separate read-only authors supplied the short proofs; one
different invocation reviews both final short arguments and portfolio
scope. Root owns 213 and its separate actual review. All calls inherit
model and visible context and are nonblind. This is not human peer
review, cross-model replication or independent-error evidence.
ARS contributes bounded CER and counterargument discipline only.

The [claim ledger](claim-ledger.md), [evidence index](evidence/README.md),
[combined actual review](evidence/review.md) and
[213 separate review](../213-relative-periodic-heat-trace/evidence/review.md)
record proof boundaries and actual bindings. Root alone owns
navigation and the sole integrated mechanical check. Links do not
certify a future check or supply Route credit.

All new infinite claims use explicit changes of variable, continuous
norm bounds, quotient topology or 213's all-integer Gaussian tails.
No numerical experiment, prime table, external theorem, changed
physical roof, borrowed determinant or fitted zero data supports
the conclusions. The abstract-level literature context in 213 is
not a premise or a claimed full-paper read here. Classical symplectic
and quantum owners are not supplied; formal Route coordinates stay
UNASSIGNED and Route B stays NOT INVOKED.
