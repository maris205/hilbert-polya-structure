# Research Protocol — Natural Koopman Lift of `FF-FROB-SUSP-P1-F2`

Protocol date: 2026-08-13  
Stage: 5, fixed quantum/operator candidate  
Scope: source lock and theorem audit only; no manuscript, numerical fit, or new
operator design

## 1. Decision first

The frozen Frobenius suspension has a canonical same-clock unitary lift: the
Koopman translation group on the \(L^2\)-space of its circle components. Its
Stone generator is completely definable and self-adjoint. It nevertheless
fails the spectral-host gate in the strongest possible way:

\[
 \sigma_{\mathrm p}(A_K)=\frac{2\pi}{\log 2}\mathbb Q,
 \qquad
 \sigma(A_K)=\sigma_{\mathrm{ess}}(A_K)=\mathbb R,
\]

and every point eigenvalue has countably infinite multiplicity. The resolvent
is not compact, every interval of positive width has infinite spectral
projection rank, and
\(e^{-tA_K^2}\) is not trace class for any \(t>0\). These conclusions hold for
every positive finite choice of component weights because all such Koopman
representations are unitarily equivalent.

Thus the natural lift earns `A4_UNITARY_OR_SCATTERING_CANDIDATE` and the
limited early audit proves `B1_COMPLETE_OPERATOR_DEFINITION` plus
`B2_SELF_ADJOINT`, but it also proves `B3_FAIL`. It is not a physical
quantization, not Route-B ready, and its self-adjoint generator does not have
the Hasse--Weil orbit zeta as a spectral determinant.

## 2. Fixed question and prohibited moves

Starting from Paper 4's unchanged classical object
`FF-FROB-SUSP-P1-F2`, what is its most direct unitary operator, and what is the
exact spectral type of that operator?

This phase does **not** ask whether some coupled, perturbed, compressed, or
regularized operator could be invented with a more favorable spectrum. Any
component coupling, potential, boundary change, degree cutoff, or subtraction
defines a new candidate and requires a new source lock.

Forbidden evidence and construction moves:

- no Riemann-zero list or rational-prime table;
- no spectral, scale, or phase fitting;
- no replacement of the constant roof by componentwise hand-set lengths;
- no transfer of a cohomological Frobenius determinant to the Koopman
  generator without a same-operator trace theorem;
- no finite cutoff promoted to the infinite arithmetic object;
- no use of “quantization” merely because Stone's generator is self-adjoint.

## 3. Inherited classical object

Let

\[
 S=\mathbb P^1(\overline{\mathbb F}_2)
\]

with the discrete topology, let \(F(a)=a^2\), and put \(\tau=\log 2\). Paper 4
freezes

\[
 M_F=(S\times\mathbb R)/\mathbb Z,\qquad
 n\cdot(a,u)=(F^n a,u-n\tau),\qquad
 \phi^t[a,u]=[a,u+t].
\]

Its proved component theorem is

\[
 M_F\cong\coprod_{x\in|\mathbb P^1_{\mathbb F_2}|} C_x,\qquad
 C_x=\mathbb R/(L_x\mathbb Z),\qquad
 L_x=d_x\tau,\quad d_x=\deg x.
\]

The homeomorphism preserves vertical time. No classical coordinate, clock,
topology, orbit multiplicity, or zeta convention is changed in this phase.

## 4. Closed points occur in every degree

Let \(a_d\) be the number of closed points of degree \(d\) on
\(\mathbb P^1_{\mathbb F_2}\). Affine closed points correspond to monic
irreducible polynomials. Niederreiter--Xing, Theorem 1.3.6, gives

\[
 I_q(d)=\frac1d\sum_{e\mid d}\mu_{\rm Mob}(e)q^{d/e}.
\]

The point at infinity has degree one, so

\[
 a_1=I_2(1)+1=3,\qquad
 a_d=I_2(d)=\frac1d\sum_{e\mid d}\mu_{\rm Mob}(e)2^{d/e}
 \quad(d\ge2).
\]

For every \(d\ge2\),

