# Final Integrity Record

Record date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Terminal status: **COMPLETE_LOCAL_FINAL_REVIEW_PASS**

This record closes the local Paper 8 manuscript pipeline after an
independent Round-2 decision of `PASS -- MAY FINALIZE`. Finalization was
strictly mechanical. It created the final release copy and updated external
release manifests; it changed no manuscript source, mathematical statement,
proof, citation, bibliography, figure, source lock, code, or result.

## Independent authorization

| Object | SHA-256 | Decision |
|---|---|---|
| `paper/reviews/round2_review.md` | `4f0da5c2174b6185a743e8834fa2a3c73b72fc4afa09b811cd730f3ad95f5d95` | `PASS -- MAY FINALIZE`, 9.2/10, zero Critical/Major/Minor findings |

Round 2 independently reproduced the approved PDF in two clean temporary
trees, reviewed the mathematics and evidence package, and authorized only a
mechanical lifecycle closure. No further scientific revision was made.

## Final manuscript binding

| Object | SHA-256 |
|---|---|
| immutable `paper/manuscript.tex` | `95ebccff1eb5f2b939be92c9a8b7020b625d4b8056cc5b6bda3b3814fcae580c` |
| immutable `paper/math_commands.tex` | `49265b2d7b07cdb2d20b9c8e612ab119a9f32d94bee27f44cec0fa3d5f683392` |
| immutable `paper/references.bib` | `0fd74e7688739c8a3eb44ea995f950250c0a9afcfc99699824bd57e753e21ba9` |
| immutable `paper/build.sh` | `860800c9488182f6101b68d8f83bc31eb43c468097f49e863164ab09fb5863b1` |
| historical `paper/paper_pre_review.pdf` | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |
| independently approved `paper/paper_round1_revision.pdf` | `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98` |
| terminal `paper/paper_final.pdf` | `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98` |

`paper_final.pdf` is byte-for-byte identical to the independently approved
Round-1 revision PDF. Its digest is therefore the approved digest, not a
newly edited manuscript digest.

The approved source and PDF retain several embedded phrases such as
“Pre-review manuscript” and “awaiting a fresh independent manuscript
review.” They are historical lifecycle labels inside the immutable reviewed
artifact. The explicit instruction that the final PDF remain byte-identical
precluded changing those bytes. They do not describe the current package
state; this integrity record and the terminal machine-readable manifests are
the authoritative release-state records.

## Review and revision chain

| Object | SHA-256 |
|---|---|
| `PAPER_PLAN.md` | `6d87e00c8cf5b21c021dfe38b572ec16d5551f576615fced4abdc72f6f70a885` |
| `notes/CITATION_VERIFICATION.md` | `4d79e865326ae7209184f42a3a204e73b189d3a3f2d9ab71c25924ea72003805` |
| `paper/reviews/round1_review.md` | `bb64f75c96ca0b3d2e78a3b295a1d1b8321ea2143f4612e08b316594991e5ac5` |
| `paper/reviews/round1_response.md` | `85b618e7a0cbd28ac4bed4cea93e3cdc7a0593a1ba7357fc9f1944650c0950eb` |
| `paper/INTEGRITY_ROUND1_REVISION.md` | `2962317aa5028baf15478c105f86ac96adae5b6a9d3c381935cccc09b700f6d3` |
| `paper/reviews/round2_review.md` | `4f0da5c2174b6185a743e8834fa2a3c73b72fc4afa09b811cd730f3ad95f5d95` |

## Terminal release manifests

| Object | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `38d64ee140b09520f34a73310aabb7634973435d727c06788c0f4eb925a63db9` |
| `paper/CLAIM_MANIFEST.json` | `9581ddf7ef1a069960f429e43f38515725c6033c8c18f6c8f25526bda1e97b0a` |
| `paper/EXPERIMENT_PASSPORT.json` | `54fd313cc29c620f127c5f205bb95b77344a1f1308ad88b69d3edcf22edb2555` |
| `paper/FIGURE_PACKAGE.json` | `cdda5fe5385f4f8005f123dade3047a95df32fd63aebb5484d4e656214c7aa05` |
| `paper/PIPELINE_STATE.json` | `00dbea0183cd525f580d845c3b886470692e40a8bc69097b3c4354b6f346492b` |

The four JSON package indexes and pipeline state parse successfully. The
pipeline hashes the configuration, claim manifest, passport, and figure
package. It intentionally does not hash this terminal integrity record;
this record hashes the pipeline, avoiding a cyclic digest dependency.

## Frozen scientific evidence

| Frozen object | SHA-256 |
|---|---|
| source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| proof package | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| raw registered result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| final result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| independent result integrity | `5f544f637ccbe9e9f584cfdd41a3188ab76153670bd5d3cdbc881ea5cbf2229d` |
| independent plan/figure/citation review | `a5e2eab53b97765bee6cedc004f4e77a29c0647c5a0186c2cd8eda7bc8262655` |
| figure machine manifest | `e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c` |
| Figure 1 PDF | `b6c0b975bc45e94da0c3e012498a507df9378239726adb2f654f6bb0225dc4ed` |
| Figure 2 PDF | `9983862ebabd20ba783441fd121925950ffffc14a9f0c397b5c1ff379d2e1789` |
| Figure 3 PDF | `b5205fbf59daf6f693318c8820419b79f2e5edc4824a0269f73d6675e0548f2f` |

All hashes reproduce their frozen bindings. Terminal finalization did not
run or extend the registered candidate, compute a new period, access an
external prime table or Riemann-zero dataset, perform a network lookup, or
open a new scientific route.

## Terminal build and PDF checks

- Two separate clean temporary paper trees were populated only with the
  approved manuscript source, macros, bibliography, build script, and three
  frozen PDF figures. Both isolated builds produced SHA-256
  `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98`.
- The two isolated PDFs compare byte-identically with each other, with
  `paper_round1_revision.pdf`, and with `paper_final.pdf`.
- Each terminal build has 12 pages, 14 bibliography items, zero BibTeX
  warning, zero LaTeX/package/citation/reference/overfull/underfull warning,
  33/33 embedded and subset fonts, and zero raster image object.
- The independently inspected approved PDF and the final PDF are the same
  bytes, so the Round-2 visual inspection of all 12 pages transfers exactly
  to the terminal copy.
- The release inventory contains the immutable pre-review PDF, immutable
  Round-1 revision PDF, and final PDF as three explicitly named lifecycle
  copies. No alternative final PDF or modified manuscript source exists.

## Terminal disposition

Independent Round 2 is complete and passed. The final local release copy and
all external lifecycle manifests are closed. Any later scientific, citation,
figure, source, code, result, or manuscript-byte change would invalidate this
record and require a new review gate.

Final status: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
