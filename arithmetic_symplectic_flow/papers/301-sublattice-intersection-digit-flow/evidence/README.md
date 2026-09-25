# Evidence — sublattice IMAGE clock and fixed-family multiplicity

Candidate ID: `ANG-20260920-SID01`.
Status: `OWNED SUBLATTICE IMAGE CLOCK; UNCOUNTABLE INTEGER-TIME MULTIPLICITY — STOP / FORK`.

## Frozen inputs and final mathematical files

The original first 156 lines of the [card](../candidate-card.md)
have SHA-256

    64744d13c29b3cc2455d1b7188bd161e0de764c0b4b64a58c0f919fa3fe9a8d2

The complete definition input in
[300's scout record](../../300-adjacent-factor-parity-flow/evidence/scout-record.md)
has SHA-256

    600697633db02a00d9ed427cbc8bf9929a87aa2c656efa85ebe75fd4ea09bf0a

Root read this input before freezing. The current 165-line
[source and breadth record](scout-record.md) has SHA-256

    6a6dbada5ea261d6cd46604e79b096bb7612adfb38de0dbba5e8cbe023edeb17

It records one audited owner, a separate untested affine-word
definition with no ID, and an unadmitted renewal definition gap.
Those separate lanes supply no mathematical result to this candidate.

The final 325-line [paper](../paper.md) has SHA-256

    99a96fb8c9228189a4a803c76659786c5e54fa0c256ee422259011328ed02977

The whole 196-line card, INCLUDING its appended outcome, has
SHA-256

    425b8bc926638d1b24e58291dbeb9fa044563885362e8627e461e2c4ba05f700

The appended digest does not replace the original pre-result freeze.

## Exact proof reproduction

1. For arbitrary finite-index L in Z^2, use its vertical projection
   and horizontal kernel to derive the unique column HNF. Reduce
   integer vectors in the stated second-then-first order to count
   the ac cosets. Prove intersection/adjoining retains finite index.
2. Use compatible residues modulo dN to prove integer multiplication
   injective on K and onto the zero-mod-d subgroup. Apply both
   triangular divisions to EVERY x in K^2; verify x=j+A_L*y.
3. Check every actual inverse and next-lattice equality. At target
   (2Z^2,Z^2), reduce modulo 2Z^2: one generator cannot span
   (Z/2Z)^2. Retain every missing-image seed as an object.
4. Normalize Haar on A_L K^2 of index det A_L. Translation
   gives inverse IMAGE 1/det A_L on every Borel subset, not
   just congruence cylinders. Use this same measure at every root.
5. Build the full retained-lag owner from finite actual branch pairs.
   Cancel common terminal products to obtain presentation independence
   and additivity of log D_m-log D_k. Full support fixes its
   continuous all-point version; use the entire real extension.
6. Check n divides m iff L_m is contained in L_n. Compute the
   actual scalar next root gcd(lcm(n,m),j) with ALL K^2 seeds.
7. At equal roots L_n, first impose root fixedness, forcing j=0
   for n>=2. Then injectivity forces x_1=0, while x_2 ranges
   over ALL K. Handle n=1 separately with its entire fixed fibre.
8. Compute the FULL retained-lag isotropy Z and its clock image.
   Prove different fixed constant tails cannot have an arrow, even
   after excursions through non-diagonal roots or finite preimages.
   Compare n=2 and n=4 without identifying equal or multiple times.
9. Rebuild the two controls' OWN IMAGE laws. For ADJOIN-OFF solve
   (n-1)x_1=-j, keeping 0 and -1 and every passive coordinate.
   For UNIT-INDEX use identity seed transport, then the two-step
   root stabilization to distinguish zero time from isotropy Z.

This is an exact infinite-family proof, not a finite lattice/seed
enumeration. No numerical precision, cutoff, scientific command or
external literature input is used. The result stops at the specified
fixed family; no all-period main theorem is implied.

## Internal review, access and adverse scope

The native reviewer owns only [independent-review.md](independent-review.md).
Its final 181-line report has SHA-256

    62ccce4d257e39fd488b9e7b72cb7cd010800d15e846cbf650aa70781a69195f

Root read that complete final report and verified its digest.
Actual access order was original complete card -> all raw owner,
fixed-family and control findings sent to root -> final 325-line
manuscript -> final adverse report. The auxiliary read only the
original card for its two frozen controls, not the manuscript.
The reviewer and auxiliary independently checked the controls.
The reviewer's raw UNIT-INDEX two-step stabilization was checked
and attributed in the paper before manuscript comparison; it is
not represented as a blinded duplicate discovery.

ARS supplied the raw-card, manuscript-comparison and strongest-
adverse-reading checkpoints. The strongest objection, possible
merging via inverse excursions outside the scalar sector, is
answered by the full tail-arrow definition, not a restricted graph.
No main-manuscript correction was requested; no review issue remains
unresolved. These are inherited-model/shared-context internal checks,
not external peer review, formal verification or independent-error
evidence. Definition scouts are not additional mathematical seats.
Historical novelty and the separate pending proposal were not
certified by this mathematical review.

T0, scoped measured T1 and the tested T2 family are established.
Multiplicity and composite primitives stop target promotion. Strong
naturalness, other fixed roots/returns and coarse topology remain
OPEN / NOT PURSUED. T3 is not supplied; classical A0/A1/A2 are
NOT APPLICABLE; formal coordinates UNASSIGNED; Route B NOT INVOKED.
The same-object ledger is intact. Old packages/mirrors unchanged;
241/242 remain paused; Markdown only; programme goal active.

## Administrative checks

The separate read-only documentation check captured an earlier
six-file snapshot: 39 local links, 35 existing targets and four
links pending the evidence README. Both registry entries were also
pending at that instant. Its six ID/status checks and two locks
(original card prefix and paper) passed. These were anticipated
unfinished targets, not concealed link failures. The checker had
authored the preceding definition proposal and is explicitly NOT
counted as an independent mathematical reviewer.

After all seven files and both registries existed, root ran a
scoped read-only Python/Path check of inline Markdown targets,
identity/status strings, final newlines and trailing whitespace,
plus hashlib SHA-256 checks of the six bound inputs/outputs above.
The check read package files and registry entries; linked external
package paths were tested for existence, not treated as new research.

Final pre-receipt snapshot, 2026-09-20:

| Checked item | Count | Result |
| --- | --- | --- |
| Package Markdown files | 7 | All present |
| Package local links | 44 | All targets exist |
| Current registry links | 2 | Both resolve to this package |
| Package plus registry ID/status checks | 9 | All agree; historical initial OPEN remains labelled |
| Original/full card, paper, review, scout, 300 input locks | 6 | All SHA-256 values match |
| New-file whitespace and EOF checks | 7 | No issue |
| Unresolved issues | 0 | Earlier pending targets resolved |

For reproduction from the workspace, use `head -n 156` on the
candidate card piped into `sha256sum` for the original prefix,
and `sha256sum` on the complete card, paper, review, scout and
the named 300 input for whole-file locks. Link checks resolve each
inline Markdown local target relative to its containing file;
the registry check is limited to each new 301 entry, not unrelated
historical documents. No network or scientific calculation is involved.

`git diff --check -- readme.md papers/README.md papers/301-sublattice-intersection-digit-flow`
exited zero. Since the package is untracked, its direct per-file
whitespace/newline checks are the relevant additional coverage.
Scoped Git status showed only the two modified registry files and
the untracked new package. Nothing was staged or committed.

The evidence README at that check was 117 lines, with five links;
its pre-receipt SHA-256 was
`41c5ed66ec44e90fe950d9f8b9ab104d3cfbc1f5e29d40f1c77c454b0d025060`.
This is a snapshot hash, not a claim about the subsequently appended
receipt. Only this evidence receipt changes after the full QA;
its links and formatting are checked again on the final bytes.
Administrative checks certify neither a theorem nor a Route result.
