# Actual mathematical risk review — ANG-20260915-OST01

**Candidate ID:** ANG-20260915-OST01  
**Date:** 2026-09-15  
**Reviewed status:** ADVANCE — OWNED FIRST-SYMBOL TRACE-CLASS DETERMINANT; FULL-OBSERVABLE AND NATURALNESS LIMITS RETAINED.  
**Review result:** COMPLETE — NO UNRESOLVED MATHEMATICAL BLOCKER; TWO MINORS ADDRESSED.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Actual scope and provenance

The reviewer is the separate invocation
`/root/research_controller/ordered_transfer_owner/ordered_transfer_risk_review`.
The frozen card and proposed claims were visible before the paper existed.
This was not a blind review. The reviewer subsequently read the complete
[paper](../paper.md), [card and appended outcome](../candidate-card.md),
[claim ledger](../claim-ledger.md), [summary](../README.md) and
[evidence index](README.md), then re-read the changed conclusion and
integrity paragraphs. The earlier card-only check was a pre-audit, not
completed manuscript review.

A separate read-only helper,
`ordered_transfer_risk_review/triangular_limit_audit`, checked the
rank-one norms, actual finite-rank range, power-trace limit and determinant
domains from the frozen card. Its result was received after this reviewer
had independently checked those calculations; it did not read an existing
review report or edit files. The present reviewer independently checked
the complete source, all inverse histories, roof and full periodic ledger,
and owns this final manuscript-level assessment.

Both invocations inherited the same model and context. The author and
reviewer communicated mathematical risks before completion. These are
separate invocations with disclosed visibility, not independent error
processes, external peer review or human endorsement. Calibration is
`NOT_CALIBRATED`; venue criteria are `criteria_binding_unavailable`.
No journal-fit or publication-readiness assessment was made. ARS was used
only for bounded evidence, counterargument and limitation discipline,
not a full review panel or publication workflow.

## Criterion-bound mathematical findings

The criteria are the version-1 card and the local same-object/gate rules.
Every row below refers to the actual paper, not to the intended proof.

| Criterion | Actual evidence anchor and independent check | Judgement and limit |
| --- | --- | --- |
| Complete arithmetic source and natural extension | Equations (1)--(3), Proposition 1: the cover-factorization argument derives the atoms; the two coordinate maps recover every compatible inverse history and intertwine the invertible shifts | MEETS. The constant-history extension is an example proving surjectivity, not a selection of histories |
| Full flow and actual roof | Equations (4)--(5), Proposition 2: integer scale translations have uniform nonzero displacement; the full quotient is Hausdorff and complete; all states meet the embedded section with first return log b_0 | MEETS. This is a broadened source/scale flow, not a finite-dimensional symplectic construction |
| Complete periodic multiplicity | Proposition 2 and equation (18): a periodic nondecreasing word is constant; a constant one-sided word has one periodic bilateral lift, although nonperiodic lifts also exist | MEETS. All scales over a constant belong to one circle; repeats are not new primitive packets |
| True full-preimage operator | Equations (6)--(8): every prefix a <= x_0 is included, its weight is the actual predecessor roof, and the local sum is finite and continuous | MEETS for the stated algebraic operator on C(Y_+), followed by its restriction to JH; no unspecified bounded full-observable operator is inferred |
| Declared representation rather than a hidden factor | Section 3 before Proposition 3: the two mixed-tail test states have the same first symbol but are separated by the displayed second-symbol observable | MEETS the disclosure obligation. H is transfer-invariant, not a deterministic first-symbol factor or a faithful description of all tails |
| Trace class and exact norm | Equations (9)--(12), Proposition 3: norm(u_j)^2 = 2^(1-j), norm(ell_j) = 2^(j/2), so the rank-one trace norm is sqrt(2) a_j^(-Re s); the trace-norm limit agrees coordinatewise with the frozen formula | MEETS on Re s > 1. The weighted kernel's factor 1/w_j is correct; the chosen ordinal norm is substantive design |
| Holomorphic family and cutoff control | Equation (11) and the final paragraph of Proposition 3: tail sums vanish uniformly on each compact subdomain; fixed-order derivative series are dominated by convergent logarithm-weighted integer series | MEETS in the stated half-plane. The bound is exact and symbolic, not a finite numerical inference or continuation statement |
| Actual finite-rank tails | Equations (15)--(17), Proposition 4: ran(T_(s,N)) is exactly span(u_1,...,u_N), with T_(s,N)u_l = sum_(j=l)^N a_j^(-s)u_j; the lower-triangular finite matrix retains its full constant tails | MEETS. The finite-rank block argument and power telescoping estimate justify the ordinary traces without finite-state cropping or diagonal substitution |
| Ordinary determinant and domain | Equations (13)--(14): trace-norm finite-rank convergence gives the ordinary determinant; the product converges locally uniformly on {Re s > 1} times C | MEETS. Entire dependence on auxiliary z is not continuation in s; no entire-z logarithm is asserted |
| Same-flow trace/product identity | Equations (18)--(20), Proposition 5: the full periodic classification matches every closed path; the absolute double sum justifies the z=1 logarithm and exact reciprocal orbit product | MEETS. The proof does not assume norm(T_s) < 1 on the whole half-plane and inserts no stability, prime or regularizing weight |
| Negative controls and nontransfer | Section 5 and the final gate table: composite 4, mixed histories, removed ordering, counting-measure failure and generic alphabets are retained; 153/157 are distinguished by their different owner and clock | MEETS. Source-clock naturalness and the chosen representation remain OPEN; no formal Route result is obtained |

