# Integrity after Round-1 author repairs

**Status:** `ROUND1_AUTHOR_REPAIRS_PASS`  
**Date:** 2026-08-14  
**Scope:** deterministic author-side verification after implementing M1--M3;
this is not an independent Round-2 review or a submission-readiness decision.

## Repair closure

| Round-1 item | Evidence | Result |
|---|---|---|
| M1, proof implications | `manuscript.tex`, Lemmas 3.4--3.5 | PASS |
| M2, Silverman/Kawaguchi metadata | `references.bib`, `../notes/CITATION_VERIFICATION.md`, `../notes/NOVELTY_AUDIT.md` | PASS |
| M3, byte `0x08` | whole-paper text control-byte scan | PASS |

The source lock, official result JSON, experiment cutoff, controls, figures,
claims, and route decision were not changed. The reviewed snapshot
`paper_pre_review.pdf` remains byte-identical at SHA-256
`450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f`.

## Validation closure

- Safe tests: 39/39 passed.
- Official result-manifest closure: 41/41 paths, sizes, and hashes matched.
- Figure output closure: 9/9 hashes matched; no generator, input, or output
  changed, so `FIGURE_PACKAGE.json` is byte-identical.
- Citation-key closure: 12/12, with no missing or unused BibTeX entry.
- Text control-character scan: PASS.
- Two consecutive `paper/build.sh` executions produced identical PDF hashes.
- Revised PDF: 11 letter-size pages; embedded/subset fonts; final log has zero
  errors, warnings, undefined citations/references, and overfull/underfull boxes.
- No external prime table, Riemann-zero data, or forbidden target data was
  accessed.

## Active artifact hashes

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `8b1e92941956872d9d504a390a9091b2e530fede93b88d2629f6daad0d1ce1d9` |
| `paper/manuscript.pdf` | `f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156` |
| `paper/paper_round1_revised.pdf` | `f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156` |
| `paper/paper_pre_review.pdf` | `450eae555f09faf7071efbd476f34c570b288166a067d81ddbeac9e6c225010f` |
| `paper/references.bib` | `de0a7b9680b4331725682f725f17a51887a8bfbe97c3bae086690cb8afcdbfd8` |
| `notes/CITATION_VERIFICATION.md` | `82a1950a85ca2efb3702b046c823df51d1202274ffa684eeb6136543ab0140bf` |
| `notes/NOVELTY_AUDIT.md` | `8e0cb2b88116f6490687bce6415329b3b4c01554ac44ec92065ada446f8ada04` |
| `paper/PAPER_CONFIGURATION.md` | `ca767e407b8521f1b4fed77afc1b84ae6455f3f05eeb58d61dd62c37a05dd1a0` |
| `paper/CLAIM_MANIFEST.json` | `231ada508295cf88c0ac529f74fd53744051a0fcddf833e34589e6f7f5803a45` |
| `paper/EXPERIMENT_PASSPORT.json` | `7ca3ed260ac67ff2a6c34e4f686124de3dd7887437263b28543c9b31fef43265` |
| `paper/FIGURE_PACKAGE.json` | `a91eaf58ffe7acfde07d1dcadf9288379732244d478aca9d2d17a87abdc51d1e` |
| `paper/INTEGRITY_PRE_REVIEW.md` | `d75d039955cea69841d2bacdf6785f755e80ec4fdc02312f25de24dce4706e5c` |
| `paper/reviews/round1_review.md` | `93199422647307a9356dd294271a3aa25fdd06deaa612eb6eeb6f93dd7f848b8` |
| `paper/reviews/round1_response.md` | `f3cf874abc19557a534b1c313c1b0f3dbb9c54984a3230c2c6341f2860b1b5fb` |
| `experiments/source_lock.json` | `3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269` |
| `results/final_result_manifest.json` | `e47c93ccc49cf37ffa5bab63bed758be9c1288500f459d539de806d7e4229863` |

## Handoff boundary

M1--M3 are ready for independent Round-2 verification. This author-side
integrity pass does not impersonate that review and does not close the final
integrity or repository-synchronization stages.

