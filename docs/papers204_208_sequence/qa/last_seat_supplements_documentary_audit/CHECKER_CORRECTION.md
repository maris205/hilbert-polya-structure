# Actual first-checker failure and bounded correction

The first invocation, preserved under run_01, exited 1 at the new checker's
reconstruction of triage command02's rg output. It had already checked all
seven exact package seals/censuses and the declared original-copy roles.
It had not finished the full audit; run_01 is not a passing audit.

The original command's full stdout is 21,971 bytes. The reconstruction also
had 21,971 bytes with exactly the same multiset of complete lines. The
mistake was assuming rg's output file order equals its argv order. The
native output is grouped GIT_SYNC_RECEIPT, PIPELINE_STATE, STATE; the argv
lists STATE, PIPELINE_STATE, GIT_SYNC_RECEIPT. No content discrepancy or
corrupt historical package was found.

Root was notified before adaptation. The exact first checker is retained
as failed_run_01_checker.py.txt, SHA256
47b13b54107b722667be66ad2f9c387176621f547492273ca2fa1e5f29543c47.
Only the new reconstruction changed: it retains the native observed file
group order and verifies every per-file expected line and the complete
reconstructed output byte-for-byte. It rejects missing, duplicate or
reordered lines within a file; it does not rerun rg or replace raw outputs.

The correction is documentary only. Old packages, scientific/source code,
original command pins and original failures remain unchanged. The final
checker also reads this note, the exact failed checker and all three failed
run artifacts twice so they are included in the successful consumed ledger.

The second invocation, run_02, passed the native triage, ORR, NED, erratum,
LNR intake-cmp and LNR audit checks, then stopped before the first LNR HTTP
input validation. The original curl records explicitly pin /usr/bin/curl
in all four before/after maps. The new checker had omitted that exact
executable from its allowed external input list. This was a conservative
scope refusal, not a pin mismatch. Its exact checker version and complete
1,667-byte stderr are retained with its actual exit 1 and empty stdout.

Root was notified before the second scoped adaptation. The executable is
now read and hashed only at the exact recorded path, requiring the original
SHA256 1530e0bbf20632b4587eea4d045e9e5e87614d1ffbbcc4bf157862b3c7fea439
and each native map's original 260,328-byte metadata. No executable is run,
no arbitrary external path is allowed, and no original map is refreshed.
The final checker consumes both failed versions and both failure records.

The third invocation, run_03, finished the native records and HTTP/source
record checks, then failed a new overly strict prose-basename assertion.
TRIAGE deliberately uses brace notation such as `{INTAKE,PROOF_PACKAGE}.md`.
The original sealed erratum parser expands that syntax. The new checker
had incorrectly demanded each expanded basename literally occur in prose.
This extra convention was not an original evidence requirement. Root was
notified and directed its removal. The exact run_03 checker, empty stdout,
703-byte stderr and actual exit 1 are retained.

The final adaptation reproduces only the original erratum's brace-name
expansion and checks the expanded mapping against each exact original
receipt's argv. It preserves the original ORR exception for three explicitly
described excerpt files. No parser/script is imported or executed, no prose
is edited, and no mathematical conclusion is drawn. All three exact failed
checker versions and all nine failed run artifacts are consumed twice by
the final checker.
