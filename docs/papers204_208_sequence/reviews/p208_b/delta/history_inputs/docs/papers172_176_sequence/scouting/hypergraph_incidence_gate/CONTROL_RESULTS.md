# Exact control results

## Scope

`verify_hypergraph_incidence.py` is a standard-library, integer-bitset
falsification harness for the labelled hypergraph update
$L=W_{2,3}^{\mathsf T}W_{2,3}$ over $\mathbb F_2$.  It does not call a random
source and it does not use floating point.

## Coverage

- `n=1..16`: exact ranks of $W$ and $L$, the literal
  $L=I+A(J(n,3))$ identity on every basis triple, $L^2=L$ or $0$ on every
  basis triple, $WW^{\mathsf T}=(n\bmod2)I+D^{\mathsf T}D$ on every basis
  edge, the fan-triangle cycle basis, and bicycle-cut cardinality.
- `n=3..7`: deterministic enumeration of every Eulerian boundary graph and
  the exact multiplicity of $W^{\mathsf T}b=y$.
- `n=3..6`: exhaustive enumeration of all
  $2^{\binom n3}$ hypergraphs (including 1,048,576 states at $n=6$), the full
  functional graph, fixed/depth census, boundary fibres, and every target's
  fibre at times `0..4`.

The canonical run made **7,387,887** exact assertions and ended in `PASS`.
Its state-transition payload digest is

```text
1665a8b308956f8815e4543e9181ccc7b40cb0b03751c3176f4a1d6f3ce7e8a2
```

## Replay

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers172_176_sequence/scouting/hypergraph_incidence_gate/verify_hypergraph_incidence.py
```

The canonical stdout is `CANONICAL.txt`.  Exact transcript equality can be
tested without creating bytecode:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers172_176_sequence/scouting/hypergraph_incidence_gate/verify_hypergraph_incidence.py \
  | cmp - \
  docs/papers172_176_sequence/scouting/hypergraph_incidence_gate/CANONICAL.txt
```

Computation here is a falsification control.  The all-$n$ proof is in
`PROOF_PACKAGE.md`; neither the computation nor its digest supplies novelty
evidence.

