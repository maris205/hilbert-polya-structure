# Exact P212 producer-call and child-interface decision

2026-09-09 UTC, root-owned source decision. The complete 865-line / 40430-byte
author verifier was read as text at the accepted source gate and again in
this continuation. Its SHA-256 remains
16cc2ff86854c6c28d530de65225b941f9e063fa22159ccd8f0c4082b80654e7.
No AST parse, compilation, import or producer invocation supplies this review.
The accepted PARAMETERS.json is the only application data input, exactly
609 bytes / 0870d9de8a1e2dde2c568656ea69b39511ae3a8ebf992f787c6e5ae060ca4550.

The entire [output schema](../../../../papers/212-closed-pointer-orbits/OUTPUT_SCHEMA.md)
and fixed four-carrier parameter contract were received at the
[source gate](../p212_author_source_reception/RECEPTION.md).
The original 12 output roles and 46 predicate families are unchanged. This
static interface decision is not a saved-output semantic acceptance; no
expected success transcript or observed size/count has been prewritten.

## Reachable standard-library surface

The five literal scientific imports are itertools, json, math, sys and
fractions.Fraction. There are no local helpers, dynamic imports, eval/exec,
subprocess, network, filesystem discovery or other application file reads.
Only the explicitly named UTF-8 parameter file is opened. The fixed JSON
callbacks reject duplicate keys and float/nonfinite number tokens; the
whole parameter object must match the fixed contract. All finite state
coordinates, multiplicities, counters and rational numerators/denominators
are consequently constructed from integers within the four-carrier source.

The following is a source-based reachability argument, not a universal
library trace. Actual source bodies were read for these branches:

- itertools.product/permutations/combinations and math.factorial operate on
  built-in finite iterables/integers. These built-in modules are supplied by
  the actually keyed interpreter, not guessed missing extension filenames.
- Fraction is constructed from one int, one existing Fraction, or two
  ints. Addition, multiplication, their reverse operators with ints,
  numerator/denominator access and truth conversion are the used methods.
  The series power helper is repeated polynomial multiplication, not
  Fraction.__pow__. Sum's integer start follows the registered Rational
  reverse-add branch. Fractions are values, not mapping keys; serialization
  explicitly converts them to numerator/denominator integer pairs.
- Actual fractions.py lines 6–11, 62–164, 256–262, 356–381, 451–497 and
  729–733 cover import initialization and these operations. _add/_mul use
  integer arithmetic and math.gcd. The numbers.Rational/Integral hierarchy,
  Integral.register(int) and the active abc/_abc instance-check route were
  inspected. No producer float/Decimal/string construction, from_decimal,
  limit_denominator, copying/pickling or custom numeric subclass is used.
- decimal is imported by fractions at initialization, selecting the actual
  observed C _decimal branch. Its keyed initialization/ELF dependency graph
  is received in the [complete discovery](../p212_runtime_discovery_root_reception01/RECEPTION.md).
  The producer does not invoke Decimal methods. The inactive _pydecimal /
  contextvars fallback is neither asserted active nor appended to the lock.
- json.load receives an already decoded str from the explicit UTF-8 file;
  json.dumps receives only builtin JSON-compatible data after Fraction
  conversion, with ensure_ascii=True, allow_nan=False, sorted compact keys.
  The actual json module/encoder/decoder/scanner source selectors were
  inspected; the observed _json module is keyed. There is no custom encoder
  default or uninspected user-defined JSON object method. sys stdout/stderr
  and ascii encoding use the declared interpreter/encoding configuration.

Thus the new reachable fractions methods introduce no identified file
dependency beyond the actually received 130-key discovery. This is a
bounded inference from this exact program and selected source branches;
it does not certify arbitrary Fraction/Decimal methods, continuous native
opens, all failed paths, or the absent separately archived late sample.
Every future module/map/open/configuration observation must still be covered
by the preaccepted key. A missing dependency stops the operation; no lock
extension after science is authorized.

## Exact compiled child interface

Root approves the received adapter's fixed compile/exec interface for this
exact source. A fresh isolated child runs from the new physical recorder
capsule containing only verify.py and PARAMETERS.json, copied and actually
compared with their pinned originals. sys.argv is exactly the absolute
verify path, --parameters and absolute parameter path. The exec globals
set __name__ to __main__ and __file__ to the exact copied source path.
The source does not use __spec__, __package__, __loader__, relative imports,
main-module identity, or inspection of its own globals/module record.
Its explicit SystemExit(0) is accepted only by the adapter's exact zero-exit
branch, and a nonzero/error remains a failure. This is not direct
`python verify.py` startup and is not described as such.

The received source/module-bootstrap and discrete observation limitations
of the runtime adapter/core remain unchanged. Root's outer native capture
must cover startup before internal gates, all real stdout/stderr, and actual
return/settlement. Initial output remains only a candidate until complete
native/dependency and every saved semantic field are received. Exclusive
CANONICAL.json adoption and a separate strict-pair binding remain later.

No theorem, source, parameter, cutoff or manuscript claim is changed here.
Root is a proof contributor, not an independent mathematical reviewer.
This document alone is not operational authority; the separate exact
AUTHORITY.md and enabled binding control the sole future initial invocation.
