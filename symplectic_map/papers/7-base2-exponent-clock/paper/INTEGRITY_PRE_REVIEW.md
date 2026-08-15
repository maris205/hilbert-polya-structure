# Pre-Review Integrity Record

Record date: 2026-08-14 UTC  
Candidate: `pcf_quadratic_exact_2adic_boundary_v1`  
Disposition: **PASS TO FRESH INDEPENDENT MANUSCRIPT REVIEW**

This record freezes the author-side pre-review package. It is an integrity
attestation, not an independent mathematical review and not authorization to
finalize the paper.

## Bound manuscript package

| Object | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `5e76f3039d51489d18bb8caf525bc6e0546aa86746d19bfa8202cdf289065812` |
| `paper/math_commands.tex` | `b2f53676ef7bb442818edf77875173e5c7770d167755e132ccfee2e37a539ea2` |
| `paper/references.bib` | `dbcb1de7f92643291e688308b472616107a0b376db24a250379f97826d5d53f1` |
| `paper/build.sh` | `654d11059118425065be5db33ccd6438a02eaf3807b6995d9330187fbf8839b7` |
| `paper/manuscript.pdf` | `36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be` |
| `paper/paper_pre_review.pdf` | `36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be` |
| `paper/PAPER_CONFIGURATION.md` | `93d3f4836746765480419842e796513152c8cc283bfabe4f1949b400bfc9fccf` |
| `paper/CLAIM_MANIFEST.json` | `d163e7046882d2d7a19a3698c30eda806e030c40602337f92136acadccbac4d6` |
| `paper/EXPERIMENT_PASSPORT.json` | `db31f8c5220ec6099c8847303bde635b16b40688ca02fa4e77588b7fbd2512bb` |
| `paper/FIGURE_PACKAGE.json` | `2165fd8916b14be3f0f548d619ad2828d07e5ed7d43c8059a3ecb040b30f2795` |
| `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `ea0b4f6de23e152621ba3fbf996ba16607ad4de240d72b5421447c9585acc4bd` |
| `paper/PIPELINE_STATE.json` | `4e5bc614afabc9c650388eecad598ba199a47cbcd29902806121b22865a4862b` |

The pipeline record intentionally does not hash this integrity record, which
avoids a cyclic digest dependency.

## Frozen upstream evidence

| Frozen object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `b654c72f1596d5c39ddcf61b8ed6314d7e7d9e149a6d1e874b390d53f113d039` |
| source lock | `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1` |
| proof package | `9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9` |
| official result | `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6` |
| strict result manifest | `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8` |
| official terminal record | `06215794b323552bc953c3ea8935d76c15b205bc7df13c170e448c0562b0b7b9` |
| official test report | `4e38e3197ec588edceac43c8292630a61f018f4f03f36bb3c8606723bbd0f237` |
| independent code review | `ac8bc40bc863613260486106ef7d46ea0370bea326019de1b3b1a83d488c6109` |
| independent result integrity | `f1a39f31ceaa6b4eee1a469c2f8fcb5028a33f6c7ccfcc1cb311b95fc5778c4f` |
| citation verification | `bb315de70ecbcd8ac6dbdeebd32d68cb6f99bd4749a1924e3ba2cdf6d77a41df` |
| citation plan audit | `1801df7e97bf3e4974c3a5d2bdc8d93e5b8fa920e9b623ed64c9476f1cc616aa` |
| figure manifest | `cd4f4a2e831790657dac7b1a4c9706e8693101cb0f0d8b3830b36691a50940c8` |
| figure determinism report | `e883612c05f4f09463d522ef7ce6bed1d5a2d3ade7d988fe29f5467f8dd39be0` |
| independent plan/figure review | `a1858ff321a4badda752ec5bc389732d22f9a35c39b4b2fd96fd6e73cf9ac2cc` |

The manuscript-writing stage did not alter any frozen plan, source, proof,
result, bibliography, or figure input, did not rerun or extend the registered
candidate, and did not access prohibited external datasets.

## Release-gate checks

- Two consecutive clean builds were byte-identical at the PDF digest above.
  The review PDF has 11 pages; the final LaTeX log has zero errors, undefined
  citations, undefined references, overfull boxes, underfull boxes, or other
  warnings.
- All 33 PDF fonts are embedded and subset. Every page of the bound final PDF
  was rendered and visually inspected (11/11): no clipping, overlap, missing
  figure, corrupt glyph, or illegible ledger entry was found.
- Citation closure is 12 cited keys against the same 12 verified BibTeX
  entries, with zero missing or unused entries. The normalized body has zero
  common 12-word shingles with each of the six earlier project manuscripts.
- All three frozen figures and the raw exact ledger appear in the manuscript.
  The ledger agrees with the official exact result, including runs R042--R047,
  both signs, all period/degree/count/norm fields, and the total runtime.
- Claim/evidence, mathematical logic, exact-period semantics, provenance,
  citation/originality/anonymity, figure/data transcription, and build/release
  failure modes all pass the author-side audit recorded in
  `paper/AUTHOR_PRE_REVIEW_AUDIT.md`.
- Required boundaries remain explicit: all finite rows are
  `DEVELOPMENT_SEEN_REPRODUCTION`, there were no blind periods, the uniform
  equality question is `OPEN_FOR_N_GE_4`, Route A is not advanced, Route B is
  not opened, and no finite record is promoted to an all-period theorem.

## Independence boundary

The deployment code, official result, and plan/figure package have their
listed independent checks. The manuscript itself has received only an
author-side red-team pass. A fresh reviewer must now inspect the bound source
and PDF without relying on that pass. Until that review and any bounded repair
cycle close, the package remains pre-review, and finalization is not
authorized.

Final status: `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`.
