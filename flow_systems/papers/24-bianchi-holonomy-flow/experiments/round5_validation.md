# P24 Round-5 validation report

## Material Passport

- Origin Skill: academic-research-suite + experiment-agent
- Origin Mode: Stage-1 research execution + validate
- Origin Date: 2026-08-27
- Verification Status: VERIFIED
- Version Label: p24_round5_validation_v1

## Reproducibility verdict

- Determinism class: exact symbolic/exact candidate arithmetic plus pinned
  high-precision control holonomy.
- Verdict: `REPRODUCIBLE`.
- Core-output combined SHA-256: `b1d323ba04b6f0a0ead32516bc11f6bdf8610847d070ffe54c1b4b7ca0778892`.
- Pre-result freeze SHA-256: `210cff78b8af54847baae1c7ef21572dd697d70004f50723f6b1bac4e19a85b7`.
- Two independent temporary builds must be byte-identical under
  `bash experiments/reproduce_round5.sh`.

## Matched census checks

- Candidate marked owners: 2074 from
  19624 raw cyclically
  reduced linear words.
- Control marked owners: 51 from
  372 raw cyclically
  reduced linear words.
- Candidate primitive loxodromic comparison rows:
  1932.
- Control primitive loxodromic comparison rows:
  39.
- The same canonicalization, symbolic primitivity, owner multiplicity, cutoff,
  binary64/17-significant-digit comparison projection, phase statistic and
  64-permutation rule are used on both sides.
- Every candidate determinant and level-`(3)` membership check passes exactly.
- Maximum control determinant residual:
  `1.562e-62`.
- Control class separation: maximum parabolic `|tr^2-4|`
  `2.203e-63`;
  minimum loxodromic gap
  `1.815e+00`.

## Frozen phase-sensitive observation

```text
candidate |q| = 0.00322886827439; z = -1.74684253916
control   |q| = 0.112113526082; z = -0.811352306226
absolute z contrast = 0.935490232934
```

This is a marking-dependent `[NUMERICAL_OBSERVATION]`.  The candidate has four
marked positive generators / alphabet size 8 while the pinned control has two
/ alphabet size 4.  Thus the Round-4 **data-type** mismatch is closed by a common executable
marked-word rule, but the alphabet/presentation confound remains.  Neither CSV
is a complete metric length spectrum or a full group-conjugacy/primitive
enumeration.

## Integrity and Route boundary

- Prime, prime-ideal and zero target data used: `false`.
- Formal Route-A tuple: `UNASSIGNED`.
- A2--A4: `NOT_EVALUATED`.
- Route B: `NOT_RUN`; invocation allowed: `false`.