\[
\begin{aligned}
 d I_2(d)
 &\ge 2^d-\sum_{\substack{e\mid d\\e\ge2}}2^{d/e}\\
 &\ge 2^d-\sum_{j=1}^{\lfloor d/2\rfloor}2^j\\
 &=2^d-2^{\lfloor d/2\rfloor+1}+2>0.
\end{aligned}
\]

Therefore \(a_d>0\) for **every** \(d\ge1\). The later
infinite-multiplicity proof needs only one closed point in each of the degrees
\(b,2b,3b,\ldots\); it does not depend on the exponential growth of \(a_d\).

## 5. Invariant measures and weight invariance

### 5.1 Canonical representative

On \(C_x\), let \(du_x\) be flow-time Lebesgue measure. The direct image of
counting measure on the discrete geometric-point set times Lebesgue measure on
one roof interval is

\[
 \mu_1=\sum_xdu_x.
\]

It is invariant, sigma-finite, full-support, and Radon. Indeed, a compact
subset of the topological coproduct meets only finitely many clopen circle
components. Its total mass is infinite; there is no canonical probability
weight across the infinitely many arithmetic components.

### 5.2 Arbitrary positive component weights

For arbitrary \(0<w_x<\infty\), set

\[
 \mu_w|_{C_x}=w_x\,du_x,\qquad
 \mathcal H_w=L^2(M_F,\mu_w)
 =\bigoplus_x^{\,2}L^2(C_x,w_xdu_x).
\]

Every \(\mu_w\) is invariant, sigma-finite, full-support, and Radon. It is a
probability measure after a noncanonical choice with
\(\sum_xw_xL_x=1\). Componentwise normalized Haar measure is the special case
\(w_x=L_x^{-1}\).

**Weight-invariance theorem (`PROVED`).** Every positive component-weight
version is unitarily equivalent to the canonical one. Explicitly,

\[
 W_w:\mathcal H_w\longrightarrow\mathcal H_1,\qquad
 (W_wf)_x=\sqrt{w_x}\,f_x
\]

is unitary, and, because each weight is constant along its circle,

\[
 W_wU_t^{(w)}=U_t^{(1)}W_w,\qquad
 W_wA_w=A_1W_w
\]

on the corresponding domains. Neither probability normalization nor any
other positive component reweighting can change the spectrum, multiplicities,
compactness, or trace-class results below.

## 6. Koopman group and complete Stone generator

Freeze the pullback convention

\[
 (U_t^{(w)}f)_x(u)=f_x(u-t)=f\circ\phi^{-t}(u).
\]

The group is unitary because \(\mu_w\) is invariant. Translation is strongly
continuous on each circle. Approximation by finite-component vectors, together
with \(\|U_t^{(w)}\|=1\), proves strong continuity on the Hilbert direct sum.

Use \(U_t^{(w)}=e^{-itA_w}\). The generator is

\[
 A_w=\bigoplus_x A_x,\qquad A_x=-i\frac{d}{du},
\]

with periodic boundary conditions and domain

\[
\begin{split}
 \mathcal D(A_w)=\bigg\{f=(f_x):\;&
 f_x\in H^1_{\rm per}(0,L_x)\ \text{for every }x,\\
 &\sum_xw_x\left(
 \|f_x\|_{L^2(du_x)}^2+\|f_x'\|_{L^2(du_x)}^2
 \right)<\infty\bigg\}.
\end{split}
\]

Trigonometric polynomials supported on finitely many circles form a dense
core. Each \(A_x\) is self-adjoint. Teschl's orthogonal-direct-sum theorem
(Theorem 2.23) proves that \(A_w\) is self-adjoint and closed. Stone's theorem
(Teschl, Theorems 5.1--5.2; Stone 1932) identifies it as the unique
self-adjoint generator of the frozen group.

This supplies B1's measure, Hilbert space, inner product, dense domain,
boundary condition, action, closedness, clock, and sign convention. For
Route-B bookkeeping only, freeze \(E\leftrightarrow s=\tfrac12+iE\). That
notation is not evidence that any \(E\) is a Riemann-zero ordinate.

## 7. Exact component and global spectra

For \(n\in\mathbb Z\), put

\[
 e^{(w)}_{x,n}(u)
 =(w_xL_x)^{-1/2}
 \exp\!\left(\frac{2\pi inu}{L_x}\right).
\]

