# Independent Paper18 Source-Lock Review

Date: 2026-08-17 UTC

Candidate: `marked_henon_scalar_boundary_v1`

Project: `papers/18-marked-henon-scalar-boundary`

Final repaired lock: `experiments/source_lock.json`

Article: **Marked Trace Coordinates and Scheme-Theoretic Ramification at the
Polynomial Boundary of Generalized Hénon Maps**

## Review identity, temporal fence, and sole-write rule

I am the fresh restarted reviewer of the final provenance-repaired Paper18
source lock. I authored none of the 15 bound inputs and authored no version of
the source lock. The preceding review attempt correctly stopped with zero
project writes because the lock introduced an unbound `GOR14` citation record.
I did not inspect or alter the repair while its author was working. I began
this restarted global audit only after the explicit `LOCK PROVENANCE REPAIR
AUTHOR STOP` and stable repaired identity were supplied.

I reread both applicable review and proof-audit instruction sets and reread all
15 bindings to EOF. Before this report was created, the future review path and
the entire `paper` path were absent. No other project path was written. This
report is the sole project-file write made by this review.

No bibliography, TeX, manuscript, code artifact, CAS, scientific computation,
experiment, parameter scan, dataset, result, figure, asset, build,
publication, finalization, release, repository action, submission, upload,
external message, or identity action was performed. Read-only parsing,
canonical serialization, hashing, byte/LF counting, path inspection, exact
in-memory history reversal, and theorem/source checks were used only for this
integrity review.

## Final stable identity and canonical JSON

The final repaired lock independently rehashed to exactly:

- SHA-256:
  `b29378068f5da669f6b9c15d4d4a3e81daa6a2ca345fd86481c403f86771fac3`;
- bytes: `32589`; and
- LF count: `1`.

Strict UTF-8 decoding and JSON parsing succeeded with duplicate-object-key and
nonfinite-number rejection. Recursive ascending Unicode-code-point key
sorting, compact separators, UTF-8 non-ASCII preservation, `allow_nan=false`,
and one terminal LF reproduced all `32589` bytes exactly. The lock has no BOM,
CR, insignificant whitespace, duplicate key, second terminal LF, `NaN`, or
positive or negative infinity. Independent synthetic probes rejected each of
`{"x":1,"x":2}`, `{"x":NaN}`, `{"x":Infinity}`, and
`{"x":-Infinity}`.

The lock does not bind itself. Its own final SHA-256 and byte count occur in no
JSON value, and `experiments/source_lock.json` is absent from the 15-entry
binding ledger. The explicit self record excludes both bytes and SHA-256.
Every bound path is unique, nonempty, relative, free of dot and dot-dot
segments, resolves inside the workspace, and names a regular non-symlink file
with strict UTF-8 and a terminal LF.

## Exact four-stage authoring-history reversal

The complete lock history was reconstructed in memory rather than accepted
from narrative assertions.

First, reversing only the final provenance repair did the following:

1. removed the four new history fields recording the pre-repair identity,
   blocker, and repair;
2. restored both apply-patch operation counters from `4` to `3`;
3. restored the Gorbovickis--Taflin internal identifier from `GT24` to `GT25`
   without changing its source or role; and
4. reinserted the former `GOR14` record after `GOR13`.

Canonical serialization then reproduced the blocked predecessor byte for
byte:

- SHA-256:
  `7c91f4aada672b29ec5ad31f1e762968388389a825bf728ba9fe071a942387b6`;
- bytes: `32100`; and
- LF count: `1`.

Thus the repair removed exactly the unbound citation record, normalized the
already-bound `GT24` label, corrected write accounting to four apply-patch
operations on one unique path, and added an exact disclosure. No binding,
theorem, proof obligation, permission, universe, score, anti-claim, or other
path changed.

Second, reversing the predecessor's final schema audit by removing the exact
A1--A20 canonical-block contract and the declared schema-history additions,
and restoring its pre-audit write accounting, reproduced:

- SHA-256:
  `afce1361a808f4d17166a98e07d8770e11eb9fb644ccf57e7d4c960f43d55364`;
- bytes: `31207`; and
- LF count: `1`.

Third, removing the earlier bounded-repair disclosure and restoring the
`PROOF_PACKAGE.md` binding's former nonexistent final-line requirement to
`SOURCE DESIGN AUTHOR STOP` reproduced the sole initial apply-patch stream:

