# An ordinary transfer determinant on the full ordered-cover source's first-symbol space

**Paper ID:** 174-ordered-source-transfer-determinant  
**Candidate ID:** ANG-20260915-OST01  
**Date:** 2026-09-15  
**Status:** ADVANCE — OWNED FIRST-SYMBOL TRACE-CLASS DETERMINANT; FULL-OBSERVABLE AND NATURALNESS LIMITS RETAINED.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The full one-sided nondecreasing divisibility-cover source has as its
natural extension the entire bilateral ordered-cover source, not only
its constant words. Its full-preimage transfer formula, weighted by
the inherited scale-return roof, preserves a specified Hilbert space
of first-symbol observables. A direct rank-one expansion proves trace
class on Re s>1, and trace-norm finite-rank approximants prove all
ordinary power traces and the ordinary Fredholm determinant. The
determinant at auxiliary variable z=1 is exactly the reciprocal of
the full scale flow's unweighted orbit product on that half-plane.
This is a new analytic contract on the restated 163 source/clock,
not a prime-diagonal operator attached after orbit classification.
Mixed states and all allowed preimages remain present. The selected
observable space does not describe all continuous observables; its
geometric ordinal weights and the source's ordering/scale choices are
declared engineering. No canonical arithmetic clock, classical
symplectic lift, continuation in s, target zeros or formal Route pass
is established.

## 1. Frozen identity, source lineage and question

The [version-1 card](candidate-card.md) fixes the following ledger
before the proofs. The source/scale construction is explicitly the
same as [163](../163-ordered-cover-scale-suspension/paper.md), expressed
in ratio coordinates; the new ID freezes the analytic fields that
163 left absent. The owner relation is proved below, not inferred
from matching a product.

| Item | ANG-20260915-OST01 owner | Boundary |
| --- | --- | --- |
| Arithmetic | Positive rationals with integer divisibility and its strict covers | Cover atoms derived below; no input prime table |
| Full source | Every nondecreasing one-sided cover-atom word Y_+ | Mixed words and every admissible prefix retained |
| Invertible owner | Full natural extension Y_Z and its bilateral shift F | No chosen inverse history or constant sector |
| Clock and flow | Q=(Y_Z times positive scales)/G, G(b,r)=(Fb,r/b_0); Phi^t[b,r]=[b,exp(t)r] | Exactly the restated scale law, not a new roof |
| Transfer | Full S-preimage sum with exp(-s tau_+) | On C(Y_+) algebraically; no unspecified Banach-space theorem |
| Analytic representation | All finite-norm first-symbol functions H=ell2(A,2^-j) | Proper observable class, not all continuous observables |
| Operator/domain | T_s on all H for Re s>1 | Bounded trace-class result proved, not assumed |
| Central function | Ordinary det_H(I-T_s), normalized by det_H(I)=1 | No flat or regularized trace |
| Full periodic data | All actual oriented primitive Phi-orbits and positive repetitions | Neither a selected representative nor a fresh orbit per repeat |
| Classical/later geometry | Classical symplectic fields NOT APPLICABLE; quantum/Hamiltonian owner NOT SUPPLIED | No credit from another lift |

The exact [prior-work](../../docs/prior_work/README.md) arrow is divisor
exclusion -> multiplicative indecomposability -> ordered symbolic
admissibility -> its scale-return flow -> a derived transfer
representation. This retains the symbolic-arithmetic starting point;
it does not claim execution of a chronological sieve or realization
of a Logistic/Henon map. The new work is analytic, not new geometry.

**Question.** Does the actual full-preimage transfer restrict to the
frozen H as a trace-class operator whose ordinary determinant owns
the complete same-clock orbit product? The strongest answer below
is yes on Re s>1 for this specific observable representation. It is
not a theorem on an unspecified full-source function space.

## 2. Exact source, all inverse histories and the clock

Let x <=_D z mean z/x is a positive integer. A strict cover
x prec_cov z means x <_D z and no intermediate rational in this
order. Let A be the set of ratios of all strict covers. If a ratio
n>=2 factors n=uv with u,v>=2, ux is intermediate; conversely an
intermediate gives such a factorization. Thus A is precisely the
integer irreducibles, the primes. This is a deduction from the
declared order, not an input prime alphabet. Enumerate the resulting
subset of positive integers increasingly as a_1,a_2,..., with a_1=2.
No numerical list or prime-count asymptotic is needed.

