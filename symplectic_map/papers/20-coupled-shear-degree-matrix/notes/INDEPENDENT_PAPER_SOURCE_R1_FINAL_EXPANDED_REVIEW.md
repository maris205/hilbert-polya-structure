# Independent final expanded-source review (Paper20 R1)

Date: 2026-08-22 UTC  
Review mode: read-only; no compile, build, CAS, experiment, transport, or
author-source edit. This reviewer-owned note is excluded from the frozen
ten-file author aggregate.

## Final identity and repair binding

The final frozen source objects were independently read and hashed:

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 58,944 / 1,552 | `67b1bf3d18fdc01be1084d969dd273bbaa1e7fe5a1677eecaa758b64ea9efbb1` |
| `paper/BUILD_METADATA_R1.json` | 5,002 / 1 | `07df9ae892159220ded19f792a568cb3a24f1fe5d7139febd915fea78d97cdce` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 5,508 / 1 | `313460b46affade4a61522e86799db9789222e637e497aa2ad8fafb991fcc4a6` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |

The earlier expanded-source receipt was blocked because it bound the pre-repair
main identity. The authorized minimal repair changed only the ledger wording
(`first, fourth, and fifth` → `first and fourth` face margins); the final
receipt and metadata now bind the resulting 58,944-byte source. Their
`source_files.main_tex`, receipt transition `after`, byte/LF fields, and
metadata digest cross-check exactly. The receipt's `build_metadata_r1` hash
also matches the independently hashed metadata object. This is the repair
receipt for the final source identity; no unrecorded source edit was observed.

All three JSON authority objects are strict canonical JSON (recursive Unicode
key order, compact separators, UTF-8, exactly one terminal LF), with no CR,
BOM, NUL, duplicate keys, NaN/Inf, or self-identity insertion. Metadata and
receipt self fields are null as required; page fields remain future-null until
an authorized build.

## Source and theorem checks

The final `main.tex` is text-clean and structurally balanced: 60 labels are
unique; all 54 internal references resolve; all seven cited keys are present
in the locked bibliography; marker tokens (`TODO`, `TBD`, `VERIFY`, `FIXME`,
and `??`) are absent; all begin/end environments and braces balance; and the
obsolete `eq:ratiomap` label is absent. No forbidden build/results/transport
path is introduced. The frozen source lock remains the theorem, citation,
anti-claim, and permission authority.

The mathematical expansion remains faithful to that lock:

* The explicit triangular inverses and block Jacobian use symmetric Hessians,
  the correct phase order, and the symplectic identity
  \(DF^{\\mathsf T}JDF=J\).
* The support ledger distinguishes the carried old vector \\(\\bar v\\) from the
  new S-phase vector \\(v^+=A_gu\\). S-carry inequalities use
  \\(\\bar v=v_n=A_gu_{n-1}\\), while T selectors use
  \\(v^+=v_{n+1}=A_gu_n\\); no self-comparison is used.
* The n=0 base gaps, simultaneous old-term induction, half-open cone, ratio
  endpoint margins, and complete-step recurrence
  \\(v_{n+1}=A_gu_n,\\ u_{n+1}=C_gu_n\\) are correctly indexed.
* Positive-semiring coefficient paths in characteristic zero rule out leading
  cancellation. \\(C_g-A_g>0\\) gives coordinate visibility, and the explicit
  Perron pairings and scalar recurrence justify
  \\(\\lambda_1=\\rho(C_g)=(\\sqrt g+1)^2\\).

The fixed-family, \\(g\\ge5\\), algebraic-degree claim is not broadened to
arbitrary potentials/words, generic Newton fans, entropy, periods, traces,
centralizers, torus translates, positive characteristic, priority, or
experimental/CAS evidence. Citations remain contextual and are not used as
proof.

## Verdict

No remaining source, theorem, label, citation, permission, phase-indexing,
block-Jacobian, no-cancellation, or provenance blocker was found. The final
source is eligible for the next separately authorized build review; this
artifact does not authorize a build or publication.

PAPER_SOURCE_R1_EXPANDED_PASS