- SHA-256:
  `25a7388bb3b528caf58b49f679f7672fa082d22ae39b5a42d4fe9cacbe77fc17`;
- bytes: `30288`; and
- LF count: `1`.

The reconstructed identities prove that the four same-path patches have the
declared history and that the final provenance repair introduced no
undeclared semantic or filesystem change.

## Exact 15-input binding replay

Immediately before this report was written, every binding matched its path,
category, byte count, LF count, SHA-256, regular-file status, non-symlink
status, UTF-8 validity, terminal LF, and required final line.

| Category | Bound path | Bytes | LF | SHA-256 |
|---|---|---:|---:|---|
| Batch | `BATCH_05_IDEA_REPORT.md` | 25617 | 560 | `7b50495f0177ef2a9a3afa16a87f5f7580dfb6f42fce5eed1d09bdff8d1d019e` |
| Batch | `BATCH_05_STATUS.md` | 13301 | 220 | `ac6778adbbe2a27a7b276885b4fa8641e3d908bc5f121fd4053f0c30e318518a` |
| Paper16 provenance | `papers/16-henon-support-size-torus-escape/paper/reviews/final_integrity_review.md` | 25462 | 234 | `e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76` |
| Paper17 provenance | `papers/17-shiftlike-torus-coset-decay/paper/reviews/final_integrity_review.md` | 20620 | 339 | `941e8b47e4436fdd9bff6f48ebf6e8c1174d07f545a220ead9ad02d73b23ed9d` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/experiments/EXPERIMENT_PLAN.md` | 12898 | 154 | `53a38842ca36ad57d84516dcc4761119a6db411ff998000dc53a6d890d2978a4` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/experiments/EXPERIMENT_TRACKER.md` | 8938 | 118 | `2f82dc00aef040ae38c182d9460c278a87731c28a940b3bc79a659ec1ddbb998` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/notes/CITATION_VERIFICATION.md` | 14139 | 236 | `16bb886a6d4fc72e71e58127b8d2ab01c695930f29c42ecf771f8c63830e9fb6` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/notes/CLAIMS_EVIDENCE_MATRIX.md` | 13447 | 113 | `bd323341293ebdcb139029c725b3f8432ba46bc627824aad7e7e911ce7d27bcc` |
| Independent design review | `papers/18-marked-henon-scalar-boundary/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 19199 | 366 | `b5112a412bf52d504b856e4652023ed41e682f35c566903df2da0fbbc58947e4` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/notes/NOVELTY_ASSESSMENT.md` | 14490 | 182 | `4edf1d891fd033f30a2754c80e0d88288577fe77030fe2e2c88440c6747f0240` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/notes/PROOF_PACKAGE.md` | 30538 | 611 | `99be46a2b242f99585b2f1692dd69facb87aca4674dab00eec79f76d0e9b4231` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/notes/RESEARCH_QUESTION.md` | 10473 | 185 | `cc04ee1db562f04f2291779481b52c2902020a8853bf1fdf186432560c892f24` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/refine-logs/FINAL_PROPOSAL.md` | 15731 | 249 | `d94c162ee19e8cf621e6599fbab3ab90589f7b0ec0daf9f34479a186bbe67c0f` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/refine-logs/INITIAL_PROPOSAL.md` | 8336 | 163 | `bfdd03291955d040594a4dd8cf8cfcb3198adb43d90b8b34a210deca96861a1b` |
| Paper18 author | `papers/18-marked-henon-scalar-boundary/refine-logs/REVIEW_SUMMARY.md` | 11953 | 177 | `7f514ac64a00acba1debb6d70c9f174bfe342c8afb2cfaf7ab72272e00d9c565` |

The categories are exactly two Batch snapshots, one terminal Paper16 record,
one terminal Paper17 record, ten Paper18 author sources, and one fresh
independent Paper18 source-design review. Both portfolio records end exactly
in `RELEASE_CONFIRMED`; the Paper18 design review ends exactly in
`SOURCE_DESIGN_PASS`. The 13 non-Batch bindings are the permanently
byte-immutable set.

## Exact inventory and lifecycle universes

Before this report, the Paper18 root contained exactly 12 regular files in
exactly three real subdirectories, with zero symlinks and zero other entry
types. The exact set was:

