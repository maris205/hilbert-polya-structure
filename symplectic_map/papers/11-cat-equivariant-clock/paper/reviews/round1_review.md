# Independent Manuscript Review — Round 1

Review date: 2026-08-15 UTC  
Candidate: `cat_equivariant_retention_tradeoff_v1`  
Manuscript: *An Equivariant-Zeta Audit of Cat-Map Centralizer Quotients*  
Reviewer role: fresh independent mathematical, literature-boundary,
reproducibility, presentation, and devil's-advocate reviewer  
Recommendation: **MINOR REVISION**  
Disposition: **REVISION_REQUIRED_DO_NOT_FINALIZE**  
Severity inventory: **0 Critical / 0 Major / 1 Minor**  
Confidence: **5/5** for mathematics and local artifact verification;
**4/5** for literature completeness because the review was intentionally
offline  
Overall score: **86/100 (8.6/10)**

## Executive assessment

The scientific core passes.  I independently checked the general finite
abelian $C$-set theorem, the distinction between point-exact and
orbit-exact Burnside classes, the additive-only use and
nonmultiplicativity of $\Phi_C$, the sign and kernel in the
$\mathbb Z\times C$ stabilizer, the quotient-stack and inertia statements,
effectivization and rigidification, the effective $C_6$ control, and the
regular centralizer-torsor specialization.  The support--exponent ledger,
all nine frozen arithmetic rows, and the interpretation of the source-cycle
shortening and gluing factors agree with those results.

The most important scope issue is now handled correctly.  The
$q=2$ point-cardinality factor $(1-t^3)^{-1}$ is the sole positive cell in
the **locked nine-row family**, not evidence that every local scalar factor
fails.  Proposition 6.2 and the surrounding discussion claim only that no
one reduction type has source support and unit exponent uniformly across
all nine rows.  The collision $r_2=r_4=3$ also blocks reading the
$q=2$ success as a modulus-specific or prime-specific clock.  The A0
conclusion is correspondingly limited to the absence of a common intrinsic
modulus/prime clock.  I found no surviving stronger quantifier in the
reader-facing manuscript.

The evidence and publication package also pass.  The source, PDF, source
lock, scope audit, strict result manifest, and asset review reproduce their
bound digests.  Two isolated clean builds are byte-identical to one another
and to the frozen 19-page PDF.  All pages, fonts, vector figures, citations,
references, labels, and terminal warnings were checked.

One bounded publication defect remains: four reader-facing references to
“Paper 10” or “Paper 11” depend on internal pipeline numbering that an
external reader cannot resolve.  This is a Minor standalone-presentation
issue only; it changes no theorem, evidence row, figure, code, or result.

## Review scope and immutable bindings

This was a source- and artifact-bound review.  Apart from this report, I
changed no manuscript, bibliography, figure, manifest, plan, source, code,
test, experiment, result, or lifecycle record.  I did not invoke the
candidate, rerun any test suite or arithmetic audit, add a modulus, compute
a centralizer, or use the network.  The only executions were the two
explicitly required isolated manuscript builds and read-only document/QA
inspection commands.

The principal bindings reproduce exactly:

