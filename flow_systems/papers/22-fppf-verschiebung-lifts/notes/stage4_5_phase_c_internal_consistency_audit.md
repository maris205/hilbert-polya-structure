# P22 Stage 4.5 Phase C and internal-consistency audit

Audit date: **2026-08-25 UTC**  
Mode: **Stage 4.5 / Mode 2 / fresh full check**  
Exact manuscript SHA-256:
`2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2`

## Phase C result

| Surface | Registered population | Result | Evidence boundary |
|---|---:|---|---|
| C1 statistical/data values | 0 | **NOT APPLICABLE** | The scan found no empirical result, dataset, sample-size, p-value, effect-size, confidence-interval, simulation-result, ablation, seed, or participant surface. Mathematical indices and ring equations are proof content, not statistical data. |
| C2 internal consistency | 16 families | **PASS WITH TWO MINOR ISSUES** | Fourteen families agree; the two frozen Stage 3-prime issues remain present and are listed below. |
| C3 figures/tables/captions | 0 figures, 0 tables, 0 captions | **NOT APPLICABLE** | The source scan found no `figure`, `table`, `tabular`, `includegraphics`, or caption surface; no Figure Package is required. |
| C4 experiment declaration/provenance | 1 passport declaration; 0 experiment-backed claims; 0 provenance rows; 0 alignment rows | **PASS** | `no_experiments_declared` was explicitly supplied by the scholar; declaration/provenance symmetry lint exits 0, and the current manuscript contains only the negative declaration “No empirical data were generated or analyzed.” |

Required C4 boundary statement:

> This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

The explicit no-experiment declaration is retained from the scholar's
Stage-2.5 event; Stage 4.5 freshly checks it against the current manuscript
and current passport rather than inferring it from theoretical prose.

## C2 consistency families

| Family | Fresh Stage 4.5 finding |
|---|---|
| English abstract -> Theorems 1.1/1.2 | PASS: both state no additive lift for every `N>1`, separately for fppf and finite-flat sites. |
| Chinese abstract -> English abstract | PASS: topology, all-index nonlift, root-cover detector, and Ext consequence agree. |
| `N=1` control -> conclusion | PASS: identity lift is retained and not blended with the nontrivial indices. |
| Decomposition `N=q^a d` -> proof | PASS: characteristic, roots of unity, `d<N`, and truncated detector roles remain consistent. |
| Root cover -> both sites | PASS: finite-free faithful flatness is used separately for fppf and the stated finite-flat topology. |
| Overlap specialization -> kernel witness | PASS: `s_1 -> epsilon`, `s_2 -> 0`, `epsilon^N=0`, and `q^a y^sharp != 0` occur in the same direction. |
| Big-Witt detector -> torsion-freeness | PASS: the inner section is detected before multiplication; torsion-freeness then detects its multiple. |
| Extension class -> topology index | PASS: `K_tau`, `e_tau`, and `Ext^1_{Ab(C_tau)}` are consistently indexed. |
| Concrete nonlift -> Ext criterion | PASS: the source section, selected target, and middle-object implication are explicit. |
| Deninger source correction | PASS: limited to version-1 Corollary 4.6, with Propositions 4.3/4.5 and Corollary 4.7 kept distinct. |
| Bounded literature search -> novelty wording | PASS: the 25-August search is explicitly bounded and disclaims global priority. |
| Conclusion -> stated limitations | PASS: additive sheaf lifts only; no nonlinear, derived, topology-changing, all-affine, or future-version claim. |
| Author metadata -> declarations | PASS: Liang Wang, affiliation/contact, contribution, no funding, and no competing interests match the explicit author events; no corresponding-author status is inferred. |
| Public manuscript -> anchored revision | PASS: deleting only whole-line block markers from the anchored revision yields the public source SHA exactly. |
| Draft chronology | **MINOR ISSUE `IL-MINOR-1` / frozen `NEW-1`**: `Draft of 24 August 2026` conflicts with the included search update completed 25 August 2026. |
| Materials availability | **MINOR ISSUE `IL-MINOR-2` / frozen `NEW-2`**: the declaration still leaves public-access status for later author confirmation. |

## Isolated source/PDF rebuild

The exact source and bibliography were copied to the isolated directory
`/tmp/p22-stage45-build.C5Sgwi` and rebuilt with LuaLaTeX, BibTeX, and two
final LuaLaTeX passes.  No repository artifact was promoted or overwritten.

| Metric | Fresh result |
|---|---:|
| pages / size | 13 / A4 |
| citation commands / bibliography entries | 21 / 3 |
| unresolved citations or references | 0 |
| overfull boxes / missing glyphs / fatal errors | 0 / 0 / 0 |
| embedded and subset font rows | 9/9 |
| pre-existing underfull notices | 2, both in the manually line-broken Chinese abstract |
| fresh PDF SHA-256 | `cd01954347c0b29356d3c5c23167211b678118acde96f3b1c5861870a5ace593` |
| fresh log SHA-256 | `df92e7e0bfd1137b95825ce6dcf50bf62dadf980b629fa80a6a7480fe05099c8` |

The fresh PDF is not expected to be binary-identical because the PDF embeds
build timestamps.  Its `pdftotext -layout` output is byte-identical to the
promoted Stage-4 PDF text; both extracted-text SHA-256 values are
`070afd082737f6cfa13de4bfec32b30607896e97e8f928ecd2094c8d401eaf0c`.

## Frozen Stage 3-prime issue disposition

Both frozen inputs are re-observed on the exact Stage 4.5 draft.  Neither is
resolved, contradicted, upgraded, or omitted:

- `NEW-1` -> `IL-MINOR-1`, open, correction recommended.
- `NEW-2` -> `IL-MINOR-2`, open, requires an author decision about public
  availability before wording can be finalized.

They do not create a SERIOUS or MEDIUM integrity finding, but they prevent a
literal zero-issue Stage-5 handoff under the stricter pipeline state-machine
boundary.  No correction is authorized by this audit.
