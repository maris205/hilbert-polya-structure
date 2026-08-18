# Object, marker, operator, and determinant contract

## Typed objects

| Symbol | Type | Owner | Forbidden identification |
|---|---|---|---|
| \(h\) | integer parameter, \(h\ge2\) | theorem family | a fitted cutoff |
| \(s\) | complex Dirichlet parameter | operator weight | determinant variable |
| \(\sigma\) | real part \(\Re s\) | singular and ideal laws | the full complex parameter |
| \(\mathcal F_h\) | \(h\)-free positive integers | block index set | rational primes alone |
| \(\tau_h\) | saturated exponent retraction | \(S_{h,s}\) | exponent reduction modulo \(h\) |
| \(\omega_h\) | exponent-modulo-\(h\) retraction | \(M_{h,s}\) | exponent saturation |
| \(m\) | \(h\)-free block label | direct-sum ledger | primitive prime atom |
| \(J_h(m)\) | saturated-prime set of \(m\) | saturated fiber | all prime divisors of \(m\) |
| \(\lambda_m\) | operator eigenvalue \(m^{-s/2}\) | cyclic ledger | singular value |
| \(\rho_T(m)\) | unique nonzero block singular value | metric ledger | eigenvalue |
| \(P_T(m)\) | Riesz-idempotent norm | similarity ledger | probability |
| \(w_{h,\sigma}(m)\) | generalized positive weight | saturated Weyl count | an integer without proof |
| \(z\) | determinant variable | Fredholm ledger | time marker or \(s\) |
| \([T^*,T]\) | \(T^*T-TT^*\) | nonnormality ledger | the operator \(T\) itself |

## Algebraic versus bounded operator

For \(T=S_{h,s}\) or \(M_{h,s}\), the basis formula first defines a linear
map on \(c_{00}(\mathbb N)\). The symbol \(T\in\mathcal B(\ell^2)\) is used
only after every fiber coefficient vector is in \(\ell^2\) and the
supremum of its norm is finite.

The exact extension table is

| Operator | Bounded extension | Compactness |
|---|---|---|
| \(S_{h,s}\) | exactly \(\sigma>0\) | throughout the same domain |
| \(M_{h,s}\) | exactly \(\sigma>1/h\) | throughout the same domain |

At a failed boundary, a formal basis prescription is not a bounded operator
and cannot own a power, trace, determinant, Riesz projection, or
self-commutator on \(\ell^2\).

Writing \(s=\sigma+it\) and

\[
U_t e_n=n^{-it/2}e_n
\]

gives \(T_{h,s}=T_{h,\sigma}U_t\). Thus singular values and ideal membership
depend only on \(\sigma\), whereas eigenvalues and traces retain the full
complex phase.

## Fiber contract

For \(m\in\mathcal F_h\),

\[
J_h(m)=\{p:v_p(m)=h-1\}.
\]

The fiber equalities are exact:

\[
\tau_h^{-1}(m)
=\left\{m\prod_{p\in J_h(m)}p^{r_p}:r_p\ge0\right\},
\]

\[
\omega_h^{-1}(m)=\{ma^h:a\ge1\}.
\]

No prime outside \(m\) may enter a saturated fiber, while every prime may
enter a modulo fiber only through an exponent divisible by \(h\).

Let

\[
\mathcal H^S_m
=\overline{\operatorname{span}}\{e_n:\tau_h(n)=m\},\qquad
\mathcal H^M_m
=\overline{\operatorname{span}}\{e_n:\omega_h(n)=m\}.
\]

The respective spaces form orthogonal partitions of \(\ell^2(\mathbb N)\).
On either block,

\[
T_m x=\left(\sum_{f(n)=m}x_n n^{-s/2}\right)e_m
\]

up to the fixed inner-product conjugation convention. It is rank one when
bounded, fixes the eigenline \(\mathbb Ce_m\), and has

\[
T_m^k=\lambda_m^{k-1}T_m,\qquad \lambda_m=m^{-s/2}.
\]

## Singular and ideal contract

\[
\rho_S(m)^2
=m^{-\sigma}\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1},
\]

\[
\rho_M(m)^2=m^{-\sigma}\zeta(h\sigma).
\]

For \(k\ge1\) and \(0<q<\infty\),

\[
S_{h,s}^k\in\mathcal S_q\iff k\sigma q>2,
\]

\[
M_{h,s}^k\in\mathcal S_q
\iff \sigma>1/h\text{ and }k\sigma q>2.
\]

The equality lines \(k\sigma q=2\) fail. The second statement never drops
the bounded-existence condition even if the formal \(k\)th-power sum would
converge.

## Eigenvalue, trace, and determinant contract

On each operator's bounded domain the simple nonzero eigenvalue multiset is

\[
\{\lambda_m=m^{-s/2}:m\in\mathcal F_h\}.
\]

The eigenvalue moduli are strictly ordered by \(m\), so there is no
cross-block multiplicity ambiguity. Zero belongs to the compact spectrum
and carries the remaining kernel structure; it contributes no Fredholm
factor.

For a positive integer \(k\), the common trace identity is asserted only
under

\[
\sigma>1/h,\qquad k\sigma>2,
\]

and then

