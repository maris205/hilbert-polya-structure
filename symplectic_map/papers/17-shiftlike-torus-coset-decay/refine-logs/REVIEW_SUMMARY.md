# Review Summary

## Review identity and limit

This is the source-design author's adversarial review, conducted under the
`research-review` instructions after the full proof, novelty, citation, and
writing-principles passes. It also binds the independent theorem-lane audits in
the Batch05 idea report. It is **not** represented as the separately required
independent source review, and it creates no source lock.

## Overall verdict

**GO TO INDEPENDENT SOURCE REVIEW.**

The merged article is mathematically unified, supports about 22 substantive
pages without padding, remains material after the Paper16 portfolio deduction,
and has no open author-level proof gap. Dominated and unproved extensions remain
stopped.

## Source intake audit

| Required input | Intake result |
|---|---|
| `BATCH_05_STATUS.md` | Fully read and bound; candidate gate and lifecycle limits preserved. |
| `BATCH_05_IDEA_REPORT.md` | Fully read and bound; corrected theorem, all proof obligations, and all 15 anti-claims preserved. |
| Paper16 `RESEARCH_QUESTION.md` | Fully read; exact planar anchored scope recorded. |
| Paper16 `PROOF_PACKAGE.md` | Fully read; no proof is silently duplicated or claimed as new. |
| Paper16 `NOVELTY_ASSESSMENT.md` | Fully read; portfolio overlap deducted. |
| Paper16 `CITATION_VERIFICATION.md` | Fully read; adjacent literature boundary carried forward only where relevant. |
| Paper16 terminal `REVIEW_SUMMARY.md` | Fully read; terminal lifecycle respected. |
| Paper16 `final_integrity_review.md` | Fully read; terminal PASS and nonparallel status respected. |
| Laurent primary journal source and author note | Exact bibliographic identity and finite-rank/division-group scope checked. |
| Bedford--Pambuccian/Bera primary records | Map provenance checked; no priority claim. |
| Closest current primary sources through 2026-08-17 | Bounded theorem/abstract-level collision search completed. |

## Part A obligation audit

| Obligation | Finding | Status |
|---|---|---|
| Exact `V_m` | `k+m` torus coordinates and equations `0<=n<m` fixed; `T_m` bijection proved. | PASS |
| Scalar orientation | State and recurrence indices agree with the one-based map. | PASS |
| Group-algebra singleton | At least three constant/power characters versus two endpoints; nonzero singleton contradiction explicit. | PASS |
| `P(xi)` split | Nonzero branch kills endpoints; zero branch gives character and scalar copy. | PASS |
| `2m` relation independence | Pivot interval plus disjoint endpoint pairs proves integral independence for all `m<=k`. | PASS |
| Future generation | Every future character copies an initial character. | PASS |
| No gcd | Killed set is `{n-nu mod k}`, a translated interval, not a `-nu` rotation orbit. | PASS |
| Disconnected components | Identity component reduction preserves dimension and removes character torsion. | PASS |
| Sharp subtorus | Explicit recurrence verification at `a=1,P(1)=0`. | PASS |
| Saturation | Projection inverse gives a free quotient lattice and saturated kernel. | PASS |
| Rank-one `T_{k-1}` | Unique free zero-based initial index `k-1-nu`; `Gamma=<2>` family explicit. | PASS |
| Arbitrary characteristic zero | Finitely generated coefficient/group field embeds in `C`; whole field need not. | PASS |
| Arbitrary finite rank | Division-hull lemma proved from a Q-basis. | PASS |
| Infinite torsion | Elementwise torsion powers include `mu_infinity`; no bound or generator assumed. | PASS |

### Adversarial Part A checks

1. If `P(xi_t)=0` in every equation, the proof still has both the middle
   triviality and endpoint-copy relations; the dimension loss does not depend
   on generic scalar values.
2. If `m=k`, the pivot interval has span exactly `k-1`, still too short to
   contain an endpoint pair separated by `k`.
3. If `gcd(k,nu)>1`, no residue is repeated because `n` rather than `n nu`
   varies.
4. If the algebraic subgroup is disconnected, a finite component group cannot
   raise dimension or introduce torsion into the identity-component lattice.
5. Equality is presented as a sufficient family, not a classification.

No Part A blocker remains.

## Part B obligation audit

| Obligation | Finding | Status |
|---|---|---|
| Fixed `k=2,nu=1` | No drift to another type or state orientation. | PASS |
| Trivial-middle nonroot branch | Both endpoint characters forced trivial. | PASS |
| Root-copy branch | Endpoint characters and scalars copied explicitly. | PASS |
| Nonlinear monomial | Two equations force `(d^2-1)u=0`; finite window, not exception. | PASS |
| Support size at least three | Middle singleton; second local equation closes any first root-copy. | PASS |
| Full binomial partitions | `A` plus both nontrivial endpoint-to-power orientations `B,C` are exhaustive. | PASS |
| All two-label words | Five `A` words and four `B/C` words checked. | PASS |
| Unique support pattern | Only `CB` survives and forces lower exponent `p=1`. | PASS |
| Scalar orientations | Both coefficient pairings written before transition composition. | PASS |
| Unique coefficient locus | Composition forces exactly `a=-beta^2`. | PASS |
| Exact `C_d` | All four coordinates forced; direct substitution and uniqueness proved. | PASS |
| `V_3` closure | `A`, `B`, and `C` continuations each contradicted for `d>=2`. | PASS |
| All other supports | Linear, monomial, binomial, and size-at-least-three cases exhaust actual supports. | PASS |
| Geometry versus arithmetic | A coset does not imply infinite intersection for every fixed `Gamma`; compatible example separate. | PASS |
| Scalar sharpness orientation | Correct tuple is `(t^e,t,2t^e)`. | PASS |

