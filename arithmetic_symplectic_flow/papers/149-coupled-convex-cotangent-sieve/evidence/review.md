# Separate-context model check — ASFS-20260915-CCS01

Date: 2026-09-15. Reviewed object: the unchanged
[version-1 card](../candidate-card.md) and the complete
[paper](../paper.md), with its [claim ledger](../claim-ledger.md) and
[summary](../README.md).

Candidate status: PRIME-ONLY FOUR-DIMENSIONAL HYPERBOLIC PACKETS AND ORDINARY ZETA ESTABLISHED; CLOCK / TRACE OPEN.

## Review scope and provenance

This is a bounded mathematical-method check in a separate model invocation,
not human peer review or evidence of independent error processes. The reviewer
read the frozen card before the paper and independently checked the displayed
identities. The author's proposed proof outline and control expectations were
visible; the review was not blind. No other review report was used, no external
model upload was performed, and no journal or venue criterion is claimed.
Calibration status: NOT_CALIBRATED. Criteria binding: unavailable.

ARS methodology guidance is used only for evidence-anchored proof and scope
checks, consistent with the bounded task. No formal editorial decision,
publication-readiness judgement or Route evaluation is produced. The reviewer
did not edit the manuscript or candidate card.

## Criterion-bound findings

The criteria below are the frozen card's early tests and the local plan's
same-object, full-state, repetition and analytic-owner requirements.

| Dimension | Judgement | Evidence anchor | Independent check and limit |
| --- | --- | --- | --- |
| Global configuration geometry | MEETS after the verified W1 correction | equation: paper (4)--(6) | Hessian positivity gives strong monotonicity; the quadratic-plus-U potential is coercive for each target and has the required gradient. Local inverse functions therefore assemble into one global smooth inverse. |
| Canonical full lift | MEETS | equation: paper (7) | Inverse-transpose momentum transport preserves the canonical one-form exactly; the inverse exists on every full four-dimensional component. |
| Composite exclusion | MEETS | equation: paper (8)--(9) | In r K_n steps the first-coordinate drift is strictly greater than r(2a(n)-1/2), positive for every composite. This uses the integer witness gap and covers all real states. |
| Prime configurations and momenta | MEETS | equation: paper (10)--(14) | Configuration norm rises strictly off zero; inverse-transpose powers at zero have no eigenvalue one. Neither configurations nor momenta were selected after computing a larger periodic set. |
| Complete primitive and repetition ledger | MEETS | equation: paper (12), (15)--(18) | The phase enforces least period K_p; cyclic quotient gives one packet, while both expanding eigenvalues and their reciprocals give the full four-dimensional monodromy. |
| Ordinary scalar zeta | MEETS | equation: paper (19)--(22) | The integer upper bound proves convergence and the self-contained finite Euler-product argument proves divergence at log 2. Determinant denominators are not substituted for the frozen ordinary weights. |
| Controls and boundaries | MEETS | table: paper section 6 control table | Witness deletion, block cardinalities, shifted divisibility and uncoupling have the stated complete profiles, including n=2. Generic constraint realizability and macrotime limitations remain explicit. |

### Strengths

The full-state exclusion is stronger than a selected zero-section argument:
the only possible periodic configuration is first derived, and its full
momentum equation then has only the zero solution. Evidence anchor:
equation: paper Proposition 3, (12)--(14).

The composite test does not require solving the nonlinear recurrence or
enumerating long periods. Its uniform full-scan displacement excludes every
composite repetition at once. Evidence anchor: equation: paper (9).

The geometric trace-denominator result is kept separate from the ordinary
zeta convention and from an unconstructed operator. Evidence anchor:
text: paper section 5, "The ordinary weights in (19) are still one".

### W1 — Missing addition sign in the minimization potential

Severity: Minor.

Evidence anchor: equation: paper Proposition 1, (6), line containing
2b(n,k)x-Z dot X.

Confidence: 5 — direct differentiation of the displayed intended potential.

At first review, the line after alpha_n U(X) lacked an addition sign before
2b(n,k)x. The formula must be

\[
\Phi_Z(X)=\tfrac12\|X\|^2+\alpha_n U(X)+2b(n,k)x-Z\cdot X.
\]

This correction makes its gradient exactly f_{n,k}(X)-Z, as already used in
the surrounding proof. The issue is a localized transcription error, not a
change to the frozen object.

Adjudication: ADDRESSED. The author inserted the missing addition sign, and
the reviewer reread the corrected equation (6) on 2026-09-15. The derivative
now matches the frozen f exactly. The author also clarified the inverse-
transpose power notation in (14) and distinguished the review-only finite
check from the global proofs. No changed inputs required a numerical rerun.

## Independent finite boundary sanity check

This optional review-only check validates arithmetic block indexing and the
two boundary-sensitive controls for n=2,...,100. It does not compute geometric
orbits or prove an infinite claim, and no mathematical result in the paper
depends on it. Integer arithmetic is exact in JavaScript over this finite
range. The command was run from the arithmetic_symplectic_flow directory;
no standalone script or data file was created.

~~~bash
node <<'NODE'
let tested=0,shifted=0,cardinality=0;
for(let n=2;n<=100;n++){
 const K=Math.max(1,(n-1).toString(2).length-1);
 let a=0,h=0,c=0;
 for(let k=1;k<=K;k++)for(let d=2**k;d<2**(k+1)&&d<n;d++){
   a+=+(n%d===0);h+=+((n+1)%d===0);c++;
 }
 const prime=m=>{for(let d=2;d*d<=m;d++)if(m%d===0)return false;return m>=2;};
 if((a===0)!==prime(n))throw Error('prime selector '+n);
 if((h===0)!==prime(n+1))throw Error('shifted selector '+n);
 if((c===0)!==(n===2)||c!==n-2)throw Error('cardinality '+n);
 tested++;shifted+=+(h===0);cardinality+=+(c===0);
}
console.log(JSON.stringify({range:[2,100],tested,shifted_survivor_labels:shifted,cardinality_survivors:cardinality,mismatches:0}));
NODE
~~~

Observed output:

~~~text
{"range":[2,100],"tested":99,"shifted_survivor_labels":25,"cardinality_survivors":1,"mismatches":0}
~~~

## Assessment and unresolved scope

No substantive mathematical blocker was identified in the operational prime
selector, full periodic ledger, monodromy or ordinary-zeta proof. W1 is
corrected and verified. The same-object ledger remains
intact: one local witness action, full cotangent carrier, unit roof and ordinary
unweighted orbit product.

Hyperbolicity here concerns the classified periodic monodromies. The one-step
eigenvalues approach one as K grows; no uniform global hyperbolicity or Anosov
claim follows. Exact log p timing still fails, the chosen macroclock does not
give logarithmic elementary computation time, and generic predicate
realizability limits canonical arithmetic naturalness. An operator, function
space, trace identity, analytic continuation and target divisor remain open.

Portfolio recommendation: retain the bounded positive result; fork any
changed clock, force or analytic-owner convention. Formal
Route coordinates remain UNASSIGNED and Route B NOT INVOKED.

## Arithmetic receipts

no_recomputable_statistics: This is a theoretical proof paper; no test statistics, sample means, standard deviations, degrees of freedom or inferential p-values were reported. The deterministic finite indexing check above is not a statistical test.
