# GCD-defect cocycle on a countable symplectic phase carrier

**Paper ID:** 228-gcd-defect-cocycle  
**Candidate ID:** ASFS-20260918-GDC01  
**Date / status:** 2026-09-18; P0 FROZEN — A0 SCOPED POSITIVE FOR THE GCD SOURCE; A1 SCOPED FAIL; A2 NOT EVALUATED  
**Route state:** exact same-object geometric and periodic-ledger audit; formal
Route-A coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

This paper freezes and audits one countable positive-dimensional symplectic
carrier. Its states have an integer n≥2, a phase 1≤d<n, an integer register
k, and z=(q,p)∈R². At each phase the endogenous defect

\[
\delta(n,d)=\gcd(n,d)-1
\]

both advances k and selects the area-preserving matrix

\[
A_\delta=\begin{pmatrix}2+\delta&1+\delta\\1&1\end{pmatrix}.
\]

The phase advances cyclically and the roof is the unit function. The map is a
global symplectomorphism of the entire disjoint union. For a prime p, all
defects vanish, so every k∈Z owns one packet of p−1 phase states at z=0, of
least base and flow period p−1. For composite n, the sum of the defects over
one phase cycle is positive; k therefore drifts and no full state is periodic,
independently of the real geometry. Thus the prime packets are countably many
in k, and the unit clock is p−1, not log p. These are exact same-object
results and decisive A1 stops. The indicator-divisor, shuffled-phase,
forgotten-k, and A0-decoupled controls are recorded. No transfer operator,
determinant, target matching, formal Route coordinate, or Route-B object is
supplied.

## 1. Candidate identity and same-object ledger

The [frozen candidate card](candidate-card.md) predates this proof. For every
n≥2, set D_n={1,…,n−1}, with the cyclic successor

\[
d^+=\begin{cases}d+1,&d<n-1,\\1,&d=n-1.\end{cases}
\]

The arithmetic defect is

\[
\delta(n,d)=\gcd(n,d)-1.
\tag{1}
\]

The full phase carrier and form are

\[
M=\coprod_{n\ge2,\ d\in D_n,\ k\in\mathbb Z}\mathbb R^2_{n,d,k},
\qquad \omega|_{\mathbb R^2_{n,d,k}}=dq\wedge dp.
\tag{2}
\]

For z=(q,p)^T, let

\[
A_\delta=\begin{pmatrix}2+\delta&1+\delta\\1&1\end{pmatrix},
\qquad \det A_\delta=1.
\tag{3}
\]

The single base map is

\[
F(n,d,k,z)=\bigl(n,d^+,k+\delta(n,d),A_{\delta(n,d)}z\bigr).
\tag{4}
\]

The roof and flow belong to this same map:

\[
\tau(n,d,k,z)=1,\qquad
M_\tau=\{(x,t):x\in M,\ 0\le t\le1\}/((x,1)\sim(Fx,0)),
\tag{5}
\]

and φ^t is translation in the second coordinate after the quotient. The base
is symplectic; the odd-dimensional suspension is not being called a
symplectic or Hamiltonian manifold merely because the base is symplectic.

| Ledger item | Owner in this candidate | State |
| --- | --- | --- |
| Phase space and form | (2), all n,d,k,q,p | frozen |
| Base map | (4), with (3) | exact symplectic proof below |
| Arithmetic source | The same gcd defect in the k-cocycle and matrix selector | endogenous at the operational level; source naturalness open |
| Symbolic lineage | gcd prime/composite observable → cyclic scan → conservative two-dimensional lift | direct constrained lift, not a historical conjugacy |
| Clock | τ≡1 in (5) | exact unit clock; not logarithmic |
| Primitive convention | All least-period full states modulo cyclic phase, retaining k and all z∈R² | complete ledger proved below |
| Repetition | r-fold traversal of one primitive oriented flow orbit | r(p−1) |
| Analytic owner | None supplied | open / not evaluated |
| Later lift | Hamiltonian/contact/quantum | deferred |

## 2. Question and claim boundary

### Question

Does the gcd-defect phase scan define one invertible symplectic suspension whose
full periodic ledger separates primes from composites, and what clock and
multiplicity does that same object actually produce?

### Strongest supported claim

