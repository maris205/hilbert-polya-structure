# Exact P211 author parameter contract

`parameters.json` is the sole mathematical/data input of `verify.py`.
The entire parsed object must equal the literal `EXPECTED_PARAMETERS`
specification in that source; unknown keys or changed values fail.
Its original byte length/hash must additionally be pinned by the recorder.

## Interface and lookup

Science argv, after interpreter flags:

```text
<absolute-capsule>/verify.py --parameters <absolute-capsule>/parameters.json
```

There are exactly two script arguments: `--parameters` and one absolute
POSIX path. There is no default path, sibling-file discovery, environment
lookup, optional mode or output flag. The required recorded working
directory is the fresh source capsule, although the implementation does
not use cwd to locate mathematical inputs. The interpreter requires
`-I -S -B` and optimization zero; the recorder also supplies and validates
a fresh absent `-X pycache_prefix` and its full runtime contract.

## Mathematical scope

- Exactly $n=1,2,3,4,5,6,7$; all nondecreasing maps $[n]\to[n]$.
- Carrier sizes $1,3,10,35,126,462,1716$, total $2353$. The source also
  compares each population with $\binom{2n-1}{n}$.
- Literal update is the ceiling onto right kernel endpoints composed
  after the ceiling onto the current image completed by $n$.
  Supports are recomputed every epoch. No extensive/top-fixing
  restriction is placed on the initial carrier.
- Exactly the seven named predicate categories in `parameters.json`.
  No new maximum-fibre, basin, all-time inverse or priority predicate.
- No randomness, external data, old pilot output or reviewer code.

## Predicate census semantics

| Category | Checks per box of size $M$ | Content |
|---|---:|---|
| C1 | $M+1$ | Every literal successor is in the whole carrier; complete distinct carrier census |
| C2 | $M+1$ | Every cycle is a singleton with predicted terminal, literal fixed iff equal coordinates; complete fixed/recurrent set equals the projections |
| C3 | $M+1$ | Every pointwise time matches the exact formula; full-box maximum and explicit parity witness attain the sharp height |
| C4 | $M$ | Every target has a literal predecessor iff the exact image condition holds |
| C5 | $M$ | Complete sorted observed and gap-decoded predecessor lists agree, without silently deduplicating the decoder |
| C6 | $M+1$ | Every Laurent count equals its fibre size; full inverse mass equals $M$ |
| C7 | number of image states | Literal next state equals the full endpoint-peeling decoder, common anchors persist, and the image-state clock drops by one unless already zero |

A check counts one stated conjunction, not its internal Boolean clauses.
Top-level `checks` must equal the sum of all category counts. C7's total
is computed from the actual first-image states; it is not an extra
assumption of an image-cardinality formula. Conditional validations inside
helpers are failure guards, not additional counted theorem predicates.

## Complete-output and failure policy

The success output follows `CANONICAL_SCHEMA.md`: one sorted-key compact
JSON object plus one LF, with every state and every target represented.
Runtime paths, dates, PID, timings and dependency observations belong only
in the outside native receipt and cannot change canonical bytes.

The science source writes no files. It reads only the explicitly named
parameter document, beyond ordinary interpreter/stdlib startup inputs.
No local helper, pilot, paper or reviewer module is imported. Direct
stdlib imports are `itertools`, `json`, `math`, `sys`; their transitive
source/native/runtime closure must still be inspected and frozen.

Success requires exit 0 and empty stderr. Predicate/schema/flag failures
raise exceptions, preserving a nonzero native return and full stderr.
The completed JSON is not written until every check succeeds. A timeout,
interruption, partial stream or unsettled writer is not a canonical.
No failed production is retried automatically and no cutoff is enlarged.

This document is a specification, not permission to execute the verifier.
