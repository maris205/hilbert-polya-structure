# HCS-C342: Directed reinforcement as a Dirichlet environment

This package proves an exact finite-graph theorem for linear reinforcement on
labelled directed edges, with at least one outgoing arc at every vertex. The
path law factors into vertex-wise rising
factorials, equals the annealed law of independent Dirichlet transition rows,
has an exact conjugate posterior, and yields almost-sure transition and
occupation limits on every finite strongly connected directed multigraph.

The proof covers deterministic outdegree-one rows, labelled parallel arcs and
the one-vertex Pólya boundary with at least one loop. Zero initial weights,
empty outgoing rows and reducible graphs are
kept outside the main theorem with their precise failure modes stated.  The
directed model is not the undirected ERRW magic-formula model and is not Wilson
sampling.

The directory contains the theorem and source audit, canonical finite
evidence, a producer-independent checker, SymPy, byte replay, hostile mutation
tests, three manuscript revisions, and the self-excluding release manifest.
Run:

```bash
python code/c342_release_manifest.py
```
