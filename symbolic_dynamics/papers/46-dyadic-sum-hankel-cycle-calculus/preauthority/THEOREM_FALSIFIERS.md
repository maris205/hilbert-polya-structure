# Theorem Falsifiers and Boundary Controls

## Purpose

Every row below must be represented by an actual mutation or exact positive
control in the later integration registry. A theorem is not certified by the
number of rows; each designated evaluator must reject the stated false
variant with an exact failure class.

## Negative controls

| ID | Mutation | Required rejection |
|---|---|---|
| F01 | Replace \(m+n=2^a\) by \(m+n=a^2\) while retaining SD-C48 | SOURCE_SUPPORT_CHANGED |
| F02 | Delete the loop at \(1\) | LOOP_CONVENTION_CHANGED |
| F03 | Insert the edge \(1\leftrightarrow5\), whose sum is not dyadic | SUPPORT_AND_VALUATION_FAILURE |
| F04 | Assert boundedness at \(\sigma=0\) | ROW_ONE_NOT_L2 |
| F05 | Assert \(S_2\) membership at \(\sigma=1/2\) | HILBERT_SCHMIDT_ENDPOINT_DIVERGES |
| F06 | Assert \(S_1\) membership at \(\sigma=1\) | TRACE_CLASS_ENDPOINT_DIVERGES |
| F07 | Remove the factor \(1/2\) from the odd-cycle alternating solution | ODD_CYCLE_FORMULA_FAILURE |
| F08 | Accept an even label tuple with nonzero alternating sum | EVEN_CYCLE_COMPATIBILITY_FAILURE |
| F09 | Use \(\det(I-zH_s)\) on \(1/2<\sigma\le1\) | ORDINARY_DETERMINANT_OUTSIDE_S1 |
| F10 | Call \(H_s\) Hermitian for \(\Im s\ne0\) | OPERATOR_TYPE_FAILURE |
| F11 | Count edge-label tuples as primitive temporal orbits | PRIMITIVE_TYPE_FAILURE |
| F12 | Infer an endpoint from a finite-cutoff SVD | FINITE_CUTOFF_LIMIT_FAILURE |
| F13 | Exchange the edge marker \(z\) with the valuation weight \(2^{-ks}\) | MARKER_WEIGHT_OWNERSHIP_FAILURE |
| F14 | Claim rational-prime emergence because the support uses powers of \(2\) | A0_PRIME_SELECTOR_FAILURE |

## Positive controls

| ID | Exact control | Expected result |
|---|---|---|
| P01 | \(1+3=4\), \(2+6=8\), \(3+5=8\) | support true and equal \(v_2\) on each edge |
| P02 | labels \((2,4,4)\) | unique odd cycle \((1,1,3)\) |
| P03 | labels \((4,8,8,4)\) | even compatibility true; positive solutions \(n_1=1,2,3\) |
| P04 | labels \((4,4,8,4)\) | even compatibility false |
| P05 | \(\sigma=1\) Hilbert–Schmidt level | exact \(2H_{2^a-1}/2^a\) and summable |
| P06 | \(\sigma=2\) entrywise level | \(O(a2^{-a})\) and summable |
| P07 | diagonal vertices \(1,2,4,8\) | legal loops and trace terms \(1,2^{-s},4^{-s},8^{-s}\) |
| P08 | nonreal \(s\) | singular values equal those of \(H_{\Re s}\) under two-sided diagonal unitaries |

## Quantifier controls

- “bounded iff sigma>0” is an infinite-operator statement, not a cutoff
  trend.
- \(S_2\) and \(S_1\) membership claims include endpoint rejection.
- the cyclic solver classifies a fixed ordered cyclic label tuple; it does not
  quotient distinct label tuples or count primitive vertex cycles by itself.
- the odd-block parity condition is additional to positivity.
- determinant identities are asserted only after ideal membership is proved.

## Proves-too-much guard

These tests do not imply that every lacunary Hankel operator has the same
thresholds, that every additive arithmetic graph has a \(v_2\) direct sum, or
that power-of-two labels select rational primes.

