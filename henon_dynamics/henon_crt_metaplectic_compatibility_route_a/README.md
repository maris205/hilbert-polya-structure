# HCS-C136 — CRT metaplectic compatibility

This package proves exact two- and multi-factor Chinese-remainder tensor
coherence for the C131 odd-level Hénon quantization after enlarging it to all
unit additive characters.  The local characters contain mandatory inverse
cofactor scalings.  The canonical direct tensor of the standard `c=1` factors
fails already at levels 3 and 5.  The package also proves that
`Theta_[r,c]=F_[r,c] K_r` is an involutive antiunitary, reverses `U_[r,c]`,
swaps Weyl coordinates, and factors exactly under canonical CRT.

## Frozen result

- matrix: `A=[[3,-1],[1,0]]`;
- levels: all odd `r>=3`;
- characters: all units `c mod r`;
- factorizations: fixed ordered lists of finite pairwise-coprime odd factors
  greater than one; split schedule and parenthesization may vary, but leaf
  permutations are not claimed;
- tuple: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
- overall: `ROUTE_A_EXPLORATORY`;
- Route B: unauthorized;
- scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

From the repository root:

```bash
python3 henon_dynamics/henon_crt_metaplectic_compatibility_route_a/code/c136_crt_metaplectic_producer.py
python3 henon_dynamics/henon_crt_metaplectic_compatibility_route_a/code/c136_crt_metaplectic_checker.py
python3 henon_dynamics/henon_crt_metaplectic_compatibility_route_a/code/c136_sympy_crosscheck.py
python3 henon_dynamics/henon_crt_metaplectic_compatibility_route_a/code/c136_replay.py
python3 henon_dynamics/henon_crt_metaplectic_compatibility_route_a/code/c136_mutation.py
```

The producer and checker enumerate 1,131,414 exact modular cases.  The
mutation suite rejects 83 repaired-hash semantic changes plus one stale-hash
change.  See `paper/main.pdf` for the paper and `C136_RELEASE_MANIFEST.json`
for the closed payload ledger.

No external source, random seed, floating-point tolerance, prime table, zero
table, or target fit is used.
