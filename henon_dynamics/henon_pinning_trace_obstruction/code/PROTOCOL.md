# Frozen exact-certificate protocol

Frozen: 2026-08-06, before the canonical run.

## Producer obligations

The producer must use exact `fractions.Fraction` arithmetic to emit:

1. the four states and all six chronological edges;
2. allowed and forbidden radicand disks;
3. the \(X\Subset Y\) margin;
4. exact square-map boundary minima and gaps;
5. the conservative \(1/360\) square-root image clearance;
6. the squared derivative bound \(2/33\);
7. deterministic rational checks of
   \(\det DR=-d\det(I-M)\);
8. the primitive/double-repeat orbitwise scalar-cocycle contradiction, with
   aggregate-only cancellation explicitly left open;
9. a single mechanical classification `C02D_NO_GO`.

It must not compute an operator spectrum, access the network, read prime or
Riemann-zero data, or change any mathematical constant after inspection.

## Checker obligations

The checker must not import the producer. It independently reconstructs all
rational constants, validates the complete ID sets, recomputes the algebraic
tests, checks the certificate's canonical SHA-256 payload hash, and rejects
missing, extra, reordered, or tampered records.

## Expected-fail controls

- Add the forbidden \((t,r)=(+,+)\) pair: its radicand disk crosses zero.
- Delete one allowed edge: the checker rejects incomplete chronology.
- Claim an orbitwise scalar correction \(-1\): its double repetition is \(+1\), so the
  checker rejects it.
- Reclassify the window as a same-clock approximation: the semantic ledger
  contains no truncated one-step coefficient and rejects the classification.

## Pass condition

Both independent programs report `all_checks_pass: true`, the stored
certificate hashes match, and the conclusion remains the pre-registered
`NO_GO`. A pass certifies the obstruction; it does not promote the candidate.
