# Evidence limits and documentary failures

Scientific counters are exactly those in INTAKE.md: three literal
descriptions, zero admissions, zero pilot boxes, zero enumerated states,
zero scientific kernels/runs/replays. Deductive examples are not experiments.
No manuscript, candidate-gate or independent-review result is produced.

## Documentary provenance

`capture.py` captures a command's full stdout/stderr bytes, argv, working
directory, exit status and stream hashes. It refuses existing output paths.
Its seven pre-audit command receipts cover discovery, three text searches,
one successful primary HTML retrieval, one unsuccessful filename resolution,
and the successful full P175 original read. An exit 0 for `rg` means matches
were returned; it does not certify a collision-free historical corpus.

The final version of `capture.py` is sealed with this dossier. It was edited
to add focused and then structural search during intake; no whole-runner
source hash was recorded before each earlier command. Four named binaries
(`rg`, `python3`, `pdftotext`, `curl`) were observed and pinned after the first
search. This is not at-run runtime closure: standard-library files, shared
libraries, dynamic loaders, environment and every executable dependency were
not frozen. `pdftotext` was only pinned, not used to inspect a paper here.
There is no hermetic or independent replay claim.

Each of the three exact search pinsets has 5,435 entries and a matching
at-time after pinset. The current-state audit does not refresh those pins.
When an indexed lifecycle document changes, an alias is accepted only if a
physical captured copy has exactly the originally pinned digest, and the
audit records the original path, expected/current digest and physical path.
Scientific-original drift is a failure, not silently repaired by an alias.
Later new files are not retroactively inserted into the selected list.

The audit script and retained audit command streams check the saved receipts,
physical snapshots, named binary pins, selected-list membership, all three
before/after pinsets and current drift/aliases. They are documentary checks,
not verification of the mathematical deductions. The non-self SHA256SUMS
seals the resulting dossier; a successful checksum pass attests bytes, not
novelty or theorem acceptance.

The retained `evidence/documentary_audit/stdout.bin` reports PASS: 26
physical snapshots checked, all 16 historical originals still exact, all
seven pre-audit command streams matching their receipts, and all four named
binaries unchanged relative to their observed pins. The three current
search comparisons are 5,434/5,435, 5,435/5,435 and 5,435/5,435 exact.
The one initial-search drift is the batch pipeline index, resolved by the
explicit same-digest physical alias in that audit's `aliases` array. No
Git-object fallback was needed. This is a timestamp-local audit; later
root integration can legitimately change live lifecycle inputs again.

## Retained unsuccessful attempts

1. An initial helper discovery queried the skill's arXiv area and a
   nonexistent local `tools` directory. The visible tool return included
   `rg: tools: No such file or directory (os error 2)` and the overall
   pipeline returned 1. No helper was found. This error is a copied
   tool-return observation, not a retrospectively invented raw command log.
2. A guessed P175 slug read failed with exit 2:
   `sed: can't read papers/175-diagonal-commutator-dynamics/main.tex: No such file or directory`.
   This is also a copied tool-return observation; its original command
   streams were not separately archived by the documentary recorder.
3. The next resolution command guessed two other P175 slugs and failed
   with exit 2. `evidence/resolve_p175/` preserves its exact argv, empty
   stdout and full stderr. The actual slug was then resolved from the
   discovered file list, and `evidence/p175_original/` retains the successful
   complete original read. The earlier failure is not replaced.
4. A guessed CS-gate filename failed with exit 2:
   `sed: can't read docs/papers204_208_sequence/scouting/algebra/CS_GATE/SOURCE_AND_PROOF.md: No such file or directory`.
   This is a copied tool-return observation, not a captured raw stream.
   The actual `CANDIDATE_GATE.md` was subsequently read and physically
   snapshotted. No content is attributed to the missing file.

Unavailable Zotero/Obsidian tools and PDF metadata-only browser responses
are capability/source-scope limitations, not successful primary-body reads.
No source, mathematical or runtime result is inferred from these failures.

## Handoff boundary

ASC is KILL_FIXED_STRATUM_LINEARIZATION; UTR is KILL_LITERAL_INTERNAL;
EMD is HOLD_PROOF_SOURCE / NO_PROMOTION, not an admitted reserve. Its exact
one-step inverse is useful partial mathematics but does not close the
two-axis gate. Root may review and integrate this sealed negative intake.
Nothing here starts another scout, assigns P210, claims the fifth paper,
performs Git synchronization or relaxes HOLD_EXTERNAL.
