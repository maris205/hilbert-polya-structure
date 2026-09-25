# A divisor-executing symplectic map has an arithmetic return selector but the wrong prime clock

**Paper ID:** 141-divisor-counter-henon-lift.  
**Candidate ID:** ASFS-20260915-DCH01.  
**Date / status:** 2026-09-15; ARITHMETIC RETURN AND FULL SYMPLECTIC LEDGER ESTABLISHED; PRIME-LOG CLOCK FAILS.  
**Portfolio:** retain as an exact positive control; fork on the clock.  
**Route:** owner-level construction only; formal Route coordinates UNASSIGNED;
Route B NOT INVOKED.

## Abstract

We freeze a two-dimensional, disconnected symplectic map that executes one
proper-divisor test per iterate while updating a cyclic scan phase and a
finite counter. The transverse map is the fixed area-preserving Hénon-form
linear map (q,p) to (p,3p-q). We prove its complete periodic set rather than
choosing geometric centres: all periodic points have zero transverse
coordinates, and the remaining full-state periods depend on the actual
divisor count. A marked integer fibre contains a full-state return after one
complete scan exactly when its label is prime.
Thus arithmetic affects the intrinsic primitive ledger, not just a coordinate
label. Every prime p nevertheless produces p primitive orbits of length
max(1,p-2), with the full multiplicity retained. The same-object ordinary
orbit product converges on the positive real-part half-plane, but no
logarithmic prime clock, unique prime orbit, transfer operator or trace formula
has been obtained. The explicit clock mismatch ends this candidate as a
Riemann-target direction without erasing its source and geometric results.

## 1. Frozen object and lineage

The [version-1 card](candidate-card.md) defines, for every n>=2,

\[
L_n=\max(1,n-2),\quad J_n=\mathbb Z/L_n\mathbb Z,\quad
C_n=\mathbb Z/n\mathbb Z,
\]
\[
M=\coprod_{n\geq2,\ j\in J_n,\ c\in C_n}\mathbb R^2_{n,j,c},
\qquad \omega=dq\wedge dp\quad\hbox{on each component}.
\]

For j represented in 0,...,L_n-1, let h(n,j) be one if j+2<n and j+2
divides n, and zero otherwise. The exact map is

\[
\mathcal F(n,j,c,q,p)=
(n,j+1\bmod L_n,c+h(n,j)\bmod n,p,3p-q).
\tag{1}
\]

All n and all counter values belong to M. No supplied prime word, prime
table, selected prime modulus, or desired period enters (1).

The source arrow in the [prior-work guide](../../docs/prior_work/README.md)
is specific: divisor-exclusion prime/composite symbols, as in
[050](../050-causal-binary-sieve-fixed-point-screen/paper.md), are replaced by
successive local divisor tests with complete scan and counter memory; that
action is realized on a positive-dimensional Hénon-form symplectic carrier.
This is a construction, not a claim of conjugacy to a historical Logistic
map or realization of every arrow in the prior-work programme.

The discrete rule also appears in the separately frozen
[140](../140-cyclic-divisor-counter/candidate-card.md), but all claims about
(1), its full geometry, periods, and roof are proved here. The geometric
idea has a close antecedent in
[052](../052-hyperbolic-wheel-packet-lift/paper.md); no novelty for hyperbolic
thickening alone is claimed. The difference to audit is that (1) executes
the divisor test at every step, whereas 052 cycles through preassembled
wheel packets without executing its inter-stage sieve action.

| Owner field | Exact object | Result / limitation |
| --- | --- | --- |
| Phase space | Full countable union M of planes | Smooth two-dimensional, noncompact, disconnected |
| Symplectic map | Equation (1), coefficient exactly 3 | Global smooth symplectomorphism |
| Arithmetic action | h(n,j) updates c while j scans all proper divisors | Zero scan displacement iff n is prime |
| Observable / coding | Full n,j,c plus transverse q,p; projection to n,j,c | Projection intertwines the same map; it is not a conjugacy of all M |
| Roof / flow | Unit roof and its endpoint-glued suspension | Complete three-dimensional flow, not itself symplectic |
| Primitive ledger | All intrinsic periodic orbits of mathcal F | Exactly classified, with all counter multiplicities |
| Monodromy | Power of the derivative of (p,3p-q) | Hyperbolic; no trace weight inferred |
| Analytic object | Ordinary unweighted primitive product | Defined for Re(s)>0; operator and trace NOT SUPPLIED |
| Later lift | Contact, Hamiltonian or quantum owner | DEFERRED / NOT SUPPLIED |

