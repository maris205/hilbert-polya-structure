# C429 — actual manuscript review, pass 2

Title: *Polynomial periodic-data rigidity for unicritical maps in finite characteristic*.

Reviewer: `/root/c429_e4_cover_review`, the same current-team nonauthor mathematical reviewer as pass 1. Actual completion-stage clock checkpoint: 2026-09-09 21:32 UTC. Review input: the real first author revision, not the original PDF or a proposed patch.

## Recommendation

**PASS this second internal manuscript review. W1–W3 are fully addressed. There are zero residual Critical, Major, or Minor findings and zero new findings. No further mathematical or expository revision is requested by this reviewer.**

The complete revised article retains the original all-prime, all-degree, all-parameter polynomial rigidity theorem and both two-return certificates. Its proofs, parameter domains, native clock, multiplicity treatment, characteristic-two cases, constants, zero input, and iterate-degree bounds remain sound on this full reread. The real revision makes the three authorized precision repairs without changing the theorem or relying on a narrower problem.

This recommendation closes this review's mathematical/expository gate only. It is not human peer review, publication acceptance, a worldwide-priority finding, final-release approval, or a formal-verification certificate. Calibration: `NOT_CALIBRATED`. No venue criteria or numerical score are inferred. This is a same-thread, current-team AI re-review; it is not a second independent reviewer or an independent error process. Same-family revision and review can share biases. The coordinator retains adjudication and release authority.

## 1. Actual read extent and comparison

I read all ten active mathematical/BibTeX files in full: `main.tex` (50 lines), `math_commands.tex` (29), `references.bib` (67), and the seven section files (171, 149, 175, 97, 254, 192, and 90). Total: **1,274 lines**. This includes every typeset proof, not just the three edited passages.

I freshly extracted the actual revised `main.pdf` with read-only `pdftotext -layout main.pdf -`. Its hash agrees with the retained **816-line** `revisions/round1_author_revision_01/main_round1.txt`, which I read completely. I also read the entire 34-line source diff, 177-line PDF-text diff, 71-line improvement log/author response, 138-line improvement state, and 85-line original author record. The latter is explicitly preserved as a round-0 historical record, not mistaken for a current-PDF receipt.

A direct baseline-to-active comparison of all ten source/BibTeX files finds precisely W1 in `main.tex` and W2–W3 in the introduction. The other eight files, including all six proof/consequence sections, are byte-identical to the baseline. The actual revision's source snapshot and build inputs match the live manuscript under the checked inventory. All **57** entries in the revision `FILES.sha256` and all **23** original snapshot entries pass checksum verification. The original PDF and first review remain preserved.

The first review's complete examination of the 1,770-line accepted proof inputs remains the prior-input comparison; I did not reread those research packages or rerun old mathematics in this pass. Here I reread the complete actual article containing those arguments. Hash matches establish byte identity; the mathematical judgment comes from reading the proofs.

## 2. First-pass findings: verified closure

The yardstick is the immutable pass-1 W1–W3 and the coordinator's acceptance of their stated minimum repairs. No new acceptance condition or stronger theorem was introduced. I checked the manuscript evidence before reading the complete author response; the response agrees with the observed edits and required no change to these conclusions. The coordinator's assignment had already disclosed the intended changes, so this is not a revision-blind procedure.

| Item | Inherited requirement and author's response | Revised evidence | Verdict / residual action |
| --- | --- | --- | --- |
| W1 — positive cap | Declare an integer cap at least one in the abstract; the author reports making that declaration. | `text:` `main.tex:32`, “for any integer”; the same clause explicitly gives $M\ge1$ and $\deg h\le M$. Section 1's definition and Theorem 1.2 still include zero input without taking its degree logarithm. The actual PDF contains the repair. | **FULLY_ADDRESSED**; none. |
| W2 — scalar | Describe the marked difference as a nonzero scalar multiple, retaining the characteristic power; the author reports this exact change. | `text:` `sections/01_introduction.tex:153`, “a nonzero scalar multiple”; equation (6.2) remains $C(n+1,s+1)-C(n,s)=\alpha a_D^P\ne0$, with $\alpha=(d-1)/P\bmod p$ defined in (5.1). | **FULLY_ADDRESSED**; none. |
| W3 — accessed version | Identify the inspected residue locator as the accessible preprint, without asserting unverified published numbering; the author reports that clarification. | `text:` `sections/01_introduction.tex:138`, “of the accessible preprint”; bibliography entry [1] retains the published chapter and its preprint link. The revised PDF renders that locator unambiguously. | **FULLY_ADDRESSED**; none. |

