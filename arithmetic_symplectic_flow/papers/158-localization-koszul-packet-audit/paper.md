# Basic de Rham grading cancels localization prime-circle returns

**Paper ID:** 158-localization-koszul-packet-audit  
**Candidate ID:** ANG-20260915-LKC01  
**Date:** 2026-09-15  
**Status:** STOP — BASIC GRADING CANCELS PRIME RETURNS; FULL ORDINARY SUPERTRACE UNDEFINED.  
**Route state:** Broadened owner audit only; formal coordinates UNASSIGNED;
Route B NOT INVOKED.

## Abstract

We freeze a basic de Rham complex and a uniform Gaussian smoothing operator
over the complete all-localization scaling groupoid. Its carrier includes
every actual ring Z[1/n], not only rank-one circles. A single
translation-invariant mean defines the Hilbert norm before component
classification. The two Hilbert degrees are canonically paired, and their
smoothed time actions agree exactly. On a rank-one component the scalar
trace tends to the genuine log-prime return comb, but the unweighted
graded trace cancels it identically. On the full direct sum, infinitely
many constant channels prevent either degree from being trace class, so
the precommitted ordinary supertrace is undefined. Finite-component
graded cutoffs and an explicitly paired operator difference are zero,
not prime-return traces. This stops this analytic contract without
asserting an obstruction to every groupoid cohomology, relative trace or
torsion.

## 1. Candidate identity and full ownership

The [version-1 card](candidate-card.md) was frozen before this audit.
Let I be the set of distinct actual subrings

\[
A_n=\mathbb Z[1/n]\subset\mathbb Q,\quad n\ge2,\qquad
E_n=\{d\ge1:d\mid n^k\text{ for some }k\ge0\}.
\tag{1}
\]

Equality in I means equality as subrings; an integer representative is not
chosen. Define U_A={q in Q_{>0}:qA=A}. Objects are all (A,u), A in I,
u in R. An arrow (A,u,q), q in U_A, has target (A,u+log q);
composition multiplies q. Ring and unit indices are discrete, and u has
its ordinary topology. Time phi^t translates u by t on objects and
arrows. Every component and time-return arrow is retained.

| Owner | Frozen construction | Boundary |
| --- | --- | --- |
| Source | All-integer divisor language, power-saturation E_n, actual rings and units | No prime-selected index or logarithmic roof |
| Carrier and action | Complete groupoid above and real translation | Generally nonproper; not a classical symplectic map |
| Time returns | Closure up to an arrow in every localization | Not ordinary point isotropy |
| Complex | Groupoid-basic de Rham forms on the object lines | Not all groupoid cochains or unit-group cohomology |
| Norm | Translation mean on each component, then unweighted Hilbert direct sum | Same rule on every component |
| Operator | Uniform Gaussian smoothing and the same time pullback | No component damping |
| Target trace | Ordinary degree traces with signs +1 and -1 | No subtraction of undefined infinite traces |
| Later quantum owner | DEFERRED | No Route-B implication |

This is a new analytic-owner contract, not a claim that the operator was
supplied in [146](../146-localization-scaling-groupoid/paper.md).
The carrier is restated and checked below. Its retained higher-rank
returns are not reclassified as primitive circles.

## 2. Question, lineage and scope

Can this natural unweighted basic complex remove mixed-support returns
while retaining prime-circle logarithmic returns? No for this complex
and trace: it pairs the two degrees on prime circles as well, and its
full degree operators have infinitely many fixed constants.

The precise [prior-work arrow](../../docs/prior_work/README.md) is

\[
1_{\{d\mid n\}}\ \longrightarrow\
1_{\{d\mid n^k\text{ for some }k\}}\ \longrightarrow\
A_n\ \longrightarrow\ U_{A_n}\curvearrowright\mathbb R.
\tag{2}
\]

Power-saturation is a stated replacement of divisor exclusion. It forgets
prime-power label distinctions while keeping denominator admissibility.
It does not give a chronological sieve conjugacy or a positive-dimensional
Logistic/Hénon symplectic lift. This authorized ANG carrier remains distinct;
classical fields are NOT APPLICABLE.

A bounded local keyword search for Koszul, higher Euler, reduced exterior,
transverse exterior, and localization/cohomology returned no matching
contract before this card was created. The nearest object is 146, whose
trace fields were OPEN; the
[156 frontier](../156-multi-round-source-trace-frontier/paper.md) explicitly
left other analytic owners open. This is a local collision receipt,
not a global novelty claim or a literature review.

