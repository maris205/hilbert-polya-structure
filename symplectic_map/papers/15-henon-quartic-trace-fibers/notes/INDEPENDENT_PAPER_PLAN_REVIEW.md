# Independent Paper-Plan Review

Date: 2026-08-17 UTC

Candidate: `henon_quartic_trace_fibers_v1`

Reviewed plan: `paper/PAPER_PLAN.md`

## Review identity and authority

This is the fresh independent review of the proof-only Paper 15 paper plan.
The reviewer authored neither the plan nor any of the thirteen locked inputs
against which it was checked. Before the explicit `PLAN AUTHOR STOP`, the
reviewer did not open, list, stat, or inventory the `paper` directory. After
the stop, the reviewer opened exactly the stable plan named above and reviewed
it in full against the thirteen authorized locked inputs, the `paper-plan`
instructions, and the shared writing and venue references.

No web search, scientific execution, code, computer algebra, symbolic engine,
parameter scan, experiment, result, figure, manuscript source, bibliography,
compilation, submission, upload, or external release was performed. The only
write made by this review is this report.

## Bound snapshot

The plan matched the author's stable handoff before and after the full read:

- SHA-256:
  `1b70ec0c37d9d587aa56b97b175c6da2f44e114d9414bf31c9f70534dd209e08`
- bytes: `45894`
- LF lines: `739`

The thirteen locked inputs also retained their source-lock identities:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 8354 | `c30436a0389c88df8f51fe6e226347bfe108aa84b5032841ec0033ffa7a987fb` |
| `experiments/EXPERIMENT_TRACKER.md` | 2955 | `d0e46a2c9a691c33e6f6e523f85367f00e8060c124044e2f011016c0a68f9efb` |
| `experiments/source_lock.json` | 26920 | `802fc883cde85cd6312e8a31e0728dc01b493c640c8918d9eacc497f44cac7be` |
| `notes/CITATION_VERIFICATION.md` | 13630 | `d84f4b523a7fee3e8f5fa8f2c4c898dbf62e3fd9528154fdd991d82c150c3609` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 9343 | `928f0923bbfddd9294508a427bfcbcbd259591cac4c136bd4effb15bd86ed109` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 12529 | `55789c4a7c62e4577b655399e7fe8247fe641381e50876d6ebad9bce1f0e8b6e` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 12014 | `39ef31d1dac337fe9856fd9d8f40f756b30730a683db43c1d9b7e183236c6f63` |
| `notes/NOVELTY_ASSESSMENT.md` | 9878 | `c0b7a102d0d63dcb71d58bdbe460e59988fbf303a10f540a0221275fd34c5eb2` |
| `notes/PROOF_PACKAGE.md` | 29436 | `f99d14bc18bd160e5d55e6254e4a2957dda40adbc2a680970506a6ecca5a42ed` |
| `notes/RESEARCH_QUESTION.md` | 8641 | `a287da2bebfa89b02dd7a83d13129e442b51d5780ccbc01c90eca93ad169e082` |
| `refine-logs/FINAL_PROPOSAL.md` | 9331 | `97daded29a79a1b19b828c4704187fa9c70bdac7448382a72b1df8c0f773ab21` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4842 | `043ca69894386ab5040099138780cc6801ba39ff0b088a2ba3f274ef263cb1a0` |
| `refine-logs/REVIEW_SUMMARY.md` | 7112 | `ab479b99e6fbf1b8f66b719df01d8abfbc97da30a8feb1c0fb1b77bab16ac0bb` |

## Binary verdict

The plan passes every paper-plan gate. It is a coherent, feasible plan for
the strengthened unified theorem package. It does not revive the rejected
naked-cutoff note, hide a proof dependency in an appendix, or widen the
locked theorem scope.

Verdict: `PAPER_PLAN_PASS`

This verdict makes the plan eligible only for a separately authorized and
separately frozen publication-stage contract. It does not itself authorize
manuscript text, LaTeX, bibliography, figures, tables, code, scientific
execution, results, compilation, release, submission, or upload.

## Narrative and front-matter audit

| Gate | Finding | Verdict |
|---|---|---|
| Stable title | The title is exactly **Low-Period Trace Fibers of Quartic Generalized Hénon Maps**, matching the source lock and avoiding an unsupported priority or injectivity claim. | PASS |
| One-sentence contribution | The sentence contains the full dependent chain: pure fixed traces bound Jacobians, the exact lower bad fiber is identified, period three separates its residual coordinate, and quasi-finiteness follows. | PASS |
| One technical story | Parts A, B, and C are explicitly presented as successive necessities, not as three unrelated contributions. | PASS |
| Naked cutoff control | The plan forbids framing the article as a short note whose only content is \(P_{\mathcal H^1}(4)=3\). The cutoff appears as the consequence of the full chain. | PASS |
| What / Why / So What | The abstract and introduction instructions identify the problem, hidden-Jacobian obstruction, exact lower failure locus, and consequence before technical preliminaries. | PASS |
| Prior-art boundary | Cantat--Dujardin receive immediate credit for the known exceptional curve, its lower-period blindness, general rigidity, and an unspecified cutoff. | PASS |