Give A the discrete topology and define

\[
Y_+=\{x\in A^{\mathbb N_0}:x_i\le x_{i+1}\},\qquad
Sx=(x_{i+1})_{i\ge0},\qquad
Y_{\mathbb Z}=\{b\in A^{\mathbb Z}:b_i\le b_{i+1}\}.
\tag{1}
\]

These are the entire product-subspace carriers defined by the rule.
The shift S is continuous and onto: prepend x_0 to any x. More
precisely, every preimage is exactly ax with a in A and a<=x_0.
Every such prefix occurs in the full source. There are finitely
many for a given x because a is a positive integer bounded by x_0.

### Proposition 1 — Full natural extension and source factor

The inverse-limit space

\[
\widehat Y=\{(x^{(0)},x^{(1)},\ldots):
Sx^{(m+1)}=x^{(m)}\text{ for all }m\ge0\}
\tag{2}
\]

is homeomorphic to all Y_Z. Under this homeomorphism its invertible
map (x^(0),x^(1),...) -> (Sx^(0),x^(0),x^(1),...) is F, the
bilateral left shift. The projection pi_+(b)=(b_0,b_1,...) is onto
and satisfies pi_+ F=S pi_+.

**Proof.** Send b to x^(m)=(b_-m,b_(1-m),...). Compatibility in
(2) is immediate. Conversely set b_n=x^(0)_n for n>=0 and
b_-m=x^(m)_0 for m>=1. Repeated compatibility gives
x^(m)_k=b_(k-m) for every m,k>=0. Adjacent inequalities in every
x^(m) give every bilateral inequality, so b belongs to Y_Z. These
maps are inverse and continuous: each coordinate in either map is
a coordinate projection. Substituting the maps gives exactly F.
Surjectivity of pi_+ also follows explicitly by using b_n=x_0 for
all n<0, but this example does not select that history in (2);
every compatible history is retained. QED.

For clarity, even the tail (3,3,3,...) has the distinct admissible
histories b_j=3 for all j, and b_j=2 for j<0, b_j=3 for j>=0.
The second is not periodic. We do not collapse these histories in
Y_Z or its flow. The one-sided tail factor itself is not injective.

Recover the exact normalized rational chain by

\[
y_0=1,\quad y_m=\prod_{i=0}^{m-1}b_i\ (m>0),\quad
y_m=\left(\prod_{i=m}^{-1}b_i\right)^{-1}\ (m<0).
\tag{3}
\]

Finite-coordinate products show this is a homeomorphism to the
entire normalized ordered-cover chain carrier in 163. Its shift is
y_j -> y_(j+1)/y_1. Accordingly freeze exactly

\[
G(b,r)=(Fb,r/b_0),\quad
Q=(Y_{\mathbb Z}\times\mathbb R_{>0})/\langle G\rangle,
\quad \Phi^t[b,r]=[b,e^tr].
\tag{4}
\]

### Proposition 2 — Same complete flow, actual roof, complete ledger

Equation (4) is a complete continuous Hausdorff quotient flow. The
section r=1 has actual first-return map F and roof log b_0>=log2.
Its complete primitive oriented orbit ledger has exactly one circle
for each a in A, time log a, and all repeated times k log a.

**Proof.** For every integer m, direct multiplication gives
G^m(b,r)=(F^m b,r/y_m). In u=log r coordinates, a nonzero iterate
changes u by -log y_m, of magnitude at least |m|log2 and sign
opposite to m. Thus the action is free. Bounded u-neighborhoods
can meet only finitely many translates of another bounded
neighborhood. For inequivalent points, separate each of this finite
set of potential translates by Hausdorff neighborhoods and take the
finite intersection. Their open saturations are disjoint. This
proves the quotient is Hausdorff without a local-compactness claim.
The quotient projection is open, and scale multiplication commutes
with G, so (4) descends jointly continuously with all real times.

