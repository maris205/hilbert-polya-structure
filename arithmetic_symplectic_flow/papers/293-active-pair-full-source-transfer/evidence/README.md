# Evidence — full-source transfer and cylinder-trace mismatch

Audit ID: `ASFS-AUDIT-20260920-AFT01`.
Candidate ID: `ANG-20260920-APR01` (unchanged 288/289/291).
Status: `OWNED TRANSFER; COFINAL CYLINDER TRACE MISMATCH — SCOPED ADVANCE / STOP`.

## Frozen inputs and byte-level bindings

The original [analytic card](../candidate-card.md), before its appended
outcome, has SHA-256

    ebd6c1c2a68ac1af187c93ea71e7c889ceb206d59c1b5b3e35bf1f372791c868

Its full-source function space, inverse-branch family, conditional-Haar
observations, ordinary finite trace, formal determinant and controls
were fixed before proof. The dynamical rule, source, joint measure,
time action and packet/repetition ledger are unchanged. The exact
read-only dependencies are:

| Input | SHA-256 |
|---|---|
| [288 card](../../288-active-pair-residue-flow/candidate-card.md) | cb48100913138d23d66b89e91c0502e5920337cc0c9969f31d33d9cf441fdc78 |
| [288 paper](../../288-active-pair-residue-flow/paper.md) | b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8 |
| [291 card](../../291-active-pair-orbit-zeta/candidate-card.md) | 84e7abac8515301102e7df48f7ed80bcc57ef0a6f14fe4a3ee6ed10f0674ed35 |
| [291 paper](../../291-active-pair-orbit-zeta/paper.md) | 7dd25c66e30d80a454f0a375c29caacf993280fa85231e82ec5358054ad3f366 |

The final [manuscript](../paper.md) SHA-256 is

    1a089d81b80d9a3957d277e6c7076a2e5ad7aaac326d95bbb468f35ce966d074

No external theorem or literature expansion is used for the new
operator/trace proofs. Prior scalar continuation is neither reproved
nor used to obtain a trace. Definition comparisons in the
[separate scout record](scout-record.md) are not theorem dependencies.

## Exact reproduction method and limits

1. Substitute the unchanged inverse branches into the frozen L_s.
   Bound output root v by 4R-5 and note integer-affine preservation
   of seed level M. Apply the defining inductive-limit property.
2. Change variables with inverse IMAGE factor 1/b to obtain the
   precise measure-duality factor b^(1-s). No trace follows from it.
3. Use root/residue indicator functions for each finite compression.
   Sum the original second differences around a closed root path:
   every nonnegative w(b_i)+j_i must vanish, leaving a constant prime
   root and the zero-digit inverse matrix B_p.
4. Count fixed classes of B_p^r on (Z/MZ)². For A=B_p^r-I,
   use the finite cokernel Z²/(A Z²+M Z²), lattice index and
   adjugate to prove the bound and equality when |det A| divides M.
   This proves cofinal stabilization, not an extrapolation from samples.
5. Compute r=1 directly. At r=2 add (p+1) times the second row
   to the first; obtain y=-x and (2p-1)x=0. Compare r=2 with
   the unchanged unit-weight orbit ledger, already at p=2.
6. Check the displayed mod-3/mod-9 kernels and their reduction.
   Use injectivity of nonzero integer multiplication on Z_hat for
   the full periodic equation; do not infer extra actual packets.
7. Derive the finite determinant identity by cofactor differentiation
   and formal series. Apply it at M=1 and compare the separate M²
   normalization control. Neither control repairs the stopped trace.

R>=2, M>=1 and r>=1 are arbitrary exact integers in these proofs.
The limit statement fixes R,r and refines M cofinally by divisibility;
it is not a simultaneous infinite-root/iterate limit. The mod-3/mod-9
examples are exact algebra, not a numerical orbit census. No scientific
run, precision parameter, target fitting, spectral calculation or
large-root determinant limit was performed. There is no scientific
output file beyond the Markdown proofs and bounded review record.

