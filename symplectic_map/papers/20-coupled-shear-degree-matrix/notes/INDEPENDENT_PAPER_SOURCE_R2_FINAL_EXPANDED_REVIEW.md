# Independent Paper20 source R2 audit (final expanded manuscript)

Date: 2026-08-22 UTC  
Review ID: `PAPER_SOURCE_R2_FINAL_EXPANDED_AUDITOR_2026_08_22`

This is an independent, read-only audit of the author-stopped expanded source.
I read `paper/main.tex`, `paper/BUILD_METADATA_R1.json`,
`paper/SOURCE_REVISION_RECEIPT_R1.json`, `experiments/source_lock.json`, and
`paper/PAPER_PLAN.md` to EOF.  No compilation, build, BibTeX run, CAS or
symbolic execution, experiment, transport, upload, or author-source edit was
performed.  This reviewer note is the only write made for this pass and is
outside the frozen source preimage.

## Identity and authority checks

The requested live identities and the cross-file bindings agree exactly:

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 58,944 / 1,552 | `67b1bf3d18fdc01be1084d969dd273bbaa1e7fe5a1677eecaa758b64ea9efbb1` |
| `paper/BUILD_METADATA_R1.json` | 5,002 / 1 | `07df9ae892159220ded19f792a568cb3a24f1fe5d7139febd915fea78d97cdce` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 5,508 / 1 | `313460b46affade4a61522e86799db9789222e637e497aa2ad8fafb991fcc4a6` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |

The metadata and revision receipt each bind every listed live source row; the
receipt's `build_metadata_r1` row matches the independently hashed metadata,
and its `source_identity_transition.main_tex.after` matches the live expanded
source.  The predecessor hash is recorded as the compact R0 source, with only
`main.tex` changing in the transition.  All three JSON authority objects are
UTF-8, LF-only, one-terminal-LF, duplicate-key-free, finite, recursively
Unicode-key-sorted canonical JSON with byte-exact round trips.  Their
self-identity fields are null/excluded as required.  The frozen lock's ten-file
allowlist still rehashes to 45,416 bytes, 873 LF, aggregate SHA
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.

The theorem binding, source-lock SHA, plan SHA, revision scope, and citation
set agree between the plan, metadata, receipt, and lock.  The existing R0 PDF
and auxiliary files are historical predecessor outputs explicitly recorded in
the R1 predecessor fields; the R1 planned build remains `NOT_RUN` with null
artifact/page fields, and no new build was performed in this audit.

## Source structure, labels, and citations

`main.tex` has 60 unique labels, 54 internal `ref`/`eqref` targets, and zero
missing or duplicate targets (including the repaired phase-ledger labels).
The eight explicit tags are unique.  All 102 `begin`/`end` environments and
TeX braces balance.  The seven cited bibliography keys are unique and all
resolve; citation use is limited to the locked planar, higher-dimensional,
spectral-terminology, valuation-context, and neighboring four-dimensional
hyperbolicity roles.  No citation is promoted to proof or priority evidence,
and no draft-marker token (`TODO`, `TBD`, `VERIFY`, `FIXME`, `??`, or `[?]`) is
present.

The final phase-ledger wording is consistent with its five aligned ledger
rows: the first and fourth rows are face comparisons, while the other three
rows compare selected gradient terms with carried coordinates.  The equations
themselves separately display both S-carry inequalities, so no carried term is
silently dropped.  The no-cancellation sentence's informal phrase “monomial
selected in `eq:phase`” is understood as the selected leading terms of that
degree recurrence and does not alter the stated proof.

## Mathematical audit against L1--L7

* **L1 (canonical inverse/symplecticity):** The triangular inverse formulas
  have the correct phase order.  The pullback computation, symmetric Hessian
  cancellation, block Jacobians, composite (DF_g^{\mathsf T}JDF_g=J), and
  determinant check are consistent with the stated coordinate order.
* **L2 (S selector):** The finite derivative support is complete.  On
  (1\le u_2/u_1<(g-2)/2), (u_1+2u_2<(g-1)u_1), the second row is
  (2u_1+u_2), and the old (p)-coordinates are compared separately.
* **L3 (T selector):** With (v=A_gu), the first row is (v_1+2v_2);
  (v_2/v_1=(2+u_2/u_1)/(g-1)\ge3/(g-1)>2/(g-2)) for (g\ge5), so the
  (p_2^g) term strictly beats (2v_1+v_2) and the carried (q_2) term.
* **L4 (two-stage cone):** The complete-step ratio map
  (f_g(r)=(g-1)(2+r)/(g+3+2r)) is increasing, has the stated lower and
  upper endpoint margins, preserves the half-open cone, and gives
  (C_gu>u).  The proof keeps the exact phase-return equality
  (v_{n+1}=A_gu_n), rather than imposing a false strict cross-phase cone.
* **L5 (old terms/no cancellation):** The (n=0) gaps and the simultaneous
  induction track every carried coordinate in both phases.  Nonnegative
  integer coefficient paths and characteristic zero make selected leading
  pieces nonzero; strict face gaps isolate them without a uniqueness claim.
* **L6 (recurrence/visibility):** The induction closes with
  (v_{n+1}=A_gu_n), (u_{n+1}=C_gu_n).  The entrywise-positive
  (C_g-A_g), (u_{n,2}>u_{n,1}) for (n\ge1), and final (p)-phase
  identification prove that (q_2) observes the total degree.
* **L7 (Perron):** Trace (2g+2), determinant ((g-1)^2), discriminant
  (16g), the explicit positive right/left eigenvectors, and their nonzero
  pairings give \\(\rho(C_g)=(\sqrt g+1)^2\\) and the degree limit.

The (g=5) hand audit, scalar recurrence, strict comparison with
`(g-1)^2`, and support-connectivity argument agree with the frozen theorem.
The field, parameter range, potentials, phase order, (A_g,B_g,C_g), and
degree identity are unchanged from `source_lock.frozen_theorem`.

## Scope, anti-claims, and permissions

The manuscript stays within the locked fixed positive-coefficient family.  It
explicitly excludes arbitrary potentials/coefficients/words, positive
characteristic, generic finite Newton fans, all symplectic automorphisms,
entropy equalities, periodic/trace/multiplier/centralizer/invariant-curve
claims, torus or arithmetic classifications, universal non-conjugacy,
numerical/CAS proof certificates, and absolute novelty or priority.  The
P12--P19 rows remain bounded collision-boundary statements, not an exhaustive
search; references remain context only.

Metadata and receipt permissions keep build, CAS, data, experiments, figures,
publication, transport, upload, and post-stop source editing disabled.  The
planned page count and artifact identities remain future-null until a separately
authorized build.  No downstream authority is granted by this source review.

## Verdict

No source-identity, theorem/proof, phase-ledger, label/citation, scope,
anti-claim, permission, or provenance blocker was found.  The final expanded
source is eligible for a separately authorized build review; this note does
not authorize compilation, publication, transport, experiments, or upload.

PAPER_SOURCE_R2_EXPANDED_PASS