These vectors form an orthonormal basis of \(\mathcal H_w\), and

\[
 A_we^{(w)}_{x,n}
 =\lambda_{x,n}e^{(w)}_{x,n},\qquad
 \lambda_{x,n}=\frac{2\pi n}{d_x\log2}.
\]

Thus every primitive degree-\(d\) Frobenius circle contributes the Fourier
lattice

\[
 \frac{2\pi}{d\log2}\mathbb Z.
\]

Changing a circle origin only changes eigenfunction phases.

### 7.1 Point spectrum and multiplicity

The union of component eigenvalue sets is

\[
 \bigcup_{d\ge1}\frac{2\pi}{d\log2}\mathbb Z
 =\frac{2\pi}{\log2}\mathbb Q.
\]

Conversely, if \(A_wf=\lambda f\) and \(f\ne0\), then some component is
nonzero, so \(\lambda=2\pi n/(d_x\log2)\). Therefore

\[
 \boxed{\sigma_{\rm p}(A_w)=\frac{2\pi}{\log2}\mathbb Q.}
\]

Every point eigenvalue has countably infinite multiplicity. Write
\(q=a/b\in\mathbb Q\) in lowest terms. For every \(k\ge1\), choose a closed
point \(x_k\) of degree \(kb\) and mode \(n=ka\). These vectors occupy
different components and

\[
 \lambda_{x_k,ka}=\frac{2\pi}{\log2}\frac ab.
\]

For \(q=0\), use the \(n=0\) mode on every circle. Hence zero has infinite
multiplicity, but zero is not the only obstruction: the same is true at every
nonzero rational frequency.

### 7.2 Full and essential spectrum

Teschl's direct-sum theorem gives

\[
 \sigma(A_w)=
 \overline{\bigcup_x\sigma(A_x)}
 =\overline{\frac{2\pi}{\log2}\mathbb Q}
 =\mathbb R.
\]

The essential spectrum is also all of \(\mathbb R\). At a rational spectral
point, use infinitely many orthogonal exact eigenvectors. At an irrational
\(\lambda\), choose distinct rational eigenvalues \(\lambda_j\to\lambda\)
and corresponding eigenvectors on mutually distinct components. Then

\[
 \|(A_w-\lambda)e_j\|=|\lambda_j-\lambda|\to0,\qquad
 e_j\rightharpoonup0.
\]

The Weyl criterion yields

\[
 \boxed{\sigma(A_w)=\sigma_{\rm ess}(A_w)=\mathbb R,\qquad
 \sigma_{\rm disc}(A_w)=\varnothing.}
\]

Terminology matters. The Fourier vectors give a complete orthonormal
eigenbasis, so spectral measures are pure point. Simultaneously, the operator
spectrum as a closed set is \(\mathbb R\), and irrational reals are
non-eigenvalue limit points. Pure-point spectral measure does not imply
compact-resolvent discrete spectrum.

## 8. B3 obstruction package

All statements here are `PROVED` and weight independent.

### 8.1 No compact resolvent

For \(z\in\mathbb C\setminus\mathbb R\), take normalized zero modes on
distinct components. Then

\[
 (A_w-z)^{-1}e_{x,0}^{(w)}=-z^{-1}e_{x,0}^{(w)}.
\]

Their images have no convergent subsequence, so the resolvent is not compact.
Deleting the kernel does not help: repeat the argument in the
infinite-dimensional eigenspace of any fixed nonzero rational frequency.

### 8.2 No locally finite counting law

Every nonempty open interval contains a rational multiple of
\(2\pi/\log2\), whose eigenspace is infinite-dimensional. Consequently

\[
 \operatorname{rank}\mathbf1_I(A_w)=\infty
\]

for every interval \(I\) of positive width. A singleton irrational interval
has zero spectral projection, so the width qualifier is essential. In
particular,

\[
 N(E):=\dim\operatorname{Ran}\mathbf1_{[-E,E]}(A_w)=\infty
\]

for every \(E\ge0\). There is no intrinsic finite counting function to compare
with a Riemann--von Mangoldt law.

### 8.3 Heat operators are not trace class

