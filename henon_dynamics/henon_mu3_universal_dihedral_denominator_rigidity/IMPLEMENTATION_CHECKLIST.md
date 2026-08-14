# HCS-C54 implementation checklist

Status: **RELEASE_FROZEN against the persistent scoped code/results and
44-entry full-project inventories; implementation commit
`f2fee2f9844b84aa31e076aabe9d4bb88fbd3618` is provenance-locked**.

## Mathematics

- [x] Define full as the projective monomial stabilizer of the ideal.
- [x] Prove that an ideal stabilizer preserves both equation lines.
- [x] Derive the phase recurrence and alternating closure condition.
- [x] Enumerate exactly the even rotations and odd reflections.
- [x] Prove the \(6n\) count and \(\operatorname{Dih}(C_{3n})\)
  presentation.
- [x] Prove the support exact sequence with kernel \(C_3\).
- [x] Compute semilinear transport and the two rational geometric elements.
- [x] Separate Reynolds averaging from quadratic transfer.
- [x] Define packet-admissibility and restrict inherited certification to
  rows \(2,3,4\).
- [x] Prove the K0 identity, separate weights, and derive \(n\mid24\).
- [x] Check every divisor and construct the complete-factor converse.
- [x] Include the \(n=3\) total-rank trap.
- [x] Compute the residue-corrected exact \(n=3\) characters.
- [x] Test coefficient-field orbit packaging.
- [x] State the common-geometric-group and rational twist caveat.
- [x] State the noninjective virtual restriction kernel correctly.
- [x] Separate split, inert, and global scopes.

## Exact implementation

- [x] Promote the canonical certificate to a release candidate.
- [x] Pass the independent semantic checker, 36/36.
- [x] Pass 93/93 unit tests, including every targeted hostile mutation,
  residue orientation, total-rank collapse, and the exhaustive 198-leaf
  semantic rebound sweep.
- [x] Verify the 1,078-leaf inventory: 198 semantic, 876 exact-derived, and
  four allowlisted history leaves.
- [x] Reject duplicate JSON keys and unknown envelope keys.
- [x] Verify rollback-atomic exception safety after each of four local release
  moves; do not claim power-loss or storage-durability atomicity.
- [x] Confirm deterministic byte-for-byte immutable RC replay.
- [x] Build and verify the persistent 11-entry release-candidate code/results
  manifest, excluding both manifest files from its own scope.
- [x] Record the final payload, certificate, check, schema, and scoped-manifest
  hashes.
- [x] Include the scoped manifest in the 44-entry full-project inventory.
- [x] Backfill the implementation commit in the later provenance stage without
  changing the frozen paper.

## Documentation

- [x] Create the research question, theorem, derivation, and proof packages.
- [x] Create the primary-source and bounded-novelty audit.
- [x] Create the claim-driven experiment plan and tracker.
- [x] Create the narrative and paper architecture.
- [x] Create a formal LaTeX manuscript with complete proofs and declarations.
- [x] Create a scoped exploratory Route-A record.
- [x] Reconcile every release-candidate certificate field with theorem
  vocabulary.
- [x] Insert promoted release-candidate hashes without changing theorem
  semantics.
- [x] Run final forbidden-claim, encoding, whitespace, and citation scans.
- [x] Freeze the documentation only after the release-candidate and paper gates
  pass.

## Paper

- [x] Keep the title in the projective-monomial and split-local category.
- [x] Put the all-\(n\)/packet-admissible boundary in the abstract.
- [x] State the complete split-factor iff theorem, not only a rank test.
- [x] Include the common-group and counterpacket caveats.
- [x] Include data, ethics, conflict, funding, and contribution declarations.
- [x] Insert release-candidate replay counts and hashes.
- [x] Compile with LaTeX after the code hash tuple is final.
- [x] Audit citations/references, warnings, boxes, fonts, text extraction, and
  representative rendered pages.

## Release firewall

- [x] No full-PGL automorphism claim.
- [x] No all-\(n\) smoothness, motive, or packet claim.
- [x] No constant rank-\(6n\) rational group claim.
- [x] No rotations-only Reynolds average.
- [x] No total-rank proof at \(n=3\).
- [x] No silent common rational group scheme at \(n=3\).
- [x] No injectivity claim for virtual restriction.
- [x] No inert/global root, automorphy, continuation, FE, or RH.
