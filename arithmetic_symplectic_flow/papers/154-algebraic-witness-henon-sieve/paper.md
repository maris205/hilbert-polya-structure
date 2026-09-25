# A fixed algebraic witness force with prime-only hyperbolic Hénon packets

Paper ID: 154-algebraic-witness-henon-sieve.  
Candidate ID: **ASFS-20260915-AWH01**.  
Date: 2026-09-15.  
Status: **PRIME-ONLY HYPERBOLIC SYMPLECTIC PACKETS AND ORDINARY ZETA ESTABLISHED; TARGET CLOCK AND OPERATOR OPEN.**  
Route state: owner-level arithmetic/orbit and ordinary-zeta results only;
formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

On a countable disjoint union of complete real symplectic planes, indexed by
every integer \(n\geq2\) and a cyclic binary-length phase, we define one
Hénon-form map using the actual number \(a(n)\) of proper divisor witnesses.
Its force is \(g_a(t)=(1-a)t+a\sqrt{1+t^2}\). For integral \(a\geq1\), this
force is strictly positive everywhere; a complete periodic-sequence sum
therefore excludes every composite periodic state. For \(a=0\), the entire
plane map becomes a fixed linear hyperbolic symplectomorphism, whose only
periodic point is its origin. Thus the full intrinsic ledger has precisely
one primitive phase cycle per prime, with nondegenerate hyperbolic
monodromy, and no other cycles. The same unit-roof suspension owns its
ordinary unweighted zeta and all repetitions. We prove its logarithmic
series has absolute-convergence abscissa \(\log2\) without prime-number
asymptotics. The clock is an explicit rounded binary macroclock, not exact
\(\log p\), and the witness aggregation is not a logarithmic-time
computation. General constraint-encoding controls delimit arithmetic
naturalness. No operator trace or formal Route conclusion is asserted.

## 1. Candidate identity and same-object ledger

The [version-1 card](candidate-card.md) preceded this proof. Every definition
below belongs to that card, not to a combination of previous packages.

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Phase space | \(M=\coprod_{n\geq2,\ k\in\mathbb Z/K_n\mathbb Z}\mathbb R^2\), canonical \(dq\wedge dp\) on each plane | Exact, full carrier |
| Integer phase | \(K_n=\max(1,\lfloor\log_2(n-1)\rfloor)\), \(k^+=k+1\bmod K_n\) | Exact all-integer rule |
| Arithmetic source | \(a(n)=\sum_{2\leq d<n}\mathbf1_{d\mid n}\), evaluated in each update | Elementary divisibility; no supplied prime flag |
| Base map | \(F(n,k,q,p)=(n,k^+,p,2p-q+g_{a(n)}(p))\) | One real-analytic symplectomorphism |
| Force | \(g_a(t)=(1-a)t+a\sqrt{1+t^2}\), positive real square root | Frozen coefficients, no tuning |
| Roof / flow | \(\tau=1\), endpoint-glued unit suspension | Complete forward/backward flow |
| Measure | Canonical area on every component, times unit time on the suspension | Infinite; no finite normalization asserted |
| Primitive ledger | All intrinsic full-state periodic orbits, modulo cyclic starting point | Exhaustively proved below |
| Analytic object | Ordinary \(Z\), weights one, full primitive ledger | Logarithmic series normally convergent for \(\Re s>\log2\) |
| Other analytic owners | Transfer operator, function space, domain, trace, Fredholm determinant | OPEN |
| Later lifts | Contact / Hamiltonian / quantum realization | NOT CONSTRUCTED |

There are countably many components, each with its usual countable rational
ball basis. Hence \(M\) is a Hausdorff, second-countable, noncompact,
disconnected smooth manifold of dimension two. The suspension has dimension
three. No symplectic form on that odd-dimensional suspension, or Hamiltonian
generator for it, is inferred from the symplectic base.

## 2. Question and claim boundary

The question is whether one fixed, direct Hénon-form force can preserve
prime-only packets while making every surviving full-state packet
hyperbolic. A passive hyperbolic factor or a borrowed monodromy does not
answer that question.

The strongest result is the following exact statement: for every integer
\(n\), the \(n\)-fibre has a periodic point if and only if \(n\) is prime;
in that case its complete periodic set is
\(\{(n,k,0,0):k\in\mathbb Z/K_n\mathbb Z\}\), one primitive cycle of length
\(K_n\), with monodromy \(B^{K_n}\), where
\[
B=\begin{pmatrix}0&1\\-1&3\end{pmatrix}.
\]
All assertions quantify over the full real planes and arbitrary periods.

