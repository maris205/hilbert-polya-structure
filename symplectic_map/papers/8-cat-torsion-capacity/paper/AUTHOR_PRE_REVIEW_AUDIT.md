# Author Pre-Review Audit

Audit date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Verdict: **PASS AUTHOR-SIDE GATES; NOT AN INDEPENDENT MANUSCRIPT REVIEW**

This audit covers the pre-review manuscript package only. It did not rerun
the candidate, add a period, access an external prime or zero table, perform
approximate matching, or alter any frozen source, code, result, bibliography,
or figure input. The earlier source-lock, result-integrity, and
plan/figure/citation gates retain their independent roles; none is relabeled
as an independent review of this manuscript.

## Bound snapshot

| Object | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `072be061acbd4ef00ecc3220449a1f872c430200becdb4e127b706d09da36ee2` |
| `paper/manuscript.pdf` | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |
| `paper/paper_pre_review.pdf` | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |
| `paper/math_commands.tex` | `49265b2d7b07cdb2d20b9c8e612ab119a9f32d94bee27f44cec0fa3d5f683392` |
| `paper/build.sh` | `860800c9488182f6101b68d8f83bc31eb43c468097f49e863164ab09fb5863b1` |
| `paper/references.bib` | `f4567be30ef6b8d6e0bc1a3a8f6a294499221de51de4064e864cbbe448b79775` |
| `paper/PAPER_CONFIGURATION.md` | `bec1ca30a45c3d44056a0f7335be29738adebd10d5fcaccea628c9cbe9c6ccc6` |
| `paper/CLAIM_MANIFEST.json` | `85f33d338f473b6b0b01eb4fbc44146b3b6366ea88b4841b59e2df7a896d5ff8` |
| `paper/EXPERIMENT_PASSPORT.json` | `bf1a0a163c8303d055854e23b1aff2cd2cd1c46f61a238517639c6c4a1fb0b71` |
| `paper/FIGURE_PACKAGE.json` | `6ac38589436ff825f9e064eeebb9981a2a314a2d44a2a4e35f79b04e0119c0bc` |
| `paper/PIPELINE_STATE.json` | `2bad0671acbaa60fbec896ea35f5c4de87a6ceec34624a700c4e656f538c276a` |
| source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| proof package | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| raw exact result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| final result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |

## Citation audit

- The manuscript has 12 unique citation keys; the bibliography has exactly
  the same 12 unique entries. Missing keys: 0. Unused entries: 0.
- All entries and claim roles were verified against the citation ledger and
  independently closed by `PAPER8_PLAN_FIGURE_CITATION_PASS`, SHA-256
  `a5e2eab53b97765bee6cedc004f4e77a29c0647c5a0186c2cd8eda7bc8262655`.
- Flatters is cited only for the positive norm-one primitive-divisor engine
  and small-index classification. The negative-trace conversion is expressly
  presented as this note's separate proof.
- Tan--Li and Chandra remain preprints. Zeta/transfer and quantum-cat sources
  delimit established neighboring theories and are not used to imply new
  results in those areas.
- The final BibTeX run has 12 `bibitem` records and zero warning, placeholder,
  unverified key, or unresolved citation.

## Proof and exact-data audit

- The primitive-kernel lemma separates additive order from least dynamical
  period and requires no splitting, diagonalizability, semisimplicity, or
  unramifiedness hypothesis.
- The positive-trace proof exposes every hypothesis of the imported
  norm-one theorem at the citation point.
- The negative-trace proof contains all three branches: odd `n` uses index
  `2n`; `4|n` uses `n`; `n=2k` with odd `k` uses `k=n/2`. The half-index
  warning and the characteristic-two exclusion are explicit.
- The standard-cat proof keeps primitive-divisor and carrier exception sets
  distinct. The modulo-five nilpotent calculation counts four period-2
  points and twenty period-10 points, hence two period-10 cycles. The
  exclusions at 1, 6, and 12 use exact determinant support plus complete
  modulo-2, modulo-3, and modulo-5 profiles.
- The clock proof keeps its domain equal to torus torsion, proves every
  integer order, proves local unboundedness by coprime perturbations, and
  separates raw labels, Birkhoff sums, return-time normalization, and native
  monodromy.
