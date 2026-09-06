# P208 A documentary correction — P208-A-ART1

2026-09-06 UTC. This supplement corrects one count-description error in the
unchanged initial REPLAY_LOG.md. It does not alter any old log, receipt,
producer, recorder, canonical, proof, manuscript, bibliography, PDF or
runtime dependency.

## Correct distinction

In each of cold07 and cold08, the four archived ldd outputs contain
**35 distinct raw path spellings**, resolving to **32 distinct canonical
files**. LIBRARIES_BEFORE.json and LIBRARIES_AFTER.json correctly contain
exactly those 32 files. The recorder's original libraries_count=35 field
counts distinct unnormalized strings. The initial REPLAY_LOG's statement
that 35 resolved libraries were pinned conflated the two counts.

The three two-to-one alias groups are identical in both runs:

| Raw path spellings | Canonical resolved file |
|---|---|
| /root/miniconda3/lib/python3.12/lib-dynload/../.././libncursesw.so.6 and /root/miniconda3/lib/python3.12/lib-dynload/../../libncursesw.so.6 | /root/miniconda3/lib/libncursesw.so.6.6 |
| /root/miniconda3/lib/python3.12/lib-dynload/../.././libtinfow.so.6 and /root/miniconda3/lib/python3.12/lib-dynload/../../libtinfow.so.6 | /root/miniconda3/lib/libtinfow.so.6.6 |
| /root/miniconda3/lib/libz.so.1 and /root/miniconda3/lib/python3.12/lib-dynload/../../libz.so.1 | /root/miniconda3/lib/libz.so.1.3.2 |

All remaining raw spellings resolve singly. Thus 35 minus three duplicate
spellings is 32; the set of resolutions equals the complete recorded pin
map, with neither missing resolved files nor extra pinned files.

## Actual affected audit

A's new documentary-only delta_audit.py reconstructed the spelling set
directly from the original python_ldd, extensions_ldd, cmp_ldd and bash_ldd
stdout files in both runs, resolved each path, checked the complete
before/after maps, and rechecked all current file digests. It also checked
the actual root strict replay receipt, all seven saved command records
and streams, its 1,878 inputs, runtime/configuration mappings and canonical
bytes. No scientific implementation or TeX was executed by this audit.

The actual first check is delta/audit01/COMMAND.json and its full
audit.stdout/audit.stderr: exit zero, PASS_LIBRARY_COUNT_AUDIT,
9,083 checks, 4,219 baseline referents, all 743 initial payloads intact.
Its complete all_resolutions maps document all 35 spellings in each run,
not merely these three examples. The later delta/audit02 record checks
the accepted documentary state and exact historical/current relocations.

P208-A-ART1 is therefore a **Minor documentary finding**, not an omitted
dependency, mathematical failure or reason to create another numerical
or PDF run. The four older resolved reviewer-evidence findings and all
failed/superseded evidence remain unchanged.

## Preservation and scope

Before changing the current FINDINGS ledger, A copied its exact initial
bytes to delta/initial_snapshot/FINDINGS.json, SHA-256
b7c27f963cd93020a530c121bb38f6ee6cb7bb85194a1730974854bb04cf6078.
The initial complete 743-entry manifest is preserved verbatim at
delta/initial_snapshot/SHA256SUMS, SHA-256
6d129aad1aec05cc08025030af1e1328cd59e66fccfd6311fc0176c901165ac8.
That archived index retains its original review-root-relative path
convention; it is not a new directory-relative manifest of the two-file
snapshot folder.

The other 742 initial payload files remain byte-identical at their
original paths. The current ledger and new complete top-level seal are
documentary successors, not falsely unchanged initial inputs. The exact
mapping in delta/INITIAL_PAYLOAD_MAPPING.json and
delta/DOCUMENTARY_RELOCATION.json allows every old payload and both
changed root-pair documentary references to be recovered. The initial
REPLAY_LOG, which contains the original wording, is deliberately retained.

This supplement supports the actual decision in DELTA.md. It does not
authorize external release or assert global novelty.
