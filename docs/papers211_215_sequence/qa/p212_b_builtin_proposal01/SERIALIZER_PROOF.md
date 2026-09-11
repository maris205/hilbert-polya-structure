# Dependency-only serializer and factorial proof

Status: SOURCE-LEVEL DEDUCTION, NOT_EXECUTED. No proposed source was imported,
compiled, AST-parsed or invoked. Examples below are deductions from code,
not saved tests. Root must read and accept the exact proposal before applying
it or binding any initial scientific invocation.

## Supported domain and static coverage

The encoder's domain D is finite acyclic trees made from exact Python bool,
int, ASCII str, list, tuple and dict objects. Dictionary keys must be exact
ASCII strings. Nested sharing without cycles is permitted. Strings contain
only code points 0 through 127. None, floats, sets, arbitrary objects, scalar
subclasses, non-string dictionary keys and non-ASCII strings are outside D.
Unsupported scalar/container types are rejected; cycles are not promised to
terminate or receive a special diagnostic. They do not occur in the checker.

This restricted domain covers every proposed output and comparison operand:

- States, IDs, edges, lengths, periods, coefficients and factorial arguments
  are exact integers from ranges, integer arithmetic and tuple/list construction.
- Predicate outcomes and membership conditions are exact Booleans. Scope and
  label/status/method strings are fixed ASCII literals or ASCII integer f-strings.
- All emitted dictionaries have literal string field names, except row_counts,
  whose seven keys are fixed ASCII strings. The temporary integer-keyed or
  tuple-keyed catalogue/group/coefficient/class maps are converted explicitly
  to lists or labelled records before any call to wire.
- Internal sets become sorted lists. Anchor's None sentinel is filtered by
  the existing `is not None` branch and is never placed in an output record.
- The output has shared state/path values but no containment back-reference.
  In particular CHECKS never appears inside one of its own observed/expected
  values; it is attached only to the final outer result.

This is a source argument, not an execution census. Exact graph enumeration,
all scientific constructions and the complete field schema are unchanged.

## Scalar encoding

The `type(value) is bool` branch emits exactly true or false. The exact int
branch emits base-ten `str(value)` without surrounding quotes. They are
different JSON token classes: Boolean true is not integer 1, and false is
not integer 0. Negative integers include their minus sign. The actual fixed
carriers generate only modest-sized integers; no unbounded decimal-conversion
resource guarantee is claimed beyond the interpreter's ordinary operation.

For an ASCII string, the encoder begins and ends with a double quote and
processes each character once. The disjoint cases are:

| Input code point | Emitted JSON content |
| --- | --- |
| quotation mark | backslash followed by quotation mark |
| backslash | two backslashes |
| 8, 9, 10, 12, 13 | short escapes b, t, n, f, r respectively |
| other code points below 32 | lowercase four-hex-digit Unicode escape |
| 127 (DEL) | lowercase Unicode escape 007f |
| all remaining ASCII code points | the unchanged character |

Every literal character in the final case lies in 32..126 and is neither
quote nor backslash, so it cannot end the string or open an escape. Every
control character is escaped, and each Unicode escape has exactly four hex
digits because its value is at most 127. Escaped quotes/backslashes preserve
the input characters rather than becoming structural delimiters. Thus the
result is valid ASCII JSON and decodes to the exact original string. Slash
is left unescaped, which is valid JSON. Empty strings become two quotes.
No locale, dictionary iteration order or imported encoder affects this rule.

These spellings are the conventional compact ensure-ASCII encoding used by
the replaced JSON call on D, including DEL. For the actual generated string
subdomain, all characters are ordinary printable ASCII without quotation,
backslash or control characters; therefore wire-byte equivalence on actual
scientific fields additionally follows without relying on exceptional escape
cases. Error messages go to stderr and are not passed to wire.

## Containers, determinism and equality

Assume inductively that wire encodes every child in D correctly. Lists and
tuples both produce a bracketed comma-separated sequence of their child
encodings in the original order, with no whitespace. The empty case is [].
Consequently tuples normalize to exactly the same representation as lists,
as under the old JSON call; ordering remains significant.

For dictionaries, key types are checked before sorting. The key strings are
sorted lexicographically, and each key is itself passed through the string
encoder (which also checks ASCII). Each value is recursively encoded. Braces,
colons and commas are inserted only as structural delimiters. Unique Python
string keys remain unique decoded JSON keys. Sorting makes the result
independent of dictionary insertion order. The empty case is {}.

Induction proves validity and determinism over D. Unique JSON parsing shows
that equal wire strings have equal normalized JSON value trees. The only
intentional normalization within D is list versus tuple; Boolean and integer,
string and numeric, array and object, element order and dictionary key spelling
all remain distinct. Conversely equal normalized trees have identical sorted
compact encodings. Thus

`wire(observed) == wire(expected)`

has exactly the same truth value as the old sorted JSON-string comparison on
the declared domain. The old comparison used the encoder's default spaces,
while wire is compact; removing deterministic separator spaces from both
operands changes no equality relation. Final stdout already requested compact
separators, so its bytes remain identical by the scalar/container induction.
Both versions append the same single LF and use the same single stdout write.
This is an equivalence proof, not a claimed raw-output comparison: neither
version has been executed by this source-delta task.

## Factorial replacement

The helper accepts exact nonnegative integers and starts result at one.
After multiplying factors 2 through k, the invariant is result=k!. The
initial empty product handles zero and one. At loop completion result=n!.
All existing call sites have n in 1..4 and n-s in 0..3. Hence their arguments
are supported and their values exactly match the removed math.factorial
calls. Rejecting Boolean or negative arguments changes no reachable call.
No new arithmetic, cutoff, core term or scientific predicate is introduced.

## Exact changed dependency boundary

The full native textual diff contains only removal of `import json` and
`import math`, insertion of wire/factorial, replacement of the comparison
encoder, replacement of the two factorial expressions, and replacement of
the final output encoder. All graph/state/orbit/catalogue/anchor/recurrence
code and every literal scientific parameter remains byte-identical outside
those sites. The two direct imports retained in the proposal are itertools
and sys. No claim that itertools is builtin on a particular interpreter is
made here; no interpreter/module/host query was performed.

OUTPUT_PLAN's old exhaustive runtime-closure paragraph is not overridden by
this dependency-only proposal. Its original lines 12–15 mention startup,
imports, configuration and native-extension/loader closure. Root's separately
commissioned ordinary-runtime source must explicitly resolve that policy
scope before execution; removing two imports does not itself waive a gate.
All original source-only findings and ready/hash statements remain immutable
history. This package supplies no mathematical revision or final Review B.
