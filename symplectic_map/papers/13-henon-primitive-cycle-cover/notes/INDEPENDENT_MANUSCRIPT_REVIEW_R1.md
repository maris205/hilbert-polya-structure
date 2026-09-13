# Independent Manuscript Review — Round 1

**Candidate:** `henon_primitive_cycle_cover_v1`  
**Reviewed snapshot:** Round-0 anonymous manuscript and deterministic Round-0 build  
**Review date (UTC):** 2026-08-16  
**Round-1 disposition:** **`BOUNDED_REVISION_REQUIRED`**  
**Theorem-level blocker:** **none found**  
**Major mathematical-validity issue:** **none found**

This is the first of the two locked manuscript-review rounds. It is not the
final Round-2 verdict `MANUSCRIPT_REVIEW_PASS`, does not authorize
finalization or submission, and does not release identity information. The
disposition above calls for one tightly bounded revision because several
proof transitions and citation qualifications should be made explicit and a
small set of source/PDF defects should be repaired. None of the required
repairs changes either theorem, the proof strategy, the claim hierarchy, or
the permitted evidence boundary.

## 1. Independence, closed scope, and method

I read the complete Round-1 allowlist and no transitive source: the eleven
frozen post-pass draft inputs, the publication scope/lock/review triad, the
three draft sources, the exact Round-0 build outputs, and the Round-0 receipt.
I did not read `experiments/source_lock.json`, any path under `code/`,
`preexecution/`, or `runtime/`, any other paper, or any unlisted source. I did
not use the network.

The review used the proof-audit and paper-review discipline of the locked
paper-improvement and proof-writing instructions, including their directly
referenced writing principles, but did not invoke an authoring or compilation
loop. I checked the theorem statements, each of the sixteen required proof
bridges, prior-art attributions against the locked citation audit, the full
LaTeX sources, every page of the PDF, the bibliography output, log warnings,
PDF metadata, page allocation, and embedded fonts. All checks were read-only
and wrote only this review. No scientific program, registered route, runtime
adjudicator, symbolic experiment, or R100 entry was invoked or recomputed.
No LaTeX/BibTeX command was run and no PDF was rebuilt.

Strict parsing and canonical-byte comparison passed for the four JSON files
in the allowlist: `experiments/manuscript_lock.json`,
`results/INDEPENDENT_RESULT_REVIEW.json`,
`experiments/publication_lock.json`, and `paper/BUILD_RECEIPT_R0.json`.

## 2. Exact input receipt

The following bindings were independently reproduced before this review was
written.

