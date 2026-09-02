# Historical pin validation note — P162–P166

**Scope:** immutable review-time evidence versus later mutable live paths.  
**Final state:** `DOCUMENTED / NONBLOCKING / HOLD_EXTERNAL`.

Several review-time `PINNED_INPUTS.sha256` files intentionally record hashes
of paths that were subsequently advanced during the normal Round-1/Round-2
workflow.  They are historical receipts, not the final-tree manifest, and
must not be silently rewritten to current hashes.

At final closure, three such historical checks have expected live-path
mismatches:

- `reviews/p163_b/PINNED_INPUTS.sha256`: `README.md`, `BUILD.md`,
  `CLAIMS_EVIDENCE.md`, and `IMPROVEMENT_LOG.md` later received lifecycle or
  closure entries.  The reviewed source, bibliography, all three reviewed
  PDF paths, author verifier, and author canonical still match their pins.
- `reviews/p164_a/PINNED_INPUTS.sha256`: live `main.tex` and `main.pdf`
  advanced when Review A's two minor proof-expansion requests were closed.
  The immutable `main_round0_original.pdf`, bibliography, author verifier,
  and author canonical still match their pins.
- `reviews/p165_b/PINNED_INPUTS.sha256`: `PROOF_PACKAGE.md`,
  `SOURCE_VERIFICATION.md`, `IMPROVEMENT_LOG.md`, and `BUILD.md` later
  received Round-2 or final-status entries.  The reviewed source,
  bibliography, all reviewed PDF paths, Review-A report, author verifier,
  and author canonical still match their pins.

The affected review evidence manifests, where present, still validate the
frozen review bundles themselves.  Immutable round PDFs remain at their
recorded hashes.  The five paper-local `SHA256SUMS` files and the batch
`CANONICAL_PDF_MANIFEST.sha256` are the authoritative manifests for the
current final tree.  This note prevents a mutable-path mismatch from being
mistaken for manuscript corruption while preserving the original historical
hashes unchanged.
