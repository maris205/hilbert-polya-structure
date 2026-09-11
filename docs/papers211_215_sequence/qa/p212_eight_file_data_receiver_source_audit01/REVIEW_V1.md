# Eight-file DATA consumer — independent V1 source findings

Verdict: HOLD_V1_TWO_MINOR_GRAMMAR_FINDINGS. Critical / Major / Minor / open: 0 / 0 / 2 / 2. HOLD_OPERATIONAL / HOLD_EXTERNAL.

The three original files were read completely: 200-line receiver, 104-line CONTRACT, 27-line prospective request. Exact pins and full same-descriptor read records are in INPUT_V1.json and READ_V1_NATIVE.json. Full source-reading stdout is raw-equal to the subsequently keyed complete three bodies. The five selected accepted schema documents were also read completely: 189-line reader, 304-line entry, both request templates and the seven-line capture; their full read stdout is likewise raw-equal to the keyed bodies. No broader old-history proof audit was performed.

## Two concrete corrections

DATA-S1: ref() at line 71 does not type-check pin.sha256 before regex coercion. A one-element array containing a 64-hex string passes the root receipt-reference grammar. Grant reference pins receive a subsequent complete content comparison; the receipt reference does not. Add an explicit string requirement. This is a minor schema defect, not self-authentication or operation authority.

DATA-S2: input() at lines 77–89 admits an empty-key nonobject before its object guard. It also validates optional errors only when truthy; false/0/empty values skip validation and can survive complete-input checks. Require the object first, validate optional error fields by own-property presence, and require their absence on complete success. These witnesses are source deductions, not executed tests.

Both findings were sent to root, which accepted them and routed a new-only V2 to the author. V1 source, contract and request are not edited. Findings remain OPEN_V1; no first-round PASS is inferred while the delta is pending.

## Positive bounded source assessment

The canonical encoder matches the accepted entry's UTF-16 code-unit escaping, default UTF-16 key ordering, dense arrays, finite node/depth policy and safe-integer/no-negative-zero numeric rule. Whole reversible UTF-8, ASCII and exact canonical raw equality with one final LF reject duplicate keys, alternate whitespace/escapes and unsafe stdout number spellings. Native fractional wall times are deliberately outside that stdout grammar.

All eight candidate roles/order/limits and expected-null/settlement-null values are source literals. No candidate path is opened by this proposed consumer; the sole import is ordinary node:crypto. Full body hex is bounded and hashed for each row, even failed/absent rows; a present successful row requires all four equal ten-field regular-file metadata structures, fd, EOF, close, complete size and hash. Optional ENOENT has the exact absence shape. Partial bytes and error/close outcomes remain available; failed-row bytes are excluded from the accepted census and only a final failing row is allowed. This receipt neither interprets candidate contents nor establishes any installed dependency.

The exact native command/arguments match the accepted capture and ENTRY_REQUEST; continuation requests are empty-input, same-session and finite, with genuine final exit and no live final handle. Native nonempty control output yields HOLD. Source-copy/binding/raw roles are fixed; complete supplied body pins and four-key equality are checked without opening DATA paths. The required external context pin, complete native originals/projections correspondence and grant authenticity/consumption are an explicit root-received trust interface. The receiver does not itself perform that authentication; receipt references and booleans have no independent authority. Generic malformed, oversized or truncated DATA is retained as supplied and rejected, not repaired; failed accepted grammar remains failure HOLD.

## Independence, evidence and scope

The source author is /root/p212_eight_file_data_receiver_source, not this reviewer. A bounded read-only helper /root/p212_minimal_s0_independent_source_audit/receiver_canonical_native_check independently checked canonical/native interfaces and confirmed DATA-S1; this reviewer personally read all source/contracts and all selected old schema and identified DATA-S2. No source-author contact occurred; findings went through root. No reviewer changed proposed code.

The symbolic-dynamics-research skill supplied the scope/evidence gate. The skill and entire linked workflow were read; only current index heads were used as navigation. Initial combined instruction/state native 57359f actually truncated; its exact returned partial native is retained without asserting omitted state text was read. The complete skill occurred before truncation, and full workflow was separately read in caabca. All source/schema reads 53a012, 634f93 and 87f532 and fixed-file full read 0da155 completed untruncated. Own evidence-directory ENOENT 96c893 is a documentary-creation observation only, not any runtime reservation.

No proposed import, execution, syntax/AST/test, runtime raw/binding/future/host/candidate query, observer/grant/build/science, central index, manuscript, Git or external action occurred. Existing accepted work is reused only at its selected unchanged schema scope. This is a compact open-finding record, not a new recursive audit or a DATA-processing authorization. Same-reviewer exact V2 delta is next.
