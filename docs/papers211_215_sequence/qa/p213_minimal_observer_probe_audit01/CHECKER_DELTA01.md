# Preserved recipient checker failure and finite correction

First documentary execution `15e888` exited 1 at an overstrict recipient
assertion that every previously frozen manifest must have sorted names.
Its exact source is retained as `CHECK_DOCUMENTARY.cjs`; its entire actual
native failure remains `DOCUMENTARY_NATIVE.json`. No original packet or
stream was edited, and no observer was invoked.

The fixed producer manifest has OBSERVATION_NATIVE.json last; the enabled
source manifest lists observe.py then capture.sh. Their exact commissioned
seal hashes, unique safe basenames, nonself membership, whole payload hashes
and no-extra inventory are the requirements. Lexical row sorting was an
unwarranted extra assertion, not a producer evidence failure. Native deaecc
displays all six exact manifests and preserves their ordering. It also
shows RAW_INPUTS.sha256 correctly uses repository-relative paths, whereas
the first checker expected absolute strings. That later assertion was not
reached by the failed execution. The delta uses those exact relative rows.

`CHECK_DOCUMENTARY_DELTA01.cjs` is a separate full-source derivative with
only these two corrections and one additional check: compare every original
materialization raw-pair field to the independent whole physical-byte pair.
All finite capabilities, original complete keys, request/grant/native,
chronology, precision warning, scope and authority checks are unchanged.
Retain this failure and correction together; a later successful data-only
checker run cannot erase or relabel the failed native return.
