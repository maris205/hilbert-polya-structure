# Hostile artifact audit

Fourteen semantic changes were tested after recomputing the canonical payload SHA-256: wrong phase, wrong Bessel order, incorrect zero-order boundary status, gauge shift, generic-flux physical time reversal, cutoff phase, heat value, cross section, target-zero scope claim, Route B flag, baseline, YAML digest, missing channel, and unexpected schema key. All were rejected by the independent checker.

Two malformed JSON inputs test duplicate keys and nonfinite NaN; both were rejected. Separate smoke cases reject boolean-as-integer fractions and duplicate, anchored, aliased, or merged YAML. These attacks validate the declared checker surfaces, not every possible malicious payload or mathematical claim.

The G3 follow-up adds three isolated attacks on the actual `c383_release_manifest.py --write` command: unknown YAML key, literal false replaced by integer zero, and unquoted evaluation date. A strict parsed YAML and hard raw-hash gate runs before any release generation. All three commands failed specifically with `evaluation changed` and produced no manifest. The full hostile lane now rejects 19/19 cases, including 14 repaired-hash payload cases and three writable-entry YAML cases. The live frozen YAML bytes were not modified by these tests.
