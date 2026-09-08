# Ninth research pass: coordinator adjudication

2026-09-08 UTC. The unchanged five-paper C419–C423 batch now has five
admitted contracts. This is a research adjudication, not a manuscript,
formal Route A evaluation, release certificate or global-priority claim.
The latest user instruction was “确认，下一轮”.

## Dispositions and exact increments

| Lane | Adjudicated result | Original-question status |
| --- | --- | --- |
| CP9, new fixed characteristic-three example | ADMIT ONE: for \(f=X^4+X^6\), infinitely many common preperiodicity parameters occur exactly for constant pairs or equal \(f\)-values, over every characteristic-three field | CLOSED within the frozen all-field/all-pair question; fifth contract |
| AS1, finite spectral-measure route | Auxiliary proof PASS: exact finite positive eigenmeasure and a fully proved counterexample to generic positive-atomic noncancellation | Original whole secondary circle NOT CLOSED; not an extra contract |
| AS1, independent spectral probe | Auxiliary proof PASS: exact linear-in-depth untwisted resolvent obstruction and a nonuniform character-phase gap | No nonreal spectral accumulation or full-sum continuation conclusion |
| AY7, integer structural atlas | Auxiliary proof PASS: forced unit section, integral normalized invariants, complete quotient-order 3/4 strata and exclusion of order 5 | Orders 6,7,8,9,10,12 remain; full atlas NOT CLOSED |

The two AS1 lanes test different mechanisms for the same old question,
not two fresh contracts. AY is also a continuation. The CP9 source-first
screen produced one frozen deep question, not three admitted alternatives.
M1/AS2/IR1/P7 are retained without rerunning their accepted mathematics.
No helper is split off as a sixth paper.

## CP9: separate mathematics, source ownership and admission

The complete [admission review](CP9_ADMISSION_REVIEW.md) records the
coordinator's full reading of the frozen question, author proof, source
ledger, scout report and complete nonauthor review, followed by actual
primary-source checks. Its verdict is ADMIT ONE with zero mandatory issues.
Lee–Nam's three-value reduction and the universal local-height equality,
attributed through their stated Ghioca–Hsia input, remain external.

The residual argument chooses \(\lambda_*=1-a-f(a)\). The first point
has an exact two-cycle for nonconstant \(a\); the forbidden difference
\(f(b)-f(a)=1\) makes the second orbit reach \(\lambda_*\) and escape
at a pole of \(a\), with local height \((\log|a|_v)/36\). Swapping the
marks treats the other sign. The proof also establishes the arbitrary-field
reduction and both sufficiency cases, including a complete elementary
one-point parameter-infinitude argument. Neither the other equal-weight
binomials nor the general colliding-orbits problem is claimed solved.
The exact named residual example and full quantifiers justify a concise
article. Current source checks are bounded, not worldwide priority.

## AS1: a finite measure does not supply noncancellation

The coordinator authored the full [spectral-measure proof](solenoid_boundary/PROOF_PACKAGE.md).
The separately assigned reviewer reconstructed it in the
[complete nonauthor review](solenoid_boundary_review/REVIEW.md).
The coordinator read that entire review: PASS, zero mandatory corrections.
One pre-review typesetting typo was corrected before the final proof hash.

For \(\ell=\lceil k/3\rceil\), each length-\(\ell\) branch has rank at
most one. Nonzero spectral multiplicity is bounded by \(F_{\ell+2}\),
giving a positive atomic measure of total mass at most \(119/55\).
The known trivial-on-\(1+8\mathbb Z_2\) contribution has mass \(11/6\);
the positive residual has mass at most \(109/330\) and no unit-circle
atoms. Coincident interior atoms from other characters are not excluded.

The package also constructs a different finite positive atomic measure
inside the disk, with support accumulating at every boundary point and
all positive analytic moments zero. Its interior generating function is
identically zero. Summable positive weights, dense formal exterior poles,
and even negative real residues for the divided atomwise transform
therefore do not suffice for noncancellation. The exterior atomwise sum
can have genuine poles without being the continuation of the interior
sum: the accumulation circle separates the domains. This measure is not
the arithmetic AS1 measure and does not disprove the original conjecture.
Classical context and access limits remain in the [source audit](solenoid_boundary/SOURCE_AUDIT.md).

