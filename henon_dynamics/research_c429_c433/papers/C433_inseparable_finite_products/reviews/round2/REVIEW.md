# C433 — actual manuscript review, pass 2

2026-09-09 UTC. Same-thread current-team internal nonauthor manuscript
review by E8, following the actual pass-1 report and the author's
genuine first revision. This is not external peer review, a publication
decision, a citation-audit pass, or the final release seal.

## 1. Verdict and exact scope

**PASS at the manuscript-review gate. All three required pass-1
manuscript findings are closed. No new mandatory repair was found.**

- Open Critical issues: **0**.
- Open Major issues: **0**.
- Open required Minor issues: **0**.
- M1, M2, M3: **closed after actual revised-source and PDF inspection**.
- New mathematical repair or content revision requested: **none**.
- No numerical score or external acceptance judgment is assigned.

The unchanged result covers every prime \(p\), every polynomial
\(f\in\overline{\mathbb F}_p[x]\) of degree \(d\ge2\) with \(f'=0\),
and every nonzero rational weight \(g=A/B\) in coprime form, with
\(m=\max(\deg A,\deg B)\). For

\[
 b=\left\lceil\frac{m}{d-1}\right\rceil+1,\qquad
 D=2b^2,\qquad N=6b^2+1,
\]

the article proves the exact ordinary cofinite-product equivalence

\[
 \mathrm{(CP)}
 \Longleftrightarrow I_g\ne(0)
 \Longleftrightarrow S_*\in I_g
 \Longleftrightarrow
 [F_n\mid S_*H_n\text{ for every }1\le n\le N].
\]

All native periods, including characteristic-divisible ones, remain
included. The visible native-period bound \(D\) is explicitly
conditional on (CP); it is neither a total-cardinality bound nor a
bound on every support cycle. No rational or algebraic transfer
existence, general separable-map theorem, target Euler factor, or
root number is claimed.

## 2. Actual read extent and identity

All paths in this report are relative to the C433 paper directory.
The following actual revised artifacts were read completely:

- main.tex: 63 lines.
- All eight included sections: 55, 107, 114, 95, 146, 115, 61,
  and 36 lines, respectively, totaling **729 section lines**.
- references.bib: 31 lines, and the complete actual revision-build
  main.bbl. Thus main/sections/bibliography comprise 823 source lines.
- All **11 pages** of the actual revised main.pdf text, extracted
  directly to standard output in page ranges 1–4, 5–8, and 9–11.
- PAPER_IMPROVEMENT_LOG.md: all 163 lines, including the full
  response table, recorded delta, real build record, limitations,
  and identity table.
- PAPER_IMPROVEMENT_STATE.json: all 55 lines.
- The frozen 236-line citation report was read in full for the
  actual adjudicated findings and retained limitations. The complete
  443-line pass-1 manuscript report remains the same-thread review
  input, not a replacement for this revised-manuscript reading;
  its identity and findings were checked.

The actual complete diffs against snapshots/v1_baseline were inspected
for main.tex, every section, and references.bib. They contain only
the five approved changed source files: main.tex, sections 1, 5,
and 8, and references.bib. The changes are exactly the two (CP)
summary qualifications, two operator commands, internal-review
disclosure, and the adjudicated name-accent normalization.
There is no additional mathematical or citation-content delta.

Current main.tex and references.bib agree with their
snapshots/v2_round1 copies, and a complete directory comparison
finds no section differences from that snapshot. The four actual
PDF files main.pdf, main_round1.pdf, snapshots/v2_round1/main.pdf,
and build/revision1_20260909/main.pdf are byte-identical.

| Revised input or retained review record | Actual SHA256 |
| --- | --- |
| main.pdf and the three identical revised copies | 489a1038a9e6f27f589e63b2be6dfe69485a6bd2ab6672360d4407b3ea49a7fa |
| main.tex | f5bade84a98663c6c2db3acede6b56810c1bbb04aeff192f98db9334d28c9cd3 |
| references.bib | 318f239a9934e4e9cd1e0467db8b989b0fd47911bda7ef58d3b85c74be93ef41 |
| sections/01_introduction.tex | e9bebaea42b583d9842a2286bc2ace1df96233272019ca90ab9714eae0a37c4a |
| sections/02_statement.tex | 3d6d5d65a715adb9a0c98f6257ab4f122491f02e81d9ff6e7458c8a0217b9f2a |
| sections/03_cycles.tex | 49bccc2a0ba02bb8634b78cdc69cd38fa217691db0df7df27ea4ab47e6f2486c |
| sections/04_extractor.tex | 20fc9ff6342288314cd71efcbdc1f9388455245b8186bf749809c103e662cb69 |
| sections/05_transfer.tex | ef6e465ea6cd9fc2e70e09a9bdc504e811c3f2fe831c2aef2ed073b302d0927e |
| sections/06_rank.tex | 53141c1b73f968333b4af2c180c678a50967df211c78f8190d95935b254fcc88 |
| sections/07_decision.tex | 88b84763f2ab5919de79d8d31b73ff40f6cfd06664b03e308dfb01c6b9477f4c |
| sections/08_conclusion.tex | f0929e8cca3d7eba6519755f71cdee503f6798de1dbd7472159cf8b9b25310c3 |
| PAPER_IMPROVEMENT_LOG.md | f736139bcc30d104125002b40604cda9e3a147ab0b1e42b3d4a0f50b856f058b |
| PAPER_IMPROVEMENT_STATE.json | 7a7510c9fd7a8174d5356e5bd585b6c47d379451b0418a6d1ce8f09e4d23ca54 |
| Frozen pass-1 manuscript review | 23b397bae79f137c323f37405024537995b64375d4ffd201558a5ececcc071a9 |
| Frozen citation report | aa5fdfa7b9d2b635f25a6e9ac5d267529fa0ed879e3f1c54a0fab6c570551fbf |
| Preserved main_round0_original.pdf | 8e58c361b89fe132183451f08b4817699ac02164e224a8cc6589d62e3bdb99f7 |

The original BUILD_RECORD.md and SOURCE_AUDIT.md retain their pass-1
hashes, respectively
e1e865cb14033b81014b0c93281cc3c4c65e0f0eff347580ab30022dc21069bc and
fc5a379ed7889cb256aa0195e4b95988f3445a6446ad5c9238a3c8c77687104c.
They remain baseline records, not retrospectively rewritten accounts
of revision 1.

## 3. Closure of the actual findings

| Finding | Actual revised evidence | Disposition |
| --- | --- | --- |
| M1: missing explicit (CP) condition in summaries | main.tex now defines (CP) in the abstract and starts the visible-period conclusion “Whenever (CP) holds”; Section 1 says “Under the cofinite product condition (CP).” Both appear correctly on PDF page 1. | **Closed** |
| M2: two bare diagonal names | Both block matrices in Section 5 use the already declared LaTeX diagonal operator; equation (5.7) on actual PDF page 7 prints both operators upright. | **Closed** |
| M3: internal-review disclosure | Section 8 retains the AI/shared-development acknowledgment and explicitly states current-team internal nonauthor mathematical review, not external peer review or publication acceptance. The full paragraph was checked in source and PDF pages 10–11. | **Closed** |
| CIT-M01: editor accents | references.bib, the actual generated bibliography, and PDF page 11 print González-Vega and Tomás. | Implemented as adjudicated; no manuscript-side issue |
| CIT-I01: optional name variant | The chosen Joël spelling appears consistently in the bibliography source, generated bibliography, and PDF page 11. Source identity and DOI are unchanged. | Optional normalization implemented; no manuscript-side issue |
| CIT-I02: unavailable database screening | The immutable citation report and the response/state retain the unavailable Retraction Watch database check as incomplete, without claiming clearance. | Limitation retained, not converted into a negative result |

For M1, the original hand counterexample is still relevant to the
unconditional statement but no longer contradicts the revised summary.
With \(p=3,f=x^3,g=-1,m=0,D=2\), there are product-visible
ordinary 3-cycles, but (CP) fails. The repaired sentence now explicitly
requires the condition that this example lacks. The formal theorem's
“If these conditions hold” and Proposition 6.2's \(I_g\ne(0)\)
remain unchanged, so the edit aligns the summary with the proved
statement rather than weakening or repairing the body theorem.

The M2 edit preserves both whole-product blocks and their one minus
sign, including characteristic two. M3 reports an already performed
internal review without falsely claiming external acceptance, two
previously completed manuscript passes, or independent origination
of the shared construction.

## 4. Full-manuscript regression assessment

The full revised source and PDF retain the complete self-contained
proof. The unchanged passages were read in their actual revised
context; no new computation or duplicate literature search was used
as a substitute for that reading.

**Definitions and scope.** The ordinary native clock, one-step skew-map
domain, admissibility, whole numerator/denominator products, return
polynomials, visible sets, annihilator ideal, and supplied \(S_*\)
remain explicit. Nonmonic normalization is actual conjugacy and
preserves the stated tests. All primes, nonmonic maps, \(m=0\),
unequal numerator/denominator degrees, arbitrary support
multiplicities, and characteristic-divisible periods remain covered.

**Ordinary roots and the local warning.** The proof still uses
\(F_n'=-1\) at every return to obtain simple ordinary roots and
the exact (CP)/finite-visible-set/ideal equivalence. The
derivative-filtered criterion is the local
\(e_n(x)S(x)H_n(x)=0\) condition in the field, not pointwise
\(F_n'(x)H_n(x)\). The comparison table and characteristic-three
example retain their explicit local, one-return, outside-the-main-
hypotheses scope. They claim no all-return separable counterexample.

**Coefficient and state proof.** The cyclic digit basis, nondegenerate
top-coefficient pairing, nonnegative-index finiteness identity,
geometric-series cancellation, and \(n=1\) case are complete.
The state bound \(R=a+\ell\), closed low range, strict
\(d^{k_S}>\ell\), all high intermediate states in the distinguished
prefix, finite-word span proof, and short-return cases remain
present. No assumption on the degree of an unknown exceptional
polynomial enters the fixed-\(S\) horizon \(k_S+4b^2\).

**Rank and persistence.** The split bound remains \(2b^2\),
while the word-space bound remains \(4b^2\). Both evaluation
matrices, the invertible diagonal, and the left/right inverses
needed for rank equality are retained. The second evaluation uses
the permutation of the ordinary visible set by \(f^{\circ h}\),
not global separability. Persistence is for one chosen visible
cycle at arbitrarily long returns, including one-sided zero
products. The order of quantifiers remains correct and the
article does not infer \(|\mathcal B|\le D\).

**Elimination and boundary.** The proof still obtains
\(S_*\in I_g\) from the conditional individual native-period
bound, uses \(\deg S_*<d^{D+1}\), and concludes
\(k_{S_*}+4b^2\le3D+1=N\). Both directions of the finite
decision remain intact. Cycles with both whole products zero
remain legitimate finite support exceptions without the period
bound; one-sided support cycles remain covered conditionally.
No phase, characteristic-two sign, or constant-weight case is lost.

**Exposition and ownership.** The abstract, introduction, theorem,
Proposition 6.2, support discussion, table, and conclusion now
agree on the scope. Classical residue/normal-form context and the
arbitrary-field finite-word principle are still credited accurately
and proved at the needed scope inside the article. No new reference,
source identity, DOI, imported theorem, novelty assertion, or
mathematical dependency was added by the revision.

These checks find no regression requiring another author content
revision. The precise source-applicability readings from pass 1
remain applicable because neither the cited propositions nor their
uses changed. No unchanged external literature was reopened in
this pass. X2's separately assigned bounded citation-delta check
is not counted as a manuscript pass or replaced by this report.

## 5. Actual PDF and response-record checks

The actual revised PDF has **11 pages, 374934 bytes**, PDF version
1.5, US Letter, with no encryption, forms, or JavaScript reported
by pdfinfo. Direct pdffonts output has 22 entries; all are embedded,
subsetted, and have Unicode mappings.

All 11 pages were read as actual PDF text. In addition, the reviewer
individually viewed the existing revision images for **pages 1, 2,
7, 10, and 11** in build/revision1_20260909/visuals/. These are
the changed pages and neighboring text-flow checks. Both (CP)
qualifiers, both diagonal operators, disclosure, and normalized
accents print correctly. No clipping, overlap, or legibility
regression was observed on these inspected pages.

This is deliberately not called an independent all-page visual
inspection of the later final release. The remaining revised
pages were text-read, not re-viewed as images in this pass.
The final release must still receive its separately required
all-page visual and reproducibility checks.

The actual revision-build main.log and main.blg were scanned for
warnings, overfull/underfull boxes, undefined items, and errors.
There were no matches; the scan's exit status 1 means no matches,
not a failed compilation. The source and completed extracted text
showed no unresolved-reference or verification-placeholder markers.
The full actual main.bbl and printed references agree with the
revised bibliography.

The author records one fresh revision build with exit 0; this
reviewer did not rerun that build or claim to have witnessed the
earlier directory-creation check. Its actual output PDF, final
logs, fonts, text, snapshots, and rendered changed pages were
inspected here. The preserved cumulative build output is not
recast as warning-free at every intermediate pass. The fixed
PDF timestamp is a deterministic build setting, not a wall-clock
execution receipt.

The 163-line response and 55-line state truthfully record the
implemented changes as pending nonauthor confirmation at their
frozen input time. They preserve complete immutable review
records and do not claim a second review, retraction clearance,
or final clean builds had already occurred. No change to those
frozen records was made by this reviewer.

## 6. Handoff and authority boundary

**The three manuscript repairs are closed and no further content
revision is requested by pass 2.** The coordinator may adjudicate
this report together with the separate citation-delta result and
continue the already specified final release gates. Two fresh
deterministic builds, final-byte comparison, final all-page visual
inspection, exact payload verification, sealing, and integration
are distinct later tasks, not achievements asserted here.

The full auto-paper-improvement-loop skill and relevant repository
workflow were read and followed within the explicit same-team,
review-only assignment. No score, external model, artificial
second revision, or automatic source edit was introduced merely
to imitate a generic workflow example.

Only this new round2/REVIEW.md was written. No author source,
bibliography, PDF, prior review, citation report, improvement log,
state, old proof, shared record, evaluator, or Git artifact was
edited. Mathematical runs, new agents, external-model/API review
calls, new literature searches, compilations, new renders, and
external submissions by this reviewer: **zero**.

**Final disposition: actual revised manuscript PASS, zero open
mandatory manuscript findings, internal review only.**
