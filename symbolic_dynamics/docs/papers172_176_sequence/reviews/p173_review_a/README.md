# P173 Hostile Review A control

This directory contains the non-author Review-A executable evidence for
P173, *Random Quotient-Leakage Erosion*.  It is intentionally separate from
both the paper-local verifier and the discovery/scouting code.

## Representation firewall

The literal lane uses canonical reduced-row-echelon row bases over prime
fields.  An ambient endomorphism is a tuple matrix over the field, and the
quotient map is evaluated in annihilator coordinates for `V/U`.  Its kernel
is solved in coefficient space and then mapped back to an ambient RREF basis.
Thus this lane uses neither materialized vector-set subspaces nor binary
matrix masks.

The quotient lane independently builds Gaussian coefficients by their
incidence recurrence and uses exact rational elimination for Jordan
nullities.  It explicitly separates direct complementary coupling from the
cases where the one-step entry is zero and coupling occurs through
intermediate dimensions.

## Exact box

- literal every-map/every-source/every-target audits for `q=2`, `n=0..3`,
  through six epochs;
- a second literal field lane for `q=3`, `n=0..2`, through five epochs;
- quotient spectrum, complete Jordan inventory, and absorption for
  `q in {2,3,4,5,7,8,9,11}` and `n=0..14`;
- explicit endpoint eigenvectors and the degenerate `n=0` inventory; and
- `36,390` exact assertions, including `128` direct and `208` indirect
  complementary pairs.

The control confirms the intended formulas but exposes that the current
manuscript's unconditional claim of two `J_1(1)` blocks is false at `n=0`,
where `0=V` and the quotient has a single state.

## Replay

From the repository root:

```bash
PYTHONHASHSEED=0 python3 \
  docs/papers172_176_sequence/reviews/p173_review_a/verify_review_a.py
cmp docs/papers172_176_sequence/reviews/p173_review_a/CANONICAL.txt \
  <(PYTHONHASHSEED=0 python3 \
    docs/papers172_176_sequence/reviews/p173_review_a/verify_review_a.py)
```

Two fresh processes matched `CANONICAL.txt` byte for byte.  Finite
enumeration is falsification evidence only.  It is not an all-parameter
proof, owner clearance, or novelty evidence.  The lifecycle remains
`SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`.
