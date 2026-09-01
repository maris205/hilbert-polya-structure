# Exact control results — round 1

## Canonical replay

Run from this paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p145.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p145.py | \
  cmp - verification_output.txt
```

The verifier uses only Python integers and `fractions.Fraction`.  It has no
sampling, floating point, seed, timestamp, third-party package, or network
dependency.  Acceptance requires byte-identical output ending in
`status=PASS`.

## Frozen round-1 coverage

| Control | Exact coverage |
|---|---:|
| Labelled simple graphs, orders 1--5 | 1,099 |
| Orbit states visited | 14,149 |
| Direct return-recurrence state cells, times 0--6 | 71,874 |
| Component partitions, every fixed total 1--30 | 28,628 |
| Distinct fixed-total spectral signatures | 28,628 |
| Input-only `(n,Q)` recoveries | 28,628 |
| Candidate exact division attempts | 624,834 |
| Successful input-only factor peels | 144,024 |
| Squarefree `E_s` factors, `2<=s<=30` | 29 |
| Folded-quotient sizes checked, including `s=1,2` | 12 |
| Constructed `P_4/K_4` adjacency witnesses | 1 |
| Constructed affine-orbit witnesses | 1 |
| Unknown-`n` edgeless orders checked | 6 |
| Total exact assertions | 155,901 |

## What is now genuinely tested

For every graph, the program independently checks the mod-two cut rank, full
relation kernel, constant fibres, BFS orbit, labelled transition closure and
symmetry, legal sign multiplicities, complete spectrum, direct return
recurrences, and period criteria.

For every partition of every fixed total through 30, it constructs `Q` and
calls

```python
recover_component_orders(total, compressed)
```

before comparing the result with the withheld partition.  The routine's
factor-choice decisions use only `total` and `compressed`: it scans sizes from
the known total down to two and tests exact integer-polynomial divisibility.
The hidden partition appears only after return, as the expected answer.  This
is a real executable version of the known-`n` inverse.

The folded-quotient control verifies the pivot generator images.  At `s=1`
the only image is zero; at `s=2` both labels give the same nonzero image; from
`s=3` onward the images are the coordinate vectors plus the distinct
all-ones vector.

The adjacency boundary is also constructed rather than formula-repeated.
The code builds the edge sets of `P_4` and `K_4`, derives each cut-generator
orbit and exact labelled transition matrix, and computes each characteristic
polynomial by the exact Faddeev--LeVerrier/Newton recurrence.  Both return
`z^8-z^6`.  The all-edgeless witness independently builds orders 1--6 and
gets `z-1` every time.

## Explicit downgrade from round 0

The round-0 root controls did not compute roots: they asserted their own
integer hypotheses.  They have been deleted.  The revised code checks exact
squarefreeness only.  It does **not** claim to computationally certify strict
nearest-root order or nearest-root noncollision; those are all-parameter
analytic proof steps in `main.tex`.

Likewise, the round-0 exact divisions used the true partition to select each
factor.  The revised division counts come only from the public-input recovery
routine.  Distinct fixed-total signatures remain a separate exhaustive
injectivity pressure test.

## Interpretation boundary

The controls can expose an erroneous quotient convention, hidden isolate
loop, duplicate-generator error, bad multiplicity, incorrect return/period
formula, failed input-only recovery, or false nonidentifiability witness.
They do not prove the all-parameter theorem and do not establish novelty,
priority, ownership, or release clearance.  External status remains
`HOLD_EXTERNAL`.
