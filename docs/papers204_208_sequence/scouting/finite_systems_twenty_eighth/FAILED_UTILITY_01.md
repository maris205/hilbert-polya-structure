# Actual missing-jq display failure

This transcribes the original terminal command and result after the event.
It is not an at-launch capture or a successful operation. No scientific code
ran and no output file was written by this failed display command.

Cwd: `/root/autodl-tmp/symbolic_dynamics`. Shell: bash. Exact command:

```text
jq '{status, snapshot_manifests, physical_snapshot_rows, discovery_scope_failure_unique_files, discoveries: [.discoveries[] | {name,searched_files,hit_lines, protected_files: (.protected_files_in_original_scope|length),protected_hit_lines_count,pattern}], completed_commands_checked, unique_path_hash_references, later_resolution_counts, unresolved_historical_bytes, zero_pin_commands: [.commands[] | select(.explicit_pin_count==0) | .name]}' docs/papers204_208_sequence/scouting/finite_systems_twenty_eighth/commands/documentary_audit_01/stdout.txt
```

Actual exit: `127`. Complete actual merged terminal output:

```text
/bin/bash: line 1: jq: command not found
```

The original terminal API returned one output field, not independently
separated stdout and stderr. The successful standard-library fallback is a
distinct recorded command at `commands/documentary_audit_summary/`; it reads
the existing audit JSON and does not modify or recreate the failed event.
