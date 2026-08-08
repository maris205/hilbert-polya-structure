# HCS-C19 adversarial review record

**Review date:** 2026-08-08

**Review type:** three independent internal adversarial audits covering the
mathematics, the implementation, and Route-A scope

**Initial verdict:** major revision; the scalar genus computation was
promising, but the dynamical provenance and finite-prime interpretation were
not yet strong enough

**Post-revision disposition:** no remaining critical or major issue within the
stated claim boundary

## Claims independently checked

The final audits checked or recomputed:

- the exact finite-field counterexample to the literal constant term printed
  in Eq. (16), without promoting it to a publisher-issued erratum;
- the quotient-field subresultant chain for the adopted septic, including the
  degree-two last nonzero member and the identity
  \(c_1=c_2(x^2-a)\);
- nonvanishing of the neighbor discriminant and diagonal value;
- the graph-theoretic passage from a symmetric simple two-regular relation on
  seven roots to one seven-cycle;
- the formulas
  \(\tau(x,y)=(a-x^2-y,x)\), \(R(x,y)=(y,x)\),
  \(\tau^7=1\), and \(R\tau R=\tau^{-1}\);
- the scalar discriminant factorization, ramification ledger, node and
  infinity corrections, and the two genus-three calculations;
- the independent finite-field point-count implementation and the sealed
  \(p=5,r=4\) regression;
- schema, source-hash, and tamper checks for both certificate families; and
- the distinction between the oriented cover \(\widetilde C\), the scalar
  quotient \(C\), Hénon time \(s\), Frobenius degree \(r\), and fixed period
  \(n=7\).

## Major finding 1: the source formula was not yet a generic carrier

The first computation proved only that the literal printed formula fails at
one exact specialization and that an alternative constant placement succeeds
there.  That did not make the alternative septic a generic Hénon eliminant.

**Resolution:** an independent characteristic-zero quotient-field
calculation now reconstructs exactly two Hénon neighbors for every generic
coordinate root.  Symmetry, nondegeneracy, geometric transitivity, and prime
degree force a single seven-cycle.  The adopted septic is therefore proved to
be one generic exact-period-seven Hénon component.  Exhaustion of the full
saturated period-seven scheme is not claimed.

## Major finding 2: the scalar curve had forgotten chronological orientation

The degree-seven curve records a coordinate and its unordered pair of Hénon
neighbors.  Hénon time cannot act after the previous neighbor is forgotten.

**Resolution:** the final object is the degree-14 ordered-edge cover.  Hénon
time acts on the whole cover, with no global choice of orientation.  The deck
involution of the scalar projection is
\(J=R\tau:(x,y)\mapsto(x,a-x^2-y)\), and generically
\(C=\widetilde C/\langle J\rangle\).  Scalar point counts are not substituted
for chronological traces upstairs.

## Major finding 3: finite-prime rows were over-interpretable

Exact affine counts plus the characteristic-zero branch ledger give
reciprocal degree-six polynomials, but they do not by themselves prove a
simultaneous normalization or good reduction of the characteristic-zero
curve at \(p=5,11,13\).

**Resolution:** every such polynomial is called a branch-corrected candidate
numerator.  The paper and artifacts explicitly decline to call these rows
certified local Hasse--Weil factors.

## Major finding 4: producer/checker independence and integrity

The first checker did not cover every new generic-neighbor claim and needed a
stronger binding between source and stored artifacts.

**Resolution:** a non-importing neighbor checker independently recomputes the
subresultants, reductions, nondegeneracy tests, finite-field graph, and
order-seven dynamics.  The test suite checks source hashes, schemas,
cross-artifact agreement, negative mutations, and direct mathematical
regressions.

## Major finding 5: Route-A objects and clocks were mixed

The original evaluation applied a scalar-quotient chronology obstruction to
the only object then available.  Once the ordered-edge cover was constructed,
that record could not serve as the current verdict.

**Resolution:** the original timestamped rejection is retained as append-only
history.  A new evaluation treats \(\widetilde C\) with \(\tau\) as the
dynamical object and \(C\) as a scalar quotient control.  It keeps \(r\),
\(s\), and \(n\) distinct and records
\((\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
\mathrm{A4\_FORMAL\_HINT})\).

## Final review ruling

The final copy audit also corrected three release-level inconsistencies: the
coordinate-index formula now distinguishes \(Rx_i=x_{-1-i}\) from
\(Jx_i=x_{-i}\); all provisional finite-prime counts retain hats rather than
being labelled normalized counts; and a missing backslash in `\qquad` was
fixed before recompiling the PDF.  None changes the mathematical theorem, but
all are material to a clean reproducible release.

The package is suitable as a positive structural result at fixed period
seven and as an exploratory Route-A candidate.  It is not a global
dynamical-zeta construction, a proof of good reduction at the displayed
primes, an exhaustion theorem for the saturated period-seven scheme, or a
Hilbert--Pólya operator.
