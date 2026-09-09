# C426 final-build handoff

**Status:** `FINAL_BUILD_COMPLETE_PENDING_SEAL`. Both actual nonauthor
manuscript rounds completed; all three adopted corrections closed, no
second-round findings. Two fresh fixed-input final builds succeeded
and their PDFs compare byte-identical; all ten final pages were viewed.
See `PAPER_IMPROVEMENT_LOG.md` for the full report, exact diff and real
revised build. This is not final
release, external submission or an additional admitted contract.

Read [main.pdf](main.pdf), [SOURCE_AUDIT.md](SOURCE_AUDIT.md) and
[BUILD_LEDGER.md](BUILD_LEDGER.md), and the current
[FINAL_BUILD_REPORT.md](FINAL_BUILD_REPORT.md). The full mathematical body has no
external Markdown-only proof dependency.

## Complete editable manuscript source list

1. `main.tex` — 11pt anonymous article, deterministic PDF settings.
2. `references.bib` — four primary public references and the actual
   unpublished GR5 working package; no invented human author.
3. `sections/01_introduction.tex` — contribution and source subtraction.
4. `sections/02_classification.tex` — all-coefficient, all-affine theorem.
5. `sections/03_local_rigidity.tex` — complete highest-term and
   indeterminacy necessity proof.
6. `sections/04_local_test.tex` — all-characteristic finite centre test,
   coefficient formulas, unique-disc proof and wild-centre example.
7. `sections/05_global.tex` — finite support, centre CRT patching,
   determinant necessity, two-generator lemma, explicit basis,
   sufficiency, all models and terminating arithmetic prescription.
8. `sections/06_examples.tex` — complete fixed-field/degree corollary,
   nonprincipal two-torsion repair and three-torsion failure.
9. `sections/07_scope.tex` — exact exclusions and AI/evidence disclosure.
10. `tables/source_scope.tex` — substantive exact source-scope table.

Every listed section/table is included from the source tree. The
source archives and persistent build logs distinguish the actual
first compile from its sole layout correction. No mathematical
program was run. The source packages in `continuation_round5/`
were read but not altered.

The local `paper-figure` workflow was used only for the typeset
comparison table; `paper-compile` supplied real PDF, log, font,
text and page inspection checks. The batch plan overrides ML
venue quotas and external-model review defaults. Both manuscript rounds
and the final build pair are complete. The historical improvement
log/state and BUILD_LEDGER retain their earlier review/build milestones;
FINAL_BUILD_REPORT is the authoritative later final-build receipt.

`main.pdf` is selected from `builds/final_02/main.pdf`, which is
byte-identical to `builds/final_01/main.pdf`: 10 pages, 343725 bytes,
SHA-256 `d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db`.
`FINAL_INPUTS.sha256` and both `input_source.tar` files fix the same ten
unchanged editable inputs. Both fresh builds exited 0, each using
three engine and two BibTeX passes. Final logs and references are
clean, all 20 fonts are embedded, and complete text/page checks passed.
Original and review PDFs, source archives and logs remain intact.

The writer stops at this handoff. Formal evaluation, payload sealing,
independent membership verification and Git integration remain separate
coordinator-owned gates; no release or external submission is claimed.
