# Integrity pre-review

**Status:** `PRE_REVIEW_PASS`  
**Date:** 2026-08-14  
**Scope:** internal integrity and evidence-boundary check before independent
manuscript review; this is not the final independent review.

## Frozen evidence closure

- The prospective source lock remains byte-identical at SHA-256
  `3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269`.
- All 41 artifacts in `results/final_result_manifest.json` were rehashed
  without rewriting the official results; 41/41 paths, byte sizes, and hashes
  match.
- `results/run_summary.json` remains `PASS`: 15/15 registered runs completed,
  zero failures, and the candidate gate opened only after controls.
- The official exact suite remains 39/39 passing (`39 passed in 1.71s` in the
  paper-stage rerun).  No official result JSON was regenerated.
- External prime tables, Riemann-zero data, and forbidden target data remain
  unused.

## Claim/evidence alignment

| Gate | Result |
|---|---|
| General (S)-integral and multiplier-unit theorem has a complete proof | PASS |
| Galois closure uses all places over the rational bad set | PASS |
| Text explicitly separates $\bar\lambda$ from $\lambda^{-1}$ | PASS |
| Frozen no-rational-prime conclusion is labeled all-period and deductive | PASS |
| (n\le3), five-cycle result is labeled a software audit only | PASS |
| (a=-15/16), ((5/4,5/4)), (2,1/2) sharp control is present | PASS |
| Geometry PASS and A0 theorem failure are both reported | PASS |
| Universal symplectic, irrational-modulus, prime--orbit, target-zero, compactness, and quantization nonclaims are explicit | PASS |

The machine-readable claim mapping is in `CLAIM_MANIFEST.json`; the experiment
mapping is in `EXPERIMENT_PASSPORT.json`.  The all-period conclusion has proof
provenance and never points to the finite ledger as its evidentiary source.

## Bibliography closure

- 12 bibliography records were checked against a publisher DOI record,
  author-supplied arXiv record, or both; details and safe-use boundaries are in
  `../notes/CITATION_VERIFICATION.md`.
- The manuscript cites exactly 12 unique keys.  `references.bib` contains
  exactly those 12 entries: zero missing keys and zero unused entries.
- No citation is used as a surrogate proof of the paper's rational-modulus
  support theorem.  One inconsistent Crossref result was deliberately omitted.

## Figure integrity

- Three publication figures have PDF and SVG vector masters plus PNG review
  copies.
- Every scientific candidate/control value is loaded from frozen JSON through
  `figures/frozen_data.py`; the loader verifies official PASS status, candidate
  identity, zero failures, and source-lock hash.
- All three PNG renderings were inspected at original resolution.  All 11
  compiled PDF pages were rendered and visually inspected.
- Fixed vector metadata and fixed SVG hash salt make the nine generated files
  byte reproducible.  Two consecutive full regenerations produced 9/9
  identical SHA-256 hashes.
- `FIGURE_PACKAGE.json` records generator, input, and output hashes.

## Compilation integrity

Build command:

```bash
paper/build.sh
```

The build fixes `SOURCE_DATE_EPOCH`, runs BibTeX, and performs four `pdflatex`
passes.  Final checks:

| Check | Result |
|---|---|
| PDF pages | 11 |
| PDF size | letter, 612 × 792 pt |
| Final LaTeX errors | 0 |
| Final LaTeX warnings | 0 |
| Overfull / underfull boxes | 0 / 0 |
| Undefined references / citations | 0 / 0 |
| Citation-key closure | 12/12 |
| Fonts embedded and subset | PASS |
| Consecutive deterministic PDF builds | identical SHA-256 |
| Manuscript PDF SHA-256 | `450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f` |
| Pre-review snapshot SHA-256 | `450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f` |

## Primary artifact hashes

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `ea6ed18de3a35b02e34882ff4e647f4e4eeec0fe33e8e285511d40d44c6eb10d` |
| `paper/paper_pre_review.pdf` | `450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f` |
| `paper/references.bib` | `3b37d83871537f7d73a1106bbf31ec013854d8eb6df46bff46f2296451aaa071` |
| `notes/CITATION_VERIFICATION.md` | `2e8226e74a3863b9335c36445152f9627703bd505aace8ae45506fe0a6711342` |
| `paper/CLAIM_MANIFEST.json` | `dd5f1d220a9c163da1022a787119b61d1c98784028d1b3699e12171846f58e1a` |
| `paper/EXPERIMENT_PASSPORT.json` | `7ca3ed260ac67ff2a6c34e4f686124de3dd7887437263b28543c9b31fef43265` |
| `paper/FIGURE_PACKAGE.json` | `a91eaf58ffe7acfde07d1dcadf9288379732244d478aca9d2d17a87abdc51d1e` |
| `results/final_result_manifest.json` | `e47c93ccc49cf37ffa5bab63bed758be9c1288500f459d539de806d7e4229863` |

## Handoff boundary

The article is ready for an independent manuscript reviewer.  No independent
final review was performed in this production thread, and no claim of
submission readiness is made yet.  Review-driven edits, a clean recompile, and
a final post-review integrity check remain pending.
