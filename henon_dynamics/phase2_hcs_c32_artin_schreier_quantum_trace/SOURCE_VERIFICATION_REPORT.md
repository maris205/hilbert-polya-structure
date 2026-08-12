# HCS-C32 verified and graded sources report

Date: 2026-08-11 UTC
Verdict: `PHASE2_RECOMMENDS_ONE_EXACT_GATE_PENDING_USER_CHECKPOINT`
Direct duplicate: `NOT_FOUND_WITHIN_SEARCH_BOUNDS`
Generic baseline collision: `CONFIRMED`

## 1. Source-certified local theorem

Let \(p>3\), let \(\ell\ne p\), fix a nontrivial additive character
\(\psi_0:\mathbb F_p\to\overline{\mathbb Q}_\ell^\times\), and set

\[
\psi_r=\psi_0\circ
\operatorname{Tr}_{\mathbb F_{p^r}/\mathbb F_p}.
\]

For

\[
\Phi_n(x_0,\ldots,x_{n-1})
=\sum_{i\bmod n}
\bigl(x_ix_{i+1}-x_i+2x_i^3\bigr),
\]

the highest homogeneous part is

\[
(\Phi_n)_3=2\sum_iX_i^3,
\qquad
\partial_{X_i}(\Phi_n)_3=6X_i^2.
\]

The derivatives have no common projective zero for \(p>3\). Deligne's
Theorem 8.4 and Lemma 8.5 therefore apply to

\[
V_{n,p}=H_c^n\!\left(
\mathbb A^n_{\overline{\mathbb F}_p},
\Phi_n^*\mathcal L_{\psi_0}
\right).
\]

With the frozen geometric-Frobenius convention,

\[
H_c^i=0\quad(i\ne n),
\qquad
\dim V_{n,p}=2^n,
\]

and

\[
E_{p,n}(r):=
\sum_{x\in\mathbb F_{p^r}^n}\psi_r(\Phi_n(x))
=(-1)^n\operatorname{Tr}
\left(\operatorname{Fr}_p^r\mid V_{n,p}\right).
\]

Every Frobenius eigenvalue has complex absolute value \(p^{n/2}\). Purity is
obtained from Deligne's p. 304 injection into smooth-projective \(H^n\) and
Theorem 1.6, rather than being quoted as the literal text of Lemma 8.5.

If

\[
(U_r f)(Q)=p^{-r/2}
\sum_{q\in\mathbb F_{p^r}}
\psi_r(S_6(q,Q))f(q),
\]

then elementary finite Fourier orthogonality makes \(U_r\) unitary, while
direct expansion of chronological powers gives

\[
\operatorname{Tr}(U_r^n)=p^{-rn/2}E_{p,n}(r).
\]

Thus there are two exact axes:

- fixed \(p^r\), varying \(n\): powers of one \(p^r\)-dimensional unitary;
- fixed \((p,n)\), varying \(r\): Frobenius powers on one
  \(2^n\)-dimensional cohomology group.

This two-axis identity is correct but generic at its cohomological layer.

## 2. Fixed raw kernel and chronology

On \(X=\mathbb A^1_{\mathbb F_p}\), define the unshifted raw kernel

\[
K_p=\mathcal L_{\psi_0(S_6)}
\quad\text{on }X\times X.
\]

Compose kernels by the usual correspondence rule using tensor product and
compactly supported pushforward. Laumon's formulas 1.1.1.2–1.1.1.3 then give
at the trace-function level

\[
t_{K_p^{\circ n}}(x_0,x_n)
=
\sum_{x_1,\ldots,x_{n-1}}
\prod_{i=0}^{n-1}
\psi_r(S_6(x_i,x_{i+1})).
\]

Diagonal summation yields \(E_{p,n}(r)\). This preserves genuine
chronology; no transition-matrix average is used.

The safe name for

\[
R\Gamma_c\!\left(X,\Delta^*K_p^{\circ n}\right)
\]

is the **compactly supported diagonal trace complex of the \(n\)-fold
!‑composed raw Artin--Schreier kernel**. It is not called an unqualified
categorical trace, because that stronger term requires an ambient dualizable
category, kernel-to-functor convention, evaluation/dualizing data, and a
choice between \(\Delta^*\) and \(\Delta^!\).

## 3. Mandatory convention firewalls

1. **Sign.** The factor \((-1)^n\) in the Frobenius trace is mandatory.
2. **Parity.** The normalized local series is
   \[
   \exp\!\left(\sum_{r\ge1}
   p^{-rn/2}E_{p,n}(r)\frac{z^r}{r}\right)
   =
   \det(1-zp^{-n/2}\operatorname{Fr}_p\mid V_{n,p})^{(-1)^{n+1}}.
   \]
   It is a determinant for odd \(n\) and a reciprocal determinant for even
   \(n\).
3. **No canonical half twist.** For odd \(n\), \(p^{-n/2}\) is an analytic
   normalization after choosing an embedding/square root, not a canonical
   integral Tate twist.
4. **Duality.** Deligne pairs \(V_{n,\psi}\) with
   \(V_{n,\psi^{-1}}\), not generally with itself.
5. **No Hilbert inference.** Purity supplies unit-modulus normalized
   eigenvalues; it does not supply a canonical positive Hermitian form,
   self-adjoint operator, semisimplicity, or a Riemann-zeta functional
   equation.
6. **Full-cover warning.** The \(2^n\)-dimensional group is one nontrivial
   Artin--Schreier isotypic summand, not the entire cover
   \(y^p-y=\Phi_n\).
7. **Shift warning.** A perverse shift \([1]\) changes trace-function signs;
   the raw kernel convention must remain frozen.
