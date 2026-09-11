# P208/P209 current-key reuse preparation

This is a sealed preparation, not an executed reuse inspection, a new scientific
run, a build, a page view, a fresh proof review, or batch acceptance. The sole
program is `inspect.py`; it reads files and writes its result only to stdout.
It never imports or invokes an original recorder, launcher, producer, auditor,
compiler, comparator, or renderer. No old artifact is modified.

## Exact scope

`INPUT_PINS.json` names 128 fixed physical input pins, six original strict
pairs, two original terminal build pairs, the four P209 native outer launch
packages, and six current accepted review/freeze packages. Original full input
ledgers remain at their original sealed paths; no host resources or large
duplicate ledgers are copied here.

| Reused original | P208 | P209 |
| --- | --- | --- |
| Author pair | 2 runs, 62,101 assertions each | 2 runs, 98,278 checks each |
| A pair | 2 runs, 130,961 assertions each | 2 runs, 135,605 checks each |
| B pair | 2 runs, 3,144,418 checks each | 2 runs, 54,794 checks each |
| Terminal pair | 2 builds, 7 pages each | 2 builds, 4 pages each |
| Previously actually viewed frames | all 7 first-build pages | all 4 first-build pages |

The checker validates complete exact nonself package seals and physical
memberships; all archived native command records, attempts where originally
recorded, full stream bytes, exact canonical and pair comparator targets,
source-only scientific capsules, original scientific counts and unchanged
current producer/canonical bytes. It reads all original full before/after
scientific, runtime, resolved-library, TeX, consumed-input, parent-input, and
configuration ledgers in scope. The 276 strict-pair native commands and 64
terminal native commands are original evidence, not new executions.

Current runtime, TeX, and configuration discovery explicitly follows the pinned
original recorder versions. File presence, recorded path resolution/symlink
fields, exact memberships, source settings, isolated interpreter settings,
absent caches and TeX user roots, archived link output, and recorded early/late
parent/child/native map samples are checked. Full raw canonical/PDF equality is
rechecked by read-only block comparison, without invoking `cmp`.

P208 and P209 terminal recorders differ: P208 has actual per-pass `.fls`, `.aux`
and `.log` artifacts but no P209-style per-pass generated-input JSON. The
checker uses P208's actual external `.fls` union and retained source/generated
artifacts; it does not invent a missing observation. P209's generated-input
JSON ledgers are checked separately. P208's one retained underfull diagnostic
is exactly `Underfull \hbox (badness 5681) in paragraph at lines 9--13`.

The original root actual all-page-view records, every individual frame, current
PDFs, frozen PDFs, and both terminal PDFs must agree with their exact pins.
Hash equality does not become a claim of a new visual inspection: the output
explicitly reuses the unchanged previous actual views and counts zero views.

## Six documentary exceptions, declared before execution

`ALIASES.json` is the complete registry. Each row binds one exact original
absolute path, historical SHA-256, physical preserved file, original provenance
record and one allowed case. There is no basename search, registry expansion,
scientific/runtime fallback, or automatic adoption of changed bytes.

1. P208 A old `FINDINGS.json` and old review `SHA256SUMS` use that review's
   `delta/initial_snapshot/` files, only in `p208_a`.
2. P208 A's old batch `FINAL_THEOREM_CONTRACTS.md` uses the exact preserved
   `qa/p208_round0_input_inspection_v2/historical_workspace_origins/` role,
   only in `p208_a`.
3. P208 B old `FINDINGS.json` and old review `SHA256SUMS` use that review's
   `delta/initial_snapshot/` files, only in `p208_b`.
4. P209 B old review `SHA256SUMS` uses its `INITIAL_REVIEW_SEAL.sha256`, only
   in `p209_b`.

The checker verifies the original provenance selectors and requires all six
declared roles to be used. Broader historical registries are not adopted.
The four current accepted review seals and current findings/delta records are
separately pinned as current inputs, never replaced by their old aliases.
Later P210 control changes cannot silently enlarge this registry. Any unknown
or changed required scientific/runtime key is a visible failure requiring the
affected fresh checks. A new documentary decision also requires a separately
reviewed preparation; do not alter this sealed preparation after execution.

## Future root-controlled execution

The root must first read all of `inspect.py`, `ALIASES.json`, and the contract,
verify this preparation's exact seal and package membership, then choose a
fresh `qa/p208_p209_reuse_NN/` outer-record directory (at least two digits).
This preparation does not create that directory and has not been run.

The native child command must have this exact shape, substituting only the
fresh absolute cache role and independently verified preparation seal digest:

```text
/usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p208_p209_reuse_NN/unused_checker_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p208_p209_reuse_preparation/inspect.py --expected-preparation-sha256 PREPARATION_SHA256SUMS_DIGEST
```

Its cwd must be `/root/autodl-tmp/symbolic_dynamics`; the complete environment
must be exactly `PATH=/usr/bin:/bin`, `LANG=C.UTF-8`, `LC_ALL=C.UTF-8`, `TZ=UTC`.
The chosen cache path must be absent. The root's separate native launcher must
preserve the actual pre-spawn intent, argv/cwd/environment, actual exit and
process outcome, full stdout and stderr, exact checker/preparation pins, and
appropriate actual checker/launcher runtime observations. A stdout PASS alone
does not establish the native parent exit or root acceptance. Do not substitute
an old initial-only auditor or import this checker as a module.

At completion every memoized current input is fully reread and its bytes,
resolution, symlink spelling and length must be unchanged; configuration
presence and memberships are repeated too. The result emits a compact current
read-key digest, counts, exact original ledger references and actually used
documentary aliases. It does not dump or duplicate the large full current
ledger. All final bytes remain reconstructible from the sealed checker,
contract, original ledger references and six declared physical roles.

Success is `PASS_CURRENT_KEYS_REUSED_NOT_NEW_EXECUTIONS_OR_BATCH_ACCEPTANCE`.
Failure is a nonzero native exit plus
`FAIL_REUSE_KEY_AFFECTED_FRESH_CHECK_REQUIRED`, case and traceback. Preserve
every failed attempt; do not overwrite it or silently retry under broader keys.

## Evidence boundary

Known original keys and their recorded settings/sample coverage are reused.
This does not reconstruct the historical OS/kernel, prove continuous tracing,
or observe historical transient loading that the original recorder did not
record. Older maps contain resolved keys rather than every original symlink
spelling; the checker checks their current resolved-key identity and current
before/final symlink state, without claiming unavailable historical fields.
No theorem novelty or correctness claim is upgraded here. `HOLD_EXTERNAL`
remains in force. `STATIC_CHECK.json` records preparation-only checks and the
read-only schema-navigation corrections; it is not a runtime reuse result.
