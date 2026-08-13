# Proof Audit — Koopman Generator of the Frobenius Suspension

Audit date: 2026-08-13  
Candidate: `FF-FROB-SUSP-P1-F2-KOOPMAN-P1`  
Scope: theorem verification, edge cases, and adversarial controls  
Data policy: exact formulas only; no prime table, Riemann-zero table, fit, or
random search

## 1. Audit conclusion

The most natural unitary lift of Paper 4's frozen flow is mathematically
complete but spectrally disqualifying.

\[
\boxed{
\sigma_{\rm p}(A_K)=\frac{2\pi}{\log2}\mathbb Q,\qquad
\sigma(A_K)=\sigma_{\rm ess}(A_K)=\mathbb R.
}
\]

Every point eigenvalue has countably infinite multiplicity. This remains true
for all families of finite, strictly positive component weights, including noncanonical
probability weights, because the corresponding representations are unitarily
equivalent. It follows that:

- the resolvent is not compact;
- every interval of positive width has infinite spectral-projection rank;
- \(e^{-tA_K^2}\) and \(e^{-t|A_K|}\) are not trace class for \(t>0\);
- deleting the zero eigenspace does not repair any of these failures;
- no ordinary Fredholm determinant or compact-resolvent spectral-zeta
  determinant of the frozen generator produces the orbit Hasse--Weil zeta.

The positive operator verdicts are
`B1_COMPLETE_OPERATOR_DEFINITION` and `B2_SELF_ADJOINT`. The exact spectral
theorem forces `B3_FAIL`. B4 and B5 are not invoked in this limited audit.

## 2. Obligation matrix

| ID | Obligation | Result | Evidence |
|---|---|---|---|
| O1 | preserve Paper 4's object, topology, and clock | no classical field changed | `PROVED` by lock comparison |
| O2 | closed points of every positive degree | \(a_1=3\), \(a_d=I_2(d)>0\) for \(d\ge2\) | `PROVED` |
| O3 | invariant full-support measure | \(\mu_w|_{C_x}=w_xdu_x\), \(0<w_x<\infty\) | `PROVED` |
| O4 | weight robustness | \(W_wf=(\sqrt{w_x}f_x)_x\) is an intertwining unitary | `PROVED` |
| O5 | strongly continuous Koopman group | \(U_tf=f\circ\phi^{-t}\) | `PROVED` |
| O6 | complete generator domain | periodic component \(H^1\) plus global graph-norm summability | `PROVED` |
| O7 | self-adjointness | periodic Fourier multiplication and orthogonal sums | `PROVED` |
| O8 | exact component frequencies | \(2\pi n/(d_x\log2)\) | `PROVED` |
| O9 | exact point spectrum | \((2\pi/\log2)\mathbb Q\) | `PROVED` |
| O10 | multiplicity | countably infinite at every point eigenvalue | `PROVED` |
| O11 | full/essential spectrum | both equal \(\mathbb R\) | `PROVED` |
| O12 | compactness/counting | noncompact resolvent; infinite rank on every positive-width interval | `PROVED` |
| O13 | heat trace | not trace class, before or after kernel deletion | `PROVED` |
| O14 | determinant boundary | standard generator determinant unavailable | `PROVED` for standard constructions |
| O15 | same-object ledger | Koopman, orbit/transfer, and etale Frobenius actions kept separate | `PROVED` distinction |
| O16 | physical quantization | no source-locked quantization structure supplied | `NOT_TESTABLE`, not an impossibility theorem |

No obligation is supported only numerically.

## 3. Frozen definitions

Put \(\tau=\log2\). Paper 4 proves

\[
M_F\cong\coprod_{x\in|\mathbb P^1_{\mathbb F_2}|}C_x,\qquad
C_x=\mathbb R/(L_x\mathbb Z),\qquad
L_x=d_x\tau,\quad d_x=\deg x,
\]

and the flow is \(\phi^t_x(u)=u+t\pmod{L_x}\).

