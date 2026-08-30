# P118 independent round-two signoff

**Role and independence.** I acted as a non-author round-two reviewer. I
inspected the settled `main.tex`, `main.pdf`, `main_round2.pdf`, Reviewer B's
round-one report, the verifier and canonical transcript, and the supporting
claim/build documents. I made no change to the manuscript, bibliography,
table, verifier, canonical output, or PDFs. This file is the only review
deliverable added by this signoff.

**Verdict: GO_INTERNAL; EXTERNAL HOLD.** Every required B-review repair is
resolved. I found no remaining mathematical, control-coverage, build, or
rendering blocker. This is an internal theorem-package verdict only; it does
not lift the explicit ownership, novelty, priority, release, or submission
hold.

## Repair-resolution matrix

| B-review item | Settled evidence | Resolution |
|---|---|---|
| False converse from part-monochromaticity to periodicity | The false sentence is absent. The settled paragraph states that a periodic graph state lies in `im Phi`, hence is part-monochromatic, and that coordinate identification on the part-monochromatic subspace intertwines `Phi` with `T`. Thus periodic graph states are exactly the lifts of the recurrent quotient list. | RESOLVED |
| Exact lift/intertwining and recurrent-state count | The part-vector lift is injective, and equation (1) gives `Phi(lift(y)) = lift(T(y))`. Therefore periodic points on that invariant subspace correspond exactly to periodic points of `T`; with Theorem 4.2 this gives `R_k=k!+2b_k` and the displayed zeta product. | RESOLVED |
| `m<g` exhaustion branch | The proof now observes that `m` occurs in the original vector but was not retained, hence occurs at least twice. At least two coordinates therefore remain, so the second image has the required repeated fill and is `x^-_{iota,m}`. | RESOLVED |
| `m=g` boundary | The proof explicitly separates at least two remaining coordinates (`x^-_{iota,g}`), one remaining coordinate (`g=k-1`, a permutation), and none (`g=k`, a permutation). | RESOLVED |
| Palette and edgeless boundaries | Section 2 states `Delta >= k-1`, so `q>=Delta+1` implies `q>=k`. Theorem 4.2 specifies the empty two-cycle sum at `k=1`, and Theorem 4.4 separately proves that every colouring of the edgeless one-part graph maps to the fixed quotient `(0)`. | RESOLVED |
| Definitions of `R`, `i_r`, and depth | Proposition 5.1 defines `R` as the complement of the image of `iota`, together with `i_r=iota(r)` and `A_R`; Proposition 6.1 repeats the local definitions before (6.2)--(6.3). Immediately before Theorem 6.2, depth is defined as the first time the graph state is part-monochromatic with quotient in `Rec_k`. | RESOLVED |
| Owner subtraction | The abstract, introduction, conclusion, README, paper plan, and narrative keep the residual claim restricted to the unconditional synchronous complete-multipartite conjunction. Faghih et al.'s distributed Grundy protocol synthesis under explicit timing models receives zero credit in both the introduction and conclusion; the bibliography renders DOI `10.23638/LMCS-14(1:12)2018`. Generic EGF and zeta machinery and the earlier local mex rule are also subtracted. | RESOLVED |
| Complete quotient controls | `verify.py` now enumerates every quotient vector in each of fifteen lanes and directly asserts `T^2(y)` lies in the displayed recurrent set. It separately asserts every listed fixed transition and both directions of every listed two-cycle, in addition to literal fibres, quotient preimages, graph-state depths, and basins. | RESOLVED |

## Independent mathematical check

The repaired transfer is exact. Every periodic point of a finite map belongs
to its image; every image of `Phi` is part-monochromatic; and on that
subspace the coordinate map is a conjugacy with the quotient update `T`.
Consequently no transient part-monochromatic vector is inadvertently counted.
In particular, the old counterexample `(2,2) -> (0,0) -> (1,1) -> (0,0)` on
canonical `K_{1,2}` is consistent with the repaired statement: `(2,2)` is
part-monochromatic but is not itself periodic.

The quotient-exhaustion proof also closes its two delicate branches. If
`m<g`, all values below `g` occur, and the missing retained value `m` must
have multiplicity at least two; if `m=g`, the number of unretained
coordinates gives exactly the repeated-fill or permutation boundary. The
standing palette assumption makes every displayed recurrent coordinate
legal, including the `k=1` case. I found no residual gap in the repaired
recurrence, fibre, or basin deductions.

## Exact verifier evidence

Fresh command:

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py

Result: **PASS, 202,965 exact assertions** over all fifteen documented
parameter lanes. Fresh stdout is 1,586 bytes and is byte-identical to
`code/verification_output.txt`; both have SHA-256
`864f9b85f7380d041b2d72a20773996f01a5459052a0b6ec47fb80a8a04c1def`.

The expanded audit loop is literal: for every quotient vector it evaluates
two quotient steps and checks membership in the independently constructed
recurrent list. It then checks every fixed state and both directed edges of
every displayed two-cycle. Thus “complete quotient graphs in every lane” is
now supported by direct transition assertions rather than inferred from the
labelled graph-state census.

## Isolated build and PDF inspection

I copied only `main.tex`, `references.bib`, and
`figures/table_k12.tex` into a fresh temporary directory and ran the four
stages `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`. All stages exited zero;
the settled fourth-pass log and BibTeX log have zero errors, unresolved
references or citations, box warnings, or rerun requests. The isolated PDF,
current `main.pdf`, and `main_round2.pdf` are byte-identical, all with
SHA-256
`d251014f4249716a77e3907cda14250b6590f376ce3d8c6aa7e832d73974a3ec`.

Mechanical and visual checks:

- 7 A4 pages, 380,381 bytes, PDF 1.5;
- 6 cited bibliography entries, all resolved and none uncited;
- 27/27 fonts embedded, subsetted, and Unicode mapped;
- empty PDF Author and Title metadata, no date fields, forms, JavaScript, or
  encryption;
- no `??`, `[?]`, `[VERIFY]`, TODO, or FIXME sentinel in source/rendered text;
- all seven pages rendered and inspected individually: equations, theorem
  blocks, cross-references, the `K_{1,2}` table, conclusion, and bibliography
  are present and legible, with no clipping, overlap, missing glyph, blank
  content page, or layout blocker.

## Final status

All Reviewer B repair gates are **RESOLVED**. P118 is signed off as
**GO_INTERNAL**. External ownership/novelty/priority assessment and any
circulation or submission remain **HOLD**.
