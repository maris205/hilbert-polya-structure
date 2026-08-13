# Independent Manuscript Review — Round 1

**Paper:** *Finite Arithmetic Capacity under Additive Locally Constant,
Good-Reduction Multiplier, and Algebraic-Action Readouts*  
**Review date:** 2026-08-14  
**Reviewed source SHA-256:**
`10dec98b3c36c03c168f2f47aa77ddf95f790b3084c38149d8ea6cdb9b9ba1b8`  
**Reviewed pre-review PDF SHA-256:**
`1be29012762238bd469a2b5e86cbc32a76e9c951ed6e524917c99bf05c0a2810`  
**Independence statement:** I did not author or revise the manuscript, source
lock, code, official results, figures, or citation package.  The only file
created in this round is this review.  I did not inspect prime tables or
Riemann-zero data and did not execute a candidate search.

## Verdict

**PASS_WITH_MINORS**

**Overall score:** 8.4/10  
**Confidence:** 0.94  
**Mathematical status of the main theorem:** `PROVABLE AS STATED`

The additive rank-plus-support theorem is correct under the displayed
positive-real-log, common-$V$, common-$S_{\mathbb Q}$, and real-algebraic
assumptions.  The paper's main advance is a clean mixed-source certificate,
not a new component theorem in transcendence theory, symbolic dynamics, or
arithmetic H\'enon dynamics.  The manuscript is unusually careful about this
scope, makes the selector result only a corollary, and treats Deninger and
Connes--Consani as positive architectures outside the certificate.  I found no
major mathematical, evidentiary, novelty-positioning, or reproducibility
defect.  The bounded changes below should be made before finalization.

## Scores

| Dimension | Score | Assessment |
|---|---:|---|
| Correctness and proof completeness | 9.1/10 | Main theorem and L/A certificates close; Class M needs one scheme-theoretic sentence repaired, but its conclusion and repair are standard. |
| Significance | 7.5/10 | Useful finite-capacity design theorem and audit framework, with deliberately narrow exact-equality scope. |
| Novelty | 6.3/10 | Moderate synthesis/certificate novelty; low novelty for the individual ingredients. |
| Scope discipline | 9.5/10 | Universal no-go, complete-trichotomy, sufficiency, priority, approximate, and Riemann-zero claims are explicitly excluded. |
| Evidence and reproducibility | 9.7/10 | Exact hashes, frozen provenance, nine gates, 51 tests, and zero-execution counters cross-close. |
| Writing and visual presentation | 8.6/10 | Clear, compact, and visually sound; one float placement and one optimality phrase merit polish. |

## Mathematical audit

### 1. Additive theorem — PASS

The proof has the correct sign and quantifier structure.  From

$$
\log p_i=v_{p_i}+\log q_{p_i}+\alpha_{p_i}
$$

and an integer relation $\sum_i m_i v_{p_i}=0$, it obtains

$$
\log\!\left(\frac{\prod_i p_i^{m_i}}
{\prod_i q_{p_i}^{m_i}}\right)
=\sum_i m_i\alpha_{p_i}.
$$

The left exponential argument is positive algebraic and the right side is
real algebraic.  Hermite--Lindemann therefore forces the latter to be zero
and the former to be one.  Squaring before taking valuations is the correct
way to use only the certified objects $q_{p_i}^2$.  In one common number field,
a place above each distinct $p_i\notin S_{\mathbb Q}$ sees zero valuation on
every $S_{\mathbb Q}$-unit and every other rational prime, so it forces
$m_i=0$.  Thus every finite outside-support family $\{v_p\}$ is rationally
independent, which gives the bound and also disposes of a possibly infinite
hit set.

The manuscript correctly handles denominator clearing, negative exponents,
$q=1$, repeated hits, arbitrary one-certificate-per-prime selection, and the
real rather than complex logarithm.  Lemma 3.3 also correctly handles rational
powers: adjoining positive algebraic roots is finite, and the identity
$(q^2)^D=\prod_j(q_j^2)^{m_j}$ forces zero outside-support valuations even
when some $m_j$ are negative.

### 2. Class L — PASS

The higher-block reduction is sufficient.  An observable with fixed finite
memory on a finite alphabet becomes an edge observable on a finite graph, so
all periodic sums lie in the rational span of finitely many edge values.  The
paper correctly excludes general H\"older roofs and does not require the edge
values themselves to be algebraic.

### 3. Class M — PASS AFTER MINOR EXPOSITION REPAIR

The recurrence, separate-degree homogenization, non-Archimedean maximum, and
monodromy-unit argument are sound.  At infinity the monic term forces every
cyclic coordinate to vanish, leaving no projective point.  At a good finite
place a maximal norm $R>1$ makes the leading term uniquely dominant with norm
$R^d>R$, contradicting the two-neighbor bound.  Integral derivative factors
and integral inverses make both return eigenvalues local units.  Passing to a
normal field and saturating all places over $S_{\mathbb Q}$ legitimizes
complex conjugation and proves that
$|\lambda|^2=\lambda\overline\lambda$ is an $S_{\mathbb Q}$-unit; the paper
correctly avoids the false shortcut
$\overline\lambda=\lambda^{-1}$.

The conclusion that the cyclic scheme is zero-dimensional is correct, but the
appendix sentence that every connected proper affine component has "only
constant global functions" is not literally correct for a nonreduced scheme:
a zero-dimensional proper affine thickening can have nonconstant nilpotent
global sections.  This is a local exposition defect, not a failed theorem.
The standard proper-plus-affine finiteness lemma repairs it immediately.