- The manuscript's 12 determinant values, eight finite-field profiles,
  41,003-vector total, exception set, Jordan counts, exact clock witnesses,
  and hashes agree with the raw result, official reports, and independent
  result-integrity audit.
- No finite row is used to prove the `n>12` tail. The manuscript records
  empty computed-tail lists and identifies the tail as theorem-only.

## Originality and anonymity audit

The normalized main-text body through the conclusion was compared
mechanically with the seven preceding project manuscripts and the legacy
Riemann--Henon manuscript. After stripping TeX control words, citations,
labels, punctuation, and appendices, every comparison had zero common
12-word body shingles. No copied paragraph, table, caption, or abstract was
found.

The source, rendered text, and PDF metadata contain `Anonymous Authors` and
no name, email, affiliation, ORCID, identifying repository URL, local path,
acknowledgment, or grant identifier. The title and metadata match the safe
plan title.

## Reverse outline and claim coverage

1. The abstract states the uniform carrier theorem, separate negative-trace
   conversion, sharp standard-cat boundary, Jordan repair, and specificity
   obstruction without a citation or priority claim.
2. Sections 1--2 separate the prescribed-period question from aggregate
   fixed-point counts, fixed-lattice matrix order, transfer/zeta, and quantum
   contexts.
3. Section 3 proves the primitive-kernel bridge, positive-trace corollary,
   and full negative-trace parity conversion.
4. Section 4 gives the complete small determinant ledger, Jordan proof,
   exclusions, exact classification, and sharpness statement.
5. Section 5 proves periodic-equals-torsion, all-order capacity, irregularity,
   orbit-sum scaling, and native-monodromy blindness.
6. Section 6 reports only the registered exact finite audit and its
   computation/proof firewall.
7. Section 7 calibrates novelty, lists every structural nonclaim, and records
   the frozen A0/route decision.
8. Appendices provide an independent Fibonacci identity, concise
   claim/evidence table, and complete disclosure statements.

Claims C1--C7 each map to a proof or frozen exact artifact. Every figure and
table supports a named claim and carries its evidentiary boundary.

## Seven-mode failure audit

1. **Claim/evidence inflation -- PASS.** The finite ledger is never promoted
   to an infinite-tail proof. A bounded negative literature search is not
   promoted to priority.
2. **Mathematical-logic failure -- PASS AUTHOR SIDE.** The kernel argument,
   norm identity, all three parity branches, characteristic-two exclusion,
   modulo-five Jordan depth, small-prime exclusions, and torsion-clock proof
   were replayed against the frozen proof package and earlier independent
   source-lock audit. This is not independent manuscript review.
3. **Semantic conflation -- PASS.** Additive order and least period, points
   and cycles, primitive-divisor and carrier exceptions, raw labels and
   summed weights, and monodromy and torsion order remain separate.
4. **Provenance or forbidden-data failure -- PASS.** One registered exact
   audit covers only periods 1--12. Candidate numerical runs, reruns, tail
   extensions, approximate matching, external prime tables, and zero data
   are all zero, false, or empty.
5. **Citation, originality, or anonymity failure -- PASS.** Citation closure
   is 12/12, normalized 12-word body overlap is zero, metadata are anonymous,
   and no new citation was created during writing.
6. **Figure or transcription failure -- PASS.** Three PDF/SVG/PNG triplets
   close under a 9/9 byte-reproducible manifest and independent review. All
   12 rendered manuscript pages were inspected with no clipping, overlap,
   missing figure, corrupt glyph, or illegible ledger entry.
7. **Build or release-state failure -- PASS.** Two clean builds produced the
   same SHA-256
   `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8`.
   The final log has zero LaTeX, citation, reference, overfull, or underfull
   warnings; all 33 fonts are embedded and subset, and the PDF contains zero
   raster image objects. The artifact remains explicitly pre-review.

## Disposition

`PASS_TO_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`. A fresh reviewer must still
audit the mathematical manuscript. No `paper_final.pdf` was created, and no
finalization is authorized by this author-side record.
