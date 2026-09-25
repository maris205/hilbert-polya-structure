# Natural differential-form flat traces for a prime-selective symplectic map

**Paper ID:** 153-saturated-sieve-flat-trace  
**Candidate ID:** ASFS-20260915-SFT01  
**Date:** 2026-09-15  
**Status:** ADVANCE — FULL-MAP FLAT TRACES AND GRADED ZETA IDENTITY; FREDHOLM AND TARGET CLOCK OPEN.  
**Route:** Owner-level A2 result; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

We specify natural pullback operators on compactly supported differential
forms over a full countably disconnected symplectic surface. Its local
divisor-witness drift generates exactly one intrinsic closed orbit per
prime and no composite periodic points. Each fixed iterate has a finite
global fixed set and nondegenerate graph/diagonal intersections. These
facts allow an actual distributional flat trace of the full return
operator, without restricting its state space to periodic points.
For form degrees zero, one and two, the resulting trace exponentials
satisfy D_0 D_2/D_1=Z, where Z is the same suspension's complete ordinary
prime-packet zeta. The cancellation is supplied by exterior algebra and
the actual monodromy, not by inserted prime weights. Scalar flat-trace
logarithms have exact absolute-convergence abscissa log(4/3); the one-form
and ordinary-zeta logarithms have abscissa log 2. None of these functions
is claimed to be a trace-class Fredholm determinant, an analytic
continuation or a Riemann target identity. The fixed binary macroclock
remains rounded logarithmic-order time.

## 1. Frozen identity and exact operators