### 4. Class A and gauge ledger — PASS

Regular evaluation of a $\overline{\mathbb Q}$-rational potential on an
algebraic finite orbit is algebraic, as are the declared real-valued algebraic
operations.  The stepwise gauge formula telescopes to both endpoint terms and
all constants with the correct signs.  The manuscript correctly distinguishes
preservation of algebraicity from canonical gauge invariance, the latter
requiring endpoint compatibility, and excludes poles, multivalued gauges,
closed non-exact changes, transcendental constants, and log-after-action.

### 5. Selector and escape statements — PASS

The three selector embeddings are direct special cases of the additive
normal form.  The escape corollary is used only contrapositively inside the
declared certificate.  The text repeatedly and correctly says that the four
failures can overlap, need not exhaust arbitrary dynamics, and are not
sufficient for arithmetic provenance.

## Novelty and literature boundary

The defensible novelty level is **moderate synthesis/certificate novelty**.
The documented search did not locate the same mixed theorem, but this is not
an exhaustive priority proof, and the manuscript wisely makes no firstness
claim.  The finite-rank symbolic observation, good-reduction/unit mechanisms,
regular algebraic evaluation, Hermite--Lindemann, and valuation isolation are
classical or elementary in their respective settings; the contribution is
their precise additive coupling, rank-plus-support count, source-class ledger,
and falsifiable implementation boundary.

The positive boundary is appropriately prominent.  Deninger's arithmetic-
scheme systems and the Connes--Consani scaling/ad\`ele architectures are
presented as intrinsic arithmetic constructions outside the finite L/M/A
certificate, not as evidence that this paper proves a universal obstruction.
Berry--Keating and Connes are used only as motivation and spectral context.
All 18 bibliography records are cited, no cited key is missing, and no
bibliography entry is unused.

## Evidence, figures, build, and visual audit

I independently reproduced the manuscript's central artifact checks:

- official result:
  `9f9878247dc821d15b503abe5a3df713d5bde0f3c76690493dc1b4a98091ace4`;
- registered-run record:
  `4ebec117a2254dc4502c7afd4094e833bc751b8a7e3bffcc16496dd0fd0ea5e3`;
- exclusive result manifest:
  `21d6910ec1e8e2995d4141f264dce06902f7d1787dea6f28d82346ebd54e3d79`;
- source lock:
  `2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc`;
- reviewed tree:
  `10fd57b1f99616799f05c3b6a4ce11a9e8ea747d33bb50299aac618948482fb7`;
- JUnit:
  `34915053371701fafd147dd39986b7a5eb157ff09c44f425edfd88f0a8ac17da`.

The JSON records agree on `CAPACITY_BOUND_CERTIFIED`, all nine gates passing,
20 proof IDs, 10 admitted and 9 excluded operations, 6 controls, 12 scanned
executables with zero findings, two terminal upstream packages, one
registered static run, 51 passing tests, zero numerical candidate runs, and
zero target matches.  Prime-table, target-array, numerical-logarithm, and
Riemann-zero flags are all false.  The paper properly treats this as proof-
dependency and provenance evidence, not as a computational proof of the
mathematics.

The three figures load only the five declared frozen machine-readable inputs.
Their PDF/SVG/PNG hashes match the reproducibility record across two complete
generations.  Original-resolution inspection of all three figures and all 11
PDF pages found no clipping, overlap, unreadable label, or rasterization
problem.  The final log has no LaTeX, reference, citation, or box warning, and
all PDF fonts are embedded and subset.

## Required minor revisions

### M1. Repair the projective-affine scheme sentence

**Location:** Section 5.2 and Appendix B.1, especially "Each connected proper
affine component has only constant global functions and is zero-dimensional."

**Action:** Replace that sentence by a scheme-valid statement, for example:

> After base change to an algebraic closure, the projective cyclic scheme has
> no point on the hyperplane at infinity, hence is both proper and affine.  A
> finite-type affine scheme proper over a field is finite over that field;
> therefore its support is zero-dimensional and the cyclic scheme is finite.

Equivalently, state the argument for the reduced irreducible components and
then note that a finite-type scheme with zero-dimensional support is Artinian.
A conventional citation for the proper-affine finiteness lemma would further
reduce reviewer friction.

### M2. Qualify or demonstrate "sharp"

**Location:** Abstract ("sharp capacity bound") and Remark 4.2.

**Action:** Either replace "sharp" in the abstract by "rank-plus-support," or
give one explicit formal construction attaining the full
$\dim_{\mathbb Q}V+|S_{\mathbb Q}|$ count: use $r$ independent inserted
outside-prime labels for the $V$ contribution and one supported multiplier
label for every prime in $S_{\mathbb Q}$.  In the same sentence, preserve the
important distinction that such a construction shows optimality of the
abstract hypotheses but is target injection, not arithmetic emergence.
Also say explicitly that target independence is a provenance condition rather
than a step needed by the linear-independence proof.

## Optional presentation polish

Table 1 belongs to Section 2 but floats to the top of page 4 after Section 3
has begun.  Moving it earlier or constraining its placement would improve
narrative continuity; this does not affect the verdict.

## Final recommendation

Accept the mathematical and evidentiary package after the two bounded minor
revisions above.  No new experiment, target computation, theorem weakening,
source-lock change, or additional novelty claim is required.  A fresh Round-2
review should verify only M1, M2, the rebuilt PDF, and the corresponding
retrospective integrity indexes.
