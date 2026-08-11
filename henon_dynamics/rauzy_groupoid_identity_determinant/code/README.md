# C29 code gate

No release producer is committed in Phase 1.  After the research checkpoint,
Phase 2 will implement two independent programs.

## Producer contract

- source-lock the six C25/C26/C28 inputs by SHA-256;
- reconstruct the C25 graph and fixed-frame arrows;
- build formal inverse arrows without identifying them with distinct original
  arrows having opposite endpoints;
- verify state continuity, linear and cyclic non-backtracking, primitivity and
  exact chronological holonomy of `C1,C2`;
- verify `B=AHA`, `C=AKA`, `KYK=YKY`, the expanded C26 word and the order-four
  repetition control;
- enumerate the frozen small-length identity census as regression evidence;
- emit determinant-moment and Route-A scope decisions in canonical JSON.

## Independent checker contract

- do not import the producer;
- implement separate integer matrix multiplication/inversion and word
  reduction;
- reconstruct expected matrices from upstream artifacts rather than copying
  producer output;
- verify the canonical payload digest before semantic fields;
- reject rehashed mutations of chronology, inverse identity, cyclic closure,
  primitivity, gauge invariance, normalized trace and natural-extension scope.

## Required mutations

1. replace a formal inverse by an opposite original Rauzy arrow;
2. allow one immediate cyclic backtrack;
3. reverse chronological multiplication;
4. change one matrix entry;
5. claim the symmetric object is the natural extension;
6. replace `Theta(g^r)` by `Theta(g)^r`;
7. call the germ an ordinary infinite-dimensional Fredholm determinant;
8. promote unit edge length to the AGY roof.

The default runner must verify an existing manifest.  Manifest refresh must
remain an explicit release-only option.
