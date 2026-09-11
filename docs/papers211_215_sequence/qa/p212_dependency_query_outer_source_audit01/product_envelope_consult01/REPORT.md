# Independent product-envelope consultation

Consultant: /root/round211_fresh_residual_scout, 2026-09-09 UTC.
Requested by root and the main independent outer-source reviewer.
Verdict: NO_BLOCKING_CODE_FINDING_IN_THIS_NARROW_SCOPE; PCE-D1 MINOR / OPEN.
Operational, runtime, broader outer-source and manuscript acceptance remain HOLD.

## Exact subject and independence

The only executable source reviewed here is the frozen 78-line, 4923-byte product_capture.js in ../../p212_dependency_query_outer_preparation01, SHA256 d9af383627eda98ea20cbd48c78cc67d99a7eca5d0ece1e40a65c0d3ff10d4bf. Native full reads be2812 and 425775 and hash observations a14fee/efe9fd establish the source inspected. This is textual branch reasoning, not code execution, import, AST/syntax parsing, a witness test or a tool-call simulation.

I did not author that collector or its outer source. I did author the separate execution-scope source amendment; that amendment, its derivative driver and all P212 mathematics are expressly outside this independent consultation. Main reviewer /root/round211_functional_surgery_residual owns the broader supervisor/preload/lifecycle/read-purpose review. No inherited author or reviewer PASS is used here.

The complete named collateral was read: SOURCE_CONTRACT.md (205 lines), READ_ENTRY_COVERAGE.md (57), READ_SCOPE.md (93), SOURCE_ORIGIN.json (94), HANDOFF.md (61), REVIEW_INPUTS.sha256 (14). The package seal was content-pinned, not treated as correctness or as a semantic review of every other source file. INPUT_PINS.sha256 lists these eight entire physical file contents, including collector and seal. Full-file hashes do not expand the stated review scope.

## Proven narrow branch behavior

| Source anchors in product_capture.js | Deduction and limit |
|---|---|
| 17–25 | Trusted root invocation must have exactly the three declared authorization keys and a nonplaceholder external binding descriptor. These are preflight checks, not proof that the runtime/startup receipts already exist. The collector does not read or validate the whole selected binding itself; that belongs to the separately reviewed supervisor/root gate. A preflight throw occurs before any native attempt. |
| 26–31 | The already supplied outer-binding descriptor is serialized as the final literal Python argument. No actual result or enclosing transport envelope is an input to that descriptor serialization. The fixed command prefix, environment, interpreter, source and binding path are explicit. |
| 29–31 | Every argv word is individually single-quoted; an embedded apostrophe is represented by closing the quote, emitting an escaped apostrophe, and reopening it. Thus dollar signs, backticks, whitespace and the canonical descriptor's trailing newline remain data in one argument. This is a shell-grammar argument for received JSON/string inputs, not an executed quoting test. It does not attest the shell's pre-env-i bootstrap; SOURCE_CONTRACT.md 145–153 leaves that external gate explicit. |
| 32–39 | Per invocation there is one exec_command call site. Its exact constructed request is recorded before the await, and its actual JSON-native returned value is copied into the next frame before semantic validation. A tool rejection creates no fabricated return frame. Sequence numbers follow append order; wall-clock timestamps are supplemental, not a causal-order proof. |
| 40–54 | Each return is classified as ongoing or final. A reported positive safe-integer session id is retained before output/truncation refusal. Repeated ongoing returns must keep the same owned id. An exit without session marks native closure, even when a later check rejects that final output. Exactly-one session/exit is required before acceptance. Both/neither, missing output and detected truncation fail closed. |
| 55–64 | Only an actual integer exit zero takes the normal terminal branch. Otherwise polling uses only the actual retained session id, empty chars and the same short bounds. Every exact poll is recorded before its call and every actual return before revalidation. There is no second exec attempt, alternative session poll, stdin intervention, termination or successor call. |
| 65–68 | A thrown tool call or validation failure produces UNKNOWN_OR_FAILED_PRODUCT_CAPTURE via a normalized name/message catch record. Prior frames and the retained active session survive. It is not a native exit and is not full exception-object preservation: see PCE-D1. |
| 69–78 | Normal return means only NATIVE_PRODUCT_CLOSED_ROOT_RECEPTION_PENDING. The collector claims neither surrounding functions.exec/functions.wait envelopes nor an outer seal, lookup/body permission or automatic intervention. It performs no file write. Root must attach actual enclosing request, yield/cell, wait and final originals, together with the returned native frames, after the events. |