- `experiments/EXPERIMENT_PLAN.md`;
- `experiments/EXPERIMENT_TRACKER.md`;
- `experiments/source_lock.json`;
- `notes/CITATION_VERIFICATION.md`;
- `notes/CLAIMS_EVIDENCE_MATRIX.md`;
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`;
- `notes/NOVELTY_ASSESSMENT.md`;
- `notes/PROOF_PACKAGE.md`;
- `notes/RESEARCH_QUESTION.md`;
- `refine-logs/FINAL_PROPOSAL.md`;
- `refine-logs/INITIAL_PROPOSAL.md`; and
- `refine-logs/REVIEW_SUMMARY.md`.

The directories were exactly `experiments`, `notes`, and `refine-logs`.
`notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`, `paper`, `code`, `data`, `results`,
`figures`, and `assets` were absent. This was exactly
`U_L12_after_source_lock`.

Every lifecycle universe has its declared count, a unique sorted path list,
and the exact adjacent set equation:

| Transition | Sole additions |
|---|---|
| `U_L12` to `U_S13` | this independent source-lock review |
| `U_S13` to `U_P14` | `paper/PAPER_PLAN.md` |
| `U_P14` to `U_PR15` | independent paper-plan review |
| `U_PR15` to `U_G17` | publication-stage scope and publication lock |
| `U_G17` to `U_PUB18` | independent publication-stage review |
| `U_PUB18` to `U_D20` | `main.tex` and `references.bib` |
| `U_D20` to `U_SRC21` | independent manuscript-source review |
| `U_SRC21` to `U_R0_23` | round-0 build receipt and PDF |
| `U_R0_23` to `U_V1_24` | round-1 manuscript review |
| `U_V1_24` to `U_S1_25` | round-1 source-revision receipt |
| `U_S1_25` to `U_R1_27` | round-1 build receipt and PDF |
| `U_R1_27` to `U_V2_28` | round-2 manuscript review |

No transition removes a path and no unlisted intermediate artifact is
allowed. Creating this report moves the local Paper18 inventory only from
`U_L12` to `U_S13`: 13 regular files, the same three directories, and zero
symlinks.

The two Batch files are exact pre-pass activation snapshots. They are not
mistaken for live post-pass dashboards. No Batch mutation is made by this
review. Only after this pass and a separate explicit plan-stage invocation
may their narrowly selected status regions and complete append-only activity
records advance; all other Batch bytes remain immutable.

## Independent theorem and proof replay

The frozen theorem is **PROVABLE AS STATED**. The exact scope is coherent
across the ten author sources, the independent design review, and the lock.

1. For every `d >= 2`, with `r=d-1` and every positive period vector,
   repetitions allowed, the construction uses labelled pairwise-disjoint,
   exact, simple cycles. Point markings are divided only by their own free
   cyclic shifts; repeated-period labels are not permuted.
2. The simple scalar cycle-marked locus is nonempty and irreducible. Regular
   components of the simple total incidence are disjoint, so the full scalar
   locus lies in one unique component. That component is etale and dominant
   over the coefficient/Jacobian base, and its scalar fiber is exactly the
   scalar locus scheme-theoretically.
3. At the scalar full-rank point, the differential of
   `Psi=(-b,rho_1,...,rho_r)` is block triangular with diagonal blocks `-1`
   and the polynomial multiplier Jacobian. Hence `Psi` is etale somewhere,
   dominant, and generically etale, and the traces are algebraically
   independent over `C(b)`.
4. The fixed-Jacobian conclusion is correctly guarded: there is an
   unspecified nonempty open subset of `G_m`; each whole fiber over that open
   maps dominantly, and at least one component of the reduced fiber is
   dominant and generically etale. There is no fiber-irreducibility,
   all-component, every-nonzero-fiber, or prescribed-fiber conclusion.
5. Formal etaleness identifies the completed scalar local rings and gives
   `rho_i=lambda_i+bG_i`. The Cartesian simple-boundary square, base change
   for Kahler differentials, and base change for zeroth Fitting ideals give
   the exact critical-scheme restriction and
   `J_H mod b = +/- J_poly`.

The auxiliary ordered-loop algebra has the monic standard-monomial basis and
rank `d^n`; its product has rank `d^(sum n_i)`. The cyclic coincidences are
handled explicitly: `n=1` has the single relation `p(x)+(b-1)x`, and `n=2`
has `p(x0)+(b-1)x1` and `p(x1)+(b-1)x0`. No irreducibility, exact-cycle count,
or all-base finiteness of the deleted simple open is inferred from this rank.

The repaired Cartier-or-empty guard is retained. The Hénon and polynomial
Jacobian sections are not identically zero. Their zero schemes are effective
Cartier divisors when nonempty and may be empty. If the polynomial critical
scheme is empty, the component-multiplicity claim is vacuous; otherwise the
scheme restriction preserves the generic length along every actual
irreducible boundary component. No arbitrary closed-point intersection number
is claimed in positive-dimensional intersections.

Finally, `det(DH^{n_i})=(-b)^{n_i}` means that a trace records only the
unordered eigenvalue pair once the determinant is known. The residual
`mu_{d-1}` normal-form action preserves `b` and every trace and prevents a
generic injectivity or birationality claim on the cover when `d>2`. No naive
coarse-quotient completed-local claim is made near stabilizers.

## Citation provenance and score gates

The final live citation lock contains only sources represented in the bound
source package:

- Gorbovickis, arXiv:1305.0867, is the sole indispensable external proof
  input, with Theorem 1.6 and Lemma 2.1 supplying the arbitrary-period
  full-rank point for `d>=2`, and Definition/Remark 1.4 and Lemma 1.5 supplying
  the irreducible marked polynomial space;
- Gorbovickis--Taflin `GT24`, Huguin, Cantat--Dujardin, and Bianchi--He are
  comparison sources only;
- Friedland--Milnor supplies classical normal-form and low-degree context
  only; and
- Stacks Tags 02GH, 0257, 07Z6, and 0C3I support only the stated etale
  formal-local and Fitting base-change steps.

The prior unbound `GOR14` record is absent from the live citation lock. It
appears only in the transparent historical blocker/repair disclosure. The
Gorbovickis--Taflin identifier is now the bound `GT24`; its exact source and
comparison-only role did not change. The bound bibliographic stop rule remains
in force, so no later source may be introduced without primary-text checking
against a specific claim.

The source-design author assessments are novelty `8.0`, standalone value
`7.7`, and proof readiness `9.3`. The separately categorized fresh independent
design review gives novelty `8.0`, standalone value `7.7`, and proof confidence
`9.2`. The lock's score gate correctly records the independent adjudicated
triple `8.0 / 7.7 / 9.2`, not the author's self-assessment. All three clear the
conjunctive thresholds `7.5 / 7.5 / 9.0`.

## A1--A20 and zero-science replay

The inclusive canonical Markdown block beginning `- **A1.**` and ending
`- **A20.**` occurs exactly once in each of the ten author-source files. Every
extracted block has exactly 20 LF-terminated records, `2064` bytes, and
SHA-256
`363aabbb21c9327db4ad47956f732846089c17e9650f41e93df1f970f78c67a3`.
All ten streams are byte-identical. The normalized 20-record semantic lock
matches the same prohibitions.

The ledger bars full-incidence and specialized-fiber irreducibility,
every-nonzero or prescribed-fiber coordinates, all-component dominance,
global injectivity or reconstruction, reducedness, transversality,
nonsimple/compactified Fitting equality, unsupported closed-point
multiplicity, individual eigenvalue branches, exact-cycle counting from
finite-free rank, treatment of `b=0` as an automorphism, positive
characteristic, multi-factor maps, naive coarse stabilizer completions,
absolute-priority claims, and computational or empirical evidence. No source
revives any barred claim.

Scientific experiments, computational experiments, CAS, datasets, numerical
results, figures, and empirical claims are all exactly zero. The planned
article remains a proof-first 23-page paper within the credible 22--24 page
range, with zero figures and zero numerical result tables.

## Permission firewall and final disposition

At review time the source lock is frozen, source-lock review is the only
authorized current stage, the external effect is false, and the only permitted
project write is this report. Paper planning, bibliography, TeX, manuscript,
code, science, data, results, figures, assets, building, publication,
finalization, release, repository push, submission, upload, external
messaging, and identity disclosure remain false.

This verdict creates eligibility only for a later, separately invoked
proof-only `paper/PAPER_PLAN.md` authoring stage and a fresh independent plan
review. It does not itself invoke that stage, create a paper path, mutate a
Batch control, or grant any later or external authority.

Every identity, binding, history, inventory, lifecycle, role, permission,
theorem, proof, citation, score, anti-claim, page, and zero-science conjunct
passed before this sole write.

SOURCE_LOCK_PASS
