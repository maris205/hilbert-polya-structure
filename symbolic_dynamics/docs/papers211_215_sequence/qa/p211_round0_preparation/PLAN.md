# P211 Round0 physical-freeze adaptation — PLAN_ONLY

2026-09-08 UTC. This is a plan, not a freeze, replay, build, audit PASS or
manuscript review. Only this file is authored in this task. Root will implement
and execute the narrowly scoped adapter after accepting the current lifecycle
documentary delta. No existing paper, seal, original or control is edited here.

## Contract and exact payload

Inherit [ARTIFACT_CONTRACT](../../../papers204_208_sequence/ARTIFACT_CONTRACT.md)
and the [project workflow](../../../research_state/WORKFLOW.md).
Current STATE/PIPELINE say initial author execution, initial build and root
five-page viewing are accepted; Round0 and actual A/B remain future gates.
The current paper README, both execution/build receipts, adoption historical
mapping and earlier execution-documentation handoff were read for their roles.
No scientific source or proof dossier was opened for this new task.

Source root: `papers/211-kernel-image-projection-feedback/`.
Destination: `papers/211-kernel-image-projection-feedback/frozen_round0/`.
The observed current inventory is exactly **32 ordinary file paths: 31 non-PDF
files plus one PDF**. It is 30 pre-build paper files, with README's accepted
lifecycle update, plus `main.pdf` and `INITIAL_BUILD_RECEIPT.md`; not 32 plus
another PDF. Bind this literal list before copying:

```text
AUTHOR_EXECUTION_RECEIPT.md
CANONICAL.json
CANONICAL_SCHEMA.md
CLAIMS_EVIDENCE.md
HANDOFF.md
INITIAL_BUILD_RECEIPT.md
NARRATIVE_REPORT.md
PAPER_PLAN.md
PARAMETER_SPECIFICATION.md
PREPARATION_PLAN.md
PROOF_PACKAGE.md
README.md
SOURCE_AUDIT.md
SOURCE_INPUT_PINS.json
SOURCE_PIN_COLLECTION_TOOL_RETURN.json
SOURCE_PREPARATION_MANIFEST.json
STATIC_CHECK_TOOL_RETURN.json
main.pdf
main.tex
math_commands.tex
parameters.json
references.bib
sections/0_abstract.tex
sections/1_introduction.tex
sections/2_image.tex
sections/3_clock.tex
sections/4_inverse.tex
sections/5_scope.tex
sources/bibliographic_metadata_web.json
sources/stein_definition_web.json
sources/stein_support_web.json
verify.py
```

The nine source-only build inputs are the eight TeX files and bibliography
in this list. The checker/parameters/schema/canonical are author scientific
evidence; proofs, claim/framing/source documents and saved source returns are
review inputs; receipts and historical seals retain their documentary roles.
The original preparation manifest remains a historical 27-payload seal, not
a current 32-file manifest.

Root's actual freeze shall require:

1. The destination is absent. Capture current exact source inventory, type,
   byte size and SHA-256 before any output. Refuse an unexpected missing/extra
   path or symlink; do not silently include new files, old auxiliary products
   or a recursively discovered `frozen_round*` tree.
2. Require the accepted README/build-receipt lifecycle bytes and unchanged
   scientific/build key established by root's pending lifecycle reception.
   Record that reception as an external pinned prerequisite, not an assumed
   PASS. Compare the current PDF to its accepted build/adoption original.
   Receipt identities are PDF 301,007 bytes /
   `532b8c462e907878c3d75829b2c4ff86de7d59c137efa91b61ebc80717a077dc`
   and canonical 1,327,062 bytes /
   `2a9d1311a491805644efa7cd4884ae50ed9f9ffa48e347b822a7ff68e12ee6b4`.
   These are cited expected identities, not new checks performed by this plan.
3. Create 32 byte-exact physical copies at the corresponding relative paths:
   no symlinks, hardlinks, pointer-only substitutes or normalization, including
   an actual `main.pdf` copy. Check ordinary-file types, distinct source/dest
   inodes and full byte comparisons. Capture source pins again and require
   every before/after/copy value to agree.
4. Write only the new `frozen_round0/SHA256SUMS` over all 32 payloads.
   Names are relative to the freeze directory (e.g. `sections/3_clock.tex`);
   the only self-exclusion is that manifest. Check exact coverage, duplicates,
   traversal/absolute paths, every raw hash and absence of extras. The freeze
   then has **33 files total**. Keep adapter, bindings, mapping, native
   command/exit/stdout/stderr records and execution result outside the freeze,
   in root's new scoped QA execution directory.
5. Preserve any failed/incomplete attempt and its native evidence; do not
   overwrite or clean it to retry. An existing destination or dependency delta
   requires an explicit new disposition from root. This plan performs none of
   these copy, byte-comparison or build/science operations.

## Reviewer input pins and external evidence

A's scientific/documentary input is the accepted physical Round0, never an
unpinned changing live paper. Its future `INPUT_PINS.sha256` resolves from the
workspace root, unlike the directory-relative freeze/review manifests.
Include the 32 reviewed frozen files and the frozen manifest as 33 explicit
workspace-root-relative inputs. Additional external records can be separate
rows with declared roles; they do not increase the physical paper payload to
a copy of the QA tree. B would instead start from a later accepted Round1;
this plan neither supplies nor anticipates A's verdict/delta.

