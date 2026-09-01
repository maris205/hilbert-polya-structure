# Exact experiment plan

## Claim-driven design

The proof supplies formulas for the two cyclic cover orders, inversion Burnside corrections, ramified gluing, fixed counts, periodic population, tail filtration, image ranks and Koopman Jordan blocks.  The evidence task is to reject implementation and boundary mistakes, not infer the theorem from samples.

## Frozen corpus

The exact field models are

`F_4,F_5,F_7,F_8,F_9,F_11,F_13,F_16,F_25,F_27,F_49`,

with explicit monic irreducible polynomials for every extension field.  Each is tested for `d=0,...,10`.  This creates 121 maps and 1,914 directly enumerated case-vertices.  The corpus contains 77 nonprime-field cases and 33 characteristic-two cases.

## Independent paths

1. The producer evaluates the closed integer formulas.  A direct Chebyshev recurrence contributes only the labeled map digest and an observed histogram.
2. The checker imports no producer.  It separately verifies that each stored modulus is monic, has the declared degree, is irreducible over `GF(p)`, and is reused unchanged across all degrees for fixed `q`; it then implements polynomial-basis finite-field arithmetic and follows every point until its first repeat.
3. The checker recomputes every fixed set, primitive cycle, tail layer and image set directly.
4. SymPy forms 64 selected full composition matrices and checks 311 exact characteristic-polynomial and rank identities.
5. Fresh replay regenerates the JSON in a temporary directory and requires byte equality.
6. Forty-one hostile mutations repair the outer payload hash before invoking the semantic checker.  The added model attack changes the `q=4,d=0` modulus from `[1,1,1]` to reducible `[1,0,1]` and must still be rejected.

## Boundary targets

- characteristic two, where `+2=-2` and one branch remains;
- odd characteristic, where both branch values survive;
- `d` sharing prime factors with neither, one, or both of `q-1,q+1`;
- identity `d=1`;
- separate constant `d=0`;
- special branch components whose folded trees are not generic uniform trees.

No floating-point threshold, random seed, prime table, zero table, fitted coefficient or target datum is used.
