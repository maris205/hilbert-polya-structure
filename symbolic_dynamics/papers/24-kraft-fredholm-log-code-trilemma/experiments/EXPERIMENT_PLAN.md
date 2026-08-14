# Exact Experiment Plan — SD-C26

## Frozen objective

Audit the finite-local-code, positive-scalar branch of the logarithmic prime
certificate program before any analytic completion. The experiment certifies
finite consequences of the theorem chain; the infinite noncompactness result
comes from proof, never from cutoff extrapolation.

## Claim-to-certificate matrix

| ID | Frozen audit | Exact success condition | Primary artifact |
|---|---|---|---|
| E1 | finite visible orbit separation | marked binary/Elias cycles have one `#`, zero cyclic collision, zero candidate target calls, and obey the finite-word capacity bound | `finite_code_counting.csv` |
| E2 | arbitrary positive roof allocation | equal, concentrated-positive, and hashed-positive allocations total one and satisfy the singular-value and AM--GM block-(S_1) bounds | `disjoint_cycle_witnesses.csv` |
| E3 | positive prime-only shared-vertex firewall | every distinct prime pair gives the exact (pq\ne r^m) obstruction | `shared_prime_pair_firewall.csv` |
| E4 | shared trie/renewal closure | every loop totals (log n), the whole concrete trie is noncompact, and every return length 2--5 has mixed primitives | `shared_trie_closure.csv`, `mixed_primitive_ledger.csv` |
| E5 | exact connected determinant | finite symbolic trie determinant equals (1-F), not the disconnected Euler product | `finite_trie_determinant_checks.json` |
| E6 | graph-step marker | every finite binary/Elias prime cycle has degree greater than one; only atom loops have degree one | `marker_firewall.csv` |
| E7 | arbitrary-inventory collapse | prime, composite, square, Fibonacci, matched random, matched hash, and decidable supports reproduce the same architecture gates | `arbitrary_inventory_controls.csv`, `diagonal_escape_controls.csv` |
| E8 | candidate-family controls | factorization renewal floods mixed connected cycles; finite-prefix S-adic compactness does not survive the stationary union | `factorization_renewal_controls.csv`, `finite_prefix_stationarization.csv` |
| E9 | finite roof inventory | distinct prime logs have the audited formal (mathbb Q)-rank and cannot lie in a smaller finite roof span | `finite_roof_inventory.csv` |
| E10 | integrity | strict Route tuple, schema, control characters, caches, two complete byte-identical runs, and SHA ledger all pass | `route_gate_summary.csv`, `double_run_certificate.json`, `integrity_audit.json`, `SHA256SUMS.txt` |

## Frozen protocol

- Cutoffs: (127,511,2047,8191).
- Visible codes: binary, Elias gamma, Elias delta, and framed binary, with one
  return marker over the fixed alphabet ({0,1,\#}).
- Roof allocations: equal, concentrated-positive, deterministic SHA-256
  positive shares.
- Real parts: (sigma=1,2).
- Trie cutoff: 127; primitive return necklaces through length five.
- Exact symbolic determinant: atoms (2,3,5,7), at (s=2).
- Controls: prime, composite, square, Fibonacci, matched-density seeded
  random, matched-density hash, and arbitrary decidable modular inventory.
- No target-zero data, root fit, GPU, network input, review loop, or Route-B
  object.

## Acceptance gates

1. all 35 tests pass;
2. every exact mismatch count is zero;
3. every finite witness is explicitly marked as non-proof of the infinite
   operator theorem;
4. the strict tuple is
   `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`;
5. overall verdict is `ROUTE_A_REJECTED` and Route B is false;
6. two complete generator/test/analysis runs are byte-identical;
7. all CSV, JSON, YAML, LF, control-character, cache, schema, and SHA checks
   pass with pending two-stage provenance.

## Reproduction

```bash
python experiments/run_sdc26_exact_suite.py
```

The canonical runner disables bytecode and pytest caches, fixes
`PYTHONHASHSEED=0`, and compares complete code/result snapshots before
integrity and SHA finalization.

## Scope firewall

Passing E1--E10 supports only positive scalar stationary simple graphs with a
finite orbit-separating local code, additive roof, and natural counting-space
adjacency. It does not rule out signed/matrix cancellations, infinite local
alphabets, nonlocal completed-orbit weights, anisotropic spaces, or all
countable/S-adic systems.

