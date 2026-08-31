# P136 exact-control results

## Frozen status

`ROUND_A_REPLAY_PASS / 2026-08-31 UTC / HOLD_EXTERNAL`

The paper-local verifier is self-contained and uses only the Python standard
library. All probabilities are `fractions.Fraction`; there is no sampling,
floating point, seed, timestamp lookup, network access, or third-party import.

## Byte replay

Run from the paper directory:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Fresh exit code: **0**.

The frozen stdout reports:

```text
P136_RANDOM_SUNFLOWER_TRANSVERSAL_LAWS
arithmetic=fractions.Fraction; sampling=none; third_party=none
parameter_inputs=5812
exact_assertions=174170
lanes=unit_aggregate:4092,weighted_aggregate:1638,unit_actual_vertices:78,two_component_forests:4
max_aggregate_support=32
max_unit_mean=2101/625
checks=weighted_endpoint,actual_vertices,uniform_step_count,top_atom,mean,second_moment,forest_endpoint,forest_step_count
status=PASS
```

## What is checked

| lane | inputs | comparisons |
|---|---:|---|
| Unit-rate aggregate | 4092 | Exact grid `c in {1,2,3}`, `m in {1,...,5}`, `p_i in {1,...,4}`; every terminal mask and step-count mass, positivity, normalization, tail mean, tail second moment, and the two-event `T=m` identity. |
| Weighted aggregate | 1638 | Exact grid `c in {1,2}`, `m in {1,2,3}`, `p_i,lambda_i in {1,2,3}`; every terminal mask and step-count mass against the inclusion--exclusion formula, with positivity and normalization. |
| Unit-rate actual vertices | 78 | Exact grid `c in {1,2}`, `m in {1,2,3}`, `p_i in {1,2,3}`; direct mark enumeration against the resolved endpoint and step-count laws. |
| Two-component forests | 4 | Every joint endpoint mass and complete step-count convolution; three controls are unit-rate and one has unequal rates. |

The total is **5812 parameter-labelled inputs** and **174170 exact
assertions**. Compared with the scout verifier, this paper-local lane adds an
explicit `T=m` split and an independent second-moment check for every
unit-rate input.

## Hashes

```text
0285c2c7f82540d421888f37bad0302a3a3fd106e916c1ad590018e927b51913  code/verify.py
5553c8c797bc4b577a6252959471f1e556e850cafcdf96d8a74b39353491271c  code/verification_output.txt
```

## Evidence boundary

This finite computation is falsification evidence, not a proof or novelty
certificate. Weighted aggregate endpoints are exhaustive only over the stated
integer grid; arbitrary positive real rates are carried by proof. Actual-vertex endpoints are separately enumerated at unit
rates. Forest factorization is checked on four two-component controls. The
weighted actual-vertex and arbitrary-forest statements rely on the manuscript's
all-parameter proofs and must not be described as exhaustively enumerated.

Every reported convolution is a convolution of discrete selection counts.
The verifier has no wall-clock observable and makes no claim about continuous
elapsed absorption times.
