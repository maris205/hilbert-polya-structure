# C112 — Piecewise-affine border-collision Hénon pilot

This package freezes the two-branch piecewise-affine map

\[
 P_s(x,y)=(-5x+c_s-y,x),\qquad c_0=-2,
 \quad c_1=2,
\]

with branch domains (x<0) and (x>0).  The border (x=0) is excluded from
the ledger.  Every binary word of length 1--8 has an exact affine fixed point
whose itinerary satisfies its declared branch inequalities; this is a finite
border-collision pilot, not a theorem about the full repeller.

The derivative matrix is (B=[[-5,-1],[1,0]]).  To make the finite transfer
screen nontrivial while keeping the geometry source-locked, the frozen branch
weights are (\rho_0=1/2), (\rho_1=2/3).  The resulting 4-by-4 weighted
transfer prefix has

\[
\det(I-zA)=\frac{49z^2+210z+36}{36},
\]

and the unweighted control has (1+10z+4z^2).  There are 71 primitive
binary necklaces through length eight.  The route verdict is

```text
A1 = A1_PARTIAL_CERTIFIED
A2 = A2_CERTIFIED_PREFIX
A3 = A3_NOT_ADDRESSED
A4 = A4_FAIL
```

The package does not claim a complete border-collision Markov partition, an
analytic Fredholm determinant, arithmetic data, or Route B.

## Reproduce

```bash
python3 code/c112_border_producer.py
python3 code/c112_border_checker.py
python3 code/c112_sympy_crosscheck.py
python3 code/c112_replay.py
python3 code/c112_mutation.py
python3 code/c112_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf), and the exact receipt is in
`results/c112_border_evidence.json`.
