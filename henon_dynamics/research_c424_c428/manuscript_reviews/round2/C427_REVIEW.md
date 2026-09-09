# C427 actual-manuscript nonauthor review — round 2

Date: 2026-09-09 UTC. Reviewer: current-team agent
`round6_positive_characteristic`, not the C427 manuscript author.
The coordinator explicitly started this second pass after adjudicating
the complete first-pass report and adopting its sole optional finding.

## Decision and resolved item

**Recommend PASS for manuscript-review round 2. Must-fix findings: 0.
New optional findings: 0. Round-1 O1: CLOSED.**

The adopted abstract wording is present in both the current TeX and
the actual revised PDF. It now explicitly refers to a coordinate whose
absolute value exceeds `|a|+4`. This precisely matches Corollary 2.3
and the two signed large-coordinate tags. The condition still applies
only to a nonzero update product; the amendment has not accidentally
excluded zero-product words or changed the n>=4 scope of the new proof.

This is a real second inspection of the revised manuscript, not a copy
of the earlier assessment or another mathematical-certificate run.
It does not grant a formal Route-A score, human peer review, journal
acceptance, global priority, final-build reproducibility or release
sealing. Formal evaluation remains a separately assigned next stage.

## Exact revised version

The paper directory is `papers/C427_vieta_semilinear/` relative to
this batch. The current PDF has 13 pages and 346694 bytes. Its SHA256 is
`cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1`.
`main.pdf`, `main_round1.pdf` and `builds/round1_revised/main.pdf`
are byte-identical.

| Reviewed record | SHA256 |
| --- | --- |
| `INPUT_MANIFEST.sha256` | `c802d78cd7ec2e4d6c3a87a1c243c657e14d7247f78514f08f6075d52627b1f9` |
| `sections/00_abstract.tex` | `49967cdb448b8cc4117f1817e83aaf64a2d83b64e58a9d43dc5879e70d1f3b7f` |
| `builds/round1_revised/source.tar` | `654d12dad810676f83e801727a9e46434963cf76552da37f7d70c9cce7e9f933` |
| `PAPER_IMPROVEMENT_LOG.md` | `c43375916c874ced9b1250f7ca798fbf727c2f58785987a0714b2c6cb46acf9b` |
| `PAPER_IMPROVEMENT_STATE.json` | `507bc84626fd1f0ec19a8280b730aafca226a9b617774333c8c9902702e77be1` |
| `README.md` | `e78e467791b7680db764b7c913d6e2bd96b0b1c2d246d24b2cc52e6ab6adc8ec` |
| `builds/round1_revised/compile.log` | `8834cf3a657ee09c958fc7f011c17a7171a36567aa0367813577e1cb92117ac0` |
| `builds/round1_revised/main.log` | `a2af098416d60c3e058606569c55581905bf370354124c8c033e76e671957dc3` |
| `builds/round1_revised/main.blg` | `590f52c496f5190716cc609e8a378362ba6fafee10a0bd5a16e33a710439fa9b` |

All ten current TeX/Bib entries passed `sha256sum -c`. I also streamed
every corresponding member from the revised source archive and compared
its digest with the manifest; all ten matched. A fresh PDF text
extraction to standard output matched the retained revised `main.txt`
exactly. These checks identify the actual source/PDF/text object being
reviewed, rather than assuming that a filename points to the right build.

The real pre-review PDF remains preserved in both
`main_round0_original.pdf` and `builds/initial_03/main.pdf`, with the
round-1 reviewed digest
`ff63cdac04d87d212e7c902ce61c56695587e3b12379e180bd6f9c3c3e4dd021`.
The earlier report remains at `manuscript_reviews/round1/C427_REVIEW.md`,
SHA256 `4c6389db5de39eedc9a35e0732f4d5427805e80c77a6a3db3bcc23d231fac812`.

## Actual difference and rereading scope

I compared each of the ten current input files with its streamed member
from `builds/initial_03/source.tar`. There is exactly one source hunk:

```diff
-sequence. Every nonzero update product containing a coordinate larger
-than $|a|+4$ has exactly one large factor, with all other factors units.
+sequence. Every nonzero update product containing a coordinate whose
+absolute value exceeds $|a|+4$ has exactly one large factor, with all
+other factors units.
```

The other nine inputs are unchanged: `main.tex`, `math_commands.tex`,
`references.bib`, and all six non-abstract section/appendix files.
Thus the theorem, its proof, both tables, citations and appendix have
not been silently altered. `SOURCE_AUDIT.md`, `PAPER_PLAN.md` and
`BUILD_LEDGER.md` also retain their first-pass hashes.

In this pass I reread the complete amended abstract in TeX, the complete
atlas section in TeX, and the entire revised PDF text from title through
the last appendix paragraph. I read the new improvement log, JSON state
and revised README in full. The unmodified inputs were compared exactly
as above; the first-pass full-source reading is not falsely represented
as a new second reading of every TeX file.

## Fresh quantifier and boundary checks

The second reading specifically challenged the following risks, rather
than merely confirming that the changed sentence looks reasonable.

1. **Magnitude, signs and mixed zeros.** The amended abstract says
   absolute value; the body uses `B=|a|+4`, the inclusive finite alphabet
   `[-B,B]`, and signed offsets beginning at `B+1`. The strict threshold
   therefore has no missing equality case. Table 2 retains a product
   containing zero regardless of the number or signs of its other large
   factors. The block-local argument does not borrow a global bound
   across intervening zeros.

