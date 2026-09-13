# Paper 13 Independent Publication-Stage Review

**Date:** 2026-08-16 UTC  
**Candidate:** `henon_primitive_cycle_cover_v1`  
**Reviewer role:** fresh, role-separated publication-stage gate reviewer  
**Reviewed scope SHA-256:**
`17f56f7f12333803bc8b27a22e27bc33535dbf777483d8da22f34dee17b04e72`  
**Reviewed publication-lock SHA-256:**
`5fd33a907d4b324c6b56fdb3b70af1315475f44f077d27ba84a17653514a69cb`  
**Canonical verdict:** `PUBLICATION_STAGE_PASS`

## 1. Independence, author stop, and effect of this review

I did not author `notes/PUBLICATION_STAGE_SCOPE.md`,
`experiments/publication_lock.json`, the M5 scope or lock, the stable paper
plan, any source-proof document, any implementation or runtime record, or any
future draft. Before reviewing the publication transition, I read the complete
`paper-writing` skill and its shared writing principles. I then read only the
closed reviewer inputs authorized by the final lock.

I did not open either publication-stage author artifact while it was being
written. After the first author-stop signal, I found a stage-closure mismatch
in two future receipt permissions and issued no verdict or project write. The
author repaired only those permissions, stopped again, and supplied the final
lock hash above. I reread and revalidated the complete final lock. Immediately
before writing this report, I rehashed both author artifacts again and obtained
the exact hashes above, with 25352 bytes for the 482-line scope and 22380 bytes
for the one-line canonical lock.

This report is my sole project write. I performed no scientific recomputation,
did not invoke R100 or either implementation route, did not inspect runtime
records, did not fetch bibliography metadata, and did not edit the plan or any
prospective manuscript artifact.

The pass activates only the anonymous publication-stage permissions stated in
the reviewed scope and lock. It authorizes no identity release, finalization,
submission, external message, repository release, or public upload.

## 2. Complete binding receipt

All fourteen gate-review inputs were regular files. Their paths were relative,
resolved inside the Paper 13 root, and had no symlink component. I independently
reproduced the following hashes and byte counts.

