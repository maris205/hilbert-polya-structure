# Stage 6 Source Audit — Frobenius, Koopman, and Operator Ownership

Audit date: **2026-08-13**  
Candidate: `FF-FROB-OPERATOR-OWNERSHIP-P1-F2`  
Scope: exact source lock for the final paper in the five-paper batch  
Source policy: primary sources for arithmetic identities; an author-hosted
research text for standard unbounded-operator facts; no formula is accepted
from a search snippet alone

## 1. Source-audit conclusion

The source record supports a strict, typed split.

1. Deligne's formula gives the exact owner of the native zeta determinant:
   finite-dimensional Frobenius actions on graded compactly supported etale
   cohomology.  For \(\mathbb P^1/\mathbb F_2\), the two nonzero groups have
   Frobenius eigenvalues \(1\) and \(2\), so the graded determinant is exactly
   \(1/((1-t)(1-2t))\).
2. Koopman's construction supplies the natural unitary representation of a
   measure-preserving flow.  Stone's theorem and direct-sum spectral theory
   validate the self-adjoint generator used in Stage 5 and this paper.
3. None of these sources identifies the etale Frobenius action with the
   periodic-circle differential generator.  Equality of the scalar orbit zeta
   and the cohomological determinant does not turn the latter into a Koopman,
   transfer, heat or zeta-regularized determinant.

This is enough to prove an operator-ownership theorem and to close the limited
Route-B audit at B3.  It is not a general theorem that cohomology can never
produce a Hilbert--Polya operator.

## 2. Acquisition and integrity record

The core sources were acquired from official archives or author-maintained
copies.  PDF physical pages are used below when they differ from printed page
numbers.

