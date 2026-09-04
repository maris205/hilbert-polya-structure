# P191 process-separated hostile Review A

## Verdict

`PROVABLE AS STATED / ZERO FINDINGS / ACCEPTED_NO_CHANGE / HOLD_EXTERNAL`

The frozen Round-0 theorem package survives the mathematical, source-boundary,
collision, build, and artifact attacks in this package.  No file in
`papers/191-prefix-divisibility-cuts/` was modified.  The separation is a
process separation between author and reviewer; it is not a claim that their
errors are statistically independent.

## Frozen input and control binding

| object | SHA-256 | disposition |
|---|---|---|
| `main.tex` | `bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84` | reviewed read-only |
| `main_round0_original.pdf` | `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b` | reviewed read-only |
| author `code/verify.py` | `70efeb7bdb522b501d64775d3ad1c300d70d9ffc83d94d65ff7924e633c59d50` | bound, not imported |
| author `code/CANONICAL.txt` | `c4643a6639ddf269dee59c97acc53aee504d081a0279d0bbe2898183f674373c` | bound; 3,408,240 assertions |
| `PROOF_PACKAGE.md` | `f89ab89d2f9fa2f82eb6482129f4803870c3b3240d7a9eb8b31bd8579511d9ef` | cross-checked against theorem text |
| `SOURCE_VERIFICATION.md` | `71e6ed195bc75584e071ff5f27975ab756eb66287acd99299fbeea596c9a1c70` | owner status retained |
| reviewer `verify_review_a_p191.py` | `c7c35da924d5e6abed1d908b0f9f23c230200ef8578600cb7ffd9c7445acb01e` | new, no author import |
| reviewer `CANONICAL.txt` | `033047bf9296586e3a8690332a1f204086db73f5455d9c0205967e9895c1c5d1` | two fresh replays required |

`PINNED_INPUTS.sha256` is the executable six-row author-input receipt.  The
package-level `SHA256SUMS` binds all reviewer artifacts and intentionally does
not list itself.

## Independent attack route

The author verifier uses tuples of parts and forward orbit tracing.  The
reviewer instead packs each composition as an internal-cut bit mask and never
reconstructs the author carrier.  The literal map is applied directly to cuts:
an old cut at prefix `s` survives exactly when its incoming gap divides `s`.
Recurrence and depth are recovered independently by indegree peeling and
reverse breadth-first search.

The inverse theorem is reopened twice.  First, a global no-skipped-target
dynamic program counts all source masks whose retained cuts equal a prescribed
target mask.  Second, the same fibre is factored through interval automata
between consecutive mandatory target cuts.  Only after both reviewer-owned
counts agree target by target are they compared with the literal indegrees.

The control exhausts every carrier `Comp_N` for `1<=N<=18`, totalling 262,143
source states and the same number of transitions.  It records exactly
**920,748** successful assertions.  This bounded computation is counterexample
pressure only; the all-parameter proof is the reason for the verdict, and the
control supplies neither proof nor novelty evidence.

## Hostile conclusions

- The cut-set rule is genuinely monotone: the image cut mask is always a
  subset of the source mask, and the first cut, when present, is forced to
  survive because its incoming part equals its endpoint.
- Indegree peeling leaves exactly the fixed states.  No nontrivial cycle
  survives the coarsening order.
- The fixed-state criterion `a_i | s_i` and the recurrence
  `A(v)=sum_{u<v, v-u|v} A(u)` agree with complete exhaustion for every
  `N<=18`.
- The sharp clock is exactly `0` for `N<=3` and exactly `N-3` for `N>=4`.
  The unique deepest source is the mask of `(1,2,1^(N-3))`, and its entire
  orbit `((1,2+t,1^(N-3-t)))_t` is checked pointwise.
- Every labelled target fibre is recovered both by the global no-skip DP and
  by the interval product.  Each target is in the image exactly when those
  counts are positive.
- The paper's control table rows for `N=4,8,12,15,18` match the reviewer's
  direct counts of state total, image size, fixed count, sharp tail, deepest
  multiplicity, and maximum fibre.
- Global and factorized fibre masses both sum to `2^(N-1)` only after the
  targetwise equalities have already passed.

The full derivation and counterexample ledger are in
`PROOF_REDERIVATION.md`; sources and historical collisions are treated in
`SOURCE_OWNER_COLLISION_AUDIT.md`; cold builds and PDF checks are in
`BUILD_PDF_QA.md`.

## Finding ledger

| severity | open | closed | finding IDs |
|---|---:|---:|---|
| Critical | 0 | 0 | none |
| Major | 0 | 0 | none |
| Minor | 0 | 0 | none |

No repair is requested.  `DELTA.md` is a standalone `PASS` /
`ACCEPTED_NO_CHANGE` receipt.  A byte-identical Round-1 lifecycle receipt is
permitted; any theorem, citation, source, or control change reopens this
review.  Review B must independently reopen every kill switch.

## Replay

From repository root:

```bash
sha256sum -c docs/papers187_191_sequence/reviews/p191_a/PINNED_INPUTS.sha256
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers187_191_sequence/reviews/p191_a/verify_review_a_p191.py \
  | cmp - docs/papers187_191_sequence/reviews/p191_a/CANONICAL.txt
(cd docs/papers187_191_sequence/reviews/p191_a && sha256sum -c SHA256SUMS)
```

Acceptance requires three zero exit codes.  External circulation remains
blocked by `OWNER_AMBER / HOLD_EXTERNAL`.
