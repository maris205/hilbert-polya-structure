# HCS-C73 generation blocker reliability

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C73 gives the structural deletion theory of the C72 universal-core atlas.
The non-isolated part of the 16-label minimal-generation hypergraph is a cone
with apex `S9` over the complete multipartite graph `K_{1,1,2,5}`; the six
dummy coordinates are isolated vertices.  This geometry yields exactly five minimal blockers of sizes
`1,4,7,8,8`, `35136` destructive deletion sets, and `30400` surviving sets.

The exact homogeneous reliability is

```text
R(q)=(1-q)(1-q^4-q^7-2q^8+3q^9),
```

and the evidence also contains the heterogeneous block formula, full deletion
spectrum, Banzhaf influences, Shapley values, and three distinct robustness
parameters `0`, `3`, and `13`.

Entry points:

- `code/c73_generation_blocker_reliability.py`: source-bound producer;
- `code/c73_generation_blocker_reliability_checker.py`: independent rank checker;
- `code/c73_polynomial_crosscheck.py`: SymPy/GAP cross-check;
- `code/c73_generation_blocker_reliability_replay_checker.py`: replay;
- `code/c73_mutation_test.py`: hostile semantic mutations;
- `results/c73_generation_blocker_reliability_evidence.json`: evidence;
- `paper/main.pdf`: manuscript.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Hypergraph automorphisms are not
identified with core automorphisms.  No full Burnside-ring, arithmetic/local,
Euler-factor, root-number, automorphy, or Hilbert--Polya claim is made.
