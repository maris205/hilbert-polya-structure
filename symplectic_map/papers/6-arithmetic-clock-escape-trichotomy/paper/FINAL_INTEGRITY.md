# Final Integrity Record

Date: 2026-08-14  
Paper ID: `finite-additive-arithmetic-capacity-lma-v1`  
Candidate ID: `additive_finite_arithmetic_capacity_v2`  
Status: **COMPLETE_LOCAL / FINAL_REVIEW_PASS**

## Scientific outcome

For a fixed exact additive readout
`log p = v_p + log q_p + alpha_p`, with all `v_p` in one finite-dimensional
rational space `V`, every positive algebraic `q_p` having `q_p^2` supported on
one fixed finite rational-prime set `S`, and every `alpha_p` real algebraic,
the number of distinct exact prime hits is at most `dim_Q(V)+|S|`.
Hermite--Lindemann removes the algebraic additive term; squaring and one
finite-place valuation over each distinct outside-support prime force rational
independence of the selected `v_p` terms.

Fixed finite-memory locally constant readouts, the declared good-reduction
generalized Hénon multiplier moduli, and regularly evaluated algebraic exact
actions supply the L/M/A source certificates.  The selector is only a
corollary, and certificate escapes are necessary failures only: they are not
exclusive, exhaustive, or sufficient.  The result is not a universal
symplectic no-go theorem, complete trichotomy, historical-priority claim, or
Riemann-zero/Route-B advance.

## Independent review closure

- Round 1: `PASS_WITH_MINORS`, 8.4/10, confidence 0.94.
- Author response: the proper-affine Class-M statement was repaired in a form
  valid for nonreduced schemes; “sharp” was removed; K001 was limited to bare
  rank attainability/target injection; target independence was separated as a
  provenance condition; and Table 1 placement was repaired.
- Fresh Round 2: `PASS`, 9.0/10, confidence 0.97, mathematical status
  `PROVABLE AS STATED`, and `MAY FINALIZE` with zero blocking issues.

| Review artifact | SHA-256 |
|---|---|
| `paper/reviews/round1_review.md` | `d9dffa9c37fd4eb4151f7953583100c0974407ffefd0eb104672bf8b463bab14` |
| `paper/reviews/round1_response.md` | `739e851904976b967c774d0ce43737f0f5f13aa04a18428006728bfcde4175c9` |
| `paper/reviews/round2_review.md` | `eda4442a8d17d50c71d8328b9b34441c81e86f4a878fe99f953418ed9c49159c` |

## Final manuscript artifacts

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `2be0a171cf94b54a58e447bb1922a14880e69c4f80733df5a0882f0302978cb4` |
| `paper/references.bib` | `88bf55d604f7f11f855892f6248663823ba8caa4c17f9c3b3d0d1f1f5e43d10f` |
| `paper/paper_round1_revision.pdf` | `9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8` |
| `paper/paper_final.pdf` | `9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8` |

`paper_final.pdf` is byte-identical to the revision approved in Round 2.  Two
clean builds in separate temporary trees, each excluding every prior LaTeX
auxiliary/output file, independently reproduced this hash.  One build also
regenerated the complete figure package first and still reproduced the same
PDF.  The final artifact is an unencrypted 12-page letter-size PDF; the
conclusion ends on page 9; all fonts are embedded and subset.  The build log
has zero LaTeX/package warnings, errors, box warnings, undefined
citations/references, or multiply defined labels.  Round 2 visually inspected
all 12 pages and all three original-resolution figure masters.

## Proof, result, upstream, figure, citation, and test closure

