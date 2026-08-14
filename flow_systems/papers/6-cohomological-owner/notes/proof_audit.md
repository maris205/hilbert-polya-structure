# Stage 6 Proof Audit — The Exact Determinant Owner

Audit date: **2026-08-13**  
Candidate: `FF-FROB-OPERATOR-OWNERSHIP-P1-F2`  
Scope: exact comparison of the orbit, Koopman and cohomological ledgers of one
finite-field parent  
Route scope: native Route-A positive control and a limited early Route-B
failure audit; no Riemann-zero data and no Hilbert--Polya claim

## 1. Audit conclusion

The frozen arithmetic parent provides a genuine same-source bridge, but not a
single all-purpose operator.

- The scheme/Frobenius pair generates the closed-point ledger, the discrete
  suspension cycles and the etale-cohomological action.  Deligne's trace
  identity proves that the orbit Hasse--Weil zeta is exactly the graded
  determinant of Frobenius on cohomology.
- The natural Koopman translation lift is a fully defined self-adjoint
  operator.  Its point frequencies are
  \((2\pi/\log2)\mathbb Q\), each with infinite multiplicity, and its full and
  essential spectra are both \(\mathbb R\).  It has neither compact resolvent
  nor a trace-class heat operator.
- The two ledgers therefore have different operator owners.  B1--B2 from the
  Koopman generator cannot be joined to the native Lefschetz determinant of
  cohomological Frobenius as though one unnamed operator supplied both.

For the native finite-field target this is a positive same-arithmetic-parent
Lefschetz calibration.  For the Riemann target the fixed characteristic-two
clock, lattice-periodic divisor and wrong operator spectral type force Route A
and the limited Route-B audit to reject promotion.

## 2. Frozen definitions

Let

\[
 X=\mathbb P^1_{\mathbb F_2},\qquad
 S=X(\overline{\mathbb F}_2)_{\rm disc},\qquad
 F(a)=a^2,\qquad \tau=\log2.
\]

The mapping torus and its vertical flow are

\[
 M_F=(S\times\mathbb R)/((a,u)\sim(Fa,u-\tau)),
 \qquad \phi^t[a,u]=[a,u+t].
\]

Stage 4 proved the flow decomposition

\[
 M_F\cong
 \coprod_{x\in|X|}\mathbb R/(d_x\tau)\mathbb Z,
 \qquad d_x=\deg x,
\]

with one primitive circle \(C_x\) of length
\(\ell_x=d_x\tau=\log N(x)\) per closed point.

Choose arbitrary finite positive constants \(w_x\).  The Koopman Hilbert
space is

\[
 \mathcal H_K=\bigoplus_{x\in|X|}
 L^2(C_x,w_xdu),
\]

and

\[
 A_K=-i\frac d{du}
\]

has the periodic graph domain