No prime table, zero data, prime-dependent weight, chosen rank-one
projection, Möbius coefficient, external flow or compact section enters
the construction.

## 3. Exact complex, normalization and operator

Set

\[
B_A=\{f\in C^\infty(\mathbb R;\mathbb C):
f(u+\log q)=f(u)\text{ for every }q\in U_A\}.
\]

The basic complex is

\[
\mathcal B^0=\bigoplus_A^{\rm alg} B_A,\qquad
\mathcal B^1=\bigoplus_A^{\rm alg}B_A\,du,\qquad
d f=f' du.
\tag{3}
\]

Basic means invariant under every arrow pullback. For this étale
groupoid there is no additional tangent direction in the discrete
arrow labels. We use this invariant de Rham complex only; it is not
identified with full stack or group cohomology. Its one-coordinate
differential has the elementary Koszul form du wedge partial_u, not
an exterior resolution with one generator per arithmetic unit.

The frozen norm is

\[
\langle f,h\rangle_A=
\lim_{R\to\infty}\frac1{2R}\int_{-R}^{R}f(u)\overline{h(u)}\,du,
\qquad
\|\eta\|^2=\sum_A\|\eta_A\|_A^2.
\tag{4}
\]

The same norm applies to coefficients of du. Let H^0,H^1 be the
completions; Proposition 2 proves they are genuine Hilbert spaces.
The normalized mean is fixed uniformly by (4), not by assigning a
selected measure to each prime.

For epsilon>0 and t in R put

\[
g_\epsilon(v)=(4\pi\epsilon)^{-1/2}e^{-v^2/(4\epsilon)},\quad
Q_\epsilon f(u)=\int_{\mathbb R}g_\epsilon(v)f(u+v)\,dv,\quad
V_t f(u)=f(u+t),\quad R_{\epsilon,t}=Q_\epsilon V_t.
\tag{5}
\]

Both operators act identically on coefficients in the two degrees.
There is no roof, coordinate rescaling or rank-dependent smoothing.
The precommitted target is

\[
\operatorname{STr}_{\rm ord}R_{\epsilon,t}
=\operatorname{Tr}_{H^0}R_{\epsilon,t}^0
-\operatorname{Tr}_{H^1}R_{\epsilon,t}^1,
\tag{6}
\]

provided both terms are ordinary traces of trace-class operators.
This contract does not define infinity minus infinity.

## 4. Proofs and decisive discriminator

### Proposition 1 — Full carrier and return classification

For any n let S(n) be its finite nonempty prime support. Then

\[
U_{A_n}=\left\{\prod_{p\in S(n)}p^{m_p}:m_p\in\mathbb Z\right\},
\qquad \Lambda_A=\log U_A.
\tag{7}
\]

Actual localization equality is equality of S(n). The arrows define an
étale groupoid with trivial point isotropy; Lambda_A is its time
stabilizer up to arrows. Support {p} gives one circle R/Lambda_A of
length L=log p. Support size at least two gives a dense proper Lambda_A.

**Proof.** A denominator divides a power of n exactly when all its prime
divisors divide n. This describes A_n, and 1/p belongs to A_n exactly
when p divides n. It proves the equality assertion. The equality
qA=A is equivalent to membership of q and q inverse in A; reduced
numerator and denominator give (7).

Each fixed (A,q) arrow line has source and target homeomorphic to the
object line, so the composition and inversion define an étale groupoid.
An arrow fixes an object only when log q=0, hence q=1. Translation
commutes with all arrows, and closing t up to an arrow means t=log q.
In rank one this gives (log p)Z.

For distinct primes p,q, log p/log q is irrational by unique
factorization. Pigeonholing 0,alpha,...,N alpha modulo one gives
nonzero integer combinations of log p and log q tending to zero.
Signs give positive ones. Their integer multiples meet every open
interval, proving density. Countability makes the subgroup proper.
QED.

No least positive return exists in a dense subgroup. These full
mixed-support returns are retained, not repaired by the representation.

### Proposition 2 — Basic spaces and uniform-mean completion

For support {p}, B_A consists exactly of smooth L-periodic functions,
L=log p, and (4) is L inverse times integration over one period.
For support size at least two, B_A consists exactly of constants,
and (4) is the ordinary complex inner product. Thus each H_A^j is
a copy of L^2(R/LZ,du/L) or C respectively, with every A retained.