Yes, at the geometric level. F is a global symplectomorphism and the
unit-roof suspension is complete. Its full periodic set consists exactly of

\[
\mathcal P=\{(p,d,k,0):p\ {\rm prime},\ k\in\mathbb Z,\ d\in D_p\}.
\tag{6}
\]

For fixed (p,k), the p−1 states in (6) form one primitive oriented flow orbit
of period p−1. Composite fibres have no periodic states.

### Explicit nonclaims

- The unit roof does not produce T_p=log p; no logarithmic target clock is
  claimed or inserted.
- The complete ledger has one packet for every k∈Z at each prime, so it is not
  a singleton prime dictionary.
- No transfer operator, Fredholm determinant, trace formula, continuation,
  Hilbert/contact/quantum owner, Route-A pass, Route-B coordinate, or
  Riemann-zero statement is supplied.
- Forgetting k, changing phase order, or replacing A_δ is a new quotient/control,
  not an allowed repair of this candidate.

## 3. Definitions, inputs, and provenance

The only arithmetic operation is the intrinsic integer gcd in (1). The integer
n is carried by the state, not selected from a prime list; no external
primality oracle is queried. The phase scan visits every d<n exactly once
before returning. The same integer δ(n,d) is used in both the discrete register
and the matrix, so the arithmetic and geometry cannot be separated in the
frozen object. The matrix coefficient is fixed once and for all by (3), with no
fitted n-, d-, k-, or prime-dependent parameter.

The lineage claim is deliberately narrow: the construction retains the
prime/composite observable and sequential admissibility-style scan from the
project's symbolic source, then realizes it in an area-preserving two-dimensional
carrier. It is not asserted to be a conjugacy to a prior Logistic or Hénon
map. The unit roof is a declared clock and is tested as such.

The three retained arrows are explicit. First, the arithmetic
prime/composite observable is the statement that \(\delta(n,d)=0\) at every
phase exactly when \(n\) is prime, whereas a proper divisor creates a positive
defect. Second, the symbolic/sequential arrow is the cyclic scan through all
phases \(d=1,\ldots,n-1\), with the defect accumulated in the reversible
integer cocycle \(k\mapsto k+\delta\). Third, the geometric lift is the
positive-dimensional conservative action \(z\mapsto A_\delta z\), using the
same defect rather than an independently fitted label. The construction
preserves these mechanisms and deliberately exposes, rather than repairs, the
unit-clock and \(k\)-multiplicity obstructions.

## 4. Exact geometry and suspension completeness

### Proposition 1 — Global invertibility and symplecticity

The map F in (4) is a smooth global symplectomorphism of the full carrier M.

**Proof.** The index map (n,d,k)↦(n,d^+,k+δ(n,d)) is bijective. Indeed, for
an output (n,d',k'), let d^- be the predecessor of d' in D_n; then the unique
input integer is

\[
k=k'-\delta(n,d^-).
\]

The matrix inverse is integral,

\[
A_\delta^{-1}=\begin{pmatrix}1&-(1+\delta)\\-1&2+\delta\end{pmatrix},
\tag{7}
\]

because det A_δ=1. Hence