\[
 \mathcal D(A_K)=\left\{(f_x):
 f_x\in H^1_{\rm per}(C_x),\quad
 \sum_x\bigl(\|f_x\|^2_{L^2(C_x,w_xdu)}
 +\|f_x'\|^2_{L^2(C_x,w_xdu)}\bigr)<\infty\right\}.
\]

Fix \(\ell\ne2\).  The cohomological operator is the Frobenius action
\(\Phi\) in Deligne's trace convention on

\[
 H^\bullet_{\rm et}
 =\bigoplus_{i=0}^2
 H^i_{\rm et}(X_{\overline{\mathbb F}_2},\mathbb Q_\ell).
\]

For the frozen example,

\[
 H^0\cong\mathbb Q_\ell,qquad H^1=0,qquad
 H^2\cong\mathbb Q_\ell(-1),
\]

and the two nonzero trace eigenvalues are \(1\) and \(2\).  The native zeta
variable is \(t\), later related to the suspension clock by \(t=2^{-s}\).

## 3. Closed points occur in every degree

Let \(I_d\) be the number of monic irreducible polynomials of degree \(d\)
over \(\mathbb F_2\).  Mobius inversion gives

\[
 I_d=\frac1d\sum_{e\mid d}\mu(e)2^{d/e}.
\]

The number \(a_d\) of degree-\(d\) closed points of \(\mathbb P^1/\mathbb F_2\)
is

\[
 a_1=I_1+1=3,
 \qquad a_d=I_d\quad(d>1),
\]

where the additional degree-one point is infinity.

### Lemma 3.1 — positivity in every degree

For every \(d\ge1\), \(a_d>0\).

#### Proof

The case \(d=1\) is immediate.  For \(d\ge2\), discard the positive terms
other than \(2^d\) and bound every remaining term in absolute value:

\[
 dI_d
 \ge 2^d-\sum_{\substack{e\mid d\\e\ge2}}2^{d/e}
 \ge 2^d-\sum_{m=1}^{\lfloor d/2\rfloor}2^m
 =2^d-2^{\lfloor d/2\rfloor+1}+2>0.
\]

Thus \(I_d\), an integer, is positive. \(\square\)

This elementary proof is stronger than any finite enumeration and makes the
later infinite-multiplicity argument cutoff-free.

## 4. Exact cohomological trace and determinant

### Theorem 4.1 — three exact ledgers

For every \(n\ge1\),

\[
 \sum_{d\mid n}d a_d
 =\#\mathbb P^1(\mathbb F_{2^n})
 =1+2^n
 =\sum_i(-1)^i
   \operatorname{tr}(\Phi^n\mid H^i).
\]

#### Proof

A primitive Frobenius cycle of least length \(d\) contributes all of its
\(d\) geometric points to \(\operatorname{Fix}(F^n)\) exactly when \(d\mid n\),
giving the first equality.  The projective line has \(2^n\) affine points and
one point at infinity, giving the second.  Deligne's Lefschetz formula gives
the third.  In this example the last expression is also directly
\(1^n+2^n\), because the odd cohomology vanishes. \(\square\)

### Corollary 4.2 — determinant ownership

As formal power series at \(t=0\), and analytically for \(|t|<1/2\),

\[
\begin{aligned}
 Z(X,t)
 &=\exp\left(\sum_{n\ge1}\frac{1+2^n}{n}t^n\right)\\
 &=\prod_{x\in|X|}(1-t^{d_x})^{-1}\\
 &=\prod_i\det(1-t\Phi\mid H^i)^{(-1)^{i+1}}\\
 &=\frac1{(1-t)(1-2t)}.
\end{aligned}
\]

With \(t=2^{-s}\), the left closed-point product is exactly the Stage-4
primitive-orbit product of the suspension.

#### Proof

Theorem 4.1 and the formal identities

\[
 -\log(1-z)=\sum_{r\ge1}\frac{z^r}{r},
 \qquad
 -\log\det(1-tT)
 =\sum_{n\ge1}\frac{\operatorname{tr}(T^n)}n t^n
\]

give every equality.  Absolute convergence for \(|t|<1/2\) justifies the
analytic reading; the rational expression then continues the function.
\(\square\)

The theorem identifies the determinant owner precisely: \(\Phi\) on graded
etale cohomology.  It does not say that the same rational function is a
Fredholm or spectral determinant of \(A_K\).

## 5. The natural Koopman generator

### Proposition 5.1 — component weights do not change the operator type

For every family \((w_x)\) with \(0<w_x<\infty\), the map

\[
 V_w:(f_x)_x\longmapsto(\sqrt{w_x}f_x)_x
\]

is unitary from \(\mathcal H_K\) to the unweighted direct sum and intertwines
the translation groups and their generators.

#### Proof

Componentwise,
\(\|\sqrt{w_x}f_x\|^2_{L^2(du)}=\|f_x\|^2_{L^2(w_xdu)}\), and summing gives a
surjective isometry.  Constant multiplication commutes with translation and
differentiation. \(\square\)

Thus no choice of positive component masses can repair the spectral type.
This differs from Stage 2, where cross-packet masses were missing from a
proposed measured trace: here the weights define unitarily equivalent Hilbert
representations, not a packet Euler coefficient.

### Proposition 5.2 — self-adjointness and Fourier ledger

The operator \(A_K\) on the displayed domain is self-adjoint.  On a component
of degree \(d\), it has normalized Fourier eigenfunctions and eigenvalues

\[
 e_{d,n}(u)=\frac{e^{2\pi inu/(d\tau)}}{\sqrt{w_xd\tau}},
 \qquad
 \lambda_{d,n}=\frac{2\pi n}{d\tau},
 \qquad n\in\mathbb Z.
\]

The union over all components is a complete orthonormal eigenbasis of
\(\mathcal H_K\).

#### Proof

The periodic derivative on one circle is self-adjoint on
\(H^1_{\rm per}\) and diagonal in its Fourier basis.  The countable
orthogonal sum of these self-adjoint operators is self-adjoint precisely on
the square-summable graph domain written in Section 2.  Orthogonal sums of
the component Fourier bases form an orthonormal basis. \(\square\)

This passes Route-B B1 and B2.  It says nothing yet about B3.

### Theorem 5.3 — exact spectral type

Put \(c=2\pi/\log2\).  Then

\[
 \sigma_p(A_K)=c\mathbb Q,
 \qquad
 \sigma(A_K)=\sigma_{\rm ess}(A_K)=\mathbb R.
\]

Every eigenvalue in \(c\mathbb Q\) has countably infinite multiplicity.  The
spectral measures nevertheless remain pure point because the Fourier
eigenvectors form a complete basis; points of
\(\mathbb R\setminus c\mathbb Q\) are set-theoretic continuous-spectrum
accumulation points, not eigenvalues.

#### Proof

By Lemma 3.1, at least one component exists in every degree.  The component
frequencies therefore have union

\[
 \bigcup_{d\ge1}\left\{c\frac nd:n\in\mathbb Z\right\}=c\mathbb Q.
\]

If \(q=a/b\) is in lowest terms, then for every multiple \(d=jb\), the
integer mode \(n=ja\) gives frequency \(cq\).  Lemma 3.1 supplies at least one
distinct degree-\(d\) component for every \(j\), producing an infinite
orthonormal family at that eigenvalue.

The spectrum of a countable self-adjoint orthogonal sum is the closure of the
union of its component spectra.  Since \(\mathbb Q\) is dense,
\(\sigma(A_K)=\mathbb R\).  Finally, every neighborhood of every real number
contains a rational-scaled eigenvalue with an infinite-dimensional
eigenspace.  Its spectral projection therefore has infinite rank.  The
standard self-adjoint essential-spectrum criterion gives
\(\sigma_{\rm ess}(A_K)=\mathbb R\). \(\square\)

### Corollary 5.4 — no compact-resolvent or heat-trace route

The resolvent of \(A_K\) is not compact.  For every \(t>0\),
\(e^{-tA_K^2}\) is neither compact nor trace class.  Every open spectral
interval has infinite-dimensional spectral projection.

#### Proof

The zero Fourier mode occurs on every primitive circle, so
\(\ker A_K\) is infinite-dimensional.  For \(z\notin\mathbb R\), the
resolvent \((A_K-z)^{-1}\) acts as multiplication by \(-1/z\) on this
subspace, which prevents compactness.  The heat operator acts as the identity
on the same subspace and is therefore not compact or trace class.  The final
statement was established in Theorem 5.3. \(\square\)

Consequently the ordinary heat-zeta/spectral-determinant mechanism required by
Route-B B3 is unavailable.  The statement does not prohibit every conceivable
renormalized distribution on this flow.

## 6. The two operator owners cannot be merged

### Theorem 6.1 — operator-ownership separation

For the frozen parent, the following are all true:

1. \(A_K\) is the Stone generator of suspension time and is self-adjoint;
2. \(\Phi\) owns the exact native Lefschetz determinant in Corollary 4.2;
3. no unitary equivalence identifies these two operators;
4. the direct sum of \(A_K\) with any finite-dimensional realization of
   \(\Phi\) still has essential spectrum \(\mathbb R\), noncompact resolvent
   and non-trace-class heat evolution.

Hence a Route-B certificate may not take B2 from \(A_K\) and an exact
determinant/trace credit from \(\Phi\) without constructing and proving a new
operator-level bridge.

#### Proof

The first two items are Propositions 5.2 and Corollary 4.2.  The Koopman
operator acts on an infinite-dimensional complex Hilbert space and has
spectrum \(\mathbb R\), whereas cohomological Frobenius is a two-dimensional
graded \(\mathbb Q_\ell\)-linear action with eigenvalue ledger \(\{1,2\}\).
They cannot be unitarily equivalent.  Even after a noncanonical complex
realization of \(\Phi\), a finite-dimensional direct summand is a finite-rank
addition at the resolvent level and cannot remove the infinite zero
eigenspace or any of the conclusions in Corollary 5.4. \(\square\)

The theorem is frozen-object specific.  It does not rule out a new
cohomological flow, a different Hilbert completion, an anisotropic transfer
operator or another source-derived bridge.  Any such construction is a new
candidate and must restart the T0--T7 and B1--B5 ledgers.

## 7. Divisor after the clock substitution

### Proposition 7.1 — lifted native divisor

For a Frobenius eigenvalue \(\alpha\in\{1,2\}\), the equation

\[
 1-\alpha2^{-s}=0
\]

has solutions

\[
 s=\frac{\log\alpha+2\pi ik}{\log2},
 \qquad k\in\mathbb Z.
\]

Thus the two inverse determinant factors give pole lattices on
\(\Re s=0\) and \(\Re s=1\).  The full function is periodic under
\(s\mapsto s+2\pi i/\log2\).

#### Proof

The equation is equivalent to
\(\exp(\log\alpha-s\log2)=1\).  Solving modulo \(2\pi i\mathbb Z\) and
renaming the integer sign gives the formula. \(\square\)

These repeated poles are preimages under \(t=2^{-s}\), not the spectrum of a
new self-adjoint operator.  In particular, the frozen \(\mathbb P^1\) zeta
has no nontrivial zero ledger to promote.

## 8. Same-object certificate result

The Stage-3 typed certificate gives the following exact split.

| Gate | Native orbit--cohomology reading | Koopman reading | Riemann promotion |
|---|---|---|---|
| T0 object identity | pass: scheme, Frobenius cycles and cohomology are linked by Deligne's theorem | pass for the suspension/operator record | no coordinatewise merge across \(A_K\) and \(\Phi\) |
| T1 classical ledger | complete closed-point/primitive-circle ledger | same complete ledger | wrong rational-prime support |
| T2 trace definition | finite graded cohomological trace | ordinary Koopman trace absent; heat trace diverges | fail |
| T3 analytic ledger | finite \(\mathbb Q_\ell\)-linear Frobenius action | complete self-adjoint operator/domain | no single target operator |
| T4 theorem extent | exact global formal/analytic identity | exact spectrum theorem | no completed-xi identity |
| T5 coefficients | signs and \(1/n\) repetitions derived by graded determinant | Fourier multiplicities derived, not orbit trace weights | fail |
| T6 clock/normalization | \(t=2^{-s}\), roof \(\log2\), conventions explicit | same suspension clock | one-characteristic periodicity |
| T7 arithmetic promotion | native closed points only | no von Mangoldt rational-prime trace | refuted for rational primes |

This is a genuine positive control for a same-arithmetic-parent
orbit--Lefschetz interface.  It also shows why T0 alone is weaker than the
single-operator obligation in Route B.

## 9. Deterministic controls

The reproduction program uses exact integers and rational numbers only.  It
performs four independent software audits.

1. Mobius inversion computes \(a_d\), checks \(a_d>0\), and verifies
   \(\sum_{d\mid n}d a_d=2^n+1\) through the frozen cutoff.
2. The point-count, cycle and cohomological trace coefficients are compared
   exactly.
3. Selected rational Koopman frequencies are tracked across increasing degree
   cutoffs to illustrate the proved multiplicity growth.
4. The two Frobenius factors and their lifted pole lattices are emitted as a
   typed divisor ledger.

The finite controls do not prove Theorem 5.3.  The theorem follows from Lemma
3.1 and exact direct-sum spectral theory.  The current reproduction reports
10/10 unit tests passing and hash-locks every generated artifact.

## 10. Route decisions

### 10.1 Native finite-field target

| Layer | Verdict | Evidence | Boundary |
|---|---|---|---|
| A0 | `A0_ANALYTIC_ARITHMETIC_ORIGIN` | `PROVED` | fixed scheme/Frobenius generates every ledger |
| A1 | `A1_PASS_ANALYTIC` | `PROVED` | one closed point/cycle/circle, complete repetitions |
| A2 | `A2_ANALYTIC_DETERMINANT` | `PROVED` | exact native orbit and cohomological determinant |
| A3 | `A3_CONTROLLED_CONTINUATION` | `PROVED` | rational native continuation; no Riemann promotion |
| A4 | `A4_UNITARY_OR_SCATTERING_CANDIDATE` | `PROVED` as a natural unitary lift | its spectral type and trace fail Route B |

Scoped native status: `ROUTE_A_SUCCESS_ROUTE_B_NOT_READY`.  This is a
finite-field calibration label, not a Riemann-candidate label.

### 10.2 Riemann rational-prime target

| Layer | Verdict | Evidence | Boundary |
|---|---|---|---|
| A0 | `A0_FAIL` | `PROVED` | only characteristic-two prime-power clock |
| A1 | `A1_PASS_ANALYTIC` for the native flow | `PROVED` | wrong arithmetic support |
| A2 | `A2_FAIL` | `PROVED` | wrong Euler product/divisor |
| A3 | `A3_FAIL` | `PROVED` | no gamma factor, completed FE or rational-prime Weil ledger |
| A4 | `A4_UNITARY_OR_SCATTERING_CANDIDATE` | `PROVED` as a lift | naturality cannot repair A0--A3 |

Overall: `ROUTE_A_REJECTED` for the Riemann target.

### 10.3 Limited early Route-B audit

The audit is limited to the natural operator and its exact spectral type.  It
does not attempt to rescue the rejected Route-A target fit.

| Layer | Verdict | Evidence | Strongest failure |
|---|---|---|---|
| B1 | `B1_COMPLETE_OPERATOR_DEFINITION` | `PROVED` | none at definition level |
| B2 | `B2_SELF_ADJOINT` | `PROVED` | none at self-adjointness level |
| B3 | `B3_FAIL` | `PROVED` | essential spectrum \(\mathbb R\), infinite multiplicities, no compact resolvent/heat trace |
| B4 | `B4_FAIL` | `PROVED` for frozen operator | no rational-prime/von-Mangoldt trace; native exact trace belongs to \(\Phi\) |
| B5 | `B5_FAIL` | `PROVED` | no global completed-\(\xi\) determinant identity |

Overall: `ROUTE_B_REJECTED`.  `hilbert_polya_claim_allowed: false`.

## 11. Adversarial controls and claim boundary

- **Positive weights:** Proposition 5.1 shows all choices are unitarily
  equivalent.
- **Finite truncation:** it creates a finite matrix but cannot certify the
  infinite operator; multiplicities grow with the cutoff.
- **Same-cycle-type permutation:** the bare orbit and Koopman ledgers survive
  while the algebraic/cohomological origin disappears.
- **Direct-sum repair:** Theorem 6.1 preserves essential spectrum and heat
  failure.
- **Universal Euler compiler:** prescribed circles reproduce arbitrary Euler
  products and therefore fail A0.
- **False-RH controls:** the proof asserts only exact finite-field identities
  and operator separation, so it derives no positivity or RH statement for a
  Davenport--Heilbronn, randomized or planted-zero object.

The smallest admissible next theorem is not another scalar identity.  It would
have to construct, from a single arithmetic parent, a complex Hilbert or
cohomological object whose one canonical operator simultaneously has:

1. a complete domain and self-adjointness or an exact justified substitute;
2. finite-multiplicity discrete spectrum with the intrinsic \(T\log T\) law;
3. a derived rational-prime/von-Mangoldt trace in the same clock; and
4. a global completed-zeta determinant with no extra divisor.

Nothing in the present finite-field model supplies that theorem.  What it does
supply is a source-locked example of where an exact zeta determinant really
lives, and a proof that natural self-adjointness by itself is not enough.