**Proof.** Rank-one invariance is periodicity by Proposition 1.
For a smooth periodic function, a symmetric integration interval
consists of full periods and a uniformly bounded remainder. Dividing
by 2R proves (4), including products f times conjugate h. The norm
is positive definite and its completion is the stated L^2 space.

For dense Lambda_A, continuity and invariance imply f(u+v)=f(u)
for every real v by approximation from that subgroup. Thus f is
constant and the norm is its absolute value. The countable algebraic
direct sum completes to the Hilbert direct sum. The map J(f)=f du
is a unitary H^0 to H^1. QED.

Basic forms collapse some function information on each dense component;
they do not remove the component. This chosen representation is not
claimed to be faithful to the complete time-return ledger.

### Proposition 3 — Owned action and scalar component traces

V_t and Q_epsilon preserve (3), commute with d there, and extend
boundedly to both completions. V_t is unitary and Q_epsilon is a
contraction. The rank-one scalar trace is

\[
\Theta_{L,\epsilon}(t)
=\sum_{m\in\mathbb Z}e^{-\epsilon(2\pi m/L)^2}e^{2\pi i mt/L}
=L\sum_{k\in\mathbb Z}g_\epsilon(t-kL).
\tag{8}
\]

On a mixed-support component the trace in either degree is 1.

**Proof.** Periodic smooth functions and constants have bounded
derivatives. Gaussian convolution is defined on them, preserves
translation invariance, and commutes with differentiation and
translation. The orthonormal circle functions exp(2pi i m u/L)
diagonalize both operators with the eigenvalues in (8).
For completeness, the Gaussian Fourier transform follows by
differentiating its integral in frequency and integrating by parts:
F'(xi)=-2 epsilon xi F(xi), F(0)=1, hence
F(xi)=exp(-epsilon xi squared).

The Q_epsilon eigenvalues have modulus at most one, and the V_t
eigenvalues have modulus one. Constants are fixed. These uniform
bounds prove extension to the full direct sums. For epsilon>0 the
sum of absolute eigenvalues in (8) is finite, giving the ordinary
component trace. Periodizing g_epsilon gives m-th Fourier coefficient
L inverse times exp(-epsilon(2pi m/L) squared); its rapidly convergent
Fourier series proves the second equality. The mixed component is
one-dimensional with identity action. QED.

For each fixed rank-one component this gives

\[
\Theta_{L,\epsilon}\longrightarrow
L\sum_{k\in\mathbb Z}\delta_{kL}
\quad\text{in distributions on }\mathbb R,\qquad
\epsilon\downarrow0.
\tag{9}
\]

The Gaussian is an approximate identity. Against a compactly supported
smooth test function, finitely many lattice sites lie in any bounded
neighborhood of its support, while the remaining Gaussian tails have
a summable bound tending to zero. This proves (9).
For L=log p the returns are the actual k log p of the frozen action.
The factor L is derived from the scalar trace, not inserted as an
arithmetic coefficient.

### Proposition 4 — Grading cancellation and full-trace failure

For every epsilon>0 and t,

\[
R_{\epsilon,t}^1=J R_{\epsilon,t}^0 J^{-1}.
\tag{10}
\]

Every finite-component ordinary supertrace is zero. In particular,
the prime-circle return comb (9) cancels completely. On the full
direct sum neither degree operator is compact or trace class, so
the precommitted ordinary supertrace (6) is undefined.

**Proof.** Both degrees have the same coefficient action and norm.
This proves (10). Proposition 3 justifies ordinary traces on each
component and each finite collection. Their two traces coincide,
giving zero before any epsilon limit and cancelling (9).

Let c_A be the constant 1 in component A and zero elsewhere.
Equation (4) makes these an orthonormal family in H^0; Jc_A
does the same in H^1. There are infinitely many distinct A:
distinct primes give distinct Z[1/p]. There are infinitely many
primes because a prime factor of one plus the product of any
proposed finite list is absent from that list.
Equation (5) fixes each c_A exactly. Their images have mutual
distance square root of two, so no subsequence converges.
The operators are not compact, hence not trace class. This fails
the explicit existence condition in (6). QED.

The strongest counterargument is that (10) allows subtraction
before taking a trace. Correct: R^0 minus J inverse R^1 J is
the zero operator, with ordinary trace zero on the full space.
That well-defined paired relative observable contains no
prime-return signal. It is not the undefined difference of
separate ordinary degree traces in (6). A declared finite-component
cutoff prescription also gives zero at every cutoff, not an
Euler product.

## 5. Results and decisive stop

The normalization, basic complex and smoothed action are well-defined
and owned. Individual rank-one scalar traces see the original
logarithmic returns. Nevertheless, unweighted grading suppresses
these desired returns together with every other paired contribution.

Every mixed component remains present, with a fixed constant channel.
Its scalar trace is 1 for every t, not a delta comb or indicator
of its countable dense return subgroup. Basic invariants thus
do not retain all return information. The full separate trace
failure is independent of enumeration and smoothing cutoff.

There is no determinant or zeta construction in this contract.
No regularized expression is relabelled as an ordinary trace.
The decisive stop needs no numerical census.

## 6. Controls and adverse findings

| Control | Exact result | Interpretation |
| --- | --- | --- |
| Z[1/2]=Z[1/4] | One actual component, L=log 2 | No duplicate prime-power label or selected representative |
| Z[1/6] | Dense returns; basic spaces C in both degrees | Component retained; representation forgets detailed returns |
| Z[1/6] and Z[1/10] | Distinct components, both returning at log 2 | Basic invariance does not identify or delete them |
| One rank-one component | Positive scalar heat trace and limit (9) | Local positive control, not the full trace |
| Same circle, both degrees | Exact cancellation for every epsilon,t | Desired prime signal is lost |
| Any finite component cutoff | Ordinary supertrace zero | No missing nonzero cutoff limit |
| Full direct sum | Infinite orthonormal fixed constants | Uniform smoothing is not trace class |
| Degree zero alone | Keeps (9) and every mixed constant | Changed observable; full noncompactness persists |
| Arbitrary circle length L>0, external comparator | Same two-degree cancellation | PROVES_TOO_MUCH: de Rham pairing is not an arithmetic selector |

No floating-point test, prime cutoff or zero comparison supports any
infinite claim. The controls follow from the exact formulas.

## 7. Gate assessment

| Gate | Evidence for this candidate | Status / boundary |
| --- | --- | --- |
| T0 carrier and analytic ownership | Propositions 1--3 | ESTABLISHED for this basic complex, not full groupoid cohomology |
| T1 source and clock | Proposition 1 and (2) | ESTABLISHED WITH SCOPE; no chronological sieve realization |
| T2 full returns | Proposition 1 | CLASSIFIED; no full primitive-circle convention |
| T3 component scalar trace | Proposition 3 | ESTABLISHED locally with the same translation time |
| T3 prime-selective unweighted grading | Proposition 4 | SCOPED FAIL; prime-circle contributions cancel too |
| T3 full ordinary supertrace | Proposition 4 | UNDEFINED under the frozen ordinary-trace contract |
| Other complexes or relative constructions | Not this candidate | OPEN; not excluded |
| Classical A0--A2 | No classical map/roof fields | NOT APPLICABLE / NOT EVALUATED |
| Formal Route / Route B | No formal evaluation | UNASSIGNED / NOT INVOKED |

## 8. Conclusion and next decision

**Portfolio decision: stop this contract.** A single genuine prime
circle already gives the decisive local cancellation. The infinite
constant family independently stops the full ordinary trace.
The same-object ledger remained intact: component deletions,
degree changes and relative prescriptions are separated as
controls and never silently adopted.

One possible next hypothesis, not executed here, concerns a genuinely
different full unit-group exterior complex and a degree-weighted trace
instead of (6). A canonical same-object analytic torsion or
return-relative owner, its domain, normalization and full multiplicity
treatment remain OPEN. A fresh card is required before claiming any
arithmetic cancellation. This note gives that different contract
neither a result nor authorization.

## Reproducibility and integrity

- [Frozen card and appended outcome](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Inputs, controls and verification](evidence/README.md)
- [Independent bounded model review](evidence/review.md)

Proofs use elementary localization algebra, density of a two-generator
logarithmic subgroup, Fourier series on a circle and the explicit
orthonormal-family obstruction. There are no external datasets or
numerical outputs. The Gaussian transform is derived in the proof.
The bounded ARS claim/evidence/counterargument discipline informed
this record, not a publication pipeline. AI-authored or separately
model-reviewed arguments are not human peer review or formal verification.
