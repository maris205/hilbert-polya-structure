# Paper 27 independent source-revision review (R1)

## Review disposition

This is the fresh, independent review authorized by
`B07-E0134-P27-SOURCE-REVISION-REVIEW-AUTHORIZATION-R1` for candidate
`positive_newton_translation_reciprocity_v5`.  The review used only the
authorized status ledger, the three anonymous source files, the
`SOURCE_LOCK.md`, `PUBLICATION_LOCK.md`, and `BUILD_PROFILE.md` control
records, and the preserved R0 `main.bbl` and `main.log`.  No compiler,
BibTeX invocation, cache operation, recursive traversal, search command,
future-root probe, source mutation, or external effect was used.

The census is all zero.  The one permitted bibliography correction is exact,
the source/control manifest remains the recorded 37-row aggregate
`ddf13a637b3e67c878bf83a89b73755bf3b9894274f3cd667ef7927ff9c40409`, and the
preserved R0 failure root is unchanged.  This review therefore passes the
source-revision gate.

## Source-trio byte census

| Path | Bytes | LF | Mode | Links | SHA-256 |
|---|---:|---:|---:|---:|---|
| `paper/main.tex` | 33811 | 829 | 0644 | 1 | `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` |
| `paper/math_commands.tex` | 601 | 17 | 0644 | 1 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6610 | 217 | 0644 | 1 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |

All three paths are regular, non-symlink files with link count one.  Direct
byte inspection shows strict UTF-8-compatible source bytes, no BOM, no CR,
and no NUL; each file has LF line termination and exactly one terminal LF.
The paper directory contains exactly the required trio.  `main.tex` embeds
the complete anonymous article, uses only the relative notation input and
bibliography named by the publication lock, and has no external asset
dependency.  `math_commands.tex` contains notation macros only.

## Bounded correction and preserved R0 evidence

The retained R0 evidence reports `main.bbl:101` as

    of {\mathbb c}^n.

and `main.log` reports `LaTeX Error: \mathbb allowed only in math mode`,
followed by `Fatal error occurred, no output PDF file produced!`.  The
current `shafikov_wolf_2003` title contains the sole authorized text-mode
repair:

    title   = {Filtrations, hyperbolicity and dimension for polynomial automorphisms of {$\mathbb{C}^n$}},

The correction is one occurrence in one title field, exactly the expression
identified by the R0 fatal line.  The ledger records the corresponding
pre/post bibliography census as 6607 bytes and
`4ec09da4d7be513d2cf11811515975e1f3c35b53ae9d84cbda6748cb39cbd23b` before
the edit, and 6610 bytes and the SHA-256 shown above after it.  The three
added bytes are confined to that explicit inline-math wrapping; no citation
key, author, title text outside the expression, venue, year, DOI, URL, or
other bibliography record changed.  `main.tex` and `math_commands.tex` retain
the frozen hashes from the build profile, so no theorem, equation, proof,
fixture, limitation, or other scientific content changed.

The failed root remains
`papers/27-positive-newton-translation-reciprocity/build/r0-20260829`.
Its preserved `main.bbl` is 3939 bytes, 118 LF, SHA-256
`23ad34a5605226dbea73edda95769b4768c2d2c6e834737f3ebe19d502f41df8`, and its
preserved `main.log` is 16625 bytes, 532 LF, SHA-256
`94419a503d6f35405ca5d45544f40db6dd6f6fa4a617a34c1b98036a153b1b51`.
The status ledger records this root as immutable, with no retained PDF and no
R1 root created.  No source revision touched that root.

## Citation closure and anonymous-source checks

The twenty bibliography keys are all cited by `main.tex`, and every citation
key used in the article has a corresponding entry:

`gomez_meiss_2004`, `shafikov_wolf_2003`, `hasselblatt_propp_2007`,
`bedford_kim_2008`, `favre_wulcan_2012`, `fordy_hone_2011`,
`koch_lomeli_2014`, `janeczko_jelonek_2008`, `blanc_van_santen_2022`,
`dang_favre_2021`, `el_hilany_2024`, `berger_turaev_2025`,
`bianchi_dinh_rakhimov_2024`, `grigoriev_containment`, `shao_sun_2025`,
`nisse_2026`, `takenawa_2026`, `abboud_xie_2026`, `deserti_2018`, and
`cheng_wang_yu_1994`.

The title, abstract, and exactly eight required body sections match the
publication lock.  The abstract has no citation, priority wording, or
empirical claim.  Authorship is neutral (`Anonymous`); the trio contains no
event IDs, filesystem paths, hashes, reviewer names, affiliations,
acknowledgements, private URLs, repository/process language, or provenance
breadcrumbs.  The bibliography contains only the verified records already
frozen for this candidate, and its URLs are public record links.

## Lock and manifest compatibility

The theorem scope, certified-branch qualification, positive-support and
carry hypotheses, edgewise observable-span reciprocity, one-edge margin
boundary, anti-claims, and exact fixture scope agree with
`SOURCE_LOCK.md` and `PUBLICATION_LOCK.md`.  The current main and notation
files match the source hashes recorded by `BUILD_PROFILE.md`.  Its old
references hash is the deliberately superseded pre-revision binding recorded
before R0; no build may use that stale binding.  A later authorized profile
update must bind the revised 6610-byte bibliography before any new root is
created.  This expected handoff is not a source finding and no build
authority is implied by this review.

The E0133 author-stop and E0134 authorization both record the same
pre/post 37-row manifest digest and framing (`ddf13a637b3e67c878bf83a89b73755bf3b9894274f3cd667ef7927ff9c40409`, 5321 framing bytes,
37 LF, `path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>`).  The three
current source rows above agree with that aggregate's revised source binding;
no path outside the single authorized bibliography edit was created or
modified.

No finding remains.

BATCH07_PAPER27_SOURCE_REVISION_PASS
