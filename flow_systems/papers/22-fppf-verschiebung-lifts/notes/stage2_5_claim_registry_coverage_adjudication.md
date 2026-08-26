# P22 Stage-2.5 claim-registry coverage adjudication

Date: **2026-08-24**  
Exact draft SHA-256:
`5976642a43907a3e01abdb586e9188c697d4a07e7137330a8f285538caaa02fc`

## Result

- Semantic E1 population: **39 registered material claims**.
- Risk-stratified Phase-E selection: **17/39**, consisting of every claim
  classified `HIGH-IMPACT`; no random/top-up row was required because the
  high-impact set already exceeds the Mode-1 minimum of 10.
- Shared evidence rows: **26**, covering **17/17 selected claims**.
- Claim verdicts: **17 VERIFIED, 0 distorted, 0 unverifiable**.
- Deterministic coverage build and exact-input replay: **PASS**.

The supplied lexical detector is Markdown-oriented: it does not recognize
LaTeX `\cite` commands, and it applies statistical regular expressions to raw
TeX source.  Its report therefore remains an auxiliary lower-bound check;
`semantic_extraction_coverage=not_machine_detectable` is retained exactly as
emitted by the tool.

## Six mechanically unregistered candidates

The deterministic tool emitted six open candidates after exact-span joining.
All six were reviewed against the raw source and are lexical false positives
or line-fragment artifacts, not omitted semantic claims.

| Raw line | Detector text | Adjudication |
|---:|---|---|
| 40 | `\newcommand{\latin}[1]{{\rmfamily #1}}` | `[1]` is a macro parameter, not a numerical citation. |
| 45 | `\newcommand{\angles}[1]{\langle #1\rangle}` | `[1]` is a macro parameter, not a numerical citation. |
| 615 | `\(X^d-1\): after ... all of its roots` | The detector reads the algebraic exponent expression as an effect-size trigger and truncates the prose at the physical line boundary; the complete roots-of-unity claim is registered in `P22-E1-20`/the Section-4 proof population. |
| 625 | `\(1-\varepsilon^NT^N=1\), placing ...` | A raw-line fragment of the already registered kernel calculation (`P22-E1-22` and exact formula `P22-E1-38`). |
| 688 | `If \(N=1\),` | An incomplete raw-line fragment; the complete control is exactly registered as `P22-E1-24`. |
| 896 | `The index \(N=1\) ... \(V_1\) is the identity` | A raw-line fragment repeating the exactly registered `N=1` control `P22-E1-24`. |

Four other quantitative-looking raw-LaTeX candidates were exactly joined to
registered spans (`P22-E1-24`, `P22-E1-37`, `P22-E1-38`, and `P22-E1-39`).
Every one of the manuscript's 18 LaTeX citation commands was separately
covered by the 100% citation-context audit; the lexical detector's inability
to parse `\cite` is not used to claim citation coverage.

## Artifact receipt

- `stage2_5_claim_registry.json`: semantic population and exact byte spans.
- `stage2_5_claim_registry_coverage.json`: deterministic lexical report.
- `stage2_5_evidence_rows.json`: shared evidence-row carrier.
- `stage2_5_build_evidence_artifacts.py`: mechanical builder and replay-source
  constructor.

This adjudication records model-mediated semantic review.  It does not turn
the lexical detector into a semantic completeness proof.