This is not a claim of exact prime-log timing, a uniquely canonical
arithmetic geometry, a natural Markov coding, a global zeta continuation,
an operator determinant, zero matching, or a formal Route pass.

## 3. Definitions, arithmetic origin, and provenance

For an integer \(n\geq2\), primality is equivalent to \(a(n)=0\). A composite
integer has at least one integer divisor \(2\leq d<n\), so \(a(n)\geq1\).
All integers are included before that distinction is made; the formula does
not receive a prime table or a precomputed list of surviving components.

The lineage arrow from the [prior-work guide](../../docs/prior_work/README.md)
is precise: the prime/composite divisor-exclusion symbol is replaced by its
complete nonnegative integer witness count, and that count acts inside a
two-dimensional conservative Hénon recurrence. The mechanism is a stated
arithmetic-constraint realization, not a claim that a previous Logistic
map has already been conjugated to this new object.

The uniform complete-count update is also distinct from executing one
divisor test per unit time. Each map step performs \(n-2\) direct tests.
A complete \(K_n\)-phase cycle performs \(K_n(n-2)\) tests, even when
the point itself remains at the transverse origin. An implementation may
cache a computed count, but that is not a new dynamical complexity theorem.

The phase rule counts a rounded binary scale for every integer, and the
roof remains exactly one. For primes tending to infinity,
\[
K_p=\frac{\log p}{\log2}+O(1).
\]
This is an owned macroclock and supplies a logarithmic-order relation. It
is not an exact \(\log p\) period, a computational running time, or a
derivation of a physical clock. Different primes can have the same \(K_p\);
the integer label distinguishes their different intrinsic cycles.

The positive square-root branch is smooth and real analytic on the entire
real line. The map is real algebraic in that sense; it is not being called
a polynomial Hénon automorphism or an entire holomorphic map.

## 4. Global symplectic geometry