The abstract plan is concrete and self-contained. Its first sentence may state
the cutoff because the remaining four sentences are required to expose the
bridge, exact failure locus, formal-period mechanism, and scoped guarantee.
This is front-loading of the unified result, not reversion to the rejected
naked theorem.

## Scope and formal-convention audit

The plan preserves every locked boundary:

1. Part A is over an algebraically closed field of characteristic zero.
2. Parts B and C are over \(\mathbb C\).
3. The global source is only the single-factor monic-centered
   \(\mathcal H^1_4\), together with its finite residual quotient
   \(\mathcal M^1_4\).
4. The Jacobian is \(-a\) and is never supplied as pure trace input.
5. The trace targets use formal-period zero-cycles, elementary symmetric
   coordinates, and scheme-theoretic multiplicities.
6. The quartic formal degrees \(4,12,60\) are explicit.
7. The conclusion is quasi-finiteness, not injectivity, global uniqueness,
   exact degree, or a branch statement.
8. The second period-three power sum is confined to the already isolated
   exceptional curve \(E\).

The notation plan also prevents the two meanings of \(q\) from colliding by
reserving \(q=p-sx\) and writing the period-three derivative as \(q_L\).
The pointwise and cyclewise moments are named separately, and division by
three is delayed until after formal subtraction and the length-60 result.

## Main-text proof-visibility audit

