# Unit-group exterior weighting retains local prime returns but has no full ordinary trace

**Paper ID:** 166-unit-exterior-weighted-trace  
**Candidate ID:** ANG-20260915-UEW01  
**Date:** 2026-09-15  
**Status:** STOP — LOCAL RANK-ONE SURVIVAL; FULL DEGREE-WEIGHTED ORDINARY TRACE UNDEFINED.  
**Route state:** Broadened owner audit only; formal coordinates UNASSIGNED;
Route B NOT INVOKED.

## Abstract

Over every actual localization Z[1/n], we freeze a full unit-group
exterior cochain complex with smooth invariant-function coefficients.
Its original real translation action is smoothed by one uniform Gaussian;
the exterior degree is weighted by its integer degree with alternating
sign. This differs from the stopped two-degree basic de Rham contract:
on any finite set of components the new weighting retains each rank-one
circle's actual logarithmic return trace and cancels the higher-rank
component traces. Nevertheless, the complete degree-one action has
infinitely many orthonormal fixed channels. The maximal direct-sum
weighted operator is closed and densely defined but is in fact unbounded
over arbitrarily large unit ranks. It has no ordinary Hilbert trace.
Even finite-component weighted traces diverge to negative infinity along
every complete exhaustion at fixed positive smoothing. These exact
obstructions stop this contract; no relative trace, torsion or changed
order of limits is installed as a repair.

## 1. Candidate identity and same-object ledger

The [version-1 card](candidate-card.md) was frozen before this audit.
Let I consist of all distinct actual subrings A_n=Z[1/n] of Q, n>=2.
For each such ring define

\[
E_n=\{d\ge1:d\mid n^k\text{ for some }k\ge0\},\qquad
U_A=\{q\in\mathbb Q_{>0}:qA=A\}.
\tag{1}
\]

Objects are (A,u), u in R. Arrows (A,u,q), q in U_A, send u to
u+log q; composition multiplies q. Unit and ring indices are discrete.
Time translates u to u+t on objects and arrows. No roof is inserted.
The full carrier, not just its rank-one components, is retained.

| Item | Frozen owner | Boundary |
| --- | --- | --- |
| Arithmetic source | All integers, divisibility, E_n, actual rings and units | No prime-selected index or external prime table |
| Lineage | Divisor symbols -> power-saturated denominator language -> unit action | A stated source replacement, not chronological sieve conjugacy |
| Clock and returns | Original real translation and all closures up to unit arrows | Not ordinary point isotropy |
| Analytic coefficients | All smooth invariant functions B_A | Not a faithful encoding of every mixed-component return |
| Exterior complex | B_A tensor exterior powers of Hom_Z(U_A,C), differential zero | Unit-group coefficient complex, not basic de Rham |
| Norm and operator | Uniform mean, unweighted direct sum, uniform Gaussian, degree j | No component damping or later normalization change |
| Classical geometry | NOT APPLICABLE | No symplectic map, roof or mapping torus claimed |
| Future quantum owner | DEFERRED | No Route-B inference |

The nearest antecedents are the
[full localization action of 146](../146-localization-scaling-groupoid/paper.md)
and the [basic-complex audit of 158](../158-localization-koszul-packet-audit/paper.md).
This is a new analytic contract, not a new carrier and not an alteration
of either earlier record.

## 2. Question, source lineage and nonclaims

The bounded question is whether degree-weighting the full unit exterior
algebra improves 158's local cancellation while supplying a genuine
ordinary trace on the full Hilbert direct sum.

The answer separates two issues. Finite-component rank-one survival is
proved. Full ordinary trace existence fails. A finite-dimensional
binomial identity is not promoted to a global trace.

The [prior-work lineage](../../docs/prior_work/README.md) is realized through

\[
1_{\{d\mid n\}}\longrightarrow
1_{\{d\mid n^k\text{ for some }k\}}
\longrightarrow A_n\longrightarrow U_{A_n}\curvearrowright\mathbb R.
\tag{2}
\]

