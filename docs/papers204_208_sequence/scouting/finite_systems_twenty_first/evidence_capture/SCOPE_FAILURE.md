# Preserved history-scope failure

The first capture's comparison and source-stability results were actual, but
its stated P208/tenth exclusion was wrong: it omitted the actual
`/papers/208-` and `/order_geometry_tenth` path forms. The selected-file list
therefore included and the search command scanned excluded scientific files.
It also included review-input snapshots and build duplicates. This is a
scope failure despite the original JSON's numerical command status PASS.
The old output and receipt are preserved unchanged, not relabelled as a valid
scoped history scan. No P208 code was imported or changed and no P208 proof
contribution or independent reviewer status is claimed by this author.

`SCRIPT_RETROSPECTIVE_SNAPSHOT.py` is an exact copy of the used recorder made
after this discovery, before repair, not a falsely pre-execution source pin.
The corrected script explicitly excludes actual paper-number paths,
order_geometry_tenth, FTH_GATE, review/input/source-only/QA/build snapshots.
It writes fresh evidence in `../evidence_capture_02/`; no old failure is erased.
Root was informed immediately. This does not alter the already pinned NED
science source or its actual passing execution pair.