Write \(Q=p\) and \(P=2p-q+g_a(p)\). The inverse is explicitly
\[
F^{-1}(n,k',Q,P)
 =\bigl(n,k'-1\bmod K_n,\ 2Q+g_{a(n)}(Q)-P,\ Q\bigr).
\]
It exists at every real point, is smooth, and reverses the discrete phase.
Moreover,
\[
dQ\wedge dP
 =dp\wedge\bigl(-dq+(2+g_a'(p))\,dp\bigr)
 =dq\wedge dp.
\]
This proves global symplecticity without restricting to the later periodic
set. The plane derivative has determinant one everywhere.

Define
\[
M_1=\{(x,u):x\in M,\ 0\leq u\leq1\}/
 ((x,1)\sim(Fx,0)).
\]
Translation in \(u\), followed by this endpoint gluing, defines the
suspension flow. The complete map and its inverse are available at every
integer crossing, and every crossing costs one time unit. No finite-time
accumulation of crossings occurs. This proves forward and backward
completeness even when real coordinates escape at infinite time.

## 5. Complete periodic-state theorem

### 5.1 Composite exclusion

For every real \(t\), let \(R(t)=\sqrt{1+t^2}\). Since \(R(t)>|t|\),
for an integer \(a\geq1\),
\[
g_a(t)=R(t)+(a-1)(R(t)-t)>0.                 \tag{1}
\]

Suppose an arbitrary state in an \(n\)-fibre has a full period \(m\geq1\).
The phase condition first requires \(K_n\mid m\). Writing its real
coordinates as \((q_j,p_j)\) with periodic indices,
\[
p_j=q_{j+1},\qquad
q_{j+2}-2q_{j+1}+q_j=g_{a(n)}(q_{j+1}).
\]
Summing this exact equation over one full period gives
\[
0=\sum_{j=0}^{m-1}g_{a(n)}(q_{j+1}).         \tag{2}
\]
If \(n\) is composite, every summand is strictly positive by (1), a
contradiction. Thus no composite fibre has any real periodic point of
any period. The argument makes no compactness, bounded-orbit, numerical
cutoff, or invariant-section assumption.

### 5.2 Prime fibres and primitivity

If \(n=p\) is prime, \(a(p)=0\), so \(g_0(t)=t\). The full plane map,
not merely its derivative at a selected point, is \(z\mapsto Bz\).
Its two distinct positive eigenvalues are
\[
\lambda_+=\frac{3+\sqrt5}{2}>1,\qquad
\lambda_-=\frac{3-\sqrt5}{2}=\lambda_+^{-1}<1.
\]
For every positive \(m\), neither eigenvalue of \(B^m\) equals one.
Consequently \((B^m-I)z=0\) implies \(z=0\).

The complete periodic set in a prime fibre is therefore exactly its
\(K_p\) origins, and the phase successor permutes those origins in a
single cycle. Its least period is \(K_p\), including \(p=2,3\), for
which \(K_p=1\). The two length-one cycles belong to different fibres.
No centres were selected after thickening: the full equations exclude
all other points.

### 5.3 Monodromy and repetitions

The primitive Poincaré monodromy is \(B^{K_p}\); the \(r\)-fold repeat has
monodromy \(B^{rK_p}\). Its multipliers are
\(\lambda_\pm^{rK_p}\), and
\[
\det(I-B^{rK_p})
 =2-\lambda_+^{rK_p}-\lambda_-^{rK_p}<0.     \tag{3}
\]
Every packet and repetition is hyperbolic and nondegenerate in the
transverse Poincaré sense. The flow's tangent direction is not counted
as a transverse multiplier.

The unit suspension of the \(K_p\) points forms one oriented circle orbit,
not \(K_p\) separate orbits and not two time orientations. Its primitive
length is \(T_{\gamma_p}=K_p\), with
\[
T_{\gamma_p^r}=rK_p.
\]
Because every closed suspension orbit meets a base section and has an
integer number of unit crossings, there are no additional closed
suspension orbits absent from the base ledger.

## 6. Same-object ordinary zeta and exact convergence boundary

Using only this complete intrinsic ledger and its frozen roof, define
\[
\log Z(s)
 =\sum_{p\ {\rm prime}}\sum_{r\geq1}\frac{e^{-srK_p}}r,
\qquad
Z(s)=\prod_{p\ {\rm prime}}(1-e^{-sK_p})^{-1}.           \tag{4}
\]
All weights in (4) are one. In particular the monodromy denominator (3)
is not silently inserted. This is the ordinary orbit zeta, not an
identified transfer-operator trace or Fredholm determinant.

For \(\sigma=\Re s>0\), absolute convergence of the double series is
equivalent to convergence of \(\sum_p e^{-\sigma K_p}\), since \(K_p\geq1\)
and
\[
e^{-\sigma K_p}
\leq \sum_{r\geq1}\frac{e^{-\sigma rK_p}}r
\leq \frac{e^{-\sigma K_p}}{1-e^{-\sigma}}.             \tag{5}
\]
For \(p\geq3\), the defining floor gives
\[
K_p>\log_2(p-1)-1,\qquad K_p\leq\log_2(p-1).
\]
If \(\sigma>\log2\), then
\[
e^{-\sigma K_p}
\leq e^\sigma(p-1)^{-\sigma/\log2}.
\]
The sum over all integers on the right converges by comparison with
the integral of \(x^{-\sigma/\log2}\). This comparison is uniform on
compact subsets of \(\Re s>\log2\), proving normal absolute convergence.
Thus (4) defines a holomorphic nonvanishing \(Z\) there.

For completeness, the needed opposite comparison requires no prime
number theorem. Suppose \(\sum_p1/p\) were finite. Since
\(-\log(1-1/p)\leq2/p\), the finite products
\(\prod_{p\leq N}(1-1/p)^{-1}\) would be uniformly bounded. But expanding
each finite geometric product over prime factorizations includes every
integer \(1\leq m\leq N\), hence the product is at least
\(\sum_{m=1}^N1/m\). The latter diverges, a contradiction. Therefore
\(\sum_p1/p\) diverges.

At \(\sigma=\log2\), for all primes \(p\geq3\),
\[
e^{-\sigma K_p}=2^{-K_p}\geq(p-1)^{-1}\geq p^{-1}.
\]
The \(r=1\) series already diverges. It also diverges for
\(0<\sigma<\log2\) by monotonicity. For \(\sigma\leq0\), even the
repetition series of a single orbit fails absolute convergence.
Hence the exact absolute-convergence abscissa of the logarithmic
series is \(\log2\).

This does not establish a natural boundary or exclude analytic continuation.
It makes no target divisor claim. The repeated prime labels in (4) are the
proved orbit classification, not arithmetic weights imported into the map.

## 7. Controls, adverse findings, and scope

The following are diagnostic comparisons, not silently substituted
versions of the frozen candidate.

| Control | Exact outcome | What it tests |
| --- | --- | --- |
| Set every witness count to zero | Every integer fibre has one hyperbolic \(K_n\)-cycle | Geometry alone does not select primes |
| Replace every divisibility test by true, so \(a(n)=n-2\) | Only the empty-test fibre \(n=2\) retains a cycle | Witness force really removes periodic states; preserve empty-input edge case |
| Replace \(d\mid n\) by \(d\mid(n+1)\), with the same \(2\leq d<n\) range | A fibre survives iff \(n+1\) is prime; \(n=4\) survives and \(n=3\) does not | Arithmetic labels are acted upon, not decorative |
| Formal real interpolation \(0<a<1\) | A fixed point exists for \(0<a<1/2\); none for \(1/2\leq a<1\) | Do not replace the integer-gap proof by an assertion about every positive real \(a\) |
| Change roof or discard components | Different periods or ledger, thus new owner/card required | No clock or periodic-subset transfer |
| Replace divisibility by an arbitrary computable nonnegative integer witness count | The same proof realizes that count's zero set | PROVES_TOO_MUCH risk for claims of special Riemann naturalness |

For the interpolation row, solving \(g_a(t)=0\) gives
\[
t_*=-\frac{a}{\sqrt{1-2a}}\quad(0<a<1/2).
\]
The pair \((t_*,t_*)\) is a fixed point of its plane map and therefore
yields a phase cycle. Here
\(g_a'(t)\geq1-2a>0\), so its fixed-point monodromy is hyperbolic.
For \(a=1/2\), \(g_a(t)=(t+\sqrt{1+t^2})/2>0\). For
\(1/2<a<1\), positivity follows separately on \(t\geq0\) and \(t<0\)
from \(\sqrt{1+t^2}>|t|\). Thus the exact threshold, not just
nonnegativity, matters. This control does not modify the integer-valued
arithmetic candidate.

The shifted-test statement holds because any composite \(n+1\geq4\)
has a proper divisor at most \((n+1)/2\leq n-1\). The \(n=2\) range
is empty and \(n+1=3\) is prime, so the edge case agrees.

The source is operationally internal: one all-integer rule computes
divisibility witnesses and those witnesses enter the same full map.
Nevertheless the zero-set realization is highly general. Its success
does not establish that this clock and geometry are uniquely natural,
or that a special arithmetic trace structure must follow. No
random-label statistics or numerical resemblance is offered as a remedy.

## 8. Gate assessment

| Gate | Evidence for ASFS-20260915-AWH01 | Status | Limitation |
| --- | --- | --- | --- |
| P0 | Full map, inverse, form, unit suspension, source and owners explicit | ESTABLISHED | Other analytic owners remain explicitly OPEN |
| A0 operational source / clock | Actual divisor witnesses select exactly prime packets; \(K_p=\log p/\log2+O(1)\); adversarial controls explicit | SCOPED POSITIVE | Rounded macroclock and generic constraint realization; stronger natural target-clock relevance OPEN |
| A1 owner-level | Full all-state ledger, one cycle per prime, no composites, exact repetitions and hyperbolic monodromy | ESTABLISHED | No complete Markov coding asserted |
| A2 owner-level ordinary zeta | Exact same-roof product and convergence abscissa \(\log2\) | ESTABLISHED FOR ORDINARY ZETA | Operator, trace, Fredholm realization and continuation OPEN |
| Formal Route A coordinates | No target/divisor evaluation performed | UNASSIGNED | Owner-level results are not formal Route credit |
| Route B | Not invoked | NOT INVOKED | No later-route rescue or operator claim |

## 9. Conclusion and next decision

Decision: **advance** the same-object positive chain to a specifically
frozen analytic-owner question if separately selected by the ongoing
search. The decisive gain is that prime-only full packets and
hyperbolicity coexist in this exact two-dimensional symplectic map.
There is no need to combine the arithmetic equation of one map with the
derivative of another.

Keep the current candidate intact. A different force, clock, roof,
carrier or analytic normalization must receive a fresh card. Exact
prime-log timing and a natural operator/trace remain independent
obligations; neither the ordinary Euler product nor hyperbolicity
settles them. This package makes no novelty, human peer-review,
publication-readiness, or Riemann-target claim.

## Reproducibility and evidence index

- [Candidate card](candidate-card.md): frozen definition and dated outcome.
- [Claim ledger](claim-ledger.md): exact statements and nonclaims.
- [Evidence index](evidence/README.md): proof coverage, commands and limits.
- [Independent model review](evidence/review.md): separately delegated audit.

All results above are mathematical derivations; no finite orbit
enumeration is used as a proof of completeness. The embedded finite check
is only an arithmetic/control regression check. ARS claim-evidence and
counterargument discipline was used in this bounded research package,
not a journal submission or full publication workflow.
