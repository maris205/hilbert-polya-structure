# Paper 22 — Deterministic Build R0 Blocker

Date: 2026-08-24 UTC  
Stage: deterministic two-root R0 build  
Disposition: hard acceptance failure; no build output persisted

## Stable authorization and inputs

The live controlling gate was exactly
`PAPER22_DETERMINISTIC_R0_BUILD_OPEN`. The formal source review was:

- `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md`;
- SHA-256
  `d38343539db88d1eeda555c464657e408df6ab58aa6ad7a811cd262f53038750`;
- 17,056 bytes and 424 LF; and
- terminal line exactly `PAPER_SOURCE_R1_PASS`.

The frozen source trio was unchanged before and after both builds:

| Source path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `9e71dca521e61000d6d850c8ca090ef36a9164e50e5ec94bab033adc2f17a78e` | 69,218 | 1,921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1,928 | 55 |

All 23 pre-existing project files were rehashed after the bounded build
diagnostics and matched their pre-build identities. The pre-blocker project
inventory remained exactly 23 regular files, four child directories, and
zero symlinks.

## Two-root deterministic execution

The two fresh live roots are:

- root A: `/tmp/paper22-r0-A.PIwA2V`, mode `0700`;
- root B: `/tmp/paper22-r0-B.xwtGZQ`, mode `0700`.

Before any command, each root contained exactly `main.tex`,
`math_commands.tex`, and `references.bib`, with the frozen identities above.
Every mandated command used exactly:

`env -i PATH=/usr/bin:/bin SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C LANG=C`

In each exact working directory, the separately executed command sequence
was:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
2. `bibtex main`;
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.

The exit vector was `0,0,0,0` in root A and `0,0,0,0` in root B. Combined
stdout/stderr was captured separately as `command-1.log` through
`command-4.log` in each root.

The following required files were raw-byte identical across the two roots:

- `main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out`, and `main.pdf`;
- `command-1.log`, `command-2.log`, `command-3.log`, and `command-4.log`; and
- the three copied source files.

The common candidate PDF was SHA-256
`5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7`,
471,647 bytes. Both roots are deliberately retained for later independent
inspection and were not cleaned or deleted. Read-only page-render evidence
created after the byte-equality checkpoint exists only under root A's
`visual/` directory; it did not change any common build output, command log,
or source file.

## Bounded checks that passed

- The PDF has 26 physical pages.
- The Abstract begins on page 1; Section 8 begins on page 24; the Conclusion
  begins and ends on page 26; and References begins on page 26 after the
  Conclusion.
- The substantive Abstract-through-Conclusion span is counted as pages
  1--26, references excluded. It passes the preferred 24--28 band and the
  hard 22--30 band; the frozen target remains 26.5 pages.
- There is no appendix.
- All 28 reported fonts are embedded, subsetted, and Unicode mapped.
- The image count is exactly zero.
- All 26 pages were rendered and inspected; no blank, corrupt, clipped, or
  table-overflow page was found.
- The exact decoded PDF title matches the locked full title. Visible author
  is exactly `Anonymous`; PDF Author, Creator, and Producer are empty.
- Raw CreationDate and ModDate are both exactly
  `D:20260824000000Z`; no visible source date occurs.
- The PDF is readable, unencrypted, has no form, JavaScript, attachment, or
  embedded file, and Ghostscript nullpage processing exits successfully.
- The final build has no fatal error, unresolved citation, unresolved
  reference, label-change request, BibTeX warning/error, overfull box,
  placeholder, forbidden marker, public-identity leak, or citation-key leak.
- Exactly six bibliography entries render, matching the six frozen citation
  keys.
- Three underfull boxes remain in Table 2 at source line 944. They are
  recorded as nonblocking warnings.

## Conjunctive hard failure

The final `main.log` and `command-4.log` contain this prohibited warning:

```text
Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 1754.
```

The exact frozen source location is `paper/main.tex` line 1754:

```tex
\subsection{The \(g=2r\) seed/selected-face boundary}
```

The R0 acceptance contract conjunctively requires zero hyperref PDF-string
findings. Therefore this warning is a hard build failure even though the PDF
is otherwise deterministic, readable, correctly paginated, anonymous, and
visually intact.

The build author has no authority to edit the frozen source. A likely bounded
repair is to supply a PDF-safe subsection bookmark, for example with an
appropriate `\texorpdfstring` form, but that decision and every source edit
belong to a separately authorized parent repair stage.

## Persistence and next authority

No R0 metadata, receipt, AUX, BBL, BLG, LOG, OUT, PDF, or round-zero PDF was
persisted in `paper/`. In particular, all nine success-only paths remain
absent:

- `paper/BUILD_METADATA_R0.json`;
- `paper/BUILD_RECEIPT_R0.json`;
- `paper/main.aux`;
- `paper/main.bbl`;
- `paper/main.blg`;
- `paper/main.log`;
- `paper/main.out`;
- `paper/main.pdf`; and
- `paper/main_round0.pdf`.

This blocker is the sole project write of the failed R0 invocation. It does
not authorize a source edit, a replacement build, independent build review,
release, Paper 23, or any external effect.

Exact next authority: `none pending parent repair`.

R0_BLOCKED
