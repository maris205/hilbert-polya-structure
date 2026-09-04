# Test report

## Exact lanes

- Producer: PASS — 2,048 classical cells, 8,385 state labels, 129 levels,
  512 revival controls, and six boundary rows.
- Independent checker: PASS — reconstructed the full artifact without
  importing producer code.
- SymPy verifier: PASS — 1,404 exact symbolic checks, including 81 Jacobi
  differential equations and 27 direct physical radial-operator
  substitutions.
- Isolated replay: PASS — two fresh outputs of 7,013,177 bytes, both
  byte-identical to the canonical evidence.
- Hostile mutation: PASS — 75 of 75 attacks rejected, including 58 attacks
  with all declared evidence hashes repaired and two unescaped TeX-spacing
  attacks; four legal spacing controls were accepted.
- Unittest smoke suite: PASS — 3 tests.
- Optimized-mode refusal: exercised by the release gate for `-O` and `-OO`
  across all six executable scripts.

## Serialization and evaluator locks

- JSON duplicate keys and nonfinite constants are rejected.
- YAML duplicate and non-string keys, merges, anchors, aliases, implicit
  timestamps, unknown fields, type changes, theorem status, tuple, domain,
  artifact, and Route-B changes are rejected.
- Evaluation raw SHA-256:
  `e093905d686c2d32e46cbaa8d711f61c460f21c35f79106be778d222fa85a541`.
- Evaluation semantic SHA-256:
  `daae2b83c7c1e7cdbc54ec7751e699d04dd9781854403de19364305fc63c13f5`.
- Evaluator SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Mathematical boundaries tested

- positive classical coupling versus nonnegative quantum coupling;
- turning polynomial, root discriminant, action recovery, Hamiltonian
  inversion, signed frequencies, and period lock;
- circular, meridional, north-equilibrium, incomplete classical zero-coupling,
  and Dirichlet quantum zero-coupling faces;
- Jacobi equation, Friedrichs exponent, energy, admissible labels,
  multiplicity, flat limit, and Dirichlet-hemisphere limit;
- rationality necessity, minimum revival multiplier, every consecutive phase
  gap, and the exactly-one global phase;
- unescaped `quad`/`qquad` rejection without false rejection of legal
  `\quad`/`\qquad` or ordinary words beginning with `quad`;
- theorem status, collision ownership, Route-A tuple, scope flags, and Route-B
  lock.

All lanes use ordinary Python. Finite checks remain regression evidence only.
