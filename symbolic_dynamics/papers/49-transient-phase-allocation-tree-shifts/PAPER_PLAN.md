# Paper Plan

**Plan status:** `PLAN_READY`  
**Working title:** *Hausdorff Dimension for Complete Cyclic Markov Hom Tree-Shifts with an Unrestricted One-Level Feeder or Canonical Unrestricted `L`-Level Forced Chains*  
**One-sentence contribution:** For complete cyclic Markov hom tree-shifts, we derive exact Hausdorff dimensions for the unrestricted one-level feeder and the canonical unrestricted `L`-level forced chain: integer phase allocation gives a finite max--min, constant circular convolution characterizes saturation, and balanced allocations give monotone `O(d^{-L})` convergence; explicitly declared finite-composition one-level variants are also covered, whereas restricted multilevel variants require balanced access.  
**Format:** anonymous, journal-neutral mathematical theory article  
**Layout:** A4, 11 pt, single column, standard `article` class; no conference style  
**Paper type:** pure theory with exact computational verification  
**Date:** 2026-08-21  
**Soft length target:** 18--23 pages through the conclusion, plus references and a 6--10 page proof/reproducibility appendix; no artificial venue page cap  
**Author block:** `Anonymous Authors` only; no affiliations, grants, acknowledgements, repository links, or identifying self-citations

## Narrative spine

An irreducible component need not determine Hausdorff dimension when the
unrestricted one-level feeder allocates exponentially many descendants among
different phases of a complete cyclic core.  In this family, the mechanism is
exactly finite-dimensional: fix the phase composition at the transient
frontier, count cylinders, and take the minimum over depth residues.  The
resulting max--min problem exposes a constant-convolution saturation law,
a Fourier-qualified divisibility criterion, and, for the canonical
unrestricted forced chain, a monotone finite-depth route to the spectral
mean.  A four-state example makes the mechanism visible without claiming an
arbitrary reducible theorem or an arbitrary transient-feeder theorem.

## Claims--evidence matrix

The normative matrix is `CLAIMS_EVIDENCE.md`.  The paper will carry seven
substantive claims, Q1--Q7, and one metric lemma Q0.  Every claim has a full
proof anchor, an independent audit anchor, and an explicit nonclaim.  Exact
enumerations will appear only in a reproducibility section and appendix.

## Section plan

### Abstract (180--230 words)

- Open with the exact transient phase-allocation theorem, not field-level
  background.
- State the frozen families: a complete cyclic core with positive phase
  sizes, the unrestricted one-level feeder, and the canonical unrestricted
  `L`-level forced chain on a rooted ordered `d`-ary tree.  Mention declared
  finite-composition one-level variants separately; restricted multilevel
  variants require balanced access.
- Present the complete-cyclic core formula only as the supporting calculation
  on which the transient results rest.
- Give the one-level max--min formula in words and name constant circular
  convolution as the saturation criterion.
- State the multilevel monotonicity and `O(d^{-L})` approach to the spectral
  mean.
- Close with the exact four-state values `log(2)/3` and `log(2)/2`.
- No citations, undefined abbreviations, or novelty superlatives.

### 1. Introduction (2.0--2.5 pages)

- **Hook:** the unrestricted one-level feeder can affect a boundary-weighted
  tree metric even though it contributes only one graph state.
- **Known boundary:** BLW develops irreducible Hausdorff theory and leaves the
  general reducible dimension problem open; reducible topological entropy can
  already exceed component values, as established in 2021/2022 work.
- **Gap:** neither fact yields an exact Hausdorff formula for the frozen
  transient complete-cyclic family.
- **Approach:** stratify by the integer phase composition at the transient
  frontier, count equiprobable cylinders, and retain the depth-residue
  minimum.
- Derive the complete-cyclic core formula as a supporting ingredient before
  listing the residual contributions.
