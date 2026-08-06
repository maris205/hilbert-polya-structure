# Code plan

No production implementation has been added yet. R000 may contain clearly
marked pilot code; R001 freezes the production interfaces and configs.

Planned modules:

| Module | Responsibility |
|---|---|
| `dependency_lock.py` | hash inherited artifacts and record environment/provenance |
| `symbolic_graph.py` | source-row/target-column SFT, cylinders, closed words, orientation tests |
| `basic_set.py` | R015 isolating neighborhood, local maximality, and dimension-theorem applicability preflight |
| `unstable_interval.py` | interval graph transform, positive adapted roof, Euclidean norm gauge, and coboundary bridge |
| `stable_angle.py` | Euclidean stable/unstable Jacobians, angle separation, and area-coboundary check |
| `one_sided_roof.py` | effective Sinai cohomology, cylinder intervals, tail bounds |
| `ruelle_matrix.py` | sparse \(m\)-memory matrices with interval weights |
| `certify_pressure.py` | real leading eigenvalue, pressure bounds, monotonic root bracket |
| `certify_dimension.py` | theorem applicability, stable-pressure reindexing, Bowen roots, and total Hausdorff-dimension certificate |
| `cycle_crosscheck.py` | independent primitive/repetition and matrix-trace checks |
| `certify_contour.py` | optional T6 contour and Rouché checker; disabled without theorem gate |
| `run_controls.py` | constant, finite-memory, flat, random, shuffled, and precision controls |
| `check_results.py` | schema and certificate verification independent of plotting |

Implementation rules:

- `symbolic_graph.py` and `cycle_crosscheck.py` must use independent word
  enumerators.
- A non-palindromic path test must fail if the adjacency matrix is transposed.
- Interval arithmetic must use documented directed rounding.
- Dense matrices are not materialized when a sparse cylinder graph suffices.
- Plotting code is not permitted to compute theorem-critical quantities.
- Prime tables, zeta/xi evaluations, and Riemann zeros are forbidden inputs.
- A complex determinant command refuses to run unless the T6 theorem flag,
  analytic-domain/closed-interior manifest, any continuation and pole ledger,
  and fixed-contour manifest are present.

Planned tests:

1. exact adjacency characteristic/determinant identity;
2. source-target orientation on non-palindromic words;
3. constant-roof pressure root;
4. exactness at the memory of a synthetic finite-memory potential;
5. periodic-sum invariance for adapted, Euclidean, and one-sided roof gauges;
6. interval containment under increased precision;
7. adapted-to-Euclidean norm coboundary, Euclidean angle coboundary, and
   matching Bowen roots;
8. isolating-neighborhood, local/compact-ambient applicability, stable-pressure
   reindexing, and dimension-theorem hypothesis checker;
9. independent cycle/matrix trace equality;
10. deterministic reproduction from an immutable config hash.
