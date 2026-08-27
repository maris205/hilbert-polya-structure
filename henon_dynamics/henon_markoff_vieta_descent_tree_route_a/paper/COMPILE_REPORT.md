# C193 compile report

Status: PASS.

## Frozen build

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Source epoch: `1787702400`; `FORCE_SOURCE_DATE=1`; `TZ=UTC`.
- Build: two successful LuaLaTeX passes per frozen artifact.
- Page geometry: A4, 595.276 by 841.89 points.

## Actual revision ledger

| artifact | pages | bytes | SHA-256 | substantive increment |
|---|---:|---:|---|---|
| `main_round0_original.pdf` | 2 | 130,820 | `ac9328bd627d43431def6772e6434341d0cb8e3a37d46e39fcf335309d20b0e9` | Vieta invariance, root identities, unique maximum, and strict parent descent |
| `main_round1.pdf` | 2 | 130,835 | `86af8b8d410519377158081fd28416079617618b79da38762118cb807702af1e` | finite termination, reverse generation, unique parenthood, rooted-tree theorem, and recurrence distinction |
| `main_round2.pdf` | 2 | 130,852 | `7dd5274a024a51df47bbcb67e57e8efbae0b672ee76c3a1ddf73ce96e1f42b06` | source ownership, independent evidence ledgers, Frobenius/modular firewall, and exact Route-A stop |
| `main.pdf` | 2 | 130,852 | `7dd5274a024a51df47bbcb67e57e8efbae0b672ee76c3a1ddf73ce96e1f42b06` | byte-identical release copy of round 2 |

The three revision hashes are pairwise distinct.  The source was revised and
recompiled between rounds; the PDFs are not macro-only relabelings.

## Independent deterministic rebuilds

Two fresh temporary directories, each seeded only with final `main.tex`, were
built twice at the frozen epoch.  Both output hashes were
`7dd5274a024a51df47bbcb67e57e8efbae0b672ee76c3a1ddf73ce96e1f42b06`;
both files were byte-identical to `paper/main.pdf`.

## Release checks

- The second-pass logs for final, round zero, round one, and round two contain
  no warnings, undefined references, missing characters, overfull or
  underfull boxes, fatal messages, or errors.  Both fresh-build final logs are
  likewise clean.
- `pdffonts` reports every listed font embedded and subsetted.
- Text extraction preserves both abstracts, all formulas, the strict Route-A
  tuple, the Frobenius and modular boundaries, declarations, and all three
  verified DOI references.  It contains no `??`, `[?]`, or `[VERIFY]` marker.
- Both rendered pages were inspected at 140 dpi: no clipping, collision,
  overlap, broken glyph, or illegible equation was found.  A visual audit
  exposed a literal `qquad`; the missing backslash was repaired before the
  frozen final build, and both pages were reinspected.