| Authority | SHA-256 | Review status |
|---|---|---|
| `paper/manuscript.tex` | `88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5` | exact |
| `paper/manuscript.pdf` and `paper/paper_pre_review.pdf` | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` | exact, 19 pages |
| `paper/INTEGRITY_PRE_REVIEW.md` | `4e82724bdee00b1c31858585c6cd1008106b818ef7cef849661767fbdb1a300f` | exact |
| source lock v2 | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` | immutable |
| proof/formula package | `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948` | immutable; publication quantifier corrected |
| raw exact result | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` | immutable |
| strict result manifest | `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c` | PASS |
| independent scope audit | `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4` | `PASS_WITH_SCOPE_CORRECTION` |
| execution source tree | `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb` | immutable |
| post-run analyzer tree | `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3` | immutable |
| independent asset review | `ebf1644dc03da4c1ccc03972b545688d595ed6da125de2ec831ffcf82e4e69cf` | `ASSET_PASS` |

The manuscript-support digests also reproduce: `math_commands.tex`
`1a057269cb071f5ba026430174b0d1b9c9651932ff2c8de286f4a8b6164e9a39`,
`build.sh`
`3526ec2fad377a51620d18318dafdd43b59620ce1b9b95fb8c3e41c544fbd27a`,
and `references.bib`
`d88a3de08479c46174831a7d562405835800822850505f455831925ff06691d7`.
The four base paper JSON manifests and pipeline state parse, and the
pre-review integrity graph remains acyclic.

## Strengths

### S1. The general finite-translation theorem is complete and internally consistent

For $X=\coprod_K n_K(C/K)$, the proof obtains the exact point period
$d_K=[H:H\cap K]$, the number of translation cycles
$M_K=[C:HK]$, the source zeta, the coarse quotient zeta, both Burnside
classes, both additive reductions, the labelled stabilizer, and the stack
decomposition from one coherent orbit calculation.

**Evidence Anchor**: `equation: Theorem 4.1 and equations (11)--(22) — finite translation hierarchy, cycle-count identity, action kernel, and stack decomposition`

### S2. Stronger carriers and scalar shadows are kept sharply separated

The manuscript applies $\Phi_C$ only to additive exact-period classes and
then forms a scalar product.  It supplies an explicit multiplication
counterexample, distinguishes the inverse in the $C$-permutation
stabilizer from the enhanced return label, and makes recovery modulo the
action kernel—not unconditional exact recovery—the general result.

**Evidence Anchor**: `equation: equations (7)--(10), (17)--(20), and Appendix B — additive-only reduction, nonmultiplicativity, and labelled stabilizer convention`

### S3. The scope correction is conspicuous and mathematically exact

The abstract, Remark 1.1, Proposition 6.2, the C21-corrected paragraph, the
nine-row discussion, both relevant figures, the Route-A disposition, and
the conclusion all retain the $q=2$ exception and use the correct
family-level quantifier.

**Evidence Anchor**: `table: Proposition 6.2, equation (38), and Table 2 — four support/exponent pairs and the unique locked q=2 point-cardinality success`

### S4. Effectivity, inertia, and rigidification are not conflated

The effective $C_6$ example proves that exact recovery of a labelled
order-six translation does not force a period-six source factor.  The stack
retains static isotropy, effectivization removes only the common kernel, and
componentwise rigidification removes residual static isotropy without
creating dynamics.  The text expressly avoids a universal statement about
all objects called stacky zetas.

**Evidence Anchor**: `equation: equations (23)--(28) and Figure 3 — effectivization and effective C6 control, with trivial/regular boundaries`

### S5. The proof/result firewall and adverse-history record are unusually transparent

The general theorem is proof-sourced; the nine rows are locked controls.
The execution and analyzer trees are separately hashed, the initial
prewrite manifest failure is retained, and the later analyzer closes only
the serialized comparison without changing the raw registered result.  The
separate scope audit is visibly allowed to correct frozen prose rather than
being hidden.

**Evidence Anchor**: `dataset: Table 2, Section 7.2--7.3, and Appendix C — nine exact controls, dual-tree closure, and preserved K005 failure history`

## Critical findings

**None.** No error invalidates the finite-$C$-set theorem, the regular
torsor specialization, or the bounded A0 conclusion.

## Major findings

**None.** No claim requires new computation, a new modulus, literature
reconstruction, or substantial mathematical re-analysis.

## Minor findings

### M1. Internal “Paper 10/11” numbering prevents a fully standalone article

**Problem**: The reader-facing source says “Paper 11 neither ...” in the
prior-art boundary, “No Paper-10 candidate or calculation is rerun here” in
the regular-torsor section, “selected before Paper-11 execution” in the
limitations, and “upstream Paper-10 final PDF” in the provenance table.
These identifiers are meaningful inside the local research sequence but are
undefined in a standalone scholarly article.

**Evidence Anchor**: `text: manuscript.tex:190, 627, 1028, and 1144 — “Paper 11 neither” and three Paper-10/Paper-11 pipeline references`

**Why it matters**: The manuscript otherwise succeeds as an anonymous,
self-contained technical note.  Internal numbering makes the imported
authority and chronology depend on repository context and weakens external
journal fit.

**Suggestion**: Replace the four occurrences with standalone wording such
as “the present note,” “the preceding centralizer audit,” “before the
registered execution,” and “the frozen upstream centralizer-audit PDF.”  If
the preceding audit is meant to be a public companion article, identify it
by scholarly title/citation rather than project sequence number.  Rebuild
and refresh only the manuscript-side downstream hashes; preserve every
frozen source/result authority and do not rerun the candidate or tests.

**Severity**: Minor  
**Confidence**: 5/5 — direct source and rendered-PDF inspection

## Independent mathematical audit

| Claim surface | Verdict | Independent check |
|---|---|---|
| General $C$-set periods and cycle counts | PASS | On $C/K$, $a^j cK=cK\iff a^j\in K$; hence the least period is $d_K=[H:H\cap K]$, and $[C:K]/d_K=[C:HK]$. |
| Source and coarse zetas | PASS | The source factor is $(1-t^{d_K})^{-n_K[C:HK]}$; each $C/K$ is one quotient point fixed from the first iterate, giving $(1-t)^{-\sum n_K}$. |
| Point-exact versus orbit-exact Burnside classes | PASS | $P_m^C=\sum_{d_K=m}n_K[C/K]$.  Every $C$-orbit is setwise fixed, so $\widetilde P_1^C=[X]$ and $\widetilde P_m^C=0$ for $m>1$.  The first depends only on $H=\langle a\rangle$, not its chosen generator. |
| Additive $\Phi_C$ | PASS | For abelian $C$, $\Phi_C([C/K])=\lvert K\rvert$, producing exponents $n_K\lvert K\rvert/d_K$ and $\sum n_K\lvert K\rvert$.  For nontrivial $C$, $u=[C/1]$ has $u^2=\lvert C\rvert u$, so $\Phi_C(u^2)=\lvert C\rvert\ne1=\Phi_C(u)^2$; no ring or power-structure claim is used. |
| $\mathbb Z\times C$ sign and recovery | PASS | For $(j,c)x=ca^jx$, the stabilizer is generated by $\{0\}\times K$ and $(1,a^{-1})$.  Across represented types it recovers $a$ modulo $N=\cap_{n_K>0}K$, exactly iff the action is effective. |
| Stack and inertia | PASS | $[X/C]\simeq\coprod_K n_KBK$; abelianness gives $\sum n_K\lvert K\rvert$ inertia components.  The arrow $a$ naturally identifies translation with the identity functor, so the induced dynamics are static. |
| Effectivization and rigidification | PASS | Replacing $C$ by $C/N$ retains $aN$ and residual $K/N$-isotropy.  Removing the common kernel and then residual component isotropy is distinguished correctly; neither operation manufactures a return period. |
| Effective $C_6$ control | PASS | $C_6/C_2\sqcup C_6/C_3$ is effective, with periods $3,2$ and one cycle of each.  The four scalar outputs are $(1-t^3)^{-1}(1-t^2)^{-1}$, $(1-t)^{-2}$, $(1-t^3)^{-2/3}(1-t^2)^{-3/2}$, and $(1-t)^{-5}$; $BC_2\sqcup BC_3$ has five static inertia components. |
| Regular torsor specialization | PASS | With $X_q\simeq G_q$, $a_q=A\bmod q$, $n_q=\lvert G_q\rvert$, $r_q=\operatorname{ord}(a_q)$, and $m_q=n_q/r_q$, the source is $m_q$ cycles of length $r_q$. |
| Four regular scalar reductions | PASS | The support/exponent pairs are exactly $(r_q,m_q)$, $(r_q,1/r_q)$, $(1,n_q)$, and $(1,1)$. |
| Twists, enhanced return, and groupoid | PASS | The twisted fixer is $g=a_q^{-k}$, hence the $G_q$-permutation label uses $a_q^{-1}$; the enhanced return is $a_q$.  The regular action groupoid is equivalent to a point with trivial inertia, and quotienting shortens each source cycle by $1/r_q$ while gluing $m_q$ cycles. |
| Corrected quantifier and A0 | PASS | Only the locked $q=2$ point-cardinality cell has source support and unit exponent.  The negative claim is uniform across the nine-row family, and $r_2=r_4=3$ makes that local success non-modulus-specific.  No universal all-$q$ scalar no-go is asserted. |

The exact row transcription also passes:

| $q$ | 2 | 3 | 5 | 7 | 11 | 4 | 6 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $n_q$ | 3 | 8 | 20 | 48 | 100 | 12 | 24 | 72 | 60 |
| $r_q$ | 3 | 4 | 10 | 8 | 5 | 3 | 12 | 12 | 30 |
| $m_q$ | 1 | 2 | 2 | 6 | 20 | 4 | 2 | 6 | 2 |

In addition to $r_2=r_4=3$, the ledger correctly records
$r_6=r_9=12$.  Those collisions support the limited non-specificity
argument; they are not promoted into an all-modulus theorem.

## Evidence, lifecycle, and provenance audit

The strict result manifest, raw result, registered claim, registered run,
official report, and independent result review agree on the nine rows and
the one registered execution.  The manuscript does not present the rows as
the proof of Theorem 4.1 or as an exhaustive search over moduli.

The execution/analyzer split is credible and visible.  The first manifest
attempt stopped before writing because the K005 comparison encountered a
serialized list-versus-tuple mismatch.  The separate post-run analyzer
fixed that comparison at its own hashed source node and closed the V2
manifest without changing the immutable raw result or execution tree.  The
post-run scope audit is a third, distinct authority: it found the false
per-row quantifier in frozen prose and supplied the family-level correction
used by the publication layer.  Preserving both adverse events materially
strengthens, rather than weakens, the audit trail.

No forward hash or self-hash was found in the pre-review lifecycle graph.
The current report is the next review node only; it does not mutate or
retroactively certify an upstream artifact.

## Literature, originality, and claim-boundary audit

Mechanical extraction gives **14 unique cited keys, 14 bibliography
entries, and 14 generated `bibitem` records**, with no missing or unused key
and no BibTeX warning.  The four directly imported constructions are
positioned at their actual roles: rational point-order, $G$-permutation,
point/orbit/additive orbifold, and enhanced equivariant zeta constructions.
Zegowitz, Miles, Walton, and Baake delimit quotient and dynamical-zeta
boundaries.  The 2023--2026 references are used as frontier context rather
than as proof authority.

The Walton publication record is correctly given as *Journal of Number
Theory* **192** (2018), 386--405, DOI
`10.1016/j.jnt.2018.03.023`.  The manuscript transparently explains that
the frozen design source contained the incorrect volume/pages and that the
publication layer uses the DOI-authoritative correction.  This is a
bibliographic repair, not an undisclosed scientific change.

The originality boundary is appropriately modest.  The paper does not
claim to invent a new zeta construction, reprove the imported centralizer
classification, establish a universal stacky-zeta no-go theorem, or open
Route B.  It presents a synthesis and retention audit whose strongest delta
is the common-framework comparison and its sharply bounded negative route
decision.  The frozen local 12-word-shingle screen reports no match against
Papers 1--10 or the proposal, but the manuscript correctly treats that as a
project-local heuristic rather than an external plagiarism certificate.
This review performed no new online literature search, so the 4/5
literature-completeness confidence is deliberate.

## Anonymity, declarations, and journal fit

The source, rendered pages, and PDF metadata identify only **Anonymous
Authors**.  I found no affiliation, email, ORCID, grant number,
acknowledgment, repository path, local filesystem path, or author-identifying
PDF metadata.  Reader-facing URLs are scholarly bibliography/arXiv
locations.  The declarations correctly defer author contributions,
conflicts, and funding details to a nonanonymous release and disclose the
bounded use of AI assistance; this does not break the current anonymous
review package.

The natural venue is a specialized technical note, equivariant-zeta audit,
or companion-methods article.  The finite-set calculations are elementary
and several constructions are imported, so a broad novelty-driven venue
would be a poor fit.  That is a significance constraint, not a correctness
defect.

## Deterministic build, typography, and visual QA

I made two separate temporary clean trees containing only
`manuscript.tex`, `math_commands.tex`, `references.bib`, `build.sh`, and the
three referenced figure PDFs, then ran the frozen build independently in
each.  The following artifacts were byte-identical across both trees and
to the workspace/frozen package:

| Artifact | SHA-256 |
|---|---|
| PDF | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` |
| terminal LOG | `89adf923399cb2257d58470c8e2e08514205d0b8389833fa2e8e6c99799a2b1c` |
| BLG | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` |
| BBL | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` |
| AUX | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` |
| OUT | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` |

