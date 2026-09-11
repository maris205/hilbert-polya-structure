# Complete author output schema: p211-author-kip-v1

Status: specified but **not produced**. `CANONICAL.json` must remain
absent until a separately authorized native initial production succeeds
and its complete actual stdout is adopted by the reviewed recorder.
No manually written placeholder and no old pilot conversion are allowed.

Serialization is exactly Python `json.dumps(result, sort_keys=True,
ensure_ascii=True, separators=(",", ":")) + "\n"`. All sets are first
converted to sorted lists. Boxes are in increasing $n$; states and
predecessors use lexicographic whole-function tuple order. Polynomial
terms use increasing integer exponent. Orbit lists use temporal order;
anchor blocks use increasing anchor order and their endpoints retain the
strict increasing order. No hash/set iteration controls output order.

## Top-level exact keys

- `schema`: string `p211-author-kip-v1`.
- `parameters`: the complete validated parameter object.
- `box_count`: integer 7.
- `total_states`: integer 2353.
- `assertions`: dictionary with exactly the seven parameter predicate keys.
- `checks`: sum of those seven integers.
- `boxes`: seven box objects, ordered by `n`.

## Box exact keys

- `n`, `carrier_size`: declared integer $n$ and complete carrier population.
- `state_records`: complete list of the state records described below.
- `image_count`, `fixed_count`, `recurrent_count`: complete graph counts,
  computed in this invocation, not copied from prior evidence.
- `maximum_height`, `theorem_height`: actual whole-carrier maximum and
  $0$ for $n=1$, otherwise $\lceil n/2\rceil$.
- `sharp_witness`: full function tuple as an integer list, using the
  explicit parity construction from the admitted theorem.
- `inverse_mass`: sum of all computed Laurent fibre counts.
- `assertions`: exactly the seven integer counts for this box.

## State-record exact keys

Every carrier map appears once, also serving as a potential target.

| Keys | Type and meaning |
|---|---|
| `source` | Full length-$n$ integer list |
| `kernel_endpoints`, `image_values`, `completed_image` | Increasing integer lists for $X,Y,A$ |
| `successor` | Literal full length-$n$ successor |
| `fixed`, `recurrent`, `in_image` | Booleans from the literal graph / compared image condition |
| `orbit` | All distinct whole states from the source up to, but excluding, the first repetition |
| `cycle_start` | Index in `orbit` of the first cyclic state |
| `cycle` | Complete cycle suffix of `orbit`; expected singleton by the checked theorem |
| `terminal`, `predicted_terminal` | Full observed terminal and ceiling onto $X\cap A$ |
| `height`, `predicted_height` | Literal entrance index and exact formula |
| `predecessors`, `decoded_predecessors` | Complete sorted lists of full source maps, including empty lists for zero fibres |
| `fibre_count`, `laurent_count` | Full observed multiplicity and coefficient formula |
| `laurent_coefficients` | Complete list `[integer exponent, positive integer coefficient]`; empty for off-image targets |
| `anchor_blocks` | Image target: ordered objects with exact keys `anchor` and `endpoints`; off-image target: null |
| `peeled_successor` | Full predicted image-state successor; null off-image |

Each anchor block's `endpoints` is the full even-length increasing list
of strict labels preceding that anchor; empty lists are retained. The
blocks cover every strict endpoint pair of the target.

## Acceptance relations, not aggregate-only evidence

The recorder/root schema check must bind all seven parameter boxes,
their complete distinct state lists, exact per-box population and
predicate census, and full predecessor/reverse-edge consistency. Native
byte comparison is a separate test: replay 1 versus immutable canonical,
replay 2 versus immutable canonical, and replay 1 versus replay 2.
Three successful comparisons do not replace semantic scope checks.

The fresh canonical is the complete actual stdout, not an extracted
summary, normalized reserialization, trimmed line or display transcript.
Its initial byte count/hash are intentionally unknown before production.
The scientific program never reads that file or adopts a new canonical.
