# Paper configuration

## Identity

- **Paper ID:** `finite-additive-arithmetic-capacity-lma-v1`
- **Candidate ID:** `additive_finite_arithmetic_capacity_v2`
- **Title:** *Finite Arithmetic Capacity under Additive Locally Constant,
  Good-Reduction Multiplier, and Algebraic-Action Readouts*
- **Author mode:** anonymous finalized local manuscript
- **Article type:** specialist arithmetic/symplectic-dynamics theorem paper with
  a source-locked exact/static implementation audit
- **Format:** 11 pt `article`, letter paper, 0.92-inch margins, author--year citations
- **Pre-review date:** 2026-08-14
- **Round-1 revision date:** 2026-08-14
- **Finalization date:** 2026-08-14
- **Status:** `COMPLETE_LOCAL / FINAL_REVIEW_PASS`; both required Round-1
  repairs and the optional float-placement polish were independently verified
  in Round 2
- **Compiled length:** 12 pages including references and appendices; the
  conclusion begins and ends on page 9

## Central claim configuration

The paper may claim the following and no stronger conclusion:

1. for exact hits represented as
   `log p = v_p + log q_p + alpha_p`, with all `v_p` in one fixed
   finite-dimensional rational space, all `q_p^2` supported on one fixed
   finite rational-prime set, and all `alpha_p` real algebraic, the distinct
   hit set has size at most `dim_Q(V)+|S|`;
2. Hermite--Lindemann removes the algebraic additive term and finite-place
   valuations isolate every outside-support prime coefficient after squaring;
3. the proof handles arbitrary valid per-prime certificate selection, repeated
   hits, `q=1`, negative powers, rational powers, and an initially infinite hit
   set;
4. fixed finite-memory locally constant readouts, declared good-reduction
   generalized Hénon multiplier moduli, and regularly evaluated algebraic exact
   actions supply the L, M, and A source certificates;
5. the selector architecture is only a corollary of the additive theorem;
6. exceeding the bound forces a certificate escape, but those failures are
   not asserted to be exclusive, exhaustive for all dynamics, or sufficient;
7. Deninger and Connes--Consani provide positive arithmetic architectures
   outside the finite L/M/A boundary;
8. the static audit verifies implementation and provenance only.

## Mandatory scope language

- This is **not** a universal no-go theorem for symplectic, arithmetic, or
  infinite-dimensional dynamics.
- It is not a complete trichotomy and makes no necessity-of-dimension claim.
- It does not cover approximate equality, nonlinear mixing, algebraic
  irrational coefficients on multiplier logarithms, log-after-action,
  multivalued logarithms, arbitrary Hölder roofs, target-dependent support, or
  target-injected labels.
- It makes no historical-priority claim.
- It makes no claim about Riemann zeros, trace formulas, zeta functions,
  determinants, quantization, or Route B.
- Static tests do not replace the all-period mathematical proof.

## Evidence policy

| Evidence class | Permitted role |
|---|---|
| Main manuscript proof | All-period rank-plus-support theorem and source certificates |
| Proof/scope ledgers | Frozen dependency and operation contracts |
| Six exact controls | Edge-case, abstract-attainment, target-injection, and schema checks |
| Registered result and JUnit | Software/provenance integrity only |
| Paper-3/Paper-4 terminal bindings | Actual upstream source-package provenance |

The official audit is static only. It may not run a numerical candidate,
compute a target match, generate a prime target array, read an external prime
table, or access Riemann-zero data.

## Bibliography policy

All 18 records in `references.bib` are cited. Publisher, DOI, NUMDAM, and
arXiv metadata plus claim-safe uses are recorded in
`../notes/PAPER_CITATION_AUDIT.md`. The invalid Parry--Pollicott DOI sometimes
reported in secondary notes is omitted in favor of the official NUMDAM record;
Deninger's 2026 article uses its formal journal metadata. Citations supply
context or identify classical inputs and never substitute for a paper-specific
proof.

## Figure policy

- Regenerate all three figures with `python paper/figures/generate_all.py`.
- Each script reads through a fail-closed adapter restricted to five official
  JSON ledgers/results.
- PDF and SVG are vector masters; PNG is a 300-dpi review copy.
- Fixed metadata and an SVG hash salt make all nine outputs byte-reproducible;
  a clean isolated second generation must match every output.
- All three masters and their placements in the manuscript require visual
  inspection before handoff.

## Build policy

Run `paper/build.sh`. It fixes `SOURCE_DATE_EPOCH`, invokes BibTeX, and performs
four LaTeX passes. A valid pre-review build has no errors, LaTeX/package
warnings, box warnings, undefined citations or references, or multiply defined
labels; every font is embedded and subset; all pages are visually clean; and
two consecutive builds have the same SHA-256. `paper_pre_review.pdf` is the
immutable Round-1 input, `paper_round1_revision.pdf` is the Round-2 input, and
`paper_final.pdf` is the terminal local artifact byte-identical to the
independently approved revision.

## Pipeline boundary

Independent Round 1 returned `PASS_WITH_MINORS`.  The two bounded manuscript
repairs and optional float-placement polish are recorded in
`reviews/round1_response.md`; they did not change the source lock or official
experiment package.  Fresh independent Round 2 returned `PASS — MAY FINALIZE`
with no residual blocking issue.  Two clean isolated builds reproduced the
approved revision byte for byte, and that exact artifact is frozen as
`paper_final.pdf`.  The local paper and final-integrity stages are complete.
Repository synchronization remains deferred to the five-paper batch close
under the Session rules.