The increasing values y_m run from zero to infinity. Every r>0 lies
in exactly one interval y_m<=r<y_(m+1); applying G^m puts it in
1<=r< b_0 at the corresponding shifted state. The closed strip
1<=r<=b_0 has seam (b,b_0)~(Fb,1), and covers all Q. A strip
|u|<epsilon with 2epsilon<log2 meets no nonzero translate, proving
that r=1 is an embedded section. Its positive crossings are exactly
t=log y_m, m>0, with the first m=1. The same lower bound prevents
Zeno accumulation in both directions. Consequently

\[
\tau(b)=\log b_0=\tau_+(\pi_+b),\qquad
\tau_+(x)=\log x_0
\tag{5}
\]

is an actual owner identity, including on nonperiodic histories.

A positive time t closes [b,r] exactly when F^m b=b and
e^t=y_m for some m>0. The cycle inequalities
b_j<=b_(j+1)<=...<=b_(j+m)=b_j force all entries constant.
Conversely constant b=a has exact time stabilizer (log a)Z.
All its scales lie on one oriented circle; distinct constants
cannot be identified by shifts. Every state meets the section,
so this exhausts all Q. Repetition means another positive traversal
of that circle, not a new primitive packet. QED.

The same monotonicity proves Fix(S^k) consists exactly of constant
one-sided words for every k>=1. Each has exactly one F^k-periodic
history, although it can have nonperiodic histories. Hence the
factor in Proposition 1 neither gains nor loses periodic-point
multiplicity. Nonperiodic mixed states remain in both carriers.

## 3. Full transfer, proper observable space, and trace class

On C(Y_+), with no boundedness assumption on the functions, define

\[
(\mathcal L_s h)(x)
=\sum_{a\in A,\ a\le x_0}e^{-s\tau_+(ax)}h(ax)
=\sum_{a\le x_0}a^{-s}h(ax).
\tag{6}
\]

The real logarithm defines a^-s. All preimages of S are included,
with their actual predecessor roof from (5). The sum is finite at
each x; on a neighborhood where x_0 is fixed it is the same finite
sum of continuous prefix maps. Thus (6) maps C(Y_+) to C(Y_+).
This assertion alone supplies no bounded operator or trace on that
whole space.

Freeze w_j=2^-j, inner product linear in the second argument, and

\[
H=\{f:A\to\mathbb C:\sum_jw_j|f(a_j)|^2<\infty\},\qquad
(Jf)(x)=f(x_0).
\tag{7}
\]

Every Jf is continuous because x_0 is discrete. The map J is
injective because all constant words occur. Equip JH with the
transported Hilbert norm, not an invented full-source invariant
measure. It contains all first-symbol functions having finite norm.
All are evaluated at every source state. It is a proper observable
space: the continuous function h(x)=1_{x_1=3} distinguishes
(2,2,2,...) and (2,3,3,...), whereas no first-symbol function does.
In particular x -> x_0 is not a deterministic factor of S;
only pi_+ in Proposition 1 is a dynamical factor. The invariance
below concerns the transfer operator, not the Koopman operator.

### Proposition 3 — True intertwining and ordinary trace class

For Re s>1, equation (6) leaves JH invariant, and under J its
operator is the bounded trace-class operator on all H

\[
(T_sf)(a_i)=\sum_{j\le i}a_j^{-s}f(a_j),\qquad
\mathcal L_sJ=JT_s.
\tag{8}
\]

Moreover s -> T_s is holomorphic in trace norm on that half-plane.

**Proof.** Set u_j(a_i)=1_{i>=j} and ell_j(f)=f(a_j). Evaluation
has norm w_j^-1/2, attained on the normalized coordinate vector;
the tail indicator has norm (sum_(i>=j) w_i)^1/2. Thus the rank-one
operator u_j ell_j has its one singular value

\[
\|u_j\|\,\|\ell_j\|
=\sqrt{\frac{\sum_{i\ge j}w_i}{w_j}}=\sqrt2.
\tag{9}
\]

In particular define finite-rank operators on the same entire H by

\[
T_{s,N}=\sum_{j=1}^N a_j^{-s}u_j\ell_j.
\tag{10}
\]

For sigma=Re s>1, sum_j a_j^-sigma <= sum_(n>=2) n^-sigma is
finite, and the trace-class Banach norm gives

