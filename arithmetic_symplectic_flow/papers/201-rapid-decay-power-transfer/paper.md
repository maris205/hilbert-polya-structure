# Ordinary weighted-return determinants on the whole rapid-decay section

**Paper ID:** 201-rapid-decay-power-transfer  
**Candidate ID:** AQC-20260916-IPT01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — FULL COMPLETED-SECTION POWER REPRESENTATION AND ORDINARY FREDHOLM IDENTITY ON RE S > 1; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The entire rapid-decay positive-cone flow of 194 admits a declared
power-observable Hilbert representation of its actual first return.
Unlike the finite-section construction of 197, values at retained
infinite-support states are infinite series. We establish absolute
convergence, uniform coefficient-tail bounds, continuity in the
original completed topology, injectivity and separation of all states
before defining the Hilbert image. The true weighted composition
preserves that image on every state. For Re(s)>1 its ordinary power
traces generate the complete flow's unit-weight repetition series,
and its ordinary Fredholm determinant equals the inverse primitive-
orbit product. No infinite-support state or mixed state is removed.
The representation is parameter dependent, nonunital, not an algebra
and not all bounded continuous observables. A generic-alphabet control
leaves source-clock and representation naturalness OPEN. This is a
new analytic contract on 194, not an automatic transfer of 197's
theorem, a symplectic realization or a fixed physical Hilbert flow.
No continuation, target divisor or formal Route result is supplied.

## 1. Frozen identity, source lineage and exact question

The [version-1 card](candidate-card.md) preceded this proof under the
[Round20 scope](../203-completed-owner-analytic-frontier/candidate-card.md).
The question is whether the proposed observable representation works
on every state of the completed owner, with its actual topology and
return clock, and has an ordinary same-object determinant on the
frozen sufficient half-plane. It is not a new completion theorem or
a repair of a failed finite-section operator.

Start with the real finite-support monoid algebra of all positive
integers, with e_m e_n=e_(mn), and the nonunit span I. Products of two
nonunits span exactly the composite coordinate directions. Thus the
nonzero integer basis classes of Q=I/I^2 are precisely the prime
classes q_a. Write A for these derived atoms. This is a consequence
of all-integer multiplication, not a supplied prime table.

The geometric owner is exactly the one constructed and proved in
[194, Sections 2--5](../194-rapid-decay-cone-completion/paper.md):

\[
\begin{split}
 E&=\{v=(v_a):\|v\|_k=\sum_a a^k|v_a|<\infty
                      \text{ for every integer }k\ge0\},\\
 \widehat P&=\{v\in E:v_a\ge0\text{ for all }a,\ v\ne0\},\qquad
 (Dv)_a=a v_a,\\
 \widehat X&=\widehat P/\langle D\rangle,\qquad
 \phi_t[v]=[e^t v].
\end{split}
\tag{1}
\]

Use the full countable-family norm topology on E and its actual
subspace and quotient topologies. The full global unit-mass section is

\[
\begin{split}
 \widehat S&=\{u\in\widehat P:\sum_a u_a=1\},\qquad
 c(u)=\sum_a\frac{u_a}{a},\\
 F(u)_a&=\frac{u_a}{a c(u)},\qquad \tau(u)=-\log c(u).
\end{split}
\tag{2}
\]

All allowed finite and infinite supports remain. The exact dependencies
from 194 are its complete Hausdorff quotient flow, continuity of D and
its inverse in all norms, the embedded entire section with actual first
return (2), and the time-preserving full endpoint suspension. In
particular 0<c(u)<=1/2, tau>=log 2, and F is a homeomorphism with
inverse Du/sum_a a u_a. The all-norm condition makes that inverse
defined for every u. These are proved geometric dependencies, not
analytic results borrowed from 197.

| Same-object field | Frozen definition used here | Boundary |
| --- | --- | --- |
| Arithmetic source | All-integer multiplication and Q=I/I^2 | Atoms are derived, not selected from a table |
| Completed carrier | All of (1), with every weighted norm | No lone-norm or coordinate-product substitution |
| Flow and section | Original radial time and entire (2) | No support deletion or assigned prime roof |
| Observable representation | H_hat_s=J_s ell^2(A), constructed below | Complex observables on a real positive state space |
| Operator | c(u)^s f(Fu) with the actual return | Forward weighted composition, not an inverse-branch sum |
| Central analytic function | det_(H_hat_s)(I-L_s) | Ordinary determinant, sufficient domain Re(s)>1 |
| Later geometric or quantum owner | NOT SUPPLIED | No import of 196's conservative geometry |

