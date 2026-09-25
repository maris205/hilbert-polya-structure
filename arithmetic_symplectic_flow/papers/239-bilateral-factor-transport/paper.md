# Bilateral factor transport: a complete arithmetic action with no nonzero periodic states

**Paper ID:** `239-bilateral-factor-transport`  
**Candidate ID:** `ANG-20260918-BFT01`  
**Date / status:** 2026-09-18; `GLOBAL OWNER; ALL NONZERO RETURNS ABSENT — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

We audit a nonconfining replacement of the preceding divisor-mode flows.
Every positive integer multiplication step and its division inverse act on
the full positive-rational coordinate space, with one summable all-integer
coefficient rule and no growing diagonal potential. The resulting bounded
generator owns a complete norm-preserving action on the entire ordinary
Hilbert sphere. It genuinely transfers amplitude across the old integer-power
supports. Nevertheless, an exact Fourier calculation proves that every
positive-time fixed space is zero. The proof separates the factor 2 in a
uniformly convergent character series: every conditional level equation has
at most two solutions on a circle, so every full level set has measure zero.
There are no nonzero stationary states or primitive periodic packets. Thus
this release of bound states also removes every desired prime return. The
same carrier and physical time are retained at the stop; no conclusion is
transferred to a unilateral integer model or to a different state topology.

## 1. Question, lineage and ownership

The [version-1 card](candidate-card.md) preceded the owner and return audit.
The question is whether replacing the confining interaction of
[237](../237-unary-divisor-coherence/paper.md) by reversible all-integer
factor transport avoids mixed-source bound packets while retaining actual
prime returns. The [238 scope](../238-nonconfining-source-frontier/candidate-card.md)
keeps this proposal separate from source-driven discrete scanning.

The precise [prior-work arrow](../../docs/prior_work/README.md) is the
proper-divisor symbolic incidence m -> am on integers, replaced by coherent
single-input transport, then extended to reversible division on all positive
rationals. This preserves a specified factor-incidence law, not a claimed
conjugacy with a chronological sieve, Logistic map or Henon map. The carrier
completion, uniform decay and norm shell are declared designs. Their
naturalness remains OPEN.

| Owner item | Exact BFT01 definition | Boundary |
| --- | --- | --- |
| State space | E=ell squared(G;C), G=positive rationals with discrete topology | Every rational coordinate retained, including 1 |
| Main carrier | M={z in E:norm(z)=1} | Full norm sphere, no spectral or prime projection |
| Arithmetic steps | V_a e_q=e_(aq), V_a* e_q=e_(q/a), every integer a>=2 | Negative prime valuations are allowed in the new carrier |
| Evolution | Phi_t=exp(-itB), equation (1) | Actual physical time t; no roof or diagonal potential |
| Packets | All nonconstant primitive point orbits modulo time translation | Global phase is not quotiented out |
| Repetition | r traversals of an actual primitive | No label-based replacement for rT |
| Classical geometry | No finite-dimensional symplectic base or suspension | Classical A0/A1/A2 NOT APPLICABLE |
| Later analysis | B is the classical amplitude generator | No trace, zeta, determinant or target quantum owner |

Compared with 237, the carrier, edge weights and diagonal are all changed.
This is a new object, not a perturbation theorem for the old one. The rational
scale quotient in [220](../220-finite-defect-cover-flow/README.md), finite
triangular fragmentation in [192](../192-six-architecture-source-frontier/README.md),
and indecomposable quotient in [193](../193-indecomposable-radial-quotient/README.md)
are different controls. No result or clock is transferred from them.

## 2. Exact inputs and complete evolution

For G=Q_(>0), put E=ell squared(G;C) and use the ordinary counting norm.
Multiplication by a permutes G, so V_a is unitary with the stated division
inverse. Define

\[
B=\sum_{a=2}^{\infty}a^{-2}(V_a+V_a^*),
\qquad \Phi_t=\exp(-itB). \tag{1}
\]

### Proposition 1 — Full bounded-generator owner

The series in (1) converges in operator norm to a bounded self-adjoint
operator on all E. The maps Phi_t form a norm-continuous unitary group;
every E-valued trajectory is a global strong solution of i dot z=Bz.
In particular the whole M is preserved.

**Proof.** Each summand has norm at most 2a^(-2), and
sum_(a>=2) a^(-2)<=1/4+integral_2^infinity x^(-2)dx=3/4. Thus the
partial sums converge in norm and norm(B)<=3/2. The finite sums are
self-adjoint and the adjoint is norm-continuous, so B*=B with domain E.
The exponential power series converges in norm for every real t. Its
termwise derivative, Cauchy product and adjoint give respectively the
equation, Phi_(t+s)=Phi_t Phi_s and Phi_t*=Phi_(-t). Hence Phi_t is
unitary and jointly continuous with its state variable. Uniqueness also
follows directly from the bounded linear ODE. No unbounded-domain or
finite-energy restriction is needed. QED.

Consequently objects z in M and arrows (z,t) from z to Phi_t z define
the full transformation groupoid. This establishes action-level T0. A
self-adjoint generator of this classical flow is not a quantization or
Route-B result.

The only arithmetic inputs to (1) are all integer multiplication/division
moves and the uniform rule a^(-2). There is no prime table, prime-specific
coefficient, von Mangoldt weight, inserted log-prime period or zero data.

## 3. A representation of the same full state space

Let Omega be the product of unit circles indexed by the ordinary primes,
with normalized product Haar measure mu. Every omega defines a character
chi_omega of G by unique factorization:

\[
q=\prod_p p^{v_p(q)},\qquad
\chi_\omega(q)=\prod_p\omega_p^{v_p(q)},\qquad v_p(q)\in\mathbb Z, \tag{2}
\]

where only finitely many exponents are nonzero. These coordinates are an
audit device for the already frozen rational group, not a prime-only
selection of physical states.

Define U e_q=chi_(.)(q). These functions form an orthonormal basis of
L2(Omega,mu): orthogonality follows by integrating each nonzero integer
exponent over its circle. Completeness follows because their span contains
every finite-coordinate trigonometric polynomial. Such polynomials are
dense in each finite product L2, and finite-coordinate functions are dense
in the countable product L2. The latter follows by approximating measurable
sets by the cylinder algebra that generates the product sigma-algebra.
Thus U extends to a unitary map from the full E onto full L2(Omega,mu).

The positive-rational character group is standard background in
Hedenmalm, Lindqvist and Seip, Introduction and Section 2.2
([primary text](https://arxiv.org/html/math/9512211)). Their integer-indexed
Hardy-space setting must not be confused with the full L2 space used here:
(2) retains negative as well as positive prime exponents. The basis argument
above specifies the exact full-state representation needed in this proof.

Since U V_a U^(-1) is multiplication by chi(a), norm convergence in (1)
gives multiplication by the real continuous function

\[
b(\omega)=\sum_{a\ge2}a^{-2}
   \bigl(\chi_\omega(a)+\overline{\chi_\omega(a)}\bigr).
\tag{3}
\]

The scalar series converges uniformly and absolutely. In particular the
same exponential power series yields

\[
U\Phi_t U^{-1}f=e^{-itb}f. \tag{4}
\]

No spectral theorem for a different operator, selected generalized state
or compressed Hardy space is used to obtain (4).

## 4. Every multiplier level set is null

### Lemma 2 — A one-circle exact discriminator

For every real lambda, mu({omega:b(omega)=lambda})=0.

**Proof.** Separate z=omega_2 and denote all other circle coordinates
by eta. Write r=1/4 and

\[
C(\eta)=\sum_{\substack{m\ge1\\m\ \text{odd}}}
          \frac{\chi_\eta(m)}{m^2},\qquad
D(z,\eta)=\sum_{n\ge1}\frac{\chi_{(z,\eta)}(n)}{n^2}.
\]

Every n has a unique expression n=2^k m with m odd. Absolute convergence
therefore gives

\[
D(z,\eta)=\frac{C(\eta)}{1-rz},
\qquad b(z,\eta)=2\operatorname{Re}\frac{C(\eta)}{1-rz}-2. \tag{5}
\]

The tail bound, uniformly for every eta, is

\[
|C(\eta)-1|
\le\sum_{\substack{m\ge3\\m\ \text{odd}}}m^{-2}
\le\sum_{m\ge3}m^{-2}
\le\frac19+\int_3^\infty x^{-2}\,dx
=\frac49<1. \tag{6}
\]

In particular C(eta) is never zero. No Euler product or arithmetic
nonvanishing conjecture is required.

Fix eta and a real lambda, and put s=(lambda+2)/2. On |z|=1, the level
equation in (5), after multiplication by |1-rz| squared, becomes

\[
\operatorname{Re} C-s(1+r^2)
+r\left(s-\frac{\bar C}{2}\right)z
+r\left(s-\frac{C}{2}\right)\bar z=0. \tag{7}
\]

This trigonometric polynomial is not identically zero. Otherwise its
z coefficient would give C=2s real, and its constant coefficient would
give s(1-r squared)=0, hence s=0 and C=0, contradicting (6).
Multiplying (7) by z gives a nonzero ordinary polynomial of degree at
most two. Thus the level has at most two points on this circle, and
has circle measure zero. Fubini on the product measure now gives the
asserted full level-set measure zero. QED.

The isolated factor 2 is used only to prove a property of the symmetric
all-integer construction (1). Its coefficient was not chosen separately,
and no prime-dependent modification of the dynamics is made.

## 5. Complete absence of point-periodic states

### Theorem 3 — All positive-time fixed spaces vanish

For every T>0, ker(Phi_T-I)={0} on E. B has no nonzero eigenvector at
any real eigenvalue. In particular there are no stationary or periodic
states on M and no nonconstant primitive packets.

**Proof.** If Phi_T z=z and f=Uz, equation (4) gives

\[
\bigl(e^{-iTb(\omega)}-1\bigr)f(\omega)=0
\quad\text{for almost every }\omega.
\]

Consequently f is supported, up to null sets, in

\[
\bigcup_{k\in\mathbb Z}
 \{\omega:b(\omega)=2\pi k/T\}. \tag{8}
\]

Each set in (8) is null by Lemma 2, and the union is countable. Hence
f=0 in L2 and z=0. Similarly Bz=lambda z forces f to be supported
on the single null level b=lambda, so f=0. Stationary states are
included by lambda=0 or by the positive-time assertion. QED.

The quantifier is every fixed T>0; there is no need to form an uncountable
union over candidate times. Any hypothetical periodic state would supply
one such T and contradict its zero fixed space. The zero vector is a
stationary state of the ambient E, but it is not in the frozen unit sphere.

This is a complete exact-return statement for BFT01, not merely absence
of one mixed packet. It does not prove decay, mixing, absence of approximate
returns, or a theorem about other transport weights or state topologies.

## 6. Controls and the cost of removing confinement

The transfer is genuinely cross-sector. At z(0)=e_6, the full equation
gives

\[
\dot z_2(0)=-i/9,\qquad \dot z_3(0)=-i/4. \tag{9}
\]

Only division by 3 or 2 respectively contributes to these coordinates.
Thus the old powers-of-6 support is not invariant. A pure prime mode also
excites rp by multiplication with coefficient r^(-2); taking r=2 when
p is odd and r=3 when p=2 shows that even the larger p^Z support is
not protected.

| Control | Exact observation | Scope |
| --- | --- | --- |
| Mixed-source support | Nonzero outside-sector derivatives (9) | A real support change, not prime-selective return |
| Pure prime initial data | Also transported across prime supports | Theorem 3 rules out their returns as well |
| Zero-generator flow | Every sphere state is stationary | Different owner; no primitive circles can be credited to BFT01 |
| Integer boundary | e_1 produces a 1/2-coordinate derivative -i/4; e_2 produces a 1-coordinate derivative -i/4 | Neither the n>=1 nor n>=2 integer subspace is invariant |
| Generalized character states | Point masses on Omega are not nonzero L2 states | Cannot replace the full norm carrier by distributional eigenstates |
| Finite truncation | No finite matrix or numerical diagonalization is used | Truncated eigenvectors do not refute or prove Theorem 3 |

The inverse coordinate completion is essential to this exact proof. A
unilateral integer shift with an adjoint boundary is a different candidate;
it cannot inherit the bilateral no-return result. Conversely, adding a
confining term or changing the state topology to recover eigenstates would
require a new card, not repair the present owner.

## 7. Gate assessment and decision

| Gate | Evidence for BFT01 | Result / limitation |
| --- | --- | --- |
| T0 | Proposition 1 and the full transformation groupoid | ESTABLISHED at action level |
| T1 | Explicit all-integer factor transport and actual time | Source/scale naturalness OPEN; no prime clock produced |
| T2 | Theorem 3, complete exact-return exclusion | Prime-return existence FAIL; no primitive/repetition ledger to advance |
| T3 | Generator and multiplier owned, but no periodic trace or zeta supplied | NOT ADVANCED |
| Classical A0/A1/A2 | No finite-dimensional symplectic suspension | NOT APPLICABLE |
| Formal Route / B | No formal evaluation | UNASSIGNED / NOT INVOKED |

**Decision: STOP / FORK.** This candidate avoids the previously exhibited
mixed bound packets by eliminating every nonzero return, including prime
returns. That is not a successful arithmetic selection mechanism. Retain
the full rational carrier, coefficient rule, physical time and empty point-
periodic ledger. No general impossibility claim about nonconfining arithmetic
dynamics follows. A future fork must supply an intrinsic source-selective
return mechanism as well as freedom from mixed-source bound packets.

## Reproducibility, source and disclosure

All exact inputs are in the [card](candidate-card.md); the [claim ledger](claim-ledger.md)
and [evidence record](evidence/README.md) distinguish proofs, background and
observed review. No numerical cutoff, precision parameter, dataset, GPU
run, fitted spectral value or publication artifact is involved.

Background reference: H. Hedenmalm, P. Lindqvist and K. Seip (1995 preprint;
journal reference 1997), *A Hilbert space of Dirichlet series and systems of
dilated functions in L2(0,1)*, Duke Mathematical Journal 86, 1--37.
[Author preprint and metadata](https://arxiv.org/abs/math/9512211);
[preprint DOI](https://doi.org/10.48550/arXiv.math/9512211).
Only the character-space background is used; no multiplier, Riesz-basis,
zeta or zero theorem from that paper is claimed for this candidate.

Data availability: all definitions, bounds and proofs are in this package.
Ethics: no human subjects or private data. AI assistance was used for
construction, drafting and bounded model checking. Human contribution roles,
funding and conflicts were not supplied and are not invented. ARS informed
the frozen contract, adverse controls and evidence separation; no venue
criteria are bound (`criteria_binding_unavailable`). This internal record
is not external peer review, a novelty certification or publication readiness.