## Review and ownership boundary

Root owns integration and every file except
[evidence/independent-review.md](independent-review.md), owned by the
native reviewer. ARS supplies raw-card, manuscript-comparison and
final adverse checkpoints. Shared-model/context checking is not
external peer review, formal verification or independent-error evidence.

The final internal review SHA-256 is

    922785e5767851f4734946c358630497dc629e079e507650627849996bfeaa6b

The reviewer sent its raw transfer/kernel/control findings before any
manuscript access. An auxiliary checked the raw congruence questions
before that checkpoint completed. The reviewer then fully read initial
manuscript fc0aa6bb76991b59c7478f0a6271eaf3a89b675e9a3d2d5f4e4ef7e198d824ce
and updated manuscript 9610e27113a200cc79c12619faddebb271ae7076582c21b284a4b53992882e57,
which added an explicit forward mod-2 non-descent example. One final
terminology correction clarified that determinant/product have constant
term one while their formal logarithms have constant term zero; the
reviewer checked that changed passage at the final manuscript hash.
The measure-duality identity was checked at manuscript stage, not
retroactively represented as a blind raw finding. The final adverse
checkpoint has no outstanding blocking issue within its stated scope.

The trace mismatch does not destroy the legitimate full-source operator,
the prior ordinary scalar zeta, or the possibility of a different
properly proved representation. In particular the M=1 root-constant
space is valid, but neither cofinal nor supplied with a global analytic
completion here. Naturalness stays OPEN; no state, clock, packet,
repetition or post-hoc weight was changed to force agreement.

Only this new Markdown package and concise registry entries are written.
Old packages/mirrors unchanged; 241/242 paused; programme active.
Classical A0/A1/A2 NOT APPLICABLE; formal coordinates UNASSIGNED;
Route B NOT INVOKED. No quantum model, PDF/LaTeX, commit, upload
or publication is part of this audit.

## Verification receipt — 2026-09-20

Root's read-only Python check covered all seven package Markdown files
and the two new registry entries. Result: **40 package-local links +
2 new registry links resolved; 7 primary identity/status records
matched; 7 hash locks matched; 0 issues**. All new files decoded as
UTF-8, ended in a newline, contained no NUL/tab, and had trailing
spaces of only zero or two characters.

The primary records were paper.md, candidate-card.md, claim-ledger.md,
package README.md, evidence/README.md and the current entries of both
root registries. Each matched ANG-20260920-APR01,
ASFS-AUDIT-20260920-AFT01 and the exact final status above. Inline
relative Markdown targets were resolved against their file's parent.

The seven byte locks are the original card prefix, final manuscript,
final review and the four read-only 288/291 dependencies listed above.
The card prefix was obtained by splitting at the first newline followed
by `## Appended audit outcome`; it still matches the original freeze.
No old dependency bytes were changed.

| Final artifact | Lines | SHA-256 |
|---|---:|---|
| paper.md | 299 | 1a089d81b80d9a3957d277e6c7076a2e5ad7aaac326d95bbb468f35ce966d074 |
| candidate-card.md with outcome | 198 | 33a72762ccbe30ea8b82ee5b29e0e4e7d3d24098d61b03302468c6384709e0f9 |
| evidence/independent-review.md | 155 | 922785e5767851f4734946c358630497dc629e079e507650627849996bfeaa6b |

Exact whitespace command, from the workspace root:

```sh
git diff --check -- readme.md papers/README.md papers/293-active-pair-full-source-transfer
```

Exit zero, no output. The Python check explicitly covered untracked
Markdown, unlike Git diff alone. It used pathlib byte reads, UTF-8
decoding, relative-target existence, identity/status string checks and
hashlib SHA-256 comparisons; it wrote no file. Session results are
recorded here, with no standalone validator or scientific output.
After this receipt only its changed content/whitespace and the scoped
Git diff were checked. Integrity checks are not a mathematical proof,
Route evaluation or external peer review.
