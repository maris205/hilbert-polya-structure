# B1 nonauthor admission audit — PC424-L

2026-09-09 UTC. Current-session internal review, independent of A1's
authorship and of the coordinator's source synthesis. This is not
external-model review, human peer review, a formal Route-A evaluation,
or the coordinator's actual admission decision.

## Recommendation

**PC424-L qualifies as one substantial, complete source-system research
contract under WORKFLOW §2. Recommend admission for one integrated paper
after the coordinator records the final bounded source synthesis and
the required attribution.** No additional mathematical theorem or
mathematical execution is requested for this admission judgment.

The core reason is not that the paper has a new finite matrix or an
exact formula. The proved equality answers the original full
polynomial-regularity question, including all odd characteristics, all
parameters, all polynomial degrees, nonreduced periodic schemes, and
ordinary periods divisible by the characteristic. Its new cross-level
coefficient statement resolves the previously explicit gap between
scheme-level detection and ordinary-cycle detection.

The finite-detection corollary strengthens the utility of that same
result. It is **not a second contract or second paper**. This review
does not itself change the admitted-paper count or assign a C-number.

| Gate | Recommendation in this audit |
| --- | --- |
| Mathematical closure of the original contract | **PASS**; no substantive mathematical must-fix identified. |
| Local predecessor subtraction | **PASS**; the accepted old normal-form, cyclic-basis, leading-coefficient and Jacobian facts are inputs. |
| Comparison with the directly inspected closest external sources | **Narrow source-relative increment survives**; substantial inherited machinery must be credited. No universal-priority claim is supported. |
| Complete source gate / final admission | Coordinator to incorporate its equality-theorem search and X2's final report, retaining access limitations. No exact collision is identified in this audit. |
| Substantiality under WORKFLOW §2 | **Qualifies for one integrated paper**, subject to no contrary exact source collision in the coordinator's synthesis. |
| Completed-paper / release gate | **Not met by these proof files**; manuscript, PDF, applicable evaluation and final release verification remain separate work. |

## 1. Exact question and versions actually reviewed

The original
[frozen PC424-L contract](../../../../research_c424_c428/positive_characteristic/FROZEN_CONTRACTS.md)
asks about the entire family
$$
T_{c,h}(x,y)=(x^2+c,y+h(x))\quad\text{on }\mathbb A^2(k),
\qquad k=\overline{\mathbb F}_p,
$$
for every odd prime $p$, every $c\in k$, and every $h\in k[x]$.
Its native clock is one application of this map. With $f_c=x^2+c$, put
$$
K_c=\left\{h:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f_c\text{-orbit }O\right\},
\qquad
B_c=\{Q\circ f_c-Q:Q\in k[x]\}.
$$
It demands $K_c=B_c$ uniformly, or a complete defect classification if
equality fails. Ordinary primitive sums count each distinct point once;
they are not scheme lengths or automatically repeated return sums.

The original contract's equality branch is exactly what the new proof
establishes. Since that branch holds, no additional defect-classification
alternative remains to be completed.

Artifacts read:

- [A1 full proof](../../a1_periodic_normal_form/PROOF_PACKAGE.md), all
  444 lines, including the final finite-detection corollary. SHA256:
  `06d0d06c1798b55d5a052b7ae3874bd176338ff31887a129b80041c5e1147450`.
- [A1 report](../../a1_periodic_normal_form/REPORT.md), including the
  distinction between frozen dispatch wording and completed reviews.
- [E2 independent derivation](../e2_carry_independent/REVIEW.md), fully
  read. SHA256:
  `ee6726f3901864109863143ee732fa9e1598b2f5af45845fc1f60e464bc46f04`.
  E2 covers the core stabilization and equality implication, not the
  subsequently appended corollary.
- [E8 full-author review](../e8_carry_stabilization/REVIEW.md), fully
  read. SHA256:
  `0a7cec693310d7798fdf87014370de2cd191413895e4aec3e8e6774618fff886`.
  E8 covers the complete current proof and corollary.
- The original contract and its
  [unchanged R2 continuation](../../../../research_c424_c428/continuation_round2/positive_characteristic/FROZEN_CONTRACTS.md).
