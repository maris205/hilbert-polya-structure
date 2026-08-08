# HCS-C19: a genus-three period-seven Hénon curve with an oriented time lift

**Date:** 2026-08-08

Status: **generic Hénon seven-cycle and degree-14 time lift proved; Route A exploratory**

This project starts from the area-preserving Hénon recurrence in Paper 5 and
the period-seven chiral formulas of Endler--Gallas.  An adversarial source
audit found that the constant term printed in their Eq. (16) is inconsistent
with one exact orbit fibre.  We record the counterexample, adopt the formula
selected by that fibre, and then certify it generically by an independent
neighbor-correspondence calculation.  The resulting scalar curve has genus
three and admits a degree-14 ordered-edge lift with exact Hénon time.

## Main result

In Hamiltonian coordinates

\[
x_{t+1}=a-x_t^2-x_{t-1},
\]

the published chiral factor is

\[
C_7(\sigma)=\sigma^2-2\sigma-a.
\]

The literal printed constant

\[
-2a^3+6a^2+2a+3(a^3-4a^2+a-2)\sigma
\]

is compared with the adopted candidate block

\[
-2a^3+6a^2+2a+3+(a^3-4a^2+a-2)\sigma.
\]

Over \(\mathbb F_{103}\), at \(a=6,\sigma=26\), the adopted polynomial has
exactly the seven coordinate roots of two reversed Hénon 7-cycles; the
literal printed polynomial has only the unrelated roots 55 and 60.  No
journal erratum is asserted: this is an exact computational diagnosis of an
apparent print error, not an official publisher erratum.

Substituting \(a=\sigma^2-2\sigma\) into the adopted polynomial gives a
septic \(P(\sigma,x)\).  For this explicit characteristic-zero curve we prove

\[
\operatorname{Disc}_x P
=(4\sigma-9)^2Q_6(\sigma)^3,
\]

where

\[
Q_6=64\sigma^6-448\sigma^5+848\sigma^4+80\sigma^3
     -1048\sigma^2+152\sigma-151.
\]

The polynomial \(Q_6\) is irreducible.  Above each of its six roots, the
normalized degree-seven cover has three simple ramification points.  The
point \((\sigma,x)=(9/4,1/4)\) is an ordinary node and becomes two unramified
branches.  Seven further unramified rational branches lie above infinity.
Riemann--Hurwitz therefore gives

\[
2g-2=-14+6\cdot3=4,
\qquad \boxed{g=3}.
\]

The plane-septic check is independent: arithmetic genus 15 minus node
\(\delta=1\) minus total infinity \(\delta=11\) again gives genus 3.

## Generic Hénon reconstruction

Over \(K=\mathbb Q(\sigma)\), reduce the subresultant chain of

\[
P(\sigma,y),\qquad P(\sigma,a-y^2-x)
\]

in \(K[x]/(P)\).  The last nonzero subresultant has degree two.  If it is
\(c_2y^2+c_1y+c_0\), exact reduction gives

\[
c_1=c_2(x^2-a),
\qquad y_1+y_2=a-x^2.
\]

Its discriminant and diagonal value are nonzero, so every generic root has
two distinct nonloop neighbors.  This relation is symmetric.  Geometric
monodromy is transitive on seven roots and preserves connected components;
prime degree therefore forces the simple two-regular graph to be one
seven-cycle.

The ordered edges form a generic degree-14 cover \(\widetilde C\).  With a
state written as current/previous coordinates,

\[
\tau(x,y)=(a-x^2-y,x),
\qquad R(x,y)=(y,x),
\]

and exactly

\[
\tau^7=R^2=1,
\qquad R\tau R=\tau^{-1}.
\]

Thus the adopted septic is generically a genuine exact-period-seven Hénon
coordinate carrier.  The scalar genus-three curve is the generic quotient by
the involution that forgets which neighbor is previous; chronological time
lives on \(\widetilde C\), not on that quotient.

## Finite-field candidate data

Exact affine point counts with the displayed characteristic-zero branch
correction over
\(\mathbb F_{p^r}\), \(r=1,2,3\), give:

| \(p\) | corrected \((\widehat N_1,\widehat N_2,\widehat N_3)\) | candidate numerator \(\widehat L_p(T)\) |
|---:|---:|---|
| 5 | \((9,39,147)\) | \(1+3T+11T^2+31T^3+55T^4+75T^5+125T^6\) |
| 11 | \((19,167,1171)\) | \(1+7T+47T^2+161T^3+517T^4+847T^5+1331T^6\) |
| 13 | \((16,242,2131)\) | \(1+2T+38T^2+51T^3+494T^4+338T^5+2197T^6\) |

All three polynomials are irreducible over \(\mathbb Q\), satisfy the genus-3
reciprocal relation, and pass the numerical Weil-circle check.
An independent finite-field implementation uses explicit polynomial-quotient
fields rather than the producer's `galois` implementation.  It also checks
the predicted \(p=5,r=4\) count directly.

The recorded finite-prime screen supports the expected singularity and branch
pattern at the tested primes, but it is not a simultaneous-normalization or
good-reduction proof.  The rows are therefore point-count-derived candidate
local factors, not yet certified local Hasse--Weil factors of the
characteristic-zero curve, and certainly not evidence for the Riemann
Hypothesis.

## Route-A boundary

The oriented lift repairs the previous chronology obstruction, but it does
not supply the missing Riemann bridge:

- the Hénon period remains fixed at seven, with no cross-period primitive
  enumeration or prime-like clock;
- the six roots of each candidate numerator have no established
  interpretation as time characters on \(\widetilde C\);
- no chronological transfer operator, Riemann divisor, or self-adjoint
  Hilbert--Pólya lift has been constructed.

The updated Route-A tuple is
**(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)** with overall status
**ROUTE_A_EXPLORATORY**.  The next large step is the geometry of
\(\widetilde C\) and the genuine two-clock data
\(\#\operatorname{Fix}(\operatorname{Frob}_p^r\tau^s)\), preserving \(s\)
rather than averaging it away.

## Reproduce

```bash
python -m pip install -r requirements.txt
python code/c19_producer.py --output results
python code/c19_independent_check.py --certificate results/c19_certificate.json \
  --output results/c19_independent_check.json
python code/c19_neighbor_correspondence.py \
  --output results/c19_neighbor_correspondence.json
python code/c19_neighbor_independent_check.py \
  --certificate results/c19_neighbor_correspondence.json \
  --output results/c19_neighbor_independent_check.json
python -m unittest discover -s code -p 'test_c19.py' -v
```

## Project map

- `DERIVATION_PACKAGE.md`: exact curve, branch analysis, genus proof, and
  claim boundary.
- `NEIGHBOR_CORRESPONDENCE.md`: generic seven-cycle and ordered-edge theorem.
- `SOURCE_AUDIT.md`: Paper-5 conjugacy, the Eq. (16) print-error diagnosis,
  and novelty scope.
- `EXPERIMENT_PLAN.md`: frozen symbolic and finite-field protocol.
- `NEXT_PAPER_ROADMAP.md`: gated geometry and equivariant-Frobenius program
  for the oriented cover.
- `code/`: producer, independent checker, and tests.
- `results/`: exact certificates and interpreted tables.
- `paper/`: short manuscript and compiled PDF.
- `evaluations/route_a/hcs_c19/`: formal Route-A ruling.
- `AUTO_REVIEW.md`, `REVIEW_SUMMARY.md`, and `COMPILE_REPORT.md`: final
  adversarial and publication checks.
