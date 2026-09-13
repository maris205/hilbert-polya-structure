# Paper20 independent manuscript-source review (R2, BibTeX repair)

**Review ID:** `PAPER_SOURCE_R2_BIBFIX_2026_08_22`

This is a fresh read-only review of the author-stopped citation-only revision.
It supersedes neither the prior review records nor their historical hashes; it
applies only to the identities below.  No compilation, BibTeX run, CAS,
experiment, transport access, upload, or author-file edit was performed.

## Exact source identities

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 37,423 | 981 | `2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014` |
| `paper/math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 | 73 | `5cc0a88c3792b945ab6181ed1e83659c6d5251e172fa4885453b90c8dee15a2c` |
| `paper/BUILD_METADATA_R0.json` | 3,588 | 1 | `fd03d826bc9e65d0b578de5fce0a6b029bd38196d561e4b092aac2cfb77bd675` |

The source lock is unchanged at SHA
`57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`,
11,847 bytes/LF1, and the plan remains
`4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3`,
22,064 bytes/LF397.

`BUILD_METADATA_R0.json` is strict-canonical JSON (UTF-8, LF1, no CR/NUL/BOM,
duplicate-key and nonfinite-number rejection, recursive Unicode-key ordering,
byte-exact roundtrip).  Its only changed source binding is the expected
`references.bib` row (2,335 bytes and the SHA above); the main, notation, and
plan rows match their files.  Self-identity fields are null and the metadata
continues to report build/CAS/experiment/figure/publication/transport/upload
as unauthorized, with planned build `NOT_RUN` and null artifacts.

## BibTeX repair and citation integrity

The repair is limited to the two titles containing `\(\mathbb C\)^k` and
`\(\mathbb C\)^2`, now protected as BibTeX/TeX math fragments
`{$\\mathbb C$}^k` and `{$\\mathbb C$}^2`.  The seven entry keys are unique:

`FriedlandMilnor1989`, `Deserti2018`, `GuedjSibony2002`,
`FavreJonsson2011`, `DangFavre2021`, `Fujioka2023`, and `HenonSurvey2024`.

The bibliography has balanced braces and quotes, LF-only bytes, and no NUL or
BOM.  Every citation key used by the unchanged `main.tex` resolves to exactly
one entry.  The locked citation roles remain bounded context only: planar
degree-product background, higher-dimensional degree-growth terminology,
spectral/dynamical-degree context, historical valuation context, and the
four-dimensional coupled-Hénon neighbor.  No citation is promoted to proof,
priority, or firstness evidence.

## Unchanged theorem and source gates

`main.tex` is byte-identical to the passed repaired source.  Therefore the
numbered selector-gap equations, removal of the obsolete `eq:ratiomap` label,
and all 40 unique resolved labels remain valid.  The independently replayed
L1--L7 proof remains unchanged: triangular symplectic inverses; literal
support rows (A_g,B_g); the two-phase cone
(1\le u_2/u_1<(g-2)/2); carried-term gaps and positive-coefficient
no-cancellation; (u_{n+1}=C_gu_n) and (q_2) visibility; and Perron roots
((\sqrt g\pm1)^2) with the strict comparison to ((g-1)^2).

The P12--P19 collision boundary and anti-claims remain narrow and bounded.
No generic Newton-fan, arbitrary-support, positive-characteristic,
topological/arithmetic entropy, period/trace/torus, universal-conjugacy,
numerical, or CAS claim is introduced.  No forbidden build or transport output
is present.

## Verdict

`PAPER_SOURCE_R2_PASS`

The BibTeX-only revision is hash-consistent, syntactically well-formed at the
source level, citation-resolved, and does not alter the passed theorem or
permission boundaries.  This receipt authorizes no compilation, publication,
transport, experiment, or downstream artifact.