The argument assumes the declared JSON-native tool result surface: copied own JSON fields with string output, numerical metadata and optional session/exit fields. JSON stringify/parse is not an identity-preserving clone of arbitrary host objects, prototypes, BigInts or error objects; no such stronger property is claimed.

## Finite dependency and envelope order

The collector is a consumer of a previously received descriptor, not its producer. SOURCE_CONTRACT.md 47–67 places the prepared Node-only request before the inner binding, the inner binding before the outer binding, and the completed outer descriptor before this actual product request. That prepared request contains only the future binding pathname, not its contents or hash. The actual native and enclosing results are attached afterward, not fed back into the already selected binding. Lines 26–31 and 69–78 are consistent with that nonrecursive order.

This consultation verifies only the collector side and the collateral's stated order. It does not certify the outer supervisor's enforcement, fresh source/runtime/bootstrap receipts, actual future binding contents, or absence/membership of proposed destinations. Root must await the single collector invocation and retain the surrounding transport originals; merely loading the function, dropping its promise or copying a prepared request is not a received native operation. The source's one-use condition is a root invocation policy, not a mutable consumed-token implementation.

## PCE-D1 — documentary exception-retention overclaim

Severity: Minor. Status: OPEN.

READ_ENTRY_COVERAGE.md line 22 describes retention of an original thrown exception. In contrast, product_capture.js lines 65–67 build a new two-property diagnostic by converting the caught value's name and message to strings. The stack, cause, other own properties and original object identity are not retained by that code. SOURCE_CONTRACT.md line 169 correctly promises a JS catch record rather than a native exit.

Required closure: separately correct the coverage claim to actual normalized name/message retention, or, if the stronger full-exception contract is required, prepare and independently review the corresponding source delta. This consultation does not choose or implement either change. The frozen author package remains untouched, and full exception preservation is NOT accepted. The main reviewer acknowledged this finding as Minor/OPEN before this consultation was sealed.

## Other explicit limits, not additional findings

The 660000 ms check at line 59 runs only at ongoing-return poll boundaries and uses Date.now. It is not an interrupting hard timer, a monotonic-clock guarantee, or an upper bound on an in-flight tool call. A final return is processed before that budget check. Nothing here automatically signals a live process on timeout.

If a later return unexpectedly reports a different positive session id, its complete returned frame is retained at line 63, but line 45 rejects it before replacing activeSession. Thus unsettled_native_session_id is the previously adopted handle, not an exhaustive list of every unexpected handle reported in frames. Root must inspect the complete failure frames. This is not a lost original-return claim or permission to poll the unexpected id.

Even actual native closure would not establish descendant, stream-writer, dependency-after-key or enclosing-envelope closure. Those are separate root/main-reviewer obligations. No collected status grants a successor phase.

## Actions and handoff

All local commands were read-only text, line, size, path and SHA-256 observations. NATIVE_READS.json retains their exact requests/results, including complete collector and collateral reads. No collector, Python supervisor, Node preload, runtime probe, inner driver, mathematical verifier, host query/body/build or Git action was executed. Only this newly assigned consultation subdirectory was written with apply_patch.

This is a completed independent bounded source consultation with one unresolved documentary Minor, not whole-source acceptance or an operational receipt. The main reviewer owns incorporation and closure. Its other findings or eventual verdict are neither assumed nor overwritten here.