Keep the accepted author production/pair, runtime binding/preparation, initial
build/binding, original receptions, actual visual receipt and adoption evidence
at their existing workspace paths. Root's adapter should emit a compact
external-reference/pin table outside Round0 with, for each actually consumed
item: role, logical source path, selected physical path, bytes/SHA-256, and
whether the resolution is current or a specifically mapped historical value.
Pin the complete actual dependency inputs needed by a later audit/reuse, not
merely an attractive headline receipt; use their existing sealed packages
without physically recopying large runtime/build QA directories.
A full runtime-key revalidation, new build or new viewing is not performed
by creating this reference table.

Known historical routing inputs, all workspace-root-relative:

- `docs/papers211_215_sequence/qa/p211_author_source_reception/source_preparation_original/`:
  the 28 unchanged source-preparation originals, including their original seal.
- `docs/papers211_215_sequence/qa/p211_author_execution_documentation01/ORIGINAL_MAPPING.json`:
  the five pre-documentary-edit source/document originals. The older
  `PROTECTED_INPUTS.initial_scope.sha256` is explicitly historical.
- `docs/papers211_215_sequence/qa/p211_initial_build_adoption01/HISTORICAL_MAPPING.json`:
  pre-build-lifecycle STATE, PIPELINE and paper README mapped respectively to
  `originals/SYMBOLIC_DYNAMICS_STATE.md`, `originals/PIPELINE_STATE.md`,
  and `originals/P211_README.md` inside that same adoption directory.

For example, an old README pin from before the latest lifecycle change
resolves only through the last exact historical mapping, not to the new frozen
README. Do not relax a hash mismatch, refresh an old seal, overwrite a mapping,
or route every similarly named historical version to the same snapshot.
Follow the claimed historical version's explicit mapping and verify its bytes.
This freeze plan does not recursively re-audit the whole infrastructure.

## Original-location Markdown links

Do not edit copied Markdown to make relocation appear link-clean.
For each copied Markdown file retain the pair
`(frozen path, original workspace paper path)` in the external mapping:

1. Parse a local link using the **original document directory** as its base,
   retaining the original token and any fragment. Normalize/validate the
   filesystem target separately; web/mail links are not filesystem inputs.
2. If the resolved target is one of the 32 selected paper files, route to its
   corresponding physical Round0 copy and verify the frozen pin.
3. Otherwise retain its original workspace-root-relative external target and
   use the external role/pin table. Directory references require their explicit
   sealed scope; directory existence alone is not proof of evidence closure.
4. Links to lifecycle indexes are navigation, not substitutes for historical
   proof pins. Record whether a target is an observed current index or a
   historical pin reference; resolve the latter through its exact mapping.

Concrete example: the frozen README's
`../../docs/papers211_215_sequence/PIPELINE_STATE.md` is resolved from the
original paper README's directory, yielding
`docs/papers211_215_sequence/PIPELINE_STATE.md`; naïve resolution from the
extra `frozen_round0/` level is wrong. Its `main.pdf` link instead resolves
to the frozen PDF. Apply the same declared-origin rule to unchanged historical
pin-list bases; do not pretend all JSON/SHA entries are relative to the freeze.

## Authorship and future B boundary

Agent: `/root/round211_rational_scout/relation_primary_sources`.

- **P211 mathematical or scientific-verifier contribution: none.**
  I supplied no KIP theorem, formula, proof repair, scientific algorithm,
  `verify.py` implementation or canonical production.
- **P211 manuscript/source contribution: no paper TeX/Bib or prose edit.**
  Earlier, under the source-only build-preparation assignment, I fully read
  all nine TeX/Bib source files, including mathematical body text, and the
  permitted build-plan section. Thus I am familiar with the author manuscript;
  I must not be described as blind or as having never read its mathematics.
- **Infrastructure source contribution: yes.** I authored the initial-build
  preparation/adapter and authorized infrastructure revisions/diagnostics in
  `qa/p211_build_preparation/`. This is code authorship, but not scientific
  or manuscript authorship. I cannot independently certify that same
  infrastructure as if I were its nonauthor reviewer.
- In this task I read only instructions, current phase/navigation records,
  README, execution/build receipts, the two relevant historical documentary
  records and filename layout. I did not reopen proof/verifier/canonical bodies,
  execute a submitted program, read a review A, or begin review B.

Root must determine any future mathematical B eligibility from the complete
contribution record and enforce a genuinely different proof representation
from author and A. Infrastructure familiarity is disclosed, not concealed as
independence; this plan assigns me no B role. Any later mathematical/proof
contribution would make me ineligible to review that contribution.

The new-plan directory was absent when checked (ordinary `ls` exit 2);
that observation is not a failed freeze or a claimed audited absence key.
The initial combined status display was truncated; only the current phase and
the separately read batch tail are used, not an asserted full historical read.
No extra framework, pilot, build, PDF view, A/B review or Git operation was
performed. `OWNER_AMBER / HOLD_EXTERNAL` remains unchanged.

