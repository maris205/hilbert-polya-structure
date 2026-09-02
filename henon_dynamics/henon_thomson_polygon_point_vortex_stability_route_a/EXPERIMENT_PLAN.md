# Executable evidence plan — HCS-C284

## Claims-to-evidence matrix

| Claim | Analytic owner | Executable evidence | Failure caught |
|---|---|---|---|
| Polygon rotates with `Omega=Gamma*(N-1)/(4*pi*R^2)` | direct gradient sum | raw equilibrium residual for every `N=3..64` | factor-two/sign convention |
| DFT Hessian block is `c*diag(2(N-1)-q,q)` | pair Hessian + root sum | 2,077 exact rows and raw `2N by 2N` reconstruction | copied closed formula, basis error |
| `N=3..6` elliptic, `N=7` degenerate, `N>=8` hyperbolic | maximize `m(N-m)` | 62 complete polygon summaries | off-by-one threshold |
| `N=7` has only modes `3,4` degenerate | exact equality | singular rows and semantic mutations | accidental nonlinear claim |
| stability is invariant under positive `Gamma/R^2` scale | positive scalar factor | 64 exact rational scale cells | wrong radius power |
| symmetry directions are not instabilities | slice proof | seven dimension/action rows plus raw-vector residuals | zero-mode overcount |
| the evidence carrier is exact | contract theorem | duplicate-reject parser, exact key/type/order/uniqueness checks | repaired-hash schema bypass |
| finite evidence is not an all-`N` proof | theorem/evidence separation | explicit nonclaim and release gate | proof by enumeration |

## Frozen finite domain

- Mode grid: every `N=3,...,64` and every `m=0,...,N-1`, totaling 2,077
  exact integer cells.
- Polygon grid: 62 complete stability summaries.
- Scale grid: `N in {3,7,8,16}`,
  `Gamma in {1/2,1,2,5}`, `R in {1/2,1,2,4}`, totaling 64 rational cells.
- Slice grid: `N in {3,4,6,7,8,16,64}`, totaling seven exact dimension and
  first-harmonic-frequency rows.
- Boundaries: `N<3`, `R=0`, `Gamma=0`, `Gamma<0`, `m=0`, first harmonic,
  heptagon degeneracy, and `R->infinity`.

## Independent implementations

The producer uses only the proved integer formulas.  The checker does not call
producer functions: for every `N=3..64` it constructs the raw Cartesian
`2N by 2N` pair Hessian, verifies equilibrium and symmetry, rotates every
block to local coordinates, verifies block circulancy, performs the DFT, and
checks explicit rotation, scale, translation, and centered first-harmonic
vectors against the raw Hessian and Hamiltonian linearization.  The SymPy
audit independently differentiates and transforms exact raw Hessians for
`N=3,4,6`, verifies the same slice actions, and obtains every root sum by
coefficient counting rather than inserting its closed value.

## Commands

```bash
python -B code/c284_point_vortex_producer.py
python -B code/c284_point_vortex_checker.py
python -B code/c284_point_vortex_sympy_crosscheck.py
python -B code/c284_point_vortex_replay.py
python -B code/c284_point_vortex_mutation.py
python -B code/c284_release_manifest.py
```

`PYTHONDONTWRITEBYTECODE=1` is used in the release run.  The release gate also
performs two fresh LuaLaTeX builds of each of the three manuscript rounds.

## Pass conditions

- canonical sorted JSON with valid payload hash and a duplicate-reject loader;
- exact top, nested, and row key sets; strict scalar/container types; ordered
  complete row coverage; and unique semantic row keys;
- 65,655 independent assertions;
- 4,585 exact symbolic identities;
- both fresh evidence paths byte-identical to the archive;
- all 76 repaired-hash, stale-hash, raw-duplicate, and nonstandard-constant
  mutations rejected;
- three distinct archived PDF hashes, two fresh builds per round, embedded and
  subset fonts, warning-free settled logs, extractable text, and visual pass;
- exactly 27 payload files plus the self-excluded release manifest.