### Adversarial Part B checks

1. In a binomial local equation with nontrivial middle character, the two
   middle powers are distinct. Any endpoint-endpoint pairing leaves singleton
   middle terms, so the two recorded orientations are exhaustive.
2. `A` includes both all-trivial scalar behavior and nontrivial root-copy
   behavior; adjacent-word closure does not assume `P(xi)` is nonzero.
3. The resonance scalar condition comes from the second low-character pairing
   `a xi_1=-beta xi_2` together with `xi_2=beta xi_1`; its sign is fixed as
   `a=-beta^2`.
4. Surjectivity of a nonzero character on a one-dimensional algebraic torus
   upgrades containment in `C_d` to equality with `C_d`.
5. A fifth coordinate cannot carry hidden dimension after the first four
   characters are trivial, because the third recurrence forces its character
   trivial.

No Part B blocker remains.

## Laurent scope audit

The journal source is Laurent 1984, Inventiones 78, 299--327,
DOI `10.1007/BF01388597`. The Bordeaux EuDML/JSTOR item is a separate
same-author seminar account, not the journal paper. The exact project input is
qualitative finite-union-of-cosets structure for a division group of a finitely
generated subgroup in a complex torus.

The internal bridge handles:

- finite rank without finite generation;
- arbitrary, possibly infinite torsion;
- arbitrary characteristic-zero ground fields; and
- Cartesian powers needed for `V_m`.

No ESS theorem, quantitative unit equation, height theorem, or effectiveness
claim is needed.

## Paper16 overlap audit

The review applies the strongest portfolio penalty:

- no credit for qualitative planar anchored `T_2` finiteness;
- no claim to improve Paper16's explicit bound;
- no reuse of Paper16's support-one theorem; and
- no absorption or parallel-replacement statement.

Paper14's support-one result is already fully absorbed by Paper16. Paper17
does not revive Paper14 or claim a second absorption.

The retained contribution is still article-sized: exact all-dimensional
torus-coset decay and equality, plus an exact zero-constant phase that Paper16
explicitly excludes.

## Unified-article and page audit

The proposed 22.00 substantive-page budget is credible:

- 6.00 pages establish one common framework;
- 6.00 pages prove and sharpen Part A;
- 7.50 pages classify and close Part B; and
- 2.50 pages handle boundary, related work, and limitations.

Part B is the exact deletion test for the constant character used in Part A,
so it is not an adjacent note. No experiments, long example catalogue, or
appendix is required to reach the page target.

## Fifteen anti-claim review

| # | Anti-claim | Review result |
|---:|---|---|
| 1 | `T_m` itself is positive-dimensional | Excluded; geometry is stated for `V_m`. |
| 2 | Resonance gives infinite `T_2` for every `Gamma` | Excluded; only a compatible example is given. |
| 3 | `a=1,P(1)=0` is necessary for equality | Excluded; stated as sufficient. |
| 4 | A gcd hypothesis is needed | Excluded and disproved by residue bookkeeping. |
| 5 | Forced indices follow a `-nu` rotation orbit | Excluded; translated interval used. |
| 6 | Nonlinear monomial has no finite window | Excluded; `V_2` closes. |
| 7 | Laurent gives an effective bound | Excluded; qualitative only. |
| 8 | Standard character partition is itself novel | Excluded; novelty is the exact recurrence classification. |
| 9 | Positive characteristic, `a=0`, rational maps, arbitrary automorphisms | Excluded. |
| 10 | Support is affine-conjugacy invariant | Excluded. |
| 11 | Finite rank means finitely generated/bounded torsion | Excluded; full division-hull proof included. |
| 12 | Paper17 improves Paper16's explicit bound | Excluded. |
| 13 | Bounded search proves global priority | Excluded. |
| 14 | All maximal/equality cosets are classified | Excluded. |
| 15 | Heights, periodic points, or effective enumeration follow | Excluded. |

## Scores after adversarial review

| Axis | Required | Reviewed score | Verdict |
|---|---:|---:|---|
| Novelty after Paper16 penalty | 7.5 | **8.0** | PASS |
| Standalone/unified article value | 7.5 | **8.2** | PASS |
| Proof confidence without CAS | 9.0 | **9.3** | PASS |

## Residual risks for an independent reviewer

These are rereading targets, not known gaps:

1. independently reconstruct the `2m` integral-independence proof;
2. rederive every `A/B/C` transition without using the author's labels;
3. check the exact original-language formulation of Laurent against the stated
   torus consequence;
4. refresh the bounded current search at any later source-lock date; and
5. verify that any future manuscript preserves all scalar signs and zero-based
   indices.

## STOP list

Do not revive the dominated planar Laurent reproof, gcd phase, effective claim,
Laurent/rational support, mixed-coset classification, arbitrary automorphism
extension, or full equality-coset classification without a genuinely new proof
and a new authorization.

## Final review decision

**AUTHOR REVIEW PASS: GO ONLY TO A SEPARATELY AUTHORIZED INDEPENDENT SOURCE
REVIEW.**

No manuscript, source lock, review artifact, code, data, computation, build, or
submission is authorized by this review.
