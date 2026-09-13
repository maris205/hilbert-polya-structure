# Paper20 deterministic R1 build authorization

This note records the parent authorization issued after both independent
expanded-source reviews passed.  It authorizes exactly one deterministic R1
LaTeX rebuild and its read-only validation; it does not authorize source edits,
experiments, CAS runs, transport, publication, or upload.

## Frozen inputs

| object | identity |
|---|---|
| `paper/main.tex` | 58,944 bytes / 1,552 LF; SHA-256 `67b1bf3d18fdc01be1084d969dd273bbaa1e7fe5a1677eecaa758b64ea9efbb1` |
| `paper/math_commands.tex` | 702 bytes / 20 LF; SHA-256 `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 bytes / 73 LF; SHA-256 `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 bytes / 397 LF; SHA-256 `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 bytes / 1 LF; SHA-256 `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |

## Independent source gates

- R1 final expanded-source review: `notes/INDEPENDENT_PAPER_SOURCE_R1_FINAL_EXPANDED_REVIEW.md`, SHA-256 `0eb9a4c6ccb5072e0f22c415624708ad98f9831a693e0bddce12ec9615d33795`, terminal `PAPER_SOURCE_R1_EXPANDED_PASS`.
- R2 final expanded-source review: `notes/INDEPENDENT_PAPER_SOURCE_R2_FINAL_EXPANDED_REVIEW.md`, SHA-256 `bcbf13754e6be43e6943be96d97eb8ab9d92c8703ae9cfae224cc6cba9aca077`, terminal `PAPER_SOURCE_R2_EXPANDED_PASS`.

The locked substantive body contract remains 22--26 pages (planned 24).
R0 metadata/receipt/PDF are historical and immutable; the R1 output must be
recorded separately as `main_round1.pdf` and `BUILD_RECEIPT_R1.json`.
