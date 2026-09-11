# Unsealed launcher privacy correction and genuine failure

Before initial sealing, the original record.py was found to serialize inherited
launcher environment fields including the platform credential key
`AutodlAutoPanelToken`. No credential value was printed or externally sent.
Root explicitly required sanitization, with no secret-bearing backup or Git
copy. Complete clean CHILD environments in production/pair/build capsules are
unaffected. The original launcher was not prehashed by the old parent receipts;
its authenticated original source/pin is therefore unavailable. The retained
`history/record_source_reconstruction_unverified.py` is explicitly an unverified
reconstruction from its creation patch, not authenticated original evidence,
not safe to execute and not a secret-bearing old receipt. Its new hash cannot
retroactively supply the missing original source pin.

The first bulk sanitizer invocation was defective: Perl `-i` without a correct
per-file input loop printed only a sanitized first record and emptied the four
parent ATTEMPT files. Its native exit was0, but the subsequent actual reader
failed255 with `malformed JSON string ... at character offset 0`. This is a
genuine documentary failure, not a successful preservation claim. Its four
empty outputs were immediately identified with actual zero-byte counts.

Affected files: execution/pair01/ATTEMPT.json,
execution/build01/ATTEMPT.json, execution/compare_author01/ATTEMPT.json and
execution/build_pdf_cmp/ATTEMPT.json. The actual tool invocation gives their
argv and cwd. Only the first original start_ns was in the sanitized tool output;
the other three original start times are unavailable. A one-time scoped script
reconstructs ONLY these known metadata, explicitly labelled not original
receipts; it does not invent missing environment/times or restore secret values.
Its actual result pins the sanitized reconstructions. Parent RESULT records,
stdout/stderr and all child CONTEXT/ATTEMPT/RESULT/source/raw/runtime/build files
remain byte-unchanged. There is no claim of secret-bearing original receipt
byte preservation.

The corrected record.py saves a whitelist of relevant nonsecret launcher
settings and only names of omitted keys. Fresh pair02/build02 plus fresh
documentary comparison receipts are produced under the corrected source, so
the selected acceptance evidence does not depend on reconstructed parent
launch metadata. No carrier/cutoff/checker/manuscript/source input is changed.