2. **Every orbit versus one tag choice.** Necessity starts with any
   actual periodic point, whose least period divides L, and labels its
   entire length-L word. Every initial phase is retained. Conversely,
   every solution of every retained tag system satisfies all L actual
   recurrence equations. The converse is not restricted to a preferred
   family or to generic parameter values. The explicit L is larger than
   n, so the length-n projection and window indexing do not require an
   unstated repeated-index convention beyond the stated modulo-L one.

3. **Existence of exclusion witnesses versus free parameters.** For
   each proposed period r, every proper divisor d is excluded by at
   least one coordinate witness and one sign. The construction enumerates
   the full finite product of those choices over all proper divisors,
   then solves each branch. This is the required conjunction over d
   of existential finite witnesses, not one shared witness for all d.
   Within a branch, slack variables turn the signed inequalities into
   equations before the cone construction. No later parameter-dependent
   non-equality condition is left on a purportedly free linear set.
   At r=1, the empty exclusion list is explicitly handled.

4. **Labels after projection and degeneracy.** The recurrence and its
   inverse make a repeated n-state determine the entire scalar word.
   Hence projection cannot turn a point of exact scalar period r into
   a point of a smaller native state period. Collapsed zero directions
   merely give singleton outputs; any surviving nonzero direction
   produces an unbounded ray when its nonnegative parameter increases.
   The construction does not claim independent directions, unique
   representations or same-period disjointness.

5. **Which bound is independent of D.** Channels and the singleton
   remainder `E_{n,a}` are constructed before specifying a level. The
   displayed maximum over that finite remainder depends on `(n,a)`.
   Appendix A's separate all-orbit box is allowed to depend on D and is
   used only for fixed-level finite counting. The revised text does not
   replace either statement by the other or claim finitely many points
   on the whole lattice.

6. **Inherited dimension and mathematical ownership.** The n=3
   statement still imports C421's computer-assisted classification with
   its exact-period table. It is not subsumed under the new analytic
   n>=4 proof. Classical period/cone tools, the auxiliary height argument
   and ordinary cycle/zeta identities retain their ownership and scope.
   The reading of Appendix A still includes zero coordinates, zero
   forcing, singular levels, both `Q=2` and `Q=-2` residual fixed-endpoint
   directions, and the extra factor n from maximizing sum-height.

All six checks passed. No new mathematical gap, claim expansion or
condition weakening was found. The bibliography and source claims are
unchanged, so this pass does not repeat source searches or claim a new
whole-paper external-literature review. The actual primary-access
boundaries remain those recorded in the source audit and first report.

## Complete new visual inspection and page continuity

I freshly viewed all 13 revised page images, including the reflowed
pages 1 and 2. None of the first-pass all-page visual receipt was simply
carried forward. As an additional identity check, I rerendered each
current PDF page at 85 dpi directly to standard output and compared it
byte for byte with the corresponding viewed revised PNG. All 13
comparisons passed; no image files were rewritten.

| Pages newly viewed | Specific continuity/content checked | Result |
| --- | --- | --- |
| 1–2 | Amended abstract; definition (1.4) continues into the free-parameter convention; full Theorem 1.1 and ownership table remain present. | No loss, clipping or overlap. |
| 3–4 | Polynomial-shear explanation, both rigidity lemmas and the corollary, followed by the period constant. | Equations and proof continuations intact. |
| 5–6 | Near-identity/period proof, cone lemma and its proof, transition to finite tags. | No missing line at page breaks. |
| 7–8 | Table 2, exact tagging, divisor-exclusion formula and all-parametric completion. | Period and quantifier statements legible and complete. |
| 9–10 | n=3 attribution, level counts, example continued across the break, limitations and references. | No incomplete example or lost qualification. |
| 11 | Final two bibliography entries before the intentional appendix break. | Short page is intentional; entries complete. |
| 12–13 | Entire height appendix, especially the small/large endpoint and fixed-endpoint transitions. | All cases and final conclusion visible. |

The revised PDF remains letter-sized, 13 pages, unencrypted and without
JavaScript. All 19 font rows are embedded, subset Type 1 resources with
Unicode mappings. I found no missing symbols, clipped equations,
overlapping text or malformed table content.

## Genuine build record and remaining gates

The retained console shows one actual revised latexmk build comprising
three engine passes and two BibTeX passes, ending with the 13-page,
346694-byte output and all targets up to date. I inspected those pass
markers and read the final engine-pass console segment in full. The
final engine/BibTeX logs have no substantive warning, undefined
reference/citation, overfull/underfull box or TeX error. Initial console
passes do contain the expected unresolved references and citations
before the multi-pass build converges; these are not hidden or
mistakenly reported as final warnings.

The improvement log and JSON accurately described the state entering
this review as first-pass revised, second-pass pending. They did not
preclaim this result. Updating them after adjudication belongs to the
coordinator. The baseline and actual revision are preserved; no fake
mathematical intermediate version or repeated old certificate execution
has been inserted to create a nominal review count.

The only file written by this reviewer is this second-pass report.
No manuscript source, PDF, build log, improvement state or old evidence
was changed. No compilation or mathematical program was launched by
the reviewer; text extraction, streamed page rendering, comparisons and
hash checks are diagnostics only. No external model or upload was used.

**Recommended disposition:** accept the revised manuscript at the
second nonauthor-review gate with O1 closed and no remaining review
findings. Proceed only under the coordinator's separately assigned
formal-evaluation and final-release workflow; this report does not
close those later gates.
