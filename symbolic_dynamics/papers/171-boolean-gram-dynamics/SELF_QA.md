# P171 author self-QA (historical Round 0)

**Result:** `PASS / ROUND0 FROZEN / HOLD_EXTERNAL`  
**Owner gate:** `GREEN_OWNER_THIN`

## Mathematical completeness

- [x] Literal Boolean-semiring multiplication and `Gamma_n(A)=AA^T` are
  explicit.
- [x] Row-intersection graph, loops, active vertices, and inactive isolates
  are defined.
- [x] The all-time `2^(t-1)` power identity is proved, not inferred from
  examples.
- [x] The exact per-source depth and `D<=1` convention are explicit.
- [x] The sharp global height has a uniform path-incidence witness.
- [x] Recurrent states are completely classified and proved all fixed.
- [x] Fixed count `Bell(n+1)` and zeta conversion are justified.
- [x] Every target, including targets outside the image, is covered by the
  inverse theorem.
- [x] The allowed clique set, loop/edge atoms, `c_H(S)`, and the
  inclusion--exclusion summand are evaluable from the target.
- [x] The image criterion is an if-and-only-if statement.

## Boundary audit

- [x] `n=1`: both states fixed, height zero.
- [x] zero source and zero target.
- [x] nonfixed sources whose first image has `D=0` or `D=1`.
- [x] symmetric target with an edge but missing endpoint loops has fibre zero.
- [x] isolated looped vertex needs a singleton atom.
- [x] empty columns are allowed and pad short covers.
- [x] repeated column supports are allowed; column positions remain labelled.
- [x] looped `K_{2,3}` at `n=5` separates compatibility from image
  feasibility.
- [x] sharp paths checked beyond the exhaustive range, through `n=64`.

## Owner and collision audit

- [x] Fitting's Boolean-power chain and strict-growth example are cited next
  to the forward mechanism.
- [x] classical intersection representation and edge clique cover owners are
  cited.
- [x] symmetric Boolean factorization `M=WW^T` is cited and subtracted.
- [x] Boolean powers, closure, Bell numbers, and inclusion--exclusion receive
  no contribution credit.
- [x] P127, P143, and P163 were compared at literal-map and proof-engine
  level in `SOURCE_VERIFICATION.md`.
- [x] No novelty or priority assertion appears; external lifecycle is
  `HOLD_EXTERNAL`.

## Exact artifact audit

- [x] Paper-local verifier is standalone and standard-library only.
- [x] Exhaustive source and full-codomain audit completed through `n=4`.
- [x] 594,955 assertions passed.
- [x] Two fresh verifier processes exactly match frozen stdout.
- [x] Canonical LaTeX/BibTeX build settled without diagnostics.
- [x] Two source-only cold builds are byte-identical to the canonical PDF.
- [x] Canonical and preserved Round-0 PDFs are byte-identical.
- [x] Three A4 pages rendered and visually inspected at 144 dpi.
- [x] All 25 font rows are embedded, subsetted, and Unicode-mapped.
- [x] PDF metadata identity fields are blank.
- [x] No encryption, forms, JavaScript, attachments, or raster images.
- [x] `SHA256SUMS` validates the frozen artifact set.

## Scope sentence

The note is mathematically complete for its declared exact package but
owner-thin after mandatory subtraction.  It is suitable only as an internal
Round-0 artifact unless a separate external owner audit changes the lifecycle.

Both later hostile manuscript reviews returned
`PROVABLE AS STATED / 0 Critical / 0 Major / 0 Minor`, and neither changed
the source or PDF.  The four live/round PDF paths are byte-identical.  Current
dual-review closure is recorded in `README.md`, `BUILD.md`,
`HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, and `IMPROVEMENT_LOG.md`;
external status remains `HOLD_EXTERNAL`.
