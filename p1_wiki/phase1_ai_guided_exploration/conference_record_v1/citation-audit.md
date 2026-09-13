# Citation, claim, and provenance audit

## Scope

This audit applies to the conference-oriented Phase-I research record in [`latex/`](latex/).  It checks whether the external references are used for the bounded background claims they support, whether the local Phase-I claims are explicitly tied to the repository record, and whether the research-governance framework, roadmap, and prime-symbolic lineage have a stated provenance.  It does **not** independently prove any local mathematical result, establish a Route-A/Route-B pass, validate an AI system's capability beyond the cited setting, or supply peer review.

## Citation register

| Key in `references.bib` | What it supports in the paper | Scope limit |
| --- | --- | --- |
| `CMI2026` | RH is listed as unsolved by the Clay Mathematics Institute on the stated access date. | An official status page; not evidence for any candidate. |
| `Davies2021` | AI can assist human mathematical conjecturing and investigation in selected settings. | Does not show autonomous proof of RH. |
| `RomeraParedes2024` | Evaluator-coupled program search can generate constructions in constrained settings. | Does not validate a dynamical candidate without its own mathematical evaluator. |
| `Trinh2024` | The bounded IMO-AG-30 geometry result cited in the introduction. | Geometry benchmark only; not a general mathematical-reasoning claim. |
| `Hubert2026` | Reinforcement-learning search for Lean-verified proofs in a specialized olympiad-level setting. | Formal verification and target domain remain bounded. |
| `BerryKeating1999` | Hilbert--Pólya / spectral-asymptotic motivation. | Motivation, not a candidate-specific theorem. |
| `Connes1999` | Trace-formula and arithmetic context. | Context, not an endorsement of the present construction. |
| `Ruelle1976` | Standard dynamical-zeta context for expanding maps and Anosov flows. | Does not supply the required arithmetic source or quantum lift. |
| `PhaseIRepository` | The six-line record, local claims, stated gaps, provenance, and repository address. | A source-bound internal research record, not independent external verification. |

The bibliography includes the DOI or official page for every external source.  The GitHub record is cited in the paper and is printed as `https://github.com/maris205/hilbert-polya-structure`.

## Internal provenance register

| Material | Local source / identifier | Permitted use in this paper |
| --- | --- | --- |
| Historical Phase-I evidence corpus | Commit `419ee36c1e310469209f7b83c096ec8aea448386`, 2026-09-13 UTC | Bounded summaries in the evidence landscape and Appendix A; not a new proof audit. |
| Six-direction navigation and claim boundaries | [`p1_wiki/`](../../README.md) and the parent [internal paper package](../README.md) | Direct the reader to controlling source records and preserve non-transfer boundaries. |
| Prime-symbolic research genealogy | [`flow_systems/docs/prior_work/README.md`](../../../flow_systems/docs/prior_work/README.md) | Constrains candidate admission; it is not proof that the displayed lineage arrows are established mathematical implications. |
| Human-governed, AI-executed framework | Figure 1 and the paper-configuration record in this package | Author-proposed prospective governance framework: the mathematician owns research origin and scientific authority; a jointly drafted, human-approved `AGENTS.md` constrains bounded AI execution and requires a handoff. It does not show that historical Phase-I materials used one uniform agent protocol, nor that a workflow document is mathematical evidence. |
| Updated roadmap | [`assets/rh_roadmap.png`](assets/rh_roadmap.png), SHA-256 `f5e70c5120474702e4f0715bce90c7a88fd5936164594e8b37a2ee0993549d1d` | Author-proposed evidence-obligation / search map; not a progress dashboard or mathematical result. |

## Session-level source map

The generic PhaseIRepository bibliography key is a navigation citation, not a
replacement for the source records controlling individual summaries. The
following static map identifies the P1 Wiki entrypoint for every row in the
evidence landscape and Appendix A.

| Paper section / landscape row | Source-bound P1 entrypoint | Permitted summary use |
| --- | --- | --- |
| Early free exploration: zeta_mvp0 | [zeta_mvp0 conclusions](../../directions/zeta_mvp0/conclusions.md) | Local operator / relative-trace structures and the still-open endogenous prime-time bridge. |
| Logistic Dynamics | [Logistic conclusions](../../directions/logistic_dynamics/conclusions.md) | Same-object return--roof--transfer--Fredholm chain and its stated stopping boundary. |
| Hénon Dynamics | [Hénon conclusions](../../directions/henon_dynamics/conclusions.md) | Restricted periodic/geometric results and object-specific Route-A limits; not inherited credit. |
| Symplectic Map | [Symplectic conclusions](../../directions/symplectic_map/conclusions.md) | Scoped interfaces/diagnostics and NOT_APPLICABLE; neither a pass nor a failure. |
| Symbolic Dynamics | [Symbolic conclusions](../../directions/symbolic_dynamics/conclusions.md) | Exact finite-system work, process labels, and the missing geometric/analytic/operator bridge. |
| Flow Systems / P24--P28 | [Flow conclusions](../../directions/flow_systems/conclusions.md) | The P24--P28-bounded positive arithmetic A2 = 0/5, Route-B invocation = 0/5, and same-object ownership boundary. |

