# Actual documentary evidence and retained checker failure

2026-09-10 UTC. Author evidence only, not independent source/runtime acceptance.

The first author document check (8f8af1) exited 1 at the arbitrary assertion
that every explanation exceed 30 characters. For example, "re imports enum."
is a complete explicit reason despite its length. No module/path permission,
source policy, archive row or runtime predicate failed or changed. The
checker now requires a nonempty trimmed reason. This corrects an author's
unjustified prose-length test; it does not relax an accepted artifact parser.
CHECK_DOCUMENTS_DRAFT.cjs preserves the complete original checker;
CHECK_DRAFT_FAILURE_NATIVE.json preserves its full native read and actual
failed invocation. CHECK_SOURCE_NATIVE.json preserves actual construction,
the repair patch/return and full final checker read. The native -u diff
shows the exact one-line documentary assertion change.

The corrected actual check (27a435) exited 0: 2,484 assertions / 18 full
document keys. Six original complete readbacks total 56,660 bytes; five
authored readbacks total 93,234 bytes. All were compared as raw UTF-8 bytes,
not normalized text. Six old keys include stable before/read/after fd and
path ten-field metadata; the strict six-input hash check (7923c6) also exited 0.
The actual wc return (950a1a) is 137 lines / 12,401 bytes for the checker.
An unmeasured 154-line value in this report's first draft was incorrect;
the draft native read is preserved with this correction. No Python AST or
reviewed-source execution was performed.

The actual checks cover 57 historical module dispositions (32/25), 11 old
map dispositions (9/2), 62 finite permitted module names (23 early), 29
unique source/cache pairs, 69 unique candidate paths and all 17 flag names.
All proposed current facts remain null; enabled, operation_authorized and
source_delta_implemented remain false. Proposed paths are data only.

Closing verifies the whole finite payload inventory, exact raw checker
readbacks, preservation of the failed draft, the passing check's unchanged
18 full keys, six old pins, JSON validity, no physical alias and every
payload's own complete key. The final SHA256SUMS is nonself. Its strict
check and full physical manifest coverage run after seal creation and are
reported separately to root; no circular self-hash receipt is included.

No reviewed Python/Bash execution, Python/import/AST/syntax test, runtime
file/path/config/env/proc/ABI observation, output directory creation, scientific
run/build, private/Git/SSH action, old source/audit edit or central edit occurred.
