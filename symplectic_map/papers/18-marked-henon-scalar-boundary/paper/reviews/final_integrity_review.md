# Final Integrity Review

Date: 2026-08-19 UTC
Reviewer role: fresh independent terminal-integrity reviewer
Result: PASS
Findings: 0

## Independence and exact input

I authored none of the recovered `R33` input universe and am distinct from every prior Paper18 role. I read exactly its 33 regular files. The package had exactly four descendant directories (`experiments`, `notes`, `paper`, `refine-logs`), zero symlinks, zero other entry types, and both `paper/reviews` and `paper/reviews/final_integrity_review.md` were absent.

The recovered governance chain was stable at these exact identities:

- `notes/FINALIZATION_STAGE_SCOPE.md`: `9c720dfcddd916f8b223fed163a34735f689be125ea6aba9748d0d685990c8fb`, 20,861 bytes, 157 LF.
- `experiments/finalization_lock.json`: `3d6dbd22282cfb528784a09d3d1370fd3383907e846cd3cc62a3ae026e8bed92`, 48,160 bytes, 1 LF.
- `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`: `a77211f190a87d434b4cb64b2bcac078c864a0660c1181292a2f85866f0dc6ad`, 4,761 bytes, 22 LF, ending `FINALIZATION_STAGE_PASS`.
- `paper/FINAL_RELEASE_MANIFEST.json`: `4ecd941e55cf14d3e84e964a484fb6bd4a9af6a7f745f42948f5760f6350c43c`, 43,491 bytes, 1 LF.

All seven live JSON artifacts were strict compact canonical JSON. The finalization lock's exact `R33` and terminal read lists matched the live universe. The release manifest excluded only its own hash and bytes and bound every other one of the 32 live files by safe unique sorted path, SHA-256, bytes, and LF. All 32 bindings matched. The prior independent terminals remained `SOURCE_DESIGN_PASS`, `SOURCE_LOCK_PASS`, `PAPER_PLAN_PASS`, `PUBLICATION_STAGE_PASS`, `MANUSCRIPT_SOURCE_PASS`, `MANUSCRIPT_R1_PASS`, and `MANUSCRIPT_R2_PASS`.

## Deterministic terminal build

The build-only runner used the two literal roots `/tmp/p18-paper18-final-R7nK4vM2` and `/tmp/p18-paper18-final-H9qT5xL3`. It attested that both were fresh and initially empty and that all eight locked commands exited zero under the exact deterministic environment. I independently verified the intact post-build roots as distinct, root-owned, non-symlink directories with mode `0700` and resolved parent `/tmp`. Each contained exactly eight regular non-symlink files and no other entries:

| File | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `main.aux` | `f59d3f82917a034819271679954f4461c7b13c2f3e5cd0ad8bf7b67626fc7f04` | 8,627 | 103 |
| `main.bbl` | `245c615779365bbe1a6f8c25b0db64361218db1beda5e7c596f3348d35c33d8b` | 1,351 | 43 |
| `main.blg` | `d70c6fc284ddc58feed42c6ee7e3d8b03d753d99c8b7900a29d589b6d5750a0c` | 890 | 46 |
| `main.log` | `6e811aba0a097630fe9f71919118ffe622ab748f723dcca31cba3a055921c697` | 25,362 | 646 |
| `main.out` | `35f8e17d8fa93b89214a97a7b7e3e734193cd481b83f8aa0bcb621e6b199ccd2` | 6,286 | 25 |
| `main.pdf` | `e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b` | 425,791 | 2,220 |
| `main.tex` | `65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d` | 69,588 | 1,602 |
| `references.bib` | `51bb41341009caa22d9433440475761608e1d4af2343a974cfbd74447070ea21` | 1,577 | 54 |

Every corresponding durable artifact was byte-identical between roots. The two source copies matched the frozen project sources. The required five-way equality held exactly:

`A/main.pdf = B/main.pdf = paper/main_round0.pdf = paper/main_round1.pdf = paper/main.pdf`.

