# P206 A — new cold build and actual all-page visual review

2026-09-05 UTC. **BUILD_PASS / FOUR_PAGES_ACTUALLY_VIEWED**.
This is A's own new build and new viewing, not reuse of the author receipt.
It does not override the critical value finding or count as a terminal
Round2 build.

## Actual source-only build

Read the pinned batch helper in full, then executed from workspace root:

```sh
bash docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/frozen_round0 /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p206_a/cold_build /root/autodl-tmp/symbolic_dynamics/papers/206-ternary-cyclic-record-feedback/frozen_round0/main.pdf > docs/papers204_208_sequence/reviews/p206_a/cold_build.stdout 2> docs/papers204_208_sequence/reviews/p206_a/cold_build.stderr
```

Actual observed helper exit: **0**, including its raw `cmp` against the
frozen PDF. It first copied only `main.tex`, `math_commands.tex`,
`references.bib` and the five section TeX files into a new temporary
directory. No PDF, auxiliary, bbl or former compiler log was input.
The [eight source hashes](cold_build/SOURCE_INPUTS.sha256) agree with
frozen inputs. The source-only directory was renamed to the new
`cold_build/` only after successful compilation and comparison.

`latexmk` is unavailable. The actual pinned helper uses pdfLaTeX, BibTeX,
pdfLaTeX, pdfLaTeX, all success-checked. No manuscript edit, retry or
failed build occurred. Complete pass stdout, final log, bibliography log,
recorder file, engine/environment reports and PDF text are retained.

| Check | Actual result |
|---|---|
| Engine | pdfTeX 1.40.22, TeX Live 2022/dev/Debian; BibTeX 0.99d |
| Environment | SOURCE_DATE_EPOCH=1704067200; FORCE_SOURCE_DATE=1; TZ=UTC; LC_ALL=C |
| Inputs | Eight source files; no auxiliary or PDF input |
| Final diagnostics | `DIAGNOSTICS.txt` and helper stderr empty |
| PDF | Four A4 pages, 267,983 bytes |
| Raw frozen-PDF comparison | `cmp` exit 0 |
| Fonts | All 18 listed font rows are embedded Type 1 |
| Anonymity | Visible author Anonymous; title/author/creator/producer metadata blank |
| Citations/layout | Both references resolve; no unresolved citations, placeholders, clipping or overlapping text |

PDF SHA256:
`fe69210f090939d0a0b1f284811d25a5b81c711e7d7359d11116cc1e1f11793b`.
The [PDF information](cold_build/PDFINFO.txt), [fonts](cold_build/FONTS.txt),
[full final log](cold_build/main.log) and [built PDF](cold_build/main.pdf)
are retained. The four-page total meets the paper's five-page ceiling
including references; the references are not discounted from that ceiling.

## Actual new rendering and viewing

Executed, actual exit **0**:

```sh
pdftoppm -png -r 140 docs/papers204_208_sequence/reviews/p206_a/cold_build/main.pdf docs/papers204_208_sequence/reviews/p206_a/page > docs/papers204_208_sequence/reviews/p206_a/render.stdout 2> docs/papers204_208_sequence/reviews/p206_a/render.stderr
```

The reviewer then actually opened all four full page images. The viewing
claim is based on that visual inspection, not on existence or hashes.

| Page | Content actually read | Visual result |
|---|---|---|
| [1](page-1.png) | Anonymous title/abstract; strict old-state cyclic definition; source subtraction and two-word control; both image sets; complete Theorem 2.1 statement | Clear formulas and margins; no clipping |
| [2](page-2.png) | Full temporal proof; image/core count corollary and matrices; run definition; inverse theorem and max1/max2 proof start | Proof continuity and piecewise formula intact |
| [3](page-3.png) | Max3 decoder; product and J formula; all maximizers and full proof; beginning of finite-verification scope | All equality cases visible; no overlap or omitted proof |
| [4](page-4.png) | Final verification sentence and both complete bibliography entries | Short final page is intact; references and DOI strings readable |

Image SHA256, page order:

```text
10f60b00f814b77c43884cc4c6a365086bc19e8a55668ccc867063c08fac52d0
060789e285224424ec5c223ab4d54c149865a8bc7d5a1c8b8f99b18135f591a9
b7d4329c0d29306798110e268c8514544f74f5e2e24f433ece5bf4df17c0c65d
31c076bf2b6bdead5b50401dcd8cc543c9a424c5be26d284f381692644e35a43
```

No figure-generation skill was used: these are deterministic rendered PDF
pages, not newly created illustrations. No public upload or external
manuscript transmission occurred. Scientific value remains governed by
the open finding in [REPORT.md](REPORT.md).
