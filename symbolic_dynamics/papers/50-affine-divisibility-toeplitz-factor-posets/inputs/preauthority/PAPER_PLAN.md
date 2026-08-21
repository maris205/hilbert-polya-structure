# Paper plan

**Working title:** *Affine Divisibility Toeplitz Systems: Constructive Periods and Same-Base Pointed Factor Posets*  
**One-sentence contribution:** For the explicit affine family
`x_{p,u}(k)=u_{nu_p((p-1)k+1)}`, with constructiveness defined by the
all-coordinate finite-block convention using Hosseini--Yassawi terminology,
the article determines the exact skeleton and
prime/composite dichotomy, proves that every onto pointed factor between
systems at the same fixed base and within this family is a unique letter
quotient, and identifies its target classes modulo pointed conjugacy with
independent-set partitions ordered by refinement.  
**Format:** anonymous, journal-neutral, A4, 11-point, one-column mathematical
theory article; no conference style.  
**Audience:** symbolic dynamics, topological dynamics, Toeplitz flows, and
finite combinatorics.  
**Date:** 2026-08-21.  
**Length target:** 17--20 pages of main text, 2--3 pages of references, and
3--5 pages of appendices; this is a planning target rather than a venue cap.  
**Status:** `AWAITING_GPT54_XHIGH_PLAN_REVIEW`; no manuscript body may be
written before `PLAN_READY`.

## Story and framing

The paper tells one story: a single affine divisibility coordinate makes a
fixed-base pointed factor problem inside this family rigid.  The same coordinate gives
one-hole skeletons, separates prime from composite bases under the
constructive-period convention, and creates high centers whose off-center
windows do not depend on the directive index.  Curtis--Hedlund--Lyndon then
collapses every pointed local rule to a letter quotient.  The quotient
kernels form a graph-theoretic refinement poset.

The abstract, introduction, and Figure 1 must expose that chain before any
long proof.  The article will not claim that general Toeplitz factor maps
have radius zero: it will place the result as an explicit specialization of
the aligned-symbol criterion of Downarowicz--Kwiatkowski--Lacroix.  It will
credit Hosseini--Yassawi for constructive period structures and their
cross-base obstruction while keeping all cross-base sufficiency out of
scope.

## Claims--evidence backbone

The frozen matrix is `CLAIMS_EVIDENCE.md`.  The four contribution-level
claims are:

1. exact one-hole skeletons, essential powers, normal simple-Toeplitz form,
   and aperiodicity for every integer base `p>=3`;
2. constructive initial blocks exactly at prime bases, with an explicit
   strict counterperiod for every composite base;
3. arbitrary-radius collapse of all onto, same-base pointed factors between
   systems in the affine family to unique surjective letter quotients;
4. classification, modulo pointed conjugacy, of in-family pointed factor
   targets by admissible graph partitions, with refinement arrows and
   graphical enumeration formulas.

Deterministic finite checks are a fifth, supporting reproducibility item,
not a mathematical contribution and not evidence for infinite quantifiers.

## Planned theorem spine

1. **Affine nonvanishing and coordinate periodicity lemma.**  Show
   `(p-1)k+1` is never zero and that a coordinate of exponent `e` has period
   `p^(e+1)` without using field inverses.
2. **Exact-skeleton theorem.**  Prove
   `Per_{p^N}(x)=Z\(r_N+p^N Z)` by both inclusions; use `r_N` and
   `r_(N+1)` to exclude the alleged hole progression.
3. **Simple-Toeplitz and essential-period corollary.**  Exhibit the nested
   one-hole filling, prove no residual integer hole, and deduce
   aperiodicity.
4. **Constructiveness theorem.**  Give the universal upper period,
   prime congruence witness for every improper common period, and composite
   counterperiod `ell p^N` for all translates, including the exponent-`N`
   coordinate.
5. **High-center lemma.**  Freeze all off-center radius-`R` letters for
   `n` above the finite exponent threshold.
6. **Pointed-factor theorem.**  Apply CHL at arbitrary radius, define the
   directive letter map from high-center windows, extend from large indices
   using directive periodicity, extend from the distinguished orbit by
   density, and prove surjectivity and uniqueness.