\[
F^{-1}(n,d',k',z')=\bigl(n,d^-,k'-\delta(n,d^-),A_{\delta(n,d^-)}^{-1}z'\bigr).
\tag{8}
\]

On each real plane, an integral 2×2 matrix of determinant one preserves the
standard area form. Writing z'=(Q,P)=A_δ(q,p),

\[
dQ\wedge dP=\det(A_\delta)\,dq\wedge dp=dq\wedge dp.
\]

The componentwise maps are smooth and the countable disjoint union has the
componentwise smooth structure. Thus F^*ω=ω and (8) proves global
invertibility. No centre, momentum slice, or prime component was selected.
\(\square\)

### Proposition 2 — Complete unit-roof suspension

The quotient (5) carries a complete translation flow for all real times.

**Proof.** Every crossing consumes exactly one unit of time. Thus any bounded
time interval contains finitely many crossings in either direction, and (8)
gives the unique backward continuation at each crossing. Equivalently,
inf_M τ=1>0 is a uniform non-Zeno bound. The endpoint identification in (5)
therefore defines φ^t for all t∈R. \(\square\)

## 5. Full periodic ledger

### Proposition 3 — Prime packets and composite k-drift

The complete periodic set of F is (6). For a prime p and fixed k∈Z, its
p−1 states have least period p−1. No state over a composite n is periodic.

**Proof.** The phase coordinate advances by one in the cyclic set D_n, so any
return after m steps requires

\[
m=r(n-1)\quad\text{for some integer }r\ge1.
\tag{9}
\]

After one complete phase cycle the integer register has changed by

\[
D_n:=\sum_{d=1}^{n-1}\delta(n,d)
=\sum_{d=1}^{n-1}(\gcd(n,d)-1).
\tag{10}
\]

If n is composite, it has a proper divisor a with 1<a<n. The summand at d=a
is a−1>0, while every summand is nonnegative; hence D_n>0. After
m=r(n−1) steps, k has changed by rD_n>0, so no composite state can return,
regardless of z.

If n=p is prime, gcd(p,d)=1 for every 1≤d<p. Therefore δ(p,d)=0, D_p=0,
and k is constant. The geometric matrix is always A_0. Its eigenvalues are

\[
\lambda_\pm=\frac{3\pm\sqrt5}{2},\qquad \lambda_+>1,\quad
0<\lambda_-<1,\quad\lambda_+\lambda_-=1.
\tag{11}
\]

For a return with m=r(p−1), the geometric condition is A_0^m z=z. Neither
eigenvalue has a positive integral power equal to one, so 1 is not an
eigenvalue of A_0^m and this forces z=0. Conversely, every (p,d,k,0) is
carried to (p,d^+,k,0), and the phase requires exactly p−1 steps to return.
No smaller positive time returns the phase, so the least period is p−1. This
includes p=2, where D_2={1} and the period is one. \(\square\)

### Corollary 4 — Countably many prime packets

For each prime p, define

\[
\mathcal C_{p,k}=\{(p,d,k,0):d\in D_p\},\qquad k\in\mathbb Z.
\tag{12}
\]

Each C_{p,k} is one primitive base orbit and one primitive unit-roof flow orbit
of period p−1. The packets are pairwise disjoint and there are countably
infinitely many of them for each p, hence countably many in total.

**Proof.** Proposition 3 gives the exact orbit and period statements. Distinct
k's lie in distinct connected components of the carrier and cannot be
identified by the endpoint quotient. Since the set of primes and Z are both
countable, the total packet family is countable. \(\square\)

## 6. Clock, repetition, and the two A1 stops

The roof is identically one, so the primitive flow period of (12) is

\[
T_{p,k}=\sum_{j=0}^{p-2}\tau(F^j x)=p-1.
\tag{13}
\]

An r-fold traversal of the same primitive orbit has T_{p,k}^{(r)}=r(p−1).
This is the only clock in the frozen candidate. In particular, the exact
construction does not yield T_{p,k}=log p, nor does it provide an endogenous
change of time units that would do so.

The complete same-object ordinary primitive Euler product and its repetition
logarithm would have the formal shapes

\[
Z(s)=\prod_{p\ {\rm prime}}\prod_{k\in\mathbb Z}
\bigl(1-e^{-s(p-1)}\bigr)^{-1},\qquad
\log Z(s)=\sum_{p\ {\rm prime}}\sum_{k\in\mathbb Z}\sum_{r\ge1}
\frac{e^{-sr(p-1)}}{r}.
\tag{14}
\]

There is one Euler factor per primitive packet (p,k); repetitions occur in
the logarithm and are not additional primitive Euler factors. Neither formal
expression is asserted as a determinant or a convergent zeta function.
For every real part σ=Re s>0, the absolute repetition-logarithm series contains

\[
\sum_{k\in\mathbb Z}e^{-\sigma(p-1)}=\infty
\]

already for one fixed prime and r=1. For σ≤0, the factors do not approach one.
Thus the full ledger has no ordinary absolute-convergence half-plane. This is
an exact multiplicity stop, independent of any operator choice. The clock
mismatch (13) and the countable k-multiplicity are the decisive A1 scoped
failures.

**Normalization correction (2026-09-18).** An earlier display of (14)
incorrectly added an Euler factor for each repetition r. The display above
corrects that double counting without changing the candidate, clock, packet
ledger or divergence conclusion: the r=1 subseries alone already diverges.

## 7. Controls and adverse findings

All controls below are comparisons, not repairs of the frozen candidate.

### 7.1 Indicator-divisor comparator

Replace (1) by

\[
\delta_{\rm ind}(n,d)=\mathbf 1_{\{2\le d<n,\ d\mid n\}}.
\]

The same phase and k-update proof gives zero drift for primes and positive
drift for composites, so the prime/composite ledger survives while the defect
magnitude changes. This shows that the classification uses the zero-versus-
positive property, not a fitted numerical size. It also confirms that no
special use of a prime table is hidden in the gcd values.

### 7.2 Single-cycle shuffled phase order

Let σ_n be any fixed single-cycle permutation of D_n, chosen without looking
at target periods, and replace d^+ by σ_n(d) while leaving the same δ(n,d) and
A_δ. The phase still returns only after n−1 steps and the sum (10) is
unchanged. Hence prime packets remain period p−1 and composite k-drift
remains positive. The control shows that cyclic order is not an unacknowledged
logarithmic clock. A non-single-cycle permutation would be a different
candidate and can create different packet periods; it is not silently
substituted here.

### 7.3 Forgetting k is not a same-object repair

The projection π(n,d,k,z)=(n,d,z) is many-to-one. It yields the semiconjugate
map (n,d,z)↦(n,d^+,A_{δ(n,d)}z), but it removes the only return obstruction
on composite fibres: z=0 is then periodic for every n, including composites.
Thus the projection changes the complete periodic ledger and cannot collapse
the k-multiplicity while preserving the candidate. Any quotient requiring a
new orbit convention needs a new card.

### 7.4 A_0-decoupled geometry control

Set every phase matrix to A_0 while retaining the gcd k-cocycle. The prime
packets and composite no-return theorem are unchanged, because those
statements are controlled by (10). This control isolates the arithmetic source
in the k-register and confirms that the matrix selector is not being credited
with the prime/composite exclusion. It also warns against claiming that the
linear geometry itself supplies a natural arithmetic mechanism.

### 7.5 Ownership and PROVES_TOO_MUCH boundaries

The proofs use all real z, all k, every integer fibre, the same map, and the
unit roof. Selecting z=0, one k, or only prime n would be an impermissible
postselection. No physical roof, determinant, or trace from another package is
imported. The exact geometric result therefore remains a same-object control,
while source naturalness and any analytic owner remain open.

## 8. Gate assessment

| Gate | Evidence for this exact candidate | Status | Limitation / next obligation |
| --- | --- | --- | --- |
| A0 | Endogenous gcd(n,d)−1 drives both the integer cocycle and matrix selector; exact prime/composite distinction is proved without a prime table | SCOPED POSITIVE (operational source) | Natural source-to-target relation and a logarithmic clock are not established |
| A1 | Full periodic ledger and repetition convention are proved, but periods are p−1 and there are countably many k-packets per prime | SCOPED FAIL | Stop/fork before tuning the roof or projecting k |
| A2 | No transfer operator, trace, zeta, or determinant owner is supplied; (14) has no absolute-convergence half-plane | NOT EVALUATED | A new frozen analytic owner would be required, with no inherited credit |
| Route B | No Route-A readiness and no separate authorization | NOT INVOKED | Remains unavailable |

## 9. Conclusion and decision

Candidate ASFS-20260918-GDC01 is retained as an exact geometric and arithmetic
control. The one-object ledger is intact: the gcd source, phase scan, k-cocycle,
matrix action, unit roof, primitive convention, and repetition law all belong
to (2)–(5). The candidate stops at A1 because its actual clock is p−1 and its
full ledger has countably infinite prime multiplicity. The correct portfolio
position is **stop / fork**. A future logarithmic or multiplicity-reduced
design must receive a fresh candidate ID; it may not borrow this candidate's
periodic theorem or roof.

## Reproducibility / evidence index

- [Frozen candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and verification record](evidence/README.md)

The statements above are symbolic proofs over the complete countable carrier,
not finite numerical evidence. Verification checks, ownership boundaries, and
the no-root-edit diff check are recorded in the evidence file.