Power-saturation forgets prime versus prime-power labels intentionally;
actual ring equality then removes those duplicate labels. It does not
supply the sequential source's chronological recurrence. This broadened
ANG contract does not claim a Logistic/Hénon geometric lift.

We claim neither full groupoid cohomology nor faithfulness of the chosen
coefficient representation. In particular, the Gaussian is smoothing
in the time direction, not the Laplacian of our zero-differential complex.
No analytic torsion, ordinary determinant, Euler product, continuation,
target divisor, Riemann-zero match or formal Route result is constructed.

## 3. Exact complex, Hilbert space and operator domain

Define

\[
B_A=\{f\in C^\infty(\mathbb R;\mathbb C):
f(u+\log q)=f(u)\text{ for every }q\in U_A\},\qquad
V_A=\operatorname{Hom}_{\mathbb Z}(U_A,\mathbb C).
\]

The unit group acts trivially on B_A by this invariance. The smooth
cochain complex and coefficient norm are

\[
C_A^j=B_A\otimes\Lambda^j V_A,\quad d=0,\qquad
\|f\|_A^2=\lim_{R\to\infty}\frac1{2R}\int_{-R}^R|f(u)|^2\,du.
\tag{3}
\]

The integer monoid U_A intersect Z_{>=1} has its multiplicatively
irreducible elements P_A, excluding 1. Use their dual basis in V_A
as orthonormal, with the induced exterior norm. Proposition 1 proves
that this is well-defined. Write H_A for the coefficient completion.
The full Hilbert space is

\[
H=\bigoplus_{A\in I}\bigoplus_{j\ge0}H_A\otimes\Lambda^j V_A.
\tag{4}
\]

For epsilon>0 and t in R define

\[
g_\epsilon(v)=(4\pi\epsilon)^{-1/2}e^{-v^2/(4\epsilon)},\quad
Q_\epsilon f(u)=\int_\mathbb R g_\epsilon(v)f(u+v)\,dv,\quad
V_t f(u)=f(u+t),\quad R_{A,\epsilon,t}=Q_\epsilon V_t.
\tag{5}
\]

Only the coefficient factor carries this action. The exterior factor
is the identity because time translation does not change any unit.
Let R denote the resulting bounded full direct-sum action. The weighted
operator has blocks W_{A,j}=(-1)^j j(R_A tensor I) and maximal domain

\[
W_{\epsilon,t}=\bigoplus_{A,j}W_{A,j},\qquad
D(W_{\epsilon,t})=
\left\{\eta\in H:
\sum_{A,j}j^2\|(R_A\otimes I)\eta_{A,j}\|^2<\infty\right\}.
\tag{6}
\]

The proposed ordinary trace means the ordinary Hilbert trace of this
actual operator, only if it is trace class. Separate degree traces
likewise require ordinary existence before any weighted summation.
No generalized supertrace or infinity-minus-infinity rule is implicit.

## 4. Exact derivation and the first global stop

### Proposition 1 — Full carrier, coefficient norm and unit complex

For every A, its unit group is free abelian of finite rank r_A>=1.
The set P_A is exactly the prime support of A, derived from the all-ring
input. If r_A=1 and P_A={p}, then H_A=L^2(R/(log p)Z,du/log p).
If r_A>=2, then H_A=C. The complex (3) is the Koszul cochain model
for U_A with its displayed trivial coefficients.

**Proof.** A denominator divides a power of n exactly when all its prime
divisors divide n. Hence 1/p lies in A_n exactly for primes dividing n.
This proves equality of actual localizations is equality of finite
prime supports. Further, qA=A if and only if both q and q inverse
belong to A. Reduced numerator and denominator therefore give

\[
U_A=\left\{\prod_{p\in S(A)}p^{m_p}:m_p\in\mathbb Z\right\}.
\tag{7}
\]

Unique factorization identifies the integer monoid's irreducibles with
S(A) and proves freeness. The exterior metric in the card is therefore
defined without a selected prime support or a per-prime coefficient.

