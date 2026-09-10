# Independent review of the C429–C433 release policy

Review completed at the observed 2026-09-09 21:26 UTC checkpoint.
**POLICY ACCEPTABLE AS WRITTEN; ZERO POLICY MUST-FIXES.** This is a
bounded policy/input-structure review, not release approval, a final-build
receipt, mathematical review or a claim that the live tree is quiescent.
The five final-build gates remain unauthorized/pending the manuscript
review process at this handoff. This review is frozen on completion.

Reviewed policy: [README.md](README.md), SHA256
`e7f78e2e84d1d0701ae2da7b72d5bdcd13ee8b571128dd66c19b6b30f49685ad`.
Any subsequent policy edit requires a relevant readback; this verdict
binds the bytes above.

## Policy findings

- The intended root is explicitly the absolute
  `/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433`,
  not the initial `henon_zeta` working directory. The policy correctly
  assigns root identity to the coordinator: the generic verifier's ledger
  does not bind an absolute root or know which batch was authorized.
- Exact membership includes all actual regular files, including ignored
  build/QA outputs, hidden files, historical snapshots and bytecode. Only
  root `PAYLOAD_LEDGER.json` and `MANIFEST.sha256` are absent from the
  payload ledger; the manifest includes the ledger and excludes itself.
  There is no undocumented cache exclusion or permission to delete an
  inconvenient member. Symlink/hardlink/special-file/empty-directory
  rejection matches the actual unchanged code.
- The candidate is generated and reviewed outside the root; the approved
  canonical ledger bytes and an outside literal trust pin are separate.
  Rehashing a changed live ledger is not approval. The policy correctly
  requires actual new-tree operations despite reuse of historical code
  regression evidence.
- Two preflights precede manifest publication; an existing manifest is not
  replaced. Quiescence, ordinary stability checks and the limits concerning
  hostile concurrent writers, crashes, rollback and authenticity are
  correctly distinguished. Post-seal records remain outside the root.
- The continuous-run user override is preserved: five complete papers form
  a saved checkpoint, not a stopping condition. Later work belongs in a new
  unsealed batch; it does not reopen this sealed payload. No external
  submission, Route B or unrelated-stream authority is inferred.

## Concrete compiler-input findings

The following is a source-definition snapshot, not the eventual approved
input ledger. It includes the local files reached by current manuscript
input declarations and the local bibliography. System TeX packages/classes,
fonts, bibliography styles and configuration are separate toolchain inputs
whose actual versions and recorder output must be retained at final build.

| Current paper directory under `papers/` | Local compiler-input structure observed |
| --- | --- |
| `C429_polynomial_periodic_rigidity` | `main.tex`, `math_commands.tex`, `references.bib`, seven `sections/*.tex`: 10 local inputs; system `plain.bst` |
| `C430_native_galois_fields` | `main.tex`, `math_commands.tex`, `references.bib`, nine sections including `00_abstract.tex`: 12 local inputs; system `plain.bst` |
| `C431_optimal_cycle_measures` | `main.tex`, `references.bib`, seven sections numbered `1_` through `7_`: 9 local inputs; macros are inline, no `math_commands.tex`; system `plain.bst` |
| `C432_local_global_reversibility` | `main.tex`, `references.bib`, seven sections, **`figures/TABLE_local_places.tex`**: 10 local inputs; macros are inline; system `amsplain.bst` |
| `C433_inseparable_finite_products` | `main.tex`, `references.bib`, eight sections: 10 local inputs; extensionless section declarations resolve to `.tex`; macros are inline; system `plain.bst` |

The material build-preparation finding is C432's nested input:
`sections/05_places.tex:68` reads `figures/TABLE_local_places.tex`. A
generic copy of only `main.tex`, bibliography and `sections/` would omit
an actual compiler dependency. The table has no additional file-input
declarations in the inspected source. Preserve the paper-root-relative
layout in both fresh final builds and input archives. Do not manufacture
missing `math_commands.tex` files for the three inline-macro articles.

C430 `references.bib:93–94` contains relative `href` targets
`../C431_optimal_cycle_measures/main.pdf` and `main.tex`. They are
**distribution/proof-access dependencies, not TeX compiler inputs**:
the link declaration does not cause C431 to be compiled into C430.
The policy correctly requires the companion distribution. Keep the selected
delivered `main.pdf` files at the sibling paper-directory level; a nested
build copy viewed in isolation need not resolve the same relative links.
This review does not reassess the mathematical sufficiency of that citation.

All 51 listed local inputs were present as regular files with link count
one at inspection. Their named `sections/` directories, C432 `figures/`,
the five named paper roots and each named ancestor from `/` to `papers/`
were observed as directories, not symlinks. No paper-root `.latexmkrc`,
`latexmkrc`, local `.sty`, `.cls`, `.bst` or shell build driver was found
in the bounded top-level check. These are observed current-source facts,
not a recursive whole-tree/snapshot/concurrency certification. Final output
directories do not yet have an authorization or safety receipt from this
review; their full ancestor chains and nonexistence must be checked when
the coordinator authorizes construction.

Deterministic PDF controls differ across the current main files. For
example C429 suppresses the trailer ID and pTeX information, C432 suppresses
the trailer ID, and C430/C431/C433 do not declare those same controls in
their main files. This is **not an established reproducibility failure**:
none of the final pairs has been run here. Preserve each reviewed source,
the fixed epoch/environment and actual toolchain, and let the authorized
two-fresh-build byte comparison decide whether a further targeted metadata
repair is required. Do not silently normalize the five sources or declare
their PDF bytes deterministic from the environment setting alone.

## Actual read extent and non-execution boundary

The reviewer fully read the root/Hénon/batch AGENTS, the Hénon batch skill
and complete workflow, and relevant current-state/BATCH_PLAN release
sections during the immediately preceding read-only reconnaissance.
That work also fully read the unchanged 279-line `exact_payload.py`,
315-line tests, 100-line helper README and complete historical test
receipt, the complete C424–C428 release policy/final-build summary and
the separate membership checker's actual code. The two source hashes
were freshly measured and matched the policy's literals. The policy's
reported coordinator read extent/environment observations are not being
relabelled as additional reviewer execution.

This review fully read the new release policy, all five current `main.tex`
files and both referenced `math_commands.tex` files. It inspected file-input
and path declarations throughout the current sections/bibliographies,
followed the C432 nested table dependency, and checked C430's actual
companion link declaration. It performed only the described bounded file
type/link-count/path and policy-digest checks. It did not fully reread the
mathematical sections, citation sources, retraction records or reviews.

No inventory, seal, verifier/test invocation, fixture, compiler, renderer,
mathematical program, new release/build code, external API, Git mutation,
source edit or shared-index edit occurred. The only created file is this
exclusive review. Live paper sources may still change; the final approved
input sets must be re-established after their writers stop. No prior test
receipt is presented as a new test run, and no final-build gate is closed.

`NO_BAD_EULER_OR_ROOT_NUMBER`.