| Path | SHA-256 | Bytes |
|---|---|---:|
| `experiments/manuscript_lock.json` | `488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd` | 9,154 |
| `notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md` | `265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307` | 16,992 |
| `notes/RESEARCH_QUESTION.md` | `18ccf35df9b0f3b73636044c9400f3d79e8f213af365fb33504fa3524f6fd287` | 12,301 |
| `notes/PROOF_PACKAGE.md` | `9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9` | 25,766 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `21537ed1ed04abf7e3e1dc7d089a105fc36eb5815d164e1cae840f8c56464890` | 13,041 |
| `notes/CITATION_VERIFICATION.md` | `08d310cb4c5b8e14810bf06e79e988ecf28b9ef2825868b7f7edfeccdce0e71b` | 27,784 |
| `notes/NOVELTY_ASSESSMENT.md` | `bde37eb93989989d2c55c81b13c6919a9ba367c6f2d7ca2320335fd0df155c6a` | 20,383 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e` | 15,344 |
| `results/INDEPENDENT_RESULT_REVIEW.json` | `a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a` | 4,462 |
| `notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md` | `3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98` | 15,574 |
| `paper/PAPER_PLAN.md` | `3dd625590a16e0fe64f475e5913a3d5f1b9eac9b2883e136f389c049ae5d0911` | 39,066 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `17f56f7f12333803bc8b27a22e27bc33535dbf777483d8da22f34dee17b04e72` | 25,352 |
| `experiments/publication_lock.json` | `5fd33a907d4b324c6b56fdb3b70af1315475f44f077d27ba84a17653514a69cb` | 22,380 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `a1213f19a6da5531f411e3a7c63ef0f746a6577f021dd360cfc874463b8dec1c` | 19,231 |
| `paper/main.tex` | `5547882d589f9a8920880994acc812248d0e134516937b43f89b30ea008ede0c` | 79,207 |
| `paper/references.bib` | `c792a29b55ad6016460fd42cca7d85554fc8d08836e08670afa4731b5fcd041c` | 7,851 |
| `paper/figures/architecture.tex` | `eabb9c99296c39a3744a57aaa7484522d20175e42dc7577a6e658dc732fed9b9` | 3,185 |
| `paper/main.aux` | `176afa439699fd0fe5ee4ac3e5ec0c7a888825acf53c29b5a1df7fcacb1b6337` | 16,708 |
| `paper/main.bbl` | `83aaef938617f4c1f6b7b4ed9bf6b6a49653b11a4ef6692943da6f0eb7797b66` | 7,917 |
| `paper/main.blg` | `f0120fd2bfd5eb0bdaadd6154df485d7ed3f84549a8a538251cca2f67af4e139` | 1,364 |
| `paper/main.log` | `4f17382ee5a41a291e2209d7e3b1f25316383651b06bf519501e8dde7f9d9232` | 38,628 |
| `paper/main.out` | `838757a680eeb5ef6b3115a65e94801212acb9659c8ae2465e3184db40920af0` | 12,541 |
| `paper/main.pdf` | `f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d` | 517,616 |
| `paper/main_round0.pdf` | `f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d` | 517,616 |
| `paper/BUILD_RECEIPT_R0.json` | `1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548` | 4,942 |

The source, output, receipt, scope, lock, and publication-review hashes match
the supplied publication gate. The publication review records
`PUBLICATION_STAGE_PASS`. The two Round-0 PDFs are byte-identical.

## 3. Required fixes, severity ranked

### Severity 1 — theorem or claim blocker

**None.** I found no counterexample, reversed implication, missing
hypothesis that changes a theorem, or conflict with the frozen PC1/PC2 claim
boundary.

### Severity 2 — bounded proof and citation repairs required before Round 2

#### R1-P1 — Close the Henselian actual-block identification explicitly

**Location:** `paper/main.tex:460–467`, Lemma
`lem:henselian-field`; and `paper/main.tex:1153–1168`, Lemma
`lem:appendix-idempotent-identification`.

The argument correctly excludes every proper-period generic factor from the
lift of the scalar exact-period factor. It also already proves
`dim_K(E_n)=nu` at lines 399–402 and `rank_{R^h}(C)=nu` at lines 1142–1144.
The final identification is nevertheless compressed into “uniqueness,” so
the precise subfactor-and-rank closure is left implicit.

**Bounded repair:** state that the finite-etale algebra over the Henselian
normal local ring extends its generic idempotents uniquely; exclusion of all
proper-period factors therefore places `C[1/a]` inside the base change of the
generic actual-period block; both sides have dimension `nu`, hence they are
equal. Add this at lines 1163–1168 and either mirror it or cite that lemma at
lines 464–467. No new lemma or proof route is needed.

#### R1-P2 — Justify the global relation before defining `D_n -> S/aS`

**Location:** `paper/main.tex:582–592`, equation
`eq:D-to-fiber`; expanded comparison at `paper/main.tex:1318–1349`.

Line 587 asserts that `Phi_{d,n}(z_0,c)` vanishes “on the exact factor.” The
Henselian residue-field identification establishes this after tensoring with
`Q(c)`, but the text does not explicitly descend the equality to the whole
`Q[c]`-algebra `S/aS` before using it to define the displayed map.

**Bounded repair:** immediately before line 588, say that Lemma
`lem:henselian-valuation-descent` gives the relation after tensoring with
`k=Q(c)`, while Proposition `prop:S-flat` makes `S/aS` flat, hence
torsion-free, over `Q[c]`. Thus
`S/aS -> (S/aS) tensor_{Q[c]} Q(c)` is injective, so the relation already
vanishes in `S/aS`. The existing finite-birational normality argument then
applies unchanged.

#### R1-P3 — State the geometric-to-arithmetic monodromy implication

**Location:** `paper/main.tex:922–927`, between equation
`eq:cycle-monodromy` and equation `eq:primitive-fields`.

Equation `eq:cycle-monodromy` gives geometric image `S_r`; the next paragraph
passes directly to a Galois closure of `F/K` and calls its arithmetic
permutation group `S_r`. This inference is correct but unstated.

**Bounded repair:** add one sentence: the arithmetic image contains the
geometric image `S_r` and is itself a subgroup of the ambient permutation
group `S_r`, so it is also `S_r`. The maximal-stabilizer arguments for `tau`
and `rho` then remain exactly as written.

#### R1-C1 — Restore the fixed-degree qualification in the Cantat--Dujardin attribution

**Location:** `paper/main.tex:155–158` and `paper/main.tex:1051–1058`.

The locked citation audit states their reconstruction theorem for a fixed
degree (or fixed multidegree, with the specified multi-Jacobian setup for
compositions). The current phrase “reconstructs Hénon map parameters up to
uniformly finite ambiguity” omits that qualification and can be read as
uniform across all degrees.

**Bounded repair:** use “fixed-degree Hénon maps” in the introductory
description and “within a fixed-degree Hénon parameter space” in the
prior-work paragraph. Preserve the existing distinctions: formal-period
trace multisets, finitely many periods, uniformly finite ambiguity, versus
one fixed actual-period cycle field. There is no need to discuss
compositions unless their parameter space is introduced.

#### R1-C2 — Qualify the Endler--Gallas carriers as quadratic

**Location:** `paper/main.tex:1062–1067`.

Both locked direct precedents concern the quadratic Hénon map, whereas the
manuscript's family allows arbitrary `d >= 2`. The current wording is
ambiguous on that boundary.

**Bounded repair:** begin the attribution with “For the quadratic Hénon map,
Endler and Gallas ...” and retain the separate period-four cubic-carrier and
period-six carrier-plus-stability descriptions.

### Severity 3 — required notation and production repairs

#### R1-E1 — Correct a ring/scheme type mismatch

**Location:** `paper/main.tex:381`.

`B_n -> Spec A is finite flat` is ill-typed. Replace it by either
`Spec B_n -> Spec A is finite flat` or `B_n is finite flat over A`.

#### R1-E2 — Restore the swallowed interword space

**Location:** `paper/main.tex:525`; visible on PDF page 7.

The source `\etaleness for` renders as “étalenessfor.” Use
`\etaleness{} for` (or an equivalent explicit space).

#### R1-E3 — Remove or define the isolated `Y_1(n)` notation

**Location:** Proposition `prop:a-divisor`, `paper/main.tex:547`.

The article defines `D_n` and explicitly avoids an implicit projective
compactification, but never defines `Y_1(n)`. The phrase
`Q(Y_1(n))=Frac(D_n)` therefore introduces an unexplained convention inside
a central proposition.

**Bounded repair:** write simply “Its residue field is `Frac(D_n)`,” which is
all the proof uses. Defining a new curve symbol is unnecessary.

#### R1-B1 — Repair the twelve Stacks Project bibliography records

**Location:** `paper/references.bib:162–244`; warnings at
`paper/main.blg:6–17`; visible on PDF page 27.

All twelve Stacks entries lack a `year` field. `plainnat` consequently emits
twelve `empty year` warnings and renders every entry with malformed
punctuation of the form `URL ..., .`. It also lowercases the proper title in
the rendered bibliography.

**Bounded repair:** add a style-compatible explicit no-date value such as
`year = {n.d.}` to each entry, retain the locked access date in `note`, and
protect the proper title with `title = {{The Stacks Project}}`. If the chosen
bibliographic policy instead places an access year in the `year` field, it
must be made clear that this is not an invented publication date. Do not use
the network or change any locked tag, URL, or access date.

## 4. Sixteen-bridge mathematical audit

| # | Required bridge | Location | Round-1 finding |
|---:|---|---|---|
| 1 | Monic coefficient-ring Gröbner basis and rank `d^n` | `main.tex:349–379`, `lem:groebner`, `eq:Bn-rank` | Pass. The graded leading terms are `z_i^d`, monic division works over `A`, and the standard monomials give the stated free basis. |
| 2 | Generic etaleness and generic actual-period idempotent | `384–419`, `lem:idempotent` | Pass. The scalar generic fiber makes the discriminant nonzero; least period is a Galois-stable clopen subset and Möbius inversion gives rank `nu`. |
| 3 | Henselian connected lift and one-field identification | `421–474`, `lem:henselian-field`; `1114–1179`, `lem:appendix-idempotent-identification` | Mathematically sound, subject to required explicit subfactor-plus-rank sentence R1-P1. Connected normal `C` is a domain and its generic fiber is a field. |
| 4 | Excellence, Nagata finiteness, finite normalization | `485–495`; `1181–1188` | Pass. The cited implications and use of the finite field extension are correctly ordered. |
| 5 | Normal-surface CM and miracle flatness | `497–522`, `prop:S-flat`; `1190–1209` | Pass. Local dimensions, zero-dimensional fibers, CM depth, and regular-base hypotheses are all supplied; rank is `nu`. |
| 6 | Unique `a`-prime, `e=1`, multiplicity one, `R_0+S_1` | `528–578`, `prop:a-divisor`; `1216–1314`, `lem:henselian-valuation-descent`, `lem:R0S1` | Pass. The text correctly separates divisor equality from ideal equality and uses `S_1` to exclude closed-point nilpotents. |
| 7 | Finite birational comparison and exact scalar fiber | `580–618`, `eq:D-to-fiber`, `eq:exact-fiber`; `1318–1349` | Sound after the one-sentence well-definedness repair R1-P2. Once the map is established, torsion-freeness, common fraction field, normality, and finite birational equality are correct. |
| 8 | Constants and geometric integrality | `620–651`, `prop:geometric-integrality`; `1351–1363` | Pass. Relative constants inject into the scalar function field, forcing constant field `Q`; characteristic-zero regularity and flat base change yield geometric integrality. |
| 9 | Reynolds invariants, arbitrary base change, affine quotient | `657–711`, `prop:invariants-base-change`, `eq:quotient-fiber` | Pass. Since `1/n` lies in `A`, the Reynolds idempotent splits `S` as a finite projective direct sum; this survives even nonflat base change. |
| 10 | Correct special-line-to-global monodromy direction and centralizer upper bound | `713–766`, `eq:pi1-direction`, `eq:cycle-monodromy`; `1366–1445` | Pass. The map is `pi_1(U_0) -> pi_1(U)` and the scalar image is contained in the global image. Commutation with the free cycle shift gives the upper bound, so the cycle image is `S_r`. |
| 11 | Cyclic invariance and ordered pointwise derivative-return trace | `775–795`, `eq:tau-rho`, `eq:n2-matrix-check` | Pass. `rho` is kept distinct from field trace and determinant; cyclicity of matrix trace and the order/sign check are correct. |
| 12 | Scalar infinity branches, word sum, independent inverse product | `797–841`; `1447–1574`, `lem:laurent-separation` | Pass. The `tau` and `rho` asymptotics are independently derived and their separating word functions are not conflated. |
| 13 | Separate non-base proofs for `tau` and `rho` | `843–919`, `prop:tau-nonbase`, `prop:rho-nonbase`; `1576–1609` | Pass. The `d>=3` and binary `n>=3` cases are covered, primitive comparison words are supplied, and rank one is excluded from the non-base claim. |
| 14 | Full-`S_r` maximal stabilizer applied separately | `920–943`, `eq:primitive-fields` | Correct, subject to the explicit geometric-to-arithmetic sentence R1-P3. Each observable uses its own non-base proposition. |
| 15 | Determinant line, characteristic polynomials, top wedge, Vandermonde, discriminant | `944–974`; `1612–1791`, `lem:determinant-base-change`, `lem:minimal-characteristic`, `lem:power-wedge-vandermonde` | Pass. Field generation precedes the nonzero power wedge; specialization is not promoted to every-fiber primitivity or separability. |
| 16 | Explicit `(d,n)=(2,2)` degree-one boundary | `322–334`, `prop:C`; `976–1006`; `1813–1854` | Pass. `nu=2`, `r=1`, `tau=a-1`, `z_0z_1=(a-1)^2+c`, and `rho=4a^2-6a+4+4c` agree, and both characteristic polynomials are linear. |

The central valuation ledger deserves an explicit clean finding. Henselian
normalization is connected, the valuation-factor correspondence gives one
prime, etaleness gives `e=1`, the residue field gives `f=nu`, and the degree
formula is exhausted. The manuscript then correctly uses coefficient one
only for generic reducedness and invokes the CM quotient's `S_1` property to
eliminate embedded or closed-point nilpotents. This is not an illicit claim
that normalization automatically commutes with base change.

## 5. Claim hierarchy, novelty, and citation audit

- **PC1/PC2 hierarchy passes.** PC1—the normalized cover, exact scalar fiber,
  and monodromy package—is dominant. PC2 is repeatedly identified as the
  narrower coordinate layer and is explicitly subordinate to Morton's
  occupied scalar generator results.
- **No priority claim appears.** The draft does not use “first,” “previously
  unknown,” “no prior work,” “method novelty,” or a universal-absence claim.
  The preserved novelty disagreement is not represented as resolved.
- **Direct and adjacent roles otherwise pass.** Gao--Ou, Morton 1998,
  Fakhruddin, Morton 1996 and the bounded 2011 corrigendum, Cantat--Dujardin,
  Endler--Gallas, Zhang, Hutz, Doyle--Poonen, Gao 2016, Schleicher, and
  Friedland--Milnor are assigned their locked roles. Morton 1998 wreath
  monodromy is not conflated with Morton 1996 scalar fixed-field generators.
  Arai and Ji--Xie are permissibly absent because their optional discussions
  were not retained.
- **Coverage passes.** All 26 bibliography keys are cited, all 26 citations
  resolve, there are 64 unique labels with no duplicate, and all 94 `ref` or
  `eqref` uses resolve to a source label. Bibliographic content matches the
  locked audit apart from the qualification and rendered-record repairs
  R1-C1, R1-C2, and R1-B1.

No live literature search was performed: citation accuracy and novelty scope
were reviewed solely against the locked citation and novelty audits, as the
Round-1 closed-world contract requires.

## 6. Result firewall, anonymity, structure, and diagram

- The exact mandatory same-family paragraph appears once, at
  `paper/main.tex:1100` in Section 8, and once in extracted PDF text. It does
  not appear in the abstract, theorem statements, proofs, equations, figure,
  table, or novelty positioning.
- `RESULT_PASS` appears only in that paragraph and is described only as
  bounded implementation consistency. The computation is explicitly denied
  proof or theorem-validation status. No R100 identifier, run value,
  certificate, hash, result table, result figure, or scientific inference is
  disclosed in the article.
- The title is exactly **“Normalized Primitive-Cycle Covers in a Degenerating
  Hénon Family”** in source and PDF metadata. The public byline is anonymous.
  PDF Author, Subject, and Keywords are empty; creation and modification
  dates are absent; Creator and Producer are the permitted fixed identifiers.
  No affiliation, email, ORCID, acknowledgment, funding identifier,
  repository, local path, hash, workflow ID, or identity clue was found.
- The article has eight main sections and Appendices A--C. There is one
  definition/theorem architecture figure and no table. The figure source uses
  the required generic/integral/scalar organization and marked/cycle
  distinction. Its caption is the exact locked non-evidence caption, and the
  diagram is not used as proof.

## 7. PDF and deterministic-build audit

The Round-0 receipt records `ROUND0_BUILD_PASS`, two clean builds, and
byte-identical PDFs. Read-only checks agree with it:

- 27 A4 pages: 25 mathematical-content pages followed by 2 reference pages;
- no unresolved citation or reference;
- no overfull or underfull box and no missing glyph;
- 30 fonts, all embedded and subset;
- one figure, zero tables;
- exact safe PDF title and clean anonymous metadata;
- 8 `hyperref` PDF-string token warnings;
- 12 BibTeX empty-year warnings, addressed by required fix R1-B1.

The only visible body-text defect found in the PDF is “étalenessfor” on page
7, addressed by R1-E2. The twelve malformed Stacks punctuation sequences on
page 27 are addressed by R1-B1. I found no LaTeX/PDF disagreement that changes
a displayed formula or theorem statement.

## 8. Nonblocking notes

1. The eight `hyperref` warnings arise from mathematical or accented material
   in subsection headings (notably around source lines 1114, 1289, and 1813).
   The bookmarks remain intelligible. A later source author may replace the
   bookmark forms with plain-text `texorpdfstring` alternatives, but this is
   not required for mathematical correctness or the Round-1 repair boundary.
2. The architecture diagram's vertical arrows are organizational rather than
   literal ring-map arrows. The exact caption expressly says that the diagram
   records definitions and theorem organization only, so no evidentiary or
   direction error results.
3. The manuscript's repeated anti-claims are useful for preventing generic
   conclusions from being promoted to every-fiber statements. They are
   somewhat redundant but should not be shortened during the single revision
   unless the same logical guardrails remain explicit.

## 9. Bounded revision and Round-2 handoff

The revision should be limited to R1-P1 through R1-P3, R1-C1 through R1-C2,
R1-E1 through R1-E3, and R1-B1, followed by the separately authorized
deterministic Round-1 rebuild and receipt. No theorem statement, definition of
`tau` or `rho`, claim hierarchy, citation set, diagram semantics, machine
result, identity field, or scientific computation needs to change.

Round 2 should verify the exact repairs against this review, re-audit all
sixteen bridges on the revised source, and bind the Round-1 build receipt and
PDF. Only that independent round may return `MANUSCRIPT_REVIEW_PASS`.

## 10. Reviewer write and execution inventory

- **Single review write:** `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`
- **Manuscript/source edits:** none
- **Build-output edits:** none
- **Compilation/rebuild:** none
- **Scientific computation or registered-route invocation:** none
- **Network/web retrieval:** none
- **Read outside the Round-1 allowlist:** none

The review file deliberately does not contain its own SHA-256; its final hash
and byte count must be reported externally after the write and after the
source/output rehash.
