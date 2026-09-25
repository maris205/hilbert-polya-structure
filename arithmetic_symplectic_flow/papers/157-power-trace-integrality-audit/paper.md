# A power-trace multiplicity obstruction for the saturated-sieve map

**Paper ID:** 157-power-trace-integrality-audit  
**Candidate ID:** ASFS-20260915-PTI01  
**Date:** 2026-09-15  
**Status:** STOP — EXACT FULL FLAT-TRACE SEQUENCES HAVE NO HILBERT TRACE-CLASS POWER REALIZATION.  
**Route:** Limited owner-level analytic audit; formal coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The complete scalar flat traces of the saturated-sieve symplectic map
cannot be the ordinary traces of all positive powers of any single
Hilbert trace-class operator. The obstruction is independent of the
choice of Hilbert space and does not require normality or positivity.
Exact dyadic packet counts and the prime number theorem give a leading
normalized coefficient 1/log 2. For trace-class power traces, a finite
strictly positive normalized limit must instead be the positive integer
algebraic multiplicity of the leading positive real eigenvalue.
The same contradiction applies separately to the natural one-form and
two-form trace sequences. It preserves the previously proved full-map
distributional flat traces and their convergent graded zeta identity.
It does not rule out non-trace-class, regularized, local, or more general
meromorphic operator frameworks. The rounded unit-roof clock is unchanged.

## 1. Frozen object and exact question

The [version-1 card](candidate-card.md) was written before this audit.
This is a fresh analytic contract over explicitly specified geometry,
not a new map and not a revision of 153's frozen owner.

