# P193 author handoff — Round 0

**Decision:** `PASS_INTERNAL / ROUND0_AUTHOR_FREEZE`  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`

## Mathematical boundary audit

- The carrier is exactly `S_n`, with one-line notation and `n>=1`.
- Both nominations are evaluated from the old state; every mutual pair is
  exchanged simultaneously.
- Active-pair disjointness is proved through exact block classification, not
  assumed from the matching story.
- The proof that an extra active pair creates a sum cut accounts for all
  values below its right endpoint.
- Direct-sum component count strictly increases only off fixed states; the
  identity is separately identified as the unique fixed state.
- Recursive height is well-founded by size and uses maximum, not sum, across
  simultaneously evolving direct-sum factors.
- The maximum-tail proof covers `n=1`; the deepest recurrence has base
  `d_1=1` and gives `(n-1)!`.
- `A_t` and `B_t` are ordinary formal series.  `A_t=1/(1-B_t)` uses ordered
  component sequences, and the two factors of `x` in `x^2 A_t B_t'` have
  distinct meanings.
- The indecomposable-parent lemma proves both directions and counts positions
  in the last suffix component.
- The fibre theorem includes empty fibres, singleton groups, and the identity
  boundary.
- Unique maximum fibre is derived from the exponent budget; it does not rely
  on a false claim that `c<=2^(c-1)` has equality only at `c=1`.
- Fibre mass is checked only after every target formula is checked pointwise.

## Exact-control audit

- Complete enumeration passes through `S_9`.
- The script uses only the Python standard library and imports no prior-paper
  or scouting implementation.
- Transition serialization is deterministic and independent of Python hash
  order.
- The recorded transition digest is
  `28eedb5ba198c502e491d2788354ab2fe6de9785af1852bc3b4dd00f69f33761`.
- Finite controls are not described as proof or novelty evidence.

## Source and collision audit

- The matching wrapper and direct-sum decomposition are explicitly
  zero-credit.
- P105, P122, P155, P156, and P181 are compared by literal update and proof
  engine rather than title alone.
- The P181 separation includes an explicit disagreement on `132` and the
  recurrent-structure difference.
- No external owner search is claimed in Round 0.
- `OWNER_AMBER/HOLD_EXTERNAL` appears in the abstract, conclusion, and package
  ledgers.
- No author identity, affiliation, grant, or self-identifying repository URL
  appears in the manuscript.

## Build audit

- The settled build is five A4 pages and has no warning, bad box, unresolved
  reference, unresolved citation, or fatal error.
- A repeated deterministic pass is byte-identical at PDF SHA-256
  `e41e171c8f412cf93aae9510052ed0d8ad165125be1bd4c04133f1b410048267`.
- All 29 font rows are embedded, subsetted, and Unicode mapped.
- PDF metadata fields are blank; the file is unencrypted and contains no
  form, JavaScript, or metadata stream.
- All five rasterized pages were inspected; no clipping, overlap, malformed
  display, missing glyph, broken table, or unintended blank page was found.
- Extracted text contains no unresolved marker or identifying author data.

Round 0 is complete.  This is an author-side internal freeze, not hostile
review, owner clearance, or permission to circulate externally.
