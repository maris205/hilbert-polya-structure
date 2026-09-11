# P215 run02 initial artifact audit corrected V2 source handoff

Status: SOURCE_READY / NOT_EXECUTED / ROOT_GRANT_REQUIRED.

ARTIFACT_DATA_CHECK.v2.cjs is the corrected independent read-only receiver for
current02, binding02 and run02. It is 124 lines and uses only Node built-ins
fs, path and crypto. It starts no child, writes nothing, follows no FLS path
and reads the complete fixed run02 tree plus explicit current/binding/live
source inputs. SHA256:
fcfa32d2ca27c847b2c37c91ca410746cce027d44818b86a5402138790c581da.

V2 supersedes only the unexecuted run01-targeted V2 source. The actual V1
failure remains preserved: c0bcbb/pid160973 exited1 before artifact traversal
because V1 requested binding01/SOURCE_RECEPTION.md instead of current01;
stdout.raw is zero bytes and stderr.raw is 1243 bytes. V1 is not a DATA report.
Separately, run01 is formally held by binding01/RUN01_HOLD.md for four FLS-
consumed AMS extra TFM files absent from its 223-row prebinding. None of those
facts is erased or reclassified by V2.

For run02, V2 requires exactly 227 resource rows and the manifest SHA
bcad5ca8f77003ff4fbbf0b52c6017c8bea463d70ce3583a04574b890e555b12.
It checks all ordered FLS inputs against that key, all eight source roles,
the exact 160-file inventory, eight product snapshots/chronology, controller
and all 14 step exits/RAW streams, bibliography/AUX/BBL/BLG, diagnostics,
16 embedded Type1 fonts, PDF/text, six PNG pins and closing whole-byte
stability. It additionally requires binding02/ACTUAL_NATIVE.json and
CONTINUATION_NATIVE.json, then checks exact accepted request, actual session,
exit0 and the complete P215 supervisor line. Those receipts were not present
at this source cutoff and must be written and root-read before authorization.

INPUT_PINS_V2.sha256 pins ten current inputs and strictly passes. The two
future outer native receipts are intentionally not assigned invented hashes.
Root must read the complete checker, confirm its hash and receive those actual
receipts before issuing one separate DATA grant. Do not execute V2 from this
handoff. Preserve any future HOLD/error without retry.

The auditor previously contributed only the section4 status-text proposal and
actually viewed run01's six pages. It contributed no P215 mathematics,
verifier, scientific run or build. No run02 view or manuscript Review A is
claimed here. No PDF adoption, live edit, Round0, central index, Git or
external action is authorized. OWNER_AMBER / HOLD_EXTERNAL.
