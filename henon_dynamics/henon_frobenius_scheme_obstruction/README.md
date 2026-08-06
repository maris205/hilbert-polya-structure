# HCS-C12A: Frobenius collapse for Hénon periodic-point schemes

Date: 2026-08-06  
Status: **complete scoped obstruction; v2 exact certificate independently checked**

This project audits the two-axis proposal

\[
H_a(q,p)=(1-aq^2-p,q),\qquad
N_{a,p}(r,n)=\#\operatorname{Fix}(H_a^n)(\mathbb F_{p^r}),
\]

while keeping Frobenius extension degree \(r\) and chronological Hénon time
\(n\) strictly separate.  The family is exactly the area-preserving recurrence
used in Paper 5; the integer specialization \(a=6\) is an arithmetic test case,
not a fitted critical parameter and not a claim about the numerically selected
parameter in Paper 5.

## Main finding

The originally registered fixed-\(n\) search is a **NO-GO**.  For every
degree-good prime, the periodic-point scheme is zero-dimensional of scheme
length \(2^n\).  After reduction, Frobenius is merely a permutation of a finite
set, so

\[
N_{a,p}(r,n)=\operatorname{Tr}(F_p^r\mid\mathbb Q_\ell[S_{a,p,n}]),
\qquad
Z_{a,p,n}(u)=\det(I-uF_p)^{-1}.
\]

Consequently fixed-\(n\) rationality, a finite recurrence in \(r\), and a
finite trace decomposition are automatic for every zero-dimensional control.
All local eigenvalues are roots of unity and ordinary point counts ignore
nilpotents.  This makes fixed-\(n\) local rationality nondiagnostic: it supplies
no new Hénon-specific divisor or Hilbert--Pólya operator.  It does **not** rule
out nontrivial zeros of the classical global Dedekind/Artin factors; for
example the \(n=1,a=6\) factor is
\(\zeta_{\mathbb Q(\sqrt7)}=\zeta L(\chi_{28})\).

## Surviving information

The ordinary table \(N(r,n)\) is not a complete invariant of a joint
Frobenius/Hénon action, even in the category of reversible finite actions.
The chronology-preserving refinement is the joint character

\[
T_{a,p,n}(r,s)=
\operatorname{Tr}(F_p^rH_a^{-s}\mid\mathbb Q_\ell[S_{a,p,n}]).
\]

This is a sound arithmetic-dynamical object with direct precedent in twisted
equivariant zeta constructions.  The finite control proves information loss
in the structural category; it does not assert that the same ambiguity occurs
in the concrete \(a=6,n=5\) fiber.  Any future novelty must therefore come
from a new exact-period Galois/monodromy theorem, a genuinely joint invariant,
or positive-dimensional parameter geometry—not from local rationality alone.

## Period-five collision

A seemingly promising exact computation at \(a=6,n=5\) recovers a sextic
with Galois group \(S_6\) and a reversor-line marker for the six period-five
orbits.  Endler--Gallas (2006) already published this same scaled \(Z\)
sextic, its discriminant, and the symmetric Galois group; Brison--Gallas
(2018) later published the companion sextics and polynomial bridges.  Our
calculation is retained as an independent reproducibility and chronology
check, not claimed as a new arithmetic result.

## Project map

- `DERIVATION_PACKAGE.md`: assumptions, invariant objects, proofs, and open
  risks.
- `SOURCE_AUDIT.md`: primary-source collision and applicability ledger.
- `EXPERIMENT_PLAN.md`: frozen exact-certificate protocol.
- `AMENDMENT_LOG.md`: transparent v1-to-v2 reversibility correction.
- `code/`: independent producer, checker, and tests.
- `results/`: machine-readable certificates and interpreted results.
- `paper/`: negative-note manuscript material.
- `evaluations/route_a/`: formal Route-A ruling.

No Riemann zero table or prime target table is used anywhere in this project.
