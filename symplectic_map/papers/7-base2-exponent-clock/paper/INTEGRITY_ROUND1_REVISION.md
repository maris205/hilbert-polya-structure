# Round-1 Revision Integrity Record

Date: 2026-08-14 UTC  
Paper ID: `exact-2adic-frozen-pcf-quadratic-v1`  
Candidate ID: `pcf_quadratic_exact_2adic_boundary_v1`  
Status: **ROUND-1 REVISION COMPLETE / AWAITING FRESH INDEPENDENT ROUND 2**

This is an author-side integrity record. It does not constitute an independent
Round-2 review and does not authorize finalization.

## Independent review and bounded response

Independent Round 1 returned `PASS_WITH_MINORS` with no critical or major
finding and four required minors. The reviewed record is
`paper/reviews/round1_review.md`, SHA-256
`b4b571cdcaf5aab6825235e2012fedf7e64b3434a14b17064f5d3d5a5b1a31a5`.
The bounded response is `paper/reviews/round1_response.md`, SHA-256
`c5a833c4db2f9e4b6fe0a706149ffe6106110278152e1da4bd6bbd969a0e6ea4`.

All four requested repairs are present:

1. Theorem 4.1 specifies a finite cycle field `L/K` and an additive
   non-Archimedean valuation `w` of `L` above the unique two-adic valuation.
2. Proposition 5.1 explicitly identifies the `g^d-X` and `g^n-X` Hensel lifts
   when `d | n` before using reduction to prove exact period.
3. Section 6 states the quotient
   `O_{K_{u,n}}/(2) \simeq F_{2^n}[\bar u]/(\bar u^3)`, its basis, the
   vanishing of square cross terms, and the `t`-expansion used for coefficient
   comparison.
4. Gcd and resultant/field norm are consistently described as separately
   implemented but algebraically equivalent exact certificates.

No optional presentation change or additional scientific edit was made.

## Revision artifacts

| Artifact | SHA-256 | Check |
|---|---|---|
| `paper/manuscript.tex` | `60a9868f92b2d34e9ae140cebc534118225d05fe647530df1341c5ad0cc96974` | bounded four-minor revision |
| `paper/manuscript.pdf` | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | build output |
| `paper/paper_round1_revision.pdf` | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | immutable Round-2 input; 11 pages |
| `paper/paper_pre_review.pdf` | `36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be` | immutable Round-1 input retained |
| `paper/math_commands.tex` | `b2f53676ef7bb442818edf77875173e5c7770d167755e132ccfee2e37a539ea2` | unchanged |
| `paper/references.bib` | `dbcb1de7f92643291e688308b472616107a0b376db24a250379f97826d5d53f1` | unchanged; 12/12 closure |
| `paper/build.sh` | `654d11059118425065be5db33ccd6438a02eaf3807b6995d9330187fbf8839b7` | unchanged deterministic build |

Two consecutive clean builds of the final revised source produced the same
PDF digest. The final log has zero errors, package or LaTeX warnings, box
warnings, undefined citations/references, or duplicate labels. All 33 fonts
are embedded and subset. The 11-page revised PDF was rendered and inspected
page by page with no clipping, overlap, missing figure, corrupt glyph, or
illegible ledger entry.

## Retrospective indexes

| Index | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `33674f12a98e18b61a36e5c040a68f5512b6427a22343fec5f77318c866a703d` |
| `paper/CLAIM_MANIFEST.json` | `47205c481af2ae7d4fc4fe230bc7eedb5c00f088f2cc1c8349e829fc5c4e1c97` |
| `paper/EXPERIMENT_PASSPORT.json` | `db31f8c5220ec6099c8847303bde635b16b40688ca02fa4e77588b7fbd2512bb` |
| `paper/FIGURE_PACKAGE.json` | `a6f9514262d97051f1c30207a328fac3e604513d41f2d9f94600fcaa8b55f5a3` |
| `paper/PIPELINE_STATE.json` | `c7699ea0c83442d600a56422f324d6a7660f472ae9944df759237cf1220947ad` |

The pipeline intentionally does not hash this record, avoiding a cyclic
digest dependency.

## Frozen evidence and verification

| Frozen object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `b654c72f1596d5c39ddcf61b8ed6314d7e7d9e149a6d1e874b390d53f113d039` |
| source lock | `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1` |
| proof package | `9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9` |
| official result | `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6` |
| strict result manifest | `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8` |
| figure manifest | `cd4f4a2e831790657dac7b1a4c9706e8693101cb0f0d8b3830b36691a50940c8` |

The safe suite passed 38/38 tests. Read-only closure recomputed all 12 strict
result-manifest hashes and the exclusive result tree, plus all 12 input and 20
artifact hashes in the figure manifest. The nine frozen PDF/SVG/PNG figure
outputs retain their recorded double-generation byte identity. Citation
closure remains 12 cited keys against the same 12 verified records. No
candidate execution, post-null extension, numerical or approximate match,
network citation search, restricted external dataset, or new datum occurred.

The finite ledger remains development-seen evidence only. The uniform equality
question remains `OPEN_FOR_N_GE_4`; Route A is not advanced and Route B is not
opened. The theorem statements and their evidence classes have not expanded.

## Independence boundary

Round 1 is the independent review bound above. All revision checks after it
are author-side mechanical, build, and integrity checks. A fresh reviewer must
verify the four repairs and this revised source/PDF in Round 2. Finalization
remains unauthorized.

Final status: `READY_FOR_INDEPENDENT_ROUND2`.
