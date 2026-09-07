# C416 author handoff

Date: 2026-09-07. Status: AUTHOR_DRAFT_READY_FOR_INDEPENDENT_MANUSCRIPT_REVIEW.
The full anonymous English article and author-side PDF are complete.
This status does not certify the pending nonauthor manuscript review,
formal evaluation, two fresh deterministic final builds or release.

## Deliverable and exact contract

- [Article source](main.tex), [author PDF](main.pdf),
  [bibliography](references.bib), [citation audit](CITATION_AUDIT.md).
- Exact factorial-product $s_d$, every odd $d\ge3$, all rational
  points in $\mathbb Q^2$, ordinary primitive cycles modulo rotation only.
- One substantive section per source file: eight body sections and
  the complete affine-table appendix, plus shared mathematical macros.
- The headline census, three total formulas and the native finite-cycle
  zeta are in Section 1. The zeta is a corollary, not a new contract.
- No AI illustration or artificial numerical experiment was introduced.

## Claim-to-proof map

| Material | Included article location |
|---|---|
| Strict prime-adic dominance, integrality of every rational cycle | Proposition 3.3 |
| Binomial generating identity, exact boundary values, second-difference induction and integer escape | Lemmas 3.1–3.2 |
| Affine recurrence, all proper-divisor linear tests and 17 actual central points | Proposition 4.1 and Appendix A / Table 8 |
| Exact arithmetic-progression clipping and cycle-count division | Equations (4.5)–(4.6), Table 4 |
| Negative-phase point conversion, ordinary periods and the central phase change | Proposition 5.1, including $g_-^n(Cz)=C S^n g^n z$ |
| Signed ordinary lift, all free strips, exact endpoint complement, 30 exceptional/surviving start states, escape transients | Section 6 / Tables 5–6 |
| Least-radius no-alias proof | Lemma 6.4 |
| Every boundary cycle and every escape branch in all three radius classes | Sections 7.1–7.3 |
| Unique growing cycle with q+1 time-2 edges, q time-6 edges and negative closure sign | Proposition 7.1 |
| Global exhaustion, empty least-radius progressions, totals and return law | Section 8 / Table 7 |

The accepted proof's precision corrections remain explicit: the negative
phase converts actual point labels; the endpoint list is the exact
complement of the generic strips; the least radii are covered; signs
double ordinary time when required; repeated periods across disjoint
tables are added. KKPS's entire positive-phase bulk/17-exception result,
rational box and growing-cycle existence are deducted in Section 2.
Its version header and internal date are separated; its numerical
inconsistency is not attributed to an unexamined journal version.

## Actual author checks

The fresh author output directory was build_author/. The actual
command, from this paper directory, was:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build_author main.tex
~~~

Environment: Latexmk 4.76; pdfTeX 3.141592653-2.6-1.40.22;
TeX Live 2022/dev/Debian; BibTeX 0.99d. This is an author-side build
with ordinary environment timestamps, not either required final
deterministic build.

The initial invocation exited 0 after resolving references/BibTeX and
produced 15 pages. It exposed six caption-anchor warnings and three
math-in-bookmark warnings. These were fixed by explicit hypcap=false
for nonfloating captions and texorpdfstring for the three radius
headings; the next invocation exited 0 with no remaining warnings.
Text inspection then found that the first table's caption was separated
from its table at a page break. All six inline tables were grouped
with their captions in minipages. The final affected rebuild exited 0.

Final author PDF:

- 15 pages, letter size, 11pt article with one-inch margins.
- 338,861 bytes.
- SHA256: f231bbe134f43fed0ceee0f858f36f235f4e6ccd54e2f3914d2154e11e65c2dc.
- Final build_author/main.log and main.blg: zero warnings,
  undefined references/citations, overfull/underfull messages or errors.
  The literal rg warning search exits 1 because it finds no matches,
  not because compilation failed.
- pdffonts reports 20 font entries, all embedded/subset with Unicode
  maps, all Type 1; no Type 3 fonts.
- pdftotext -layout produced build_author/main.txt; title,
  mathematical sections, all tables and both references are present.
- All 15 pages were rendered with pdftoppm -png -r 96 and actually
  viewed individually. No clipping, overlapping text or detached
  captions remained. Page 15 contains the two references with ample
  remaining whitespace; no arbitrary page target was imposed.
- The source inputs, including all body/appendix files, were written
  and author-read for the reverse outline. The paper proceeds from
  exact theorem to arithmetic reduction, clipped cells, phase transfer,
  signed returns, exhaustive routing and ordinary-count closure.

A separate read-only new-manuscript transcription check compared the
TeX data against the frozen proof's Markdown data, without executing
any frozen mathematical code. It passed:

~~~text
bulk 36/36
strips 12/12
endpoint display rows 29/29 (30 start states)
11 TeX files
52 unique labels; 72 resolved reference uses
2 cited bibliography entries
all input paths exist; no placeholders
~~~

The first version of this one-off parser also selected table headers
and failed its comparison; restricting it to numeric data rows fixed
the parser. No mathematical table value had to be changed. The later
minipage edit did not change any table data, labels, references or
bibliography keys, so that data-transcription receipt remains applicable.

## Pending gates and boundaries

The coordinator's nonauthor full TeX/Bib/PDF manuscript review is pending.
The accepted frozen proof review is not substituted for this new
transcription/readability gate. Further final builds, evaluation,
exact release manifests and Git integration belong to the coordinator.
No unresolved mathematical assumption was knowingly introduced; the
bounded novelty/source-access limitations remain as stated.

Only this allocated paper directory was written. The frozen research
tree, mapping-class reserve, other paper directories, global indexes,
evaluations and Git were untouched. No old certificate or numerical
degree graph was rerun. The result remains a source-cycle classification:
no target Euler factors, root number, automorphy, target divisor or
Hilbert–Pólya claim is made.

The paper-write and paper-compile skills influenced modular proof
coverage, explicit source ownership, actual compilation, warning repair
and PDF inspection. The shared batch's anonymous mathematical-article
format and current-team review rule replaced unrelated legacy
conference/named-external-review defaults; no external review is claimed.