The final terminal log has no LaTeX/package, undefined-citation,
undefined-reference, overfull, or underfull warning; the BibTeX log reports
zero warning.  Messages from the intentionally unresolved first LaTeX pass
appear in build stdout as expected and are absent from the terminal log.

All 19 pages were rendered and inspected.  There is no clipping, overlap,
missing glyph, broken reference, or corrupt asset.  All three figures are
legible vector graphics, and the nine-row table remains readable.  All 39
font records are embedded, subset, and Unicode-mapped; there is no Type-3
font and no raster image object.  PDF title, author, page size, and security
metadata are clean.  As a nonblocking editorial observation, Table 1 floats
to the top of page 3 between two halves of an introductory sentence; the
sentence remains unambiguous, so I do not count this as a severity-bearing
finding, but a later typesetting pass may keep that paragraph together.

## Dimension scores

These scores are ordinal manuscript-quality judgments, not venue
acceptance probabilities.  The concrete Minor finding controls the
recommendation even though the weighted score exceeds an ordinary
acceptance threshold.

| Dimension | Score | Basis |
|---|---:|---|
| Originality (20%) | 62 | Deliberately modest synthesis/audit contribution; direct prior-art collisions are candidly acknowledged. |
| Methodological rigor (25%) | 94 | General proof, edge cases, sign conventions, effectivity boundaries, and corrected quantifier all close. |
| Evidence sufficiency (25%) | 94 | Immutable rows, separate engines, adverse-history preservation, strict manifest, and deterministic builds. |
| Argument coherence (15%) | 90 | General hierarchy to regular torsor to locked audit to bounded A0 disposition is logically clean. |
| Writing quality (15%) | 88 | Precise and readable; the sole standalone-numbering defect remains. |
| Literature integration | 91 | Fourteen-role bibliography is well bounded; no fresh online completeness search was permitted. |
| Significance and impact | 66 | Useful route-closing and semantic clarification, but narrow and not a new general zeta theory. |
| **Weighted average** | **86** | **Minor Revision because M1 remains** |