| Key | Source and verified locator | Local manifestation and SHA-256 | Role | Boundary |
|---|---|---|---|---|
| `DEL74` | Pierre Deligne, [“La conjecture de Weil I,” *Publications Mathématiques de l'IHÉS* 43 (1974), 273--307](https://numdam.org/articles/10.1007/BF02684373/), DOI `10.1007/BF02684373`; §§1.1--1.6, printed pp. 273--276 | `notes/sources/deligne-weil-i.pdf`, 36 physical pages, `8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5` | closed-point product, point Frobenius cycles, fixed-point trace, formal determinant, rationality/weights | determinant acts on etale cohomology; no complex suspension Hilbert space is asserted |
| `KOO31` | B. O. Koopman, [“Hamiltonian Systems and Transformations in Hilbert Space,” *PNAS* 17(5) (1931), 315--318](https://doi.org/10.1073/pnas.17.5.315), DOI `10.1073/pnas.17.5.315`; pp. 315--318 | university-hosted scan `notes/sources/koopman-1931.pdf`, 4 pages, `1e8042406f9e450c288573536a423c727bd1237083324545f188966b6ebee767` | invariant-measure Hilbert space and unitary composition group | historical Hamiltonian setting; our disjoint-circle model is proved directly |
| `STO32` | M. H. Stone, “On One-Parameter Unitary Groups in Hilbert Space,” *Annals of Mathematics* 33 (1932), 643--648, DOI [`10.2307/1968538`](https://doi.org/10.2307/1968538) | metadata checked through the DOI/journal record; no local full PDF required because the theorem is also checked in `TES09` | one-parameter unitary group/self-adjoint-generator correspondence | does not imply compact resolvent or trace class |
| `TES09` | Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/), GSM 99, AMS, 2009; Theorem 2.23, printed pp. 79--80; Theorems 5.1--5.2, pp. 123--125; §6.4, pp. 145--147 | author-hosted first edition `notes/sources/teschl-mathematical-methods-qm.pdf`, 317 physical pages, `8dc8de0b58aa0a3fedfe594a345f9b5875322e5526ea581cb640a98d55b82818`; title page records GSM 99, ISBN 978-0-8218-4660-5, and version 12 February 2009 | countable orthogonal sums, Stone theorem, spectrum closure and essential-spectrum criterion | general functional analysis only; arithmetic conclusions are proved here |
| `STACKS-TRACE` | [Stacks Project, Chapter “The Trace Formula,” Tag 03SJ](https://stacks.math.columbia.edu/tag/03SJ), especially §64.2 | `notes/sources/stacks-trace.pdf`, 45 pages, `99d5358fe636cb18afa5a81f93c7906995db2a02a15efd742ba90e07cb74c828` | authoritative convention check for Frobenius trace in dimension one | living reference/supporting exposition, not substituted for `DEL74` |
| `TEL` | A. F. M. ter Elst and M. Lemańczyk, “On one-parameter Koopman groups,” theorem and generator discussion in the locally acquired author/journal PDF | `notes/sources/ter-elst-lemanczyk-koopman-groups.pdf`, `9dcf83e9318360ed5211ef4844f224973d15213f907e2e891512c4ddfebb1a56` | modern check that Koopman groups and their generators require explicit measure/action hypotheses | not needed for the exact circle spectrum, which is diagonalized directly |

The official PNAS PDF endpoint returned HTTP 403 on the audit date.  The
university-hosted four-page scan was checked against DOI metadata and the
printed title, author, volume and pages.  This access fact is disclosed rather
than silently treating a mirror as the publisher manifestation.

No source contains Riemann-zero data, a fitted parameter or a proposed
identification of the two frozen operators.

## 3. Deligne source lock

### 3.1 Closed points and the native variable

`DEL74`, §1.1 (physical PDF p. 2, printed p. 273), defines the Hasse--Weil
closed-point product and then introduces \(t=q^{-s}\) for a variety over
\(\mathbb F_q\):

\[
 Z(X,t)=\prod_{x\in|X|}(1-t^{\deg x})^{-1}.
\]

This is the source of the native determinant variable.  The later vertical
lattices in the \(s\)-plane arise from the many-to-one exponential map
\(t=2^{-s}\); they are not a larger Frobenius spectrum.

### 3.2 Point-cycle dictionary

`DEL74`, §1.4 (physical PDF pp. 3--4, printed pp. 274--275), fixes a
Frobenius endomorphism \(F\), identifies \(F^n\)-fixed points with
\(X_0(\mathbb F_{q^n})\), identifies closed points of \(X_0\) with
Frobenius orbits on geometric points, and gives

\[
 \#X_0(\mathbb F_{q^n})
 =\sum_{\substack{x\in|X_0|\\\deg x\mid n}}\deg x.
\]

Stage 4 proves directly that suspending this discrete permutation with roof
\(\log q\) turns precisely these cycles into the primitive flow circles.
The topology of that suspension is a disclosed modeling choice; it is not an
etale-topology theorem in Deligne.

### 3.3 Lefschetz trace and determinant

`DEL74`, equations (1.5.1)--(1.5.4) (physical PDF pp. 4--5, printed pp.
275--276), gives

\[
 \#X_0(\mathbb F_{q^n})
 =\sum_i(-1)^i\operatorname{Tr}
   (F^{*n}\mid H_c^i(X,\mathbb Q_\ell))
\]

and

\[
 Z(X_0,t)=\prod_i
 \det(1-tF^*\mid H_c^i(X,\mathbb Q_\ell))^{(-1)^{i+1}}.
\]

The proof proceeds through logarithmic differentiation and the formal identity

\[
 -\frac d{dt}\log\det(1-tT)
 =\sum_{n\ge1}\operatorname{Tr}(T^n)t^{n-1}.
\]

This exactly derives the \(1/n\) repetitions.  For
\(\mathbb P^1/\mathbb F_2\), elementary cohomology or comparison with every
point count gives one eigenvalue \(1\) in degree zero, no degree-one term and
one eigenvalue \(2\) in degree two.  Hence

\[
 Z(\mathbb P^1,t)=\frac1{(1-t)(1-2t)}.
\]

The notation `F*` in the manuscript will be tied to Deligne's displayed
formula rather than casually relabeled “arithmetic” or “geometric”
Frobenius.  On the point-permutation side, inversion reverses each finite
cycle and leaves its length unchanged.  This avoids a convention error while
preserving every claim used here.

### 3.4 What the source does not supply

The cohomology groups are finite-dimensional \(\mathbb Q_\ell\)-vector
spaces.  `DEL74` does not furnish:

- a canonical embedding into a complex Hilbert space;
- a positive-definite complex inner product making \(F^*\) a Hamiltonian;
- a logarithm branch turning its eigenvalues into real energies;
- a unitary equivalence with the suspension Koopman group;
- a compact-resolvent self-adjoint operator with Riemann--von Mangoldt growth;
- a determinant equal to completed \(\xi\).

For this two-eigenvalue example one can of course copy \(1,2\) into a complex
diagonal matrix and choose an inner product.  That is an external realization,
not a source-derived Hilbert--Polya construction, and it proves too little.

## 4. Koopman and Stone source lock

### 4.1 Natural Hilbert representation

`KOO31`, printed pp. 315--317, starts from an invariant positive measure,
forms the corresponding \(L^2\) Hilbert space and represents the flow by
composition operators.  Measure invariance makes the group unitary.  This is
the exact structural role used here.

For the frozen suspension the measure and all operators are more elementary:
each circle receives a positive constant multiple of Lebesgue measure, and
translation preserves it.  Strong continuity and the Fourier action are
proved directly, so no smooth Hamiltonian hypothesis from the historical
paper is imported.

### 4.2 Complete generator and direct sum

`TES09`, Theorems 5.1--5.2, gives the unitary-group/self-adjoint-generator
correspondence.  Theorem 2.23 states that the countable orthogonal sum of
self-adjoint operators, on the square-summable graph domain, is self-adjoint
and has spectrum equal to the closure of the union of component spectra.

For a degree-\(d\) circle of length \(d\log2\), periodic Fourier analysis gives

\[
 \sigma(A_d)=\left\{\frac{2\pi n}{d\log2}:n\in\mathbb Z\right\}.
\]

The cited theorem therefore applies exactly to the domain frozen in
`research_protocol.md`.  No boundary condition is selected after looking at a
target spectrum: periodicity is forced by the circle quotient.

### 4.3 Essential spectrum and trace-class boundary

`TES09`, §6.4, characterizes the essential spectrum of a self-adjoint
operator through infinite-rank spectral projections in every neighborhood.
In the frozen model, every rational-scaled frequency is itself an
infinite-multiplicity eigenvalue and such frequencies are dense.  Therefore
every nonempty open interval has infinite-rank spectral projection, proving
\(\sigma_{\rm ess}(A_K)=\mathbb R\).

The failure of compact resolvent and heat trace class requires no delicate
external theorem.  The zero mode is present once on every primitive-orbit
circle, hence \(\ker A_K\) is infinite-dimensional.  The resolvent acts by one
fixed nonzero scalar on that subspace, so it is not compact.  Similarly,
\(e^{-tA_K^2}\) acts as the identity there, so it is not trace class for
\(t>0\).

## 5. Claim-to-source matrix

| Claim ID | Claim | Evidence | Exact status |
|---|---|---|---|
| `S1` | closed points equal primitive Frobenius cycles | `DEL74` §1.4 plus Stage-4 direct suspension proof | `PROVED` |
| `S2` | point count equals graded Frobenius trace | `DEL74` (1.5.1) | `PROVED` |
| `S3` | native zeta equals graded Frobenius determinant | `DEL74` (1.5.4) | `PROVED` |
| `S4` | Koopman translation is a natural unitary group | `KOO31`; direct circle proof | `PROVED` |
| `S5` | direct-sum periodic derivative is self-adjoint | `TES09` Thm. 2.23 and Fourier proof | `PROVED` |
| `S6` | direct-sum spectrum is the closure of component spectra | `TES09` Thm. 2.23 | `PROVED` |
| `S7` | essential spectrum is detected by infinite-rank local projections | `TES09` §6.4 | `PROVED` |
| `S8` | Frobenius determinant is a spectral determinant of \(A_K\) | no source theorem; spectra and data types differ | `REFUTED` for the frozen equality |
| `S9` | a future source-defined bridge is impossible | not established | `OPEN`; forbidden wording |
| `S10` | either operator realizes completed Riemann \(\xi\) | wrong clock/divisor/spectral type | `REFUTED` for frozen objects |

## 6. Excluded inferences

The following inferences are source-inadmissible and will be rejected in peer
review:

1. “Unitary” implies compact resolvent or discrete finite-multiplicity
   spectrum.
2. A pure Fourier eigenbasis implies that the set-theoretic spectrum is only
   the eigenvalue set; the dense closure must be included.
3. A scalar Euler-product identity identifies every operator used to derive
   either side.
4. A finite-dimensional \(\ell\)-adic determinant is automatically a
   zeta-regularized determinant of a complex self-adjoint generator.
5. The substitution \(t=2^{-s}\) turns two Frobenius eigenvalues into a new
   physical energy spectrum.
6. Native finite-field Riemann-hypothesis/weight statements promote a
   characteristic-two model to the rational-prime Hilbert--Polya problem.
7. B2 from Koopman and B4 from etale cohomology can be recorded as one Route-B
   tuple without an operator-level bridge.

## 7. Search and stopping log

Search proceeded only far enough to lock the four required interfaces:
Frobenius orbit/trace/determinant, Koopman unitary representation, Stone
self-adjointness, and countable direct-sum spectral type.  Deligne and Teschl
already state the exact theorems needed, and the remaining candidate-specific
claims admit elementary proofs.  Additional surveys were excluded to avoid
reference inflation.

The search stopped without finding a source-defined unitary equivalence or
trace bridge between the two frozen operators.  Absence from this finite
search is not used as proof; the negative theorem instead compares their
explicit spectra, domains and determinant data types.
