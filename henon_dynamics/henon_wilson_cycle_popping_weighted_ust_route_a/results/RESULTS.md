# Exact results

- Evidence file SHA-256:
  `6fe802d7b5a5cbaae6426001309931949ccae872b94ed23825607a9fa7c7f282`
- Canonical payload SHA-256:
  `e3462ae811ed6b1a1f63c4d263bda036c34f462215d0d97eb63ee82778722148`
- Connected labelled simple graphs on \(1\le n\le5\): **772**.
- Simple graph--tree pairs: **8,136**.
- Simple-graph edge-subset transfer-current events: **55,895**.
- Weighted labelled multigraph cases: **24**.
- Weighted tree rows: **846**.
- Weighted edge-subset events: **7,032**.
- Rooted connected simple graphs in the finite-stack audit: **167**.
- Depth-two stack tables: **12,754**.
- Independent checker: **224,424 exact checks**, pass.
- SymPy: **85 symbolic/exact checks**, pass.
- Hostile mutation: **142/142 rejected**, pass.
- Replay: **1,844,227 bytes**, exact match.

All matrix-tree determinants equal their explicit weighted tree partitions.
Every principal transfer-current determinant equals its enumerated edge-event
probability.  All tested roots give the same edge kernel.  Every selected pair
of parallel labels has zero simultaneous-inclusion minor.  Every finite stack
table that terminates within the frozen depth has a unique terminal pop vector
and agrees with canonical Wilson exploration; no disagreement was found.

These finite results are convention and implementation receipts.  The local
diamond/strip proof, finite-chain hitting argument, last-exit telescope, and
conductance-perturbation identity prove the theorem.
