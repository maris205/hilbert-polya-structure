# Repository update

Date: 2026-08-06  
Generation: **HCS-2026-08-06/C12A--C12B closure**  
State: **ready for repository handoff; workspace has no Git metadata**

## Decision

Close the registered fixed-period Frobenius-rationality mechanism as

\[
\boxed{\texttt{C12A\_NO\_GO\_ZERO\_DIMENSIONAL\_FROBENIUS\_COLLAPSE}}.
\]

Separately close the \(a=6,n=5\) novelty reframe as

\[
\boxed{\texttt{C12B\_N5\_PRIOR\_WORK\_COLLISION}}.
\]

The Route-A tuple is
\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}),
\]
with overall ROUTE_A_REJECTED for this registered mechanism.  Route B is not
authorized.

## Added

- a scheme-level cyclic presentation of
  \(\operatorname{Fix}(H_A^n)\) over \(\mathbb Z[A,A^{-1}]\);
- a monic Gröbner proof of finite flatness with rank \(2^n\);
- exact \(n=1,2\) ideal regressions, normalized Jacobian norms, and a generic
  period-two CRT splitting certificate;
- a strict distinction among degree-good fibers, étale fibers, reduced
  support, scheme length, and local-length-weighted controls;
- a general proof that every finite fixed-\(n\) local factor is the
  nilpotent-blind determinant of a finite Frobenius permutation;
- a chronology-preserving joint trace
  \(T(r,s)=\operatorname{Tr}(F^rH^{-s})\), together with a reversible
  ten-point control proving that ordinary rectangular traces are incomplete;
- a transparent frozen-protocol v2 amendment after the original one-cycle
  control failed the reversor commutation constraint;
- 36 exact low-period cells, an explicit finite-field checker, eight tests,
  complete schema/hash guards, and a period-five modular \(S_6\) certificate;
- a primary-source audit identifying Walton's direct twisted-count precedent
  and the decisive Endler--Gallas 2006 period-five collision;
- a formal Route-A evaluation, a compiled nine-page negative note, and a
  next-candidate registry update.

## Scoped mathematical conclusion

At fixed chronological \(n\), a finite periodic-point fiber has only
zero-dimensional \(H_c^0\).  Its Frobenius eigenvalues are roots of unity, so
local rationality, recurrence in extension degree, and finite trace
reconstruction are universal controls rather than Hénon-specific evidence.
Ordinary rational points also ignore nilpotents.

This does **not** prove that global zeta functions have no nontrivial zeros.
For example,
\[
\zeta_{\mathbb Q(\sqrt7)}(s)=\zeta(s)L(s,\chi_{28})
\]
already occurs at \(a=6,n=1\).  Such classical Dedekind/Artin factors are
arithmetically valid but do not supply a new Hénon-derived Riemann divisor or
Hilbert--Pólya operator.

## Prior-work boundary

The independently recovered sextic
\[
Z(x)=x^6+2x^5-16x^4-22x^3+85x^2+60x-151
\]
and its \(S_6\) Galois group are already in Endler--Gallas (2006).  The
certificate's nonmonic marker is \(Z(6q)\), and
\[
\operatorname{Disc}(Z(6q))
=6^{30}\operatorname{Disc}(Z)
=2^{36}3^{30}\cdot31\cdot241\cdot389.
\]
Brison--Gallas (2018) later gives the companion sextics and polynomial
bridges.  None of these low-period arithmetic facts is claimed as new.

## Verification

All final checks pass:

- Python syntax compilation: passed;
- unit tests: 8/8;
- certificate cells: 36/36 independently reproduced;
- finite-field ledgers: 16/16 verified as fields;
- exact \(H_0^4\) degree-drop controls: passed;
- full JSON metadata/schema and canonical CSV comparison: passed;
- frozen plan/protocol/producer hashes: passed;
- independent period-five recurrence and frozen constants: passed;
- enumerated reversible relations and joint-trace separation: passed;
- independent checker result: all_pass = true;
- final code referee audit: PASS;
- PDF compilation: 9 pages, zero undefined citations/references, zero box
  warnings, all fonts embedded.

Key SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| DERIVATION_PACKAGE.md | f524678196be667f0861c8cf64cb2f847824e3604bc356d6e59ca3188bdc6dfb |
| SOURCE_AUDIT.md | f7653c951703d9de13493fa86b438044b17b2befd51b0daa8026265c9bd81b41 |
| evaluations/route_a/evaluation.yaml | dc98f0a8d9760660c99559d224ecc2aa821013a8505283d2aebb5faf663e58a9 |
| code/c12a_producer.py | 0e1c64ed3554a1625c9b720075b815a0b6e09152ab316fb7f2f76eb65f31263d |
| code/c12a_checker.py | 47a01350e87394286a123ec5a21a704556c6a73cf80b0891b6fb64570497c0da |
| results/c12a_certificate.json | 851ca31f62fb508ad806c26084eab9fe092d5ee037bf99f0cb811cbccf7f8eb8 |
| results/c12a_independent_check.json | 4784e8b2fbf98ad835a5f1c0ef9217de14537adcff486046e74a6b0f47e93778 |
| paper/main.pdf | e36ed99e10376af03548b489ff70eba222b5dcc5d7c64f9633b5d82c9de79f35 |

## Next authorized work

Return to breadth-first source locking.  Provisional HCS-C12C keeps the
parameter \(A\) alive and studies a canonical exact-period quotient curve
\[
\mathcal P_n/\langle H_A,R\rangle
\]
rather than another fixed-\(a\), fixed-\(n\) point scan.  The only authorized
next step is a primary-source/equivalence audit of Hénon dynatomic curves,
orbital polynomials, reversor quotients, compactifications, and arithmetic
monodromy.  No genus computation, Euler product, or RH promotion should begin
until the quotient is canonical and its novelty survives that audit.

## Not done

- no target-zero, prime-gap, or Euler-factor fitting;
- no diagonal identification \(r=n\);
- no averaged transition matrix replacing chronological dynamics;
- no claim that classical global Artin zeros are absent;
- no new transfer operator, self-adjoint realization, or Hilbert--Pólya
  construction;
- no Route-B evaluation;
- no Git commit, because this workspace is not a Git worktree.
