# Actual local executions and byte comparisons

2026-09-05 UTC, workspace root `/root/autodl-tmp/symbolic_dynamics`.
Runtime checked directly: Python 3.12.3; Bash process substitution; stdlib
only. `-B` disables new bytecode caches. A cache left by an earlier pilot
import is non-input runtime residue, excluded from this evidence package.

Full direct executions of both pilot scripts produced the complete JSONL
streams stored as INITIAL_CANONICAL.jsonl and ADDITIONAL_CANONICAL.jsonl.
The direct first execution of verify_controls.py returned exit 0 and the
entire JSON object stored as CONTROLS_CANONICAL.json (655,223 assertions).
All three canonical files preserve the trailing LF. The control script
imports both literal update modules, so all three scripts are pinned.

The following are six **new actual executions**, not archived-hash checks.
Each command was run separately through `/bin/bash`, with cwd at the
workspace root. Here `lane` is a display abbreviation for
`docs/papers204_208_sequence/scouting/combinatorial_second`, not an
unrecorded environment dependency:

| Fresh execution | Exact command after expanding `lane/` | Exit | Complete stdout |
|---|---|---:|---|
| Initial 1 | `cmp lane/INITIAL_CANONICAL.jsonl <(python -B lane/pilot_initial.py)` | 0 | empty |
| Additional 1 | `cmp lane/ADDITIONAL_CANONICAL.jsonl <(python -B lane/pilot_additional.py)` | 0 | empty |
| Controls 1 | `cmp lane/CONTROLS_CANONICAL.json <(python -B lane/verify_controls.py)` | 0 | empty |
| Initial 2 | `cmp lane/INITIAL_CANONICAL.jsonl <(python -B lane/pilot_initial.py)` | 0 | empty |
| Additional 2 | `cmp lane/ADDITIONAL_CANONICAL.jsonl <(python -B lane/pilot_additional.py)` | 0 | empty |
| Controls 2 | `cmp lane/CONTROLS_CANONICAL.json <(python -B lane/verify_controls.py)` | 0 | empty |

`cmp` compared raw program-output bytes against the complete archived bytes;
there was no JSON normalization, whitespace stripping or partial match.
The three actual direct runs also reported exit zero, so no producer failure
was inferred away by a process-substitution consumer status.

Numerical role: pilot graph censuses and author-level theorem-fragment
controls only. No external/independent review, all-size proof-by-enumeration,
paper build or final acceptance is claimed. The deductions and deliberate
nonclaims are in PROOF_NOTES.md. INPUTS.sha256 pins scientific scripts;
SHA256SUMS covers all nonself evidence files in this package (excluding the
non-input cache). Both pin lists are checked after construction.
