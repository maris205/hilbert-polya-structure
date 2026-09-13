# Paper20 deterministic R1 build authorization after page-contract repair

Date: 2026-08-22 UTC

The page-fixed source has passed two fresh independent source audits.  This
note authorizes exactly one replacement deterministic R1 LaTeX build in two
fresh isolated roots, followed by read-only diagnostic validation.  It does
not authorize source edits, experiments, CAS runs, transport, publication, or
upload.

## Frozen source and authority identities

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 61,835 / 1,619 | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |
| `paper/BUILD_METADATA_R1.json` | 5,549 / 1 | `b891b8bb81d6383fc4b49fb81f41c346ecafbbd9663a25b44e7eb6bb8badf8dd` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 6,206 / 1 | `d8600e8d50efcda1b694e332a5b4282beb8b6c9ad9b5f302199f6f1aba728d3a` |

Fresh source reviews:

- `notes/INDEPENDENT_PAPER_SOURCE_R1_PAGEFIX_REVIEW.md`, 9,340 bytes / 181
  LF, SHA-256 `e83053d521542773696a59478944d8974b46b97b5b854cb7c775cc257cb2ee30`, terminal `PAPER_SOURCE_R1_PAGEFIX_PASS`;
- `notes/INDEPENDENT_PAPER_SOURCE_R2_PAGEFIX_REVIEW.md`, 9,803 bytes / 177
  LF, SHA-256 `e81e148cc8e9d4b220a62146a6bebb906df0cdb4fb5e555eca423e8ef2a8eaa5`, terminal `PAPER_SOURCE_R2_PAGEFIX_PASS`.

## Locked build

The exact four-command sequence in each root is:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The environment is exactly `HOME=/root`, `PATH=/usr/bin:/bin`,
`FORCE_SOURCE_DATE=1`, `LANG=C`, `LC_ALL=C`,
`SOURCE_DATE_EPOCH=1787356800`, and `TZ=UTC`; network access is disabled.
Only `main.tex`, `math_commands.tex`, and `references.bib` may be copied into
each initially empty root.  The persisted artifact must be named
`paper/main_round1.pdf`; the historical pre-pagefix PDF is immutable.

The substantive-body contract is minimum 22, maximum 26, planned 24 pages,
measured through the conclusion and before references.  A successful receipt
must bind both root outputs byte-for-byte and record all diagnostic counts,
font embedding, and the no-source-edit boundary.  After the build, fresh
independent build R1/R2 reviews are required before publication-stage work.

`BUILD_AUTHORIZATION_R1_PAGEFIX`