The [card](candidate-card.md) predates this analytic audit. For all n>=2 set

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
b(n,k)=\sum_{\substack{2^k\le d<2^{k+1}\\d<n}}1_{\{d\mid n\}},
\]
\[
f_{n,k}(q)=q+\tfrac12\tanh q+K_n b(n,k),
\]
\[
M=\coprod_{n\ge2,\ 1\le k\le K_n}\mathbb R^2,\qquad
\omega=dq\wedge dp,\qquad
F(n,k,q,p)=(n,k^+,f_{n,k}(q),p/f'_{n,k}(q)).
\tag{1}
\]

The full flow is the unit-roof suspension of (1), not a changed physical
clock. Its weighted return acts on the full section M.

For j=0,1,2 define

\[
\mathcal E_j=C_c^\infty(M;\Lambda^jT^*M),\quad
U_j=F^*:\mathcal E_j\longrightarrow\mathcal E_j,\quad
U_{j,s}=e^{-s}U_j.
\tag{2}
\]

These are continuous operators on the usual compact-support test-section
spaces, not operators initially declared on an anisotropic Hilbert space.
All integer fibres and all real phase points belong to their domains.
The full componentwise area measure is used to express their kernels.

| Owner | Exact definition | Scope |
| --- | --- | --- |
| Source | Local proper-divisor witnesses in (1) | No prime table or completed prime flag |
| Geometric base | Full M, omega, F | Disconnected, noncompact dimension two |
| Roof and flow | tau=1 and endpoint-glued suspension | Complete three-dimensional flow |
| Symbols | Intrinsic integer, phase and witness observations | No unrelated Markov clock or coding |
| Primitive ledger | All full-state least-period cycles modulo cyclic phase | Reproved below, not a selected support |
| Transfer owners | Natural pullbacks (2) on full compact-support form spaces | Same unit return clock e^{-s} |
| Traces | Distributional graph-kernel diagonal restriction and integration | Defined only after transversality and compact-support proof |
| Central functions | D_j=exp(-sum_m e^{-sm} tr_flat(U_j^m)/m) | Flat-trace exponentials, not yet Fredholm determinants |
| Comparison | Complete ordinary orbit Z of this same F and roof | Natural graded quotient tested below |
| Later owner | Contact, Hamiltonian, quantum, spectral realization | NOT SUPPLIED |

147 is a separate earlier geometry contract. The current card explicitly
adds the analytic owners that were OPEN there. The argument below checks
the relevant geometry and every analytic step for (1)--(2); it does not
retroactively assign a trace to 147.

## 2. Question, lineage and scope

Does removal of the parabolic obstruction lead to more than a formal
prime-indexed product? Here it leads to actual full-map distributional
flat traces and a natural differential-form identity.

The lineage remains the prior-work divisor-exclusion symbolic constraint,
deformed into a phase-resolved witness drift and its exact cotangent
geometry. No sequence of different primes occurs along one orbit: n is
conserved. The object realizes all integer tests in parallel, not a
conjugacy to the chronological infinite sieve.

The flat-trace terminology follows the graph-kernel diagonal operation
described by Dyatlov and Zworski, Section 2.4. Their compact Anosov
continuation theorem is not invoked: we prove the finite-iterate
transversality and compact restricted support directly for this
noncompact map. The source also illustrates the distinction between
natural form traces and their graded zeta combination.
[Primary source](https://math.berkeley.edu/~zworski/zeta.pdf).

No reference theorem supplies a source, clock, primitive orbit, spectral
continuation or determinant realization for this candidate.

## 3. Geometry and the full periodic ledger

### Proposition 1 — Full geometric owner and all returns

The map (1) is a global smooth symplectomorphism. Its complete periodic
set is

\[
\{(p,k,0,0):p\text{ prime},\ 1\le k\le K_p\}.
\tag{3}
\]

Each prime p contributes exactly one primitive K_p-cycle. At any point
fixed by F^m, the full derivative is

\[
J_m=\operatorname{diag}(\lambda^m,\lambda^{-m}),\qquad\lambda=3/2.
\tag{4}
\]

**Proof.** Every f_{n,k} has derivative
1+(1/2)sech^2 q>1 and differs from q by a bounded function and a
constant. It is therefore an increasing onto diffeomorphism of R.
Recovering the preceding phase and the inverse configuration determines
the inverse momentum uniquely. The canonical one-form obeys
(p/f'(q))d(f(q))=p\,dq, hence F preserves omega.

A putative period m requires m=rK_n. Summing the exact configuration
increments gives

\[
0=\tfrac12\sum_{t=0}^{m-1}\tanh q_t
  +K_nr\,a(n),\qquad
a(n)=\sum_k b(n,k)=\#\{d:2\le d<n,\ d\mid n\}.
\tag{5}
\]

If n is composite then a(n)>=1, and the right side is strictly greater
than m(a(n)-1/2)>0. If n is prime all witnesses vanish. The remaining
configuration map sends every positive q strictly right and every
negative q strictly left, so its only periodic point is zero. At zero,
momentum multiplies by 2/3 at each step, so a full return forces p=0.
Conversely these zero states traverse the complete cyclic phase.
Their least period is K_n; no smaller phase return is possible.

At zero momentum the derivative cross term
-p f''(q)/(f'(q))^2 vanishes, giving the step matrix
diag(3/2,2/3) and (4). Unit roof gives a complete flow, because any finite
time uses finitely many iterates of a globally invertible map. QED.

Write

\[
N_m=\#\operatorname{Fix}(F^m)
=\sum_{\substack{p\ \mathrm{prime}\\K_p\mid m}}K_p.
\tag{6}
\]

This is finite: K_n<=m implies n<=2^{m+1}, with n=2 included separately
if necessary. Every fixed point in every component is counted. In
particular m=1 includes the distinct points for n=2 and n=3.

The full flow has lengths K_p and repetitions rK_p. Its ordinary product is

\[
Z(s)=\prod_p(1-e^{-sK_p})^{-1}
=\exp\left(\sum_{m\ge1}\frac{e^{-sm}N_m}{m}\right)
\quad(\Re s>\log2).
\tag{7}
\]

The second equality uses m=rK_p, including all K_p section points before
division by m. It is not a substitution of one point for a whole orbit.

## 4. Full graph kernels and distributional traces

### Proposition 2 — The flat traces exist for every positive iterate

All U_j^m have a well-defined diagonal restriction of their full
distributional kernels, and that restriction has compact support. Its
integral is

\[
\operatorname{tr}^{\flat}(U_j^m)
=\sum_{x\in\operatorname{Fix}(F^m)}
\frac{\operatorname{tr}(\Lambda^j(DF_x^m)^T)}
     {|\det(I-DF_x^m)|}.
\tag{8}
\]

**Proof.** A homeomorphism takes compact sets to compact sets in both
directions. Thus F^* preserves compact support, and its smooth pullback
coefficients give continuous operators on the spaces (2).

In component coordinates the kernel is

\[
K_{j,m}(x,y)
=\Lambda^j(DF_x^m)^T\,\delta(y-F^m x).
\tag{9}
\]

At a diagonal intersection x=F^m x, (4) shows I-DF_x^m invertible.
Consequently x-F^m x is a local coordinate system there. Applying the
ordinary change-of-variables rule to the delta distribution yields the
point mass with the absolute Jacobian denominator in (8). Off the
fixed set, the graph has no local diagonal intersection and contributes
zero. This is equivalently transversality of graph and diagonal.

Proposition 1 and (6) give a finite full fixed set. Hence the globally
defined restricted distribution is a finite sum of point masses with
matrix coefficients, and has compact support even though the original
kernel and M do not. It can be paired with the constant one: any compact
cutoff equal to one near that full finite support gives the same answer.
Taking the fibre trace yields (8). No periodic-point restriction was
made in (2) or (9). QED.

This is not a claim that one fixed compact cutoff works for all m.
The operation is defined globally for each m first; later convergence
will justify summing those exact traces.

### Proposition 3 — Scalar and form weights

Define B_m=lambda^m+lambda^{-m}-2>0 and T_j(m)=tr_flat(U_j^m). Then

\[
T_0(m)=T_2(m)=\frac{N_m}{B_m},\qquad
T_1(m)=\frac{(\lambda^m+\lambda^{-m})N_m}{B_m}
=N_m+2T_0(m).
\tag{10}
\]

Thus the natural graded flat trace is

\[
T_0(m)-T_1(m)+T_2(m)=-N_m.
\tag{11}
\]

**Proof.** At every fixed point,
det(I-J_m)=2-lambda^m-lambda^{-m}=-B_m, whereas (8) has the
absolute denominator B_m. The traces of the exterior powers of J_m^T
are respectively 1, lambda^m+lambda^{-m}, and 1. Substitute them in (8).
The negative sign in (11) is therefore intrinsic to this two-dimensional
hyperbolic return, not a chosen prime coefficient. QED.

## 5. Analytic trace exponentials and exact domains

### Proposition 4 — Exact absolute-convergence abscissae

With the definitions fixed in the card,

\[
D_j(s)=\exp\left(-\sum_{m\ge1}
\frac{e^{-sm}}mT_j(m)\right),
\tag{12}
\]

D_0=D_2 are holomorphic and nonzero on Re(s)>log(4/3).
Their defining logarithmic series have exact absolute-convergence
abscissa log(4/3). The corresponding abscissa for D_1 is log 2.

**Proof.** First verify the ordinary series (7). For n>=3 with K_n=l
there are 2^l integers, so

\[
\sum_p e^{-\sigma K_p}
\le e^{-\sigma}+\sum_{l\ge1}2^l e^{-\sigma l}<\infty
\quad(\sigma>\log2).
\tag{13}
\]

The repetition sum is at most this bound divided by 1-e^{-sigma}.
For the lower boundary, the sum of reciprocals of primes diverges:
otherwise the finite products prod_{p<=N}(1-1/p)^{-1} would be
uniformly bounded by exp(2 sum_p 1/p), but their positive geometric
expansions contain all terms of the divergent harmonic sum through N.
For p>2, 2^{K_p}<p, so at sigma=log2 the first repetition is
2^{-K_p}>1/p. This proves exact absolute abscissa log2 for (7).

Now

\[
\frac1{B_m}
=\frac{\lambda^{-m}}{(1-\lambda^{-m})^2},\qquad
\lambda^{-m}\le\frac1{B_m}\le9\lambda^{-m}.
\tag{14}
\]

The absolute logarithmic series of D_0 is therefore comparable term by
term to that of Z(s+log lambda). Its exact boundary is
log2-log lambda=log(4/3). The estimates are locally uniform in that
half-plane, proving holomorphy and nonvanishing of the exponential.
Since T_1=N_m+2T_0 and all coefficients are nonnegative, its series has
the exact abscissa log2. QED.

“Exact absolute-convergence abscissa” does not mean “natural boundary.”
No conditional boundary behavior or analytic continuation is proved.

### Proposition 5 — Derived scalar product and graded identity

On Re(s)>log(4/3),

\[
D_0(s)=D_2(s)
=\prod_{p}\prod_{\ell\ge1}
\left(1-e^{-(s+\ell\log\lambda)K_p}\right)^\ell.
\tag{15}
\]

On the common half-plane Re(s)>log2,

\[
\boxed{\frac{D_0(s)D_2(s)}{D_1(s)}=Z(s)}.
\tag{16}
\]

**Proof.** The elementary identity

\[
\frac1{B_m}=\sum_{\ell\ge1}\ell\lambda^{-\ell m}
\]

combined with m=rK_p in (12) gives

\[
\log D_0(s)
=-\sum_{p,r,\ell\ge1}\frac{\ell}{r}
e^{-(s+\ell\log\lambda)rK_p}.
\]

Absolute convergence follows from the preceding proposition, so summation
may be reordered and log(1-z) expanded, proving (15). In (16), either
use (11) in (12), or use T_1=N_m+2T_0 to obtain
D_1=D_0^2/Z on the common domain. The exponential conventions fix the
normalization; no unexplained constant is left over. QED.

Equation (16) is a natural return-operator form identity on the same
full geometric owner. It is not an identity with Riemann's zeta.

## 6. Controls, operator boundaries and adverse findings

| Control or distinction | Exact effect / boundary |
| --- | --- |
| Keep all components and momenta | Full periodic classification excludes rather than crops composite or noncentral returns |
| Keep all cyclic section points | N_m counts K_p points for every contributing prime packet; division by m gives 1/r |
| Scalar trace versus ordinary count | Scalar weight is 1/B_m, not one; the graded natural form action, not a manual replacement, gives (11) |
| Signed versus absolute determinant | The trace denominator is positive B_m, while the graded numerator is -B_m; omitting this sign would invert (16) |
| Delete witness tests, b=0 | The return support changes to all integers; any resulting trace formula belongs to that different comparator action |
| Source naturalness | The bounded-drift selector extends to finite nonnegative integer constraints with a positive witness gap; no privileged Riemann explanation follows |
| Macroclock | K_p=log(p)/log2+O(1), and K_5=K_7=2; neither exact log p nor a uniquely natural timing mechanism |
| Default area L2 | Scalar F* is unitary and any e^{-s} multiple is noncompact on this infinite-dimensional space |
| Differential-form spaces | Operators were defined on full compact-support smooth sections; no default L2 boundedness is asserted for the one-form pullback |
| Noncompact geometry | Each fixed iterate has finite restricted support; no compact Anosov or uniform resonance-continuation theorem is imported |

For the scalar L2 statement, symplectic area and invertibility preserve
norm. An infinite orthonormal sequence stays orthogonal with the same
nonzero norm after multiplication by e^{-s}. Thus the images have no
convergent subsequence, excluding compactness and trace class.
Consequently (12) is not the usual trace-class Fredholm determinant on
that Hilbert space.

The appropriate new fact is a legitimate flat trace and convergent trace
exponential of specified full operators. Constructing a Banach or Hilbert
realization with the needed Fredholm/spectral properties remains a
different, explicit obligation.

## 7. Gate assessment

| Gate | Evidence | Scoped status |
| --- | --- | --- |
| P0 | Full geometry, roof, operators, domains, kernel and normalizations specified | ESTABLISHED for this tuple |
| Operational A0 | Local integer witnesses determine the full prime-only return support, with controls | ESTABLISHED; exact/natural target clock not established |
| Owner A1 | All periodic states, one packet per prime, nondegenerate monodromy and repetitions | ESTABLISHED |
| Owner A2 flat trace | Actual full graph kernels, transverse diagonal pullback and finite restricted support | ESTABLISHED for every positive iterate |
| Owner A2 analytic identity | Exact trace-series domains and graded identity (16) | ESTABLISHED on the stated half-plane |
| Fredholm / spectral continuation | No qualifying analytic function-space realization supplied | OPEN; default scalar area-L2 proposal fails |
| Formal Route A | No target/divisor protocol evaluated | UNASSIGNED |
| Route B | No invocation, quantization or spectral target assessment | NOT INVOKED |

## 8. Decision and reproducibility

**Advance** the bounded same-object flat-trace and graded-zeta result.
Do not relabel it a Fredholm determinant or conceal the rounded clock.
Any new roof, analytic completion, damping or periodic-support restriction
requires a new frozen contract and its own ownership checks.

All candidate-specific statements are exact derivations above. No finite
orbit census, zero data, numerical precision parameter or prime table was
used. The one external source supplies standard terminology and a scope
comparison, not the proof of this candidate's trace or convergence.

See [card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence](evidence/README.md), [independent model review](evidence/review.md),
and [summary](README.md). Model review is not human peer review.
