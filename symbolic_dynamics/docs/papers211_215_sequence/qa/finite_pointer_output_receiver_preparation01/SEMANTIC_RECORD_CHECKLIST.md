# Semantic-record receiver checklist

Status: SOURCE_ONLY / NOT_EXECUTED / ROOT_FULL_SOURCE_RECEPTION_PENDING.
This checklist describes checks implemented in receive_output.py. It is not
a claim that saved output has passed. The source was frozen before root
announced the actual initial-output location; that output was not opened.

## Exact saved input and typed schema

1. Require a separate approved, hash-pinned root binding. No binding is
   created here. Check the receiver's exact source bytes and the root-bound
   saved-stdout path/hash/size. Producer and parameter pins in the binding
   must match the frozen original metadata; the receiver never opens them.
2. Require the root-bound physical cwd, clean system Python 3.10,
   -I -S -B, optimize zero, explicit ENV4, the exact source-only sys.path
   and a distinct nonexistent pycache prefix. Root separately checks
   transitive runtime/native provenance and actual command completion.
3. Decode the saved file as ASCII; reject duplicate object keys, every
   float/nonfinite numeric literal, and any deviation from sorted-key compact
   ensure_ascii JSON followed by exactly one LF. Do not normalize or rewrite
   saved stdout.
4. Check exactly the eight top-level fields, literal schema/role/arithmetic
   strings and complete fixed PARAMETERS object. The four boxes are exactly
   n=1,2,3,4 with 1,16,243,4096 states. No input field selects a cutoff.
5. Every saved semantic object is compared to a freshly reconstructed complete
   object using canonical typed JSON equality. This checks all nested keys,
   array order and number types, not just Python equality of 1 and true.
   Extra, missing, duplicated or reordered records cannot be ignored.
   All ratio fields are compared with reduced numerator/positive-denominator
   Fraction records; integral count fields must use integers.

## Complete record mappings

| Saved record family | Full reconstruction/check |
|---|---|
| states: id,u,v,f | Fixed-width base-n ID decoding supplies every declared lexical state exactly once; compare every coordinate, not just unique IDs or count. |
| states: next,predecessors,inverse_formula_state_id | Direct old-state overwrite computes every successor and the full incoming lists. A separately written inverse expression checks the saved inverse ID; inverse data never drives graph discovery. |
| edges | Compare the entire ordered [source,target] list against all direct literal successors. No target is dropped or replaced with an inverse shortcut. |
| states: orbit_id,orbit_position,preperiod,observed_period | First verify every directly reconstructed indegree is one. Then follow unused state IDs from the least remaining ID. Periods and positions come solely from this graph, without core or coefficient input. |
| graph_multiset,active_component,attached_tree_vertices,inactive_vertices | Rebuild the n+1 undirected edges by an integer adjacency matrix, including loop degree two and edge multiplicity; flood the active component from u and delete one degree-below-two vertex at a time. Compare every saved array. |
| core: vertices,edges,edge_count,degrees,kind,parameters,branches,chains,predicted_period,predicted_orbit_count,error | Check the complete labelled core. Maximal branch chains use canonical vertex orientation and full-graph occurrence IDs exactly as specified. Check lower/upper branch assignment for barbell a,b, all ordering and degeneration cases, period/multiplicity table values and null error on accepted output. |
| frozen_arrows,core_key,group_key,core_id,group_id | Recover every outside pointer, both attached trees and inactive components. Reconstruct full canonical JSON strings and lexically sorted key-ID dictionaries. Do not group by isomorphism type, core size or period. |
| orbits | Compare every cycle's ID, complete successor-ordered states starting at its minimum ID, period, distinct group_ids and core_sizes. The cycle list itself follows increasing minimum IDs. |
| groups | Compare complete states, distinct orbit IDs, observed periods and orbit count, predicted period/count, representative core/frozen arrows and core ID. Counts come from distinct discovered cycles, never state_count/period. |
| core_catalog | Compare every lexical core key, ID, first-state representative core object and complete increasing group list. Occurrence IDs may depend on the full multigraph; do not assume a catalogue representative's temporary IDs describe all frozen complements. |
| core_series.pieces and total | Independently sum the reviewed ordered core-length weights through s=4, including symmetry/decoration factors and theta internal-list composition coefficients. Check all nonzero (s,p) rows, order, exact rational values and the complete piece sum. No q cutoff or saved coefficient is an input to this computation. |
| egf_extension_terms | Check every saved nonzero (s,p) term, exact core ratio, falling-factorial/frozen-map multiplier and exact contribution, in order. |
| total_orbit_formula_terms | Check every s=1,...,n term from the separately written c_s formula and its exact multiplier/contribution; do not substitute the observed orbit total. |
| all histogram/scalar box fields | Check complete observed and expected period/core-period rows, attainable period set, maximum, fixed-state count, orbit total and weighted cycle cover. Unexpected keys/periods cannot be truncated away. |

Temporary multigraph occurrence IDs serve only the wire-format chain audit.
They are never carrier coordinates, extra orientation labels, group keys
or additional orbit distinctions. In particular, indistinguishable direct
theta paths cannot be split into spurious labelled orbits.

The degree-two/core formulas are deliberately the same reviewed theorem
contract, not new mathematical claims. This receiver independently implements
their finite inspection, not an independent proof of their all-n correctness.

## Every saved assertion record

The receiver reconstructs complete lists, including id, observed, expected
and pass, in the original declared source order:

- Ten S01–S10 comparisons for every state.
- Three O01–O03 comparisons for every directly discovered cycle.
- Three G01–G03 comparisons for every exact core/frozen group.
- Every E01 integrality comparison for the retained extension terms.
- All B01–B11 comparisons in each of the four boxes.
- Every nonzero-coefficient C01, the C02/C03 pair for each s=1,...,4,
  and global T01/T02/T03, including T03's own ID in uniqueness.

The entire saved top-level and per-box check arrays are compared, not sampled.
The final summary must exactly count all these records, preserve failed-ID
order, and agree with their reconstructed booleans. No record may be removed
because the supplied summary says PASS. The receiver only accepts a complete
successful output; a malformed or failed report is refused and left unchanged,
not repaired, rewritten or retried.

## Explicit small-box coverage ceiling

Even after a later accepted n<=4 reception, these subclasses remain
unexercised and deductive-only:

| Absent subclass | First possible core size |
|---|---:|
| Figure-eight with both cycles of length at least three | 5 |
| Barbell with both cycles of length at least three | 6 |
| Theta with three nondirect paths | 5 |

The receiver reports these exclusions on success. Its s<=4 coefficient
implementation does not exercise the three-nondirect theta contribution.
No n=5/6 state, target snippet or larger box is generated. No received finite
histogram proves the all-parameter theorem, supplies source priority, closes
E1 by itself or constitutes candidate admission.

## Outcome and failure boundaries

On a successful later root invocation, stdout contains only a compact
reception summary with input pin, exact checked box populations and record
counts, the missing-family caveat and NOT_DECIDED admission status. On any
error, stderr contains a failure description and a nonzero exit; no output
file is created and no producer/helper is invoked.

Root must preserve the original scientific stdout, stderr, native exit,
runtime/closure records and the receiver's own exact command/results.
This semantic checker cannot authenticate execution provenance from a
self-asserted binding flag; independent root native/runtime reception is
a separate obligation. The same candidate reviewer, not this author,
decides whether the supplied finite evidence closes the gate finding.