7. **Conjugacy corollary.**  Use the pointed inverse to obtain bijective
   relabeling.
8. **Partition-poset theorem.**  Identify kernels with independent-set
   partitions; prove the arrow direction `P refines Q`; quotient directives
   are reduced to least period.
9. **Graphical enumeration corollary.**  Derive graphical Stirling counts,
   chromatic number, the bipartite criterion, and the falling-factorial
   expansion.

## Section plan

### Abstract (180--220 words; about 0.4 page)

- Begin with the explicit family and the complete classification, not with
  generic symbolic-dynamics background.
- State the four main results with their quantifiers.
- State the scope bundle at first use: same fixed base, onto pointed maps,
  source and target both in the affine family, target classes modulo pointed
  conjugacy, and the all-coordinate finite-block constructive convention.
- Explain the mechanism in one sentence: one-hole congruences create high
  centers that collapse CHL rules.
- Give exact theoretical objects rather than experimental numbers.
- Mention deterministic checks only as a reproducibility supplement.
- No citations or undefined acronyms.

### 1. Introduction (about 2 pages)

- Opening: pointed Toeplitz factor maps over zero at a fixed period base are
  naturally described by aligned blocks; ask when the explicit affine
  one-hole family forces those blocks to collapse to letters.
- Introduce the affine formula at once and state why composite bases require
  care.
- In the first theorem preview, spell out the entire scope bundle: one fixed
  base, onto pointed maps, source and target inside the affine family,
  target classes modulo pointed conjugacy, and constructiveness under the
  all-coordinate finite-block convention.
- State the one-sentence contribution before technical background.
- Give exactly four contribution bundles: `{C1}`, `{C2}`,
  `{C4 proved via C3}`, and `{C5--C6}`.  Label C7 separately as
  reproducibility support and never as a theorem contribution.
- Preview Figure 1 and the prime/composite split.
- State the same-base pointed scope and major nonclaims before the roadmap.
- Citations: DKL95 for aligned symbols; Hosseini--Yassawi for constructive
  period structures; verified classical/simple-Toeplitz references for
  context.

### 2. Toeplitz factor criteria and the residual question (about 1.5 pages)

- Organize by problem, not paper-by-paper summary:
  1. period structures and one-hole/simple-Toeplitz constructions;
  2. pointed homomorphisms over the odometer zero and aligned symbols;
  3. constructive pure-power obstructions.
- Include a scope table comparing hypotheses, map quantifiers, conclusion,
  and what remains after owner subtraction.
- State that bounded source search licenses no priority language.
- End with the exact owner-subtracted residual question: for this affine
  divisibility family at one fixed base, when does every pointed over-zero
  aligned-symbol factor collapse to a unique letter quotient?

### 3. The affine family and conventions (about 2.5 pages)

- Define subshifts, pointed factor maps, position periods, skeletons,
  essential periods, period structures, and the all-coordinate finite-block
  convention.
- Freeze `p>=3`, exact-support periodic directives, least period `h>=2`, and
  unequal cyclic neighbors.
- Emphasize that `nu_p` is a divisibility exponent at composite bases and is
  never applied to zero.
- Define `r_N`, the cyclic adjacency graph, admissible partitions, and
  refinement.
- State a single consolidated main theorem, followed by a dependency map.

### 4. Skeletons and constructive periods (about 4 pages)

- Prove coordinate periodicity and the exact skeleton in full.
- Deduce essential powers, normal simple-Toeplitz recursion, and
  aperiodicity.
- Prove the universal finite-block upper period.
- Split the constructiveness proof into the prime congruence lane and the
  composite counterperiod lane; quantify all integer translates.
- Include Figure 2 immediately before or after the split theorem.
- Add a short boundary paragraph for `p=3`, composite divisibility, and the
  alternate zero-coordinate convention.

### 5. High centers and pointed factor rigidity (about 4 pages)

