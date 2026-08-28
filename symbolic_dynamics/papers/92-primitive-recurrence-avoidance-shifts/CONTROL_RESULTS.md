# P92 Exact Control Results

## Command

```text
python3 code/verify_primitive_avoidance.py
```

## Frozen output

```text
q=2, r=2, coefficients=(1, 1), states=4, degree=1, L=3, H=1, first_anomaly=3, anomaly_size=3, mixing=no (q=2 boundary)
q=3, r=2, coefficients=(1, 1), states=9, degree=2, L=8, H=2, first_anomaly=8, anomaly_size=32, mixing=yes
q=3, r=3, coefficients=(2, 0, 1), states=27, degree=2, L=26, H=8, first_anomaly=26, anomaly_size=6656, mixing=yes
q=4, r=2, coefficients=(2, 1), states=16, degree=3, L=15, H=3, first_anomaly=15, anomaly_size=405, mixing=yes
q=5, r=2, coefficients=(2, 2), states=25, degree=4, L=24, H=4, first_anomaly=24, anomaly_size=6144, mixing=yes
PASS: 258 exact assertions
```

For `q=4`, integer `2` denotes `u` in
`F_4=F_2[u]/(u^2+u+1)`.

## What is computed independently

The checker does not insert the claimed characteristic polynomial and report
success.  For each lane it:

1. searches for a primitive companion and checks that its orbit is all
   `q^r-1` nonzero state vectors;
2. independently enumerates the transpose orbit on dual vectors;
3. counts exactly `q^(r-1)-1` dual vectors on the last-coordinate
   hyperplane and verifies the parity of the remaining count;
4. constructs the full zero–one adjacency matrix from all nonzero errors;
5. checks constant indegree and outdegree `q-1`;
6. computes `det(lambda I-A)` over the integers with the
   Faddeev–LeVerrier algorithm;
7. checks strong connectivity and graph period one for all `q>=3` lanes;
8. computes actual matrix traces through time `L+1`;
9. finds the first deviation from `(q-1)^n` and reconstructs `(q,r)`.

The binary lane is deliberately a negative mixing control.  The nonprime
`F_4` lane prevents the calculation from depending on prime-field integer
arithmetic.

## Sharp witness

For `(q,r)=(3,3)`, the first 25 periodic counts equal those of the full
two-shift.  At the first anomaly,

```text
F_26 = 2^26 + 6656 = 67,115,520.
```

## Limits of the controls

- The finite controls cover five small lanes; the theorem for arbitrary
  prime powers and ranks is supplied by the Fourier proof.
- Only one binary rank is enumerated because `q=2` is a boundary control,
  not part of the mixing theorem.
- Nonprimitive companions and error subsets other than `F_q^×` are outside
  the frozen theorem contract.
