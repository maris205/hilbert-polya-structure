# P188 process-separated hostile Review A

## Verdict

`PROVABLE AS STATED / ZERO FINDINGS / ACCEPTED_NO_CHANGE / HOLD_EXTERNAL`

The frozen Round-0 theorem package survives this review.  No file in
`papers/188-self-cardinality-truncation/` was modified.  The author and this
reviewer ran in separate processes; that provenance is not a claim of
statistically independent error.

## Frozen input and control binding

| object | SHA-256 | disposition |
|---|---|---|
| `main.tex` | `f08712d1b1e43f707c1254ebf791724727e9387a5e0794dae3b5c40d4874ab39` | reviewed read-only |
| `main_round0_original.pdf` | `10b881a6200e075ed66514e8f4f8873c433383c8118c6037ad1ecd1d5bcb8bc3` | reviewed read-only |
| author `verify_p188.py` | `94f4aa2b656fcbf291106b63b0b22bf2fe3ca4f5d7ac6f0dfb3dc6693be9741d` | bound, not imported |
| author `CANONICAL.txt` | `ff0457f32e495f2405f494af83f461ad6bca310d25f04923fdb413c856d245ef` | bound; 13,283,014 assertions |
| `PROOF_PACKAGE.md` | `6307ac2d3f7eb9b82dff1118898225c910d3647e98bd823fc6ae7fc73c785235` | cross-checked against theorem text |
| `SOURCE_VERIFICATION.md` | `aa0ccf0a56fe33ddcd087d94f52177369da4bc19d920766c71fe67eddd20dc47` | owner status retained |
| reviewer `verify_review_a_p188.py` | `663c60581e78074de8ec7f6dbff8e46f0b2d54334eaa262fe851bc2f2d696ae8` | new, no author import |
| reviewer `CANONICAL.txt` | `989c6bf33f2e261ec83f79703ac82c29b6fb646fd989ea67eff901aa0e8c2d23` | two fresh replays required |

The six author-side rows are executable through `PINNED_INPUTS.sha256`.
The non-self-referential package manifest binds the reviewer-side files.

## Independent attack route

The author verifier uses integer bit masks and enumerates weak rank chains in
the forward direction.  This control uses actual `frozenset` carriers and
reconstructs the displayed fibre formula by a backward transfer through
nested interval capacities, starting from `(k_t,k_(t-1))`.  It imports no
author module.

Pointwise dynamics, extremizers, image layers, terminal basins, and one-step
fibres are exhausted through `n=16` (131,071 cumulative states).  Every-time,
every-target formulae are separately exhausted through `n=10` and through
time `n+2`, including 24,575 target/time comparisons.  The replay records
exactly **8,193,247** successful assertions.  These controls are finite
counterexample pressure, not a proof or novelty result.

## Hostile conclusions

- The identity `T^t(A)=A cap [k_(t-1)]` is correct already at `t=1` and the
  original-set rank, rather than the current-set rank, is used consistently
  thereafter.  The scalar chain is weakly decreasing and strictly decreases
  above the first missing-position statistic `rho(A)`.
- Endpoints are exactly the `n+1` initial segments.  Their basin sizes are
  `2^(n-r-1)` for `r<n` and one for `r=n`, with `n=0` and `n=1` reopened.
- Each nonfixed step deletes at least one element.  Equality in the global
  `n-1` bound forces `rho=0` and source size `n-1`, hence uniquely
  `{2,...,n}`.  Its displayed deletion chain has exactly `n-1` arrows.
- In the every-time fibre law, the outside interval contributes
  `C(n-k0,k0-k1)`, each nested interval contributes
  `C(k_(j-1)-k_j,k_j-k_(j+1))`, and the final interval is pinned to the
  labelled target.  Direct source counts agree at `t=0`, the dangerous
  specialization `t=1`, every intermediate tested time, and all stabilized
  times `t>=n-1`.
- The one-step nonempty-range condition is exactly
  `2 M(B) <= n+|B|`.  Layer summation gives `F_(n+2)`, while the empty target
  has `F_(n+1)` sources.  Every nonempty fibre is bounded by `F_n`, proving
  the empty target is the unique maximizer for `n>=2`; the `n=1` tie is stated
  correctly.
- Every time-slice fibre sum is `2^n`, and after the maximum tail only the
  terminal basin fibres remain.

The full derivation is in `PROOF_REDERIVATION.md`; citation, owner, and
historical-collision limits are in `SOURCE_OWNER_COLLISION_AUDIT.md`; cold
build and PDF evidence is in `BUILD_PDF_QA.md`.

## Finding ledger

| severity | open | closed | finding IDs |
|---|---:|---:|---|
| Critical | 0 | 0 | none |
| Major | 0 | 0 | none |
| Minor | 0 | 0 | none |

No manuscript repair is requested.  `DELTA.md` supplies the standalone
`PASS` / `ACCEPTED_NO_CHANGE` disposition.  A byte-identical Round-1 receipt
is permitted; any semantic, typographic, source, or control change reopens
this review.  Review B inherits no mathematical conclusion from this report.

## Replay

From repository root:

```bash
sha256sum -c docs/papers187_191_sequence/reviews/p188_a/PINNED_INPUTS.sha256
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers187_191_sequence/reviews/p188_a/verify_review_a_p188.py \
  | cmp - docs/papers187_191_sequence/reviews/p188_a/CANONICAL.txt
(cd docs/papers187_191_sequence/reviews/p188_a && sha256sum -c SHA256SUMS)
```

Acceptance requires three zero exit codes.  The separate owner gate remains
`OWNER_AMBER / HOLD_EXTERNAL`.