The [prior-work guide](../../docs/prior_work/README.md) supplies the
lineage: proper-factor symbolic admissibility -> all-integer
multiplicative source -> indecomposable observable -> positive radial
geometry -> rapid-decay completion -> operator geometry for its actual
return. This is a specific algebraic replacement and completion of
the prime/composite symbolic seed, not chronological trial division
or a Logistic/Henon conjugacy. Its external-paper assertions are not
premises here. No global novelty or literature-completeness claim is
made. The choices of quotient, positivity, size and time remain
declared engineering; their naturalness is not settled by (1).

## 2. Infinite-state observables before a Hilbert-image claim

Fix s in C with sigma=Re(s)>1 and H=ell^2(A;C), with inner product
linear in its first argument. For x>0 define x^s=exp(s log x), using
the real logarithm, and put 0^s=0. The proposed functions are

\[
 J_s b(u)=\sum_{a\in A}b_a u_a^s,\qquad b\in H,
 \quad u\in\widehat S.
\tag{3}
\]

No assumption makes this sum finite. Let A_N={a in A:a<=N} and
b^(N) retain precisely those coefficients.

**Proposition 1 (whole-completion embedding).** Equation (3) converges
absolutely at every state and defines an injective norm-one linear
map H->C_b(S_hat). For each b its coefficient truncations converge
uniformly on the whole section. Its image separates every pair of
distinct states, including infinite-support states.

**Proof.** Because 0<=u_a<=1 and sum_a u_a=1, countable nonnegative
sums give

\[
 \sum_a |u_a^s|^2=\sum_a u_a^{2\sigma}\le1,
 \qquad
 \sum_a|b_a u_a^s|\le\|b\|_2.
\tag{4}
\]

The second inequality follows by applying Cauchy--Schwarz to finite
sets and taking their supremum, so it proves absolute convergence,
not just bounded formal partial sums. Applying the same argument to
the omitted coefficients gives the uniform bound

\[
 \sup_{u\in\widehat S}
 \left|J_s b(u)-\sum_{a\le N}b_a u_a^s\right|
 \le\left(\sum_{a>N}|b_a|^2\right)^{1/2}\longrightarrow0.
\tag{5}
\]

Each coordinate is continuous for the original topology, and x^s
extends continuously to zero. Thus (5) already proves continuity.
There is also a direct global estimate. On [0,1] the real-variable
derivative s x^(s-1) extends continuously by zero at zero, since
sigma>1, and has absolute value at most |s|. Consequently
\(|x^s-y^s|\le |s|\,|x-y|\). The difference of the two absolutely convergent
sums in (3) satisfies

\[
 |J_s b(u)-J_s b(v)|
 \le |s|\,\|b\|_2
       \left(\sum_a|u_a-v_a|^2\right)^{1/2}
 \le |s|\,\|b\|_2\|u-v\|_0.
\tag{6}
\]

Every countable step follows from the finite-set estimate and (4).
The zero-th norm is continuous in the frozen all-norm topology, so
this does not replace that topology by a weaker one.

At each singleton q_a, J_s b(q_a)=b_a. Hence the map is injective.
Taking b to be a coordinate unit vector gives equality in its norm
bound, so its norm into C_b is one. For u different from v, some
coordinate u_a differs from v_a; then u_a^s differs from v_a^s
because their moduli u_a^sigma and v_a^sigma differ. The image of
that coordinate unit vector separates them, regardless of either
support being infinite. QED.

Only after this injection define H_hat_s=J_s H, with transported
inner product and norm. The map J_s is now a unitary map from H
onto this image by definition. It makes the image complete in its
Hilbert norm; no C_b-closedness or change to S_hat is claimed.
Finite coefficient sums are dense in that Hilbert norm, and (5)
also gives their uniform convergence as actual functions.

The distinction between coefficient tails and state tails matters.
Equation (5) is uniform in u for each fixed b. It does not say the
maps J_s b^(N) converge to J_s in operator norm: with a>N, b a
coordinate unit vector and u=q_a, the error is one. Nor is a uniform
two-variable kernel truncation asserted below.