- Prove the high-center identity, including negative offsets.
- State CHL precisely and pad to a symmetric radius.
- Display the stabilized high-center window.
- Define `lambda` from local-rule values, prove independence from directive
  occurrence, extend to all indices using the lcm of directive periods, and
  extend equality to the orbit closure.
- Prove onto and uniqueness from exact target support.
- Treat radius zero explicitly and state why pointedness and same-base scope
  cannot be dropped.
- Conclude with the conjugacy characterization.

### 6. The pointed factor poset (about 3.5 pages)

- Define kernels of letter quotients and prove admissibility iff blocks are
  independent in the cyclic adjacency graph.
- Show quotient directives retain exact support, unequal cyclic neighbors,
  and least period at least two after reduction.
- Prove pointed-conjugacy classes correspond exactly to kernels.
- Prove arrows correspond to refinement in the stated direction and are
  unique; call the quotient a poset and explicitly avoid a lattice claim.
- Derive `S_G(k)`, `chi(G)`, binary iff bipartite, and
  `P_G(q)=sum_k S_G(k)(q)_k`.
- Work through the `C_4` directive example and Figure 3.

### 7. Exact examples and proof diagnostics (about 1.5 pages)

- Example A: prime base `p=3`, first hole residues, and the next-power block
  period.
- Example B: composite base `p=4`, strict period `2*4^N`.
- Example C: directive `(0,1,2,3)` and the four-node diamond factor poset.
- Present a compact table of deterministic check counts read from frozen
  JSON.  Label every row “finite falsification control.”
- Explain two independent evaluators and typed mutations without calling
  them experiments.

### 8. Scope and conclusion (about 0.75 page)

- Rephrase the arithmetic-to-categorical chain without copying the
  introduction.
- State limitations: same base, pointed maps, periodic exact-support
  directives, and in-family targets.
- Give concrete future questions: nonzero odometer phases and cross-base
  sufficiency, explicitly separated from the proved results.
- Make no priority or submission claim.

### Appendix A. Boundary conventions and alternate indexing (1--2 pages)

- Record the finite-block convention cleanly.
- Give the `k=1` replacement for the prime witness if coordinate zero is
  omitted literally.
- Collect radius-zero, negative-offset, exact-support, and least-period
  boundary checks.

### Appendix B. Deterministic verification protocol (2--3 pages)

- List the two evaluator algorithms without copying candidate source.
- Bind all evidence tables to input JSON hashes.
- Document bounds, exact counts, mutations, and the limitation of finite
  verification.
- Give a one-command fixed-input rerun path inside the writer candidate only;
  do not write or modify frozen inputs.

## Figure and table plan

| ID | Type | Content and comparison | Reproducible source | Placement |
|---|---|---|---|---|
| Figure 1 | Two-panel TikZ hero | (a) nested single-hole skeletons `H_N superset H_(N+1)` with successive letters; (b) a radius-`R` high-center window whose off-center labels are fixed while the center is `u_n`, ending in a unique letter map. It visually connects the two proof mechanisms rather than comparing empirical methods. | `figures/fig1_mechanism.tex`, compiled from TikZ only. | Introduction. |
| Figure 2 | TikZ arithmetic dichotomy | Prime lane: every improper `q=p^j d` is killed at a center by a mod-`p^2` witness. Composite lane: `ell p^N<p^(N+1)` preserves every block coordinate. The caption must call this a schematic proof map, not evidence. | `figures/fig2_constructive_split.tex`. | Section 4. |
| Figure 3 | TikZ Hasse diagram | For directive `(0,1,2,3)`, show the `C_4` adjacency graph and the four admissible partitions in a diamond ordered from fine to coarse. | `figures/fig3_c4_poset.tex`. | Section 6. |
| Table 1 | LaTeX source-scope table | Compare DKL95, Hosseini--Yassawi, and the present frozen theorem by period hypotheses, pointedness, base relation, and conclusion. The present row must say: one fixed base, onto pointed maps, both objects in the affine family, target classes modulo pointed conjugacy, and all-coordinate finite-block constructiveness. Its conclusion is the in-family collapse of pointed over-zero aligned-symbol factors to unique letter quotients. No “first” row or novelty ranking. | `figures/table1_owner_scope.tex`; metadata from verified primary records. | Section 2. |
| Table 2 | Generated LaTeX proof-diagnostic table | Exact candidate, reciprocal, and root-audit counts, with input hash and “finite falsification control only” label. | `figures/gen_diagnostic_table.py` reading a checked JSON receipt derived from frozen evidence. | Section 7 / Appendix B. |

