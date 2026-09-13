# Paper 21 Deterministic R0 Blocker Record

Date: 2026-08-22 UTC

Status: `R0_BLOCKED`

This record is historical and grants no build, release, transport, or external
authority. It records the first deterministic build attempt of the source trio
below.

## Bound source

- `paper/main.tex`: SHA-256
  `c3d34411f3012a446238c098a10e1f76258236a5d0b6da91f7b01475633c1e86`,
  67,605 bytes, 1,554 LF.
- `paper/math_commands.tex`: SHA-256
  `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a`,
  981 bytes, 33 LF.
- `paper/references.bib`: SHA-256
  `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8`,
  675 bytes, 19 LF.

The effective source reviews were replacement R1 SHA-256
`135657999f99081f4eb92a35f3b017b87349c0a85de4e75526f48e52a287c6e5`
ending `PAPER_SOURCE_R1_REPLACEMENT_PASS`, and R2 SHA-256
`0aca263b6836f899c134e887f9cc4979f93ab966132eb7d5c74bb1157cf501f6`
ending `PAPER_SOURCE_R2_PASS`.

## Deterministic procedure

Two independent `mktemp` roots each received only the three bound source
files. Both roots used:

```text
SOURCE_DATE_EPOCH=1787356800
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
LANG=C
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The two roots agreed byte for byte on every stable generated output:

| Output | SHA-256 | Bytes |
|---|---|---:|
| `main.aux` | `e9e6ce749505f712e1c7f4b0339c9cedd1dcee77b88ea6be2161121cdbdcb75f` | 10,368 |
| `main.bbl` | `1be6c9b14cae6da54ed8ab04d9739d0bb02ccc363f52ac6ad69b2c2dcf19a1de` | 731 |
| `main.blg` | `4ef0e5c28c45d31e9cd0f4459679b0a06bfaa2555498a2f87c6b6e68f588d804` | 885 |
| `main.log` | `d69250da39c1efb7b2755f14cda6a5035fdc0f395dbd6c2f947315592a9b7008` | 29,763 |
| `main.out` | `6cd460dec1bb409d6278753c3cef2b128c6e2162eeaedd6c3a798d52be443e3b` | 3,804 |
| `main.pdf` | `b004e961ea4184b222c98bbafff217fbff78b5e95c7b2a359757ee67b665a100` | 440,506 |

## Validation result

- PDF metadata title is exactly `Three-Mode Hamiltonian Shears in A6: Exact
  Degree Growth and Cubic Perron Subfamilies` and author is `Anonymous
  Authors`.
- The PDF is unencrypted, letter size, version 1.5, and has 21 pages.
- All 25 listed fonts are embedded, subsetted, and Unicode mapped.
- No fatal error, undefined reference, undefined citation, unresolved marker,
  `TODO`, `FIXME`, or `VERIFY` string was found.
- The log contains two underfull boxes and two overfull boxes. The overfull
  widths are 0.4714 pt at the displayed matrix ending near source line 597 and
  26.77045 pt at the displayed row-sum differences ending near source line
  1405.
- The conclusion reaches page 21 and the references begin on that same page.
  The locked plan requires 24--29 substantive pages, targeting 26.0.

Determinism and basic PDF hygiene therefore pass, but the substantive-page
contract and zero-overfull requirement fail. No PDF from this attempt is a
release candidate. The only permitted continuation is a bounded proof-first
source repair, followed by fresh source review before another deterministic
build.

`R0_BLOCKED`
