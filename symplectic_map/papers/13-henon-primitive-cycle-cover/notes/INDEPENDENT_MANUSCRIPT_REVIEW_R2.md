# Independent Manuscript Review — Round 2

Date: 2026-08-16  
Candidate: henon_primitive_cycle_cover_v1  
Review role: fresh terminal reviewer, separate from the Round-1 reviewer,
revision author, and both builders

## 1. Disposition and review boundary

I find no remaining required repair under the locked Round-2 manuscript
contract.  Every required Round-1 repair is present in the revised source and
rendered artifact, the repairs close the corresponding proof or publication
defect, and the revision introduces no out-of-scope theorem, evidence, claim,
citation, identity, or diagram change.

This was a closed-world, read-only review until the creation of this file.  I
read exactly the Round-2 reviewer allowlist: the prior post-pass author inputs,
the three manuscript sources, the exact Round-0 and Round-1 build outputs and
receipts, the Round-1 review, and the revision receipt.  I did not read
experiments/source_lock.json, code/, preexecution/, refine-logs/, runtime/, any
other paper, or any path reached transitively from an embedded reference.  I
did not use the network.

I ran only local read-only hash, byte-size, path-safety, strict-JSON, source,
log, font, metadata, bibliography, and PDF-text checks.  I did not run
LaTeX, BibTeX, a scientific program, a registered route, R100, a symbolic
experiment, or any theorem computation.  No manuscript source or generated
output was modified.  Immediately before this sole write, a second exact
rehash verified all 29 allowlisted inputs and confirmed that this review path
was absent.

## 2. Frozen input and output bindings

| Path | SHA-256 | Bytes |
|---|---|---:|
| experiments/manuscript_lock.json | 488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd | 9,154 |
| notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md | 265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307 | 16,992 |
| notes/RESEARCH_QUESTION.md | 18ccf35df9b0f3b73636044c9400f3d79e8f213af365fb33504fa3524f6fd287 | 12,301 |
| notes/PROOF_PACKAGE.md | 9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9 | 25,766 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 21537ed1ed04abf7e3e1dc7d089a105fc36eb5815d164e1cae840f8c56464890 | 13,041 |
| notes/CITATION_VERIFICATION.md | 08d310cb4c5b8e14810bf06e79e988ecf28b9ef2825868b7f7edfeccdce0e71b | 27,784 |
| notes/NOVELTY_ASSESSMENT.md | bde37eb93989989d2c55c81b13c6919a9ba367c6f2d7ca2320335fd0df155c6a | 20,383 |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md | 83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e | 15,344 |
| results/INDEPENDENT_RESULT_REVIEW.json | a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a | 4,462 |
| notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md | 3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98 | 15,574 |
| paper/PAPER_PLAN.md | 3dd625590a16e0fe64f475e5913a3d5f1b9eac9b2883e136f389c049ae5d0911 | 39,066 |
| notes/PUBLICATION_STAGE_SCOPE.md | 17f56f7f12333803bc8b27a22e27bc33535dbf777483d8da22f34dee17b04e72 | 25,352 |
| experiments/publication_lock.json | 5fd33a907d4b324c6b56fdb3b70af1315475f44f077d27ba84a17653514a69cb | 22,380 |
| notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md | a1213f19a6da5531f411e3a7c63ef0f746a6577f021dd360cfc874463b8dec1c | 19,231 |
| paper/main.tex | f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce | 80,689 |
| paper/references.bib | 005edd30410ffd8b9b9851e9008636aed9bcddba3195af550bd6daed0529a19b | 8,175 |
| paper/figures/architecture.tex | eabb9c99296c39a3744a57aaa7484522d20175e42dc7577a6e658dc732fed9b9 | 3,185 |
| paper/main.aux | dcd56fb868640a1207f8f7c2c9d9b9b3d9de460078b89098e0d934c28ddb7592 | 16,780 |
| paper/main.bbl | 1664a96990b3415b471194395b4d4e0d37ccb318013f50bf0e41cd0cd4dd1c9d | 8,037 |
| paper/main.blg | 401ed26512f413fbdbfab267da368164e702c87c2a425eb8afc92f08a2d2a61c | 918 |
| paper/main.log | 998ff0432beb546b56300d41a6a7b5295265de217127c0232a2b1b88b50e9c7b | 38,628 |
| paper/main.out | 838757a680eeb5ef6b3115a65e94801212acb9659c8ae2465e3184db40920af0 | 12,541 |
| paper/main.pdf | 4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09 | 519,969 |
| paper/main_round0.pdf | f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d | 517,616 |
| paper/main_round1.pdf | 4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09 | 519,969 |
| paper/BUILD_RECEIPT_R0.json | 1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548 | 4,942 |
| paper/BUILD_RECEIPT_R1.json | 5480ab22ebc7c9676395f9309baae15aa406f73f0cfa3e4901f288fb3e94ca51 | 5,445 |
| notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md | aaa77a37a8d8a8fccedd18073f346312b1ea0245447bbf1b0f5c60095809848c | 22,525 |
| notes/MANUSCRIPT_REVISION_R1.md | 44f081e3f9497c460ed3101dee5b7ba007bfe6022ded1abe8e0391202b8e2725 | 6,120 |