\[
\|T_s\|_1\le\sqrt2\sum_j a_j^{-\sigma},\qquad
\|T_s-T_{s,N}\|_1\le\sqrt2\sum_{j>N}a_j^{-\sigma}\longrightarrow0.
\tag{11}
\]

This constructs a bounded trace-class limit on all H. Since each
coordinate evaluation is continuous, the limit at a_i stabilizes
after N>=i and is exactly (8). Substitution in (6) then proves
the intertwining and invariance for every f in H, not just finite
coordinate functions. Bounds (11) are uniform on compact subsets
of Re s>1. The finite-rank summands are entire in s, so their
locally normally convergent trace-class-valued series is
holomorphic there. Equivalently all derivative series are locally
dominated by sum_(n>=2) (log n)^m n^-(1+delta), for delta>0.
QED.

The actual kernel relative to the measure w on A and the actual
matrix in the orthonormal basis e_j=w_j^-1/2 1_{a_j} are

\[
K_s(a_i,a_j)=\frac{a_j^{-s}}{w_j}1_{j\le i},\qquad
\langle e_i,T_se_j\rangle
=a_j^{-s}\sqrt{\frac{w_i}{w_j}}1_{j\le i}.
\tag{12}
\]

The factor 1/w_j in the weighted kernel is essential. Entries
strictly below the diagonal are nonzero. For example e_1 is sent
to a nonzero tail on every a_i, not back to its own coordinate.
This is not a diagonal operator assigned to prime orbits.