All figures must work in grayscale, contain no decorative titles, use
self-contained captions, and remain legible at the intended width.  There
will be no raster or AI-generated imagery and no invented data.

## Citation scaffold

Every entry must be fetched or verified from a primary publisher, DOI,
DBLP, CrossRef, or arXiv record before entering `references.bib`.

- **Introduction:** Downarowicz--Kwiatkowski--Lacroix (1995);
  Hosseini--Yassawi (published 2026); Gjerde--Johansen (2000), DOI
  `10.1017/S0143385700000948`, for Toeplitz period-structure context.
- **Section 2:** DKL95; Hosseini--Yassawi; Gjerde--Johansen on
  Bratteli--Vershik models; Downarowicz--Durand on factors of Toeplitz flows;
  one verified simple-Toeplitz combinatorics source if it supports the exact
  contextual claim.
- **Section 3:** G. A. Hedlund, “Endomorphisms and automorphisms of the
  shift dynamical system,” *Mathematical Systems Theory* 3 (1969),
  320--375, DOI `10.1007/BF01691062`, for CHL; DKL95 for the standard
  position-period, skeleton, and Toeplitz terminology used in the same
  factor setting; Gjerde--Johansen, DOI `10.1017/S0143385700000948`, for
  Toeplitz/Bratteli--Vershik period-structure context.  Definitions specific
  to the affine family need no citation.
- **Sections 4--6:** cite only dependencies or terminology owners; theorem
  proofs are self-contained.
- **Section 7 / appendix:** cite the frozen audit artifacts by internal hash,
  not as bibliography entries.

Published versions are preferred.  Ambiguous metadata remains outside the
bibliography rather than receiving a plausible placeholder.  The abstract
will contain no citations.

## Reverse-outline targets

The first sentence of each main section should reconstruct this sequence:

1. explicit arithmetic family and factor question;
2. nearest general criteria and exact residual scope;
3. frozen object and quantifiers;
4. one-hole arithmetic and constructiveness split;
5. high centers collapse local rules;
6. letter kernels form a graph-partition poset;
7. exact examples and bounded proof diagnostics;
8. scope-limited conclusion.

No section may launch a second paper about general Toeplitz automorphisms,
cross-base factor sufficiency, or experimental symbolic dynamics.

## Plan-review gate

An independent GPT-5.4 reviewer at xhigh reasoning must assess:

1. exact alignment of every claim with `CLAIMS_EVIDENCE.md`;
2. completeness of the prime/composite and arbitrary-radius proof spines;
3. owner subtraction and absence of priority language;
4. whether the journal-neutral A4 structure is proportionate;
5. whether each figure is necessary, reproducible, and non-empirical;
6. citation sufficiency and the finite-check/nonproof firewall;
7. whether the main story is recoverable from title, abstract plan,
   introduction plan, and Figure 1.

The reviewer must return exactly one gate token: `PLAN_READY` or
`PLAN_REVISE`.  If it returns `PLAN_REVISE`, every blocking item must be
fixed and the same reviewer must re-evaluate before any body text is written.

## Pipeline after `PLAN_READY`

1. Generate and independently review the three TikZ figures and two tables.
2. Draft modular LaTeX section by section, verify every bibliography entry,
   and run the reverse-outline and anti-inflation passes.
3. Compile with a fixed `SOURCE_DATE_EPOCH`, inspect the rendered PDF, and
   preserve `main_round0_original.pdf`.
4. Run exactly two GPT-5.4 xhigh improvement rounds in one continued review
   thread; implement supported CRITICAL/MAJOR fixes and recompile after each.
5. Preserve round 0, 1, and 2 sources/PDFs, freeze a self-verifying manifest,
   and stop at `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.
