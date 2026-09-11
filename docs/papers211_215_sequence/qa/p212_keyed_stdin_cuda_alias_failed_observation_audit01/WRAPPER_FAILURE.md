# Preserved receiver documentary capture failure

The first documentary READ_RAW_LOSSLESS.cjs run returned native b34432,
exit 0, with a tool-level truncation warning: original token count 28471
exceeded that request's max_output_tokens=23000. The actual shortened
92105-character native output remains intact in READS_NATIVE_02.json;
no missing interval is reconstructed or credited as a whole return.

After the complete native object was retained, the wrapper's JSON.parse
failed with the actually returned message:
SyntaxError: Unexpected token 'W', "Warning: t"... is not valid JSON

A separate new documentary read of the same permitted raw files, with
max_output_tokens=45000, returned native 03c29e, exit 0, without truncation.
Its entire stdout parses losslessly and is preserved as INITIAL_RAW_RESULT.json,
with the actual request/result in INITIAL_RAW_NATIVE.json. This is a repeat
data reading, not an observer execution or retry of the consumed once grant.
The original raw files remained unchanged. The observer was never invoked here.

A later workspace-only envelope projection a3933f also exited 0 but exceeded
its native 15,000-token display limit (16,305 tokens before truncation).
That exact shortened return is retained, not labelled a full source reading.
The next smaller projection 62dddf exited 1 after printing the preparation
summary: its code mistook an array's inherited keys method for a keys array
and raised TypeError: out.keys.map is not a function. The original request,
partial output and complete actual error remain retained. A distinct corrected
projection 37893a used Array.isArray(out.keys), exited 0 and returned all seven
selected native-envelope summaries. These are documentary tooling failures,
not missing raw observer events, source defects or consumed-grant retries.

The separate, older root request-wrapper TextEncoder failure and unavailable
two parallel returns remain as documented by the frozen root receipt; they
are not reconstructed. No positive evidence is backfilled from either failure.
