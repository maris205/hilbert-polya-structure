# Paper 20 final-manuscript integrity R1 metadata correction

Date: 2026-08-22 UTC  
Project: `papers/20-coupled-shear-degree-matrix`  
Role: bounded governance-correction author

## 1. Purpose and authority

This note corrects two measured metadata fields in the retained review
`notes/FINAL_MANUSCRIPT_INTEGRITY_R1.md`. It neither edits nor replaces that
historical file. It changes no theorem, source, bibliography, PDF, build
receipt, source lock, publication lock, prior review, title, or external-effect
boundary. No compilation, BibTeX, scientific execution, network access,
transport, submission, upload, public hosting, repository push, external
message, or identity disclosure was performed.

The retained review has exact live identity:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `notes/FINAL_MANUSCRIPT_INTEGRITY_R1.md` | `181159fa04aa03fa1c8ba4dd92f08061e6d112b6b1555faf30e5d54e04f8eaf1` | 8,635 | 152 |

Its terminal line `FINAL_MANUSCRIPT_INTEGRITY_PASS` remains historical
read-only evidence that the manuscript/build package passed its stated gate;
as that review itself says, it grants no release or downstream external
effect.

## 2. Exact superseding correction

The frozen-identity table in the retained review assigns the correct SHA-256
but incorrect size and LF count to
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`. Direct byte readback gives:

| Field | Retained incorrect value | Authoritative live value |
|---|---:|---:|
| bytes | 9,484 | 8,742 |
| LF bytes | 213 | 161 |
| SHA-256 | `937612e3810c99eda8e9499abaa188b1d5b4d8421c7d8c260188d2d4b1481e02` | `937612e3810c99eda8e9499abaa188b1d5b4d8421c7d8c260188d2d4b1481e02` |

The review file exists as a regular non-symlink file and its last nonempty
line is exactly `PUBLICATION_STAGE_PASS`. Every later inventory, lock,
manifest, receipt, dashboard, or terminal review must use the authoritative
live values 8,742 bytes and 161 LF. The two incorrect numbers above are
retained only as disclosed historical transcription errors and may not be
promoted as evidence.

## 3. Frozen title and artifact lineage

The rendered public title is exactly:

> Coupled Hamiltonian Shear Degree Matrices in A4: An Asymmetric g>=5 Family

The TeX source displays `A^4` and `g\geq 5`; the ASCII rendering above is only
the governance-safe text form. The shorter PDF metadata title is exactly
`Coupled Hamiltonian Shear Degree Matrices in A4`. Earlier discovery wording,
if different, is superseded by this frozen rendered title and must be
disclosed as historical rather than silently reused.

The authoritative source trio remains:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` | 61,835 | 1,619 |
| `paper/math_commands.tex` | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` | 702 | 20 |
| `paper/references.bib` | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` | 2,335 | 73 |

The sole reviewed final candidate input is `paper/main_round1.pdf`, SHA-256
`07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40`,
429,723 bytes, 2,338 LF, and 23 pages. Existing `paper/main.pdf` and
`paper/main_round0.pdf` are byte-identical historical R0 artifacts at
`ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9`,
380,574 bytes, 2,049 LF, and 14 pages. They are not final candidates and may
not be substituted for `main_round1.pdf`. The retained failed pre-pagefix PDF
is likewise historical and non-authoritative.

## 4. Stop condition

This correction authorizes no source or PDF edit and no build, finalization,
candidate copy, release manifest, terminal receipt, cleanup, or terminal
review by itself. Any such local-only work requires its own exact governance
scope and independent gates. All external effects remain false.

FINAL_MANUSCRIPT_INTEGRITY_METADATA_CORRECTION_AUTHOR_STOP
