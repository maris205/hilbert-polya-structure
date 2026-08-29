# Exact control results

The deterministic control uses only integer bitsets and finite sets.  It has
two update implementations with different representations.

Registered lanes:

- every simple graph through six vertices;
- every state of those graphs;
- every bipartite graph with color classes through `3+3`;
- every state of paths through 17 vertices;
- explicit `K_2` and nonbipartite `K_3` sentinels.

The canonical output is `code/verification_output.txt`.  It must report
`PASS`; exact assertion and state counts are frozen after execution.

These controls are finite falsifiers.  The general theorems are proved in
the manuscript.
