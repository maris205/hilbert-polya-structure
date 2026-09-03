# P176 independent Hostile Review B executable

This directory contains the fresh executable evidence for the second hostile
review of P176. It preserves the paper's lifecycle
`AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`; finite computation is a falsifier,
not a proof or an owner-clearance result.

## Independence barrier

`verify_p176_review_b.py` imports no author, scout, or Review-A module. It was
implemented and run before Review A's derivation or executable was opened.
Its representation and algorithms differ from both earlier controls:

- states are binary strings and coordinate rotation is literal string slicing;
- orbit clocks are obtained with Brent's constant-memory cycle algorithm;
- every generator component is rebuilt as a finite successor digraph, whose
  cycles and distances are found directly before comparison with the claimed
  `10`-boundary/run classification; and
- inverse fibres are formed from a reverse adjacency table and compared
  target by target with the two independently undone rotations.

The author/scout control uses tuples, while Review A uses integer bit masks.

## Exact scope

The exhaustive box contains every binary state for `1 <= n <= 17`. For every
state and every pointed necklace it checks:

1. carrier, weight, necklace, and complement invariants;
2. the exact signed phase map and all generator components;
3. every recurrent cycle and pointwise tail;
4. the complete period set and deepest-state set, including `n=1,2`;
5. every target predecessor set and each weight-layer `0/1/2` histogram;
6. the image formula; and
7. primitive fixed-density counts and the Möbius fixed census.

For `2 <= n <= 96`, a separate arithmetic pass constructs a literal witness
for every advertised proper-divisor period and checks nonnegativity plus both
mass identities for every closed fibre histogram.

The canonical run reports **19,758,014 assertions** and `RESULT: PASS`.

## Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  python3 docs/papers172_176_sequence/reviews/p176_review_b/verify_p176_review_b.py \
  > /tmp/p176_review_b.txt
cmp /tmp/p176_review_b.txt \
  docs/papers172_176_sequence/reviews/p176_review_b/CANONICAL.txt
```

The run is standard-library only. On the review host it takes about five
minutes because the component audit is deliberately pointwise rather than
only aggregate.
