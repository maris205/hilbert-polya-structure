# Canonical Experiment Plan — Paper 33 / SD-C35

**Freeze date:** 2026-08-15 UTC

**Status at freeze:** this plan supersedes the 00:58 pre-firewall experiment
outputs.  Those files are implementation scaffolding only.  No authority
result produced before this plan is canonical.

## 1. Claim and decision target

Reproduce the final research-stage relation-homology obstruction on the exact
Paper-32 projective-residue object.  The experiment audits implementation and
controls; the infinite rank, cusp-survivor, diamond-contractibility, and
operator-non-descent statements remain theorem-backed.

The positive candidate stops if any composite residual, generic-action
residual, cross-linkage collapse, or inherited-operator non-descent occurs.
The negative paper succeeds only if every preregistered exact check passes.

## 2. Prototype bridge lock

The authority implementation must bridge exactly from the final `/tmp`
prototype:

| Prototype artifact | Frozen SHA-256 |
|---|---|
| `cycle_quotient_core.py` | `3843f0871278c0c2544494be3fff1bca1def98bfb6b870141812fd90b8897168` |
| `run_prototype.py` | `03e840f8941e69220a467fa106a55939529bd1adbe1b2fe2d2e67d2fb1887335` |
| prototype payload ledger | `c5c5f34673590f98e89e6229354a8dc8fc851677c7af8702d4bf54a87e8037d4` |
| prototype stdout | `fbe2401157055ecdabd41190ea0372bd7228c60d90f812dc955632cb3d107cd4` |

Required prototype semantics are 25/25 checks and the complete character
firewall `0/6, 2/6, 15/15, 2/15`, with every one-dimensional cancellation
case retaining the universal cusp class.

## 3. Information firewall and physical separation

The code is split into four canonical processes plus one immutable bridge:

1. `cycle_quotient_core.py`: source construction and exact source invariants;
   no arithmetic class labels, target zeros, or accepted-support data.
2. `source_generator.py`: source-only generator; writes raw census/control
   payloads without prime/composite labels.
3. `post_census_classifier.py`: reads the completed raw census and appends
   arithmetic labels only after all source invariants are frozen.
4. `independent_evaluator.py`: independently recomputes labels and aggregate
   checks from CSV/JSON payloads; it imports neither the core nor the
   classifier.

`generate_results.py` is retained byte-for-byte at prototype SHA
`03e840...` only as a bridge witness.  It is never invoked by the canonical
pipeline because the research prototype combined generation with post-census
reporting.

No component may use target-zero data.  The classifier and evaluator may not
alter source invariants.

## 4. Frozen parameters

```text
moduli:                  2,...,192
coefficient audit:       F_1000003
matched relabel seed:    1003003+n
random controls:         64
random seeds:            330000,...,330063
random sizes:            12,18,24,30,36,42,48,60,72 cyclically
cross multipliers:       2,3
honest characters:       all 6 characters of C6
virtual differences:     all 15 unordered distinct pairs
target-zero data:        none
Route B:                 false / locked
```

The generator sequence is always stated as `R` then `S`; under the
right-to-left operator convention the corresponding operator word is `SR`.

## 5. Must-run milestones and success criteria

### M0 — preregistration and source firewall

- This plan must exist before canonical outputs.
- Core SHA must equal the prototype bridge lock.
- Core source-oracle scan must have zero forbidden-token hits.
- No Python cache, CRLF, trailing whitespace, or non-single-LF EOF may remain.

### M1 — exact source generation

- 191 raw modulus rows covering exactly `2,...,192`.
- Every row satisfies the orbit-rank formula and the `R`-then-`S` cusp return.
- Inherited adjacency descends on 0/191 blocks.
- 191/191 opaque relabels transport rank and quotient dimension exactly.
- 64/64 random transitive `C2*C3` controls kill the presentation relations
  and retain nonzero residual homology.
- Cross graph Betti number 31, diamond-boundary rank 31, filled `H1=0`.

### M2 — post-census classification and character firewall

- Independent arithmetic strata: 43 primes, 14 prime-power composites, and
  134 mixed composites.
- Relative quotient nonzero on 43/43, 14/14, and 134/134 respectively.
- Honest characters killing identity cycle words: 0/6.
- Honest characters killing both Manin chain norms: 2/6.
- Virtual differences killing identity-word supertraces: 15/15.
- Virtual differences killing both chain norms: 2/15.
- All 6 honest character weights and all 15 virtual differences have nonzero
  weight on the universal cusp class.

### M3 — independent evaluation and tests

- Source-only generator self-tests: 21/21.
- Post-classifier prototype-compatible checks: 25/25.
- Authority unit/integration tests recompute every block/control and pass.
- Independent evaluator checks arithmetic labels without importing candidate
  code and reports all checks passing.
- Target-zero fields remain exactly `not_applicable` and
  `target_zero_data_used=false`.

### M4 — fresh double run and integrity

- Two fresh temporary runs execute the complete source-generator -> classifier
  pipeline independently.
- Every primary payload and stdout is byte-identical between runs and matches
  the frozen authority payload.
- Re-running classifier, evaluator, freeze, and integrity audit is idempotent.
- `SHA256SUMS.txt`, aggregate digest, inventory, double-run certificate, and
  integrity audit agree.
- The frozen paper-root ledger hashes 40 entries: 12 Python source files,
  7 experiment-control files, and 21 generated result payloads.  The
  double-run certificate compares 20 source-separated payloads against the
  frozen authority copy.
- A cold-start audit begins with an empty result directory, reruns all six
  canonical stages to regenerate 20 payloads, adds the frozen 20/20
  double-run certificate as payload 21, creates all five meta-integrity files,
  and ends with the exact 21+5 result set.
- The five self-referential meta-integrity files are excluded from
  `SHA256SUMS.txt`; the strict audit validates their structure and agreement
  directly, and the later paper manifest binds them externally.

## 6. Strict Route-A v0.2 freeze

```text
A0 evidence_status = PROVED
A1 evidence_status = REFUTED
A2 evidence_status = REFUTED
A3 evidence_status = STOP_SCOPED
A4 evidence_status = STOP_SCOPED
proves_too_much_risk = REALIZED
adversarial verdict = STOP_PROVES_TOO_MUCH
route tuple = (A0_STRUCTURAL_ARITHMETIC_RELATION,
               A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
```

Commit metadata is intentionally outside this canonical experiment plan.  The
Route-A card and paper manifest bind `source_commit`, `code_commit`, and the
paper artifact commit after the corrective artifact commit exists.  This plan
therefore carries no future commit hash and avoids a circular
plan -> result-lock -> commit -> plan dependency.

## 7. Required reports

- Machine-readable raw and labelled tables in `results/`.
- Independent evaluation and exact comparison table in `results/`.
- Human-readable raw table, findings, implications, and stop decision in
  `EXPERIMENT_REPORT.md`.
- Canonical Route-A card in `evaluations/route_a/SD-C35/2026-08-15.yaml`.