The arrows compose and invert as translations, and are étale on each
fixed unit-label line. Ordinary point isotropy is trivial: log q=0
implies q=1. The time-return group up to arrows is log U_A.
In rank one it is (log p)Z, so the coarse component is one circle with
least positive time log p and repetitions m log p.

For distinct primes p,q, log p/log q is irrational, since a rational
relation would identify positive powers of different primes. Applying
the pigeonhole principle to multiples of this ratio modulo one gives
arbitrarily small nonzero integer combinations of log p and log q.
Their integer multiples prove density of log U_A at higher rank.
The group is countable and proper, with no least positive return.

Thus B_A consists of smooth periodic functions in rank one and constants
at higher rank. On periodic functions, splitting a symmetric long
interval into complete periods and a bounded remainder proves the mean
in (3) is normalized period integration. On constants it is absolute
value squared. This proves the stated positive-definite completions.
All A remain present; the invariant representation loses detailed
higher-rank return information, not the carrier itself.

For the cochain interpretation, order the finite set P_A only to write
coordinates. The group algebra is the Laurent ring
R_A=C[z_1^{+/-1},...,z_r^{+/-1}]. In one variable, multiplication by
z-1 is injective, its cokernel is evaluation at 1, and
(f(z)-f(1))/(z-1) is a Laurent polynomial. This gives the split
augmented resolution as complex vector spaces. Tensoring its r copies
over C gives an exact free R_A resolution of the augmentation module,
with degree-j rank binom(r,j) and Koszul differential built from z_i-1.
Applying Hom over R_A into B_A makes each z_i-1 act as zero. The
cochain differential is therefore zero, with spaces B_A tensor
Lambda^j V_A as in (3). Reordering the basis induces the usual exterior
identification and leaves the norm unchanged. This supplies the claimed
unit-group model; it is not an assertion about every groupoid cochain.
QED.

### Proposition 2 — Owned smoothing and finite-component rank selection

The operator R is a contraction on H. For a rank-one component with
L=log p the coefficient action is trace class and has trace

\[
\Theta_{L,\epsilon}(t)
=\sum_{m\in\mathbb Z}e^{-\epsilon(2\pi m/L)^2}e^{2\pi i mt/L}
=L\sum_{k\in\mathbb Z}g_\epsilon(t-kL).
\tag{8}
\]

Its distributional limit for this fixed L is
L sum_k delta_(kL) as epsilon decreases to zero. At higher rank the
coefficient trace is 1. Every single-component weighted operator is
trace class and

\[
\operatorname{Tr}W_A=
\begin{cases}
-\Theta_{\log p,\epsilon}(t),&r_A=1,\ P_A=\{p\},\\
0,&r_A\ge2.
\end{cases}
\tag{9}
\]

**Proof.** The normalized circle Fourier basis is exp(2 pi i m u/L).
Translation acts by a unit-modulus multiplier and Gaussian convolution
by exp(-epsilon(2 pi m/L)^2). The Gaussian transform can be derived
by differentiating its integral in frequency and integrating by parts:
its transform F satisfies F'(xi)=-2 epsilon xi F(xi), F(0)=1.
The multipliers prove the uniform contraction bound. Constants are
fixed, giving the higher-rank assertion. The circle multipliers are
absolutely summable for each fixed L and epsilon>0.

Periodizing g_epsilon has Fourier coefficient
L inverse times exp(-epsilon(2 pi m/L)^2). Multiplication by L proves
the second equality in (8). The Gaussian approximate-identity limit
gives the stated comb: on a compactly supported test function only
finitely many lattice sites are nearby, and the other Gaussian tails
are summably bounded and tend to zero. The coefficient L is thus
derived from the original time action, not inserted as an arithmetic
weight.

Each exterior power is finite dimensional with dimension binom(r,j).
For the polynomial (1-z)^r, evaluating z times its derivative at z=1
gives