\[
\operatorname{Tr}(S_{h,s}^k)
=\operatorname{Tr}(M_{h,s}^k)
=\sum_{m\in\mathcal F_h}m^{-ks/2}
=\frac{\zeta(ks/2)}{\zeta(hks/2)}.
\]

For every integer \(r\ge1\), if

\[
\sigma>1/h,\qquad r\sigma>2,
\]

both operators lie in \(\mathcal S_r\), and their regularized determinants
are the same entire function of \(z\):

\[
\det_r(I-zT)
=\prod_{m\in\mathcal F_h}
\left[
(1-z\lambda_m)
\exp\left(\sum_{j=1}^{r-1}\frac{(z\lambda_m)^j}{j}\right)
\right].
\]

For \(r=1\) the exponential is empty and this is the ordinary Fredholm
determinant; its common domain requires \(\sigma>2\). Determinant equality
is a negative control for geometric identifiability, not a new generic
determinant mechanism.

## Riesz and similarity contract

The nonzero spectral idempotent on block \(m\) is

\[
\Pi_{T,m}=\lambda_m^{-1}T_m.
\]

Its norm is

\[
\|\Pi_{S,m}\|
=\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1/2},
\qquad
\|\Pi_{M,m}\|=\sqrt{\zeta(h\sigma)}.
\]

The phrase boundedly similar to normal means that a single bounded
invertible operator on the full \(\ell^2\) conjugates \(T\) to a compact
normal diagonal operator. It is not enough to diagonalize each finite block
with condition numbers depending on \(m\).

The exact iff statements are

\[
S_{h,s}\sim_{\mathrm{bd}}\text{ compact normal}
\iff \sigma>1,
\]

\[
M_{h,s}\sim_{\mathrm{bd}}\text{ compact normal}
\iff \sigma>1/h.
\]

At \(\sigma=1\), \(S\) fails and \(M\) passes.

## Weyl counting contract

For \(S\),

\[
w_{h,\sigma}(m)
=m\prod_{p\in J_h(m)}(1-p^{-\sigma})^{1/\sigma},
\qquad
\rho_S(m)=w_{h,\sigma}(m)^{-\sigma/2}.
\]

The positive counting function and its consequence are

\[
A_S(x)=\#\{m\in\mathcal F_h:w_{h,\sigma}(m)\le x\}
\sim C_{h,\sigma}x,
\]

\[
s_n(S_{h,s})\sim
\left(\frac{C_{h,\sigma}}n\right)^{\sigma/2}.
\]

For \(M\),

\[
s_n(M_{h,s})\sim
\left(\frac{D_{h,\sigma}}n\right)^{\sigma/2},
\qquad
D_{h,\sigma}=\frac{\zeta(h\sigma)^{1/\sigma}}{\zeta(h)}.
\]

For the common eigenvalues,

\[
|\lambda_n|\sim
\left(\frac{1/\zeta(h)}n\right)^{\sigma/2}.
\]

The exact crossover is

\[
C_{h,1}=D_{h,1}=1.
\]

There is no frozen sign or ordering for \(C_{h,\sigma}-D_{h,\sigma}\) away
from one.

## Self-commutator contract

For a rank-one block with singular norm \(\rho\) and eigenvalue modulus
\(a\), the two possibly zero singular values of \(T^*T-TT^*\) are

\[
c=\rho^2\sqrt{1-a^2/\rho^2}.
\]

Accordingly,

\[
[S_{h,s}^*,S_{h,s}]\in\mathcal S_q\iff\sigma q>1,
\]

\[
[M_{h,s}^*,M_{h,s}]\in\mathcal S_q
\iff\sigma>1/h\text{ and }\sigma q>1.
\]

At \(h=2\), necessity must vary a second saturated prime after fixing one;
the \(h\ge3\) varying exponent-one witness is not well typed.

## Firewall verdicts

| Proposed move | Verdict | Reason |
|---|---|---|
| replace \(\tau_h\) by \(\omega_h\) in one fiber formula | SOURCE_TYPE_ERROR | the preimages and existence walls differ |
| call \(\rho_T(m)\) an eigenvalue | SPECTRAL_TYPE_ERROR | singular and cyclic ledgers are distinct |
| use \(k\sigma q>2\) without \(\sigma>1/h\) for \(M^k\) | EXISTENCE_ERROR | an unbounded basis prescription owns no bounded power |
| trace at \(k\sigma=2\) | ENDPOINT_ERROR | the \(h\)-free Dirichlet sum diverges |
| claim \(C_{h,\sigma}\ne D_{h,\sigma}\) universally | CROSSOVER_ERROR | both equal one at \(\sigma=1\) |
| infer similarity from equal eigenvalues or determinants | GEOMETRY_ERROR | saturated Riesz projections are not uniformly bounded for \(\sigma\le1\) |
| count free-UFD replication as prime emergence | FIREWALL_ERROR | it proves atom-label indistinguishability |
| call the regularized determinant a Hilbert--Polya determinant | OWNERSHIP_ERROR | no completed target divisor or self-adjoint owner is defined |
| share expected values between evaluators | INDEPENDENCE_ERROR | agreement would not be an independent reproduction |

## Claim boundary

The contract governs only the frozen all-\(h\) pair on
\(\ell^2(\mathbb N)\). It does not assert a theorem for arbitrary weighted
composition, arbitrary multiplicative maps, other coefficient weights, a
changed base measure, or a completed arithmetic spectral model.
