# Complete output schema v1 — planned, no output generated

The wire is one JSON document plus LF, encoded by the proved restricted
ASCII encoder. OUTPUT_SCHEMA.json supplies structural JSON Schema vocabulary;
no schema validator or parser has been run. This prose specifies semantic
constraints beyond the structural schema. Arrays are complete, not examples.
No CANONICAL.json exists as a result of this source contribution.

Success/semantic-failure documents have kind=p215_author_verification and
schema_version=1. The parameters repeat the exact fixed arrays. Boxes appear
in n-outer/q-inner increasing order, exactly 24, with carrier size (q+1)^n.
Each states and targets array contains every carrier word exactly once in
lexical order. The total source-derived expectation is 1798, pending execution.
checks is the number of all comparison records at all levels; failures is
the number whose pass is false; top-level pass is exactly failures==0.

Every comparison has name, actual, expected, pass. Its values may recursively
be the encoder's JSON values; pass must equal actual==expected, with the
intended typed scientific meanings described here. All named comparisons
occur exactly once at their specified scope and in the source order below.

State record fields:

- x, Fx: input and literal output words. orbit lists every distinct visited
  word followed by the first repeated endpoint. repeat_index is its original
  index; period is len(orbit)-1-repeat_index; cycle is the suffix of distinct
  words from repeat_index; clock is repeat_index.
- differences: length-n differences from initial zero. nonzero_signs is their
  nonzero signs, runs compresses equal adjacent signs. output_differences,
  output_nonzero_signs and output_runs are the same statistics for Fx.
- alternating_nonzero: every difference is nonzero and adjacent differences
  have opposite signs. maximal_predicate uses this for n,q>0 and x==zero on
  singleton boundaries.
- comparisons: exact_clock, cycle_is_zero, output_runs, run_drop,
  deepest_predicate, in this order, with both sides defined in verify.py.

Target records have y, actual_predecessors (lexical full bucket), actual_count,
image_predicate, formula, comparisons. formula fields are:

- zeros: 1-based target zero positions; b and B: block maxima and prefix
  maxima; c: reversed-complement ceilings q-B in increasing order.
- height_sequences: every feasible monotone height tuple in lexical order.
  constructed_sources is aligned one-to-one with that array, without sorting
  away the pairing; complete_fibre compares its sorted version to the bucket.
- A: all A_0..A_k; count is A_k. recurrence_terms lists m=1..k; each term has
  m, base_upper, base_lower, base, subtractions, value. Subtractions are in
  i=1..m-1 order and contain i, prefix_count=A_(i-1), upper, lower, binomial,
  product. The value is base minus the sum of all products.
- On n=0: zeros/b/B/c/recurrence_terms are empty, A=[1], both height_sequences
  and constructed_sources are [[]], count=1. On a nonimage target y_1!=0:
  every formula array is empty (including A), count=0. These are separate
  branches, not applications of nonempty-target notation to the empty word.

Target comparisons, in order: complete_fibre, construction_injective,
height_source_lengths, recurrence_actual, recurrence_construction,
image_predicate. They retain actual buckets even when formula checks fail.

Each box also contains sorted recurrent_states, actual height, lexical
deepest_states and expected_deepest_states, lexical image and expected_image,
maximum_fibre, lexical maximum_fibre_targets, clock_census and fibre_census.
Both censuses have carrier_size+1 bins; bin index is the clock or fibre size,
bin value is its complete state/target count, including all zero bins.
Box comparisons, in order: carrier_size, unique_recurrent, sharp_height,
complete_deepest_set, complete_image, image_size, maximum_fibre,
maximum_fibre_targets, clock_census_total, target_census_total, fibre_mass.
Top-level comparisons are box_count and state_count. Consequently the planned
comparison count is 11 times the state total plus 11 times the box total plus
2 (20044 at the source-derived expected domain), not an executed assertion
count. The nonimage and boundary targets still receive all six comparisons.

Argument failure is exactly kind=failure, reason=arguments_forbidden. Runtime
failure has kind=failure, reason=runtime_exception, context={n,q},
completed_boxes, checks and failures. Completed boxes may be a proper prefix;
the failing current box is identified by context and is not claimed complete.
Both exit 2. A complete semantic-failure document exits 1; a complete successful
document exits 0. Hard process/I/O failure may leave incomplete raw output and
must not be forced into the success schema. The executor must preserve every
failed original before any separately authorized changed-source rerun.

Structural conformance alone cannot establish scientific correctness or
provenance. Future independent DATA reception must reconstruct every record
and comparison, check complete membership/order/counts, receive the full
actual stdout/stderr/exit and dependency key, then compare raw replay bytes.
