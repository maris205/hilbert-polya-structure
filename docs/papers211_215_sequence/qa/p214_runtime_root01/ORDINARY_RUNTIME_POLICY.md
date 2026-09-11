# P214 finite ordinary-runtime policy

2026-09-11 UTC. Root explicitly adopts ordinary trusted CPython3.10,
bootstrap/sys/builtins/stdio, Node capture/hash/filesystem semantics and
ordinary path resolution for the accepted standalone P214 source.
This is not zero imports: sys is retained for argv/stdout/exit; the builtin
codec removes the json module dependency only. No local/data/canonical
input is read by the producer. The full source and its five-file amendment
were accepted in ../p214_source_root01/SOURCE_RECEPTION.md.

The selected baseline is the exact 19 roles in
../p212_a_source_root01/RUNTIME_INPUTS.json, fully read as archival DATA by
root (7f3b6a/9b313a). It has 18 files and required absent /usr/lib/python310.zip.
Root authorizes a fresh read of those exact roles now: complete bytes/hash,
size and six ordinary metadata fields, true lstat ENOENT for the absent zip.
Preserve failures; content/member changes cannot be silently substituted.
Historical metadata differences are recorded and may be refreshed in the
new runtime baseline; the actual fresh run PRE/POST must fully agree.

This finite selected set is not an exhaustive dynamic dependency, syscall,
loader or package census. No recursive host scan, old B/S or ELF closure
inquiry is implied. Selected standard tools and path traversal are trusted,
not newly authenticated. Disk capacity is an observation, not a reservation.

Execution, after separate one-run grant and new-path preflight, is exactly
/usr/bin/python3.10 -I -S -B followed by the live absolute verify.py, cwd
workspace, no script args, stdin /dev/null, env LANG=C and LC_ALL=C only.
Full raw stdout/stderr use exclusive files; actual exit precedes postflight.
600000ms timeout uses SIGKILL and is a failure. No output-size cap is used.
All source/proof/parameter/schema/preparation/grant keys are pinned, with
documentary inputs distinguished from imported modules. Canonical adoption
requires complete independent semantic reception; strict pairs require new
grants and complete raw comparisons. This policy is not a science grant.

No build, freeze, paper PASS or external action. HOLD_EXTERNAL.
