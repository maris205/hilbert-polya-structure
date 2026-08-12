# Paper Improvement Log

## Score progression

| Version | Score | Verdict | Status |
|---|---:|---|---|
| Round 0 baseline | 6/10 | Almost | Independent review completed |
| Round 1 revision | 8/10 | Accept with minor fixes | Independently verified |
| Round 2 revision | 8/10 | Accept as a scoped project preprint | Complete |

## Round 1 review and fixes

<details>
<summary>Full independent Round 1 review (verbatim)</summary>

# Stage-02 Paper Improvement — Round 1 Review

## Overall score

**6/10 — Weak accept as an internal scoped theory note; not yet ready as an external archival paper.**

## Verdict

**Almost.** The central obstruction arguments are sound and the scope discipline is unusually careful. One substantive formalization pass is still needed before broad sharing: the wheel object and “stationarization” must become self-contained, three theorem statements need tightening, and the decision diagram must stop implying an exhaustive sequence of mutually exclusive cases.

## Summary

The manuscript gives a clear falsification-first screen for attempts to add periodic dynamics to the graded wheel-sieve system while retaining its exact clock. The periodic-point projection proof, finite-DAG bisimulation argument, quotient-grading argument, and finite-image obstruction are mathematically correct in substance, and the manuscript consistently refuses to infer a universal no-go theorem or positive evidence for the undefined infinite-recoding branch. The main deficiencies are not failed conclusions but formal imprecision and external shareability: the system named in the title is not fully defined in the paper, “stationary” is never formalized, and several project-internal governance terms are presented to an outside reader without definition.

## Strengths

1. **Excellent scope and nonclaim discipline.** The manuscript repeatedly and correctly distinguishes finite DAGs from arbitrary infinite DAGs, finite-local decoders from countable-alphabet or infinite-memory constructions, theorem stops from positive evidence, and finite observations from infinite conclusions. It does not introduce `SD-C07`, define a determinant, run a numerical experiment, or unlock Route B.

2. **The main proof mechanisms are correct.**
   - A periodic point in an equivariant system \((Y,S)\) would project to a periodic point of the strictly graded shift, which is impossible.
   - A quotient cycle under successor matching lifts to an infinite source path; for a finite DAG this contradicts acyclicity.
   - A quotient relation respecting a level-injective label inherits a strict quotient grading.
   - A fixed decoder on a finite pattern domain has finite image and cannot recover infinitely many exact clock values.

3. **Important theorem boundaries are exposed rather than hidden.** The infinite-ray example correctly shows that source acyclicity alone is insufficient for arbitrary infinite graphs. The text also correctly states that escaping the finite-image theorem is only a necessary condition, not evidence that a countable-alphabet or infinite-memory construction works.

4. **The source-lock ledger is useful and concrete.** The requirements concerning map direction, topology, cutoff independence, exact decoding, representative compatibility, and finite-approximation consistency make the surviving branch auditable without pretending that it is already a candidate.

5. **The PDF is technically clean.** An independent two-pass build in a temporary directory succeeded. The baseline PDF has 10 pages, with zero undefined references, undefined citations, LaTeX warnings, overfull boxes, or underfull boxes. All fonts are embedded. `main.pdf` and `main_round0_original.pdf` are byte-identical with SHA-256
   `9ae2f124b41c9fe8c8f1a47c149258f3f2cdb2f9f9f6381f01f07a7186c21ce1`.

6. **The visual presentation is generally readable.** Figure 1 is legible at normal page scale, uses text and line style in addition to color, and visibly records the two principal noncoverage statements. The tables fit within the margins and remain readable.

## Weaknesses and actionable fixes

### CRITICAL

**No conclusion-changing critical error was found.** The following major issues should nevertheless be corrected before the paper is treated as externally shareable.

### MAJOR 1 — The named wheel-sieve object and “stationarization” are not self-contained

In `sections/2_setup.tex`, lines 23–33 assert that the wheel system generates distinct unbounded primes and the clock \(\tau_k=\log q_{k+1}\), but the manuscript never states the wheel recurrence, defines the residue graph, or proves the prime-enumeration fact. Because the paper intentionally contains no citations and Appendix B claims mathematical self-containedness, an outside reader cannot verify the wheel-specific application from the PDF.

