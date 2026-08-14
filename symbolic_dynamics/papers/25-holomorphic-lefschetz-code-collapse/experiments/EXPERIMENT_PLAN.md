# Exact Experiment Plan — SD-C27

## Frozen objective

Test whether the canonical holomorphic (0|1) de Rham grading repairs the
all-repetition stability denominator of logarithmic-code branches, then audit
the arithmetic ceiling of that repair in shared and disjoint recurrence.

## Claim-to-certificate matrix

| ID | Frozen audit | Exact success condition | Primary artifact |
|---|---|---|---|
| E1 | Elias gamma source registry | all 4,095 branches obey the code-length and derivative formulas, common compact containment, and one inventory-independent prefix-free registry | `code_registry.csv`, `prefix_free_certificate.json` |
| E2 | scalar first-trace fit | (alpha=1-q) matches (r=1) and fails every audited (r=2,ldots,6) exactly | `scalar_power_rigidity.csv` |
| E3 | ordinary matrix firewall | required determinant is ((1-t)/(1-qt)), has a genuine pole, and the exact two-dimensional moment control fails at (r=3) | `ordinary_matrix_firewall.json` |
| E4 | exact de Rham complex | (DM_0=M_1D), all supertraces through (r=8) equal ((sum w)^r), and the characteristic quotient is exact | `de_rham_chain_checks.csv`, `de_rham_power_supertraces.csv` |
| E5 | local all-order determinant | every centered finite product telescopes to (1-zw) | `local_determinant_telescoping.csv` |
| E6 | determinant ownership | ordinary block product differs from the graded ratio in every fixture | `ordinary_block_graded_firewall.csv` |
| E7 | shared versus disjoint | on the first four atoms of each finite inventory fixture, shared gives (1-zsum w), disjoint gives (prod(1-zw)), with exact all-power mixed residuals | `shared_disjoint_determinants.csv`, `shared_disjoint_power_ledger.csv` |
| E8 | primitive mixed ledger | enumerate every primitive necklace on two, three, and four labels through length six; every mixed row survives the de Rham grading | `primitive_necklace_ledger.csv` |
| E9 | arbitrary inventories and ownership | all seven inventories receive the same compiler; digit marker retains (u^{\ell(n)}); the trace-class/cohomology domain remains explicit | `arbitrary_inventory_controls.csv`, `marker_ownership_controls.csv`, `nuclearity_domain_ledger.csv` |
| E10 | reproducibility and Route | exact tests, fresh byte-identical double run, integrity, control characters, schema, and SHA ledger all pass | `test_summary.json`, `double_run_certificate.json`, `integrity_audit.json`, `SHA256SUMS.txt` |

## Frozen protocol

- Code range: (2le nle4096).
- Scalar rigidity: (2le nle512), powers one through six.
- Polynomial complexes: degrees two through five; local spectral truncations
  additionally use degrees one and eight.
- De Rham power traces: one through eight.
- Inventory cutoffs: 31, 127, 511. The determinant/all-power fixture takes the
  first four atoms at each cutoff; the arbitrary-inventory control separately
  records the exact full-inventory sum and product at (z=1).
- Primitive necklaces: two, three, and four labels, lengths one through six.
- Weights in exact polynomial certificates: (w_n=n^{-2}).
- Inventories: primes, squares, Fibonacci, all integers, matched seeded
  random, matched hash, and arbitrary decidable modular support.
- Main calculations use exact integers, fractions, rational matrices, and
  polynomials; no floating-point calculation decides a claim.

## Acceptance gates

1. every exact residual required to vanish is zero;
2. scalar (rge2) residuals and all ordinary/graded ownership comparisons
   required to differ are nonzero;
3. all mixed primitive necklaces survive shared recurrence;
4. every arbitrary-inventory row has zero selectivity credit and is labeled
   `PROVES_TOO_MUCH`;
5. strict tuple:
   `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`;
6. overall `ROUTE_A_REJECTED`, Route B false;
7. two complete runs byte-identical, integrity true, and SHA ledger verified.

## Reproduction

```bash
python experiments/run_sdc27_exact_suite.py
```

## Scope firewall

The ordinary tensor-fiber no-go is not generalized to all nontensor nuclear
operators. The successful determinant is a graded ratio of two ordinary
degreewise determinants, not an ordinary ungraded block determinant. Return
time and digit time remain different marked objects.
