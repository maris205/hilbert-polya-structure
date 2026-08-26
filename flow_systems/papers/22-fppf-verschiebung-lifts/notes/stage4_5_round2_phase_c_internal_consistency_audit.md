# P22 Stage 4.5 Round 2 Phase C and internal-consistency audit

Audit date: **2026-08-25 UTC**  
Mode: **Stage 4.5 / Mode 2 / fresh full check after authorized correction**  
Exact public manuscript SHA-256:
`e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed`

## Phase C result

| Surface | Registered population | Result | Evidence boundary |
|---|---:|---|---|
| C1 statistical/data values | 0 | **NOT APPLICABLE** | Fresh scan found no empirical result, dataset, sample size, p-value, effect size, confidence interval, simulation, ablation, seed, or participant surface. Mathematical indices and ring equations are proof content, not statistical data. |
| C2 internal consistency | 16 families | **PASS (16/16)** | All registered families agree; both previously frozen MINOR issues are closed on the exact Round 2 bytes. |
| C3 figures/tables/captions | 0 figures, 0 tables, 0 captions | **NOT APPLICABLE** | No `figure`, `table`, `tabular`, `includegraphics`, or caption surface occurs; no Figure Package is required. |
| C4 experiment declaration/provenance | 1 passport declaration; 0 experiment-backed claims; 0 provenance rows; 0 alignment rows | **PASS** | `no_experiments_declared` was explicitly supplied by the scholar; fresh declaration/provenance symmetry checks both exit 0, and the manuscript retains the negative declaration “No empirical data were generated or analyzed.” |

Required C4 boundary statement:

> This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether an experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

The no-experiment declaration is carried from the scholar's Stage 2.5 event,
but this audit checks it afresh against the Round 2 manuscript and current
passport rather than inferring it from theoretical prose.

## C2 consistency families

| Family | Fresh Round 2 finding |
|---|---|
| English abstract -> Theorems 1.1/1.2 | PASS: both state no additive lift for every `N>1`, separately for the fppf and finite-flat sites. |
| Chinese abstract -> English abstract | PASS: topology, all-index nonlift, root-cover detector, and Ext consequence agree. |
| `N=1` control -> conclusion | PASS: the identity lift remains explicit and separate from nontrivial indices. |
| Decomposition `N=q^a d` -> proof | PASS: characteristic, roots of unity, `d<N`, and truncated detector roles agree. |
| Root cover -> both sites | PASS: finite-free faithful flatness is used separately for fppf and the stated finite-flat topology. |
| Overlap specialization -> kernel witness | PASS: `s_1 -> epsilon`, `s_2 -> 0`, `epsilon^N=0`, and `q^a y^sharp != 0` occur in the same direction. |
| Big-Witt detector -> torsion-freeness | PASS: the inner section is detected before multiplication; torsion-freeness then detects its multiple. |
| Extension class -> topology index | PASS: `K_tau`, `e_tau`, and `Ext^1_{Ab(C_tau)}` are consistently indexed. |
| Concrete nonlift -> Ext criterion | PASS: source section, selected target, and middle-object implication are explicit. |
| Deninger source correction | PASS: limited to version-1 Corollary 4.6, with Propositions 4.3/4.5 and Corollary 4.7 distinct. |
| Bounded literature search -> novelty wording | PASS: the 25-August search is bounded and explicitly disclaims global priority. |
| Conclusion -> stated limitations | PASS: additive sheaf lifts only; no nonlinear, derived, topology-changing, all-affine, or future-version claim. |
| Author metadata -> declarations | PASS: Liang Wang, affiliation/contact, contribution, no funding, and no competing interests match the explicit author events; corresponding-author status is not inferred. |
| Public manuscript -> anchored revision | PASS: deleting only whole-line block markers from Round 2 anchored revision SHA `a93b64f5...58a2` yields the exact public source. |
| Draft chronology | **PASS / `IL-MINOR-1` CLOSED**: displayed draft date and bounded update both read 25 August 2026. |
| Materials availability | **PASS / `IL-MINOR-2` CLOSED**: the text states an explicit author-owned “upon reasonable request” policy and makes no public-repository claim. |

## Integrity-correction replay

- Authorized patch SHA-256:
  `421e969a54bcd5a783faeab1485605533e4465bd8b7e4289cdf522de0770ebc0`.
- Exact targets: `IL-MINOR-1 -> B0005/replace_block` and
  `IL-MINOR-2 -> B0094/replace_block`.
- Authorization carrier validation: PASS.
- Apply report SHA-256:
  `88c2becd2a644537d3ba356f2b97eb9d3eecca00fdbab93713d02226e1b51765`.
- Apply result: 103/105 blocks byte-preserved, touched ratio `0.019`, no
  heading/section-count/structural flag.
- Continuous two-round evidence bundle validation: PASS.

The old phrases `Draft of 24 August 2026` and `public-access status must be
confirmed` occur zero times on the exact audit target. The authorized new date
and access policy each occur exactly where expected.

## Isolated source/PDF rebuild

The exact public source and bibliography were copied to
`/tmp/p22-stage45-r2-build.wqPfZ0` and rebuilt with LuaLaTeX, BibTeX, and two
final LuaLaTeX passes. No repository artifact was promoted from this isolated
check.

| Metric | Fresh Round 2 result |
|---|---:|
| pages / page size / file size | 13 / A4 / 152366 bytes |
| citation commands / bibliography entries | 21 / 3 |
| unresolved citations or references | 0 |
| overfull boxes / missing glyphs / fatal errors | 0 / 0 / 0 |
| embedded and subset font rows | 9/9 |
| underfull notices | 2, both in the manually line-broken Chinese abstract |
| isolated PDF SHA-256 | `ebc7d8b96080e2d6d455244e529d3af91a71654cbe8fc2f4d7a5ce521263d78a` |
| isolated log SHA-256 | `4e314c5d19b2cae6e78727378a0f255c7724c57baf6a21681745dce6f696c99d` |
| isolated/published extracted-text SHA-256 | both `5bdca519563858a0c084c2315f5f28d0132f0ad9b1459c07294953bfdab64c67` |
| promoted PDF SHA-256 | `20e2d14f5a9e46b7d4f5eafac6669032c72fc69367fdf902e54440816a4a3f04` |

The isolated PDF need not be binary-identical because build timestamps are
embedded. Its layout-preserving extracted text is byte-identical to the
promoted PDF text.

## Frozen issue disposition

- `NEW-1 -> IL-MINOR-1`: **closed and freshly verified**.
- `NEW-2 -> IL-MINOR-2`: **closed and freshly verified**.

No SERIOUS, MEDIUM, or MINOR Phase C issue remains. The materials sentence
places a practical retention/sharing obligation on the author; it does not
authorize sharing third-party full text and is not a hidden public-access
claim.
