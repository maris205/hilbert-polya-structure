# Complete read-entry coverage for revision02

SOURCE_ONLY author control-flow proof; not an independent audit or executed
test. Line references address the exact978-line driver SHA256
57ce0d5815e3b0d051925dd351030d26067eb796a47f7058cf8f3a08c5e90032.

## All bound-file/reference call sites

All calls in the source to readPinned and receiveRef are listed below.
The complete actual source-text enumeration is retained in
DIFF_AND_READ_ENTRY_NATIVE.json; its rg result is navigation, not AST execution.

| Caller / new lines | Passed purpose | Dominating pre-byte conditions |
| --- | --- | --- |
| main SELF,902 | source | Exact lexical+regular referent source roles, nonnull matching whole pins, driver expected pin, full bound resolution and no body-role chain component |
| Six nonnull binding.receipts,903 → receiveRef452 | receipt | Workspace reference/pin schema, then same role/content/alias guard; includes plan_source/driver_source/prestartup/options/queries/body_scope acceptance documents |
| controller.outer_entry_source,904 →452 | source | Same source channel and complete expected pin; not a receipt-role or body-role exemption |
| controller.outer_request_record,904 →452 | receipt | Same documentary receipt channel; a future original request, not an implemented outer capture |
| oldCompanions,475 | source | Four fixed whole originals, nonnull prebound source pins; whole hardcoded SHA and canonical JSON checks remain |
| Eight fixed profile inputs,908 | source | Same source channel plus each fixed complete expected pin |
| validateQueryInputs stdout and stderr,729 | query_result | Explicit archived-result role on lexical and resolved regular descriptors, full pins and no body-role alias chain, before any read |
| validateQueryInputs result JSON,730 | query_result | Identical pre-read guard; canonical/result/label/argv/event/raw checks remain after safe documentary read |
| snapshot,432 | d.role (validated finite purpose at358–376) | Every pinned file still enters central guard; body requires installed full-set capability even when content was already pinned; non-body source/runtime/configuration/receipt/query_result requires its own complete pin |
| Final body reread,933 | body | Whole-set capability includes lexical+resolved path, complete first-observed expected pin; not a bootstrap receipt/query path |

There is no default read-purpose parameter. Missing, unknown, ancestor/cwd/
device purpose for a byte-read file rejects in fileForPurpose. The controller
and native executable descriptors additionally pass explicit runtime-purpose
validation at580–581 before main can receive any bootstrap references.
Directory/character metadata reads remain distinct from file-byte reads.

## Two source-input byte-open sites

1. readPinned opens at395 and reads at404. fileForPurpose at384 precedes
   requireBodyRead at385 for body; expected/nonnull whole pin checks precede
   resolveBound; the complete alias/ancestor body-channel exclusion precedes
   the open. Actual handle regularity/stat validation precedes fs.readSync.
   Consequently neither receipt, source, runtime/configuration snapshot nor
   query-result call can use an expected pin as body permission.
2. captureBody opens at809 and reads at820. fileForPurpose and requireBodyRead
   at797–798 plus saved exact ordered request equality at799 precede every
   side effect of that call. The existing actual regular-handle/stat checks
   precede its read loop. The only caller is main's ordered body_requests loop
   after validateQueryInputs returned and installed both capabilities.

All direct native source comparison is the unchanged cmp inside captureBody,
which is reached after the second entry's guard and completed first copy.
The cmp's internal file handles are explicitly not claimed observed. Its
surrounding snapshot also uses the first guarded entry for any pre-pinned
body file. No native body/source command exists before that call path.

## Capability proof and malformed-branch cases

Before main, approvedBodyPaths and approvedBodyRequests are null. There are
no assignments except initialization240 and the two final successful
validateQueryInputs assignments792–793. This function is synchronous:
all38 result contexts, every ordered raw-return request, every declared body
role and every returned alias chain must pass before that transition.

fileForPurpose(body) is safe for pre-transition validation because it performs
only descriptor assertions. resolveBound does finite lstat/readlink metadata
operations, never open/read of file bodies. requireBodyRead is not called to
grant permission during validation; it can only observe the completed state.

- Receipt/query ref uses body lexical descriptor: exact purpose mismatch
  rejects before resolver/open, irrespective of expected pin.
- Only lexical descriptor is retagged non-body: resolved purpose mismatch
  rejects before open; null/nonmatching referent/content pins also reject.
- Body-role intermediate alias or ancestor under otherwise non-body endpoint
  roles: resolution-chain role check rejects before open.
- Body file has already-known content or caller supplies a complete expected
  pin: requireBodyRead still requires the full-set state; content does not
  alter that state.
- The final returned request, a referent role or an extra body descriptor is
  invalid: validation throws before assigning the capability. Earlier safe
  documentary result reads remain permissible; no body read has occurred.
- A copy is called for a path outside the accepted set or for a changed/reordered
  request: capability/saved-index equality fails before its mkdir/open.
- A body alias chain changes afterward: the unchanged metadata resolution and
  actual read-handle checks still fail closed in their bounded observations;
  no continuous no-race/OS-hermetic claim is added.

## Remaining raw read/open sites are separate channels

| Site | Exact scope and unchanged boundary |
| --- | --- |
| Initial fs.readFileSync(filename),894 | The one selected fixed workspace disabled/enabled binding before descriptor initialization. Nonself outer byte/identity/before-after key remains mandatory and unimplemented, DQD-O1. No generic receipt/query path reaches it. |
| /dev/null open,614 | Explicit device metadata/actual character-handle stdin, not body-file data; remains inside post-gate native capture |
| openOutput,584 | Exclusive write-only owned output, not a source/body read |
| Native stdout/stderr fs.readFileSync,680–681 | Newly created closed owned raw outputs; no root-supplied input reference selects their paths |
| Copied body.raw fs.readFileSync,852 | Newly written owned copy, after guarded source read and native cmp |
| sealLocal fs.readFileSync,884 | Exact generated-file membership list under exclusive owned output; not an input/reference read |

These paths do not discharge broader product/session settlement or startup
runtime provenance. They are unchanged and remain subject to the original
separate outer reception/HOLD. No circular binding pin, new host selector or
additional execution mechanism is introduced by the repair.
