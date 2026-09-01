# Hostile audit

The hostile harness mutates one semantically decisive field at a time, repairs
the receipt's internal payload hash, and then invokes the producer-independent
checker on the mutated bytes.  This prevents a trivial stale-hash failure from
counting as semantic detection.

## Mutation classes

- candidate/source/evaluator/date/epoch/scope identity;
- flow matrix, determinant, symplectic, energy, and semigroup fields;
- stable frequency, amplitude, action, normal-form, and Krein-sign fields;
- bounded and forward-bounded dimensions, growth rates, and regime labels;
- active-mode minimal periods and stable/critical/zero-axial strobe dimensions;
- field-sign conjugacy and boundary labels;
- Route-A tuple/overall/Route-B permission; and
- forbidden arithmetic/operator claim flags.

## Result

`26/26` repaired-hash mutations were rejected.  The unmodified control receipt
passes the same checker.  Fresh producer replay is also byte-identical, so the
audit covers both semantic validation and deterministic regeneration.
