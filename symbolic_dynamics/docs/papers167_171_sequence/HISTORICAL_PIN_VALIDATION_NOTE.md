# Historical pin validation note — P167–P171

**Scope:** review-time evidence versus the final mutable tree.  
**Final state:** `NO HISTORICAL PIN MANIFESTS / HOLD_EXTERNAL`.

No file named `PINNED_INPUTS.sha256` exists inside the P167–P171 batch
archive or any of its five paper directories.  Consequently there is no
historical pin ledger whose review-time hashes should be interpreted as a
current-tree manifest, and there are no expected live-path mismatches to
waive.

Round provenance is nevertheless preserved explicitly:

- P167 retains `main_round0_original.pdf` at SHA-256
  `81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379`;
  the live, Round-1, and Round-2 PDFs share
  `b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9`
  after the proceedings-year metadata repair requested by Hostile Review A.
- P169 retains `main_round0_original.pdf` at SHA-256
  `df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2`;
  the live, Round-1, and Round-2 PDFs share
  `419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3`
  after the formal-publication citation repair requested by Hostile Review A.
- P168 and P171 are byte-identical across the preserved Round-0, Round-1,
  Round-2, and live PDFs because neither review requested a manuscript
  change.
- P170 is byte-identical across its preserved review rounds and live PDF
  because neither review requested a manuscript change.

The five paper-local `SHA256SUMS` files are the authoritative integrity
manifests for the final paper trees.  The batch
`CANONICAL_PDF_MANIFEST.sha256` is the authoritative five-PDF receipt.
Neither final manifest changes the historical round copies or author/reviewer
transcripts.  All artifacts remain internal under `HOLD_EXTERNAL`.
