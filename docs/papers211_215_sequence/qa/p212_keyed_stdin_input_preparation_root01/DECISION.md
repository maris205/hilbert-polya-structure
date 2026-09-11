# Root decision: prepare exactly the new empty regular input

2026-09-10 UTC. The exact P212 source combination and independent non-lineage
audit have root reception at p212_keyed_stdin_source_root01/RECEPTION.md,
sealed by 0f65f815ca28d4153bc968b0d8dd041f3571287ebe639c942abce6064bb32380.
Root now authorizes only the following physical input-preparation operation.

Select exactly the previously contracted directory
/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_keyed_stdin_input01
and its one leaf empty.stdin. Check both exact names for absence; stop if
either exists or gives any non-ENOENT error. Create the directory exclusively
and nonrecursively, require mode 0700, then create the leaf through one
O_CREAT|O_EXCL|O_NOFOLLOW descriptor with mode 0600 and no data write. Keep any
partial directory/file on failure; no deletion, replacement or automatic retry.
Do not use /dev/null, inherited ambient stdin or a symlink as the new input.

PREPARE_INPUT.cjs is a small root-owned artifact-preparation utility, not
any reviewed observer/probe/driver. It may inspect only these two exact
names, its new descriptor and their ordinary ten-field/non-atime endpoint
metadata. It records the current whole empty content digest and creation
outcome; no native statx/birthtime/fourteen-field receipt is inferred from
this standard-library preparation. The old /dev failure stays unsatisfied.
This uses ordinary trusted Node/filesystem/parent resolution, not a hostile-
parent or continuously observed race-proof creation claim.

No observer/capture/private directory creation, host executable, proc,
environment/configuration/capacity query, live application, author probe,
science/build/Git/SSH or external action is authorized. The disabled next
observer request proposal remains separately owned, and this decision does
not enable it. Actual finite native observation still requires an exact
relocated request/trust binding, separate root grant and independent original
reception. HOLD_AUTHOR_PROBES / HOLD_OPERATIONAL / HOLD_EXTERNAL.
