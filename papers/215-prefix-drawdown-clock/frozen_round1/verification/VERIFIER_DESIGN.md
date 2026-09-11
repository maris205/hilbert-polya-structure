# P215 author verifier design — not executed

This original standalone implementation imports only sys. It does not import
or copy any old paper, pilot, reviewer or scientific helper implementation.
Its mathematical input is the admitted Fresh68 theorem contract and author's
DESK, not observed finite output. This contributor is a verifier/proof author,
not an independent manuscript reviewer. The repository workflow requires
source reception and a separate grant before running even help or import.

`words` forms the full Cartesian carrier by appending every digit in increasing
order at each position. Induction on length gives each word once in lexical
order; length zero gives the singleton empty tuple. Boxes retain n=0 and q=0
duplicates as distinct parameter cases. PARAMETERS.json records the fixed
source-derived 24-box / 1798-state expectation, not empirical success.

`transition` scans coordinates once and updates the running maximum directly.
Its integer maximum minus the current entry is the literal admitted map.
Actual edges are computed for all states. For each source, the orbit walk
uses only the actual edge table and a dictionary of already visited states;
it stops only on repetition. The orbit includes the repeated endpoint on
output. The first occurrence index of that endpoint gives the transient
clock and the intervening suffix gives the cycle. Finite carrier closure
guarantees termination without a formula-based cutoff. All cycles are unioned
to obtain the actual recurrent set, not assumed to be zero.

Separately `signs` forms initial-zero differences, deletes zeros and compresses
same-sign runs. The comparison joins this independent formula to the actual
clock. It also checks the stronger signed-run transformation, its numeric
drop, and the full deepest-state predicate. Vacuous alternation for n=0 is
recorded literally; maximal_predicate explicitly uses the singleton boundary
instead of suggesting a positive-height equality. The complete actual and
predicted deepest sets are compared after every source has been inspected.

Actual predecessor buckets receive every source from the direct edge table.
`inverse_formula` has no access to this table or its buckets and never calls
transition. For each eligible target it independently finds zero blocks,
barriers b and prefix barriers B. It enumerates every height tuple in the
bounded Cartesian height box, filters precisely for monotonicity and lower
barriers, and reconstructs every aligned source from L_j-y_i. All retained
height tuples and their source words are emitted. Complete sorted source lists
are compared to actual buckets; a separate cardinality/set comparison checks
injectivity. This does not confuse a cardinality check with a bijection check.

The same target's reverse-complement ceilings feed an independently evaluated
explicit binomial recurrence, not the enumerated height list. `choose` uses
the product recurrence C(u,r)=C(u,r-1)(u-r+1)/r from C(u,0)=1, whose divisions
are exact; it gives zero if r>u>=0 and rejects negative arguments. Each A_m
emits its base coefficient and every first-violation subtraction, including
both binomial indices, its value, prior-prefix count and product. The final
value is separately compared to actual and reconstructed cardinalities.
The empty target on n=0 emits A=[1] and the single empty height/source;
nonimage targets emit empty formula arrays and count zero.

Every target is retained, including empty fibres. Actual/predicted images,
actual maximum fibre and every maximizing target are emitted and compared.
Clock and fibre censuses include all bins from 0 through carrier size,
including zeros; total counts and fibre mass are checked. The complete
recurrent set and sharp height are compared. The top-level box and state
totals are separate comparisons. These are finite consistency checks, not
proofs of the unbounded theorem or novelty of any component.

`Ledger.compare` never raises on a mathematical disagreement: it retains both
values, the predicate name and false result and increments failures. Thus
every box still emits on ordinary semantic failure, ending with pass=false
and exit 1. Exceptions yield an explicit incomplete failure document with
current box context and already completed boxes, exit 2; external capture
must also preserve partial output/stderr for uncaught process/I/O failures.
No assertion is disabled by interpreter optimization, no failed comparison
is omitted, and no post-hoc output selection is permitted. The encoder's
exact grammar/proof is in ENCODER_PROOF.md; output and future provenance/replay
obligations are in OUTPUT_SCHEMA.md and OUTPUT_PLAN.md.