For every integer n>=2 and phase 1<=k<=K_n set
\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
b(n,k)=\sum_{\substack{2^k\le d<2^{k+1}\\d<n}}1_{\{d\mid n\}},
\]
\[
f_{n,k}(q)=q+\tfrac12\tanh q+K_n b(n,k).
\]
With k^+ the cyclic successor, the full symplectic map is
\[
M=\coprod_{n\ge2,\ 1\le k\le K_n}\mathbb R^2,\quad
\omega=dq\wedge dp,\quad
F(n,k,q,p)=(n,k^+,f_{n,k}(q),p/f'_{n,k}(q)).
\tag{1}
\]
Its roof is tau=1 and its suspension is the endpoint-glued
(M times [0,1])/((x,1)~(Fx,0)), with translation flow. No component,
momentum, phase, or noncentral point is removed. The base is symplectic;
the three-dimensional suspension is not thereby a symplectic manifold.

| Owner | Definition and audit scope |
| --- | --- |
| Arithmetic/symbolic lineage | Local proper-divisor exclusion, deformed to bounded-drift witness dynamics and its exact cotangent lift |
| Complete geometric owner | Formula (1), all integer and real states, unit roof |
| Existing analytic owner | U_j=F* on C_c^infinity(M;Lambda^j T*M), j=0,1,2, with canonical componentwise area kernels |
| Clock weighting | U_{j,s}=e^{-s}U_j, with m-th return weight e^{-sm} |
| Flat-trace target | Exact full graph-diagonal traces T_j(m) in (2) below, all m>=1 |
| Proposed new realization | Any complex Hilbert H and trace-class A with tr(A^m)=T_0(m) for every m>=1 |
| Optional form questions | The same existential question separately for T_1 and T_2 |
| Determinant normalization | d_j(z)=exp(-sum_{m>=1}T_j(m)z^m/m), z=e^{-s}; only ordinary det(I-zA) is tested |
| Future geometric/quantum owner | NOT SUPPLIED |

The existing full-map flat-trace construction is documented and reviewed
in [153](../153-saturated-sieve-flat-trace/paper.md). Its strongest
analytic result and remaining limitations are also distinguished in
[156](../156-multi-round-source-trace-frontier/paper.md).
This paper checks its precise numerical sequence before imposing the
new, stronger ordinary trace-class requirement.

An abstract realization would still need a geometric ownership argument.
Its nonexistence is therefore a necessary-condition obstruction to any
completion having these exact ordinary traces, not a claim that abstract
matrix realization alone would have met the research programme.

## 2. Rechecking the complete return-count input

Each f has derivative 1+(1/2)sech^2(q)>1 and differs from q by a bounded
function and a constant. It is an onto diffeomorphism. Its cotangent lift
preserves p dq, and (1) is globally invertible and symplectic. The unit
roof gives a complete suspension.

A cycle of length m must have m=rK_n. Let
a(n)=sum_k b(n,k), the number of proper divisors of n other than one.
Summing all configuration increments on the cycle gives
\[
0=\tfrac12\sum_{t=0}^{m-1}\tanh q_t+K_nr\,a(n).
\]
For composite n, a(n)>=1 and the right side is strictly positive.
For prime n the witnesses vanish; every nonzero q moves strictly away
from zero, so a return requires q=0. Momentum then scales by 2/3 at each
step, forcing p=0. Thus there is exactly one full primitive K_p-cycle
per prime and no other periodic state. At its points,
DF^m=diag(lambda^m,lambda^{-m}), lambda=3/2.

The resulting exact targets are
\[
N_m=\sum_{p:\,K_p\mid m}K_p,\qquad
B_m=\lambda^m+\lambda^{-m}-2,\qquad
T_0(m)=T_2(m)=\frac{N_m}{B_m},\quad
T_1(m)=N_m+2T_0(m).
\tag{2}
\]
All these counts are finite since K_n<=m implies n<=2^{m+1}.
Every contributing packet retains its K_p section points.
For scalar and natural form pullbacks, the graph-diagonal denominator
is the absolute determinant B_m, with exterior-power numerator
1, lambda^m+lambda^{-m}, or 1. This verifies (2) with the same complete
owner; the full distributional construction itself remains 153's result.

The lineage is a conservative deformation of prime/composite symbolic
admissibility, as required by the
[prior-work guide](../../docs/prior_work/README.md).
The integer n is conserved: this is not one chronological sieve orbit.
Neither prime tables nor the prime number theorem enters (1). PNT is
used below to analyse the resulting full packet distribution.

## 3. Dyadic endpoints and the exact leading coefficient

### Proposition 1 — Full return-count asymptotic

For the complete sequence in (2),
\[
\lim_{m\to\infty}\frac{N_m}{2^m}=\frac1{\log 2}.
\tag{3}
\]

**Proof.** Write c_k=#{p:K_p=k}. The exceptional prime p=2 and the
prime p=3 both have K_p=1, so c_1=2. For k>=2,
\[
K_p=k\ \Longleftrightarrow\ 2^k<p\le2^{k+1},\qquad
c_k=\pi(2^{k+1})-\pi(2^k).
\tag{4}
\]
Indeed floor(log_2(p-1))=k means
2^k<=p-1<2^{k+1}; the upper integer endpoint is p<=2^{k+1}.
The dyadic endpoints are composite for k>=2. No shift of an endpoint
by one, and no omission of the empty n=2 witness block, is hidden here.

The prime number theorem states
pi(x)=x/log x+o(x/log x); we use this standard theorem in exactly that
form. See the author's
[De Angelis statement of PNT](https://vdeangel.xula.edu/Notes/PNT.html),
under “Statement of the Prime Number Theorem.” Substitution at the two
dyadic endpoints of (4) yields
\[
\frac{m c_m}{2^m}
=\frac1{\log 2}\left(\frac{2m}{m+1}-1\right)+o(1)
\longrightarrow\frac1{\log 2}.
\tag{5}
\]
This subtraction is legitimate: each separate PNT error, after
m/2^m scaling, is o(1). No estimate on primes in shrinking intervals
is required; the interval has fixed endpoint ratio two.

Since N_m=sum_{d|m} d c_d, its proper-divisor remainder is
\[
R_m=N_m-mc_m
=\sum_{\substack{d\mid m\\d<m}}d c_d.
\]
Every proper divisor d is at most m/2, and c_d<=2^d for all d>=1,
including c_1=2. For m>=2 and h=floor(m/2),
\[
0\le R_m\le\sum_{d=1}^h d\,2^d
\le h\sum_{d=1}^h2^d
\le m\,2^h.
\tag{6}
\]
Therefore R_m/2^m<=m 2^{-m/2}->0. Combining (5) and (6) proves (3)
along all positive integers m, not just a prime or special subsequence.
QED.

### Corollary 2 — The three normalized trace limits

For R_0=R_2=4/3 and R_1=2,
\[
\lim_{m\to\infty}\frac{T_j(m)}{R_j^m}
=C,\qquad C=\frac1{\log 2},\qquad j=0,1,2.
\tag{7}
\]

**Proof.** Since B_m=lambda^m(1-lambda^{-m})^2,
\[
\frac{T_0(m)}{(4/3)^m}
=\frac{N_m}{2^m}(1-(2/3)^m)^{-2}\longrightarrow C.
\]
The two-form equality is exact. Also
T_1(m)/2^m=N_m/2^m+2T_0(m)/2^m, and the second term tends to zero.
Finally, 1/2<integral_1^2(dt/t)=log 2<1, so
\[
1<C<2.
\tag{8}
\]
In particular C is not an integer; no transcendence result or decimal
approximation is required. QED.

## 4. Integral multiplicity for trace-class power traces

We use the trace-class ideal property and Lidskii's formula.
[Dai, Section 3.1, pp. 36–37, Theorem 3.1.2](https://web.math.ucsb.edu/~dai/book.pdf)
states the ideal property and trace formula.
[Kostenko's author lecture notes](https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf)
give the nonnormal compact-spectrum statement in Theorem 2.3.1 (p. 12),
algebraic-multiplicity conventions on p. 36, absolute eigenvalue
summability through (3.4.14) at p=1 (p. 37), and the determinant product
and Lidskii formula in Theorem 3.4.7 (p. 41). These facts do not require
normality or positivity. The finite-phase argument below is proved here.

For completeness, the ideal property makes every A^m trace class.
Nonzero polynomial spectral mapping follows by factoring
A^m-nu I into the commuting factors A-mu I over the m-th roots of
nu!=0. On the finite-dimensional generalized eigenspaces, the Jordan
form shows that raising A to the m-th power replaces mu by mu^m and
preserves the sum of algebraic multiplicities when values coincide.
Thus Lidskii applied to A^m yields
tr(A^m)=sum_i mu_i(A)^m. The sum is absolutely convergent because
sum_i |mu_i(A)| is finite and the eigenvalues are bounded.

### Lemma 3 — A convergent finite phase sum

Let omega_1,...,omega_q be distinct unit complex numbers and
a_1,...,a_q complex coefficients. If sum_l a_l omega_l^m -> L as
m->infinity, then every coefficient at omega_l!=1 is zero and the
coefficient at omega_l=1 is L, taking that coefficient to be zero
when one is absent.

**Proof.** For any fixed unit omega,
the Cesàro mean of (eta/omega)^m is one when eta=omega and tends to
zero otherwise. Multiply the assumed sequence by omega^{-m} and take
Cesàro means. The o(1) error still has mean tending to zero, while
L omega^{-m} averages to zero unless omega=1. This extracts precisely
the indicated coefficient. QED.

### Proposition 4 — Leading positive power-trace limits are integral

Let A be trace class on a complex Hilbert space, let R>0, and suppose
\[
\frac{\operatorname{tr}(A^m)}{R^m}\longrightarrow L
\quad\hbox{with }0<L<\infty.
\tag{9}
\]
Then L is a positive integer: specifically the algebraic multiplicity
of the eigenvalue R. No other eigenvalue has modulus R, and no
eigenvalue has greater modulus.

**Proof.** Put B=A/R and list its nonzero eigenvalues mu_i with
algebraic multiplicity. Lidskii applied to each B^m gives
tr(B^m)=sum_i mu_i^m, with sum_i |mu_i|<infinity.
If there are no nonzero eigenvalues then every trace is zero,
contradicting (9).

The largest modulus rho=max_i |mu_i| is attained. The set of
eigenvalues of modulus rho is finite, each with a positive integer
algebraic multiplicity. All remaining moduli are bounded by some
r<rho: absolute summability permits only finitely many moduli
above rho/2, and hence a strict gap below the largest modulus.
If no eigenvalues remain, the remainder below is zero.
For the remaining indices,
\[
\left|\sum_{|\mu_i|<\rho}\mu_i^m\right|
\le r^{m-1}\sum_{|\mu_i|<\rho}|\mu_i|.
\tag{10}
\]

If rho<1, the same estimate with rho for the full list shows
tr(B^m)->0, contradicting (9).
If rho>1, tr(B^m)/rho^m->0. By (10), its difference from the finite
peripheral sum
P_m=sum_{|\mu|=rho} a_mu (mu/rho)^m tends to zero.
Thus P_m->0. Lemma 3 would force every positive integer a_mu to be
zero, a contradiction.

Consequently rho=1. The remainder in (10) tends to zero, and the
peripheral sum tends to L. Lemma 3 eliminates every phase except
mu=1 and identifies L with its positive integer multiplicity.
Rescaling B to A gives the assertion. Jordan blocks do not change
the argument: power traces count algebraic multiplicities, not
polynomial-in-m off-diagonal terms. QED.

For a possibly nonseparable Hilbert space, the same proof applies on the
separable reducing subspace generated by the closures of the ranges of
A and A*. Compactness makes these ranges separable, and A is zero on
the orthogonal complement. Thus enlarging the Hilbert space does not
avoid the argument.

## 5. No ordinary trace-class realization of the frozen targets

### Theorem 5 — Exact Hilbert trace-class realization is impossible

For each j in {0,1,2}, there is no complex Hilbert space H_j and
trace-class operator A_j on H_j satisfying
\[
\operatorname{tr}(A_j^m)=T_j(m)
\qquad\hbox{for every integer }m\ge1.
\tag{11}
\]

**Proof.** Corollary 2 supplies (9), with R=R_j and
L=1/log 2 in the open interval (1,2). Proposition 4 requires this
same L to be an integer. Contradiction. QED.

This is stronger than noncompactness on the default symplectic-area
L2 space: it excludes the exact target sequences on every Hilbert
trace-class realization, even one not yet tied to geometry.
It is narrower than a prohibition of all operator realizations.

### Corollary 6 — The ordinary Fredholm determinant germ is excluded

For each j, the germ
\[
d_j(z)=\exp\left(-\sum_{m\ge1}\frac{T_j(m)}m z^m\right)
\tag{12}
\]
does not equal det(I-zA) near z=0 for any fixed Hilbert trace-class A.

**Proof.** For trace class, the ordinary determinant has the absolutely
convergent eigenvalue product prod_i(1-z mu_i), by the cited
Kostenko Theorem 3.4.7 with z replaced by -z. Near zero, expansion
of log(1-z mu_i) and absolute summability give
log det(I-zA)=-sum_m tr(A^m)z^m/m.
Both sides of a proposed equality have value one at zero and thus the
same normalized logarithm there. Coefficient comparison would give
(11), contradicting Theorem 5. QED.

No assertion is made about a parameter-dependent family A(z) unrelated
to powers of one fixed return operator. Nor is this a claim that
I-zU is a non-Fredholm operator: Fredholmness of an operator and the
existence of an ordinary trace-class determinant are different matters.

## 6. Adversarial controls and limits

| Control | Exact finding and its role |
| --- | --- |
| Exceptional n=2 and small iterates | c_1=2, c_2=2, c_3=2; N_1=2, N_2=6, N_3=8. Thus T_0(1)=12, T_0(2)=216/25, T_0(3)=1728/361. These are arithmetic checks, not evidence for the infinite limit. |
| Full proper-divisor contribution | Estimate (6) includes every earlier period dividing m. Ignoring it without a bound would leave a gap in (3). |
| Integral coefficient positive control | On C^h, A=R I_h has tr(A^m)/R^m=h for any positive integer h. Proposition 4 allows these examples. |
| Complex peripheral cancellation | A=diag(R,-R) gives normalized traces 1+(-1)^m. Its oscillation shows why a limsup or subsequence cannot replace the full limit in (9). |
| Nonnormal blocks | A size-h Jordan block at R has trace hR^m. Off-diagonal growth does not create a fractional limiting multiplicity. |
| Uniform nonzero damping | If a trace-class B realized c^m T_j(m), c!=0, then B/c would realize T_j(m). A uniform scalar clock weight cannot remove this exact obstruction. This is an implication, not a changed candidate. |
| Finite packet cutoff | The explicit trace-class construction below realizes every finite packet cutoff, showing that finite models do not contradict the full obstruction. |
| Scope / PROVES_TOO_MUCH | The theorem uses this full sequence's nonintegral leading coefficient. It does not say all prime-linked dynamics or all flat-trace sequences lack operator realizations. |

For the finite-cutoff control, let S be any finite set of the actual
prime packets, and let P_K be the unitary cyclic permutation on C^K.
On the Hilbert direct sum of finite-dimensional blocks define
\[
A_S=\bigoplus_{p\in S}\ \bigoplus_{\ell\ge1}
\ \bigoplus_{a=1}^{\ell}\lambda^{-\ell}P_{K_p}.
\tag{13}
\]
Its trace norm is
(sum_{p in S}K_p)sum_{ell>=1}ell lambda^{-ell}<infinity.
Since tr(P_K^m)=K when K divides m and zero otherwise,
\[
\operatorname{tr}(A_S^m)
=\frac{\sum_{p\in S:\,K_p\mid m}K_p}{B_m}.
\tag{14}
\]
Thus finite packet cutoffs have exact ordinary trace-class models.
They are controls only: (13) is not the full geometric pullback and
does not authorize replacing its carrier by finitely many packets.
If S includes every packet with K_p<=M, (14) even matches the complete
target for every m<=M. Arbitrarily long finite-prefix agreement
therefore cannot prove the requested all-powers realization.

The full noncompact geometry and its local graph-diagonal flat traces
remain valid. The earlier graded identity D_0 D_2/D_1=Z on
Re(s)>log 2 remains a flat-trace identity. The present result does not
establish a natural boundary, exclude all meromorphic continuations,
or classify regularized determinants or non-trace-class spaces.
No compact Anosov theorem is invoked. The periods are still K_p,
not exact log p, and no target-zero or quantum comparison is performed.

## 7. Gate assessment and decision

| Gate or obligation | Evidence | Scoped status |
| --- | --- | --- |
| Frozen analytic identity | Complete (1), unit roof, full targets (2), exact question (11) | ESTABLISHED |
| Source and orbit input | Full-state recurrence check in Section 2 | Retained, not a new A0/A1 promotion |
| Leading coefficient | Dyadic endpoint count, PNT and proper-divisor estimate | THEOREM |
| Ordinary Hilbert trace-class powers | Theorem 5 excludes every H and A with the exact all-m target | SCOPED NEGATIVE |
| Fixed-operator ordinary determinant | Corollary 6 | SCOPED NEGATIVE |
| Distributional flat trace and graded identity | Different established claim, unchanged | RETAINED |
| Other spectral or regularized framework | Not investigated by this contract | OPEN / OUT OF SCOPE |
| Formal Route A | No target/divisor evaluation | UNASSIGNED |
| Route B | No formal invocation | NOT INVOKED |

**Stop** the exact ordinary Hilbert trace-class realization contract.
Do not continue searching for a clever Hilbert norm with the same
required ordinary power traces: Theorem 5 is independent of that norm.
**Advance** only the reusable obstruction and retain 153's bounded
flat-trace result. A genuinely different analytic requirement or
clock/carrier mechanism needs a new frozen contract; no such new
candidate is created here.

## Reproducibility and research integrity

All candidate-specific results are exact proofs above. No orbit search,
floating-point experiment, numerical prime table or external-model API
was used. PNT and the trace-class spectral facts are external theorem
inputs, not numerically tested conjectures or new proofs here.
No literature-wide novelty claim is made.

This is a Markdown research note, not a publication submission.
There are no human-subject data; no new funding, conflict-of-interest,
or human-authorship claims are made. Model-assisted argumentation and
source checking are disclosed; model review is not human peer review.
ARS was used only for the claim/evidence/counterargument discipline.

See the [card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence record](evidence/README.md), and [summary](README.md).
