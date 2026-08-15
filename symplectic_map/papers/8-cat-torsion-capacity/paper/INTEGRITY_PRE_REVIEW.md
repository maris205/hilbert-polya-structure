# Pre-Review Integrity Record

Record date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Disposition: **PASS TO FRESH INDEPENDENT MANUSCRIPT REVIEW**

This record freezes the author-side Paper 8 pre-review package. It is an
integrity attestation, not an independent mathematical review of the
manuscript and not authorization to finalize the paper.

## Bound manuscript package

| Object | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `072be061acbd4ef00ecc3220449a1f872c430200becdb4e127b706d09da36ee2` |
| `paper/math_commands.tex` | `49265b2d7b07cdb2d20b9c8e612ab119a9f32d94bee27f44cec0fa3d5f683392` |
| `paper/references.bib` | `f4567be30ef6b8d6e0bc1a3a8f6a294499221de51de4064e864cbbe448b79775` |
| `paper/build.sh` | `860800c9488182f6101b68d8f83bc31eb43c468097f49e863164ab09fb5863b1` |
| `paper/manuscript.pdf` | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |
| `paper/paper_pre_review.pdf` | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |
| `paper/PAPER_CONFIGURATION.md` | `bec1ca30a45c3d44056a0f7335be29738adebd10d5fcaccea628c9cbe9c6ccc6` |
| `paper/CLAIM_MANIFEST.json` | `85f33d338f473b6b0b01eb4fbc44146b3b6366ea88b4841b59e2df7a896d5ff8` |
| `paper/EXPERIMENT_PASSPORT.json` | `bf1a0a163c8303d055854e23b1aff2cd2cd1c46f61a238517639c6c4a1fb0b71` |
| `paper/FIGURE_PACKAGE.json` | `6ac38589436ff825f9e064eeebb9981a2a314a2d44a2a4e35f79b04e0119c0bc` |
| `paper/PIPELINE_STATE.json` | `2bad0671acbaa60fbec896ea35f5c4de87a6ceec34624a700c4e656f538c276a` |
| `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `47d6fb558c847129157537de464a1c753bb677ecc9f1c1b027409561427ca277` |

The pipeline state intentionally does not hash the author audit or this
integrity record. The audit hashes the pipeline state, and this terminal
record hashes both, thereby avoiding a cyclic digest dependency.

## Frozen upstream evidence

| Frozen object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `3dd4162ac543b177d07aad8e4fb2921d7812dc1ed4d2b07320324aee0f33af35` |
| `notes/CITATION_VERIFICATION.md` | `7c984ced5d1ac9a22b61795d080393f9e8c83dabe04e2f4b612560f04fbdf779` |
| source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| proof package | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| novelty audit | `dcc30076f31099db5fb960284374819c39fdbf5f9a5c9348c19bf5ed92a22212` |
| independent source-lock review | `38ec6aaacf40da5bcf93f62916b53d6f07f18d2cfcf6d91865989875a997b951` |
| raw exact result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| final result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| official experiment report | `4cf1645505a835a9d0aa62d84e7b6b47fc708b1347a954eeac26eb9710b9187d` |
| official validation report | `ac9ac741cffd89dc8ab32db654ae59dc901b823a4b496be0607c7ce05fd403c3` |
| independent result integrity | `5f544f637ccbe9e9f584cfdd41a3188ab76153670bd5d3cdbc881ea5cbf2229d` |
| independent plan/figure/citation review | `a5e2eab53b97765bee6cedc004f4e77a29c0647c5a0186c2cd8eda7bc8262655` |
| figure machine manifest | `e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c` |
| figure provenance record | `a5f29b9fc53cfc5ea722b9083ef7f5f1ff0589b87a3ebe3d9241f4aa4d5d43a3` |

Manuscript production changed none of these frozen inputs and changed no
file under `source/`, `code/`, or `results/`. It did not rerun or extend the
registered candidate and did not access prohibited external datasets.

## Release-gate checks

- Two consecutive clean builds were byte-identical at the PDF digest above.
  The pre-review PDF has 12 pages. The terminal LaTeX log has zero errors,
  undefined citations, undefined references, overfull boxes, underfull boxes,
  or other warnings.
- All 33 PDF fonts are embedded and subset. The PDF contains no raster image
  object. Every page was rendered and visually inspected (12/12): no
  clipping, overlap, missing figure, corrupt glyph, or illegible ledger entry
  was found.
- Citation closure is 12 cited keys against the same 12 verified BibTeX
  entries, with zero missing or unused entry. The independently reviewed
  citation roles preserve positive-unit attribution, preprint status, and the
  zeta/transfer/quantum nonclaim boundary.
- All three frozen vector figures appear in the manuscript with semantic
  captions. Their nine PDF/SVG/PNG outputs reproduce byte-identically across
  two generation runs and agree with the raw exact result.
- The full determinant ledger, finite-field profiles, modulo-five counts,
  theorem/computation firewall, and clock witnesses agree with the official
  result and independent result-integrity report.
- The normalized substantive body has zero common 12-word shingles with each
  of the seven earlier project manuscripts and the legacy manuscript.
- Claim/evidence, proof logic, additive-order/period semantics, provenance,
  citation/originality/anonymity, figure/data transcription, and
  build/release-state failure modes all pass the author-side audit recorded in
  `paper/AUTHOR_PRE_REVIEW_AUDIT.md`.
- Required boundaries remain explicit: the infinite tail is proof-only;
  primitive divisibility is not claimed necessary; all torsion orders occur;
  the order clock is nonlocal/irregular and not prime-specific; native
  monodromy is torsion-order-blind; and no transfer, zeta, Fredholm,
  trace-formula, quantization, prime/zero, or priority result is claimed.

## Independence and finalization boundary

The source-lock proof, official result package, and plan/figure/citation
package have the independent checks listed above. The manuscript itself has
received only author-side production and integrity checks. A fresh reviewer
must now inspect the bound source and PDF without treating those checks as an
independent manuscript verdict.

Until that review and any bounded repair cycle close, the package remains
pre-review. `paper/paper_pre_review.pdf` is the only release copy;
`paper_final.pdf` was not created and finalization is not authorized.

Final status: `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`.
