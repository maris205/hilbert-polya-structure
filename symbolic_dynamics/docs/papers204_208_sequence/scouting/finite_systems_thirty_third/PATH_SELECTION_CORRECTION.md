# Initial path selection rejected before body search

The initial documentary discovery selected 1,239 actual files, each passing
its original depth grammar and filesystem checks. Its tool display was
truncated. Manual inspection of the displayed paths caught reviewer/gate
ambiguity: e.g. `scouting/mip_hostile_gate/PROOF_REDERIVATION.md` was selected,
as were title inventories. These are not acceptable original-body discovery
inputs. No selected-file body search had run; this was a filename-only scope
failure, not a prohibited scientific-body access.

The original `record.py`, `SELECTED_ORIGINALS.json`, raw filename discovery
and native receipt remain unchanged. `record_v2.py` adds an explicit exclusion
for every gate directory and title inventory. It excludes the entire
finite_systems_nineteenth lane, whose original dossiers interleave FTH with
other scouts. Named OFS/FTH and numeric papers/208-* /209-* were already
excluded. The batch label papers204_208_sequence is a container, not P208.

`SELECTED_ORIGINALS_V2.json` is the corrected path set. Command 02 emits every
actual selected path and checks regular-file existence and complete structural
grammar, with full before/after pins, before any body search. This correction
does not rewrite or retroactively relabel the failed initial selection.
