# Final additional conservative exclusion

After reading the complete V2 selected path list in four untruncated chunks,
the scout excluded the whole `order_geometry_tenth` and
`order_geometry_tenth_desk` lanes as potentially interleaving OFS material.
V2 had only run structural/path/byte-hash verification, not a body search.
No proof body of either lane was displayed. V2 scripts/paths/pins remain.

`record_final.py` is the only body-search entry point. It selects a strict
subset of that fully inspected path list, performs actual complete path checks
again as command 03, and records full expanded argv and full original input
pins for every subsequent search. No claim of reviewing or accepting any
excluded manuscript follows from filename or hash access.
