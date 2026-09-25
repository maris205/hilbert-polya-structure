# Evidence — owned parity clock and arbitrary-period nonreturn

Candidate ID: `ANG-20260920-AFP01`.
Status: `OWNED PARITY IMAGE CLOCK; ALL POSITIVE RETURN PACKETS ABSENT — STOP / FORK`.

## Freeze, provenance and exact inputs

The original 158-line [card](../candidate-card.md), before its
appended outcome, has SHA-256

    fe1dc06ce89644078e422659e0b99cf48b45bbd97dd6ae3baa74faaa2a6553d5

The complete definition-only input from
[299](../../299-quotient-remainder-reciprocal-flow/evidence/scout-record.md)
has SHA-256

    1b7d92d27032ec555d6afc1041bc29246089143e51abde864128470d2b647423

Inputs are all positive root pairs, full compatible K^2 seeds,
canonical residues, current parity, exact divisibility domains and
rootwise joint Haar. Every terminal/missing-image point remains.
The [scout record](scout-record.md) separates source provenance,
bounded collisions and a new unproved sublattice proposal. No old
clock or packet theorem is used as an input to the main proof.

## Exact proof reproduction

1. Use reductions modulo aN to prove multiplication injective in K
   and to construct its inverse onto the residue-zero clopen subgroup.
   Verify every displayed U, V and inverse by substitution; use
   target roots (1,1) with odd first seed to test non-surjectivity.
2. Build the full partial-tail topology from actual finite branch
   pairs and clopen refinements. Align only already-defined middle
   histories; no terminal is assumed to admit a future step.
3. Decompose the inverse into an integral shear/swap, first-coordinate
   multiplication and translation. This gives the Borel IMAGE factor
   1/a on the parity-restricted domain with no extra half-factor.
4. Multiply actual branch factors and cancel common terminal products.
   Prove continuous all-point uniqueness using full support, then
   translate the entire real extension in both time directions.
5. For an ARBITRARY positive index word, use P_a=[[0,1],[1/a,1]].
   For length>=2, prove strict positivity and row sums >1; the
   larger eigenvalue exceeds 1, while |det|<=1 puts the other's
   absolute value below 1. Handle length one by its quadratic.
6. Solve the periodic affine equation over S^(-1)K using det(I-M)!=0.
   Prove Q intersect K=Z. Canonical digits then give the exact
   ordinary-integer floor recurrence, including negative integers.
7. Separate adjacent nonnegative, adjacent negative and alternating
   sign cases. Only a constant k, 0<=k<every index, can be periodic.
   Thus main parity is constant; multiply ALL root equations around
   the period to obtain the impossible adjacent-factor product.
8. Infer absence of nonzero lag isotropy from absence of all periods.
   Check the explicit mixed-sign four-root family and its finite
   seed witness with digits (0,0,n,n), not a flow period. Rebuild
   both controls' branch laws;
   use the same proved seed lemma where its hypotheses match.
9. For ADJACENCY-OFF prove constant root ratio, enumerate ALL fixed
   cores (n,n,k,k), and use actual tail arrows to count their basins,
   multiplicities, repeats and the n=1 zero-time isotropy boundary.

This is an exact argument at arbitrary indices and period, with no
cutoff, numerical determinant, finite congruence sample or trajectory
census. The final 353-line [paper](../paper.md) has SHA-256

    3fea72d3c21e436345a8344af96c7a9107973ecf9172a713921da2e7961b55ca

## Internal review and scope limits

Root owns integration and every file except the native reviewer's
[independent-review.md](independent-review.md). ARS raw-card,
manuscript-comparison and final adverse checks preserve actual
access order and byte bindings. The auxiliary scope is only the
two frozen controls. Execution uses inherited model/shared context;
it is not external peer review, formal verification or independent-
error evidence. Definition scouts are not extra mathematical seats.

Actual access order was complete original card -> all raw owner,
seed, main and control findings -> complete final 353-line paper ->
final adverse report. The reviewer used an inverse-integer-matrix
proof before seeing root's forward-positive-matrix argument, then
checked both. The auxiliary read only the raw controls and supplied
its own constant-index seed proof before manuscript access.

