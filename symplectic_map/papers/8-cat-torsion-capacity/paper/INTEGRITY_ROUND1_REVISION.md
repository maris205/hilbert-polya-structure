# Round-1 Revision Integrity Record

Record date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Disposition: **READY FOR FRESH INDEPENDENT ROUND 2**

This record freezes the author-side Paper 8 Round-1 bounded revision. It
attests that the three minor findings in the independent Round-1 review were
implemented and mechanically checked. It is not an independent Round-2
review, does not authorize finalization, and does not authorize creation of
`paper_final.pdf`.

## Bound Round-1 revision package

| Object | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `95ebccff1eb5f2b939be92c9a8b7020b625d4b8056cc5b6bda3b3814fcae580c` |
| `paper/math_commands.tex` | `49265b2d7b07cdb2d20b9c8e612ab119a9f32d94bee27f44cec0fa3d5f683392` |
| `paper/references.bib` | `0fd74e7688739c8a3eb44ea995f950250c0a9afcfc99699824bd57e753e21ba9` |
| `paper/build.sh` | `860800c9488182f6101b68d8f83bc31eb43c468097f49e863164ab09fb5863b1` |
| `paper/manuscript.pdf` | `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98` |
| `paper/paper_round1_revision.pdf` | `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98` |
| immutable `paper/paper_pre_review.pdf` | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |
| `PAPER_PLAN.md` | `6d87e00c8cf5b21c021dfe38b572ec16d5551f576615fced4abdc72f6f70a885` |
| `notes/CITATION_VERIFICATION.md` | `4d79e865326ae7209184f42a3a204e73b189d3a3f2d9ab71c25924ea72003805` |
| `paper/reviews/round1_review.md` | `bb64f75c96ca0b3d2e78a3b295a1d1b8321ea2143f4612e08b316594991e5ac5` |
| `paper/reviews/round1_response.md` | `85b618e7a0cbd28ac4bed4cea93e3cdc7a0593a1ba7357fc9f1944650c0950eb` |
| `paper/PAPER_CONFIGURATION.md` | `53d8864ccf2a411a3cb3a8456820c4655955437c69bb9c4bb28db1eecf9b1cc1` |
| `paper/CLAIM_MANIFEST.json` | `60735a6b9cb21c1e8710772c95bead8e0e851efa6c721fd47a7c4a62479bbf86` |
| `paper/EXPERIMENT_PASSPORT.json` | `dfe788aa14217ff901cbdee6ff7f9d37b7d8c0c3e9f92260bb6d69153e636ec7` |
| `paper/FIGURE_PACKAGE.json` | `807add866bb09ead61854aa606d6cbedf41b229f80b2a18750bdc07aacadb430` |
| `paper/PIPELINE_STATE.json` | `9affad3a1d70bce6f85bd1e759928ac593c4a07a4605ad4ff1b00c7c21a79d20` |

The pipeline state intentionally does not hash this integrity record. This
terminal record hashes the pipeline state, so no cyclic digest dependency is
introduced.

## Historical and frozen evidence

| Frozen object | SHA-256 |
|---|---|
| historical `paper/AUTHOR_PRE_REVIEW_AUDIT.md` | `47d6fb558c847129157537de464a1c753bb677ecc9f1c1b027409561427ca277` |
| historical `paper/INTEGRITY_PRE_REVIEW.md` | `91ef2cc2227beccb920a67d7cfd031a2b6ed1b387a09df8174830e2772b55afb` |
| source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| proof package | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| raw exact result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| final result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| independent result integrity | `5f544f637ccbe9e9f584cfdd41a3188ab76153670bd5d3cdbc881ea5cbf2229d` |
| independent plan/figure/citation review | `a5e2eab53b97765bee6cedc004f4e77a29c0647c5a0186c2cd8eda7bc8262655` |
| figure machine manifest | `e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c` |
| Figure 1 PDF | `b6c0b975bc45e94da0c3e012498a507df9378239726adb2f654f6bb0225dc4ed` |
| Figure 2 PDF | `9983862ebabd20ba783441fd121925950ffffc14a9f0c397b5c1ff379d2e1789` |
| Figure 3 PDF | `b5205fbf59daf6f693318c8820419b79f2e5edc4824a0269f73d6675e0548f2f` |

The bounded revision changed no frozen source-lock, proof, code, result, or
figure file. The registered candidate was not run or extended; no additional
period was computed; and no external prime table, Riemann-zero dataset, or
network lookup was accessed. The two added related-work records were copied
from locally frozen citation evidence and retain narrowly delimited roles.

## Round-1 findings and closure

- **M1 closed.** Every general negative-trace/native-instability occurrence
  now uses the sign-independent quantity `n log rho(A)`, equivalently the
  logarithm of the modulus of the unstable multiplier. A static scan found
  zero stale general `n log alpha` occurrences in the revised manuscript,
  current plan, captions, and claim surfaces. Fixed positive-trace
  standard-cat evidence continues to use its valid positive `alpha` and was
  not edited.
- **M2 closed.** Related work now records the ordinary-period-set result of
  Kannan et al. (2011) and Seibt's rational-lattice period formula (2003).
  The manuscript explicitly limits both citations to ordinary/global period
  context and states that neither establishes prime additive order or the
  cross-prime carrier theorem.
- **M3 closed.** The citation ledger's terminal checklist and release state
  are reconciled. The revised manuscript cites 14 unique keys, exactly the
  14 entries in the bibliography; BibTeX reports zero warning. Revised
  source, plan, ledger, response, configuration, claim, passport, figure,
  and pipeline hashes are bound above.

These are author-side closure statements. The newly revised notation,
literature bridge, citation roles, and hash package still require fresh
independent Round-2 inspection.

## Build and regression checks

- Two consecutive clean builds produced byte-identical 12-page PDFs at
  SHA-256
  `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98`.
  The original pre-review PDF remains byte-unchanged at its historical hash.
- The terminal LaTeX log has zero errors, package warnings, undefined
  citations, undefined references, overfull boxes, or underfull boxes.
- All 33 PDF fonts are embedded and subset; the revised PDF contains no
  raster image object.
- Every page was rendered and visually inspected (12/12). The new
  first-page related-work paragraph, corrected page-7 instability notation,
  all three figures, tables, hashes, and the expanded bibliography are
  legible and uncropped, with no overlap, missing content, or corrupt glyph.
- All four machine-readable revision artifacts parse as JSON. Their embedded
  hashes agree with the bound files, the three figure hashes remain
  unchanged, and `paper_final.pdf` is absent.
- The theorem statements, exact ledger, finite-field profiles, modulo-five
  Jordan repair, negative-trace three-case proof, capacity-versus-specificity
  theorem, and all frozen nonclaims are unchanged.

## Independence and finalization boundary

Round 1 was independently reviewed and returned `MINOR REVISION` with three
bounded findings. This revision was produced and checked on the author side.
No independent Round-2 verdict has yet been issued, and this record must not
be represented as one.

The next permitted stage is a fresh independent Round-2 review of the bound
source, PDF, response, and integrity package. Finalization remains
unauthorized; `paper_final.pdf` was not created.

Final status: `READY_FOR_INDEPENDENT_ROUND2`.
