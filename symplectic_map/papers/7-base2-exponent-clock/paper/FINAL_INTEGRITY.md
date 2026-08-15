# Final Integrity Record

Date: 2026-08-14 UTC  
Paper ID: `exact-2adic-frozen-pcf-quadratic-v1`  
Candidate ID: `pcf_quadratic_exact_2adic_boundary_v1`  
Status: **COMPLETE_LOCAL_FINAL_REVIEW_PASS**

## Independent authorization

Independent Round 2 returned `PASS / MAY_FINALIZE`, closed all four required
Round-1 minors, and reported no critical, major, residual-minor, scientific,
evidentiary, citation, figure, build, or PDF blocker. The review is frozen at
`paper/reviews/round2_review.md`, SHA-256
`f9a9937fd439bd5a91df1b45709775615fc1fe7920777488d72e8d1e6cfb62d6`.
It binds the approved manuscript source and PDF hashes recorded below.

Finalization was mechanical. The accepted manuscript content was not altered,
no candidate was executed or extended, and no frozen evidence, citation, or
figure was changed.

## Terminal manuscript artifacts

| Artifact | SHA-256 | Status |
|---|---|---|
| `paper/manuscript.tex` | `60a9868f92b2d34e9ae140cebc534118225d05fe647530df1341c5ad0cc96974` | independently approved source; unchanged |
| `paper/manuscript.pdf` | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | deterministic working build |
| `paper/paper_round1_revision.pdf` | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | independently approved Round-2 input |
| `paper/paper_final.pdf` | `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf` | terminal PDF; byte-identical copy |
| `paper/paper_pre_review.pdf` | `36cf7d4f50ef712e3208565d081a57dd5602a828c3eedc5ad50e4386603bf8be` | immutable historical Round-1 input |
| `paper/math_commands.tex` | `b2f53676ef7bb442818edf77875173e5c7770d167755e132ccfee2e37a539ea2` | unchanged |
| `paper/references.bib` | `dbcb1de7f92643291e688308b472616107a0b376db24a250379f97826d5d53f1` | unchanged |
| `paper/build.sh` | `654d11059118425065be5db33ccd6438a02eaf3807b6995d9330187fbf8839b7` | unchanged |

Two fresh builds in separate temporary project copies each reproduced the
approved PDF digest exactly. Both isolated logs had zero errors, LaTeX or
package warnings, undefined citations/references, duplicate labels, overfull
boxes, or underfull boxes. The final PDF is an unencrypted 11-page letter-size
document; all 33 fonts are embedded and subset. Its title and author metadata
remain anonymous. Because `paper_final.pdf` is byte-identical to the approved
revision, it is also byte-identical to the 11-page file inspected page by page
in independent Round 2.

## Review chain

| Artifact | SHA-256 | Verdict or role |
|---|---|---|
| `paper/reviews/round1_review.md` | `b4b571cdcaf5aab6825235e2012fedf7e64b3434a14b17064f5d3d5a5b1a31a5` | `PASS_WITH_MINORS` |
| `paper/reviews/round1_response.md` | `c5a833c4db2f9e4b6fe0a706149ffe6106110278152e1da4bd6bbd969a0e6ea4` | bounded four-minor response |
| `paper/INTEGRITY_ROUND1_REVISION.md` | `8c98badc4125d8e319d3e2efe26d65c8d91fdde51aad5abaad18246442306335` | author-side Round-1 revision integrity |
| `paper/reviews/round2_review.md` | `f9a9937fd439bd5a91df1b45709775615fc1fe7920777488d72e8d1e6cfb62d6` | `PASS_MAY_FINALIZE` |

## Terminal indexes

| Index | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `63f8fb6b034db7de6d26e760d0243c63c079cf59d4452881aea39a3198eb8232` |
| `paper/CLAIM_MANIFEST.json` | `1fb3727833dbe9c9aa7fd8cb24cec9d9beb787f5a3cb99ed7ba2dabc768889e5` |
| `paper/EXPERIMENT_PASSPORT.json` | `bd525b773182b605ee7bf5bc643223e4822fcc0294d2347b35a5da4db8d0dc39` |
| `paper/FIGURE_PACKAGE.json` | `a1f41aa96293807d8d98ddcb50e17b706b741883a99e4570886f8d70fb3683f2` |
| `paper/PIPELINE_STATE.json` | `9dc8b2eb3a97e292bb999b59f812380f7f325673db005b06afd9b82737e91c6b` |

The pipeline intentionally does not embed the hash of this terminal record,
which avoids a circular digest dependency.

## Frozen scientific evidence

| Object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `b654c72f1596d5c39ddcf61b8ed6314d7e7d9e149a6d1e874b390d53f113d039` |
| source lock | `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1` |
| proof package | `9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9` |
| official result | `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6` |
| strict result manifest | `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8` |
| official JUnit report | `4e38e3197ec588edceac43c8292630a61f018f4f03f36bb3c8606723bbd0f237` |
| figure manifest | `cd4f4a2e831790657dac7b1a4c9706e8693101cb0f0d8b3830b36691a50940c8` |
| figure determinism record | `e883612c05f4f09463d522ef7ce6bed1d5a2d3ade7d988fe29f5467f8dd39be0` |

## Terminal regression checks

- Safe tests: 38 passed, with zero failures, errors, or skips; bytecode and the
  pytest cache provider were disabled.
- The strict result manifest closes all 12 recorded file hashes and the exact
  nine-file pre-manifest result tree. No nested, symlinked, unsafe, missing,
  unsupported, target-hit, or extra evidence was found.
- The figure manifest closes 12 frozen inputs and 20 artifacts. All nine
  PDF/SVG/PNG figure outputs retain the recorded two-generation byte identity.
- The six manuscript ledger rows, 12 zero-gcd/nonzero-norm decisions, run IDs,
  exact degrees and cycle counts, norm values, nanosecond times, and total
  `23,239,165,865 ns` agree with the official exact JSON.
- Citation closure is 12 cited keys against the same 12 verified bibliography
  entries. Source labels and references are closed with no duplicate label or
  missing target.
- A control-character scan of 79 textual project artifacts found no disallowed
  ASCII control byte. Extracted PDF text contains no unresolved-reference,
  unresolved-citation, verification, TODO, FIXME, TBD, or placeholder marker.
- Candidate numerical runs, approximate matching, post-null extension,
  external prime-table access, Riemann-zero access, and forbidden-data use all
  remain zero or false.

## Scientific and synchronization boundary

The all-period result remains the exact 2-adic valuation theorem. Rational
equality is excluded by proof only at periods two and three and is absent over
periods two through seven only in the disclosed development-seen reproduction.
The uniform equality question remains `OPEN_FOR_N_GE_4`. Route A is not
advanced and Route B is not opened.

The local paper package is complete. GitHub synchronization is deliberately
not performed here and remains pending under the existing five-paper batch
rule. No Paper 8 work was started.

Final status: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
