# P190 process-separated Hostile Review A

## Verdict

**PASS_DELTA_ACCEPTED.**  Round 1 repairs both Round-0 Minor presentation
findings and changes no theorem, proof, citation, or lifecycle statement.
The formal package survived the process-separated proof reconstruction and
2,615,881 exact reviewer assertions with no mathematical counterexample.
Final counts are `Critical 0 / Major 0 / Minor 0`.

External status is unchanged: `OWNER_AMBER / HOLD_EXTERNAL`.  This review is
not a novelty, priority, ownership, or release determination.

## Process and frozen object

The reviewer did not author P190, did not import its verifier, and did not
edit any file in `papers/190-brandt-sandwich-erosion/`.  Seven required
Round-0/Round-1 inputs are pinned in `PINNED_INPUTS.sha256`:

| input | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66` |
| `main_round1.pdf` | `81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d` |
| Round-1 `main.tex` | `73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300` |
| `code/verify_p190.py` | `99bccb56fd9324409f7ee23742dbceda04c76cb887cac7bd8553a1ee84b4f081` |
| `code/CANONICAL.txt` | `9652d76deed795b561f9ceddd28ff4db1f296215f920d97ad4014b3ca75e6b2f` |
| `PROOF_PACKAGE.md` | `01ab488f347c91c41650c860ac8e396b6054bcb749e98efa0a83228cbffa6628` |
| `SOURCE_VERIFICATION.md` | `e873ff99bac17675c124b16a5b5107266e9736f12493bc7f317a5d7de768285c` |

The reviewer representation uses integers `0,...,n^2`, base-`q` serials for
whole cyclic words, literal three-factor Brandt multiplication, and directed
walk tables.  The author instead uses tuples from Cartesian products and a
different matrix/path implementation.  Two fresh author-control processes
matched the pinned author canonical; that observation is package QA, not a
substitute for the reviewer control.

## Finding register

### Critical — 0

No Critical finding.

### Major — 0

No Major finding.

### Minor — 0

No open Minor finding.

## Historical Round-0 findings and disposition

#### P190-A-MI-01 — Eq. (11) has an empty leading subscript field

In the bound Round-0 `main.tex` at line 231, the displayed factor was

```tex
(A^{h_j})_{,y_{i_j}^*,\,y_{i_{j+1}}}
```

and the frozen Round-0 PDF visibly renders a comma before the first index on
page 3.
With rows equal to current source letters and columns equal to next source
letters, the proved factor is

```tex
(A^{h_j})_{y_{i_j}^*,\,y_{i_{j+1}}}.
```

The prose on lines 223–240, the proof package, and the exact control all use
that intended two-index entry.  Thus this is a central-formula notation
defect, not an orientation counterexample.  **Round-1 disposition:
ACCEPTED.**  The leading comma is absent from source and PDF; the intended
two-index entry is unchanged.

#### P190-A-MI-02 — the CRediT heading renders `CRediT..`

The bound Round-0 `main.tex` at line 362 used `\paragraph{CRediT.}`.  In
`amsart`, the terminal
capital before that period causes the paragraph-heading punctuation logic to
append another full stop.  The page-4 Round-0 PDF and its text layer both show
`CRediT.. Anonymous author(s)`.  **Round-1 disposition: ACCEPTED.**  The
source now uses `\paragraph{CRediT}`, and the cold-built PDF shows exactly one
full stop.

## Hostile mathematical attack matrix

| claim surface | reviewer attack | result |
|---|---|---|
| local identity | Literal matrix-unit multiplication computes `(uv)u` for every ordered pair, then compares with the inverse-successor filter | Pass |
| all-time formula | Every state in 28 boxes, times `0..2m+3`, including empty products and long post-height times | Pass |
| recurrence | General orbit detection, without assuming eventual fixedness | All observed periods are one |
| odd/even sharpness | Exact maximum-tail census; explicit count of one-bad-edge words | Pass; none for even `m`, witnesses for odd `m>=3`, `n>=2` |
| `n=1` | Every word through `m=12` | Pass; maximum `max(0,m-1)` |
| `m=1,2` | Every source and every target for `n=1,...,5` | Pass, including empty off-diagonal fibres |
| trace orientation | Directed row-to-column products versus literal fibres; entry-level off-diagonal anchor test rejects the reversed ordered pair | Pass |
| gap product | Every target in all 28 boxes, including all-zero and zero-fibre targets | Pass with the intended two-index formula |
| zero spectrum | Exact rational ranks of `A-I` and `A+I`, symmetry, exceptional two-dimensional block, and traces through exponent 12 for `n=1,...,5` | Pass |
| image iff | Every target in all boxes | Pass |
| fibre mass | Sum of independently predicted target fibres and literal source counts | Both equal `(n^2+1)^m` |

The reviewer run covers 28 boxes: `n=1,m=1..12`; `n=2,m=1..7`;
`n=3,m=1..4`; `n=4,m=1..3`; and `n=5,m=1..2`.  Its canonical result is
2,615,881 exact assertions, zero formal counterexamples, and no open finding.
The proof route and its uniform quantifiers are recorded in
`PROOF_REDERIVATION.md`.

## Artifact and source result

- A Round-1 source-only cold build from only `main.tex` and `references.bib`
  produced a 4-page, 383,748-byte A4 PDF with SHA-256
  `81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d`,
  byte-identical to the frozen Round-1 PDF.
- The settled log has no warning, unresolved reference/citation, bad box,
  overfull/underfull box, or fatal error.
- All 29 font rows are embedded, subsetted, and Unicode-mapped; metadata
  identity fields are blank; there is no encryption, form, JavaScript, or
  metadata stream.
- All four Round-1 pages, with focused inspection of repaired pages 3 and 4,
  have no clipping, overlap, corruption, or unintended blank page.  Both
  Round-0 defects are absent.
- The exact cite-key and bibliography-key sets agree (five each); bounded
  primary-record checks found no source mismatch.  Direct ownership remains
  amber for the reasons in `OWNER_COLLISION_AUDIT.md`.

## Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers187_191_sequence/reviews/p190_a/verify_p190_review_a.py
```

Two fresh processes must match `CANONICAL.txt` byte for byte.  `SHA256SUMS`
binds every review artifact except itself and is intentionally
non-self-referential.