For constants \(0<w_x<\infty\), let

\[
\mu_w=\sum_xw_xdu_x,\qquad
\mathcal H_w=L^2(M_F,\mu_w)
=\bigoplus_x^{\,2}L^2(C_x,w_xdu_x).
\]

The pullback convention and Stone convention are

\[
(U_t^{(w)}f)_x(u)=f_x(u-t),\qquad
U_t^{(w)}=e^{-itA_w}.
\]

The proposed operator is

\[
A_w=\bigoplus_x\left(-i\frac d{du}\right)_x
\]

on

\[
\begin{split}
\mathcal D(A_w)=\bigg\{f=(f_x):\;&
 f_x\in H^1_{\rm per}(0,L_x)\ \forall x,\\
&\sum_xw_x\big(\|f_x\|_2^2+\|f'_x\|_2^2\big)<\infty
\bigg\}.
\end{split}
\]

All later claims refer to this one operator.

## 4. Arithmetic input: a closed point in every degree

### Lemma 4.1 — exact count

The number \(a_d\) of degree-\(d\) closed points of
\(\mathbb P^1_{\mathbb F_2}\) is

\[
a_1=3,\qquad
a_d=\frac1d\sum_{e\mid d}\mu_{\rm Mob}(e)2^{d/e}
\quad(d\ge2).
\]

**Proof.** Closed points of the affine chart are monic irreducible polynomials
over \(\mathbb F_2\). Niederreiter--Xing, Theorem 1.3.6, gives their count.
The point at infinity contributes one additional degree-one point. \(\square\)

### Lemma 4.2 — positivity in all degrees

\[
a_d>0\qquad(d\ge1).
\]

**Proof.** Degree one is immediate. For \(d\ge2\),

\[
\begin{aligned}
d\,a_d
&=2^d+\sum_{\substack{e\mid d\\e\ge2}}
  \mu_{\rm Mob}(e)2^{d/e}\\
&\ge2^d-\sum_{\substack{e\mid d\\e\ge2}}2^{d/e}\\
&\ge2^d-\sum_{j=1}^{\lfloor d/2\rfloor}2^j\\
&=2^d-2^{\lfloor d/2\rfloor+1}+2>0.
\end{aligned}
\]

The second inequality enlarges the set of exponents \(d/e\) to all integers
from one through \(\lfloor d/2\rfloor\). For \(d=2\) the last expression is
two; it is plainly positive thereafter. \(\square\)

### Minimal input actually used

The spectral multiplicity theorem uses only

\[
\forall d\ge1\quad a_d\ge1.
\]

It does not use the exact exponential size of \(a_d\). Therefore retaining
only one closed point per degree is already enough to produce the B3
obstruction.

## 5. Measure and weight audit

### Proposition 5.1 — measure properties

Every \(\mu_w\) is invariant, sigma-finite, full-support, and Radon.

**Proof.**

- Translation preserves \(du_x\), so it preserves the constant multiple
  \(w_xdu_x\) on every invariant component.
- There are countably many closed points and each circle has finite measure,
  giving sigma-finiteness.
- Strict positivity of \(w_x\) makes every nonempty open subset of every
  component have positive measure, hence full support.
- A compact subset of a topological coproduct meets only finitely many clopen
  components. Its intersection with each circle has finite weighted Lebesgue
  measure, proving the Radon property. \(\square\)

For \(w_x=1\), the measure is exactly the quotient of counting measure on the
geometric-point base times flow-time Lebesgue measure on a roof interval: a
degree-\(d\) cycle contributes \(d\) intervals of length \(\tau\), which join
to one circle of Lebesgue length \(d\tau\).

### Proposition 5.2 — unitary equivalence for every positive weight family

Define

\[
W_w:\mathcal H_w\to\mathcal H_1,\qquad
(W_wf)_x=\sqrt{w_x}f_x.
\]

Then

\[
W_wU_t^{(w)}=U_t^{(1)}W_w,\qquad
W_w\mathcal D(A_w)=\mathcal D(A_1),\qquad
W_wA_w=A_1W_w.
\]

**Proof.** Directly,

\[
\|W_wf\|_{\mathcal H_1}^2
=\sum_x\int_{C_x}w_x|f_x|^2du_x
=\|f\|_{\mathcal H_w}^2.
\]

The inverse is componentwise multiplication by \(w_x^{-1/2}\), which is
well-defined because \(0<w_x<\infty\). Constant multiplication commutes with
translation and differentiation. The same norm identity for \(f_x'\) proves
the domain assertion. \(\square\)

This proves that no strictly positive component reweighting can change any
unitary invariant, including spectral sets, multiplicities, resolvent
compactness, or trace ideals.

## 6. Strong continuity and the Stone generator

### Proposition 6.1 — \(C_0\) Koopman group

\((U_t^{(w)})_{t\in\mathbb R}\) is a strongly continuous unitary group.

**Proof.** The group law is the flow law. Proposition 5.1 gives unitarity.
Circle translations are strongly continuous on each \(L^2(C_x)\). Given
\(f\in\mathcal H_w\) and \(\epsilon>0\), choose a finite-component vector
\(g\) with \(\|f-g\|<\epsilon\). Then

\[
\|U_tf-f\|
\le2\|f-g\|+\|U_tg-g\|.
\]

The last term tends to zero because \(g\) occupies a finite direct sum.
\(\square\)

### Proposition 6.2 — component operator

On \(L^2(C_x,w_xdu_x)\), the periodic derivative

\[
A_x=-i\frac d{du},\qquad
\mathcal D(A_x)=H^1_{\rm per}(0,L_x),
\]

is self-adjoint and has normalized eigenbasis

\[
e^{(w)}_{x,n}(u)
=(w_xL_x)^{-1/2}e^{2\pi inu/L_x},
\qquad n\in\mathbb Z,
\]

with eigenvalues \(2\pi n/L_x\).

**Proof.** Periodic Fourier transform is unitary from the component
\(L^2\)-space to \(\ell^2(\mathbb Z)\). It sends \(A_x\) to multiplication by
the real sequence \(2\pi n/L_x\), on the maximal domain for which the
multiplied sequence is square summable. This domain is exactly periodic
\(H^1\). Real multiplication on its maximal domain is self-adjoint.
\(\square\)

### Theorem 6.3 — global self-adjointness

\(A_w=\bigoplus_xA_x\) is self-adjoint and is the Stone generator of
\(U_t^{(w)}\).

**Proof.** Teschl, Theorem 2.23, proves self-adjointness of a countable
orthogonal sum on the maximal graph-summability domain; that is exactly the
frozen domain. Componentwise exponentiation gives the translation group.
Stone's theorem gives uniqueness. The sign is consistent:

\[
\left.\frac d{dt}U_tf\right|_{t=0}=-f'
=-i\left(-i\frac d{du}\right)f.
\]

\(\square\)

Finite-component trigonometric polynomials are a dense core, since finite
component truncation and finite Fourier truncation approximate in the global
graph norm.

## 7. Spectral theorem

### Theorem 7.1 — exact point spectrum

\[
\sigma_{\rm p}(A_w)=\frac{2\pi}{\log2}\mathbb Q.
\]

**Proof.** A closed point of degree \(d\) contributes

\[
\frac{2\pi}{d\log2}\mathbb Z.
\]

Lemma 4.2 supplies at least one such circle for every \(d\), so the union is
\((2\pi/\log2)\mathbb Q\). Conversely, if \(A_wf=\lambda f\) and \(f\ne0\),
then some component \(f_x\ne0\) and satisfies \(A_xf_x=\lambda f_x\). The
component Fourier calculation forces
\(\lambda=2\pi n/(d_x\log2)\). \(\square\)

### Theorem 7.2 — every point eigenvalue has infinite multiplicity

Let \(q=a/b\) in lowest terms with \(b\ge1\). For every \(k\ge1\), choose one
closed point \(x_k\) of degree \(kb\) and Fourier mode \(n=ka\). Then

\[
A_we_{x_k,ka}^{(w)}
=\frac{2\pi}{\log2}\frac ab\,e_{x_k,ka}^{(w)}.
\]

These vectors lie on distinct components and are orthonormal. Hence the
multiplicity is at least countably infinite. It is at most countable because
the full Hilbert space has a countable Fourier basis. For \(a=0,b=1\), this is
the constant mode on each component. \(\square\)

### Theorem 7.3 — full spectrum

\[
\sigma(A_w)=\mathbb R.
\]

**Proof.** Teschl, Theorem 2.23, gives

\[
\sigma(A_w)=\overline{\bigcup_x\sigma(A_x)}
=\overline{\frac{2\pi}{\log2}\mathbb Q}=\mathbb R.
\]

\(\square\)

### Theorem 7.4 — essential and discrete spectra

\[
\sigma_{\rm ess}(A_w)=\mathbb R,\qquad
\sigma_{\rm disc}(A_w)=\varnothing.
\]

**First proof.** Teschl's characterization (equation (6.28)) says that
\(\lambda\) is essential precisely when every symmetric neighborhood has
infinite spectral-projection rank. Every such neighborhood contains a rational
frequency, and Theorem 7.2 gives an infinite-dimensional eigenspace inside the
projection.

**Second proof / Weyl control.** At a rational point, take exact eigenvectors
on distinct components. At irrational \(\lambda\), choose distinct rational
frequencies \(\lambda_j\to\lambda\) and eigenvectors supported on mutually
distinct components. Then

\[
\|(A_w-\lambda)e_j\|=|\lambda_j-\lambda|\to0,\qquad
e_j\rightharpoonup0.
\]

Thus every real point has a singular Weyl sequence. \(\square\)

### Spectral-type terminology

The set

\[
\{e_{x,n}^{(w)}:x\in|\mathbb P^1_{\mathbb F_2}|,\ n\in\mathbb Z\}
\]

is a complete orthonormal eigenbasis. Hence every vector spectral measure is
pure point. This does not contradict the set-theoretic decomposition

\[
\sigma_{\rm p}(A_w)=\frac{2\pi}{\log2}\mathbb Q,\qquad
\sigma_{\rm c}(A_w)=
\mathbb R\setminus\frac{2\pi}{\log2}\mathbb Q,
\]

with empty residual spectrum for a self-adjoint operator. Irrational points
are injective, dense-range, nonsurjective accumulation points. “Pure-point
spectral measures” and “compact-resolvent discrete spectrum” are different
properties.

## 8. Consequences forcing B3 failure

### Proposition 8.1 — noncompact resolvent

For \(z\notin\mathbb R\),

\[
(A_w-z)^{-1}e_{x,0}^{(w)}=-z^{-1}e_{x,0}^{(w)}.
\]

An infinite orthonormal set is sent to a fixed nonzero scalar multiple of
itself. The image has no norm-convergent subsequence, so the resolvent is not
compact.

The proof is not kernel-dependent. On the orthogonal complement of the kernel,
fix any nonzero rational eigenvalue \(\lambda\); its infinite-dimensional
eigenspace is multiplied by \((\lambda-z)^{-1}\).

### Proposition 8.2 — no locally finite counting

If \(I\subset\mathbb R\) is any interval of positive width, it contains a
frequency in \((2\pi/\log2)\mathbb Q\). Therefore

\[
\operatorname{rank}\mathbf1_I(A_w)=\infty.
\]

In particular,

\[
N(E)=\dim\operatorname{Ran}\mathbf1_{[-E,E]}(A_w)=\infty
\qquad(E\ge0).
\]

The qualifier “positive width” is necessary. A singleton irrational set has
zero spectral projection; the audit makes no contrary claim.

### Proposition 8.3 — no trace-class heat

For \(t>0\), \(e^{-tA_w^2}\) fixes every zero mode. Hence it is noncompact and

\[
\operatorname{Tr}(e^{-tA_w^2})=\infty.
\]

Likewise \(e^{-t|A_w|}\) is not trace class. After deleting zero modes, choose
any nonzero rational eigenvalue \(\lambda\); infinitely many orthonormal
vectors receive the same positive multiplier \(e^{-t\lambda^2}\), respectively
\(e^{-t|\lambda|}\). Thus the reduced heat operators are still not trace
class. The same argument applies to \((1+A_w^2)^{-s/2}\) for every \(s>0\).

The notation \(e^{-tA_w}\) is intentionally avoided as a heat kernel because
\(A_w\) is unbounded below.

### Proposition 8.4 — determinant boundary

Bornemann §3 reviews the canonical Fredholm determinant
\(\det(I+zK)\) for trace-class \(K\). The resolvent and heat functions above
are not trace class; \(U_t\) itself is an infinite-dimensional unitary with
eigenvalue one of infinite multiplicity and is not trace class. Therefore the
ordinary Fredholm determinants suggested by these frozen inputs are
undefined.

A standard spectral-zeta determinant based on discrete compact-resolvent
eigenvalues is also unavailable: every positive-width window already has
infinite rank. This conclusion is scoped. A relative, compressed, or
renormalized determinant after additional choices is a new construction, not
an intrinsic determinant of \(A_w\).

## 9. Same-object determinant audit

### Ledger K — Koopman/Stone

\[
\mathcal H_w=\bigoplus_xL^2(C_x,w_xdu_x),\qquad
A_w=\bigoplus_x(-i\,d/du)_{\rm per}.
\]

This ledger counts Fourier modes of observables. Its point frequencies are
dense rational multiples of \(2\pi/\log2\), all infinitely repeated.

### Ledger O — primitive orbit product

\[
\prod_x(1-e^{-s d_x\log2})^{-1}.
\]

This ledger counts one primitive suspension circle per closed point and all
positive repetitions. It is an exact scalar orbit product.

### Ledger C — cohomological Frobenius

Deligne's equation (1.5.4) is an alternating product of finite-dimensional
determinants of Frobenius on etale cohomology. It explains the native
Hasse--Weil rational function.

### Non-identification theorem

The exact scalar equality between Ledger O and the Hasse--Weil expression in
Ledger C follows from their common closed-point arithmetic. It supplies no
unitary map, conjugacy, trace identity, or determinant identity between Ledger
K and Ledger C. Their spaces, actions, spectral types, and determinant
mechanisms differ explicitly.

Paper 3's same-object certificate therefore blocks a coordinatewise merge:
T0 object identity, T3 analytic/operator ledger, and T5 coefficient provenance
cannot be taken from separate rows and presented as one construction.

## 10. A4 and Route-B proof verdicts

### A4

The Koopman lift is intrinsic to the flow, preserves the same clock, and has a
named Hilbert space and domain. Thus:

```text
A4_UNITARY_OR_SCATTERING_CANDIDATE — PROVED
```

It is not awarded `A4_NATURAL_QUANTIZATION`: the frozen data do not supply a
symplectic/prequantum/polarization or alternative physical quantization map.
It is not awarded `A4_ROUTE_B_READY`: the orbit weights are not a trace of the
same operator, and B3 fails.

### Limited B1--B3 audit

```text
B1_COMPLETE_OPERATOR_DEFINITION — PROVED
B2_SELF_ADJOINT — PROVED
B3_FAIL — PROVED
overall scoped result: ROUTE_B_REJECTED
hilbert_polya_claim_allowed: false
```

B4 and B5 are outside this audit and receive no layer verdict.

## 11. Adversarial review

| Hostile objection or repair | Audit response |
|---|---|
| “The infinite mass causes the problem.” | False. Choose summable positive probability weights; Proposition 5.2 gives unitary equivalence. |
| “Normalize Haar on each circle.” | This is \(w_x=L_x^{-1}>0\), again unitarily equivalent. |
| “There are too many closed points of each degree.” | Keep one per degree; degrees \(kb\) still give every rational frequency infinitely often. |
| “Only invariant functions cause divergence.” | Delete all zero modes; every nonzero rational eigenspace remains infinite-dimensional. |
| “Pure point means discrete.” | False here. The eigenbasis is pure point, but eigenvalues are dense and infinitely repeated; \(\sigma_{\rm ess}=\mathbb R\). |
| “Use a finite degree cutoff.” | A finite union has compact resolvent, but it is a new cutoff object and no limit determinant is frozen. |
| “Use Deligne's determinant.” | It is exact on etale cohomology and is a different operator ledger. |
| “Add coupling or a potential.” | That may alter spectral type but creates a new candidate requiring provenance, domain, and same-object audits. |
| “Call the Stone generator a quantum Hamiltonian.” | Unitary evolution alone is not a source-derived physical quantization. |
| “Regularize the infinite multiplicities.” | A specific subtraction/compression must be stated and becomes new data; it cannot be attributed to the locked generator. |

## 12. Edge-case checklist

- [x] degree one includes \(0,1,\infty\);
- [x] negative rational frequencies use negative Fourier modes;
- [x] \(q=0\) handled separately without an invalid denominator choice;
- [x] all eigenspace multiplicities are countably, not uncountably, infinite;
- [x] weights are finite, strictly positive, and componentwise constant;
- [x] probability weights are permitted but noncanonical;
- [x] the group sign \(f(u-t)\) matches \(A=-i\,d/du\);
- [x] the global operator domain includes derivative square summability;
- [x] singleton irrational spectral projections are not called infinite rank;
- [x] pure-point spectral measures are distinguished from the continuous
  subset of the operator spectrum;
- [x] heat is stated for \(A^2\) or \(|A|\), not the unbounded \(e^{-tA}\);
- [x] zero-mode deletion is tested;
- [x] ordinary and regularized determinant claims are separated;
- [x] no cohomological operator is relabeled as Koopman;
- [x] no target-zero or fitting data enter any step.

## 13. Proof dependencies

```text
closed-point count in every degree
        |
        v
circle Fourier lattices ---- positive-weight unitary equivalence
        |                              |
        +--------------+---------------+
                       v
point spectrum = (2 pi / log 2) Q
every point eigenvalue has infinite multiplicity
                       |
          +------------+------------+
          v            v            v
 spectrum/ess = R   no local N(E)   heat/resolvent noncompact
          \            |            /
           +-----------+-----------+
                       v
                    B3_FAIL
                       |
                       v
no standard AK determinant = orbit Hasse--Weil zeta
```

The cohomological determinant enters only in the final ledger comparison; it
does not enter the proof of self-adjointness or spectral type.

## 14. Final proof certificate

```yaml
candidate_id: FF-FROB-SUSP-P1-F2-KOOPMAN-P1
proof_status: COMPLETE_FOR_PHASE_1_B1_B3_AUDIT
source_status: LOCKED
all_positive_component_weights_unitarily_equivalent: true
point_spectrum: (2 pi / log(2)) Q
point_multiplicity: countably_infinite_at_every_point_eigenvalue
spectrum: R
essential_spectrum: R
discrete_spectrum: empty
complete_pure_point_eigenbasis: true
irrational_continuous_spectrum_points: true
compact_resolvent: false
positive_width_local_projection_rank: infinite
heat_trace_class: false
kernel_deletion_repairs_failure: false
orbit_zeta_is_generator_determinant: false
a4: A4_UNITARY_OR_SCATTERING_CANDIDATE
b1: B1_COMPLETE_OPERATOR_DEFINITION
b2: B2_SELF_ADJOINT
b3: B3_FAIL
uninvoked_layers:
  - B4
  - B5
overall_scoped_route_b: ROUTE_B_REJECTED
hilbert_polya_claim_allowed: false
target_zero_data_used: false
```