For every \(t>0\), \(e^{-tA_w^2}\) is the identity on the
infinite-dimensional zero eigenspace, so it is not compact and

\[
 \operatorname{Tr}(e^{-tA_w^2})=\infty.
\]

Likewise \(e^{-t|A_w|}\) is not trace class. Even after deleting zero, any
fixed nonzero rational eigenspace contributes infinitely many copies of the
same positive heat eigenvalue. Since \(A_w\) is unbounded below,
\(e^{-tA_w}\) itself is not the relevant bounded heat operator; the precise
failures concern \(A_w^2\) and \(|A_w|\). Also
\((1+A_w^2)^{-s/2}\) is not trace class for any \(s>0\).

### 8.4 No standard generator spectral determinant

The ordinary Fredholm determinant \(\det(I+zK)\) is canonically defined for
trace-class \(K\) (Bornemann, §3). Here neither a resolvent nor the heat
regularizations above are trace class. The unitary \(U_t^{(w)}\) is not compact
and has infinitely many invariant vectors, so \(\det(I-zU_t^{(w)})\) is not
an ordinary Fredholm determinant either.

The dense, infinitely repeated eigenvalue ledger also prevents the standard
compact-resolvent spectral-zeta construction. This does not rule out every
author-chosen relative or renormalized determinant. It says that any
subtraction, compression, or regularization is extra data, not an intrinsic
determinant of the frozen Koopman generator.

## 9. Distinct operator ledgers

| Ledger | Object and space | What it counts | Audit result |
|---|---|---|---|
| Koopman/Stone | \(U_t=e^{-itA_w}\), \(A_w=-i\,d/du\) on \(\bigoplus_xL^2(C_x,w_xdu)\) | Fourier frequencies of observables on every suspension circle | complete, self-adjoint; B3 fails |
| Orbit / transfer / Lefschetz | primitive circles and repetitions, or a separately built transfer action | one factor \((1-e^{-sL_x})^{-1}\) per closed point | orbit product exact; no trace-class transfer operator on \(\mathcal H_w\) identified |
| Etale cohomological Frobenius | Frobenius on finite-dimensional \(H_c^i(\overline{\mathbb P}^1,\mathbb Q_\ell)\) | alternating finite-dimensional determinants, Deligne (1.5.4) | exact Hasse--Weil factors; different operator and space |

The shared arithmetic source proves

\[
 \zeta_{\rm orb}(s)
 =Z(\mathbb P^1_{\mathbb F_2},2^{-s})
 =\frac1{(1-2^{-s})(1-2^{1-s})}.
\]

It does **not** prove that this is a determinant of \(A_w\). The
cohomological formula is an alternating determinant of Frobenius on etale
cohomology; \(A_w\) is a self-adjoint differential operator on an infinite
Hilbert direct sum. Equality through a common closed-point ledger is not
operator conjugacy, unitary equivalence, or a Koopman trace identity.

Paper 3's same-object certificate forbids assembling T0, T3, and T5
coordinatewise from these different operators. A future bridge claim must
supply a morphism and prove a same-operator trace/determinant theorem.

## 10. Koopman lift is not physical quantization

Koopman theory gives unitary transport of classical observables by a
measure-preserving flow. The frozen candidate supplies no source-locked
symplectic phase space, prequantum line bundle, polarization, Planck scale, or
observable-to-operator rule. It also supplies no scattering system or
component interaction. Calling \(A_w\) “the Hamiltonian” would add an
interpretation not derived from the candidate.

Safe classifications:

- natural Koopman unitary lift: `PROVED`;
- self-adjoint Stone generator: `PROVED`;
- physical/geometric quantization: `NOT_TESTABLE` from frozen data;
- transfer/Lefschetz determinant identity for \(A_w\): `NOT_TESTABLE`, with
  the naive Fredholm version obstructed by proved non-trace-class results.

## 11. Route decisions

### Route A / A4