\[
\sum_{j=0}^r(-1)^j j\binom rj
=\begin{cases}-1,&r=1,\\0,&r\ge2.\end{cases}
\tag{10}
\]

This is a finite trace calculation because each component action is
trace class in every degree. Multiplying its coefficient trace by
(10) proves (9). In contrast, the unweighted exterior sum is zero
for every r>=1. QED.

Equation (9) is a genuine finite-component improvement over 158's
basic de Rham pairing. It is not a deletion of mixed-support components,
an equality of their original return ledgers, or a global ordinary trace.

### Proposition 3 — Closed operator, infinite fixed channels and global failure

For every epsilon>0 and real t, (6) defines a densely defined closed
operator. Its degree-one restriction is bounded but not compact.
The full operator W is unbounded and has no ordinary Hilbert trace.

**Proof.** Each block W_{A,j} is bounded. Vectors with finite component
and degree support belong to (6) and are dense in H. If eta_n tends
to eta in H and W eta_n tends to zeta in H, projecting onto each block
gives zeta_{A,j}=W_{A,j} eta_{A,j}. The square-summability of zeta
then puts eta in the displayed maximal domain and proves W eta=zeta.
This proves that W is closed on the displayed maximal domain.

For every distinct prime p, take e_p to be coefficient 1 tensored
with the unit dual basis vector in degree 1 on A=Z[1/p], and zero
elsewhere. These are orthonormal in H. Both translation and Gaussian
smoothing fix the coefficient 1, so

\[
W_{\epsilon,t}e_p=-e_p.
\tag{11}
\]

There are infinitely many primes: a prime divisor of one plus the
product of any proposed finite list is absent from that list.
The images in (11) have no convergent subsequence. Thus the degree-one
block is not compact and cannot be trace class. This is already the
decisive failure of the precommitted ordinary-trace contract. Even
a hypothetical bounded full trace-class operator could not have this
noncompact compression to a closed invariant degree subspace.

There are also actual components of every finite rank r, by taking
the localization of a product of r distinct primes. The unit-norm
constant coefficient tensored with the top exterior basis vector
belongs to (6) and has W-image norm r. Hence W is unbounded on its
unit vectors. Ordinary Hilbert trace-class operators are bounded,
so the full W is not trace class independently of (11). QED.

The global analytic contract stops here. Its negative result does not
depend on a truncation, a numerical precision, or a choice of enumeration.

### Proposition 4 — The precommitted finite-cutoff control does not repair the trace

Let F range over finite subsets of I. At any fixed epsilon>0 and real t,

\[
\operatorname{Tr}W_F
=-\sum_{\{p:\ \mathbb Z[1/p]\in F\}}\Theta_{\log p,\epsilon}(t).
\tag{12}
\]

Along every increasing exhaustion of all I, these real numbers tend
to negative infinity.

**Proof.** Finite direct sums permit ordinary trace addition, so (9)
gives (12). The second formula in (8) is positive and its k=0 term
gives

\[
\Theta_{\log p,\epsilon}(t)\ge(\log p)g_\epsilon(t)
\ge(\log2)g_\epsilon(t)>0.
\]

Every exhaustion includes arbitrarily many distinct rank-one components.
Equation (12) therefore tends to negative infinity. No conditionally
reordered cancellation is involved. QED.

This is only the finite-cutoff control stated before the audit, not
a new regularization proposal. Changing the order of the smoothing
and component limits, subtracting a zero-time term, or defining a
relative distribution would change the analytic requirement and
receives no existence or zeta claim here.

## 5. Results and representation boundary

The same original action supplies the coefficient time trace. In a
single rank-one component its returns are exactly m log p, with the
normalization in (8). Full exterior degree weighting retains that local
signal with sign minus and cancels each higher-rank component's finite
trace algebraically.

However, on mixed-support components B_A=C and the coefficient action
is the identity at every t, although the actual groupoid time-return
subgroup is countable, dense and proper. This is not a faithful
return representation. Equation (10) cannot be applied by fiat to
an undefined full return distribution or to the infinite direct-sum
ordinary trace.

