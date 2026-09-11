# P194 author handoff — Round 0 plus source-repair addendum

**Decision:** `PASS_INTERNAL / ROUND0_AUTHOR_FREEZE`  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`

## Mathematical boundary audit

- The carrier is exactly `[k]^n` with `n,k>=1`.
- The sign encoding, cancellation direction, selected unmatched occurrence,
  and least-colour order are stated literally and consistently.
- Operator availability is recomputed after every single update.
- The proof uses reverse-word RSK because of the frozen tensor convention and
  does not describe reversal as part of the dynamic.
- Highest iff ballot is proved from prefix deficits under the actual signature
  rule rather than borrowed under an incompatible convention.
- Component preservation and unique highest vertices are classical inputs;
  the one-unit energy drop independently excludes nontrivial recurrence.
- The pointwise clock subtracts `sum_i i lambda_i`, not the unweighted size
  of `lambda`.
- The global maximum proof checks both equality conditions and identifies
  `k^n` as the unique deepest word.
- The component depth polynomial includes the normalization that cancels the
  usual `q^(n(lambda))` factor in principal specialization.
- Shape multiplicity counts recording tableaux; it is not confused with the
  semistandard size of a component.
- The fixed census is bounded by the number of rows, matching longest
  decreasing subsequence length under RSK.
- The fibre theorem compares complete predecessor sets, not only their sizes.
- A self-predecessor is included exactly for highest targets; empty fibres are
  allowed.
- Lower-colour admissibility is tested at `f_i(y)`, not at `y`.
- Candidates of different colours are distinguished by content.
- The stable threshold proves necessity and sufficiency.  It asserts
  existence of a full fibre, not uniform equality for all targets.
- The `n=1` and `k=1` cases are explicitly covered.

## Exact-control audit

- Complete word enumeration passes for `1<=k<=4` and `1<=n<=7`.
- The script uses only the Python standard library and imports no prior-paper
  or scouting implementation.
- Functional-graph logic and tableau logic are separate routines.
- SSYT enumeration is compared with an exact polynomial quotient; hook length
  is compared with a separate corner-removal recurrence.
- Every actual and predicted predecessor set agrees for all 25,384 targets.
- Involution shapes are checked through `S_8` by direct inversion and RSK.
- Large-alphabet staircase witnesses are checked without claiming exhaustive
  ambient enumeration.
- Two fresh runs are byte-identical to `code/CANONICAL.txt`.
- The recorded transition digest is
  `15eae7619f324f7730af7dddb103820cb72434ebf897ee8ec4fde1c611e8df49`.
- Finite checks are never described as proof or novelty evidence.

## Source and collision audit

- All five Round-0 bibliography records had publisher or DOI metadata and were cited.
- The accepted Review-B source repair adds a sixth matched citation/BibTeX
  record for Defant--Williams and zero-credits its deterministic crystal
  pop-stack sorting/orbit surface.
- No uncited bibliography entry is present.
- Kashiwara/crystal structure, RSK, tableaux, Schur specialization, hook
  formulas, and involution correspondences are explicitly zero-credit.
- P144 prevents standalone credit for a deterministic leftmost scheduler or
  ballot-layer mechanism.
- The standing 0-Hecke/sorting firewall prevents a generic least-descent
  framing.
- P181 is separated by literal move, carrier, recurrent structure, and clock.
- The killed RSK retractions in the P142–146 scout and P166 open-fresh ledger
  are respected: RSK is not the P194 update.
- Within-batch P192 and P193 have different state changes, temporal
  statistics, and inverse tests.
- The bounded source non-hit is explicitly not a novelty, priority,
  completeness, or freedom-to-operate conclusion.
- `OWNER_AMBER/HOLD_EXTERNAL` appears in the abstract, manuscript close, and
  package ledgers.
- No author identity, affiliation, grant, or self-identifying repository URL
  appears in the paper.

## Writing and package audit

- The abstract leads with the literal process and states the strongest exact
  bounds.
- Every manuscript claim has a proof location and a finite falsifier in
  `CLAIMS_EVIDENCE.md`.
- Classical ingredients are subtracted before the residual is described.
- No TODO, FIXME, XXX, `[VERIFY]`, unresolved citation, or unresolved reference
  remains.
- `FIGURE_PLAN.md` records an explicit zero-figure Round-0 decision.
- The requested files `main.tex`, `references.bib`, `README.md`,
  `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`,
  `PROOF_PACKAGE.md`, `CLAIMS_EVIDENCE.md`, `SOURCE_VERIFICATION.md`,
  `BUILD.md`, `SELF_QA.md`, `code/verify.py`, and `code/CANONICAL.txt` all
  exist.
- No hostile review was part of the immutable author Round 0. Later
  process-separated review and its source repair are recorded in the central
  P192--P196 review packages.

## Build audit

- The settled Round-0 PDF is four A4 pages and has no warning, bad box, unresolved
  reference, unresolved citation, or fatal error.
- A repeated deterministic pass and an isolated source-only cold build match
  SHA-256
  `9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207`.
- All 27 font rows are embedded, subsetted, and Unicode mapped.
- PDF metadata fields are blank; the file is unencrypted and contains no
  form, JavaScript, or metadata stream.
- All four rasterized pages were inspected; no clipping, overlap, malformed
  display, missing glyph, broken bibliography, or unintended blank page was
  found.
- The current source-repair PDF is five A4 pages, 372,121 bytes, with SHA-256
  `682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b`;
  it likewise has zero warning/bad-box/unresolved-reference matches and all
  27 font rows embedded, subsetted, and Unicode mapped.
- Extracted text contains no unresolved marker or identifying author data.

Round 0 remains the immutable author-side baseline. The current manuscript
also incorporates the Review-B source subtraction; neither state is owner
clearance or permission to circulate externally.