W1 changes only the cap's declaration, not either return formula. W2 now accurately describes the unchanged proposition for every allowed characteristic, without assuming $\alpha=1$ or dropping the Frobenius power on coefficients. W3 fixes version traceability, not a mathematical premise; it makes no fresh claim that the published chapter has been read in full.

## 3. Full mathematical regression review

### 3.1. Original contract and finite theorem

**Evidence:** Theorems 1.1–1.2, Table 1, equations (1.1)–(1.5), and Section 7.3.

The domain remains $k=\overline{\mathbb F}_p$, every prime $p$, every integer $d\ge2$, every $c\in k$, and every polynomial observable. Primitive affine cycles count each distinct point once, including native periods divisible by $p$. Table 1 is still disjoint and exhaustive. Its ordinary-root condition concerns full return sums on every root at both adjacent levels, not merely exact-period cycles. The displayed bounds concern iterate degrees, not all unreduced test products or optimized computational complexity.

### 3.2. Normal form, nonreduced algebra, and ordinary data

**Evidence:** Lemmas 2.1–2.4 and equations (2.1)–(2.6).

Degree-decreasing monic elimination still supplies the direct sum and transfer uniqueness modulo constants, with no assumption that $d$ is invertible. The cyclic algebra has dimension $d^n$ by elimination, and its terminating reductions span exactly that many legal digit monomials; reducedness is unnecessary. The leading detector retains its endpoint/window argument and singleton case. The local Hasse order estimate yields the necessary certificate at arbitrary root multiplicity. Formula (2.1) uses an integer repetition count, not field division. None of these passages has been shortened or altered by the introductory reflow.

### 3.3. Ordinary carry stabilization and the first two regimes

**Evidence:** Proposition 3.1, equations (3.2)–(3.9), and Sections 4.1–4.3.

The full one-circuit expansion still includes all, even zero-weight, branches. Normality makes the final source digit legal after the carry falls to zero or one. Source localization covers every contributing source. Both insertion and deletion use the two consecutive zero outputs to force a weight-one transition; the longer-level source blocks correspond exactly. Constants cannot contribute to the short target. The adjacent Jacobian equations then give $(1-d)a_D=0$, while the separate $p\mid d$ branch uses $F_j'=-1$. Adjacent levels remove constant normal parts, and telescoping completes the finite equivalence.

### 3.4. Hasse paths, adaptive cuts, and common-cut validity

**Evidence:** equations (5.1)–(5.15), especially Sections 5.3–5.5.

The first nonlinear composition coefficient remains valid at $P=2$, and the Frobenius identity raises all observable coefficients. Target digits remain legal, with the first post-block digit at most $d-2$. The adaptive cut excludes overflowing branches because their final cut digit is at most one, strictly below $d-1$. For nonoverflow branches the cut quotient and weight are unchanged. The baseline identity is used only below the last index; its nonpositive-excess argument localizes every source and excludes constants. After localization, the fixed cut at zero is justified independently, giving $t_0=t_n=1$ without a second circuit. No hidden reducedness or generic-parameter hypothesis has appeared.

### 3.5. Marked insertion, uniqueness, and all boundary cases

**Evidence:** Proposition 6.1, equations (6.2)–(6.7), and Sections 6.1–6.4.

All old marked paths are paired, including marks neighboring the insertion site. The new mark resets the carry, and the first smaller digit forces the source at or before the marked target block. The integer loss identity

$$Pr=PDd^{S-i}+\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}$$

has only nonnegative losses; $r\le D$ and $i\le S$ force $i=S$, $r=D$, and zero loss. The manuscript supplies the existence and uniqueness of that path, with weight one. Including its two coefficients gives the exact unchanged $\alpha a_D^P$ which now agrees with the introduction. A return index prime to $p$ eliminates constants using the nonzero leading coefficient $j\alpha$ of $D^{[P]}F_j$. The explicit $p=2,d=3,P=2$ boundary retains the strict overflow and first-small-digit comparisons even though the anchor and long-block digits coincide.

### 3.6. Bounds and consequences

**Evidence:** Sections 4.3, 6.3–6.4, and 7.1–7.3.

