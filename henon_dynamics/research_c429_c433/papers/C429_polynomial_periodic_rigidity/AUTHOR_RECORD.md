# C429 author baseline: preparation, sources, and real build record

Status: author-prepared manuscript baseline for two subsequent nonauthor manuscript reviews. This is not an independent manuscript review, external peer review, publication acceptance, final release, or a batch evaluation result. No review scores or fictitious review versions were created.

## Scope and files

The article is anonymous English `article`, 11 pt, letter paper with one-inch margins, modularized into seven section files. The approved shared `BATCH_PLAN.md` supplies its outline; no competing outline was introduced. The complete source entry point is `main.tex`, with `math_commands.tex` and six actually cited entries in `references.bib`.

The theorem concerns ordinary affine primitive cycles of `f(x)=x^d+c` over the algebraic closure of the prime field, for every prime, every integer `d >= 2`, and every coefficient `c`. It includes zero/constant observables, non-prime-field coefficients, and native periods divisible by the characteristic. The observable class remains polynomial. The finite bounds concern return levels and iterate degrees, not every unreduced test product, runtime, or an optimal cutoff.

The paper-plan and paper-write skills guided the theorem-first organization, contribution boundaries, and complete proof drafting. The paper-compile skill guided actual compilation and PDF checks. The task-specific anonymous mathematical-article instruction superseded the skills' old ML venue, page-limit, empirical-experiment, and external-model defaults. No manuscript text depends on a research-note hyperlink in place of a proof.

## Proof-to-manuscript map and author self-check

| Manuscript | Mathematical content and author check |
|---|---|
| Section 1; Theorems 1.1 and 1.2 | All-parameter rigidity; positive cap `M` including the zero input; full definitions of `F_j` and `H_j`; all three disjoint finite tests; both adjacent levels; ordinary-root equivalence; primitive-period and iterate-degree bounds. |
| Section 2; Lemmas 2.1–2.4 | Full normal-form proof and uniqueness modulo constants; full cyclic digit basis without squarefreeness; source-window leading-digit detector; multiplicity-safe Hasse certificate proved locally. Native repetitions use integer counting, not field division. |
| Section 3; Proposition 3.1 | Complete weighted one-circuit expansion, legal final source digit, carry bound, localization of every source, mutually inverse insertion/deletion with weight one, and the constant contribution. The general base is not asserted by analogy with base two. |
| Section 4 | Two Jacobians when the scalar difference is nonzero; derivative-zero/squarefree branch; constant elimination using adjacent levels; finite equivalence and the first explicit bound. |
| Section 5 | First nonlinear Hasse derivative, full marked-background identity, Frobenius on coefficients, legal target digits, adaptive cut and overflow exclusion, all-source localization, and common-cut path convention. |
| Section 6; Proposition 6.1 | Bijection for all old marks, new-mark reset, integer weighted loss identity, existence and uniqueness of the leading-source path, nonzero coefficient difference, constant elimination, remaining finite equivalence/bound, and explicit characteristic-two boundary. |
| Section 7 | Direct polynomial-shear identity; native lifted periods; proved all-level Jacobian blind-test example, clearly not a rigidity counterexample; scope and preparation disclosure. |

All ten mathematical source/BibTeX files were read back in full after drafting. The two modified heading lines were checked again after the only compiler-warning repair. The author's comparison found no missing central proof or unresolved mathematical dependency to declare; this does not substitute for the separate nonauthor reviews. Particular reviewer attention is invited to the adaptive-cut correspondence in Section 5 and the deletion/new-mark exhaustion in Section 6, the longest proof components.

## Local proof and planning provenance

All prior proof packages and source reports were read-only. `PROVENANCE_INPUTS.sha256` records 20 actual local inputs, including the three applicable `AGENTS.md` files, approved batch outline, outline review, admission decisions, proof packages, source reports, and the three selected skills plus writing-principles reference. Relative paths in that checksum file are relative to `henon_dynamics/research_c429_c433/`.

