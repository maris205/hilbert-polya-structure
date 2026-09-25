# Prime-only nondegenerate packets in one coupled witness Hénon map

**Paper ID:** 152-coupled-witness-henon-escape  
**Candidate ID:** ASFS-20260915-CHE01  
**Date:** 2026-09-15  
**Status:** ADVANCE — PRIME-ONLY NONDEGENERATE HÉNON PACKETS; ROUNDED CLOCK AND OPERATOR OPEN.  
**Evidence class:** exact full-state proof; no numerical claim.  
**Route state:** owner-level arithmetic, complete orbit and ordinary-zeta
results only; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

We study the already frozen four-dimensional generalized Hénon map whose
potential depends, by one uniform rule, on the number of proper-divisor
witnesses of every integer label. All integer components and all their real
coordinates belong to its phase space. On composite components, a strictly
positive force component makes the sum of a hypothetical periodic recurrence
impossible. On prime components, the full recurrence is linear and
hyperbolic, forcing every periodic real coordinate to be zero. Thus there is
exactly one primitive cycle per prime, no composite cycle, no additional
continuous family, and no degenerate prime repetition. The frozen phase
length is \(K_p=\max(1,\lfloor\log_2(p-1)\rfloor)\); the unit-roof flow's
ordinary unweighted zeta has logarithmic-series absolute-convergence
abscissa \(\log 2\). This establishes a same-object arithmetic/geometry/orbit
chain, not an exact prime-log clock or a transfer-operator trace identity.
The complete divisor count is recomputed at every macrostep; the construction
remains a generic constraint-realization mechanism whose privileged Riemann
naturalness is unproved.

## 1. Candidate identity and same-object ledger

The [version-1 card](candidate-card.md) was frozen before this audit. Put
\[
a(n)=\sum_{d=2}^{n-1}1_{\{d\mid n\}},\qquad
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad n\geq2.
\]
An empty sum is zero. Write \(k\in\mathbb Z/K_n\mathbb Z\), with
\(k^+=k+1\). For \(X=(x,y)\), define exactly
\[
V_a(x,y)=\frac{1-a}{2}\big((x+y)^2+y^2\big)
             +a\big(e^{x+y}+e^y\big).
\tag{1}
\]
The full map, with no omitted states, is
\[
M=\coprod_{n\geq2}\coprod_{k\in\mathbb Z/K_n\mathbb Z}
       \mathbb R^4_{n,k},\quad
\omega=\sum_{i=1}^{2}dQ_i\wedge dP_i,
\]
\[
F(n,k,Q,P)=
\bigl(n,k^+,P,\,2P-Q+\nabla V_{a(n)}(P)\bigr).
\tag{2}
\]

| Item | Frozen owner | Audit state |
| --- | --- | --- |
| Phase space | All displayed real components of \(M\), canonical \(\omega\) | Smooth noncompact, disconnected four-dimensional symplectic manifold |
| Map and coefficients | Exactly (1)--(2), all-integer finite divisor rule | Global symplectomorphism, proved below |
| Arithmetic | Every \(d=2,\ldots,n-1\) is tested inside each update | No supplied prime list or primality flag |
| Phase and clock | Cyclic \(k\), unit roof \(\tau=1\) | Genuine macrotime; no elementary-cost claim |
| Flow | Endpoint quotient \((x,1)\sim(Fx,0)\) | Complete five-dimensional suspension |
| Measure | Counting over components times Lebesgue volume; suspension Lebesgue time | Invariant and sigma-finite; no finite invariant probability claimed |
| Coding | Witness observations and intrinsic cyclic phase | No claimed conjugacy to a full prime-symbolic source |
| Periodic data | Entire periodic set of (2), oriented cycles modulo phase | Classified for all \(n\) and all periods |
| Analytic object | Ordinary unweighted \(Z\), with repetition weight one | Defined from this complete unit-roof ledger |
| Operator, domain, trace | None constructed | OPEN |
| Later Hamiltonian/contact/quantum owner | None constructed | DEFERRED |

