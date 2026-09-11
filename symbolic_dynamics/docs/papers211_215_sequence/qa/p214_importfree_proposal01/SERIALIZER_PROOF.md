# Proof of the proposed P214 serializer's domain and exact spelling

Status: `PROVABLE AS STATED ON THE EXPLICIT DOMAIN / SOURCE_ONLY`.
No serializer or scientific program has been executed. This is an author
deduction for root review, not an independently accepted test result.

## Claim, assumptions and dependency map

Let D consist of exact builtin None/bool/int/str values and finite acyclic
list/tuple/dict structures over those values, with exact str dictionary keys.
Sharing a child between two branches is allowed; ancestry cycles are not.
Assume ordinary, unmodified builtin types and sufficient interpreter resources
for both encoders to finish. Then the proposed `wire(v)` for every v in D
has the same string as

    json.dumps(v, ensure_ascii=True, sort_keys=True,
               separators=(",", ":"), allow_nan=False).

This is exact serialized-string equality, not merely equal parsed objects.
Because both arguments are supplied to the same original stdout.write call
and followed by the same separate newline write, successful complete output
has the same bytes under the same stdout encoding/configuration. Buffering,
flush behavior (no new flush call), argv handling and exit handlers are
unchanged. This is a conditional equivalence proof, not a measured RAW match.

The proof depends on: (1) individual character spelling; (2) primitive value
spelling; (3) structural induction for containers; (4) an exhaustive census
of every record constructor and mismatch operand in the frozen source.