The separate author supplied a [414-line spectral probe](solenoid_spectral_probe/PROOF_PACKAGE.md).
The coordinator read and checked it fully and wrote the
[nonauthor review](solenoid_spectral_probe/COORDINATOR_REVIEW.md):
PASS, zero mandatory issues. At every fixed unit \(\zeta\ne1\), the
untwisted weighted-supremum resolvent grows proportionally to
\(\lceil k/3\rceil\), although its only nonzero normalized eigenvalues
are \(1,-\varphi^{-2}\). This is nilpotent memory, not phase eigenvalue
accumulation, and is invisible in traces. The character-phase gap is
explicit but deteriorates with depth. No uniform nonreal spectral or
full-sum continuation theorem follows.

## AY: complete low-order strata, higher orders still open

The coordinator read the full frozen attempt, 400-line
[author proof](adler_yamilov/PROOF_PACKAGE.md), source audit, execution
receipt and complete [independent review](adler_yamilov_review/REVIEW.md).
The review is PASS with zero mandatory corrections. The coordinator
contributed the Tate-model suggestion during research; that is not
mislabeled as blind independent review. The separately assigned reviewer
supplied the actual nonauthor reconstruction.

The maximum-coordinate argument forces \(h=k/D=\pm1\) somewhere on
each nonzero ordinary integral cycle with \(k\ne0\). It gives integer
\(\gamma=C/k,\lambda=L/k\) and \(h_nh_{n-1}\mid k\). The cubic
chord equations then prove:

- Quotient order three: exactly the two signed-divisor families in
  (5.3)–(5.4); native period three for \(\gamma=-1\), six for \(\gamma=1\).
- Quotient order four: only \(k=\pm4\), with the complete families in
  (6.4) and its conjugate, all of native period eight.
- Quotient order five: no ordinary integral periodic lift.

Zeros, both ordinary poles and native least periods remain in scope.
The origin and \(k=0\) pair-swap are inherited. Quotient orders
\(6,7,8,9,10,12\) remain unclassified; no Miller-function/return-multiplier
relation was proved or used. Native periods 3/6/8 are not claimed exhaustive.

## Execution, integrity snapshots and next gate

Research-pass mathematical programs: **0**. Old mathematics, diagnostics,
enumerations and builds rerun: **0**. File reading, patching and hashing
are static work, not experiments. No source PDF was saved, GPU or paid
external reviewer invoked, Git written, or Route B entered. These are
AI-assisted current-team internal reviews, not human peer review.

Successful fresh search submissions: **54** (CP9 author 35, CP9 reviewer
5, coordinator 11: AS1 5 and CP9 6, AY author 3). An earlier three-query
coordinator AS1 call failed with arrival unknown; those three are not
added to the successful total. Exact queries, source opens and access
limits are in the individual audits. Spectral-probe author and AS1/AY
helper reviewers made no new queries. Counts are not novelty scores.

Final SHA-256 snapshots, recomputed by the coordinator:

| Artifact | SHA-256 |
| --- | --- |
| AY author proof | 556f831e7d079ed4baa5c5548511fa46740bf62808854a7aba29bc17fe91fcec |
| AY independent review | 9129397e7d14795812893e986cdde65cf6b0f9096d227259b248b29d097380e2 |
| AS1 measure proof | c94860d7b80f54a31b4875a0ebb21c18c47824a22917df691b383c25b0e8a19b |
| AS1 measure review | 69fb1dfbf2bfa8659b39f45936471636496e452064939ba2da2507ef9602e260 |

One initial attempt to write this adjudication had a JavaScript delimiter
error and executed no patch or shell command; the corrected write is
not a mathematical rerun.

The research gate ends at five admitted contracts. The separately
[approved manuscript plan](../BATCH_PLAN.md) assigns C419–C423 and
authorizes writing, two real manuscript review passes, formal evaluation
and release verification. Those later operations are not included in
this research-pass zero-execution receipt. NO_BAD_EULER_OR_ROOT_NUMBER
remains unconditional.
