# Preserved initial capture failure

The actual command `python3 -I docs/papers211_215_sequence/scouting/rational_coupling_lane/capture_native.py`
returned exit code 1. It successfully wrote the initial twelve-input
hash output and two physical control copies with two successful raw
comparisons, then failed while launching the proposed narrow history search.

The terminal reported `FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/rg'`.
The traceback pointed to `main` line 69, `run` line 49, and the
`subprocess.run`/`Popen` launch path. This paragraph is an author transcription
of the actual tool response, not a separately captured native stderr file.
The failed process did not reach its final receipt writer; no missing
receipt, after-hash check, fetch, or source extraction is asserted to exist.

The initial `capture_native.py`, all ten initial native stdout/stderr
payloads, and both control snapshots remain unchanged. No scientific run
occurred. `capture_native02.py` is a separate repair with the actual resolved
rg and curl paths, a new `native02/` output directory, and reuse-by-comparison
of the already captured control bytes, not replacement of those snapshots.
The empty initial `sources/` directory contained no fetched payload.

Independent source-access failures also occurred in browsing: opening
`https://par.nsf.gov/servlets/purl/10415826` returned `(400) Timeout fetching`;
the EMIS `find` operation for `Example 4.2` returned no matching text.
The preceding EMIS PDF open itself succeeded. These browser events are
recorded honestly as browser-response observations, not curl native records.
Later successful native fetch/extraction does not erase them.
