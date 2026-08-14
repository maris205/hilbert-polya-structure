# Pre-review integrity record

Date: 2026-08-14  
Paper ID: `finite-additive-arithmetic-capacity-lma-v1`  
Candidate ID: `additive_finite_arithmetic_capacity_v2`  
Status: **PRE_REVIEW_COMPLETE / READY_FOR_FRESH_INDEPENDENT_REVIEW**

## Scientific outcome

For a fixed exact additive readout
`log p = v_p + log q_p + alpha_p`, with `v_p` in one finite-dimensional
rational space `V`, `q_p > 0` algebraic and `q_p^2` a unit away from one fixed
finite rational-prime set `S`, and `alpha_p` real algebraic, the manuscript
proves

`#hits <= dim_Q(V) + |S|`.

A rational dependence among selected outside-support `v_p` terms yields
`log R = beta` with `R > 0` algebraic and `beta` algebraic.
Hermite--Lindemann forces `beta=0` and `R=1`; squaring and taking a place over
each distinct outside prime forces every relation coefficient to vanish. The
argument needs no prior finiteness assumption.

The paper gives L/M/A source certificates, makes the selector construction a
corollary, and states the escape boundary only as necessary certificate
failures. Deninger and Connes--Consani are presented as positive arithmetic
architectures outside the finite boundary. The result is not framed as a
universal no-go theorem, complete trichotomy, priority claim, or Route-B,
Riemann-zero, trace-formula, zeta, determinant, or quantization advance.

## Official static-audit closure

| Artifact | SHA-256 | Verification |
|---|---|---|
| `experiments/source_lock.json` | `2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc` | prospective lock unchanged |
| `results/CODE_REVIEW.md` | `5c3db5e39a09070491ca8c3d1cebcb1aad5ae13d0218f76411abe20e2c25d88b` | independent `DEPLOYMENT_PASS` bound to exact tree and lock |
| `experiments/proof_ledger.json` | `c411260d57947d454553094ef7bfd71222b5108f802b0479bea0d92c3dd396c3` | 20 exact IDs, zero cycles |
| `experiments/scope_ledger.json` | `c3eae19c807b955fa2d09e474aea84852b735a194f48fd1217cb3b093062f15d` | 10 admitted, 9 excluded operations |
| `experiments/upstream_bindings.json` | `654dcd13336e0dea7d4ae49a165601cae31f83db418316a5c356f1b108c40d2e` | two actual terminal packages, seven artifacts each |
| `results/EXPERIMENT_RESULTS.json` | `9f9878247dc821d15b503abe5a3df713d5bde0f3c76690493dc1b4a98091ace4` | `CAPACITY_BOUND_CERTIFIED`, 9/9 gates |
| `results/registered_run.json` | `4ebec117a2254dc4502c7afd4094e833bc751b8a7e3bffcc16496dd0fd0ea5e3` | exactly one registered static run |
| `results/result_manifest.json` | `21d6910ec1e8e2995d4141f264dce06902f7d1787dea6f28d82346ebd54e3d79` | 8/8 hashes and exclusive result tree close |
| `experiments/official_pytest.xml` | `34915053371701fafd147dd39986b7a5eb157ff09c44f425edfd88f0a8ac17da` | 51 tests, zero failures/errors |

The registered executable ran no numerical candidate, computed no target
match, generated no prime target array, and accessed no external prime table
or Riemann-zero data. Its outputs are implementation/provenance evidence, not
a substitute for the mathematical proof.

## Manuscript, figure, and citation package