- **Residual contributions:** four falsifiable bullets:
  1. the exact one-level transient phase-allocation max--min formula, including
     only the explicitly declared finite-composition one-level variants;
  2. constant-convolution saturation plus the Fourier-qualified divisibility
     criterion and mandatory nondivisible witness;
  3. closed two-phase formulas and exact monotone convergence for the
     canonical unrestricted `L`-level forced chain;
  4. the four-state Hausdorff cyclic-essential-SCC counterexample and reproducible exact
     validation.
- Place Figure 1 after the approach paragraph so a skim reader sees the
  feeder/frontier/core mechanism before notation becomes dense.
- End with scope boundaries, not a generic roadmap alone.

### 2. Related work and source boundary (1.5--2.0 pages)

- **Markov hom tree-shifts and entropy:** origin/definition sources and
  classical entropy owners, verified from primary metadata before citation.
- **Reducibility:** synthesize the 2021 and 2022 topological-entropy results;
  explicitly subtract the conceptual max-component-failure mechanism.
- **Hausdorff dimension:** position against BLW's metric, irreducible formula,
  and general upper-bound/open-question boundary.
- **Residual claim:** the present article studies complete cyclic cores with
  the unrestricted one-level feeder and the canonical unrestricted
  `L`-level forced chain.  It includes only explicitly declared
  finite-composition one-level variants; a restricted multilevel extension is
  stated only under a balanced-access hypothesis.  It neither treats
  arbitrary finite strictly transient feeder shapes nor solves the arbitrary
  reducible question, and it makes no priority claim.
- Include Table 1 comparing object class, quantity, and theorem scope; no
  “ours is first” column.

### 3. Setting, metric, and exact cylinders (2.0--2.5 pages)

- Define the rooted ordered `d`-ary tree, `Delta_n`, the BLW metric, incidence
  constraints, complete cyclic phases, the unrestricted one-level feeder,
  and the canonical unrestricted forced chain.  Isolate any declared
  finite-composition one-level variant from the principal family.
- State the equiprobable cylinder lemma Q0.
- Give the complete upper-bound cover and lower-bound Frostman argument in
  the main text, including the closed-ball interval
  `[e^{-|Delta_n|},e^{-|Delta_(n-1)|})`.
- Define `c`, `H`, the cyclic mean, weak compositions, and circular index
  conventions.
- Prove the periodic weighted-limit lemma with the backward `j-t` index.

### 4. Complete cyclic cores and one-level phase allocation (2.5--3.0 pages)

- Derive the exact root-phase cylinder product and
  `dim_H T_C=min_j H_j(c)`.
- Compute `rho(C(a))=(prod_j a_j)^{1/p}` elementarily; do not invoke a BLW
  equality.
- Define the one-level feeder and fixed ordered phase strata.
- Derive `D_1(m;c)` by exact prefix counting and the factor
  `d|Delta_(n-1)|/|Delta_n|`.
- Prove the finite union over `p^d` assignments and the max over weak
  compositions.
- State explicitly that each concentrated composition `m=d e_s` recovers
  `min_j H_j(c)` (up to a cyclic reindexing).  Consequently the feeder
  maximum dominates every core-root stratum, so this maximum is the
  Hausdorff dimension of the full one-level shift, as used in Q2 and Q7.
- Add an interpretation paragraph explaining why finite graph transience is
  not dimension-negligible in this metric.

### 5. Saturation: mean, convolution, and Fourier support (2.5--3.0 pages)

- Prove mean preservation and invertibility of the `H` kernel through its
  nonvanishing root-of-unity multiplier.
- State and prove the exact equivalence among spectral-mean saturation,
  constant circular log-convolution, and equality of shifted integer
  products.
- Separate universal sufficiency `p|d` from conditional necessity under full
  nonzero Fourier support.
- Display the `p=4,d=2,a=(2,3,2,3)` witness immediately after the qualified
  theorem.
