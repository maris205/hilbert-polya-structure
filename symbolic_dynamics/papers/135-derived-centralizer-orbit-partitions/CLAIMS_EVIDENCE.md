# Claims and evidence

External status: `HOLD_EXTERNAL`.  Finite enumeration is never used as the
proof of an all-weight statement.

| ID | Claim | Formal support | Executable support | Status |
|---|---|---|---|---|
| C1 | The literal derived-centralizer orbit partition obeys the three-case local rule. | Proposition 2.1 | `verify_wreath_rule` | proved |
| C2 | Two consecutive clean transitions put the intermediate reachable tagged state on a period-one or period-two orbit. | Lemmas 3.1--3.3 | `verify_colored` | proved |
| C3 | Every orbit has period at most two and tail at most `2 ell(lambda) <= 2n`. | Theorem 3.4 | complete functional graphs through weight 45 | proved, bound nonsharp |
| C4 | `B/O1/O2=/O2!=` are the complete recurrent classes. | Theorem 4.1 | `recurrent_class` on 540,634 partitions | proved |
| C5 | The displayed formal OGFs count all fixed points and strict two-cycles. | Equations (8)--(9), Theorem 4.1, and the unnumbered generating-function proof in Section 4 | coefficient comparison through weight 30 | proved |
| C6 | The multivariate product coefficient is the fibre over every target. | Theorem 5.1 | all 28,628 target cells through weight 30 | proved |

## Zero-credit inputs

- the centralizer decomposition by cycle multiplicity;
- generic commutator-subgroup structure in wreath products;
- orbit-partition language for permutation groups;
- the existence of weight-preserving maps on integer partitions and generic
  multiplicity dynamics;
- formal ordinary/multivariate generating-function extraction;
- generic finite-map conversion between recurrent points and cycles.

## Scope sentinels

- `2 ell(lambda)` is not advertised as exact or sharp.
- The two-clean lemma is asserted for tagged states reachable from the
  initial atomic-tag lift, not for arbitrary synthetically coloured states.
- Search-result absence is not novelty or priority evidence.
- P113 has a different Ferrers/principal-hook map and sharp potential; P123
  has graph component complementation and a refinement mechanism.  The tag
  coarsening here is only a proof lift.
- No posting, submission, or owner contact is authorized.