## 2. Geometry, inverse, and clock ownership

### Proposition 1 — A genuine positive-dimensional symplectic base

M is a Hausdorff second-countable smooth manifold of dimension two.
The map mathcal F is a smooth symplectomorphism with a smooth inverse.

**Proof.** The component index set is countable. The topological disjoint
union of its planes has a countable union of countable Euclidean bases and
the ordinary charts on every component. Distinct components are separated,
and within each component the usual Hausdorff property holds.

For output (n,j',c',q',p'), put j=j'-1 modulo L_n and recover

\[
c=c'-h(n,j)\bmod n,\qquad q=3q'-p',\qquad p=q'.
\]

This is a globally defined inverse. Both maps are affine smooth maps between
the appropriate open plane components. On every component,

\[
H(q,p)=(p,3p-q),\qquad H^*(dq\wedge dp)
=dp\wedge(3dp-dq)=dq\wedge dp.
\]

The discrete component permutation does not change this equality. QED.

There is no parameter-selection uncertainty: 3 was fixed before the audit.
Componentwise area has infinite total mass; no invariant probability measure
or finite operator trace is inferred.

Define the suspension
\[
S=(M\times[0,1])/((z,1)\sim(\mathcal Fz,0)).
\]
At time t from (z,u), 0<=u<1, use
k=floor(u+t), obtaining (mathcal F^k z,u+t-k). This is defined for every
real t. Every return time is an integer, since height modulo one must return,
so primitive flow lengths equal the least full base periods. The flow is
three-dimensional and is not being called symplectic or Hamiltonian.

## 3. Arithmetic executed during return

Let
\[
a_n=\sum_{j=0}^{L_n-1}h(n,j),\qquad g_n=\gcd(n,a_n),
\qquad \gcd(n,0)=n.
\tag{2}
\]
These are quantities derived from the frozen action, not inputs used to
choose its periods.

### Proposition 2 — Exact scan-return selector

After L_n steps, j first returns and c changes by a_n modulo n,
independently of the starting j and c. The integer a_n counts proper
divisors d with 2<=d<n, and

\[
0\leq a_n<n,\qquad a_n=0\ \Longleftrightarrow\ n\hbox{ is prime}.
\tag{3}
\]

**Proof.** For n>=3 a complete scan visits exactly d=2,...,n-1; every
successful divisor test adds one to c. Starting at another phase cyclically
reorders those additions and leaves their sum unchanged. For n=2 the single
guarded test has d=2 and fails d<n, so its count is zero. A prime has no
proper divisor in the stated range and every composite has at least one.
There are at most n-2 such candidate divisors, proving the strict upper
bound and excluding nonzero wraparound to zero modulo n. QED.

The symbol in (3) is the same prime/composite exclusion as the small-divisor
test of 050: either range has no witness exactly for primes. The evolution
is different and explicitly frozen. There is no omitted increasing history
or external reset that supplies a return.

## 4. Complete intrinsic periodic ledger

### Theorem 3 — Isolated hyperbolic packets and full multiplicity

Put
\[
\ell_n=L_n\,\frac{n}{g_n}.
\tag{4}
\]
For each n, mathcal F has exactly g_n primitive orbits, each of least
period ell_n. Every periodic point in M has q=p=0. No other periodic
points exist. In the unit suspension each such orbit has length ell_n
and r-fold traversal length r ell_n.