The runner kept command streams in memory rather than creating transcript files. Its actual per-root transcript attestations were, in order, `c36ef3c86f512309708c403a547ef94d6b53d7f17a603e08c216b3957ec46ab7` / 11,079 / 313, `fd9a13dc2ce58e3d773115b95a63c6bc23e005f41b8676999cb6efad4baa0822` / 155 / 4, `8de4a5473a6cf419c257d80ea0e391cea0e2930200256a564f53868e334977b0` / 7,567 / 151, and `8933540883d83f339e14296672f018710c61672eeca893e7ec752aa12d6e17df` / 6,523 / 102. The separator-free combined attestation was `df915d282f868f837feeeea574aaca90f579cc17028a71e43d1a1300ec6cc297` / 25,324 / 570. These non-durable observations could not be reread by this reviewer; I bound them transparently as the build-runner's actual attestations and confirmed that they exactly match the frozen contract. Every durable consequence was independently replayed.

## PDF, content, and security replay

Both PDFs independently passed a length-aware physical parser: 70 unique physical object headers, 69 stream objects, 69 Flate streams, 69 successful decodes, 706,269 decoded bytes, zero decode failure, and zero silent skip. Payloads were sliced only by resolved `/Length` and checked at the resulting `endstream`; delimiter-regex payload-end detection was not used.

The authoritative output probes matched on A and B. `/usr/bin/pdfinfo` produced `effd968c18be03dab90f89b99934a51e96e34984d9c52f10415a4c6ee0041fe5` / 546 bytes. `/usr/bin/pdftotext -layout` produced `ab8426724bea8ecf6d1856d230adb1ca88821cf591ac6fd87565d23fb79fd45f` / 73,353 bytes. The raw font table was byte-identical at `35bbbf5b09cc08665fa2b3b302b0b2ea622b48a531fecbd0419b19d42d3ed379` / 2,256 bytes / 24 LF and listed exactly 22 fonts, all embedded, subset, and Unicode-mapped.

The document has exactly 23 nonempty pages, eight main sections, one appendix, one proof table, five theorem parts, twelve uniquely numbered proof bridges, twenty anti-claims, and the exact seven citation keys `BH26`, `CD26`, `FM89`, `GT24`, `Gor13`, `Hug24`, and `StacksProject`. The bibliography and BBL contain the same exact keys. `References` occurs as the sole page heading on page 23. Final LaTeX and BibTeX diagnostics are zero in every locked category.

The corrected anonymity contract holds. `paper/main.tex` contains blank `\author{}` and `\date{}` fields. The first extracted nonempty lines are the two-line exact title followed immediately by `Abstract`, so the visible byline is blank; the token `Anonymous` is absent from public PDF text. Governance identity remains `Anonymous`. PDF Author, Subject, Keywords, and Creator are empty; Producer is exactly `pdfTeX-1.40.22` and is toolchain rather than identity metadata; creation and modification dates are absent.

Exactly one URI action exists, with sole target `https://stacks.math.columbia.edu`. Every other URI/external-file action and every AcroForm, XFA, JavaScript/JS, Launch, RichMedia, FileAttachment, EmbeddedFile/Filespec, image XObject, attachment, signature, trailer ID, and encryption predicate is zero/false. The public-marker gates for identity leakage, local paths/hashes, governance/review tokens, grants/acknowledgments, repository/submission markers, unsupported priority, empirical claims, agent/model names, draft markers, and operational instructions all returned zero.

## Exact cleanup and terminal poststate

Before cleanup I replayed every gate above and revalidated the frozen in-memory cleanup plan at `bc99948f14583d6d8d6b029e69fe1797a3e27cea830902d34f20e5d1a705ac6f` / 2,279 bytes / 1 LF. Through no-follow directory descriptors anchored to the validated root inodes, I unlinked exactly the eight listed literal children in root A and then the eight in root B. I then removed exactly those two empty literal roots, in that order. No recursive deletion, wildcard, glob, cleanup walk, shell cleanup, symlink traversal, transcript/evidence/helper file, or project write occurred.

All sixteen child paths and both roots are absent. No top-level temporary path containing either root suffix remains. A complete post-cleanup snapshot equals the pre-cleanup `R33` snapshot byte for byte: 33 regular files, four descendant directories, zero symlinks, zero other entries. `paper/reviews` and this report path remained absent through all validation and cleanup checks.

## Effect

This pass authorizes only the contract's local anonymous release state. It performs no submission, upload, hosting, repository push, dashboard action, external messaging, identity disclosure, or other external release effect. The sole terminal project mutation is creation of the `paper/reviews` parent and this exact report, producing immutable `T34` with 34 regular files, five descendant directories, zero symlinks, and zero other entries.

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED
