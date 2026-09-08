# Sixth-pass coordinator adjudication

2026-09-08 UTC. The user said **继续** after the delivered fifth checkpoint.
This pass continued two original full questions, not two new candidates.
The batch remains **M1/AS2/IR1: 3/5 admitted contracts; zero manuscripts,
PDFs, new C-numbers, formal evaluations or A2 promotions**.

## 1. Final separated decisions

| Original question | Mathematical result | Independent-increment disposition |
| --- | --- | --- |
| AF5-C: terminating all-$c$ cyclotomic periodic-point procedure | **PROVED AS STATED**, retaining the external finite-set theorem; every integer parameter, zero coordinate, conductor and least native period remains covered | **REJECT_AS_SHORT_EFFECTIVE_COROLLARY**; no fourth paper slot |
| LY4: all-parameter signed integer third-order Lyness classification | **NOT CLOSED**; new six-step identities and a local noncontraction example are proved, but neither the global section lemma nor all residual returns are exhausted | **NO ADMISSION**; the local obstruction is not a periodic counterexample |

In particular, AF5-C must no longer be described as missing an effective
stopping argument. The fifth-pass open statement is a historical checkpoint
superseded by this proof. Conversely, mathematical completion of AF5-C
does not mean that a fourth independently substantial contract is admitted.

## 2. AF5-C: why the effective gap is actually closed

The [global proof](cyclotomic_algorithm/PROOF_PACKAGE.md) supplies an
explicit procedure for $F_c(x,y)=(y,y^2+c-x)$ on
$\mathbb A^2(\mathbb Q^{\rm cyc})$ for every input integer $c$.
The original freeze expressly allowed a terminating finite algebraic
alternative to conductor/period bounds; no weaker contract is substituted.

The [effective length proof](cyclotomic_sources/EFFECTIVE_LENGTH_LEMMA.md)
gives

$$H=2|c|+4,\qquad
L(H)=H\left(\prod_{p\le4H,\ p\ {\rm prime}}(p-1)\right)(2H)^{2H},
\qquad M=L(H)+2.$$

It proves uniform root-sum length by integral trace decompositions, descent
of a containing-field index, and a bounded branching tree. Padding by
zero sums of lengths two and three gives exactly $M$ roots, including
zero coordinates. No unspecified Loxton constant is used.

The [torsion kernel](torsion_kernel/PROOF_PACKAGE.md) proves a finite
exact rational-Mann/Smith-normal-form procedure, with every connected
component, exact equality and torsion lifting under closed projection.
The coordinator read its entire proof, including the rational Mann lemma;
the unavailable original Mann proof pages do not leave an unchecked
mathematical black box.

Let $T=\mathbb G_m^{2M}$, let $\phi$ sum the two blocks, and let
$\Gamma$ be the computed torsion closure of the full lifted graph.
The corrected, equivalent iteration is

$$V_0=T,\qquad
V_{j+1}=\pi_1\bigl(\Gamma\cap(V_j\times V_j)\bigr).$$

It is a descending chain of closed subsets in one fixed Noetherian torus,
with decidable equality. At equality, all torsion images have integral
bounded-house forward orbits in their **one original finite number field**;
these orbits are finite, and invertibility makes them periodic. Every
required periodic point survives. External finiteness then forces a
constant image on each surviving connected coset. Exact basepoint sums
produce the complete finite point list; its induced permutation gives
least native periods.

This is a proof of a theoretical terminating algorithm. It is **not** an
executed point-list computation, practical runtime claim, numerical atlas,
or closed-form uniform conductor/period theorem. No such claim is needed
for the frozen full mathematical question.

## 3. Why the complete algorithm is not admitted as a paper

The coordinator independently read the decisive primary sections, not
only source summaries. Ji–Xie–Zhang
[v2, §3 Step 3](https://arxiv.org/html/2511.13443v2) already descends
along a torsion correspondence and stabilizes by Noetherianity. KKPR
[§7, Algorithm 7.5 and Theorem 7.6](https://math.mit.edu/~poonen/papers/space_vectors.pdf)
already gives an effective general torsion-closure algorithm. The length
and lattice inputs are classical constructions. These ingredients are
deducted in full; the explicit local proofs do not create extra discoveries.

The non-author review further proves that the torsion closure need only
be computed once. This was incorporated as global equation (4.5), removing
repeated closure computation as a proposed increment. The remaining
contribution is known-whole-torus initialization, exact preservation of
all point representatives, fixed-correspondence pruning and elementary
finite-point extraction. It is a correct and useful effective-corollary
synthesis, but does not clear this batch's substantial-independent-increment
gate. More proof pages, a sample implementation, or splitting its helpers
would not change that judgment.

The coordinator therefore accepts the independent recommendation
**REJECT_AS_SHORT_EFFECTIVE_COROLLARY**. This is not a claim that the final
algorithm is literally printed in a located earlier source, nor a global
novelty impossibility theorem. The bounded ownership evidence is in the
[coordinator audit](cyclotomic_algorithm/OWNERSHIP_AUDIT.md) and the
[arithmetic source audit](cyclotomic_sources/SOURCE_AUDIT.md).
The external non-density input remains the explicitly identified JXZ
preprint; no target arithmetic follows from this source-side algorithm.

## 4. Actual non-author review and correction closure

The coordinator read the entire 358-line
[independent proof/source/increment review](cyclotomic_review/INDEPENDENT_REVIEW.md),
including its final-byte receipt and the complete explanation separating
the two verdicts. The reviewer was not an author of the global proof,
the effective length proof, or the torsion kernel. Its fixed-$\Gamma$
finding and source-ownership corrections were implemented and rechecked.
The final small wording correction distinguishes a fixed number field
from a finite field. **No mandatory mathematical or provenance correction
remains in the reviewed scope.** This is current-team AI-assisted internal
review, not external peer review.

Key pinned SHA-256 identities:

| Artifact | SHA-256 |
| --- | --- |
| Global proof | `cda0ca45a2e4b0485aa1fc31a8af3c5ac8e6ebb73cf1ef60b73258bb81d45178` |
| Effective length proof | `7ea1bb456913cd87e5cabe9a57b7b5cb41d6fafd4b160faf08dddc93a7445102` |
| Torsion kernel proof | `4d58735eafe1c52003eb255d1be273a8fb4b75dc9b65216cc4b6cf65921846d7` |
| Independent review | `a576d0f344d99f1ed4e5aac19087f2c20e12724dd5bdf2a7e4cdb428a2921e71` |

These byte identities locate what was reviewed; they are not themselves
mathematical verification. The global/E/T author proofs retain their
pre-review “pending at this revision” language as pinned author snapshots.
Their **current** review status is superseded by the final independent
review and this adjudication. They are not rewritten solely to change
retrospective status text and invalidate the reviewed byte identities.

## 5. LY4: the exact new result and surviving gap

The coordinator read all 205 lines of the
[new LY4 proof/gap package](lyness_exhaustion/PROOF_PACKAGE.md) and its
complete report, then wrote a separate
[non-author helper review](lyness_exhaustion/COORDINATOR_HELPER_REVIEW.md).
The six-step factorization, both midpoint identities, the positive integer
segment with unbounded local multiplier, and its failed integral extension
are correct within their stated scopes.

The segment at $a=20m+1$ is not periodic: all members lose integrality at
the next or following step. It defeats a local contraction inference,
not the proposed global periodic statement. The implication that every
residual periodic orbit visits $\{1,-2\}$ remains unproved, and even that
implication would leave its full section-return atlas. The inherited finite
clock possibilities do not bound the remaining coefficient/height variables.
No enlargement of the old height-eight alphabet or rerun of accepted strata
was used to conceal this gap.

The helper review is PASS only for its explicitly bounded algebraic scope;
the original all-integer-parameter classification remains **NOT CLOSED**.

## 6. Execution, source limits and next boundary

Four ledgers list 71 query formulations across workers: coordinator 18,
arithmetic source worker 32, torsion source worker 12, independent reviewer
9. Three reviewer formulations were submitted twice, giving **74 actual
query submissions**. These counts are not globally deduplicated or an
exhaustive novelty check. LY4's new hand-algebra lane made no new source
query. Source opens and document checks are not mathematical experiments.

There were **zero mathematical program executions**, no old accepted
proof/census/build reruns, no GPU or paid/external-model job, and no new
manuscript/PDF/formal evaluation. Source records distinguish unavailable
Loxton/Mann original pages, the withdrawn Mello arXiv version, and the
served HTML/PDF date discrepancy for a separate cyclotomic-integer paper.
None is silently promoted to verified original full text or used as an
unproved replacement for the supplied local lemmas.

Retain M1/AS2/IR1 **3/5**. AF5-C should now be retained as a proved source
consequence, not repeatedly reopened as an unresolved effectivity gap or
split into helpers to fill slots. LY4 can only progress through a genuinely
global arithmetic/exhaustion argument. A new paper candidate must bring
independent substance beyond these deducted mechanisms. The five-paper
checkpoint has not been completed; C424 and Route B are not opened.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