The finite four-root seed witness was supplied by the reviewer in
raw analysis, checked directly by root and attributed in the paper
before manuscript review. It is not claimed as a blinded duplicate
discovery. Root read the entire final 188-line review report, SHA-256

    4c9f8f55d8fccae619868c871824fcb040dee3a40dc419a3fa7ccae67dbd084e

The report binds the exact final paper and original card prefix.
No correction was requested and no review issue remains unresolved.
Historical source comparisons, author-side scouting and companion
documents were outside the mathematical review's independent scope.
Byte locks and agreement are not proof certificates or Route credit.

The whole appended 197-line card has SHA-256

    a805404d51bda80de0ef805d5ab5f67d9aca228b0fba89960c77869027881413

The 124-line current definition/admission record has SHA-256

    600697633db02a00d9ed427cbc8bf9929a87aa2c656efa85ebe75fd4ea09bf0a

The whole-card digest does not replace its original freeze.

The mathematical stop is ALL positive time-return packets absent,
not merely failure to find a short orbit. The reusable seed lemma
applies only to the exact residue/shear law proved here, not every
profinite dynamics. Nonreturning orbit equivalences and coarse
Hausdorffness remain OPEN, as does stronger source/measure naturalness.
T3 NOT SUPPLIED / NOT PURSUED; classical A0/A1/A2 NOT APPLICABLE;
formal UNASSIGNED; B NOT INVOKED. Old packages unchanged; 241/242
paused; goal active. No PDF/LaTeX, staging, commit, upload or publication.

## Separate document-check snapshot

The read-only document checker captured the six existing package
Markdown files before the reviewer-owned report was written. Its
48 relative links included both current registry links: 42 targets
existed, while six references to independent-review.md were correctly
left pending. No other link or formatting issue was found. This
snapshot was not presented as a complete seven-file package PASS.

All seven primary/current-registry identity and status records matched.
The original 158-line prefix, whole appended card, 353-line paper
and scout record matched their specified locks. Additional captured
input hashes were:

- Evidence index before this receipt:
  `9a1cf9e04c0ed41543d3a9fbb0031b89a979454e9572d0d1bc8c991856b2aae2`.
- Claim ledger:
  `c7230d14c810629c53efa93d5010ba0543f290dc0835f7225adaed5a7c9127ff`.
- Package README:
  `0554e07f71ced9ad0edfef0ca950ebba816b6f5a751423303e792088435f1ea0`.

The checker used UTF-8, final-newline, control-character, trailing-
whitespace and actual relative-target checks. It made no edits,
mathematical claims or expanded historical checks. Final report
bytes and later receipt changes are separately checked by root;
the snapshot does not silently claim coverage of later versions.

## Final artifact verification — 2026-09-20

After the final reviewer-owned file existed and root read it in
full, read-only Python `pathlib`, `re`, `hashlib` and `json` checked
exactly the seven package Markdown files and both current registry
sections. UTF-8, final newlines, NUL/tab/CR rejection, zero-or-two
trailing spaces and actual relative Markdown targets were checked.
The source's exact methods above, not these file checks, support
the mathematical conclusions.

- Seven package Markdown files: PASS.
- 48 package-relative links plus two current registry links,
  50 total: PASS. The previously pending review links now resolve.
- Five primary package records and two current registry records,
  seven candidate-ID/final-status checks: PASS.
- Six byte locks: original card prefix, whole appended card,
  final paper, final review, current scout record and read-only
  299 definition input: PASS.
- Zero format, link, identity or byte-lock issues.

The original prefix was recovered by splitting once at
`\n## Appended audit outcome`; its 158 lines and digest match the
freeze. The evidence-index input before this final receipt was
SHA-256 `65a807b3d1bcc290fc5312a99d926e9814098a9cd8a5ee45c4c138597cd0769a`.
Root separately checked this changed receipt after appending it.

The scoped whitespace command was

    git diff --check -- readme.md papers/README.md papers/300-adjacent-factor-parity-flow

It exited 0. Direct file checks cover the untracked package, which
Git diff alone would omit. No staging or commit was made. These
checks certify neither mathematics nor formal Route readiness.
