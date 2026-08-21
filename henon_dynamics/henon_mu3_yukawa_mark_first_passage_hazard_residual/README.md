# HCS-C94 exact hazard and residual-life atlas

C94 extends the frozen C88 first-passage receipt for the twenty actual subgroup
targets.  For each target and each step `k=0,...,16` it records the exact
at-risk count, first-passage count, discrete hazard
`P(T=k | T>=k)`, and the complementary survival transition.  It also records
the complete `k,r` grid for the conditional residual variable
`R_k=T-k | T>k`: survival probabilities, probability masses, mean, second
moment, and variance.  Empty conditioning events are represented by `null`.

The package uses only the frozen C88 evidence and C88 prefreeze manifest.  The
producer, independent bitset checker, SymPy cross-check, clean replay, and
13 hostile mutations all pass.  Evidence SHA-256:

`e185462629459a7d6602e3d1e3f49977a82d3fdee86007c3f906b224f028d1b3`

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

No arithmetic/local-data, Euler-factor, root-number, automorphy, full
Burnside/table-of-marks, or Hilbert-Polya operator claim is made.
