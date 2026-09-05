# P205 Review A — source-only build and all-page viewing

2026-09-05 UTC. **ACTUAL BUILD PASS / THREE PAGES ACTUALLY VIEWED**.
This is the reviewer A build, not either future terminal Round2 build.
There was one attempt, no repair, and no change to the frozen input.

## Executed build

Working directory: `/root/autodl-tmp/symbolic_dynamics`.

```sh
bash docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/frozen_round0 /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p205_a/cold_build /root/autodl-tmp/symbolic_dynamics/papers/205-conflict-triggered-cyclic-increments/frozen_round0/main.pdf > docs/papers204_208_sequence/reviews/p205_a/build.stdout 2> docs/papers204_208_sequence/reviews/p205_a/build.stderr
```

The helper was read before execution and is pinned among supplementary
inputs. It checked that the destination did not exist, made a fresh sibling
staging directory and copied only `main.tex`, `math_commands.tex`,
`references.bib` and `sections/`. No PDF, auxiliary file, bbl, canonical or
verifier was copied as an input. There are eight source files, all pinned
in [cold_build/SOURCE_INPUTS.sha256](cold_build/SOURCE_INPUTS.sha256).

`latexmk` was unavailable; the inspected helper actually ran
pdflatex/BibTeX/pdflatex/pdflatex, with recorder output and complete pass
logs. Engine: **pdfTeX 3.141592653-2.6-1.40.22**, TeX Live 2022/dev/Debian;
**BibTeX 0.99d**. Full versions are retained in the build directory.

The actual settings were:

```text
SOURCE_DATE_EPOCH=1704067200
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
```

All four engine invocations and the helper's raw PDF `cmp` succeeded; the
combined process exited **0**. The PDF was compared against frozen Round0
before the staging directory was moved into its final review location.
The byte-identity claim concerns that actual comparison, not equal page
counts or matching text extraction alone.

## Output inspection

- [Complete build stdout](build.stdout); [stderr](build.stderr) is empty.
- [Built PDF](cold_build/main.pdf): **3 pages**, A4, **306,286 bytes**.
- SHA256: `f4aec5af74f6ab4a78e1120270e818f20b412694d9d7938145564b9b447e41cc`,
  exactly the frozen manuscript digest.
- [Final diagnostic file](cold_build/DIAGNOSTICS.txt) is empty: no final
  undefined reference/citation, overfull box or warning.
- [Font report](cold_build/FONTS.txt): all listed fonts embedded Type 1.
- [PDF metadata](cold_build/PDFINFO.txt): personal/title/creator/producer
  fields blank. The displayed author is Anonymous.
- No missing section, figure, reference or TODO/FIXME/VERIFY placeholder
  was found in the complete rendered text/source checks.

The actual three-page output meets both the task's suggested four-page
cap and the paper plan's five-total-page ceiling. No padding was requested
or added. Page count includes the complete reference list.

## Actual all-page visual review

The following render command ran with exit zero:

```sh
mkdir -p docs/papers204_208_sequence/reviews/p205_a/views
pdftoppm -png -r 140 docs/papers204_208_sequence/reviews/p205_a/cold_build/main.pdf docs/papers204_208_sequence/reviews/p205_a/views/page
```

Every resulting image was then opened using the image-viewing tool, with
the complete page visible. This is an actual viewing receipt, not a claim
inferred from the files' existence or hashes.

| Page | Actual visible content inspected | Result |
|---|---|---|
| [1](views/page-1.png) | Anonymous title, complete abstract, literal update, all four citation contexts, oriented weight definition, Theorem 2.1 start and coordinate formula | Readable; no clipping/overlap; the theorem visibly continues onto page 2 rather than being omitted. |
| [2](views/page-2.png) | Theorem 2.1 continuation, sharp bound, complete forward proof, decoder's three conditions and complete necessity/converse, static bound and Lemma 3.2 statement | Timing notation, infinity branch, equations and list are intact; proof continuity is complete. |
| [3](views/page-3.png) | Full static proof, six four-vertex values, disconnected cases, Theorem 3.3 and equality proof, limits/check scope, all four references | No missing tail or orphan reference page; bibliography DOIs are readable; bottom margin clear. |

Image SHA256 values:

```text
page-1.png a03b9d48b5543da31881314747cf67bdad7a60300f51fc2ff775b9bcd8b45be5
page-2.png 20e39fc8dba394d05ee082e20de2267e0b09d97cb42eeae8c239b8ecae79e0fa
page-3.png f8042441470099facd622880383156c38b11223465d154fbc94c883a194e0e5e
```

The theorem/lemma page breaks are ordinary continuous typesetting, not
missing proof. No layout change is requested. This build/view evidence
depends on the pinned frozen TeX/bibliography, helper, recorded engine and
environment; a future changed manuscript requires its affected build/view
and reviewer delta checks.
