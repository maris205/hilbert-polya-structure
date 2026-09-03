# P172 hostile review B — independent control lane

This directory contains Reviewer B's formulation-independent exact controls
for `papers/172-fresh-map-self-image-erosion/`.

## Independence

`verify_review_b.py` imports no author, scouting, Review-A, or earlier-paper
module.  It starts from the literal update (A\leftarrow A\cap f(A)) and
uses a deliberately different stack:

1. complete endomap tuples (f:[n]\to[n]), rather than only restrictions;
2. explicit restricted-growth words for set partitions, rather than a
   Stirling recurrence or onto inclusion–exclusion;
3. a second required-box sieve for the unmarked kernel;
4. SymPy characteristic polynomials of the full labelled operator;
5. the explicit intertwining (PL=LQ) for cardinality functions;
6. CAS rank tests for the resonant quotient; and
7. Kronecker substitution to encode complete image-size histories in one
   polynomial exponent.

## Run

```sh
python3 verify_review_b.py
```

The canonical output is `CANONICAL.txt`.  `MANIFEST.sha256` records the
settled verifier, transcript, and this provenance note.  The calculations
are falsification controls, not proofs or owner clearance.  External status
remains `HOLD_EXTERNAL`.