The five JSON artifacts in this allowlist parse strictly as UTF-8 without
duplicate keys or nonfinite values.  Their compact/sorted canonical form,
terminal newline, and applicable self-hash exclusion agree with their
contracts.  Every reviewed path is a regular non-symlink file under the paper
root; the closed lists were not expanded.

## 3. Exact Round-1 repair verification

| Repair | Revised location | Round-2 finding |
|---|---|---|
| R1-P1 | main.tex 465–474 and 1170–1204 | PASS.  The Henselian lift is explicitly placed as a direct subfactor of the base-changed generic actual-period block; the two displayed dimensions are both ν, so the subfactor is the whole block.  Faithful-flat persistence of idempotents then proves that E_n is one field. |
| R1-P2 | main.tex 594–605 | PASS.  The dynatomic relation is first proved after localization, flatness supplies Q[c]-torsion-freeness, and injectivity descends the relation before the homomorphism D_n → S/aS is defined. |
| R1-P3 | main.tex 936–940 | PASS.  The arithmetic permutation image is stated to contain the geometric S_r and to lie in the ambient S_r, so equality follows before the maximal-stabilizer argument. |
| R1-C1 | main.tex 155–158 and 1067–1074 | PASS.  Both Cantat–Dujardin descriptions now say fixed-degree and retain the finite-period, uniformly finite-ambiguity scope. |
| R1-C2 | main.tex 1079–1084 | PASS.  The Endler–Gallas carrier attribution is expressly restricted to the quadratic Hénon map. |
| R1-E1 | main.tex 381 | PASS.  The type-mismatched morphism wording is replaced by the correct statement that B_n is finite flat over A. |
| R1-E2 | main.tex 531–533 | PASS.  The source and PDF contain the restored space in “étaleness for”; “étalenessfor” is absent. |
| R1-E3 | main.tex 550–555 | PASS.  The undefined Y_1(n) convention is gone from source and PDF; only Frac(D_n), which is what the proof uses, remains. |
| R1-B1 | references.bib 162–256 | PASS, 12/12.  Every Stacks record has protected title {{The Stacks Project}} and year={n.d.}; all twelve keys, URLs, tags, and 2026-08-16 access notes are retained.  The BibTeX warning count is now zero. |

I independently compared the Round-0 and Round-1 PDF text at token level.
All substantive visible changes are induced by P1–P3, C1–C2, E1–E3, and B1;
the only additional change is consequent line wrapping/hyphenation.  The
theorem statements, definitions of τ and ρ, PC hierarchy, mandatory paragraph,
figure source and semantics, citation-key set, and anonymous identity fields
do not drift.

One locked, nonblocking rendering observation is recorded for completeness.
Because the exact R1-B1 no-date value ends in a period, plainnat appends its
own record-ending period and displays “n.d..” on page 27.  This is deterministic
style output, not a missing date, broken citation, or metadata error.  R1-B1's
bounded acceptance conditions are satisfied literally and semantically:
12/12 explicit no-date values, 12/12 protected titles, 12/12 unchanged access
notes, and zero BibTeX warnings.  It does not create a further locked repair.

## 4. Proof and theorem audit

I re-audited the revised manuscript against all sixteen ordered bridges, not
only the edited passages.

