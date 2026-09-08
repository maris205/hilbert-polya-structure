# P210 artifact reader: bounded historical-interface source check

Scope: read-only interface check of `p210_terminal_artifact_revision_01/inspect_p210_artifact.py`,
principally lines 914–1263 (`round0_closure`, `round_anchor_roles`,
`successive_round_links`, `successive_round`, and the Round2 lifecycle refresh),
plus the necessary history/native/manifest helpers and actual originals.
This is not independent mathematical review, execution of the reader, artifact
acceptance, paper completion or exact-five acceptance.

Conclusion: no concrete interface/schema mismatch found in this bounded read.
The checked 914–1263 source slice has SHA256
`070b2dc625ac23b5b2ff45b191caca7ae71dd82cffe07983f9eac0058093bd92`.
The full source was observed afterward as 2,180 lines / 152,913 bytes, SHA256
`04a256596eed566148534ed5732faed886f5dfec33e222db108488a86f79ffd6`;
other branches are still being prepared and are not covered by this finding.

Evidence from separate small JSON/Markdown data reads, without importing or
executing the reader, a gate, old script or scientific/native child command:

- Round1/2 `raw_byte_comparisons` are actual lists of 1,000 / 1,016 records.
  Every row has exactly bytes/equal/left/method/right/role; bytes is a
  nonnegative int, equal is true, both operands and role are strings, and the
  method is exactly the complete-Python-bytes sentence checked in the reader.
  All non-input-map operands are physical copies inside the relevant frozen
  round. No list-versus-integer assumption remains in this branch.
- Their full source maps have 1,653 / 2,077 entries, all using
  real/sha256/size/symlink, matching `current_record`, not `convert_rich`.
  The ten declared logical-path/hash/size aliases all match their exact
  physical history files. The Round1 and Round2 control-map entries match
  their respective old control triples, rather than using a prefix fallback.
  Actual A initial aliases are a list; B initial aliases are a dict, as the
  helper's two explicit cases require.
- The literal frozen Markdown occurrence census is 57 / 71 / 86.
  The latter two equal inherited 57 + 14 and inherited 71 + 15, respectively.
  Full inherited rows, original href occurrences, and new anchor source/
  origin/physical-target/mode tuples agree with the stored provenance.
  Round0's 19 archive rows plus capsule/original-origin overrides reproduce
  its entire exact document-origin map.
- Round0's actual three cmp rows include `--`; its root's three checksum
  rows use `-c`. Their entire ordered six-row root command record, including
  reconstructed stdout and empty stderr, matches the branch.
  Round1/2's five checksum rows use `--check`; their last cmp row has no
  `--`. These differences are correctly retained.
- Both later freezer parent command strings tokenize to the exact
  `/usr/bin/env -i` ENV4 prefix plus recorded full `launch_orig_argv`.
  The script argv equals its suffix at index 6. Original sessions, native
  field names (exit / stdout_utf8 / stderr_utf8), six-command counts and
  receipt counts match: 507 / 523 copies, 2,164 / 2,603 current inputs,
  29,273 / 38,968 checks. Accepted Round1 assertions equal the actual A root
  record.
- The actual Round2 refresh summary equals its receipt minus native; its
  complete 2,021-line checksum stdout and ENV4 match the stored native row.
  The historical 1,496 → 2,021 transition is explicitly not treated as
  current terminal directory membership.

The compact data observations completed normally (50c201, 46ce49, 649121 and
64cbe4, all exit 0). An earlier oververbose schema display was truncated; it
is not relied on as full evidence, and the bounded displays above were read.
This check did not rerun all 2,016 raw operand comparisons or the broad host
maps and does not claim their full artifact-gate acceptance. No preparation,
manuscript, historical original or executable source was modified.