| Required bridge | Main-text placement | Finding | Verdict |
|---|---|---|---|
| Pure fixed traces determine \(C_f\) | Lemma 3.1 | The fixed equations, finite algebra, derivative matrix, and characteristic polynomial are all required in the main text. | PASS |
| \(C_f'(s)=0\) | Lemmas 3.2--3.3 and Theorem 3.4 | Both the squarefree residue identity and the nonreduced local-factor proof are complete; division by \(C_f(s)\) is expressly forbidden in the nonreduced case. | PASS |
| Jacobian candidate bound | Corollary 3.5 | Characteristic zero, degree \(d-1\), \(J=s-1\), and the quartic bound three are all visible. | PASS |
| Cantat--Dujardin ordering | Proposition 4.1 | The plan forces pure-trace enumeration before applying Theorem 4.2 separately to fixed candidates with \(a\ne1\). | PASS |
| Nonreduced period two | Proposition 4.2 | The length-16 tensor algebra, trace element, embedded length-4 formal fixed cycle, scheme subtraction, and length 12 remain in the main text. | PASS |
| Five quartic partitions | Propositions 5.1--5.5 and Lemma 5.4 | \([1111]\) alone uses Sugiyama; \([31]\), \([211]\), \([22]\), \([4]\), ordering choices, and every boundary are direct and explicit. | PASS |
| Exact lower bad locus | Theorem 5.7 | The \(C_f(T)=T^4\) argument rules out an unseen \(a\ne1\) component before the pointwise quasi-finite conclusion. | PASS |
| Period-three algebra | Proposition 6.1 | Rank 64, cyclic signs, equality of the complete-intersection Jacobian and derivative trace, and the exponent \(\operatorname{Tr}(M_{t^2})=\operatorname{Res}(t^3)\) are required. | PASS |
| Two-term support | Lemma 6.2 | Weights, separated-algebra removal, both Puiseux cluster types, diagonal nilpotence, and continuation to \(L=0\) remain visible. | PASS |
| Exact coefficients | Propositions 6.3--6.4 | Both independent slope routes and the constant recurrence certificate retain their definitions, decisive values, signs, and final arithmetic in the main text. | PASS |
| Nonreduced period three | Proposition 6.5 and Corollary 6.7 | Fixed-algebra nilpotence, multiplicities two and four, local exact order, lengths 64 and 4, residual length 60, and delayed orbit normalization are explicit. | PASS |
| Finite fibers to quasi-finite | Theorem 7.1 and Corollary 7.2 | The two lower-fiber cases are separated before applying the finite-type finite-fiber criterion. | PASS |
| Residual quotient and sharpness | Corollaries 7.3--7.4 | The \(\mu_3\)-action, invariant \(L^3\), direct quotient-fiber argument, and positive-dimensional lower quotient fiber are separate steps. | PASS |

No theorem is planned with only a bare statement or a proof sketch. The main
text retains every hypothesis and logical implication needed to audit Parts
A--C without consulting an appendix.

## Appendix and page-budget audit

The plan allocates 25 mathematical-content pages across eight numbered main
sections. This lies within the required 22--26-page range. The densest part,
formal period three, receives 6.5 main-text pages, while the fixed-algebra
lemma, conservative reduction, five-stratum classification, and global
quasi-finite conclusion retain distinct sections. The allocation is demanding
but feasible because the appendices absorb repetitive certificate expansion
rather than theorem logic.

The five appendices have nonoverlapping roles:

- Appendix A expands the finite \(H/A\) slope certificate;
- Appendix B expands the independent tensor--Laurent slope ledger;
- Appendix C expands every terminating normal-form recurrence path;
- Appendix D expands the formal local subtraction at multiplicities two and
  four;
- Appendix E records only auxiliary coordinate, matrix, and valuation detail.

The placement matrix expressly prevents an appendix from introducing a new
assumption, theorem, formal-multiplicity bridge, or missing implication. If
the main text overruns its budget, only line-by-line arithmetic and expanded
substitutions may move. This is the correct proof-first adaptation of the
generic paper-plan template.

## Citation and novelty audit

The citation plan gives each verified primary record one exact role and
preserves version precedence:

- the May 10, 2026 Cantat--Dujardin author PDF controls over arXiv v1;
- Theorem 3.7 supplies no explicit quartic cutoff;
- Theorem 4.2 remains complex, fixed-Jacobian, and restricted to \(a\ne1\);
- Example 4.3 is credited for the known exceptional family and lower-period
  blindness;
- Sugiyama is confined to the no-multiple-fixed-point \([1111]\) stratum;
- Friedland--Milnor, Hutz, Huguin, and the residue reference retain only
  their stated background or method roles;
- Stacks Tag 02NH is used only for the finite-type finite-fiber criterion.

The plan has no unresolved citation marker and forbids generating
bibliographic data from memory. Its collision language is date-bounded and
does not become “first,” “new family,” or a claim about unpublished work.
The fourteen anti-claims preserve every novelty and theorem-scope boundary
from the source lock.

## Evidence, visual, anonymity, and overlap audit

There is no experiment, dataset, baseline, metric, empirical result, hero
figure, or evidentiary visualization. The absence of a hero figure is
justified: three formulas and a short implication chain communicate the proof
structure more clearly. The only optional in-text table is a non-evidentiary
roadmap to the five complete stratum proofs; it cannot replace any argument.
Coefficient tables are exact proof certificates rather than empirical data.

The plan requires an anonymous author block and excludes author names,
affiliations, acknowledgments, grants, self-identifying links, internal paths,
hashes, lifecycle labels, and operational metadata from the public article.
No venue or template is invented before selection. The mandatory overlap
disclosure preserves the exact substantive rule that Paper 15 absorbs the
overlapping Paper 12 theorem and proof and that the two cannot be submitted
in parallel. No public citation to a non-public development artifact is
fabricated, and the absorbed material receives no renewed novelty credit.

## Final checklist

All eighteen checks in the plan's fresh-review list pass:

1. exact safe title: PASS;
2. full dependent one-sentence contribution: PASS;
3. field split: PASS;
4. single-factor normalized scope: PASS;
5. formal targets, degrees, and multiplicities: PASS;
6. complete main-text fixed-algebra proof: PASS;
7. Cantat--Dujardin invoked only after enumeration: PASS;
8. Sugiyama confined to \([1111]\): PASS;
9. all \([211]\) orderings and boundaries represented: PASS;
10. exact lower fiber and non-quasi-finite locus proved: PASS;
11. rank, signs, residue exponent, support, and subtraction visible: PASS;
12. two slope routes and constant ledger correctly placed: PASS;
13. multiplicities two and four, length 60, and delayed division: PASS;
14. finite fibers, finite type, quotient, and sharpness separated: PASS;
15. verified citation versions and roles: PASS;
16. limitations and fourteen anti-claims: PASS;
17. Paper 12 absorption and no-parallel rule: PASS;
18. no experiment, evidentiary figure, computation, or priority claim: PASS.

## Passing effect and downstream fence

No paper-plan blocker remains. The plan is eligible to be bound by a new,
separately authored publication-stage contract and then reviewed under that
contract. Until such an authorization exists, the only admissible paper
artifact remains the reviewed `PAPER_PLAN.md` itself.

This review does not authorize `main.tex`, section files, a bibliography,
figures, tables, generated assets, code, a build, a PDF, finalization,
submission, upload, or external communication. The optional five-stratum
table is still conceptual. Any later manuscript must preserve this plan's
proof placement, scope, citation, anonymity, overlap, and anti-claim controls.

PAPER_PLAN_PASS
