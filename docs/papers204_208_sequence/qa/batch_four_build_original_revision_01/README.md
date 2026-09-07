# Four-build original inspector revision 01 — exact selection repair

Status: **ADAPTER_SELECTION_ERROR_DIAGNOSED / CORRECTED_INSPECTOR_PREPARED_NOT_EXECUTED / ROOT_RECEPTION_PENDING**.

Root's real first execution stopped at the first `known_membership(before)` assertion with native exit 1. Its complete launch/completion records remain unchanged at `qa/BATCH_FOUR_BUILDS_ROOT_ORIGINAL_{LAUNCH,COMPLETION}.actual.json`, session 34245. The original failed inspector remains unchanged in `batch_four_build_original_preparation/`, with source hash `83b1666ae75e7051ee1c57e234b69832f0f47df5772a5916d2ca2f0897e42e0f` and original preparation seal `c1c06e90b59dd25fadbb665690b66abfdb265cbb4faa5f7745e6611756134897`. No old source, receipt, seal, builder, execution package, paper, review, central/index or Git file was edited.

## Exact cause and actual bounded diagnosis

The original builder explicitly adds fixed configuration candidates after recursive enumeration, including absent children underneath a configured root. My first adapter instead retained fixed candidates only when their paths were outside all recursive roots. Thus an explicitly selected absent descendant was lost: `rglob` cannot enumerate an absent file, while the adapter also excluded that path from its fixed set.

[DIAGNOSIS.actual.json](DIAGNOSIS.actual.json) and its [actual native diagnostic record](DIAGNOSTIC_NATIVE.actual.json) show the exact differences against **both** complete original gzip ledgers:

| Group | Original ledger | Failed selection | Restored original selection |
|---|---:|---:|---:|
| Configuration | 1,875 | 1,873 | 1,875 |
| Runtime | 3,095 | 3,095 | 3,095 |
| TeX | 118,878 | 118,878 | 118,878 |

The failed selection omitted exactly `/etc/fonts/local.conf` and `/root/.config/fontconfig/fonts.conf`, with no unexpected paths. Both paths are explicitly fixed in the original builder, absent in both original ledgers, and still absent now, with unchanged resolved spellings. Reconstructing the original fixed literals, Python configuration-derived candidates and `ldd` loader-list candidates gives **no missing or unexpected member in any group**. The before/after original ledgers are equal.

This establishes an adapter error at the failed membership assertion, not a current membership change. It does **not** establish that all file bytes remain unchanged or that the later native/FLS/runtime checks pass: root's failed inspector had not reached them. The full corrected inspector must perform those checks, without any dependency waiver.

The bounded diagnostic enumerated only the original defined selection scope and printed explicit set differences; it did not hash a new broad host-file inventory or import/execute a builder or either full inspector. Its first attempt failed while formatting source pins because it treated the absent sysconfig Makefile candidate as a file. [The complete failure](DIAGNOSTIC_FAILED_01.actual.json) and [original diagnostic source](diagnose_membership.py) are preserved. [Diagnostic version 2](diagnose_membership_v2.py) records absent candidates as absence metadata and exited 0. [The original absence records](DIAGNOSTIC_ABSENCE_RECORDS.actual.json) confirm that the Makefile and `pyconfig.h` candidates were already absent in both original ledgers; this was a diagnostic formatting error, not an excused dependency change.

## Minimal separate correction

[inspect_four_builds.py](inspect_four_builds.py) is a separate corrected copy. [SOURCE_DELTA.diff](SOURCE_DELTA.diff) contains the actual native source difference, with its [native diff record](SOURCE_DIFF_NATIVE.actual.json). The only behavior changes are inside `known_membership`, plus the required standard-library `sysconfig` import:

- Restore the original 18 fixed path literals, eight `_pth` candidates, exact sysconfig Makefile/header and `LDLIBRARY`/`INSTSONAME` rules, and parsed `ldd` `RTLDLIST` rule. Fixed candidates are selected even when absent beneath recursive roots. No historical “extra” is accepted merely because it appeared in a ledger.
- Keep exact equality of group membership and provide explicit sorted missing/unexpected paths in any future membership failure.

Everything else, including full original file/presence/link hashes, final uncached rereads, all 58 native records, auxiliary/FLS/generated-file roles, exact P207 Underfull string and bounded runtime limitations, is unchanged. [The static check](STATIC_CHECK.actual.json) verifies that all other top-level behavior is AST-identical, that the read-only surface remains, and that the loader-header check contains a real newline. It did not import or execute the corrected inspector. Native `diff` exit 1 records the expected source change, not an inspector execution failure.

[INPUT_PINS.json](INPUT_PINS.json) supplies 17 direct original source, seal, receipt, gzip/sidecar and interpreter/configuration bindings. The original execution seal remains `1ae09fd38c3b99d49563a5bfcf82f075cf30287980ced9b60a5b95b81ba38f26`; the original writer preparation seal remains `6f2d19d844644e5a161001913d9248d27f77e638e792d647fc4dbd1084005109`.

## Root execution still required

After reading the exact delta and original evidence, root may capture a new actual invocation and full native return in a fresh reception record:

```text
/usr/bin/python3.10 -I -S -B /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/batch_four_build_original_revision_01/inspect_four_builds.py
```

The corrected inspector has **not** been executed here. There is no root reception/acceptance claim. The ten root page views remain outside the inspector, and no new science/build/view/review was performed. This revision was prepared by `/root/p210_author`, a P210 author who remains ineligible for P210 manuscript A/B. OWNER_AMBER / HOLD_EXTERNAL remain. Only this new revision directory was written, and its own `SHA256SUMS` seals its nonself contents without replacing any historical seal.