| Role | Project-relative path | SHA-256 | Bytes |
|---|---|---|---:|
| publication scope | `notes/PUBLICATION_STAGE_SCOPE.md` | `17f56f7f12333803bc8b27a22e27bc33535dbf777483d8da22f34dee17b04e72` | 25352 |
| canonical publication lock | `experiments/publication_lock.json` | `5fd33a907d4b324c6b56fdb3b70af1315475f44f077d27ba84a17653514a69cb` | 22380 |
| canonical M5 manuscript lock | `experiments/manuscript_lock.json` | `488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd` | 9154 |
| M5 result-aware scope | `notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md` | `265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307` | 16992 |
| research question | `notes/RESEARCH_QUESTION.md` | `18ccf35df9b0f3b73636044c9400f3d79e8f213af365fb33504fa3524f6fd287` | 12301 |
| sole source-proof package | `notes/PROOF_PACKAGE.md` | `9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9` | 25766 |
| claims/evidence matrix | `notes/CLAIMS_EVIDENCE_MATRIX.md` | `21537ed1ed04abf7e3e1dc7d089a105fc36eb5815d164e1cae840f8c56464890` | 13041 |
| citation verification | `notes/CITATION_VERIFICATION.md` | `08d310cb4c5b8e14810bf06e79e988ecf28b9ef2825868b7f7edfeccdce0e71b` | 27784 |
| novelty assessment | `notes/NOVELTY_ASSESSMENT.md` | `bde37eb93989989d2c55c81b13c6919a9ba367c6f2d7ca2320335fd0df155c6a` | 20383 |
| independent source review R2 | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e` | 15344 |
| independent bounded-result review | `results/INDEPENDENT_RESULT_REVIEW.json` | `a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a` | 4462 |
| independent M5 handoff review | `notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md` | `3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98` | 15574 |
| stable paper plan | `paper/PAPER_PLAN.md` | `3dd625590a16e0fe64f475e5913a3d5f1b9eac9b2883e136f389c049ae5d0911` | 39066 |
| reviewer-only source-lock governance receipt | `experiments/source_lock.json` | `11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469` | 21351 |

The plan has exactly 822 lines and ends in one newline. The source lock was
used only for its reviewer-side governance rehash and strict structural
validation; it was not treated as a manuscript input.

## 3. JSON, self-hash, path, and inventory audit

I strictly decoded the publication lock, manuscript lock, independent result
review, and source lock as UTF-8 JSON. All four had zero duplicate keys, zero
nonfinite numeric values, and no parse error. The publication lock, manuscript
lock, and independent result review reproduced sorted-key compact canonical
JSON byte for byte. The source lock remains its intentionally formatted,
hash-bound JSON representation and strictly parsed without semantic use.

The final publication lock:

- has schema `P13_PUBLICATION_STAGE_LOCK_V1`;
- is exactly one canonical line ending in one newline;
- excludes its own SHA-256 and declares `self_hash_excluded=true`;
- binds the exact scope hash, byte count, and line count;
- contains eleven unique direct-input bindings and fourteen unique gate inputs;
- uses only relative, normalized, nonescaping paths;
- contains no absolute path, backslash alias, empty component, `.` component,
  `..` component, or symlinked existing ancestor; and
- makes every read and write list closed and non-transitive.

Across the final lock I checked 246 declared path occurrences representing 33
unique file paths. None escaped the project root and none had a symlink
component. Before this review was created, `paper/` contained exactly the
stable `PAPER_PLAN.md`; `paper/main.tex`, `paper/references.bib`, the optional
diagram, all ten build outputs, both manuscript-review files, the revision
receipt, the draft manifest, and the draft-integrity review were absent. This
review path was also absent.

## 4. M5 transition and theorem authority

The exact M5 triad remains intact:

- result-aware scope SHA-256
  `265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307`;
- manuscript-lock SHA-256
  `488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd`;
  and
- handoff-review SHA-256
  `3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98`,
  with canonical verdict `RESULT_AWARE_HANDOFF_PASS`.

That handoff authorized only the first closed drafting transition and required
the present separately locked expansion. It did not authorize figures,
builds, finalization, or submission by itself.

The sole theorem authority remains the exact proof package conjoined with the
exact independent R2 `SOURCE_LOCK_PASS`. The research question, claim matrix,
citation audit, novelty assessment, plans, scopes, locks, and reviews constrain
notation, evidence, positioning, and permissions; none enlarges the theorem.

## 5. Independent repeat of the thirteen plan-review criteria

The earlier `PLAN_REVIEW_PASS` was a zero-write message receipt. There is no
durable plan-review artifact, path, hash, or attested file, and I did not rely
on that message as evidence. I reread the exact 39066-byte, 822-line plan and
independently obtained the following results.

1. **Identity and story — PASS.** The title is exactly *Normalized
   Primitive-Cycle Covers in a Degenerating Hénon Family*. The one-sentence
   contribution, What/Why/So-What structure, anonymous specialist audience,
   and proof-first drafting order are explicit.
2. **Claim hierarchy — PASS.** PC1 is the theorem spine and carries most of
   the residual contribution. PC2 is explicitly subordinate and narrower
   after Morton's scalar generator results.
3. **C1--C20 and evidence firewall — PASS.** The six article claim groups
   cover C1--C20 without a gap, and every group points to source proof or a
   narrowly assigned imported theorem. R100 has no theorem role.
4. **Sixteen bridges — PASS.** All sixteen bridges occur in the source order;
   the unique-prime, `e=1`, multiplicity-one, `R_0+S_1`, finite-birational
   exact-fiber chain and the monodromy transfer remain visible in the main
   text.
5. **Monodromy direction — PASS.** The plan displays
   `pi_1(U_0) -> pi_1(U) -> S_r`; the scalar image is a subgroup of the global
   image, and the time-shift centralizer supplies the upper bound.
6. **Separate observables — PASS.** The word-sum proof for `tau` and the
   independently derived inverse-word-product proof for `rho` remain separate
   until the full-`S_r` maximal-stabilizer step.
7. **Rank-one boundary — PASS.** The exact `(d,n)=(2,2)` formulas, linear
   multiplication polynomials, trivial `S_1`, and non-evidence limitation are
   present.
8. **Prior-art boundaries — PASS.** Scalar geometry, wreath monodromy,
   scalar generators, formal trace-spectrum reconstruction, low-period Hénon
   carriers, and bounded cyclic-polynomial computation are assigned to their
   proper sources without a priority claim.
9. **Result scope — PASS.** `RESULT_PASS` is confined to bounded
   implementation consistency and is excluded from proofs, claims, equations,
   abstract, figures, tables, novelty, and scientific conclusions.
10. **Same-family disclosure — PASS.** The exact required paragraph is
    locked once in Section 8 and forbidden from every evidentiary or headline
    location.
11. **Visual policy — PASS.** There are zero experimental figures and result
    tables. The article is complete figure-free, with at most one separately
    authorized definition-only diagram that is explicitly non-evidence.
12. **Structure and style — PASS.** The plan has eight numbered sections,
    Appendices A--C, a 24.5-page mathematical-content budget excluding
    references, closed citation keys, anonymous metadata, and no public
    workflow jargon.
13. **Permission closure — PASS.** The plan itself grants no draft expansion,
    build, review, finalization, identity release, or submission authority.

## 6. Proof and source-scope receipt

The publication scope and plan preserve the complete PC1 conjunction:
`B_n`, `E_n`, `S`, and `S_0` remain distinct; actual exact period is isolated
only as a generic clopen block; the ranks `d^n`, `nu`, and `r` attach to the
correct objects; the relative normalization is finite locally free and
geometrically integral; the scalar point and affine cycle fibers are exact;
and the geometric cycle monodromy is `S_r`, with `S_1` explicitly trivial.

PC2 remains the two separate statements

\[
K(\tau)=F=K(\rho),
\]

with `rho` the ordered pointwise derivative-return matrix trace, never a field
trace or the determinant. Each multiplication characteristic polynomial is
defined on the determinant line, belongs to `A[T]`, and is irreducible of
degree `r` over `K`, without a fiberwise irreducibility promotion.

The sixteen ordered bridges were individually checked:

1. monic coefficient-ring cyclic Groebner reduction and the rank-`d^n` basis;
2. generic etaleness and the generic actual-period idempotent;
3. the Henselian connected lift and one-field identification;
4. excellence, Nagata finiteness, and finite normalization;
5. normal-surface Cohen--Macaulayness and miracle flatness;
6. the unique `a`-adic prime, `e=1`, residue degree, multiplicity-one divisor,
   and `R_0+S_1` nilpotent exclusion;
7. finite birational normality and the exact scalar fiber;
8. constants and geometric integrality;
9. Reynolds invariants, arbitrary base change, rank, and affine quotient;
10. the correctly directed scalar-line-to-global monodromy map and
    time-shift centralizer bound;
11. cyclic invariance and the ordered derivative-return trace;
12. scalar infinity branches with independently derived sum and inverse
    product;
13. separate non-base proofs in all nontrivial degree cases;
14. the full-`S_r` maximal-stabilizer step applied separately;
15. determinant-line characteristic polynomials, top wedge, Vandermonde, and
    generic discriminant; and
16. the direct degree-one boundary derivation.

The boundary is exactly

\[
\nu=2,\qquad r=1,\qquad \tau=a-1,
\]

\[
z_0z_1=(a-1)^2+c,\qquad
\rho=4a^2-6a+4+4c.
\]

The twelve anti-claims also remain global: no formal-to-actual promotion on
every fiber; no everywhere embedded primitive subscheme; no automatic
normalization/base-change compatibility; no every-fiber smoothness,
reducedness, etaleness, or free torsor; no projective reading of the affine
quotient; no reversed monodromy inclusion; no primitivity from non-base
behavior alone; no field-trace or determinant reinterpretation of `rho`; no
non-base or nontrivial-monodromy claim when `r=1`; no arbitrary-Hénon
extension; no finite-case or machine proof; and no novelty credit for occupied
scalar generators or formal trace-spectrum rigidity.

The citation boundary is complete: Gao--Ou carry scalar geometry; Morton
(1998) and Fakhruddin carry scalar geometric wreath monodromy; Morton (1996),
with the bounded 2011 corrigendum scope, carries the occupied scalar generator
results; Cantat--Dujardin carry formal-period trace-spectrum parameter
reconstruction; Endler--Gallas carry low-period Hénon orbit-sum and stability
precedents; and Zhang carries bounded-period cyclic-polynomial precedent.
Priority and universal-absence language remain prohibited.

## 7. Machine-result and same-family firewall

The bound independent result review has schema
`P13_INDEPENDENT_RESULT_REVIEW_V1`, verdict `RESULT_PASS`, and scope exactly
`BOUNDED_IMPLEMENTATION_CONSISTENCY_ONLY`. It records:

- one registered audit;
- no rerun and no rerun permission;
- zero reviewer registered-entry invocations;
- zero reviewer scientific recomputations;
- no machine-proof authority; and
- no proof, theorem-validation, scientific-truth, novelty, or priority claim.

The publication lock sets `r100_invocation_authorized=false`. All publication
roles are barred from invoking, importing, or recomputing either route, the
runtime adjudicator, or any scientific engine. `code/`, `preexecution/`, and
`runtime/` remain recursively denied, and the only readable result path is
the independent bounded-result review.

The exact same-family paragraph is required once in Section 8. It states the
single sealed run, narrow `RESULT_PASS`, non-proof status, one-model-family
correlated-error risk, and absence of cross-model validation. It cannot be
used in any proof, claim, equation, abstract headline, contribution bullet,
figure, table, novelty argument, or scientific conclusion.

## 8. Closed role and write-authority audit

The final role sets match the scope exactly and contain no duplicate path:

| Role | Exact read count | Closure result |
|---|---:|---|
| publication gate reviewer | 14 | PASS; eleven direct inputs, scope, lock, and reviewer-only source-lock rehash |
| draft author | 14 | PASS; may separately reread only the three active source paths |
| optional diagram author | 5 | PASS; no result, runtime, build, or external-asset input |
| deterministic builder | 16 | PASS; three sources, three governance inputs, and ten exact generated paths |
| Round-1 manuscript reviewer | 25 | PASS; Round-0 sources, outputs, and receipt only |
| revision author | 26 | PASS; Round-1 review added, no future Round-1 build receipt |
| Round-2 manuscript reviewer | 29 | PASS; revised sources, revision receipt, and Round-1 build outputs added |
| draft-integrity roles | 31 | PASS; closed pre-existing inventory, no reviewer-only source lock or self-review output |

The exact publication-stage write universe contains only:

- the two now-frozen author governance files;
- this sole gate review;
- `paper/main.tex`, `paper/references.bib`, and the optional
  `paper/figures/architecture.tex`;
- ten named deterministic build outputs;
- the two manuscript reviews and one revision receipt; and
- the draft artifact manifest and independent draft-integrity review.

No directory-wide permission follows from these paths. In particular,
`paper/math_commands.tex`, split sections, classes, styles, build scripts,
data, raster/vector exports, supplements, acknowledgments, `.toc`, `.fls`,
`.fdb_latexmk`, SyncTeX, indexes, glossaries, Biber products, caches, and
temporary images remain unauthorized.

## 9. Figure, build, review, anonymity, and terminal limits

The default article is figure-free. The sole optional visual is a TikZ source
at `paper/figures/architecture.tex`, capped at one definition-and-theorem
architecture diagram. It has no experimental, result, runtime, audit,
certificate, or numerical content; its exact caption says that the diagram is
not evidence. No standalone PDF, SVG, PNG, external asset, second figure,
plot, result table, or machine-evidence display is authorized.

The deterministic build contract fixes pdfLaTeX plus BibTeX, working directory
`paper/`, `TZ=UTC`, `SOURCE_DATE_EPOCH=1786838400`, and
`FORCE_SOURCE_DATE=1`. Each clean build runs the four locked commands in order,
and two clean builds must produce byte-identical PDF hashes. `latexmk`, Biber,
shell escape, networked tooling, and side outputs are forbidden. The receipts
must be canonical JSON and bind source/output hashes and sizes, pages, tool
versions, commands, environment, warnings, fonts, metadata, and the second
clean-build hash.

The PDF checks require the exact safe title, embedded fonts, zero undefined
references or citations, zero missing glyphs, no overfull box above 10 pt, and
no local path, hash, workflow marker, identity clue, or unresolved drafting
marker. Author, Subject, Keywords, CreationDate, and ModDate are empty or
absent; Creator and Producer may contain only fixed tool identifiers.

There are exactly two manuscript-review rounds and at most one revision cycle.
Round 2 must return `MANUSCRIPT_REVIEW_PASS`; otherwise the stage fails closed
and no Round-2 patch is authorized. A later `DRAFT_INTEGRITY_PASS` certifies
only the closed integrity of an anonymous reviewed draft. `paper/main.pdf`
remains a draft, not a camera-ready or submission-authorized artifact.

Author name, affiliation, email, ORCID, acknowledgments, funding identifiers,
identifying repository URLs, institution-specific phrases, and hidden identity
metadata remain forbidden. Finalization, identity release, submission,
supplementary archives, preprint upload, repository release, announcements,
and external messages all remain false and require a new explicit authority.

## 10. Verdict

No final binding drift, malformed JSON, duplicate key, nonfinite value,
self-hash, path escape, symlink, transitive expansion, role-set mismatch,
unauthorized pre-existing output, theorem/result conflation, missing proof
bridge, anti-claim loss, boundary error, citation promotion, priority claim,
same-family omission, visual expansion, build-path expansion, identity leak,
finalization, or submission authority was found.

The exact scope and final publication lock identified above therefore pass the
independent publication-stage gate under their closed, fail-closed contract.

**Final canonical verdict: `PUBLICATION_STAGE_PASS`.**