| Artifact | SHA-256 | Verification |
|---|---|---|
| `PAPER_PLAN.md` | `f3bd08b782afc08bb9e3ddde0dd581e073fa0aa6001700dd8840fd31000766fc` | claim-driven paper plan complete |
| `paper/manuscript.tex` | `10dec98b3c36c03c168f2f47aa77ddf95f790b3084c38149d8ea6cdb9b9ba1b8` | complete source |
| `paper/references.bib` | `88bf55d604f7f11f855892f6248663823ba8caa4c17f9c3b3d0d1f1f5e43d10f` | 18 cited entries |
| `notes/PAPER_CITATION_AUDIT.md` | `8a59c0e212037c51aaad94e508d58fb16d59636ed1cf93efebaea8d69f298c0c` | 18/18 primary-metadata and safe-use checks |
| `notes/CITATION_VERIFICATION.md` | `457c41048b23fd13c33a3eabdda935f715cc115d858b5aa6b7d0faeaf8bf93b1` | verification protocol and boundary ledger |
| `paper/figures/figure_reproducibility.json` | `d43819b88619ecd6075d67ceb2f9f9008ef34644941a33124d593e50f216bdfc` | nine visual outputs match isolated second generation |
| `paper/paper_pre_review.pdf` | `1be29012762238bd469a2b5e86cbc32a76e9c951ed6e524917c99bf05c0a2810` | immutable pre-review snapshot |

The invalid Parry--Pollicott DOI reported in a prior research note was removed;
the official NUMDAM record is retained. Deninger's article uses the formal
*Indagationes Mathematicae* 37(1) (2026), 25--136 metadata. The final citation
closure has zero missing and zero unused bibliography keys, no placeholder
citation, and no raw arXiv URL in the manuscript.

Three reproducible figures use only five allowlisted official machine-readable
inputs. Their fail-closed loader rechecks the lock, reviewed tree, classification,
nine gates, proof/scope ledgers, upstream packages, and all zero-target flags.
PDF/SVG vector masters plus 300-dpi PNG copies were regenerated twice with
byte-identical results. Original-size inspection caught layout overlap in the
first draft; the repaired masters and all three final placements pass visual
inspection.

## Compile and visual closure

- `paper/build.sh`: four LaTeX passes plus BibTeX under fixed
  `SOURCE_DATE_EPOCH`.
- Two consecutive builds: identical SHA-256
  `1be29012762238bd469a2b5e86cbc32a76e9c951ed6e524917c99bf05c0a2810`.
- Output: unencrypted 11-page letter-size PDF; conclusion ends on page 9.
- Final log: zero LaTeX/package warnings, errors, box warnings, undefined
  citations/references, or multiply defined labels.
- Fonts: all embedded and subset.
- Visual inspection: all 11 pages and all three original-size figure masters
  pass after the layout repair.

## Retrospective indexes

| Index | SHA-256 | Status |
|---|---|---|
| `paper/PAPER_CONFIGURATION.md` | `d129b058e17bf6c6a0ad9d5eed2bf2e87a83f0d89e9a521b39581fea590e86e4` | pre-review configuration |
| `paper/CLAIM_MANIFEST.json` | `117138089a5d69abf96704289525d2c843050d623d242cbc384831ab8bfc346c` | eight scoped claims |
| `paper/EXPERIMENT_PASSPORT.json` | `126fb14f23913cbb9038ab84ca6c3be9c82ce7473f63fb8863d4e14c239951cb` | static-only execution boundary |
| `paper/FIGURE_PACKAGE.json` | `29b2e9071f4f7205d307162dfc9d4f0a4b8dc88c0a0f60e52557b8990cd4066a` | three figures, nine outputs |
| `paper/PIPELINE_STATE.json` | `176f411f84f0c91c06dd7983298404d5fb39931df105a00d630fc3bda374f5ea` | `PRE_REVIEW_COMPLETE` |

These indexes are retrospective and do not modify the prospective source lock
or any official result. This integrity record intentionally does not hash
itself.

## Independence boundary and handoff

This is an author-side pre-review integrity check, not an independent manuscript
review. The paper-writing pipeline stops here by design. The immutable PDF is
ready for a fresh independent Round-1 reviewer. Repository synchronization
remains deferred to the five-paper batch close under the Session rules.