**Proposition 2 (whole-state kernel and representation boundaries).**
The image is a reproducing-kernel Hilbert space on all S_hat, with

\[
 K_s(u,v)=\sum_a u_a^s\overline{v_a^s},\qquad
 \|\operatorname{ev}_u\|
       =\left(\sum_a u_a^{2\sigma}\right)^{1/2}\le1.
\tag{7}
\]

It contains no nonzero constant, is not closed under pointwise
products, and is not all C_b(S_hat). For distinct s,t with both
real parts greater than one, H_hat_s and H_hat_t are distinct sets
of functions on this same section.

**Proof.** For an infinite-support v the coefficient vector
(overline(v_a^s))_a need not be finite. It belongs to H by (4).
Cauchy--Schwarz proves absolute convergence of (7). Its function is
J_s of that coefficient vector, so the first-linear inner-product
convention gives

    <J_s b, K_s(.,v)> = sum_a b_a v_a^s = J_s b(v).

The same coefficient vector gives the exact evaluation norm in (7).
Its finite coefficient approximations converge uniformly in u by
(5), with v fixed; no uniformity over all v is needed.

If J_s b equals a constant C, singleton evaluation forces b_a=C for
every atom. There are infinitely many atoms: the elementary product-
plus-one argument rules out a finite list of primes. Square summability
therefore forces C=0, and the bounded continuous function 1 is absent.
For a different from d, the two image functions u_a^s and u_d^s
have a product vanishing at every singleton, but not at
(q_a+q_d)/2. Any image function vanishing at all singletons has all
coefficients zero, so this product is not in H_hat_s.

If the function u_a^s were in H_hat_t, its singleton values would
force its H_hat_t coefficients to be the same coordinate unit vector.
It would equal u_a^t on every state. Along a two-atom edge this says
x^s=x^t for every 0<x<1. Thus exp((s-t)y)=1 on a real interval of
y=log x, which by differentiation implies s=t, a contradiction.
QED.

These are point-separating but constrained observables: every mixed
and infinite-state value is determined by the singleton coefficient
values through the convergent series (3). A fixed abstract coefficient
space does not give a fixed physical observable space for the flow.
Complex coefficients are not a complexification of the state cone.

## 3. Actual return invariance on every infinite support

Use precisely the real first return of (2):

\[
 \mathcal L_s f(u)=e^{-s\tau(u)} f(Fu)=c(u)^s f(Fu).
\tag{8}
\]

This is bounded on C_b(S_hat), with norm at most 2^(-sigma), since
F and c^s are continuous. The present contract is its restriction
to H_hat_s, not a compactness claim for the whole C_b space.

**Proposition 3 (true completed-state intertwining).** H_hat_s is
invariant under (8), and on every u in the full S_hat,

\[
 \mathcal L_s J_s b=J_s T_s b,
 \qquad (T_s b)_a=a^{-s}b_a.
\tag{9}
\]

Thus L_s is an everywhere-defined bounded Hilbert operator, unitarily
represented by T_s, with norm 2^(-sigma).

**Proof.** First take a finite coefficient truncation, but do not
truncate the state or replace its full c(u). All its positive terms
use real logarithms, so

\[
 c(u)^s\sum_{a\le N}b_a
          \left(\frac{u_a}{a c(u)}\right)^s
       =\sum_{a\le N} a^{-s}b_a u_a^s.
\tag{10}
\]

Zero-coordinate terms agree by 0^s=0. For an infinite-support u,
both full series are absolutely convergent by (4), applied at Fu
on the left and with T_s b on the right. More strongly, (5) and
the bound on (8) show that the omitted left side in (10) is at
most 2^(-sigma) times the ell^2 norm of the coefficient tail,
uniformly on S_hat. The right side has the same bound because
the multiplier a^(-s) has norm 2^(-sigma). Letting N tend to
infinity proves (9) on the entire carrier, even uniformly for
each fixed b. The multiplier norm is attained at the derived atom
2, proving the claimed operator norm. Invariance and identification
precede every trace assertion. QED.

The genuine r-return law is also retained. For r>=1 put
c_r(u)=sum_a u_a a^(-r), and c_0(u)=1. Each sum is positive and
convergent, and c_r(u)<=2^(-r). Induction in (2) gives