| # | Required bridge | Revised manuscript finding |
|---:|---|---|
| 1 | Monic cyclic Gröbner basis over A | PASS.  Graded leading monomials z_i^d are pairwise coprime, monic Buchberger reduction is over the coefficient ring, and the standard monomials give rank d^n. |
| 2 | Generic étaleness and actual-period idempotent | PASS.  A separable scalar generic fiber makes the discriminant nonzero; the Galois-stable clopen least-period-n subset descends and has Möbius degree ν. |
| 3 | Henselian connected lift and one-field identification | PASS.  The exact scalar field lifts to a connected normal finite-étale domain, P1 identifies its generic fiber with all of E_n after base change, and idempotent descent closes the field claim. |
| 4 | Excellence/Nagata finiteness | PASS.  Excellence, the Nagata property, and finite normalization are invoked in the correct order. |
| 5 | Normal-surface Cohen–Macaulayness and miracle flatness | PASS.  S_2 in local dimensions at most two gives Cohen–Macaulayness; local dimensions and zero-dimensional fibers supply finite flatness and rank ν. |
| 6 | Unique a-adic prime, e=1, and R0+S1 | PASS.  Henselian valuation descent yields one height-one prime, residue degree ν and ramification index one; the multiplicity-one divisor gives R0 and the Cohen–Macaulay quotient gives S1, excluding closed-point nilpotents. |
| 7 | Finite birational exact scalar fiber | PASS.  P2 constructs D_n → S/aS only after the relation descends; common fraction field, normality of D_n, and integrality give the ring isomorphism rather than assuming normalization commutes with base change. |
| 8 | Constants and geometric integrality | PASS.  Constants inject into Frac(D_n), geometric integrality of D_n forces constant field Q, and characteristic-zero regularity plus flat base change proves geometric integrality of S. |
| 9 | Reynolds invariants and arbitrary base change | PASS.  Since n is invertible, the averaging idempotent splits S, survives arbitrary base change, gives rank r, and identifies the affine scalar quotient. |
| 10 | Correct scalar-to-global monodromy and centralizer | PASS.  The fundamental-group map is directed from the scalar good locus to the global good locus, so scalar image is a lower bound; commuting with the global shift gives the wreath-product upper bound. |
| 11 | Cyclic invariance and ordered derivative-return trace | PASS.  The orbit sum and the pointwise matrix trace are distinguished from field trace and determinant, and M_{n-1}⋯M_0 has the chain-rule order. |
| 12 | Scalar branches and independent leading invariants | PASS.  Hensel/implicit lifting indexes primitive words; τ uses the word sum, while a separate ordered-matrix induction gives the inverse-product leading term for ρ. |
| 13 | Separate non-base proofs | PASS.  The d≥3 one-exception words and the d=2 one-minus/two-adjacent-minus words are proved primitive and distinguish sums and inverse products separately; r=1 is excluded before either assertion. |
| 14 | Full-S_r maximal-stabilizer generation | PASS.  P3 establishes arithmetic S_r, S_{r-1} is used as a maximal point stabilizer, and the argument is applied once to τ and independently to ρ. |
| 15 | Determinant-line characteristic polynomials | PASS.  The top exterior power gives a basis-free integral polynomial compatible with arbitrary base change; generic generation identifies it with the minimal polynomial, and the Vandermonde/discriminant discussion preserves the generic-versus-fiber distinction. |
| 16 | Exact degree-one boundary | PASS.  For (d,n)=(2,2), ν=2, r=1, τ=a−1, z_0z_1=(a−1)^2+c, and ρ=4a^2−6a+4+4c are derived directly, and both multiplication polynomials are correctly linear. |

The two theorem statements retain the fixed hypotheses d,n≥2 and do not
promote generic, dense-open, or characteristic-zero conclusions into
every-fiber assertions.  PC1—the normalized actual-period cover, exact scalar
fiber, affine quotient, and cycle monodromy—remains dominant in the abstract,
introduction, theorem order, and conclusion.  PC2—the two cycle
coordinates—remains explicitly narrower and subordinate to the cited Morton
scalar-generator results.  The rank-one pair (2,2) is neither used as
non-base evidence nor advertised as nontrivial monodromy.