Likewise, “stationary,” “stationarizing,” and “level-blind” do not receive formal definitions. The source is already presented as a self-map \(\sigma:X\to X\), so the intended difference between that self-map and a “stationary” target is not mathematically explicit. None of the proved theorems actually has stationarity as a hypothesis.

**Actionable fix:**

- Add a compact wheel-definition subsection containing
  \[
  Q_1=q_1=2,\qquad
  q_{k+1}=\min\{n>q_k:\gcd(n,Q_k)=1\},\qquad
  Q_{k+1}=Q_kq_{k+1},
  \]
  the residue levels and tail-path shift, and a short lemma proving \(q_k\) is the \(k\)-th rational prime.
- Define exactly what this project means by a stationary or level-blind recoding: one fixed target phase space, one cutoff-independent shift rule, and no externally supplied level or prime table.
- If those definitions are intentionally deferred, narrow the title and abstract to “periodic-orbit and exact-clock obstructions for strictly graded shifts,” and present the wheel application explicitly as conditional on the Stage-01 lemma.

### MAJOR 2 — Three formal statements need tightening

#### 2a. Codomain mismatch in the local-clock theorem

`sections/5_clock.tex`, lines 10–13 define \(d:A^W\to\mathbb N\) and then say that the same decoder conclusion applies to exact values \(\log q_k\). Those logarithms are generally not elements of \(\mathbb N\). The proof has the correct finite-image idea, but the theorem is ill-typed as written.

**Actionable fix:** State a finite-image lemma with arbitrary codomain \(Z\), or introduce separate decoders
\[
d_q:A^W\to\mathbb N,\qquad d_\tau:A^W\to\mathbb R.
\]
Then apply the lemma to the two infinite target sets \(\{q_k\}\) and \(\{\log q_k\}\).

#### 2b. The exact-label corollary omits its representative-consistency hypothesis

`sections/4_bisimulation.tex`, lines 84–94 say that if every quotient class “carries one exact state-only value \(q_{k+1}\),” then the quotient cannot merge levels. On its face, that wording does not require the class value to be exact for every representative in the class, which is the hypothesis needed to invoke Proposition 4.3.

**Actionable fix:** Replace the premise with an explicit class decoder:
\[
D([v])=q_{\level(v)+1}\qquad\text{for every representative }v.
\]
Equivalently, require
\[
v\sim w\Longrightarrow
q_{\level(v)+1}=q_{\level(w)+1}.
\]
The conclusion then follows immediately from level injectivity.

#### 2c. “Equivalently” is too strong in the inverse-limit proposition

`sections/3_strict_extensions.tex`, lines 39–53 call
\[
\varprojlim(X,\sigma)=\varnothing
\quad\text{and}\quad
\bigcap_{n\ge0}\sigma^n(X)=\varnothing
\]
equivalent. For a general noncompact, infinitely branching system, membership in every finite-depth image need not by itself supply one compatible infinite backward orbit. In the present strictly graded system both sets are empty by separate direct arguments, so the conclusion is safe but the equivalence language is unjustified.

**Actionable fix:** Replace “Equivalently” and “For the equivalent formulation” with “Moreover” and “Independently.” Alternatively, state additional hypotheses under which the usual equivalence is intended.

### MAJOR 3 — The bisimulation boundary is correct but not stated at its natural strength

The proof of Theorem 4.1 does not fundamentally need finiteness; it needs the absence of an infinite forward path. Thus the sentence “The finiteness hypothesis is essential rather than technical” is too strong. The infinite ray shows only that finiteness cannot be dropped while retaining acyclicity alone.

**Actionable fix:**

- Prefer the stronger theorem: if the source graph has no infinite directed path and the quotient relation has successor matching, then the quotient is acyclic.
- State the finite-DAG theorem as an immediate corollary.
- Retain the infinite-ray example to show that an infinite acyclic graph may fail the no-infinite-path hypothesis.
- If the paper deliberately keeps the finite formulation, change the prose to: “Finiteness cannot simply be removed while retaining only acyclicity.”

This change would make the dependency audit exact: the proof uses successor matching plus forward well-foundedness; finite acyclicity is one sufficient package.

