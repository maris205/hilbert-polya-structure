# P213 verifier output schema V1

Status: declaration before execution. No expected numerical result table,
canonical, PASS record or observed branch census is prefilled here.

## Transport and deterministic order

verify.py uses only integer/builtin operations and constructs the entire
output list before its first print. On successful execution, stdout is
ASCII tagged text with one LF per line and a final LF; no blank lines.
A complete result begins with P213_VERIFY_V1, follows the order below,
and ends with exactly one PASS line. The source does not print a digest.

Any exception, nonzero exit, stderr, missing record, malformed transport,
truncation, incomplete native capture or failed declared assertion is a
failed run. A buffered computation is not an atomic transport guarantee:
a failed/partial print is still failure, even if a visible prefix looks
correct. The future receiver preserves the complete actual native result,
including stdout, stderr and exit status, without reconstructing omitted
bytes. No “PASS” in a document substitutes for the actual final record.

Carriers run in increasing n=1..6, then N=0..4. States are lexicographic
weak compositions. For each target y, n>=3 mixed words are visited by
ascending integer mask 1..2^n-2, before that target's TARGET record.
One CARRIER record follows all its targets. TOTAL and PASS follow the
last carrier. There are 30 CARRIER and 461 TARGET records by contract.
WORD records cover every mixed word for every n>=3 target; the count is
the sum of |X_(n,N)|*(2^n-2) over those carriers, checked by complete
record reception, not by a hand-filled census in this source package.

## Token grammar

Record fields use a single ASCII space separator and key=value tokens.
No value contains whitespace. All site vectors use n comma-separated
nonnegative decimal integers, in label order 0..n-1, without parentheses.
A vector list uses semicolons, lexicographic vector order; "-" is empty.
A word is exactly n bits in edge-index order s_0...s_(n-1); it is not
the conventional most-significant-bit-first rendering of its integer mask.

An interval list uses semicolon-separated five-integer tuples:
prepeak_index,peak_index,lower,upper,pair_sum. Coordinate indices are
reduced modulo n. Tuple order is increasing valley index of its block.
Signed decimal upper endpoints are allowed, including -1 for an empty
interval. "-" means no interval recorded. For a rejected word this list
is only the interval prefix constructed before first failure; it is not
the complete set of structural long ascents.

A census uses comma-separated KEY:nonnegative_integer entries, in the
declared order. Status order:
ACCEPTED, PARITY, NEGATIVE_DESCENT, NONSTRICT_DESCENT, SHORT_PEAK,
ASCENT_EQUALITY, ASCENT_ORDER, EMPTY_INTERVAL.
Shape order: R1, R2, RGE3, WRAP.

## Exact record layouts

1. P213_VERIFY_V1
2. PARAM n_min=1 n_max=6 mass_min=0 mass_max=4 carriers=30 states=461
3. WORD n=<n> N=<N> y=<vector> s=<word> status=<STATUS>
   weight=<integer> intervals=<interval-list> sources=<vector-list>
4. TARGET n=<n> N=<N> y=<vector> next=<vector> tau=<integer>
   terminal=<vector> indegree=<integer> fixed_product=<integer-or-"-">
   sources=<vector-list>
5. CARRIER n=<n> N=<N> states=<integer> height=<integer>
   max_indegree=<integer> maximizers=<vector-list> status=<census>
   shapes=<census> accepted_shapes=<census> degree_two=<integer>
6. TOTAL carriers=<integer> states=<integer> words=<integer>
   two_site=<integer> degree_two=<integer> status=<census>
   shapes=<census> accepted_shapes=<census>
7. PASS checks=<integer>

Layouts above wrap for prose only; every actual record occupies one line.
All keys occur once and in the displayed order; no extra fields are emitted.

WORD sources are the theorem reconstruction's full sorted source list for
that one comparison word, checked against direct graph sources having
exactly that word. Its weight equals its source count when ACCEPTED and
is zero for every rejection. Constant words are not WORD records:
all-zero is impossible; all-one contributes the uniform source only.
For n<=2 the atlas is the identity and emits no WORD records.

TARGET next, tau, terminal and sources come from the direct forward graph
and direct trajectory. Each is checked against its applicable theorem
formula. fixed_product is "-" for a nonfixed target and the checked
integer product for a fixed target, including the uniform case.

CARRIER maximizers lists all maximizing targets in that finite carrier
only, never all-size extremizers. TOTAL status sums the first-failure
classification of complete mixed-word attempts. shapes counts all
structural blocks of those attempted words, even if an earlier test
rejected the word before a block's formula was reached. accepted_shapes
counts those same block shapes only in accepted words.
R1/R2/RGE3 refer to one-run lengths 1/2/at least 3.
WRAP is added for a block whose unwrapped next-valley index is >=n;
touching n is counted as crossing the chosen cyclic cut.
degree_two counts accepted words with at least two independent intervals;
interval length one still counts as an interval parameter.
two_site counts n=3 initial states with exactly two positive residual
coordinates, for which the exact clock is checked through one time after
fixation. PASS checks counts actual require() calls, including the final
coverage assertions; it is not a count of independent theorems.

## Assertion and branch scope

Every direct source belongs to the carrier; mass and minimum are preserved,
residual zeros persist, and the fixed/isolated equivalence holds.
Every trajectory rejects a nonfixed repeat and ends at the exact original
endpoint terminal state. Full-carrier heights equal the piecewise formula,
with an attaining witness; two-site residuals satisfy the pointwise clock.

Every mixed-word source set equals the direct graph's set for that word,
and the disjoint union equals every target's complete predecessor set.
Automatic mass and exact tie words are asserted, not used to filter
incorrect reconstructed sources. The fixed-target product is checked for
all fixed targets. Upper-bound instances are checked for n>=3; lower-bound
instances and spaced-spike witnesses only where N>=2*floor(n/3).

The final assertions require every retained first-failure status other
than NEGATIVE_DESCENT to occur, every accepted shape to occur, at least
one degree-two word, and at least one two-site clock. These are source
requirements, not observed results. NEGATIVE_DESCENT is a defensive guard
that is unreachable for a nonnegative target and recursively nonnegative
forced values; its census is required to be zero, not advertised as
positively exercised. No extra parameters or additional experiment may be
silently used to repair a failed coverage assertion.

Finite equality does not prove the all-parameter atlas or asymptotic
bounds. An unexpected failure returns to a source delta and review.