| Evidence/index artifact | SHA-256 | Verification |
|---|---|---|
| `experiments/source_lock.json` | `2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc` | prospective commitment unchanged |
| `notes/PROOF_PACKAGE.md` | `62f9dd20e687f05ed085df5fcac233bc2bfbace2f9cdc526a544403409b2d855` | all-period deductive source |
| `results/CODE_REVIEW.md` | `5c3db5e39a09070491ca8c3d1cebcb1aad5ae13d0218f76411abe20e2c25d88b` | independent `DEPLOYMENT_PASS` |
| `results/EXPERIMENT_RESULTS.json` | `9f9878247dc821d15b503abe5a3df713d5bde0f3c76690493dc1b4a98091ace4` | `CAPACITY_BOUND_CERTIFIED`, 9/9 gates |
| `results/registered_run.json` | `4ebec117a2254dc4502c7afd4094e833bc751b8a7e3bffcc16496dd0fd0ea5e3` | exactly one registered static run |
| `results/result_manifest.json` | `21d6910ec1e8e2995d4141f264dce06902f7d1787dea6f28d82346ebd54e3d79` | 8/8 hashes and exclusive result tree close |
| `experiments/proof_ledger.json` | `c411260d57947d454553094ef7bfd71222b5108f802b0479bea0d92c3dd396c3` | 20 exact IDs, zero cycles |
| `experiments/scope_ledger.json` | `c3eae19c807b955fa2d09e474aea84852b735a194f48fd1217cb3b093062f15d` | 10 admitted, 9 excluded operations |
| `experiments/upstream_bindings.json` | `654dcd13336e0dea7d4ae49a165601cae31f83db418316a5c356f1b108c40d2e` | two terminal packages, seven artifacts each |
| `experiments/official_pytest.xml` | `34915053371701fafd147dd39986b7a5eb157ff09c44f425edfd88f0a8ac17da` | official 51 tests, zero failures/errors |
| `paper/EXPERIMENT_PASSPORT.json` | `7096f178c2f0fe4beae4b64162e07daf2c1171977997b0fb6cd01d85a9824f85` | static-only and zero-target boundary |
| `paper/FIGURE_PACKAGE.json` | `cddb618ceea59feb8b38177ac9a9fd53c8fbc41ed33ac9d03f3223a2278e5fda` | 3 figures and 9 outputs indexed |
| `paper/figures/figure_reproducibility.json` | `382a3781f90110416610e470f5442e9e25ae040ee78b9523236020e75fbde434` | 9/9 outputs match isolated second generation |
| `notes/PAPER_CITATION_AUDIT.md` | `8a59c0e212037c51aaad94e508d58fb16d59636ed1cf93efebaea8d69f298c0c` | 18/18 metadata and safe-use closure |
| `notes/CITATION_VERIFICATION.md` | `457c41048b23fd13c33a3eabdda935f715cc115d858b5aa6b7d0faeaf8bf93b1` | reference/context ledger |

The finalization check independently reran 51/51 safe tests.  All 18
bibliography records are cited, with zero missing or unused keys.  All eight
manifest claims remain within the source lock.  The registered implementation
still records zero numerical candidate runs, zero target matches, no external
prime-table or generated prime-array access, no numerical logarithm, and no
Riemann-zero data access.  Static outputs are implementation/provenance
evidence only and do not replace the mathematical proof.

## Final integrity checklist

- References and citation contexts: **PASS 18/18**; no dangling, unused, or
  semantically overextended entry.
- Mathematical/data claims: **PASS 8/8 manifest claims**; main claims are
  deductive and the exact/static audit is described only as provenance
  evidence.
- Class-M repair: **PASS**; proper plus affine implies finite, explicitly
  allowing nilpotents and invoking descent of finiteness.
- Claim strength: **PASS**; no “sharp” claim remains, formal rank attainability
  is explicitly target injection, and provenance is separated from the
  linear-independence argument.
- Figures: **PASS 3/3**; 9/9 PDF/SVG/PNG outputs are byte reproducible, with no
  clipping, collision, broken glyph, or illegible label.
- Build and visual package: **PASS**; two clean builds match the approved PDF,
  all 12 pages pass visual inspection, and all fonts are embedded/subset.
- Forbidden execution/data: **CLEAR**; candidate numerical runs, target
  matches, prime tables/arrays, and Riemann-zero data are all zero/false.

## Retrospective final indexes

| Index | SHA-256 | Status |
|---|---|---|
| `paper/PAPER_CONFIGURATION.md` | `6e26f0732d14429b9be96d147870fd9b660f3a40f8b32da2dbce06c9e7f4b76b` | terminal local configuration |
| `paper/CLAIM_MANIFEST.json` | `054be395b4cfa0ae1c7e447db017d76e3bb6c7c1126f043f0a67aa3266c803ed` | valid JSON; final PDF and Round-2 review bound; eight claims unchanged |
| `paper/PIPELINE_STATE.json` | `34b6c7a6e479fe20d17dac6ec010659a5fb8d4550e0399118b45202affc2b417` | `COMPLETE_LOCAL`; Round 2 and final PDF complete |

These indexes are retrospective.  They do not rewrite the prospective source
lock or any official scientific result.  This record intentionally does not
hash itself.

## Repository handoff

Paper 5 is complete locally.  Repository synchronization remains deferred to
the five-paper batch close under the Session's scoped sync rules.
