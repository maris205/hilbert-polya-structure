# P22 Stage 4.5 E1.1 coverage adjudication

Audit date: **2026-08-25 UTC**  
Mode: **Stage 4.5 / Mode 2**

## Deterministic receipt

- Exact draft SHA-256:
  `2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2`
- Claim Registry: `49` rows, all `selection_tier=ALL`, semantic/model-mediated.
- Claim Registry SHA-256:
  `b5a62ee06844eff8c5f5aeec6fb73090cef998373d73c64917cd9f237cb81954`
- Coverage report SHA-256:
  `7da7d0b6c1f1f4696928f6789fda818cac1b75266b253aa0d53d48779b9f0bee`
- Coverage build: PASS.
- Exact-input `--validate-report` replay: PASS.
- Mechanically enumerated candidates: `10`.
- Exact registry-span matches: `4`.
- Raw `candidate_unregistered_count`: `6`.
- Required semantic boundary:
  `semantic_extraction_coverage=not_machine_detectable`.

The six raw gaps were returned to semantic E1 inspection.  None is silently
converted into a claim, and the raw gap count remains unchanged in the
machine report.

## Candidate-by-candidate adjudication

| Candidate | Mechanical trigger | Adjudication | E1 action |
|---|---|---|---|
| `CAND-B1247-1285-b58ab8f3d8a0` | `[1]` inside `\newcommand{\latin}[1]...` | LaTeX macro parameter, not a citation or factual claim | Do not register |
| `CAND-B1406-1448-30fadd0d5d3a` | `[1]` inside `\newcommand{\angles}[1]...` | LaTeX macro parameter, not a citation or factual claim | Do not register |
| `CAND-B29439-29511-ed18240064a7` | `d-1` inside a line-fragment beginning `\(X^d-1\)` | Sentence splitter stopped at a physical LaTeX line; incomplete fragment rather than an independent claim | Broader mathematical claim already inspected in registered proof rows; do not fabricate a fragment claim |
| `CAND-B29942-30017-3842672614e1` | lexical `N=1` across `1-\varepsilon^NT^N=1` | Formula/line fragment; detector reads an equality endpoint as a parameter assignment | Exact displayed equality is already registered as `P22-E1-38`; do not add a duplicate fragment |
| `CAND-B33390-33401-40d8fe02841a` | `N=1` in `If \(N=1\),` | Incomplete conditional fragment produced at a comma | Full control claim is registered as `P22-E1-24`; do not register the fragment |
| `CAND-B42921-42993-14398d21a345` | `N=1` in the conclusion control sentence | Sentence splitter stopped at a physical line boundary | The full control is semantically inspected through `P22-E1-24`, `P22-E1-30`, and the conclusion rows; do not register a partial duplicate |

The four clean mechanical matches are `P22-E1-24`, `P22-E1-37`,
`P22-E1-38`, and `P22-E1-39`.  A clean bounded candidate replay does not
prove that every substantive claim was extracted; conversely, an adjudicated
lexical false positive is not evidence that the semantic registry is complete.