**Proof.** Any discrete return must have time divisible by L_n, due to the
scan phase. After k scans the counter displacement is k a_n modulo n.
Its least positive vanishing time is k=n/g_n. Thus every discrete state
with this n has least period ell_n. There are n L_n such states, so
division by the exact cyclic phase count ell_n gives g_n distinct orbits.

For the transverse map, the matrix is
\[
B=\begin{pmatrix}0&1\\-1&3\end{pmatrix},
\qquad \lambda_\pm=\frac{3\pm\sqrt5}{2}.
\]
The eigenvalues are distinct and satisfy lambda_+>1 and
0<lambda_-<1. For every integer m>0 neither eigenvalue of B^m equals
one. Therefore B^m v=v only for v=0.

The full return condition from (1) combines the discrete return and B^m v=v,
so v=0 is necessary and sufficient together with the already proved
discrete period. The zero transverse coordinates have not been selected as
a subsystem; they are the complete solution of the periodic equations on
all M. The owned roof gives the stated primitive lengths and repetitions.
QED.

The derivative monodromy of a least-period-ell_n orbit is B^ell_n, with
multipliers lambda_+^ell_n and lambda_-^ell_n. It is nondegenerate:
\[
\det(I-B^{\ell_n})=2-\lambda_+^{\ell_n}-\lambda_-^{\ell_n}\ne0.
\]
Area preservation does not turn this expression into one or establish an
unweighted transfer-operator trace. No such trace is used below.

An immediate same-object consequence is
\[
n\hbox{ prime}\quad\Longleftrightarrow\quad
\operatorname{Fix}(\mathcal F^{L_n})\cap M_n\ne\varnothing.
\tag{5}
\]
For a prime p there are exactly p primitive orbits of length L_p; for a
composite n every primitive orbit above n has length strictly greater than
L_n. This is a genuine arithmetic return distinction, not just a prime
observable read from dynamics with a source-independent period spectrum.

## 5. Ordinary orbit product and its boundary

### Proposition 4 — Same-object local analytic result

The complete ordinary unweighted product is
\[
Z_{\rm DCH}(s)=\prod_{n\geq2}(1-e^{-s\ell_n})^{-g_n},
\qquad \Re s>0.
\tag{6}
\]
It converges absolutely in its logarithmic expansion, locally uniformly on
that half-plane, and defines a holomorphic nonvanishing function there.

**Proof.** Formula (6) uses exactly Theorem 3's full orbit multiplicity and
the roof fixed in Section 2. For sigma>0, g_n<=n and ell_n>=n-2 for
n>=3. Also ell_n>=1 for every n. Hence
\[
\sum_{n\geq2}g_n\sum_{r\geq1}\frac{e^{-\sigma r\ell_n}}r
\leq\frac1{1-e^{-\sigma}}
\sum_{n\geq2}n e^{-\sigma\ell_n}<\infty.
\]
The n=2 term is finite and the remainder is dominated by
sum n exp(-sigma(n-2)). The same bound is uniform on compact subsets
of Re(s)>0. Exponentiating the absolutely convergent logarithmic series
proves the result. QED.

This is not a transfer-operator determinant or trace formula. No continuation
across Re(s)=0, target divisor identity, completed structure, or zero comparison
has been established. The formula does not discard composite orbits.

### Proposition 5 — The prime clock is not logarithmic

For primes p>=3 the actual primitive length is p-2, and its multiplicity is p.
In particular (p-2)/log(p) tends to infinity along the primes. No fixed
positive rescaling of the unit clock makes these lengths asymptotic to log(p).

**Proof.** For prime p, (3) gives a_p=0 and g_p=p, so (4) gives L_p=p-2.
The ratio follows from the elementary growth of x/log(x) and the unboundedness
of the primes. A fixed positive multiplier cannot change that divergence.
QED.

For p=2 the length is 1 and there are two primitive orbits. All exceptions
and multiplicities are preserved. Repetition of a given prime-carrying orbit
gives r(p-2), not r log(p). It does not change the conserved label p to p^r.
Assigning log(p) after this finding would change the roof and the candidate.

## 6. Controls and argument boundaries