We use only standard Hilbert trace-ideal facts: trace class is a
Banach operator ideal, |tr B|<=||B||_1, and finite-rank convergence
in trace norm yields locally uniform ordinary Fredholm determinants.
The ideal/trace bounds and determinant approximation are recorded
in [Bornemann, Sections 2--3, equations (2.3)--(2.5) and (3.2)](https://arxiv.org/pdf/0804.2543).
All source, intertwining and column estimates above are proved
here, not attributed to that reference.

## 4. All power traces and the ordinary determinant

### Proposition 4 — Finite-rank proof with the full tails retained

For every integer k>=1 and Re s>1,

\[
\operatorname{tr}_H(T_s^k)=\sum_{j\ge1}a_j^{-ks}.
\tag{13}
\]

For every complex auxiliary z, the ordinary Fredholm determinant is

\[
D(s,z)=\det_H(I-zT_s)=\prod_{j\ge1}(1-za_j^{-s}).
\tag{14}
\]

The product is locally uniform in z and s on C times {Re s>1}.

**Proof.** The range of T_(s,N) is E_N=span(u_1,...,u_N).
These tail vectors are independent, since their first N evaluations
form a triangular matrix with diagonal one. The range is invariant,
and its matrix in that basis has entries

\[
[T_{s,N}|_{E_N}]_{ij}=a_i^{-s}\ell_i(u_j)
=a_i^{-s}1_{j\le i},\qquad 1\le i,j\le N.
\tag{15}
\]

Indeed the first N evaluations are onto C^N and no a_i^-s
vanishes, so the range is exactly E_N, not a smaller unexamined
space. This is a finite lower-triangular matrix. A finite-rank
operator with range E_N has, relative to E_N plus its orthogonal
complement, block form [[B,C],[0,0]]. Therefore its ordinary trace
of each positive power and its ordinary determinant are the trace
of B^k and det(I-zB). Equation (15) gives

\[
\operatorname{tr}(T_{s,N}^k)=\sum_{j=1}^N a_j^{-ks},\qquad
\det(I-zT_{s,N})=\prod_{j=1}^N(1-za_j^{-s}).
\tag{16}
\]

The approximants are not operators on a selected finite source or
constant sector: every u_j remains a tail on all indices. They
truncate incoming terms for an estimate, then converge on the
same entire H by (11). If B bounds the operator norms of T_s and
all T_(s,N), telescoping products and the ideal inequality give

\[
\|T_s^k-T_{s,N}^k\|_1
\le k B^{k-1}\|T_s-T_{s,N}\|_1\longrightarrow0.
\tag{17}
\]

Trace continuity proves (13). The ordinary determinant
finite-rank continuity theorem cited above proves the limit in
(14) for every z, locally uniformly. Finally sum_j |z a_j^-s|
is locally uniformly bounded and has uniformly vanishing tails
on the stated domain, directly proving local uniform product
convergence and joint holomorphy there. QED.

There is also an exact path interpretation, not a heuristic trace
formula: (6) iterated k times sums every length-k permitted prefix
c_0<=c_1<=...<=c_(k-1)<=x_0, with weight
(c_0 c_1 ... c_(k-1))^-s. A closed path in this first-symbol
adjacency relation must have all its indices equal. Its weight is
a^-ks. These are exactly all points of Fix(S^k) and their unique
periodic bilateral lifts from Proposition 2. Thus

\[
\operatorname{tr}(T_s^k)
=\sum_{x\in\operatorname{Fix}(S^k)}
\exp\left(-s\sum_{m=0}^{k-1}\tau_+(S^m x)\right).
\tag{18}
\]

No extra periodic paths are removed by the representation. The
proof is (13) plus the full fixed-point classification, rather
than a general fixed-point theorem for an unconstructed full
operator. The same-cycle normalization is k copies of one
section point, so the orbit logarithm has its usual 1/k factor.

### Proposition 5 — Exact same-flow ordinary product

For Re s>1, with Z_Q the complete ordinary unweighted orbit product
of (4),

\[
D(s,1)=\exp\left(-\sum_{k\ge1}\frac{\operatorname{tr}(T_s^k)}k\right)
=\prod_{a\in A}(1-a^{-s})=Z_Q(s)^{-1}.
\tag{19}
\]

**Proof.** For sigma>1,

\[
\sum_{k\ge1}\frac1k\sum_j |a_j^{-ks}|
\le\frac1{1-2^{-\sigma}}\sum_j a_j^{-\sigma}<\infty.
\tag{20}
\]

Elementary log(1-v)=-sum_(k>=1) v^k/k, valid for |v|<1,
can therefore be summed over every a to derive the middle
expression from (14) at z=1. We do not use the sufficient
condition ||T_s||<1, which has not been established on the
entire half-plane. Absolute convergence (20) and the already
proved product are what justify this power-trace identity.
Proposition 2 gives exactly one full primitive circle of length
log a and its repeats k log a, so its full ordinary orbit
logarithm is the negative exponent in (19). This proves the last
equality with no normalization factor or added orbit weight. QED.

For completeness, the cover classification and unique integer
factorization identify Z_Q(s)=sum_(n>=1) n^-s on Re s>1:
finite products expand over the integers supported on those
atoms, and absolute convergence of the full integer series
permits exhaustion. This is only the defining Euler/Dirichlet
half-plane identity. The result is not meromorphic continuation
of either T_s or its determinant in s. Entire dependence on
the auxiliary z in (14) does not change that limitation.

## 5. Controls, negative findings and nontransfer

| Control | Exact result | What it prevents |
| --- | --- | --- |
| Composite ratio 4 | The rational 2x is intermediate between x and 4x | A composite is not made a cover atom by a label |
| Mixed tails (2,2,...) and (2,3,3,...) | Both are in Y_+; (6) acts on both; first-symbol observables do not distinguish their tails | Explicit proper-space limitation, not a claim of full-observable faithfulness |
| Different inverse histories of (3,3,...) | All compatible histories remain in Y_Z; only the constant history is periodic | No selected prefix or inverse branch masquerading as full extension |
| Remove ordering, retain covers/scale | The full source permits mixed closed word (2,3), time log6 | Its transfer no longer has (8)'s triangular path rule; (19) cannot be transferred to that changed owner |
| Remove covers but retain ordering | Every constant integer n>=2 becomes a packet | Ordering alone is not prime specificity |
| Off-diagonal entry i=2,j=1 | It is 2^-s sqrt(w_2/w_1), not zero | No prime-diagonal operator replacement |
| Weight normalization | Tail/evaluation norm product is exactly sqrt2; kernel uses 1/w_j | No unweighted-kernel trace error |
| Counting measure instead of w | T_s 1_{a_j} has a nonzero infinite constant tail and is not in unweighted ell2 | The chosen Hilbert norm is substantive analytic design, not an invariantly forced norm |
| Full finite-rank limit | T_(s,N) retains tail functions; bound (11) controls omitted incoming columns | No finite cutoff or partial periodic support is credited as the full operator |
| Another ordered integer alphabet | The same triangular/cycle argument applies whenever the corresponding coefficient sum converges | PROVES_TOO_MUCH: transfer machinery is generic; arithmetic specificity is in the covers |

[153](../153-saturated-sieve-flat-trace/paper.md) owns flat traces
on compactly supported forms for a different symplectic witness
map with a unit binary macroclock. No such trace enters (9)--(20).
[157](../157-power-trace-integrality-audit/paper.md) excludes a
fixed trace-class operator whose all-powers traces are those exact
rounded-clock sequences. Our trace-class family T_s has the
different, explicitly derived traces (13); neither 157's obstruction
nor 153's positive result is being reassigned to this owner.

The whole source and clock from 163 are retained and re-identified,
but the analytic engineering is new: a one-sided presentation,
a proper first-symbol space, and weights chosen by ordinal index.
The entries of T_s are forced once this source, roof and space are
fixed; the decision to use that space is not forced by arithmetic.
No theorem here constructs a trace-class operator on all continuous
observables, or proves that all such richer spaces have this
determinant. No measure on Q, self-adjointness, Hamiltonian lift,
functional equation, completed determinant or zero theorem follows.

## 6. Owner-level gate assessment

| Audit | Result | Limitation |
| --- | --- | --- |
| T0 full carrier and ownership | ESTABLISHED: Propositions 1--2 identify the full extension and scale flow | Broadened category, not classical finite-dimensional symplectic geometry |
| T1 arithmetic and clock owner | SCOPED ESTABLISHED: covers derive atoms; (5)--(6) use the actual same roof | Admissibility, exp(t) normalization and analytic weights are declared design; naturalness OPEN |
| T2 full packets/repetitions | ESTABLISHED: complete ledger, periodic-lift multiplicity and closed paths | No new geometric realization or sequential prime execution |
| T3 analytic owner | ESTABLISHED on Re s>1: ordinary Hilbert power traces and Fredholm determinant on the specified first-symbol H | Not an operator theorem on all C(Y_+); no continuation or target/divisor claim |
| Classical A0--A2 | NOT APPLICABLE | No natural A0 or formal Route coordinate inferred from T labels |
| Formal Route / Route B | UNASSIGNED / NOT INVOKED | Neither formally evaluated |

## 7. Conclusion and decision

**Decision: advance this scoped analytic construction; fork before a
changed source, clock, norm or observable representation.** The
decisive positive test is trace-norm summability of the actual
full-preimage columns, followed by exact finite-rank triangular
determinants and full periodic-path ownership. This closes the
specified first-symbol ordinary Fredholm question. It does not
close source-clock naturalness or a full-observable spectral problem.

The same-object ledger remains intact: (1)--(5) own the source,
inverse histories, flow, clock and packets; (6)--(12) are its
derived operator in the openly chosen representation; (13)--(20)
are its ordinary traces and determinant. No later research or
formal evaluation is authorized by this conclusion.

## Reproducibility and integrity

Exact inputs are the full rational divisibility order, weak numerical
ordering, y_0=1, scale exp(t), w_j=2^-j and the real logarithm.
Proofs above are the mathematical method; no numerical experiment,
prime table, fitted coefficient, finite-data inference or zero data
was used. The cutoff N appears only in exact inequalities followed
by a proved infinite limit. See the [claim ledger](claim-ledger.md),
[card](candidate-card.md), [evidence index](evidence/README.md) and
[summary](README.md).

This is an AI-authored bounded Markdown research record. A separate
same-model, inherited-context invocation provides a nonblind
mathematical review, not human peer review or independent-error
certification. The initially listed ARS skill path was unavailable;
after the controller supplied the actual cache path, its router,
academic-paper workflow and argument-builder prompt were read in
full. Only bounded claim/evidence/counterargument checking was
applied, with the initial fallback preserved in the evidence record.
No publication workflow,
human-subject study, external-model upload or publication artifact
is part of this work.