\[
 F^r(u)_a=\frac{a^{-r}u_a}{c_r(u)},\qquad
 c(F^j u)=\frac{c_{j+1}(u)}{c_j(u)},\qquad
 \sum_{j=0}^{r-1}\tau(F^j u)=-\log c_r(u).
\tag{11}
\]

All sums here involve the full state, with no finite-support step.
The ratios are positive, so telescoping real logarithms is valid.
Consequently L_s^r f(u)=c_r(u)^s f(F^r u), the actual multiple-
return rule. On mixed states this is not generally r times a
constant roof.

For a concrete retained infinite state let
v_*=lim_N sum_(n=2)^N exp(-n)q_n and u_*=v_*/sum_a exp(-a).
The bound sum_(n>=2)n^k exp(-n)<infinity puts it in E for every
k, and its derived atom support is infinite. Both c(u_*) and
J_s b(u_*) use the infinite formulas above; for example b_a=a^(-1)
belongs to H and gives genuinely infinitely many nonzero summands.
Equation (10) with its uniform tail proof applies without replacing
u_* by a favorable finite state. For the two-atom control
u=(q_2+q_3)/2, c(u)=5/12, Fu=(3q_2+2q_3)/5 and
L_s(u_2^s)(u)=(5/12)^s(3/5)^s=4^(-s), as (9) requires.

For the normalized-state truncation control, put
delta_k(N)=sum_(a>N) a^k u_a and, once delta_0(N)<1, let
u^(N)=sum_(a<=N) u_a q_a/(1-delta_0(N)). Directly,

    ||u^(N)-u||_k = delta_k(N)
       + delta_0(N)/(1-delta_0(N)) sum_(a<=N) a^k u_a -> 0.

This verifies dense finite support in every original weighted norm,
in agreement with 194. After the full-state continuity and invariance
proof, restriction to that dense section gives exactly 197's J_s
formula, hence its unique continuous extension for each b. This is
a consequence, not automatic transport of 197's analytic theorem.

## 4. Ordinary traces and determinant in the sufficient half-plane

Let e_a be the standard orthonormal coefficient basis, P_a its rank-
one orthogonal projection, and lambda_a=a^(-s). Having proved (9),
we may now use

\[
 T_s=\sum_a \lambda_a P_a,\qquad
 \sum_a|\lambda_a|=\sum_a a^{-\sigma}
       \le\sum_{n=2}^{\infty}n^{-\sigma}<\infty.
\tag{12}
\]

The last sum converges by the elementary integral bound. Finite-rank
partial sums converge in trace norm; equivalently, T_s^*T_s has
diagonal entries a^(-2 sigma), so its singular values are a^(-sigma).
This proves ordinary Hilbert trace class and transports it to L_s
on H_hat_s by (9), not by analogy with a finite-section theorem.

The trace is basis independent here for an explicit reason. For any
orthonormal basis (v_j), Parseval and nonnegative summation give

\[
 \sum_{j,a}|\lambda_a|\,|\langle v_j,e_a\rangle|^2
       =\sum_a|\lambda_a|<\infty.
\tag{13}
\]

Absolute convergence therefore allows interchanging the diagonal
trace sums, yielding tr(T_s)=sum_a lambda_a. Apply the same argument
to every power and transport under J_s to obtain

\[
 \operatorname{tr}_{\widehat H_s}(\mathcal L_s^r)=\sum_a a^{-rs},
 \qquad
 \|\mathcal L_s^r\|_1=\sum_a a^{-r\sigma},\quad r\ge1.
\tag{14}
\]

For the integer arithmetic threshold N>=2, the trace-norm tail is bounded by

\[
 \sum_{a>N}a^{-\sigma}
       \le\sum_{n>N}n^{-\sigma}
       \le\frac{N^{1-\sigma}}{\sigma-1}.
\tag{15}
\]

This operator tail differs from the coefficient-observable tail in
(5). Neither is a finite numerical inference about the entire flow.

The ordinary Fredholm determinant can be constructed through its
exterior-power series. The k-th exterior power of T_s is diagonal
on e_(a_1) wedge ... wedge e_(a_k), a_1<...<a_k, with entries
lambda_(a_1)...lambda_(a_k). Their absolute sum is at most
(sum_a |lambda_a|)^k/k!. Thus its determinant series converges
absolutely and agrees with the finite-rank product limit:

\[
\begin{split}
 D_{201}(s)&=\det_{\widehat H_s}(I-\mathcal L_s)
      =\sum_{k\ge0}(-1)^k\operatorname{tr}(\wedge^k T_s)\\
      &=\prod_a(1-a^{-s})
       =\exp\left(-\sum_{r\ge1}\frac1r\sum_a a^{-rs}\right).
\end{split}
\tag{16}
\]

The k=0 term is one. The product and exponential comparison is
legitimate because |a^(-s)|<=2^(-sigma)<1 and

\[
 \sum_{a,r\ge1}\frac{a^{-r\sigma}}r
       \le \frac{1}{1-2^{-\sigma}}\sum_a a^{-\sigma}<\infty.
\tag{17}
\]

The power-series logarithm of each factor can therefore be summed
absolutely, with no ambiguous branch selection. Every compact subset
of Re(s)>1 has a common lower real-part bound sigma_0>1; (12) and
(17) with sigma_0 give local uniform convergence. Thus the scalar
function (16) is holomorphic and nonzero on this half-plane and tends
to one as real s tends to positive infinity. This is an analytic
scalar family despite the physical spaces depending on s; it is
not a fixed physical Hilbert-flow assertion. No sharp convergence
boundary, regularized determinant or continuation is asserted.

## 5. The completed owner's full ledger and the typed orbit identity

For a full v in P_hat, a return of [v] at time t means

\[
 e^t v=D^j v\quad\text{for one common integer }j.
\tag{18}
\]

At every positive coordinate this requires e^t=a^j. If j=0 then
t=0. If j is nonzero, distinct positive atoms have distinct j-th
powers. Hence every mixed state, including every infinite support,
has trivial time stabilizer. This is a direct all-coordinate proof,
not a finite-truncation periodic census. A singleton support a has
stabilizer (log a)Z. All positive amplitudes on that support are
connected by the actual radial flow, so they give exactly one
primitive oriented circle gamma_a, with least time log a and all
positive repeats r log a. Every state is covered by these cases.
There are no other closed or stationary packets. This also directly
checks the exact all-support ledger of 194 used by this representation.

Equation (11) gives the equivalent section test: F^r u=u forces
a^(-r)=c_r(u) on every positive coordinate, so only the singleton
q_a returns. Its primitive return number is one. Define the flow's
unit-weight repetition logarithm and primitive product by

\[
\begin{split}
 \log Z_{\widehat X}(s)
   &=\sum_{\gamma\ \mathrm{primitive}}\sum_{r\ge1}
             \frac{e^{-srT_\gamma}}r
     =\sum_a\sum_{r\ge1}\frac{a^{-rs}}r,\\
 Z_{\widehat X}(s)&=\prod_a(1-a^{-s})^{-1}.
\end{split}
\tag{19}
\]

Equation (17) proves convergence and fixes the logarithm used here.
Combining the separately established full-state operator and complete
geometric ledger gives exactly

\[
 \log Z_{\widehat X}(s)
       =\sum_{r\ge1}\frac{\operatorname{tr}_{\widehat H_s}
                                  (\mathcal L_s^r)}r,
 \qquad
 \det_{\widehat H_s}(I-\mathcal L_s)
       =Z_{\widehat X}(s)^{-1},\quad\Re(s)>1.
\tag{20}
\]

The traces, logarithm and product are distinct objects with the
relations displayed in (20); no individual power trace is equated
with a product. Unit weights and 1/r count the actual repetitions,
without added stability factors or von Mangoldt weights. Every
intrinsic primitive orbit is included. Infinite mixed states do not
supply missing orbit terms because they do not close, not because
the representation deleted them. The proof is a direct comparison
of this representation with this completed flow, not an invocation
of an unproved geometric fixed-point trace formula.

## 6. Controls and adverse boundaries