### MAJOR 4 — Figure 1 is visually good but logically misleading as a decision tree

The diagram asks three questions sequentially. A “no” answer to one question does not logically place an object in the next class, and “no” to all three does not establish that the object has exact decoders or compatible path lifting. The three hypothesis classes can overlap, and they are not an exhaustive partition of symbolic constructions.

**Actionable fix:** Redraw the figure as four parallel branches from the graded source:

- strict equivariant extension → theorem stop;
- forward-well-founded/finite DAG strong bisimulation → theorem stop;
- finite-alphabet fixed-window exact decoder → theorem stop;
- other infinite factor or observational recoding → unclassified, with explicit source-lock obligations.

If retaining the current layout, remove the “yes/no” labels and title it a “project screening sequence,” making clear that the dashed final box is the branch retained by the project workflow, not the logical complement of the preceding theorem classes.

### MAJOR 5 — The paper still reads as an internal gate memo rather than a standalone research note

Terms such as `SD-C07`, “Route B,” “source lock,” “theorem stop,” and “not testable” appear in the abstract, status box, introduction, Section 6, conclusion, and appendix. `SD-C07` and Route B are not defined for an outside reader. Repetition of governance status also obscures the mathematical contribution.

The intentionally empty bibliography creates a second shareability problem. Full proofs remove dependence on references for correctness, but they do not position the standard notions of natural extension, symbolic recoding, and bisimulation or distinguish the paper’s screening synthesis from existing theory.

**Actionable fix:**

- Define “source lock” once in plain mathematical language as a complete, frozen specification of the infinite object and its decoders.
- Either define Route B as the later analytic determinant-comparison stage or replace it everywhere in the paper with “analytic determinant comparison remains outside scope.”
- Move the internal identifier `SD-C07` to the sharing/status appendix; it need not appear in the abstract.
- Consolidate the governance statement in the title-page status box and one conclusion sentence.
- Add a short, metadata-verified related-work paragraph covering graded symbolic systems/natural extensions, symbolic codings, and bisimulation quotients. Present the contribution modestly as a scoped screening synthesis unless a novelty search establishes stronger priority.

### MINOR 1 — Harmonize the semiconjugacy convention

The paper correctly observes that surjectivity of \(\pi\) is unnecessary, while `STAGE2_PREREGISTRATION.md` says “semiconjugating onto.” Standard usage varies.

**Actionable fix:** Define the convention once: the theorem assumes only a total map \(\pi:Y\to X\) satisfying equivariance; surjectivity is optional. Use the same wording in the paper, README, plan, and preregistration.

### MINOR 2 — Table 2 floats before the Section 6 heading

In the PDF, the Stage-02 decision table appears at the top of page 7 before “6 The Surviving Class and Its Current Status,” although the table is introduced inside that section. This is legal LaTeX placement but weakens reading order.

**Actionable fix:** Move the table source immediately after the Section 6 opening paragraph and constrain placement, or insert an appropriate float barrier so the table cannot precede its section heading.

### MINOR 3 — Clarify the path-lifting obligation for periodic target words

“Lift to one compatible source path” is directionally correct, but it could be read as demanding a closed source path, which is impossible in the strictly graded source. The intended requirement appears to be one globally compatible infinite source orbit whose recoding realizes the repeated target word.

**Actionable fix:** State explicitly whether the lift is finite, one-sided infinite, or bi-infinite, and whether a target periodic point in an orbit closure but outside the direct image is admissible. Do not call it an intrinsic periodic orbit of the source unless the source orbit itself is periodic.

### MINOR 4 — State the minimal dependency in the bisimulation definition

Because \(\sim\) is an equivalence relation, the two successor-matching clauses are symmetric restatements, and Theorem 4.1 uses only the successor-lifting property after swapping related vertices.

**Actionable fix:** Either keep the conventional two-sided definition and say it is used only through successor matching, or define the exact successor-stable equivalence needed by the theorem.

## Missing references

The manuscript currently has no citations. Before external circulation, add verified references for:

- symbolic dynamics and sliding/block recodings;
- natural extensions and inverse limits;
- bisimulation quotients of directed transition graphs;
- wheel/primorial sieve recurrences, unless the elementary recurrence and its prime-enumeration lemma are fully reproduced.

