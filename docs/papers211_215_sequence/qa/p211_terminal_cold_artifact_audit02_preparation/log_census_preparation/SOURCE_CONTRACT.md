# Source-preparation integration contract

Status: SOURCE_PREPARATION_NO_RUN. Only the designated v02 function is proposed for integration.

- Source: diagnostic_census.source_only.v02.py, 12924 bytes, SHA-256 228614c455a09f80f6c25c97c1315a1cdb2a3be6e5ac97a17ca64a19e46d6665.
- Function: diagnostic_census(); no top-level call or standalone launch path.
- Helpers: read(path) returning bytes; raw_pin(bytes) returning bytes/SHA-256; obj(path); put(name, value); demand(test, group, detail).
- Globals: INNER and COLD are Path-like; DETAILS is a dict without a prior diagnostic_census entry; FINDINGS is a list without the prospective finding ID.
- Runtime dependency: the function imports re. Parent must bind actual source/runtime/settings and provide provenance-enforcing read/obj plus exclusive-output put; none are supplied or executed here.
- Exact future inputs: the 18 entries of RAW_LOG_ROLES.json, plus the actual cold2 INNER/MEASURED_NOT_VIEWED.json. This preparation did not open that measurement object and therefore does not assert an emitted-versus-recorded mismatch for cold2.
- Exact future output: FULL_LOG_DIAGNOSTIC_CENSUS.json, assembled entirely from future raw reads; DETAILS receives a compact association and FINDINGS receives a new pending-disposition warning-census discrepancy only if dynamically derived.
- The function preserves every matching line and ±2-line context; matching is case-insensitive and separate from semantic emission categories. Unknown literal matches remain explicit. Six actually observed BLG warning$ -- 0 rows are function-call counters, not warning emissions.
- Final warning comparison is an exact-text multiset, not set equality: duplicate occurrences are retained. Both emitted-not-recorded and recorded-not-emitted are returned. No cold1-specific warning text or count is assumed.
- The 18 log bodies and measurement are reread at the end and pinned against the initial same-invocation reads. No host path embedded in log text is followed.
- Parent must independently enforce the full artifact directory tree and all-file manifest, exact native launch/capture/session evidence, source/binding/options/runtime, ordered FLS and BibTeX dependencies, final diagnostics beyond warning-summary mismatch, actual page-view evidence, and root disposition. The function is not a substitute for those components.
- There is no executable authority, Python/import/compile/test result, future wrapper, runtime probe, science, TeX run, page view, terminal PASS or diagnostic disposition in this preparation.

Initial source and preparation census remain as pre-v02 drafts. v02 adds an explicit BibTeX counter classification and a no-overwrite DETAILS guard. No failed execution was concealed: neither draft was executed at all.