## Required revision checklist

1. Replace the four reader-facing `Paper 10`/`Paper 11` labels with
   standalone scholarly wording, or cite an externally identifiable
   companion audit by title/reference.
2. Rebuild in two isolated clean trees and refresh all manuscript/PDF-side
   downstream bindings invalidated by that textual edit.
3. Preserve the immutable source lock, registered claim/run, raw result,
   execution tree, analyzer tree, scope audit, and pre-review PDF.  No
   candidate, test, arithmetic, centralizer, or figure rerun is needed for
   this revision.
4. Submit the revised package to a fresh hash-bound Round-2 manuscript
   review.  Do **not** create or bless `paper_final.pdf` from this Round-1
   report.

## Questions for the authors

1. Is the preceding centralizer audit intended to be a separately citable
   companion paper?  If yes, identify it by scholarly title/reference; if
   not, the neutral “frozen preceding audit” formulation is sufficient.
2. Is the intended outlet a specialist note/companion venue?  The current
   bounded novelty and negative-route framing are appropriate for that
   format but should not be enlarged merely to target a broader venue.

## Devil's-advocate conclusion

The strongest objection is that the manuscript combines known equivariant
zeta constructions with an imported regular centralizer torsor and then
draws an elementary four-cell support/exponent comparison; moreover, an
earlier frozen source review accepted a scalar quantifier that the later
scope audit had to correct.  That objection materially limits novelty and
demands unusually careful trust in the publication boundary.  It does not
defeat the present manuscript.  The general finite-$C$-set hierarchy is
proved rather than inferred from nine rows, the constructions are credited
at their exact roles, the adverse scope correction is disclosed in every
scientifically relevant location, and the final claim is only the
nine-family common-clock failure plus the non-specificity witnessed by the
period collision.  I found no hidden promotion of the frozen per-row error,
no unsupported universal stacky-zeta theorem, and no unresolved
Devil's-Advocate Critical or Major issue.

## Final verdict

**MINOR REVISION — 0 Critical, 0 Major, 1 Minor.**  The mathematics,
q2/family quantifier, literature boundary, frozen evidence, dual-tree
provenance, anonymous presentation, and deterministic 19-page PDF all pass.
Only the four internal sequence-number references require repair.  This is
a manuscript-side wording revision with no scientific rerun or scope
expansion.  Round 1 does **not** authorize finalization; a fresh Round-2
review must verify the standalone wording and regenerated downstream hash
chain.