- The actual initial
  [normal-form proof](../../../../research_c424_c428/positive_characteristic/PROOF_PACKAGE.md),
  including the old distinction between arbitrary-function transfers and
  polynomial transfers; and the actual
  [cyclic proof](../../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md),
  Steps 1–5, including its one-level Jacobian counterexample.
- [X2's 272-line source report](../x2_pc_l_sources/REPORT.md), fully
  read. Its broader source inspection is attributed to X2; my own
  primary-source readback is specified in Section 4 below.
- Repository/Hénon/batch instructions, the complete batch skill and
  WORKFLOW, and the active [SCOUT_PLAN](../../../SCOUT_PLAN.md).

## 2. Mathematical gate: why the original closure survives

This admission audit did not merely use the two earlier PASS labels.
I read the authored mechanism and matched its inherited implications
against the actual earlier proofs. I found no contradiction, omitted
parameter stratum, or new assumption needed for the claimed conclusion.

For a normal representative
$v\in V=k\oplus xk[x^2]$ with positive odd leading degree $D$, let
$m=\lfloor\log_2D\rfloor$, and let $E_D$ be its binary support. The
accepted squarefree cyclic basis gives
$$
[P_{E_D}]H_n(v)=a_D\qquad(n>2m).
$$
The new statement is stabilization of a different coefficient:
$$
C_n=[P_{E_D}]\bigl(P_{{\rm all},n}H_n(v)\bigr),
\qquad C_{n+1}=C_n\quad(n\ge3m+4).
$$
The authored weighted paths terminate in one circuit because the source
is initially cleared and the final carry is at most one. Every source
contributing to a nonempty short target lies in
$[-m,m+1]\pmod n$. In the complementary interval, two consecutive
zero outputs force the transition $1\to1$ of weight one. Insertion and
deletion preserve all source/path pairs and their weights, including
lower odd monomials, wraparound sources, and zero weights in
characteristic $p$. The extra source at the new site contributes no
target path. Constants contribute only to the full-support monomial.
These checks justify a uniform identity, not an empirical recurrence.

Ordinary-cycle vanishing supplies only the valid necessary implication
$$
(2^nP_{{\rm all},n}-1)H_n(v)=0\quad\text{in }A_n.
$$
It is sufficient at two consecutive levels: coefficient extraction
gives $2^nC_n=a_D=2^{n+1}C_{n+1}$, and stabilization forces $a_D=0$.
A fixed point then kills the constant normal defect. Telescoping gives
the reverse inclusion. No converse to the Jacobian condition at a
single level is used.

This preserves the difficult cases rather than excluding them:

- $p\mid n$ or a root multiplicity divisible by $p$ introduces no
  division by that integer.
- The parabolic parameter $c=1/4$ is retained despite having a repeated
  fixed root in every iterate polynomial.
- $c=0$ is included, but is not the whole new theorem.
- The full cyclic quotient may be nonreduced; individual coefficient
  functionals are not incorrectly asserted to descend to its reduction.
- The proof covers unbounded polynomial degrees through the explicit
  degree-dependent threshold, not through a finite-degree census.

The two-level corollary also matches its proof. For $\deg h\le M$,
$M\ge1$, take $n=3\lfloor\log_2M\rfloor+4$. The two derivative
divisibility tests, or the ordinary-root return-sum tests, at $n,n+1$
are equivalent to polynomial coboundary membership. A failed test
detects a primitive cycle of length dividing one of those two integers.
It does not require that the primitive length equal $n$ or $n+1$.

The bound $2^{n+1}\le32M^3$ is a degree bound for the two iterate
polynomials. It is not a claim of optimal period cutoff, a measured
running time, or a complexity analysis of every unreduced product in
the displayed tests. No such algorithmic strengthening is needed for
the admission recommendation.

## 3. Local subtraction and the substantial increment

The initial normal form made polynomial membership decidable by
coefficient elimination, but did not establish that ordinary orbit data
detects every nonzero quotient class. Finite-field interpolation gave
field-size-dependent transfer degrees, not one global polynomial
transfer. The earlier full cyclic basis and leading-binary coefficient
proved scheme-level nonvanishing, but the trace could still lie in the
nilradical. The earlier Jacobian annihilation was necessary, with a
documented false converse at a single level. All remain inherited inputs.

The new proof closes that precise unfinished implication, rather than
relabeling any one of those inputs as the answer. It determines the
entire kernel $K_c$ for every allowed base parameter, not merely an
example, a special fibre, a low-degree range, or a list of exceptions.

Under WORKFLOW §2, this is enough substance for **one source
classification/regularity paper**. The result answers when all native
additive periodic obstructions are removed by a polynomial vertical
shear. Its effective finite detection makes the infinite orbit
criterion usable by two explicit algebraic tests. These are meaningful
conclusions independent of the length of the proof or the number of
generated files.

This does not imply that a publicly recognized major conjecture has
been solved. PC424-L is the team's previously frozen complete question;
its significance here comes from its mathematical scope and conclusion,
not from an unsupported historical-open-problem claim. Nor does a new
source-system theorem automatically qualify as an A1/A2 target-arithmetic
success. The route verdict must be evaluated separately.

## 4. Closest-source subtraction and its exact limit

The following primary texts were independently opened and their stated
passages read in this audit; this is additional source checking, not a
claim that every source in X2's report was independently reread here.

**Cattani–Dickenstein–Sturmfels.**
[Computing Multidimensional Residues](https://arxiv.org/pdf/alg-geom/9404011),
1994 preprint, §4, Lemma 4.2, Theorem 4.3 and Algorithm 4.8;
Remark 1.6(iii) was also inspected. These passages supply normal-form
coefficient extraction by residues, the residue pairing, and the
Jacobian trace formula. The pure-power initial-form setting structurally
matches the cyclic quadratic algebra. Although the displayed setup
starts over subfields of $\mathbb C$, the text discusses extension to
other fields. Thus changing the coefficient characteristic is not by
itself a new method. No inspected statement establishes the particular
adjacent-dimension short-support stabilization used here. This is a
source-relative comparison, not a proof that no consequence of the
general theory could yield it.

**Cvitanović–Hansen–Rolf–Vattay.**
[Beyond the periodic orbit theory](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf),
*Nonlinearity* 11 (1998), 1209–1232, §§3–4, especially equations
(25)–(28). These already give finite binomial matrices and explicitly
relate successive multiplier-weighted trace sums. The paper credits
Levin–Sodin–Yuditskii's 1994 work for those matrices. Therefore neither
“finite binomial transfer” nor “comparison of successive cycle lengths”
is a defensible broad novelty claim. The inspected observables are
weighted fixed-point traces, not the stated all-ordinary-orbit
polynomial coboundary criterion. Passing from their formulas to the
specific coefficient stabilization and kernel exclusion still requires
an argument not supplied by the inspected passages.

**Access limits.** X2 records the LSY publisher abstract and its
unavailable full theorem text. I do not upgrade that to an independent
full-text exclusion. X2 also compares recent finite approximate Livšic
results and explicitly distinguishes their smooth/hyperbolic hypotheses
and approximate conclusions from this exact arithmetic claim. Those
broader findings are attributed to
[X2's source report](../x2_pc_l_sources/REPORT.md).

My additional twelve web queries covered polynomial coboundaries over
finite fields, positive-characteristic Livšic statements, polynomial
cohomological equations, periodic orbit sums, and arXiv-indexed variants.
They returned unrelated uses of “coboundary polynomial” and analytic
analogies, but no applicable exact theorem was identified. This is
bounded retrieval evidence, not proof of worldwide novelty. No native
authenticated scholarly-database coverage or complete bibliography is
claimed. No relevant external-library PDF was selected from the local
root paper collection, which belongs to the separate symbolic stream.

The admissible source claim is therefore narrow: the inspected closest
sources contain substantial antecedent machinery, but the exact
uniform ordinary-cycle characterization and its stated stabilization
and two-return certificate have not been identified in them. The
coordinator's parallel search for the unrestricted equality theorem
must be incorporated before recording the overall source gate.

## 5. Required boundaries and remaining gates

No substantive mathematical repair is requested. The following are
admission/presentation requirements, not additional paper questions:

1. Credit the inherited quotient/normal-form/Jacobian machinery and the
   classical residue and finite-matrix antecedents. State the increment
   as the specific stabilization-to-ordinary-kernel theorem, not the
   general invention of periodic trace recurrences.
2. Preserve the source-access limitations. Do not claim “first finite
   Livšic theorem,” “no prior result can imply this,” or a certified
   global-priority result. If an applicable exact collision emerges,
   reopen substantiality instead of using the finite certificate as
   an automatic replacement paper.
3. Keep the all-odd-prime, all-parameter, all-degree and ordinary
   primitive-cycle quantifiers in the principal theorem. Keep the
   finite corollary's two-level and full-return-sum conventions.
4. Count the kernel theorem, carry lemma, finite tests and shear
   interpretation as one integrated contribution. A1 and A2 are
   routes to the same original contract, not separate admissions.
5. The coordinator must adjudicate the combined mathematical/source
   records and explicitly admit the contract. This review recommends
   that action; it does not take it.
6. A complete paper still needs readable LaTeX and an actual PDF,
   substantive internal manuscript/source review, applicable pinned
   evaluation, and the workflow's final deterministic builds, visual
   inspection, exact payload/release checks and integration record.
   Reuse accepted proof checks on unchanged inputs; do not rerun
   mathematical work merely to fill a verification quota.

The theorem proves no target Euler factors, root numbers, automorphy,
zero/divisor correspondence or Hilbert–Pólya realization. Route B is
outside this task. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.

## Work receipt

Work comprised actual local proof/contract/review reads, bounded
primary-source browsing, independent symbolic reasoning, coordination
with X2, and read-only hash checks. No mathematical program, external
model/API, manuscript or PDF operation, formal evaluation, shared-state
edit, Git action, or additional review agent was used. The only new
workspace write is this assigned review file.

The research-review skill was applied in the repository's explicitly
authorized current-session internal mode; no older external-model
example was executed. Research-lit governed primary-source comparison,
and the repository batch workflow supplied the substantiality and
remaining-release gates.

**FINAL: MATHEMATICAL_GATE_PASS; ONE_SUBSTANTIAL_CONTRACT_RECOMMENDED;
SOURCE_CLAIM_NARROW_AND_ACCESS_LIMITED; COORDINATOR_SOURCE_ADJUDICATION
AND_PAPER_RELEASE_PENDING; ZERO_ADDITIONAL_PAPERS_FROM_COROLLARIES.**

## Targeted final-source readback

The coordinator subsequently supplied
[NOVELTY_CHECK_PC_L.md](../../NOVELTY_CHECK_PC_L.md). I read its complete
161-line version, SHA256
`29200483f461368496945b2107a0e4da48badf41726d53a3e8dc77441467ee7f`,
against the conditional source recommendation above. This is a bounded
readback of the newly completed gate, not another full proof-review loop.

**The source condition in this admission recommendation is satisfied.**
The synthesis includes the unrestricted equality-theorem comparison and
X2's narrower claims, explicitly subtracts the normal-form/residue/
Jacobian infrastructure and successive weighted-trace recurrences,
credits the LSY antecedent without pretending full-text access, and
retains the differences between exact arithmetic and approximate
smooth finite-data statements. Its safe positioning matches the
reviewed theorem and does not promote the iterate-degree bound into
an optimized-runtime claim. No required mathematical or source-wording
repair is identified in this final bounded package.

The synthesis's numerical novelty score is explicitly heuristic. I do
not use that score as evidence for admission; the exact theorem,
source-subtracted conclusion and substantiality reasoning above remain
the grounds. The LSY access limitation and the nonexhaustive search
coverage remain limitations, not a certificate excluding every possible
prior implication. Those limits are compatible with this internal
admission recommendation because they are disclosed and no universal
priority statement is made.

Accordingly, **recommend that the coordinator admit PC424-L as exactly
one substantial contract and proceed to its integrated manuscript**.
The coordinator's actual admission action and all completed-paper,
evaluation and release gates remain separate. No new paper is counted
or numbered by this readback, and no mathematical execution was run.

**UPDATED FINAL: MATHEMATICAL_GATE_PASS; BOUNDED_SOURCE_READBACK_PASS;
ONE_SUBSTANTIAL_CONTRACT_RECOMMENDED; ZERO_OPEN_REQUIRED_REPAIRS_IN_THIS
REVIEW; COORDINATOR_ADMISSION_AND_PAPER_RELEASE_PENDING;
NO_UNIVERSAL_PRIORITY_CLAIM; NO_BAD_EULER_OR_ROOT_NUMBER.**
