# HCS-C375: LPS quaternion nonbacktracking dynamics

This package closes the arithmetic and oriented-cycle dynamics of the
six-regular Lubotzky--Phillips--Sarnak family `X^{5,q}`.  Six integral
Hamilton quaternions of norm five reduce modulo every prime
`q > 5`, `q = 1 mod 4`.  The Legendre symbol `(5/q)` selects a connected
`PSL2(F_q)` or `PGL2(F_q)` Cayley graph.  Its Hashimoto operator has an
exact Bass determinant, every-iterate trace and primitive-oriented-cycle
ledger, while the LPS Ramanujan theorem puts every nontrivial quadratic
Hashimoto root on the circle of radius `sqrt(5)`.

The result is one theorem-scale unit, not a generic repackaging of graph
zeta theory.  HCS-C329 already owns the workspace's general
Bass--Ihara--Hashimoto mechanism.  C375 owns only the explicit norm-five
quaternion congruence family, its two arithmetic chambers, gauge lock,
complete specialized spectral map, and executable five-graph atlas.

The exact evidence constructs the full groups for `q=13,17,29,37,41`:
104,316 vertices, 625,896 oriented edges, and 60 iterate rows through time
12.  A separate ledger classifies all 1,124 eligible primes at most 20,000.
These finite calculations audit the implementation; they do not replace
the cited all-prime LPS theorem.

## Route decision

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`

Overall: `ROUTE_A_EXPLORATORY`.  The primitive-cycle theorem is exact for
each source graph, but it does not transfer the modulus `q` or primality into
an orbit label, give `p <-> gamma_p` and prime-power repetition, or produce
intrinsic `log p`/von Mangoldt weights.  The mandatory shuffled-period,
random-weight, random-phase, same-density-length, neighboring-parameter, and
simpler-parent controls at the A1 orbit-correspondence layer are absent.
Separately, A0 does execute exact wrong-residue-prime, matched-composite, and
cyclic chamber-label-shuffle controls; those do not supply the missing orbit
correspondence.
The package contains no target Euler product, target divisor, zero matching,
automorphy claim, root number, or Hilbert--Pólya operator.  Route B remains
locked.

## Reproduce

```bash
python -B code/c375_release_manifest.py --write --build-pdfs
python -B code/c375_release_manifest.py
python -m unittest tests/test_c375_smoke.py
```

The canonical manuscript is [paper/main.pdf](paper/main.pdf).  The exact
proof chain is in [THEOREM_PACKAGE.md](THEOREM_PACKAGE.md).
