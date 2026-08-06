# HCS-C12A exact-certificate results

Date: 2026-08-06  
Status: **complete; independent checker passed**

## Decision

\[
\boxed{\texttt{C12A\_NO\_GO\_ZERO\_DIMENSIONAL\_FROBENIUS\_COLLAPSE}}
\]

The period-five reframe separately receives

\[
\boxed{\texttt{C12B\_N5\_PRIOR\_WORK\_COLLISION}}.
\]

## Symbolic theorem regression

Every frozen exact identity passed:

\[
D_{a,1}=-4(a+1),\qquad
D_{a,2}=2^8(a+1)(a-3)^3.
\]

The \(n=1,2\) iterate ideals agree exactly with their cyclic presentations.
The fixed and primitive period-two parameterizations have zero residual, the
branch ideals are comaximal over \(\mathbb Q(A)\), the difference
factorization passes, and the cyclic quotient has the expected \(2^n\)
standard-monomial count.  The splitting is generic: the two branches collide
at \(A=3\).

These samples support the implementation.  The finite-flat rank theorem is
proved in `../DERIVATION_PACKAGE.md`; it is not inferred from the samples.

## Low-period arithmetic firewall

The certificate contains 36 cells.  Direct enumeration in an independently
implemented \(\mathbb F_{p^r}\) reproduced every support count, rational
singular-support count, and defined multiplicity-weighted count.

| prime | status | \(N(r,1)\), \(r=1,\ldots,4\) | \(N(r,2)\), \(r=1,\ldots,4\) |
|---:|---|---|---|
| 5 | étale-good | 0, 2, 0, 2 | 0, 4, 0, 4 |
| 11 | étale-good | 0, 2, 0, 2 | 2, 4, 2, 4 |
| 7 | nonreduced | 1, 1, 1, 1 | 1, 3, 1, 3 |
| 3 | degree-drop | 1, 1, 1, 1 | 1, 1, 1, 1 |

Here the nonstandard multiplicity-weighted statistic is the sum of geometric
local Artin lengths over support points rational over \(\mathbb F_{p^r}\).
At \(p=7\), its rows are \((2,2,2,2)\) for \(n=1\)
and \((2,4,2,4)\) for \(n=2\).  The ordinary rows remain smaller because
field-valued points see only the reduced support.

At \(p=3\), direct reduction of the original uninverted family makes the
quadratic coefficient vanish.  This is not a fiber of the finite-flat family
over \(\mathbb Z[A,A^{-1}]\).  The direct counts for \(n=4\) are

\[
9,81,729,6561,
\]

because \(H_0^4=I\) and the fixed scheme is all of
\(\mathbb A^2(\mathbb F_{3^r})\).  This cell demonstrates a degree collapse,
not a large periodic-point anomaly.

## Rectangular-count information loss

On two five-cycles exchanged by the reversor, the matched actions
\(F_c(\varepsilon,i)=(\varepsilon,i+\varepsilon c)\), \(c=1,2\), commute
with both \(H\) and \(R\) and have the same ordinary trace sequence through
the frozen range:

\[
(0,0,0,0,10,0,0,0,0,10).
\]

Their joint characters differ already at \((r,s)=(1,1)\):

\[
\operatorname{Tr}(F_1H^{-1})=5,
\qquad
\operatorname{Tr}(F_2H^{-1})=0.
\]

Thus \(N(r,n)=T(r,0;n)\) is not a complete invariant of a joint action, even
among reversible finite actions.  This control does not claim that the same
ambiguity occurs inside the concrete \(a=6,n=5\) fiber.

## Period-five exact collision

The generic reversor-line marker specializes at \(a=6\) to

\[
46656q^6+15552q^5-20736q^4-4752q^3+3060q^2+360q-151.
\]

Its discriminant is

\[
2^{36}3^{30}\cdot31\cdot241\cdot389.
\]

At the unramified primes \(37,5,157\), the modular factor degrees are

\[
[6],\qquad[5,1],\qquad[2,1,1,1,1].
\]

They certify transitivity, a 5-cycle, and a transposition.  The 5-cycle rules
out every nontrivial block system in degree six, and conjugates of the
transposition then generate \(S_6\).  This exact certificate passes.

However, substituting \(x=6q\) gives

\[
x^6+2x^5-16x^4-22x^3+85x^2+60x-151,
\]

Endler--Gallas (2006) already published this \(Z(x)\), its discriminant
\(2^6\cdot31\cdot241\cdot389\), and its symmetric Galois group.  The
identity
\[
\operatorname{Disc}(Z(6q))=6^{30}\operatorname{Disc}(Z)
\]
explains the powers \(2^{36}3^{30}\) above.  Brison--Gallas (2018) later
records the companion sextics and polynomial bridges.  The apparent positive
signal is therefore a reproducible prior-work collision no later than 2006.

## Verification

- unit tests: 8/8 passed;
- independent count cells: 36/36 passed;
- frozen finite-field quotient ledgers: 16/16 fields passed the direct
  all-nonzero-elements-are-units check;
- period-five independent recurrence derivation: passed;
- joint-action expected-fail control: passed.

Artifact hashes:

| artifact | SHA-256 |
|---|---|
| `c12a_certificate.json` | `851ca31f62fb508ad806c26084eab9fe092d5ee037bf99f0cb811cbccf7f8eb8` |
| `c12a_low_period_counts.csv` | `d07d9558dd9036507b89699452edc1494bea2faca8344d5ce6cf2d031f9bc480` |
| `c12a_independent_check.json` | `4784e8b2fbf98ad835a5f1c0ef9217de14537adcff486046e74a6b0f47e93778` |
| producer | `0e1c64ed3554a1625c9b720075b815a0b6e09152ab316fb7f2f76eb65f31263d` |
| checker | `47a01350e87394286a123ec5a21a704556c6a73cf80b0891b6fb64570497c0da` |
| frozen protocol | `fa88bd1003a62b8025922aec72314af452e0f8e48f18184ac35ef7697fce1e31` |
| frozen experiment plan | `f02d1ef77682c0ae54266cafbf0650ade4b928d38c1366168e3db83dba409bf9` |

## Reproduction

From the repository root:

```bash
python henon_frobenius_scheme_obstruction/code/test_c12a.py
python henon_frobenius_scheme_obstruction/code/c12a_producer.py
python henon_frobenius_scheme_obstruction/code/c12a_checker.py
```

## Scope of the negative result

The result kills fixed-\(n\) recurrence discovery and local cyclotomic factors
as distinctive Route-A anomaly signals.  It does not preclude nontrivial
global zeros: finite algebras globalize to classical Dedekind/Artin factors,
and the \(a=6,n=1\) factor already contains
\(\zeta_{\mathbb Q(\sqrt7)}=\zeta L(\chi_{28})\).  That inherited factor is
universal arithmetic contamination, not a new Hénon-derived encoding.  The
result also does not prove that every higher-period Galois tower is trivial or
rule out positive-dimensional parameter curves with nontrivial cohomology.
Those are new candidates requiring new source locks.