No theorem, lemma, proposition, corollary, proof bridge, hypothesis, or
conclusion depends on R100, RESULT_PASS, a build receipt, a PDF, or any
generated build output.

## 5. Citations, prior art, and claim discipline

The manuscript has 50 citation commands, 26 unique cited keys, and 26
bibliography entries; the cited-key and bibliography-key sets are identical.
All citations and all 97 ref/eqref uses resolve.  There are 64 unique labels
and no duplicate label.

The locked collision roles are preserved: Gao–Ou supplies scalar smoothness
and irreducibility; Morton 1998 and Fakhruddin supply the scalar
wreath/geometric input; Morton 1996 supplies the scalar fixed-field
generators, with the bounded 2011 corrigendum accurately delimited;
Cantat–Dujardin is fixed-degree trace-spectrum adjacency; Endler–Gallas is
quadratic low-period carrier prior art; Zhang is cyclic-polynomial context;
and the remaining cited sources retain their audited roles.  No scalar result
is relabeled as the paper's contribution.

The manuscript contains no first-in-literature, previously-unknown,
no-prior-work, method-novelty, “we introduce,” all-Hénon-maps, or arbitrary
generalized-Hénon claim.  Its positive contribution is the exact conjunction
proved for the normalized family.  No live literature search or metadata
lookup was performed; this finding is bounded to the frozen citation and
novelty authorities.

## 6. Result firewall, anonymity, diagram, and artifact quality

The mandatory same-family paragraph occurs exactly once in Section 8 and once
in rendered PDF text.  It contains the sole public RESULT_PASS reference and
limits it to bounded implementation consistency, expressly denying proof or
theorem-validation status and preserving the one-model correlated-error
warning.  It is absent from the abstract, claims, proofs, equations, figure,
and bibliography.  The public manuscript contains no R100 identifier, hash,
local path, workflow ID, drafting placeholder, or unapproved internal
evidence language.  The locked registered count remains one, rerun remains
false, and this review did not invoke it.

The architecture diagram satisfies the exact definition-and-theorem-only
contract: one vector TikZ figure, one exact caption, no raster image, no
experimental or result graphic, and an express statement that it is not
evidence.  It separates generic marked points, cycles, integral models, and
scalar fibers; it gives S_1 as trivial when r=1.  There are no tables.

The source has eight main sections followed by Appendices A–C.  The PDF has
27 A4 pages; the locked allocation is 25 content pages excluding references,
with the References heading on page 26 and bibliography on pages 26–27.  All
pages were text-inspected.  The exact safe title is present, the byline is
“Anonymous Authors,” author/subject/keywords metadata are empty, and creation
and modification dates are absent.  Creator and producer are only pdfLaTeX
and pdfTeX.  There is no metadata stream, JavaScript, embedded file, identity
clue, replacement character, null byte, or raster image.

All 30 fonts are embedded, subset, and Unicode-mapped.  The final log has no
LaTeX error, overfull or underfull box, missing glyph, unresolved citation,
unresolved reference, or multiply-defined label.  The eight hyperref
PDF-string token warnings are the same intelligible-bookmark warnings already
classified as nonblocking in Round 1.  The bibliography log has zero warning
and zero error.

## 7. Build preservation and reproducibility

Both build receipts are strict canonical JSON and correctly limit themselves
to reproducibility rather than mathematical evidence.  The Round-0 snapshot
and receipt remain byte-exact:

- paper/main_round0.pdf:
  f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d,
  517,616 bytes.
- paper/BUILD_RECEIPT_R0.json:
  1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548,
  4,942 bytes.

The Round-1 receipt binds the revised source hashes listed above, records two
clean deterministic builds with the locked commands and environment, and
records no forbidden build mode.  The current paper/main.pdf and
paper/main_round1.pdf are byte-identical at
4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09,
519,969 bytes.  Every current auxiliary/output hash and byte size matches the
Round-1 receipt.  These facts verify preservation and reproducibility only;
they are not used in the proof audit.

## 8. Terminal verdict

No required change remains.  Under the fail-closed Round-2 rule, this verdict
authorizes only the next anonymous reviewed-draft integrity step specified by
the lock; it does not authorize finalization, submission, or identity release.

MANUSCRIPT_REVIEW_PASS
