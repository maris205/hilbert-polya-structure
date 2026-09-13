# Paper 13 Independent Source-Lock Review — Round 2

**Date:** 2026-08-16 UTC  
**Candidate:** `henon_primitive_cycle_cover_v1`  
**Reviewed lock:** `experiments/source_lock.json`  
**Reviewed lock version:** 2  
**Exact reviewed lock SHA-256:**
`11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469`  
**Preserved v1 lock SHA-256:**
`61fed111b1948b8118481f4c0ffb6d2922b8b2bd3e8742cb8db8237a2646e19b`  
**Immutable Round-1 review SHA-256:**
`d9ba3def010fea36bf8d0613ad6ca2d66cb2c4f00e412bf582d069a023acbc06`  
**Canonical verdict:** `SOURCE_LOCK_PASS`

## 1. Independence, scope, and decision

I did not author the frozen Paper 13 files or the Round-1 review. I reviewed
the exact v2 artifact identified above, with special attention to the three
Round-1 repairs and possible regressions. This was a source-design review
only. I created no code, registered run, result, figure, manuscript, or scan.
This report is the sole write and uses the sole future-review path authorized
by the lock.

The v2 package closes all three Round-1 findings. Independent source and proof
checks found no theorem collision, no mathematical blocker, and no incorrect
change to the PC1/PC2 theorem chain. The exact strengthened two-parameter
package narrowly clears both requested gates:

- independent novelty score: **5.2/10**;
- independent standalone-size score: **5.1/10**.

The pass is narrow and is carried principally by PC1. PC2 is materially
incremental after the direct Morton comparison, but that narrower assessment
is now accurately disclosed throughout the v2 package.

## 2. Mechanical lock audit

All mechanical checks passed against the exact reviewed SHA.

| Check | Round-2 result |
|---|---|
| Strict JSON parse | PASS |
| Duplicate keys | none |
| Nonfinite numeric values | none |
| Current lock SHA-256 | exact match |
| Local design bindings | 16/16 SHA matches |
| Preserved Round-1 review binding | 1/1 SHA match |
| Upstream bindings | 6/6 SHA matches |
| Total bindings excluding the lock | 23/23 SHA matches |
| Declared line counts | all match |
| Planner/refinement freeze digest | exact match |
| Pre-review local inventory | 18 regular files |
| Symlinks | 0 |
| Unauthorized artifacts or directories | none |

The independently recomputed 11-file planner/refinement digest is

`157068cb2b0d4447ac45575cc255fd2d7ff778f1b5192dd53722012f7a678f10`.

The six line-counted normative/review documents match their declarations:
`RESEARCH_QUESTION.md` 363 lines, `NOVELTY_ASSESSMENT.md` 410,
`PROOF_PACKAGE.md` 821, `CLAIMS_EVIDENCE_MATRIX.md` 182,
`CITATION_VERIFICATION.md` 577, and the preserved Round-1 review 215.
The remaining bound local documents and every upstream artifact also match
their locked hashes.

Before this report was created, the Paper 13 directory contained exactly the
18 regular files declared by the v2 contract, in the three child directories
`experiments`, `notes`, and `refine-logs`. There were no symlinks and no code,
run, result, figure, or manuscript artifact or directory. The R2 report path
was absent before review.

The live normative state is consistently

`SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 / NO_CODE / NO_RESULTS`,

with `source_review_status` equal to
`PENDING_INDEPENDENT_R2_NOT_SELF_SIGNED`. Every implementation, execution,
result, figure, and manuscript authorization flag is false. The obsolete
`DESIGN_ONLY / NO_SOURCE_LOCK / ...` text survives only as quoted historical
evidence inside the immutable Round-1 review, not as a competing current-state
authority.

