# Correction to BibTeX-only R2 review

**Review ID:** PAPER_SOURCE_R2_BIBFIX_CORRECTION_2026_08_22

This correction supersedes the provisional PAPER_SOURCE_R2_PASS receipt for
the current BibTeX identity. The pass receipt verified hashes and balanced
BibTeX delimiters but missed a TeX math-mode defect in the repaired title
fields. No source, build, or transport file was edited by the reviewer.

## Current identity (verified)

* paper/main.tex: 37,423 bytes/LF981,
  SHA 2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014.
* paper/math_commands.tex: 702 bytes/LF20,
  SHA 37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582.
* paper/references.bib: 2,335 bytes/LF73,
  SHA 5cc0a88c3792b945ab6181ed1e83659c6d5251e172fa4885453b90c8dee15a2c.
* paper/BUILD_METADATA_R0.json: 3,588 bytes/LF1,
  SHA fd03d826bc9e65d0b578de5fce0a6b029bd38196d561e4b092aac2cfb77bd675.

The key set, brace balance, source bindings, theorem source, and permissions
otherwise pass.

## Blocking TeX defect

The two changed fields currently contain the forms:

    title = {Dynamics of polynomial automorphisms of {$\mathbb C$}^k},
    title = {Dynamical compactifications of {$\mathbb C$}^2},

BibTeX preserves the inner braces and emits the TeX token sequence equivalent
to {$\mathbb C$}^k (respectively ...}^2). The dollar signs close math mode
before the superscript; the ^k/^2 therefore occurs outside math mode and is
not a valid stable title expression. Depending on the TeX path it triggers a
“Missing $ inserted”/superscript error or changes the title tokenization. A
balanced BibTeX brace scan cannot detect this semantic TeX error.

The exponent must remain inside math mode, for example:

    title = {Dynamics of polynomial automorphisms of {$\mathbb C^k$}},
    title = {Dynamical compactifications of {$\mathbb C^2$}},

($\mathbb{C}^k$ and $\mathbb{C}^2$ inside the protecting braces are equivalent
acceptable forms.) After that exact repair, the metadata citation row and its
canonical hash must be regenerated and a new author stop requested. The
reviewer is not authorized to edit references.bib.

## Verdict

PAPER_SOURCE_R2_BLOCK

The mathematical manuscript and citation key identities remain sound, but the
current bibliography is not TeX-safe. No compilation, publication, upload,
transport, or downstream artifact is authorized by this review.
