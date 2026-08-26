# C171 results

The all-\(d\) Walsh, trace/determinant, return and Krawtchouk lumping theorem is
proved.  Exact sentinels cover \(d=1,\ldots,18\) and \(n=0,\ldots,24\).

- Evidence payload SHA-256: `27d7fb820cc12dea00c0997a5d7fde2da7df366221e524f8d05ccff032be51b4`.
- Evidence file SHA-256: `63ded054f12b3309d4202fb2d15c584b927ff7ba9386f37c2f45a724112b01dc`.
- Independent checker: 2,990 assertions.
- Independent SymPy reconstruction: 914 checks.
- Mutation suite: 38/38 repaired-hash mutations and 1/1 stale-hash mutation rejected.
- Producer replay: byte-identical.

No pivot was required.  A0 fails because the family is generic across every
dimension and has no prime-derived orbit/clock/weight structure.  The natural
self-adjoint Markov operator is explicit progress, but a Hamiltonian
exponential changes the frozen dynamics, so A4 remains a formal hint.  Since
A0 is mandatory, the overall verdict is `ROUTE_A_REJECTED`; the source theorem
is retained.