Principal proof inputs were the complete round-3 normal-form package, complete round-4 unicritical carry package, complete round-5 excluded-congruence package, and complete characteristic-two extension. The older C424–C428 base package was read in full; the round-2 older package was read for the required normal-form/leading-digit steps and Jacobian control, not represented as a fresh full read. The source comparison used the round-3 PC-L novelty/source records and round-4/round-5 A2 source reports. Admission Section 1, including all relevant extensions, was read; the full shared batch outline and its closed repair record were read.

## Actually checked external sources

Metadata was transcribed from original publisher/author/arXiv records during this author task, not guessed from citations in secondary pages. Bibliographic web checks were performed directly; no external model or bibliographic API was invoked. These references frame antecedents only: every algebraic ingredient used in the theorem is proved in the manuscript.

| BibTeX key | Original metadata and actually inspected scope |
|---|---|
| `kalinin2011livsic` | Boris Kalinin, Annals of Mathematics 173(2) (2011), 1025–1042, DOI `10.4007/annals.2011.173.2.11`, verified at the [publisher record](https://annals.math.princeton.edu/2011/173-2/p11). Theorem 1.1 and its compact-metric/transitive/closing/Hölder hypotheses were checked in the [author preprint](https://arxiv.org/html/0808.0350v2). No polynomial finite-characteristic specialization is claimed. |
| `cattani1996residues` | Eduardo Cattani, Alicia Dickenstein, Bernd Sturmfels, in *Algorithms in Algebraic Geometry and Applications*, Progress in Mathematics 143, Birkhäuser, Basel (1996), 135–164; editors Laureano González-Vega and Tomás Recio; DOI `10.1007/978-3-0348-9104-2_8`, checked at the [publisher chapter](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8). [Original preprint](https://arxiv.org/pdf/alg-geom/9404011), Section 4, supplies the normal-form/residue/Jacobian-trace comparison. Those classical results are credited, not transplanted analytically into characteristic `p`. |
| `cvitanovic1998beyond` | Predrag Cvitanović, Kim Hansen, Juri Rolf, Gábor Vattay, Nonlinearity 11(5) (1998), 1209–1232. Title/authors/pages were checked in the [author PDF](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf), DOI `10.1088/0951-7715/11/5/003` in the [arXiv record](https://arxiv.org/abs/chao-dyn/9712002). Section 4, equations (24)–(28), and its credit to Levin–Sodin–Yuditskii were read directly. The DOI/publisher opening itself failed; this is not represented as a successful publisher full-text read. |
| `levin1994ruelle` | G. Levin, M. Sodin, P. Yuditskii, *Ruelle operators with rational weights for Julia sets*, Journal d'Analyse Mathématique 63 (1994), 303–331, DOI `10.1007/BF03008428`; verified at the [publisher page](https://link.springer.com/article/10.1007/BF03008428). Only metadata and abstract were accessible. Original theorem/proof full text was not read and is not invoked. Its earlier matrix construction is attributed through the directly inspected 1998 article; this access limit also appears in Section 1.1. |
| `li2025ground` | Zhiqiang Li, Yiwei Zhang, Mathematische Annalen 391 (2025), 3913–3985, DOI `10.1007/s00208-024-03018-0`, checked at the [publisher](https://doi.org/10.1007/s00208-024-03018-0). Online publication was in 2024; the cited volume year is 2025. [Preprint](https://arxiv.org/pdf/2303.00514v2), Theorem 1.1, was read directly, including the distinct expanding-Thurston/PCF-rational-map settings and real Hölder regularity. |
| `zou2025finite` | Rui Zou, Hua Wei, Journal of Applied Analysis and Computation 15(4) (2025), 2185–2194, DOI `10.11948/20240420`, all verified from the [published PDF](https://www.jaac-online.com/data/article/jaac/preview/pdf/jaac-15-4-2185.pdf). Theorem 1.1's transitive Anosov, bounded Hölder norm, finite-data, approximate conclusion was read. The DOI resolver opening failed, while the actual published PDF was accessible. |

This is a bounded source comparison, not a worldwide-priority certification. The inaccessible 1994 full text is the one explicit bibliographic limitation; it is not an unproved premise of the article.

## Real compilation sequence

Both actual invocations used:

```sh
SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The shell used `pipefail` and `tee` to retain each actual transcript. Installed tools were used without installation: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian), latexmk 4.76, and BibTeX 0.99d.

| Actual attempt | Result and retained evidence |
|---|---|
| `build_attempts/01/` | Successful first latexmk invocation: 3 pdfLaTeX passes and 2 BibTeX passes; 16-page converged PDF, 423,845 bytes. Source was copied before invocation. PDF, full invocation log, final pass log, BibTeX output/log, auxiliary/output files, recorder, and latexmk database were saved before editing. Final-pass warnings: 6 hyperref PDF-string warnings from math in two headings, and 1 underfull bibliography line, badness 2173. Initial-pass unresolved labels/citations converged and are preserved honestly in `compile.log`. |
| `build_attempts/02/` | Successful real repair build: only the two Section 4 headings gained `texorpdfstring` alternatives; no theorem/proof content changed. 2 pdfLaTeX passes and 1 BibTeX pass. Converged PDF: 16 pages, 423,862 bytes. The same evidence and pre-invocation source snapshot were retained. This is a compiler-warning repair, not a manuscript-review round. |

The current `main.pdf` is attempt 02. Its SHA-256 is `118733318d139821d5cb29ab8deccc9d46fe577230563fbd38858df7ea431a02`. The first actual converged PDF remains in attempt 01, SHA-256 `09c65ef93ad4eb3c098df4c20c01f046e9f8ce9af41232b4051d179169dd9e0b`.

## PDF and warning checks actually performed

- `pdfinfo`: 16 pages, letter dimensions 612 by 792 pt, no encryption, no PDF JavaScript, anonymous author metadata. Fixed epoch was supplied as requested; metadata displays the corresponding instant in its recorded offset.
- `pdffonts`: all 25 listed font resources are embedded; no missing/nonembedded font was found.
- Final `main.log`: no LaTeX error, undefined reference/citation, multiply-defined label, overfull box, or hyperref warning. One underfull hbox remains, badness 2173, `main.bbl` lines 33–38, Li–Zhang entry.
- `pdftotext -layout`: no `??`, `[?]`, `[VERIFY]`, `TODO`, `TBD`, or `FIXME` was found in extracted text or active source. All six bibliography entries are used. All seven section files are included; there are no orphan active sections.
- References begin on page 15 after the article/disclosure and continue through page 16. There is no appendix and no task-imposed venue page cap.
- All 16 actual attempt-02 pages were rendered at 96 dpi and individually viewed. No clipping, equation/number collision, missing table content, or unreadable symbol was seen. The three-regime table and carry-transition table are fully visible. The underfull reference line on page 16 is mildly stretched but remains readable and inside the margins; it was not suppressed.
- The exact rendered page images and extracted text are retained under `build_attempts/02/visual/` and `build_attempts/02/main.txt`.

`BUILD_INPUTS.sha256` contains 171 actual entries: every distinct recorder input, plus the bibliography database/style, latexmk configuration, compiler binaries, and inspection/render binaries. Relative paths in this file are relative to this paper directory. `SOURCE_AND_PDF.sha256` separately records the ten active source/BibTeX files and the three current/attempt PDF paths. These are provenance/technical checksums, not a formal batch manifest or release seal.

## Handoff and remaining work

The real author baseline is copied to `snapshots/author_baseline/`, with source, PDF, bibliography output, logs, recorder, this record, and the checksum records. `BASELINE_FILES.sha256` outside that directory freezes its copied contents. The two earlier build-attempt records remain separate so that a later reviewer can distinguish the first compiler output from the warning repair. No artificial third version was generated.

Checksum paths inside copied provenance records retain their original batch/paper-directory interpretation; the separate baseline inventory is the direct check of snapshot-relative copied files.

No known author-detected mathematical must-fix remains. The residual typographic item is the one underfull bibliography line above; it may be polished in a real later revision if desired. The main outstanding gate is the two genuine nonauthor manuscript reviews and any repairs they require. Source comparison remains bounded, with the disclosed Levin–Sodin–Yuditskii full-text limitation. This handoff makes no final-release claim.

No prior proof/report was edited, and no new agent, formal evaluation, mathematical program, Git operation, upload, external-model call, or release operation was performed by the author during this drafting task. Only source preparation, bibliography checks, compilation, PDF inspection, copying, and technical hashing were used.