- Give a short algebraic interpretation: arithmetic availability of a
  uniform phase composition versus degeneracy in the phase profile.

### 6. Two phases: parity and strict gain (1.5--2.0 pages)

- Derive both `p=2` formulas from the two entries of `H`.
- Treat `Delta=0` separately from the nonconstant profile.
- Prove strict feeder improvement for `Delta>0`, even-arity saturation, and
  the exact odd deficit.
- Use Figure 2 to visualize the formula for a fixed declared profile such as
  `a=(1,2)`; label it an analytic plot, not an experiment.

### 7. Deeper transient chains (2.5--3.0 pages)

- Define the canonical unrestricted `L`-level forced chain and the exact
  frontier size `N=d^L`; do not infer a result for arbitrary transient feeder
  shapes.
- Prove the fixed-composition formula `D_L`, finite optimizer `D_L^*`, and
  domination of later transient/core root strata.
- Prove monotonicity via `m -> d m`.
- State the finite-`L` constant-convolution iff and the Fourier-qualified
  divisibility consequence.
- Prove the balanced-composition bound
  `0 <= bar(c)-D_L^* <= p max_j H_j(c)/d^L`.
- State a restricted-multilevel variant only when a balanced-access
  hypothesis is imposed explicitly.
- Use Figure 3 to distinguish exact small-`L` optimizer data from the
  balanced-allocation upper certificate.

### 8. Four states and exact verification (1.5--2.0 pages)

- Display the four-state matrix in the fixed state order `(r,a,b_1,b_2)`.
- Compute the cyclic core `log(2)/3` and full shift `log(2)/2` from the
  preceding theorems.
- Explain precisely what the example refutes and what it does not establish.
- Present Table 2 with the internal and two independent audit counts/hashes.
- Describe exact rational prime-log forms and independent recursive counts;
  avoid “experimental confirmation” language.

### 9. Scope, limitations, and conclusion (1.0--1.5 pages)

- Restate the mechanism: the unrestricted one-level feeder, and iteratively
  the canonical forced chain, creates an integer phase allocation whose
  boundary descendants have asymptotic metric weight.
- Restate the exact scope: the complete cyclic core with the unrestricted
  one-level feeder, the canonical unrestricted `L`-level forced chain,
  explicitly declared finite-composition one-level variants, and restricted
  multilevel variants only under balanced access.
- List the excluded classes: arbitrary finite strictly transient feeder
  shapes, incomplete phase blocks, return edges, nontransient reuse,
  arbitrary reducible matrices, and unrestricted divisibility necessity.
- Give two concrete future questions: exact formulas for selected
  non-complete blocks, and controlled nontransient communication without an
  invalid finite-union reduction.
- State that the source search was bounded and does not establish priority.

### Appendix A. Full proof bookkeeping

- Consolidate endpoint conventions, boundary cases `p=1` and `a_j=1`, and
  the finite-union lemma.
- Repeat no main theorem wholesale; supply only deferred technical details.

### Appendix B. Exact computational verification

- State frozen input hashes, canonical domains, independent-lane separation,
  exact log-form ordering, mutation controls, and reproduction commands.
- Include no generated performance data and no claim upgrade from finite
  enumeration.

## Figure and table plan

| ID | Type | Content | Data/proof source | Priority |
|---|---|---|---|---|
| Figure 1 | Pure TikZ hero schematic | One unrestricted transient root, its `d` ordered children grouped into phase counts `m_s`, and a complete cyclic `p`-phase core; annotate the max--min formula and show that this one-level feeder fixes an exponentially replicated frontier allocation. | Frozen definitions Q1--Q2 | High |
| Figure 2 | Vector analytic plot | For `p=2,a=(1,2)`, plot core dimension, optimized feeder dimension, and spectral mean versus integer `d=2,...,12`; mark even exact saturation. | Q5 formula, generated deterministically | Medium |
| Figure 3 | Vector data plot, two panels | Left: exact `D_L^*` for selected audited profiles at `L=1,2,3` against `bar(c)`. Right: balanced-allocation gaps and the proved `p max H/d^L` certificate through `L=8`. Use line style/markers in addition to color. | `evidence/level_l.json`, source hash `cf8ae3...` | High |
| Table 1 | LaTeX scope table | BLW 2025; Ban et al. 2021/2022; present frozen family. Columns: object class, quantity, principal result, boundary relative to this paper. | Verified primary sources | High |
| Table 2 | LaTeX verification ledger | Internal, cross-audit, and root-audit counts, hashes, and role. | All three frozen inputs | Medium |