```yaml
candidate_id: FF-FROB-SUSP-P1-F2-KOOPMAN-P1
underlying_classical_candidate: FF-FROB-SUSP-P1-F2
a4_verdict: A4_UNITARY_OR_SCATTERING_CANDIDATE
evidence_status: PROVED
same_clock: true
zero_data_used: false
natural_unitary_lift: true
physical_quantization: NOT_TESTABLE
orbit_weight_trace_bridge: NOT_TESTABLE
route_b_ready: false
not_awarded:
  - A4_NATURAL_QUANTIZATION
  - A4_ROUTE_B_READY
reason: >-
  Koopman pullback is canonical and preserves the frozen clock, but no
  source-derived physical quantization or same-operator orbit-weight trace and
  determinant bridge exists; the exact spectrum also proves B3 failure.
```

For the Riemann target, Paper 4's A0, A2, A3 obstructions and
`ROUTE_A_REJECTED` verdict remain unchanged. A4 cannot repair the wrong
arithmetic support or one-clock divisor.

### Limited Route B / B1--B3

Route B would not normally open because Route A did not report
`ROUTE_A_SUCCESS_ROUTE_B_READY`. Stage 5 and the project lead authorize only
the early B1--B3 obstruction audit allowed by the Route-B evaluator.

```yaml
entry_status: PROJECT_LEAD_AUTHORIZED_LIMITED_EARLY_AUDIT
b1:
  verdict: B1_COMPLETE_OPERATOR_DEFINITION
  evidence_status: PROVED
b2:
  verdict: B2_SELF_ADJOINT
  evidence_status: PROVED
b3:
  verdict: B3_FAIL
  evidence_status: PROVED
audit_scope:
  included:
    - B1
    - B2
    - B3
  not_invoked:
    - B4
    - B5
overall_verdict: ROUTE_B_REJECTED
hilbert_polya_claim_allowed: false
```

B1 and B2 certify a rigorous operator, not a spectral host. B3 fails because
\(\sigma_{\rm ess}=\mathbb R\), every point eigenvalue has infinite
multiplicity, there is no compact resolvent or locally finite counting law, and
the standard determinant mechanisms are unavailable. B4 and B5 have no
verdict in this limited audit; the `not_invoked` list is a scope annotation,
not an evaluator enum or a serialized layer verdict.

## 12. Adversarial controls

| Control | Result | Consequence |
|---|---|---|
| arbitrary \(0<w_x<\infty\) | explicitly unitarily equivalent | weights cannot repair B3 |
| probability or normalized-Haar weights | cases of the same theorem | finite total mass cannot repair B3 |
| retain one closed point per degree | degrees \(kb\) still realize every rational frequency infinitely | exponential closed-point counts are not the cause |
| remove all zero modes | every nonzero rational eigenspace stays infinite-dimensional | kernel removal cannot restore compactness or heat trace |
| finitely many degrees | finite union has compact resolvent | artificial cutoff; no theorem for the full arithmetic object |
| substitute etale cohomology | exact native Hasse--Weil determinant | different space and operator ledger |
| add coupling, potential, or new boundary condition | spectral type may change | new candidate, not the Koopman generator |

## 13. Falsification and re-identification triggers

Reject this audit or assign a new candidate ID if:

1. a weight vanishes and deletes an arithmetic component;
2. a nonconstant density, potential, or component coupling is inserted;
3. a boundary condition other than periodic suspension gluing is used;
4. \(U_t\) is replaced by a transfer operator under the same ID;
5. the cohomological Frobenius determinant is called a determinant of \(A_w\);
6. “pure point” is used to claim compact-resolvent discreteness;
7. zero modes alone are blamed after nonzero infinite multiplicities are known;
8. a finite cutoff or regularized subtraction is hidden in the full candidate;
9. target zeros or fitted spectral maps enter the definition.

## 14. Next smallest theorem

The natural frozen lift is exhausted. Paper 6 should not extract a prime trace
from \(A_w\) by formal analogy. Its smallest legitimate question is:

> Is there a source-derived operator, distinct from but functorially connected
> to the Frobenius suspension, whose rigorous trace carries primitive
> closed-point repetition weights, and is there an explicit morphism relating
> that trace ledger to the Koopman or cohomological ledger?

Absent such a morphism, the reusable theorem is the obstruction: a disjoint
constant-roof Frobenius suspension's canonical Koopman generator has dense
rational point spectrum with infinite multiplicity and cannot support a
locally finite spectral determinant.
