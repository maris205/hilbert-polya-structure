# Exact Control Results — P119

## Canonical result

`PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py` completed with:

```text
regular Engel exact control: PASS
assertions=1,491,877
fields=F_2,F_3,F_4,F_5,F_8,F_9
exhaustive_phase_states=55,808
restricted_surjections=39
iterated_fibre_profiles=112
nonregular_counterexample_states=20,514
exact_layer_table_rows=43
claim_ceiling=fixed_J_equals_I_plus_regular_shift
```

Canonical stdout is stored in `code/verification_output.txt`. The assertion
counter is the number of executed `check` calls, not a number of logically
independent mathematical claims.

Bier 2013 already proves the same fixed-`J` restricted and iterated image
equalities over arbitrary fields.  Their computational checks below are
regressions for a reproduced owned input; contribution credit is restricted
to the finite-field multiplicities and the derived temporal/type census.

## Exhaustive regular lanes

| Field | Polynomial-basis modulus | Maximum `n` | Phase states through maximum `n` |
|---|---|---:|---:|
| `F_2` | `z` | 6 | 33,867 |
| `F_3` | `z` | 4 | 760 |
| `F_4` | `z^2+z+1` | 4 | 4,165 |
| `F_5` | `z` | 4 | 15,756 |
| `F_8` | `z^3+z+1` | 3 | 521 |
| `F_9` | `z^2+1` | 3 | 739 |

Each lane includes the `n=1` singleton. All field addition,
multiplication, inverses, Frobenius identities, and distributivity are
checked before the matrix dynamics.

## Assertion families

1. Literal upper-unitriangular inverses are both left and right inverses.
2. Every update from `gamma_k` lies in `gamma_(k+1)`.
3. Each restricted image equals the full next filtration level (owned input
   regression).
4. Every one-step target has the predicted finite-field fibre size.
5. Commuting matrices equal exactly the prescribed polynomial-in-`N`
   centralizer.
6. Every literal fibre equals the corresponding **left** centralizer coset.
7. The matrix identity `XJ=JX E(X)` holds statewise.
8. Every discrete-difference map has one free field constant over each
   target (existence itself is owned).
9. Every iterated target fibre agrees with the product formula; the owned
   iterated image is checked as a regression.
10. Every cumulative root fibre, exact depth layer, sharp height, and deepest
    shell agrees with the theorem.
11. Full and exact-filtration-source indegrees agree for every target.
12. The identity is the unique point fixed by each tested positive iterate.
13. For `J'=I+E12+E34`, the literal centralizer equations, image size,
    strict failure of `gamma_2` surjectivity, and `q^4` fibres all agree.
14. The 43-row layer table is rebuilt and compared byte for byte.

## Counterexample guards

- Nonprime-field lanes guard against a proof that silently assumes a prime
  field.
- The near-regular `U_4` lane rejects arbitrary-unipotent generalization.
- Targets outside the next filtration level reject a fictitious positive
  fibre everywhere.
- Literal left-coset comparisons guard the commutator-orientation convention.
- The `n=1`, `n=2`, and `t=0` lanes guard empty-sum and terminal-depth
  conventions.

The program uses only the Python standard library. It does not certify
novelty, owner completeness, specialist approval, or external release.