The selected levels remain $n_J=3\lfloor\log_d M\rfloor+4$ and $n_H=7\lfloor\log_d(PM)\rfloor+22$. The resulting degrees remain bounded by $d^5M^3$ and $d^{23}(PM)^7$. A failed ordinary-root test gives a nonzero primitive sum without dividing by the repetition count. The shear has the correct sign, and the lifted native period is $r$ or $pr$, even when $p\mid r$. Example 7.1 remains a failure of the ordinary-Jacobian detector, not a counterexample to rigidity. No rational-observable, general-polynomial-base, global-inverse, or target-arithmetic conclusion was added.

## 4. Strengths and coverage of the empty findings list

**S1 — complete proof-bearing manuscript.** `equation:` Propositions 3.1 and 6.1. The article retains actual exhaustive path correspondences and the isolated new contribution; no central proof is replaced by a link or a computational assertion.

**S2 — revision aligned with mathematical evidence.** `table:` Table 1 and Theorem 1.2. The revised cap and unchanged three-regime statements agree globally, including zero/constant observables and native wild periods.

**Coverage receipt — Weaknesses:** no new or residual weakness was found in the examined dimensions. Criteria are inherited from the approved batch's C429 contract and its proof-only manuscript requirements; no journal-specific binding is supplied (`criteria_binding_unavailable`).

| Dimension / criterion | Judgment | Checked evidence and basis for no weakness | Scope / decision bearing |
| --- | --- | --- | --- |
| Original theorem and quantifiers | MEETS | Theorems 1.1–1.2 and Table 1 preserve all original parameters and both ordinary-root levels. | Full source reread; supports pass. |
| Proof rigor and evidence sufficiency | MEETS | Lemmas 2.1–2.4, Propositions 3.1 and 6.1, and all completion arguments remain complete. | Hand review, not formal verification; supports pass. |
| Argument and notation coherence | MEETS | Both cut conventions, source/mark relabeling, integer losses, and coefficient Frobenius remain consistent. | Mathematical exposition; supports pass. |
| Requested precision and source locator | MEETS | W1–W3 have substantive manuscript-side repairs matching the frozen criteria. | Bounded closure check; supports pass. |
| Consequence and limitation scope | MEETS | Section 7 preserves the polynomial/native-clock scope and blind-test distinction. | No target-arithmetic promotion; supports pass. |
| Revised rendering | MEETS within inspected scope | Full text read; six retained revised images show legible edits, table, continuations, and references. | Selected images only; not final all-page release QA. |
| Worldwide novelty, full citation-status clearance, venue fit, final reproducibility | NOT_ASSESSED | No new search, bibliographic-status sweep, venue selection, or deterministic release builds were allocated. | Cannot be inferred from this pass. |

There are no questions requiring an author response. There is no statistical dataset, reported significance test, sample mean, or degrees-of-freedom claim to recompute: the evidence is proof-only.

## 5. Actual revised artifact and build observations

The three actual PDFs—`main.pdf`, `main_round1.pdf`, and `revisions/round1_author_revision_01/build/main.pdf`—have the same SHA-256, 16 letter-size pages, and 423,936 bytes. The retained build transcript records one latexmk invocation with three pdfLaTeX passes and two BibTeX passes, ending with all targets up to date. I inspected its pass/completion records and screened the final log and bibliography log; I did not run a build or claim to reread every compiler-log line.

The final-log screen finds only the known underfull bibliography paragraph, badness 2173 at `main.bbl` lines 33–38. Initial unresolved labels/citations are present in the full invocation transcript and have converged; they are not reported as final warnings. No final error, undefined citation/reference, multiply-defined label, overfull box, or package warning was found by the stated screen. All 25 listed font resources are embedded. The active sources and extracted text contain none of the screened unresolved markers.

I individually viewed the six retained revised images named `page-01`–`page-04`, `page-15`, and `page-16`. The cap, scalar wording, preprint locator, algebraic-closure bars, theorem/table content, proof continuations, and bibliography are legible without observed clipping or collisions. The underfull reference remains readable. These are existing author-rendered images, not a fresh rendering by this reviewer or an independent all-page visual release inspection. No PDF structural-preflight PASS is claimed; proof anchors in this report use source lines, sections, and equation numbers.

The source-version repair is checked against the primary-source scope already established in pass 1. I did not repeat external browsing, reopen the unread 1994 full text, or turn a prior access limitation into clearance. The manuscript still states its abstract-only access and direct 1998 attribution, with no unread theorem used. The separate citation-delta assignment remains a separate coordinator gate; this report does not replace it or certify current retraction/Crossmark status.