The [Python documentation](https://docs.python.org/3/library/json.html)
specifies the supported container/scalar conversions, ensure_ascii,
sort_keys and compact separator options. The selected
[CPython reference source](https://raw.githubusercontent.com/python/cpython/3.10/Lib/json/encoder.py)
supplies the concrete escape spelling and ordering rule inspected here:
ESCAPE_ASCII/ESCAPE_DCT, py_encode_basestring_ascii, primitive dispatch and
the list/dict branches. It is a reference implementation, not a discovered
local runtime. No claim is made about interpreter resource failures, timing
or arbitrary externally monkeypatched I/O/type objects.

## 1. Every string code point

`wire_string` opens and closes with a quotation mark and processes code
points in their original order. Its mutually exclusive cases are exhaustive:

| Input code point | Output fragment inside the quotes |
| --- | --- |
| U+0022, U+005C | backslash-quote, doubled backslash |
| U+0008, U+000C, U+000A, U+000D, U+0009 | the short b, f, n, r, t backslash escapes |
| Other U+0020 through U+007E | the character unchanged, including slash |
| Remaining code point at most U+FFFF | backslash-u followed by exactly four lowercase hexadecimal digits |
| Above U+FFFF | the two lowercase four-digit UTF-16 surrogate escapes |

For the last case, write n=code-0x10000. The high unit is
0xD800+(n>>10), and the low unit 0xDC00+(n & 0x3FF). Since
0<=n<=0xFFFFF, these lie respectively in D800..DBFF and DC00..DFFF.
This is the same pair encoded by the reference branch. For BMP code points,
format(code,"04x") has exactly four digits; each surrogate unit also does.
DEL U+007F is escaped, rather than copied. Lone surrogate code points are
in the BMP branch and emitted as their own escaped unit. No normalization,
Unicode replacement or locale-sensitive ordering occurs.

The empty string has only its two surrounding quotes. Concatenating the
proven equal fragment for every code point proves equal complete strings,
including arbitrary CLI and runtime-error strings. This does not rely on
the normal success stream happening to use only ASCII labels.

## 2. Primitive values

None, True and False return the literals null, true and false. The boolean
tests occur before the integer branch, so Python's bool/int relationship
cannot turn a boolean into 0 or 1. Exact builtin integers use decimal str;
the reference's integer representation gives the same decimal sign/digits
for an exact int. There is no leading plus or floating-point notation.
Exact strings use Section 1. These exhaust primitive members of D.

No float enters D, so the allow_nan=False promise is not weakened: no NaN
or Infinity token can be emitted. Unsupported values fail explicitly instead
of receiving an invented encoding. The proposal does not claim compatibility
for finite floats, nonstring keys, Enums or custom subclasses, all absent
from the frozen source's emitted values.

## 3. Container induction and alias safety

Induct on maximum container nesting depth. For a list or tuple, both
encoders retain element order and place the inductively equal child strings
between square brackets, separated by commas with no spaces. Empty lists
and tuples therefore both give [].

For a dict, all keys are exact strings. Sorting its keys before escaping
has the same order as sorting its key/value pairs: dictionary keys are
distinct, so pair comparison is decided by the key. The encoder does not
sort escaped spellings, which could differ from Unicode code-point order.
For every key it concatenates the equal escaped key, a colon, and the equal
child-value string; braces and comma separators are identical. The empty
dictionary gives {}. This proves the induction step.

The `active` set holds identities of containers on the current recursion
ancestry only. Each call adds its identity and removes it in a finally
clause. An acyclic structure never meets an ancestor twice, so the guard
does not reject any member of D. Reusing a completed sibling container is
allowed because its identity has already been removed. An actual ancestry
cycle raises before the record's stdout.write argument is available; cycle
handling is defensive and not needed to justify the emitted domain.

## 4. Complete coverage of all reachable emit values

The original and proposed record constructors outside the codec are
byte-identical. The following covers every emitter kind, not only the
successful terminal summary. Dictionary keys in every row are literal
field names or concatenations of literal check names, hence exact strings.

| Emitter | Constructed domain |
| --- | --- |
| run_start | ordered integer parameter lists and fixed strings |
| field | q/characteristic/modulus integers or None; string labels; integer addition/multiplication/inverse lists, with the zero inverse None; boolean checks |
| carrier | integer counts/codes and lists of dictionaries whose coefficients and valuations are integers; boolean checks |
| adapter | integer permutation/transition lists; an integer-field witness dictionary; boolean checks |
| state | integer coordinates/valuations/depths/IDs; orbit dictionaries containing integer lists and nullable first-zero index; integer scalar path; boolean checks |
| target | integer IDs/counts/codes, boolean feasibility, nullable unit/representative values, integer kernel/predecessor/coset lists; boolean checks |
| depth_row | integer thresholds/counts plus integer ID lists and boolean checks |
| fibre_row | integer row/counts and integer target lists, with boolean checks |
| carrier_complete | integer counts/IDs and lists; nullable witness dictionaries made only of integer/list/orbit values; boolean checks |
| run_complete | integer totals and string-to-integer counter maps, fixed strings, ordered integer parameters and boolean checks |
| verification_failure | string-field scope dictionary over integers or run strings; string check name; actual/expected operands described below; integer counters |
| runtime_error | type name and str(error), integer attempted count and string-to-integer preceding counters |

Every Audit.equal actual/expected operand is an integer, boolean, ordered
integer list, or string-to-integer record-count dictionary. Its scopes use
q,m,state/target IDs,h,d or literal run strings. The direct CLI rejection
adds only sys.argv[1:], a list of strings, and the empty expected list.
Field labels use str on integers. All coefficient and count arithmetic is
integer arithmetic; division uses //, never a floating-point quotient.
Generator expressions are consumed into list/sorted/sum/join results before
their surrounding payload is emitted; no generator or range object is
serialized. No source class instance, exception object, field/ring object,
set, file handle or callable is an emit value.

The builders allocate containers that refer only to primitive values and
already-built child lists/dictionaries. None inserts itself or a future
ancestor into a child. The check/count dictionaries store only booleans or
integers, so references to those shared dictionaries cannot create cycles.
Orbit and predecessor structures use integer IDs, not object references
back into states. Thus all emitted records are in D, including mismatch
operands and the exception handler's stringified metadata.

The helper has no I/O, imports or global mutation. Arithmetic methods,
scientific comparisons, parameters, no-argument guard, exception control,
record/check counters and output order are unchanged. Domain correctness
therefore establishes codec equivalence for every complete emit call of
the unchanged program; it does not execute that program or erase ordinary
resource/startup/I/O risks.

## Open risks and adoption boundary

The proposal has not been parsed by Python, imported, tested against the
installed json implementation or executed over the scientific box. An actual
runtime input key, author run and full output reception remain necessary.
Removing the json import is not proof that a prior runtime key automatically
applies. The two TeX range clarifications have no serializer or theorem
dependency. Root may adopt them independently of this optional code change.
