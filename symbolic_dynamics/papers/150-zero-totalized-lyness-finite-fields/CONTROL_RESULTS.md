# P150 exact control results

Status: **PASS / HOLD_EXTERNAL**.

## Canonical command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p150.py
```

The frozen stdout is `verification_output.txt`, with SHA-256
`f95db125148f156dd5ea4a75e2acbf22a68ed565e4c5df6c1399e018acf8f460`.
A fresh replay compares byte for byte with that transcript.

```text
P150_ZERO_TOTALIZED_LYNESS_EXACT_CONTROL
SCOPE=all_odd_prime_fields_through_F101_plus_F9_F25_F27_F49_F121_F125
TOTAL_FIELDS=31
TOTAL_STATE_TARGET_CELLS=110095
TOTAL_ASSERTIONS=2144131
ENUMERATION_IS_NOT_PROOF=1
HOLD_EXTERNAL=1
STATUS=PASS
```

## Finite boxes

The verifier exhausts all 25 odd prime fields through `F101` and the six
nonprime fields `F9`, `F25`, `F27`, `F49`, `F121`, and `F125`.  Their state
counts sum to 110,095.  Each state is used in the forward classification and
each target is used in the inverse classification; the frozen manuscript
therefore reports **110,095 state/target cells each**.

All extension fields are constructed as explicit irreducible quadratic or
cubic quotients.  Before dynamical checks, the program verifies the declared
moduli have no base-field root, every element satisfies the Frobenius
identity, and every nonzero extension element has the computed inverse.

## Checked theorem interfaces

| interface | exact checks |
|---|---|
| carrier and strata | every state, unique membership, pairwise disjointness, coverage, and all five cardinalities |
| temporal atlas | every orbit signature, all tails, all periods, recurrent count, and the four coefficients of the tail polynomial |
| generic dynamics | every one of the five displayed iterate identities at every generic state |
| cycle census | literal cycle extraction, exact-period point counts, divisibility into 5-cycles, and fixed-iterate shadows through iterate 20 |
| fibres and image | every target indegree, image size, unique maximum fibre, and the complete predecessor sets of the singular component |
| exceptional arrows | the distinguished leaf and 2-cycle plus all `q-2` length-three chains in every field |

The implementation uses Python 3 standard-library exact arithmetic only.  It
does not sample, use floating point, call a computer algebra system, access a
network at runtime, or import a third-party package.  Exhaustive tests over
finitely many fields can expose counterexamples but cannot prove the
all-parameter theorem, novelty, priority, ownership, or release clearance.