The suspension is
\[
M_1=(M\times[0,1])/\bigl((x,1)\sim(Fx,0)\bigr)
\]
with flow induced by translation of the second coordinate. The map is
globally invertible and the roof is bounded below by one, so the flow exists
for all real times. This five-dimensional manifold is not being called
symplectic or Hamiltonian.

## 2. Question and claim boundary

Can a direct coupled Hénon potential own both prime-exclusive periodic data
and nondegenerate monodromy without selecting an invariant centre or adding
an unrelated hyperbolic factor?

The answer is yes for the exact constructor (2): the full periodic set is
\[
\operatorname{Per}(F)
=\{(p,k,0,0):p\text{ prime},\ k\in\mathbb Z/K_p\mathbb Z\}.
\tag{3}
\]
Its monodromy is part of that same map. This is a theorem about the frozen
constructor, not an assertion that arbitrary sieve systems have this
geometry.

The period is only logarithmic-order macrotime. We claim no exact
\(\log p\) period, von Mangoldt trace, Riemann divisor identity, global
analytic continuation, trace-class operator, quantization, or Route pass.
No periodic set, clock, stability matrix, or zeta is imported from another
candidate.

## 3. Lineage, inputs, and provenance

The [prior-work lineage](../../docs/prior_work/README.md) begins with
prime/composite observables and their symbolic exclusion constraints, then
motivates a conservative Hénon-dimensional realization. This candidate
realizes the specific arrow
\[
\bigl(1_{\{d\mid n\}}\bigr)_{2\leq d<n}
\longrightarrow a(n)
\longrightarrow\nabla V_{a(n)}
\longrightarrow\text{intrinsic periodic-orbit exclusion}.
\tag{4}
\]
The retained arithmetic condition is exactly the vanishing of every
proper-divisor witness, not a supplied prime word. Its deformation consists
of aggregating that finite nonnegative witness list into the coupled
potential (1). The geometric realization is a direct four-dimensional
generalized Hénon recurrence with symmetric force derivative.

All integers \(n\geq2\) are present before evolution; no prime-selected
submanifolds are used to define the carrier. The elementary divisibility
rule and the fixed quadratic/exponential interpolation are permitted inputs.
Nevertheless, evaluating a complete finite constraint is not the same as
proving an autonomous enumeration of primes from one low-dimensional seed.
There is no such enumeration claim here.

The clock is also explicit engineering: \(K_n\) is a binary phase length for
every integer, independent of the outcome of the witness test. Every
application of (2) evaluates the complete list of \(n-2\) direct tests.
The \(K_n\) steps do not partition one scan. Therefore one primitive prime
period evaluates \(K_p(p-2)\) tests under this stipulated direct implementation,
not \(K_p\) elementary tests. No Riemann-zero or per-prime parameter data were
used.

## 4. Exact proof

### 4.1 Full global geometry

