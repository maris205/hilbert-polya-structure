# Independent Paper20 expanded-source review (R1)

Date: 2026-08-22 (UTC)

Scope: read-only review of the expanded manuscript source, its frozen theorem
contract, citations, labels, permissions, and source-revision bookkeeping.
No compilation, build, experiment, transport access, or author-file edit was
performed.  This reviewer artifact is provenance-only and is excluded from
the ten-file author aggregate.

## Objects read and identity check

The current source objects were hashed independently:

| object | bytes/LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 58,944 / 1,552 | `67b1bf3d18fdc01be1084d969dd273bbaa1e7fe5a1677eecaa758b64ea9efbb1` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |

The source is strict-text clean (LF-only, no BOM/CR/NUL), and the manuscript
has balanced environments/braces, 60 unique labels, no missing references,
and no undefined citation keys.  The seven cited keys are present in the
locked bibliography; citation roles remain contextual and no priority claim
is introduced.

## Mathematical review

The expanded proof is substantive and remains within the frozen theorem.  In
particular:

* The triangular inverse and block Jacobian use
  `Q=H_V(q)`, `P=H_W(\widehat p)` and
  `DF=[[I+PQ,P],[Q,I]]`; the displayed symplectic block multiplication is
  correct.
* The phase ledger now distinguishes the carried old vector `\bar v` from
  the new `v^+=A_g u`.  The S-carry inequalities are applied to `\bar v`,
  while the T inequalities use `v^+`; substituting `v^+` in the former is
  explicitly identified as a zero-identity error.  The base case and the
  simultaneous old-term induction use the correct indexing
  `v_n=A_g u_{n-1}` for `n>=1`.
* The selector gaps, half-open cone, ratio map, endpoint margins, and
  complete-step matrix `C_g=B_gA_g` are algebraically consistent.  The text
  does not confuse the off-diagonal half-step matrix with the complete-step
  dynamical matrix.
* Positive-semiring/no-cancellation, `C_g-A_g` visibility, Perron pairings,
  scalar recurrence, and the g=5 audit are consistent with the stated
  characteristic-zero and positive-coefficient hypotheses.

The anti-claims and STOP conditions continue to exclude arbitrary supports or
words, generic Newton-fan statements, entropy/period/trace/centralizer claims,
positive characteristic, and contextual citations as proof.  No hidden
external or experimental authority was found.

## Final binding and disposition

The prior bookkeeping blocker was mechanically repaired before this fresh
review.  `BUILD_METADATA_R1.json` now binds the current main identity and has
SHA-256 `07df9ae892159220ded19f792a568cb3a24f1fe5d7139febd915fea78d97cdce`
(5,002 bytes/LF1); `SOURCE_REVISION_RECEIPT_R1.json` binds that metadata and
the same current main identity, with SHA-256
`313460b46affade4a61522e86799db9789222e637e497aa2ad8fafb991fcc4a6`
(5,508 bytes/LF1).  Both JSON objects and the frozen source lock pass strict
recursive-key canonicalization, exact one-LF, self-null, and byte/hash
round-trip checks.  The receipt's transition `after` object, metadata hash,
and source-file bytes/LF all agree with the current files.

The seven-byte source correction only fixes the ledger sentence to identify
the first and fourth displayed margins as face comparisons; it does not alter
the theorem, phase equations, or proof dependencies.  The page count remains
future-null until an authorized build and is not a source-review blocker.

PAPER_SOURCE_R1_EXPANDED_PASS
