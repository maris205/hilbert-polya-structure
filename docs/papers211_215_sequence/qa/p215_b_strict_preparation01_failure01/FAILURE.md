# P215 B strict preparation01 PRE-EXEC failure

The separately granted strict01 controller stopped before invoking the
verifier because `qa/p215_b_strict_runs/` did not yet exist and the exclusive
nonrecursive creation of its `strict01` child returned `ENOENT`. The consumed
grant is preserved at its original path. No strict output tree, verifier
execution, stdout or scientific result exists; this is not strict credit.

Preparation02 changes only the parent-directory creation/check before the
fresh exclusive child slot, plus mechanical preparation/grant path updates.