## 6. Exact input hashes

All paths below are relative to the C429 manuscript directory. Values were actually checked in this pass.

| Input | SHA-256 |
| --- | --- |
| `main.pdf` / `main_round1.pdf` / revised `build/main.pdf` | `635f6868081c83ac0d76adde5ffe6a80e8eb7077a5c72dd44f7e7f19d75a36c6` |
| `main_round0_original.pdf` | `118733318d139821d5cb29ab8deccc9d46fe577230563fbd38858df7ea431a02` |
| `main.tex` | `1a607bc23fc307c86f15d4a489d260c0c9bd31ad77475bec9340ee4738e8a7b0` |
| `math_commands.tex` | `08d91e8041f21be8f5f08a273468daef71a75262e65efc0d6508b7b818b4e40d` |
| `references.bib` | `2572ac5a6b6be971085d89df647042ea43f62df451b8c65962f31466db22f04b` |
| `sections/01_introduction.tex` | `17d4ee29e93504bb8f618f2221eb94feab237d368aac894b45dcdd125eb54c0e` |
| `sections/02_periodic_algebra.tex` | `5eda56a89a9d279180b42e0289ce5d57f315d0e87e374b9e148d4d54154fd1f2` |
| `sections/03_carry_stabilization.tex` | `0c10b30eac8d3cbf3b34b8d6f133a009cd27b9b1c3f9c6d8b0c70141006146e3` |
| `sections/04_jacobian_regimes.tex` | `3ebb7dd19724c1cedfa0d3e1c158ce65a7f8c4bc04268b85b90f0c4ff283367a` |
| `sections/05_hasse_paths.tex` | `8891ca9a50f08062be10d4ccc2d9cec62603f4ed144b4b89971a63d6469a2386` |
| `sections/06_marked_insertion.tex` | `8e041a4fce45ff486c4718409a065984ddb2c7c8ca7d0104ed3698a7eb9d8226` |
| `sections/07_consequences.tex` | `bb55c5c3603fb1ab1b942c1da7beb10816fcb9dfed7cdfa5eb4cd9ee8a37ce1b` |
| `reviews/round1/REVIEW.md` | `edbae0516b3ac82f0196ac14871b7b63094591392f932a18a44555c3a17e8b4f` |
| `PAPER_IMPROVEMENT_LOG.md` | `16aea4fcb2d4d90220ff050af78affaad331e1b778cc3c56280a5b9454c8826d` |
| `PAPER_IMPROVEMENT_STATE.json` | `6605faaf0841e9fc2e5d960b099c20e3ea4affc917b16c3dadec935d3b91e551` |
| `revisions/round1_author_revision_01/main_round1.txt` | `de4fbeb8f15e8e11bf9e56dc1213ab9161dfbc6830a76b5d2989a32a77adf310` |
| `revisions/round1_author_revision_01/FILES.sha256` | `26dab4db642bffbfb75f4a6883a107acaa9cd0d30bdd73d3fe51451f85474737` |
| `revisions/round1_author_revision_01/SOURCE_DIFF.patch` | `bb0a9d613ae966a43a4eb25616c58a7bf1e436b24c2f7ee43b035527eb9fe60c` |
| `revisions/round1_author_revision_01/PDF_TEXT_DIFF.patch` | `f5f5aa7a472e4461ca7f9dbda208c6a2355c64715b1ae91eb101f3c0bb848401` |

## 7. Handoff and execution boundary

The named auto-paper-improvement-loop skill supplied actual same-thread review/revision continuity. The batch, proof-writer, research-review, and bounded ARS theoretical/re-review guidance supplied scope preservation, full-proof checking, criterion continuity, and manuscript-side verification of responses. The coordinator's explicit current-team assignment overrides older external-model, ML-venue, numerical-score, automatic-edit/build, and full-panel defaults. No full ARS panel, three-gate machine-checked ARS protocol, cross-model review, calibration run, or unavailable script execution is claimed.

Only this newly allocated second-review file was written. The first review, citation report, sources, bibliography, author log/state, snapshots, PDFs, prior proofs, shared files, evaluator, and Git state were not edited. No compilation, mathematical program, new agent, external model/API/upload, or publication action was performed.

The coordinator may close W1–W3 and this second mathematical manuscript pass on the bound revised bytes. No second author rewrite is required merely to manufacture another version. The separate citation-delta adjudication, final deterministic builds, full final-page inspection, release inventory/manifest verification, and integration remain outside this report. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