For theorem hypotheses, exact evaluators, frozen inputs, or canonical
manuscripts, follow the source links within those conclusion pages or the
historical [evidence map](../evidence-map.md). This paper does not turn a
navigation page into a replacement proof source.

## Claim discipline checked

- The abstract, introduction, figure captions, discussion, and end matter state that the paper does not prove RH or a Hilbert--Pólya realization.
- The AI background is intentionally limited to the cited task settings.  The paper does not claim that AI solved RH, solved an active Millennium Prize Problem, or replaces mathematical validation.
- `NOT_APPLICABLE`, internal process completion, scoped negative controls, and local results are not displayed as transferable Route credit.
- The Flow `positive arithmetic A2 = 0/5` and `Route-B invocation = 0/5` statement is explicitly restricted to P24--P28, rather than all continuous flows.
- The proposal for broader Round-2 search is a methodological recommendation from the record, not a theorem or empirical optimization result.
- The lineage requirement is stated as an admission and preservation ledger: a generic map, flow, trace formula, or operator that receives primes only after construction is an external control, not a main candidate.
- The new `GO`/`END`/`FORK`/`HOLD` labels are explicitly operational workflow dispositions in the proposed framework, not existing Route-A/Route-B verdicts or claims about the wording of every historical/current project protocol. A token/compute-budget stop is recorded as an operational boundary, not as a negative mathematical result.

## Build and rendering checks

The release-local build command is:

```bash
cd p1_wiki/phase1_ai_guided_exploration/conference_record_v1/latex
./build.sh
```

Closing checks should include a successful LuaLaTeX/BibTeX build, no undefined citation/reference warnings in `build/manuscript.log`, `pdfinfo manuscript.pdf`, a manual inspection of all rendered pages, and `git diff --check`.  Passing these checks establishes rendering and reference-resolution integrity only; it does not establish mathematical correctness or external scholarly validation.

## Verification record for the two-column v1 baseline

The following closing checks were run on 2026-09-13 UTC.

| Check | Command / method | Result |
| --- | --- | --- |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; tracked PDF is 8 pages. |
| Citation and cross-reference resolution | Inspect <code>latex/build/manuscript.log</code> for undefined citations/references and fatal errors | PASS: none found. |
| Bibliography processor | Inspect <code>latex/build/manuscript.blg</code> | PASS: no BibTeX warnings or errors. |
| PDF metadata | <code>pdfinfo latex/manuscript.pdf</code> | PASS: title, author Liang Wang, subject, A4 page size, and 8-page count present. |
| Page rendering | Render and inspect pages 1--8 | PASS: roadmap, evidence landscape, protocol, candidate card, appendices, and bibliography are legible; no clipped candidate-card rows remain. |
| Wiki links | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root | PASS: 19,261 local links in 2,306 Markdown files. |
| Asset identity | SHA-256 comparison against the Round-2 roadmap reference | PASS: both values are <code>f5e70c5120474702e4f0715bce90c7a88fd5936164594e8b37a2ee0993549d1d</code>. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Verification record for the framework and single-column revision

The following closing checks were run on 2026-09-14 UTC after the new Figure 1,
the governance-framework prose, and the single-column A4 conversion were
applied.

| Check | Command / method | Result |
| --- | --- | --- |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; tracked PDF is a 13-page single-column A4 document. |
| Citation and cross-reference resolution | Inspect <code>latex/build/manuscript.log</code> for undefined citations/references and fatal errors after the final pass | PASS: none found. |
| Layout diagnostics | Inspect the final log for <code>Overfull</code>, <code>Float too large</code>, and unprocessed-float warnings | PASS: none found. Two non-fatal underfull line-break diagnostics remain. |
| PDF metadata | <code>pdfinfo latex/manuscript.pdf</code> | PASS: title, author Liang Wang, subject, A4 page size, and 13-page count present. |
| Page rendering | Render and inspect pages 2--9 and the bibliography page | PASS: Figure 1 is the human-governed framework and appears before Figure 2 (the RH roadmap); the evidence landscape, candidate-engineering protocol, role table, candidate card, appendices, and bibliography are legible with no visible clipping. |
| Wiki links | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root | PASS: 19,261 local links in 2,306 Markdown files. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Release note

Before external circulation, repeat this audit on the release commit, freeze the repository with a tag or archival deposit, and replace the provisional funding and competing-interest text with the author's actual declarations.  A double-blind venue also requires a separately anonymized manuscript and repository link strategy.