8. **Gauge.** Replacing
   \(S(q,Q)\) by \(S(q,Q)+G(Q)-G(q)+C\) produces conjugacy plus a common
   scalar phase. The fixed-\(z\) spectrum is not intrinsically normalized by
   classical dynamics alone.

## 4. Claim-by-claim evidence matrix

| Claim | Status | Source grade | Ruling |
|---|---|---|---|
| Smooth top cubic gives concentration and rank \(2^n\) | VERIFIED | A | Deligne 8.4 and 8.5; generic, not novel |
| Purity of weight \(n\) | VERIFIED, DERIVED | A | Deligne p. 304 plus Theorem 1.6 |
| Extension degree \(r\) is Frobenius power with \(\psi_r=\psi_0\circ\mathrm{Tr}\) | VERIFIED | A | SGA 4 1/2, §§1.7 and 1.9 |
| Mandatory \((-1)^n\) | VERIFIED | A | alternating trace plus concentration |
| \(\psi\)-summand self-pairs | REJECTED GENERICALLY | A | pairing is \(\psi\leftrightarrow\psi^{-1}\) |
| Chronological raw-kernel powers | VERIFIED AT SIX-FUNCTOR/FUNCTION LEVEL | A | Laumon tensor and \(Rf_!\) rules |
| Raw diagonal complex is automatically a categorical trace | NOT VERIFIED | A boundary | extra categorical data required |
| Numerical rank equals total critical multiplicity | VERIFIED; GENERIC FRAMEWORK IS PRIOR ART | A | Deligne and C12A verify the number; Adolphson--Sperber give a Milnor-number framework under stated hypotheses; a canonical orbitwise decomposition is NOT VERIFIED |
| Hénon Hessian equals multiplier determinant | VERIFIED SPECIALIZATION, GENERIC THEOREM | A | Bolotin--Treschev plus exact local derivation |
| Vanishing cycles of separated sums use local convolution in characteristic \(p\) | VERIFIED GENERICALLY | A | Fu 2014; Illusie 2017 |
| First quantized Hénon map | PRIOR-WORK COLLISION | A | Fornæss--Weickert 2000 |
| First finite-field Hénon dynamics | PRIOR-WORK COLLISION | A | Roberts--Vivaldi 2005/2009 |
| First finite-field nonlinear Hénon Artin--Schreier kernel | NOT FOUND WITHIN SEARCH BOUNDS | search-limited | absence is not proof of novelty |
| Critical-value/Hill-controlled vanishing-cycle factors | OPEN | partial sources only | this is the only remaining big door |
| Hilbert--Pólya operator | NOT ESTABLISHED | none | prohibited inference |

## 5. What is generic and what could still be new

The following package is mathematically valid but not publishably new by
itself:

\[
\boxed{
\text{Fourier--cubic unitary}
+\text{Deligne rank/purity}
+\text{kernel Fubini}
+\text{Hill determinant}.}
\]

The missing nonformal statement would have to resolve more than the dimension
of the cohomology. It would need to expose how Frobenius acts on pieces tied to
the actual Hénon critical values and how the local quadratic/vanishing-cycle
factor records

\[
\det D^2\Phi_n
=(-1)^{n+1}\det(I-DH_6^n).
\]

No audited source supplies this complete specialization.

## 6. Candidate Phase-3 gate, not yet authorized

One candidate gate remains: test whether critical-value vanishing-cycle data
detects the Hénon Hill multiplier beyond the universal Morse factor.  Under
Laumon's shifted convention the precise comparison is

\[
\mathcal F_\psi\!\left(R\Phi_{n,!}\overline{\mathbb Q}_\ell\right)_t
\simeq
R\Gamma_c\!\left(\mathbb A^n,
\mathcal L_{\psi(t\Phi_n)}\right)[1],
\]

so its trace function is \(-E_{p,n}(r;t)\); the unshifted raw Fourier integral,
not this shifted transform, has trace function \(E_{p,n}(r;t)\).  Any later
test must verify the exact stationary-phase hypotheses and the contribution at
infinity.  It must also distinguish a genuinely multiplier-sensitive invariant
from the local quadratic factor, which generically records only a Hessian
square class/Weil index.  This gate is a Phase-2 recommendation only and is not
authorized until the user checkpoint is cleared.

## 7. Provisional informal Route-A ceiling

No formal Route-A evaluator was invoked in Phase 2.  The formal status is
`NOT_TESTABLE`: the clock, global normalization, determinant target, and
reproducible experiment artifacts required by the evaluator are not yet
locked.  The following tuple is only an informal upper ceiling:

\[
(A1\_WEAK,\ A2\_FAIL,\ A3\_FAIL,\ A4\_FORMAL\_HINT),
\qquad
\text{informal outcome ceiling: rejected}.
\]

- A1 is weak because critical points are genuine chronological Hénon
  periodic points, but no prime law or von-Mangoldt correspondence exists.
- A2 fails because the current finite \((p,n)\) determinants do not assemble
  into a canonical global analytic determinant.
- A3 fails because purity is a generic finite-field theorem and no critical
  line for the Riemann zeta function is obtained.
- A4 is only a formal hint: \(U_r\) is genuinely unitary, but its dimension
  varies with \(r\), the cohomology varies with \(n\), and no single
  self-adjoint Hilbert--Pólya operator is present.

Route B is not authorized.

## 8. Phase-2 checkpoint recommendation

\[
\boxed{
\texttt{RECOMMEND\_ONE\_EXACT\_GATE\_PENDING\_USER\_AUTHORIZATION}}
\]

This is not a positive-construction claim and does not start Phase 3.  It means
only that the generic baseline has been separated from one sharply defined,
Hénon-specific unresolved gate.  If the user authorizes Phase 3 and that gate
does not clear, C32 should stop immediately and pivot to a different Hénon
deformation or to the previously identified Livšic-quotient action question.