| Claim / evidence | Adversarial check | Result and limitation |
| --- | --- | --- |
| Local divisibility changes full-state returns, (3)--(5) | Suppress h entirely | Every integer fibre then returns after one scan, including composites; the selector is destroyed |
| Same selector is not mere phase cycling | Replace every h by one | Scan displacement becomes L_n, strictly between 0 and n; every fibre fails the one-scan return, including primes |
| Counter modulus prevents false zero displacement | Separate modulus-two counter comparator | n=6 has two proper divisors and aliases to zero; the original modulus-n rule does not |
| Full positive-dimensional periodic classification | Include every noncentral transverse point | Theorem 3 excludes all of them by B^m-I invertibility, without selecting a centre |
| Geometric thickening supplies arithmetic | Replace the discrete permutation by an arbitrary permutation | The same geometric argument works, but supplies no arithmetic selection; that content must come from (1)'s actual divisor updates |
| Conserved integer coordinate is external prime data | Compare with separately selected prime fibres | M includes all integers and uses one fixed local rule; no prime-specific carrier or omitted construction process is supplied |
| Countable prime-associated packets give the desired prime product | Retain g_n and ell_n for every n | Prime multiplicity p, composite packets and nonlogarithmic clocks remain; the desired product does not follow |

These controls support a fixed endogenous primality-sensitive return
criterion. They do not prove that this engineered arithmetic algorithm is a
canonical Riemann geometry, or that disconnected component labels have a
unique intrinsic geometric interpretation. That naturalness question stays
OPEN. It is equally unwarranted to declare every integer-labelled uniform
action external merely because the label is conserved.

The argument separates source ownership, geometric ownership, and target
fit, following the ARS claim-evidence and counterargument discipline. It does
not invoke a full ARS publication workflow, a calibrated panel or human review.

## 7. Gate assessment and decision

| Obligation | Evidence for ASFS-20260915-DCH01 | Status |
| --- | --- | --- |
| P0 geometric owner | Explicit M, omega, mathcal F, inverse, roof and complete suspension | ESTABLISHED |
| A0 source component | Same-map divisor tests and primality-sensitive full return criterion, with controls | Exact endogenous source-return result; not a claim of full Riemann-target A0 success |
| A0 clock / target fit | Actual prime lengths p-2 and multiplicity p | Prime-log clock scoped FAIL; canonical Riemann relevance OPEN |
| A1 owner component | Complete intrinsic periodic set, primitive periods, all multiplicity, monodromy and repetitions | ESTABLISHED as an owner-level result |
| A2 owner component | Complete ordinary orbit product on Re(s)>0 | ESTABLISHED for that scalar product only; operator/trace OPEN |
| Formal Route coordinates | No formal target/divisor protocol evaluated | UNASSIGNED |
| Route B | No invocation or later operator audit | NOT INVOKED |

**Decision: retain the exact arithmetic/symplectic return control; fork on
the clock and target architecture.** Unlike a fixed arithmetic decoration,
the same map now executes the arithmetic tests and owns the return. Unlike
an indiscriminate disk thickening, its full periodic ledger has no continuum
of extra orbits. But neither improvement repairs the proved clock mismatch
or licenses selecting one of p indistinguishable prime-fibre packets.

The short full-ledger calculation is needed to audit the actual clock and
is not a prolonged investigation of a failed A0 fit. Equation (6) records its
immediate same-object consequence, not a formal A2 evaluation after a Route
failure. No spectral experiments, parameter sweeps or later lifts are pursued.

## Reproducibility and declarations

[Card](candidate-card.md), [claim ledger](claim-ledger.md), and
[evidence index](evidence/README.md) contain the exact inputs and scope.
All infinite statements are proved above. There is no finite numerical
experiment, precision cutoff or supplied prime data.

Data availability: all definitions and proofs are local Markdown. Ethics:
no human or animal study and no personal data. Contributions: AI-assisted
construction, proof drafting and checking under the user's direction; no
human verification is attested. Funding and conflicts: no user declaration
supplied, so unknown. This is a research record, not a submission package.