The inverse of (2) is, with \(a=a(n)\),
\[
F^{-1}(n,k',Q',P')
=\bigl(n,k'-1,\,2Q'-P'+\nabla V_a(Q'),\,Q'\bigr).
\tag{5}
\]
Every coordinate in (5) is finite for every real input, and both maps are
smooth on every component. The countable disjoint union is Hausdorff and
second countable, with ordinary four-dimensional smooth charts.

Set \(S(P)=2I+\nabla^2V_a(P)\). It is symmetric. Differentiating (2) gives
\[
dQ'=dP,\qquad dP'=-dQ+S(P)dP,
\]
and consequently
\[
F^*\omega
=\sum_i dP_i\wedge(-dQ_i)
 +\sum_{i,j}S_{ij}(P)dP_i\wedge dP_j
=\omega.
\tag{6}
\]
The second sum vanishes by symmetry. Thus this is an actual positive-dimensional
symplectomorphism, not merely an invertible or volume-preserving rule.

### 4.2 Composite exclusion on all real states

Define
\[
g_a(t)=(1-a)t+ae^t.
\]
The potential has the coupled gradient
\[
\nabla V_a(x,y)=
\bigl(g_a(x+y),\,g_a(x+y)+g_a(y)\bigr).
\tag{7}
\]
If \(a\) is a positive integer, then
\[
g_a(t)=e^t+(a-1)(e^t-t)>0
\quad(t\in\mathbb R),
\tag{8}
\]
because \(e^t-t\geq1\). In particular the second coordinate of (7) is
strictly positive at every point.

Suppose an arbitrary state of a composite component were \(m\)-periodic.
Its label \(n\), and therefore \(a=a(n)\geq1\), remain fixed. Write its
coordinate history as \((Q_t,P_t)\), with indices modulo \(m\).
The first equation of (2) implies \(Q_t=P_{t-1}\), so
\[
P_{t+1}-2P_t+P_{t-1}=\nabla V_a(P_t).
\tag{9}
\]
Summing (9) over all \(t\) makes the left side zero. The second coordinate
of the right side is a sum of strictly positive numbers by (8), a
contradiction. This excludes every period and every continuous state over
every composite. It does not assume boundedness of arbitrary nonperiodic
trajectories or assert a particular escape rate.

### 4.3 Prime components: complete periodic set and hyperbolicity

For prime \(p\), the divisor sum is zero. Equation (1) is quadratic and
\[
\nabla V_0(P)=CP,\qquad
C=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]
Thus the real-coordinate update is the fixed matrix
\[
J=\begin{pmatrix}0&I\\-I&2I+C\end{pmatrix}.
\tag{10}
\]
The eigenvalues of the real symmetric matrix \(C\) are
\[
\nu_\pm=(3\pm\sqrt5)/2>0.
\]
An orthogonal change of both \(Q\) and \(P\) diagonalizes \(C\) and preserves
\(\omega\). In each resulting two-dimensional block the update is
\[
B_\nu=\begin{pmatrix}0&1\\-1&2+\nu\end{pmatrix},
\]
with eigenvalues
\[
\lambda_\nu^\pm
=\frac{2+\nu\pm\sqrt{(2+\nu)^2-4}}2,\qquad
\lambda_\nu^+>1,\quad
0<\lambda_\nu^-<1,\quad
\lambda_\nu^+\lambda_\nu^-=1.
\tag{11}
\]
No eigenvalue of \(J^m\) is one for any integer \(m\geq1\).
Therefore \(J^mZ=Z\) forces \(Z=0\). Conversely zero is fixed by (10).
The full phase still advances by one at each step, so the \(K_p\) zero
states form one primitive map cycle of least period exactly \(K_p\).
This proves (3), including the small cases \(p=2,3\), each with one
distinct period-one cycle.

The monodromy of the primitive \(p\)-cycle is \(J^{K_p}\); for its
\(r\)-fold traversal it is \(J^{rK_p}\). For every \(m\geq1\),
\[
\det(I-J^m)
=\prod_{\nu\in\{\nu_-,\nu_+\}}
 \left(2-(\lambda_\nu^+)^m-(\lambda_\nu^-)^m\right)>0.
\tag{12}
\]
Each factor is strictly negative since \(u+u^{-1}>2\) for \(u>1\).
All prime cycles and their repetitions are consequently hyperbolic and
nondegenerate. This transverse claim does not exclude the usual flow
direction of a suspended closed orbit; (12) is the return-map determinant.
It is not itself a trace formula.

### 4.4 The full flow packet and repetition convention

Under the unit roof, the \(K_p\) phase points are the intersections of one
oriented primitive flow orbit \(\gamma_p\) with the section. They are not
\(K_p\) separate flow packets. Conversely any closed orbit of the suspension
meets that section and gives a periodic point of \(F\), so (3) supplies the
complete flow ledger, with no omitted composite or continuous packets.

Using the orientation of forward suspension time and identifying cyclic
phase shifts,
\[
T_{\gamma_p}=K_p,\qquad T_{\gamma_p^r}=rK_p.
\tag{13}
\]
There is one primitive packet for each prime even if distinct primes have
the same length. No orientation reversal is counted as a second packet.

## 5. Same-object ordinary zeta

The frozen analytic proposal is the ordinary unweighted product, not a
stability-weighted determinant:
\[
\log Z(s)=\sum_{p\ \mathrm{prime}}\sum_{r\geq1}
             \frac{e^{-srK_p}}r,\qquad
Z(s)=\prod_{p\ \mathrm{prime}}(1-e^{-sK_p})^{-1}.
\tag{14}
\]
The appearance of primes in (14) is the consequence of (3), not an input
restriction in (2). Both (13) and (14) use the same unit roof. Formula
(12) has not been inserted into these weights.

We give a fresh convergence proof. For \(\sigma=\Re s>\log2\), put
\(\alpha=\sigma/\log2>1\). For \(p\geq3\),
\[
K_p>\log_2(p-1)-1,\qquad
e^{-\sigma K_p}\leq e^\sigma(p-1)^{-\alpha}.
\]
The sum over all integers of the latter bound converges. Also \(K_p\geq1\),
so
\[
\sum_p\sum_{r\geq1}\frac{e^{-\sigma rK_p}}r
\leq \frac{1}{1-e^{-\sigma}}\sum_pe^{-\sigma K_p}<\infty.
\tag{15}
\]
The same bound on closed right half-planes proves normal convergence.
Thus (14) defines a holomorphic nonzero function for \(\Re s>\log2\).

At \(\sigma=\log2\), one has \(2^{-K_p}\geq1/p\) for every prime.
The elementary divergence of \(\sum_p1/p\) is sufficient here; for
completeness, if that sum converged, the finite products
\(\prod_{p\leq N}(1-1/p)^{-1}\) would be bounded, since
\(-\log(1-1/p)\leq2/p\). But expanding such a finite product into its
nonnegative geometric terms includes \(1/n\) for every \(n\leq N\),
by unique prime factorization, so it is at least
\(\sum_{n=1}^{N}1/n\), which is unbounded. This contradiction proves
the required divergence.

The \(r=1\) subseries of (14) therefore diverges absolutely on
\(\Re s=\log2\), and on every smaller real part by termwise comparison.
Its exact absolute-convergence abscissa is \(\log2\). This proves no
natural boundary and no meromorphic continuation statement.

As a consistency identity, for any integer \(m\geq1\),
\[
\#\operatorname{Fix}(F^m)
=\sum_{\substack{p\ \mathrm{prime}\\K_p\mid m}}K_p<\infty.
\tag{16}
\]
Finiteness follows because \(K_p\leq m\) implies \(p\leq2^{m+1}+1\),
with the small prime \(2\) included separately if needed. In the same
convergence region, expansion of
\(\sum_{m\geq1}\#\operatorname{Fix}(F^m)e^{-sm}/m\) gives exactly
(14). This is an orbit-count identity, not a trace on a specified
function space.

## 6. Controls and adverse findings

The following are counterfactual controls of the formula, not changes to
ASFS-20260915-CHE01 and not separately promoted candidates.

| Control | Exact result | What it distinguishes |
| --- | --- | --- |
| Force \(a=0\) for every integer | Every \(n\) has one hyperbolic primitive \(K_n\)-cycle | Generic geometry and binary clock alone do not select primes |
| Replace the sum by \(a=n-2\) | Only \(n=2\) retains a packet; all \(n\geq3\) have positive force | The presence of an arithmetic test, not simply an integer-dependent coefficient, selects the ledger |
| Replace the summand by \(1_{\{d\mid n+1\}}\), still \(2\leq d<n\) | Surviving labels are \(n=2\) and those \(n\geq3\) with \(n+1\) prime | Changing the tested integer changes the selection; the geometry is not secretly hard-coded to the original prime set |
| Retain every continuous state | Equations (8)--(11) exclude every additional periodic state | No centre/section selection repairs multiplicity |
| Change the roof | Not executed; it would be a new candidate | No unit-time zeta is credited to a different physical time |
| Replace divisor witnesses by another finite nonnegative integer witness count | The same proof selects precisely its zero-count labels | Explicit PROVES_TOO_MUCH limit on claims of privileged arithmetic naturalness |

For the shifted control and \(n\geq3\), if \(n+1\) is composite it has a
proper divisor \(d\leq\sqrt{n+1}<n\), so at least one displayed test is
positive. If \(n+1\) is prime there is none. For \(n=2\) the interval is
empty. In particular \(n=3\) does not survive that control, because
\(2\mid4\). These exact controls require no randomized cutoff experiment.

This is a fixed construction, not a sweep of potential parameters. Its
interpolation is deliberately selected to combine a hyperbolic zero-witness
branch with a monotone-force positive-witness branch. The wider
constraint-realization fact is a real limitation on naturalness, not a
reason to deny the proved source and full-periodic-set identities.

Binary rounding remains an adverse clock finding:
\[
K_p=\frac{\log p}{\log2}+O(1),
\]
but all lengths are integers and distinct primes can share one length.
No constant rescaling identifies these with all exact \(\log p\).
In particular \(K_2=K_3=1\), whereas \(\log2\ne\log3\).
The prime-power arithmetic is represented only by repeated traversals in
(13), not by a separately proved arithmetic trace law.

## 7. Gate assessment

| Gate | Evidence for this frozen candidate | Status | Remaining boundary |
| --- | --- | --- | --- |
| P0 | Exact full carrier, smooth symplectic map, roof, all data and controls | ESTABLISHED | No finite invariant probability claimed |
| Owner-level A0 source | Executed proper-divisor constraints select exactly prime periodic components; three altered-source controls | ESTABLISHED, scoped arithmetic mechanism | Generic constraint engineering and target naturalness remain explicit limitations |
| Owner-level A0 clock | Exact \(K_p=\log p/\log2+O(1)\) from the chosen all-integer phase | Time ownership ESTABLISHED; source-derived clock OPEN | Not a derived batch-scan duration, exact \(\log p\), or elementary computation time |
| Owner-level A1 | Full all-state periodic classification, one packet per prime, every repetition, hyperbolic monodromy | ESTABLISHED | No additional packet selection or borrowed stability |
| Owner-level A2 ordinary zeta | Equation (14) from the same roof and complete ledger; exact abscissa | ESTABLISHED, ordinary product only | Operator/domain/trace and continuation OPEN |
| Formal Route A | No target/divisor protocol evaluation | UNASSIGNED | No Route-A pass or readiness statement |
| Route B | Not evaluated or invoked | NOT INVOKED | No Hilbert-space, spectral or self-adjointness claim |

## 8. Conclusion and decision

**Advance** this bounded constructor result: a direct coupled symplectic
Hénon map simultaneously owns prime-exclusive packets and nondegenerate
monodromy, with no passive factor and no post-selection. Its ordinary
zeta is already established at the owner level, so further local
period searches or witness tuning would add little.

The next relevant obligation is a separately scoped same-object
operator/trace construction or a genuinely new clock architecture.
Nondegeneracy removes one obvious local denominator obstruction, but
does not establish a trace formula, its function space, summability,
normalization, or target relevance. A new roof or potential gets a new ID;
no such fork is silently made here.

## Reproducibility / evidence index

- [Frozen identity and adjudication](candidate-card.md).
- [Scoped claim ledger](claim-ledger.md).
- [Exact derivation and verification record](evidence/README.md).

All mathematical results are derived above from the displayed definitions.
No numerical cutoff, precision choice, prime table, external theorem beyond
the elementary facts proved or explicitly used here, or Riemann-zero input
is part of the evidence.