The carrier is complete as an all-real-time groupoid action. No new
primitive-circle convention for dense-return components was invented.
No identity from 153, no clock from 160, and no external operator is used.

## 6. Controls and adverse findings

| Control | Exact finding | Meaning |
| --- | --- | --- |
| A=Z[1/2] | Weighted component trace is -Theta_(log 2,epsilon), with actual return-comb limit | Local positive time control |
| A=Z[1/4] versus Z[1/2] | Same actual ring and one component | Prime-power labels do not duplicate packets |
| A=Z[1/6] | Exterior dimensions 1,2,1; weighted trace -2+2=0 | Mixed component retained, not removed |
| Same rank-two component | Weighted identity has trace norm 2+2=4 despite trace zero | Algebraic cancellation is not absence of channels |
| Infinite degree-one constants | Equation (11) | Full ordinary trace fails at fixed epsilon and t |
| Arbitrarily large unit rank | Top-degree constant has image norm r | Full maximal-domain operator is unbounded |
| Finite component cutoff | Equation (12), diverging negatively under complete exhaustion | Finite signed traces do not define a finite global cutoff trace |
| Unweighted exterior grading | Sum_j (-1)^j binom(r,j)=0 for all r>=1 | The degree weight changes local selection, not global summability |
| Arbitrary finite exterior rank, nonarithmetic comparator | Equation (10) holds for every r-dimensional vector space | PROVES_TOO_MUCH: this is a rank selector, not itself an arithmetic theorem |

These are exact controls, not finite numerical evidence for an infinite
claim. The full-ring provenance and the derived rank-one arithmetic
classification matter; the binomial identity alone contains no primes.

## 7. Gate assessment

| Gate | Evidence for this exact candidate | Status and boundary |
| --- | --- | --- |
| T0 carrier and analytic ownership | Propositions 1--3 | ESTABLISHED; explicit maximal closed operator domain |
| T1 source and clock | Equations (1)--(2), Proposition 1 | ESTABLISHED WITH SCOPE; power-saturation replacement, no chronological sieve conjugacy |
| T2 full returns | Proposition 1 | CLASSIFIED; dense mixed-return components retained, no full primitive-circle convention |
| T3 finite-component degree-weighted trace | Proposition 2 | ESTABLISHED LOCAL; rank-one time signal survives |
| T3 full ordinary trace | Proposition 3 | UNDEFINED; decisive scoped STOP |
| T3 finite-cutoff repair | Proposition 4 | SCOPED FAIL at fixed positive smoothing |
| Other relative/torsion/regularized owners | Not constructed | OPEN; not ruled out by this contract |
| Classical A0--A2 | No classical carrier | NOT APPLICABLE / NOT EVALUATED |
| Formal Route / Route B | No formal evaluation | UNASSIGNED / NOT INVOKED |

## 8. Conclusion and decision

**Portfolio decision: stop ANG-20260915-UEW01.** The full-unit exterior
degree weighting achieves the finite-component rank selection that the
earlier basic complex did not. Its prescribed full ordinary trace still
fails immediately on infinitely many degree-one constant channels;
the maximal-domain full operator is additionally unbounded.
The same-object ledger remained intact throughout this negative audit.

The next genuinely different relative or torsion framework would require
a new exact complex, action, domain and normalization. None is initiated
or credited here. No continued local tuning follows this STOP.

## Reproducibility and integrity

- [Frozen card and appended outcome](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and artifact checks](evidence/README.md)
- [Separate bounded mathematical review](evidence/review.md)

All substantive claims have self-contained exact proofs above. There are
no numerical experiments, finite precision claims, external datasets or
source-dependent theorem imports. The earlier papers are named scope
antecedents, not detached trace owners. The bounded ARS claim/evidence/
counterargument discipline informed this note; no full publication
workflow, human-peer-review approval or formal proof certificate is claimed.
