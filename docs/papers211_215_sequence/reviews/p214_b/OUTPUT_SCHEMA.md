# P214 Review B proposed output schema

Status: `SOURCE_ONLY_NOT_EXECUTED`. A successful future run emits ASCII/UTF-8
text with LF endings in this exact order:

1. One `P214_B_FORWARD_TRIANGULAR_V1` header.
2. For each carrier in q-major order q=2,3,4 and m=2,3,4, one `STATE` row for
   every state ID, then one `TARGET` row for every target ID, then one
   `CARRIER` row.
3. One final `PASS` row.

There are prospectively 5,271 `STATE`, 5,271 `TARGET`, nine `CARRIER`, one
header and one final row, for 10,553 lines. This is a source-derived envelope,
not an observed output. State IDs encode `(x,y)` as
`x_index * ideal_size + y_index`. Every target row retains both the complete
literal predecessor list and the independently derived coefficient-triangular
list; `-` denotes an empty list. The two lists must agree in order and
multiplicity. No digest substitutes for a source list.

The final row is emitted only after all assertions and the exact 5,271-state,
nine-carrier totals pass. Any assertion or runtime exception is failure even
if partial stdout exists. A future accepted run requires exit zero, nonempty
complete stdout, empty stderr and the final row. It must be captured without
normalization and later strict replays must compare full raw bytes.