| Control or objection | Exact result | Remaining boundary |
| --- | --- | --- |
| Infinite-state values and return | Absolute bounds (4), uniform coefficient tails (5), full-state (10) and explicit u_* | No pointwise-finite argument substitutes for infinite support |
| Original topology | Global estimate (6) and normalized positive truncations in every norm | Neither state topology nor physical carrier is changed |
| Observable truncation versus operator truncation | Equation (5) is for each fixed b; equation (15) is an operator trace-norm tail | J_s coefficient truncations do not converge in operator norm |
| Change tau to a unit roof while keeping F and J_s | On u_2^s the changed rule is e^(-s)2^(-s)c(u)^(-s)u_2^s | The nonconstant cancellation (10) uses the actual roof; a unit roof is a different owner |
| Nonzero constants and cross-coordinate products | Proposition 2 excludes both | Nonunital, not an algebra, proper subspace of C_b |
| Change s | Proposition 2 proves different physical function spaces | A fixed abstract H does not supply a fixed physical Hilbert flow or generator |
| Add conservative geometry | No such construction occurs in this package | No operator or trace is credited to 196 |
| Generic free commutative alphabet | Distinct generator multipliers lambda_j>=2 with explicit summability give the same mechanism | PROVES_TOO_MUCH for a claim of unique arithmetic naturalness |

For the final control take a countably generated free commutative
monoid with a declared multiplicative norm whose distinct generator
values are lambda_j>=2. Form its indecomposable quotient and complete
under all weights lambda_j^k. The positive cone, size map, normalization
and real clock have the same explicit formulas with a replaced by
lambda_j. The all-coordinate return equation again gives one circle
of length log lambda_j per generator, and (4)--(11) use only positive
mass and that size law. Ordinary traces additionally require
sum_j lambda_j^(-sigma)<infinity; this condition is not implicit for
an arbitrary dense alphabet. For a full half-plane example, choose
lambda_j=j+1. Then the integer-series comparison holds for every
sigma>1, although composite as well as prime numerical values label
the generators. This is a changed-source control, not a change to
the frozen integer multiplication of the main candidate. Equal
multipliers would instead allow mixed recurrent directions and
would invalidate the one-generator-one-circle packet comparison.

Thus a useful exact operator identity does not force the source,
I/I^2 quotient, positivity, rapid-decay topology, size law, radial
speed or coordinate-power Hilbert norm. Their naturalness remains
OPEN. No prime-counting asymptotic, target zeros or fitted arithmetic
data are needed for the positive theorem, and none can be inferred
from it. Point separation is not a claim to represent every observable.

## 7. Gate assessment and decision

| Obligation | Evidence for this exact analytic extension | Status / limit |
| --- | --- | --- |
| T0 full carrier and representation ownership | Entire 194 owner, Propositions 1--3 on all S_hat | ESTABLISHED for the declared completed AQC category |
| T1-style source and clock | All-integer quotient and actual (2) | Scoped mechanism retained; naturalness OPEN |
| T2 whole packets and repetitions | Direct equation (18) and Section 5 | ESTABLISHED for all finite and infinite supports |
| T3 ordinary operator and analytic identity | Equations (12)--(20) | ESTABLISHED for H_hat_s on Re(s)>1 only |
| Classical symplectic A0--A2 | No such carrier or symplectic form supplied | NOT APPLICABLE; no natural-A0 or formal A2 pass |
| Formal Route coordinates / Route B | No formal evaluation or readiness contract invoked | UNASSIGNED / NOT INVOKED |

Decision: ADVANCE this bounded completed-section analytic contract.
The actual weighted return is ordinary trace class in its declared
Hilbert representation. Its power traces generate the full completed
flow's unit-weight repetition logarithm, and its ordinary Fredholm
determinant equals the inverse primitive-orbit product,
det(I-L_s)=Z_Xhat(s)^(-1), for Re(s)>1. Stop this contract at that
result. Another norm, a fixed physical Hilbert flow, continuation,
target divisor or conservative lift requires its own authorization
and frozen obligation. Naturalness stays OPEN; the existence of the
representation supplies no formal Route credit.

## Evidence and reproducibility

The [card](candidate-card.md) fixes the exact inputs, the
[claim ledger](claim-ledger.md) identifies each proof and limit, and
the [evidence index](evidence/README.md) records actual review and
integration receipts separately. The methods are finite-set estimates
followed by absolute or uniform infinite limits, all-coordinate return
equations, singular-value sums and exterior-power determinant limits.
All infinite assertions have exact bounds or proofs. There is no
numerical experiment, finite precision, prime table, fitted parameter,
script or external theorem with unchecked hypotheses.

ARS is used only for bounded claim/evidence/reasoning and counterargument
discipline under the approved question. Author and separate reviewer
share inherited context and model settings; this is nonblind model
work, not human peer review, a venue assessment or an independent-error
certificate. No full ARS publication pipeline is claimed.