No citation is needed merely to justify the elementary proofs, but literature positioning is necessary to avoid implying that each basic obstruction is itself a new theorem.

## Recommended Round 1 implementation order

1. Add the self-contained wheel recurrence and formal definition of the targeted stationarity/level-blind condition.
2. Correct Theorem 5.1, Corollary 4.4, and Proposition 3.2.
3. Strengthen or accurately rephrase the bisimulation theorem boundary.
4. Redesign Figure 1 as a parallel hypothesis map.
5. Consolidate internal governance terminology and add verified scholarly positioning.
6. Fix the Table 2 float and clarify periodic-word path lifting.
7. Recompile and repeat the existing reference, box, font, metadata, and visual checks.

With those corrections, the manuscript should move to approximately **7/10** as a precise, shareable scoped theory note while preserving all current nonclaims and keeping Route B locked.

</details>

### Actions implemented

1. **Self-contained arithmetic source.** Added the frozen \(Q_k,q_k\)
   recurrence, canonical residue levels and tail-path shift, a complete prime
   induction lemma, and the exact primorial-ratio clock identity.
2. **Stationarization convention.** Defined a project stationarization as one
   target system with a cutoff-independent, level-blind rule and total
   decoders that receive neither an external level nor a stored prime table.
3. **Decoder types.** Replaced the ill-typed clock theorem by a
   codomain-independent finite-image theorem and separate decoders
   \(d_q:A^W\to\mathbb N\) and \(d_\tau:A^W\to\mathbb R\).
4. **Exact class-decoder hypothesis.** Replaced the ambiguous state-label
   corollary by the explicit requirement
   \(D([v])=q_{\operatorname{lev}(v)+1}\) for every representative.
5. **Inverse-limit wording.** Replaced the unsupported general-equivalence
   language by a separate “Moreover” image-intersection conclusion.
6. **Natural bisimulation boundary.** Strengthened the main quotient theorem
   to forward-well-founded graphs, derived finite-DAG acyclicity as a
   corollary, and retained the infinite ray as the counter-boundary to
   acyclicity alone.
7. **Parallel figure.** Replaced the sequential yes/no tree with four parallel
   hypothesis branches. The dashed branch is explicitly a project-retained
   undefined class, not the logical complement of the theorems.
8. **External terminology.** Defined “source lock” as a complete frozen
   mathematical specification, defined Route B once as the later analytic
   determinant-comparison route, moved the internal candidate identifier to
   Appendix B, and replaced theorem-stop jargon in the body with
   plain-language decisions.
9. **No priority overclaim.** Added an explicit statement that equivariant
   maps, inverse limits, bisimulation, and finite-range observations are
   standard mechanisms and are not claimed as new standalone concepts. No
   unverified bibliography metadata was invented.
10. **Path semantics.** Required one one-sided infinite source lift for a
    direct-image target periodic point; closure-only periodic points require
    a separate approximation and clock-inheritance theorem.
11. **Presentation.** Constrained the Section 6 status table to appear after
    its section heading and harmonized the equivariant-map convention without
    assuming surjectivity.
12. **Source/extension subject clarity.** Rewrote the abstract so the empty
    full-backward inverse limit is attributed only to the graded source
    \(X\); the extension conclusion is separately and correctly limited to
    absence of periodic points.

### Round 1 artifacts

- `main_round0_original.pdf` — untouched baseline.
- `main_round1.pdf` — compiled manuscript after the fixes above.
- `main.pdf` — current working copy, byte-identical to `main_round1.pdf` at
  the Round 1 checkpoint.

## Round 2

### Independent Round 2 review

**Score before the Round 2 edits: 8/10 — accept with minor fixes.**

**Final score: 8/10 — accept as a precise, externally shareable scoped
project preprint.**

The preserved Round 0 PDF was compared with the Round 1 working PDF before
any Round 2 edit.  The Round 1 revision adds the missing wheel recurrence and
prime-enumeration proof, formalizes the level-blind stationarization
convention, corrects the finite-image decoder types, strengthens the
bisimulation result to forward-well-founded sources, separates the two
inverse-limit conclusions, replaces the sequential decision tree by a
parallel hypothesis map, and makes path-lifting obligations explicit.  The
Round 0 and Round 1 PDFs have distinct hashes, and every listed Round 1
change is visible in the compiled manuscript.