These findings establish the correctness of the stated restricted analytic
construction, not an optimality theorem for H or an exhaustive audit of
all possible source-observable spaces. The basic trace-ideal and
finite-rank determinant facts were also checked directly in
[Bornemann, Sections 2--3, especially (2.3)--(2.5) and (3.2)](https://arxiv.org/pdf/0804.2543).
The source-specific arithmetic, inverse-limit, roof and column calculations
are the paper's own proofs, not results borrowed from that reference.

## Minor findings and actual dispositions

| ID | Severity / confidence | Original anchor and minimum remedy | Actual disposition |
| --- | --- | --- | --- |
| M1 | Minor; high confidence from direct heading inspection | Text: the initial complete draft numbered the gate assessment as Section 7 immediately after Section 5. Number the final sections consecutively | ADDRESSED. The current actual headings are Section 6, owner-level gate assessment, and Section 7, conclusion; no mathematical statement changed |
| M2 | Minor; high confidence on the corrected path and current prose | Text: the initial integrity paragraph said the listed ARS path was unavailable without recording the later usable cache path. Preserve the failed attempt while distinguishing subsequent successful access | ADDRESSED. The evidence index records the initial failed path attempt, corrected cache path and author's subsequent full reads; the paper now agrees. This reviewer also actually read the usable SKILL.md and its selected review instructions. This verifies the corrected disclosure, not an independently observed replay of the author's earlier tool history |

No Critical or Major issue was found in the reviewed propositions. The
coverage table above records the specific obligations examined, including
the strongest potential objection: a proper first-symbol space does not
recover all aperiodic tails. That limitation is true and explicitly
conceded; it does not invalidate the proved intertwining or the separately
proved complete periodic trace identity. Conversely, the trace identity
does not erase the limitation or establish canonical arithmetic dynamics.

## Reviewed file identity and handoff

After the two minor corrections, a read-only `sha256sum` of the actual
mathematical core returned:

| File | SHA-256 |
| --- | --- |
| paper.md | d9334077a23b134b4e428f2d63329be90281f2171a8a8d92e118de7e429ff8aa |
| candidate-card.md | 5f66096b904829a9b31f06f8ddbab46bf03b39dff3ba9c73b68fe9f54416d602 |
| claim-ledger.md | 2acaead04a5bd6e5c2c0be2d80032347fcab336afdabb26edb11eaf52a40ffcd |

These identify the files actually reviewed; hashes do not prove the
mathematics. Final local-link and package consistency checks remain the
author/integrator's mechanical receipt in the evidence index. The
reviewer modified only this review file, used no Git operation or
numerical script, and uploaded no manuscript to an external model.

**Decision: ADVANCE the exact first-symbol ordinary Fredholm contract.**
The same-object ledger is intact from the full source and actual roof to
the specified transfer restriction and determinant. Any changed source,
clock, norm or observable representation requires a new contract. Natural
A0, full-observable trace theory, classical geometry, continuation and
target/divisor claims are not established. Formal Route coordinates remain
UNASSIGNED and Route B remains NOT INVOKED; this review authorizes no
additional research or evaluation.
