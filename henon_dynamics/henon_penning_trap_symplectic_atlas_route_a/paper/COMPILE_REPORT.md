# Deterministic LuaLaTeX compile report

Status: **PASS**.

## Build contract

- Engine: LuaLaTeX
- Fixed environment: `SOURCE_DATE_EPOCH=1788220800`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`
- Fixed hexadecimal trailer ID in the retained source
- Two passes per fresh build
- Two independent fresh builds per revision round
- Settled-log status: warning-free; forbidden-pattern count 0 for all six builds
- Final font rows: 17; all embedded and subset
- `main.pdf` is byte-identical to `main_round2.pdf`
- The claim-local formal citations and no-proof-outsourcing boundary are
  confined to round 2; fresh round-0 and round-1 hashes remain unchanged.

## Artifacts

| Artifact | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 3 | 122,323 | `ff97af92b8e5eb9c75ac232176f733bddeaf2e3c45c9b5861d970fda67c440c2` |
| `main_round1.pdf` | 3 | 125,283 | `4624322756d44a9db0a26ef23b2a7c55f797dd62c1dce2deb4a1d979b226fada` |
| `main_round2.pdf` | 4 | 151,830 | `960afb3c5ec99cbd320a033c72affbc3cde357b0fe4b4cee6c741de773df9d42` |
| `main.pdf` | 4 | 151,830 | `960afb3c5ec99cbd320a033c72affbc3cde357b0fe4b4cee6c741de773df9d42` |

For each row, fresh build 1 and fresh build 2 produced the displayed digest.
The three revision hashes are pairwise distinct.

## Settled-log gate

Each second-pass log was searched for

```text
LaTeX Warning
Package ... Warning
Overfull
Underfull
undefined references
Rerun to get
Missing character
```

No match was found.  `pdfinfo`, `pdffonts`, and `pdftotext` succeeded; visual
inspection of all four final pages found no clipping, collision, or missing
glyph.

## Reproduction form

Each fresh build uses the equivalent of

```bash
lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{2}\input{/absolute/path/to/paper/main.tex}'
lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{2}\input{/absolute/path/to/paper/main.tex}'
```

Replace `2` by `0` or `1` for the earlier archived revisions.  Build sidecars
remain outside the release directory.
