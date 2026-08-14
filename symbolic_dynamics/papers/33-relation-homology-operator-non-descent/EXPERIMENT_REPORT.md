# Experiment Report — Paper 33 / SD-C35

## Status

The canonical experiment is `PASS` for the negative obstruction claim and
`STOP` for the positive Route-A candidate.  The strict route tuple is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

The overall verdict is `ROUTE_A_REJECTED`; Route B is false/locked; the branch
action is `CLOSE_SEMIRING_RESIDUE_FAMILY`.

## Canonical pipeline

The 00:58 pre-firewall files were discarded as canonical evidence.  The final
pipeline was preregistered in `experiments/EXPERIMENT_PLAN.md` and physically
separates:

```text
cycle_quotient_core.py
  -> source_generator.py
  -> audit_source_separation.py
  -> post_census_classifier.py
  -> independent_evaluator.py
  -> run_tests.py
```

`cycle_quotient_core.py` and `source_generator.py` contain no arithmetic class
identifier detected by the AST firewall.  Arithmetic labels are appended only
after the raw 191-row census is complete.  The evaluator imports none of the
candidate, generator, prototype-runner, or classifier modules and independently
rebuilds all finite objects.

The immutable prototype bridge is:

| Artifact | SHA-256 |
|---|---|
| research core | `3843f0871278c0c2544494be3fff1bca1def98bfb6b870141812fd90b8897168` |
| research runner | `03e840f8941e69220a467fa106a55939529bd1adbe1b2fe2d2e67d2fb1887335` |
| eight-payload aggregate | `c5c5f34673590f98e89e6229354a8dc8fc851677c7af8702d4bf54a87e8037d4` |
| prototype tests | 25/25 |

## Raw comparison table

The independent evaluator rebuilt the projective states, `S/R` maps, orbit
partitions, relation and augmented ranks, cusp counts, post-census labels, and
residual flags for every modulus.

| Stratum | Blocks | Relative nonzero | Cuspidal nonzero | Relative Betti mean ± population std | Range | Cuspidal Betti mean ± population std | Range |
|---|---:|---:|---:|---:|---:|---:|---:|
| prime | 43 | 43 | 38 | 14.2093 ± 9.5979 | 1–33 | 13.2093 ± 9.5979 | 0–32 |
| prime-power composite | 14 | 14 | 9 | 13.5000 ± 10.2313 | 2–33 | 5.8571 ± 6.6101 | 0–18 |
| mixed composite | 134 | 134 | 130 | 29.8060 ± 15.8559 | 3–73 | 22.8955 ± 13.9884 | 0–58 |

The machine-readable table is `results/evaluation_comparison.csv`.

## Exact control ledger

| Metric | Canonical result |
|---|---:|
| moduli `2,...,192` | 191 |
| relative quotient nonzero | 191/191 |
| prime / prime-power / mixed survivors | 43/43, 14/14, 134/134 |
| relative Betti sums by stratum | 611, 189, 3994 |
| cuspidal nonzero by stratum | 38, 9, 130 |
| universal cusp return | 191/191 |
| inherited adjacency descends | 0/191 |
| matched opaque relabel exact | 191/191 |
| random relation controls killed | 64/64 |
| random controls residual nonzero | 64/64 |
| random residual Betti sum / range | 251 / 1–9 |
| cross graph Betti before filling | 31 |
| diamond boundary rank | 31 |
| cross `H1` after filling | 0 |
| source-only self-checks | 21/21 |
| prototype-compatible checks | 25/25 |
| independent low-level reconstruction | 8349/8349 |
| authority unit/integration assertions | 1932/1932 |
| fresh canonical double-run payloads | 20/20 byte-identical |

The cusp generator sequence is `R` then `S`; under the right-to-left operator
convention the operator word is `SR`.

## Complete character firewall

Cycle relator words and Manin chain-norm polynomials are recorded separately.

| Character family | Identity-word cancellation | Both chain norms vanish | Universal cusp weight nonzero |
|---|---:|---:|---:|
| six honest characters | 0/6 | 2/6 | 6/6 |
| fifteen zero-superdimension differences | 15/15 | 2/15 | 15/15 |

Thus honest characters can annihilate both chain polynomials in two cases;
the obstruction is that every such cancellation regime still retains the
universal cusp class.

## Reproducibility and integrity

- Two new temporary directories ran the entire lock -> source -> separation
  -> classification -> evaluation -> test pipeline independently.
- All 20 canonical payloads and all six stage stdout streams were identical
  across both runs and to the frozen authority copy.
- `freeze_artifacts.py` and `audit_artifact_integrity.py` are byte-idempotent
  across consecutive executions.
- `results/SHA256SUMS.txt` is a paper-root-relative 40-entry ledger covering
  12 Python source files, 7 experiment-control files, and 21 generated result
  payloads.
- The integrity audit verifies the frozen SHA ledger; the source-separation
  certificate, independent evaluator, unit tests, double run, and paper
  manifest cover the remaining source/provenance boundaries.
- No target-zero data or Route-B object is present; every zero-fit field is
  `not_applicable`.

## Findings

1. **Observation:** all 148 composite blocks retain relative homology, and all
   191 blocks carry the concrete cusp survivor.
   **Interpretation:** the quotient removes presentation-generic relations,
   not composite residue blocks.
   **Implication:** A1 is refuted before roofs or analytic continuation.
   **Next step:** do not add a field projector; it is the forbidden terminal
   selector.

2. **Observation:** the 31 independent cross cycles are exactly spanned by the
   31 diamond boundaries, leaving cross `H1=0`.
   **Interpretation:** diamond filling erases the only cross-modulus linkage.
   **Implication:** the quotient leaves a blockwise ledger rather than a linked
   prime family.
   **Next step:** stop further diamond variants in this source family.

3. **Observation:** the inherited adjacency fails quotient descent on 191/191
   tested blocks, with the exact rank jump already at `n=2`.
   **Interpretation:** a scalar homology determinant would replace the clock
   rather than inherit the graph step.
   **Implication:** A2 is refuted for the quotient even though the unquotiented
   Paper-32 operator independently owns a Fredholm determinant.
   **Next step:** require marker-preserving operator descent at the start of
   any future homological candidate.

4. **Observation:** all 64 generic transitive `C2*C3` controls reproduce
   relation cancellation and nonzero residuals.
   **Interpretation:** the mechanism is presentation topology rather than a
   field-specific arithmetic effect.
   **Implication:** the candidate proves too much; adversarial risk is
   `REALIZED` and the verdict is `STOP_PROVES_TOO_MUCH`.
   **Next step:** first consolidate this inside Symbolic Dynamics as a
   recognition-to-recurrence obstruction theorem.  An `ax+b`/Bost--Connes
   system can serve later only as a source-locked symbolic coding benchmark,
   not as the next primary route.
