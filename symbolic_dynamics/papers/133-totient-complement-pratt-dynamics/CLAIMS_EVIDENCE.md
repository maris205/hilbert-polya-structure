# Claims and evidence

External status: `HOLD_EXTERNAL`.  Enumeration is never used as the proof of
an unbounded statement.

| ID | Claim | Formal support | Executable support | Status |
|---|---|---|---|---|
| C1 | For squarefree `n`, the divisor map is conjugate to the displayed Pratt-DAG support map. | Proposition 2.1 | `literal_support_conjugacy` | proved |
| C2 | Every recurrent state is uniquely decoded from its source phases. | Equations (6)--(7), Lemma 3.1, and the completeness paragraph after Proposition 3.3 | `source_phase_decoder` | proved |
| C3 | There are no fixed states, exactly `2^s` recurrent states, and `2^(s-1)` exact two-cycles. | Lemma 3.1 and the census paragraph after Proposition 3.3 | `recurrent_census` | proved |
| C4 | Every orbit enters recurrence by time at most `h+1`. | Two-step erasure Lemma 3.2 and level induction Proposition 3.3 | `entry_bound` | proved, nonsharp |
| C5 | The inclusion--exclusion formula counts the fibre over every target. | Theorem 1.1(iv) and the derivation in Section 4 | `all_target_fibres` | proved |

## Zero-credit inputs

- Euler's product formula for `phi` and squarefree support encoding;
- the prime-chain relation `p|(q-1)`, Pratt trees, and Pratt height;
- AND--NOT/signed interaction diagrams and generic DAG propagation;
- inclusion--exclusion as a general method;
- finite-map conversion from recurrent points to cycles.

## Scope sentinels

- `h+1` is not advertised as exact or sharp.
- Search-result absence is not a novelty certificate.
- The four finite prime sets are falsifiers only.
- No posting, submission, or owner contact is authorized.
