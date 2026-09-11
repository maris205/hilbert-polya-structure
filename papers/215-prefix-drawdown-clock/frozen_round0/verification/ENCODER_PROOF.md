# Deterministic wire encoder proof — author SOURCE

The sole imported module in verify.py is sys, used only for argv, stdout and
exit. The encoder uses no json library, hidden serialization, locale operation,
floating-point number or external data. This is a deductive source argument,
not a parse test or executed round-trip claim.

Domain G is the set of finite acyclic values recursively formed from None,
exact booleans, exact Python integers, strings with every code point in
32..126, lists of G, and dictionaries with distinct such string keys and G
values. All emitted scientific records lie in G: numeric quantities use
integer arithmetic; predicate results are booleans; absent failure context is
None; all labels are literal printable ASCII; words and tuples are converted
to lists before inclusion. Sets are converted to sorted lists. No tuple, set,
float, class instance or exception string is emitted. In particular the
runtime failure reason is fixed ASCII, not arbitrary exception text.

For None the encoder returns null. The exact-type boolean branch precedes
integers, yielding true or false rather than Python's boolean spelling.
For an integer, str produces its ordinary decimal representation, with a
minus sign exactly for negative integers and no leading zero except zero;
this is a JSON integer token. All numerical values in the fixed finite boxes
are small finite integers, so decimal digit limits do not affect this domain.

For strings, the encoder opens and closes double quotes and visits characters
in their existing order. Each double quote or backslash is preceded by one
backslash; each other printable ASCII character is emitted unchanged. These
are exactly valid JSON string characters/escapes and decode to the original
characters. No newline, control character or non-ASCII character is accepted.
Thus encoded labels are unambiguous and cannot introduce an unescaped token
delimiter. Empty strings correctly become two quotes.

Structural induction proves the remaining cases. A list brackets, in order,
its recursively encoded members separated by commas, with no trailing comma;
the empty list is []. A dictionary first rejects non-string keys, then sorts
keys by Python string order (ASCII lexicographic on this domain), emits each
encoded key, one colon and its recursively encoded value, comma-separated
between braces. Keys are distinct because the input is a dictionary. The
empty dictionary is {}. By the induction hypothesis every component is valid
JSON and has its original meaning. Finite acyclic inputs terminate. Values
outside G are rejected rather than coerced. On G the result is therefore a
valid lossless JSON encoding, independent of dictionary insertion order.

The scientific enumeration fixes box and state order. All sets exposed on
the wire are sorted; constructed heights use lexical Cartesian order, and
their aligned sources retain that order. Comparisons and recurrence terms
use explicit source order. No timestamps, hashes, random seed, filesystem
ordering, object addresses or runtime exception messages enter the output.
Consequently identical successful arithmetic computations produce identical
ASCII text. One appended LF is the sole record terminator. Byte identity
additionally depends on the actual stdout text encoding/newline settings;
the future runtime binding must fix and record these (ASCII-compatible
UTF-8 and LF are the intended settings), and compare complete raw bytes.
This proof does not replace that future binding or an actual byte comparison.
