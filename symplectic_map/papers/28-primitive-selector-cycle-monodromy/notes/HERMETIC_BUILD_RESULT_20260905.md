# Paper28 first captured-only build: stopped, preserved

Date: 2026-09-05. Actual execution session: 17361, exit1.

Decision: `BUILD_FAILED_PRESERVED_NO_RETRY`. This is an actual first-pass dependency failure, not a completed PDF, not a source defect established by this run, and not a two-root or publication acceptance.

## What ran

The user's “确认，下一轮” was consumed for the executable-profile implementation/review and its one-shot governed local execution. `paper-compile` supplied log/page/font/visual-check discipline under the existing stricter immutable-source, captured-only, fixed-pass and preserved-failure contract.

The final prospective independent review passed and bound the controller, plan, loader selection and PDF validator before the new root was created. The controller rechecked all12 sealed CAPTURE2 outputs and all6838 archive members, then exclusively created `build-capsule-20260905`. No old build/capture root was reused or repaired.

The captured namespace was materialized, including the declared null device. The first pdfTeX child passed its chroot, identity/capability drop, no-new-privileges and parent-ownership setup; it actually loaded the captured loader, executable, configuration and precompiled pdflatex format. This establishes those operations for this child only, not all role loading or runtime dependency completeness.

The sole publication child was r0/01-latex, pid903265, returncode1, elapsed0.17036886513233185seconds, timeoutfalse, reapedtrue. The remaining BibTeX/LaTeX/PDF-inspection commands were not dispatched; r1 was not materialized. No PDF was produced.

## Actual cause and scope

The preserved log reports at captured `fontenc.sty:112`:

```text
Font T1/cmr/m/n/10.95=ecrm1095 at 10.95pt not loadable:
Metric (TFM) file not found.
```

The locked source loads `fontenc` with T1 encoding before `inputenc` and `lmodern`. Thus the initial Computer Modern selection requests EC metric `ecrm1095.tfm` before the later Latin Modern switch. Read-only inspection of the already captured manifest finds zero `ecrm1095` entries and zero entries under `/fonts/tfm/public/ec/`, although596 Latin Modern and75 Computer Modern metric files are captured. This is the concrete captured-dependency omission exposed by the actual run. It does not prove that this is the only possible downstream missing input.

No live-host EC directory, metadata or file content was inspected after this discovery. No package installation, font generation, new capture, source reordering, validator relaxation, host fallback or automatic second attempt was performed. Static capture-recording and prospective profile PASS records retain their original limited meanings and are not rewritten to conceal this runtime failure.

## Preserved evidence and integrity

All files under the execution root and the frozen control/review files remain as executed. The controller failure record seals the preceding evidence and reports the complete materialized readonly-input snapshot unchanged. Original source hashes and the isolated source copies remained bound. The failure-input and before-input manifests are each1801218bytes and share SHA256 `44a030aa74e5f84e01d0d283fc72bbbcd38255bbe8dac034f5be6b856b907984`.

| Artifact | SHA256 |
|---|---|
| notes/HERMETIC_BUILD_20260905.py | `3081c6c677fac2ac4adca4fe34066289708875e9280bce2a035a517653a1b098` |
| notes/HERMETIC_BUILD_PLAN_20260905.md | `dddff3b541e91d8175934e64a551f74d6ad74a55de9232e617e655076e322be8` |
| notes/PDF_ACCEPTANCE_20260905.py | `e173a8a54d051f8d296b5d1319a44bdea0f30d3ab0be91cc16747027bf9a126c` |
| notes/LOADER_SELECTION_20260905.json | `ecc5e3751def20eac1bb96a2ddb5336925d46cf8fcb80b5ee60f4ab25bed9606` |
| notes/HERMETIC_BUILD_REVIEW_20260905.json | `fe49cec6d57a1d678c59eb593397e01be71650777a2c90211f64510c4f3d8d2a` |
| build-capsule-20260905/evidence/failure.json | `eb3814163d9ebac4e58b60dc75f637b685b0f17fa0872c8509e924b2f5962afd` |
| evidence/r0-01-latex/status.json, relative to the build root | `e3000bf7f2f57b4b4f2721cec841bb350925582ce6bcfd96b59c33e82ef39c6c` |
| evidence/r0-01-latex/main.log, relative to the build root | `dcd6c6e39cbe4e05ac2d4069b9cde8865ca0f0f3f9159a8dafef2b2970816a92` |
| evidence/r0-01-latex/main.fls, relative to the build root | `014fc8e9f09f2302e635cbe97dc743ca07c318964c56c29a302b56e97fcc732e` |

The original manuscript remains:

- main.tex: `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e`.
- math_commands.tex: `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5`.
- references.bib: `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e`.

The separate independent post-failure note, `HERMETIC_BUILD_FAILURE_AUDIT_20260905.md`, gives `FAILURE_RECORDING_INTEGRITY_PASS`, not a build PASS. Its SHA256 is `80df476a1eadb1267d08979068ada42f7bee08f19e1e3bc6736b8438f818b157`. It verified16 sealed regular evidence files plus failure.json (17total), both evidence directories, source immutability, identical input snapshots and absence of the requested metric in the manifest/aliases.

## Next action requires the user's brief confirmation

Proposed successor: keep CAPTURE2, this failed build and all original controls/evidence immutable; perform a narrowly bounded supplemental capture of the now-identified EC font metric and any directly demonstrated necessary metric dependency, with a prospective exact inventory/budget/read-before-intent discipline and independent review. This is not permission to recapture broad host trees, install packages or increase the existing resource budget. Then bind the audited supplement alongside the unchanged original capsule in a reviewed successor controller and execute in an entirely fresh evidence/build root. Do not reorder or edit the manuscript to sidestep the missing dependency.

No supplemental host read or successor execution is authorized merely by this result note. A short user “确认” responding to this proposal is sufficient; do not request a long authorization formula. Until then, do not rerun the frozen controller or re-enter its failed root for mutation.

Paper27 stays locally accepted, Paper28 remains incomplete, Papers29–31 remain pending: Batch07 is still1/5 locally completed and the cross-paper audit is unfinished. No external publication operation occurred.
