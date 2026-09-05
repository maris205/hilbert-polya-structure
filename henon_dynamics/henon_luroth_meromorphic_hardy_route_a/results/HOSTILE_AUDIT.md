# Actual hostile-check receipt

Executed `python -B code/c392_luroth_mutation.py`:
**32 repaired-hash + 3 JSON + 9 YAML = 44/44 refused.**

Each mathematical mutation recomputes the outer digest, then invokes the
standalone checker in a subprocess. The checks do not rely on the release
producer-byte comparison to detect wrong source data.

Covered metadata/baseline, target false-to-true and false-to-integer-zero,
numeric bool/float, route upgrade, unknown/missing/duplicate rows, source
mathematical values, canonical rational fractions and source-boundary changes.
Parser attacks cover duplicate JSON, NaN, Infinity; YAML duplicate/nonstring
keys, implicit date, anchor/alias/merge, explicit tag, route zero substitution
and target claim upgrade. The unmodified source is the valid control.

The checker validates exact types before mathematical comparison, rejects
all unexpected evidence members, and locks evaluator semantics separately.
This is adversarial regression, not a formal proof that no software defect exists.