The preserved v1 hash appears identically in the current lock's previous-v1
field, its preserved-review binding, and the immutable Round-1 report. The
actual v1 lock bytes are not retained at a separate workspace path, so Round 2
can verify this archival hash chain but cannot recompute the v1 hash from a
second byte copy. That limitation is explicit and produces no inconsistency.
The Round-1 report itself is byte-verifiable at the exact SHA printed above.

## 3. Round-1 repair closure

### R1 — lifecycle propagation: fully addressed

The plan, tracker, five owned notes, normative refinement synthesis, and
current summaries now use the same v2 pending-review lifecycle. Historical
proposal and review material is either labeled non-normative or accompanied
by a normative post-R1 correction. No lifecycle regression was found.

### R2 — Morton (1996) direct scalar fixed-field generation: fully addressed

The primary source supports the repaired disclosure:

- Corollary 1 and the discussion on printed pp. 322–323 treat
  \(f_c(z)=z^d+c\), \(d\geq2\), at arbitrary fixed period and supply the
  all-degree multiplier-polynomial input.
- On printed p. 336, with \(K_0=\mathbb Q(c,z)\), Morton identifies
  \(K_0^{\langle\sigma\rangle}=\mathbb Q(c,w)\), where
  \(w=\prod_i f_c'(f_c^i(z))\). On the Paper 13 scalar fiber this is exactly
  \(w=\rho|_{a=0}\). Thus scalar \(\rho\)-generation is occupied for every
  fixed \(d,n\geq2\).
- Corollary 3 on printed p. 335 and the fixed-field statement on p. 336 give
  the orbit-sum generator
  \(t=\sum_i f_c^i(z)=\tau|_{a=0}\) in degree \(d=2\).
- The 2011 corrigendum repairs a later finite-characteristic lifting argument;
  it does not retract these characteristic-zero fixed-field statements.

The v2 research question, novelty assessment, proof package, claim matrix,
citation audit, plan, tracker, and refinement synthesis all disclose this
direct collision. They do not claim invention of scalar \(\rho\)-generation
for any \(d,n\), or scalar \(\tau\)-generation for \(d=2\). The residual PC2
delta is correctly limited to the two-parameter lift over
\(\mathbb Q(a,c)\), the uniform \(\tau\) proof including \(d\geq3\), and the
integral basis-free multiplication characteristic polynomials in \(A[T]\).

Primary locator: Patrick Morton, *On certain algebraic curves related to
polynomial maps*, [NUMDAM record](https://www.numdam.org/item/CM_1996__103_3_319_0/),
especially Corollaries 1 and 3 and printed pp. 322–323, 335–336. The
[2011 corrigendum](https://doi.org/10.1112/S0010437X1000480X) has the bounded
scope stated above.

### R3 — Cantat–Dujardin trace-spectrum rigidity: fully addressed

The primary source confirms the repaired object and theorem scopes:

- Section 3.1 constructs formal-period points with their scheme/intersection
  multiplicities.
- Section 3.2 defines the regular formal-period trace multiset
  \(\operatorname{Trace}_n(f)\), of length \(p_n\), from the pointwise values
  \(\operatorname{tr}(D_zf^n)\).
- Theorem A gives finite ambiguity for a single normalized complex Hénon map
  from the full trace spectrum; no fixed-Jacobian qualification is needed for
  the single-map space \(H_d^1\).
- Theorem 3.7 supplies finite \(P,N\) depending on the degree or multidegree,
  extends to algebraically closed characteristic-zero fields, and uses the
  fixed multi-Jacobian parameter space for compositions.

The v2 package preserves formal period, multiplicities, pointwise derivative
trace, the finite-period/finite-ambiguity conclusion, and the composition
qualification. It also states the correct noncollision boundary:
Cantat–Dujardin use whole formal-period trace multisets across several periods
to recover map parameters up to finite ambiguity; PC2 fixes one actual period
and asks whether one cycle value generates the degree-\(r\) cycle function
field. Neither theorem implies the other.

Primary locator: Cantat–Dujardin, *Multiplier rigidity for complex Hénon
maps*, [arXiv:2603.09445v1](https://arxiv.org/abs/2603.09445v1), Section 3 and
Theorems A/3.7. At the 2026-08-16 cutoff this remains v1; Ji–Xie
arXiv:2607.12561 is v2, revised 2026-07-18.

### Citation gates, nonclaims, and score history: fully addressed

The updated claim-to-source map assigns no individual novelty credit to
dynatomic machinery, Gröbner freeness, normalization, Reynolds operators,
scalar wreath monodromy, orbit sums, trace coordinates, determinant-line
characteristic polynomials, or generic primitive-element methods. It also
locks the low-period Endler–Gallas/Zhang observable collisions and distinguishes
Morton 1998's wreath theorem from the unrelated displayed Theorem D in Morton
1996.

Historical assessments remain separate and unaveraged:

- adjudicated GO: novelty 6.8/10, standalone size 7.4/10, proof confidence
  0.74;
- preserved dissent: STOP, novelty 4.5/10, standalone size 3.9/10;
- corrected author-side/R1-informed risk ranges: novelty 4.8–5.5/10 and size
  4.5–5.5/10.

The last pair is explicitly nonconsensus and does not overwrite either
historical judgment. The bounded no-hit is not promoted into a claim of
priority, universal absence, or method novelty.

## 4. Independent proof and source audit

No theorem blocker and no v2 proof regression was found.

| Claim group | Result | Round-2 finding |
|---|---|---|
| C2 | PASS | Monic coefficient-ring Gröbner reduction gives the \(d^n\) standard-monomial basis. |
| C3–C5 | PASS | Generic étaleness, the actual-period idempotent, Henselian scalar lift, and connected-field identification are correctly linked. |
| C7 | PASS | Excellence/Nagata finiteness, normal-surface Cohen–Macaulayness, dimension equality, and miracle flatness give finite local freeness of rank \(\nu\). |
| C8–C9 | PASS | The unique \(a\)-adic prime, \(e=1\), multiplicity-one divisor, \(R_0+S_1\) reducedness, and normal finite-birational comparison give exactly \(S/aS=D_n\). |
| C10 | PASS | Constants inject into \(\operatorname{Frac}(D_n)\), giving regularity and geometric integrality. |
| C12–C13 | PASS | The Reynolds idempotent is a split summand, so invariants commute with arbitrary base change and give the exact affine quotient fiber. |
| C14 | PASS | The scalar geometric wreath source, special-to-global \(\pi_1\) direction, centralizer upper bound, and \(S_r\) cycle quotient are correct. |
| C16–C17 | PASS | The \(\tau\) word-sum and \(\rho\) inverse-product comparisons are genuinely separate and cover all nontrivial cases. |
| C18 | PASS | Proper stabilizers containing \(S_{r-1}\) equal \(S_{r-1}\), yielding separate primitive generation. |
| C19 | PASS | The determinant-line construction is basis-free and generic primitivity makes the degree-\(r\) characteristic polynomials irreducible. |
| C20 | PASS | The complete \((d,n)=(2,2)\) formulas and degree-one boundary check directly. |

Fakhruddin's Theorem 3.2 explicitly restates Morton 1998, Theorem 10, over an
arbitrary characteristic-zero field and gives the product of wreath groups.
Taking the constant field to be \(\overline{\mathbb Q}\) supplies the geometric
exact-period factor \(C_n\wr S_r\). The proof then uses the correctly directed
map from the scalar good line's geometric fundamental group into the global
good open and the global centralizer bound. See the
[primary Fakhruddin source](https://msp.org/ant/2014/8-3/ant-v8-n3-p03-s.pdf),
Theorem 3.2. Gao–Ou's result is used only for the smooth geometrically integral
affine scalar dynatomic curve, consistent with its
[published scope](https://arxiv.org/abs/1304.4751).

The exact Stacks Project tags locked for excellence, Nagata normalization,
normal surfaces, miracle flatness, Henselian finite-étale lifting,
ramification/residue degrees, normality, constants, geometric reducedness,
and geometric integrality were individually checked and match their assigned
roles.

### A resolved false-positive concern at C10

`PROOF_PACKAGE.md:371–373` says that

\[
E_n\otimes_{\mathbb Q}\overline{\mathbb Q}
\]

is a field. This stronger wording is correct, not a source-lock defect. The
preceding constants argument and characteristic zero make
\(E_n/\mathbb Q\) regular. For every finite
\(L/\mathbb Q\) inside \(\overline{\mathbb Q}\), regularity gives linear
disjointness, so \(E_n\otimes_{\mathbb Q}L\) is a domain. It is also a
finite-dimensional algebra over the field \(E_n\), hence is itself a field.
Every element of the tensor product with \(\overline{\mathbb Q}\), and the
inverse of every nonzero element, lies in one such finite stage. The directed
union is therefore a field. Transcendence degree two does not invalidate the
statement; for example,
\(\mathbb Q(t)\otimes_{\mathbb Q}\overline{\mathbb Q}
=\overline{\mathbb Q}(t)\).

Thus no `field`-to-`domain` repair is required, and C10 and all downstream
claims pass as written.

The separate v1 proof bytes are not available for a bytewise proof diff.
Semantic comparison against the immutable Round-1 theorem audit, the v2
theorem lock, and every required C-claim found that the lifecycle/literature
repairs did not change PC1/PC2 mathematics incorrectly.

## 5. Independent novelty and standalone-size decision

### Novelty: 5.2/10 — clears the 5/10 gate narrowly

No located source states the exact strengthened conjunction. The residual
novelty is concentrated in PC1: the relative normalization of the generic
actual-period field across the degenerating scalar line, exact reduced
scheme-theoretic scalar fiber with hidden nilpotents excluded, affine cyclic
quotient, and coherent two-parameter primitive-cycle cover are not found
together in the checked literature.

This score does not credit the standard algebraic machinery or imported scalar
monodromy. It also gives little independent credit to PC2: Morton already
occupies scalar \(\rho\)-generation for all \(d,n\) and scalar
\(\tau\)-generation for \(d=2\). PC2's remaining contribution is the
two-parameter lift, the \(d\geq3\) uniform \(\tau\) treatment, and integration
with PC1 plus integral characteristic polynomials. PC2 alone would not clear
the novelty gate; the exact PC1+PC2 package does.

### Standalone size: 5.1/10 — clears the 5/10 gate narrowly

The full package has enough theorem mass as a self-contained short paper
because PC1 requires a nontrivial chain from coefficient-ring freeness through
Henselian block identification, finite-flat normalization, exact
scheme-theoretic special fiber, quotient base change, and geometric monodromy,
with PC2 adding two separate primitive-coordinate arguments and integral
polynomials. It is nevertheless close to the threshold because several tools
and the decisive scalar wreath input are imported and PC2 is substantially
incremental.

If PC1's exact-fiber or finite-flat-normalization bridge had failed, both
scores would fall below five. The independent proof audit found that those
bridges survive, so the exact locked conjunction clears both gates.

No target venue was supplied, so the only valid venue status is
`criteria_binding_unavailable`; these are source-design scores, not a venue-fit
or acceptance prediction.

## 6. Limitations and gate

The literature audit was bounded through 2026-08-16. A no-hit result is not
proof of historical priority or universal absence. No cross-model Phase C was
available or simulated, so same-model-family correlated-error risk remains.
Those limitations are already accurately disclosed in the v2 package.

This verdict binds only the exact source-lock SHA
`11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469`.
It authorizes no code, registered execution, result, figure, or manuscript by
itself; any later lifecycle transition remains governed by the package and
batch authorities.

**Final canonical verdict: `SOURCE_LOCK_PASS`.**