#### Mathematical verification of the Round 1 fixes

1. **Wheel recurrence and clock: verified.**  The induction proving that the
   minimizer is the next rational prime is correct: the next prime supplies
   existence, while any composite minimizer has a smaller prime factor that
   either divides the current primorial or is itself a smaller admissible
   integer.  The identity \(Q_{k+1}/Q_k=q_{k+1}\) gives the stated exact
   logarithmic clock.
2. **Strict-extension obstruction: verified.**  Equivariance sends a target
   periodic point to a source periodic point, contradicting disjoint
   one-step level growth.  Surjectivity is not used.
3. **Source inverse limit: verified.**  A backward history based at level
   \(k\) would require a negative level after more than \(k\) steps.  The
   image-intersection statement follows separately from
   \(\sigma^n(X)\subseteq\bigsqcup_{j\geq n}X_j\); no unjustified general
   equivalence remains.
4. **Bisimulation obstruction: verified.**  A quotient cycle and successor
   matching recursively lift to an infinite source path, contradicting
   forward well-foundedness.  The finite-DAG statement is a valid corollary,
   and the infinite ray correctly shows why source acyclicity alone is not
   enough.
5. **Representative-exact grading: verified.**  Exactness of one class
   decoder for every representative forces equal prime labels and hence
   equal levels inside a class.  Quotient edges then raise the induced level
   by one.
6. **Finite-local decoder: verified.**  The arbitrary-codomain theorem is
   well typed, and the separate integer and real decoder corollaries follow
   from the infinitude of the prime and logarithmic-clock ranges.
7. **Scope boundaries: verified.**  The paper does not extend the
   forward-well-founded theorem to infinite rays, does not extend the
   finite-image theorem to countable alphabets or infinite memory, and does
   not treat escape from a theorem as positive evidence.

No critical or major mathematical defect remained after Round 1.  The one
recurrent minor issue was grammatical rather than theorem-level: in Figure
1, Table 1, the contribution list, and the conclusion, the target
periodic-point obstruction and the source inverse-limit result were still
juxtaposed without an explicit change of subject.  An outside reader could
therefore misread the paper as claiming that the extension's inverse limit
is empty.  Two smaller sharing issues remained: “genuinely new” could sound
like a priority claim, and a negative internal candidate identifier was not
useful to an outside reader.

The figure, all eleven PDF pages, the Section 6 table, and both appendices
were rasterized and visually inspected.  Text is legible at normal page
scale, the four branches are parallel rather than sequential, color is not
the sole carrier of meaning, and no content crosses a page boundary.  The
paper is self-contained for the elementary claims it proves.  It deliberately
does not attempt a literature-positioned priority claim; a future archival
submission would still benefit from a metadata-verified related-work
section, but that is not a correctness condition for this scoped project
preprint and no unverified citations were introduced.

### Round 2 actions

1. Changed every potentially ambiguous summary to say explicitly that the
   target extension has no periodic points while, independently, the graded
   source has an empty full-backward-orbit inverse limit.
2. Applied the same subject separation to Figure 1, Table 1, the
   introduction, Section 3, the conclusion, README, narrative report, and
   claims--evidence plan.
3. Replaced “genuinely new infinite factor” by “separately defined infinite
   factor,” avoiding an unsupported novelty implication.
4. Removed the unnecessary internal candidate identifier from the
   share-facing manuscript and plan while retaining the mathematically useful
   statement that no candidate has been opened.
5. Recompiled twice and repeated reference, box, font, metadata, control-byte,
   sentinel, extracted-text, and visual checks.

### Final Round 2 artifact

- `main_round2.pdf` preserves the completed second-round revision.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- `main_round0_original.pdf` and `main_round1.pdf` remain untouched.
- Final SHA-256:
  `91d8f9ffd1b067be00d0fea1b033d46df44b931378e934b345dfab31feacf09d`.
- Final length: 11 pages.
- Undefined references/citations: 0.
- Overfull/underfull boxes: 0.
- Nonembedded fonts: 0.

The two-round improvement workflow is complete.