**Figure 1 caption draft.** The unrestricted one-level feeder selects an
integer composition `m` of its frontier among the cyclic phases.  Completeness then
makes each fixed allocation equiprobable, so its dimension is the minimum of
the phase-residue averages; the full feeder dimension is the maximum over
admissible integer compositions.  The diagram depicts the mechanism, not an
arbitrary reducible graph.

## Citation plan

Every bibliography entry must be retrieved from DBLP, CrossRef, the publisher,
or arXiv and cross-checked against a second trusted source.  Published versions
take precedence.

- **Introduction/Related work:** BLW 2025 (`10.1112/jlms.70198`); Ban et al.
  2021 (`10.1016/j.jde.2021.05.016`); Ban et al. 2022
  (`10.1016/j.tcs.2022.07.007`).
- **Definitions/history:** verify the primary Aubrun--Béal Markov hom
  tree-shift source and Petersen--Salama entropy sources before adding them.
- **Dimension lemma:** cite a standard mass-distribution/Frostman reference
  only if exact primary/book metadata is verified; the proof itself is
  self-contained.
- No citation will be inferred from a title alone, and no `[VERIFY]` marker
  may remain in the compiled candidate.

## Writing and notation rules

- Natural logarithms throughout; all cyclic indices are in `Z/pZ`.
- Reserve `d` for tree arity, `p` for phase period, `L` for transient depth,
  `N=d^L`, `a_j` for phase sizes, `c_j=log a_j`, and `m` for an integer
  composition.
- State assumptions immediately before every theorem and use the same names
  in captions, prose, and appendices.
- Keep proof intuition in the main text; appendices contain bookkeeping, not
  the logical heart.
- Avoid “first,” “novel,” “groundbreaking,” and generic significance claims.
- Call the code results “exact verification” or “falsification controls,”
  never experiments.

## Compile and preservation plan

- Use `\documentclass[11pt,a4paper]{article}` with `geometry`, AMS packages,
  `microtype`, `natbib`, `hyperref`, `cleveref`, `booktabs`, `tikz`, and
  `pgfplots` only if installed.
- Fix `SOURCE_DATE_EPOCH` before the first compile and record it in the build
  report.  Because `latexmk` is absent in the frozen environment, run the
  documented deterministic fallback `pdflatex`, `bibtex`, `pdflatex`,
  `pdflatex` from a clean build directory.
- Preserve `main_round0_original.pdf`, `main_round1.pdf`, and
  `main_round2.pdf`; keep the full raw GPT-5.4 xhigh reviews.
- Round 2 must continue in the same review thread as Round 1.
- Terminal state is `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`, followed by a frozen
  self-excluding manifest and explicit `STOP`.

## Plan-review gate

No section prose, figure source, bibliography, or LaTeX manuscript may be
written until an independent GPT-5.4 xhigh reviewer issues the exact token
`PLAN_READY`.  If the verdict is `PLAN_REVISE`, revise this file and request a
same-reviewer recheck.

**Gate receipt:** same-reviewer GPT-5.4 xhigh recheck returned `PLAN_READY`;
raw receipt SHA-256
`ebe20d1c4d33be751b78c7770ac28247e5bca035b7592ec744315024ae2e14ba`.
