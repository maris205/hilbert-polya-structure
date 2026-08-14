# Final Integrity Record

Date: 2026-08-14  
Paper ID: `integral-area-henon-multiplier-support-v1`  
Candidate ID: `integral_area_henon_multiplier_support_v1`  
Status: **COMPLETE_LOCAL / FINAL_REVIEW_PASS**

## Scientific outcome

For finite compositions of monic area-preserving generalized Hénon maps over
an `S`-integer ring, every finite periodic coordinate is `S`-integral, return
eigenvalues are algebraic `S`-units, and an exact rational multiplier modulus
can involve only rational primes in the predeclared bad support.  At the frozen
integral parameter, that support is empty, so every exact rational periodic
multiplier modulus is one and no rational-prime modulus occurs at any period.

The exact period-1--3 ledger is an implementation audit, not the proof of the
all-period statement.  It contains ten exact points on five cycles, one
selected-embedding unit-modulus cycle and four irrational algebraic-unit
cycles.  The denominator-2 control realizes exact moduli `2` and `1/2`, showing
that the fixed-support boundary is sharp.  The formal route outcome remains:
carrier geometry passes, Route-A A0 fails by theorem, later Route-A gates stop,
and Route B is not opened.

## Independent review chain

- Round 1: `PASS_WITH_MINORS`, 8.5/10.  It requested two explicit
  ring/place implications, correction of Silverman/Kawaguchi metadata, and
  removal of one control character.
- Author response: all three minor items implemented without changing the
  scientific source lock, result JSON, experiment cutoff, controls, figures,
  or route decision.
- Round 2: `PASS — MAY FINALIZE`, 8.8/10, with zero remaining critical,
  major, or required minor issues.

| Review artifact | SHA-256 |
|---|---|
| `paper/reviews/round1_review.md` | `93199422647307a9356dd294271a3aa25fdd06deaa612eb6eeb6f93dd7f848b8` |
| `paper/reviews/round1_response.md` | `f3cf874abc19557a534b1c313c1b0f3dbb9c54984a3230c2c6341f2860b1b5fb` |
| `paper/reviews/round2_review.md` | `9cd87c6110ee821886d220726aafcd816b60b312858c7a5b1da3df9719d6f8e9` |

## Final manuscript artifacts

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `8b1e92941956872d9d504a390a9091b2e530fede93b88d2629f6daad0d1ce1d9` |
| `paper/manuscript.pdf` | `f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156` |
| `paper/paper_round1_revised.pdf` | `f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156` |
| `paper/paper_final.pdf` | `f7368ecfa03929143311516303bb1c7a1a97e77869cb245f47e82e8e91a63156` |
| `paper/references.bib` | `de0a7b9680b4331725682f725f17a51887a8bfbe97c3bae086690cb8afcdbfd8` |

The final PDF is byte-identical to the independently approved Round-1 revised
snapshot.  Two consecutive final builds reproduced the same PDF hash.  The
file is an unencrypted, 11-page letter-size PDF; all fonts are embedded and
subset.  The retained final log has zero LaTeX or package warnings, undefined
citations/references, multiply defined labels, overfull boxes, underfull boxes,
or compilation errors.  Round 2 visually inspected all 11 pages and found no
clipping, detached caption, broken equation, figure regression, or page-boundary
defect.

## Proof, result, figure, and citation closure

| Evidence/index artifact | SHA-256 | Verification |
|---|---|---|
| `experiments/source_lock.json` | `3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269` | prospective commitment unchanged |
| `notes/PROOF_PACKAGE.md` | `2c536656bef0d98bfc0fd8fbf60ae04ac3e39943a178630a199203d52429afdd` | all-period proof source |
| `results/final_result_manifest.json` | `e47c93ccc49cf37ffa5bab63bed758be9c1288500f459d539de806d7e4229863` | 41/41 declared paths, sizes, hashes matched |
| `paper/EXPERIMENT_PASSPORT.json` | `7ca3ed260ac67ff2a6c34e4f686124de3dd7887437263b28543c9b31fef43265` | frozen run and theorem/experiment boundary |
| `paper/FIGURE_PACKAGE.json` | `a91eaf58ffe7acfde07d1dcadf9288379732244d478aca9d2d17a87abdc51d1e` | 23/23 frozen-input/generator/output checks; 9/9 outputs |
| `notes/CITATION_VERIFICATION.md` | `82a1950a85ca2efb3702b046c823df51d1202274ffa684eeb6136543ab0140bf` | 12/12 citation-key closure |
| `notes/NOVELTY_AUDIT.md` | `8e0cb2b88116f6490687bce6415329b3b4c01554ac44ec92065ada446f8ada04` | corrected bibliography ledger and scoped positioning |

Round 2 independently recomputed the official result closure and figure
closure, matched all displayed counts and classifications to frozen JSON, and
confirmed that the finite audit remains explicitly subordinate to the
all-period proof.  The whole-paper UTF-8/C0 text scan found no disallowed
control character.

## Retrospective final indexes

| Index | SHA-256 | Status |
|---|---|---|
| `paper/PAPER_CONFIGURATION.md` | `8f92e0068e33d2fb7c587fa6241dd8e5b95aa439662be04d2162883d603654a8` | terminal local configuration |
| `paper/CLAIM_MANIFEST.json` | `53e7482a260af4b1d9725652a1cd66e72509a916c6ad2350405c9983798df7d9` | JSON valid; final PDF/review bound; seven claims unchanged |
| `paper/PIPELINE_STATE.json` | `61ec1ff8c39102bd12e651a0735a978b6e38f290c4f3ad9d5f9e9384e9d5592f` | `COMPLETE_LOCAL`; independent Round 2 and final PDF complete |

These are retrospective audit indexes.  They do not rewrite the prospective
source lock or any official result.  This record intentionally does not hash
itself.

## Reproducibility and safety checks

- Safe unit/protocol suite: **39 passed**, zero failures, with project cache
  writing disabled during independent Round 2.
- Deterministic build: **2/2** consecutive final builds matched the approved
  PDF hash.
- Official result closure: **41/41**.
- Figure package closure: **23/23** indexed checks and **9/9** output hashes.
- Citation-key closure: **12/12**, zero missing and zero unused.
- Control-character scan: **PASS**, zero findings.
- External prime tables accessed: **false**.
- Riemann-zero data accessed: **false**.
- Forbidden target data used: **false**.

## Repository handoff

Paper 3 is complete locally.  GitHub synchronization remains deliberately
deferred to the five-paper batch close, where the Session's scoped clone-and-
sync rules will exclude nested `.git/` and `.ipynb_checkpoints/` paths before
one batch commit.
